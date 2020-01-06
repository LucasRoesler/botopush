# botopush OpenFaaS Example

Very minimal example of useing the `boto3` Python package and the `python3-http` template.

This will accept an arbtrary payload and save it to an S3 bucket

## Build
Just use the `faas-cli`
```sh
faas-cli build --tag=describe
```

## Deploy
This requires an the AWS credentials to be created as a secret. First, create a text file called `botopush-aws` so that it looks like this

```txt
[default]
aws_access_key_id=<value>
aws_secret_access_key=<value>
```

Make sure that these credentials have access to the required bucket and update the stack file, replacing `botopush-example`.

Then use the faas-cli to deploy the secret:
```sh
faas-cli secret create -n beta botopush-aws --from-file `pwd`/botopush-aws
```

Once the secret is deployed, you can deploy the function using

```sh
faas-cli deploy
```
