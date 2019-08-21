# CE BLOG

CE Personal blog

## Getting Started

```
git clone --recurse-submodules https://github.com/escrichov/blog
pipenv install
pipenv run make devserver
```

Open [http://localhost:8000](http://localhost:8000) 

### Prerequisites

Install pipenv

```
pip install pipenv
```

### Installing

Install python dependencies

```
git clone --recurse-submodules https://github.com/escrichov/blog
pipenv install
```

Install netlify

```
npm install netlify-cli -g
netlify login
```

Run devserver

```
pipenv run make devserver
```


## Deployment

Deployment is configured to automatically deploy blog when you push to github.

If you need to deploy manually you need to run this command:
```
netlify deploy
```

## Built With

* [Pelican](https://github.com/getpelican/pelican) - The static site generator used
* [Pelican Plugins](https://github.com/getpelican/pelican-plugins) - Pelican plugins
* [Pelican Flex Theme](https://github.com/alexandrevicenzi/Flex) - Pelican theme used

