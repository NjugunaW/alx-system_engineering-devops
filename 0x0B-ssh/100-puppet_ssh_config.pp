#!/usr/bin/env bash

# Using Puppet to make changes to our configuration file
include stdlib

_file_line { 'No password authentication':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}

_file_line { 'Use the private key':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school'
}
