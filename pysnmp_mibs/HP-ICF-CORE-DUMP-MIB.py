#
# PySNMP MIB module HP-ICF-CORE-DUMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HP-ICF-CORE-DUMP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:10:05 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpicfCommon, = mibBuilder.importSymbols("HP-ICF-OID", "hpicfCommon")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("HP-ICF-CORE-DUMP-MIB", hpicfCoreDumpConfigGroup=hpicfCoreDumpConfigGroup, PYSNMP_MODULE_ID=hpicfCoreDumpMIB, hpicfCoreDumpConformance=hpicfCoreDumpConformance, hpicfCoreDumpEntry=hpicfCoreDumpEntry, hpicfCoreDumpImStatus=hpicfCoreDumpImStatus, hpicfCoreDumpConfigGroups=hpicfCoreDumpConfigGroups, hpicfCoreDumpTftpServerAddressType=hpicfCoreDumpTftpServerAddressType, hpicfCoreDumpCompliances=hpicfCoreDumpCompliances, hpicfCoreDumpMmStatus=hpicfCoreDumpMmStatus, hpicfCoreDumpObjects=hpicfCoreDumpObjects, hpicfCoreDumpTable=hpicfCoreDumpTable, hpicfCoreDumpConfig=hpicfCoreDumpConfig, hpicfCoreDumpModule=hpicfCoreDumpModule, hpicfCoreDumpMIB=hpicfCoreDumpMIB, hpicfCoreDumpTftpServerAddress=hpicfCoreDumpTftpServerAddress, hpicfCoreDumpCompliance=hpicfCoreDumpCompliance)
