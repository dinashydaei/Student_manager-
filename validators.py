def get_valid_name():
    name = input("نام دانشجو: ").strip()
    if not name:
        raise ValueError("نام نمی‌تونه خالی باشه")
    return name

def get_valid_age():
    try:
        age = int(input("سن: "))
    except ValueError:
        raise ValueError("سن باید عدد باشه")
    if age < 10 or age > 100:
        raise ValueError("سن باید بین ۱۰ تا ۱۰۰ باشه")
    return age

def get_valid_scores():
    raw = input("نمرات (با کاما جدا کن، مثلا 18,17.5,20): ")
    try:
        scores = [float(x.strip()) for x in raw.split(",") if x.strip()]
    except ValueError:
        raise ValueError("نمرات باید عدد باشن")
    if not scores:
        raise ValueError("حداقل یک نمره لازمه")
    if any(s < 0 or s > 20 for s in scores):
        raise ValueError("هر نمره باید بین ۰ تا ۲۰ باشه")
    return scores