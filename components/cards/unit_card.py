# components/cards/unit_card.py
import antigravity as ag
from styles.theme import VIPColors

def unit_card(nome: str, local: str, modalidades: str, texto_apoio: str, cta_text: str = "Ver Horários e Agendar") -> ag.Component:
    return ag.box(
        # Estilização do cartão
        background_color=VIPColors.text_light,
        border_radius="15px",
        box_shadow="0 4px 15px rgba(0,0,0,0.05)",
        padding="2rem",
        display="flex",
        flex_direction="column",
        height="100%", # Para manter os cartões alinhados
        _hover={"transform": "translateY(-5px)", "box_shadow": "0 8px 25px rgba(0,0,0,0.1)", "transition": "0.3s"},
        
        children=[
            # Nome da Unidade
            ag.heading(nome, size="lg", color=VIPColors.secondary, margin_bottom="0.5rem"),
            
            # Localização (com um ícone de pino 📍)
            ag.text(f"📍 {local}", font_weight="bold", color=VIPColors.text_dark, margin_bottom="1rem"),
            
            # Modalidades em destaque
            ag.box(
                background_color=VIPColors.highlight,
                padding="0.25rem 0.75rem",
                border_radius="20px",
                display="inline-block",
                margin_bottom="1rem",
                children=[
                    ag.text(modalidades, font_size="0.85rem", font_weight="bold", color=VIPColors.secondary)
                ]
            ),
            
            # Texto explicativo (ocupa o espaço flexível para empurrar o botão para baixo)
            ag.text(texto_apoio, color=VIPColors.text_dark, margin_bottom="1.5rem", flex_grow="1"),
            
            # Botão de Ação
            ag.button(
                cta_text,
                width="100%",
                background_color=VIPColors.primary,
                color=VIPColors.text_light,
                border_radius="8px",
                padding="0.75rem",
                font_weight="bold",
                _hover={"opacity": "0.9"}
            )
        ]
    )