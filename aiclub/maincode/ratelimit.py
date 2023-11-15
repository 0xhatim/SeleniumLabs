import time
from django.http import HttpResponseForbidden

class RateLimitMiddleware:
    def __init__(self, get_response, rate_limit=8, rate_period=60):
        self.get_response = get_response
        self.rate_limit = rate_limit  # Number of requests allowed
        self.rate_period = rate_period  # Time period (in seconds) for the rate limit
        self.requests = {}  # Dictionary to store requests and their timestamps

    def __call__(self, request):
        # Get the IP address of the client (you can customize this based on your needs)
        ip_address = request.META.get('REMOTE_ADDR')

        # Get the current timestamp
        current_time = int(time.time())

        # Check if the IP address is in the requests dictionary
        if ip_address in self.requests:
            # If it is, check the timestamp of the last request
            last_request_time = self.requests[ip_address]
            
            # Calculate the time elapsed since the last request
            elapsed_time = current_time - last_request_time

            # If the time elapsed is within the rate limit period
            if elapsed_time < self.rate_period:
                # Check if the number of requests exceeds the rate limit
                if self.requests[ip_address + "_count"] >= self.rate_limit:
                    return HttpResponseForbidden("Rate limit exceeded. Please try again later.")

                # Increment the request count
                self.requests[ip_address + "_count"] += 1
            else:
                # Reset the request count and update the timestamp
                self.requests[ip_address + "_count"] = 1
                self.requests[ip_address] = current_time
        else:
            # If the IP address is not in the dictionary, add it
            self.requests[ip_address] = current_time
            self.requests[ip_address + "_count"] = 1

        # Call the next middleware or view function
        response = self.get_response(request)
        return response
