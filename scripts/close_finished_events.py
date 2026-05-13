#!/usr/bin/env python3
"""Close finished course and meeting pages based on front matter dates."""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path
from zoneinfo import ZoneInfo


TARGET_DIRS = (
    Path("pages/training_courses"),
    Path("pages/meetings_workshops"),
)

DATE_RE = re.compile(r'^(startDate|endDate):\s*["\']?(\d{4}-\d{2}-\d{2})["\']?\s*$', re.MULTILINE)
TOP_LEVEL_STATE_RE = re.compile(r"^state:\s*([A-Za-z_-]+)\s*$", re.MULTILINE)
EVENT_STATE_RE = re.compile(r"^(\s+state:\s*)([A-Za-z_-]+)(\s*)$", re.MULTILINE)
TYPE_RE = re.compile(r"^type:\s*.+$", re.MULTILINE)


def today_in_rome() -> dt.date:
    return dt.datetime.now(ZoneInfo("Europe/Rome")).date()


def parse_front_matter(text: str) -> tuple[str, str, str] | None:
    if not text.startswith("---"):
        return None

    first_end = text.find("\n")
    if first_end == -1:
        return None

    second_marker = text.find("\n---", first_end + 1)
    if second_marker == -1:
        return None

    marker_end = text.find("\n", second_marker + 1)
    if marker_end == -1:
        marker_end = len(text)

    prefix = text[: first_end + 1]
    front_matter = text[first_end + 1 : second_marker]
    suffix = text[second_marker:marker_end] + text[marker_end:]
    return prefix, front_matter, suffix


def page_end_date(front_matter: str) -> dt.date | None:
    dates: dict[str, dt.date] = {}
    for key, value in DATE_RE.findall(front_matter):
        dates[key] = dt.date.fromisoformat(value)

    return dates.get("endDate") or dates.get("startDate")


def close_front_matter(front_matter: str) -> tuple[str, bool]:
    changed = False

    state_match = TOP_LEVEL_STATE_RE.search(front_matter)
    if state_match:
        if state_match.group(1) != "closed":
            front_matter = TOP_LEVEL_STATE_RE.sub("state: closed", front_matter, count=1)
            changed = True
    else:
        type_match = TYPE_RE.search(front_matter)
        insert_at = type_match.end() if type_match else 0
        front_matter = front_matter[:insert_at] + "\nstate: closed" + front_matter[insert_at:]
        changed = True

    def close_event_state(match: re.Match[str]) -> str:
        nonlocal changed
        if match.group(2) == "closed":
            return match.group(0)
        changed = True
        return f"{match.group(1)}closed{match.group(3)}"

    front_matter = EVENT_STATE_RE.sub(close_event_state, front_matter)
    return front_matter, changed


def close_file(path: Path, today: dt.date, dry_run: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    parsed = parse_front_matter(text)
    if not parsed:
        return False

    prefix, front_matter, suffix = parsed
    end_date = page_end_date(front_matter)
    if not end_date or end_date >= today:
        return False

    updated_front_matter, changed = close_front_matter(front_matter)
    if not changed:
        return False

    if not dry_run:
        path.write_text(prefix + updated_front_matter + suffix, encoding="utf-8", newline="")

    print(f"Closed {path} (ended {end_date.isoformat()})")
    return True


def iter_target_pages() -> list[Path]:
    pages: list[Path] = []
    for target_dir in TARGET_DIRS:
        pages.extend(sorted(target_dir.glob("*.md")))
    return pages


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Report changes without writing files.")
    parser.add_argument("--today", help="Override today's date in YYYY-MM-DD format.")
    args = parser.parse_args()

    today = dt.date.fromisoformat(args.today) if args.today else today_in_rome()
    closed_count = sum(close_file(path, today, args.dry_run) for path in iter_target_pages())

    if closed_count == 0:
        print("No pages to close.")
    else:
        print(f"Closed {closed_count} page(s).")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
