import os

from pygame import display,image
#from .layer import bulletlayer
scr = display.get_surface()
scrrect = scr.get_rect()

maindir = os.path.dirname(os.path.dirname(__file__))

class Background(object):
    """The background layer. Can make this use not static method, but why bother"""

    #from .starsfield import Starsfield
    #st           = Starsfield()
    #update       = st.update
    earth        = image.load(os.path.join(maindir, 'img/earth.png'))
    earthrect    = earth.get_rect(midbottom=scrrect.midbottom)

    @staticmethod
    def render():
        scr.fill(0)
        #scr.blit(Background.st,(0,0))
        scr.blit(Background.earth,Background.earthrect)
