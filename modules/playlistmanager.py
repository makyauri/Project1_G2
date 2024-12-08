import sys
sys.path.append('modules\\')

from modules.arraylist import ArrayList

class PlaylistManager(ArrayList):
    def __init__(self) -> None:
        super().__init__()
    def __str__(self) -> str:
        s='''
==================================
            Playlists
==================================
        '''
        for playlist in self.get_list():
            self.incrCount()
            s += f'[{self.getcount}] {str(playlist)}'
        return s
    