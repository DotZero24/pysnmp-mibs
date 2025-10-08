#
# PySNMP MIB module FS-EG-BSP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fscom/FS-EG-BSP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:33 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
fsEgBspMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 147))
fsEgBspMIB.setRevisions(('2016-02-19 00:00',))
if mibBuilder.loadTexts: fsEgBspMIB.setLastUpdated('201602190000Z')
if mibBuilder.loadTexts: fsEgBspMIB.setOrganization('FS.COM Inc..')
fsEgBspMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 147, 1))
fsEgBspMaxNumber = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 147, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsEgBspMaxNumber.setStatus('current')
fsEgBspInfoTable = MibTable((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 147, 1, 2), )
if mibBuilder.loadTexts: fsEgBspInfoTable.setStatus('current')
fsEgBspInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 147, 1, 2, 1), ).setIndexNames((0, "FS-EG-BSP-MIB", "fsEgBspInfoMacAddress"), (0, "FS-EG-BSP-MIB", "fsEgBspInfoVlanID"), (0, "FS-EG-BSP-MIB", "fsEgBspInfoPort"))
if mibBuilder.loadTexts: fsEgBspInfoEntry.setStatus('current')
fsEgBspInfoMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 147, 1, 2, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsEgBspInfoMacAddress.setStatus('current')
fsEgBspInfoVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 147, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsEgBspInfoVlanID.setStatus('current')
fsEgBspInfoPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 147, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsEgBspInfoPort.setStatus('current')
fsEgBspInfoAge = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 147, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsEgBspInfoAge.setStatus('current')
fsEgBspMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 147, 2))
fsEgBspMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 147, 2, 1))
fsEgBspMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 147, 2, 2))
fsEgBspMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 147, 2, 1, 1)).setObjects(("FS-EG-BSP-MIB", "fsEgBspMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsEgBspMIBCompliance = fsEgBspMIBCompliance.setStatus('current')
fsEgBspMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 147, 2, 2, 1)).setObjects(("FS-EG-BSP-MIB", "fsEgBspMaxNumber"), ("FS-EG-BSP-MIB", "fsEgBspInfoMacAddress"), ("FS-EG-BSP-MIB", "fsEgBspInfoVlanID"), ("FS-EG-BSP-MIB", "fsEgBspInfoPort"), ("FS-EG-BSP-MIB", "fsEgBspInfoAge"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsEgBspMIBGroup = fsEgBspMIBGroup.setStatus('current')
mibBuilder.exportSymbols("FS-EG-BSP-MIB", fsEgBspInfoPort=fsEgBspInfoPort, fsEgBspMIBGroup=fsEgBspMIBGroup, fsEgBspMIBCompliance=fsEgBspMIBCompliance, fsEgBspMIBCompliances=fsEgBspMIBCompliances, fsEgBspInfoTable=fsEgBspInfoTable, fsEgBspMIBConformance=fsEgBspMIBConformance, fsEgBspInfoMacAddress=fsEgBspInfoMacAddress, PYSNMP_MODULE_ID=fsEgBspMIB, fsEgBspInfoAge=fsEgBspInfoAge, fsEgBspInfoEntry=fsEgBspInfoEntry, fsEgBspMIBGroups=fsEgBspMIBGroups, fsEgBspMaxNumber=fsEgBspMaxNumber, fsEgBspMIBObjects=fsEgBspMIBObjects, fsEgBspMIB=fsEgBspMIB, fsEgBspInfoVlanID=fsEgBspInfoVlanID)
