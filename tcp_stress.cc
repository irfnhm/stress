#include <iostream>
#include <thread>
#include <vector>

#include <unistd.h>
#include <netdb.h>
#include <arpa/inet.h>

void connectToServer() {
  int sockfd = socket(AF_INET, SOCK_STREAM, 0);
  if (sockfd < 0) {
    std::cerr << "ERROR opening socket" << std::endl;
    return;
  }

  struct hostent *server = gethostbyname("example.com");
  if (server == NULL) {
    std::cerr << "ERROR, no such host" << std::endl;
    return;
  }

  struct sockaddr_in serv_addr{};
  serv_addr.sin_family = AF_INET;
  bcopy((char *)server->h_addr, (char *)&serv_addr.sin_addr.s_addr, (size_t)server->h_length);
  serv_addr.sin_port = htons(80);

  if (connect(sockfd, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
    std::cerr << "ERROR connecting" << std::endl;
    return;
  }

  // Send a message to the server
  write(sockfd, "GET / HTTP/1.0\r\n\r\n", 20);

  close(sockfd);
}

int main() {
  std::vector<std::thread> threads;

  for (int i = 0; i < 10; i++) {
    threads.emplace_back(connectToServer);
  }

  for (auto &t : threads) {
    t.join();
  }

  return 0;
}
