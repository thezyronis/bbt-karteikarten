"""BBT Karteikarten – Lernen in Levels mit Streamlit.

Start lokal:  streamlit run app.py
"""
import json
import random

import streamlit as st

from cards import CARDS, LEVELS

st.set_page_config(page_title="BBT Karteikarten", page_icon="🏗️", layout="centered")

CARD_BY_ID = {c["id"]: c for c in CARDS}
NEED_NORMAL = 2   # so oft hintereinander „Gewusst“, damit eine Karte im Level sitzt
NEED_FINAL = 1    # in der Abschlussprüfung reicht einmal (Fehler setzen zurück)


# ---------- Zustand ----------
def init_state():
    ss = st.session_state
    ss.setdefault("streak", {})       # "levelIndex-cardId" -> Anzahl Treffer in Folge
    ss.setdefault("unlocked", 0)      # höchstes freigeschaltetes Level (Index)
    ss.setdefault("level", 0)         # aktuell gewähltes Level
    ss.setdefault("current", None)    # aktuelle Karten-ID
    ss.setdefault("revealed", False)
    ss.setdefault("last", None)
    ss.setdefault("just_cleared", None)


def need(level_idx):
    return NEED_FINAL if level_idx == len(LEVELS) - 1 else NEED_NORMAL


def key(level_idx, card_id):
    return f"{level_idx}-{card_id}"


def streak(level_idx, card_id):
    return st.session_state.streak.get(key(level_idx, card_id), 0)


def open_cards(level_idx):
    return [i for i in LEVELS[level_idx]["ids"] if streak(level_idx, i) < need(level_idx)]


def level_progress(level_idx):
    ids = LEVELS[level_idx]["ids"]
    n = need(level_idx)
    points = sum(min(streak(level_idx, i), n) for i in ids)
    return points / (len(ids) * n)


def level_cleared(level_idx):
    return not open_cards(level_idx)


def pick_card(level_idx):
    pool = open_cards(level_idx)
    if not pool:
        return None
    choices = [i for i in pool if i != st.session_state.last] or pool
    return random.choice(choices)


def answer(correct):
    ss = st.session_state
    lvl, cid = ss.level, ss.current
    k = key(lvl, cid)
    ss.streak[k] = ss.streak.get(k, 0) + 1 if correct else 0
    ss.last = cid
    ss.current = None
    ss.revealed = False
    if level_cleared(lvl):
        ss.just_cleared = lvl
        if lvl == ss.unlocked and lvl < len(LEVELS) - 1:
            ss.unlocked = lvl + 1


def go_level(idx):
    ss = st.session_state
    ss.level = idx
    ss.current = None
    ss.revealed = False
    ss.just_cleared = None


def reset_level(idx):
    for i in LEVELS[idx]["ids"]:
        st.session_state.streak.pop(key(idx, i), None)
    go_level(idx)


def reset_all():
    for k in ["streak", "unlocked", "level", "current", "revealed", "last", "just_cleared"]:
        st.session_state.pop(k, None)
    init_state()


init_state()
ss = st.session_state


# ---------- Seitenleiste: Levels & Fortschritt ----------
with st.sidebar:
    st.header("Levels")
    for idx, lvl in enumerate(LEVELS):
        locked = idx > ss.unlocked
        done = level_cleared(idx)
        icon = "🔒" if locked else ("✅" if done else ("▶️" if idx == ss.level else "📘"))
        if st.button(f"{icon} {lvl['name']}", key=f"lvl{idx}", disabled=locked,
                     use_container_width=True):
            go_level(idx)
            st.rerun()
        if not locked:
            st.progress(level_progress(idx))

    st.divider()
    st.caption(f"Ein Level gilt als geschafft, wenn du jede Karte **{NEED_NORMAL}× hintereinander** "
               "gewusst hast. „Nochmal“ setzt die Karte zurück.")

    st.divider()
    st.subheader("Fortschritt sichern")
    st.caption("Streamlit vergisst den Stand beim Neuladen. Speichere ihn als Datei und lade ihn später wieder.")
    st.download_button(
        "💾 Fortschritt herunterladen",
        data=json.dumps({"streak": ss.streak, "unlocked": ss.unlocked}),
        file_name="bbt_fortschritt.json",
        mime="application/json",
        use_container_width=True,
    )
    up = st.file_uploader("Fortschritt laden", type="json", label_visibility="collapsed")
    if up is not None and st.button("📂 Laden", use_container_width=True):
        try:
            data = json.load(up)
            ss.streak = {str(k): int(v) for k, v in data.get("streak", {}).items()}
            ss.unlocked = min(int(data.get("unlocked", 0)), len(LEVELS) - 1)
            go_level(ss.unlocked)
            st.rerun()
        except (ValueError, TypeError, AttributeError):
            st.error("Die Datei ist kein gültiger Fortschritt. Bitte eine bbt_fortschritt.json wählen.")

    if st.button("↺ Alles zurücksetzen", use_container_width=True):
        reset_all()
        st.rerun()


# ---------- Hauptbereich ----------
lvl_idx = ss.level
lvl = LEVELS[lvl_idx]

st.title("BBT Karteikarten")
st.subheader(lvl["name"])
st.caption(lvl["goal"])
st.progress(level_progress(lvl_idx),
            text=f"{len(lvl['ids']) - len(open_cards(lvl_idx))} von {len(lvl['ids'])} Karten sitzen")

# Level geschafft
if level_cleared(lvl_idx):
    if ss.just_cleared == lvl_idx:
        st.balloons()
        ss.just_cleared = None
    if lvl_idx == len(LEVELS) - 1:
        st.success("🏆 Abschlussprüfung bestanden! Du hast alle 17 Karten drauf. Viel Erfolg in der Klausur!")
    else:
        st.success(f"Level geschafft! **{LEVELS[lvl_idx + 1]['name']}** ist freigeschaltet.")
        if st.button(f"Weiter zu {LEVELS[lvl_idx + 1]['name']} →", type="primary",
                     use_container_width=True):
            go_level(lvl_idx + 1)
            st.rerun()
    if st.button("Dieses Level wiederholen", use_container_width=True):
        reset_level(lvl_idx)
        st.rerun()
    st.stop()

# Karte ziehen
if ss.current is None or ss.current not in open_cards(lvl_idx):
    ss.current = pick_card(lvl_idx)
card = CARD_BY_ID[ss.current]
s = streak(lvl_idx, card["id"])
n = need(lvl_idx)

with st.container(border=True):
    st.caption(f"{card['topic'].upper()} · FRAGE {card['id']} · "
               + ("⭐" * s + "☆" * (n - s)))
    st.markdown(f"### {card['q']}")

    if not ss.revealed:
        st.info("Erst selbst antworten – laut oder auf Papier. Skizzen immer zeichnen!")
        if st.button("Antwort zeigen", type="primary", use_container_width=True):
            ss.revealed = True
            st.rerun()
    else:
        st.divider()
        if card.get("a"):
            st.markdown(card["a"])
        if card.get("sketch"):
            st.markdown(card["sketch"], unsafe_allow_html=True)
        if card.get("a2"):
            st.markdown(card["a2"])

        st.divider()
        st.write("**Wie lief's?**")
        c1, c2 = st.columns(2)
        if c1.button("🔁 Nochmal", use_container_width=True):
            answer(False)
            st.rerun()
        if c2.button("✅ Gewusst", type="primary", use_container_width=True):
            answer(True)
            st.rerun()
