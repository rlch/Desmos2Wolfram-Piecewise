# desmos2wolfram_piecewise
Converts piecewise desmos functions to a format acceptable by WolframAlpha

# Usage
```python
python desmos2wolfram.py "function 1" "function 2" ...
```

# Example
```python
python .\desmos2wolfram.py "\left\{0\le w<\frac{1}{2}:0,\frac{1}{2}\le w<1:0.999,w=1:1\right\}" 
                           "\left\{0\le w\le\frac{1}{2}:\frac{1}{2}w,\frac{1}{2}<w\le\frac{3}{4}:\frac{1}{4},\frac{3}{4}<w\le1:3w-2\right\}" 
                           "\left\{0\le w\le1:w^{\frac{1}{5}}\right\}"

> Piecewise[{{0, 0\le w<\frac{1}{2}},{0.999, \frac{1}{2}\le w<1},{1, w=1}}] 
> Piecewise[{{\frac{1}{2}w, 0\le w\le\frac{1}{2}},{\frac{1}{4}, \frac{1}{2}<w\le\frac{3}{4}},{3w-2, \frac{3}{4}<w\le1}}]
> Piecewise[{{w^{\frac{1}{5}}, 0\le w\le1}}]
```
