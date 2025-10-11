# SNMP MIB module (ADTRAN-DSX1COMMON-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-DSX1COMMON-TRAPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:30:57 2025
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

(adIdentityShared,
 adShared) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentityShared",
    "adShared")

(adTAeSCUTrapAlarmLevel,) = mibBuilder.importSymbols(
    "ADTRAN-TAeSCUEXT1-MIB",
    "adTAeSCUTrapAlarmLevel")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

adDSX1commonTrapsModuleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 29)
)
if mibBuilder.loadTexts:
    adDSX1commonTrapsModuleIdentity.setRevisions(
        ("2014-02-28 00:00",
         "2007-10-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdDSX1CommonTraps_ObjectIdentity = ObjectIdentity
adDSX1CommonTraps = _AdDSX1CommonTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 29)
)
_AdDSX1CommonAlmTraps_ObjectIdentity = ObjectIdentity
adDSX1CommonAlmTraps = _AdDSX1CommonAlmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0)
)
_AdDSX1CommonTrapsMibConformance_ObjectIdentity = ObjectIdentity
adDSX1CommonTrapsMibConformance = _AdDSX1CommonTrapsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 2)
)
_AdDSX1CommonTrapsMibGroups_ObjectIdentity = ObjectIdentity
adDSX1CommonTrapsMibGroups = _AdDSX1CommonTrapsMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 2, 1)
)

# Managed Objects groups


# Notification objects

dsx1almcondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002901)
)
dsx1almcondition.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almcondition.setStatus(
        "current"
    )

dsx1SAalmLOSClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002902)
)
dsx1SAalmLOSClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAalmLOSClear.setStatus(
        "current"
    )

dsx1SAalmLOSActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002903)
)
dsx1SAalmLOSActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAalmLOSActive.setStatus(
        "current"
    )

dsx1SAalmLOFClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002904)
)
dsx1SAalmLOFClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAalmLOFClear.setStatus(
        "current"
    )

dsx1SAalmLOFActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002905)
)
dsx1SAalmLOFActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAalmLOFActive.setStatus(
        "current"
    )

dsx1SAalmAISClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002906)
)
dsx1SAalmAISClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAalmAISClear.setStatus(
        "current"
    )

dsx1SAalmAISActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002907)
)
dsx1SAalmAISActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAalmAISActive.setStatus(
        "current"
    )

dsx1SAalmRAIClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002908)
)
dsx1SAalmRAIClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAalmRAIClear.setStatus(
        "current"
    )

dsx1SAalmRAIActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002909)
)
dsx1SAalmRAIActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAalmRAIActive.setStatus(
        "current"
    )

dsx1loopbackcondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002911)
)
dsx1loopbackcondition.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1loopbackcondition.setStatus(
        "current"
    )

dsx1NSAINFOFarShelfRFIClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002912)
)
dsx1NSAINFOFarShelfRFIClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAINFOFarShelfRFIClear.setStatus(
        "current"
    )

dsx1NSAINFOFarShelfRFIActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002913)
)
dsx1NSAINFOFarShelfRFIActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAINFOFarShelfRFIActive.setStatus(
        "current"
    )

dsx1NSAINFODTLKFailINCClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002914)
)
dsx1NSAINFODTLKFailINCClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAINFODTLKFailINCClear.setStatus(
        "current"
    )

dsx1NSAINFODTLKFailINCActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002915)
)
dsx1NSAINFODTLKFailINCActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAINFODTLKFailINCActive.setStatus(
        "current"
    )

dsx1SAalmBPVClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002916)
)
dsx1SAalmBPVClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAalmBPVClear.setStatus(
        "current"
    )

dsx1SAalmBPVActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002917)
)
dsx1SAalmBPVActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAalmBPVActive.setStatus(
        "current"
    )

dsx1SAalmFarShelfRFIClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002918)
)
dsx1SAalmFarShelfRFIClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAalmFarShelfRFIClear.setStatus(
        "current"
    )

dsx1SAalmFarShelfRFIActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002919)
)
dsx1SAalmFarShelfRFIActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAalmFarShelfRFIActive.setStatus(
        "current"
    )

dsx1SAalmDTLKFailINCClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002920)
)
dsx1SAalmDTLKFailINCClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAalmDTLKFailINCClear.setStatus(
        "current"
    )

dsx1SAalmDTLKFailINCActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002921)
)
dsx1SAalmDTLKFailINCActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAalmDTLKFailINCActive.setStatus(
        "current"
    )

dsx1NSAalmLOSClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002922)
)
dsx1NSAalmLOSClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmLOSClear.setStatus(
        "current"
    )

dsx1NSAalmLOSActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002923)
)
dsx1NSAalmLOSActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmLOSActive.setStatus(
        "current"
    )

dsx1NSAalmLOFClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002924)
)
dsx1NSAalmLOFClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmLOFClear.setStatus(
        "current"
    )

dsx1NSAalmLOFActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002925)
)
dsx1NSAalmLOFActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmLOFActive.setStatus(
        "current"
    )

dsx1NSAalmAISClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002926)
)
dsx1NSAalmAISClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmAISClear.setStatus(
        "current"
    )

dsx1NSAalmAISActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002927)
)
dsx1NSAalmAISActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmAISActive.setStatus(
        "current"
    )

dsx1NSAalmRAIClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002928)
)
dsx1NSAalmRAIClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmRAIClear.setStatus(
        "current"
    )

dsx1NSAalmRAIActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002929)
)
dsx1NSAalmRAIActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmRAIActive.setStatus(
        "current"
    )

dsx1SAFarLoopLPBKDS1FEACClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002932)
)
dsx1SAFarLoopLPBKDS1FEACClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAFarLoopLPBKDS1FEACClear.setStatus(
        "current"
    )

dsx1SAFarLoopLPBKDS1FEACActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002933)
)
dsx1SAFarLoopLPBKDS1FEACActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAFarLoopLPBKDS1FEACActive.setStatus(
        "current"
    )

dsx1NSAalmBPVClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002936)
)
dsx1NSAalmBPVClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmBPVClear.setStatus(
        "current"
    )

dsx1NSAalmBPVActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002937)
)
dsx1NSAalmBPVActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmBPVActive.setStatus(
        "current"
    )

dsx1NSAalmFarShelfRFIClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002938)
)
dsx1NSAalmFarShelfRFIClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmFarShelfRFIClear.setStatus(
        "current"
    )

dsx1NSAalmFarShelfRFIActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002939)
)
dsx1NSAalmFarShelfRFIActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmFarShelfRFIActive.setStatus(
        "current"
    )

dsx1NSAalmDTLKFailINCClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002940)
)
dsx1NSAalmDTLKFailINCClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmDTLKFailINCClear.setStatus(
        "current"
    )

dsx1NSAalmDTLKFailINCActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002941)
)
dsx1NSAalmDTLKFailINCActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmDTLKFailINCActive.setStatus(
        "current"
    )

dsx1NSAT1WKSWPRClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002942)
)
dsx1NSAT1WKSWPRClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAT1WKSWPRClear.setStatus(
        "current"
    )

dsx1NSAT1WKSWPRActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002943)
)
dsx1NSAT1WKSWPRActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAT1WKSWPRActive.setStatus(
        "current"
    )

dsx1NSAalmSYNCPRIClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002944)
)
dsx1NSAalmSYNCPRIClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmSYNCPRIClear.setStatus(
        "current"
    )

dsx1NSAalmSYNCPRIActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002945)
)
dsx1NSAalmSYNCPRIActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmSYNCPRIActive.setStatus(
        "current"
    )

dsx1NSAalmSYNCSECClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002946)
)
dsx1NSAalmSYNCSECClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmSYNCSECClear.setStatus(
        "current"
    )

dsx1NSAalmSYNCSECActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002947)
)
dsx1NSAalmSYNCSECActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmSYNCSECActive.setStatus(
        "current"
    )

dsx1SAalmLPBKLOCALClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002948)
)
dsx1SAalmLPBKLOCALClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAalmLPBKLOCALClear.setStatus(
        "current"
    )

dsx1SAalmLPBKLOCALActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002949)
)
dsx1SAalmLPBKLOCALActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAalmLPBKLOCALActive.setStatus(
        "current"
    )

dsx1SAalmLPBKLINEClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002950)
)
dsx1SAalmLPBKLINEClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAalmLPBKLINEClear.setStatus(
        "current"
    )

dsx1SAalmLPBKLINEActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002951)
)
dsx1SAalmLPBKLINEActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAalmLPBKLINEActive.setStatus(
        "current"
    )

dsx1SAalmLPBKPAYLOADClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002952)
)
dsx1SAalmLPBKPAYLOADClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAalmLPBKPAYLOADClear.setStatus(
        "current"
    )

dsx1SAalmLPBKPAYLOADActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002953)
)
dsx1SAalmLPBKPAYLOADActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAalmLPBKPAYLOADActive.setStatus(
        "current"
    )

dsx1NSAalmLPBKLOCALClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002954)
)
dsx1NSAalmLPBKLOCALClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmLPBKLOCALClear.setStatus(
        "current"
    )

dsx1NSAalmLPBKLOCALActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002955)
)
dsx1NSAalmLPBKLOCALActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmLPBKLOCALActive.setStatus(
        "current"
    )

dsx1NSAalmLPBKLINEClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002956)
)
dsx1NSAalmLPBKLINEClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmLPBKLINEClear.setStatus(
        "current"
    )

dsx1NSAalmLPBKLINEActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002957)
)
dsx1NSAalmLPBKLINEActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmLPBKLINEActive.setStatus(
        "current"
    )

dsx1NSAalmLPBKPAYLOADClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002958)
)
dsx1NSAalmLPBKPAYLOADClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmLPBKPAYLOADClear.setStatus(
        "current"
    )

dsx1NSAalmLPBKPAYLOADActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002959)
)
dsx1NSAalmLPBKPAYLOADActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmLPBKPAYLOADActive.setStatus(
        "current"
    )

dsx1SAalmSYNCOOSClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002960)
)
dsx1SAalmSYNCOOSClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAalmSYNCOOSClear.setStatus(
        "current"
    )

dsx1SAalmSYNCOOSActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002961)
)
dsx1SAalmSYNCOOSActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAalmSYNCOOSActive.setStatus(
        "current"
    )

dsx1NSAalmPHTLClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002962)
)
dsx1NSAalmPHTLClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmPHTLClear.setStatus(
        "current"
    )

dsx1NSAalmPHTLActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002963)
)
dsx1NSAalmPHTLActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmPHTLActive.setStatus(
        "current"
    )

dsx1NSAalmATBClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002964)
)
dsx1NSAalmATBClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmATBClear.setStatus(
        "current"
    )

dsx1NSAalmATBActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002965)
)
dsx1NSAalmATBActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmATBActive.setStatus(
        "current"
    )

dsx1NSAalmNoDS0AvailableClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002966)
)
dsx1NSAalmNoDS0AvailableClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmNoDS0AvailableClear.setStatus(
        "current"
    )

dsx1NSAalmNoDS0AvailableActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002967)
)
dsx1NSAalmNoDS0AvailableActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmNoDS0AvailableActive.setStatus(
        "current"
    )

dsx1NSAalmInvalidSlotClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002968)
)
dsx1NSAalmInvalidSlotClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmInvalidSlotClear.setStatus(
        "current"
    )

dsx1NSAalmInvalidSlotActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002969)
)
dsx1NSAalmInvalidSlotActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmInvalidSlotActive.setStatus(
        "current"
    )

dsx1SAalmTAUFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002970)
)
dsx1SAalmTAUFailureClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAalmTAUFailureClear.setStatus(
        "current"
    )

dsx1SAalmTAUFailureActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002971)
)
dsx1SAalmTAUFailureActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAalmTAUFailureActive.setStatus(
        "current"
    )

dsx1SAalmPCMFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002972)
)
dsx1SAalmPCMFailureClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAalmPCMFailureClear.setStatus(
        "current"
    )

dsx1SAalmPCMFailureActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002973)
)
dsx1SAalmPCMFailureActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAalmPCMFailureActive.setStatus(
        "current"
    )

dsx1SAalmLOMFClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002974)
)
dsx1SAalmLOMFClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAalmLOMFClear.setStatus(
        "current"
    )

dsx1SAalmLOMFActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002975)
)
dsx1SAalmLOMFActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1SAalmLOMFActive.setStatus(
        "current"
    )

dsx1EnhancedSAalmLOSClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002976)
)
dsx1EnhancedSAalmLOSClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    dsx1EnhancedSAalmLOSClear.setStatus(
        "current"
    )

dsx1EnhancedSAalmLOSActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002977)
)
dsx1EnhancedSAalmLOSActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    dsx1EnhancedSAalmLOSActive.setStatus(
        "current"
    )

dsx1EnhancedSAalmLOFClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002978)
)
dsx1EnhancedSAalmLOFClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    dsx1EnhancedSAalmLOFClear.setStatus(
        "current"
    )

dsx1EnhancedSAalmLOFActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002979)
)
dsx1EnhancedSAalmLOFActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    dsx1EnhancedSAalmLOFActive.setStatus(
        "current"
    )

dsx1EnhancedSAalmAISClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002980)
)
dsx1EnhancedSAalmAISClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    dsx1EnhancedSAalmAISClear.setStatus(
        "current"
    )

dsx1EnhancedSAalmAISActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002981)
)
dsx1EnhancedSAalmAISActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    dsx1EnhancedSAalmAISActive.setStatus(
        "current"
    )

dsx1EnhancedSAalmRAIClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002982)
)
dsx1EnhancedSAalmRAIClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    dsx1EnhancedSAalmRAIClear.setStatus(
        "current"
    )

dsx1EnhancedSAalmRAIActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002983)
)
dsx1EnhancedSAalmRAIActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    dsx1EnhancedSAalmRAIActive.setStatus(
        "current"
    )

dsx1SAalmLOSRemoteClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002984)
)
dsx1SAalmLOSRemoteClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    dsx1SAalmLOSRemoteClear.setStatus(
        "current"
    )

dsx1SAalmLOSRemoteActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002985)
)
dsx1SAalmLOSRemoteActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    dsx1SAalmLOSRemoteActive.setStatus(
        "current"
    )

dsx1SAalmLOFRemoteClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002986)
)
dsx1SAalmLOFRemoteClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    dsx1SAalmLOFRemoteClear.setStatus(
        "current"
    )

dsx1SAalmLOFRemoteActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002987)
)
dsx1SAalmLOFRemoteActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    dsx1SAalmLOFRemoteActive.setStatus(
        "current"
    )

dsx1SAalmAISRemoteClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002988)
)
dsx1SAalmAISRemoteClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    dsx1SAalmAISRemoteClear.setStatus(
        "current"
    )

dsx1SAalmAISRemoteActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002989)
)
dsx1SAalmAISRemoteActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    dsx1SAalmAISRemoteActive.setStatus(
        "current"
    )

dsx1NSAalmRAIRemoteClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002990)
)
dsx1NSAalmRAIRemoteClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmRAIRemoteClear.setStatus(
        "current"
    )

dsx1NSAalmRAIRemoteActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 0, 1002991)
)
dsx1NSAalmRAIRemoteActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    dsx1NSAalmRAIRemoteActive.setStatus(
        "current"
    )


# Notifications groups

adDSX1CommonTrapsEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 29, 2, 1, 1)
)
adDSX1CommonTrapsEventGroup.setObjects(
      *(("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1almcondition"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmLOSClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmLOSActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmLOFClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmLOFActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmAISClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmAISActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmRAIClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmRAIActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1loopbackcondition"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAINFOFarShelfRFIClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAINFOFarShelfRFIActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAINFODTLKFailINCClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAINFODTLKFailINCActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmBPVClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmBPVActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmFarShelfRFIClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmFarShelfRFIActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmDTLKFailINCClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmDTLKFailINCActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmLOSClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmLOSActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmLOFClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmLOFActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmAISClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmAISActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmRAIClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmRAIActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAFarLoopLPBKDS1FEACClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAFarLoopLPBKDS1FEACActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmBPVClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmBPVActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmFarShelfRFIClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmFarShelfRFIActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmDTLKFailINCClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmDTLKFailINCActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAT1WKSWPRClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAT1WKSWPRActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmSYNCPRIClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmSYNCPRIActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmSYNCSECClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmSYNCSECActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmLPBKLOCALClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmLPBKLOCALActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmLPBKLINEClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmLPBKLINEActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmLPBKPAYLOADClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmLPBKPAYLOADActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmLPBKLOCALClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmLPBKLOCALActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmLPBKLINEClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmLPBKLINEActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmLPBKPAYLOADClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmLPBKPAYLOADActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmSYNCOOSClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmSYNCOOSActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmPHTLClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmPHTLActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmATBClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmATBActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmNoDS0AvailableClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmNoDS0AvailableActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmInvalidSlotClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmInvalidSlotActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmTAUFailureClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmTAUFailureActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmPCMFailureClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmPCMFailureActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmLOMFClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmLOMFActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1EnhancedSAalmLOSClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1EnhancedSAalmLOSActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1EnhancedSAalmLOFClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1EnhancedSAalmLOFActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1EnhancedSAalmAISClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1EnhancedSAalmAISActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1EnhancedSAalmRAIClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1EnhancedSAalmRAIActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmLOSRemoteClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmLOSRemoteActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmLOFRemoteClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmLOFRemoteActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmAISRemoteClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1SAalmAISRemoteActive"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmRAIRemoteClear"),
        ("ADTRAN-DSX1COMMON-TRAPS-MIB", "dsx1NSAalmRAIRemoteActive"))
)
if mibBuilder.loadTexts:
    adDSX1CommonTrapsEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-DSX1COMMON-TRAPS-MIB",
    **{"adDSX1CommonTraps": adDSX1CommonTraps,
       "adDSX1CommonAlmTraps": adDSX1CommonAlmTraps,
       "dsx1almcondition": dsx1almcondition,
       "dsx1SAalmLOSClear": dsx1SAalmLOSClear,
       "dsx1SAalmLOSActive": dsx1SAalmLOSActive,
       "dsx1SAalmLOFClear": dsx1SAalmLOFClear,
       "dsx1SAalmLOFActive": dsx1SAalmLOFActive,
       "dsx1SAalmAISClear": dsx1SAalmAISClear,
       "dsx1SAalmAISActive": dsx1SAalmAISActive,
       "dsx1SAalmRAIClear": dsx1SAalmRAIClear,
       "dsx1SAalmRAIActive": dsx1SAalmRAIActive,
       "dsx1loopbackcondition": dsx1loopbackcondition,
       "dsx1NSAINFOFarShelfRFIClear": dsx1NSAINFOFarShelfRFIClear,
       "dsx1NSAINFOFarShelfRFIActive": dsx1NSAINFOFarShelfRFIActive,
       "dsx1NSAINFODTLKFailINCClear": dsx1NSAINFODTLKFailINCClear,
       "dsx1NSAINFODTLKFailINCActive": dsx1NSAINFODTLKFailINCActive,
       "dsx1SAalmBPVClear": dsx1SAalmBPVClear,
       "dsx1SAalmBPVActive": dsx1SAalmBPVActive,
       "dsx1SAalmFarShelfRFIClear": dsx1SAalmFarShelfRFIClear,
       "dsx1SAalmFarShelfRFIActive": dsx1SAalmFarShelfRFIActive,
       "dsx1SAalmDTLKFailINCClear": dsx1SAalmDTLKFailINCClear,
       "dsx1SAalmDTLKFailINCActive": dsx1SAalmDTLKFailINCActive,
       "dsx1NSAalmLOSClear": dsx1NSAalmLOSClear,
       "dsx1NSAalmLOSActive": dsx1NSAalmLOSActive,
       "dsx1NSAalmLOFClear": dsx1NSAalmLOFClear,
       "dsx1NSAalmLOFActive": dsx1NSAalmLOFActive,
       "dsx1NSAalmAISClear": dsx1NSAalmAISClear,
       "dsx1NSAalmAISActive": dsx1NSAalmAISActive,
       "dsx1NSAalmRAIClear": dsx1NSAalmRAIClear,
       "dsx1NSAalmRAIActive": dsx1NSAalmRAIActive,
       "dsx1SAFarLoopLPBKDS1FEACClear": dsx1SAFarLoopLPBKDS1FEACClear,
       "dsx1SAFarLoopLPBKDS1FEACActive": dsx1SAFarLoopLPBKDS1FEACActive,
       "dsx1NSAalmBPVClear": dsx1NSAalmBPVClear,
       "dsx1NSAalmBPVActive": dsx1NSAalmBPVActive,
       "dsx1NSAalmFarShelfRFIClear": dsx1NSAalmFarShelfRFIClear,
       "dsx1NSAalmFarShelfRFIActive": dsx1NSAalmFarShelfRFIActive,
       "dsx1NSAalmDTLKFailINCClear": dsx1NSAalmDTLKFailINCClear,
       "dsx1NSAalmDTLKFailINCActive": dsx1NSAalmDTLKFailINCActive,
       "dsx1NSAT1WKSWPRClear": dsx1NSAT1WKSWPRClear,
       "dsx1NSAT1WKSWPRActive": dsx1NSAT1WKSWPRActive,
       "dsx1NSAalmSYNCPRIClear": dsx1NSAalmSYNCPRIClear,
       "dsx1NSAalmSYNCPRIActive": dsx1NSAalmSYNCPRIActive,
       "dsx1NSAalmSYNCSECClear": dsx1NSAalmSYNCSECClear,
       "dsx1NSAalmSYNCSECActive": dsx1NSAalmSYNCSECActive,
       "dsx1SAalmLPBKLOCALClear": dsx1SAalmLPBKLOCALClear,
       "dsx1SAalmLPBKLOCALActive": dsx1SAalmLPBKLOCALActive,
       "dsx1SAalmLPBKLINEClear": dsx1SAalmLPBKLINEClear,
       "dsx1SAalmLPBKLINEActive": dsx1SAalmLPBKLINEActive,
       "dsx1SAalmLPBKPAYLOADClear": dsx1SAalmLPBKPAYLOADClear,
       "dsx1SAalmLPBKPAYLOADActive": dsx1SAalmLPBKPAYLOADActive,
       "dsx1NSAalmLPBKLOCALClear": dsx1NSAalmLPBKLOCALClear,
       "dsx1NSAalmLPBKLOCALActive": dsx1NSAalmLPBKLOCALActive,
       "dsx1NSAalmLPBKLINEClear": dsx1NSAalmLPBKLINEClear,
       "dsx1NSAalmLPBKLINEActive": dsx1NSAalmLPBKLINEActive,
       "dsx1NSAalmLPBKPAYLOADClear": dsx1NSAalmLPBKPAYLOADClear,
       "dsx1NSAalmLPBKPAYLOADActive": dsx1NSAalmLPBKPAYLOADActive,
       "dsx1SAalmSYNCOOSClear": dsx1SAalmSYNCOOSClear,
       "dsx1SAalmSYNCOOSActive": dsx1SAalmSYNCOOSActive,
       "dsx1NSAalmPHTLClear": dsx1NSAalmPHTLClear,
       "dsx1NSAalmPHTLActive": dsx1NSAalmPHTLActive,
       "dsx1NSAalmATBClear": dsx1NSAalmATBClear,
       "dsx1NSAalmATBActive": dsx1NSAalmATBActive,
       "dsx1NSAalmNoDS0AvailableClear": dsx1NSAalmNoDS0AvailableClear,
       "dsx1NSAalmNoDS0AvailableActive": dsx1NSAalmNoDS0AvailableActive,
       "dsx1NSAalmInvalidSlotClear": dsx1NSAalmInvalidSlotClear,
       "dsx1NSAalmInvalidSlotActive": dsx1NSAalmInvalidSlotActive,
       "dsx1SAalmTAUFailureClear": dsx1SAalmTAUFailureClear,
       "dsx1SAalmTAUFailureActive": dsx1SAalmTAUFailureActive,
       "dsx1SAalmPCMFailureClear": dsx1SAalmPCMFailureClear,
       "dsx1SAalmPCMFailureActive": dsx1SAalmPCMFailureActive,
       "dsx1SAalmLOMFClear": dsx1SAalmLOMFClear,
       "dsx1SAalmLOMFActive": dsx1SAalmLOMFActive,
       "dsx1EnhancedSAalmLOSClear": dsx1EnhancedSAalmLOSClear,
       "dsx1EnhancedSAalmLOSActive": dsx1EnhancedSAalmLOSActive,
       "dsx1EnhancedSAalmLOFClear": dsx1EnhancedSAalmLOFClear,
       "dsx1EnhancedSAalmLOFActive": dsx1EnhancedSAalmLOFActive,
       "dsx1EnhancedSAalmAISClear": dsx1EnhancedSAalmAISClear,
       "dsx1EnhancedSAalmAISActive": dsx1EnhancedSAalmAISActive,
       "dsx1EnhancedSAalmRAIClear": dsx1EnhancedSAalmRAIClear,
       "dsx1EnhancedSAalmRAIActive": dsx1EnhancedSAalmRAIActive,
       "dsx1SAalmLOSRemoteClear": dsx1SAalmLOSRemoteClear,
       "dsx1SAalmLOSRemoteActive": dsx1SAalmLOSRemoteActive,
       "dsx1SAalmLOFRemoteClear": dsx1SAalmLOFRemoteClear,
       "dsx1SAalmLOFRemoteActive": dsx1SAalmLOFRemoteActive,
       "dsx1SAalmAISRemoteClear": dsx1SAalmAISRemoteClear,
       "dsx1SAalmAISRemoteActive": dsx1SAalmAISRemoteActive,
       "dsx1NSAalmRAIRemoteClear": dsx1NSAalmRAIRemoteClear,
       "dsx1NSAalmRAIRemoteActive": dsx1NSAalmRAIRemoteActive,
       "adDSX1CommonTrapsMibConformance": adDSX1CommonTrapsMibConformance,
       "adDSX1CommonTrapsMibGroups": adDSX1CommonTrapsMibGroups,
       "adDSX1CommonTrapsEventGroup": adDSX1CommonTrapsEventGroup,
       "adDSX1commonTrapsModuleIdentity": adDSX1commonTrapsModuleIdentity}
)
