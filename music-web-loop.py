from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


class MusicWebLooperYouTube:
    def __init__(self):
        print('Opening browser...')
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'en.en_US'})
        chrome_driver_mananager = ChromeDriverManager()
        self.browser = webdriver.Chrome(chrome_driver_mananager.install(), options=options)
        print('Chrome opened')
        self.url = "https://www.youtube.com/watch?v=V5IHShM6FCk&list=PLywxw6QWG0OHF0bp1Q3aQd6gMfhisMaCy"

    def launch(self):
        print(f'Opening url "{self.url}" ...')
        self.browser.get(self.url)
        print(f'Url {self.url} opened')

    def activate_buttons(self):
        # Mute volume
        try:
            mute_button = self.browser.find_element_by_css_selector('button[aria-label="Mute (m)"')
            print('Activate mute')
            mute_button.click()
        except Exception as e:
            print('Mute already on')

        # Play the music
        try:
            play_button = self.browser.find_element_by_css_selector('button[aria-label="Play (k)"]')
            print('Click play')
            play_button.click()
        except Exception as e:
            print('Is already playing')

        time.sleep(1)

        # Turn on the loop
        loop_button = self.browser.find_element_by_css_selector('button[aria-label="Loop playlist"]')
        loop_button_aria_pressed = loop_button.get_attribute('aria-pressed')
        if loop_button_aria_pressed == 'false':
            print('Activate loop')
            loop_button.click()

        # Turn on shuffling
        shuffle_button = self.browser.find_element_by_css_selector('button[aria-label="Shuffle playlist"]')
        shuffle_button_aria_pressed = shuffle_button.get_attribute('aria-pressed')
        if shuffle_button_aria_pressed == 'false':
            print('Activate shuffling')
            shuffle_button.click()

    def confirm_popup(self):
        try:
            confirm_button = self.browser.find_element_by_css_selector('paper-button#button[aria-label="Yes"]')
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
    music_web_looper = MusicWebLooperYouTube()
    music_web_looper.launch()
    music_web_looper.loop()

