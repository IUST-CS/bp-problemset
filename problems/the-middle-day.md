[_metadata_:id]:- "the-middle-day"
[_metadata_:title]:- "روز وسط"
[_metadata_:level]:- "easy"
[_metadata_:author]:- "نفیسه جلیلوند"
[_metadata_:series]:- "arrays-and-recursion"
+ محدودیت زمان: ۱ ثانیه
+ محدودیت حافظه: ۲۵۶ مگابایت

----------

در تقویم جلیلی، هر سال از $m$ ماه تشکیل شده است: ماه ۱، ماه ۲، ...، ماه $m$. ماه $i$ام از $d_i$ روز تشکیل شده است: روز ۱، روز ۲، ...، روز $d_i$. همچنین، تعداد روزها در هر سال فرد است، یعنی

$$d_1 + d_2 + ... + d_m$$

فرد است.

مشخص کنید کدام روز از کدام ماه، روز وسط سال است؛ یعنی اگر روز ۱ از ماه ۱ روز اول باشد، $a$ و $b$ را بیابید به‌طوری که روز

$$ \dfrac{ d_1 + d_2 + ... + d_m + 1 }{2} $$

روز $b$ از ماه $a$ باشد.

# ورودی

ورودی تنها شامل دو خط است که در خط اول عدد طبیعی $m$ و در خط دوم $d_i$ها با فاصله از هم آمده است.

$$1 \le m, d_i \le 100$$
# خروجی

خروجی برنامه شما باید شامل یک خط باشد که در آن به ترتیب $a$ و $b$ (روز $b$ از ماه $a$) با فاصله از هم چاپ شوند.

# مثال
## ورودی نمونه ۱
```
12
31 28 31 30 31 30 31 31 30 31 30 31
```


## خروجی نمونه ۱
```
7 2
```


## ورودی نمونه ۲
```
1
1
```


## خروجی نمونه ۲
```
1 1
```

