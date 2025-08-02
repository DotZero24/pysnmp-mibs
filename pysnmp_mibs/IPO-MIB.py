_Ay='ipoGenSvcMiscNotificationObjectsGroup'
_Ax='ipoGenSvcMiscNotificationsGroup'
_Aw='ipoGenQosMonNotificationObjectsGroup'
_Av='ipoGenSOGNotificationsGroup'
_Au='ipoGenEmergencyCallSvcEvent'
_At='ipoGenLinkChangeSvcEvent'
_As='ipoGenLinkErrorSvcEvent'
_Ar='ipoGenLinkOperationalSvcEvent'
_Aq='ipoGenLinkFailureSvcEvent'
_Ap='ipoGenTrunkChangeSvcEvent'
_Ao='ipoGenTrunkErrorSvcEvent'
_An='ipoGenTrunkOperationalSvcEvent'
_Am='ipoGenTrunkFailureSvcEvent'
_Al='ipoGenServiceChangeSvcEvent'
_Ak='ipoGenServiceErrorSvcEvent'
_Aj='ipoGenServiceOperationalSvcEvent'
_Ai='ipoGenServiceFailureSvcEvent'
_Ah='ipoGenConfigChangeSvcEvent'
_Ag='ipoGenConfigErrorSvcEvent'
_Af='ipoGenConfigOperationalSvcEvent'
_Ae='ipoGenConfigFailureSvcEvent'
_Ad='ipoGenMemoryCardCapacityEvent'
_Ac='ipoGenNoLicenceKeyDongleEvent'
_Ab='ipoGenInvalidMemoryCardEvent'
_Aa='ipoGenSystemRunningBackupEvent'
_AZ='ipoGenSystemShutdownSvcEvent'
_AY='ipoGenQoSMonSvcEvent'
_AX='ipoGenUPriLicCallRejectedSvcEvent'
_AW='ipoGenUPriLicChansReducedSvcEvent'
_AV='ipoGenSogModeChangeSvcEvent'
_AU='ipoGenSogHostFailureSvcEvent'
_AT='ipoGenLoopbackSvcEvent'
_AS='ipoGenLKSCommsChangeSvcEvent'
_AR='ipoGenLKSCommsErrorSvcEvent'
_AQ='ipoGenLKSCommsOperationalSvcEvent'
_AP='ipoGenLKSCommsFailureSvcEvent'
_AO='ipoGenEntityChangeSvcEvent'
_AN='ipoGenEntityErrorSvcEvent'
_AM='ipoGenEntityOperationalSvcEvent'
_AL='ipoGenEntityFailureSvcEvent'
_AK='ipoGenAuthFailureSvcEvent'
_AJ='ipoGenLinkUpSvcEvent'
_AI='ipoGenLinkDownSvcEvent'
_AH='ipoGenWarmStartSvcEvent'
_AG='ipoGenColdStartSvcEvent'
_AF='ipoGenSogModeChangeEvent'
_AE='ipoGenSogHostFailureEvent'
_AD='ipoGenAppEvent'
_AC='ipoGenAppFailureEvent'
_AB='ipoGenAppOperationalEvent'
_AA='ipoGenLoopbackEvent'
_A9='ipoGenLKSCommsChangeEvent'
_A8='ipoGenLKSCommsErrorEvent'
_A7='ipoGenLKSCommsOperationalEvent'
_A6='ipoGenLKSCommsFailureEvent'
_A5='ipoGenEntityChangeEvent'
_A4='ipoGenEntityErrorEvent'
_A3='ipoGenEntityOperationalEvent'
_A2='ipoGenEntityFailureEvent'
_A1='2014-06-25 00:00'
_A0='ipoGenSDcardNotificationObjectsGroup'
_z='ipoGenSDcardNotificationsGroup'
_y='ipoGenSvcSystemShutdownObjectGroup'
_x='ipoGenSvcSystemShutdownNotificationsGroup'
_w='ipoGenNotificationsGroup'
_v='ipoGenNotificationObjectsGroup'
_u='ipoGenAppSvcEvent'
_t='ipoGenAppFailureSvcEvent'
_s='ipoGenAppOperationalSvcEvent'
_r='ipoGTEventNoValidKeyReason'
_q='ipoGTEventSystemShutdownTimeout'
_p='ipoGTEventSystemShutdownSource'
_o='ipoGTEventQoSMonExtnNo'
_n='ipoGTEventQoSMonDevId'
_m='ipoGTEventQoSMonDevType'
_l='ipoGTEventQoSMonCallId'
_k='ipoGTEventQoSMonPktLoss'
_j='ipoGTEventQoSMonRndTrip'
_i='ipoGTEventQoSMonJitter'
_h='ipoGTEventLoopbackStatusBits'
_g='ipoGTEventLoopbackStatus'
_f='ifIndex'
_e='IF-MIB'
_d='ipoGenSvcQoSMonNotificationsGroup'
_c='ipoGTEventMemoryCardSlotId'
_b='ipoGTEventSOGMode'
_a='ipoGTEventHostAddress'
_Z='ipoGenUPriLicSvcNotificationsGroup'
_Y='ipoGenSvcSOGNotificationsGroup'
_X='ipoGenSvcNotificationsGroup'
_W='ipoGenEntGenNotificationsGroup'
_V='ipoGenv2NotificationObjectsGroup'
_U='ipoGTEventAppEvent'
_T='ipoGenSOGNotificationObjectsGroup'
_S='ipoGTEventEntityName'
_R='SnmpAdminString'
_Q='ipoGTEventAppEntity'
_P='Integer32'
_O='ipoGTEventEntity'
_N='ipoGTEventAlarmRemedialAction'
_M='ipoGTEventAlarmDescription'
_L='ipoGTEventSeverity'
_K='ipoGTEventData'
_J='ipoGTEventReason'
_I='deprecated'
_H='accessible-for-notify'
_G='sysDescr'
_F='SNMPv2-MIB'
_E='ipoGTEventDevID'
_D='ipoGTEventStdSeverity'
_C='ipoGTEventDateTime'
_B='current'
_A='IPO-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mibs,=mibBuilder.importSymbols('AVAYAGEN-MIB','mibs')
ifIndex,=mibBuilder.importSymbols(_e,_f)
ItuPerceivedSeverity,=mibBuilder.importSymbols('ITU-ALARM-TC-MIB','ItuPerceivedSeverity')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_R)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysDescr,=mibBuilder.importSymbols(_F,_G)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_P,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
ipoMIB=ModuleIdentity((1,3,6,1,4,1,6889,2,2))
if mibBuilder.loadTexts:ipoMIB.setRevisions(('2014-07-04 00:00',_A1,_A1,'2014-06-16 00:00','2014-06-04 00:00','2014-05-23 00:00','2014-05-08 00:00','2014-01-06 00:00','2013-10-08 00:00','2013-08-06 00:00','2013-04-24 19:00','2013-04-24 15:18','2012-11-17 15:11','2012-02-28 13:00','2011-11-01 22:00','2011-09-27 11:30','2011-03-15 15:17','2010-10-13 14:17','2010-07-12 13:45','2009-10-19 07:35','2009-10-09 13:47','2009-09-11 09:50','2009-09-07 16:20','2008-04-28 16:40','2008-04-18 14:50','2006-06-29 00:00','2004-10-06 00:00','2004-08-27 00:00','2004-08-06 00:00','2004-07-10 00:00','2004-05-28 00:00','2004-03-03 00:00','2003-12-15 00:00','2003-11-11 00:00','2003-10-10 00:00'))
_IpoGeneric_ObjectIdentity=ObjectIdentity
ipoGeneric=_IpoGeneric_ObjectIdentity((1,3,6,1,4,1,6889,2,2,1))
_IpoGenMibs_ObjectIdentity=ObjectIdentity
ipoGenMibs=_IpoGenMibs_ObjectIdentity((1,3,6,1,4,1,6889,2,2,1,1))
_IpoGenTraps_ObjectIdentity=ObjectIdentity
ipoGenTraps=_IpoGenTraps_ObjectIdentity((1,3,6,1,4,1,6889,2,2,1,2))
_IpoGTEvents_ObjectIdentity=ObjectIdentity
ipoGTEvents=_IpoGTEvents_ObjectIdentity((1,3,6,1,4,1,6889,2,2,1,2,0))
_IpoGTObjects_ObjectIdentity=ObjectIdentity
ipoGTObjects=_IpoGTObjects_ObjectIdentity((1,3,6,1,4,1,6889,2,2,1,2,1))
class _IpoGTEventSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('critical',1),('major',2),('minor',3)))
_IpoGTEventSeverity_Type.__name__=_P
_IpoGTEventSeverity_Object=MibScalar
ipoGTEventSeverity=_IpoGTEventSeverity_Object((1,3,6,1,4,1,6889,2,2,1,2,1,1),_IpoGTEventSeverity_Type())
ipoGTEventSeverity.setMaxAccess(_H)
if mibBuilder.loadTexts:ipoGTEventSeverity.setStatus(_I)
_IpoGTEventDateTime_Type=DateAndTime
_IpoGTEventDateTime_Object=MibScalar
ipoGTEventDateTime=_IpoGTEventDateTime_Object((1,3,6,1,4,1,6889,2,2,1,2,1,2),_IpoGTEventDateTime_Type())
ipoGTEventDateTime.setMaxAccess(_H)
if mibBuilder.loadTexts:ipoGTEventDateTime.setStatus(_B)
_IpoGTEventEntity_Type=Unsigned32
_IpoGTEventEntity_Object=MibScalar
ipoGTEventEntity=_IpoGTEventEntity_Object((1,3,6,1,4,1,6889,2,2,1,2,1,3),_IpoGTEventEntity_Type())
ipoGTEventEntity.setMaxAccess(_H)
if mibBuilder.loadTexts:ipoGTEventEntity.setStatus(_B)
class _IpoGTEventLoopbackStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_IpoGTEventLoopbackStatus_Type.__name__=_P
_IpoGTEventLoopbackStatus_Object=MibScalar
ipoGTEventLoopbackStatus=_IpoGTEventLoopbackStatus_Object((1,3,6,1,4,1,6889,2,2,1,2,1,4),_IpoGTEventLoopbackStatus_Type())
ipoGTEventLoopbackStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:ipoGTEventLoopbackStatus.setStatus(_I)
class _IpoGTEventAppEntity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('voiceMail',1),('deltaServer',2),('customerCallReporter',3),('oneXPortal',4)))
_IpoGTEventAppEntity_Type.__name__=_P
_IpoGTEventAppEntity_Object=MibScalar
ipoGTEventAppEntity=_IpoGTEventAppEntity_Object((1,3,6,1,4,1,6889,2,2,1,2,1,5),_IpoGTEventAppEntity_Type())
ipoGTEventAppEntity.setMaxAccess(_H)
if mibBuilder.loadTexts:ipoGTEventAppEntity.setStatus(_B)
class _IpoGTEventAppEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73)));namedValues=NamedValues(*(('storageFull',1),('storageNearlyFull',2),('storageOkay',3),('backupCommunicationError',4),('backupFileError',5),('httpFailure',6),('httpSslAcceptFailure',7),('httpSslConnection',8),('httpSslFailure',9),('httpSslPortFailure',10),('ignoringRequest',11),('imapInitializationFailed',12),('imapInvalidMsgNr',13),('imapMailboxNotExist',14),('imapMessageInvalid',15),('imapMessageNotExist',16),('imapMessageNrNotExist',17),('imapMissingConnection',18),('imapMissingSettings',19),('imapNoLicence',20),('imapNotConfigured',21),('imapShiftConnection',22),('mapiInitializationFailed',23),('mapiMissingSettings',24),('mapiConnectionFailed',25),('mapiShiftConnection',26),('licence',27),('licenceDistributed',28),('licenceExpired',29),('licenceSOG',30),('loginFailure',31),('loginFailureInvalidMailbox',32),('mailboxNotFound',33),('makeLiveFileAccess',34),('makeLiveMissingFile',35),('offlineMakeLive',36),('onexError',37),('pbxConnectionLost',38),('pbxIncompatibility',39),('smgrSettingsError',40),('smtpConnectionFailed',41),('smtpConnectionTimeout',42),('smtpError',43),('smtpSecureConnectionFailed',44),('smtpUnexpectedData',45),('smtpUnsuportedData',46),('socketAbortingError',47),('socketBindError',48),('socketClientDisconnectedError',49),('socketConnectionError',50),('socketNoresponseError',51),('socketOptionError',52),('socketReceiveError',53),('socketRecvFailedError',54),('socketSendFailedError',55),('socketSelectError',56),('socketTimedOutError',57),('switchedToPrimary',58),('switchedToSecondary',59),('tcpAcceptError',60),('tcpListenError',61),('tcpSelectError',62),('tcpError',63),('testTimeExpired',64),('tftpConnectionError',65),('tftpMonitoringError',66),('tftpReadingError',67),('tftpReceivingError',68),('tftpWrittingError',69),('tooManyClients',70),('updateEerror',71),('updateSuccess',72),('vmScript',73)))
_IpoGTEventAppEvent_Type.__name__=_P
_IpoGTEventAppEvent_Object=MibScalar
ipoGTEventAppEvent=_IpoGTEventAppEvent_Object((1,3,6,1,4,1,6889,2,2,1,2,1,6),_IpoGTEventAppEvent_Type())
ipoGTEventAppEvent.setMaxAccess(_H)
if mibBuilder.loadTexts:ipoGTEventAppEvent.setStatus(_B)
_IpoGTEventHostAddress_Type=IpAddress
_IpoGTEventHostAddress_Object=MibScalar
ipoGTEventHostAddress=_IpoGTEventHostAddress_Object((1,3,6,1,4,1,6889,2,2,1,2,1,7),_IpoGTEventHostAddress_Type())
ipoGTEventHostAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:ipoGTEventHostAddress.setStatus(_B)
class _IpoGTEventSOGMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('survivable',1),('subTending',2)))
_IpoGTEventSOGMode_Type.__name__=_P
_IpoGTEventSOGMode_Object=MibScalar
ipoGTEventSOGMode=_IpoGTEventSOGMode_Object((1,3,6,1,4,1,6889,2,2,1,2,1,8),_IpoGTEventSOGMode_Type())
ipoGTEventSOGMode.setMaxAccess(_H)
if mibBuilder.loadTexts:ipoGTEventSOGMode.setStatus(_B)
_IpoGTEventStdSeverity_Type=ItuPerceivedSeverity
_IpoGTEventStdSeverity_Object=MibScalar
ipoGTEventStdSeverity=_IpoGTEventStdSeverity_Object((1,3,6,1,4,1,6889,2,2,1,2,1,9),_IpoGTEventStdSeverity_Type())
ipoGTEventStdSeverity.setMaxAccess(_H)
if mibBuilder.loadTexts:ipoGTEventStdSeverity.setStatus(_B)
class _IpoGTEventDevID_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_IpoGTEventDevID_Type.__name__=_R
_IpoGTEventDevID_Object=MibScalar
ipoGTEventDevID=_IpoGTEventDevID_Object((1,3,6,1,4,1,6889,2,2,1,2,1,10),_IpoGTEventDevID_Type())
ipoGTEventDevID.setMaxAccess(_H)
if mibBuilder.loadTexts:ipoGTEventDevID.setStatus(_B)
class _IpoGTEventEntityName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_IpoGTEventEntityName_Type.__name__=_R
_IpoGTEventEntityName_Object=MibScalar
ipoGTEventEntityName=_IpoGTEventEntityName_Object((1,3,6,1,4,1,6889,2,2,1,2,1,11),_IpoGTEventEntityName_Type())
ipoGTEventEntityName.setMaxAccess(_H)
if mibBuilder.loadTexts:ipoGTEventEntityName.setStatus(_B)
class _IpoGTEventLoopbackStatusBits_Type(Bits):namedValues=NamedValues(*(('noLoopback',0),('nearEndPayloadLoopback',1),('nearEndLineLoopback',2),('nearEndOtherLoopback',3),('nearEndInwardLoopback',4),('farEndPayloadLoopback',5),('farEndLineLoopback',6)))
_IpoGTEventLoopbackStatusBits_Type.__name__='Bits'
_IpoGTEventLoopbackStatusBits_Object=MibScalar
ipoGTEventLoopbackStatusBits=_IpoGTEventLoopbackStatusBits_Object((1,3,6,1,4,1,6889,2,2,1,2,1,12),_IpoGTEventLoopbackStatusBits_Type())
ipoGTEventLoopbackStatusBits.setMaxAccess(_H)
if mibBuilder.loadTexts:ipoGTEventLoopbackStatusBits.setStatus(_B)
_IpoGTEventQoSMonJitter_Type=Unsigned32
_IpoGTEventQoSMonJitter_Object=MibScalar
ipoGTEventQoSMonJitter=_IpoGTEventQoSMonJitter_Object((1,3,6,1,4,1,6889,2,2,1,2,1,13),_IpoGTEventQoSMonJitter_Type())
ipoGTEventQoSMonJitter.setMaxAccess(_H)
if mibBuilder.loadTexts:ipoGTEventQoSMonJitter.setStatus(_B)
_IpoGTEventQoSMonRndTrip_Type=Unsigned32
_IpoGTEventQoSMonRndTrip_Object=MibScalar
ipoGTEventQoSMonRndTrip=_IpoGTEventQoSMonRndTrip_Object((1,3,6,1,4,1,6889,2,2,1,2,1,14),_IpoGTEventQoSMonRndTrip_Type())
ipoGTEventQoSMonRndTrip.setMaxAccess(_H)
if mibBuilder.loadTexts:ipoGTEventQoSMonRndTrip.setStatus(_B)
_IpoGTEventQoSMonPktLoss_Type=Unsigned32
_IpoGTEventQoSMonPktLoss_Object=MibScalar
ipoGTEventQoSMonPktLoss=_IpoGTEventQoSMonPktLoss_Object((1,3,6,1,4,1,6889,2,2,1,2,1,15),_IpoGTEventQoSMonPktLoss_Type())
ipoGTEventQoSMonPktLoss.setMaxAccess(_H)
if mibBuilder.loadTexts:ipoGTEventQoSMonPktLoss.setStatus(_B)
_IpoGTEventQoSMonCallId_Type=Unsigned32
_IpoGTEventQoSMonCallId_Object=MibScalar
ipoGTEventQoSMonCallId=_IpoGTEventQoSMonCallId_Object((1,3,6,1,4,1,6889,2,2,1,2,1,16),_IpoGTEventQoSMonCallId_Type())
ipoGTEventQoSMonCallId.setMaxAccess(_H)
if mibBuilder.loadTexts:ipoGTEventQoSMonCallId.setStatus(_B)
class _IpoGTEventQoSMonDevType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('line',1),('extn',2)))
_IpoGTEventQoSMonDevType_Type.__name__=_P
_IpoGTEventQoSMonDevType_Object=MibScalar
ipoGTEventQoSMonDevType=_IpoGTEventQoSMonDevType_Object((1,3,6,1,4,1,6889,2,2,1,2,1,17),_IpoGTEventQoSMonDevType_Type())
ipoGTEventQoSMonDevType.setMaxAccess(_H)
if mibBuilder.loadTexts:ipoGTEventQoSMonDevType.setStatus(_B)
_IpoGTEventQoSMonDevId_Type=Unsigned32
_IpoGTEventQoSMonDevId_Object=MibScalar
ipoGTEventQoSMonDevId=_IpoGTEventQoSMonDevId_Object((1,3,6,1,4,1,6889,2,2,1,2,1,18),_IpoGTEventQoSMonDevId_Type())
ipoGTEventQoSMonDevId.setMaxAccess(_H)
if mibBuilder.loadTexts:ipoGTEventQoSMonDevId.setStatus(_B)
_IpoGTEventQoSMonExtnNo_Type=Unsigned32
_IpoGTEventQoSMonExtnNo_Object=MibScalar
ipoGTEventQoSMonExtnNo=_IpoGTEventQoSMonExtnNo_Object((1,3,6,1,4,1,6889,2,2,1,2,1,19),_IpoGTEventQoSMonExtnNo_Type())
ipoGTEventQoSMonExtnNo.setMaxAccess(_H)
if mibBuilder.loadTexts:ipoGTEventQoSMonExtnNo.setStatus(_B)
class _IpoGTEventSystemShutdownSource_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IpoGTEventSystemShutdownSource_Type.__name__=_R
_IpoGTEventSystemShutdownSource_Object=MibScalar
ipoGTEventSystemShutdownSource=_IpoGTEventSystemShutdownSource_Object((1,3,6,1,4,1,6889,2,2,1,2,1,20),_IpoGTEventSystemShutdownSource_Type())
ipoGTEventSystemShutdownSource.setMaxAccess(_H)
if mibBuilder.loadTexts:ipoGTEventSystemShutdownSource.setStatus(_B)
_IpoGTEventSystemShutdownTimeout_Type=Unsigned32
_IpoGTEventSystemShutdownTimeout_Object=MibScalar
ipoGTEventSystemShutdownTimeout=_IpoGTEventSystemShutdownTimeout_Object((1,3,6,1,4,1,6889,2,2,1,2,1,21),_IpoGTEventSystemShutdownTimeout_Type())
ipoGTEventSystemShutdownTimeout.setMaxAccess(_H)
if mibBuilder.loadTexts:ipoGTEventSystemShutdownTimeout.setStatus(_B)
class _IpoGTEventMemoryCardSlotId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('compactFlash',1),('systemSD',2),('optionalSD',3)))
_IpoGTEventMemoryCardSlotId_Type.__name__=_P
_IpoGTEventMemoryCardSlotId_Object=MibScalar
ipoGTEventMemoryCardSlotId=_IpoGTEventMemoryCardSlotId_Object((1,3,6,1,4,1,6889,2,2,1,2,1,22),_IpoGTEventMemoryCardSlotId_Type())
ipoGTEventMemoryCardSlotId.setMaxAccess(_H)
if mibBuilder.loadTexts:ipoGTEventMemoryCardSlotId.setStatus(_B)
class _IpoGTEventNoValidKeyReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('noReason',1),('notPresent',2),('noRegisterAccess',3),('invalidRegisters',4),('invalidWatermark',5),('invalidClusterSize',6),('invalidVolume',7),('invalidHeaderFiles',8),('nonSpecificError',9)))
_IpoGTEventNoValidKeyReason_Type.__name__=_P
_IpoGTEventNoValidKeyReason_Object=MibScalar
ipoGTEventNoValidKeyReason=_IpoGTEventNoValidKeyReason_Object((1,3,6,1,4,1,6889,2,2,1,2,1,23),_IpoGTEventNoValidKeyReason_Type())
ipoGTEventNoValidKeyReason.setMaxAccess(_H)
if mibBuilder.loadTexts:ipoGTEventNoValidKeyReason.setStatus(_B)
class _IpoGTEventReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79)));namedValues=NamedValues(*(('configurationAgentNotTargeted',1),('configurationSCNDialPlanConflict',2),('configurationNoIncomingCallRoute',3),('configurationHWTypeFailure',4),('serviceFeatureLicenseMissing',5),('serviceAllLicensesInUse',6),('serviceClockSourceChanged',7),('serviceLogonFailed',8),('serviceNoFreeChannelsAvail',9),('serviceHoldMusicFileFailure',10),('serviceAllResourcesInUse',11),('serviceAlarm',12),('serviceNetworkInterconnectFailure',13),('trunkSeizeFailure',14),('trunkIncomingCallOutgoingTrunk',15),('trunkCLINotDelivered',16),('trunkDDIIncomplete',17),('trunkLOS',18),('trunkOOS',19),('trunkRedAlarm',20),('trunkBlueAlarm',21),('trunkYellowAlarm',22),('trunkIPConnectFail',23),('trunkSCNInvalidConnection',24),('linkDeviceChanged',25),('linkLDAPServerCommFailure',26),('linkResourceDown',27),('linkSMTPServerCommFailure',28),('linkVMProConnFailure',29),('serviceTimeServerAlarm',30),('serviceLicenseFileInvalid',31),('serviceLicenseError',32),('securityError',33),('codecError',34),('scepNoRespError',35),('configAppsProcAlarm',36),('serviceAppsProcAlarm',37),('serviceLicenseServerError',38),('testAlarm',39),('servicePlannedMaintenance',40),('serviceNetworkDisconnection',41),('serviceFailedTlsNegotiation',42),('serviceFailedTlsRenegotiation',43),('serviceLackOfResources',44),('serviceInternalError',45),('serviceTooManyMissedHeartbeats',46),('serviceFailedDnsResolution',47),('serviceDuplicateIpAddress',48),('serviceAuthenticationFailure',49),('serviceSslVpnStackProtocolError',50),('serviceSslVpnServerReportedError',51),('servicePortRangeExhausted',52),('serviceWebservicesUWSError',53),('trunkNoFreeVoIPChannel',54),('serviceEmergencyCall',55),('serviceLocationCongestion',56),('serviceCpuAlarm',57),('serviceCpuIOAlarm',58),('serviceMemoryAlarm',59),('serviceLocalBackup',60),('trunkSMConnectAsSIP',61),('trunkSIPConnectAsSM',62),('serviceSipRxPacketSizeError',63),('serviceACCSAlarm',64),('serviceSystemHardDriveAlarm',65),('serviceAdditionalHardDriveAlarm',66),('linkDialerConnFailure',67),('trunkSIPDNSInvalidConfig',68),('trunkSIPDNSTransportError',69),('monitorLogStamped',70),('trunkSCNInvalidSubOperMode',71),('serviceIPDECTSystemError',72),('serviceIPOCCAlarm',73),('serviceGeneralAlarm',74),('serviceSystemInfo',75),('serviceNonSelectAlarm',76),('serviceCCRNotSupported',77),('serviceAMServerNotAvailable',78),('trunkMediaSecuritySettingsIncompatible',79)))
_IpoGTEventReason_Type.__name__=_P
_IpoGTEventReason_Object=MibScalar
ipoGTEventReason=_IpoGTEventReason_Object((1,3,6,1,4,1,6889,2,2,1,2,1,24),_IpoGTEventReason_Type())
ipoGTEventReason.setMaxAccess(_H)
if mibBuilder.loadTexts:ipoGTEventReason.setStatus(_B)
class _IpoGTEventData_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IpoGTEventData_Type.__name__=_R
_IpoGTEventData_Object=MibScalar
ipoGTEventData=_IpoGTEventData_Object((1,3,6,1,4,1,6889,2,2,1,2,1,25),_IpoGTEventData_Type())
ipoGTEventData.setMaxAccess(_H)
if mibBuilder.loadTexts:ipoGTEventData.setStatus(_B)
class _IpoGTEventAlarmDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IpoGTEventAlarmDescription_Type.__name__=_R
_IpoGTEventAlarmDescription_Object=MibScalar
ipoGTEventAlarmDescription=_IpoGTEventAlarmDescription_Object((1,3,6,1,4,1,6889,2,2,1,2,1,26),_IpoGTEventAlarmDescription_Type())
ipoGTEventAlarmDescription.setMaxAccess(_H)
if mibBuilder.loadTexts:ipoGTEventAlarmDescription.setStatus(_B)
class _IpoGTEventAlarmRemedialAction_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IpoGTEventAlarmRemedialAction_Type.__name__=_R
_IpoGTEventAlarmRemedialAction_Object=MibScalar
ipoGTEventAlarmRemedialAction=_IpoGTEventAlarmRemedialAction_Object((1,3,6,1,4,1,6889,2,2,1,2,1,27),_IpoGTEventAlarmRemedialAction_Type())
ipoGTEventAlarmRemedialAction.setMaxAccess(_H)
if mibBuilder.loadTexts:ipoGTEventAlarmRemedialAction.setStatus(_B)
_IpoGenConformance_ObjectIdentity=ObjectIdentity
ipoGenConformance=_IpoGenConformance_ObjectIdentity((1,3,6,1,4,1,6889,2,2,1,3))
_IpoGenCompliances_ObjectIdentity=ObjectIdentity
ipoGenCompliances=_IpoGenCompliances_ObjectIdentity((1,3,6,1,4,1,6889,2,2,1,3,1))
_IpoGenGroups_ObjectIdentity=ObjectIdentity
ipoGenGroups=_IpoGenGroups_ObjectIdentity((1,3,6,1,4,1,6889,2,2,1,3,2))
ipoGenNotificationObjectsGroup=ObjectGroup((1,3,6,1,4,1,6889,2,2,1,3,2,1))
ipoGenNotificationObjectsGroup.setObjects(*((_A,_L),(_A,_C),(_A,_O),(_A,_g),(_A,_Q),(_A,_U)))
if mibBuilder.loadTexts:ipoGenNotificationObjectsGroup.setStatus(_I)
ipoGenSOGNotificationObjectsGroup=ObjectGroup((1,3,6,1,4,1,6889,2,2,1,3,2,3))
ipoGenSOGNotificationObjectsGroup.setObjects(*((_A,_a),(_A,_b)))
if mibBuilder.loadTexts:ipoGenSOGNotificationObjectsGroup.setStatus(_B)
ipoGenv2NotificationObjectsGroup=ObjectGroup((1,3,6,1,4,1,6889,2,2,1,3,2,5))
ipoGenv2NotificationObjectsGroup.setObjects(*((_A,_C),(_A,_O),(_A,_Q),(_A,_U),(_A,_D),(_A,_E),(_A,_S),(_A,_h)))
if mibBuilder.loadTexts:ipoGenv2NotificationObjectsGroup.setStatus(_B)
ipoGenQosMonNotificationObjectsGroup=ObjectGroup((1,3,6,1,4,1,6889,2,2,1,3,2,10))
ipoGenQosMonNotificationObjectsGroup.setObjects(*((_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:ipoGenQosMonNotificationObjectsGroup.setStatus(_B)
ipoGenSvcSystemShutdownObjectGroup=ObjectGroup((1,3,6,1,4,1,6889,2,2,1,3,2,12))
ipoGenSvcSystemShutdownObjectGroup.setObjects(*((_A,_p),(_A,_q)))
if mibBuilder.loadTexts:ipoGenSvcSystemShutdownObjectGroup.setStatus(_B)
ipoGenSDcardNotificationObjectsGroup=ObjectGroup((1,3,6,1,4,1,6889,2,2,1,3,2,14))
ipoGenSDcardNotificationObjectsGroup.setObjects(*((_A,_c),(_A,_r)))
if mibBuilder.loadTexts:ipoGenSDcardNotificationObjectsGroup.setStatus(_B)
ipoGenSvcMiscNotificationObjectsGroup=ObjectGroup((1,3,6,1,4,1,6889,2,2,1,3,2,16))
ipoGenSvcMiscNotificationObjectsGroup.setObjects(*((_A,_J),(_A,_K),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ipoGenSvcMiscNotificationObjectsGroup.setStatus(_B)
ipoGenEntityFailureEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,1))
ipoGenEntityFailureEvent.setObjects(*((_A,_L),(_A,_C),(_A,_O)))
if mibBuilder.loadTexts:ipoGenEntityFailureEvent.setStatus(_I)
ipoGenEntityOperationalEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,2))
ipoGenEntityOperationalEvent.setObjects(*((_A,_L),(_A,_C),(_A,_O)))
if mibBuilder.loadTexts:ipoGenEntityOperationalEvent.setStatus(_I)
ipoGenEntityErrorEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,3))
ipoGenEntityErrorEvent.setObjects(*((_A,_L),(_A,_C),(_A,_O)))
if mibBuilder.loadTexts:ipoGenEntityErrorEvent.setStatus(_I)
ipoGenEntityChangeEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,4))
ipoGenEntityChangeEvent.setObjects(*((_A,_L),(_A,_C),(_A,_O)))
if mibBuilder.loadTexts:ipoGenEntityChangeEvent.setStatus(_I)
ipoGenLKSCommsFailureEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,5))
ipoGenLKSCommsFailureEvent.setObjects(*((_A,_L),(_A,_C)))
if mibBuilder.loadTexts:ipoGenLKSCommsFailureEvent.setStatus(_I)
ipoGenLKSCommsOperationalEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,6))
ipoGenLKSCommsOperationalEvent.setObjects(*((_A,_L),(_A,_C)))
if mibBuilder.loadTexts:ipoGenLKSCommsOperationalEvent.setStatus(_I)
ipoGenLKSCommsErrorEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,7))
ipoGenLKSCommsErrorEvent.setObjects(*((_A,_L),(_A,_C)))
if mibBuilder.loadTexts:ipoGenLKSCommsErrorEvent.setStatus(_I)
ipoGenLKSCommsChangeEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,8))
ipoGenLKSCommsChangeEvent.setObjects(*((_A,_L),(_A,_C)))
if mibBuilder.loadTexts:ipoGenLKSCommsChangeEvent.setStatus(_I)
ipoGenLoopbackEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,9))
ipoGenLoopbackEvent.setObjects(*((_A,_L),(_A,_C),(_A,_O),(_A,_g)))
if mibBuilder.loadTexts:ipoGenLoopbackEvent.setStatus(_I)
ipoGenAppFailureEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,10))
ipoGenAppFailureEvent.setObjects(*((_A,_L),(_A,_C),(_A,_Q)))
if mibBuilder.loadTexts:ipoGenAppFailureEvent.setStatus(_I)
ipoGenAppOperationalEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,11))
ipoGenAppOperationalEvent.setObjects(*((_A,_L),(_A,_C),(_A,_Q)))
if mibBuilder.loadTexts:ipoGenAppOperationalEvent.setStatus(_I)
ipoGenAppEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,12))
ipoGenAppEvent.setObjects(*((_A,_L),(_A,_C),(_A,_Q),(_A,_U)))
if mibBuilder.loadTexts:ipoGenAppEvent.setStatus(_I)
ipoGenSogHostFailureEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,13))
ipoGenSogHostFailureEvent.setObjects(*((_A,_L),(_A,_C),(_A,_a)))
if mibBuilder.loadTexts:ipoGenSogHostFailureEvent.setStatus(_I)
ipoGenSogModeChangeEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,14))
ipoGenSogModeChangeEvent.setObjects(*((_A,_L),(_A,_C),(_A,_b)))
if mibBuilder.loadTexts:ipoGenSogModeChangeEvent.setStatus(_I)
ipoGenColdStartSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,15))
ipoGenColdStartSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G)))
if mibBuilder.loadTexts:ipoGenColdStartSvcEvent.setStatus(_B)
ipoGenWarmStartSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,16))
ipoGenWarmStartSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G)))
if mibBuilder.loadTexts:ipoGenWarmStartSvcEvent.setStatus(_B)
ipoGenLinkDownSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,17))
ipoGenLinkDownSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_e,_f)))
if mibBuilder.loadTexts:ipoGenLinkDownSvcEvent.setStatus(_B)
ipoGenLinkUpSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,18))
ipoGenLinkUpSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_e,_f)))
if mibBuilder.loadTexts:ipoGenLinkUpSvcEvent.setStatus(_B)
ipoGenAuthFailureSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,19))
ipoGenAuthFailureSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G)))
if mibBuilder.loadTexts:ipoGenAuthFailureSvcEvent.setStatus(_B)
ipoGenEntityFailureSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,20))
ipoGenEntityFailureSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_O),(_A,_S)))
if mibBuilder.loadTexts:ipoGenEntityFailureSvcEvent.setStatus(_B)
ipoGenEntityOperationalSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,21))
ipoGenEntityOperationalSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_O),(_A,_S)))
if mibBuilder.loadTexts:ipoGenEntityOperationalSvcEvent.setStatus(_B)
ipoGenEntityErrorSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,22))
ipoGenEntityErrorSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_O),(_A,_S)))
if mibBuilder.loadTexts:ipoGenEntityErrorSvcEvent.setStatus(_B)
ipoGenEntityChangeSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,23))
ipoGenEntityChangeSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_O),(_A,_S)))
if mibBuilder.loadTexts:ipoGenEntityChangeSvcEvent.setStatus(_B)
ipoGenLKSCommsFailureSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,24))
ipoGenLKSCommsFailureSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G)))
if mibBuilder.loadTexts:ipoGenLKSCommsFailureSvcEvent.setStatus(_B)
ipoGenLKSCommsOperationalSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,25))
ipoGenLKSCommsOperationalSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G)))
if mibBuilder.loadTexts:ipoGenLKSCommsOperationalSvcEvent.setStatus(_B)
ipoGenLKSCommsErrorSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,26))
ipoGenLKSCommsErrorSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G)))
if mibBuilder.loadTexts:ipoGenLKSCommsErrorSvcEvent.setStatus(_B)
ipoGenLKSCommsChangeSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,27))
ipoGenLKSCommsChangeSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G)))
if mibBuilder.loadTexts:ipoGenLKSCommsChangeSvcEvent.setStatus(_B)
ipoGenLoopbackSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,28))
ipoGenLoopbackSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_O),(_A,_S),(_A,_h)))
if mibBuilder.loadTexts:ipoGenLoopbackSvcEvent.setStatus(_B)
ipoGenAppFailureSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,29))
ipoGenAppFailureSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_Q)))
if mibBuilder.loadTexts:ipoGenAppFailureSvcEvent.setStatus(_B)
ipoGenAppOperationalSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,30))
ipoGenAppOperationalSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_Q)))
if mibBuilder.loadTexts:ipoGenAppOperationalSvcEvent.setStatus(_B)
ipoGenAppSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,31))
ipoGenAppSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_Q),(_A,_U),(_A,_M)))
if mibBuilder.loadTexts:ipoGenAppSvcEvent.setStatus(_B)
ipoGenSogHostFailureSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,32))
ipoGenSogHostFailureSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_a)))
if mibBuilder.loadTexts:ipoGenSogHostFailureSvcEvent.setStatus(_B)
ipoGenSogModeChangeSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,33))
ipoGenSogModeChangeSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_b)))
if mibBuilder.loadTexts:ipoGenSogModeChangeSvcEvent.setStatus(_B)
ipoGenUPriLicChansReducedSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,34))
ipoGenUPriLicChansReducedSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G)))
if mibBuilder.loadTexts:ipoGenUPriLicChansReducedSvcEvent.setStatus(_B)
ipoGenUPriLicCallRejectedSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,35))
ipoGenUPriLicCallRejectedSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G)))
if mibBuilder.loadTexts:ipoGenUPriLicCallRejectedSvcEvent.setStatus(_B)
ipoGenQoSMonSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,36))
ipoGenQoSMonSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:ipoGenQoSMonSvcEvent.setStatus(_B)
ipoGenSystemShutdownSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,37))
ipoGenSystemShutdownSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:ipoGenSystemShutdownSvcEvent.setStatus(_B)
ipoGenSystemRunningBackupEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,38))
ipoGenSystemRunningBackupEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G)))
if mibBuilder.loadTexts:ipoGenSystemRunningBackupEvent.setStatus(_B)
ipoGenInvalidMemoryCardEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,39))
ipoGenInvalidMemoryCardEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_c)))
if mibBuilder.loadTexts:ipoGenInvalidMemoryCardEvent.setStatus(_B)
ipoGenNoLicenceKeyDongleEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,40))
ipoGenNoLicenceKeyDongleEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_r)))
if mibBuilder.loadTexts:ipoGenNoLicenceKeyDongleEvent.setStatus(_B)
ipoGenMemoryCardCapacityEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,41))
ipoGenMemoryCardCapacityEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_c),(_A,_U)))
if mibBuilder.loadTexts:ipoGenMemoryCardCapacityEvent.setStatus(_B)
ipoGenConfigFailureSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,42))
ipoGenConfigFailureSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_J),(_A,_K),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ipoGenConfigFailureSvcEvent.setStatus(_B)
ipoGenConfigOperationalSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,43))
ipoGenConfigOperationalSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:ipoGenConfigOperationalSvcEvent.setStatus(_B)
ipoGenConfigErrorSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,44))
ipoGenConfigErrorSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_J),(_A,_K),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ipoGenConfigErrorSvcEvent.setStatus(_B)
ipoGenConfigChangeSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,45))
ipoGenConfigChangeSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_J),(_A,_K),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ipoGenConfigChangeSvcEvent.setStatus(_B)
ipoGenServiceFailureSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,46))
ipoGenServiceFailureSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_J),(_A,_K),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ipoGenServiceFailureSvcEvent.setStatus(_B)
ipoGenServiceOperationalSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,47))
ipoGenServiceOperationalSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:ipoGenServiceOperationalSvcEvent.setStatus(_B)
ipoGenServiceErrorSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,48))
ipoGenServiceErrorSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_J),(_A,_K),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ipoGenServiceErrorSvcEvent.setStatus(_B)
ipoGenServiceChangeSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,49))
ipoGenServiceChangeSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_J),(_A,_K),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ipoGenServiceChangeSvcEvent.setStatus(_B)
ipoGenTrunkFailureSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,50))
ipoGenTrunkFailureSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_J),(_A,_K),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ipoGenTrunkFailureSvcEvent.setStatus(_B)
ipoGenTrunkOperationalSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,51))
ipoGenTrunkOperationalSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:ipoGenTrunkOperationalSvcEvent.setStatus(_B)
ipoGenTrunkErrorSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,52))
ipoGenTrunkErrorSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_J),(_A,_K),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ipoGenTrunkErrorSvcEvent.setStatus(_B)
ipoGenTrunkChangeSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,53))
ipoGenTrunkChangeSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_J),(_A,_K),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ipoGenTrunkChangeSvcEvent.setStatus(_B)
ipoGenLinkFailureSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,54))
ipoGenLinkFailureSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_J),(_A,_K),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ipoGenLinkFailureSvcEvent.setStatus(_B)
ipoGenLinkOperationalSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,55))
ipoGenLinkOperationalSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:ipoGenLinkOperationalSvcEvent.setStatus(_B)
ipoGenLinkErrorSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,56))
ipoGenLinkErrorSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_J),(_A,_K),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ipoGenLinkErrorSvcEvent.setStatus(_B)
ipoGenLinkChangeSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,57))
ipoGenLinkChangeSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_J),(_A,_K),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ipoGenLinkChangeSvcEvent.setStatus(_B)
ipoGenEmergencyCallSvcEvent=NotificationType((1,3,6,1,4,1,6889,2,2,1,2,0,58))
ipoGenEmergencyCallSvcEvent.setObjects(*((_A,_D),(_A,_C),(_A,_E),(_F,_G),(_A,_J),(_A,_K),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ipoGenEmergencyCallSvcEvent.setStatus(_B)
ipoGenNotificationsGroup=NotificationGroup((1,3,6,1,4,1,6889,2,2,1,3,2,2))
ipoGenNotificationsGroup.setObjects(*((_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD)))
if mibBuilder.loadTexts:ipoGenNotificationsGroup.setStatus(_I)
ipoGenSOGNotificationsGroup=NotificationGroup((1,3,6,1,4,1,6889,2,2,1,3,2,4))
ipoGenSOGNotificationsGroup.setObjects(*((_A,_AE),(_A,_AF)))
if mibBuilder.loadTexts:ipoGenSOGNotificationsGroup.setStatus(_I)
ipoGenEntGenNotificationsGroup=NotificationGroup((1,3,6,1,4,1,6889,2,2,1,3,2,6))
ipoGenEntGenNotificationsGroup.setObjects(*((_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:ipoGenEntGenNotificationsGroup.setStatus(_B)
ipoGenSvcNotificationsGroup=NotificationGroup((1,3,6,1,4,1,6889,2,2,1,3,2,7))
ipoGenSvcNotificationsGroup.setObjects(*((_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_s),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:ipoGenSvcNotificationsGroup.setStatus(_B)
ipoGenSvcSOGNotificationsGroup=NotificationGroup((1,3,6,1,4,1,6889,2,2,1,3,2,8))
ipoGenSvcSOGNotificationsGroup.setObjects(*((_A,_AU),(_A,_AV)))
if mibBuilder.loadTexts:ipoGenSvcSOGNotificationsGroup.setStatus(_B)
ipoGenUPriLicSvcNotificationsGroup=NotificationGroup((1,3,6,1,4,1,6889,2,2,1,3,2,9))
ipoGenUPriLicSvcNotificationsGroup.setObjects(*((_A,_AW),(_A,_AX)))
if mibBuilder.loadTexts:ipoGenUPriLicSvcNotificationsGroup.setStatus(_B)
ipoGenSvcQoSMonNotificationsGroup=NotificationGroup((1,3,6,1,4,1,6889,2,2,1,3,2,11))
ipoGenSvcQoSMonNotificationsGroup.setObjects((_A,_AY))
if mibBuilder.loadTexts:ipoGenSvcQoSMonNotificationsGroup.setStatus(_B)
ipoGenSvcSystemShutdownNotificationsGroup=NotificationGroup((1,3,6,1,4,1,6889,2,2,1,3,2,13))
ipoGenSvcSystemShutdownNotificationsGroup.setObjects((_A,_AZ))
if mibBuilder.loadTexts:ipoGenSvcSystemShutdownNotificationsGroup.setStatus(_B)
ipoGenSDcardNotificationsGroup=NotificationGroup((1,3,6,1,4,1,6889,2,2,1,3,2,15))
ipoGenSDcardNotificationsGroup.setObjects(*((_A,_s),(_A,_t),(_A,_u),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad)))
if mibBuilder.loadTexts:ipoGenSDcardNotificationsGroup.setStatus(_B)
ipoGenSvcMiscNotificationsGroup=NotificationGroup((1,3,6,1,4,1,6889,2,2,1,3,2,17))
ipoGenSvcMiscNotificationsGroup.setObjects(*((_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At),(_A,_Au)))
if mibBuilder.loadTexts:ipoGenSvcMiscNotificationsGroup.setStatus(_B)
ipoGenCompliance=ModuleCompliance((1,3,6,1,4,1,6889,2,2,1,3,1,1))
ipoGenCompliance.setObjects(*((_A,_v),(_A,_w)))
if mibBuilder.loadTexts:ipoGenCompliance.setStatus(_I)
ipoGen2Compliance=ModuleCompliance((1,3,6,1,4,1,6889,2,2,1,3,1,2))
ipoGen2Compliance.setObjects(*((_A,_v),(_A,_w),(_A,_T),(_A,_Av)))
if mibBuilder.loadTexts:ipoGen2Compliance.setStatus(_I)
ipoGen3Compliance=ModuleCompliance((1,3,6,1,4,1,6889,2,2,1,3,1,3))
ipoGen3Compliance.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_T),(_A,_Y)))
if mibBuilder.loadTexts:ipoGen3Compliance.setStatus(_I)
ipoGen4Compliance=ModuleCompliance((1,3,6,1,4,1,6889,2,2,1,3,1,4))
ipoGen4Compliance.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_T),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:ipoGen4Compliance.setStatus(_I)
ipoGen5Compliance=ModuleCompliance((1,3,6,1,4,1,6889,2,2,1,3,1,5))
ipoGen5Compliance.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_T),(_A,_Y),(_A,_Z),(_A,_Aw),(_A,_d)))
if mibBuilder.loadTexts:ipoGen5Compliance.setStatus(_I)
ipoGen6Compliance=ModuleCompliance((1,3,6,1,4,1,6889,2,2,1,3,1,6))
ipoGen6Compliance.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_T),(_A,_Y),(_A,_Z),(_A,_d),(_A,_x),(_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:ipoGen6Compliance.setStatus(_I)
ipoGen7Compliance=ModuleCompliance((1,3,6,1,4,1,6889,2,2,1,3,1,7))
ipoGen7Compliance.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_Ax),(_A,_Ay),(_A,_T),(_A,_Y),(_A,_Z),(_A,_d),(_A,_x),(_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:ipoGen7Compliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ipoMIB':ipoMIB,'ipoGeneric':ipoGeneric,'ipoGenMibs':ipoGenMibs,'ipoGenTraps':ipoGenTraps,'ipoGTEvents':ipoGTEvents,_A2:ipoGenEntityFailureEvent,_A3:ipoGenEntityOperationalEvent,_A4:ipoGenEntityErrorEvent,_A5:ipoGenEntityChangeEvent,_A6:ipoGenLKSCommsFailureEvent,_A7:ipoGenLKSCommsOperationalEvent,_A8:ipoGenLKSCommsErrorEvent,_A9:ipoGenLKSCommsChangeEvent,_AA:ipoGenLoopbackEvent,_AC:ipoGenAppFailureEvent,_AB:ipoGenAppOperationalEvent,_AD:ipoGenAppEvent,_AE:ipoGenSogHostFailureEvent,_AF:ipoGenSogModeChangeEvent,_AG:ipoGenColdStartSvcEvent,_AH:ipoGenWarmStartSvcEvent,_AI:ipoGenLinkDownSvcEvent,_AJ:ipoGenLinkUpSvcEvent,_AK:ipoGenAuthFailureSvcEvent,_AL:ipoGenEntityFailureSvcEvent,_AM:ipoGenEntityOperationalSvcEvent,_AN:ipoGenEntityErrorSvcEvent,_AO:ipoGenEntityChangeSvcEvent,_AP:ipoGenLKSCommsFailureSvcEvent,_AQ:ipoGenLKSCommsOperationalSvcEvent,_AR:ipoGenLKSCommsErrorSvcEvent,_AS:ipoGenLKSCommsChangeSvcEvent,_AT:ipoGenLoopbackSvcEvent,_t:ipoGenAppFailureSvcEvent,_s:ipoGenAppOperationalSvcEvent,_u:ipoGenAppSvcEvent,_AU:ipoGenSogHostFailureSvcEvent,_AV:ipoGenSogModeChangeSvcEvent,_AW:ipoGenUPriLicChansReducedSvcEvent,_AX:ipoGenUPriLicCallRejectedSvcEvent,_AY:ipoGenQoSMonSvcEvent,_AZ:ipoGenSystemShutdownSvcEvent,_Aa:ipoGenSystemRunningBackupEvent,_Ab:ipoGenInvalidMemoryCardEvent,_Ac:ipoGenNoLicenceKeyDongleEvent,_Ad:ipoGenMemoryCardCapacityEvent,_Ae:ipoGenConfigFailureSvcEvent,_Af:ipoGenConfigOperationalSvcEvent,_Ag:ipoGenConfigErrorSvcEvent,_Ah:ipoGenConfigChangeSvcEvent,_Ai:ipoGenServiceFailureSvcEvent,_Aj:ipoGenServiceOperationalSvcEvent,_Ak:ipoGenServiceErrorSvcEvent,_Al:ipoGenServiceChangeSvcEvent,_Am:ipoGenTrunkFailureSvcEvent,_An:ipoGenTrunkOperationalSvcEvent,_Ao:ipoGenTrunkErrorSvcEvent,_Ap:ipoGenTrunkChangeSvcEvent,_Aq:ipoGenLinkFailureSvcEvent,_Ar:ipoGenLinkOperationalSvcEvent,_As:ipoGenLinkErrorSvcEvent,_At:ipoGenLinkChangeSvcEvent,_Au:ipoGenEmergencyCallSvcEvent,'ipoGTObjects':ipoGTObjects,_L:ipoGTEventSeverity,_C:ipoGTEventDateTime,_O:ipoGTEventEntity,_g:ipoGTEventLoopbackStatus,_Q:ipoGTEventAppEntity,_U:ipoGTEventAppEvent,_a:ipoGTEventHostAddress,_b:ipoGTEventSOGMode,_D:ipoGTEventStdSeverity,_E:ipoGTEventDevID,_S:ipoGTEventEntityName,_h:ipoGTEventLoopbackStatusBits,_i:ipoGTEventQoSMonJitter,_j:ipoGTEventQoSMonRndTrip,_k:ipoGTEventQoSMonPktLoss,_l:ipoGTEventQoSMonCallId,_m:ipoGTEventQoSMonDevType,_n:ipoGTEventQoSMonDevId,_o:ipoGTEventQoSMonExtnNo,_p:ipoGTEventSystemShutdownSource,_q:ipoGTEventSystemShutdownTimeout,_c:ipoGTEventMemoryCardSlotId,_r:ipoGTEventNoValidKeyReason,_J:ipoGTEventReason,_K:ipoGTEventData,_M:ipoGTEventAlarmDescription,_N:ipoGTEventAlarmRemedialAction,'ipoGenConformance':ipoGenConformance,'ipoGenCompliances':ipoGenCompliances,'ipoGenCompliance':ipoGenCompliance,'ipoGen2Compliance':ipoGen2Compliance,'ipoGen3Compliance':ipoGen3Compliance,'ipoGen4Compliance':ipoGen4Compliance,'ipoGen5Compliance':ipoGen5Compliance,'ipoGen6Compliance':ipoGen6Compliance,'ipoGen7Compliance':ipoGen7Compliance,'ipoGenGroups':ipoGenGroups,_v:ipoGenNotificationObjectsGroup,_w:ipoGenNotificationsGroup,_T:ipoGenSOGNotificationObjectsGroup,_Av:ipoGenSOGNotificationsGroup,_V:ipoGenv2NotificationObjectsGroup,_W:ipoGenEntGenNotificationsGroup,_X:ipoGenSvcNotificationsGroup,_Y:ipoGenSvcSOGNotificationsGroup,_Z:ipoGenUPriLicSvcNotificationsGroup,_Aw:ipoGenQosMonNotificationObjectsGroup,_d:ipoGenSvcQoSMonNotificationsGroup,_y:ipoGenSvcSystemShutdownObjectGroup,_x:ipoGenSvcSystemShutdownNotificationsGroup,_A0:ipoGenSDcardNotificationObjectsGroup,_z:ipoGenSDcardNotificationsGroup,_Ay:ipoGenSvcMiscNotificationObjectsGroup,_Ax:ipoGenSvcMiscNotificationsGroup})