#
# PySNMP MIB module CISCO-UNIFIED-COMPUTING-NOTIFS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-UNIFIED-COMPUTING-NOTIFS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:26:51 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
cucsFaultType, cucsFaultSeverity, cucsFaultCode, cucsFaultOccur, cucsFaultIndex, cucsFaultDescription, cucsFaultAffectedObjectId, cucsFaultCreationTime, cucsFaultAffectedObjectDn, cucsFaultProbableCause, cucsFaultLastModificationTime, cucsFaultId = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultType", "cucsFaultSeverity", "cucsFaultCode", "cucsFaultOccur", "cucsFaultIndex", "cucsFaultDescription", "cucsFaultAffectedObjectId", "cucsFaultCreationTime", "cucsFaultAffectedObjectDn", "cucsFaultProbableCause", "cucsFaultLastModificationTime", "cucsFaultId")
ciscoUnifiedComputingMIB, ciscoUnifiedComputingMIBObjects = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-MIB", "ciscoUnifiedComputingMIB", "ciscoUnifiedComputingMIBObjects")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoUnifiedComputingMIBNotifs = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 719, 0))
ciscoUnifiedComputingMIBNotifs.setRevisions(('2010-01-29 00:00',))
if mibBuilder.loadTexts: ciscoUnifiedComputingMIBNotifs.setLastUpdated('201001290000Z')
if mibBuilder.loadTexts: ciscoUnifiedComputingMIBNotifs.setOrganization('Cisco')
cucsFaultActiveNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 719, 0, 1)).setObjects(("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultIndex"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultDescription"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedObjectId"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedObjectDn"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultCreationTime"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultLastModificationTime"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultCode"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultType"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultProbableCause"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultSeverity"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultOccur"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultId"))
if mibBuilder.loadTexts: cucsFaultActiveNotif.setStatus('current')
cucsFaultClearNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 719, 0, 2)).setObjects(("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultIndex"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultDescription"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedObjectId"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedObjectDn"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultCreationTime"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultLastModificationTime"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultCode"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultType"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultProbableCause"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultSeverity"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultOccur"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultId"))
if mibBuilder.loadTexts: cucsFaultClearNotif.setStatus('current')
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-NOTIFS-MIB", ciscoUnifiedComputingMIBNotifs=ciscoUnifiedComputingMIBNotifs, cucsFaultActiveNotif=cucsFaultActiveNotif, PYSNMP_MODULE_ID=ciscoUnifiedComputingMIBNotifs, cucsFaultClearNotif=cucsFaultClearNotif)
