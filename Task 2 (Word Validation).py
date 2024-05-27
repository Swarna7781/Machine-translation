class ValidWords:
    def __init__(self):
        self.valid_words = {
            "hello": ["hi", "hey", "greetings"],
            "goodbye": ["bye", "farewell", "see you later"],
            "thank": ["thanks", "thank you", "gratitude"],
        }
        self.wrong_words = []
        self.consecutive_wrong_count = 0

    def validate_word(self, word):
        if word.lower() not in self.valid_words:
            self.wrong_words.append(word)
            self.consecutive_wrong_count += 1
            if self.consecutive_wrong_count >= 2:
                suggestions = self.get_combined_suggestions(self.wrong_words)
                error_msg = (
                    f"Word is not available. Wrong words entered so far: "
                    f"{', '.join(self.wrong_words)}. Suggestions: {', '.join(suggestions)}"
                )
                self.consecutive_wrong_count = 0  
                self.wrong_words = []  
                raise ValueError(error_msg)
            else:
                suggestions = self.get_suggestions(word)
                error_msg = f"Word is not available. Suggestions: {', '.join(suggestions)}"
                raise ValueError(error_msg)
        else:
            self.consecutive_wrong_count = 0  
            self.wrong_words = []  
            return f"Valid word: {word}"

    def get_suggestions(self, word):
        suggestions = []
        for valid_word in self.valid_words:
            if valid_word.startswith(word[0]):
                suggestions.extend(self.valid_words[valid_word])
        return suggestions

    def get_combined_suggestions(self, wrong_words):
        combined_suggestions = []
        for wrong_word in wrong_words:
            combined_suggestions.extend(self.get_suggestions(wrong_word))
        return list(set(combined_suggestions))  

def main():
    validator = ValidWords()
    
    while True:
        user_input = input("Enter a word: ")
        
        try:
            print(validator.validate_word(user_input))
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()


