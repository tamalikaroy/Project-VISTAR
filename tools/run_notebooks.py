# Simple script to execute all notebooks in Notebooks/ (useful locally or in CI)
import glob, nbformat
from nbconvert.preprocessors import ExecutePreprocessor

for path in glob.glob("Notebooks/*.ipynb"):
    print("Executing", path)
    nb = nbformat.read(path, as_version=4)
    ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
    ep.preprocess(nb, {'metadata': {'path': 'Notebooks/'}})
    print("OK", path)
