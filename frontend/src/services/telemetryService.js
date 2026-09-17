import { getGazeTelemetryMetrics } from './webgazerService';
import { evaluateTelemetry } from './api';

class TelemetryCollector {
  constructor() {
    this.sessionId = null;
    this.isTracking = false;
    this.intervalId = null;

    this.clicks = [];
    this.rapidClickCount = 0;
    this.lastClickTime = 0;

    this.lastMouseMoveTime = Date.now();
    this.idleDurationSec = 0;

    this.taskStartTime = Date.now();
    this.incorrectAttempts = 0;
    this.hintRequests = 0;
    this.currentDifficulty = 2;

    this.sessionStartTime = Date.now();
    this.onStateEvaluated = null;
  }

  startTracking(sessionId, onStateEvaluatedCallback) {
    this.sessionId = sessionId;
    this.isTracking = true;
    this.sessionStartTime = Date.now();
    this.taskStartTime = Date.now();
    this.onStateEvaluated = onStateEvaluatedCallback;

    this.attachEventListeners();

    // Evaluate telemetry every 5 seconds
    this.intervalId = setInterval(() => {
      this.flushTelemetryWindow();
    }, 5000);
  }

  stopTracking() {
    this.isTracking = false;
    if (this.intervalId) {
      clearInterval(this.intervalId);
      this.intervalId = null;
    }
    this.detachEventListeners();
  }

  attachEventListeners() {
    window.addEventListener('click', this.handleMouseClick);
    window.addEventListener('mousemove', this.handleMouseMove);
  }

  detachEventListeners() {
    window.removeEventListener('click', this.handleMouseClick);
    window.removeEventListener('mousemove', this.handleMouseMove);
  }

  handleMouseClick = (e) => {
    const now = Date.now();
    this.clicks.push(now);

    // Rapid frustrated clicking detection (2 clicks within < 350ms)
    if (now - this.lastClickTime < 350) {
      this.rapidClickCount += 1;
    }
    this.lastClickTime = now;
    this.lastMouseMoveTime = now;
  };

  handleMouseMove = () => {
    this.lastMouseMoveTime = Date.now();
  };

  recordIncorrectAttempt() {
    this.incorrectAttempts += 1;
  }

  recordHintRequest() {
    this.hintRequests += 1;
  }

  resetTaskTimer(difficulty = 2) {
    this.taskStartTime = Date.now();
    this.incorrectAttempts = 0;
    this.hintRequests = 0;
    this.currentDifficulty = difficulty;
  }

  async flushTelemetryWindow() {
    if (!this.isTracking || !this.sessionId) return;

    const now = Date.now();

    // 1. Calculate Idle Ratio in 5s window
    const idleMs = now - this.lastMouseMoveTime;
    const windowIdleSec = Math.min(idleMs / 1000, 5.0);
    const idleRatio = Math.round((windowIdleSec / 5.0) * 100) / 100;

    // 2. Click rate per minute
    const recentClicks = this.clicks.filter(t => now - t <= 60000).length;

    // 3. Response time
    const responseTimeSec = Math.round((now - this.taskStartTime) / 1000);
    const sessionDurationMins = Math.round(((now - this.sessionStartTime) / 60000) * 10) / 10;

    // 4. Gaze metrics from WebGazer
    const gazeMetrics = getGazeTelemetryMetrics();

    const payload = {
      session_id: this.sessionId,
      has_gaze: gazeMetrics.has_gaze,
      gaze_drift_std: gazeMetrics.gaze_drift_std,
      gaze_offscreen_ratio: gazeMetrics.gaze_offscreen_ratio,
      click_rate_per_min: recentClicks,
      rapid_click_count: this.rapidClickCount,
      idle_ratio: idleRatio,
      avg_response_time_sec: responseTimeSec,
      incorrect_attempt_count: this.incorrectAttempts,
      hint_request_count: this.hintRequests,
      session_duration_mins: sessionDurationMins,
      current_difficulty: this.currentDifficulty
    };

    try {
      const res = await evaluateTelemetry(payload);
      if (this.onStateEvaluated && res.data) {
        this.onStateEvaluated(res.data);
      }
    } catch (err) {
      console.warn('Telemetry evaluation warning:', err);
    } finally {
      // Reset window counters
      this.rapidClickCount = 0;
    }
  }
}

export const telemetryCollector = new TelemetryCollector();
