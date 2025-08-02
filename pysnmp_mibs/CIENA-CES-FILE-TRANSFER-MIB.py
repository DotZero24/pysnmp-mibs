_K='cienaCesFTransferNotificationInfo'
_J='cienaCesFTransferNotificationStatus'
_I='cienaCesFTransferLocalFilename'
_H='cienaCesFTransferRemoteFilename'
_G='Integer32'
_F='cienaGlobalSeverity'
_E='cienaGlobalMacAddress'
_D='CIENA-GLOBAL-MIB'
_C='accessible-for-notify'
_B='CIENA-CES-FILE-TRANSFER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaGlobalMacAddress,cienaGlobalSeverity=mibBuilder.importSymbols(_D,_E,_F)
cienaCesConfig,cienaCesNotifications=mibBuilder.importSymbols('CIENA-SMI','cienaCesConfig','cienaCesNotifications')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cienaCesFileTransferMIB=ModuleIdentity((1,3,6,1,4,1,1271,2,1,15))
if mibBuilder.loadTexts:cienaCesFileTransferMIB.setRevisions(('2017-06-07 00:00','2011-02-02 00:00'))
_CienaCesFileTransferMIBObjects_ObjectIdentity=ObjectIdentity
cienaCesFileTransferMIBObjects=_CienaCesFileTransferMIBObjects_ObjectIdentity((1,3,6,1,4,1,1271,2,1,15,1))
_CienaCesFileTransfer_ObjectIdentity=ObjectIdentity
cienaCesFileTransfer=_CienaCesFileTransfer_ObjectIdentity((1,3,6,1,4,1,1271,2,1,15,1,1))
_CienaCesFTransferRemoteFilename_Type=DisplayString
_CienaCesFTransferRemoteFilename_Object=MibScalar
cienaCesFTransferRemoteFilename=_CienaCesFTransferRemoteFilename_Object((1,3,6,1,4,1,1271,2,1,15,1,1,1),_CienaCesFTransferRemoteFilename_Type())
cienaCesFTransferRemoteFilename.setMaxAccess(_C)
if mibBuilder.loadTexts:cienaCesFTransferRemoteFilename.setStatus(_A)
_CienaCesFTransferLocalFilename_Type=DisplayString
_CienaCesFTransferLocalFilename_Object=MibScalar
cienaCesFTransferLocalFilename=_CienaCesFTransferLocalFilename_Object((1,3,6,1,4,1,1271,2,1,15,1,1,2),_CienaCesFTransferLocalFilename_Type())
cienaCesFTransferLocalFilename.setMaxAccess(_C)
if mibBuilder.loadTexts:cienaCesFTransferLocalFilename.setStatus(_A)
class _CienaCesFTransferNotificationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*(('noStatus',0),('fileAlreadyExist',1),('tftpServerNotFound',2),('fileGetError',3),('filePutError',4),('fileSystemError',5),('fileContentsInvalid',6),('flashOffline',7),('badFileCrc',8),('allFilesSkipped',9),('serverIpAddrInvalid',10),('filePathInvalid',11),('fileNameInvalid',12),('sourceNotFound',13),('fileNameNeeded',14),('notEnoughSpace',15),('putSuccessful',16),('downloadSuccess',17),('internalError',18)))
_CienaCesFTransferNotificationStatus_Type.__name__=_G
_CienaCesFTransferNotificationStatus_Object=MibScalar
cienaCesFTransferNotificationStatus=_CienaCesFTransferNotificationStatus_Object((1,3,6,1,4,1,1271,2,1,15,1,1,3),_CienaCesFTransferNotificationStatus_Type())
cienaCesFTransferNotificationStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cienaCesFTransferNotificationStatus.setStatus(_A)
_CienaCesFTransferNotificationInfo_Type=DisplayString
_CienaCesFTransferNotificationInfo_Object=MibScalar
cienaCesFTransferNotificationInfo=_CienaCesFTransferNotificationInfo_Object((1,3,6,1,4,1,1271,2,1,15,1,1,4),_CienaCesFTransferNotificationInfo_Type())
cienaCesFTransferNotificationInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:cienaCesFTransferNotificationInfo.setStatus(_A)
_CienaCesFileTransferMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
cienaCesFileTransferMIBNotificationPrefix=_CienaCesFileTransferMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,1271,2,2,16))
_CienaCesFileTransferMIBNotifications_ObjectIdentity=ObjectIdentity
cienaCesFileTransferMIBNotifications=_CienaCesFileTransferMIBNotifications_ObjectIdentity((1,3,6,1,4,1,1271,2,2,16,0))
cienaCesFTransferCompletion=NotificationType((1,3,6,1,4,1,1271,2,2,16,0,1))
cienaCesFTransferCompletion.setObjects(*((_D,_F),(_D,_E),(_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:cienaCesFTransferCompletion.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cienaCesFileTransferMIB':cienaCesFileTransferMIB,'cienaCesFileTransferMIBObjects':cienaCesFileTransferMIBObjects,'cienaCesFileTransfer':cienaCesFileTransfer,_H:cienaCesFTransferRemoteFilename,_I:cienaCesFTransferLocalFilename,_J:cienaCesFTransferNotificationStatus,_K:cienaCesFTransferNotificationInfo,'cienaCesFileTransferMIBNotificationPrefix':cienaCesFileTransferMIBNotificationPrefix,'cienaCesFileTransferMIBNotifications':cienaCesFileTransferMIBNotifications,'cienaCesFTransferCompletion':cienaCesFTransferCompletion})