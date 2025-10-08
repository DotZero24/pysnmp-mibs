#
# PySNMP MIB module PDN-MPE-HEALTH-AND-STATUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/paradyne/PDN-MPE-HEALTH-AND-STATUS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:38 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
mpe_devHealth, = mibBuilder.importSymbols("PDN-HEADER-MIB", "mpe-devHealth")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, NotificationType, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mpeDevHealthAndStatusMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 1))
mpeDevHealthAndStatusMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 2))
mpeDevHealthAndStatusTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 1, 1), )
if mibBuilder.loadTexts: mpeDevHealthAndStatusTable.setStatus('mandatory')
mpeDevHealthAndStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mpeDevHealthAndStatusEntry.setStatus('mandatory')
mpeDevSelfTestResults = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpeDevSelfTestResults.setStatus('mandatory')
mpeSelfTestFailure = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7, 2) + (0,1)).setObjects(("PDN-MPE-HEALTH-AND-STATUS-MIB", "mpeDevSelfTestResults"))
mibBuilder.exportSymbols("PDN-MPE-HEALTH-AND-STATUS-MIB", mpeDevHealthAndStatusMIBTraps=mpeDevHealthAndStatusMIBTraps, mpeSelfTestFailure=mpeSelfTestFailure, mpeDevHealthAndStatusTable=mpeDevHealthAndStatusTable, mpeDevHealthAndStatusEntry=mpeDevHealthAndStatusEntry, mpeDevHealthAndStatusMIBObjects=mpeDevHealthAndStatusMIBObjects, mpeDevSelfTestResults=mpeDevSelfTestResults)
