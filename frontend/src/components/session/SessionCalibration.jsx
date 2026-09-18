import React, { useState } from 'react';
import { Camera, CameraOff, Sparkles, Check, ArrowRight, ShieldCheck, Heart } from 'lucide-react';
import { initWebGazer } from '../../services/webgazerService';
import AudioButton from '../common/AudioButton';

const SessionCalibration = ({ onCalibrationComplete }) => {
  const [step, setStep] = useState(0); // 0: Camera Choice, 1: Target Clicks, 2: Complete
  const [useCamera, setUseCamera] = useState(false);
  const [clickCount, setClickCount] = useState(0);
  const [loading, setLoading] = useState(false);

  const targets = [
    { top: '25%', left: '20%', label: 'Star 1' },
    { top: '50%', left: '75%', label: 'Star 2' },
    { top: '70%', left: '40%', label: 'Star 3' }
  ];

  const handleCameraChoice = async (enableCam) => {
    setUseCamera(enableCam);
    setLoading(true);

    if (enableCam) {
      const success = await initWebGazer();
      if (!success) {
        console.warn('WebGazer init failed or permission denied. Proceeding in non-camera mode.');
        setUseCamera(false);
      }
    }

    setLoading(false);
    setStep(1); // Move to click target calibration
  };

  const handleTargetClick = () => {
    const nextCount = clickCount + 1;
    setClickCount(nextCount);
    if (nextCount >= targets.length) {
      setStep(2);
      setTimeout(() => {
        onCalibrationComplete({ useCamera });
      }, 1200);
    }
  };

  return (
    <div className="fixed inset-0 z-50 bg-slate-900/90 backdrop-blur-md flex items-center justify-center p-4">
      <div className="bg-white rounded-3xl p-6 sm:p-8 max-w-lg w-full shadow-2xl border border-slate-200 text-slate-800 space-y-6 animate-fadeIn">
        
        {/* Header */}
        <div className="text-center space-y-2">
          <div className="w-12 h-12 rounded-2xl bg-indigo-600 text-white mx-auto flex items-center justify-center shadow-md">
            <Sparkles className="w-6 h-6 fill-current" />
          </div>
          <h2 className="text-2xl font-extrabold tracking-tight text-slate-900">
            Let's Get Ready!
          </h2>
          <p className="text-xs text-slate-500 font-medium">
            Short, low-pressure calibration to prepare your learning space.
          </p>
        </div>

        {/* STEP 0: CAMERA PERMISSION CHOICE */}
        {step === 0 && (
          <div className="space-y-5 animate-fadeIn">
            <div className="bg-slate-50 p-4 rounded-2xl border border-slate-200 space-y-2">
              <div className="flex items-center justify-between">
                <span className="text-xs font-bold text-indigo-700 uppercase tracking-wider flex items-center gap-1.5">
                  <ShieldCheck className="w-4 h-4 text-indigo-600" /> Privacy First
                </span>
                <AudioButton
                  text="We can use your camera locally in your browser to check where you look. No video or images are stored or sent anywhere."
                  label="Listen Info"
                />
              </div>
              <p className="text-xs text-slate-600 leading-relaxed font-medium">
                We use WebGazer to process gaze position <strong>100% locally in your browser</strong>. No raw video or images are recorded, stored, or sent to any server.
              </p>
            </div>

            <div className="space-y-3">
              <button
                type="button"
                onClick={() => handleCameraChoice(true)}
                disabled={loading}
                className="w-full p-4 rounded-2xl border-2 border-indigo-600 bg-indigo-50/70 hover:bg-indigo-100 text-indigo-950 font-bold text-sm transition-all flex items-center justify-between shadow-sm"
              >
                <div className="flex items-center gap-3">
                  <Camera className="w-5 h-5 text-indigo-600" />
                  <div className="text-left">
                    <div>Allow Camera Gaze Assist</div>
                    <div className="text-[11px] text-slate-500 font-normal">Enables focus assistance</div>
                  </div>
                </div>
                <ArrowRight className="w-4 h-4 text-indigo-600" />
              </button>

              <button
                type="button"
                onClick={() => handleCameraChoice(false)}
                disabled={loading}
                className="w-full p-4 rounded-2xl border border-slate-300 bg-white hover:bg-slate-50 text-slate-700 font-bold text-sm transition-all flex items-center justify-between"
              >
                <div className="flex items-center gap-3">
                  <CameraOff className="w-5 h-5 text-slate-400" />
                  <div className="text-left">
                    <div>Continue without Camera</div>
                    <div className="text-[11px] text-slate-500 font-normal">Uses non-camera telemetry (mouse & timing)</div>
                  </div>
                </div>
                <ArrowRight className="w-4 h-4 text-slate-400" />
              </button>
            </div>
          </div>
        )}

        {/* STEP 1: TARGET CLICK CALIBRATION */}
        {step === 1 && (
          <div className="space-y-4 text-center animate-fadeIn py-4">
            <p className="text-sm font-bold text-slate-800">
              Click the glowing star to calibrate your pointer! ({clickCount + 1} / {targets.length})
            </p>

            <div className="relative h-48 bg-slate-100 rounded-2xl border border-slate-200 overflow-hidden">
              {targets.map((tgt, idx) => {
                if (idx !== clickCount) return null;
                return (
                  <button
                    key={idx}
                    type="button"
                    onClick={handleTargetClick}
                    style={{ top: tgt.top, left: tgt.left }}
                    className="absolute -translate-x-1/2 -translate-y-1/2 p-3.5 rounded-2xl bg-amber-400 text-amber-950 shadow-md ring-4 ring-amber-300/60 hover:scale-110 active:scale-95 transition-all cursor-pointer"
                    title="Click star to calibrate"
                  >
                    <Sparkles className="w-6 h-6 fill-current" />
                  </button>
                );
              })}
            </div>

            <div className="pt-2 flex justify-center">
              <button
                type="button"
                onClick={() => onCalibrationComplete({ useCamera })}
                className="text-xs font-semibold text-slate-400 hover:text-slate-700 underline transition-colors"
              >
                Skip Calibration & Enter Quest
              </button>
            </div>
          </div>
        )}

        {/* STEP 2: COMPLETE */}
        {step === 2 && (
          <div className="text-center py-6 space-y-3 animate-fadeIn">
            <div className="w-14 h-14 rounded-full bg-emerald-100 text-emerald-600 mx-auto flex items-center justify-center font-bold">
              <Check className="w-8 h-8" />
            </div>
            <h3 className="text-xl font-extrabold text-slate-900">Calibration Complete!</h3>
            <p className="text-xs text-slate-500 font-semibold">
              Entering your personalized learning quest space...
            </p>
          </div>
        )}

      </div>
    </div>
  );
};

export default SessionCalibration;
