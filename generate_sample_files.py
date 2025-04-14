import os
import time
from pathlib import Path

def create_file(path, content="", modified_offset_days=0, created_offset_days=0):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

    now = time.time()
    modified_time = now - (modified_offset_days * 86400)
    created_time = now - (created_offset_days * 86400)

    os.utime(path, (created_time, modified_time))

def generate_samples(base_dir):
    print(f"📂 Creating test samples in '{base_dir}'")
    base = Path(base_dir)
    if base.exists():
        print("⚠️ Directory already exists. Overwriting files...")

    # Shallow and recent
    create_file(f"{base_dir}/recent.txt", "This is a recent file.")

    # Deep and old
    create_file(f"{base_dir}/deep/inside/archive/old_config.log", "Old config log", modified_offset_days=900)

    # Weird metadata (created after modified)
    create_file(f"{base_dir}/metadata/weird_meta.txt", "Created after modified", modified_offset_days=100, created_offset_days=-1)

    # Hidden file
    create_file(f"{base_dir}/.hidden/.secrets", "Hidden file content", modified_offset_days=400)

    # Decoy file
    create_file(f"{base_dir}/decoy/harmless.txt", "Looks harmless", modified_offset_days=300)

    # Very deep and very old
    create_file(f"{base_dir}/system/hidden/deep/further/down/logs/sys.old", "Very old and deep", modified_offset_days=1000)

    print("✅ Sample files created successfully.")

if __name__ == "__main__":
    generate_samples("test_samples")
