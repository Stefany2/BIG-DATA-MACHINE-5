import cv2
from ultralytics import YOLO

# Cargar el modelo YOLOv8
model = YOLO("yolov8s.pt")

# Inicializar la cámara
capture = cv2.VideoCapture(0)

# Umbral de confianza
confidence_threshold = 0.45

while True:
    
    ret, frame = capture.read()
    
    if not ret:
        break

    # Convertir la imagen de BGR a RGB para que YOLO pueda procesarla
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Realizar la predicción
    results = model(frame_rgb)

    filtered_boxes = []
    
    # Filtrar las cajas detectadas que superen el umbral de confianza y que no sean personas
    for res in results:
        for box in res.boxes:
            if box.conf.item() > confidence_threshold:
                # Obtener el ID de la clase
                class_id = int(box.cls[0])
                
                # Ignorar las detecciones de personas (class_id == 0)
                if class_id == 0:  # La clase 0 corresponde a personas en el modelo YOLO
                    continue
                
                filtered_boxes.append(box)

    # Dibujar las cajas y las etiquetas
    for box in filtered_boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        conf = box.conf[0]
        cls = int(box.cls[0])
        label = model.names[cls]
       
        # Dibujar la caja delimitadora
        cv2.rectangle(frame_rgb, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)

        # Mostrar la etiqueta y la confianza
        label = f"{label} {conf:.2f}"
        cv2.putText(frame_rgb, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Convertir de nuevo la imagen de RGB a BGR para mostrarla en OpenCV
    frame_bgr = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)
    
    # Mostrar el frame con las detecciones
    cv2.imshow('Webcam with Object Detection ', frame_bgr)

    # Salir del bucle al presionar la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar las ventanas
capture.release()
cv2.destroyAllWindows()
