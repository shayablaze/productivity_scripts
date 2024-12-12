docker build . -t prox_thing2
docker run -it -e HTTP_PROXY=http://localhost:4444: -e HTTPS_PROXY=http://localhost:4444 -e REQUESTS_CA_BUNDLE=/root/.mitmproxy/mitmproxy-ca-cert.pem prox_thing2