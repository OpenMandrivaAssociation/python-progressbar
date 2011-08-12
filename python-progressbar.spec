%define module	progressbar
%define name	python-%{module}
%define version	2.3
%define release %mkrel 1

Summary:	Progress bar module for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://python-%{module}.googlecode.com/files/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://pypi.python.org/progressbar/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	python-setuptools
%py_requires -d

%description
The progressbar Python module provides a text mode progress bar class
that can be used to display the progress of an operation that takes a
long time.

%prep
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
chmod 644 *.txt

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc *.txt examples.py
