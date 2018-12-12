
# uMap project

[![Requirements Status](https://requires.io/github/umap-project/umap/requirements.svg?branch=master)](https://requires.io/github/umap-project/umap/requirements/?branch=master)
[![Join the chat at https://gitter.im/umap-project/umap](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/umap-project/umap?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) [![Documentation Status](https://readthedocs.org/projects/umap-project/badge/?version=latest)](http://umap-project.readthedocs.io/en/latest/?badge=latest)[![Build Status](https://travis-ci.org/umap-project/umap.svg?branch=master)](https://travis-ci.org/umap-project/umap)

## About

uMap lets you create maps with OpenStreetMap layers in a minute and embed them in your site.
*Because we think that the more OSM will be used, the more OSM will be ''cured''.*
It uses [django-leaflet-storage](https://github.com/umap-project/django-leaflet-storage) and [Leaflet.Storage](https://github.com/umap-project/Leaflet.Storage),  built on top of Django and Leaflet.


## Installation and configuration

See [developer documentation](https://umap-project.readthedocs.io/en/latest/install/).


### Co jsem udělal já:

nainstalovat GEOS, PROJ.4 a GDAL a podle https://docs.djangoproject.com/en/2.1/ref/contrib/gis/install/geolibs/#geosbuild
to je nadlouho tak dělat ve druhém terminálu a během kompilací udělat zbytek


#### nasazení
víceméně podle tohodle návodu, semtam se musí udělat něco jinak https://umap-project.readthedocs.io/en/latest/ubuntu/

```
sudo apt install python3.5 python3.5-dev python-virtualenv wget nginx uwsgi uwsgi-plugin-python3 postgresql postgis git certbot sudo
mkdir -p /srv/umap
mkdir -p /etc/umap
adduser --home /srv/umap umap
usermod -aG sudo umap
su - umap
sudo chown umap:users /etc/umap

# popř. sudo chown umap:users /srv/umap # pokud se vytvořilo home directory při přidání uživatele

# pak je potřeba to samé udělat pro media folder, ale asi by šlo rekurzivně pro celou /srv/umap

# klasicky
pip install umap

# nase
pip install git+https://github.com/EndevelCZ/umap
```

### nastaveni
#### klasicky
`wget https://raw.githubusercontent.com/umap-project/umap/master/umap/settings/local.py.sample -O /etc/umap/umap.conf`
a upravit dle upravit setingy podle https://umap-project.readthedocs.io/en/latest/install/ nebo v duchu conf_examples/local.py

#### nase
zkopirovat z gitu conf_examples/local.py do `/etc/umap/umap.conf`

####DB
podle https://docs.djangoproject.com/en/2.1/ref/contrib/gis/install/postgis/

```
sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable
sudo apt-get u
sudo apt-get install postgis

su - postgres (nebo sudo -i -u postgres)

createdb umap
psql umap
CREATE EXTENSION postgis;
CREATE EXTENSION postgis_topology;

\q

psql
CREATE USER umap PASSWORD 'd5Q}W9{Jbm/(aD{v'; 		# nebo fSA3TzPb

# Povolit připojení na DB uživateli
GRANT CONNECT
ON DATABASE umap 
TO umap;


# Nastavit permissions na všechny tabulky (v public schema)
\c umap;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO umap;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO umap;
```

#### devel


pokud instalováno z local gitu

```
pip install .

make isntalljs
make vendors


umap collectstatic
umap compress
umap migrate

```


# FAQ
ERROR při migraci s geosem - https://stackoverflow.com/a/18721622/7113416

umap collectstatic # vyhazuje nějaký error o Leafletu v /home/ybon/... - ale rozjede se to i bez toho

důležité - pip balíček obsahuje bugy - nejlepší přepsat vše potřebné v něm, hlavně local settings
všechny přepsané věci pro p. Doležala stažené v srv.tar.gz v Dropboxu v projektu umap (do něj si forknout umap a upravovat vše tam, stejně tak leaflet storage asi)



