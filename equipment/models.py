from django.db import models

# Create your models here.

"""This represents equipment classes (e.g. "DSLR," "Tripod," etc.)
"""

class EquipmentClass(models.Model):
    equipment_class = models.CharField(max_length=200)
    is_active = models.BooleanField()

    def __unicode__(self):
        return self.equipment_class


"""This is the make and model of equipment (e.g. "Canon Rebel T3i DSLR")
People create reservations for EquipmentTypes"""


class EquipmentType(models.Model):
    equipment_class = models.ForeignKey(EquipmentClass, verbose_name='kind of equipment')
    equipment_name = models.CharField(max_length=200, verbose_name='make and model of equipment')
    equipment_image = models.ImageField(upload_to='eq_type_images/')
    equipment_description = models.TextField(verbose_name='description of equipment kit')
    is_active = models.BooleanField()
    def __unicode__(self):
        return self.equipment_name


"""This is an instantiation of an equipment type (e.g. "Canon Rebel T3i #4")
People pick up specific pieces of Equipment, based on their reservations"""


class Equipment(models.Model):
    equipment_type = models.ForeignKey(EquipmentType, verbose_name='make and model of equipment')
    barcode = models.CharField(max_length=200)
    equipment_notes = models.CharField(max_length=500, blank=True)
    is_active = models.BooleanField()

    def __unicode__(self):
        return unicode(self.equipment_type) + ' #' + unicode(self.barcode) + ' -- ' + unicode(self.equipment_notes)


"""
SPECIAL NOTE:
EquipTypeComponents should be a standard set of components which belong to an EquipmentType.
EquipComponent represents what components actual Equipment holds.
"""

"""This is the make and model of a component (e.g. "32GB SDHC Card")"""


class ComponentType(models.Model):
    component_name = models.CharField(max_length=200, verbose_name='')
    is_active = models.BooleanField()

    def __unicode__(self):
        return self.component_name


"""This is the list of which EquipmentTypes should have which Components"""


class EquipTypeComponent(models.Model):
    equipment_type = models.ForeignKey(EquipmentType)
    component_type = models.ForeignKey(ComponentType)
    is_active = models.BooleanField()

    def __unicode__(self):
        return 'Note: Each <' + unicode(self.equipment_type) + '> should have a <' + unicode(self.component_type) + '>'


"""This is the list of which Equipment actually has which Components"""


class EquipComponent(models.Model):
    component_type = models.ForeignKey(ComponentType)
    equipment = models.ForeignKey(Equipment)
    component_notes = models.CharField(max_length=500, blank=True)
    is_active = models.BooleanField()

    def __unicode__(self):
        return unicode(self.equipment.equipment_type) + ' #' + unicode(self.equipment.barcode) + ' has its ' + unicode(
            self.component_type)
