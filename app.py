import json
import urllib.request
from urllib.error import HTTPError
import streamlit as st

st.title('Free English Dictionary')


def main():
    form2 = st.form(key='form2')
    text = form2.text_input('Enter any word')
    submit_button = form2.form_submit_button('Find')

    if submit_button:
        try:
            with urllib.request.urlopen("https://api.dictionaryapi.dev/api/v2/entries/en/{}".format(text)) as url:
                #print('data 1')
                data = json.load(url)
                #print('data 2', data)

                if len(data) > 0 and data[0]['meanings'][0] is not None:
                    i = data[0]['meanings'][0]
                    if i['definitions'] is not None:
                        definitions = data[0]['meanings'][0]['definitions']
                        st.write('Meaning of ', text, 'is: ')
                        c = 0
                        for i in definitions:
                            st.write(c+1, i['definition'])
                            c += 1

                    col1, col2 = st.columns([6, 6])
                    synonyms = i['synonyms']
                    antonyms = i['antonyms']
                    #print(antonyms)
                    with col1:
                        if len(synonyms) > 0:
                            st.write('Synonyms')
                            for s in synonyms:
                                st.write(s)
                    with col2:
                        if len(antonyms) > 0:
                            st.write('Antonyms')
                            for s in antonyms:
                                st.write(s)
        except urllib.error.HTTPError as err:
            st.write('Sorry pal, we could not find definitions for the word you were looking for')
            st.write('You can try the search again at later time or head to the web instead.')


if __name__ == '__main__':
    main()
