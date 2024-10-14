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

    const nameWarning = document.createElement('p');
    const emailWarning = document.createElement('p');
    const phoneWarning = document.createElement('p');
    
    nameWarning.style.color = 'red';
    emailWarning.style.color = 'red';
    phoneWarning.style.color = 'red';
    
    nameWarning.style.display = 'none';
    emailWarning.style.display = 'none';
    phoneWarning.style.display = 'none';
    
    nameWarning.textContent = 'Profile name cannot be empty!';
    emailWarning.textContent = 'Email cannot be empty!';
    phoneWarning.textContent = 'Phone number cannot be empty!';
    
    document.getElementById('profile-form').insertBefore(nameWarning, confirmButton);
    document.getElementById('profile-form').insertBefore(emailWarning, confirmButton);
    document.getElementById('profile-form').insertBefore(phoneWarning, confirmButton);

    confirmButton.style.visibility = 'hidden';

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
    });

    document.getElementById("profile-form").addEventListener("submit", function(event) {
        let isValid = true;

        const nameValue = nameInput.value.trim();
        const emailValue = emailInput.value.trim();
        const phoneValue = phoneInput.value.trim();

        if (nameValue === "") {
            nameWarning.style.display = 'block';
            nameInput.style.borderColor = 'red';
            isValid = false;
        } else {
            nameWarning.style.display = 'none';
            nameInput.style.borderColor = '';
        }

        if (emailValue === "") {
            emailWarning.style.display = 'block';
            emailInput.style.borderColor = 'red';
            isValid = false;
        } else {
            emailWarning.style.display = 'none';
            emailInput.style.borderColor = '';
        }

        if (phoneValue === "") {
            phoneWarning.style.display = 'block';
            phoneInput.style.borderColor = 'red';
            isValid = false;
        } else {
            phoneWarning.style.display = 'none';
            phoneInput.style.borderColor = '';
        }

        if (!isValid) {
            event.preventDefault();
        }
    });
});
