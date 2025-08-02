if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Cabletron_ObjectIdentity=ObjectIdentity
cabletron=_Cabletron_ObjectIdentity((1,3,6,1,4,1,52))
_CtronProducts_ObjectIdentity=ObjectIdentity
ctronProducts=_CtronProducts_ObjectIdentity((1,3,6,1,4,1,52,10))
_Ssr3000_ObjectIdentity=ObjectIdentity
ssr3000=_Ssr3000_ObjectIdentity((1,3,6,1,4,1,52,10,1))
_Ssr32000_ObjectIdentity=ObjectIdentity
ssr32000=_Ssr32000_ObjectIdentity((1,3,6,1,4,1,52,10,2))
mibBuilder.exportSymbols('CTRON-PRODUCTS-MIB',**{'cabletron':cabletron,'ctronProducts':ctronProducts,'ssr3000':ssr3000,'ssr32000':ssr32000})