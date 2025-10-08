#
# PySNMP MIB module RADLAN-SWPACKAGEVERSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/radlan/RADLAN-SWPACKAGEVERSION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:40:51 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlSwPackageVersion = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 67))
rlSwPackageVersion.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rlSwPackageVersion.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlSwPackageVersion.setOrganization('Radlan - a MARVELL company. Marvell Semiconductor, Inc.')
rlSwPackageVersionTable = MibTable((1, 3, 6, 1, 4, 1, 89, 67, 1), )
if mibBuilder.loadTexts: rlSwPackageVersionTable.setStatus('current')
rlSwPackageVersionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 67, 1, 1), ).setIndexNames((1, "RADLAN-SWPACKAGEVERSION-MIB", "rlSwPackageVersionName"))
if mibBuilder.loadTexts: rlSwPackageVersionEntry.setStatus('current')
rlSwPackageVersionName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 67, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSwPackageVersionName.setStatus('current')
rlSwPackageVersionVesrion = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 67, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSwPackageVersionVesrion.setStatus('current')
mibBuilder.exportSymbols("RADLAN-SWPACKAGEVERSION-MIB", rlSwPackageVersion=rlSwPackageVersion, rlSwPackageVersionEntry=rlSwPackageVersionEntry, rlSwPackageVersionName=rlSwPackageVersionName, PYSNMP_MODULE_ID=rlSwPackageVersion, rlSwPackageVersionVesrion=rlSwPackageVersionVesrion, rlSwPackageVersionTable=rlSwPackageVersionTable)
