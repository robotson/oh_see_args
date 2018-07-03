################################################################################
################################################################################
## "OH SEE ARGS" - A HACKY COMMAND LINE PYTHON SCRIPT TO GET TEXT FROM IMAGES
## https://github.com/robotson/oh_see_args
## by lance robotson
## robotsun@gmail.com
## july 2nd 2018
## version 0.0.0.0.0.666

## REQUIREMENTS TO INSTALL:
## pyocr (python library provides wrappers for tesseract or other OCR software)
# https://gitlab.gnome.org/World/OpenPaperwork/pyocr

## tesseract (C, C++, my code assumes tesseract with all languages installed)
# https://github.com/tesseract-ocr/tesseract

################################################################################
##  Need these guys to get command line arguments and such:
import sys
import argparse ## readmore: https://docs.python.org/3/library/argparse.html
##of course PIL for reading images
from PIL import Image
## and these guys for doing the OCR:
## (much of this script is based on the demo code at
## https://gitlab.gnome.org/World/OpenPaperwork/pyocr )
import pyocr
import pyocr.builders

################################################################################
### OCR PART!
## # https://gitlab.gnome.org/World/OpenPaperwork/pyocr
# Create PyOCR tools and check for tesseract or other OCR:
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1) # if we can't do OCR lets bail

tool = tools[0]
# uncomment to see what pyocr is getting for tools:

# print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'libtesseract'

langs = tool.get_available_languages()
# uncomment to see what pyocr is getting for languages!:

# print("Available languages: %s" % ", ".join(langs))
# print("Will use lang '%s'" % (lang))
# Ex: Will use lang 'fra'
# Note that languages are NOT sorted in any way. Please refer
# to the system locale settings for the default language
# to use.

## argparse lets us make nice help messages in the commange line usage,
try:
    from language_list_module import get_languages_help_text as help_text_getter
    languages_help_text = help_text_getter()
except:

    languages_help_text = "\n ".join(langs)

################################################################################
# see more: https://docs.python.org/3/library/argparse.html
#DEFINE THE ARGUMENT PARSER WITH HELPFUL MESSAGES
parser = argparse.ArgumentParser(
    description=
    'Run OCR on a provided path to an image file with optional language',
    formatter_class=argparse.RawTextHelpFormatter  # this argument gives line /
                                                 # / breaks in the help text :P
)

parser.add_argument(
    'path_to_image',
    help="Provide the full path to the image you wish to run OCR on\n "
)

parser.add_argument(
    'language_code',
    nargs='?',
    default="eng",
    help=
    "Specify language (defaults to english)\nReference Codes available:\n "
        + languages_help_text
)
#parse_args() gives us back an args object with the properties from command line
arguments = parser.parse_args()




################################################################################
#here's the actual magic part, we provide values from arguments and go!

# first lets try to see if the image is valid
# is the path to the image actually an image, or what?
# if we don't see a valid image we'll get an exception raised: IOError
# https://pillow.readthedocs.io/en/3.1.x/reference/Image.html
try:
    image = Image.open(arguments.path_to_image)
except:
    print(
    '\n An error occured looking for the image. Please double check path. \n '
    )
    sys.exit(1) # no image no point in sticking around SO BAIL

#if we make it this far lets get the actual OCR GOING ON OUR IMAGE!

txt = tool.image_to_string(
    image,
    lang=arguments.language_code,
    builder=pyocr.builders.TextBuilder()
)

##finally we just gonna print the result
print(txt)
#maybe in future version i pipe it to a translation service or something!
