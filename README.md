# gudlogger

a nice and simple logging library for python

not very optimised, but the log messages r pretty so

## installation

right now its not on pip, so you need to download gudlogger.py and put it in your project.
next, you can import it

## usage

### basic example
```py
import gudlogger

logger = gudlogger()

logger.info("this sucks ass")
```
### more advanced example
```py
from gudlogger import *

logger = Logger(defaultPrefix="<TIME> GUDLOGGER", shouldColorText=True, debug=True)

logger.info("Hello", "INFO")
```

## all arguments
```py
debug: bool (default = False)
defaultPrefix: str (default = None)
shouldColorText: bool (default = False)
newlineBetweenLogs: bool (default = False)
```