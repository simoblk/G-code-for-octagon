# G-code Octagon Generator

A Python script that generates G-code for machining an octagon shape on a CNC machine. 
The script dynamically calculates coordinates based on the input `SW` (width across flats) and allows customization of the `Z-depth` parameter.

## Features
- Interactive input prompts for `SW` and optional `Z-depth`.
- Dynamically calculates `X` and `C` coordinates for the octagon toolpath.
- Includes tool compensation (G42/G40) and precise positioning commands.
- Displays a summary of calculated values for verification.

## Usage
1. Run the script in a Python environment.
2. Enter the `SW` (width across flats) value when prompted. The value must be greater than 0.
3. Optionally, provide a custom `Z-depth` (e.g., `-40`) or press Enter to use the default (`-40`).
4. The script will output the generated G-code along with a summary of the calculated values.

## Example
```python
╔══════════════════════════════╗
║  G-code Generator - Octogone ║
╚══════════════════════════════╝

➤ Dkhl SW (Width Across Flats): 20
➤ Dkhl Z-depth (Ex: -40) [Default=-40]: -40

════════ G-code ════════

G112
G01Z-40F5000  
G01G42X140C0
G01X40
G01X21.62C0F700  
G01X8.28C7.65 
G01X8.28C10.83 
G01X-8.28C7.65  
G01X-21.62C0
G01X-8.28C-7.65 
G01X8.28C-10.83
G01X8.28C-7.65 
G01X21.62C0  
G01X8.28C7.65  
G1G40X140C0F5000
G01X140C0
G01Z20
G113

═══════════════════════════
► SW: 20 | RX: 21.62 | GX: 8.28 | C: 7.65 | C Intermediate: 10.83
═══════════════════════════
