#
# PySNMP MIB module ADTRAN-GENCHASSISTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/adtran/ADTRAN-GENCHASSISTRAP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:29:17 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
adGenericShelves, = mibBuilder.importSymbols("ADTRAN-GENCHASSIS-MIB", "adGenericShelves")
adGenPortTrapIdentifier, = mibBuilder.importSymbols("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier")
adGenSlotInfoIndex, adGenSlotAlarmStatus = mibBuilder.importSymbols("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex", "adGenSlotAlarmStatus")
adTrapInformSeqNum, = mibBuilder.importSymbols("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
ModuleIdentity, NotificationType, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("ADTRAN-GENCHASSISTRAP-MIB", adCtrpBusBpowerAlm=adCtrpBusBpowerAlm, adCtrpCardInserted=adCtrpCardInserted, adCtrpExt2Alm=adCtrpExt2Alm, adCtrpRmtAlmClear=adCtrpRmtAlmClear, adCtrpBusApowerAlm=adCtrpBusApowerAlm, adCtrpInService=adCtrpInService, adCtrpBlownFuse=adCtrpBlownFuse, adCtrpBusBpwrAlmClear=adCtrpBusBpwrAlmClear, adCtrpRmtAlm=adCtrpRmtAlm, adCtrpCardRemoved=adCtrpCardRemoved, adCtrpOutOfService=adCtrpOutOfService, adCtrpExt2AlmClear=adCtrpExt2AlmClear, adCtrpExt1Alm=adCtrpExt1Alm, adCtrpExt1AlmClear=adCtrpExt1AlmClear, adCtrpBusApwrAlmClear=adCtrpBusApwrAlmClear)
