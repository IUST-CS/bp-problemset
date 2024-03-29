[_metadata_:id]:- "qazanfars-sufferings"
[_metadata_:title]:- "مصائب غضنفر"
[_metadata_:level]:- "hard"
[_metadata_:author]:- "علیرضا خادم دقیق"
[_metadata_:series]:- "io-stream-and-exception-handling"

+ محدودیت زمان: ۱ ثانیه
+ محدودیت حافظه: ۲۵۶ مگابایت

----------

غضنفر به‌تازگی برنامه‌نویسی را شروع کرده است. او جلوی دوستش، علی، ادعا کرده که می‌تواند برنامه‌ای بنویسد که هر تعداد صفحه از بازی دوز سه‌تایی را به آن بدهیم، وضعیتش را گزارش کند!

علی که می‌داند غضنفر دارد گزافه‌گویی می‌کند با اطمینان خاطر می‌گوید:«اگر می‌توانی بنویس!».

خلاصه که غضنفر برای عمل به این ادعای گزافش از شما کمک می‌خواهد.

برای آشنایی با بازی دوز سه‌تایی می‌توانید [اینجا](https://fa.wikipedia.org/wiki/%D8%AF%D9%88%D8%B2_%D8%B3%D9%87_%D8%AA%D8%A7%DB%8C%DB%8C) را بخوانید.

# ورودی

ورودی در قالب فایل `input.txt` داده می‌شود که داخل آن تعداد نامشخصی صفحه بازی با `-----` از هم جدا شده‌اند.


# خروجی

در خروجی برنامه شما باید وضعیت هر بازی به‌ترتیب چاپ می‌شود.

هر بازی یکی از چهار حالت زیر را می‌تواند داشته باشد:

+ بازی به اتمام نرسیده است (`Not finished`).
+ بازی با تساوی تمام شده است (`Draw`).
+ بازیکن `X` برنده شده است (`Winner: X`).
+ بازیکن `O` برنده شده است (`Winner: O`).

همچنین چنانچه هر گونه مشکلی در باز شدن و دسترسی فایل ورودی وجود داشت می‌بایست با استفاده از دستور `cerr` پیام `sth went wrong` نمایش داده شده و اجرای برنامه متوقف شود.

برای درک بهتر فرمت خروجی به مثال توجه کنید.

# مثال

## نمونه ورودی ۱

### فایل `input.txt`
```
X O O
O X X
# # #
-----
X O O 
X X O
X O #
-----
X O X
O O X
X O #
-----
X O X
X X O
O X O
-----
```


## خروجی نمونه
```
Not finished
Winner: X
Winner: O
Draw
```

