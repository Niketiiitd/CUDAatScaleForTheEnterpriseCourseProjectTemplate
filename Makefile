# Define the default target
.DEFAULT_GOAL := all

# Define the Python executable
PYTHON := python

# Define the pip executable
PIP := pip

# Define the requirements file
REQUIREMENTS := requirements.txt

# Define the scripts
EXTRACT_SCRIPT := extract.py
MAIN_SCRIPT := scripts/main.py

# Directories
DATA_DIR := data
TEXTURES_DIR := $(DATA_DIR)/initial/textures
AERIALS_DIR := $(DATA_DIR)/initial/aerials

# URLs
TEXTURES_URL := https://sipi.usc.edu/database/textures.tar.gz
AERIALS_URL := https://sipi.usc.edu/database/aerials.tar.gz

# Files
TEXTURES_TAR := $(TEXTURES_DIR).tar.gz
AERIALS_TAR := $(AERIALS_DIR).tar.gz

# Default target: download data, run extract.py, install requirements, and run main.py
all: download-data extract install-requirements run-main

# Download data
download-data: $(TEXTURES_DIR) $(AERIALS_DIR)

$(TEXTURES_DIR):
	mkdir -p $(TEXTURES_DIR)
	curl -o $(TEXTURES_TAR) $(TEXTURES_URL)
	tar -xzf $(TEXTURES_TAR) -C $(TEXTURES_DIR)
	rm $(TEXTURES_TAR)

$(AERIALS_DIR):
	mkdir -p $(AERIALS_DIR)
	curl -o $(AERIALS_TAR) $(AERIALS_URL)
	tar -xzf $(AERIALS_TAR) -C $(AERIALS_DIR)
	rm $(AERIALS_TAR)

# Run extract.py
extract:
	$(PYTHON) $(EXTRACT_SCRIPT)

# Install required packages
install-requirements:
	$(PIP) install -r $(REQUIREMENTS)

# Run main.py
run-main:
	$(PYTHON) $(MAIN_SCRIPT)

# Clean target (optional): cleans up any generated files if needed
clean:
	@echo "Nothing to clean"

# Phony targets to avoid conflicts with files of the same name
.PHONY: all download-data extract install-requirements run-main clean
