FROM rapid7/insightconnect-python-3-38-plugin:5
LABEL organization=rapid7
LABEL sdk=python
LABEL type=plugin

ENV SSL_CERT_FILE /etc/ssl/certs/ca-certificates.crt
ENV SSL_CERT_DIR /etc/ssl/certs
ENV REQUESTS_CA_BUNDLE  /etc/ssl/certs/ca-certificates.crt

RUN apt-get update && apt-get install -y pandoc texlive lmodern --no-install-recommends

ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src

WORKDIR /python/src
# Add any package dependencies here

# End package dependencies
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
RUN python setup.py build && python setup.py install

# needed for SSL
USER root

ENTRYPOINT ["/usr/local/bin/icon_html"]