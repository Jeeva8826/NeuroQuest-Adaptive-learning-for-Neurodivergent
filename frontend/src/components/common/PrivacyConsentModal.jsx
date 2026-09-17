import React, { useState } from 'react';
import { ShieldCheck, Camera, Mic, EyeOff, Lock, CheckCircle, X } from 'lucide-react';

const PrivacyConsentModal = ({ isOpen, onClose, onSaveConsent }) => {
  const [cameraAllowed, setCameraAllowed] = useState(true);
  const [micAllowed, setMicAllowed] = useState(false);
  const [telemetryEnabled, setTelemetryEnabled] = useState(true);

  if (!isOpen) return null;

  const handleSave = () => {
    if (onSaveConsent) {
      onSaveConsent({ cameraAllowed, micAllowed, telemetryEnabled });
    }
    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 bg-slate-900/80 backdrop-blur-sm flex items-center justify-center p-4">
      <div className="bg-white rounded-3xl p-6 sm:p-8 max-w-lg w-full shadow-2xl space-y-6 animate-fadeIn relative border border-slate-200">
        <button
          onClick={onClose}
          className="absolute top-4 right-4 p-2 text-slate-400 hover:text-slate-700 rounded-full hover:bg-slate-100 transition-all"
        >
          <X className="w-5 h-5" />
        </button>

        {/* Modal Header */}
        <div className="text-center space-y-2">
          <div className="w-14 h-14 rounded-3xl bg-emerald-100 text-emerald-600 mx-auto flex items-center justify-center font-bold">
            <ShieldCheck className="w-7 h-7" />
          </div>
          <h3 className="text-2xl font-black text-slate-900">Privacy & Sensing Preferences</h3>
          <p className="text-xs text-slate-600 font-medium max-w-sm mx-auto">
            NeuroQuest processes gaze signals client-side in your browser. Raw video is <span className="font-extrabold text-slate-900">never recorded or uploaded</span>.
          </p>
        </div>

        {/* Privacy Guarantees */}
        <div className="bg-emerald-50/70 border border-emerald-200/80 p-4 rounded-2xl space-y-2 text-xs text-emerald-950 font-medium">
          <div className="flex items-center gap-2 font-bold text-emerald-800">
            <Lock className="w-4 h-4 text-emerald-600" />
            <span>Privacy-Conscious Safeguards:</span>
          </div>
          <ul className="space-y-1 text-[11px] list-disc list-inside text-emerald-900">
            <li>100% Client-Side WebGazer gaze feature extraction.</li>
            <li>No video feed leaves your local device.</li>
            <li>Disabling sensing allows full platform fallback functionality.</li>
          </ul>
        </div>

        {/* Sensing Controls */}
        <div className="space-y-3">

          <div className="flex items-center justify-between p-3.5 bg-slate-50 border border-slate-200 rounded-2xl">
            <div className="flex items-center gap-3">
              <div className="w-9 h-9 rounded-xl bg-indigo-100 text-indigo-600 flex items-center justify-center">
                <Camera className="w-5 h-5" />
              </div>
              <div>
                <div className="text-xs font-extrabold text-slate-900">Camera Gaze Telemetry</div>
                <div className="text-[10px] text-slate-500">Extracts subtle gaze drift in browser</div>
              </div>
            </div>
            <input
              type="checkbox"
              checked={cameraAllowed}
              onChange={(e) => setCameraAllowed(e.target.checked)}
              className="w-5 h-5 accent-indigo-600 rounded cursor-pointer"
            />
          </div>

          <div className="flex items-center justify-between p-3.5 bg-slate-50 border border-slate-200 rounded-2xl">
            <div className="flex items-center gap-3">
              <div className="w-9 h-9 rounded-xl bg-purple-100 text-purple-600 flex items-center justify-center">
                <Mic className="w-5 h-5" />
              </div>
              <div>
                <div className="text-xs font-extrabold text-slate-900">Voice Navigation Support</div>
                <div className="text-[10px] text-slate-500">Audio playback & voice commands</div>
              </div>
            </div>
            <input
              type="checkbox"
              checked={micAllowed}
              onChange={(e) => setMicAllowed(e.target.checked)}
              className="w-5 h-5 accent-indigo-600 rounded cursor-pointer"
            />
          </div>

          <div className="flex items-center justify-between p-3.5 bg-slate-50 border border-slate-200 rounded-2xl">
            <div className="flex items-center gap-3">
              <div className="w-9 h-9 rounded-xl bg-sky-100 text-sky-600 flex items-center justify-center">
                <EyeOff className="w-5 h-5" />
              </div>
              <div>
                <div className="text-xs font-extrabold text-slate-900">Non-Camera Interaction Fallback</div>
                <div className="text-[10px] text-slate-500">Use click speed & idle signals if camera is off</div>
              </div>
            </div>
            <input
              type="checkbox"
              checked={telemetryEnabled}
              onChange={(e) => setTelemetryEnabled(e.target.checked)}
              className="w-5 h-5 accent-indigo-600 rounded cursor-pointer"
            />
          </div>

        </div>

        <button
          onClick={handleSave}
          className="w-full py-3.5 rounded-2xl text-xs font-extrabold text-white bg-emerald-600 hover:bg-emerald-700 shadow-md transition-all flex items-center justify-center gap-2"
        >
          <CheckCircle className="w-4 h-4" />
          <span>Save Privacy & Sensing Settings</span>
        </button>
      </div>
    </div>
  );
};

export default PrivacyConsentModal;
