#
# PySNMP MIB module MX-PPPOE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/media5/MX-PPPOE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:06:05 2025
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
pppoeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4935, 15, 105))
pppoeMIB.setRevisions(('1903-07-09 00:00',))
if mibBuilder.loadTexts: pppoeMIB.setLastUpdated('0307090000Z')
if mibBuilder.loadTexts: pppoeMIB.setOrganization('Mediatrix Telecom, Inc.')
pppoeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 105, 1))
pppoeConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 105, 5))
pppoeEnable = MibScalar((1, 3, 6, 1, 4, 1, 4935, 15, 105, 1, 5), MxEnableState().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppoeEnable.setStatus('current')
pppoeAcName = MibScalar((1, 3, 6, 1, 4, 1, 4935, 15, 105, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppoeAcName.setStatus('current')
pppoeServiceName = MibScalar((1, 3, 6, 1, 4, 1, 4935, 15, 105, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppoeServiceName.setStatus('current')
pppoeCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 105, 5, 1))
pppoeComplVer1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4935, 15, 105, 5, 1, 1)).setObjects(("MX-PPPOE-MIB", "pppoeConnectionCustomizationVer1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pppoeComplVer1 = pppoeComplVer1.setStatus('current')
pppoeGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 105, 5, 5))
pppoeConnectionCustomizationVer1 = ObjectGroup((1, 3, 6, 1, 4, 1, 4935, 15, 105, 5, 5, 10)).setObjects(("MX-PPPOE-MIB", "pppoeEnable"), ("MX-PPPOE-MIB", "pppoeAcName"), ("MX-PPPOE-MIB", "pppoeServiceName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pppoeConnectionCustomizationVer1 = pppoeConnectionCustomizationVer1.setStatus('current')
mibBuilder.exportSymbols("MX-PPPOE-MIB", pppoeServiceName=pppoeServiceName, pppoeComplVer1=pppoeComplVer1, PYSNMP_MODULE_ID=pppoeMIB, pppoeAcName=pppoeAcName, pppoeMIB=pppoeMIB, pppoeGroups=pppoeGroups, pppoeMIBObjects=pppoeMIBObjects, pppoeEnable=pppoeEnable, pppoeConnectionCustomizationVer1=pppoeConnectionCustomizationVer1, pppoeConformance=pppoeConformance, pppoeCompliances=pppoeCompliances)
