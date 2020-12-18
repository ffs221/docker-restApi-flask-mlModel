# docker-restApi-flask-mlModel
The model used to predict the outcome comes from this challenge:

https://www.kaggle.com/c/santander-product-recommendation/discussion/25579

Credit to BreakFast Pirate and SRK for the model and service functions.

This project simply extract the model (filename: modal.save) and using the machine learning modal to create a REST API using flask framework and dockerize the project for easy migration.

To run this project simply build the docker image:

docker build . -t {your file name}

and run docker:

docker run -d -p 5000:5000 {your file name}

Server is ready to use on your localhost:5000

Feel free to contact me for any question.
