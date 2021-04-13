from random import randint
from sys import argv
import io
import csv
from mimesis import Person, Address


def checkArgs(argv):
    if len(argv) < 3 or len(argv) > 3:
        raise AttributeError('Incorrect number of parameters')
    else:
        script, num, locale = argv
        if not (int(num) > 0):
            raise AttributeError('The number of entries must be greater than 0')
        else:
            return num, locale


def getRegion(locale):
    if locale in ('en', 'us', 'US', 'en_US'):
        locale = 'en'
        country = 'US'
    elif locale in ('ru', 'Ru'):
        locale = 'ru'
        country = 'РФ'
    elif locale in ('uk', 'UA'):
        locale = 'uk'
        country = 'Укр'
    else:
        raise ValueError('you can choose locale from English(\'en\'), Русский(\'ru\'), Українська (\'uk\')')
    return locale, country


def generatingData(num, locale, country):
    person = Person(locale)
    address = Address(locale)
    buffer = io.StringIO()
    writer = csv.writer(buffer, delimiter=';', lineterminator="\n", quoting=csv.QUOTE_NONE, escapechar='\\')
    for i in range(int(num)):
        writer.writerow([
            person.full_name(),
            country if randint(0, 1) == 1 else address.country(),
            ', '.join([
                address.province(),
                address.city(),
                address.address()
            ]),
            person.telephone()
        ])
    return buffer.getvalue()


if __name__ == '__main__':
    try:
        num, locale = checkArgs(argv)
        locale, country = getRegion(locale)
        print(generatingData(num, str(locale), country))
    except AttributeError as e:
        print("AttributeError.  {0}".format(e))
    except ValueError as e:
        print('ValueError.  {0}'.format(e))
    except Exception as e:
        print('Error. Something wrong.{0}'.format(e))
