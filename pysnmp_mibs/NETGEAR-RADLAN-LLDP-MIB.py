_W='rlLldpRemEntry'
_V='rlLldpPortConfigEntry'
_U='rlLldpTxOverloadingIndex'
_T='rlLldpXMedLocMediaPolicyContainerIndex'
_S='rlLldpAutoAdvLocPortNum'
_R='lldpV2LocPortIfIndex'
_Q='LLDP-V2-MIB'
_P='rlLldpTxOverloadingPortNum'
_O='PortList'
_N='rndErrorSeverity'
_M='rndErrorDesc'
_L='lldpRemTimeMark'
_K='lldpRemLocalPortNum'
_J='lldpRemIndex'
_I='not-accessible'
_H='TruthValue'
_G='NETGEAR-RADLAN-DEVICEPARAMS-MIB'
_F='Integer32'
_E='LLDP-MIB'
_D='NETGEAR-RADLAN-LLDP-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Dscp,=mibBuilder.importSymbols('DIFFSERV-DSCP-TC','Dscp')
AddressFamilyNumbers,=mibBuilder.importSymbols('IANA-ADDRESS-FAMILY-NUMBERS-MIB','AddressFamilyNumbers')
LldpXMedCapabilities,=mibBuilder.importSymbols('LLDP-EXT-MED-MIB','LldpXMedCapabilities')
LldpManAddress,LldpPortList,LldpPortNumber,lldpPortConfigEntry,lldpRemEntry,lldpRemIndex,lldpRemLocalPortNum,lldpRemTimeMark=mibBuilder.importSymbols(_E,'LldpManAddress','LldpPortList','LldpPortNumber','lldpPortConfigEntry','lldpRemEntry',_J,_K,_L)
lldpV2LocPortIfIndex,lldpV2RemLocalIfIndex=mibBuilder.importSymbols(_Q,_R,'lldpV2RemLocalIfIndex')
rndErrorDesc,rndErrorSeverity=mibBuilder.importSymbols(_G,_M,_N)
rnd,rndNotifications=mibBuilder.importSymbols('NETGEAR-RADLAN-MIB','rnd','rndNotifications')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_O)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_H)
rlLldp=ModuleIdentity((1,3,6,1,4,1,4526,17,110))
if mibBuilder.loadTexts:rlLldp.setRevisions(('2005-06-20 00:00',))
class PolicyNumber(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32768))
class PolicyContainerAppType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('unknown',0),('voice',1),('voiceSignaling',2),('guestVoice',3),('guestVoiceSignaling',4),('softPhoneVoice',5),('videoconferencing',6),('streamingVideo',7),('videoSignaling',8)))
class PolicyAppVoiceUpdateMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('manual',0),('auto',1)))
_RlLldpObjects_ObjectIdentity=ObjectIdentity
rlLldpObjects=_RlLldpObjects_ObjectIdentity((1,3,6,1,4,1,4526,17,110,1))
_RlLldpConfig_ObjectIdentity=ObjectIdentity
rlLldpConfig=_RlLldpConfig_ObjectIdentity((1,3,6,1,4,1,4526,17,110,1,1))
_RlLldpEnabled_Type=TruthValue
_RlLldpEnabled_Object=MibScalar
rlLldpEnabled=_RlLldpEnabled_Object((1,3,6,1,4,1,4526,17,110,1,1,1),_RlLldpEnabled_Type())
rlLldpEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:rlLldpEnabled.setStatus(_A)
class _RlLldpClearRx_Type(PortList):defaultHexValue=''
_RlLldpClearRx_Type.__name__=_O
_RlLldpClearRx_Object=MibScalar
rlLldpClearRx=_RlLldpClearRx_Object((1,3,6,1,4,1,4526,17,110,1,1,2),_RlLldpClearRx_Type())
rlLldpClearRx.setMaxAccess(_C)
if mibBuilder.loadTexts:rlLldpClearRx.setStatus(_A)
class _RlLldpDuMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('filtering',1),('flooding',2)))
_RlLldpDuMode_Type.__name__=_F
_RlLldpDuMode_Object=MibScalar
rlLldpDuMode=_RlLldpDuMode_Object((1,3,6,1,4,1,4526,17,110,1,1,3),_RlLldpDuMode_Type())
rlLldpDuMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rlLldpDuMode.setStatus(_A)
_RlLldpAutoAdvLocPortManAddrTable_Object=MibTable
rlLldpAutoAdvLocPortManAddrTable=_RlLldpAutoAdvLocPortManAddrTable_Object((1,3,6,1,4,1,4526,17,110,1,1,4))
if mibBuilder.loadTexts:rlLldpAutoAdvLocPortManAddrTable.setStatus(_A)
_RlLldpAutoAdvLocPortManAddrEntry_Object=MibTableRow
rlLldpAutoAdvLocPortManAddrEntry=_RlLldpAutoAdvLocPortManAddrEntry_Object((1,3,6,1,4,1,4526,17,110,1,1,4,1))
rlLldpAutoAdvLocPortManAddrEntry.setIndexNames((0,_D,_S))
if mibBuilder.loadTexts:rlLldpAutoAdvLocPortManAddrEntry.setStatus(_A)
_RlLldpAutoAdvLocPortNum_Type=LldpPortNumber
_RlLldpAutoAdvLocPortNum_Object=MibTableColumn
rlLldpAutoAdvLocPortNum=_RlLldpAutoAdvLocPortNum_Object((1,3,6,1,4,1,4526,17,110,1,1,4,1,1),_RlLldpAutoAdvLocPortNum_Type())
rlLldpAutoAdvLocPortNum.setMaxAccess(_I)
if mibBuilder.loadTexts:rlLldpAutoAdvLocPortNum.setStatus(_A)
class _RlLldpAutoAdvManAddrOwnerIfId_Type(Integer32):defaultValue=0
_RlLldpAutoAdvManAddrOwnerIfId_Type.__name__=_F
_RlLldpAutoAdvManAddrOwnerIfId_Object=MibTableColumn
rlLldpAutoAdvManAddrOwnerIfId=_RlLldpAutoAdvManAddrOwnerIfId_Object((1,3,6,1,4,1,4526,17,110,1,1,4,1,2),_RlLldpAutoAdvManAddrOwnerIfId_Type())
rlLldpAutoAdvManAddrOwnerIfId.setMaxAccess(_C)
if mibBuilder.loadTexts:rlLldpAutoAdvManAddrOwnerIfId.setStatus(_A)
class _RlLldpAutoAdvManAddrNone_Type(TruthValue):defaultValue=2
_RlLldpAutoAdvManAddrNone_Type.__name__=_H
_RlLldpAutoAdvManAddrNone_Object=MibTableColumn
rlLldpAutoAdvManAddrNone=_RlLldpAutoAdvManAddrNone_Object((1,3,6,1,4,1,4526,17,110,1,1,4,1,3),_RlLldpAutoAdvManAddrNone_Type())
rlLldpAutoAdvManAddrNone.setMaxAccess(_C)
if mibBuilder.loadTexts:rlLldpAutoAdvManAddrNone.setStatus(_A)
_RlLldpAutoAdvManAddrSubtype_Type=AddressFamilyNumbers
_RlLldpAutoAdvManAddrSubtype_Object=MibTableColumn
rlLldpAutoAdvManAddrSubtype=_RlLldpAutoAdvManAddrSubtype_Object((1,3,6,1,4,1,4526,17,110,1,1,4,1,4),_RlLldpAutoAdvManAddrSubtype_Type())
rlLldpAutoAdvManAddrSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLldpAutoAdvManAddrSubtype.setStatus(_A)
_RlLldpAutoAdvManAddr_Type=LldpManAddress
_RlLldpAutoAdvManAddr_Object=MibTableColumn
rlLldpAutoAdvManAddr=_RlLldpAutoAdvManAddr_Object((1,3,6,1,4,1,4526,17,110,1,1,4,1,5),_RlLldpAutoAdvManAddr_Type())
rlLldpAutoAdvManAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLldpAutoAdvManAddr.setStatus(_A)
_RlLldpAutoAdvPortsStatus_Type=RowStatus
_RlLldpAutoAdvPortsStatus_Object=MibTableColumn
rlLldpAutoAdvPortsStatus=_RlLldpAutoAdvPortsStatus_Object((1,3,6,1,4,1,4526,17,110,1,1,4,1,6),_RlLldpAutoAdvPortsStatus_Type())
rlLldpAutoAdvPortsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlLldpAutoAdvPortsStatus.setStatus(_A)
class _RlLldpChassisIdSubtype_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(4,7)));namedValues=NamedValues(*(('macAddress',4),('local',7)))
_RlLldpChassisIdSubtype_Type.__name__=_F
_RlLldpChassisIdSubtype_Object=MibScalar
rlLldpChassisIdSubtype=_RlLldpChassisIdSubtype_Object((1,3,6,1,4,1,4526,17,110,1,1,5),_RlLldpChassisIdSubtype_Type())
rlLldpChassisIdSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:rlLldpChassisIdSubtype.setStatus(_A)
_RlLldpPortConfigTable_Object=MibTable
rlLldpPortConfigTable=_RlLldpPortConfigTable_Object((1,3,6,1,4,1,4526,17,110,1,1,6))
if mibBuilder.loadTexts:rlLldpPortConfigTable.setStatus(_A)
_RlLldpPortConfigEntry_Object=MibTableRow
rlLldpPortConfigEntry=_RlLldpPortConfigEntry_Object((1,3,6,1,4,1,4526,17,110,1,1,6,1))
if mibBuilder.loadTexts:rlLldpPortConfigEntry.setStatus(_A)
class _RlLldpPortConfig4wireTxEnable_Type(TruthValue):defaultValue=2
_RlLldpPortConfig4wireTxEnable_Type.__name__=_H
_RlLldpPortConfig4wireTxEnable_Object=MibTableColumn
rlLldpPortConfig4wireTxEnable=_RlLldpPortConfig4wireTxEnable_Object((1,3,6,1,4,1,4526,17,110,1,1,6,1,1),_RlLldpPortConfig4wireTxEnable_Type())
rlLldpPortConfig4wireTxEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlLldpPortConfig4wireTxEnable.setStatus(_A)
_RlLldpXMedConfig_ObjectIdentity=ObjectIdentity
rlLldpXMedConfig=_RlLldpXMedConfig_ObjectIdentity((1,3,6,1,4,1,4526,17,110,1,2))
_RlLldpXMedLocMediaPolicyContainerTable_Object=MibTable
rlLldpXMedLocMediaPolicyContainerTable=_RlLldpXMedLocMediaPolicyContainerTable_Object((1,3,6,1,4,1,4526,17,110,1,2,1))
if mibBuilder.loadTexts:rlLldpXMedLocMediaPolicyContainerTable.setStatus(_A)
_RlLldpXMedLocMediaPolicyContainerEntry_Object=MibTableRow
rlLldpXMedLocMediaPolicyContainerEntry=_RlLldpXMedLocMediaPolicyContainerEntry_Object((1,3,6,1,4,1,4526,17,110,1,2,1,1))
rlLldpXMedLocMediaPolicyContainerEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:rlLldpXMedLocMediaPolicyContainerEntry.setStatus(_A)
_RlLldpXMedLocMediaPolicyContainerIndex_Type=PolicyNumber
_RlLldpXMedLocMediaPolicyContainerIndex_Object=MibTableColumn
rlLldpXMedLocMediaPolicyContainerIndex=_RlLldpXMedLocMediaPolicyContainerIndex_Object((1,3,6,1,4,1,4526,17,110,1,2,1,1,1),_RlLldpXMedLocMediaPolicyContainerIndex_Type())
rlLldpXMedLocMediaPolicyContainerIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:rlLldpXMedLocMediaPolicyContainerIndex.setStatus(_A)
_RlLldpXMedLocMediaPolicyContainerAppType_Type=PolicyContainerAppType
_RlLldpXMedLocMediaPolicyContainerAppType_Object=MibTableColumn
rlLldpXMedLocMediaPolicyContainerAppType=_RlLldpXMedLocMediaPolicyContainerAppType_Object((1,3,6,1,4,1,4526,17,110,1,2,1,1,2),_RlLldpXMedLocMediaPolicyContainerAppType_Type())
rlLldpXMedLocMediaPolicyContainerAppType.setMaxAccess(_C)
if mibBuilder.loadTexts:rlLldpXMedLocMediaPolicyContainerAppType.setStatus(_A)
class _RlLldpXMedLocMediaPolicyContainerVlanID_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4094),ValueRangeConstraint(4095,4095))
_RlLldpXMedLocMediaPolicyContainerVlanID_Type.__name__=_F
_RlLldpXMedLocMediaPolicyContainerVlanID_Object=MibTableColumn
rlLldpXMedLocMediaPolicyContainerVlanID=_RlLldpXMedLocMediaPolicyContainerVlanID_Object((1,3,6,1,4,1,4526,17,110,1,2,1,1,3),_RlLldpXMedLocMediaPolicyContainerVlanID_Type())
rlLldpXMedLocMediaPolicyContainerVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:rlLldpXMedLocMediaPolicyContainerVlanID.setStatus(_A)
class _RlLldpXMedLocMediaPolicyContainerPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RlLldpXMedLocMediaPolicyContainerPriority_Type.__name__=_F
_RlLldpXMedLocMediaPolicyContainerPriority_Object=MibTableColumn
rlLldpXMedLocMediaPolicyContainerPriority=_RlLldpXMedLocMediaPolicyContainerPriority_Object((1,3,6,1,4,1,4526,17,110,1,2,1,1,4),_RlLldpXMedLocMediaPolicyContainerPriority_Type())
rlLldpXMedLocMediaPolicyContainerPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:rlLldpXMedLocMediaPolicyContainerPriority.setStatus(_A)
class _RlLldpXMedLocMediaPolicyContainerDscp_Type(Dscp):defaultValue=0
_RlLldpXMedLocMediaPolicyContainerDscp_Type.__name__='Dscp'
_RlLldpXMedLocMediaPolicyContainerDscp_Object=MibTableColumn
rlLldpXMedLocMediaPolicyContainerDscp=_RlLldpXMedLocMediaPolicyContainerDscp_Object((1,3,6,1,4,1,4526,17,110,1,2,1,1,5),_RlLldpXMedLocMediaPolicyContainerDscp_Type())
rlLldpXMedLocMediaPolicyContainerDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:rlLldpXMedLocMediaPolicyContainerDscp.setStatus(_A)
class _RlLldpXMedLocMediaPolicyContainerUnknown_Type(TruthValue):defaultValue=2
_RlLldpXMedLocMediaPolicyContainerUnknown_Type.__name__=_H
_RlLldpXMedLocMediaPolicyContainerUnknown_Object=MibTableColumn
rlLldpXMedLocMediaPolicyContainerUnknown=_RlLldpXMedLocMediaPolicyContainerUnknown_Object((1,3,6,1,4,1,4526,17,110,1,2,1,1,6),_RlLldpXMedLocMediaPolicyContainerUnknown_Type())
rlLldpXMedLocMediaPolicyContainerUnknown.setMaxAccess(_C)
if mibBuilder.loadTexts:rlLldpXMedLocMediaPolicyContainerUnknown.setStatus(_A)
class _RlLldpXMedLocMediaPolicyContainerTagged_Type(TruthValue):defaultValue=2
_RlLldpXMedLocMediaPolicyContainerTagged_Type.__name__=_H
_RlLldpXMedLocMediaPolicyContainerTagged_Object=MibTableColumn
rlLldpXMedLocMediaPolicyContainerTagged=_RlLldpXMedLocMediaPolicyContainerTagged_Object((1,3,6,1,4,1,4526,17,110,1,2,1,1,7),_RlLldpXMedLocMediaPolicyContainerTagged_Type())
rlLldpXMedLocMediaPolicyContainerTagged.setMaxAccess(_C)
if mibBuilder.loadTexts:rlLldpXMedLocMediaPolicyContainerTagged.setStatus(_A)
class _RlLldpXMedLocMediaPolicyContainerPorts_Type(PortList):defaultHexValue=''
_RlLldpXMedLocMediaPolicyContainerPorts_Type.__name__=_O
_RlLldpXMedLocMediaPolicyContainerPorts_Object=MibTableColumn
rlLldpXMedLocMediaPolicyContainerPorts=_RlLldpXMedLocMediaPolicyContainerPorts_Object((1,3,6,1,4,1,4526,17,110,1,2,1,1,8),_RlLldpXMedLocMediaPolicyContainerPorts_Type())
rlLldpXMedLocMediaPolicyContainerPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:rlLldpXMedLocMediaPolicyContainerPorts.setStatus(_A)
_RlLldpXMedLocMediaPolicyContainerRowStatus_Type=RowStatus
_RlLldpXMedLocMediaPolicyContainerRowStatus_Object=MibTableColumn
rlLldpXMedLocMediaPolicyContainerRowStatus=_RlLldpXMedLocMediaPolicyContainerRowStatus_Object((1,3,6,1,4,1,4526,17,110,1,2,1,1,9),_RlLldpXMedLocMediaPolicyContainerRowStatus_Type())
rlLldpXMedLocMediaPolicyContainerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlLldpXMedLocMediaPolicyContainerRowStatus.setStatus(_A)
_RlLldpXMedNetPolVoiceUpdateMode_Type=PolicyAppVoiceUpdateMode
_RlLldpXMedNetPolVoiceUpdateMode_Object=MibScalar
rlLldpXMedNetPolVoiceUpdateMode=_RlLldpXMedNetPolVoiceUpdateMode_Object((1,3,6,1,4,1,4526,17,110,1,2,2),_RlLldpXMedNetPolVoiceUpdateMode_Type())
rlLldpXMedNetPolVoiceUpdateMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rlLldpXMedNetPolVoiceUpdateMode.setStatus(_A)
_RlLldpTLVsTxOverload_ObjectIdentity=ObjectIdentity
rlLldpTLVsTxOverload=_RlLldpTLVsTxOverload_ObjectIdentity((1,3,6,1,4,1,4526,17,110,1,3))
_RlLldpTLVsTxOverloadingTable_Object=MibTable
rlLldpTLVsTxOverloadingTable=_RlLldpTLVsTxOverloadingTable_Object((1,3,6,1,4,1,4526,17,110,1,3,1))
if mibBuilder.loadTexts:rlLldpTLVsTxOverloadingTable.setStatus(_A)
_RlLldpTLVsTxOverloadingEntry_Object=MibTableRow
rlLldpTLVsTxOverloadingEntry=_RlLldpTLVsTxOverloadingEntry_Object((1,3,6,1,4,1,4526,17,110,1,3,1,1))
rlLldpTLVsTxOverloadingEntry.setIndexNames((0,_D,_P),(0,_D,_U))
if mibBuilder.loadTexts:rlLldpTLVsTxOverloadingEntry.setStatus(_A)
_RlLldpTxOverloadingPortNum_Type=LldpPortNumber
_RlLldpTxOverloadingPortNum_Object=MibTableColumn
rlLldpTxOverloadingPortNum=_RlLldpTxOverloadingPortNum_Object((1,3,6,1,4,1,4526,17,110,1,3,1,1,1),_RlLldpTxOverloadingPortNum_Type())
rlLldpTxOverloadingPortNum.setMaxAccess(_I)
if mibBuilder.loadTexts:rlLldpTxOverloadingPortNum.setStatus(_A)
_RlLldpTxOverloadingIndex_Type=Unsigned32
_RlLldpTxOverloadingIndex_Object=MibTableColumn
rlLldpTxOverloadingIndex=_RlLldpTxOverloadingIndex_Object((1,3,6,1,4,1,4526,17,110,1,3,1,1,2),_RlLldpTxOverloadingIndex_Type())
rlLldpTxOverloadingIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:rlLldpTxOverloadingIndex.setStatus(_A)
class _RlLldpTxOverloadingGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('mandatory',1),('optional',2),('medCap',3),('medLocation',4),('medNetPolicy',5),('medPoe',6),('medInventory',7),('xDot3',8),('xDot1',9),('dcbx',10),('cisco',11)))
_RlLldpTxOverloadingGroupId_Type.__name__=_F
_RlLldpTxOverloadingGroupId_Object=MibTableColumn
rlLldpTxOverloadingGroupId=_RlLldpTxOverloadingGroupId_Object((1,3,6,1,4,1,4526,17,110,1,3,1,1,3),_RlLldpTxOverloadingGroupId_Type())
rlLldpTxOverloadingGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLldpTxOverloadingGroupId.setStatus(_A)
_RlLldpTLVsTxSize_Type=Unsigned32
_RlLldpTLVsTxSize_Object=MibTableColumn
rlLldpTLVsTxSize=_RlLldpTLVsTxSize_Object((1,3,6,1,4,1,4526,17,110,1,3,1,1,4),_RlLldpTLVsTxSize_Type())
rlLldpTLVsTxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLldpTLVsTxSize.setStatus(_A)
_RlLldpTLVsTxGroupOverloading_Type=TruthValue
_RlLldpTLVsTxGroupOverloading_Object=MibTableColumn
rlLldpTLVsTxGroupOverloading=_RlLldpTLVsTxGroupOverloading_Object((1,3,6,1,4,1,4526,17,110,1,3,1,1,5),_RlLldpTLVsTxGroupOverloading_Type())
rlLldpTLVsTxGroupOverloading.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLldpTLVsTxGroupOverloading.setStatus(_A)
_RlLldpTLVsTxLeftSize_Type=Unsigned32
_RlLldpTLVsTxLeftSize_Object=MibTableColumn
rlLldpTLVsTxLeftSize=_RlLldpTLVsTxLeftSize_Object((1,3,6,1,4,1,4526,17,110,1,3,1,1,6),_RlLldpTLVsTxLeftSize_Type())
rlLldpTLVsTxLeftSize.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLldpTLVsTxLeftSize.setStatus(_A)
_RlLldpTLVsTxOverloadingSizeTable_Object=MibTable
rlLldpTLVsTxOverloadingSizeTable=_RlLldpTLVsTxOverloadingSizeTable_Object((1,3,6,1,4,1,4526,17,110,1,3,2))
if mibBuilder.loadTexts:rlLldpTLVsTxOverloadingSizeTable.setStatus(_A)
_RlLldpTLVsTxOverloadingSizeEntry_Object=MibTableRow
rlLldpTLVsTxOverloadingSizeEntry=_RlLldpTLVsTxOverloadingSizeEntry_Object((1,3,6,1,4,1,4526,17,110,1,3,2,1))
rlLldpTLVsTxOverloadingSizeEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:rlLldpTLVsTxOverloadingSizeEntry.setStatus(_A)
_RlLldpTotalTLVsTxSize_Type=Unsigned32
_RlLldpTotalTLVsTxSize_Object=MibTableColumn
rlLldpTotalTLVsTxSize=_RlLldpTotalTLVsTxSize_Object((1,3,6,1,4,1,4526,17,110,1,3,2,1,2),_RlLldpTotalTLVsTxSize_Type())
rlLldpTotalTLVsTxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLldpTotalTLVsTxSize.setStatus(_A)
_RlLldpTLVsTxOverloading_Type=TruthValue
_RlLldpTLVsTxOverloading_Object=MibTableColumn
rlLldpTLVsTxOverloading=_RlLldpTLVsTxOverloading_Object((1,3,6,1,4,1,4526,17,110,1,3,2,1,3),_RlLldpTLVsTxOverloading_Type())
rlLldpTLVsTxOverloading.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLldpTLVsTxOverloading.setStatus(_A)
_RlLldpLeftTLVsTxSize_Type=Unsigned32
_RlLldpLeftTLVsTxSize_Object=MibTableColumn
rlLldpLeftTLVsTxSize=_RlLldpLeftTLVsTxSize_Object((1,3,6,1,4,1,4526,17,110,1,3,2,1,4),_RlLldpLeftTLVsTxSize_Type())
rlLldpLeftTLVsTxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLldpLeftTLVsTxSize.setStatus(_A)
_RlLldpTLVsTxOverloadingPorts_Type=PortList
_RlLldpTLVsTxOverloadingPorts_Object=MibScalar
rlLldpTLVsTxOverloadingPorts=_RlLldpTLVsTxOverloadingPorts_Object((1,3,6,1,4,1,4526,17,110,1,3,3),_RlLldpTLVsTxOverloadingPorts_Type())
rlLldpTLVsTxOverloadingPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLldpTLVsTxOverloadingPorts.setStatus(_A)
_RlLldpRemStatus_ObjectIdentity=ObjectIdentity
rlLldpRemStatus=_RlLldpRemStatus_ObjectIdentity((1,3,6,1,4,1,4526,17,110,1,4))
_RlLldpRemTtlTable_Object=MibTable
rlLldpRemTtlTable=_RlLldpRemTtlTable_Object((1,3,6,1,4,1,4526,17,110,1,4,1))
if mibBuilder.loadTexts:rlLldpRemTtlTable.setStatus(_A)
_RlLldpRemTtlEntry_Object=MibTableRow
rlLldpRemTtlEntry=_RlLldpRemTtlEntry_Object((1,3,6,1,4,1,4526,17,110,1,4,1,1))
rlLldpRemTtlEntry.setIndexNames((0,_E,_L),(0,_E,_K),(0,_E,_J))
if mibBuilder.loadTexts:rlLldpRemTtlEntry.setStatus(_A)
_RlLldpRemTtl_Type=Unsigned32
_RlLldpRemTtl_Object=MibTableColumn
rlLldpRemTtl=_RlLldpRemTtl_Object((1,3,6,1,4,1,4526,17,110,1,4,1,1,1),_RlLldpRemTtl_Type())
rlLldpRemTtl.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLldpRemTtl.setStatus(_A)
if mibBuilder.loadTexts:rlLldpRemTtl.setUnits('seconds')
_RlLldpLocalSystemData_ObjectIdentity=ObjectIdentity
rlLldpLocalSystemData=_RlLldpLocalSystemData_ObjectIdentity((1,3,6,1,4,1,4526,17,110,1,5))
_RlLldpLoc4WirePowerTable_Object=MibTable
rlLldpLoc4WirePowerTable=_RlLldpLoc4WirePowerTable_Object((1,3,6,1,4,1,4526,17,110,1,5,1))
if mibBuilder.loadTexts:rlLldpLoc4WirePowerTable.setStatus(_A)
_RlLldpLoc4WirePowerEntry_Object=MibTableRow
rlLldpLoc4WirePowerEntry=_RlLldpLoc4WirePowerEntry_Object((1,3,6,1,4,1,4526,17,110,1,5,1,1))
rlLldpLoc4WirePowerEntry.setIndexNames((0,_Q,_R))
if mibBuilder.loadTexts:rlLldpLoc4WirePowerEntry.setStatus(_A)
_RlLldpLoc4WirePowerSupported_Type=TruthValue
_RlLldpLoc4WirePowerSupported_Object=MibTableColumn
rlLldpLoc4WirePowerSupported=_RlLldpLoc4WirePowerSupported_Object((1,3,6,1,4,1,4526,17,110,1,5,1,1,1),_RlLldpLoc4WirePowerSupported_Type())
rlLldpLoc4WirePowerSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLldpLoc4WirePowerSupported.setStatus(_A)
_RlLldpLoc4WirePowerSpPairDetClasReq_Type=TruthValue
_RlLldpLoc4WirePowerSpPairDetClasReq_Object=MibTableColumn
rlLldpLoc4WirePowerSpPairDetClasReq=_RlLldpLoc4WirePowerSpPairDetClasReq_Object((1,3,6,1,4,1,4526,17,110,1,5,1,1,2),_RlLldpLoc4WirePowerSpPairDetClasReq_Type())
rlLldpLoc4WirePowerSpPairDetClasReq.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLldpLoc4WirePowerSpPairDetClasReq.setStatus(_A)
_RlLldpLoc4WirePowerPdSpPairDesStEn_Type=TruthValue
_RlLldpLoc4WirePowerPdSpPairDesStEn_Object=MibTableColumn
rlLldpLoc4WirePowerPdSpPairDesStEn=_RlLldpLoc4WirePowerPdSpPairDesStEn_Object((1,3,6,1,4,1,4526,17,110,1,5,1,1,3),_RlLldpLoc4WirePowerPdSpPairDesStEn_Type())
rlLldpLoc4WirePowerPdSpPairDesStEn.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLldpLoc4WirePowerPdSpPairDesStEn.setStatus(_A)
_RlLldpLoc4WirePowerPseSpPairOpStEn_Type=TruthValue
_RlLldpLoc4WirePowerPseSpPairOpStEn_Object=MibTableColumn
rlLldpLoc4WirePowerPseSpPairOpStEn=_RlLldpLoc4WirePowerPseSpPairOpStEn_Object((1,3,6,1,4,1,4526,17,110,1,5,1,1,4),_RlLldpLoc4WirePowerPseSpPairOpStEn_Type())
rlLldpLoc4WirePowerPseSpPairOpStEn.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLldpLoc4WirePowerPseSpPairOpStEn.setStatus(_A)
_RlLldpRemoteSystemsData_ObjectIdentity=ObjectIdentity
rlLldpRemoteSystemsData=_RlLldpRemoteSystemsData_ObjectIdentity((1,3,6,1,4,1,4526,17,110,1,6))
_RlLldpRem4WirePowerTable_Object=MibTable
rlLldpRem4WirePowerTable=_RlLldpRem4WirePowerTable_Object((1,3,6,1,4,1,4526,17,110,1,6,1))
if mibBuilder.loadTexts:rlLldpRem4WirePowerTable.setStatus(_A)
_RlLldpRem4WirePowerEntry_Object=MibTableRow
rlLldpRem4WirePowerEntry=_RlLldpRem4WirePowerEntry_Object((1,3,6,1,4,1,4526,17,110,1,6,1,1))
rlLldpRem4WirePowerEntry.setIndexNames((0,_E,_L),(0,_E,_K),(0,_E,_J))
if mibBuilder.loadTexts:rlLldpRem4WirePowerEntry.setStatus(_A)
_RlLldpRem4WirePowerSupported_Type=TruthValue
_RlLldpRem4WirePowerSupported_Object=MibTableColumn
rlLldpRem4WirePowerSupported=_RlLldpRem4WirePowerSupported_Object((1,3,6,1,4,1,4526,17,110,1,6,1,1,1),_RlLldpRem4WirePowerSupported_Type())
rlLldpRem4WirePowerSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLldpRem4WirePowerSupported.setStatus(_A)
_RlLldpRem4WirePowerSpPairDetClasReq_Type=TruthValue
_RlLldpRem4WirePowerSpPairDetClasReq_Object=MibTableColumn
rlLldpRem4WirePowerSpPairDetClasReq=_RlLldpRem4WirePowerSpPairDetClasReq_Object((1,3,6,1,4,1,4526,17,110,1,6,1,1,2),_RlLldpRem4WirePowerSpPairDetClasReq_Type())
rlLldpRem4WirePowerSpPairDetClasReq.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLldpRem4WirePowerSpPairDetClasReq.setStatus(_A)
_RlLldpRem4WirePowerPdSpPairDesStEn_Type=TruthValue
_RlLldpRem4WirePowerPdSpPairDesStEn_Object=MibTableColumn
rlLldpRem4WirePowerPdSpPairDesStEn=_RlLldpRem4WirePowerPdSpPairDesStEn_Object((1,3,6,1,4,1,4526,17,110,1,6,1,1,3),_RlLldpRem4WirePowerPdSpPairDesStEn_Type())
rlLldpRem4WirePowerPdSpPairDesStEn.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLldpRem4WirePowerPdSpPairDesStEn.setStatus(_A)
_RlLldpRem4WirePowerPseSpPairOpStEn_Type=TruthValue
_RlLldpRem4WirePowerPseSpPairOpStEn_Object=MibTableColumn
rlLldpRem4WirePowerPseSpPairOpStEn=_RlLldpRem4WirePowerPseSpPairOpStEn_Object((1,3,6,1,4,1,4526,17,110,1,6,1,1,4),_RlLldpRem4WirePowerPseSpPairOpStEn_Type())
rlLldpRem4WirePowerPseSpPairOpStEn.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLldpRem4WirePowerPseSpPairOpStEn.setStatus(_A)
_RlLldpRemTable_Object=MibTable
rlLldpRemTable=_RlLldpRemTable_Object((1,3,6,1,4,1,4526,17,110,1,6,2))
if mibBuilder.loadTexts:rlLldpRemTable.setStatus(_A)
_RlLldpRemEntry_Object=MibTableRow
rlLldpRemEntry=_RlLldpRemEntry_Object((1,3,6,1,4,1,4526,17,110,1,6,2,1))
if mibBuilder.loadTexts:rlLldpRemEntry.setStatus(_A)
_RlLldpRemSrcMacAddr_Type=MacAddress
_RlLldpRemSrcMacAddr_Object=MibTableColumn
rlLldpRemSrcMacAddr=_RlLldpRemSrcMacAddr_Object((1,3,6,1,4,1,4526,17,110,1,6,2,1,1),_RlLldpRemSrcMacAddr_Type())
rlLldpRemSrcMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLldpRemSrcMacAddr.setStatus(_A)
_RlLldpRemActiveStation_Type=TruthValue
_RlLldpRemActiveStation_Object=MibTableColumn
rlLldpRemActiveStation=_RlLldpRemActiveStation_Object((1,3,6,1,4,1,4526,17,110,1,6,2,1,2),_RlLldpRemActiveStation_Type())
rlLldpRemActiveStation.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLldpRemActiveStation.setStatus(_A)
lldpPortConfigEntry.registerAugmentions((_D,_V))
rlLldpPortConfigEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())
lldpRemEntry.registerAugmentions((_D,_W))
rlLldpRemEntry.setIndexNames(*lldpRemEntry.getIndexNames())
rlLldpTLVsTxOverloadingStateEnterTrap=NotificationType((1,3,6,1,4,1,4526,17,0,209))
rlLldpTLVsTxOverloadingStateEnterTrap.setObjects(*((_G,_M),(_G,_N)))
if mibBuilder.loadTexts:rlLldpTLVsTxOverloadingStateEnterTrap.setStatus(_A)
rlLldpTLVsTxOverloadingStateExitTrap=NotificationType((1,3,6,1,4,1,4526,17,0,210))
rlLldpTLVsTxOverloadingStateExitTrap.setObjects(*((_G,_M),(_G,_N)))
if mibBuilder.loadTexts:rlLldpTLVsTxOverloadingStateExitTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'PolicyNumber':PolicyNumber,'PolicyContainerAppType':PolicyContainerAppType,'PolicyAppVoiceUpdateMode':PolicyAppVoiceUpdateMode,'rlLldpTLVsTxOverloadingStateEnterTrap':rlLldpTLVsTxOverloadingStateEnterTrap,'rlLldpTLVsTxOverloadingStateExitTrap':rlLldpTLVsTxOverloadingStateExitTrap,'rlLldp':rlLldp,'rlLldpObjects':rlLldpObjects,'rlLldpConfig':rlLldpConfig,'rlLldpEnabled':rlLldpEnabled,'rlLldpClearRx':rlLldpClearRx,'rlLldpDuMode':rlLldpDuMode,'rlLldpAutoAdvLocPortManAddrTable':rlLldpAutoAdvLocPortManAddrTable,'rlLldpAutoAdvLocPortManAddrEntry':rlLldpAutoAdvLocPortManAddrEntry,_S:rlLldpAutoAdvLocPortNum,'rlLldpAutoAdvManAddrOwnerIfId':rlLldpAutoAdvManAddrOwnerIfId,'rlLldpAutoAdvManAddrNone':rlLldpAutoAdvManAddrNone,'rlLldpAutoAdvManAddrSubtype':rlLldpAutoAdvManAddrSubtype,'rlLldpAutoAdvManAddr':rlLldpAutoAdvManAddr,'rlLldpAutoAdvPortsStatus':rlLldpAutoAdvPortsStatus,'rlLldpChassisIdSubtype':rlLldpChassisIdSubtype,'rlLldpPortConfigTable':rlLldpPortConfigTable,_V:rlLldpPortConfigEntry,'rlLldpPortConfig4wireTxEnable':rlLldpPortConfig4wireTxEnable,'rlLldpXMedConfig':rlLldpXMedConfig,'rlLldpXMedLocMediaPolicyContainerTable':rlLldpXMedLocMediaPolicyContainerTable,'rlLldpXMedLocMediaPolicyContainerEntry':rlLldpXMedLocMediaPolicyContainerEntry,_T:rlLldpXMedLocMediaPolicyContainerIndex,'rlLldpXMedLocMediaPolicyContainerAppType':rlLldpXMedLocMediaPolicyContainerAppType,'rlLldpXMedLocMediaPolicyContainerVlanID':rlLldpXMedLocMediaPolicyContainerVlanID,'rlLldpXMedLocMediaPolicyContainerPriority':rlLldpXMedLocMediaPolicyContainerPriority,'rlLldpXMedLocMediaPolicyContainerDscp':rlLldpXMedLocMediaPolicyContainerDscp,'rlLldpXMedLocMediaPolicyContainerUnknown':rlLldpXMedLocMediaPolicyContainerUnknown,'rlLldpXMedLocMediaPolicyContainerTagged':rlLldpXMedLocMediaPolicyContainerTagged,'rlLldpXMedLocMediaPolicyContainerPorts':rlLldpXMedLocMediaPolicyContainerPorts,'rlLldpXMedLocMediaPolicyContainerRowStatus':rlLldpXMedLocMediaPolicyContainerRowStatus,'rlLldpXMedNetPolVoiceUpdateMode':rlLldpXMedNetPolVoiceUpdateMode,'rlLldpTLVsTxOverload':rlLldpTLVsTxOverload,'rlLldpTLVsTxOverloadingTable':rlLldpTLVsTxOverloadingTable,'rlLldpTLVsTxOverloadingEntry':rlLldpTLVsTxOverloadingEntry,_P:rlLldpTxOverloadingPortNum,_U:rlLldpTxOverloadingIndex,'rlLldpTxOverloadingGroupId':rlLldpTxOverloadingGroupId,'rlLldpTLVsTxSize':rlLldpTLVsTxSize,'rlLldpTLVsTxGroupOverloading':rlLldpTLVsTxGroupOverloading,'rlLldpTLVsTxLeftSize':rlLldpTLVsTxLeftSize,'rlLldpTLVsTxOverloadingSizeTable':rlLldpTLVsTxOverloadingSizeTable,'rlLldpTLVsTxOverloadingSizeEntry':rlLldpTLVsTxOverloadingSizeEntry,'rlLldpTotalTLVsTxSize':rlLldpTotalTLVsTxSize,'rlLldpTLVsTxOverloading':rlLldpTLVsTxOverloading,'rlLldpLeftTLVsTxSize':rlLldpLeftTLVsTxSize,'rlLldpTLVsTxOverloadingPorts':rlLldpTLVsTxOverloadingPorts,'rlLldpRemStatus':rlLldpRemStatus,'rlLldpRemTtlTable':rlLldpRemTtlTable,'rlLldpRemTtlEntry':rlLldpRemTtlEntry,'rlLldpRemTtl':rlLldpRemTtl,'rlLldpLocalSystemData':rlLldpLocalSystemData,'rlLldpLoc4WirePowerTable':rlLldpLoc4WirePowerTable,'rlLldpLoc4WirePowerEntry':rlLldpLoc4WirePowerEntry,'rlLldpLoc4WirePowerSupported':rlLldpLoc4WirePowerSupported,'rlLldpLoc4WirePowerSpPairDetClasReq':rlLldpLoc4WirePowerSpPairDetClasReq,'rlLldpLoc4WirePowerPdSpPairDesStEn':rlLldpLoc4WirePowerPdSpPairDesStEn,'rlLldpLoc4WirePowerPseSpPairOpStEn':rlLldpLoc4WirePowerPseSpPairOpStEn,'rlLldpRemoteSystemsData':rlLldpRemoteSystemsData,'rlLldpRem4WirePowerTable':rlLldpRem4WirePowerTable,'rlLldpRem4WirePowerEntry':rlLldpRem4WirePowerEntry,'rlLldpRem4WirePowerSupported':rlLldpRem4WirePowerSupported,'rlLldpRem4WirePowerSpPairDetClasReq':rlLldpRem4WirePowerSpPairDetClasReq,'rlLldpRem4WirePowerPdSpPairDesStEn':rlLldpRem4WirePowerPdSpPairDesStEn,'rlLldpRem4WirePowerPseSpPairOpStEn':rlLldpRem4WirePowerPseSpPairOpStEn,'rlLldpRemTable':rlLldpRemTable,_W:rlLldpRemEntry,'rlLldpRemSrcMacAddr':rlLldpRemSrcMacAddr,'rlLldpRemActiveStation':rlLldpRemActiveStation})