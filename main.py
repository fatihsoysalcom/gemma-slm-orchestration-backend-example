import json

# Simulate a simple Small Language Model (SLM) for sentiment analysis
def analyze_sentiment(text):
    """Simulates a Gemma-like SLM for sentiment analysis."""
    text_lower = text.lower()
    if "great" in text_lower or "excellent" in text_lower or "love" in text_lower:
        return "positive"
    elif "bad" in text_lower or "terrible" in text_lower or "hate" in text_lower:
        return "negative"
    else:
        return "neutral"

# Simulate another SLM for topic extraction
def extract_topic(text):
    """Simulates a Gemma-like SLM for topic extraction."""
    text_lower = text.lower()
    if "python" in text_lower or "code" in text_lower or "programming" in text_lower:
        return "programming"
    elif "weather" in text_lower or "sunny" in text_lower or "rainy" in text_lower:
        return "weather"
    else:
        return "general"

# Backend Orchestrator
def orchestrate_request(user_input):
    """Orchestrates calls to different SLMs based on the input."""
    print(f"--- Processing Input: '{user_input}' ---")

    # Step 1: Analyze sentiment using the sentiment SLM
    sentiment = analyze_sentiment(user_input)
    print(f"Sentiment Analysis SLM: Detected sentiment is '{sentiment}'.")

    # Step 2: Extract topic using the topic extraction SLM
    topic = extract_topic(user_input)
    print(f"Topic Extraction SLM: Detected topic is '{topic}'.")

    # Step 3: Combine results and decide on a response strategy
    # This is where the 'backend orchestration' logic resides.
    # We can use the results from SLMs to inform a final output or action.
    final_response = {
        "original_input": user_input,
        "sentiment": sentiment,
        "topic": topic,
        "orchestrated_output": f"Based on your input, the sentiment is {sentiment} and the topic is {topic}."
    }

    if sentiment == "positive" and topic == "programming":
        final_response["orchestrated_output"] += " It sounds like you're enjoying programming!"
    elif sentiment == "negative":
        final_response["orchestrated_output"] += " I hope things get better."

    print(f"Orchestrated Response: {json.dumps(final_response, indent=2)}")
    print("-------------------------------------\n")
    return final_response

# --- Example Usage ---
if __name__ == "__main__":
    # Simulate user requests that would be handled by the backend
    requests = [
        "I love learning about Gemma and Python programming!",
        "The weather today is terrible, very rainy.",
        "This is a general statement.",
        "Excellent code, very efficient!"
    ]

    for req in requests:
        orchestrate_request(req)
