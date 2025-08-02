_R='hh3cTISessionId'
_Q='nonexclusive'
_P='hh3cTargetIpAddress'
_O='hh3cTargetIpAddrType'
_N='hh3cLvRaidUuid'
_M='Hh3cStorageEnableState'
_L='hh3cInitiatorId'
_K='hh3cSanClientId'
_J='MB'
_I='hh3cLvIndex'
_H='hh3cTargetId'
_G='not-accessible'
_F='OctetString'
_E='Integer32'
_D='HH3C-LOGIC-VOLUME-MIB'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols('ENTITY-MIB','entPhysicalIndex')
Hh3cLvIDType,Hh3cRaidIDType,Hh3cSessionIDType,Hh3cStorageActionType,Hh3cStorageEnableState,Hh3cStorageLedStateType,Hh3cWwpnListType,hh3cStorageRef=mibBuilder.importSymbols('HH3C-STORAGE-REF-MIB','Hh3cLvIDType','Hh3cRaidIDType','Hh3cSessionIDType','Hh3cStorageActionType',_M,'Hh3cStorageLedStateType','Hh3cWwpnListType','hh3cStorageRef')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
hh3cLogicVolume=ModuleIdentity((1,3,6,1,4,1,25506,10,5))
_Hh3cLvMibObjects_ObjectIdentity=ObjectIdentity
hh3cLvMibObjects=_Hh3cLvMibObjects_ObjectIdentity((1,3,6,1,4,1,25506,10,5,1))
_Hh3cLogicResourceCapacityObject_ObjectIdentity=ObjectIdentity
hh3cLogicResourceCapacityObject=_Hh3cLogicResourceCapacityObject_ObjectIdentity((1,3,6,1,4,1,25506,10,5,1,1))
_Hh3cLvCount_Type=Integer32
_Hh3cLvCount_Object=MibScalar
hh3cLvCount=_Hh3cLvCount_Object((1,3,6,1,4,1,25506,10,5,1,1,1),_Hh3cLvCount_Type())
hh3cLvCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cLvCount.setStatus(_A)
_Hh3cLvMaxSize_Type=Integer32
_Hh3cLvMaxSize_Object=MibScalar
hh3cLvMaxSize=_Hh3cLvMaxSize_Object((1,3,6,1,4,1,25506,10,5,1,1,2),_Hh3cLvMaxSize_Type())
hh3cLvMaxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cLvMaxSize.setStatus(_A)
if mibBuilder.loadTexts:hh3cLvMaxSize.setUnits('TB')
_Hh3cTargetCount_Type=Integer32
_Hh3cTargetCount_Object=MibScalar
hh3cTargetCount=_Hh3cTargetCount_Object((1,3,6,1,4,1,25506,10,5,1,1,3),_Hh3cTargetCount_Type())
hh3cTargetCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cTargetCount.setStatus(_A)
_Hh3cInitiatorCount_Type=Integer32
_Hh3cInitiatorCount_Object=MibScalar
hh3cInitiatorCount=_Hh3cInitiatorCount_Object((1,3,6,1,4,1,25506,10,5,1,1,4),_Hh3cInitiatorCount_Type())
hh3cInitiatorCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cInitiatorCount.setStatus(_A)
_Hh3cSanClientCount_Type=Integer32
_Hh3cSanClientCount_Object=MibScalar
hh3cSanClientCount=_Hh3cSanClientCount_Object((1,3,6,1,4,1,25506,10,5,1,1,5),_Hh3cSanClientCount_Type())
hh3cSanClientCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cSanClientCount.setStatus(_A)
_Hh3cLogicVolumeResource_ObjectIdentity=ObjectIdentity
hh3cLogicVolumeResource=_Hh3cLogicVolumeResource_ObjectIdentity((1,3,6,1,4,1,25506,10,5,1,2))
_Hh3cLvCreateIndex_Type=Hh3cLvIDType
_Hh3cLvCreateIndex_Object=MibScalar
hh3cLvCreateIndex=_Hh3cLvCreateIndex_Object((1,3,6,1,4,1,25506,10,5,1,2,1),_Hh3cLvCreateIndex_Type())
hh3cLvCreateIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cLvCreateIndex.setStatus(_A)
_Hh3cLvTable_Object=MibTable
hh3cLvTable=_Hh3cLvTable_Object((1,3,6,1,4,1,25506,10,5,1,2,2))
if mibBuilder.loadTexts:hh3cLvTable.setStatus(_A)
_Hh3cLvEntry_Object=MibTableRow
hh3cLvEntry=_Hh3cLvEntry_Object((1,3,6,1,4,1,25506,10,5,1,2,2,1))
hh3cLvEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:hh3cLvEntry.setStatus(_A)
_Hh3cLvIndex_Type=Hh3cLvIDType
_Hh3cLvIndex_Object=MibTableColumn
hh3cLvIndex=_Hh3cLvIndex_Object((1,3,6,1,4,1,25506,10,5,1,2,2,1,1),_Hh3cLvIndex_Type())
hh3cLvIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hh3cLvIndex.setStatus(_A)
class _Hh3cLvName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Hh3cLvName_Type.__name__=_F
_Hh3cLvName_Object=MibTableColumn
hh3cLvName=_Hh3cLvName_Object((1,3,6,1,4,1,25506,10,5,1,2,2,1,2),_Hh3cLvName_Type())
hh3cLvName.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cLvName.setStatus(_A)
_Hh3cLvTotalSize_Type=Integer32
_Hh3cLvTotalSize_Object=MibTableColumn
hh3cLvTotalSize=_Hh3cLvTotalSize_Object((1,3,6,1,4,1,25506,10,5,1,2,2,1,3),_Hh3cLvTotalSize_Type())
hh3cLvTotalSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cLvTotalSize.setStatus(_A)
if mibBuilder.loadTexts:hh3cLvTotalSize.setUnits(_J)
_Hh3cLvCreateRaidUuid_Type=Hh3cRaidIDType
_Hh3cLvCreateRaidUuid_Object=MibTableColumn
hh3cLvCreateRaidUuid=_Hh3cLvCreateRaidUuid_Object((1,3,6,1,4,1,25506,10,5,1,2,2,1,4),_Hh3cLvCreateRaidUuid_Type())
hh3cLvCreateRaidUuid.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cLvCreateRaidUuid.setStatus(_A)
_Hh3cLvCreateRaidSize_Type=Integer32
_Hh3cLvCreateRaidSize_Object=MibTableColumn
hh3cLvCreateRaidSize=_Hh3cLvCreateRaidSize_Object((1,3,6,1,4,1,25506,10,5,1,2,2,1,5),_Hh3cLvCreateRaidSize_Type())
hh3cLvCreateRaidSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cLvCreateRaidSize.setStatus(_A)
if mibBuilder.loadTexts:hh3cLvCreateRaidSize.setUnits(_J)
_Hh3cLvSedInquiryStringKeep_Type=TruthValue
_Hh3cLvSedInquiryStringKeep_Object=MibTableColumn
hh3cLvSedInquiryStringKeep=_Hh3cLvSedInquiryStringKeep_Object((1,3,6,1,4,1,25506,10,5,1,2,2,1,6),_Hh3cLvSedInquiryStringKeep_Type())
hh3cLvSedInquiryStringKeep.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cLvSedInquiryStringKeep.setStatus(_A)
_Hh3cLvSedRaidUuid_Type=Hh3cRaidIDType
_Hh3cLvSedRaidUuid_Object=MibTableColumn
hh3cLvSedRaidUuid=_Hh3cLvSedRaidUuid_Object((1,3,6,1,4,1,25506,10,5,1,2,2,1,7),_Hh3cLvSedRaidUuid_Type())
hh3cLvSedRaidUuid.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cLvSedRaidUuid.setStatus(_A)
class _Hh3cLvState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('usable',1),('unusable',2),('conflict',3)))
_Hh3cLvState_Type.__name__=_E
_Hh3cLvState_Object=MibTableColumn
hh3cLvState=_Hh3cLvState_Object((1,3,6,1,4,1,25506,10,5,1,2,2,1,8),_Hh3cLvState_Type())
hh3cLvState.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cLvState.setStatus(_A)
class _Hh3cLvAssigned_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('use',1),('unused',2)))
_Hh3cLvAssigned_Type.__name__=_E
_Hh3cLvAssigned_Object=MibTableColumn
hh3cLvAssigned=_Hh3cLvAssigned_Object((1,3,6,1,4,1,25506,10,5,1,2,2,1,9),_Hh3cLvAssigned_Type())
hh3cLvAssigned.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cLvAssigned.setStatus(_A)
class _Hh3cLvType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('virtual',1),('direct',2),('serviceEnabled',3)))
_Hh3cLvType_Type.__name__=_E
_Hh3cLvType_Object=MibTableColumn
hh3cLvType=_Hh3cLvType_Object((1,3,6,1,4,1,25506,10,5,1,2,2,1,10),_Hh3cLvType_Type())
hh3cLvType.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cLvType.setStatus(_A)
_Hh3cLvExtendTimes_Type=Integer32
_Hh3cLvExtendTimes_Object=MibTableColumn
hh3cLvExtendTimes=_Hh3cLvExtendTimes_Object((1,3,6,1,4,1,25506,10,5,1,2,2,1,11),_Hh3cLvExtendTimes_Type())
hh3cLvExtendTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cLvExtendTimes.setStatus(_A)
_Hh3cLvRowStatus_Type=RowStatus
_Hh3cLvRowStatus_Object=MibTableColumn
hh3cLvRowStatus=_Hh3cLvRowStatus_Object((1,3,6,1,4,1,25506,10,5,1,2,2,1,12),_Hh3cLvRowStatus_Type())
hh3cLvRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cLvRowStatus.setStatus(_A)
_Hh3cLvExtTable_Object=MibTable
hh3cLvExtTable=_Hh3cLvExtTable_Object((1,3,6,1,4,1,25506,10,5,1,3))
if mibBuilder.loadTexts:hh3cLvExtTable.setStatus(_A)
_Hh3cLvExtEntry_Object=MibTableRow
hh3cLvExtEntry=_Hh3cLvExtEntry_Object((1,3,6,1,4,1,25506,10,5,1,3,1))
hh3cLvExtEntry.setIndexNames((0,_D,_I),(0,_D,_N))
if mibBuilder.loadTexts:hh3cLvExtEntry.setStatus(_A)
_Hh3cLvRaidUuid_Type=Hh3cRaidIDType
_Hh3cLvRaidUuid_Object=MibTableColumn
hh3cLvRaidUuid=_Hh3cLvRaidUuid_Object((1,3,6,1,4,1,25506,10,5,1,3,1,1),_Hh3cLvRaidUuid_Type())
hh3cLvRaidUuid.setMaxAccess(_G)
if mibBuilder.loadTexts:hh3cLvRaidUuid.setStatus(_A)
class _Hh3cLvExtSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Hh3cLvExtSize_Type.__name__=_E
_Hh3cLvExtSize_Object=MibTableColumn
hh3cLvExtSize=_Hh3cLvExtSize_Object((1,3,6,1,4,1,25506,10,5,1,3,1,2),_Hh3cLvExtSize_Type())
hh3cLvExtSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cLvExtSize.setStatus(_A)
if mibBuilder.loadTexts:hh3cLvExtSize.setUnits(_J)
_Hh3cLvRaidSize_Type=Integer32
_Hh3cLvRaidSize_Object=MibTableColumn
hh3cLvRaidSize=_Hh3cLvRaidSize_Object((1,3,6,1,4,1,25506,10,5,1,3,1,3),_Hh3cLvRaidSize_Type())
hh3cLvRaidSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cLvRaidSize.setStatus(_A)
if mibBuilder.loadTexts:hh3cLvRaidSize.setUnits(_J)
_Hh3cLvExtRowStatus_Type=RowStatus
_Hh3cLvExtRowStatus_Object=MibTableColumn
hh3cLvExtRowStatus=_Hh3cLvExtRowStatus_Object((1,3,6,1,4,1,25506,10,5,1,3,1,4),_Hh3cLvExtRowStatus_Type())
hh3cLvExtRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cLvExtRowStatus.setStatus(_A)
_Hh3cTargetResource_ObjectIdentity=ObjectIdentity
hh3cTargetResource=_Hh3cTargetResource_ObjectIdentity((1,3,6,1,4,1,25506,10,5,1,4))
_Hh3cTargetCreateIndex_Type=Integer32
_Hh3cTargetCreateIndex_Object=MibScalar
hh3cTargetCreateIndex=_Hh3cTargetCreateIndex_Object((1,3,6,1,4,1,25506,10,5,1,4,1),_Hh3cTargetCreateIndex_Type())
hh3cTargetCreateIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cTargetCreateIndex.setStatus(_A)
_Hh3cTargetTable_Object=MibTable
hh3cTargetTable=_Hh3cTargetTable_Object((1,3,6,1,4,1,25506,10,5,1,4,2))
if mibBuilder.loadTexts:hh3cTargetTable.setStatus(_A)
_Hh3cTargetEntry_Object=MibTableRow
hh3cTargetEntry=_Hh3cTargetEntry_Object((1,3,6,1,4,1,25506,10,5,1,4,2,1))
hh3cTargetEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:hh3cTargetEntry.setStatus(_A)
_Hh3cTargetId_Type=Integer32
_Hh3cTargetId_Object=MibTableColumn
hh3cTargetId=_Hh3cTargetId_Object((1,3,6,1,4,1,25506,10,5,1,4,2,1,1),_Hh3cTargetId_Type())
hh3cTargetId.setMaxAccess(_G)
if mibBuilder.loadTexts:hh3cTargetId.setStatus(_A)
class _Hh3cTargetName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,223))
_Hh3cTargetName_Type.__name__=_F
_Hh3cTargetName_Object=MibTableColumn
hh3cTargetName=_Hh3cTargetName_Object((1,3,6,1,4,1,25506,10,5,1,4,2,1,2),_Hh3cTargetName_Type())
hh3cTargetName.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cTargetName.setStatus(_A)
class _Hh3cTargetMinLun_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_Hh3cTargetMinLun_Type.__name__=_E
_Hh3cTargetMinLun_Object=MibTableColumn
hh3cTargetMinLun=_Hh3cTargetMinLun_Object((1,3,6,1,4,1,25506,10,5,1,4,2,1,3),_Hh3cTargetMinLun_Type())
hh3cTargetMinLun.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cTargetMinLun.setStatus(_A)
_Hh3cTargetRowStatus_Type=RowStatus
_Hh3cTargetRowStatus_Object=MibTableColumn
hh3cTargetRowStatus=_Hh3cTargetRowStatus_Object((1,3,6,1,4,1,25506,10,5,1,4,2,1,4),_Hh3cTargetRowStatus_Type())
hh3cTargetRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cTargetRowStatus.setStatus(_A)
_Hh3cTargetAddressTable_Object=MibTable
hh3cTargetAddressTable=_Hh3cTargetAddressTable_Object((1,3,6,1,4,1,25506,10,5,1,5))
if mibBuilder.loadTexts:hh3cTargetAddressTable.setStatus(_A)
_Hh3cTargetAddressEntry_Object=MibTableRow
hh3cTargetAddressEntry=_Hh3cTargetAddressEntry_Object((1,3,6,1,4,1,25506,10,5,1,5,1))
hh3cTargetAddressEntry.setIndexNames((0,_D,_H),(0,_D,_O),(0,_D,_P))
if mibBuilder.loadTexts:hh3cTargetAddressEntry.setStatus(_A)
_Hh3cTargetIpAddress_Type=InetAddress
_Hh3cTargetIpAddress_Object=MibTableColumn
hh3cTargetIpAddress=_Hh3cTargetIpAddress_Object((1,3,6,1,4,1,25506,10,5,1,5,1,1),_Hh3cTargetIpAddress_Type())
hh3cTargetIpAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:hh3cTargetIpAddress.setStatus(_A)
_Hh3cTargetIpAddrType_Type=InetAddressType
_Hh3cTargetIpAddrType_Object=MibTableColumn
hh3cTargetIpAddrType=_Hh3cTargetIpAddrType_Object((1,3,6,1,4,1,25506,10,5,1,5,1,2),_Hh3cTargetIpAddrType_Type())
hh3cTargetIpAddrType.setMaxAccess(_G)
if mibBuilder.loadTexts:hh3cTargetIpAddrType.setStatus(_A)
_Hh3cTargetIpRowStatus_Type=RowStatus
_Hh3cTargetIpRowStatus_Object=MibTableColumn
hh3cTargetIpRowStatus=_Hh3cTargetIpRowStatus_Object((1,3,6,1,4,1,25506,10,5,1,5,1,3),_Hh3cTargetIpRowStatus_Type())
hh3cTargetIpRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cTargetIpRowStatus.setStatus(_A)
_Hh3cTargetLvAssignTable_Object=MibTable
hh3cTargetLvAssignTable=_Hh3cTargetLvAssignTable_Object((1,3,6,1,4,1,25506,10,5,1,6))
if mibBuilder.loadTexts:hh3cTargetLvAssignTable.setStatus(_A)
_Hh3cTargetLvAssignEntry_Object=MibTableRow
hh3cTargetLvAssignEntry=_Hh3cTargetLvAssignEntry_Object((1,3,6,1,4,1,25506,10,5,1,6,1))
hh3cTargetLvAssignEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:hh3cTargetLvAssignEntry.setStatus(_A)
class _Hh3cTargetLvLun_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_Hh3cTargetLvLun_Type.__name__=_E
_Hh3cTargetLvLun_Object=MibTableColumn
hh3cTargetLvLun=_Hh3cTargetLvLun_Object((1,3,6,1,4,1,25506,10,5,1,6,1,1),_Hh3cTargetLvLun_Type())
hh3cTargetLvLun.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cTargetLvLun.setStatus(_A)
_Hh3cTargetLvRowStatus_Type=RowStatus
_Hh3cTargetLvRowStatus_Object=MibTableColumn
hh3cTargetLvRowStatus=_Hh3cTargetLvRowStatus_Object((1,3,6,1,4,1,25506,10,5,1,6,1,2),_Hh3cTargetLvRowStatus_Type())
hh3cTargetLvRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cTargetLvRowStatus.setStatus(_A)
_Hh3cInitiatorResource_ObjectIdentity=ObjectIdentity
hh3cInitiatorResource=_Hh3cInitiatorResource_ObjectIdentity((1,3,6,1,4,1,25506,10,5,1,7))
_Hh3cInitiatorCreateIndex_Type=Integer32
_Hh3cInitiatorCreateIndex_Object=MibScalar
hh3cInitiatorCreateIndex=_Hh3cInitiatorCreateIndex_Object((1,3,6,1,4,1,25506,10,5,1,7,1),_Hh3cInitiatorCreateIndex_Type())
hh3cInitiatorCreateIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cInitiatorCreateIndex.setStatus(_A)
_Hh3cInitiatorTable_Object=MibTable
hh3cInitiatorTable=_Hh3cInitiatorTable_Object((1,3,6,1,4,1,25506,10,5,1,7,2))
if mibBuilder.loadTexts:hh3cInitiatorTable.setStatus(_A)
_Hh3cInitiatorEntry_Object=MibTableRow
hh3cInitiatorEntry=_Hh3cInitiatorEntry_Object((1,3,6,1,4,1,25506,10,5,1,7,2,1))
hh3cInitiatorEntry.setIndexNames((0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:hh3cInitiatorEntry.setStatus(_A)
_Hh3cInitiatorId_Type=Integer32
_Hh3cInitiatorId_Object=MibTableColumn
hh3cInitiatorId=_Hh3cInitiatorId_Object((1,3,6,1,4,1,25506,10,5,1,7,2,1,1),_Hh3cInitiatorId_Type())
hh3cInitiatorId.setMaxAccess(_G)
if mibBuilder.loadTexts:hh3cInitiatorId.setStatus(_A)
class _Hh3cInitiatorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,223))
_Hh3cInitiatorName_Type.__name__=_F
_Hh3cInitiatorName_Object=MibTableColumn
hh3cInitiatorName=_Hh3cInitiatorName_Object((1,3,6,1,4,1,25506,10,5,1,7,2,1,2),_Hh3cInitiatorName_Type())
hh3cInitiatorName.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cInitiatorName.setStatus(_A)
_Hh3cInitiatorRowStatus_Type=RowStatus
_Hh3cInitiatorRowStatus_Object=MibTableColumn
hh3cInitiatorRowStatus=_Hh3cInitiatorRowStatus_Object((1,3,6,1,4,1,25506,10,5,1,7,2,1,3),_Hh3cInitiatorRowStatus_Type())
hh3cInitiatorRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cInitiatorRowStatus.setStatus(_A)
_Hh3cTargetInitiatorAssociateTable_Object=MibTable
hh3cTargetInitiatorAssociateTable=_Hh3cTargetInitiatorAssociateTable_Object((1,3,6,1,4,1,25506,10,5,1,8))
if mibBuilder.loadTexts:hh3cTargetInitiatorAssociateTable.setStatus(_A)
_Hh3cTargetInitiatorAssociateEntry_Object=MibTableRow
hh3cTargetInitiatorAssociateEntry=_Hh3cTargetInitiatorAssociateEntry_Object((1,3,6,1,4,1,25506,10,5,1,8,1))
hh3cTargetInitiatorAssociateEntry.setIndexNames((0,_D,_H),(0,_D,_L))
if mibBuilder.loadTexts:hh3cTargetInitiatorAssociateEntry.setStatus(_A)
class _Hh3cTIAccessMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('read',1),('write',2),(_Q,3)))
_Hh3cTIAccessMode_Type.__name__=_E
_Hh3cTIAccessMode_Object=MibTableColumn
hh3cTIAccessMode=_Hh3cTIAccessMode_Object((1,3,6,1,4,1,25506,10,5,1,8,1,1),_Hh3cTIAccessMode_Type())
hh3cTIAccessMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cTIAccessMode.setStatus(_A)
class _Hh3cTIChap_Type(Hh3cStorageEnableState):defaultValue=2
_Hh3cTIChap_Type.__name__=_M
_Hh3cTIChap_Object=MibTableColumn
hh3cTIChap=_Hh3cTIChap_Object((1,3,6,1,4,1,25506,10,5,1,8,1,2),_Hh3cTIChap_Type())
hh3cTIChap.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cTIChap.setStatus(_A)
class _Hh3cTIUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_Hh3cTIUserName_Type.__name__=_F
_Hh3cTIUserName_Object=MibTableColumn
hh3cTIUserName=_Hh3cTIUserName_Object((1,3,6,1,4,1,25506,10,5,1,8,1,3),_Hh3cTIUserName_Type())
hh3cTIUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cTIUserName.setStatus(_A)
class _Hh3cTIPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,16))
_Hh3cTIPassword_Type.__name__=_F
_Hh3cTIPassword_Object=MibTableColumn
hh3cTIPassword=_Hh3cTIPassword_Object((1,3,6,1,4,1,25506,10,5,1,8,1,4),_Hh3cTIPassword_Type())
hh3cTIPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cTIPassword.setStatus(_A)
_Hh3cTIRowStatus_Type=RowStatus
_Hh3cTIRowStatus_Object=MibTableColumn
hh3cTIRowStatus=_Hh3cTIRowStatus_Object((1,3,6,1,4,1,25506,10,5,1,8,1,5),_Hh3cTIRowStatus_Type())
hh3cTIRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cTIRowStatus.setStatus(_A)
_Hh3cTISessionTable_Object=MibTable
hh3cTISessionTable=_Hh3cTISessionTable_Object((1,3,6,1,4,1,25506,10,5,1,9))
if mibBuilder.loadTexts:hh3cTISessionTable.setStatus(_A)
_Hh3cTISessionEntry_Object=MibTableRow
hh3cTISessionEntry=_Hh3cTISessionEntry_Object((1,3,6,1,4,1,25506,10,5,1,9,1))
hh3cTISessionEntry.setIndexNames((0,_D,_H),(0,_D,_R))
if mibBuilder.loadTexts:hh3cTISessionEntry.setStatus(_A)
_Hh3cTISessionId_Type=Hh3cSessionIDType
_Hh3cTISessionId_Object=MibTableColumn
hh3cTISessionId=_Hh3cTISessionId_Object((1,3,6,1,4,1,25506,10,5,1,9,1,1),_Hh3cTISessionId_Type())
hh3cTISessionId.setMaxAccess(_G)
if mibBuilder.loadTexts:hh3cTISessionId.setStatus(_A)
_Hh3cTISessionConnectionCount_Type=Counter32
_Hh3cTISessionConnectionCount_Object=MibTableColumn
hh3cTISessionConnectionCount=_Hh3cTISessionConnectionCount_Object((1,3,6,1,4,1,25506,10,5,1,9,1,2),_Hh3cTISessionConnectionCount_Type())
hh3cTISessionConnectionCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cTISessionConnectionCount.setStatus(_A)
class _Hh3cTISessionInitiatorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,223))
_Hh3cTISessionInitiatorName_Type.__name__=_F
_Hh3cTISessionInitiatorName_Object=MibTableColumn
hh3cTISessionInitiatorName=_Hh3cTISessionInitiatorName_Object((1,3,6,1,4,1,25506,10,5,1,9,1,3),_Hh3cTISessionInitiatorName_Type())
hh3cTISessionInitiatorName.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cTISessionInitiatorName.setStatus(_A)
_Hh3cSanClientResource_ObjectIdentity=ObjectIdentity
hh3cSanClientResource=_Hh3cSanClientResource_ObjectIdentity((1,3,6,1,4,1,25506,10,5,1,10))
_Hh3cSanClientCreateIndex_Type=Integer32
_Hh3cSanClientCreateIndex_Object=MibScalar
hh3cSanClientCreateIndex=_Hh3cSanClientCreateIndex_Object((1,3,6,1,4,1,25506,10,5,1,10,1),_Hh3cSanClientCreateIndex_Type())
hh3cSanClientCreateIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cSanClientCreateIndex.setStatus(_A)
_Hh3cSanClientTable_Object=MibTable
hh3cSanClientTable=_Hh3cSanClientTable_Object((1,3,6,1,4,1,25506,10,5,1,10,2))
if mibBuilder.loadTexts:hh3cSanClientTable.setStatus(_A)
_Hh3cSanClientEntry_Object=MibTableRow
hh3cSanClientEntry=_Hh3cSanClientEntry_Object((1,3,6,1,4,1,25506,10,5,1,10,2,1))
hh3cSanClientEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:hh3cSanClientEntry.setStatus(_A)
_Hh3cSanClientId_Type=Integer32
_Hh3cSanClientId_Object=MibTableColumn
hh3cSanClientId=_Hh3cSanClientId_Object((1,3,6,1,4,1,25506,10,5,1,10,2,1,1),_Hh3cSanClientId_Type())
hh3cSanClientId.setMaxAccess(_G)
if mibBuilder.loadTexts:hh3cSanClientId.setStatus(_A)
class _Hh3cSanClientName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_Hh3cSanClientName_Type.__name__=_F
_Hh3cSanClientName_Object=MibTableColumn
hh3cSanClientName=_Hh3cSanClientName_Object((1,3,6,1,4,1,25506,10,5,1,10,2,1,2),_Hh3cSanClientName_Type())
hh3cSanClientName.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cSanClientName.setStatus(_A)
class _Hh3cSanClientType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('iscsi',1),('fc',2)))
_Hh3cSanClientType_Type.__name__=_E
_Hh3cSanClientType_Object=MibTableColumn
hh3cSanClientType=_Hh3cSanClientType_Object((1,3,6,1,4,1,25506,10,5,1,10,2,1,3),_Hh3cSanClientType_Type())
hh3cSanClientType.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cSanClientType.setStatus(_A)
_Hh3cFcInitiatorWwpnList_Type=Hh3cWwpnListType
_Hh3cFcInitiatorWwpnList_Object=MibTableColumn
hh3cFcInitiatorWwpnList=_Hh3cFcInitiatorWwpnList_Object((1,3,6,1,4,1,25506,10,5,1,10,2,1,4),_Hh3cFcInitiatorWwpnList_Type())
hh3cFcInitiatorWwpnList.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cFcInitiatorWwpnList.setStatus(_A)
class _Hh3cFcAccessMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('read',1),('write',2),(_Q,3)))
_Hh3cFcAccessMode_Type.__name__=_E
_Hh3cFcAccessMode_Object=MibTableColumn
hh3cFcAccessMode=_Hh3cFcAccessMode_Object((1,3,6,1,4,1,25506,10,5,1,10,2,1,6),_Hh3cFcAccessMode_Type())
hh3cFcAccessMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cFcAccessMode.setStatus(_A)
_Hh3cSanClientRowStatus_Type=RowStatus
_Hh3cSanClientRowStatus_Object=MibTableColumn
hh3cSanClientRowStatus=_Hh3cSanClientRowStatus_Object((1,3,6,1,4,1,25506,10,5,1,10,2,1,7),_Hh3cSanClientRowStatus_Type())
hh3cSanClientRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cSanClientRowStatus.setStatus(_A)
_Hh3cFcLogicResourceTable_Object=MibTable
hh3cFcLogicResourceTable=_Hh3cFcLogicResourceTable_Object((1,3,6,1,4,1,25506,10,5,1,11))
if mibBuilder.loadTexts:hh3cFcLogicResourceTable.setStatus(_A)
_Hh3cFcLogicResourceEntry_Object=MibTableRow
hh3cFcLogicResourceEntry=_Hh3cFcLogicResourceEntry_Object((1,3,6,1,4,1,25506,10,5,1,11,1))
hh3cFcLogicResourceEntry.setIndexNames((0,_D,_K),(0,_D,_I))
if mibBuilder.loadTexts:hh3cFcLogicResourceEntry.setStatus(_A)
class _Hh3cFcLvLun_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_Hh3cFcLvLun_Type.__name__=_E
_Hh3cFcLvLun_Object=MibTableColumn
hh3cFcLvLun=_Hh3cFcLvLun_Object((1,3,6,1,4,1,25506,10,5,1,11,1,1),_Hh3cFcLvLun_Type())
hh3cFcLvLun.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cFcLvLun.setStatus(_A)
_Hh3cFcTargetWwpnName_Type=Hh3cWwpnListType
_Hh3cFcTargetWwpnName_Object=MibTableColumn
hh3cFcTargetWwpnName=_Hh3cFcTargetWwpnName_Object((1,3,6,1,4,1,25506,10,5,1,11,1,2),_Hh3cFcTargetWwpnName_Type())
hh3cFcTargetWwpnName.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cFcTargetWwpnName.setStatus(_A)
_Hh3cFcInitiatorWwpnName_Type=Hh3cWwpnListType
_Hh3cFcInitiatorWwpnName_Object=MibTableColumn
hh3cFcInitiatorWwpnName=_Hh3cFcInitiatorWwpnName_Object((1,3,6,1,4,1,25506,10,5,1,11,1,3),_Hh3cFcInitiatorWwpnName_Type())
hh3cFcInitiatorWwpnName.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cFcInitiatorWwpnName.setStatus(_A)
_Hh3cFcLvRowStatus_Type=RowStatus
_Hh3cFcLvRowStatus_Object=MibTableColumn
hh3cFcLvRowStatus=_Hh3cFcLvRowStatus_Object((1,3,6,1,4,1,25506,10,5,1,11,1,4),_Hh3cFcLvRowStatus_Type())
hh3cFcLvRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cFcLvRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hh3cLogicVolume':hh3cLogicVolume,'hh3cLvMibObjects':hh3cLvMibObjects,'hh3cLogicResourceCapacityObject':hh3cLogicResourceCapacityObject,'hh3cLvCount':hh3cLvCount,'hh3cLvMaxSize':hh3cLvMaxSize,'hh3cTargetCount':hh3cTargetCount,'hh3cInitiatorCount':hh3cInitiatorCount,'hh3cSanClientCount':hh3cSanClientCount,'hh3cLogicVolumeResource':hh3cLogicVolumeResource,'hh3cLvCreateIndex':hh3cLvCreateIndex,'hh3cLvTable':hh3cLvTable,'hh3cLvEntry':hh3cLvEntry,_I:hh3cLvIndex,'hh3cLvName':hh3cLvName,'hh3cLvTotalSize':hh3cLvTotalSize,'hh3cLvCreateRaidUuid':hh3cLvCreateRaidUuid,'hh3cLvCreateRaidSize':hh3cLvCreateRaidSize,'hh3cLvSedInquiryStringKeep':hh3cLvSedInquiryStringKeep,'hh3cLvSedRaidUuid':hh3cLvSedRaidUuid,'hh3cLvState':hh3cLvState,'hh3cLvAssigned':hh3cLvAssigned,'hh3cLvType':hh3cLvType,'hh3cLvExtendTimes':hh3cLvExtendTimes,'hh3cLvRowStatus':hh3cLvRowStatus,'hh3cLvExtTable':hh3cLvExtTable,'hh3cLvExtEntry':hh3cLvExtEntry,_N:hh3cLvRaidUuid,'hh3cLvExtSize':hh3cLvExtSize,'hh3cLvRaidSize':hh3cLvRaidSize,'hh3cLvExtRowStatus':hh3cLvExtRowStatus,'hh3cTargetResource':hh3cTargetResource,'hh3cTargetCreateIndex':hh3cTargetCreateIndex,'hh3cTargetTable':hh3cTargetTable,'hh3cTargetEntry':hh3cTargetEntry,_H:hh3cTargetId,'hh3cTargetName':hh3cTargetName,'hh3cTargetMinLun':hh3cTargetMinLun,'hh3cTargetRowStatus':hh3cTargetRowStatus,'hh3cTargetAddressTable':hh3cTargetAddressTable,'hh3cTargetAddressEntry':hh3cTargetAddressEntry,_P:hh3cTargetIpAddress,_O:hh3cTargetIpAddrType,'hh3cTargetIpRowStatus':hh3cTargetIpRowStatus,'hh3cTargetLvAssignTable':hh3cTargetLvAssignTable,'hh3cTargetLvAssignEntry':hh3cTargetLvAssignEntry,'hh3cTargetLvLun':hh3cTargetLvLun,'hh3cTargetLvRowStatus':hh3cTargetLvRowStatus,'hh3cInitiatorResource':hh3cInitiatorResource,'hh3cInitiatorCreateIndex':hh3cInitiatorCreateIndex,'hh3cInitiatorTable':hh3cInitiatorTable,'hh3cInitiatorEntry':hh3cInitiatorEntry,_L:hh3cInitiatorId,'hh3cInitiatorName':hh3cInitiatorName,'hh3cInitiatorRowStatus':hh3cInitiatorRowStatus,'hh3cTargetInitiatorAssociateTable':hh3cTargetInitiatorAssociateTable,'hh3cTargetInitiatorAssociateEntry':hh3cTargetInitiatorAssociateEntry,'hh3cTIAccessMode':hh3cTIAccessMode,'hh3cTIChap':hh3cTIChap,'hh3cTIUserName':hh3cTIUserName,'hh3cTIPassword':hh3cTIPassword,'hh3cTIRowStatus':hh3cTIRowStatus,'hh3cTISessionTable':hh3cTISessionTable,'hh3cTISessionEntry':hh3cTISessionEntry,_R:hh3cTISessionId,'hh3cTISessionConnectionCount':hh3cTISessionConnectionCount,'hh3cTISessionInitiatorName':hh3cTISessionInitiatorName,'hh3cSanClientResource':hh3cSanClientResource,'hh3cSanClientCreateIndex':hh3cSanClientCreateIndex,'hh3cSanClientTable':hh3cSanClientTable,'hh3cSanClientEntry':hh3cSanClientEntry,_K:hh3cSanClientId,'hh3cSanClientName':hh3cSanClientName,'hh3cSanClientType':hh3cSanClientType,'hh3cFcInitiatorWwpnList':hh3cFcInitiatorWwpnList,'hh3cFcAccessMode':hh3cFcAccessMode,'hh3cSanClientRowStatus':hh3cSanClientRowStatus,'hh3cFcLogicResourceTable':hh3cFcLogicResourceTable,'hh3cFcLogicResourceEntry':hh3cFcLogicResourceEntry,'hh3cFcLvLun':hh3cFcLvLun,'hh3cFcTargetWwpnName':hh3cFcTargetWwpnName,'hh3cFcInitiatorWwpnName':hh3cFcInitiatorWwpnName,'hh3cFcLvRowStatus':hh3cFcLvRowStatus})