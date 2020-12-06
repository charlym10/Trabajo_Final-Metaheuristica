import os

def main():

    # Ejecutar test
    os.system('coverage run -m unittest discover -v')

    # Coverage report
    os.system('coverage report --omit=env/*')
    os.system('coverage html --omit=env/*')
    os.system('python -m http.server --bind 127.0.0.1 --directory ./htmlcov')

if __name__ == "__main__":
    main()