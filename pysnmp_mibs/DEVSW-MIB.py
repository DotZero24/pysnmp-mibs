#
# PySNMP MIB module DEVSW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/aperto/DEVSW-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:18 2025
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
mibBuilder.exportSymbols("DEVSW-MIB", aniDevSwBuild=aniDevSwBuild, aniDevSwConfigFile=aniDevSwConfigFile, aniDevSwVersion=aniDevSwVersion, aniDevSwSystemSoftwareFile=aniDevSwSystemSoftwareFile, PYSNMP_MODULE_ID=aniDevSoftware, aniDevSwBuildDate=aniDevSwBuildDate, aniDevSwWssSoftwareFile=aniDevSwWssSoftwareFile, aniDevSoftware=aniDevSoftware)
