_S='atiswitchStaticMACAddress'
_R='atiswitchFwdVlanMACAddr'
_Q='atiswitchEthPortErrorId'
_P='atiswitchEthPortMonId'
_O='atiswitchPvPortNumber'
_N='atiswitchBeVlanIndex'
_M='disable'
_L='atiswitchPortNumber'
_K='atiswitchNwMgrIndex'
_J='copper'
_I='disabled'
_H='unknown'
_G='DisplayString'
_F='read-create'
_E='AtiSwitch-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention','TruthValue')
atiSwitchMib=ModuleIdentity((1,3,6,1,4,1,207,8,15))
class MACAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class BridgeId(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class Timeout(Integer32):0
_AlliedTelesyn_ObjectIdentity=ObjectIdentity
alliedTelesyn=_AlliedTelesyn_ObjectIdentity((1,3,6,1,4,1,207))
_AtiProduct_ObjectIdentity=ObjectIdentity
atiProduct=_AtiProduct_ObjectIdentity((1,3,6,1,4,1,207,1))
_Swhub_ObjectIdentity=ObjectIdentity
swhub=_Swhub_ObjectIdentity((1,3,6,1,4,1,207,1,4))
_At_8024_ObjectIdentity=ObjectIdentity
at_8024=_At_8024_ObjectIdentity((1,3,6,1,4,1,207,1,4,66))
_At_8024GB_ObjectIdentity=ObjectIdentity
at_8024GB=_At_8024GB_ObjectIdentity((1,3,6,1,4,1,207,1,4,67))
_At_8024M_ObjectIdentity=ObjectIdentity
at_8024M=_At_8024M_ObjectIdentity((1,3,6,1,4,1,207,1,4,78))
_At_8016F_SC_ObjectIdentity=ObjectIdentity
at_8016F_SC=_At_8016F_SC_ObjectIdentity((1,3,6,1,4,1,207,1,4,79))
_At_8026FC_ObjectIdentity=ObjectIdentity
at_8026FC=_At_8026FC_ObjectIdentity((1,3,6,1,4,1,207,1,4,80))
_At_8016F_MT_ObjectIdentity=ObjectIdentity
at_8016F_MT=_At_8016F_MT_ObjectIdentity((1,3,6,1,4,1,207,1,4,82))
_At_8012M_ObjectIdentity=ObjectIdentity
at_8012M=_At_8012M_ObjectIdentity((1,3,6,1,4,1,207,1,4,86))
_At_8088_SC_ObjectIdentity=ObjectIdentity
at_8088_SC=_At_8088_SC_ObjectIdentity((1,3,6,1,4,1,207,1,4,87))
_At_8088_MT_ObjectIdentity=ObjectIdentity
at_8088_MT=_At_8088_MT_ObjectIdentity((1,3,6,1,4,1,207,1,4,88))
_At_8026T_ObjectIdentity=ObjectIdentity
at_8026T=_At_8026T_ObjectIdentity((1,3,6,1,4,1,207,1,4,89))
_MibObject_ObjectIdentity=ObjectIdentity
mibObject=_MibObject_ObjectIdentity((1,3,6,1,4,1,207,8))
_AtiswitchSysGroup_ObjectIdentity=ObjectIdentity
atiswitchSysGroup=_AtiswitchSysGroup_ObjectIdentity((1,3,6,1,4,1,207,8,15,1))
class _AtiswitchProductType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,20)));namedValues=NamedValues(*(('at8024',1),('at8024GB',2),('at8024M',3),('at8016F-SC',4),('at8016F-MT',5),('at8026FC',6),('at8012M',7),('at8088-SC',8),('at8088-MT',9),('at8026T',10),('other',20)))
_AtiswitchProductType_Type.__name__=_C
_AtiswitchProductType_Object=MibScalar
atiswitchProductType=_AtiswitchProductType_Object((1,3,6,1,4,1,207,8,15,1,1),_AtiswitchProductType_Type())
atiswitchProductType.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchProductType.setStatus(_A)
_AtiswitchBasePortCount_Type=Integer32
_AtiswitchBasePortCount_Object=MibScalar
atiswitchBasePortCount=_AtiswitchBasePortCount_Object((1,3,6,1,4,1,207,8,15,1,2),_AtiswitchBasePortCount_Type())
atiswitchBasePortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchBasePortCount.setStatus(_A)
_AtiswitchUplinkPortCount_Type=Integer32
_AtiswitchUplinkPortCount_Object=MibScalar
atiswitchUplinkPortCount=_AtiswitchUplinkPortCount_Object((1,3,6,1,4,1,207,8,15,1,3),_AtiswitchUplinkPortCount_Type())
atiswitchUplinkPortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchUplinkPortCount.setStatus(_A)
class _AtiswitchReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('switchnoreset',1),('switchreset',2)))
_AtiswitchReset_Type.__name__=_C
_AtiswitchReset_Object=MibScalar
atiswitchReset=_AtiswitchReset_Object((1,3,6,1,4,1,207,8,15,1,4),_AtiswitchReset_Type())
atiswitchReset.setMaxAccess(_D)
if mibBuilder.loadTexts:atiswitchReset.setStatus(_A)
class _AtiswitchUplink1Type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('fiber',2),('none',3)))
_AtiswitchUplink1Type_Type.__name__=_C
_AtiswitchUplink1Type_Object=MibScalar
atiswitchUplink1Type=_AtiswitchUplink1Type_Object((1,3,6,1,4,1,207,8,15,1,5),_AtiswitchUplink1Type_Type())
atiswitchUplink1Type.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchUplink1Type.setStatus(_A)
class _AtiswitchUplink2Type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('fiber',2),('none',3)))
_AtiswitchUplink2Type_Type.__name__=_C
_AtiswitchUplink2Type_Object=MibScalar
atiswitchUplink2Type=_AtiswitchUplink2Type_Object((1,3,6,1,4,1,207,8,15,1,6),_AtiswitchUplink2Type_Type())
atiswitchUplink2Type.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchUplink2Type.setStatus(_A)
_AtiswitchSwGroup_ObjectIdentity=ObjectIdentity
atiswitchSwGroup=_AtiswitchSwGroup_ObjectIdentity((1,3,6,1,4,1,207,8,15,1,7))
class _AtiswitchSw_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AtiswitchSw_Type.__name__=_G
_AtiswitchSw_Object=MibScalar
atiswitchSw=_AtiswitchSw_Object((1,3,6,1,4,1,207,8,15,1,7,1),_AtiswitchSw_Type())
atiswitchSw.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchSw.setStatus(_A)
class _AtiswitchSwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AtiswitchSwVersion_Type.__name__=_G
_AtiswitchSwVersion_Object=MibScalar
atiswitchSwVersion=_AtiswitchSwVersion_Object((1,3,6,1,4,1,207,8,15,1,7,2),_AtiswitchSwVersion_Type())
atiswitchSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchSwVersion.setStatus(_A)
_AtiswitchIpGroup_ObjectIdentity=ObjectIdentity
atiswitchIpGroup=_AtiswitchIpGroup_ObjectIdentity((1,3,6,1,4,1,207,8,15,1,8))
_AtiswitchConfigIpAddress_Type=IpAddress
_AtiswitchConfigIpAddress_Object=MibScalar
atiswitchConfigIpAddress=_AtiswitchConfigIpAddress_Object((1,3,6,1,4,1,207,8,15,1,8,1),_AtiswitchConfigIpAddress_Type())
atiswitchConfigIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:atiswitchConfigIpAddress.setStatus(_A)
_AtiswitchConfigSubMask_Type=IpAddress
_AtiswitchConfigSubMask_Object=MibScalar
atiswitchConfigSubMask=_AtiswitchConfigSubMask_Object((1,3,6,1,4,1,207,8,15,1,8,2),_AtiswitchConfigSubMask_Type())
atiswitchConfigSubMask.setMaxAccess(_D)
if mibBuilder.loadTexts:atiswitchConfigSubMask.setStatus(_A)
_AtiswitchConfigRouting_Type=IpAddress
_AtiswitchConfigRouting_Object=MibScalar
atiswitchConfigRouting=_AtiswitchConfigRouting_Object((1,3,6,1,4,1,207,8,15,1,8,3),_AtiswitchConfigRouting_Type())
atiswitchConfigRouting.setMaxAccess(_D)
if mibBuilder.loadTexts:atiswitchConfigRouting.setStatus(_A)
class _AtiswitchIPAddressStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fromDhcp',1),('fromBootp',2),('fromStatic',3)))
_AtiswitchIPAddressStatus_Type.__name__=_C
_AtiswitchIPAddressStatus_Object=MibScalar
atiswitchIPAddressStatus=_AtiswitchIPAddressStatus_Object((1,3,6,1,4,1,207,8,15,1,8,4),_AtiswitchIPAddressStatus_Type())
atiswitchIPAddressStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchIPAddressStatus.setStatus(_A)
_AtiswitchDNServer_Type=IpAddress
_AtiswitchDNServer_Object=MibScalar
atiswitchDNServer=_AtiswitchDNServer_Object((1,3,6,1,4,1,207,8,15,1,8,5),_AtiswitchDNServer_Type())
atiswitchDNServer.setMaxAccess(_D)
if mibBuilder.loadTexts:atiswitchDNServer.setStatus(_A)
_AtiswitchDefaultDomainName_Type=DisplayString
_AtiswitchDefaultDomainName_Object=MibScalar
atiswitchDefaultDomainName=_AtiswitchDefaultDomainName_Object((1,3,6,1,4,1,207,8,15,1,8,6),_AtiswitchDefaultDomainName_Type())
atiswitchDefaultDomainName.setMaxAccess(_D)
if mibBuilder.loadTexts:atiswitchDefaultDomainName.setStatus(_A)
_AtiswitchNMGroup_ObjectIdentity=ObjectIdentity
atiswitchNMGroup=_AtiswitchNMGroup_ObjectIdentity((1,3,6,1,4,1,207,8,15,1,9))
_AtiswitchNwMgrTable_Object=MibTable
atiswitchNwMgrTable=_AtiswitchNwMgrTable_Object((1,3,6,1,4,1,207,8,15,1,9,1))
if mibBuilder.loadTexts:atiswitchNwMgrTable.setStatus(_A)
_AtiswitchNwMgrEntry_Object=MibTableRow
atiswitchNwMgrEntry=_AtiswitchNwMgrEntry_Object((1,3,6,1,4,1,207,8,15,1,9,1,1))
atiswitchNwMgrEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:atiswitchNwMgrEntry.setStatus(_A)
class _AtiswitchNwMgrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AtiswitchNwMgrIndex_Type.__name__=_C
_AtiswitchNwMgrIndex_Object=MibTableColumn
atiswitchNwMgrIndex=_AtiswitchNwMgrIndex_Object((1,3,6,1,4,1,207,8,15,1,9,1,1,1),_AtiswitchNwMgrIndex_Type())
atiswitchNwMgrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchNwMgrIndex.setStatus(_A)
_AtiswitchNwMgrIpAddr_Type=IpAddress
_AtiswitchNwMgrIpAddr_Object=MibTableColumn
atiswitchNwMgrIpAddr=_AtiswitchNwMgrIpAddr_Object((1,3,6,1,4,1,207,8,15,1,9,1,1,2),_AtiswitchNwMgrIpAddr_Type())
atiswitchNwMgrIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:atiswitchNwMgrIpAddr.setStatus(_A)
_AtiswitchConfigGroup_ObjectIdentity=ObjectIdentity
atiswitchConfigGroup=_AtiswitchConfigGroup_ObjectIdentity((1,3,6,1,4,1,207,8,15,2))
class _AtiswitchMirrorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('receive',1),('transmit',2),('both',3),(_I,4)))
_AtiswitchMirrorState_Type.__name__=_C
_AtiswitchMirrorState_Object=MibScalar
atiswitchMirrorState=_AtiswitchMirrorState_Object((1,3,6,1,4,1,207,8,15,2,1),_AtiswitchMirrorState_Type())
atiswitchMirrorState.setMaxAccess(_D)
if mibBuilder.loadTexts:atiswitchMirrorState.setStatus(_A)
_AtiswitchMirroringSourcePorts_Type=DisplayString
_AtiswitchMirroringSourcePorts_Object=MibScalar
atiswitchMirroringSourcePorts=_AtiswitchMirroringSourcePorts_Object((1,3,6,1,4,1,207,8,15,2,2),_AtiswitchMirroringSourcePorts_Type())
atiswitchMirroringSourcePorts.setMaxAccess(_D)
if mibBuilder.loadTexts:atiswitchMirroringSourcePorts.setStatus(_A)
_AtiswitchMirroringDestinationPort_Type=Integer32
_AtiswitchMirroringDestinationPort_Object=MibScalar
atiswitchMirroringDestinationPort=_AtiswitchMirroringDestinationPort_Object((1,3,6,1,4,1,207,8,15,2,3),_AtiswitchMirroringDestinationPort_Type())
atiswitchMirroringDestinationPort.setMaxAccess(_D)
if mibBuilder.loadTexts:atiswitchMirroringDestinationPort.setStatus(_A)
class _AtiswitchSecurityConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),('enabledLearningLocked',2),('enabledLimited',3),('enabledSecured',4)))
_AtiswitchSecurityConfig_Type.__name__=_C
_AtiswitchSecurityConfig_Object=MibScalar
atiswitchSecurityConfig=_AtiswitchSecurityConfig_Object((1,3,6,1,4,1,207,8,15,2,4),_AtiswitchSecurityConfig_Type())
atiswitchSecurityConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:atiswitchSecurityConfig.setStatus(_A)
class _AtiswitchSecurityAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('sendTrapOnly',1),('disablePortOnly',2),('disablePortAndSendTrap',3),('doNothing',4)))
_AtiswitchSecurityAction_Type.__name__=_C
_AtiswitchSecurityAction_Object=MibScalar
atiswitchSecurityAction=_AtiswitchSecurityAction_Object((1,3,6,1,4,1,207,8,15,2,5),_AtiswitchSecurityAction_Type())
atiswitchSecurityAction.setMaxAccess(_D)
if mibBuilder.loadTexts:atiswitchSecurityAction.setStatus(_A)
_AtiswitchPortGroup_ObjectIdentity=ObjectIdentity
atiswitchPortGroup=_AtiswitchPortGroup_ObjectIdentity((1,3,6,1,4,1,207,8,15,3))
_AtiswitchPortTable_Object=MibTable
atiswitchPortTable=_AtiswitchPortTable_Object((1,3,6,1,4,1,207,8,15,3,1))
if mibBuilder.loadTexts:atiswitchPortTable.setStatus(_A)
_AtiswitchPortEntry_Object=MibTableRow
atiswitchPortEntry=_AtiswitchPortEntry_Object((1,3,6,1,4,1,207,8,15,3,1,1))
atiswitchPortEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:atiswitchPortEntry.setStatus(_A)
class _AtiswitchPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtiswitchPortNumber_Type.__name__=_C
_AtiswitchPortNumber_Object=MibTableColumn
atiswitchPortNumber=_AtiswitchPortNumber_Object((1,3,6,1,4,1,207,8,15,3,1,1,1),_AtiswitchPortNumber_Type())
atiswitchPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchPortNumber.setStatus(_A)
class _AtiswitchPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AtiswitchPortName_Type.__name__=_G
_AtiswitchPortName_Object=MibTableColumn
atiswitchPortName=_AtiswitchPortName_Object((1,3,6,1,4,1,207,8,15,3,1,1,2),_AtiswitchPortName_Type())
atiswitchPortName.setMaxAccess(_D)
if mibBuilder.loadTexts:atiswitchPortName.setStatus(_A)
class _AtiswitchPortAutosenseOrHalfDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('portAutoSense',1),('forceHalfDuplex-10M',2),('forceHalfDuplex-100M',3),('forceFullDuplex-10M',4),('forceFullDuplex-100M',5),('forceHalfDuplex-1G',6),('forceFullDuplex-1G',7)))
_AtiswitchPortAutosenseOrHalfDuplex_Type.__name__=_C
_AtiswitchPortAutosenseOrHalfDuplex_Object=MibTableColumn
atiswitchPortAutosenseOrHalfDuplex=_AtiswitchPortAutosenseOrHalfDuplex_Object((1,3,6,1,4,1,207,8,15,3,1,1,3),_AtiswitchPortAutosenseOrHalfDuplex_Type())
atiswitchPortAutosenseOrHalfDuplex.setMaxAccess(_D)
if mibBuilder.loadTexts:atiswitchPortAutosenseOrHalfDuplex.setStatus(_A)
class _AtiswitchPortLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('online',1),('offline',2)))
_AtiswitchPortLinkState_Type.__name__=_C
_AtiswitchPortLinkState_Object=MibTableColumn
atiswitchPortLinkState=_AtiswitchPortLinkState_Object((1,3,6,1,4,1,207,8,15,3,1,1,4),_AtiswitchPortLinkState_Type())
atiswitchPortLinkState.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchPortLinkState.setStatus(_A)
class _AtiswitchPortDuplexStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fullDuplex',1),('halfDuplex',2),('autosense',3)))
_AtiswitchPortDuplexStatus_Type.__name__=_C
_AtiswitchPortDuplexStatus_Object=MibTableColumn
atiswitchPortDuplexStatus=_AtiswitchPortDuplexStatus_Object((1,3,6,1,4,1,207,8,15,3,1,1,5),_AtiswitchPortDuplexStatus_Type())
atiswitchPortDuplexStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchPortDuplexStatus.setStatus(_A)
class _AtiswitchPortSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('tenMBits',1),('hundredMBits',2),('gigaBits',3),(_H,4)))
_AtiswitchPortSpeed_Type.__name__=_C
_AtiswitchPortSpeed_Object=MibTableColumn
atiswitchPortSpeed=_AtiswitchPortSpeed_Object((1,3,6,1,4,1,207,8,15,3,1,1,6),_AtiswitchPortSpeed_Type())
atiswitchPortSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchPortSpeed.setStatus(_A)
class _AtiswitchPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('enabled',1),(_I,2),('blocking',3),('listening',4),('learning',5),(_H,6)))
_AtiswitchPortState_Type.__name__=_C
_AtiswitchPortState_Object=MibTableColumn
atiswitchPortState=_AtiswitchPortState_Object((1,3,6,1,4,1,207,8,15,3,1,1,7),_AtiswitchPortState_Type())
atiswitchPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:atiswitchPortState.setStatus(_A)
class _AtiswitchPortFlowControlConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_M,1),('transmit-only',2),('receive-only',3),('transmit-and-receive',4),(_H,5)))
_AtiswitchPortFlowControlConfig_Type.__name__=_C
_AtiswitchPortFlowControlConfig_Object=MibTableColumn
atiswitchPortFlowControlConfig=_AtiswitchPortFlowControlConfig_Object((1,3,6,1,4,1,207,8,15,3,1,1,8),_AtiswitchPortFlowControlConfig_Type())
atiswitchPortFlowControlConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:atiswitchPortFlowControlConfig.setStatus(_A)
class _AtiswitchPortBackPressureConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('enable',2),(_H,3)))
_AtiswitchPortBackPressureConfig_Type.__name__=_C
_AtiswitchPortBackPressureConfig_Object=MibTableColumn
atiswitchPortBackPressureConfig=_AtiswitchPortBackPressureConfig_Object((1,3,6,1,4,1,207,8,15,3,1,1,9),_AtiswitchPortBackPressureConfig_Type())
atiswitchPortBackPressureConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:atiswitchPortBackPressureConfig.setStatus(_A)
class _AtiswitchPortVlanTagPriorityConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('use-vlan-priority',1),('override-vlan-priority',2)))
_AtiswitchPortVlanTagPriorityConfig_Type.__name__=_C
_AtiswitchPortVlanTagPriorityConfig_Object=MibTableColumn
atiswitchPortVlanTagPriorityConfig=_AtiswitchPortVlanTagPriorityConfig_Object((1,3,6,1,4,1,207,8,15,3,1,1,10),_AtiswitchPortVlanTagPriorityConfig_Type())
atiswitchPortVlanTagPriorityConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:atiswitchPortVlanTagPriorityConfig.setStatus(_A)
class _AtiswitchPortCOSPriorityConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AtiswitchPortCOSPriorityConfig_Type.__name__=_C
_AtiswitchPortCOSPriorityConfig_Object=MibTableColumn
atiswitchPortCOSPriorityConfig=_AtiswitchPortCOSPriorityConfig_Object((1,3,6,1,4,1,207,8,15,3,1,1,11),_AtiswitchPortCOSPriorityConfig_Type())
atiswitchPortCOSPriorityConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:atiswitchPortCOSPriorityConfig.setStatus(_A)
class _AtiswitchPortBroadcastConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('discard-broadcasts',1),('do-not-discard-broadcasts',2)))
_AtiswitchPortBroadcastConfig_Type.__name__=_C
_AtiswitchPortBroadcastConfig_Object=MibTableColumn
atiswitchPortBroadcastConfig=_AtiswitchPortBroadcastConfig_Object((1,3,6,1,4,1,207,8,15,3,1,1,12),_AtiswitchPortBroadcastConfig_Type())
atiswitchPortBroadcastConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:atiswitchPortBroadcastConfig.setStatus(_A)
class _AtiswitchPortReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('reset',1),('no-reset',2)))
_AtiswitchPortReset_Type.__name__=_C
_AtiswitchPortReset_Object=MibTableColumn
atiswitchPortReset=_AtiswitchPortReset_Object((1,3,6,1,4,1,207,8,15,3,1,1,13),_AtiswitchPortReset_Type())
atiswitchPortReset.setMaxAccess(_D)
if mibBuilder.loadTexts:atiswitchPortReset.setStatus(_A)
_AtiswitchVlanConfigGroup_ObjectIdentity=ObjectIdentity
atiswitchVlanConfigGroup=_AtiswitchVlanConfigGroup_ObjectIdentity((1,3,6,1,4,1,207,8,15,4))
_AtiswitchBasicVlanTable_Object=MibTable
atiswitchBasicVlanTable=_AtiswitchBasicVlanTable_Object((1,3,6,1,4,1,207,8,15,4,1))
if mibBuilder.loadTexts:atiswitchBasicVlanTable.setStatus(_A)
_AtiswitchBasicVlanEntry_Object=MibTableRow
atiswitchBasicVlanEntry=_AtiswitchBasicVlanEntry_Object((1,3,6,1,4,1,207,8,15,4,1,1))
atiswitchBasicVlanEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:atiswitchBasicVlanEntry.setStatus(_A)
class _AtiswitchBeVlanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_AtiswitchBeVlanIndex_Type.__name__=_C
_AtiswitchBeVlanIndex_Object=MibTableColumn
atiswitchBeVlanIndex=_AtiswitchBeVlanIndex_Object((1,3,6,1,4,1,207,8,15,4,1,1,1),_AtiswitchBeVlanIndex_Type())
atiswitchBeVlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchBeVlanIndex.setStatus(_A)
class _AtiswitchBeVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AtiswitchBeVlanName_Type.__name__=_G
_AtiswitchBeVlanName_Object=MibTableColumn
atiswitchBeVlanName=_AtiswitchBeVlanName_Object((1,3,6,1,4,1,207,8,15,4,1,1,2),_AtiswitchBeVlanName_Type())
atiswitchBeVlanName.setMaxAccess(_F)
if mibBuilder.loadTexts:atiswitchBeVlanName.setStatus(_A)
class _AtiswitchBeVlanTagId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_AtiswitchBeVlanTagId_Type.__name__=_C
_AtiswitchBeVlanTagId_Object=MibTableColumn
atiswitchBeVlanTagId=_AtiswitchBeVlanTagId_Object((1,3,6,1,4,1,207,8,15,4,1,1,3),_AtiswitchBeVlanTagId_Type())
atiswitchBeVlanTagId.setMaxAccess(_F)
if mibBuilder.loadTexts:atiswitchBeVlanTagId.setStatus(_A)
_AtiswitchBeVlanTaggedPortMask_Type=DisplayString
_AtiswitchBeVlanTaggedPortMask_Object=MibTableColumn
atiswitchBeVlanTaggedPortMask=_AtiswitchBeVlanTaggedPortMask_Object((1,3,6,1,4,1,207,8,15,4,1,1,4),_AtiswitchBeVlanTaggedPortMask_Type())
atiswitchBeVlanTaggedPortMask.setMaxAccess(_F)
if mibBuilder.loadTexts:atiswitchBeVlanTaggedPortMask.setStatus(_A)
_AtiswitchBeVlanUntaggedPortMask_Type=DisplayString
_AtiswitchBeVlanUntaggedPortMask_Object=MibTableColumn
atiswitchBeVlanUntaggedPortMask=_AtiswitchBeVlanUntaggedPortMask_Object((1,3,6,1,4,1,207,8,15,4,1,1,5),_AtiswitchBeVlanUntaggedPortMask_Type())
atiswitchBeVlanUntaggedPortMask.setMaxAccess(_F)
if mibBuilder.loadTexts:atiswitchBeVlanUntaggedPortMask.setStatus(_A)
class _AtiswitchBeVlanMirrorPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtiswitchBeVlanMirrorPort_Type.__name__=_C
_AtiswitchBeVlanMirrorPort_Object=MibTableColumn
atiswitchBeVlanMirrorPort=_AtiswitchBeVlanMirrorPort_Object((1,3,6,1,4,1,207,8,15,4,1,1,6),_AtiswitchBeVlanMirrorPort_Type())
atiswitchBeVlanMirrorPort.setMaxAccess(_F)
if mibBuilder.loadTexts:atiswitchBeVlanMirrorPort.setStatus(_A)
_AtiswitchBeVlanRowStatus_Type=RowStatus
_AtiswitchBeVlanRowStatus_Object=MibTableColumn
atiswitchBeVlanRowStatus=_AtiswitchBeVlanRowStatus_Object((1,3,6,1,4,1,207,8,15,4,1,1,7),_AtiswitchBeVlanRowStatus_Type())
atiswitchBeVlanRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:atiswitchBeVlanRowStatus.setStatus(_A)
_AtiswitchPort2VlanTable_Object=MibTable
atiswitchPort2VlanTable=_AtiswitchPort2VlanTable_Object((1,3,6,1,4,1,207,8,15,4,2))
if mibBuilder.loadTexts:atiswitchPort2VlanTable.setStatus(_A)
_AtiswitchPort2VlanEntry_Object=MibTableRow
atiswitchPort2VlanEntry=_AtiswitchPort2VlanEntry_Object((1,3,6,1,4,1,207,8,15,4,2,1))
atiswitchPort2VlanEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:atiswitchPort2VlanEntry.setStatus(_A)
class _AtiswitchPvPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtiswitchPvPortNumber_Type.__name__=_C
_AtiswitchPvPortNumber_Object=MibTableColumn
atiswitchPvPortNumber=_AtiswitchPvPortNumber_Object((1,3,6,1,4,1,207,8,15,4,2,1,1),_AtiswitchPvPortNumber_Type())
atiswitchPvPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchPvPortNumber.setStatus(_A)
_AtiswitchPvVlanName_Type=DisplayString
_AtiswitchPvVlanName_Object=MibTableColumn
atiswitchPvVlanName=_AtiswitchPvVlanName_Object((1,3,6,1,4,1,207,8,15,4,2,1,2),_AtiswitchPvVlanName_Type())
atiswitchPvVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchPvVlanName.setStatus(_A)
class _AtiswitchVlanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('user-configured',1),('multiple',2),('multiple-802-1Q',3)))
_AtiswitchVlanMode_Type.__name__=_C
_AtiswitchVlanMode_Object=MibScalar
atiswitchVlanMode=_AtiswitchVlanMode_Object((1,3,6,1,4,1,207,8,15,4,3),_AtiswitchVlanMode_Type())
atiswitchVlanMode.setMaxAccess(_D)
if mibBuilder.loadTexts:atiswitchVlanMode.setStatus(_A)
_AtiswitchVlanUplinkVlanPort_Type=Integer32
_AtiswitchVlanUplinkVlanPort_Object=MibScalar
atiswitchVlanUplinkVlanPort=_AtiswitchVlanUplinkVlanPort_Object((1,3,6,1,4,1,207,8,15,4,4),_AtiswitchVlanUplinkVlanPort_Type())
atiswitchVlanUplinkVlanPort.setMaxAccess(_D)
if mibBuilder.loadTexts:atiswitchVlanUplinkVlanPort.setStatus(_A)
_AtiswitchEthernetStatsGroup_ObjectIdentity=ObjectIdentity
atiswitchEthernetStatsGroup=_AtiswitchEthernetStatsGroup_ObjectIdentity((1,3,6,1,4,1,207,8,15,5))
_AtiswitchEthMonStats_ObjectIdentity=ObjectIdentity
atiswitchEthMonStats=_AtiswitchEthMonStats_ObjectIdentity((1,3,6,1,4,1,207,8,15,5,1))
_AtiswitchEthMonRxGoodFrames_Type=Counter32
_AtiswitchEthMonRxGoodFrames_Object=MibScalar
atiswitchEthMonRxGoodFrames=_AtiswitchEthMonRxGoodFrames_Object((1,3,6,1,4,1,207,8,15,5,1,1),_AtiswitchEthMonRxGoodFrames_Type())
atiswitchEthMonRxGoodFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEthMonRxGoodFrames.setStatus(_A)
_AtiswitchEthMonTxGoodFrames_Type=Counter32
_AtiswitchEthMonTxGoodFrames_Object=MibScalar
atiswitchEthMonTxGoodFrames=_AtiswitchEthMonTxGoodFrames_Object((1,3,6,1,4,1,207,8,15,5,1,2),_AtiswitchEthMonTxGoodFrames_Type())
atiswitchEthMonTxGoodFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEthMonTxGoodFrames.setStatus(_A)
_AtiswitchEthMonTxTotalBytes_Type=Counter32
_AtiswitchEthMonTxTotalBytes_Object=MibScalar
atiswitchEthMonTxTotalBytes=_AtiswitchEthMonTxTotalBytes_Object((1,3,6,1,4,1,207,8,15,5,1,3),_AtiswitchEthMonTxTotalBytes_Type())
atiswitchEthMonTxTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEthMonTxTotalBytes.setStatus(_A)
_AtiswitchEthMonTxDeferred_Type=Counter32
_AtiswitchEthMonTxDeferred_Object=MibScalar
atiswitchEthMonTxDeferred=_AtiswitchEthMonTxDeferred_Object((1,3,6,1,4,1,207,8,15,5,1,4),_AtiswitchEthMonTxDeferred_Type())
atiswitchEthMonTxDeferred.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEthMonTxDeferred.setStatus(_A)
_AtiswitchEthMonTxCollisions_Type=Counter32
_AtiswitchEthMonTxCollisions_Object=MibScalar
atiswitchEthMonTxCollisions=_AtiswitchEthMonTxCollisions_Object((1,3,6,1,4,1,207,8,15,5,1,5),_AtiswitchEthMonTxCollisions_Type())
atiswitchEthMonTxCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEthMonTxCollisions.setStatus(_A)
_AtiswitchEthMonTxBroadcastFrames_Type=Counter32
_AtiswitchEthMonTxBroadcastFrames_Object=MibScalar
atiswitchEthMonTxBroadcastFrames=_AtiswitchEthMonTxBroadcastFrames_Object((1,3,6,1,4,1,207,8,15,5,1,6),_AtiswitchEthMonTxBroadcastFrames_Type())
atiswitchEthMonTxBroadcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEthMonTxBroadcastFrames.setStatus(_A)
_AtiswitchEthMonTxMulticastFrames_Type=Counter32
_AtiswitchEthMonTxMulticastFrames_Object=MibScalar
atiswitchEthMonTxMulticastFrames=_AtiswitchEthMonTxMulticastFrames_Object((1,3,6,1,4,1,207,8,15,5,1,7),_AtiswitchEthMonTxMulticastFrames_Type())
atiswitchEthMonTxMulticastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEthMonTxMulticastFrames.setStatus(_A)
_AtiswitchEthMonRxOverruns_Type=Counter32
_AtiswitchEthMonRxOverruns_Object=MibScalar
atiswitchEthMonRxOverruns=_AtiswitchEthMonRxOverruns_Object((1,3,6,1,4,1,207,8,15,5,1,8),_AtiswitchEthMonRxOverruns_Type())
atiswitchEthMonRxOverruns.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEthMonRxOverruns.setStatus(_A)
_AtiswitchEthErrorStats_ObjectIdentity=ObjectIdentity
atiswitchEthErrorStats=_AtiswitchEthErrorStats_ObjectIdentity((1,3,6,1,4,1,207,8,15,5,2))
_AtiswitchEthErrorCRC_Type=Counter32
_AtiswitchEthErrorCRC_Object=MibScalar
atiswitchEthErrorCRC=_AtiswitchEthErrorCRC_Object((1,3,6,1,4,1,207,8,15,5,2,1),_AtiswitchEthErrorCRC_Type())
atiswitchEthErrorCRC.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEthErrorCRC.setStatus(_A)
_AtiswitchEthErrorAlignment_Type=Counter32
_AtiswitchEthErrorAlignment_Object=MibScalar
atiswitchEthErrorAlignment=_AtiswitchEthErrorAlignment_Object((1,3,6,1,4,1,207,8,15,5,2,2),_AtiswitchEthErrorAlignment_Type())
atiswitchEthErrorAlignment.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEthErrorAlignment.setStatus(_A)
_AtiswitchEthErrorRxBadFrames_Type=Counter32
_AtiswitchEthErrorRxBadFrames_Object=MibScalar
atiswitchEthErrorRxBadFrames=_AtiswitchEthErrorRxBadFrames_Object((1,3,6,1,4,1,207,8,15,5,2,3),_AtiswitchEthErrorRxBadFrames_Type())
atiswitchEthErrorRxBadFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEthErrorRxBadFrames.setStatus(_A)
_AtiswitchEthErrorLateCollision_Type=Counter32
_AtiswitchEthErrorLateCollision_Object=MibScalar
atiswitchEthErrorLateCollision=_AtiswitchEthErrorLateCollision_Object((1,3,6,1,4,1,207,8,15,5,2,4),_AtiswitchEthErrorLateCollision_Type())
atiswitchEthErrorLateCollision.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEthErrorLateCollision.setStatus(_A)
_AtiswitchEthErrorTxTotal_Type=Counter32
_AtiswitchEthErrorTxTotal_Object=MibScalar
atiswitchEthErrorTxTotal=_AtiswitchEthErrorTxTotal_Object((1,3,6,1,4,1,207,8,15,5,2,5),_AtiswitchEthErrorTxTotal_Type())
atiswitchEthErrorTxTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEthErrorTxTotal.setStatus(_A)
_AtiswitchEthPortStatsGroup_ObjectIdentity=ObjectIdentity
atiswitchEthPortStatsGroup=_AtiswitchEthPortStatsGroup_ObjectIdentity((1,3,6,1,4,1,207,8,15,6))
_AtiswitchEthPortMonStats_ObjectIdentity=ObjectIdentity
atiswitchEthPortMonStats=_AtiswitchEthPortMonStats_ObjectIdentity((1,3,6,1,4,1,207,8,15,6,1))
_AtiswitchEthPortMonTable_Object=MibTable
atiswitchEthPortMonTable=_AtiswitchEthPortMonTable_Object((1,3,6,1,4,1,207,8,15,6,1,1))
if mibBuilder.loadTexts:atiswitchEthPortMonTable.setStatus(_A)
_AtiswitchEthPortMonEntry_Object=MibTableRow
atiswitchEthPortMonEntry=_AtiswitchEthPortMonEntry_Object((1,3,6,1,4,1,207,8,15,6,1,1,1))
atiswitchEthPortMonEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:atiswitchEthPortMonEntry.setStatus(_A)
class _AtiswitchEthPortMonId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtiswitchEthPortMonId_Type.__name__=_C
_AtiswitchEthPortMonId_Object=MibTableColumn
atiswitchEthPortMonId=_AtiswitchEthPortMonId_Object((1,3,6,1,4,1,207,8,15,6,1,1,1,1),_AtiswitchEthPortMonId_Type())
atiswitchEthPortMonId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEthPortMonId.setStatus(_A)
_AtiswitchEthPortMonRxGoodFrames_Type=Counter32
_AtiswitchEthPortMonRxGoodFrames_Object=MibTableColumn
atiswitchEthPortMonRxGoodFrames=_AtiswitchEthPortMonRxGoodFrames_Object((1,3,6,1,4,1,207,8,15,6,1,1,1,2),_AtiswitchEthPortMonRxGoodFrames_Type())
atiswitchEthPortMonRxGoodFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEthPortMonRxGoodFrames.setStatus(_A)
_AtiswitchEthPortMonTxGoodFrames_Type=Counter32
_AtiswitchEthPortMonTxGoodFrames_Object=MibTableColumn
atiswitchEthPortMonTxGoodFrames=_AtiswitchEthPortMonTxGoodFrames_Object((1,3,6,1,4,1,207,8,15,6,1,1,1,3),_AtiswitchEthPortMonTxGoodFrames_Type())
atiswitchEthPortMonTxGoodFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEthPortMonTxGoodFrames.setStatus(_A)
_AtiswitchEthPortMonTxTotalBytes_Type=Counter32
_AtiswitchEthPortMonTxTotalBytes_Object=MibTableColumn
atiswitchEthPortMonTxTotalBytes=_AtiswitchEthPortMonTxTotalBytes_Object((1,3,6,1,4,1,207,8,15,6,1,1,1,4),_AtiswitchEthPortMonTxTotalBytes_Type())
atiswitchEthPortMonTxTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEthPortMonTxTotalBytes.setStatus(_A)
_AtiswitchEthPortMonTxDeferred_Type=Counter32
_AtiswitchEthPortMonTxDeferred_Object=MibTableColumn
atiswitchEthPortMonTxDeferred=_AtiswitchEthPortMonTxDeferred_Object((1,3,6,1,4,1,207,8,15,6,1,1,1,5),_AtiswitchEthPortMonTxDeferred_Type())
atiswitchEthPortMonTxDeferred.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEthPortMonTxDeferred.setStatus(_A)
_AtiswitchEthPortMonTxCollisions_Type=Counter32
_AtiswitchEthPortMonTxCollisions_Object=MibTableColumn
atiswitchEthPortMonTxCollisions=_AtiswitchEthPortMonTxCollisions_Object((1,3,6,1,4,1,207,8,15,6,1,1,1,6),_AtiswitchEthPortMonTxCollisions_Type())
atiswitchEthPortMonTxCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEthPortMonTxCollisions.setStatus(_A)
_AtiswitchEthPortMonTxBroadcastFrames_Type=Counter32
_AtiswitchEthPortMonTxBroadcastFrames_Object=MibTableColumn
atiswitchEthPortMonTxBroadcastFrames=_AtiswitchEthPortMonTxBroadcastFrames_Object((1,3,6,1,4,1,207,8,15,6,1,1,1,7),_AtiswitchEthPortMonTxBroadcastFrames_Type())
atiswitchEthPortMonTxBroadcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEthPortMonTxBroadcastFrames.setStatus(_A)
_AtiswitchEthPortMonTxMulticastFrames_Type=Counter32
_AtiswitchEthPortMonTxMulticastFrames_Object=MibTableColumn
atiswitchEthPortMonTxMulticastFrames=_AtiswitchEthPortMonTxMulticastFrames_Object((1,3,6,1,4,1,207,8,15,6,1,1,1,8),_AtiswitchEthPortMonTxMulticastFrames_Type())
atiswitchEthPortMonTxMulticastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEthPortMonTxMulticastFrames.setStatus(_A)
_AtiswitchEthPortMonRxOverruns_Type=Counter32
_AtiswitchEthPortMonRxOverruns_Object=MibTableColumn
atiswitchEthPortMonRxOverruns=_AtiswitchEthPortMonRxOverruns_Object((1,3,6,1,4,1,207,8,15,6,1,1,1,9),_AtiswitchEthPortMonRxOverruns_Type())
atiswitchEthPortMonRxOverruns.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEthPortMonRxOverruns.setStatus(_A)
_AtiswitchEthPortError_ObjectIdentity=ObjectIdentity
atiswitchEthPortError=_AtiswitchEthPortError_ObjectIdentity((1,3,6,1,4,1,207,8,15,6,2))
_AtiswitchEthPortErrorTable_Object=MibTable
atiswitchEthPortErrorTable=_AtiswitchEthPortErrorTable_Object((1,3,6,1,4,1,207,8,15,6,2,1))
if mibBuilder.loadTexts:atiswitchEthPortErrorTable.setStatus(_A)
_AtiswitchEthPortErrorEntry_Object=MibTableRow
atiswitchEthPortErrorEntry=_AtiswitchEthPortErrorEntry_Object((1,3,6,1,4,1,207,8,15,6,2,1,1))
atiswitchEthPortErrorEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:atiswitchEthPortErrorEntry.setStatus(_A)
class _AtiswitchEthPortErrorId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtiswitchEthPortErrorId_Type.__name__=_C
_AtiswitchEthPortErrorId_Object=MibTableColumn
atiswitchEthPortErrorId=_AtiswitchEthPortErrorId_Object((1,3,6,1,4,1,207,8,15,6,2,1,1,1),_AtiswitchEthPortErrorId_Type())
atiswitchEthPortErrorId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEthPortErrorId.setStatus(_A)
_AtiswitchEthPortErrorRxBadFrames_Type=Counter32
_AtiswitchEthPortErrorRxBadFrames_Object=MibTableColumn
atiswitchEthPortErrorRxBadFrames=_AtiswitchEthPortErrorRxBadFrames_Object((1,3,6,1,4,1,207,8,15,6,2,1,1,2),_AtiswitchEthPortErrorRxBadFrames_Type())
atiswitchEthPortErrorRxBadFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEthPortErrorRxBadFrames.setStatus(_A)
_AtiswitchEthPortErrorTxTotal_Type=Counter32
_AtiswitchEthPortErrorTxTotal_Object=MibTableColumn
atiswitchEthPortErrorTxTotal=_AtiswitchEthPortErrorTxTotal_Object((1,3,6,1,4,1,207,8,15,6,2,1,1,3),_AtiswitchEthPortErrorTxTotal_Type())
atiswitchEthPortErrorTxTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEthPortErrorTxTotal.setStatus(_A)
_AtiswitchFwdVlanGroup_ObjectIdentity=ObjectIdentity
atiswitchFwdVlanGroup=_AtiswitchFwdVlanGroup_ObjectIdentity((1,3,6,1,4,1,207,8,15,7))
_AtiswitchFwdVlanTable_Object=MibTable
atiswitchFwdVlanTable=_AtiswitchFwdVlanTable_Object((1,3,6,1,4,1,207,8,15,7,1))
if mibBuilder.loadTexts:atiswitchFwdVlanTable.setStatus(_A)
_AtiswitchFwdVlanEntry_Object=MibTableRow
atiswitchFwdVlanEntry=_AtiswitchFwdVlanEntry_Object((1,3,6,1,4,1,207,8,15,7,1,1))
atiswitchFwdVlanEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:atiswitchFwdVlanEntry.setStatus(_A)
_AtiswitchFwdVlanMACAddr_Type=MACAddress
_AtiswitchFwdVlanMACAddr_Object=MibTableColumn
atiswitchFwdVlanMACAddr=_AtiswitchFwdVlanMACAddr_Object((1,3,6,1,4,1,207,8,15,7,1,1,1),_AtiswitchFwdVlanMACAddr_Type())
atiswitchFwdVlanMACAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchFwdVlanMACAddr.setStatus(_A)
_AtiswitchFwdVlanVlanId_Type=Integer32
_AtiswitchFwdVlanVlanId_Object=MibTableColumn
atiswitchFwdVlanVlanId=_AtiswitchFwdVlanVlanId_Object((1,3,6,1,4,1,207,8,15,7,1,1,2),_AtiswitchFwdVlanVlanId_Type())
atiswitchFwdVlanVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchFwdVlanVlanId.setStatus(_A)
_AtiswitchFwdVlanAge_Type=Integer32
_AtiswitchFwdVlanAge_Object=MibTableColumn
atiswitchFwdVlanAge=_AtiswitchFwdVlanAge_Object((1,3,6,1,4,1,207,8,15,7,1,1,3),_AtiswitchFwdVlanAge_Type())
atiswitchFwdVlanAge.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchFwdVlanAge.setStatus(_A)
class _AtiswitchFwdVlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inactive',1),('active',2),('other',3)))
_AtiswitchFwdVlanStatus_Type.__name__=_C
_AtiswitchFwdVlanStatus_Object=MibTableColumn
atiswitchFwdVlanStatus=_AtiswitchFwdVlanStatus_Object((1,3,6,1,4,1,207,8,15,7,1,1,4),_AtiswitchFwdVlanStatus_Type())
atiswitchFwdVlanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchFwdVlanStatus.setStatus(_A)
_AtiswitchFwdVlanPort_Type=Integer32
_AtiswitchFwdVlanPort_Object=MibTableColumn
atiswitchFwdVlanPort=_AtiswitchFwdVlanPort_Object((1,3,6,1,4,1,207,8,15,7,1,1,5),_AtiswitchFwdVlanPort_Type())
atiswitchFwdVlanPort.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchFwdVlanPort.setStatus(_A)
_AtiswitchStaticMACGroup_ObjectIdentity=ObjectIdentity
atiswitchStaticMACGroup=_AtiswitchStaticMACGroup_ObjectIdentity((1,3,6,1,4,1,207,8,15,8))
_AtiswitchStaticMACTable_Object=MibTable
atiswitchStaticMACTable=_AtiswitchStaticMACTable_Object((1,3,6,1,4,1,207,8,15,8,1))
if mibBuilder.loadTexts:atiswitchStaticMACTable.setStatus(_A)
_AtiswitchStaticMACEntry_Object=MibTableRow
atiswitchStaticMACEntry=_AtiswitchStaticMACEntry_Object((1,3,6,1,4,1,207,8,15,8,1,1))
atiswitchStaticMACEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:atiswitchStaticMACEntry.setStatus(_A)
_AtiswitchStaticMACAddress_Type=MACAddress
_AtiswitchStaticMACAddress_Object=MibTableColumn
atiswitchStaticMACAddress=_AtiswitchStaticMACAddress_Object((1,3,6,1,4,1,207,8,15,8,1,1,1),_AtiswitchStaticMACAddress_Type())
atiswitchStaticMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:atiswitchStaticMACAddress.setStatus(_A)
class _AtiswitchStaticMACPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtiswitchStaticMACPortNumber_Type.__name__=_C
_AtiswitchStaticMACPortNumber_Object=MibTableColumn
atiswitchStaticMACPortNumber=_AtiswitchStaticMACPortNumber_Object((1,3,6,1,4,1,207,8,15,8,1,1,2),_AtiswitchStaticMACPortNumber_Type())
atiswitchStaticMACPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:atiswitchStaticMACPortNumber.setStatus(_A)
class _AtiswitchStaticMACEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_AtiswitchStaticMACEntryStatus_Type.__name__=_C
_AtiswitchStaticMACEntryStatus_Object=MibTableColumn
atiswitchStaticMACEntryStatus=_AtiswitchStaticMACEntryStatus_Object((1,3,6,1,4,1,207,8,15,8,1,1,3),_AtiswitchStaticMACEntryStatus_Type())
atiswitchStaticMACEntryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:atiswitchStaticMACEntryStatus.setStatus(_A)
_AtiswitchTraps_ObjectIdentity=ObjectIdentity
atiswitchTraps=_AtiswitchTraps_ObjectIdentity((1,3,6,1,4,1,207,8,15,9))
atiswitchFanStopTrap=NotificationType((1,3,6,1,4,1,207,8,15,9,1))
if mibBuilder.loadTexts:atiswitchFanStopTrap.setStatus(_A)
atiswitchTemperatureAbnormalTrap=NotificationType((1,3,6,1,4,1,207,8,15,9,2))
if mibBuilder.loadTexts:atiswitchTemperatureAbnormalTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'MACAddress':MACAddress,'BridgeId':BridgeId,'Timeout':Timeout,'alliedTelesyn':alliedTelesyn,'atiProduct':atiProduct,'swhub':swhub,'at-8024':at_8024,'at-8024GB':at_8024GB,'at-8024M':at_8024M,'at-8016F-SC':at_8016F_SC,'at-8026FC':at_8026FC,'at-8016F-MT':at_8016F_MT,'at-8012M':at_8012M,'at-8088-SC':at_8088_SC,'at-8088-MT':at_8088_MT,'at-8026T':at_8026T,'mibObject':mibObject,'atiSwitchMib':atiSwitchMib,'atiswitchSysGroup':atiswitchSysGroup,'atiswitchProductType':atiswitchProductType,'atiswitchBasePortCount':atiswitchBasePortCount,'atiswitchUplinkPortCount':atiswitchUplinkPortCount,'atiswitchReset':atiswitchReset,'atiswitchUplink1Type':atiswitchUplink1Type,'atiswitchUplink2Type':atiswitchUplink2Type,'atiswitchSwGroup':atiswitchSwGroup,'atiswitchSw':atiswitchSw,'atiswitchSwVersion':atiswitchSwVersion,'atiswitchIpGroup':atiswitchIpGroup,'atiswitchConfigIpAddress':atiswitchConfigIpAddress,'atiswitchConfigSubMask':atiswitchConfigSubMask,'atiswitchConfigRouting':atiswitchConfigRouting,'atiswitchIPAddressStatus':atiswitchIPAddressStatus,'atiswitchDNServer':atiswitchDNServer,'atiswitchDefaultDomainName':atiswitchDefaultDomainName,'atiswitchNMGroup':atiswitchNMGroup,'atiswitchNwMgrTable':atiswitchNwMgrTable,'atiswitchNwMgrEntry':atiswitchNwMgrEntry,_K:atiswitchNwMgrIndex,'atiswitchNwMgrIpAddr':atiswitchNwMgrIpAddr,'atiswitchConfigGroup':atiswitchConfigGroup,'atiswitchMirrorState':atiswitchMirrorState,'atiswitchMirroringSourcePorts':atiswitchMirroringSourcePorts,'atiswitchMirroringDestinationPort':atiswitchMirroringDestinationPort,'atiswitchSecurityConfig':atiswitchSecurityConfig,'atiswitchSecurityAction':atiswitchSecurityAction,'atiswitchPortGroup':atiswitchPortGroup,'atiswitchPortTable':atiswitchPortTable,'atiswitchPortEntry':atiswitchPortEntry,_L:atiswitchPortNumber,'atiswitchPortName':atiswitchPortName,'atiswitchPortAutosenseOrHalfDuplex':atiswitchPortAutosenseOrHalfDuplex,'atiswitchPortLinkState':atiswitchPortLinkState,'atiswitchPortDuplexStatus':atiswitchPortDuplexStatus,'atiswitchPortSpeed':atiswitchPortSpeed,'atiswitchPortState':atiswitchPortState,'atiswitchPortFlowControlConfig':atiswitchPortFlowControlConfig,'atiswitchPortBackPressureConfig':atiswitchPortBackPressureConfig,'atiswitchPortVlanTagPriorityConfig':atiswitchPortVlanTagPriorityConfig,'atiswitchPortCOSPriorityConfig':atiswitchPortCOSPriorityConfig,'atiswitchPortBroadcastConfig':atiswitchPortBroadcastConfig,'atiswitchPortReset':atiswitchPortReset,'atiswitchVlanConfigGroup':atiswitchVlanConfigGroup,'atiswitchBasicVlanTable':atiswitchBasicVlanTable,'atiswitchBasicVlanEntry':atiswitchBasicVlanEntry,_N:atiswitchBeVlanIndex,'atiswitchBeVlanName':atiswitchBeVlanName,'atiswitchBeVlanTagId':atiswitchBeVlanTagId,'atiswitchBeVlanTaggedPortMask':atiswitchBeVlanTaggedPortMask,'atiswitchBeVlanUntaggedPortMask':atiswitchBeVlanUntaggedPortMask,'atiswitchBeVlanMirrorPort':atiswitchBeVlanMirrorPort,'atiswitchBeVlanRowStatus':atiswitchBeVlanRowStatus,'atiswitchPort2VlanTable':atiswitchPort2VlanTable,'atiswitchPort2VlanEntry':atiswitchPort2VlanEntry,_O:atiswitchPvPortNumber,'atiswitchPvVlanName':atiswitchPvVlanName,'atiswitchVlanMode':atiswitchVlanMode,'atiswitchVlanUplinkVlanPort':atiswitchVlanUplinkVlanPort,'atiswitchEthernetStatsGroup':atiswitchEthernetStatsGroup,'atiswitchEthMonStats':atiswitchEthMonStats,'atiswitchEthMonRxGoodFrames':atiswitchEthMonRxGoodFrames,'atiswitchEthMonTxGoodFrames':atiswitchEthMonTxGoodFrames,'atiswitchEthMonTxTotalBytes':atiswitchEthMonTxTotalBytes,'atiswitchEthMonTxDeferred':atiswitchEthMonTxDeferred,'atiswitchEthMonTxCollisions':atiswitchEthMonTxCollisions,'atiswitchEthMonTxBroadcastFrames':atiswitchEthMonTxBroadcastFrames,'atiswitchEthMonTxMulticastFrames':atiswitchEthMonTxMulticastFrames,'atiswitchEthMonRxOverruns':atiswitchEthMonRxOverruns,'atiswitchEthErrorStats':atiswitchEthErrorStats,'atiswitchEthErrorCRC':atiswitchEthErrorCRC,'atiswitchEthErrorAlignment':atiswitchEthErrorAlignment,'atiswitchEthErrorRxBadFrames':atiswitchEthErrorRxBadFrames,'atiswitchEthErrorLateCollision':atiswitchEthErrorLateCollision,'atiswitchEthErrorTxTotal':atiswitchEthErrorTxTotal,'atiswitchEthPortStatsGroup':atiswitchEthPortStatsGroup,'atiswitchEthPortMonStats':atiswitchEthPortMonStats,'atiswitchEthPortMonTable':atiswitchEthPortMonTable,'atiswitchEthPortMonEntry':atiswitchEthPortMonEntry,_P:atiswitchEthPortMonId,'atiswitchEthPortMonRxGoodFrames':atiswitchEthPortMonRxGoodFrames,'atiswitchEthPortMonTxGoodFrames':atiswitchEthPortMonTxGoodFrames,'atiswitchEthPortMonTxTotalBytes':atiswitchEthPortMonTxTotalBytes,'atiswitchEthPortMonTxDeferred':atiswitchEthPortMonTxDeferred,'atiswitchEthPortMonTxCollisions':atiswitchEthPortMonTxCollisions,'atiswitchEthPortMonTxBroadcastFrames':atiswitchEthPortMonTxBroadcastFrames,'atiswitchEthPortMonTxMulticastFrames':atiswitchEthPortMonTxMulticastFrames,'atiswitchEthPortMonRxOverruns':atiswitchEthPortMonRxOverruns,'atiswitchEthPortError':atiswitchEthPortError,'atiswitchEthPortErrorTable':atiswitchEthPortErrorTable,'atiswitchEthPortErrorEntry':atiswitchEthPortErrorEntry,_Q:atiswitchEthPortErrorId,'atiswitchEthPortErrorRxBadFrames':atiswitchEthPortErrorRxBadFrames,'atiswitchEthPortErrorTxTotal':atiswitchEthPortErrorTxTotal,'atiswitchFwdVlanGroup':atiswitchFwdVlanGroup,'atiswitchFwdVlanTable':atiswitchFwdVlanTable,'atiswitchFwdVlanEntry':atiswitchFwdVlanEntry,_R:atiswitchFwdVlanMACAddr,'atiswitchFwdVlanVlanId':atiswitchFwdVlanVlanId,'atiswitchFwdVlanAge':atiswitchFwdVlanAge,'atiswitchFwdVlanStatus':atiswitchFwdVlanStatus,'atiswitchFwdVlanPort':atiswitchFwdVlanPort,'atiswitchStaticMACGroup':atiswitchStaticMACGroup,'atiswitchStaticMACTable':atiswitchStaticMACTable,'atiswitchStaticMACEntry':atiswitchStaticMACEntry,_S:atiswitchStaticMACAddress,'atiswitchStaticMACPortNumber':atiswitchStaticMACPortNumber,'atiswitchStaticMACEntryStatus':atiswitchStaticMACEntryStatus,'atiswitchTraps':atiswitchTraps,'atiswitchFanStopTrap':atiswitchFanStopTrap,'atiswitchTemperatureAbnormalTrap':atiswitchTemperatureAbnormalTrap})