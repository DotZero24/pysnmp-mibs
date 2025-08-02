_AD='ethIfSrcMacCtrlLastViolatingAddr'
_AC='dot3OamXPeerState'
_AB='ethIfRingOperStatus'
_AA='erpPortState'
_A9='erpPortDescr'
_A8='dot3OamXEntry'
_A7='ethIfSysValidEtherTypeIdx'
_A6='ethIfSrcMacCtrlAddrIdx3'
_A5='ethIfSrcMacCtrlAddr'
_A4='ethIfSrcMacCtrlAddrIndex'
_A3='ethIfSrcMacCtrlIdx2'
_A2='ethIfSrcMacCtrlIndex'
_A1='dot3OamDescrId'
_A0='ethIfStormPacketType'
_z='ethIfStormDirection'
_y='ethIfStormIfIdx'
_x='ethIfStormCnfgIdx'
_w='erpVlanIdx'
_v='erpSubRingSubRingIndex'
_u='erpSubRingMajorRingIndex'
_t='erpPortIdx'
_s='destroy'
_r='createAndGo'
_q='ethIfRingIdx'
_p='ethIfIntervalNumber'
_o='ethIfIntervalIndex'
_n='ethIfCurrentIndex'
_m='manual'
_l='passive'
_k='unBlock'
_j='ifIndex'
_i='ifDescr'
_h='dot3OamOperStatus'
_g='dot3OamLoopbackStatus'
_f='dot3OamLoopbackIgnoreRx'
_e='west'
_d='east'
_c='active'
_b='ethIfIdx'
_a='SnmpAdminString'
_Z='erpIdx'
_Y='Bits'
_X='DOT3-OAM-MIB'
_W='OctetString'
_V='yes'
_U='no'
_T='enable'
_S='disable'
_R='ifAlias'
_Q='Unsigned32'
_P='alarmEventReason'
_O='alarmEventLogSourceName'
_N='alarmEventLogSeverity'
_M='alarmEventLogDescription'
_L='alarmEventLogDateAndTime'
_K='alarmEventLogAlarmOrEventId'
_J='IF-MIB'
_I='not-accessible'
_H='notApplicable'
_G='RAD-EthIf-MIB'
_F='read-create'
_E='read-write'
_D='Integer32'
_C='RAD-GEN-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_W,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot3OamEntry,dot3OamLoopbackIgnoreRx,dot3OamLoopbackStatus,dot3OamOperStatus=mibBuilder.importSymbols(_X,'dot3OamEntry',_f,_g,_h)
InterfaceIndexOrZero,ifAlias,ifDescr,ifIndex=mibBuilder.importSymbols(_J,'InterfaceIndexOrZero',_R,_i,_j)
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
alarmEventLogAlarmOrEventId,alarmEventLogDateAndTime,alarmEventLogDescription,alarmEventLogSeverity,alarmEventLogSourceName,alarmEventReason,prtTestCmdAndStatus=mibBuilder.importSymbols(_C,_K,_L,_M,_N,_O,_P,'prtTestCmdAndStatus')
diverseIfWanGen,=mibBuilder.importSymbols('RAD-SMI-MIB','diverseIfWanGen')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_a)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_Y,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_Q,'iso')
DisplayString,MacAddress,PhysAddress,RowPointer,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowPointer','RowStatus','TextualConvention','TruthValue')
ethIf=ModuleIdentity((1,3,6,1,4,1,164,3,1,6,1))
_EthIfEvents_ObjectIdentity=ObjectIdentity
ethIfEvents=_EthIfEvents_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,1,0))
_EthIfTable_Object=MibTable
ethIfTable=_EthIfTable_Object((1,3,6,1,4,1,164,3,1,6,1,1))
if mibBuilder.loadTexts:ethIfTable.setStatus(_A)
_EthIfEntry_Object=MibTableRow
ethIfEntry=_EthIfEntry_Object((1,3,6,1,4,1,164,3,1,6,1,1,1))
ethIfEntry.setIndexNames((0,_G,_b))
if mibBuilder.loadTexts:ethIfEntry.setStatus(_A)
_EthIfIdx_Type=Integer32
_EthIfIdx_Object=MibTableColumn
ethIfIdx=_EthIfIdx_Object((1,3,6,1,4,1,164,3,1,6,1,1,1,1),_EthIfIdx_Type())
ethIfIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIdx.setStatus(_A)
class _EthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('halfDuplex',1),('fullDuplex',2),(_H,255)))
_EthMode_Type.__name__=_D
_EthMode_Object=MibTableColumn
ethMode=_EthMode_Object((1,3,6,1,4,1,164,3,1,6,1,1,1,2),_EthMode_Type())
ethMode.setMaxAccess(_E)
if mibBuilder.loadTexts:ethMode.setStatus(_A)
class _EthBridgingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('filtered',1),('transparent',2)))
_EthBridgingMode_Type.__name__=_D
_EthBridgingMode_Object=MibTableColumn
ethBridgingMode=_EthBridgingMode_Object((1,3,6,1,4,1,164,3,1,6,1,1,1,3),_EthBridgingMode_Type())
ethBridgingMode.setMaxAccess(_E)
if mibBuilder.loadTexts:ethBridgingMode.setStatus(_A)
class _EthEncapsulationCRCMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('withCRC',2),('withoutCRC',3)))
_EthEncapsulationCRCMode_Type.__name__=_D
_EthEncapsulationCRCMode_Object=MibTableColumn
ethEncapsulationCRCMode=_EthEncapsulationCRCMode_Object((1,3,6,1,4,1,164,3,1,6,1,1,1,4),_EthEncapsulationCRCMode_Type())
ethEncapsulationCRCMode.setMaxAccess(_E)
if mibBuilder.loadTexts:ethEncapsulationCRCMode.setStatus(_A)
class _EthBackPressure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_S,2),(_T,3)))
_EthBackPressure_Type.__name__=_D
_EthBackPressure_Object=MibTableColumn
ethBackPressure=_EthBackPressure_Object((1,3,6,1,4,1,164,3,1,6,1,1,1,5),_EthBackPressure_Type())
ethBackPressure.setMaxAccess(_E)
if mibBuilder.loadTexts:ethBackPressure.setStatus(_A)
class _EthLimit4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_S,2),(_T,3)))
_EthLimit4_Type.__name__=_D
_EthLimit4_Object=MibTableColumn
ethLimit4=_EthLimit4_Object((1,3,6,1,4,1,164,3,1,6,1,1,1,6),_EthLimit4_Type())
ethLimit4.setMaxAccess(_E)
if mibBuilder.loadTexts:ethLimit4.setStatus(_A)
class _EthSkipInitReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('notSkip',2),('skip',3)))
_EthSkipInitReset_Type.__name__=_D
_EthSkipInitReset_Object=MibTableColumn
ethSkipInitReset=_EthSkipInitReset_Object((1,3,6,1,4,1,164,3,1,6,1,1,1,7),_EthSkipInitReset_Type())
ethSkipInitReset.setMaxAccess(_E)
if mibBuilder.loadTexts:ethSkipInitReset.setStatus(_A)
class _EthMulticastBlock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_k,2),('block',3)))
_EthMulticastBlock_Type.__name__=_D
_EthMulticastBlock_Object=MibTableColumn
ethMulticastBlock=_EthMulticastBlock_Object((1,3,6,1,4,1,164,3,1,6,1,1,1,8),_EthMulticastBlock_Type())
ethMulticastBlock.setMaxAccess(_E)
if mibBuilder.loadTexts:ethMulticastBlock.setStatus(_A)
class _EthBroadcastBlock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_k,2),('block',3)))
_EthBroadcastBlock_Type.__name__=_D
_EthBroadcastBlock_Object=MibTableColumn
ethBroadcastBlock=_EthBroadcastBlock_Object((1,3,6,1,4,1,164,3,1,6,1,1,1,9),_EthBroadcastBlock_Type())
ethBroadcastBlock.setMaxAccess(_E)
if mibBuilder.loadTexts:ethBroadcastBlock.setStatus(_A)
class _EthSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('s10Mbps',2),('s100Mbps',3),('s1Gbps',4)))
_EthSpeed_Type.__name__=_D
_EthSpeed_Object=MibTableColumn
ethSpeed=_EthSpeed_Object((1,3,6,1,4,1,164,3,1,6,1,1,1,10),_EthSpeed_Type())
ethSpeed.setMaxAccess(_E)
if mibBuilder.loadTexts:ethSpeed.setStatus(_A)
class _EthRip2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_U,2),(_V,3)))
_EthRip2_Type.__name__=_D
_EthRip2_Object=MibTableColumn
ethRip2=_EthRip2_Object((1,3,6,1,4,1,164,3,1,6,1,1,1,11),_EthRip2_Type())
ethRip2.setMaxAccess(_E)
if mibBuilder.loadTexts:ethRip2.setStatus(_A)
class _EthPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('none',2),('fixed',3)))
_EthPortPriority_Type.__name__=_D
_EthPortPriority_Object=MibTableColumn
ethPortPriority=_EthPortPriority_Object((1,3,6,1,4,1,164,3,1,6,1,1,1,12),_EthPortPriority_Type())
ethPortPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:ethPortPriority.setStatus(_A)
class _EthPortMngEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_U,2),(_V,3),('localOnly',4)))
_EthPortMngEnable_Type.__name__=_D
_EthPortMngEnable_Object=MibTableColumn
ethPortMngEnable=_EthPortMngEnable_Object((1,3,6,1,4,1,164,3,1,6,1,1,1,13),_EthPortMngEnable_Type())
ethPortMngEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ethPortMngEnable.setStatus(_A)
_EthFlowCtrlMacAddress_Type=MacAddress
_EthFlowCtrlMacAddress_Object=MibTableColumn
ethFlowCtrlMacAddress=_EthFlowCtrlMacAddress_Object((1,3,6,1,4,1,164,3,1,6,1,1,1,14),_EthFlowCtrlMacAddress_Type())
ethFlowCtrlMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:ethFlowCtrlMacAddress.setStatus(_A)
_EthRateLimit_Type=Integer32
_EthRateLimit_Object=MibTableColumn
ethRateLimit=_EthRateLimit_Object((1,3,6,1,4,1,164,3,1,6,1,1,1,15),_EthRateLimit_Type())
ethRateLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:ethRateLimit.setStatus(_A)
class _EthJumboFrameEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_U,2),(_V,3)))
_EthJumboFrameEnable_Type.__name__=_D
_EthJumboFrameEnable_Object=MibTableColumn
ethJumboFrameEnable=_EthJumboFrameEnable_Object((1,3,6,1,4,1,164,3,1,6,1,1,1,16),_EthJumboFrameEnable_Type())
ethJumboFrameEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ethJumboFrameEnable.setStatus(_A)
class _EthAutoMdiXEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_U,2),(_V,3)))
_EthAutoMdiXEnable_Type.__name__=_D
_EthAutoMdiXEnable_Object=MibTableColumn
ethAutoMdiXEnable=_EthAutoMdiXEnable_Object((1,3,6,1,4,1,164,3,1,6,1,1,1,17),_EthAutoMdiXEnable_Type())
ethAutoMdiXEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ethAutoMdiXEnable.setStatus(_A)
class _EthPortDataEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_U,2),(_V,3)))
_EthPortDataEnable_Type.__name__=_D
_EthPortDataEnable_Object=MibTableColumn
ethPortDataEnable=_EthPortDataEnable_Object((1,3,6,1,4,1,164,3,1,6,1,1,1,18),_EthPortDataEnable_Type())
ethPortDataEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ethPortDataEnable.setStatus(_A)
_EthIfUse_Type=Integer32
_EthIfUse_Object=MibTableColumn
ethIfUse=_EthIfUse_Object((1,3,6,1,4,1,164,3,1,6,1,1,1,19),_EthIfUse_Type())
ethIfUse.setMaxAccess(_E)
if mibBuilder.loadTexts:ethIfUse.setStatus(_A)
class _EthLineOam_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_S,2),(_l,3)))
_EthLineOam_Type.__name__=_D
_EthLineOam_Object=MibTableColumn
ethLineOam=_EthLineOam_Object((1,3,6,1,4,1,164,3,1,6,1,1,1,20),_EthLineOam_Type())
ethLineOam.setMaxAccess(_E)
if mibBuilder.loadTexts:ethLineOam.setStatus(_A)
class _EthRoutingProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,6)));namedValues=NamedValues(*((_H,1),('none',2),('proprietary',3),('rip2',4),('rip1and2',6)))
_EthRoutingProtocol_Type.__name__=_D
_EthRoutingProtocol_Object=MibTableColumn
ethRoutingProtocol=_EthRoutingProtocol_Object((1,3,6,1,4,1,164,3,1,6,1,1,1,21),_EthRoutingProtocol_Type())
ethRoutingProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:ethRoutingProtocol.setStatus(_A)
class _EthMdiXManualSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('crossOver',1),('straightThrough',2)))
_EthMdiXManualSwitch_Type.__name__=_D
_EthMdiXManualSwitch_Object=MibTableColumn
ethMdiXManualSwitch=_EthMdiXManualSwitch_Object((1,3,6,1,4,1,164,3,1,6,1,1,1,22),_EthMdiXManualSwitch_Type())
ethMdiXManualSwitch.setMaxAccess(_E)
if mibBuilder.loadTexts:ethMdiXManualSwitch.setStatus(_A)
class _EthDot1xEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_U,2),(_V,3)))
_EthDot1xEnable_Type.__name__=_D
_EthDot1xEnable_Object=MibTableColumn
ethDot1xEnable=_EthDot1xEnable_Object((1,3,6,1,4,1,164,3,1,6,1,1,1,23),_EthDot1xEnable_Type())
ethDot1xEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ethDot1xEnable.setStatus(_A)
class _EthPartnerRateMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_m,1),('automatic',2)))
_EthPartnerRateMode_Type.__name__=_D
_EthPartnerRateMode_Object=MibTableColumn
ethPartnerRateMode=_EthPartnerRateMode_Object((1,3,6,1,4,1,164,3,1,6,1,1,1,24),_EthPartnerRateMode_Type())
ethPartnerRateMode.setMaxAccess(_E)
if mibBuilder.loadTexts:ethPartnerRateMode.setStatus(_A)
class _EthDot1xPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('authenticator',1),('supplicant',2)))
_EthDot1xPortRole_Type.__name__=_D
_EthDot1xPortRole_Object=MibTableColumn
ethDot1xPortRole=_EthDot1xPortRole_Object((1,3,6,1,4,1,164,3,1,6,1,1,1,25),_EthDot1xPortRole_Type())
ethDot1xPortRole.setMaxAccess(_E)
if mibBuilder.loadTexts:ethDot1xPortRole.setStatus(_A)
class _EthDhcpRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('never',1),('normal',2),('whenUp',3)))
_EthDhcpRequest_Type.__name__=_D
_EthDhcpRequest_Object=MibTableColumn
ethDhcpRequest=_EthDhcpRequest_Object((1,3,6,1,4,1,164,3,1,6,1,1,1,26),_EthDhcpRequest_Type())
ethDhcpRequest.setMaxAccess(_E)
if mibBuilder.loadTexts:ethDhcpRequest.setStatus(_A)
class _EthSfpCapabilities_Type(Bits):namedValues=NamedValues(*(('speed10MFullAutoNegDisabled',0),('speed10MHalfAutoNegDisabled',1),('speed100MFullAutoNegDisabled',2),('speed100MHalfAutoNegDisabled',3),('speed1GFullAutoNegDisabled',4),('speed10GFullAutoNegDisabled',5),('autoNegConfigurable',6),('speed10MFullAutoNegEnabled',7),('speed10MHalfAutoNegEnabled',8),('speed100MFullAutoNegEnabled',9),('speed100MHalfAutoNegEnabled',10),('speed1GFullAutoNegEnabled',11),('speed10GFullAutoNegEnabled',12),('maxCapabilitiesAdvertised',13),('flowControlSupport',14),('sfpOpticInterface',15)))
_EthSfpCapabilities_Type.__name__=_Y
_EthSfpCapabilities_Object=MibTableColumn
ethSfpCapabilities=_EthSfpCapabilities_Object((1,3,6,1,4,1,164,3,1,6,1,1,1,27),_EthSfpCapabilities_Type())
ethSfpCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:ethSfpCapabilities.setStatus(_A)
_EthIfPerformance_ObjectIdentity=ObjectIdentity
ethIfPerformance=_EthIfPerformance_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,1,2))
_EthIfCurrentTable_Object=MibTable
ethIfCurrentTable=_EthIfCurrentTable_Object((1,3,6,1,4,1,164,3,1,6,1,2,1))
if mibBuilder.loadTexts:ethIfCurrentTable.setStatus(_A)
_EthIfCurrentEntry_Object=MibTableRow
ethIfCurrentEntry=_EthIfCurrentEntry_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1))
ethIfCurrentEntry.setIndexNames((0,_G,_n))
if mibBuilder.loadTexts:ethIfCurrentEntry.setStatus(_A)
_EthIfCurrentIndex_Type=Integer32
_EthIfCurrentIndex_Object=MibTableColumn
ethIfCurrentIndex=_EthIfCurrentIndex_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,1),_EthIfCurrentIndex_Type())
ethIfCurrentIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentIndex.setStatus(_A)
class _EthIfCurrentStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_EthIfCurrentStatus_Type.__name__=_W
_EthIfCurrentStatus_Object=MibTableColumn
ethIfCurrentStatus=_EthIfCurrentStatus_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,2),_EthIfCurrentStatus_Type())
ethIfCurrentStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentStatus.setStatus(_A)
_EthIfCurrentInFrames_Type=Gauge32
_EthIfCurrentInFrames_Object=MibTableColumn
ethIfCurrentInFrames=_EthIfCurrentInFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,3),_EthIfCurrentInFrames_Type())
ethIfCurrentInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentInFrames.setStatus(_A)
_EthIfCurrentInOctets_Type=Gauge32
_EthIfCurrentInOctets_Object=MibTableColumn
ethIfCurrentInOctets=_EthIfCurrentInOctets_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,4),_EthIfCurrentInOctets_Type())
ethIfCurrentInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentInOctets.setStatus(_A)
_EthIfCurrentAlignmentErrors_Type=Gauge32
_EthIfCurrentAlignmentErrors_Object=MibTableColumn
ethIfCurrentAlignmentErrors=_EthIfCurrentAlignmentErrors_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,5),_EthIfCurrentAlignmentErrors_Type())
ethIfCurrentAlignmentErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentAlignmentErrors.setStatus(_A)
_EthIfCurrentFCSErrors_Type=Gauge32
_EthIfCurrentFCSErrors_Object=MibTableColumn
ethIfCurrentFCSErrors=_EthIfCurrentFCSErrors_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,6),_EthIfCurrentFCSErrors_Type())
ethIfCurrentFCSErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentFCSErrors.setStatus(_A)
_EthIfCurrentLengthError_Type=Gauge32
_EthIfCurrentLengthError_Object=MibTableColumn
ethIfCurrentLengthError=_EthIfCurrentLengthError_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,7),_EthIfCurrentLengthError_Type())
ethIfCurrentLengthError.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentLengthError.setStatus(_A)
_EthIfCurrentOutFrames_Type=Gauge32
_EthIfCurrentOutFrames_Object=MibTableColumn
ethIfCurrentOutFrames=_EthIfCurrentOutFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,8),_EthIfCurrentOutFrames_Type())
ethIfCurrentOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentOutFrames.setStatus(_A)
_EthIfCurrentOutOctets_Type=Gauge32
_EthIfCurrentOutOctets_Object=MibTableColumn
ethIfCurrentOutOctets=_EthIfCurrentOutOctets_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,9),_EthIfCurrentOutOctets_Type())
ethIfCurrentOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentOutOctets.setStatus(_A)
_EthIfCurrentSingleCollisionFrames_Type=Gauge32
_EthIfCurrentSingleCollisionFrames_Object=MibTableColumn
ethIfCurrentSingleCollisionFrames=_EthIfCurrentSingleCollisionFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,10),_EthIfCurrentSingleCollisionFrames_Type())
ethIfCurrentSingleCollisionFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentSingleCollisionFrames.setStatus(_A)
_EthIfCurrentMultipleCollisionFrames_Type=Gauge32
_EthIfCurrentMultipleCollisionFrames_Object=MibTableColumn
ethIfCurrentMultipleCollisionFrames=_EthIfCurrentMultipleCollisionFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,11),_EthIfCurrentMultipleCollisionFrames_Type())
ethIfCurrentMultipleCollisionFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentMultipleCollisionFrames.setStatus(_A)
_EthIfCurrentDeferredTransmissions_Type=Gauge32
_EthIfCurrentDeferredTransmissions_Object=MibTableColumn
ethIfCurrentDeferredTransmissions=_EthIfCurrentDeferredTransmissions_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,12),_EthIfCurrentDeferredTransmissions_Type())
ethIfCurrentDeferredTransmissions.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentDeferredTransmissions.setStatus(_A)
_EthIfCurrentLateCollisions_Type=Gauge32
_EthIfCurrentLateCollisions_Object=MibTableColumn
ethIfCurrentLateCollisions=_EthIfCurrentLateCollisions_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,13),_EthIfCurrentLateCollisions_Type())
ethIfCurrentLateCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentLateCollisions.setStatus(_A)
_EthIfCurrentCarrierSenseErrors_Type=Gauge32
_EthIfCurrentCarrierSenseErrors_Object=MibTableColumn
ethIfCurrentCarrierSenseErrors=_EthIfCurrentCarrierSenseErrors_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,14),_EthIfCurrentCarrierSenseErrors_Type())
ethIfCurrentCarrierSenseErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentCarrierSenseErrors.setStatus(_A)
_EthIfCurrentInputCongestionDropped_Type=Gauge32
_EthIfCurrentInputCongestionDropped_Object=MibTableColumn
ethIfCurrentInputCongestionDropped=_EthIfCurrentInputCongestionDropped_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,15),_EthIfCurrentInputCongestionDropped_Type())
ethIfCurrentInputCongestionDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentInputCongestionDropped.setStatus(_A)
_EthIfCurrentOutputCongestionDropped_Type=Gauge32
_EthIfCurrentOutputCongestionDropped_Object=MibTableColumn
ethIfCurrentOutputCongestionDropped=_EthIfCurrentOutputCongestionDropped_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,16),_EthIfCurrentOutputCongestionDropped_Type())
ethIfCurrentOutputCongestionDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentOutputCongestionDropped.setStatus(_A)
_EthIfCurrentOverflowInFrames_Type=Gauge32
_EthIfCurrentOverflowInFrames_Object=MibTableColumn
ethIfCurrentOverflowInFrames=_EthIfCurrentOverflowInFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,17),_EthIfCurrentOverflowInFrames_Type())
ethIfCurrentOverflowInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentOverflowInFrames.setStatus(_A)
_EthIfCurrentOverflowInOctets_Type=Gauge32
_EthIfCurrentOverflowInOctets_Object=MibTableColumn
ethIfCurrentOverflowInOctets=_EthIfCurrentOverflowInOctets_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,18),_EthIfCurrentOverflowInOctets_Type())
ethIfCurrentOverflowInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentOverflowInOctets.setStatus(_A)
_EthIfCurrentOverflowFCSErrors_Type=Gauge32
_EthIfCurrentOverflowFCSErrors_Object=MibTableColumn
ethIfCurrentOverflowFCSErrors=_EthIfCurrentOverflowFCSErrors_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,19),_EthIfCurrentOverflowFCSErrors_Type())
ethIfCurrentOverflowFCSErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentOverflowFCSErrors.setStatus(_A)
_EthIfCurrentOverflowOutFrames_Type=Gauge32
_EthIfCurrentOverflowOutFrames_Object=MibTableColumn
ethIfCurrentOverflowOutFrames=_EthIfCurrentOverflowOutFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,20),_EthIfCurrentOverflowOutFrames_Type())
ethIfCurrentOverflowOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentOverflowOutFrames.setStatus(_A)
_EthIfCurrentOverflowOutOctets_Type=Gauge32
_EthIfCurrentOverflowOutOctets_Object=MibTableColumn
ethIfCurrentOverflowOutOctets=_EthIfCurrentOverflowOutOctets_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,21),_EthIfCurrentOverflowOutOctets_Type())
ethIfCurrentOverflowOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentOverflowOutOctets.setStatus(_A)
_EthIfCurrentOverflowMultipleCollisionFrames_Type=Gauge32
_EthIfCurrentOverflowMultipleCollisionFrames_Object=MibTableColumn
ethIfCurrentOverflowMultipleCollisionFrames=_EthIfCurrentOverflowMultipleCollisionFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,22),_EthIfCurrentOverflowMultipleCollisionFrames_Type())
ethIfCurrentOverflowMultipleCollisionFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentOverflowMultipleCollisionFrames.setStatus(_A)
_EthIfCurrentInUnicastFrames_Type=Gauge32
_EthIfCurrentInUnicastFrames_Object=MibTableColumn
ethIfCurrentInUnicastFrames=_EthIfCurrentInUnicastFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,23),_EthIfCurrentInUnicastFrames_Type())
ethIfCurrentInUnicastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentInUnicastFrames.setStatus(_A)
_EthIfCurrentOutUnicastFrames_Type=Gauge32
_EthIfCurrentOutUnicastFrames_Object=MibTableColumn
ethIfCurrentOutUnicastFrames=_EthIfCurrentOutUnicastFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,24),_EthIfCurrentOutUnicastFrames_Type())
ethIfCurrentOutUnicastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentOutUnicastFrames.setStatus(_A)
_EthIfCurrentInMulticastFrames_Type=Gauge32
_EthIfCurrentInMulticastFrames_Object=MibTableColumn
ethIfCurrentInMulticastFrames=_EthIfCurrentInMulticastFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,25),_EthIfCurrentInMulticastFrames_Type())
ethIfCurrentInMulticastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentInMulticastFrames.setStatus(_A)
_EthIfCurrentOutMulticastFrames_Type=Gauge32
_EthIfCurrentOutMulticastFrames_Object=MibTableColumn
ethIfCurrentOutMulticastFrames=_EthIfCurrentOutMulticastFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,26),_EthIfCurrentOutMulticastFrames_Type())
ethIfCurrentOutMulticastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentOutMulticastFrames.setStatus(_A)
_EthIfCurrentInBroadcastFrames_Type=Gauge32
_EthIfCurrentInBroadcastFrames_Object=MibTableColumn
ethIfCurrentInBroadcastFrames=_EthIfCurrentInBroadcastFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,27),_EthIfCurrentInBroadcastFrames_Type())
ethIfCurrentInBroadcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentInBroadcastFrames.setStatus(_A)
_EthIfCurrentOutBroadcastFrames_Type=Gauge32
_EthIfCurrentOutBroadcastFrames_Object=MibTableColumn
ethIfCurrentOutBroadcastFrames=_EthIfCurrentOutBroadcastFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,28),_EthIfCurrentOutBroadcastFrames_Type())
ethIfCurrentOutBroadcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentOutBroadcastFrames.setStatus(_A)
_EthIfCurrentInDiscardFrames_Type=Gauge32
_EthIfCurrentInDiscardFrames_Object=MibTableColumn
ethIfCurrentInDiscardFrames=_EthIfCurrentInDiscardFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,29),_EthIfCurrentInDiscardFrames_Type())
ethIfCurrentInDiscardFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentInDiscardFrames.setStatus(_A)
_EthIfCurrentOutDiscardFrames_Type=Gauge32
_EthIfCurrentOutDiscardFrames_Object=MibTableColumn
ethIfCurrentOutDiscardFrames=_EthIfCurrentOutDiscardFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,30),_EthIfCurrentOutDiscardFrames_Type())
ethIfCurrentOutDiscardFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentOutDiscardFrames.setStatus(_A)
_EthIfCurrentInPauseFrames_Type=Gauge32
_EthIfCurrentInPauseFrames_Object=MibTableColumn
ethIfCurrentInPauseFrames=_EthIfCurrentInPauseFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,31),_EthIfCurrentInPauseFrames_Type())
ethIfCurrentInPauseFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentInPauseFrames.setStatus(_A)
_EthIfCurrentOutPauseFrames_Type=Gauge32
_EthIfCurrentOutPauseFrames_Object=MibTableColumn
ethIfCurrentOutPauseFrames=_EthIfCurrentOutPauseFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,32),_EthIfCurrentOutPauseFrames_Type())
ethIfCurrentOutPauseFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentOutPauseFrames.setStatus(_A)
_EthIfCurrentOverflowInUnicastFrames_Type=Gauge32
_EthIfCurrentOverflowInUnicastFrames_Object=MibTableColumn
ethIfCurrentOverflowInUnicastFrames=_EthIfCurrentOverflowInUnicastFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,33),_EthIfCurrentOverflowInUnicastFrames_Type())
ethIfCurrentOverflowInUnicastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentOverflowInUnicastFrames.setStatus(_A)
_EthIfCurrentOverflowOutUnicastFrames_Type=Gauge32
_EthIfCurrentOverflowOutUnicastFrames_Object=MibTableColumn
ethIfCurrentOverflowOutUnicastFrames=_EthIfCurrentOverflowOutUnicastFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,34),_EthIfCurrentOverflowOutUnicastFrames_Type())
ethIfCurrentOverflowOutUnicastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentOverflowOutUnicastFrames.setStatus(_A)
_EthIfCurrentOverflowInMulticastFrames_Type=Gauge32
_EthIfCurrentOverflowInMulticastFrames_Object=MibTableColumn
ethIfCurrentOverflowInMulticastFrames=_EthIfCurrentOverflowInMulticastFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,35),_EthIfCurrentOverflowInMulticastFrames_Type())
ethIfCurrentOverflowInMulticastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentOverflowInMulticastFrames.setStatus(_A)
_EthIfCurrentOverflowOutMulticastFrames_Type=Gauge32
_EthIfCurrentOverflowOutMulticastFrames_Object=MibTableColumn
ethIfCurrentOverflowOutMulticastFrames=_EthIfCurrentOverflowOutMulticastFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,36),_EthIfCurrentOverflowOutMulticastFrames_Type())
ethIfCurrentOverflowOutMulticastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentOverflowOutMulticastFrames.setStatus(_A)
_EthIfCurrentOverflowInBroadcastFrames_Type=Gauge32
_EthIfCurrentOverflowInBroadcastFrames_Object=MibTableColumn
ethIfCurrentOverflowInBroadcastFrames=_EthIfCurrentOverflowInBroadcastFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,37),_EthIfCurrentOverflowInBroadcastFrames_Type())
ethIfCurrentOverflowInBroadcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentOverflowInBroadcastFrames.setStatus(_A)
_EthIfCurrentOverflowOutBroadcastFrames_Type=Gauge32
_EthIfCurrentOverflowOutBroadcastFrames_Object=MibTableColumn
ethIfCurrentOverflowOutBroadcastFrames=_EthIfCurrentOverflowOutBroadcastFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,38),_EthIfCurrentOverflowOutBroadcastFrames_Type())
ethIfCurrentOverflowOutBroadcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentOverflowOutBroadcastFrames.setStatus(_A)
_EthIfCurrentOverflowInDiscardFrames_Type=Gauge32
_EthIfCurrentOverflowInDiscardFrames_Object=MibTableColumn
ethIfCurrentOverflowInDiscardFrames=_EthIfCurrentOverflowInDiscardFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,39),_EthIfCurrentOverflowInDiscardFrames_Type())
ethIfCurrentOverflowInDiscardFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentOverflowInDiscardFrames.setStatus(_A)
_EthIfCurrentOverflowOutDiscardFrames_Type=Gauge32
_EthIfCurrentOverflowOutDiscardFrames_Object=MibTableColumn
ethIfCurrentOverflowOutDiscardFrames=_EthIfCurrentOverflowOutDiscardFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,40),_EthIfCurrentOverflowOutDiscardFrames_Type())
ethIfCurrentOverflowOutDiscardFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentOverflowOutDiscardFrames.setStatus(_A)
_EthIfCurrentOverflowInPauseFrames_Type=Gauge32
_EthIfCurrentOverflowInPauseFrames_Object=MibTableColumn
ethIfCurrentOverflowInPauseFrames=_EthIfCurrentOverflowInPauseFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,41),_EthIfCurrentOverflowInPauseFrames_Type())
ethIfCurrentOverflowInPauseFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentOverflowInPauseFrames.setStatus(_A)
_EthIfCurrentOverflowOutPauseFrames_Type=Gauge32
_EthIfCurrentOverflowOutPauseFrames_Object=MibTableColumn
ethIfCurrentOverflowOutPauseFrames=_EthIfCurrentOverflowOutPauseFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,1,1,42),_EthIfCurrentOverflowOutPauseFrames_Type())
ethIfCurrentOverflowOutPauseFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfCurrentOverflowOutPauseFrames.setStatus(_A)
_EthIfIntervalTable_Object=MibTable
ethIfIntervalTable=_EthIfIntervalTable_Object((1,3,6,1,4,1,164,3,1,6,1,2,2))
if mibBuilder.loadTexts:ethIfIntervalTable.setStatus(_A)
_EthIfIntervalEntry_Object=MibTableRow
ethIfIntervalEntry=_EthIfIntervalEntry_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1))
ethIfIntervalEntry.setIndexNames((0,_G,_o),(0,_G,_p))
if mibBuilder.loadTexts:ethIfIntervalEntry.setStatus(_A)
_EthIfIntervalIndex_Type=Integer32
_EthIfIntervalIndex_Object=MibTableColumn
ethIfIntervalIndex=_EthIfIntervalIndex_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,1),_EthIfIntervalIndex_Type())
ethIfIntervalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalIndex.setStatus(_A)
class _EthIfIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_EthIfIntervalNumber_Type.__name__=_D
_EthIfIntervalNumber_Object=MibTableColumn
ethIfIntervalNumber=_EthIfIntervalNumber_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,2),_EthIfIntervalNumber_Type())
ethIfIntervalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalNumber.setStatus(_A)
class _EthIfIntervalStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_EthIfIntervalStatus_Type.__name__=_W
_EthIfIntervalStatus_Object=MibTableColumn
ethIfIntervalStatus=_EthIfIntervalStatus_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,3),_EthIfIntervalStatus_Type())
ethIfIntervalStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalStatus.setStatus(_A)
_EthIfIntervalInFrames_Type=Gauge32
_EthIfIntervalInFrames_Object=MibTableColumn
ethIfIntervalInFrames=_EthIfIntervalInFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,4),_EthIfIntervalInFrames_Type())
ethIfIntervalInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalInFrames.setStatus(_A)
_EthIfIntervalInOctets_Type=Gauge32
_EthIfIntervalInOctets_Object=MibTableColumn
ethIfIntervalInOctets=_EthIfIntervalInOctets_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,5),_EthIfIntervalInOctets_Type())
ethIfIntervalInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalInOctets.setStatus(_A)
_EthIfIntervalAlignmentErrors_Type=Gauge32
_EthIfIntervalAlignmentErrors_Object=MibTableColumn
ethIfIntervalAlignmentErrors=_EthIfIntervalAlignmentErrors_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,6),_EthIfIntervalAlignmentErrors_Type())
ethIfIntervalAlignmentErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalAlignmentErrors.setStatus(_A)
_EthIfIntervalFCSErrors_Type=Gauge32
_EthIfIntervalFCSErrors_Object=MibTableColumn
ethIfIntervalFCSErrors=_EthIfIntervalFCSErrors_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,7),_EthIfIntervalFCSErrors_Type())
ethIfIntervalFCSErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalFCSErrors.setStatus(_A)
_EthIfIntervalLengthError_Type=Gauge32
_EthIfIntervalLengthError_Object=MibTableColumn
ethIfIntervalLengthError=_EthIfIntervalLengthError_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,8),_EthIfIntervalLengthError_Type())
ethIfIntervalLengthError.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalLengthError.setStatus(_A)
_EthIfIntervalOutFrames_Type=Gauge32
_EthIfIntervalOutFrames_Object=MibTableColumn
ethIfIntervalOutFrames=_EthIfIntervalOutFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,9),_EthIfIntervalOutFrames_Type())
ethIfIntervalOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalOutFrames.setStatus(_A)
_EthIfIntervalOutOctets_Type=Gauge32
_EthIfIntervalOutOctets_Object=MibTableColumn
ethIfIntervalOutOctets=_EthIfIntervalOutOctets_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,10),_EthIfIntervalOutOctets_Type())
ethIfIntervalOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalOutOctets.setStatus(_A)
_EthIfIntervalSingleCollisionFrames_Type=Gauge32
_EthIfIntervalSingleCollisionFrames_Object=MibTableColumn
ethIfIntervalSingleCollisionFrames=_EthIfIntervalSingleCollisionFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,11),_EthIfIntervalSingleCollisionFrames_Type())
ethIfIntervalSingleCollisionFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalSingleCollisionFrames.setStatus(_A)
_EthIfIntervalMultipleCollisionFrames_Type=Gauge32
_EthIfIntervalMultipleCollisionFrames_Object=MibTableColumn
ethIfIntervalMultipleCollisionFrames=_EthIfIntervalMultipleCollisionFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,12),_EthIfIntervalMultipleCollisionFrames_Type())
ethIfIntervalMultipleCollisionFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalMultipleCollisionFrames.setStatus(_A)
_EthIfIntervalDeferredTransmissions_Type=Gauge32
_EthIfIntervalDeferredTransmissions_Object=MibTableColumn
ethIfIntervalDeferredTransmissions=_EthIfIntervalDeferredTransmissions_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,13),_EthIfIntervalDeferredTransmissions_Type())
ethIfIntervalDeferredTransmissions.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalDeferredTransmissions.setStatus(_A)
_EthIfIntervalLateCollisions_Type=Gauge32
_EthIfIntervalLateCollisions_Object=MibTableColumn
ethIfIntervalLateCollisions=_EthIfIntervalLateCollisions_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,14),_EthIfIntervalLateCollisions_Type())
ethIfIntervalLateCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalLateCollisions.setStatus(_A)
_EthIfIntervalCarrierSenseErrors_Type=Gauge32
_EthIfIntervalCarrierSenseErrors_Object=MibTableColumn
ethIfIntervalCarrierSenseErrors=_EthIfIntervalCarrierSenseErrors_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,15),_EthIfIntervalCarrierSenseErrors_Type())
ethIfIntervalCarrierSenseErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalCarrierSenseErrors.setStatus(_A)
_EthIfIntervalInputCongestionDropped_Type=Gauge32
_EthIfIntervalInputCongestionDropped_Object=MibTableColumn
ethIfIntervalInputCongestionDropped=_EthIfIntervalInputCongestionDropped_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,16),_EthIfIntervalInputCongestionDropped_Type())
ethIfIntervalInputCongestionDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalInputCongestionDropped.setStatus(_A)
_EthIfIntervalOutputCongestionDropped_Type=Gauge32
_EthIfIntervalOutputCongestionDropped_Object=MibTableColumn
ethIfIntervalOutputCongestionDropped=_EthIfIntervalOutputCongestionDropped_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,17),_EthIfIntervalOutputCongestionDropped_Type())
ethIfIntervalOutputCongestionDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalOutputCongestionDropped.setStatus(_A)
_EthIfIntervalOverflowInFrames_Type=Gauge32
_EthIfIntervalOverflowInFrames_Object=MibTableColumn
ethIfIntervalOverflowInFrames=_EthIfIntervalOverflowInFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,18),_EthIfIntervalOverflowInFrames_Type())
ethIfIntervalOverflowInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalOverflowInFrames.setStatus(_A)
_EthIfIntervalOverflowInOctets_Type=Gauge32
_EthIfIntervalOverflowInOctets_Object=MibTableColumn
ethIfIntervalOverflowInOctets=_EthIfIntervalOverflowInOctets_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,19),_EthIfIntervalOverflowInOctets_Type())
ethIfIntervalOverflowInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalOverflowInOctets.setStatus(_A)
_EthIfIntervalOverflowFCSErrors_Type=Gauge32
_EthIfIntervalOverflowFCSErrors_Object=MibTableColumn
ethIfIntervalOverflowFCSErrors=_EthIfIntervalOverflowFCSErrors_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,20),_EthIfIntervalOverflowFCSErrors_Type())
ethIfIntervalOverflowFCSErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalOverflowFCSErrors.setStatus(_A)
_EthIfIntervalOverflowOutFrames_Type=Gauge32
_EthIfIntervalOverflowOutFrames_Object=MibTableColumn
ethIfIntervalOverflowOutFrames=_EthIfIntervalOverflowOutFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,21),_EthIfIntervalOverflowOutFrames_Type())
ethIfIntervalOverflowOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalOverflowOutFrames.setStatus(_A)
_EthIfIntervalOverflowOutOctets_Type=Gauge32
_EthIfIntervalOverflowOutOctets_Object=MibTableColumn
ethIfIntervalOverflowOutOctets=_EthIfIntervalOverflowOutOctets_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,22),_EthIfIntervalOverflowOutOctets_Type())
ethIfIntervalOverflowOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalOverflowOutOctets.setStatus(_A)
_EthIfIntervalOverflowMultipleCollisionFrames_Type=Gauge32
_EthIfIntervalOverflowMultipleCollisionFrames_Object=MibTableColumn
ethIfIntervalOverflowMultipleCollisionFrames=_EthIfIntervalOverflowMultipleCollisionFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,23),_EthIfIntervalOverflowMultipleCollisionFrames_Type())
ethIfIntervalOverflowMultipleCollisionFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalOverflowMultipleCollisionFrames.setStatus(_A)
_EthIfIntervalInUnicastFrames_Type=Gauge32
_EthIfIntervalInUnicastFrames_Object=MibTableColumn
ethIfIntervalInUnicastFrames=_EthIfIntervalInUnicastFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,24),_EthIfIntervalInUnicastFrames_Type())
ethIfIntervalInUnicastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalInUnicastFrames.setStatus(_A)
_EthIfIntervalOutUnicastFrames_Type=Gauge32
_EthIfIntervalOutUnicastFrames_Object=MibTableColumn
ethIfIntervalOutUnicastFrames=_EthIfIntervalOutUnicastFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,25),_EthIfIntervalOutUnicastFrames_Type())
ethIfIntervalOutUnicastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalOutUnicastFrames.setStatus(_A)
_EthIfIntervalInMulticastFrames_Type=Gauge32
_EthIfIntervalInMulticastFrames_Object=MibTableColumn
ethIfIntervalInMulticastFrames=_EthIfIntervalInMulticastFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,26),_EthIfIntervalInMulticastFrames_Type())
ethIfIntervalInMulticastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalInMulticastFrames.setStatus(_A)
_EthIfIntervalOutMulticastFrames_Type=Gauge32
_EthIfIntervalOutMulticastFrames_Object=MibTableColumn
ethIfIntervalOutMulticastFrames=_EthIfIntervalOutMulticastFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,27),_EthIfIntervalOutMulticastFrames_Type())
ethIfIntervalOutMulticastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalOutMulticastFrames.setStatus(_A)
_EthIfIntervalInBroadcastFrames_Type=Gauge32
_EthIfIntervalInBroadcastFrames_Object=MibTableColumn
ethIfIntervalInBroadcastFrames=_EthIfIntervalInBroadcastFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,28),_EthIfIntervalInBroadcastFrames_Type())
ethIfIntervalInBroadcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalInBroadcastFrames.setStatus(_A)
_EthIfIntervalOutBroadcastFrames_Type=Gauge32
_EthIfIntervalOutBroadcastFrames_Object=MibTableColumn
ethIfIntervalOutBroadcastFrames=_EthIfIntervalOutBroadcastFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,29),_EthIfIntervalOutBroadcastFrames_Type())
ethIfIntervalOutBroadcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalOutBroadcastFrames.setStatus(_A)
_EthIfIntervalInDiscardFrames_Type=Gauge32
_EthIfIntervalInDiscardFrames_Object=MibTableColumn
ethIfIntervalInDiscardFrames=_EthIfIntervalInDiscardFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,30),_EthIfIntervalInDiscardFrames_Type())
ethIfIntervalInDiscardFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalInDiscardFrames.setStatus(_A)
_EthIfIntervalOutDiscardFrames_Type=Gauge32
_EthIfIntervalOutDiscardFrames_Object=MibTableColumn
ethIfIntervalOutDiscardFrames=_EthIfIntervalOutDiscardFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,31),_EthIfIntervalOutDiscardFrames_Type())
ethIfIntervalOutDiscardFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalOutDiscardFrames.setStatus(_A)
_EthIfIntervalInPauseFrames_Type=Gauge32
_EthIfIntervalInPauseFrames_Object=MibTableColumn
ethIfIntervalInPauseFrames=_EthIfIntervalInPauseFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,32),_EthIfIntervalInPauseFrames_Type())
ethIfIntervalInPauseFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalInPauseFrames.setStatus(_A)
_EthIfIntervalOutPauseFrames_Type=Gauge32
_EthIfIntervalOutPauseFrames_Object=MibTableColumn
ethIfIntervalOutPauseFrames=_EthIfIntervalOutPauseFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,33),_EthIfIntervalOutPauseFrames_Type())
ethIfIntervalOutPauseFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalOutPauseFrames.setStatus(_A)
_EthIfIntervalOverflowInUnicastFrames_Type=Gauge32
_EthIfIntervalOverflowInUnicastFrames_Object=MibTableColumn
ethIfIntervalOverflowInUnicastFrames=_EthIfIntervalOverflowInUnicastFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,34),_EthIfIntervalOverflowInUnicastFrames_Type())
ethIfIntervalOverflowInUnicastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalOverflowInUnicastFrames.setStatus(_A)
_EthIfIntervalOverflowOutUnicastFrames_Type=Gauge32
_EthIfIntervalOverflowOutUnicastFrames_Object=MibTableColumn
ethIfIntervalOverflowOutUnicastFrames=_EthIfIntervalOverflowOutUnicastFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,35),_EthIfIntervalOverflowOutUnicastFrames_Type())
ethIfIntervalOverflowOutUnicastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalOverflowOutUnicastFrames.setStatus(_A)
_EthIfIntervalOverflowInMulticastFrames_Type=Gauge32
_EthIfIntervalOverflowInMulticastFrames_Object=MibTableColumn
ethIfIntervalOverflowInMulticastFrames=_EthIfIntervalOverflowInMulticastFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,36),_EthIfIntervalOverflowInMulticastFrames_Type())
ethIfIntervalOverflowInMulticastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalOverflowInMulticastFrames.setStatus(_A)
_EthIfIntervalOverflowOutMulticastFrames_Type=Gauge32
_EthIfIntervalOverflowOutMulticastFrames_Object=MibTableColumn
ethIfIntervalOverflowOutMulticastFrames=_EthIfIntervalOverflowOutMulticastFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,37),_EthIfIntervalOverflowOutMulticastFrames_Type())
ethIfIntervalOverflowOutMulticastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalOverflowOutMulticastFrames.setStatus(_A)
_EthIfIntervalOverflowInBroadcastFrames_Type=Gauge32
_EthIfIntervalOverflowInBroadcastFrames_Object=MibTableColumn
ethIfIntervalOverflowInBroadcastFrames=_EthIfIntervalOverflowInBroadcastFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,38),_EthIfIntervalOverflowInBroadcastFrames_Type())
ethIfIntervalOverflowInBroadcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalOverflowInBroadcastFrames.setStatus(_A)
_EthIfIntervalOverflowOutBroadcastFrames_Type=Gauge32
_EthIfIntervalOverflowOutBroadcastFrames_Object=MibTableColumn
ethIfIntervalOverflowOutBroadcastFrames=_EthIfIntervalOverflowOutBroadcastFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,39),_EthIfIntervalOverflowOutBroadcastFrames_Type())
ethIfIntervalOverflowOutBroadcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalOverflowOutBroadcastFrames.setStatus(_A)
_EthIfIntervalOverflowInDiscardFrames_Type=Gauge32
_EthIfIntervalOverflowInDiscardFrames_Object=MibTableColumn
ethIfIntervalOverflowInDiscardFrames=_EthIfIntervalOverflowInDiscardFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,40),_EthIfIntervalOverflowInDiscardFrames_Type())
ethIfIntervalOverflowInDiscardFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalOverflowInDiscardFrames.setStatus(_A)
_EthIfIntervalOverflowOutDiscardFrames_Type=Gauge32
_EthIfIntervalOverflowOutDiscardFrames_Object=MibTableColumn
ethIfIntervalOverflowOutDiscardFrames=_EthIfIntervalOverflowOutDiscardFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,41),_EthIfIntervalOverflowOutDiscardFrames_Type())
ethIfIntervalOverflowOutDiscardFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalOverflowOutDiscardFrames.setStatus(_A)
_EthIfIntervalOverflowInPauseFrames_Type=Gauge32
_EthIfIntervalOverflowInPauseFrames_Object=MibTableColumn
ethIfIntervalOverflowInPauseFrames=_EthIfIntervalOverflowInPauseFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,42),_EthIfIntervalOverflowInPauseFrames_Type())
ethIfIntervalOverflowInPauseFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalOverflowInPauseFrames.setStatus(_A)
_EthIfIntervalOverflowOutPauseFrames_Type=Gauge32
_EthIfIntervalOverflowOutPauseFrames_Object=MibTableColumn
ethIfIntervalOverflowOutPauseFrames=_EthIfIntervalOverflowOutPauseFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,2,1,43),_EthIfIntervalOverflowOutPauseFrames_Type())
ethIfIntervalOverflowOutPauseFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIntervalOverflowOutPauseFrames.setStatus(_A)
class _EthPerformanceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('countOK',2),('countFail',3)))
_EthPerformanceMode_Type.__name__=_D
_EthPerformanceMode_Object=MibScalar
ethPerformanceMode=_EthPerformanceMode_Object((1,3,6,1,4,1,164,3,1,6,1,2,3),_EthPerformanceMode_Type())
ethPerformanceMode.setMaxAccess(_E)
if mibBuilder.loadTexts:ethPerformanceMode.setStatus(_A)
_EthIfPerfTable_Object=MibTable
ethIfPerfTable=_EthIfPerfTable_Object((1,3,6,1,4,1,164,3,1,6,1,2,4))
if mibBuilder.loadTexts:ethIfPerfTable.setStatus(_A)
_EthIfPerfEntry_Object=MibTableRow
ethIfPerfEntry=_EthIfPerfEntry_Object((1,3,6,1,4,1,164,3,1,6,1,2,4,1))
ethIfPerfEntry.setIndexNames((0,_G,_b))
if mibBuilder.loadTexts:ethIfPerfEntry.setStatus(_A)
_EthIfPerfInOkFrames_Type=Gauge32
_EthIfPerfInOkFrames_Object=MibTableColumn
ethIfPerfInOkFrames=_EthIfPerfInOkFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,4,1,1),_EthIfPerfInOkFrames_Type())
ethIfPerfInOkFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfPerfInOkFrames.setStatus(_A)
_EthIfPerfOutOkFrames_Type=Gauge32
_EthIfPerfOutOkFrames_Object=MibTableColumn
ethIfPerfOutOkFrames=_EthIfPerfOutOkFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,4,1,2),_EthIfPerfOutOkFrames_Type())
ethIfPerfOutOkFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfPerfOutOkFrames.setStatus(_A)
_EthIfPerfTotalCollisions_Type=Gauge32
_EthIfPerfTotalCollisions_Object=MibTableColumn
ethIfPerfTotalCollisions=_EthIfPerfTotalCollisions_Object((1,3,6,1,4,1,164,3,1,6,1,2,4,1,3),_EthIfPerfTotalCollisions_Type())
ethIfPerfTotalCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfPerfTotalCollisions.setStatus(_A)
_EthIfPerfInOkOctets_Type=Gauge32
_EthIfPerfInOkOctets_Object=MibTableColumn
ethIfPerfInOkOctets=_EthIfPerfInOkOctets_Object((1,3,6,1,4,1,164,3,1,6,1,2,4,1,4),_EthIfPerfInOkOctets_Type())
ethIfPerfInOkOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfPerfInOkOctets.setStatus(_A)
_EthIfStatsTable_Object=MibTable
ethIfStatsTable=_EthIfStatsTable_Object((1,3,6,1,4,1,164,3,1,6,1,2,5))
if mibBuilder.loadTexts:ethIfStatsTable.setStatus(_A)
_EthIfStatsEntry_Object=MibTableRow
ethIfStatsEntry=_EthIfStatsEntry_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1))
ethIfStatsEntry.setIndexNames((0,_J,_j))
if mibBuilder.loadTexts:ethIfStatsEntry.setStatus(_A)
_EthIfStatsInOctets_Type=Counter64
_EthIfStatsInOctets_Object=MibTableColumn
ethIfStatsInOctets=_EthIfStatsInOctets_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,1),_EthIfStatsInOctets_Type())
ethIfStatsInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsInOctets.setStatus(_A)
_EthIfStatsInPkts_Type=Counter64
_EthIfStatsInPkts_Object=MibTableColumn
ethIfStatsInPkts=_EthIfStatsInPkts_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,2),_EthIfStatsInPkts_Type())
ethIfStatsInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsInPkts.setStatus(_A)
_EthIfStatsInUcastPkts_Type=Counter64
_EthIfStatsInUcastPkts_Object=MibTableColumn
ethIfStatsInUcastPkts=_EthIfStatsInUcastPkts_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,3),_EthIfStatsInUcastPkts_Type())
ethIfStatsInUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsInUcastPkts.setStatus(_A)
_EthIfStatsInMulticastPkts_Type=Counter64
_EthIfStatsInMulticastPkts_Object=MibTableColumn
ethIfStatsInMulticastPkts=_EthIfStatsInMulticastPkts_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,4),_EthIfStatsInMulticastPkts_Type())
ethIfStatsInMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsInMulticastPkts.setStatus(_A)
_EthIfStatsInBroadcastPkts_Type=Counter64
_EthIfStatsInBroadcastPkts_Object=MibTableColumn
ethIfStatsInBroadcastPkts=_EthIfStatsInBroadcastPkts_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,5),_EthIfStatsInBroadcastPkts_Type())
ethIfStatsInBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsInBroadcastPkts.setStatus(_A)
_EthIfStatsInJabberPkts_Type=Counter64
_EthIfStatsInJabberPkts_Object=MibTableColumn
ethIfStatsInJabberPkts=_EthIfStatsInJabberPkts_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,6),_EthIfStatsInJabberPkts_Type())
ethIfStatsInJabberPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsInJabberPkts.setStatus(_A)
_EthIfStatsInL2CPDiscardPkts_Type=Counter64
_EthIfStatsInL2CPDiscardPkts_Object=MibTableColumn
ethIfStatsInL2CPDiscardPkts=_EthIfStatsInL2CPDiscardPkts_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,7),_EthIfStatsInL2CPDiscardPkts_Type())
ethIfStatsInL2CPDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsInL2CPDiscardPkts.setStatus(_A)
_EthIfStatsInCFMDiscardPkts_Type=Counter64
_EthIfStatsInCFMDiscardPkts_Object=MibTableColumn
ethIfStatsInCFMDiscardPkts=_EthIfStatsInCFMDiscardPkts_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,8),_EthIfStatsInCFMDiscardPkts_Type())
ethIfStatsInCFMDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsInCFMDiscardPkts.setStatus(_A)
_EthIfStatsInACLDiscardPkts_Type=Counter64
_EthIfStatsInACLDiscardPkts_Object=MibTableColumn
ethIfStatsInACLDiscardPkts=_EthIfStatsInACLDiscardPkts_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,9),_EthIfStatsInACLDiscardPkts_Type())
ethIfStatsInACLDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsInACLDiscardPkts.setStatus(_A)
_EthIfStatsInFCSErrorPkts_Type=Counter64
_EthIfStatsInFCSErrorPkts_Object=MibTableColumn
ethIfStatsInFCSErrorPkts=_EthIfStatsInFCSErrorPkts_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,10),_EthIfStatsInFCSErrorPkts_Type())
ethIfStatsInFCSErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsInFCSErrorPkts.setStatus(_A)
_EthIfStatsInMacOverflowPkts_Type=Counter64
_EthIfStatsInMacOverflowPkts_Object=MibTableColumn
ethIfStatsInMacOverflowPkts=_EthIfStatsInMacOverflowPkts_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,11),_EthIfStatsInMacOverflowPkts_Type())
ethIfStatsInMacOverflowPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsInMacOverflowPkts.setStatus(_A)
_EthIfStatsInternalMacReceiveErrors_Type=Counter64
_EthIfStatsInternalMacReceiveErrors_Object=MibTableColumn
ethIfStatsInternalMacReceiveErrors=_EthIfStatsInternalMacReceiveErrors_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,12),_EthIfStatsInternalMacReceiveErrors_Type())
ethIfStatsInternalMacReceiveErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsInternalMacReceiveErrors.setStatus(_A)
_EthIfStatsInUndersizePkts_Type=Counter64
_EthIfStatsInUndersizePkts_Object=MibTableColumn
ethIfStatsInUndersizePkts=_EthIfStatsInUndersizePkts_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,13),_EthIfStatsInUndersizePkts_Type())
ethIfStatsInUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsInUndersizePkts.setStatus(_A)
_EthIfStatsInPkts64Octets_Type=Counter64
_EthIfStatsInPkts64Octets_Object=MibTableColumn
ethIfStatsInPkts64Octets=_EthIfStatsInPkts64Octets_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,14),_EthIfStatsInPkts64Octets_Type())
ethIfStatsInPkts64Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsInPkts64Octets.setStatus(_A)
_EthIfStatsInPkts65to127Octets_Type=Counter64
_EthIfStatsInPkts65to127Octets_Object=MibTableColumn
ethIfStatsInPkts65to127Octets=_EthIfStatsInPkts65to127Octets_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,15),_EthIfStatsInPkts65to127Octets_Type())
ethIfStatsInPkts65to127Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsInPkts65to127Octets.setStatus(_A)
_EthIfStatsInPkts128to255Octets_Type=Counter64
_EthIfStatsInPkts128to255Octets_Object=MibTableColumn
ethIfStatsInPkts128to255Octets=_EthIfStatsInPkts128to255Octets_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,16),_EthIfStatsInPkts128to255Octets_Type())
ethIfStatsInPkts128to255Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsInPkts128to255Octets.setStatus(_A)
_EthIfStatsInPkts256to511Octets_Type=Counter64
_EthIfStatsInPkts256to511Octets_Object=MibTableColumn
ethIfStatsInPkts256to511Octets=_EthIfStatsInPkts256to511Octets_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,17),_EthIfStatsInPkts256to511Octets_Type())
ethIfStatsInPkts256to511Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsInPkts256to511Octets.setStatus(_A)
_EthIfStatsInPkts512to1023Octets_Type=Counter64
_EthIfStatsInPkts512to1023Octets_Object=MibTableColumn
ethIfStatsInPkts512to1023Octets=_EthIfStatsInPkts512to1023Octets_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,18),_EthIfStatsInPkts512to1023Octets_Type())
ethIfStatsInPkts512to1023Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsInPkts512to1023Octets.setStatus(_A)
_EthIfStatsInPkts1024to1518Octets_Type=Counter64
_EthIfStatsInPkts1024to1518Octets_Object=MibTableColumn
ethIfStatsInPkts1024to1518Octets=_EthIfStatsInPkts1024to1518Octets_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,19),_EthIfStatsInPkts1024to1518Octets_Type())
ethIfStatsInPkts1024to1518Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsInPkts1024to1518Octets.setStatus(_A)
_EthIfStatsInPkts1519to2047Octets_Type=Counter64
_EthIfStatsInPkts1519to2047Octets_Object=MibTableColumn
ethIfStatsInPkts1519to2047Octets=_EthIfStatsInPkts1519to2047Octets_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,20),_EthIfStatsInPkts1519to2047Octets_Type())
ethIfStatsInPkts1519to2047Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsInPkts1519to2047Octets.setStatus(_A)
_EthIfStatsInPkts1519toMaxOctets_Type=Counter64
_EthIfStatsInPkts1519toMaxOctets_Object=MibTableColumn
ethIfStatsInPkts1519toMaxOctets=_EthIfStatsInPkts1519toMaxOctets_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,21),_EthIfStatsInPkts1519toMaxOctets_Type())
ethIfStatsInPkts1519toMaxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsInPkts1519toMaxOctets.setStatus(_A)
_EthIfStatsInPkts2048toMaxOctets_Type=Counter64
_EthIfStatsInPkts2048toMaxOctets_Object=MibTableColumn
ethIfStatsInPkts2048toMaxOctets=_EthIfStatsInPkts2048toMaxOctets_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,22),_EthIfStatsInPkts2048toMaxOctets_Type())
ethIfStatsInPkts2048toMaxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsInPkts2048toMaxOctets.setStatus(_A)
_EthIfStatsInOversizePkts_Type=Counter64
_EthIfStatsInOversizePkts_Object=MibTableColumn
ethIfStatsInOversizePkts=_EthIfStatsInOversizePkts_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,23),_EthIfStatsInOversizePkts_Type())
ethIfStatsInOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsInOversizePkts.setStatus(_A)
_EthIfStatsInErrorPkts_Type=Counter64
_EthIfStatsInErrorPkts_Object=MibTableColumn
ethIfStatsInErrorPkts=_EthIfStatsInErrorPkts_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,24),_EthIfStatsInErrorPkts_Type())
ethIfStatsInErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsInErrorPkts.setStatus(_A)
_EthIfStatsOutOctets_Type=Counter64
_EthIfStatsOutOctets_Object=MibTableColumn
ethIfStatsOutOctets=_EthIfStatsOutOctets_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,25),_EthIfStatsOutOctets_Type())
ethIfStatsOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsOutOctets.setStatus(_A)
_EthIfStatsOutPkts_Type=Counter64
_EthIfStatsOutPkts_Object=MibTableColumn
ethIfStatsOutPkts=_EthIfStatsOutPkts_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,26),_EthIfStatsOutPkts_Type())
ethIfStatsOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsOutPkts.setStatus(_A)
_EthIfStatsOutUcastPkts_Type=Counter64
_EthIfStatsOutUcastPkts_Object=MibTableColumn
ethIfStatsOutUcastPkts=_EthIfStatsOutUcastPkts_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,27),_EthIfStatsOutUcastPkts_Type())
ethIfStatsOutUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsOutUcastPkts.setStatus(_A)
_EthIfStatsOutMulticastPkts_Type=Counter64
_EthIfStatsOutMulticastPkts_Object=MibTableColumn
ethIfStatsOutMulticastPkts=_EthIfStatsOutMulticastPkts_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,28),_EthIfStatsOutMulticastPkts_Type())
ethIfStatsOutMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsOutMulticastPkts.setStatus(_A)
_EthIfStatsOutBroadcastPkts_Type=Counter64
_EthIfStatsOutBroadcastPkts_Object=MibTableColumn
ethIfStatsOutBroadcastPkts=_EthIfStatsOutBroadcastPkts_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,29),_EthIfStatsOutBroadcastPkts_Type())
ethIfStatsOutBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsOutBroadcastPkts.setStatus(_A)
_EthIfStatsOutDiscardPkts_Type=Counter64
_EthIfStatsOutDiscardPkts_Object=MibTableColumn
ethIfStatsOutDiscardPkts=_EthIfStatsOutDiscardPkts_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,30),_EthIfStatsOutDiscardPkts_Type())
ethIfStatsOutDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsOutDiscardPkts.setStatus(_A)
_EthIfStatsOutPkts64Octets_Type=Counter64
_EthIfStatsOutPkts64Octets_Object=MibTableColumn
ethIfStatsOutPkts64Octets=_EthIfStatsOutPkts64Octets_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,31),_EthIfStatsOutPkts64Octets_Type())
ethIfStatsOutPkts64Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsOutPkts64Octets.setStatus(_A)
_EthIfStatsOutPkts65to127Octets_Type=Counter64
_EthIfStatsOutPkts65to127Octets_Object=MibTableColumn
ethIfStatsOutPkts65to127Octets=_EthIfStatsOutPkts65to127Octets_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,32),_EthIfStatsOutPkts65to127Octets_Type())
ethIfStatsOutPkts65to127Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsOutPkts65to127Octets.setStatus(_A)
_EthIfStatsOutPkts128to255Octets_Type=Counter64
_EthIfStatsOutPkts128to255Octets_Object=MibTableColumn
ethIfStatsOutPkts128to255Octets=_EthIfStatsOutPkts128to255Octets_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,33),_EthIfStatsOutPkts128to255Octets_Type())
ethIfStatsOutPkts128to255Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsOutPkts128to255Octets.setStatus(_A)
_EthIfStatsOutPkts256to511Octets_Type=Counter64
_EthIfStatsOutPkts256to511Octets_Object=MibTableColumn
ethIfStatsOutPkts256to511Octets=_EthIfStatsOutPkts256to511Octets_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,34),_EthIfStatsOutPkts256to511Octets_Type())
ethIfStatsOutPkts256to511Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsOutPkts256to511Octets.setStatus(_A)
_EthIfStatsOutPkts512to1023Octets_Type=Counter64
_EthIfStatsOutPkts512to1023Octets_Object=MibTableColumn
ethIfStatsOutPkts512to1023Octets=_EthIfStatsOutPkts512to1023Octets_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,35),_EthIfStatsOutPkts512to1023Octets_Type())
ethIfStatsOutPkts512to1023Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsOutPkts512to1023Octets.setStatus(_A)
_EthIfStatsOutPkts1024to1518Octets_Type=Counter64
_EthIfStatsOutPkts1024to1518Octets_Object=MibTableColumn
ethIfStatsOutPkts1024to1518Octets=_EthIfStatsOutPkts1024to1518Octets_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,36),_EthIfStatsOutPkts1024to1518Octets_Type())
ethIfStatsOutPkts1024to1518Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsOutPkts1024to1518Octets.setStatus(_A)
_EthIfStatsOutPkts1519to2047Octets_Type=Counter64
_EthIfStatsOutPkts1519to2047Octets_Object=MibTableColumn
ethIfStatsOutPkts1519to2047Octets=_EthIfStatsOutPkts1519to2047Octets_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,37),_EthIfStatsOutPkts1519to2047Octets_Type())
ethIfStatsOutPkts1519to2047Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsOutPkts1519to2047Octets.setStatus(_A)
_EthIfStatsOutPkts2048toMaxOctets_Type=Counter64
_EthIfStatsOutPkts2048toMaxOctets_Object=MibTableColumn
ethIfStatsOutPkts2048toMaxOctets=_EthIfStatsOutPkts2048toMaxOctets_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,38),_EthIfStatsOutPkts2048toMaxOctets_Type())
ethIfStatsOutPkts2048toMaxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsOutPkts2048toMaxOctets.setStatus(_A)
_EthIfStatsOutOversizePkts_Type=Counter64
_EthIfStatsOutOversizePkts_Object=MibTableColumn
ethIfStatsOutOversizePkts=_EthIfStatsOutOversizePkts_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,39),_EthIfStatsOutOversizePkts_Type())
ethIfStatsOutOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsOutOversizePkts.setStatus(_A)
_EthIfStatsInUnMappedCosFrames_Type=Counter64
_EthIfStatsInUnMappedCosFrames_Object=MibTableColumn
ethIfStatsInUnMappedCosFrames=_EthIfStatsInUnMappedCosFrames_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,40),_EthIfStatsInUnMappedCosFrames_Type())
ethIfStatsInUnMappedCosFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsInUnMappedCosFrames.setStatus(_A)
_EthIfStatsEgressMTUDiscarded_Type=Counter64
_EthIfStatsEgressMTUDiscarded_Object=MibTableColumn
ethIfStatsEgressMTUDiscarded=_EthIfStatsEgressMTUDiscarded_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,42),_EthIfStatsEgressMTUDiscarded_Type())
ethIfStatsEgressMTUDiscarded.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsEgressMTUDiscarded.setStatus(_A)
_EthIfStatsLastEgressMTUDiscardingFlow_Type=RowPointer
_EthIfStatsLastEgressMTUDiscardingFlow_Object=MibTableColumn
ethIfStatsLastEgressMTUDiscardingFlow=_EthIfStatsLastEgressMTUDiscardingFlow_Object((1,3,6,1,4,1,164,3,1,6,1,2,5,1,43),_EthIfStatsLastEgressMTUDiscardingFlow_Type())
ethIfStatsLastEgressMTUDiscardingFlow.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatsLastEgressMTUDiscardingFlow.setStatus(_A)
_EthIfRing_ObjectIdentity=ObjectIdentity
ethIfRing=_EthIfRing_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,1,4))
_EthIfRingEvents_ObjectIdentity=ObjectIdentity
ethIfRingEvents=_EthIfRingEvents_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,1,4,0))
_EthIfRingTable_Object=MibTable
ethIfRingTable=_EthIfRingTable_Object((1,3,6,1,4,1,164,3,1,6,1,4,1))
if mibBuilder.loadTexts:ethIfRingTable.setStatus(_A)
_EthIfRingEntry_Object=MibTableRow
ethIfRingEntry=_EthIfRingEntry_Object((1,3,6,1,4,1,164,3,1,6,1,4,1,1))
ethIfRingEntry.setIndexNames((0,_G,_q))
if mibBuilder.loadTexts:ethIfRingEntry.setStatus(_A)
_EthIfRingIdx_Type=Unsigned32
_EthIfRingIdx_Object=MibTableColumn
ethIfRingIdx=_EthIfRingIdx_Object((1,3,6,1,4,1,164,3,1,6,1,4,1,1,1),_EthIfRingIdx_Type())
ethIfRingIdx.setMaxAccess(_I)
if mibBuilder.loadTexts:ethIfRingIdx.setStatus(_A)
class _EthIfRingAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('down',2),('up',3)))
_EthIfRingAdminStatus_Type.__name__=_D
_EthIfRingAdminStatus_Object=MibTableColumn
ethIfRingAdminStatus=_EthIfRingAdminStatus_Object((1,3,6,1,4,1,164,3,1,6,1,4,1,1,2),_EthIfRingAdminStatus_Type())
ethIfRingAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ethIfRingAdminStatus.setStatus(_A)
_EthIfRingPorts_Type=PortList
_EthIfRingPorts_Object=MibTableColumn
ethIfRingPorts=_EthIfRingPorts_Object((1,3,6,1,4,1,164,3,1,6,1,4,1,1,3),_EthIfRingPorts_Type())
ethIfRingPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:ethIfRingPorts.setStatus(_A)
class _EthIfRingOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('open',2),('close',3)))
_EthIfRingOperStatus_Type.__name__=_D
_EthIfRingOperStatus_Object=MibTableColumn
ethIfRingOperStatus=_EthIfRingOperStatus_Object((1,3,6,1,4,1,164,3,1,6,1,4,1,1,4),_EthIfRingOperStatus_Type())
ethIfRingOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfRingOperStatus.setStatus(_A)
_EthIfRingKeepAliveInterval_Type=Unsigned32
_EthIfRingKeepAliveInterval_Object=MibTableColumn
ethIfRingKeepAliveInterval=_EthIfRingKeepAliveInterval_Object((1,3,6,1,4,1,164,3,1,6,1,4,1,1,5),_EthIfRingKeepAliveInterval_Type())
ethIfRingKeepAliveInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:ethIfRingKeepAliveInterval.setStatus(_A)
_EthIfRingKeepAliveThresh_Type=Unsigned32
_EthIfRingKeepAliveThresh_Object=MibTableColumn
ethIfRingKeepAliveThresh=_EthIfRingKeepAliveThresh_Object((1,3,6,1,4,1,164,3,1,6,1,4,1,1,6),_EthIfRingKeepAliveThresh_Type())
ethIfRingKeepAliveThresh.setMaxAccess(_E)
if mibBuilder.loadTexts:ethIfRingKeepAliveThresh.setStatus(_A)
_EthIfRingKeepAliveVlanId_Type=Unsigned32
_EthIfRingKeepAliveVlanId_Object=MibTableColumn
ethIfRingKeepAliveVlanId=_EthIfRingKeepAliveVlanId_Object((1,3,6,1,4,1,164,3,1,6,1,4,1,1,7),_EthIfRingKeepAliveVlanId_Type())
ethIfRingKeepAliveVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:ethIfRingKeepAliveVlanId.setStatus(_A)
_EthIfRingMultiCastVlanId_Type=Unsigned32
_EthIfRingMultiCastVlanId_Object=MibTableColumn
ethIfRingMultiCastVlanId=_EthIfRingMultiCastVlanId_Object((1,3,6,1,4,1,164,3,1,6,1,4,1,1,8),_EthIfRingMultiCastVlanId_Type())
ethIfRingMultiCastVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:ethIfRingMultiCastVlanId.setStatus(_A)
class _EthIfRingRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,6)));namedValues=NamedValues(*((_c,1),(_r,4),(_s,6)))
_EthIfRingRowStatus_Type.__name__=_D
_EthIfRingRowStatus_Object=MibTableColumn
ethIfRingRowStatus=_EthIfRingRowStatus_Object((1,3,6,1,4,1,164,3,1,6,1,4,1,1,9),_EthIfRingRowStatus_Type())
ethIfRingRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ethIfRingRowStatus.setStatus(_A)
_Erp_ObjectIdentity=ObjectIdentity
erp=_Erp_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,1,4,2))
_ErpTable_Object=MibTable
erpTable=_ErpTable_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1))
if mibBuilder.loadTexts:erpTable.setStatus(_A)
_ErpEntry_Object=MibTableRow
erpEntry=_ErpEntry_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1))
erpEntry.setIndexNames((0,_G,_Z))
if mibBuilder.loadTexts:erpEntry.setStatus(_A)
class _ErpIdx_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ErpIdx_Type.__name__=_Q
_ErpIdx_Object=MibTableColumn
erpIdx=_ErpIdx_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,1),_ErpIdx_Type())
erpIdx.setMaxAccess(_I)
if mibBuilder.loadTexts:erpIdx.setStatus(_A)
_ErpRowStatus_Type=RowStatus
_ErpRowStatus_Object=MibTableColumn
erpRowStatus=_ErpRowStatus_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,2),_ErpRowStatus_Type())
erpRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:erpRowStatus.setStatus(_A)
class _ErpAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('down',2),('up',3)))
_ErpAdminStatus_Type.__name__=_D
_ErpAdminStatus_Object=MibTableColumn
erpAdminStatus=_ErpAdminStatus_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,3),_ErpAdminStatus_Type())
erpAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:erpAdminStatus.setStatus(_A)
class _ErpNodeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('init',1),('idle',2),('protected',3),('manualSwitch',4),('forcedSwitch',5),('pending',6)))
_ErpNodeState_Type.__name__=_D
_ErpNodeState_Object=MibTableColumn
erpNodeState=_ErpNodeState_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,4),_ErpNodeState_Type())
erpNodeState.setMaxAccess(_B)
if mibBuilder.loadTexts:erpNodeState.setStatus(_A)
_ErpBridgeNum_Type=Unsigned32
_ErpBridgeNum_Object=MibTableColumn
erpBridgeNum=_ErpBridgeNum_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,5),_ErpBridgeNum_Type())
erpBridgeNum.setMaxAccess(_F)
if mibBuilder.loadTexts:erpBridgeNum.setStatus(_A)
_ErpEastPort_Type=Integer32
_ErpEastPort_Object=MibTableColumn
erpEastPort=_ErpEastPort_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,6),_ErpEastPort_Type())
erpEastPort.setMaxAccess(_F)
if mibBuilder.loadTexts:erpEastPort.setStatus(_A)
_ErpWestPort_Type=Integer32
_ErpWestPort_Object=MibTableColumn
erpWestPort=_ErpWestPort_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,7),_ErpWestPort_Type())
erpWestPort.setMaxAccess(_F)
if mibBuilder.loadTexts:erpWestPort.setStatus(_A)
class _ErpRplPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_d,2),(_e,3)))
_ErpRplPort_Type.__name__=_D
_ErpRplPort_Object=MibTableColumn
erpRplPort=_ErpRplPort_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,8),_ErpRplPort_Type())
erpRplPort.setMaxAccess(_F)
if mibBuilder.loadTexts:erpRplPort.setStatus(_A)
class _ErpRapsVlanId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_ErpRapsVlanId_Type.__name__=_Q
_ErpRapsVlanId_Object=MibTableColumn
erpRapsVlanId=_ErpRapsVlanId_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,9),_ErpRapsVlanId_Type())
erpRapsVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:erpRapsVlanId.setStatus(_A)
class _ErpOamCfmMel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ErpOamCfmMel_Type.__name__=_Q
_ErpOamCfmMel_Object=MibTableColumn
erpOamCfmMel=_ErpOamCfmMel_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,10),_ErpOamCfmMel_Type())
erpOamCfmMel.setMaxAccess(_F)
if mibBuilder.loadTexts:erpOamCfmMel.setStatus(_A)
_ErpWTR_Type=Unsigned32
_ErpWTR_Object=MibTableColumn
erpWTR=_ErpWTR_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,11),_ErpWTR_Type())
erpWTR.setMaxAccess(_F)
if mibBuilder.loadTexts:erpWTR.setStatus(_A)
_ErpWTRStatus_Type=Unsigned32
_ErpWTRStatus_Object=MibTableColumn
erpWTRStatus=_ErpWTRStatus_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,12),_ErpWTRStatus_Type())
erpWTRStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:erpWTRStatus.setStatus(_A)
_ErpGuardTimer_Type=Unsigned32
_ErpGuardTimer_Object=MibTableColumn
erpGuardTimer=_ErpGuardTimer_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,13),_ErpGuardTimer_Type())
erpGuardTimer.setMaxAccess(_F)
if mibBuilder.loadTexts:erpGuardTimer.setStatus(_A)
_ErpHoldoffTimer_Type=Unsigned32
_ErpHoldoffTimer_Object=MibTableColumn
erpHoldoffTimer=_ErpHoldoffTimer_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,14),_ErpHoldoffTimer_Type())
erpHoldoffTimer.setMaxAccess(_F)
if mibBuilder.loadTexts:erpHoldoffTimer.setStatus(_A)
class _ErpForceSfCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6)));namedValues=NamedValues(*(('off',2),('eastOn',3),('westOn',4),('eastClear',5),('westClear',6)))
_ErpForceSfCmd_Type.__name__=_D
_ErpForceSfCmd_Object=MibTableColumn
erpForceSfCmd=_ErpForceSfCmd_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,15),_ErpForceSfCmd_Type())
erpForceSfCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:erpForceSfCmd.setStatus(_A)
class _ErpClearStatistics_Type(Bits):namedValues=NamedValues(*((_d,0),(_e,1)))
_ErpClearStatistics_Type.__name__=_Y
_ErpClearStatistics_Object=MibTableColumn
erpClearStatistics=_ErpClearStatistics_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,16),_ErpClearStatistics_Type())
erpClearStatistics.setMaxAccess(_F)
if mibBuilder.loadTexts:erpClearStatistics.setStatus(_A)
_ErpRapsVlanPriority_Type=Unsigned32
_ErpRapsVlanPriority_Object=MibTableColumn
erpRapsVlanPriority=_ErpRapsVlanPriority_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,17),_ErpRapsVlanPriority_Type())
erpRapsVlanPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:erpRapsVlanPriority.setStatus(_A)
class _ErpDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ErpDescr_Type.__name__=_a
_ErpDescr_Object=MibTableColumn
erpDescr=_ErpDescr_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,18),_ErpDescr_Type())
erpDescr.setMaxAccess(_F)
if mibBuilder.loadTexts:erpDescr.setStatus(_A)
class _ErpRingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('majorRing',1),('subRing',2)))
_ErpRingType_Type.__name__=_D
_ErpRingType_Object=MibTableColumn
erpRingType=_ErpRingType_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,19),_ErpRingType_Type())
erpRingType.setMaxAccess(_F)
if mibBuilder.loadTexts:erpRingType.setStatus(_A)
_ErpWTBStatus_Type=Unsigned32
_ErpWTBStatus_Object=MibTableColumn
erpWTBStatus=_ErpWTBStatus_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,20),_ErpWTBStatus_Type())
erpWTBStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:erpWTBStatus.setStatus(_A)
class _ErpRevertiveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_S,2),(_T,3)))
_ErpRevertiveMode_Type.__name__=_D
_ErpRevertiveMode_Object=MibTableColumn
erpRevertiveMode=_ErpRevertiveMode_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,21),_ErpRevertiveMode_Type())
erpRevertiveMode.setMaxAccess(_F)
if mibBuilder.loadTexts:erpRevertiveMode.setStatus(_A)
_ErpBackwardCompatibility_Type=TruthValue
_ErpBackwardCompatibility_Object=MibTableColumn
erpBackwardCompatibility=_ErpBackwardCompatibility_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,22),_ErpBackwardCompatibility_Type())
erpBackwardCompatibility.setMaxAccess(_F)
if mibBuilder.loadTexts:erpBackwardCompatibility.setStatus(_A)
class _ErpTopologyChangepropogation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_S,2),(_T,3)))
_ErpTopologyChangepropogation_Type.__name__=_D
_ErpTopologyChangepropogation_Object=MibTableColumn
erpTopologyChangepropogation=_ErpTopologyChangepropogation_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,23),_ErpTopologyChangepropogation_Type())
erpTopologyChangepropogation.setMaxAccess(_F)
if mibBuilder.loadTexts:erpTopologyChangepropogation.setStatus(_A)
_ErpInterconnectionNode_Type=TruthValue
_ErpInterconnectionNode_Object=MibTableColumn
erpInterconnectionNode=_ErpInterconnectionNode_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,24),_ErpInterconnectionNode_Type())
erpInterconnectionNode.setMaxAccess(_F)
if mibBuilder.loadTexts:erpInterconnectionNode.setStatus(_A)
class _ErpCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('force',1),(_m,2),('clear',3),('noCommand',4)))
_ErpCommand_Type.__name__=_D
_ErpCommand_Object=MibTableColumn
erpCommand=_ErpCommand_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,25),_ErpCommand_Type())
erpCommand.setMaxAccess(_F)
if mibBuilder.loadTexts:erpCommand.setStatus(_A)
class _ErpCommandParam_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('eastPort',2),('westPort',3)))
_ErpCommandParam_Type.__name__=_D
_ErpCommandParam_Object=MibTableColumn
erpCommandParam=_ErpCommandParam_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,26),_ErpCommandParam_Type())
erpCommandParam.setMaxAccess(_F)
if mibBuilder.loadTexts:erpCommandParam.setStatus(_A)
_ErpEastPhyPort_Type=Unsigned32
_ErpEastPhyPort_Object=MibTableColumn
erpEastPhyPort=_ErpEastPhyPort_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,27),_ErpEastPhyPort_Type())
erpEastPhyPort.setMaxAccess(_F)
if mibBuilder.loadTexts:erpEastPhyPort.setStatus(_A)
_ErpWestPhyPort_Type=Unsigned32
_ErpWestPhyPort_Object=MibTableColumn
erpWestPhyPort=_ErpWestPhyPort_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,28),_ErpWestPhyPort_Type())
erpWestPhyPort.setMaxAccess(_F)
if mibBuilder.loadTexts:erpWestPhyPort.setStatus(_A)
_ErpCosMapProfile_Type=Unsigned32
_ErpCosMapProfile_Object=MibTableColumn
erpCosMapProfile=_ErpCosMapProfile_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,29),_ErpCosMapProfile_Type())
erpCosMapProfile.setMaxAccess(_F)
if mibBuilder.loadTexts:erpCosMapProfile.setStatus(_A)
class _ErpVirtualChannel_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_S,2),(_T,3)))
_ErpVirtualChannel_Type.__name__=_D
_ErpVirtualChannel_Object=MibTableColumn
erpVirtualChannel=_ErpVirtualChannel_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,30),_ErpVirtualChannel_Type())
erpVirtualChannel.setMaxAccess(_F)
if mibBuilder.loadTexts:erpVirtualChannel.setStatus(_A)
class _ErpPassthroughVids_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_ErpPassthroughVids_Type.__name__=_W
_ErpPassthroughVids_Object=MibTableColumn
erpPassthroughVids=_ErpPassthroughVids_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,31),_ErpPassthroughVids_Type())
erpPassthroughVids.setMaxAccess(_F)
if mibBuilder.loadTexts:erpPassthroughVids.setStatus(_A)
class _ErpColorMapProfile_Type(Unsigned32):defaultValue=0
_ErpColorMapProfile_Type.__name__=_Q
_ErpColorMapProfile_Object=MibTableColumn
erpColorMapProfile=_ErpColorMapProfile_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,32),_ErpColorMapProfile_Type())
erpColorMapProfile.setMaxAccess(_F)
if mibBuilder.loadTexts:erpColorMapProfile.setStatus(_A)
_ErpPassthroughQueueBlockEast_Type=RowPointer
_ErpPassthroughQueueBlockEast_Object=MibTableColumn
erpPassthroughQueueBlockEast=_ErpPassthroughQueueBlockEast_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,33),_ErpPassthroughQueueBlockEast_Type())
erpPassthroughQueueBlockEast.setMaxAccess(_F)
if mibBuilder.loadTexts:erpPassthroughQueueBlockEast.setStatus(_A)
_ErpPassthroughQueueBlockWest_Type=RowPointer
_ErpPassthroughQueueBlockWest_Object=MibTableColumn
erpPassthroughQueueBlockWest=_ErpPassthroughQueueBlockWest_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,1,1,34),_ErpPassthroughQueueBlockWest_Type())
erpPassthroughQueueBlockWest.setMaxAccess(_F)
if mibBuilder.loadTexts:erpPassthroughQueueBlockWest.setStatus(_A)
_ErpPortTable_Object=MibTable
erpPortTable=_ErpPortTable_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,2))
if mibBuilder.loadTexts:erpPortTable.setStatus(_A)
_ErpPortEntry_Object=MibTableRow
erpPortEntry=_ErpPortEntry_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,2,1))
erpPortEntry.setIndexNames((0,_G,_Z),(0,_G,_t))
if mibBuilder.loadTexts:erpPortEntry.setStatus(_A)
class _ErpPortIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_d,1),(_e,2)))
_ErpPortIdx_Type.__name__=_D
_ErpPortIdx_Object=MibTableColumn
erpPortIdx=_ErpPortIdx_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,2,1,1),_ErpPortIdx_Type())
erpPortIdx.setMaxAccess(_I)
if mibBuilder.loadTexts:erpPortIdx.setStatus(_A)
_ErpPortOamCfmMdId_Type=Unsigned32
_ErpPortOamCfmMdId_Object=MibTableColumn
erpPortOamCfmMdId=_ErpPortOamCfmMdId_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,2,1,2),_ErpPortOamCfmMdId_Type())
erpPortOamCfmMdId.setMaxAccess(_E)
if mibBuilder.loadTexts:erpPortOamCfmMdId.setStatus(_A)
_ErpPortOamCfmMaId_Type=Unsigned32
_ErpPortOamCfmMaId_Object=MibTableColumn
erpPortOamCfmMaId=_ErpPortOamCfmMaId_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,2,1,3),_ErpPortOamCfmMaId_Type())
erpPortOamCfmMaId.setMaxAccess(_E)
if mibBuilder.loadTexts:erpPortOamCfmMaId.setStatus(_A)
_ErpPortOamCfmMepId_Type=Unsigned32
_ErpPortOamCfmMepId_Object=MibTableColumn
erpPortOamCfmMepId=_ErpPortOamCfmMepId_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,2,1,4),_ErpPortOamCfmMepId_Type())
erpPortOamCfmMepId.setMaxAccess(_E)
if mibBuilder.loadTexts:erpPortOamCfmMepId.setStatus(_A)
class _ErpPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*(('blocked',2),('forwarding',3),('rAPSAndDataChannelBlocked',4)))
_ErpPortState_Type.__name__=_D
_ErpPortState_Object=MibTableColumn
erpPortState=_ErpPortState_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,2,1,5),_ErpPortState_Type())
erpPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:erpPortState.setStatus(_A)
class _ErpPortLocalSfSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('serverLayer',2),('oamCfm',3),('forced',4)))
_ErpPortLocalSfSource_Type.__name__=_D
_ErpPortLocalSfSource_Object=MibTableColumn
erpPortLocalSfSource=_ErpPortLocalSfSource_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,2,1,6),_ErpPortLocalSfSource_Type())
erpPortLocalSfSource.setMaxAccess(_B)
if mibBuilder.loadTexts:erpPortLocalSfSource.setStatus(_A)
_ErpPortRapsRxValidMsg_Type=Counter32
_ErpPortRapsRxValidMsg_Object=MibTableColumn
erpPortRapsRxValidMsg=_ErpPortRapsRxValidMsg_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,2,1,7),_ErpPortRapsRxValidMsg_Type())
erpPortRapsRxValidMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:erpPortRapsRxValidMsg.setStatus(_A)
_ErpPortRapsRxInvalidMsg_Type=Counter32
_ErpPortRapsRxInvalidMsg_Object=MibTableColumn
erpPortRapsRxInvalidMsg=_ErpPortRapsRxInvalidMsg_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,2,1,8),_ErpPortRapsRxInvalidMsg_Type())
erpPortRapsRxInvalidMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:erpPortRapsRxInvalidMsg.setStatus(_A)
_ErpPortRapsRxSfMsg_Type=Counter32
_ErpPortRapsRxSfMsg_Object=MibTableColumn
erpPortRapsRxSfMsg=_ErpPortRapsRxSfMsg_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,2,1,9),_ErpPortRapsRxSfMsg_Type())
erpPortRapsRxSfMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:erpPortRapsRxSfMsg.setStatus(_A)
_ErpPortRapsRxNrMsg_Type=Counter32
_ErpPortRapsRxNrMsg_Object=MibTableColumn
erpPortRapsRxNrMsg=_ErpPortRapsRxNrMsg_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,2,1,10),_ErpPortRapsRxNrMsg_Type())
erpPortRapsRxNrMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:erpPortRapsRxNrMsg.setStatus(_A)
_ErpPortRapsRxNrrbMsg_Type=Counter32
_ErpPortRapsRxNrrbMsg_Object=MibTableColumn
erpPortRapsRxNrrbMsg=_ErpPortRapsRxNrrbMsg_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,2,1,11),_ErpPortRapsRxNrrbMsg_Type())
erpPortRapsRxNrrbMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:erpPortRapsRxNrrbMsg.setStatus(_A)
_ErpPortRapsTxValidMsg_Type=Counter32
_ErpPortRapsTxValidMsg_Object=MibTableColumn
erpPortRapsTxValidMsg=_ErpPortRapsTxValidMsg_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,2,1,12),_ErpPortRapsTxValidMsg_Type())
erpPortRapsTxValidMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:erpPortRapsTxValidMsg.setStatus(_A)
_ErpPortRapsTxInvalidMsg_Type=Counter32
_ErpPortRapsTxInvalidMsg_Object=MibTableColumn
erpPortRapsTxInvalidMsg=_ErpPortRapsTxInvalidMsg_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,2,1,13),_ErpPortRapsTxInvalidMsg_Type())
erpPortRapsTxInvalidMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:erpPortRapsTxInvalidMsg.setStatus(_A)
_ErpPortRapsTxSfMsg_Type=Counter32
_ErpPortRapsTxSfMsg_Object=MibTableColumn
erpPortRapsTxSfMsg=_ErpPortRapsTxSfMsg_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,2,1,14),_ErpPortRapsTxSfMsg_Type())
erpPortRapsTxSfMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:erpPortRapsTxSfMsg.setStatus(_A)
_ErpPortRapsTxNrMsg_Type=Counter32
_ErpPortRapsTxNrMsg_Object=MibTableColumn
erpPortRapsTxNrMsg=_ErpPortRapsTxNrMsg_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,2,1,15),_ErpPortRapsTxNrMsg_Type())
erpPortRapsTxNrMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:erpPortRapsTxNrMsg.setStatus(_A)
_ErpPortRapsTxNrrbMsg_Type=Counter32
_ErpPortRapsTxNrrbMsg_Object=MibTableColumn
erpPortRapsTxNrrbMsg=_ErpPortRapsTxNrrbMsg_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,2,1,16),_ErpPortRapsTxNrrbMsg_Type())
erpPortRapsTxNrrbMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:erpPortRapsTxNrrbMsg.setStatus(_A)
class _ErpPortDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ErpPortDescr_Type.__name__=_a
_ErpPortDescr_Object=MibTableColumn
erpPortDescr=_ErpPortDescr_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,2,1,17),_ErpPortDescr_Type())
erpPortDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:erpPortDescr.setStatus(_A)
_ErpPortRapsRxFsMsg_Type=Counter32
_ErpPortRapsRxFsMsg_Object=MibTableColumn
erpPortRapsRxFsMsg=_ErpPortRapsRxFsMsg_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,2,1,18),_ErpPortRapsRxFsMsg_Type())
erpPortRapsRxFsMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:erpPortRapsRxFsMsg.setStatus(_A)
_ErpPortRapsRxMsMsg_Type=Counter32
_ErpPortRapsRxMsMsg_Object=MibTableColumn
erpPortRapsRxMsMsg=_ErpPortRapsRxMsMsg_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,2,1,19),_ErpPortRapsRxMsMsg_Type())
erpPortRapsRxMsMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:erpPortRapsRxMsMsg.setStatus(_A)
_ErpPortRapsRxDnfMsg_Type=Counter32
_ErpPortRapsRxDnfMsg_Object=MibTableColumn
erpPortRapsRxDnfMsg=_ErpPortRapsRxDnfMsg_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,2,1,20),_ErpPortRapsRxDnfMsg_Type())
erpPortRapsRxDnfMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:erpPortRapsRxDnfMsg.setStatus(_A)
_ErpPortRapsRxEvtMsg_Type=Counter32
_ErpPortRapsRxEvtMsg_Object=MibTableColumn
erpPortRapsRxEvtMsg=_ErpPortRapsRxEvtMsg_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,2,1,21),_ErpPortRapsRxEvtMsg_Type())
erpPortRapsRxEvtMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:erpPortRapsRxEvtMsg.setStatus(_A)
_ErpPortRapsTxFsMsg_Type=Counter32
_ErpPortRapsTxFsMsg_Object=MibTableColumn
erpPortRapsTxFsMsg=_ErpPortRapsTxFsMsg_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,2,1,22),_ErpPortRapsTxFsMsg_Type())
erpPortRapsTxFsMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:erpPortRapsTxFsMsg.setStatus(_A)
_ErpPortRapsTxMsMsg_Type=Counter32
_ErpPortRapsTxMsMsg_Object=MibTableColumn
erpPortRapsTxMsMsg=_ErpPortRapsTxMsMsg_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,2,1,23),_ErpPortRapsTxMsMsg_Type())
erpPortRapsTxMsMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:erpPortRapsTxMsMsg.setStatus(_A)
_ErpPortRapsTxDnfMsg_Type=Counter32
_ErpPortRapsTxDnfMsg_Object=MibTableColumn
erpPortRapsTxDnfMsg=_ErpPortRapsTxDnfMsg_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,2,1,24),_ErpPortRapsTxDnfMsg_Type())
erpPortRapsTxDnfMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:erpPortRapsTxDnfMsg.setStatus(_A)
_ErpPortRapsTxEvtMsg_Type=Counter32
_ErpPortRapsTxEvtMsg_Object=MibTableColumn
erpPortRapsTxEvtMsg=_ErpPortRapsTxEvtMsg_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,2,1,25),_ErpPortRapsTxEvtMsg_Type())
erpPortRapsTxEvtMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:erpPortRapsTxEvtMsg.setStatus(_A)
class _ErpPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('nodePort',1),('rpl',2),('neighbor',3),('nextNeighbor',4)))
_ErpPortType_Type.__name__=_D
_ErpPortType_Object=MibTableColumn
erpPortType=_ErpPortType_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,2,1,26),_ErpPortType_Type())
erpPortType.setMaxAccess(_E)
if mibBuilder.loadTexts:erpPortType.setStatus(_A)
_ErpSubRingTable_Object=MibTable
erpSubRingTable=_ErpSubRingTable_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,4))
if mibBuilder.loadTexts:erpSubRingTable.setStatus(_A)
_ErpSubRingEntry_Object=MibTableRow
erpSubRingEntry=_ErpSubRingEntry_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,4,1))
erpSubRingEntry.setIndexNames((0,_G,_u),(0,_G,_v))
if mibBuilder.loadTexts:erpSubRingEntry.setStatus(_A)
class _ErpSubRingMajorRingIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ErpSubRingMajorRingIndex_Type.__name__=_Q
_ErpSubRingMajorRingIndex_Object=MibTableColumn
erpSubRingMajorRingIndex=_ErpSubRingMajorRingIndex_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,4,1,1),_ErpSubRingMajorRingIndex_Type())
erpSubRingMajorRingIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:erpSubRingMajorRingIndex.setStatus(_A)
class _ErpSubRingSubRingIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ErpSubRingSubRingIndex_Type.__name__=_Q
_ErpSubRingSubRingIndex_Object=MibTableColumn
erpSubRingSubRingIndex=_ErpSubRingSubRingIndex_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,4,1,2),_ErpSubRingSubRingIndex_Type())
erpSubRingSubRingIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:erpSubRingSubRingIndex.setStatus(_A)
_ErpSubRingRowStatus_Type=RowStatus
_ErpSubRingRowStatus_Object=MibTableColumn
erpSubRingRowStatus=_ErpSubRingRowStatus_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,4,1,3),_ErpSubRingRowStatus_Type())
erpSubRingRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:erpSubRingRowStatus.setStatus(_A)
class _ErpSubRingVirtualChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_S,2),(_T,3)))
_ErpSubRingVirtualChannel_Type.__name__=_D
_ErpSubRingVirtualChannel_Object=MibTableColumn
erpSubRingVirtualChannel=_ErpSubRingVirtualChannel_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,4,1,4),_ErpSubRingVirtualChannel_Type())
erpSubRingVirtualChannel.setMaxAccess(_F)
if mibBuilder.loadTexts:erpSubRingVirtualChannel.setStatus('deprecated')
class _ErpSubRingRAPSVlanId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_ErpSubRingRAPSVlanId_Type.__name__=_Q
_ErpSubRingRAPSVlanId_Object=MibTableColumn
erpSubRingRAPSVlanId=_ErpSubRingRAPSVlanId_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,4,1,5),_ErpSubRingRAPSVlanId_Type())
erpSubRingRAPSVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:erpSubRingRAPSVlanId.setStatus(_A)
_ErpSubRingRAPSVlanPriority_Type=Unsigned32
_ErpSubRingRAPSVlanPriority_Object=MibTableColumn
erpSubRingRAPSVlanPriority=_ErpSubRingRAPSVlanPriority_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,4,1,6),_ErpSubRingRAPSVlanPriority_Type())
erpSubRingRAPSVlanPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:erpSubRingRAPSVlanPriority.setStatus(_A)
_ErpVlanTable_Object=MibTable
erpVlanTable=_ErpVlanTable_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,5))
if mibBuilder.loadTexts:erpVlanTable.setStatus(_A)
_ErpVlanEntry_Object=MibTableRow
erpVlanEntry=_ErpVlanEntry_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,5,1))
erpVlanEntry.setIndexNames((0,_G,_Z),(0,_G,_w))
if mibBuilder.loadTexts:erpVlanEntry.setStatus(_A)
class _ErpVlanIdx_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ErpVlanIdx_Type.__name__=_Q
_ErpVlanIdx_Object=MibTableColumn
erpVlanIdx=_ErpVlanIdx_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,5,1,1),_ErpVlanIdx_Type())
erpVlanIdx.setMaxAccess(_I)
if mibBuilder.loadTexts:erpVlanIdx.setStatus(_A)
_ErpVlanRowStatus_Type=RowStatus
_ErpVlanRowStatus_Object=MibTableColumn
erpVlanRowStatus=_ErpVlanRowStatus_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,5,1,2),_ErpVlanRowStatus_Type())
erpVlanRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:erpVlanRowStatus.setStatus(_A)
_ErpVlanEastQblock_Type=ObjectIdentifier
_ErpVlanEastQblock_Object=MibTableColumn
erpVlanEastQblock=_ErpVlanEastQblock_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,5,1,3),_ErpVlanEastQblock_Type())
erpVlanEastQblock.setMaxAccess(_F)
if mibBuilder.loadTexts:erpVlanEastQblock.setStatus(_A)
_ErpVlanWestQblock_Type=ObjectIdentifier
_ErpVlanWestQblock_Object=MibTableColumn
erpVlanWestQblock=_ErpVlanWestQblock_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,5,1,4),_ErpVlanWestQblock_Type())
erpVlanWestQblock.setMaxAccess(_F)
if mibBuilder.loadTexts:erpVlanWestQblock.setStatus(_A)
_ErpVlanServiceIdName_Type=SnmpAdminString
_ErpVlanServiceIdName_Object=MibTableColumn
erpVlanServiceIdName=_ErpVlanServiceIdName_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,5,1,5),_ErpVlanServiceIdName_Type())
erpVlanServiceIdName.setMaxAccess(_F)
if mibBuilder.loadTexts:erpVlanServiceIdName.setStatus(_A)
_ErpVlanMajorEastQblock_Type=ObjectIdentifier
_ErpVlanMajorEastQblock_Object=MibTableColumn
erpVlanMajorEastQblock=_ErpVlanMajorEastQblock_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,5,1,6),_ErpVlanMajorEastQblock_Type())
erpVlanMajorEastQblock.setMaxAccess(_F)
if mibBuilder.loadTexts:erpVlanMajorEastQblock.setStatus(_A)
_ErpVlanMajorWestQblock_Type=ObjectIdentifier
_ErpVlanMajorWestQblock_Object=MibTableColumn
erpVlanMajorWestQblock=_ErpVlanMajorWestQblock_Object((1,3,6,1,4,1,164,3,1,6,1,4,2,5,1,7),_ErpVlanMajorWestQblock_Type())
erpVlanMajorWestQblock.setMaxAccess(_F)
if mibBuilder.loadTexts:erpVlanMajorWestQblock.setStatus(_A)
_EthIfStorming_ObjectIdentity=ObjectIdentity
ethIfStorming=_EthIfStorming_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,1,5))
_EthIfStormTable_Object=MibTable
ethIfStormTable=_EthIfStormTable_Object((1,3,6,1,4,1,164,3,1,6,1,5,1))
if mibBuilder.loadTexts:ethIfStormTable.setStatus(_A)
_EthIfStormEntry_Object=MibTableRow
ethIfStormEntry=_EthIfStormEntry_Object((1,3,6,1,4,1,164,3,1,6,1,5,1,1))
ethIfStormEntry.setIndexNames((0,_G,_x),(0,_G,_y),(0,_G,_z),(0,_G,_A0))
if mibBuilder.loadTexts:ethIfStormEntry.setStatus(_A)
class _EthIfStormCnfgIdx_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_EthIfStormCnfgIdx_Type.__name__=_Q
_EthIfStormCnfgIdx_Object=MibTableColumn
ethIfStormCnfgIdx=_EthIfStormCnfgIdx_Object((1,3,6,1,4,1,164,3,1,6,1,5,1,1,1),_EthIfStormCnfgIdx_Type())
ethIfStormCnfgIdx.setMaxAccess(_I)
if mibBuilder.loadTexts:ethIfStormCnfgIdx.setStatus(_A)
_EthIfStormIfIdx_Type=Unsigned32
_EthIfStormIfIdx_Object=MibTableColumn
ethIfStormIfIdx=_EthIfStormIfIdx_Object((1,3,6,1,4,1,164,3,1,6,1,5,1,1,2),_EthIfStormIfIdx_Type())
ethIfStormIfIdx.setMaxAccess(_I)
if mibBuilder.loadTexts:ethIfStormIfIdx.setStatus(_A)
class _EthIfStormDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('all',1),('ingress',2),('egress',3)))
_EthIfStormDirection_Type.__name__=_D
_EthIfStormDirection_Object=MibTableColumn
ethIfStormDirection=_EthIfStormDirection_Object((1,3,6,1,4,1,164,3,1,6,1,5,1,1,3),_EthIfStormDirection_Type())
ethIfStormDirection.setMaxAccess(_I)
if mibBuilder.loadTexts:ethIfStormDirection.setStatus(_A)
class _EthIfStormPacketType_Type(Bits):namedValues=NamedValues(*(('unknownUnicast',0),('broadcast',1),('multicast',2)))
_EthIfStormPacketType_Type.__name__=_Y
_EthIfStormPacketType_Object=MibTableColumn
ethIfStormPacketType=_EthIfStormPacketType_Object((1,3,6,1,4,1,164,3,1,6,1,5,1,1,4),_EthIfStormPacketType_Type())
ethIfStormPacketType.setMaxAccess(_I)
if mibBuilder.loadTexts:ethIfStormPacketType.setStatus(_A)
class _EthIfStormCtrlEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_S,2),(_T,3)))
_EthIfStormCtrlEnable_Type.__name__=_D
_EthIfStormCtrlEnable_Object=MibTableColumn
ethIfStormCtrlEnable=_EthIfStormCtrlEnable_Object((1,3,6,1,4,1,164,3,1,6,1,5,1,1,5),_EthIfStormCtrlEnable_Type())
ethIfStormCtrlEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ethIfStormCtrlEnable.setStatus(_A)
_EthIfStormMaxRate_Type=Unsigned32
_EthIfStormMaxRate_Object=MibTableColumn
ethIfStormMaxRate=_EthIfStormMaxRate_Object((1,3,6,1,4,1,164,3,1,6,1,5,1,1,6),_EthIfStormMaxRate_Type())
ethIfStormMaxRate.setMaxAccess(_E)
if mibBuilder.loadTexts:ethIfStormMaxRate.setStatus(_A)
_EthIfOamEfm_ObjectIdentity=ObjectIdentity
ethIfOamEfm=_EthIfOamEfm_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,1,6))
_Dot3OamEvents_ObjectIdentity=ObjectIdentity
dot3OamEvents=_Dot3OamEvents_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,1,6,0))
_Dot3OamDescrTable_Object=MibTable
dot3OamDescrTable=_Dot3OamDescrTable_Object((1,3,6,1,4,1,164,3,1,6,1,6,1))
if mibBuilder.loadTexts:dot3OamDescrTable.setStatus(_A)
_Dot3OamDescrEntry_Object=MibTableRow
dot3OamDescrEntry=_Dot3OamDescrEntry_Object((1,3,6,1,4,1,164,3,1,6,1,6,1,1))
dot3OamDescrEntry.setIndexNames((0,_G,_A1))
if mibBuilder.loadTexts:dot3OamDescrEntry.setStatus(_A)
class _Dot3OamDescrId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_Dot3OamDescrId_Type.__name__=_Q
_Dot3OamDescrId_Object=MibTableColumn
dot3OamDescrId=_Dot3OamDescrId_Object((1,3,6,1,4,1,164,3,1,6,1,6,1,1,1),_Dot3OamDescrId_Type())
dot3OamDescrId.setMaxAccess(_I)
if mibBuilder.loadTexts:dot3OamDescrId.setStatus(_A)
_Dot3OamDescrRowStatus_Type=RowStatus
_Dot3OamDescrRowStatus_Object=MibTableColumn
dot3OamDescrRowStatus=_Dot3OamDescrRowStatus_Object((1,3,6,1,4,1,164,3,1,6,1,6,1,1,2),_Dot3OamDescrRowStatus_Type())
dot3OamDescrRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:dot3OamDescrRowStatus.setStatus(_A)
class _Dot3OamDescrMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_c,2)))
_Dot3OamDescrMode_Type.__name__=_D
_Dot3OamDescrMode_Object=MibTableColumn
dot3OamDescrMode=_Dot3OamDescrMode_Object((1,3,6,1,4,1,164,3,1,6,1,6,1,1,3),_Dot3OamDescrMode_Type())
dot3OamDescrMode.setMaxAccess(_F)
if mibBuilder.loadTexts:dot3OamDescrMode.setStatus(_A)
class _Dot3OamDescrLbRxOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ignore',1),('process',2)))
_Dot3OamDescrLbRxOperation_Type.__name__=_D
_Dot3OamDescrLbRxOperation_Object=MibTableColumn
dot3OamDescrLbRxOperation=_Dot3OamDescrLbRxOperation_Object((1,3,6,1,4,1,164,3,1,6,1,6,1,1,4),_Dot3OamDescrLbRxOperation_Type())
dot3OamDescrLbRxOperation.setMaxAccess(_F)
if mibBuilder.loadTexts:dot3OamDescrLbRxOperation.setStatus(_A)
_Dot3OamDescrRateLimit_Type=Unsigned32
_Dot3OamDescrRateLimit_Object=MibTableColumn
dot3OamDescrRateLimit=_Dot3OamDescrRateLimit_Object((1,3,6,1,4,1,164,3,1,6,1,6,1,1,5),_Dot3OamDescrRateLimit_Type())
dot3OamDescrRateLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:dot3OamDescrRateLimit.setStatus(_A)
_Dot3OamXTable_Object=MibTable
dot3OamXTable=_Dot3OamXTable_Object((1,3,6,1,4,1,164,3,1,6,1,6,2))
if mibBuilder.loadTexts:dot3OamXTable.setStatus(_A)
_Dot3OamXEntry_Object=MibTableRow
dot3OamXEntry=_Dot3OamXEntry_Object((1,3,6,1,4,1,164,3,1,6,1,6,2,1))
if mibBuilder.loadTexts:dot3OamXEntry.setStatus(_A)
class _Dot3OamXDescrId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_Dot3OamXDescrId_Type.__name__=_Q
_Dot3OamXDescrId_Object=MibTableColumn
dot3OamXDescrId=_Dot3OamXDescrId_Object((1,3,6,1,4,1,164,3,1,6,1,6,2,1,1),_Dot3OamXDescrId_Type())
dot3OamXDescrId.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3OamXDescrId.setStatus(_A)
class _Dot3OamXPeerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unknown',1),('operational',2),('linkFault',3),('dyingGasp',4),('criticalEvent',5)))
_Dot3OamXPeerState_Type.__name__=_D
_Dot3OamXPeerState_Object=MibTableColumn
dot3OamXPeerState=_Dot3OamXPeerState_Object((1,3,6,1,4,1,164,3,1,6,1,6,2,1,2),_Dot3OamXPeerState_Type())
dot3OamXPeerState.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamXPeerState.setStatus(_A)
_EthIfMacLayer_ObjectIdentity=ObjectIdentity
ethIfMacLayer=_EthIfMacLayer_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,1,7))
_EthIfMacLayerEvents_ObjectIdentity=ObjectIdentity
ethIfMacLayerEvents=_EthIfMacLayerEvents_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,1,7,0))
_EthIfSrcMacCtrlTable_Object=MibTable
ethIfSrcMacCtrlTable=_EthIfSrcMacCtrlTable_Object((1,3,6,1,4,1,164,3,1,6,1,7,1))
if mibBuilder.loadTexts:ethIfSrcMacCtrlTable.setStatus(_A)
_EthIfSrcMacCtrlEntry_Object=MibTableRow
ethIfSrcMacCtrlEntry=_EthIfSrcMacCtrlEntry_Object((1,3,6,1,4,1,164,3,1,6,1,7,1,1))
ethIfSrcMacCtrlEntry.setIndexNames((0,_G,_A2),(0,_G,_A3))
if mibBuilder.loadTexts:ethIfSrcMacCtrlEntry.setStatus(_A)
_EthIfSrcMacCtrlIndex_Type=Unsigned32
_EthIfSrcMacCtrlIndex_Object=MibTableColumn
ethIfSrcMacCtrlIndex=_EthIfSrcMacCtrlIndex_Object((1,3,6,1,4,1,164,3,1,6,1,7,1,1,1),_EthIfSrcMacCtrlIndex_Type())
ethIfSrcMacCtrlIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ethIfSrcMacCtrlIndex.setStatus(_A)
_EthIfSrcMacCtrlIdx2_Type=Unsigned32
_EthIfSrcMacCtrlIdx2_Object=MibTableColumn
ethIfSrcMacCtrlIdx2=_EthIfSrcMacCtrlIdx2_Object((1,3,6,1,4,1,164,3,1,6,1,7,1,1,2),_EthIfSrcMacCtrlIdx2_Type())
ethIfSrcMacCtrlIdx2.setMaxAccess(_I)
if mibBuilder.loadTexts:ethIfSrcMacCtrlIdx2.setStatus(_A)
class _EthIfSrcMacCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_S,2),(_T,3)))
_EthIfSrcMacCtrl_Type.__name__=_D
_EthIfSrcMacCtrl_Object=MibTableColumn
ethIfSrcMacCtrl=_EthIfSrcMacCtrl_Object((1,3,6,1,4,1,164,3,1,6,1,7,1,1,3),_EthIfSrcMacCtrl_Type())
ethIfSrcMacCtrl.setMaxAccess(_E)
if mibBuilder.loadTexts:ethIfSrcMacCtrl.setStatus(_A)
_EthIfSrcMacCtrlMaxPermitAddr_Type=Unsigned32
_EthIfSrcMacCtrlMaxPermitAddr_Object=MibTableColumn
ethIfSrcMacCtrlMaxPermitAddr=_EthIfSrcMacCtrlMaxPermitAddr_Object((1,3,6,1,4,1,164,3,1,6,1,7,1,1,4),_EthIfSrcMacCtrlMaxPermitAddr_Type())
ethIfSrcMacCtrlMaxPermitAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:ethIfSrcMacCtrlMaxPermitAddr.setStatus(_A)
_EthIfSrcMacCtrlCurNumPermitAddr_Type=Unsigned32
_EthIfSrcMacCtrlCurNumPermitAddr_Object=MibTableColumn
ethIfSrcMacCtrlCurNumPermitAddr=_EthIfSrcMacCtrlCurNumPermitAddr_Object((1,3,6,1,4,1,164,3,1,6,1,7,1,1,5),_EthIfSrcMacCtrlCurNumPermitAddr_Type())
ethIfSrcMacCtrlCurNumPermitAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfSrcMacCtrlCurNumPermitAddr.setStatus(_A)
class _EthIfSrcMacCtrlFlushAddrCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('off',2),('on',3)))
_EthIfSrcMacCtrlFlushAddrCmd_Type.__name__=_D
_EthIfSrcMacCtrlFlushAddrCmd_Object=MibTableColumn
ethIfSrcMacCtrlFlushAddrCmd=_EthIfSrcMacCtrlFlushAddrCmd_Object((1,3,6,1,4,1,164,3,1,6,1,7,1,1,6),_EthIfSrcMacCtrlFlushAddrCmd_Type())
ethIfSrcMacCtrlFlushAddrCmd.setMaxAccess(_E)
if mibBuilder.loadTexts:ethIfSrcMacCtrlFlushAddrCmd.setStatus(_A)
_EthIfSrcMacCtrlAging_Type=Unsigned32
_EthIfSrcMacCtrlAging_Object=MibTableColumn
ethIfSrcMacCtrlAging=_EthIfSrcMacCtrlAging_Object((1,3,6,1,4,1,164,3,1,6,1,7,1,1,7),_EthIfSrcMacCtrlAging_Type())
ethIfSrcMacCtrlAging.setMaxAccess(_E)
if mibBuilder.loadTexts:ethIfSrcMacCtrlAging.setStatus(_A)
class _EthIfSrcMacCtrlLocking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('unlock',2),('lock',3)))
_EthIfSrcMacCtrlLocking_Type.__name__=_D
_EthIfSrcMacCtrlLocking_Object=MibTableColumn
ethIfSrcMacCtrlLocking=_EthIfSrcMacCtrlLocking_Object((1,3,6,1,4,1,164,3,1,6,1,7,1,1,8),_EthIfSrcMacCtrlLocking_Type())
ethIfSrcMacCtrlLocking.setMaxAccess(_E)
if mibBuilder.loadTexts:ethIfSrcMacCtrlLocking.setStatus(_A)
class _EthIfSrcMacCtrlViolationAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*(('drop',2),('dropNotify',3),('shutdown',4)))
_EthIfSrcMacCtrlViolationAction_Type.__name__=_D
_EthIfSrcMacCtrlViolationAction_Object=MibTableColumn
ethIfSrcMacCtrlViolationAction=_EthIfSrcMacCtrlViolationAction_Object((1,3,6,1,4,1,164,3,1,6,1,7,1,1,9),_EthIfSrcMacCtrlViolationAction_Type())
ethIfSrcMacCtrlViolationAction.setMaxAccess(_E)
if mibBuilder.loadTexts:ethIfSrcMacCtrlViolationAction.setStatus(_A)
_EthIfSrcMacCtrlLastViolatingAddr_Type=MacAddress
_EthIfSrcMacCtrlLastViolatingAddr_Object=MibTableColumn
ethIfSrcMacCtrlLastViolatingAddr=_EthIfSrcMacCtrlLastViolatingAddr_Object((1,3,6,1,4,1,164,3,1,6,1,7,1,1,10),_EthIfSrcMacCtrlLastViolatingAddr_Type())
ethIfSrcMacCtrlLastViolatingAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:ethIfSrcMacCtrlLastViolatingAddr.setStatus(_A)
class _EthIfSrcMacCtrlPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*(('shutdown',2),('secureActive',3),('secureInactive',4)))
_EthIfSrcMacCtrlPortStatus_Type.__name__=_D
_EthIfSrcMacCtrlPortStatus_Object=MibTableColumn
ethIfSrcMacCtrlPortStatus=_EthIfSrcMacCtrlPortStatus_Object((1,3,6,1,4,1,164,3,1,6,1,7,1,1,11),_EthIfSrcMacCtrlPortStatus_Type())
ethIfSrcMacCtrlPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfSrcMacCtrlPortStatus.setStatus(_A)
_EthIfSrcMacCtrlAddrTable_Object=MibTable
ethIfSrcMacCtrlAddrTable=_EthIfSrcMacCtrlAddrTable_Object((1,3,6,1,4,1,164,3,1,6,1,7,2))
if mibBuilder.loadTexts:ethIfSrcMacCtrlAddrTable.setStatus(_A)
_EthIfSrcMacCtrlAddrEntry_Object=MibTableRow
ethIfSrcMacCtrlAddrEntry=_EthIfSrcMacCtrlAddrEntry_Object((1,3,6,1,4,1,164,3,1,6,1,7,2,1))
ethIfSrcMacCtrlAddrEntry.setIndexNames((0,_G,_A4),(0,_G,_A5),(0,_G,_A6))
if mibBuilder.loadTexts:ethIfSrcMacCtrlAddrEntry.setStatus(_A)
_EthIfSrcMacCtrlAddrIndex_Type=Unsigned32
_EthIfSrcMacCtrlAddrIndex_Object=MibTableColumn
ethIfSrcMacCtrlAddrIndex=_EthIfSrcMacCtrlAddrIndex_Object((1,3,6,1,4,1,164,3,1,6,1,7,2,1,1),_EthIfSrcMacCtrlAddrIndex_Type())
ethIfSrcMacCtrlAddrIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ethIfSrcMacCtrlAddrIndex.setStatus(_A)
_EthIfSrcMacCtrlAddr_Type=MacAddress
_EthIfSrcMacCtrlAddr_Object=MibTableColumn
ethIfSrcMacCtrlAddr=_EthIfSrcMacCtrlAddr_Object((1,3,6,1,4,1,164,3,1,6,1,7,2,1,2),_EthIfSrcMacCtrlAddr_Type())
ethIfSrcMacCtrlAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:ethIfSrcMacCtrlAddr.setStatus(_A)
_EthIfSrcMacCtrlAddrIdx3_Type=Unsigned32
_EthIfSrcMacCtrlAddrIdx3_Object=MibTableColumn
ethIfSrcMacCtrlAddrIdx3=_EthIfSrcMacCtrlAddrIdx3_Object((1,3,6,1,4,1,164,3,1,6,1,7,2,1,3),_EthIfSrcMacCtrlAddrIdx3_Type())
ethIfSrcMacCtrlAddrIdx3.setMaxAccess(_I)
if mibBuilder.loadTexts:ethIfSrcMacCtrlAddrIdx3.setStatus(_A)
class _EthIfSrcMacCtrlAddrRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,6)));namedValues=NamedValues(*((_c,1),(_r,4),(_s,6)))
_EthIfSrcMacCtrlAddrRowStatus_Type.__name__=_D
_EthIfSrcMacCtrlAddrRowStatus_Object=MibTableColumn
ethIfSrcMacCtrlAddrRowStatus=_EthIfSrcMacCtrlAddrRowStatus_Object((1,3,6,1,4,1,164,3,1,6,1,7,2,1,4),_EthIfSrcMacCtrlAddrRowStatus_Type())
ethIfSrcMacCtrlAddrRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ethIfSrcMacCtrlAddrRowStatus.setStatus(_A)
class _EthIfSrcMacCtrlAddrStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,5)));namedValues=NamedValues(*(('invalid',2),('learned',3),('mgmt',5)))
_EthIfSrcMacCtrlAddrStatus_Type.__name__=_D
_EthIfSrcMacCtrlAddrStatus_Object=MibTableColumn
ethIfSrcMacCtrlAddrStatus=_EthIfSrcMacCtrlAddrStatus_Object((1,3,6,1,4,1,164,3,1,6,1,7,2,1,5),_EthIfSrcMacCtrlAddrStatus_Type())
ethIfSrcMacCtrlAddrStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfSrcMacCtrlAddrStatus.setStatus(_A)
_EthIfSysConfig_ObjectIdentity=ObjectIdentity
ethIfSysConfig=_EthIfSysConfig_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,1,11))
_EthIfSysValidEtherTypeTable_Object=MibTable
ethIfSysValidEtherTypeTable=_EthIfSysValidEtherTypeTable_Object((1,3,6,1,4,1,164,3,1,6,1,11,1))
if mibBuilder.loadTexts:ethIfSysValidEtherTypeTable.setStatus(_A)
_EthIfSysValidEtherTypeEntry_Object=MibTableRow
ethIfSysValidEtherTypeEntry=_EthIfSysValidEtherTypeEntry_Object((1,3,6,1,4,1,164,3,1,6,1,11,1,1))
ethIfSysValidEtherTypeEntry.setIndexNames((0,_G,_A7))
if mibBuilder.loadTexts:ethIfSysValidEtherTypeEntry.setStatus(_A)
_EthIfSysValidEtherTypeIdx_Type=Unsigned32
_EthIfSysValidEtherTypeIdx_Object=MibTableColumn
ethIfSysValidEtherTypeIdx=_EthIfSysValidEtherTypeIdx_Object((1,3,6,1,4,1,164,3,1,6,1,11,1,1,1),_EthIfSysValidEtherTypeIdx_Type())
ethIfSysValidEtherTypeIdx.setMaxAccess(_I)
if mibBuilder.loadTexts:ethIfSysValidEtherTypeIdx.setStatus(_A)
_EthIfSysValidEtherTypeRowStatus_Type=RowStatus
_EthIfSysValidEtherTypeRowStatus_Object=MibTableColumn
ethIfSysValidEtherTypeRowStatus=_EthIfSysValidEtherTypeRowStatus_Object((1,3,6,1,4,1,164,3,1,6,1,11,1,1,2),_EthIfSysValidEtherTypeRowStatus_Type())
ethIfSysValidEtherTypeRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ethIfSysValidEtherTypeRowStatus.setStatus(_A)
_EthIfSysValidEtherTypeCode_Type=Unsigned32
_EthIfSysValidEtherTypeCode_Object=MibTableColumn
ethIfSysValidEtherTypeCode=_EthIfSysValidEtherTypeCode_Object((1,3,6,1,4,1,164,3,1,6,1,11,1,1,3),_EthIfSysValidEtherTypeCode_Type())
ethIfSysValidEtherTypeCode.setMaxAccess(_F)
if mibBuilder.loadTexts:ethIfSysValidEtherTypeCode.setStatus(_A)
dot3OamEntry.registerAugmentions((_G,_A8))
dot3OamXEntry.setIndexNames(*dot3OamEntry.getIndexNames())
ethLos=NotificationType((1,3,6,1,4,1,164,3,1,6,1,0,1))
ethLos.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_J,_R)))
if mibBuilder.loadTexts:ethLos.setStatus(_A)
erpStateProtected=NotificationType((1,3,6,1,4,1,164,3,1,6,1,0,4))
erpStateProtected.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_G,'erpDescr')))
if mibBuilder.loadTexts:erpStateProtected.setStatus(_A)
erpPortStateChange=NotificationType((1,3,6,1,4,1,164,3,1,6,1,0,5))
erpPortStateChange.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_G,_A9),(_G,_AA)))
if mibBuilder.loadTexts:erpPortStateChange.setStatus(_A)
oamEfmRemoteLoopback=NotificationType((1,3,6,1,4,1,164,3,1,6,1,0,17))
oamEfmRemoteLoopback.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_J,_R),(_X,_g),(_X,_f)))
if mibBuilder.loadTexts:oamEfmRemoteLoopback.setStatus(_A)
oamEfmRemoteLoopbackOff=NotificationType((1,3,6,1,4,1,164,3,1,6,1,0,19))
oamEfmRemoteLoopbackOff.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_J,_R)))
if mibBuilder.loadTexts:oamEfmRemoteLoopbackOff.setStatus(_A)
oamEfmLinkFaultIndication=NotificationType((1,3,6,1,4,1,164,3,1,6,1,0,20))
oamEfmLinkFaultIndication.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_J,_R)))
if mibBuilder.loadTexts:oamEfmLinkFaultIndication.setStatus(_A)
oamEfmFeLinkFaultIndication=NotificationType((1,3,6,1,4,1,164,3,1,6,1,0,21))
oamEfmFeLinkFaultIndication.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_J,_R)))
if mibBuilder.loadTexts:oamEfmFeLinkFaultIndication.setStatus(_A)
oamEfmCriticalLinkIndication=NotificationType((1,3,6,1,4,1,164,3,1,6,1,0,22))
oamEfmCriticalLinkIndication.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_J,_R)))
if mibBuilder.loadTexts:oamEfmCriticalLinkIndication.setStatus(_A)
oamEfmFeCriticalLinkIndication=NotificationType((1,3,6,1,4,1,164,3,1,6,1,0,23))
oamEfmFeCriticalLinkIndication.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_J,_R)))
if mibBuilder.loadTexts:oamEfmFeCriticalLinkIndication.setStatus(_A)
oamEfmDyingGaspIndication=NotificationType((1,3,6,1,4,1,164,3,1,6,1,0,24))
oamEfmDyingGaspIndication.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_J,_R)))
if mibBuilder.loadTexts:oamEfmDyingGaspIndication.setStatus(_A)
oamEfmFeDyingGaspIndication=NotificationType((1,3,6,1,4,1,164,3,1,6,1,0,25))
oamEfmFeDyingGaspIndication.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_J,_R)))
if mibBuilder.loadTexts:oamEfmFeDyingGaspIndication.setStatus(_A)
pcsLinkDown=NotificationType((1,3,6,1,4,1,164,3,1,6,1,0,26))
pcsLinkDown.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_J,_R)))
if mibBuilder.loadTexts:pcsLinkDown.setStatus(_A)
ethIfRingStatusChange=NotificationType((1,3,6,1,4,1,164,3,1,6,1,4,0,1))
ethIfRingStatusChange.setObjects((_G,_AB))
if mibBuilder.loadTexts:ethIfRingStatusChange.setStatus(_A)
dot3OamOperStatusChange=NotificationType((1,3,6,1,4,1,164,3,1,6,1,6,0,1))
dot3OamOperStatusChange.setObjects((_X,_h))
if mibBuilder.loadTexts:dot3OamOperStatusChange.setStatus(_A)
dot3OamPeerEvent=NotificationType((1,3,6,1,4,1,164,3,1,6,1,6,0,2))
dot3OamPeerEvent.setObjects((_G,_AC))
if mibBuilder.loadTexts:dot3OamPeerEvent.setStatus(_A)
ethIfMacAccessViolation=NotificationType((1,3,6,1,4,1,164,3,1,6,1,7,0,1))
ethIfMacAccessViolation.setObjects(*((_J,_i),(_G,_AD)))
if mibBuilder.loadTexts:ethIfMacAccessViolation.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'ethIf':ethIf,'ethIfEvents':ethIfEvents,'ethLos':ethLos,'erpStateProtected':erpStateProtected,'erpPortStateChange':erpPortStateChange,'oamEfmRemoteLoopback':oamEfmRemoteLoopback,'oamEfmRemoteLoopbackOff':oamEfmRemoteLoopbackOff,'oamEfmLinkFaultIndication':oamEfmLinkFaultIndication,'oamEfmFeLinkFaultIndication':oamEfmFeLinkFaultIndication,'oamEfmCriticalLinkIndication':oamEfmCriticalLinkIndication,'oamEfmFeCriticalLinkIndication':oamEfmFeCriticalLinkIndication,'oamEfmDyingGaspIndication':oamEfmDyingGaspIndication,'oamEfmFeDyingGaspIndication':oamEfmFeDyingGaspIndication,'pcsLinkDown':pcsLinkDown,'ethIfTable':ethIfTable,'ethIfEntry':ethIfEntry,_b:ethIfIdx,'ethMode':ethMode,'ethBridgingMode':ethBridgingMode,'ethEncapsulationCRCMode':ethEncapsulationCRCMode,'ethBackPressure':ethBackPressure,'ethLimit4':ethLimit4,'ethSkipInitReset':ethSkipInitReset,'ethMulticastBlock':ethMulticastBlock,'ethBroadcastBlock':ethBroadcastBlock,'ethSpeed':ethSpeed,'ethRip2':ethRip2,'ethPortPriority':ethPortPriority,'ethPortMngEnable':ethPortMngEnable,'ethFlowCtrlMacAddress':ethFlowCtrlMacAddress,'ethRateLimit':ethRateLimit,'ethJumboFrameEnable':ethJumboFrameEnable,'ethAutoMdiXEnable':ethAutoMdiXEnable,'ethPortDataEnable':ethPortDataEnable,'ethIfUse':ethIfUse,'ethLineOam':ethLineOam,'ethRoutingProtocol':ethRoutingProtocol,'ethMdiXManualSwitch':ethMdiXManualSwitch,'ethDot1xEnable':ethDot1xEnable,'ethPartnerRateMode':ethPartnerRateMode,'ethDot1xPortRole':ethDot1xPortRole,'ethDhcpRequest':ethDhcpRequest,'ethSfpCapabilities':ethSfpCapabilities,'ethIfPerformance':ethIfPerformance,'ethIfCurrentTable':ethIfCurrentTable,'ethIfCurrentEntry':ethIfCurrentEntry,_n:ethIfCurrentIndex,'ethIfCurrentStatus':ethIfCurrentStatus,'ethIfCurrentInFrames':ethIfCurrentInFrames,'ethIfCurrentInOctets':ethIfCurrentInOctets,'ethIfCurrentAlignmentErrors':ethIfCurrentAlignmentErrors,'ethIfCurrentFCSErrors':ethIfCurrentFCSErrors,'ethIfCurrentLengthError':ethIfCurrentLengthError,'ethIfCurrentOutFrames':ethIfCurrentOutFrames,'ethIfCurrentOutOctets':ethIfCurrentOutOctets,'ethIfCurrentSingleCollisionFrames':ethIfCurrentSingleCollisionFrames,'ethIfCurrentMultipleCollisionFrames':ethIfCurrentMultipleCollisionFrames,'ethIfCurrentDeferredTransmissions':ethIfCurrentDeferredTransmissions,'ethIfCurrentLateCollisions':ethIfCurrentLateCollisions,'ethIfCurrentCarrierSenseErrors':ethIfCurrentCarrierSenseErrors,'ethIfCurrentInputCongestionDropped':ethIfCurrentInputCongestionDropped,'ethIfCurrentOutputCongestionDropped':ethIfCurrentOutputCongestionDropped,'ethIfCurrentOverflowInFrames':ethIfCurrentOverflowInFrames,'ethIfCurrentOverflowInOctets':ethIfCurrentOverflowInOctets,'ethIfCurrentOverflowFCSErrors':ethIfCurrentOverflowFCSErrors,'ethIfCurrentOverflowOutFrames':ethIfCurrentOverflowOutFrames,'ethIfCurrentOverflowOutOctets':ethIfCurrentOverflowOutOctets,'ethIfCurrentOverflowMultipleCollisionFrames':ethIfCurrentOverflowMultipleCollisionFrames,'ethIfCurrentInUnicastFrames':ethIfCurrentInUnicastFrames,'ethIfCurrentOutUnicastFrames':ethIfCurrentOutUnicastFrames,'ethIfCurrentInMulticastFrames':ethIfCurrentInMulticastFrames,'ethIfCurrentOutMulticastFrames':ethIfCurrentOutMulticastFrames,'ethIfCurrentInBroadcastFrames':ethIfCurrentInBroadcastFrames,'ethIfCurrentOutBroadcastFrames':ethIfCurrentOutBroadcastFrames,'ethIfCurrentInDiscardFrames':ethIfCurrentInDiscardFrames,'ethIfCurrentOutDiscardFrames':ethIfCurrentOutDiscardFrames,'ethIfCurrentInPauseFrames':ethIfCurrentInPauseFrames,'ethIfCurrentOutPauseFrames':ethIfCurrentOutPauseFrames,'ethIfCurrentOverflowInUnicastFrames':ethIfCurrentOverflowInUnicastFrames,'ethIfCurrentOverflowOutUnicastFrames':ethIfCurrentOverflowOutUnicastFrames,'ethIfCurrentOverflowInMulticastFrames':ethIfCurrentOverflowInMulticastFrames,'ethIfCurrentOverflowOutMulticastFrames':ethIfCurrentOverflowOutMulticastFrames,'ethIfCurrentOverflowInBroadcastFrames':ethIfCurrentOverflowInBroadcastFrames,'ethIfCurrentOverflowOutBroadcastFrames':ethIfCurrentOverflowOutBroadcastFrames,'ethIfCurrentOverflowInDiscardFrames':ethIfCurrentOverflowInDiscardFrames,'ethIfCurrentOverflowOutDiscardFrames':ethIfCurrentOverflowOutDiscardFrames,'ethIfCurrentOverflowInPauseFrames':ethIfCurrentOverflowInPauseFrames,'ethIfCurrentOverflowOutPauseFrames':ethIfCurrentOverflowOutPauseFrames,'ethIfIntervalTable':ethIfIntervalTable,'ethIfIntervalEntry':ethIfIntervalEntry,_o:ethIfIntervalIndex,_p:ethIfIntervalNumber,'ethIfIntervalStatus':ethIfIntervalStatus,'ethIfIntervalInFrames':ethIfIntervalInFrames,'ethIfIntervalInOctets':ethIfIntervalInOctets,'ethIfIntervalAlignmentErrors':ethIfIntervalAlignmentErrors,'ethIfIntervalFCSErrors':ethIfIntervalFCSErrors,'ethIfIntervalLengthError':ethIfIntervalLengthError,'ethIfIntervalOutFrames':ethIfIntervalOutFrames,'ethIfIntervalOutOctets':ethIfIntervalOutOctets,'ethIfIntervalSingleCollisionFrames':ethIfIntervalSingleCollisionFrames,'ethIfIntervalMultipleCollisionFrames':ethIfIntervalMultipleCollisionFrames,'ethIfIntervalDeferredTransmissions':ethIfIntervalDeferredTransmissions,'ethIfIntervalLateCollisions':ethIfIntervalLateCollisions,'ethIfIntervalCarrierSenseErrors':ethIfIntervalCarrierSenseErrors,'ethIfIntervalInputCongestionDropped':ethIfIntervalInputCongestionDropped,'ethIfIntervalOutputCongestionDropped':ethIfIntervalOutputCongestionDropped,'ethIfIntervalOverflowInFrames':ethIfIntervalOverflowInFrames,'ethIfIntervalOverflowInOctets':ethIfIntervalOverflowInOctets,'ethIfIntervalOverflowFCSErrors':ethIfIntervalOverflowFCSErrors,'ethIfIntervalOverflowOutFrames':ethIfIntervalOverflowOutFrames,'ethIfIntervalOverflowOutOctets':ethIfIntervalOverflowOutOctets,'ethIfIntervalOverflowMultipleCollisionFrames':ethIfIntervalOverflowMultipleCollisionFrames,'ethIfIntervalInUnicastFrames':ethIfIntervalInUnicastFrames,'ethIfIntervalOutUnicastFrames':ethIfIntervalOutUnicastFrames,'ethIfIntervalInMulticastFrames':ethIfIntervalInMulticastFrames,'ethIfIntervalOutMulticastFrames':ethIfIntervalOutMulticastFrames,'ethIfIntervalInBroadcastFrames':ethIfIntervalInBroadcastFrames,'ethIfIntervalOutBroadcastFrames':ethIfIntervalOutBroadcastFrames,'ethIfIntervalInDiscardFrames':ethIfIntervalInDiscardFrames,'ethIfIntervalOutDiscardFrames':ethIfIntervalOutDiscardFrames,'ethIfIntervalInPauseFrames':ethIfIntervalInPauseFrames,'ethIfIntervalOutPauseFrames':ethIfIntervalOutPauseFrames,'ethIfIntervalOverflowInUnicastFrames':ethIfIntervalOverflowInUnicastFrames,'ethIfIntervalOverflowOutUnicastFrames':ethIfIntervalOverflowOutUnicastFrames,'ethIfIntervalOverflowInMulticastFrames':ethIfIntervalOverflowInMulticastFrames,'ethIfIntervalOverflowOutMulticastFrames':ethIfIntervalOverflowOutMulticastFrames,'ethIfIntervalOverflowInBroadcastFrames':ethIfIntervalOverflowInBroadcastFrames,'ethIfIntervalOverflowOutBroadcastFrames':ethIfIntervalOverflowOutBroadcastFrames,'ethIfIntervalOverflowInDiscardFrames':ethIfIntervalOverflowInDiscardFrames,'ethIfIntervalOverflowOutDiscardFrames':ethIfIntervalOverflowOutDiscardFrames,'ethIfIntervalOverflowInPauseFrames':ethIfIntervalOverflowInPauseFrames,'ethIfIntervalOverflowOutPauseFrames':ethIfIntervalOverflowOutPauseFrames,'ethPerformanceMode':ethPerformanceMode,'ethIfPerfTable':ethIfPerfTable,'ethIfPerfEntry':ethIfPerfEntry,'ethIfPerfInOkFrames':ethIfPerfInOkFrames,'ethIfPerfOutOkFrames':ethIfPerfOutOkFrames,'ethIfPerfTotalCollisions':ethIfPerfTotalCollisions,'ethIfPerfInOkOctets':ethIfPerfInOkOctets,'ethIfStatsTable':ethIfStatsTable,'ethIfStatsEntry':ethIfStatsEntry,'ethIfStatsInOctets':ethIfStatsInOctets,'ethIfStatsInPkts':ethIfStatsInPkts,'ethIfStatsInUcastPkts':ethIfStatsInUcastPkts,'ethIfStatsInMulticastPkts':ethIfStatsInMulticastPkts,'ethIfStatsInBroadcastPkts':ethIfStatsInBroadcastPkts,'ethIfStatsInJabberPkts':ethIfStatsInJabberPkts,'ethIfStatsInL2CPDiscardPkts':ethIfStatsInL2CPDiscardPkts,'ethIfStatsInCFMDiscardPkts':ethIfStatsInCFMDiscardPkts,'ethIfStatsInACLDiscardPkts':ethIfStatsInACLDiscardPkts,'ethIfStatsInFCSErrorPkts':ethIfStatsInFCSErrorPkts,'ethIfStatsInMacOverflowPkts':ethIfStatsInMacOverflowPkts,'ethIfStatsInternalMacReceiveErrors':ethIfStatsInternalMacReceiveErrors,'ethIfStatsInUndersizePkts':ethIfStatsInUndersizePkts,'ethIfStatsInPkts64Octets':ethIfStatsInPkts64Octets,'ethIfStatsInPkts65to127Octets':ethIfStatsInPkts65to127Octets,'ethIfStatsInPkts128to255Octets':ethIfStatsInPkts128to255Octets,'ethIfStatsInPkts256to511Octets':ethIfStatsInPkts256to511Octets,'ethIfStatsInPkts512to1023Octets':ethIfStatsInPkts512to1023Octets,'ethIfStatsInPkts1024to1518Octets':ethIfStatsInPkts1024to1518Octets,'ethIfStatsInPkts1519to2047Octets':ethIfStatsInPkts1519to2047Octets,'ethIfStatsInPkts1519toMaxOctets':ethIfStatsInPkts1519toMaxOctets,'ethIfStatsInPkts2048toMaxOctets':ethIfStatsInPkts2048toMaxOctets,'ethIfStatsInOversizePkts':ethIfStatsInOversizePkts,'ethIfStatsInErrorPkts':ethIfStatsInErrorPkts,'ethIfStatsOutOctets':ethIfStatsOutOctets,'ethIfStatsOutPkts':ethIfStatsOutPkts,'ethIfStatsOutUcastPkts':ethIfStatsOutUcastPkts,'ethIfStatsOutMulticastPkts':ethIfStatsOutMulticastPkts,'ethIfStatsOutBroadcastPkts':ethIfStatsOutBroadcastPkts,'ethIfStatsOutDiscardPkts':ethIfStatsOutDiscardPkts,'ethIfStatsOutPkts64Octets':ethIfStatsOutPkts64Octets,'ethIfStatsOutPkts65to127Octets':ethIfStatsOutPkts65to127Octets,'ethIfStatsOutPkts128to255Octets':ethIfStatsOutPkts128to255Octets,'ethIfStatsOutPkts256to511Octets':ethIfStatsOutPkts256to511Octets,'ethIfStatsOutPkts512to1023Octets':ethIfStatsOutPkts512to1023Octets,'ethIfStatsOutPkts1024to1518Octets':ethIfStatsOutPkts1024to1518Octets,'ethIfStatsOutPkts1519to2047Octets':ethIfStatsOutPkts1519to2047Octets,'ethIfStatsOutPkts2048toMaxOctets':ethIfStatsOutPkts2048toMaxOctets,'ethIfStatsOutOversizePkts':ethIfStatsOutOversizePkts,'ethIfStatsInUnMappedCosFrames':ethIfStatsInUnMappedCosFrames,'ethIfStatsEgressMTUDiscarded':ethIfStatsEgressMTUDiscarded,'ethIfStatsLastEgressMTUDiscardingFlow':ethIfStatsLastEgressMTUDiscardingFlow,'ethIfRing':ethIfRing,'ethIfRingEvents':ethIfRingEvents,'ethIfRingStatusChange':ethIfRingStatusChange,'ethIfRingTable':ethIfRingTable,'ethIfRingEntry':ethIfRingEntry,_q:ethIfRingIdx,'ethIfRingAdminStatus':ethIfRingAdminStatus,'ethIfRingPorts':ethIfRingPorts,_AB:ethIfRingOperStatus,'ethIfRingKeepAliveInterval':ethIfRingKeepAliveInterval,'ethIfRingKeepAliveThresh':ethIfRingKeepAliveThresh,'ethIfRingKeepAliveVlanId':ethIfRingKeepAliveVlanId,'ethIfRingMultiCastVlanId':ethIfRingMultiCastVlanId,'ethIfRingRowStatus':ethIfRingRowStatus,'erp':erp,'erpTable':erpTable,'erpEntry':erpEntry,_Z:erpIdx,'erpRowStatus':erpRowStatus,'erpAdminStatus':erpAdminStatus,'erpNodeState':erpNodeState,'erpBridgeNum':erpBridgeNum,'erpEastPort':erpEastPort,'erpWestPort':erpWestPort,'erpRplPort':erpRplPort,'erpRapsVlanId':erpRapsVlanId,'erpOamCfmMel':erpOamCfmMel,'erpWTR':erpWTR,'erpWTRStatus':erpWTRStatus,'erpGuardTimer':erpGuardTimer,'erpHoldoffTimer':erpHoldoffTimer,'erpForceSfCmd':erpForceSfCmd,'erpClearStatistics':erpClearStatistics,'erpRapsVlanPriority':erpRapsVlanPriority,'erpDescr':erpDescr,'erpRingType':erpRingType,'erpWTBStatus':erpWTBStatus,'erpRevertiveMode':erpRevertiveMode,'erpBackwardCompatibility':erpBackwardCompatibility,'erpTopologyChangepropogation':erpTopologyChangepropogation,'erpInterconnectionNode':erpInterconnectionNode,'erpCommand':erpCommand,'erpCommandParam':erpCommandParam,'erpEastPhyPort':erpEastPhyPort,'erpWestPhyPort':erpWestPhyPort,'erpCosMapProfile':erpCosMapProfile,'erpVirtualChannel':erpVirtualChannel,'erpPassthroughVids':erpPassthroughVids,'erpColorMapProfile':erpColorMapProfile,'erpPassthroughQueueBlockEast':erpPassthroughQueueBlockEast,'erpPassthroughQueueBlockWest':erpPassthroughQueueBlockWest,'erpPortTable':erpPortTable,'erpPortEntry':erpPortEntry,_t:erpPortIdx,'erpPortOamCfmMdId':erpPortOamCfmMdId,'erpPortOamCfmMaId':erpPortOamCfmMaId,'erpPortOamCfmMepId':erpPortOamCfmMepId,_AA:erpPortState,'erpPortLocalSfSource':erpPortLocalSfSource,'erpPortRapsRxValidMsg':erpPortRapsRxValidMsg,'erpPortRapsRxInvalidMsg':erpPortRapsRxInvalidMsg,'erpPortRapsRxSfMsg':erpPortRapsRxSfMsg,'erpPortRapsRxNrMsg':erpPortRapsRxNrMsg,'erpPortRapsRxNrrbMsg':erpPortRapsRxNrrbMsg,'erpPortRapsTxValidMsg':erpPortRapsTxValidMsg,'erpPortRapsTxInvalidMsg':erpPortRapsTxInvalidMsg,'erpPortRapsTxSfMsg':erpPortRapsTxSfMsg,'erpPortRapsTxNrMsg':erpPortRapsTxNrMsg,'erpPortRapsTxNrrbMsg':erpPortRapsTxNrrbMsg,_A9:erpPortDescr,'erpPortRapsRxFsMsg':erpPortRapsRxFsMsg,'erpPortRapsRxMsMsg':erpPortRapsRxMsMsg,'erpPortRapsRxDnfMsg':erpPortRapsRxDnfMsg,'erpPortRapsRxEvtMsg':erpPortRapsRxEvtMsg,'erpPortRapsTxFsMsg':erpPortRapsTxFsMsg,'erpPortRapsTxMsMsg':erpPortRapsTxMsMsg,'erpPortRapsTxDnfMsg':erpPortRapsTxDnfMsg,'erpPortRapsTxEvtMsg':erpPortRapsTxEvtMsg,'erpPortType':erpPortType,'erpSubRingTable':erpSubRingTable,'erpSubRingEntry':erpSubRingEntry,_u:erpSubRingMajorRingIndex,_v:erpSubRingSubRingIndex,'erpSubRingRowStatus':erpSubRingRowStatus,'erpSubRingVirtualChannel':erpSubRingVirtualChannel,'erpSubRingRAPSVlanId':erpSubRingRAPSVlanId,'erpSubRingRAPSVlanPriority':erpSubRingRAPSVlanPriority,'erpVlanTable':erpVlanTable,'erpVlanEntry':erpVlanEntry,_w:erpVlanIdx,'erpVlanRowStatus':erpVlanRowStatus,'erpVlanEastQblock':erpVlanEastQblock,'erpVlanWestQblock':erpVlanWestQblock,'erpVlanServiceIdName':erpVlanServiceIdName,'erpVlanMajorEastQblock':erpVlanMajorEastQblock,'erpVlanMajorWestQblock':erpVlanMajorWestQblock,'ethIfStorming':ethIfStorming,'ethIfStormTable':ethIfStormTable,'ethIfStormEntry':ethIfStormEntry,_x:ethIfStormCnfgIdx,_y:ethIfStormIfIdx,_z:ethIfStormDirection,_A0:ethIfStormPacketType,'ethIfStormCtrlEnable':ethIfStormCtrlEnable,'ethIfStormMaxRate':ethIfStormMaxRate,'ethIfOamEfm':ethIfOamEfm,'dot3OamEvents':dot3OamEvents,'dot3OamOperStatusChange':dot3OamOperStatusChange,'dot3OamPeerEvent':dot3OamPeerEvent,'dot3OamDescrTable':dot3OamDescrTable,'dot3OamDescrEntry':dot3OamDescrEntry,_A1:dot3OamDescrId,'dot3OamDescrRowStatus':dot3OamDescrRowStatus,'dot3OamDescrMode':dot3OamDescrMode,'dot3OamDescrLbRxOperation':dot3OamDescrLbRxOperation,'dot3OamDescrRateLimit':dot3OamDescrRateLimit,'dot3OamXTable':dot3OamXTable,_A8:dot3OamXEntry,'dot3OamXDescrId':dot3OamXDescrId,_AC:dot3OamXPeerState,'ethIfMacLayer':ethIfMacLayer,'ethIfMacLayerEvents':ethIfMacLayerEvents,'ethIfMacAccessViolation':ethIfMacAccessViolation,'ethIfSrcMacCtrlTable':ethIfSrcMacCtrlTable,'ethIfSrcMacCtrlEntry':ethIfSrcMacCtrlEntry,_A2:ethIfSrcMacCtrlIndex,_A3:ethIfSrcMacCtrlIdx2,'ethIfSrcMacCtrl':ethIfSrcMacCtrl,'ethIfSrcMacCtrlMaxPermitAddr':ethIfSrcMacCtrlMaxPermitAddr,'ethIfSrcMacCtrlCurNumPermitAddr':ethIfSrcMacCtrlCurNumPermitAddr,'ethIfSrcMacCtrlFlushAddrCmd':ethIfSrcMacCtrlFlushAddrCmd,'ethIfSrcMacCtrlAging':ethIfSrcMacCtrlAging,'ethIfSrcMacCtrlLocking':ethIfSrcMacCtrlLocking,'ethIfSrcMacCtrlViolationAction':ethIfSrcMacCtrlViolationAction,_AD:ethIfSrcMacCtrlLastViolatingAddr,'ethIfSrcMacCtrlPortStatus':ethIfSrcMacCtrlPortStatus,'ethIfSrcMacCtrlAddrTable':ethIfSrcMacCtrlAddrTable,'ethIfSrcMacCtrlAddrEntry':ethIfSrcMacCtrlAddrEntry,_A4:ethIfSrcMacCtrlAddrIndex,_A5:ethIfSrcMacCtrlAddr,_A6:ethIfSrcMacCtrlAddrIdx3,'ethIfSrcMacCtrlAddrRowStatus':ethIfSrcMacCtrlAddrRowStatus,'ethIfSrcMacCtrlAddrStatus':ethIfSrcMacCtrlAddrStatus,'ethIfSysConfig':ethIfSysConfig,'ethIfSysValidEtherTypeTable':ethIfSysValidEtherTypeTable,'ethIfSysValidEtherTypeEntry':ethIfSysValidEtherTypeEntry,_A7:ethIfSysValidEtherTypeIdx,'ethIfSysValidEtherTypeRowStatus':ethIfSysValidEtherTypeRowStatus,'ethIfSysValidEtherTypeCode':ethIfSysValidEtherTypeCode})