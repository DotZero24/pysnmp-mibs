#
# PySNMP MIB module MX-SYSTEM-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/media5/MX-SYSTEM-MGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:05:58 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
mediatrixMgmt, = mibBuilder.importSymbols("MX-SMI", "mediatrixMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sysMgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4935, 10, 15))
sysMgmtMIB.setRevisions(('2010-03-01 00:00', '1901-08-29 00:00',))
if mibBuilder.loadTexts: sysMgmtMIB.setLastUpdated('201003010000Z')
if mibBuilder.loadTexts: sysMgmtMIB.setOrganization('Mediatrix Telecom')
sysMgmtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 10, 15, 1))
sysMgmtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 10, 15, 2))
sysMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 4935, 10, 15, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 50)).clone(' ')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysMacAddress.setStatus('current')
sysHardwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 4935, 10, 15, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255)).clone(' ')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHardwareVersion.setStatus('current')
sysSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 4935, 10, 15, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255)).clone(' ')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSoftwareVersion.setStatus('current')
sysMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 4935, 10, 15, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255)).clone(' ')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysMibVersion.setStatus('current')
sysSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 4935, 10, 15, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 25)).clone(' ')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSerialNumber.setStatus('current')
sysMgmtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 10, 15, 2, 1))
sysMgmtComplVer1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4935, 10, 15, 2, 1, 1)).setObjects(("MX-SYSTEM-MGMT-MIB", "sysMgmtGroupVer1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysMgmtComplVer1 = sysMgmtComplVer1.setStatus('current')
sysMgmtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 10, 15, 2, 2))
sysMgmtGroupVer1 = ObjectGroup((1, 3, 6, 1, 4, 1, 4935, 10, 15, 2, 2, 1)).setObjects(("MX-SYSTEM-MGMT-MIB", "sysMacAddress"), ("MX-SYSTEM-MGMT-MIB", "sysHardwareVersion"), ("MX-SYSTEM-MGMT-MIB", "sysSoftwareVersion"), ("MX-SYSTEM-MGMT-MIB", "sysMibVersion"), ("MX-SYSTEM-MGMT-MIB", "sysSerialNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysMgmtGroupVer1 = sysMgmtGroupVer1.setStatus('current')
mibBuilder.exportSymbols("MX-SYSTEM-MGMT-MIB", sysMgmtMIB=sysMgmtMIB, sysHardwareVersion=sysHardwareVersion, sysMgmtGroupVer1=sysMgmtGroupVer1, PYSNMP_MODULE_ID=sysMgmtMIB, sysSerialNumber=sysSerialNumber, sysMgmtGroups=sysMgmtGroups, sysMacAddress=sysMacAddress, sysMgmtMIBObjects=sysMgmtMIBObjects, sysSoftwareVersion=sysSoftwareVersion, sysMgmtConformance=sysMgmtConformance, sysMgmtComplVer1=sysMgmtComplVer1, sysMibVersion=sysMibVersion, sysMgmtCompliances=sysMgmtCompliances)
