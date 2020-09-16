from src.Languages import Languages


class YoutubeButtons:
    def __init__(self, language=Languages.en):
        self.language = language
        self.mute_button_text = 'Mute (m)'
        self.play_button_text = 'Play (k)'
        self.loop_playlist_button_text = 'Loop playlist'
        self.shuffle_playlist_button_text = 'Shuffle playlist'
        self.confirm_popup_button_text = 'Yes'
        self.setting_button = 'Settings'
        self.dark_theme_button = "Dark theme: Off"
        self.refuse_login = 'No Thanks'
        self.handle_languages()

    def handle_languages(self):
        if self.language == Languages.fr:
            self.mute_button_text = 'Désactiver le son (m)'
            self.play_button_text = 'Lire (k)'
            self.loop_playlist_button_text = 'Playlist en boucle'
            self.shuffle_playlist_button_text = 'Playlist en mode aléatoire'
            self.confirm_popup_button_text = 'Oui'
            self.setting_button = 'Paramètres'
            self.dark_theme_button = 'Thème sombre\u00A0: désactivé'
            self.refuse_login = 'Non merci'


