#
# PySNMP MIB module MICROSENS-G6-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/microsens/MICROSENS-G6-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:10 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
microsens = ModuleIdentity((1, 3, 6, 1, 4, 1, 3181))
microsens.setRevisions(('2018-02-12 16:19',))
if mibBuilder.loadTexts: microsens.setLastUpdated('201802121619Z')
if mibBuilder.loadTexts: microsens.setOrganization('MICROSENS GmbH & Co. KG')
managedSwitches = MibIdentifier((1, 3, 6, 1, 4, 1, 3181, 10))
g6 = MibIdentifier((1, 3, 6, 1, 4, 1, 3181, 10, 6))
mibBuilder.exportSymbols("MICROSENS-G6-MIB", PYSNMP_MODULE_ID=microsens, g6=g6, microsens=microsens, managedSwitches=managedSwitches)
