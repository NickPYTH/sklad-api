from django.db import models

class Material(models.Model):
    name = models.CharField(max_length=250, verbose_name="Наименование")
    category = models.CharField(max_length=250, verbose_name="Категория товара")
    number = models.CharField(max_length=250, verbose_name="Инв. номер")

    def __str__(self):
        return "{} #{}".format(self.name, self.number)

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'

class Supplier(models.Model):
    phone = models.CharField(max_length=250, verbose_name="Телефон")
    fio = models.CharField(max_length=250, verbose_name="Контактное лицо")
    organization = models.CharField(max_length=100, verbose_name="Наименование организации")


    def __str__(self):
        return "{} {} {}".format(self.title, self.fio, self.phone)

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Employee(models.Model):
    fio = models.CharField(max_length=250, verbose_name="ФИО")
    post = models.CharField(max_length=100, verbose_name="Должность")
    phone = models.CharField(max_length=250, verbose_name="Телефон")

    def __str__(self):
        return "{} {} {}".format(self.fio, self.post, self.phone)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Supply(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name="Поставщик")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Сотрудник")
    date = models.DateTimeField(verbose_name="Дата поставки", default=None)
    materials = models.ManyToManyField(Material)
    def __str__(self):
        return "{} {}".format(self.name, self.supplier.title)

    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'


class Inventory(models.Model):
    materials = models.ManyToManyField(Material, verbose_name="Материалы")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Сотрудник")
    count = models.IntegerField(verbose_name="Фактическое количество")

    class Meta:
        verbose_name = 'Инвентаризация'
        verbose_name_plural = 'Инвентаризации'

class Remain(models.Model):
    name = models.IntegerField(verbose_name="Мин. кол-во")
    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name="Материал")

class Response(models.Model):
    material = models.ManyToManyField(Material, verbose_name="Материалы")
    getter = models.IntegerField(verbose_name="Получатель")
    date = models.DateTimeField(verbose_name="Дата выдачи", default=None)
    count = models.IntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Сотрудник")
