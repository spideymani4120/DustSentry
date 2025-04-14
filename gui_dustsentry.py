import os
import time
import json
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from datetime import datetime
from dustsentry import scan_directory  # Assumes dustsentry.py is in the same directory


def export_to_json(data, filename="dustcloak_report.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"\nExported results to {filename}")


def launch_gui():
    def browse_directory():
        path = filedialog.askdirectory()
        if path:
            entry_dir.delete(0, tk.END)
            entry_dir.insert(0, path)

    def run_scan():
        nonlocal all_results, flagged
        output_box.delete("1.0", tk.END)
        path = entry_dir.get()
        if not os.path.isdir(path):
            messagebox.showerror("Invalid Directory", "Please select a valid directory.")
            return
        output_box.insert(tk.END, f"Scanning directory: {path}\n\n")
        try:
            all_results, flagged = scan_directory(path)
            for entry in all_results:
                output_box.insert(tk.END, f"{entry['path']} → Score: {entry['score']}\n")
            output_box.insert(tk.END, f"\nSuspicious Files ({len(flagged)}):\n")
            for entry in flagged:
                output_box.insert(tk.END, f"[!] {entry['path']} → Score: {entry['score']}\n")
            export_button.config(state=tk.NORMAL)
        except Exception as e:
            messagebox.showerror("Scan Error", str(e))

    def export_results():
        if not all_results:
            messagebox.showwarning("No Data", "Please run a scan first.")
            return
        results_dir = os.path.join(os.getcwd(), "results")
        os.makedirs(results_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(results_dir, f"dustcloak_report_{timestamp}.json")
        export_to_json({
            "timestamp": time.time(),
            "scanned": all_results,
            "suspicious": flagged
        }, filename)
        messagebox.showinfo("Exported", f"Results saved to:\n{filename}")

    # GUI Setup
    root = tk.Tk()
    root.title("DustSentry - Directory Scanner")

    all_results = []
    flagged = []

    tk.Label(root, text="Directory to scan:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_dir = tk.Entry(root, width=50)
    entry_dir.grid(row=0, column=1, padx=5)
    tk.Button(root, text="Browse", command=browse_directory).grid(row=0, column=2, padx=5)

    tk.Button(root, text="Run Scan", command=run_scan, bg="#4CAF50", fg="white").grid(row=1, column=1, pady=10)

    export_button = tk.Button(root, text="Export Results", command=export_results, state=tk.DISABLED)
    export_button.grid(row=1, column=2, pady=10)

    output_box = scrolledtext.ScrolledText(root, width=100, height=30)
    output_box.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    launch_gui()
