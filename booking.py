#
print("*** MAPA DEL HOTEL ***")
print('*' * 40)
matrix = [['101','102','103','104'],
          ['201','202','203','204'],
          ['301','302','303','304'],
          ['401','402','403','404']
         ]

for row in matrix:
  print(row)
print('*' * 40)
print(' ' * 40)

floor_input =0
room_input =0
hotel_matrix = [[
  {'name': 'Jesus Carrillo',  'room': '101'},
  {'name': 'Sandra Villalba', 'room': '102'},
  {'name': 'Available', 'room': '103'},
  {'name': 'Available', 'room': '104'}
],
[
  {'name': 'Available',  'room': '201'},
  {'name': 'Andres Flores', 'room': '202'},
  {'name': 'Available', 'room': '203'},
  {'name': 'Available', 'room': '204'}
],
[
  {'name': 'Available',  'room': '301'},
  {'name': 'Available', 'room': '302'},
  {'name': 'Ana Soto', 'room': '303'},
  {'name': 'Xochitl Galvez', 'room': '304'}
],
[
  {'name': 'Carlos Maldonado',  'room': '401'},
  {'name': 'Available', 'room': '402'},
  {'name': 'Isable Sanchez', 'room': '403'},
  {'name': 'Available', 'room': '404'}
]]

print('Verificar disponibilidad => presiona 1')
print('Consultar habitacion  => presiona 2')
user_input = input("Presiona tu opcion => ")
print(user_input)

if user_input == '1':
  floor_input = int(input("Elija un piso donde desee verificar disponibilidad (1-4) => "))
  print('-' * 40)
  for room in hotel_matrix[floor_input-1]:
    if room.get('name') == 'Available':
      print("Room: ", room.get('room'), " is available")
elif user_input == '2':
  room_input = input("Habitacion a consultar => ")
  print('-' * 40)
  if room_input.startswith('1'):
    #print("habitacion en piso 1")
    floor_input = int(room_input[0])     
    for room in hotel_matrix[floor_input-1]:
      if not room.get('room') == room_input:
        continue
      else:
        if room.get('name') == 'Available':
          print("Room: ", room.get('room'), " is available")
        else:
          print("Room: ", room.get('room'), " is occupied by ", room.get('name'))
  elif room_input.startswith('2'):
    #print("habitacion en piso 2")
    floor_input = int(room_input[0])    
    for room in hotel_matrix[floor_input-1]:
      if not room.get('room') == room_input:
        continue
      else:
        if room.get('name') == 'Available':
          print("Room: ", room.get('room'), " is available")
        else:
          print("Room: ", room.get('room'), " is occupied by ", room.get('name'))
  elif room_input.startswith('3'):
    #print("habitacion en piso 3")
    floor_input = int(room_input[0])    
    for room in hotel_matrix[floor_input-1]:
      if not room.get('room') == room_input:
        continue
      else:
        if room.get('name') == 'Available':
          print("Room: ", room.get('room'), " is available")
        else:
          print("Room: ", room.get('room'), " is occupied by ", room.get('name'))
  else:
    #print("habitacion en piso 4")
    floor_input = int(room_input[0]) 
    for room in hotel_matrix[floor_input-1]:
      if not room.get('room') == room_input:
        continue
      else:
        if room.get('name') == 'Available':
          print("Room: ", room.get('room'), " is available")
        else:
          print("Room: ", room.get('room'), " is occupied by ", room.get('name'))
      
              
      
      



      






    

