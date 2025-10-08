#
# PySNMP MIB module CISCO-FIREPOWER-NOTIFS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-FIREPOWER-NOTIFS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:23:16 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cfprFaultInstCode, cfprFaultInstType, cfprFaultInstCause, cfprFaultInstDescr, cfprFaultInstSeverity, cfprFaultInstLastTransition, cfprFaultInstOccur, cfprFaultInstInstanceId, cfprFaultInstCreated, cfprFaultInstAffectedObjectDn, cfprFaultInstAffectedObjectId, cfprFaultInstId = mibBuilder.importSymbols("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstCode", "cfprFaultInstType", "cfprFaultInstCause", "cfprFaultInstDescr", "cfprFaultInstSeverity", "cfprFaultInstLastTransition", "cfprFaultInstOccur", "cfprFaultInstInstanceId", "cfprFaultInstCreated", "cfprFaultInstAffectedObjectDn", "cfprFaultInstAffectedObjectId", "cfprFaultInstId")
ciscoFirepowerMIB, = mibBuilder.importSymbols("CISCO-FIREPOWER-MIB", "ciscoFirepowerMIB")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoFirepowerMIBNotifs = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 826, 0))
ciscoFirepowerMIBNotifs.setRevisions(('2010-01-29 00:00',))
if mibBuilder.loadTexts: ciscoFirepowerMIBNotifs.setLastUpdated('201703151700Z')
if mibBuilder.loadTexts: ciscoFirepowerMIBNotifs.setOrganization('Cisco')
cfprFaultActiveNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 826, 0, 1)).setObjects(("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstInstanceId"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstDescr"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstAffectedObjectId"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstAffectedObjectDn"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstCreated"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstLastTransition"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstCode"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstType"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstCause"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstSeverity"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstOccur"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstId"))
if mibBuilder.loadTexts: cfprFaultActiveNotif.setStatus('current')
cfprFaultClearNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 826, 0, 2)).setObjects(("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstInstanceId"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstDescr"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstAffectedObjectId"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstAffectedObjectDn"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstCreated"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstLastTransition"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstCode"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstType"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstCause"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstSeverity"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstOccur"), ("CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstId"))
if mibBuilder.loadTexts: cfprFaultClearNotif.setStatus('current')
mibBuilder.exportSymbols("CISCO-FIREPOWER-NOTIFS-MIB", cfprFaultClearNotif=cfprFaultClearNotif, cfprFaultActiveNotif=cfprFaultActiveNotif, PYSNMP_MODULE_ID=ciscoFirepowerMIBNotifs, ciscoFirepowerMIBNotifs=ciscoFirepowerMIBNotifs)
