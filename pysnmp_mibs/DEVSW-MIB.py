#
# PySNMP MIB module DEVSW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aperto/DEVSW-MIB
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
aniDevSoftware = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 2, 2))
if mibBuilder.loadTexts: aniDevSoftware.setLastUpdated('0105091130Z')
if mibBuilder.loadTexts: aniDevSoftware.setOrganization('Aperto Networks')
aniDevSwConfigFile = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevSwConfigFile.setStatus('current')
aniDevSwSystemSoftwareFile = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevSwSystemSoftwareFile.setStatus('current')
aniDevSwWssSoftwareFile = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevSwWssSoftwareFile.setStatus('current')
aniDevSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 2, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevSwVersion.setStatus('current')
aniDevSwBuild = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevSwBuild.setStatus('current')
aniDevSwBuildDate = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 2, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 22))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevSwBuildDate.setStatus('current')
mibBuilder.exportSymbols("DEVSW-MIB", aniDevSwSystemSoftwareFile=aniDevSwSystemSoftwareFile, aniDevSwVersion=aniDevSwVersion, aniDevSwWssSoftwareFile=aniDevSwWssSoftwareFile, aniDevSwBuild=aniDevSwBuild, aniDevSoftware=aniDevSoftware, PYSNMP_MODULE_ID=aniDevSoftware, aniDevSwConfigFile=aniDevSwConfigFile, aniDevSwBuildDate=aniDevSwBuildDate)
