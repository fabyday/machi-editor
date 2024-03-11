from typing import Any



class Context:
    pass 

class MEngineState():
    def __init__(self):
        self.m_engine_attached = False
        
        self.m_mainview = None 
        self.focused_object = []
        self.current_focused
        self.layout_state = {}

    




    def __getattribute__(self, __name: str) -> Any:
        pass