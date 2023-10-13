# SecureText - Python Encryption and Decryption Tool

SecureText is a Python-based desktop application designed to provide a simple and secure way to encrypt and decrypt text data. The tool uses a user-defined password to encrypt the text and allows users to decrypt it later using the same password. This README provides an overview of the project, its features, usage instructions, and other important information.

## Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Usage](#usage)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

1. **User-Friendly Interface**: The application provides a user-friendly graphical user interface (GUI) that allows users to interact with the tool seamlessly.

2. **Text Encryption**: Users can input the text they want to protect into the application. The tool uses a password provided by the user to encrypt the text securely.

3. **Text Decryption**: When users want to access their encrypted text, they can use the same password to decrypt it.

4. **Password Protection**: The tool enforces password protection to ensure that only authorized individuals can decrypt and access the content.

5. **Data Privacy**: All text data is encrypted using a strong encryption algorithm, such as base64, to ensure data privacy and security.

6. **Reset and Clear**: Users have the option to reset the password and clear the input fields to start a new encryption process.

## Technology Stack

- **Python**: The core programming language used for application development.
- **Tkinter**: The Python library for creating the graphical user interface.
- **Base64 Encryption**: The base64 encoding/decoding technique is used for text encryption and decryption.

## Usage

1. Launch the application.
2. Enter the text you want to encrypt.
3. Set a password for encryption.
4. Click the "ENCRYPT" button to encrypt the text.
5. The encrypted text is displayed on the screen.
6. To decrypt, enter the password used for encryption.
7. Click the "DECRYPT" button to reveal the original text.

## Installation

There is no specific installation process required for this tool. You need to have Python installed on your system.

## How to Run

1. Clone this repository to your local machine or download the source code as a ZIP file.
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Run the following command to start the application:

```bash
python main.py
