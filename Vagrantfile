Vagrant::Config.run do |config|

  config.vm.box = "lucid32"
  config.vm.box_url = "http://files.vagrantup.com/lucid32.box"

  config.vm.share_folder("v-root", "/vagrant", ".", :nfs => true)

  config.vm.forward_port("ssh", 22, 2222, :auto => true)

  config.vm.network("33.33.33.70")

  config.vm.provision :chef_solo do |chef|

    chef.recipe_url = "http://cloud.github.com/downloads/d0ugal/chef_recipes/cookbooks.tar.gz"
    chef.cookbooks_path = [:vm, "cookbooks"]

    chef.add_recipe "main"
    chef.add_recipe "python"
    chef.add_recipe "postgres"

    chef.json.merge!({

      :project_name => "tally",

    })

  end

end

