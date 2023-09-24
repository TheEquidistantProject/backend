![Equidistant Project Logo](logo_banner.png)

Welcome to the Backend repository of The Equidistant Project. This repository houses the code and resources for the backend part of our mission to combat misinformation and bias in the news sphere. Our goal is to provide a scalable and efficient platform for storing and serving factual news articles.

## Table of Contents
- [Project Overview](#project-overview)
- [Technology Stack](#technology-stack)
- [Backend Architecture](#backend-architecture)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The Equidistant Project stands as a beacon against the tide of misinformation and bias prevalent in the news sphere. Our mission is to provide users with access to unbiased news articles crafted from a diverse range of sources. This backend repository is a critical component of our platform.

### Technology Stack

Our backend is built using the following technologies and services:

- **MongoDB Atlas**: MongoDB Atlas is our chosen cloud-based database service for storing and managing our generated articles. It provides scalability, reliability, and ease of use.

- **Algolia**: Algolia powers our search functionality, allowing users to perform fuzzy searches and find relevant articles quickly.

- **FastAPI**: FastAPI serves as the web framework for handling HTTP requests. It offers high performance and is designed for building APIs quickly and efficiently.

- **Uvicorn**: Uvicorn is the ASGI server used to serve FastAPI applications. It ensures high concurrency and can handle a large number of requests.

- **Cloudflare Workers**: Cloudflare Workers provide a scalable and distributed execution environment. They enable our backend to be highly available and performant on an international scale.

### Backend Architecture

Our backend architecture is designed for scalability and performance:

- **MongoDB Atlas**: MongoDB Atlas hosts our database, ensuring that it can handle large volumes of articles and serve them efficiently.

- **Algolia**: Algolia's fuzzy search capabilities make it easy for users to find articles matching their interests.

- **FastAPI**: FastAPI handles incoming HTTP requests, including article retrieval and search queries.

- **Uvicorn**: Uvicorn serves the FastAPI application and manages concurrent connections effectively.

- **Cloudflare Workers**: Cloudflare Workers provide an additional layer of scalability and performance. They ensure that our backend can handle requests from users around the world.

### Features

Our backend offers the following key features:

- **Efficient Article Storage**: MongoDB Atlas efficiently stores and manages our database of generated articles.

- **Fuzzy Search**: Algolia's fuzzy search allows users to find articles even when their search terms are not an exact match.

- **API Endpoints**: FastAPI provides well-defined API endpoints for retrieving articles and conducting searches.

- **Scalability**: Cloudflare Workers ensure that our backend can scale on an international level, providing a responsive experience to users worldwide.

## Getting Started

To get started with the Equidistant Project Backend repository, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/YourUsername/Equidistant-Backend.git
   ```

2. Install the required dependencies and configure the backend settings, including MongoDB Atlas and Algolia credentials.

3. Deploy the backend using Uvicorn and ensure that it is accessible via the specified API endpoints.


## License

This project is licensed under the [MIT License](LICENSE).

---

