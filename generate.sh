#!/bin/bash

openapi-generator generate -g python \
    -i https://raw.githubusercontent.com/chajath/classics-proxy/master/openapi/itkc_api.yaml \
    -p packageName=classics_proxy_client,packageVersion=0.0.1,packageUrl=https://github.com/chajath/classics-proxy-client,projectName=classics-proxy-client \
    --git-user-id chajath \
    --git-repo-id classics-proxy-client