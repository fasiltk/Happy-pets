document.addEventListener("DOMContentLoaded", function () {
    const buyButtons = document.querySelectorAll('.btn.btn-primary');

    buyButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            alert('Order is placed. Please wait for confirmation.');
        });
    });
});
