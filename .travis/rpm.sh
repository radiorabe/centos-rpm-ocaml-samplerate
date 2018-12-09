#!/bin/bash
#
# RPM build wrapper for ocaml-samplerate, runs inside the build container on travis-ci

set -xe

curl -o /etc/yum.repos.d/liquidsoap.repo https://download.opensuse.org/repositories/home:/radiorabe:/liquidsoap/CentOS_7/home:radiorabe:liquidsoap.repo

yum -y install \
    epel-release

chown root:root ocaml-samplerate.spec

USER=nobody build-rpm-package.sh ocaml-samplerate.spec
