import MInitializer
from imgui.integrations.sdl2 import SDL2Renderer
from sdl2 import *
import OpenGL.GL as gl



class MNativeWindow():
    def __init__(self):
            self.window, self.gl_context = MInitializer.impl_pysdl2_init()
            self.impl = SDL2Renderer(self.window)


    def deinitialize(self):
        self.impl.shutdown()
        SDL_GL_DeleteContext(self.gl_context)
        SDL_DestroyWindow(self.window)
        SDL_Quit()


    def render():
        event = SDL_Event()


        gl.glClearColor(1.0, 1.0, 1.0, 1)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)