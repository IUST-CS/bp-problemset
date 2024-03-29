[_metadata_:id]:- "searching-mandalore"
[_metadata_:title]:- "در جست‌وجوی Mandalore"
[_metadata_:level]:- "hard"
[_metadata_:author]:- "عبدالسلام نیک‌کردار"
[_metadata_:series]:- "strings-and-vectors"

+ محدودیت زمان: ۲ ثانیه
+ محدودیت حافظه: ۲۵۶ مگابایت

----------

![توضیح تصویر](../assets/searching-mandalore-1.jpg)

بعد از مدت‌ها **Mandalorian** و **Grogu (Baby Yoda)** تصمیم گرفتند که برای کشف حقایق به سمت سیاره **Mandalore** حرکت کنند، اما با یک مشکل بزرگ مواجه شدند. سفینه آنها در آخرین رویاروییشان با نیروهای گارد امپراطوری کهکشان آسیب دیده بود و بر اثر آن سیستم موقعیت‌یاب سفینه به مشکل خورده بود، به صورتی که به جای نشان دادن اسم سیاره‌های مورد نظر یک رشته کدگذاری‌شده حاوی اسم آنها را نشان می‌داد.

به آنها کمک کنید دستگاهی بسازند که به‌وسیله آن رشته‌های رمزگذاری‌شده را ترجمه کنند.

الفبای مورد استفاده دستگاه شامل ۷۴ کاراکتر به ترتیب زیر است:
```
1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m n o p q r s t u v w x y z
```

هر رشته رمزگذاری‌شده به الگوی `Prefix + A + X + B + Suffix` است که در آن هر بخش به شکل زیر می‌باشد:

|        بخش       |        توضیح       |
|:------------------:|:------------------:|
|         Prefix         |          رشته پیشوند        |
|         Suffix         |         رشته پسوند        |
|         A, B         |          رشته‌های اضافی که می‌توانند خالی باشند        |
|         X         |         می‌تواند برابر Prefix یا Suffix باشد        |

رمزگذاری به این صورت انجام گرفته که طول رشته‌های `Prefix` و `Suffix` همواره برابر است و مجموع جایگاه $i$امین کاراکتر `Prefix` و جایگاه $i$امین کاراکتر `Suffix` در الفبای ذکر شده همیشه برابر ۷۵ است. برای مثال اگر $i$امین کاراکتر `Prefix` برابر `1` باشد که در جایگاه ۱ حروف الفبا است، آنگاه $i$امین کاراکتر `Suffix` برابر `z` خواهد بود.

در این سؤال از شما می‌خواهیم:

+ رشته `X` را به‌گونه‌ای بیابید که `Prefix` و `Suffix` بیشترین طول ممکن را داشته باشند.
+ رشته خروجی باید تنها شامل:
1. ارقام:
```
1 2 3 4 5 6 7 8 9
```

2. حروف بزرگ:
```
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
```

3. حروف کوچک:
```
a b c d e f g h i j k l m n o p q r s t u v w x y z
```

باشد و قبل از خروجی دادن باید کاراکترهای اضافی را از رشته `X` حذف کنید.
+ اگر بعد از حذف کاراکترهای اضافی رشته خالی شد رشته یافت‌شده صحیح نمی‌باشد و باید رشته دیگری را بیابید و خروجی دهید.
+ در صورتی که هیچ رشته‌ای با ویژگی‌های مذکور یافت نشد عبارت `Error 404` را خروجی دهید.

# ورودی

ورودی تنها شامل یک رشته رمزگذاری‌شده است که طول آن می‌تواند از 1 تا $10^6$ متغیر باشد و شامل الفبای مذکور در متن سؤال است.

# خروجی

خروجی برنامه شما اسم موقعیت مخفی شده در رشته رمزگذاری‌شده به‌صورت یک رشته در صورت وجود و در غیر این صورت `Error 404` است.

# مثال

## ورودی نمونه ۱

```
A8@BiQ?A8@BiwE>>jskiB
```


## خروجی نمونه ۱

```
A8Bi
```


## ورودی نمونه ۲

```
klmnACZ@@?>=A:x72hds>@?>=
```


## خروجی نمونه ۲

```
Error 404
```

