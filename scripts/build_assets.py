#!/usr/bin/env python3
from pathlib import Path
import html

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
ACCENT = '#F0FFF0'
BG = '#050807'
PANEL = '#09100d'
MUTED = '#9fb0a5'
GRID = '#24312a'


def esc(s): return html.escape(s)

def write(path, s):
    (ASSETS / path).write_text(s, encoding='utf-8')


def terminal_card():
    rows = (ASSETS / 'ascii-portrait.txt').read_text(encoding='utf-8').splitlines()
    # crop/truncate to fit left console
    rows = [r[:68] for r in rows[:34]]
    lines=[]
    y=64
    for r in rows:
        lines.append(f'<text x="42" y="{y}" class="ascii">{esc(r)}</text>')
        y += 12
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="560" viewBox="0 0 1200 560">
<defs>
  <pattern id="grid" width="16" height="16" patternUnits="userSpaceOnUse"><path d="M16 0H0V16" fill="none" stroke="{GRID}" stroke-width="0.6" opacity="0.35"/></pattern>
  <linearGradient id="fade" x1="0" x2="1"><stop offset="0" stop-color="{BG}"/><stop offset="1" stop-color="{PANEL}"/></linearGradient>
</defs>
<rect width="1200" height="560" rx="14" fill="url(#fade)"/>
<rect width="1200" height="560" rx="14" fill="url(#grid)"/>
<rect x="1" y="1" width="1198" height="558" rx="13" fill="none" stroke="{ACCENT}" stroke-opacity="0.75"/>
<line x1="22" y1="38" x2="1178" y2="38" stroke="{ACCENT}" stroke-opacity="0.55"/>
<circle cx="42" cy="20" r="4" fill="{ACCENT}"/><circle cx="57" cy="20" r="4" fill="{ACCENT}" opacity="0.45"/><circle cx="72" cy="20" r="4" fill="{ACCENT}" opacity="0.25"/>
<text x="93" y="25" class="tiny">sayem@github:~ / profile.signal</text>
<g>{''.join(lines)}</g>
<line x1="692" y1="56" x2="692" y2="520" stroke="{ACCENT}" stroke-opacity="0.28"/>
<text x="735" y="88" class="label">01 / IDENTITY</text>
<text x="735" y="138" class="name">SAYEM AHMED</text>
<text x="735" y="178" class="name">SHAYEED</text>
<text x="735" y="218" class="tag">I BUILD SOFTWARE THAT FEELS OBVIOUS.</text>
<text x="735" y="254" class="body">Mobile · Full Stack · Automation · UI/UX · AI</text>
<text x="735" y="300" class="body muted">Designing interfaces. Automating boring things.</text>
<text x="735" y="327" class="body muted">Chasing stars after dark.</text>
<rect x="735" y="366" width="412" height="72" rx="8" fill="none" stroke="{ACCENT}" stroke-opacity="0.35"/>
<text x="758" y="392" class="label">CURRENTLY BUILDING</text>
<text x="758" y="420" class="body">SoundFlow / privacy-first desktop dictation</text>
<text x="735" y="476" class="quote">“When I am not coding, you'll find me looking at the stars.”</text>
<text x="735" y="510" class="tiny">SYLHET · BANGLADESH   //   BUILD · LEARN · EXPLORE · REPEAT</text>
<style>
.ascii{{font: 10px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;fill:{ACCENT};white-space:pre;opacity:.88}}
.tiny{{font:12px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;fill:{MUTED};letter-spacing:.8px}}
.label{{font:700 14px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;fill:{ACCENT};letter-spacing:1.8px}}
.name{{font:700 34px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;fill:{ACCENT};letter-spacing:2px}}
.tag{{font:700 16px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;fill:{ACCENT};letter-spacing:1.1px}}
.body{{font:15px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;fill:{ACCENT}}}
.muted{{fill:{MUTED}}}.quote{{font:italic 14px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;fill:{MUTED}}}
</style>
</svg>'''
    write('profile-terminal.svg', svg)


def project_card(filename, index, title, subtitle, lines, tech):
    chips=[]; x=34
    for t in tech:
        w=17+len(t)*8
        chips.append(f'<rect x="{x}" y="218" width="{w}" height="27" rx="5" fill="none" stroke="{ACCENT}" stroke-opacity="0.45"/><text x="{x+9}" y="236" class="chip">{esc(t)}</text>')
        x += w+10
    desc=''.join(f'<text x="34" y="{126+i*26}" class="body">{esc(line)}</text>' for i,line in enumerate(lines))
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="570" height="280" viewBox="0 0 570 280">
<rect width="570" height="280" rx="12" fill="{BG}"/><rect x="1" y="1" width="568" height="278" rx="11" fill="none" stroke="{ACCENT}" stroke-opacity="0.58"/>
<text x="34" y="43" class="label">0{index} / SELECTED WORK</text><line x1="190" y1="38" x2="536" y2="38" stroke="{ACCENT}" stroke-opacity="0.35"/>
<text x="34" y="84" class="title">{esc(title)}</text><text x="536" y="84" class="arrow">↗</text>
<text x="34" y="104" class="sub">{esc(subtitle)}</text>{desc}{''.join(chips)}
<text x="34" y="265" class="foot">OPEN REPOSITORY //</text>
<style>.label{{font:700 12px ui-monospace,monospace;fill:{ACCENT};letter-spacing:1.3px}}.title{{font:700 27px ui-monospace,monospace;fill:{ACCENT}}}.sub{{font:12px ui-monospace,monospace;fill:{MUTED}}}.body{{font:14px ui-monospace,monospace;fill:{ACCENT}}}.chip{{font:11px ui-monospace,monospace;fill:{ACCENT}}}.foot{{font:10px ui-monospace,monospace;fill:{MUTED};letter-spacing:1px}}.arrow{{font:28px ui-monospace,monospace;fill:{ACCENT};text-anchor:end}}</style>
</svg>'''
    write(filename, svg)


def music_card():
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="760" height="250" viewBox="0 0 760 250">
<defs><pattern id="grid" width="14" height="14" patternUnits="userSpaceOnUse"><path d="M14 0H0V14" fill="none" stroke="{GRID}" stroke-width=".55" opacity=".32"/></pattern></defs>
<rect width="760" height="250" rx="12" fill="{BG}"/><rect width="760" height="250" rx="12" fill="url(#grid)"/><rect x="1" y="1" width="758" height="248" rx="11" fill="none" stroke="{ACCENT}" stroke-opacity=".62"/>
<text x="28" y="36" class="label">05 / NOW PLAYING</text><line x1="184" y1="31" x2="730" y2="31" stroke="{ACCENT}" stroke-opacity=".3"/>
<rect x="30" y="65" width="112" height="112" rx="6" fill="{PANEL}" stroke="{ACCENT}" stroke-opacity=".4"/>
<rect x="56" y="92" width="60" height="60" rx="3" fill="none" stroke="{ACCENT}" stroke-width="2"/><text x="86" y="128" class="album" text-anchor="middle">1975</text>
<text x="175" y="92" class="title">About You</text><text x="175" y="119" class="artist">The 1975</text>
<line x1="175" y1="151" x2="690" y2="151" stroke="{MUTED}" stroke-opacity=".4" stroke-width="4"/><line x1="175" y1="151" x2="427" y2="151" stroke="{ACCENT}" stroke-width="4"/><circle cx="427" cy="151" r="6" fill="{ACCENT}"/>
<text x="175" y="176" class="time">02:24</text><text x="690" y="176" class="time" text-anchor="end">05:26</text>
<circle cx="455" cy="200" r="25" fill="none" stroke="{ACCENT}" stroke-width="2"/><path d="M449 188L468 200L449 212Z" fill="{ACCENT}"/>
<text x="175" y="219" class="hint">CLICK CARD TO PLAY ON SPOTIFY</text>
<style>.label{{font:700 12px ui-monospace,monospace;fill:{ACCENT};letter-spacing:1.5px}}.title{{font:700 27px ui-monospace,monospace;fill:{ACCENT}}}.artist{{font:16px ui-monospace,monospace;fill:{MUTED}}}.album{{font:700 14px ui-monospace,monospace;fill:{ACCENT}}}.time{{font:11px ui-monospace,monospace;fill:{MUTED}}}.hint{{font:10px ui-monospace,monospace;fill:{MUTED};letter-spacing:1px}}</style>
</svg>'''
    write('now-playing.svg', svg)


def quote_card():
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="760" height="180" viewBox="0 0 760 180">
<rect width="760" height="180" rx="12" fill="{BG}"/><rect x="1" y="1" width="758" height="178" rx="11" fill="none" stroke="{ACCENT}" stroke-opacity=".5"/>
<text x="30" y="37" class="label">06 / HUMAN MODE</text><text x="35" y="86" class="quote">Still learning.</text><text x="35" y="113" class="quote">Still building.</text><text x="35" y="140" class="quote">Still looking at the stars.</text>
<text x="720" y="145" class="moon" text-anchor="end">☾ · · ✦</text>
<style>.label{{font:700 12px ui-monospace,monospace;fill:{ACCENT};letter-spacing:1.5px}}.quote{{font:18px ui-monospace,monospace;fill:{ACCENT}}}.moon{{font:26px ui-monospace,monospace;fill:{MUTED}}}</style></svg>'''
    write('human-mode.svg', svg)

if __name__ == '__main__':
    terminal_card()
    project_card('project-soundflow.svg',1,'SoundFlow','PRIVACY-FIRST DESKTOP DICTATION',[
        'Local speech-to-text for Linux and Windows.','Whisper inference, system shortcuts, exports,','Wayland integration, themes, and optional AI polish.'
    ], ['Python','faster-whisper','Qt'])
    project_card('project-sadstt.svg',2,'SadSTT','FLUTTER × NATIVE ANDROID SPEECH',[
        'Speech-to-text across Flutter and Android.','Kotlin services, IME/accessibility integration,','continuous listening, overlays, and multilingual UX.'
    ], ['Flutter','Kotlin','Android'])
    music_card()
    quote_card()
