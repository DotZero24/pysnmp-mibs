#
# PySNMP MIB module HP-ICF-DOS-FILTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HP-ICF-DOS-FILTER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:09:24 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("HP-ICF-DOS-FILTER-MIB", hpicfDosFilterMib=hpicfDosFilterMib, hpicfDosFilterGroups=hpicfDosFilterGroups, hpicfDosFilterObjects=hpicfDosFilterObjects, hpicfDosFilterGroup=hpicfDosFilterGroup, hpicfDosFilterCompliance=hpicfDosFilterCompliance, hpicfDosFilterCompliances=hpicfDosFilterCompliances, hpicfDosFilterConformance=hpicfDosFilterConformance, hpicfDosFilterConfig=hpicfDosFilterConfig, PYSNMP_MODULE_ID=hpicfDosFilterMib)
