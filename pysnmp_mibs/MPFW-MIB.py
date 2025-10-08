#
# PySNMP MIB module MPFW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/maipu/MPFW-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:57 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mpMgmt, = mibBuilder.importSymbols("MAIPU-SMI", "mpMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, ObjectSyntax, iso, MibIdentifier, ObjectName, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "ObjectSyntax", "iso", "MibIdentifier", "ObjectName", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, RowStatus, DateAndTime, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "DateAndTime", "TruthValue", "TextualConvention")
mpFwMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 5651, 3, 35))
if mibBuilder.loadTexts: mpFwMib.setLastUpdated('0603191042Z')
if mibBuilder.loadTexts: mpFwMib.setOrganization('ĴͨŹɷ\u07b9˾, Maipu (Sichuan) Communication Technology Co. LTD.')
mpFwIfTable = MibTable((1, 3, 6, 1, 4, 1, 5651, 3, 35, 10), )
if mibBuilder.loadTexts: mpFwIfTable.setStatus('current')
mpFwIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5651, 3, 35, 10, 1), ).setIndexNames((0, "MPFW-MIB", "fwIfName"), (0, "MPFW-MIB", "fwIfDirection"))
if mibBuilder.loadTexts: mpFwIfEntry.setStatus('current')
fwIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 5651, 3, 35, 10, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 39))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fwIfName.setStatus('current')
fwIfDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 5651, 3, 35, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("in", 1), ("out", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fwIfDirection.setStatus('current')
fwIfGrpName = MibTableColumn((1, 3, 6, 1, 4, 1, 5651, 3, 35, 10, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwIfGrpName.setStatus('current')
fwIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5651, 3, 35, 10, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fwIfRowStatus.setStatus('current')
mibBuilder.exportSymbols("MPFW-MIB", fwIfRowStatus=fwIfRowStatus, fwIfName=fwIfName, fwIfGrpName=fwIfGrpName, PYSNMP_MODULE_ID=mpFwMib, mpFwIfTable=mpFwIfTable, fwIfDirection=fwIfDirection, mpFwIfEntry=mpFwIfEntry, mpFwMib=mpFwMib)
