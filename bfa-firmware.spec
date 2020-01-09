Name:		bfa-firmware
Summary:	Brocade Fibre Channel HBA Firmware
Version:	2.3.2.3
Release:	1%{?dist}
License:	Redistributable, no modification permitted
Group:		System Environment/Kernel
# These files were taken from:
# http://www.brocade.com/forms/getFile?p=documents/downloads/HBA/Linux/Drivers/NOARCH/bfa_firmware_linux-2.3.2.3-0.src.rpm
Source0:	cbfw_fc.bin
Source1:	ctfw_fc.bin
Source2:	ctfw_cna.bin
Source3:	LICENSE
URL:		http://www.brocade.com/sites/dotcom/services-support/drivers-downloads/CNA/Linux.page
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
# Needed for /lib/firmware
Requires:	udev

%description
Brocade Fibre Channel HBA Firmware.

%prep
%setup -n %{name} -c -T
cp %{SOURCE0} .
cp %{SOURCE1} .
cp %{SOURCE2} .
cp %{SOURCE3} .

%build
# Firmware, do nothing.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/lib/firmware/
install -m0644 cbfw_fc.bin ctfw_fc.bin ctfw_cna.bin %{buildroot}/lib/firmware/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE
/lib/firmware/cbfw_fc.bin
/lib/firmware/ctfw_fc.bin
/lib/firmware/ctfw_cna.bin

%changelog
* Mon Jan  3 2011 Tom Callaway <spot@fedoraproject.org> 2.3.2.3-1
- update to 2.3.2.3

* Mon Mar  8 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.1.2.1-2
- Add missing Requires: udev

* Fri Jan 29 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.1.2.1-1
- Initial package for Fedora
