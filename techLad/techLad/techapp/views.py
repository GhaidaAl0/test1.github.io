from django.shortcuts import render, redirect
import qrcode
from django.http import HttpResponse, JsonResponse
from io import BytesIO
import base64

def home(request):
    qr_code_data = None
    if request.method == 'POST':
        keycard_id = request.POST.get('keycard_id')
        if keycard_id and len(keycard_id) == 10 and keycard_id.isdigit():
            # Generate QR code
            room_url = request.build_absolute_uri(f'/room/{keycard_id}/')
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(room_url)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            
            # Save to BytesIO
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            img_str = base64.b64encode(buffer.getvalue()).decode()
            qr_code_data = f"data:image/png;base64,{img_str}"

    return render(request, 'index.html', {'qr_code_data': qr_code_data})

def hello(request):
    return render(request, 'index.html')

def room(request, keycard_id):
    # Fetch room information based on keycard_id
    room_info = {
        'keycard_id': keycard_id,
        'room_number': '101',
        'guest_name': 'John Doe',
        'check_in': '2024-07-20',
        'check_out': '2024-07-25',
    }
    return render(request, 'room.html', {'room_info': room_info})
