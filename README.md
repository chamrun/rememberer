# remember
Rememberer is a tool to help your functions remember their previous results.

## Installation

```bash
pip install rememberer
```

## Usage

```python
from rememberer import rem

@rem
def add(a, b):
    import time
    time.sleep(3)
    return a + b

add(1, 2)  # this will take 3 seconds
add(1, 2)  # this will take 0 seconds
```

