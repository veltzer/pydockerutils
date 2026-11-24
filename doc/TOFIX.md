# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `src/pydockerutils/main.py:11-16` - the package does nothing: its only endpoint is a placeholder `test` ("test description") whose body is `pass`, yet version 0.0.6 is published on PyPI with "Development Status :: 4 - Beta" (`pyproject.toml:24`). Implement the utilities listed in `doc/TODO.txt:2-8` (`docker_bash`, `docker_containers_rm_all`, `docker_images_rm_none`, `docker_kill_all`, `docker_connect`, `docker_images_rm_all`, `docker_kill_all_and_remove`) and remove the `test` endpoint, or mark the project as "1 - Planning" until it has content.

## Medium

- `.pyre_configuration:1-8` - stale config for the pyre type checker, which nothing in the build runs; it hardcodes absolute paths into a hatch-era `.venv/default/` that does not exist and uses `"source_directories": ["."]`. Delete it (mypy already covers type checking).

## Low

- `src/pydockerutils/utils.py` - empty file, and `src/pydockerutils/configs.py:1-3` holds only a docstring; delete them or fill them when the endpoints above are implemented.
- `rsconstruct.toml:28,32` - ruff and mypy list `config` in `src_dirs`, but `config/` holds only Lua files; drop it so the dirs are precise.
- `README.md` - generated README has no usage section (no `tera.snippets/main.md.tera`); add one once there are real endpoints.
