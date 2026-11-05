# Asian Workshop on Scientific Machine Learning 2027

A Markdown-based Jekyll website for a workshop planned for **26–28 April 2027** at **ACROS Fukuoka, Fukuoka, Japan**.

**[日本語の編集・公開ガイド](README_JA.md)**

## Run locally

Use a current Ruby 3.3 patch release and Bundler 2.6.9. The included lockfile resolves Jekyll 4.4.1 and requires **Ruby 3.2 or later in the 3.x series**; Ruby 3.3.9 was used for the verified build. Check `ruby -v` in the same terminal where you will run Bundler. See the [Jekyll installation guide](https://jekyllrb.com/docs/installation/) for your operating system.

From the project directory:

```sh
gem install bundler -v 2.6.9
bundle _2.6.9_ install
bundle _2.6.9_ exec jekyll serve
```

Open <http://localhost:4000/>. Restart Jekyll after changing `_config.yml`.

To build static files:

```sh
bundle exec jekyll build
```

The result is written to `_site/`. Edit the source files and rebuild; direct edits to `_site/` are overwritten by the next build. Ruby is needed to build the site; the resulting website only needs static hosting.

If this package includes a prebuilt `preview/` directory, view that version without Ruby:

```sh
python3 -m http.server 8000 --directory preview
```

Open <http://localhost:8000/>. The prebuilt preview is a snapshot; rebuild Jekyll to see subsequent source edits. Use an HTTP server for the directory-style page URLs; opening files directly with `file://` does not guarantee that every link works.

### If installing `public_suffix 7.0.5` fails

The final dependency trace alone does not identify the cause. First check:

```sh
ruby -v
gem --version
bundle -v
command -v ruby
command -v bundle
```

`public_suffix 7.0.5` and `sass-embedded 1.105.2` both require Ruby >= 3.2. If the active Ruby is older, select a current Ruby 3.3 release in your version manager, then install Bundler 2.6.9 using that Ruby. Downgrading `public_suffix` alone does not make this lockfile compatible with Ruby 3.1.

For an existing, configured rbenv + ruby-build installation, the following example uses Ruby 3.3.12, listed by the Ruby project as a 3.3 release as of 21 October 2026. Run it from the site directory:

```sh
rbenv install -s 3.3.12
rbenv local 3.3.12
ruby -v
gem install bundler -v 2.6.9
bundle _2.6.9_ install
bundle _2.6.9_ exec jekyll serve
```

Confirm that `ruby -v` now reports the selected version. Keep the existing lockfile. If Ruby is already suitable, inspect the first error preceding the dependency trace: permissions, certificates and download failures require different fixes. The Ruby declaration in `Gemfile` reports an incompatible interpreter early; it does not install or switch Ruby.

Primary references: [public_suffix 7.0.5 requirements](https://rubygems.org/gems/public_suffix/versions/7.0.5), [sass-embedded 1.105.2 requirements](https://rubygems.org/gems/sass-embedded/versions/1.105.2), [Ruby releases](https://www.ruby-lang.org/en/downloads/releases/), [rbenv](https://github.com/rbenv/rbenv).

## Edit content

| File | Purpose |
| --- | --- |
| `index.md` | Workshop overview |
| `programme.md` | Programme information |
| `participation.md` | Registration, contributions and contact information |
| `venue.md` | Venue and travel information |
| `_data/conference.yml` | Shared name, dates, venue, contact and calendar metadata |
| `_data/programme.yml` | Planned dates and programme status |
| `_data/announcements.yml` | Dated announcements |
| `_data/topics.yml` | Editable research-area descriptions |
| `_data/navigation.yml` | Menu labels and page paths |
| `_data/photo.yml` | Photograph path within `assets_path`, alt text and attribution |
| `assets/css/main.css` | Typography, layout, mobile and print styles; default asset directory |
| `_config.yml` | Site metadata, `assets_path` and deployment URL |
| `_includes/local-url.html`, `_includes/asset-url.html` | Page-relative internal links and asset references |

The organiser supplied the conference name, planned dates and venue. The short navigation name and research-area descriptions are editorial starting points. Set `show_topics: false` in `_data/conference.yml` to hide the latter until the scope is confirmed. `contact_email: ""` hides the sidebar contact section. No organisers, sponsors, speakers, fees or deadlines have been invented.

The calendar event is tentative. Keep its `calendar_uid` stable after distribution, update `calendar_updated_utc` when revising it, and preserve the exclusive all-day end date: **29 April 2027** represents an event ending on **28 April**. See the Japanese guide for the complete update procedure.

## Relative paths and the asset directory

Normal pages use page-relative references for CSS, favicon, photographs, the calendar and internal links. With the default `assets_path: "assets"`, the CSS URL is `./assets/css/main.css` on the home page, `../assets/css/main.css` on a page such as `/programme/`, and `../../assets/css/main.css` on a page two directories deep. These links follow the site's location when its directory structure is moved together.

Serve directory pages with their trailing slash, such as `/programme/`, or with an explicit `index.html`. A static server should redirect `/programme` to `/programme/`, as the standard Jekyll server does.

Use the supplied Liquid includes for new links; no Jekyll plugin is required:

```liquid
[Programme]({% include local-url.html path='/programme/' %})
![ACROS Fukuoka]({% include asset-url.html path='images/acros-fukuoka-2011.jpg' %})
```

`assets_path` is a directory reference relative to the generated site's root. It sets the URL location and does **not** move or copy files. To rename the directory:

```sh
mv assets static
```

Then set this in `_config.yml` and rebuild:

```yaml
assets_path: "./static"
```

No template changes are needed. `static/` and nested paths such as `static/files` are also supported. For a path outside the site, such as `../shared/static`, build first, then place the generated asset files at that location on the server yourself. Use the generated calendar file: its source contains Liquid expressions that Jekyll must expand. The photograph's `_data/photo.yml` entry remains `path: images/acros-fukuoka-2011.jpg`, relative to `assets_path`.

Normal local links do not use `baseurl`. Keep `url` and `baseurl` set to the actual public location for canonical/OG metadata and the 404 page. `404.md` uses `root_relative_urls: true`, so it can link back correctly even when displayed for an unknown deeply nested URL. Restart `jekyll serve` after changing `_config.yml`.

## Publish with GitHub Pages

1. Create your own repository and place the project contents at its root, including `.github/workflows/pages.yml` and `Gemfile.lock`.
2. Use `main` as the default branch, or update the branch in the workflow.
3. In **Settings → Pages → Build and deployment → Source**, select **GitHub Actions**.
4. Push to `main`, or run the workflow from the **Actions** tab.

The supplied workflow builds with Ruby 3.3 and the lockfile, then deploys `_site/`. It takes `url` and `baseurl` from GitHub Pages metadata, including repository subpaths and configured custom domains. No repository is created by this package.

For another static host, set `url` to the origin and `baseurl` to the public path prefix in `_config.yml` for metadata and 404 links, run `bundle exec jekyll build`, and publish the contents of `_site/`. Preserve the relative placement of pages and assets. Ordinary page links and assets then follow the site's directory even if it is deployed under a different subdirectory; update the public URL settings and rebuild when the production location changes. See [GitHub Pages custom workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) and [Jekyll documentation](https://jekyllrb.com/docs/).

## Assets and sources

The venue photo is **Kenta Mabuchi, *ACROS Fukuoka 2011***, licensed **CC BY-SA 2.0**. Keep the visible attribution and licence links. Full provenance is in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

- [Official venue access](https://www.acros.or.jp/english/access/)
- [Photograph on Wikimedia Commons](https://commons.wikimedia.org/wiki/File:ACROS_Fukuoka_2011.jpg)
- [CC BY-SA 2.0 licence](https://creativecommons.org/licenses/by-sa/2.0/)

The site uses system fonts and plain HTML/CSS, with mobile and print styles. It does not require JavaScript or a front-end framework.
