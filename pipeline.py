import subprocess

def install_requirements():
    print("Installing requirements...")
    subprocess.run(["pip", "install", "-r", "requirements.txt"])

def run_tests():
    print("Running tests with Pytest...")
    subprocess.run(["pytest"])

def lint_code():
    print("Linting code with Flake8...")
    subprocess.run(["flake8", "."])

if __name__ == "__main__":
    install_requirements()
    run_tests()
    lint_code()
