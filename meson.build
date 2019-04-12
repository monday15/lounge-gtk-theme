project('lounge-gtk-theme',
        version: '1.17',
        meson_version: '>= 0.45',
        license : ['GPL3+'],
        default_options: ['prefix=/usr'])

# Dependencies

sassc = find_program('sassc')
gnomeshell = find_program('gnome-shell', required: false)
# gtk3 is also a dependency, located below, becuase it is not required for fltapak build


##### Regular build

if get_option('flatpak') == false

# Installation directories

theme_dir = join_paths(get_option('datadir'), 'themes', 'Lounge')
shell_dir = join_paths(theme_dir, 'gnome-shell')
gtk2_dir = join_paths(theme_dir, 'gtk-2.0')
gtk3_dir = join_paths(theme_dir, 'gtk-3.0')
xfwm_dir = join_paths(theme_dir, 'xfwm4')

  # Dark theme
dark_theme_dir = join_paths(get_option('datadir'), 'themes', 'Lounge-night')
dark_gtk2_dir = join_paths(dark_theme_dir, 'gtk-2.0')
dark_gtk3_dir = join_paths(dark_theme_dir, 'gtk-3.0')
dark_xfwm_dir = join_paths(dark_theme_dir, 'xfwm4')


# Install index files

  # Copy is used for copying input to builddir;
  # copy.set doesn't change anything, just prevents meson warnings.
copy = configuration_data()
copy.set('something', 'something')

index_file = 'src/index.theme'
install_data(index_file, install_dir: theme_dir)

configure_file(input : index_file,
               output : 'index.theme',
               capture : true,
               command: ['sed', 's#Lounge#Lounge-night#g', '@INPUT@'],
               install_dir: dark_theme_dir)


# Check Gnome version

if gnomeshell.found()
  gnome_version_array = run_command([gnomeshell, '--version']).stdout().split('\n')[0].split(' ')[-1].strip().split('.')
    if gnome_version_array[1].to_int().is_even()
      gnome_version = '.'.join([ gnome_version_array[0], gnome_version_array[1] ])
    else
      gnome_version = '.'.join([ gnome_version_array[0], (gnome_version_array[1].to_int() + 1).to_string() ])
    endif

    message('Gnome ' + gnome_version)

else
  message('Gnome-shell not found, using styles for last gnome version availible')
  gnome_version = '3.32'

endif


# Check gtk3 version

gtk3_version_check = find_program('gtk-launch')
gtk3_version_array = run_command([gtk3_version_check, '--version']).stdout().split('\n')[0].split(' ')[-1].strip().split('.')
gtk3_version = '.'.join([ gtk3_version_array[0], gtk3_version_array[1] ])
message ('gtk version is ' + gtk3_version)


# Generate and install gnome-shell theme

shell_sources = [
  'shell-colors.scss',
  'shell-drawing.scss',
  'shell-extensions.scss'
]

  # Configure scss file
shell_conf = configuration_data()
shell_conf.set('gnome_version', gnome_version)

shell_scss = configure_file(input : 'src/gnome-shell/gnome-shell.scss',
                            output : 'gnome-shell.scss',
                            configuration : shell_conf)

  # Copy sources to builddir
foreach file : shell_sources
configure_file(input : join_paths('src/gnome-shell/' + file),
               output : file,
               configuration : copy)
endforeach

  # Select font
if get_option('shell-font') != ''

  configure_file(input :  join_paths('src/gnome-shell/shell-common.scss'),
                 output : 'shell-common.scss',
                 capture : true,
                 command: ['sed', 's#$font-family: Roboto#$font-family: ' + get_option('shell-font') + '#g', '@INPUT@'])

else 

  configure_file(input : join_paths('src/gnome-shell/shell-common.scss'),
               output : 'shell-common.scss',
               configuration : copy)

endif

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
  'src/gtk2/gtkrc',
  'src/gtk2/apps.rc',
  'src/gtk2/hacks.rc',
  'src/gtk2/xfce.rc',
]

dark_gtk2_data = [
  'src/gtk2-dark/gtkrc',
  'src/gtk2-dark/apps.rc',
  'src/gtk2-dark/hacks.rc',
  'src/gtk2-dark/xfce.rc',
]

  # Configure main.rc with enabled/disabled solid menu border
gtk2_mainrc_conf = [[ 'src/gtk2/main.rc',      '',     gtk2_dir],
                    [ 'src/gtk2-dark/main.rc', '.dark', dark_gtk2_dir]]

foreach mainrc : gtk2_mainrc_conf
  if get_option('gtk2-solid-menu')
    configure_file(input : mainrc[0],
                   output : 'main.rc' + mainrc[1],
                   capture : true,
                   command: ['sed', '-e', 's!GtkMenu::horizontal-padding  = 0!GtkMenu::horizontal-padding  = 1!g',
                                    '-e', 's!#widget_class!widget_class!g', '@INPUT@'],
                   install_dir: mainrc[2])
  else
    configure_file(input : mainrc[0],
                   output : 'main.rc' + mainrc[1],
                   configuration : copy,
                   install_dir: mainrc[2])

  endif
endforeach

  # Rename main.rc.dark file in dark theme
meson.add_install_script('sh', '-c', 'mv $MESON_INSTALL_DESTDIR_PREFIX/'+dark_gtk2_dir+'/main.rc.dark $MESON_INSTALL_DESTDIR_PREFIX/'+dark_gtk2_dir+'/main.rc')

install_data(gtk2_data, install_dir: gtk2_dir)
install_data(dark_gtk2_data, install_dir: dark_gtk2_dir)


# Generate and install gtk3 theme

gtk3_sources = [
  'gtk3-colors.scss',
  'gtk3-colors-public.scss',
  'gtk3-drawing.scss',
  'gtk3-common.scss',
  'gtk3-apps.scss',
  'gtk3-xfce.scss'
]

foreach file : gtk3_sources
  configure_file(input : join_paths('src/gtk3/' + file),
                 output : file,
                 configuration : copy)
endforeach

  # Generate css files for dark/light theme
gtk3_variants = [['light', ''],
                 ['dark',  '-dark']]

foreach variant : gtk3_variants
  gtk3_conf = configuration_data()
  gtk3_conf.set('gtk_variant', variant[0])
  gtk3_conf.set('gtk_version', gtk3_version)
  gtk3_conf.set('gnome_version', gnome_version)
  #gtk3_conf.set('nautilus_version', gnome_version)

    # Ubuntu 18.10 hack
    # Replace nautilus variable in scss files with gnome after Ubuntu 19.04 release
    check_nautilus = find_program('nautilus', required: false)
    if check_nautilus.found()
      nautilus_version_array = run_command([check_nautilus, '--version']).stdout().split('\n')[0].split(' ')[-1].strip().split('.')
      nautilus_version = '.'.join([ nautilus_version_array[0], nautilus_version_array[1] ])
      message ('nautilus version is ' + nautilus_version)

      gtk3_conf.set('nautilus_version', nautilus_version)
    else
      gtk3_conf.set('nautilus_version', gnome_version)
    endif
    # End of hack

  gtk3_scss = configure_file(input : 'src/gtk3/gtk3.scss',
                             output : 'gtk3' + variant[1] + '.scss',
                             configuration : gtk3_conf)

  custom_target('generate css for ' + variant[0] + ' theme',
                input: gtk3_scss,
                output: 'gtk' + variant[1] + '.css',
                command: [ sassc, '-M', '-t', 'compact', '@INPUT@', '@OUTPUT@' ],
                install: true,
                install_dir: gtk3_dir, 
                build_by_default: true)
endforeach

  # Create subfolders for Lounge-night theme, copy dark variant css file to Lounge-night theme
meson.add_install_script('sh', '-c', 'mkdir -p $MESON_INSTALL_DESTDIR_PREFIX/'+dark_gtk3_dir)
meson.add_install_script('sh', '-c', 'cp $MESON_INSTALL_DESTDIR_PREFIX/'+gtk3_dir+'/gtk-dark.css $MESON_INSTALL_DESTDIR_PREFIX/'+dark_gtk3_dir+'/gtk.css')


# Install xfwm theme

xfwm_variants = [['', xfwm_dir],
                 ['-dark', dark_xfwm_dir]]

foreach variant : xfwm_variants
  install_subdir('src/xfwm4' + variant[0],
                 install_dir: variant[1],
                 exclude_files: ['xfwm4-assets.txt', 'xfwm4-assets.svg', 'xfwm4-render-assets.sh'],
                 strip_directory: true)
endforeach


# Install assets

if gnome_version.version_compare('<=3.30')
  install_subdir('src/gnome-shell/assets', install_dir: shell_dir)
else
  install_subdir('src/gnome-shell/assets', install_dir: shell_dir,
                 exclude_files: ['close-window.svg', 'close-window-active.svg', 'close-window-hover.svg',
                                 'calendar-arrow-left.svg', 'calendar-arrow-right.svg'])
endif

install_subdir('src/gtk2/assets', install_dir: gtk2_dir)
install_subdir('src/gtk2-dark/assets', install_dir: dark_gtk2_dir)

install_subdir('src/gtk3/assets', install_dir: gtk3_dir)
install_subdir('src/gtk3/assets', install_dir: dark_gtk3_dir)

if get_option('icons')
  subdir('src/aux-icons')
endif

endif


##### Flatpak build

if get_option('flatpak')

if get_option('flatpak-ver') == 'day'
  theme_dir = join_paths(get_option('datadir'), 'themes', 'Lounge')
else
  theme_dir = join_paths(get_option('datadir'), 'themes', 'Lounge-night')
endif

gtk3_dir = join_paths(theme_dir, 'gtk-3.0')

gtk3_sources = [
  'gtk3-colors.scss',
  'gtk3-colors-public.scss',
  'gtk3-drawing.scss',
  'gtk3-common.scss',
  'gtk3-apps.scss',
  'gtk3-xfce.scss'
]

gtk3_version = '3.24'
gnome_version = '3.32'

copy = configuration_data()
copy.set('something', 'something')

foreach file : gtk3_sources
  configure_file(input : join_paths('src/gtk3/' + file),
                 output : file,
                 configuration : copy)
endforeach

if get_option('flatpak-ver') == 'day'
  gtk3_variants = [['light', ''],
                   ['dark',  '-dark']]
else
  gtk3_variants = [['dark', '']]
endif

foreach variant : gtk3_variants
  gtk3_conf = configuration_data()
  gtk3_conf.set('gtk_variant', variant[0])
  gtk3_conf.set('gtk_version', gtk3_version)
  gtk3_conf.set('gnome_version', gnome_version)
  gtk3_conf.set('nautilus_version', gnome_version)

  gtk3_scss = configure_file(input : 'src/gtk3/gtk3.scss',
                             output : 'gtk3' + variant[1] + '.scss',
                             configuration : gtk3_conf)

  custom_target('generate css for ' + variant[0] + ' theme',
                input: gtk3_scss,
                output: 'gtk' + variant[1] + '.css',
                command: [ sassc, '-M', '-t', 'compact', '@INPUT@', '@OUTPUT@' ],
                install: true,
                install_dir: gtk3_dir, 
                build_by_default: true)
endforeach

install_subdir('src/gtk3/assets', install_dir: gtk3_dir)

endif
