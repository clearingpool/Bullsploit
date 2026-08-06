FROM python:3.13-alpine
RUN apk add --no-cache go git bash
WORKDIR /app
COPY go.mod ./
RUN go mod download
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN chmod +x BullsploitFramework.py Setup.sh hashchecker.sh
ENTRYPOINT ["python3", "BullsploitFramework.py"]
