# debian_version_mapping.sh
#!/bin/sh

# This script is used to map the Debian version to the appropriate Docker image tag.
# The script is called with the Debian version as the first argument and should echo the Docker image tag to use.

# Run the following commands to test this script:
# chmod +x .devcontainer/debian_version_mapping.sh
# ./.devcontainer/debian_version_mapping.sh 12

case "$1" in
  12) echo "bookworm" ;;
  13) echo "trixie" ;;
  # Add more mappings as needed
  *) echo "unknown" ;;
esac
