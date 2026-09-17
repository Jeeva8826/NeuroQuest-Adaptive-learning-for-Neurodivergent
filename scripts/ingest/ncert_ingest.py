import json
import os
from pathlib import Path

def ingest_ncert_metadata():
    # Setup paths
    base_dir = Path(__file__).resolve().parent.parent.parent
    curriculum_dir = base_dir / "data" / "curriculum"
    curriculum_dir.mkdir(parents=True, exist_ok=True)

    # Class 7 Science Metadata
    class7_science = {
        "subject": "Science",
        "class_level": 7,
        "source": "NCERT",
        "license": "NCERT Permitted Metadata",
        "chapters": [
            {
                "chapter_id": "S7_C1",
                "chapter_title": "Nutrition in Plants",
                "topics": [
                    "Mode of Nutrition in Plants",
                    "Photosynthesis - Food Making Process in Plants",
                    "Other Modes of Nutrition in Plants",
                    "Saprotrophs",
                    "How Nutrients are Replenished in the Soil"
                ],
                "learning_outcomes": [
                    "Explains the process of photosynthesis",
                    "Differentiates between autotrophic and heterotrophic nutrition",
                    "Understands the role of stomata and chlorophyll"
                ],
                "source_url": "https://ncert.nic.in/textbook.php?gesc1=1-18"
            }
        ]
    }

    # Class 7 Mathematics Metadata
    class7_math = {
        "subject": "Mathematics",
        "class_level": 7,
        "source": "NCERT",
        "license": "NCERT Permitted Metadata",
        "chapters": [
            {
                "chapter_id": "M7_C1",
                "chapter_title": "Integers",
                "topics": [
                    "Properties of Addition and Subtraction of Integers",
                    "Multiplication of Integers",
                    "Properties of Multiplication of Integers",
                    "Division of Integers",
                    "Properties of Division of Integers"
                ],
                "learning_outcomes": [
                    "Performs operations on integers",
                    "Applies properties of operations on integers to solve problems"
                ],
                "source_url": "https://ncert.nic.in/textbook.php?gemh1=1-15"
            }
        ]
    }

    # Save to JSON
    science_path = curriculum_dir / "class7_science.json"
    math_path = curriculum_dir / "class7_math.json"
    
    with open(science_path, "w") as f:
        json.dump(class7_science, f, indent=4)
        
    with open(math_path, "w") as f:
        json.dump(class7_math, f, indent=4)

    print(f"Successfully ingested NCERT metadata into {curriculum_dir}")
    print(f"Files created:\n- {science_path}\n- {math_path}")

if __name__ == "__main__":
    ingest_ncert_metadata()
