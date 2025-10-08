#
# PySNMP MIB module HPN-ICF-LswSMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HPN-ICF-LswSMON-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:34 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpnicfRhw, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfRhw")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfSmonExtend = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 26))
hpnicfsmonExtendObject = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 26, 1))
hpnicfdot1qVlanStatNumber = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 26, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1qVlanStatNumber.setStatus('mandatory')
hpnicfdot1qVlanStatStatusTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 26, 1, 2), )
if mibBuilder.loadTexts: hpnicfdot1qVlanStatStatusTable.setStatus('mandatory')
hpnicfdot1qVlanStatStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 26, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-LswSMON-MIB", "hpnicfdot1qVlanStatEnableIndex"))
if mibBuilder.loadTexts: hpnicfdot1qVlanStatStatusEntry.setStatus('mandatory')
hpnicfdot1qVlanStatEnableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 26, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1qVlanStatEnableIndex.setStatus('mandatory')
hpnicfdot1qVlanStatEnableStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 26, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1qVlanStatEnableStatus.setStatus('mandatory')
mibBuilder.exportSymbols("HPN-ICF-LswSMON-MIB", hpnicfdot1qVlanStatStatusEntry=hpnicfdot1qVlanStatStatusEntry, hpnicfSmonExtend=hpnicfSmonExtend, hpnicfsmonExtendObject=hpnicfsmonExtendObject, hpnicfdot1qVlanStatEnableStatus=hpnicfdot1qVlanStatEnableStatus, hpnicfdot1qVlanStatEnableIndex=hpnicfdot1qVlanStatEnableIndex, hpnicfdot1qVlanStatStatusTable=hpnicfdot1qVlanStatStatusTable, hpnicfdot1qVlanStatNumber=hpnicfdot1qVlanStatNumber)
