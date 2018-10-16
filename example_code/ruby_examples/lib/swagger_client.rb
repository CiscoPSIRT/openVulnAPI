=begin
###############################################################################
# This is an example in Ruby of how you can create different functions
# to query each of the Resource URIs of the openVuln API.
# ** This is just a starting point, you will need to add your own authentication
# information and Authorization tokens
#
# For a complete "turn-key" tool, check out the openVulnQuery python tool
# https://github.com/CiscoPSIRT/openVulnAPI/tree/master/openVulnQuery
# Contact: os@cisco.com

=end

# Common files
require 'swagger_client/api_client'
require 'swagger_client/api_error'
require 'swagger_client/version'
require 'swagger_client/configuration'

# Models

# APIs
require 'swagger_client/api/default_api'

module SwaggerClient
  class << self
    # Customize default settings for the SDK using block.
    #   SwaggerClient.configure do |config|
    #     config.username = "xxx"
    #     config.password = "xxx"
    #   end
    # If no block given, return the default Configuration object.
    def configure
      if block_given?
        yield(Configuration.default)
      else
        Configuration.default
      end
    end
  end
end
