#
# PySNMP MIB module QTECH-NMSTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/qtech/QTECH-NMSTRAP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:21 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, ifType, ifDescr = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifType", "ifDescr")
adslPtInCRC, adslPtSpeed, adslPtOutPkts, adslPtInPkts, adslProductID, adslPtInSpeed, adslLineUser, adslPtInError, adslPtOutDrop, adslPtStatus, adslPtOutSpeed, adslPtInDrop, adslCPULoad, adslPtOutError, adslMemLoad, adslConfigAddr = mibBuilder.importSymbols("QTECH-NMS-1705", "adslPtInCRC", "adslPtSpeed", "adslPtOutPkts", "adslPtInPkts", "adslProductID", "adslPtInSpeed", "adslLineUser", "adslPtInError", "adslPtOutDrop", "adslPtStatus", "adslPtOutSpeed", "adslPtInDrop", "adslCPULoad", "adslPtOutError", "adslMemLoad", "adslConfigAddr")
nms, = mibBuilder.importSymbols("QTECH-NMS-SMI", "nms")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
ModuleIdentity, NotificationType, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adslConnection = NotificationType((1, 3, 6, 1, 4, 1, 34751) + (0,0)).setObjects(("QTECH-NMS-1705", "adslLineUser"), ("QTECH-NMS-1705", "adslProductID"), ("QTECH-NMS-1705", "adslConfigAddr"))
adslPeriod = NotificationType((1, 3, 6, 1, 4, 1, 34751) + (0,1)).setObjects(("QTECH-NMS-1705", "adslMemLoad"), ("QTECH-NMS-1705", "adslCPULoad"), ("QTECH-NMS-1705", "adslPtInCRC"), ("QTECH-NMS-1705", "adslPtStatus"), ("QTECH-NMS-1705", "adslPtSpeed"), ("QTECH-NMS-1705", "adslPtOutPkts"), ("QTECH-NMS-1705", "adslPtInPkts"), ("QTECH-NMS-1705", "adslPtOutError"), ("QTECH-NMS-1705", "adslPtInError"), ("QTECH-NMS-1705", "adslPtOutSpeed"), ("QTECH-NMS-1705", "adslPtInSpeed"), ("QTECH-NMS-1705", "adslPtOutDrop"), ("QTECH-NMS-1705", "adslPtInDrop"))
mibBuilder.exportSymbols("QTECH-NMSTRAP-MIB", adslPeriod=adslPeriod, adslConnection=adslConnection)
