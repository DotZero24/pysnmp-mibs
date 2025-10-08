#
# PySNMP MIB module NTWS-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nortel/NTWS-PORT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:59:11 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NtwsPhysPortNumberOrZero, NtwsPhysPortNumber = mibBuilder.importSymbols("NTWS-BASIC-TC", "NtwsPhysPortNumberOrZero", "NtwsPhysPortNumber")
ntwsMibs, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsMibs")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
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
mibBuilder.exportSymbols("NTWS-PORT-MIB", ntwsPortConfigEntry=ntwsPortConfigEntry, ntwsPortConfigTrunkMaster=ntwsPortConfigTrunkMaster, ntwsPortGroups=ntwsPortGroups, ntwsPortMib=ntwsPortMib, PYSNMP_MODULE_ID=ntwsPortMib, NtwsPortPoeMode=NtwsPortPoeMode, ntwsPortConfigTable=ntwsPortConfigTable, ntwsPortObjects=ntwsPortObjects, ntwsPortConfigPortNumber=ntwsPortConfigPortNumber, ntwsPortConformance=ntwsPortConformance, ntwsPortConfigGroup=ntwsPortConfigGroup, ntwsPortConfigPoeMode=ntwsPortConfigPoeMode, ntwsPortCompliance=ntwsPortCompliance, ntwsPortCompliances=ntwsPortCompliances, ntwsPortConfigPortMode=ntwsPortConfigPortMode, NtwsPortMode=NtwsPortMode, ntwsPortDataObjects=ntwsPortDataObjects)
