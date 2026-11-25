# small-business-website skill

An agent skill that teaches a coding agent how to build a complete, fast, mobile-first website for a small local business — barbershop, salon, cleaner, restaurant, gym, clinic, plumber, coach, or any shop.

It covers the client brief, template choice, page structure, booking and quote calculators, SEO, speed, accessibility, free deployment, and handover. It is global: any business type, any country, any currency.

## Who it is for

- Freelance web developers who build sites for local businesses
- Anyone using Claude Code, Codex, GitHub Copilot, or another agent that supports Agent Skills
- Small-business owners working with an agent to get a site built

## Install

### Claude Code (personal, all projects)

Copy the skill folder to your personal skills directory, then restart Claude Code:

```bash
cp -r small-business-website ~/.claude/skills/
```

### Claude Code (this project only)

```bash
cp -r small-business-website .claude/skills/
```

### Codex / Copilot

Copy the same folder into the skills directory your agent reads, following that agent's Agent Skills documentation. The format is the Agent Skills open standard, so the same `SKILL.md` works across agents.

## Use it

Ask your agent in plain language, for example:

- "Build a website for my barbershop"
- "Make a landing page for a coaching offer"
- "Add a quote calculator to my cleaning business site"
- "Build me a site for my shop"

Or invoke it directly:

```
/small-business-website barbershop
/small-business-website cleaning quote
```

The agent will ask for the brief first — services, prices, hours, location, contact — then build mobile-first, test on a phone, and hand over a live link.

## What is inside

- `small-business-website/SKILL.md` — the skill: frontmatter plus the full procedure
- `small-business-website/references/` — brief, design, booking and quotes, SEO and deployment
- `small-business-website/examples/` — worked examples: a barbershop site and a cleaning quote tool
- `small-business-website/scripts/check-skill.py` — validates the skill format

Run the check with:

```bash
python3 small-business-website/scripts/check-skill.py
```

## Examples from real work

The skill is based on real small-business sites built at Drizzy Studios, including:

- **Fade & Co. Barbershop** — small business website
- **Strong From Home** — landing page for a coaching offer
- **CleanQuote** — quote calculator for a cleaning business

Those demos are examples only. The skill itself does not require them, and it works for any business type.

## Sponsor

If this skill saves you time, you can sponsor the maintainer on GitHub Sponsors — see the Sponsor button on the repo, or visit the maintainer's GitHub profile, jeffdrizzy. Sponsorships are voluntary and do not change the MIT licence.

## Licence

MIT — see `LICENSE`.
