# use an official Python runtime as a parent image
FROM python:3.6.2

# set the working directory to /usr/app
WORKDIR /usr/app

# copy the current directory contents into the container at /usr/app
COPY ./ ./

# install any needed dependencies specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# make port 80 available to the world outside the container
EXPOSE 80

# run app.py when the container launches
CMD [ "python", "app.py" ]
