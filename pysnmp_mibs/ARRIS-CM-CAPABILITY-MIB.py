if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
arrisProdIdCM,=mibBuilder.importSymbols('ARRIS-MIB','arrisProdIdCM')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
modemCapabilities=ModuleIdentity((1,3,6,1,4,1,4115,1,3,20))
_ModemCapabilitiesObjects_ObjectIdentity=ObjectIdentity
modemCapabilitiesObjects=_ModemCapabilitiesObjects_ObjectIdentity((1,3,6,1,4,1,4115,1,3,20,1))
_ModemAgentDocsis10_ObjectIdentity=ObjectIdentity
modemAgentDocsis10=_ModemAgentDocsis10_ObjectIdentity((1,3,6,1,4,1,4115,1,3,20,1,1))
_ModemAgentDocsis11_ObjectIdentity=ObjectIdentity
modemAgentDocsis11=_ModemAgentDocsis11_ObjectIdentity((1,3,6,1,4,1,4115,1,3,20,1,2))
_ModemAgentDocsis20_ObjectIdentity=ObjectIdentity
modemAgentDocsis20=_ModemAgentDocsis20_ObjectIdentity((1,3,6,1,4,1,4115,1,3,20,1,3))
mibBuilder.exportSymbols('ARRIS-CM-CAPABILITY-MIB',**{'modemCapabilities':modemCapabilities,'modemCapabilitiesObjects':modemCapabilitiesObjects,'modemAgentDocsis10':modemAgentDocsis10,'modemAgentDocsis11':modemAgentDocsis11,'modemAgentDocsis20':modemAgentDocsis20})