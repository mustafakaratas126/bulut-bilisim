from flask import jsonify, request

from app import app

# isim:Mustafa soyisim:karataş ogrno:02230201126
@app.route('/isimDondur', methods=['POST'])
def isim_dondur():
    veri = request.json
    isim = veri.get('isim', 'herhangi bir isim belirtilmedi')
    return jsonify({'mesaj': f'merhaba, {isim}!'}), 200
