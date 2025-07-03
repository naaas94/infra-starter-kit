# tests/test_pipeline.py

from src.infra_kit.pipeline import DummyPrivacyClassifier
import numbers

def test_pipeline_runs():
    clf = DummyPrivacyClassifier()
    result = clf.run()
    for i, pair in enumerate(result):
        assert isinstance(pair, tuple), f"Item {i} is not a tuple"
        assert len(pair) == 2, f"Item {i} does not have 2 elements"
        assert isinstance(pair[1], numbers.Integral), f"Item {i} second element is not an integer type"

