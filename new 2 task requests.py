import yadisk

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        y = yadisk.YaDisk(token=token)
        y.upload("text.txt", "/text.txt")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = input('путь к файлу: ')
    token = input('введите токкен: ')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)