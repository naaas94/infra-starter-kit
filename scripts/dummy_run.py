# scripts/dummy_run.py

from infra_kit.pipeline import DummyPrivacyClassifier

if __name__ == "__main__":
    pipeline = DummyPrivacyClassifier()
    results = pipeline.run()

    print("Predictions:")
    for text, label in results:
        print(f"Text: '{text}' → Predicted: {label}")
