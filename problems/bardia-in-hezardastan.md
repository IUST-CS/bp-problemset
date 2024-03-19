[_metadata_:id]:- "bardia-in-hezardastan"
[_metadata_:title]:- "بردیا در هزاردستان!"
[_metadata_:level]:- "easy"
[_metadata_:author]:- "سام احمدی‌زاده"
[_metadata_:series]:- "strings-and-vectors"

+ محدودیت زمان: ۱ ثانیه
+ محدودیت حافظه: ۲۵۶ مگابایت

----------

بردیا به‌تازگی به‌عنوان یک گولنگ دولوپر وارد هولدینگ هزاردستان شده است. وظیفه‌ای به او داده شده که بسیار آسان است ولی چون عینک بردیا شکسته، چشمش نمی‌بیند. از آنجا که او باید وظیفه‌اش را انجام دهد پس از شما کمک خواسته که آن را حل کنید.

سؤال به این صورت است که دو رشته‌ متشکل از حروف انگلیسی به شما داده می‌شود و شما باید بررسی کنید که این دو رشته یکسان هستند یا خیر. اما مسئله یک شرط دارد و آن این است که بزرگ و کوچک بودن حروف رشته‌ها باید عکس هم باشد؛ یعنی اگر در رشته اول `a` داشتیم معادل آن در رشته دوم باید `A` باشد و برعکس.

# ورودی

ورودی دو رشته به‌ترتیب با طول‌های $n$ و $m$ است که در دو خط به شما داده می‌شود.

$$1 \le n, m \le 100$$

تضمین می‌شود که رشته‌های ورودی فقط از حروف بزرگ و کوچک انگلیسی تشکیل شده‌اند.

# خروجی

خروجی باید یکی از عبارات `YES` یا `NO` باشد. در صورتی که رشته‌ها بر هم منطبق بودند `YES` و در غیر این صورت `NO` را خروجی دهید.

# مثال

## ورودی نمونه ۱
```
AzTrrEEeIOuh
aZtRReeEioUH
```


## خروجی نمونه ۱
```
YES
```


## ورودی نمونه ۲
```
hGxZwQQkLp
HgxzWqqKlP
```


## خروجی نمونه ۲
```
NO
```

در این نمونه تنها حرف مشکل‌دار در رشته دوم حرف `x` است.