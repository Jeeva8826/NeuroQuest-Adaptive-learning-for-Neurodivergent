import React, { createContext, useContext, useState, useEffect } from 'react';
import { getLearnerProfile, updateLearnerPreferences } from '../services/api';
import { useAuth } from './AuthContext';

const ThemeContext = createContext();

const PALETTE_THEMES = {
  soft: { bg: '#f8fafc', card: '#ffffff', text: '#0f172a', muted: '#64748b' },
  bright: { bg: '#f0f9ff', card: '#ffffff', text: '#0c4a6e', muted: '#0284c7' },
  dark: { bg: '#0f172a', card: '#1e293b', text: '#f8fafc', muted: '#94a3b8' },
  high_contrast: { bg: '#ffffff', card: '#f1f5f9', text: '#000000', muted: '#334155' },
  minimal: { bg: '#fafafa', card: '#ffffff', text: '#18181b', muted: '#71717a' }
};

export const ThemeProvider = ({ children }) => {
  const { user, hasCompletedOnboarding } = useAuth();
  
  const [profile, setProfile] = useState(null);
  const [primaryColor, setPrimaryColor] = useState('#3b82f6');
  const [secondaryColor, setSecondaryColor] = useState('#8b5cf6');
  const [paletteType, setPaletteType] = useState('soft');
  const [backgroundTheme, setBackgroundTheme] = useState('space');
  const [fontFamily, setFontFamily] = useState('rounded');
  const [fontScale, setFontScale] = useState('medium');
  const [animationIntensity, setAnimationIntensity] = useState('normal');
  const [soundEnabled, setSoundEnabled] = useState(false);
  const [visualDensity, setVisualDensity] = useState('spacious');

  useEffect(() => {
    if (user && hasCompletedOnboarding) {
      loadProfileTheme();
    }
  }, [user, hasCompletedOnboarding]);

  const loadProfileTheme = async () => {
    try {
      const res = await getLearnerProfile();
      const p = res.data;
      setProfile(p);
      
      const vis = p.visual_preferences || {};
      const sen = p.sensory_preferences || {};
      
      if (vis.primary_color) setPrimaryColor(vis.primary_color);
      if (vis.secondary_color) setSecondaryColor(vis.secondary_color);
      if (vis.palette_type) setPaletteType(vis.palette_type);
      if (vis.background_theme) setBackgroundTheme(vis.background_theme);
      if (vis.font_family) setFontFamily(vis.font_family);
      if (vis.font_scale) setFontScale(vis.font_scale);
      
      if (sen.animation_intensity) setAnimationIntensity(sen.animation_intensity);
      if (sen.sound_enabled !== undefined) setSoundEnabled(sen.sound_enabled);
      if (sen.visual_density) setVisualDensity(sen.visual_density);

      applyThemeVariables({
        primary: vis.primary_color || '#3b82f6',
        secondary: vis.secondary_color || '#8b5cf6',
        palette: vis.palette_type || 'soft',
        scale: vis.font_scale || 'medium',
        anim: sen.animation_intensity || 'normal'
      });
    } catch (err) {
      console.warn('Could not load learner theme profile:', err);
    }
  };

  const applyThemeVariables = ({ primary, secondary, palette, scale, anim }) => {
    const root = document.documentElement;
    const colors = PALETTE_THEMES[palette] || PALETTE_THEMES.soft;

    root.style.setProperty('--color-primary', primary);
    root.style.setProperty('--color-secondary', secondary);
    root.style.setProperty('--bg-main', colors.bg);
    root.style.setProperty('--bg-card', colors.card);
    root.style.setProperty('--text-main', colors.text);
    root.style.setProperty('--text-muted', colors.muted);

    // Font Scale
    let scaleVal = '1';
    if (scale === 'large') scaleVal = '1.125';
    if (scale === 'xlarge') scaleVal = '1.25';
    if (scale === 'small') scaleVal = '0.9';
    root.style.setProperty('--font-scale', scaleVal);

    // Animation intensity
    if (anim === 'none') {
      document.body.classList.add('motion-reduce');
    } else {
      document.body.classList.remove('motion-reduce');
    }
  };

  const updatePreferences = async (newPrefs) => {
    try {
      const res = await updateLearnerPreferences(newPrefs);
      const updated = res.data;
      setProfile(updated);
      
      const vis = updated.visual_preferences || {};
      const sen = updated.sensory_preferences || {};

      if (newPrefs.primary_color) setPrimaryColor(newPrefs.primary_color);
      if (newPrefs.secondary_color) setSecondaryColor(newPrefs.secondary_color);
      if (newPrefs.background_theme) setBackgroundTheme(newPrefs.background_theme);
      if (newPrefs.font_family) setFontFamily(newPrefs.font_family);
      if (newPrefs.font_scale) setFontScale(newPrefs.font_scale);
      if (newPrefs.palette_type) setPaletteType(newPrefs.palette_type);
      if (newPrefs.animation_intensity) setAnimationIntensity(newPrefs.animation_intensity);

      applyThemeVariables({
        primary: vis.primary_color || primaryColor,
        secondary: vis.secondary_color || secondaryColor,
        palette: vis.palette_type || paletteType,
        scale: vis.font_scale || fontScale,
        anim: sen.animation_intensity || animationIntensity
      });
      return updated;
    } catch (err) {
      console.error('Failed to update preferences:', err);
      throw err;
    }
  };

  return (
    <ThemeContext.Provider
      value={{
        profile,
        primaryColor,
        secondaryColor,
        paletteType,
        backgroundTheme,
        fontFamily,
        fontScale,
        animationIntensity,
        soundEnabled,
        visualDensity,
        updatePreferences,
        reloadTheme: loadProfileTheme
      }}
    >
      <div
        className={`min-h-screen transition-colors duration-300 ${
          fontFamily === 'dyslexic'
            ? 'font-dyslexic'
            : fontFamily === 'rounded'
            ? 'font-rounded'
            : 'font-sans'
        }`}
        style={{
          backgroundColor: PALETTE_THEMES[paletteType]?.bg || '#f8fafc',
          color: PALETTE_THEMES[paletteType]?.text || '#0f172a'
        }}
      >
        {children}
      </div>
    </ThemeContext.Provider>
  );
};

export const useTheme = () => useContext(ThemeContext);
