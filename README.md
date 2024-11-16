# Inter-Django app communication using Kafka PoC

This repository contains an example of data model syncing between two separate django apps, facilitated by Kafka.

The system is composed of two Django apps: **Main** and **Other**. The Main Django app is where users will be created.
The Other Django app will receive this information via Kafka and synchronize with the Main Django app.

## Requirements
- Make
- Docker

## Getting started
- `make run` will start the application
    - the Main Django app will be running on http://localhost:8000
    - the Other Django app will be running on http://localhost:8500
- `make m` and `make m-other` will run migrations in the Main Django app and the Other Django app respectively.
    - Similarly `make createsuperuser` and `make createsuperuser-other` will let you create superusers for each respective app
- run `./bin/setup-kafka.sh` to initialize the Kafka topic that the apps will use
- Run the kafka consumer on the Other app with make django-consumer
- Sign into the Main Django app and navigate to http://localhost:8000/api/users/v1/users/. Create a new user via POST request
    - You can check the Kafka Producer Logs here: http://localhost:8000/admin/kafka/kafkaproducerlog/
- At this point the Kafka consumer will have picked up on the user event produced by the Main app and will have created the corresponding user on the Other app
    - you can check it in the admin here: http://localhost:8500/admin/users/externaluser/
    - You can also check the Kafka Consumer Logs here: http://localhost:8500/admin/kafka/kafkaconsumerlog/
