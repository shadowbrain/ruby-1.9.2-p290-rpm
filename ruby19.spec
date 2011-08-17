%define rubyver         1.9.2
%define rubyminorver    p290
%define _prefix		/opt/ruby-1.9.2
%define _localstatedir	/opt/ruby-1.9.2/var
%define _mandir		/opt/ruby-1.9.2/man
%define _infodir	/opt/ruby-1.9.2/share/info

Name:           ruby
Version:        %{rubyver}%{rubyminorver}
Release:        1%{?dist}
License:        Ruby License/GPL - see COPYING
URL:            http://www.ruby-lang.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  readline readline-devel ncurses ncurses-devel gdbm gdbm-devel glibc-devel tcl-devel gcc unzip openssl-devel db4-devel byacc make
Source0:        ftp://ftp.ruby-lang.org/pub/ruby/ruby-%{rubyver}-%{rubyminorver}.tar.gz
Summary:        An interpreter of object-oriented scripting language
Group:          Development/Languages
Provides: ruby(abi) = 1.9
Provides: ruby-irb
Provides: ruby-rdoc
Provides: ruby-libs
Provides: ruby-devel

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming.  It has many features to process text
files and to do system management tasks (as in Perl).  It is simple,
straight-forward, and extensible.

%prep
%setup -n ruby-%{rubyver}-%{rubyminorver}

%build
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"

./configure \
  --enable-shared \
  --disable-rpath \
  --prefix=%{_prefix}

make RUBY_INSTALL_NAME=ruby %{?_smp_mflags}

%install
#cleanup before install
rm -rf $RPM_BUILD_ROOT/usr/src

# installing binaries ...
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README COPYING ChangeLog LEGAL ToDo
%{_prefix}/*

%changelog
* Wed Aug 17 2011 Brian Butler <brian@tumblr.com> - 1.9.2-p290-1
- Created initial spec for ruby 1.9.2-p290
