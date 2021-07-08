from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class NetworkList(models.Model):

    subnet_name = models.CharField(_("Subnet Name"), max_length=255)
    subnet_value = models.IntegerField(_("Subnet Value"))
    
    class Meta:
        verbose_name = "NetworkList"
        verbose_name_plural = "NetworkLists"

    def get_absolute_url(self):
        return reverse("NetworkList_detail", kwargs={"pk": self.pk})


class AddSubList(models.Model):

    acc_subnet_name = models.CharField(_("Subnet Name"), max_length=10)
    acc_subnet_value = models.IntegerField(_("Subnet Value"))

    class Meta:
        verbose_name = "AddSubList"
        verbose_name_plural = "AddSubLists"

    def get_absolute_url(self):
        return reverse("AddSubList_detail", kwargs={"pk": self.pk})


class NewExposure(models.Model):
    """Collection od some subnets without their values"""
    new_sub_name = models.CharField(_("Subnet Name"), max_length=10)
    new_sub_value = models.IntegerField(_("Subnet Valuesss"), blank=True, null=True)

    class Meta:
        verbose_name = "NewExposure"
        verbose_name_plural = "NewExposures"

    def get_absolute_url(self):
        return reverse("NewExposure_detail", kwargs={"pk": self.pk})