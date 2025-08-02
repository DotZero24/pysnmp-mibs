_R='fsDhcp6RlyTrapInvalidMsgType'
_Q='accessible-for-notify'
_P='fsDhcp6RlyOutIfIndex'
_O='fsDhcp6RlyIfIndex'
_N='fsDhcp6RlyTrapIfIndex'
_M='fsDhcp6RlySrvAddress'
_L='fsDhcp6RlyInIfIndex'
_K='read-create'
_J='disabled'
_I='enabled'
_H='OctetString'
_G='not-accessible'
_F='DisplayString'
_E='read-only'
_D='ARICENT-DHCPv6-RELAY-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention','TruthValue')
fsdhcpv6rly=ModuleIdentity((1,3,6,1,4,1,29601,2,41))
if mibBuilder.loadTexts:fsdhcpv6rly.setRevisions(('2012-09-05 00:00',))
_FsDhcp6RlyNotify_ObjectIdentity=ObjectIdentity
fsDhcp6RlyNotify=_FsDhcp6RlyNotify_ObjectIdentity((1,3,6,1,4,1,29601,2,41,0))
_FsDhcp6RlySystem_ObjectIdentity=ObjectIdentity
fsDhcp6RlySystem=_FsDhcp6RlySystem_ObjectIdentity((1,3,6,1,4,1,29601,2,41,1))
class _FsDhcp6RlyDebugTrace_Type(DisplayString):defaultValue=OctetString('critical');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_FsDhcp6RlyDebugTrace_Type.__name__=_F
_FsDhcp6RlyDebugTrace_Object=MibScalar
fsDhcp6RlyDebugTrace=_FsDhcp6RlyDebugTrace_Object((1,3,6,1,4,1,29601,2,41,1,1),_FsDhcp6RlyDebugTrace_Type())
fsDhcp6RlyDebugTrace.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6RlyDebugTrace.setStatus(_A)
class _FsDhcp6RlyTrapAdminControl_Type(Bits):namedValues=NamedValues(*(('none',0),('trapInvalidPacketIn',1),('trapMaxHopCount',2)))
_FsDhcp6RlyTrapAdminControl_Type.__name__='Bits'
_FsDhcp6RlyTrapAdminControl_Object=MibScalar
fsDhcp6RlyTrapAdminControl=_FsDhcp6RlyTrapAdminControl_Object((1,3,6,1,4,1,29601,2,41,1,2),_FsDhcp6RlyTrapAdminControl_Type())
fsDhcp6RlyTrapAdminControl.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6RlyTrapAdminControl.setStatus(_A)
class _FsDhcp6RlySysLogAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsDhcp6RlySysLogAdminStatus_Type.__name__=_C
_FsDhcp6RlySysLogAdminStatus_Object=MibScalar
fsDhcp6RlySysLogAdminStatus=_FsDhcp6RlySysLogAdminStatus_Object((1,3,6,1,4,1,29601,2,41,1,3),_FsDhcp6RlySysLogAdminStatus_Type())
fsDhcp6RlySysLogAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6RlySysLogAdminStatus.setStatus(_A)
class _FsDhcp6RlyListenPort_Type(Integer32):defaultValue=547;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsDhcp6RlyListenPort_Type.__name__=_C
_FsDhcp6RlyListenPort_Object=MibScalar
fsDhcp6RlyListenPort=_FsDhcp6RlyListenPort_Object((1,3,6,1,4,1,29601,2,41,1,4),_FsDhcp6RlyListenPort_Type())
fsDhcp6RlyListenPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6RlyListenPort.setStatus(_A)
class _FsDhcp6RlyClientTransmitPort_Type(Integer32):defaultValue=546;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsDhcp6RlyClientTransmitPort_Type.__name__=_C
_FsDhcp6RlyClientTransmitPort_Object=MibScalar
fsDhcp6RlyClientTransmitPort=_FsDhcp6RlyClientTransmitPort_Object((1,3,6,1,4,1,29601,2,41,1,5),_FsDhcp6RlyClientTransmitPort_Type())
fsDhcp6RlyClientTransmitPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6RlyClientTransmitPort.setStatus(_A)
class _FsDhcp6RlyServerTransmitPort_Type(Integer32):defaultValue=547;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsDhcp6RlyServerTransmitPort_Type.__name__=_C
_FsDhcp6RlyServerTransmitPort_Object=MibScalar
fsDhcp6RlyServerTransmitPort=_FsDhcp6RlyServerTransmitPort_Object((1,3,6,1,4,1,29601,2,41,1,6),_FsDhcp6RlyServerTransmitPort_Type())
fsDhcp6RlyServerTransmitPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6RlyServerTransmitPort.setStatus(_A)
class _FsDhcp6RlyOption37Control_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsDhcp6RlyOption37Control_Type.__name__=_C
_FsDhcp6RlyOption37Control_Object=MibScalar
fsDhcp6RlyOption37Control=_FsDhcp6RlyOption37Control_Object((1,3,6,1,4,1,29601,2,41,1,7),_FsDhcp6RlyOption37Control_Type())
fsDhcp6RlyOption37Control.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6RlyOption37Control.setStatus(_A)
class _FsDhcp6RlyPDRouteControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsDhcp6RlyPDRouteControl_Type.__name__=_C
_FsDhcp6RlyPDRouteControl_Object=MibScalar
fsDhcp6RlyPDRouteControl=_FsDhcp6RlyPDRouteControl_Object((1,3,6,1,4,1,29601,2,41,1,8),_FsDhcp6RlyPDRouteControl_Type())
fsDhcp6RlyPDRouteControl.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6RlyPDRouteControl.setStatus(_A)
_FsDhcp6RlyConfig_ObjectIdentity=ObjectIdentity
fsDhcp6RlyConfig=_FsDhcp6RlyConfig_ObjectIdentity((1,3,6,1,4,1,29601,2,41,2))
_FsDhcp6RlyIfTable_Object=MibTable
fsDhcp6RlyIfTable=_FsDhcp6RlyIfTable_Object((1,3,6,1,4,1,29601,2,41,2,1))
if mibBuilder.loadTexts:fsDhcp6RlyIfTable.setStatus(_A)
_FsDhcp6RlyIfEntry_Object=MibTableRow
fsDhcp6RlyIfEntry=_FsDhcp6RlyIfEntry_Object((1,3,6,1,4,1,29601,2,41,2,1,1))
fsDhcp6RlyIfEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:fsDhcp6RlyIfEntry.setStatus(_A)
class _FsDhcp6RlyIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsDhcp6RlyIfIndex_Type.__name__=_C
_FsDhcp6RlyIfIndex_Object=MibTableColumn
fsDhcp6RlyIfIndex=_FsDhcp6RlyIfIndex_Object((1,3,6,1,4,1,29601,2,41,2,1,1,1),_FsDhcp6RlyIfIndex_Type())
fsDhcp6RlyIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fsDhcp6RlyIfIndex.setStatus(_A)
class _FsDhcp6RlyIfHopThreshold_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_FsDhcp6RlyIfHopThreshold_Type.__name__=_C
_FsDhcp6RlyIfHopThreshold_Object=MibTableColumn
fsDhcp6RlyIfHopThreshold=_FsDhcp6RlyIfHopThreshold_Object((1,3,6,1,4,1,29601,2,41,2,1,1,3),_FsDhcp6RlyIfHopThreshold_Type())
fsDhcp6RlyIfHopThreshold.setMaxAccess(_K)
if mibBuilder.loadTexts:fsDhcp6RlyIfHopThreshold.setStatus(_A)
_FsDhcp6RlyIfInformIn_Type=Counter32
_FsDhcp6RlyIfInformIn_Object=MibTableColumn
fsDhcp6RlyIfInformIn=_FsDhcp6RlyIfInformIn_Object((1,3,6,1,4,1,29601,2,41,2,1,1,4),_FsDhcp6RlyIfInformIn_Type())
fsDhcp6RlyIfInformIn.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDhcp6RlyIfInformIn.setStatus(_A)
_FsDhcp6RlyIfRelayForwIn_Type=Counter32
_FsDhcp6RlyIfRelayForwIn_Object=MibTableColumn
fsDhcp6RlyIfRelayForwIn=_FsDhcp6RlyIfRelayForwIn_Object((1,3,6,1,4,1,29601,2,41,2,1,1,5),_FsDhcp6RlyIfRelayForwIn_Type())
fsDhcp6RlyIfRelayForwIn.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDhcp6RlyIfRelayForwIn.setStatus(_A)
_FsDhcp6RlyIfRelayReplyIn_Type=Counter32
_FsDhcp6RlyIfRelayReplyIn_Object=MibTableColumn
fsDhcp6RlyIfRelayReplyIn=_FsDhcp6RlyIfRelayReplyIn_Object((1,3,6,1,4,1,29601,2,41,2,1,1,6),_FsDhcp6RlyIfRelayReplyIn_Type())
fsDhcp6RlyIfRelayReplyIn.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDhcp6RlyIfRelayReplyIn.setStatus(_A)
_FsDhcp6RlyIfInvalidPktIn_Type=Counter32
_FsDhcp6RlyIfInvalidPktIn_Object=MibTableColumn
fsDhcp6RlyIfInvalidPktIn=_FsDhcp6RlyIfInvalidPktIn_Object((1,3,6,1,4,1,29601,2,41,2,1,1,10),_FsDhcp6RlyIfInvalidPktIn_Type())
fsDhcp6RlyIfInvalidPktIn.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDhcp6RlyIfInvalidPktIn.setStatus(_A)
_FsDhcp6RlyIfCounterRest_Type=TruthValue
_FsDhcp6RlyIfCounterRest_Object=MibTableColumn
fsDhcp6RlyIfCounterRest=_FsDhcp6RlyIfCounterRest_Object((1,3,6,1,4,1,29601,2,41,2,1,1,11),_FsDhcp6RlyIfCounterRest_Type())
fsDhcp6RlyIfCounterRest.setMaxAccess(_K)
if mibBuilder.loadTexts:fsDhcp6RlyIfCounterRest.setStatus(_A)
_FsDhcp6RlyIfRowStatus_Type=RowStatus
_FsDhcp6RlyIfRowStatus_Object=MibTableColumn
fsDhcp6RlyIfRowStatus=_FsDhcp6RlyIfRowStatus_Object((1,3,6,1,4,1,29601,2,41,2,1,1,12),_FsDhcp6RlyIfRowStatus_Type())
fsDhcp6RlyIfRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:fsDhcp6RlyIfRowStatus.setStatus(_A)
class _FsDhcp6RlyIfRemoteIdOption_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('duid',1),('switchName',2),('mgmtIp',3),('userDefined',4)))
_FsDhcp6RlyIfRemoteIdOption_Type.__name__=_C
_FsDhcp6RlyIfRemoteIdOption_Object=MibTableColumn
fsDhcp6RlyIfRemoteIdOption=_FsDhcp6RlyIfRemoteIdOption_Object((1,3,6,1,4,1,29601,2,41,2,1,1,13),_FsDhcp6RlyIfRemoteIdOption_Type())
fsDhcp6RlyIfRemoteIdOption.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6RlyIfRemoteIdOption.setStatus(_A)
class _FsDhcp6RlyIfRemoteIdDUID_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FsDhcp6RlyIfRemoteIdDUID_Type.__name__=_H
_FsDhcp6RlyIfRemoteIdDUID_Object=MibTableColumn
fsDhcp6RlyIfRemoteIdDUID=_FsDhcp6RlyIfRemoteIdDUID_Object((1,3,6,1,4,1,29601,2,41,2,1,1,14),_FsDhcp6RlyIfRemoteIdDUID_Type())
fsDhcp6RlyIfRemoteIdDUID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6RlyIfRemoteIdDUID.setStatus(_A)
class _FsDhcp6RlyIfRemoteIdOptionValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_FsDhcp6RlyIfRemoteIdOptionValue_Type.__name__=_F
_FsDhcp6RlyIfRemoteIdOptionValue_Object=MibTableColumn
fsDhcp6RlyIfRemoteIdOptionValue=_FsDhcp6RlyIfRemoteIdOptionValue_Object((1,3,6,1,4,1,29601,2,41,2,1,1,15),_FsDhcp6RlyIfRemoteIdOptionValue_Type())
fsDhcp6RlyIfRemoteIdOptionValue.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDhcp6RlyIfRemoteIdOptionValue.setStatus(_A)
class _FsDhcp6RlyIfRemoteIdUserDefined_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FsDhcp6RlyIfRemoteIdUserDefined_Type.__name__=_F
_FsDhcp6RlyIfRemoteIdUserDefined_Object=MibTableColumn
fsDhcp6RlyIfRemoteIdUserDefined=_FsDhcp6RlyIfRemoteIdUserDefined_Object((1,3,6,1,4,1,29601,2,41,2,1,1,16),_FsDhcp6RlyIfRemoteIdUserDefined_Type())
fsDhcp6RlyIfRemoteIdUserDefined.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6RlyIfRemoteIdUserDefined.setStatus(_A)
_FsDhcp6RlyIfRelayForwOut_Type=Counter32
_FsDhcp6RlyIfRelayForwOut_Object=MibTableColumn
fsDhcp6RlyIfRelayForwOut=_FsDhcp6RlyIfRelayForwOut_Object((1,3,6,1,4,1,29601,2,41,2,1,1,17),_FsDhcp6RlyIfRelayForwOut_Type())
fsDhcp6RlyIfRelayForwOut.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDhcp6RlyIfRelayForwOut.setStatus(_A)
_FsDhcp6RlyIfRelayReplyOut_Type=Counter32
_FsDhcp6RlyIfRelayReplyOut_Object=MibTableColumn
fsDhcp6RlyIfRelayReplyOut=_FsDhcp6RlyIfRelayReplyOut_Object((1,3,6,1,4,1,29601,2,41,2,1,1,18),_FsDhcp6RlyIfRelayReplyOut_Type())
fsDhcp6RlyIfRelayReplyOut.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDhcp6RlyIfRelayReplyOut.setStatus(_A)
class _FsDhcp6RlyIfRelayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dynamic',1),('static',2),('both',3)))
_FsDhcp6RlyIfRelayState_Type.__name__=_C
_FsDhcp6RlyIfRelayState_Object=MibTableColumn
fsDhcp6RlyIfRelayState=_FsDhcp6RlyIfRelayState_Object((1,3,6,1,4,1,29601,2,41,2,1,1,19),_FsDhcp6RlyIfRelayState_Type())
fsDhcp6RlyIfRelayState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6RlyIfRelayState.setStatus(_A)
_FsDhcp6RlySrvAddressTable_Object=MibTable
fsDhcp6RlySrvAddressTable=_FsDhcp6RlySrvAddressTable_Object((1,3,6,1,4,1,29601,2,41,2,2))
if mibBuilder.loadTexts:fsDhcp6RlySrvAddressTable.setStatus(_A)
_FsDhcp6RlySrvAddressEntry_Object=MibTableRow
fsDhcp6RlySrvAddressEntry=_FsDhcp6RlySrvAddressEntry_Object((1,3,6,1,4,1,29601,2,41,2,2,1))
fsDhcp6RlySrvAddressEntry.setIndexNames((0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:fsDhcp6RlySrvAddressEntry.setStatus(_A)
class _FsDhcp6RlyInIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsDhcp6RlyInIfIndex_Type.__name__=_C
_FsDhcp6RlyInIfIndex_Object=MibTableColumn
fsDhcp6RlyInIfIndex=_FsDhcp6RlyInIfIndex_Object((1,3,6,1,4,1,29601,2,41,2,2,1,1),_FsDhcp6RlyInIfIndex_Type())
fsDhcp6RlyInIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fsDhcp6RlyInIfIndex.setStatus(_A)
class _FsDhcp6RlySrvAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsDhcp6RlySrvAddress_Type.__name__=_H
_FsDhcp6RlySrvAddress_Object=MibTableColumn
fsDhcp6RlySrvAddress=_FsDhcp6RlySrvAddress_Object((1,3,6,1,4,1,29601,2,41,2,2,1,2),_FsDhcp6RlySrvAddress_Type())
fsDhcp6RlySrvAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:fsDhcp6RlySrvAddress.setStatus(_A)
_FsDhcp6RlySrvAddressRowStatus_Type=RowStatus
_FsDhcp6RlySrvAddressRowStatus_Object=MibTableColumn
fsDhcp6RlySrvAddressRowStatus=_FsDhcp6RlySrvAddressRowStatus_Object((1,3,6,1,4,1,29601,2,41,2,2,1,3),_FsDhcp6RlySrvAddressRowStatus_Type())
fsDhcp6RlySrvAddressRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6RlySrvAddressRowStatus.setStatus(_A)
_FsDhcp6RlyOutIfTable_Object=MibTable
fsDhcp6RlyOutIfTable=_FsDhcp6RlyOutIfTable_Object((1,3,6,1,4,1,29601,2,41,2,3))
if mibBuilder.loadTexts:fsDhcp6RlyOutIfTable.setStatus(_A)
_FsDhcp6RlyOutIfEntry_Object=MibTableRow
fsDhcp6RlyOutIfEntry=_FsDhcp6RlyOutIfEntry_Object((1,3,6,1,4,1,29601,2,41,2,3,1))
fsDhcp6RlyOutIfEntry.setIndexNames((0,_D,_L),(0,_D,_M),(0,_D,_P))
if mibBuilder.loadTexts:fsDhcp6RlyOutIfEntry.setStatus(_A)
class _FsDhcp6RlyOutIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsDhcp6RlyOutIfIndex_Type.__name__=_C
_FsDhcp6RlyOutIfIndex_Object=MibTableColumn
fsDhcp6RlyOutIfIndex=_FsDhcp6RlyOutIfIndex_Object((1,3,6,1,4,1,29601,2,41,2,3,1,1),_FsDhcp6RlyOutIfIndex_Type())
fsDhcp6RlyOutIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fsDhcp6RlyOutIfIndex.setStatus(_A)
_FsDhcp6RlyOutIfRowStatus_Type=RowStatus
_FsDhcp6RlyOutIfRowStatus_Object=MibTableColumn
fsDhcp6RlyOutIfRowStatus=_FsDhcp6RlyOutIfRowStatus_Object((1,3,6,1,4,1,29601,2,41,2,3,1,2),_FsDhcp6RlyOutIfRowStatus_Type())
fsDhcp6RlyOutIfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcp6RlyOutIfRowStatus.setStatus(_A)
_FsDhcp6RlyTraps_ObjectIdentity=ObjectIdentity
fsDhcp6RlyTraps=_FsDhcp6RlyTraps_ObjectIdentity((1,3,6,1,4,1,29601,2,41,3))
_FsDhcp6RlyTrapIfIndex_Type=Integer32
_FsDhcp6RlyTrapIfIndex_Object=MibScalar
fsDhcp6RlyTrapIfIndex=_FsDhcp6RlyTrapIfIndex_Object((1,3,6,1,4,1,29601,2,41,3,1),_FsDhcp6RlyTrapIfIndex_Type())
fsDhcp6RlyTrapIfIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:fsDhcp6RlyTrapIfIndex.setStatus(_A)
_FsDhcp6RlyTrapInvalidMsgType_Type=Integer32
_FsDhcp6RlyTrapInvalidMsgType_Object=MibScalar
fsDhcp6RlyTrapInvalidMsgType=_FsDhcp6RlyTrapInvalidMsgType_Object((1,3,6,1,4,1,29601,2,41,3,2),_FsDhcp6RlyTrapInvalidMsgType_Type())
fsDhcp6RlyTrapInvalidMsgType.setMaxAccess(_Q)
if mibBuilder.loadTexts:fsDhcp6RlyTrapInvalidMsgType.setStatus(_A)
fsDhcp6RlyRlyInvalidPacketTrap=NotificationType((1,3,6,1,4,1,29601,2,41,0,1))
fsDhcp6RlyRlyInvalidPacketTrap.setObjects(*((_D,_R),(_D,_N)))
if mibBuilder.loadTexts:fsDhcp6RlyRlyInvalidPacketTrap.setStatus(_A)
fsDhcp6RlyRlyMaxHopCountTrap=NotificationType((1,3,6,1,4,1,29601,2,41,0,2))
fsDhcp6RlyRlyMaxHopCountTrap.setObjects((_D,_N))
if mibBuilder.loadTexts:fsDhcp6RlyRlyMaxHopCountTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'fsdhcpv6rly':fsdhcpv6rly,'fsDhcp6RlyNotify':fsDhcp6RlyNotify,'fsDhcp6RlyRlyInvalidPacketTrap':fsDhcp6RlyRlyInvalidPacketTrap,'fsDhcp6RlyRlyMaxHopCountTrap':fsDhcp6RlyRlyMaxHopCountTrap,'fsDhcp6RlySystem':fsDhcp6RlySystem,'fsDhcp6RlyDebugTrace':fsDhcp6RlyDebugTrace,'fsDhcp6RlyTrapAdminControl':fsDhcp6RlyTrapAdminControl,'fsDhcp6RlySysLogAdminStatus':fsDhcp6RlySysLogAdminStatus,'fsDhcp6RlyListenPort':fsDhcp6RlyListenPort,'fsDhcp6RlyClientTransmitPort':fsDhcp6RlyClientTransmitPort,'fsDhcp6RlyServerTransmitPort':fsDhcp6RlyServerTransmitPort,'fsDhcp6RlyOption37Control':fsDhcp6RlyOption37Control,'fsDhcp6RlyPDRouteControl':fsDhcp6RlyPDRouteControl,'fsDhcp6RlyConfig':fsDhcp6RlyConfig,'fsDhcp6RlyIfTable':fsDhcp6RlyIfTable,'fsDhcp6RlyIfEntry':fsDhcp6RlyIfEntry,_O:fsDhcp6RlyIfIndex,'fsDhcp6RlyIfHopThreshold':fsDhcp6RlyIfHopThreshold,'fsDhcp6RlyIfInformIn':fsDhcp6RlyIfInformIn,'fsDhcp6RlyIfRelayForwIn':fsDhcp6RlyIfRelayForwIn,'fsDhcp6RlyIfRelayReplyIn':fsDhcp6RlyIfRelayReplyIn,'fsDhcp6RlyIfInvalidPktIn':fsDhcp6RlyIfInvalidPktIn,'fsDhcp6RlyIfCounterRest':fsDhcp6RlyIfCounterRest,'fsDhcp6RlyIfRowStatus':fsDhcp6RlyIfRowStatus,'fsDhcp6RlyIfRemoteIdOption':fsDhcp6RlyIfRemoteIdOption,'fsDhcp6RlyIfRemoteIdDUID':fsDhcp6RlyIfRemoteIdDUID,'fsDhcp6RlyIfRemoteIdOptionValue':fsDhcp6RlyIfRemoteIdOptionValue,'fsDhcp6RlyIfRemoteIdUserDefined':fsDhcp6RlyIfRemoteIdUserDefined,'fsDhcp6RlyIfRelayForwOut':fsDhcp6RlyIfRelayForwOut,'fsDhcp6RlyIfRelayReplyOut':fsDhcp6RlyIfRelayReplyOut,'fsDhcp6RlyIfRelayState':fsDhcp6RlyIfRelayState,'fsDhcp6RlySrvAddressTable':fsDhcp6RlySrvAddressTable,'fsDhcp6RlySrvAddressEntry':fsDhcp6RlySrvAddressEntry,_L:fsDhcp6RlyInIfIndex,_M:fsDhcp6RlySrvAddress,'fsDhcp6RlySrvAddressRowStatus':fsDhcp6RlySrvAddressRowStatus,'fsDhcp6RlyOutIfTable':fsDhcp6RlyOutIfTable,'fsDhcp6RlyOutIfEntry':fsDhcp6RlyOutIfEntry,_P:fsDhcp6RlyOutIfIndex,'fsDhcp6RlyOutIfRowStatus':fsDhcp6RlyOutIfRowStatus,'fsDhcp6RlyTraps':fsDhcp6RlyTraps,_N:fsDhcp6RlyTrapIfIndex,_R:fsDhcp6RlyTrapInvalidMsgType})