# Stage 1: Build using Maven
FROM maven:3.8.8-eclipse-temurin-17 AS build
WORKDIR /app

# Since Render is now starting inside the /backend folder,
# COPY . . will copy everything inside /backend into the container
COPY . .

RUN mvn clean package -DskipTests

# Stage 2: Tiny lightweight runtime
FROM eclipse-temurin:17-jdk-alpine
VOLUME /tmp

# The jar file is generated inside target/ (not backend/target/)
COPY --from=build /app/target/political-sim-backend-0.0.1-SNAPSHOT.jar app.jar

ENTRYPOINT ["java","-jar","/app.jar"]
EXPOSE 7810