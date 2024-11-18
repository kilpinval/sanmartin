import flet as ft
def main(page:ft.page):
  page.title = "Flet.chat"
  def on_message(msg):
    menssages.contlols.append(ft.Text(msg))
    page.updates()
  page.pubsub.susbcribe(on_message)
  def send_click(e):
    page pubsub.send_all(f"{user.value} , {message.value)")
    message.value = ""
    page.update()
  messages = ft.Column()
  user = ft.Text.Field(hint_Text = "Your name", with = 150)
  message = ft.Text.Field(hint_int = "Your message...", expand = True)
  send =ft.ElevatedButton("Send", on_click = Send_click)
  
    
  
    
  
  
