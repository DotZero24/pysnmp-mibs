#
# PySNMP MIB module CISCO-DS0BUNDLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-DS0BUNDLE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:13:24 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
TestAndIncr, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TestAndIncr", "RowStatus", "DisplayString", "TextualConvention")
ds0Bundle = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 32))
if mibBuilder.loadTexts: ds0Bundle.setLastUpdated('9805242010Z')
if mibBuilder.loadTexts: ds0Bundle.setOrganization('Cisco Systems, Inc.')
dsx0BundleNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 32, 2), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx0BundleNextIndex.setStatus('current')
dsx0BundleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 32, 3), )
if mibBuilder.loadTexts: dsx0BundleTable.setStatus('current')
dsx0BundleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 32, 3, 1), ).setIndexNames((0, "CISCO-DS0BUNDLE-MIB", "dsx0BundleIndex"))
if mibBuilder.loadTexts: dsx0BundleEntry.setStatus('current')
dsx0BundleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 32, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: dsx0BundleIndex.setStatus('current')
dsx0BundleIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 32, 3, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx0BundleIfIndex.setStatus('current')
dsx0BundleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 32, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dsx0BundleRowStatus.setStatus('current')
ds0BundleConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 32, 4))
ds0BundleGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 32, 4, 1))
ds0BundleCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 32, 4, 2))
ds0BundleCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 32, 4, 2, 1)).setObjects(("CISCO-DS0BUNDLE-MIB", "ds0BundleConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ds0BundleCompliance = ds0BundleCompliance.setStatus('current')
ds0BundleConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 32, 4, 1, 2)).setObjects(("CISCO-DS0BUNDLE-MIB", "dsx0BundleNextIndex"), ("CISCO-DS0BUNDLE-MIB", "dsx0BundleIfIndex"), ("CISCO-DS0BUNDLE-MIB", "dsx0BundleRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ds0BundleConfigGroup = ds0BundleConfigGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DS0BUNDLE-MIB", dsx0BundleRowStatus=dsx0BundleRowStatus, ds0BundleCompliances=ds0BundleCompliances, ds0BundleCompliance=ds0BundleCompliance, dsx0BundleTable=dsx0BundleTable, PYSNMP_MODULE_ID=ds0Bundle, dsx0BundleIfIndex=dsx0BundleIfIndex, dsx0BundleNextIndex=dsx0BundleNextIndex, ds0BundleConfigGroup=ds0BundleConfigGroup, ds0BundleGroups=ds0BundleGroups, dsx0BundleEntry=dsx0BundleEntry, ds0Bundle=ds0Bundle, dsx0BundleIndex=dsx0BundleIndex, ds0BundleConformance=ds0BundleConformance)
