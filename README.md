# Arabic-English Flashcard Program

An advanced web-based flashcard application for learning Arabic verbs with comprehensive conjugation tables and example sentences.

## Features

- **Interactive Flashcards**: Flip cards to see Arabic/English translations
- **Verb Conjugations**: View past and present tense conjugations for different genders
- **Example Sentences**: 6 example sentences per verb (3 past tense, 3 present tense)
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Keyboard Navigation**: Use arrow keys, spacebar, and Enter for quick navigation
- **Search & Navigation**: Jump to specific cards or navigate sequentially

## Technology Stack

- **Backend**: Python 3.13, Flask
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Data**: JSON-based flashcard system
- **Styling**: CSS Grid, Flexbox, CSS Animations

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ejuPhd/arabic-flashcards.git
   cd arabic-flashcards
   ```bash
   git clone https://github.com/ejuPhd/arabic-flashcards.git
   cd arabic-flashcards

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt

4. **Run the application**:
   ```bash
   python app.py

5. **Open your browser** and navigate to:

   http://localhost:8000


**Project Structure**

arabic-flashcards/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── data/
│   └── arabic_verbs.json # Flashcard data (verbs, conjugations, sentences)
├── templates/
│   └── index.html        # Main HTML template
└── static/
    ├── styles/
    │   └── style.css     # All CSS styles
    └── scripts/
        └── script.js     # All JavaScript functionality


**Data Format**

The flashcard data is stored in data/arabic_verbs.json with the following structure:
json

{
  "verbs": [
    {
      "english": "to write",
      "arabic": "كَتَبَ",
      "form": "Form I",
      "pronunciation": "kataba",
      "conjugations": {
        "past": {
          "he": "كَتَبَ",
          "she": "كَتَبَتْ",
          "you_m": "كَتَبْتَ",
          "you_f": "كَتَبْتِ",
          "we": "كَتَبْنَا",
          "they": "كَتَبُوا"
        },
        "present": {
          "he": "يَكْتُبُ",
          "she": "تَكْتُبُ",
          "you_m": "تَكْتُبُ",
          "you_f": "تَكْتُبِينَ",
          "we": "نَكْتُبُ",
          "they": "يَكْتُبُونَ"
        }
      },
      "example_sentences": {
        "past": [
          {
            "arabic": "كَتَبَ الرَّسُولُ الرِّسَالَةَ أَمْسِ",
            "english": "The messenger wrote the letter yesterday.",
            "pronunciation": "Kataba ar-rasūlu ar-risālata amsi"
          }
        ],
        "present": [
          {
            "arabic": "يَكْتُبُ الْكَاتِبُ رِوَايَةً جَدِيدَةً",
            "english": "The writer is writing a new novel.",
            "pronunciation": "Yaktubu al-kātibu riwāyatan jadīdatan"
          }
        ]
      }
    }
  ]
}

Usage
Navigation
Click the flashcard to flip between Arabic and English

Use arrow keys (← →) to navigate between cards

Press Home/End to jump to first/last card

Press Space or Enter to flip the current card

Use the number input to jump to specific cards

Sidebar Features
Conjugations Tab: Switch between past and present tense verb forms

Example Sentences Tab: View contextual usage in both tenses

All Arabic text includes proper diacritical marks (tashkeel)

Adding New Verbs
Edit data/arabic_verbs.json

Add new verb objects following the existing format

Include conjugations and example sentences for both tenses

The application will automatically load the new data on refresh

Browser Compatibility
Chrome 90+

Firefox 88+

Safari 14+

Edge 90+

Development


**Running in Debug Mode**

python app.py
The application will be available at http://localhost:8000 with hot reloading enabled.

Customizing Styles
Edit static/styles/style.css to modify the appearance

The design uses CSS variables and responsive units for easy customization

Extending Functionality
JavaScript logic is in static/scripts/script.js

Backend routes are defined in app.py
New features can be added by extending the existing JSON data structure

Contributing
Fork the repository
Create a feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request

License:

MIT License
Copyright (c) 2025 Dr. Earnest J. Ujaama.
Permission is hereby granted, free of charge, to any person obtaining a copy...

Acknowledgments:
- Arabic language data compiled from various educational resources
- Designed for students of Modern Standard Arabic
- Thanks to the folks behind DeepSeek and ChatGPT Nano
- Go AI. 
