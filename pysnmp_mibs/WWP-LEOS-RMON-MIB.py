_J='wwpLeosRmonHistoryIndex'
_I='enable'
_H='disable'
_G='wwpLeosRmonFileIndex'
_F='WWP-LEOS-RMON-MIB'
_E='read-only'
_D='DisplayString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention','TruthValue')
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosRmonMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,41))
if mibBuilder.loadTexts:wwpLeosRmonMIB.setRevisions(('2012-06-27 00:00','2011-08-01 17:00','2010-06-20 17:00'))
_WwpLeosRmonMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosRmonMIBObjects=_WwpLeosRmonMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,41,1))
_WwpLeosRmon_ObjectIdentity=ObjectIdentity
wwpLeosRmon=_WwpLeosRmon_ObjectIdentity((1,3,6,1,4,1,6141,2,60,41,1,1))
_WwpLeosRmonFileTable_Object=MibTable
wwpLeosRmonFileTable=_WwpLeosRmonFileTable_Object((1,3,6,1,4,1,6141,2,60,41,1,1,1))
if mibBuilder.loadTexts:wwpLeosRmonFileTable.setStatus(_A)
_WwpLeosRmonFileEntry_Object=MibTableRow
wwpLeosRmonFileEntry=_WwpLeosRmonFileEntry_Object((1,3,6,1,4,1,6141,2,60,41,1,1,1,1))
wwpLeosRmonFileEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:wwpLeosRmonFileEntry.setStatus(_A)
class _WwpLeosRmonFileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_WwpLeosRmonFileIndex_Type.__name__=_C
_WwpLeosRmonFileIndex_Object=MibTableColumn
wwpLeosRmonFileIndex=_WwpLeosRmonFileIndex_Object((1,3,6,1,4,1,6141,2,60,41,1,1,1,1,1),_WwpLeosRmonFileIndex_Type())
wwpLeosRmonFileIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosRmonFileIndex.setStatus(_A)
class _WwpLeosRmonFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_WwpLeosRmonFileName_Type.__name__=_D
_WwpLeosRmonFileName_Object=MibTableColumn
wwpLeosRmonFileName=_WwpLeosRmonFileName_Object((1,3,6,1,4,1,6141,2,60,41,1,1,1,1,2),_WwpLeosRmonFileName_Type())
wwpLeosRmonFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRmonFileName.setStatus(_A)
class _WwpLeosRmonFileRemoteDir_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_WwpLeosRmonFileRemoteDir_Type.__name__=_D
_WwpLeosRmonFileRemoteDir_Object=MibTableColumn
wwpLeosRmonFileRemoteDir=_WwpLeosRmonFileRemoteDir_Object((1,3,6,1,4,1,6141,2,60,41,1,1,1,1,3),_WwpLeosRmonFileRemoteDir_Type())
wwpLeosRmonFileRemoteDir.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRmonFileRemoteDir.setStatus(_A)
class _WwpLeosRmonFileServer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WwpLeosRmonFileServer_Type.__name__=_D
_WwpLeosRmonFileServer_Object=MibTableColumn
wwpLeosRmonFileServer=_WwpLeosRmonFileServer_Object((1,3,6,1,4,1,6141,2,60,41,1,1,1,1,4),_WwpLeosRmonFileServer_Type())
wwpLeosRmonFileServer.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRmonFileServer.setStatus(_A)
class _WwpLeosRmonFileInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3600,65535))
_WwpLeosRmonFileInterval_Type.__name__=_C
_WwpLeosRmonFileInterval_Object=MibTableColumn
wwpLeosRmonFileInterval=_WwpLeosRmonFileInterval_Object((1,3,6,1,4,1,6141,2,60,41,1,1,1,1,5),_WwpLeosRmonFileInterval_Type())
wwpLeosRmonFileInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRmonFileInterval.setStatus(_A)
_WwpLeosRmonFilePushLastFile_Type=TruthValue
_WwpLeosRmonFilePushLastFile_Object=MibTableColumn
wwpLeosRmonFilePushLastFile=_WwpLeosRmonFilePushLastFile_Object((1,3,6,1,4,1,6141,2,60,41,1,1,1,1,6),_WwpLeosRmonFilePushLastFile_Type())
wwpLeosRmonFilePushLastFile.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRmonFilePushLastFile.setStatus(_A)
class _WwpLeosRmonFileState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_WwpLeosRmonFileState_Type.__name__=_C
_WwpLeosRmonFileState_Object=MibTableColumn
wwpLeosRmonFileState=_WwpLeosRmonFileState_Object((1,3,6,1,4,1,6141,2,60,41,1,1,1,1,7),_WwpLeosRmonFileState_Type())
wwpLeosRmonFileState.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRmonFileState.setStatus(_A)
class _WwpLeosRmonFileLastRemoteName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_WwpLeosRmonFileLastRemoteName_Type.__name__=_D
_WwpLeosRmonFileLastRemoteName_Object=MibTableColumn
wwpLeosRmonFileLastRemoteName=_WwpLeosRmonFileLastRemoteName_Object((1,3,6,1,4,1,6141,2,60,41,1,1,1,1,8),_WwpLeosRmonFileLastRemoteName_Type())
wwpLeosRmonFileLastRemoteName.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosRmonFileLastRemoteName.setStatus(_A)
class _WwpLeosRmonFileLastPushTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WwpLeosRmonFileLastPushTime_Type.__name__=_D
_WwpLeosRmonFileLastPushTime_Object=MibTableColumn
wwpLeosRmonFileLastPushTime=_WwpLeosRmonFileLastPushTime_Object((1,3,6,1,4,1,6141,2,60,41,1,1,1,1,9),_WwpLeosRmonFileLastPushTime_Type())
wwpLeosRmonFileLastPushTime.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosRmonFileLastPushTime.setStatus(_A)
class _WwpLeosRmonFileLastPushStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_WwpLeosRmonFileLastPushStatus_Type.__name__=_D
_WwpLeosRmonFileLastPushStatus_Object=MibTableColumn
wwpLeosRmonFileLastPushStatus=_WwpLeosRmonFileLastPushStatus_Object((1,3,6,1,4,1,6141,2,60,41,1,1,1,1,10),_WwpLeosRmonFileLastPushStatus_Type())
wwpLeosRmonFileLastPushStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosRmonFileLastPushStatus.setStatus(_A)
class _WwpLeosRmonFileUserFilesKept_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_WwpLeosRmonFileUserFilesKept_Type.__name__=_C
_WwpLeosRmonFileUserFilesKept_Object=MibTableColumn
wwpLeosRmonFileUserFilesKept=_WwpLeosRmonFileUserFilesKept_Object((1,3,6,1,4,1,6141,2,60,41,1,1,1,1,11),_WwpLeosRmonFileUserFilesKept_Type())
wwpLeosRmonFileUserFilesKept.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRmonFileUserFilesKept.setStatus(_A)
class _WwpLeosRmonFileMaxFiles_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_WwpLeosRmonFileMaxFiles_Type.__name__=_C
_WwpLeosRmonFileMaxFiles_Object=MibTableColumn
wwpLeosRmonFileMaxFiles=_WwpLeosRmonFileMaxFiles_Object((1,3,6,1,4,1,6141,2,60,41,1,1,1,1,12),_WwpLeosRmonFileMaxFiles_Type())
wwpLeosRmonFileMaxFiles.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosRmonFileMaxFiles.setStatus(_A)
class _WwpLeosRmonFileXftpTransferMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('tftp',1),('ftp',2),('sftp',3),('defaultTftp',4),('defaultFtp',5),('defaultSftp',6),('default',7)))
_WwpLeosRmonFileXftpTransferMode_Type.__name__=_C
_WwpLeosRmonFileXftpTransferMode_Object=MibTableColumn
wwpLeosRmonFileXftpTransferMode=_WwpLeosRmonFileXftpTransferMode_Object((1,3,6,1,4,1,6141,2,60,41,1,1,1,1,13),_WwpLeosRmonFileXftpTransferMode_Type())
wwpLeosRmonFileXftpTransferMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRmonFileXftpTransferMode.setStatus(_A)
class _WwpLeosRmonFileXftpLoginId_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WwpLeosRmonFileXftpLoginId_Type.__name__=_D
_WwpLeosRmonFileXftpLoginId_Object=MibTableColumn
wwpLeosRmonFileXftpLoginId=_WwpLeosRmonFileXftpLoginId_Object((1,3,6,1,4,1,6141,2,60,41,1,1,1,1,14),_WwpLeosRmonFileXftpLoginId_Type())
wwpLeosRmonFileXftpLoginId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRmonFileXftpLoginId.setStatus(_A)
class _WwpLeosRmonFileXftpPassword_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_WwpLeosRmonFileXftpPassword_Type.__name__=_D
_WwpLeosRmonFileXftpPassword_Object=MibTableColumn
wwpLeosRmonFileXftpPassword=_WwpLeosRmonFileXftpPassword_Object((1,3,6,1,4,1,6141,2,60,41,1,1,1,1,15),_WwpLeosRmonFileXftpPassword_Type())
wwpLeosRmonFileXftpPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRmonFileXftpPassword.setStatus(_A)
class _WwpLeosRmonFileXftpSecret_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_WwpLeosRmonFileXftpSecret_Type.__name__=_D
_WwpLeosRmonFileXftpSecret_Object=MibTableColumn
wwpLeosRmonFileXftpSecret=_WwpLeosRmonFileXftpSecret_Object((1,3,6,1,4,1,6141,2,60,41,1,1,1,1,16),_WwpLeosRmonFileXftpSecret_Type())
wwpLeosRmonFileXftpSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRmonFileXftpSecret.setStatus(_A)
_WwpLeosRmonHistoryTable_Object=MibTable
wwpLeosRmonHistoryTable=_WwpLeosRmonHistoryTable_Object((1,3,6,1,4,1,6141,2,60,41,1,1,2))
if mibBuilder.loadTexts:wwpLeosRmonHistoryTable.setStatus(_A)
_WwpLeosRmonHistoryEntry_Object=MibTableRow
wwpLeosRmonHistoryEntry=_WwpLeosRmonHistoryEntry_Object((1,3,6,1,4,1,6141,2,60,41,1,1,2,1))
wwpLeosRmonHistoryEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:wwpLeosRmonHistoryEntry.setStatus(_A)
class _WwpLeosRmonHistoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_WwpLeosRmonHistoryIndex_Type.__name__=_C
_WwpLeosRmonHistoryIndex_Object=MibTableColumn
wwpLeosRmonHistoryIndex=_WwpLeosRmonHistoryIndex_Object((1,3,6,1,4,1,6141,2,60,41,1,1,2,1,1),_WwpLeosRmonHistoryIndex_Type())
wwpLeosRmonHistoryIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosRmonHistoryIndex.setStatus(_A)
class _WwpLeosRmonHistoryAutoConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_WwpLeosRmonHistoryAutoConfig_Type.__name__=_C
_WwpLeosRmonHistoryAutoConfig_Object=MibTableColumn
wwpLeosRmonHistoryAutoConfig=_WwpLeosRmonHistoryAutoConfig_Object((1,3,6,1,4,1,6141,2,60,41,1,1,2,1,2),_WwpLeosRmonHistoryAutoConfig_Type())
wwpLeosRmonHistoryAutoConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRmonHistoryAutoConfig.setStatus(_A)
class _WwpLeosRmonHistoryFileLogging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_WwpLeosRmonHistoryFileLogging_Type.__name__=_C
_WwpLeosRmonHistoryFileLogging_Object=MibTableColumn
wwpLeosRmonHistoryFileLogging=_WwpLeosRmonHistoryFileLogging_Object((1,3,6,1,4,1,6141,2,60,41,1,1,2,1,3),_WwpLeosRmonHistoryFileLogging_Type())
wwpLeosRmonHistoryFileLogging.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRmonHistoryFileLogging.setStatus(_A)
class _WwpLeosRmonHistoryInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosRmonHistoryInterval_Type.__name__=_C
_WwpLeosRmonHistoryInterval_Object=MibTableColumn
wwpLeosRmonHistoryInterval=_WwpLeosRmonHistoryInterval_Object((1,3,6,1,4,1,6141,2,60,41,1,1,2,1,4),_WwpLeosRmonHistoryInterval_Type())
wwpLeosRmonHistoryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRmonHistoryInterval.setStatus(_A)
class _WwpLeosRmonHistoryNumBuckets_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosRmonHistoryNumBuckets_Type.__name__=_C
_WwpLeosRmonHistoryNumBuckets_Object=MibTableColumn
wwpLeosRmonHistoryNumBuckets=_WwpLeosRmonHistoryNumBuckets_Object((1,3,6,1,4,1,6141,2,60,41,1,1,2,1,5),_WwpLeosRmonHistoryNumBuckets_Type())
wwpLeosRmonHistoryNumBuckets.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRmonHistoryNumBuckets.setStatus(_A)
class _WwpLeosRmonHistoryOwner_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_WwpLeosRmonHistoryOwner_Type.__name__=_D
_WwpLeosRmonHistoryOwner_Object=MibTableColumn
wwpLeosRmonHistoryOwner=_WwpLeosRmonHistoryOwner_Object((1,3,6,1,4,1,6141,2,60,41,1,1,2,1,6),_WwpLeosRmonHistoryOwner_Type())
wwpLeosRmonHistoryOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRmonHistoryOwner.setStatus(_A)
class _WwpLeosRmonHistoryStatistics_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,9,10,13,22,36,37,38,39,45,47,51,54,55,63,71,79,87,95,103,111,119,127)));namedValues=NamedValues(*(('none',0),('basicTx',1),('basicRx',2),('basicRxBasicTx',3),('basicError',4),('basicTxBasicError',5),('basicRxBasicError',6),('basicAll',7),('txAll',9),('rxAll',10),('txAllBasicError',13),('rxAllBasicError',22),('errorAll',36),('basicTxErrorAll',37),('basicRxErrorAll',38),('basicRxBasicTxErroAll',39),('txAllErrorAll',45),('txAllRxBasicErrorAll',47),('rxTxAll',51),('rxAllErrorAll',54),('rxAllTxBasicErrorAll',55),('allStatsNoStandard',63),('standardRmon',71),('standardTxAll',79),('standardRxAll',87),('standardRxAllTxAll',95),('standardErrorAll',103),('standardTxAllErrorAll',111),('standardRxAllErrorAll',119),('allStatsWithStandard',127)))
_WwpLeosRmonHistoryStatistics_Type.__name__=_C
_WwpLeosRmonHistoryStatistics_Object=MibTableColumn
wwpLeosRmonHistoryStatistics=_WwpLeosRmonHistoryStatistics_Object((1,3,6,1,4,1,6141,2,60,41,1,1,2,1,7),_WwpLeosRmonHistoryStatistics_Type())
wwpLeosRmonHistoryStatistics.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRmonHistoryStatistics.setStatus(_A)
_WwpLeosRmonMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosRmonMIBNotificationPrefix=_WwpLeosRmonMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,41,2))
_WwpLeosRmonMIBNotifications_ObjectIdentity=ObjectIdentity
wwpLeosRmonMIBNotifications=_WwpLeosRmonMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,41,2,0))
_WwpLeosRmonMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosRmonMIBConformance=_WwpLeosRmonMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,41,3))
_WwpLeosRmonsMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosRmonsMIBCompliances=_WwpLeosRmonsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,41,3,1))
_WwpLeosRmonMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosRmonMIBGroups=_WwpLeosRmonMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,41,3,2))
mibBuilder.exportSymbols(_F,**{'wwpLeosRmonMIB':wwpLeosRmonMIB,'wwpLeosRmonMIBObjects':wwpLeosRmonMIBObjects,'wwpLeosRmon':wwpLeosRmon,'wwpLeosRmonFileTable':wwpLeosRmonFileTable,'wwpLeosRmonFileEntry':wwpLeosRmonFileEntry,_G:wwpLeosRmonFileIndex,'wwpLeosRmonFileName':wwpLeosRmonFileName,'wwpLeosRmonFileRemoteDir':wwpLeosRmonFileRemoteDir,'wwpLeosRmonFileServer':wwpLeosRmonFileServer,'wwpLeosRmonFileInterval':wwpLeosRmonFileInterval,'wwpLeosRmonFilePushLastFile':wwpLeosRmonFilePushLastFile,'wwpLeosRmonFileState':wwpLeosRmonFileState,'wwpLeosRmonFileLastRemoteName':wwpLeosRmonFileLastRemoteName,'wwpLeosRmonFileLastPushTime':wwpLeosRmonFileLastPushTime,'wwpLeosRmonFileLastPushStatus':wwpLeosRmonFileLastPushStatus,'wwpLeosRmonFileUserFilesKept':wwpLeosRmonFileUserFilesKept,'wwpLeosRmonFileMaxFiles':wwpLeosRmonFileMaxFiles,'wwpLeosRmonFileXftpTransferMode':wwpLeosRmonFileXftpTransferMode,'wwpLeosRmonFileXftpLoginId':wwpLeosRmonFileXftpLoginId,'wwpLeosRmonFileXftpPassword':wwpLeosRmonFileXftpPassword,'wwpLeosRmonFileXftpSecret':wwpLeosRmonFileXftpSecret,'wwpLeosRmonHistoryTable':wwpLeosRmonHistoryTable,'wwpLeosRmonHistoryEntry':wwpLeosRmonHistoryEntry,_J:wwpLeosRmonHistoryIndex,'wwpLeosRmonHistoryAutoConfig':wwpLeosRmonHistoryAutoConfig,'wwpLeosRmonHistoryFileLogging':wwpLeosRmonHistoryFileLogging,'wwpLeosRmonHistoryInterval':wwpLeosRmonHistoryInterval,'wwpLeosRmonHistoryNumBuckets':wwpLeosRmonHistoryNumBuckets,'wwpLeosRmonHistoryOwner':wwpLeosRmonHistoryOwner,'wwpLeosRmonHistoryStatistics':wwpLeosRmonHistoryStatistics,'wwpLeosRmonMIBNotificationPrefix':wwpLeosRmonMIBNotificationPrefix,'wwpLeosRmonMIBNotifications':wwpLeosRmonMIBNotifications,'wwpLeosRmonMIBConformance':wwpLeosRmonMIBConformance,'wwpLeosRmonsMIBCompliances':wwpLeosRmonsMIBCompliances,'wwpLeosRmonMIBGroups':wwpLeosRmonMIBGroups})