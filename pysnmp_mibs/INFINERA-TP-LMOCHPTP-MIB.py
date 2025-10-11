# SNMP MIB module (INFINERA-TP-LMOCHPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-LMOCHPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:50 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(terminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "terminationPoint")

(FloatTenths,) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

lmOchPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 27)
)
if mibBuilder.loadTexts:
    lmOchPtpMIB.setRevisions(
        ("2011-05-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LmOchPtpTable_Object = MibTable
lmOchPtpTable = _LmOchPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 27, 1)
)
if mibBuilder.loadTexts:
    lmOchPtpTable.setStatus("current")
_LmOchPtpEntry_Object = MibTableRow
lmOchPtpEntry = _LmOchPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 27, 1, 1)
)
lmOchPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lmOchPtpEntry.setStatus("current")


class _LmOchPtpAutoDiscoveryState_Type(Integer32):
    """Custom type lmOchPtpAutoDiscoveryState based on Integer32"""
    defaultValue = 4

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
        *(("inProgress", 1),
          ("completed", 2),
          ("unknown", 3),
          ("notValidOrShutdown", 4),
          ("failed", 5))
    )


_LmOchPtpAutoDiscoveryState_Type.__name__ = "Integer32"
_LmOchPtpAutoDiscoveryState_Object = MibTableColumn
lmOchPtpAutoDiscoveryState = _LmOchPtpAutoDiscoveryState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 27, 1, 1, 1),
    _LmOchPtpAutoDiscoveryState_Type()
)
lmOchPtpAutoDiscoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpAutoDiscoveryState.setStatus("current")
_LmOchPtpRate_Type = Integer32
_LmOchPtpRate_Object = MibTableColumn
lmOchPtpRate = _LmOchPtpRate_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 27, 1, 1, 2),
    _LmOchPtpRate_Type()
)
lmOchPtpRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpRate.setStatus("current")
_LmOchPtpTuneableOchNumber_Type = Integer32
_LmOchPtpTuneableOchNumber_Object = MibTableColumn
lmOchPtpTuneableOchNumber = _LmOchPtpTuneableOchNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 27, 1, 1, 3),
    _LmOchPtpTuneableOchNumber_Type()
)
lmOchPtpTuneableOchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpTuneableOchNumber.setStatus("current")
_LmOchPtpTuneableOcgNumber_Type = Integer32
_LmOchPtpTuneableOcgNumber_Object = MibTableColumn
lmOchPtpTuneableOcgNumber = _LmOchPtpTuneableOcgNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 27, 1, 1, 4),
    _LmOchPtpTuneableOcgNumber_Type()
)
lmOchPtpTuneableOcgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpTuneableOcgNumber.setStatus("current")
_LmOchPtpInstalledOchNumber_Type = Integer32
_LmOchPtpInstalledOchNumber_Object = MibTableColumn
lmOchPtpInstalledOchNumber = _LmOchPtpInstalledOchNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 27, 1, 1, 5),
    _LmOchPtpInstalledOchNumber_Type()
)
lmOchPtpInstalledOchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpInstalledOchNumber.setStatus("current")
_LmOchPtpInstalledOcgNumber_Type = Integer32
_LmOchPtpInstalledOcgNumber_Object = MibTableColumn
lmOchPtpInstalledOcgNumber = _LmOchPtpInstalledOcgNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 27, 1, 1, 6),
    _LmOchPtpInstalledOcgNumber_Type()
)
lmOchPtpInstalledOcgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpInstalledOcgNumber.setStatus("current")
_LmOchPtpInstalledWavelength_Type = FloatTenths
_LmOchPtpInstalledWavelength_Object = MibTableColumn
lmOchPtpInstalledWavelength = _LmOchPtpInstalledWavelength_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 27, 1, 1, 7),
    _LmOchPtpInstalledWavelength_Type()
)
lmOchPtpInstalledWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpInstalledWavelength.setStatus("current")
_LmOchPtpDiscoveredOchPortId_Type = DisplayString
_LmOchPtpDiscoveredOchPortId_Object = MibTableColumn
lmOchPtpDiscoveredOchPortId = _LmOchPtpDiscoveredOchPortId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 27, 1, 1, 8),
    _LmOchPtpDiscoveredOchPortId_Type()
)
lmOchPtpDiscoveredOchPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpDiscoveredOchPortId.setStatus("current")
_LmOchPtpRemoteOcgPortId_Type = DisplayString
_LmOchPtpRemoteOcgPortId_Object = MibTableColumn
lmOchPtpRemoteOcgPortId = _LmOchPtpRemoteOcgPortId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 27, 1, 1, 9),
    _LmOchPtpRemoteOcgPortId_Type()
)
lmOchPtpRemoteOcgPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpRemoteOcgPortId.setStatus("current")


class _LmOchPtpPmHistStatsEnable_Type(Integer32):
    """Custom type lmOchPtpPmHistStatsEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_LmOchPtpPmHistStatsEnable_Type.__name__ = "Integer32"
_LmOchPtpPmHistStatsEnable_Object = MibTableColumn
lmOchPtpPmHistStatsEnable = _LmOchPtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 27, 1, 1, 10),
    _LmOchPtpPmHistStatsEnable_Type()
)
lmOchPtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmOchPtpPmHistStatsEnable.setStatus("current")
_LmOchPtpFFCRBlockSize_Type = Integer32
_LmOchPtpFFCRBlockSize_Object = MibTableColumn
lmOchPtpFFCRBlockSize = _LmOchPtpFFCRBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 27, 1, 1, 11),
    _LmOchPtpFFCRBlockSize_Type()
)
lmOchPtpFFCRBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpFFCRBlockSize.setStatus("current")


class _LmOchPtpModulation_Type(Integer32):
    """Custom type lmOchPtpModulation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pm-Qpsk", 1),
          ("pm-Bpsk", 2))
    )


_LmOchPtpModulation_Type.__name__ = "Integer32"
_LmOchPtpModulation_Object = MibTableColumn
lmOchPtpModulation = _LmOchPtpModulation_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 27, 1, 1, 12),
    _LmOchPtpModulation_Type()
)
lmOchPtpModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpModulation.setStatus("current")


class _LmOchPtpInstalledModulation_Type(Integer32):
    """Custom type lmOchPtpInstalledModulation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pm-Qpsk", 1),
          ("pm-Bpsk", 2))
    )


_LmOchPtpInstalledModulation_Type.__name__ = "Integer32"
_LmOchPtpInstalledModulation_Object = MibTableColumn
lmOchPtpInstalledModulation = _LmOchPtpInstalledModulation_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 27, 1, 1, 13),
    _LmOchPtpInstalledModulation_Type()
)
lmOchPtpInstalledModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpInstalledModulation.setStatus("current")


class _LmOchPtpCDCompMode_Type(Integer32):
    """Custom type lmOchPtpCDCompMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2),
          ("disable", 3))
    )


_LmOchPtpCDCompMode_Type.__name__ = "Integer32"
_LmOchPtpCDCompMode_Object = MibTableColumn
lmOchPtpCDCompMode = _LmOchPtpCDCompMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 27, 1, 1, 14),
    _LmOchPtpCDCompMode_Type()
)
lmOchPtpCDCompMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpCDCompMode.setStatus("current")
_LmOchPtpCDSearchStepSize_Type = Integer32
_LmOchPtpCDSearchStepSize_Object = MibTableColumn
lmOchPtpCDSearchStepSize = _LmOchPtpCDSearchStepSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 27, 1, 1, 15),
    _LmOchPtpCDSearchStepSize_Type()
)
lmOchPtpCDSearchStepSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpCDSearchStepSize.setStatus("current")
_LmOchPtpCDCompStart_Type = Integer32
_LmOchPtpCDCompStart_Object = MibTableColumn
lmOchPtpCDCompStart = _LmOchPtpCDCompStart_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 27, 1, 1, 16),
    _LmOchPtpCDCompStart_Type()
)
lmOchPtpCDCompStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpCDCompStart.setStatus("current")
_LmOchPtpCDCompEnd_Type = Integer32
_LmOchPtpCDCompEnd_Object = MibTableColumn
lmOchPtpCDCompEnd = _LmOchPtpCDCompEnd_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 27, 1, 1, 17),
    _LmOchPtpCDCompEnd_Type()
)
lmOchPtpCDCompEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpCDCompEnd.setStatus("current")


class _LmOchPtpFwUpgradeStatus_Type(Integer32):
    """Custom type lmOchPtpFwUpgradeStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("inProgress", 2),
          ("completed", 3),
          ("failed", 4))
    )


_LmOchPtpFwUpgradeStatus_Type.__name__ = "Integer32"
_LmOchPtpFwUpgradeStatus_Object = MibTableColumn
lmOchPtpFwUpgradeStatus = _LmOchPtpFwUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 27, 1, 1, 18),
    _LmOchPtpFwUpgradeStatus_Type()
)
lmOchPtpFwUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpFwUpgradeStatus.setStatus("current")
_LmOchPtpConformance_ObjectIdentity = ObjectIdentity
lmOchPtpConformance = _LmOchPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 27, 3)
)
_LmOchPtpCompliances_ObjectIdentity = ObjectIdentity
lmOchPtpCompliances = _LmOchPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 27, 3, 1)
)
_LmOchPtpGroups_ObjectIdentity = ObjectIdentity
lmOchPtpGroups = _LmOchPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 27, 3, 2)
)

# Managed Objects groups

lmOchPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 27, 3, 2, 1)
)
lmOchPtpGroup.setObjects(
      *(("INFINERA-TP-LMOCHPTP-MIB", "lmOchPtpAutoDiscoveryState"),
        ("INFINERA-TP-LMOCHPTP-MIB", "lmOchPtpRate"),
        ("INFINERA-TP-LMOCHPTP-MIB", "lmOchPtpTuneableOchNumber"),
        ("INFINERA-TP-LMOCHPTP-MIB", "lmOchPtpTuneableOcgNumber"),
        ("INFINERA-TP-LMOCHPTP-MIB", "lmOchPtpInstalledOchNumber"),
        ("INFINERA-TP-LMOCHPTP-MIB", "lmOchPtpInstalledOcgNumber"),
        ("INFINERA-TP-LMOCHPTP-MIB", "lmOchPtpInstalledWavelength"),
        ("INFINERA-TP-LMOCHPTP-MIB", "lmOchPtpDiscoveredOchPortId"),
        ("INFINERA-TP-LMOCHPTP-MIB", "lmOchPtpRemoteOcgPortId"),
        ("INFINERA-TP-LMOCHPTP-MIB", "lmOchPtpPmHistStatsEnable"),
        ("INFINERA-TP-LMOCHPTP-MIB", "lmOchPtpFFCRBlockSize"),
        ("INFINERA-TP-LMOCHPTP-MIB", "lmOchPtpModulation"),
        ("INFINERA-TP-LMOCHPTP-MIB", "lmOchPtpInstalledModulation"),
        ("INFINERA-TP-LMOCHPTP-MIB", "lmOchPtpCDCompMode"),
        ("INFINERA-TP-LMOCHPTP-MIB", "lmOchPtpCDSearchStepSize"),
        ("INFINERA-TP-LMOCHPTP-MIB", "lmOchPtpCDCompStart"),
        ("INFINERA-TP-LMOCHPTP-MIB", "lmOchPtpCDCompEnd"),
        ("INFINERA-TP-LMOCHPTP-MIB", "lmOchPtpFwUpgradeStatus"))
)
if mibBuilder.loadTexts:
    lmOchPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lmOchPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 27, 3, 1, 1)
)
lmOchPtpCompliance.setObjects(
    ("INFINERA-TP-LMOCHPTP-MIB", "lmOchPtpGroup")
)
if mibBuilder.loadTexts:
    lmOchPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-LMOCHPTP-MIB",
    **{"lmOchPtpMIB": lmOchPtpMIB,
       "lmOchPtpTable": lmOchPtpTable,
       "lmOchPtpEntry": lmOchPtpEntry,
       "lmOchPtpAutoDiscoveryState": lmOchPtpAutoDiscoveryState,
       "lmOchPtpRate": lmOchPtpRate,
       "lmOchPtpTuneableOchNumber": lmOchPtpTuneableOchNumber,
       "lmOchPtpTuneableOcgNumber": lmOchPtpTuneableOcgNumber,
       "lmOchPtpInstalledOchNumber": lmOchPtpInstalledOchNumber,
       "lmOchPtpInstalledOcgNumber": lmOchPtpInstalledOcgNumber,
       "lmOchPtpInstalledWavelength": lmOchPtpInstalledWavelength,
       "lmOchPtpDiscoveredOchPortId": lmOchPtpDiscoveredOchPortId,
       "lmOchPtpRemoteOcgPortId": lmOchPtpRemoteOcgPortId,
       "lmOchPtpPmHistStatsEnable": lmOchPtpPmHistStatsEnable,
       "lmOchPtpFFCRBlockSize": lmOchPtpFFCRBlockSize,
       "lmOchPtpModulation": lmOchPtpModulation,
       "lmOchPtpInstalledModulation": lmOchPtpInstalledModulation,
       "lmOchPtpCDCompMode": lmOchPtpCDCompMode,
       "lmOchPtpCDSearchStepSize": lmOchPtpCDSearchStepSize,
       "lmOchPtpCDCompStart": lmOchPtpCDCompStart,
       "lmOchPtpCDCompEnd": lmOchPtpCDCompEnd,
       "lmOchPtpFwUpgradeStatus": lmOchPtpFwUpgradeStatus,
       "lmOchPtpConformance": lmOchPtpConformance,
       "lmOchPtpCompliances": lmOchPtpCompliances,
       "lmOchPtpCompliance": lmOchPtpCompliance,
       "lmOchPtpGroups": lmOchPtpGroups,
       "lmOchPtpGroup": lmOchPtpGroup}
)
