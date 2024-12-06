document.addEventListener('DOMContentLoaded', function () {
    var loginForm = document.querySelector('.form-group');

    loginForm.addEventListener('submit', function (event) {
        var emailInput = document.getElementById('email');
        var passwordInput = document.getElementById('password');

        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (!emailRegex.test(emailInput.value)) {
            alert('Please enter a valid email address.');
            event.preventDefault(); 
            return;
        }

    });
});