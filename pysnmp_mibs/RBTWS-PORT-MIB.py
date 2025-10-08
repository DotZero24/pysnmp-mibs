#
# PySNMP MIB module RBTWS-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cabletron/RBTWS-PORT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:05:50 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rbtwsMibs, = mibBuilder.importSymbols("RBTWS-ROOT-MIB", "rbtwsMibs")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbtwsPortMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6))
rbtwsPortMib.setRevisions(('2008-05-19 00:04', '2006-11-09 00:01', '2006-04-06 00:00',))
if mibBuilder.loadTexts: rbtwsPortMib.setLastUpdated('200805191722Z')
if mibBuilder.loadTexts: rbtwsPortMib.setOrganization('Enterasys Networks')
class RbtwsPhysPortNumber(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 1024)

class RbtwsPortMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("directAttachAP", 1), ("networkPort", 2), ("wired", 3))

class RbtwsPortPoeMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("poeEnable", 1), ("poeDisable", 2))

rbtwsPortObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1))
rbtwsPortDataObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 1))
rbtwsPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 1, 1), )
if mibBuilder.loadTexts: rbtwsPortConfigTable.setStatus('current')
rbtwsPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 1, 1, 1), ).setIndexNames((0, "RBTWS-PORT-MIB", "rbtwsPortConfigPortNumber"))
if mibBuilder.loadTexts: rbtwsPortConfigEntry.setStatus('current')
rbtwsPortConfigPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 1, 1, 1, 1), RbtwsPhysPortNumber())
if mibBuilder.loadTexts: rbtwsPortConfigPortNumber.setStatus('current')
rbtwsPortConfigPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 1, 1, 1, 2), RbtwsPortMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbtwsPortConfigPortMode.setStatus('current')
rbtwsPortConfigPoeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 1, 1, 1, 3), RbtwsPortPoeMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbtwsPortConfigPoeMode.setStatus('current')
rbtwsPortConfigTrunkMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 1, 1, 1, 4), RbtwsPhysPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbtwsPortConfigTrunkMaster.setStatus('current')
rbtwsPortConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 2))
rbtwsPortCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 2, 1))
rbtwsPortGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 2, 2))
rbtwsPortCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 2, 1, 1)).setObjects(("RBTWS-PORT-MIB", "rbtwsPortConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbtwsPortCompliance = rbtwsPortCompliance.setStatus('current')
rbtwsPortConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 2, 2, 1)).setObjects(("RBTWS-PORT-MIB", "rbtwsPortConfigPortMode"), ("RBTWS-PORT-MIB", "rbtwsPortConfigPoeMode"), ("RBTWS-PORT-MIB", "rbtwsPortConfigTrunkMaster"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbtwsPortConfigGroup = rbtwsPortConfigGroup.setStatus('current')
mibBuilder.exportSymbols("RBTWS-PORT-MIB", RbtwsPhysPortNumber=RbtwsPhysPortNumber, rbtwsPortConfigPortNumber=rbtwsPortConfigPortNumber, rbtwsPortConfigPoeMode=rbtwsPortConfigPoeMode, rbtwsPortMib=rbtwsPortMib, rbtwsPortConfigTrunkMaster=rbtwsPortConfigTrunkMaster, RbtwsPortPoeMode=RbtwsPortPoeMode, rbtwsPortConformance=rbtwsPortConformance, rbtwsPortGroups=rbtwsPortGroups, rbtwsPortConfigEntry=rbtwsPortConfigEntry, rbtwsPortDataObjects=rbtwsPortDataObjects, rbtwsPortCompliance=rbtwsPortCompliance, PYSNMP_MODULE_ID=rbtwsPortMib, rbtwsPortObjects=rbtwsPortObjects, rbtwsPortConfigTable=rbtwsPortConfigTable, RbtwsPortMode=RbtwsPortMode, rbtwsPortConfigGroup=rbtwsPortConfigGroup, rbtwsPortConfigPortMode=rbtwsPortConfigPortMode, rbtwsPortCompliances=rbtwsPortCompliances)
