document.getElementById('contactForm').addEventListener('submit', function(event) {
    const form = event.target;
    let valid = true;
    form.querySelectorAll('.error').forEach(el => el.classList.remove('error'));
    form.querySelectorAll('input[required], textarea[required]').forEach(input => {
      if ((input.type === 'checkbox' && !input.checked) || !input.value.trim()) {
        input.classList.add('error');
        valid = false;
      }
    });

    const radios = form.querySelectorAll('input[name="queryType"]');
    if (![...radios].some(r => r.checked)) {
      radios.forEach(r => r.classList.add('error'));
      valid = false;
    }

    if (!valid) {
      event.preventDefault();
    }
  });
