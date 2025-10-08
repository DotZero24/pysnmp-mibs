#
# PySNMP MIB module INFINERA-TP-PXMINTERFACE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-TP-PXMINTERFACE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:02 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
InfnPxmIntfProtocolType, = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnPxmIntfProtocolType")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pxmInterfaceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 73))
pxmInterfaceMIB.setRevisions(('2016-05-20 00:00',))
if mibBuilder.loadTexts: pxmInterfaceMIB.setLastUpdated('201605200000Z')
if mibBuilder.loadTexts: pxmInterfaceMIB.setOrganization('Infinera')
pxmInterfaceConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 73, 3))
pxmInterfaceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 73, 3, 1))
pxmInterfaceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 73, 3, 2))
pxmInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 73, 1), )
if mibBuilder.loadTexts: pxmInterfaceTable.setStatus('current')
pxmInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 73, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pxmInterfaceEntry.setStatus('current')
pxmInterfaceProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 73, 1, 1, 1), InfnPxmIntfProtocolType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmInterfaceProtocolType.setStatus('current')
pxmInterfaceMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 73, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmInterfaceMacAddress.setStatus('current')
pxmInterfaceCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 73, 3, 1, 1)).setObjects(("INFINERA-TP-PXMINTERFACE-MIB", "pxmInterfaceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pxmInterfaceCompliance = pxmInterfaceCompliance.setStatus('current')
pxmInterfaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 73, 3, 2, 1)).setObjects(("INFINERA-TP-PXMINTERFACE-MIB", "pxmInterfaceProtocolType"), ("INFINERA-TP-PXMINTERFACE-MIB", "pxmInterfaceMacAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pxmInterfaceGroup = pxmInterfaceGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-TP-PXMINTERFACE-MIB", pxmInterfaceCompliance=pxmInterfaceCompliance, PYSNMP_MODULE_ID=pxmInterfaceMIB, pxmInterfaceConformance=pxmInterfaceConformance, pxmInterfaceMacAddress=pxmInterfaceMacAddress, pxmInterfaceEntry=pxmInterfaceEntry, pxmInterfaceTable=pxmInterfaceTable, pxmInterfaceMIB=pxmInterfaceMIB, pxmInterfaceGroup=pxmInterfaceGroup, pxmInterfaceCompliances=pxmInterfaceCompliances, pxmInterfaceGroups=pxmInterfaceGroups, pxmInterfaceProtocolType=pxmInterfaceProtocolType)
