gnomeshell_theme_dir = join_paths(theme_dir, 'gnome-shell')

# generate .css files
theme_sources = files([
  'gnome-shell.scss',
  'gnome-shell-sass/_colors.scss',
  'gnome-shell-sass/_common.scss',
  'gnome-shell-sass/_drawing.scss',
])

styles = [
  'gnome-shell'
]

theme_deps = []

sassc = find_program('sassc')
foreach style: styles
  theme_deps += custom_target('style-' + style,
                              input: '@0@.scss'.format(style),
                              output: '@0@.css'.format(style),
                              command: [
                                sassc, '-a', '@INPUT@', '@OUTPUT@'
                              ],
                              install: true,
                              install_dir: gnomeshell_theme_dir,
                              depend_files: theme_sources)
endforeach

gnomeshell_asset_dir = join_paths(gnomeshell_theme_dir, 'assets')

# static files to copy
gnomeshell_assets = [
  'assets/calendar-arrow-left.svg',
  'assets/calendar-arrow-right.svg',
  'assets/calendar-today-active.svg',
  'assets/calendar-today.svg',
  'assets/checkbox-focused.svg',
  'assets/checkbox-off-focused.svg',
  'assets/checkbox-off.svg',
  'assets/checkbox.svg',
  'assets/close-window-active.svg',
  'assets/close-window-hover.svg',
  'assets/close-window.svg',
  'assets/corner-ripple-ltr.png',
  'assets/corner-ripple-rtl.png',
  'assets/dash-placeholder.svg',
  'assets/key-enter.svg',
  'assets/key-hide.svg',
  'assets/key-layout.svg',
  'assets/key-shift-latched-uppercase.svg',
  'assets/key-shift.svg',
  'assets/key-shift-uppercase.svg',
  'assets/message-indicator-symbolic.svg',
  'assets/no-events.svg',
  'assets/noise-texture.png',
  'assets/no-notifications.svg',
  'assets/page-indicator-active.svg',
  'assets/page-indicator-checked.svg',
  'assets/page-indicator-hover.svg',
  'assets/page-indicator-inactive.svg',
  'assets/process-working.svg',
  'assets/running-indicator.svg',
  'assets/toggle-off.svg',
  'assets/toggle-on.svg',


]

# install static data files
install_data(gnomeshell_assets, install_dir: gnomeshell_asset_dir)
