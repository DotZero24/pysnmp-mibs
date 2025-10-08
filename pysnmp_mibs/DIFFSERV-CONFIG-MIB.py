#
# PySNMP MIB module DIFFSERV-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/DIFFSERV-CONFIG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:49:24 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, zeroDotZero, MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "zeroDotZero", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "mib-2")
RowStatus, DateAndTime, TextualConvention, StorageType, RowPointer, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "StorageType", "RowPointer", "DisplayString")
diffServConfigMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 108))
diffServConfigMib.setRevisions(('2004-01-22 00:00',))
if mibBuilder.loadTexts: diffServConfigMib.setLastUpdated('200401220000Z')
if mibBuilder.loadTexts: diffServConfigMib.setOrganization('SNMPCONF WG')
diffServConfigMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 108, 1))
diffServConfigMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 108, 2))
diffServConfigTable = MibTable((1, 3, 6, 1, 2, 1, 108, 1, 2), )
if mibBuilder.loadTexts: diffServConfigTable.setStatus('current')
diffServConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 108, 1, 2, 1), ).setIndexNames((0, "DIFFSERV-CONFIG-MIB", "diffServConfigId"))
if mibBuilder.loadTexts: diffServConfigEntry.setStatus('current')
diffServConfigId = MibTableColumn((1, 3, 6, 1, 2, 1, 108, 1, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 116)))
if mibBuilder.loadTexts: diffServConfigId.setStatus('current')
diffServConfigDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 108, 1, 2, 1, 2), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: diffServConfigDescr.setStatus('current')
diffServConfigOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 108, 1, 2, 1, 3), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: diffServConfigOwner.setStatus('current')
diffServConfigLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 108, 1, 2, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diffServConfigLastChange.setStatus('current')
diffServConfigStart = MibTableColumn((1, 3, 6, 1, 2, 1, 108, 1, 2, 1, 5), RowPointer().clone((0, 0))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: diffServConfigStart.setStatus('current')
diffServConfigStorage = MibTableColumn((1, 3, 6, 1, 2, 1, 108, 1, 2, 1, 6), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: diffServConfigStorage.setStatus('current')
diffServConfigStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 108, 1, 2, 1, 7), RowStatus().clone('notInService')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: diffServConfigStatus.setStatus('current')
diffServConfigMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 108, 2, 1))
diffServConfigMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 108, 2, 2))
diffServConfigMIBFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 108, 2, 1, 1)).setObjects(("DIFFSERV-CONFIG-MIB", "diffServConfigMIBConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    diffServConfigMIBFullCompliance = diffServConfigMIBFullCompliance.setStatus('current')
diffServConfigMIBConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 108, 2, 2, 1)).setObjects(("DIFFSERV-CONFIG-MIB", "diffServConfigDescr"), ("DIFFSERV-CONFIG-MIB", "diffServConfigOwner"), ("DIFFSERV-CONFIG-MIB", "diffServConfigLastChange"), ("DIFFSERV-CONFIG-MIB", "diffServConfigStart"), ("DIFFSERV-CONFIG-MIB", "diffServConfigStorage"), ("DIFFSERV-CONFIG-MIB", "diffServConfigStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    diffServConfigMIBConfigGroup = diffServConfigMIBConfigGroup.setStatus('current')
mibBuilder.exportSymbols("DIFFSERV-CONFIG-MIB", diffServConfigStatus=diffServConfigStatus, diffServConfigMIBConfigGroup=diffServConfigMIBConfigGroup, diffServConfigMIBConformance=diffServConfigMIBConformance, diffServConfigMIBObjects=diffServConfigMIBObjects, diffServConfigTable=diffServConfigTable, diffServConfigDescr=diffServConfigDescr, diffServConfigStorage=diffServConfigStorage, diffServConfigStart=diffServConfigStart, diffServConfigMIBGroups=diffServConfigMIBGroups, diffServConfigMIBFullCompliance=diffServConfigMIBFullCompliance, diffServConfigMib=diffServConfigMib, diffServConfigEntry=diffServConfigEntry, diffServConfigOwner=diffServConfigOwner, diffServConfigLastChange=diffServConfigLastChange, diffServConfigId=diffServConfigId, diffServConfigMIBCompliances=diffServConfigMIBCompliances, PYSNMP_MODULE_ID=diffServConfigMib)
