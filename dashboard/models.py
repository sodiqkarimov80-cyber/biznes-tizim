from django.db import models

class Mahsulot(models.Model):
    nomi = models.CharField(max_length=100, verbose_name="Mahsulot nomi")
    jami_soni = models.IntegerField(default=0, verbose_name="Jami kelgan soni")
    dokonlarga_berilgani = models.IntegerField(default=0, verbose_name="Do'konlarga berilgani")
    
    # Narxlar bo'limi
    tannarxi = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Olingan narxi (Tannarxi)")
    sotish_narxi = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Sotiladigan narxi")

    # Avtomatik hisoblanadigan bo'limlar (Bularni akangiz o'zi yozib o'tirmaydi, tizim o'zi hisoblaydi)
    @property
    def sotilmaganlari(self):
        # Jami sondan do'konlarga berilganini ayirib tashlaydi
        return self.jami_soni - self.dokonlarga_berilgani

    @property
    def jami_kassa_puli(self):
        # Do'konlarga berilgan tavorlarning umumiy aylanma puli
        return self.dokonlarga_berilgani * self.sotish_narxi

    @property
    def sof_foyda(self):
        # Har bitta sotilgan (do'konga berilgan) tavordan kelgan sof foyda
        bitta_tavordan_foyda = self.sotish_narxi - self.tannarxi
        return self.dokonlarga_berilgani * bitta_tavordan_foyda

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "1. Mahsulotlar Ombori"

    def __str__(self):
        return self.nomi