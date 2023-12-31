### Useful link for installing pyenv: https://www.dedicatedcore.com/blog/install-pyenv-ubuntu/
sudo apt update
sudo apt install -y git vim
sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git
curl https://pyenv.run | bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc
exec "$SHELL"
#pyenv install --list
pyenv install 3.8.3
pyenv versions
ls ~/.pyenv/versions/
pyenv global 3.8.3
python -m test
#pyenv global system ### K: Revert to global installation.
#python -V


pyenv virtualenv 3.8.3 mestrado
echo 'Run in the repository directory: "pyenv local mestrado"'
echo 'Proceed with the installation: "pip install -r requirements"'
echo 'Run the Flower base script to verify if the installation was successful'
