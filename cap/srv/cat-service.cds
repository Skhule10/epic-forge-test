using { Entity } from '@sap/cds/common';

service ChatService {
  entity Messages : Entity {
    key ID : UUID;
    text  : String;
    author: String;
    timestamp: DateTime;
  };
}