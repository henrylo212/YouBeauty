document.addEventListener('DOMContentLoaded', function() {
    const editButton = document.getElementById('salonedit-button');
    const confirmButton = document.getElementById('salonconfirm');
    const inputs = document.querySelectorAll('#salon-form input');

    // Existing salon fields
    const nameInput = document.getElementById('salon-name');
    const openingtimeInput = document.getElementById('salon_openingtime');
    const closingtimeInput = document.getElementById('salon_closingtime');
    const happyhourtimesInput = document.getElementById('happyhour_times');
    const happyhourdaysInput = document.getElementById('happyhour_days');
    const happyhourdiscountInput = document.getElementById('happyhour_discount');

    // New address fields
    const addressline1Input = document.getElementById('addressline1');
    const addressline2Input = document.getElementById('addressline2');
    const suburbInput = document.getElementById('suburb');
    const stateInput = document.getElementById('state');
    const postcodeInput = document.getElementById('postcode');
    const countryInput = document.getElementById('country');

    // Console logging for debugging
    console.log(editButton);
    console.log(confirmButton);
    console.log(inputs);
    console.log(nameInput);
    console.log(openingtimeInput);
    console.log(closingtimeInput);
    console.log(happyhourtimesInput);
    console.log(happyhourdaysInput);
    console.log(happyhourdiscountInput);
    console.log(addressline1Input);
    console.log(addressline2Input);
    console.log(suburbInput);
    console.log(stateInput);
    console.log(postcodeInput);
    console.log(countryInput);

    // Warnings for existing fields
    const nameWarning = document.createElement('p');
    const openingtimeWarning = document.createElement('p');
    const closingtimeWarning = document.createElement('p');
    const happyhourtimesWarning = document.createElement('p');
    const happyhourdaysWarning = document.createElement('p');
    const happyhourdiscountWarning = document.createElement('p');

    // Warnings for new address fields
    const addressline1Warning = document.createElement('p');
    const addressline2Warning = document.createElement('p');
    const suburbWarning = document.createElement('p');
    const stateWarning = document.createElement('p');
    const postcodeWarning = document.createElement('p');
    const countryWarning = document.createElement('p');

    // Styling warnings
    const warnings = [
        { el: nameWarning, message: 'Salon name cannot be empty!' },
        { el: openingtimeWarning, message: 'Opening time cannot be empty!' },
        { el: closingtimeWarning, message: 'Closing time cannot be empty!' },
        { el: happyhourtimesWarning, message: 'Happy hour times cannot be empty!' },
        { el: happyhourdaysWarning, message: 'Happy hour days cannot be empty!' },
        { el: happyhourdiscountWarning, message: 'Happy hour discount cannot be empty!' },
        { el: addressline1Warning, message: 'Address Line 1 cannot be empty!' },
        { el: addressline2Warning, message: 'Address Line 2 cannot be empty!' },
        { el: suburbWarning, message: 'Suburb cannot be empty!' },
        { el: stateWarning, message: 'State cannot be empty!' },
        { el: postcodeWarning, message: 'Postcode cannot be empty!' },
        { el: countryWarning, message: 'Country cannot be empty!' },
    ];

    warnings.forEach(({ el, message }) => {
        el.style.color = 'red';
        el.style.display = 'none';
        el.textContent = message;
        document.getElementById('salon-form').insertBefore(el, confirmButton);
    });

    confirmButton.style.visibility = 'hidden';

    editButton.addEventListener('click', function() {
        inputs.forEach(input => {
            input.disabled = false;
        });

        // Set minimum width for inputs
        [nameInput, openingtimeInput, closingtimeInput, happyhourtimesInput, happyhourdaysInput, happyhourdiscountInput,
            addressline1Input, addressline2Input, suburbInput, stateInput, postcodeInput, countryInput].forEach(input => {
            input.style.minWidth = "9em";
        });

        editButton.style.display = 'none';
        confirmButton.style.visibility = 'visible';
        confirmButton.style.width = '100%';
        confirmButton.style.height = 'auto';
        confirmButton.style.overflow = 'auto';
    });

    document.getElementById("salon-form").addEventListener("submit", function(event) {
        let isValid = true;

        const nameValue = nameInput.value.trim();
        const openingtimeValue = openingtimeInput.value.trim();
        const closingtimeValue = closingtimeInput.value.trim();
        const happyhourtimesValue = happyhourtimesInput.value.trim();
        const happyhourdaysValue = happyhourdaysInput.value.trim();
        const happyhourdiscountValue = happyhourdiscountInput.value.trim();
        const addressline1Value = addressline1Input.value.trim();
        const addressline2Value = addressline2Input.value.trim();
        const suburbValue = suburbInput.value.trim();
        const stateValue = stateInput.value.trim();
        const postcodeValue = postcodeInput.value.trim();
        const countryValue = countryInput.value.trim();

        // Existing field validations
        if (nameValue === "") {
            nameWarning.style.display = 'block';
            nameInput.style.borderColor = 'red';
            isValid = false;
        } else {
            nameWarning.style.display = 'none';
            nameInput.style.borderColor = '';
        }

        if (openingtimeValue === "") {
            openingtimeWarning.style.display = 'block';
            openingtimeInput.style.borderColor = 'red';
            isValid = false;
        } else {
            openingtimeWarning.style.display = 'none';
            openingtimeInput.style.borderColor = '';
        }

        if (closingtimeValue === "") {
            closingtimeWarning.style.display = 'block';
            closingtimeInput.style.borderColor = 'red';
            isValid = false;
        } else {
            closingtimeWarning.style.display = 'none';
            closingtimeInput.style.borderColor = '';
        }

        if (happyhourtimesValue === "") {
            happyhourtimesWarning.style.display = 'block';
            happyhourtimesInput.style.borderColor = 'red';
            isValid = false;
        } else {
            happyhourtimesWarning.style.display = 'none';
            happyhourtimesInput.style.borderColor = '';
        }

        if (happyhourdaysValue === "") {
            happyhourdaysWarning.style.display = 'block';
            happyhourdaysInput.style.borderColor = 'red';
            isValid = false;
        } else {
            happyhourdaysWarning.style.display = 'none';
            happyhourdaysInput.style.borderColor = '';
        }

        if (happyhourdiscountValue === "") {
            happyhourdiscountWarning.style.display = 'block';
            happyhourdiscountInput.style.borderColor = 'red';
            isValid = false;
        } else {
            happyhourdiscountWarning.style.display = 'none';
            happyhourdiscountInput.style.borderColor = '';
        }

        // New address field validations
        if (addressline1Value === "") {
            addressline1Warning.style.display = 'block';
            addressline1Input.style.borderColor = 'red';
            isValid = false;
        } else {
            addressline1Warning.style.display = 'none';
            addressline1Input.style.borderColor = '';
        }

        if (addressline2Value === "") {
            addressline2Warning.style.display = 'block';
            addressline2Input.style.borderColor = 'red';
            isValid = false;
        } else {
            addressline2Warning.style.display = 'none';
            addressline2Input.style.borderColor = '';
        }

        if (suburbValue === "") {
            suburbWarning.style.display = 'block';
            suburbInput.style.borderColor = 'red';
            isValid = false;
        } else {
            suburbWarning.style.display = 'none';
            suburbInput.style.borderColor = '';
        }

        if (stateValue === "") {
            stateWarning.style.display = 'block';
            stateInput.style.borderColor = 'red';
            isValid = false;
        } else {
            stateWarning.style.display = 'none';
            stateInput.style.borderColor = '';
        }

        if (postcodeValue === "") {
            postcodeWarning.style.display = 'block';
            postcodeInput.style.borderColor = 'red';
            isValid = false;
        } else {
            postcodeWarning.style.display = 'none';
            postcodeInput.style.borderColor = '';
        }

        if (countryValue === "") {
            countryWarning.style.display = 'block';
            countryInput.style.borderColor = 'red';
            isValid = false;
        } else {
            countryWarning.style.display = 'none';
            countryInput.style.borderColor = '';
        }

        if (!isValid) {
            event.preventDefault();
        }
    });
});
