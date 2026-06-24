# Stage 1: Build the application using Maven
FROM maven:3.8.8-eclipse-temurin-17 AS build
WORKDIR /app

# Copy the source code and pom.xml from your repository
COPY . .

# Run the maven build to generate the JAR file inside the container
RUN mvn clean package -DskipTests

# Stage 2: Create the lightweight runtime container
FROM eclipse-temurin:17-jdk-alpine
VOLUME /tmp

# Copy the built JAR file from the first stage (adjust target name if needed)
COPY --from=build /app/target/political-sim-backend-0.0.1-SNAPSHOT.jar app.jar

ENTRYPOINT ["java","-jar","/app.jar"]
EXPOSE 7810