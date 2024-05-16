REPO="$(basename $PWD)"
VENV="venv_$REPO"
if [ ! -d "$VENV" ]; then
    echo "Creating venv in $PWD/$VENV/"
    python3 -m venv $VENV
fi
export PYTHONPATH=$PWD
source $VENV/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
# This line won't work unless ipykernel is in requirements.txt
python3 -m ipykernel install --user --name="$VENV" --display-name="$REPO"