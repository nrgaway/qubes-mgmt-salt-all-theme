%{!?version: %define version %(make get-version)}
%{!?rel: %define rel %(make get-release)}
%{!?package_name: %define package_name %(make get-package_name)}
%{!?package_summary: %define package_summary %(make get-summary)}
%{!?package_description: %define package_description %(make get-description)}

%{!?formula_name: %define formula_name %(make get-formula_name)}
%{!?state_name: %define state_name %(make get-state_name)}
%{!?saltenv: %define saltenv %(make get-saltenv)}
%{!?pillar_dir: %define pillar_dir %(make get-pillar_dir)}
%{!?formula_dir: %define formula_dir %(make get-formula_dir)}

Name:      %{package_name}
Version:   %{version}
Release:   %{rel}%{?dist}
Summary:   %{package_summary}
License:   GPL 2.0
URL:	   http://www.qubes-os.org/

Group:     System administration tools
BuildArch: noarch
Requires:  qubes-mgmt-salt

%define _builddir %(pwd)

%description
%{package_description}

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
qubesctl topd.enable %{state_name} saltenv=%{saltenv} -l quiet --out quiet > /dev/null || true
qubesctl topd.enable %{state_name}.fonts_ubuntu saltenv=all -l quiet --out quiet > /dev/null || true
qubesctl topd.enable %{state_name}.fonts_source_code_pro saltenv=all -l quiet --out quiet > /dev/null || true

%files
%defattr(-,root,root)
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
