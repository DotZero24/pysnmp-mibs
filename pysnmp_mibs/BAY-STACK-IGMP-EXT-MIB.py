_M='bsIgmpExtMvrReceiversVlanId'
_L='bsIgmpExtMvrGroupRangeMask'
_K='bsIgmpExtMvrGroupRangeAddress'
_J='bsIgmpExtFilterRangeId'
_I='PortList'
_H='bsIgmpExtFilterProfileId'
_G='read-only'
_F='read-write'
_E='not-accessible'
_D='BAY-STACK-IGMP-EXT-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
PortList,VlanId=mibBuilder.importSymbols('Q-BRIDGE-MIB',_I,'VlanId')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackIgmpExtMib=ModuleIdentity((1,3,6,1,4,1,45,5,32))
if mibBuilder.loadTexts:bayStackIgmpExtMib.setRevisions(('2016-03-09 00:00','2015-12-21 00:00','2015-08-10 00:00','2009-10-26 00:00','2009-01-19 00:00','2008-11-19 00:00'))
_BsIgmpExtNotifications_ObjectIdentity=ObjectIdentity
bsIgmpExtNotifications=_BsIgmpExtNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,32,0))
_BsIgmpExtObjects_ObjectIdentity=ObjectIdentity
bsIgmpExtObjects=_BsIgmpExtObjects_ObjectIdentity((1,3,6,1,4,1,45,5,32,1))
_BsIgmpExtFilterProfileTable_Object=MibTable
bsIgmpExtFilterProfileTable=_BsIgmpExtFilterProfileTable_Object((1,3,6,1,4,1,45,5,32,1,1))
if mibBuilder.loadTexts:bsIgmpExtFilterProfileTable.setStatus(_A)
_BsIgmpExtFilterProfileEntry_Object=MibTableRow
bsIgmpExtFilterProfileEntry=_BsIgmpExtFilterProfileEntry_Object((1,3,6,1,4,1,45,5,32,1,1,1))
bsIgmpExtFilterProfileEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:bsIgmpExtFilterProfileEntry.setStatus(_A)
class _BsIgmpExtFilterProfileId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BsIgmpExtFilterProfileId_Type.__name__=_C
_BsIgmpExtFilterProfileId_Object=MibTableColumn
bsIgmpExtFilterProfileId=_BsIgmpExtFilterProfileId_Object((1,3,6,1,4,1,45,5,32,1,1,1,1),_BsIgmpExtFilterProfileId_Type())
bsIgmpExtFilterProfileId.setMaxAccess(_E)
if mibBuilder.loadTexts:bsIgmpExtFilterProfileId.setStatus(_A)
class _BsIgmpExtFilterProfileType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('deny',2)))
_BsIgmpExtFilterProfileType_Type.__name__=_C
_BsIgmpExtFilterProfileType_Object=MibTableColumn
bsIgmpExtFilterProfileType=_BsIgmpExtFilterProfileType_Object((1,3,6,1,4,1,45,5,32,1,1,1,2),_BsIgmpExtFilterProfileType_Type())
bsIgmpExtFilterProfileType.setMaxAccess(_B)
if mibBuilder.loadTexts:bsIgmpExtFilterProfileType.setStatus(_A)
class _BsIgmpExtFilterProfilePortList_Type(PortList):defaultHexValue=''
_BsIgmpExtFilterProfilePortList_Type.__name__=_I
_BsIgmpExtFilterProfilePortList_Object=MibTableColumn
bsIgmpExtFilterProfilePortList=_BsIgmpExtFilterProfilePortList_Object((1,3,6,1,4,1,45,5,32,1,1,1,3),_BsIgmpExtFilterProfilePortList_Type())
bsIgmpExtFilterProfilePortList.setMaxAccess(_B)
if mibBuilder.loadTexts:bsIgmpExtFilterProfilePortList.setStatus(_A)
_BsIgmpExtFilterProfileRowStatus_Type=RowStatus
_BsIgmpExtFilterProfileRowStatus_Object=MibTableColumn
bsIgmpExtFilterProfileRowStatus=_BsIgmpExtFilterProfileRowStatus_Object((1,3,6,1,4,1,45,5,32,1,1,1,4),_BsIgmpExtFilterProfileRowStatus_Type())
bsIgmpExtFilterProfileRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:bsIgmpExtFilterProfileRowStatus.setStatus(_A)
_BsIgmpExtFilterProfileDroppedPackets_Type=Counter32
_BsIgmpExtFilterProfileDroppedPackets_Object=MibTableColumn
bsIgmpExtFilterProfileDroppedPackets=_BsIgmpExtFilterProfileDroppedPackets_Object((1,3,6,1,4,1,45,5,32,1,1,1,5),_BsIgmpExtFilterProfileDroppedPackets_Type())
bsIgmpExtFilterProfileDroppedPackets.setMaxAccess(_G)
if mibBuilder.loadTexts:bsIgmpExtFilterProfileDroppedPackets.setStatus(_A)
_BsIgmpExtFilterRangeTable_Object=MibTable
bsIgmpExtFilterRangeTable=_BsIgmpExtFilterRangeTable_Object((1,3,6,1,4,1,45,5,32,1,2))
if mibBuilder.loadTexts:bsIgmpExtFilterRangeTable.setStatus(_A)
_BsIgmpExtFilterRangeEntry_Object=MibTableRow
bsIgmpExtFilterRangeEntry=_BsIgmpExtFilterRangeEntry_Object((1,3,6,1,4,1,45,5,32,1,2,1))
bsIgmpExtFilterRangeEntry.setIndexNames((0,_D,_H),(0,_D,_J))
if mibBuilder.loadTexts:bsIgmpExtFilterRangeEntry.setStatus(_A)
class _BsIgmpExtFilterRangeId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BsIgmpExtFilterRangeId_Type.__name__=_C
_BsIgmpExtFilterRangeId_Object=MibTableColumn
bsIgmpExtFilterRangeId=_BsIgmpExtFilterRangeId_Object((1,3,6,1,4,1,45,5,32,1,2,1,1),_BsIgmpExtFilterRangeId_Type())
bsIgmpExtFilterRangeId.setMaxAccess(_E)
if mibBuilder.loadTexts:bsIgmpExtFilterRangeId.setStatus(_A)
_BsIgmpExtFilterRangeAddressType_Type=InetAddressType
_BsIgmpExtFilterRangeAddressType_Object=MibTableColumn
bsIgmpExtFilterRangeAddressType=_BsIgmpExtFilterRangeAddressType_Object((1,3,6,1,4,1,45,5,32,1,2,1,2),_BsIgmpExtFilterRangeAddressType_Type())
bsIgmpExtFilterRangeAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:bsIgmpExtFilterRangeAddressType.setStatus(_A)
_BsIgmpExtFilterRangeAddressStart_Type=InetAddress
_BsIgmpExtFilterRangeAddressStart_Object=MibTableColumn
bsIgmpExtFilterRangeAddressStart=_BsIgmpExtFilterRangeAddressStart_Object((1,3,6,1,4,1,45,5,32,1,2,1,3),_BsIgmpExtFilterRangeAddressStart_Type())
bsIgmpExtFilterRangeAddressStart.setMaxAccess(_B)
if mibBuilder.loadTexts:bsIgmpExtFilterRangeAddressStart.setStatus(_A)
_BsIgmpExtFilterRangeAddressEnd_Type=InetAddress
_BsIgmpExtFilterRangeAddressEnd_Object=MibTableColumn
bsIgmpExtFilterRangeAddressEnd=_BsIgmpExtFilterRangeAddressEnd_Object((1,3,6,1,4,1,45,5,32,1,2,1,4),_BsIgmpExtFilterRangeAddressEnd_Type())
bsIgmpExtFilterRangeAddressEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:bsIgmpExtFilterRangeAddressEnd.setStatus(_A)
_BsIgmpExtFilterRangeRowStatus_Type=RowStatus
_BsIgmpExtFilterRangeRowStatus_Object=MibTableColumn
bsIgmpExtFilterRangeRowStatus=_BsIgmpExtFilterRangeRowStatus_Object((1,3,6,1,4,1,45,5,32,1,2,1,5),_BsIgmpExtFilterRangeRowStatus_Type())
bsIgmpExtFilterRangeRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:bsIgmpExtFilterRangeRowStatus.setStatus(_A)
_BsIgmpExtFilterProfileScalars_ObjectIdentity=ObjectIdentity
bsIgmpExtFilterProfileScalars=_BsIgmpExtFilterProfileScalars_ObjectIdentity((1,3,6,1,4,1,45,5,32,1,3))
class _BsIgmpExtFilterProfileClearStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BsIgmpExtFilterProfileClearStats_Type.__name__=_C
_BsIgmpExtFilterProfileClearStats_Object=MibScalar
bsIgmpExtFilterProfileClearStats=_BsIgmpExtFilterProfileClearStats_Object((1,3,6,1,4,1,45,5,32,1,3,1),_BsIgmpExtFilterProfileClearStats_Type())
bsIgmpExtFilterProfileClearStats.setMaxAccess(_F)
if mibBuilder.loadTexts:bsIgmpExtFilterProfileClearStats.setStatus(_A)
_BsIgmpExtScalars_ObjectIdentity=ObjectIdentity
bsIgmpExtScalars=_BsIgmpExtScalars_ObjectIdentity((1,3,6,1,4,1,45,5,32,1,4))
_BsIgmpExtAvailableHardwareResources_Type=Gauge32
_BsIgmpExtAvailableHardwareResources_Object=MibScalar
bsIgmpExtAvailableHardwareResources=_BsIgmpExtAvailableHardwareResources_Object((1,3,6,1,4,1,45,5,32,1,4,1),_BsIgmpExtAvailableHardwareResources_Type())
bsIgmpExtAvailableHardwareResources.setMaxAccess(_G)
if mibBuilder.loadTexts:bsIgmpExtAvailableHardwareResources.setStatus(_A)
class _BsIgmpExtHardwareCompatibilityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ers5510',1),('nonErs5510',2)))
_BsIgmpExtHardwareCompatibilityMode_Type.__name__=_C
_BsIgmpExtHardwareCompatibilityMode_Object=MibScalar
bsIgmpExtHardwareCompatibilityMode=_BsIgmpExtHardwareCompatibilityMode_Object((1,3,6,1,4,1,45,5,32,1,4,2),_BsIgmpExtHardwareCompatibilityMode_Type())
bsIgmpExtHardwareCompatibilityMode.setMaxAccess(_F)
if mibBuilder.loadTexts:bsIgmpExtHardwareCompatibilityMode.setStatus(_A)
class _BsIgmpExtStreamFlushAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('flushAllGroup',2),('flushAllStream',3),('flushAllMrouter',4),('flushAll',5)))
_BsIgmpExtStreamFlushAll_Type.__name__=_C
_BsIgmpExtStreamFlushAll_Object=MibScalar
bsIgmpExtStreamFlushAll=_BsIgmpExtStreamFlushAll_Object((1,3,6,1,4,1,45,5,32,1,4,3),_BsIgmpExtStreamFlushAll_Type())
bsIgmpExtStreamFlushAll.setMaxAccess(_F)
if mibBuilder.loadTexts:bsIgmpExtStreamFlushAll.setStatus(_A)
_BsIgmpExtStreamCount_Type=Gauge32
_BsIgmpExtStreamCount_Object=MibScalar
bsIgmpExtStreamCount=_BsIgmpExtStreamCount_Object((1,3,6,1,4,1,45,5,32,1,4,4),_BsIgmpExtStreamCount_Type())
bsIgmpExtStreamCount.setMaxAccess(_G)
if mibBuilder.loadTexts:bsIgmpExtStreamCount.setStatus(_A)
_BsIgmpExtGroupCount_Type=Gauge32
_BsIgmpExtGroupCount_Object=MibScalar
bsIgmpExtGroupCount=_BsIgmpExtGroupCount_Object((1,3,6,1,4,1,45,5,32,1,4,5),_BsIgmpExtGroupCount_Type())
bsIgmpExtGroupCount.setMaxAccess(_G)
if mibBuilder.loadTexts:bsIgmpExtGroupCount.setStatus(_A)
_BsIgmpExtMvrGlobal_ObjectIdentity=ObjectIdentity
bsIgmpExtMvrGlobal=_BsIgmpExtMvrGlobal_ObjectIdentity((1,3,6,1,4,1,45,5,32,1,5))
_BsIgmpExtMvrGlobalEnable_Type=TruthValue
_BsIgmpExtMvrGlobalEnable_Object=MibScalar
bsIgmpExtMvrGlobalEnable=_BsIgmpExtMvrGlobalEnable_Object((1,3,6,1,4,1,45,5,32,1,5,1),_BsIgmpExtMvrGlobalEnable_Type())
bsIgmpExtMvrGlobalEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:bsIgmpExtMvrGlobalEnable.setStatus(_A)
_BsIgmpExtMvrGlobalSourceVlan_Type=VlanId
_BsIgmpExtMvrGlobalSourceVlan_Object=MibScalar
bsIgmpExtMvrGlobalSourceVlan=_BsIgmpExtMvrGlobalSourceVlan_Object((1,3,6,1,4,1,45,5,32,1,5,2),_BsIgmpExtMvrGlobalSourceVlan_Type())
bsIgmpExtMvrGlobalSourceVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:bsIgmpExtMvrGlobalSourceVlan.setStatus(_A)
_BsIgmpExtMvrGroupRangeTable_Object=MibTable
bsIgmpExtMvrGroupRangeTable=_BsIgmpExtMvrGroupRangeTable_Object((1,3,6,1,4,1,45,5,32,1,6))
if mibBuilder.loadTexts:bsIgmpExtMvrGroupRangeTable.setStatus(_A)
_BsIgmpExtMvrGroupRangeEntry_Object=MibTableRow
bsIgmpExtMvrGroupRangeEntry=_BsIgmpExtMvrGroupRangeEntry_Object((1,3,6,1,4,1,45,5,32,1,6,1))
bsIgmpExtMvrGroupRangeEntry.setIndexNames((0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:bsIgmpExtMvrGroupRangeEntry.setStatus(_A)
_BsIgmpExtMvrGroupRangeAddress_Type=IpAddress
_BsIgmpExtMvrGroupRangeAddress_Object=MibTableColumn
bsIgmpExtMvrGroupRangeAddress=_BsIgmpExtMvrGroupRangeAddress_Object((1,3,6,1,4,1,45,5,32,1,6,1,1),_BsIgmpExtMvrGroupRangeAddress_Type())
bsIgmpExtMvrGroupRangeAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:bsIgmpExtMvrGroupRangeAddress.setStatus(_A)
_BsIgmpExtMvrGroupRangeMask_Type=IpAddress
_BsIgmpExtMvrGroupRangeMask_Object=MibTableColumn
bsIgmpExtMvrGroupRangeMask=_BsIgmpExtMvrGroupRangeMask_Object((1,3,6,1,4,1,45,5,32,1,6,1,2),_BsIgmpExtMvrGroupRangeMask_Type())
bsIgmpExtMvrGroupRangeMask.setMaxAccess(_E)
if mibBuilder.loadTexts:bsIgmpExtMvrGroupRangeMask.setStatus(_A)
_BsIgmpExtMvrGroupRangeRowStatus_Type=RowStatus
_BsIgmpExtMvrGroupRangeRowStatus_Object=MibTableColumn
bsIgmpExtMvrGroupRangeRowStatus=_BsIgmpExtMvrGroupRangeRowStatus_Object((1,3,6,1,4,1,45,5,32,1,6,1,3),_BsIgmpExtMvrGroupRangeRowStatus_Type())
bsIgmpExtMvrGroupRangeRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:bsIgmpExtMvrGroupRangeRowStatus.setStatus(_A)
_BsIgmpExtMvrReceiversTable_Object=MibTable
bsIgmpExtMvrReceiversTable=_BsIgmpExtMvrReceiversTable_Object((1,3,6,1,4,1,45,5,32,1,7))
if mibBuilder.loadTexts:bsIgmpExtMvrReceiversTable.setStatus(_A)
_BsIgmpExtMvrReceiversEntry_Object=MibTableRow
bsIgmpExtMvrReceiversEntry=_BsIgmpExtMvrReceiversEntry_Object((1,3,6,1,4,1,45,5,32,1,7,1))
bsIgmpExtMvrReceiversEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:bsIgmpExtMvrReceiversEntry.setStatus(_A)
_BsIgmpExtMvrReceiversVlanId_Type=VlanId
_BsIgmpExtMvrReceiversVlanId_Object=MibTableColumn
bsIgmpExtMvrReceiversVlanId=_BsIgmpExtMvrReceiversVlanId_Object((1,3,6,1,4,1,45,5,32,1,7,1,1),_BsIgmpExtMvrReceiversVlanId_Type())
bsIgmpExtMvrReceiversVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:bsIgmpExtMvrReceiversVlanId.setStatus(_A)
_BsIgmpExtMvrReceiversRowStatus_Type=RowStatus
_BsIgmpExtMvrReceiversRowStatus_Object=MibTableColumn
bsIgmpExtMvrReceiversRowStatus=_BsIgmpExtMvrReceiversRowStatus_Object((1,3,6,1,4,1,45,5,32,1,7,1,2),_BsIgmpExtMvrReceiversRowStatus_Type())
bsIgmpExtMvrReceiversRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:bsIgmpExtMvrReceiversRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'bayStackIgmpExtMib':bayStackIgmpExtMib,'bsIgmpExtNotifications':bsIgmpExtNotifications,'bsIgmpExtObjects':bsIgmpExtObjects,'bsIgmpExtFilterProfileTable':bsIgmpExtFilterProfileTable,'bsIgmpExtFilterProfileEntry':bsIgmpExtFilterProfileEntry,_H:bsIgmpExtFilterProfileId,'bsIgmpExtFilterProfileType':bsIgmpExtFilterProfileType,'bsIgmpExtFilterProfilePortList':bsIgmpExtFilterProfilePortList,'bsIgmpExtFilterProfileRowStatus':bsIgmpExtFilterProfileRowStatus,'bsIgmpExtFilterProfileDroppedPackets':bsIgmpExtFilterProfileDroppedPackets,'bsIgmpExtFilterRangeTable':bsIgmpExtFilterRangeTable,'bsIgmpExtFilterRangeEntry':bsIgmpExtFilterRangeEntry,_J:bsIgmpExtFilterRangeId,'bsIgmpExtFilterRangeAddressType':bsIgmpExtFilterRangeAddressType,'bsIgmpExtFilterRangeAddressStart':bsIgmpExtFilterRangeAddressStart,'bsIgmpExtFilterRangeAddressEnd':bsIgmpExtFilterRangeAddressEnd,'bsIgmpExtFilterRangeRowStatus':bsIgmpExtFilterRangeRowStatus,'bsIgmpExtFilterProfileScalars':bsIgmpExtFilterProfileScalars,'bsIgmpExtFilterProfileClearStats':bsIgmpExtFilterProfileClearStats,'bsIgmpExtScalars':bsIgmpExtScalars,'bsIgmpExtAvailableHardwareResources':bsIgmpExtAvailableHardwareResources,'bsIgmpExtHardwareCompatibilityMode':bsIgmpExtHardwareCompatibilityMode,'bsIgmpExtStreamFlushAll':bsIgmpExtStreamFlushAll,'bsIgmpExtStreamCount':bsIgmpExtStreamCount,'bsIgmpExtGroupCount':bsIgmpExtGroupCount,'bsIgmpExtMvrGlobal':bsIgmpExtMvrGlobal,'bsIgmpExtMvrGlobalEnable':bsIgmpExtMvrGlobalEnable,'bsIgmpExtMvrGlobalSourceVlan':bsIgmpExtMvrGlobalSourceVlan,'bsIgmpExtMvrGroupRangeTable':bsIgmpExtMvrGroupRangeTable,'bsIgmpExtMvrGroupRangeEntry':bsIgmpExtMvrGroupRangeEntry,_K:bsIgmpExtMvrGroupRangeAddress,_L:bsIgmpExtMvrGroupRangeMask,'bsIgmpExtMvrGroupRangeRowStatus':bsIgmpExtMvrGroupRangeRowStatus,'bsIgmpExtMvrReceiversTable':bsIgmpExtMvrReceiversTable,'bsIgmpExtMvrReceiversEntry':bsIgmpExtMvrReceiversEntry,_M:bsIgmpExtMvrReceiversVlanId,'bsIgmpExtMvrReceiversRowStatus':bsIgmpExtMvrReceiversRowStatus})