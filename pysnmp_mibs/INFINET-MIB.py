#
# PySNMP MIB module INFINET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinet/INFINET-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:16 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
infinet = ModuleIdentity((1, 3, 6, 1, 4, 1, 3942))
infinet.setRevisions(('2007-11-08 11:04', '2004-08-16 19:10',))
if mibBuilder.loadTexts: infinet.setLastUpdated('200711081104Z')
if mibBuilder.loadTexts: infinet.setOrganization('Infinet Wireless Ltd.')
iwrouter = MibIdentifier((1, 3, 6, 1, 4, 1, 3942, 1))
wanflex = MibIdentifier((1, 3, 6, 1, 4, 1, 3942, 1, 1))
mibBuilder.exportSymbols("INFINET-MIB", infinet=infinet, iwrouter=iwrouter, wanflex=wanflex, PYSNMP_MODULE_ID=infinet)
