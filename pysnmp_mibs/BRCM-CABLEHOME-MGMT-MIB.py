#
# PySNMP MIB module BRCM-CABLEHOME-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/broadcom/BRCM-CABLEHOME-MGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:15 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cableDataMgmtMIBObjects, = mibBuilder.importSymbols("BRCM-CABLEDATA-MGMT-MIB", "cableDataMgmtMIBObjects")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cablehomeMgmt = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 3))
cablehomeMgmt.setRevisions(('2007-02-05 00:00', '2004-04-05 00:00', '2003-03-06 00:00',))
if mibBuilder.loadTexts: cablehomeMgmt.setLastUpdated('200702050000Z')
if mibBuilder.loadTexts: cablehomeMgmt.setOrganization('Broadcom Corporation')
chMgmtBase = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 3, 1))
chCsaOperMode = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("csa10", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chCsaOperMode.setStatus('current')
mibBuilder.exportSymbols("BRCM-CABLEHOME-MGMT-MIB", PYSNMP_MODULE_ID=cablehomeMgmt, chMgmtBase=chMgmtBase, chCsaOperMode=chCsaOperMode, cablehomeMgmt=cablehomeMgmt)
