#
# PySNMP MIB module HUAWEI-LswSMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/h3c/HUAWEI-LswSMON-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:22:44 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
huaweiDatacomm, huaweiMgmt = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "huaweiDatacomm", "huaweiMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hwSmonExtend = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 26))
smonExtendObject = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 26, 1))
hwdot1qVlanStatNumber = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 26, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qVlanStatNumber.setStatus('mandatory')
hwdot1qVlanStatStatusTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 26, 1, 2), )
if mibBuilder.loadTexts: hwdot1qVlanStatStatusTable.setStatus('mandatory')
hwdot1qVlanStatStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 26, 1, 2, 1), ).setIndexNames((0, "HUAWEI-LswSMON-MIB", "hwdot1qVlanStatEnableIndex"))
if mibBuilder.loadTexts: hwdot1qVlanStatStatusEntry.setStatus('mandatory')
hwdot1qVlanStatEnableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 26, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qVlanStatEnableIndex.setStatus('mandatory')
hwdot1qVlanStatEnableStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 26, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qVlanStatEnableStatus.setStatus('mandatory')
mibBuilder.exportSymbols("HUAWEI-LswSMON-MIB", hwdot1qVlanStatEnableIndex=hwdot1qVlanStatEnableIndex, smonExtendObject=smonExtendObject, hwdot1qVlanStatStatusEntry=hwdot1qVlanStatStatusEntry, hwdot1qVlanStatNumber=hwdot1qVlanStatNumber, hwSmonExtend=hwSmonExtend, hwdot1qVlanStatStatusTable=hwdot1qVlanStatStatusTable, hwdot1qVlanStatEnableStatus=hwdot1qVlanStatEnableStatus)
