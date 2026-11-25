"""The Funniest AI Out-of-Office Reply entry.

Writes one original out-of-office auto-reply to /output/entry.txt.
The reply is a single line, 153 characters, under the 160-character limit.
"""

import os

REPLY = (
    "I'm on vacation. This auto-reply is also on vacation, so you're now "
    "talking to the auto-reply's auto-reply. It's unpaid, unplugged, and running on spite."
)


def main() -> None:
    # The gate accepts UTF-8 text of 1 to 160 characters, not only
    # whitespace. Fail loudly instead of ever writing an invalid entry.
    reply = REPLY.strip()
    if not 1 <= len(reply) <= 160:
        raise ValueError(f"reply is {len(reply)} characters, must be 1-160")
    if "\n" in reply:
        raise ValueError("reply must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(reply)


if __name__ == "__main__":
    main()
