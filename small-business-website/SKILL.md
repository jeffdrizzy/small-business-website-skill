---
name: small-business-website
description: Build a complete, fast, mobile-first website for a small local business — barbershop, salon, cleaner, restaurant, gym, clinic, plumber, or any shop. Use when the user asks to build a website for a small business, make a landing page for a local service, add online booking or a quote calculator, or says "build me a site for my shop" or "make a website for a barber / salon / cleaning business". Covers the client brief, template choice, page structure, booking and quotes, SEO, speed, and free deployment.
---

# Small-Business Website

Build a website that gets a small business booked, called, or quoted — not a portfolio piece. The site has one job: a visitor on a phone, in under a minute, can see what the business does, what it costs, when it is open, and how to book or get a quote.

This skill is for a real local business with real services, prices, hours, and contact details. If any of those are missing, ask for them or mark them clearly as placeholders. Never invent prices, hours, reviews, or addresses.

## When to use

Use this skill when the user asks for:

- A website for a small business, shop, salon, barbershop, cleaning service, restaurant, cafe, gym, clinic, tradesperson, or coach
- A landing page for a local service or offer
- Online booking, a booking form, or a quote / price calculator
- A redesign of an existing small-business site

Do not use it for a personal portfolio, a blog, a web app with accounts, or an online store with checkout. Those need different skills.

## Before you build: the 10-minute brief

Do not start coding until you have the brief. Ask for what is missing, in one short round of questions. Use `references/brief.md` for the full checklist.

Collect, at minimum:

1. Business name, what it does, and who it serves
2. Services, with a price for each (or "from" prices, or "ask for a quote")
3. Opening hours, including closed days
4. Location or service area, and how customers reach it
5. Contact: phone / WhatsApp number and email — exactly as the owner gives them
6. Booking method: phone, WhatsApp, form, or walk-in only
7. Photos: real photos of the shop, staff, and work, if available. If none, use plain colour blocks and typography, not stock photos that pretend to be the business
8. Reviews: only real reviews, with the customer's first name or initial if the owner provides it. Never invent reviews
9. One clear goal: bookings, calls, quote requests, or visits

If the owner cannot give prices, build the page so prices are easy to add later, and say so in your handover. Do not guess prices.

## Step 1: Pick the template

Pick one of three templates. Do not mix them.

### A. Business website

For a shop with several services — barbershop, salon, clinic, restaurant, gym.
Sections: hero, services and prices, about / why choose us, reviews, booking, hours and location, contact.

### B. Landing page

For one offer — a coaching programme, a seasonal promotion, a new service.
Sections: hero with the offer, the problem and the result, what is included, price, proof, one call to action, FAQ, contact.
One page, one offer, one button repeated. No navigation to other services.

### C. Quote tool

For a service priced per job — cleaning, plumbing, gardening, repairs, moving.
Sections: hero, the calculator, what affects the price, example prices, how booking works, contact.
The calculator must show a price range or an estimate and say it is an estimate, not a final price. Always offer "send this quote on WhatsApp / by email" as the next step.

See `references/brief.md` for how to choose, and `examples/barbershop.md` and `examples/cleaning-quote.md` for worked examples.

## Step 2: Build mobile-first, one page

Build a single page first. Add extra pages only if the business truly needs them.

Page order, in this order:

1. **Hero** — business name, what it does, where it is, one button: Book, Call, or Get a quote. Phone number visible.
2. **Services and prices** — every service with a price, or a clear "from" price. No service without a price or a reason why.
3. **Proof** — real reviews, real photos, years in business, or number of customers served, if true.
4. **How it works** — three steps: book, visit / service, pay. Keep it to three steps.
5. **Booking or quote** — the booking form, WhatsApp button, or calculator. This is the point of the page. Do not bury it at the bottom with no link from the hero.
6. **Hours and location** — opening hours in a table, address or service area, map link. State closed days.
7. **Contact and footer** — phone, WhatsApp, email, hours again, copyright line.

Design rules — see `references/design.md` for the full list:

- Mobile first. Test at phone width first, then desktop. Most visitors are on a phone.
- One clear call to action per screen. Book, Call, or Get a quote — not all three competing.
- Readable text: body text at least 16px, high contrast, no light grey text on white.
- Real photos only. If there are no photos, use colour, type, and spacing — do not fake it.
- Keep the page fast: compress images, no heavy libraries for a simple site, no autoplay video.
- Accessible: real buttons and links, labels on form fields, alt text on images, keyboard-usable navigation.

## Step 3: Booking and quotes

See `references/booking-quote.md` for the full procedure.

### Booking

- Offer the booking method the owner actually answers: phone, WhatsApp, or a form that goes to their email.
- A WhatsApp booking link must be built from the number the owner gave you, with a pre-filled message like "Hi, I'd like to book [service] on [date]". Test the link.
- A form must ask only what is needed to book: name, service, date / time, phone. No account, no password, no extra fields.
- After submit, show a clear confirmation: what happens next, and when the owner will reply. Do not show a dead end.
- Show opening hours next to the booking widget, so people do not try to book when the shop is closed.

### Quote calculator

- Inputs: the things that change the price — size, number of rooms, service type, frequency. Keep it to 3–5 inputs.
- Output: a price range, labelled as an estimate, with what is included and what is not.
- Next step: "Send this quote" by WhatsApp or email, with the inputs included in the message.
- Never present an estimate as a fixed price. Never hide fees that appear later.

## Step 4: SEO, speed, and accessibility basics

See `references/seo-deploy.md` for the checklist.

- Title: business name, what it does, and town / area — in that order.
- One H1, matching the title. One meta description, written as a sentence a customer would read.
- Local SEO: business name, address / service area, and phone number, written the same way on every page.
- Images: compressed, with descriptive file names and alt text.
- Speed: the page should load in under 3 seconds on a phone connection. Check it before handover.
- Accessibility: colour contrast, focus states, form labels, no text baked into images as the only copy.

## Step 5: Deploy free and test on a phone

1. Deploy to a free static host — Netlify or GitHub Pages. No server needed for templates A and B; a quote tool can be client-side only.
2. Test on a real phone, not just a desktop preview: tap every button, submit the form, tap the WhatsApp link, tap the phone number to call.
3. Check: hero fits without scrolling sideways, prices are readable, hours are correct, the booking button works, the page loads fast.
4. Fix what fails, then test again. Do not hand over a site you have not tested on a phone.

## Step 6: Handover checklist

Hand over in writing, in plain language the owner can follow:

- [ ] Live link, and how to open it
- [ ] What to send you to change prices, hours, photos, or services
- [ ] How bookings / quote requests reach the owner, and what to do when one arrives
- [ ] What is still a placeholder, if anything, and what is needed to fill it
- [ ] How to renew or keep the free hosting live, if anything is needed

## Common mistakes — do not do these

- Desktop-only design. Most customers are on a phone.
- No prices, no hours, no contact on the page. Those are the three things visitors look for first.
- A beautiful hero and a hidden booking button. The booking action must be visible in the hero and repeated.
- Inventing reviews, prices, addresses, or photos. If you do not have it, leave it out or mark it as a placeholder.
- Slow images, autoplay video, pop-ups on first visit, or a cookie banner that covers the booking button.
- Client copy that sounds like a robot or an ad for AI. Write like the owner talks: plain, local, specific. Name the services, the area, and the price.
- Adding an online store, accounts, or payments when the owner only asked for bookings. Keep the scope to what was asked.

## What NOT to do

- Do not lead with AI in client-facing copy, and do not say the site was built with AI unless the owner asks directly. Frame the work as fast and hand-finished.
- Do not collect customer data you do not need. No accounts, no tracking beyond basic anonymous visit counts if the owner asks for it.
- Do not use stock photos as if they are the business, and do not use another business's name, logo, or reviews.
- Do not hardcode one currency, country, or language as if every business is the same. Use the currency and language the owner uses, and keep it as a single setting so it can be changed.
- Do not promise bookings, customers, or search rankings. Promise a fast, clear site that makes booking easy.

## Arguments

When invoked as `/small-business-website [business type]`, use the argument as the business type and template hint, for example `/small-business-website barbershop` or `/small-business-website cleaning quote`. If no argument is given, ask for the business type and the goal — bookings, calls, or quotes — before building.
