#
# PySNMP MIB module A3COM-HUAWEI-LswSMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/a3com/A3COM-HUAWEI-LswSMON-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:01 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
huaweiDatacomm, huaweiMgmt = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "huaweiDatacomm", "huaweiMgmt")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hwSmonExtend = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 26))
smonExtendObject = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 26, 1))
hwdot1qVlanStatNumber = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 26, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qVlanStatNumber.setStatus('mandatory')
hwdot1qVlanStatStatusTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 26, 1, 2), )
if mibBuilder.loadTexts: hwdot1qVlanStatStatusTable.setStatus('mandatory')
hwdot1qVlanStatStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 26, 1, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-LswSMON-MIB", "hwdot1qVlanStatEnableIndex"))
if mibBuilder.loadTexts: hwdot1qVlanStatStatusEntry.setStatus('mandatory')
hwdot1qVlanStatEnableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 26, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qVlanStatEnableIndex.setStatus('mandatory')
hwdot1qVlanStatEnableStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 26, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qVlanStatEnableStatus.setStatus('mandatory')
mibBuilder.exportSymbols("A3COM-HUAWEI-LswSMON-MIB", hwdot1qVlanStatStatusEntry=hwdot1qVlanStatStatusEntry, hwdot1qVlanStatEnableIndex=hwdot1qVlanStatEnableIndex, hwSmonExtend=hwSmonExtend, smonExtendObject=smonExtendObject, hwdot1qVlanStatStatusTable=hwdot1qVlanStatStatusTable, hwdot1qVlanStatNumber=hwdot1qVlanStatNumber, hwdot1qVlanStatEnableStatus=hwdot1qVlanStatEnableStatus)
