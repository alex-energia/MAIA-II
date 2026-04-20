# -*- coding: utf-8 -*- 
import os 
from flask import Flask, render_template_string, request 
app = Flask(__name__) 
@app.route('/', methods=['GET', 'POST']) 
def home(): 
    res = None 
    idea = "" 
    if request.method == 'POST' and 'drone_idea' in request.form: 
        idea = request.form.get('drone_idea', '') 
        res = "active" 
    h = "<html><head><title>MAIA II GLI-60 V-PRO</title><style>" 
    h += "body{background:#000; color:#0ff; font-family:monospace; padding:20px; overflow-x:hidden;}" 
    h += ".panel{border:2px solid #0ff; padding:20px; background:#001a1a; margin-bottom:20px; box-shadow: 0 0 50px #0ff;}" 
    h += "details{background:#050505; border:1px solid #444; margin:10px 0; padding:15px; border-radius:4px;}" 
    h += "summary{font-weight:bold; color:#ffff00; cursor:pointer; padding:5px; text-transform:uppercase;}" 
    h += ".code-view{background:#000; color:#0f0; padding:20px; border-left:4px solid #f0f; white-space:pre; font-size:0.9em; height:550px; overflow-y:scroll; overflow-x:auto; line-height:1.6; border-top: 1px solid #333; margin-top:10px; display:block;}" 
    h += "input{width:60%; background:#000; color:#0ff; border:2px solid #0ff; padding:18px; font-size:1.2em;}" 
    h += "button{padding:18px 25px; font-weight:bold; cursor:pointer; margin:5px; border:none; text-transform:uppercase;}" 
    h += ".folder{margin-left:30px; border-left:2px dotted #f0f; padding-left:20px;}" 
    h += ".hw-spec{background:rgba(0,255,255,0.05); border:1px solid #0ff; padding:20px; margin:15px 0; border-radius:8px; border-left: 5px solid #f0f;}" 
    h += "b{color:#f0f;} .param{color:yellow;}" 
    h += "</style><script>" 
    h += "let v=false; function tVoz(){ let b=document.getElementById('btnVoz'); if(!v){ b.style.background='green'; v=true; " 
    h += "let m=new SpeechSynthesisUtterance('Alex, arquitectura corregida. Desplegando stack vertical sesenta sesenta. Codigo de bajo nivel y DOM tactico activos.'); " 
    h += "m.lang='es-MX'; window.speechSynthesis.speak(m); " 
    h += "} else { window.speechSynthesis.cancel(); v=false; } }" 
    h += "</script></head><body>" 
    h += "<h1> [ M.A.I.A. II - PRODUCTION STACK 60/60 ]</h1>" 
    h += "<div class='panel'><h2>UNIDAD DE INGENIERIA: DEFENSA Y AEROESPACIAL</h2>" 
    h += "<form method='post'><input name='drone_idea' placeholder='Defina especificacion del dron...' value=''>" 
    h += "<button type='submit' style='background:#0ff; color:#000;'>RECOMPILAR SISTEMA</button>" 
    h += "<button type='button' id='btnVoz' style='background:red; color:#fff;' onclick='tVoz()'>VOZ MAIA</button></form></div>" 
    if res: 
        h += "<div class='panel'><h2>EXPEDIENTE TACTICO: " + idea + "</h2>" 
        h += "<details open><summary>[DIR] AGENTE SOFTWARE: 14 NODOS DE PRODUCCION (STRICT VERTICAL)</summary><div class='folder'>" 
        h += "<details><summary>?? control/low_level</summary><div class='folder'><div class='code-view'>// dshot_hal_driver.c - Low Level Motor Control\\n#include ^stm32h7xx_hal.h^\\n\\n#define DSHOT_TICKS_0 40\\n#define DSHOT_TICKS_1 80\\n\\nvoid DSHOT600_Transmit(uint16_t value, uint8_t telemetry) {\\n    uint16_t packet = (value << 1) | (telemetry ? 1 : 0);\\n    uint8_t checksum = (packet ^ (packet >> 4) ^ (packet >> 8)) & 0x0F;\\n    uint16_t frame = (packet << 4) | checksum;\\n\\n    static uint32_t dma_buffer[17];\\n    for (int i = 0; i < 16; i++) {\\n        dma_buffer[i] = (frame & (0x8000 >> i)) ? DSHOT_TICKS_1 : DSHOT_TICKS_0;\\n    }\\n    dma_buffer[16] = 0;\\n\\n    HAL_TIM_PWM_Start_DMA(&htim1, TIM_CHANNEL_1, dma_buffer, 17);\\n    // Verification of bus integrity\\n    if(HAL_TIM_GetChannelState(&htim1, TIM_CHANNEL_1) != HAL_TIM_CHANNEL_STATE_BUSY) {\\n        log_error(ERR_DMA_TRANSFER_FAILED);\\n    }\\n}</div></div></details>" 
        h += "<details><summary>?? ai/perception</summary><div class='folder'><div class='code-view'># perception_engine.py - GPU Accelerated AI\\nimport tensorrt as trt\\nimport pycuda.driver as cuda\\n\\nclass VisionSystem:\\n    def __init__(self, model_path):\\n        self.trt_logger = trt.Logger(trt.Logger.INFO)\\n        with open(model_path, 'rb') as f, trt.Runtime(self.trt_logger) as runtime:\\n            self.engine = runtime.deserialize_cuda_engine(f.read())\\n        self.context = self.engine.create_execution_context()\\n        self.stream = cuda.Stream()\\n\\n    def infer(self, image_input):\\n        # Pre-processing: Normalization and FP16 cast\\n        img = image_input.astype(np.float16) / 255.0\\n        d_input = cuda.mem_alloc(img.nbytes)\\n        cuda.memcpy_htod_async(d_input, img, self.stream)\\n        \\n        # Bindings for input/output pointers\\n        self.context.execute_async_v2(bindings=[int(d_input), int(self.d_output)], stream_handle=self.stream.handle)\\n        self.stream.synchronize()\\n        return self.h_output</div></div></details>" 
        h += "<details><summary>?? fusion/ekf_core</summary><div class='folder'><div class='code-view'>// extended_kalman_core.cpp\\n#include ^Eigen/Dense^\\n\\nMatrix<double, 15, 1> x_state; // p, v, q, b_acc, b_gyro\\n\\nvoid EKF_Update(const Vector3d& measurement, double R_noise) {\\n    Matrix<double, 3, 15> H = MatrixXd::Zero(3, 15);\\n    H.block^0, 0, 3, 3^ = Matrix3d::Identity();\\n\\n    auto S = H * P_cov * H.transpose() + R_noise * Matrix3d::Identity();\\n    auto K = P_cov * H.transpose() * S.inverse();\\n\\n    x_state = x_state + K * (measurement - x_state.head^3^);\\n    P_cov = (MatrixXd::Identity(15, 15) - K * H) * P_cov;\\n    \\n    // Maintain quaternion unit length\\n    Quaterniond q(x_state.segment^6, 4^);\\n    q.normalize();\\n    x_state.segment^6, 4^ << q.w(), q.x(), q.y(), q.z();\\n}</div></div></details>" 
        h += "<details><summary>?? core/rtos</summary><div class='folder'><div class='code-view'>// os_kernel_init.c\\n#include ^FreeRTOS.h^\\n\\nvoid SysInit() {\\n    // Priority 15: Critical Flight Control (400Hz)\\n    xTaskCreate(vFlightControl, ^F_CTRL^, 1024, NULL, 15, NULL);\\n    // Priority 8: SLAM ^ Lidar Processing\\n    xTaskCreate(vSlamTask, ^SLAM^, 4096, NULL, 8, NULL);\\n    // Priority 5: Telemetry ^ MAVLink\\n    xTaskCreate(vCommTask, ^COMM^, 512, NULL, 5, NULL);\\n    vTaskStartScheduler();\\n}</div></div></details>" 
        h += "<details><summary>?? telemetry/mavlink</summary><div class='folder'>?? fast_mavlink_parser.py</div></details>" 
        h += "<details><summary>?? power/bms</summary><div class='folder'>?? can_bms_driver.cpp</div></details>" 
        h += "<details><summary>?? simulation/gazebo</summary><div class='folder'>?? sitl_bridge.cpp</div></details>" 
        h += "<details><summary>?? perception_lidar</summary><div class='folder'>?? ouster_driver.py</div></details>" 
        h += "<details><summary>?? diagnostics</summary><div class='folder'>?? system_health.py</div></details>" 
        h += "<details><summary>?? mission</summary><div class='folder'>?? gcs_sync.cpp</div></details>" 
        h += "<details><summary>?? estimation</summary><div class='folder'>?? ahrs_mahony.c</div></details>" 
        h += "<details><summary>?? communication/mesh</summary><div class='folder'>?? wave_relay_link.py</div></details>" 
        h += "</div></details>" 
        h += "<details open><summary>[DOM] AGENTE HARDWARE: ESPECIFICACION BRUTAL (60% REAL)</summary><div class='folder'>" 
        h += "<div class='hw-spec'><h3>?? COMPUTO Y LOGICA CENTRAL</h3>" 
        h += "<b>Unidad:</b> NVIDIA Jetson Orin Nano (8GB) + FPGA CrossLink-NX<br>" 
        h += "<b>Bus de Sensor:</b> MIPI-CSI 4-Lanes con ancho de banda de 2.5Gbps/lane.<br>" 
        h += "<b>Protocolo de Control:</b> CAN-FD @ 5Mbps para sincronizacion de microsegundos entre nodos.</div>" 
        h += "<div class='hw-spec'><h3>??? ESTRUCTURA Y SIGILO MILITAR</h3>" 
        h += "<b>Material:</b> Fibra de Carbono Torayca M40J con nucleo de panal Nomex (Aeroespacial).<br>" 
        h += "<b>Aislamiento:</b> Pintura de absorcion IR (Radar Absorbent Material - RAM) en secciones criticas.<br>" 
        h += "<b>Motores:</b> KDE Direct 7215XF con ESCs FOC de grado industrial y disipacion de grafeno.</div>" 
        h += "<div class='hw-spec'><h3>?? COMUNICACION Y SENSORES TACTICOS</h3>" 
        h += "<b>Lidar:</b> Ouster OS1-64 (V2) con proteccion IP69K y alcance de 200m al 10% de reflectividad.<br>" 
        h += "<b>Enlace:</b> Persistent Systems MPU5 (Wave Relay) para operacion en entornos denegados por GNSS.<br>" 
        h += "<b>GPS/RTK:</b> u-blox ZED-F9P con correcciones NTRIP para precision de < 1.5 cm.</div>" 
        h += "</div></details></div>" 
    h += "<div class='panel' style='border-color:#f0f;'><h2>PROJECT LAB</h2>" 
    h += "<button>SEARCH PROJECT</button><button style='background:#f0f;'>CREATE NEW PROJECT</button></div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 
