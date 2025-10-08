#
# PySNMP MIB module ELTEX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:58 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class Percents(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class NetNumber(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class VlanPriority(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

elt = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265))
elt.setRevisions(('2012-12-18 00:00',))
if mibBuilder.loadTexts: elt.setLastUpdated('201212180000Z')
if mibBuilder.loadTexts: elt.setOrganization('Eltex Enterprise Co, Ltd.')
eltNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 35265, 0))
if mibBuilder.loadTexts: eltNotifications.setStatus('current')
eltMng = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1))
eltDevParams = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 2))
eltCopy = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 3))
eltIpOspfMtu = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 4))
eltIpBfd = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 6))
eltIpUnnumbered = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 7))
eltDhcp = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 8))
eltLinkAgg = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 9))
eltQosTailDropMib = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 12))
eltTuning = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 29))
eltSwInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 43))
eltIpMulticast = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 46))
eltPhdTransceiver = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 53))
eltMacMulticast = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 55))
eltStormCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 77))
eltRadius = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 80))
eltQosCliMib = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 88))
eltPhy = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 90))
ipSpec = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 91))
eltdot1x = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 95))
eltBridgeSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 112))
eltEndOfMibGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1000))
mibBuilder.exportSymbols("ELTEX-MIB", eltStormCtrl=eltStormCtrl, eltLinkAgg=eltLinkAgg, eltIpMulticast=eltIpMulticast, eltTuning=eltTuning, ipSpec=ipSpec, VlanPriority=VlanPriority, eltIpBfd=eltIpBfd, eltPhy=eltPhy, eltBridgeSecurity=eltBridgeSecurity, eltEndOfMibGroup=eltEndOfMibGroup, NetNumber=NetNumber, eltMacMulticast=eltMacMulticast, eltDhcp=eltDhcp, eltQosTailDropMib=eltQosTailDropMib, eltMng=eltMng, elt=elt, PYSNMP_MODULE_ID=elt, eltIpOspfMtu=eltIpOspfMtu, eltIpUnnumbered=eltIpUnnumbered, Percents=Percents, eltQosCliMib=eltQosCliMib, eltdot1x=eltdot1x, eltRadius=eltRadius, eltCopy=eltCopy, eltDevParams=eltDevParams, eltSwInterfaces=eltSwInterfaces, eltPhdTransceiver=eltPhdTransceiver, eltNotifications=eltNotifications)
