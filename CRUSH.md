# Hyprland Configuration and Scripts

This repository primarily contains configuration files for Hyprland and associated utility scripts.

## File Types:
- `.conf` files: Hyprland configuration.
- Shell scripts: Utility scripts for various tasks.

## General Guidelines:
- **Consistency:** Maintain existing naming conventions and formatting for `.conf` files.
- **Shell Scripts:**
    - Ensure scripts are executable (`chmod +x`).
    - Use descriptive variable names.
    - Add comments for complex logic.
- **Error Handling:** When adding new scripts, include basic error handling where appropriate.
- **Dependencies:** For scripts, clearly state any external dependencies at the top.

## Build/Lint/Test Commands:
- No formal build, lint, or test commands are defined for this repository.
- **Verification:** Changes to `.conf` files should be tested by reloading Hyprland. Scripts should be tested by running them directly.