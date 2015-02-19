import os
import sys

import requests
from bs4 import BeautifulSoup


PREFIX = 'http://www.urbandictionary.com/define.php?term='


def download_page(url, file_where_to_save):
    print('Attempt to get ' + url)
    r = requests.get(url)
    print('Success')
    with open(file_where_to_save, 'w') as fout:
        fout.write(r.text)


def get_ten_words(letter):
    url = 'http://www.urbandictionary.com/popular.php?character=' + letter.upper()
    html = requests.get(url).text
    soup = BeautifulSoup(html)
    for tag in soup.find_all(class_='popular'):
        yield tag.a.get_text()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: {0} LETTER\n'
              '    Downloads ten articles from Urban Dictionary and places\n'
              '    them in LETTER/ directory.'
              .format(sys.argv[0]))
        sys.exit(1)
    else:
        letter = sys.argv[1]
        if not os.path.exists(letter):
            os.mkdir(letter)
        words = list(get_ten_words(letter))[:10]
        print(words)
        for word in words:
            # maybe use robotic style '{0}/{1}.html'.format(letter, word)?
            # or vulgar style '{letter}/{word}.html'.format(**locals())?
            # or schizophrenic '{letter}/{word}.html'.format(letter=letter, word=word)?
            download_page(PREFIX + word, letter + '/' + word + '.html')

