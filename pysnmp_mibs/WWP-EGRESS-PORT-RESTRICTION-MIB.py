#
# PySNMP MIB module WWP-EGRESS-PORT-RESTRICTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ciena/WWP-EGRESS-PORT-RESTRICTION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:06 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("WWP-EGRESS-PORT-RESTRICTION-MIB", wwpEgressPortRestrictionEntry=wwpEgressPortRestrictionEntry, wwpEgressPortRestrictionMIBObjects=wwpEgressPortRestrictionMIBObjects, wwpERestStatus=wwpERestStatus, wwpEgressPortRestrictionMIBGroups=wwpEgressPortRestrictionMIBGroups, wwpERestPortId=wwpERestPortId, wwpEgressPortRestrictionTable=wwpEgressPortRestrictionTable, PYSNMP_MODULE_ID=wwpEgressPortRestrictionMIB, wwpERestVlanId=wwpERestVlanId, wwpEgressPortRestriction=wwpEgressPortRestriction, wwpEgressPortRestrictionNotificationPrefix=wwpEgressPortRestrictionNotificationPrefix, PortList=PortList, wwpEgressPortRestrictionNotifications=wwpEgressPortRestrictionNotifications, wwpERestEgreesPorts=wwpERestEgreesPorts, VlanId=VlanId, wwpEgressPortRestrictionMIBCompliances=wwpEgressPortRestrictionMIBCompliances, wwpEgressPortRestrictionMIBConformance=wwpEgressPortRestrictionMIBConformance, wwpEgressPortRestrictionMIB=wwpEgressPortRestrictionMIB)
