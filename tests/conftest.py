import shutil
import sys
from pathlib import Path

import pytest
from cookiecutter import main

CCDS_ROOT = Path(__file__).parents[1].resolve()

args = {
    "project_name": "DrivenData",
    "author_name": "DrivenData",
    "author_email": "fixture@pytest.com",
    "open_source_license": "BSD-3-Clause",
}


def system_check(basename):
    if "linux" in sys.platform:
        basename = basename.lower()
    return basename


@pytest.fixture(scope="class", params=[{}, args])
def default_baked_project(tmpdir_factory, request):
    temp = tmpdir_factory.mktemp("data-project")
    out_dir = Path(temp).resolve()

    main.cookiecutter(
        str(CCDS_ROOT), no_input=True, extra_context=request.param, output_dir=out_dir
    )

    request.cls.project_input = request.param.get("project_name")

    pn = request.param.get("project_name") or "project_name"
    # project name gets converted to lower case on Linux but not Mac
    pn = system_check(pn)
    proj = out_dir / pn
    request.cls.path = proj
    yield

    # cleanup after
    shutil.rmtree(out_dir)
