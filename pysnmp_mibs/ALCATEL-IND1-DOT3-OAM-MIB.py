_AC='alaDot3OamNotificationGroup'
_AB='alaDot3OamRetrieveResponseGroup'
_AA='alaDot3OamRetrieveRequestGroup'
_A9='alaDot3OamPortEventLogsGroup'
_A8='alaDot3OamPortStatsGroup'
_A7='alaDot3OamPortLoopbackControlGroup'
_A6='alaDot3OamPortConfigGroup'
_A5='alaDot3OamBaseGroup'
_A4='alaDot3OamNonThresholdEventClear'
_A3='alaDot3OamThresholdEventClear'
_A2='alaDot3OamVariableResponseValue'
_A1='alaDot3OamPortClearVariableTransactions'
_A0='alaDot3OamVariableRequestRowStatus'
_z='alaDot3OamVariableRequestRetrieveStatus'
_y='alaDot3OamPortClearEventLogs'
_x='alaDot3OamPortClearStats'
_w='alaDot3OamPortL1PingAverageRoundTripDelay'
_v='alaDot3OamPortL1PingFramesReceived'
_u='alaDot3OamPortL1PingFramesSent'
_t='alaDot3OamPortL1PingStatus'
_s='alaDot3OamPortL1PingFramesDelay'
_r='alaDot3OamPortL1PingFramesConf'
_q='alaDot3OamNextTransactionId'
_p='alaDot3OamHelloInterval'
_o='alaDot3OamKeepAliveInterval'
_n='alaDot3OamMultiplePduCount'
_m='alaDot3OamGlobalClearVariableTransactions'
_l='alaDot3OamGlobalClearEventLogs'
_k='alaDot3OamGlobalClearStats'
_j='alaDot3OamStatus'
_i='alaDot3OamStatsEntry'
_h='alaDot3OamLoopbackEntry'
_g='alaDot3OamEntry'
_f='alaDot3OamVariableResponseLeaf'
_e='alaDot3OamVariableResponseBranch'
_d='read-create'
_c='attribute'
_b='package'
_a='object'
_Z='alaDot3OamVariableRequestLeaf'
_Y='alaDot3OamVariableRequestBranch'
_X='DisplayString'
_W='dot3OamEventLogWindowLo'
_V='dot3OamEventLogWindowHi'
_U='dot3OamEventLogValue'
_T='dot3OamEventLogThresholdLo'
_S='dot3OamEventLogThresholdHi'
_R='dot3OamEventLogRunningTotal'
_Q='alaDot3OamTransactionId'
_P='dot3OamEventLogType'
_O='dot3OamEventLogTimestamp'
_N='dot3OamEventLogOui'
_M='dot3OamEventLogLocation'
_L='dot3OamEventLogEventTotal'
_K='ifIndex'
_J='IF-MIB'
_I='not-accessible'
_H='read-only'
_G='reset'
_F='default'
_E='read-write'
_D='DOT3-OAM-MIB'
_C='Integer32'
_B='ALCATEL-IND1-DOT3-OAM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1Dot3Oam,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','softentIND1Dot3Oam')
dot3OamEntry,dot3OamEventLogEventTotal,dot3OamEventLogLocation,dot3OamEventLogOui,dot3OamEventLogRunningTotal,dot3OamEventLogThresholdHi,dot3OamEventLogThresholdLo,dot3OamEventLogTimestamp,dot3OamEventLogType,dot3OamEventLogValue,dot3OamEventLogWindowHi,dot3OamEventLogWindowLo,dot3OamLoopbackEntry,dot3OamStatsEntry=mibBuilder.importSymbols(_D,'dot3OamEntry',_L,_M,_N,_R,_S,_T,_O,_P,_U,_V,_W,'dot3OamLoopbackEntry','dot3OamStatsEntry')
ifIndex,=mibBuilder.importSymbols(_J,_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_X,'PhysAddress','RowStatus','TextualConvention')
alcatelIND1Dot3OamMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,52,1))
if mibBuilder.loadTexts:alcatelIND1Dot3OamMIB.setRevisions(('2009-02-25 00:00',))
_AlcatelIND1Dot3OamNotifications_ObjectIdentity=ObjectIdentity
alcatelIND1Dot3OamNotifications=_AlcatelIND1Dot3OamNotifications_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,52,1,0))
if mibBuilder.loadTexts:alcatelIND1Dot3OamNotifications.setStatus(_A)
_AlcatelIND1Dot3OamMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1Dot3OamMIBObjects=_AlcatelIND1Dot3OamMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,52,1,1))
if mibBuilder.loadTexts:alcatelIND1Dot3OamMIBObjects.setStatus(_A)
class _AlaDot3OamStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_AlaDot3OamStatus_Type.__name__=_C
_AlaDot3OamStatus_Object=MibScalar
alaDot3OamStatus=_AlaDot3OamStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,1),_AlaDot3OamStatus_Type())
alaDot3OamStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDot3OamStatus.setStatus(_A)
class _AlaDot3OamGlobalClearStats_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AlaDot3OamGlobalClearStats_Type.__name__=_C
_AlaDot3OamGlobalClearStats_Object=MibScalar
alaDot3OamGlobalClearStats=_AlaDot3OamGlobalClearStats_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,2),_AlaDot3OamGlobalClearStats_Type())
alaDot3OamGlobalClearStats.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDot3OamGlobalClearStats.setStatus(_A)
class _AlaDot3OamGlobalClearEventLogs_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AlaDot3OamGlobalClearEventLogs_Type.__name__=_C
_AlaDot3OamGlobalClearEventLogs_Object=MibScalar
alaDot3OamGlobalClearEventLogs=_AlaDot3OamGlobalClearEventLogs_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,3),_AlaDot3OamGlobalClearEventLogs_Type())
alaDot3OamGlobalClearEventLogs.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDot3OamGlobalClearEventLogs.setStatus(_A)
class _AlaDot3OamGlobalClearVariableTransactions_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AlaDot3OamGlobalClearVariableTransactions_Type.__name__=_C
_AlaDot3OamGlobalClearVariableTransactions_Object=MibScalar
alaDot3OamGlobalClearVariableTransactions=_AlaDot3OamGlobalClearVariableTransactions_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,4),_AlaDot3OamGlobalClearVariableTransactions_Type())
alaDot3OamGlobalClearVariableTransactions.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDot3OamGlobalClearVariableTransactions.setStatus(_A)
class _AlaDot3OamMultiplePduCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_AlaDot3OamMultiplePduCount_Type.__name__=_C
_AlaDot3OamMultiplePduCount_Object=MibScalar
alaDot3OamMultiplePduCount=_AlaDot3OamMultiplePduCount_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,5),_AlaDot3OamMultiplePduCount_Type())
alaDot3OamMultiplePduCount.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDot3OamMultiplePduCount.setStatus(_A)
_AlaDot3OamPortConfig_ObjectIdentity=ObjectIdentity
alaDot3OamPortConfig=_AlaDot3OamPortConfig_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,8))
_AlaDot3OamTable_Object=MibTable
alaDot3OamTable=_AlaDot3OamTable_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,8,1))
if mibBuilder.loadTexts:alaDot3OamTable.setStatus(_A)
_AlaDot3OamEntry_Object=MibTableRow
alaDot3OamEntry=_AlaDot3OamEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,8,1,1))
if mibBuilder.loadTexts:alaDot3OamEntry.setStatus(_A)
class _AlaDot3OamKeepAliveInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,120))
_AlaDot3OamKeepAliveInterval_Type.__name__=_C
_AlaDot3OamKeepAliveInterval_Object=MibTableColumn
alaDot3OamKeepAliveInterval=_AlaDot3OamKeepAliveInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,8,1,1,1),_AlaDot3OamKeepAliveInterval_Type())
alaDot3OamKeepAliveInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDot3OamKeepAliveInterval.setStatus(_A)
class _AlaDot3OamHelloInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_AlaDot3OamHelloInterval_Type.__name__=_C
_AlaDot3OamHelloInterval_Object=MibTableColumn
alaDot3OamHelloInterval=_AlaDot3OamHelloInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,8,1,1,2),_AlaDot3OamHelloInterval_Type())
alaDot3OamHelloInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDot3OamHelloInterval.setStatus(_A)
if mibBuilder.loadTexts:alaDot3OamHelloInterval.setUnits('seconds')
class _AlaDot3OamNextTransactionId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AlaDot3OamNextTransactionId_Type.__name__=_C
_AlaDot3OamNextTransactionId_Object=MibTableColumn
alaDot3OamNextTransactionId=_AlaDot3OamNextTransactionId_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,8,1,1,3),_AlaDot3OamNextTransactionId_Type())
alaDot3OamNextTransactionId.setMaxAccess(_H)
if mibBuilder.loadTexts:alaDot3OamNextTransactionId.setStatus(_A)
_AlaDot3OamPortLoopbackControl_ObjectIdentity=ObjectIdentity
alaDot3OamPortLoopbackControl=_AlaDot3OamPortLoopbackControl_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,9))
_AlaDot3OamLoopbackTable_Object=MibTable
alaDot3OamLoopbackTable=_AlaDot3OamLoopbackTable_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,9,1))
if mibBuilder.loadTexts:alaDot3OamLoopbackTable.setStatus(_A)
_AlaDot3OamLoopbackEntry_Object=MibTableRow
alaDot3OamLoopbackEntry=_AlaDot3OamLoopbackEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,9,1,1))
if mibBuilder.loadTexts:alaDot3OamLoopbackEntry.setStatus(_A)
class _AlaDot3OamPortL1PingFramesConf_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_AlaDot3OamPortL1PingFramesConf_Type.__name__=_C
_AlaDot3OamPortL1PingFramesConf_Object=MibTableColumn
alaDot3OamPortL1PingFramesConf=_AlaDot3OamPortL1PingFramesConf_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,9,1,1,1),_AlaDot3OamPortL1PingFramesConf_Type())
alaDot3OamPortL1PingFramesConf.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDot3OamPortL1PingFramesConf.setStatus(_A)
class _AlaDot3OamPortL1PingFramesDelay_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_AlaDot3OamPortL1PingFramesDelay_Type.__name__=_C
_AlaDot3OamPortL1PingFramesDelay_Object=MibTableColumn
alaDot3OamPortL1PingFramesDelay=_AlaDot3OamPortL1PingFramesDelay_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,9,1,1,2),_AlaDot3OamPortL1PingFramesDelay_Type())
alaDot3OamPortL1PingFramesDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDot3OamPortL1PingFramesDelay.setStatus(_A)
if mibBuilder.loadTexts:alaDot3OamPortL1PingFramesDelay.setUnits('milliseconds')
class _AlaDot3OamPortL1PingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_F,0),('start',1),('running',2),('operationSuccessful',3),('operationUnsuccessful',4)))
_AlaDot3OamPortL1PingStatus_Type.__name__=_C
_AlaDot3OamPortL1PingStatus_Object=MibTableColumn
alaDot3OamPortL1PingStatus=_AlaDot3OamPortL1PingStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,9,1,1,3),_AlaDot3OamPortL1PingStatus_Type())
alaDot3OamPortL1PingStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDot3OamPortL1PingStatus.setStatus(_A)
_AlaDot3OamPortL1PingFramesSent_Type=Counter32
_AlaDot3OamPortL1PingFramesSent_Object=MibTableColumn
alaDot3OamPortL1PingFramesSent=_AlaDot3OamPortL1PingFramesSent_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,9,1,1,4),_AlaDot3OamPortL1PingFramesSent_Type())
alaDot3OamPortL1PingFramesSent.setMaxAccess(_H)
if mibBuilder.loadTexts:alaDot3OamPortL1PingFramesSent.setStatus(_A)
_AlaDot3OamPortL1PingFramesReceived_Type=Counter32
_AlaDot3OamPortL1PingFramesReceived_Object=MibTableColumn
alaDot3OamPortL1PingFramesReceived=_AlaDot3OamPortL1PingFramesReceived_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,9,1,1,5),_AlaDot3OamPortL1PingFramesReceived_Type())
alaDot3OamPortL1PingFramesReceived.setMaxAccess(_H)
if mibBuilder.loadTexts:alaDot3OamPortL1PingFramesReceived.setStatus(_A)
_AlaDot3OamPortL1PingAverageRoundTripDelay_Type=Integer32
_AlaDot3OamPortL1PingAverageRoundTripDelay_Object=MibTableColumn
alaDot3OamPortL1PingAverageRoundTripDelay=_AlaDot3OamPortL1PingAverageRoundTripDelay_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,9,1,1,6),_AlaDot3OamPortL1PingAverageRoundTripDelay_Type())
alaDot3OamPortL1PingAverageRoundTripDelay.setMaxAccess(_H)
if mibBuilder.loadTexts:alaDot3OamPortL1PingAverageRoundTripDelay.setStatus(_A)
_AlaDot3OamPortStats_ObjectIdentity=ObjectIdentity
alaDot3OamPortStats=_AlaDot3OamPortStats_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,10))
_AlaDot3OamStatsTable_Object=MibTable
alaDot3OamStatsTable=_AlaDot3OamStatsTable_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,10,1))
if mibBuilder.loadTexts:alaDot3OamStatsTable.setStatus(_A)
_AlaDot3OamStatsEntry_Object=MibTableRow
alaDot3OamStatsEntry=_AlaDot3OamStatsEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,10,1,1))
if mibBuilder.loadTexts:alaDot3OamStatsEntry.setStatus(_A)
class _AlaDot3OamPortClearStats_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AlaDot3OamPortClearStats_Type.__name__=_C
_AlaDot3OamPortClearStats_Object=MibTableColumn
alaDot3OamPortClearStats=_AlaDot3OamPortClearStats_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,10,1,1,1),_AlaDot3OamPortClearStats_Type())
alaDot3OamPortClearStats.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDot3OamPortClearStats.setStatus(_A)
_AlaDot3OamPortEventLogs_ObjectIdentity=ObjectIdentity
alaDot3OamPortEventLogs=_AlaDot3OamPortEventLogs_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,11))
_AlaDot3OamEventLogTable_Object=MibTable
alaDot3OamEventLogTable=_AlaDot3OamEventLogTable_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,11,1))
if mibBuilder.loadTexts:alaDot3OamEventLogTable.setStatus(_A)
_AlaDot3OamEventLogEntry_Object=MibTableRow
alaDot3OamEventLogEntry=_AlaDot3OamEventLogEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,11,1,1))
alaDot3OamEventLogEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:alaDot3OamEventLogEntry.setStatus(_A)
class _AlaDot3OamPortClearEventLogs_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AlaDot3OamPortClearEventLogs_Type.__name__=_C
_AlaDot3OamPortClearEventLogs_Object=MibTableColumn
alaDot3OamPortClearEventLogs=_AlaDot3OamPortClearEventLogs_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,11,1,1,1),_AlaDot3OamPortClearEventLogs_Type())
alaDot3OamPortClearEventLogs.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDot3OamPortClearEventLogs.setStatus(_A)
_AlaDot3OamRetrieveRequest_ObjectIdentity=ObjectIdentity
alaDot3OamRetrieveRequest=_AlaDot3OamRetrieveRequest_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,12))
_AlaDot3OamRetrieveRequestTable_Object=MibTable
alaDot3OamRetrieveRequestTable=_AlaDot3OamRetrieveRequestTable_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,12,1))
if mibBuilder.loadTexts:alaDot3OamRetrieveRequestTable.setStatus(_A)
_AlaDot3OamRetrieveRequestEntry_Object=MibTableRow
alaDot3OamRetrieveRequestEntry=_AlaDot3OamRetrieveRequestEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,12,1,1))
alaDot3OamRetrieveRequestEntry.setIndexNames((0,_J,_K),(0,_B,_Q),(0,_B,_Y),(0,_B,_Z))
if mibBuilder.loadTexts:alaDot3OamRetrieveRequestEntry.setStatus(_A)
class _AlaDot3OamTransactionId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AlaDot3OamTransactionId_Type.__name__=_C
_AlaDot3OamTransactionId_Object=MibTableColumn
alaDot3OamTransactionId=_AlaDot3OamTransactionId_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,12,1,1,1),_AlaDot3OamTransactionId_Type())
alaDot3OamTransactionId.setMaxAccess(_I)
if mibBuilder.loadTexts:alaDot3OamTransactionId.setStatus(_A)
class _AlaDot3OamVariableRequestBranch_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,7)));namedValues=NamedValues(*((_a,3),(_b,4),(_c,7)))
_AlaDot3OamVariableRequestBranch_Type.__name__=_C
_AlaDot3OamVariableRequestBranch_Object=MibTableColumn
alaDot3OamVariableRequestBranch=_AlaDot3OamVariableRequestBranch_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,12,1,1,2),_AlaDot3OamVariableRequestBranch_Type())
alaDot3OamVariableRequestBranch.setMaxAccess(_I)
if mibBuilder.loadTexts:alaDot3OamVariableRequestBranch.setStatus(_A)
class _AlaDot3OamVariableRequestLeaf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AlaDot3OamVariableRequestLeaf_Type.__name__=_C
_AlaDot3OamVariableRequestLeaf_Object=MibTableColumn
alaDot3OamVariableRequestLeaf=_AlaDot3OamVariableRequestLeaf_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,12,1,1,3),_AlaDot3OamVariableRequestLeaf_Type())
alaDot3OamVariableRequestLeaf.setMaxAccess(_I)
if mibBuilder.loadTexts:alaDot3OamVariableRequestLeaf.setStatus(_A)
class _AlaDot3OamVariableRequestRetrieveStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('failed',2),('success',3)))
_AlaDot3OamVariableRequestRetrieveStatus_Type.__name__=_C
_AlaDot3OamVariableRequestRetrieveStatus_Object=MibTableColumn
alaDot3OamVariableRequestRetrieveStatus=_AlaDot3OamVariableRequestRetrieveStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,12,1,1,4),_AlaDot3OamVariableRequestRetrieveStatus_Type())
alaDot3OamVariableRequestRetrieveStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:alaDot3OamVariableRequestRetrieveStatus.setStatus(_A)
_AlaDot3OamVariableRequestRowStatus_Type=RowStatus
_AlaDot3OamVariableRequestRowStatus_Object=MibTableColumn
alaDot3OamVariableRequestRowStatus=_AlaDot3OamVariableRequestRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,12,1,1,5),_AlaDot3OamVariableRequestRowStatus_Type())
alaDot3OamVariableRequestRowStatus.setMaxAccess(_d)
if mibBuilder.loadTexts:alaDot3OamVariableRequestRowStatus.setStatus(_A)
class _AlaDot3OamPortClearVariableTransactions_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_AlaDot3OamPortClearVariableTransactions_Type.__name__=_C
_AlaDot3OamPortClearVariableTransactions_Object=MibTableColumn
alaDot3OamPortClearVariableTransactions=_AlaDot3OamPortClearVariableTransactions_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,12,1,1,6),_AlaDot3OamPortClearVariableTransactions_Type())
alaDot3OamPortClearVariableTransactions.setMaxAccess(_d)
if mibBuilder.loadTexts:alaDot3OamPortClearVariableTransactions.setStatus(_A)
_AlaDot3OamRetrieveResponse_ObjectIdentity=ObjectIdentity
alaDot3OamRetrieveResponse=_AlaDot3OamRetrieveResponse_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,13))
_AlaDot3OamRetrieveResponseTable_Object=MibTable
alaDot3OamRetrieveResponseTable=_AlaDot3OamRetrieveResponseTable_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,13,1))
if mibBuilder.loadTexts:alaDot3OamRetrieveResponseTable.setStatus(_A)
_AlaDot3OamRetrieveResponseEntry_Object=MibTableRow
alaDot3OamRetrieveResponseEntry=_AlaDot3OamRetrieveResponseEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,13,1,1))
alaDot3OamRetrieveResponseEntry.setIndexNames((0,_J,_K),(0,_B,_Q),(0,_B,_e),(0,_B,_f))
if mibBuilder.loadTexts:alaDot3OamRetrieveResponseEntry.setStatus(_A)
class _AlaDot3OamVariableResponseBranch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,7)));namedValues=NamedValues(*((_a,3),(_b,4),(_c,7)))
_AlaDot3OamVariableResponseBranch_Type.__name__=_C
_AlaDot3OamVariableResponseBranch_Object=MibTableColumn
alaDot3OamVariableResponseBranch=_AlaDot3OamVariableResponseBranch_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,13,1,1,1),_AlaDot3OamVariableResponseBranch_Type())
alaDot3OamVariableResponseBranch.setMaxAccess(_I)
if mibBuilder.loadTexts:alaDot3OamVariableResponseBranch.setStatus(_A)
class _AlaDot3OamVariableResponseLeaf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AlaDot3OamVariableResponseLeaf_Type.__name__=_C
_AlaDot3OamVariableResponseLeaf_Object=MibTableColumn
alaDot3OamVariableResponseLeaf=_AlaDot3OamVariableResponseLeaf_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,13,1,1,2),_AlaDot3OamVariableResponseLeaf_Type())
alaDot3OamVariableResponseLeaf.setMaxAccess(_I)
if mibBuilder.loadTexts:alaDot3OamVariableResponseLeaf.setStatus(_A)
class _AlaDot3OamVariableResponseValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_AlaDot3OamVariableResponseValue_Type.__name__=_X
_AlaDot3OamVariableResponseValue_Object=MibTableColumn
alaDot3OamVariableResponseValue=_AlaDot3OamVariableResponseValue_Object((1,3,6,1,4,1,6486,800,1,2,1,52,1,1,13,1,1,3),_AlaDot3OamVariableResponseValue_Type())
alaDot3OamVariableResponseValue.setMaxAccess(_H)
if mibBuilder.loadTexts:alaDot3OamVariableResponseValue.setStatus(_A)
_AlcatelIND1Dot3OamMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1Dot3OamMIBConformance=_AlcatelIND1Dot3OamMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,52,1,2))
if mibBuilder.loadTexts:alcatelIND1Dot3OamMIBConformance.setStatus(_A)
_AlcatelIND1Dot3OamMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1Dot3OamMIBGroups=_AlcatelIND1Dot3OamMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,52,1,2,1))
if mibBuilder.loadTexts:alcatelIND1Dot3OamMIBGroups.setStatus(_A)
_AlcatelIND1Dot3OamMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1Dot3OamMIBCompliances=_AlcatelIND1Dot3OamMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,52,1,2,2))
if mibBuilder.loadTexts:alcatelIND1Dot3OamMIBCompliances.setStatus(_A)
dot3OamEntry.registerAugmentions((_B,_g))
alaDot3OamEntry.setIndexNames(*dot3OamEntry.getIndexNames())
dot3OamLoopbackEntry.registerAugmentions((_B,_h))
alaDot3OamLoopbackEntry.setIndexNames(*dot3OamLoopbackEntry.getIndexNames())
dot3OamStatsEntry.registerAugmentions((_B,_i))
alaDot3OamStatsEntry.setIndexNames(*dot3OamStatsEntry.getIndexNames())
alaDot3OamBaseGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,52,1,2,1,1))
alaDot3OamBaseGroup.setObjects(*((_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:alaDot3OamBaseGroup.setStatus(_A)
alaDot3OamPortConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,52,1,2,1,2))
alaDot3OamPortConfigGroup.setObjects(*((_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:alaDot3OamPortConfigGroup.setStatus(_A)
alaDot3OamPortLoopbackControlGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,52,1,2,1,3))
alaDot3OamPortLoopbackControlGroup.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:alaDot3OamPortLoopbackControlGroup.setStatus(_A)
alaDot3OamPortStatsGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,52,1,2,1,4))
alaDot3OamPortStatsGroup.setObjects((_B,_x))
if mibBuilder.loadTexts:alaDot3OamPortStatsGroup.setStatus(_A)
alaDot3OamPortEventLogsGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,52,1,2,1,5))
alaDot3OamPortEventLogsGroup.setObjects((_B,_y))
if mibBuilder.loadTexts:alaDot3OamPortEventLogsGroup.setStatus(_A)
alaDot3OamRetrieveRequestGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,52,1,2,1,6))
alaDot3OamRetrieveRequestGroup.setObjects(*((_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:alaDot3OamRetrieveRequestGroup.setStatus(_A)
alaDot3OamRetrieveResponseGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,52,1,2,1,7))
alaDot3OamRetrieveResponseGroup.setObjects((_B,_A2))
if mibBuilder.loadTexts:alaDot3OamRetrieveResponseGroup.setStatus(_A)
alaDot3OamThresholdEventClear=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,52,1,0,1))
alaDot3OamThresholdEventClear.setObjects(*((_D,_O),(_D,_N),(_D,_P),(_D,_M),(_D,_V),(_D,_W),(_D,_S),(_D,_T),(_D,_U),(_D,_R),(_D,_L)))
if mibBuilder.loadTexts:alaDot3OamThresholdEventClear.setStatus(_A)
alaDot3OamNonThresholdEventClear=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,52,1,0,2))
alaDot3OamNonThresholdEventClear.setObjects(*((_D,_O),(_D,_N),(_D,_P),(_D,_M),(_D,_L)))
if mibBuilder.loadTexts:alaDot3OamNonThresholdEventClear.setStatus(_A)
alaDot3OamNotificationGroup=NotificationGroup((1,3,6,1,4,1,6486,800,1,2,1,52,1,2,1,8))
alaDot3OamNotificationGroup.setObjects(*((_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:alaDot3OamNotificationGroup.setStatus(_A)
alcatelIND1Dot3OamMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,52,1,2,2,1))
alcatelIND1Dot3OamMIBCompliance.setObjects(*((_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:alcatelIND1Dot3OamMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1Dot3OamMIB':alcatelIND1Dot3OamMIB,'alcatelIND1Dot3OamNotifications':alcatelIND1Dot3OamNotifications,_A3:alaDot3OamThresholdEventClear,_A4:alaDot3OamNonThresholdEventClear,'alcatelIND1Dot3OamMIBObjects':alcatelIND1Dot3OamMIBObjects,_j:alaDot3OamStatus,_k:alaDot3OamGlobalClearStats,_l:alaDot3OamGlobalClearEventLogs,_m:alaDot3OamGlobalClearVariableTransactions,_n:alaDot3OamMultiplePduCount,'alaDot3OamPortConfig':alaDot3OamPortConfig,'alaDot3OamTable':alaDot3OamTable,_g:alaDot3OamEntry,_o:alaDot3OamKeepAliveInterval,_p:alaDot3OamHelloInterval,_q:alaDot3OamNextTransactionId,'alaDot3OamPortLoopbackControl':alaDot3OamPortLoopbackControl,'alaDot3OamLoopbackTable':alaDot3OamLoopbackTable,_h:alaDot3OamLoopbackEntry,_r:alaDot3OamPortL1PingFramesConf,_s:alaDot3OamPortL1PingFramesDelay,_t:alaDot3OamPortL1PingStatus,_u:alaDot3OamPortL1PingFramesSent,_v:alaDot3OamPortL1PingFramesReceived,_w:alaDot3OamPortL1PingAverageRoundTripDelay,'alaDot3OamPortStats':alaDot3OamPortStats,'alaDot3OamStatsTable':alaDot3OamStatsTable,_i:alaDot3OamStatsEntry,_x:alaDot3OamPortClearStats,'alaDot3OamPortEventLogs':alaDot3OamPortEventLogs,'alaDot3OamEventLogTable':alaDot3OamEventLogTable,'alaDot3OamEventLogEntry':alaDot3OamEventLogEntry,_y:alaDot3OamPortClearEventLogs,'alaDot3OamRetrieveRequest':alaDot3OamRetrieveRequest,'alaDot3OamRetrieveRequestTable':alaDot3OamRetrieveRequestTable,'alaDot3OamRetrieveRequestEntry':alaDot3OamRetrieveRequestEntry,_Q:alaDot3OamTransactionId,_Y:alaDot3OamVariableRequestBranch,_Z:alaDot3OamVariableRequestLeaf,_z:alaDot3OamVariableRequestRetrieveStatus,_A0:alaDot3OamVariableRequestRowStatus,_A1:alaDot3OamPortClearVariableTransactions,'alaDot3OamRetrieveResponse':alaDot3OamRetrieveResponse,'alaDot3OamRetrieveResponseTable':alaDot3OamRetrieveResponseTable,'alaDot3OamRetrieveResponseEntry':alaDot3OamRetrieveResponseEntry,_e:alaDot3OamVariableResponseBranch,_f:alaDot3OamVariableResponseLeaf,_A2:alaDot3OamVariableResponseValue,'alcatelIND1Dot3OamMIBConformance':alcatelIND1Dot3OamMIBConformance,'alcatelIND1Dot3OamMIBGroups':alcatelIND1Dot3OamMIBGroups,_A5:alaDot3OamBaseGroup,_A6:alaDot3OamPortConfigGroup,_A7:alaDot3OamPortLoopbackControlGroup,_A8:alaDot3OamPortStatsGroup,_A9:alaDot3OamPortEventLogsGroup,_AA:alaDot3OamRetrieveRequestGroup,_AB:alaDot3OamRetrieveResponseGroup,_AC:alaDot3OamNotificationGroup,'alcatelIND1Dot3OamMIBCompliances':alcatelIND1Dot3OamMIBCompliances,'alcatelIND1Dot3OamMIBCompliance':alcatelIND1Dot3OamMIBCompliance})