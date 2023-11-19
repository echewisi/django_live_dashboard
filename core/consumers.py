from channels.generic.websocket import AsyncWebsocketConsumer
import json

class DashboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("connection...")
        await self.accept()
    
    async def disconnect(self, close_code):
        print(f"connecting closed...{close_code}")
        
    
    async def receive(self, text_data):
        print("reading text...")
        text_data= json.loads(text_data)