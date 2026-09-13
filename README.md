<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/LabbeSimon/LabbeSimon/main/banner-dark.svg">
  <img alt="Simon Labbé — take out the part everyone assumes is required, then see what still works." src="https://raw.githubusercontent.com/LabbeSimon/LabbeSimon/main/banner-light.svg" width="100%">
</picture>

France · [simonlabbe.fr](https://simonlabbe.fr) · contact@simonlabbe.fr

**On paper I do marketing and communication** — BUT MMI, currently at ADN Technologies
and president of Sapense SAS. In practice I spend my evenings on a reverse-engineered BLE
protocol and a CMS with no database. I have found that the two jobs are the same one:
figure out what a thing is really for, cut everything that is only there out of habit,
and say plainly what is left. It just happens in a different file format.

---

### Four projects, one habit

Each one removes the piece everyone treats as non-negotiable, then asks what is
actually left to build.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/LabbeSimon/LabbeSimon/main/stats-dark.svg">
  <img alt="G1 Extended: zero accounts, servers or telemetry. CMS: 2 blocking requests before first paint, down from 30. VectorFix: 3000× less storage to cover France. Start Browser: nothing phones home, telemetry and Mozilla services off." src="https://raw.githubusercontent.com/LabbeSimon/LabbeSimon/main/stats-light.svg" width="100%">
</picture>

---

### What I'm building

**[G1 Extended](https://github.com/LabbeSimon/G1_Extended)** — an open-source Android
client for [Even Realities G1](https://www.evenrealities.com) smart glasses, written
against a reverse-engineered BLE protocol: two Nordic UART radios, one per temple.
HUD layouts the official app never exposes, hardware events it throws away, and a path
for your own microcontroller to push lines to the lens. No account, no telemetry,
nothing leaves the phone.
<br><sub>Dart · Flutter · C · BLE — [docs](https://simonlabbe.fr/g1) · [releases](https://github.com/LabbeSimon/G1_Extended/releases)</sub>

**[CMS](https://github.com/LabbeSimon/CMS)** — a PHP CMS for the sites nobody writes
software for: town halls, associations, schools, small practices. Pages, accounts and
config are files, so there is no database to install and no root access to ask for.
The core merges every plugin's CSS and JS into one file each, in an order the plugins
declare themselves — fifteen plugins still cost two blocking requests instead of thirty.
<br><sub>PHP · zero-dependency · file storage</sub>

**VectorFix** *(private · pre-alpha)* — absolute visual localisation for UAVs in
GNSS-denied conditions, matching a nadir camera against **vector map data** rather than
imagery. France in 1–3 GB instead of 5–10 TB, cold start with no position prior,
targeting an ESP32-S3 at roughly half a watt. The core hypothesis is not validated yet,
and the README says so.
<br><sub>C · ESP-IDF · computer vision</sub>

**Start Browser** *(private)* — one browser on two engines: an Android fork of
[FOSS Browser](https://codeberg.org/Gaukler_Faun/FOSS_Browser) and a desktop build of
Gecko from Firefox ESR source. Neither repository carries engine code — the desktop one
is a mozconfig, a branding folder and one stylesheet, and fetches Mozilla's tarball at
build time, so there is no patched copy of Gecko to carry forward at each release. Same
engine, same extensions, same Sync, and a profile directory of its own so it never
touches a Firefox install.
<br><sub>Java · Gecko · CSS — Firefox ESR 153 · fork of FOSS Browser (AGPL-3.0)</sub>

---

### Nothing here phones home

The one default I take out of everything I ship. G1 Extended has no account and no server
to send to — the phone talks to the glasses and stops there. The CMS loads no third-party
script: no CDN, no font host, no analytics tag, so a visitor's browser only ever contacts
the site they typed. Start Browser's branding folder is, literally, the preference file
that switches Mozilla's telemetry, health reports, Shield studies and sponsored content
off, and points the update links at my own releases. VectorFix reads map data that is
already on the device, and has no network code at all.

**It is the goal, not a feature I bolt on at the end** — I want to live without all this
surplus data, mine and anyone else's. Software that collects nothing has nothing to lose,
nothing to sell and nothing to explain, and that is worth more to me than a dashboard of
usage numbers I would never open.

---

### What I write it in

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/LabbeSimon/LabbeSimon/main/langs-dark.svg">
  <img alt="Language mix across my own repositories: Dart 70.9%, PHP 18.9%, CSS 5.1%, Kotlin 1.3%, other 3.7%." src="https://raw.githubusercontent.com/LabbeSimon/LabbeSimon/main/langs-light.svg" width="100%">
</picture>

<sub>Rebuilt every Monday from the GitHub API by
<a href="https://github.com/LabbeSimon/LabbeSimon/blob/main/.github/workflows/refresh-charts.yml">a workflow in this repo</a>,
and served from it — no third-party card service standing between this page and you.
Vendored libraries are excluded, so the bar counts code I actually wrote.</sub>

---

### How I work

Plain READMEs that state what fails as clearly as what works — the VectorFix one opens
with *"the core hypothesis is not yet validated"*, because that is the useful sentence.
Commit messages in the present tense that say what changed and why. A preference for the
version with fewer moving parts, even when it costs more work up front.

The rest of the toolbox: SEO, brand and campaign work, video production and interviews
for the IUT Troyes Web TV, and enough English to ship documentation in it.

<sub>Open to talk — **contact@simonlabbe.fr**</sub>
