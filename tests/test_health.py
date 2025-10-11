"""
Basic health test for the Storm Events Analysis project.
Ensures the environment and folder structure are valid.
"""

import os
import importlib
import pytest

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def test_environment_structure():
    """Verify that expected key directories exist."""
    expected_dirs = [
        "data/raw",
        "data/interim",
        "data/processed",
        "notebooks",
        "models/artifacts",
        "reports/figures",
    ]
    for d in expected_dirs:
        assert os.path.isdir(os.path.join(PROJECT_ROOT, d)), f"Missing directory: {d}"

def test_src_imports():
    """Confirm that helper modules in src can be imported."""
    modules = ["io_utils", "clean_utils", "fe_utils", "viz_utils"]
    for mod in modules:
        try:
            importlib.import_module(f"src.{mod}")
        except Exception as e:
            pytest.fail(f"Import failed for src.{mod}: {e}")

def test_readme_present():
    """Ensure a main README.md file exists."""
    readme_path = os.path.join(PROJECT_ROOT, "README.md")
    assert os.path.exists(readme_path), "README.md not found in project root"
