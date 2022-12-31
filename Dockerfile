FROM python:3.10

# Create this directory in the image at the root of the file system, then go inside
WORKDIR /Lil-Buddy-App

# Copy these files into the folder.
COPY requirements.txt .
COPY .env .

RUN pip install -r requirements.txt

# Copy app contents into /Lil-Buddy-App/Lil-Buddy
COPY ./Lil-Buddy ./Lil-Buddy

#Command to run the bot
CMD ["python3", "./Lil-Buddy/"]
