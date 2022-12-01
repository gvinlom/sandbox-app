FROM node:lts-alpine as build-step
WORKDIR /app

COPY ./public /public
COPY ./src /src
COPY ./package.json ./

RUN npm install
RUN npm run build

FROM caddy:alpine
EXPOSE 80
EXPOSE 443
COPY --from=build-step /app/build /usr/share/caddy