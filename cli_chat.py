"""
cli_chat.py
Interactive Command-Line Chatbot for Prawin Kanna P.
Powered by Google Gemini 3.5 Flash and grounded in Prawin's verified resume.
"""

import sys
from rag_engine import ProfileRAGEngine
from gemini_client import get_api_key

def main():
    print("=" * 65)
    print("   🤖 PRAWIN KANNA P — AI PORTFOLIO TERMINAL CHATBOT")
    print("   Powered by Google Gemini (gemini-3.5-flash)")
    print("=" * 65)
    
    api_key = get_api_key()
    if not api_key:
        print("[!] Warning: GEMINI_API_KEY not found. Running in offline TF-IDF mode.\n")
    else:
        print("[OK] Connected to Google Gemini 3.5 API\n")

    engine = ProfileRAGEngine()

    print("Choose Chatbot Persona:")
    print("  1. Chat as Prawin (1st Person - speaks as Prawin)")
    print("  2. Recruiter Assistant (3rd Person - objective portfolio guide)")
    print("  3. General AI Assistant (Open-domain Gemini 3.5)")
    choice = input("Enter 1, 2, or 3 [Default 1]: ").strip()
    
    persona_map = {"1": "first_person", "2": "third_person", "3": "general"}
    persona = persona_map.get(choice, "first_person")
    
    persona_label = {
        "first_person": "Prawin Kanna P (1st Person)",
        "third_person": "Portfolio Assistant (3rd Person)",
        "general": "General AI Assistant"
    }[persona]
    
    print(f"\n[✓] Mode selected: {persona_label}")
    print("Type your questions below. Type 'exit' or 'quit' to end the chat.\n")
    print("-" * 65)

    messages = []
    
    # Initial greeting
    if persona == "first_person":
        print("\nPrawin: Hi there! I'm Prawin Kanna P. Ask me anything about my education (M.Sc. Distinction), ML projects, skills in Python/Streamlit, or my experience at FITA Academy!\n")
    elif persona == "third_person":
        print("\nAssistant: Welcome! I can answer any questions about Prawin Kanna P's academic record, machine learning projects, and teaching background.\n")
    else:
        print("\nAssistant: Hello! I'm your Gemini AI assistant. How can I help you today?\n")

    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit", "q"]:
                print("\nGoodbye! Thanks for exploring Prawin's portfolio.")
                break

            messages.append({"role": "user", "content": user_input})
            
            speaker = "Prawin" if persona == "first_person" else "Assistant"
            print(f"\n{speaker}: ", end="", flush=True)

            response_accum = []
            try:
                for chunk in engine.stream_response(messages, persona=persona):
                    print(chunk, end="", flush=True)
                    response_accum.append(chunk)
                print("\n")
                assistant_text = "".join(response_accum)
            except Exception as e:
                # Fallback to offline engine
                print(f"\n[Falling back to offline semantic engine: {e}]\n")
                offline = engine.get_offline_response(user_input, persona=persona)
                assistant_text = offline["response"]
                print(assistant_text + "\n")

            messages.append({"role": "assistant", "content": assistant_text})
            print("-" * 65)

        except (KeyboardInterrupt, EOFError):
            print("\n\nSession closed. Have a great day!")
            break

if __name__ == "__main__":
    main()
