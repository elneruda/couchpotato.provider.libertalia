from .main import libertalia

def autoload():
    return libertalia()

config = [{
    'name': 'libertalia',
    'groups': [
        {
            'tab': 'searcher',
            'list': 'torrent_providers',
            'name': 'libertalia',
            'description': 'See <a href="https://libertalia.me">Libertalia</a>',
            'icon': 'AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAAAABMLAAATCwAAAAAAAAAAAABcXGH/XFxh/1xcYf9cXGH/XFxh/1xcYf9cXGH/XFxh/1xcYf9cXGH/XFxh/1xcYf9cXGH/XFxh/1xcYf9cXGH/XFxh/1xcYf9cXGH/XFxh/1xdYf9cXGH/W1xh/1tcYf9bXGH/XFxh/1xcYf9cXGH/XFxh/1xcYf9cXGH/XFxh/1xcYf9cXGH/XFxh/1xcYf9bXGH/XV9i/2BhZf9eYGT/XV1i/1tcYf9cXGH/XFxh/1xcYf9cXGH/XFxh/1xcYf9cXGH/XFxh/1xcYf9bXGH/XF1i/1hZXv9PUFb/WFle/11fY/9dX2P/W1xh/1xdYf9cXGH/XFxh/1xcYf9cXGH/XFxh/1xcYf9cXGH/XF1i/1laX/9mZ2r/cnN2/1dYXP9HSE7/Wltf/15gY/9bXGD/XF1h/1xcYf9cXGH/XFxh/1xcYf9cXGH/XFxh/15gY/9RUlf/gYKE/9PT1P/d3d3/vb2+/1hZXv9SVFj/YGFl/1tcYP9cXGH/XF1h/1xcYf9cXGH/XF1h/1tcYf9bXGH/YmNm/zs9RP+0tLb////////////IyMn/XmBk/1tcYP9hYmX/XF1i/1tcYf9cXGH/XF1h/1tcYf9bXGH/Y2Ro/0xNUf+IiYv/8PDw/+zs7P+ys7T/1tfX/5eYmv8tLzj/UlRY/1tcYf9dX2P/W1xh/1tcYf9cXWL/ZWZp/0ZHTf9WV1v/6+vr//7+/v+MjY//BAsg/3d4e/+/wMH/qqus/3d4ev9UVVn/Vldb/11dYv9dX2P/XV9i/zM2Pv9rbG//3N3d//////+4uLn/OTpB/2RlaP9OT1T/bW5x/7Cwsf+0tLX/mJia/2lqbf9ZWl3/V1db/0pMUf+qqqz/7Ozs/+jp6f+qqqz/YWJm/1tcYP9dX2P/YGFk/1JUWP9BQkj/XmBk/4uLjv99foH/V1hc/15gZP++v7//4ODh/62ur/9bXGH/P0BG/1hZXv9dX2L/W1xh/1tcYf9eYGT/YWJl/1VWWv9PUFX/W1xh/1xdYv+DhIb/rKyu/2Vmaf81Nj//Vldb/2FiZv9dX2P/W1xh/1xdYf9cXWH/W1xh/1tcYf9eYGP/Xl9j/1pbYP9cXGH/XV9i/0dITv9SVFj/YmJm/15gZP9cXWH/W1xh/1xdYf9cXGH/XFxh/1xdYf9cXGH/W1xh/1xcYf9cXWL/XFxh/1pbYP9eYGT/XmBk/1tcYf9bXGH/XFxh/1xcYf9cXGH/XFxh/1xcYf9cXGH/XFxh/1xdYf9cXGH/W1xh/1xcYf9cXWL/XFxh/1tcYf9cXGH/XFxh/1xcYf9cXGH/XFxh/1xcYf9cXGH/XFxh/1xcYf9cXGH/XFxh/1xcYf9cXGH/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==',
            'wizard': True,
            'options': [
                {
                    'name': 'enabled',
                    'type': 'enabler',
                    'default': False,
                },
                {
                    'name': 'username',
                    'default': '',
                },
                {
                    'name': 'password',
                    'default': '',
                    'type': 'password',
                },
                {
                    'name': 'ignore_year',
                    'label': 'ignore year',
                    'default': 0,
                    'type': 'bool',
                    'description': 'Will ignore the year in the search results',
                },
                {
                    'name': 'seed_ratio',
                    'label': 'Seed ratio',
                    'type': 'float',
                    'default': 1,
                    'description': 'Will not be (re)moved until this seed ratio is met.',
                },
                {
                    'name': 'seed_time',
                    'label': 'Seed time',
                    'type': 'int',
                    'default': 40,
                    'description': 'Will not be (re)moved until this seed time (in hours) is met.',
                },
                {
                    'name': 'extra_score',
                    'advanced': True,
                    'label': 'Extra Score',
                    'type': 'int',
                    'default': 20,
                    'description': 'Starting score for each release found via this provider.',
                }
            ],
        },
    ],
}]
