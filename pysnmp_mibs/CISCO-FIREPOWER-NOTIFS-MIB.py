#
# PySNMP MIB module CISCO-FIREPOWER-NOTIFS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-FIREPOWER-NOTIFS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:11:13 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cfprFaultInstId, cfprFaultInstDescr, cfprFaultInstLastTransition, cfprFaultInstSeverity, cfprFaultInstOccur, cfprFaultInstCode, cfprFaultInstCreated, cfprFaultInstInstanceId, cfprFaultInstAffectedObjectId, cfprFaultInstCause, cfprFaultInstType, cfprFaultInstAffectedObjectDn = mibBuilder.importSymbols("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstId", "cfprFaultInstDescr", "cfprFaultInstLastTransition", "cfprFaultInstSeverity", "cfprFaultInstOccur", "cfprFaultInstCode", "cfprFaultInstCreated", "cfprFaultInstInstanceId", "cfprFaultInstAffectedObjectId", "cfprFaultInstCause", "cfprFaultInstType", "cfprFaultInstAffectedObjectDn")
ciscoFirepowerMIB, = mibBuilder.importSymbols("CISCO-FIREPOWER-MIB", "ciscoFirepowerMIB")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoFirepowerMIBNotifs = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 826, 0))
ciscoFirepowerMIBNotifs.setRevisions(('2010-01-29 00:00',))
if mibBuilder.loadTexts: ciscoFirepowerMIBNotifs.setLastUpdated('201703151700Z')
if mibBuilder.loadTexts: ciscoFirepowerMIBNotifs.setOrganization('Cisco')
cfprFaultActiveNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 826, 0, 1)).setObjects(("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstInstanceId"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstDescr"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstAffectedObjectId"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstAffectedObjectDn"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstCreated"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstLastTransition"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstCode"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstType"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstCause"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstSeverity"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstOccur"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstId"))
if mibBuilder.loadTexts: cfprFaultActiveNotif.setStatus('current')
cfprFaultClearNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 826, 0, 2)).setObjects(("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstInstanceId"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstDescr"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstAffectedObjectId"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstAffectedObjectDn"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstCreated"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstLastTransition"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstCode"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstType"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstCause"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstSeverity"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstOccur"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstId"))
if mibBuilder.loadTexts: cfprFaultClearNotif.setStatus('current')
mibBuilder.exportSymbols("CISCO-FIREPOWER-NOTIFS-MIB", ciscoFirepowerMIBNotifs=ciscoFirepowerMIBNotifs, cfprFaultActiveNotif=cfprFaultActiveNotif, cfprFaultClearNotif=cfprFaultClearNotif, PYSNMP_MODULE_ID=ciscoFirepowerMIBNotifs)
