# USAGE: make <command>
# Example: make cover
# It will run the unit tests and report the testing coverage's code


# Terminal Colors
Color_Off=\033[0m
Black=\033[1;30m
Red=\033[1;31m
Green=\033[1;32m
Yellow=\033[1;33m

# Use guard for make commands that have required arguments
guard-%:
	@ if [ "${${*}}" = "" ]; then \
		echo "Informe a variável \"$*\" "; \
		exit 1; \
	fi

clean:
	find . -type d -name __pycache__ -exec rm -r {} \+

# =================================================================
# TESTING
# =================================================================

collect-tests:
	pytest --collect-only

cover:
	coverage run --source=src/ -m pytest -vv tests/ && coverage report -m

test-verbose-with-print:
	pytest -svv tests/

cover-html:
	coverage html

delete-local-branch: guard-name
	git branch -D ${name}

delete-remote-origin-branch: guard-name
	git push origin --delete ${name}

# =================================================================
# GITFLOW SUGESTIONS
# =================================================================

new-feature: guard-name
	git checkout -b feature/${name} dev
	git pull origin dev
	git push -u origin feature/${name}
	git branch

new-hotfix: guard-name
	git checkout -b hotfix/${name} master
	git pull origin master
	git branch

new-release: guard-name
	git checkout -b release/${name} dev
	git pull origin dev
	git push -u origin release/${name}
	git branch

new-release-by-current-branch: guard-name
	git checkout -b release/${name} $(git symbolic-ref --short HEAD)
	git push -u origin release/${name}
	git branch

new-tag: guard-name guard-text
	git checkout master
	git pull origin master
	git tag -a ${name} -m"${text}" master 
	git push origin ${name}
	git tag

solve-conflict: guard-destiny guard-working
	git checkout -b conflict/${destiny}-${working} ${destiny}
	git push -u origin conflict/${destiny}-${working}
	git pull origin ${working}
	git branch

# =================================================================
# Installation, configuration and running
# =================================================================

install:
	echo -e "${Green}🐍🐍 Installing Python 3.11.1 🐍🐍${Color_Off}";
	pyenv install 3.11.1;
	echo -e "${Green}⏯️⏯️ Activating local environment ⏯️⏯️${Color_Off}";
	pyenv local 3.11.1;
	echo -e "${Green}📜📜 Installing poetry with pyenv version 📜📜${Color_Off}";
	pip3 install poetry;
	echo -e "${Green}🚸🚸 Installing dependencies 🚸🚸${Color_Off}";
	poetry install;
	echo -e "${Green}🐚🐚 Spawning poetry shell 🐚🐚${Color_Off}";
	poetry shell;
	echo -e "${Green}✨✨ All Done ✨✨${Color_Off}";

run: guard-arg
	poetry run notas-musicais ${arg}