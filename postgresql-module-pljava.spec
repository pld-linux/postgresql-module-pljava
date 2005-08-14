#
%define		postgresql_version	8.0.3
%define		postgresql_release	3
%define		_pgmoduledir		%{_libdir}/postgresql

Summary:	PL/Java - PostgreSQL procedural language
Summary(pl):	PL/Java - jêzyk proceduralny bazy danych PostgreSQL
Name:		postgresql-module-pljava
Version:	1.1.0
Release:	1
License:	BSD
Group:		Applications/Databases
Source0:	http://gborg.postgresql.org/download/pljava/stable/pljava-src-%{version}.tar.gz
BuildRequires:	postgresql-backend-devel
Requires:	postgresql = %{postgresql_version}-%{postgresql_release}
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

%description -l pl
Z dokumentacji PostgreSQL:

Postgres ma wsparcie dla jêzyków proceduralnych. W przypadku, kiedy
programista zdefiniuje procedurê wyzwalacza lub funkcjê w jêzyku
proceduralnym, baza danych nie ma pojêcia jak interpretowaæ tego typu
funkcjê. Funkcja lub procedura ta jest przekazywana do interpretera,
który wie jak j± wykonaæ. Interpreter jest odpowiedni±, specjaln±
funkcj±, która jest skompilowana w obiekt dzielony i ³adowany w razie
potrzeby.

Za pomoc± polecenia createlang mo¿na dodaæ obs³ugê jêzyka
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

%changelog
* %{date} PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org

$Log: postgresql-module-pljava.spec,v $
Revision 1.2  2005-08-14 11:32:35  zbyniu
- JAVA_HOME; cleanups

Revision 1.1  2005/05/30 14:56:22  martii
- new spec
- initial version not test
- not finished
