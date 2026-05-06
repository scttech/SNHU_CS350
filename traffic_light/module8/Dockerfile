# Use the official nginx image built on Alpine Linux (small footprint)
FROM nginx:alpine

# Copy our web content into the nginx default web root
COPY html/ /usr/share/nginx/html/

# Expose port 80 so the host can reach the web server
EXPOSE 80
