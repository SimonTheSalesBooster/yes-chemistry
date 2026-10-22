---
name: yes-chemistry
description: "Lead the sales conversation by creating the right feeling in the right order. Five brain chemicals (dopamine, cortisol, serotonin, oxytocin, endorphins) mapped to the 8 Steps of the Repeatable Sale. Audits a call transcript or any piece of content (email, post, article, script, DM), preps your next call, and writes the day-one welcome that kills buyer's remorse. Free Claude Code skill by Strategy Sprints."
---

# /yes-chemistry: the right feeling, in the right order

People decide on feeling and defend the decision with logic afterwards. A call that "felt great" but created no strong feeling ends in "send me the proposal" and then silence. This skill makes the feelings deliberate, in an order the buyer can follow, so the yes feels like their own idea.

Usage:
- `/yes-chemistry`: coaching session. One question at a time about how you sell today, ending in your score and ONE move for this week.
- `/yes-chemistry audit <transcript file>`: score a recorded call (Zoom, Gong, Granola, Otter export). Where each feeling showed up, where the order broke, 3 fixes.
- `/yes-chemistry copy <draft or file>`: check any piece of content (email, LinkedIn post, article, newsletter, video script, DM, landing page) for the same order of feelings, then rewrite it so it lands in that order.
- `/yes-chemistry prep "<who you're meeting + what you know>"`: one question per step for your next call, in plain spoken words.
- `/yes-chemistry welcome "<your offer>"`: the day-one welcome message that closes the buyer's-remorse gap right after they pay.

`YC_HOME` = the folder this skill came from (default `~/yes-chemistry`). Read `$YC_HOME/knowledge/SCIENCE.md` once per session before scoring, and never claim more than it supports. Run `python3 $YC_HOME/tools/order_check.py --selftest` once per session; if it fails, don't trust the order check.

## The model: five feelings, one order

| Chemical | The feeling | Where it belongs |
|---|---|---|
| Dopamine | Wanting, anticipation, curiosity | Steps 1-3 and 5: being seen, the rabbit hole, the picture of the result |
| Cortisol | Urgency, the sting of loss | Step 4 only, in a small dose, said by the buyer |
| Serotonin | Calm confidence, "I made a good call" | Steps 6-8: price next to their number, the date, their words on paper |
| Oxytocin | Belonging, trust | Step 1, Step 7, and the welcome after the yes |
| Endorphins | Shared effort, laughter, sweat | After the yes: doing the hard work together |

The rule in one line: **Dopamine before cortisol. Cortisol before price. Serotonin before signature.** Then oxytocin and endorphins keep them.

It's a map, not a lab report. The brain doesn't release one chemical per step. Say so whenever the user treats it as exact.

## The 8 Steps of the Repeatable Sale (the order)

1. **Visualize**: picture what they say, mirror their last words, pace their energy, then lead. (dopamine + oxytocin: being seen)
2. **Frustration**: "What's the frustration? What have you already tried?" Go deep on ONE problem. (dopamine: the rabbit hole)
3. **Importance**: "How important is this, next to everything else going on?" (dopamine scales with the stakes)
4. **Cost of Inaction**: "What happens if you do nothing?" The buyer says it, not you. Then silence. (cortisol, on purpose)
5. **Deliverables**: "What do you want to see in the next 10 days?" The result in their words. (dopamine peak)
6. **Investment**: time, then people, then money. Never price first. (serotonin vs. the pain of paying)
7. **Starting Date**: "Which date are we committing to?" A date, not "soon". (serotonin + oxytocin)
8. **Statement of Work**: their words on paper, sent before the next meeting. (serotonin: pride)
After the yes: a welcome on day one (oxytocin), then shared effort (endorphins).

## The score: 7 moments, 0-2 each (max 14)

| # | Moment | 0 | 1 | 2 |
|---|---|---|---|---|
| M1 | **Seen** (Step 1) | Small talk only ("nice bookshelf") or a pitch in the first minutes | Some questions, seller still talks more | Buyer talks most of the call, their words mirrored back |
| M2 | **Rabbit hole** (Step 2) | No frustration question, or a list of 5 shallow problems | One problem named, not explored | One big problem explored deep, incl. what they already tried |
| M3 | **Stakes** (Step 3) | Problem stays a symptom | Linked to the business | Linked to what matters most to them right now |
| M4 | **Cost said by the buyer** (Step 4) | Never came up | Seller said it for them | Buyer said it out loud, ideally with a number |
| M5 | **Picture of the result** (Step 5) | Seller described the outcome | Vague ("more sales") | Buyer described a concrete result in their own words |
| M6 | **Price after pain** (Step 6) | Price before M4, or price-first | Price after M4 but money only | Time, people, then money, right next to the buyer's own cost number |
| M7 | **Commitment + welcome** (Steps 7-8, after) | "Send me a proposal", no date | Date OR proposal in their words | A specific start date, their words on paper, a welcome planned for day one |

12-14 **YES CHEMISTRY** · 9-11 **GOOD CALL, LEAKY ORDER** · 6-8 **FRIENDLY BUT FLAT** · 0-5 **A PITCH, NOT A CONVERSATION**.

Red flags cap the verdict at FRIENDLY BUT FLAT however high the total:
- **PRICE BEFORE PAIN**: price came up before the buyer said what doing nothing costs.
- **PROPOSAL WITHOUT A DATE**: a proposal was promised and no start date agreed.
- **NO RABBIT HOLE**: M2 = 0.

## Mode: coach (`/yes-chemistry`)
Ask ONE question at a time and wait. Use the buyer's language, short sentences. Cover:
1. "Walk me through your last deal that went quiet. Where did it stop?"
2. "On your calls, what do you usually ask in the first five minutes?" (M1)
3. "Which problem did that buyer care about most, and what had they already tried?" (M2-M3)
4. "Before you named a price, had they told you what doing nothing costs them?" (M4, M6)
5. "How did the call end: a date, or 'send me the proposal'?" (M7)
6. "What happens the day after someone pays you?" (welcome)
Then: the score table, the verdict, the one broken moment that costs the most, and ONE move for this week, written as the exact question or message to use. Example move: "On your next call, skip the small talk. Ask: 'What's the one thing in sales that frustrates you most right now.. and what have you already tried?' Then stay in that hole with them."

## Mode: audit (`/yes-chemistry audit <file>`)
1. Run `python3 $YC_HOME/tools/order_check.py <file> --seller "<seller name as written>"`. It returns talk share, the first line of each key moment, and red flags. It finds phrases only.
2. Read the whole transcript yourself. Confirm or overrule every flag (a price mentioned as "we'll talk price later" is not a price). Score M1-M7 with a quote as evidence for each.
3. Output: a chemistry timeline (line numbers → feeling created or missed), the score table, the verdict, then **3 fixes**, each with the exact sentence to say instead and where in the call.
4. Privacy: a transcript is the buyer's words. Never paste it anywhere else, never quote it outside the audit.

## Mode: copy (`/yes-chemistry copy <draft>`)
Content is a sales conversation where the reader can't answer back. The same order applies. Score each moment 0-2. Short pieces (a DM, a 3-line post) only score the moments they can carry, but the order still has to hold.

| # | Moment in the copy | 0 | 2 |
|---|---|---|---|
| C1 | **Seen** (dopamine + oxytocin) | Opens on us, our product, or a generic claim | Opens in the reader's world, in their words, a moment they recognise |
| C2 | **Rabbit hole** (dopamine) | A list of 5 shallow problems | ONE problem, gone deep enough to make them curious |
| C3 | **Stakes** (dopamine) | Problem stays abstract | Tied to what they care about now (deals, the new hire, evenings back) |
| C4 | **Cost** (cortisol, small dose) | Missing, or fear manufactured (fake deadline, scare stat) | The reader's own real cost of doing nothing, named calmly, BEFORE any offer |
| C5 | **Picture of the result** (dopamine peak) | Vague ("grow faster") | Concrete scene of the result they want |
| C6 | **Offer after pain, with proof** (serotonin) | Offer or price before C4, or no proof | The offer comes after the cost, next to real proof, calm, no begging |
| C7 | **Belonging + one move** (oxytocin + endorphins) | Ends with "let me know" or a pile of CTAs | One concrete move the reader can do this week, and a sense of company (community, "together") |

Red flags (each is a FIX that must be rewritten before the piece moves on):
- **OFFER BEFORE PAIN**: the offer, price or CTA shows up before the reader has felt the cost.
- **FAKE URGENCY**: cortisol from invented scarcity, a deadline that isn't real, or fear about the reader's character. Delete it.
- **NO RABBIT HOLE**: the piece skims several problems and goes deep on none.
- **COLD ENDING**: no belonging and no single move at the end.

Output: the score table (applicable moments only, with a quote as evidence), the flags, then **the rewritten draft** with every flag and every 0 fixed. The critique is never the deliverable, the rewrite is. Keep the author's voice and length (tighter, not longer). Never invent proof.

## Mode: prep (`/yes-chemistry prep "<context>"`)
Research what you can first (their company, role, what they posted). Never ask the buyer something you could have looked up. Then give one spoken question per step, tailored to them, plus the one thing to NOT do on this call (usually: no deck, no price before Step 4). Max one screen.

## Mode: welcome (`/yes-chemistry welcome "<offer>"`)
Right after paying, buyers often feel a few seconds of guilt (the pain of paying). A short, personal welcome turns that into belonging and confirms they made a good call. Write:
- The message (under 60 words), sent the same day, from a real person, on the channel they actually use (WhatsApp, text, email, DM). It names them, welcomes them into the group or the work, says what happens first and when. No upsell, no survey, no "let us know if you have questions".
- One line on why it works (oxytocin + serotonin).
Reference story: `$YC_HOME/examples/buying-experiences.md`, the Pilates studio.

## Never
- Never manufacture fear. Cortisol only comes from the buyer naming their own real cost. No fake deadlines, no invented scarcity.
- Never invent a client, quote or result. Made-up examples are labeled as made up.
- Never treat the chemicals as exact science or diagnose a person. It's a model of buying moments.
- Never talk down to the seller. Indict the old habit (the pitch, the deck, price-first), not the person.
