#
# PySNMP MIB module WESTERMO-DDM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/westermo/WESTERMO-DDM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:54 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
common, = mibBuilder.importSymbols("WESTERMO-OID-MIB", "common")
ddmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 16177, 2, 2))
ddmMIB.setRevisions(('2017-12-05 00:00',))
if mibBuilder.loadTexts: ddmMIB.setLastUpdated('201712050000Z')
if mibBuilder.loadTexts: ddmMIB.setOrganization('Westermo Teleindustri AB')
ddmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 16177, 2, 2, 1))
ddmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 16177, 2, 2, 2))
ddmPortTable = MibTable((1, 3, 6, 1, 4, 1, 16177, 2, 2, 1, 1), )
if mibBuilder.loadTexts: ddmPortTable.setStatus('current')
ddmPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 16177, 2, 2, 1, 1, 1), ).setIndexNames((0, "WESTERMO-DDM-MIB", "ddmPortIfIndex"))
if mibBuilder.loadTexts: ddmPortEntry.setStatus('current')
ddmPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 16177, 2, 2, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: ddmPortIfIndex.setStatus('current')
ddmPortIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 16177, 2, 2, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddmPortIfName.setStatus('current')
ddmPortVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 16177, 2, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 6550))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddmPortVoltage.setStatus('current')
ddmPortTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 16177, 2, 2, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-128, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddmPortTemperature.setStatus('current')
ddmPortBiasCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 16177, 2, 2, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 131))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddmPortBiasCurrent.setStatus('current')
ddmPortTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 16177, 2, 2, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-4000, 820))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddmPortTxPower.setStatus('current')
ddmPortRxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 16177, 2, 2, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-4000, 820))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddmPortRxPower.setStatus('current')
ddmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 16177, 2, 2, 2, 1))
ddmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 16177, 2, 2, 2, 2))
ddmPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 16177, 2, 2, 2, 1, 1)).setObjects(("WESTERMO-DDM-MIB", "ddmPortIfName"), ("WESTERMO-DDM-MIB", "ddmPortVoltage"), ("WESTERMO-DDM-MIB", "ddmPortTemperature"), ("WESTERMO-DDM-MIB", "ddmPortBiasCurrent"), ("WESTERMO-DDM-MIB", "ddmPortTxPower"), ("WESTERMO-DDM-MIB", "ddmPortRxPower"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ddmPortGroup = ddmPortGroup.setStatus('current')
ddmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 16177, 2, 2, 2, 2, 1)).setObjects(("WESTERMO-DDM-MIB", "ddmPortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ddmCompliance = ddmCompliance.setStatus('current')
mibBuilder.exportSymbols("WESTERMO-DDM-MIB", ddmPortIfIndex=ddmPortIfIndex, ddmPortBiasCurrent=ddmPortBiasCurrent, ddmMIB=ddmMIB, ddmGroups=ddmGroups, ddmPortIfName=ddmPortIfName, ddmPortGroup=ddmPortGroup, ddmPortVoltage=ddmPortVoltage, PYSNMP_MODULE_ID=ddmMIB, ddmPortTable=ddmPortTable, ddmPortRxPower=ddmPortRxPower, ddmPortEntry=ddmPortEntry, ddmCompliances=ddmCompliances, ddmConformance=ddmConformance, ddmCompliance=ddmCompliance, ddmObjects=ddmObjects, ddmPortTxPower=ddmPortTxPower, ddmPortTemperature=ddmPortTemperature)
