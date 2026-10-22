#!/usr/bin/env python3
"""Yes Chemistry order check: who talked, and in which order the call hit the key moments.

Reads a plain-text call transcript with one turn per line, "Speaker: what they said".
Prints JSON: talk share per speaker, the first line of each key moment (frustration,
cost of inaction, price, start date, proposal), and red flags when the order is wrong.

It only finds phrases. Judging whether a moment really landed is the skill's job.

Usage:
  python3 order_check.py transcript.txt --seller "Simon"
  python3 order_check.py --selftest
"""
import argparse
import json
import re
import sys
from pathlib import Path

MOMENTS = {
    "frustration": [r"frustrat", r"what have you (already )?tried", r"what('s| is) not working",
                    r"biggest (problem|challenge)", r"what bugs you"],
    "cost_of_inaction": [r"if you do nothing", r"if nothing changes", r"what happens if (you|we) (don't|do not|wait)",
                         r"cost(s|ing)? (you|us) ", r"what does (that|this) cost", r"(lose|losing) (\$|€|deals|clients|money)"],
    "price": [r"[$€£]\s?\d", r"\bprice\b", r"\bpricing\b", r"\binvestment\b", r"\bper month\b", r"\bfee\b", r"\bcosts? \d"],
    "start_date": [r"start(ing)? (date|on|monday|tuesday|wednesday|thursday|friday|the \d|next week|in)",
                   r"kick ?off", r"which date", r"when (do|should|can) we start"],
    "proposal": [r"\bproposal\b", r"statement of work", r"\bSOW\b", r"\bcontract\b", r"send (you|me) (the|a) (deck|offer|quote)"],
}

LINE = re.compile(r"^\s*([^:]{1,40}):\s*(.+)$")


def parse(text):
    turns = []
    for raw in text.splitlines():
        m = LINE.match(raw)
        if m:
            turns.append((m.group(1).strip(), m.group(2).strip()))
        elif turns and raw.strip():
            spk, said = turns[-1]
            turns[-1] = (spk, said + " " + raw.strip())
    return turns


def first_hit(turns, patterns, speaker=None, not_speaker=None):
    for i, (spk, said) in enumerate(turns):
        if speaker and spk.lower() != speaker.lower():
            continue
        if not_speaker and spk.lower() == not_speaker.lower():
            continue
        if any(re.search(p, said, re.I) for p in patterns):
            return i
    return None


def check(text, seller):
    turns = parse(text)
    if not turns:
        return {"error": "no 'Speaker: text' lines found"}
    words = {}
    for spk, said in turns:
        words[spk] = words.get(spk, 0) + len(said.split())
    total = sum(words.values()) or 1
    share = {k: round(v / total, 2) for k, v in words.items()}

    hits = {k: first_hit(turns, p) for k, p in MOMENTS.items()}
    # Cost of inaction counts most when the BUYER says it.
    hits["cost_said_by_buyer"] = first_hit(turns, MOMENTS["cost_of_inaction"], not_speaker=seller)

    flags = []
    if hits["price"] is not None and (hits["cost_said_by_buyer"] is None or hits["price"] < hits["cost_said_by_buyer"]):
        flags.append("PRICE BEFORE PAIN: the price came up before the buyer said what doing nothing costs")
    if hits["proposal"] is not None and hits["start_date"] is None:
        flags.append("PROPOSAL WITHOUT A DATE: a proposal was promised, no starting date was agreed")
    if hits["frustration"] is None:
        flags.append("NO RABBIT HOLE: no frustration question found")
    seller_share = next((v for k, v in share.items() if k.lower() == seller.lower()), None)
    if seller_share is not None and seller_share > 0.6:
        flags.append(f"SELLER TALKED {int(seller_share * 100)}%: the buyer barely got to be seen")

    return {"turns": len(turns), "talk_share": share,
            "first_line": {k: (v + 1 if v is not None else None) for k, v in hits.items()},
            "flags": flags}


def selftest():
    here = Path(__file__).parent / "fixtures"
    good = check((here / "good_call.txt").read_text(), "Seller")
    bad = check((here / "pitch_call.txt").read_text(), "Seller")
    ok = True
    if good["flags"]:
        print("FAIL known-good call raised flags:", good["flags"]); ok = False
    for want in ("PRICE BEFORE PAIN", "PROPOSAL WITHOUT A DATE", "NO RABBIT HOLE", "SELLER TALKED"):
        if not any(f.startswith(want) for f in bad["flags"]):
            print("FAIL known-bad call missed:", want); ok = False
    if check("no speakers here", "x").get("error") is None:
        print("FAIL empty transcript not caught"); ok = False
    print("selftest PASS" if ok else "selftest FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("transcript", nargs="?")
    ap.add_argument("--seller", default="")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(selftest())
    if not a.transcript or not a.seller:
        ap.error("give a transcript file and --seller <name as written in the transcript>")
    print(json.dumps(check(Path(a.transcript).read_text(), a.seller), indent=2))
