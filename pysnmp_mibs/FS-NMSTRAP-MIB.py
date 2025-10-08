#
# PySNMP MIB module FS-NMSTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fscom/FS-NMSTRAP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:01:37 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
adslConfigAddr, adslPtOutError, adslMemLoad, adslPtStatus, adslPtSpeed, adslPtOutPkts, adslCPULoad, adslPtOutSpeed, adslPtInCRC, adslPtOutDrop, adslPtInError, adslLineUser, adslProductID, adslPtInDrop, adslPtInPkts, adslPtInSpeed = mibBuilder.importSymbols("FS-NMS-1705", "adslConfigAddr", "adslPtOutError", "adslMemLoad", "adslPtStatus", "adslPtSpeed", "adslPtOutPkts", "adslCPULoad", "adslPtOutSpeed", "adslPtInCRC", "adslPtOutDrop", "adslPtInError", "adslLineUser", "adslProductID", "adslPtInDrop", "adslPtInPkts", "adslPtInSpeed")
nms, = mibBuilder.importSymbols("FS-NMS-SMI", "nms")
ifDescr, ifType, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifDescr", "ifType", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adslConnection = NotificationType((1, 3, 6, 1, 4, 1, 52642) + (0,0)).setObjects(("FS-NMS-1705", "adslLineUser"), ("FS-NMS-1705", "adslProductID"), ("FS-NMS-1705", "adslConfigAddr"))
adslPeriod = NotificationType((1, 3, 6, 1, 4, 1, 52642) + (0,1)).setObjects(("FS-NMS-1705", "adslMemLoad"), ("FS-NMS-1705", "adslCPULoad"), ("FS-NMS-1705", "adslPtInCRC"), ("FS-NMS-1705", "adslPtStatus"), ("FS-NMS-1705", "adslPtSpeed"), ("FS-NMS-1705", "adslPtOutPkts"), ("FS-NMS-1705", "adslPtInPkts"), ("FS-NMS-1705", "adslPtOutError"), ("FS-NMS-1705", "adslPtInError"), ("FS-NMS-1705", "adslPtOutSpeed"), ("FS-NMS-1705", "adslPtInSpeed"), ("FS-NMS-1705", "adslPtOutDrop"), ("FS-NMS-1705", "adslPtInDrop"))
mibBuilder.exportSymbols("FS-NMSTRAP-MIB", adslPeriod=adslPeriod, adslConnection=adslConnection)
