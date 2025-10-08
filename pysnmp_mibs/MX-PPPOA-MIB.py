#
# PySNMP MIB module MX-PPPOA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/media5/MX-PPPOA-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:05:55 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
mediatrixConfig, = mibBuilder.importSymbols("MX-SMI", "mediatrixConfig")
MxEnableState, = mibBuilder.importSymbols("MX-TC", "MxEnableState")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("MX-PPPOA-MIB", pppoaEnable=pppoaEnable, pppoaMIB=pppoaMIB, pppoaMIBObjects=pppoaMIBObjects, PYSNMP_MODULE_ID=pppoaMIB, pppoaConformance=pppoaConformance, pppoaConnectionCustomizationVer1=pppoaConnectionCustomizationVer1, pppoaGroups=pppoaGroups, pppoaComplVer1=pppoaComplVer1, pppoaCompliances=pppoaCompliances)
