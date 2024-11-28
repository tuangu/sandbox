# sandbox

# west
This sandbox use [west](https://github.com/zephyrproject-rtos/west) tool from the Zephyr RTOS to manage multiple repositories.

Initialize and update with external repos:
```
# optional: create and activate virtual env
python -m venv .venv
bash$ source .venv/bin/activate
# or
pwsh$ .venv/bin/Activate.ps1

# install west
pip install west

# initialize from existing manifest
west init -l --mf west.yml

# update repos
west update
```