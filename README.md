<div align="center">
  <h1 align="center">Bullsploit Framework</h1>
</div>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.13-blue" />
  <img src="https://img.shields.io/badge/go-lang-blue" />
  <img src="https://img.shields.io/badge/Bullsploit-Framework-red" />
  <img src="https://img.shields.io/badge/Ast-Parse-yellow" />
</p>


<img width="1188" height="393" alt="photo_2026-04-25_15-35-52" src="https://github.com/user-attachments/assets/41f8e638-69f9-4de2-87f8-243017fbee36" />



BullSploit is a modular, high-performance penetration testing framework designed for automated network reconnaissance and security research. The framework provides a robust environment for developing, managing, and executing security-centric modules. More detailed information about the framework can be found on the website https://bullsploit.ru/framework

### 🏗 Technical Architecture

The framework is built upon a modular micro-kernel design, prioritizing scalability and runtime stability.

•  Dynamic Module Introspection: Implements importlib for runtime dependency injection and module management.

•  AST-based Validation: Utilizes the Abstract Syntax Tree (AST) library for pre-execution syntax verification, ensuring core stability against malformed module code.

•  Concurrency Engine: Optimized for I/O-bound tasks using the threading library, supporting high-concurrency network operations (3000+ threads).

•  Unified Argument Parser: A specialized parameter management system providing strict type validation for user-defined inputs.

•  


### 📂 Module Classification

Functional units are categorized into four distinct domains:

### • Payloads:
 Payload for initial machine compromise and system persistence.

 
### • Post:
 Post-exploitation payload for various types of interaction on the machine after its initial compromise.


### • Auxiliary:
 Auxiliary modules of various types, such as reconnaissance tools, scanners, search engines, and others


### • builder:
 Module builders (specifically payload builders) that assemble/compile modules to make them ready for deployment

## 🛠 Installation & Deployment

The framework requires an isolated Python environment. An automated deployment script is provided for Linux-based systems.

## Automated Setup
### Clone the repository
```
git clone https://github.com/clearingpool/BullSploit.git
```

### Execute the deployment script
```
chmod +x Setup.sh
```
```
./Setup.sh
```

### Manual Launch
```
./BullsploitFramework.py
```

## ⚖️ Legal Disclaimer

This software is intended for authorized security auditing and educational purposes only. The developer assumes no liability for misuse or illicit activity. Unauthorized access to computer systems is illegal and strictly prohibited.

## 📝 Information

•   Lead Developer: Rapid
•   Language: Python 3.13
•   License: [MIT](LICENSE)
