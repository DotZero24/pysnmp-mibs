_D='Integer32'
_C='current'
_B='read-write'
_A='Unsigned32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ng7000managedswitch,=mibBuilder.importSymbols('NETGEAR-REF-MIB','ng7000managedswitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_A,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fastPathInterfaceApp=ModuleIdentity((1,3,6,1,4,1,4526,10,70))
if mibBuilder.loadTexts:fastPathInterfaceApp.setRevisions(('2016-08-18 00:00',))
_AgentLinkFlapMIBObjects_ObjectIdentity=ObjectIdentity
agentLinkFlapMIBObjects=_AgentLinkFlapMIBObjects_ObjectIdentity((1,3,6,1,4,1,4526,10,70,1))
_AgentLinkFlapGlobal_ObjectIdentity=ObjectIdentity
agentLinkFlapGlobal=_AgentLinkFlapGlobal_ObjectIdentity((1,3,6,1,4,1,4526,10,70,1,1))
class _AgentLinkFlapAdminMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AgentLinkFlapAdminMode_Type.__name__=_D
_AgentLinkFlapAdminMode_Object=MibScalar
agentLinkFlapAdminMode=_AgentLinkFlapAdminMode_Object((1,3,6,1,4,1,4526,10,70,1,1,1),_AgentLinkFlapAdminMode_Type())
agentLinkFlapAdminMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentLinkFlapAdminMode.setStatus(_C)
class _AgentLinkFlapDuration_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,200))
_AgentLinkFlapDuration_Type.__name__=_A
_AgentLinkFlapDuration_Object=MibScalar
agentLinkFlapDuration=_AgentLinkFlapDuration_Object((1,3,6,1,4,1,4526,10,70,1,1,2),_AgentLinkFlapDuration_Type())
agentLinkFlapDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:agentLinkFlapDuration.setStatus(_C)
if mibBuilder.loadTexts:agentLinkFlapDuration.setUnits('seconds')
class _AgentLinkFlapMaxCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,100))
_AgentLinkFlapMaxCount_Type.__name__=_A
_AgentLinkFlapMaxCount_Object=MibScalar
agentLinkFlapMaxCount=_AgentLinkFlapMaxCount_Object((1,3,6,1,4,1,4526,10,70,1,1,3),_AgentLinkFlapMaxCount_Type())
agentLinkFlapMaxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentLinkFlapMaxCount.setStatus(_C)
mibBuilder.exportSymbols('NETGEAR-INTERFACE-APP-MIB',**{'fastPathInterfaceApp':fastPathInterfaceApp,'agentLinkFlapMIBObjects':agentLinkFlapMIBObjects,'agentLinkFlapGlobal':agentLinkFlapGlobal,'agentLinkFlapAdminMode':agentLinkFlapAdminMode,'agentLinkFlapDuration':agentLinkFlapDuration,'agentLinkFlapMaxCount':agentLinkFlapMaxCount})