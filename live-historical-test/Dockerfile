# Start from a Node.js ready container
FROM node:latest
# Network port number
EXPOSE 3000
# Set working directory in the container
WORKDIR /home
# Clone the Linked Connections server and download all static, live and historical data
RUN git clone https://github.com/linkedconnections/linked-connections-server.git lc-server; \
    cd lc-server; git checkout swj-evaluation; npm install; \
    cd ..; wget -O live-data.zip https://cloud.ilabt.imec.be/index.php/s/2TjYTXGGoi8Le2B/download \
    && unzip live-data.zip; rm live-data.zip; \
    wget -O lc-data.zip https://cloud.ilabt.imec.be/index.php/s/mp283ioeigpf8qq/download \
    && unzip lc-data.zip; rm lc-data.zip; \
    mkdir live-publish 
# Copy Fake live data web server
COPY live-publish/index.js ./live-publish/
# Copy LC-Server config files
COPY datasets_config.json server_config.json ./lc-server/
# Copy start script
COPY run.sh .
# Setup container's entrypoint script
RUN chmod +x run.sh 
ENTRYPOINT [ "./run.sh" ]