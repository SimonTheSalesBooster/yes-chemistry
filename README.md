# Yes Chemistry

**Stop getting ghosted after a great sales call.** Find the exact sentence where the buyer stopped wanting the yes, and what to say instead.

The call felt great. They laughed, they nodded, they said "send me the proposal." Then nothing. Your phone stays quiet. No reply to the follow-up, no reply to the follow-up of the follow-up. 🐬

Maybe you ran that call. Maybe it was your new hire. Same silence either way.

The call never created a feeling strong enough to make anyone move. People decide on feeling and defend it with logic later. Antonio Damasio studied patients with damaged emotional brain regions: logic intact, and they could barely decide anything. No feeling, no decision.

The old fix is "pitch harder." More slides, more follow-ups. That hands the buyer control. The better question for your next call: **which feeling does this buyer need right now, and are you creating it in the right order?** Get the order right and you lead the call, and your price lands next to the number they named. No begging, no chasing. 🐯

This free Claude Code skill maps five brain chemicals to the 8 Steps of the Repeatable Sale, reads your call transcript, and shows the exact moment the order broke. Then it hands you the sentence to say instead.

**Dopamine before cortisol. Cortisol before price. Serotonin before signature.** 🌴

Free. No sign-up. Install below, then type `/yes-chemistry`. Not for you if you want pressure tactics: this skill never fakes urgency.

---

## Five feelings, one order

| Chemical | The feeling | Where it belongs in the call |
|---|---|---|
| **Dopamine** | Wanting, curiosity | Being seen, the rabbit hole on ONE big problem, the picture of the result |
| **Cortisol** | The sting of loss | "What happens if you do nothing?" Said by the buyer, never by you |
| **Serotonin** | Calm confidence | Price next to their number, a start date, their words on paper |
| **Oxytocin** | Belonging | Being heard, the commitment, the welcome after they pay |
| **Endorphins** | Shared effort | The hard work together after the yes |

Flip the order and the same chemistry works against you. Price before the buyer has named what doing nothing costs lights up a pain region in the brain (Stanford, 2007) with no reward on the other side of the scale. That's the proposal that goes quiet. 🐬

## The welcome most sellers never send

Simon (who built this) wanted a weekly high-intensity Pilates class. Two studios were cheap. One was very expensive: better teachers, better playlists, fresher air. He picked the expensive one, and right after paying he felt it.. a few seconds of guilt.

Then his phone buzzed. A WhatsApp from the studio, welcoming him to their community. Connection. And proof he'd made the right call paying up for quality. Neither cheap studio sent one. 🐯

Your buyer gets the same bitter few seconds right after signing. `/yes-chemistry welcome` writes that message for your offer.

## What you get

| You type | You get |
|---|---|
| `/yes-chemistry` | A coaching session, one question at a time, ending in your score and ONE move for this week |
| `/yes-chemistry audit call.txt` | Your recorded call scored: where each feeling showed up, where the order broke, 3 fixes with the exact words |
| `/yes-chemistry prep "<who + what you know>"` | One question per step for your next call, plus the one thing NOT to do on it |
| `/yes-chemistry welcome "<your offer>"` | The day-one welcome that turns buyer's remorse into belonging |

## The score: 7 moments, max 14

Seen · Rabbit hole · Stakes · Cost said by the buyer · Picture of the result · Price after pain · Commitment + welcome.

12-14 **YES CHEMISTRY** · 9-11 GOOD CALL, LEAKY ORDER · 6-8 FRIENDLY BUT FLAT · 0-5 A PITCH, NOT A CONVERSATION.

Three red flags cap the verdict: **PRICE BEFORE PAIN**, **PROPOSAL WITHOUT A DATE**, **NO RABBIT HOLE**. Audit every call for a week (yours and your new hire's) and watch the number move. 🐬

See it on a (made-up, very common) demo-first call: [examples/sample-audit.md](./examples/sample-audit.md). 0 out of 14, and the 3 sentences that fix it. 🌴

## Install

```bash
git clone https://github.com/SimonTheSalesBooster/yes-chemistry ~/yes-chemistry
cp ~/yes-chemistry/yes-chemistry.md ~/.claude/commands/
python3 ~/yes-chemistry/tools/order_check.py --selftest
```

Plain Python, no dependencies. The self-test runs a known-good call that must pass clean and a known-bad pitch that must trip every red flag. Export any transcript as plain text ("Speaker: what they said", one line per turn) and run `/yes-chemistry audit`.

## Honest about the science

It's a map, not a lab report. The behaviour research is solid (Damasio, Schultz, Kahneman and Tversky, Knutson, Tamir and Mitchell, Kardas and Epley). "Chemical X at step Y" is shorthand. The famous oxytocin-trust spray study didn't replicate well, so read oxytocin as belonging. Every source and every limit: [knowledge/SCIENCE.md](./knowledge/SCIENCE.md).

## What's in the repo

| File | What it is |
|---|---|
| `yes-chemistry.md` | The skill: the model, the 8 Steps, the score, 4 modes |
| `tools/order_check.py` | Talk share, the order of key moments, red flags, self-test |
| `knowledge/SCIENCE.md` | Sources and honest limits |
| `examples/buying-experiences.md` | Great and weak buying experiences (Apple, Ritz-Carlton, Zappos, Harley-Davidson, the car dealership) |
| `examples/sample-audit.md` | A full audit of a demo-first call |

---

## Who made this

**[Strategy Sprints](https://www.strategysprints.com)**, Simon Severino. We help B2B founders take control of the sales conversation with the 8 Steps of the Repeatable Sale. 2,400+ founders have gone through our programs. 🐯

Want the tools, the AI skills and a room full of founders practicing this every week? Join the Sprint Club, 7 days free: https://www.strategysprints.com 🌴

Ready to accelerate now? Book a Discovery Call: https://calendly.com/strategysprint/discovery-call

Happy hunting.

Simon & The Sprinters 🐬⚡️🐆
