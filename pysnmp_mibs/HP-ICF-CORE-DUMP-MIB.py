#
# PySNMP MIB module HP-ICF-CORE-DUMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HP-ICF-CORE-DUMP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:34 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpicfCommon, = mibBuilder.importSymbols("HP-ICF-OID", "hpicfCommon")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpicfCoreDumpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14))
hpicfCoreDumpMIB.setRevisions(('2010-06-13 00:00',))
if mibBuilder.loadTexts: hpicfCoreDumpMIB.setLastUpdated('201006130000Z')
if mibBuilder.loadTexts: hpicfCoreDumpMIB.setOrganization('Hp Networking')
hpicfCoreDumpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14, 1))
hpicfCoreDumpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14, 2))
hpicfCoreDumpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14, 1, 1))
hpicfCoreDumpTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14, 1, 1, 1), )
if mibBuilder.loadTexts: hpicfCoreDumpTable.setStatus('current')
hpicfCoreDumpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14, 1, 1, 1, 1), ).setIndexNames((0, "HP-ICF-CORE-DUMP-MIB", "hpicfCoreDumpModule"))
if mibBuilder.loadTexts: hpicfCoreDumpEntry.setStatus('current')
hpicfCoreDumpModule = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hpicfCoreDumpModule.setStatus('current')
hpicfCoreDumpMmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfCoreDumpMmStatus.setStatus('current')
hpicfCoreDumpImStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfCoreDumpImStatus.setStatus('current')
hpicfCoreDumpTftpServerAddressType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14, 1, 1, 2), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfCoreDumpTftpServerAddressType.setStatus('current')
hpicfCoreDumpTftpServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14, 1, 1, 3), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfCoreDumpTftpServerAddress.setStatus('current')
hpicfCoreDumpConfigGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14, 2, 1))
hpicfCoreDumpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14, 2, 2))
hpicfCoreDumpConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14, 2, 1, 1)).setObjects(("HP-ICF-CORE-DUMP-MIB", "hpicfCoreDumpMmStatus"), ("HP-ICF-CORE-DUMP-MIB", "hpicfCoreDumpImStatus"), ("HP-ICF-CORE-DUMP-MIB", "hpicfCoreDumpTftpServerAddress"), ("HP-ICF-CORE-DUMP-MIB", "hpicfCoreDumpTftpServerAddressType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfCoreDumpConfigGroup = hpicfCoreDumpConfigGroup.setStatus('current')
hpicfCoreDumpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14, 2, 2, 1)).setObjects(("HP-ICF-CORE-DUMP-MIB", "hpicfCoreDumpConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfCoreDumpCompliance = hpicfCoreDumpCompliance.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-CORE-DUMP-MIB", hpicfCoreDumpConfig=hpicfCoreDumpConfig, PYSNMP_MODULE_ID=hpicfCoreDumpMIB, hpicfCoreDumpConformance=hpicfCoreDumpConformance, hpicfCoreDumpMmStatus=hpicfCoreDumpMmStatus, hpicfCoreDumpCompliance=hpicfCoreDumpCompliance, hpicfCoreDumpMIB=hpicfCoreDumpMIB, hpicfCoreDumpEntry=hpicfCoreDumpEntry, hpicfCoreDumpModule=hpicfCoreDumpModule, hpicfCoreDumpTftpServerAddressType=hpicfCoreDumpTftpServerAddressType, hpicfCoreDumpConfigGroups=hpicfCoreDumpConfigGroups, hpicfCoreDumpTftpServerAddress=hpicfCoreDumpTftpServerAddress, hpicfCoreDumpCompliances=hpicfCoreDumpCompliances, hpicfCoreDumpObjects=hpicfCoreDumpObjects, hpicfCoreDumpConfigGroup=hpicfCoreDumpConfigGroup, hpicfCoreDumpImStatus=hpicfCoreDumpImStatus, hpicfCoreDumpTable=hpicfCoreDumpTable)
