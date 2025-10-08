#
# PySNMP MIB module RBTWS-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cabletron/RBTWS-PORT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:13:38 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rbtwsMibs, = mibBuilder.importSymbols("RBTWS-ROOT-MIB", "rbtwsMibs")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
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
mibBuilder.exportSymbols("RBTWS-PORT-MIB", rbtwsPortObjects=rbtwsPortObjects, rbtwsPortDataObjects=rbtwsPortDataObjects, rbtwsPortGroups=rbtwsPortGroups, rbtwsPortConfigPoeMode=rbtwsPortConfigPoeMode, rbtwsPortConformance=rbtwsPortConformance, RbtwsPortMode=RbtwsPortMode, rbtwsPortMib=rbtwsPortMib, rbtwsPortConfigGroup=rbtwsPortConfigGroup, rbtwsPortCompliance=rbtwsPortCompliance, rbtwsPortConfigPortNumber=rbtwsPortConfigPortNumber, PYSNMP_MODULE_ID=rbtwsPortMib, RbtwsPhysPortNumber=RbtwsPhysPortNumber, rbtwsPortConfigPortMode=rbtwsPortConfigPortMode, RbtwsPortPoeMode=RbtwsPortPoeMode, rbtwsPortConfigEntry=rbtwsPortConfigEntry, rbtwsPortConfigTrunkMaster=rbtwsPortConfigTrunkMaster, rbtwsPortConfigTable=rbtwsPortConfigTable, rbtwsPortCompliances=rbtwsPortCompliances)
