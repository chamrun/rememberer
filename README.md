# remember
Rememberer is a tool to help your functions remember their previous results.

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

