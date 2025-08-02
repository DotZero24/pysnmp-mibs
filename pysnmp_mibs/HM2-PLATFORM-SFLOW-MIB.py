if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hm2PlatformMibs,=mibBuilder.importSymbols('HM2-TC-MIB','hm2PlatformMibs')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hm2PlatformSflow=ModuleIdentity((1,3,6,1,4,1,248,12,59))
if mibBuilder.loadTexts:hm2PlatformSflow.setRevisions(('2011-10-12 00:00',))
_Hm2AgentFastPathSflowObjects_ObjectIdentity=ObjectIdentity
hm2AgentFastPathSflowObjects=_Hm2AgentFastPathSflowObjects_ObjectIdentity((1,3,6,1,4,1,248,12,59,1))
_Hm2AgentSflowSourceInterface_Type=InterfaceIndexOrZero
_Hm2AgentSflowSourceInterface_Object=MibScalar
hm2AgentSflowSourceInterface=_Hm2AgentSflowSourceInterface_Object((1,3,6,1,4,1,248,12,59,1,1),_Hm2AgentSflowSourceInterface_Type())
hm2AgentSflowSourceInterface.setMaxAccess('read-write')
if mibBuilder.loadTexts:hm2AgentSflowSourceInterface.setStatus('current')
mibBuilder.exportSymbols('HM2-PLATFORM-SFLOW-MIB',**{'hm2PlatformSflow':hm2PlatformSflow,'hm2AgentFastPathSflowObjects':hm2AgentFastPathSflowObjects,'hm2AgentSflowSourceInterface':hm2AgentSflowSourceInterface})