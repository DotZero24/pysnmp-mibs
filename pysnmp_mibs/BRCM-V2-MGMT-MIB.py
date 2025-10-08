#
# PySNMP MIB module BRCM-V2-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/broadcom/BRCM-V2-MGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:18:10 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cableDataMgmtMIBObjects, = mibBuilder.importSymbols("BRCM-CABLEDATA-MGMT-MIB", "cableDataMgmtMIBObjects")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
v2Mgmt = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 4))
v2Mgmt.setRevisions(('2007-02-05 00:00', '2003-03-06 00:00',))
if mibBuilder.loadTexts: v2Mgmt.setLastUpdated('200702050000Z')
if mibBuilder.loadTexts: v2Mgmt.setOrganization('Broadcom Corporation')
v2MgmtBase = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 4, 1))
mibBuilder.exportSymbols("BRCM-V2-MGMT-MIB", v2MgmtBase=v2MgmtBase, v2Mgmt=v2Mgmt, PYSNMP_MODULE_ID=v2Mgmt)
