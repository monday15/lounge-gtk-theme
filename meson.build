project('lounge-gtk-theme',
        version: '1.19',
        meson_version: '>= 0.45',
        license : ['GPL3+'],
        default_options: ['prefix=/usr'])

# Dependencies

sassc = find_program('sassc')
gnomeshell = find_program('gnome-shell', required: false)
# gtk3 is also a dependency, located below, becuase it is not required for fltapak build

# Variable, used several times in install scripts
mid = '$MESON_INSTALL_DESTDIR_PREFIX/'


##### REGULAR BUILD

if get_option('flatpak') == false


  # CHECK GNOME VERSION

if get_option('gnome-version') != ''
  gnome_version = get_option('gnome-version')
else

  if gnomeshell.found()
    gnome_version_array = run_command([gnomeshell, '--version']).stdout().split('\n')[0].split(' ')[-1].strip().split('.')
    if gnome_version_array[1].to_int().is_even()
      gnome_version = '.'.join([ gnome_version_array[0], gnome_version_array[1] ])
    else
      gnome_version = '.'.join([ gnome_version_array[0], (gnome_version_array[1].to_int() + 1).to_string() ])
    endif

  else
    message('Gnome-shell not found, using styles for last gnome version availible')
    gnome_version = '3.32'
  endif
endif
message('Gnome ' + gnome_version)

  # CHECK GTK3 VERSION

if get_option('gtk3-version') != ''
  gtk_version = get_option('gtk-version')
else
  gtk3_version_check = find_program('gtk-launch')
  gtk3_version_array = run_command([gtk3_version_check, '--version']).stdout().split('\n')[0].split(' ')[-1].strip().split('.')
  gtk3_version = '.'.join([ gtk3_version_array[0], gtk3_version_array[1] ])
endif
message ('Gtk3 ' + gtk3_version)


  # INSTALLATION DIRECTORIES

themes_array = [
  ['Lounge',               ''             ],
  ['Lounge-night',         'dark_'        ],
  ['Lounge-compact',       'compact_'     ],
  ['Lounge-night-compact', 'compact_dark_']
]

dirs_array = [
  ['gtk-2.0',     'gtk2_dir' ],
  ['gtk-3.0',     'gtk3_dir' ],
  ['gnome-shell', 'shell_dir'],
  ['xfwm4',       'xfwm4_dir']
]

# Create variables for theme directories
foreach theme : themes_array
  set_variable(theme[1] + 'theme_dir', join_paths(get_option('datadir'), 'themes', theme[0]))

  foreach dir : dirs_array
    set_variable(theme[1] + dir[1], join_paths(get_option('datadir'), 'themes', theme[0], dir[0]))
  endforeach
endforeach

  # INDEX FILES

# Copy is used for copying input to builddir,
# copy.set doesn't change anything, but prevents meson warnings
copy = configuration_data()
copy.set('something', 'something')

# Create index files for themes, output files has to have different names,
# install_script will rename them later
foreach theme : themes_array
  conf_index = configuration_data()
  conf_index.set('theme_name', theme[0])

  configure_file(input : 'src/index.theme.in',
                 output : 'index.theme.' + theme[0],
                 configuration: conf_index,
                 install_dir: get_variable(theme[1] + 'theme_dir'))

  meson.add_install_script('sh', '-c', 'mv ' + mid + get_variable(theme[1] + 'theme_dir') + '/index.theme.' + theme[0] +
                                         ' ' + mid + get_variable(theme[1] + 'theme_dir') + '/index.theme')
endforeach


  # GNOME-SHELL THEME

shell_noconf_sources = [
  'shell-colors.scss',
  'shell-drawing.scss',
  'shell-extensions.scss'
]

# Copy sources that doesnt require configuration to builddir
foreach file : shell_noconf_sources
  configure_file(input : 'src/gnome-shell/' + file,
                 output : file,
                 configuration : copy)
endforeach

# Set font
configure_file(input :  join_paths('src/gnome-shell/shell-common.scss'),
               output : 'shell-common.scss',
               capture : true,
               command: ['sed', 's#Roboto#' + get_option('shell-font') + '#g', '@INPUT@'])

# Configure main scss file
shell_conf = configuration_data()
shell_conf.set('gnome_version', gnome_version)

shell_scss = configure_file(input : 'src/gnome-shell/gnome-shell.scss',
                            output : 'gnome-shell.scss',
                            configuration : shell_conf)

# Generate and install theme css file
custom_target('Generate shell theme',
              input: shell_scss,
              output: 'gnome-shell.css',
              command: [ sassc, '-a', '@INPUT@', '@OUTPUT@'],
              install: true,
              install_dir: shell_dir)

# Install assets
if gnome_version.version_compare('<=3.30')
  install_subdir('src/gnome-shell/assets',
                 install_dir: shell_dir)
else
  install_subdir('src/gnome-shell/assets',
                 install_dir: shell_dir,
                 exclude_files: ['close-window.svg', 'close-window-active.svg', 'close-window-hover.svg',
                                 'calendar-arrow-left.svg', 'calendar-arrow-right.svg'])
endif


  # GTK3 THEME

gtk3_noconf_sources = [
  'gtk3-colors.scss',
  'gtk3-colors-public.scss',
  'gtk3-variables.scss',
  'gtk3-drawing.scss',
  'gtk3-common.scss',
  'gtk3-apps.scss',
  'gtk3-xfce.scss'
]

# Copy sources that doesnt require configuration to builddir
foreach file : gtk3_noconf_sources
  configure_file(input : join_paths('src/gtk3/' + file),
                 output : file,
                 configuration : copy)
endforeach

gtk3_array = [
  ['',              'light', 'regular'],
  ['dark_',         'dark' , 'regular'],
  ['compact_',      'light', 'compact'],
  ['compact_dark_', 'dark' , 'compact']
]

foreach theme : gtk3_array
  gtk3_conf = configuration_data()
  gtk3_conf.set('gtk_variant', theme[1])
  gtk3_conf.set('gtk_size', theme[2])
  gtk3_conf.set('gtk_version', gtk3_version)
  gtk3_conf.set('gnome_version', gnome_version)

  # Configure main scss file
  gtk3_scss = configure_file(input : 'src/gtk3/gtk3.scss',
                             output : 'gtk3' + theme[0] + '.scss',
                             configuration : gtk3_conf)

  # Generate and install css files
  custom_target('Generate gtk3 theme ' + theme[0],
                input: gtk3_scss,
                output: 'gtk' + theme[0] + '.css',
                command: [ sassc, '-M', '-t', 'compact', '@INPUT@', '@OUTPUT@' ],
                install: true,
                install_dir: get_variable(theme[0] + 'gtk3_dir'))

  # Rename generated files (output files has to have different names at configuration),
  # ignore regular light theme, mv fails if source and destination are the same file
  if theme[0] != ''
    meson.add_install_script('sh', '-c', 'mv ' + mid + get_variable(theme[0] + 'gtk3_dir') + '/gtk' + theme[0] + '.css ' +
                                                 mid + get_variable(theme[0] + 'gtk3_dir') + '/gtk.css')
  endif
endforeach

# Copy dark theme css files to light themes
meson.add_install_script('sh', '-c', 'cp ' + mid + compact_dark_gtk3_dir + '/gtk.css ' +
                                             mid + compact_gtk3_dir + '/gtk-dark.css')
meson.add_install_script('sh', '-c', 'cp ' + mid + dark_gtk3_dir +'/gtk.css ' +
                                             mid + gtk3_dir + '/gtk-dark.css')


  # GTK2 THEME

gtk2_sources = [
  'gtkrc',
  'main.rc',
  'apps.rc',
  'hacks.rc',
  'xfce.rc'
]

gtk2_array = [
  ['',              '$regular ', '$light '],                 
  ['dark_',         '$regular ', '$dark ' ],
  ['compact_',      '$compact ', '$light '],
  ['compact_dark_', '$compact ', '$dark ' ]]

# Solid menu option for xfce/sway and other environments without compositor,
# uses png asset to draw menu's border 
if get_option('gtk2-solid-menu')
  gtk2_menu_border = 's/$solid_menu //g'
else
  gtk2_menu_border = 's/$normal_menu //g'
endif

# Create gtk2 themes from templates
foreach theme : gtk2_array
  foreach file : gtk2_sources

    # Add suffix for assets urls used in compact themes
    if theme[1] == '$compact '
      set_assets_size = 's/\-$size/\-compact/g'
    else
      set_assets_size = 's/\-$size//g'
    endif

    # Add suffix for assets urls used in dark themes
    if theme[2] == '$dark '
      set_color_variant = 's/.png\"/\-dark.png\"/g'
    else
      set_color_variant = 's///'
    endif

    # Create data files: templates has lines, that starts with $ (whole line is a variable),
    # sed enables needed variables - removes variable, so the line became a regular one,
    # lines with unused variables are removed on the fourth step
    configure_file(input : 'src/gtk2/' + file + '.in',
                   output : file + theme[0],
                   capture : true,
                   command: ['sed', '-e', 's/' + theme[1] + '//g',
                                    '-e', 's/' + theme[2] + '//g',
                                    '-e', gtk2_menu_border,
                                    '-e', '/^\$/ d',
                                    '-e', set_assets_size,
                                    '-e', set_color_variant,
                                    '@INPUT@'],
                   install_dir: get_variable(theme[0] + 'gtk2_dir'))

    # Rename generated files (output files has to have different names at configuration),
    # ignore regular light theme, mv fails if source and destination are the same file
    if theme[0] != ''
      meson.add_install_script('sh', '-c', 'mv ' + mid + get_variable(theme[0] + 'gtk2_dir') + '/' + file + theme[0] +
                                             ' ' + mid + get_variable(theme[0] + 'gtk2_dir') + '/' + file)
    endif
  endforeach
endforeach

  # XFWM THEME 

# Use array from gtk2 theme, variables are the same
foreach theme : gtk2_array
  # Generate and install themerc files
  configure_file(input : 'src/xfwm4/themerc.in',
                 output : 'themerc' + theme[0],
                 capture : true,
                 command: ['sed', '-e', 's/' + theme[1] + '//g',
                                  '-e', 's/' + theme[2] + '//g',
                                  '-e', '/^\$/ d',
                                  '@INPUT@'],
                 install_dir: get_variable(theme[0] + 'xfwm4_dir'))

  # Rename generated files (output files has to have different names at configuration),
  # ignore regular light theme, mv fails if source and destination are the same file
  if theme[0] != ''
    meson.add_install_script('sh', '-c', 'mv ' + mid + get_variable(theme[0] + 'xfwm4_dir') + '/' + 'themerc' + theme[0] +
                                           ' ' + mid + get_variable(theme[0] + 'xfwm4_dir') + '/' + 'themerc')
  endif
endforeach

  # ASSETS

assets_themes = [
  'gtk2',
  'gtk3',
  'xfwm4'
]

# Specifies excluded assets for each theme
#  theme          | gtk3/gtk2/xfwm | gtk3    | gtk2/xfwm
assets_array = [
  [''             , '_compact',     '_none',  '_dark' ],
  ['dark_'        , '_compact',     '_light', '_light'],
  ['compact_'     , '_regular',     '_none',  '_dark' ],
  ['compact_dark_', '_regular',     '_light', '_light']
]

foreach theme : assets_themes
  # Helpers for excluding assets from different size/color variants
  set_variable(theme + '_assets_none', '')
  set_variable(theme + '_assets_light',
               run_command('sh', '-c', 'ls ' + join_paths(meson.source_root(), 'src', theme, 'assets') +
                                           ' | grep dark | sed s/-dark//').stdout())
  set_variable(theme + '_assets_dark',
               run_command('sh', '-c', 'ls ' + join_paths(meson.source_root(), 'src', theme, 'assets') +
                                           ' | grep dark').stdout())
  set_variable(theme + '_assets_regular',
               run_command('sh', '-c', 'ls ' + join_paths(meson.source_root(), 'src', theme, 'assets') +
                                           ' | grep compact | sed s/-compact//').stdout())
  set_variable(theme + '_assets_compact',
               run_command('sh', '-c', 'ls ' + join_paths(meson.source_root(), 'src', theme, 'assets') +
                                           ' | grep compact').stdout())

  foreach assets : assets_array
    # Exclude different types of assets from gtk3 theme
    # (light gtk3 theme needs dark assets for dark variant)
    if theme == 'gtk3'
      exclude_color_variants = assets[2]
    else 
      exclude_color_variants = assets[3]
    endif

    # Assets for xfwm theme should be in main 'xfwm4' folder (other themes has 'assets' subfolder)
    if theme == 'xfwm4'
      assets_install_dir = join_paths(get_variable(assets[0] + theme +'_dir'))
    else
      assets_install_dir = join_paths(get_variable(assets[0] + theme +'_dir'), 'assets')
    endif

    install_subdir('src/' + theme +'/assets',
                    install_dir: assets_install_dir,
                    exclude_files : [get_variable(theme + '_assets' + assets[1]).split('\n'),
                                     get_variable(theme + '_assets' + exclude_color_variants).split('\n')],
                                     strip_directory: true)

    if theme == 'xfwm4'
      # Remove color/size suffixes from xfwm assets
      meson.add_install_script('sh', '-c', 'for i in $(ls ' + mid + get_variable(assets[0] + 'xfwm4_dir') + ' | grep "compact\|dark"); do mv ' + mid + get_variable(assets[0] + 'xfwm4_dir') + '/$i ' + mid + get_variable(assets[0] + 'xfwm4_dir') + '/$(echo $i | sed s/\-compact// | sed s/\-dark//); done')
    endif

  endforeach
endforeach


  # AUXILIARY ICON THEME

if get_option('icons')
  subdir('src/aux-icons')
endif

# Regular build end
endif

##### Flatpak build

if get_option('flatpak')

if get_option('flatpak-variant') == 'light'
  if get_option('flatpak-size') == 'regular'
    theme_dir = join_paths(get_option('datadir'), 'themes', 'Lounge')
    gtk3_variants = [['light', '',      'regular'],
                     ['dark',  '-dark', 'regular']]
    exclude_assets = ['_none', '_compact']

  else
    theme_dir = join_paths(get_option('datadir'), 'themes', 'Lounge-compact')
    gtk3_variants = [['light', '',      'compact'],
                     ['dark',  '-dark', 'compact']]
    exclude_assets = ['_none', '_regular']

  endif
else
  if get_option('flatpak-size') == 'regular'
    theme_dir = join_paths(get_option('datadir'), 'themes', 'Lounge-night')
    gtk3_variants = [['dark', '', 'regular']]
    exclude_assets = ['_light', '_compact']

  else
    theme_dir = join_paths(get_option('datadir'), 'themes', 'Lounge-night-compact')
    gtk3_variants = [['dark', '', 'compact']]
    exclude_assets = ['_light', '_regular']

  endif
endif

gtk3_dir = join_paths(theme_dir, 'gtk-3.0')

gtk3_noconf_sources = [
  'gtk3-colors.scss',
  'gtk3-colors-public.scss',
  'gtk3-variables.scss',
  'gtk3-drawing.scss',
  'gtk3-common.scss',
  'gtk3-apps.scss',
  'gtk3-xfce.scss'
]

gtk3_version = '3.24'
gnome_version = '3.32'

copy = configuration_data()
copy.set('something', 'something')

foreach file : gtk3_noconf_sources
  configure_file(input : join_paths('src/gtk3/' + file),
                 output : file,
                 configuration : copy)
endforeach


foreach variant : gtk3_variants
  gtk3_conf = configuration_data()
  gtk3_conf.set('gtk_variant', variant[0])
  gtk3_conf.set('gtk_size', variant[2])
  gtk3_conf.set('gtk_version', gtk3_version)
  gtk3_conf.set('gnome_version', gnome_version)

  gtk3_scss = configure_file(input : 'src/gtk3/gtk3.scss',
                             output : 'gtk3' + variant[1] + '.scss',
                             configuration : gtk3_conf)

  custom_target('generate css for ' + variant[0] + ' theme',
                input: gtk3_scss,
                output: 'gtk' + variant[1] + '.css',
                command: [ sassc, '-M', '-t', 'compact', '@INPUT@', '@OUTPUT@' ],
                install: true,
                install_dir: gtk3_dir)
endforeach

theme = 'gtk3'

set_variable(theme + '_assets_none', '')
set_variable(theme + '_assets_light',
             run_command('sh', '-c', 'ls ' + join_paths(meson.source_root(), 'src', theme, 'assets') +
                                         ' | grep dark | sed s/-dark//').stdout())
set_variable(theme + '_assets_dark',
             run_command('sh', '-c', 'ls ' + join_paths(meson.source_root(), 'src', theme, 'assets') +
                                         ' | grep dark').stdout())
set_variable(theme + '_assets_regular',
             run_command('sh', '-c', 'ls ' + join_paths(meson.source_root(), 'src', theme, 'assets') +
                                         ' | grep compact | sed s/-compact//').stdout())
set_variable(theme + '_assets_compact',
             run_command('sh', '-c', 'ls ' + join_paths(meson.source_root(), 'src', theme, 'assets') +
                                         ' | grep compact').stdout())

install_subdir('src/' + theme +'/assets',
                install_dir: gtk3_dir,
                exclude_files : [get_variable(theme + '_assets' + exclude_assets[0]).split('\n'),
                                 get_variable(theme + '_assets' + exclude_assets[1]).split('\n')])

endif
