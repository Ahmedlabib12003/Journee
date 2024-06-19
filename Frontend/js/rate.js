// script.js
document.addEventListener('DOMContentLoaded', function() {
    const rateButtons = document.querySelectorAll('.card button');
    const modal = document.getElementById('modal');
    const ratingNumbers = document.querySelectorAll('.numbers-list li');
    const closeButton = document.querySelector('.modal .close');

    rateButtons.forEach(button => {
        button.addEventListener('click', () => {
            modal.style.display = 'block';
        });
    });

    ratingNumbers.forEach(number => {
        number.addEventListener('click', () => {
            modal.style.display = 'none';
        });
    });

    closeButton.addEventListener('click', () => {
        modal.style.display = 'none';
    });

    modal.addEventListener('click', (event) => {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
});

