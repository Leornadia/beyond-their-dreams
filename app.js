/**
 * Beyond Their Dreams - App Logic & SPA Router
 * Crafted by Antigravity IDE
 */

document.addEventListener('DOMContentLoaded', () => {
  // Initialize Core Modules
  initRouter();
  initStickyHeader();
  initMobileMenu();
  initModals();
  initForms();
  initVideoPlayer();
  checkAccordionCapabilities();
});

/* ==========================================================================
   SPA ROUTER (Client-side Page Switching)
   ========================================================================== */
function initRouter() {
  const navLinks = document.querySelectorAll('.nav-link, .nav-trigger');
  const views = document.querySelectorAll('.main-content .view');

  function switchView(targetId) {
    // Normalize targetId (e.g. remove '#')
    const viewId = targetId.replace('#', '');
    const activeView = document.getElementById(`view-${viewId}`);

    if (activeView) {
      // 1. Hide all views
      views.forEach(view => {
        view.classList.remove('active');
      });

      // 2. Show active view
      activeView.classList.add('active');

      // 3. Update active nav link classes
      document.querySelectorAll('.nav-link').forEach(link => {
        if (link.getAttribute('data-view') === viewId) {
          link.classList.add('active');
        } else {
          link.classList.remove('active');
        }
      });

      // 4. Scroll to top of window smoothly
      window.scrollTo({ top: 0, behavior: 'smooth' });

      // 5. Close mobile menu if open
      const navMenu = document.getElementById('navMenu');
      const mobileToggle = document.getElementById('mobileToggle');
      if (navMenu.classList.contains('active')) {
        navMenu.classList.remove('active');
        mobileToggle.classList.remove('active');
      }
    }
  }

  // Handle click triggers on navigation links
  navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      const href = link.getAttribute('href');
      const dataView = link.getAttribute('data-view');
      
      // If it's a dynamic router switch
      if (dataView) {
        e.preventDefault();
        window.location.hash = dataView;
        switchView(dataView);
      }
    });
  });

  // Handle Direct Link/Reload deep-linking via Hash
  function handleHash() {
    const currentHash = window.location.hash || '#home';
    switchView(currentHash);
  }

  // Watch for back/forward navigation button clicks
  window.addEventListener('hashchange', handleHash);
  
  // Trigger initial routing pass
  handleHash();
}

/* ==========================================================================
   STICKY GLASSMORPHIC HEADER
   ========================================================================== */
function initStickyHeader() {
  const header = document.getElementById('mainHeader');
  const shrinkDistance = 50;

  window.addEventListener('scroll', () => {
    if (window.scrollY > shrinkDistance) {
      header.classList.add('shrink');
    } else {
      header.classList.remove('shrink');
    }
  });
}

/* ==========================================================================
   MOBILE HAMBURGER MENU
   ========================================================================== */
function initMobileMenu() {
  const mobileToggle = document.getElementById('mobileToggle');
  const navMenu = document.getElementById('navMenu');

  mobileToggle.addEventListener('click', () => {
    mobileToggle.classList.toggle('active');
    navMenu.classList.toggle('active');
  });

  // Close when clicking outside header container on mobile
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.header-container') && navMenu.classList.contains('active')) {
      mobileToggle.classList.remove('active');
      navMenu.classList.remove('active');
    }
  });
}

/* ==========================================================================
   HIGH-CONVERSION MODAL SYSTEMS
   ========================================================================== */
function initModals() {
  const modal = document.getElementById('bookingModal');
  const closeBtns = document.querySelectorAll('.modal-close, .modal-close-btn');
  const triggerBtns = document.querySelectorAll('.trigger-booking, #headerCta');
  const packageInput = document.getElementById('selectedPackage');
  const modalHeaderTitle = document.querySelector('.modal-header h2');
  const modalHeaderBadge = document.querySelector('.modal-header .badge');

  function openModal(pkgName = 'Free Clarity Call') {
    // Dynamically adjust modal values based on what package was clicked
    packageInput.value = pkgName;
    
    if (pkgName !== 'Free Clarity Call') {
      modalHeaderTitle.textContent = `Apply for: ${pkgName.split(' - ')[0]}`;
      modalHeaderBadge.textContent = 'Bespoke zoom support package setup';
    } else {
      modalHeaderTitle.textContent = 'Book a Free Clarity Call';
      modalHeaderBadge.textContent = 'Free Call • 15 Minutes • Virtual Zoom';
    }

    // Reset success/form states
    document.getElementById('modalBookingForm').style.display = 'flex';
    document.getElementById('bookingSuccess').style.display = 'none';

    modal.classList.add('active');
    document.body.style.overflow = 'hidden'; // Lock body scroll behind modal
  }

  function closeModal() {
    modal.classList.remove('active');
    document.body.style.overflow = ''; // Unlock body scroll
  }

  triggerBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const pkg = btn.getAttribute('data-pkg') || 'Free Clarity Call';
      openModal(pkg);
    });
  });

  closeBtns.forEach(btn => {
    btn.addEventListener('click', closeModal);
  });

  // Close when clicking on background backdrop blur
  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      closeModal();
    }
  });
}

/* ==========================================================================
   LEAD CAPTURING & SCHEDULER SIMULATION
   ========================================================================== */
function initForms() {
  // 1. Modal Booking Form Submissions
  const bookingForm = document.getElementById('modalBookingForm');
  const bookingSuccessBlock = document.getElementById('bookingSuccess');

  bookingForm.addEventListener('submit', (e) => {
    e.preventDefault();
    
    // Extract parameters
    const name = document.getElementById('parentName').value;
    const email = document.getElementById('parentEmail').value;
    const age = document.getElementById('babyAge').value;
    const challenge = document.getElementById('primaryChallenge').value;
    const pkg = document.getElementById('selectedPackage').value;

    console.log('✓ High-Intent Lead Captured:', { name, email, age, challenge, pkg });

    // Store lead locally for reference/analytics sandbox demo
    const leads = JSON.parse(localStorage.getItem('btd_leads') || '[]');
    leads.push({ name, email, age, challenge, pkg, timestamp: new Date().toISOString() });
    localStorage.setItem('btd_leads', JSON.stringify(leads));

    // Animate successful callback screen
    bookingForm.style.display = 'none';
    bookingSuccessBlock.style.display = 'block';
  });

  // 2. Footer Newsletter / MailChimp Integration Simulation
  const newsletterForm = document.getElementById('newsletterForm');
  const newsletterSuccess = document.getElementById('newsletterSuccess');

  newsletterForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = document.getElementById('newsletterEmail').value;
    console.log('✓ Newsletter Subscribed:', email);

    // Save lead
    const subscriptions = JSON.parse(localStorage.getItem('btd_newsletter') || '[]');
    subscriptions.push({ email, timestamp: new Date().toISOString() });
    localStorage.setItem('btd_newsletter', JSON.stringify(subscriptions));

    // Show MailChimp Success Reassurance
    newsletterForm.reset();
    newsletterSuccess.style.display = 'block';
    setTimeout(() => {
      newsletterSuccess.style.opacity = '1';
    }, 50);

    // Fade success message out after 8 seconds
    setTimeout(() => {
      newsletterSuccess.style.opacity = '0';
      setTimeout(() => {
        newsletterSuccess.style.display = 'none';
      }, 500);
    }, 8000);
  });

  // 3. Courses Coming-Soon Waitlist Form
  const waitlistForm = document.getElementById('waitlistForm');
  const waitlistSuccess = document.getElementById('waitlistSuccess');

  waitlistForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = document.getElementById('waitlistEmail').value;
    console.log('✓ Course Waitlist Captured:', email);

    // Save waitlist lead
    const waitlist = JSON.parse(localStorage.getItem('btd_waitlists') || '[]');
    waitlist.push({ email, course: 'Beyond Sensory: Sleep & The Nervous System', timestamp: new Date().toISOString() });
    localStorage.setItem('btd_waitlists', JSON.stringify(waitlist));

    // Display success
    waitlistForm.reset();
    waitlistSuccess.style.display = 'block';
    setTimeout(() => {
      waitlistSuccess.style.opacity = '1';
    }, 50);

    setTimeout(() => {
      waitlistSuccess.style.opacity = '0';
      setTimeout(() => {
        waitlistSuccess.style.display = 'none';
      }, 500);
    }, 8000);
  });
}

/* ==========================================================================
   HOMEPAGE CLARITY VIDEO CONTROLS
   ========================================================================== */
function initVideoPlayer() {
  const playBtn = document.getElementById('playVideoBtn');
  const placeholder = document.querySelector('.video-placeholder');

  if (playBtn) {
    playBtn.addEventListener('click', () => {
      // Nicole's clarity video recorded in landscape format as requested.
      // We will dynamically replace placeholder image with a responsive video tag.
      placeholder.innerHTML = `
        <video controls autoplay class="video-cover" style="width: 100%; height: 100%; object-fit: cover;">
          <source src="https://www.w3schools.com/html/mov_bbb.mp4" type="video/mp4">
          Your browser does not support HTML5 video playing.
        </video>
      `;
    });
  }
}

/* ==========================================================================
   DISCLOSURES ACCESS CRITICAL CAPABILITIES FEATURE-DETECTION FALLBACK
   ========================================================================== */
function checkAccordionCapabilities() {
  // Feature-detect native exclusive disclosures support (details name="..." attribute)
  // Standard details element has Baseline Widely-Available support, so it works flawlessly.
  // The 'name' attribute which allows mutually-exclusive groups is widely supported now,
  // but if the browser doesn't enforce it, we can fallback to standard single-accordion toggle.
  
  const detailsElements = document.querySelectorAll('.disclosure[name="service-accordion"]');
  
  if (detailsElements.length > 0) {
    detailsElements.forEach(detail => {
      detail.addEventListener('toggle', () => {
        if (detail.open) {
          // If the browser doesn't natively close other accordions in the named set,
          // we manually enforce exclusivity to protect layout scannability.
          detailsElements.forEach(otherDetail => {
            if (otherDetail !== detail && otherDetail.open) {
              otherDetail.removeAttribute('open');
            }
          });
        }
      });
    });
  }
}
