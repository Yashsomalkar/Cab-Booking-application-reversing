

# Uber & Rapido API Reverse Engineering

This repository documents the reverse engineering of Uber's POST request and Rapido's protobuf structure. The project involves analyzing API interactions to uncover hidden parameters, and request structures, and improve understanding of how these services handle OTP authentication and session flows.

## Overview

### 1. **Uber POST Request Analysis**
   - Reversed Uber’s OTP request during the login process.
   - Focused on `POST /rt/silk-screen/submit-form` API interactions.
   - Captured detailed request headers and payloads, including device-specific information and session identifiers.
   - Explored device metadata and session management through Uber’s API, such as:
     - `X-Uber-Device-Udid`, `X-Uber-Request-Uuid`, `X-Uber-Client-Version`
   - Reconstructed OTP flows to simulate the app's verification mechanism.

### 2. **Rapido Protobuf Reverse Engineering**
   - Analyzed and reversed Rapido’s protobuf messages for API communication.
   - Decoded the serialized protobuf structures to understand the transport layer data.
   - Investigated how protobuf handles user information, authentication, and ride details.

## Purpose

The purpose of this project is to:
   - Explore API behaviors in popular ride-hailing apps.
   - Improve understanding of authentication mechanisms, including OTP handling.
   - Gain insight into API security and how device-related information is passed through requests.
   - Enable further research into enhancing API security and privacy.

