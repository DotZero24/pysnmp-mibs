#
# PySNMP MIB module HP-ICF-DOS-FILTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HP-ICF-DOS-FILTER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:11 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpicfDosFilterMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60))
hpicfDosFilterMib.setRevisions(('2009-04-03 10:00',))
if mibBuilder.loadTexts: hpicfDosFilterMib.setLastUpdated('200904031000Z')
if mibBuilder.loadTexts: hpicfDosFilterMib.setOrganization('HP Networking')
hpicfDosFilterObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60, 1))
hpicfDosFilterConfig = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDosFilterConfig.setStatus('current')
hpicfDosFilterConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60, 2))
hpicfDosFilterCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60, 2, 1))
hpicfDosFilterGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60, 2, 2))
hpicfDosFilterCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60, 2, 1, 1)).setObjects(("HP-ICF-DOS-FILTER-MIB", "hpicfDosFilterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDosFilterCompliance = hpicfDosFilterCompliance.setStatus('current')
hpicfDosFilterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60, 2, 2, 1)).setObjects(("HP-ICF-DOS-FILTER-MIB", "hpicfDosFilterConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDosFilterGroup = hpicfDosFilterGroup.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-DOS-FILTER-MIB", hpicfDosFilterGroup=hpicfDosFilterGroup, hpicfDosFilterConfig=hpicfDosFilterConfig, hpicfDosFilterCompliance=hpicfDosFilterCompliance, hpicfDosFilterObjects=hpicfDosFilterObjects, hpicfDosFilterConformance=hpicfDosFilterConformance, PYSNMP_MODULE_ID=hpicfDosFilterMib, hpicfDosFilterCompliances=hpicfDosFilterCompliances, hpicfDosFilterGroups=hpicfDosFilterGroups, hpicfDosFilterMib=hpicfDosFilterMib)
