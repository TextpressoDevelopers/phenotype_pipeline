# phenotype_pipeline

This is a wrapper of Textpressocentral API that can be used to easily query phenotype papers and export all sentences to TSV file. 
The returned sentences can be either those matched by the query or all sentences in the documents. The types of sentences to be 
returned is specified by the *include_match_sentences* and *include_all_sentences* parameters (see examples below).

Note that a valid Textpressocentral API token is required in order to run the script. See the 
[API documentation](https://textpressoapi.readthedocs.io/en/latest/obtaining_a_token.html) for additional info on how to 
obtain a token.

## Examples

Remember to replace the API token and the paper IDs in the following examples.

### Extract all matching phenotype sentences from a specific paper and save them to TSV file

`python3 phenotype_pipeline.py -a "{\"token\":\"XXX\", \"query\": {\"categories\": [\"tables and figures (tptbfig:0000001)\",\"genetic perturbation (tpgp:0000001)\",\"phenotypic perturbation (tppp:0000001)\"], \"categories_and_ed\": true, \"accession\": \"WBPaper00000000\", \"type\": \"sentence\", \"corpora\": [\"C. elegans\"]}, \"include_match_sentences\": true}" > output.tsv`

Note that the example uses a TPC query containing a combination of categories on sentences, but any valid TPC query can 
be passed to the script. See the [API documentation](https://textpressoapi.readthedocs.io/en/latest/?badge=latest) for 
more details on TPC queries.

### Extract all sentences from a specific paper and save them to TSV file

`python3 phenotype_pipeline.py -a "{\"token\":\"XXX\", \"query\": {\"accession\": \"WBPaper00000000\", \"type\": \"document\", \"corpora\": [\"C. elegans\"]}, \"include_all_sentences\": true}" > output.tsv`

## Other example queries

`python3 phenotype_pipeline.py -a "{\"token:\"XXX\", \"query\": {\"keywords\": \"daf-16 AND Parkinson\", \"type\": \"sentence\", \"corpora\": [\"C. elegans\"]}, \"include_match_sentences\": true}"` 

`python3 phenotype_pipeline.py -a "{\"token:\"XXX\", \"query\": {\"keywords\": \"daf-16 AND Parkinson\", \"type\": \"sentence\", \"corpora\": [\"C. elegans\"]}, \"include_all_sentences\": true}"`

