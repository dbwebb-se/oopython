#!/usr/bin/make -f
#
# Makefile for course repos
#

# Colors
NO_COLOR		= \033[0m
TARGET_COLOR	= \033[32;01m
OK_COLOR		= \033[32;01m
ERROR_COLOR		= \033[31;01m
WARN_COLOR		= \033[33;01m
ACTION			= $(TARGET_COLOR)--> 
HELPTEXT 		= "$(ACTION)" `egrep "^\# target: $(1) " Makefile | sed "s/\# target: $(1)[ ]\+- / /g"` "$(NO_COLOR)"

# Add local bin path for test tools
PATH := "$(PWD)/bin:$(PWD)/vendor/bin:$(PWD)/node_modules/.bin:$(PATH)"



# target: help                    - Displays help.
.PHONY:  help
help:
	@echo $(call HELPTEXT,$@)
	@echo "Usage:"
	@echo " make [target] ..."
	@echo "target:"
	@egrep "^# target:" Makefile | sed 's/# target: / /g'



# target: install                 - Install needed utilities locally.
.PHONY: install
install: automated-tests-prepare
	@echo $(call HELPTEXT,$@)



# target: check                   - Check installed utilities.
.PHONY: check
check: automated-tests-check
	@echo $(call HELPTEXT,$@)




# target: test                    - Install test tools & run tests.
.PHONY: test
test: automated-tests-prepare automated-tests-check automated-tests-run dbwebb-testrepo
	@echo $(call HELPTEXT,$@)



# target: build-prepare           - Prepare the build directory.
.PHONY: build-prepare
build-prepare:
	@echo $(call HELPTEXT,$@)
	install -d build
	install -d bin/pip



# target: clean                   - Remove all generated files.
.PHONY:  clean
clean:
	@echo $(call HELPTEXT,$@)
	rm -rf build
	rm -f npm-debug.log



# target: clean-me                - Remove me-directory.
.PHONY:  clean-me
clean-me:
	@echo $(call HELPTEXT,$@)
	rm -rf me



# target: clean-all               - Remove all installed files.
.PHONY:  clean-all
clean-all: clean
	@echo $(call HELPTEXT,$@)
	rm -rf bin
	rm -rf node_modules
	rm -rf vendor



# target: dbwebb-install          - Download and install dbwebb-cli.
.PHONY: dbwebb-install
dbwebb-install: build-prepare
	@echo $(call HELPTEXT,$@)
	wget --quiet -O bin/dbwebb https://raw.githubusercontent.com/mosbth/dbwebb-cli/master/dbwebb2
	chmod 755 bin/dbwebb
	export PATH=$(PATH) && dbwebb config create noinput && dbwebb --version



# target: dbwebb-testrepo         - Test course repo.
.PHONY: dbwebb-testrepo
dbwebb-testrepo: dbwebb-install
	@echo $(call HELPTEXT,$@)
	export PATH=$(PATH) && dbwebb --silent --local testrepo



# target: dbwebb-validate-install - Download and install dbwebb-validate.
.PHONY: dbwebb-validate-install
dbwebb-validate-install: build-prepare
	@echo $(call HELPTEXT,$@)
	wget --quiet -O bin/dbwebb-validate https://raw.githubusercontent.com/mosbth/dbwebb-cli/master/dbwebb2-validate
	chmod 755 bin/dbwebb-validate
	export PATH=$(PATH) && dbwebb-validate --version



# target: dbwebb-validate-check   - Check version and environment for dbwebb-validate.
.PHONY: dbwebb-validate-check
dbwebb-validate-check:
	@echo $(call HELPTEXT,$@)
	export PATH=$(PATH) && dbwebb-validate --version && dbwebb-validate --check



# target: dbwebb-validate-run     - Run tests with dbwebb-validate.
.PHONY: dbwebb-validate-run
dbwebb-validate-run:
	@echo $(call HELPTEXT,$@)
	export PATH=$(PATH) && dbwebb-validate --publish --publish-to build/webroot/ example



# target: npm-install-dev         - Install npm packages for development.
.PHONY: npm-install-dev
npm-install-dev: build-prepare
	@echo $(call HELPTEXT,$@)
	if [ -f package.json ]; then npm install --only=dev; fi



# target: npm-update-dev          - Update npm packages for development.
.PHONY: npm-update-dev
npm-update-dev:
	@echo $(call HELPTEXT,$@)
	if [ -f package.json ]; then npm update --only=dev; fi



# target: composer-install-dev    - Install composer packages for development.
.PHONY: composer-install-dev
composer-install-dev: build-prepare
	@echo $(call HELPTEXT,$@)
	if [ -f composer.json ]; then composer install; fi



# target: composer-update-dev     - Update composer packages for development.
.PHONY: composer-update-dev
composer-update-dev:
	@echo $(call HELPTEXT,$@)
	if [ -f composer.json ]; composer update; fi



# target: tools-install-dev       - Install tools for development.
.PHONY: tools-install-dev
tools-install-dev: build-prepare composer-install-dev npm-install-dev
	@echo $(call HELPTEXT,$@)



# target: tools-update-dev        - Update tools for development.
.PHONY: tools-update-dev
tools-update-dev: composer-update-dev npm-update-dev
	@echo $(call HELPTEXT,$@)



# target: automated-tests-prepare - Prepare for automated tests.
.PHONY: automated-tests-prepare
automated-tests-prepare: build-prepare dbwebb-validate-install dbwebb-install npm-install-dev composer-install-dev
	@echo $(call HELPTEXT,$@)



# target: automated-tests-check   - Check version and environment for automated tests.
.PHONY: automated-tests-check
automated-tests-check: dbwebb-validate-check
	@echo $(call HELPTEXT,$@)



# target: automated-tests-run     - Run all automated tests.
.PHONY: automated-tests-run
automated-tests-run: dbwebb-validate-run dbwebb-testrepo
	@echo $(call HELPTEXT,$@)


# target: dbwebb-validate         - Execute dbwebb validate with arg1=what.
.PHONY: dbwebb-validate
dbwebb-validate:
	@echo $(call HELPTEXT,$@)
	bin/dbwebb-validate --publish --publish-to build/webroot/ $(arg1)
