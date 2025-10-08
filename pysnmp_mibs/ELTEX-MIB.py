#
# PySNMP MIB module ELTEX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:40 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("ELTEX-MIB", elt=elt, NetNumber=NetNumber, eltRadius=eltRadius, eltQosTailDropMib=eltQosTailDropMib, eltEndOfMibGroup=eltEndOfMibGroup, PYSNMP_MODULE_ID=elt, eltPhy=eltPhy, eltMacMulticast=eltMacMulticast, eltIpMulticast=eltIpMulticast, eltIpOspfMtu=eltIpOspfMtu, eltIpBfd=eltIpBfd, VlanPriority=VlanPriority, eltStormCtrl=eltStormCtrl, eltIpUnnumbered=eltIpUnnumbered, eltQosCliMib=eltQosCliMib, eltDhcp=eltDhcp, eltDevParams=eltDevParams, eltSwInterfaces=eltSwInterfaces, eltPhdTransceiver=eltPhdTransceiver, eltLinkAgg=eltLinkAgg, eltNotifications=eltNotifications, ipSpec=ipSpec, eltBridgeSecurity=eltBridgeSecurity, eltdot1x=eltdot1x, Percents=Percents, eltCopy=eltCopy, eltTuning=eltTuning, eltMng=eltMng)
