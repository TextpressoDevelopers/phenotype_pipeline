import argparse
import json
import os
import re
import ssl
from collections import defaultdict
from itertools import zip_longest
from urllib import request


def get_document_sentences(api_request_text):
    """
    get the sentences of the specified documents
    :param api_request_text: a json text containing the API request to perform - include_sentences must be set to true
    :return (Dict[str, List[str]]): a dictionary with paper ids as key and the list of their sentences as value
    """
    api_endpoint = "https://textpressocentral.org:18080/v1/textpresso/api/search_documents"
    data = api_request_text
    data = data.encode('utf-8')
    req = request.Request(api_endpoint, data, headers={'Content-type': 'application/json',
                                                       'Accept': 'application/json'})
    res = request.urlopen(req)
    sentences = defaultdict(list)
    doc_key = "matched_sentences" if "include_match_sentences" in api_request_text else "all_sentences"
    for doc in json.loads(res.read().decode('utf-8')):
        sentences[doc["identifier"].split("/")[1][7:].split(".")[0]] = [re.sub(
            '\\t', ' ', re.sub('\\s+', ' ', sent.replace('\n', '')).strip()) for sent in doc[doc_key] if sent and
                                                                                                         sent != ""]
        sentences[doc["identifier"].split("/")[1][7:].split(".")[0]] = [
            sent for sent in sentences[doc["identifier"].split("/")[1][7:].split(".")[0]] if sent]
    return sentences


def main():
    parser = argparse.ArgumentParser(description="Perform phenotype search ")
    parser.add_argument("-a", "--api-request", metavar="api_request_text", dest="api_request_text", type=str)
    args = parser.parse_args()

    if not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context
    sentences = get_document_sentences(args.api_request_text)
    sent_rows = zip_longest(*[pap_sentences for pap_sentences in sentences.values()])
    print(*[paper_id for paper_id in sentences.keys()], sep="\t")
    for sent_row in sent_rows:
        sent_row = [sent if sent else "" for sent in
                    sent_row]
        print(*sent_row, sep="\t")


if __name__ == '__main__':
    main()
