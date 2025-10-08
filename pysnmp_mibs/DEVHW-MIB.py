#
# PySNMP MIB module DEVHW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/aperto/DEVHW-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:19 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
device, = mibBuilder.importSymbols("ANIROOT-MIB", "device")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aniDevHardware = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 2, 3))
if mibBuilder.loadTexts: aniDevHardware.setLastUpdated('0105091130Z')
if mibBuilder.loadTexts: aniDevHardware.setOrganization('Aperto Networks')
aniDevHwRevision = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevHwRevision.setStatus('current')
aniDevHwSpeed = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 3, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevHwSpeed.setStatus('current')
aniDevHwBuildDate = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 3, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 22))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevHwBuildDate.setStatus('current')
aniDevHwSerialNum = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 3, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevHwSerialNum.setStatus('current')
aniDevHwBoardRevision = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 3, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevHwBoardRevision.setStatus('current')
mibBuilder.exportSymbols("DEVHW-MIB", aniDevHwBoardRevision=aniDevHwBoardRevision, PYSNMP_MODULE_ID=aniDevHardware, aniDevHardware=aniDevHardware, aniDevHwBuildDate=aniDevHwBuildDate, aniDevHwSerialNum=aniDevHwSerialNum, aniDevHwRevision=aniDevHwRevision, aniDevHwSpeed=aniDevHwSpeed)
