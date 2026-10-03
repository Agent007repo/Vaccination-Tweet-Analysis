import ast
import json
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock
ROOT = Path(__file__).resolve().parents[1]

def definitions(filename, names, namespace):
    path = ROOT / filename
    if path.suffix == '.ipynb':
        nb = json.loads(path.read_text())
        text = '\n'.join(''.join(c['source']) for c in nb['cells'] if c['cell_type'] == 'code')
        text = '\n'.join(line if not line.startswith(('!', '%', 'pip install')) else '# '+line for line in text.splitlines())
    else:
        text = path.read_text()
    tree = ast.parse(text)
    body = [ast.ImportFrom(module='__future__', names=[ast.alias(name='annotations')], level=0)]
    body += [node for node in tree.body if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)) and node.name in names]
    module = ast.fix_missing_locations(ast.Module(body=body, type_ignores=[]))
    exec(compile(module, str(path), 'exec'), namespace)
    return namespace
import pandas as pd, numpy as np, networkx as nx, re, string

NS=definitions('Taha_Vaccination_tweet_analysis-2-fixed.ipynb',
    {'create_interaction_network','parse_hashtags','analyze_transformer_sentiment'},
    dict(pd=pd,np=np,nx=nx,re=re,string=string,ast=ast))

class TweetRegressionTests(unittest.TestCase):
    def test_weight_and_distance_have_opposite_meaning(self):
        frame=pd.DataFrame({'user_name':['alice','alice'],'mentions':[['bob'],['bob']]})
        graph=NS['create_interaction_network'](frame,min_weight=1)
        self.assertEqual(graph['alice']['bob']['weight'],2)
        self.assertEqual(graph['alice']['bob']['distance'],.5)
    def test_hashtag_literals_are_always_lists(self):
        self.assertEqual(NS['parse_hashtags']("'pfizer'"),['pfizer'])
        self.assertEqual(NS['parse_hashtags']("['a','b']"),['a','b'])
    def test_transformer_truncates_long_inputs(self):
        classifier=MagicMock(return_value=[{'label':'POSITIVE'}])
        NS['classifier']=classifier
        NS['analyze_transformer_sentiment'](['x'*10000])
        self.assertTrue(classifier.call_args.kwargs['truncation'])
