// Web Speech API text-to-speech helper

let currentUtterance = null;

export const speakText = (text, options = {}) => {
  if (!('speechSynthesis' in window)) {
    console.warn('Web Speech API text-to-speech is not supported in this browser.');
    return;
  }

  stopSpeech();

  if (!text) return;

  const utterance = new SpeechSynthesisUtterance(text);
  utterance.rate = options.rate || 0.95; // slightly slower for clear accessibility
  utterance.pitch = options.pitch || 1.0;
  utterance.volume = options.volume || 1.0;

  if (options.onEnd) {
    utterance.onend = options.onEnd;
  }
  if (options.onError) {
    utterance.onerror = options.onError;
  }

  currentUtterance = utterance;
  window.speechSynthesis.speak(utterance);
};

export const stopSpeech = () => {
  if ('speechSynthesis' in window) {
    window.speechSynthesis.cancel();
    currentUtterance = null;
  }
};

export const isSpeaking = () => {
  return 'speechSynthesis' in window && window.speechSynthesis.speaking;
};
