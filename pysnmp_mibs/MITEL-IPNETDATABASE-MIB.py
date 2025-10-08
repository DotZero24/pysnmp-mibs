#
# PySNMP MIB module MITEL-IPNETDATABASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/mitel/MITEL-IPNETDATABASE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:40 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("MITEL-IPNETDATABASE-MIB", mitelRouterDatabaseVersion=mitelRouterDatabaseVersion, mitelProprietary=mitelProprietary, mitelRouterDatabaseMajorVersion=mitelRouterDatabaseMajorVersion, mitelPropIpNetworking=mitelPropIpNetworking, PYSNMP_MODULE_ID=mitelRouterDatabaseVersion, mitelRouterDatabaseMinorVersion=mitelRouterDatabaseMinorVersion, mitel=mitel, mitelIpNetRouter=mitelIpNetRouter)
