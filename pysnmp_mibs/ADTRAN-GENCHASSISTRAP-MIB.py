# SNMP MIB module (ADTRAN-GENCHASSISTRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENCHASSISTRAP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:30:39 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(adGenericShelves,) = mibBuilder.importSymbols(
    "ADTRAN-GENCHASSIS-MIB",
    "adGenericShelves")

(adGenPortTrapIdentifier,) = mibBuilder.importSymbols(
    "ADTRAN-GENPORT-MIB",
    "adGenPortTrapIdentifier")

(adGenSlotAlarmStatus,
 adGenSlotInfoIndex) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotAlarmStatus",
    "adGenSlotInfoIndex")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 NotificationType,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

adCtrpCardInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 0, 1001302)
)
adCtrpCardInserted.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adCtrpCardInserted.setStatus(
        ""
    )

adCtrpCardRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 0, 1001303)
)
adCtrpCardRemoved.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adCtrpCardRemoved.setStatus(
        ""
    )

adCtrpBlownFuse = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 0, 1001305)
)
adCtrpBlownFuse.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adCtrpBlownFuse.setStatus(
        ""
    )

adCtrpRmtAlmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 0, 1001308)
)
adCtrpRmtAlmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adCtrpRmtAlmClear.setStatus(
        ""
    )

adCtrpRmtAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 0, 1001309)
)
adCtrpRmtAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adCtrpRmtAlm.setStatus(
        ""
    )

adCtrpExt1AlmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 0, 1001310)
)
adCtrpExt1AlmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adCtrpExt1AlmClear.setStatus(
        ""
    )

adCtrpExt1Alm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 0, 1001311)
)
adCtrpExt1Alm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adCtrpExt1Alm.setStatus(
        ""
    )

adCtrpExt2AlmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 0, 1001312)
)
adCtrpExt2AlmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adCtrpExt2AlmClear.setStatus(
        ""
    )

adCtrpExt2Alm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 0, 1001313)
)
adCtrpExt2Alm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adCtrpExt2Alm.setStatus(
        ""
    )

adCtrpBusApwrAlmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 0, 1001314)
)
adCtrpBusApwrAlmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adCtrpBusApwrAlmClear.setStatus(
        ""
    )

adCtrpBusApowerAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 0, 1001315)
)
adCtrpBusApowerAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adCtrpBusApowerAlm.setStatus(
        ""
    )

adCtrpBusBpwrAlmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 0, 1001316)
)
adCtrpBusBpwrAlmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adCtrpBusBpwrAlmClear.setStatus(
        ""
    )

adCtrpBusBpowerAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 0, 1001317)
)
adCtrpBusBpowerAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adCtrpBusBpowerAlm.setStatus(
        ""
    )

adCtrpInService = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 0, 1001318)
)
adCtrpInService.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adCtrpInService.setStatus(
        ""
    )

adCtrpOutOfService = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 0, 1001319)
)
adCtrpOutOfService.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adCtrpOutOfService.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENCHASSISTRAP-MIB",
    **{"adCtrpCardInserted": adCtrpCardInserted,
       "adCtrpCardRemoved": adCtrpCardRemoved,
       "adCtrpBlownFuse": adCtrpBlownFuse,
       "adCtrpRmtAlmClear": adCtrpRmtAlmClear,
       "adCtrpRmtAlm": adCtrpRmtAlm,
       "adCtrpExt1AlmClear": adCtrpExt1AlmClear,
       "adCtrpExt1Alm": adCtrpExt1Alm,
       "adCtrpExt2AlmClear": adCtrpExt2AlmClear,
       "adCtrpExt2Alm": adCtrpExt2Alm,
       "adCtrpBusApwrAlmClear": adCtrpBusApwrAlmClear,
       "adCtrpBusApowerAlm": adCtrpBusApowerAlm,
       "adCtrpBusBpwrAlmClear": adCtrpBusBpwrAlmClear,
       "adCtrpBusBpowerAlm": adCtrpBusBpowerAlm,
       "adCtrpInService": adCtrpInService,
       "adCtrpOutOfService": adCtrpOutOfService}
)
