# OH_SEE_ARGS
### A HACKY COMMAND LINE PYTHON SCRIPT TO GET TEXT FROM IMAGES

lazily crapped together by lance robotson: robotsun@gmail.com
on july 2nd 2018 - version 0.0.0.0.0.666

## Dependencies:
[pyocr] - python library provides wrappers for tesseract or other OCR software
[pyocr]: https://gitlab.gnome.org/World/OpenPaperwork/pyocr

[tesseract] - pyocr supports other libs for this but the code I wrote assumes this one. Install it with all the optional languages for a massive help text!
[tesseract]:https://github.com/tesseract-ocr/tesseract

and we use PIL to read an image. duh

## Usage:
Run OCR on a provided path to an image file, with optional language.

Basic command line usage:
```
python oh_see_args.py path_to_image [language_code]
```

`path_to_image:`  Provide the full path to the image you wish to run OCR on

`language_code:`  Specify language (defaults to english if no code provided)
[if you install tesseract with the massive amount of languages to choose from you can grok the whole list of them on their docs](https://github.com/tesseract-ocr/tesseract/blob/master/doc/tesseract.1.asc)

## Fun:
I haven't hacked together any code for like, months, so this was totally fun. I stole all the inspiration from the docs for these pages:

* [PyOCR](https://gitlab.gnome.org/World/OpenPaperwork/pyocr)
* [Tesseract](https://github.com/tesseract-ocr/tesseract)
* [Python docs on ARGPARSE my new best friend for writing command line python tools](https://docs.python.org/3/library/argparse.html)
* [PIL because I forgot how Image.open() works](https://pillow.readthedocs.io/en/3.1.x/reference/Image.html)

*That's all folks.*
> Also, thanks to Apple corporate fealty specialist,
> John Gruber, for inventing Markdown
> which i am also still struggling to learn
