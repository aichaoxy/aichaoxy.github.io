This is a pelican blog repository consisting of raw markdown files. Thanks to pelican, site generation is quite handy. The static content
is hosted on Cloudflare.

* I use pdm to manage the local env.
```
pdm init
pdm add "pelican[markdown]"
```
* If you prefer pip over pdm.
```
# export the dependencies eligible to pip
pdm export -o requirements.txt
pip install -r requirements.txt
```
* Preview the website with autoreload
```
pelican -r -l
```
* Generate the site
```
# default output dir is `output`
pelican 
```