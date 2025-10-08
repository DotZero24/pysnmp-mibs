#
# PySNMP MIB module MX-PPPOA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/media5/MX-PPPOA-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:39:22 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mediatrixConfig, = mibBuilder.importSymbols("MX-SMI", "mediatrixConfig")
MxEnableState, = mibBuilder.importSymbols("MX-TC", "MxEnableState")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pppoaMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4935, 15, 350))
pppoaMIB.setRevisions(('2006-03-06 00:00', '2005-04-12 00:00',))
if mibBuilder.loadTexts: pppoaMIB.setLastUpdated('200603060000Z')
if mibBuilder.loadTexts: pppoaMIB.setOrganization('Mediatrix Telecom, Inc.')
pppoaMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 350, 1))
pppoaConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 350, 5))
pppoaEnable = MibScalar((1, 3, 6, 1, 4, 1, 4935, 15, 350, 1, 50), MxEnableState().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppoaEnable.setStatus('current')
pppoaCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 350, 5, 1))
pppoaComplVer1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4935, 15, 350, 5, 1, 1)).setObjects(("MX-PPPOA-MIB", "pppoaConnectionCustomizationVer1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pppoaComplVer1 = pppoaComplVer1.setStatus('current')
pppoaGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 350, 5, 5))
pppoaConnectionCustomizationVer1 = ObjectGroup((1, 3, 6, 1, 4, 1, 4935, 15, 350, 5, 5, 10)).setObjects(("MX-PPPOA-MIB", "pppoaEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pppoaConnectionCustomizationVer1 = pppoaConnectionCustomizationVer1.setStatus('current')
mibBuilder.exportSymbols("MX-PPPOA-MIB", pppoaComplVer1=pppoaComplVer1, pppoaCompliances=pppoaCompliances, pppoaMIBObjects=pppoaMIBObjects, pppoaGroups=pppoaGroups, pppoaMIB=pppoaMIB, pppoaEnable=pppoaEnable, pppoaConnectionCustomizationVer1=pppoaConnectionCustomizationVer1, pppoaConformance=pppoaConformance, PYSNMP_MODULE_ID=pppoaMIB)
