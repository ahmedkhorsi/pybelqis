# Belqis client by Ahmed Khorsi

This is a python client for Belqis System
https://belqis.intelgx.com


# Installation
First you will have to sign up to get an API key 
https://belqis.intelgx.com/signup

then install the package

`pip install -U belqis`

# Usage

```python
from belqis import Belqis
b = Belqis(token='<put here the token you get from https://belqis.intelgx.com/dashboard>')

# Diactritization
r = b.tashkeel('the sentence you want belqis to diacritize')

# NER
r = b.ner('the sentence you want belqis to diacritize')

#Speech recognition
r = b.dictate(<audio_file_url>)

#Speech recognition
r = b.pronounce(<audio_file_url>, <ref_text>)
r = b.diac('the sentence you want belqis to diacritize')
```

If no error occurs you will get a json. Try it out so you get familiar with the format
