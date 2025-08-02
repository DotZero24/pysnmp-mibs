_E='applicationIndex'
_D='deviceIndex'
_C='MIB-Dell-CM'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class SystemID(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
class Unsigned16BitRange(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dell_ObjectIdentity=ObjectIdentity
dell=_Dell_ObjectIdentity((1,3,6,1,4,1,674))
_Cm_ObjectIdentity=ObjectIdentity
cm=_Cm_ObjectIdentity((1,3,6,1,4,1,674,10899))
_InventoryGroup_ObjectIdentity=ObjectIdentity
inventoryGroup=_InventoryGroup_ObjectIdentity((1,3,6,1,4,1,674,10899,1))
_InventoryLocale_Type=DisplayString
_InventoryLocale_Object=MibScalar
inventoryLocale=_InventoryLocale_Object((1,3,6,1,4,1,674,10899,1,1),_InventoryLocale_Type())
inventoryLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:inventoryLocale.setStatus(_A)
_InventorySchemaVersion_Type=DisplayString
_InventorySchemaVersion_Object=MibScalar
inventorySchemaVersion=_InventorySchemaVersion_Object((1,3,6,1,4,1,674,10899,1,2),_InventorySchemaVersion_Type())
inventorySchemaVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:inventorySchemaVersion.setStatus(_A)
_InventorySystemID_Type=SystemID
_InventorySystemID_Object=MibScalar
inventorySystemID=_InventorySystemID_Object((1,3,6,1,4,1,674,10899,1,3),_InventorySystemID_Type())
inventorySystemID.setMaxAccess(_B)
if mibBuilder.loadTexts:inventorySystemID.setStatus(_A)
_DeviceTable_Object=MibTable
deviceTable=_DeviceTable_Object((1,3,6,1,4,1,674,10899,1,5))
if mibBuilder.loadTexts:deviceTable.setStatus(_A)
_DeviceEntry_Object=MibTableRow
deviceEntry=_DeviceEntry_Object((1,3,6,1,4,1,674,10899,1,5,1))
deviceEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:deviceEntry.setStatus(_A)
_DeviceIndex_Type=Unsigned16BitRange
_DeviceIndex_Object=MibTableColumn
deviceIndex=_DeviceIndex_Object((1,3,6,1,4,1,674,10899,1,5,1,1),_DeviceIndex_Type())
deviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceIndex.setStatus(_A)
_DeviceComponentID_Type=Integer32
_DeviceComponentID_Object=MibTableColumn
deviceComponentID=_DeviceComponentID_Object((1,3,6,1,4,1,674,10899,1,5,1,2),_DeviceComponentID_Type())
deviceComponentID.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceComponentID.setStatus(_A)
_DeviceDisplayString_Type=DisplayString
_DeviceDisplayString_Object=MibTableColumn
deviceDisplayString=_DeviceDisplayString_Object((1,3,6,1,4,1,674,10899,1,5,1,3),_DeviceDisplayString_Type())
deviceDisplayString.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceDisplayString.setStatus(_A)
_DeviceVendorID_Type=OctetString
_DeviceVendorID_Object=MibTableColumn
deviceVendorID=_DeviceVendorID_Object((1,3,6,1,4,1,674,10899,1,5,1,4),_DeviceVendorID_Type())
deviceVendorID.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceVendorID.setStatus(_A)
_DeviceDeviceID_Type=OctetString
_DeviceDeviceID_Object=MibTableColumn
deviceDeviceID=_DeviceDeviceID_Object((1,3,6,1,4,1,674,10899,1,5,1,5),_DeviceDeviceID_Type())
deviceDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceDeviceID.setStatus(_A)
_DeviceSubID_Type=OctetString
_DeviceSubID_Object=MibTableColumn
deviceSubID=_DeviceSubID_Object((1,3,6,1,4,1,674,10899,1,5,1,6),_DeviceSubID_Type())
deviceSubID.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceSubID.setStatus(_A)
_DeviceSubVendorID_Type=OctetString
_DeviceSubVendorID_Object=MibTableColumn
deviceSubVendorID=_DeviceSubVendorID_Object((1,3,6,1,4,1,674,10899,1,5,1,7),_DeviceSubVendorID_Type())
deviceSubVendorID.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceSubVendorID.setStatus(_A)
_ApplicationTable_Object=MibTable
applicationTable=_ApplicationTable_Object((1,3,6,1,4,1,674,10899,1,6))
if mibBuilder.loadTexts:applicationTable.setStatus(_A)
_ApplicationEntry_Object=MibTableRow
applicationEntry=_ApplicationEntry_Object((1,3,6,1,4,1,674,10899,1,6,1))
applicationEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:applicationEntry.setStatus(_A)
_ApplicationIndex_Type=Unsigned16BitRange
_ApplicationIndex_Object=MibTableColumn
applicationIndex=_ApplicationIndex_Object((1,3,6,1,4,1,674,10899,1,6,1,1),_ApplicationIndex_Type())
applicationIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:applicationIndex.setStatus(_A)
_ApplicationDeviceIndex_Type=Unsigned16BitRange
_ApplicationDeviceIndex_Object=MibTableColumn
applicationDeviceIndex=_ApplicationDeviceIndex_Object((1,3,6,1,4,1,674,10899,1,6,1,2),_ApplicationDeviceIndex_Type())
applicationDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:applicationDeviceIndex.setStatus(_A)
_ApplicationComponentType_Type=DisplayString
_ApplicationComponentType_Object=MibTableColumn
applicationComponentType=_ApplicationComponentType_Object((1,3,6,1,4,1,674,10899,1,6,1,3),_ApplicationComponentType_Type())
applicationComponentType.setMaxAccess(_B)
if mibBuilder.loadTexts:applicationComponentType.setStatus(_A)
_ApplicationVersion_Type=DisplayString
_ApplicationVersion_Object=MibTableColumn
applicationVersion=_ApplicationVersion_Object((1,3,6,1,4,1,674,10899,1,6,1,4),_ApplicationVersion_Type())
applicationVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:applicationVersion.setStatus(_A)
_ApplicationDisplayString_Type=DisplayString
_ApplicationDisplayString_Object=MibTableColumn
applicationDisplayString=_ApplicationDisplayString_Object((1,3,6,1,4,1,674,10899,1,6,1,5),_ApplicationDisplayString_Type())
applicationDisplayString.setMaxAccess(_B)
if mibBuilder.loadTexts:applicationDisplayString.setStatus(_A)
_ApplicationSubComponentID_Type=DisplayString
_ApplicationSubComponentID_Object=MibTableColumn
applicationSubComponentID=_ApplicationSubComponentID_Object((1,3,6,1,4,1,674,10899,1,6,1,6),_ApplicationSubComponentID_Type())
applicationSubComponentID.setMaxAccess(_B)
if mibBuilder.loadTexts:applicationSubComponentID.setStatus(_A)
_OperatingSystemGroup_ObjectIdentity=ObjectIdentity
operatingSystemGroup=_OperatingSystemGroup_ObjectIdentity((1,3,6,1,4,1,674,10899,2))
_OperatingSystemVendor_Type=DisplayString
_OperatingSystemVendor_Object=MibScalar
operatingSystemVendor=_OperatingSystemVendor_Object((1,3,6,1,4,1,674,10899,2,1),_OperatingSystemVendor_Type())
operatingSystemVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:operatingSystemVendor.setStatus(_A)
_OperatingSystemMajorVersion_Type=DisplayString
_OperatingSystemMajorVersion_Object=MibScalar
operatingSystemMajorVersion=_OperatingSystemMajorVersion_Object((1,3,6,1,4,1,674,10899,2,2),_OperatingSystemMajorVersion_Type())
operatingSystemMajorVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:operatingSystemMajorVersion.setStatus(_A)
_OperatingSystemMinorVersion_Type=DisplayString
_OperatingSystemMinorVersion_Object=MibScalar
operatingSystemMinorVersion=_OperatingSystemMinorVersion_Object((1,3,6,1,4,1,674,10899,2,3),_OperatingSystemMinorVersion_Type())
operatingSystemMinorVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:operatingSystemMinorVersion.setStatus(_A)
_OperatingSystemSPMajorVersion_Type=DisplayString
_OperatingSystemSPMajorVersion_Object=MibScalar
operatingSystemSPMajorVersion=_OperatingSystemSPMajorVersion_Object((1,3,6,1,4,1,674,10899,2,5),_OperatingSystemSPMajorVersion_Type())
operatingSystemSPMajorVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:operatingSystemSPMajorVersion.setStatus(_A)
_OperatingSystemSPMinorVersion_Type=DisplayString
_OperatingSystemSPMinorVersion_Object=MibScalar
operatingSystemSPMinorVersion=_OperatingSystemSPMinorVersion_Object((1,3,6,1,4,1,674,10899,2,6),_OperatingSystemSPMinorVersion_Type())
operatingSystemSPMinorVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:operatingSystemSPMinorVersion.setStatus(_A)
_OperatingSystemArchitecture_Type=DisplayString
_OperatingSystemArchitecture_Object=MibScalar
operatingSystemArchitecture=_OperatingSystemArchitecture_Object((1,3,6,1,4,1,674,10899,2,7),_OperatingSystemArchitecture_Type())
operatingSystemArchitecture.setMaxAccess(_B)
if mibBuilder.loadTexts:operatingSystemArchitecture.setStatus(_A)
_ProductID_ObjectIdentity=ObjectIdentity
productID=_ProductID_ObjectIdentity((1,3,6,1,4,1,674,10899,100))
_ProductIDDisplayName_Type=DisplayString
_ProductIDDisplayName_Object=MibScalar
productIDDisplayName=_ProductIDDisplayName_Object((1,3,6,1,4,1,674,10899,100,1),_ProductIDDisplayName_Type())
productIDDisplayName.setMaxAccess(_B)
if mibBuilder.loadTexts:productIDDisplayName.setStatus(_A)
_ProductIDDescription_Type=DisplayString
_ProductIDDescription_Object=MibScalar
productIDDescription=_ProductIDDescription_Object((1,3,6,1,4,1,674,10899,100,2),_ProductIDDescription_Type())
productIDDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:productIDDescription.setStatus(_A)
_ProductIDVendor_Type=DisplayString
_ProductIDVendor_Object=MibScalar
productIDVendor=_ProductIDVendor_Object((1,3,6,1,4,1,674,10899,100,3),_ProductIDVendor_Type())
productIDVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:productIDVendor.setStatus(_A)
_ProductIDVersion_Type=DisplayString
_ProductIDVersion_Object=MibScalar
productIDVersion=_ProductIDVersion_Object((1,3,6,1,4,1,674,10899,100,4),_ProductIDVersion_Type())
productIDVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:productIDVersion.setStatus(_A)
_ProductIDBuildNumber_Type=DisplayString
_ProductIDBuildNumber_Object=MibScalar
productIDBuildNumber=_ProductIDBuildNumber_Object((1,3,6,1,4,1,674,10899,100,5),_ProductIDBuildNumber_Type())
productIDBuildNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:productIDBuildNumber.setStatus('obsolete')
mibBuilder.exportSymbols(_C,**{'SystemID':SystemID,'Unsigned16BitRange':Unsigned16BitRange,'dell':dell,'cm':cm,'inventoryGroup':inventoryGroup,'inventoryLocale':inventoryLocale,'inventorySchemaVersion':inventorySchemaVersion,'inventorySystemID':inventorySystemID,'deviceTable':deviceTable,'deviceEntry':deviceEntry,_D:deviceIndex,'deviceComponentID':deviceComponentID,'deviceDisplayString':deviceDisplayString,'deviceVendorID':deviceVendorID,'deviceDeviceID':deviceDeviceID,'deviceSubID':deviceSubID,'deviceSubVendorID':deviceSubVendorID,'applicationTable':applicationTable,'applicationEntry':applicationEntry,_E:applicationIndex,'applicationDeviceIndex':applicationDeviceIndex,'applicationComponentType':applicationComponentType,'applicationVersion':applicationVersion,'applicationDisplayString':applicationDisplayString,'applicationSubComponentID':applicationSubComponentID,'operatingSystemGroup':operatingSystemGroup,'operatingSystemVendor':operatingSystemVendor,'operatingSystemMajorVersion':operatingSystemMajorVersion,'operatingSystemMinorVersion':operatingSystemMinorVersion,'operatingSystemSPMajorVersion':operatingSystemSPMajorVersion,'operatingSystemSPMinorVersion':operatingSystemSPMinorVersion,'operatingSystemArchitecture':operatingSystemArchitecture,'productID':productID,'productIDDisplayName':productIDDisplayName,'productIDDescription':productIDDescription,'productIDVendor':productIDVendor,'productIDVersion':productIDVersion,'productIDBuildNumber':productIDBuildNumber})