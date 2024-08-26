
$(document).ready(function() {
    var passwordField = $('#id_password');
    var toggleDiv = $('#passwordToggle');

    // Function to toggle visibility of the checkbox
    function toggleCheckboxVisibility() {
        if (passwordField.val()) {
            toggleDiv.show();
        } else {
            toggleDiv.hide();
        }
    }

    // Initial check
    toggleCheckboxVisibility();

    // Check on input change
    passwordField.on('input', function() {
        toggleCheckboxVisibility();
    });


    
    // Toggle password visibility and label text on checkbox click
    $('#flexCheckIndeterminate').on('click', function() {
        var type = passwordField.attr('type') === 'password' ? 'text' : 'password';
        passwordField.attr('type', type);

        var labelText = (type === 'password') ? 'Show' : 'Hide';
        $('.form-check-label').text(labelText);
    });


});

$(document).ready(function(){

    $('.submitForm').submit(function (e) { 
        
        var password = $('#id_password').val();


    
            // if (password.length < 6) {
            //         $('.passwordValidation').text('Password must contain 6 characters')
                    
            //         e.preventDefault();
            // }

        
        
    });
})



