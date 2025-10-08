#
# PySNMP MIB module CT-DAREGISTRY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cabletron/CT-DAREGISTRY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:13:08 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cabletron, = mibBuilder.importSymbols("CTRON-OIDS", "cabletron")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CT-DAREGISTRY-MIB", ctDARegistryTable=ctDARegistryTable, ctDARegistryLastChange=ctDARegistryLastChange, ctSSA=ctSSA, DisplayString=DisplayString, ctDARegistryEntry=ctDARegistryEntry, ctDARegistryAdminStatus=ctDARegistryAdminStatus, ctDARegistryOperStatus=ctDARegistryOperStatus, ctDARegistryIndex=ctDARegistryIndex, ctDARegistryInstance=ctDARegistryInstance, ctDARegistryDescr=ctDARegistryDescr)
