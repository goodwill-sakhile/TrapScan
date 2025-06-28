# api/schema.py

from typing import Tuple

# For now, we're only working with string label + float confidence score
PredictionResult = Tuple[str, float]
