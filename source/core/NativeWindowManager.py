import primitives 

import NativeWindow

class MNativeWindowManager:
    def __init__(self):
        self.native_root_window = {}


    
    


    def create_window(self, root_container : primitives.MContainer):

        if(self.native_root_window.get(root_container.m_uuid, None)):
            self.native_root_window[root_container.m_uuid] = self._create_native_window()

    def _create_native_window(self):
        return NativeWindow.MNativeWindow()
    

    def delete_window(self, id):
        if(self.native_root_window.get(id, None)):
            self.native_root_window.pop(id)

    def start(self):
        while True : 
            for key, item in self.native_root_window:
                item.render()


    