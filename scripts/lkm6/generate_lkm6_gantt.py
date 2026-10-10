# -*- coding: utf-8 -*-
"""
Generator for High-Resolution Gantt Chart & Schedule Computation
Pertemuan 6: Manajemen Jadwal Proyek (Bagian II)
Author: Muhammad Nailul Ghufron Majid (240605110160)
"""

import os
from datetime import datetime, timedelta
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 21 Activities Definition
ACTIVITIES = [
    {"id": "ACT-01", "wbs": "1.1.1", "name": "Formulasi Problem Statement & Spesifikasi 7 Fitur", "dur": 3, "preds": []},
    {"id": "ACT-02", "wbs": "1.1.2", "name": "Penyusunan Project Charter & Schedule Plan", "dur": 2, "preds": ["ACT-01"]},
    {"id": "ACT-03", "wbs": "2.1.1", "name": "Studi Literatur SOTA Machine Learning Delay", "dur": 5, "preds": ["ACT-01"]},
    {"id": "ACT-04", "wbs": "2.1.2", "name": "Penyusunan Matriks Literatur & Research Gap", "dur": 3, "preds": ["ACT-03"]},
    {"id": "ACT-05", "wbs": "3.1.1", "name": "Ekstraksi Data Metrik dari 8 Dokumen PMP ERP", "dur": 4, "preds": ["ACT-02"]},
    {"id": "ACT-06", "wbs": "3.1.2", "name": "Data Cleansing & Deteksi Anomali/Outlier", "dur": 3, "preds": ["ACT-05"]},
    {"id": "ACT-07", "wbs": "3.1.3", "name": "Imputasi Missing Values & Konsistensi Skema", "dur": 2, "preds": ["ACT-06"]},
    {"id": "ACT-08", "wbs": "3.1.4", "name": "Feature Engineering & Dependency Scoring", "dur": 3, "preds": ["ACT-07"]},
    {"id": "ACT-09", "wbs": "3.1.5", "name": "Normalisasi Fitur (Min-Max) & Encoding", "dur": 2, "preds": ["ACT-08"]},
    {"id": "ACT-10", "wbs": "3.1.6", "name": "Stratified Train-Test Dataset Splitting (80:20)", "dur": 1, "preds": ["ACT-09"]},
    {"id": "ACT-11", "wbs": "4.1.1", "name": "Training Baseline Logistic Regression", "dur": 3, "preds": ["ACT-10"]},
    {"id": "ACT-12", "wbs": "4.1.2", "name": "Training Ensemble Random Forest (predict_proba)", "dur": 4, "preds": ["ACT-10"]},
    {"id": "ACT-13", "wbs": "4.1.3", "name": "Training Gradient Boosting (XGBoost/LightGBM)", "dur": 4, "preds": ["ACT-10"]},
    {"id": "ACT-14", "wbs": "4.1.4", "name": "Arsitektur & Training Deep Learning MLP", "dur": 5, "preds": ["ACT-10"]},
    {"id": "ACT-15", "wbs": "4.2.1", "name": "Implementasi Kalibrasi Probabilitas (Platt Scaling)", "dur": 3, "preds": ["ACT-11", "ACT-12", "ACT-13", "ACT-14"]},
    {"id": "ACT-16", "wbs": "4.2.2", "name": "Implementasi Kalibrasi Isotonic Regression", "dur": 3, "preds": ["ACT-15"]},
    {"id": "ACT-17", "wbs": "5.1.1", "name": "Komputasi Metrik Evaluasi (Brier, ROC-AUC, ECE)", "dur": 3, "preds": ["ACT-16"]},
    {"id": "ACT-18", "wbs": "5.1.2", "name": "Optimasi Ambang Batas Alert EWS (Youden J >= 0.65)", "dur": 2, "preds": ["ACT-17"]},
    {"id": "ACT-19", "wbs": "5.1.3", "name": "Desain & Pengujian Modul Interface Alert EWS", "dur": 3, "preds": ["ACT-18"]},
    {"id": "ACT-20", "wbs": "6.1.1", "name": "Penyusunan Draft Paper Lengkap Format IMRAD", "dur": 5, "preds": ["ACT-04", "ACT-19"]},
    {"id": "ACT-21", "wbs": "6.1.2", "name": "Finalisasi Slide Presentasi Eksekutif & Review", "dur": 2, "preds": ["ACT-20"]}
]

def add_working_days(start_date, num_days):
    """Add working days (Monday-Friday) to start_date."""
    curr = start_date
    added = 0
    while added < num_days:
        if curr.weekday() < 5:  # Monday to Friday
            added += 1
        if added < num_days:
            curr += timedelta(days=1)
    return curr

def compute_cpm_schedule():
    # Map index
    act_dict = {a['id']: a for a in ACTIVITIES}
    
    # Forward Pass
    for a in ACTIVITIES:
        if not a['preds']:
            a['es'] = 0
        else:
            a['es'] = max(act_dict[p]['ef'] for p in a['preds'])
        a['ef'] = a['es'] + a['dur']

    total_project_duration = max(a['ef'] for a in ACTIVITIES)

    # Successor mapping
    succ_map = {a['id']: [] for a in ACTIVITIES}
    for a in ACTIVITIES:
        for p in a['preds']:
            succ_map[p].append(a['id'])

    # Backward Pass
    for a in reversed(ACTIVITIES):
        succs = succ_map[a['id']]
        if not succs:
            a['lf'] = total_project_duration
        else:
            a['lf'] = min(act_dict[s]['ls'] for s in succs)
        a['ls'] = a['lf'] - a['dur']
        a['tf'] = a['ls'] - a['es']
        a['is_critical'] = (a['tf'] == 0)

    # Free Float
    for a in ACTIVITIES:
        succs = succ_map[a['id']]
        if not succs:
            a['ff'] = a['lf'] - a['ef']
        else:
            a['ff'] = min(act_dict[s]['es'] for s in succs) - a['ef']

    # Compute Calendar Dates (Starting Monday, Oct 5, 2026)
    proj_start = datetime(2026, 10, 5)
    
    # Helper to convert working day offset to date
    def day_to_date(offset_days):
        curr = proj_start
        passed = 0
        while passed < offset_days:
            if curr.weekday() < 5:
                passed += 1
            curr += timedelta(days=1)
        # Advance if weekend
        while curr.weekday() >= 5:
            curr += timedelta(days=1)
        return curr

    for a in ACTIVITIES:
        a['start_date'] = day_to_date(a['es'])
        a['end_date'] = add_working_days(a['start_date'], a['dur'])

    return ACTIVITIES, total_project_duration

def generate_gantt_chart(output_path):
    activities, total_dur = compute_cpm_schedule()
    n = len(activities)

    fig, ax = plt.subplots(figsize=(15, 11), dpi=300)
    
    # Y-coordinates
    y_positions = range(n - 1, -1, -1)
    
    # Colors
    crit_color = "#C62828"      # Crimson Red
    non_crit_color = "#1565C0"  # Enterprise Blue
    float_color = "#81C784"     # Light Green (Slack)

    for idx, a in enumerate(activities):
        y = y_positions[idx]
        bar_color = crit_color if a['is_critical'] else non_crit_color
        
        # Activity Bar
        ax.barh(y, a['dur'], left=a['es'], height=0.55, align='center',
                color=bar_color, edgecolor='#212121', linewidth=1.0, zorder=3)
        
        # Free Float / Total Float indicator
        if a['tf'] > 0:
            ax.barh(y, a['tf'], left=a['ef'], height=0.25, align='center',
                    color=float_color, edgecolor='#4CAF50', linewidth=0.8, linestyle='--',
                    alpha=0.85, zorder=2)
            ax.text(a['ef'] + a['tf'] + 0.3, y, f"TF={a['tf']}d", va='center', fontsize=7.5,
                    color='#2E7D32', fontweight='bold')

        # Label inside or next to bar
        dur_label = f"{a['dur']}d"
        if a['dur'] >= 3:
            ax.text(a['es'] + a['dur'] / 2.0, y, dur_label, ha='center', va='center',
                    color='white', fontweight='bold', fontsize=8, zorder=4)
        else:
            ax.text(a['es'] + a['dur'] + 0.3, y, dur_label, ha='left', va='center',
                    color=bar_color, fontweight='bold', fontsize=8, zorder=4)

    # Y-axis labels: WBS + Code + Name
    y_labels = [f"[{a['wbs']}] {a['id']}: {a['name'][:36]}..." if len(a['name']) > 36 
                else f"[{a['wbs']}] {a['id']}: {a['name']}" for a in activities]
    ax.set_yticks(list(y_positions))
    ax.set_yticklabels(y_labels, fontsize=8.5, fontweight='500', family='sans-serif')

    # X-axis configuration (Working Days 0 to total_dur + 2)
    ax.set_xlim(-1, total_dur + 5)
    ax.set_xlabel("Durasi Jadwal Proyek (Hari Kerja Kalender / Workdays)", fontsize=10, fontweight='bold', labelpad=10)
    ax.set_xticks(range(0, total_dur + 6, 2))
    ax.grid(axis='x', linestyle=':', alpha=0.6, color='#9E9E9E', zorder=1)

    # Title & Subtitle
    plt.title("GANTT CHART JADWAL PROYEK PRE-02 (21 AKTIVITAS DEKOMPOSISI WBS)\n"
              "Sistem Prediksi Probabilitas Keterlambatan Proyek Berbasis Machine Learning | Total Durasi: 46 Hari Kerja",
              fontsize=11.5, fontweight='bold', pad=15, color='#0D47A1')

    # Legend
    crit_patch = patches.Patch(facecolor=crit_color, edgecolor='#212121', label='Aktivitas Kritis (Total Float = 0)')
    non_crit_patch = patches.Patch(facecolor=non_crit_color, edgecolor='#212121', label='Aktivitas Non-Kritis (Total Float > 0)')
    float_patch = patches.Patch(facecolor=float_color, edgecolor='#4CAF50', linestyle='--', label='Kelonggaran Waktu (Total Float / Slack)')
    ax.legend(handles=[crit_patch, non_crit_patch, float_patch], loc='lower right', frameon=True, fontsize=9)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[SUCCESS] Gantt Chart image generated at: {output_path}")

if __name__ == "__main__":
    out_img = os.path.join(os.path.dirname(__file__), "pre02_gantt_chart.png")
    generate_gantt_chart(out_img)
