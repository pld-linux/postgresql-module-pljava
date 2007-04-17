#
%define		_pgmoduledir		%{_libdir}/postgresql

Summary:	PL/Java - PostgreSQL procedural language
Summary(pl.UTF-8):	PL/Java - język proceduralny bazy danych PostgreSQL
Name:		postgresql-module-pljava
Version:	1.2.0
Release:	0.1
License:	BSD
Group:		Applications/Databases
Source0:	http://gborg.postgresql.org/download/pljava/stable/pljava-src-%{version}.tar.gz
# Source0-md5:	fca1db791d6888b6655efa04ce0b63ee
URL:		http://gborg.postgresql.org/project/pljava/projdisplay.php
BuildRequires:	postgresql-backend-devel >= 8.0
Requires:	postgresql >= 8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
From PostgreSQL documentation:

Postgres supports the definition of procedural languages. In the case
of a function or trigger procedure defined in a procedural language,
the database has no built-in knowledge about how to interpret the
function's source text. Instead, the task is passed to a handler that
knows the details of the language. The handler itself is a special
programming language function compiled into a shared object and loaded
on demand.

To enable PL/Java procedural language for your database you have to
run createlang command.

%description -l pl.UTF-8
Z dokumentacji PostgreSQL:

Postgres ma wsparcie dla języków proceduralnych. W przypadku, kiedy
programista zdefiniuje procedurę wyzwalacza lub funkcję w języku
proceduralnym, baza danych nie ma pojęcia jak interpretować tego typu
funkcję. Funkcja lub procedura ta jest przekazywana do interpretera,
który wie jak ją wykonać. Interpreter jest odpowiednią, specjalną
funkcją, która jest skompilowana w obiekt dzielony i ładowany w razie
potrzeby.

Za pomocą polecenia createlang można dodać obsługę języka
proceduralnego PL/Java dla swojej bazy danych.

%prep
%setup -q -n pljava-%{version}

%build
%{__make} \
	JAVA_HOME=/usr/lib/java

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pgmoduledir}

install build/objs/*.so $RPM_BUILD_ROOT%{_pgmoduledir}

%files
%defattr(644,root,root,755)
%doc docs/*
%attr(755,root,root) %{_pgmoduledir}/*.so
