=begin
#Cisco PSIRT openVuln API

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

module SwaggerClient
  class ApiError < StandardError
    attr_reader :code, :response_headers, :response_body

    # Usage examples:
    #   ApiError.new
    #   ApiError.new("message")
    #   ApiError.new(:code => 500, :response_headers => {}, :response_body => "")
    #   ApiError.new(:code => 404, :message => "Not Found")
    def initialize(arg = nil)
      if arg.is_a? Hash
        if arg.key?(:message) || arg.key?('message')
          super(arg[:message] || arg['message'])
        else
          super arg
        end

        arg.each do |k, v|
          instance_variable_set "@#{k}", v
        end
      else
        super arg
      end
    end
  end
end
