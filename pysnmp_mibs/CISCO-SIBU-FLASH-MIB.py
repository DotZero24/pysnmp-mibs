#
# PySNMP MIB module CISCO-SIBU-FLASH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-SIBU-FLASH-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:15:57 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSibuFlashMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 45))
ciscoSibuFlashMIB.setRevisions(('1998-10-23 00:00',))
if mibBuilder.loadTexts: ciscoSibuFlashMIB.setLastUpdated('9810230000Z')
if mibBuilder.loadTexts: ciscoSibuFlashMIB.setOrganization('Cisco Systems Inc.')
ciscoSibuFlashMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 45, 1))
csfUpgrade = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1))
csfUpgradeFirmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: csfUpgradeFirmwareVersion.setStatus('current')
csfUpgradeFlashSize = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('kbytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: csfUpgradeFlashSize.setStatus('current')
csfUpgradeTFTPServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 3), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csfUpgradeTFTPServerAddress.setStatus('current')
csfUpgradeTFTPLoadFilename = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csfUpgradeTFTPLoadFilename.setStatus('current')
csfUpgradeTFTPInitiate = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("upgrade", 1), ("noUpgrade", 2))).clone('noUpgrade')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csfUpgradeTFTPInitiate.setStatus('current')
csfUpgradeFlashMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permanent", 1), ("temporary", 2))).clone('permanent')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csfUpgradeFlashMode.setStatus('current')
csfUpgradeFirmwareStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("inProgress", 2), ("succeeded", 3), ("failed", 4))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: csfUpgradeFirmwareStatus.setStatus('current')
ciscoSibuFlashMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 45, 2))
ciscoSibuFlashMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 45, 2, 0))
ciscoSibuFlashMIBComformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 45, 3))
ciscoSibuFlashMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 45, 3, 1))
ciscoSibuFlashMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 45, 3, 2))
ciscoSibuFlashCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 45, 3, 1, 1)).setObjects(("CISCO-SIBU-FLASH-MIB", "ciscoSibuFlashMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSibuFlashCompliance = ciscoSibuFlashCompliance.setStatus('current')
ciscoSibuFlashMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 45, 3, 2, 1)).setObjects(("CISCO-SIBU-FLASH-MIB", "csfUpgradeFirmwareVersion"), ("CISCO-SIBU-FLASH-MIB", "csfUpgradeFlashSize"), ("CISCO-SIBU-FLASH-MIB", "csfUpgradeTFTPServerAddress"), ("CISCO-SIBU-FLASH-MIB", "csfUpgradeTFTPLoadFilename"), ("CISCO-SIBU-FLASH-MIB", "csfUpgradeTFTPInitiate"), ("CISCO-SIBU-FLASH-MIB", "csfUpgradeFlashMode"), ("CISCO-SIBU-FLASH-MIB", "csfUpgradeFirmwareStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSibuFlashMIBGroup = ciscoSibuFlashMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SIBU-FLASH-MIB", csfUpgradeTFTPServerAddress=csfUpgradeTFTPServerAddress, csfUpgradeTFTPLoadFilename=csfUpgradeTFTPLoadFilename, ciscoSibuFlashMIBNotificationsPrefix=ciscoSibuFlashMIBNotificationsPrefix, ciscoSibuFlashMIBGroup=ciscoSibuFlashMIBGroup, csfUpgrade=csfUpgrade, csfUpgradeFlashMode=csfUpgradeFlashMode, csfUpgradeFirmwareStatus=csfUpgradeFirmwareStatus, ciscoSibuFlashMIBNotifications=ciscoSibuFlashMIBNotifications, ciscoSibuFlashMIBCompliances=ciscoSibuFlashMIBCompliances, ciscoSibuFlashMIBComformance=ciscoSibuFlashMIBComformance, ciscoSibuFlashCompliance=ciscoSibuFlashCompliance, csfUpgradeFirmwareVersion=csfUpgradeFirmwareVersion, csfUpgradeTFTPInitiate=csfUpgradeTFTPInitiate, ciscoSibuFlashMIBGroups=ciscoSibuFlashMIBGroups, csfUpgradeFlashSize=csfUpgradeFlashSize, PYSNMP_MODULE_ID=ciscoSibuFlashMIB, ciscoSibuFlashMIB=ciscoSibuFlashMIB, ciscoSibuFlashMIBObjects=ciscoSibuFlashMIBObjects)
