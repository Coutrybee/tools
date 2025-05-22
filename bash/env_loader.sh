# env_loader.sh

load_env_var() {
    local var_name="$1"
    local env_file="$2"

    # grep '^LOG_DIR' "$PROJECT_DIR/.env" | cut -d '=' -f2- | cut -d '#' -f1 | tr -d '"' | xargs
    grep "^$var_name" "$env_file" | cut -d '=' -f2- | cut -d '#' -f1 | tr -d '"' | xargs
}
