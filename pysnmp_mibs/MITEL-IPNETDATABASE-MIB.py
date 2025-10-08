#
# PySNMP MIB module MITEL-IPNETDATABASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/mitel/MITEL-IPNETDATABASE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:05:00 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mitelRouterDatabaseVersion = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 8))
mitelRouterDatabaseVersion.setRevisions(('2003-03-24 09:26',))
if mibBuilder.loadTexts: mitelRouterDatabaseVersion.setLastUpdated('200303240926Z')
if mibBuilder.loadTexts: mitelRouterDatabaseVersion.setOrganization('MITEL Corporation')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelPropIpNetworking = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8))
mitelIpNetRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1))
mitelRouterDatabaseMajorVersion = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 8, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelRouterDatabaseMajorVersion.setStatus('current')
mitelRouterDatabaseMinorVersion = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 8, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelRouterDatabaseMinorVersion.setStatus('current')
mibBuilder.exportSymbols("MITEL-IPNETDATABASE-MIB", mitelIpNetRouter=mitelIpNetRouter, mitelProprietary=mitelProprietary, mitelRouterDatabaseMinorVersion=mitelRouterDatabaseMinorVersion, mitel=mitel, mitelRouterDatabaseMajorVersion=mitelRouterDatabaseMajorVersion, PYSNMP_MODULE_ID=mitelRouterDatabaseVersion, mitelRouterDatabaseVersion=mitelRouterDatabaseVersion, mitelPropIpNetworking=mitelPropIpNetworking)
