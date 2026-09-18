import os
import sys
import json
import shutil
from pathlib import Path
import pandas as pd

DATASETS_TO_FETCH = [
    {"handle": "adityasharma01/ncert-books", "name": "NCERT Books", "tag": "ncert_books"},
    {"handle": "shibumohapatra/icmr-data", "name": "ICMR Data", "tag": "icmr_data"},
    {"handle": "n1sarg/icmr-testing-data", "name": "ICMR Testing Data", "tag": "icmr_testing_data"},
    {"handle": "rahuldev77788/neurodivergent-learner-personalization", "name": "Neurodivergent Learner Personalization", "tag": "neurodivergent_personalization"},
    {"handle": "raiyangani/autistic-spectrum-disorder-screening-data", "name": "Autistic Spectrum Disorder Screening Data", "tag": "asd_screening_raiyangani"},
    {"handle": "fabdelja/asd-screening-data-toddler-child-adoles-adult", "name": "ASD Screening Across Age Groups", "tag": "asd_screening_fabdelja"},
    {"handle": "ziya07/student-learning-interaction-logs-dataset", "name": "Student Learning Interaction Logs", "tag": "student_interaction_logs"},
    {"handle": "adilshamim8/student-performance-and-learning-style", "name": "Student Performance & Learning Style", "tag": "student_perf_learning_style"},
    {"handle": "ziya07/personalized-learning-interaction-dataset", "name": "Personalized Learning Interaction Dataset", "tag": "personalized_learning_interaction"}
]

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
DATA_METADATA = PROJECT_ROOT / "data" / "metadata"

DATA_RAW.mkdir(parents=True, exist_ok=True)
DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
DATA_METADATA.mkdir(parents=True, exist_ok=True)

def inspect_file(filepath: Path):
    ext = filepath.suffix.lower()
    size_bytes = filepath.stat().st_size
    info = {
        "filename": filepath.name,
        "extension": ext,
        "size_bytes": size_bytes,
        "columns": [],
        "sample_records": [],
        "record_count": None,
        "notes": ""
    }
    
    try:
        if ext in [".csv", ".tsv"]:
            sep = "\t" if ext == ".tsv" else ","
            try:
                df = pd.read_csv(filepath, sep=sep, nrows=5)
                info["columns"] = list(df.columns)
                info["sample_records"] = df.head(2).to_dict(orient="records")
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    info["record_count"] = sum(1 for _ in f) - 1
            except Exception as e:
                info["notes"] = f"CSV read error: {e}"
                
        elif ext == ".json":
            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    data = json.load(f)
                if isinstance(data, list):
                    info["record_count"] = len(data)
                    if data and isinstance(data[0], dict):
                        info["columns"] = list(data[0].keys())
                        info["sample_records"] = data[:2]
                elif isinstance(data, dict):
                    info["columns"] = list(data.keys())
                    info["record_count"] = 1
            except Exception as e:
                info["notes"] = f"JSON read error: {e}"
                
        elif ext in [".arff", ".txt"]:
            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    lines = [f.readline() for _ in range(50)]
                info["notes"] = f"Text preview: {len(lines)} sample lines"
                attrs = [l.strip() for l in lines if l.lower().startswith("@attribute")]
                if attrs:
                    info["columns"] = [a.split()[1] for a in attrs if len(a.split()) > 1]
            except Exception as e:
                info["notes"] = f"Text read error: {e}"
                
    except Exception as e:
        info["notes"] = f"General file inspect error: {e}"
        
    return info

def main():
    import kagglehub
    
    inventory = []
    
    print("=========================================================")
    print("NEUROQUEST KAGGLE DATASET FETCH & INVENTORY PIPELINE")
    print("=========================================================")
    
    for item in DATASETS_TO_FETCH:
        handle = item["handle"]
        name = item["name"]
        tag = item["tag"]
        print(f"\n[FETCHING] {name} ({handle})...")
        
        record = {
            "dataset_name": name,
            "handle": handle,
            "tag": tag,
            "download_status": "FAILED",
            "download_path": "",
            "target_raw_dir": str(DATA_RAW / tag),
            "files": [],
            "total_size_bytes": 0,
            "category": "UNCATEGORIZED",
            "usability": "UNKNOWN",
            "reason": ""
        }
        
        try:
            download_path = kagglehub.dataset_download(handle)
            print(f"   [SUCCESS] Downloaded to: {download_path}")
            record["download_status"] = "SUCCESS"
            record["download_path"] = str(download_path)
            
            target_dir = DATA_RAW / tag
            target_dir.mkdir(parents=True, exist_ok=True)
            
            dl_path_obj = Path(download_path)
            found_files = []
            
            if dl_path_obj.is_dir():
                for p in dl_path_obj.rglob("*"):
                    if p.is_file():
                        rel = p.relative_to(dl_path_obj)
                        dest = target_dir / rel
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        if not dest.exists() or dest.stat().st_size != p.stat().st_size:
                            shutil.copy2(p, dest)
                        
                        f_info = inspect_file(dest)
                        found_files.append(f_info)
                        record["total_size_bytes"] += f_info["size_bytes"]
            elif dl_path_obj.is_file():
                dest = target_dir / dl_path_obj.name
                shutil.copy2(dl_path_obj, dest)
                f_info = inspect_file(dest)
                found_files.append(f_info)
                record["total_size_bytes"] += f_info["size_bytes"]
                
            record["files"] = found_files
            print(f"   [INSPECTED] Found {len(found_files)} files. Total size: {record['total_size_bytes']} bytes")
            
        except Exception as e:
            print(f"   [ERROR] Failed to download {handle}: {e}")
            record["download_status"] = f"FAILED: {str(e)}"
            record["reason"] = str(e)
            
        inventory.append(record)
        
    inv_file = DATA_METADATA / "dataset_inventory.json"
    with open(inv_file, "w", encoding="utf-8") as f:
        json.dump(inventory, f, indent=2, default=str)
        
    print("\n=========================================================")
    print(f"Inventory written to: {inv_file}")
    print("=========================================================")

if __name__ == "__main__":
    main()
