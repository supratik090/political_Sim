# syntax=docker/dockerfile:1.4

# ---------- Builder stage ----------
# Use a Maven image with a recent version and JDK 17.
# The cache mount speeds up repeated builds by persisting the Maven repository.
FROM maven:3.9.6-eclipse-temurin-17 AS builder
WORKDIR /src

# Copy only the pom.xml first to leverage Docker layer caching for dependencies.
COPY pom.xml .
# Download dependencies (including plugins) without compiling the code.
RUN mvn -B dependency:go-offline

# Now copy the source code and build the JAR.
COPY src ./src
RUN mvn -B -DskipTests clean package

# ---------- Runtime stage ----------
# Use a minimal JDK distribution (Alpine) for the final image.
FROM eclipse-temurin:17-jdk-alpine
VOLUME /tmp

# Copy the built JAR from the builder stage.
COPY --from=builder /src/target/political-sim-backend-0.0.1-SNAPSHOT.jar /app.jar

# Expose default HTTP port
EXPOSE 8080

# Set Java heap memory (256MB heap leaves ~256MB for JVM metaspace/native RAM in a 512MB container)
ENV JAVA_OPTS="-Xms64m -Xmx256m"

# Run the application.
ENTRYPOINT ["sh", "-c", "java $JAVA_OPTS -jar /app.jar"]