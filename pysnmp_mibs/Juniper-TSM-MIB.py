#
# PySNMP MIB module Juniper-TSM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/junose/Juniper-TSM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:23:06 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniIfType, = mibBuilder.importSymbols("Juniper-UNI-IF-MIB", "JuniIfType")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
juniTsmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72))
juniTsmMIB.setRevisions(('2005-05-23 14:37', '2005-04-27 22:57', '2003-10-23 20:45',))
if mibBuilder.loadTexts: juniTsmMIB.setLastUpdated('200505231437Z')
if mibBuilder.loadTexts: juniTsmMIB.setOrganization('Juniper Networks, Inc.')
class JuniTsmLocationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("slotPort", 1), ("slotAdapterPort", 2), ("adapterPort", 3))

class JuniTsmLocationValue(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 16)

juniTsmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1))
juniTsmData = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1))
juniTsmLocationType = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 1), JuniTsmLocationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTsmLocationType.setStatus('current')
juniTsmPortTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 2), )
if mibBuilder.loadTexts: juniTsmPortTable.setStatus('current')
juniTsmPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 2, 1), ).setIndexNames((0, "Juniper-TSM-MIB", "juniTsmPortLocation"))
if mibBuilder.loadTexts: juniTsmPortEntry.setStatus('current')
juniTsmPortLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 2, 1, 1), JuniTsmLocationValue())
if mibBuilder.loadTexts: juniTsmPortLocation.setStatus('current')
juniTsmPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("generalPurposeStatic", 1), ("generalPurposeDynamic", 2), ("securityStatic", 3), ("securityDynamic", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTsmPortType.setStatus('current')
juniTsmPortHwPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTsmPortHwPresent.setStatus('current')
juniTsmPortAvailableInterfaces = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTsmPortAvailableInterfaces.setStatus('current')
juniTsmPortProvisionedInterfaces = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 16000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniTsmPortProvisionedInterfaces.setStatus('current')
juniTsmAppRegistryTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 3), )
if mibBuilder.loadTexts: juniTsmAppRegistryTable.setStatus('current')
juniTsmAppRegistryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 3, 1), ).setIndexNames((0, "Juniper-TSM-MIB", "juniTsmAppRegistryIndex"))
if mibBuilder.loadTexts: juniTsmAppRegistryEntry.setStatus('current')
juniTsmAppRegistryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: juniTsmAppRegistryIndex.setStatus('current')
juniTsmAppRegistryIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 3, 1, 2), JuniIfType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTsmAppRegistryIfType.setStatus('current')
juniTsmAppRegistryName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTsmAppRegistryName.setStatus('current')
juniTsmAppRegistryInterfaceLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTsmAppRegistryInterfaceLimit.setStatus('current')
juniTsmApplicationTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 4), )
if mibBuilder.loadTexts: juniTsmApplicationTable.setStatus('current')
juniTsmApplicationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 4, 1), ).setIndexNames((0, "Juniper-TSM-MIB", "juniTsmPortLocation"), (0, "Juniper-TSM-MIB", "juniTsmAppRegistryIndex"))
if mibBuilder.loadTexts: juniTsmApplicationEntry.setStatus('current')
juniTsmApplicationMaxInterfaces = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTsmApplicationMaxInterfaces.setStatus('current')
juniTsmApplicationActiveInterfaces = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 4, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTsmApplicationActiveInterfaces.setStatus('current')
juniTsmMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 4))
juniTsmMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 4, 1))
juniTsmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 4, 2))
juniTsmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 4, 1, 1)).setObjects(("Juniper-TSM-MIB", "juniTsmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniTsmCompliance = juniTsmCompliance.setStatus('current')
juniTsmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 4, 2, 1)).setObjects(("Juniper-TSM-MIB", "juniTsmLocationType"), ("Juniper-TSM-MIB", "juniTsmPortType"), ("Juniper-TSM-MIB", "juniTsmPortHwPresent"), ("Juniper-TSM-MIB", "juniTsmPortAvailableInterfaces"), ("Juniper-TSM-MIB", "juniTsmPortProvisionedInterfaces"), ("Juniper-TSM-MIB", "juniTsmAppRegistryIfType"), ("Juniper-TSM-MIB", "juniTsmAppRegistryName"), ("Juniper-TSM-MIB", "juniTsmAppRegistryInterfaceLimit"), ("Juniper-TSM-MIB", "juniTsmApplicationMaxInterfaces"), ("Juniper-TSM-MIB", "juniTsmApplicationActiveInterfaces"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniTsmGroup = juniTsmGroup.setStatus('current')
mibBuilder.exportSymbols("Juniper-TSM-MIB", juniTsmObjects=juniTsmObjects, juniTsmPortAvailableInterfaces=juniTsmPortAvailableInterfaces, juniTsmAppRegistryIfType=juniTsmAppRegistryIfType, juniTsmCompliance=juniTsmCompliance, juniTsmAppRegistryInterfaceLimit=juniTsmAppRegistryInterfaceLimit, JuniTsmLocationValue=JuniTsmLocationValue, juniTsmAppRegistryIndex=juniTsmAppRegistryIndex, juniTsmApplicationMaxInterfaces=juniTsmApplicationMaxInterfaces, juniTsmGroup=juniTsmGroup, juniTsmAppRegistryTable=juniTsmAppRegistryTable, PYSNMP_MODULE_ID=juniTsmMIB, juniTsmPortHwPresent=juniTsmPortHwPresent, juniTsmPortProvisionedInterfaces=juniTsmPortProvisionedInterfaces, juniTsmMIBConformance=juniTsmMIBConformance, juniTsmAppRegistryName=juniTsmAppRegistryName, juniTsmPortEntry=juniTsmPortEntry, juniTsmMIBCompliances=juniTsmMIBCompliances, JuniTsmLocationType=JuniTsmLocationType, juniTsmPortType=juniTsmPortType, juniTsmData=juniTsmData, juniTsmLocationType=juniTsmLocationType, juniTsmApplicationEntry=juniTsmApplicationEntry, juniTsmApplicationActiveInterfaces=juniTsmApplicationActiveInterfaces, juniTsmPortLocation=juniTsmPortLocation, juniTsmPortTable=juniTsmPortTable, juniTsmApplicationTable=juniTsmApplicationTable, juniTsmAppRegistryEntry=juniTsmAppRegistryEntry, juniTsmMIBGroups=juniTsmMIBGroups, juniTsmMIB=juniTsmMIB)
