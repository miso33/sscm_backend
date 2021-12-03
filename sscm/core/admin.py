from import_export.admin import ImportExportModelAdmin


class BaseAdmin(ImportExportModelAdmin):
    exclude = ("status_changed", "is_removed")
    title = ""

    def changelist_view(self, request, extra_context=None):
        extra_context = {"title": self.title}
        return super().changelist_view(request, extra_context=extra_context)


class BaseStatusAdmin(BaseAdmin):
    list_display = ("status",)
    list_filter = ("status",)


class BaseRemovableAdmin(BaseAdmin):
    list_display = ("is_removed",)
    list_filter = ("is_removed",)


class BaseFullAdmin(BaseStatusAdmin, BaseRemovableAdmin):
    pass
