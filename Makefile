.PHONY: setup lab build check
setup:   ## create .venv and install everything
	uv sync
lab:     ## open JupyterLab
	uv run jupyter lab
build:   ## regenerate practice/solution notebooks from dayN/*.py
	uv run python tools/build_notebooks.py
check:   ## run snippets + execute every solution notebook + confirm practice checks start red
	./run_all.sh && uv run python tools/check_notebooks.py
