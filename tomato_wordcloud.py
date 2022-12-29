''' given a .csv file downloaded from https://mytomatoes.com,
    this script extracts and conjugates the verbs,
    then outputs them to a .txt file 

    subsequently, i recommend generating a point cloud by
    uploading the .txt file to https://wordclouds.com '''


import os, sys
import pandas as pd
import nltk # https://pypi.org/project/nltk/
from nltk.stem.wordnet import WordNetLemmatizer as WNL
nltk.download('wordnet')


def main():

    # read input csv, extract activity summary 
    df = pd.read_csv('csv/mytomatoes.csv',
                     sep=',',
                     names=['start', 'end', 'did'])
    did = df['did'].tolist()

    # extract and conjugate verbs
    verbs = get_conjug_verb_list(did)

    # write to txt
    with open('verbs.txt', mode='wt', encoding='utf-8') as f:
        f.write('\n'.join(verbs))


def get_conjug_verb_list(did):
    ''' given a list of activities (did),
        extract verbs, conjugate to present, correct errors
        note: assumes verb is first word in did column '''

    # from each entry, extract first word
    # note: assumes first word is verb
    verbs = [s.split(' ')[0] for s in did]

    # conjugate verbs to present tense
    verbs = [WNL().lemmatize(s,'v') for s in verbs]

    # define manual substitutions to correct typos + ntlk errors
    subs = {
            'analyzew': 'analyze',
            'buidl': 'build',
            'crete': 'create',
            'derivwe': 'derive',
            'disucss': 'discuss',
            'eval': 'evaluate',
            'instal': 'install',
            'organizer': 'organize',
            'organizew': 'organize',
            'prep': 'prepare',
            'prepped': 'prepare',
            'prepping': 'prepare',
            'robustified': 'robustify',
            'thikn': 'think',
    }

    # make substitutions
    verbs = [subs.get(i,i) for i in verbs]

    return verbs

if __name__ == '__main__':
    main()
