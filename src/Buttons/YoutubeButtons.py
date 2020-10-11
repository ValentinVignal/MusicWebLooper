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
        self.dark_theme_button = "Appearance: Device theme"
        self.dark_theme_button_2 = 'Dark theme'
        self.refuse_login = 'Not Now'
        self.handle_languages()

    def handle_languages(self):
        if self.language == Languages.fr:
            self.mute_button_text = 'Désactiver le son (m)'
            self.play_button_text = 'Lire (k)'
            self.loop_playlist_button_text = 'Playlist en boucle'
            self.shuffle_playlist_button_text = 'Playlist en mode aléatoire'
            self.confirm_popup_button_text = 'Oui'
            self.setting_button = 'Paramètres'
            # TODO(Valentin):
            self.dark_theme_button = "Apparence\u00A0: thème de l'appareil"
            self.dark_theme_button_2 = 'Thème foncé'
            self.refuse_login = 'Non merci'


