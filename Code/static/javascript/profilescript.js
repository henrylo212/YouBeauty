document.addEventListener('DOMContentLoaded', function() {
    const editButton = document.getElementById('edit-button');
    const confirmButton = document.getElementById('confirm');
    const inputs = document.querySelectorAll('#profile-form input');
    const nameInput = document.getElementById('profile-name');
    const emailInput = document.getElementById('email');
    const phoneInput = document.getElementById('phone-number');

    console.log(editButton);
    console.log(confirmButton);
    console.log(inputs);
    console.log(nameInput);
    console.log(emailInput);
    console.log(phoneInput);

    // confirmButton.style.display = 'none';

    editButton.addEventListener('click', function() {
        inputs.forEach(input => {
            input.disabled = false;
        });

        nameInput.style.minWidth = "9em";
        emailInput.style.minWidth = "9em";
        phoneInput.style.minWidth = "9em";


        editButton.style.display = 'none';
        confirmButton.style.visibility = 'visible';
        confirmButton.style.width = '100%';
        confirmButton.style.height = 'auto';
        confirmButton.style.overflow = 'auto';
    })

    confirmButton.addEventListener('click', function() {
        inputs.forEach(input => {
            input.disabled = false;
   