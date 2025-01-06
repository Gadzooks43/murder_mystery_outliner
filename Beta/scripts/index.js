// Global object to store story details
const storyDetails = {
    mysteryArchetype: '',
    suspects: '',
    redHerring: '',
    bStory: '',
    murderDetails: '',
    twist: ''
};

// Function to update the progress bar
function updateProgressBar() {
    const totalFields = Object.keys(storyDetails).length;
    const filledFields = Object.values(storyDetails).filter(value => value !== '').length;
    const progressPercentage = (filledFields / totalFields) * 100;
    
    const progressBar = document.getElementById('progressBar');
    progressBar.style.width = `${progressPercentage}%`;
    progressBar.setAttribute('aria-valuenow', progressPercentage);
}

// Initialize progress bar on page load
document.addEventListener('DOMContentLoaded', updateProgressBar);
