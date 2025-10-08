#
# PySNMP MIB module MAIPU-LLC2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/maipu/MAIPU-LLC2-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:19:20 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
mpMgmt, = mibBuilder.importSymbols("MAIPU-SMI", "mpMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
mpLlc2Mib = ModuleIdentity((1, 3, 6, 1, 4, 1, 5651, 3, 23))
if mibBuilder.loadTexts: mpLlc2Mib.setLastUpdated('0204270000Z')
if mibBuilder.loadTexts: mpLlc2Mib.setOrganization('Maipu DataComm')
llc2ConfTable = MibTable((1, 3, 6, 1, 4, 1, 5651, 3, 23, 1), )
if mibBuilder.loadTexts: llc2ConfTable.setStatus('current')
llc2ConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5651, 3, 23, 1, 1), ).setIndexNames((0, "MAIPU-LLC2-MIB", "llc2IfIndex"))
if mibBuilder.loadTexts: llc2ConfEntry.setStatus('current')
llc2IfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5651, 3, 23, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llc2IfIndex.setStatus('current')
llc2Group = MibTableColumn((1, 3, 6, 1, 4, 1, 5651, 3, 23, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: llc2Group.setStatus('current')
llc2Status = MibTableColumn((1, 3, 6, 1, 4, 1, 5651, 3, 23, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: llc2Status.setStatus('current')
mibBuilder.exportSymbols("MAIPU-LLC2-MIB", llc2ConfEntry=llc2ConfEntry, llc2IfIndex=llc2IfIndex, mpLlc2Mib=mpLlc2Mib, llc2Status=llc2Status, llc2ConfTable=llc2ConfTable, llc2Group=llc2Group, PYSNMP_MODULE_ID=mpLlc2Mib)
