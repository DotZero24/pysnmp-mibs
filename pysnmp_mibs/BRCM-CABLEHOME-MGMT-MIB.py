#
# PySNMP MIB module BRCM-CABLEHOME-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/broadcom/BRCM-CABLEHOME-MGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:18:02 2025
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
cablehomeMgmt = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 3))
cablehomeMgmt.setRevisions(('2007-02-05 00:00', '2004-04-05 00:00', '2003-03-06 00:00',))
if mibBuilder.loadTexts: cablehomeMgmt.setLastUpdated('200702050000Z')
if mibBuilder.loadTexts: cablehomeMgmt.setOrganization('Broadcom Corporation')
chMgmtBase = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 3, 1))
chCsaOperMode = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("csa10", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chCsaOperMode.setStatus('current')
mibBuilder.exportSymbols("BRCM-CABLEHOME-MGMT-MIB", PYSNMP_MODULE_ID=cablehomeMgmt, chMgmtBase=chMgmtBase, cablehomeMgmt=cablehomeMgmt, chCsaOperMode=chCsaOperMode)
