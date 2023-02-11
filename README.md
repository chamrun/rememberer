# rememberer
Rememberer is a tool to help your functions remember their previous results.


The advantage of this package compared to other memoization packages is that 
it will remember the result of the function even if you kill the program and restart it. 

It will also remember the result even if you restart the python interpreter because
it uses a pickle file to store the results.

## Installation

```bash
pip install rememberer
```

## Usage

```python
from rememberer import rem

def add(a, b):
    import time
    time.sleep(3)
    return a + b

rem(add, 1, b=2)  # this will take 3 seconds
rem(add, 1, b=2)  # this will take ~0 seconds
```

You can use it as a decorator as well:

```python
from rememberer import rem_dec

@rem_dec
def add(a, b):
    import time
    time.sleep(3)
    return a + b

add(1, b=2)  # this will take 3 seconds
add(1, b=2)  # this will take ~0 seconds
```


If you want to clear the cache, you can use the `forget` method:

```python
from rememberer import forget

forget(add, 1, b=2)

```

