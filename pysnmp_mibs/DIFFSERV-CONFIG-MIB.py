#
# PySNMP MIB module DIFFSERV-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/DIFFSERV-CONFIG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:13 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, zeroDotZero, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, TimeTicks, Unsigned32, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "zeroDotZero", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "TimeTicks", "Unsigned32", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
DisplayString, RowStatus, TextualConvention, DateAndTime, RowPointer, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "DateAndTime", "RowPointer", "StorageType")
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
mibBuilder.exportSymbols("DIFFSERV-CONFIG-MIB", diffServConfigId=diffServConfigId, diffServConfigMIBFullCompliance=diffServConfigMIBFullCompliance, diffServConfigStart=diffServConfigStart, diffServConfigMIBGroups=diffServConfigMIBGroups, PYSNMP_MODULE_ID=diffServConfigMib, diffServConfigMIBConformance=diffServConfigMIBConformance, diffServConfigOwner=diffServConfigOwner, diffServConfigMIBObjects=diffServConfigMIBObjects, diffServConfigLastChange=diffServConfigLastChange, diffServConfigMIBConfigGroup=diffServConfigMIBConfigGroup, diffServConfigMIBCompliances=diffServConfigMIBCompliances, diffServConfigTable=diffServConfigTable, diffServConfigMib=diffServConfigMib, diffServConfigStorage=diffServConfigStorage, diffServConfigDescr=diffServConfigDescr, diffServConfigStatus=diffServConfigStatus, diffServConfigEntry=diffServConfigEntry)
