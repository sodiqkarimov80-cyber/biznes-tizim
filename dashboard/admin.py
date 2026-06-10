from django.contrib import admin
from .models import Mahsulot

@admin.register(Mahsulot)
class MahsulotAdmin(admin.ModelAdmin):
    # Jadvalda nimalar ko'rinib turishi shartligi:
    list_display = (
        'nomi', 
        'jami_soni', 
        'dokonlarga_berilgani', 
        'sotilmaganlari_soni', 
        'tannarxi', 
        'sotish_narxi', 
        'umumiy_tushum', 
        'sof_foyda_miqdori'
    )
    
    # Narxlarni va maxsulotlarni admin panelning o'zida tezda o'zgartirish imkoniyati
    list_editable = ('jami_soni', 'dokonlarga_berilgani', 'tannarxi', 'sotish_narxi')

    # Hisoblanadigan bo'limlarni jadvalga o'zbekcha nom bilan chiqarish:
    def sotilmaganlari_soni(self, obj):
        return obj.sotilmaganlari
    sotilmaganlari_soni.short_description = "Sotilmaganlari (Qoldiq)"

    def umumiy_tushum(self, obj):
        return f"{obj.jami_kassa_puli:,.2f} so'm"
    umumiy_tushum.short_description = "Jami Pul (Kassa)"

    def sof_foyda_miqdori(self, obj):
        return f"{obj.sof_foyda:,.2f} so'm"
    sof_foyda_miqdori.short_description = "Sof Foyda"