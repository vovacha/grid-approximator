# Grid Approximator

Approximates contrast element using grid. 

Input:
- a picture with contrast elements to be approximated
- one of two parameters (grid size in pixels or number of grid pieces)

Output:
- a picture with an approximated element

![Alt text](ukraine_grid.jpg?raw=true "Grid approximation example")

## Usage examples
#### 1. Approximate element with unknown grid size and 784 grid pieces
    > python grid_approximator.py --image ukraine.jpg --divide 784
    Element was divided into 780 pieces instead of 784 (63 pixels grid size)
    New image with approximated element was successfully created: ukraine_grid.jpg
The output is shown in the picture above.
#### 2. Approximate element with known grid size equals to 55 pixels
    > python grid_approximator.py --image ukraine.jpg --grid 55
    New image with approximated element was successfully created: ukraine_grid.jpg
