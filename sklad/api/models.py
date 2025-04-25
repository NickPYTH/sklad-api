from django.db import models


class Supplier(models.Model):
    title = models.CharField(max_length=100, verbose_name="Наименование")
    fio = models.CharField(max_length=250, verbose_name="Контактное лицо")
    phone = models.CharField(max_length=250, verbose_name="Телефон")

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
    name = models.CharField(max_length=250, verbose_name="Наименование")
    description = models.CharField(max_length=250, verbose_name="Описание")
    createDateTime = models.DateTimeField(verbose_name="Дата запроса", default=None)
    receiveDateTime = models.DateTimeField(verbose_name="Дата поставки", default=None)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Сотрудник")
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name="Поставщик")

    def __str__(self):
        return "{} {}".format(self.name, self.supplier.title)

    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name="Наименование")

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Material(models.Model):
    name = models.CharField(max_length=250, verbose_name="Наименование")
    description = models.CharField(max_length=250, verbose_name="Описание")
    number = models.CharField(max_length=250, verbose_name="Инв. номер")
    dropDate = models.DateField(verbose_name="Дата выдачи", default=None)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Получатель")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")

    def __str__(self):
        return "{} #{}".format(self.name, self.number)

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


class SupplyMaterial(models.Model):
    supply = models.ForeignKey(Supply, on_delete=models.CASCADE, verbose_name="Поставка")
    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name="Материал")

    def __str__(self):
        return "{} #{}".format(self.supply.name, self.material.name)

    class Meta:
        verbose_name = 'Поставка материала'
        verbose_name_plural = 'Поставки материалов'


class InventoryStatus(models.Model):
    name = models.CharField(max_length=250, verbose_name="Наименование")

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Статус инвентаризации'
        verbose_name_plural = 'Статусы инвентаризации'


class Inventory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Сотрудник")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория материала")
    description = models.CharField(max_length=250, verbose_name="Описание")
    date = models.DateField(verbose_name="Дата инвентаризации", default=None)
    count = models.IntegerField(verbose_name="Учетное количество")
    count_fact = models.IntegerField(verbose_name="Фактическое количество")
    status = models.ForeignKey(InventoryStatus, on_delete=models.CASCADE, verbose_name="Статус")

    def __str__(self):
        return "{} {}".format(self.category.name, self.status.name)

    class Meta:
        verbose_name = 'Инвентаризация'
        verbose_name_plural = 'Инвентаризации'


class Requirement(models.Model):
    name = models.CharField(max_length=250, verbose_name="Наименование")
    supply = models.ForeignKey(Supply, on_delete=models.CASCADE, verbose_name="Поставка")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория материала")
    count = models.IntegerField(verbose_name="Необходимое количество")

    def __str__(self):
        return "{}".format(self.name.name)

    class Meta:
        verbose_name = 'Потребность'
        verbose_name_plural = 'Потребности'