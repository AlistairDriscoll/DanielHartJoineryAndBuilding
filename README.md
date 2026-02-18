# Daniel Hart Joinery & Building — Static Website

A lightweight, multi-page **static website** for a joinery / building services business. Visitors can browse past work, read reviews, and get in touch for enquiries/quotes.

## Contents

- [Project Overview](#project-overview)
- [Pages](#pages)
- [Tech Stack](#tech-stack)
- [Run Locally](#run-locally)
- [Deployment](#deployment)
- [SEO](#seo)
- [Contact](#contact)

## Project Overview

This repository contains the website source for **Daniel Hart Joinery & Building**. It’s built as a static site (HTML + assets) and includes multiple pages for services, reviews, and past work.
## Pages

The site is organised as separate HTML pages, including:
- `index.html` — Home
- `get_a_quote.html` — Quote/enquiry
- `past_work_main.html` — Past work hub
- `reviews_page1.html`, `reviews_page2.html`, `reviews_page3.html` — Reviews
- `bookcases.html` — Service/work page
- `stairs.html` — Service/work page
- `joinery_1.html` — Service/work page
- `offices_in_leeds.html` — Service/work page

Static assets live in:

- `assets/` — CSS, images, and any JS used by the site

## Tech Stack

- **HTML** (multi-page site)
- **CSS / assets** (in `assets/`) :contentReference[oaicite:4]{index=4}
- Optional: **JavaScript** (if included in `assets/`)

## Run Locally

### Option A: Open directly
You can open `index.html` in your browser (double-click it), but some browsers can be picky about relative paths.

### Option B: Use a local server (recommended)
From the repo root:

**Python**
```bash
python -m http.server 8000
```

Then visit:

http://localhost:8000

### VS Code Live Server

1. Install the **Live Server** extension in VS Code
2. Right-click `index.html`
3. Select **Open with Live Server**

---

## Deployment

This repo is suitable for **GitHub Pages** deployment (static site). It also includes:

- `CNAME` (for a custom domain)

There is also a 'full-stack' branch of the site, the client in question at first wanted this in order to store a database of enquiries that users make, but after deeming it too expensive to host, this static site branch was made instead. The templates are slightly incomplete and don't do as well on small screens but do still look mostly the same.

### Typical GitHub Pages Setup

1. Go to **Repo → Settings → Pages**
2. Under **Source**, select:
   - Branch: `main`
   - Folder: `/ (root)`
3. (Optional) Add or confirm your custom domain

---

## SEO

This project includes:

- `robots.txt`
- `sitemap.xml`

If you add or remove pages, make sure to update `sitemap.xml` so search engines can correctly discover and index your content.

---

## Contact

**Repo owner:** AlistairDriscoll