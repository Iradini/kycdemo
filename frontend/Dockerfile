FROM node:20-alpine
WORKDIR /app
COPY package.json package-lock.json* yarn.lock* ./
RUN npm ci || npm install
COPY . . 
ExPOSE 5173
CMD ["npm", "run", "dev", "--", "--host"]