_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','experimental','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bgp4V2TC=ModuleIdentity((1,3,6,1,3,5,1))
if mibBuilder.loadTexts:bgp4V2TC.setRevisions(('2014-01-23 00:00',))
class Bgp4V2IdentifierTC(TextualConvention,OctetString):status=_A;displayHint='1d.';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class Bgp4V2AddressFamilyIdentifierTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
class Bgp4V2SubsequentAddressFamilyIdentifierTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*(('unicast',1),('multicast',2),('mpls',4)))
_Frr_ObjectIdentity=ObjectIdentity
frr=_Frr_ObjectIdentity((1,3,6,1,3,5))
mibBuilder.exportSymbols('BGP4V2-TC-MIB',**{'Bgp4V2IdentifierTC':Bgp4V2IdentifierTC,'Bgp4V2AddressFamilyIdentifierTC':Bgp4V2AddressFamilyIdentifierTC,'Bgp4V2SubsequentAddressFamilyIdentifierTC':Bgp4V2SubsequentAddressFamilyIdentifierTC,'frr':frr,'bgp4V2TC':bgp4V2TC})