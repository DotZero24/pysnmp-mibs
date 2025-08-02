_y='adTWAMPNumOfSpawnedReflectors'
_x='adTWAMPVerboseReflectorStatsTestTmoStatus'
_w='adTWAMPVerboseReflectorStatsTestTmoRemaining'
_v='adTWAMPVerboseReflectorStatsTestTmo'
_u='adTWAMPVerboseReflectorStatsPacketTimeout'
_t='adTWAMPVerboseReflectorStatsTypePDescriptor'
_s='adTWAMPVerboseReflectorStatsPaddingLength'
_r='adTWAMPVerboseReflectorStatsTxTestPkts'
_q='adTWAMPVerboseReflectorStatsRxTestPkts'
_p='adTWAMPVerboseReflectorStatsState'
_o='adTWAMPAssociatedClientTcpSourcePort'
_n='adTWAMPAssociatedClientIpAddress'
_m='adTWAMPSenderUdpSourcePort'
_l='adTWAMPVerboseServerStatsServTmoStatus'
_k='adTWAMPVerboseServerStatsServTmoRemaining'
_j='adTWAMPVerboseServerStatsServTmo'
_i='adTWAMPVerboseServerStatsAuthMode'
_h='adTWAMPVerboseServerStatsTxTestPkts'
_g='adTWAMPVerboseServerStatsRxTestPkts'
_f='adTWAMPVerboseServerStatsState'
_e='adTWAMPClientTcpDestPort'
_d='adTWAMPReflectorStatsTestSessionsActive'
_c='adTWAMPReflectorStatsTestSessionsRejected'
_b='adTWAMPReflectorStatsTestSessionsClosed'
_a='adTWAMPReflectorStatsTestSessionsOpened'
_Z='adTWAMPReflectorStatsSessionsActive'
_Y='adTWAMPReflectorStatsSessionsRejected'
_X='adTWAMPReflectorStatsSessionsClosed'
_W='adTWAMPReflectorStatsSessionsOpened'
_V='adTWAMPReflectorStatsTxTestPkts'
_U='adTWAMPReflectorStatsRxTestPkts'
_T='adTWAMPReflectorCtrlTestTimeout'
_S='adTWAMPReflectorCtrlTimeout'
_R='adTWAMPReflectorCtrlEnable'
_Q='adTWAMPReflectorCtrlMaxSessions'
_P='adTWAMPReflectorCtrlTCPport'
_O='adTWAMPReflectorApplClearCounters'
_N='unknown'
_M='initialized'
_L='adTWAMPSenderUdpDestPort'
_K='adTWAMPSenderIpAddress'
_J='active'
_I='adTWAMPClientTcpSourcePort'
_H='adTWAMPClientIpAddress'
_G='not-accessible'
_F='octets'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='ADTRAN-TWAMP-REFLECTOR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adShared,=mibBuilder.importSymbols('ADTRAN-MIB','adShared')
adGenTWAMPReflector,adTWAMPReflectorID=mibBuilder.importSymbols('ADTRAN-SHARED-EOCU-MIB','adGenTWAMPReflector','adTWAMPReflectorID')
InterfaceIndex,OwnerString,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','OwnerString','ifIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
adtranTwampReflectorMib=ModuleIdentity((1,3,6,1,4,1,664,6,10000,69,5,1))
if mibBuilder.loadTexts:adtranTwampReflectorMib.setRevisions(('2008-01-29 00:00',))
_AdTWAMPReflectorObjects_ObjectIdentity=ObjectIdentity
adTWAMPReflectorObjects=_AdTWAMPReflectorObjects_ObjectIdentity((1,3,6,1,4,1,664,5,69,5,1))
_AdTWAMPReflectorAppl_ObjectIdentity=ObjectIdentity
adTWAMPReflectorAppl=_AdTWAMPReflectorAppl_ObjectIdentity((1,3,6,1,4,1,664,5,69,5,1,1))
class _AdTWAMPReflectorApplClearCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clearCounters',1))
_AdTWAMPReflectorApplClearCounters_Type.__name__=_D
_AdTWAMPReflectorApplClearCounters_Object=MibScalar
adTWAMPReflectorApplClearCounters=_AdTWAMPReflectorApplClearCounters_Object((1,3,6,1,4,1,664,5,69,5,1,1,1),_AdTWAMPReflectorApplClearCounters_Type())
adTWAMPReflectorApplClearCounters.setMaxAccess(_E)
if mibBuilder.loadTexts:adTWAMPReflectorApplClearCounters.setStatus(_A)
_AdTWAMPReflectorCtrl_ObjectIdentity=ObjectIdentity
adTWAMPReflectorCtrl=_AdTWAMPReflectorCtrl_ObjectIdentity((1,3,6,1,4,1,664,5,69,5,1,2))
class _AdTWAMPReflectorCtrlEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_AdTWAMPReflectorCtrlEnable_Type.__name__=_D
_AdTWAMPReflectorCtrlEnable_Object=MibScalar
adTWAMPReflectorCtrlEnable=_AdTWAMPReflectorCtrlEnable_Object((1,3,6,1,4,1,664,5,69,5,1,2,1),_AdTWAMPReflectorCtrlEnable_Type())
adTWAMPReflectorCtrlEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:adTWAMPReflectorCtrlEnable.setStatus(_A)
class _AdTWAMPReflectorCtrlTCPport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AdTWAMPReflectorCtrlTCPport_Type.__name__=_D
_AdTWAMPReflectorCtrlTCPport_Object=MibScalar
adTWAMPReflectorCtrlTCPport=_AdTWAMPReflectorCtrlTCPport_Object((1,3,6,1,4,1,664,5,69,5,1,2,2),_AdTWAMPReflectorCtrlTCPport_Type())
adTWAMPReflectorCtrlTCPport.setMaxAccess(_E)
if mibBuilder.loadTexts:adTWAMPReflectorCtrlTCPport.setStatus(_A)
if mibBuilder.loadTexts:adTWAMPReflectorCtrlTCPport.setUnits(_F)
class _AdTWAMPReflectorCtrlMaxSessions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_AdTWAMPReflectorCtrlMaxSessions_Type.__name__=_D
_AdTWAMPReflectorCtrlMaxSessions_Object=MibScalar
adTWAMPReflectorCtrlMaxSessions=_AdTWAMPReflectorCtrlMaxSessions_Object((1,3,6,1,4,1,664,5,69,5,1,2,3),_AdTWAMPReflectorCtrlMaxSessions_Type())
adTWAMPReflectorCtrlMaxSessions.setMaxAccess(_E)
if mibBuilder.loadTexts:adTWAMPReflectorCtrlMaxSessions.setStatus(_A)
if mibBuilder.loadTexts:adTWAMPReflectorCtrlMaxSessions.setUnits(_F)
class _AdTWAMPReflectorCtrlTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AdTWAMPReflectorCtrlTimeout_Type.__name__=_D
_AdTWAMPReflectorCtrlTimeout_Object=MibScalar
adTWAMPReflectorCtrlTimeout=_AdTWAMPReflectorCtrlTimeout_Object((1,3,6,1,4,1,664,5,69,5,1,2,4),_AdTWAMPReflectorCtrlTimeout_Type())
adTWAMPReflectorCtrlTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:adTWAMPReflectorCtrlTimeout.setStatus(_A)
if mibBuilder.loadTexts:adTWAMPReflectorCtrlTimeout.setUnits(_F)
class _AdTWAMPReflectorCtrlTestTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AdTWAMPReflectorCtrlTestTimeout_Type.__name__=_D
_AdTWAMPReflectorCtrlTestTimeout_Object=MibScalar
adTWAMPReflectorCtrlTestTimeout=_AdTWAMPReflectorCtrlTestTimeout_Object((1,3,6,1,4,1,664,5,69,5,1,2,5),_AdTWAMPReflectorCtrlTestTimeout_Type())
adTWAMPReflectorCtrlTestTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:adTWAMPReflectorCtrlTestTimeout.setStatus(_A)
if mibBuilder.loadTexts:adTWAMPReflectorCtrlTestTimeout.setUnits(_F)
_AdTWAMPReflectorTestUDPportRange_Type=OctetString
_AdTWAMPReflectorTestUDPportRange_Object=MibScalar
adTWAMPReflectorTestUDPportRange=_AdTWAMPReflectorTestUDPportRange_Object((1,3,6,1,4,1,664,5,69,5,1,2,6),_AdTWAMPReflectorTestUDPportRange_Type())
adTWAMPReflectorTestUDPportRange.setMaxAccess(_E)
if mibBuilder.loadTexts:adTWAMPReflectorTestUDPportRange.setStatus(_A)
_AdTWAMPReflectorStats_ObjectIdentity=ObjectIdentity
adTWAMPReflectorStats=_AdTWAMPReflectorStats_ObjectIdentity((1,3,6,1,4,1,664,5,69,5,1,3))
_AdTWAMPReflectorStatsRxTestPkts_Type=Gauge32
_AdTWAMPReflectorStatsRxTestPkts_Object=MibScalar
adTWAMPReflectorStatsRxTestPkts=_AdTWAMPReflectorStatsRxTestPkts_Object((1,3,6,1,4,1,664,5,69,5,1,3,1),_AdTWAMPReflectorStatsRxTestPkts_Type())
adTWAMPReflectorStatsRxTestPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPReflectorStatsRxTestPkts.setStatus(_A)
_AdTWAMPReflectorStatsTxTestPkts_Type=Gauge32
_AdTWAMPReflectorStatsTxTestPkts_Object=MibScalar
adTWAMPReflectorStatsTxTestPkts=_AdTWAMPReflectorStatsTxTestPkts_Object((1,3,6,1,4,1,664,5,69,5,1,3,2),_AdTWAMPReflectorStatsTxTestPkts_Type())
adTWAMPReflectorStatsTxTestPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPReflectorStatsTxTestPkts.setStatus(_A)
_AdTWAMPReflectorStatsSessionsOpened_Type=Gauge32
_AdTWAMPReflectorStatsSessionsOpened_Object=MibScalar
adTWAMPReflectorStatsSessionsOpened=_AdTWAMPReflectorStatsSessionsOpened_Object((1,3,6,1,4,1,664,5,69,5,1,3,3),_AdTWAMPReflectorStatsSessionsOpened_Type())
adTWAMPReflectorStatsSessionsOpened.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPReflectorStatsSessionsOpened.setStatus(_A)
_AdTWAMPReflectorStatsSessionsClosed_Type=Gauge32
_AdTWAMPReflectorStatsSessionsClosed_Object=MibScalar
adTWAMPReflectorStatsSessionsClosed=_AdTWAMPReflectorStatsSessionsClosed_Object((1,3,6,1,4,1,664,5,69,5,1,3,4),_AdTWAMPReflectorStatsSessionsClosed_Type())
adTWAMPReflectorStatsSessionsClosed.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPReflectorStatsSessionsClosed.setStatus(_A)
_AdTWAMPReflectorStatsSessionsRejected_Type=Gauge32
_AdTWAMPReflectorStatsSessionsRejected_Object=MibScalar
adTWAMPReflectorStatsSessionsRejected=_AdTWAMPReflectorStatsSessionsRejected_Object((1,3,6,1,4,1,664,5,69,5,1,3,5),_AdTWAMPReflectorStatsSessionsRejected_Type())
adTWAMPReflectorStatsSessionsRejected.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPReflectorStatsSessionsRejected.setStatus(_A)
_AdTWAMPReflectorStatsSessionsActive_Type=Gauge32
_AdTWAMPReflectorStatsSessionsActive_Object=MibScalar
adTWAMPReflectorStatsSessionsActive=_AdTWAMPReflectorStatsSessionsActive_Object((1,3,6,1,4,1,664,5,69,5,1,3,6),_AdTWAMPReflectorStatsSessionsActive_Type())
adTWAMPReflectorStatsSessionsActive.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPReflectorStatsSessionsActive.setStatus(_A)
_AdTWAMPReflectorStatsTestSessionsOpened_Type=Gauge32
_AdTWAMPReflectorStatsTestSessionsOpened_Object=MibScalar
adTWAMPReflectorStatsTestSessionsOpened=_AdTWAMPReflectorStatsTestSessionsOpened_Object((1,3,6,1,4,1,664,5,69,5,1,3,7),_AdTWAMPReflectorStatsTestSessionsOpened_Type())
adTWAMPReflectorStatsTestSessionsOpened.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPReflectorStatsTestSessionsOpened.setStatus(_A)
_AdTWAMPReflectorStatsTestSessionsClosed_Type=Gauge32
_AdTWAMPReflectorStatsTestSessionsClosed_Object=MibScalar
adTWAMPReflectorStatsTestSessionsClosed=_AdTWAMPReflectorStatsTestSessionsClosed_Object((1,3,6,1,4,1,664,5,69,5,1,3,8),_AdTWAMPReflectorStatsTestSessionsClosed_Type())
adTWAMPReflectorStatsTestSessionsClosed.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPReflectorStatsTestSessionsClosed.setStatus(_A)
_AdTWAMPReflectorStatsTestSessionsRejected_Type=Gauge32
_AdTWAMPReflectorStatsTestSessionsRejected_Object=MibScalar
adTWAMPReflectorStatsTestSessionsRejected=_AdTWAMPReflectorStatsTestSessionsRejected_Object((1,3,6,1,4,1,664,5,69,5,1,3,9),_AdTWAMPReflectorStatsTestSessionsRejected_Type())
adTWAMPReflectorStatsTestSessionsRejected.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPReflectorStatsTestSessionsRejected.setStatus(_A)
_AdTWAMPReflectorStatsTestSessionsActive_Type=Gauge32
_AdTWAMPReflectorStatsTestSessionsActive_Object=MibScalar
adTWAMPReflectorStatsTestSessionsActive=_AdTWAMPReflectorStatsTestSessionsActive_Object((1,3,6,1,4,1,664,5,69,5,1,3,10),_AdTWAMPReflectorStatsTestSessionsActive_Type())
adTWAMPReflectorStatsTestSessionsActive.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPReflectorStatsTestSessionsActive.setStatus(_A)
_AdTWAMPVerboseServerStatsTable_Object=MibTable
adTWAMPVerboseServerStatsTable=_AdTWAMPVerboseServerStatsTable_Object((1,3,6,1,4,1,664,5,69,5,1,3,11))
if mibBuilder.loadTexts:adTWAMPVerboseServerStatsTable.setStatus(_A)
_AdTWAMPVerboseServerStatsEntry_Object=MibTableRow
adTWAMPVerboseServerStatsEntry=_AdTWAMPVerboseServerStatsEntry_Object((1,3,6,1,4,1,664,5,69,5,1,3,11,1))
adTWAMPVerboseServerStatsEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:adTWAMPVerboseServerStatsEntry.setStatus(_A)
_AdTWAMPClientIpAddress_Type=IpAddress
_AdTWAMPClientIpAddress_Object=MibTableColumn
adTWAMPClientIpAddress=_AdTWAMPClientIpAddress_Object((1,3,6,1,4,1,664,5,69,5,1,3,11,1,1),_AdTWAMPClientIpAddress_Type())
adTWAMPClientIpAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:adTWAMPClientIpAddress.setStatus(_A)
_AdTWAMPClientTcpSourcePort_Type=Integer32
_AdTWAMPClientTcpSourcePort_Object=MibTableColumn
adTWAMPClientTcpSourcePort=_AdTWAMPClientTcpSourcePort_Object((1,3,6,1,4,1,664,5,69,5,1,3,11,1,2),_AdTWAMPClientTcpSourcePort_Type())
adTWAMPClientTcpSourcePort.setMaxAccess(_G)
if mibBuilder.loadTexts:adTWAMPClientTcpSourcePort.setStatus(_A)
_AdTWAMPClientTcpDestPort_Type=Integer32
_AdTWAMPClientTcpDestPort_Object=MibTableColumn
adTWAMPClientTcpDestPort=_AdTWAMPClientTcpDestPort_Object((1,3,6,1,4,1,664,5,69,5,1,3,11,1,3),_AdTWAMPClientTcpDestPort_Type())
adTWAMPClientTcpDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPClientTcpDestPort.setStatus(_A)
class _AdTWAMPVerboseServerStatsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_M,1),('opening',2),('setup',3),('starting',4),(_J,5),('registerSession',6),('acceptSession',7),('startSessions',8),('startAck',9),('stopSessions',10),('stopAck',11),('closed',12),('reserved',13),(_N,14)))
_AdTWAMPVerboseServerStatsState_Type.__name__=_D
_AdTWAMPVerboseServerStatsState_Object=MibTableColumn
adTWAMPVerboseServerStatsState=_AdTWAMPVerboseServerStatsState_Object((1,3,6,1,4,1,664,5,69,5,1,3,11,1,4),_AdTWAMPVerboseServerStatsState_Type())
adTWAMPVerboseServerStatsState.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPVerboseServerStatsState.setStatus(_A)
_AdTWAMPVerboseServerStatsRxTestPkts_Type=Integer32
_AdTWAMPVerboseServerStatsRxTestPkts_Object=MibTableColumn
adTWAMPVerboseServerStatsRxTestPkts=_AdTWAMPVerboseServerStatsRxTestPkts_Object((1,3,6,1,4,1,664,5,69,5,1,3,11,1,5),_AdTWAMPVerboseServerStatsRxTestPkts_Type())
adTWAMPVerboseServerStatsRxTestPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPVerboseServerStatsRxTestPkts.setStatus(_A)
_AdTWAMPVerboseServerStatsTxTestPkts_Type=Integer32
_AdTWAMPVerboseServerStatsTxTestPkts_Object=MibTableColumn
adTWAMPVerboseServerStatsTxTestPkts=_AdTWAMPVerboseServerStatsTxTestPkts_Object((1,3,6,1,4,1,664,5,69,5,1,3,11,1,6),_AdTWAMPVerboseServerStatsTxTestPkts_Type())
adTWAMPVerboseServerStatsTxTestPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPVerboseServerStatsTxTestPkts.setStatus(_A)
class _AdTWAMPVerboseServerStatsAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unauthenticated',1),('authenticated',2),('encrypted',3)))
_AdTWAMPVerboseServerStatsAuthMode_Type.__name__=_D
_AdTWAMPVerboseServerStatsAuthMode_Object=MibTableColumn
adTWAMPVerboseServerStatsAuthMode=_AdTWAMPVerboseServerStatsAuthMode_Object((1,3,6,1,4,1,664,5,69,5,1,3,11,1,7),_AdTWAMPVerboseServerStatsAuthMode_Type())
adTWAMPVerboseServerStatsAuthMode.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPVerboseServerStatsAuthMode.setStatus(_A)
_AdTWAMPVerboseServerStatsServTmo_Type=Integer32
_AdTWAMPVerboseServerStatsServTmo_Object=MibTableColumn
adTWAMPVerboseServerStatsServTmo=_AdTWAMPVerboseServerStatsServTmo_Object((1,3,6,1,4,1,664,5,69,5,1,3,11,1,8),_AdTWAMPVerboseServerStatsServTmo_Type())
adTWAMPVerboseServerStatsServTmo.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPVerboseServerStatsServTmo.setStatus(_A)
_AdTWAMPVerboseServerStatsServTmoRemaining_Type=Integer32
_AdTWAMPVerboseServerStatsServTmoRemaining_Object=MibTableColumn
adTWAMPVerboseServerStatsServTmoRemaining=_AdTWAMPVerboseServerStatsServTmoRemaining_Object((1,3,6,1,4,1,664,5,69,5,1,3,11,1,9),_AdTWAMPVerboseServerStatsServTmoRemaining_Type())
adTWAMPVerboseServerStatsServTmoRemaining.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPVerboseServerStatsServTmoRemaining.setStatus(_A)
class _AdTWAMPVerboseServerStatsServTmoStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('suspendedForActiveTestSession',2),('serverClosurePending',3)))
_AdTWAMPVerboseServerStatsServTmoStatus_Type.__name__=_D
_AdTWAMPVerboseServerStatsServTmoStatus_Object=MibTableColumn
adTWAMPVerboseServerStatsServTmoStatus=_AdTWAMPVerboseServerStatsServTmoStatus_Object((1,3,6,1,4,1,664,5,69,5,1,3,11,1,10),_AdTWAMPVerboseServerStatsServTmoStatus_Type())
adTWAMPVerboseServerStatsServTmoStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPVerboseServerStatsServTmoStatus.setStatus(_A)
_AdTWAMPVerboseReflectorStatsTable_Object=MibTable
adTWAMPVerboseReflectorStatsTable=_AdTWAMPVerboseReflectorStatsTable_Object((1,3,6,1,4,1,664,5,69,5,1,3,12))
if mibBuilder.loadTexts:adTWAMPVerboseReflectorStatsTable.setStatus(_A)
_AdTWAMPVerboseReflectorStatsEntry_Object=MibTableRow
adTWAMPVerboseReflectorStatsEntry=_AdTWAMPVerboseReflectorStatsEntry_Object((1,3,6,1,4,1,664,5,69,5,1,3,12,1))
adTWAMPVerboseReflectorStatsEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:adTWAMPVerboseReflectorStatsEntry.setStatus(_A)
_AdTWAMPSenderIpAddress_Type=IpAddress
_AdTWAMPSenderIpAddress_Object=MibTableColumn
adTWAMPSenderIpAddress=_AdTWAMPSenderIpAddress_Object((1,3,6,1,4,1,664,5,69,5,1,3,12,1,1),_AdTWAMPSenderIpAddress_Type())
adTWAMPSenderIpAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:adTWAMPSenderIpAddress.setStatus(_A)
_AdTWAMPSenderUdpDestPort_Type=Integer32
_AdTWAMPSenderUdpDestPort_Object=MibTableColumn
adTWAMPSenderUdpDestPort=_AdTWAMPSenderUdpDestPort_Object((1,3,6,1,4,1,664,5,69,5,1,3,12,1,2),_AdTWAMPSenderUdpDestPort_Type())
adTWAMPSenderUdpDestPort.setMaxAccess(_G)
if mibBuilder.loadTexts:adTWAMPSenderUdpDestPort.setStatus(_A)
_AdTWAMPSenderUdpSourcePort_Type=Integer32
_AdTWAMPSenderUdpSourcePort_Object=MibTableColumn
adTWAMPSenderUdpSourcePort=_AdTWAMPSenderUdpSourcePort_Object((1,3,6,1,4,1,664,5,69,5,1,3,12,1,3),_AdTWAMPSenderUdpSourcePort_Type())
adTWAMPSenderUdpSourcePort.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPSenderUdpSourcePort.setStatus(_A)
_AdTWAMPAssociatedClientIpAddress_Type=IpAddress
_AdTWAMPAssociatedClientIpAddress_Object=MibTableColumn
adTWAMPAssociatedClientIpAddress=_AdTWAMPAssociatedClientIpAddress_Object((1,3,6,1,4,1,664,5,69,5,1,3,12,1,4),_AdTWAMPAssociatedClientIpAddress_Type())
adTWAMPAssociatedClientIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPAssociatedClientIpAddress.setStatus(_A)
_AdTWAMPAssociatedClientTcpSourcePort_Type=Integer32
_AdTWAMPAssociatedClientTcpSourcePort_Object=MibTableColumn
adTWAMPAssociatedClientTcpSourcePort=_AdTWAMPAssociatedClientTcpSourcePort_Object((1,3,6,1,4,1,664,5,69,5,1,3,12,1,5),_AdTWAMPAssociatedClientTcpSourcePort_Type())
adTWAMPAssociatedClientTcpSourcePort.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPAssociatedClientTcpSourcePort.setStatus(_A)
class _AdTWAMPVerboseReflectorStatsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_M,1),('waitingToStart',2),('inProgress',3),('stopping',4),('stopped',5),('exception',6),(_N,7)))
_AdTWAMPVerboseReflectorStatsState_Type.__name__=_D
_AdTWAMPVerboseReflectorStatsState_Object=MibTableColumn
adTWAMPVerboseReflectorStatsState=_AdTWAMPVerboseReflectorStatsState_Object((1,3,6,1,4,1,664,5,69,5,1,3,12,1,6),_AdTWAMPVerboseReflectorStatsState_Type())
adTWAMPVerboseReflectorStatsState.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPVerboseReflectorStatsState.setStatus(_A)
_AdTWAMPVerboseReflectorStatsRxTestPkts_Type=Integer32
_AdTWAMPVerboseReflectorStatsRxTestPkts_Object=MibTableColumn
adTWAMPVerboseReflectorStatsRxTestPkts=_AdTWAMPVerboseReflectorStatsRxTestPkts_Object((1,3,6,1,4,1,664,5,69,5,1,3,12,1,7),_AdTWAMPVerboseReflectorStatsRxTestPkts_Type())
adTWAMPVerboseReflectorStatsRxTestPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPVerboseReflectorStatsRxTestPkts.setStatus(_A)
_AdTWAMPVerboseReflectorStatsTxTestPkts_Type=Integer32
_AdTWAMPVerboseReflectorStatsTxTestPkts_Object=MibTableColumn
adTWAMPVerboseReflectorStatsTxTestPkts=_AdTWAMPVerboseReflectorStatsTxTestPkts_Object((1,3,6,1,4,1,664,5,69,5,1,3,12,1,8),_AdTWAMPVerboseReflectorStatsTxTestPkts_Type())
adTWAMPVerboseReflectorStatsTxTestPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPVerboseReflectorStatsTxTestPkts.setStatus(_A)
_AdTWAMPVerboseReflectorStatsPaddingLength_Type=Integer32
_AdTWAMPVerboseReflectorStatsPaddingLength_Object=MibTableColumn
adTWAMPVerboseReflectorStatsPaddingLength=_AdTWAMPVerboseReflectorStatsPaddingLength_Object((1,3,6,1,4,1,664,5,69,5,1,3,12,1,9),_AdTWAMPVerboseReflectorStatsPaddingLength_Type())
adTWAMPVerboseReflectorStatsPaddingLength.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPVerboseReflectorStatsPaddingLength.setStatus(_A)
_AdTWAMPVerboseReflectorStatsTypePDescriptor_Type=Integer32
_AdTWAMPVerboseReflectorStatsTypePDescriptor_Object=MibTableColumn
adTWAMPVerboseReflectorStatsTypePDescriptor=_AdTWAMPVerboseReflectorStatsTypePDescriptor_Object((1,3,6,1,4,1,664,5,69,5,1,3,12,1,10),_AdTWAMPVerboseReflectorStatsTypePDescriptor_Type())
adTWAMPVerboseReflectorStatsTypePDescriptor.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPVerboseReflectorStatsTypePDescriptor.setStatus(_A)
_AdTWAMPVerboseReflectorStatsPacketTimeout_Type=Integer32
_AdTWAMPVerboseReflectorStatsPacketTimeout_Object=MibTableColumn
adTWAMPVerboseReflectorStatsPacketTimeout=_AdTWAMPVerboseReflectorStatsPacketTimeout_Object((1,3,6,1,4,1,664,5,69,5,1,3,12,1,11),_AdTWAMPVerboseReflectorStatsPacketTimeout_Type())
adTWAMPVerboseReflectorStatsPacketTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPVerboseReflectorStatsPacketTimeout.setStatus(_A)
_AdTWAMPVerboseReflectorStatsTestTmo_Type=Integer32
_AdTWAMPVerboseReflectorStatsTestTmo_Object=MibTableColumn
adTWAMPVerboseReflectorStatsTestTmo=_AdTWAMPVerboseReflectorStatsTestTmo_Object((1,3,6,1,4,1,664,5,69,5,1,3,12,1,12),_AdTWAMPVerboseReflectorStatsTestTmo_Type())
adTWAMPVerboseReflectorStatsTestTmo.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPVerboseReflectorStatsTestTmo.setStatus(_A)
_AdTWAMPVerboseReflectorStatsTestTmoRemaining_Type=Integer32
_AdTWAMPVerboseReflectorStatsTestTmoRemaining_Object=MibTableColumn
adTWAMPVerboseReflectorStatsTestTmoRemaining=_AdTWAMPVerboseReflectorStatsTestTmoRemaining_Object((1,3,6,1,4,1,664,5,69,5,1,3,12,1,13),_AdTWAMPVerboseReflectorStatsTestTmoRemaining_Type())
adTWAMPVerboseReflectorStatsTestTmoRemaining.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPVerboseReflectorStatsTestTmoRemaining.setStatus(_A)
class _AdTWAMPVerboseReflectorStatsTestTmoStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('waitingOnPacketTimeout',2)))
_AdTWAMPVerboseReflectorStatsTestTmoStatus_Type.__name__=_D
_AdTWAMPVerboseReflectorStatsTestTmoStatus_Object=MibTableColumn
adTWAMPVerboseReflectorStatsTestTmoStatus=_AdTWAMPVerboseReflectorStatsTestTmoStatus_Object((1,3,6,1,4,1,664,5,69,5,1,3,12,1,14),_AdTWAMPVerboseReflectorStatsTestTmoStatus_Type())
adTWAMPVerboseReflectorStatsTestTmoStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPVerboseReflectorStatsTestTmoStatus.setStatus(_A)
_AdTWAMPReflectorLookup_ObjectIdentity=ObjectIdentity
adTWAMPReflectorLookup=_AdTWAMPReflectorLookup_ObjectIdentity((1,3,6,1,4,1,664,5,69,5,1,4))
_AdTWAMPAssociationTable_Object=MibTable
adTWAMPAssociationTable=_AdTWAMPAssociationTable_Object((1,3,6,1,4,1,664,5,69,5,1,4,1))
if mibBuilder.loadTexts:adTWAMPAssociationTable.setStatus(_A)
_AdTWAMPAssociationEntry_Object=MibTableRow
adTWAMPAssociationEntry=_AdTWAMPAssociationEntry_Object((1,3,6,1,4,1,664,5,69,5,1,4,1,1))
adTWAMPAssociationEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:adTWAMPAssociationEntry.setStatus(_A)
_AdTWAMPNumOfSpawnedReflectors_Type=Integer32
_AdTWAMPNumOfSpawnedReflectors_Object=MibTableColumn
adTWAMPNumOfSpawnedReflectors=_AdTWAMPNumOfSpawnedReflectors_Object((1,3,6,1,4,1,664,5,69,5,1,4,1,1,1),_AdTWAMPNumOfSpawnedReflectors_Type())
adTWAMPNumOfSpawnedReflectors.setMaxAccess(_C)
if mibBuilder.loadTexts:adTWAMPNumOfSpawnedReflectors.setStatus(_A)
_AdTWAMPReflectorMibConformance_ObjectIdentity=ObjectIdentity
adTWAMPReflectorMibConformance=_AdTWAMPReflectorMibConformance_ObjectIdentity((1,3,6,1,4,1,664,5,69,5,2))
_AdTWAMPReflectorMibGroups_ObjectIdentity=ObjectIdentity
adTWAMPReflectorMibGroups=_AdTWAMPReflectorMibGroups_ObjectIdentity((1,3,6,1,4,1,664,5,69,5,2,1))
adTWAMPReflectorApplGroupRev1=ObjectGroup((1,3,6,1,4,1,664,5,69,5,2,1,1))
adTWAMPReflectorApplGroupRev1.setObjects((_B,_O))
if mibBuilder.loadTexts:adTWAMPReflectorApplGroupRev1.setStatus(_A)
adTWAMPReflectorCtrlGroupRev1=ObjectGroup((1,3,6,1,4,1,664,5,69,5,2,1,2))
adTWAMPReflectorCtrlGroupRev1.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:adTWAMPReflectorCtrlGroupRev1.setStatus(_A)
adTWAMPReflectorStatsGroupRev1=ObjectGroup((1,3,6,1,4,1,664,5,69,5,2,1,3))
adTWAMPReflectorStatsGroupRev1.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:adTWAMPReflectorStatsGroupRev1.setStatus(_A)
adTWAMPReflectorLookupGroupRev1=ObjectGroup((1,3,6,1,4,1,664,5,69,5,2,1,4))
adTWAMPReflectorLookupGroupRev1.setObjects((_B,_y))
if mibBuilder.loadTexts:adTWAMPReflectorLookupGroupRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'adTWAMPReflectorObjects':adTWAMPReflectorObjects,'adTWAMPReflectorAppl':adTWAMPReflectorAppl,_O:adTWAMPReflectorApplClearCounters,'adTWAMPReflectorCtrl':adTWAMPReflectorCtrl,_R:adTWAMPReflectorCtrlEnable,_P:adTWAMPReflectorCtrlTCPport,_Q:adTWAMPReflectorCtrlMaxSessions,_S:adTWAMPReflectorCtrlTimeout,_T:adTWAMPReflectorCtrlTestTimeout,'adTWAMPReflectorTestUDPportRange':adTWAMPReflectorTestUDPportRange,'adTWAMPReflectorStats':adTWAMPReflectorStats,_U:adTWAMPReflectorStatsRxTestPkts,_V:adTWAMPReflectorStatsTxTestPkts,_W:adTWAMPReflectorStatsSessionsOpened,_X:adTWAMPReflectorStatsSessionsClosed,_Y:adTWAMPReflectorStatsSessionsRejected,_Z:adTWAMPReflectorStatsSessionsActive,_a:adTWAMPReflectorStatsTestSessionsOpened,_b:adTWAMPReflectorStatsTestSessionsClosed,_c:adTWAMPReflectorStatsTestSessionsRejected,_d:adTWAMPReflectorStatsTestSessionsActive,'adTWAMPVerboseServerStatsTable':adTWAMPVerboseServerStatsTable,'adTWAMPVerboseServerStatsEntry':adTWAMPVerboseServerStatsEntry,_H:adTWAMPClientIpAddress,_I:adTWAMPClientTcpSourcePort,_e:adTWAMPClientTcpDestPort,_f:adTWAMPVerboseServerStatsState,_g:adTWAMPVerboseServerStatsRxTestPkts,_h:adTWAMPVerboseServerStatsTxTestPkts,_i:adTWAMPVerboseServerStatsAuthMode,_j:adTWAMPVerboseServerStatsServTmo,_k:adTWAMPVerboseServerStatsServTmoRemaining,_l:adTWAMPVerboseServerStatsServTmoStatus,'adTWAMPVerboseReflectorStatsTable':adTWAMPVerboseReflectorStatsTable,'adTWAMPVerboseReflectorStatsEntry':adTWAMPVerboseReflectorStatsEntry,_K:adTWAMPSenderIpAddress,_L:adTWAMPSenderUdpDestPort,_m:adTWAMPSenderUdpSourcePort,_n:adTWAMPAssociatedClientIpAddress,_o:adTWAMPAssociatedClientTcpSourcePort,_p:adTWAMPVerboseReflectorStatsState,_q:adTWAMPVerboseReflectorStatsRxTestPkts,_r:adTWAMPVerboseReflectorStatsTxTestPkts,_s:adTWAMPVerboseReflectorStatsPaddingLength,_t:adTWAMPVerboseReflectorStatsTypePDescriptor,_u:adTWAMPVerboseReflectorStatsPacketTimeout,_v:adTWAMPVerboseReflectorStatsTestTmo,_w:adTWAMPVerboseReflectorStatsTestTmoRemaining,_x:adTWAMPVerboseReflectorStatsTestTmoStatus,'adTWAMPReflectorLookup':adTWAMPReflectorLookup,'adTWAMPAssociationTable':adTWAMPAssociationTable,'adTWAMPAssociationEntry':adTWAMPAssociationEntry,_y:adTWAMPNumOfSpawnedReflectors,'adTWAMPReflectorMibConformance':adTWAMPReflectorMibConformance,'adTWAMPReflectorMibGroups':adTWAMPReflectorMibGroups,'adTWAMPReflectorApplGroupRev1':adTWAMPReflectorApplGroupRev1,'adTWAMPReflectorCtrlGroupRev1':adTWAMPReflectorCtrlGroupRev1,'adTWAMPReflectorStatsGroupRev1':adTWAMPReflectorStatsGroupRev1,'adTWAMPReflectorLookupGroupRev1':adTWAMPReflectorLookupGroupRev1,'adtranTwampReflectorMib':adtranTwampReflectorMib})