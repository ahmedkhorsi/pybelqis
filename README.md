# PyBelqis by Ahmed Khorsi

This is a python client for Belqis System
https://belqis.intelgx.com

# Installation

`pip install -U pybelqis`

# Usage

```python
from belqis import
b = Belqis(token='<put here the token you get from https://belqis.intelgx.com/dashboard>')
r = b.diac('the sentence you want belqis to diacritize')
```

If no error occurs you will get a json. Try it out so you get familiar with the format
