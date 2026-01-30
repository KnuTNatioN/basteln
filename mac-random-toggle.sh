#!/usr/bin/env bash
set -euo pipefail

# -----------------------------------------------------------------------------
# mac-random-toggle.sh
#
# Toggle MAC randomization for NetworkManager by creating/removing:
#   /etc/NetworkManager/conf.d/00-macrandomize.conf
#
# When enabled, the config sets:
#   - wifi.scan-rand-mac-address=yes
#   - wifi/ethernet cloned-mac-address=random
#
# Requires root privileges.
# -----------------------------------------------------------------------------

readonly CONF_FILE="/etc/NetworkManager/conf.d/00-macrandomize.conf"
readonly NM_SERVICE="NetworkManager"

readonly CONF_CONTENT='[device]
wifi.scan-rand-mac-address=yes

[connection]
wifi.cloned-mac-address=random
ethernet.cloned-mac-address=random
'

log()  { printf '%s\n' "$*"; }
info() { printf '[INFO] %s\n' "$*"; }
warn() { printf '[WARN] %s\n' "$*" >&2; }
die()  { printf '[ERR ] %s\n' "$*" >&2; exit 1; }

require_root() {
  if [[ "${EUID:-$(id -u)}" -ne 0 ]]; then
    die "Bitte mit sudo ausführen (z.B.: sudo $0)"
  fi
}

nm_restart() {
  # systemd check (Ubuntu uses systemd, but keep it robust)
  command -v systemctl >/dev/null 2>&1 || die "systemctl nicht gefunden. Kann $NM_SERVICE nicht neustarten."
  systemctl restart "$NM_SERVICE"
}

conf_exists() {
  [[ -f "$CONF_FILE" ]]
}

conf_write() {
  local dir
  dir="$(dirname "$CONF_FILE")"
  mkdir -p "$dir"

  # Atomic write: write to temp file, then move into place
  local tmp
  tmp="$(mktemp)"
  printf '%s' "$CONF_CONTENT" >"$tmp"
  chmod 0644 "$tmp"
  mv -f "$tmp" "$CONF_FILE"
}

conf_remove() {
  rm -f -- "$CONF_FILE"
}

enable_randomization() {
  info "Aktiviere MAC Randomization…"
  conf_write
  nm_restart
  info "MAC Randomization: AN. 🎭 (Neue Identität, gleiches Gerät.)"
}

disable_randomization() {
  info "Deaktiviere MAC Randomization…"
  conf_remove
  nm_restart
  info "MAC Randomization: AUS. 🧯 (Zurück zur Stamm-MAC.)"
}

status() {
  if conf_exists; then
    log "Status: AN (Konfig vorhanden: $CONF_FILE)"
  else
    log "Status: AUS (Konfig fehlt: $CONF_FILE)"
  fi
}

usage() {
  cat <<'EOF'
Usage:
  sudo mac-random-toggle.sh            # toggle on/off
  sudo mac-random-toggle.sh --on       # enable
  sudo mac-random-toggle.sh --off      # disable
  sudo mac-random-toggle.sh --status   # show status
  mac-random-toggle.sh --help          # show help

Notes:
  - Needs root because it writes to /etc/NetworkManager/conf.d/
  - Restarts NetworkManager on changes.
EOF
}

toggle() {
  if conf_exists; then
    disable_randomization
  else
    enable_randomization
  fi
}

main() {
  local cmd="${1:-}"

  case "$cmd" in
    "" )        require_root; toggle ;;
    --on )      require_root; enable_randomization ;;
    --off )     require_root; disable_randomization ;;
    --status )  status ;;
    --help|-h ) usage ;;
    * )         usage; die "Unbekannte Option: $cmd" ;;
  esac
}

main "$@"

