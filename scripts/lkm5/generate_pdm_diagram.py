# -*- coding: utf-8 -*-
"""
Generator for PDM Network Diagram Image
Outputs a publication-quality diagram of the Critical Path Method (CPM)
Pertemuan 5: Manajemen Jadwal Proyek (Bagian I)
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_pdm_diagram(output_path):
    fig, ax = plt.subplots(figsize=(13, 6), dpi=300)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 5.5)
    ax.axis('off')

    # Color palette
    crit_edge = "#B71C1C"       # Deep red
    crit_fill = "#FFEBEE"       # Very soft red/pink
    crit_hdr = "#FFCDD2"        # Soft red header
    non_crit_edge = "#1565C0"   # Deep blue
    non_crit_fill = "#E3F2FD"   # Soft blue
    non_crit_hdr = "#BBDEFB"    # Soft blue header
    text_color = "#1A1A1A"
    arrow_crit = "#C62828"
    arrow_non = "#546E7A"

    nodes = {
        'A': {'x': 1.0, 'y': 1.75, 'dur': 3, 'es': 0, 'ef': 3, 'ls': 0, 'lf': 3, 'tf': 0, 'crit': True, 'name': 'Aktivitas A'},
        'B': {'x': 4.6, 'y': 3.15, 'dur': 4, 'es': 3, 'ef': 7, 'ls': 4, 'lf': 8, 'tf': 1, 'crit': False, 'name': 'Aktivitas B'},
        'C': {'x': 4.6, 'y': 0.35, 'dur': 5, 'es': 3, 'ef': 8, 'ls': 3, 'lf': 8, 'tf': 0, 'crit': True, 'name': 'Aktivitas C'},
        'D': {'x': 8.2, 'y': 1.75, 'dur': 2, 'es': 8, 'ef': 10, 'ls': 8, 'lf': 10, 'tf': 0, 'crit': True, 'name': 'Aktivitas D'},
        'E': {'x': 11.8, 'y': 1.75, 'dur': 3, 'es': 10, 'ef': 13, 'ls': 10, 'lf': 13, 'tf': 0, 'crit': True, 'name': 'Aktivitas E'},
    }

    box_w = 2.4
    box_h = 1.6

    # Draw Nodes
    for key, d in nodes.items():
        x, y = d['x'], d['y']
        is_c = d['crit']
        edge_c = crit_edge if is_c else non_crit_edge
        fill_c = crit_fill if is_c else non_crit_fill
        hdr_c = crit_hdr if is_c else non_crit_hdr

        # Outer box
        rect = patches.FancyBboxPatch((x, y), box_w, box_h,
                                      boxstyle="round,pad=0.03,rounding_size=0.08",
                                      linewidth=2.2 if is_c else 1.6,
                                      edgecolor=edge_c,
                                      facecolor=fill_c)
        ax.add_patch(rect)

        # Dividing lines inside node (Standard 3-row PDM representation)
        row_h = box_h / 3.0
        # Horizontal line 1 (between top row and middle)
        ax.plot([x, x + box_w], [y + 2 * row_h, y + 2 * row_h], color=edge_c, linewidth=1.0)
        # Horizontal line 2 (between middle and bottom row)
        ax.plot([x, x + box_w], [y + row_h, y + row_h], color=edge_c, linewidth=1.0)
        
        # Vertical dividers in top row: ES (left), Duration (center), EF (right)
        col_w = box_w / 3.0
        ax.plot([x + col_w, x + col_w], [y + 2 * row_h, y + box_h], color=edge_c, linewidth=0.9)
        ax.plot([x + 2 * col_w, x + 2 * col_w], [y + 2 * row_h, y + box_h], color=edge_c, linewidth=0.9)

        # Vertical dividers in bottom row: LS (left), Float (center), LF (right)
        ax.plot([x + col_w, x + col_w], [y, y + row_h], color=edge_c, linewidth=0.9)
        ax.plot([x + 2 * col_w, x + 2 * col_w], [y, y + row_h], color=edge_c, linewidth=0.9)

        # Top row text: ES, Dur, EF
        ax.text(x + 0.5 * col_w, y + 2.5 * row_h, f"{d['es']}", ha='center', va='center', fontsize=9.5, fontweight='bold', color=text_color)
        ax.text(x + 1.5 * col_w, y + 2.5 * row_h, f"D: {d['dur']}", ha='center', va='center', fontsize=9, fontweight='bold', color=edge_c)
        ax.text(x + 2.5 * col_w, y + 2.5 * row_h, f"{d['ef']}", ha='center', va='center', fontsize=9.5, fontweight='bold', color=text_color)

        # Middle row text: Activity ID & Label
        lbl_status = " [KRITIS]" if is_c else ""
        ax.text(x + 0.5 * box_w, y + 1.5 * row_h, f"{d['name']}{lbl_status}", ha='center', va='center', 
                fontsize=9.5, fontweight='bold', color=edge_c)

        # Bottom row text: LS, Float, LF
        ax.text(x + 0.5 * col_w, y + 0.5 * row_h, f"{d['ls']}", ha='center', va='center', fontsize=9.5, fontweight='bold', color=text_color)
        ax.text(x + 1.5 * col_w, y + 0.5 * row_h, f"TF: {d['tf']}", ha='center', va='center', fontsize=9, fontweight='bold', color="#2E7D32" if d['tf'] > 0 else "#C62828")
        ax.text(x + 2.5 * col_w, y + 0.5 * row_h, f"{d['lf']}", ha='center', va='center', fontsize=9.5, fontweight='bold', color=text_color)

    # Connections (Arrows)
    arrows = [
        # (from, to, is_crit, rad, annot)
        ('A', 'B', False, 0.15, 'FS'),
        ('A', 'C', True, -0.15, 'FS (Kritis)'),
        ('B', 'D', False, -0.15, 'FS'),
        ('C', 'D', True, 0.15, 'FS (Kritis)'),
        ('D', 'E', True, 0.0, 'FS (Kritis)'),
    ]

    for start_k, end_k, is_c, rad, annot in arrows:
        n1 = nodes[start_k]
        n2 = nodes[end_k]
        x1 = n1['x'] + box_w
        y1 = n1['y'] + box_h / 2.0
        x2 = n2['x']
        y2 = n2['y'] + box_h / 2.0

        arr_color = arrow_crit if is_c else arrow_non
        lw = 2.4 if is_c else 1.4

        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="-|>", color=arr_color, lw=lw,
                                    mutation_scale=16,
                                    connectionstyle=f"arc3,rad={rad}"))

    # Title & Legend Box
    ax.text(8.0, 5.15, "PREPARED NETWORK DIAGRAM: PRECEDENCE DIAGRAMMING METHOD (PDM)",
            ha='center', va='center', fontsize=12, fontweight='bold', color='#0D47A1')
    ax.text(8.0, 4.80, "Proyek Analisis Jalur Kritis (Critical Path Method - CPM) | Total Durasi: 13 Hari Kalender",
            ha='center', va='center', fontsize=10, fontstyle='italic', color='#37474F')

    # Legend patch
    crit_legend = patches.Patch(facecolor=crit_fill, edgecolor=crit_edge, linewidth=1.5, label='Jalur Kritis: A → C → D → E (TF = 0, Durasi = 13 Hari)')
    non_crit_legend = patches.Patch(facecolor=non_crit_fill, edgecolor=non_crit_edge, linewidth=1.5, label='Jalur Non-Kritis: A → B → D → E (TF = 1 Hari)')
    ax.legend(handles=[crit_legend, non_crit_legend], loc='lower center', ncol=2, frameon=True, fontsize=9.5)

    # Node Anatomy Legend at top-left
    ax.text(1.0, 4.90, "Format Node PDM Standar:", fontsize=8.5, fontweight='bold', color='#333333')
    ax.text(1.0, 4.60, "[ ES  |  Durasi  |  EF  ]\n[  Nama Aktivitas (ID) ]\n[ LS  |  Float   |  LF  ]", 
            fontsize=8, family='monospace', color='#333333',
            bbox=dict(boxstyle='square,pad=0.3', facecolor='#F5F5F5', edgecolor='#CCCCCC', lw=0.8))

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[SUCCESS] Network Diagram successfully generated at: {output_path}")

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "pdm_network_diagram.png")
    generate_pdm_diagram(out)
