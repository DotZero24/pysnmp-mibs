#
# PySNMP MIB module TRAPEZE-NETWORKS-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/trapeze/TRAPEZE-NETWORKS-PORT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:05:16 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
TrpzPhysPortNumber, TrpzPhysPortNumberOrZero = mibBuilder.importSymbols("TRAPEZE-NETWORKS-BASIC-TC", "TrpzPhysPortNumber", "TrpzPhysPortNumberOrZero")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzPortMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 6))
trpzPortMib.setRevisions(('2008-10-23 00:10', '2008-05-19 00:04', '2006-11-09 00:01', '2006-04-06 00:00',))
if mibBuilder.loadTexts: trpzPortMib.setLastUpdated('200810230010Z')
if mibBuilder.loadTexts: trpzPortMib.setOrganization('Trapeze Networks')
class TrpzPortMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("directAttachAP", 1), ("networkPort", 2), ("wired", 3))

class TrpzPortPoeMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("poeEnable", 1), ("poeDisable", 2))

trpzPortObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1))
trpzPortDataObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 1))
trpzPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 1, 1), )
if mibBuilder.loadTexts: trpzPortConfigTable.setStatus('current')
trpzPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 1, 1, 1), ).setIndexNames((0, "TRAPEZE-NETWORKS-PORT-MIB", "trpzPortConfigPortNumber"))
if mibBuilder.loadTexts: trpzPortConfigEntry.setStatus('current')
trpzPortConfigPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 1, 1, 1, 1), TrpzPhysPortNumber())
if mibBuilder.loadTexts: trpzPortConfigPortNumber.setStatus('current')
trpzPortConfigPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 1, 1, 1, 2), TrpzPortMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzPortConfigPortMode.setStatus('current')
trpzPortConfigPoeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 1, 1, 1, 3), TrpzPortPoeMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzPortConfigPoeMode.setStatus('current')
trpzPortConfigTrunkMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 1, 1, 1, 4), TrpzPhysPortNumberOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzPortConfigTrunkMaster.setStatus('current')
trpzPortConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 2))
trpzPortCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 2, 1))
trpzPortGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 2, 2))
trpzPortCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 2, 1, 1)).setObjects(("TRAPEZE-NETWORKS-PORT-MIB", "trpzPortConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzPortCompliance = trpzPortCompliance.setStatus('current')
trpzPortConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 2, 2, 1)).setObjects(("TRAPEZE-NETWORKS-PORT-MIB", "trpzPortConfigPortMode"), ("TRAPEZE-NETWORKS-PORT-MIB", "trpzPortConfigPoeMode"), ("TRAPEZE-NETWORKS-PORT-MIB", "trpzPortConfigTrunkMaster"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzPortConfigGroup = trpzPortConfigGroup.setStatus('current')
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-PORT-MIB", TrpzPortPoeMode=TrpzPortPoeMode, trpzPortMib=trpzPortMib, trpzPortCompliance=trpzPortCompliance, trpzPortCompliances=trpzPortCompliances, trpzPortConfigPortMode=trpzPortConfigPortMode, trpzPortConfigGroup=trpzPortConfigGroup, trpzPortObjects=trpzPortObjects, TrpzPortMode=TrpzPortMode, trpzPortDataObjects=trpzPortDataObjects, trpzPortConfigEntry=trpzPortConfigEntry, trpzPortConformance=trpzPortConformance, trpzPortConfigPoeMode=trpzPortConfigPoeMode, trpzPortConfigPortNumber=trpzPortConfigPortNumber, PYSNMP_MODULE_ID=trpzPortMib, trpzPortConfigTrunkMaster=trpzPortConfigTrunkMaster, trpzPortConfigTable=trpzPortConfigTable, trpzPortGroups=trpzPortGroups)
