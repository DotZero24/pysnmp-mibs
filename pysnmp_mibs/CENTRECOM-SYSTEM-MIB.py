# SNMP MIB module (CENTRECOM-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/allied-old/CENTRECOM-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:12:41 2025
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

(extSwitchMIB,) = mibBuilder.importSymbols(
    "CENTRECOM-MIB",
    "extSwitchMIB")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

atiSwitchSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _AtiSaveConfiguration_Type(Integer32):
    """Custom type atiSaveConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("saveToPrimary", 1),
          ("saveToSecondary", 2))
    )


_AtiSaveConfiguration_Type.__name__ = "Integer32"
_AtiSaveConfiguration_Object = MibScalar
atiSaveConfiguration = _AtiSaveConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 3, 3),
    _AtiSaveConfiguration_Type()
)
atiSaveConfiguration.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    atiSaveConfiguration.setStatus("mandatory")


class _AtiSaveStatus_Type(Integer32):
    """Custom type atiSaveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("saveInProgress", 1),
          ("saveNotInProgress", 2))
    )


_AtiSaveStatus_Type.__name__ = "Integer32"
_AtiSaveStatus_Object = MibScalar
atiSaveStatus = _AtiSaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 3, 4),
    _AtiSaveStatus_Type()
)
atiSaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiSaveStatus.setStatus("mandatory")


class _AtiCurrentConfigInUse_Type(Integer32):
    """Custom type atiCurrentConfigInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_AtiCurrentConfigInUse_Type.__name__ = "Integer32"
_AtiCurrentConfigInUse_Object = MibScalar
atiCurrentConfigInUse = _AtiCurrentConfigInUse_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 3, 5),
    _AtiCurrentConfigInUse_Type()
)
atiCurrentConfigInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiCurrentConfigInUse.setStatus("mandatory")


class _AtiConfigToUseOnReboot_Type(Integer32):
    """Custom type atiConfigToUseOnReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_AtiConfigToUseOnReboot_Type.__name__ = "Integer32"
_AtiConfigToUseOnReboot_Object = MibScalar
atiConfigToUseOnReboot = _AtiConfigToUseOnReboot_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 3, 6),
    _AtiConfigToUseOnReboot_Type()
)
atiConfigToUseOnReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiConfigToUseOnReboot.setStatus("mandatory")
_AtiOverTemperatureAlarm_Type = TruthValue
_AtiOverTemperatureAlarm_Object = MibScalar
atiOverTemperatureAlarm = _AtiOverTemperatureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 3, 7),
    _AtiOverTemperatureAlarm_Type()
)
atiOverTemperatureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiOverTemperatureAlarm.setStatus("mandatory")


class _AtiCurrentTemperature_Type(Integer32):
    """Custom type atiCurrentTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AtiCurrentTemperature_Type.__name__ = "Integer32"
_AtiCurrentTemperature_Object = MibScalar
atiCurrentTemperature = _AtiCurrentTemperature_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 3, 8),
    _AtiCurrentTemperature_Type()
)
atiCurrentTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiCurrentTemperature.setStatus("mandatory")
_AtiFanStatusTable_Object = MibTable
atiFanStatusTable = _AtiFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 3, 9)
)
if mibBuilder.loadTexts:
    atiFanStatusTable.setStatus("mandatory")
_AtiFanStatusEntry_Object = MibTableRow
atiFanStatusEntry = _AtiFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 3, 9, 1)
)
atiFanStatusEntry.setIndexNames(
    (0, "CENTRECOM-SYSTEM-MIB", "atiFanNumber"),
)
if mibBuilder.loadTexts:
    atiFanStatusEntry.setStatus("mandatory")
_AtiFanNumber_Type = Integer32
_AtiFanNumber_Object = MibTableColumn
atiFanNumber = _AtiFanNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 3, 9, 1, 1),
    _AtiFanNumber_Type()
)
atiFanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiFanNumber.setStatus("mandatory")
_AtiFanOperational_Type = TruthValue
_AtiFanOperational_Object = MibTableColumn
atiFanOperational = _AtiFanOperational_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 3, 9, 1, 2),
    _AtiFanOperational_Type()
)
atiFanOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiFanOperational.setStatus("mandatory")
_AtiPrimaryPowerOperational_Type = TruthValue
_AtiPrimaryPowerOperational_Object = MibScalar
atiPrimaryPowerOperational = _AtiPrimaryPowerOperational_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 3, 10),
    _AtiPrimaryPowerOperational_Type()
)
atiPrimaryPowerOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiPrimaryPowerOperational.setStatus("mandatory")


class _AtiRedundantPowerStatus_Type(Integer32):
    """Custom type atiRedundantPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("presentOK", 2),
          ("presentNotOK", 3))
    )


_AtiRedundantPowerStatus_Type.__name__ = "Integer32"
_AtiRedundantPowerStatus_Object = MibScalar
atiRedundantPowerStatus = _AtiRedundantPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 3, 11),
    _AtiRedundantPowerStatus_Type()
)
atiRedundantPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiRedundantPowerStatus.setStatus("mandatory")
_AtiRedundantPowerAlarm_Type = TruthValue
_AtiRedundantPowerAlarm_Object = MibScalar
atiRedundantPowerAlarm = _AtiRedundantPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 3, 12),
    _AtiRedundantPowerAlarm_Type()
)
atiRedundantPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiRedundantPowerAlarm.setStatus("mandatory")


class _AtiPrimarySoftwareRev_Type(DisplayString):
    """Custom type atiPrimarySoftwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AtiPrimarySoftwareRev_Type.__name__ = "DisplayString"
_AtiPrimarySoftwareRev_Object = MibScalar
atiPrimarySoftwareRev = _AtiPrimarySoftwareRev_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 3, 13),
    _AtiPrimarySoftwareRev_Type()
)
atiPrimarySoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiPrimarySoftwareRev.setStatus("mandatory")


class _AtiSecondarySoftwareRev_Type(DisplayString):
    """Custom type atiSecondarySoftwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AtiSecondarySoftwareRev_Type.__name__ = "DisplayString"
_AtiSecondarySoftwareRev_Object = MibScalar
atiSecondarySoftwareRev = _AtiSecondarySoftwareRev_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 3, 14),
    _AtiSecondarySoftwareRev_Type()
)
atiSecondarySoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiSecondarySoftwareRev.setStatus("mandatory")


class _AtiImageToUseOnReboot_Type(Integer32):
    """Custom type atiImageToUseOnReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_AtiImageToUseOnReboot_Type.__name__ = "Integer32"
_AtiImageToUseOnReboot_Object = MibScalar
atiImageToUseOnReboot = _AtiImageToUseOnReboot_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 3, 15),
    _AtiImageToUseOnReboot_Type()
)
atiImageToUseOnReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiImageToUseOnReboot.setStatus("mandatory")


class _AtiSystemID_Type(DisplayString):
    """Custom type atiSystemID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 126),
    )


_AtiSystemID_Type.__name__ = "DisplayString"
_AtiSystemID_Object = MibScalar
atiSystemID = _AtiSystemID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 3, 16),
    _AtiSystemID_Type()
)
atiSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiSystemID.setStatus("mandatory")


class _AtiSystemBoardID_Type(DisplayString):
    """Custom type atiSystemBoardID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 126),
    )


_AtiSystemBoardID_Type.__name__ = "DisplayString"
_AtiSystemBoardID_Object = MibScalar
atiSystemBoardID = _AtiSystemBoardID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 3, 17),
    _AtiSystemBoardID_Type()
)
atiSystemBoardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiSystemBoardID.setStatus("mandatory")


class _AtiSystemLeftBoardID_Type(DisplayString):
    """Custom type atiSystemLeftBoardID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 126),
    )


_AtiSystemLeftBoardID_Type.__name__ = "DisplayString"
_AtiSystemLeftBoardID_Object = MibScalar
atiSystemLeftBoardID = _AtiSystemLeftBoardID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 3, 18),
    _AtiSystemLeftBoardID_Type()
)
atiSystemLeftBoardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiSystemLeftBoardID.setStatus("mandatory")


class _AtiSystemRightBoardID_Type(DisplayString):
    """Custom type atiSystemRightBoardID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 126),
    )


_AtiSystemRightBoardID_Type.__name__ = "DisplayString"
_AtiSystemRightBoardID_Object = MibScalar
atiSystemRightBoardID = _AtiSystemRightBoardID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 3, 19),
    _AtiSystemRightBoardID_Type()
)
atiSystemRightBoardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiSystemRightBoardID.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTRECOM-SYSTEM-MIB",
    **{"atiSwitchSystem": atiSwitchSystem,
       "atiSaveConfiguration": atiSaveConfiguration,
       "atiSaveStatus": atiSaveStatus,
       "atiCurrentConfigInUse": atiCurrentConfigInUse,
       "atiConfigToUseOnReboot": atiConfigToUseOnReboot,
       "atiOverTemperatureAlarm": atiOverTemperatureAlarm,
       "atiCurrentTemperature": atiCurrentTemperature,
       "atiFanStatusTable": atiFanStatusTable,
       "atiFanStatusEntry": atiFanStatusEntry,
       "atiFanNumber": atiFanNumber,
       "atiFanOperational": atiFanOperational,
       "atiPrimaryPowerOperational": atiPrimaryPowerOperational,
       "atiRedundantPowerStatus": atiRedundantPowerStatus,
       "atiRedundantPowerAlarm": atiRedundantPowerAlarm,
       "atiPrimarySoftwareRev": atiPrimarySoftwareRev,
       "atiSecondarySoftwareRev": atiSecondarySoftwareRev,
       "atiImageToUseOnReboot": atiImageToUseOnReboot,
       "atiSystemID": atiSystemID,
       "atiSystemBoardID": atiSystemBoardID,
       "atiSystemLeftBoardID": atiSystemLeftBoardID,
       "atiSystemRightBoardID": atiSystemRightBoardID}
)
