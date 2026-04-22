import os

import json
import streamlit.components.v1 as components

GA_MEASUREMENT_ID = os.environ["GA_MEASUREMENT_ID"]

def inject_ga():
    if not GA_MEASUREMENT_ID:
        return

    ga_html = f"""
    <script async src="https://www.googletagmanager.com/gtag/js?id={GA_MEASUREMENT_ID}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', '{GA_MEASUREMENT_ID}', {{
        page_title: 'account_assistant',
        page_path: window.location.pathname
      }});
    </script>
    """
    components.html(ga_html, height=0)

def track_event(event_name: str, params: dict | None = None):
    if not GA_MEASUREMENT_ID:
        return

    params = params or {}
    payload = json.dumps(params)

    event_html = f"""
    <script>
      if (window.parent && window.parent.gtag) {{
        window.parent.gtag('event', '{event_name}', {payload});
      }} else if (window.gtag) {{
        window.gtag('event', '{event_name}', {payload});
      }}
    </script>
    """
    components.html(event_html, height=0)