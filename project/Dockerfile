FROM python:2.7
LABEL maintainer="Imran Mirza"

# Copy local code to the container image.
WORKDIR /app
COPY  techtrends ./
EXPOSE 3111
# Install production dependencies.
RUN pip install -r requirements.txt
RUN python init_db.py
CMD [ "python", "app.py" ]
