[_metadata_:id]:- "volumetric-calculation"
[_metadata_:title]:- "حساب حجمی"
[_metadata_:level]:- "medium"
[_metadata_:author]:- "هربد پورعلی"
[_metadata_:series]:- "functions"

+ محدودیت زمان: ۱ ثانیه
+ محدودیت حافظه: ۲۵۶ مگابایت

----------

در این سؤال باید سه تابع با نام یکسان `CalculateVolume` بسازید که حجم هر یک از اشکال کره، مکعب مستطیل یا استوانه را بتوانند محاسبه کنند.

به ترتيب برای کره، استوانه و مکعب مستطیل داریم:
```
CalculateVolume: (radius: double)
CalculateVolume: (length: double, width: double, height: double)
CalculateVolume: (radius: double, height: double)
```


همچنین برای ورودی گرفتن منویی به شکل زیر طراحی کنید:

```
Choose a shape to calculate the volume:
1. Sphere
2. Rectangular Prism
3. Cylinder
4. Exit
Enter your choice (1/2/3/4): 
```

نکته: در تمام محاسبات مقدار عدد $\pi$ را $3.14$ در نظر بگیرید.

# محدودیت

1. پیاده‌سازی تابع `CalculateVolume` دقیقاً به همان شکلی در توضیح سؤال آمده است الزامی است.
2. برای پیاده‌سازی منو از بلوک‌های do-while و switch-case استفاده کنید.

# ورودی

ورودی هر بار شامل یک خط است که در آن یک عدد طبیعی $n_i$ آمده است.

هر مقدار $n_i$ متناظر با یک دستور طبق جدول زیر است.

| شماره | دستور | ورودی‌های بعدی
| --- | --- | --- |
| ۱ | محاسبه حجم کره | شعاع |
| ۲ | محاسبه حجم مکعب مستطیل | طول، عرض، ارتفاع |
| ۳ | محاسبه حجم استوانه | شعاع قاعده، ارتفاع |
| ۴ | خروج | ندارد |

به محض اینکه یکی از دستورهای ۱ تا ۳ وارد شد ورودی‌های بعدی آن که شامل مشخصات شکل مورد نظر است به‌ ترتیب و در خطوط مجزا داده می‌شود.

و گرفتن $n_i$ها تا زمانی که عدد `4` (متناظر با دستور خروج) وارد نشود به همین صورت ادامه دارد.

# خروجی

حجم شکل‌های متناظر با دستورهای ورودی را در خروجی چاپ نمایید.

همچنین چنانچه برای $n_i$ها شماره دستوری به‌جز اعداد ۱ تا ۴ وارد شد پیغام خطای

```
Invalid choice. Please enter 1, 2, 3, or 4.
```

را در یک خط مجزا چاپ نمایید.

برای درک بهتر فرمت خروجی به مثال‌ها توجه کنید.

# مثال

**نکته**: عبارت‌های بعد از `//` در بخش ورودی‌ها و خروجی‌های نمونه زیر صرفاً برای درک بهتر سوال قرار داده شده‌اند و جزو ورودی یا خروجی نیستند.

## ورودی نمونه ۱
```
1 // choice
12 // radius
2 // choice
12 // length
12 // width
12 // height
3 // choice
12 // radius
12 // height
5 // choice
4 // choice
```


## خروجی نمونه ۱
```
Choose a shape to calculate the volume:
1. Sphere
2. Rectangular Prism
3. Cylinder
4. Exit
Enter your choice (1/2/3/4): 
// The choice entered: 1
Volume of the sphere: 7234.56
Choose a shape to calculate the volume:
1. Sphere
2. Rectangular Prism
3. Cylinder
4. Exit
Enter your choice (1/2/3/4): 
// The choice entered: 2
Volume of the rectangular prism: 1728
Choose a shape to calculate the volume:
1. Sphere
2. Rectangular Prism
3. Cylinder
4. Exit
Enter your choice (1/2/3/4): 
// The choice entered: 3
Volume of the cylinder: 5425.92
Choose a shape to calculate the volume:
1. Sphere
2. Rectangular Prism
3. Cylinder
4. Exit
Enter your choice (1/2/3/4): 
// The choice entered: 5
Invalid choice. Please enter 1, 2, 3, or 4.
Choose a shape to calculate the volume:
1. Sphere
2. Rectangular Prism
3. Cylinder
4. Exit
Enter your choice (1/2/3/4): 
// The choice entered: 4
Exiting the program.
```

