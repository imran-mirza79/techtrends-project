FROM python:3.8
LABEL maintainer="Imran Mirza"

# Copy local code to the container image.
COPY  . /app
WORKDIR /app
EXPOSE 3111
# Install production dependencies.
RUN pip install -r requirements.txt
RUN python init_db.py
CMD [ "python", "app.py" ]