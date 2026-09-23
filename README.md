# tinygpt.ai

Parked for-sale page for [tinygpt.ai](https://tinygpt.ai). Static HTML on GitHub Pages. Inquiries go to [@cepstrum9](https://x.com/cepstrum9) on X.

## Local preview

Open `index.html` in a browser, or:

```bash
python3 -m http.server 8080
```

Then visit `http://localhost:8080`.

## Tests

```bash
python3 -m unittest tests.test_site
```

## GitHub Pages

This repo is the site. After the first push:

1. Settings → Pages → Deploy from branch `main` / root (already set if created via `gh`).
2. Custom domain: `tinygpt.ai`.
3. Wait for DNS, then enable **Enforce HTTPS**.

## DNS (at your registrar)

Point the apex at GitHub Pages. Delete any Website Builder / parking `@` record first. Leave `www` as CNAME → `tinygpt.ai.`

| Type | Name | Value |
|---|---|---|
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |

## Another domain

Copy this repo, then change the domain string in `index.html`, `404.html`, `CNAME`, `robots.txt`, and `sitemap.xml`.
