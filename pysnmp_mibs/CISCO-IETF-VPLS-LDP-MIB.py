#
# PySNMP MIB module CISCO-IETF-VPLS-LDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-IETF-VPLS-LDP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:13:00 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cvplsConfigIndex, cvplsPwBindIndex = mibBuilder.importSymbols("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex", "cvplsPwBindIndex")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
VPNId, = mibBuilder.importSymbols("VPN-TC-STD-MIB", "VPNId")
cvplsLdpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 141))
cvplsLdpMIB.setRevisions(('2007-11-22 12:00',))
if mibBuilder.loadTexts: cvplsLdpMIB.setLastUpdated('200711221200Z')
if mibBuilder.loadTexts: cvplsLdpMIB.setOrganization('Cisco Systems, Inc.')
cvplsLdpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 141, 1))
cvplsLdpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 141, 2))
cvplsLdpConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 1), )
if mibBuilder.loadTexts: cvplsLdpConfigTable.setStatus('current')
cvplsLdpConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 1, 1), ).setIndexNames((0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"))
if mibBuilder.loadTexts: cvplsLdpConfigEntry.setStatus('current')
cvplsLdpConfigMacAddrWithdraw = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvplsLdpConfigMacAddrWithdraw.setStatus('current')
cvplsLdpPwBindTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 2), )
if mibBuilder.loadTexts: cvplsLdpPwBindTable.setStatus('current')
cvplsLdpPwBindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 2, 1), ).setIndexNames((0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"), (0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsPwBindIndex"))
if mibBuilder.loadTexts: cvplsLdpPwBindEntry.setStatus('current')
cvplsLdpPwBindMacAddressLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvplsLdpPwBindMacAddressLimit.setStatus('current')
cvplsLdpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 1))
cvplsLdpModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 1, 1)).setObjects(("CISCO-IETF-VPLS-LDP-MIB", "cvplsLdpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvplsLdpModuleFullCompliance = cvplsLdpModuleFullCompliance.setStatus('current')
cvplsLdpModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 1, 2)).setObjects(("CISCO-IETF-VPLS-LDP-MIB", "cvplsLdpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvplsLdpModuleReadOnlyCompliance = cvplsLdpModuleReadOnlyCompliance.setStatus('current')
cvplsLdpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 2))
cvplsLdpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 2, 1)).setObjects(("CISCO-IETF-VPLS-LDP-MIB", "cvplsLdpConfigMacAddrWithdraw"), ("CISCO-IETF-VPLS-LDP-MIB", "cvplsLdpPwBindMacAddressLimit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvplsLdpGroup = cvplsLdpGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-VPLS-LDP-MIB", cvplsLdpConfigEntry=cvplsLdpConfigEntry, cvplsLdpPwBindEntry=cvplsLdpPwBindEntry, cvplsLdpGroups=cvplsLdpGroups, cvplsLdpGroup=cvplsLdpGroup, cvplsLdpObjects=cvplsLdpObjects, cvplsLdpMIB=cvplsLdpMIB, cvplsLdpPwBindTable=cvplsLdpPwBindTable, cvplsLdpConformance=cvplsLdpConformance, cvplsLdpConfigTable=cvplsLdpConfigTable, cvplsLdpPwBindMacAddressLimit=cvplsLdpPwBindMacAddressLimit, PYSNMP_MODULE_ID=cvplsLdpMIB, cvplsLdpModuleFullCompliance=cvplsLdpModuleFullCompliance, cvplsLdpModuleReadOnlyCompliance=cvplsLdpModuleReadOnlyCompliance, cvplsLdpConfigMacAddrWithdraw=cvplsLdpConfigMacAddrWithdraw, cvplsLdpCompliances=cvplsLdpCompliances)
