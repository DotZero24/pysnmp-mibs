_T='hpnicfSSHUserAuthFailureReason'
_S='hpnicfSSHAttemptUserName'
_R='hpnicfSSHSessionID'
_Q='stelnet'
_P='not-accessible'
_O='hpnicfSSHUserName'
_N='hpnicfSSHSessionUserIpAddr'
_M='hpnicfSSHSessionUserIpAddrType'
_L='hpnicfSSHSessionUserName'
_K='hpnicfSSHAttemptIpAddr'
_J='hpnicfSSHAttemptIpAddrType'
_I='DisplayString'
_H='accessible-for-notify'
_G='invalid'
_F='read-create'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='HPN-ICF-SSH-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','RowStatus','TextualConvention')
hpnicfSSH=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,22))
if mibBuilder.loadTexts:hpnicfSSH.setRevisions(('2014-02-20 00:00','2014-01-17 00:00','2013-12-21 00:00','2007-11-19 00:00'))
_HpnicfSSHServerMIB_ObjectIdentity=ObjectIdentity
hpnicfSSHServerMIB=_HpnicfSSHServerMIB_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,22,1))
_HpnicfSSHServerMIBObjects_ObjectIdentity=ObjectIdentity
hpnicfSSHServerMIBObjects=_HpnicfSSHServerMIBObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1))
_HpnicfSSHServerGlobalConfig_ObjectIdentity=ObjectIdentity
hpnicfSSHServerGlobalConfig=_HpnicfSSHServerGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,1))
_HpnicfSSHServerVersion_Type=DisplayString
_HpnicfSSHServerVersion_Object=MibScalar
hpnicfSSHServerVersion=_HpnicfSSHServerVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,1,1),_HpnicfSSHServerVersion_Type())
hpnicfSSHServerVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfSSHServerVersion.setStatus(_A)
class _HpnicfSSHServerCompatibleSSH1x_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enableCompatibleSSH1x',1),('disableCompatibleSSH1x',2)))
_HpnicfSSHServerCompatibleSSH1x_Type.__name__=_C
_HpnicfSSHServerCompatibleSSH1x_Object=MibScalar
hpnicfSSHServerCompatibleSSH1x=_HpnicfSSHServerCompatibleSSH1x_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,1,2),_HpnicfSSHServerCompatibleSSH1x_Type())
hpnicfSSHServerCompatibleSSH1x.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSSHServerCompatibleSSH1x.setStatus(_A)
_HpnicfSSHServerRekeyInterval_Type=Integer32
_HpnicfSSHServerRekeyInterval_Object=MibScalar
hpnicfSSHServerRekeyInterval=_HpnicfSSHServerRekeyInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,1,3),_HpnicfSSHServerRekeyInterval_Type())
hpnicfSSHServerRekeyInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSSHServerRekeyInterval.setStatus(_A)
_HpnicfSSHServerAuthRetries_Type=Integer32
_HpnicfSSHServerAuthRetries_Object=MibScalar
hpnicfSSHServerAuthRetries=_HpnicfSSHServerAuthRetries_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,1,4),_HpnicfSSHServerAuthRetries_Type())
hpnicfSSHServerAuthRetries.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSSHServerAuthRetries.setStatus(_A)
_HpnicfSSHServerAuthTimeout_Type=Integer32
_HpnicfSSHServerAuthTimeout_Object=MibScalar
hpnicfSSHServerAuthTimeout=_HpnicfSSHServerAuthTimeout_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,1,5),_HpnicfSSHServerAuthTimeout_Type())
hpnicfSSHServerAuthTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSSHServerAuthTimeout.setStatus(_A)
_HpnicfSFTPServerIdleTimeout_Type=Integer32
_HpnicfSFTPServerIdleTimeout_Object=MibScalar
hpnicfSFTPServerIdleTimeout=_HpnicfSFTPServerIdleTimeout_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,1,6),_HpnicfSFTPServerIdleTimeout_Type())
hpnicfSFTPServerIdleTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSFTPServerIdleTimeout.setStatus(_A)
class _HpnicfSSHServerEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enableSSHServer',1),('disableSSHServer',2)))
_HpnicfSSHServerEnable_Type.__name__=_C
_HpnicfSSHServerEnable_Object=MibScalar
hpnicfSSHServerEnable=_HpnicfSSHServerEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,1,7),_HpnicfSSHServerEnable_Type())
hpnicfSSHServerEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSSHServerEnable.setStatus(_A)
class _HpnicfSFTPServerEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enableSFTPService',1),('disableSFTPService',2)))
_HpnicfSFTPServerEnable_Type.__name__=_C
_HpnicfSFTPServerEnable_Object=MibScalar
hpnicfSFTPServerEnable=_HpnicfSFTPServerEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,1,8),_HpnicfSFTPServerEnable_Type())
hpnicfSFTPServerEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSFTPServerEnable.setStatus(_A)
class _HpnicfSTelnetServerEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enableSTelnetServer',1),('disableSTelnetServer',2)))
_HpnicfSTelnetServerEnable_Type.__name__=_C
_HpnicfSTelnetServerEnable_Object=MibScalar
hpnicfSTelnetServerEnable=_HpnicfSTelnetServerEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,1,9),_HpnicfSTelnetServerEnable_Type())
hpnicfSTelnetServerEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSTelnetServerEnable.setStatus(_A)
class _HpnicfSCPServerEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enableSCPService',1),('disableSCPService',2)))
_HpnicfSCPServerEnable_Type.__name__=_C
_HpnicfSCPServerEnable_Object=MibScalar
hpnicfSCPServerEnable=_HpnicfSCPServerEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,1,10),_HpnicfSCPServerEnable_Type())
hpnicfSCPServerEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSCPServerEnable.setStatus(_A)
_HpnicfSSHUserConfig_ObjectIdentity=ObjectIdentity
hpnicfSSHUserConfig=_HpnicfSSHUserConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,2))
_HpnicfSSHUserConfigTable_Object=MibTable
hpnicfSSHUserConfigTable=_HpnicfSSHUserConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,2,1))
if mibBuilder.loadTexts:hpnicfSSHUserConfigTable.setStatus(_A)
_HpnicfSSHUserConfigEntry_Object=MibTableRow
hpnicfSSHUserConfigEntry=_HpnicfSSHUserConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,2,1,1))
hpnicfSSHUserConfigEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:hpnicfSSHUserConfigEntry.setStatus(_A)
_HpnicfSSHUserName_Type=DisplayString
_HpnicfSSHUserName_Object=MibTableColumn
hpnicfSSHUserName=_HpnicfSSHUserName_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,2,1,1,1),_HpnicfSSHUserName_Type())
hpnicfSSHUserName.setMaxAccess(_P)
if mibBuilder.loadTexts:hpnicfSSHUserName.setStatus(_A)
class _HpnicfSSHUserServiceType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),('all',2),(_Q,3),('sftp',4),('scp',5)))
_HpnicfSSHUserServiceType_Type.__name__=_C
_HpnicfSSHUserServiceType_Object=MibTableColumn
hpnicfSSHUserServiceType=_HpnicfSSHUserServiceType_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,2,1,1,2),_HpnicfSSHUserServiceType_Type())
hpnicfSSHUserServiceType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSSHUserServiceType.setStatus(_A)
class _HpnicfSSHUserAuthType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),('password',2),('publicKey',3),('any',4),('publicKeyPassword',5)))
_HpnicfSSHUserAuthType_Type.__name__=_C
_HpnicfSSHUserAuthType_Object=MibTableColumn
hpnicfSSHUserAuthType=_HpnicfSSHUserAuthType_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,2,1,1,3),_HpnicfSSHUserAuthType_Type())
hpnicfSSHUserAuthType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSSHUserAuthType.setStatus(_A)
class _HpnicfSSHUserPublicKeyName_Type(DisplayString):defaultValue=OctetString('')
_HpnicfSSHUserPublicKeyName_Type.__name__=_I
_HpnicfSSHUserPublicKeyName_Object=MibTableColumn
hpnicfSSHUserPublicKeyName=_HpnicfSSHUserPublicKeyName_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,2,1,1,4),_HpnicfSSHUserPublicKeyName_Type())
hpnicfSSHUserPublicKeyName.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSSHUserPublicKeyName.setStatus(_A)
class _HpnicfSSHUserWorkDirectory_Type(DisplayString):defaultValue=OctetString('')
_HpnicfSSHUserWorkDirectory_Type.__name__=_I
_HpnicfSSHUserWorkDirectory_Object=MibTableColumn
hpnicfSSHUserWorkDirectory=_HpnicfSSHUserWorkDirectory_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,2,1,1,5),_HpnicfSSHUserWorkDirectory_Type())
hpnicfSSHUserWorkDirectory.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSSHUserWorkDirectory.setStatus(_A)
_HpnicfSSHUserRowStatus_Type=RowStatus
_HpnicfSSHUserRowStatus_Object=MibTableColumn
hpnicfSSHUserRowStatus=_HpnicfSSHUserRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,2,1,1,6),_HpnicfSSHUserRowStatus_Type())
hpnicfSSHUserRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSSHUserRowStatus.setStatus(_A)
_HpnicfSSHSessionInfoTable_Object=MibTable
hpnicfSSHSessionInfoTable=_HpnicfSSHSessionInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,3))
if mibBuilder.loadTexts:hpnicfSSHSessionInfoTable.setStatus(_A)
_HpnicfSSHSessionInfoEntry_Object=MibTableRow
hpnicfSSHSessionInfoEntry=_HpnicfSSHSessionInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,3,1))
hpnicfSSHSessionInfoEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:hpnicfSSHSessionInfoEntry.setStatus(_A)
_HpnicfSSHSessionID_Type=Integer32
_HpnicfSSHSessionID_Object=MibTableColumn
hpnicfSSHSessionID=_HpnicfSSHSessionID_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,3,1,1),_HpnicfSSHSessionID_Type())
hpnicfSSHSessionID.setMaxAccess(_P)
if mibBuilder.loadTexts:hpnicfSSHSessionID.setStatus(_A)
_HpnicfSSHSessionUserName_Type=DisplayString
_HpnicfSSHSessionUserName_Object=MibTableColumn
hpnicfSSHSessionUserName=_HpnicfSSHSessionUserName_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,3,1,2),_HpnicfSSHSessionUserName_Type())
hpnicfSSHSessionUserName.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfSSHSessionUserName.setStatus(_A)
_HpnicfSSHSessionUserIpAddrType_Type=InetAddressType
_HpnicfSSHSessionUserIpAddrType_Object=MibTableColumn
hpnicfSSHSessionUserIpAddrType=_HpnicfSSHSessionUserIpAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,3,1,3),_HpnicfSSHSessionUserIpAddrType_Type())
hpnicfSSHSessionUserIpAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfSSHSessionUserIpAddrType.setStatus(_A)
_HpnicfSSHSessionUserIpAddr_Type=InetAddress
_HpnicfSSHSessionUserIpAddr_Object=MibTableColumn
hpnicfSSHSessionUserIpAddr=_HpnicfSSHSessionUserIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,3,1,4),_HpnicfSSHSessionUserIpAddr_Type())
hpnicfSSHSessionUserIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfSSHSessionUserIpAddr.setStatus(_A)
_HpnicfSSHSessionClientVersion_Type=DisplayString
_HpnicfSSHSessionClientVersion_Object=MibTableColumn
hpnicfSSHSessionClientVersion=_HpnicfSSHSessionClientVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,3,1,5),_HpnicfSSHSessionClientVersion_Type())
hpnicfSSHSessionClientVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfSSHSessionClientVersion.setStatus(_A)
class _HpnicfSSHSessionServiceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_Q,2),('sftp',3),('scp',4)))
_HpnicfSSHSessionServiceType_Type.__name__=_C
_HpnicfSSHSessionServiceType_Object=MibTableColumn
hpnicfSSHSessionServiceType=_HpnicfSSHSessionServiceType_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,3,1,6),_HpnicfSSHSessionServiceType_Type())
hpnicfSSHSessionServiceType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfSSHSessionServiceType.setStatus(_A)
class _HpnicfSSHSessionEncry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('aes128CBC',2),('desCBC',3),('des3CBC',4)))
_HpnicfSSHSessionEncry_Type.__name__=_C
_HpnicfSSHSessionEncry_Object=MibTableColumn
hpnicfSSHSessionEncry=_HpnicfSSHSessionEncry_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,3,1,7),_HpnicfSSHSessionEncry_Type())
hpnicfSSHSessionEncry.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfSSHSessionEncry.setStatus(_A)
class _HpnicfSSHSessionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('init',1),('verExchange',2),('keysExchange',3),('authRequest',4),('serviceRequest',5),('established',6),('disconnect',7)))
_HpnicfSSHSessionState_Type.__name__=_C
_HpnicfSSHSessionState_Object=MibTableColumn
hpnicfSSHSessionState=_HpnicfSSHSessionState_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,1,3,1,8),_HpnicfSSHSessionState_Type())
hpnicfSSHSessionState.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfSSHSessionState.setStatus(_A)
_HpnicfSSHServerObjForTrap_ObjectIdentity=ObjectIdentity
hpnicfSSHServerObjForTrap=_HpnicfSSHServerObjForTrap_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,22,1,2))
_HpnicfSSHAttemptUserName_Type=DisplayString
_HpnicfSSHAttemptUserName_Object=MibScalar
hpnicfSSHAttemptUserName=_HpnicfSSHAttemptUserName_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,2,1),_HpnicfSSHAttemptUserName_Type())
hpnicfSSHAttemptUserName.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSSHAttemptUserName.setStatus(_A)
_HpnicfSSHAttemptIpAddrType_Type=InetAddressType
_HpnicfSSHAttemptIpAddrType_Object=MibScalar
hpnicfSSHAttemptIpAddrType=_HpnicfSSHAttemptIpAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,2,2),_HpnicfSSHAttemptIpAddrType_Type())
hpnicfSSHAttemptIpAddrType.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSSHAttemptIpAddrType.setStatus(_A)
_HpnicfSSHAttemptIpAddr_Type=InetAddress
_HpnicfSSHAttemptIpAddr_Object=MibScalar
hpnicfSSHAttemptIpAddr=_HpnicfSSHAttemptIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,2,3),_HpnicfSSHAttemptIpAddr_Type())
hpnicfSSHAttemptIpAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSSHAttemptIpAddr.setStatus(_A)
class _HpnicfSSHUserAuthFailureReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('exceedRetries',1),('authTimeout',2),('otherReason',3)))
_HpnicfSSHUserAuthFailureReason_Type.__name__=_C
_HpnicfSSHUserAuthFailureReason_Object=MibScalar
hpnicfSSHUserAuthFailureReason=_HpnicfSSHUserAuthFailureReason_Object((1,3,6,1,4,1,11,2,14,11,15,2,22,1,2,4),_HpnicfSSHUserAuthFailureReason_Type())
hpnicfSSHUserAuthFailureReason.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSSHUserAuthFailureReason.setStatus(_A)
_HpnicfSSHServerNotifications_ObjectIdentity=ObjectIdentity
hpnicfSSHServerNotifications=_HpnicfSSHServerNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,22,1,3))
_HpnicfSSHServerNotificationsPrefix_ObjectIdentity=ObjectIdentity
hpnicfSSHServerNotificationsPrefix=_HpnicfSSHServerNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,22,1,3,0))
hpnicfSSHUserAuthFailure=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,22,1,3,0,1))
hpnicfSSHUserAuthFailure.setObjects(*((_B,_S),(_B,_J),(_B,_K),(_B,_T)))
if mibBuilder.loadTexts:hpnicfSSHUserAuthFailure.setStatus(_A)
hpnicfSSHVersionNegotiationFailure=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,22,1,3,0,2))
hpnicfSSHVersionNegotiationFailure.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:hpnicfSSHVersionNegotiationFailure.setStatus(_A)
hpnicfSSHUserLogin=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,22,1,3,0,3))
hpnicfSSHUserLogin.setObjects(*((_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:hpnicfSSHUserLogin.setStatus(_A)
hpnicfSSHUserLogoff=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,22,1,3,0,4))
hpnicfSSHUserLogoff.setObjects(*((_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:hpnicfSSHUserLogoff.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfSSH':hpnicfSSH,'hpnicfSSHServerMIB':hpnicfSSHServerMIB,'hpnicfSSHServerMIBObjects':hpnicfSSHServerMIBObjects,'hpnicfSSHServerGlobalConfig':hpnicfSSHServerGlobalConfig,'hpnicfSSHServerVersion':hpnicfSSHServerVersion,'hpnicfSSHServerCompatibleSSH1x':hpnicfSSHServerCompatibleSSH1x,'hpnicfSSHServerRekeyInterval':hpnicfSSHServerRekeyInterval,'hpnicfSSHServerAuthRetries':hpnicfSSHServerAuthRetries,'hpnicfSSHServerAuthTimeout':hpnicfSSHServerAuthTimeout,'hpnicfSFTPServerIdleTimeout':hpnicfSFTPServerIdleTimeout,'hpnicfSSHServerEnable':hpnicfSSHServerEnable,'hpnicfSFTPServerEnable':hpnicfSFTPServerEnable,'hpnicfSTelnetServerEnable':hpnicfSTelnetServerEnable,'hpnicfSCPServerEnable':hpnicfSCPServerEnable,'hpnicfSSHUserConfig':hpnicfSSHUserConfig,'hpnicfSSHUserConfigTable':hpnicfSSHUserConfigTable,'hpnicfSSHUserConfigEntry':hpnicfSSHUserConfigEntry,_O:hpnicfSSHUserName,'hpnicfSSHUserServiceType':hpnicfSSHUserServiceType,'hpnicfSSHUserAuthType':hpnicfSSHUserAuthType,'hpnicfSSHUserPublicKeyName':hpnicfSSHUserPublicKeyName,'hpnicfSSHUserWorkDirectory':hpnicfSSHUserWorkDirectory,'hpnicfSSHUserRowStatus':hpnicfSSHUserRowStatus,'hpnicfSSHSessionInfoTable':hpnicfSSHSessionInfoTable,'hpnicfSSHSessionInfoEntry':hpnicfSSHSessionInfoEntry,_R:hpnicfSSHSessionID,_L:hpnicfSSHSessionUserName,_M:hpnicfSSHSessionUserIpAddrType,_N:hpnicfSSHSessionUserIpAddr,'hpnicfSSHSessionClientVersion':hpnicfSSHSessionClientVersion,'hpnicfSSHSessionServiceType':hpnicfSSHSessionServiceType,'hpnicfSSHSessionEncry':hpnicfSSHSessionEncry,'hpnicfSSHSessionState':hpnicfSSHSessionState,'hpnicfSSHServerObjForTrap':hpnicfSSHServerObjForTrap,_S:hpnicfSSHAttemptUserName,_J:hpnicfSSHAttemptIpAddrType,_K:hpnicfSSHAttemptIpAddr,_T:hpnicfSSHUserAuthFailureReason,'hpnicfSSHServerNotifications':hpnicfSSHServerNotifications,'hpnicfSSHServerNotificationsPrefix':hpnicfSSHServerNotificationsPrefix,'hpnicfSSHUserAuthFailure':hpnicfSSHUserAuthFailure,'hpnicfSSHVersionNegotiationFailure':hpnicfSSHVersionNegotiationFailure,'hpnicfSSHUserLogin':hpnicfSSHUserLogin,'hpnicfSSHUserLogoff':hpnicfSSHUserLogoff})