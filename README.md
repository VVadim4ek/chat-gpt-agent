# OpenAI GPT Agent With Memory Microservice

## Overview

This project aims to build a Conversational Agent with a memory microservice using OpenAI's GPT-3.5 and FastAPI. The agent is designed to overcome the limitations of traditional chatbot implementations by retaining context during conversations. This is particularly useful in microservice architectures and container orchestration systems like Kubernetes, where services frequently restart, update, and scale.

## Table of Contents

1. [Introduction](#introduction)
2. [Motivation](#motivation)
3. [Technologies](#technologies)
4. [Getting Started](#getting-started)
5. [Usage](#usage)
6. [Acknowledgments](#acknowledgments)

## Introduction

Conversational Agents are increasingly becoming essential in various applications like customer support, virtual assistants, and information retrieval systems. However, most traditional chatbots lack the ability to maintain context in ongoing conversations, leading to a disjointed and frustrating user experience. This project aims to solve this problem by adding a memory microservice to the conversational agent.

## Motivation

The project is motivated by the need to improve the capabilities of conversational agents, especially in complex environments like Kubernetes. In such systems, microservices are often subject to frequent restarts, updates, and scaling operations. These events can disrupt the state of ongoing conversations in traditional chatbot implementations. By adding a memory microservice, this project aims to preserve the state of conversations, allowing for more natural and continuous interactions.

## Technologies

- **OpenAI GPT-3.5**: Used for natural language processing tasks, including text generation, conversation management, and context retention. You will need to generate an OpenAI API Key for this.
- **FastAPI**: Serves as the backbone of the microservice, handling HTTP requests, managing conversation states, and integrating with the OpenAI API.

## Getting Started

1. Clone the GitHub repository
2. Install the required packages using `pip install -r requirements.txt`
3. Generate your OpenAI API Key and add it to the configuration
4. Run the FastAPI server

## Usage

Once the server is up and running, you can interact with the conversational agent through HTTP requests. The memory microservice will ensure that the context of the conversation is maintained even if the microservice restarts or updates.

## Acknowledgments

Special thanks to Cesar Flores and Towards Data Science for the original tutorial and inspiration for this project. I have made many modifications and additions to the original code, but the core idea remains the same.
