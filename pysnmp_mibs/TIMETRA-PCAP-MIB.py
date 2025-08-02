_d='tmnxPcapSessionNotifGroupV16v0'
_c='tmnxPcapSessionGroupV16v0'
_b='tmnxPcapSoftwareFailure'
_a='tmnxPcapBufferReadWriteFailure'
_Z='tmnxPcapBufferFull'
_Y='tmnxPcapFileError'
_X='tmnxPcapSessionProcTimeBailouts'
_W='tmnxPcapSessionLastFileWriteTime'
_V='tmnxPcapSessionFileSize'
_U='tmnxPcapSessionCapture'
_T='tmnxPcapSessionFileUrl'
_S='tmnxPcapSessionEntryLastChanged'
_R='tmnxPcapSessionRowStatus'
_Q='tmnxPcapSessionTableLastChanged'
_P='tmnxPcapSessionStatsEntry'
_O='tmnxPcapSessionName'
_N='tmnxPcapApplicationName'
_M='tmnxPcapApplicationType'
_L='TmnxDisplayStringURL'
_K='tmnxPcapSessionDroppedPackets'
_J='tmnxPcapSessionBufReadFailures'
_I='tmnxPcapSessionBufWriteFailures'
_H='tmnxPcapSessionBufferSize'
_G='read-create'
_F='not-accessible'
_E='tmnxPcapSessionState'
_D='Integer32'
_C='read-only'
_B='current'
_A='TIMETRA-PCAP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
TLNamedItemOrEmpty,TNamedItemOrEmpty,TmnxDisplayStringURL=mibBuilder.importSymbols('TIMETRA-TC-MIB','TLNamedItemOrEmpty','TNamedItemOrEmpty',_L)
timetraPcapMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,119))
if mibBuilder.loadTexts:timetraPcapMIBModule.setRevisions(('2017-10-17 00:00',))
_TmnxPcapConformance_ObjectIdentity=ObjectIdentity
tmnxPcapConformance=_TmnxPcapConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,119))
_TmnxPcapCompliances_ObjectIdentity=ObjectIdentity
tmnxPcapCompliances=_TmnxPcapCompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,119,1))
_TmnxPcapGroups_ObjectIdentity=ObjectIdentity
tmnxPcapGroups=_TmnxPcapGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,119,2))
_TmnxPcapObjects_ObjectIdentity=ObjectIdentity
tmnxPcapObjects=_TmnxPcapObjects_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,119))
_TmnxPcapConfigTimestamps_ObjectIdentity=ObjectIdentity
tmnxPcapConfigTimestamps=_TmnxPcapConfigTimestamps_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,119,1))
_TmnxPcapSessionTableLastChanged_Type=TimeStamp
_TmnxPcapSessionTableLastChanged_Object=MibScalar
tmnxPcapSessionTableLastChanged=_TmnxPcapSessionTableLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,119,1,1),_TmnxPcapSessionTableLastChanged_Type())
tmnxPcapSessionTableLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPcapSessionTableLastChanged.setStatus(_B)
_TmnxPcapConfigurations_ObjectIdentity=ObjectIdentity
tmnxPcapConfigurations=_TmnxPcapConfigurations_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,119,2))
_TmnxPcapSessionTable_Object=MibTable
tmnxPcapSessionTable=_TmnxPcapSessionTable_Object((1,3,6,1,4,1,6527,3,1,2,119,2,1))
if mibBuilder.loadTexts:tmnxPcapSessionTable.setStatus(_B)
_TmnxPcapSessionEntry_Object=MibTableRow
tmnxPcapSessionEntry=_TmnxPcapSessionEntry_Object((1,3,6,1,4,1,6527,3,1,2,119,2,1,1))
tmnxPcapSessionEntry.setIndexNames((0,_A,_M),(0,_A,_N),(0,_A,_O))
if mibBuilder.loadTexts:tmnxPcapSessionEntry.setStatus(_B)
class _TmnxPcapApplicationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('mirror-dest',1))
_TmnxPcapApplicationType_Type.__name__=_D
_TmnxPcapApplicationType_Object=MibTableColumn
tmnxPcapApplicationType=_TmnxPcapApplicationType_Object((1,3,6,1,4,1,6527,3,1,2,119,2,1,1,1),_TmnxPcapApplicationType_Type())
tmnxPcapApplicationType.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxPcapApplicationType.setStatus(_B)
_TmnxPcapApplicationName_Type=TLNamedItemOrEmpty
_TmnxPcapApplicationName_Object=MibTableColumn
tmnxPcapApplicationName=_TmnxPcapApplicationName_Object((1,3,6,1,4,1,6527,3,1,2,119,2,1,1,2),_TmnxPcapApplicationName_Type())
tmnxPcapApplicationName.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxPcapApplicationName.setStatus(_B)
_TmnxPcapSessionName_Type=TNamedItemOrEmpty
_TmnxPcapSessionName_Object=MibTableColumn
tmnxPcapSessionName=_TmnxPcapSessionName_Object((1,3,6,1,4,1,6527,3,1,2,119,2,1,1,3),_TmnxPcapSessionName_Type())
tmnxPcapSessionName.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxPcapSessionName.setStatus(_B)
_TmnxPcapSessionRowStatus_Type=RowStatus
_TmnxPcapSessionRowStatus_Object=MibTableColumn
tmnxPcapSessionRowStatus=_TmnxPcapSessionRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,119,2,1,1,4),_TmnxPcapSessionRowStatus_Type())
tmnxPcapSessionRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxPcapSessionRowStatus.setStatus(_B)
_TmnxPcapSessionEntryLastChanged_Type=TimeStamp
_TmnxPcapSessionEntryLastChanged_Object=MibTableColumn
tmnxPcapSessionEntryLastChanged=_TmnxPcapSessionEntryLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,119,2,1,1,5),_TmnxPcapSessionEntryLastChanged_Type())
tmnxPcapSessionEntryLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPcapSessionEntryLastChanged.setStatus(_B)
class _TmnxPcapSessionFileUrl_Type(TmnxDisplayStringURL):defaultHexValue=''
_TmnxPcapSessionFileUrl_Type.__name__=_L
_TmnxPcapSessionFileUrl_Object=MibTableColumn
tmnxPcapSessionFileUrl=_TmnxPcapSessionFileUrl_Object((1,3,6,1,4,1,6527,3,1,2,119,2,1,1,6),_TmnxPcapSessionFileUrl_Type())
tmnxPcapSessionFileUrl.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxPcapSessionFileUrl.setStatus(_B)
class _TmnxPcapSessionCapture_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('stop',2)))
_TmnxPcapSessionCapture_Type.__name__=_D
_TmnxPcapSessionCapture_Object=MibTableColumn
tmnxPcapSessionCapture=_TmnxPcapSessionCapture_Object((1,3,6,1,4,1,6527,3,1,2,119,2,1,1,7),_TmnxPcapSessionCapture_Type())
tmnxPcapSessionCapture.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxPcapSessionCapture.setStatus(_B)
class _TmnxPcapSessionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('failed',0),('init',1),('ready',2),('start',3),('in-progress',4),('stopped',5),('file-error',6),('buffer-full',7),('buffer-high-watermark',8)))
_TmnxPcapSessionState_Type.__name__=_D
_TmnxPcapSessionState_Object=MibTableColumn
tmnxPcapSessionState=_TmnxPcapSessionState_Object((1,3,6,1,4,1,6527,3,1,2,119,2,1,1,8),_TmnxPcapSessionState_Type())
tmnxPcapSessionState.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPcapSessionState.setStatus(_B)
_TmnxPcapStatistics_ObjectIdentity=ObjectIdentity
tmnxPcapStatistics=_TmnxPcapStatistics_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,119,3))
_TmnxPcapSessionStatsTable_Object=MibTable
tmnxPcapSessionStatsTable=_TmnxPcapSessionStatsTable_Object((1,3,6,1,4,1,6527,3,1,2,119,3,1))
if mibBuilder.loadTexts:tmnxPcapSessionStatsTable.setStatus(_B)
_TmnxPcapSessionStatsEntry_Object=MibTableRow
tmnxPcapSessionStatsEntry=_TmnxPcapSessionStatsEntry_Object((1,3,6,1,4,1,6527,3,1,2,119,3,1,1))
if mibBuilder.loadTexts:tmnxPcapSessionStatsEntry.setStatus(_B)
_TmnxPcapSessionBufferSize_Type=Unsigned32
_TmnxPcapSessionBufferSize_Object=MibTableColumn
tmnxPcapSessionBufferSize=_TmnxPcapSessionBufferSize_Object((1,3,6,1,4,1,6527,3,1,2,119,3,1,1,1),_TmnxPcapSessionBufferSize_Type())
tmnxPcapSessionBufferSize.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPcapSessionBufferSize.setStatus(_B)
if mibBuilder.loadTexts:tmnxPcapSessionBufferSize.setUnits('bytes')
_TmnxPcapSessionFileSize_Type=Unsigned32
_TmnxPcapSessionFileSize_Object=MibTableColumn
tmnxPcapSessionFileSize=_TmnxPcapSessionFileSize_Object((1,3,6,1,4,1,6527,3,1,2,119,3,1,1,2),_TmnxPcapSessionFileSize_Type())
tmnxPcapSessionFileSize.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPcapSessionFileSize.setStatus(_B)
if mibBuilder.loadTexts:tmnxPcapSessionFileSize.setUnits('bytes')
_TmnxPcapSessionLastFileWriteTime_Type=TimeStamp
_TmnxPcapSessionLastFileWriteTime_Object=MibTableColumn
tmnxPcapSessionLastFileWriteTime=_TmnxPcapSessionLastFileWriteTime_Object((1,3,6,1,4,1,6527,3,1,2,119,3,1,1,3),_TmnxPcapSessionLastFileWriteTime_Type())
tmnxPcapSessionLastFileWriteTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPcapSessionLastFileWriteTime.setStatus(_B)
_TmnxPcapSessionBufWriteFailures_Type=Unsigned32
_TmnxPcapSessionBufWriteFailures_Object=MibTableColumn
tmnxPcapSessionBufWriteFailures=_TmnxPcapSessionBufWriteFailures_Object((1,3,6,1,4,1,6527,3,1,2,119,3,1,1,4),_TmnxPcapSessionBufWriteFailures_Type())
tmnxPcapSessionBufWriteFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPcapSessionBufWriteFailures.setStatus(_B)
_TmnxPcapSessionBufReadFailures_Type=Unsigned32
_TmnxPcapSessionBufReadFailures_Object=MibTableColumn
tmnxPcapSessionBufReadFailures=_TmnxPcapSessionBufReadFailures_Object((1,3,6,1,4,1,6527,3,1,2,119,3,1,1,5),_TmnxPcapSessionBufReadFailures_Type())
tmnxPcapSessionBufReadFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPcapSessionBufReadFailures.setStatus(_B)
_TmnxPcapSessionDroppedPackets_Type=Unsigned32
_TmnxPcapSessionDroppedPackets_Object=MibTableColumn
tmnxPcapSessionDroppedPackets=_TmnxPcapSessionDroppedPackets_Object((1,3,6,1,4,1,6527,3,1,2,119,3,1,1,6),_TmnxPcapSessionDroppedPackets_Type())
tmnxPcapSessionDroppedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPcapSessionDroppedPackets.setStatus(_B)
if mibBuilder.loadTexts:tmnxPcapSessionDroppedPackets.setUnits('packets')
_TmnxPcapSessionProcTimeBailouts_Type=Unsigned32
_TmnxPcapSessionProcTimeBailouts_Object=MibTableColumn
tmnxPcapSessionProcTimeBailouts=_TmnxPcapSessionProcTimeBailouts_Object((1,3,6,1,4,1,6527,3,1,2,119,3,1,1,7),_TmnxPcapSessionProcTimeBailouts_Type())
tmnxPcapSessionProcTimeBailouts.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPcapSessionProcTimeBailouts.setStatus(_B)
_TmnxPcapNotifyPrefix_ObjectIdentity=ObjectIdentity
tmnxPcapNotifyPrefix=_TmnxPcapNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,119))
_TmnxPcapNofitications_ObjectIdentity=ObjectIdentity
tmnxPcapNofitications=_TmnxPcapNofitications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,119,1))
tmnxPcapSessionEntry.registerAugmentions((_A,_P))
tmnxPcapSessionStatsEntry.setIndexNames(*tmnxPcapSessionEntry.getIndexNames())
tmnxPcapSessionGroupV16v0=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,119,2,1))
tmnxPcapSessionGroupV16v0.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_E),(_A,_H),(_A,_V),(_A,_W),(_A,_I),(_A,_J),(_A,_K),(_A,_X)))
if mibBuilder.loadTexts:tmnxPcapSessionGroupV16v0.setStatus(_B)
tmnxPcapFileError=NotificationType((1,3,6,1,4,1,6527,3,1,3,119,1,1))
tmnxPcapFileError.setObjects((_A,_E))
if mibBuilder.loadTexts:tmnxPcapFileError.setStatus(_B)
tmnxPcapBufferFull=NotificationType((1,3,6,1,4,1,6527,3,1,3,119,1,2))
tmnxPcapBufferFull.setObjects(*((_A,_H),(_A,_K)))
if mibBuilder.loadTexts:tmnxPcapBufferFull.setStatus(_B)
tmnxPcapBufferReadWriteFailure=NotificationType((1,3,6,1,4,1,6527,3,1,3,119,1,3))
tmnxPcapBufferReadWriteFailure.setObjects(*((_A,_J),(_A,_I)))
if mibBuilder.loadTexts:tmnxPcapBufferReadWriteFailure.setStatus(_B)
tmnxPcapSoftwareFailure=NotificationType((1,3,6,1,4,1,6527,3,1,3,119,1,4))
tmnxPcapSoftwareFailure.setObjects((_A,_E))
if mibBuilder.loadTexts:tmnxPcapSoftwareFailure.setStatus(_B)
tmnxPcapSessionNotifGroupV16v0=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,119,2,2))
tmnxPcapSessionNotifGroupV16v0.setObjects(*((_A,_Y),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:tmnxPcapSessionNotifGroupV16v0.setStatus(_B)
tmnxPcapComplianceV16v0=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,119,1,1))
tmnxPcapComplianceV16v0.setObjects(*((_A,_c),(_A,_d)))
if mibBuilder.loadTexts:tmnxPcapComplianceV16v0.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'timetraPcapMIBModule':timetraPcapMIBModule,'tmnxPcapConformance':tmnxPcapConformance,'tmnxPcapCompliances':tmnxPcapCompliances,'tmnxPcapComplianceV16v0':tmnxPcapComplianceV16v0,'tmnxPcapGroups':tmnxPcapGroups,_c:tmnxPcapSessionGroupV16v0,_d:tmnxPcapSessionNotifGroupV16v0,'tmnxPcapObjects':tmnxPcapObjects,'tmnxPcapConfigTimestamps':tmnxPcapConfigTimestamps,_Q:tmnxPcapSessionTableLastChanged,'tmnxPcapConfigurations':tmnxPcapConfigurations,'tmnxPcapSessionTable':tmnxPcapSessionTable,'tmnxPcapSessionEntry':tmnxPcapSessionEntry,_M:tmnxPcapApplicationType,_N:tmnxPcapApplicationName,_O:tmnxPcapSessionName,_R:tmnxPcapSessionRowStatus,_S:tmnxPcapSessionEntryLastChanged,_T:tmnxPcapSessionFileUrl,_U:tmnxPcapSessionCapture,_E:tmnxPcapSessionState,'tmnxPcapStatistics':tmnxPcapStatistics,'tmnxPcapSessionStatsTable':tmnxPcapSessionStatsTable,_P:tmnxPcapSessionStatsEntry,_H:tmnxPcapSessionBufferSize,_V:tmnxPcapSessionFileSize,_W:tmnxPcapSessionLastFileWriteTime,_I:tmnxPcapSessionBufWriteFailures,_J:tmnxPcapSessionBufReadFailures,_K:tmnxPcapSessionDroppedPackets,_X:tmnxPcapSessionProcTimeBailouts,'tmnxPcapNotifyPrefix':tmnxPcapNotifyPrefix,'tmnxPcapNofitications':tmnxPcapNofitications,_Y:tmnxPcapFileError,_Z:tmnxPcapBufferFull,_a:tmnxPcapBufferReadWriteFailure,_b:tmnxPcapSoftwareFailure})