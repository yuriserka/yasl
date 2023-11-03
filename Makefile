.PHONY: run, create-env, install-requirements

run:
	@python3 src/main.py

create-env: install-requirements
	@echo "Creating virtual environment..."
	@python3 -m venv .venv
	@echo "Virtual environment created."

install-requirements:
	@echo "Installing requirements..."
	@pip3 install -r requirements.txt
	@echo "Requirements installed."
