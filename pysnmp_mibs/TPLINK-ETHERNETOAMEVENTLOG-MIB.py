_H='ethernetOamEventLogSeq'
_G='TPLINK-ETHERNETOAMEVENTLOG-MIB'
_F='OctetString'
_E='Integer32'
_D='ifIndex'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ethernetOamEventLog,=mibBuilder.importSymbols('TPLINK-ETHERNETOAM-MIB','ethernetOamEventLog')
_EthernetOamEventLogStatTable_Object=MibTable
ethernetOamEventLogStatTable=_EthernetOamEventLogStatTable_Object((1,3,6,1,4,1,11863,6,60,1,7,1))
if mibBuilder.loadTexts:ethernetOamEventLogStatTable.setStatus(_A)
_EthernetOamEventLogStatEntry_Object=MibTableRow
ethernetOamEventLogStatEntry=_EthernetOamEventLogStatEntry_Object((1,3,6,1,4,1,11863,6,60,1,7,1,1))
ethernetOamEventLogStatEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:ethernetOamEventLogStatEntry.setStatus(_A)
_EthernetOamEventLogStatPort_Type=DisplayString
_EthernetOamEventLogStatPort_Object=MibTableColumn
ethernetOamEventLogStatPort=_EthernetOamEventLogStatPort_Object((1,3,6,1,4,1,11863,6,60,1,7,1,1,1),_EthernetOamEventLogStatPort_Type())
ethernetOamEventLogStatPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamEventLogStatPort.setStatus(_A)
_EthernetOamEventLogStatLocalSymbolPeriod_Type=Counter32
_EthernetOamEventLogStatLocalSymbolPeriod_Object=MibTableColumn
ethernetOamEventLogStatLocalSymbolPeriod=_EthernetOamEventLogStatLocalSymbolPeriod_Object((1,3,6,1,4,1,11863,6,60,1,7,1,1,2),_EthernetOamEventLogStatLocalSymbolPeriod_Type())
ethernetOamEventLogStatLocalSymbolPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamEventLogStatLocalSymbolPeriod.setStatus(_A)
_EthernetOamEventLogStatRemoteSymbolPeriod_Type=Counter32
_EthernetOamEventLogStatRemoteSymbolPeriod_Object=MibTableColumn
ethernetOamEventLogStatRemoteSymbolPeriod=_EthernetOamEventLogStatRemoteSymbolPeriod_Object((1,3,6,1,4,1,11863,6,60,1,7,1,1,3),_EthernetOamEventLogStatRemoteSymbolPeriod_Type())
ethernetOamEventLogStatRemoteSymbolPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamEventLogStatRemoteSymbolPeriod.setStatus(_A)
_EthernetOamEventLogStatLocalFrame_Type=Counter32
_EthernetOamEventLogStatLocalFrame_Object=MibTableColumn
ethernetOamEventLogStatLocalFrame=_EthernetOamEventLogStatLocalFrame_Object((1,3,6,1,4,1,11863,6,60,1,7,1,1,4),_EthernetOamEventLogStatLocalFrame_Type())
ethernetOamEventLogStatLocalFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamEventLogStatLocalFrame.setStatus(_A)
_EthernetOamEventLogStatRemoteFrame_Type=Counter32
_EthernetOamEventLogStatRemoteFrame_Object=MibTableColumn
ethernetOamEventLogStatRemoteFrame=_EthernetOamEventLogStatRemoteFrame_Object((1,3,6,1,4,1,11863,6,60,1,7,1,1,5),_EthernetOamEventLogStatRemoteFrame_Type())
ethernetOamEventLogStatRemoteFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamEventLogStatRemoteFrame.setStatus(_A)
_EthernetOamEventLogStatLocalFramePeriod_Type=Counter32
_EthernetOamEventLogStatLocalFramePeriod_Object=MibTableColumn
ethernetOamEventLogStatLocalFramePeriod=_EthernetOamEventLogStatLocalFramePeriod_Object((1,3,6,1,4,1,11863,6,60,1,7,1,1,6),_EthernetOamEventLogStatLocalFramePeriod_Type())
ethernetOamEventLogStatLocalFramePeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamEventLogStatLocalFramePeriod.setStatus(_A)
_EthernetOamEventLogStatRemoteFramePeriod_Type=Counter32
_EthernetOamEventLogStatRemoteFramePeriod_Object=MibTableColumn
ethernetOamEventLogStatRemoteFramePeriod=_EthernetOamEventLogStatRemoteFramePeriod_Object((1,3,6,1,4,1,11863,6,60,1,7,1,1,7),_EthernetOamEventLogStatRemoteFramePeriod_Type())
ethernetOamEventLogStatRemoteFramePeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamEventLogStatRemoteFramePeriod.setStatus(_A)
_EthernetOamEventLogStatLocalFrameSeconds_Type=Counter32
_EthernetOamEventLogStatLocalFrameSeconds_Object=MibTableColumn
ethernetOamEventLogStatLocalFrameSeconds=_EthernetOamEventLogStatLocalFrameSeconds_Object((1,3,6,1,4,1,11863,6,60,1,7,1,1,8),_EthernetOamEventLogStatLocalFrameSeconds_Type())
ethernetOamEventLogStatLocalFrameSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamEventLogStatLocalFrameSeconds.setStatus(_A)
_EthernetOamEventLogStatRemoteFrameSeconds_Type=Counter32
_EthernetOamEventLogStatRemoteFrameSeconds_Object=MibTableColumn
ethernetOamEventLogStatRemoteFrameSeconds=_EthernetOamEventLogStatRemoteFrameSeconds_Object((1,3,6,1,4,1,11863,6,60,1,7,1,1,9),_EthernetOamEventLogStatRemoteFrameSeconds_Type())
ethernetOamEventLogStatRemoteFrameSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamEventLogStatRemoteFrameSeconds.setStatus(_A)
_EthernetOamEventLogStatLocalDyingGasp_Type=Counter32
_EthernetOamEventLogStatLocalDyingGasp_Object=MibTableColumn
ethernetOamEventLogStatLocalDyingGasp=_EthernetOamEventLogStatLocalDyingGasp_Object((1,3,6,1,4,1,11863,6,60,1,7,1,1,10),_EthernetOamEventLogStatLocalDyingGasp_Type())
ethernetOamEventLogStatLocalDyingGasp.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamEventLogStatLocalDyingGasp.setStatus(_A)
_EthernetOamEventLogStatRemoteDyingGasp_Type=Counter32
_EthernetOamEventLogStatRemoteDyingGasp_Object=MibTableColumn
ethernetOamEventLogStatRemoteDyingGasp=_EthernetOamEventLogStatRemoteDyingGasp_Object((1,3,6,1,4,1,11863,6,60,1,7,1,1,11),_EthernetOamEventLogStatRemoteDyingGasp_Type())
ethernetOamEventLogStatRemoteDyingGasp.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamEventLogStatRemoteDyingGasp.setStatus(_A)
_EthernetOamEventLogStatLocalCriticalEvent_Type=Counter32
_EthernetOamEventLogStatLocalCriticalEvent_Object=MibTableColumn
ethernetOamEventLogStatLocalCriticalEvent=_EthernetOamEventLogStatLocalCriticalEvent_Object((1,3,6,1,4,1,11863,6,60,1,7,1,1,12),_EthernetOamEventLogStatLocalCriticalEvent_Type())
ethernetOamEventLogStatLocalCriticalEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamEventLogStatLocalCriticalEvent.setStatus(_A)
_EthernetOamEventLogStatRemoteCriticalEvent_Type=Counter32
_EthernetOamEventLogStatRemoteCriticalEvent_Object=MibTableColumn
ethernetOamEventLogStatRemoteCriticalEvent=_EthernetOamEventLogStatRemoteCriticalEvent_Object((1,3,6,1,4,1,11863,6,60,1,7,1,1,13),_EthernetOamEventLogStatRemoteCriticalEvent_Type())
ethernetOamEventLogStatRemoteCriticalEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamEventLogStatRemoteCriticalEvent.setStatus(_A)
_EthernetOamEventLogTable_Object=MibTable
ethernetOamEventLogTable=_EthernetOamEventLogTable_Object((1,3,6,1,4,1,11863,6,60,1,7,2))
if mibBuilder.loadTexts:ethernetOamEventLogTable.setStatus(_A)
_EthernetOamEventLogEntry_Object=MibTableRow
ethernetOamEventLogEntry=_EthernetOamEventLogEntry_Object((1,3,6,1,4,1,11863,6,60,1,7,2,1))
ethernetOamEventLogEntry.setIndexNames((0,_C,_D),(0,_G,_H))
if mibBuilder.loadTexts:ethernetOamEventLogEntry.setStatus(_A)
_EthernetOamEventLogPort_Type=DisplayString
_EthernetOamEventLogPort_Object=MibTableColumn
ethernetOamEventLogPort=_EthernetOamEventLogPort_Object((1,3,6,1,4,1,11863,6,60,1,7,2,1,1),_EthernetOamEventLogPort_Type())
ethernetOamEventLogPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamEventLogPort.setStatus(_A)
_EthernetOamEventLogSeq_Type=Integer32
_EthernetOamEventLogSeq_Object=MibTableColumn
ethernetOamEventLogSeq=_EthernetOamEventLogSeq_Object((1,3,6,1,4,1,11863,6,60,1,7,2,1,2),_EthernetOamEventLogSeq_Type())
ethernetOamEventLogSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamEventLogSeq.setStatus(_A)
class _EthernetOamEventLogType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,16,32,48)));namedValues=NamedValues(*(('symbol-period',1),('frame',2),('frame-period',3),('frame-seconds',4),('link-fault',16),('dying-gasp',32),('critical-event',48)))
_EthernetOamEventLogType_Type.__name__=_E
_EthernetOamEventLogType_Object=MibTableColumn
ethernetOamEventLogType=_EthernetOamEventLogType_Object((1,3,6,1,4,1,11863,6,60,1,7,2,1,3),_EthernetOamEventLogType_Type())
ethernetOamEventLogType.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamEventLogType.setStatus(_A)
class _EthernetOamEventLogLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('local',0),('remote',1)))
_EthernetOamEventLogLocation_Type.__name__=_E
_EthernetOamEventLogLocation_Object=MibTableColumn
ethernetOamEventLogLocation=_EthernetOamEventLogLocation_Object((1,3,6,1,4,1,11863,6,60,1,7,2,1,4),_EthernetOamEventLogLocation_Type())
ethernetOamEventLogLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamEventLogLocation.setStatus(_A)
class _EthernetOamEventLogTimestamp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_EthernetOamEventLogTimestamp_Type.__name__=_F
_EthernetOamEventLogTimestamp_Object=MibTableColumn
ethernetOamEventLogTimestamp=_EthernetOamEventLogTimestamp_Object((1,3,6,1,4,1,11863,6,60,1,7,2,1,5),_EthernetOamEventLogTimestamp_Type())
ethernetOamEventLogTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamEventLogTimestamp.setStatus(_A)
_EthernetOamEventLogValue_Type=Counter32
_EthernetOamEventLogValue_Object=MibTableColumn
ethernetOamEventLogValue=_EthernetOamEventLogValue_Object((1,3,6,1,4,1,11863,6,60,1,7,2,1,6),_EthernetOamEventLogValue_Type())
ethernetOamEventLogValue.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamEventLogValue.setStatus(_A)
_EthernetOamEventLogWindow_Type=Counter32
_EthernetOamEventLogWindow_Object=MibTableColumn
ethernetOamEventLogWindow=_EthernetOamEventLogWindow_Object((1,3,6,1,4,1,11863,6,60,1,7,2,1,7),_EthernetOamEventLogWindow_Type())
ethernetOamEventLogWindow.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamEventLogWindow.setStatus(_A)
_EthernetOamEventLogThreshold_Type=Counter32
_EthernetOamEventLogThreshold_Object=MibTableColumn
ethernetOamEventLogThreshold=_EthernetOamEventLogThreshold_Object((1,3,6,1,4,1,11863,6,60,1,7,2,1,8),_EthernetOamEventLogThreshold_Type())
ethernetOamEventLogThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamEventLogThreshold.setStatus(_A)
_EthernetOamEventLogAccumulatedErr_Type=Counter64
_EthernetOamEventLogAccumulatedErr_Object=MibTableColumn
ethernetOamEventLogAccumulatedErr=_EthernetOamEventLogAccumulatedErr_Object((1,3,6,1,4,1,11863,6,60,1,7,2,1,9),_EthernetOamEventLogAccumulatedErr_Type())
ethernetOamEventLogAccumulatedErr.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamEventLogAccumulatedErr.setStatus(_A)
_EthernetOamEventLogClearTable_Object=MibTable
ethernetOamEventLogClearTable=_EthernetOamEventLogClearTable_Object((1,3,6,1,4,1,11863,6,60,1,7,3))
if mibBuilder.loadTexts:ethernetOamEventLogClearTable.setStatus(_A)
_EthernetOamEventLogClearEntry_Object=MibTableRow
ethernetOamEventLogClearEntry=_EthernetOamEventLogClearEntry_Object((1,3,6,1,4,1,11863,6,60,1,7,3,1))
ethernetOamEventLogClearEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:ethernetOamEventLogClearEntry.setStatus(_A)
_EthernetOamEventLogClearPort_Type=DisplayString
_EthernetOamEventLogClearPort_Object=MibTableColumn
ethernetOamEventLogClearPort=_EthernetOamEventLogClearPort_Object((1,3,6,1,4,1,11863,6,60,1,7,3,1,1),_EthernetOamEventLogClearPort_Type())
ethernetOamEventLogClearPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamEventLogClearPort.setStatus(_A)
class _EthernetOamEventLogClearAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unchange',0),('clear',1)))
_EthernetOamEventLogClearAction_Type.__name__=_E
_EthernetOamEventLogClearAction_Object=MibTableColumn
ethernetOamEventLogClearAction=_EthernetOamEventLogClearAction_Object((1,3,6,1,4,1,11863,6,60,1,7,3,1,2),_EthernetOamEventLogClearAction_Type())
ethernetOamEventLogClearAction.setMaxAccess('read-write')
if mibBuilder.loadTexts:ethernetOamEventLogClearAction.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'ethernetOamEventLogStatTable':ethernetOamEventLogStatTable,'ethernetOamEventLogStatEntry':ethernetOamEventLogStatEntry,'ethernetOamEventLogStatPort':ethernetOamEventLogStatPort,'ethernetOamEventLogStatLocalSymbolPeriod':ethernetOamEventLogStatLocalSymbolPeriod,'ethernetOamEventLogStatRemoteSymbolPeriod':ethernetOamEventLogStatRemoteSymbolPeriod,'ethernetOamEventLogStatLocalFrame':ethernetOamEventLogStatLocalFrame,'ethernetOamEventLogStatRemoteFrame':ethernetOamEventLogStatRemoteFrame,'ethernetOamEventLogStatLocalFramePeriod':ethernetOamEventLogStatLocalFramePeriod,'ethernetOamEventLogStatRemoteFramePeriod':ethernetOamEventLogStatRemoteFramePeriod,'ethernetOamEventLogStatLocalFrameSeconds':ethernetOamEventLogStatLocalFrameSeconds,'ethernetOamEventLogStatRemoteFrameSeconds':ethernetOamEventLogStatRemoteFrameSeconds,'ethernetOamEventLogStatLocalDyingGasp':ethernetOamEventLogStatLocalDyingGasp,'ethernetOamEventLogStatRemoteDyingGasp':ethernetOamEventLogStatRemoteDyingGasp,'ethernetOamEventLogStatLocalCriticalEvent':ethernetOamEventLogStatLocalCriticalEvent,'ethernetOamEventLogStatRemoteCriticalEvent':ethernetOamEventLogStatRemoteCriticalEvent,'ethernetOamEventLogTable':ethernetOamEventLogTable,'ethernetOamEventLogEntry':ethernetOamEventLogEntry,'ethernetOamEventLogPort':ethernetOamEventLogPort,_H:ethernetOamEventLogSeq,'ethernetOamEventLogType':ethernetOamEventLogType,'ethernetOamEventLogLocation':ethernetOamEventLogLocation,'ethernetOamEventLogTimestamp':ethernetOamEventLogTimestamp,'ethernetOamEventLogValue':ethernetOamEventLogValue,'ethernetOamEventLogWindow':ethernetOamEventLogWindow,'ethernetOamEventLogThreshold':ethernetOamEventLogThreshold,'ethernetOamEventLogAccumulatedErr':ethernetOamEventLogAccumulatedErr,'ethernetOamEventLogClearTable':ethernetOamEventLogClearTable,'ethernetOamEventLogClearEntry':ethernetOamEventLogClearEntry,'ethernetOamEventLogClearPort':ethernetOamEventLogClearPort,'ethernetOamEventLogClearAction':ethernetOamEventLogClearAction})