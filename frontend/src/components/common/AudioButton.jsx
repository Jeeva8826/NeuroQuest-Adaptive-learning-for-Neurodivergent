import React, { useState } from 'react';
import { Volume2, VolumeX, Square } from 'lucide-react';
import { speakText, stopSpeech, isSpeaking } from '../../services/speech';

const AudioButton = ({ text, label = 'Listen', className = '' }) => {
  const [playing, setPlaying] = useState(false);

  const handleToggle = () => {
    if (playing || isSpeaking()) {
      stopSpeech();
      setPlaying(false);
    } else {
      setPlaying(true);
      speakText(text, {
        onEnd: () => setPlaying(false),
        onError: () => setPlaying(false)
      });
    }
  };

  return (
    <button
      type="button"
      onClick={handleToggle}
      aria-label={playing ? 'Stop reading' : 'Read aloud'}
      title={playing ? 'Stop reading' : 'Read aloud'}
      className={`inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-semibold tracking-wide transition-all ${
        playing
          ? 'bg-rose-100 text-rose-700 hover:bg-rose-200 border border-rose-300'
          : 'bg-indigo-50 text-indigo-700 hover:bg-indigo-100 border border-indigo-200'
      } ${className}`}
    >
      {playing ? (
        <>
          <Square className="w-3.5 h-3.5 fill-current animate-pulse" />
          <span>Stop</span>
        </>
      ) : (
        <>
          <Volume2 className="w-4 h-4" />
          <span>{label}</span>
        </>
      )}
    </button>
  );
};

export default AudioButton;
