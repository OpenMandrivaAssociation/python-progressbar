%define module	progressbar
%define name	python-%{module}
%define version	2.3
%define rel	dev
%define release %mkrel 0.%rel.0

Summary:	Progress bar module for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://python-%{module}.googlecode.com/files/%{module}-%{version}-dev.tar.gz
Source1:	https://python-%{module}.googlecode.com/hg/%{module}/examples.py
License:	BSD
Group:		Development/Python
Url:		http://pypi.python.org/progressbar/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
%py_requires -d

%description
The progressbar Python module provides a text mode progress bar class
that can be used to display the progress of an operation that takes a
long time.

%prep
%setup -q -n %{module}-%{version}-dev

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
%__install -m 644 %SOURCE1 .
chmod 644 README LICENSE

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc README LICENSE examples.py
