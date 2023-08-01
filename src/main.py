import multiprocessing

from dota_notes.dota_notes import DotaNotes

if __name__ == '__main__':
    multiprocessing.freeze_support()
    DotaNotes().run()
