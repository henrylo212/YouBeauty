document.addEventListener('DOMContentLoaded', function() {
    const editButton = document.getElementById('edit-button');
    const inputs = document.querySelectorAll('#profile-form input');

    console.log(editButton);
    console.log(inputs);

    editButton.addEventListener('click', function() {
        inputs.forEach(input => {
            input.disabled = false;
        });
        editButton.style.display = 'none';
    });
});


// function editProfile(element, color) {
//     element.style.backgroundcolor = color;
// }