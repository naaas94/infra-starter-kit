# tests/test_pipeline.py

from infra_kit.pipeline import DummyPrivacyClassifier

def test_pipeline_runs():
    clf = DummyPrivacyClassifier()
    result = clf.run()
    assert isinstance(result, list)
    assert all(len(pair) == 2 for pair in result)
    assert all(isinstance(pair[1], (int, float)) for pair in result)
