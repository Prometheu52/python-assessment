import pptx
import logging
import json
import logging as log
from main import exit_on_failure
from pptx.presentation import Presentation
from pptx.slide import SlideLayout, Slide
from pptx.shapes.placeholder import SlidePlaceholder
from pptx.util import Cm
from pptx.text.text import TextFrame
from pptx.enum.text import PP_PARAGRAPH_ALIGNMENT


#   Title slide:    Presentation().slide_layouts[0]     Title slide
#    Text slide:    Presentation().slide_layouts[1]     Title with Content,  Content = Text
#    List slide:    Presentation().slide_layouts[1]     Title with Content,  Content = List
# Picture slide:    Presentation().slide_layouts[8]     Picture with caption
#    Plot slide:    Presentation().slide_layouts[x]     Dunno

class ConfingDecoder:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.presentations: [str] = []
        try:
            self.json_file = open(self.config_path)
            self.config: dict = json.load(self.json_file)
        except OSError as err:
            log.critical(f"Could not open file with error: {err}")
            exit_on_failure()
        except ValueError as err:
            log.critical(f"The provided file is not in a valid json format, error: {err}")
            exit_on_failure()

        for presentation in self.config.keys():
            # Presentation raises ValueError if the given file is not a pptx file,
            # since we are not providing any, it should be fine
            prs: Presentation = pptx.Presentation()
            for slide in self.config[presentation]:
                # Handle Type
                match slide["type"]:
                    case "title":
                        logging.info(f"Title slide added to {presentation}")
                        self.__title_slide(prs, slide["title"], slide["content"])
                    case "text":
                        self.__text_slide(prs, slide["title"], slide["content"])
                    case "list":
                        print("list")
                    case "picture":
                        print("picture")
                    case "plot":
                        print("plot")
                    case other:
                        log.error(f"Unsupported type: \"{other}\" in \"{presentation}\" at {slide}")
                        log.info("Skipping slide..")
                        continue
                # Handle Title
                # Handle Content
                # Handle Configuration
            prs.save(f"{presentation}.pptx")

    def __title_slide(self, prs, title_name: str, subtitle: str):
        slide = prs.slides.add_slide(prs.slide_layouts[0])
        slide.shapes.title.text = title_name
        slide.placeholders[1].text = subtitle

    def __text_slide(self, prs: Presentation, title_name: str, content: str):
        slide: Slide = prs.slides.add_slide(prs.slide_layouts[5])
        slide.shapes.title.text = title_name

        w = Cm(22.86)
        #h = Cm(12.57)
        h = Cm(300)
        x = Cm(-7.7)
        y = Cm(4.45)
        textbox = slide.shapes.add_textbox(x, y, w, h)
        tf: TextFrame = textbox.text_frame
        tf.text = content
        tf.add_paragraph()
        tf.paragraphs[0].alignment = PP_PARAGRAPH_ALIGNMENT.LEFT


