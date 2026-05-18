# components/navigation/navbar.py
import antigravity as ag
from styles.theme import VIPColors, navbar_style

def navbar() -> ag.Component:
    return ag.nav(
        # Logotipo inserido usando o arquivo exportado
        ag.image(
            src="/assets/branding/VIP-COLOR.png", 
            alt="Logo VIP Esportes", 
            height="60px",
            cursor="pointer",
            on_click=ag.redirect("/")
        ),
        
        # Menu central
        ag.hstack(
            ag.link("Home", href="/", font_weight="bold", color=VIPColors.text_dark),
            ag.link("A VIP", href="/a-vip", color=VIPColors.text_dark),
            
            # Dropdown para as modalidades
            ag.menu(
                ag.menu_button("Modalidades ▼", color=VIPColors.text_dark),
                ag.menu_list(
                    ag.menu_item("Beach Tennis", href="/modalidades/beach-tennis"),
                    ag.menu_item("Vôlei de Praia", href="/modalidades/volei-de-praia"),
                    ag.menu_item("Futevôlei", href="/modalidades/futevolei")
                )
            ),
            
            ag.link("Unidades e Horários", href="/unidades", color=VIPColors.text_dark),
            ag.link("Contato", href="/contato", color=VIPColors.text_dark),
            
            # Destaque dinâmico no menu
            ag.link(
                "🎾 ITF BT 400 Copacabana", 
                href="/eventos/itf-bt-400", 
                color=VIPColors.primary, 
                font_weight="bold"
            ),
            spacing="1.5rem"
        ),
        
        # Botão Call to Action (CTA)
        ag.button(
            "Agendar Aula Experimental", 
            background_color=VIPColors.primary, 
            color=VIPColors.text_light,
            border_radius="25px",
            padding="0.75rem 1.5rem",
            _hover={"opacity": "0.9"}
        ),
        
        style=navbar_style
    )