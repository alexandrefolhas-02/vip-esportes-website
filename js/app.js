/* js/app.js */

document.addEventListener('DOMContentLoaded', () => {
  // --- 1. MOBILE MENU TOGGLE ---
  const menuToggle = document.getElementById('menuToggle');
  const navMenu = document.getElementById('navMenu');
  
  if (menuToggle && navMenu) {
    menuToggle.addEventListener('click', () => {
      navMenu.classList.toggle('active');
      
      // Animate the hamburger button
      const spans = menuToggle.querySelectorAll('span');
      if (navMenu.classList.contains('active')) {
        spans[0].style.transform = 'rotate(45deg) translate(6px, 6px)';
        spans[1].style.opacity = '0';
        spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
      } else {
        spans[0].style.transform = 'none';
        spans[1].style.opacity = '1';
        spans[2].style.transform = 'none';
      }
    });
  }

  // Close menu when clicking a link
  const navLinks = document.querySelectorAll('.nav-link');
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      if (navMenu && navMenu.classList.contains('active')) {
        navMenu.classList.remove('active');
        const spans = menuToggle.querySelectorAll('span');
        spans[0].style.transform = 'none';
        spans[1].style.opacity = '1';
        spans[2].style.transform = 'none';
      }
    });
  });

  // --- 2. DROPDOWN ACCORDION ON MOBILE ---
  const dropdown = document.querySelector('.dropdown');
  if (dropdown) {
    dropdown.addEventListener('click', (e) => {
      if (window.innerWidth <= 992) {
        // Only toggle dropdown if clicking the trigger itself
        if (e.target.classList.contains('nav-link') || e.target.parentElement.classList.contains('dropdown')) {
          e.preventDefault();
          dropdown.classList.toggle('active');
        }
      }
    });
  }

  // --- 3. DYNAMIC SMART WHATSAPP CTA ---
  const whatsappFloat = document.getElementById('whatsappFloat');
  if (whatsappFloat) {
    // Official VIP Esportes number (international format: Country + DDD + Number)
    const WHATSAPP_NUMBER = "5521999999999"; // Replace with official number
    
    // Messages mapped by context/page
    const messages = {
      'home': "Olá! Estava a ver o site da VIP Esportes e gostaria de agendar uma aula experimental.",
      'beach-tennis': "Olá! Gostaria de agendar a minha aula experimental de Beach Tennis na VIP. Como funcionam as turmas?",
      'volei-de-praia': "Olá! Tenho interesse nas aulas de Vôlei de Praia (Metodologia Paula Pequeno). Podem passar-me os horários?",
      'unidades': "Olá! Estava a ver as unidades no site e gostava de saber qual é a mais próxima de mim para agendar um treino.",
      'contato': "Olá! Gostaria de obter mais informações sobre a VIP Esportes."
    };

    // Determine context based on current page URL
    let context = 'home';
    const path = window.location.pathname.toLowerCase();
    
    if (path.includes('beach-tennis')) {
      context = 'beach-tennis';
    } else if (path.includes('volei-de-praia')) {
      context = 'volei-de-praia';
    } else if (path.includes('unidades')) {
      context = 'unidades';
    } else if (path.includes('contato')) {
      context = 'contato';
    }

    const selectedMessage = messages[context] || messages['home'];
    const encodedMessage = encodeURIComponent(selectedMessage);
    
    // Update the link href
    whatsappFloat.href = `https://wa.me/${WHATSAPP_NUMBER}?text=${encodedMessage}`;
  }

  // --- 4. SCROLL REVEAL ANIMATIONS ---
  const revealElements = document.querySelectorAll('.unit-card, .modality-card, .methodology-box, .highlight-banner, .two-column');
  
  // Set initial hidden styles for scroll reveal
  revealElements.forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'opacity 0.8s ease, transform 0.8s cubic-bezier(0.25, 0.8, 0.25, 1)';
  });

  const revealOnScroll = () => {
    const triggerBottom = window.innerHeight * 0.85;
    
    revealElements.forEach(el => {
      const elTop = el.getBoundingClientRect().top;
      
      if (elTop < triggerBottom) {
        el.style.opacity = '1';
        el.style.transform = 'translateY(0)';
      }
    });
  };

  // Run once on load and bind to scroll
  revealOnScroll();
  window.addEventListener('scroll', revealOnScroll);
});
