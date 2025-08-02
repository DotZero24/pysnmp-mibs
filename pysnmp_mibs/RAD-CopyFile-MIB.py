_X='copyFileError'
_W='copyFilePort'
_V='copyFileAddress'
_U='copyFileDstFileName'
_T='copyFileDstFilePath'
_S='copyFileDstType'
_R='copyFileSrcFileName'
_Q='copyFileSrcFilePath'
_P='copyFileSrcType'
_O='copyFileIdx'
_N='sysName'
_M='SNMPv2-MIB'
_L='alarmEventReason'
_K='alarmEventLogSourceName'
_J='alarmEventLogSeverity'
_I='alarmEventLogDescription'
_H='alarmEventLogDateAndTime'
_G='alarmEventLogAlarmOrEventId'
_F='read-only'
_E='Integer32'
_D='RAD-GEN-MIB'
_C='RAD-CopyFile-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
alarmEventLogAlarmOrEventId,alarmEventLogDateAndTime,alarmEventLogDescription,alarmEventLogSeverity,alarmEventLogSourceName,alarmEventReason=mibBuilder.importSymbols(_D,_G,_H,_I,_J,_K,_L)
fileTransfer,=mibBuilder.importSymbols('RAD-SMI-MIB','fileTransfer')
FileType,=mibBuilder.importSymbols('RAD-TC','FileType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_M,_N)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention')
copyFileGroup=ModuleIdentity((1,3,6,1,4,1,164,6,2,12,18))
_CopyFileNotifications_ObjectIdentity=ObjectIdentity
copyFileNotifications=_CopyFileNotifications_ObjectIdentity((1,3,6,1,4,1,164,6,2,12,18,0))
if mibBuilder.loadTexts:copyFileNotifications.setStatus(_A)
_CopyFileTable_Object=MibTable
copyFileTable=_CopyFileTable_Object((1,3,6,1,4,1,164,6,2,12,18,1))
if mibBuilder.loadTexts:copyFileTable.setStatus(_A)
_CopyFileEntry_Object=MibTableRow
copyFileEntry=_CopyFileEntry_Object((1,3,6,1,4,1,164,6,2,12,18,1,1))
copyFileEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:copyFileEntry.setStatus(_A)
_CopyFileIdx_Type=Integer32
_CopyFileIdx_Object=MibTableColumn
copyFileIdx=_CopyFileIdx_Object((1,3,6,1,4,1,164,6,2,12,18,1,1,1),_CopyFileIdx_Type())
copyFileIdx.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:copyFileIdx.setStatus(_A)
_CopyFileRowStatus_Type=RowStatus
_CopyFileRowStatus_Object=MibTableColumn
copyFileRowStatus=_CopyFileRowStatus_Object((1,3,6,1,4,1,164,6,2,12,18,1,1,2),_CopyFileRowStatus_Type())
copyFileRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:copyFileRowStatus.setStatus(_A)
class _CopyFileProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('undefined',1),('tftp',2),('sftp',3),('xmodem',4),('localFile',5)))
_CopyFileProtocol_Type.__name__=_E
_CopyFileProtocol_Object=MibTableColumn
copyFileProtocol=_CopyFileProtocol_Object((1,3,6,1,4,1,164,6,2,12,18,1,1,3),_CopyFileProtocol_Type())
copyFileProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:copyFileProtocol.setStatus(_A)
_CopyFileAddressType_Type=InetAddressType
_CopyFileAddressType_Object=MibTableColumn
copyFileAddressType=_CopyFileAddressType_Object((1,3,6,1,4,1,164,6,2,12,18,1,1,4),_CopyFileAddressType_Type())
copyFileAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:copyFileAddressType.setStatus(_A)
_CopyFileAddress_Type=InetAddress
_CopyFileAddress_Object=MibTableColumn
copyFileAddress=_CopyFileAddress_Object((1,3,6,1,4,1,164,6,2,12,18,1,1,5),_CopyFileAddress_Type())
copyFileAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:copyFileAddress.setStatus(_A)
_CopyFilePort_Type=InetPortNumber
_CopyFilePort_Object=MibTableColumn
copyFilePort=_CopyFilePort_Object((1,3,6,1,4,1,164,6,2,12,18,1,1,6),_CopyFilePort_Type())
copyFilePort.setMaxAccess(_B)
if mibBuilder.loadTexts:copyFilePort.setStatus(_A)
_CopyFileUserName_Type=SnmpAdminString
_CopyFileUserName_Object=MibTableColumn
copyFileUserName=_CopyFileUserName_Object((1,3,6,1,4,1,164,6,2,12,18,1,1,7),_CopyFileUserName_Type())
copyFileUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:copyFileUserName.setStatus(_A)
_CopyFilePassword_Type=SnmpAdminString
_CopyFilePassword_Object=MibTableColumn
copyFilePassword=_CopyFilePassword_Object((1,3,6,1,4,1,164,6,2,12,18,1,1,8),_CopyFilePassword_Type())
copyFilePassword.setMaxAccess(_B)
if mibBuilder.loadTexts:copyFilePassword.setStatus(_A)
_CopyFileSrcType_Type=FileType
_CopyFileSrcType_Object=MibTableColumn
copyFileSrcType=_CopyFileSrcType_Object((1,3,6,1,4,1,164,6,2,12,18,1,1,9),_CopyFileSrcType_Type())
copyFileSrcType.setMaxAccess(_B)
if mibBuilder.loadTexts:copyFileSrcType.setStatus(_A)
_CopyFileSrcFilePath_Type=SnmpAdminString
_CopyFileSrcFilePath_Object=MibTableColumn
copyFileSrcFilePath=_CopyFileSrcFilePath_Object((1,3,6,1,4,1,164,6,2,12,18,1,1,10),_CopyFileSrcFilePath_Type())
copyFileSrcFilePath.setMaxAccess(_B)
if mibBuilder.loadTexts:copyFileSrcFilePath.setStatus(_A)
_CopyFileSrcFileName_Type=SnmpAdminString
_CopyFileSrcFileName_Object=MibTableColumn
copyFileSrcFileName=_CopyFileSrcFileName_Object((1,3,6,1,4,1,164,6,2,12,18,1,1,11),_CopyFileSrcFileName_Type())
copyFileSrcFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:copyFileSrcFileName.setStatus(_A)
_CopyFileDstType_Type=FileType
_CopyFileDstType_Object=MibTableColumn
copyFileDstType=_CopyFileDstType_Object((1,3,6,1,4,1,164,6,2,12,18,1,1,12),_CopyFileDstType_Type())
copyFileDstType.setMaxAccess(_B)
if mibBuilder.loadTexts:copyFileDstType.setStatus(_A)
_CopyFileDstFilePath_Type=SnmpAdminString
_CopyFileDstFilePath_Object=MibTableColumn
copyFileDstFilePath=_CopyFileDstFilePath_Object((1,3,6,1,4,1,164,6,2,12,18,1,1,13),_CopyFileDstFilePath_Type())
copyFileDstFilePath.setMaxAccess(_B)
if mibBuilder.loadTexts:copyFileDstFilePath.setStatus(_A)
_CopyFileDstFileName_Type=SnmpAdminString
_CopyFileDstFileName_Object=MibTableColumn
copyFileDstFileName=_CopyFileDstFileName_Object((1,3,6,1,4,1,164,6,2,12,18,1,1,14),_CopyFileDstFileName_Type())
copyFileDstFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:copyFileDstFileName.setStatus(_A)
class _CopyFileStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7,8)));namedValues=NamedValues(*(('noOp',2),('authenticating',3),('connecting',4),('transferringData',5),('endedOk',6),('error',7),('errorOveridden',8)))
_CopyFileStatus_Type.__name__=_E
_CopyFileStatus_Object=MibTableColumn
copyFileStatus=_CopyFileStatus_Object((1,3,6,1,4,1,164,6,2,12,18,1,1,15),_CopyFileStatus_Type())
copyFileStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:copyFileStatus.setStatus(_A)
class _CopyFileError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,8,9,10,11,14,15,255)));namedValues=NamedValues(*(('noError',1),('serverNotResponding',2),('fileNotFound',3),('accessViolationDst',4),('invalidSrcFile',5),('invalidRollbackSrc',6),('connectionFail',8),('lackOfSpace',9),('lackOfInternalResources',10),('endedTimeout',11),('accessViolationSrc',14),('transferToStandbyFailed',15),('otherError',255)))
_CopyFileError_Type.__name__=_E
_CopyFileError_Object=MibTableColumn
copyFileError=_CopyFileError_Object((1,3,6,1,4,1,164,6,2,12,18,1,1,16),_CopyFileError_Type())
copyFileError.setMaxAccess(_F)
if mibBuilder.loadTexts:copyFileError.setStatus(_A)
_CopyFileStartTime_Type=DateAndTime
_CopyFileStartTime_Object=MibTableColumn
copyFileStartTime=_CopyFileStartTime_Object((1,3,6,1,4,1,164,6,2,12,18,1,1,17),_CopyFileStartTime_Type())
copyFileStartTime.setMaxAccess(_F)
if mibBuilder.loadTexts:copyFileStartTime.setStatus(_A)
_CopyFileEndTime_Type=DateAndTime
_CopyFileEndTime_Object=MibTableColumn
copyFileEndTime=_CopyFileEndTime_Object((1,3,6,1,4,1,164,6,2,12,18,1,1,18),_CopyFileEndTime_Type())
copyFileEndTime.setMaxAccess(_F)
if mibBuilder.loadTexts:copyFileEndTime.setStatus(_A)
_CopyFileProgressBytes_Type=Unsigned32
_CopyFileProgressBytes_Object=MibTableColumn
copyFileProgressBytes=_CopyFileProgressBytes_Object((1,3,6,1,4,1,164,6,2,12,18,1,1,19),_CopyFileProgressBytes_Type())
copyFileProgressBytes.setMaxAccess(_F)
if mibBuilder.loadTexts:copyFileProgressBytes.setStatus(_A)
class _CopyFileDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('networkToDevice',1),('deviceToNetwork',2),('deviceLocally',3)))
_CopyFileDirection_Type.__name__=_E
_CopyFileDirection_Object=MibTableColumn
copyFileDirection=_CopyFileDirection_Object((1,3,6,1,4,1,164,6,2,12,18,1,1,20),_CopyFileDirection_Type())
copyFileDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:copyFileDirection.setStatus(_A)
systemDownloadEnd=NotificationType((1,3,6,1,4,1,164,6,2,12,18,0,2))
systemDownloadEnd.setObjects(*((_D,_K),(_D,_G),(_D,_I),(_D,_J),(_D,_H),(_D,_L),(_M,_N),(_C,_P),(_C,_Q),(_C,_R),(_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_W),(_C,_X)))
if mibBuilder.loadTexts:systemDownloadEnd.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'copyFileGroup':copyFileGroup,'copyFileNotifications':copyFileNotifications,'systemDownloadEnd':systemDownloadEnd,'copyFileTable':copyFileTable,'copyFileEntry':copyFileEntry,_O:copyFileIdx,'copyFileRowStatus':copyFileRowStatus,'copyFileProtocol':copyFileProtocol,'copyFileAddressType':copyFileAddressType,_V:copyFileAddress,_W:copyFilePort,'copyFileUserName':copyFileUserName,'copyFilePassword':copyFilePassword,_P:copyFileSrcType,_Q:copyFileSrcFilePath,_R:copyFileSrcFileName,_S:copyFileDstType,_T:copyFileDstFilePath,_U:copyFileDstFileName,'copyFileStatus':copyFileStatus,_X:copyFileError,'copyFileStartTime':copyFileStartTime,'copyFileEndTime':copyFileEndTime,'copyFileProgressBytes':copyFileProgressBytes,'copyFileDirection':copyFileDirection})