Vagrant.configure('2') do |config|
  config.vm.box = 'azure'
  config.vm.box_url = 'https://github.com/msopentech/vagrant-azure/raw/master/dummy.box' #Caja base vacía
  config.vm.network "private_network",ip: "192.168.50.4", virtualbox__intnet: "vboxnet0" #Ip privada
  config.vm.hostname = "localhost"
  config.vm.network "forwarded_port", guest: 80, host: 80

  # use local ssh key to connect to remote vagrant box
  config.ssh.private_key_path = '~/.ssh/id_rsa'

  config.vm.provider :azure do |azure, override|

    # use Azure Active Directory Application / Service Principal to connect to Azure
    # see: https://azure.microsoft.com/en-us/documentation/articles/resource-group-create-service-principal-portal/

    # each of the below values will default to use the env vars named as below if not specified explicitly

    azure.vm_image_urn = 'canonical:UbuntuServer:16.04-LTS:16.04.201701130' #Imagen base del sistema
    azure.vm_size = 'Basic_A0' #Tamaño (recursos) de la MV
    azure.location = 'westeurope'
    azure.vm_name = 'MVbaresytapas'
    azure.tcp_endpoints = '80:80'
    azure.vm_password = 'pass'

    azure.tenant_id = ENV['AZURE_TENANT_ID']
    azure.client_id = ENV['AZURE_CLIENT_ID']
    azure.client_secret = ENV['AZURE_CLIENT_SECRET']
    azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']
  end

  #Provisionamiento
  config.vm.provision "ansible" do |ansible|
        ansible.sudo = true
        ansible.playbook = "configuracion.yml"
        ansible.verbose = "-vvvv"
        ansible.host_key_checking = false
  end

end
