# Domain Model



## Example

```yaml
$Type: DomainModels$DomainModel
Annotations:
- $Type: DomainModels$Annotation
  Caption: "This Domain model defines the data structure of this module. \r\n\r\nAdd
    new entities and associations to define your database tables and their relations.
    \r\nWe automatically provision the underlying database for you.\r\n\r\nTo define
    in-memory data, you can turn off the 'persistable' property on the entity.\r\n\r\nMore
    info: https://docs.mendix.com/refguide/domain-model"
  ExportLevel: Hidden
  Width: 440
Associations: null
CrossAssociations: null
Documentation: ""
Entities:
- $Type: DomainModels$EntityImpl
  AccessRules:
  - $Type: DomainModels$AccessRule
    AllowCreate: false
    AllowDelete: false
    AllowedModuleRoles:
    - MyFirstModule.User
    DefaultMemberAccessRights: ReadOnly
    Documentation: ""
    MemberAccesses:
    - $Type: DomainModels$MemberAccess
      AccessRights: ReadOnly
      Association: ""
      Attribute: System.Image.PublicThumbnailPath
    - $Type: DomainModels$MemberAccess
      AccessRights: ReadOnly
      Association: ""
      Attribute: System.Image.EnableCaching
    - $Type: DomainModels$MemberAccess
      AccessRights: ReadOnly
      Association: ""
      Attribute: System.FileDocument.FileID
    - $Type: DomainModels$MemberAccess
      AccessRights: ReadOnly
      Association: ""
      Attribute: System.FileDocument.Name
    - $Type: DomainModels$MemberAccess
      AccessRights: ReadOnly
      Association: ""
      Attribute: System.FileDocument.DeleteAfterDownload
    - $Type: DomainModels$MemberAccess
      AccessRights: ReadOnly
      Association: ""
      Attribute: System.FileDocument.Contents
    - $Type: DomainModels$MemberAccess
      AccessRights: ReadOnly
      Association: ""
      Attribute: System.FileDocument.HasContents
    - $Type: DomainModels$MemberAccess
      AccessRights: ReadOnly
      Association: ""
      Attribute: System.FileDocument.Size
    XPathConstraint: ""
    XPathConstraintCaption: ""
  Attributes: null
  Documentation: ""
  Events: null
  ExportLevel: Hidden
  Indexes: null
  MaybeGeneralization:
    $Type: DomainModels$Generalization
    Generalization: System.Image
  Name: Photo
  Source: null
  ValidationRules: null
- $Type: DomainModels$EntityImpl
  AccessRules:
  - $Type: DomainModels$AccessRule
    AllowCreate: false
    AllowDelete: false
    AllowedModuleRoles:
    - MyFirstModule.User
    DefaultMemberAccessRights: ReadOnly
    Documentation: ""
    MemberAccesses:
    - $Type: DomainModels$MemberAccess
      AccessRights: ReadOnly
      Association: ""
      Attribute: MyFirstModule.Bike.Name
    - $Type: DomainModels$MemberAccess
      AccessRights: ReadOnly
      Association: ""
      Attribute: MyFirstModule.Bike.PurchaseDate
    - $Type: DomainModels$MemberAccess
      AccessRights: ReadOnly
      Association: ""
      Attribute: MyFirstModule.Bike.VA_age
    - $Type: DomainModels$MemberAccess
      AccessRights: ReadOnly
      Association: ""
      Attribute: MyFirstModule.Bike.Year
    XPathConstraint: ""
    XPathConstraintCaption: ""
  Attributes:
  - $Type: DomainModels$Attribute
    Documentation: ""
    ExportLevel: Hidden
    Name: Name
    NewType:
      $Type: DomainModels$StringAttributeType
      Length: 200
    Value:
      $Type: DomainModels$StoredValue
      DefaultValue: ""
  - $Type: DomainModels$Attribute
    Documentation: ""
    ExportLevel: Hidden
    Name: PurchaseDate
    NewType:
      $Type: DomainModels$DateTimeAttributeType
      LocalizeDate: true
    Value:
      $Type: DomainModels$StoredValue
      DefaultValue: ""
  - $Type: DomainModels$Attribute
    Documentation: ""
    ExportLevel: Hidden
    Name: VA_age
    NewType:
      $Type: DomainModels$IntegerAttributeType
    Value:
      $Type: DomainModels$CalculatedValue
      Microflow: MyFirstModule.VA_Age
      PassEntity: true
  - $Type: DomainModels$Attribute
    Documentation: ""
    ExportLevel: Hidden
    Name: Year
    NewType:
      $Type: DomainModels$IntegerAttributeType
    Value:
      $Type: DomainModels$StoredValue
      DefaultValue: "2010"
  Documentation: ""
  Events: null
  ExportLevel: Hidden
  Indexes: null
  MaybeGeneralization:
    $Type: DomainModels$NoGeneralization
    HasChangedByAttr: false
    HasChangedDateAttr: false
    HasCreatedDateAttr: false
    HasOwnerAttr: false
    Persistable: true
  Name: Bike
  Source: null
  ValidationRules: null
```