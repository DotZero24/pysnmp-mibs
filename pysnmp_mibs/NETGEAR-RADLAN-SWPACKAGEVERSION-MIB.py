#
# PySNMP MIB module NETGEAR-RADLAN-SWPACKAGEVERSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/netgear/NETGEAR-RADLAN-SWPACKAGEVERSION-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:50:33 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("NETGEAR-RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rlSwPackageVersion = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 17, 67))
rlSwPackageVersion.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rlSwPackageVersion.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlSwPackageVersion.setOrganization('Radlan - a MARVELL company. Marvell Semiconductor, Inc.')
rlSwPackageVersionTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 17, 67, 1), )
if mibBuilder.loadTexts: rlSwPackageVersionTable.setStatus('current')
rlSwPackageVersionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 17, 67, 1, 1), ).setIndexNames((1, "NETGEAR-RADLAN-SWPACKAGEVERSION-MIB", "rlSwPackageVersionName"))
if mibBuilder.loadTexts: rlSwPackageVersionEntry.setStatus('current')
rlSwPackageVersionName = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 67, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSwPackageVersionName.setStatus('current')
rlSwPackageVersionVesrion = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 67, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSwPackageVersionVesrion.setStatus('current')
mibBuilder.exportSymbols("NETGEAR-RADLAN-SWPACKAGEVERSION-MIB", rlSwPackageVersionTable=rlSwPackageVersionTable, rlSwPackageVersionEntry=rlSwPackageVersionEntry, rlSwPackageVersion=rlSwPackageVersion, rlSwPackageVersionVesrion=rlSwPackageVersionVesrion, PYSNMP_MODULE_ID=rlSwPackageVersion, rlSwPackageVersionName=rlSwPackageVersionName)
