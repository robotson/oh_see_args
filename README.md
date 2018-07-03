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
