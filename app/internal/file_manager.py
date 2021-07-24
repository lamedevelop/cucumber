import os.path


class FileManager:

    media_files_dir = 'media/'

    @staticmethod
    def is_file(filepath) -> bool:
        return os.path.isfile(filepath)
