# Tupper´s self-referential formula

### Introduction

It is a formula that visually represents itself when graphed at a specific location in the *(x, y)* plane. The formula was defined by Jeff Tupper and appears as an example in [Tupper's 2001 SIGGRAPH paper](http://www.dgp.toronto.edu/people/mooncake/papers/SIGGRAPH2001_Tupper.pdf) on reliable two-dimensional computer graphing algorithms.  

The formula is a general-purpose method of decoding a bitmap stored in the constant k, and it could actually be used to draw any other image. When applied to the unbounded positive range 0 ≤ y, the formula tiles a vertical swath of the plane with a pattern that contains all possible 17-pixel-tall bitmaps. One horizontal slice of that infinite bitmap depicts the drawing formula itself, but this is not remarkable, since other slices depict all other possible formulae that might fit in a 17-pixel-tall bitmap. Tupper has created extended versions of his original formula that rule out all but one slice (For example, [1](http://www.peda.com/selfplot/selfplot3big.png), [2](http://www.peda.com/selfplot/selfplot2.png) or [3](http://www.peda.com/selfplot/selfplot.png)).  

The constant k is a simple monochrome bitmap image of the formula treated as a binary number and multiplied by 17. If k is divided by 17, the least significant bit encodes the upper-right corner (k, 0); the 17 least significant bits encode the rightmost column of pixels; the next 17 least significant bits encode the 2nd-rightmost column, and so on.  

Information taken from [Wikipedia](https://en.wikipedia.org/wiki/Tupper%27s_self-referential_formula).

### Formula

The formula is an inequality defined as:  

![tupper-plot](https://github.com/PatricioIribarneCatella/tupper-plot/blob/master/tupper-plot.png)

### Build and Run

```bash
	make
```

It will generate a directory called *images* that contains the result in two different formats (*png* and *svg*).  

To delete this directory type:  

```bash
	make clean
```

