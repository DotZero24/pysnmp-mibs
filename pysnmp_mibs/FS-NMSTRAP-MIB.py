#
# PySNMP MIB module FS-NMSTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fscom/FS-NMSTRAP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:42 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
adslPtInCRC, adslPtSpeed, adslPtOutPkts, adslPtInPkts, adslProductID, adslPtInSpeed, adslLineUser, adslPtInError, adslPtOutDrop, adslPtStatus, adslPtOutSpeed, adslPtInDrop, adslCPULoad, adslPtOutError, adslMemLoad, adslConfigAddr = mibBuilder.importSymbols("FS-NMS-1705", "adslPtInCRC", "adslPtSpeed", "adslPtOutPkts", "adslPtInPkts", "adslProductID", "adslPtInSpeed", "adslLineUser", "adslPtInError", "adslPtOutDrop", "adslPtStatus", "adslPtOutSpeed", "adslPtInDrop", "adslCPULoad", "adslPtOutError", "adslMemLoad", "adslConfigAddr")
nms, = mibBuilder.importSymbols("FS-NMS-SMI", "nms")
ifIndex, ifType, ifDescr = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifType", "ifDescr")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
ModuleIdentity, NotificationType, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adslConnection = NotificationType((1, 3, 6, 1, 4, 1, 52642) + (0,0)).setObjects(("FS-NMS-1705", "adslLineUser"), ("FS-NMS-1705", "adslProductID"), ("FS-NMS-1705", "adslConfigAddr"))
adslPeriod = NotificationType((1, 3, 6, 1, 4, 1, 52642) + (0,1)).setObjects(("FS-NMS-1705", "adslMemLoad"), ("FS-NMS-1705", "adslCPULoad"), ("FS-NMS-1705", "adslPtInCRC"), ("FS-NMS-1705", "adslPtStatus"), ("FS-NMS-1705", "adslPtSpeed"), ("FS-NMS-1705", "adslPtOutPkts"), ("FS-NMS-1705", "adslPtInPkts"), ("FS-NMS-1705", "adslPtOutError"), ("FS-NMS-1705", "adslPtInError"), ("FS-NMS-1705", "adslPtOutSpeed"), ("FS-NMS-1705", "adslPtInSpeed"), ("FS-NMS-1705", "adslPtOutDrop"), ("FS-NMS-1705", "adslPtInDrop"))
mibBuilder.exportSymbols("FS-NMSTRAP-MIB", adslPeriod=adslPeriod, adslConnection=adslConnection)
