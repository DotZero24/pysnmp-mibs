#
# PySNMP MIB module PDN-MPE-HEALTH-AND-STATUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/paradyne/PDN-MPE-HEALTH-AND-STATUS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:57:14 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
mpe_devHealth, = mibBuilder.importSymbols("PDN-HEADER-MIB", "mpe-devHealth")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mpeDevHealthAndStatusMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 1))
mpeDevHealthAndStatusMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 2))
mpeDevHealthAndStatusTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 1, 1), )
if mibBuilder.loadTexts: mpeDevHealthAndStatusTable.setStatus('mandatory')
mpeDevHealthAndStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mpeDevHealthAndStatusEntry.setStatus('mandatory')
mpeDevSelfTestResults = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpeDevSelfTestResults.setStatus('mandatory')
mpeSelfTestFailure = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 2) + (0,1)).setObjects(("PDN-MPE-HEALTH-AND-STATUS-MIB", "mpeDevSelfTestResults"))
mibBuilder.exportSymbols("PDN-MPE-HEALTH-AND-STATUS-MIB", mpeDevHealthAndStatusEntry=mpeDevHealthAndStatusEntry, mpeDevHealthAndStatusMIBTraps=mpeDevHealthAndStatusMIBTraps, mpeDevHealthAndStatusMIBObjects=mpeDevHealthAndStatusMIBObjects, mpeSelfTestFailure=mpeSelfTestFailure, mpeDevHealthAndStatusTable=mpeDevHealthAndStatusTable, mpeDevSelfTestResults=mpeDevSelfTestResults)
