document.addEventListener('DOMContentLoaded', function() {
    function validateInput() {
        const input = document.getElementById('keyCardID').value;
        const button = document.getElementById('submitButton');
        const regex = /^\d{10}$/;
        if (regex.test(input)) {
            button.disabled = false;
            button.classList.remove('btn-secondary');
            button.classList.add('btn-primary');
        } else {
            button.disabled = true;
            button.classList.remove('btn-primary');
            button.classList.add('btn-secondary');
        }
    }
    window.validateInput = validateInput;
});
