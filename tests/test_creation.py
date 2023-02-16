import os
from subprocess import check_output

import pytest
from conftest import system_check


def no_curlies(filepath):
    """Utility to make sure no curly braces appear in a file.
    That is, was Jinja able to render everything?
    """
    with open(filepath, "r") as f:
        data = f.read()

    template_strings = ["{{", "}}", "{%", "%}"]

    template_strings_in_file = [s in data for s in template_strings]
    return not any(template_strings_in_file)


@pytest.mark.usefixtures("default_baked_project")
class TestCookieSetup:
    @property
    def proj_name(self):
        if self.project_input:
            name = system_check("DrivenData")
        else:
            name = "project_name"
        return name

    def test_project_name(self):
        project = self.path
        assert project.name == self.proj_name

    def test_readme(self):
        readme_path = self.path / "README.md"
        assert readme_path.exists()
        assert no_curlies(readme_path)
        if self.proj_name == "DrivenData":
            with open(readme_path) as fin:
                assert "DrivenData" == next(fin).strip()

    def test_pyproject(self):
        working_dir = os.getcwd()
        try:
            os.chdir(self.path)
            args = ["poetry", "version"]
            p = check_output(args).decode("ascii").strip()
            assert p == f"{self.proj_name.replace('_', '-')} 0.1.0"

            args = ["poetry", "check"]
            p = check_output(args).decode("ascii").strip()
            assert p == "All set!"
        finally:
            os.chdir(working_dir)

    def test_license(self):
        license_path = self.path / "LICENSE"
        assert license_path.exists()
        assert no_curlies(license_path)

    def test_makefile(self):
        makefile_path = self.path / "Makefile"
        assert makefile_path.exists()
        assert no_curlies(makefile_path)

    def test_folders(self):
        expected_dirs = [
            "data",
            "data/external",
            "data/interim",
            "data/processed",
            "data/raw",
            "docs",
            "notebooks",
            "src",
            f"src/{self.proj_name}",
            f"src/{self.proj_name}/data",
            f"src/{self.proj_name}/features",
            f"src/{self.proj_name}/models",
            "tests",
        ]

        ignored_dirs = [str(self.path)]

        abs_expected_dirs = [str(self.path / d) for d in expected_dirs]
        abs_dirs, _, _ = list(zip(*os.walk(self.path)))
        assert len(set(abs_expected_dirs + ignored_dirs) - set(abs_dirs)) == 0
