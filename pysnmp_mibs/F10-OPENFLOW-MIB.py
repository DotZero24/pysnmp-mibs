_AR='ofSwitchMibNotificationsGroup'
_AQ='ofFlowActionGroup'
_AP='ofFlowMatchParamsGroup'
_AO='ofFlowGroup'
_AN='ofVlanGroup'
_AM='ofPortGroup'
_AL='ofControllerGroup'
_AK='ofInstanceGroup'
_AJ='ofSwitchScalarGroup'
_AI='ofSwitchFlowTableFull'
_AH='ofSwitchCntlrSessionStatusChanged'
_AG='ofSwitchFlowTableSrc'
_AF='ofFlowActionNWTos'
_AE='ofFlowActionVlanPcp'
_AD='ofFlowActionMaxLen'
_AC='ofFlowActionVlanId'
_AB='ofFlowActionPortIndex'
_AA='ofFlowActionDstMac'
_A9='ofFlowActionSrcMac'
_A8='ofFlowActionType'
_A7='ofFlowMatchTpDstPort'
_A6='ofFlowMatchTpSrcPort'
_A5='ofFlowMatchIpDestAddr'
_A4='ofFlowMatchIpSrcAddr'
_A3='ofFlowMatchIpProto'
_A2='ofFlowMatchIpTos'
_A1='ofFlowMatchVlanPri'
_A0='ofFlowMatchEthType'
_z='ofFlowMatchVlanId'
_y='ofFlowMatchEtherDstAddr'
_x='ofFlowMatchEtherSrcAddr'
_w='ofFlowMatchInPort'
_v='ofFlowByteCount'
_u='ofFlowPacketCount'
_t='ofFlowCookie'
_s='ofFlowUpTime'
_r='ofFlowHardTime'
_q='ofFlowIdleTime'
_p='ofFlowPriority'
_o='ofVlanId'
_n='ofPortAssociationType'
_m='ofCntlrProtocol'
_l='ofCntlrPortNumber'
_k='ofCntlrAddr'
_j='ofCntlrAddrType'
_i='ofInstSuppActions'
_h='ofInstSuppCapabilities'
_g='ofInstNumFlows'
_f='ofInstEchoReqInterval'
_e='ofInstEchoReplyTimeout'
_d='ofInstConnectTimeout'
_c='ofInstDataPathId'
_b='ofInstIntfType'
_a='ofInstAdminState'
_Z='ofSwitchVersion'
_Y='ofSwitchSerialNo'
_X='ofSoftwareDesc'
_W='ofHardwareDesc'
_V='ofManufacturerDesc'
_U='ofSwitchId'
_T='ofFlowMatchParamsEntry'
_S='ofFlowActionId'
_R='ofVlanIfIndex'
_Q='ofPortIfIndex'
_P='ofCntlrId'
_O='InetAddress'
_N='ofCntlrConState'
_M='ofFlowTblId'
_L='ofFlowId'
_K='Bits'
_J='seconds'
_I='DisplayString'
_H='not-accessible'
_G='ofInstId'
_F='Integer32'
_E='Unsigned32'
_D='OctetString'
_C='read-only'
_B='F10-OPENFLOW-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
f10Mgmt,=mibBuilder.importSymbols('FORCE10-SMI','f10Mgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_O,'InetAddressType','InetPortNumber')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_K,'Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'MacAddress','PhysAddress','TextualConvention','TimeStamp','TruthValue')
f10OpenFlow=ModuleIdentity((1,3,6,1,4,1,6027,3,20))
class DataPathIdentifier(TextualConvention,OctetString):status=_A;displayHint='1x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_OfSwitchObjects_ObjectIdentity=ObjectIdentity
ofSwitchObjects=_OfSwitchObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,20,1))
class _OfSwitchId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OfSwitchId_Type.__name__=_E
_OfSwitchId_Object=MibScalar
ofSwitchId=_OfSwitchId_Object((1,3,6,1,4,1,6027,3,20,1,1),_OfSwitchId_Type())
ofSwitchId.setMaxAccess(_C)
if mibBuilder.loadTexts:ofSwitchId.setStatus(_A)
class _OfManufacturerDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_OfManufacturerDesc_Type.__name__=_I
_OfManufacturerDesc_Object=MibScalar
ofManufacturerDesc=_OfManufacturerDesc_Object((1,3,6,1,4,1,6027,3,20,1,2),_OfManufacturerDesc_Type())
ofManufacturerDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:ofManufacturerDesc.setStatus(_A)
class _OfHardwareDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_OfHardwareDesc_Type.__name__=_I
_OfHardwareDesc_Object=MibScalar
ofHardwareDesc=_OfHardwareDesc_Object((1,3,6,1,4,1,6027,3,20,1,3),_OfHardwareDesc_Type())
ofHardwareDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:ofHardwareDesc.setStatus(_A)
class _OfSoftwareDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_OfSoftwareDesc_Type.__name__=_I
_OfSoftwareDesc_Object=MibScalar
ofSoftwareDesc=_OfSoftwareDesc_Object((1,3,6,1,4,1,6027,3,20,1,4),_OfSoftwareDesc_Type())
ofSoftwareDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:ofSoftwareDesc.setStatus(_A)
class _OfSwitchSerialNo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_OfSwitchSerialNo_Type.__name__=_D
_OfSwitchSerialNo_Object=MibScalar
ofSwitchSerialNo=_OfSwitchSerialNo_Object((1,3,6,1,4,1,6027,3,20,1,5),_OfSwitchSerialNo_Type())
ofSwitchSerialNo.setMaxAccess(_C)
if mibBuilder.loadTexts:ofSwitchSerialNo.setStatus(_A)
class _OfSwitchVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_OfSwitchVersion_Type.__name__=_D
_OfSwitchVersion_Object=MibScalar
ofSwitchVersion=_OfSwitchVersion_Object((1,3,6,1,4,1,6027,3,20,1,6),_OfSwitchVersion_Type())
ofSwitchVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:ofSwitchVersion.setStatus(_A)
_OfInstTable_Object=MibTable
ofInstTable=_OfInstTable_Object((1,3,6,1,4,1,6027,3,20,1,7))
if mibBuilder.loadTexts:ofInstTable.setStatus(_A)
_OfInstEntry_Object=MibTableRow
ofInstEntry=_OfInstEntry_Object((1,3,6,1,4,1,6027,3,20,1,7,1))
ofInstEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:ofInstEntry.setStatus(_A)
class _OfInstId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OfInstId_Type.__name__=_E
_OfInstId_Object=MibTableColumn
ofInstId=_OfInstId_Object((1,3,6,1,4,1,6027,3,20,1,7,1,1),_OfInstId_Type())
ofInstId.setMaxAccess(_H)
if mibBuilder.loadTexts:ofInstId.setStatus(_A)
class _OfInstAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_OfInstAdminState_Type.__name__=_F
_OfInstAdminState_Object=MibTableColumn
ofInstAdminState=_OfInstAdminState_Object((1,3,6,1,4,1,6027,3,20,1,7,1,2),_OfInstAdminState_Type())
ofInstAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:ofInstAdminState.setStatus(_A)
class _OfInstIntfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('port',1),('vlan',2),('any',3)))
_OfInstIntfType_Type.__name__=_F
_OfInstIntfType_Object=MibTableColumn
ofInstIntfType=_OfInstIntfType_Object((1,3,6,1,4,1,6027,3,20,1,7,1,3),_OfInstIntfType_Type())
ofInstIntfType.setMaxAccess(_C)
if mibBuilder.loadTexts:ofInstIntfType.setStatus(_A)
_OfInstDataPathId_Type=DataPathIdentifier
_OfInstDataPathId_Object=MibTableColumn
ofInstDataPathId=_OfInstDataPathId_Object((1,3,6,1,4,1,6027,3,20,1,7,1,4),_OfInstDataPathId_Type())
ofInstDataPathId.setMaxAccess(_C)
if mibBuilder.loadTexts:ofInstDataPathId.setStatus(_A)
class _OfInstConnectTimeout_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OfInstConnectTimeout_Type.__name__=_E
_OfInstConnectTimeout_Object=MibTableColumn
ofInstConnectTimeout=_OfInstConnectTimeout_Object((1,3,6,1,4,1,6027,3,20,1,7,1,5),_OfInstConnectTimeout_Type())
ofInstConnectTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:ofInstConnectTimeout.setStatus(_A)
if mibBuilder.loadTexts:ofInstConnectTimeout.setUnits(_J)
class _OfInstEchoReplyTimeout_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OfInstEchoReplyTimeout_Type.__name__=_E
_OfInstEchoReplyTimeout_Object=MibTableColumn
ofInstEchoReplyTimeout=_OfInstEchoReplyTimeout_Object((1,3,6,1,4,1,6027,3,20,1,7,1,6),_OfInstEchoReplyTimeout_Type())
ofInstEchoReplyTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:ofInstEchoReplyTimeout.setStatus(_A)
if mibBuilder.loadTexts:ofInstEchoReplyTimeout.setUnits(_J)
class _OfInstEchoReqInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OfInstEchoReqInterval_Type.__name__=_E
_OfInstEchoReqInterval_Object=MibTableColumn
ofInstEchoReqInterval=_OfInstEchoReqInterval_Object((1,3,6,1,4,1,6027,3,20,1,7,1,7),_OfInstEchoReqInterval_Type())
ofInstEchoReqInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:ofInstEchoReqInterval.setStatus(_A)
_OfInstNumFlows_Type=Unsigned32
_OfInstNumFlows_Object=MibTableColumn
ofInstNumFlows=_OfInstNumFlows_Object((1,3,6,1,4,1,6027,3,20,1,7,1,8),_OfInstNumFlows_Type())
ofInstNumFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:ofInstNumFlows.setStatus(_A)
class _OfInstSuppCapabilities_Type(Bits):namedValues=NamedValues(*(('port',0),('table',1),('flow',2)))
_OfInstSuppCapabilities_Type.__name__=_K
_OfInstSuppCapabilities_Object=MibTableColumn
ofInstSuppCapabilities=_OfInstSuppCapabilities_Object((1,3,6,1,4,1,6027,3,20,1,7,1,9),_OfInstSuppCapabilities_Type())
ofInstSuppCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:ofInstSuppCapabilities.setStatus(_A)
class _OfInstSuppActions_Type(Bits):namedValues=NamedValues(*(('output',0),('set-vlan',1),('set-pcp',2),('set-smac',3),('set-dmac',4),('set-tos',5)))
_OfInstSuppActions_Type.__name__=_K
_OfInstSuppActions_Object=MibTableColumn
ofInstSuppActions=_OfInstSuppActions_Object((1,3,6,1,4,1,6027,3,20,1,7,1,10),_OfInstSuppActions_Type())
ofInstSuppActions.setMaxAccess(_C)
if mibBuilder.loadTexts:ofInstSuppActions.setStatus(_A)
_OfCntlrTable_Object=MibTable
ofCntlrTable=_OfCntlrTable_Object((1,3,6,1,4,1,6027,3,20,1,8))
if mibBuilder.loadTexts:ofCntlrTable.setStatus(_A)
_OfCntlrEntry_Object=MibTableRow
ofCntlrEntry=_OfCntlrEntry_Object((1,3,6,1,4,1,6027,3,20,1,8,1))
ofCntlrEntry.setIndexNames((0,_B,_G),(0,_B,_P))
if mibBuilder.loadTexts:ofCntlrEntry.setStatus(_A)
class _OfCntlrId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OfCntlrId_Type.__name__=_E
_OfCntlrId_Object=MibTableColumn
ofCntlrId=_OfCntlrId_Object((1,3,6,1,4,1,6027,3,20,1,8,1,1),_OfCntlrId_Type())
ofCntlrId.setMaxAccess(_H)
if mibBuilder.loadTexts:ofCntlrId.setStatus(_A)
_OfCntlrAddrType_Type=InetAddressType
_OfCntlrAddrType_Object=MibTableColumn
ofCntlrAddrType=_OfCntlrAddrType_Object((1,3,6,1,4,1,6027,3,20,1,8,1,2),_OfCntlrAddrType_Type())
ofCntlrAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:ofCntlrAddrType.setStatus(_A)
class _OfCntlrAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(8,8),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_OfCntlrAddr_Type.__name__=_O
_OfCntlrAddr_Object=MibTableColumn
ofCntlrAddr=_OfCntlrAddr_Object((1,3,6,1,4,1,6027,3,20,1,8,1,3),_OfCntlrAddr_Type())
ofCntlrAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ofCntlrAddr.setStatus(_A)
_OfCntlrPortNumber_Type=InetPortNumber
_OfCntlrPortNumber_Object=MibTableColumn
ofCntlrPortNumber=_OfCntlrPortNumber_Object((1,3,6,1,4,1,6027,3,20,1,8,1,4),_OfCntlrPortNumber_Type())
ofCntlrPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ofCntlrPortNumber.setStatus(_A)
class _OfCntlrProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tls',1),('tcp',2)))
_OfCntlrProtocol_Type.__name__=_F
_OfCntlrProtocol_Object=MibTableColumn
ofCntlrProtocol=_OfCntlrProtocol_Object((1,3,6,1,4,1,6027,3,20,1,8,1,5),_OfCntlrProtocol_Type())
ofCntlrProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ofCntlrProtocol.setStatus(_A)
class _OfCntlrConState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('down',1),('up',2)))
_OfCntlrConState_Type.__name__=_F
_OfCntlrConState_Object=MibTableColumn
ofCntlrConState=_OfCntlrConState_Object((1,3,6,1,4,1,6027,3,20,1,8,1,6),_OfCntlrConState_Type())
ofCntlrConState.setMaxAccess(_C)
if mibBuilder.loadTexts:ofCntlrConState.setStatus(_A)
_OfPortTable_Object=MibTable
ofPortTable=_OfPortTable_Object((1,3,6,1,4,1,6027,3,20,1,9))
if mibBuilder.loadTexts:ofPortTable.setStatus(_A)
_OfPortEntry_Object=MibTableRow
ofPortEntry=_OfPortEntry_Object((1,3,6,1,4,1,6027,3,20,1,9,1))
ofPortEntry.setIndexNames((0,_B,_G),(0,_B,_Q))
if mibBuilder.loadTexts:ofPortEntry.setStatus(_A)
_OfPortIfIndex_Type=InterfaceIndex
_OfPortIfIndex_Object=MibTableColumn
ofPortIfIndex=_OfPortIfIndex_Object((1,3,6,1,4,1,6027,3,20,1,9,1,1),_OfPortIfIndex_Type())
ofPortIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ofPortIfIndex.setStatus(_A)
class _OfPortAssociationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('instancePort',1),('instVlanPort',2)))
_OfPortAssociationType_Type.__name__=_F
_OfPortAssociationType_Object=MibTableColumn
ofPortAssociationType=_OfPortAssociationType_Object((1,3,6,1,4,1,6027,3,20,1,9,1,2),_OfPortAssociationType_Type())
ofPortAssociationType.setMaxAccess(_C)
if mibBuilder.loadTexts:ofPortAssociationType.setStatus(_A)
_OfVlanTable_Object=MibTable
ofVlanTable=_OfVlanTable_Object((1,3,6,1,4,1,6027,3,20,1,10))
if mibBuilder.loadTexts:ofVlanTable.setStatus(_A)
_OfVlanEntry_Object=MibTableRow
ofVlanEntry=_OfVlanEntry_Object((1,3,6,1,4,1,6027,3,20,1,10,1))
ofVlanEntry.setIndexNames((0,_B,_G),(0,_B,_R))
if mibBuilder.loadTexts:ofVlanEntry.setStatus(_A)
_OfVlanIfIndex_Type=InterfaceIndex
_OfVlanIfIndex_Object=MibTableColumn
ofVlanIfIndex=_OfVlanIfIndex_Object((1,3,6,1,4,1,6027,3,20,1,10,1,1),_OfVlanIfIndex_Type())
ofVlanIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ofVlanIfIndex.setStatus(_A)
_OfVlanId_Type=VlanId
_OfVlanId_Object=MibTableColumn
ofVlanId=_OfVlanId_Object((1,3,6,1,4,1,6027,3,20,1,10,1,2),_OfVlanId_Type())
ofVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:ofVlanId.setStatus(_A)
_OfFlowTable_Object=MibTable
ofFlowTable=_OfFlowTable_Object((1,3,6,1,4,1,6027,3,20,1,11))
if mibBuilder.loadTexts:ofFlowTable.setStatus(_A)
_OfFlowEntry_Object=MibTableRow
ofFlowEntry=_OfFlowEntry_Object((1,3,6,1,4,1,6027,3,20,1,11,1))
ofFlowEntry.setIndexNames((0,_B,_G),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:ofFlowEntry.setStatus(_A)
_OfFlowId_Type=Unsigned32
_OfFlowId_Object=MibTableColumn
ofFlowId=_OfFlowId_Object((1,3,6,1,4,1,6027,3,20,1,11,1,1),_OfFlowId_Type())
ofFlowId.setMaxAccess(_H)
if mibBuilder.loadTexts:ofFlowId.setStatus(_A)
_OfFlowTblId_Type=Unsigned32
_OfFlowTblId_Object=MibTableColumn
ofFlowTblId=_OfFlowTblId_Object((1,3,6,1,4,1,6027,3,20,1,11,1,2),_OfFlowTblId_Type())
ofFlowTblId.setMaxAccess(_H)
if mibBuilder.loadTexts:ofFlowTblId.setStatus(_A)
class _OfFlowPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OfFlowPriority_Type.__name__=_E
_OfFlowPriority_Object=MibTableColumn
ofFlowPriority=_OfFlowPriority_Object((1,3,6,1,4,1,6027,3,20,1,11,1,3),_OfFlowPriority_Type())
ofFlowPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:ofFlowPriority.setStatus(_A)
class _OfFlowIdleTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OfFlowIdleTime_Type.__name__=_E
_OfFlowIdleTime_Object=MibTableColumn
ofFlowIdleTime=_OfFlowIdleTime_Object((1,3,6,1,4,1,6027,3,20,1,11,1,4),_OfFlowIdleTime_Type())
ofFlowIdleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ofFlowIdleTime.setStatus(_A)
if mibBuilder.loadTexts:ofFlowIdleTime.setUnits(_J)
class _OfFlowHardTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OfFlowHardTime_Type.__name__=_E
_OfFlowHardTime_Object=MibTableColumn
ofFlowHardTime=_OfFlowHardTime_Object((1,3,6,1,4,1,6027,3,20,1,11,1,5),_OfFlowHardTime_Type())
ofFlowHardTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ofFlowHardTime.setStatus(_A)
if mibBuilder.loadTexts:ofFlowHardTime.setUnits(_J)
_OfFlowUpTime_Type=TimeTicks
_OfFlowUpTime_Object=MibTableColumn
ofFlowUpTime=_OfFlowUpTime_Object((1,3,6,1,4,1,6027,3,20,1,11,1,6),_OfFlowUpTime_Type())
ofFlowUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ofFlowUpTime.setStatus(_A)
class _OfFlowCookie_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_OfFlowCookie_Type.__name__=_D
_OfFlowCookie_Object=MibTableColumn
ofFlowCookie=_OfFlowCookie_Object((1,3,6,1,4,1,6027,3,20,1,11,1,7),_OfFlowCookie_Type())
ofFlowCookie.setMaxAccess(_C)
if mibBuilder.loadTexts:ofFlowCookie.setStatus(_A)
_OfFlowPacketCount_Type=Counter64
_OfFlowPacketCount_Object=MibTableColumn
ofFlowPacketCount=_OfFlowPacketCount_Object((1,3,6,1,4,1,6027,3,20,1,11,1,8),_OfFlowPacketCount_Type())
ofFlowPacketCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ofFlowPacketCount.setStatus(_A)
_OfFlowByteCount_Type=Counter64
_OfFlowByteCount_Object=MibTableColumn
ofFlowByteCount=_OfFlowByteCount_Object((1,3,6,1,4,1,6027,3,20,1,11,1,9),_OfFlowByteCount_Type())
ofFlowByteCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ofFlowByteCount.setStatus(_A)
_OfFlowMatchParamsTable_Object=MibTable
ofFlowMatchParamsTable=_OfFlowMatchParamsTable_Object((1,3,6,1,4,1,6027,3,20,1,12))
if mibBuilder.loadTexts:ofFlowMatchParamsTable.setStatus(_A)
_OfFlowMatchParamsEntry_Object=MibTableRow
ofFlowMatchParamsEntry=_OfFlowMatchParamsEntry_Object((1,3,6,1,4,1,6027,3,20,1,12,1))
if mibBuilder.loadTexts:ofFlowMatchParamsEntry.setStatus(_A)
class _OfFlowMatchInPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_OfFlowMatchInPort_Type.__name__=_D
_OfFlowMatchInPort_Object=MibTableColumn
ofFlowMatchInPort=_OfFlowMatchInPort_Object((1,3,6,1,4,1,6027,3,20,1,12,1,1),_OfFlowMatchInPort_Type())
ofFlowMatchInPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ofFlowMatchInPort.setStatus(_A)
class _OfFlowMatchEtherSrcAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_OfFlowMatchEtherSrcAddr_Type.__name__=_D
_OfFlowMatchEtherSrcAddr_Object=MibTableColumn
ofFlowMatchEtherSrcAddr=_OfFlowMatchEtherSrcAddr_Object((1,3,6,1,4,1,6027,3,20,1,12,1,2),_OfFlowMatchEtherSrcAddr_Type())
ofFlowMatchEtherSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ofFlowMatchEtherSrcAddr.setStatus(_A)
class _OfFlowMatchEtherDstAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_OfFlowMatchEtherDstAddr_Type.__name__=_D
_OfFlowMatchEtherDstAddr_Object=MibTableColumn
ofFlowMatchEtherDstAddr=_OfFlowMatchEtherDstAddr_Object((1,3,6,1,4,1,6027,3,20,1,12,1,3),_OfFlowMatchEtherDstAddr_Type())
ofFlowMatchEtherDstAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ofFlowMatchEtherDstAddr.setStatus(_A)
class _OfFlowMatchVlanId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_OfFlowMatchVlanId_Type.__name__=_D
_OfFlowMatchVlanId_Object=MibTableColumn
ofFlowMatchVlanId=_OfFlowMatchVlanId_Object((1,3,6,1,4,1,6027,3,20,1,12,1,4),_OfFlowMatchVlanId_Type())
ofFlowMatchVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:ofFlowMatchVlanId.setStatus(_A)
class _OfFlowMatchEthType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_OfFlowMatchEthType_Type.__name__=_D
_OfFlowMatchEthType_Object=MibTableColumn
ofFlowMatchEthType=_OfFlowMatchEthType_Object((1,3,6,1,4,1,6027,3,20,1,12,1,5),_OfFlowMatchEthType_Type())
ofFlowMatchEthType.setMaxAccess(_C)
if mibBuilder.loadTexts:ofFlowMatchEthType.setStatus(_A)
class _OfFlowMatchVlanPri_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1))
_OfFlowMatchVlanPri_Type.__name__=_D
_OfFlowMatchVlanPri_Object=MibTableColumn
ofFlowMatchVlanPri=_OfFlowMatchVlanPri_Object((1,3,6,1,4,1,6027,3,20,1,12,1,6),_OfFlowMatchVlanPri_Type())
ofFlowMatchVlanPri.setMaxAccess(_C)
if mibBuilder.loadTexts:ofFlowMatchVlanPri.setStatus(_A)
class _OfFlowMatchIpTos_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1))
_OfFlowMatchIpTos_Type.__name__=_D
_OfFlowMatchIpTos_Object=MibTableColumn
ofFlowMatchIpTos=_OfFlowMatchIpTos_Object((1,3,6,1,4,1,6027,3,20,1,12,1,7),_OfFlowMatchIpTos_Type())
ofFlowMatchIpTos.setMaxAccess(_C)
if mibBuilder.loadTexts:ofFlowMatchIpTos.setStatus(_A)
class _OfFlowMatchIpProto_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1))
_OfFlowMatchIpProto_Type.__name__=_D
_OfFlowMatchIpProto_Object=MibTableColumn
ofFlowMatchIpProto=_OfFlowMatchIpProto_Object((1,3,6,1,4,1,6027,3,20,1,12,1,8),_OfFlowMatchIpProto_Type())
ofFlowMatchIpProto.setMaxAccess(_C)
if mibBuilder.loadTexts:ofFlowMatchIpProto.setStatus(_A)
class _OfFlowMatchIpSrcAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_OfFlowMatchIpSrcAddr_Type.__name__=_D
_OfFlowMatchIpSrcAddr_Object=MibTableColumn
ofFlowMatchIpSrcAddr=_OfFlowMatchIpSrcAddr_Object((1,3,6,1,4,1,6027,3,20,1,12,1,9),_OfFlowMatchIpSrcAddr_Type())
ofFlowMatchIpSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ofFlowMatchIpSrcAddr.setStatus(_A)
class _OfFlowMatchIpDestAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_OfFlowMatchIpDestAddr_Type.__name__=_D
_OfFlowMatchIpDestAddr_Object=MibTableColumn
ofFlowMatchIpDestAddr=_OfFlowMatchIpDestAddr_Object((1,3,6,1,4,1,6027,3,20,1,12,1,10),_OfFlowMatchIpDestAddr_Type())
ofFlowMatchIpDestAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ofFlowMatchIpDestAddr.setStatus(_A)
class _OfFlowMatchTpSrcPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_OfFlowMatchTpSrcPort_Type.__name__=_D
_OfFlowMatchTpSrcPort_Object=MibTableColumn
ofFlowMatchTpSrcPort=_OfFlowMatchTpSrcPort_Object((1,3,6,1,4,1,6027,3,20,1,12,1,11),_OfFlowMatchTpSrcPort_Type())
ofFlowMatchTpSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ofFlowMatchTpSrcPort.setStatus(_A)
class _OfFlowMatchTpDstPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_OfFlowMatchTpDstPort_Type.__name__=_D
_OfFlowMatchTpDstPort_Object=MibTableColumn
ofFlowMatchTpDstPort=_OfFlowMatchTpDstPort_Object((1,3,6,1,4,1,6027,3,20,1,12,1,12),_OfFlowMatchTpDstPort_Type())
ofFlowMatchTpDstPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ofFlowMatchTpDstPort.setStatus(_A)
_OfFlowActionTable_Object=MibTable
ofFlowActionTable=_OfFlowActionTable_Object((1,3,6,1,4,1,6027,3,20,1,13))
if mibBuilder.loadTexts:ofFlowActionTable.setStatus(_A)
_OfFlowActionEntry_Object=MibTableRow
ofFlowActionEntry=_OfFlowActionEntry_Object((1,3,6,1,4,1,6027,3,20,1,13,1))
ofFlowActionEntry.setIndexNames((0,_B,_G),(0,_B,_L),(0,_B,_M),(0,_B,_S))
if mibBuilder.loadTexts:ofFlowActionEntry.setStatus(_A)
_OfFlowActionId_Type=Unsigned32
_OfFlowActionId_Object=MibTableColumn
ofFlowActionId=_OfFlowActionId_Object((1,3,6,1,4,1,6027,3,20,1,13,1,1),_OfFlowActionId_Type())
ofFlowActionId.setMaxAccess(_H)
if mibBuilder.loadTexts:ofFlowActionId.setStatus(_A)
class _OfFlowActionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,65535)));namedValues=NamedValues(*(('outToSwitchPort',1),('setVlanVid',2),('setVlanPcp',3),('stripVlan',4),('setDlSrc',5),('setDlDst',6),('setNetworkSrc',7),('setNetworkDst',8),('setNetworkTos',9),('setTpSrc',10),('setTpDest',11),('outToQueue',12),('vendor',65535)))
_OfFlowActionType_Type.__name__=_F
_OfFlowActionType_Object=MibTableColumn
ofFlowActionType=_OfFlowActionType_Object((1,3,6,1,4,1,6027,3,20,1,13,1,2),_OfFlowActionType_Type())
ofFlowActionType.setMaxAccess(_C)
if mibBuilder.loadTexts:ofFlowActionType.setStatus(_A)
_OfFlowActionSrcMac_Type=MacAddress
_OfFlowActionSrcMac_Object=MibTableColumn
ofFlowActionSrcMac=_OfFlowActionSrcMac_Object((1,3,6,1,4,1,6027,3,20,1,13,1,3),_OfFlowActionSrcMac_Type())
ofFlowActionSrcMac.setMaxAccess(_C)
if mibBuilder.loadTexts:ofFlowActionSrcMac.setStatus(_A)
_OfFlowActionDstMac_Type=MacAddress
_OfFlowActionDstMac_Object=MibTableColumn
ofFlowActionDstMac=_OfFlowActionDstMac_Object((1,3,6,1,4,1,6027,3,20,1,13,1,4),_OfFlowActionDstMac_Type())
ofFlowActionDstMac.setMaxAccess(_C)
if mibBuilder.loadTexts:ofFlowActionDstMac.setStatus(_A)
_OfFlowActionPortIndex_Type=InterfaceIndex
_OfFlowActionPortIndex_Object=MibTableColumn
ofFlowActionPortIndex=_OfFlowActionPortIndex_Object((1,3,6,1,4,1,6027,3,20,1,13,1,5),_OfFlowActionPortIndex_Type())
ofFlowActionPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ofFlowActionPortIndex.setStatus(_A)
_OfFlowActionVlanId_Type=VlanId
_OfFlowActionVlanId_Object=MibTableColumn
ofFlowActionVlanId=_OfFlowActionVlanId_Object((1,3,6,1,4,1,6027,3,20,1,13,1,6),_OfFlowActionVlanId_Type())
ofFlowActionVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:ofFlowActionVlanId.setStatus(_A)
class _OfFlowActionMaxLen_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OfFlowActionMaxLen_Type.__name__=_E
_OfFlowActionMaxLen_Object=MibTableColumn
ofFlowActionMaxLen=_OfFlowActionMaxLen_Object((1,3,6,1,4,1,6027,3,20,1,13,1,7),_OfFlowActionMaxLen_Type())
ofFlowActionMaxLen.setMaxAccess(_C)
if mibBuilder.loadTexts:ofFlowActionMaxLen.setStatus(_A)
class _OfFlowActionVlanPcp_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OfFlowActionVlanPcp_Type.__name__=_E
_OfFlowActionVlanPcp_Object=MibTableColumn
ofFlowActionVlanPcp=_OfFlowActionVlanPcp_Object((1,3,6,1,4,1,6027,3,20,1,13,1,8),_OfFlowActionVlanPcp_Type())
ofFlowActionVlanPcp.setMaxAccess(_C)
if mibBuilder.loadTexts:ofFlowActionVlanPcp.setStatus(_A)
class _OfFlowActionNWTos_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OfFlowActionNWTos_Type.__name__=_E
_OfFlowActionNWTos_Object=MibTableColumn
ofFlowActionNWTos=_OfFlowActionNWTos_Object((1,3,6,1,4,1,6027,3,20,1,13,1,9),_OfFlowActionNWTos_Type())
ofFlowActionNWTos.setMaxAccess(_C)
if mibBuilder.loadTexts:ofFlowActionNWTos.setStatus(_A)
_OfSwitchMibConformance_ObjectIdentity=ObjectIdentity
ofSwitchMibConformance=_OfSwitchMibConformance_ObjectIdentity((1,3,6,1,4,1,6027,3,20,1,14))
_OfSwitchMibCompliances_ObjectIdentity=ObjectIdentity
ofSwitchMibCompliances=_OfSwitchMibCompliances_ObjectIdentity((1,3,6,1,4,1,6027,3,20,1,14,1))
_OfSwitchMibGroups_ObjectIdentity=ObjectIdentity
ofSwitchMibGroups=_OfSwitchMibGroups_ObjectIdentity((1,3,6,1,4,1,6027,3,20,1,14,2))
_OfSwitchNotification_ObjectIdentity=ObjectIdentity
ofSwitchNotification=_OfSwitchNotification_ObjectIdentity((1,3,6,1,4,1,6027,3,20,2))
_OfSwitchNotifications_ObjectIdentity=ObjectIdentity
ofSwitchNotifications=_OfSwitchNotifications_ObjectIdentity((1,3,6,1,4,1,6027,3,20,2,0))
_OfSwitchNotifyVariable_ObjectIdentity=ObjectIdentity
ofSwitchNotifyVariable=_OfSwitchNotifyVariable_ObjectIdentity((1,3,6,1,4,1,6027,3,20,2,1))
class _OfSwitchFlowTableSrc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ifp',1),('vlan',2),('dmac',3),('route',4),('lb',5)))
_OfSwitchFlowTableSrc_Type.__name__=_F
_OfSwitchFlowTableSrc_Object=MibScalar
ofSwitchFlowTableSrc=_OfSwitchFlowTableSrc_Object((1,3,6,1,4,1,6027,3,20,2,1,1),_OfSwitchFlowTableSrc_Type())
ofSwitchFlowTableSrc.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:ofSwitchFlowTableSrc.setStatus(_A)
ofFlowEntry.registerAugmentions((_B,_T))
ofFlowMatchParamsEntry.setIndexNames(*ofFlowEntry.getIndexNames())
ofSwitchScalarGroup=ObjectGroup((1,3,6,1,4,1,6027,3,20,1,14,2,1))
ofSwitchScalarGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:ofSwitchScalarGroup.setStatus(_A)
ofInstanceGroup=ObjectGroup((1,3,6,1,4,1,6027,3,20,1,14,2,2))
ofInstanceGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:ofInstanceGroup.setStatus(_A)
ofControllerGroup=ObjectGroup((1,3,6,1,4,1,6027,3,20,1,14,2,3))
ofControllerGroup.setObjects(*((_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_N)))
if mibBuilder.loadTexts:ofControllerGroup.setStatus(_A)
ofPortGroup=ObjectGroup((1,3,6,1,4,1,6027,3,20,1,14,2,4))
ofPortGroup.setObjects((_B,_n))
if mibBuilder.loadTexts:ofPortGroup.setStatus(_A)
ofVlanGroup=ObjectGroup((1,3,6,1,4,1,6027,3,20,1,14,2,5))
ofVlanGroup.setObjects((_B,_o))
if mibBuilder.loadTexts:ofVlanGroup.setStatus(_A)
ofFlowGroup=ObjectGroup((1,3,6,1,4,1,6027,3,20,1,14,2,6))
ofFlowGroup.setObjects(*((_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:ofFlowGroup.setStatus(_A)
ofFlowMatchParamsGroup=ObjectGroup((1,3,6,1,4,1,6027,3,20,1,14,2,7))
ofFlowMatchParamsGroup.setObjects(*((_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:ofFlowMatchParamsGroup.setStatus(_A)
ofFlowActionGroup=ObjectGroup((1,3,6,1,4,1,6027,3,20,1,14,2,8))
ofFlowActionGroup.setObjects(*((_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF)))
if mibBuilder.loadTexts:ofFlowActionGroup.setStatus(_A)
ofSwitchCntlrSessionStatusChanged=NotificationType((1,3,6,1,4,1,6027,3,20,2,0,1))
ofSwitchCntlrSessionStatusChanged.setObjects((_B,_N))
if mibBuilder.loadTexts:ofSwitchCntlrSessionStatusChanged.setStatus(_A)
ofSwitchFlowTableFull=NotificationType((1,3,6,1,4,1,6027,3,20,2,0,2))
ofSwitchFlowTableFull.setObjects((_B,_AG))
if mibBuilder.loadTexts:ofSwitchFlowTableFull.setStatus(_A)
ofSwitchMibNotificationsGroup=NotificationGroup((1,3,6,1,4,1,6027,3,20,1,14,2,9))
ofSwitchMibNotificationsGroup.setObjects(*((_B,_AH),(_B,_AI)))
if mibBuilder.loadTexts:ofSwitchMibNotificationsGroup.setStatus(_A)
ofSwitchMibCompliance=ModuleCompliance((1,3,6,1,4,1,6027,3,20,1,14,1,1))
ofSwitchMibCompliance.setObjects(*((_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR)))
if mibBuilder.loadTexts:ofSwitchMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'DataPathIdentifier':DataPathIdentifier,'f10OpenFlow':f10OpenFlow,'ofSwitchObjects':ofSwitchObjects,_U:ofSwitchId,_V:ofManufacturerDesc,_W:ofHardwareDesc,_X:ofSoftwareDesc,_Y:ofSwitchSerialNo,_Z:ofSwitchVersion,'ofInstTable':ofInstTable,'ofInstEntry':ofInstEntry,_G:ofInstId,_a:ofInstAdminState,_b:ofInstIntfType,_c:ofInstDataPathId,_d:ofInstConnectTimeout,_e:ofInstEchoReplyTimeout,_f:ofInstEchoReqInterval,_g:ofInstNumFlows,_h:ofInstSuppCapabilities,_i:ofInstSuppActions,'ofCntlrTable':ofCntlrTable,'ofCntlrEntry':ofCntlrEntry,_P:ofCntlrId,_j:ofCntlrAddrType,_k:ofCntlrAddr,_l:ofCntlrPortNumber,_m:ofCntlrProtocol,_N:ofCntlrConState,'ofPortTable':ofPortTable,'ofPortEntry':ofPortEntry,_Q:ofPortIfIndex,_n:ofPortAssociationType,'ofVlanTable':ofVlanTable,'ofVlanEntry':ofVlanEntry,_R:ofVlanIfIndex,_o:ofVlanId,'ofFlowTable':ofFlowTable,'ofFlowEntry':ofFlowEntry,_L:ofFlowId,_M:ofFlowTblId,_p:ofFlowPriority,_q:ofFlowIdleTime,_r:ofFlowHardTime,_s:ofFlowUpTime,_t:ofFlowCookie,_u:ofFlowPacketCount,_v:ofFlowByteCount,'ofFlowMatchParamsTable':ofFlowMatchParamsTable,_T:ofFlowMatchParamsEntry,_w:ofFlowMatchInPort,_x:ofFlowMatchEtherSrcAddr,_y:ofFlowMatchEtherDstAddr,_z:ofFlowMatchVlanId,_A0:ofFlowMatchEthType,_A1:ofFlowMatchVlanPri,_A2:ofFlowMatchIpTos,_A3:ofFlowMatchIpProto,_A4:ofFlowMatchIpSrcAddr,_A5:ofFlowMatchIpDestAddr,_A6:ofFlowMatchTpSrcPort,_A7:ofFlowMatchTpDstPort,'ofFlowActionTable':ofFlowActionTable,'ofFlowActionEntry':ofFlowActionEntry,_S:ofFlowActionId,_A8:ofFlowActionType,_A9:ofFlowActionSrcMac,_AA:ofFlowActionDstMac,_AB:ofFlowActionPortIndex,_AC:ofFlowActionVlanId,_AD:ofFlowActionMaxLen,_AE:ofFlowActionVlanPcp,_AF:ofFlowActionNWTos,'ofSwitchMibConformance':ofSwitchMibConformance,'ofSwitchMibCompliances':ofSwitchMibCompliances,'ofSwitchMibCompliance':ofSwitchMibCompliance,'ofSwitchMibGroups':ofSwitchMibGroups,_AJ:ofSwitchScalarGroup,_AK:ofInstanceGroup,_AL:ofControllerGroup,_AM:ofPortGroup,_AN:ofVlanGroup,_AO:ofFlowGroup,_AP:ofFlowMatchParamsGroup,_AQ:ofFlowActionGroup,_AR:ofSwitchMibNotificationsGroup,'ofSwitchNotification':ofSwitchNotification,'ofSwitchNotifications':ofSwitchNotifications,_AH:ofSwitchCntlrSessionStatusChanged,_AI:ofSwitchFlowTableFull,'ofSwitchNotifyVariable':ofSwitchNotifyVariable,_AG:ofSwitchFlowTableSrc})