"""
Exercise: Pipeline health status
Student: Sabita Rajbanshi
Day: 1

"""
# Variables
rows_loaded = 9800
rows_failed = 200
runtime_minutes = 18

# Calculation of total rows
total_rows = rows_loaded + rows_failed

# Calculation of failure percentage
failure_rate = (rows_failed / total_rows) * 100

# Classification of pipeline status based on failure rate and runtime
if failure_rate <= 2 and runtime_minutes <=20:
  pipeline_status = "Healthy"
elif failure_rate <=5:
  pipeline_status = "Warning"
else:
  pipeline_status = "Critical"

# Outputs: failure rate and pipeline status based on input
print(f"Failure rate: {failure_rate:.2f}")
print(f"Pipeline health status: {pipeline_status}")