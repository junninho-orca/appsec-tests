require 'base64'
require 'yaml'

# Insecure Deserialization
def insecure_deserialize(data)
  decoded_data = Base64.decode64(data)
  YAML.load(decoded_data)
end

# Example usage from a web request (e.g., Rails controller)
# params[:data] would come from user input
# user_input = params[:data]
# insecure_deserialize(user_input) 