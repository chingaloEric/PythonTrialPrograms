# imports from python built in modules
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['eric'] = 'Javascript'
favorite_languages['lisa'] = 'Java'
favorite_languages['Miguel'] = 'Python'
favorite_languages['Mirabelle'] = 'Typescript'

for name, language in favorite_languages.items():
    print(name.title() + ' codes in ' + language + '.' )
