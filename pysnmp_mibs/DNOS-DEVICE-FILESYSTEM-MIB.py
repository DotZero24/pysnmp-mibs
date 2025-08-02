_G='agentDeviceFileSystemContentFileName'
_F='agentDevFileSystemIndex'
_E='agentDeviceFileSystemIndex'
_D='DNOS-DEVICE-FILESYSTEM-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dnOS,=mibBuilder.importSymbols('DELL-REF-MIB','dnOS')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
fastpathDeviceFileSystem=ModuleIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,44))
if mibBuilder.loadTexts:fastpathDeviceFileSystem.setRevisions(('2011-01-26 00:00',))
_AgentDeviceFileSystemGroup_ObjectIdentity=ObjectIdentity
agentDeviceFileSystemGroup=_AgentDeviceFileSystemGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,44,1))
_AgentDeviceFileSystemTable_Object=MibTable
agentDeviceFileSystemTable=_AgentDeviceFileSystemTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,44,1,1))
if mibBuilder.loadTexts:agentDeviceFileSystemTable.setStatus(_A)
_AgentDeviceFileSystemEntry_Object=MibTableRow
agentDeviceFileSystemEntry=_AgentDeviceFileSystemEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,44,1,1,1))
agentDeviceFileSystemEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:agentDeviceFileSystemEntry.setStatus(_A)
class _AgentDeviceFileSystemIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9))
_AgentDeviceFileSystemIndex_Type.__name__=_C
_AgentDeviceFileSystemIndex_Object=MibTableColumn
agentDeviceFileSystemIndex=_AgentDeviceFileSystemIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,44,1,1,1,1),_AgentDeviceFileSystemIndex_Type())
agentDeviceFileSystemIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDeviceFileSystemIndex.setStatus(_A)
class _AgentDeviceFileSystemStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('inactive',2),('invalid',3)))
_AgentDeviceFileSystemStatus_Type.__name__=_C
_AgentDeviceFileSystemStatus_Object=MibTableColumn
agentDeviceFileSystemStatus=_AgentDeviceFileSystemStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,44,1,1,1,2),_AgentDeviceFileSystemStatus_Type())
agentDeviceFileSystemStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDeviceFileSystemStatus.setStatus(_A)
_AgentDeviceFileSystemVendorID_Type=DisplayString
_AgentDeviceFileSystemVendorID_Object=MibTableColumn
agentDeviceFileSystemVendorID=_AgentDeviceFileSystemVendorID_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,44,1,1,1,3),_AgentDeviceFileSystemVendorID_Type())
agentDeviceFileSystemVendorID.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDeviceFileSystemVendorID.setStatus(_A)
_AgentDeviceFileSystemProductID_Type=DisplayString
_AgentDeviceFileSystemProductID_Object=MibTableColumn
agentDeviceFileSystemProductID=_AgentDeviceFileSystemProductID_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,44,1,1,1,4),_AgentDeviceFileSystemProductID_Type())
agentDeviceFileSystemProductID.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDeviceFileSystemProductID.setStatus(_A)
_AgentDeviceFileSystemManufacturer_Type=DisplayString
_AgentDeviceFileSystemManufacturer_Object=MibTableColumn
agentDeviceFileSystemManufacturer=_AgentDeviceFileSystemManufacturer_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,44,1,1,1,5),_AgentDeviceFileSystemManufacturer_Type())
agentDeviceFileSystemManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDeviceFileSystemManufacturer.setStatus(_A)
_AgentDeviceFileSystemSerialNumber_Type=DisplayString
_AgentDeviceFileSystemSerialNumber_Object=MibTableColumn
agentDeviceFileSystemSerialNumber=_AgentDeviceFileSystemSerialNumber_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,44,1,1,1,6),_AgentDeviceFileSystemSerialNumber_Type())
agentDeviceFileSystemSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDeviceFileSystemSerialNumber.setStatus(_A)
_AgentDeviceFileSystemVersion_Type=DisplayString
_AgentDeviceFileSystemVersion_Object=MibTableColumn
agentDeviceFileSystemVersion=_AgentDeviceFileSystemVersion_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,44,1,1,1,7),_AgentDeviceFileSystemVersion_Type())
agentDeviceFileSystemVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDeviceFileSystemVersion.setStatus(_A)
_AgentDeviceFileSystemProtocol_Type=DisplayString
_AgentDeviceFileSystemProtocol_Object=MibTableColumn
agentDeviceFileSystemProtocol=_AgentDeviceFileSystemProtocol_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,44,1,1,1,8),_AgentDeviceFileSystemProtocol_Type())
agentDeviceFileSystemProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDeviceFileSystemProtocol.setStatus(_A)
_AgentDeviceFileSystemClass_Type=DisplayString
_AgentDeviceFileSystemClass_Object=MibTableColumn
agentDeviceFileSystemClass=_AgentDeviceFileSystemClass_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,44,1,1,1,9),_AgentDeviceFileSystemClass_Type())
agentDeviceFileSystemClass.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDeviceFileSystemClass.setStatus(_A)
_AgentDeviceFileSystemSubclass_Type=DisplayString
_AgentDeviceFileSystemSubclass_Object=MibTableColumn
agentDeviceFileSystemSubclass=_AgentDeviceFileSystemSubclass_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,44,1,1,1,10),_AgentDeviceFileSystemSubclass_Type())
agentDeviceFileSystemSubclass.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDeviceFileSystemSubclass.setStatus(_A)
_AgentDeviceFileSystemTotalSize_Type=DisplayString
_AgentDeviceFileSystemTotalSize_Object=MibTableColumn
agentDeviceFileSystemTotalSize=_AgentDeviceFileSystemTotalSize_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,44,1,1,1,11),_AgentDeviceFileSystemTotalSize_Type())
agentDeviceFileSystemTotalSize.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDeviceFileSystemTotalSize.setStatus(_A)
_AgentDeviceFileSystemBytesUsed_Type=DisplayString
_AgentDeviceFileSystemBytesUsed_Object=MibTableColumn
agentDeviceFileSystemBytesUsed=_AgentDeviceFileSystemBytesUsed_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,44,1,1,1,12),_AgentDeviceFileSystemBytesUsed_Type())
agentDeviceFileSystemBytesUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDeviceFileSystemBytesUsed.setStatus(_A)
_AgentDeviceFileSystemBytesFree_Type=DisplayString
_AgentDeviceFileSystemBytesFree_Object=MibTableColumn
agentDeviceFileSystemBytesFree=_AgentDeviceFileSystemBytesFree_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,44,1,1,1,13),_AgentDeviceFileSystemBytesFree_Type())
agentDeviceFileSystemBytesFree.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDeviceFileSystemBytesFree.setStatus(_A)
class _AgentDeviceFileSystemUnmount_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),('unmount',1)))
_AgentDeviceFileSystemUnmount_Type.__name__=_C
_AgentDeviceFileSystemUnmount_Object=MibTableColumn
agentDeviceFileSystemUnmount=_AgentDeviceFileSystemUnmount_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,44,1,1,1,14),_AgentDeviceFileSystemUnmount_Type())
agentDeviceFileSystemUnmount.setMaxAccess('read-write')
if mibBuilder.loadTexts:agentDeviceFileSystemUnmount.setStatus(_A)
_AgentDeviceFileSystemContentTable_Object=MibTable
agentDeviceFileSystemContentTable=_AgentDeviceFileSystemContentTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,44,1,2))
if mibBuilder.loadTexts:agentDeviceFileSystemContentTable.setStatus(_A)
_AgentDeviceFileSystemContentEntry_Object=MibTableRow
agentDeviceFileSystemContentEntry=_AgentDeviceFileSystemContentEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,44,1,2,1))
agentDeviceFileSystemContentEntry.setIndexNames((0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:agentDeviceFileSystemContentEntry.setStatus(_A)
class _AgentDevFileSystemIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9))
_AgentDevFileSystemIndex_Type.__name__=_C
_AgentDevFileSystemIndex_Object=MibTableColumn
agentDevFileSystemIndex=_AgentDevFileSystemIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,44,1,2,1,1),_AgentDevFileSystemIndex_Type())
agentDevFileSystemIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDevFileSystemIndex.setStatus(_A)
_AgentDeviceFileSystemContentFileName_Type=DisplayString
_AgentDeviceFileSystemContentFileName_Object=MibTableColumn
agentDeviceFileSystemContentFileName=_AgentDeviceFileSystemContentFileName_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,44,1,2,1,2),_AgentDeviceFileSystemContentFileName_Type())
agentDeviceFileSystemContentFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDeviceFileSystemContentFileName.setStatus(_A)
_AgentDeviceFileSystemContentFileSize_Type=Unsigned32
_AgentDeviceFileSystemContentFileSize_Object=MibTableColumn
agentDeviceFileSystemContentFileSize=_AgentDeviceFileSystemContentFileSize_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,44,1,2,1,3),_AgentDeviceFileSystemContentFileSize_Type())
agentDeviceFileSystemContentFileSize.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDeviceFileSystemContentFileSize.setStatus(_A)
_AgentDeviceFileSystemContentFileModificationTime_Type=DateAndTime
_AgentDeviceFileSystemContentFileModificationTime_Object=MibTableColumn
agentDeviceFileSystemContentFileModificationTime=_AgentDeviceFileSystemContentFileModificationTime_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,44,1,2,1,4),_AgentDeviceFileSystemContentFileModificationTime_Type())
agentDeviceFileSystemContentFileModificationTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDeviceFileSystemContentFileModificationTime.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'fastpathDeviceFileSystem':fastpathDeviceFileSystem,'agentDeviceFileSystemGroup':agentDeviceFileSystemGroup,'agentDeviceFileSystemTable':agentDeviceFileSystemTable,'agentDeviceFileSystemEntry':agentDeviceFileSystemEntry,_E:agentDeviceFileSystemIndex,'agentDeviceFileSystemStatus':agentDeviceFileSystemStatus,'agentDeviceFileSystemVendorID':agentDeviceFileSystemVendorID,'agentDeviceFileSystemProductID':agentDeviceFileSystemProductID,'agentDeviceFileSystemManufacturer':agentDeviceFileSystemManufacturer,'agentDeviceFileSystemSerialNumber':agentDeviceFileSystemSerialNumber,'agentDeviceFileSystemVersion':agentDeviceFileSystemVersion,'agentDeviceFileSystemProtocol':agentDeviceFileSystemProtocol,'agentDeviceFileSystemClass':agentDeviceFileSystemClass,'agentDeviceFileSystemSubclass':agentDeviceFileSystemSubclass,'agentDeviceFileSystemTotalSize':agentDeviceFileSystemTotalSize,'agentDeviceFileSystemBytesUsed':agentDeviceFileSystemBytesUsed,'agentDeviceFileSystemBytesFree':agentDeviceFileSystemBytesFree,'agentDeviceFileSystemUnmount':agentDeviceFileSystemUnmount,'agentDeviceFileSystemContentTable':agentDeviceFileSystemContentTable,'agentDeviceFileSystemContentEntry':agentDeviceFileSystemContentEntry,_F:agentDevFileSystemIndex,_G:agentDeviceFileSystemContentFileName,'agentDeviceFileSystemContentFileSize':agentDeviceFileSystemContentFileSize,'agentDeviceFileSystemContentFileModificationTime':agentDeviceFileSystemContentFileModificationTime})