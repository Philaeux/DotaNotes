import multiprocessing
from d2notes.d2notes import D2Notes

if __name__ == '__main__':
    multiprocessing.freeze_support()
    D2Notes().run()
