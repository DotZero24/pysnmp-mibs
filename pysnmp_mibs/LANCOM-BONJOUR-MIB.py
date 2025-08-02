_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fastPath,=mibBuilder.importSymbols('LANCOM-REF-MIB','fastPath')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fastPathBonjour=ModuleIdentity((1,3,6,1,4,1,2356,16,1,71))
if mibBuilder.loadTexts:fastPathBonjour.setRevisions(('2017-06-06 00:00',))
_AgentBonjourObjects_ObjectIdentity=ObjectIdentity
agentBonjourObjects=_AgentBonjourObjects_ObjectIdentity((1,3,6,1,4,1,2356,16,1,71,1))
_AgentBonjourGlobal_ObjectIdentity=ObjectIdentity
agentBonjourGlobal=_AgentBonjourGlobal_ObjectIdentity((1,3,6,1,4,1,2356,16,1,71,1,1))
class _AgentBonjourAdminMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_AgentBonjourAdminMode_Type.__name__=_A
_AgentBonjourAdminMode_Object=MibScalar
agentBonjourAdminMode=_AgentBonjourAdminMode_Object((1,3,6,1,4,1,2356,16,1,71,1,1,1),_AgentBonjourAdminMode_Type())
agentBonjourAdminMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:agentBonjourAdminMode.setStatus('current')
mibBuilder.exportSymbols('LANCOM-BONJOUR-MIB',**{'fastPathBonjour':fastPathBonjour,'agentBonjourObjects':agentBonjourObjects,'agentBonjourGlobal':agentBonjourGlobal,'agentBonjourAdminMode':agentBonjourAdminMode})