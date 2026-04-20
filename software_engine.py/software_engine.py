# -*- coding: utf-8 -*- 
def get_node_library(idea): 
    return { 
        "01_CORE_RTOS": f"// KERNEL PARA: {idea}\nvoid vTaskFire(void *pv) {{ for(;;) {{ vTaskDelay(10); }} }}", 
        "02_CONTROL_ATTITUDE": f"// CONTROL DE VUELO\nvoid stabilize() {{ float error = get_pitch_error(); apply_pid(error); }}", 
        "03_NAVIGATION_ASTAR": f"// NAVEGACION A-STAR\nvoid find_path() {{ // Algoritmo optimizado para {idea} }}", 
        "04_PERCEPTION_THERMAL": f"// ANALISIS TERMICO\ndef thermal(): return detect_heat_points('{idea}')", 
        "05_PERCEPTION_LIDAR": "// PCL FILTERING\nvoid filter() { ground_rejection(); }", 
        "06_TELEMETRY_MAVLINK": "// MAVLINK V2\nvoid send() { mavlink_msg_heartbeat_send(); }", 
        "07_POWER_BMS": "// BMS REDUNDANTE\nvoid check_power() { if(v < 3.4) return_to_launch(); }", 
        "08_COMM_SILVUS": "// MESH RADIO\nvoid init_radio() { set_freq(4400); }", 
        "09_DIAGNOSTICS_HEALTH": "// HEALTH CHECK\nbool status() { return imu_ok && esc_ok; }", 
        "10_SIMULATION_SITL": "// GAZEBO PHYS\ndef step(): apply_forces()", 
        "11_MISSION_PLANNER": "// MISSION MGMT\nvoid upload() { wp_clear(); wp_set(); }", 
        "12_HARDWARE_HAL": "// HAL LAYER\n#define MOT_1 GPIO_PIN_0", 
        "13_AI_INFERENCE": f"// TENSORRT\ndef predict(): return model.run('{idea}')", 
        "14_FILESYSTEM_LOGS": "// BLACKBOX\nvoid log() { sd_write(timestamp); }" 
    } 
