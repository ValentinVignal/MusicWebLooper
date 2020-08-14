import argparse

from src import MusicWebLooper
from src import Languages
from src import Urls


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Loop over the playlist of Arquets and Veval',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('--fr', default=False, action='store_true', help='Use French Language')
    args = parser.parse_args()

    language = Languages.fr if args.fr else Languages.en

    music_web_looper = MusicWebLooper(
        language=language
    )
    music_web_looper.launch(Urls.Youtube)
    music_web_looper.loop_youtube()
