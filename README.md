# Sample Function: Reddit API

Simple example showing how to interact with the Reddit API from a DigitalOcean
Function. This example installs a Python dependency called `praw` to work with
the Reddit API.

This example shows:

* Adding a Python library dependency
* Passing secrets through environment variables

## Setup doctl

Follow the [DigitalOcean installation instructions](https://docs.digitalocean.com/reference/doctl/how-to/install/).

Something like:

```sh
doctl auth init --context default
doctl serverless connect
```

## Deploy Function

Clone the repository:

```sh
git clone https://github.com/kevinms/sample-functions-python-reddit.git
```

Configure Reddit API secrets:

```sh
cd sample-functions-python-reddit
cp .env.template .env
# Edit the .env to contain your Reddit API secrets.
```

Deploy function (must run outside of the repository):

```sh
doctl serverless deploy sample-functions-python-reddit --remote-build
doctl serverless functions invoke "reddit/hot"
```

## References

DigitalOcean's example python project: [sample-functions-python-jokes](https://github.com/digitalocean/sample-functions-python-jokes)
