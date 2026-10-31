from student import Student
from validators import get_valid_name, get_valid_age, get_valid_scores
from data_manager import load_students, save_students, get_unique_names


def show_menu():
    print("\n" + "=" * 35)
    print("   📚 دستیار مدیریت دانشجو")
    print("=" * 35)
    print("1. افزودن دانشجو")
    print("2. نمایش همه")
    print("3. جستجو با نام")
    print("4. حذف دانشجو")
    print("5. معدل کل کلاس")
    print("6. لیست اسم‌های یکتا")
    print("0. خروج")
    print("=" * 35)


def add_student(students):
    try:
        name = get_valid_name()
        age = get_valid_age()
        scores = get_valid_scores()
        students.append(Student(name, age, scores).to_dict())
        save_students(students)
        print(f"✅ '{name}' اضافه شد")
    except ValueError as e:
        print(f"❌ خطا: {e}")


def show_all(students):
    if not students:
        print("📭 لیست خالیه")
        return
    for i, s in enumerate(students, 1):
        st = Student(s["name"], s["age"], s["scores"])
        print(f"{i}. {st}")


def search_student(students):
    query = input("بخشی از نام: ").strip().lower()
    results = [s for s in students if query in s["name"].lower()]
    if not results:
        print("🔍 چیزی پیدا نشد")
        return
    for s in results:
        print("  -", Student(s["name"], s["age"], s["scores"]))


def delete_student(students):
    name = input("نام دقیق برای حذف: ").strip()
    before = len(students)
    students[:] = [s for s in students if s["name"] != name]
    if len(students) < before:
        save_students(students)
        print("🗑 حذف شد")
    else:
        print("❌ چنین دانشجویی نیست")


def class_average(students):
    if not students:
        print("📭 لیست خالیه")
        return
    total = sum(sum(s["scores"]) for s in students)
    count = sum(len(s["scores"]) for s in students)
    print(f"📊 معدل کل: {total / count:.2f}" if count else "نمره‌ای ثبت نشده")


def show_unique_names(students):
    names = get_unique_names(students)
    print(f"👥 {len(names)} اسم یکتا:")
    for n in names:
        print("  -", n)


def main():
    students = load_students()
    actions = {
        "1": add_student, "2": show_all, "3": search_student,
        "4": delete_student, "5": class_average, "6": show_unique_names,
    }

    while True:
        show_menu()
        choice = input("انتخاب: ").strip()
        if choice == "0":
            print("👋 خداحافظ!")
            break
        action = actions.get(choice)
        if action:
            action(students)
        else:
            print("❌ گزینه نامعتبر")


if __name__ == "__main__":
    main()