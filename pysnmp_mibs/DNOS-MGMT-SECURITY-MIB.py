_U='agentSSHServerKexIndex'
_T='agentSSHServerMacIndex'
_S='agentSSHServerEncryptionIndex'
_R='dsa-ecdsa'
_Q='rsa-ecdsa'
_P='rsa-dsa'
_O='read-create'
_N='not-accessible'
_M='DNOS-MGMT-SECURITY-MIB'
_L='undefined'
_K='delete'
_J='generate'
_I='noop'
_H='both'
_G='Unsigned32'
_F='read-only'
_E='disable'
_D='enable'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dnOS,=mibBuilder.importSymbols('DELL-REF-MIB','dnOS')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
fastPathMgmtSecurity=ModuleIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11))
if mibBuilder.loadTexts:fastPathMgmtSecurity.setRevisions(('2022-02-22 00:00','2021-11-22 00:00','2021-09-21 00:00','2019-07-25 00:00','2018-12-05 00:00','2018-03-01 00:00','2007-05-23 00:00','2003-11-21 00:00'))
_AgentSSLConfigGroup_ObjectIdentity=ObjectIdentity
agentSSLConfigGroup=_AgentSSLConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,1))
class _AgentSSLAdminMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentSSLAdminMode_Type.__name__=_B
_AgentSSLAdminMode_Object=MibScalar
agentSSLAdminMode=_AgentSSLAdminMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,1,1),_AgentSSLAdminMode_Type())
agentSSLAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSLAdminMode.setStatus(_A)
class _AgentSSLSecurePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(443,443),ValueRangeConstraint(1025,65535))
_AgentSSLSecurePort_Type.__name__=_B
_AgentSSLSecurePort_Object=MibScalar
agentSSLSecurePort=_AgentSSLSecurePort_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,1,2),_AgentSSLSecurePort_Type())
agentSSLSecurePort.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSLSecurePort.setStatus(_A)
class _AgentSSLProtocolLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ssl30',1),('tls10',2),(_H,3),('tls12',4)))
_AgentSSLProtocolLevel_Type.__name__=_B
_AgentSSLProtocolLevel_Object=MibScalar
agentSSLProtocolLevel=_AgentSSLProtocolLevel_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,1,3),_AgentSSLProtocolLevel_Type())
agentSSLProtocolLevel.setMaxAccess(_F)
if mibBuilder.loadTexts:agentSSLProtocolLevel.setStatus(_A)
class _AgentSSLMaxSessions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AgentSSLMaxSessions_Type.__name__=_B
_AgentSSLMaxSessions_Object=MibScalar
agentSSLMaxSessions=_AgentSSLMaxSessions_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,1,4),_AgentSSLMaxSessions_Type())
agentSSLMaxSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSLMaxSessions.setStatus(_A)
class _AgentSSLHardTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_AgentSSLHardTimeout_Type.__name__=_B
_AgentSSLHardTimeout_Object=MibScalar
agentSSLHardTimeout=_AgentSSLHardTimeout_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,1,5),_AgentSSLHardTimeout_Type())
agentSSLHardTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSLHardTimeout.setStatus(_A)
class _AgentSSLSoftTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_AgentSSLSoftTimeout_Type.__name__=_B
_AgentSSLSoftTimeout_Object=MibScalar
agentSSLSoftTimeout=_AgentSSLSoftTimeout_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,1,6),_AgentSSLSoftTimeout_Type())
agentSSLSoftTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSLSoftTimeout.setStatus(_A)
_AgentSSLCertificatePresent_Type=TruthValue
_AgentSSLCertificatePresent_Object=MibScalar
agentSSLCertificatePresent=_AgentSSLCertificatePresent_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,1,7),_AgentSSLCertificatePresent_Type())
agentSSLCertificatePresent.setMaxAccess(_F)
if mibBuilder.loadTexts:agentSSLCertificatePresent.setStatus(_A)
class _AgentSSLCertificateControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3)))
_AgentSSLCertificateControl_Type.__name__=_B
_AgentSSLCertificateControl_Object=MibScalar
agentSSLCertificateControl=_AgentSSLCertificateControl_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,1,8),_AgentSSLCertificateControl_Type())
agentSSLCertificateControl.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSLCertificateControl.setStatus(_A)
_AgentSSLCertificateGenerationStatus_Type=TruthValue
_AgentSSLCertificateGenerationStatus_Object=MibScalar
agentSSLCertificateGenerationStatus=_AgentSSLCertificateGenerationStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,1,9),_AgentSSLCertificateGenerationStatus_Type())
agentSSLCertificateGenerationStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:agentSSLCertificateGenerationStatus.setStatus(_A)
class _AgentSSLIpHttpSecureCiphersuite_Type(Bits):namedValues=NamedValues(*((_L,0),('aes128-cbc-sha',1),('aes256-cbc-sha',2),('dhe-aes128-cbc-sha',3),('dhe-aes-cbc-sha2',4),('dhe-aes-gcm-sha2',5),('ecdhe-rsa-aes-cbc-sha2',6),('ecdhe-rsa-aes-gcm-sha2',7),('rsa-aes-cbc-sha2',8),('rsa-aes-gcm-sha2',9)))
_AgentSSLIpHttpSecureCiphersuite_Type.__name__='Bits'
_AgentSSLIpHttpSecureCiphersuite_Object=MibScalar
agentSSLIpHttpSecureCiphersuite=_AgentSSLIpHttpSecureCiphersuite_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,1,10),_AgentSSLIpHttpSecureCiphersuite_Type())
agentSSLIpHttpSecureCiphersuite.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSLIpHttpSecureCiphersuite.setStatus(_A)
class _AgentSSLCryptoDhParam_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dh1024',1),('dh2048',2)))
_AgentSSLCryptoDhParam_Type.__name__=_B
_AgentSSLCryptoDhParam_Object=MibScalar
agentSSLCryptoDhParam=_AgentSSLCryptoDhParam_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,1,11),_AgentSSLCryptoDhParam_Type())
agentSSLCryptoDhParam.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSLCryptoDhParam.setStatus(_A)
_AgentSSHConfigGroup_ObjectIdentity=ObjectIdentity
agentSSHConfigGroup=_AgentSSHConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2))
class _AgentSSHAdminMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentSSHAdminMode_Type.__name__=_B
_AgentSSHAdminMode_Object=MibScalar
agentSSHAdminMode=_AgentSSHAdminMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,1),_AgentSSHAdminMode_Type())
agentSSHAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSHAdminMode.setStatus(_A)
class _AgentSSHProtocolLevel_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ssh10',1),('ssh20',2),(_H,3)))
_AgentSSHProtocolLevel_Type.__name__=_B
_AgentSSHProtocolLevel_Object=MibScalar
agentSSHProtocolLevel=_AgentSSHProtocolLevel_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,2),_AgentSSHProtocolLevel_Type())
agentSSHProtocolLevel.setMaxAccess(_F)
if mibBuilder.loadTexts:agentSSHProtocolLevel.setStatus(_A)
_AgentSSHSessionsCount_Type=Integer32
_AgentSSHSessionsCount_Object=MibScalar
agentSSHSessionsCount=_AgentSSHSessionsCount_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,3),_AgentSSHSessionsCount_Type())
agentSSHSessionsCount.setMaxAccess(_F)
if mibBuilder.loadTexts:agentSSHSessionsCount.setStatus(_A)
class _AgentSSHMaxSessionsCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_AgentSSHMaxSessionsCount_Type.__name__=_B
_AgentSSHMaxSessionsCount_Object=MibScalar
agentSSHMaxSessionsCount=_AgentSSHMaxSessionsCount_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,4),_AgentSSHMaxSessionsCount_Type())
agentSSHMaxSessionsCount.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSHMaxSessionsCount.setStatus(_A)
class _AgentSSHSessionTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3932159))
_AgentSSHSessionTimeout_Type.__name__=_B
_AgentSSHSessionTimeout_Object=MibScalar
agentSSHSessionTimeout=_AgentSSHSessionTimeout_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,5),_AgentSSHSessionTimeout_Type())
agentSSHSessionTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSHSessionTimeout.setStatus(_A)
class _AgentSSHKeysPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('dsa',1),('rsa',2),(_H,3),('none',4),('ecdsa',5),('all',6),(_P,7),(_Q,8),(_R,9)))
_AgentSSHKeysPresent_Type.__name__=_B
_AgentSSHKeysPresent_Object=MibScalar
agentSSHKeysPresent=_AgentSSHKeysPresent_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,6),_AgentSSHKeysPresent_Type())
agentSSHKeysPresent.setMaxAccess(_F)
if mibBuilder.loadTexts:agentSSHKeysPresent.setStatus(_A)
class _AgentSSHKeyGenerationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('dsa',1),('rsa',2),(_H,3),('none',4),('ecdsa',5),('all',6),(_P,7),(_Q,8),(_R,9)))
_AgentSSHKeyGenerationStatus_Type.__name__=_B
_AgentSSHKeyGenerationStatus_Object=MibScalar
agentSSHKeyGenerationStatus=_AgentSSHKeyGenerationStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,7),_AgentSSHKeyGenerationStatus_Type())
agentSSHKeyGenerationStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:agentSSHKeyGenerationStatus.setStatus(_A)
class _AgentSSHRSAKeyControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3)))
_AgentSSHRSAKeyControl_Type.__name__=_B
_AgentSSHRSAKeyControl_Object=MibScalar
agentSSHRSAKeyControl=_AgentSSHRSAKeyControl_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,8),_AgentSSHRSAKeyControl_Type())
agentSSHRSAKeyControl.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSHRSAKeyControl.setStatus(_A)
class _AgentSSHDSAKeyControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3)))
_AgentSSHDSAKeyControl_Type.__name__=_B
_AgentSSHDSAKeyControl_Object=MibScalar
agentSSHDSAKeyControl=_AgentSSHDSAKeyControl_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,9),_AgentSSHDSAKeyControl_Type())
agentSSHDSAKeyControl.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSHDSAKeyControl.setStatus(_A)
class _AgentSSHExecBannerState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentSSHExecBannerState_Type.__name__=_B
_AgentSSHExecBannerState_Object=MibScalar
agentSSHExecBannerState=_AgentSSHExecBannerState_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,10),_AgentSSHExecBannerState_Type())
agentSSHExecBannerState.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSHExecBannerState.setStatus(_A)
class _AgentSSHLoginBannerState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentSSHLoginBannerState_Type.__name__=_B
_AgentSSHLoginBannerState_Object=MibScalar
agentSSHLoginBannerState=_AgentSSHLoginBannerState_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,11),_AgentSSHLoginBannerState_Type())
agentSSHLoginBannerState.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSHLoginBannerState.setStatus(_A)
class _AgentSSHMotdBannerState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentSSHMotdBannerState_Type.__name__=_B
_AgentSSHMotdBannerState_Object=MibScalar
agentSSHMotdBannerState=_AgentSSHMotdBannerState_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,12),_AgentSSHMotdBannerState_Type())
agentSSHMotdBannerState.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSHMotdBannerState.setStatus(_A)
class _AgentSSHEcdsaKeyControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3)))
_AgentSSHEcdsaKeyControl_Type.__name__=_B
_AgentSSHEcdsaKeyControl_Object=MibScalar
agentSSHEcdsaKeyControl=_AgentSSHEcdsaKeyControl_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,13),_AgentSSHEcdsaKeyControl_Type())
agentSSHEcdsaKeyControl.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSHEcdsaKeyControl.setStatus(_A)
_AgentSSHEcdsaKeyLen_Type=Integer32
_AgentSSHEcdsaKeyLen_Object=MibScalar
agentSSHEcdsaKeyLen=_AgentSSHEcdsaKeyLen_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,14),_AgentSSHEcdsaKeyLen_Type())
agentSSHEcdsaKeyLen.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSHEcdsaKeyLen.setStatus(_A)
class _AgentSSHDsaKeyLen_Type(Integer32):defaultValue=1024
_AgentSSHDsaKeyLen_Type.__name__=_B
_AgentSSHDsaKeyLen_Object=MibScalar
agentSSHDsaKeyLen=_AgentSSHDsaKeyLen_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,15),_AgentSSHDsaKeyLen_Type())
agentSSHDsaKeyLen.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSHDsaKeyLen.setStatus(_A)
class _AgentSSHRsaKeyLen_Type(Integer32):defaultValue=1024
_AgentSSHRsaKeyLen_Type.__name__=_B
_AgentSSHRsaKeyLen_Object=MibScalar
agentSSHRsaKeyLen=_AgentSSHRsaKeyLen_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,16),_AgentSSHRsaKeyLen_Type())
agentSSHRsaKeyLen.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSHRsaKeyLen.setStatus(_A)
class _AgentSSHAuthenticationRetries_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_AgentSSHAuthenticationRetries_Type.__name__=_G
_AgentSSHAuthenticationRetries_Object=MibScalar
agentSSHAuthenticationRetries=_AgentSSHAuthenticationRetries_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,17),_AgentSSHAuthenticationRetries_Type())
agentSSHAuthenticationRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSHAuthenticationRetries.setStatus(_A)
_AgentSSHEncryptionAlgorithmsConfigGroup_ObjectIdentity=ObjectIdentity
agentSSHEncryptionAlgorithmsConfigGroup=_AgentSSHEncryptionAlgorithmsConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,18))
_AgentSSHServerEncryptionAlgorithmsTable_Object=MibTable
agentSSHServerEncryptionAlgorithmsTable=_AgentSSHServerEncryptionAlgorithmsTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,18,1))
if mibBuilder.loadTexts:agentSSHServerEncryptionAlgorithmsTable.setStatus(_A)
_AgentSSHServerEncryptionAlgorithmsEntry_Object=MibTableRow
agentSSHServerEncryptionAlgorithmsEntry=_AgentSSHServerEncryptionAlgorithmsEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,18,1,1))
agentSSHServerEncryptionAlgorithmsEntry.setIndexNames((0,_M,_S))
if mibBuilder.loadTexts:agentSSHServerEncryptionAlgorithmsEntry.setStatus(_A)
class _AgentSSHServerEncryptionIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AgentSSHServerEncryptionIndex_Type.__name__=_G
_AgentSSHServerEncryptionIndex_Object=MibTableColumn
agentSSHServerEncryptionIndex=_AgentSSHServerEncryptionIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,18,1,1,1),_AgentSSHServerEncryptionIndex_Type())
agentSSHServerEncryptionIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:agentSSHServerEncryptionIndex.setStatus(_A)
class _AgentSSHServerEncryptionAlgorithms_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_L,0),('aes128-ctr',1),('aes192-ctr',2),('aes256-ctr',3),('chacha20-poly1305',4)))
_AgentSSHServerEncryptionAlgorithms_Type.__name__=_B
_AgentSSHServerEncryptionAlgorithms_Object=MibTableColumn
agentSSHServerEncryptionAlgorithms=_AgentSSHServerEncryptionAlgorithms_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,18,1,1,2),_AgentSSHServerEncryptionAlgorithms_Type())
agentSSHServerEncryptionAlgorithms.setMaxAccess(_O)
if mibBuilder.loadTexts:agentSSHServerEncryptionAlgorithms.setStatus(_A)
class _AgentSSHServerEncryptionRefresh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentSSHServerEncryptionRefresh_Type.__name__=_B
_AgentSSHServerEncryptionRefresh_Object=MibScalar
agentSSHServerEncryptionRefresh=_AgentSSHServerEncryptionRefresh_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,18,2),_AgentSSHServerEncryptionRefresh_Type())
agentSSHServerEncryptionRefresh.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSHServerEncryptionRefresh.setStatus(_A)
_AgentSSHMacAlgorithmsConfigGroup_ObjectIdentity=ObjectIdentity
agentSSHMacAlgorithmsConfigGroup=_AgentSSHMacAlgorithmsConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,19))
_AgentSSHServerMacAlgorithmsTable_Object=MibTable
agentSSHServerMacAlgorithmsTable=_AgentSSHServerMacAlgorithmsTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,19,1))
if mibBuilder.loadTexts:agentSSHServerMacAlgorithmsTable.setStatus(_A)
_AgentSSHServerMacAlgorithmsEntry_Object=MibTableRow
agentSSHServerMacAlgorithmsEntry=_AgentSSHServerMacAlgorithmsEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,19,1,1))
agentSSHServerMacAlgorithmsEntry.setIndexNames((0,_M,_T))
if mibBuilder.loadTexts:agentSSHServerMacAlgorithmsEntry.setStatus(_A)
class _AgentSSHServerMacIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_AgentSSHServerMacIndex_Type.__name__=_G
_AgentSSHServerMacIndex_Object=MibTableColumn
agentSSHServerMacIndex=_AgentSSHServerMacIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,19,1,1,1),_AgentSSHServerMacIndex_Type())
agentSSHServerMacIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:agentSSHServerMacIndex.setStatus(_A)
class _AgentSSHServerMacAlgorithms_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_L,0),('hmac-sha1',1),('hmac-sha1-etm',2),('hmac-md5-etm',3),('hmac-sha2-256',4),('hmac-sha2-512',5),('hmac-sha1-96-etm',6),('hmac-md5-96-etm',7),('hmac-md5',8),('hmac-sha2-256-etm',9),('hmac-sha2-512-etm',10)))
_AgentSSHServerMacAlgorithms_Type.__name__=_B
_AgentSSHServerMacAlgorithms_Object=MibTableColumn
agentSSHServerMacAlgorithms=_AgentSSHServerMacAlgorithms_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,19,1,1,2),_AgentSSHServerMacAlgorithms_Type())
agentSSHServerMacAlgorithms.setMaxAccess(_O)
if mibBuilder.loadTexts:agentSSHServerMacAlgorithms.setStatus(_A)
class _AgentSSHServerMacRefresh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentSSHServerMacRefresh_Type.__name__=_B
_AgentSSHServerMacRefresh_Object=MibScalar
agentSSHServerMacRefresh=_AgentSSHServerMacRefresh_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,19,2),_AgentSSHServerMacRefresh_Type())
agentSSHServerMacRefresh.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSHServerMacRefresh.setStatus(_A)
_AgentSSHKexAlgorithmsConfigGroup_ObjectIdentity=ObjectIdentity
agentSSHKexAlgorithmsConfigGroup=_AgentSSHKexAlgorithmsConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,20))
_AgentSSHServerKexAlgorithmsTable_Object=MibTable
agentSSHServerKexAlgorithmsTable=_AgentSSHServerKexAlgorithmsTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,20,1))
if mibBuilder.loadTexts:agentSSHServerKexAlgorithmsTable.setStatus(_A)
_AgentSSHServerKexAlgorithmsEntry_Object=MibTableRow
agentSSHServerKexAlgorithmsEntry=_AgentSSHServerKexAlgorithmsEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,20,1,1))
agentSSHServerKexAlgorithmsEntry.setIndexNames((0,_M,_U))
if mibBuilder.loadTexts:agentSSHServerKexAlgorithmsEntry.setStatus(_A)
class _AgentSSHServerKexIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_AgentSSHServerKexIndex_Type.__name__=_G
_AgentSSHServerKexIndex_Object=MibTableColumn
agentSSHServerKexIndex=_AgentSSHServerKexIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,20,1,1,1),_AgentSSHServerKexIndex_Type())
agentSSHServerKexIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:agentSSHServerKexIndex.setStatus(_A)
class _AgentSSHServerKexAlgorithms_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_L,0),('curve25519-sha256',1),('curve25519-sha256-libssh',2),('ecdh-sha2-nistp256',3),('ecdh-sha2-nistp384',4),('ecdh-sha2-nistp521',5),('diffie-hellman-group-exchange-sha256',6),('diffie-hellman-group16-sha512',7),('diffie-hellman-group18-sha512',8),('diffie-hellman-group14-sha256',9),('diffie-hellman-group14-sha1',10)))
_AgentSSHServerKexAlgorithms_Type.__name__=_B
_AgentSSHServerKexAlgorithms_Object=MibTableColumn
agentSSHServerKexAlgorithms=_AgentSSHServerKexAlgorithms_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,20,1,1,2),_AgentSSHServerKexAlgorithms_Type())
agentSSHServerKexAlgorithms.setMaxAccess(_O)
if mibBuilder.loadTexts:agentSSHServerKexAlgorithms.setStatus(_A)
class _AgentSSHServerKexRefresh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentSSHServerKexRefresh_Type.__name__=_B
_AgentSSHServerKexRefresh_Object=MibScalar
agentSSHServerKexRefresh=_AgentSSHServerKexRefresh_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,2,20,2),_AgentSSHServerKexRefresh_Type())
agentSSHServerKexRefresh.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSHServerKexRefresh.setStatus(_A)
_AgentOutboundSSHGroup_ObjectIdentity=ObjectIdentity
agentOutboundSSHGroup=_AgentOutboundSSHGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,3))
class _AgentOutboundSSHAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentOutboundSSHAdminMode_Type.__name__=_B
_AgentOutboundSSHAdminMode_Object=MibScalar
agentOutboundSSHAdminMode=_AgentOutboundSSHAdminMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,3,1),_AgentOutboundSSHAdminMode_Type())
agentOutboundSSHAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOutboundSSHAdminMode.setStatus(_A)
class _AgentOutboundSSHMaxSessions_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_AgentOutboundSSHMaxSessions_Type.__name__=_B
_AgentOutboundSSHMaxSessions_Object=MibScalar
agentOutboundSSHMaxSessions=_AgentOutboundSSHMaxSessions_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,3,2),_AgentOutboundSSHMaxSessions_Type())
agentOutboundSSHMaxSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOutboundSSHMaxSessions.setStatus(_A)
_AgentOutboundSSHActiveSessions_Type=Integer32
_AgentOutboundSSHActiveSessions_Object=MibScalar
agentOutboundSSHActiveSessions=_AgentOutboundSSHActiveSessions_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,3,3),_AgentOutboundSSHActiveSessions_Type())
agentOutboundSSHActiveSessions.setMaxAccess(_F)
if mibBuilder.loadTexts:agentOutboundSSHActiveSessions.setStatus(_A)
class _AgentOutboundSSHTimeout_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,160))
_AgentOutboundSSHTimeout_Type.__name__=_B
_AgentOutboundSSHTimeout_Object=MibScalar
agentOutboundSSHTimeout=_AgentOutboundSSHTimeout_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,11,3,4),_AgentOutboundSSHTimeout_Type())
agentOutboundSSHTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOutboundSSHTimeout.setStatus(_A)
mibBuilder.exportSymbols(_M,**{'fastPathMgmtSecurity':fastPathMgmtSecurity,'agentSSLConfigGroup':agentSSLConfigGroup,'agentSSLAdminMode':agentSSLAdminMode,'agentSSLSecurePort':agentSSLSecurePort,'agentSSLProtocolLevel':agentSSLProtocolLevel,'agentSSLMaxSessions':agentSSLMaxSessions,'agentSSLHardTimeout':agentSSLHardTimeout,'agentSSLSoftTimeout':agentSSLSoftTimeout,'agentSSLCertificatePresent':agentSSLCertificatePresent,'agentSSLCertificateControl':agentSSLCertificateControl,'agentSSLCertificateGenerationStatus':agentSSLCertificateGenerationStatus,'agentSSLIpHttpSecureCiphersuite':agentSSLIpHttpSecureCiphersuite,'agentSSLCryptoDhParam':agentSSLCryptoDhParam,'agentSSHConfigGroup':agentSSHConfigGroup,'agentSSHAdminMode':agentSSHAdminMode,'agentSSHProtocolLevel':agentSSHProtocolLevel,'agentSSHSessionsCount':agentSSHSessionsCount,'agentSSHMaxSessionsCount':agentSSHMaxSessionsCount,'agentSSHSessionTimeout':agentSSHSessionTimeout,'agentSSHKeysPresent':agentSSHKeysPresent,'agentSSHKeyGenerationStatus':agentSSHKeyGenerationStatus,'agentSSHRSAKeyControl':agentSSHRSAKeyControl,'agentSSHDSAKeyControl':agentSSHDSAKeyControl,'agentSSHExecBannerState':agentSSHExecBannerState,'agentSSHLoginBannerState':agentSSHLoginBannerState,'agentSSHMotdBannerState':agentSSHMotdBannerState,'agentSSHEcdsaKeyControl':agentSSHEcdsaKeyControl,'agentSSHEcdsaKeyLen':agentSSHEcdsaKeyLen,'agentSSHDsaKeyLen':agentSSHDsaKeyLen,'agentSSHRsaKeyLen':agentSSHRsaKeyLen,'agentSSHAuthenticationRetries':agentSSHAuthenticationRetries,'agentSSHEncryptionAlgorithmsConfigGroup':agentSSHEncryptionAlgorithmsConfigGroup,'agentSSHServerEncryptionAlgorithmsTable':agentSSHServerEncryptionAlgorithmsTable,'agentSSHServerEncryptionAlgorithmsEntry':agentSSHServerEncryptionAlgorithmsEntry,_S:agentSSHServerEncryptionIndex,'agentSSHServerEncryptionAlgorithms':agentSSHServerEncryptionAlgorithms,'agentSSHServerEncryptionRefresh':agentSSHServerEncryptionRefresh,'agentSSHMacAlgorithmsConfigGroup':agentSSHMacAlgorithmsConfigGroup,'agentSSHServerMacAlgorithmsTable':agentSSHServerMacAlgorithmsTable,'agentSSHServerMacAlgorithmsEntry':agentSSHServerMacAlgorithmsEntry,_T:agentSSHServerMacIndex,'agentSSHServerMacAlgorithms':agentSSHServerMacAlgorithms,'agentSSHServerMacRefresh':agentSSHServerMacRefresh,'agentSSHKexAlgorithmsConfigGroup':agentSSHKexAlgorithmsConfigGroup,'agentSSHServerKexAlgorithmsTable':agentSSHServerKexAlgorithmsTable,'agentSSHServerKexAlgorithmsEntry':agentSSHServerKexAlgorithmsEntry,_U:agentSSHServerKexIndex,'agentSSHServerKexAlgorithms':agentSSHServerKexAlgorithms,'agentSSHServerKexRefresh':agentSSHServerKexRefresh,'agentOutboundSSHGroup':agentOutboundSSHGroup,'agentOutboundSSHAdminMode':agentOutboundSSHAdminMode,'agentOutboundSSHMaxSessions':agentOutboundSSHMaxSessions,'agentOutboundSSHActiveSessions':agentOutboundSSHActiveSessions,'agentOutboundSSHTimeout':agentOutboundSSHTimeout})