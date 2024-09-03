import subprocess
import sys
import os
from pathlib import Path

def create_virtual_environment(venv_name=".venv"):
    """
    Function to create a virtual environment using the venv module.
    
    Args:
        venv_name (str): The name of the virtual environment directory.
    """
    try:
        subprocess.check_call([sys.executable, "-m", "venv", venv_name])
        print(f"Virtual environment '{venv_name}' created successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to create virtual environment '{venv_name}'.")

def activate_virtual_environment(venv_name=".venv"):
    """
    Function to activate the virtual environment.
    
    Args:
        venv_name (str): The name of the virtual environment directory.
    """
    activate_script = Path(venv_name) / ("Scripts" if os.name == "nt" else "bin") / "activate"
    if activate_script.exists():
        print(f"To activate the virtual environment, run: \nsource {activate_script}")
    else:
        print(f"Activation script not found for virtual environment '{venv_name}'.")

def install_package(package, venv_name=".venv"):
    """
    Function to install a Python package using pip in the virtual environment.
    
    Args:
        package (str): The name of the package to install.
        venv_name (str): The name of the virtual environment directory.
    """
    pip_executable = Path(venv_name) / ("Scripts" if os.name == "nt" else "bin") / "pip"
    try:
        subprocess.check_call([str(pip_executable), "install", package])
        print(f"Successfully installed {package}")
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}")

def save_requirements(venv_name=".venv", file_name="requirements.txt"):
    """
    Function to save the installed packages to a requirements.txt file in the virtual environment.
    
    Args:
        venv_name (str): The name of the virtual environment directory.
        file_name (str): The name of the file to save the requirements.
    """
    pip_executable = Path(venv_name) / ("Scripts" if os.name == "nt" else "bin") / "pip"
    try:
        with open(file_name, 'w') as f:
            subprocess.check_call([str(pip_executable), "freeze"], stdout=f)
        print(f"Requirements saved to {file_name}")
    except subprocess.CalledProcessError:
        print("Failed to save requirements to file.")

def generate_gitignore(file_name=".gitignore"):
    """
    Function to generate a .gitignore file with specified lines.
    
    Args:
        file_name (str): The name of the .gitignore file.
    """
    gitignore_content = [ ".venv/"]

    try:
        with open(file_name, 'w') as f:
            for line in gitignore_content:
                f.write(line + "\n")
        print(f".gitignore file created with content: {gitignore_content}")
    except Exception as e:
        print(f"Failed to create .gitignore file: {e}")

def main():
    # Define the virtual environment name
    venv_name = ".venv"

    # List of packages to install
    packages = ['pandas', 
                'numpy', 
                'matplotlib', 
                # 'yfinance', 
                # 'mplfinance', 
                # 'scikit-learn'
                 ]

    # Create and activate the virtual environment
    # create_virtual_environment(venv_name)
    activate_virtual_environment(venv_name)

    # Generate .gitignore file
    generate_gitignore()

    # Loop through the list of packages and install each one in the virtual environment
    for package in packages:
        install_package(package, venv_name)
    
    # Save installed packages to requirements.txt
    save_requirements(venv_name)

if __name__ == "__main__":
    main()