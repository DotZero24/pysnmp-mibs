_Ac='tmnxTwampSrvV9v0Group'
_Ab='tmnxTwampSrvV14v0Group'
_Aa='tmnxTwampSrvNotifyObjsV9v0Group'
_AZ='tmnxTwampRflInactivityV19v0Group'
_AY='tmnxTwampRflInNotifyObjsV19v0Grp'
_AX='tmnxTwampSrvNotifyV9v0Group'
_AW='tmnxTwampRflInactNotifV19v0Group'
_AV='tmnxTwampRflInactivityTimeout'
_AU='tmnxTwampSrvPfxMaxSessExceeded'
_AT='tmnxTwampSrvMaxSessExceeded'
_AS='tmnxTwampSrvPfxMaxConnsExceeded'
_AR='tmnxTwampSrvMaxConnsExceeded'
_AQ='tmnxTwampSrvInactivityTimeout'
_AP='tmnxTwampRflInactTimeout'
_AO='tmnxTwampSrvSessSenderUdpPort'
_AN='tmnxTwampSrvSessSenderAddress'
_AM='tmnxTwampSrvSessSenderAddrType'
_AL='tmnxTwampSrvSessReflectorUdpPort'
_AK='tmnxTwampSrvSessReflectorAddress'
_AJ='tmnxTwampSrvSessReflectorAddrTyp'
_AI='tmnxTwampSrvSessOperState'
_AH='tmnxTwampSrvSessID'
_AG='tmnxTwampSrvCapabilities'
_AF='tmnxTwampSrvConnTestPacketsTx'
_AE='tmnxTwampSrvConnTestPacketsRx'
_AD='tmnxTwampSrvConnTestSessRejected'
_AC='tmnxTwampSrvConnTestSessComplete'
_AB='tmnxTwampSrvConnSessionCount'
_AA='tmnxTwampSrvConnState'
_A9='tmnxTwampSrvPfxTestPacketsTx'
_A8='tmnxTwampSrvPfxTestPacketsRx'
_A7='tmnxTwampSrvPfxTestSessAbort'
_A6='tmnxTwampSrvPfxTestSessRejected'
_A5='tmnxTwampSrvPfxTestSessCompleted'
_A4='tmnxTwampSrvPfxConnsRejected'
_A3='tmnxTwampSrvTestPacketsTx'
_A2='tmnxTwampSrvTestPacketsRx'
_A1='tmnxTwampSrvTestSessAborted'
_A0='tmnxTwampSrvTestSessRejected'
_z='tmnxTwampSrvTestSessCompleted'
_y='tmnxTwampSrvConnectionsRejected'
_x='tmnxTwampSrvUpTime'
_w='tmnxTwampSrvOperState'
_v='tmnxTwampSrvPrefixMaxSessions'
_u='tmnxTwampSrvPrefixMaxConnections'
_t='tmnxTwampSrvPrefixDescription'
_s='tmnxTwampSrvPrefixLastChg'
_r='tmnxTwampSrvPrefixRowStatus'
_q='tmnxTwampSrvPrefixTblLastChg'
_p='tmnxTwampSrvMaxSessions'
_o='tmnxTwampSrvMaxConnections'
_n='tmnxTwampSrvInactTimeout'
_m='tmnxTwampSrvAdminState'
_l='tmnxTwampSrvPrefixStatsEntry'
_k='tmnxTwampSrvSessSeqNum'
_j='TmnxAdminState'
_i='TItemDescription'
_h='InetAddressPrefixLength'
_g='OctetString'
_f='tmnxTwampRflNotifRemoteUdpPort'
_e='tmnxTwampRflNotifRemoteAddrType'
_d='tmnxTwampRflNotifRemoteAddr'
_c='tmnxTwampRflNotifLocalUdpPort'
_b='tmnxTwampRflNotifLocalAddrType'
_a='tmnxTwampRflNotifLocalAddr'
_Z='tmnxTwampSrvConnIdleTime'
_Y='tmnxTwampSrvPfxSessionCount'
_X='tmnxTwampSrvPfxConnCount'
_W='tmnxTwampSrvSessionCount'
_V='tmnxTwampSrvConnectionCount'
_U='tmnxTwampSrvConnSeqNum'
_T='tmnxTwampSrvConnClientAddr'
_S='tmnxTwampSrvConnClientAddrType'
_R='tmnxTwampSrvPrefixLen'
_Q='tmnxTwampSrvPrefixAddr'
_P='tmnxTwampSrvPrefixAddrType'
_O='TmnxTwampSrvSessionCount'
_N='TmnxTwampSrvConnectionCount'
_M='Integer32'
_L='read-create'
_K='seconds'
_J='read-write'
_I='Unsigned32'
_H='tmnxTwampSrvNotifClientAddr'
_G='tmnxTwampSrvNotifClientAddrType'
_F='not-accessible'
_E='accessible-for-notify'
_D='InetAddress'
_C='read-only'
_B='current'
_A='TIMETRA-TWAMP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_g,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressPrefixLength,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_D,_h,'InetAddressType','InetPortNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
TItemDescription,TTcpUdpPort,TmnxAdminState,TmnxOperState=mibBuilder.importSymbols('TIMETRA-TC-MIB',_i,'TTcpUdpPort',_j,'TmnxOperState')
timetraTwampMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,76))
if mibBuilder.loadTexts:timetraTwampMIBModule.setRevisions(('2016-01-01 00:00','2011-02-01 00:00'))
class TmnxTwampSrvConnectionCount(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
class TmnxTwampSrvSessionCount(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_TmnxTwampConformance_ObjectIdentity=ObjectIdentity
tmnxTwampConformance=_TmnxTwampConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,76))
_TmnxTwampComplianceObjs_ObjectIdentity=ObjectIdentity
tmnxTwampComplianceObjs=_TmnxTwampComplianceObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,76,1))
_TmnxTwampGroupObjs_ObjectIdentity=ObjectIdentity
tmnxTwampGroupObjs=_TmnxTwampGroupObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,76,2))
_TmnxTwampV9v0GroupObjs_ObjectIdentity=ObjectIdentity
tmnxTwampV9v0GroupObjs=_TmnxTwampV9v0GroupObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,76,2,1))
_TmnxTwampV14v0GroupObjs_ObjectIdentity=ObjectIdentity
tmnxTwampV14v0GroupObjs=_TmnxTwampV14v0GroupObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,76,2,2))
_TmnxTwampV19v0GroupObjs_ObjectIdentity=ObjectIdentity
tmnxTwampV19v0GroupObjs=_TmnxTwampV19v0GroupObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,76,2,3))
_TmnxTwampObjs_ObjectIdentity=ObjectIdentity
tmnxTwampObjs=_TmnxTwampObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,76))
_TmnxTwampTableLastChangeObjs_ObjectIdentity=ObjectIdentity
tmnxTwampTableLastChangeObjs=_TmnxTwampTableLastChangeObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,76,1))
_TmnxTwampSrvPrefixTblLastChg_Type=TimeStamp
_TmnxTwampSrvPrefixTblLastChg_Object=MibScalar
tmnxTwampSrvPrefixTblLastChg=_TmnxTwampSrvPrefixTblLastChg_Object((1,3,6,1,4,1,6527,3,1,2,76,1,1),_TmnxTwampSrvPrefixTblLastChg_Type())
tmnxTwampSrvPrefixTblLastChg.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvPrefixTblLastChg.setStatus(_B)
_TmnxTwampConfigObjs_ObjectIdentity=ObjectIdentity
tmnxTwampConfigObjs=_TmnxTwampConfigObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,76,2))
_TmnxTwampConfigScalarObjs_ObjectIdentity=ObjectIdentity
tmnxTwampConfigScalarObjs=_TmnxTwampConfigScalarObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,76,2,1))
class _TmnxTwampSrvAdminState_Type(TmnxAdminState):defaultValue=3
_TmnxTwampSrvAdminState_Type.__name__=_j
_TmnxTwampSrvAdminState_Object=MibScalar
tmnxTwampSrvAdminState=_TmnxTwampSrvAdminState_Object((1,3,6,1,4,1,6527,3,1,2,76,2,1,1),_TmnxTwampSrvAdminState_Type())
tmnxTwampSrvAdminState.setMaxAccess(_J)
if mibBuilder.loadTexts:tmnxTwampSrvAdminState.setStatus(_B)
class _TmnxTwampSrvInactTimeout_Type(Unsigned32):defaultValue=900;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,3600))
_TmnxTwampSrvInactTimeout_Type.__name__=_I
_TmnxTwampSrvInactTimeout_Object=MibScalar
tmnxTwampSrvInactTimeout=_TmnxTwampSrvInactTimeout_Object((1,3,6,1,4,1,6527,3,1,2,76,2,1,2),_TmnxTwampSrvInactTimeout_Type())
tmnxTwampSrvInactTimeout.setMaxAccess(_J)
if mibBuilder.loadTexts:tmnxTwampSrvInactTimeout.setStatus(_B)
if mibBuilder.loadTexts:tmnxTwampSrvInactTimeout.setUnits(_K)
class _TmnxTwampSrvMaxConnections_Type(TmnxTwampSrvConnectionCount):defaultValue=32
_TmnxTwampSrvMaxConnections_Type.__name__=_N
_TmnxTwampSrvMaxConnections_Object=MibScalar
tmnxTwampSrvMaxConnections=_TmnxTwampSrvMaxConnections_Object((1,3,6,1,4,1,6527,3,1,2,76,2,1,3),_TmnxTwampSrvMaxConnections_Type())
tmnxTwampSrvMaxConnections.setMaxAccess(_J)
if mibBuilder.loadTexts:tmnxTwampSrvMaxConnections.setStatus(_B)
class _TmnxTwampSrvMaxSessions_Type(TmnxTwampSrvSessionCount):defaultValue=32
_TmnxTwampSrvMaxSessions_Type.__name__=_O
_TmnxTwampSrvMaxSessions_Object=MibScalar
tmnxTwampSrvMaxSessions=_TmnxTwampSrvMaxSessions_Object((1,3,6,1,4,1,6527,3,1,2,76,2,1,4),_TmnxTwampSrvMaxSessions_Type())
tmnxTwampSrvMaxSessions.setMaxAccess(_J)
if mibBuilder.loadTexts:tmnxTwampSrvMaxSessions.setStatus(_B)
class _TmnxTwampRflInactTimeout_Type(Unsigned32):defaultValue=900;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,3600))
_TmnxTwampRflInactTimeout_Type.__name__=_I
_TmnxTwampRflInactTimeout_Object=MibScalar
tmnxTwampRflInactTimeout=_TmnxTwampRflInactTimeout_Object((1,3,6,1,4,1,6527,3,1,2,76,2,1,5),_TmnxTwampRflInactTimeout_Type())
tmnxTwampRflInactTimeout.setMaxAccess(_J)
if mibBuilder.loadTexts:tmnxTwampRflInactTimeout.setStatus(_B)
if mibBuilder.loadTexts:tmnxTwampRflInactTimeout.setUnits(_K)
_TmnxTwampConfigTableObjs_ObjectIdentity=ObjectIdentity
tmnxTwampConfigTableObjs=_TmnxTwampConfigTableObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,76,2,2))
_TmnxTwampSrvPrefixTable_Object=MibTable
tmnxTwampSrvPrefixTable=_TmnxTwampSrvPrefixTable_Object((1,3,6,1,4,1,6527,3,1,2,76,2,2,1))
if mibBuilder.loadTexts:tmnxTwampSrvPrefixTable.setStatus(_B)
_TmnxTwampSrvPrefixEntry_Object=MibTableRow
tmnxTwampSrvPrefixEntry=_TmnxTwampSrvPrefixEntry_Object((1,3,6,1,4,1,6527,3,1,2,76,2,2,1,1))
tmnxTwampSrvPrefixEntry.setIndexNames((0,_A,_P),(0,_A,_Q),(0,_A,_R))
if mibBuilder.loadTexts:tmnxTwampSrvPrefixEntry.setStatus(_B)
_TmnxTwampSrvPrefixAddrType_Type=InetAddressType
_TmnxTwampSrvPrefixAddrType_Object=MibTableColumn
tmnxTwampSrvPrefixAddrType=_TmnxTwampSrvPrefixAddrType_Object((1,3,6,1,4,1,6527,3,1,2,76,2,2,1,1,1),_TmnxTwampSrvPrefixAddrType_Type())
tmnxTwampSrvPrefixAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxTwampSrvPrefixAddrType.setStatus(_B)
class _TmnxTwampSrvPrefixAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TmnxTwampSrvPrefixAddr_Type.__name__=_D
_TmnxTwampSrvPrefixAddr_Object=MibTableColumn
tmnxTwampSrvPrefixAddr=_TmnxTwampSrvPrefixAddr_Object((1,3,6,1,4,1,6527,3,1,2,76,2,2,1,1,2),_TmnxTwampSrvPrefixAddr_Type())
tmnxTwampSrvPrefixAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxTwampSrvPrefixAddr.setStatus(_B)
class _TmnxTwampSrvPrefixLen_Type(InetAddressPrefixLength):subtypeSpec=InetAddressPrefixLength.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_TmnxTwampSrvPrefixLen_Type.__name__=_h
_TmnxTwampSrvPrefixLen_Object=MibTableColumn
tmnxTwampSrvPrefixLen=_TmnxTwampSrvPrefixLen_Object((1,3,6,1,4,1,6527,3,1,2,76,2,2,1,1,3),_TmnxTwampSrvPrefixLen_Type())
tmnxTwampSrvPrefixLen.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxTwampSrvPrefixLen.setStatus(_B)
if mibBuilder.loadTexts:tmnxTwampSrvPrefixLen.setUnits('bits')
_TmnxTwampSrvPrefixRowStatus_Type=RowStatus
_TmnxTwampSrvPrefixRowStatus_Object=MibTableColumn
tmnxTwampSrvPrefixRowStatus=_TmnxTwampSrvPrefixRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,76,2,2,1,1,4),_TmnxTwampSrvPrefixRowStatus_Type())
tmnxTwampSrvPrefixRowStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:tmnxTwampSrvPrefixRowStatus.setStatus(_B)
_TmnxTwampSrvPrefixLastChg_Type=TimeStamp
_TmnxTwampSrvPrefixLastChg_Object=MibTableColumn
tmnxTwampSrvPrefixLastChg=_TmnxTwampSrvPrefixLastChg_Object((1,3,6,1,4,1,6527,3,1,2,76,2,2,1,1,5),_TmnxTwampSrvPrefixLastChg_Type())
tmnxTwampSrvPrefixLastChg.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvPrefixLastChg.setStatus(_B)
class _TmnxTwampSrvPrefixDescription_Type(TItemDescription):defaultHexValue=''
_TmnxTwampSrvPrefixDescription_Type.__name__=_i
_TmnxTwampSrvPrefixDescription_Object=MibTableColumn
tmnxTwampSrvPrefixDescription=_TmnxTwampSrvPrefixDescription_Object((1,3,6,1,4,1,6527,3,1,2,76,2,2,1,1,6),_TmnxTwampSrvPrefixDescription_Type())
tmnxTwampSrvPrefixDescription.setMaxAccess(_L)
if mibBuilder.loadTexts:tmnxTwampSrvPrefixDescription.setStatus(_B)
class _TmnxTwampSrvPrefixMaxConnections_Type(TmnxTwampSrvConnectionCount):defaultValue=32
_TmnxTwampSrvPrefixMaxConnections_Type.__name__=_N
_TmnxTwampSrvPrefixMaxConnections_Object=MibTableColumn
tmnxTwampSrvPrefixMaxConnections=_TmnxTwampSrvPrefixMaxConnections_Object((1,3,6,1,4,1,6527,3,1,2,76,2,2,1,1,7),_TmnxTwampSrvPrefixMaxConnections_Type())
tmnxTwampSrvPrefixMaxConnections.setMaxAccess(_L)
if mibBuilder.loadTexts:tmnxTwampSrvPrefixMaxConnections.setStatus(_B)
class _TmnxTwampSrvPrefixMaxSessions_Type(TmnxTwampSrvSessionCount):defaultValue=32
_TmnxTwampSrvPrefixMaxSessions_Type.__name__=_O
_TmnxTwampSrvPrefixMaxSessions_Object=MibTableColumn
tmnxTwampSrvPrefixMaxSessions=_TmnxTwampSrvPrefixMaxSessions_Object((1,3,6,1,4,1,6527,3,1,2,76,2,2,1,1,8),_TmnxTwampSrvPrefixMaxSessions_Type())
tmnxTwampSrvPrefixMaxSessions.setMaxAccess(_L)
if mibBuilder.loadTexts:tmnxTwampSrvPrefixMaxSessions.setStatus(_B)
_TmnxTwampStatisticsObjs_ObjectIdentity=ObjectIdentity
tmnxTwampStatisticsObjs=_TmnxTwampStatisticsObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,76,3))
_TmnxTwampStatisticsScalarObjs_ObjectIdentity=ObjectIdentity
tmnxTwampStatisticsScalarObjs=_TmnxTwampStatisticsScalarObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,76,3,1))
_TmnxTwampSrvOperState_Type=TmnxOperState
_TmnxTwampSrvOperState_Object=MibScalar
tmnxTwampSrvOperState=_TmnxTwampSrvOperState_Object((1,3,6,1,4,1,6527,3,1,2,76,3,1,1),_TmnxTwampSrvOperState_Type())
tmnxTwampSrvOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvOperState.setStatus(_B)
_TmnxTwampSrvUpTime_Type=Counter32
_TmnxTwampSrvUpTime_Object=MibScalar
tmnxTwampSrvUpTime=_TmnxTwampSrvUpTime_Object((1,3,6,1,4,1,6527,3,1,2,76,3,1,2),_TmnxTwampSrvUpTime_Type())
tmnxTwampSrvUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvUpTime.setStatus(_B)
if mibBuilder.loadTexts:tmnxTwampSrvUpTime.setUnits(_K)
_TmnxTwampSrvConnectionCount_Type=TmnxTwampSrvConnectionCount
_TmnxTwampSrvConnectionCount_Object=MibScalar
tmnxTwampSrvConnectionCount=_TmnxTwampSrvConnectionCount_Object((1,3,6,1,4,1,6527,3,1,2,76,3,1,3),_TmnxTwampSrvConnectionCount_Type())
tmnxTwampSrvConnectionCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvConnectionCount.setStatus(_B)
_TmnxTwampSrvConnectionsRejected_Type=Counter32
_TmnxTwampSrvConnectionsRejected_Object=MibScalar
tmnxTwampSrvConnectionsRejected=_TmnxTwampSrvConnectionsRejected_Object((1,3,6,1,4,1,6527,3,1,2,76,3,1,4),_TmnxTwampSrvConnectionsRejected_Type())
tmnxTwampSrvConnectionsRejected.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvConnectionsRejected.setStatus(_B)
_TmnxTwampSrvSessionCount_Type=TmnxTwampSrvSessionCount
_TmnxTwampSrvSessionCount_Object=MibScalar
tmnxTwampSrvSessionCount=_TmnxTwampSrvSessionCount_Object((1,3,6,1,4,1,6527,3,1,2,76,3,1,5),_TmnxTwampSrvSessionCount_Type())
tmnxTwampSrvSessionCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvSessionCount.setStatus(_B)
_TmnxTwampSrvTestSessCompleted_Type=Counter32
_TmnxTwampSrvTestSessCompleted_Object=MibScalar
tmnxTwampSrvTestSessCompleted=_TmnxTwampSrvTestSessCompleted_Object((1,3,6,1,4,1,6527,3,1,2,76,3,1,6),_TmnxTwampSrvTestSessCompleted_Type())
tmnxTwampSrvTestSessCompleted.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvTestSessCompleted.setStatus(_B)
_TmnxTwampSrvTestSessRejected_Type=Counter32
_TmnxTwampSrvTestSessRejected_Object=MibScalar
tmnxTwampSrvTestSessRejected=_TmnxTwampSrvTestSessRejected_Object((1,3,6,1,4,1,6527,3,1,2,76,3,1,7),_TmnxTwampSrvTestSessRejected_Type())
tmnxTwampSrvTestSessRejected.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvTestSessRejected.setStatus(_B)
_TmnxTwampSrvTestSessAborted_Type=Counter32
_TmnxTwampSrvTestSessAborted_Object=MibScalar
tmnxTwampSrvTestSessAborted=_TmnxTwampSrvTestSessAborted_Object((1,3,6,1,4,1,6527,3,1,2,76,3,1,8),_TmnxTwampSrvTestSessAborted_Type())
tmnxTwampSrvTestSessAborted.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvTestSessAborted.setStatus(_B)
_TmnxTwampSrvTestPacketsRx_Type=Counter32
_TmnxTwampSrvTestPacketsRx_Object=MibScalar
tmnxTwampSrvTestPacketsRx=_TmnxTwampSrvTestPacketsRx_Object((1,3,6,1,4,1,6527,3,1,2,76,3,1,9),_TmnxTwampSrvTestPacketsRx_Type())
tmnxTwampSrvTestPacketsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvTestPacketsRx.setStatus(_B)
_TmnxTwampSrvTestPacketsTx_Type=Counter32
_TmnxTwampSrvTestPacketsTx_Object=MibScalar
tmnxTwampSrvTestPacketsTx=_TmnxTwampSrvTestPacketsTx_Object((1,3,6,1,4,1,6527,3,1,2,76,3,1,10),_TmnxTwampSrvTestPacketsTx_Type())
tmnxTwampSrvTestPacketsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvTestPacketsTx.setStatus(_B)
class _TmnxTwampSrvCapabilities_Type(Bits):namedValues=NamedValues(*(('unauthenticated',0),('authenticated',1),('encrypted',2),('unauthTestEncryptControl',3),('individualSessionControl',4),('reflectOctets',5),('symmetricalSizeSenderTestPkt',6),('ikeV2DerivedMode',7),('dscpAndEcnMonitoring',8)))
_TmnxTwampSrvCapabilities_Type.__name__='Bits'
_TmnxTwampSrvCapabilities_Object=MibScalar
tmnxTwampSrvCapabilities=_TmnxTwampSrvCapabilities_Object((1,3,6,1,4,1,6527,3,1,2,76,3,1,11),_TmnxTwampSrvCapabilities_Type())
tmnxTwampSrvCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvCapabilities.setStatus(_B)
_TmnxTwampStatisticsTableObjs_ObjectIdentity=ObjectIdentity
tmnxTwampStatisticsTableObjs=_TmnxTwampStatisticsTableObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,76,3,2))
_TmnxTwampSrvPrefixStatsTable_Object=MibTable
tmnxTwampSrvPrefixStatsTable=_TmnxTwampSrvPrefixStatsTable_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,1))
if mibBuilder.loadTexts:tmnxTwampSrvPrefixStatsTable.setStatus(_B)
_TmnxTwampSrvPrefixStatsEntry_Object=MibTableRow
tmnxTwampSrvPrefixStatsEntry=_TmnxTwampSrvPrefixStatsEntry_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,1,1))
if mibBuilder.loadTexts:tmnxTwampSrvPrefixStatsEntry.setStatus(_B)
_TmnxTwampSrvPfxConnCount_Type=TmnxTwampSrvConnectionCount
_TmnxTwampSrvPfxConnCount_Object=MibTableColumn
tmnxTwampSrvPfxConnCount=_TmnxTwampSrvPfxConnCount_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,1,1,1),_TmnxTwampSrvPfxConnCount_Type())
tmnxTwampSrvPfxConnCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvPfxConnCount.setStatus(_B)
_TmnxTwampSrvPfxConnsRejected_Type=Counter32
_TmnxTwampSrvPfxConnsRejected_Object=MibTableColumn
tmnxTwampSrvPfxConnsRejected=_TmnxTwampSrvPfxConnsRejected_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,1,1,2),_TmnxTwampSrvPfxConnsRejected_Type())
tmnxTwampSrvPfxConnsRejected.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvPfxConnsRejected.setStatus(_B)
_TmnxTwampSrvPfxSessionCount_Type=TmnxTwampSrvSessionCount
_TmnxTwampSrvPfxSessionCount_Object=MibTableColumn
tmnxTwampSrvPfxSessionCount=_TmnxTwampSrvPfxSessionCount_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,1,1,3),_TmnxTwampSrvPfxSessionCount_Type())
tmnxTwampSrvPfxSessionCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvPfxSessionCount.setStatus(_B)
_TmnxTwampSrvPfxTestSessCompleted_Type=Counter32
_TmnxTwampSrvPfxTestSessCompleted_Object=MibTableColumn
tmnxTwampSrvPfxTestSessCompleted=_TmnxTwampSrvPfxTestSessCompleted_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,1,1,4),_TmnxTwampSrvPfxTestSessCompleted_Type())
tmnxTwampSrvPfxTestSessCompleted.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvPfxTestSessCompleted.setStatus(_B)
_TmnxTwampSrvPfxTestSessRejected_Type=Counter32
_TmnxTwampSrvPfxTestSessRejected_Object=MibTableColumn
tmnxTwampSrvPfxTestSessRejected=_TmnxTwampSrvPfxTestSessRejected_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,1,1,5),_TmnxTwampSrvPfxTestSessRejected_Type())
tmnxTwampSrvPfxTestSessRejected.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvPfxTestSessRejected.setStatus(_B)
_TmnxTwampSrvPfxTestSessAbort_Type=Counter32
_TmnxTwampSrvPfxTestSessAbort_Object=MibTableColumn
tmnxTwampSrvPfxTestSessAbort=_TmnxTwampSrvPfxTestSessAbort_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,1,1,6),_TmnxTwampSrvPfxTestSessAbort_Type())
tmnxTwampSrvPfxTestSessAbort.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvPfxTestSessAbort.setStatus(_B)
_TmnxTwampSrvPfxTestPacketsRx_Type=Counter32
_TmnxTwampSrvPfxTestPacketsRx_Object=MibTableColumn
tmnxTwampSrvPfxTestPacketsRx=_TmnxTwampSrvPfxTestPacketsRx_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,1,1,7),_TmnxTwampSrvPfxTestPacketsRx_Type())
tmnxTwampSrvPfxTestPacketsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvPfxTestPacketsRx.setStatus(_B)
_TmnxTwampSrvPfxTestPacketsTx_Type=Counter32
_TmnxTwampSrvPfxTestPacketsTx_Object=MibTableColumn
tmnxTwampSrvPfxTestPacketsTx=_TmnxTwampSrvPfxTestPacketsTx_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,1,1,8),_TmnxTwampSrvPfxTestPacketsTx_Type())
tmnxTwampSrvPfxTestPacketsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvPfxTestPacketsTx.setStatus(_B)
_TmnxTwampSrvConnStatsTable_Object=MibTable
tmnxTwampSrvConnStatsTable=_TmnxTwampSrvConnStatsTable_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,2))
if mibBuilder.loadTexts:tmnxTwampSrvConnStatsTable.setStatus(_B)
_TmnxTwampSrvConnStatsEntry_Object=MibTableRow
tmnxTwampSrvConnStatsEntry=_TmnxTwampSrvConnStatsEntry_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,2,1))
tmnxTwampSrvConnStatsEntry.setIndexNames((0,_A,_P),(0,_A,_Q),(0,_A,_R),(0,_A,_S),(0,_A,_T),(0,_A,_U))
if mibBuilder.loadTexts:tmnxTwampSrvConnStatsEntry.setStatus(_B)
_TmnxTwampSrvConnClientAddrType_Type=InetAddressType
_TmnxTwampSrvConnClientAddrType_Object=MibTableColumn
tmnxTwampSrvConnClientAddrType=_TmnxTwampSrvConnClientAddrType_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,2,1,1),_TmnxTwampSrvConnClientAddrType_Type())
tmnxTwampSrvConnClientAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxTwampSrvConnClientAddrType.setStatus(_B)
class _TmnxTwampSrvConnClientAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TmnxTwampSrvConnClientAddr_Type.__name__=_D
_TmnxTwampSrvConnClientAddr_Object=MibTableColumn
tmnxTwampSrvConnClientAddr=_TmnxTwampSrvConnClientAddr_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,2,1,2),_TmnxTwampSrvConnClientAddr_Type())
tmnxTwampSrvConnClientAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxTwampSrvConnClientAddr.setStatus(_B)
class _TmnxTwampSrvConnSeqNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TmnxTwampSrvConnSeqNum_Type.__name__=_I
_TmnxTwampSrvConnSeqNum_Object=MibTableColumn
tmnxTwampSrvConnSeqNum=_TmnxTwampSrvConnSeqNum_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,2,1,3),_TmnxTwampSrvConnSeqNum_Type())
tmnxTwampSrvConnSeqNum.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxTwampSrvConnSeqNum.setStatus(_B)
class _TmnxTwampSrvConnState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('settingUp',1),('ready',2),('running',3)))
_TmnxTwampSrvConnState_Type.__name__=_M
_TmnxTwampSrvConnState_Object=MibTableColumn
tmnxTwampSrvConnState=_TmnxTwampSrvConnState_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,2,1,4),_TmnxTwampSrvConnState_Type())
tmnxTwampSrvConnState.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvConnState.setStatus(_B)
_TmnxTwampSrvConnIdleTime_Type=Unsigned32
_TmnxTwampSrvConnIdleTime_Object=MibTableColumn
tmnxTwampSrvConnIdleTime=_TmnxTwampSrvConnIdleTime_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,2,1,5),_TmnxTwampSrvConnIdleTime_Type())
tmnxTwampSrvConnIdleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvConnIdleTime.setStatus(_B)
if mibBuilder.loadTexts:tmnxTwampSrvConnIdleTime.setUnits(_K)
_TmnxTwampSrvConnSessionCount_Type=TmnxTwampSrvSessionCount
_TmnxTwampSrvConnSessionCount_Object=MibTableColumn
tmnxTwampSrvConnSessionCount=_TmnxTwampSrvConnSessionCount_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,2,1,6),_TmnxTwampSrvConnSessionCount_Type())
tmnxTwampSrvConnSessionCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvConnSessionCount.setStatus(_B)
_TmnxTwampSrvConnTestSessComplete_Type=Counter32
_TmnxTwampSrvConnTestSessComplete_Object=MibTableColumn
tmnxTwampSrvConnTestSessComplete=_TmnxTwampSrvConnTestSessComplete_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,2,1,7),_TmnxTwampSrvConnTestSessComplete_Type())
tmnxTwampSrvConnTestSessComplete.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvConnTestSessComplete.setStatus(_B)
_TmnxTwampSrvConnTestSessRejected_Type=Counter32
_TmnxTwampSrvConnTestSessRejected_Object=MibTableColumn
tmnxTwampSrvConnTestSessRejected=_TmnxTwampSrvConnTestSessRejected_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,2,1,8),_TmnxTwampSrvConnTestSessRejected_Type())
tmnxTwampSrvConnTestSessRejected.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvConnTestSessRejected.setStatus(_B)
_TmnxTwampSrvConnTestPacketsRx_Type=Counter32
_TmnxTwampSrvConnTestPacketsRx_Object=MibTableColumn
tmnxTwampSrvConnTestPacketsRx=_TmnxTwampSrvConnTestPacketsRx_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,2,1,9),_TmnxTwampSrvConnTestPacketsRx_Type())
tmnxTwampSrvConnTestPacketsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvConnTestPacketsRx.setStatus(_B)
_TmnxTwampSrvConnTestPacketsTx_Type=Counter32
_TmnxTwampSrvConnTestPacketsTx_Object=MibTableColumn
tmnxTwampSrvConnTestPacketsTx=_TmnxTwampSrvConnTestPacketsTx_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,2,1,10),_TmnxTwampSrvConnTestPacketsTx_Type())
tmnxTwampSrvConnTestPacketsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvConnTestPacketsTx.setStatus(_B)
_TmnxTwampSrvSessStatsTable_Object=MibTable
tmnxTwampSrvSessStatsTable=_TmnxTwampSrvSessStatsTable_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,3))
if mibBuilder.loadTexts:tmnxTwampSrvSessStatsTable.setStatus(_B)
_TmnxTwampSrvSessStatsEntry_Object=MibTableRow
tmnxTwampSrvSessStatsEntry=_TmnxTwampSrvSessStatsEntry_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,3,1))
tmnxTwampSrvSessStatsEntry.setIndexNames((0,_A,_S),(0,_A,_T),(0,_A,_U),(0,_A,_k))
if mibBuilder.loadTexts:tmnxTwampSrvSessStatsEntry.setStatus(_B)
class _TmnxTwampSrvSessSeqNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TmnxTwampSrvSessSeqNum_Type.__name__=_I
_TmnxTwampSrvSessSeqNum_Object=MibTableColumn
tmnxTwampSrvSessSeqNum=_TmnxTwampSrvSessSeqNum_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,3,1,1),_TmnxTwampSrvSessSeqNum_Type())
tmnxTwampSrvSessSeqNum.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxTwampSrvSessSeqNum.setStatus(_B)
class _TmnxTwampSrvSessID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_TmnxTwampSrvSessID_Type.__name__=_g
_TmnxTwampSrvSessID_Object=MibTableColumn
tmnxTwampSrvSessID=_TmnxTwampSrvSessID_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,3,1,2),_TmnxTwampSrvSessID_Type())
tmnxTwampSrvSessID.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvSessID.setStatus(_B)
class _TmnxTwampSrvSessOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('create',1),('active',2),('stop',3)))
_TmnxTwampSrvSessOperState_Type.__name__=_M
_TmnxTwampSrvSessOperState_Object=MibTableColumn
tmnxTwampSrvSessOperState=_TmnxTwampSrvSessOperState_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,3,1,3),_TmnxTwampSrvSessOperState_Type())
tmnxTwampSrvSessOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvSessOperState.setStatus(_B)
_TmnxTwampSrvSessSenderAddrType_Type=InetAddressType
_TmnxTwampSrvSessSenderAddrType_Object=MibTableColumn
tmnxTwampSrvSessSenderAddrType=_TmnxTwampSrvSessSenderAddrType_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,3,1,4),_TmnxTwampSrvSessSenderAddrType_Type())
tmnxTwampSrvSessSenderAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvSessSenderAddrType.setStatus(_B)
class _TmnxTwampSrvSessSenderAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TmnxTwampSrvSessSenderAddress_Type.__name__=_D
_TmnxTwampSrvSessSenderAddress_Object=MibTableColumn
tmnxTwampSrvSessSenderAddress=_TmnxTwampSrvSessSenderAddress_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,3,1,5),_TmnxTwampSrvSessSenderAddress_Type())
tmnxTwampSrvSessSenderAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvSessSenderAddress.setStatus(_B)
_TmnxTwampSrvSessSenderUdpPort_Type=InetPortNumber
_TmnxTwampSrvSessSenderUdpPort_Object=MibTableColumn
tmnxTwampSrvSessSenderUdpPort=_TmnxTwampSrvSessSenderUdpPort_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,3,1,6),_TmnxTwampSrvSessSenderUdpPort_Type())
tmnxTwampSrvSessSenderUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvSessSenderUdpPort.setStatus(_B)
_TmnxTwampSrvSessReflectorAddrTyp_Type=InetAddressType
_TmnxTwampSrvSessReflectorAddrTyp_Object=MibTableColumn
tmnxTwampSrvSessReflectorAddrTyp=_TmnxTwampSrvSessReflectorAddrTyp_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,3,1,7),_TmnxTwampSrvSessReflectorAddrTyp_Type())
tmnxTwampSrvSessReflectorAddrTyp.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvSessReflectorAddrTyp.setStatus(_B)
class _TmnxTwampSrvSessReflectorAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TmnxTwampSrvSessReflectorAddress_Type.__name__=_D
_TmnxTwampSrvSessReflectorAddress_Object=MibTableColumn
tmnxTwampSrvSessReflectorAddress=_TmnxTwampSrvSessReflectorAddress_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,3,1,8),_TmnxTwampSrvSessReflectorAddress_Type())
tmnxTwampSrvSessReflectorAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvSessReflectorAddress.setStatus(_B)
_TmnxTwampSrvSessReflectorUdpPort_Type=InetPortNumber
_TmnxTwampSrvSessReflectorUdpPort_Object=MibTableColumn
tmnxTwampSrvSessReflectorUdpPort=_TmnxTwampSrvSessReflectorUdpPort_Object((1,3,6,1,4,1,6527,3,1,2,76,3,2,3,1,9),_TmnxTwampSrvSessReflectorUdpPort_Type())
tmnxTwampSrvSessReflectorUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxTwampSrvSessReflectorUdpPort.setStatus(_B)
_TmnxTwampNotificationObjs_ObjectIdentity=ObjectIdentity
tmnxTwampNotificationObjs=_TmnxTwampNotificationObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,76,4))
_TmnxTwampSrvNotifClientAddrType_Type=InetAddressType
_TmnxTwampSrvNotifClientAddrType_Object=MibScalar
tmnxTwampSrvNotifClientAddrType=_TmnxTwampSrvNotifClientAddrType_Object((1,3,6,1,4,1,6527,3,1,2,76,4,1),_TmnxTwampSrvNotifClientAddrType_Type())
tmnxTwampSrvNotifClientAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxTwampSrvNotifClientAddrType.setStatus(_B)
class _TmnxTwampSrvNotifClientAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TmnxTwampSrvNotifClientAddr_Type.__name__=_D
_TmnxTwampSrvNotifClientAddr_Object=MibScalar
tmnxTwampSrvNotifClientAddr=_TmnxTwampSrvNotifClientAddr_Object((1,3,6,1,4,1,6527,3,1,2,76,4,2),_TmnxTwampSrvNotifClientAddr_Type())
tmnxTwampSrvNotifClientAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxTwampSrvNotifClientAddr.setStatus(_B)
_TmnxTwampRflNotifLocalAddrType_Type=InetAddressType
_TmnxTwampRflNotifLocalAddrType_Object=MibScalar
tmnxTwampRflNotifLocalAddrType=_TmnxTwampRflNotifLocalAddrType_Object((1,3,6,1,4,1,6527,3,1,2,76,4,3),_TmnxTwampRflNotifLocalAddrType_Type())
tmnxTwampRflNotifLocalAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxTwampRflNotifLocalAddrType.setStatus(_B)
class _TmnxTwampRflNotifLocalAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TmnxTwampRflNotifLocalAddr_Type.__name__=_D
_TmnxTwampRflNotifLocalAddr_Object=MibScalar
tmnxTwampRflNotifLocalAddr=_TmnxTwampRflNotifLocalAddr_Object((1,3,6,1,4,1,6527,3,1,2,76,4,4),_TmnxTwampRflNotifLocalAddr_Type())
tmnxTwampRflNotifLocalAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxTwampRflNotifLocalAddr.setStatus(_B)
_TmnxTwampRflNotifLocalUdpPort_Type=TTcpUdpPort
_TmnxTwampRflNotifLocalUdpPort_Object=MibScalar
tmnxTwampRflNotifLocalUdpPort=_TmnxTwampRflNotifLocalUdpPort_Object((1,3,6,1,4,1,6527,3,1,2,76,4,5),_TmnxTwampRflNotifLocalUdpPort_Type())
tmnxTwampRflNotifLocalUdpPort.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxTwampRflNotifLocalUdpPort.setStatus(_B)
_TmnxTwampRflNotifRemoteAddrType_Type=InetAddressType
_TmnxTwampRflNotifRemoteAddrType_Object=MibScalar
tmnxTwampRflNotifRemoteAddrType=_TmnxTwampRflNotifRemoteAddrType_Object((1,3,6,1,4,1,6527,3,1,2,76,4,6),_TmnxTwampRflNotifRemoteAddrType_Type())
tmnxTwampRflNotifRemoteAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxTwampRflNotifRemoteAddrType.setStatus(_B)
class _TmnxTwampRflNotifRemoteAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TmnxTwampRflNotifRemoteAddr_Type.__name__=_D
_TmnxTwampRflNotifRemoteAddr_Object=MibScalar
tmnxTwampRflNotifRemoteAddr=_TmnxTwampRflNotifRemoteAddr_Object((1,3,6,1,4,1,6527,3,1,2,76,4,7),_TmnxTwampRflNotifRemoteAddr_Type())
tmnxTwampRflNotifRemoteAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxTwampRflNotifRemoteAddr.setStatus(_B)
_TmnxTwampRflNotifRemoteUdpPort_Type=TTcpUdpPort
_TmnxTwampRflNotifRemoteUdpPort_Object=MibScalar
tmnxTwampRflNotifRemoteUdpPort=_TmnxTwampRflNotifRemoteUdpPort_Object((1,3,6,1,4,1,6527,3,1,2,76,4,8),_TmnxTwampRflNotifRemoteUdpPort_Type())
tmnxTwampRflNotifRemoteUdpPort.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxTwampRflNotifRemoteUdpPort.setStatus(_B)
_TmnxTwampNotifyPrefix_ObjectIdentity=ObjectIdentity
tmnxTwampNotifyPrefix=_TmnxTwampNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,76))
_TmnxTwampNotifications_ObjectIdentity=ObjectIdentity
tmnxTwampNotifications=_TmnxTwampNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,76,0))
tmnxTwampSrvPrefixEntry.registerAugmentions((_A,_l))
tmnxTwampSrvPrefixStatsEntry.setIndexNames(*tmnxTwampSrvPrefixEntry.getIndexNames())
tmnxTwampSrvV9v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,76,2,1,1))
tmnxTwampSrvV9v0Group.setObjects(*((_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_V),(_A,_y),(_A,_W),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_X),(_A,_A4),(_A,_Y),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_Z),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF)))
if mibBuilder.loadTexts:tmnxTwampSrvV9v0Group.setStatus(_B)
tmnxTwampSrvNotifyObjsV9v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,76,2,1,3))
tmnxTwampSrvNotifyObjsV9v0Group.setObjects(*((_A,_G),(_A,_H)))
if mibBuilder.loadTexts:tmnxTwampSrvNotifyObjsV9v0Group.setStatus(_B)
tmnxTwampSrvV14v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,76,2,2,1))
tmnxTwampSrvV14v0Group.setObjects(*((_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO)))
if mibBuilder.loadTexts:tmnxTwampSrvV14v0Group.setStatus(_B)
tmnxTwampRflInactivityV19v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,76,2,3,1))
tmnxTwampRflInactivityV19v0Group.setObjects((_A,_AP))
if mibBuilder.loadTexts:tmnxTwampRflInactivityV19v0Group.setStatus(_B)
tmnxTwampRflInNotifyObjsV19v0Grp=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,76,2,3,3))
tmnxTwampRflInNotifyObjsV19v0Grp.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:tmnxTwampRflInNotifyObjsV19v0Grp.setStatus(_B)
tmnxTwampSrvInactivityTimeout=NotificationType((1,3,6,1,4,1,6527,3,1,3,76,0,1))
tmnxTwampSrvInactivityTimeout.setObjects((_A,_Z))
if mibBuilder.loadTexts:tmnxTwampSrvInactivityTimeout.setStatus(_B)
tmnxTwampSrvMaxConnsExceeded=NotificationType((1,3,6,1,4,1,6527,3,1,3,76,0,2))
tmnxTwampSrvMaxConnsExceeded.setObjects(*((_A,_V),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:tmnxTwampSrvMaxConnsExceeded.setStatus(_B)
tmnxTwampSrvPfxMaxConnsExceeded=NotificationType((1,3,6,1,4,1,6527,3,1,3,76,0,3))
tmnxTwampSrvPfxMaxConnsExceeded.setObjects(*((_A,_X),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:tmnxTwampSrvPfxMaxConnsExceeded.setStatus(_B)
tmnxTwampSrvMaxSessExceeded=NotificationType((1,3,6,1,4,1,6527,3,1,3,76,0,4))
tmnxTwampSrvMaxSessExceeded.setObjects(*((_A,_W),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:tmnxTwampSrvMaxSessExceeded.setStatus(_B)
tmnxTwampSrvPfxMaxSessExceeded=NotificationType((1,3,6,1,4,1,6527,3,1,3,76,0,5))
tmnxTwampSrvPfxMaxSessExceeded.setObjects(*((_A,_Y),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:tmnxTwampSrvPfxMaxSessExceeded.setStatus(_B)
tmnxTwampRflInactivityTimeout=NotificationType((1,3,6,1,4,1,6527,3,1,3,76,0,6))
tmnxTwampRflInactivityTimeout.setObjects(*((_A,_G),(_A,_H),(_A,_b),(_A,_a),(_A,_c),(_A,_e),(_A,_d),(_A,_f)))
if mibBuilder.loadTexts:tmnxTwampRflInactivityTimeout.setStatus(_B)
tmnxTwampSrvNotifyV9v0Group=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,76,2,1,2))
tmnxTwampSrvNotifyV9v0Group.setObjects(*((_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU)))
if mibBuilder.loadTexts:tmnxTwampSrvNotifyV9v0Group.setStatus(_B)
tmnxTwampRflInactNotifV19v0Group=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,76,2,3,2))
tmnxTwampRflInactNotifV19v0Group.setObjects((_A,_AV))
if mibBuilder.loadTexts:tmnxTwampRflInactNotifV19v0Group.setStatus(_B)
tmnxTwampCompliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,76,1,1))
tmnxTwampCompliance.setObjects(*((_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac)))
if mibBuilder.loadTexts:tmnxTwampCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_N:TmnxTwampSrvConnectionCount,_O:TmnxTwampSrvSessionCount,'timetraTwampMIBModule':timetraTwampMIBModule,'tmnxTwampConformance':tmnxTwampConformance,'tmnxTwampComplianceObjs':tmnxTwampComplianceObjs,'tmnxTwampCompliance':tmnxTwampCompliance,'tmnxTwampGroupObjs':tmnxTwampGroupObjs,'tmnxTwampV9v0GroupObjs':tmnxTwampV9v0GroupObjs,_Ac:tmnxTwampSrvV9v0Group,_AX:tmnxTwampSrvNotifyV9v0Group,_Aa:tmnxTwampSrvNotifyObjsV9v0Group,'tmnxTwampV14v0GroupObjs':tmnxTwampV14v0GroupObjs,_Ab:tmnxTwampSrvV14v0Group,'tmnxTwampV19v0GroupObjs':tmnxTwampV19v0GroupObjs,_AZ:tmnxTwampRflInactivityV19v0Group,_AW:tmnxTwampRflInactNotifV19v0Group,_AY:tmnxTwampRflInNotifyObjsV19v0Grp,'tmnxTwampObjs':tmnxTwampObjs,'tmnxTwampTableLastChangeObjs':tmnxTwampTableLastChangeObjs,_q:tmnxTwampSrvPrefixTblLastChg,'tmnxTwampConfigObjs':tmnxTwampConfigObjs,'tmnxTwampConfigScalarObjs':tmnxTwampConfigScalarObjs,_m:tmnxTwampSrvAdminState,_n:tmnxTwampSrvInactTimeout,_o:tmnxTwampSrvMaxConnections,_p:tmnxTwampSrvMaxSessions,_AP:tmnxTwampRflInactTimeout,'tmnxTwampConfigTableObjs':tmnxTwampConfigTableObjs,'tmnxTwampSrvPrefixTable':tmnxTwampSrvPrefixTable,'tmnxTwampSrvPrefixEntry':tmnxTwampSrvPrefixEntry,_P:tmnxTwampSrvPrefixAddrType,_Q:tmnxTwampSrvPrefixAddr,_R:tmnxTwampSrvPrefixLen,_r:tmnxTwampSrvPrefixRowStatus,_s:tmnxTwampSrvPrefixLastChg,_t:tmnxTwampSrvPrefixDescription,_u:tmnxTwampSrvPrefixMaxConnections,_v:tmnxTwampSrvPrefixMaxSessions,'tmnxTwampStatisticsObjs':tmnxTwampStatisticsObjs,'tmnxTwampStatisticsScalarObjs':tmnxTwampStatisticsScalarObjs,_w:tmnxTwampSrvOperState,_x:tmnxTwampSrvUpTime,_V:tmnxTwampSrvConnectionCount,_y:tmnxTwampSrvConnectionsRejected,_W:tmnxTwampSrvSessionCount,_z:tmnxTwampSrvTestSessCompleted,_A0:tmnxTwampSrvTestSessRejected,_A1:tmnxTwampSrvTestSessAborted,_A2:tmnxTwampSrvTestPacketsRx,_A3:tmnxTwampSrvTestPacketsTx,_AG:tmnxTwampSrvCapabilities,'tmnxTwampStatisticsTableObjs':tmnxTwampStatisticsTableObjs,'tmnxTwampSrvPrefixStatsTable':tmnxTwampSrvPrefixStatsTable,_l:tmnxTwampSrvPrefixStatsEntry,_X:tmnxTwampSrvPfxConnCount,_A4:tmnxTwampSrvPfxConnsRejected,_Y:tmnxTwampSrvPfxSessionCount,_A5:tmnxTwampSrvPfxTestSessCompleted,_A6:tmnxTwampSrvPfxTestSessRejected,_A7:tmnxTwampSrvPfxTestSessAbort,_A8:tmnxTwampSrvPfxTestPacketsRx,_A9:tmnxTwampSrvPfxTestPacketsTx,'tmnxTwampSrvConnStatsTable':tmnxTwampSrvConnStatsTable,'tmnxTwampSrvConnStatsEntry':tmnxTwampSrvConnStatsEntry,_S:tmnxTwampSrvConnClientAddrType,_T:tmnxTwampSrvConnClientAddr,_U:tmnxTwampSrvConnSeqNum,_AA:tmnxTwampSrvConnState,_Z:tmnxTwampSrvConnIdleTime,_AB:tmnxTwampSrvConnSessionCount,_AC:tmnxTwampSrvConnTestSessComplete,_AD:tmnxTwampSrvConnTestSessRejected,_AE:tmnxTwampSrvConnTestPacketsRx,_AF:tmnxTwampSrvConnTestPacketsTx,'tmnxTwampSrvSessStatsTable':tmnxTwampSrvSessStatsTable,'tmnxTwampSrvSessStatsEntry':tmnxTwampSrvSessStatsEntry,_k:tmnxTwampSrvSessSeqNum,_AH:tmnxTwampSrvSessID,_AI:tmnxTwampSrvSessOperState,_AM:tmnxTwampSrvSessSenderAddrType,_AN:tmnxTwampSrvSessSenderAddress,_AO:tmnxTwampSrvSessSenderUdpPort,_AJ:tmnxTwampSrvSessReflectorAddrTyp,_AK:tmnxTwampSrvSessReflectorAddress,_AL:tmnxTwampSrvSessReflectorUdpPort,'tmnxTwampNotificationObjs':tmnxTwampNotificationObjs,_G:tmnxTwampSrvNotifClientAddrType,_H:tmnxTwampSrvNotifClientAddr,_b:tmnxTwampRflNotifLocalAddrType,_a:tmnxTwampRflNotifLocalAddr,_c:tmnxTwampRflNotifLocalUdpPort,_e:tmnxTwampRflNotifRemoteAddrType,_d:tmnxTwampRflNotifRemoteAddr,_f:tmnxTwampRflNotifRemoteUdpPort,'tmnxTwampNotifyPrefix':tmnxTwampNotifyPrefix,'tmnxTwampNotifications':tmnxTwampNotifications,_AQ:tmnxTwampSrvInactivityTimeout,_AR:tmnxTwampSrvMaxConnsExceeded,_AS:tmnxTwampSrvPfxMaxConnsExceeded,_AT:tmnxTwampSrvMaxSessExceeded,_AU:tmnxTwampSrvPfxMaxSessExceeded,_AV:tmnxTwampRflInactivityTimeout})