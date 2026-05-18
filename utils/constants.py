# utils/constants.py
import urllib.parse

# Número oficial de atendimento (Formato internacional: 55 + DDD + Número)
WHATSAPP_NUMBER = "5521999999999"  # Substitua pelo número real da VIP

def gerar_link_whatsapp(mensagem: str) -> str:
    """
    Recebe um texto normal e transforma num link válido para abrir o WhatsApp.
    O urllib.parse.quote codifica os espaços (para %20), acentos, etc.
    """
    mensagem_codificada = urllib.parse.quote(mensagem)
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={mensagem_codificada}"