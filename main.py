import hmac
import hashlib
import base64
import json
from typing import Dict, Any

def compute_hmac(message: str, secret_key: str) -> str:
    """Compute HMAC for a given message and secret key.

    Args:
        message: The message to be hashed.
        secret_key: The secret key used for HMAC computation.

    Returns:
        A Base64-encoded HMAC digest.
    """
    # Choose a hash function
    hash_algorithm = hashlib.sha256
    # Compute the HMAC using the chosen hash function and the secret key
    hmac_object = hmac.new(secret_key.encode(), message.encode(), hash_algorithm)
    # Get the digest (HMAC value)
    hmac_digest = hmac_object.digest()
    # Encode the digest to Base64
    encoded_hmac = base64.b64encode(hmac_digest).decode()
    return encoded_hmac


def create_payload(message: str, secret_key: str) -> Dict[str, Any]:
    """Create a payload with the message and its HMAC.

    Args:
        message: The message to be sent.
        secret_key: The secret key used for HMAC computation.

    Returns:
        A dictionary containing the message and its HMAC.
    """
    hmac_result = compute_hmac(message, secret_key)
    payload = {
        'message': message,
        'hmac': hmac_result,
    }
    return payload


def send_payload(payload: Dict[str, Any]) -> None:
    """Simulate sending the payload to a receiver.

    Args:
        payload: The payload containing the message and HMAC.
    """
    # Simulate sending the payload (e.g., via HTTP, socket, etc.)
    print("Sending payload to appRecv...")
    print(json.dumps(payload, indent=2))


def verify_payload(payload: Dict[str, Any], secret_key: str) -> bool:
    """Verify the integrity of the received payload using HMAC.

    Args:
        payload: The payload containing the message and HMAC.
        secret_key: The secret key used for HMAC computation.

    Returns:
        True if the HMAC is valid, False otherwise.
    """
    received_message = payload.get('message', '')
    received_hmac = payload.get('hmac', '')

    # Recompute the HMAC for the received message
    computed_hmac = compute_hmac(received_message, secret_key)

    # Compare the computed HMAC with the received HMAC
    return hmac.compare_digest(computed_hmac, received_hmac)


def app_send(message: str, secret_key: str) -> None:
    """Simulate the sender application.

    Args:
        message: The message to be sent.
        secret_key: The secret key used for HMAC computation.
    """
    payload = create_payload(message, secret_key)
    send_payload(payload)


def app_recv(payload: Dict[str, Any], secret_key: str) -> None:
    """Simulate the receiver application.

    Args:
        payload: The payload containing the message and HMAC.
        secret_key: The secret key used for HMAC computation.
    """
    print("Receiving payload in appRecv...")
    if verify_payload(payload, secret_key):
        print("HMAC verification successful. Message is authentic.")
        print("Received message:", payload['message'])
    else:
        print("HMAC verification failed. Message may have been tampered with.")


def main() -> None:
    """Main function to demonstrate sending and receiving a payload."""
    message = "Hello, HMAC!"
    secret_key = "mySecretKey"

    # Simulate sending the payload from appSend to appRecv
    app_send(message, secret_key)

    # Simulate receiving the payload in appRecv
    payload = {
        'message': message,
        'hmac': compute_hmac(message, secret_key),
    }
    app_recv(payload, secret_key)


if __name__ == "__main__":
    main()