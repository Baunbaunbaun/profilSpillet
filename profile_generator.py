import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
import os
import glob

# Importer profilerne fra den anden fil
from profiles import PROFILES

# --- MAPPE KONFIGURATION ---
IMAGE_FOLDER = "images"   
OUTPUT_FOLDER = "profiles" 

# Opret output mappen hvis den ikke findes
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# --- HJÆLPEFUNKTIONER ---

def find_image_path(base_name):
    """
    Leder efter et billede med base_name og forskellige endelser (.jpg, .png, etc.)
    Returnerer stien til den første fil den finder, eller None.
    """
    # Liste af fil-endelser vi understøtter
    extensions = [".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"]
    
    for ext in extensions:
        full_path = os.path.join(IMAGE_FOLDER, base_name + ext)
        if os.path.exists(full_path):
            return full_path
            
    return None

def crop_to_target_aspect(pil_img, target_ratio):
    """
    Beskærer billedet (Center Crop) så det passer præcis til mål-formatet.
    """
    img_w, img_h = pil_img.size
    img_ratio = img_w / img_h
    
    if img_ratio > target_ratio:
        # Billedet er for bredt: Beskær siderne
        new_w = int(img_h * target_ratio)
        offset = (img_w - new_w) // 2
        return pil_img.crop((offset, 0, offset + new_w, img_h))
    else:
        # Billedet er for højt: Beskær toppen og bunden
        new_h = int(img_w / target_ratio)
        offset = (img_h - new_h) // 2
        return pil_img.crop((0, offset, img_w, offset + new_h))

# --- GENERATOR FUNKTION ---
def create_card(profile):
    print(f"Genererer kort for: {profile['name']}...")
    
    # A5 Mål
    fig_w_cm = 14.8
    fig_h_cm = 21.0
    fig, ax = plt.subplots(figsize=(fig_w_cm/2.54, fig_h_cm/2.54), dpi=300)
    
    # --- PRINTER-VENLIGT LAYOUT (HVID) ---
    bg_color = '#ffffff' # Hvid baggrund
    text_color = '#000000' # Sort tekst
    bar_bg_color = '#e0e0e0' # Lys grå baggrund til barer
    
    ax.set_facecolor(bg_color)
    fig.patch.set_facecolor(bg_color)
    ax.axis('off')

    # Farve tema
    accent = profile.get("theme_color", "#e63946")

    # 1. Billede Håndtering (Smart Search + Crop)
    # Vi fjerner evt. filendelse fra profil-navnet for en sikkerheds skyld
    base_name_clean = os.path.splitext(profile["image_base_name"])[0]
    image_path = find_image_path(base_name_clean)
    
    # Definer hvor billedet skal sidde [left, right, bottom, top]
    extent_coords = [0.1, 0.9, 0.55, 0.95] 
    
    box_width_rel = extent_coords[1] - extent_coords[0]
    box_height_rel = extent_coords[3] - extent_coords[2]
    target_aspect = (box_width_rel * fig_w_cm) / (box_height_rel * fig_h_cm)

    if image_path:
        try:
            img = Image.open(image_path)
            img_cropped = crop_to_target_aspect(img, target_aspect)
            img_arr = np.array(img_cropped)
            ax.imshow(img_arr, extent=extent_coords, transform=ax.transAxes, aspect='auto', zorder=1)
        except Exception as e:
            print(f"Fejl ved billede: {e}")
    else:
        print(f"ADVARSEL: Kunne ikke finde billede for {base_name_clean} (søgte efter jpg/png)")
        # Tegn en grå kasse hvis billede mangler
        rect_missing = patches.Rectangle((0.1, 0.55), 0.8, 0.4, facecolor='#f0f0f0', transform=ax.transAxes)
        ax.add_patch(rect_missing)
        ax.text(0.5, 0.75, "BILLEDE MANGLER", color='#999', ha='center', transform=ax.transAxes)

    # Ramme om billede (Accent farve)
    rect = patches.Rectangle((0.095, 0.545), 0.81, 0.41, linewidth=3, edgecolor=accent, facecolor='none', transform=ax.transAxes, zorder=2)
    ax.add_patch(rect)

    # 2. Tekst: Navn og Titel
    ax.text(0.5, 0.50, profile["name"].upper(), color=text_color, ha='center', va='top', fontsize=22, fontweight='bold', transform=ax.transAxes)
    ax.text(0.5, 0.46, profile["title"], color=accent, ha='center', va='top', fontsize=18, fontweight='bold', transform=ax.transAxes, style='italic')

    # 3. Stats Søjler
    y_pos = 0.38
    bar_height = 0.03
    gap = 0.02

    for label, score in profile["stats"]:
        # Label (Sort tekst)
        ax.text(0.1, y_pos, label, color=text_color, ha='left', va='center', fontsize=10, transform=ax.transAxes, fontweight='bold')
        # Score Tal (Sort tekst)
        ax.text(0.9, y_pos, str(score), color=text_color, ha='right', va='center', fontsize=12, transform=ax.transAxes, fontweight='bold')
        
        # Bar baggrund (Lys grå)
        bg_bar = patches.Rectangle((0.1, y_pos - 0.025), 0.8, 0.015, facecolor=bar_bg_color, transform=ax.transAxes)
        ax.add_patch(bg_bar)
        
        # Score Bar
        # Hvis score er meget lav, gør vi den mørkegrå for kontrast, ellers accent
        bar_c = accent if score > 10 else '#999999'
        display_score = max(score, 1) 
        score_width = 0.8 * (display_score / 100)
        score_bar = patches.Rectangle((0.1, y_pos - 0.025), score_width, 0.015, facecolor=bar_c, transform=ax.transAxes)
        ax.add_patch(score_bar)
        y_pos -= (bar_height + gap)

    # 4. Special Ability Box (Lys boks med mørk kant/tekst)
    box_y = 0.05
    box_h = 0.08
    # Lys grå baggrund, mørk grå kant
    box_rect = patches.FancyBboxPatch((0.1, box_y), 0.8, box_h, boxstyle="round,pad=0.02", facecolor='#f8f9fa', edgecolor='#cccccc', transform=ax.transAxes)
    ax.add_patch(box_rect)

    ax.text(0.5, box_y + box_h - 0.01, "SPECIAL ABILITY", color='#666666', ha='center', va='top', fontsize=8, transform=ax.transAxes)
    ax.text(0.5, box_y + 0.03, profile["ability_title"], color=text_color, ha='center', va='center', fontsize=12, fontweight='bold', transform=ax.transAxes)
    ax.text(0.5, box_y + 0.01, profile["ability_desc"], color='#444444', ha='center', va='center', fontsize=8, transform=ax.transAxes)

    # Gem filen
    safe_name = profile["name"].replace(" ", "_").lower()
    filename = f"bilkort_{safe_name}.png"
    save_path = os.path.join(OUTPUT_FOLDER, filename)
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0, dpi=300)
    plt.close()
    print(f"-> Gemt som {save_path}")

# --- START ---
if __name__ == "__main__":
    create_card(PROFILES[0]) # Test kørsel af den første for at se om det virker
    print("Test færdig. Kører alle...")
    for p in PROFILES:
        create_card(p)