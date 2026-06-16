class Streamer:    
  def live(self):       
    return "Запускаю стрим! Подписывайтесь, ставьте лайки!"
  def earn(self):       
    return "Заработал 500 донатов за 2 часа"

class TikToker:    
  def live(self):        
   return "Снимаю трендовый тикток под песню месяца!"
  
  def viral(self):        
      return "Набрал 3 миллиона просмотров за сутки!"

class Mutant:    
  def live(self):        
    return "Я... я свечусь в темноте... это мой вайб..."
    
  def superpower(self):       
    return "Летаю и стреляю лазерами из глаз"


class GlowStreamer(Streamer, Mutant):
    def ultimate_content(self):
        return f"я транслирую стрим из космоса,{self.superpower()}, я {self.earn()}"

class ViralCyborg(TikToker, Mutant):
    def ultimate_content(self):
        return f"записал видео, где {self.superpower()}и {self.viral()}"

class DonateMage(Streamer, TikToker):
    def ultimate_content(self):
        return f"коллаборация с Мистером Бистом, ролик {self.viral()}за это время я {self.earn()}"
  
glow_streamer = GlowStreamer()
print(glow_streamer.live())
print(GlowStreamer.mro())

viral_ciborg = ViralCyborg()
print(viral_ciborg.live())
print(ViralCyborg.mro())

donate_mage = DonateMage()
print(donate_mage.live())
print(DonateMage.mro())