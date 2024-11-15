# Check if an argument (file to transfer) is provided
param (
    [string]$filePath
)

# Ensure the file path is provided
if (-not $filePath) {
    Write-Host "Error: You must provide a file to transfer." -ForegroundColor Red
    exit 1
}

# Define the destination information
$username = "pichones_pi"
$hostname = "raspberrypi.local"
$destination = "/home/pichones_pi/Documents"

# Use string interpolation to reference variables in the SCP command
$scpCommand = "scp -r $filePath ${username}@${hostname}:${destination}"

# Execute the SCP command
Invoke-Expression $scpCommand

# Output result
if ($LASTEXITCODE -eq 0) {
    Write-Host "File transfer completed successfully."
} else {
    Write-Host "Error: File transfer failed." -ForegroundColor Red
}
