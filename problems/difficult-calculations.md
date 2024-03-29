[_metadata_:id]:- "difficult-calculations"
[_metadata_:title]:- "محاسبات دشوار"
[_metadata_:level]:- "hard"
[_metadata_:author]:- "علی زرگر"
[_metadata_:series]:- "functions"

+ محدودیت زمان: ۱ ثانیه
+ محدودیت حافظه: ۲۵۶ مگابایت

---------
> همان‌طور که می‌دانید توابع همانند یک برنامه کوچک در یک برنامه بزرگ عمل می‌کنند که مهم‌ترین کاربردهای آنها عبارتند از:
> + قابلیت استفاده مجدد از آنها (به‌ویژه از کتابخانه‌های موجود)
> + تقسیم یک وظیفه بزرگ به چند وظیفه کوچک‌تر
> + خوانایی و نظم بیشتر با گروه‌بندی عملیات‌های مرتبط
> + سهولت آزمایش تکه‌های مختلف برنامه
> + و غیره. 

در این سؤال با استفاده از [کتابخانه `cmath`](https://cplusplus.com/reference/cmath/) باید خروجی دو تابع زیر را بدست آورید.

$$
f(x) = \lceil \sin(\cosh(\sqrt[3]{x})) + e^{\arctan(x)} - \log_{2}(|x|) + \sqrt[3]{x^{2}} \rceil
$$

\[
\text{g}(x) = \lfloor \sqrt[4]{f(x^2)^3} + \frac{1}{x+10} \rfloor
\]

در جدول زیر تعدادی نمونه‌هایی از مقادیر این دو تابع به ازای ورودی‌هایی جهت سهولت بررسی کدتان داده شده است.

|        $g(x)$       |        $f(x)$         |       $x$      |
|:------------------:|:------------------:|:------------------:|
|       3      |        3       |       -1      |
|       98       |          21          |       100      |
|         19        |       9      |   $f(100)$      |


با این حال در این سؤال ورودی این دو تابع به‌صورت هگزادسیمال به شما داده می‌شوند و خروجی را نیز به‌صورت هگزادسیمال از شما می‌خواهیم.

دستگاه هگزادسیمال یا همان شانزده‌شانزدهی از نمادهای ۰ تا ۹ برای مقادیر ۰ تا ۹ و از حروف A و B و C و D و E و F برای مقادیر ۱۰ تا ۱۵ استفاده می‌کند.

برای مثال:
```
1. Hex: 3AB, Decimal: 939
2. Hex: 10, Decimal: 16
3. Hex: 777, Decimal: 1911
4. Hex: D7, Decimal: 215
```

که در آن

$$
(3AB)_{16} = 3 \times 16^2 + 10 \times 16^1 + 11 \times 16^0 = (939)_{10}
$$


# محدودیت

+ حداقل چهار تابع برای
	+ محاسبه مقدار $f(x)$ 
	+ محاسبه مقدار $g(x)$
	+ تبدیل از سیستم دسیمال به هگزادسیمال
	+ تبدیل از سیستم هگزادسیمال به دسیمال
باید تعریف شود.

# ورودی

عدد صحیح $x$ در سیستم شانزده‌شانزدهی به شما داده می‌شود.
$$-9 \le x \le 3E8$$
$$x \neq 0$$

# خروجی

در خط اول خروجی مقدار $f(x)$ و در خط دوم مقدار $g(x)$ به‌صورت هگزادسیمال گزارش شود.

# مثال‌

## ورودی نمونه ۱
```
3F
```

## خروجی نمونه ۱
```
10
3D
```

$$
(3F)_{16} = 3 \times 16^1 + 15 \times 16^0 = (63)_{10}
$$

$$
f(63) = (16)_{10}  = (10)_{16}
$$

$$
g(63) = (61)_{10} = (3D)_{16}
$$
