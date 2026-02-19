// Wait until the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Select all tour items
    const tourItems = document.querySelectorAll('ul li');

    // Add click effect
    tourItems.forEach(item => {
        item.addEventListener('click', () => {
            alert(`You clicked on: ${item.textContent}`);
        });
    });
});
