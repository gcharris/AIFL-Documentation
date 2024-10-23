# install_deps.py
import subprocess
import sys

def install_dependencies():
    """Install required packages"""
    packages = [
        'flask==2.2.2',
        'python-dotenv==0.19.0',
        'lark-parser==0.11.3',
        'cffi==1.15.1',
        'cryptography==3.4.7',
        'openai>=1.0.0',
        'requests>=2.26.0',
        'pytest>=7.0.0',
        'watchdog>=2.1.9'
    ]

    print("Installing dependencies...")
    for package in packages:
        print(f"Installing {package}...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            print(f"Successfully installed {package}")
        except subprocess.CalledProcessError as e:
            print(f"Error installing {package}: {e}")
            return False
    return True

if __name__ == "__main__":
    success = install_dependencies()
    if success:
        print("\nAll dependencies installed successfully!")
    else:
        print("\nSome dependencies failed to install. Please check the errors above.")