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
    "1": os.path.join(SCRIPT_DIR, "lkm1", "generate_lkm1_final.py"),
    "3": os.path.join(SCRIPT_DIR, "lkm3", "generate_lkm3_final.py"),
    "4": os.path.join(SCRIPT_DIR, "lkm4", "generate_lkm4_final.py"),
    "5": os.path.join(SCRIPT_DIR, "lkm5", "generate_lkm5_final.py"),
    "6": os.path.join(SCRIPT_DIR, "lkm6", "generate_lkm6_final.py"),
    "7": os.path.join(SCRIPT_DIR, "lkm7", "generate_lkm7_final.py"),
    "8": os.path.join(SCRIPT_DIR, "lkm8", "generate_lkm8_final.py"),
    "9": os.path.join(SCRIPT_DIR, "lkm9", "generate_lkm9_final.py"),
    "10": os.path.join(SCRIPT_DIR, "lkm10", "generate_lkm10_final.py"),
    "11": os.path.join(SCRIPT_DIR, "lkm11", "generate_lkm11_final.py"),
    "12": os.path.join(SCRIPT_DIR, "lkm12", "generate_lkm12_final.py"),
    "13": os.path.join(SCRIPT_DIR, "lkm13", "generate_lkm13_final.py"),
    "14": os.path.join(SCRIPT_DIR, "lkm14", "generate_lkm14_final.py")
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
    parser.add_argument("--lkm", type=str, choices=["1", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"], help="LKM number to generate (e.g. 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, or 14)")
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
        print("  3) LKM 5: Manajemen Jadwal Proyek (Bagian I)")
        print("  4) LKM 6: Manajemen Jadwal Proyek (Bagian II)")
        print("  5) Generate All")
        print("  q) Quit")
        choice = input("\nSelect an option [1-5, q]: ").strip()
        if choice == "1":
            run_lkm("3")
        elif choice == "2":
            run_lkm("4")
        elif choice == "3":
            run_lkm("5")
        elif choice == "4":
            run_lkm("6")
        elif choice == "5":
            for k in sorted(LKM_SCRIPTS.keys()):
                run_lkm(k)
        else:
            print("Exiting.")

if __name__ == "__main__":
    main()
