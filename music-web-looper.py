from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from enum import Enum
import argparse


class Languages(Enum):
    fr = 'fr'
    en = 'en'


class MusicWebLooperYouTube:
    def __init__(self, language=Languages.en):
        self.language = language
        print('Opening browser...')
        options = webdriver.ChromeOptions()
        language_value = 'en.en_US'
        if language == Languages.fr:
            language_value = 'fr-FR'
        options.add_experimental_option('prefs', {'intl.accept_languages': language_value})
        chrome_driver_mananager = ChromeDriverManager()
        self.browser = webdriver.Chrome(chrome_driver_mananager.install(), options=options)
        print('Chrome opened')
        self.url = "https://www.youtube.com/watch?v=V5IHShM6FCk&list=PLywxw6QWG0OHF0bp1Q3aQd6gMfhisMaCy"

        self.mute_button_text = 'Mute (m)'
        self.play_button_text = 'Play (k)'
        self.loop_playlist_button_text = 'Loop playlist'
        self.shuffle_playlist_button_text = 'Shuffle playlist'
        self.confirm_popup_button_text = 'Yes'

        self.handle_languages()

    def handle_languages(self):
        if self.language == Languages.fr:
            self.mute_button_text = 'Désactiver le son (m)'
            self.play_button_text = 'Lire (k)'
            self.loop_playlist_button_text = 'Playlist en boucle'
            self.shuffle_playlist_button_text = 'Playlist en mode aléatoire'
            self.confirm_popup_button_text = 'Oui'

    def launch(self):
        print(f'Opening url "{self.url}" ...')
        self.browser.get(self.url)
        print(f'Url {self.url} opened')

    def activate_buttons(self):
        # Mute volume
        try:
            mute_button = self.browser.find_element_by_css_selector(
                css_selector=f'button[aria-label="{self.mute_button_text}"'
            )
            print('Activate mute')
            mute_button.click()
        except Exception as e:
            print('Mute already on')

        # Play the music
        try:
            play_button = self.browser.find_element_by_css_selector(
                css_selector=f'button[aria-label="{self.play_button_text}"]'
            )
            print('Click play')
            play_button.click()
        except Exception as e:
            print('Is already playing')

        time.sleep(1)

        # Turn on the loop
        loop_button = self.browser.find_element_by_css_selector(
            css_selector=f'button[aria-label="{self.loop_playlist_button_text}"]'
        )
        loop_button_aria_pressed = loop_button.get_attribute('aria-pressed')
        if loop_button_aria_pressed == 'false':
            print('Activate loop')
            loop_button.click()

        # Turn on shuffling
        shuffle_button = self.browser.find_element_by_css_selector(
            css_selector=f'button[aria-label="{self.shuffle_playlist_button_text}"]'
        )
        shuffle_button_aria_pressed = shuffle_button.get_attribute('aria-pressed')
        if shuffle_button_aria_pressed == 'false':
            print('Activate shuffling')
            shuffle_button.click()

    def confirm_popup(self):
        try:
            confirm_button = self.browser.find_element_by_css_selector(
                css_selector=f'paper-button#button[aria-label="{self.confirm_popup_button_text}"]'
            )
            print('Confirm continue playlist')
            confirm_button.click()
            return True
        except Exception:
            return False

    def loop(self, activate_first=True):
        if activate_first:
            self.activate_buttons()
        while True:
            had_to_confirm = self.confirm_popup()
            if had_to_confirm:
                self.activate_buttons()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Loop over the playlist of Arquets and Veval',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('--fr', default=False, action='store_true', help='Use French Language')
    args = parser.parse_args()

    language = Languages.fr if args.fr else Languages.en

    music_web_looper = MusicWebLooperYouTube(
        language=language
    )
    music_web_looper.launch()
    music_web_looper.loop()
