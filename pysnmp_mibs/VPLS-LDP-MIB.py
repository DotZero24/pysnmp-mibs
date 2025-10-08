#
# PySNMP MIB module VPLS-LDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/VPLS-LDP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:50:06 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
pwID, pwIndex = mibBuilder.importSymbols("PW-STD-MIB", "pwID", "pwIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
transmission, MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "transmission", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
vplsConfigName, vplsConfigIndex = mibBuilder.importSymbols("VPLS-GENERIC-MIB", "vplsConfigName", "vplsConfigIndex")
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
mibBuilder.exportSymbols("VPLS-LDP-MIB", vplsLdpModuleReadOnlyCompliance=vplsLdpModuleReadOnlyCompliance, vplsLdpNotificationGroup=vplsLdpNotificationGroup, vplsLdpPwBindMacAddressLimit=vplsLdpPwBindMacAddressLimit, vplsLdpConfigMacAddrWithdraw=vplsLdpConfigMacAddrWithdraw, vplsLdpCompliances=vplsLdpCompliances, vplsLdpGroup=vplsLdpGroup, vplsLdpObjects=vplsLdpObjects, vplsLdpNotifications=vplsLdpNotifications, vplsLdpMIB=vplsLdpMIB, vplsLdpConformance=vplsLdpConformance, PYSNMP_MODULE_ID=vplsLdpMIB, vplsLdpGroups=vplsLdpGroups, vplsLdpModuleFullCompliance=vplsLdpModuleFullCompliance, vplsLdpConfigTable=vplsLdpConfigTable, vplsLdpPwBindTable=vplsLdpPwBindTable, vplsLdpConfigEntry=vplsLdpConfigEntry, vplsLdpPwBindMacTableFull=vplsLdpPwBindMacTableFull, vplsLdpPwBindEntry=vplsLdpPwBindEntry)
