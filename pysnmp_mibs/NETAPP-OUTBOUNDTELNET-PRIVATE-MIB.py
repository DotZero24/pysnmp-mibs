_C='current'
_B='read-write'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fastPath,=mibBuilder.importSymbols('NETAPP-REF-MIB','fastPath')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fastPathOutboundTelnetPrivate=ModuleIdentity((1,3,6,1,4,1,789,4413,1,1,19))
if mibBuilder.loadTexts:fastPathOutboundTelnetPrivate.setRevisions(('2011-01-26 00:00','2007-05-23 00:00'))
_AgentOutboundTelnetGroup_ObjectIdentity=ObjectIdentity
agentOutboundTelnetGroup=_AgentOutboundTelnetGroup_ObjectIdentity((1,3,6,1,4,1,789,4413,1,1,19,1))
class _AgentOutboundTelnetAdminMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AgentOutboundTelnetAdminMode_Type.__name__=_A
_AgentOutboundTelnetAdminMode_Object=MibScalar
agentOutboundTelnetAdminMode=_AgentOutboundTelnetAdminMode_Object((1,3,6,1,4,1,789,4413,1,1,19,1,1),_AgentOutboundTelnetAdminMode_Type())
agentOutboundTelnetAdminMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOutboundTelnetAdminMode.setStatus(_C)
class _AgentOutboundTelnetMaxNoOfSessions_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_AgentOutboundTelnetMaxNoOfSessions_Type.__name__=_A
_AgentOutboundTelnetMaxNoOfSessions_Object=MibScalar
agentOutboundTelnetMaxNoOfSessions=_AgentOutboundTelnetMaxNoOfSessions_Object((1,3,6,1,4,1,789,4413,1,1,19,1,2),_AgentOutboundTelnetMaxNoOfSessions_Type())
agentOutboundTelnetMaxNoOfSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOutboundTelnetMaxNoOfSessions.setStatus(_C)
class _AgentOutboundTelnetTimeout_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,160))
_AgentOutboundTelnetTimeout_Type.__name__=_A
_AgentOutboundTelnetTimeout_Object=MibScalar
agentOutboundTelnetTimeout=_AgentOutboundTelnetTimeout_Object((1,3,6,1,4,1,789,4413,1,1,19,1,3),_AgentOutboundTelnetTimeout_Type())
agentOutboundTelnetTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOutboundTelnetTimeout.setStatus(_C)
mibBuilder.exportSymbols('NETAPP-OUTBOUNDTELNET-PRIVATE-MIB',**{'fastPathOutboundTelnetPrivate':fastPathOutboundTelnetPrivate,'agentOutboundTelnetGroup':agentOutboundTelnetGroup,'agentOutboundTelnetAdminMode':agentOutboundTelnetAdminMode,'agentOutboundTelnetMaxNoOfSessions':agentOutboundTelnetMaxNoOfSessions,'agentOutboundTelnetTimeout':agentOutboundTelnetTimeout})