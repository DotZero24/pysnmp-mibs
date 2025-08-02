if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fastPath,=mibBuilder.importSymbols('EdgeSwitch-REF-MIB','fastPath')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fastPathSflow=ModuleIdentity((1,3,6,1,4,1,4413,1,1,59))
_AgentFastPathSflowObjects_ObjectIdentity=ObjectIdentity
agentFastPathSflowObjects=_AgentFastPathSflowObjects_ObjectIdentity((1,3,6,1,4,1,4413,1,1,59,1))
_AgentSflowSourceInterface_Type=InterfaceIndexOrZero
_AgentSflowSourceInterface_Object=MibScalar
agentSflowSourceInterface=_AgentSflowSourceInterface_Object((1,3,6,1,4,1,4413,1,1,59,1,1),_AgentSflowSourceInterface_Type())
agentSflowSourceInterface.setMaxAccess('read-write')
if mibBuilder.loadTexts:agentSflowSourceInterface.setStatus('current')
mibBuilder.exportSymbols('EdgeSwitch-SFLOW-MIB',**{'fastPathSflow':fastPathSflow,'agentFastPathSflowObjects':agentFastPathSflowObjects,'agentSflowSourceInterface':agentSflowSourceInterface})