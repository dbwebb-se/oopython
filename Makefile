#!/usr/bin/make -f
#
# Makefile for course repos
#

# Colors
NO_COLOR=\033[0m
TARGET_COLOR=\033[32;01m
OK_COLOR=\033[32;01m
ERROR_COLOR=\033[31;01m
WARN_COLOR=\033[33;01m
ACTION=$(TARGET_COLOR)--> 

# Add local bin path for test tools
PATH := "$(PWD)/build/bin:$(PWD)/build/node_modules/.bin:$(PATH)"



# target: help          - Displays help.
.PHONY:  help
help:
	@echo "Displaying help for this Makefile."
	@echo "Usage:"
	@echo " make [target] ..."
	@echo "target:"
	@egrep "^# target:" Makefile | sed 's/# target: / /g'



# target: clean         - Remove all generated files.
.PHONY:  clean
clean:
	@echo "$(ACTION)Remove all generated files$(NO_COLOR)"
	rm -rf build/
	rm -f npm-debug.log



# target: clean-all     - Remove all installed files.
.PHONY:  clean-all
clean-all: clean
	@echo "$(ACTION)Remove all installed files$(NO_COLOR)"



# target: build-prepare - Prepare the build directory.
.PHONY: build-prepare
build-prepare:
	@echo "$(ACTION)Prepare the build directory$(NO_COLOR)"
	install -d build/bin
	install .package.json build/package.json



# target: dbwebb-validate-install - Download and install dbwebb-validate.
.PHONY: dbwebb-validate-install
dbwebb-validate-install: build-prepare
	@echo "$(ACTION)Download and install dbwebb-validate$(NO_COLOR)"
	wget --quiet -O build/bin/dbwebb-validate https://raw.githubusercontent.com/mosbth/dbwebb-cli/master/dbwebb2-validate
	chmod 755 build/bin/dbwebb-validate



# target: dbwebb-validate-check   - Check version and environment for dbwebb-validate.
.PHONY: dbwebb-validate-check
dbwebb-validate-check:
	@echo "$(ACTION)Check version and environment for dbwebb-validate$(NO_COLOR)"
	export PATH=$(PATH) && dbwebb-validate --version && dbwebb-validate --check



# target: dbwebb-validate-run     - Run tests with dbwebb-validate.
.PHONY: dbwebb-validate-run
dbwebb-validate-run:
	@echo "$(ACTION)Run tests with dbwebb-validate$(NO_COLOR)"
	export PATH=$(PATH) && dbwebb-validate --publish --publish-to build/webroot/ example



# target: npm-install-dev - Install npm packages for development.
.PHONY: npm-install-dev
npm-install-dev: build-prepare
	@echo "$(ACTION)Install npm packages for development$(NO_COLOR)"
	npm install --only=dev --prefix build



# target: npm-update-dev  - Update npm packages for development.
.PHONY: npm-update-dev
npm-update-dev:
	@echo "$(ACTION)Update npm packages for development$(NO_COLOR)"
	npm update --only=dev --prefix build



# target: automated-tests-prepare - Prepare for automated tests.
.PHONY: automated-tests-prepare
automated-tests-prepare: build-prepare dbwebb-validate-install npm-install-dev
	@echo "$(ACTION)Prepared for automated tests$(NO_COLOR)"



# target: automated-tests-check   - Check version and enviroment for automated tests.
.PHONY: automated-tests-check
automated-tests-check: dbwebb-validate-check
	@echo "$(ACTION)Checked version and environment for automated tests$(NO_COLOR)"



# target: automated-tests-run     - Run all automated tests.
.PHONY: automated-tests-run
automated-tests-run: dbwebb-validate-run
	@echo "$(ACTION)Executed all automated tests$(NO_COLOR)"
