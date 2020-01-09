Name:		bfa-firmware
Summary:	Brocade Fibre Channel HBA Firmware
Version:	3.0.0.0
Release:	1%{?dist}
License:	Redistributable, no modification permitted
Group:		System Environment/Kernel
# These files were taken from:
# http://www.brocade.com/sites/dotcom/services-support/drivers-downloads/CNA/Linux.page
# No direct link is available.
Source0:	bfa_firmware_linux-%{version}-0.tgz
Source3:	LICENSE
URL:		http://www.brocade.com/sites/dotcom/services-support/drivers-downloads/CNA/Linux.page
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
# Needed for /lib/firmware
Requires:	udev

%description
Brocade Fibre Channel HBA Firmware.

%prep
%setup -n 3.0_GA_firwmare_image -q
cp %{SOURCE3} .

%build
# Firmware, do nothing.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/lib/firmware/
install -m0644 cbfw.bin ct2fw.bin ctfw.bin %{buildroot}/lib/firmware/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE
/lib/firmware/cbfw.bin
/lib/firmware/ctfw.bin
/lib/firmware/ct2fw.bin

%changelog
* Wed Sep 07 2011 Tom Callaway <spot@fedoraproject.org> 3.0.0.0-1
- update to 3.0.0.0

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan  3 2011 Tom Callaway <spot@fedoraproject.org> 2.3.2.3-1
- update to 2.3.2.3

* Mon Mar  8 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.1.2.1-2
- Add missing Requires: udev

* Fri Jan 29 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.1.2.1-1
- Initial package for Fedora
