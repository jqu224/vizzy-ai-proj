from pathlib import Path
import sys


CHALLENGE_ROOT = Path(__file__).resolve().parents[1]

if str(CHALLENGE_ROOT) not in sys.path:
    sys.path.insert(0, str(CHALLENGE_ROOT))
