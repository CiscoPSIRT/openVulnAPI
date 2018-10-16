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

require 'spec_helper'

describe SwaggerClient::Configuration do
  let(:config) { SwaggerClient::Configuration.default }

  before(:each) do
    # uncomment below to setup host and base_path
    #require 'URI'
    #uri = URI.parse("https://api.cisco.com")
    #SwaggerClient.configure do |c|
    #  c.host = uri.host
    #  c.base_path = uri.path
    #end
  end

  describe '#base_url' do
    it 'should have the default value' do
      # uncomment below to test default value of the base path
      #expect(config.base_url).to eq("https://api.cisco.com")
    end

    it 'should remove trailing slashes' do
      [nil, '', '/', '//'].each do |base_path|
        config.base_path = base_path
        # uncomment below to test trailing slashes
        #expect(config.base_url).to eq("https://api.cisco.com")
      end
    end
  end
end
