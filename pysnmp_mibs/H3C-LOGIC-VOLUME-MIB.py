_R='h3cTISessionId'
_Q='nonexclusive'
_P='h3cTargetIpAddress'
_O='h3cTargetIpAddrType'
_N='h3cLvRaidUuid'
_M='H3cStorageEnableState'
_L='h3cInitiatorId'
_K='h3cSanClientId'
_J='MB'
_I='h3cLvIndex'
_H='h3cTargetId'
_G='not-accessible'
_F='OctetString'
_E='Integer32'
_D='H3C-LOGIC-VOLUME-MIB'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols('ENTITY-MIB','entPhysicalIndex')
H3cLvIDType,H3cRaidIDType,H3cSessionIDType,H3cStorageActionType,H3cStorageEnableState,H3cStorageLedStateType,H3cWwpnListType,h3cStorageRef=mibBuilder.importSymbols('H3C-STORAGE-REF-MIB','H3cLvIDType','H3cRaidIDType','H3cSessionIDType','H3cStorageActionType',_M,'H3cStorageLedStateType','H3cWwpnListType','h3cStorageRef')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
h3cLogicVolume=ModuleIdentity((1,3,6,1,4,1,2011,10,10,5))
_H3cLvMibObjects_ObjectIdentity=ObjectIdentity
h3cLvMibObjects=_H3cLvMibObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,10,5,1))
_H3cLogicResourceCapacityObject_ObjectIdentity=ObjectIdentity
h3cLogicResourceCapacityObject=_H3cLogicResourceCapacityObject_ObjectIdentity((1,3,6,1,4,1,2011,10,10,5,1,1))
_H3cLvCount_Type=Integer32
_H3cLvCount_Object=MibScalar
h3cLvCount=_H3cLvCount_Object((1,3,6,1,4,1,2011,10,10,5,1,1,1),_H3cLvCount_Type())
h3cLvCount.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cLvCount.setStatus(_A)
_H3cLvMaxSize_Type=Integer32
_H3cLvMaxSize_Object=MibScalar
h3cLvMaxSize=_H3cLvMaxSize_Object((1,3,6,1,4,1,2011,10,10,5,1,1,2),_H3cLvMaxSize_Type())
h3cLvMaxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cLvMaxSize.setStatus(_A)
if mibBuilder.loadTexts:h3cLvMaxSize.setUnits('TB')
_H3cTargetCount_Type=Integer32
_H3cTargetCount_Object=MibScalar
h3cTargetCount=_H3cTargetCount_Object((1,3,6,1,4,1,2011,10,10,5,1,1,3),_H3cTargetCount_Type())
h3cTargetCount.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTargetCount.setStatus(_A)
_H3cInitiatorCount_Type=Integer32
_H3cInitiatorCount_Object=MibScalar
h3cInitiatorCount=_H3cInitiatorCount_Object((1,3,6,1,4,1,2011,10,10,5,1,1,4),_H3cInitiatorCount_Type())
h3cInitiatorCount.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cInitiatorCount.setStatus(_A)
_H3cSanClientCount_Type=Integer32
_H3cSanClientCount_Object=MibScalar
h3cSanClientCount=_H3cSanClientCount_Object((1,3,6,1,4,1,2011,10,10,5,1,1,5),_H3cSanClientCount_Type())
h3cSanClientCount.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSanClientCount.setStatus(_A)
_H3cLogicVolumeResource_ObjectIdentity=ObjectIdentity
h3cLogicVolumeResource=_H3cLogicVolumeResource_ObjectIdentity((1,3,6,1,4,1,2011,10,10,5,1,2))
_H3cLvCreateIndex_Type=H3cLvIDType
_H3cLvCreateIndex_Object=MibScalar
h3cLvCreateIndex=_H3cLvCreateIndex_Object((1,3,6,1,4,1,2011,10,10,5,1,2,1),_H3cLvCreateIndex_Type())
h3cLvCreateIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cLvCreateIndex.setStatus(_A)
_H3cLvTable_Object=MibTable
h3cLvTable=_H3cLvTable_Object((1,3,6,1,4,1,2011,10,10,5,1,2,2))
if mibBuilder.loadTexts:h3cLvTable.setStatus(_A)
_H3cLvEntry_Object=MibTableRow
h3cLvEntry=_H3cLvEntry_Object((1,3,6,1,4,1,2011,10,10,5,1,2,2,1))
h3cLvEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:h3cLvEntry.setStatus(_A)
_H3cLvIndex_Type=H3cLvIDType
_H3cLvIndex_Object=MibTableColumn
h3cLvIndex=_H3cLvIndex_Object((1,3,6,1,4,1,2011,10,10,5,1,2,2,1,1),_H3cLvIndex_Type())
h3cLvIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cLvIndex.setStatus(_A)
class _H3cLvName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_H3cLvName_Type.__name__=_F
_H3cLvName_Object=MibTableColumn
h3cLvName=_H3cLvName_Object((1,3,6,1,4,1,2011,10,10,5,1,2,2,1,2),_H3cLvName_Type())
h3cLvName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLvName.setStatus(_A)
_H3cLvTotalSize_Type=Integer32
_H3cLvTotalSize_Object=MibTableColumn
h3cLvTotalSize=_H3cLvTotalSize_Object((1,3,6,1,4,1,2011,10,10,5,1,2,2,1,3),_H3cLvTotalSize_Type())
h3cLvTotalSize.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cLvTotalSize.setStatus(_A)
if mibBuilder.loadTexts:h3cLvTotalSize.setUnits(_J)
_H3cLvCreateRaidUuid_Type=H3cRaidIDType
_H3cLvCreateRaidUuid_Object=MibTableColumn
h3cLvCreateRaidUuid=_H3cLvCreateRaidUuid_Object((1,3,6,1,4,1,2011,10,10,5,1,2,2,1,4),_H3cLvCreateRaidUuid_Type())
h3cLvCreateRaidUuid.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLvCreateRaidUuid.setStatus(_A)
_H3cLvCreateRaidSize_Type=Integer32
_H3cLvCreateRaidSize_Object=MibTableColumn
h3cLvCreateRaidSize=_H3cLvCreateRaidSize_Object((1,3,6,1,4,1,2011,10,10,5,1,2,2,1,5),_H3cLvCreateRaidSize_Type())
h3cLvCreateRaidSize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLvCreateRaidSize.setStatus(_A)
if mibBuilder.loadTexts:h3cLvCreateRaidSize.setUnits(_J)
_H3cLvSedInquiryStringKeep_Type=TruthValue
_H3cLvSedInquiryStringKeep_Object=MibTableColumn
h3cLvSedInquiryStringKeep=_H3cLvSedInquiryStringKeep_Object((1,3,6,1,4,1,2011,10,10,5,1,2,2,1,6),_H3cLvSedInquiryStringKeep_Type())
h3cLvSedInquiryStringKeep.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLvSedInquiryStringKeep.setStatus(_A)
_H3cLvSedRaidUuid_Type=H3cRaidIDType
_H3cLvSedRaidUuid_Object=MibTableColumn
h3cLvSedRaidUuid=_H3cLvSedRaidUuid_Object((1,3,6,1,4,1,2011,10,10,5,1,2,2,1,7),_H3cLvSedRaidUuid_Type())
h3cLvSedRaidUuid.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cLvSedRaidUuid.setStatus(_A)
class _H3cLvState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('usable',1),('unusable',2),('conflict',3)))
_H3cLvState_Type.__name__=_E
_H3cLvState_Object=MibTableColumn
h3cLvState=_H3cLvState_Object((1,3,6,1,4,1,2011,10,10,5,1,2,2,1,8),_H3cLvState_Type())
h3cLvState.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cLvState.setStatus(_A)
class _H3cLvAssigned_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('use',1),('unused',2)))
_H3cLvAssigned_Type.__name__=_E
_H3cLvAssigned_Object=MibTableColumn
h3cLvAssigned=_H3cLvAssigned_Object((1,3,6,1,4,1,2011,10,10,5,1,2,2,1,9),_H3cLvAssigned_Type())
h3cLvAssigned.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cLvAssigned.setStatus(_A)
class _H3cLvType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('virtual',1),('direct',2),('serviceEnabled',3)))
_H3cLvType_Type.__name__=_E
_H3cLvType_Object=MibTableColumn
h3cLvType=_H3cLvType_Object((1,3,6,1,4,1,2011,10,10,5,1,2,2,1,10),_H3cLvType_Type())
h3cLvType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cLvType.setStatus(_A)
_H3cLvExtendTimes_Type=Integer32
_H3cLvExtendTimes_Object=MibTableColumn
h3cLvExtendTimes=_H3cLvExtendTimes_Object((1,3,6,1,4,1,2011,10,10,5,1,2,2,1,11),_H3cLvExtendTimes_Type())
h3cLvExtendTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cLvExtendTimes.setStatus(_A)
_H3cLvRowStatus_Type=RowStatus
_H3cLvRowStatus_Object=MibTableColumn
h3cLvRowStatus=_H3cLvRowStatus_Object((1,3,6,1,4,1,2011,10,10,5,1,2,2,1,12),_H3cLvRowStatus_Type())
h3cLvRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLvRowStatus.setStatus(_A)
_H3cLvExtTable_Object=MibTable
h3cLvExtTable=_H3cLvExtTable_Object((1,3,6,1,4,1,2011,10,10,5,1,3))
if mibBuilder.loadTexts:h3cLvExtTable.setStatus(_A)
_H3cLvExtEntry_Object=MibTableRow
h3cLvExtEntry=_H3cLvExtEntry_Object((1,3,6,1,4,1,2011,10,10,5,1,3,1))
h3cLvExtEntry.setIndexNames((0,_D,_I),(0,_D,_N))
if mibBuilder.loadTexts:h3cLvExtEntry.setStatus(_A)
_H3cLvRaidUuid_Type=H3cRaidIDType
_H3cLvRaidUuid_Object=MibTableColumn
h3cLvRaidUuid=_H3cLvRaidUuid_Object((1,3,6,1,4,1,2011,10,10,5,1,3,1,1),_H3cLvRaidUuid_Type())
h3cLvRaidUuid.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cLvRaidUuid.setStatus(_A)
class _H3cLvExtSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cLvExtSize_Type.__name__=_E
_H3cLvExtSize_Object=MibTableColumn
h3cLvExtSize=_H3cLvExtSize_Object((1,3,6,1,4,1,2011,10,10,5,1,3,1,2),_H3cLvExtSize_Type())
h3cLvExtSize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLvExtSize.setStatus(_A)
if mibBuilder.loadTexts:h3cLvExtSize.setUnits(_J)
_H3cLvRaidSize_Type=Integer32
_H3cLvRaidSize_Object=MibTableColumn
h3cLvRaidSize=_H3cLvRaidSize_Object((1,3,6,1,4,1,2011,10,10,5,1,3,1,3),_H3cLvRaidSize_Type())
h3cLvRaidSize.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cLvRaidSize.setStatus(_A)
if mibBuilder.loadTexts:h3cLvRaidSize.setUnits(_J)
_H3cLvExtRowStatus_Type=RowStatus
_H3cLvExtRowStatus_Object=MibTableColumn
h3cLvExtRowStatus=_H3cLvExtRowStatus_Object((1,3,6,1,4,1,2011,10,10,5,1,3,1,4),_H3cLvExtRowStatus_Type())
h3cLvExtRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cLvExtRowStatus.setStatus(_A)
_H3cTargetResource_ObjectIdentity=ObjectIdentity
h3cTargetResource=_H3cTargetResource_ObjectIdentity((1,3,6,1,4,1,2011,10,10,5,1,4))
_H3cTargetCreateIndex_Type=Integer32
_H3cTargetCreateIndex_Object=MibScalar
h3cTargetCreateIndex=_H3cTargetCreateIndex_Object((1,3,6,1,4,1,2011,10,10,5,1,4,1),_H3cTargetCreateIndex_Type())
h3cTargetCreateIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTargetCreateIndex.setStatus(_A)
_H3cTargetTable_Object=MibTable
h3cTargetTable=_H3cTargetTable_Object((1,3,6,1,4,1,2011,10,10,5,1,4,2))
if mibBuilder.loadTexts:h3cTargetTable.setStatus(_A)
_H3cTargetEntry_Object=MibTableRow
h3cTargetEntry=_H3cTargetEntry_Object((1,3,6,1,4,1,2011,10,10,5,1,4,2,1))
h3cTargetEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:h3cTargetEntry.setStatus(_A)
_H3cTargetId_Type=Integer32
_H3cTargetId_Object=MibTableColumn
h3cTargetId=_H3cTargetId_Object((1,3,6,1,4,1,2011,10,10,5,1,4,2,1,1),_H3cTargetId_Type())
h3cTargetId.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cTargetId.setStatus(_A)
class _H3cTargetName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,223))
_H3cTargetName_Type.__name__=_F
_H3cTargetName_Object=MibTableColumn
h3cTargetName=_H3cTargetName_Object((1,3,6,1,4,1,2011,10,10,5,1,4,2,1,2),_H3cTargetName_Type())
h3cTargetName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTargetName.setStatus(_A)
class _H3cTargetMinLun_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_H3cTargetMinLun_Type.__name__=_E
_H3cTargetMinLun_Object=MibTableColumn
h3cTargetMinLun=_H3cTargetMinLun_Object((1,3,6,1,4,1,2011,10,10,5,1,4,2,1,3),_H3cTargetMinLun_Type())
h3cTargetMinLun.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTargetMinLun.setStatus(_A)
_H3cTargetRowStatus_Type=RowStatus
_H3cTargetRowStatus_Object=MibTableColumn
h3cTargetRowStatus=_H3cTargetRowStatus_Object((1,3,6,1,4,1,2011,10,10,5,1,4,2,1,4),_H3cTargetRowStatus_Type())
h3cTargetRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTargetRowStatus.setStatus(_A)
_H3cTargetAddressTable_Object=MibTable
h3cTargetAddressTable=_H3cTargetAddressTable_Object((1,3,6,1,4,1,2011,10,10,5,1,5))
if mibBuilder.loadTexts:h3cTargetAddressTable.setStatus(_A)
_H3cTargetAddressEntry_Object=MibTableRow
h3cTargetAddressEntry=_H3cTargetAddressEntry_Object((1,3,6,1,4,1,2011,10,10,5,1,5,1))
h3cTargetAddressEntry.setIndexNames((0,_D,_H),(0,_D,_O),(0,_D,_P))
if mibBuilder.loadTexts:h3cTargetAddressEntry.setStatus(_A)
_H3cTargetIpAddress_Type=InetAddress
_H3cTargetIpAddress_Object=MibTableColumn
h3cTargetIpAddress=_H3cTargetIpAddress_Object((1,3,6,1,4,1,2011,10,10,5,1,5,1,1),_H3cTargetIpAddress_Type())
h3cTargetIpAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cTargetIpAddress.setStatus(_A)
_H3cTargetIpAddrType_Type=InetAddressType
_H3cTargetIpAddrType_Object=MibTableColumn
h3cTargetIpAddrType=_H3cTargetIpAddrType_Object((1,3,6,1,4,1,2011,10,10,5,1,5,1,2),_H3cTargetIpAddrType_Type())
h3cTargetIpAddrType.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cTargetIpAddrType.setStatus(_A)
_H3cTargetIpRowStatus_Type=RowStatus
_H3cTargetIpRowStatus_Object=MibTableColumn
h3cTargetIpRowStatus=_H3cTargetIpRowStatus_Object((1,3,6,1,4,1,2011,10,10,5,1,5,1,3),_H3cTargetIpRowStatus_Type())
h3cTargetIpRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTargetIpRowStatus.setStatus(_A)
_H3cTargetLvAssignTable_Object=MibTable
h3cTargetLvAssignTable=_H3cTargetLvAssignTable_Object((1,3,6,1,4,1,2011,10,10,5,1,6))
if mibBuilder.loadTexts:h3cTargetLvAssignTable.setStatus(_A)
_H3cTargetLvAssignEntry_Object=MibTableRow
h3cTargetLvAssignEntry=_H3cTargetLvAssignEntry_Object((1,3,6,1,4,1,2011,10,10,5,1,6,1))
h3cTargetLvAssignEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:h3cTargetLvAssignEntry.setStatus(_A)
class _H3cTargetLvLun_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_H3cTargetLvLun_Type.__name__=_E
_H3cTargetLvLun_Object=MibTableColumn
h3cTargetLvLun=_H3cTargetLvLun_Object((1,3,6,1,4,1,2011,10,10,5,1,6,1,1),_H3cTargetLvLun_Type())
h3cTargetLvLun.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTargetLvLun.setStatus(_A)
_H3cTargetLvRowStatus_Type=RowStatus
_H3cTargetLvRowStatus_Object=MibTableColumn
h3cTargetLvRowStatus=_H3cTargetLvRowStatus_Object((1,3,6,1,4,1,2011,10,10,5,1,6,1,2),_H3cTargetLvRowStatus_Type())
h3cTargetLvRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTargetLvRowStatus.setStatus(_A)
_H3cInitiatorResource_ObjectIdentity=ObjectIdentity
h3cInitiatorResource=_H3cInitiatorResource_ObjectIdentity((1,3,6,1,4,1,2011,10,10,5,1,7))
_H3cInitiatorCreateIndex_Type=Integer32
_H3cInitiatorCreateIndex_Object=MibScalar
h3cInitiatorCreateIndex=_H3cInitiatorCreateIndex_Object((1,3,6,1,4,1,2011,10,10,5,1,7,1),_H3cInitiatorCreateIndex_Type())
h3cInitiatorCreateIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cInitiatorCreateIndex.setStatus(_A)
_H3cInitiatorTable_Object=MibTable
h3cInitiatorTable=_H3cInitiatorTable_Object((1,3,6,1,4,1,2011,10,10,5,1,7,2))
if mibBuilder.loadTexts:h3cInitiatorTable.setStatus(_A)
_H3cInitiatorEntry_Object=MibTableRow
h3cInitiatorEntry=_H3cInitiatorEntry_Object((1,3,6,1,4,1,2011,10,10,5,1,7,2,1))
h3cInitiatorEntry.setIndexNames((0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:h3cInitiatorEntry.setStatus(_A)
_H3cInitiatorId_Type=Integer32
_H3cInitiatorId_Object=MibTableColumn
h3cInitiatorId=_H3cInitiatorId_Object((1,3,6,1,4,1,2011,10,10,5,1,7,2,1,1),_H3cInitiatorId_Type())
h3cInitiatorId.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cInitiatorId.setStatus(_A)
class _H3cInitiatorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,223))
_H3cInitiatorName_Type.__name__=_F
_H3cInitiatorName_Object=MibTableColumn
h3cInitiatorName=_H3cInitiatorName_Object((1,3,6,1,4,1,2011,10,10,5,1,7,2,1,2),_H3cInitiatorName_Type())
h3cInitiatorName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cInitiatorName.setStatus(_A)
_H3cInitiatorRowStatus_Type=RowStatus
_H3cInitiatorRowStatus_Object=MibTableColumn
h3cInitiatorRowStatus=_H3cInitiatorRowStatus_Object((1,3,6,1,4,1,2011,10,10,5,1,7,2,1,3),_H3cInitiatorRowStatus_Type())
h3cInitiatorRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cInitiatorRowStatus.setStatus(_A)
_H3cTargetInitiatorAssociateTable_Object=MibTable
h3cTargetInitiatorAssociateTable=_H3cTargetInitiatorAssociateTable_Object((1,3,6,1,4,1,2011,10,10,5,1,8))
if mibBuilder.loadTexts:h3cTargetInitiatorAssociateTable.setStatus(_A)
_H3cTargetInitiatorAssociateEntry_Object=MibTableRow
h3cTargetInitiatorAssociateEntry=_H3cTargetInitiatorAssociateEntry_Object((1,3,6,1,4,1,2011,10,10,5,1,8,1))
h3cTargetInitiatorAssociateEntry.setIndexNames((0,_D,_H),(0,_D,_L))
if mibBuilder.loadTexts:h3cTargetInitiatorAssociateEntry.setStatus(_A)
class _H3cTIAccessMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('read',1),('write',2),(_Q,3)))
_H3cTIAccessMode_Type.__name__=_E
_H3cTIAccessMode_Object=MibTableColumn
h3cTIAccessMode=_H3cTIAccessMode_Object((1,3,6,1,4,1,2011,10,10,5,1,8,1,1),_H3cTIAccessMode_Type())
h3cTIAccessMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTIAccessMode.setStatus(_A)
class _H3cTIChap_Type(H3cStorageEnableState):defaultValue=2
_H3cTIChap_Type.__name__=_M
_H3cTIChap_Object=MibTableColumn
h3cTIChap=_H3cTIChap_Object((1,3,6,1,4,1,2011,10,10,5,1,8,1,2),_H3cTIChap_Type())
h3cTIChap.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTIChap.setStatus(_A)
class _H3cTIUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_H3cTIUserName_Type.__name__=_F
_H3cTIUserName_Object=MibTableColumn
h3cTIUserName=_H3cTIUserName_Object((1,3,6,1,4,1,2011,10,10,5,1,8,1,3),_H3cTIUserName_Type())
h3cTIUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTIUserName.setStatus(_A)
class _H3cTIPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,16))
_H3cTIPassword_Type.__name__=_F
_H3cTIPassword_Object=MibTableColumn
h3cTIPassword=_H3cTIPassword_Object((1,3,6,1,4,1,2011,10,10,5,1,8,1,4),_H3cTIPassword_Type())
h3cTIPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTIPassword.setStatus(_A)
_H3cTIRowStatus_Type=RowStatus
_H3cTIRowStatus_Object=MibTableColumn
h3cTIRowStatus=_H3cTIRowStatus_Object((1,3,6,1,4,1,2011,10,10,5,1,8,1,5),_H3cTIRowStatus_Type())
h3cTIRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTIRowStatus.setStatus(_A)
_H3cTISessionTable_Object=MibTable
h3cTISessionTable=_H3cTISessionTable_Object((1,3,6,1,4,1,2011,10,10,5,1,9))
if mibBuilder.loadTexts:h3cTISessionTable.setStatus(_A)
_H3cTISessionEntry_Object=MibTableRow
h3cTISessionEntry=_H3cTISessionEntry_Object((1,3,6,1,4,1,2011,10,10,5,1,9,1))
h3cTISessionEntry.setIndexNames((0,_D,_H),(0,_D,_R))
if mibBuilder.loadTexts:h3cTISessionEntry.setStatus(_A)
_H3cTISessionId_Type=H3cSessionIDType
_H3cTISessionId_Object=MibTableColumn
h3cTISessionId=_H3cTISessionId_Object((1,3,6,1,4,1,2011,10,10,5,1,9,1,1),_H3cTISessionId_Type())
h3cTISessionId.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cTISessionId.setStatus(_A)
_H3cTISessionConnectionCount_Type=Counter32
_H3cTISessionConnectionCount_Object=MibTableColumn
h3cTISessionConnectionCount=_H3cTISessionConnectionCount_Object((1,3,6,1,4,1,2011,10,10,5,1,9,1,2),_H3cTISessionConnectionCount_Type())
h3cTISessionConnectionCount.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTISessionConnectionCount.setStatus(_A)
class _H3cTISessionInitiatorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,223))
_H3cTISessionInitiatorName_Type.__name__=_F
_H3cTISessionInitiatorName_Object=MibTableColumn
h3cTISessionInitiatorName=_H3cTISessionInitiatorName_Object((1,3,6,1,4,1,2011,10,10,5,1,9,1,3),_H3cTISessionInitiatorName_Type())
h3cTISessionInitiatorName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTISessionInitiatorName.setStatus(_A)
_H3cSanClientResource_ObjectIdentity=ObjectIdentity
h3cSanClientResource=_H3cSanClientResource_ObjectIdentity((1,3,6,1,4,1,2011,10,10,5,1,10))
_H3cSanClientCreateIndex_Type=Integer32
_H3cSanClientCreateIndex_Object=MibScalar
h3cSanClientCreateIndex=_H3cSanClientCreateIndex_Object((1,3,6,1,4,1,2011,10,10,5,1,10,1),_H3cSanClientCreateIndex_Type())
h3cSanClientCreateIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSanClientCreateIndex.setStatus(_A)
_H3cSanClientTable_Object=MibTable
h3cSanClientTable=_H3cSanClientTable_Object((1,3,6,1,4,1,2011,10,10,5,1,10,2))
if mibBuilder.loadTexts:h3cSanClientTable.setStatus(_A)
_H3cSanClientEntry_Object=MibTableRow
h3cSanClientEntry=_H3cSanClientEntry_Object((1,3,6,1,4,1,2011,10,10,5,1,10,2,1))
h3cSanClientEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:h3cSanClientEntry.setStatus(_A)
_H3cSanClientId_Type=Integer32
_H3cSanClientId_Object=MibTableColumn
h3cSanClientId=_H3cSanClientId_Object((1,3,6,1,4,1,2011,10,10,5,1,10,2,1,1),_H3cSanClientId_Type())
h3cSanClientId.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSanClientId.setStatus(_A)
class _H3cSanClientName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_H3cSanClientName_Type.__name__=_F
_H3cSanClientName_Object=MibTableColumn
h3cSanClientName=_H3cSanClientName_Object((1,3,6,1,4,1,2011,10,10,5,1,10,2,1,2),_H3cSanClientName_Type())
h3cSanClientName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSanClientName.setStatus(_A)
class _H3cSanClientType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('iscsi',1),('fc',2)))
_H3cSanClientType_Type.__name__=_E
_H3cSanClientType_Object=MibTableColumn
h3cSanClientType=_H3cSanClientType_Object((1,3,6,1,4,1,2011,10,10,5,1,10,2,1,3),_H3cSanClientType_Type())
h3cSanClientType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSanClientType.setStatus(_A)
_H3cFcInitiatorWwpnList_Type=H3cWwpnListType
_H3cFcInitiatorWwpnList_Object=MibTableColumn
h3cFcInitiatorWwpnList=_H3cFcInitiatorWwpnList_Object((1,3,6,1,4,1,2011,10,10,5,1,10,2,1,4),_H3cFcInitiatorWwpnList_Type())
h3cFcInitiatorWwpnList.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcInitiatorWwpnList.setStatus(_A)
class _H3cFcAccessMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('read',1),('write',2),(_Q,3)))
_H3cFcAccessMode_Type.__name__=_E
_H3cFcAccessMode_Object=MibTableColumn
h3cFcAccessMode=_H3cFcAccessMode_Object((1,3,6,1,4,1,2011,10,10,5,1,10,2,1,6),_H3cFcAccessMode_Type())
h3cFcAccessMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcAccessMode.setStatus(_A)
_H3cSanClientRowStatus_Type=RowStatus
_H3cSanClientRowStatus_Object=MibTableColumn
h3cSanClientRowStatus=_H3cSanClientRowStatus_Object((1,3,6,1,4,1,2011,10,10,5,1,10,2,1,7),_H3cSanClientRowStatus_Type())
h3cSanClientRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSanClientRowStatus.setStatus(_A)
_H3cFcLogicResourceTable_Object=MibTable
h3cFcLogicResourceTable=_H3cFcLogicResourceTable_Object((1,3,6,1,4,1,2011,10,10,5,1,11))
if mibBuilder.loadTexts:h3cFcLogicResourceTable.setStatus(_A)
_H3cFcLogicResourceEntry_Object=MibTableRow
h3cFcLogicResourceEntry=_H3cFcLogicResourceEntry_Object((1,3,6,1,4,1,2011,10,10,5,1,11,1))
h3cFcLogicResourceEntry.setIndexNames((0,_D,_K),(0,_D,_I))
if mibBuilder.loadTexts:h3cFcLogicResourceEntry.setStatus(_A)
class _H3cFcLvLun_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_H3cFcLvLun_Type.__name__=_E
_H3cFcLvLun_Object=MibTableColumn
h3cFcLvLun=_H3cFcLvLun_Object((1,3,6,1,4,1,2011,10,10,5,1,11,1,1),_H3cFcLvLun_Type())
h3cFcLvLun.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFcLvLun.setStatus(_A)
_H3cFcTargetWwpnName_Type=H3cWwpnListType
_H3cFcTargetWwpnName_Object=MibTableColumn
h3cFcTargetWwpnName=_H3cFcTargetWwpnName_Object((1,3,6,1,4,1,2011,10,10,5,1,11,1,2),_H3cFcTargetWwpnName_Type())
h3cFcTargetWwpnName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcTargetWwpnName.setStatus(_A)
_H3cFcInitiatorWwpnName_Type=H3cWwpnListType
_H3cFcInitiatorWwpnName_Object=MibTableColumn
h3cFcInitiatorWwpnName=_H3cFcInitiatorWwpnName_Object((1,3,6,1,4,1,2011,10,10,5,1,11,1,3),_H3cFcInitiatorWwpnName_Type())
h3cFcInitiatorWwpnName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcInitiatorWwpnName.setStatus(_A)
_H3cFcLvRowStatus_Type=RowStatus
_H3cFcLvRowStatus_Object=MibTableColumn
h3cFcLvRowStatus=_H3cFcLvRowStatus_Object((1,3,6,1,4,1,2011,10,10,5,1,11,1,4),_H3cFcLvRowStatus_Type())
h3cFcLvRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcLvRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'h3cLogicVolume':h3cLogicVolume,'h3cLvMibObjects':h3cLvMibObjects,'h3cLogicResourceCapacityObject':h3cLogicResourceCapacityObject,'h3cLvCount':h3cLvCount,'h3cLvMaxSize':h3cLvMaxSize,'h3cTargetCount':h3cTargetCount,'h3cInitiatorCount':h3cInitiatorCount,'h3cSanClientCount':h3cSanClientCount,'h3cLogicVolumeResource':h3cLogicVolumeResource,'h3cLvCreateIndex':h3cLvCreateIndex,'h3cLvTable':h3cLvTable,'h3cLvEntry':h3cLvEntry,_I:h3cLvIndex,'h3cLvName':h3cLvName,'h3cLvTotalSize':h3cLvTotalSize,'h3cLvCreateRaidUuid':h3cLvCreateRaidUuid,'h3cLvCreateRaidSize':h3cLvCreateRaidSize,'h3cLvSedInquiryStringKeep':h3cLvSedInquiryStringKeep,'h3cLvSedRaidUuid':h3cLvSedRaidUuid,'h3cLvState':h3cLvState,'h3cLvAssigned':h3cLvAssigned,'h3cLvType':h3cLvType,'h3cLvExtendTimes':h3cLvExtendTimes,'h3cLvRowStatus':h3cLvRowStatus,'h3cLvExtTable':h3cLvExtTable,'h3cLvExtEntry':h3cLvExtEntry,_N:h3cLvRaidUuid,'h3cLvExtSize':h3cLvExtSize,'h3cLvRaidSize':h3cLvRaidSize,'h3cLvExtRowStatus':h3cLvExtRowStatus,'h3cTargetResource':h3cTargetResource,'h3cTargetCreateIndex':h3cTargetCreateIndex,'h3cTargetTable':h3cTargetTable,'h3cTargetEntry':h3cTargetEntry,_H:h3cTargetId,'h3cTargetName':h3cTargetName,'h3cTargetMinLun':h3cTargetMinLun,'h3cTargetRowStatus':h3cTargetRowStatus,'h3cTargetAddressTable':h3cTargetAddressTable,'h3cTargetAddressEntry':h3cTargetAddressEntry,_P:h3cTargetIpAddress,_O:h3cTargetIpAddrType,'h3cTargetIpRowStatus':h3cTargetIpRowStatus,'h3cTargetLvAssignTable':h3cTargetLvAssignTable,'h3cTargetLvAssignEntry':h3cTargetLvAssignEntry,'h3cTargetLvLun':h3cTargetLvLun,'h3cTargetLvRowStatus':h3cTargetLvRowStatus,'h3cInitiatorResource':h3cInitiatorResource,'h3cInitiatorCreateIndex':h3cInitiatorCreateIndex,'h3cInitiatorTable':h3cInitiatorTable,'h3cInitiatorEntry':h3cInitiatorEntry,_L:h3cInitiatorId,'h3cInitiatorName':h3cInitiatorName,'h3cInitiatorRowStatus':h3cInitiatorRowStatus,'h3cTargetInitiatorAssociateTable':h3cTargetInitiatorAssociateTable,'h3cTargetInitiatorAssociateEntry':h3cTargetInitiatorAssociateEntry,'h3cTIAccessMode':h3cTIAccessMode,'h3cTIChap':h3cTIChap,'h3cTIUserName':h3cTIUserName,'h3cTIPassword':h3cTIPassword,'h3cTIRowStatus':h3cTIRowStatus,'h3cTISessionTable':h3cTISessionTable,'h3cTISessionEntry':h3cTISessionEntry,_R:h3cTISessionId,'h3cTISessionConnectionCount':h3cTISessionConnectionCount,'h3cTISessionInitiatorName':h3cTISessionInitiatorName,'h3cSanClientResource':h3cSanClientResource,'h3cSanClientCreateIndex':h3cSanClientCreateIndex,'h3cSanClientTable':h3cSanClientTable,'h3cSanClientEntry':h3cSanClientEntry,_K:h3cSanClientId,'h3cSanClientName':h3cSanClientName,'h3cSanClientType':h3cSanClientType,'h3cFcInitiatorWwpnList':h3cFcInitiatorWwpnList,'h3cFcAccessMode':h3cFcAccessMode,'h3cSanClientRowStatus':h3cSanClientRowStatus,'h3cFcLogicResourceTable':h3cFcLogicResourceTable,'h3cFcLogicResourceEntry':h3cFcLogicResourceEntry,'h3cFcLvLun':h3cFcLvLun,'h3cFcTargetWwpnName':h3cFcTargetWwpnName,'h3cFcInitiatorWwpnName':h3cFcInitiatorWwpnName,'h3cFcLvRowStatus':h3cFcLvRowStatus})