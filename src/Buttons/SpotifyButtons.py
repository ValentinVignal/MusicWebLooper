from src.Languages import Languages


class SpotifyButtons:
    def __init__(self, language=Languages.en):
        self.language = language
        self.play_button_text = "Play"
        self.handle_languages()

    def handle_languages(self):
        if self.language == Languages.fr:
            self.play_button_text = 'Lecture'


