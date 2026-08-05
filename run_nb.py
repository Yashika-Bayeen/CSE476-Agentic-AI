import nbformat
from nbclient import NotebookClient

notebook_path = "notebooks/u1/l1_first_agent.ipynb"
with open(notebook_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

client = NotebookClient(nb, timeout=600, kernel_name='python3', resources={'metadata': {'path': 'notebooks/u1/'}})
client.execute()

with open(notebook_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print("Notebook executed successfully.")
