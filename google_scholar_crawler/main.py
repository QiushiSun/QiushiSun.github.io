from scholarly import scholarly, ProxyGenerator
import json
from datetime import datetime
import os

# GitHub Actions runner IPs are blocked by Google Scholar's captcha. Route
# scholarly's HTTP calls through a rotating pool of free proxies so the
# scrape has a fighting chance. FreeProxies() returns False if no working
# proxy was found, in which case we still try a direct connection (which
# usually fails — but the step has a hard timeout, so we won't hang).
pg = ProxyGenerator()
if pg.FreeProxies():
    scholarly.use_proxy(pg)

author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
# Only fetch the lightweight sections — 'publications' is what gets us
# rate-limited, and we don't actually use it for the citations badge.
scholarly.fill(author, sections=['basics', 'indices', 'counts'])
author['updated'] = str(datetime.now())
print(json.dumps({'citedby': author.get('citedby'), 'updated': author['updated']}))

os.makedirs('results', exist_ok=True)
with open('results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
    'schemaVersion': 1,
    'label': 'citations',
    'message': f"{author['citedby']}",
}
with open('results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
