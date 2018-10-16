# -*- encoding: utf-8 -*-
#
=begin
###############################################################################
# This is an example in Ruby of how you can create different functions
# to query each of the Resource URIs of the openVuln API.
# ** This is just a starting point, you will need to add your own authentication
# information and Authorization tokens
#
# For a complete "turn-key" tool, check out the openVulnQuery python tool
# https://github.com/CiscoPSIRT/openVulnAPI/tree/master/openVulnQuery
###############################################################################

=end

$:.push File.expand_path("../lib", __FILE__)
require "swagger_client/version"

Gem::Specification.new do |s|
  s.name        = "swagger_client"
  s.version     = SwaggerClient::VERSION
  s.platform    = Gem::Platform::RUBY
  s.authors     = ["Swagger-Codegen"]
  s.email       = ["os@cisco.com"]
  s.homepage    = "https://github.com/swagger-api/swagger-codegen"
  s.summary     = "Cisco PSIRT openVuln API Ruby Gem"
  s.description = "The Cisco Product Security Incident Response Team (PSIRT) openVuln API is a RESTful API that allows customers to obtain Cisco Security Vulnerability information in different machine-consumable formats. APIs are important for customers because they allow their technical staff and programmers to build tools that help them do their job more effectively (in this case, to keep up with security vulnerability information). For more information about the Cisco PSIRT openVuln API visit https://developer.cisco.com/psirt  For detail steps on how to use the API go to: https://developer.cisco.com/psirt  This is a beta release of a swagger YAML for the Cisco PSIRT openVuln API  To access the API sign in with your Cisco CCO account at http://apiconsole.cisco.com and register an application to recieve a client_id and a client_secret  You can then get your token using curl or any other method you prefer.  'curl -s -k -H \"Content-Type: application/x-www-form-urlencoded\" -X POST -d \"client_id=<your_client_id>\" -d \"client_secret=<your_client_secret>\" -d \"grant_type=client_credentials\" https://cloudsso.cisco.com/as/token.oauth2'  You will receive an access token as demonstrated in the following example:  '{\"access_token\":\"I7omWtBDAieSiUX3shOxNJfuy4J6\",\"token_type\":\"Bearer\",\"expires_in\":3599}'  In Swagger, click on Change Authentication  enter the text \"I7omWtBDAieSiUX3shOxNJfuy4J6\" (which is the token you received)  then click on \"Try this operation\" "
  # TODO uncommnet and update below with a proper license
  #s.license     = "Apache 2.0"
  s.required_ruby_version = ">= 1.9"

  s.add_runtime_dependency 'typhoeus', '~> 1.0', '>= 1.0.1'
  s.add_runtime_dependency 'json', '~> 2.1', '>= 2.1.0'

  s.add_development_dependency 'rspec', '~> 3.6', '>= 3.6.0'
  s.add_development_dependency 'vcr', '~> 3.0', '>= 3.0.1'
  s.add_development_dependency 'webmock', '~> 1.24', '>= 1.24.3'
  s.add_development_dependency 'autotest', '~> 4.4', '>= 4.4.6'
  s.add_development_dependency 'autotest-rails-pure', '~> 4.1', '>= 4.1.2'
  s.add_development_dependency 'autotest-growl', '~> 0.2', '>= 0.2.16'
  s.add_development_dependency 'autotest-fsevent', '~> 0.2', '>= 0.2.12'

  s.files         = `find *`.split("\n").uniq.sort.select{|f| !f.empty? }
  s.test_files    = `find spec/*`.split("\n")
  s.executables   = []
  s.require_paths = ["lib"]
end
