FROM node:18

# Set working directory
WORKDIR /app

# Install dependencies
COPY package.json package-lock.json* ./
RUN npm install

# Copy the rest of the code
COPY . .

# Build the project
RUN npm run build

# Start the app
CMD ["npm", "start"]
