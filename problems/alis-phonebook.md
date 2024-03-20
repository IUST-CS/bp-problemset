[_metadata_:id]:- "alis-phonebook"
[_metadata_:title]:- "دفترچه تلفن علی"
[_metadata_:level]:- "medium"
[_metadata_:author]:- "علیرضا خادم دقیق"
[_metadata_:series]:- "io-stream-and-exception-handling"

+ محدودیت زمان: ۱ ثانیه
+ محدودیت حافظه: ۲۵۶ مگابایت

----------
علی دو فایل متنی با پسوند `.txt` دارد که در یکی اسامی دوستانش (به نام `names.txt`) و در دیگری شماره تلفن آنها (به نام `phones.txt`) قرار گرفته است. علی که از این وضعیت خسته شده از شما می‌خواهد برنامه‌ای بنویسید که محتوای این دو فایل را به فرمت JSON مرتب‌شده در فایلی به اسم `result.json` ذخیره کند. 

جهت آشنایی بیشتر با فرمت JSON [اینجا](https://www.w3schools.com/js/js_json_syntax.asp) را بخوانید. 

برای هر شماره تلفن مراحل زیر را طی نمایید.

1. اگر شماره تلفن با `98+` شروع شود باید به فرم نرمال (شروع با `0`) تبدیل شود. 
2. پس از نرمال‌سازی اگر با `09` شروع شود و دارای ۱۱ رقم باشد یک شماره همراه معتبر نامیده می‌شود.
3. چنانچه شماره معتبر بود به شکل نرمال در خروجی می‌آید و در غیر این صورت  `null` در خروجی خواهد آمد.

هر تورفتگی فایل JSON شامل ۴ کاراکتر فاصله خالی است.

# محدودیت

استفاده از کتابخانه‌های آماده برای تولید فایل JSON ممنوع است.

# ورودی

ورودی در قالب دو فایل `names.txt` و `phones.txt` داده می‌شود که محتوای هر کدام پیش از این توضیح داده شد. تضمین می‌شود که فایل‌ها تهی نیستند و تعداد سطرهای هر فایل از $10^3$ تجاوز نمی‌کند. تعداد سطرهای دو فایل با هم برابر است.

# خروجی

چنانچه خطایی رخ نداد تنها خروجی برنامه فایل `result.json` است. 

همچنین چنانچه هر گونه مشکلی در باز شدن و دسترسی به هر یک از سه فایل مذکور وجود داشت می‌بایست با استفاده از دستور `cerr` پیام `sth went wrong` نمایش داده شده و اجرای برنامه متوقف شود.

# مثال

## ورودی نمونه ۱

### فایل `names.txt`
```
ali
mohammad
maryam
mostafa
ahmad
mahmood
```

### فایل `phones.txt`
```
09319471827
+989369341578
+989309456785
12893476
123498712638947
+987309456785
```

## خروجی نمونه ۱

### فایل `result.json`
```
{
    "ali": "09319471827",
    "mohammad": "09369341578",
    "maryam": "09309456785",
    "mostafa": null,
    "ahmad": null,
    "mahmood": null
}
```
