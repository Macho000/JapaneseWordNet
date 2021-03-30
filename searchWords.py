import sqlite3
# from optparse import OptionParser
import argparse
import sys

parser = argparse.ArgumentParser(
        description='preprocess.py',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--inputfile', help='Import data')
args = parser.parse_args()

with open(args.inputfile, 'r') as f:
    read_data = f.read().splitlines()

# connect to wnjpn-small on sqlite3 
con = sqlite3.connect('wnjpn-small.db')
cur = con.cursor()

#loop each word 
for word in read_data:
    t = (word.lower(),)
    print(word)
    ## Get synonym word using index word
    cur.execute('select word.lemma from sense inner join word on sense.wordid=word.wordid inner join synset on synset.synset=sense.synset where synset.name=?', t)
    print("Synonyms are below")
    print(cur.fetchall())
    ## Get definition using index word
    cur.execute('select synset_def.def from synset_def left join synset on synset.synset=synset_def.synset where synset.name=?', t)
    print("definition are below")
    print(cur.fetchall())
    ## Get short sentence using index word
    cur.execute('select synset_ex.def from synset_ex left join synset on synset_ex.synset=synset.synset where synset.name=?', t)
    print("short sentence are below")
    print(cur.fetchall())
    print('-------------------------------------------------------------------------------------------------------')

