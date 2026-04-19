# Scripts

Helper scripts for the site. Excluded from the Jekyll build (see `_config.yml > exclude`).

## `migrate_old_blog.py`

Migrates selected Hexo posts from `QiushiSun-Blog-old/` into Jekyll's
`_posts/YYYY-MM-DD-slug.md` format and copies referenced images from
`QiushiSun-Blog-old/source/gallery/` into `assets/blog/<slug>/`.

The list of posts to migrate (and their new slugs) is hard-coded in the
`MIGRATE` list inside the script — edit it if you want to add/remove posts.

```bash
python3 scripts/migrate_old_blog.py
```

What it does for each post:

1. Parses the Hexo YAML front matter
2. Rewrites `/gallery/<...>` image paths to `/assets/blog/<slug>/<file>`
3. Strips the Hexo `<!--more-->` excerpt separator
4. Writes a normalized Jekyll front matter (`title`, `date`, `lang: zh`, `categories`, `tags`, `cover`, `excerpt`)
5. Copies referenced images into the new location

Once the original `QiushiSun-Blog-old/` directory is no longer needed, you can
safely remove it from the repo — the migrated posts and assets are
self-contained.
