FROM node:20-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

# Run Vite dev server in host mode for docker-compose
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
