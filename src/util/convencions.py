from enum import Enum

class Colors(Enum):
    DARK_GRAY = "#353535"
    DARK_HARD_GRAY = "#181818"
    COLOR_FONT_DEFAULT = "#F2F2F2"

class Font(Enum):
    ROBOTO = ('src/view/RobotoMono-Regular.ttf', 11)
    ROBOTO_TITLE = ('src/view/RobotoMono-Regular.ttf', 13, 'bold')

class Labels(Enum):
    TITLE = "Cameras IP - RSTP"
    

class Contants(Enum):
    ENCONDING = 'utf-8'
    KEY= b'lv7oVYE8bvsSl466'
    VETOR=b'cIp6LlipSkGVNowd'
    
