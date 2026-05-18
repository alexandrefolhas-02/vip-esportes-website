# components/ui/whatsapp_button.py
import antigravity as ag
from utils.constants import gerar_link_whatsapp
from styles.theme import VIPColors

def whatsapp_cta(contexto: str, flutuante: bool = False, texto_botao: str = "Falar no WhatsApp") -> ag.Component:
    
    # 1. Inteligência: Definir a mensagem com base no contexto (página atual)
    mensagens = {
        "home": "Olá! Estava a ver o site da VIP Esportes e gostaria de agendar uma aula experimental.",
        "beach_tennis": "Olá! Gostaria de agendar a minha aula experimental de Beach Tennis na VIP. Como funcionam as turmas?",
        "volei_de_praia": "Olá! Tenho interesse nas aulas de Vôlei de Praia (Metodologia Paula Pequeno). Podem passar-me os horários?",
        "unidades": "Olá! Estava a ver as unidades no site e gostava de saber qual é a mais próxima de mim para agendar um treino.",
        "condominio": "Olá! Sou síndico/morador e gostaria de saber como levar a VIP Esportes para o meu condomínio.",
        "padrao": "Olá! Gostaria de obter mais informações sobre a VIP Esportes."
    }
    
    # Seleciona a mensagem certa ou usa a padrão se o contexto não existir na lista
    mensagem_escolhida = mensagens.get(contexto, mensagens["padrao"])
    
    # 2. Gera o link com a mensagem já embutida
    link_wa = gerar_link_whatsapp(mensagem_escolhida)
    
    # 3. Estilização: Botão Flutuante (canto inferior direito) vs Botão Normal (meio da página)
    if flutuante:
        estilo = {
            "position": "fixed",
            "bottom": "30px",
            "right": "30px",
            "background_color": "#25D366", # Verde oficial do WhatsApp
            "color": "white",
            "border_radius": "50px",
            "padding": "1rem 1.5rem",
            "box_shadow": "0 4px 15px rgba(37, 211, 102, 0.4)",
            "z_index": "1000",
            "display": "flex",
            "align_items": "center",
            "gap": "0.5rem",
            "_hover": {"transform": "scale(1.1)", "transition": "0.3s"}
        }
        texto = "💬 Agende a sua Aula"
    else:
        estilo = {
            "background_color": "#25D366",
            "color": "white",
            "border_radius": "8px",
            "padding": "0.75rem 1.5rem",
            "font_weight": "bold",
            "_hover": {"opacity": "0.9"}
        }
        texto = texto_botao

    # 4. Retorna o componente clicável
    return ag.link(
        href=link_wa,
        target="_blank", # Abre num novo separador
        children=[ag.text(texto)],
        style=estilo
    )