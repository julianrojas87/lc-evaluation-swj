FROM node:latest
RUN mkdir /opt/app
WORKDIR /opt/app
COPY . .
RUN npm install
RUN chmod +x run.sh 
ENTRYPOINT [ "./run.sh" ]