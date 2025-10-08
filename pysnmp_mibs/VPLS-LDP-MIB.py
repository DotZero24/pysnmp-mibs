#
# PySNMP MIB module VPLS-LDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/VPLS-LDP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:39 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
pwID, pwIndex = mibBuilder.importSymbols("PW-STD-MIB", "pwID", "pwIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, transmission, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "transmission", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
vplsConfigIndex, vplsConfigName = mibBuilder.importSymbols("VPLS-GENERIC-MIB", "vplsConfigIndex", "vplsConfigName")
vplsLdpMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 275))
vplsLdpMIB.setRevisions(('2014-05-19 12:00',))
if mibBuilder.loadTexts: vplsLdpMIB.setLastUpdated('201405191200Z')
if mibBuilder.loadTexts: vplsLdpMIB.setOrganization('Layer 2 Virtual Private Networks (L2VPN) Working Group')
vplsLdpNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 275, 0))
vplsLdpObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 275, 1))
vplsLdpConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 275, 2))
vplsLdpConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 275, 1, 1), )
if mibBuilder.loadTexts: vplsLdpConfigTable.setStatus('current')
vplsLdpConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 275, 1, 1, 1), ).setIndexNames((0, "VPLS-GENERIC-MIB", "vplsConfigIndex"))
if mibBuilder.loadTexts: vplsLdpConfigEntry.setStatus('current')
vplsLdpConfigMacAddrWithdraw = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 275, 1, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vplsLdpConfigMacAddrWithdraw.setStatus('current')
vplsLdpPwBindTable = MibTable((1, 3, 6, 1, 2, 1, 10, 275, 1, 2), )
if mibBuilder.loadTexts: vplsLdpPwBindTable.setStatus('current')
vplsLdpPwBindEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 275, 1, 2, 1), ).setIndexNames((0, "VPLS-GENERIC-MIB", "vplsConfigIndex"), (0, "PW-STD-MIB", "pwIndex"))
if mibBuilder.loadTexts: vplsLdpPwBindEntry.setStatus('current')
vplsLdpPwBindMacAddressLimit = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 275, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vplsLdpPwBindMacAddressLimit.setStatus('current')
vplsLdpPwBindMacTableFull = NotificationType((1, 3, 6, 1, 2, 1, 10, 275, 0, 1)).setObjects(("VPLS-GENERIC-MIB", "vplsConfigName"), ("PW-STD-MIB", "pwID"))
if mibBuilder.loadTexts: vplsLdpPwBindMacTableFull.setStatus('current')
vplsLdpCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 275, 2, 1))
vplsLdpModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 275, 2, 1, 1)).setObjects(("VPLS-LDP-MIB", "vplsLdpGroup"), ("VPLS-LDP-MIB", "vplsLdpNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vplsLdpModuleFullCompliance = vplsLdpModuleFullCompliance.setStatus('current')
vplsLdpModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 275, 2, 1, 2)).setObjects(("VPLS-LDP-MIB", "vplsLdpGroup"), ("VPLS-LDP-MIB", "vplsLdpNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vplsLdpModuleReadOnlyCompliance = vplsLdpModuleReadOnlyCompliance.setStatus('current')
vplsLdpGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 275, 2, 2))
vplsLdpGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 275, 2, 2, 1)).setObjects(("VPLS-LDP-MIB", "vplsLdpConfigMacAddrWithdraw"), ("VPLS-LDP-MIB", "vplsLdpPwBindMacAddressLimit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vplsLdpGroup = vplsLdpGroup.setStatus('current')
vplsLdpNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 10, 275, 2, 2, 2)).setObjects(("VPLS-LDP-MIB", "vplsLdpPwBindMacTableFull"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vplsLdpNotificationGroup = vplsLdpNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("VPLS-LDP-MIB", vplsLdpPwBindMacAddressLimit=vplsLdpPwBindMacAddressLimit, vplsLdpPwBindMacTableFull=vplsLdpPwBindMacTableFull, vplsLdpGroups=vplsLdpGroups, vplsLdpMIB=vplsLdpMIB, vplsLdpConfigEntry=vplsLdpConfigEntry, PYSNMP_MODULE_ID=vplsLdpMIB, vplsLdpObjects=vplsLdpObjects, vplsLdpModuleFullCompliance=vplsLdpModuleFullCompliance, vplsLdpModuleReadOnlyCompliance=vplsLdpModuleReadOnlyCompliance, vplsLdpPwBindEntry=vplsLdpPwBindEntry, vplsLdpConfigMacAddrWithdraw=vplsLdpConfigMacAddrWithdraw, vplsLdpCompliances=vplsLdpCompliances, vplsLdpConfigTable=vplsLdpConfigTable, vplsLdpNotifications=vplsLdpNotifications, vplsLdpGroup=vplsLdpGroup, vplsLdpNotificationGroup=vplsLdpNotificationGroup, vplsLdpPwBindTable=vplsLdpPwBindTable, vplsLdpConformance=vplsLdpConformance)
