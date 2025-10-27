FROM node:20-bookworm-slim

WORKDIR /app

ENV ROLLUP_SKIP_NODEJS_NATIVE=true

COPY package.json ./
# COPY package-lock.json ./
COPY package.json package-lock.json* yarn.lock* ./

RUN npm install --no-fund --no-audit --legacy-peer-deps

COPY . . 

EXPOSE 5173
CMD ["npm", "run", "dev", "--", "--host"]