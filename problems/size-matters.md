[_metadata_:id]:- "size-matters"
[_metadata_:title]:- "!سایز مهمه"
[_metadata_:level]:- "easy"
[_metadata_:author]:- "محمدمهدی پورحیدری"
[_metadata_:series]:- "compensation-1-5"

+ محدودیت زمان: ۱ ثانیه
+ محدودیت حافظه: ۲۵۶ مگابایت

----------
هاشم، برادر احمد آقا، به‌تازگی به‌همراه خانواده‌اش از شیراز به تهران آمده است. او در هنگام ورودش به تهران با احمد آقا تماس می‌گیرد و می‌خواهد به خانه آنها برود. احمد آقا که مدت زیادی است برادرش را ندیده است، خوشحال می‌شود و فوراً او و خانواده‌اش را به خانه خود دعوت می‌کند. احمد آقا این خبر را با همسرش، سحر خانم، به اشتراک می‌گذراد و از او درخواست می‌کند تا برای این مهمانی یک شام درست و حسابی ترتیب دهد. سحر خانم که احساس می‌کند وقت کمی دارد فوراً خود را آماده می‌کند و غذا را می‌پزد.

حال که غذا آماده شده، فقط مرحله جا کردن و آماده‌سازی آن در ظروف باقی مانده است. از آنجایی که سحر خانم می‌خواهد بهترین مدل ظرف را انتخاب کند و جلوی خانواده برادر شوهرش آبروداری کند، باید بهترین مدل ظرف ممکن را انتخاب کند. همچنین از آنجا که سحر خانم خیلی روی اندازه ظرف حساس است، از نظر او بهترین مدل ظرف، ظرفی است که اندازه‌اش نه کوچک و نه بزرگ باشد.

سحر خانم $n$ مدل ظرف در آشپزخانه در اختیار دارد که هر کدام اندازه $m{_{i}}$ را دارند. از آنجایی که سحر خانم نمی‌تواند به‌طور مستقیم بهترین مدل ظرف را انتخاب کند، او تمام ظرف‌ها را به‌ترتیب اندازه مرتب می‌کند و در هر مرحله، یکی‌درمیان به‌ترتیب بزرگ‌ترین یا کوچک‌ترین ظرف را کنار می‌گذارد تا به ظرف آخر برسد. او ابتدا از کنار گذاشتن بزرگ‌ترین ظرف شروع می‌کند.

در این کار به سحر خانم کمک کنید.

# ورودی
در خط اول ورودی عدد طبیعی $n$ داده شده است که نشان‌دهنده تعداد مدل‌های ظروف می‌باشد و در خط بعدی، $n$ عدد، که نشان‌دهنده اندازه‌های مختلف هستند و با فاصله از هم جدا شده‌اند به شما داده شده است.

$$2 \le n,m{_{i}} \le 100$$

# خروجی
هر خط از خروجی شما باید شامل اعداد مرتب شده باشد که در هر مرحله بزرگ‌ترین یا کوچک‌ترین آن حذف شده باشد تا به آخرین عدد برسیم. حذف کردن از بزرگ‌ترین عدد شروع می‌شود.

برای فهم بهتر مسئله به مثال‌ها توجه کنید.

# مثال

## ورودی نمونه ۱
```
5
8 12 3 9 4
```


## خروجی نمونه ۱
```
3 4 8 9
4 8 9
4 8
8
```

در این مثال، ابتدا اعداد مرتب شدند و در مرحله اول بزرگ‌ترین عدد و در مرحله دوم کوچک‌ترین عدد حذف شدند. این روند به‌ترتیب و یکی‌درمیان ادامه یافته تا به عدد آخر برسیم.
