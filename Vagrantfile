# -*- mode: ruby -*-
# vi: set ft=ruby ts=2 sw=2 tw=0 et :

role = File.basename(File.expand_path(File.dirname(__FILE__)))

boxes = [
  {
    :name => "ubuntu-1404",
    :box => "bento/ubuntu-14.04",
    :ip => '10.0.0.12',
    :cpu => "50",
    :ram => "256"
  },
  {
    :name => "ubuntu-1604",
    :box => "bento/ubuntu-16.04",
    :ip => '10.0.0.13',
    :cpu => "50",
    :ram => "256"
  },
  {
    :name => "ubuntu-1804",
    :box => "bento/ubuntu-18.04",
    :ip => '10.0.0.14',
    :cpu => "50",
    :ram => "384"
  },
]

Vagrant.configure("2") do |config|
  boxes.each do |box|
    config.vm.define box[:name] do |vms|
      vms.vm.box = box[:box]
      vms.vm.hostname = "ansible-#{role}-#{box[:name]}"

      vms.vm.provider "virtualbox" do |v|
        v.customize ["modifyvm", :id, "--cpuexecutioncap", box[:cpu]]
        v.customize ["modifyvm", :id, "--memory", box[:ram]]
      end

      vms.vm.network :private_network, ip: box[:ip]

      vms.vm.provision :ansible do |ansible|
        ansible.playbook = "tests/vagrant.yml"
        ansible.verbose = "vv"
      end
    end
  end
end
