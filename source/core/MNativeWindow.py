import MInitializer




class NativeWindow():
    def __init__(self):
            self.window, self.gl_context = MInitializer.impl_pysdl2_init()

