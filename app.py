from flask import Flask, render_template, jsonify, request
import json
import os

app = Flask(__name__)


class FlashcardManager:
    def __init__(self, json_file='data/arabic_verbs.json'):
        self.json_file = json_file
        self.flashcards = []
        self.current_index = 0
        self.load_flashcards()

    def load_flashcards(self):
        """Load flashcards from JSON file"""
        try:
            if os.path.exists(self.json_file):
                with open(self.json_file, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    self.flashcards = data.get('verbs', [])
                print(
                    f"Loaded {len(self.flashcards)} flashcards from {self.json_file}")
            else:
                print(
                    f"JSON file {self.json_file} not found. Using sample data.")
                self.flashcards = self.get_sample_data()
        except Exception as e:
            print(f"Error loading flashcards: {e}")
            self.flashcards = self.get_sample_data()

    def get_sample_data(self):
        """Return sample data if JSON file is not available"""
        return [
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
                }
            },
            {
                "english": "to read",
                "arabic": "قَرَأَ",
                "form": "Form I",
                "pronunciation": "qara'a",
                "conjugations": {
                    "past": {
                        "he": "قَرَأَ",
                        "she": "قَرَأَتْ",
                        "you_m": "قَرَأْتَ",
                        "you_f": "قَرَأْتِ",
                        "we": "قَرَأْنَا",
                        "they": "قَرَأُوا"
                    },
                    "present": {
                        "he": "يَقْرَأُ",
                        "she": "تَقْرَأُ",
                        "you_m": "تَقْرَأُ",
                        "you_f": "تَقْرَئِينَ",
                        "we": "نَقْرَأُ",
                        "they": "يَقْرَؤُونَ"
                    }
                }
            },
            {
                "english": "to study",
                "arabic": "دَرَسَ",
                "form": "Form I",
                "pronunciation": "darasa",
                "conjugations": {
                    "past": {
                        "he": "دَرَسَ",
                        "she": "دَرَسَتْ",
                        "you_m": "دَرَسْتَ",
                        "you_f": "دَرَسْتِ",
                        "we": "دَرَسْنَا",
                        "they": "دَرَسُوا"
                    },
                    "present": {
                        "he": "يَدْرُسُ",
                        "she": "تَدْرُسُ",
                        "you_m": "تَدْرُسُ",
                        "you_f": "تَدْرُسِينَ",
                        "we": "نَدْرُسُ",
                        "they": "يَدْرُسُونَ"
                    }
                }
            }
        ]

    def get_current_card(self):
        """Get the current flashcard"""
        if self.flashcards:
            return self.flashcards[self.current_index]
        return None

    def next_card(self):
        """Move to the next card"""
        if self.flashcards:
            self.current_index = (self.current_index +
                                  1) % len(self.flashcards)
        return self.get_current_card()

    def previous_card(self):
        """Move to the previous card"""
        if self.flashcards:
            self.current_index = (self.current_index -
                                  1) % len(self.flashcards)
        return self.get_current_card()

    def first_card(self):
        """Move to the first card"""
        if self.flashcards:
            self.current_index = 0
        return self.get_current_card()

    def last_card(self):
        """Move to the last card"""
        if self.flashcards:
            self.current_index = len(self.flashcards) - 1
        return self.get_current_card()

    def go_to_card(self, card_number):
        """Move to a specific card number (1-indexed)"""
        if self.flashcards and 1 <= card_number <= len(self.flashcards):
            self.current_index = card_number - 1
            return self.get_current_card()
        return None

    def get_total_cards(self):
        """Get total number of cards"""
        return len(self.flashcards)

    def get_current_position(self):
        """Get current card position"""
        return self.current_index + 1


# Initialize flashcard manager
flashcard_manager = FlashcardManager()


@app.route('/')
def index():
    """Main page showing the flashcard"""
    current_card = flashcard_manager.get_current_card()
    return render_template('index.html',
                           card=current_card,
                           position=flashcard_manager.get_current_position(),
                           total=flashcard_manager.get_total_cards())


@app.route('/next')
def next_card():
    """Get next flashcard"""
    card = flashcard_manager.next_card()

    if card is None:
        return jsonify({
            'english': 'No cards available',
            'arabic': 'لا توجد بطاقات',
            'form': '',
            'pronunciation': '',
            'conjugations': {},
            'position': 0,
            'total': 0
        })

    return jsonify({
        'english': card.get('english', ''),
        'arabic': card.get('arabic', ''),
        'form': card.get('form', ''),
        'pronunciation': card.get('pronunciation', ''),
        'conjugations': card.get('conjugations', {}),
        'position': flashcard_manager.get_current_position(),
        'total': flashcard_manager.get_total_cards()
    })


@app.route('/previous')
def previous_card():
    """Get previous flashcard"""
    card = flashcard_manager.previous_card()

    if card is None:
        return jsonify({
            'english': 'No cards available',
            'arabic': 'لا توجد بطاقات',
            'form': '',
            'pronunciation': '',
            'conjugations': {},
            'position': 0,
            'total': 0
        })

    return jsonify({
        'english': card.get('english', ''),
        'arabic': card.get('arabic', ''),
        'form': card.get('form', ''),
        'pronunciation': card.get('pronunciation', ''),
        'conjugations': card.get('conjugations', {}),
        'position': flashcard_manager.get_current_position(),
        'total': flashcard_manager.get_total_cards()
    })


@app.route('/first')
def first_card():
    """Get first flashcard"""
    card = flashcard_manager.first_card()

    if card is None:
        return jsonify({
            'english': 'No cards available',
            'arabic': 'لا توجد بطاقات',
            'form': '',
            'pronunciation': '',
            'conjugations': {},
            'position': 0,
            'total': 0
        })

    return jsonify({
        'english': card.get('english', ''),
        'arabic': card.get('arabic', ''),
        'form': card.get('form', ''),
        'pronunciation': card.get('pronunciation', ''),
        'conjugations': card.get('conjugations', {}),
        'position': flashcard_manager.get_current_position(),
        'total': flashcard_manager.get_total_cards()
    })


@app.route('/last')
def last_card():
    """Get last flashcard"""
    card = flashcard_manager.last_card()

    if card is None:
        return jsonify({
            'english': 'No cards available',
            'arabic': 'لا توجد بطاقات',
            'form': '',
            'pronunciation': '',
            'conjugations': {},
            'position': 0,
            'total': 0
        })

    return jsonify({
        'english': card.get('english', ''),
        'arabic': card.get('arabic', ''),
        'form': card.get('form', ''),
        'pronunciation': card.get('pronunciation', ''),
        'conjugations': card.get('conjugations', {}),
        'position': flashcard_manager.get_current_position(),
        'total': flashcard_manager.get_total_cards()
    })


@app.route('/goto', methods=['POST'])
def go_to_card():
    """Go to a specific card number"""
    data = request.get_json()
    card_number = data.get('card_number', 1)

    card = flashcard_manager.go_to_card(card_number)

    if card is None:
        return jsonify({
            'english': 'Invalid card number',
            'arabic': 'رقم البطاقة غير صالح',
            'form': '',
            'pronunciation': '',
            'conjugations': {},
            'position': 0,
            'total': flashcard_manager.get_total_cards(),
            'error': True
        })

    return jsonify({
        'english': card.get('english', ''),
        'arabic': card.get('arabic', ''),
        'form': card.get('form', ''),
        'pronunciation': card.get('pronunciation', ''),
        'conjugations': card.get('conjugations', {}),
        'position': flashcard_manager.get_current_position(),
        'total': flashcard_manager.get_total_cards(),
        'error': False
    })


@app.route('/cards')
def get_all_cards():
    """Get all flashcards (for debugging)"""
    return jsonify(flashcard_manager.flashcards)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
