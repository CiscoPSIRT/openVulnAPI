<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Cisco PSIRT VulnAPI PHP Serverside Access Example</title>
  <script type="text/javascript">
  //minimal clientside code to display the json response in a prettier format
  window.onload=function(){
    var responseContainer=document.getElementById("responseContainer");
    var response=responseContainer.innerHTML;
    responseContainer.innerHTML=JSON.stringify(JSON.parse(response),null, '\t');
  };


  </script>
</head>
<body>
  <h1>Cisco PSIRT VulnAPI PHP Serverside Access Example</h1>
  <?PHP




  require __DIR__ . '/vendor/autoload.php';
  use GuzzleHttp\Client;

  session_start();

  $provider = new \League\OAuth2\Client\Provider\GenericProvider([
    'clientId'                => '<put here your client id>',    // The client ID assigned to you by the provider
    'clientSecret'            => '<put here your secret>',   // The client password assigned to you by the provider
    'redirectUri'             => 'http://myserver.example.com.com/vulnapi/vulnapicm.php',
    'urlAuthorize'            => 'https://cloudsso.cisco.com/as/authorization.oauth2',
    'urlAccessToken'          => 'https://cloudsso.cisco.com/as/token.oauth2',
    'urlResourceOwnerDetails' => ''
  ]);

  // If we don't have an authorization code then get one
  if (!isset($_GET['code'])) {

    // Fetch the authorization URL from the provider; this returns the
    // urlAuthorize option and generates and applies any necessary parameters
    // (e.g. state).
    $authorizationUrl = $provider->getAuthorizationUrl();

    // Get the state generated for you and store it to the session.
    $_SESSION['oauth2state'] = $provider->getState();

    // Redirect the user to the authorization URL.
    header('Location: ' . $authorizationUrl);
    exit;

    // Check given state against previously stored one to mitigate CSRF attack
  } elseif (empty($_GET['state']) || ($_GET['state'] !== $_SESSION['oauth2state'])) {
    var_dump($_GET['state']);
    var_dump($_SESSION['oauth2state']);
    unset($_SESSION['oauth2state']);
    exit('Invalid state');

  } else {

    try {

      // Try to get an access token using the authorization code grant.
      $accessToken = $provider->getAccessToken('authorization_code', [
        'code' => $_GET['code']
      ]);

      // We have an access token, which we may use in authenticated
      // requests against the service provider's API.
      echo "Access Token: ".$accessToken->getToken()."<br />";
      echo "Refresh Token: ".$accessToken->getRefreshToken()."<br />";
      echo "Expires: ".$accessToken->getExpires() ."<br />";
      echo "Has expired: ".($accessToken->hasExpired() ? 'expired' : 'not expired')."<br />";


      // The provider provides a way to get an authenticated API request for
      // the service, using the access token; it returns an object conforming
      // to Psr\Http\Message\RequestInterface.
      $request = $provider->getAuthenticatedRequest(
      'GET',
      'https://api-stage.cisco.com/security/advisories/cvrf/cve/CVE-2012-2486',
      $accessToken
    );

    //print var_export($request,true);

    $client = new Client([
      // Base URI is used with relative requests
      'base_uri' => 'https://api-stage.cisco.com',
      // You can set any number of default request options.
      'timeout'  => 2.0,
    ]);

    $response = $client->send($request, ['timeout' => 2]);

    print("<br/><br/>");
    //var_dump($response);

    if( $response->getStatusCode() == 200){
      print("<h2>REQUEST SUCCESSFUL</h2>");

      print('<pre id="responseContainer">'.$response->getBody().'</pre>');

    }




  } catch (\League\OAuth2\Client\Provider\Exception\IdentityProviderException $e) {

    // Failed to get the access token or user details.
    exit($e->getMessage());

  }

}

?>


</body>
</html>
