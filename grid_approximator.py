import sys

from PIL import Image, ImageDraw
import numpy


def iterate_squares(im, step):
    black_white_image = im.convert('1')
    arr = numpy.array(black_white_image)
    width, height = len(arr[0]), len(arr)

    width_squares, r = divmod(width, step)
    if r:
        width_squares += 1
    height_squares, r = divmod(height, step)
    if r:
        height_squares += 1

    for w1 in range(width_squares):
        w1 *= step
        if w1 + step > width:
            w2 = width
        else:
            w2 = w1 + step

        for h1 in range(height_squares):
            h1 *= step
            if h1 + step > height:
                h2 = height
            else:
                h2 = h1 + step

            for ww in range(w1, w2):
                for hh in range(h1, h2):
                    if not arr[hh][ww]:
                        yield (w1, w2), (h1, h2)
                        break
                else:
                    continue
                break


def draw_squares(im, step, color, width=2):
    draw = ImageDraw.Draw(im)
    for (w1, w2), (h1, h2) in iterate_squares(im, step):
        draw.line(((w1, h1), (w2, h1)), fill=color, width=width)
        draw.line(((w1, h2), (w2, h2)), fill=color, width=width)
        draw.line(((w1, h1), (w1, h2)), fill=color, width=width)
        draw.line(((w2, h1), (w2, h2)), fill=color, width=width)
    return im


def find_optimal_grid_step(im, divide_by):
    print('Searching for optimal grid step in pixels ...')
    width = im.width
    left, right = 0, width - 1
    count_step = {}

    while left <= right:
        step = (left + right) // 2
        count = len(list(iterate_squares(im, step)))
        if count == divide_by:
            return step, count

        if count > divide_by:
            left = step + 1
        elif count < divide_by:
            right = step - 1

        print(f'Divided by: {count}. Step pixels: {step}')
        count_step[count] = step

    prev_count = None
    for count in sorted([c for c in count_step]):
        if prev_count is None:
            prev_count = count
            continue
        if prev_count < divide_by < count:
            return count_step[prev_count], prev_count
        prev_count = count


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Approximates contrast element using grid. As input could '
                                        'take grid size in pixels or number of grid pieces')
    parser.add_argument('-i', '--image',
                        dest='image',
                        help='Input image path',
                        metavar='FILE',
                        required=True)
    parser.add_argument('-d', '--divide',
                        dest='divide',
                        help='How many pieces to divide',
                        type=int,
                        default=None)
    parser.add_argument('-g', '--grid',
                        dest='grid',
                        type=int,
                        default=None,
                        help='Step in pixels for grid')

    args = parser.parse_args()
    divide_by = args.divide
    image_path = args.image
    step_pixels = args.grid

    if not any((divide_by, step_pixels)):
        print('Provide one of next params: --grid (in pixels) or --divide (in pieces)')
        sys.exit()

    im = Image.open(image_path)
    if not divide_by:
        pass
    elif not step_pixels:
        step_pixels, divided_by = find_optimal_grid_step(im, divide_by)
        print('_' * 100)
        if divided_by != divide_by:
            print(f'Element was divided into {divided_by} pieces instead of {divide_by}')
        else:
            print(f'Element was divided into {divided_by} pieces')

    color = (0, 0, 0, 0)
    im_grid = draw_squares(im, step_pixels, color)
    file_name = image_path.split('.')[0] + '_grid' + '.jpg'
    im_grid.save(file_name)
    print(f'New image with approximated element was successfully created: {file_name}')
