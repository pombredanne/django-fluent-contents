from django.db import models
from fluent_contents.models import ContentItem, PlaceholderField, PlaceholderRelation, ContentItemRelation


class TestPage(models.Model):
    """
    A plain model, for testing placeholders.
    """
    contents = models.TextField("Contents")

    class Meta:
        verbose_name = "Test page"
        verbose_name_plural = "Test pages"


class PlaceholderFieldTestPage(models.Model):
    """
    A model with PlaceholderField, for testing,
    """
    title = models.CharField(max_length=200)
    contents = PlaceholderField("field_slot1")

    placeholder_set = PlaceholderRelation()
    contentitem_set = ContentItemRelation()

    class Meta:
        verbose_name = "Test page"
        verbose_name_plural = "Test pages"

    def __unicode__(self):
        return self.title


class RawHtmlTestItem(ContentItem):
    """
    The most basic "raw HTML" content item, for testing.
    """
    html = models.TextField("HTML code")

    class Meta:
        verbose_name = 'Test HTML code'
        verbose_name_plural = 'Test HTML codes'

    def __unicode__(self):
        return self.html
