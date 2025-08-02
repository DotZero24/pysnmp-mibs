_U='h3cSSHUserAuthFailureReason'
_T='h3cSSHAttemptUserName'
_S='h3cSSHSessionID'
_R='netconf'
_Q='stelnet'
_P='not-accessible'
_O='h3cSSHUserName'
_N='h3cSSHSessionUserIpAddr'
_M='h3cSSHSessionUserIpAddrType'
_L='h3cSSHSessionUserName'
_K='h3cSSHAttemptIpAddr'
_J='h3cSSHAttemptIpAddrType'
_I='accessible-for-notify'
_H='invalid'
_G='read-only'
_F='DisplayString'
_E='read-write'
_D='read-create'
_C='Integer32'
_B='H3C-SSH-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
h3cSSH=ModuleIdentity((1,3,6,1,4,1,2011,10,2,22))
if mibBuilder.loadTexts:h3cSSH.setRevisions(('2018-02-06 00:00','2016-04-26 00:00','2014-10-25 00:00','2014-02-20 00:00','2014-01-17 00:00','2013-12-21 00:00','2007-11-19 00:00'))
_H3cSSHServerMIB_ObjectIdentity=ObjectIdentity
h3cSSHServerMIB=_H3cSSHServerMIB_ObjectIdentity((1,3,6,1,4,1,2011,10,2,22,1))
_H3cSSHServerMIBObjects_ObjectIdentity=ObjectIdentity
h3cSSHServerMIBObjects=_H3cSSHServerMIBObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,22,1,1))
_H3cSSHServerGlobalConfig_ObjectIdentity=ObjectIdentity
h3cSSHServerGlobalConfig=_H3cSSHServerGlobalConfig_ObjectIdentity((1,3,6,1,4,1,2011,10,2,22,1,1,1))
_H3cSSHServerVersion_Type=DisplayString
_H3cSSHServerVersion_Object=MibScalar
h3cSSHServerVersion=_H3cSSHServerVersion_Object((1,3,6,1,4,1,2011,10,2,22,1,1,1,1),_H3cSSHServerVersion_Type())
h3cSSHServerVersion.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSSHServerVersion.setStatus(_A)
class _H3cSSHServerCompatibleSSH1x_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enableCompatibleSSH1x',1),('disableCompatibleSSH1x',2)))
_H3cSSHServerCompatibleSSH1x_Type.__name__=_C
_H3cSSHServerCompatibleSSH1x_Object=MibScalar
h3cSSHServerCompatibleSSH1x=_H3cSSHServerCompatibleSSH1x_Object((1,3,6,1,4,1,2011,10,2,22,1,1,1,2),_H3cSSHServerCompatibleSSH1x_Type())
h3cSSHServerCompatibleSSH1x.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSSHServerCompatibleSSH1x.setStatus(_A)
_H3cSSHServerRekeyInterval_Type=Integer32
_H3cSSHServerRekeyInterval_Object=MibScalar
h3cSSHServerRekeyInterval=_H3cSSHServerRekeyInterval_Object((1,3,6,1,4,1,2011,10,2,22,1,1,1,3),_H3cSSHServerRekeyInterval_Type())
h3cSSHServerRekeyInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSSHServerRekeyInterval.setStatus(_A)
_H3cSSHServerAuthRetries_Type=Integer32
_H3cSSHServerAuthRetries_Object=MibScalar
h3cSSHServerAuthRetries=_H3cSSHServerAuthRetries_Object((1,3,6,1,4,1,2011,10,2,22,1,1,1,4),_H3cSSHServerAuthRetries_Type())
h3cSSHServerAuthRetries.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSSHServerAuthRetries.setStatus(_A)
_H3cSSHServerAuthTimeout_Type=Integer32
_H3cSSHServerAuthTimeout_Object=MibScalar
h3cSSHServerAuthTimeout=_H3cSSHServerAuthTimeout_Object((1,3,6,1,4,1,2011,10,2,22,1,1,1,5),_H3cSSHServerAuthTimeout_Type())
h3cSSHServerAuthTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSSHServerAuthTimeout.setStatus(_A)
_H3cSFTPServerIdleTimeout_Type=Integer32
_H3cSFTPServerIdleTimeout_Object=MibScalar
h3cSFTPServerIdleTimeout=_H3cSFTPServerIdleTimeout_Object((1,3,6,1,4,1,2011,10,2,22,1,1,1,6),_H3cSFTPServerIdleTimeout_Type())
h3cSFTPServerIdleTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSFTPServerIdleTimeout.setStatus(_A)
class _H3cSSHServerEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enableSSHServer',1),('disableSSHServer',2)))
_H3cSSHServerEnable_Type.__name__=_C
_H3cSSHServerEnable_Object=MibScalar
h3cSSHServerEnable=_H3cSSHServerEnable_Object((1,3,6,1,4,1,2011,10,2,22,1,1,1,7),_H3cSSHServerEnable_Type())
h3cSSHServerEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSSHServerEnable.setStatus(_A)
class _H3cSFTPServerEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enableSFTPService',1),('disableSFTPService',2)))
_H3cSFTPServerEnable_Type.__name__=_C
_H3cSFTPServerEnable_Object=MibScalar
h3cSFTPServerEnable=_H3cSFTPServerEnable_Object((1,3,6,1,4,1,2011,10,2,22,1,1,1,8),_H3cSFTPServerEnable_Type())
h3cSFTPServerEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSFTPServerEnable.setStatus(_A)
class _H3cSTelnetServerEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enableSTelnetServer',1),('disableSTelnetServer',2)))
_H3cSTelnetServerEnable_Type.__name__=_C
_H3cSTelnetServerEnable_Object=MibScalar
h3cSTelnetServerEnable=_H3cSTelnetServerEnable_Object((1,3,6,1,4,1,2011,10,2,22,1,1,1,9),_H3cSTelnetServerEnable_Type())
h3cSTelnetServerEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSTelnetServerEnable.setStatus(_A)
class _H3cSCPServerEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enableSCPService',1),('disableSCPService',2)))
_H3cSCPServerEnable_Type.__name__=_C
_H3cSCPServerEnable_Object=MibScalar
h3cSCPServerEnable=_H3cSCPServerEnable_Object((1,3,6,1,4,1,2011,10,2,22,1,1,1,10),_H3cSCPServerEnable_Type())
h3cSCPServerEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSCPServerEnable.setStatus(_A)
_H3cSSHUserConfig_ObjectIdentity=ObjectIdentity
h3cSSHUserConfig=_H3cSSHUserConfig_ObjectIdentity((1,3,6,1,4,1,2011,10,2,22,1,1,2))
_H3cSSHUserConfigTable_Object=MibTable
h3cSSHUserConfigTable=_H3cSSHUserConfigTable_Object((1,3,6,1,4,1,2011,10,2,22,1,1,2,1))
if mibBuilder.loadTexts:h3cSSHUserConfigTable.setStatus(_A)
_H3cSSHUserConfigEntry_Object=MibTableRow
h3cSSHUserConfigEntry=_H3cSSHUserConfigEntry_Object((1,3,6,1,4,1,2011,10,2,22,1,1,2,1,1))
h3cSSHUserConfigEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:h3cSSHUserConfigEntry.setStatus(_A)
_H3cSSHUserName_Type=DisplayString
_H3cSSHUserName_Object=MibTableColumn
h3cSSHUserName=_H3cSSHUserName_Object((1,3,6,1,4,1,2011,10,2,22,1,1,2,1,1,1),_H3cSSHUserName_Type())
h3cSSHUserName.setMaxAccess(_P)
if mibBuilder.loadTexts:h3cSSHUserName.setStatus(_A)
class _H3cSSHUserServiceType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_H,1),('all',2),(_Q,3),('sftp',4),('scp',5),(_R,6)))
_H3cSSHUserServiceType_Type.__name__=_C
_H3cSSHUserServiceType_Object=MibTableColumn
h3cSSHUserServiceType=_H3cSSHUserServiceType_Object((1,3,6,1,4,1,2011,10,2,22,1,1,2,1,1,2),_H3cSSHUserServiceType_Type())
h3cSSHUserServiceType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSSHUserServiceType.setStatus(_A)
class _H3cSSHUserAuthType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_H,1),('password',2),('publicKey',3),('any',4),('publicKeyPassword',5),('keyboardInteractive',6)))
_H3cSSHUserAuthType_Type.__name__=_C
_H3cSSHUserAuthType_Object=MibTableColumn
h3cSSHUserAuthType=_H3cSSHUserAuthType_Object((1,3,6,1,4,1,2011,10,2,22,1,1,2,1,1,3),_H3cSSHUserAuthType_Type())
h3cSSHUserAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSSHUserAuthType.setStatus(_A)
class _H3cSSHUserPublicKeyName_Type(DisplayString):defaultValue=OctetString('')
_H3cSSHUserPublicKeyName_Type.__name__=_F
_H3cSSHUserPublicKeyName_Object=MibTableColumn
h3cSSHUserPublicKeyName=_H3cSSHUserPublicKeyName_Object((1,3,6,1,4,1,2011,10,2,22,1,1,2,1,1,4),_H3cSSHUserPublicKeyName_Type())
h3cSSHUserPublicKeyName.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSSHUserPublicKeyName.setStatus(_A)
class _H3cSSHUserWorkDirectory_Type(DisplayString):defaultValue=OctetString('')
_H3cSSHUserWorkDirectory_Type.__name__=_F
_H3cSSHUserWorkDirectory_Object=MibTableColumn
h3cSSHUserWorkDirectory=_H3cSSHUserWorkDirectory_Object((1,3,6,1,4,1,2011,10,2,22,1,1,2,1,1,5),_H3cSSHUserWorkDirectory_Type())
h3cSSHUserWorkDirectory.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSSHUserWorkDirectory.setStatus(_A)
_H3cSSHUserRowStatus_Type=RowStatus
_H3cSSHUserRowStatus_Object=MibTableColumn
h3cSSHUserRowStatus=_H3cSSHUserRowStatus_Object((1,3,6,1,4,1,2011,10,2,22,1,1,2,1,1,6),_H3cSSHUserRowStatus_Type())
h3cSSHUserRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSSHUserRowStatus.setStatus(_A)
class _H3cSSHUserPublicKeyName2_Type(DisplayString):defaultValue=OctetString('')
_H3cSSHUserPublicKeyName2_Type.__name__=_F
_H3cSSHUserPublicKeyName2_Object=MibTableColumn
h3cSSHUserPublicKeyName2=_H3cSSHUserPublicKeyName2_Object((1,3,6,1,4,1,2011,10,2,22,1,1,2,1,1,7),_H3cSSHUserPublicKeyName2_Type())
h3cSSHUserPublicKeyName2.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSSHUserPublicKeyName2.setStatus(_A)
class _H3cSSHUserPublicKeyName3_Type(DisplayString):defaultValue=OctetString('')
_H3cSSHUserPublicKeyName3_Type.__name__=_F
_H3cSSHUserPublicKeyName3_Object=MibTableColumn
h3cSSHUserPublicKeyName3=_H3cSSHUserPublicKeyName3_Object((1,3,6,1,4,1,2011,10,2,22,1,1,2,1,1,8),_H3cSSHUserPublicKeyName3_Type())
h3cSSHUserPublicKeyName3.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSSHUserPublicKeyName3.setStatus(_A)
class _H3cSSHUserPublicKeyName4_Type(DisplayString):defaultValue=OctetString('')
_H3cSSHUserPublicKeyName4_Type.__name__=_F
_H3cSSHUserPublicKeyName4_Object=MibTableColumn
h3cSSHUserPublicKeyName4=_H3cSSHUserPublicKeyName4_Object((1,3,6,1,4,1,2011,10,2,22,1,1,2,1,1,9),_H3cSSHUserPublicKeyName4_Type())
h3cSSHUserPublicKeyName4.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSSHUserPublicKeyName4.setStatus(_A)
class _H3cSSHUserPublicKeyName5_Type(DisplayString):defaultValue=OctetString('')
_H3cSSHUserPublicKeyName5_Type.__name__=_F
_H3cSSHUserPublicKeyName5_Object=MibTableColumn
h3cSSHUserPublicKeyName5=_H3cSSHUserPublicKeyName5_Object((1,3,6,1,4,1,2011,10,2,22,1,1,2,1,1,10),_H3cSSHUserPublicKeyName5_Type())
h3cSSHUserPublicKeyName5.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSSHUserPublicKeyName5.setStatus(_A)
class _H3cSSHUserPublicKeyName6_Type(DisplayString):defaultValue=OctetString('')
_H3cSSHUserPublicKeyName6_Type.__name__=_F
_H3cSSHUserPublicKeyName6_Object=MibTableColumn
h3cSSHUserPublicKeyName6=_H3cSSHUserPublicKeyName6_Object((1,3,6,1,4,1,2011,10,2,22,1,1,2,1,1,11),_H3cSSHUserPublicKeyName6_Type())
h3cSSHUserPublicKeyName6.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSSHUserPublicKeyName6.setStatus(_A)
_H3cSSHSessionInfoTable_Object=MibTable
h3cSSHSessionInfoTable=_H3cSSHSessionInfoTable_Object((1,3,6,1,4,1,2011,10,2,22,1,1,3))
if mibBuilder.loadTexts:h3cSSHSessionInfoTable.setStatus(_A)
_H3cSSHSessionInfoEntry_Object=MibTableRow
h3cSSHSessionInfoEntry=_H3cSSHSessionInfoEntry_Object((1,3,6,1,4,1,2011,10,2,22,1,1,3,1))
h3cSSHSessionInfoEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:h3cSSHSessionInfoEntry.setStatus(_A)
_H3cSSHSessionID_Type=Integer32
_H3cSSHSessionID_Object=MibTableColumn
h3cSSHSessionID=_H3cSSHSessionID_Object((1,3,6,1,4,1,2011,10,2,22,1,1,3,1,1),_H3cSSHSessionID_Type())
h3cSSHSessionID.setMaxAccess(_P)
if mibBuilder.loadTexts:h3cSSHSessionID.setStatus(_A)
_H3cSSHSessionUserName_Type=DisplayString
_H3cSSHSessionUserName_Object=MibTableColumn
h3cSSHSessionUserName=_H3cSSHSessionUserName_Object((1,3,6,1,4,1,2011,10,2,22,1,1,3,1,2),_H3cSSHSessionUserName_Type())
h3cSSHSessionUserName.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSSHSessionUserName.setStatus(_A)
_H3cSSHSessionUserIpAddrType_Type=InetAddressType
_H3cSSHSessionUserIpAddrType_Object=MibTableColumn
h3cSSHSessionUserIpAddrType=_H3cSSHSessionUserIpAddrType_Object((1,3,6,1,4,1,2011,10,2,22,1,1,3,1,3),_H3cSSHSessionUserIpAddrType_Type())
h3cSSHSessionUserIpAddrType.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSSHSessionUserIpAddrType.setStatus(_A)
_H3cSSHSessionUserIpAddr_Type=InetAddress
_H3cSSHSessionUserIpAddr_Object=MibTableColumn
h3cSSHSessionUserIpAddr=_H3cSSHSessionUserIpAddr_Object((1,3,6,1,4,1,2011,10,2,22,1,1,3,1,4),_H3cSSHSessionUserIpAddr_Type())
h3cSSHSessionUserIpAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSSHSessionUserIpAddr.setStatus(_A)
_H3cSSHSessionClientVersion_Type=DisplayString
_H3cSSHSessionClientVersion_Object=MibTableColumn
h3cSSHSessionClientVersion=_H3cSSHSessionClientVersion_Object((1,3,6,1,4,1,2011,10,2,22,1,1,3,1,5),_H3cSSHSessionClientVersion_Type())
h3cSSHSessionClientVersion.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSSHSessionClientVersion.setStatus(_A)
class _H3cSSHSessionServiceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),(_Q,2),('sftp',3),('scp',4),(_R,5)))
_H3cSSHSessionServiceType_Type.__name__=_C
_H3cSSHSessionServiceType_Object=MibTableColumn
h3cSSHSessionServiceType=_H3cSSHSessionServiceType_Object((1,3,6,1,4,1,2011,10,2,22,1,1,3,1,6),_H3cSSHSessionServiceType_Type())
h3cSSHSessionServiceType.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSSHSessionServiceType.setStatus(_A)
class _H3cSSHSessionEncry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_H,1),('aes128CBC',2),('desCBC',3),('des3CBC',4),('aes128CTR',5),('aes192CTR',6),('aes256CTR',7),('aes128GCM',8),('aes256GCM',9),('aes256CBC',10)))
_H3cSSHSessionEncry_Type.__name__=_C
_H3cSSHSessionEncry_Object=MibTableColumn
h3cSSHSessionEncry=_H3cSSHSessionEncry_Object((1,3,6,1,4,1,2011,10,2,22,1,1,3,1,7),_H3cSSHSessionEncry_Type())
h3cSSHSessionEncry.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSSHSessionEncry.setStatus(_A)
class _H3cSSHSessionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('init',1),('verExchange',2),('keysExchange',3),('authRequest',4),('serviceRequest',5),('established',6),('disconnect',7)))
_H3cSSHSessionState_Type.__name__=_C
_H3cSSHSessionState_Object=MibTableColumn
h3cSSHSessionState=_H3cSSHSessionState_Object((1,3,6,1,4,1,2011,10,2,22,1,1,3,1,8),_H3cSSHSessionState_Type())
h3cSSHSessionState.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSSHSessionState.setStatus(_A)
_H3cSSHServerObjForTrap_ObjectIdentity=ObjectIdentity
h3cSSHServerObjForTrap=_H3cSSHServerObjForTrap_ObjectIdentity((1,3,6,1,4,1,2011,10,2,22,1,2))
_H3cSSHAttemptUserName_Type=DisplayString
_H3cSSHAttemptUserName_Object=MibScalar
h3cSSHAttemptUserName=_H3cSSHAttemptUserName_Object((1,3,6,1,4,1,2011,10,2,22,1,2,1),_H3cSSHAttemptUserName_Type())
h3cSSHAttemptUserName.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cSSHAttemptUserName.setStatus(_A)
_H3cSSHAttemptIpAddrType_Type=InetAddressType
_H3cSSHAttemptIpAddrType_Object=MibScalar
h3cSSHAttemptIpAddrType=_H3cSSHAttemptIpAddrType_Object((1,3,6,1,4,1,2011,10,2,22,1,2,2),_H3cSSHAttemptIpAddrType_Type())
h3cSSHAttemptIpAddrType.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cSSHAttemptIpAddrType.setStatus(_A)
_H3cSSHAttemptIpAddr_Type=InetAddress
_H3cSSHAttemptIpAddr_Object=MibScalar
h3cSSHAttemptIpAddr=_H3cSSHAttemptIpAddr_Object((1,3,6,1,4,1,2011,10,2,22,1,2,3),_H3cSSHAttemptIpAddr_Type())
h3cSSHAttemptIpAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cSSHAttemptIpAddr.setStatus(_A)
class _H3cSSHUserAuthFailureReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('exceedRetries',1),('authTimeout',2),('otherReason',3)))
_H3cSSHUserAuthFailureReason_Type.__name__=_C
_H3cSSHUserAuthFailureReason_Object=MibScalar
h3cSSHUserAuthFailureReason=_H3cSSHUserAuthFailureReason_Object((1,3,6,1,4,1,2011,10,2,22,1,2,4),_H3cSSHUserAuthFailureReason_Type())
h3cSSHUserAuthFailureReason.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cSSHUserAuthFailureReason.setStatus(_A)
_H3cSSHServerNotifications_ObjectIdentity=ObjectIdentity
h3cSSHServerNotifications=_H3cSSHServerNotifications_ObjectIdentity((1,3,6,1,4,1,2011,10,2,22,1,3))
_H3cSSHServerNotificationsPrefix_ObjectIdentity=ObjectIdentity
h3cSSHServerNotificationsPrefix=_H3cSSHServerNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,22,1,3,0))
h3cSSHUserAuthFailure=NotificationType((1,3,6,1,4,1,2011,10,2,22,1,3,0,1))
h3cSSHUserAuthFailure.setObjects(*((_B,_T),(_B,_J),(_B,_K),(_B,_U)))
if mibBuilder.loadTexts:h3cSSHUserAuthFailure.setStatus(_A)
h3cSSHVersionNegotiationFailure=NotificationType((1,3,6,1,4,1,2011,10,2,22,1,3,0,2))
h3cSSHVersionNegotiationFailure.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:h3cSSHVersionNegotiationFailure.setStatus(_A)
h3cSSHUserLogin=NotificationType((1,3,6,1,4,1,2011,10,2,22,1,3,0,3))
h3cSSHUserLogin.setObjects(*((_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:h3cSSHUserLogin.setStatus(_A)
h3cSSHUserLogoff=NotificationType((1,3,6,1,4,1,2011,10,2,22,1,3,0,4))
h3cSSHUserLogoff.setObjects(*((_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:h3cSSHUserLogoff.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cSSH':h3cSSH,'h3cSSHServerMIB':h3cSSHServerMIB,'h3cSSHServerMIBObjects':h3cSSHServerMIBObjects,'h3cSSHServerGlobalConfig':h3cSSHServerGlobalConfig,'h3cSSHServerVersion':h3cSSHServerVersion,'h3cSSHServerCompatibleSSH1x':h3cSSHServerCompatibleSSH1x,'h3cSSHServerRekeyInterval':h3cSSHServerRekeyInterval,'h3cSSHServerAuthRetries':h3cSSHServerAuthRetries,'h3cSSHServerAuthTimeout':h3cSSHServerAuthTimeout,'h3cSFTPServerIdleTimeout':h3cSFTPServerIdleTimeout,'h3cSSHServerEnable':h3cSSHServerEnable,'h3cSFTPServerEnable':h3cSFTPServerEnable,'h3cSTelnetServerEnable':h3cSTelnetServerEnable,'h3cSCPServerEnable':h3cSCPServerEnable,'h3cSSHUserConfig':h3cSSHUserConfig,'h3cSSHUserConfigTable':h3cSSHUserConfigTable,'h3cSSHUserConfigEntry':h3cSSHUserConfigEntry,_O:h3cSSHUserName,'h3cSSHUserServiceType':h3cSSHUserServiceType,'h3cSSHUserAuthType':h3cSSHUserAuthType,'h3cSSHUserPublicKeyName':h3cSSHUserPublicKeyName,'h3cSSHUserWorkDirectory':h3cSSHUserWorkDirectory,'h3cSSHUserRowStatus':h3cSSHUserRowStatus,'h3cSSHUserPublicKeyName2':h3cSSHUserPublicKeyName2,'h3cSSHUserPublicKeyName3':h3cSSHUserPublicKeyName3,'h3cSSHUserPublicKeyName4':h3cSSHUserPublicKeyName4,'h3cSSHUserPublicKeyName5':h3cSSHUserPublicKeyName5,'h3cSSHUserPublicKeyName6':h3cSSHUserPublicKeyName6,'h3cSSHSessionInfoTable':h3cSSHSessionInfoTable,'h3cSSHSessionInfoEntry':h3cSSHSessionInfoEntry,_S:h3cSSHSessionID,_L:h3cSSHSessionUserName,_M:h3cSSHSessionUserIpAddrType,_N:h3cSSHSessionUserIpAddr,'h3cSSHSessionClientVersion':h3cSSHSessionClientVersion,'h3cSSHSessionServiceType':h3cSSHSessionServiceType,'h3cSSHSessionEncry':h3cSSHSessionEncry,'h3cSSHSessionState':h3cSSHSessionState,'h3cSSHServerObjForTrap':h3cSSHServerObjForTrap,_T:h3cSSHAttemptUserName,_J:h3cSSHAttemptIpAddrType,_K:h3cSSHAttemptIpAddr,_U:h3cSSHUserAuthFailureReason,'h3cSSHServerNotifications':h3cSSHServerNotifications,'h3cSSHServerNotificationsPrefix':h3cSSHServerNotificationsPrefix,'h3cSSHUserAuthFailure':h3cSSHUserAuthFailure,'h3cSSHVersionNegotiationFailure':h3cSSHVersionNegotiationFailure,'h3cSSHUserLogin':h3cSSHUserLogin,'h3cSSHUserLogoff':h3cSSHUserLogoff})