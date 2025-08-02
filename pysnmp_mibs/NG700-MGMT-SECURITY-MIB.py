_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ng700smartswitch,=mibBuilder.importSymbols('NG700-REF-MIB','ng700smartswitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
fastPathMgmtSecurity=ModuleIdentity((1,3,6,1,4,1,4526,11,11))
if mibBuilder.loadTexts:fastPathMgmtSecurity.setRevisions(('2011-01-26 00:00','2007-05-23 00:00','2003-11-21 00:00'))
_AgentSSLConfigGroup_ObjectIdentity=ObjectIdentity
agentSSLConfigGroup=_AgentSSLConfigGroup_ObjectIdentity((1,3,6,1,4,1,4526,11,11,1))
class _AgentSSLAdminMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AgentSSLAdminMode_Type.__name__=_B
_AgentSSLAdminMode_Object=MibScalar
agentSSLAdminMode=_AgentSSLAdminMode_Object((1,3,6,1,4,1,4526,11,11,1,1),_AgentSSLAdminMode_Type())
agentSSLAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSLAdminMode.setStatus(_A)
class _AgentSSLSecurePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65535))
_AgentSSLSecurePort_Type.__name__=_B
_AgentSSLSecurePort_Object=MibScalar
agentSSLSecurePort=_AgentSSLSecurePort_Object((1,3,6,1,4,1,4526,11,11,1,2),_AgentSSLSecurePort_Type())
agentSSLSecurePort.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSLSecurePort.setStatus(_A)
class _AgentSSLProtocolLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ssl30',1),('tls10',2),('both',3)))
_AgentSSLProtocolLevel_Type.__name__=_B
_AgentSSLProtocolLevel_Object=MibScalar
agentSSLProtocolLevel=_AgentSSLProtocolLevel_Object((1,3,6,1,4,1,4526,11,11,1,3),_AgentSSLProtocolLevel_Type())
agentSSLProtocolLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSLProtocolLevel.setStatus(_A)
class _AgentSSLMaxSessions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AgentSSLMaxSessions_Type.__name__=_B
_AgentSSLMaxSessions_Object=MibScalar
agentSSLMaxSessions=_AgentSSLMaxSessions_Object((1,3,6,1,4,1,4526,11,11,1,4),_AgentSSLMaxSessions_Type())
agentSSLMaxSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSLMaxSessions.setStatus(_A)
class _AgentSSLHardTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,168))
_AgentSSLHardTimeout_Type.__name__=_B
_AgentSSLHardTimeout_Object=MibScalar
agentSSLHardTimeout=_AgentSSLHardTimeout_Object((1,3,6,1,4,1,4526,11,11,1,5),_AgentSSLHardTimeout_Type())
agentSSLHardTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSLHardTimeout.setStatus(_A)
class _AgentSSLSoftTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_AgentSSLSoftTimeout_Type.__name__=_B
_AgentSSLSoftTimeout_Object=MibScalar
agentSSLSoftTimeout=_AgentSSLSoftTimeout_Object((1,3,6,1,4,1,4526,11,11,1,6),_AgentSSLSoftTimeout_Type())
agentSSLSoftTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSLSoftTimeout.setStatus(_A)
_AgentSSLCertificatePresent_Type=TruthValue
_AgentSSLCertificatePresent_Object=MibScalar
agentSSLCertificatePresent=_AgentSSLCertificatePresent_Object((1,3,6,1,4,1,4526,11,11,1,7),_AgentSSLCertificatePresent_Type())
agentSSLCertificatePresent.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSSLCertificatePresent.setStatus(_A)
class _AgentSSLCertificateControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noop',1),('generate',2),('delete',3)))
_AgentSSLCertificateControl_Type.__name__=_B
_AgentSSLCertificateControl_Object=MibScalar
agentSSLCertificateControl=_AgentSSLCertificateControl_Object((1,3,6,1,4,1,4526,11,11,1,8),_AgentSSLCertificateControl_Type())
agentSSLCertificateControl.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSLCertificateControl.setStatus(_A)
_AgentSSLCertificateGenerationStatus_Type=TruthValue
_AgentSSLCertificateGenerationStatus_Object=MibScalar
agentSSLCertificateGenerationStatus=_AgentSSLCertificateGenerationStatus_Object((1,3,6,1,4,1,4526,11,11,1,9),_AgentSSLCertificateGenerationStatus_Type())
agentSSLCertificateGenerationStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSSLCertificateGenerationStatus.setStatus(_A)
mibBuilder.exportSymbols('NG700-MGMT-SECURITY-MIB',**{'fastPathMgmtSecurity':fastPathMgmtSecurity,'agentSSLConfigGroup':agentSSLConfigGroup,'agentSSLAdminMode':agentSSLAdminMode,'agentSSLSecurePort':agentSSLSecurePort,'agentSSLProtocolLevel':agentSSLProtocolLevel,'agentSSLMaxSessions':agentSSLMaxSessions,'agentSSLHardTimeout':agentSSLHardTimeout,'agentSSLSoftTimeout':agentSSLSoftTimeout,'agentSSLCertificatePresent':agentSSLCertificatePresent,'agentSSLCertificateControl':agentSSLCertificateControl,'agentSSLCertificateGenerationStatus':agentSSLCertificateGenerationStatus})