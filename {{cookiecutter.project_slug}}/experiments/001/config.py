import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

EXP_NAME = "001"


# ---------- # DIRECTORIES # ---------- #
IS_KAGGLE_ENV = os.environ["KAGGLE_DATA_PROXY_TOKEN"] is not None
KAGGLE_COMPETITION_NAME = os.getenv("KAGGLE_COMPETITION_NAME", "equity-post-HCT-survival-predictions")
KAGGLE_USERNAME = os.environ["KAGGLE_USERNAME"]

if not IS_KAGGLE_ENV:
    import rootutils

    ROOT_DIR = rootutils.setup_root(
        ".",
        indicator="pyproject.toml",
        cwd=True,
        pythonpath=True,
    )
    INPUT_DIR = ROOT_DIR / "data" / "input"
    # Assumes access via RTIFACT_DIR / EXP_NAME / 1
    ARTIFACT_DIR = ROOT_DIR / "data" / "output"
    # The output destination of the code. Add 1 to match the path of the kaggle code.
    OUTPUT_DIR = ARTIFACT_DIR / EXP_NAME / "1"

    ARTIFACTS_HANDLE = f"{KAGGLE_USERNAME}/{KAGGLE_COMPETITION_NAME}-artifacts/other/{EXP_NAME}"
    CODES_HANDLE = f"{KAGGLE_USERNAME}/{KAGGLE_COMPETITION_NAME}-codes"
else:
    ROOT_DIR = Path("/kaggle/working")
    INPUT_DIR = Path("/kaggle/input")
    # The location where artifacts other than the code are stored (can be used as a model) can be accessed at ARTIFACT_DIR / EXP_NAME / 1
    ARTIFACT_DIR = INPUT_DIR / f"{KAGGLE_COMPETITION_NAME.lower()}-artifacts" / "other"
    OUTPUT_DIR = ROOT_DIR  # The output destination of the code

COMP_DATASET_DIR = INPUT_DIR / KAGGLE_COMPETITION_NAME

for d in [INPUT_DIR, OUTPUT_DIR]:
    d.mkdir(exist_ok=True, parents=True)

ARTIFACT_EXP_DIR = lambda exp_name=EXP_NAME: ARTIFACT_DIR / exp_name / "1"  # noqa # Returns the location where the artifact of the target exp is stored
