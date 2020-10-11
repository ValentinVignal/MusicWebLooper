from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

from .Languages import Languages
from .Buttons import YoutubeButtons, SpotifyButtons


class MusicWebLooper:
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

        self.youtube_buttons = YoutubeButtons(language=language)
        self.spotify_buttons = SpotifyButtons(language=language)

    def launch(self, url):
        print(f'Opening url "{url}" ...')
        self.browser.get(url)
        print(f'Url {url} opened')

    def play_spotify(self):
        try:
            play_button = self.browser.find_element_by_css_selector(
                css_selector=f'button[aria-label="{self.spotify_buttons.play_button_text}"]'
                f'[title="{self.spotify_buttons.play_button_text}"][data-testid="play-button"]'
            )
            print('click play')
            self.browser.execute_script("arguments[0].click();", play_button)
        except Exception as e:
            print('Could not click on play', e)

    def activate_buttons_youtube(self):
        # Mute volume
        try:
            mute_button = self.browser.find_element_by_css_selector(
                css_selector=f'button[aria-label="{self.youtube_buttons.mute_button_text}"'
            )
            print('Activate mute')
            mute_button.click()
        except Exception as e:
            print('Mute already on')

        # Play the music
        try:
            play_button = self.browser.find_element_by_css_selector(
                css_selector=f'button[aria-label="{self.youtube_buttons.play_button_text}"]'
            )
            print('Click play')
            play_button.click()
        except Exception as e:
            print('Is already playing')

        time.sleep(1)

        # Turn on the loop
        loop_button = self.browser.find_element_by_css_selector(
            css_selector=f'button[aria-label="{self.youtube_buttons.loop_playlist_button_text}"]'
        )
        loop_button_aria_pressed = loop_button.get_attribute('aria-pressed')
        if loop_button_aria_pressed == 'false':
            print('Activate loop')
            loop_button.click()

        # Turn on shuffling
        shuffle_button = self.browser.find_element_by_css_selector(
            css_selector=f'button[aria-label="{self.youtube_buttons.shuffle_playlist_button_text}"]'
        )
        shuffle_button_aria_pressed = shuffle_button.get_attribute('aria-pressed')
        if shuffle_button_aria_pressed == 'false':
            print('Activate shuffling')
            shuffle_button.click()

    def confirm_popup_youtube(self):
        try:
            confirm_button = self.browser.find_element_by_css_selector(
                css_selector=f'paper-dialog:not([style*="display: none"]) yt-confirm-dialog-renderer:not([aria-hidden="true"]) paper-button#button[aria-label="{self.youtube_buttons.confirm_popup_button_text}"]'
            )
            print('Confirm continue playlist')
            confirm_button.click()
            return True
        except Exception:
            return False

    def refuse_login(self):
        try:
            refuse_login_button = self.browser.find_element_by_css_selector(
                css_selector=f'paper-dialog:not([style*="display: none"])  paper-button#button[aria-label="{self.youtube_buttons.refuse_login}"]'
            )
            print('Refuse login')
            refuse_login_button.click()
            return True
        except Exception:
            return False

    def loop_youtube(self, activate_first=True):
        if activate_first:
            self.activate_buttons_youtube()
            self.apply_dark_theme_youtube()
        while True:
            had_to_confirm = self.confirm_popup_youtube()
            had_to_refuse_login = self.refuse_login()
            if had_to_confirm or had_to_refuse_login:
                self.activate_buttons_youtube()

            time.sleep(10)

    def new_tab(self, url):
        self.browser.execute_script(f"window.open('{url}');")

    def apply_dark_theme_youtube(self):
        setting_button = self.browser.find_element_by_css_selector(
            css_selector=f'button[aria-label="{self.youtube_buttons.setting_button}"]'
        )
        setting_button.click()
        time.sleep(1)
        try:
            dark_theme_button = self.browser.find_element_by_xpath(
                f'//div[contains(text(), "{self.youtube_buttons.dark_theme_button}")]'
            )
            dark_theme_button.click()
        except Exception as e:
            print('Already using the Dark Theme mode')

        try:
            toggle_button = self.browser.find_element_by_css_selector(
                css_selector='paper-toggle-button[aria-pressed="false"]'
            )
            print('Activate dark mode')
            toggle_button.click()
        except Exception as e:
            print('Could not press toggle button', e)

        setting_button.click()
