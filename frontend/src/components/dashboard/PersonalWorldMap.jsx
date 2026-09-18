import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Compass, Shield, Award, Cpu, BookOpen, Star, CheckCircle, Lock, Sparkles, ArrowRight } from 'lucide-react';

const PersonalWorldMap = ({ gameWorld, masteryTree }) => {
  const navigate = useNavigate();
  const [activeTab, setActiveTab] = useState('map'); // 'map', 'mastery', 'inventory'

  if (!gameWorld) return null;

  const worldName = gameWorld.world_name || "Personal Realm";
  const heroRole = gameWorld.hero_role || "Explorer";
  const activeZone = gameWorld.active_zone || "Station Dock";
  const explorationMap = gameWorld.exploration_map || [];
  const inventory = gameWorld.inventory || [];
  const masteryNodes = masteryTree?.nodes || [];

  return (
    <div className="bg-white rounded-3xl border border-slate-200/80 shadow-md overflow-hidden">
      {/* Header Banner */}
      <div className="bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white p-6 sm:p-8 border-b border-slate-800">
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
          <div className="space-y-1">
            <div className="flex items-center gap-2">
              <span className="px-3 py-1 bg-indigo-500/30 text-indigo-300 text-xs font-extrabold rounded-full border border-indigo-400/30 uppercase tracking-wider">
                Personal Game World
              </span>
              <span className="text-xs text-slate-400 font-medium">Hero: {heroRole}</span>
            </div>
            <h2 className="text-2xl font-black">{worldName}</h2>
            <p className="text-xs text-slate-300">Active Location: <span className="font-bold text-indigo-300">{activeZone}</span></p>
          </div>

          {/* Navigation Tabs */}
          <div className="flex bg-slate-800/80 p-1.5 rounded-2xl border border-slate-700/80 text-xs font-bold gap-1 self-stretch sm:self-auto justify-center">
            <button
              onClick={() => setActiveTab('map')}
              className={`px-4 py-2 rounded-xl transition-all flex items-center gap-1.5 ${
                activeTab === 'map' ? 'bg-indigo-600 text-white shadow-md' : 'text-slate-400 hover:text-white'
              }`}
            >
              <Compass className="w-4 h-4" />
              <span>Exploration Map</span>
            </button>

            <button
              onClick={() => setActiveTab('mastery')}
              className={`px-4 py-2 rounded-xl transition-all flex items-center gap-1.5 ${
                activeTab === 'mastery' ? 'bg-indigo-600 text-white shadow-md' : 'text-slate-400 hover:text-white'
              }`}
            >
              <Shield className="w-4 h-4" />
              <span>Mastery Tree</span>
            </button>

            <button
              onClick={() => setActiveTab('inventory')}
              className={`px-4 py-2 rounded-xl transition-all flex items-center gap-1.5 ${
                activeTab === 'inventory' ? 'bg-indigo-600 text-white shadow-md' : 'text-slate-400 hover:text-white'
              }`}
            >
              <Award className="w-4 h-4" />
              <span>Vault ({inventory.length})</span>
            </button>
          </div>
        </div>
      </div>

      {/* Tab Content */}
      <div className="p-6 sm:p-8">

        {/* 1. EXPLORATION MAP VIEW */}
        {activeTab === 'map' && (
          <div className="space-y-6">
            <div className="flex items-center justify-between">
              <h3 className="text-lg font-black text-slate-900 flex items-center gap-2">
                <Compass className="w-5 h-5 text-indigo-600" />
                World Zones & Sector Progression
              </h3>
              <span className="text-xs font-bold text-slate-400">Non-Competitive Self-Journey</span>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
              {explorationMap.map((zone, idx) => {
                const canEnter = zone.is_current || zone.is_unlocked;
                return (
                  <div
                    key={zone.id || idx}
                    onClick={() => {
                      if (canEnter) navigate('/session', { state: { zone: zone.name } });
                    }}
                    className={`p-5 rounded-2xl border transition-all flex flex-col justify-between space-y-4 ${
                      canEnter ? 'cursor-pointer hover:shadow-lg hover:scale-[1.02]' : 'cursor-not-allowed opacity-60'
                    } ${
                      zone.is_current
                        ? 'bg-indigo-50/90 border-indigo-300 ring-2 ring-indigo-500/20 shadow-md'
                        : zone.is_unlocked
                        ? 'bg-emerald-50/60 border-emerald-200'
                        : 'bg-slate-50 border-slate-200'
                    }`}
                    title={canEnter ? `Enter ${zone.name} Mission` : `${zone.name} is Locked`}
                  >
                    <div className="flex items-start justify-between">
                      <div className={`w-10 h-10 rounded-xl flex items-center justify-center font-bold text-white shadow-sm ${
                        zone.is_current ? 'bg-indigo-600' : zone.is_unlocked ? 'bg-emerald-500' : 'bg-slate-400'
                      }`}>
                        {zone.is_unlocked ? <CheckCircle className="w-5 h-5" /> : <Lock className="w-5 h-5" />}
                      </div>
                      <span className="text-[10px] font-extrabold px-2.5 py-1 rounded-full uppercase tracking-wider bg-white/80 text-slate-600 border border-slate-200/80">
                        Sector {idx + 1}
                      </span>
                    </div>

                    <div className="space-y-1">
                      <h4 className="font-extrabold text-sm text-slate-900">{zone.name}</h4>
                      <p className="text-xs text-slate-500 line-clamp-2">{zone.description}</p>
                    </div>

                    <div className="pt-2 flex items-center justify-between border-t border-slate-100/80">
                      <span className="text-[11px] font-bold text-slate-400">
                        {zone.is_current ? '📍 Active Sector' : zone.is_unlocked ? '✨ Unlocked' : '🔒 Locked'}
                      </span>
                      {canEnter && (
                        <span className="text-[11px] font-extrabold text-indigo-600 flex items-center gap-0.5">
                          Enter <ArrowRight className="w-3 h-3" />
                        </span>
                      )}
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        )}

        {/* 2. PERSONAL MASTERY TREE VIEW */}
        {activeTab === 'mastery' && (
          <div className="space-y-6">
            <div className="flex items-center justify-between">
              <h3 className="text-lg font-black text-slate-900 flex items-center gap-2">
                <Shield className="w-5 h-5 text-indigo-600" />
                Personal Mastery Skill Branches
              </h3>
              <span className="text-xs font-bold text-emerald-600 bg-emerald-50 px-3 py-1 rounded-full border border-emerald-200">
                Growth vs. Past Self
              </span>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
              {masteryNodes.map((node) => (
                <div
                  key={node.id}
                  className={`p-4 rounded-2xl border flex items-center gap-4 ${
                    node.is_completed
                      ? 'bg-amber-50/80 border-amber-200'
                      : node.is_unlocked
                      ? 'bg-indigo-50/60 border-indigo-200'
                      : 'bg-slate-50 border-slate-200 opacity-50'
                  }`}
                >
                  <div className={`w-12 h-12 rounded-2xl flex items-center justify-center shrink-0 font-bold ${
                    node.is_completed ? 'bg-amber-400 text-amber-950' : node.is_unlocked ? 'bg-indigo-600 text-white' : 'bg-slate-300 text-slate-600'
                  }`}>
                    {node.is_completed ? <Award className="w-6 h-6" /> : <Star className="w-6 h-6" />}
                  </div>
                  <div>
                    <span className="text-[10px] font-extrabold uppercase text-slate-400 tracking-wider">{node.subject}</span>
                    <h4 className="text-sm font-extrabold text-slate-900">{node.title}</h4>
                    <span className="text-xs font-semibold text-slate-500">Level {node.level} Skill Leaf</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* 3. PERSONAL REWARD VAULT VIEW */}
        {activeTab === 'inventory' && (
          <div className="space-y-6">
            <div className="flex items-center justify-between">
              <h3 className="text-lg font-black text-slate-900 flex items-center gap-2">
                <Award className="w-5 h-5 text-amber-500" />
                Unlocked Vault & Personal Collectibles
              </h3>
              <span className="text-xs font-bold text-slate-400">{inventory.length} Items Unlocked</span>
            </div>

            {inventory.length === 0 ? (
              <div className="text-center py-8 text-slate-400 text-xs font-bold">
                Complete learning missions to unlock customized collectibles!
              </div>
            ) : (
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                {inventory.map((item, i) => (
                  <div key={item.id || i} className="bg-slate-50 border border-slate-200/90 rounded-2xl p-4 flex items-start gap-4">
                    <div className="w-12 h-12 rounded-2xl bg-gradient-to-br from-indigo-500 to-purple-600 text-white flex items-center justify-center font-bold shadow-md shrink-0">
                      <Sparkles className="w-6 h-6" />
                    </div>
                    <div className="space-y-1">
                      <span className="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded bg-indigo-100 text-indigo-700">
                        {item.item_type}
                      </span>
                      <h4 className="text-sm font-extrabold text-slate-900">{item.name}</h4>
                      <p className="text-xs text-slate-500">{item.description}</p>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        )}

      </div>
    </div>
  );
};

export default PersonalWorldMap;
