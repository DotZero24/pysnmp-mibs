_C='current'
_B='read-write'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch,=mibBuilder.importSymbols('QUANTA-SWITCH-MIB','switch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
outboundSSHPrivate=ModuleIdentity((1,3,6,1,4,1,7244,2,21))
_AgentOutboundSSHGroup_ObjectIdentity=ObjectIdentity
agentOutboundSSHGroup=_AgentOutboundSSHGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,21,1))
class _AgentOutboundSSHAdminMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AgentOutboundSSHAdminMode_Type.__name__=_A
_AgentOutboundSSHAdminMode_Object=MibScalar
agentOutboundSSHAdminMode=_AgentOutboundSSHAdminMode_Object((1,3,6,1,4,1,7244,2,21,1,1),_AgentOutboundSSHAdminMode_Type())
agentOutboundSSHAdminMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOutboundSSHAdminMode.setStatus(_C)
class _AgentOutboundSSHMaxNoOfSessions_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_AgentOutboundSSHMaxNoOfSessions_Type.__name__=_A
_AgentOutboundSSHMaxNoOfSessions_Object=MibScalar
agentOutboundSSHMaxNoOfSessions=_AgentOutboundSSHMaxNoOfSessions_Object((1,3,6,1,4,1,7244,2,21,1,2),_AgentOutboundSSHMaxNoOfSessions_Type())
agentOutboundSSHMaxNoOfSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOutboundSSHMaxNoOfSessions.setStatus(_C)
class _AgentOutboundSSHTimeout_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,160))
_AgentOutboundSSHTimeout_Type.__name__=_A
_AgentOutboundSSHTimeout_Object=MibScalar
agentOutboundSSHTimeout=_AgentOutboundSSHTimeout_Object((1,3,6,1,4,1,7244,2,21,1,3),_AgentOutboundSSHTimeout_Type())
agentOutboundSSHTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOutboundSSHTimeout.setStatus(_C)
mibBuilder.exportSymbols('OUTBOUNDSSH-PRIVATE-MIB',**{'outboundSSHPrivate':outboundSSHPrivate,'agentOutboundSSHGroup':agentOutboundSSHGroup,'agentOutboundSSHAdminMode':agentOutboundSSHAdminMode,'agentOutboundSSHMaxNoOfSessions':agentOutboundSSHMaxNoOfSessions,'agentOutboundSSHTimeout':agentOutboundSSHTimeout})