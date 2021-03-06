import os

from celloapi2 import CelloQuery, CelloResult

# Set our directory variables.
in_dir = os.path.join(os.getcwd(), 'input')
out_dir = os.path.join(os.getcwd(), 'output')

# Set our input files.
chassis_name = 'Eco1C1G1T1'
in_ucf = f'{chassis_name}.UCF.json'
v_file = 'and.v'
options = 'options.csv'
input_sensor_file = f'{chassis_name}.input.json'
output_device_file = f'{chassis_name}.output.json'
q = CelloQuery(
    input_directory=in_dir,
    output_directory=out_dir,
    verilog_file=v_file,
    compiler_options=options,
    input_ucf=in_ucf,
    input_sensors=input_sensor_file,
    output_device=output_device_file,
)


# Submit our query to Cello. This might take a second.
q.get_results()
# Fetch our Results.
res = CelloResult(results_dir=out_dir)
print(res.circuit_score)
