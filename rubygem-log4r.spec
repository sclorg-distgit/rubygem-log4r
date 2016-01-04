%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from log4r-1.1.10.gem by gem2rpm -*- rpm-spec -*-
%global gem_name log4r

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.1.10
Release: 3%{?dist}
Summary: Log4r, logging framework for ruby
Group: Development/Languages
License: BDS
URL: https://github.com/colbygk/log4r
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel 
# We don't have test/unit nor compatible minitest version
#BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
#BuildRequires: %{?scl_prefix_ror}rubygem(builder)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}


%description
Log4r is a comprehensive and flexible logging library for use in Ruby programs.
It features a heirarchical logging system of any number of levels, custom level
names, multiple output destinations per log event, custom formatting, and more.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Run the test suite

%check
%{?scl:scl enable %{scl} - << \EOF}
pushd .%{gem_instdir}
# 6 failures
# https://github.com/colbygk/log4r/issues/37
#ruby -Ilib:tests -e 'Dir.glob "./tests/test*.rb", &method(:require)' | grep '47 tests, 180 assertions, 6 failures, 6 errors, 0 skips'
popd
%{?scl:EOF}

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/tests
%{gem_instdir}/doc
%{gem_instdir}/examples

%changelog
* Thu Jun 04 2015 Josef Stribny <jstribny@redhat.com> - 1.1.10-3
- Disable tests due to lack of test/unit

* Thu Oct 16 2014 Josef Stribny <jstribny@redhat.com> - 1.1.10-2
- Add SCL macros

* Mon Sep 08 2014 Josef Stribny <jstribny@redhat.com> - 1.1.10-1
- Initial package
