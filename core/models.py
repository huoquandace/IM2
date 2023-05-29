from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    title = models.CharField(_("title"), max_length=255)
    label = models.CharField(_("label"), max_length=255)
    image = models.ImageField(_("image"), upload_to="category")
    description = models.TextField(_("description"))
    class Meta:
        verbose_name_plural = _("categories")
    def __str__(self):
        return self.title
    
class Product(models.Model):
    id_product = models.CharField(_("product id"), max_length=255)
    name = models.CharField(_("name"), max_length=255)
    brand = models.CharField(_("brand"), max_length=255)
    image = models.ImageField(_("image"), upload_to="product")
    price = models.IntegerField(_("price"))
    description = models.TextField(_("description"))
    category = models.ForeignKey(Category, verbose_name=_("category"), on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = _("products")
    def __str__(self):
        return f'{self.name} ({self.brand})'
    
class Supplier(models.Model):
    id_supplier = models.CharField(_("supplier id"), max_length=255)
    name = models.CharField(_("name"), max_length=255)
    logo = models.ImageField(_("logo"), upload_to="supplier", null=True, blank=True)
    phone = models.CharField(_("phone"), max_length=255)
    address = models.TextField(_("address"))
    fax = models.CharField(_("fax"), max_length=255)
    email = models.EmailField(_("email"), max_length=255)
    products = models.ManyToManyField(Product, verbose_name=_("products"), blank=True)
    account = models.OneToOneField(get_user_model(), verbose_name=_("account"), on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class POrder(models.Model):
    label = models.CharField(_("label"), max_length=255, null=True, blank=True)
    supplier = models.ForeignKey(Supplier, verbose_name=_("supplier"), on_delete=models.CASCADE)
    order_date = models.DateField(_("order date"), null=True, blank=True)
    status = models.CharField(_("status"), max_length=255, null=True, blank=True, default="draft")
    created_at = models.DateTimeField(auto_now=True, editable=False)
    total = models.IntegerField(_("total"), null=True, blank=True)
    note = models.TextField(_("note"), null=True, blank=True)

    def save(self, *args, **kwargs):
        self.label = "PUR-" + str(POrder.objects.count()+1)
        return super(POrder, self).save(*args, **kwargs)

    def total_product(self):
        return self.porderdetail_set.all().count()
    def total_item(self):
        return sum([x.quantity for x in self.porderdetail_set.all()])
    def estimated_bill(self):
        sum = 0
        for porderdetail in self.porderdetail_set.all():
            if porderdetail.price is not None:
                sum += porderdetail.price * porderdetail.quantity
        return sum
    


class POrderDetail(models.Model):
    porder = models.ForeignKey(POrder, verbose_name=_("purchare order"), on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(_("quantity"), default=1, null=True, blank=True)
    price = models.IntegerField(_("price"), null=True, blank=True)
    status = models.CharField(_("status"), max_length=255, null=True, blank=True)

    def total(self):
        if self.price == None or self.quantity == None:
            return 0
        return self.price * self.quantity
    