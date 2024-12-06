// Validate email input
function validateEmail(email) {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
  }
  
  // Validate password input
  function validatePassword(password) {
    const re = /^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[@$!%?&])[A-Za-z\d@$!%?&]{8,}$/;
    return re.test(password);
  }
  
  // Validate password confirmation input
  function validateConfirmPassword(password, confirmPassword) {
    return password === confirmPassword;
  }
  
  // Get input fields
  const emailInput = document.getElementById('email');
  const passwordInput = document.getElementById('password');
  const confirmPasswordInput = document.getElementById('confirm-password');
  
  // Add event listeners to input fields
  emailInput.addEventListener('input', () => {
    if (!validateEmail(emailInput.value)) {
      emailInput.setCustomValidity('Please enter a valid email address.');
    } else {
      emailInput.setCustomValidity('');
    }
  });
  
  passwordInput.addEventListener('input', () => {
    if (!validatePassword(passwordInput.value)) {
      passwordInput.setCustomValidity('Password must be at least 8 characters long and contain at least one lowercase letter, one uppercase letter, one number, and one special character.');
    } else {
      passwordInput.setCustomValidity('');
    }
  });
   
   // Add event listeners to input fields
   confirmPasswordInput.addEventListener('input', () => {
    if (!validateConfirmPassword(passwordInput.value, confirmPasswordInput.value)) {
        confirmPasswordInput.setCustomValidity('Passwords do not match.');
    } else {
        confirmPasswordInput.setCustomValidity('');
    }
});