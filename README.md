![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![Spark](https://img.shields.io/badge/Spark-Streaming-orange)
![Kafka](https://img.shields.io/badge/Kafka-Realtime-black)

#  Real-Time Analytics Pipeline (Kafka → Spark Streaming)

**Why I built this project ?**

I didn’t build this project just to “ use **Kafka** and **Spark**”.

I built it because real-world data doesn’t wait.

Transactions, clicks, payments, and events are constantly flowing and i wanted to understand what really happens from the moment an event is created to the moment it is processed and analyzed in real time.

So I decided to build the whole pipeline myself, end to end.


# :lotus_position: You can see the Full Project via Figma (easier) ! 
Click this link to view the Project ->  https://www.figma.com/make/v0DRrtrvwKEjx9iA1PZjNa/Confetti-Explosion-on-Click?p=f&t=avk3mMhhpyjcGvNg-0&fullscreen=1





---

## Architecture Overview

```
Producer (Python)
      ↓
   Kafka Topic (transactions)
      ↓
Spark Structured Streaming
      ↓
 Console Output / (Next: Parquet, MinIO, Dashboard)
```

---

## Tech Stack

* **Python 3.10+**
* **Apache Kafka** (event streaming)
* **Apache Spark 3.5.1** (Structured Streaming)
* **Docker & Docker Compose**
* **Zookeeper** (Kafka dependency)

---

## 📁 Project Structure

```
realtime-analytics-pipeline/
│
├── producer/
│   ├── Dockerfile
│   └── producer.py          # Kafka producer (simulated transactions)
│
├── spark/
│   ├── docker-compose.yml   # Kafka + Spark cluster
│   └── streaming_test.py    # Spark Structured Streaming job
│
├── data/                    # (future) persisted streaming outputs
├── dashboard/               # (future) Streamlit dashboard
└── README.md
```

---

## Data Flow

Each event represents a transaction:

```json
{
  "transaction_id": "24236",
  "amount": 472.32,
  "city": "Nice",
  "timestamp": 1765741726.39
}
```

Flow:

1. Python producer sends events to Kafka
2. Spark reads Kafka topic in real time
3. JSON is parsed with an explicit schema
4. Data is streamed to the console (live)

---

## ▶️ How to Run the Project

### 1️⃣ Start Kafka & Spark Cluster

```bash
docker compose -f spark/docker-compose.yml up -d
```

Verify:

* Spark Master UI → [http://localhost:8080](http://localhost:8080)
* Spark Worker UI → [http://localhost:8081](http://localhost:8081)

---

### 2️⃣ Create Kafka Topic

```bash
docker exec -it kafka kafka-topics \
  --bootstrap-server kafka:9092 \
  --create \
  --topic transactions \
  --partitions 1 \
  --replication-factor 1
```

---

### 3️⃣ Start the Kafka Producer

```bash
docker compose -f spark/docker-compose.yml up -d --build producer
```

Check producer logs:

```bash
docker logs -f producer
```

---

### 4️⃣ Run Spark Streaming Job

```bash
docker exec -it spark-master \
  /opt/spark/bin/spark-submit \
  --master spark://spark-master:7077 \
  /opt/spark/work-dir/streaming_test.py
```

You should see **live streaming data** in the terminal.

---

## 📊 Spark UI

* Spark Master: [http://localhost:8080](http://localhost:8080)
* Spark Worker: [http://localhost:8081](http://localhost:8081)

You can observe:

* Running applications
* Executors
* Memory & CPU usage

---

## 🧠 Key Concepts Demonstrated

* Event-driven architecture
* Kafka topics & producers
* Spark Structured Streaming
* JSON schema enforcement
* Dockerized data platforms
* Real-time processing semantics

---

## 🚧 Next Improvements (Roadmap)

* ⏱ Windowed aggregations (KPIs per minute)
* 💾 Persist streaming output to Parquet / MinIO
* 📈 Streamlit real-time dashboard
* ☁️ Cloud deployment (AWS / GCP)
* 🧪 Data quality checks

---

## 🎯 Why This Project Matters

This project reflects **real-world data engineering pipelines** used in:

* FinTech
* E-commerce
* IoT & event analytics

It demonstrates practical skills expected from a **Data Engineer / AI Engineer intern**.

---

## 👤 Author

**Wassim Elmoufakkir**
MSc Data Engineering for Artificial Intelligence


---

⭐ If you find this project useful, feel free to star the repository!

