import os


class Loader:

    def __init__(self):
        pass

    def search(self, dirname):
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            yield full_filename

if __name__ == '__main__':
    print("A")



