#
# PySNMP MIB module WWP-EGRESS-PORT-RESTRICTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ciena/WWP-EGRESS-PORT-RESTRICTION-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:10:58 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
wwpModules, = mibBuilder.importSymbols("WWP-SMI", "wwpModules")
wwpEgressPortRestrictionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 34))
wwpEgressPortRestrictionMIB.setRevisions(('2001-04-03 17:00',))
if mibBuilder.loadTexts: wwpEgressPortRestrictionMIB.setLastUpdated('200104031700Z')
if mibBuilder.loadTexts: wwpEgressPortRestrictionMIB.setOrganization('World Wide Packets, Inc')
class PortList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class VlanId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

wwpEgressPortRestrictionMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 34, 1))
wwpEgressPortRestriction = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 34, 1, 1))
wwpEgressPortRestrictionNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 34, 2))
wwpEgressPortRestrictionNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 34, 2, 0))
wwpEgressPortRestrictionMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 34, 3))
wwpEgressPortRestrictionMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 34, 3, 1))
wwpEgressPortRestrictionMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 34, 3, 2))
wwpEgressPortRestrictionTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 34, 1, 1, 1), )
if mibBuilder.loadTexts: wwpEgressPortRestrictionTable.setStatus('current')
wwpEgressPortRestrictionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 34, 1, 1, 1, 1), ).setIndexNames((0, "WWP-EGRESS-PORT-RESTRICTION-MIB", "wwpERestVlanId"), (0, "WWP-EGRESS-PORT-RESTRICTION-MIB", "wwpERestPortId"))
if mibBuilder.loadTexts: wwpEgressPortRestrictionEntry.setStatus('current')
wwpERestVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 34, 1, 1, 1, 1, 1), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpERestVlanId.setStatus('current')
wwpERestPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 34, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpERestPortId.setStatus('current')
wwpERestEgreesPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 34, 1, 1, 1, 1, 3), PortList().clone(hexValue="0000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpERestEgreesPorts.setStatus('current')
wwpERestStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 34, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpERestStatus.setStatus('current')
mibBuilder.exportSymbols("WWP-EGRESS-PORT-RESTRICTION-MIB", wwpERestVlanId=wwpERestVlanId, wwpERestEgreesPorts=wwpERestEgreesPorts, wwpEgressPortRestrictionEntry=wwpEgressPortRestrictionEntry, wwpEgressPortRestrictionMIB=wwpEgressPortRestrictionMIB, wwpEgressPortRestrictionTable=wwpEgressPortRestrictionTable, PYSNMP_MODULE_ID=wwpEgressPortRestrictionMIB, wwpEgressPortRestrictionNotificationPrefix=wwpEgressPortRestrictionNotificationPrefix, wwpEgressPortRestrictionMIBConformance=wwpEgressPortRestrictionMIBConformance, wwpEgressPortRestrictionMIBGroups=wwpEgressPortRestrictionMIBGroups, wwpEgressPortRestriction=wwpEgressPortRestriction, PortList=PortList, wwpERestPortId=wwpERestPortId, wwpERestStatus=wwpERestStatus, wwpEgressPortRestrictionMIBObjects=wwpEgressPortRestrictionMIBObjects, wwpEgressPortRestrictionNotifications=wwpEgressPortRestrictionNotifications, VlanId=VlanId, wwpEgressPortRestrictionMIBCompliances=wwpEgressPortRestrictionMIBCompliances)
