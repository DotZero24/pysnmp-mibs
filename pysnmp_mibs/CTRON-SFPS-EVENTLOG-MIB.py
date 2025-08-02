_W='agentIP'
_V='lostNeighbor'
_U='foundNeighbor'
_T='changeCount'
_S='ageCnt'
_R='portFromStandby'
_Q='portToStandby'
_P='dstBlock'
_O='srcBlock'
_N='violation'
_M='newUser'
_L='sfpsEventLogClientConfigId'
_K='sfpsEventLogGenConfigSwInst'
_J='sfpsEventLogWindowStart'
_I='sfpsEventLogStatsSwInst'
_H='CTRON-SFPS-EVENTLOG-MIB'
_G='enable'
_F='disable'
_E='other'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sfpsEventLogClientConfig,sfpsEventLogClientConfigAPI,sfpsEventLogGenConfig,sfpsEventLogStats,sfpsFragStats,sfpsTrapAPI,sfpsTrapTable=mibBuilder.importSymbols('CTRON-SFPS-INCLUDE-MIB','sfpsEventLogClientConfig','sfpsEventLogClientConfigAPI','sfpsEventLogGenConfig','sfpsEventLogStats','sfpsFragStats','sfpsTrapAPI','sfpsTrapTable')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class SfpsSwitchInstance(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class HexInteger(Integer32):0
_SfpsEventLogStatsTable_Object=MibTable
sfpsEventLogStatsTable=_SfpsEventLogStatsTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,3,1))
if mibBuilder.loadTexts:sfpsEventLogStatsTable.setStatus(_A)
_SfpsEventLogStatsEntry_Object=MibTableRow
sfpsEventLogStatsEntry=_SfpsEventLogStatsEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,3,1,1))
sfpsEventLogStatsEntry.setIndexNames((0,_H,_I),(0,_H,_J))
if mibBuilder.loadTexts:sfpsEventLogStatsEntry.setStatus(_A)
_SfpsEventLogStatsSwInst_Type=SfpsSwitchInstance
_SfpsEventLogStatsSwInst_Object=MibTableColumn
sfpsEventLogStatsSwInst=_SfpsEventLogStatsSwInst_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,3,1,1,1),_SfpsEventLogStatsSwInst_Type())
sfpsEventLogStatsSwInst.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsEventLogStatsSwInst.setStatus(_A)
_SfpsEventLogWindowStart_Type=Integer32
_SfpsEventLogWindowStart_Object=MibTableColumn
sfpsEventLogWindowStart=_SfpsEventLogWindowStart_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,3,1,1,2),_SfpsEventLogWindowStart_Type())
sfpsEventLogWindowStart.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsEventLogWindowStart.setStatus(_A)
_SfpsEventLogIndex_Type=Integer32
_SfpsEventLogIndex_Object=MibTableColumn
sfpsEventLogIndex=_SfpsEventLogIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,3,1,1,3),_SfpsEventLogIndex_Type())
sfpsEventLogIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsEventLogIndex.setStatus(_A)
_SfpsEventLogClientName_Type=DisplayString
_SfpsEventLogClientName_Object=MibTableColumn
sfpsEventLogClientName=_SfpsEventLogClientName_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,3,1,1,4),_SfpsEventLogClientName_Type())
sfpsEventLogClientName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsEventLogClientName.setStatus(_A)
_SfpsEventLogLevel_Type=DisplayString
_SfpsEventLogLevel_Object=MibTableColumn
sfpsEventLogLevel=_SfpsEventLogLevel_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,3,1,1,5),_SfpsEventLogLevel_Type())
sfpsEventLogLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsEventLogLevel.setStatus(_A)
_SfpsEventLogMessageString_Type=DisplayString
_SfpsEventLogMessageString_Object=MibTableColumn
sfpsEventLogMessageString=_SfpsEventLogMessageString_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,3,1,1,6),_SfpsEventLogMessageString_Type())
sfpsEventLogMessageString.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsEventLogMessageString.setStatus(_A)
_SfpsEventLogTime_Type=TimeTicks
_SfpsEventLogTime_Object=MibTableColumn
sfpsEventLogTime=_SfpsEventLogTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,3,1,1,7),_SfpsEventLogTime_Type())
sfpsEventLogTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsEventLogTime.setStatus(_A)
_SfpsEventLogCallTag_Type=HexInteger
_SfpsEventLogCallTag_Object=MibTableColumn
sfpsEventLogCallTag=_SfpsEventLogCallTag_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,3,1,1,8),_SfpsEventLogCallTag_Type())
sfpsEventLogCallTag.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsEventLogCallTag.setStatus(_A)
_SfpsEventLogInfo1_Type=HexInteger
_SfpsEventLogInfo1_Object=MibTableColumn
sfpsEventLogInfo1=_SfpsEventLogInfo1_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,3,1,1,9),_SfpsEventLogInfo1_Type())
sfpsEventLogInfo1.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsEventLogInfo1.setStatus(_A)
_SfpsEventLogInfo2_Type=HexInteger
_SfpsEventLogInfo2_Object=MibTableColumn
sfpsEventLogInfo2=_SfpsEventLogInfo2_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,3,1,1,10),_SfpsEventLogInfo2_Type())
sfpsEventLogInfo2.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsEventLogInfo2.setStatus(_A)
_SfpsEventLogGenConfigTable_Object=MibTable
sfpsEventLogGenConfigTable=_SfpsEventLogGenConfigTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,4,1))
if mibBuilder.loadTexts:sfpsEventLogGenConfigTable.setStatus(_A)
_SfpsEventLogGenConfigEntry_Object=MibTableRow
sfpsEventLogGenConfigEntry=_SfpsEventLogGenConfigEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,4,1,1))
sfpsEventLogGenConfigEntry.setIndexNames((0,_H,_K))
if mibBuilder.loadTexts:sfpsEventLogGenConfigEntry.setStatus(_A)
_SfpsEventLogGenConfigSwInst_Type=SfpsSwitchInstance
_SfpsEventLogGenConfigSwInst_Object=MibTableColumn
sfpsEventLogGenConfigSwInst=_SfpsEventLogGenConfigSwInst_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,4,1,1,1),_SfpsEventLogGenConfigSwInst_Type())
sfpsEventLogGenConfigSwInst.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsEventLogGenConfigSwInst.setStatus(_A)
class _SfpsEventLogGenConfigWindowStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20000))
_SfpsEventLogGenConfigWindowStart_Type.__name__=_C
_SfpsEventLogGenConfigWindowStart_Object=MibTableColumn
sfpsEventLogGenConfigWindowStart=_SfpsEventLogGenConfigWindowStart_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,4,1,1,2),_SfpsEventLogGenConfigWindowStart_Type())
sfpsEventLogGenConfigWindowStart.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsEventLogGenConfigWindowStart.setStatus(_A)
class _SfpsEventLogGenConfigLoggingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20000))
_SfpsEventLogGenConfigLoggingIndex_Type.__name__=_C
_SfpsEventLogGenConfigLoggingIndex_Object=MibTableColumn
sfpsEventLogGenConfigLoggingIndex=_SfpsEventLogGenConfigLoggingIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,4,1,1,3),_SfpsEventLogGenConfigLoggingIndex_Type())
sfpsEventLogGenConfigLoggingIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsEventLogGenConfigLoggingIndex.setStatus(_A)
_SfpsEventLogGenConfigMessageFilter_Type=DisplayString
_SfpsEventLogGenConfigMessageFilter_Object=MibTableColumn
sfpsEventLogGenConfigMessageFilter=_SfpsEventLogGenConfigMessageFilter_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,4,1,1,4),_SfpsEventLogGenConfigMessageFilter_Type())
sfpsEventLogGenConfigMessageFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsEventLogGenConfigMessageFilter.setStatus(_A)
_SfpsEventLogGenConfigCallTagFilter_Type=HexInteger
_SfpsEventLogGenConfigCallTagFilter_Object=MibTableColumn
sfpsEventLogGenConfigCallTagFilter=_SfpsEventLogGenConfigCallTagFilter_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,4,1,1,5),_SfpsEventLogGenConfigCallTagFilter_Type())
sfpsEventLogGenConfigCallTagFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsEventLogGenConfigCallTagFilter.setStatus(_A)
class _SfpsEventLogGenConfigAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),('reset',4),('continue',5)))
_SfpsEventLogGenConfigAdminStatus_Type.__name__=_C
_SfpsEventLogGenConfigAdminStatus_Object=MibTableColumn
sfpsEventLogGenConfigAdminStatus=_SfpsEventLogGenConfigAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,4,1,1,6),_SfpsEventLogGenConfigAdminStatus_Type())
sfpsEventLogGenConfigAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsEventLogGenConfigAdminStatus.setStatus(_A)
class _SfpsEventLogGenConfigOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),('pending-disable',4),('pending-enable',5)))
_SfpsEventLogGenConfigOperStatus_Type.__name__=_C
_SfpsEventLogGenConfigOperStatus_Object=MibTableColumn
sfpsEventLogGenConfigOperStatus=_SfpsEventLogGenConfigOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,4,1,1,7),_SfpsEventLogGenConfigOperStatus_Type())
sfpsEventLogGenConfigOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsEventLogGenConfigOperStatus.setStatus(_A)
_SfpsEventLogGenConfigOperTime_Type=TimeTicks
_SfpsEventLogGenConfigOperTime_Object=MibTableColumn
sfpsEventLogGenConfigOperTime=_SfpsEventLogGenConfigOperTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,4,1,1,8),_SfpsEventLogGenConfigOperTime_Type())
sfpsEventLogGenConfigOperTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsEventLogGenConfigOperTime.setStatus(_A)
class _SfpsEventLogGenConfigAutoFreeze_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_SfpsEventLogGenConfigAutoFreeze_Type.__name__=_C
_SfpsEventLogGenConfigAutoFreeze_Object=MibTableColumn
sfpsEventLogGenConfigAutoFreeze=_SfpsEventLogGenConfigAutoFreeze_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,4,1,1,9),_SfpsEventLogGenConfigAutoFreeze_Type())
sfpsEventLogGenConfigAutoFreeze.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsEventLogGenConfigAutoFreeze.setStatus(_A)
class _SfpsEventLogGenConfigDisplayWrapDetect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_SfpsEventLogGenConfigDisplayWrapDetect_Type.__name__=_C
_SfpsEventLogGenConfigDisplayWrapDetect_Object=MibTableColumn
sfpsEventLogGenConfigDisplayWrapDetect=_SfpsEventLogGenConfigDisplayWrapDetect_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,4,1,1,10),_SfpsEventLogGenConfigDisplayWrapDetect_Type())
sfpsEventLogGenConfigDisplayWrapDetect.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsEventLogGenConfigDisplayWrapDetect.setStatus(_A)
_SfpsEventLogGenConfigAdvertiseAddr_Type=IpAddress
_SfpsEventLogGenConfigAdvertiseAddr_Object=MibTableColumn
sfpsEventLogGenConfigAdvertiseAddr=_SfpsEventLogGenConfigAdvertiseAddr_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,4,1,1,11),_SfpsEventLogGenConfigAdvertiseAddr_Type())
sfpsEventLogGenConfigAdvertiseAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsEventLogGenConfigAdvertiseAddr.setStatus(_A)
_SfpsEventLogClientConfigTable_Object=MibTable
sfpsEventLogClientConfigTable=_SfpsEventLogClientConfigTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,5,1))
if mibBuilder.loadTexts:sfpsEventLogClientConfigTable.setStatus(_A)
_SfpsEventLogClientConfigEntry_Object=MibTableRow
sfpsEventLogClientConfigEntry=_SfpsEventLogClientConfigEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,5,1,1))
sfpsEventLogClientConfigEntry.setIndexNames((0,_H,_L))
if mibBuilder.loadTexts:sfpsEventLogClientConfigEntry.setStatus(_A)
_SfpsEventLogClientConfigId_Type=Integer32
_SfpsEventLogClientConfigId_Object=MibTableColumn
sfpsEventLogClientConfigId=_SfpsEventLogClientConfigId_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,5,1,1,1),_SfpsEventLogClientConfigId_Type())
sfpsEventLogClientConfigId.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsEventLogClientConfigId.setStatus(_A)
_SfpsEventLogClientConfigName_Type=DisplayString
_SfpsEventLogClientConfigName_Object=MibTableColumn
sfpsEventLogClientConfigName=_SfpsEventLogClientConfigName_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,5,1,1,2),_SfpsEventLogClientConfigName_Type())
sfpsEventLogClientConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsEventLogClientConfigName.setStatus(_A)
class _SfpsEventLogClientLogStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_SfpsEventLogClientLogStatus_Type.__name__=_C
_SfpsEventLogClientLogStatus_Object=MibTableColumn
sfpsEventLogClientLogStatus=_SfpsEventLogClientLogStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,5,1,1,3),_SfpsEventLogClientLogStatus_Type())
sfpsEventLogClientLogStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsEventLogClientLogStatus.setStatus(_A)
class _SfpsEventLogClientDisplayStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_SfpsEventLogClientDisplayStatus_Type.__name__=_C
_SfpsEventLogClientDisplayStatus_Object=MibTableColumn
sfpsEventLogClientDisplayStatus=_SfpsEventLogClientDisplayStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,5,1,1,4),_SfpsEventLogClientDisplayStatus_Type())
sfpsEventLogClientDisplayStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsEventLogClientDisplayStatus.setStatus(_A)
class _SfpsEventLogClientFreezeLogStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_SfpsEventLogClientFreezeLogStatus_Type.__name__=_C
_SfpsEventLogClientFreezeLogStatus_Object=MibTableColumn
sfpsEventLogClientFreezeLogStatus=_SfpsEventLogClientFreezeLogStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,5,1,1,5),_SfpsEventLogClientFreezeLogStatus_Type())
sfpsEventLogClientFreezeLogStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsEventLogClientFreezeLogStatus.setStatus(_A)
class _SfpsEventLogClientFreezeDisplayStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_SfpsEventLogClientFreezeDisplayStatus_Type.__name__=_C
_SfpsEventLogClientFreezeDisplayStatus_Object=MibTableColumn
sfpsEventLogClientFreezeDisplayStatus=_SfpsEventLogClientFreezeDisplayStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,5,1,1,6),_SfpsEventLogClientFreezeDisplayStatus_Type())
sfpsEventLogClientFreezeDisplayStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsEventLogClientFreezeDisplayStatus.setStatus(_A)
class _SfpsEventLogClientErrorLogStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_SfpsEventLogClientErrorLogStatus_Type.__name__=_C
_SfpsEventLogClientErrorLogStatus_Object=MibTableColumn
sfpsEventLogClientErrorLogStatus=_SfpsEventLogClientErrorLogStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,5,1,1,7),_SfpsEventLogClientErrorLogStatus_Type())
sfpsEventLogClientErrorLogStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsEventLogClientErrorLogStatus.setStatus(_A)
class _SfpsEventLogClientErrorDisplayStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_SfpsEventLogClientErrorDisplayStatus_Type.__name__=_C
_SfpsEventLogClientErrorDisplayStatus_Object=MibTableColumn
sfpsEventLogClientErrorDisplayStatus=_SfpsEventLogClientErrorDisplayStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,5,1,1,8),_SfpsEventLogClientErrorDisplayStatus_Type())
sfpsEventLogClientErrorDisplayStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsEventLogClientErrorDisplayStatus.setStatus(_A)
class _SfpsEventLogClientCriticalLogStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_SfpsEventLogClientCriticalLogStatus_Type.__name__=_C
_SfpsEventLogClientCriticalLogStatus_Object=MibTableColumn
sfpsEventLogClientCriticalLogStatus=_SfpsEventLogClientCriticalLogStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,5,1,1,9),_SfpsEventLogClientCriticalLogStatus_Type())
sfpsEventLogClientCriticalLogStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsEventLogClientCriticalLogStatus.setStatus(_A)
class _SfpsEventLogClientCriticalDisplayStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_SfpsEventLogClientCriticalDisplayStatus_Type.__name__=_C
_SfpsEventLogClientCriticalDisplayStatus_Object=MibTableColumn
sfpsEventLogClientCriticalDisplayStatus=_SfpsEventLogClientCriticalDisplayStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,5,1,1,10),_SfpsEventLogClientCriticalDisplayStatus_Type())
sfpsEventLogClientCriticalDisplayStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsEventLogClientCriticalDisplayStatus.setStatus(_A)
class _SfpsEventLogClientInfoLogStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_SfpsEventLogClientInfoLogStatus_Type.__name__=_C
_SfpsEventLogClientInfoLogStatus_Object=MibTableColumn
sfpsEventLogClientInfoLogStatus=_SfpsEventLogClientInfoLogStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,5,1,1,11),_SfpsEventLogClientInfoLogStatus_Type())
sfpsEventLogClientInfoLogStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsEventLogClientInfoLogStatus.setStatus(_A)
class _SfpsEventLogClientInfoDisplayStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_SfpsEventLogClientInfoDisplayStatus_Type.__name__=_C
_SfpsEventLogClientInfoDisplayStatus_Object=MibTableColumn
sfpsEventLogClientInfoDisplayStatus=_SfpsEventLogClientInfoDisplayStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,5,1,1,12),_SfpsEventLogClientInfoDisplayStatus_Type())
sfpsEventLogClientInfoDisplayStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsEventLogClientInfoDisplayStatus.setStatus(_A)
class _SfpsEventLogClientDebugLogStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_SfpsEventLogClientDebugLogStatus_Type.__name__=_C
_SfpsEventLogClientDebugLogStatus_Object=MibTableColumn
sfpsEventLogClientDebugLogStatus=_SfpsEventLogClientDebugLogStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,5,1,1,13),_SfpsEventLogClientDebugLogStatus_Type())
sfpsEventLogClientDebugLogStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsEventLogClientDebugLogStatus.setStatus(_A)
class _SfpsEventLogClientDebugDisplayStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_SfpsEventLogClientDebugDisplayStatus_Type.__name__=_C
_SfpsEventLogClientDebugDisplayStatus_Object=MibTableColumn
sfpsEventLogClientDebugDisplayStatus=_SfpsEventLogClientDebugDisplayStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,5,1,1,14),_SfpsEventLogClientDebugDisplayStatus_Type())
sfpsEventLogClientDebugDisplayStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsEventLogClientDebugDisplayStatus.setStatus(_A)
class _SfpsEventLogClientConfigAPIVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('freezeLog',1),('errorLog',2),('criticalLog',3),('infoLog',4),('debugLog',5),('allLogLevels',6),('allClients',7),('masterLog',8)))
_SfpsEventLogClientConfigAPIVerb_Type.__name__=_C
_SfpsEventLogClientConfigAPIVerb_Object=MibScalar
sfpsEventLogClientConfigAPIVerb=_SfpsEventLogClientConfigAPIVerb_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,5,2,1),_SfpsEventLogClientConfigAPIVerb_Type())
sfpsEventLogClientConfigAPIVerb.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsEventLogClientConfigAPIVerb.setStatus(_A)
class _SfpsEventLogClientConfigAPIAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_SfpsEventLogClientConfigAPIAdminStatus_Type.__name__=_C
_SfpsEventLogClientConfigAPIAdminStatus_Object=MibScalar
sfpsEventLogClientConfigAPIAdminStatus=_SfpsEventLogClientConfigAPIAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,5,2,2),_SfpsEventLogClientConfigAPIAdminStatus_Type())
sfpsEventLogClientConfigAPIAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsEventLogClientConfigAPIAdminStatus.setStatus(_A)
_SfpsEventLogClientConfigAPIClientName_Type=DisplayString
_SfpsEventLogClientConfigAPIClientName_Object=MibScalar
sfpsEventLogClientConfigAPIClientName=_SfpsEventLogClientConfigAPIClientName_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,5,2,3),_SfpsEventLogClientConfigAPIClientName_Type())
sfpsEventLogClientConfigAPIClientName.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsEventLogClientConfigAPIClientName.setStatus(_A)
_SfpsEventLogClientConfigAPIClientID_Type=Integer32
_SfpsEventLogClientConfigAPIClientID_Object=MibScalar
sfpsEventLogClientConfigAPIClientID=_SfpsEventLogClientConfigAPIClientID_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,5,2,4),_SfpsEventLogClientConfigAPIClientID_Type())
sfpsEventLogClientConfigAPIClientID.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsEventLogClientConfigAPIClientID.setStatus(_A)
class _SfpsEventLogClientConfigAPILogDisplay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('logAndDisplay',2),('logOnly',3),('displayOnly',4)))
_SfpsEventLogClientConfigAPILogDisplay_Type.__name__=_C
_SfpsEventLogClientConfigAPILogDisplay_Object=MibScalar
sfpsEventLogClientConfigAPILogDisplay=_SfpsEventLogClientConfigAPILogDisplay_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,5,2,5),_SfpsEventLogClientConfigAPILogDisplay_Type())
sfpsEventLogClientConfigAPILogDisplay.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsEventLogClientConfigAPILogDisplay.setStatus(_A)
class _SfpsTrapAPIVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_G,2),(_F,3),('resetTrapStats',4),('resetAllStats',5)))
_SfpsTrapAPIVerb_Type.__name__=_C
_SfpsTrapAPIVerb_Object=MibScalar
sfpsTrapAPIVerb=_SfpsTrapAPIVerb_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,7,1,1),_SfpsTrapAPIVerb_Type())
sfpsTrapAPIVerb.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsTrapAPIVerb.setStatus(_A)
class _SfpsTrapAPITrapId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1400,1401,1402,1403,1404,1405,1406,1407,1408,1409,1410)));namedValues=NamedValues(*((_M,1400),(_N,1401),(_O,1402),(_P,1403),(_Q,1404),(_R,1405),(_S,1406),(_T,1407),(_U,1408),(_V,1409),(_W,1410)))
_SfpsTrapAPITrapId_Type.__name__=_C
_SfpsTrapAPITrapId_Object=MibScalar
sfpsTrapAPITrapId=_SfpsTrapAPITrapId_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,7,1,2),_SfpsTrapAPITrapId_Type())
sfpsTrapAPITrapId.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsTrapAPITrapId.setStatus(_A)
_SfpsTrapAPITotalSent_Type=Integer32
_SfpsTrapAPITotalSent_Object=MibScalar
sfpsTrapAPITotalSent=_SfpsTrapAPITotalSent_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,7,1,3),_SfpsTrapAPITotalSent_Type())
sfpsTrapAPITotalSent.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTrapAPITotalSent.setStatus(_A)
class _SfpsTrapTableTrapId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1400,1401,1402,1403,1404,1405,1406,1407,1408,1409,1410,1411,1412,1413,1414,1415,1416,1417,1418,1419,1420,1421,1422)));namedValues=NamedValues(*((_M,1400),(_N,1401),(_O,1402),(_P,1403),(_Q,1404),(_R,1405),(_S,1406),(_T,1407),(_U,1408),(_V,1409),(_W,1410),('noSrcVlans',1411),('noDestVlans',1412),('noSrcVlansEnabled',1413),('noDestVlansEnabled',1414),('noCommonSecureVlan',1415),('incVlanUserCount',1416),('decVlanUserCount',1417),('vrrpPrimaryResign',1418),('vrrpPrimaryAged',1419),('vrrpSecondaryUp',1420),('hsrpPrimaryResign',1421),('hsrpSecondaryUp',1422)))
_SfpsTrapTableTrapId_Type.__name__=_C
_SfpsTrapTableTrapId_Object=MibScalar
sfpsTrapTableTrapId=_SfpsTrapTableTrapId_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,7,2,1),_SfpsTrapTableTrapId_Type())
sfpsTrapTableTrapId.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTrapTableTrapId.setStatus(_A)
class _SfpsTrapTableAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_SfpsTrapTableAdminStatus_Type.__name__=_C
_SfpsTrapTableAdminStatus_Object=MibScalar
sfpsTrapTableAdminStatus=_SfpsTrapTableAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,7,2,2),_SfpsTrapTableAdminStatus_Type())
sfpsTrapTableAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTrapTableAdminStatus.setStatus(_A)
_SfpsTrapTableNumSent_Type=Integer32
_SfpsTrapTableNumSent_Object=MibScalar
sfpsTrapTableNumSent=_SfpsTrapTableNumSent_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,7,2,3),_SfpsTrapTableNumSent_Type())
sfpsTrapTableNumSent.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTrapTableNumSent.setStatus(_A)
_SfpsTrapTableLastSent_Type=TimeTicks
_SfpsTrapTableLastSent_Object=MibScalar
sfpsTrapTableLastSent=_SfpsTrapTableLastSent_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,7,2,4),_SfpsTrapTableLastSent_Type())
sfpsTrapTableLastSent.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTrapTableLastSent.setStatus(_A)
_SfpsFragStatsTotalFrags_Type=Integer32
_SfpsFragStatsTotalFrags_Object=MibScalar
sfpsFragStatsTotalFrags=_SfpsFragStatsTotalFrags_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,11,1),_SfpsFragStatsTotalFrags_Type())
sfpsFragStatsTotalFrags.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsFragStatsTotalFrags.setStatus(_A)
_SfpsFragStatsNumLookupFail_Type=Integer32
_SfpsFragStatsNumLookupFail_Object=MibScalar
sfpsFragStatsNumLookupFail=_SfpsFragStatsNumLookupFail_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,11,2),_SfpsFragStatsNumLookupFail_Type())
sfpsFragStatsNumLookupFail.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsFragStatsNumLookupFail.setStatus(_A)
_SfpsFragStatsAvgCompares_Type=OctetString
_SfpsFragStatsAvgCompares_Object=MibScalar
sfpsFragStatsAvgCompares=_SfpsFragStatsAvgCompares_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,11,3),_SfpsFragStatsAvgCompares_Type())
sfpsFragStatsAvgCompares.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsFragStatsAvgCompares.setStatus(_A)
_SfpsFragStatsNumNodes_Type=Integer32
_SfpsFragStatsNumNodes_Object=MibScalar
sfpsFragStatsNumNodes=_SfpsFragStatsNumNodes_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,11,4),_SfpsFragStatsNumNodes_Type())
sfpsFragStatsNumNodes.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsFragStatsNumNodes.setStatus(_A)
_SfpsFragStatsNumUsed_Type=Integer32
_SfpsFragStatsNumUsed_Object=MibScalar
sfpsFragStatsNumUsed=_SfpsFragStatsNumUsed_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,11,5),_SfpsFragStatsNumUsed_Type())
sfpsFragStatsNumUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsFragStatsNumUsed.setStatus(_A)
_SfpsFragStatsMaxNumUsed_Type=Integer32
_SfpsFragStatsMaxNumUsed_Object=MibScalar
sfpsFragStatsMaxNumUsed=_SfpsFragStatsMaxNumUsed_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,11,6),_SfpsFragStatsMaxNumUsed_Type())
sfpsFragStatsMaxNumUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsFragStatsMaxNumUsed.setStatus(_A)
_SfpsFragStatsNumStolen_Type=Integer32
_SfpsFragStatsNumStolen_Object=MibScalar
sfpsFragStatsNumStolen=_SfpsFragStatsNumStolen_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,11,7),_SfpsFragStatsNumStolen_Type())
sfpsFragStatsNumStolen.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsFragStatsNumStolen.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'SfpsSwitchInstance':SfpsSwitchInstance,'HexInteger':HexInteger,'sfpsEventLogStatsTable':sfpsEventLogStatsTable,'sfpsEventLogStatsEntry':sfpsEventLogStatsEntry,_I:sfpsEventLogStatsSwInst,_J:sfpsEventLogWindowStart,'sfpsEventLogIndex':sfpsEventLogIndex,'sfpsEventLogClientName':sfpsEventLogClientName,'sfpsEventLogLevel':sfpsEventLogLevel,'sfpsEventLogMessageString':sfpsEventLogMessageString,'sfpsEventLogTime':sfpsEventLogTime,'sfpsEventLogCallTag':sfpsEventLogCallTag,'sfpsEventLogInfo1':sfpsEventLogInfo1,'sfpsEventLogInfo2':sfpsEventLogInfo2,'sfpsEventLogGenConfigTable':sfpsEventLogGenConfigTable,'sfpsEventLogGenConfigEntry':sfpsEventLogGenConfigEntry,_K:sfpsEventLogGenConfigSwInst,'sfpsEventLogGenConfigWindowStart':sfpsEventLogGenConfigWindowStart,'sfpsEventLogGenConfigLoggingIndex':sfpsEventLogGenConfigLoggingIndex,'sfpsEventLogGenConfigMessageFilter':sfpsEventLogGenConfigMessageFilter,'sfpsEventLogGenConfigCallTagFilter':sfpsEventLogGenConfigCallTagFilter,'sfpsEventLogGenConfigAdminStatus':sfpsEventLogGenConfigAdminStatus,'sfpsEventLogGenConfigOperStatus':sfpsEventLogGenConfigOperStatus,'sfpsEventLogGenConfigOperTime':sfpsEventLogGenConfigOperTime,'sfpsEventLogGenConfigAutoFreeze':sfpsEventLogGenConfigAutoFreeze,'sfpsEventLogGenConfigDisplayWrapDetect':sfpsEventLogGenConfigDisplayWrapDetect,'sfpsEventLogGenConfigAdvertiseAddr':sfpsEventLogGenConfigAdvertiseAddr,'sfpsEventLogClientConfigTable':sfpsEventLogClientConfigTable,'sfpsEventLogClientConfigEntry':sfpsEventLogClientConfigEntry,_L:sfpsEventLogClientConfigId,'sfpsEventLogClientConfigName':sfpsEventLogClientConfigName,'sfpsEventLogClientLogStatus':sfpsEventLogClientLogStatus,'sfpsEventLogClientDisplayStatus':sfpsEventLogClientDisplayStatus,'sfpsEventLogClientFreezeLogStatus':sfpsEventLogClientFreezeLogStatus,'sfpsEventLogClientFreezeDisplayStatus':sfpsEventLogClientFreezeDisplayStatus,'sfpsEventLogClientErrorLogStatus':sfpsEventLogClientErrorLogStatus,'sfpsEventLogClientErrorDisplayStatus':sfpsEventLogClientErrorDisplayStatus,'sfpsEventLogClientCriticalLogStatus':sfpsEventLogClientCriticalLogStatus,'sfpsEventLogClientCriticalDisplayStatus':sfpsEventLogClientCriticalDisplayStatus,'sfpsEventLogClientInfoLogStatus':sfpsEventLogClientInfoLogStatus,'sfpsEventLogClientInfoDisplayStatus':sfpsEventLogClientInfoDisplayStatus,'sfpsEventLogClientDebugLogStatus':sfpsEventLogClientDebugLogStatus,'sfpsEventLogClientDebugDisplayStatus':sfpsEventLogClientDebugDisplayStatus,'sfpsEventLogClientConfigAPIVerb':sfpsEventLogClientConfigAPIVerb,'sfpsEventLogClientConfigAPIAdminStatus':sfpsEventLogClientConfigAPIAdminStatus,'sfpsEventLogClientConfigAPIClientName':sfpsEventLogClientConfigAPIClientName,'sfpsEventLogClientConfigAPIClientID':sfpsEventLogClientConfigAPIClientID,'sfpsEventLogClientConfigAPILogDisplay':sfpsEventLogClientConfigAPILogDisplay,'sfpsTrapAPIVerb':sfpsTrapAPIVerb,'sfpsTrapAPITrapId':sfpsTrapAPITrapId,'sfpsTrapAPITotalSent':sfpsTrapAPITotalSent,'sfpsTrapTableTrapId':sfpsTrapTableTrapId,'sfpsTrapTableAdminStatus':sfpsTrapTableAdminStatus,'sfpsTrapTableNumSent':sfpsTrapTableNumSent,'sfpsTrapTableLastSent':sfpsTrapTableLastSent,'sfpsFragStatsTotalFrags':sfpsFragStatsTotalFrags,'sfpsFragStatsNumLookupFail':sfpsFragStatsNumLookupFail,'sfpsFragStatsAvgCompares':sfpsFragStatsAvgCompares,'sfpsFragStatsNumNodes':sfpsFragStatsNumNodes,'sfpsFragStatsNumUsed':sfpsFragStatsNumUsed,'sfpsFragStatsMaxNumUsed':sfpsFragStatsMaxNumUsed,'sfpsFragStatsNumStolen':sfpsFragStatsNumStolen})