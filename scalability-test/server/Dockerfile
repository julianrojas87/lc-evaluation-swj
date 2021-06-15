# Start from Java-ready container
FROM openjdk:11.0.11-9-jdk-buster
# Create a new directory for app files
RUN mkdir -p /opt/otp
# Set working directory in the container
WORKDIR /opt/otp
# Download OTP binary
RUN wget https://cloud.ilabt.imec.be/index.php/s/GXDJW87NZYFaQyp/download/otp-2.1.0-SNAPSHOT-shaded.jar
# Copy OTP
COPY router-config.json build-config.json run.sh ./
# Install osmium to filter OSM road networks
RUN apt-get update && apt-get install -y osmium-tool
# Expose HTTP default port
EXPOSE 8080
# Setup container's entrypoint script
RUN chmod +x run.sh 
ENTRYPOINT [ "./run.sh" ]