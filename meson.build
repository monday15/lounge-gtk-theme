project('lounge-gtk-theme',
        version: '1.4',
        meson_version: '>= 0.40',
        license : ['GPL3+'],
        default_options: ['prefix=/usr'])

# Dependencies

sassc = find_program('sassc')
gnomeshell = find_program('gnome-shell', required: false)


# Installation directories

theme_dir = join_paths(get_option('datadir'), 'themes', 'Lounge')
shell_dir = join_paths(theme_dir, 'gnome-shell')
shell_asset_dir = join_paths(shell_dir, 'assets')
gtk2_dir = join_paths(theme_dir, 'gtk-2.0')
gtk2_asset_dir = join_paths(gtk2_dir, 'assets')

gtk322_dir = join_paths(theme_dir, 'gtk-3.22')
gtk324_dir = join_paths(theme_dir, 'gtk-3.24')
gtk3_asset_dir = join_paths(theme_dir, 'gtk3-assets')

  # Dark theme

dark_theme_dir = join_paths(get_option('datadir'), 'themes', 'Lounge-night')
dark_gtk2_dir = join_paths(dark_theme_dir, 'gtk-2.0')
dark_gtk2_asset_dir = join_paths(dark_gtk2_dir, 'assets')

dark_gtk322_dir = join_paths(dark_theme_dir, 'gtk-3.22')
dark_gtk324_dir = join_paths(dark_theme_dir, 'gtk-3.24')
dark_gtk3_asset_dir = join_paths(dark_theme_dir, 'gtk3-assets')


# Install index files

  # Copy used for preventing meson warnings, it is not changing anything,
  # only copies index file for night theme under a different name. 

index_file = [ 'src/index.theme' ]
install_data(index_file, install_dir: theme_dir)

copy = configuration_data()
copy.set('something', 'something')
configure_file(input : 'src/index.theme-dark',
               output : 'index.theme',
               configuration : copy,
               install_dir: dark_theme_dir)


# Generate and install gnome-shell theme

shell_sources = [
  '_colors-shell.scss',
  '_drawing-shell.scss',
  '_common-shell.scss',
  '_common-shell-3-28.scss',
  '_common-shell-3-30.scss',
]

shell_conf = configuration_data()

  # Check gnome-shell version

if gnomeshell.found()
  gnomeshell_res = run_command([gnomeshell, '--version'])
  gnomeshell_ver = gnomeshell_res.stdout().split('\n')[0].split(' ')[-1].strip()

  if gnomeshell_ver.version_compare('<3.30')
    message('Gnome-shell version <3.30')
    shell_conf.set('common_var', '_common-shell-3-28.scss')
  else
    message('Gnome-shell version >=3.30')
    shell_conf.set('common_var', '_common-shell-3-30.scss')

  endif

else
  message('Gnome-shell not found, using last version availible')
  shell_conf.set('common_var', '_common-shell-3-30.scss')

endif

  # Configure scss file for building right version of shell theme

shell_scss = configure_file(input : 'src/gnome-shell/gnome-shell.scss',
                            output : 'gnome-shell.scss',
                            configuration : shell_conf)

  # Copy sources to builddir

foreach file : shell_sources
configure_file(input : join_paths('src/gnome-shell/' + file),
               output : file,
               configuration : copy)
endforeach

  # Generate shell theme

custom_target('shell-gen',
              input: shell_scss,
              output: 'gnome-shell.css',
              command: [ sassc, '-a', '@INPUT@', '@OUTPUT@'],
              install: true,
              install_dir: shell_dir,
              build_by_default: true)


# Install gtk2 theme

gtk2_data = [
  'src/gtk-2.0/gtkrc',
  'src/gtk-2.0/main.rc',
  'src/gtk-2.0/apps.rc',
  'src/gtk-2.0/hacks.rc',
]

dark_gtk2_data = [
  'src/gtk-2.0-dark/gtkrc',
  'src/gtk-2.0-dark/main.rc',
  'src/gtk-2.0-dark/apps.rc',
  'src/gtk-2.0-dark/hacks.rc',
]

install_data(gtk2_data, install_dir: gtk2_dir)
install_data(dark_gtk2_data, install_dir: dark_gtk2_dir)


# Generate and install gtk3 theme

gtk3_sources = [
  '_colors-public.scss',
  '_colors.scss',
  '_common.scss',
  '_common-3-22.scss',
  '_common-3-24.scss',
  '_apps.scss',
  '_apps-3-28.scss',
  '_apps-3-30.scss',
  '_drawing.scss',
  '_apps-nautilus-3-28.scss',
  '_apps-nautilus-3-30.scss',
]

gtk3_version = [
  '3-22',
  '3-24',
]

foreach ver : gtk3_version

  if ver == '3-22'
    gnome_version = '3-28'
  endif
  if ver == '3-24'
    gnome_version = '3-30'
  endif

gtk3_conf = configuration_data()
gtk3_conf.set('common_var', 'common-' + ver)
gtk3_conf.set('apps_var', 'apps-' + gnome_version)
gtk3_conf.set('apps_nautilus_var', 'apps-nautilus-' + gnome_version)

gtk3_scss = configure_file(input : 'src/gtk-3.0/gtk.scss',
                           output : 'gtk-' + ver + '.scss',
                           configuration : gtk3_conf)

gtk3_scss_dark = configure_file(input : 'src/gtk-3.0/gtk-dark.scss',
                                output : 'gtk-dark-' + ver + '.scss',
                                configuration : gtk3_conf)

endforeach

foreach file : gtk3_sources
configure_file(input : join_paths('src/gtk-3.0/' + file),
               output : file,
               configuration : copy)
endforeach

gtk322_scss_light = join_paths(meson.build_root(), 'gtk-3-22.scss')
gtk322_scss_dark  = join_paths(meson.build_root(), 'gtk-dark-3-22.scss')

gtk324_scss_light = join_paths(meson.build_root(), 'gtk-3-24.scss')
gtk324_scss_dark  = join_paths(meson.build_root(), 'gtk-dark-3-24.scss')

  custom_target('gtk322-light',
                input: gtk322_scss_light,
                output: 'gtk.css',
                command: [ sassc, '-M', '-t', 'compact', '@INPUT@', '@OUTPUT@', ],
                install: true,
                install_dir: gtk322_dir, 
                build_by_default: true)

  custom_target('gtk322-dark',
                input: gtk322_scss_dark,
                output: 'gtk-dark.css',
                command: [ sassc, '-M', '-t', 'compact', '@INPUT@', '@OUTPUT@', ],
                install: true,
                install_dir: gtk322_dir,
                build_by_default: true)


  custom_target('gtk324-light',
                input: gtk324_scss_light,
                output: 'gtk324.css',
                command: [ sassc, '-M', '-t', 'compact', '@INPUT@', '@OUTPUT@', ],
                install: true,
                install_dir: gtk324_dir,
                build_by_default: true)

  custom_target('gtk324-dark',
                input: gtk324_scss_dark,
                output: 'gtk-dark324.css',
                command: [ sassc, '-M', '-t', 'compact', '@INPUT@', '@OUTPUT@', ],
                install: true,
                install_dir: gtk324_dir,
                build_by_default: true)

  # Rename Lounge dark variant css files
  meson.add_install_script('sh', '-c', 'mv $MESON_INSTALL_DESTDIR_PREFIX/'+gtk324_dir+'/gtk-dark324.css $MESON_INSTALL_DESTDIR_PREFIX/'+gtk324_dir+'/gtk-dark.css')
  meson.add_install_script('sh', '-c', 'mv $MESON_INSTALL_DESTDIR_PREFIX/'+gtk324_dir+'/gtk324.css $MESON_INSTALL_DESTDIR_PREFIX/'+gtk324_dir+'/gtk.css')

  # Create subfolders for Lounge-night theme
  meson.add_install_script('sh', '-c', 'mkdir -p $MESON_INSTALL_DESTDIR_PREFIX/'+dark_gtk322_dir)
  meson.add_install_script('sh', '-c', 'mkdir -p $MESON_INSTALL_DESTDIR_PREFIX/'+dark_gtk324_dir)

  # Copy Lounge dark variant css files to Lounge-night theme
  meson.add_install_script('sh', '-c', 'cp $MESON_INSTALL_DESTDIR_PREFIX/'+gtk322_dir+'/gtk-dark.css $MESON_INSTALL_DESTDIR_PREFIX/'+dark_gtk322_dir+'/gtk.css')
  meson.add_install_script('sh', '-c', 'cp $MESON_INSTALL_DESTDIR_PREFIX/'+gtk324_dir+'/gtk-dark.css $MESON_INSTALL_DESTDIR_PREFIX/'+dark_gtk324_dir+'/gtk.css')


# Install assets

gnomeshell_assets = [
  'src/gnome-shell/assets/calendar-arrow-left.svg',
  'src/gnome-shell/assets/calendar-arrow-right.svg',
  'src/gnome-shell/assets/calendar-today-active.svg',
  'src/gnome-shell/assets/calendar-today.svg',
  'src/gnome-shell/assets/checkbox-focused.svg',
  'src/gnome-shell/assets/checkbox-off-focused.svg',
  'src/gnome-shell/assets/checkbox-off.svg',
  'src/gnome-shell/assets/checkbox.svg',
  'src/gnome-shell/assets/close-window-active.svg',
  'src/gnome-shell/assets/close-window-hover.svg',
  'src/gnome-shell/assets/close-window.svg',
  'src/gnome-shell/assets/corner-ripple-ltr.png',
  'src/gnome-shell/assets/corner-ripple-rtl.png',
  'src/gnome-shell/assets/dash-placeholder.svg',
  'src/gnome-shell/assets/key-enter.svg',
  'src/gnome-shell/assets/key-hide.svg',
  'src/gnome-shell/assets/key-layout.svg',
  'src/gnome-shell/assets/key-shift-latched-uppercase.svg',
  'src/gnome-shell/assets/key-shift.svg',
  'src/gnome-shell/assets/key-shift-uppercase.svg',
  'src/gnome-shell/assets/message-indicator-symbolic.svg',
  'src/gnome-shell/assets/no-events.svg',
  'src/gnome-shell/assets/noise-texture.png',
  'src/gnome-shell/assets/no-notifications.svg',
  'src/gnome-shell/assets/page-indicator-active.svg',
  'src/gnome-shell/assets/page-indicator-checked.svg',
  'src/gnome-shell/assets/page-indicator-hover.svg',
  'src/gnome-shell/assets/page-indicator-inactive.svg',
  'src/gnome-shell/assets/process-working.svg',
  'src/gnome-shell/assets/running-indicator.svg',
  'src/gnome-shell/assets/toggle-off.svg',
  'src/gnome-shell/assets/toggle-on.svg',
]

gtk2_assets = [
  'src/gtk-2.0/assets/border.png',
  'src/gtk-2.0/assets/button-active.png',
  'src/gtk-2.0/assets/button-hover.png',
  'src/gtk-2.0/assets/button-insensitive.png',
  'src/gtk-2.0/assets/button.png',
  'src/gtk-2.0/assets/checkbox-checked-active.png',
  'src/gtk-2.0/assets/checkbox-checked-hover.png',
  'src/gtk-2.0/assets/checkbox-checked-insensitive.png',
  'src/gtk-2.0/assets/checkbox-checked.png',
  'src/gtk-2.0/assets/checkbox-mixed-active.png',
  'src/gtk-2.0/assets/checkbox-mixed-hover.png',
  'src/gtk-2.0/assets/checkbox-mixed-insensitive.png',
  'src/gtk-2.0/assets/checkbox-mixed.png',
  'src/gtk-2.0/assets/checkbox-unchecked-active.png',
  'src/gtk-2.0/assets/checkbox-unchecked-hover.png',
  'src/gtk-2.0/assets/checkbox-unchecked-insensitive.png',
  'src/gtk-2.0/assets/checkbox-unchecked.png',
  'src/gtk-2.0/assets/combo-entry-ltr-button-active.png',
  'src/gtk-2.0/assets/combo-entry-ltr-button-hover.png',
  'src/gtk-2.0/assets/combo-entry-ltr-button-insensitive.png',
  'src/gtk-2.0/assets/combo-entry-ltr-button.png',
  'src/gtk-2.0/assets/combo-entry-ltr-entry-active.png',
  'src/gtk-2.0/assets/combo-entry-ltr-entry-insensitive.png',
  'src/gtk-2.0/assets/combo-entry-ltr-entry.png',
  'src/gtk-2.0/assets/combo-entry-rtl-button-active.png',
  'src/gtk-2.0/assets/combo-entry-rtl-button-hover.png',
  'src/gtk-2.0/assets/combo-entry-rtl-button-insensitive.png',
  'src/gtk-2.0/assets/combo-entry-rtl-button.png',
  'src/gtk-2.0/assets/combo-entry-rtl-entry-active.png',
  'src/gtk-2.0/assets/combo-entry-rtl-entry-insensitive.png',
  'src/gtk-2.0/assets/combo-entry-rtl-entry.png',
  'src/gtk-2.0/assets/entry-active.png',
  'src/gtk-2.0/assets/entry-background-insensitive.png',
  'src/gtk-2.0/assets/entry-background.png',
  'src/gtk-2.0/assets/entry-insensitive.png',
  'src/gtk-2.0/assets/entry.png',
  'src/gtk-2.0/assets/focus.png',
  'src/gtk-2.0/assets/frame-inline.png',
  'src/gtk-2.0/assets/frame-notebook.png',
  'src/gtk-2.0/assets/frame.png',
  'src/gtk-2.0/assets/handle-horz.png',
  'src/gtk-2.0/assets/handle.png',
  'src/gtk-2.0/assets/handle-vert.png',
  'src/gtk-2.0/assets/line.png',
  'src/gtk-2.0/assets/menu-border.png',
  'src/gtk-2.0/assets/menu-checkbox-checked-insensitive.png',
  'src/gtk-2.0/assets/menu-checkbox-checked.png',
  'src/gtk-2.0/assets/menu-checkbox-insensitive.png',
  'src/gtk-2.0/assets/menu-checkbox-mixed-insensitive.png',
  'src/gtk-2.0/assets/menu-checkbox-mixed.png',
  'src/gtk-2.0/assets/menu-checkbox.png',
  'src/gtk-2.0/assets/menu-item-active.png',
  'src/gtk-2.0/assets/menu-radio-checked-insensitive.png',
  'src/gtk-2.0/assets/menu-radio-checked.png',
  'src/gtk-2.0/assets/menu-radio-insensitive.png',
  'src/gtk-2.0/assets/menu-radio-mixed-insensitive.png',
  'src/gtk-2.0/assets/menu-radio-mixed.png',
  'src/gtk-2.0/assets/menu-radio.png',
  'src/gtk-2.0/assets/notebook-combo-entry-ltr-entry-active.png',
  'src/gtk-2.0/assets/notebook-combo-entry-ltr-entry-insensitive.png',
  'src/gtk-2.0/assets/notebook-combo-entry-ltr-entry.png',
  'src/gtk-2.0/assets/notebook-combo-entry-rtl-entry-active.png',
  'src/gtk-2.0/assets/notebook-combo-entry-rtl-entry-insensitive.png',
  'src/gtk-2.0/assets/notebook-combo-entry-rtl-entry.png',
  'src/gtk-2.0/assets/notebook-entry-active.png',
  'src/gtk-2.0/assets/notebook-entry-insensitive.png',
  'src/gtk-2.0/assets/notebook-entry.png',
  'src/gtk-2.0/assets/pan-down-insensitive.png',
  'src/gtk-2.0/assets/pan-down.png',
  'src/gtk-2.0/assets/pan-left-insensitive.png',
  'src/gtk-2.0/assets/pan-left.png',
  'src/gtk-2.0/assets/pan-left-semi.png',
  'src/gtk-2.0/assets/pan-right-insensitive.png',
  'src/gtk-2.0/assets/pan-right.png',
  'src/gtk-2.0/assets/pan-right-semi.png',
  'src/gtk-2.0/assets/pan-up-insensitive.png',
  'src/gtk-2.0/assets/pan-up.png',
  'src/gtk-2.0/assets/progressbar-horz.png',
  'src/gtk-2.0/assets/progressbar-trough-horz.png',
  'src/gtk-2.0/assets/progressbar-trough-vert.png',
  'src/gtk-2.0/assets/progressbar-vert.png',
  'src/gtk-2.0/assets/radio-checked-active.png',
  'src/gtk-2.0/assets/radio-checked-hover.png',
  'src/gtk-2.0/assets/radio-checked-insensitive.png',
  'src/gtk-2.0/assets/radio-checked.png',
  'src/gtk-2.0/assets/radio-mixed-active.png',
  'src/gtk-2.0/assets/radio-mixed-hover.png',
  'src/gtk-2.0/assets/radio-mixed-insensitive.png',
  'src/gtk-2.0/assets/radio-mixed.png',
  'src/gtk-2.0/assets/radio-unchecked-active.png',
  'src/gtk-2.0/assets/radio-unchecked-hover.png',
  'src/gtk-2.0/assets/radio-unchecked-insensitive.png',
  'src/gtk-2.0/assets/radio-unchecked.png',
  'src/gtk-2.0/assets/scale-horz-trough-active.png',
  'src/gtk-2.0/assets/scale-horz-trough.png',
  'src/gtk-2.0/assets/scale-slider-active.png',
  'src/gtk-2.0/assets/scale-slider-hover.png',
  'src/gtk-2.0/assets/scale-slider-insensitive.png',
  'src/gtk-2.0/assets/scale-slider.png',
  'src/gtk-2.0/assets/scale-vert-trough-active.png',
  'src/gtk-2.0/assets/scale-vert-trough.png',
  'src/gtk-2.0/assets/scrollbar-slider-active.png',
  'src/gtk-2.0/assets/scrollbar-slider.png',
  'src/gtk-2.0/assets/scrollbar-trough.png',
  'src/gtk-2.0/assets/spin-down-insensitive.png',
  'src/gtk-2.0/assets/spin-down.png',
  'src/gtk-2.0/assets/spin-ltr-down-active.png',
  'src/gtk-2.0/assets/spin-ltr-down-hover.png',
  'src/gtk-2.0/assets/spin-ltr-down-insensitive.png',
  'src/gtk-2.0/assets/spin-ltr-down.png',
  'src/gtk-2.0/assets/spin-ltr-up-active.png',
  'src/gtk-2.0/assets/spin-ltr-up-hover.png',
  'src/gtk-2.0/assets/spin-ltr-up-insensitive.png',
  'src/gtk-2.0/assets/spin-ltr-up.png',
  'src/gtk-2.0/assets/spin-rtl-down-active.png',
  'src/gtk-2.0/assets/spin-rtl-down-hover.png',
  'src/gtk-2.0/assets/spin-rtl-down-insensitive.png',
  'src/gtk-2.0/assets/spin-rtl-down.png',
  'src/gtk-2.0/assets/spin-rtl-up-active.png',
  'src/gtk-2.0/assets/spin-rtl-up-hover.png',
  'src/gtk-2.0/assets/spin-rtl-up-insensitive.png',
  'src/gtk-2.0/assets/spin-rtl-up.png',
  'src/gtk-2.0/assets/spin-up-insensitive.png',
  'src/gtk-2.0/assets/spin-up.png',
  'src/gtk-2.0/assets/tooltip-bg.png',
  'src/gtk-2.0/assets/tab-down-active.png',
  'src/gtk-2.0/assets/tab-horz-gap.png',
  'src/gtk-2.0/assets/tab-left-active.png',
  'src/gtk-2.0/assets/tab-right-active.png',
  'src/gtk-2.0/assets/tab-up-active.png',
  'src/gtk-2.0/assets/tab-vert-gap.png',
  'src/gtk-2.0/assets/transparent-dot.png',
  'src/gtk-2.0/assets/treeview-pan-down-active.png',
  'src/gtk-2.0/assets/treeview-pan-down-hover.png',
  'src/gtk-2.0/assets/treeview-pan-down.png',
  'src/gtk-2.0/assets/treeview-pan-up-active.png',
  'src/gtk-2.0/assets/treeview-pan-up-hover.png',
  'src/gtk-2.0/assets/treeview-pan-up.png',
  'src/gtk-2.0/assets/treeview-separator-ltr.png',
  'src/gtk-2.0/assets/treeview-separator-rtl.png',
]

dark_gtk2_assets = [
  'src/gtk-2.0-dark/assets/border.png',
  'src/gtk-2.0-dark/assets/button-active.png',
  'src/gtk-2.0-dark/assets/button-hover.png',
  'src/gtk-2.0-dark/assets/button-insensitive.png',
  'src/gtk-2.0-dark/assets/button.png',
  'src/gtk-2.0-dark/assets/checkbox-checked-active.png',
  'src/gtk-2.0-dark/assets/checkbox-checked-hover.png',
  'src/gtk-2.0-dark/assets/checkbox-checked-insensitive.png',
  'src/gtk-2.0-dark/assets/checkbox-checked.png',
  'src/gtk-2.0-dark/assets/checkbox-mixed-active.png',
  'src/gtk-2.0-dark/assets/checkbox-mixed-hover.png',
  'src/gtk-2.0-dark/assets/checkbox-mixed-insensitive.png',
  'src/gtk-2.0-dark/assets/checkbox-mixed.png',
  'src/gtk-2.0-dark/assets/checkbox-unchecked-active.png',
  'src/gtk-2.0-dark/assets/checkbox-unchecked-hover.png',
  'src/gtk-2.0-dark/assets/checkbox-unchecked-insensitive.png',
  'src/gtk-2.0-dark/assets/checkbox-unchecked.png',
  'src/gtk-2.0-dark/assets/combo-entry-ltr-button-active.png',
  'src/gtk-2.0-dark/assets/combo-entry-ltr-button-hover.png',
  'src/gtk-2.0-dark/assets/combo-entry-ltr-button-insensitive.png',
  'src/gtk-2.0-dark/assets/combo-entry-ltr-button.png',
  'src/gtk-2.0-dark/assets/combo-entry-ltr-entry-active.png',
  'src/gtk-2.0-dark/assets/combo-entry-ltr-entry-insensitive.png',
  'src/gtk-2.0-dark/assets/combo-entry-ltr-entry.png',
  'src/gtk-2.0-dark/assets/combo-entry-rtl-button-active.png',
  'src/gtk-2.0-dark/assets/combo-entry-rtl-button-hover.png',
  'src/gtk-2.0-dark/assets/combo-entry-rtl-button-insensitive.png',
  'src/gtk-2.0-dark/assets/combo-entry-rtl-button.png',
  'src/gtk-2.0-dark/assets/combo-entry-rtl-entry-active.png',
  'src/gtk-2.0-dark/assets/combo-entry-rtl-entry-insensitive.png',
  'src/gtk-2.0-dark/assets/combo-entry-rtl-entry.png',
  'src/gtk-2.0-dark/assets/entry-active.png',
  'src/gtk-2.0-dark/assets/entry-background-insensitive.png',
  'src/gtk-2.0-dark/assets/entry-background.png',
  'src/gtk-2.0-dark/assets/entry-insensitive.png',
  'src/gtk-2.0-dark/assets/entry.png',
  'src/gtk-2.0-dark/assets/focus.png',
  'src/gtk-2.0-dark/assets/frame-inline.png',
  'src/gtk-2.0-dark/assets/frame-notebook.png',
  'src/gtk-2.0-dark/assets/frame.png',
  'src/gtk-2.0-dark/assets/handle-horz.png',
  'src/gtk-2.0-dark/assets/handle.png',
  'src/gtk-2.0-dark/assets/handle-vert.png',
  'src/gtk-2.0-dark/assets/line.png',
  'src/gtk-2.0-dark/assets/menu-border.png',
  'src/gtk-2.0-dark/assets/menu-checkbox-checked-insensitive.png',
  'src/gtk-2.0-dark/assets/menu-checkbox-checked.png',
  'src/gtk-2.0-dark/assets/menu-checkbox-insensitive.png',
  'src/gtk-2.0-dark/assets/menu-checkbox-mixed-insensitive.png',
  'src/gtk-2.0-dark/assets/menu-checkbox-mixed.png',
  'src/gtk-2.0-dark/assets/menu-checkbox.png',
  'src/gtk-2.0-dark/assets/menu-item-active.png',
  'src/gtk-2.0-dark/assets/menu-radio-checked-insensitive.png',
  'src/gtk-2.0-dark/assets/menu-radio-checked.png',
  'src/gtk-2.0-dark/assets/menu-radio-insensitive.png',
  'src/gtk-2.0-dark/assets/menu-radio-mixed-insensitive.png',
  'src/gtk-2.0-dark/assets/menu-radio-mixed.png',
  'src/gtk-2.0-dark/assets/menu-radio.png',
  'src/gtk-2.0-dark/assets/notebook-combo-entry-ltr-entry-active.png',
  'src/gtk-2.0-dark/assets/notebook-combo-entry-ltr-entry-insensitive.png',
  'src/gtk-2.0-dark/assets/notebook-combo-entry-ltr-entry.png',
  'src/gtk-2.0-dark/assets/notebook-combo-entry-rtl-entry-active.png',
  'src/gtk-2.0-dark/assets/notebook-combo-entry-rtl-entry-insensitive.png',
  'src/gtk-2.0-dark/assets/notebook-combo-entry-rtl-entry.png',
  'src/gtk-2.0-dark/assets/notebook-entry-active.png',
  'src/gtk-2.0-dark/assets/notebook-entry-insensitive.png',
  'src/gtk-2.0-dark/assets/notebook-entry.png',
  'src/gtk-2.0-dark/assets/pan-down-insensitive.png',
  'src/gtk-2.0-dark/assets/pan-down.png',
  'src/gtk-2.0-dark/assets/pan-left-insensitive.png',
  'src/gtk-2.0-dark/assets/pan-left.png',
  'src/gtk-2.0-dark/assets/pan-left-semi.png',
  'src/gtk-2.0-dark/assets/pan-right-insensitive.png',
  'src/gtk-2.0-dark/assets/pan-right.png',
  'src/gtk-2.0-dark/assets/pan-right-semi.png',
  'src/gtk-2.0-dark/assets/pan-up-insensitive.png',
  'src/gtk-2.0-dark/assets/pan-up.png',
  'src/gtk-2.0-dark/assets/progressbar-horz.png',
  'src/gtk-2.0-dark/assets/progressbar-trough-horz.png',
  'src/gtk-2.0-dark/assets/progressbar-trough-vert.png',
  'src/gtk-2.0-dark/assets/progressbar-vert.png',
  'src/gtk-2.0-dark/assets/radio-checked-active.png',
  'src/gtk-2.0-dark/assets/radio-checked-hover.png',
  'src/gtk-2.0-dark/assets/radio-checked-insensitive.png',
  'src/gtk-2.0-dark/assets/radio-checked.png',
  'src/gtk-2.0-dark/assets/radio-mixed-active.png',
  'src/gtk-2.0-dark/assets/radio-mixed-hover.png',
  'src/gtk-2.0-dark/assets/radio-mixed-insensitive.png',
  'src/gtk-2.0-dark/assets/radio-mixed.png',
  'src/gtk-2.0-dark/assets/radio-unchecked-active.png',
  'src/gtk-2.0-dark/assets/radio-unchecked-hover.png',
  'src/gtk-2.0-dark/assets/radio-unchecked-insensitive.png',
  'src/gtk-2.0-dark/assets/radio-unchecked.png',
  'src/gtk-2.0-dark/assets/scale-horz-trough-active.png',
  'src/gtk-2.0-dark/assets/scale-horz-trough.png',
  'src/gtk-2.0-dark/assets/scale-slider-active.png',
  'src/gtk-2.0-dark/assets/scale-slider-hover.png',
  'src/gtk-2.0-dark/assets/scale-slider-insensitive.png',
  'src/gtk-2.0-dark/assets/scale-slider.png',
  'src/gtk-2.0-dark/assets/scale-vert-trough-active.png',
  'src/gtk-2.0-dark/assets/scale-vert-trough.png',
  'src/gtk-2.0-dark/assets/scrollbar-slider-active.png',
  'src/gtk-2.0-dark/assets/scrollbar-slider.png',
  'src/gtk-2.0-dark/assets/scrollbar-trough.png',
  'src/gtk-2.0-dark/assets/spin-down-insensitive.png',
  'src/gtk-2.0-dark/assets/spin-down.png',
  'src/gtk-2.0-dark/assets/spin-ltr-down-active.png',
  'src/gtk-2.0-dark/assets/spin-ltr-down-hover.png',
  'src/gtk-2.0-dark/assets/spin-ltr-down-insensitive.png',
  'src/gtk-2.0-dark/assets/spin-ltr-down.png',
  'src/gtk-2.0-dark/assets/spin-ltr-up-active.png',
  'src/gtk-2.0-dark/assets/spin-ltr-up-hover.png',
  'src/gtk-2.0-dark/assets/spin-ltr-up-insensitive.png',
  'src/gtk-2.0-dark/assets/spin-ltr-up.png',
  'src/gtk-2.0-dark/assets/spin-rtl-down-active.png',
  'src/gtk-2.0-dark/assets/spin-rtl-down-hover.png',
  'src/gtk-2.0-dark/assets/spin-rtl-down-insensitive.png',
  'src/gtk-2.0-dark/assets/spin-rtl-down.png',
  'src/gtk-2.0-dark/assets/spin-rtl-up-active.png',
  'src/gtk-2.0-dark/assets/spin-rtl-up-hover.png',
  'src/gtk-2.0-dark/assets/spin-rtl-up-insensitive.png',
  'src/gtk-2.0-dark/assets/spin-rtl-up.png',
  'src/gtk-2.0-dark/assets/spin-up-insensitive.png',
  'src/gtk-2.0-dark/assets/spin-up.png',
  'src/gtk-2.0-dark/assets/tooltip-bg.png',
  'src/gtk-2.0-dark/assets/tab-down-active.png',
  'src/gtk-2.0-dark/assets/tab-horz-gap.png',
  'src/gtk-2.0-dark/assets/tab-left-active.png',
  'src/gtk-2.0-dark/assets/tab-right-active.png',
  'src/gtk-2.0-dark/assets/tab-up-active.png',
  'src/gtk-2.0-dark/assets/tab-vert-gap.png',
  'src/gtk-2.0-dark/assets/transparent-dot.png',
  'src/gtk-2.0-dark/assets/treeview-pan-down-active.png',
  'src/gtk-2.0-dark/assets/treeview-pan-down-hover.png',
  'src/gtk-2.0-dark/assets/treeview-pan-down.png',
  'src/gtk-2.0-dark/assets/treeview-pan-up-active.png',
  'src/gtk-2.0-dark/assets/treeview-pan-up-hover.png',
  'src/gtk-2.0-dark/assets/treeview-pan-up.png',
  'src/gtk-2.0-dark/assets/treeview-separator-ltr.png',
  'src/gtk-2.0-dark/assets/treeview-separator-rtl.png',
]

gtk3_assets = [
  'src/gtk-3.0/assets/bullet-symbolic.svg',
  'src/gtk-3.0/assets/bullet-symbolic.symbolic.png',
  'src/gtk-3.0/assets/checkbox-active-selectionmode@2.png',
  'src/gtk-3.0/assets/checkbox-active-selectionmode.png',
  'src/gtk-3.0/assets/checkbox-backdrop-selectionmode@2.png',
  'src/gtk-3.0/assets/checkbox-backdrop-selectionmode.png',
  'src/gtk-3.0/assets/checkbox-checked-active-selectionmode@2.png',
  'src/gtk-3.0/assets/checkbox-checked-active-selectionmode.png',
  'src/gtk-3.0/assets/checkbox-checked-backdrop-selectionmode@2.png',
  'src/gtk-3.0/assets/checkbox-checked-backdrop-selectionmode.png',
  'src/gtk-3.0/assets/checkbox-checked-hover-selectionmode@2.png',
  'src/gtk-3.0/assets/checkbox-checked-hover-selectionmode.png',
  'src/gtk-3.0/assets/checkbox-checked-selectionmode@2.png',
  'src/gtk-3.0/assets/checkbox-checked-selectionmode.png',
  'src/gtk-3.0/assets/checkbox-hover-selectionmode@2.png',
  'src/gtk-3.0/assets/checkbox-hover-selectionmode.png',
  'src/gtk-3.0/assets/checkbox-selectionmode@2.png',
  'src/gtk-3.0/assets/checkbox-selectionmode.png',
  'src/gtk-3.0/assets/check-symbolic.svg',
  'src/gtk-3.0/assets/check-symbolic.symbolic.png',
  'src/gtk-3.0/assets/dash-symbolic.svg',
  'src/gtk-3.0/assets/dash-symbolic.symbolic.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-active@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-active-dark@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-active-dark.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-active.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-backdrop@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-backdrop-dark@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-backdrop-dark.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-backdrop-insensitive@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-backdrop-insensitive-dark@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-backdrop-insensitive-dark.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-backdrop-insensitive.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-backdrop.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-dark@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-dark.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-hover@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-hover-dark@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-hover-dark.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-hover.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-insensitive@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-insensitive-dark@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-insensitive-dark.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-insensitive.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-active@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-active-dark@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-active-dark.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-active.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-backdrop@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-backdrop-dark@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-backdrop-dark.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-backdrop-insensitive@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-backdrop-insensitive-dark@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-backdrop-insensitive-dark.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-backdrop-insensitive.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-backdrop.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-dark@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-dark.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-hover@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-hover-dark@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-hover-dark.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-hover.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-insensitive@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-insensitive-dark@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-insensitive-dark.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-insensitive.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-active@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-active-dark@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-active-dark.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-active.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-backdrop@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-backdrop-dark@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-backdrop-dark.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-backdrop-insensitive@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-backdrop-insensitive-dark@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-backdrop-insensitive-dark.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-backdrop-insensitive.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-backdrop.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-dark@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-dark.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-hover@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-hover-dark@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-hover-dark.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-hover.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-insensitive@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-insensitive-dark@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-insensitive-dark.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-insensitive.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-active@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-active-dark@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-active-dark.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-active.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-backdrop@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-backdrop-dark@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-backdrop-dark.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-backdrop-insensitive@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-backdrop-insensitive-dark@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-backdrop-insensitive-dark.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-backdrop-insensitive.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-backdrop.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-dark@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-dark.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-hover@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-hover-dark@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-hover-dark.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-hover.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-insensitive@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-insensitive-dark@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-insensitive-dark.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-insensitive.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below.png',
  'src/gtk-3.0/assets/text-select-end@2.png',
  'src/gtk-3.0/assets/text-select-end-active@2.png',
  'src/gtk-3.0/assets/text-select-end-active-dark@2.png',
  'src/gtk-3.0/assets/text-select-end-active-dark.png',
  'src/gtk-3.0/assets/text-select-end-active.png',
  'src/gtk-3.0/assets/text-select-end-dark@2.png',
  'src/gtk-3.0/assets/text-select-end-dark.png',
  'src/gtk-3.0/assets/text-select-end-hover@2.png',
  'src/gtk-3.0/assets/text-select-end-hover-dark@2.png',
  'src/gtk-3.0/assets/text-select-end-hover-dark.png',
  'src/gtk-3.0/assets/text-select-end-hover.png',
  'src/gtk-3.0/assets/text-select-end.png',
  'src/gtk-3.0/assets/text-select-start@2.png',
  'src/gtk-3.0/assets/text-select-start-active@2.png',
  'src/gtk-3.0/assets/text-select-start-active-dark@2.png',
  'src/gtk-3.0/assets/text-select-start-active-dark.png',
  'src/gtk-3.0/assets/text-select-start-active.png',
  'src/gtk-3.0/assets/text-select-start-dark@2.png',
  'src/gtk-3.0/assets/text-select-start-dark.png',
  'src/gtk-3.0/assets/text-select-start-hover@2.png',
  'src/gtk-3.0/assets/text-select-start-hover-dark@2.png',
  'src/gtk-3.0/assets/text-select-start-hover-dark.png',
  'src/gtk-3.0/assets/text-select-start-hover.png',
  'src/gtk-3.0/assets/text-select-start.png',
]

dark_gtk3_assets = [
  'src/gtk-3.0/assets/bullet-symbolic.svg',
  'src/gtk-3.0/assets/bullet-symbolic.symbolic.png',
  'src/gtk-3.0/assets/checkbox-active-selectionmode@2.png',
  'src/gtk-3.0/assets/checkbox-active-selectionmode.png',
  'src/gtk-3.0/assets/checkbox-backdrop-selectionmode@2.png',
  'src/gtk-3.0/assets/checkbox-backdrop-selectionmode.png',
  'src/gtk-3.0/assets/checkbox-checked-active-selectionmode@2.png',
  'src/gtk-3.0/assets/checkbox-checked-active-selectionmode.png',
  'src/gtk-3.0/assets/checkbox-checked-backdrop-selectionmode@2.png',
  'src/gtk-3.0/assets/checkbox-checked-backdrop-selectionmode.png',
  'src/gtk-3.0/assets/checkbox-checked-hover-selectionmode@2.png',
  'src/gtk-3.0/assets/checkbox-checked-hover-selectionmode.png',
  'src/gtk-3.0/assets/checkbox-checked-selectionmode@2.png',
  'src/gtk-3.0/assets/checkbox-checked-selectionmode.png',
  'src/gtk-3.0/assets/checkbox-hover-selectionmode@2.png',
  'src/gtk-3.0/assets/checkbox-hover-selectionmode.png',
  'src/gtk-3.0/assets/checkbox-selectionmode@2.png',
  'src/gtk-3.0/assets/checkbox-selectionmode.png',
  'src/gtk-3.0/assets/check-symbolic.svg',
  'src/gtk-3.0/assets/check-symbolic.symbolic.png',
  'src/gtk-3.0/assets/dash-symbolic.svg',
  'src/gtk-3.0/assets/dash-symbolic.symbolic.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-active-dark@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-active-dark.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-backdrop-dark@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-backdrop-dark.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-backdrop-insensitive-dark@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-backdrop-insensitive-dark.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-dark@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-dark.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-hover-dark@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-hover-dark.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-insensitive-dark@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-insensitive-dark.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-above-insensitive.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-active-dark@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-active-dark.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-backdrop-dark@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-backdrop-dark.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-backdrop-insensitive-dark@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-backdrop-insensitive-dark.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-dark@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-dark.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-hover-dark@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-hover-dark.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-insensitive-dark@2.png',
  'src/gtk-3.0/assets/slider-horz-scale-has-marks-below-insensitive-dark.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-active-dark@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-active-dark.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-backdrop-dark@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-backdrop-dark.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-backdrop-insensitive-dark@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-backdrop-insensitive-dark.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-dark@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-dark.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-hover-dark@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-hover-dark.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-insensitive-dark@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-above-insensitive-dark.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-active-dark@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-active-dark.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-backdrop-dark@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-backdrop-dark.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-backdrop-insensitive-dark@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-backdrop-insensitive-dark.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-dark@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-dark.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-hover-dark@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-hover-dark.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-insensitive-dark@2.png',
  'src/gtk-3.0/assets/slider-vert-scale-has-marks-below-insensitive-dark.png',
  'src/gtk-3.0/assets/text-select-end-active-dark@2.png',
  'src/gtk-3.0/assets/text-select-end-active-dark.png',
  'src/gtk-3.0/assets/text-select-end-dark@2.png',
  'src/gtk-3.0/assets/text-select-end-dark.png',
  'src/gtk-3.0/assets/text-select-end-hover-dark@2.png',
  'src/gtk-3.0/assets/text-select-end-hover-dark.png',
  'src/gtk-3.0/assets/text-select-start-active-dark@2.png',
  'src/gtk-3.0/assets/text-select-start-active-dark.png',
  'src/gtk-3.0/assets/text-select-start-dark@2.png',
  'src/gtk-3.0/assets/text-select-start-dark.png',
  'src/gtk-3.0/assets/text-select-start-hover-dark@2.png',
  'src/gtk-3.0/assets/text-select-start-hover-dark.png',
]


install_data(gnomeshell_assets, install_dir: shell_asset_dir)
install_data(gtk2_assets, install_dir: gtk2_asset_dir)
install_data(gtk3_assets, install_dir: gtk3_asset_dir)
install_data(dark_gtk2_assets, install_dir: dark_gtk2_asset_dir)
install_data(dark_gtk3_assets, install_dir: dark_gtk3_asset_dir)
