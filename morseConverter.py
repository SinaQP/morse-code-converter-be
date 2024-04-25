class MorseConverter:
    """Converts between letters and their Morse code representations."""
    ENGLISH_TO_MORSE = {
        'A': '.-', 'B': '-...',
        'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-',
        'R': '.-.', 'S': "...", 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--',
        'X': '-..-', 'Y': '.-.--', 'Z': '--..',
        ' ': '/'
    }
    MORSE_TO_ENGLISH = {value: key for key, value in ENGLISH_TO_MORSE.items()}

    def encode(self, message):
        """Encodes an English message into Morse code."""
        morse_code = ''.join(self.ENGLISH_TO_MORSE.get(character.upper(), character) + ' ' for character in message)
        return morse_code.rstrip()

    def decode(self, morse_code):
        """Decodes Morse code into an English message."""
        try:
            words = morse_code.split('/')
            decoded_words = []

            for word in words:
                letters = word.upper().split()
                decoded_word = ''.join(self.MORSE_TO_ENGLISH.get(letter) for letter in letters if letter)
                decoded_words.append(decoded_word)

            return ' '.join(decoded_words)
        except Exception as error:
            raise ValueError("Enter Valid Morse Code")
