from PIL import Image
from PIL import ImageDraw
import json


def mark_image(filters):
    im = Image.open("./resultado.jpg")

    with open('./resultado.json') as j:
        it_orig = json.loads("".join(j.
                                     readlines()))['responses'][0].values()[0]

        for str_filter in filters:
            it = _find(_equals(str_filter), it_orig)

            if not it:
                it = _find(lambda x: str_filter in x['description'], it_orig)

            if not it:
                it = _find(lambda x: str_filter in
                           ''.join(c for c in x['description'] if c.isalnum()),
                           it_orig)

            if not it:
                for z in str_filter.split(' '):
                    it = _find(_equals(z), it_orig)
                    _execute(it, im)
                if it:
                    continue

            if not it:
                it = _find(lambda x: x['description'] in str_filter, it_orig)

            _execute(it, im)

        # write to stdout
        im.save("./PY.png", "PNG")


def _execute(it, im):
    diff = 15
    width = 8

    for name, vertices in it:
        bounds = [vertices[0]['x']-diff, vertices[0]['y']-diff,
                  vertices[2]['x']+diff, vertices[2]['y']+diff]
        print 'Name found: ' + name
        for i in range(width):
            draw = ImageDraw.Draw(im)
            draw.rectangle(bounds, outline="red")
            bounds = (bounds[0]+1, bounds[1]+1, bounds[2]+1,
                      bounds[3]+1)
            del draw


def _equals(_str):
    return lambda x: _str == x['description']


def _find(function, it_orig):
    return map(lambda z: (z['description'], z['boundingPoly']['vertices']),
               filter(function, it_orig[1:]))


if __name__ == '__main__':
    _list = {'ONYX COMPUTER SERVICES', '00017015', '1090', '1/1/2015'}
    mark_image(_list)
