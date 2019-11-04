```
Build Tower
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *
Python: return a list;
JavaScript: returns an Array;
C#: returns a string[];
PHP: returns an array;
C++: returns a vector<string>;
Haskell: returns a [String];
Ruby: returns an Array;
Have fun!
```

def tower_builder(n_floors):
    # build here
    tower = []
    for i in range(n_floors):
        tower.append(' ' * (n_floors - i - 1) + '*' * ((i*2) + 1) + ' ' * (n_floors - i - 1))
    return tower
