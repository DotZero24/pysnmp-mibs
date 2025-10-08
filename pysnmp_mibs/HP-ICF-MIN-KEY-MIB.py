#
# PySNMP MIB module HP-ICF-MIN-KEY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HP-ICF-MIN-KEY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
hpicfMinKeyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132))
hpicfMinKeyMIB.setRevisions(('2016-06-22 09:00',))
if mibBuilder.loadTexts: hpicfMinKeyMIB.setLastUpdated('201606220900Z')
if mibBuilder.loadTexts: hpicfMinKeyMIB.setOrganization('HP Networking')
hpicfMinKeyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 0))
hpicfMinKeyConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 1))
hpicfMinKeyConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 0, 1))
hpicfMinKeyTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 0, 1, 1), )
if mibBuilder.loadTexts: hpicfMinKeyTable.setStatus('current')
hpicfMinKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 0, 1, 1, 1), ).setIndexNames((0, "HP-ICF-MIN-KEY-MIB", "hpicfMinKeyType"))
if mibBuilder.loadTexts: hpicfMinKeyEntry.setStatus('current')
hpicfMinKeyType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 0, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("rsa", 1))))
if mibBuilder.loadTexts: hpicfMinKeyType.setStatus('current')
hpicfMinKeySize = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 0, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("minBit1024", 1), ("minBit2048", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfMinKeySize.setStatus('current')
hpicfMinKeyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 0, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfMinKeyRowStatus.setStatus('current')
hpicfMinKeyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 1, 1))
hpicfMinKeyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 1, 2))
hpicfMinKeyCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 1, 1, 1)).setObjects(("HP-ICF-MIN-KEY-MIB", "hpicfMinKeyConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMinKeyCompliance1 = hpicfMinKeyCompliance1.setStatus('current')
hpicfMinKeyConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 1, 2, 1)).setObjects(("HP-ICF-MIN-KEY-MIB", "hpicfMinKeySize"), ("HP-ICF-MIN-KEY-MIB", "hpicfMinKeyRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMinKeyConfigGroup = hpicfMinKeyConfigGroup.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-MIN-KEY-MIB", hpicfMinKeyMIB=hpicfMinKeyMIB, hpicfMinKeyConformance=hpicfMinKeyConformance, hpicfMinKeyGroups=hpicfMinKeyGroups, hpicfMinKeySize=hpicfMinKeySize, hpicfMinKeyCompliance1=hpicfMinKeyCompliance1, hpicfMinKeyObjects=hpicfMinKeyObjects, hpicfMinKeyTable=hpicfMinKeyTable, hpicfMinKeyConfigObjects=hpicfMinKeyConfigObjects, hpicfMinKeyRowStatus=hpicfMinKeyRowStatus, hpicfMinKeyConfigGroup=hpicfMinKeyConfigGroup, hpicfMinKeyEntry=hpicfMinKeyEntry, hpicfMinKeyType=hpicfMinKeyType, hpicfMinKeyCompliances=hpicfMinKeyCompliances, PYSNMP_MODULE_ID=hpicfMinKeyMIB)
