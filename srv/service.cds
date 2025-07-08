using my.cap from '../db/schema';

service CatalogService {
  entity Books as projection on my.cap.Books;
}