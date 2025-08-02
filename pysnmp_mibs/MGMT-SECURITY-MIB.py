_J='disable'
_I='enable'
_H='delete'
_G='generate'
_F='noop'
_E='both'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
quanta,switch=mibBuilder.importSymbols('QUANTA-SWITCH-MIB','quanta','switch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
mgmtSecurity=ModuleIdentity((1,3,6,1,4,1,7244,2,11))
_AgentSSLConfigGroup_ObjectIdentity=ObjectIdentity
agentSSLConfigGroup=_AgentSSLConfigGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,11,1))
class _AgentSSLAdminMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_AgentSSLAdminMode_Type.__name__=_B
_AgentSSLAdminMode_Object=MibScalar
agentSSLAdminMode=_AgentSSLAdminMode_Object((1,3,6,1,4,1,7244,2,11,1,1),_AgentSSLAdminMode_Type())
agentSSLAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSLAdminMode.setStatus(_A)
class _AgentSSLSecurePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentSSLSecurePort_Type.__name__=_B
_AgentSSLSecurePort_Object=MibScalar
agentSSLSecurePort=_AgentSSLSecurePort_Object((1,3,6,1,4,1,7244,2,11,1,2),_AgentSSLSecurePort_Type())
agentSSLSecurePort.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSLSecurePort.setStatus(_A)
class _AgentSSLProtocolLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ssl30',1),('tls10',2),(_E,3)))
_AgentSSLProtocolLevel_Type.__name__=_B
_AgentSSLProtocolLevel_Object=MibScalar
agentSSLProtocolLevel=_AgentSSLProtocolLevel_Object((1,3,6,1,4,1,7244,2,11,1,3),_AgentSSLProtocolLevel_Type())
agentSSLProtocolLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSLProtocolLevel.setStatus(_A)
class _AgentSSLMaxSessions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AgentSSLMaxSessions_Type.__name__=_B
_AgentSSLMaxSessions_Object=MibScalar
agentSSLMaxSessions=_AgentSSLMaxSessions_Object((1,3,6,1,4,1,7244,2,11,1,4),_AgentSSLMaxSessions_Type())
agentSSLMaxSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSLMaxSessions.setStatus(_A)
class _AgentSSLHardTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,168))
_AgentSSLHardTimeout_Type.__name__=_B
_AgentSSLHardTimeout_Object=MibScalar
agentSSLHardTimeout=_AgentSSLHardTimeout_Object((1,3,6,1,4,1,7244,2,11,1,5),_AgentSSLHardTimeout_Type())
agentSSLHardTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSLHardTimeout.setStatus(_A)
class _AgentSSLSoftTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_AgentSSLSoftTimeout_Type.__name__=_B
_AgentSSLSoftTimeout_Object=MibScalar
agentSSLSoftTimeout=_AgentSSLSoftTimeout_Object((1,3,6,1,4,1,7244,2,11,1,6),_AgentSSLSoftTimeout_Type())
agentSSLSoftTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSLSoftTimeout.setStatus(_A)
_AgentSSLCertificatePresent_Type=TruthValue
_AgentSSLCertificatePresent_Object=MibScalar
agentSSLCertificatePresent=_AgentSSLCertificatePresent_Object((1,3,6,1,4,1,7244,2,11,1,7),_AgentSSLCertificatePresent_Type())
agentSSLCertificatePresent.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSSLCertificatePresent.setStatus(_A)
class _AgentSSLCertificateControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_AgentSSLCertificateControl_Type.__name__=_B
_AgentSSLCertificateControl_Object=MibScalar
agentSSLCertificateControl=_AgentSSLCertificateControl_Object((1,3,6,1,4,1,7244,2,11,1,8),_AgentSSLCertificateControl_Type())
agentSSLCertificateControl.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSLCertificateControl.setStatus(_A)
_AgentSSLCertificateGenerationStatus_Type=TruthValue
_AgentSSLCertificateGenerationStatus_Object=MibScalar
agentSSLCertificateGenerationStatus=_AgentSSLCertificateGenerationStatus_Object((1,3,6,1,4,1,7244,2,11,1,9),_AgentSSLCertificateGenerationStatus_Type())
agentSSLCertificateGenerationStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSSLCertificateGenerationStatus.setStatus(_A)
_AgentSSHConfigGroup_ObjectIdentity=ObjectIdentity
agentSSHConfigGroup=_AgentSSHConfigGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,11,2))
class _AgentSSHAdminMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_AgentSSHAdminMode_Type.__name__=_B
_AgentSSHAdminMode_Object=MibScalar
agentSSHAdminMode=_AgentSSHAdminMode_Object((1,3,6,1,4,1,7244,2,11,2,1),_AgentSSHAdminMode_Type())
agentSSHAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSHAdminMode.setStatus(_A)
class _AgentSSHProtocolLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ssh10',1),('ssh20',2),(_E,3)))
_AgentSSHProtocolLevel_Type.__name__=_B
_AgentSSHProtocolLevel_Object=MibScalar
agentSSHProtocolLevel=_AgentSSHProtocolLevel_Object((1,3,6,1,4,1,7244,2,11,2,2),_AgentSSHProtocolLevel_Type())
agentSSHProtocolLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSHProtocolLevel.setStatus(_A)
_AgentSSHSessionsCount_Type=Integer32
_AgentSSHSessionsCount_Object=MibScalar
agentSSHSessionsCount=_AgentSSHSessionsCount_Object((1,3,6,1,4,1,7244,2,11,2,3),_AgentSSHSessionsCount_Type())
agentSSHSessionsCount.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSSHSessionsCount.setStatus(_A)
class _AgentSSHMaxSessionsCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_AgentSSHMaxSessionsCount_Type.__name__=_B
_AgentSSHMaxSessionsCount_Object=MibScalar
agentSSHMaxSessionsCount=_AgentSSHMaxSessionsCount_Object((1,3,6,1,4,1,7244,2,11,2,4),_AgentSSHMaxSessionsCount_Type())
agentSSHMaxSessionsCount.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSHMaxSessionsCount.setStatus(_A)
class _AgentSSHSessionTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,160))
_AgentSSHSessionTimeout_Type.__name__=_B
_AgentSSHSessionTimeout_Object=MibScalar
agentSSHSessionTimeout=_AgentSSHSessionTimeout_Object((1,3,6,1,4,1,7244,2,11,2,5),_AgentSSHSessionTimeout_Type())
agentSSHSessionTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSHSessionTimeout.setStatus(_A)
class _AgentSSHKeysPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dsa',1),('rsa',2),(_E,3),('none',4)))
_AgentSSHKeysPresent_Type.__name__=_B
_AgentSSHKeysPresent_Object=MibScalar
agentSSHKeysPresent=_AgentSSHKeysPresent_Object((1,3,6,1,4,1,7244,2,11,2,6),_AgentSSHKeysPresent_Type())
agentSSHKeysPresent.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSSHKeysPresent.setStatus(_A)
class _AgentSSHKeyGenerationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dsa',1),('rsa',2),(_E,3),('none',4)))
_AgentSSHKeyGenerationStatus_Type.__name__=_B
_AgentSSHKeyGenerationStatus_Object=MibScalar
agentSSHKeyGenerationStatus=_AgentSSHKeyGenerationStatus_Object((1,3,6,1,4,1,7244,2,11,2,7),_AgentSSHKeyGenerationStatus_Type())
agentSSHKeyGenerationStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSSHKeyGenerationStatus.setStatus(_A)
class _AgentSSHRSAKeyControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_AgentSSHRSAKeyControl_Type.__name__=_B
_AgentSSHRSAKeyControl_Object=MibScalar
agentSSHRSAKeyControl=_AgentSSHRSAKeyControl_Object((1,3,6,1,4,1,7244,2,11,2,8),_AgentSSHRSAKeyControl_Type())
agentSSHRSAKeyControl.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSHRSAKeyControl.setStatus(_A)
class _AgentSSHDSAKeyControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_AgentSSHDSAKeyControl_Type.__name__=_B
_AgentSSHDSAKeyControl_Object=MibScalar
agentSSHDSAKeyControl=_AgentSSHDSAKeyControl_Object((1,3,6,1,4,1,7244,2,11,2,9),_AgentSSHDSAKeyControl_Type())
agentSSHDSAKeyControl.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSHDSAKeyControl.setStatus(_A)
mibBuilder.exportSymbols('MGMT-SECURITY-MIB',**{'mgmtSecurity':mgmtSecurity,'agentSSLConfigGroup':agentSSLConfigGroup,'agentSSLAdminMode':agentSSLAdminMode,'agentSSLSecurePort':agentSSLSecurePort,'agentSSLProtocolLevel':agentSSLProtocolLevel,'agentSSLMaxSessions':agentSSLMaxSessions,'agentSSLHardTimeout':agentSSLHardTimeout,'agentSSLSoftTimeout':agentSSLSoftTimeout,'agentSSLCertificatePresent':agentSSLCertificatePresent,'agentSSLCertificateControl':agentSSLCertificateControl,'agentSSLCertificateGenerationStatus':agentSSLCertificateGenerationStatus,'agentSSHConfigGroup':agentSSHConfigGroup,'agentSSHAdminMode':agentSSHAdminMode,'agentSSHProtocolLevel':agentSSHProtocolLevel,'agentSSHSessionsCount':agentSSHSessionsCount,'agentSSHMaxSessionsCount':agentSSHMaxSessionsCount,'agentSSHSessionTimeout':agentSSHSessionTimeout,'agentSSHKeysPresent':agentSSHKeysPresent,'agentSSHKeyGenerationStatus':agentSSHKeyGenerationStatus,'agentSSHRSAKeyControl':agentSSHRSAKeyControl,'agentSSHDSAKeyControl':agentSSHDSAKeyControl})