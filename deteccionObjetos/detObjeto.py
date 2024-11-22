import cv2
from ultralytics import YOLO

# Cargar el modelo YOLO
model = YOLO("yolov8n.pt")  # Modelo ligero (yolov8n) es más rápido; para más precisión usa yolov8s.pt o yolov8m.pt

# Inicializar la cámara
cap = cv2.VideoCapture(0)  # 0 para la cámara predeterminada
cap.set(3, 640)  # Ancho de la cámara
cap.set(4, 480)  # Alto de la cámara

# Establecer tamaño de entrada para el modelo (más pequeño = más rápido)
model.overrides["imgsz"] = 416  # Reduce el tamaño de entrada para mejorar la velocidad (por defecto 640)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error al acceder a la cámara")
        break

    # Realizar la detección de objetos
    results = model.predict(frame, conf=0.35)  # Umbral de confianza ajustado a 0.35 para mayor rapidez

    # Dibujar las cajas delimitadoras y etiquetas
    for result in results:
        boxes = result.boxes  # Coordenadas de las cajas detectadas
        for box in boxes:
            # Extraer información de cada caja
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Coordenadas
            confidence = box.conf[0]  # Confianza de la detección
            class_id = int(box.cls[0])  # ID de la clase

            # Ignorar detecciones de personas (ID de clase 0)
            if class_id == 0:
                continue

            # Obtener el nombre de la clase detectada
            class_name = model.names[class_id]

            # Dibujar caja y etiqueta en la imagen
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{class_name} {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Mostrar el frame con las detecciones
    cv2.imshow("Detección de Objetos (Optimizada)", frame)

    # Presionar 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()
