[_metadata_:id]:- "inverse-of-table"
[_metadata_:title]:- "عکس جدول"
[_metadata_:level]:- "medium"
[_metadata_:author]:- "علی زرگر"
[_metadata_:series]:- "strings-and-vectors"

+ محدودیت زمان: ۱ ثانیه
+ محدودیت حافظه: ۲۵۶ مگابایت

---------

عمل عکس را بر یک جدول چنین تعریف می‌کنیم:

+ اگر سطری از جدول $n$ خانه داشته باشد؛ خانه اول با خانه $n$ام، خانه دوم با خانه $n-1$ام... جابه‌جا می‌شود.
+ اگر جدول $n$ سطر داشته باشد؛ سطر اول با سطر $n$ام، سطر دوم با سطر $n-1$ام... جابه‌جا می‌شود.

# ورودی

سطرهای یک جدول که هر خانه آن عدد صحیح و نامنفی $x \le 100$ است داده می‌شوند که انتهای هر سطر و انتهای جدول با $-1$ مشخص می‌شود.

تضمین می‌شود هر جدول حداکثر $100$ سطر و هر سطر حداکثر $100$ خانه دارد.

# خروجی

از شما عکس جدول را (بدون $-1$ در پایان جدول و سطرها) می‌خواهیم.

# مثال

## ورودی نمونه ۱
```
1 2 3 -1
4 5 -1
6 7 8 9 -1
-1
```

## خروجی نمونه ۱
```
9 8 7 6
5 4
3 2 1
```


## ورودی نمونه ۲
```
3 3 3 -1
2 2 -1
1 -1
-1
```

## خروجی نمونه ۲
```
1
2 2
3 3 3
```

