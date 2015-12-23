%{!?version: %define version %(cat version)}

Name:      qubes-mgmt-salt-all-theme
Version:   %{version}
Release:   1%{?dist}
Summary:   Fine tunes graphics rendering to render fonts more like Ubuntu.
License:   GPL 2.0
URL:	   http://www.qubes-os.org/

Group:     System administration tools
BuildArch: noarch
Requires:  qubes-mgmt-salt
Requires:  ttmkfdir 
Requires:  gnome-tweak-tool
Requires:  dconf-editor
Requires:  xdg-user-dirs
Requires:  gnome-themes-standard
Requires:  xsettingsd

%define _builddir %(pwd)

%description
Fine tunes graphics rendering to render fonts more like Ubuntu.
Installs Source-Code-Pro and Ubuntu fonts.

%prep
# we operate on the current directory, so no need to unpack anything
# symlink is to generate useful debuginfo packages
rm -f %{name}-%{version}
ln -sf . %{name}-%{version}
%setup -T -D

%build

%install
make install DESTDIR=%{buildroot} LIBDIR=%{_libdir} BINDIR=%{_bindir} SBINDIR=%{_sbindir} SYSCONFDIR=%{_sysconfdir}

%post
# Update Salt Configuration
qubesctl state.sls config -l quiet --out quiet > /dev/null || true
qubesctl saltutil.clear_cache -l quiet --out quiet > /dev/null || true
qubesctl saltutil.sync_all refresh=true -l quiet --out quiet > /dev/null || true

# Enable States
qubesctl top.enable theme saltenv=all -l quiet --out quiet > /dev/null || true
qubesctl top.enable theme.fonts_ubuntu saltenv=all -l quiet --out quiet > /dev/null || true
qubesctl top.enable theme.fonts_source_code_pro saltenv=all -l quiet --out quiet > /dev/null || true

%files
%defattr(-,root,root)
%doc LICENSE README.rst
%attr(750, root, root) %dir /srv/formulas/all/theme-formula

/srv/formulas/all/theme-formula/LICENSE
/srv/formulas/all/theme-formula/README.rst
/srv/formulas/all/theme-formula/theme/files/25xdg-qubes-settings
/srv/formulas/all/theme-formula/theme/files/fedora-font-fix.conf
/srv/formulas/all/theme-formula/theme/files/fonts/source-code-pro/OFL.txt
/srv/formulas/all/theme-formula/theme/files/fonts/source-code-pro/SourceCodePro-Black.ttf
/srv/formulas/all/theme-formula/theme/files/fonts/source-code-pro/SourceCodePro-Bold.ttf
/srv/formulas/all/theme-formula/theme/files/fonts/source-code-pro/SourceCodePro-ExtraLight.ttf
/srv/formulas/all/theme-formula/theme/files/fonts/source-code-pro/SourceCodePro-Light.ttf
/srv/formulas/all/theme-formula/theme/files/fonts/source-code-pro/SourceCodePro-Medium.ttf
/srv/formulas/all/theme-formula/theme/files/fonts/source-code-pro/SourceCodePro-Regular.ttf
/srv/formulas/all/theme-formula/theme/files/fonts/source-code-pro/SourceCodePro-Semibold.ttf
/srv/formulas/all/theme-formula/theme/files/fonts/ubuntu-font-family-0.80/CONTRIBUTING.txt
/srv/formulas/all/theme-formula/theme/files/fonts/ubuntu-font-family-0.80/copyright.txt
/srv/formulas/all/theme-formula/theme/files/fonts/ubuntu-font-family-0.80/FONTLOG.txt
/srv/formulas/all/theme-formula/theme/files/fonts/ubuntu-font-family-0.80/LICENCE-FAQ.txt
/srv/formulas/all/theme-formula/theme/files/fonts/ubuntu-font-family-0.80/LICENCE.txt
/srv/formulas/all/theme-formula/theme/files/fonts/ubuntu-font-family-0.80/README.txt
/srv/formulas/all/theme-formula/theme/files/fonts/ubuntu-font-family-0.80/TRADEMARKS.txt
/srv/formulas/all/theme-formula/theme/files/fonts/ubuntu-font-family-0.80/Ubuntu-BI.ttf
/srv/formulas/all/theme-formula/theme/files/fonts/ubuntu-font-family-0.80/Ubuntu-B.ttf
/srv/formulas/all/theme-formula/theme/files/fonts/ubuntu-font-family-0.80/Ubuntu-C.ttf
/srv/formulas/all/theme-formula/theme/files/fonts/ubuntu-font-family-0.80/Ubuntu-LI.ttf
/srv/formulas/all/theme-formula/theme/files/fonts/ubuntu-font-family-0.80/Ubuntu-L.ttf
/srv/formulas/all/theme-formula/theme/files/fonts/ubuntu-font-family-0.80/Ubuntu-MI.ttf
/srv/formulas/all/theme-formula/theme/files/fonts/ubuntu-font-family-0.80/UbuntuMono-BI.ttf
/srv/formulas/all/theme-formula/theme/files/fonts/ubuntu-font-family-0.80/UbuntuMono-B.ttf
/srv/formulas/all/theme-formula/theme/files/fonts/ubuntu-font-family-0.80/UbuntuMono-RI.ttf
/srv/formulas/all/theme-formula/theme/files/fonts/ubuntu-font-family-0.80/UbuntuMono-R.ttf
/srv/formulas/all/theme-formula/theme/files/fonts/ubuntu-font-family-0.80/Ubuntu-M.ttf
/srv/formulas/all/theme-formula/theme/files/fonts/ubuntu-font-family-0.80/Ubuntu-RI.ttf
/srv/formulas/all/theme-formula/theme/files/fonts/ubuntu-font-family-0.80/Ubuntu-R.ttf
/srv/formulas/all/theme-formula/theme/files/fonts.conf
/srv/formulas/all/theme-formula/theme/files/Xresources
/srv/formulas/all/theme-formula/theme/files/xsettingsd
/srv/formulas/all/theme-formula/theme/fonts_source_code_pro.sls
/srv/formulas/all/theme-formula/theme/fonts_source_code_pro.top
/srv/formulas/all/theme-formula/theme/fonts_ubuntu.sls
/srv/formulas/all/theme-formula/theme/fonts_ubuntu.top
/srv/formulas/all/theme-formula/theme/init.sls
/srv/formulas/all/theme-formula/theme/init.top
/srv/formulas/all/theme-formula/theme/map.sls

%changelog
