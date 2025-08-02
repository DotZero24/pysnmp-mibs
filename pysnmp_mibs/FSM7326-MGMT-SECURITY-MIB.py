_E='disable'
_D='enable'
_C='read-write'
_B='current'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsm7326,=mibBuilder.importSymbols('FSM7326-REF-MIB','fsm7326')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsm7326MgmtSecurity=ModuleIdentity((1,3,6,1,4,1,4526,1,9,11))
if mibBuilder.loadTexts:fsm7326MgmtSecurity.setRevisions(('2003-11-21 00:00',))
_AgentSSLConfigGroup_ObjectIdentity=ObjectIdentity
agentSSLConfigGroup=_AgentSSLConfigGroup_ObjectIdentity((1,3,6,1,4,1,4526,1,9,11,1))
class _AgentSSLAdminMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentSSLAdminMode_Type.__name__=_A
_AgentSSLAdminMode_Object=MibScalar
agentSSLAdminMode=_AgentSSLAdminMode_Object((1,3,6,1,4,1,4526,1,9,11,1,1),_AgentSSLAdminMode_Type())
agentSSLAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSLAdminMode.setStatus(_B)
class _AgentSSLSecurePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AgentSSLSecurePort_Type.__name__=_A
_AgentSSLSecurePort_Object=MibScalar
agentSSLSecurePort=_AgentSSLSecurePort_Object((1,3,6,1,4,1,4526,1,9,11,1,2),_AgentSSLSecurePort_Type())
agentSSLSecurePort.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSLSecurePort.setStatus(_B)
class _AgentSSLProtocolLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ssl30',1),('tls10',2),('both',3)))
_AgentSSLProtocolLevel_Type.__name__=_A
_AgentSSLProtocolLevel_Object=MibScalar
agentSSLProtocolLevel=_AgentSSLProtocolLevel_Object((1,3,6,1,4,1,4526,1,9,11,1,3),_AgentSSLProtocolLevel_Type())
agentSSLProtocolLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSLProtocolLevel.setStatus(_B)
_AgentSSHConfigGroup_ObjectIdentity=ObjectIdentity
agentSSHConfigGroup=_AgentSSHConfigGroup_ObjectIdentity((1,3,6,1,4,1,4526,1,9,11,2))
class _AgentSSHAdminMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentSSHAdminMode_Type.__name__=_A
_AgentSSHAdminMode_Object=MibScalar
agentSSHAdminMode=_AgentSSHAdminMode_Object((1,3,6,1,4,1,4526,1,9,11,2,1),_AgentSSHAdminMode_Type())
agentSSHAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSHAdminMode.setStatus(_B)
class _AgentSSHProtocolLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ssh10',1),('ssh20',2),('both',3)))
_AgentSSHProtocolLevel_Type.__name__=_A
_AgentSSHProtocolLevel_Object=MibScalar
agentSSHProtocolLevel=_AgentSSHProtocolLevel_Object((1,3,6,1,4,1,4526,1,9,11,2,2),_AgentSSHProtocolLevel_Type())
agentSSHProtocolLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSSHProtocolLevel.setStatus(_B)
_AgentSSHSessionsCount_Type=Integer32
_AgentSSHSessionsCount_Object=MibScalar
agentSSHSessionsCount=_AgentSSHSessionsCount_Object((1,3,6,1,4,1,4526,1,9,11,2,3),_AgentSSHSessionsCount_Type())
agentSSHSessionsCount.setMaxAccess('read-only')
if mibBuilder.loadTexts:agentSSHSessionsCount.setStatus(_B)
mibBuilder.exportSymbols('FSM7326-MGMT-SECURITY-MIB',**{'fsm7326MgmtSecurity':fsm7326MgmtSecurity,'agentSSLConfigGroup':agentSSLConfigGroup,'agentSSLAdminMode':agentSSLAdminMode,'agentSSLSecurePort':agentSSLSecurePort,'agentSSLProtocolLevel':agentSSLProtocolLevel,'agentSSHConfigGroup':agentSSHConfigGroup,'agentSSHAdminMode':agentSSHAdminMode,'agentSSHProtocolLevel':agentSSHProtocolLevel,'agentSSHSessionsCount':agentSSHSessionsCount})