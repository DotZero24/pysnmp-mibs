#
# PySNMP MIB module BRCM-CABLEDATA-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/broadcom/BRCM-CABLEDATA-MGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:23 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cableDataMgmt, = mibBuilder.importSymbols("BRCM-CABLEDATA-SMI", "cableDataMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cableDataMgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2))
cableDataMgmtMIB.setRevisions(('2011-03-01 00:00', '2010-08-16 00:00', '2009-08-27 00:00', '2009-08-26 00:00', '2007-02-05 00:00', '2002-06-04 00:00',))
if mibBuilder.loadTexts: cableDataMgmtMIB.setLastUpdated('201103010000Z')
if mibBuilder.loadTexts: cableDataMgmtMIB.setOrganization('Broadcom Corporation')
cableDataMgmtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1))
cableDataMgmtBase = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1))
cableDataMgmtVendor = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 2, 99))
broadcomCableDataMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 2, 99, 4413))
mibBuilder.exportSymbols("BRCM-CABLEDATA-MGMT-MIB", cableDataMgmtBase=cableDataMgmtBase, cableDataMgmtMIB=cableDataMgmtMIB, cableDataMgmtVendor=cableDataMgmtVendor, broadcomCableDataMgmt=broadcomCableDataMgmt, PYSNMP_MODULE_ID=cableDataMgmtMIB, cableDataMgmtMIBObjects=cableDataMgmtMIBObjects)
