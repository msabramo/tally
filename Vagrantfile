Vagrant::Config.run do |config|

  config.vm.box = "lucid32"
  config.vm.box_url = "http://files.vagrantup.com/lucid32.box"

  config.vm.network :hostonly, "33.33.33.70"

  config.vm.provision :chef_solo do |chef|

    chef.recipe_url = "https://github.com/d0ugal/chef_recipes/tarball/master"
    chef.cookbooks_path = [:vm, "d0ugal-chef_recipes-6a1e376/cookbooks"]

    chef.add_recipe "python"

  end

end

