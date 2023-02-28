# Belqis client by Ahmed Khorsi

This is a python client for Belqis System
https://belqis.intelgx.com

# Installation

First you will have to sign up to get an API key
https://belqis.intelgx.com/signup

It is FREE

Then copy the token from the dashboard
https://belqis.intelgx.com/dashboard

then install the package

`pip install -U pybelqis`

# Usage

```python
from pybelqis import Belqis
b = Belqis(token='<put in here the token you get from https://belqis.intelgx.com/dashboard>')

# Diactritization
r = await b.tashkeel('السلام عليكم')
print(r)

# Other services
IN SHAA ALLAH will be made available
```
