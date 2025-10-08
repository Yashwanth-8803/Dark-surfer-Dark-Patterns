#!/bin/bash

# Test valid tokens including new dark pattern types
curl -X POST http://localhost:5000/ -H "Content-Type: application/json" -d '{"tokens": ["limited offer", "hidden fee", "subscribe now", "urgent action required"]}'

echo -e "\n"

# Test empty tokens array
curl -X POST http://localhost:5000/ -H "Content-Type: application/json" -d '{"tokens": []}'

echo -e "\n"

# Test missing tokens key
curl -X POST http://localhost:5000/ -H "Content-Type: application/json" -d '{}'

echo -e "\n"

# Test invalid JSON
curl -X POST http://localhost:5000/ -H "Content-Type: application/json" -d '{"tokens": ["valid", "test"'

echo -e "\n"

# Test GET request (should return friendly message)
curl -X GET http://localhost:5000/
