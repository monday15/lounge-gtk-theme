icons_dir = join_paths(get_option('datadir'), 'icons', 'Lounge-aux')

MIT = get_option('icon-theme')

icons_conf = configuration_data()

if MIT == ''
  icons_conf.set('main_icon_theme', 'Adwaita')
else
  icons_conf.set('main_icon_theme', MIT)
endif

configure_file(input : 'index.theme',
               output : 'index.theme',
               configuration : icons_conf,
               install_dir: icons_dir)

install_subdir('16x16', install_dir: icons_dir )
install_subdir('24x24', install_dir: icons_dir )
install_subdir('32x32', install_dir: icons_dir )
install_subdir('48x48', install_dir: icons_dir )
install_subdir('64x64', install_dir: icons_dir )
install_subdir('96x96', install_dir: icons_dir )
install_subdir('scalable', install_dir: icons_dir )

meson.add_install_script('post_install.py')
