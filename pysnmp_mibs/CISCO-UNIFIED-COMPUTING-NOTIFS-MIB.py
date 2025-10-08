#
# PySNMP MIB module CISCO-UNIFIED-COMPUTING-NOTIFS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-UNIFIED-COMPUTING-NOTIFS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:13:42 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
cucsFaultCreationTime, cucsFaultType, cucsFaultCode, cucsFaultLastModificationTime, cucsFaultSeverity, cucsFaultAffectedObjectDn, cucsFaultAffectedObjectId, cucsFaultIndex, cucsFaultProbableCause, cucsFaultId, cucsFaultDescription, cucsFaultOccur = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultCreationTime", "cucsFaultType", "cucsFaultCode", "cucsFaultLastModificationTime", "cucsFaultSeverity", "cucsFaultAffectedObjectDn", "cucsFaultAffectedObjectId", "cucsFaultIndex", "cucsFaultProbableCause", "cucsFaultId", "cucsFaultDescription", "cucsFaultOccur")
ciscoUnifiedComputingMIB, ciscoUnifiedComputingMIBObjects = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-MIB", "ciscoUnifiedComputingMIB", "ciscoUnifiedComputingMIBObjects")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoUnifiedComputingMIBNotifs = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 719, 0))
ciscoUnifiedComputingMIBNotifs.setRevisions(('2010-01-29 00:00',))
if mibBuilder.loadTexts: ciscoUnifiedComputingMIBNotifs.setLastUpdated('201001290000Z')
if mibBuilder.loadTexts: ciscoUnifiedComputingMIBNotifs.setOrganization('Cisco')
cucsFaultActiveNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 719, 0, 1)).setObjects(("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultIndex"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultDescription"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedObjectId"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedObjectDn"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultCreationTime"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultLastModificationTime"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultCode"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultType"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultProbableCause"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultSeverity"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultOccur"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultId"))
if mibBuilder.loadTexts: cucsFaultActiveNotif.setStatus('current')
cucsFaultClearNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 719, 0, 2)).setObjects(("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultIndex"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultDescription"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedObjectId"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedObjectDn"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultCreationTime"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultLastModificationTime"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultCode"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultType"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultProbableCause"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultSeverity"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultOccur"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultId"))
if mibBuilder.loadTexts: cucsFaultClearNotif.setStatus('current')
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-NOTIFS-MIB", ciscoUnifiedComputingMIBNotifs=ciscoUnifiedComputingMIBNotifs, PYSNMP_MODULE_ID=ciscoUnifiedComputingMIBNotifs, cucsFaultActiveNotif=cucsFaultActiveNotif, cucsFaultClearNotif=cucsFaultClearNotif)
