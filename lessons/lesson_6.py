# if __name__ == "__main__"

#не вызывает побочные принты 

#для чего __main__.py 
#какие есть паттерны организации файлов\кода 

#магические методы,  magic methods, dunder (double underscore) methods
#rm .git/index.lock
class PlayList:
    def __init__(self, name, songs):
        self.__songs = songs
        self.name = name 
    
    def __str__(self):
        return f"<PlayList: {self.name}, songs: {len(self.songs)}"
    
    def __len__(self):
        return len(self.__songs) > 1 
    
    def __contains__(self, item):
        return item in self.__songs
    
    def __bool__(self):
        return bool(self.__songs)

if __name__ == "__main__":
    playlist_pop = PlayList(
    'pop', 
    ['Shape of my heart']
    )
    print(len(playlist_pop))
    print('Shape of my heart' in playlist_pop)
    if playlist_pop:
        print('in playlist there are more than 1 song')
    else:
        print('in playlist there is less than 2 song')