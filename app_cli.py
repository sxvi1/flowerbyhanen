#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from mood_flower.analyzer import load_lexicon, build_index, score_text, dominant_emotions
from mood_flower.mapper import load_flowers, choose_flower

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

def main():
    print("🌸 AI Mood Flower — Type how you feel (English or Arabic).")
    print("Example: 'I feel calm and grateful today'  |  'انا اليوم مبسوطة ومتفائلة'")
    print("-" * 72)

    # Load resources
    lex_path = os.path.join(DATA_DIR, "mood_lexicon.csv")
    flw_path = os.path.join(DATA_DIR, "flowers.csv")
    lex_rows = load_lexicon(lex_path)
    index = build_index(lex_rows)
    flower_db = load_flowers(flw_path)

    while True:
        try:
            text = input("\nYour mood > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye 🌷")
            break

        if not text:
            print("Please type something like: 'tired but hopeful' or 'حزين شوي بس متفائل'")
            continue

        scores = score_text(text, index)
        dom = dominant_emotions(scores, top_k=2)
        if not dom:
            print("Hmm… I couldn't detect a strong emotion. Try different words (e.g., happy, calm, sad, angry, anxious, grateful, hopeful, tired).")
            continue

        main_flower, ribbon = choose_flower(dom, flower_db)

        if not main_flower:
            print("No flower mapping found. Try again with simpler words.")
            continue

        print("\nRecommendation:")
        print(f"  • Flower : {main_flower['flower']} ({main_flower['color']})")
        print(f"  • Meaning: {main_flower['meaning']}")
        if main_flower.get('ascii'):
            print(main_flower['ascii'])

        if ribbon:
            print("\nRibbon note (secondary emotion detected):")
            print(f"  • {ribbon['flower']} ribbon — {ribbon['meaning']}")

        print("\nTip: You can run again and try a different mood sentence.")

if __name__ == '__main__':
    main()
