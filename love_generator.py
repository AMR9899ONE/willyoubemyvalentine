#!/usr/bin/env python3
"""
💕 Infinite Reasons I Love You Generator 💕

A simple script to remind you why you're amazing!
Run this whenever you need a pick-me-up.
"""

import random
from datetime import datetime

# Reasons in English
reasons_en = [
    "Your compassion for others shines through in everything you do",
    "The way you dedicate yourself to becoming a great doctor",
    "Your beautiful smile that lights up every room",
    "How you never give up, even when things are tough",
    "The gentle way you care for everyone around you",
    "Your brilliant mind and how you love to learn",
    "The way you make even difficult days feel manageable",
    "Your kindness to everyone you meet",
    "How your eyes sparkle when you talk about your dreams",
    "The way you balance strength and gentleness perfectly",
    "Your adorable love for Totoro and all things Ghibli",
    "How you appreciate the beauty in small things, like flowers",
    "Your determination to make a difference in the world",
    "The way you make me want to be a better person",
    "Your infectious laughter that I could listen to forever",
    "How you stay humble despite being so accomplished",
    "The way you care about doing things right",
    "Your ability to find joy even during stressful times",
    "How you treat everyone with respect and dignity",
    "The beautiful person you are, inside and out",
    "Your dedication to helping and healing others",
    "The way you light up my entire world",
    "How you make every day an adventure",
    "Your courage in pursuing such a challenging career",
    "The way you never lose sight of what matters most",
    "How you make me feel loved and cherished",
    "Your ability to see the good in people",
    "The way you work so hard while staying so kind",
    "How you inspire me every single day",
    "Simply everything about you"
]

# Reasons in Japanese (romanized for easy display)
reasons_jp = [
    "優しい心を持っているところ (Your gentle heart)",
    "いつも一生懸命頑張っているところ (How you always try your best)",
    "素敵な笑顔 (Your wonderful smile)",
    "思いやりがあるところ (Your compassion)",
    "夢に向かって頑張る姿 (How you work towards your dreams)",
    "トトロが好きなところ (How you love Totoro)",
    "花が好きな優しい心 (Your gentle heart that loves flowers)",
    "頭が良くて尊敬できるところ (Your intelligence and how I respect you)",
    "困難に立ち向かう強さ (Your strength facing difficulties)",
    "全部が大好き (I love everything about you)"
]

def get_random_reason():
    """Get a random reason in both English and Japanese"""
    en_reason = random.choice(reasons_en)
    jp_reason = random.choice(reasons_jp)
    return en_reason, jp_reason

def print_heart_border():
    """Print a decorative border"""
    print("\n" + "💕" * 30)

def main():
    print("\n✨ Welcome to the 'Infinite Reasons I Love You' Generator ✨\n")
    print("Press Enter to see a reason why you're amazing!")
    print("(Type 'quit' to exit)\n")
    
    count = 0
    
    while True:
        user_input = input("💕 Ready? Press Enter: ").strip().lower()
        
        if user_input == 'quit':
            print_heart_border()
            print("\n🌸 Remember: You are loved beyond measure! 🌸")
            print("愛してる (I love you) ❤️\n")
            print_heart_border()
            break
        
        count += 1
        en_reason, jp_reason = get_random_reason()
        
        print_heart_border()
        print(f"\n💝 Reason #{count}:")
        print(f"\n{en_reason}")
        print(f"\n{jp_reason}")
        print_heart_border()
        print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n💕 You are loved! 愛してる ❤️ 💕\n")
