_L='wwpFTransferNotificationInfo'
_K='wwpFTransferNotificationStatus'
_J='wwpFTransferLocalFilename'
_I='noStatus'
_H='wwpFTransferRemoteFilename'
_G='TruthValue'
_F='DisplayString'
_E='Integer32'
_D='read-only'
_C='WWP-FILE-TRANSFER-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention',_G)
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpFileTransferMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,7))
if mibBuilder.loadTexts:wwpFileTransferMIB.setRevisions(('2001-04-03 17:00',))
class FileTransferState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('idle',1),('sending',2),('receiving',3),('transferComplete',4),('failed',5)))
class FileTransferFailCause(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_I,1),('timeout',2),('networkError',3),('noSpace',4),('invalidFileName',5),('commandCompleted',6),('internalError',7),('commandFileParseError',8)))
_WwpFileTransferMIBObjects_ObjectIdentity=ObjectIdentity
wwpFileTransferMIBObjects=_WwpFileTransferMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,7,1))
_WwpFileTransfer_ObjectIdentity=ObjectIdentity
wwpFileTransfer=_WwpFileTransfer_ObjectIdentity((1,3,6,1,4,1,6141,2,7,1,1))
class _WwpFTransferOp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('sendFile',1),('getFile',2),('getCmdFile',3)))
_WwpFTransferOp_Type.__name__=_E
_WwpFTransferOp_Object=MibScalar
wwpFTransferOp=_WwpFTransferOp_Object((1,3,6,1,4,1,6141,2,7,1,1,1),_WwpFTransferOp_Type())
wwpFTransferOp.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpFTransferOp.setStatus(_A)
_WwpFTransferServerAddr_Type=IpAddress
_WwpFTransferServerAddr_Object=MibScalar
wwpFTransferServerAddr=_WwpFTransferServerAddr_Object((1,3,6,1,4,1,6141,2,7,1,1,2),_WwpFTransferServerAddr_Type())
wwpFTransferServerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpFTransferServerAddr.setStatus(_A)
class _WwpFTransferRemoteFilename_Type(DisplayString):defaultValue=OctetString('')
_WwpFTransferRemoteFilename_Type.__name__=_F
_WwpFTransferRemoteFilename_Object=MibScalar
wwpFTransferRemoteFilename=_WwpFTransferRemoteFilename_Object((1,3,6,1,4,1,6141,2,7,1,1,3),_WwpFTransferRemoteFilename_Type())
wwpFTransferRemoteFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpFTransferRemoteFilename.setStatus(_A)
_WwpFTransferLocalFilename_Type=DisplayString
_WwpFTransferLocalFilename_Object=MibScalar
wwpFTransferLocalFilename=_WwpFTransferLocalFilename_Object((1,3,6,1,4,1,6141,2,7,1,1,4),_WwpFTransferLocalFilename_Type())
wwpFTransferLocalFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpFTransferLocalFilename.setStatus(_A)
class _WwpFTransferActivate_Type(TruthValue):defaultValue=2
_WwpFTransferActivate_Type.__name__=_G
_WwpFTransferActivate_Object=MibScalar
wwpFTransferActivate=_WwpFTransferActivate_Object((1,3,6,1,4,1,6141,2,7,1,1,5),_WwpFTransferActivate_Type())
wwpFTransferActivate.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpFTransferActivate.setStatus(_A)
class _WwpFTransferNotifOnCompletion_Type(TruthValue):defaultValue=1
_WwpFTransferNotifOnCompletion_Type.__name__=_G
_WwpFTransferNotifOnCompletion_Object=MibScalar
wwpFTransferNotifOnCompletion=_WwpFTransferNotifOnCompletion_Object((1,3,6,1,4,1,6141,2,7,1,1,6),_WwpFTransferNotifOnCompletion_Type())
wwpFTransferNotifOnCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpFTransferNotifOnCompletion.setStatus(_A)
_WwpFTransferStatus_Type=FileTransferState
_WwpFTransferStatus_Object=MibScalar
wwpFTransferStatus=_WwpFTransferStatus_Object((1,3,6,1,4,1,6141,2,7,1,1,7),_WwpFTransferStatus_Type())
wwpFTransferStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpFTransferStatus.setStatus(_A)
_WwpFTransferFailCause_Type=FileTransferFailCause
_WwpFTransferFailCause_Object=MibScalar
wwpFTransferFailCause=_WwpFTransferFailCause_Object((1,3,6,1,4,1,6141,2,7,1,1,8),_WwpFTransferFailCause_Type())
wwpFTransferFailCause.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpFTransferFailCause.setStatus(_A)
class _WwpFTransferNotificationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('downloadSuccess',0),('tftpServerNotFound',1),('couldNotGetFile',2),('cmdFileParseError',3),('internalFilesystemError',4),('inValidFileContents',5),('flashOffline',6),(_I,7),('putSuccessful',8),('couldNotPutFile',9),('badFileCrc',10),('allFilesSkipped',11)))
_WwpFTransferNotificationStatus_Type.__name__=_E
_WwpFTransferNotificationStatus_Object=MibScalar
wwpFTransferNotificationStatus=_WwpFTransferNotificationStatus_Object((1,3,6,1,4,1,6141,2,7,1,1,9),_WwpFTransferNotificationStatus_Type())
wwpFTransferNotificationStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpFTransferNotificationStatus.setStatus(_A)
class _WwpFTransferNotificationInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_WwpFTransferNotificationInfo_Type.__name__=_F
_WwpFTransferNotificationInfo_Object=MibScalar
wwpFTransferNotificationInfo=_WwpFTransferNotificationInfo_Object((1,3,6,1,4,1,6141,2,7,1,1,10),_WwpFTransferNotificationInfo_Type())
wwpFTransferNotificationInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpFTransferNotificationInfo.setStatus(_A)
_WwpFileTransferMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpFileTransferMIBNotificationPrefix=_WwpFileTransferMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,7,2))
_WwpFiletransferMIBNotifications_ObjectIdentity=ObjectIdentity
wwpFiletransferMIBNotifications=_WwpFiletransferMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,7,2,0))
_WwpFileTransferMIBConformance_ObjectIdentity=ObjectIdentity
wwpFileTransferMIBConformance=_WwpFileTransferMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,7,3))
_WwpFileTransferMIBCompliances_ObjectIdentity=ObjectIdentity
wwpFileTransferMIBCompliances=_WwpFileTransferMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,7,3,1))
_WwpFileTransferMIBGroups_ObjectIdentity=ObjectIdentity
wwpFileTransferMIBGroups=_WwpFileTransferMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,7,3,2))
wwpFTransferCompletion=NotificationType((1,3,6,1,4,1,6141,2,7,2,0,1))
wwpFTransferCompletion.setObjects(*((_C,_H),(_C,_J),(_C,_K),(_C,_L)))
if mibBuilder.loadTexts:wwpFTransferCompletion.setStatus(_A)
wwpFTransferCmdParseError=NotificationType((1,3,6,1,4,1,6141,2,7,2,0,2))
wwpFTransferCmdParseError.setObjects((_C,_H))
if mibBuilder.loadTexts:wwpFTransferCmdParseError.setStatus('deprecated')
mibBuilder.exportSymbols(_C,**{'FileTransferState':FileTransferState,'FileTransferFailCause':FileTransferFailCause,'wwpFileTransferMIB':wwpFileTransferMIB,'wwpFileTransferMIBObjects':wwpFileTransferMIBObjects,'wwpFileTransfer':wwpFileTransfer,'wwpFTransferOp':wwpFTransferOp,'wwpFTransferServerAddr':wwpFTransferServerAddr,_H:wwpFTransferRemoteFilename,_J:wwpFTransferLocalFilename,'wwpFTransferActivate':wwpFTransferActivate,'wwpFTransferNotifOnCompletion':wwpFTransferNotifOnCompletion,'wwpFTransferStatus':wwpFTransferStatus,'wwpFTransferFailCause':wwpFTransferFailCause,_K:wwpFTransferNotificationStatus,_L:wwpFTransferNotificationInfo,'wwpFileTransferMIBNotificationPrefix':wwpFileTransferMIBNotificationPrefix,'wwpFiletransferMIBNotifications':wwpFiletransferMIBNotifications,'wwpFTransferCompletion':wwpFTransferCompletion,'wwpFTransferCmdParseError':wwpFTransferCmdParseError,'wwpFileTransferMIBConformance':wwpFileTransferMIBConformance,'wwpFileTransferMIBCompliances':wwpFileTransferMIBCompliances,'wwpFileTransferMIBGroups':wwpFileTransferMIBGroups})