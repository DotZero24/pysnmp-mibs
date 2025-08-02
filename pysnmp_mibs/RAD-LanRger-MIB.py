_z='pppLinkConfigXEntry'
_y='pppLinkStatusXEntry'
_x='lanrangerSpoofingMacAddress'
_w='lanrangerSpoofingGroup'
_v='lanrangerPermanentAddress'
_u='lanrangerPermanentLogLink'
_t='lanrangerPermanentIfIndex'
_s='lanrangerStationAddress'
_r='lanrangerStationLogLink'
_q='lanrangerStationPhysLink'
_p='pppSecurityPriority'
_o='pppSecurityType'
_n='pppoeClientReceivedTagNumber'
_m='compressionOn'
_l='compressionOff'
_k='lanrangerLinkPktSwIndex'
_j='lanrangerModemLinkIndex'
_i='lanrangerLinkConnMacAddr'
_h='connect'
_g='lanrangerLinkIndex'
_f='delete'
_e='active'
_d='lanrangerBootPIpAddress'
_c='failed'
_b='initial'
_a='agnLed'
_Z='RAD-GEN-MIB'
_Y='pPPoEID'
_X='pPPoECnfgIdx'
_W='yes'
_V='none'
_U='down'
_T='fail'
_S='SnmpAdminString'
_R='lanrangerLinkConnAid'
_Q='lanrangerLinkConnPhysLink'
_P='TruthValue'
_O='ifIndex'
_N='IF-MIB'
_M='not-accessible'
_L='on'
_K='enable'
_J='off'
_I='unknown'
_H='disable'
_G='notApplicable'
_F='read-create'
_E='RAD-LanRger-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,ifAlias,ifIndex=mibBuilder.importSymbols(_N,'InterfaceIndexOrZero','ifAlias',_O)
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
pppLinkConfigEntry,pppLinkStatusEntry=mibBuilder.importSymbols('PPP-LCP-MIB','pppLinkConfigEntry','pppLinkStatusEntry')
agnLed,alarmEventLogAlarmOrEventId,alarmEventLogDateAndTime,alarmEventLogDescription,alarmEventLogSeverity,alarmEventLogSourceName,alarmEventReason=mibBuilder.importSymbols(_Z,_a,'alarmEventLogAlarmOrEventId','alarmEventLogDateAndTime','alarmEventLogDescription','alarmEventLogSeverity','alarmEventLogSourceName','alarmEventReason')
radBridges,=mibBuilder.importSymbols('RAD-SMI-MIB','radBridges')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_S)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowPointer,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowPointer','RowStatus','TextualConvention',_P)
lanranger=ModuleIdentity((1,3,6,1,4,1,164,4,2))
class PppAuthMethod(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noAuth',1),('chap',2),('pap',3)))
class PppAuthStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),(_b,2),('completed',3),('inProgress',4),(_c,5)))
class PppState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_b,1),('starting',2),('closed',3),('stopped',4),('closing',5),('stopping',6),('requestSent',7),('ackReceived',8),('ackSent',9),('opened',10)))
_LanrangerEvents_ObjectIdentity=ObjectIdentity
lanrangerEvents=_LanrangerEvents_ObjectIdentity((1,3,6,1,4,1,164,4,2,0))
if mibBuilder.loadTexts:lanrangerEvents.setStatus(_A)
_LanrangerConfig_ObjectIdentity=ObjectIdentity
lanrangerConfig=_LanrangerConfig_ObjectIdentity((1,3,6,1,4,1,164,4,2,1))
class _LanrangerLoc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('main',1),('remote',2)))
_LanrangerLoc_Type.__name__=_D
_LanrangerLoc_Object=MibScalar
lanrangerLoc=_LanrangerLoc_Object((1,3,6,1,4,1,164,4,2,1,1),_LanrangerLoc_Type())
lanrangerLoc.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerLoc.setStatus(_A)
_LanrangerBurnAddress_Type=MacAddress
_LanrangerBurnAddress_Object=MibScalar
lanrangerBurnAddress=_LanrangerBurnAddress_Object((1,3,6,1,4,1,164,4,2,1,2),_LanrangerBurnAddress_Type())
lanrangerBurnAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerBurnAddress.setStatus(_A)
_LanrangerLocAddress_Type=MacAddress
_LanrangerLocAddress_Object=MibScalar
lanrangerLocAddress=_LanrangerLocAddress_Object((1,3,6,1,4,1,164,4,2,1,3),_LanrangerLocAddress_Type())
lanrangerLocAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerLocAddress.setStatus(_A)
class _LanrangerActiveAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('burnedIn',1),('locallyAdministered',2)))
_LanrangerActiveAddress_Type.__name__=_D
_LanrangerActiveAddress_Object=MibScalar
lanrangerActiveAddress=_LanrangerActiveAddress_Object((1,3,6,1,4,1,164,4,2,1,4),_LanrangerActiveAddress_Type())
lanrangerActiveAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerActiveAddress.setStatus(_A)
class _LanrangerLearningStationTopology_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dynamic',1),('permanent',2),('permanentAndDynamic',3)))
_LanrangerLearningStationTopology_Type.__name__=_D
_LanrangerLearningStationTopology_Object=MibScalar
lanrangerLearningStationTopology=_LanrangerLearningStationTopology_Object((1,3,6,1,4,1,164,4,2,1,5),_LanrangerLearningStationTopology_Type())
lanrangerLearningStationTopology.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerLearningStationTopology.setStatus(_A)
_LanrangerIpRouterInfo_ObjectIdentity=ObjectIdentity
lanrangerIpRouterInfo=_LanrangerIpRouterInfo_ObjectIdentity((1,3,6,1,4,1,164,4,2,1,6))
_LanrangerIpDefaultLink_Type=Integer32
_LanrangerIpDefaultLink_Object=MibScalar
lanrangerIpDefaultLink=_LanrangerIpDefaultLink_Object((1,3,6,1,4,1,164,4,2,1,6,1),_LanrangerIpDefaultLink_Type())
lanrangerIpDefaultLink.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerIpDefaultLink.setStatus(_A)
_LanrangerIpFastReTxLevel_Type=Integer32
_LanrangerIpFastReTxLevel_Object=MibScalar
lanrangerIpFastReTxLevel=_LanrangerIpFastReTxLevel_Object((1,3,6,1,4,1,164,4,2,1,6,2),_LanrangerIpFastReTxLevel_Type())
lanrangerIpFastReTxLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerIpFastReTxLevel.setStatus(_A)
_LanrangerIpAgingTimeout_Type=Integer32
_LanrangerIpAgingTimeout_Object=MibScalar
lanrangerIpAgingTimeout=_LanrangerIpAgingTimeout_Object((1,3,6,1,4,1,164,4,2,1,6,3),_LanrangerIpAgingTimeout_Type())
lanrangerIpAgingTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerIpAgingTimeout.setStatus(_A)
_LanrangerIpBootP_ObjectIdentity=ObjectIdentity
lanrangerIpBootP=_LanrangerIpBootP_ObjectIdentity((1,3,6,1,4,1,164,4,2,1,6,4))
class _LanrangerBootPAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_K,3)))
_LanrangerBootPAction_Type.__name__=_D
_LanrangerBootPAction_Object=MibScalar
lanrangerBootPAction=_LanrangerBootPAction_Object((1,3,6,1,4,1,164,4,2,1,6,4,1),_LanrangerBootPAction_Type())
lanrangerBootPAction.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerBootPAction.setStatus(_A)
_LanrangerBootPAvailableEntries_Type=Integer32
_LanrangerBootPAvailableEntries_Object=MibScalar
lanrangerBootPAvailableEntries=_LanrangerBootPAvailableEntries_Object((1,3,6,1,4,1,164,4,2,1,6,4,2),_LanrangerBootPAvailableEntries_Type())
lanrangerBootPAvailableEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerBootPAvailableEntries.setStatus(_A)
_LanrangerBootPCurrentEntries_Type=Integer32
_LanrangerBootPCurrentEntries_Object=MibScalar
lanrangerBootPCurrentEntries=_LanrangerBootPCurrentEntries_Object((1,3,6,1,4,1,164,4,2,1,6,4,3),_LanrangerBootPCurrentEntries_Type())
lanrangerBootPCurrentEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerBootPCurrentEntries.setStatus(_A)
_LanrangerBootPTable_Object=MibTable
lanrangerBootPTable=_LanrangerBootPTable_Object((1,3,6,1,4,1,164,4,2,1,6,4,4))
if mibBuilder.loadTexts:lanrangerBootPTable.setStatus(_A)
_LanrangerBootPEntry_Object=MibTableRow
lanrangerBootPEntry=_LanrangerBootPEntry_Object((1,3,6,1,4,1,164,4,2,1,6,4,4,1))
lanrangerBootPEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:lanrangerBootPEntry.setStatus(_A)
_LanrangerBootPIpAddress_Type=IpAddress
_LanrangerBootPIpAddress_Object=MibTableColumn
lanrangerBootPIpAddress=_LanrangerBootPIpAddress_Object((1,3,6,1,4,1,164,4,2,1,6,4,4,1,1),_LanrangerBootPIpAddress_Type())
lanrangerBootPIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerBootPIpAddress.setStatus(_A)
class _LanrangerBootPIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(255));namedValues=NamedValues(('notAllocated',255))
_LanrangerBootPIfIndex_Type.__name__=_D
_LanrangerBootPIfIndex_Object=MibTableColumn
lanrangerBootPIfIndex=_LanrangerBootPIfIndex_Object((1,3,6,1,4,1,164,4,2,1,6,4,4,1,2),_LanrangerBootPIfIndex_Type())
lanrangerBootPIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerBootPIfIndex.setStatus(_A)
class _LanrangerBootPOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_e,1),(_f,2)))
_LanrangerBootPOperation_Type.__name__=_D
_LanrangerBootPOperation_Object=MibTableColumn
lanrangerBootPOperation=_LanrangerBootPOperation_Object((1,3,6,1,4,1,164,4,2,1,6,4,4,1,3),_LanrangerBootPOperation_Type())
lanrangerBootPOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerBootPOperation.setStatus(_A)
_LanrangerSpoofingInfo_ObjectIdentity=ObjectIdentity
lanrangerSpoofingInfo=_LanrangerSpoofingInfo_ObjectIdentity((1,3,6,1,4,1,164,4,2,1,7))
_LanrangerSpoofingAction_Type=Integer32
_LanrangerSpoofingAction_Object=MibScalar
lanrangerSpoofingAction=_LanrangerSpoofingAction_Object((1,3,6,1,4,1,164,4,2,1,7,1),_LanrangerSpoofingAction_Type())
lanrangerSpoofingAction.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerSpoofingAction.setStatus(_A)
_LanrangerSpoofingAgingStation_Type=Integer32
_LanrangerSpoofingAgingStation_Object=MibScalar
lanrangerSpoofingAgingStation=_LanrangerSpoofingAgingStation_Object((1,3,6,1,4,1,164,4,2,1,7,2),_LanrangerSpoofingAgingStation_Type())
lanrangerSpoofingAgingStation.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerSpoofingAgingStation.setStatus(_A)
_LanrangerInterface_ObjectIdentity=ObjectIdentity
lanrangerInterface=_LanrangerInterface_ObjectIdentity((1,3,6,1,4,1,164,4,2,2))
_LanrangerLinkTable_Object=MibTable
lanrangerLinkTable=_LanrangerLinkTable_Object((1,3,6,1,4,1,164,4,2,2,1))
if mibBuilder.loadTexts:lanrangerLinkTable.setStatus(_A)
_LanrangerLinkEntry_Object=MibTableRow
lanrangerLinkEntry=_LanrangerLinkEntry_Object((1,3,6,1,4,1,164,4,2,2,1,1))
lanrangerLinkEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:lanrangerLinkEntry.setStatus(_A)
_LanrangerLinkIndex_Type=Integer32
_LanrangerLinkIndex_Object=MibTableColumn
lanrangerLinkIndex=_LanrangerLinkIndex_Object((1,3,6,1,4,1,164,4,2,2,1,1,1),_LanrangerLinkIndex_Type())
lanrangerLinkIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerLinkIndex.setStatus(_A)
class _LanrangerLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,254,255)));namedValues=NamedValues(*(('synchronous',1),('asynchronous',2),('x25FRconfig',3),('x25FRchannel',4),('isdn',5),('frameRelay',6),('pcmcia',7),('dm2wire',8),('notExist',254),(_I,255)))
_LanrangerLinkType_Type.__name__=_D
_LanrangerLinkType_Object=MibTableColumn
lanrangerLinkType=_LanrangerLinkType_Object((1,3,6,1,4,1,164,4,2,2,1,1,2),_LanrangerLinkType_Type())
lanrangerLinkType.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerLinkType.setStatus(_A)
class _LanrangerLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*((_H,2),(_K,3),('backup',4)))
_LanrangerLinkState_Type.__name__=_D
_LanrangerLinkState_Object=MibTableColumn
lanrangerLinkState=_LanrangerLinkState_Object((1,3,6,1,4,1,164,4,2,2,1,1,3),_LanrangerLinkState_Type())
lanrangerLinkState.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerLinkState.setStatus(_A)
class _LanrangerLinkDTRMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,255)));namedValues=NamedValues(*((_J,2),(_L,3),(_I,255)))
_LanrangerLinkDTRMode_Type.__name__=_D
_LanrangerLinkDTRMode_Object=MibTableColumn
lanrangerLinkDTRMode=_LanrangerLinkDTRMode_Object((1,3,6,1,4,1,164,4,2,2,1,1,4),_LanrangerLinkDTRMode_Type())
lanrangerLinkDTRMode.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerLinkDTRMode.setStatus(_A)
class _LanrangerLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,255)));namedValues=NamedValues(*(('ok',1),(_T,2),('rxNoClock',3),('txProblem',4),('noCarrierD',5),(_I,255)))
_LanrangerLinkStatus_Type.__name__=_D
_LanrangerLinkStatus_Object=MibTableColumn
lanrangerLinkStatus=_LanrangerLinkStatus_Object((1,3,6,1,4,1,164,4,2,2,1,1,5),_LanrangerLinkStatus_Type())
lanrangerLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerLinkStatus.setStatus(_A)
class _LanrangerLinkConnectionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,255)));namedValues=NamedValues(*((_T,1),('disconnect',2),(_h,3),('wait',4),(_U,5),('trying',6),('testing',7),(_I,255)))
_LanrangerLinkConnectionStatus_Type.__name__=_D
_LanrangerLinkConnectionStatus_Object=MibTableColumn
lanrangerLinkConnectionStatus=_LanrangerLinkConnectionStatus_Object((1,3,6,1,4,1,164,4,2,2,1,1,6),_LanrangerLinkConnectionStatus_Type())
lanrangerLinkConnectionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerLinkConnectionStatus.setStatus(_A)
_LanrangerLinkNumOfLogLinks_Type=Integer32
_LanrangerLinkNumOfLogLinks_Object=MibTableColumn
lanrangerLinkNumOfLogLinks=_LanrangerLinkNumOfLogLinks_Object((1,3,6,1,4,1,164,4,2,2,1,1,7),_LanrangerLinkNumOfLogLinks_Type())
lanrangerLinkNumOfLogLinks.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerLinkNumOfLogLinks.setStatus(_A)
class _LanrangerLinkReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_J,2),(_L,3)))
_LanrangerLinkReset_Type.__name__=_D
_LanrangerLinkReset_Object=MibTableColumn
lanrangerLinkReset=_LanrangerLinkReset_Object((1,3,6,1,4,1,164,4,2,2,1,1,8),_LanrangerLinkReset_Type())
lanrangerLinkReset.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerLinkReset.setStatus(_A)
_LanrangerLinkRxMaskedFrames_Type=Counter32
_LanrangerLinkRxMaskedFrames_Object=MibTableColumn
lanrangerLinkRxMaskedFrames=_LanrangerLinkRxMaskedFrames_Object((1,3,6,1,4,1,164,4,2,2,1,1,9),_LanrangerLinkRxMaskedFrames_Type())
lanrangerLinkRxMaskedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerLinkRxMaskedFrames.setStatus(_A)
class _LanrangerLinkLayer2Type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_I,1),('bridge',2),('ipRouter',3),('ipxRouter',4),('ipAndIpxRouter',5),('bRouter',6),('ipBrouter',7),('ipxBrouter',8),('ipAndIpxBrouter',9),('bridgeAndStp',10)))
_LanrangerLinkLayer2Type_Type.__name__=_D
_LanrangerLinkLayer2Type_Object=MibTableColumn
lanrangerLinkLayer2Type=_LanrangerLinkLayer2Type_Object((1,3,6,1,4,1,164,4,2,2,1,1,10),_LanrangerLinkLayer2Type_Type())
lanrangerLinkLayer2Type.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerLinkLayer2Type.setStatus(_A)
class _LanrangerLinkLayer3Type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,30,31,40,41,42,43)));namedValues=NamedValues(*((_I,1),('proprietary',2),('terminalServer',3),('slip',30),('cSlip',31),('ppp',40),('rfc1490',41),('hdlcFraming',42),('mlPpp',43)))
_LanrangerLinkLayer3Type_Type.__name__=_D
_LanrangerLinkLayer3Type_Object=MibTableColumn
lanrangerLinkLayer3Type=_LanrangerLinkLayer3Type_Object((1,3,6,1,4,1,164,4,2,2,1,1,11),_LanrangerLinkLayer3Type_Type())
lanrangerLinkLayer3Type.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerLinkLayer3Type.setStatus(_A)
_LanrangerBackupLink_Type=Integer32
_LanrangerBackupLink_Object=MibTableColumn
lanrangerBackupLink=_LanrangerBackupLink_Object((1,3,6,1,4,1,164,4,2,2,1,1,12),_LanrangerBackupLink_Type())
lanrangerBackupLink.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerBackupLink.setStatus(_A)
_WrWanThrottle_Type=Integer32
_WrWanThrottle_Object=MibTableColumn
wrWanThrottle=_WrWanThrottle_Object((1,3,6,1,4,1,164,4,2,2,1,1,13),_WrWanThrottle_Type())
wrWanThrottle.setMaxAccess(_C)
if mibBuilder.loadTexts:wrWanThrottle.setStatus(_A)
class _WrIpTransparentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),('enableAll',3)))
_WrIpTransparentMode_Type.__name__=_D
_WrIpTransparentMode_Object=MibTableColumn
wrIpTransparentMode=_WrIpTransparentMode_Object((1,3,6,1,4,1,164,4,2,2,1,1,14),_WrIpTransparentMode_Type())
wrIpTransparentMode.setMaxAccess(_C)
if mibBuilder.loadTexts:wrIpTransparentMode.setStatus(_A)
_WrIpTransparentGateway_Type=IpAddress
_WrIpTransparentGateway_Object=MibTableColumn
wrIpTransparentGateway=_WrIpTransparentGateway_Object((1,3,6,1,4,1,164,4,2,2,1,1,15),_WrIpTransparentGateway_Type())
wrIpTransparentGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:wrIpTransparentGateway.setStatus(_A)
class _LanrangerLinkProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),('noRoutingProtocol',2),('rip1',3),('rip2',4),('rip1OrRip2',5),('ospf',6)))
_LanrangerLinkProtocolType_Type.__name__=_D
_LanrangerLinkProtocolType_Object=MibTableColumn
lanrangerLinkProtocolType=_LanrangerLinkProtocolType_Object((1,3,6,1,4,1,164,4,2,2,1,1,16),_LanrangerLinkProtocolType_Type())
lanrangerLinkProtocolType.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerLinkProtocolType.setStatus(_A)
_LanrangerLinkConnection_ObjectIdentity=ObjectIdentity
lanrangerLinkConnection=_LanrangerLinkConnection_ObjectIdentity((1,3,6,1,4,1,164,4,2,2,2))
_LanrangerConnMaxEntries_Type=Integer32
_LanrangerConnMaxEntries_Object=MibScalar
lanrangerConnMaxEntries=_LanrangerConnMaxEntries_Object((1,3,6,1,4,1,164,4,2,2,2,1),_LanrangerConnMaxEntries_Type())
lanrangerConnMaxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerConnMaxEntries.setStatus(_A)
_LanrangerConnCurrentEntries_Type=Integer32
_LanrangerConnCurrentEntries_Object=MibScalar
lanrangerConnCurrentEntries=_LanrangerConnCurrentEntries_Object((1,3,6,1,4,1,164,4,2,2,2,2),_LanrangerConnCurrentEntries_Type())
lanrangerConnCurrentEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerConnCurrentEntries.setStatus(_A)
_LanrangerLinkConnTable_Object=MibTable
lanrangerLinkConnTable=_LanrangerLinkConnTable_Object((1,3,6,1,4,1,164,4,2,2,2,3))
if mibBuilder.loadTexts:lanrangerLinkConnTable.setStatus(_A)
_LanrangerLinkConnEntry_Object=MibTableRow
lanrangerLinkConnEntry=_LanrangerLinkConnEntry_Object((1,3,6,1,4,1,164,4,2,2,2,3,1))
lanrangerLinkConnEntry.setIndexNames((0,_E,_Q),(0,_E,_R),(0,_E,_i))
if mibBuilder.loadTexts:lanrangerLinkConnEntry.setStatus(_A)
_LanrangerLinkConnPhysLink_Type=Integer32
_LanrangerLinkConnPhysLink_Object=MibTableColumn
lanrangerLinkConnPhysLink=_LanrangerLinkConnPhysLink_Object((1,3,6,1,4,1,164,4,2,2,2,3,1,1),_LanrangerLinkConnPhysLink_Type())
lanrangerLinkConnPhysLink.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerLinkConnPhysLink.setStatus(_A)
_LanrangerLinkConnAid_Type=Integer32
_LanrangerLinkConnAid_Object=MibTableColumn
lanrangerLinkConnAid=_LanrangerLinkConnAid_Object((1,3,6,1,4,1,164,4,2,2,2,3,1,2),_LanrangerLinkConnAid_Type())
lanrangerLinkConnAid.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerLinkConnAid.setStatus(_A)
_LanrangerLinkConnMacAddr_Type=MacAddress
_LanrangerLinkConnMacAddr_Object=MibTableColumn
lanrangerLinkConnMacAddr=_LanrangerLinkConnMacAddr_Object((1,3,6,1,4,1,164,4,2,2,2,3,1,3),_LanrangerLinkConnMacAddr_Type())
lanrangerLinkConnMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerLinkConnMacAddr.setStatus(_A)
class _LanrangerLinkConnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_I,1),(_V,2),(_T,3),(_h,4),('wait',5),(_U,6)))
_LanrangerLinkConnStatus_Type.__name__=_D
_LanrangerLinkConnStatus_Object=MibTableColumn
lanrangerLinkConnStatus=_LanrangerLinkConnStatus_Object((1,3,6,1,4,1,164,4,2,2,2,3,1,4),_LanrangerLinkConnStatus_Type())
lanrangerLinkConnStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerLinkConnStatus.setStatus(_A)
class _LanrangerLinkConnDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,255)));namedValues=NamedValues(*(('tre1',1),('tre8',2),('tre1D',3),('tre8D',4),('tre8M',5),('rrTre',6),('rrTre1D',7),('rrTre8D',8),('iTre1',9),('iTre2',10),('mpTre8',11),('kTre8',12),('treRasA',13),('treRasS',14),('trePCAsync',15),('trePCSync',16),('mbe1',17),('mbe8',18),('mbe1D',19),('mbe8D',20),('ete8M',21),('iEre1',22),('iEe2',23),('mpMbe8',24),('kMbe8',25),('mbePCAsync',26),('mbePCSync',27),('mbeRasA',28),('mbeRasS',29),('other',255)))
_LanrangerLinkConnDeviceType_Type.__name__=_D
_LanrangerLinkConnDeviceType_Object=MibTableColumn
lanrangerLinkConnDeviceType=_LanrangerLinkConnDeviceType_Object((1,3,6,1,4,1,164,4,2,2,2,3,1,5),_LanrangerLinkConnDeviceType_Type())
lanrangerLinkConnDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerLinkConnDeviceType.setStatus(_A)
_LanrangerLinkConnDeviceName_Type=DisplayString
_LanrangerLinkConnDeviceName_Object=MibTableColumn
lanrangerLinkConnDeviceName=_LanrangerLinkConnDeviceName_Object((1,3,6,1,4,1,164,4,2,2,2,3,1,6),_LanrangerLinkConnDeviceName_Type())
lanrangerLinkConnDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerLinkConnDeviceName.setStatus(_A)
_LanrangerLinkConnDeviceSWVer_Type=DisplayString
_LanrangerLinkConnDeviceSWVer_Object=MibTableColumn
lanrangerLinkConnDeviceSWVer=_LanrangerLinkConnDeviceSWVer_Object((1,3,6,1,4,1,164,4,2,2,2,3,1,7),_LanrangerLinkConnDeviceSWVer_Type())
lanrangerLinkConnDeviceSWVer.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerLinkConnDeviceSWVer.setStatus(_A)
_LanrangerLinkConnNumLanStation_Type=Integer32
_LanrangerLinkConnNumLanStation_Object=MibTableColumn
lanrangerLinkConnNumLanStation=_LanrangerLinkConnNumLanStation_Object((1,3,6,1,4,1,164,4,2,2,2,3,1,8),_LanrangerLinkConnNumLanStation_Type())
lanrangerLinkConnNumLanStation.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerLinkConnNumLanStation.setStatus(_A)
class _LanrangerLinkSyncStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41)));namedValues=NamedValues(*(('synchronized',1),('syncNotObtained',2),('waitForSync',3),('codDisconnected',4),('lcp',5),('ip',6),('ipvj',7),('ipx',8),('ipIpx',9),('ipvj-ipx',10),('mlPpp',11),('mlPpp-ip',12),('mlPpp-ip-ipvj',13),('mlPpp-ip-ipx',14),('mlPpp-ipvj-ipx',15),('mlPpp-ipx',16),('frUp',17),('frDown',18),('dlciUp',19),('dlciDown',20),('extLoop',21),('ipcp',22),('lcpIpcp',23),('redAlarm',24),('yellowAlarm',26),('localSyncLoss',27),('remoteSyncLoss',28),('networkLoop',29),('networkLoopRedAlarm',30),('networkLoopYelAlarm',31),('networkLocSyncLoss',32),('networkRemSyncLoss',33),('fdlLoop',34),('fdlLoopRedAlarm',35),('fdlLoopYellowAlarm',36),('fdlLoopLocSyncLoss',37),('fdlLoopRemSyncLoss',38),('loopback',39),('loopbackLocSyncLoss',40),('loopbackRemSyncLoss',41)))
_LanrangerLinkSyncStatus_Type.__name__=_D
_LanrangerLinkSyncStatus_Object=MibTableColumn
lanrangerLinkSyncStatus=_LanrangerLinkSyncStatus_Object((1,3,6,1,4,1,164,4,2,2,2,3,1,9),_LanrangerLinkSyncStatus_Type())
lanrangerLinkSyncStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerLinkSyncStatus.setStatus(_A)
_LanrangerModemTable_Object=MibTable
lanrangerModemTable=_LanrangerModemTable_Object((1,3,6,1,4,1,164,4,2,2,3))
if mibBuilder.loadTexts:lanrangerModemTable.setStatus(_A)
_LanrangerModemEntry_Object=MibTableRow
lanrangerModemEntry=_LanrangerModemEntry_Object((1,3,6,1,4,1,164,4,2,2,3,1))
lanrangerModemEntry.setIndexNames((0,_E,_j))
if mibBuilder.loadTexts:lanrangerModemEntry.setStatus(_A)
_LanrangerModemLinkIndex_Type=Integer32
_LanrangerModemLinkIndex_Object=MibTableColumn
lanrangerModemLinkIndex=_LanrangerModemLinkIndex_Object((1,3,6,1,4,1,164,4,2,2,3,1,1),_LanrangerModemLinkIndex_Type())
lanrangerModemLinkIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerModemLinkIndex.setStatus(_A)
_LanrangerModemName_Type=DisplayString
_LanrangerModemName_Object=MibTableColumn
lanrangerModemName=_LanrangerModemName_Object((1,3,6,1,4,1,164,4,2,2,3,1,2),_LanrangerModemName_Type())
lanrangerModemName.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerModemName.setStatus(_A)
_LanrangerModemSettingString_Type=DisplayString
_LanrangerModemSettingString_Object=MibTableColumn
lanrangerModemSettingString=_LanrangerModemSettingString_Object((1,3,6,1,4,1,164,4,2,2,3,1,3),_LanrangerModemSettingString_Type())
lanrangerModemSettingString.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerModemSettingString.setStatus(_A)
class _LanrangerModemAutobaudingSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_K,3)))
_LanrangerModemAutobaudingSpeed_Type.__name__=_D
_LanrangerModemAutobaudingSpeed_Object=MibTableColumn
lanrangerModemAutobaudingSpeed=_LanrangerModemAutobaudingSpeed_Object((1,3,6,1,4,1,164,4,2,2,3,1,4),_LanrangerModemAutobaudingSpeed_Type())
lanrangerModemAutobaudingSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerModemAutobaudingSpeed.setStatus(_A)
class _LanrangerModemResetBeforeSetup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('no',2),(_W,3)))
_LanrangerModemResetBeforeSetup_Type.__name__=_D
_LanrangerModemResetBeforeSetup_Object=MibTableColumn
lanrangerModemResetBeforeSetup=_LanrangerModemResetBeforeSetup_Object((1,3,6,1,4,1,164,4,2,2,3,1,5),_LanrangerModemResetBeforeSetup_Type())
lanrangerModemResetBeforeSetup.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerModemResetBeforeSetup.setStatus(_A)
class _LanrangerModemAnalyzeAnswers_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_K,3)))
_LanrangerModemAnalyzeAnswers_Type.__name__=_D
_LanrangerModemAnalyzeAnswers_Object=MibTableColumn
lanrangerModemAnalyzeAnswers=_LanrangerModemAnalyzeAnswers_Object((1,3,6,1,4,1,164,4,2,2,3,1,6),_LanrangerModemAnalyzeAnswers_Type())
lanrangerModemAnalyzeAnswers.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerModemAnalyzeAnswers.setStatus(_A)
class _LanrangerModemSpeaker_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_J,2),(_L,3)))
_LanrangerModemSpeaker_Type.__name__=_D
_LanrangerModemSpeaker_Object=MibTableColumn
lanrangerModemSpeaker=_LanrangerModemSpeaker_Object((1,3,6,1,4,1,164,4,2,2,3,1,7),_LanrangerModemSpeaker_Type())
lanrangerModemSpeaker.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerModemSpeaker.setStatus(_A)
_LanrangerModemDialingNumber_Type=DisplayString
_LanrangerModemDialingNumber_Object=MibTableColumn
lanrangerModemDialingNumber=_LanrangerModemDialingNumber_Object((1,3,6,1,4,1,164,4,2,2,3,1,8),_LanrangerModemDialingNumber_Type())
lanrangerModemDialingNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerModemDialingNumber.setStatus(_A)
_WrLocalDialBackNumber_Type=DisplayString
_WrLocalDialBackNumber_Object=MibTableColumn
wrLocalDialBackNumber=_WrLocalDialBackNumber_Object((1,3,6,1,4,1,164,4,2,2,3,1,9),_WrLocalDialBackNumber_Type())
wrLocalDialBackNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:wrLocalDialBackNumber.setStatus(_A)
_WrRingsBeforeAnswer_Type=Integer32
_WrRingsBeforeAnswer_Object=MibTableColumn
wrRingsBeforeAnswer=_WrRingsBeforeAnswer_Object((1,3,6,1,4,1,164,4,2,2,3,1,10),_WrRingsBeforeAnswer_Type())
wrRingsBeforeAnswer.setMaxAccess(_C)
if mibBuilder.loadTexts:wrRingsBeforeAnswer.setStatus(_A)
class _LanrangerModemDialRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_LanrangerModemDialRetries_Type.__name__=_D
_LanrangerModemDialRetries_Object=MibTableColumn
lanrangerModemDialRetries=_LanrangerModemDialRetries_Object((1,3,6,1,4,1,164,4,2,2,3,1,11),_LanrangerModemDialRetries_Type())
lanrangerModemDialRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerModemDialRetries.setStatus(_A)
_LanrangerLinkPktSwTable_Object=MibTable
lanrangerLinkPktSwTable=_LanrangerLinkPktSwTable_Object((1,3,6,1,4,1,164,4,2,2,4))
if mibBuilder.loadTexts:lanrangerLinkPktSwTable.setStatus(_A)
_LanrangerLinkPktSwEntry_Object=MibTableRow
lanrangerLinkPktSwEntry=_LanrangerLinkPktSwEntry_Object((1,3,6,1,4,1,164,4,2,2,4,1))
lanrangerLinkPktSwEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:lanrangerLinkPktSwEntry.setStatus(_A)
_LanrangerLinkPktSwIndex_Type=Integer32
_LanrangerLinkPktSwIndex_Object=MibTableColumn
lanrangerLinkPktSwIndex=_LanrangerLinkPktSwIndex_Object((1,3,6,1,4,1,164,4,2,2,4,1,1),_LanrangerLinkPktSwIndex_Type())
lanrangerLinkPktSwIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerLinkPktSwIndex.setStatus(_A)
class _LanrangerLinkPktSwType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('x25FRChannel',1),('x25FRConfig',2)))
_LanrangerLinkPktSwType_Type.__name__=_D
_LanrangerLinkPktSwType_Object=MibTableColumn
lanrangerLinkPktSwType=_LanrangerLinkPktSwType_Object((1,3,6,1,4,1,164,4,2,2,4,1,2),_LanrangerLinkPktSwType_Type())
lanrangerLinkPktSwType.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerLinkPktSwType.setStatus(_A)
class _LanrangerLinkPktSwControlSignal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_J,2),(_L,3)))
_LanrangerLinkPktSwControlSignal_Type.__name__=_D
_LanrangerLinkPktSwControlSignal_Object=MibTableColumn
lanrangerLinkPktSwControlSignal=_LanrangerLinkPktSwControlSignal_Object((1,3,6,1,4,1,164,4,2,2,4,1,3),_LanrangerLinkPktSwControlSignal_Type())
lanrangerLinkPktSwControlSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerLinkPktSwControlSignal.setStatus(_A)
_LanrangerLinkPktSwSpeed_Type=Integer32
_LanrangerLinkPktSwSpeed_Object=MibTableColumn
lanrangerLinkPktSwSpeed=_LanrangerLinkPktSwSpeed_Object((1,3,6,1,4,1,164,4,2,2,4,1,4),_LanrangerLinkPktSwSpeed_Type())
lanrangerLinkPktSwSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerLinkPktSwSpeed.setStatus(_A)
class _LanrangerLinkPktSwConfigParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*((_V,1),('odd',2),('even',3),(_G,255)))
_LanrangerLinkPktSwConfigParity_Type.__name__=_D
_LanrangerLinkPktSwConfigParity_Object=MibTableColumn
lanrangerLinkPktSwConfigParity=_LanrangerLinkPktSwConfigParity_Object((1,3,6,1,4,1,164,4,2,2,4,1,5),_LanrangerLinkPktSwConfigParity_Type())
lanrangerLinkPktSwConfigParity.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerLinkPktSwConfigParity.setStatus(_A)
class _LanrangerLinkPktSwConfigStopBit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('one',1),('two',2),(_G,255)))
_LanrangerLinkPktSwConfigStopBit_Type.__name__=_D
_LanrangerLinkPktSwConfigStopBit_Object=MibTableColumn
lanrangerLinkPktSwConfigStopBit=_LanrangerLinkPktSwConfigStopBit_Object((1,3,6,1,4,1,164,4,2,2,4,1,6),_LanrangerLinkPktSwConfigStopBit_Type())
lanrangerLinkPktSwConfigStopBit.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerLinkPktSwConfigStopBit.setStatus(_A)
class _LanrangerLinkPktSwResetModule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_J,2),(_L,3)))
_LanrangerLinkPktSwResetModule_Type.__name__=_D
_LanrangerLinkPktSwResetModule_Object=MibTableColumn
lanrangerLinkPktSwResetModule=_LanrangerLinkPktSwResetModule_Object((1,3,6,1,4,1,164,4,2,2,4,1,7),_LanrangerLinkPktSwResetModule_Type())
lanrangerLinkPktSwResetModule.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerLinkPktSwResetModule.setStatus(_A)
_WrPPPTable_Object=MibTable
wrPPPTable=_WrPPPTable_Object((1,3,6,1,4,1,164,4,2,2,5))
if mibBuilder.loadTexts:wrPPPTable.setStatus(_A)
_WrPPPEntry_Object=MibTableRow
wrPPPEntry=_WrPPPEntry_Object((1,3,6,1,4,1,164,4,2,2,5,1))
wrPPPEntry.setIndexNames((0,_N,_O))
if mibBuilder.loadTexts:wrPPPEntry.setStatus(_A)
class _WrPPPCompressionHeaderField_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_l,2),(_m,3)))
_WrPPPCompressionHeaderField_Type.__name__=_D
_WrPPPCompressionHeaderField_Object=MibTableColumn
wrPPPCompressionHeaderField=_WrPPPCompressionHeaderField_Object((1,3,6,1,4,1,164,4,2,2,5,1,1),_WrPPPCompressionHeaderField_Type())
wrPPPCompressionHeaderField.setMaxAccess(_C)
if mibBuilder.loadTexts:wrPPPCompressionHeaderField.setStatus(_A)
class _WrPPPCompressionProtocolFields_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_l,2),(_m,3)))
_WrPPPCompressionProtocolFields_Type.__name__=_D
_WrPPPCompressionProtocolFields_Object=MibTableColumn
wrPPPCompressionProtocolFields=_WrPPPCompressionProtocolFields_Object((1,3,6,1,4,1,164,4,2,2,5,1,2),_WrPPPCompressionProtocolFields_Type())
wrPPPCompressionProtocolFields.setMaxAccess(_C)
if mibBuilder.loadTexts:wrPPPCompressionProtocolFields.setStatus(_A)
class _WrPPPSTACCompressionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),('noHistory',2),('lCB',3),('sequence',4),('extended',5)))
_WrPPPSTACCompressionType_Type.__name__=_D
_WrPPPSTACCompressionType_Object=MibTableColumn
wrPPPSTACCompressionType=_WrPPPSTACCompressionType_Object((1,3,6,1,4,1,164,4,2,2,5,1,3),_WrPPPSTACCompressionType_Type())
wrPPPSTACCompressionType.setMaxAccess(_C)
if mibBuilder.loadTexts:wrPPPSTACCompressionType.setStatus(_A)
class _WrPPPAuthProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('noneNone',1),('chapNone',2),('chapPap',3),('chapChap',4),('papNone',5),('papPap',6)))
_WrPPPAuthProtocol_Type.__name__=_D
_WrPPPAuthProtocol_Object=MibTableColumn
wrPPPAuthProtocol=_WrPPPAuthProtocol_Object((1,3,6,1,4,1,164,4,2,2,5,1,4),_WrPPPAuthProtocol_Type())
wrPPPAuthProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:wrPPPAuthProtocol.setStatus(_A)
class _WrPPPSecurityType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('host',1),('guest',2)))
_WrPPPSecurityType_Type.__name__=_D
_WrPPPSecurityType_Object=MibTableColumn
wrPPPSecurityType=_WrPPPSecurityType_Object((1,3,6,1,4,1,164,4,2,2,5,1,5),_WrPPPSecurityType_Type())
wrPPPSecurityType.setMaxAccess(_C)
if mibBuilder.loadTexts:wrPPPSecurityType.setStatus(_A)
class _WrPPPUserName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,36))
_WrPPPUserName_Type.__name__=_S
_WrPPPUserName_Object=MibTableColumn
wrPPPUserName=_WrPPPUserName_Object((1,3,6,1,4,1,164,4,2,2,5,1,6),_WrPPPUserName_Type())
wrPPPUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:wrPPPUserName.setStatus(_A)
class _WrPPPPassword_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,36))
_WrPPPPassword_Type.__name__=_S
_WrPPPPassword_Object=MibTableColumn
wrPPPPassword=_WrPPPPassword_Object((1,3,6,1,4,1,164,4,2,2,5,1,7),_WrPPPPassword_Type())
wrPPPPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:wrPPPPassword.setStatus(_A)
_WrPPPLinkActiveTime_Type=Integer32
_WrPPPLinkActiveTime_Object=MibTableColumn
wrPPPLinkActiveTime=_WrPPPLinkActiveTime_Object((1,3,6,1,4,1,164,4,2,2,5,1,8),_WrPPPLinkActiveTime_Type())
wrPPPLinkActiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:wrPPPLinkActiveTime.setStatus(_A)
_WrPPPIPCPSubnetMaskNegotiation_Type=InterfaceIndexOrZero
_WrPPPIPCPSubnetMaskNegotiation_Object=MibTableColumn
wrPPPIPCPSubnetMaskNegotiation=_WrPPPIPCPSubnetMaskNegotiation_Object((1,3,6,1,4,1,164,4,2,2,5,1,9),_WrPPPIPCPSubnetMaskNegotiation_Type())
wrPPPIPCPSubnetMaskNegotiation.setMaxAccess(_C)
if mibBuilder.loadTexts:wrPPPIPCPSubnetMaskNegotiation.setStatus(_A)
class _WrPPPLinkControlProtocolStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('close',2),('open',3)))
_WrPPPLinkControlProtocolStatus_Type.__name__=_D
_WrPPPLinkControlProtocolStatus_Object=MibTableColumn
wrPPPLinkControlProtocolStatus=_WrPPPLinkControlProtocolStatus_Object((1,3,6,1,4,1,164,4,2,2,5,1,10),_WrPPPLinkControlProtocolStatus_Type())
wrPPPLinkControlProtocolStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wrPPPLinkControlProtocolStatus.setStatus(_A)
class _WrPPPAuthenticationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_c,2),('passed',3)))
_WrPPPAuthenticationStatus_Type.__name__=_D
_WrPPPAuthenticationStatus_Object=MibTableColumn
wrPPPAuthenticationStatus=_WrPPPAuthenticationStatus_Object((1,3,6,1,4,1,164,4,2,2,5,1,11),_WrPPPAuthenticationStatus_Type())
wrPPPAuthenticationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wrPPPAuthenticationStatus.setStatus(_A)
class _WrPPPIpcpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('close',2),('open',3)))
_WrPPPIpcpStatus_Type.__name__=_D
_WrPPPIpcpStatus_Object=MibTableColumn
wrPPPIpcpStatus=_WrPPPIpcpStatus_Object((1,3,6,1,4,1,164,4,2,2,5,1,12),_WrPPPIpcpStatus_Type())
wrPPPIpcpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wrPPPIpcpStatus.setStatus(_A)
_WrPPPAssignedIPAddress_Type=IpAddress
_WrPPPAssignedIPAddress_Object=MibTableColumn
wrPPPAssignedIPAddress=_WrPPPAssignedIPAddress_Object((1,3,6,1,4,1,164,4,2,2,5,1,13),_WrPPPAssignedIPAddress_Type())
wrPPPAssignedIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wrPPPAssignedIPAddress.setStatus(_A)
class _WrPPPActualAuthProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_V,1),('pap',2),('chap',3)))
_WrPPPActualAuthProtocol_Type.__name__=_D
_WrPPPActualAuthProtocol_Object=MibTableColumn
wrPPPActualAuthProtocol=_WrPPPActualAuthProtocol_Object((1,3,6,1,4,1,164,4,2,2,5,1,14),_WrPPPActualAuthProtocol_Type())
wrPPPActualAuthProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:wrPPPActualAuthProtocol.setStatus(_A)
class _WrPPPIpTranslationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_K,3)))
_WrPPPIpTranslationMode_Type.__name__=_D
_WrPPPIpTranslationMode_Object=MibTableColumn
wrPPPIpTranslationMode=_WrPPPIpTranslationMode_Object((1,3,6,1,4,1,164,4,2,2,5,1,15),_WrPPPIpTranslationMode_Type())
wrPPPIpTranslationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:wrPPPIpTranslationMode.setStatus(_A)
_WrPPPTranslatedIpAddr_Type=IpAddress
_WrPPPTranslatedIpAddr_Object=MibTableColumn
wrPPPTranslatedIpAddr=_WrPPPTranslatedIpAddr_Object((1,3,6,1,4,1,164,4,2,2,5,1,16),_WrPPPTranslatedIpAddr_Type())
wrPPPTranslatedIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:wrPPPTranslatedIpAddr.setStatus(_A)
_WrMLPPPTable_Object=MibTable
wrMLPPPTable=_WrMLPPPTable_Object((1,3,6,1,4,1,164,4,2,2,6))
if mibBuilder.loadTexts:wrMLPPPTable.setStatus(_A)
_WrMLPPPEntry_Object=MibTableRow
wrMLPPPEntry=_WrMLPPPEntry_Object((1,3,6,1,4,1,164,4,2,2,6,1))
wrMLPPPEntry.setIndexNames((0,_N,_O))
if mibBuilder.loadTexts:wrMLPPPEntry.setStatus(_A)
class _WrMLPPPEpDiscriminatorEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('no',2),(_W,3)))
_WrMLPPPEpDiscriminatorEnable_Type.__name__=_D
_WrMLPPPEpDiscriminatorEnable_Object=MibTableColumn
wrMLPPPEpDiscriminatorEnable=_WrMLPPPEpDiscriminatorEnable_Object((1,3,6,1,4,1,164,4,2,2,6,1,1),_WrMLPPPEpDiscriminatorEnable_Type())
wrMLPPPEpDiscriminatorEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:wrMLPPPEpDiscriminatorEnable.setStatus(_A)
class _WrMLPPPReorderingEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('no',2),(_W,3)))
_WrMLPPPReorderingEnable_Type.__name__=_D
_WrMLPPPReorderingEnable_Object=MibTableColumn
wrMLPPPReorderingEnable=_WrMLPPPReorderingEnable_Object((1,3,6,1,4,1,164,4,2,2,6,1,2),_WrMLPPPReorderingEnable_Type())
wrMLPPPReorderingEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:wrMLPPPReorderingEnable.setStatus(_A)
_WrMLPPPTxQueueSize_Type=Unsigned32
_WrMLPPPTxQueueSize_Object=MibTableColumn
wrMLPPPTxQueueSize=_WrMLPPPTxQueueSize_Object((1,3,6,1,4,1,164,4,2,2,6,1,3),_WrMLPPPTxQueueSize_Type())
wrMLPPPTxQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:wrMLPPPTxQueueSize.setStatus(_A)
_PPPoE_ObjectIdentity=ObjectIdentity
pPPoE=_PPPoE_ObjectIdentity((1,3,6,1,4,1,164,4,2,2,7))
_PPPoETable_Object=MibTable
pPPoETable=_PPPoETable_Object((1,3,6,1,4,1,164,4,2,2,7,1))
if mibBuilder.loadTexts:pPPoETable.setStatus(_A)
_PPPoEEntry_Object=MibTableRow
pPPoEEntry=_PPPoEEntry_Object((1,3,6,1,4,1,164,4,2,2,7,1,1))
pPPoEEntry.setIndexNames((0,_E,_X),(0,_E,_Y))
if mibBuilder.loadTexts:pPPoEEntry.setStatus(_A)
_PPPoECnfgIdx_Type=Unsigned32
_PPPoECnfgIdx_Object=MibTableColumn
pPPoECnfgIdx=_PPPoECnfgIdx_Object((1,3,6,1,4,1,164,4,2,2,7,1,1,1),_PPPoECnfgIdx_Type())
pPPoECnfgIdx.setMaxAccess(_M)
if mibBuilder.loadTexts:pPPoECnfgIdx.setStatus(_A)
_PPPoEID_Type=Unsigned32
_PPPoEID_Object=MibTableColumn
pPPoEID=_PPPoEID_Object((1,3,6,1,4,1,164,4,2,2,7,1,1,2),_PPPoEID_Type())
pPPoEID.setMaxAccess(_M)
if mibBuilder.loadTexts:pPPoEID.setStatus(_A)
_PPPoERowStatus_Type=RowStatus
_PPPoERowStatus_Object=MibTableColumn
pPPoERowStatus=_PPPoERowStatus_Object((1,3,6,1,4,1,164,4,2,2,7,1,1,3),_PPPoERowStatus_Type())
pPPoERowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:pPPoERowStatus.setStatus(_A)
_PPPoEACName_Type=SnmpAdminString
_PPPoEACName_Object=MibTableColumn
pPPoEACName=_PPPoEACName_Object((1,3,6,1,4,1,164,4,2,2,7,1,1,4),_PPPoEACName_Type())
pPPoEACName.setMaxAccess(_F)
if mibBuilder.loadTexts:pPPoEACName.setStatus(_A)
_PPPoEServiceName_Type=SnmpAdminString
_PPPoEServiceName_Object=MibTableColumn
pPPoEServiceName=_PPPoEServiceName_Object((1,3,6,1,4,1,164,4,2,2,7,1,1,5),_PPPoEServiceName_Type())
pPPoEServiceName.setMaxAccess(_F)
if mibBuilder.loadTexts:pPPoEServiceName.setStatus(_A)
_PPPoEEntityPointer_Type=RowPointer
_PPPoEEntityPointer_Object=MibTableColumn
pPPoEEntityPointer=_PPPoEEntityPointer_Object((1,3,6,1,4,1,164,4,2,2,7,1,1,6),_PPPoEEntityPointer_Type())
pPPoEEntityPointer.setMaxAccess(_F)
if mibBuilder.loadTexts:pPPoEEntityPointer.setStatus(_A)
class _PPPoESessionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),(_U,2),('up',3),('lowerLayerDown',4),('adminDisabled',5)))
_PPPoESessionStatus_Type.__name__=_D
_PPPoESessionStatus_Object=MibTableColumn
pPPoESessionStatus=_PPPoESessionStatus_Object((1,3,6,1,4,1,164,4,2,2,7,1,1,7),_PPPoESessionStatus_Type())
pPPoESessionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:pPPoESessionStatus.setStatus(_A)
_PPPoESessionID_Type=Unsigned32
_PPPoESessionID_Object=MibTableColumn
pPPoESessionID=_PPPoESessionID_Object((1,3,6,1,4,1,164,4,2,2,7,1,1,8),_PPPoESessionID_Type())
pPPoESessionID.setMaxAccess(_B)
if mibBuilder.loadTexts:pPPoESessionID.setStatus(_A)
_PPPoERemoteMacAddr_Type=MacAddress
_PPPoERemoteMacAddr_Object=MibTableColumn
pPPoERemoteMacAddr=_PPPoERemoteMacAddr_Object((1,3,6,1,4,1,164,4,2,2,7,1,1,9),_PPPoERemoteMacAddr_Type())
pPPoERemoteMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:pPPoERemoteMacAddr.setStatus(_A)
_PPPoENoOfUsages_Type=Unsigned32
_PPPoENoOfUsages_Object=MibTableColumn
pPPoENoOfUsages=_PPPoENoOfUsages_Object((1,3,6,1,4,1,164,4,2,2,7,1,1,10),_PPPoENoOfUsages_Type())
pPPoENoOfUsages.setMaxAccess(_B)
if mibBuilder.loadTexts:pPPoENoOfUsages.setStatus(_A)
class _PPPoESchedRestartMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_K,3)))
_PPPoESchedRestartMode_Type.__name__=_D
_PPPoESchedRestartMode_Object=MibTableColumn
pPPoESchedRestartMode=_PPPoESchedRestartMode_Object((1,3,6,1,4,1,164,4,2,2,7,1,1,11),_PPPoESchedRestartMode_Type())
pPPoESchedRestartMode.setMaxAccess(_F)
if mibBuilder.loadTexts:pPPoESchedRestartMode.setStatus(_A)
_PPPoESchedRestartTime_Type=DisplayString
_PPPoESchedRestartTime_Object=MibTableColumn
pPPoESchedRestartTime=_PPPoESchedRestartTime_Object((1,3,6,1,4,1,164,4,2,2,7,1,1,12),_PPPoESchedRestartTime_Type())
pPPoESchedRestartTime.setMaxAccess(_F)
if mibBuilder.loadTexts:pPPoESchedRestartTime.setStatus(_A)
_PPPoESchedRestartRandomRange_Type=Unsigned32
_PPPoESchedRestartRandomRange_Object=MibTableColumn
pPPoESchedRestartRandomRange=_PPPoESchedRestartRandomRange_Object((1,3,6,1,4,1,164,4,2,2,7,1,1,13),_PPPoESchedRestartRandomRange_Type())
pPPoESchedRestartRandomRange.setMaxAccess(_F)
if mibBuilder.loadTexts:pPPoESchedRestartRandomRange.setStatus(_A)
_PPPoESchedRestartActualTime_Type=DisplayString
_PPPoESchedRestartActualTime_Object=MibTableColumn
pPPoESchedRestartActualTime=_PPPoESchedRestartActualTime_Object((1,3,6,1,4,1,164,4,2,2,7,1,1,14),_PPPoESchedRestartActualTime_Type())
pPPoESchedRestartActualTime.setMaxAccess(_B)
if mibBuilder.loadTexts:pPPoESchedRestartActualTime.setStatus(_A)
_PPPoEInitDelayRandomRange_Type=Unsigned32
_PPPoEInitDelayRandomRange_Object=MibTableColumn
pPPoEInitDelayRandomRange=_PPPoEInitDelayRandomRange_Object((1,3,6,1,4,1,164,4,2,2,7,1,1,15),_PPPoEInitDelayRandomRange_Type())
pPPoEInitDelayRandomRange.setMaxAccess(_F)
if mibBuilder.loadTexts:pPPoEInitDelayRandomRange.setStatus(_A)
_PPPoEInitActualDelay_Type=Unsigned32
_PPPoEInitActualDelay_Object=MibTableColumn
pPPoEInitActualDelay=_PPPoEInitActualDelay_Object((1,3,6,1,4,1,164,4,2,2,7,1,1,16),_PPPoEInitActualDelay_Type())
pPPoEInitActualDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:pPPoEInitActualDelay.setStatus(_A)
class _PPPoEVlanTagging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('untag',2),('tag',3)))
_PPPoEVlanTagging_Type.__name__=_D
_PPPoEVlanTagging_Object=MibTableColumn
pPPoEVlanTagging=_PPPoEVlanTagging_Object((1,3,6,1,4,1,164,4,2,2,7,1,1,17),_PPPoEVlanTagging_Type())
pPPoEVlanTagging.setMaxAccess(_F)
if mibBuilder.loadTexts:pPPoEVlanTagging.setStatus(_A)
_PPPoEVlanId_Type=Unsigned32
_PPPoEVlanId_Object=MibTableColumn
pPPoEVlanId=_PPPoEVlanId_Object((1,3,6,1,4,1,164,4,2,2,7,1,1,18),_PPPoEVlanId_Type())
pPPoEVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:pPPoEVlanId.setStatus(_A)
_PPPoEVlanPriority_Type=Unsigned32
_PPPoEVlanPriority_Object=MibTableColumn
pPPoEVlanPriority=_PPPoEVlanPriority_Object((1,3,6,1,4,1,164,4,2,2,7,1,1,19),_PPPoEVlanPriority_Type())
pPPoEVlanPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:pPPoEVlanPriority.setStatus(_A)
_PppoeClientReceivedTagsTable_Object=MibTable
pppoeClientReceivedTagsTable=_PppoeClientReceivedTagsTable_Object((1,3,6,1,4,1,164,4,2,2,7,2))
if mibBuilder.loadTexts:pppoeClientReceivedTagsTable.setStatus(_A)
_PppoeClientReceivedTagsEntry_Object=MibTableRow
pppoeClientReceivedTagsEntry=_PppoeClientReceivedTagsEntry_Object((1,3,6,1,4,1,164,4,2,2,7,2,1))
pppoeClientReceivedTagsEntry.setIndexNames((0,_E,_X),(0,_E,_Y),(0,_E,_n))
if mibBuilder.loadTexts:pppoeClientReceivedTagsEntry.setStatus(_A)
_PppoeClientReceivedTagNumber_Type=Unsigned32
_PppoeClientReceivedTagNumber_Object=MibTableColumn
pppoeClientReceivedTagNumber=_PppoeClientReceivedTagNumber_Object((1,3,6,1,4,1,164,4,2,2,7,2,1,1),_PppoeClientReceivedTagNumber_Type())
pppoeClientReceivedTagNumber.setMaxAccess(_M)
if mibBuilder.loadTexts:pppoeClientReceivedTagNumber.setStatus(_A)
_PppoeClientReceivedTagType_Type=Unsigned32
_PppoeClientReceivedTagType_Object=MibTableColumn
pppoeClientReceivedTagType=_PppoeClientReceivedTagType_Object((1,3,6,1,4,1,164,4,2,2,7,2,1,2),_PppoeClientReceivedTagType_Type())
pppoeClientReceivedTagType.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeClientReceivedTagType.setStatus(_A)
_PppoeClientReceivedTagValue_Type=SnmpAdminString
_PppoeClientReceivedTagValue_Object=MibTableColumn
pppoeClientReceivedTagValue=_PppoeClientReceivedTagValue_Object((1,3,6,1,4,1,164,4,2,2,7,2,1,3),_PppoeClientReceivedTagValue_Type())
pppoeClientReceivedTagValue.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeClientReceivedTagValue.setStatus(_A)
_PppSecurityTable_Object=MibTable
pppSecurityTable=_PppSecurityTable_Object((1,3,6,1,4,1,164,4,2,2,8))
if mibBuilder.loadTexts:pppSecurityTable.setStatus(_A)
_PppSecurityEntry_Object=MibTableRow
pppSecurityEntry=_PppSecurityEntry_Object((1,3,6,1,4,1,164,4,2,2,8,1))
pppSecurityEntry.setIndexNames((0,_N,_O),(0,_E,_o),(0,_E,_p))
if mibBuilder.loadTexts:pppSecurityEntry.setStatus(_A)
class _PppSecurityType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('chapHostname',1),('chapPassword',2),('papUsername',3)))
_PppSecurityType_Type.__name__=_D
_PppSecurityType_Object=MibTableColumn
pppSecurityType=_PppSecurityType_Object((1,3,6,1,4,1,164,4,2,2,8,1,1),_PppSecurityType_Type())
pppSecurityType.setMaxAccess(_M)
if mibBuilder.loadTexts:pppSecurityType.setStatus(_A)
_PppSecurityPriority_Type=Unsigned32
_PppSecurityPriority_Object=MibTableColumn
pppSecurityPriority=_PppSecurityPriority_Object((1,3,6,1,4,1,164,4,2,2,8,1,2),_PppSecurityPriority_Type())
pppSecurityPriority.setMaxAccess(_M)
if mibBuilder.loadTexts:pppSecurityPriority.setStatus(_A)
_PppSecurityRowStatus_Type=RowStatus
_PppSecurityRowStatus_Object=MibTableColumn
pppSecurityRowStatus=_PppSecurityRowStatus_Object((1,3,6,1,4,1,164,4,2,2,8,1,3),_PppSecurityRowStatus_Type())
pppSecurityRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:pppSecurityRowStatus.setStatus(_A)
class _PppSecurityDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('localToRemote',1),('remoteToLocal',2)))
_PppSecurityDirection_Type.__name__=_D
_PppSecurityDirection_Object=MibTableColumn
pppSecurityDirection=_PppSecurityDirection_Object((1,3,6,1,4,1,164,4,2,2,8,1,4),_PppSecurityDirection_Type())
pppSecurityDirection.setMaxAccess(_F)
if mibBuilder.loadTexts:pppSecurityDirection.setStatus(_A)
_PppSecurityIdentity_Type=SnmpAdminString
_PppSecurityIdentity_Object=MibTableColumn
pppSecurityIdentity=_PppSecurityIdentity_Object((1,3,6,1,4,1,164,4,2,2,8,1,5),_PppSecurityIdentity_Type())
pppSecurityIdentity.setMaxAccess(_F)
if mibBuilder.loadTexts:pppSecurityIdentity.setStatus(_A)
_PppSecuritySecret_Type=SnmpAdminString
_PppSecuritySecret_Object=MibTableColumn
pppSecuritySecret=_PppSecuritySecret_Object((1,3,6,1,4,1,164,4,2,2,8,1,6),_PppSecuritySecret_Type())
pppSecuritySecret.setMaxAccess(_F)
if mibBuilder.loadTexts:pppSecuritySecret.setStatus(_A)
class _PppSecuritySecretType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('clear',2),('encrypted',3)))
_PppSecuritySecretType_Type.__name__=_D
_PppSecuritySecretType_Object=MibTableColumn
pppSecuritySecretType=_PppSecuritySecretType_Object((1,3,6,1,4,1,164,4,2,2,8,1,7),_PppSecuritySecretType_Type())
pppSecuritySecretType.setMaxAccess(_F)
if mibBuilder.loadTexts:pppSecuritySecretType.setStatus(_A)
_PppLinkStatusXTable_Object=MibTable
pppLinkStatusXTable=_PppLinkStatusXTable_Object((1,3,6,1,4,1,164,4,2,2,9))
if mibBuilder.loadTexts:pppLinkStatusXTable.setStatus(_A)
_PppLinkStatusXEntry_Object=MibTableRow
pppLinkStatusXEntry=_PppLinkStatusXEntry_Object((1,3,6,1,4,1,164,4,2,2,9,1))
if mibBuilder.loadTexts:pppLinkStatusXEntry.setStatus(_A)
_PppLinkStatusXLcpState_Type=PppState
_PppLinkStatusXLcpState_Object=MibTableColumn
pppLinkStatusXLcpState=_PppLinkStatusXLcpState_Object((1,3,6,1,4,1,164,4,2,2,9,1,1),_PppLinkStatusXLcpState_Type())
pppLinkStatusXLcpState.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusXLcpState.setStatus(_A)
_PppLinkStatusXUsAuthProtocol_Type=PppAuthMethod
_PppLinkStatusXUsAuthProtocol_Object=MibTableColumn
pppLinkStatusXUsAuthProtocol=_PppLinkStatusXUsAuthProtocol_Object((1,3,6,1,4,1,164,4,2,2,9,1,2),_PppLinkStatusXUsAuthProtocol_Type())
pppLinkStatusXUsAuthProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusXUsAuthProtocol.setStatus(_A)
_PppLinkStatusXUsAuthState_Type=PppAuthStatus
_PppLinkStatusXUsAuthState_Object=MibTableColumn
pppLinkStatusXUsAuthState=_PppLinkStatusXUsAuthState_Object((1,3,6,1,4,1,164,4,2,2,9,1,3),_PppLinkStatusXUsAuthState_Type())
pppLinkStatusXUsAuthState.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusXUsAuthState.setStatus(_A)
_PppLinkStatusXUsAuthIdentity_Type=SnmpAdminString
_PppLinkStatusXUsAuthIdentity_Object=MibTableColumn
pppLinkStatusXUsAuthIdentity=_PppLinkStatusXUsAuthIdentity_Object((1,3,6,1,4,1,164,4,2,2,9,1,4),_PppLinkStatusXUsAuthIdentity_Type())
pppLinkStatusXUsAuthIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusXUsAuthIdentity.setStatus(_A)
_PppLinkStatusXPeerAuthProtocol_Type=PppAuthMethod
_PppLinkStatusXPeerAuthProtocol_Object=MibTableColumn
pppLinkStatusXPeerAuthProtocol=_PppLinkStatusXPeerAuthProtocol_Object((1,3,6,1,4,1,164,4,2,2,9,1,5),_PppLinkStatusXPeerAuthProtocol_Type())
pppLinkStatusXPeerAuthProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusXPeerAuthProtocol.setStatus(_A)
_PppLinkStatusXPeerAuthState_Type=PppAuthStatus
_PppLinkStatusXPeerAuthState_Object=MibTableColumn
pppLinkStatusXPeerAuthState=_PppLinkStatusXPeerAuthState_Object((1,3,6,1,4,1,164,4,2,2,9,1,6),_PppLinkStatusXPeerAuthState_Type())
pppLinkStatusXPeerAuthState.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusXPeerAuthState.setStatus(_A)
_PppLinkStatusXPeerAuthIdentity_Type=SnmpAdminString
_PppLinkStatusXPeerAuthIdentity_Object=MibTableColumn
pppLinkStatusXPeerAuthIdentity=_PppLinkStatusXPeerAuthIdentity_Object((1,3,6,1,4,1,164,4,2,2,9,1,7),_PppLinkStatusXPeerAuthIdentity_Type())
pppLinkStatusXPeerAuthIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusXPeerAuthIdentity.setStatus(_A)
_PppLinkStatusXIpcpState_Type=PppState
_PppLinkStatusXIpcpState_Object=MibTableColumn
pppLinkStatusXIpcpState=_PppLinkStatusXIpcpState_Object((1,3,6,1,4,1,164,4,2,2,9,1,8),_PppLinkStatusXIpcpState_Type())
pppLinkStatusXIpcpState.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusXIpcpState.setStatus(_A)
_PppLinkStatusXIpcpLocalIp_Type=InetAddressIPv4
_PppLinkStatusXIpcpLocalIp_Object=MibTableColumn
pppLinkStatusXIpcpLocalIp=_PppLinkStatusXIpcpLocalIp_Object((1,3,6,1,4,1,164,4,2,2,9,1,9),_PppLinkStatusXIpcpLocalIp_Type())
pppLinkStatusXIpcpLocalIp.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusXIpcpLocalIp.setStatus(_A)
_PppLinkStatusXIpcpLocalIpNegotiated_Type=TruthValue
_PppLinkStatusXIpcpLocalIpNegotiated_Object=MibTableColumn
pppLinkStatusXIpcpLocalIpNegotiated=_PppLinkStatusXIpcpLocalIpNegotiated_Object((1,3,6,1,4,1,164,4,2,2,9,1,10),_PppLinkStatusXIpcpLocalIpNegotiated_Type())
pppLinkStatusXIpcpLocalIpNegotiated.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusXIpcpLocalIpNegotiated.setStatus(_A)
_PppLinkStatusXIpcpRemoteIp_Type=InetAddressIPv4
_PppLinkStatusXIpcpRemoteIp_Object=MibTableColumn
pppLinkStatusXIpcpRemoteIp=_PppLinkStatusXIpcpRemoteIp_Object((1,3,6,1,4,1,164,4,2,2,9,1,11),_PppLinkStatusXIpcpRemoteIp_Type())
pppLinkStatusXIpcpRemoteIp.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusXIpcpRemoteIp.setStatus(_A)
_PppLinkStatusXIpv6cpState_Type=PppState
_PppLinkStatusXIpv6cpState_Object=MibTableColumn
pppLinkStatusXIpv6cpState=_PppLinkStatusXIpv6cpState_Object((1,3,6,1,4,1,164,4,2,2,9,1,12),_PppLinkStatusXIpv6cpState_Type())
pppLinkStatusXIpv6cpState.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusXIpv6cpState.setStatus(_A)
_PppLinkStatusXIpv6cpLocalIp_Type=InetAddressIPv6
_PppLinkStatusXIpv6cpLocalIp_Object=MibTableColumn
pppLinkStatusXIpv6cpLocalIp=_PppLinkStatusXIpv6cpLocalIp_Object((1,3,6,1,4,1,164,4,2,2,9,1,13),_PppLinkStatusXIpv6cpLocalIp_Type())
pppLinkStatusXIpv6cpLocalIp.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusXIpv6cpLocalIp.setStatus(_A)
_PppLinkStatusXIpv6cpLocalIpNegotiated_Type=TruthValue
_PppLinkStatusXIpv6cpLocalIpNegotiated_Object=MibTableColumn
pppLinkStatusXIpv6cpLocalIpNegotiated=_PppLinkStatusXIpv6cpLocalIpNegotiated_Object((1,3,6,1,4,1,164,4,2,2,9,1,14),_PppLinkStatusXIpv6cpLocalIpNegotiated_Type())
pppLinkStatusXIpv6cpLocalIpNegotiated.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusXIpv6cpLocalIpNegotiated.setStatus(_A)
_PppLinkStatusXIpv6cpRemoteIp_Type=InetAddressIPv6
_PppLinkStatusXIpv6cpRemoteIp_Object=MibTableColumn
pppLinkStatusXIpv6cpRemoteIp=_PppLinkStatusXIpv6cpRemoteIp_Object((1,3,6,1,4,1,164,4,2,2,9,1,15),_PppLinkStatusXIpv6cpRemoteIp_Type())
pppLinkStatusXIpv6cpRemoteIp.setMaxAccess(_B)
if mibBuilder.loadTexts:pppLinkStatusXIpv6cpRemoteIp.setStatus(_A)
_PppLinkConfigXTable_Object=MibTable
pppLinkConfigXTable=_PppLinkConfigXTable_Object((1,3,6,1,4,1,164,4,2,2,10))
if mibBuilder.loadTexts:pppLinkConfigXTable.setStatus(_A)
_PppLinkConfigXEntry_Object=MibTableRow
pppLinkConfigXEntry=_PppLinkConfigXEntry_Object((1,3,6,1,4,1,164,4,2,2,10,1))
if mibBuilder.loadTexts:pppLinkConfigXEntry.setStatus(_A)
_PppLinkConfigXLowerLayer_Type=Unsigned32
_PppLinkConfigXLowerLayer_Object=MibTableColumn
pppLinkConfigXLowerLayer=_PppLinkConfigXLowerLayer_Object((1,3,6,1,4,1,164,4,2,2,10,1,1),_PppLinkConfigXLowerLayer_Type())
pppLinkConfigXLowerLayer.setMaxAccess(_C)
if mibBuilder.loadTexts:pppLinkConfigXLowerLayer.setStatus(_A)
class _PppLinkConfigXRefuseChap_Type(TruthValue):defaultValue=2
_PppLinkConfigXRefuseChap_Type.__name__=_P
_PppLinkConfigXRefuseChap_Object=MibTableColumn
pppLinkConfigXRefuseChap=_PppLinkConfigXRefuseChap_Object((1,3,6,1,4,1,164,4,2,2,10,1,2),_PppLinkConfigXRefuseChap_Type())
pppLinkConfigXRefuseChap.setMaxAccess(_C)
if mibBuilder.loadTexts:pppLinkConfigXRefuseChap.setStatus(_A)
class _PppLinkConfigXRefuseNoAuth_Type(TruthValue):defaultValue=1
_PppLinkConfigXRefuseNoAuth_Type.__name__=_P
_PppLinkConfigXRefuseNoAuth_Object=MibTableColumn
pppLinkConfigXRefuseNoAuth=_PppLinkConfigXRefuseNoAuth_Object((1,3,6,1,4,1,164,4,2,2,10,1,3),_PppLinkConfigXRefuseNoAuth_Type())
pppLinkConfigXRefuseNoAuth.setMaxAccess(_C)
if mibBuilder.loadTexts:pppLinkConfigXRefuseNoAuth.setStatus(_A)
class _PppLinkConfigXRefusePap_Type(TruthValue):defaultValue=1
_PppLinkConfigXRefusePap_Type.__name__=_P
_PppLinkConfigXRefusePap_Object=MibTableColumn
pppLinkConfigXRefusePap=_PppLinkConfigXRefusePap_Object((1,3,6,1,4,1,164,4,2,2,10,1,4),_PppLinkConfigXRefusePap_Type())
pppLinkConfigXRefusePap.setMaxAccess(_C)
if mibBuilder.loadTexts:pppLinkConfigXRefusePap.setStatus(_A)
_LanrangerStation_ObjectIdentity=ObjectIdentity
lanrangerStation=_LanrangerStation_ObjectIdentity((1,3,6,1,4,1,164,4,2,3))
_LanrangerStationTable_Object=MibTable
lanrangerStationTable=_LanrangerStationTable_Object((1,3,6,1,4,1,164,4,2,3,1))
if mibBuilder.loadTexts:lanrangerStationTable.setStatus(_A)
_LanrangerStationEntry_Object=MibTableRow
lanrangerStationEntry=_LanrangerStationEntry_Object((1,3,6,1,4,1,164,4,2,3,1,1))
lanrangerStationEntry.setIndexNames((0,_E,_q),(0,_E,_r),(0,_E,_s))
if mibBuilder.loadTexts:lanrangerStationEntry.setStatus(_A)
_LanrangerStationPhysLink_Type=Integer32
_LanrangerStationPhysLink_Object=MibTableColumn
lanrangerStationPhysLink=_LanrangerStationPhysLink_Object((1,3,6,1,4,1,164,4,2,3,1,1,1),_LanrangerStationPhysLink_Type())
lanrangerStationPhysLink.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerStationPhysLink.setStatus(_A)
_LanrangerStationLogLink_Type=Integer32
_LanrangerStationLogLink_Object=MibTableColumn
lanrangerStationLogLink=_LanrangerStationLogLink_Object((1,3,6,1,4,1,164,4,2,3,1,1,2),_LanrangerStationLogLink_Type())
lanrangerStationLogLink.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerStationLogLink.setStatus(_A)
_LanrangerStationAddress_Type=MacAddress
_LanrangerStationAddress_Object=MibTableColumn
lanrangerStationAddress=_LanrangerStationAddress_Object((1,3,6,1,4,1,164,4,2,3,1,1,3),_LanrangerStationAddress_Type())
lanrangerStationAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerStationAddress.setStatus(_A)
class _LanrangerStationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),('learned',2),('self',3),('static',4)))
_LanrangerStationStatus_Type.__name__=_D
_LanrangerStationStatus_Object=MibTableColumn
lanrangerStationStatus=_LanrangerStationStatus_Object((1,3,6,1,4,1,164,4,2,3,1,1,4),_LanrangerStationStatus_Type())
lanrangerStationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerStationStatus.setStatus(_A)
class _LanrangerStationSpoofingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_J,2),(_L,3)))
_LanrangerStationSpoofingStatus_Type.__name__=_D
_LanrangerStationSpoofingStatus_Object=MibTableColumn
lanrangerStationSpoofingStatus=_LanrangerStationSpoofingStatus_Object((1,3,6,1,4,1,164,4,2,3,1,1,5),_LanrangerStationSpoofingStatus_Type())
lanrangerStationSpoofingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerStationSpoofingStatus.setStatus(_A)
_LanrangerLanMaxStations_Type=Integer32
_LanrangerLanMaxStations_Object=MibScalar
lanrangerLanMaxStations=_LanrangerLanMaxStations_Object((1,3,6,1,4,1,164,4,2,3,2),_LanrangerLanMaxStations_Type())
lanrangerLanMaxStations.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerLanMaxStations.setStatus(_A)
_LanrangerLanCurrentStations_Type=Integer32
_LanrangerLanCurrentStations_Object=MibScalar
lanrangerLanCurrentStations=_LanrangerLanCurrentStations_Object((1,3,6,1,4,1,164,4,2,3,3),_LanrangerLanCurrentStations_Type())
lanrangerLanCurrentStations.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerLanCurrentStations.setStatus(_A)
_LanrangerPermanentStation_ObjectIdentity=ObjectIdentity
lanrangerPermanentStation=_LanrangerPermanentStation_ObjectIdentity((1,3,6,1,4,1,164,4,2,3,4))
_LanrangerPermanentMaxEntries_Type=Integer32
_LanrangerPermanentMaxEntries_Object=MibScalar
lanrangerPermanentMaxEntries=_LanrangerPermanentMaxEntries_Object((1,3,6,1,4,1,164,4,2,3,4,1),_LanrangerPermanentMaxEntries_Type())
lanrangerPermanentMaxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerPermanentMaxEntries.setStatus(_A)
_LanrangerPermanentCurrentEntries_Type=Integer32
_LanrangerPermanentCurrentEntries_Object=MibScalar
lanrangerPermanentCurrentEntries=_LanrangerPermanentCurrentEntries_Object((1,3,6,1,4,1,164,4,2,3,4,2),_LanrangerPermanentCurrentEntries_Type())
lanrangerPermanentCurrentEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerPermanentCurrentEntries.setStatus(_A)
_LanrangerPermanentTable_Object=MibTable
lanrangerPermanentTable=_LanrangerPermanentTable_Object((1,3,6,1,4,1,164,4,2,3,4,3))
if mibBuilder.loadTexts:lanrangerPermanentTable.setStatus(_A)
_LanrangerPermanentEntry_Object=MibTableRow
lanrangerPermanentEntry=_LanrangerPermanentEntry_Object((1,3,6,1,4,1,164,4,2,3,4,3,1))
lanrangerPermanentEntry.setIndexNames((0,_E,_t),(0,_E,_u),(0,_E,_v))
if mibBuilder.loadTexts:lanrangerPermanentEntry.setStatus(_A)
_LanrangerPermanentIfIndex_Type=Integer32
_LanrangerPermanentIfIndex_Object=MibTableColumn
lanrangerPermanentIfIndex=_LanrangerPermanentIfIndex_Object((1,3,6,1,4,1,164,4,2,3,4,3,1,1),_LanrangerPermanentIfIndex_Type())
lanrangerPermanentIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerPermanentIfIndex.setStatus(_A)
_LanrangerPermanentLogLink_Type=Integer32
_LanrangerPermanentLogLink_Object=MibTableColumn
lanrangerPermanentLogLink=_LanrangerPermanentLogLink_Object((1,3,6,1,4,1,164,4,2,3,4,3,1,2),_LanrangerPermanentLogLink_Type())
lanrangerPermanentLogLink.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerPermanentLogLink.setStatus(_A)
_LanrangerPermanentAddress_Type=MacAddress
_LanrangerPermanentAddress_Object=MibTableColumn
lanrangerPermanentAddress=_LanrangerPermanentAddress_Object((1,3,6,1,4,1,164,4,2,3,4,3,1,3),_LanrangerPermanentAddress_Type())
lanrangerPermanentAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerPermanentAddress.setStatus(_A)
class _LanrangerPermanentOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_e,1),(_f,2)))
_LanrangerPermanentOperation_Type.__name__=_D
_LanrangerPermanentOperation_Object=MibTableColumn
lanrangerPermanentOperation=_LanrangerPermanentOperation_Object((1,3,6,1,4,1,164,4,2,3,4,3,1,4),_LanrangerPermanentOperation_Type())
lanrangerPermanentOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:lanrangerPermanentOperation.setStatus(_A)
_LanrangerIpStation_ObjectIdentity=ObjectIdentity
lanrangerIpStation=_LanrangerIpStation_ObjectIdentity((1,3,6,1,4,1,164,4,2,3,5))
_LanrangerIpPermanentAvailableEntries_Type=Integer32
_LanrangerIpPermanentAvailableEntries_Object=MibScalar
lanrangerIpPermanentAvailableEntries=_LanrangerIpPermanentAvailableEntries_Object((1,3,6,1,4,1,164,4,2,3,5,1),_LanrangerIpPermanentAvailableEntries_Type())
lanrangerIpPermanentAvailableEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerIpPermanentAvailableEntries.setStatus(_A)
_LanrangerIpPermanentCurrentEntries_Type=Integer32
_LanrangerIpPermanentCurrentEntries_Object=MibScalar
lanrangerIpPermanentCurrentEntries=_LanrangerIpPermanentCurrentEntries_Object((1,3,6,1,4,1,164,4,2,3,5,2),_LanrangerIpPermanentCurrentEntries_Type())
lanrangerIpPermanentCurrentEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerIpPermanentCurrentEntries.setStatus(_A)
_LanrangerSpoofingStation_ObjectIdentity=ObjectIdentity
lanrangerSpoofingStation=_LanrangerSpoofingStation_ObjectIdentity((1,3,6,1,4,1,164,4,2,3,6))
_LanrangerSpoofingMaxEntries_Type=Integer32
_LanrangerSpoofingMaxEntries_Object=MibScalar
lanrangerSpoofingMaxEntries=_LanrangerSpoofingMaxEntries_Object((1,3,6,1,4,1,164,4,2,3,6,1),_LanrangerSpoofingMaxEntries_Type())
lanrangerSpoofingMaxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerSpoofingMaxEntries.setStatus(_A)
_LanrangerSpoofingCurrentEntries_Type=Integer32
_LanrangerSpoofingCurrentEntries_Object=MibScalar
lanrangerSpoofingCurrentEntries=_LanrangerSpoofingCurrentEntries_Object((1,3,6,1,4,1,164,4,2,3,6,2),_LanrangerSpoofingCurrentEntries_Type())
lanrangerSpoofingCurrentEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerSpoofingCurrentEntries.setStatus(_A)
_LanrangerSpoofingTable_Object=MibTable
lanrangerSpoofingTable=_LanrangerSpoofingTable_Object((1,3,6,1,4,1,164,4,2,3,6,3))
if mibBuilder.loadTexts:lanrangerSpoofingTable.setStatus(_A)
_LanrangerSpoofingEntry_Object=MibTableRow
lanrangerSpoofingEntry=_LanrangerSpoofingEntry_Object((1,3,6,1,4,1,164,4,2,3,6,3,1))
lanrangerSpoofingEntry.setIndexNames((0,_E,_w),(0,_E,_x))
if mibBuilder.loadTexts:lanrangerSpoofingEntry.setStatus(_A)
_LanrangerSpoofingGroup_Type=Integer32
_LanrangerSpoofingGroup_Object=MibTableColumn
lanrangerSpoofingGroup=_LanrangerSpoofingGroup_Object((1,3,6,1,4,1,164,4,2,3,6,3,1,1),_LanrangerSpoofingGroup_Type())
lanrangerSpoofingGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerSpoofingGroup.setStatus(_A)
_LanrangerSpoofingMacAddress_Type=MacAddress
_LanrangerSpoofingMacAddress_Object=MibTableColumn
lanrangerSpoofingMacAddress=_LanrangerSpoofingMacAddress_Object((1,3,6,1,4,1,164,4,2,3,6,3,1,2),_LanrangerSpoofingMacAddress_Type())
lanrangerSpoofingMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerSpoofingMacAddress.setStatus(_A)
_LanrangerSpoofingAging_Type=Integer32
_LanrangerSpoofingAging_Object=MibTableColumn
lanrangerSpoofingAging=_LanrangerSpoofingAging_Object((1,3,6,1,4,1,164,4,2,3,6,3,1,3),_LanrangerSpoofingAging_Type())
lanrangerSpoofingAging.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerSpoofingAging.setStatus(_A)
_LanrangerSpoofingTimeLeft_Type=Integer32
_LanrangerSpoofingTimeLeft_Object=MibTableColumn
lanrangerSpoofingTimeLeft=_LanrangerSpoofingTimeLeft_Object((1,3,6,1,4,1,164,4,2,3,6,3,1,4),_LanrangerSpoofingTimeLeft_Type())
lanrangerSpoofingTimeLeft.setMaxAccess(_B)
if mibBuilder.loadTexts:lanrangerSpoofingTimeLeft.setStatus(_A)
pppLinkStatusEntry.registerAugmentions((_E,_y))
pppLinkStatusXEntry.setIndexNames(*pppLinkStatusEntry.getIndexNames())
pppLinkConfigEntry.registerAugmentions((_E,_z))
pppLinkConfigXEntry.setIndexNames(*pppLinkConfigEntry.getIndexNames())
lanrangerLogLinkUp=NotificationType((1,3,6,1,4,1,164,4,2,0,1))
lanrangerLogLinkUp.setObjects(*((_E,_Q),(_E,_R)))
if mibBuilder.loadTexts:lanrangerLogLinkUp.setStatus(_A)
lanrangerLogLinkDown=NotificationType((1,3,6,1,4,1,164,4,2,0,2))
lanrangerLogLinkDown.setObjects(*((_E,_Q),(_E,_R)))
if mibBuilder.loadTexts:lanrangerLogLinkDown.setStatus(_A)
lanrangerLanTableOverflow=NotificationType((1,3,6,1,4,1,164,4,2,0,3))
if mibBuilder.loadTexts:lanrangerLanTableOverflow.setStatus(_A)
lanrangerStatusChanged=NotificationType((1,3,6,1,4,1,164,4,2,0,4))
lanrangerStatusChanged.setObjects((_Z,_a))
if mibBuilder.loadTexts:lanrangerStatusChanged.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'PppAuthMethod':PppAuthMethod,'PppAuthStatus':PppAuthStatus,'PppState':PppState,'lanranger':lanranger,'lanrangerEvents':lanrangerEvents,'lanrangerLogLinkUp':lanrangerLogLinkUp,'lanrangerLogLinkDown':lanrangerLogLinkDown,'lanrangerLanTableOverflow':lanrangerLanTableOverflow,'lanrangerStatusChanged':lanrangerStatusChanged,'lanrangerConfig':lanrangerConfig,'lanrangerLoc':lanrangerLoc,'lanrangerBurnAddress':lanrangerBurnAddress,'lanrangerLocAddress':lanrangerLocAddress,'lanrangerActiveAddress':lanrangerActiveAddress,'lanrangerLearningStationTopology':lanrangerLearningStationTopology,'lanrangerIpRouterInfo':lanrangerIpRouterInfo,'lanrangerIpDefaultLink':lanrangerIpDefaultLink,'lanrangerIpFastReTxLevel':lanrangerIpFastReTxLevel,'lanrangerIpAgingTimeout':lanrangerIpAgingTimeout,'lanrangerIpBootP':lanrangerIpBootP,'lanrangerBootPAction':lanrangerBootPAction,'lanrangerBootPAvailableEntries':lanrangerBootPAvailableEntries,'lanrangerBootPCurrentEntries':lanrangerBootPCurrentEntries,'lanrangerBootPTable':lanrangerBootPTable,'lanrangerBootPEntry':lanrangerBootPEntry,_d:lanrangerBootPIpAddress,'lanrangerBootPIfIndex':lanrangerBootPIfIndex,'lanrangerBootPOperation':lanrangerBootPOperation,'lanrangerSpoofingInfo':lanrangerSpoofingInfo,'lanrangerSpoofingAction':lanrangerSpoofingAction,'lanrangerSpoofingAgingStation':lanrangerSpoofingAgingStation,'lanrangerInterface':lanrangerInterface,'lanrangerLinkTable':lanrangerLinkTable,'lanrangerLinkEntry':lanrangerLinkEntry,_g:lanrangerLinkIndex,'lanrangerLinkType':lanrangerLinkType,'lanrangerLinkState':lanrangerLinkState,'lanrangerLinkDTRMode':lanrangerLinkDTRMode,'lanrangerLinkStatus':lanrangerLinkStatus,'lanrangerLinkConnectionStatus':lanrangerLinkConnectionStatus,'lanrangerLinkNumOfLogLinks':lanrangerLinkNumOfLogLinks,'lanrangerLinkReset':lanrangerLinkReset,'lanrangerLinkRxMaskedFrames':lanrangerLinkRxMaskedFrames,'lanrangerLinkLayer2Type':lanrangerLinkLayer2Type,'lanrangerLinkLayer3Type':lanrangerLinkLayer3Type,'lanrangerBackupLink':lanrangerBackupLink,'wrWanThrottle':wrWanThrottle,'wrIpTransparentMode':wrIpTransparentMode,'wrIpTransparentGateway':wrIpTransparentGateway,'lanrangerLinkProtocolType':lanrangerLinkProtocolType,'lanrangerLinkConnection':lanrangerLinkConnection,'lanrangerConnMaxEntries':lanrangerConnMaxEntries,'lanrangerConnCurrentEntries':lanrangerConnCurrentEntries,'lanrangerLinkConnTable':lanrangerLinkConnTable,'lanrangerLinkConnEntry':lanrangerLinkConnEntry,_Q:lanrangerLinkConnPhysLink,_R:lanrangerLinkConnAid,_i:lanrangerLinkConnMacAddr,'lanrangerLinkConnStatus':lanrangerLinkConnStatus,'lanrangerLinkConnDeviceType':lanrangerLinkConnDeviceType,'lanrangerLinkConnDeviceName':lanrangerLinkConnDeviceName,'lanrangerLinkConnDeviceSWVer':lanrangerLinkConnDeviceSWVer,'lanrangerLinkConnNumLanStation':lanrangerLinkConnNumLanStation,'lanrangerLinkSyncStatus':lanrangerLinkSyncStatus,'lanrangerModemTable':lanrangerModemTable,'lanrangerModemEntry':lanrangerModemEntry,_j:lanrangerModemLinkIndex,'lanrangerModemName':lanrangerModemName,'lanrangerModemSettingString':lanrangerModemSettingString,'lanrangerModemAutobaudingSpeed':lanrangerModemAutobaudingSpeed,'lanrangerModemResetBeforeSetup':lanrangerModemResetBeforeSetup,'lanrangerModemAnalyzeAnswers':lanrangerModemAnalyzeAnswers,'lanrangerModemSpeaker':lanrangerModemSpeaker,'lanrangerModemDialingNumber':lanrangerModemDialingNumber,'wrLocalDialBackNumber':wrLocalDialBackNumber,'wrRingsBeforeAnswer':wrRingsBeforeAnswer,'lanrangerModemDialRetries':lanrangerModemDialRetries,'lanrangerLinkPktSwTable':lanrangerLinkPktSwTable,'lanrangerLinkPktSwEntry':lanrangerLinkPktSwEntry,_k:lanrangerLinkPktSwIndex,'lanrangerLinkPktSwType':lanrangerLinkPktSwType,'lanrangerLinkPktSwControlSignal':lanrangerLinkPktSwControlSignal,'lanrangerLinkPktSwSpeed':lanrangerLinkPktSwSpeed,'lanrangerLinkPktSwConfigParity':lanrangerLinkPktSwConfigParity,'lanrangerLinkPktSwConfigStopBit':lanrangerLinkPktSwConfigStopBit,'lanrangerLinkPktSwResetModule':lanrangerLinkPktSwResetModule,'wrPPPTable':wrPPPTable,'wrPPPEntry':wrPPPEntry,'wrPPPCompressionHeaderField':wrPPPCompressionHeaderField,'wrPPPCompressionProtocolFields':wrPPPCompressionProtocolFields,'wrPPPSTACCompressionType':wrPPPSTACCompressionType,'wrPPPAuthProtocol':wrPPPAuthProtocol,'wrPPPSecurityType':wrPPPSecurityType,'wrPPPUserName':wrPPPUserName,'wrPPPPassword':wrPPPPassword,'wrPPPLinkActiveTime':wrPPPLinkActiveTime,'wrPPPIPCPSubnetMaskNegotiation':wrPPPIPCPSubnetMaskNegotiation,'wrPPPLinkControlProtocolStatus':wrPPPLinkControlProtocolStatus,'wrPPPAuthenticationStatus':wrPPPAuthenticationStatus,'wrPPPIpcpStatus':wrPPPIpcpStatus,'wrPPPAssignedIPAddress':wrPPPAssignedIPAddress,'wrPPPActualAuthProtocol':wrPPPActualAuthProtocol,'wrPPPIpTranslationMode':wrPPPIpTranslationMode,'wrPPPTranslatedIpAddr':wrPPPTranslatedIpAddr,'wrMLPPPTable':wrMLPPPTable,'wrMLPPPEntry':wrMLPPPEntry,'wrMLPPPEpDiscriminatorEnable':wrMLPPPEpDiscriminatorEnable,'wrMLPPPReorderingEnable':wrMLPPPReorderingEnable,'wrMLPPPTxQueueSize':wrMLPPPTxQueueSize,'pPPoE':pPPoE,'pPPoETable':pPPoETable,'pPPoEEntry':pPPoEEntry,_X:pPPoECnfgIdx,_Y:pPPoEID,'pPPoERowStatus':pPPoERowStatus,'pPPoEACName':pPPoEACName,'pPPoEServiceName':pPPoEServiceName,'pPPoEEntityPointer':pPPoEEntityPointer,'pPPoESessionStatus':pPPoESessionStatus,'pPPoESessionID':pPPoESessionID,'pPPoERemoteMacAddr':pPPoERemoteMacAddr,'pPPoENoOfUsages':pPPoENoOfUsages,'pPPoESchedRestartMode':pPPoESchedRestartMode,'pPPoESchedRestartTime':pPPoESchedRestartTime,'pPPoESchedRestartRandomRange':pPPoESchedRestartRandomRange,'pPPoESchedRestartActualTime':pPPoESchedRestartActualTime,'pPPoEInitDelayRandomRange':pPPoEInitDelayRandomRange,'pPPoEInitActualDelay':pPPoEInitActualDelay,'pPPoEVlanTagging':pPPoEVlanTagging,'pPPoEVlanId':pPPoEVlanId,'pPPoEVlanPriority':pPPoEVlanPriority,'pppoeClientReceivedTagsTable':pppoeClientReceivedTagsTable,'pppoeClientReceivedTagsEntry':pppoeClientReceivedTagsEntry,_n:pppoeClientReceivedTagNumber,'pppoeClientReceivedTagType':pppoeClientReceivedTagType,'pppoeClientReceivedTagValue':pppoeClientReceivedTagValue,'pppSecurityTable':pppSecurityTable,'pppSecurityEntry':pppSecurityEntry,_o:pppSecurityType,_p:pppSecurityPriority,'pppSecurityRowStatus':pppSecurityRowStatus,'pppSecurityDirection':pppSecurityDirection,'pppSecurityIdentity':pppSecurityIdentity,'pppSecuritySecret':pppSecuritySecret,'pppSecuritySecretType':pppSecuritySecretType,'pppLinkStatusXTable':pppLinkStatusXTable,_y:pppLinkStatusXEntry,'pppLinkStatusXLcpState':pppLinkStatusXLcpState,'pppLinkStatusXUsAuthProtocol':pppLinkStatusXUsAuthProtocol,'pppLinkStatusXUsAuthState':pppLinkStatusXUsAuthState,'pppLinkStatusXUsAuthIdentity':pppLinkStatusXUsAuthIdentity,'pppLinkStatusXPeerAuthProtocol':pppLinkStatusXPeerAuthProtocol,'pppLinkStatusXPeerAuthState':pppLinkStatusXPeerAuthState,'pppLinkStatusXPeerAuthIdentity':pppLinkStatusXPeerAuthIdentity,'pppLinkStatusXIpcpState':pppLinkStatusXIpcpState,'pppLinkStatusXIpcpLocalIp':pppLinkStatusXIpcpLocalIp,'pppLinkStatusXIpcpLocalIpNegotiated':pppLinkStatusXIpcpLocalIpNegotiated,'pppLinkStatusXIpcpRemoteIp':pppLinkStatusXIpcpRemoteIp,'pppLinkStatusXIpv6cpState':pppLinkStatusXIpv6cpState,'pppLinkStatusXIpv6cpLocalIp':pppLinkStatusXIpv6cpLocalIp,'pppLinkStatusXIpv6cpLocalIpNegotiated':pppLinkStatusXIpv6cpLocalIpNegotiated,'pppLinkStatusXIpv6cpRemoteIp':pppLinkStatusXIpv6cpRemoteIp,'pppLinkConfigXTable':pppLinkConfigXTable,_z:pppLinkConfigXEntry,'pppLinkConfigXLowerLayer':pppLinkConfigXLowerLayer,'pppLinkConfigXRefuseChap':pppLinkConfigXRefuseChap,'pppLinkConfigXRefuseNoAuth':pppLinkConfigXRefuseNoAuth,'pppLinkConfigXRefusePap':pppLinkConfigXRefusePap,'lanrangerStation':lanrangerStation,'lanrangerStationTable':lanrangerStationTable,'lanrangerStationEntry':lanrangerStationEntry,_q:lanrangerStationPhysLink,_r:lanrangerStationLogLink,_s:lanrangerStationAddress,'lanrangerStationStatus':lanrangerStationStatus,'lanrangerStationSpoofingStatus':lanrangerStationSpoofingStatus,'lanrangerLanMaxStations':lanrangerLanMaxStations,'lanrangerLanCurrentStations':lanrangerLanCurrentStations,'lanrangerPermanentStation':lanrangerPermanentStation,'lanrangerPermanentMaxEntries':lanrangerPermanentMaxEntries,'lanrangerPermanentCurrentEntries':lanrangerPermanentCurrentEntries,'lanrangerPermanentTable':lanrangerPermanentTable,'lanrangerPermanentEntry':lanrangerPermanentEntry,_t:lanrangerPermanentIfIndex,_u:lanrangerPermanentLogLink,_v:lanrangerPermanentAddress,'lanrangerPermanentOperation':lanrangerPermanentOperation,'lanrangerIpStation':lanrangerIpStation,'lanrangerIpPermanentAvailableEntries':lanrangerIpPermanentAvailableEntries,'lanrangerIpPermanentCurrentEntries':lanrangerIpPermanentCurrentEntries,'lanrangerSpoofingStation':lanrangerSpoofingStation,'lanrangerSpoofingMaxEntries':lanrangerSpoofingMaxEntries,'lanrangerSpoofingCurrentEntries':lanrangerSpoofingCurrentEntries,'lanrangerSpoofingTable':lanrangerSpoofingTable,'lanrangerSpoofingEntry':lanrangerSpoofingEntry,_w:lanrangerSpoofingGroup,_x:lanrangerSpoofingMacAddress,'lanrangerSpoofingAging':lanrangerSpoofingAging,'lanrangerSpoofingTimeLeft':lanrangerSpoofingTimeLeft})