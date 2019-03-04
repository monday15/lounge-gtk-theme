project('lounge-gtk-theme',
        version: '1.14',
        meson_version: '>= 0.45',
        license : ['GPL3+'],
        default_options: ['prefix=/usr'])

# Dependencies

sassc = find_program('sassc')
gnomeshell = find_program('gnome-shell', required: false)




##### Flatpak build

#if get_option('flatpak')

#if get_option('flatpak-ver') == 'day322'
#theme_dir = join_paths(get_option('datadir'), 'themes', 'Lounge')
#endif

#if get_option('flatpak-ver') == 'night322'
#theme_dir = join_paths(get_option('datadir'), 'themes', 'Lounge-night')
#endif

#gtk3_dir = join_paths(theme_dir, 'gtk-3.0')

#gtk3_sources = [
#  '_colors-public.scss',
#  '_colors.scss',
#  '_common.scss',
#  '_common-3-22.scss',
#  '_common-3-24.scss',
#  '_xfce.scss',
#  '_apps.scss',
#  '_apps-3-28.scss',
#  '_apps-3-30.scss',
#  '_drawing.scss',
#  '_apps-nautilus-3-28.scss',
#  '_apps-nautilus-3-30.scss',
#]

#gtk3_version = '3-22'
#gnome_version = '3-30'

#gtk3_conf = configuration_data()
#gtk3_conf.set('common_var', 'common-' + gtk3_version)
#gtk3_conf.set('apps_var', 'apps-' + gnome_version)
#gtk3_conf.set('apps_nautilus_var', 'apps-nautilus-' + gnome_version)


#gtk3_scss = configure_file(input : 'src/gtk3/gtk.scss',
#                           output : 'gtk-' + gtk3_version + '.scss',
#                           configuration : gtk3_conf)

#gtk3_scss_dark = configure_file(input : 'src/gtk3/gtk-dark.scss',
#                                output : 'gtk-dark-' + gtk3_version + '.scss',
#                                configuration : gtk3_conf)

#foreach file : gtk3_sources
#configure_file(input : join_paths('src/gtk3/' + file),
#               capture : true,
#               output : file,
#               command: ['sed', 's#../gtk3-assets#gtk3-assets#g', '@INPUT@'])
#endforeach


#gtk322_scss_light = join_paths(meson.build_root(), 'gtk-3-22.scss')
#gtk322_scss_dark  = join_paths(meson.build_root(), 'gtk-dark-3-22.scss')

#if get_option('flatpak-ver') == 'day322'
#  custom_target('gtk322-light',
#                input: gtk322_scss_light,
#                output: 'gtk.css',
#                command: [ sassc, '-M', '-t', 'compact', '@INPUT@', '@OUTPUT@', ],
#                install: true,
#                install_dir: gtk3_dir, 
#                build_by_default: true)


#  custom_target('gtk322-dark',
#                input: gtk322_scss_dark,
#                output: 'gtk-dark.css',
#                command: [ sassc, '-M', '-t', 'compact', '@INPUT@', '@OUTPUT@', ],
#                install: true,
#                install_dir: gtk3_dir,
#                build_by_default: true)
#endif

#if get_option('flatpak-ver') == 'night322'
#  custom_target('gtk322-dark',
#                input: gtk322_scss_dark,
#                output: 'gtk.css',
#                command: [ sassc, '-M', '-t', 'compact', '@INPUT@', '@OUTPUT@', ],
#                install: true,
#                install_dir: gtk3_dir,
#                build_by_default: true)
#endif

#install_subdir('src/gtk3/gtk3-assets', install_dir: gtk3_dir)


#else




##### Regular build

# Installation directories

theme_dir = join_paths(get_option('datadir'), 'themes', 'Lounge')
shell_dir = join_paths(theme_dir, 'gnome-shell')
gtk2_dir = join_paths(theme_dir, 'gtk-2.0')
gtk322_dir = join_paths(theme_dir, 'gtk-3.22')
gtk324_dir = join_paths(theme_dir, 'gtk-3.24')
xfwm_dir = join_paths(theme_dir, 'xfwm4')

  # Dark theme

dark_theme_dir = join_paths(get_option('datadir'), 'themes', 'Lounge-night')
dark_gtk2_dir = join_paths(dark_theme_dir, 'gtk-2.0')
dark_gtk322_dir = join_paths(dark_theme_dir, 'gtk-3.22')
dark_gtk324_dir = join_paths(dark_theme_dir, 'gtk-3.24')
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


# Generate and install gnome-shell theme

shell_sources = [
  'shell-colors.scss',
  'shell-drawing.scss',
#  'shell-common-shell.scss',
  'shell-extensions.scss'
]


  # Check Gnome version

if gnomeshell.found()
  gnome_ver_array = run_command([gnomeshell, '--version']).stdout().split('\n')[0].split(' ')[-1].strip().split('.')

    if gnome_ver_array[1].to_int().is_even()
      gnome_ver = '.'.join([ gnome_ver_array[0], gnome_ver_array[1] ])
    else
      gnome_ver = '.'.join([ gnome_ver_array[0], (gnome_ver_array[1].to_int() + 1).to_string() ])
    endif

    message('Gnome ' + gnome_ver)

else
  message('Gnome-shell not found, using styles for last gnome version availible')
  gnome_ver = '3.32'

endif

  # Configure scss file for building right version of shell theme

shell_conf = configuration_data()
shell_conf.set('gnome_version', gnome_ver)

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
  'src/gtk2/main.rc',
  'src/gtk2/apps.rc',
  'src/gtk2/hacks.rc',
  'src/gtk2/xfce.rc',
]

dark_gtk2_data = [
  'src/gtk2-dark/gtkrc',
  'src/gtk2-dark/main.rc',
  'src/gtk2-dark/apps.rc',
  'src/gtk2-dark/hacks.rc',
  'src/gtk2-dark/xfce.rc',
]

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

gtk3_version = [
  '3.22',
  '3.24'
]


foreach ver : gtk3_version

  if ver == '3.22'
    gnome_version = '3.28'
  endif
  if ver == '3.24'
    gnome_version = gnome_ver
  endif

gtk3_conf = configuration_data()
gtk3_conf.set('gtk_version', ver)
gtk3_conf.set('gnome_version', gnome_version)

  # Ubuntu 18.10 hack
  # Replace nautilus variable in scss files with gnome after Ubuntu 19.04 release

  check_gtk3 = find_program('gtk-launch', required: false)
  check_nautilus = find_program('nautilus', required: false)
  if (check_gtk3.found() and check_nautilus.found())
    check_gtk3_res = run_command([check_gtk3, '--version'])
    check_gtk3_ver = check_gtk3_res.stdout().split('\n')[0].split(' ')[-1].strip()
    check_nautilus_res = run_command([check_nautilus, '--version'])
    check_nautilus_ver = check_nautilus_res.stdout().split('\n')[0].split(' ')[-1].strip()

    if (check_gtk3_ver.version_compare('>=3.24') and check_nautilus_ver.version_compare('<3.30'))
      message('Using Nautilus 3.28 css for gtk 3.24')
      gtk3_conf.set('nautilus_version', '3.28')
    else
      gtk3_conf.set('nautilus_version', gnome_version)
    endif
  else
    gtk3_conf.set('nautilus_version', gnome_version)
  endif

  # End of hack


gtk3_scss = configure_file(input : 'src/gtk3/gtk3.scss',
                           output : 'gtk3-' + ver + '.scss',
                           configuration : gtk3_conf)

gtk3_scss_dark = configure_file(input : 'src/gtk3/gtk3-dark.scss',
                                output : 'gtk3-dark-' + ver + '.scss',
                                configuration : gtk3_conf)

endforeach

foreach file : gtk3_sources
configure_file(input : join_paths('src/gtk3/' + file),
               output : file,
               configuration : copy)
endforeach

gtk322_scss_light = join_paths(meson.build_root(), 'gtk3-3.22.scss')
gtk322_scss_dark  = join_paths(meson.build_root(), 'gtk3-dark-3.22.scss')

gtk324_scss_light = join_paths(meson.build_root(), 'gtk3-3.24.scss')
gtk324_scss_dark  = join_paths(meson.build_root(), 'gtk3-dark-3.24.scss')

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


# Install xfwm theme

install_subdir('src/xfwm4',
               install_dir: xfwm_dir,
               exclude_files: ['xfwm4-assets.txt', 'xfwm4-assets.svg', 'xfwm4-render-assets.sh'],
               strip_directory: true)

install_subdir('src/xfwm4-dark',
               install_dir: dark_xfwm_dir,
               exclude_files: ['xfwm4-assets.txt', 'xfwm4-assets.svg', 'xfwm4-render-assets.sh'],
               strip_directory: true)


# Install assets

install_subdir('src/gnome-shell/assets', install_dir: shell_dir)
install_subdir('src/gtk2/assets', install_dir: gtk2_dir)
install_subdir('src/gtk3/gtk3-assets', install_dir: theme_dir)
install_subdir('src/gtk2-dark/assets', install_dir: dark_gtk2_dir)
install_subdir('src/gtk3/gtk3-assets', install_dir: dark_theme_dir)

if get_option('icons')
  subdir('src/aux-icons')
endif

#endif
