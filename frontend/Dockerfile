FROM node:20-bullseye

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY src ./src
COPY vite.config.ts ./vite.config.ts

EXPOSE 3000
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "3000"]
