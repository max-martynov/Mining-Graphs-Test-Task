import sys
import tqdm
import json
from pathlib import Path

sys.path.append("libs/parser")

from libs.parser.src.modules.php.resource import build_resource_tree
from libs.parser.src.modules.php.visitors.resolvers import TablesBuilder
from libs.parser.src.modules.php.traversers.bf import BFTraverser

repos_root = Path('repos')

tree = build_resource_tree(repos_root)
bft = BFTraverser(tree)
node_finder = TablesBuilder(tree)
bft.register_visitor(node_finder) 
bft.traverse()

def explore(dict, cnt):
    for k, v in dict.items():
        if isinstance(v, list):
            for tup in v:
                if isinstance(tup, tuple):
                    cur = cnt.get(tup[0], 0)
                    cnt[tup[0]] = cur + 1
                    explore(tup[1], cnt)
        elif isinstance (v, tuple):
            cur = cnt.get(v[0], 0)
            cnt[v[0]] = cur + 1
            explore(v[1], cnt)

methods_to_stats = {}
for file, method_nodes in tqdm.tqdm(dict(tree.method_table).items()):
    for k, v in method_nodes.items():
        method, _ = v
        _, dic = method.generic()
        cnt = {}
        explore(dic, cnt)
        methods_to_stats[file.lstrip(str(repos_root.resolve())) + '#' + method.name] = cnt

for file, function_nodes in tqdm.tqdm(dict(tree.function_table).items()):
    for k, v in function_nodes.items():
        _, dic = v.generic()
        cnt = {}
        explore(dic, cnt)
        methods_to_stats[file.lstrip(str(repos_root.resolve())) + ':' + v.name] = cnt

stats_sum = {}
for file, stats in methods_to_stats.items():
    for param_name, value in stats.items():
        cur = stats_sum.get(param_name, 0)
        stats_sum[param_name] = cur + value

f = open('output.txt', 'a')
f.truncate(0)
f.write('Processed {} php files with {} methods and functions in total. See statistics below.\n\n'.format(len(dict(tree.method_table)) + len(dict(tree.function_table)), len(methods_to_stats)))

for param_name, sum_values in stats_sum.items():
    f.write('Average number of {} statement: {}\n'.format(param_name, sum_values / len(methods_to_stats)))

f.write('\n-----------------------\n')

f.write(json.dumps(methods_to_stats, sort_keys=True, indent=4))

