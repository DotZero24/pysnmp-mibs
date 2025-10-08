#
# PySNMP MIB module NTWS-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nortel/NTWS-PORT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:02:36 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NtwsPhysPortNumberOrZero, NtwsPhysPortNumber = mibBuilder.importSymbols("NTWS-BASIC-TC", "NtwsPhysPortNumberOrZero", "NtwsPhysPortNumber")
ntwsMibs, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsMibs")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntwsPortMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6))
ntwsPortMib.setRevisions(('2008-10-23 00:10', '2008-05-19 00:04', '2007-08-16 00:02', '2006-11-09 00:01', '2006-04-06 00:00',))
if mibBuilder.loadTexts: ntwsPortMib.setLastUpdated('200810230010Z')
if mibBuilder.loadTexts: ntwsPortMib.setOrganization('Nortel Networks')
class NtwsPortMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("directAttachAP", 1), ("networkPort", 2), ("wired", 3))

class NtwsPortPoeMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("poeEnable", 1), ("poeDisable", 2))

ntwsPortObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1))
ntwsPortDataObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 1))
ntwsPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 1, 1), )
if mibBuilder.loadTexts: ntwsPortConfigTable.setStatus('current')
ntwsPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 1, 1, 1), ).setIndexNames((0, "NTWS-PORT-MIB", "ntwsPortConfigPortNumber"))
if mibBuilder.loadTexts: ntwsPortConfigEntry.setStatus('current')
ntwsPortConfigPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 1, 1, 1, 1), NtwsPhysPortNumber())
if mibBuilder.loadTexts: ntwsPortConfigPortNumber.setStatus('current')
ntwsPortConfigPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 1, 1, 1, 2), NtwsPortMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsPortConfigPortMode.setStatus('current')
ntwsPortConfigPoeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 1, 1, 1, 3), NtwsPortPoeMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsPortConfigPoeMode.setStatus('current')
ntwsPortConfigTrunkMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 1, 1, 1, 4), NtwsPhysPortNumberOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsPortConfigTrunkMaster.setStatus('current')
ntwsPortConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 2))
ntwsPortCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 2, 1))
ntwsPortGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 2, 2))
ntwsPortCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 2, 1, 1)).setObjects(("NTWS-PORT-MIB", "ntwsPortConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsPortCompliance = ntwsPortCompliance.setStatus('current')
ntwsPortConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 2, 2, 1)).setObjects(("NTWS-PORT-MIB", "ntwsPortConfigPortMode"), ("NTWS-PORT-MIB", "ntwsPortConfigPoeMode"), ("NTWS-PORT-MIB", "ntwsPortConfigTrunkMaster"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsPortConfigGroup = ntwsPortConfigGroup.setStatus('current')
mibBuilder.exportSymbols("NTWS-PORT-MIB", ntwsPortDataObjects=ntwsPortDataObjects, ntwsPortGroups=ntwsPortGroups, ntwsPortObjects=ntwsPortObjects, ntwsPortConfigTrunkMaster=ntwsPortConfigTrunkMaster, NtwsPortPoeMode=NtwsPortPoeMode, ntwsPortConfigPortNumber=ntwsPortConfigPortNumber, ntwsPortConfigPortMode=ntwsPortConfigPortMode, ntwsPortConfigEntry=ntwsPortConfigEntry, ntwsPortCompliance=ntwsPortCompliance, ntwsPortConfigGroup=ntwsPortConfigGroup, NtwsPortMode=NtwsPortMode, PYSNMP_MODULE_ID=ntwsPortMib, ntwsPortConfigTable=ntwsPortConfigTable, ntwsPortCompliances=ntwsPortCompliances, ntwsPortMib=ntwsPortMib, ntwsPortConfigPoeMode=ntwsPortConfigPoeMode, ntwsPortConformance=ntwsPortConformance)
