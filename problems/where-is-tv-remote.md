[_metadata_:id]:- "where-is-tv-remote"
[_metadata_:title]:- "کنترل تلویزیون کجاست؟"
[_metadata_:level]:- "hard"
[_metadata_:author]:- "محمدمهدی پورحیدری"
[_metadata_:series]:- "functions"
+ محدودیت زمان: ۱ ثانیه
+ محدودیت حافظه: ۲۵۶ مگابایت

----------

احمد که دیشب به دلیل کار بیش از حد نتوانسته است سریال مورد علاقه خود را مشاهده کند، خسته و کوفته از سر کار برگشته و بدون سلام کردن به کسی و عوض کردن لباس‌هایش، به سمت مبل روبه‌روی تلویزیون می‌رود تا بازپخش قسمت جدید را ببیند. اما او هر چه اطراف میز تلویزیون را جست‌وجو می‌کند کنترل تلویزیون را نمی‌یابد! سپس با خشم زیاد فریاد می‌زند:«اگه بفهمم کی کنترل رو برداشته، تیکه بزرگش گوششه!».

احمد که وقت این را ندارد که کنترل را پیدا کند، تصمیم می‌گیرد با استفاده از دکمه‌های خود تلویزیون به شبکه مورد نظرش برسد. اما به دلیل قدیمی بودن تلویزیون، دکمه‌هایش فرسوده شده‌اند و درست کار نمی‌کنند.
دکمه جلو بردن شبکه $n-1$ در میان، و دکمه عقب بردن شبکه $m-1$ در میان کار می‌کند؛ یعنی برای جلو بردن شبکه، از هر $n$ بار فشار دکمه، یک بار آن مؤثر است و همین‌طور برای عقب بردن شبکه، از هر $m$ بار فشار دکمه، یک بار آن مؤثر است. در هر دوره از تلاش، آخرین فشار دکمه موفق است. برای مثال اگر دکمه جلو بردن $n-1$ در میان باشد، تلاش $n$ام باعث جلو رفتن شبکه می‌شود.

احمد که می‌داند $s$ ثانیه تا شروع سریال مانده است و هر فشار دکمه ۱ ثانیه زمان می‌برد، می‌خواهد با سریع‌ترین روش به سریال خود برسد. تلویزیون دارای $A$ شبکه است و در حال حاضر روی شبکه شماره $C$ قرار دارد و مقصد شبکه شماره $D$ است. توجه کنید که شبکه بعد از شبکه آخر، شبکه اول هست. حال به او کمک کنید و بگویید که با جلو رفتن (J)، با عقب رفتن (A)، با هر دو (A و J) یا با هیچ‌کدام (1-) می‌تواند سریال را از دست ندهد و نیز زمان باقی‌مانده را محاسبه کنید.

# محدودیت

برای حل این سؤال باید دو تابع زیر را تعریف کنید تا هر یک مقادیر لازم را برگرداند یا در خروجی چاپ کند.

1. تابعی برای حالت جلو بردن (J) 
2. تابعی برای حالت عقب بردن (A)

در غیر این صورت امتیازی به پاسخ شما اختصاص داده نخواهد شد.

# ورودی

ورودی شامل سه خط است که در خط اول آن عدد طبیعی $s$ و در خط دوم به‌ترتیب اعداد طبیعی $n$ و $m$ که با فاصله از هم جدا شده‌اند و در خط سوم سه عدد طبیعی $C$ و $D$ و $A$ که با فاصله از هم جدا شده‌اند داده شده است.
$$2 \le s \le 1000$$
$$1 \le m,n \le 15$$
$$1 \le C,D \le A \le 1000$$

# خروجی

خروجی برنامه شما باید شامل حالت‌های ممکن برای رسیدن به‌موقع به شبکه مورد نظر و زمان اضافه آمده باشد. توجه داشته باشید که زمان اضافه آمده می‌تواند صفر باشد. در صورت غیر ممکن بودن رسیدن به شبکه مورد نظر در زمان مورد نظر $-1$ را خروجی دهید.

برای درک بهتر سؤال، به مثال‌ها توجه کنید.

# مثال

## ورودی نمونه ۱
```
200
2 5
5 51 100
```


## خروجی نمونه ۱
```
J : 108
```

## ورودی نمونه ۲
```
150
7 5
13 31 47
```


## خروجی نمونه ۲
```
J : 24
A : 5
```


## ورودی نمونه ۳
```
20
5 8
35 13 70
```


## خروجی نمونه ۳
```
-1
```

