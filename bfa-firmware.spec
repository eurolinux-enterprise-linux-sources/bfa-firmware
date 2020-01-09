Name:		bfa-firmware
Summary:	Brocade Fibre Channel HBA Firmware
Version:	3.0.3.1
Release:	1%{?dist}
License:	Redistributable, no modification permitted
Group:		System Environment/Kernel
# These files were taken from:
# http://www.brocade.com/sites/dotcom/services-support/drivers-downloads/CNA/Linux.page
# No direct link is available.
Source0:	bfa_firmware_linux-%{version}-0.tgz
# We need to keep the old 3.0.0.0 firmware around for RHEL builds
Source1:	bfa_firmware_linux-3.0.0.0-0.tgz
Source3:	LICENSE
URL:		http://www.brocade.com/sites/dotcom/services-support/drivers-downloads/CNA/Linux.page
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
# Needed for /lib/firmware
Requires:	udev

%description
Brocade Fibre Channel HBA Firmware.

%prep
%setup -c -n %{name}-%{version} -q
cp %{SOURCE3} .
# RHEL needs to also have the old 3.0.0.0 firmware present, to ensure
# compatibility for the pre-6.4 kernels. These firmware files are not versioned.
# When the upstream driver change to use a versioned firmware lands in Fedora
# we will need to apply the renaming changes universally.
%if 0%{?rhel}
# Rename the new files to embed version in the way that the RHEL 6.4 driver
# is expecting.
mv cbfw.bin cbfw-%{version}.bin
mv ct2fw.bin ct2fw-%{version}.bin
mv ctfw.bin ctfw-%{version}.bin
# Unpack the old source into 3.0_GA_firwmare_image/
tar xvf %{SOURCE1}
%endif

%build
# Firmware, do nothing.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/lib/firmware/

%if 0%{?rhel}
install -m0644 cbfw-%{version}.bin ct2fw-%{version}.bin ctfw-%{version}.bin %{buildroot}/lib/firmware/
pushd 3.0_GA_firwmare_image
install -m0644 cbfw.bin ct2fw.bin ctfw.bin %{buildroot}/lib/firmware/
popd
pushd %{buildroot}/lib/firmware/
ln -s cbfw.bin cbfw-3.0.0.0.bin
ln -s ct2fw.bin ct2fw-3.0.0.0.bin
ln -s ctfw.bin ctfw-3.0.0.0.bin
popd
%else
install -m0644 cbfw.bin ct2fw.bin ctfw.bin %{buildroot}/lib/firmware/
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE
%if 0%{?rhel}
/lib/firmware/cbfw-%{version}.bin
/lib/firmware/ctfw-%{version}.bin
/lib/firmware/ct2fw-%{version}.bin
/lib/firmware/cbfw-3.0.0.0.bin
/lib/firmware/ctfw-3.0.0.0.bin
/lib/firmware/ct2fw-3.0.0.0.bin
%endif
/lib/firmware/cbfw.bin
/lib/firmware/ctfw.bin
/lib/firmware/ct2fw.bin

%changelog
* Thu Sep  6 2012 Tom Callaway <spot@fedoraproject.org> 3.0.3.1-1
- update to 3.0.3.1

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

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
