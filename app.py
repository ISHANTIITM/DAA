import os
import base64
from io import BytesIO
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

def fig_to_base64(fig):
    buf = BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    return f"data:image/png;base64,{img_base64}"

@app.get("/")
def analyze_network():
    # Read CSV
    df = pd.read_csv("edges.csv")
    G = nx.Graph()
    for _, row in df.iterrows():
        G.add_edge(row[0], row[1])

    # Metrics
    edge_count = G.number_of_edges()
    degrees = dict(G.degree())
    highest_degree_node = max(degrees, key=degrees.get)
    average_degree = sum(degrees.values()) / len(degrees)
    density = nx.density(G)

    try:
        shortest_path_alice_eve = nx.shortest_path(G, source="Alice", target="Eve")
    except (nx.NetworkXNoPath, nx.NodeNotFound):
        shortest_path_alice_eve = None

    # Network graph image
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', ax=ax1)
    network_graph_b64 = fig_to_base64(fig1)

    # Degree histogram image
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    ax2.hist(list(degrees.values()), bins=range(1, max(degrees.values()) + 2), align='left', rwidth=0.8)
    ax2.set_xlabel("Degree")
    ax2.set_ylabel("Frequency")
    ax2.set_title("Degree Histogram")
    degree_histogram_b64 = fig_to_base64(fig2)

    # JSON response
    return JSONResponse(content={
        "edge_count": edge_count,
        "highest_degree_node": highest_degree_node,
        "average_degree": average_degree,
        "density": density,
        "shortest_path_alice_eve": shortest_path_alice_eve,
        "network_graph": network_graph_b64,
        "degree_histogram": degree_histogram_b64
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port)
