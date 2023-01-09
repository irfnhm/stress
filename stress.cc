#include <iostream>
#include <thread>
#include <vector>

#include <curl/curl.h>

void sendRequest() {
  CURL *curl;
  CURLcode res;

  curl = curl_easy_init();
  if (curl) {
    curl_easy_setopt(curl, CURLOPT_URL, "https://example.com");
    res = curl_easy_perform(curl);
    if (res != CURLE_OK) {
      std::cerr << "curl_easy_perform() failed: " << curl_easy_strerror(res) << std::endl;
    }
    curl_easy_cleanup(curl);
  }
}

int main() {
  std::vector<std::thread> threads;

  for (int i = 0; i < 10000000000000000000; i++) {
    threads.emplace_back(sendRequest);
  }

  for (auto &t : threads) {
    t.join();
  }

  return 0;
}
