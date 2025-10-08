#
# PySNMP MIB module MAIPU-LLC2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/maipu/MAIPU-LLC2-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:59 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mpMgmt, = mibBuilder.importSymbols("MAIPU-SMI", "mpMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("MAIPU-LLC2-MIB", llc2ConfTable=llc2ConfTable, PYSNMP_MODULE_ID=mpLlc2Mib, mpLlc2Mib=mpLlc2Mib, llc2IfIndex=llc2IfIndex, llc2Status=llc2Status, llc2Group=llc2Group, llc2ConfEntry=llc2ConfEntry)
