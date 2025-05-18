import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    """Install dependencies, run checks and build a wheel."""
    req_file = ROOT / "requirements.txt"
    subprocess.check_call([
        sys.executable,
        "-m",
        "pip",
        "install",
        "-r",
        str(req_file),
    ])

    subprocess.check_call([sys.executable, "-m", "flake8", str(ROOT)])
    subprocess.check_call([sys.executable, "-m", "pytest", str(ROOT / "tests")])
    subprocess.check_call([sys.executable, "-m", "build"], cwd=str(ROOT))


if __name__ == "__main__":
    main()
