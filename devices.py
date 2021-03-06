# The Evervolv Project

# XXX: EDITING :XXX
# ADDING DEVICES:
#     Add to the _devices dict, should be alphabetical.
#     'maintainer' field needs to be a tuple, so single entries need a trailing comma
# ADDING MAINTAINERS:
#     Add yourself to the bottom of the _maintainers dict,
#     'url' should be twitter or g+ (somewhere you publicly post your android news) 


from collections import OrderedDict

__all__ = (
    'devices',
    'maintainers',
)

_devices = {
    'bravo': {
        'codename': 'Turba',
        'retail_name': 'HTC Desire (GSM)',
        'maintainer': ('Nikez',),
    },
    'd710': {
        'codename': 'Clarus',
        'retail_name': 'Samsung Epic 4G Touch',
        'maintainer': ('dastin1015',),
    },
    'glacier': {
        'codename': 'Glacialis',
        'retail_name': 'T-mobile myTouch 4G',
        'maintainer': ('elginsk8r',),
    },
    'grouper': {
        'codename': 'Mirus',
        'retail_name': 'Google Nexus 7',
        'maintainer': ('drewis',),
    },
    'hercules': {
        'codename': 'Potens',
        'retail_name': 'Samsung Galaxy S II (T-Mobile)',
        'maintainer': ('elginsk8r',),
    },
    'inc': {
        'codename': 'Dives',
        'retail_name': 'HTC Droid Incredible',
        'maintainer': ('MongooseHelix',),
    },
    'jewel': {
        'codename': 'Bellus',
        'retail_name': 'HTC Evo 4G LTE',
        'maintainer': ('preludedrew','dastin1015'),
    },
    'kingdom': {
        'codename': 'Scio',
        'retail_name': 'HTC Evo Design 4G',
        'maintainer': ('preludedrew',),
    },
    'm7spr': {
        'codename': 'Regius',
        'retail_name': 'HTC One (Sprint)',
        'maintainer': ('dastin1015','preludedrew'),
    },
    'mako': {
        'codename': 'Fulsi',
        'retail_name': 'Google Nexus 4',
        'maintainer': ('drewis',),
    },
    'manta': {
        'codename': 'Stella',
        'retail_name': 'Google Nexus 10',
        'maintainer': ('',),
    },
    'passion': {
        'codename': 'Perdo',
        'retail_name': 'Google Nexus One',
        'maintainer': ('drewis',),
    },
    'pyramid': {
        'codename': 'Macto',
        'retail_name': 'HTC Sensation',
        'maintainer': ('Nikez',),
    },
    'ruby': {
        'codename': 'Iaceo',
        'retail_name': 'HTC Amaze 4G',
        'maintainer': ('preludedrew',),
    },
    'shooter': {
        'codename': 'Neco',
        'retail_name': 'HTC Evo 3D',
        'maintainer': ('preludedrew','Flintman','dastin1015'),
    },
    'shooteru': {
        'codename': 'Signum',
        'retail_name': 'HTC Evo 3D (GSM)',
        'maintainer': ('helicopter88',),
    },
    'speedy': {
        'codename': 'Artis',
        'retail_name': 'HTC Evo Shift 4G',
        'maintainer': ('preludedrew',),
    },
    'supersonic': {
        'codename': 'Acies',
        'retail_name': 'HTC Evo 4G',
        'maintainer': ('preludedrew',),
    },
    'tenderloin': {
        'codename': 'Queo',
        'retail_name': 'HP Touchpad',
        'maintainer': ('preludedrew','Flintman'),
    },
    'toro': {
        'codename': 'Primo',
        'retail_name': 'Samsung Galaxy Nexus (Verizon)',
        'maintainer': ('MongooseHelix',),
    },
    'vivow': {
        'codename': 'Conor',
        'retail_name': 'HTC Droid Incredible 2',
        'maintainer': ('preludedrew',),
    },
}

# Note: this is initialized as a list of tuples
# This will not get sorted, order here is how it appears on the site
_maintainers = OrderedDict ([
    (
        'preludedrew',
        {
            'url': 'http://twitter.com/preludedrew',
            'extra': ('Founder','Admin'),
        }
    ),
    (
        'drewis',
        {
            'url': 'https://plus.google.com/u/0/102710594547223731659/posts',
            'extra': ('Admin',),
        }
    ),
    (
        'MongooseHelix',
        {
            'url': 'http://twitter.com/MongooseHelix',
            'extra': ('Admin',),
        }
    ),
    (
        'Nikez',
        {
            'url': 'http://twitter.com/LaidbackNikez',
        }
    ),
    (
        'elginsk8r',
        {
            'url': 'https://plus.google.com/u/0/100948280470840956633/posts',
        }
    ),
    (
        'Flintman',
        {
            'url': 'http://twitter.com/wbellavance',
        }
    ),
    (
        'dastin1015',
        {
            'url': 'http://twitter.com/dastin1015',
        }
    ),
    (
        'helicopter88',
        {
            'url': 'http://forum.xda-developers.com/member.php?u=1924950',
        }
    ),
])

# Add devices to _maintainers
for m in _maintainers.keys():
    _maintainers[m]['devices'] = tuple(sorted(d for d in _devices.keys() if m in
                    _devices.get(d).get('maintainer')))

# Public
def devices(device=None):
    if device:
        return _devices.get(device)
    else:
        return sorted(_devices.keys())

def maintainers(name=None):
    if name:
        return _maintainers.get(name)
    else:
        return _maintainers.keys()
