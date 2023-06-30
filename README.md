# DotaNotes
Software to add notes about dota players encountered in matchmaking.

# User Setup
TODO `.exe` for noobs

# Developer Setup
In `src` do -
## Unix

```
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python 
```

## Windows

```
python -m venv .wenv
.\.wenv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
"$(get-location)" > .\.wenv\Lib\site-packages\obugs.pth
python main.py
```
