icons_dir = join_paths(get_option('datadir'), 'icons', 'Lounge-aux')

configure_file(input : 'index.theme',
               output : 'index.theme',
               capture : true,
               command: ['sed', 's#Adwaita#' + get_option('icon_theme') + '#g', '@INPUT@'],
               install_dir: icons_dir)

install_subdir('16x16', install_dir: icons_dir )
install_subdir('24x24', install_dir: icons_dir )
install_subdir('32x32', install_dir: icons_dir )
install_subdir('48x48', install_dir: icons_dir )
install_subdir('64x64', install_dir: icons_dir )
install_subdir('96x96', install_dir: icons_dir )
install_subdir('scalable', install_dir: icons_dir )

meson.add_install_script('post_install.py')
