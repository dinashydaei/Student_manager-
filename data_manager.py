import json

DATA_FILE = "students.json"

def load_students():
    """برمی‌گردونه: list از dict"""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("⚠ فایل داده خراب بود، لیست جدید ساخته شد")
        return []

def save_students(students):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=2)

def get_unique_names(students):
    """با Set اسم‌های یکتا برمی‌گرده"""
    return {s["name"] for s in students}