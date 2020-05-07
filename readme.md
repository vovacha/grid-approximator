# Grid Approximator

Approximates contrast element using grid. 

Input:
- a picture with contrast element to be approximated
- one of two parameters (grid size in pixels or number of grid pieces)

Output:
- a picture with an approximated element

## Usage examples
##### Approximate element with unknown grid size and 300 grid pieces
    > python grid_approximator.py --image ukraine.jpg --divide 300
    Element was divided into 296 pieces instead of 300
    New image with approximated element was successfully created: ukraine_grid.jpg
##### Approximate element with known grid size equals to 55 pixels
    > python grid_approximator.py --image ukraine.jpg --grid 55
    New image with approximated element was successfully created: ukraine_grid.jpg