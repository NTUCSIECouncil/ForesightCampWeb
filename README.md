# CSIE Foresight Camp Challenge Webpage
---

## Installation

```shell
# Step 1 : Clone the repo
git clone git@github.com:vppyw/ForesightCampWeb.git
# Step 2 : Setup python ( you may skip this step if the environment is set up )
sudo apt-get install python3-pip
python3 -m pip install -U pip
# Step 3 : Install Django and channels
pip3 install -r requirements.txt
```

## Usage

1. Start the server

   ```shell
   docker run -p 6379:6379 -d redis:5
   ./manage.py runserver <ip or domain-name>:<port> --insecure
   ```

2. Management
	
	Log in the backstage as administrator and revise flag

	Be sure to change adminstration's password before start it !!!
    ```shell
    ./manager.py changepassword admin
    ```

### Acknowledgement

This repository is originally forked from [Tenyoku's foresight_camp_ctf repository](https://github.com/Tenyoku8478/foresight_camp_ctf) and [NTUCSIECouncil/ForesightCampWeb](https://github.com/NTUCSIECouncil/ForesightCampWeb)

### References

Django (https://docs.djangoproject.com/en/3.2/)

Channels (https://channels.readthedocs.io/en/stable/index.html)
