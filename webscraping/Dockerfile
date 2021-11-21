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

FROM alpine:3.13.2