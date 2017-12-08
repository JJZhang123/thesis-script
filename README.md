Provided are 4 directories:

- csicorpus: the CSI corpus of Verhoeven and Daelemans (2014), in the vanilla state.
- features: every feature has a directory with 2 files (features.txt, labels.txt),
			preprocessed and such.
- parsed_reviews: the raw reviews parsed by the Alpino Parser (all, positive, and negative data).
- tokenized_reviews: tokenized sentences for the Alpino Parser using sentokenizer.py

Provided are 3 scripts:

- classification.py: main script used for classification tasks.
- sentokenizer.py: script to tokenize the sentences, appropriate for the Alpino Parser.
- parser.py: script used to parse the tokenized sentences.

If anything is unclear please contact me:
j.j.zhang.1@student.rug.nl