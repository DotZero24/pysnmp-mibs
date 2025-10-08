#
# PySNMP MIB module MPFW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/maipu/MPFW-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:19:13 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
mpMgmt, = mibBuilder.importSymbols("MAIPU-SMI", "mpMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectSyntax, Counter32, ModuleIdentity, TimeTicks, Counter64, ObjectIdentity, Gauge32, ObjectName = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectSyntax", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "ObjectIdentity", "Gauge32", "ObjectName")
RowStatus, DateAndTime, TextualConvention, MacAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "MacAddress", "TruthValue", "DisplayString")
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
mibBuilder.exportSymbols("MPFW-MIB", fwIfDirection=fwIfDirection, fwIfRowStatus=fwIfRowStatus, PYSNMP_MODULE_ID=mpFwMib, mpFwIfEntry=mpFwIfEntry, fwIfName=fwIfName, mpFwIfTable=mpFwIfTable, fwIfGrpName=fwIfGrpName, mpFwMib=mpFwMib)
