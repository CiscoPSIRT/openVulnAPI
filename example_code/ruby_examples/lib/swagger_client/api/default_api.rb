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

require "uri"

module SwaggerClient
  class DefaultApi
    attr_accessor :api_client

    def initialize(api_client = ApiClient.default)
      @api_client = api_client
    end

    #
    # Used to obtain an advisory given its advisory ID `advisory_id` (i.e., cisco-sa-20180221-ucdm)
    # @param advisory_id advisory ID
    # @param [Hash] opts the optional parameters
    # @return [nil]
    def security_advisories_advisory_advisory_id_get(advisory_id, opts = {})
      security_advisories_advisory_advisory_id_get_with_http_info(advisory_id, opts)
      return nil
    end

    #
    # Used to obtain an advisory given its advisory ID &#x60;advisory_id&#x60; (i.e., cisco-sa-20180221-ucdm)
    # @param advisory_id advisory ID
    # @param [Hash] opts the optional parameters
    # @return [Array<(nil, Fixnum, Hash)>] nil, response status code and response headers
    def security_advisories_advisory_advisory_id_get_with_http_info(advisory_id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug "Calling API: DefaultApi.security_advisories_advisory_advisory_id_get ..."
      end
      # verify the required parameter 'advisory_id' is set
      if @api_client.config.client_side_validation && advisory_id.nil?
        fail ArgumentError, "Missing the required parameter 'advisory_id' when calling DefaultApi.security_advisories_advisory_advisory_id_get"
      end
      # resource path
      local_var_path = "/security/advisories/advisory/{advisory_id}".sub('{' + 'advisory_id' + '}', advisory_id.to_s)

      # query parameters
      query_params = {}

      # header parameters
      header_params = {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = {}

      # http body (model)
      post_body = nil
      auth_names = ['psirt_openvuln_api_auth']
      data, status_code, headers = @api_client.call_api(:GET, local_var_path,
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: DefaultApi#security_advisories_advisory_advisory_id_get\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    #
    # Used to obtain information about all published security advisories. By default the output is in JSON. To obtain the output in XML use the .xml extension. For example, /advisories/all.xml
    # @param [Hash] opts the optional parameters
    # @return [nil]
    def security_advisories_all_get(opts = {})
      security_advisories_all_get_with_http_info(opts)
      return nil
    end

    #
    # Used to obtain information about all published security advisories. By default the output is in JSON. To obtain the output in XML use the .xml extension. For example, /advisories/all.xml
    # @param [Hash] opts the optional parameters
    # @return [Array<(nil, Fixnum, Hash)>] nil, response status code and response headers
    def security_advisories_all_get_with_http_info(opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug "Calling API: DefaultApi.security_advisories_all_get ..."
      end
      # resource path
      local_var_path = "/security/advisories/all"

      # query parameters
      query_params = {}

      # header parameters
      header_params = {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = {}

      # http body (model)
      post_body = nil
      auth_names = ['psirt_openvuln_api_auth']
      data, status_code, headers = @api_client.call_api(:GET, local_var_path,
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: DefaultApi#security_advisories_all_get\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    #
    # Used to obtain an advisory using a given Common Vulnerability Enumerator (CVE). The `cve_id` format is CVE-YYYY-NNNN. For more information about CVE visit http://cve.mitre.org/
    # @param cve_id CVE Identifier (i.e., CVE-YYYY-NNNN)
    # @param [Hash] opts the optional parameters
    # @return [nil]
    def security_advisories_cve_cve_id_get(cve_id, opts = {})
      security_advisories_cve_cve_id_get_with_http_info(cve_id, opts)
      return nil
    end

    #
    # Used to obtain an advisory using a given Common Vulnerability Enumerator (CVE). The &#x60;cve_id&#x60; format is CVE-YYYY-NNNN. For more information about CVE visit http://cve.mitre.org/
    # @param cve_id CVE Identifier (i.e., CVE-YYYY-NNNN)
    # @param [Hash] opts the optional parameters
    # @return [Array<(nil, Fixnum, Hash)>] nil, response status code and response headers
    def security_advisories_cve_cve_id_get_with_http_info(cve_id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug "Calling API: DefaultApi.security_advisories_cve_cve_id_get ..."
      end
      # verify the required parameter 'cve_id' is set
      if @api_client.config.client_side_validation && cve_id.nil?
        fail ArgumentError, "Missing the required parameter 'cve_id' when calling DefaultApi.security_advisories_cve_cve_id_get"
      end
      # resource path
      local_var_path = "/security/advisories/cve/{cve_id}".sub('{' + 'cve_id' + '}', cve_id.to_s)

      # query parameters
      query_params = {}

      # header parameters
      header_params = {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = {}

      # http body (model)
      post_body = nil
      auth_names = ['psirt_openvuln_api_auth']
      data, status_code, headers = @api_client.call_api(:GET, local_var_path,
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: DefaultApi#security_advisories_cve_cve_id_get\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    #
    # Used to obtain all advisories that affects the given ios version
    # @param version IOS version to obtain security advisories
    # @param [Hash] opts the optional parameters
    # @return [nil]
    def security_advisories_ios_get(version, opts = {})
      security_advisories_ios_get_with_http_info(version, opts)
      return nil
    end

    #
    # Used to obtain all advisories that affects the given ios version
    # @param version IOS version to obtain security advisories
    # @param [Hash] opts the optional parameters
    # @return [Array<(nil, Fixnum, Hash)>] nil, response status code and response headers
    def security_advisories_ios_get_with_http_info(version, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug "Calling API: DefaultApi.security_advisories_ios_get ..."
      end
      # verify the required parameter 'version' is set
      if @api_client.config.client_side_validation && version.nil?
        fail ArgumentError, "Missing the required parameter 'version' when calling DefaultApi.security_advisories_ios_get"
      end
      # resource path
      local_var_path = "/security/advisories/ios"

      # query parameters
      query_params = {}
      query_params[:'version'] = version

      # header parameters
      header_params = {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = {}

      # http body (model)
      post_body = nil
      auth_names = ['psirt_openvuln_api_auth']
      data, status_code, headers = @api_client.call_api(:GET, local_var_path,
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: DefaultApi#security_advisories_ios_get\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    #
    # Used to obtain all advisories that affects the given ios version
    # @param version IOS version to obtain security advisories
    # @param [Hash] opts the optional parameters
    # @return [nil]
    def security_advisories_iosxe_get(version, opts = {})
      security_advisories_iosxe_get_with_http_info(version, opts)
      return nil
    end

    #
    # Used to obtain all advisories that affects the given ios version
    # @param version IOS version to obtain security advisories
    # @param [Hash] opts the optional parameters
    # @return [Array<(nil, Fixnum, Hash)>] nil, response status code and response headers
    def security_advisories_iosxe_get_with_http_info(version, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug "Calling API: DefaultApi.security_advisories_iosxe_get ..."
      end
      # verify the required parameter 'version' is set
      if @api_client.config.client_side_validation && version.nil?
        fail ArgumentError, "Missing the required parameter 'version' when calling DefaultApi.security_advisories_iosxe_get"
      end
      # resource path
      local_var_path = "/security/advisories/iosxe"

      # query parameters
      query_params = {}
      query_params[:'version'] = version

      # header parameters
      header_params = {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = {}

      # http body (model)
      post_body = nil
      auth_names = ['psirt_openvuln_api_auth']
      data, status_code, headers = @api_client.call_api(:GET, local_var_path,
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: DefaultApi#security_advisories_iosxe_get\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    #
    # Used to obtain all the latest security advisories given an absolute number. For instance, the latest 10 or latest 5.
    # @param number An absolute number to obtain the latest security advisories.
    # @param [Hash] opts the optional parameters
    # @return [nil]
    def security_advisories_latest_number_get(number, opts = {})
      security_advisories_latest_number_get_with_http_info(number, opts)
      return nil
    end

    #
    # Used to obtain all the latest security advisories given an absolute number. For instance, the latest 10 or latest 5.
    # @param number An absolute number to obtain the latest security advisories.
    # @param [Hash] opts the optional parameters
    # @return [Array<(nil, Fixnum, Hash)>] nil, response status code and response headers
    def security_advisories_latest_number_get_with_http_info(number, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug "Calling API: DefaultApi.security_advisories_latest_number_get ..."
      end
      # verify the required parameter 'number' is set
      if @api_client.config.client_side_validation && number.nil?
        fail ArgumentError, "Missing the required parameter 'number' when calling DefaultApi.security_advisories_latest_number_get"
      end
      # resource path
      local_var_path = "/security/advisories/latest/{number}".sub('{' + 'number' + '}', number.to_s)

      # query parameters
      query_params = {}

      # header parameters
      header_params = {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = {}

      # http body (model)
      post_body = nil
      auth_names = ['psirt_openvuln_api_auth']
      data, status_code, headers = @api_client.call_api(:GET, local_var_path,
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: DefaultApi#security_advisories_latest_number_get\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    #
    # Used to obtain all the advisories that affects the given product name.
    # @param product An product name to obtain security advisories that matches given product name.
    # @param [Hash] opts the optional parameters
    # @return [nil]
    def security_advisories_product_get(product, opts = {})
      security_advisories_product_get_with_http_info(product, opts)
      return nil
    end

    #
    # Used to obtain all the advisories that affects the given product name.
    # @param product An product name to obtain security advisories that matches given product name.
    # @param [Hash] opts the optional parameters
    # @return [Array<(nil, Fixnum, Hash)>] nil, response status code and response headers
    def security_advisories_product_get_with_http_info(product, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug "Calling API: DefaultApi.security_advisories_product_get ..."
      end
      # verify the required parameter 'product' is set
      if @api_client.config.client_side_validation && product.nil?
        fail ArgumentError, "Missing the required parameter 'product' when calling DefaultApi.security_advisories_product_get"
      end
      # resource path
      local_var_path = "/security/advisories/product"

      # query parameters
      query_params = {}
      query_params[:'product'] = product

      # header parameters
      header_params = {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = {}

      # http body (model)
      post_body = nil
      auth_names = ['psirt_openvuln_api_auth']
      data, status_code, headers = @api_client.call_api(:GET, local_var_path,
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: DefaultApi#security_advisories_product_get\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    #
    # Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) and additionally filter based of firstpublished start date and enddate.
    # @param severity Used to obtain all advisories that have a security impact rating of critical
    # @param start_date
    # @param end_date
    # @param [Hash] opts the optional parameters
    # @return [nil]
    def security_advisories_severity_severity_firstpublished_get(severity, start_date, end_date, opts = {})
      security_advisories_severity_severity_firstpublished_get_with_http_info(severity, start_date, end_date, opts)
      return nil
    end

    #
    # Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) and additionally filter based of firstpublished start date and enddate.
    # @param severity Used to obtain all advisories that have a security impact rating of critical
    # @param start_date
    # @param end_date
    # @param [Hash] opts the optional parameters
    # @return [Array<(nil, Fixnum, Hash)>] nil, response status code and response headers
    def security_advisories_severity_severity_firstpublished_get_with_http_info(severity, start_date, end_date, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug "Calling API: DefaultApi.security_advisories_severity_severity_firstpublished_get ..."
      end
      # verify the required parameter 'severity' is set
      if @api_client.config.client_side_validation && severity.nil?
        fail ArgumentError, "Missing the required parameter 'severity' when calling DefaultApi.security_advisories_severity_severity_firstpublished_get"
      end
      # verify enum value
      if @api_client.config.client_side_validation && !['critical', 'high', 'medium', 'low'].include?(severity)
        fail ArgumentError, "invalid value for 'severity', must be one of critical, high, medium, low"
      end
      # verify the required parameter 'start_date' is set
      if @api_client.config.client_side_validation && start_date.nil?
        fail ArgumentError, "Missing the required parameter 'start_date' when calling DefaultApi.security_advisories_severity_severity_firstpublished_get"
      end
      # verify the required parameter 'end_date' is set
      if @api_client.config.client_side_validation && end_date.nil?
        fail ArgumentError, "Missing the required parameter 'end_date' when calling DefaultApi.security_advisories_severity_severity_firstpublished_get"
      end
      # resource path
      local_var_path = "/security/advisories/severity/{severity}/firstpublished".sub('{' + 'severity' + '}', severity.to_s)

      # query parameters
      query_params = {}
      query_params[:'startDate'] = start_date
      query_params[:'endDate'] = end_date

      # header parameters
      header_params = {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = {}

      # http body (model)
      post_body = nil
      auth_names = ['psirt_openvuln_api_auth']
      data, status_code, headers = @api_client.call_api(:GET, local_var_path,
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: DefaultApi#security_advisories_severity_severity_firstpublished_get\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    #
    # Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low).
    # @param severity Critical, High, Medium, Low
    # @param [Hash] opts the optional parameters
    # @return [nil]
    def security_advisories_severity_severity_get(severity, opts = {})
      security_advisories_severity_severity_get_with_http_info(severity, opts)
      return nil
    end

    #
    # Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low).
    # @param severity Critical, High, Medium, Low
    # @param [Hash] opts the optional parameters
    # @return [Array<(nil, Fixnum, Hash)>] nil, response status code and response headers
    def security_advisories_severity_severity_get_with_http_info(severity, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug "Calling API: DefaultApi.security_advisories_severity_severity_get ..."
      end
      # verify the required parameter 'severity' is set
      if @api_client.config.client_side_validation && severity.nil?
        fail ArgumentError, "Missing the required parameter 'severity' when calling DefaultApi.security_advisories_severity_severity_get"
      end
      # verify enum value
      if @api_client.config.client_side_validation && !['critical', 'high', 'medium', 'low'].include?(severity)
        fail ArgumentError, "invalid value for 'severity', must be one of critical, high, medium, low"
      end
      # resource path
      local_var_path = "/security/advisories/severity/{severity}".sub('{' + 'severity' + '}', severity.to_s)

      # query parameters
      query_params = {}

      # header parameters
      header_params = {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = {}

      # http body (model)
      post_body = nil
      auth_names = ['psirt_openvuln_api_auth']
      data, status_code, headers = @api_client.call_api(:GET, local_var_path,
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: DefaultApi#security_advisories_severity_severity_get\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    #
    # Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low).
    # @param severity Used to obtain all advisories that have a security impact rating of critical
    # @param start_date
    # @param end_date
    # @param [Hash] opts the optional parameters
    # @return [nil]
    def security_advisories_severity_severity_lastpublished_get(severity, start_date, end_date, opts = {})
      security_advisories_severity_severity_lastpublished_get_with_http_info(severity, start_date, end_date, opts)
      return nil
    end

    #
    # Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low).
    # @param severity Used to obtain all advisories that have a security impact rating of critical
    # @param start_date
    # @param end_date
    # @param [Hash] opts the optional parameters
    # @return [Array<(nil, Fixnum, Hash)>] nil, response status code and response headers
    def security_advisories_severity_severity_lastpublished_get_with_http_info(severity, start_date, end_date, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug "Calling API: DefaultApi.security_advisories_severity_severity_lastpublished_get ..."
      end
      # verify the required parameter 'severity' is set
      if @api_client.config.client_side_validation && severity.nil?
        fail ArgumentError, "Missing the required parameter 'severity' when calling DefaultApi.security_advisories_severity_severity_lastpublished_get"
      end
      # verify enum value
      if @api_client.config.client_side_validation && !['critical', 'high', 'medium', 'low'].include?(severity)
        fail ArgumentError, "invalid value for 'severity', must be one of critical, high, medium, low"
      end
      # verify the required parameter 'start_date' is set
      if @api_client.config.client_side_validation && start_date.nil?
        fail ArgumentError, "Missing the required parameter 'start_date' when calling DefaultApi.security_advisories_severity_severity_lastpublished_get"
      end
      # verify the required parameter 'end_date' is set
      if @api_client.config.client_side_validation && end_date.nil?
        fail ArgumentError, "Missing the required parameter 'end_date' when calling DefaultApi.security_advisories_severity_severity_lastpublished_get"
      end
      # resource path
      local_var_path = "/security/advisories/severity/{severity}/lastpublished".sub('{' + 'severity' + '}', severity.to_s)

      # query parameters
      query_params = {}
      query_params[:'startDate'] = start_date
      query_params[:'endDate'] = end_date

      # header parameters
      header_params = {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = {}

      # http body (model)
      post_body = nil
      auth_names = ['psirt_openvuln_api_auth']
      data, status_code, headers = @api_client.call_api(:GET, local_var_path,
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: DefaultApi#security_advisories_severity_severity_lastpublished_get\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    #
    # Used to obtain all security advisories that have were orginally published in a specific year `YYYY`.
    # @param year The four digit year.
    # @param [Hash] opts the optional parameters
    # @return [nil]
    def security_advisories_year_year_get(year, opts = {})
      security_advisories_year_year_get_with_http_info(year, opts)
      return nil
    end

    #
    # Used to obtain all security advisories that have were orginally published in a specific year &#x60;YYYY&#x60;.
    # @param year The four digit year.
    # @param [Hash] opts the optional parameters
    # @return [Array<(nil, Fixnum, Hash)>] nil, response status code and response headers
    def security_advisories_year_year_get_with_http_info(year, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug "Calling API: DefaultApi.security_advisories_year_year_get ..."
      end
      # verify the required parameter 'year' is set
      if @api_client.config.client_side_validation && year.nil?
        fail ArgumentError, "Missing the required parameter 'year' when calling DefaultApi.security_advisories_year_year_get"
      end
      # resource path
      local_var_path = "/security/advisories/year/{year}".sub('{' + 'year' + '}', year.to_s)

      # query parameters
      query_params = {}

      # header parameters
      header_params = {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = {}

      # http body (model)
      post_body = nil
      auth_names = ['psirt_openvuln_api_auth']
      data, status_code, headers = @api_client.call_api(:GET, local_var_path,
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: DefaultApi#security_advisories_year_year_get\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
  end
end
