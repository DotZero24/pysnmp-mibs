_J='enable'
_I='disable'
_H='cienaCesRmonTransferServerIndex'
_G='CIENA-CES-RMON-MIB'
_F='OctetString'
_E='read-only'
_D='DisplayString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaCesConfig,cienaCommon=mibBuilder.importSymbols('CIENA-SMI','cienaCesConfig','cienaCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention','TruthValue')
cienaCesRmonMIB=ModuleIdentity((1,3,6,1,4,1,1271,2,1,34))
if mibBuilder.loadTexts:cienaCesRmonMIB.setRevisions(('2014-11-11 00:00',))
_CienaCesRmonMIBObjects_ObjectIdentity=ObjectIdentity
cienaCesRmonMIBObjects=_CienaCesRmonMIBObjects_ObjectIdentity((1,3,6,1,4,1,1271,2,1,34,1))
_CienaCesRmon_ObjectIdentity=ObjectIdentity
cienaCesRmon=_CienaCesRmon_ObjectIdentity((1,3,6,1,4,1,1271,2,1,34,1,1))
_CienaCesRmonTransfer_ObjectIdentity=ObjectIdentity
cienaCesRmonTransfer=_CienaCesRmonTransfer_ObjectIdentity((1,3,6,1,4,1,1271,2,1,34,1,1,1))
_CienaCesRmonTransferServerTable_Object=MibTable
cienaCesRmonTransferServerTable=_CienaCesRmonTransferServerTable_Object((1,3,6,1,4,1,1271,2,1,34,1,1,1,1))
if mibBuilder.loadTexts:cienaCesRmonTransferServerTable.setStatus(_A)
_CienaCesRmonTransferServerEntry_Object=MibTableRow
cienaCesRmonTransferServerEntry=_CienaCesRmonTransferServerEntry_Object((1,3,6,1,4,1,1271,2,1,34,1,1,1,1,1))
cienaCesRmonTransferServerEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cienaCesRmonTransferServerEntry.setStatus(_A)
class _CienaCesRmonTransferServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_CienaCesRmonTransferServerIndex_Type.__name__=_C
_CienaCesRmonTransferServerIndex_Object=MibTableColumn
cienaCesRmonTransferServerIndex=_CienaCesRmonTransferServerIndex_Object((1,3,6,1,4,1,1271,2,1,34,1,1,1,1,1,1),_CienaCesRmonTransferServerIndex_Type())
cienaCesRmonTransferServerIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesRmonTransferServerIndex.setStatus(_A)
class _CienaCesRmonTransferServerServer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CienaCesRmonTransferServerServer_Type.__name__=_D
_CienaCesRmonTransferServerServer_Object=MibTableColumn
cienaCesRmonTransferServerServer=_CienaCesRmonTransferServerServer_Object((1,3,6,1,4,1,1271,2,1,34,1,1,1,1,1,2),_CienaCesRmonTransferServerServer_Type())
cienaCesRmonTransferServerServer.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRmonTransferServerServer.setStatus(_A)
class _CienaCesRmonTransferServerLastRemoteName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_CienaCesRmonTransferServerLastRemoteName_Type.__name__=_D
_CienaCesRmonTransferServerLastRemoteName_Object=MibTableColumn
cienaCesRmonTransferServerLastRemoteName=_CienaCesRmonTransferServerLastRemoteName_Object((1,3,6,1,4,1,1271,2,1,34,1,1,1,1,1,3),_CienaCesRmonTransferServerLastRemoteName_Type())
cienaCesRmonTransferServerLastRemoteName.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesRmonTransferServerLastRemoteName.setStatus(_A)
class _CienaCesRmonTransferServerLastPushTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CienaCesRmonTransferServerLastPushTime_Type.__name__=_D
_CienaCesRmonTransferServerLastPushTime_Object=MibTableColumn
cienaCesRmonTransferServerLastPushTime=_CienaCesRmonTransferServerLastPushTime_Object((1,3,6,1,4,1,1271,2,1,34,1,1,1,1,1,4),_CienaCesRmonTransferServerLastPushTime_Type())
cienaCesRmonTransferServerLastPushTime.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesRmonTransferServerLastPushTime.setStatus(_A)
class _CienaCesRmonTransferServerLastPushStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_CienaCesRmonTransferServerLastPushStatus_Type.__name__=_D
_CienaCesRmonTransferServerLastPushStatus_Object=MibTableColumn
cienaCesRmonTransferServerLastPushStatus=_CienaCesRmonTransferServerLastPushStatus_Object((1,3,6,1,4,1,1271,2,1,34,1,1,1,1,1,5),_CienaCesRmonTransferServerLastPushStatus_Type())
cienaCesRmonTransferServerLastPushStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesRmonTransferServerLastPushStatus.setStatus(_A)
class _CienaCesRmonTransferServerXftpTransferMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('tftp',1),('ftp',2),('sftp',3),('defaultTftp',4),('defaultFtp',5),('defaultSftp',6),('default',7)))
_CienaCesRmonTransferServerXftpTransferMode_Type.__name__=_C
_CienaCesRmonTransferServerXftpTransferMode_Object=MibTableColumn
cienaCesRmonTransferServerXftpTransferMode=_CienaCesRmonTransferServerXftpTransferMode_Object((1,3,6,1,4,1,1271,2,1,34,1,1,1,1,1,6),_CienaCesRmonTransferServerXftpTransferMode_Type())
cienaCesRmonTransferServerXftpTransferMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRmonTransferServerXftpTransferMode.setStatus(_A)
class _CienaCesRmonTransferServerXftpLoginId_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CienaCesRmonTransferServerXftpLoginId_Type.__name__=_D
_CienaCesRmonTransferServerXftpLoginId_Object=MibTableColumn
cienaCesRmonTransferServerXftpLoginId=_CienaCesRmonTransferServerXftpLoginId_Object((1,3,6,1,4,1,1271,2,1,34,1,1,1,1,1,7),_CienaCesRmonTransferServerXftpLoginId_Type())
cienaCesRmonTransferServerXftpLoginId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRmonTransferServerXftpLoginId.setStatus(_A)
class _CienaCesRmonTransferServerXftpPassword_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CienaCesRmonTransferServerXftpPassword_Type.__name__=_D
_CienaCesRmonTransferServerXftpPassword_Object=MibTableColumn
cienaCesRmonTransferServerXftpPassword=_CienaCesRmonTransferServerXftpPassword_Object((1,3,6,1,4,1,1271,2,1,34,1,1,1,1,1,8),_CienaCesRmonTransferServerXftpPassword_Type())
cienaCesRmonTransferServerXftpPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRmonTransferServerXftpPassword.setStatus(_A)
class _CienaCesRmonTransferServerXftpSecret_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,259))
_CienaCesRmonTransferServerXftpSecret_Type.__name__=_F
_CienaCesRmonTransferServerXftpSecret_Object=MibTableColumn
cienaCesRmonTransferServerXftpSecret=_CienaCesRmonTransferServerXftpSecret_Object((1,3,6,1,4,1,1271,2,1,34,1,1,1,1,1,9),_CienaCesRmonTransferServerXftpSecret_Type())
cienaCesRmonTransferServerXftpSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRmonTransferServerXftpSecret.setStatus(_A)
class _CienaCesRmonTransferName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CienaCesRmonTransferName_Type.__name__=_D
_CienaCesRmonTransferName_Object=MibScalar
cienaCesRmonTransferName=_CienaCesRmonTransferName_Object((1,3,6,1,4,1,1271,2,1,34,1,1,1,2),_CienaCesRmonTransferName_Type())
cienaCesRmonTransferName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRmonTransferName.setStatus(_A)
class _CienaCesRmonTransferRemoteDir_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_CienaCesRmonTransferRemoteDir_Type.__name__=_D
_CienaCesRmonTransferRemoteDir_Object=MibScalar
cienaCesRmonTransferRemoteDir=_CienaCesRmonTransferRemoteDir_Object((1,3,6,1,4,1,1271,2,1,34,1,1,1,3),_CienaCesRmonTransferRemoteDir_Type())
cienaCesRmonTransferRemoteDir.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRmonTransferRemoteDir.setStatus(_A)
class _CienaCesRmonTransferInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3600,31536000))
_CienaCesRmonTransferInterval_Type.__name__=_C
_CienaCesRmonTransferInterval_Object=MibScalar
cienaCesRmonTransferInterval=_CienaCesRmonTransferInterval_Object((1,3,6,1,4,1,1271,2,1,34,1,1,1,4),_CienaCesRmonTransferInterval_Type())
cienaCesRmonTransferInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRmonTransferInterval.setStatus(_A)
class _CienaCesRmonTransferUserFilesKept_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_CienaCesRmonTransferUserFilesKept_Type.__name__=_C
_CienaCesRmonTransferUserFilesKept_Object=MibScalar
cienaCesRmonTransferUserFilesKept=_CienaCesRmonTransferUserFilesKept_Object((1,3,6,1,4,1,1271,2,1,34,1,1,1,5),_CienaCesRmonTransferUserFilesKept_Type())
cienaCesRmonTransferUserFilesKept.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRmonTransferUserFilesKept.setStatus(_A)
class _CienaCesRmonTransferMaxFiles_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_CienaCesRmonTransferMaxFiles_Type.__name__=_C
_CienaCesRmonTransferMaxFiles_Object=MibScalar
cienaCesRmonTransferMaxFiles=_CienaCesRmonTransferMaxFiles_Object((1,3,6,1,4,1,1271,2,1,34,1,1,1,6),_CienaCesRmonTransferMaxFiles_Type())
cienaCesRmonTransferMaxFiles.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesRmonTransferMaxFiles.setStatus(_A)
_CienaCesRmonTransferPushRecentFiles_Type=TruthValue
_CienaCesRmonTransferPushRecentFiles_Object=MibScalar
cienaCesRmonTransferPushRecentFiles=_CienaCesRmonTransferPushRecentFiles_Object((1,3,6,1,4,1,1271,2,1,34,1,1,1,7),_CienaCesRmonTransferPushRecentFiles_Type())
cienaCesRmonTransferPushRecentFiles.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRmonTransferPushRecentFiles.setStatus(_A)
class _CienaCesRmonTransferState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_CienaCesRmonTransferState_Type.__name__=_C
_CienaCesRmonTransferState_Object=MibScalar
cienaCesRmonTransferState=_CienaCesRmonTransferState_Object((1,3,6,1,4,1,1271,2,1,34,1,1,1,8),_CienaCesRmonTransferState_Type())
cienaCesRmonTransferState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRmonTransferState.setStatus(_A)
_CienaCesRmonAutoConfigure_ObjectIdentity=ObjectIdentity
cienaCesRmonAutoConfigure=_CienaCesRmonAutoConfigure_ObjectIdentity((1,3,6,1,4,1,1271,2,1,34,1,1,2))
class _CienaCesRmonHistAutoConfigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_CienaCesRmonHistAutoConfigState_Type.__name__=_C
_CienaCesRmonHistAutoConfigState_Object=MibScalar
cienaCesRmonHistAutoConfigState=_CienaCesRmonHistAutoConfigState_Object((1,3,6,1,4,1,1271,2,1,34,1,1,2,1),_CienaCesRmonHistAutoConfigState_Type())
cienaCesRmonHistAutoConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRmonHistAutoConfigState.setStatus(_A)
class _CienaCesRmonHistAutoConfigFileLogging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_CienaCesRmonHistAutoConfigFileLogging_Type.__name__=_C
_CienaCesRmonHistAutoConfigFileLogging_Object=MibScalar
cienaCesRmonHistAutoConfigFileLogging=_CienaCesRmonHistAutoConfigFileLogging_Object((1,3,6,1,4,1,1271,2,1,34,1,1,2,2),_CienaCesRmonHistAutoConfigFileLogging_Type())
cienaCesRmonHistAutoConfigFileLogging.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRmonHistAutoConfigFileLogging.setStatus(_A)
class _CienaCesRmonHistAutoConfigInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesRmonHistAutoConfigInterval_Type.__name__=_C
_CienaCesRmonHistAutoConfigInterval_Object=MibScalar
cienaCesRmonHistAutoConfigInterval=_CienaCesRmonHistAutoConfigInterval_Object((1,3,6,1,4,1,1271,2,1,34,1,1,2,3),_CienaCesRmonHistAutoConfigInterval_Type())
cienaCesRmonHistAutoConfigInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRmonHistAutoConfigInterval.setStatus(_A)
class _CienaCesRmonHistAutoConfigNumBuckets_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesRmonHistAutoConfigNumBuckets_Type.__name__=_C
_CienaCesRmonHistAutoConfigNumBuckets_Object=MibScalar
cienaCesRmonHistAutoConfigNumBuckets=_CienaCesRmonHistAutoConfigNumBuckets_Object((1,3,6,1,4,1,1271,2,1,34,1,1,2,4),_CienaCesRmonHistAutoConfigNumBuckets_Type())
cienaCesRmonHistAutoConfigNumBuckets.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRmonHistAutoConfigNumBuckets.setStatus(_A)
class _CienaCesRmonHistAutoConfigOwner_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_CienaCesRmonHistAutoConfigOwner_Type.__name__=_D
_CienaCesRmonHistAutoConfigOwner_Object=MibScalar
cienaCesRmonHistAutoConfigOwner=_CienaCesRmonHistAutoConfigOwner_Object((1,3,6,1,4,1,1271,2,1,34,1,1,2,5),_CienaCesRmonHistAutoConfigOwner_Type())
cienaCesRmonHistAutoConfigOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRmonHistAutoConfigOwner.setStatus(_A)
class _CienaCesRmonHistAutoConfigStatistics_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,9,10,13,18,22,36,37,38,39,45,47,51,54,55,63,71,79,87,95,103,111,119,127)));namedValues=NamedValues(*(('none',0),('basicTx',1),('basicRx',2),('basicRxBasicTx',3),('basicError',4),('basicTxBasicError',5),('basicRxBasicError',6),('basicAll',7),('txAll',9),('txAllBasicRx',10),('txAllBasicError',13),('rxAllBasicRx',18),('rxAllBasicError',22),('errorAll',36),('basicTxErrorAll',37),('basicRxErrorAll',38),('basicRxBasicTxErroAll',39),('txAllErrorAll',45),('txAllRxBasicErrorAll',47),('rxTxAll',51),('rxAllErrorAll',54),('rxAllTxBasicErrorAll',55),('allStatsNoStandard',63),('standardRmon',71),('standardTxAll',79),('standardRxAll',87),('standardRxAllTxAll',95),('standardErrorAll',103),('standardTxAllErrorAll',111),('standardRxAllErrorAll',119),('allStatsWithStandard',127)))
_CienaCesRmonHistAutoConfigStatistics_Type.__name__=_C
_CienaCesRmonHistAutoConfigStatistics_Object=MibScalar
cienaCesRmonHistAutoConfigStatistics=_CienaCesRmonHistAutoConfigStatistics_Object((1,3,6,1,4,1,1271,2,1,34,1,1,2,6),_CienaCesRmonHistAutoConfigStatistics_Type())
cienaCesRmonHistAutoConfigStatistics.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRmonHistAutoConfigStatistics.setStatus(_A)
_CienaCesRmonMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
cienaCesRmonMIBNotificationPrefix=_CienaCesRmonMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,1271,2,1,34,2))
_CienaCesRmonMIBNotifications_ObjectIdentity=ObjectIdentity
cienaCesRmonMIBNotifications=_CienaCesRmonMIBNotifications_ObjectIdentity((1,3,6,1,4,1,1271,2,1,34,2,0))
_CienaCesRmonMIBConformance_ObjectIdentity=ObjectIdentity
cienaCesRmonMIBConformance=_CienaCesRmonMIBConformance_ObjectIdentity((1,3,6,1,4,1,1271,2,1,34,3))
_CienaCesRmonsMIBCompliances_ObjectIdentity=ObjectIdentity
cienaCesRmonsMIBCompliances=_CienaCesRmonsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,1271,2,1,34,3,1))
_CienaCesRmonMIBGroups_ObjectIdentity=ObjectIdentity
cienaCesRmonMIBGroups=_CienaCesRmonMIBGroups_ObjectIdentity((1,3,6,1,4,1,1271,2,1,34,3,2))
mibBuilder.exportSymbols(_G,**{'cienaCesRmonMIB':cienaCesRmonMIB,'cienaCesRmonMIBObjects':cienaCesRmonMIBObjects,'cienaCesRmon':cienaCesRmon,'cienaCesRmonTransfer':cienaCesRmonTransfer,'cienaCesRmonTransferServerTable':cienaCesRmonTransferServerTable,'cienaCesRmonTransferServerEntry':cienaCesRmonTransferServerEntry,_H:cienaCesRmonTransferServerIndex,'cienaCesRmonTransferServerServer':cienaCesRmonTransferServerServer,'cienaCesRmonTransferServerLastRemoteName':cienaCesRmonTransferServerLastRemoteName,'cienaCesRmonTransferServerLastPushTime':cienaCesRmonTransferServerLastPushTime,'cienaCesRmonTransferServerLastPushStatus':cienaCesRmonTransferServerLastPushStatus,'cienaCesRmonTransferServerXftpTransferMode':cienaCesRmonTransferServerXftpTransferMode,'cienaCesRmonTransferServerXftpLoginId':cienaCesRmonTransferServerXftpLoginId,'cienaCesRmonTransferServerXftpPassword':cienaCesRmonTransferServerXftpPassword,'cienaCesRmonTransferServerXftpSecret':cienaCesRmonTransferServerXftpSecret,'cienaCesRmonTransferName':cienaCesRmonTransferName,'cienaCesRmonTransferRemoteDir':cienaCesRmonTransferRemoteDir,'cienaCesRmonTransferInterval':cienaCesRmonTransferInterval,'cienaCesRmonTransferUserFilesKept':cienaCesRmonTransferUserFilesKept,'cienaCesRmonTransferMaxFiles':cienaCesRmonTransferMaxFiles,'cienaCesRmonTransferPushRecentFiles':cienaCesRmonTransferPushRecentFiles,'cienaCesRmonTransferState':cienaCesRmonTransferState,'cienaCesRmonAutoConfigure':cienaCesRmonAutoConfigure,'cienaCesRmonHistAutoConfigState':cienaCesRmonHistAutoConfigState,'cienaCesRmonHistAutoConfigFileLogging':cienaCesRmonHistAutoConfigFileLogging,'cienaCesRmonHistAutoConfigInterval':cienaCesRmonHistAutoConfigInterval,'cienaCesRmonHistAutoConfigNumBuckets':cienaCesRmonHistAutoConfigNumBuckets,'cienaCesRmonHistAutoConfigOwner':cienaCesRmonHistAutoConfigOwner,'cienaCesRmonHistAutoConfigStatistics':cienaCesRmonHistAutoConfigStatistics,'cienaCesRmonMIBNotificationPrefix':cienaCesRmonMIBNotificationPrefix,'cienaCesRmonMIBNotifications':cienaCesRmonMIBNotifications,'cienaCesRmonMIBConformance':cienaCesRmonMIBConformance,'cienaCesRmonsMIBCompliances':cienaCesRmonsMIBCompliances,'cienaCesRmonMIBGroups':cienaCesRmonMIBGroups})