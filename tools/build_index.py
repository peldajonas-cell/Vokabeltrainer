#!/usr/bin/env python3
"""Erzeugt index.html (Website) aus src/app.html (Quelle, auch für die Claude-Seite)."""
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
HEAD = """<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Wortkasten">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<link rel="apple-touch-icon" href="icon.png">
<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>
</head>
<body>
"""
app = (ROOT / "src" / "app.html").read_text(encoding="utf-8")
(ROOT / "index.html").write_text(HEAD + app + "\n</body>\n</html>\n", encoding="utf-8")
print("index.html gebaut")
