# styles/theme.py
import antigravity as ag

class VIPColors:
    # Cores baseadas no arquivo VIP-COLOR.png
    primary = "#ff6600"       # Exemplo: Laranja vibrante da marca
    secondary = "#001f3f"     # Exemplo: Azul marinho profundo
    background = "#f4f4f4"    # Fundo padrão claro
    text_dark = "#1a1a1a"     # Texto principal
    text_light = "#ffffff"    # Texto sobre fundos escuros
    highlight = "#ffcc00"     # Amarelo para destaques

# Estilos reutilizáveis para os componentes
navbar_style = {
    "padding": "1rem 2rem",
    "background_color": VIPColors.text_light,
    "box_shadow": "0 2px 10px rgba(0,0,0,0.1)",
    "display": "flex",
    "justify_content": "space-between",
    "align_items": "center",
    "position": "sticky",
    "top": "0",
    "z_index": "100"
}