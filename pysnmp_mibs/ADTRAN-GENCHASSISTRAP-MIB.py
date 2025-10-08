#
# PySNMP MIB module ADTRAN-GENCHASSISTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/adtran/ADTRAN-GENCHASSISTRAP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:52:26 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
adGenericShelves, = mibBuilder.importSymbols("ADTRAN-GENCHASSIS-MIB", "adGenericShelves")
adGenPortTrapIdentifier, = mibBuilder.importSymbols("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier")
adGenSlotAlarmStatus, adGenSlotInfoIndex = mibBuilder.importSymbols("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus", "adGenSlotInfoIndex")
adTrapInformSeqNum, = mibBuilder.importSymbols("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adCtrpCardInserted = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 13) + (0,1001302)).setObjects(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"), ("SNMPv2-MIB", "sysName"), ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
adCtrpCardRemoved = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 13) + (0,1001303)).setObjects(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"), ("SNMPv2-MIB", "sysName"), ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
adCtrpBlownFuse = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 13) + (0,1001305)).setObjects(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"), ("SNMPv2-MIB", "sysName"), ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
adCtrpRmtAlmClear = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 13) + (0,1001308)).setObjects(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"), ("SNMPv2-MIB", "sysName"))
adCtrpRmtAlm = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 13) + (0,1001309)).setObjects(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"), ("SNMPv2-MIB", "sysName"))
adCtrpExt1AlmClear = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 13) + (0,1001310)).setObjects(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"), ("SNMPv2-MIB", "sysName"))
adCtrpExt1Alm = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 13) + (0,1001311)).setObjects(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"), ("SNMPv2-MIB", "sysName"))
adCtrpExt2AlmClear = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 13) + (0,1001312)).setObjects(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"), ("SNMPv2-MIB", "sysName"))
adCtrpExt2Alm = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 13) + (0,1001313)).setObjects(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"), ("SNMPv2-MIB", "sysName"))
adCtrpBusApwrAlmClear = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 13) + (0,1001314)).setObjects(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"), ("SNMPv2-MIB", "sysName"))
adCtrpBusApowerAlm = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 13) + (0,1001315)).setObjects(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"), ("SNMPv2-MIB", "sysName"))
adCtrpBusBpwrAlmClear = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 13) + (0,1001316)).setObjects(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"), ("SNMPv2-MIB", "sysName"))
adCtrpBusBpowerAlm = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 13) + (0,1001317)).setObjects(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"), ("SNMPv2-MIB", "sysName"))
adCtrpInService = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 13) + (0,1001318)).setObjects(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"), ("SNMPv2-MIB", "sysName"), ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
adCtrpOutOfService = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 13) + (0,1001319)).setObjects(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"), ("SNMPv2-MIB", "sysName"), ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
mibBuilder.exportSymbols("ADTRAN-GENCHASSISTRAP-MIB", adCtrpCardRemoved=adCtrpCardRemoved, adCtrpBusApowerAlm=adCtrpBusApowerAlm, adCtrpOutOfService=adCtrpOutOfService, adCtrpExt1Alm=adCtrpExt1Alm, adCtrpBlownFuse=adCtrpBlownFuse, adCtrpExt2Alm=adCtrpExt2Alm, adCtrpCardInserted=adCtrpCardInserted, adCtrpRmtAlm=adCtrpRmtAlm, adCtrpBusApwrAlmClear=adCtrpBusApwrAlmClear, adCtrpInService=adCtrpInService, adCtrpBusBpwrAlmClear=adCtrpBusBpwrAlmClear, adCtrpExt1AlmClear=adCtrpExt1AlmClear, adCtrpExt2AlmClear=adCtrpExt2AlmClear, adCtrpBusBpowerAlm=adCtrpBusBpowerAlm, adCtrpRmtAlmClear=adCtrpRmtAlmClear)
