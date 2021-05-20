THIS_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
.PHONY: regen docs help
.DEFAULT_GOAL := help
PYTHON="3.7 3.8 3.9"

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/pypi_oldest_requirements.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ pypi_oldest_requirements
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

regen_%:
		docker build --build-arg PYTHON=$* \
			-t local/test_pypi_oldest_requirements:$* .
		docker run -v $(THIS_DIR):/src local/test_pypi_oldest_requirements:$*

REGEN = $(addprefix regen_,$(PYTHONS))
regen: $(REGEN)
