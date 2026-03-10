
import json
from validator import validate_dataset
from triangulation import detect_triangulation
from relationship_graph import build_graph
from ai_runners import run_chatgpt,run_grok,run_gemini
from consensus import score

def run(dataset_path):

with open(dataset_path) as f:
    data=json.load(f)

validate_dataset(data)

triangulation=detect_triangulation(data["messages"])
graph=build_graph(data["messages"])

chatgpt=run_chatgpt(data)
grok=run_grok(data)
gemini=run_gemini(data)

ai={
"chatgpt":chatgpt,
"grok":grok,
"gemini":gemini
}

consensus_scores=score(ai)

results={
"ai":ai,
"triangulation":triangulation,
"graph":graph,
"consensus":consensus_scores
}

return results
