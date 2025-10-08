#
# PySNMP MIB module HP-ICF-MIN-KEY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HP-ICF-MIN-KEY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:09:30 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("HP-ICF-MIN-KEY-MIB", hpicfMinKeyGroups=hpicfMinKeyGroups, hpicfMinKeyCompliance1=hpicfMinKeyCompliance1, hpicfMinKeyConfigGroup=hpicfMinKeyConfigGroup, hpicfMinKeyType=hpicfMinKeyType, PYSNMP_MODULE_ID=hpicfMinKeyMIB, hpicfMinKeyMIB=hpicfMinKeyMIB, hpicfMinKeyConformance=hpicfMinKeyConformance, hpicfMinKeyEntry=hpicfMinKeyEntry, hpicfMinKeyRowStatus=hpicfMinKeyRowStatus, hpicfMinKeyTable=hpicfMinKeyTable, hpicfMinKeyObjects=hpicfMinKeyObjects, hpicfMinKeySize=hpicfMinKeySize, hpicfMinKeyCompliances=hpicfMinKeyCompliances, hpicfMinKeyConfigObjects=hpicfMinKeyConfigObjects)
