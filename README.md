# DustSentry - Cybersecurity Tool

**DustSentry** is a cybersecurity tool designed to scan directories and files for suspicious content by calculating a custom **DustCloak Score** based on file age, directory depth, and metadata anomalies. The tool flags files with high scores as potentially suspicious.

## Features
- Scans directories for suspicious files.
- Calculates a **DustCloak Score** for each file using:
  - File age (based on last modified time)
  - Directory depth (how deep the file is in the folder structure)
  - Metadata anomalies (e.g., creation date > last modified date)
- Flags files with scores above a threshold (≥ 70) as suspicious.
- Provides export of results in **JSON** format.
- Portable Dockerized solution for cross-platform use.
- Native OS binaries for direct installation (Windows, macOS, and Linux).
- Lightweight, minimal dependencies.

## Installation Options

You can use **DustSentry** either through Docker or by installing the native binaries for your operating system. Below are the instructions for both methods:

### Option 1: Using Docker (Recommended for Cross-Platform Use)
**DustSentry** can be easily run using Docker. This method is cross-platform and does not require installation of any additional software beyond Docker.

1. **Install Docker**:  
   Follow the instructions on the official [Docker website](https://www.docker.com/get-started) to install Docker on your system.

2. **Clone this repository**:
   ```bash
   git clone https://github.com/ViswanathPeri/DustSentry.git
   cd DustSentry
   ```

3. **Build the Docker image**:
   ```bash
   docker build -t dustsentry .
   ```

4. **Run the tool**:
   Replace `<path_to_scan_folder>` with the absolute path to the directory you want to scan.  
   
   Example for **Windows** (scanning a folder in Downloads):
   ```bash
   docker run -v <path_to_scan_folder>:/scan_dir dustsentry /scan_dir
   ```

   Example for **macOS** (scanning a folder in Documents):
   ```bash
   docker run -v <path_to_scan_folder>:/scan_dir dustsentry /scan_dir
   ```

   Example for **Linux** (scanning a folder in Documents):
   ```bash
   docker run -v <path_to_scan_folder>:/scan_dir dustsentry /scan_dir
   ```

### Option 2: Installing Using Native OS Binaries (No Docker Required)
If you prefer not to use Docker, you can install **DustSentry** using the native binaries for your operating system. This allows you to use the tool directly on your system without needing Docker.

#### For Windows:
1. **Download the Windows binary**:
   - [Download DustSentry for Windows (link to your release here)]

2. **Run the tool**:
   ```bash
   dustsentry.exe <path_to_scan_folder>
   ```

#### For macOS:
1. **Download the macOS binary**:
   - [Download DustSentry for macOS (link to your release here)]

2. **Run the tool**:
   ```bash
   ./dustsentry <path_to_scan_folder>
   ```

#### For Linux:
1. **Download the Linux binary**:
   - [Download DustSentry for Linux (link to your release here)]

2. **Run the tool**:
   ```bash
   ./dustsentry <path_to_scan_folder>
   ```

## Usage
Once you have installed **DustSentry** (either via Docker or native binaries), you can run it on the directory you wish to scan. The tool will analyze the directory and provide you with a list of suspicious files based on their **DustCloak Score**.

### Using Docker:
```bash
docker run -v <path_to_scan_folder>:/scan_dir dustsentry /scan_dir
```

### Using Native OS Binary:
#### Windows:
```bash
dustsentry.exe <path_to_scan_folder>
```

#### macOS:
```bash
./dustsentry <path_to_scan_folder>
```

#### Linux:
```bash
./dustsentry <path_to_scan_folder>
```

### Scan Output:
Once the scan is complete, **DustSentry** will provide a summary of any files with a **DustCloak Score** above the threshold (≥ 70). It will list the file paths and scores, and output the results in JSON format if requested.

```bash
🔍 Scanning directory: <path_to_scan_folder>

<path_to_scan_folder>/file1.txt → DustCloak Score: 81.67
<path_to_scan_folder>/subfolder/file2.pdf → DustCloak Score: 92.14

🚨 Suspicious Files Detected:
⚠️ <path_to_scan_folder>/file1.txt → Score: 81.67
⚠️ <path_to_scan_folder>/subfolder/file2.pdf → Score: 92.14

📁 Exported results to dustcloak_report.json
```

## Contributing
Contributions are welcome! If you have any ideas for improvements or find any bugs, feel free to fork the repository and submit a pull request. Please make sure to follow the code of conduct and maintain the consistency of the existing code structure.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
=======