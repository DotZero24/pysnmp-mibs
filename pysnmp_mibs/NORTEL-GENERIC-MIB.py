#
# PySNMP MIB module NORTEL-GENERIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nortel/NORTEL-GENERIC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:03:05 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
nortel, = mibBuilder.importSymbols("NORTEL-MIB", "nortel")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nortelGenericMIBs = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 29))
nortelGenericMIBs.setRevisions(('1999-06-24 00:00', '1999-05-31 00:00', '1999-04-12 00:00', '1999-03-22 00:00',))
if mibBuilder.loadTexts: nortelGenericMIBs.setLastUpdated('9906240000Z')
if mibBuilder.loadTexts: nortelGenericMIBs.setOrganization('Nortel Networks')
nortelNetworkManagementInterfaceMIBs = ObjectIdentity((1, 3, 6, 1, 4, 1, 562, 29, 1))
if mibBuilder.loadTexts: nortelNetworkManagementInterfaceMIBs.setStatus('current')
mibBuilder.exportSymbols("NORTEL-GENERIC-MIB", nortelGenericMIBs=nortelGenericMIBs, PYSNMP_MODULE_ID=nortelGenericMIBs, nortelNetworkManagementInterfaceMIBs=nortelNetworkManagementInterfaceMIBs)
