months = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]

while True:
    date = input("Date: ").strip()
    try:
        if "/" in date and "," not in date:
            m, d, y = date.split("/")
            m = int(m); d = int(d); y = int(y)
        elif "," in date:
            m_str, d_str = date.split(" ", 1)
            d_str, y_str = d_str.split(", ")
            m = months.index(m_str) + 1
            d = int(d_str); y = int(y_str)
        else:
            continue
        if 1 <= m <= 12 and 1 <= d <= 31:
            print(f"{y:04}-{m:02}-{d:02}")
            break
    except:
        continue
