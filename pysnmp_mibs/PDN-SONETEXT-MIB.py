#
# PySNMP MIB module PDN-SONETEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/paradyne/PDN-SONETEXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:57:07 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
pdnSonetMIB, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdnSonetMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sonetSectionCurrentStatus, sonetLineCurrentStatus, sonetPathCurrentStatus = mibBuilder.importSymbols("SONET-MIB", "sonetSectionCurrentStatus", "sonetLineCurrentStatus", "sonetPathCurrentStatus")
devSonetConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 1))
devSonetTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 2))
devSonetConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 1, 1), )
if mibBuilder.loadTexts: devSonetConfigTable.setStatus('mandatory')
devSonetConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 1, 1, 1), ).setIndexNames((0, "PDN-SONETEXT-MIB", "devSonetIfIndex"))
if mibBuilder.loadTexts: devSonetConfigEntry.setStatus('mandatory')
devSonetIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devSonetIfIndex.setStatus('mandatory')
devSonetXmitClkSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("loopTiming", 1), ("localTiming", 2), ("throughTiming", 3), ("systemTiming", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devSonetXmitClkSrc.setStatus('mandatory')
devSonetStatusLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 1, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devSonetStatusLastChange.setStatus('mandatory')
devSonetStatusChangeTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devSonetStatusChangeTrapEnable.setStatus('mandatory')
devSonetStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 2) + (0,1)).setObjects(("PDN-SONETEXT-MIB", "devSonetStatusLastChange"), ("SONET-MIB", "sonetSectionCurrentStatus"), ("SONET-MIB", "sonetLineCurrentStatus"), ("SONET-MIB", "sonetPathCurrentStatus"))
mibBuilder.exportSymbols("PDN-SONETEXT-MIB", devSonetStatusLastChange=devSonetStatusLastChange, devSonetStatusChange=devSonetStatusChange, devSonetConfig=devSonetConfig, devSonetStatusChangeTrapEnable=devSonetStatusChangeTrapEnable, devSonetTraps=devSonetTraps, devSonetXmitClkSrc=devSonetXmitClkSrc, devSonetConfigEntry=devSonetConfigEntry, devSonetConfigTable=devSonetConfigTable, devSonetIfIndex=devSonetIfIndex)
