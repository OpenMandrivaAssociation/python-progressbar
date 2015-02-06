%define module	progressbar

Summary:	Progress bar module for Python

Name:		python-%{module}
Version:	2.3
Release:	3
Source0:	http://python-%{module}.googlecode.com/files/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://pypi.python.org/progressbar/
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:  python-devel

%description
The progressbar Python module provides a text mode progress bar class
that can be used to display the progress of an operation that takes a
long time.

%prep
%setup -q -n %{module}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
chmod 644 *.txt
sed -i 's/.*egg-info$//' FILE_LIST

%files -f FILE_LIST
%doc *.txt examples.py


