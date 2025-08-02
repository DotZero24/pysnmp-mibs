_Q='wwpLeosFileTransferIPv6Group'
_P='wwpLeosFTransferNotificationInfo'
_O='wwpLeosFTransferNotificationStatus'
_N='wwpLeosFTransferLocalFilename'
_M='wwpLeosFTransferRemoteFilename'
_L='wwpLeosFTransferServerInetAddr'
_K='wwpLeosFTransferServerInetAddrType'
_J='internalError'
_I='noStatus'
_H='IpAddress'
_G='TruthValue'
_F='Integer32'
_E='read-only'
_D='OctetString'
_C='WWP-LEOS-FILE-TRANSFER-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,_H,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_G)
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosFileTransferMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,23))
if mibBuilder.loadTexts:wwpLeosFileTransferMIB.setRevisions(('2012-03-22 00:00','2001-04-03 17:00'))
class FileTransferState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('idle',1),('sending',2),('receiving',3),('transferComplete',4),('failed',5)))
class FileTransferFailCause(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_I,1),('timeout',2),('networkError',3),('noSpace',4),('invalidFileName',5),('commandCompleted',6),(_J,7),('commandFileParseError',8)))
_WwpLeosFileTransferMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosFileTransferMIBObjects=_WwpLeosFileTransferMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,23,1))
_WwpLeosFileTransfer_ObjectIdentity=ObjectIdentity
wwpLeosFileTransfer=_WwpLeosFileTransfer_ObjectIdentity((1,3,6,1,4,1,6141,2,60,23,1,1))
class _WwpLeosFTransferOp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('sendFile',1),('getFile',2),('getCmdFile',3)))
_WwpLeosFTransferOp_Type.__name__=_F
_WwpLeosFTransferOp_Object=MibScalar
wwpLeosFTransferOp=_WwpLeosFTransferOp_Object((1,3,6,1,4,1,6141,2,60,23,1,1,1),_WwpLeosFTransferOp_Type())
wwpLeosFTransferOp.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosFTransferOp.setStatus(_A)
class _WwpLeosFTransferServerAddr_Type(IpAddress):defaultHexValue='00000000'
_WwpLeosFTransferServerAddr_Type.__name__=_H
_WwpLeosFTransferServerAddr_Object=MibScalar
wwpLeosFTransferServerAddr=_WwpLeosFTransferServerAddr_Object((1,3,6,1,4,1,6141,2,60,23,1,1,2),_WwpLeosFTransferServerAddr_Type())
wwpLeosFTransferServerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosFTransferServerAddr.setStatus(_A)
class _WwpLeosFTransferRemoteFilename_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_WwpLeosFTransferRemoteFilename_Type.__name__=_D
_WwpLeosFTransferRemoteFilename_Object=MibScalar
wwpLeosFTransferRemoteFilename=_WwpLeosFTransferRemoteFilename_Object((1,3,6,1,4,1,6141,2,60,23,1,1,3),_WwpLeosFTransferRemoteFilename_Type())
wwpLeosFTransferRemoteFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosFTransferRemoteFilename.setStatus(_A)
class _WwpLeosFTransferLocalFilename_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_WwpLeosFTransferLocalFilename_Type.__name__=_D
_WwpLeosFTransferLocalFilename_Object=MibScalar
wwpLeosFTransferLocalFilename=_WwpLeosFTransferLocalFilename_Object((1,3,6,1,4,1,6141,2,60,23,1,1,4),_WwpLeosFTransferLocalFilename_Type())
wwpLeosFTransferLocalFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosFTransferLocalFilename.setStatus(_A)
class _WwpLeosFTransferActivate_Type(TruthValue):defaultValue=2
_WwpLeosFTransferActivate_Type.__name__=_G
_WwpLeosFTransferActivate_Object=MibScalar
wwpLeosFTransferActivate=_WwpLeosFTransferActivate_Object((1,3,6,1,4,1,6141,2,60,23,1,1,5),_WwpLeosFTransferActivate_Type())
wwpLeosFTransferActivate.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosFTransferActivate.setStatus(_A)
class _WwpLeosFTransferNotifOnCompletion_Type(TruthValue):defaultValue=1
_WwpLeosFTransferNotifOnCompletion_Type.__name__=_G
_WwpLeosFTransferNotifOnCompletion_Object=MibScalar
wwpLeosFTransferNotifOnCompletion=_WwpLeosFTransferNotifOnCompletion_Object((1,3,6,1,4,1,6141,2,60,23,1,1,6),_WwpLeosFTransferNotifOnCompletion_Type())
wwpLeosFTransferNotifOnCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosFTransferNotifOnCompletion.setStatus(_A)
_WwpLeosFTransferStatus_Type=FileTransferState
_WwpLeosFTransferStatus_Object=MibScalar
wwpLeosFTransferStatus=_WwpLeosFTransferStatus_Object((1,3,6,1,4,1,6141,2,60,23,1,1,7),_WwpLeosFTransferStatus_Type())
wwpLeosFTransferStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFTransferStatus.setStatus(_A)
_WwpLeosFTransferFailCause_Type=FileTransferFailCause
_WwpLeosFTransferFailCause_Object=MibScalar
wwpLeosFTransferFailCause=_WwpLeosFTransferFailCause_Object((1,3,6,1,4,1,6141,2,60,23,1,1,8),_WwpLeosFTransferFailCause_Type())
wwpLeosFTransferFailCause.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFTransferFailCause.setStatus(_A)
class _WwpLeosFTransferNotificationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24)));namedValues=NamedValues(*(('downloadSuccess',0),('tftpServerNotFound',1),('couldNotGetFile',2),('cmdFileParseError',3),('internalFilesystemError',4),('inValidFileContents',5),('flashOffline',6),(_I,7),('putSuccessful',8),('couldNotPutFile',9),('badFileCrc',10),('allFilesSkipped',11),('fileAlreadyExist',12),('fileGetError',13),('filePutError',14),('fileSystemError',15),('fileContentsInvalid',16),('serverIpAddrInvalid',18),('filePathInvalid',19),('fileNameInvalid',20),('sourceNotFound',21),('fileNameNeeded',22),('notEnoughSpace',23),(_J,24)))
_WwpLeosFTransferNotificationStatus_Type.__name__=_F
_WwpLeosFTransferNotificationStatus_Object=MibScalar
wwpLeosFTransferNotificationStatus=_WwpLeosFTransferNotificationStatus_Object((1,3,6,1,4,1,6141,2,60,23,1,1,9),_WwpLeosFTransferNotificationStatus_Type())
wwpLeosFTransferNotificationStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFTransferNotificationStatus.setStatus(_A)
class _WwpLeosFTransferNotificationInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_WwpLeosFTransferNotificationInfo_Type.__name__=_D
_WwpLeosFTransferNotificationInfo_Object=MibScalar
wwpLeosFTransferNotificationInfo=_WwpLeosFTransferNotificationInfo_Object((1,3,6,1,4,1,6141,2,60,23,1,1,10),_WwpLeosFTransferNotificationInfo_Type())
wwpLeosFTransferNotificationInfo.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFTransferNotificationInfo.setStatus(_A)
_WwpLeosFTransferServerInetAddrType_Type=InetAddressType
_WwpLeosFTransferServerInetAddrType_Object=MibScalar
wwpLeosFTransferServerInetAddrType=_WwpLeosFTransferServerInetAddrType_Object((1,3,6,1,4,1,6141,2,60,23,1,1,11),_WwpLeosFTransferServerInetAddrType_Type())
wwpLeosFTransferServerInetAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosFTransferServerInetAddrType.setStatus(_A)
_WwpLeosFTransferServerInetAddr_Type=InetAddress
_WwpLeosFTransferServerInetAddr_Object=MibScalar
wwpLeosFTransferServerInetAddr=_WwpLeosFTransferServerInetAddr_Object((1,3,6,1,4,1,6141,2,60,23,1,1,12),_WwpLeosFTransferServerInetAddr_Type())
wwpLeosFTransferServerInetAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosFTransferServerInetAddr.setStatus(_A)
_WwpLeosFileTransferMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosFileTransferMIBNotificationPrefix=_WwpLeosFileTransferMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,23,2))
_WwpLeosFiletransferMIBNotifications_ObjectIdentity=ObjectIdentity
wwpLeosFiletransferMIBNotifications=_WwpLeosFiletransferMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,23,2,0))
_WwpLeosFileTransferMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosFileTransferMIBConformance=_WwpLeosFileTransferMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,23,3))
_WwpLeosFileTransferMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosFileTransferMIBCompliances=_WwpLeosFileTransferMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,23,3,1))
_WwpLeosFileTransferMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosFileTransferMIBGroups=_WwpLeosFileTransferMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,23,3,2))
wwpLeosFileTransferIPv6Group=ObjectGroup((1,3,6,1,4,1,6141,2,60,23,3,2,1))
wwpLeosFileTransferIPv6Group.setObjects(*((_C,_K),(_C,_L)))
if mibBuilder.loadTexts:wwpLeosFileTransferIPv6Group.setStatus(_A)
wwpLeosFTransferCompletion=NotificationType((1,3,6,1,4,1,6141,2,60,23,2,0,1))
wwpLeosFTransferCompletion.setObjects(*((_C,_M),(_C,_N),(_C,_O),(_C,_P)))
if mibBuilder.loadTexts:wwpLeosFTransferCompletion.setStatus(_A)
wwpLeosFileTransferCompliance=ModuleCompliance((1,3,6,1,4,1,6141,2,60,23,3,1,1))
wwpLeosFileTransferCompliance.setObjects((_C,_Q))
if mibBuilder.loadTexts:wwpLeosFileTransferCompliance.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'FileTransferState':FileTransferState,'FileTransferFailCause':FileTransferFailCause,'wwpLeosFileTransferMIB':wwpLeosFileTransferMIB,'wwpLeosFileTransferMIBObjects':wwpLeosFileTransferMIBObjects,'wwpLeosFileTransfer':wwpLeosFileTransfer,'wwpLeosFTransferOp':wwpLeosFTransferOp,'wwpLeosFTransferServerAddr':wwpLeosFTransferServerAddr,_M:wwpLeosFTransferRemoteFilename,_N:wwpLeosFTransferLocalFilename,'wwpLeosFTransferActivate':wwpLeosFTransferActivate,'wwpLeosFTransferNotifOnCompletion':wwpLeosFTransferNotifOnCompletion,'wwpLeosFTransferStatus':wwpLeosFTransferStatus,'wwpLeosFTransferFailCause':wwpLeosFTransferFailCause,_O:wwpLeosFTransferNotificationStatus,_P:wwpLeosFTransferNotificationInfo,_K:wwpLeosFTransferServerInetAddrType,_L:wwpLeosFTransferServerInetAddr,'wwpLeosFileTransferMIBNotificationPrefix':wwpLeosFileTransferMIBNotificationPrefix,'wwpLeosFiletransferMIBNotifications':wwpLeosFiletransferMIBNotifications,'wwpLeosFTransferCompletion':wwpLeosFTransferCompletion,'wwpLeosFileTransferMIBConformance':wwpLeosFileTransferMIBConformance,'wwpLeosFileTransferMIBCompliances':wwpLeosFileTransferMIBCompliances,'wwpLeosFileTransferCompliance':wwpLeosFileTransferCompliance,'wwpLeosFileTransferMIBGroups':wwpLeosFileTransferMIBGroups,_Q:wwpLeosFileTransferIPv6Group})