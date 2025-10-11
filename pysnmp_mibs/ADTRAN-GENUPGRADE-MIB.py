# SNMP MIB module (ADTRAN-GENUPGRADE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENUPGRADE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:31:45 2025
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

_AdGenUpgrade_ObjectIdentity = ObjectIdentity
adGenUpgrade = _AdGenUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 4)
)
_AdGenUpgradeStatus_ObjectIdentity = ObjectIdentity
adGenUpgradeStatus = _AdGenUpgradeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 4, 1)
)
_AdGenUpgradeStatusTable_Object = MibTable
adGenUpgradeStatusTable = _AdGenUpgradeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 4, 1, 1)
)
if mibBuilder.loadTexts:
    adGenUpgradeStatusTable.setStatus("mandatory")
_AdGenUpgradeStatusEntry_Object = MibTableRow
adGenUpgradeStatusEntry = _AdGenUpgradeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 4, 1, 1, 1)
)
adGenUpgradeStatusEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenUpgradeStatusEntry.setStatus("mandatory")


class _AdGenUpgradeFailureStatus_Type(Integer32):
    """Custom type adGenUpgradeFailureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noFailure", 1),
          ("genericFailure", 2),
          ("ymodemProtocolFailure", 3),
          ("wrongSoftwareSentFailure", 4),
          ("softwareValidationFailure", 5))
    )


_AdGenUpgradeFailureStatus_Type.__name__ = "Integer32"
_AdGenUpgradeFailureStatus_Object = MibTableColumn
adGenUpgradeFailureStatus = _AdGenUpgradeFailureStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 4, 1, 1, 1, 1),
    _AdGenUpgradeFailureStatus_Type()
)
adGenUpgradeFailureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenUpgradeFailureStatus.setStatus("mandatory")


class _AdGenUpgradeSoftwareStatus_Type(Integer32):
    """Custom type adGenUpgradeSoftwareStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("upgradeNotInProgress", 1),
          ("ymodemNegotiation", 2),
          ("ymodemInProgress", 3),
          ("tftpNegotiation", 4),
          ("tftpInProgress", 5),
          ("validatingSoftware", 6),
          ("erasingEntireSoftware", 7),
          ("erasingNonBootblockSoftware", 8),
          ("writingSoftware", 9),
          ("rebooting", 10))
    )


_AdGenUpgradeSoftwareStatus_Type.__name__ = "Integer32"
_AdGenUpgradeSoftwareStatus_Object = MibTableColumn
adGenUpgradeSoftwareStatus = _AdGenUpgradeSoftwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 4, 1, 1, 1, 2),
    _AdGenUpgradeSoftwareStatus_Type()
)
adGenUpgradeSoftwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenUpgradeSoftwareStatus.setStatus("optional")


class _AdGenUpgradeSoftwarePercentageStatus_Type(Integer32):
    """Custom type adGenUpgradeSoftwarePercentageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 101),
    )


_AdGenUpgradeSoftwarePercentageStatus_Type.__name__ = "Integer32"
_AdGenUpgradeSoftwarePercentageStatus_Object = MibTableColumn
adGenUpgradeSoftwarePercentageStatus = _AdGenUpgradeSoftwarePercentageStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 4, 1, 1, 1, 3),
    _AdGenUpgradeSoftwarePercentageStatus_Type()
)
adGenUpgradeSoftwarePercentageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenUpgradeSoftwarePercentageStatus.setStatus("optional")


class _AdGenUpgradeSwUpgradeability_Type(Integer32):
    """Custom type adGenUpgradeSwUpgradeability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("upgradeable", 1),
          ("notUpgradeable", 2))
    )


_AdGenUpgradeSwUpgradeability_Type.__name__ = "Integer32"
_AdGenUpgradeSwUpgradeability_Object = MibTableColumn
adGenUpgradeSwUpgradeability = _AdGenUpgradeSwUpgradeability_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 4, 1, 1, 1, 4),
    _AdGenUpgradeSwUpgradeability_Type()
)
adGenUpgradeSwUpgradeability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenUpgradeSwUpgradeability.setStatus("mandatory")
_AdGenUpgradeConfig_ObjectIdentity = ObjectIdentity
adGenUpgradeConfig = _AdGenUpgradeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 4, 2)
)
_AdGenUpgradeConfigTable_Object = MibTable
adGenUpgradeConfigTable = _AdGenUpgradeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 4, 2, 1)
)
if mibBuilder.loadTexts:
    adGenUpgradeConfigTable.setStatus("mandatory")
_AdGenUpgradeConfigEntry_Object = MibTableRow
adGenUpgradeConfigEntry = _AdGenUpgradeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 4, 2, 1, 1)
)
adGenUpgradeConfigEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenUpgradeConfigEntry.setStatus("mandatory")


class _AdGenUpgradeSwConfiguration_Type(Integer32):
    """Custom type adGenUpgradeSwConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("mainCodeOnly", 1),
          ("mainAndStandbyCode", 2),
          ("mainCodeWithBootSector", 3),
          ("mainAndStandbyWithBootSector", 4),
          ("noneOfTheAbove", 5))
    )


_AdGenUpgradeSwConfiguration_Type.__name__ = "Integer32"
_AdGenUpgradeSwConfiguration_Object = MibTableColumn
adGenUpgradeSwConfiguration = _AdGenUpgradeSwConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 4, 2, 1, 1, 1),
    _AdGenUpgradeSwConfiguration_Type()
)
adGenUpgradeSwConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenUpgradeSwConfiguration.setStatus("optional")
_AdGenUpgradeSwConfigDescription_Type = DisplayString
_AdGenUpgradeSwConfigDescription_Object = MibTableColumn
adGenUpgradeSwConfigDescription = _AdGenUpgradeSwConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 4, 2, 1, 1, 2),
    _AdGenUpgradeSwConfigDescription_Type()
)
adGenUpgradeSwConfigDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenUpgradeSwConfigDescription.setStatus("optional")
_AdGenUpgradeProdMainSwVersion_Type = DisplayString
_AdGenUpgradeProdMainSwVersion_Object = MibTableColumn
adGenUpgradeProdMainSwVersion = _AdGenUpgradeProdMainSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 4, 2, 1, 1, 3),
    _AdGenUpgradeProdMainSwVersion_Type()
)
adGenUpgradeProdMainSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenUpgradeProdMainSwVersion.setStatus("mandatory")
_AdGenUpgradeProdStandbySwVersion_Type = DisplayString
_AdGenUpgradeProdStandbySwVersion_Object = MibTableColumn
adGenUpgradeProdStandbySwVersion = _AdGenUpgradeProdStandbySwVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 4, 2, 1, 1, 4),
    _AdGenUpgradeProdStandbySwVersion_Type()
)
adGenUpgradeProdStandbySwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenUpgradeProdStandbySwVersion.setStatus("mandatory")
_AdGenUpgradeProdMainBootSwVersion_Type = DisplayString
_AdGenUpgradeProdMainBootSwVersion_Object = MibTableColumn
adGenUpgradeProdMainBootSwVersion = _AdGenUpgradeProdMainBootSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 4, 2, 1, 1, 5),
    _AdGenUpgradeProdMainBootSwVersion_Type()
)
adGenUpgradeProdMainBootSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenUpgradeProdMainBootSwVersion.setStatus("mandatory")
_AdGenUpgradeProdStandbyBootSwVersion_Type = DisplayString
_AdGenUpgradeProdStandbyBootSwVersion_Object = MibTableColumn
adGenUpgradeProdStandbyBootSwVersion = _AdGenUpgradeProdStandbyBootSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 4, 2, 1, 1, 6),
    _AdGenUpgradeProdStandbyBootSwVersion_Type()
)
adGenUpgradeProdStandbyBootSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenUpgradeProdStandbyBootSwVersion.setStatus("mandatory")

# Managed Objects groups


# Notification objects

adClrSWFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 4, 0, 1001340)
)
adClrSWFailAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENUPGRADE-MIB", "adGenUpgradeFailureStatus"))
)
if mibBuilder.loadTexts:
    adClrSWFailAlarm.setStatus(
        ""
    )

adSWFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 4, 0, 1001341)
)
adSWFailAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENUPGRADE-MIB", "adGenUpgradeFailureStatus"))
)
if mibBuilder.loadTexts:
    adSWFailAlarm.setStatus(
        ""
    )

adClrIncompatibleSWAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 4, 0, 1001342)
)
adClrIncompatibleSWAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENUPGRADE-MIB", "adGenUpgradeFailureStatus"))
)
if mibBuilder.loadTexts:
    adClrIncompatibleSWAlarm.setStatus(
        ""
    )

adIncompatibleSWAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 4, 0, 1001343)
)
adIncompatibleSWAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENUPGRADE-MIB", "adGenUpgradeFailureStatus"))
)
if mibBuilder.loadTexts:
    adIncompatibleSWAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENUPGRADE-MIB",
    **{"adGenUpgrade": adGenUpgrade,
       "adClrSWFailAlarm": adClrSWFailAlarm,
       "adSWFailAlarm": adSWFailAlarm,
       "adClrIncompatibleSWAlarm": adClrIncompatibleSWAlarm,
       "adIncompatibleSWAlarm": adIncompatibleSWAlarm,
       "adGenUpgradeStatus": adGenUpgradeStatus,
       "adGenUpgradeStatusTable": adGenUpgradeStatusTable,
       "adGenUpgradeStatusEntry": adGenUpgradeStatusEntry,
       "adGenUpgradeFailureStatus": adGenUpgradeFailureStatus,
       "adGenUpgradeSoftwareStatus": adGenUpgradeSoftwareStatus,
       "adGenUpgradeSoftwarePercentageStatus": adGenUpgradeSoftwarePercentageStatus,
       "adGenUpgradeSwUpgradeability": adGenUpgradeSwUpgradeability,
       "adGenUpgradeConfig": adGenUpgradeConfig,
       "adGenUpgradeConfigTable": adGenUpgradeConfigTable,
       "adGenUpgradeConfigEntry": adGenUpgradeConfigEntry,
       "adGenUpgradeSwConfiguration": adGenUpgradeSwConfiguration,
       "adGenUpgradeSwConfigDescription": adGenUpgradeSwConfigDescription,
       "adGenUpgradeProdMainSwVersion": adGenUpgradeProdMainSwVersion,
       "adGenUpgradeProdStandbySwVersion": adGenUpgradeProdStandbySwVersion,
       "adGenUpgradeProdMainBootSwVersion": adGenUpgradeProdMainBootSwVersion,
       "adGenUpgradeProdStandbyBootSwVersion": adGenUpgradeProdStandbyBootSwVersion}
)
