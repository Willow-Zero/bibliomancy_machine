# Maintainer: Willow-Zero (zero@32bit.cafe)
pkgname=bibliomancy-machine
pkgver=1.0.0
pkgrel=1
pkgdesc="Random text selection tool for electronic bibliomancy - supports TXT, MD, and PDF files"
arch=('any')
url="https://github.com/yourusername/bibliomancy"
license=('GPL-3.0-or-later OR LicenseRef-WTFPL')
depends=('python' 'python-pypdf')
makedepends=()
optdepends=('kitty: for icat image preview support')
source=("bibliomancy.py" "LICENSE")
sha256sums=('80b29d5f347538b7269dd052f40b68363da855a4716191c3959ca16f4cee0aec'
            '8437135538bd712a059f12f255b8b4bc7afca4f3967c240b348ca810c814facb')
package() {
    install -Dm755 "${srcdir}/bibliomancy.py" "${pkgdir}/usr/bin/bibliomancy-machine"
    install -Dm644 LICENSE -t"${pkgdir}/usr/share/licenses/${pkgname}/"
}

post_install() {
    echo ":: Bibliomancy installed successfully!"
    echo ":: Usage: bibliomancy-machine -d /path/to/library -k (for Kitty icat support)"
    echo ":: Dependencies: python-pypdf is required for PDF support"
}
