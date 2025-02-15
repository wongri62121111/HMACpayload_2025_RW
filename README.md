# Python HMAC Payload Sender and Receiver

This project demonstrates how to use HMAC (Hash-based Message Authentication Code) to securely send a payload from a sender application (`appSend`) to a receiver application (`appRecv`). The payload includes a message and its HMAC, which ensures the integrity and authenticity of the message.

---

## Table of Contents
1. [Overview](#overview)
2. [How It Works](#how-it-works)
3. [Code Explanation](#code-explanation)
4. [Usage](#usage)
5. [Dependencies](#dependencies)
6. [License](#license)

---

## Overview

HMAC is a cryptographic technique used to verify the integrity and authenticity of a message. This project:
- Computes an HMAC for a given message using a secret key.
- Sends the message and its HMAC as a payload from `appSend` to `appRecv`.
- Verifies the HMAC in `appRecv` to ensure the message has not been tampered with.

---

## How It Works

1. **Sender (`appSend`)**:
   - Takes a message and a secret key as input.
   - Computes the HMAC for the message using the secret key.
   - Creates a payload containing the message and its HMAC.
   - Sends the payload to the receiver.

2. **Receiver (`appRecv`)**:
   - Receives the payload containing the message and its HMAC.
   - Recomputes the HMAC for the received message using the same secret key.
   - Compares the recomputed HMAC with the received HMAC.
   - If they match, the message is authentic; otherwise, it is considered tampered.

---

## Code Explanation

### 1. `compute_hmac(message: str, secret_key: str) -> str`
- **Purpose**: Computes the HMAC for a given message using a secret key.
- **Steps**:
  1. Uses the SHA-256 hash algorithm.
  2. Computes the HMAC using the `hmac` library.
  3. Encodes the HMAC digest in Base64 for easy transmission.

### 2. `create_payload(message: str, secret_key: str) -> Dict[str, Any]`
- **Purpose**: Creates a payload containing the message and its HMAC.
- **Steps**:
  1. Calls `compute_hmac` to generate the HMAC for the message.
  2. Constructs a dictionary with the message and HMAC.

### 3. `send_payload(payload: Dict[str, Any]) -> None`
- **Purpose**: Simulates sending the payload to the receiver.
- **Steps**:
  1. Prints the payload to the console (simulates sending over a network).

### 4. `verify_payload(payload: Dict[str, Any], secret_key: str) -> bool`
- **Purpose**: Verifies the integrity of the received payload.
- **Steps**:
  1. Extracts the message and HMAC from the payload.
  2. Recomputes the HMAC for the received message.
  3. Compares the recomputed HMAC with the received HMAC using `hmac.compare_digest`.

### 5. `app_send(message: str, secret_key: str) -> None`
- **Purpose**: Simulates the sender application.
- **Steps**:
  1. Calls `create_payload` to generate the payload.
  2. Calls `send_payload` to send the payload.

### 6. `app_recv(payload: Dict[str, Any], secret_key: str) -> None`
- **Purpose**: Simulates the receiver application.
- **Steps**:
  1. Calls `verify_payload` to check the integrity of the payload.
  2. Prints whether the message is authentic or tampered.

### 7. `main() -> None`
- **Purpose**: Demonstrates the workflow of sending and receiving a payload.
- **Steps**:
  1. Defines a message and secret key.
  2. Calls `app_send` to send the payload.
  3. Simulates receiving the payload and calls `app_recv` to verify it.

---

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/python-hmac-example.git
   cd python-hmac-example
   ```

2. Run the script:
   ```bash
   python hmac_example.py
   ```

3. Output Example:
   ```
   Sending payload to appRecv...
   {
     "message": "Hello, HMAC!",
     "hmac": "3e9b8f8a9c8f8a9c8f8a9c8f8a9c8f8a9c8f8a9c8f8a9c8f8a9c8f8a9c8f8a"
   }
   Receiving payload in appRecv...
   HMAC verification successful. Message is authentic.
   Received message: Hello, HMAC!
   ```

---

## Dependencies

- Python 3.x
- Standard Python libraries:
  - `hmac`
  - `hashlib`
  - `base64`
  - `json`

No additional packages are required.