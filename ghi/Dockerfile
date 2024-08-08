FROM node:18-alpine3.20

WORKDIR /app

COPY package*.json ./

RUN npm install --force

COPY . .

EXPOSE 5173

ENV HOST=0.0.0.0
ENV PORT=5173

CMD ["npm", "run", "dev", "--", "--host"]
