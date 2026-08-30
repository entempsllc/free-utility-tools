# Free Utility Tools — Durable Project Memory

## Source of truth
- Project: `free-utility-tools`
- Live: https://entempsllc.github.io/free-utility-tools/
- Repository: `/Users/jp/Projects/github-sites/free-utility-tools`
- Published branch: `main`

## Current verified state
- Production is GitHub Pages at the project URL; no custom domain is evidenced.
- Homepage and six tool routes return HTTP 200. `sitemap.xml` and `sitemap.txt` return 200; `robots.txt` and a random invalid route return 404.
- The homepage includes AdSense loader account `ca-pub-9706598462382632` and styled placeholders. Active ad units, account approval, fill, viewability, CMP configuration, RPM, and revenue are unverified.
- Authorized Search Console and analytics data were unavailable; traffic and tool usage are unverified.
- `AGENTS.md`, `PROJECT_BRIEF.md`, and `.project-agent/` are local project-control files and remain untracked; site-source publication must preserve them unless deliberately reviewed.

## Durable decisions
- Prefer useful-tool quality, navigation, and privacy-safe aggregate usage evidence before traffic-dependent monetization claims.
- Do not mass-generate tools or infer demand from repository activity, page count, tags, or polish.
- Protected indexing, account, outreach, spending, deletion, pricing/payment, and legal-policy changes require approval.

## Run history
### 2026-08-16 — Portfolio referral CTA
- Commit `2e7db95` added a conditional CTA for the exact Entemps portfolio UTM contract. Live production was verified; no traffic, conversion, or revenue was established.

### 2026-08-17 — Internal navigation retention repair
- **Purpose gate:** This artifact serves word-counter, password-generator, and Base64 users by returning them to the Free Utility Tools project rather than losing them to the GitHub account root, fits clear navigation and measurable tool usefulness, advances retained discovery of useful tools, is not a duplicate of the portfolio-referral CTA, and is supported by source URL resolution plus live HTTP/HTML evidence.
- Found three `href="/"` back links resolving to `https://entempsllc.github.io/` instead of the project root. Changed only those links to `../`.
- Added `tests/test_navigation.py` with two contracts across all six tool pages: every tool links to the production project root and none links to the GitHub account root.
- Fresh validation: 2/2 tests passed; seven HTML pages parsed; `git diff --check` passed.
- Published commit `e7c3f5462b1404227159f068576ee6b96cb0c3bd`. Live word-counter, password-generator, and Base64 routes each returned HTTP 200 and served `../` without the old `/` back link on deployment poll 7.
- No deletion, indexing/crawler, analytics/account, outreach, spending, pricing/payment, legal-policy, affiliate, or ad configuration change. No traffic, conversion, or revenue claim.
- Release state: **live production verified**.

## Next highest-value task
Audit the remaining five tools for functional correctness, privacy-claim accuracy, route metadata, real ad-unit/CMP readiness, and measurement. If an authorized analytics destination and matching disclosure are verified, implement aggregate `tool_view` and first-interaction events without input/output payloads.

### 2026-08-22 — Password generator secure-randomness repair
- **Purpose gate:** This artifact serves privacy-conscious users generating passwords by replacing predictable `Math.random()` selection with rejection-sampled Web Crypto randomness, fits developer encoding and security helpers plus truthful claims, advances trustworthy useful-tool completion, is not a duplicate of the prior navigation repair, and is supported by source inspection, regression tests, preview, deployment, and live HTML evidence.
- Changed only `password-generator/index.html` and `tests/test_navigation.py` in commit `d706e97`.
- Added an honest empty-selection state instead of returning an empty password when all character groups are disabled.
- Fresh validation: 3/3 canonical tests passed; `git diff --check` passed; local HTTP preview passed.
- Published to `main`; live production HTML at `/password-generator/` contained `crypto.getRandomValues`, omitted `Math.random`, and contained the empty-selection message on deployment poll 5.
- No deletion, indexing/crawler, outreach, spending, account, pricing/payment, legal-policy, analytics, affiliate, or ad change. Traffic, usage, conversion, sales, and revenue remain unverified.
- Release state: **published and live production verified**.

### 2026-08-23 — Resume scanner matching correctness repair
- **Purpose gate:** This artifact serves job seekers using the ATS resume scanner by preventing substring false positives and an undefined empty-keyword score, fits career workflow tools and truthful measurable usefulness, advances trustworthy tool completion, is not a duplicate of the password or navigation repairs, and is supported by source inspection, RED/GREEN regression evidence, executable JavaScript behavior checks, and live production HTML.
- In isolated detached worktree `/tmp/free-utility-tools-run`, changed only `resume-scanner/index.html` and `tests/test_navigation.py`; pre-existing untracked project-control files were preserved.
- Commit `686af4644d9ff2e2b65926b7e31f4083d1562abb` tokenizes resume text and matches whole normalized words, so `java` is no longer falsely found inside `javascript`; an empty meaningful-keyword set now produces an actionable message rather than `NaN%`.
- RED contract failed before implementation; fresh GREEN canonical suite passed 4/4; `git diff --check` passed. Node VM behavior check verified job keywords `[java, sql]`, resume `JavaScript SQL` finds only `sql`, and stop-word-only input yields zero keywords.
- Published to `main`; live `/resume-scanner/` returned HTTP 200 and served all new matching/guard contracts on deployment poll 7 (7,797 bytes).
- No deletion, indexing/crawler, outreach, spending, account, pricing/payment, legal-policy, analytics, affiliate, or ad change. Traffic, tool usage, conversions, sales, and revenue remain unverified.
- Release state: **published and live production verified**.

## Next highest-value task
Audit remaining calculator/word-counter/PDF tool correctness and privacy claims; assess privacy-safe aggregate measurement only if an authorized destination and matching disclosure exist.

### 2026-08-24 — Base64 Unicode correctness repair
- **Purpose gate:** This artifact serves developers and multilingual users by making Base64 text encoding/decoding work for UTF-8 text rather than Latin-1 only, fits developer encoding helpers and truthful measurable usefulness, advances trustworthy tool completion, is not a duplicate of navigation/password/resume repairs, and is supported by RED/GREEN tests, an executable Unicode round-trip, deployment, and live HTML.
- Used detached worktree `/tmp/free-utility-tools-base64.bILfXD` from current `origin/main`; preserved untracked project-control files in the primary checkout.
- Commit `0b7336936e444c47de654ba76bbd28c5c53224f5` changed only `base64-tool/index.html` and `tests/test_navigation.py`.
- Fresh validation: RED test failed against the prior `btoa`/`atob` direct-text implementation; GREEN canonical suite passed 5/5; Node VM verified `Hello 👋 café 漢字` encodes to `SGVsbG8g8J+RiyBjYWbDqSDmvKLlrZc=`, round-trips exactly, and invalid UTF-8 is rejected; `git diff --check` passed.
- GitHub Pages workflow `32697745053` completed successfully. Live `/base64-tool/?release=0b73369` returned HTTP 200 (2,520 bytes) with `TextEncoder` and fatal UTF-8 `TextDecoder`; a random invalid route returned HTTP 404.
- No deletion, indexing/crawler, outreach, spending, account, pricing/payment, legal-policy, analytics, affiliate, or ad change. Traffic, usage, conversion, sales, and revenue remain unverified.
- Release state: **published and live production verified**.

### 2026-08-25 — Word counter empty-line correctness repair
- **Purpose gate:** This artifact serves writers and other word-counter users by keeping the displayed line count at zero after all text is removed, fits privacy-conscious text utilities and truthful measurable usefulness, advances trustworthy tool completion, is not a duplicate of the navigation/password/resume/Base64 repairs, and is supported by source inspection, the current ECMAScript `String.prototype.split` specification, RED/GREEN tests, executable browser-script behavior, deployment, and live HTML evidence.
- Search Console evidence remained unavailable (`search_console_unavailable` in the 2026-08-25 demand queue), so this was a bounded standards-backed freshness/correctness review rather than invented demand.
- Used detached clean worktree `/tmp/free-utility-tools-word-counter.bLMc1v` from current `origin/main`; preserved the primary checkout's untracked project-control files.
- Commit `6b60bffd444be74f5a6a13dcd2122cd154a5e82b` changed only `word-counter/index.html` and `tests/test_navigation.py`. Empty text now reports 0 lines rather than becoming 1 line after an input event.
- RED contract failed before implementation. Fresh GREEN canonical suite passed 6/6; `git diff --check` passed; Node behavior verification passed for empty, one-line, newline, and trailing-newline cases; temporary harness was removed; local HTTP preview returned 200 with the expected title, H1, and guard.
- Official sources checked 2026-08-25: ECMAScript `String.prototype.split` (`https://tc39.es/ecma262/multipage/text-processing.html#sec-string.prototype.split`), Google Search Essentials (`https://developers.google.com/search/docs/essentials`), and spam policies (`https://developers.google.com/search/docs/essentials/spam-policies`), all HTTP 200.
- GitHub Pages build for the exact commit reached `built`. Live `/word-counter/?release=6b60bff` returned HTTP 200 (2,519 bytes), contained the new empty-line guard and not the old unconditional expression, retained the title, H1, and project back link; `sitemap.xml` remained 200 while `robots.txt` and a random invalid route remained 404.
- No deletion, indexing/crawler, sitemap, canonical, outreach, spending, account, pricing/payment, legal-policy, analytics, affiliate, or ad change. Traffic, tool usage, conversion, sales, and revenue remain unverified.
- Release state: **published and live production verified**.

## Next highest-value task
Audit for missing initial-HTML canonicals and ad-unit/CMP readiness without changing protected indexing controls or account configuration; assess aggregate measurement only if an authorized destination and matching disclosure exist.

### 2026-08-26 — Freelance calculator input and tax-boundary repair
- **Purpose gate:** This artifact serves freelancers using the hourly-rate calculator by rejecting impossible work-capacity inputs and accurately delimiting what the formula includes, fits career and freelance workflow tools plus truthful claims, advances trustworthy tool completion, is not a duplicate of the navigation/password/resume/Base64/word-counter repairs, and is supported by source inspection, RED/GREEN tests, executable behavior, IRS guidance, the HTML standard, and current Google Search policy checks.
- Search Console remained unavailable (`search_console_unavailable`, queue generated 2026-08-26 with data through 2026-08-22), so this was one bounded standards/documentation correctness review; no search demand was invented.
- Used detached clean worktree `/tmp/free-utility-tools-20260826.ktWMm9` from `origin/main` at `6b60bff`; preserved the primary checkout's untracked project-control files.
- Commit `1a49b418d78cd90bfa35765698c86d1746ef491b` changed only `calculators/index.html` and `tests/test_navigation.py`. The calculator now rejects negative salary/expenses, 52 or more weeks off, and zero billable hours; it also states that the baseline excludes personal income and self-employment taxes instead of implying a net/tax-inclusive result.
- RED contract failed before implementation. GREEN canonical suite passed 7/7; `git diff --check` passed; Node behavior verification produced `$79.17` for the defaults and rejected both 52 weeks off and zero billable hours; local preview returned HTTP 200 with the expected H1, tax boundary, and live-result region.
- Current sources checked 2026-08-26 (all HTTP 200): IRS Self-Employed Individuals Tax Center, WHATWG HTML number-input standard, Google Search Essentials, and Google spam policies.
- Commit was pushed to `origin/main`. GitHub Pages build/API commit `1a49b41` remained `building` and Actions run `32984074612` remained queued after repeated polling; GitHub Status simultaneously reported a major Actions outage and degraded Pages performance. The live calculator still served the prior 4,921-byte version, so **production is not yet verified**.
- No deletion, indexing/crawler, sitemap, canonical, outreach, spending, account, pricing/payment, legal-policy, analytics, affiliate, ad, or training-crawler policy change. Traffic, usage, conversion, sales, and revenue remain unverified.
- Release state: **COMPLETED ARTIFACT — validated and pushed; live publication verification blocked by GitHub outage**.

### 2026-08-27 — Calculator deployment reconciliation
- **Purpose gate:** This reconciliation serves freelancers using the hourly-rate calculator by making the already-tested input and tax-boundary repair available on production, fits career and freelance workflow tools plus truthful claims, advances trustworthy tool completion, is not a duplicate artifact because no new site content was created, and is supported by the preserved commit, fresh canonical tests, GitHub Pages build evidence, and exact live-route checks.
- Search Console remained unavailable (`search_console_unavailable`, queue generated 2026-08-27 with data through 2026-08-23); no demand was invented and no second content artifact was started.
- Preserved the dirty primary checkout and validated detached clean worktree `/tmp/free-utility-tools-reconcile.VZjxlt` at exact `origin/main` commit `1a49b418d78cd90bfa35765698c86d1746ef491b`.
- Fresh canonical suite passed 7/7; `git diff --check` passed. The prepared calculator source retained the title, H1, project back link, impossible-capacity guards, personal-tax boundary, and polite live-result region.
- The stale Actions run `32984074612` remained queued, but the Pages API showed the exact commit stuck in `building`. A bounded manual Pages build request returned HTTP 201; the replacement build for the exact commit reached `built` at `2026-08-27T21:57:16Z`.
- Live `/calculators/?release=1a49b41` returned HTTP 200 (5,750 bytes) with the exact new guards, tax-boundary copy, title, H1, `aria-live`, and project back link. Rendered extraction also showed the new explanation and validation text. Homepage, `sitemap.xml`, and `sitemap.txt` returned 200; project `robots.txt` and a random invalid route returned 404; account-root `robots.txt` returned 200.
- AI-discoverability check: the calculator is useful in crawler-readable initial HTML and is internally linked/sitemapped, but has no initial-HTML canonical. This pre-existing protected indexing-control gap was recorded and not changed. Search/user crawler access was not blocked by the verified root robots policy; no indexing, ingestion, citation, or traffic result is claimed.
- Current Google Search Essentials, spam policies, structured-data policies, and official OpenAI/Anthropic/Perplexity crawler documentation were reachable during reconciliation. No crawler, sitemap, canonical, structured-data, training-crawler, ad, analytics, account, pricing, outreach, spending, legal-policy, deletion, or site-source change was made.
- Release state: **COMPLETED ARTIFACT — published and live production verified** (reconciliation of the 2026-08-26 artifact).

### 2026-08-28 — PDF merger privacy and usability repair
- **Purpose gate:** This artifact serves privacy-conscious users needing to merge PDFs by providing a 100% local, stable, and usable tool, fits developer encoding and security helpers plus career workflow pillars, advances trustworthy tool completion, is not a duplicate of prior repairs, and is supported by source inspection, RED/GREEN trust tests, executable behavior verification, and live HTML evidence.
- Used detached clean worktree `/tmp/free-utility-tools-pdf.0TF0ya` from `origin/main` at `dd8f79d`; preserved the primary checkout's untracked project-control files.
- Commit `dd8f79d` changed `pdf-tools/index.html` and `tests/test_navigation.py`.
- Pinned `pdf-lib` version to `1.17.1` for stability and added a "Clear All" button to the UI.
- Added `PdfMergerTrustTests` to verify the "100% Local" claim by checking for the absence of server-side upload destinations and confirming the presence of the new usability feature.
- Fresh validation: GREEN canonical suite passed 8/8; `git diff --check` passed. Verified no `form action`, `fetch`, or `XMLHttpRequest` in the PDF tool source.
- Live `/pdf-tools/` returned HTTP 200 and served the pinned library version and "Clear All" button on deployment poll 4 (6,675 bytes).
- No deletion, indexing/crawler, sitemap, canonical, outreach, spending, account, pricing/payment, legal-policy, analytics, affiliate, ad, or training-crawler policy change. Traffic, usage, conversion, sales, and revenue remain unverified.
- Release state: **COMPLETED ARTIFACT — published and live production verified**.

### 2026-08-29 — GitHub repository referral path reconciliation
- **Purpose gate:** This artifact serves developers and other GitHub repository visitors by giving them a direct, attributable path to the visitor-facing tools, fits clear navigation and measurable tool usefulness, advances qualified discovery, is not a duplicate of the on-site portfolio-referral CTA because it starts on the public repository surface, and is supported by commit, rendered GitHub HTML, raw README, and destination checks.
- Anti-churn pivot: after repeated on-site tool-correctness releases, this run completed a different action class—an owned, public acquisition/referral surface. It did not create another tool repair.
- Reconciled new remote commit `b8cd25240414fbb138a10e8977e7104844903129` (`docs: add live site visitor path`), which adds only `README.md`. The dirty primary checkout remained untouched and six commits behind `origin/main`; local untracked project-control files were preserved.
- Verified the public repository returned HTTP 200, rendered the heading `Visit the live site`, and contained the exact encoded link to `https://entempsllc.github.io/free-utility-tools/?utm_source=github.com&utm_medium=repository_referral&utm_campaign=repository_readme`.
- Verified the exact UTM destination returned HTTP 200, retained the query string, rendered the `Free Utility Tools` H1, and contained links to all six tools.
- Current official Google Search Essentials, spam policies, and people-first guidance were checked on 2026-08-29. This is a descriptive owned-surface navigation link, not paid or manipulative link building.
- Search Console remains unavailable (`missing_access`; demand queue generated 2026-08-29, data through 2026-08-25). Complete 7-day and 28-day clicks/impressions are therefore unavailable, and no click, human visit, ranking, conversion, or revenue is claimed. Earliest release-inclusive windows can only be evaluated after access exists and reporting delay has elapsed.
- No site-source, indexing/crawler, sitemap, canonical, account, analytics, outreach, spending, pricing/payment, legal-policy, affiliate, ad, deletion, or external-submission change was made in this run.
- Release state: **public GitHub referral surface and live destination verified; traffic measurement blocked**.

## Next highest-value task
Obtain read-only Search Console access for this property and measure the complete site baseline plus the repository-referral landing URL. If access remains unavailable, audit and narrowly correct the homepage's broad privacy wording without changing protected policy or indexing controls.
