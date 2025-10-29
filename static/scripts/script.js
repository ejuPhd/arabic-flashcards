// Global variables
let currentTense = 'past';
let currentSentenceTense = 'past';
let currentCardData = null;

// DOM elements
const flashcard = document.getElementById('flashcard');
const englishWord = document.getElementById('english-word');
const arabicWord = document.getElementById('arabic-word');
const verbForm = document.getElementById('verb-form');
const pronunciation = document.getElementById('pronunciation');
const counter = document.getElementById('counter');
const gotoInput = document.getElementById('goto-input');
const errorMessage = document.getElementById('error-message');
const conjugationList = document.getElementById('conjugation-list');
const sentencesList = document.getElementById('sentences-list');

// Conjugation labels mapping
const conjugationLabels = {
    'he': 'He',
    'she': 'She',
    'you_m': 'You (M)',
    'you_f': 'You (F)',
    'we': 'We',
    'they': 'They'
};

// Flashcard functions
function flipCard() {
    flashcard.classList.toggle('flipped');
}

// Navigation functions
function nextCard() {
    fetch('/next')
        .then(response => response.json())
        .then(data => {
            updateCard(data);
            flashcard.classList.remove('flipped');
            hideError();
        })
        .catch(error => console.error('Error:', error));
}

function previousCard() {
    fetch('/previous')
        .then(response => response.json())
        .then(data => {
            updateCard(data);
            flashcard.classList.remove('flipped');
            hideError();
        })
        .catch(error => console.error('Error:', error));
}

function firstCard() {
    fetch('/first')
        .then(response => response.json())
        .then(data => {
            updateCard(data);
            flashcard.classList.remove('flipped');
            hideError();
        })
        .catch(error => console.error('Error:', error));
}

function lastCard() {
    fetch('/last')
        .then(response => response.json())
        .then(data => {
            updateCard(data);
            flashcard.classList.remove('flipped');
            hideError();
        })
        .catch(error => console.error('Error:', error));
}

function goToCard() {
    const cardNumber = parseInt(gotoInput.value);
    if (isNaN(cardNumber) || cardNumber < 1) {
        showError('Please enter a valid card number');
        return;
    }

    fetch('/goto', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ card_number: cardNumber })
    })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                showError('Invalid card number. Please enter a number between 1 and ' + data.total);
            } else {
                updateCard(data);
                flashcard.classList.remove('flipped');
                hideError();
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showError('Error navigating to card');
        });
}

// Sidebar functions
function switchTense(tense) {
    currentTense = tense;

    // Update active tab
    document.querySelectorAll('.sidebar-section:first-child .tense-tab').forEach(tab => {
        if (tab.textContent.toLowerCase().includes(tense)) {
            tab.classList.add('active');
        } else {
            tab.classList.remove('active');
        }
    });

    updateConjugationsDisplay();
}

function switchSentenceTense(tense) {
    currentSentenceTense = tense;

    // Update active tab
    document.querySelectorAll('.sidebar-section:last-child .tense-tab').forEach(tab => {
        if (tab.textContent.toLowerCase().includes(tense)) {
            tab.classList.add('active');
        } else {
            tab.classList.remove('active');
        }
    });

    updateSentencesDisplay();
}

function updateConjugationsDisplay() {
    if (!currentCardData || !currentCardData.conjugations || !currentCardData.conjugations[currentTense]) {
        conjugationList.innerHTML = '<div class="no-data">No conjugation data available</div>';
        return;
    }

    const conjugations = currentCardData.conjugations[currentTense];
    let html = '';

    for (const [key, arabicText] of Object.entries(conjugations)) {
        html += `
            <div class="conjugation-item">
                <span class="conjugation-person">${conjugationLabels[key]}</span>
                <span class="conjugation-arabic">${arabicText}</span>
            </div>
        `;
    }

    conjugationList.innerHTML = html;
}

function updateSentencesDisplay() {
    if (!currentCardData || !currentCardData.example_sentences || !currentCardData.example_sentences[currentSentenceTense]) {
        sentencesList.innerHTML = '<div class="no-data">No example sentences available</div>';
        return;
    }

    const sentences = currentCardData.example_sentences[currentSentenceTense];
    let html = '';

    sentences.forEach(sentence => {
        html += `
            <div class="sentence-item">
                <div class="sentence-arabic">${sentence.arabic}</div>
                <div class="sentence-english">${sentence.english}</div>
                <div class="sentence-pronunciation">${sentence.pronunciation}</div>
            </div>
        `;
    });

    sentencesList.innerHTML = html;
}

// Card update functions
function updateCard(data) {
    englishWord.textContent = data.english;
    arabicWord.textContent = data.arabic;

    if (data.form) {
        verbForm.textContent = data.form;
        verbForm.style.display = 'block';
    } else {
        verbForm.style.display = 'none';
    }

    if (data.pronunciation) {
        pronunciation.textContent = data.pronunciation;
        pronunciation.style.display = 'block';
    } else {
        pronunciation.style.display = 'none';
    }

    counter.textContent = `Card ${data.position} of ${data.total}`;
    gotoInput.max = data.total;

    // Store current card data
    currentCardData = data;

    // Update displays
    updateConjugationsDisplay();
    updateSentencesDisplay();
}

// Utility functions
function showError(message) {
    errorMessage.textContent = message;
    errorMessage.style.display = 'block';
}

function hideError() {
    errorMessage.style.display = 'none';
}

// Event listeners and initialization
function initializeEventListeners() {
    // Add Enter key support for goto input
    gotoInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            goToCard();
        }
    });

    // Add click event to the flashcard
    flashcard.addEventListener('click', flipCard);

    // Add keyboard navigation
    document.addEventListener('keydown', (event) => {
        switch (event.key) {
            case 'ArrowLeft':
                previousCard();
                break;
            case 'ArrowRight':
                nextCard();
                break;
            case 'Home':
                event.preventDefault();
                firstCard();
                break;
            case 'End':
                event.preventDefault();
                lastCard();
                break;
            case ' ':
            case 'Enter':
                if (document.activeElement !== gotoInput) {
                    event.preventDefault();
                    flipCard();
                }
                break;
        }
    });
}

// Initialize the application
function initializeApp() {
    initializeEventListeners();
    updateConjugationsDisplay();
    updateSentencesDisplay();
}

// Start the application when DOM is loaded
document.addEventListener('DOMContentLoaded', initializeApp);