#
# PySNMP MIB module BRCM-CABLEDATA-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/broadcom/BRCM-CABLEDATA-MGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:18:17 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cableDataMgmt, = mibBuilder.importSymbols("BRCM-CABLEDATA-SMI", "cableDataMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cableDataMgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2))
cableDataMgmtMIB.setRevisions(('2011-03-01 00:00', '2010-08-16 00:00', '2009-08-27 00:00', '2009-08-26 00:00', '2007-02-05 00:00', '2002-06-04 00:00',))
if mibBuilder.loadTexts: cableDataMgmtMIB.setLastUpdated('201103010000Z')
if mibBuilder.loadTexts: cableDataMgmtMIB.setOrganization('Broadcom Corporation')
cableDataMgmtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1))
cableDataMgmtBase = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1))
cableDataMgmtVendor = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 2, 99))
broadcomCableDataMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 2, 99, 4413))
mibBuilder.exportSymbols("BRCM-CABLEDATA-MGMT-MIB", PYSNMP_MODULE_ID=cableDataMgmtMIB, cableDataMgmtBase=cableDataMgmtBase, broadcomCableDataMgmt=broadcomCableDataMgmt, cableDataMgmtMIBObjects=cableDataMgmtMIBObjects, cableDataMgmtVendor=cableDataMgmtVendor, cableDataMgmtMIB=cableDataMgmtMIB)
