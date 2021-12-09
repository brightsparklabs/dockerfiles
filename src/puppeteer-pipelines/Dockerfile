FROM node:14.16.0-alpine

RUN apt-get update \
 && apt-get install -y \
    libgconf-2-4 \
    wget \
 && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
 && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
    fonts-ipafont-gothic \
    fonts-kacst \
    fonts-thai-tlwg \
    fonts-wqy-zenhei \
    google-chrome-unstable \
    ttf-freefont \
 && rm -rf /var/lib/apt/lists/* \
 && apt-get purge --auto-remove -y curl \
 && rm -rf /src/*.deb