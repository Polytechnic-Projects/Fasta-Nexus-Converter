# 🧬 Fasta to Nexus Converter - Simple Format Transformation Tool
This project is a Python script that converts DNA sequence data from FASTA format into the NEXUS format. Uses a simple CLI interface and basic unit tests written with pytest. 

---

### 👩‍🔬 Authors

A group of 4 students from ESTBarreiro with their school ID numbers assigned.

- Bianca Silva, 202300273  
- Erica Alaiz, 202300154  
- Filipa Fernandes, 202300218  
- Melissa Rocha, 202101023

---

### 📋 Index

- [📝 Introduction](#-introduction)
- [⚙️ Features](#-features)
- [💻 Installation](#-installation)
- [🚀 Usage](#-usage)
- [📜 License](#-license)  

---

## 📝 Introduction

The Fasta to Nexus Converter was created as part of a bioinformatics course to assist in formatting sequence data for downstream phylogenetic analysis. This utility takes a `.fasta` file and outputs a properly structured `.nex` (NEXUS) file, with support for DNA sequences, missing data handling, and basic cleanup.

---

## ⚙️ Features

- 📖 Converts FASTA-formatted sequences into valid NEXUS format  
- 🔡 Handles lowercase 'n' characters by replacing them with 'N'  
- 📊 Automatically calculates and includes NTAX and NCHAR  
- 🧪 Includes test coverage for all core functions using `pytest`  
- 🖥️ CLI-based tool for easy terminal use  

---

## 💻 Installation

### Prerequisites

- Python 3.7+
- `pytest`

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Polytechnic-Projects/Fasta-Nexus-Converter.git
   cd Fasta-Nexus-Converter

2. Install dependencies:
   ```bash
   pip install pytest

---

## 🚀 Usage

Run the script from the command line, providing a FASTA file as input:

  ```bash
  python3 fasta_nexus_converter.py your_sequences.fasta > output.nex
  ```

### For testing:

```bash
python3 -m pytest unit_tests.py
```

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
