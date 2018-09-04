project('Lounge',
        version: '3.28.0',
        meson_version: '>= 0.40',
        license : ['GPL3+'],
        default_options: ['prefix=/usr'])

theme_dir = join_paths(get_option('datadir'), 'themes', meson.project_name())

index_file = [ 'index.theme' ]

install_data(index_file, install_dir: theme_dir)

sassc = find_program('sassc')

subdir('gnome-shell')
subdir('gtk-2.0')
subdir('gtk-3.0')
