_L='contNetAddressIndex'
_K='contResourceID'
_J='operational'
_I='testing'
_H='contPhysicalEntryID'
_G='contLogicalEntryID'
_F='DisplayString'
_E='Integer32'
_D='read-write'
_C='CT-CONTAINER-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctChassis2,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctChassis2')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
_ContType_ObjectIdentity=ObjectIdentity
contType=_ContType_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,9,1))
_ContTypeDevice_Type=ObjectIdentifier
_ContTypeDevice_Object=MibScalar
contTypeDevice=_ContTypeDevice_Object((1,3,6,1,4,1,52,4,1,1,9,1,1),_ContTypeDevice_Type())
contTypeDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:contTypeDevice.setStatus(_A)
_ContTypePhysicalEntries_Type=Integer32
_ContTypePhysicalEntries_Object=MibScalar
contTypePhysicalEntries=_ContTypePhysicalEntries_Object((1,3,6,1,4,1,52,4,1,1,9,1,2),_ContTypePhysicalEntries_Type())
contTypePhysicalEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:contTypePhysicalEntries.setStatus(_A)
_ContTypePhysicalChanges_Type=Counter32
_ContTypePhysicalChanges_Object=MibScalar
contTypePhysicalChanges=_ContTypePhysicalChanges_Object((1,3,6,1,4,1,52,4,1,1,9,1,3),_ContTypePhysicalChanges_Type())
contTypePhysicalChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:contTypePhysicalChanges.setStatus(_A)
_ContTypeLogicalChanges_Type=Counter32
_ContTypeLogicalChanges_Object=MibScalar
contTypeLogicalChanges=_ContTypeLogicalChanges_Object((1,3,6,1,4,1,52,4,1,1,9,1,4),_ContTypeLogicalChanges_Type())
contTypeLogicalChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:contTypeLogicalChanges.setStatus(_A)
_ContTypeSerialNumber_Type=DisplayString
_ContTypeSerialNumber_Object=MibScalar
contTypeSerialNumber=_ContTypeSerialNumber_Object((1,3,6,1,4,1,52,4,1,1,9,1,5),_ContTypeSerialNumber_Type())
contTypeSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:contTypeSerialNumber.setStatus(_A)
_ContTypeContainingDevice_Type=ObjectIdentifier
_ContTypeContainingDevice_Object=MibScalar
contTypeContainingDevice=_ContTypeContainingDevice_Object((1,3,6,1,4,1,52,4,1,1,9,1,6),_ContTypeContainingDevice_Type())
contTypeContainingDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:contTypeContainingDevice.setStatus(_A)
_ContTypeContainingPhysicalEntries_Type=Integer32
_ContTypeContainingPhysicalEntries_Object=MibScalar
contTypeContainingPhysicalEntries=_ContTypeContainingPhysicalEntries_Object((1,3,6,1,4,1,52,4,1,1,9,1,7),_ContTypeContainingPhysicalEntries_Type())
contTypeContainingPhysicalEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:contTypeContainingPhysicalEntries.setStatus(_A)
_ContTypeContainingPhysicalEntryID_Type=Integer32
_ContTypeContainingPhysicalEntryID_Object=MibScalar
contTypeContainingPhysicalEntryID=_ContTypeContainingPhysicalEntryID_Object((1,3,6,1,4,1,52,4,1,1,9,1,8),_ContTypeContainingPhysicalEntryID_Type())
contTypeContainingPhysicalEntryID.setMaxAccess(_B)
if mibBuilder.loadTexts:contTypeContainingPhysicalEntryID.setStatus(_A)
_ContTypeContainingSerialNumber_Type=DisplayString
_ContTypeContainingSerialNumber_Object=MibScalar
contTypeContainingSerialNumber=_ContTypeContainingSerialNumber_Object((1,3,6,1,4,1,52,4,1,1,9,1,9),_ContTypeContainingSerialNumber_Type())
contTypeContainingSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:contTypeContainingSerialNumber.setStatus(_A)
_ContLogical_ObjectIdentity=ObjectIdentity
contLogical=_ContLogical_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,9,2))
_ContLogicalEntryTable_Object=MibTable
contLogicalEntryTable=_ContLogicalEntryTable_Object((1,3,6,1,4,1,52,4,1,1,9,2,1))
if mibBuilder.loadTexts:contLogicalEntryTable.setStatus(_A)
_ContLogicalEntry_Object=MibTableRow
contLogicalEntry=_ContLogicalEntry_Object((1,3,6,1,4,1,52,4,1,1,9,2,1,1))
contLogicalEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:contLogicalEntry.setStatus(_A)
_ContLogicalEntryID_Type=Integer32
_ContLogicalEntryID_Object=MibTableColumn
contLogicalEntryID=_ContLogicalEntryID_Object((1,3,6,1,4,1,52,4,1,1,9,2,1,1,1),_ContLogicalEntryID_Type())
contLogicalEntryID.setMaxAccess(_B)
if mibBuilder.loadTexts:contLogicalEntryID.setStatus(_A)
_ContLogicalEntryType_Type=ObjectIdentifier
_ContLogicalEntryType_Object=MibTableColumn
contLogicalEntryType=_ContLogicalEntryType_Object((1,3,6,1,4,1,52,4,1,1,9,2,1,1,2),_ContLogicalEntryType_Type())
contLogicalEntryType.setMaxAccess(_B)
if mibBuilder.loadTexts:contLogicalEntryType.setStatus(_A)
class _ContLogicalEntryName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ContLogicalEntryName_Type.__name__=_F
_ContLogicalEntryName_Object=MibTableColumn
contLogicalEntryName=_ContLogicalEntryName_Object((1,3,6,1,4,1,52,4,1,1,9,2,1,1,3),_ContLogicalEntryName_Type())
contLogicalEntryName.setMaxAccess(_B)
if mibBuilder.loadTexts:contLogicalEntryName.setStatus(_A)
class _ContLogicalEntryVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ContLogicalEntryVersion_Type.__name__=_F
_ContLogicalEntryVersion_Object=MibTableColumn
contLogicalEntryVersion=_ContLogicalEntryVersion_Object((1,3,6,1,4,1,52,4,1,1,9,2,1,1,4),_ContLogicalEntryVersion_Type())
contLogicalEntryVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:contLogicalEntryVersion.setStatus(_A)
_ContLogicalEntryROCommStr_Type=OctetString
_ContLogicalEntryROCommStr_Object=MibTableColumn
contLogicalEntryROCommStr=_ContLogicalEntryROCommStr_Object((1,3,6,1,4,1,52,4,1,1,9,2,1,1,5),_ContLogicalEntryROCommStr_Type())
contLogicalEntryROCommStr.setMaxAccess(_B)
if mibBuilder.loadTexts:contLogicalEntryROCommStr.setStatus(_A)
_ContLogicalEntryRWCommStr_Type=OctetString
_ContLogicalEntryRWCommStr_Object=MibTableColumn
contLogicalEntryRWCommStr=_ContLogicalEntryRWCommStr_Object((1,3,6,1,4,1,52,4,1,1,9,2,1,1,6),_ContLogicalEntryRWCommStr_Type())
contLogicalEntryRWCommStr.setMaxAccess(_B)
if mibBuilder.loadTexts:contLogicalEntryRWCommStr.setStatus(_A)
_ContLogicalEntrySUCommStr_Type=OctetString
_ContLogicalEntrySUCommStr_Object=MibTableColumn
contLogicalEntrySUCommStr=_ContLogicalEntrySUCommStr_Object((1,3,6,1,4,1,52,4,1,1,9,2,1,1,7),_ContLogicalEntrySUCommStr_Type())
contLogicalEntrySUCommStr.setMaxAccess(_B)
if mibBuilder.loadTexts:contLogicalEntrySUCommStr.setStatus(_A)
class _ContLogicalEntryAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,7,9)));namedValues=NamedValues(*(('enable',3),('disable',7),('reset',9)))
_ContLogicalEntryAdminStatus_Type.__name__=_E
_ContLogicalEntryAdminStatus_Object=MibTableColumn
contLogicalEntryAdminStatus=_ContLogicalEntryAdminStatus_Object((1,3,6,1,4,1,52,4,1,1,9,2,1,1,8),_ContLogicalEntryAdminStatus_Type())
contLogicalEntryAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:contLogicalEntryAdminStatus.setStatus(_A)
class _ContLogicalEntryOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('unknown',1),('invalid',2),('enabled',3),(_I,4),(_J,5),('error',6),('disabled',7),('delete',8)))
_ContLogicalEntryOperStatus_Type.__name__=_E
_ContLogicalEntryOperStatus_Object=MibTableColumn
contLogicalEntryOperStatus=_ContLogicalEntryOperStatus_Object((1,3,6,1,4,1,52,4,1,1,9,2,1,1,9),_ContLogicalEntryOperStatus_Type())
contLogicalEntryOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:contLogicalEntryOperStatus.setStatus(_A)
_ContPhysical_ObjectIdentity=ObjectIdentity
contPhysical=_ContPhysical_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,9,3))
_ContPhysicalEntryTable_Object=MibTable
contPhysicalEntryTable=_ContPhysicalEntryTable_Object((1,3,6,1,4,1,52,4,1,1,9,3,1))
if mibBuilder.loadTexts:contPhysicalEntryTable.setStatus(_A)
_ContPhysicalEntry_Object=MibTableRow
contPhysicalEntry=_ContPhysicalEntry_Object((1,3,6,1,4,1,52,4,1,1,9,3,1,1))
contPhysicalEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:contPhysicalEntry.setStatus(_A)
_ContPhysicalEntryID_Type=Integer32
_ContPhysicalEntryID_Object=MibTableColumn
contPhysicalEntryID=_ContPhysicalEntryID_Object((1,3,6,1,4,1,52,4,1,1,9,3,1,1,1),_ContPhysicalEntryID_Type())
contPhysicalEntryID.setMaxAccess(_B)
if mibBuilder.loadTexts:contPhysicalEntryID.setStatus(_A)
_ContPhysicalEntries_Type=Integer32
_ContPhysicalEntries_Object=MibTableColumn
contPhysicalEntries=_ContPhysicalEntries_Object((1,3,6,1,4,1,52,4,1,1,9,3,1,1,2),_ContPhysicalEntries_Type())
contPhysicalEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:contPhysicalEntries.setStatus(_A)
_ContPhysicalEntryClass_Type=ObjectIdentifier
_ContPhysicalEntryClass_Object=MibTableColumn
contPhysicalEntryClass=_ContPhysicalEntryClass_Object((1,3,6,1,4,1,52,4,1,1,9,3,1,1,3),_ContPhysicalEntryClass_Type())
contPhysicalEntryClass.setMaxAccess(_B)
if mibBuilder.loadTexts:contPhysicalEntryClass.setStatus(_A)
_ContPhysicalEntryType_Type=ObjectIdentifier
_ContPhysicalEntryType_Object=MibTableColumn
contPhysicalEntryType=_ContPhysicalEntryType_Object((1,3,6,1,4,1,52,4,1,1,9,3,1,1,4),_ContPhysicalEntryType_Type())
contPhysicalEntryType.setMaxAccess(_B)
if mibBuilder.loadTexts:contPhysicalEntryType.setStatus(_A)
_ContPhysicalEntryTimeStamp_Type=TimeTicks
_ContPhysicalEntryTimeStamp_Object=MibTableColumn
contPhysicalEntryTimeStamp=_ContPhysicalEntryTimeStamp_Object((1,3,6,1,4,1,52,4,1,1,9,3,1,1,5),_ContPhysicalEntryTimeStamp_Type())
contPhysicalEntryTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:contPhysicalEntryTimeStamp.setStatus(_A)
class _ContPhysicalEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,11)));namedValues=NamedValues(*(('reset',1),('powerOff',2),('busy',3),('crippled',4),(_J,5),('error',6),(_I,7),('booting',11)))
_ContPhysicalEntryStatus_Type.__name__=_E
_ContPhysicalEntryStatus_Object=MibTableColumn
contPhysicalEntryStatus=_ContPhysicalEntryStatus_Object((1,3,6,1,4,1,52,4,1,1,9,3,1,1,6),_ContPhysicalEntryStatus_Type())
contPhysicalEntryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:contPhysicalEntryStatus.setStatus(_A)
_ContLogicalToPhysicalMapTable_Object=MibTable
contLogicalToPhysicalMapTable=_ContLogicalToPhysicalMapTable_Object((1,3,6,1,4,1,52,4,1,1,9,3,2))
if mibBuilder.loadTexts:contLogicalToPhysicalMapTable.setStatus(_A)
_ContLogicalToPhysicalMapEntry_Object=MibTableRow
contLogicalToPhysicalMapEntry=_ContLogicalToPhysicalMapEntry_Object((1,3,6,1,4,1,52,4,1,1,9,3,2,1))
contLogicalToPhysicalMapEntry.setIndexNames((0,_C,_H),(0,_C,_G))
if mibBuilder.loadTexts:contLogicalToPhysicalMapEntry.setStatus(_A)
_ContPhysicalEntryMapID_Type=Integer32
_ContPhysicalEntryMapID_Object=MibTableColumn
contPhysicalEntryMapID=_ContPhysicalEntryMapID_Object((1,3,6,1,4,1,52,4,1,1,9,3,2,1,1),_ContPhysicalEntryMapID_Type())
contPhysicalEntryMapID.setMaxAccess(_B)
if mibBuilder.loadTexts:contPhysicalEntryMapID.setStatus(_A)
_ContLogicalEntryMapID_Type=Integer32
_ContLogicalEntryMapID_Object=MibTableColumn
contLogicalEntryMapID=_ContLogicalEntryMapID_Object((1,3,6,1,4,1,52,4,1,1,9,3,2,1,2),_ContLogicalEntryMapID_Type())
contLogicalEntryMapID.setMaxAccess(_B)
if mibBuilder.loadTexts:contLogicalEntryMapID.setStatus(_A)
_ContResource_ObjectIdentity=ObjectIdentity
contResource=_ContResource_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,9,4))
_ContResourceTable_Object=MibTable
contResourceTable=_ContResourceTable_Object((1,3,6,1,4,1,52,4,1,1,9,4,1))
if mibBuilder.loadTexts:contResourceTable.setStatus(_A)
_ContResourceEntry_Object=MibTableRow
contResourceEntry=_ContResourceEntry_Object((1,3,6,1,4,1,52,4,1,1,9,4,1,1))
contResourceEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:contResourceEntry.setStatus(_A)
_ContResourceID_Type=Integer32
_ContResourceID_Object=MibTableColumn
contResourceID=_ContResourceID_Object((1,3,6,1,4,1,52,4,1,1,9,4,1,1,1),_ContResourceID_Type())
contResourceID.setMaxAccess(_B)
if mibBuilder.loadTexts:contResourceID.setStatus(_A)
_ContResourceType_Type=ObjectIdentifier
_ContResourceType_Object=MibTableColumn
contResourceType=_ContResourceType_Object((1,3,6,1,4,1,52,4,1,1,9,4,1,1,2),_ContResourceType_Type())
contResourceType.setMaxAccess(_B)
if mibBuilder.loadTexts:contResourceType.setStatus(_A)
_ContResourceMibPointer_Type=ObjectIdentifier
_ContResourceMibPointer_Object=MibTableColumn
contResourceMibPointer=_ContResourceMibPointer_Object((1,3,6,1,4,1,52,4,1,1,9,4,1,1,3),_ContResourceMibPointer_Type())
contResourceMibPointer.setMaxAccess(_B)
if mibBuilder.loadTexts:contResourceMibPointer.setStatus(_A)
_ContCommStr_ObjectIdentity=ObjectIdentity
contCommStr=_ContCommStr_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,9,5))
_ContROCommStr_Type=OctetString
_ContROCommStr_Object=MibScalar
contROCommStr=_ContROCommStr_Object((1,3,6,1,4,1,52,4,1,1,9,5,1),_ContROCommStr_Type())
contROCommStr.setMaxAccess(_D)
if mibBuilder.loadTexts:contROCommStr.setStatus(_A)
_ContRWCommStr_Type=OctetString
_ContRWCommStr_Object=MibScalar
contRWCommStr=_ContRWCommStr_Object((1,3,6,1,4,1,52,4,1,1,9,5,2),_ContRWCommStr_Type())
contRWCommStr.setMaxAccess(_D)
if mibBuilder.loadTexts:contRWCommStr.setStatus(_A)
_ContSUCommStr_Type=OctetString
_ContSUCommStr_Object=MibScalar
contSUCommStr=_ContSUCommStr_Object((1,3,6,1,4,1,52,4,1,1,9,5,3),_ContSUCommStr_Type())
contSUCommStr.setMaxAccess(_D)
if mibBuilder.loadTexts:contSUCommStr.setStatus(_A)
_ContAddress_ObjectIdentity=ObjectIdentity
contAddress=_ContAddress_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,9,6))
_ContNetAddressTable_Object=MibTable
contNetAddressTable=_ContNetAddressTable_Object((1,3,6,1,4,1,52,4,1,1,9,6,1))
if mibBuilder.loadTexts:contNetAddressTable.setStatus(_A)
_ContNetAddressEntry_Object=MibTableRow
contNetAddressEntry=_ContNetAddressEntry_Object((1,3,6,1,4,1,52,4,1,1,9,6,1,1))
contNetAddressEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:contNetAddressEntry.setStatus(_A)
_ContNetAddressIndex_Type=Integer32
_ContNetAddressIndex_Object=MibTableColumn
contNetAddressIndex=_ContNetAddressIndex_Object((1,3,6,1,4,1,52,4,1,1,9,6,1,1,1),_ContNetAddressIndex_Type())
contNetAddressIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:contNetAddressIndex.setStatus(_A)
_ContNetAddressNetworkType_Type=ObjectIdentifier
_ContNetAddressNetworkType_Object=MibTableColumn
contNetAddressNetworkType=_ContNetAddressNetworkType_Object((1,3,6,1,4,1,52,4,1,1,9,6,1,1,2),_ContNetAddressNetworkType_Type())
contNetAddressNetworkType.setMaxAccess(_B)
if mibBuilder.loadTexts:contNetAddressNetworkType.setStatus(_A)
_ContNetAddress_Type=IpAddress
_ContNetAddress_Object=MibTableColumn
contNetAddress=_ContNetAddress_Object((1,3,6,1,4,1,52,4,1,1,9,6,1,1,3),_ContNetAddress_Type())
contNetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:contNetAddress.setStatus(_A)
_ContNetAddressMask_Type=IpAddress
_ContNetAddressMask_Object=MibTableColumn
contNetAddressMask=_ContNetAddressMask_Object((1,3,6,1,4,1,52,4,1,1,9,6,1,1,4),_ContNetAddressMask_Type())
contNetAddressMask.setMaxAccess(_D)
if mibBuilder.loadTexts:contNetAddressMask.setStatus(_A)
_ContTypeID_ObjectIdentity=ObjectIdentity
contTypeID=_ContTypeID_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,9,7))
_ContUnknownTypeID_ObjectIdentity=ObjectIdentity
contUnknownTypeID=_ContUnknownTypeID_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,9,7,1))
mibBuilder.exportSymbols(_C,**{'contType':contType,'contTypeDevice':contTypeDevice,'contTypePhysicalEntries':contTypePhysicalEntries,'contTypePhysicalChanges':contTypePhysicalChanges,'contTypeLogicalChanges':contTypeLogicalChanges,'contTypeSerialNumber':contTypeSerialNumber,'contTypeContainingDevice':contTypeContainingDevice,'contTypeContainingPhysicalEntries':contTypeContainingPhysicalEntries,'contTypeContainingPhysicalEntryID':contTypeContainingPhysicalEntryID,'contTypeContainingSerialNumber':contTypeContainingSerialNumber,'contLogical':contLogical,'contLogicalEntryTable':contLogicalEntryTable,'contLogicalEntry':contLogicalEntry,_G:contLogicalEntryID,'contLogicalEntryType':contLogicalEntryType,'contLogicalEntryName':contLogicalEntryName,'contLogicalEntryVersion':contLogicalEntryVersion,'contLogicalEntryROCommStr':contLogicalEntryROCommStr,'contLogicalEntryRWCommStr':contLogicalEntryRWCommStr,'contLogicalEntrySUCommStr':contLogicalEntrySUCommStr,'contLogicalEntryAdminStatus':contLogicalEntryAdminStatus,'contLogicalEntryOperStatus':contLogicalEntryOperStatus,'contPhysical':contPhysical,'contPhysicalEntryTable':contPhysicalEntryTable,'contPhysicalEntry':contPhysicalEntry,_H:contPhysicalEntryID,'contPhysicalEntries':contPhysicalEntries,'contPhysicalEntryClass':contPhysicalEntryClass,'contPhysicalEntryType':contPhysicalEntryType,'contPhysicalEntryTimeStamp':contPhysicalEntryTimeStamp,'contPhysicalEntryStatus':contPhysicalEntryStatus,'contLogicalToPhysicalMapTable':contLogicalToPhysicalMapTable,'contLogicalToPhysicalMapEntry':contLogicalToPhysicalMapEntry,'contPhysicalEntryMapID':contPhysicalEntryMapID,'contLogicalEntryMapID':contLogicalEntryMapID,'contResource':contResource,'contResourceTable':contResourceTable,'contResourceEntry':contResourceEntry,_K:contResourceID,'contResourceType':contResourceType,'contResourceMibPointer':contResourceMibPointer,'contCommStr':contCommStr,'contROCommStr':contROCommStr,'contRWCommStr':contRWCommStr,'contSUCommStr':contSUCommStr,'contAddress':contAddress,'contNetAddressTable':contNetAddressTable,'contNetAddressEntry':contNetAddressEntry,_L:contNetAddressIndex,'contNetAddressNetworkType':contNetAddressNetworkType,'contNetAddress':contNetAddress,'contNetAddressMask':contNetAddressMask,'contTypeID':contTypeID,'contUnknownTypeID':contUnknownTypeID})