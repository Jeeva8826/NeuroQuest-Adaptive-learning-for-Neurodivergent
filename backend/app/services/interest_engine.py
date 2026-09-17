import logging
from typing import Dict, Any, List

logger = logging.getLogger("neuroquest.interest_engine")

PREDEFINED_THEMES = {
    "space": {
        "theme_id": "space",
        "world_name": "Cosmic Observatory",
        "hero_role": "Commander",
        "currency_name": "Starlight Shards",
        "zones": ["Space Station Dock", "Lunar Base", "Asteroid Belt", "Deep Galaxy"],
        "collectible_types": ["Model Rocket", "Moon Rock", "Star Map", "Satellite Module"],
        "primary_color": "#8b5cf6",
        "secondary_color": "#3b82f6",
        "metaphors": {"math": "power cell alignment", "science": "planetary scanning", "english": "transmission decoding", "coding": "thruster programming"}
    },
    "animals": {
        "theme_id": "animals",
        "world_name": "Wildlife Sanctuary",
        "hero_role": "Ranger",
        "currency_name": "Habitat Badges",
        "zones": ["Sanctuary Gate", "Savannah Reserve", "Deep Jungle", "Ocean Reef"],
        "collectible_types": ["Golden Paw", "Feather Collection", "Reef Fossil", "Animal Companion"],
        "primary_color": "#10b981",
        "secondary_color": "#14b8a6",
        "metaphors": {"math": "food portioning", "science": "ecosystem observation", "english": "wildlife logbook", "coding": "tracker tagging"}
    },
    "sports": {
        "theme_id": "sports",
        "world_name": "Athlete Training Complex",
        "hero_role": "Champion",
        "currency_name": "Skill Trophies",
        "zones": ["Warmup Court", "Main Arena", "Championship Field", "Hall of Fame"],
        "collectible_types": ["Gold Medal", "Custom Jersey", "Speed Cleats", "Training Whistle"],
        "primary_color": "#f59e0b",
        "secondary_color": "#ef4444",
        "metaphors": {"math": "score tracking", "science": "biomechanics", "english": "playbook strategy", "coding": "drill automation"}
    },
    "art": {
        "theme_id": "art",
        "world_name": "Creative Studio",
        "hero_role": "Artist",
        "currency_name": "Palette Sparks",
        "zones": ["Sketchroom", "Color Gallery", "Sculpture Plaza", "Masterpiece Hall"],
        "collectible_types": ["Golden Brush", "Rainbow Palette", "Marble Chisel", "Exhibition Canvas"],
        "primary_color": "#ec4899",
        "secondary_color": "#8b5cf6",
        "metaphors": {"math": "canvas grid math", "science": "color mixing theory", "english": "visual storytelling", "coding": "pattern design"}
    },
    "coding": {
        "theme_id": "coding",
        "world_name": "Cyber Workshop",
        "hero_role": "Engineer",
        "currency_name": "Logic Cores",
        "zones": ["Debugging Lab", "Robot Assembly", "Quantum Server", "Mainframe Core"],
        "collectible_types": ["Microchip", "Quantum Key", "Robot Companion", "Circuit Blueprint"],
        "primary_color": "#0284c7",
        "secondary_color": "#6366f1",
        "metaphors": {"math": "binary logic", "science": "hardware architecture", "english": "syntax analysis", "coding": "algorithm design"}
    },
    "music": {
        "theme_id": "music",
        "world_name": "Harmony Stage",
        "hero_role": "Maestro",
        "currency_name": "Rhythm Notes",
        "zones": ["Practice Studio", "Acoustic Lounge", "Concert Stage", "Grand Symphony"],
        "collectible_types": ["Golden Clef", "Rhythm Drum", "Crystal Violin", "Stage Light"],
        "primary_color": "#7c3aed",
        "secondary_color": "#ec4899",
        "metaphors": {"math": "beat division", "science": "sound wave physics", "english": "lyric composition", "coding": "rhythm sequencing"}
    },
    "cars": {
        "theme_id": "cars",
        "world_name": "Speedway Garage",
        "hero_role": "Racer",
        "currency_name": "Turbo Gears",
        "zones": ["Pit Stop", "Tuning Workshop", "Desert Circuit", "Grand Prix Track"],
        "collectible_types": ["Nitro Boost", "Titanium Wrench", "Custom Spoiler", "Champion Trophy"],
        "primary_color": "#f97316",
        "secondary_color": "#eab308",
        "metaphors": {"math": "speed calculations", "science": "engine physics", "english": "race logs", "coding": "autopilot logic"}
    },
    "fantasy": {
        "theme_id": "fantasy",
        "world_name": "Enchanted Kingdom",
        "hero_role": "Adventurer",
        "currency_name": "Runestone Crystals",
        "zones": ["Whispering Forest", "Crystal Citadel", "Dragon Peak", "Celestial Shrine"],
        "collectible_types": ["Ancient Scroll", "Mythic Shield", "Phoenix Feather", "Sorcerer Staff"],
        "primary_color": "#6366f1",
        "secondary_color": "#a855f7",
        "metaphors": {"math": "rune deciphering", "science": "alchemy recipes", "english": "epic legends", "coding": "spellcraft logic"}
    }
}

class InterestEngine:
    """Interest-to-Game Engine mapping learner interests into game worlds and mission themes."""

    def resolve_theme(self, interests: List[str]) -> Dict[str, Any]:
        """Maps any list of learner interests or custom text to a game world structure."""
        if not interests:
            return PREDEFINED_THEMES["space"]

        combined_text = " ".join(interests).lower()

        # Check matched predefined themes
        for key in PREDEFINED_THEMES:
            if key in combined_text:
                return PREDEFINED_THEMES[key]

        # Word keyword matching
        if any(w in combined_text for w in ["star", "planet", "galaxy", "astro", "moon", "rocket"]):
            return PREDEFINED_THEMES["space"]
        elif any(w in combined_text for w in ["dog", "cat", "bird", "wild", "ocean", "pet", "dinosaur", "zoo"]):
            return PREDEFINED_THEMES["animals"]
        elif any(w in combined_text for w in ["ball", "run", "game", "match", "swim", "bike"]):
            return PREDEFINED_THEMES["sports"]
        elif any(w in combined_text for w in ["paint", "draw", "craft", "build", "lego"]):
            return PREDEFINED_THEMES["art"]
        elif any(w in combined_text for w in ["tech", "robot", "computer", "program", "code"]):
            return PREDEFINED_THEMES["coding"]
        elif any(w in combined_text for w in ["song", "beat", "drum", "sing", "piano"]):
            return PREDEFINED_THEMES["music"]
        elif any(w in combined_text for w in ["drive", "wheel", "race", "truck", "motor"]):
            return PREDEFINED_THEMES["cars"]
        elif any(w in combined_text for w in ["magic", "dragon", "knight", "sword", "quest"]):
            return PREDEFINED_THEMES["fantasy"]

        # Dynamic fallback theme for custom interest text (e.g. "dinosaurs", "rollercoasters")
        custom_topic = interests[0].capitalize()
        return {
            "theme_id": "custom",
            "world_name": f"{custom_topic} World",
            "hero_role": "Explorer",
            "currency_name": f"{custom_topic} Badges",
            "zones": [f"{custom_topic} Discovery Zone", f"{custom_topic} Advanced Outpost", f"{custom_topic} Master Realm"],
            "collectible_types": [f"{custom_topic} Artifact", f"{custom_topic} Blueprint", f"Golden {custom_topic} Medal"],
            "primary_color": "#6366f1",
            "secondary_color": "#14b8a6",
            "metaphors": {
                "math": f"{custom_topic} counts",
                "science": f"{custom_topic} discovery",
                "english": f"{custom_topic} tales",
                "coding": f"{custom_topic} logic"
            }
        }

interest_engine = InterestEngine()
