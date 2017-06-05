###############################################################################
# This is an example in Ruby of how you can create different functions
# to query each of the Resource URIs of the openVuln API.
# ** This is just a starting point, you will need to add your own authentication
# information and Authorization tokens
#
# For a complete "turn-key" tool, check out the openVulnQuery python tool
# https://github.com/CiscoPSIRT/openVulnAPI/tree/master/openVulnQuery
###############################################################################

require 'net/http'
require 'net/https'

# /security/advisories/cvrf/all (GET )
def get_cvrf_all
  uri = URI('https://api.cisco.com/security/advisories/cvrf/all')

  # Create client
  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_PEER

  # Create Request
  req =  Net::HTTP::Get.new(uri)
  # Add headers - this is where you will put your Authorization token
  req.add_field "Authorization", "Bearer "

  # Fetch Request
  res = http.request(req)
  puts "Response HTTP Status Code: #{res.code}"
  puts "Response HTTP Response Body: #{res.body}"
rescue StandardError => e
  puts "HTTP Request failed (#{e.message})"
end


# /security/advisories/cvrf/cve/{cve_id} (GET )
def get_cvrf_cve
  uri = URI('https://api.cisco.com/security/advisories/cvrf/cve/')

  # Create client
  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_PEER

  # Create Request
  req =  Net::HTTP::Get.new(uri)
  # Add headers - this is where you will put your Authorization token
  req.add_field "Authorization", "Bearer "

  # Fetch Request
  res = http.request(req)
  puts "Response HTTP Status Code: #{res.code}"
  puts "Response HTTP Response Body: #{res.body}"
rescue StandardError => e
  puts "HTTP Request failed (#{e.message})"
end


# /security/advisories/cvrf/advisory/{advisory_id} (GET )
def get_cvrf_advisory
  uri = URI('https://api.cisco.com/security/advisories/cvrf/advisory/')

  # Create client
  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_PEER

  # Create Request
  req =  Net::HTTP::Get.new(uri)
  # Add headers - this is where you will put your Authorization token
  req.add_field "Authorization", "Bearer "

  # Fetch Request
  res = http.request(req)
  puts "Response HTTP Status Code: #{res.code}"
  puts "Response HTTP Response Body: #{res.body}"
rescue StandardError => e
  puts "HTTP Request failed (#{e.message})"
end


# /security/advisories/cvrf/severity/{severity} (GET )
def get_cvrf_severity
  uri = URI('https://api.cisco.com/security/advisories/cvrf/severity/')

  # Create client
  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_PEER

  # Create Request
  req =  Net::HTTP::Get.new(uri)
  # Add headers - this is where you will put your Authorization token
  req.add_field "Authorization", "Bearer "

  # Fetch Request
  res = http.request(req)
  puts "Response HTTP Status Code: #{res.code}"
  puts "Response HTTP Response Body: #{res.body}"
rescue StandardError => e
  puts "HTTP Request failed (#{e.message})"
end

# /security/advisories/cvrf/year/{year} (GET )
def get_cvrf_year
  uri = URI('https://api.cisco.com/security/advisories/cvrf/year/')

  # Create client
  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_PEER

  # Create Request
  req =  Net::HTTP::Get.new(uri)
  # Add headers - this is where you will put your Authorization token
  req.add_field "Authorization", "Bearer "

  # Fetch Request
  res = http.request(req)
  puts "Response HTTP Status Code: #{res.code}"
  puts "Response HTTP Response Body: #{res.body}"
rescue StandardError => e
  puts "HTTP Request failed (#{e.message})"
end


# /security/advisories/cvrf/latest/{number} (GET )
def get_cvrf_latest
  uri = URI('https://api.cisco.com/security/advisories/cvrf/latest/')

  # Create client
  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_PEER

  # Create Request
  req =  Net::HTTP::Get.new(uri)
  # Add headers - this is where you will put your Authorization token
  req.add_field "Authorization", "Bearer "

  # Fetch Request
  res = http.request(req)
  puts "Response HTTP Status Code: #{res.code}"
  puts "Response HTTP Response Body: #{res.body}"
rescue StandardError => e
  puts "HTTP Request failed (#{e.message})"
end


# /security/advisories/oval/all (GET )
def get_oval_all
  uri = URI('https://api.cisco.com/security/advisories/oval/all')

  # Create client
  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_PEER

  # Create Request
  req =  Net::HTTP::Get.new(uri)
  # Add headers - this is where you will put your Authorization token
  req.add_field "Authorization", "Bearer "

  # Fetch Request
  res = http.request(req)
  puts "Response HTTP Status Code: #{res.code}"
  puts "Response HTTP Response Body: #{res.body}"
rescue StandardError => e
  puts "HTTP Request failed (#{e.message})"
end

# /security/advisories/oval/cve/{cve_id} (GET )
def get_oval_cve
  uri = URI('https://api.cisco.com/security/advisories/oval/cve/')

  # Create client
  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_PEER

  # Create Request
  req =  Net::HTTP::Get.new(uri)
  # Add headers - this is where you will put your Authorization token
  req.add_field "Authorization", "Bearer "

  # Fetch Request
  res = http.request(req)
  puts "Response HTTP Status Code: #{res.code}"
  puts "Response HTTP Response Body: #{res.body}"
rescue StandardError => e
  puts "HTTP Request failed (#{e.message})"
end


# /security/advisories/oval/advisory/{advisory_id} (GET )
def get_oval_advisory
  uri = URI('https://api.cisco.com/security/advisories/oval/advisory/')

  # Create client
  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_PEER

  # Create Request
  req =  Net::HTTP::Get.new(uri)
  # Add headers
  req.add_field "Authorization", "Bearer "

  # Fetch Request
  res = http.request(req)
  puts "Response HTTP Status Code: #{res.code}"
  puts "Response HTTP Response Body: #{res.body}"
rescue StandardError => e
  puts "HTTP Request failed (#{e.message})"
end

# /security/advisories/oval/severity/{severity} (GET )
def get_oval_severity
  uri = URI('https://api.cisco.com/security/advisories/oval/severity/')

  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_PEER

  # Create Request
  req =  Net::HTTP::Get.new(uri)
  # Add headers - this is where you will put your Authorization token
  req.add_field "Authorization", "Bearer "

  # Fetch Request
  res = http.request(req)
  puts "Response HTTP Status Code: #{res.code}"
  puts "Response HTTP Response Body: #{res.body}"
rescue StandardError => e
  puts "HTTP Request failed (#{e.message})"
end

# /security/advisories/oval/latest/{number} (GET )
def get_oval_latest
  uri = URI('https://api.cisco.com/security/advisories/oval/latest/')

  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_PEER

  # Create Request
  req =  Net::HTTP::Get.new(uri)
  # Add headers - this is where you will put your Authorization token
  req.add_field "Authorization", "Bearer "

  # Fetch Request
  res = http.request(req)
  puts "Response HTTP Status Code: #{res.code}"
  puts "Response HTTP Response Body: #{res.body}"
rescue StandardError => e
  puts "HTTP Request failed (#{e.message})"
end
