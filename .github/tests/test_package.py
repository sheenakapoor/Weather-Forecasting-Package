"""GitHub Actions tests."""
import os
import subprocess


def test_src_dir():
    """Check that src directory exists."""
    assert os.path.exists("src")


def test_pkg_dir():
    """Check that package directory exists."""
    assert os.path.exists("src/weatherfc")


def test_setup():
    """Check that setup script exists."""
    assert os.path.exists("src/setup.py")


def test_license():
    """Check that license exists."""
    assert os.path.exists("src/LICENSE")
    with open("src/LICENSE", encoding="utf-8") as fname:
        assert len(fname.read().strip()) > 0


def test_init():
    """Check that __init__.py exists."""
    assert os.path.exists("src/weatherfc/__init__.py")


def test_bin():
    """Check that executable script in bin exists."""
    assert os.path.exists("src/weatherfc/bin/wfc.py")


def test_package_install():
    """Check that package is installable."""
    assert 0 == os.system("pip install src/")


def test_package():
    """Check that file in package gets executed."""
    path = "/root/work/project-sheenakapoor/src/weatherfc/bin/wfc.py"
    subprocess.run(
        ["python", path, "15232"],
        capture_output=True,
        check=True,
    ).stdout.decode()


def test_egginfo():
    """Check that egginfo file exists."""
    assert os.path.isdir("src/weather.egg-info")


def test_makefile():
    """Check that makefile file exists."""
    assert os.path.exists("makefile")


def test_precommit_yml():
    """Make sure .pre-commit-config.yaml was made."""
    assert os.path.exists(".pre-commit-config.yaml")
