###########################
# This is a "builder" pattern in Docker.
# We need to process our React code into
# static files that we can serve (npm run build).
# You could also skip this part and just run 
# "npm run build" and copy over the output manually
# like some kind of barbarian
########################### 

FROM node:lts-alpine as builder

RUN apk add --no-cache openssl
RUN apk add --no-cache --repository=http://dl-cdn.alpinelinux.org/alpine/edge/main \
    libcrypto1.1 \
    libssl1.1

WORKDIR /frontend

# These two lines will allow us to pass in an environment
# variable when the image is *built* (not run).  For local
# development, localhost; for production, your EC2's IP address
ARG REACT_APP_BASE_URL=localhost
ENV REACT_APP_BASE_URL=$REACT_APP_BASE_URL

COPY ./frontend/package.json .
RUN npm install
COPY ./frontend .
RUN npm run build

###########################
# This is the final image we want.
#  First, it copies over a config file which basically says:
# "if any requests come in whose uri starts with /api/,
# then hand them off to the gunicorn (Django) server, 
# otherwise, serve up the React static files."
# Second, it copies over the React static files to the place
# where nginx expects them to be.
###########################
FROM nginx:alpine

COPY ./webserver/default.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /frontend/build /usr/share/nginx/html