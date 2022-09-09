# hotelApiFlask

API em Flask com as seguinte funcionalidades:

1. Endpoint de consulta do hotel mais barato
2. Endpoint para realizar a reserva. 
	* Entradas: Nome, telefone, email, período, Hotel, tipo de reserva (Regular ou Reward) e observações. Saídas: número da reserva.
3. Endpoint para consultar reservas. 
	* Entradas: número da reserva, hotel, tipo de reserva (Regular ou Reward) e período. 
	* Saída: lista de reservas com número da reserva, nome,
telefone, email, período, hotel, tipo de reserva (Regular ou Reward), preço.
4. Endpoint para cancelar reservas. 
	* Entrada: a reserva a ser cancelada. 
	* Saída: informação de sucesso ou falha
