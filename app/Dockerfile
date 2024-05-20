#
FROM python:3 AS builder
COPY requirements.txt .

RUN pip install --user -r requirements.txt

#
FROM python:3-slim
WORKDIR /opt/pidor_bot

COPY --from=builder /root/.local /root/.local
COPY ./main.py .
COPY ./repositories repositories
COPY ./routers routers
COPY ./services services
COPY ./utils utils

ENV PATH=/root/.local:$PATH

# CMD [ "python", "main.py" ]
# CMD [ "python", "-c", "import time; time.sleep(322)" ]
