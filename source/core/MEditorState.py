class MEditorState():
    def __init__(self):
        self.m_editor_width = 1280
        self.m_editor_height = 980

        self.m_root_container = None 
    


    @property
    def editor_width(self):
        return self.m_editor_width