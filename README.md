# What is this spec?

This spec is an attempt to push for a stable replacement of Ruby 1.8.x with 1.9.2+ on RHEL based systems. I have based it off of the work of [FrameOS](http://www.frameos.org) specs for Ruby 1.9.2 and Ruby Enterprise Edition.

### How to install

#### RHEL/CentOS 5/6

    yum install -y rpm-build rpmdevtools
    rpmdev-setuptree
    cd ~/rpmbuild/SOURCES
    wget http://ftp.ruby-lang.org/pub/ruby/1.9/ruby-1.9.2-p180.tar.gz
    cd ~/rpmbuild/SPECS
    curl https://raw.github.com/robduncan/ruby-1.9.2-rpm/master/ruby19.spec > ruby19.spec
    rpmbuild -bb ruby19.spec
    rpm -Uvh ~/rpmbuild/RPMS/x86_64/ruby-1.9.2p180-2.ruby-1.9.2p180-2.i386.rpm

**PROFIT!**

### What it does

+ Builds
+ Installs

### Distro support

Tested working (as sane as I could test for) on:

* RHEL 5.6 x86_64
* RHEL 6 x86_64
* RHEL 6.1 x86_64
* RHEL 6.1 i686
* CentOS 5.6 x86_64