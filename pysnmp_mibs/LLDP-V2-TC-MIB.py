_G='interfaceName'
_F='networkAddress'
_E='macAddress'
_D='portComponent'
_C='interfaceAlias'
_B='1x:'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,org=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','org')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
lldpV2TcMIB=ModuleIdentity((1,3,111,2,802,1,1,12))
if mibBuilder.loadTexts:lldpV2TcMIB.setRevisions(('2016-03-11 00:00','2009-06-08 00:00'))
class LldpV2ChassisIdSubtype(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('chassisComponent',1),(_C,2),(_D,3),(_E,4),(_F,5),(_G,6),('local',7)))
class LldpV2ChassisId(TextualConvention,OctetString):status=_A;displayHint=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
class LldpV2PortIdSubtype(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_C,1),(_D,2),(_E,3),(_F,4),(_G,5),('agentCircuitId',6),('local',7)))
class LldpV2PortId(TextualConvention,OctetString):status=_A;displayHint=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
class LldpV2ManAddrIfSubtype(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('ifIndex',2),('systemPortNumber',3)))
class LldpV2ManAddress(TextualConvention,OctetString):status=_A;displayHint=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
class LldpV2SystemCapabilitiesMap(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('other',0),('repeater',1),('bridge',2),('wlanAccessPoint',3),('router',4),('telephone',5),('docsisCableDevice',6),('stationOnly',7),('cVLANComponent',8),('sVLANComponent',9),('twoPortMACRelay',10)))
class LldpV2DestAddressTableIndex(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
class LldpV2PowerPortClass(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pClassPSE',1),('pClassPD',2)))
_Ieee802dot1mibs_ObjectIdentity=ObjectIdentity
ieee802dot1mibs=_Ieee802dot1mibs_ObjectIdentity((1,3,111,2,802,1,1))
mibBuilder.exportSymbols('LLDP-V2-TC-MIB',**{'LldpV2ChassisIdSubtype':LldpV2ChassisIdSubtype,'LldpV2ChassisId':LldpV2ChassisId,'LldpV2PortIdSubtype':LldpV2PortIdSubtype,'LldpV2PortId':LldpV2PortId,'LldpV2ManAddrIfSubtype':LldpV2ManAddrIfSubtype,'LldpV2ManAddress':LldpV2ManAddress,'LldpV2SystemCapabilitiesMap':LldpV2SystemCapabilitiesMap,'LldpV2DestAddressTableIndex':LldpV2DestAddressTableIndex,'LldpV2PowerPortClass':LldpV2PowerPortClass,'ieee802dot1mibs':ieee802dot1mibs,'lldpV2TcMIB':lldpV2TcMIB})