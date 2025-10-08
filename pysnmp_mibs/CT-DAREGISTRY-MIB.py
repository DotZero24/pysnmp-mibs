#
# PySNMP MIB module CT-DAREGISTRY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cabletron/CT-DAREGISTRY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:05:30 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cabletron, = mibBuilder.importSymbols("CTRON-OIDS", "cabletron")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctSSA = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4497))
class DisplayString(OctetString):
    pass

ctDARegistryTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4497, 1), )
if mibBuilder.loadTexts: ctDARegistryTable.setStatus('mandatory')
ctDARegistryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4497, 1, 1), ).setIndexNames((0, "CT-DAREGISTRY-MIB", "ctDARegistryIndex"), (0, "CT-DAREGISTRY-MIB", "ctDARegistryInstance"))
if mibBuilder.loadTexts: ctDARegistryEntry.setStatus('mandatory')
ctDARegistryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDARegistryIndex.setStatus('mandatory')
ctDARegistryInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDARegistryInstance.setStatus('mandatory')
ctDARegistryAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDARegistryAdminStatus.setStatus('mandatory')
ctDARegistryOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDARegistryOperStatus.setStatus('mandatory')
ctDARegistryLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDARegistryLastChange.setStatus('mandatory')
ctDARegistryDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDARegistryDescr.setStatus('mandatory')
mibBuilder.exportSymbols("CT-DAREGISTRY-MIB", ctDARegistryAdminStatus=ctDARegistryAdminStatus, ctDARegistryLastChange=ctDARegistryLastChange, ctSSA=ctSSA, ctDARegistryDescr=ctDARegistryDescr, ctDARegistryInstance=ctDARegistryInstance, ctDARegistryIndex=ctDARegistryIndex, ctDARegistryOperStatus=ctDARegistryOperStatus, ctDARegistryTable=ctDARegistryTable, DisplayString=DisplayString, ctDARegistryEntry=ctDARegistryEntry)
