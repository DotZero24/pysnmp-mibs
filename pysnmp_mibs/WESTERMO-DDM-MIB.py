#
# PySNMP MIB module WESTERMO-DDM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/westermo/WESTERMO-DDM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:11 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("WESTERMO-DDM-MIB", ddmMIB=ddmMIB, ddmPortBiasCurrent=ddmPortBiasCurrent, ddmPortEntry=ddmPortEntry, ddmPortIfName=ddmPortIfName, ddmPortTxPower=ddmPortTxPower, ddmCompliances=ddmCompliances, PYSNMP_MODULE_ID=ddmMIB, ddmPortRxPower=ddmPortRxPower, ddmPortIfIndex=ddmPortIfIndex, ddmPortVoltage=ddmPortVoltage, ddmPortTemperature=ddmPortTemperature, ddmGroups=ddmGroups, ddmPortGroup=ddmPortGroup, ddmConformance=ddmConformance, ddmObjects=ddmObjects, ddmCompliance=ddmCompliance, ddmPortTable=ddmPortTable)
