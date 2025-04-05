import math

def generate_octagon_gcode():
    print("""
╔══════════════════════════════╗
║  G-code Generator - Octogone ║
╚══════════════════════════════╝
""")
    
    # Input dyal SW
    while True:
        try:
            sw = float(input("➤ Dkhl SW (Width Across Flats): "))
            if sw <= 0:
                print("✖ Error: SW khassha tkoun > 0!")
                continue
            break
        except:
            print("✖ Error: Dkhl nombre valide!")

    # Input dyal Z-depth (optional)
    z_depth = input("➤ Dkhl Z-depth (Ex: -40) [Default=-40]: ").strip() or "-40"

    # L7sabat DYALEK (b7al ma bghiti)
    x_hamra = round(sw / math.cos(math.pi/8), 2)
    x_khadra = round(sw * 0.414, 2)  # 8.28/20 ≈ 0.414
    c = round(sw * 0.3825, 2)        # 7.65/20 ≈ 0.3825
    c_intermediate = round(sw * 0.54125, 2)  # 10.825/20 ≈ 0.54125

    # Génération G-code (EXACT b7al ma bghiti)
    gcode = f"""
G112
G01Z{z_depth}F5000  
G01G42X140C0
G01X40
G01X{x_hamra}C0F700  
G01X{x_khadra}C{c} 
G01X{x_khadra}C{c_intermediate} 
G01X{-x_khadra}C{c}  
G01X{-x_hamra}C0
G01X{-x_khadra}C-{c} 
G01X{x_khadra}C-{c_intermediate}
G01X{x_khadra}C-{c} 
G01X{x_hamra}C0  
G01X{x_khadra}C{c}  
G1G40X140C0F5000
G01X140C0
G01Z20
G113
"""
    print("\n════════ G-code S7i7 ════════")
    print(gcode)
    print("═══════════════════════════")
    print(f"► SW: {sw} | X Hamra: {x_hamra} | X Khadra: {x_khadra} | C: {c} | C Intermediate: {c_intermediate}")
    print("═══════════════════════════")

# Lancer le programme
generate_octagon_gcode()