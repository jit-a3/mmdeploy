_base_ = ['./pose-detection_static.py', '../_base_/backends/openvino.py']

backend_config = dict(
    model_inputs=[dict(opt_shapes=dict(input=[1, 3, 512, 512]))])
onnx_config = dict(
    input_shape=[512, 512],
    output_names=['simcc_x', 'simcc_y'],
    dynamic_axes={
        'input': {
            0: 'batch',
        },
        'simcc_x': {
            0: 'batch'
        },
        'simcc_y': {
            0: 'batch'
        }
    })
