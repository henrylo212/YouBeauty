document.addEventListener('DOMContentLoaded', function() {
    const editButton = document.getElementById('edit-button');
    const confirmButton = document.getElementById('confirm');
    const inputs = document.querySelectorAll('#profile-form input');

    console.log(editButton);
    console.log(confirmButton);
    console.log(inputs);

    // confirmButton.style.display = 'none';

    editButton.addEventListener('click', function() {
        inputs.forEach(input => {
            input.disabled = false;
        });
        editButton.style.display = 'none';
    })

    confirmButton.addEventListener('click', function() {
        inputs.forEach(input => {
            input.disabled = false;
        });
        // confirmButton.style.display = 'inline';
        // confirmButton.style.display = 'inline-block';
        // confirmButton.style.display = 'block';

        // confirmButton.style.display = 'unset';
        // confirmButton.style.display=
        // confirmButton.style.display = "";
        // confirmButton.style.contentVisibility = "visible";
        // confirmButton.style.display = initial;
    });
});


// function editProfile(element, color) {
//     element.style.backgroundcolor = color;
// }