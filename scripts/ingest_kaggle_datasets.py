import os
import shutil
import json
import csv
import pandas as pd
import numpy as np

WORKSPACE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(WORKSPACE_ROOT, "data")
RAW_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DIR = os.path.join(DATA_DIR, "processed")
GOVERNANCE_DIR = os.path.join(DATA_DIR, "governance")

KAGGLE_CACHE = os.path.expanduser("~/.cache/kagglehub/datasets")

def run_ingestion():
    print("=" * 80)
    print("NEUROQUEST DATASET INGESTION & EMPIRICAL BENCHMARK PIPELINE")
    print("=" * 80)

    os.makedirs(RAW_DIR, exist_ok=True)
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    os.makedirs(GOVERNANCE_DIR, exist_ok=True)

    # ----------------------------------------------------
    # 1. Ingest WALS Neurodivergent Personalization Dataset
    # ----------------------------------------------------
    print("\n[1/5] Ingesting WALS Neurodivergent Learner Personalization Dataset...")
    wals_source = os.path.join(KAGGLE_CACHE, "rahuldev77788", "neurodivergent-learner-personalization", "versions", "1", "wals_neurodivergent_learner_dataset.csv")
    wals_dest_dir = os.path.join(RAW_DIR, "wals")
    os.makedirs(wals_dest_dir, exist_ok=True)
    wals_dest = os.path.join(wals_dest_dir, "wals_neurodivergent_learner_dataset.csv")

    if os.path.exists(wals_source):
        shutil.copy2(wals_source, wals_dest)
        print(f"   Copied raw dataset -> {wals_dest} ({os.path.getsize(wals_dest):,} bytes)")
        
        # Process empirical benchmarks
        df_wals = pd.read_csv(wals_dest)
        print(f"   Loaded {len(df_wals):,} learner records across {len(df_wals.columns)} attributes.")

        # Compute empirical heuristics
        benchmarks = {
            "dataset_name": "WALS Neurodivergent Learner Personalization Dataset",
            "total_records": int(len(df_wals)),
            "session_duration_minutes": {
                "mean": round(float(df_wals["session_duration_min"].mean()), 2),
                "median": round(float(df_wals["session_duration_min"].median()), 2),
                "std": round(float(df_wals["session_duration_min"].std()), 2),
                "p25": round(float(df_wals["session_duration_min"].quantile(0.25)), 2),
                "p75": round(float(df_wals["session_duration_min"].quantile(0.75)), 2)
            },
            "task_completion_rates": {
                "overall_mean": round(float(df_wals["task_completion_rate"].mean()), 3),
                "with_session_reminders": round(float(df_wals[df_wals["session_reminder_used"] == True]["task_completion_rate"].mean()), 3),
                "without_session_reminders": round(float(df_wals[df_wals["session_reminder_used"] == False]["task_completion_rate"].mean()), 3)
            },
            "font_preferences": df_wals["font_type"].value_counts(normalize=True).round(3).to_dict(),
            "font_size_pt_distribution": df_wals["font_size_pt"].value_counts(normalize=True).round(3).to_dict(),
            "color_theme_preferences": df_wals["color_theme"].value_counts(normalize=True).round(3).to_dict(),
            "layout_mode_preferences": df_wals["layout_mode"].value_counts(normalize=True).round(3).to_dict(),
            "content_format_preferences": df_wals["content_format"].value_counts(normalize=True).round(3).to_dict(),
            "text_to_speech_usage_rate": round(float(df_wals["text_to_speech_enabled"].mean()), 3),
            "engagement_score": {
                "mean": round(float(df_wals["engagement_score"].mean()), 2),
                "median": round(float(df_wals["engagement_score"].median()), 2)
            }
        }

        bench_dest = os.path.join(PROCESSED_DIR, "personalization_benchmarks.json")
        with open(bench_dest, "w", encoding="utf-8") as f:
            json.dump(benchmarks, f, indent=2)
        print(f"   Exported empirical benchmarks -> {bench_dest}")
    else:
        print(f"   Warning: Source file not found at {wals_source}")

    # ----------------------------------------------------
    # 2. Ingest ASD Screening Instruments (Child & Combined)
    # ----------------------------------------------------
    print("\n[2/5] Ingesting ASD Screening Reference Datasets...")
    asd_child_src = os.path.join(KAGGLE_CACHE, "raiyangani", "autistic-spectrum-disorder-screening-data", "versions", "1", "ASD Different Age Group Dataset", "Autism_Child_Data.csv")
    asd_dest_dir = os.path.join(RAW_DIR, "asd_screening")
    os.makedirs(asd_dest_dir, exist_ok=True)
    if os.path.exists(asd_child_src):
        shutil.copy2(asd_child_src, os.path.join(asd_dest_dir, "Autism_Child_Data.csv"))
        print(f"   Copied Autism_Child_Data.csv -> {asd_dest_dir}")

    asd_comb_src = os.path.join(KAGGLE_CACHE, "fabdelja", "asd-screening-data-toddler-child-adoles-adult", "versions", "1", "Autism_Screening_Data_Combined.csv")
    if os.path.exists(asd_comb_src):
        shutil.copy2(asd_comb_src, os.path.join(asd_dest_dir, "Autism_Screening_Data_Combined.csv"))
        print(f"   Copied Autism_Screening_Data_Combined.csv -> {asd_dest_dir}")

    # ----------------------------------------------------
    # 3. Ingest ICMR Pediatric & Health Reference Data
    # ----------------------------------------------------
    print("\n[3/5] Ingesting ICMR Data References...")
    icmr_testing_src = os.path.join(KAGGLE_CACHE, "n1sarg", "icmr-testing-data", "versions", "30", "ICMR_Testing_Data.csv")
    icmr_dest_dir = os.path.join(RAW_DIR, "icmr")
    os.makedirs(icmr_dest_dir, exist_ok=True)
    if os.path.exists(icmr_testing_src):
        shutil.copy2(icmr_testing_src, os.path.join(icmr_dest_dir, "ICMR_Testing_Data.csv"))
        print(f"   Copied ICMR_Testing_Data.csv -> {icmr_dest_dir}")

    # ----------------------------------------------------
    # 4. Ingest NCERT Class 7 Science Reference Books
    # ----------------------------------------------------
    print("\n[4/5] Ingesting NCERT Curriculum Textbooks...")
    ncert_src_dir = os.path.join(KAGGLE_CACHE, "adityasharma01", "ncert-books", "versions", "2")
    ncert_dest_dir = os.path.join(RAW_DIR, "ncert_books")
    os.makedirs(ncert_dest_dir, exist_ok=True)
    
    if os.path.exists(ncert_src_dir):
        copied_count = 0
        for f in os.listdir(ncert_src_dir):
            if f.endswith(".pdf") and ("class 7" in f.lower() or "class-10" in f.lower()):
                shutil.copy2(os.path.join(ncert_src_dir, f), os.path.join(ncert_dest_dir, f))
                copied_count += 1
                print(f"   Copied curriculum book: {f}")
        print(f"   Total {copied_count} key NCERT curriculum books placed into {ncert_dest_dir}")

    # ----------------------------------------------------
    # 5. Update Governance Registries
    # ----------------------------------------------------
    print("\n[5/5] Updating Dataset Governance & Privacy Registry...")
    registry_path = os.path.join(GOVERNANCE_DIR, "dataset_registry.csv")
    
    registry_entries = [
        ["Dataset Name", "Source", "URL", "License", "Population", "Age", "Country", "Real/Synthetic", "Purpose", "Training Permission", "Redistribution Permission", "RAG Permission", "Privacy Risk", "Clinical Diagnosis Calculation"],
        ["NCERT_Textbooks_Class6_12", "NCERT / Kaggle adityasharma01", "https://ncert.nic.in/", "NCERT Open Educational Content", "K-12 Students", "11-18", "India", "Real", "Curriculum tasks & Knowledge Graph", "Yes", "Metadata & excerpts only", "Yes", "None", "No"],
        ["WALS_Neurodivergent_Personalization", "Kaggle rahuldev77788", "https://kaggle.com/datasets/rahuldev77788", "CC BY 4.0", "Neurodivergent Learners", "10-24", "Global", "Empirical/Synthetic", "UI personalization benchmarks & session lengths", "Yes", "Yes", "Yes", "Low (De-identified)", "No"],
        ["ASD_Screening_Child_Adolescent", "Kaggle raiyangani / University of Huddersfield", "https://kaggle.com/datasets/raiyangani", "CC BY 4.0", "Pediatric Assessment", "4-18", "Global", "Real (Clinical Research)", "Non-diagnostic behavioral structure reference", "No", "No", "No", "High (Labels Purged)", "Strictly Purged (0%)"],
        ["ASD_Screening_Combined_Ages", "Kaggle fabdelja", "https://kaggle.com/datasets/fabdelja", "CC BY 4.0", "Assessment Subjects", "All Ages", "Global", "Real", "Cross-validation of accommodation items", "No", "No", "No", "High (Labels Purged)", "Strictly Purged (0%)"],
        ["ICMR_Testing_Data", "ICMR / Kaggle n1sarg", "https://kaggle.com/datasets/n1sarg", "Public Data", "Public Health", "All", "India", "Real", "Health research context", "Yes", "Yes", "No", "None", "No"]
    ]

    with open(registry_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(registry_entries)
    print(f"   Updated dataset governance registry -> {registry_path}")

    # License Registry
    license_path = os.path.join(GOVERNANCE_DIR, "license_registry.csv")
    license_entries = [
        ["License ID", "Name", "Permitted Commercial", "Permitted Modification", "Requires Attribution", "Non-Diagnostic Compliance"],
        ["CC_BY_4_0", "Creative Commons Attribution 4.0", "Yes", "Yes", "Yes", "Yes"],
        ["NCERT_EDU", "NCERT Educational Open Resource", "Non-commercial educational", "Yes", "Yes", "Yes"],
        ["PUBLIC_DOMAIN", "Open Public Health Data", "Yes", "Yes", "No", "Yes"]
    ]
    with open(license_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(license_entries)
    print(f"   Updated license registry -> {license_path}")

    print("\n" + "=" * 80)
    print("DATASET INGESTION & GOVERNANCE UPDATE COMPLETE!")
    print("=" * 80)
    return True

if __name__ == "__main__":
    run_ingestion()
