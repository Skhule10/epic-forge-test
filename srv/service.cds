
    using { Entity } from '@sap/cds';

    service DigitalAssistantService {
        entity Queries : Entity {
            key ID : UUID;
            queryText : String;
            responseText : String;
        }
    }
    