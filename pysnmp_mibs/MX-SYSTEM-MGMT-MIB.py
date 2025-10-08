#
# PySNMP MIB module MX-SYSTEM-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/media5/MX-SYSTEM-MGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:39:24 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mediatrixMgmt, = mibBuilder.importSymbols("MX-SMI", "mediatrixMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("MX-SYSTEM-MGMT-MIB", sysMgmtGroups=sysMgmtGroups, sysSoftwareVersion=sysSoftwareVersion, sysSerialNumber=sysSerialNumber, sysMgmtGroupVer1=sysMgmtGroupVer1, sysMacAddress=sysMacAddress, sysMibVersion=sysMibVersion, sysMgmtMIBObjects=sysMgmtMIBObjects, sysMgmtMIB=sysMgmtMIB, sysMgmtConformance=sysMgmtConformance, PYSNMP_MODULE_ID=sysMgmtMIB, sysMgmtCompliances=sysMgmtCompliances, sysHardwareVersion=sysHardwareVersion, sysMgmtComplVer1=sysMgmtComplVer1)
