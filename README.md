# About this repo
## This repo is the sqlite3 database for japanese word net
- How to use
  - `git clone https://github.com/Macho000/JapaneseWordNet`
  - `sqlite3 wnjpn.db`
- How to retrieve word from wnjpn.db
## Get synonym word using index word
  - `select word.lemma from sense inner join word on sense.wordid=word.wordid inner join synset on synset.synset=sense.synset where synset.name=?`
## Get definition using index word
  - `select synset_def.def from synset_def left join synset on synset.synset=synset_def.synset where synset.name=?`
## Get short sentence using index word
  - `select synset_ex.def from synset_ex left join synset on synset_ex.synset=synset.synset where synset.name=?`
