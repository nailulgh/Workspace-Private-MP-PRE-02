# -*- coding: utf-8 -*-
"""
Master Generator Runner for Lembar Kerja Mahasiswa (LKM)
Usage:
    python scripts/run_generator.py --lkm 4
    python scripts/run_generator.py --lkm 3
    python scripts/run_generator.py --all
"""

import os
import sys
import argparse
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))

LKM_SCRIPTS = {
    "3": os.path.join(SCRIPT_DIR, "lkm3", "generate_lkm3_final.py"),
    "4": os.path.join(SCRIPT_DIR, "lkm4", "generate_lkm4_final.py")
}

def run_lkm(lkm_num):
    script_path = LKM_SCRIPTS.get(str(lkm_num))
    if not script_path or not os.path.exists(script_path):
        print(f"[ERROR] Script for LKM {lkm_num} not found at {script_path}")
        return False
        
    print(f"\n========================================================")
    print(f"  EXECUTING LKM {lkm_num} GENERATOR")
    print(f"  Script: {os.path.relpath(script_path, WORKSPACE_ROOT)}")
    print(f"========================================================")
    
    result = subprocess.run([sys.executable, script_path], cwd=os.path.dirname(script_path))
    if result.returncode == 0:
        print(f"[SUCCESS] LKM {lkm_num} document generated successfully!\n")
        return True
    else:
        print(f"[FAILED] Error running generator for LKM {lkm_num} (Exit code: {result.returncode})\n")
        return False

def main():
    parser = argparse.ArgumentParser(description="Generate LKM documents.")
    parser.add_argument("--lkm", type=str, choices=["3", "4"], help="LKM number to generate (e.g. 3 or 4)")
    parser.add_argument("--all", action="store_true", help="Generate all available LKMs")
    args = parser.parse_args()

    if args.all:
        for k in sorted(LKM_SCRIPTS.keys()):
            run_lkm(k)
    elif args.lkm:
        run_lkm(args.lkm)
    else:
        print("\nAvailable LKM Generators:")
        print("  1) LKM 3: Manajemen Integrasi Proyek")
        print("  2) LKM 4: Manajemen Ruang Lingkup Proyek")
        print("  3) Generate All")
        print("  q) Quit")
        choice = input("\nSelect an option [1-3, q]: ").strip()
        if choice == "1":
            run_lkm("3")
        elif choice == "2":
            run_lkm("4")
        elif choice == "3":
            for k in sorted(LKM_SCRIPTS.keys()):
                run_lkm(k)
        else:
            print("Exiting.")

if __name__ == "__main__":
    main()
