FROM golang:1.16-alpine as builder

# create and change into the webscraping directory
WORKDIR /webscraping

# get dependencies for the app
# this lets the container reuse cached dependencies
# expecting to copy go mod and if a go sum exists then that too
COPY go.* ./
RUN go mod download

# copy the local code into the container image
COPY . ./

# build the binaries 
# not sure about this bit, something like:
RUN go build 
# TODO fix above

# move onto another image for production
# we copy accross all the go code from the above container
# FROM alpine:3.13.2
# etc
# TODO
# add more stuff here
CMD ["go", "run", "main.go"]
# returns csv in container, we need to get it out
# set up a volume that is accessable by both containers
# volume = directory
# docker compose volume
# volume represents something in my machine vs the containers
# mount the volume in neural-net