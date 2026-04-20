import numpy as np

RHO = 1000  # kg/m3
G = 9.8     # m/s2

def hydraulic_power(flow_m3_hr, head_m):
    flow_m3_sec = flow_m3_hr / 3600
    return (RHO * G * flow_m3_sec * head_m) / 1000  # kW

def efficiency(flow, head, input_power):
    output = hydraulic_power(flow, head)
    return output / input_power

def expected_power(flow, head, design_eff=0.65):
    output = hydraulic_power(flow, head)
    return output / design_eff
