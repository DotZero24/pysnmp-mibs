#
# PySNMP MIB module FS-EG-BSP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fscom/FS-EG-BSP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:01:17 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("FS-EG-BSP-MIB", PYSNMP_MODULE_ID=fsEgBspMIB, fsEgBspMIBCompliance=fsEgBspMIBCompliance, fsEgBspMIB=fsEgBspMIB, fsEgBspInfoTable=fsEgBspInfoTable, fsEgBspInfoEntry=fsEgBspInfoEntry, fsEgBspInfoMacAddress=fsEgBspInfoMacAddress, fsEgBspInfoAge=fsEgBspInfoAge, fsEgBspInfoVlanID=fsEgBspInfoVlanID, fsEgBspMIBGroups=fsEgBspMIBGroups, fsEgBspMIBConformance=fsEgBspMIBConformance, fsEgBspMIBGroup=fsEgBspMIBGroup, fsEgBspMIBCompliances=fsEgBspMIBCompliances, fsEgBspMIBObjects=fsEgBspMIBObjects, fsEgBspMaxNumber=fsEgBspMaxNumber, fsEgBspInfoPort=fsEgBspInfoPort)
