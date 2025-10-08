#
# PySNMP MIB module DEVHW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aperto/DEVHW-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:55 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
device, = mibBuilder.importSymbols("ANIROOT-MIB", "device")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("DEVHW-MIB", aniDevHwSpeed=aniDevHwSpeed, aniDevHwRevision=aniDevHwRevision, aniDevHwBoardRevision=aniDevHwBoardRevision, aniDevHwBuildDate=aniDevHwBuildDate, aniDevHardware=aniDevHardware, aniDevHwSerialNum=aniDevHwSerialNum, PYSNMP_MODULE_ID=aniDevHardware)
