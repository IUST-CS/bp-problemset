import re
import json
from pathlib import Path
from builder import *

# Functions

def persian (text):
    text = str(text)
    for x, y in zip("1234567890", "۱۲۳۴۵۶۷۸۹۰"):
        text = text.replace(x, y)
    return text

# Metadata

with open("metadata.json", encoding = "utf8") as handler:
    metadata = json.load(handler)

series = {
    item["id"]: item
    for item in metadata["series"]
}

root = Path("problems")
root.mkdir(parents = True, exist_ok = True)

# Problems

class Problem:
    def __init__ (self, path):
        if isinstance(path, Path):
            self.path = path
        else:
            self.path = Path(path)

        if not self.path.exists():
            raise FileNotFoundError(path)

        self.entries = {}

    def parse (self):
        with path.open("r", encoding = "utf8") as handler:
            content = handler.read()
        
        self.entries = re.findall(r'\[\_metadata\_\:(.*?)\]\:\-\s+\"(.*?)\"', content)
        self.entries = dict(self.entries)

        return self.entries

    def rename (self):
        if not self.entries:
            self.parse()
        name = entries["id"] + ".md"
        self.path.rename(path.parent / name)
        self.path = path.parent / name


paths = sorted(root.glob("*.md"))

problems = {}

for path in paths:
    if path.name == "README.md":
        continue
    
    problem = Problem(path)
    entries = problem.parse()

    if entries["series"] not in problems:
        problems[entries["series"]] = []
    problems[entries["series"]].append(entries)

    problem.rename()

# README.md

LEVELS = {
    "easy": "ساده",
    "medium": "متوسط",
    "hard": "سخت"
}

output = ""

output += Heading("بانک سؤالات").render() + "\n\n"

output += Heading("بررسی اجمالی", 2).render() + "\n\n"

table = Table()

table.add_row(
    [
        "شماره",
        "نوع",
        "عنوان",
        "ساده",
        "متوسط",
        "سخت",
        "مجموع",
        ""
    ],
    header = True
)

for i, (id, data) in enumerate(series.items()):
    table.add_row(
        [
            persian(i + 1),
            "سری" if data["type"] == "series" else "بسته جبرانی",
            data["title"]["fa"],
            persian(str(len([x for x in problems.get(data["id"], []) if x["level"] == "easy"]))),
            persian(str(len([x for x in problems.get(data["id"], []) if x["level"] == "medium"]))),
            persian(str(len([x for x in problems.get(data["id"], []) if x["level"] == "hard"]))),
            persian(str(len(problems.get(data["id"], [])))),
            Link("مشاهده", "#" + data["id"]).render()
        ]
    )

output += table.render()

output += "\n\n"

for id, data in series.items():
    mode = "سری" if data["type"] == "series" else "بسته جبرانی"

    problems_count = sum(
        len(y) for x, y in problems.items()
    )

    output += Heading(
        persian(
            mode + " " + str(data["number"]) + ": " + data["title"]["fa"]
        ),
        2,
        {
            "id": data["id"]
        }
    ).render()
    
    output += "\n\n"

    prbs = problems.get(data["id"], [])

    if prbs:
        easy = persian(str(len([x for x in problems.get(data["id"], []) if x["level"] == "easy"])))
        medium = persian(str(len([x for x in problems.get(data["id"], []) if x["level"] == "medium"])))
        hard = persian(str(len([x for x in problems.get(data["id"], []) if x["level"] == "hard"])))

        output += f"برای این {mode}، {easy} سؤال ساده، {medium} سؤال متوسط و {hard} سؤال سخت و مجموعاً " + persian(len(prbs)) + f" سؤال  طرح شده است."
        output += "\n\n"
        table = Table()
        table.add_row(
            [
                "شماره",
                "عنوان",
                "سطح",
                "طراح",
                ""
            ],
            header = True
        )

        def get_level(level):
            if level == "easy":
                return 0
            if level == "medium":
                return 1
            return 2
        
        prbs = sorted(
            sorted(
                sorted(
                    prbs,
                    key = lambda x: x["id"]
                ),
                key = lambda x: x["author"]
            ),
            key = lambda x: get_level(x["level"])
        )

        for i, entries in enumerate(prbs):
            table.add_row(
                [
                    persian(i + 1),
                    entries["title"],
                    LEVELS[entries["level"]],
                    entries["author"],
                    Link("مشاهده", entries["id"] + ".md").render()
                ]
            )

        output += table.render()
    else:
        output += f"تا حالا هیچ سؤالی برای این {mode} طرح نشده است."

with (root / "README.md").open("w", encoding = "utf-8") as handler:
    handler.write(output)