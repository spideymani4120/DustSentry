import os
import time
import json
import argparse
from pathlib import Path
from datetime import datetime

# Constants for score weights
WEIGHT_AGE = 0.4
WEIGHT_DEPTH = 0.3
WEIGHT_METADATA = 0.3

# Threshold to flag suspicious files
SUSPICIOUS_THRESHOLD = 70

def get_file_age_in_days(file_path):
    try:
        last_modified = os.path.getmtime(file_path)
        age_days = (time.time() - last_modified) / 86400
        return age_days
    except Exception:
        return 0

def get_file_depth(file_path, base_path):
    relative = Path(file_path).relative_to(base_path)
    return len(relative.parents)

def has_weird_metadata(file_path):
    try:
        created = os.path.getctime(file_path)
        modified = os.path.getmtime(file_path)
        return created > modified
    except Exception:
        return False

def calculate_dustcloak_score(age_days, depth, weird_meta):
    score = 0
    score += min(age_days / 180, 1.0) * 100 * WEIGHT_AGE
    score += min(depth / 5, 1.0) * 100 * WEIGHT_DEPTH
    score += (100 * WEIGHT_METADATA) if weird_meta else 0
    return round(score, 2)

def scan_directory(path):
    base_path = Path(path)
    suspicious = []
    all_results = []

    print(f"\nScanning directory: {path}\n")

    for file_path in base_path.rglob("*"):
        if file_path.is_file():
            age_days = get_file_age_in_days(file_path)
            depth = get_file_depth(file_path, base_path)
            weird_meta = has_weird_metadata(file_path)
            score = calculate_dustcloak_score(age_days, depth, weird_meta)

            print(f"{file_path} → DustCloak Score: {score}")

            entry = {
                "path": str(file_path),
                "age_days": age_days,
                "depth": depth,
                "weird_metadata": weird_meta,
                "score": score
            }
            all_results.append(entry)

            if score >= SUSPICIOUS_THRESHOLD:
                suspicious.append(entry)

    print("\nSuspicious Files Detected:")
    for entry in suspicious:
        print(f"{entry['path']} → Score: {entry['score']}")

    return all_results, suspicious

def export_to_json(data, filename="dustcloak_report.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"\nExported results to {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DustSentry: Scan directories for suspicious files.")
    parser.add_argument("directory", help="Directory to scan")
    parser.add_argument("--export", choices=["json"], help="Export results to JSON")
    args = parser.parse_args()

    all_results, flagged = scan_directory(args.directory)

    if args.export == "json":
        export_to_json({
            "timestamp": time.time(),
            "scanned": all_results,
            "suspicious": flagged
        })
