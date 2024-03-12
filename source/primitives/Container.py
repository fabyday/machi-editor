# this is 

import ctypes 

class MContainer:
    pass

import uuid
class MContainer:

    def __init__(self, parent = None):
        self.m_label = "" 
        self.m_uuid = uuid.uuid1()
        self.m_id = ""
        self.width = 0
        self.height = 0
        self.m_parent = parent 
        self.m_child = []

    @property
    def M_id(self):
        return self.m_id


    def attach(self, *containers : MContainer):
        pass


    def detach(self, *containers_or_ids):
        pass


    def __delattr__(self, __name: str) -> None:
        pass


    def render(self):
        # render this and child.
        pass 






if __name__ == "__main__":

    # testing 
    MContainer()