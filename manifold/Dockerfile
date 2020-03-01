FROM node:latest

WORKDIR /app

RUN git clone https://github.com/uber/manifold.git

WORKDIR /app/manifold

RUN yarn && \
    cd /app/manifold/examples/manifold && \
    yarn

WORKDIR /app/manifold/examples/manifold

ENV MAPBOX_ACCESS_TOKEN=pk.eyJ1IjoiZ2F1dGFtYm9yZzEyMyIsImEiOiJjazc5MXZvem0wMDFlM2ZudjU5eWVlbDIyIn0.BchpTuaxZlIfAM16z2h4Qw

COPY package.json .

CMD npm run start