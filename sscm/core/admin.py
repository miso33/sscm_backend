from import_export.admin import ImportExportModelAdmin


class BaseAdmin(ImportExportModelAdmin):
    exclude = ("status_changed", "is_removed")


class BaseStatusAdmin(BaseAdmin):
    list_display = ("status",)
    list_filter = ("status",)


class BaseRemovableAdmin(BaseAdmin):
    list_display = ("is_removed",)
    list_filter = ("is_removed",)


class BaseFullAdmin(BaseStatusAdmin, BaseRemovableAdmin):
    pass
