# SNMP MIB module (APS-R-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/APS-R-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:18:57 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(radExperimental,) = mibBuilder.importSymbols(
    "RAD-SMI-MIB",
    "radExperimental")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

apsMIBr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ApsK1K2(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2



class ApsSwitchCommand(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("lockoutOfProtection", 2),
          ("forcedSwitchWorkToProtect", 3),
          ("forcedSwitchProtectToWork", 4),
          ("manualSwitchWorkToProtect", 5),
          ("manualSwitchProtectToWork", 6),
          ("exercise", 7))
    )



class ApsControlCommand(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lockoutWorkingChannel", 1),
          ("clearLockoutWorkingChannel", 2))
    )



# MIB Managed Objects in the order of their OIDs

_ApsMIBObjectsR_ObjectIdentity = ObjectIdentity
apsMIBObjectsR = _ApsMIBObjectsR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1)
)
_ApsConfigR_ObjectIdentity = ObjectIdentity
apsConfigR = _ApsConfigR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 1)
)
_ApsConfigGroupsR_Type = Counter32
_ApsConfigGroupsR_Object = MibScalar
apsConfigGroupsR = _ApsConfigGroupsR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 1, 1),
    _ApsConfigGroupsR_Type()
)
apsConfigGroupsR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsConfigGroupsR.setStatus("current")
_ApsConfigTableR_Object = MibTable
apsConfigTableR = _ApsConfigTableR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    apsConfigTableR.setStatus("current")
_ApsConfigEntryR_Object = MibTableRow
apsConfigEntryR = _ApsConfigEntryR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 1, 2, 1)
)
apsConfigEntryR.setIndexNames(
    (1, "APS-R-MIB", "apsConfigNameR"),
)
if mibBuilder.loadTexts:
    apsConfigEntryR.setStatus("current")


class _ApsConfigNameR_Type(SnmpAdminString):
    """Custom type apsConfigNameR based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ApsConfigNameR_Type.__name__ = "SnmpAdminString"
_ApsConfigNameR_Object = MibTableColumn
apsConfigNameR = _ApsConfigNameR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 1, 2, 1, 1),
    _ApsConfigNameR_Type()
)
apsConfigNameR.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apsConfigNameR.setStatus("current")
_ApsConfigRowStatusR_Type = RowStatus
_ApsConfigRowStatusR_Object = MibTableColumn
apsConfigRowStatusR = _ApsConfigRowStatusR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 1, 2, 1, 2),
    _ApsConfigRowStatusR_Type()
)
apsConfigRowStatusR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsConfigRowStatusR.setStatus("current")


class _ApsConfigModeR_Type(Bits):
    """Custom type apsConfigModeR based on Bits"""
    namedValues = NamedValues(
        *(("onePlusOne", 0),
          ("oneToN", 1),
          ("revertive", 2),
          ("bidirectional", 3),
          ("extraTrafficAllowed", 4),
          ("onePlusOneOptimized", 5),
          ("pathProtection", 6),
          ("yCable", 7))
    )

_ApsConfigModeR_Type.__name__ = "Bits"
_ApsConfigModeR_Object = MibTableColumn
apsConfigModeR = _ApsConfigModeR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 1, 2, 1, 3),
    _ApsConfigModeR_Type()
)
apsConfigModeR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsConfigModeR.setStatus("current")


class _ApsConfigSdBerThresholdR_Type(Integer32):
    """Custom type apsConfigSdBerThresholdR based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 9),
    )


_ApsConfigSdBerThresholdR_Type.__name__ = "Integer32"
_ApsConfigSdBerThresholdR_Object = MibTableColumn
apsConfigSdBerThresholdR = _ApsConfigSdBerThresholdR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 1, 2, 1, 4),
    _ApsConfigSdBerThresholdR_Type()
)
apsConfigSdBerThresholdR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsConfigSdBerThresholdR.setStatus("current")


class _ApsConfigSfBerThresholdR_Type(Integer32):
    """Custom type apsConfigSfBerThresholdR based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 5),
    )


_ApsConfigSfBerThresholdR_Type.__name__ = "Integer32"
_ApsConfigSfBerThresholdR_Object = MibTableColumn
apsConfigSfBerThresholdR = _ApsConfigSfBerThresholdR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 1, 2, 1, 5),
    _ApsConfigSfBerThresholdR_Type()
)
apsConfigSfBerThresholdR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsConfigSfBerThresholdR.setStatus("current")


class _ApsConfigWaitToRestoreR_Type(Integer32):
    """Custom type apsConfigWaitToRestoreR based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 720),
    )


_ApsConfigWaitToRestoreR_Type.__name__ = "Integer32"
_ApsConfigWaitToRestoreR_Object = MibTableColumn
apsConfigWaitToRestoreR = _ApsConfigWaitToRestoreR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 1, 2, 1, 6),
    _ApsConfigWaitToRestoreR_Type()
)
apsConfigWaitToRestoreR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsConfigWaitToRestoreR.setStatus("current")
_ApsConfigCreationTimeR_Type = TimeTicks
_ApsConfigCreationTimeR_Object = MibTableColumn
apsConfigCreationTimeR = _ApsConfigCreationTimeR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 1, 2, 1, 7),
    _ApsConfigCreationTimeR_Type()
)
apsConfigCreationTimeR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsConfigCreationTimeR.setStatus("current")


class _ApsConfigOperDelayR_Type(Integer32):
    """Custom type apsConfigOperDelayR based on Integer32"""
    defaultValue = 10


_ApsConfigOperDelayR_Type.__name__ = "Integer32"
_ApsConfigOperDelayR_Object = MibTableColumn
apsConfigOperDelayR = _ApsConfigOperDelayR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 1, 2, 1, 8),
    _ApsConfigOperDelayR_Type()
)
apsConfigOperDelayR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsConfigOperDelayR.setStatus("current")
_ApsStatusTableR_Object = MibTable
apsStatusTableR = _ApsStatusTableR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 2)
)
if mibBuilder.loadTexts:
    apsStatusTableR.setStatus("current")
_ApsStatusEntryR_Object = MibTableRow
apsStatusEntryR = _ApsStatusEntryR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 2, 1)
)
apsStatusEntryR.setIndexNames(
    (1, "APS-R-MIB", "apsConfigNameR"),
)
if mibBuilder.loadTexts:
    apsStatusEntryR.setStatus("current")
_ApsStatusK1K2RcvR_Type = ApsK1K2
_ApsStatusK1K2RcvR_Object = MibTableColumn
apsStatusK1K2RcvR = _ApsStatusK1K2RcvR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 2, 1, 1),
    _ApsStatusK1K2RcvR_Type()
)
apsStatusK1K2RcvR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStatusK1K2RcvR.setStatus("current")
_ApsStatusK1K2TransR_Type = ApsK1K2
_ApsStatusK1K2TransR_Object = MibTableColumn
apsStatusK1K2TransR = _ApsStatusK1K2TransR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 2, 1, 2),
    _ApsStatusK1K2TransR_Type()
)
apsStatusK1K2TransR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStatusK1K2TransR.setStatus("current")


class _ApsStatusCurrentR_Type(Bits):
    """Custom type apsStatusCurrentR based on Bits"""
    namedValues = NamedValues(
        *(("modeMismatch", 0),
          ("channelMismatch", 1),
          ("psbf", 2),
          ("feplf", 3),
          ("extraTraffic", 4))
    )

_ApsStatusCurrentR_Type.__name__ = "Bits"
_ApsStatusCurrentR_Object = MibTableColumn
apsStatusCurrentR = _ApsStatusCurrentR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 2, 1, 3),
    _ApsStatusCurrentR_Type()
)
apsStatusCurrentR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStatusCurrentR.setStatus("current")
_ApsStatusModeMismatchesR_Type = Counter32
_ApsStatusModeMismatchesR_Object = MibTableColumn
apsStatusModeMismatchesR = _ApsStatusModeMismatchesR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 2, 1, 4),
    _ApsStatusModeMismatchesR_Type()
)
apsStatusModeMismatchesR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStatusModeMismatchesR.setStatus("current")
_ApsStatusChannelMismatchesR_Type = Counter32
_ApsStatusChannelMismatchesR_Object = MibTableColumn
apsStatusChannelMismatchesR = _ApsStatusChannelMismatchesR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 2, 1, 5),
    _ApsStatusChannelMismatchesR_Type()
)
apsStatusChannelMismatchesR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStatusChannelMismatchesR.setStatus("current")
_ApsStatusPSBFsR_Type = Counter32
_ApsStatusPSBFsR_Object = MibTableColumn
apsStatusPSBFsR = _ApsStatusPSBFsR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 2, 1, 6),
    _ApsStatusPSBFsR_Type()
)
apsStatusPSBFsR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStatusPSBFsR.setStatus("current")
_ApsStatusFEPLFsR_Type = Counter32
_ApsStatusFEPLFsR_Object = MibTableColumn
apsStatusFEPLFsR = _ApsStatusFEPLFsR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 2, 1, 7),
    _ApsStatusFEPLFsR_Type()
)
apsStatusFEPLFsR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStatusFEPLFsR.setStatus("current")
_ApsMapR_ObjectIdentity = ObjectIdentity
apsMapR = _ApsMapR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 3)
)
_ApsChanLTEsR_Type = Counter32
_ApsChanLTEsR_Object = MibScalar
apsChanLTEsR = _ApsChanLTEsR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 3, 1),
    _ApsChanLTEsR_Type()
)
apsChanLTEsR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsChanLTEsR.setStatus("current")
_ApsMapTableR_Object = MibTable
apsMapTableR = _ApsMapTableR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    apsMapTableR.setStatus("current")
_ApsMapEntryR_Object = MibTableRow
apsMapEntryR = _ApsMapEntryR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 3, 2, 1)
)
apsMapEntryR.setIndexNames(
    (0, "APS-R-MIB", "apsMapIfIndexR"),
)
if mibBuilder.loadTexts:
    apsMapEntryR.setStatus("current")
_ApsMapIfIndexR_Type = InterfaceIndex
_ApsMapIfIndexR_Object = MibTableColumn
apsMapIfIndexR = _ApsMapIfIndexR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 3, 2, 1, 1),
    _ApsMapIfIndexR_Type()
)
apsMapIfIndexR.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apsMapIfIndexR.setStatus("current")


class _ApsMapGroupNameR_Type(SnmpAdminString):
    """Custom type apsMapGroupNameR based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ApsMapGroupNameR_Type.__name__ = "SnmpAdminString"
_ApsMapGroupNameR_Object = MibTableColumn
apsMapGroupNameR = _ApsMapGroupNameR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 3, 2, 1, 2),
    _ApsMapGroupNameR_Type()
)
apsMapGroupNameR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsMapGroupNameR.setStatus("current")


class _ApsMapChanNumberR_Type(Integer32):
    """Custom type apsMapChanNumberR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 14),
    )


_ApsMapChanNumberR_Type.__name__ = "Integer32"
_ApsMapChanNumberR_Object = MibTableColumn
apsMapChanNumberR = _ApsMapChanNumberR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 3, 2, 1, 3),
    _ApsMapChanNumberR_Type()
)
apsMapChanNumberR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsMapChanNumberR.setStatus("current")
_ApsChanConfigTableR_Object = MibTable
apsChanConfigTableR = _ApsChanConfigTableR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 4)
)
if mibBuilder.loadTexts:
    apsChanConfigTableR.setStatus("current")
_ApsChanConfigEntryR_Object = MibTableRow
apsChanConfigEntryR = _ApsChanConfigEntryR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 4, 1)
)
apsChanConfigEntryR.setIndexNames(
    (0, "APS-R-MIB", "apsChanGroupNameR"),
    (0, "APS-R-MIB", "apsChanNumberR"),
)
if mibBuilder.loadTexts:
    apsChanConfigEntryR.setStatus("current")


class _ApsChanGroupNameR_Type(SnmpAdminString):
    """Custom type apsChanGroupNameR based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ApsChanGroupNameR_Type.__name__ = "SnmpAdminString"
_ApsChanGroupNameR_Object = MibTableColumn
apsChanGroupNameR = _ApsChanGroupNameR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 4, 1, 1),
    _ApsChanGroupNameR_Type()
)
apsChanGroupNameR.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apsChanGroupNameR.setStatus("current")


class _ApsChanNumberR_Type(Integer32):
    """Custom type apsChanNumberR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_ApsChanNumberR_Type.__name__ = "Integer32"
_ApsChanNumberR_Object = MibTableColumn
apsChanNumberR = _ApsChanNumberR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 4, 1, 2),
    _ApsChanNumberR_Type()
)
apsChanNumberR.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apsChanNumberR.setStatus("current")
_ApsChanRowStatusR_Type = RowStatus
_ApsChanRowStatusR_Object = MibTableColumn
apsChanRowStatusR = _ApsChanRowStatusR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 4, 1, 3),
    _ApsChanRowStatusR_Type()
)
apsChanRowStatusR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsChanRowStatusR.setStatus("current")
_ApsChanIfIndexR_Type = InterfaceIndex
_ApsChanIfIndexR_Object = MibTableColumn
apsChanIfIndexR = _ApsChanIfIndexR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 4, 1, 4),
    _ApsChanIfIndexR_Type()
)
apsChanIfIndexR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsChanIfIndexR.setStatus("current")


class _ApsChanPriorityR_Type(Integer32):
    """Custom type apsChanPriorityR based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2))
    )


_ApsChanPriorityR_Type.__name__ = "Integer32"
_ApsChanPriorityR_Object = MibTableColumn
apsChanPriorityR = _ApsChanPriorityR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 4, 1, 5),
    _ApsChanPriorityR_Type()
)
apsChanPriorityR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsChanPriorityR.setStatus("current")
_ApsCommandTableR_Object = MibTable
apsCommandTableR = _ApsCommandTableR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 5)
)
if mibBuilder.loadTexts:
    apsCommandTableR.setStatus("current")
_ApsCommandEntryR_Object = MibTableRow
apsCommandEntryR = _ApsCommandEntryR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 5, 1)
)
apsCommandEntryR.setIndexNames(
    (0, "APS-R-MIB", "apsChanGroupNameR"),
    (0, "APS-R-MIB", "apsChanNumberR"),
)
if mibBuilder.loadTexts:
    apsCommandEntryR.setStatus("current")
_ApsCommandSwitchR_Type = ApsSwitchCommand
_ApsCommandSwitchR_Object = MibTableColumn
apsCommandSwitchR = _ApsCommandSwitchR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 5, 1, 1),
    _ApsCommandSwitchR_Type()
)
apsCommandSwitchR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsCommandSwitchR.setStatus("current")
_ApsCommandControlR_Type = ApsControlCommand
_ApsCommandControlR_Object = MibTableColumn
apsCommandControlR = _ApsCommandControlR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 5, 1, 2),
    _ApsCommandControlR_Type()
)
apsCommandControlR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsCommandControlR.setStatus("current")
_ApsChanStatusTableR_Object = MibTable
apsChanStatusTableR = _ApsChanStatusTableR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 6)
)
if mibBuilder.loadTexts:
    apsChanStatusTableR.setStatus("current")
_ApsChanStatusEntryR_Object = MibTableRow
apsChanStatusEntryR = _ApsChanStatusEntryR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 6, 1)
)
apsChanStatusEntryR.setIndexNames(
    (0, "APS-R-MIB", "apsChanGroupNameR"),
    (0, "APS-R-MIB", "apsChanNumberR"),
)
if mibBuilder.loadTexts:
    apsChanStatusEntryR.setStatus("current")


class _ApsChanStatusR_Type(Bits):
    """Custom type apsChanStatusR based on Bits"""
    namedValues = NamedValues(
        *(("lockedOut", 0),
          ("sd", 1),
          ("sf", 2),
          ("switched", 3))
    )

_ApsChanStatusR_Type.__name__ = "Bits"
_ApsChanStatusR_Object = MibTableColumn
apsChanStatusR = _ApsChanStatusR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 6, 1, 1),
    _ApsChanStatusR_Type()
)
apsChanStatusR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsChanStatusR.setStatus("current")
_ApsChanSignalDegradesR_Type = Counter32
_ApsChanSignalDegradesR_Object = MibTableColumn
apsChanSignalDegradesR = _ApsChanSignalDegradesR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 6, 1, 2),
    _ApsChanSignalDegradesR_Type()
)
apsChanSignalDegradesR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsChanSignalDegradesR.setStatus("current")
_ApsChanSignalFailuresR_Type = Counter32
_ApsChanSignalFailuresR_Object = MibTableColumn
apsChanSignalFailuresR = _ApsChanSignalFailuresR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 6, 1, 3),
    _ApsChanSignalFailuresR_Type()
)
apsChanSignalFailuresR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsChanSignalFailuresR.setStatus("current")
_ApsChanSwitchoversR_Type = Counter32
_ApsChanSwitchoversR_Object = MibTableColumn
apsChanSwitchoversR = _ApsChanSwitchoversR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 6, 1, 4),
    _ApsChanSwitchoversR_Type()
)
apsChanSwitchoversR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsChanSwitchoversR.setStatus("current")
_ApsChanLastSwitchoverR_Type = TimeTicks
_ApsChanLastSwitchoverR_Object = MibTableColumn
apsChanLastSwitchoverR = _ApsChanLastSwitchoverR_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 1, 6, 1, 5),
    _ApsChanLastSwitchoverR_Type()
)
apsChanLastSwitchoverR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsChanLastSwitchoverR.setStatus("current")
_ApsMIBNotificationsR_ObjectIdentity = ObjectIdentity
apsMIBNotificationsR = _ApsMIBNotificationsR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 2)
)
_ApsNotificationsPrefixR_ObjectIdentity = ObjectIdentity
apsNotificationsPrefixR = _ApsNotificationsPrefixR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 2, 0)
)
_ApsMIBConformanceR_ObjectIdentity = ObjectIdentity
apsMIBConformanceR = _ApsMIBConformanceR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 3)
)
_ApsGroupsR_ObjectIdentity = ObjectIdentity
apsGroupsR = _ApsGroupsR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 3, 1)
)
_ApsCompliancesR_ObjectIdentity = ObjectIdentity
apsCompliancesR = _ApsCompliancesR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 3, 2)
)

# Managed Objects groups

apsConfigGeneralR = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 3, 1, 1)
)
apsConfigGeneralR.setObjects(
      *(("APS-R-MIB", "apsConfigRowStatusR"),
        ("APS-R-MIB", "apsConfigModeR"),
        ("APS-R-MIB", "apsConfigSdBerThresholdR"),
        ("APS-R-MIB", "apsConfigSfBerThresholdR"),
        ("APS-R-MIB", "apsConfigOperDelayR"),
        ("APS-R-MIB", "apsConfigCreationTimeR"))
)
if mibBuilder.loadTexts:
    apsConfigGeneralR.setStatus("current")

apsConfigOneToNr = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 3, 1, 2)
)
apsConfigOneToNr.setObjects(
    ("APS-R-MIB", "apsConfigWaitToRestoreR")
)
if mibBuilder.loadTexts:
    apsConfigOneToNr.setStatus("current")

apsCommandOnePlusOneR = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 3, 1, 3)
)
apsCommandOnePlusOneR.setObjects(
    ("APS-R-MIB", "apsCommandSwitchR")
)
if mibBuilder.loadTexts:
    apsCommandOnePlusOneR.setStatus("current")

apsCommandOneToNr = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 3, 1, 4)
)
apsCommandOneToNr.setObjects(
      *(("APS-R-MIB", "apsCommandSwitchR"),
        ("APS-R-MIB", "apsCommandControlR"))
)
if mibBuilder.loadTexts:
    apsCommandOneToNr.setStatus("current")

apsStatusGeneralR = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 3, 1, 5)
)
apsStatusGeneralR.setObjects(
      *(("APS-R-MIB", "apsStatusK1K2RcvR"),
        ("APS-R-MIB", "apsStatusK1K2TransR"),
        ("APS-R-MIB", "apsStatusCurrentR"),
        ("APS-R-MIB", "apsStatusModeMismatchesR"),
        ("APS-R-MIB", "apsStatusChannelMismatchesR"),
        ("APS-R-MIB", "apsStatusPSBFsR"),
        ("APS-R-MIB", "apsStatusFEPLFsR"))
)
if mibBuilder.loadTexts:
    apsStatusGeneralR.setStatus("current")

apsChanGeneralR = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 3, 1, 6)
)
apsChanGeneralR.setObjects(
      *(("APS-R-MIB", "apsChanIfIndexR"),
        ("APS-R-MIB", "apsChanRowStatusR"),
        ("APS-R-MIB", "apsChanStatusR"),
        ("APS-R-MIB", "apsChanSignalDegradesR"),
        ("APS-R-MIB", "apsChanSignalFailuresR"),
        ("APS-R-MIB", "apsChanSwitchoversR"),
        ("APS-R-MIB", "apsChanLastSwitchoverR"))
)
if mibBuilder.loadTexts:
    apsChanGeneralR.setStatus("current")

apsChanOneToNr = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 3, 1, 7)
)
apsChanOneToNr.setObjects(
    ("APS-R-MIB", "apsChanPriorityR")
)
if mibBuilder.loadTexts:
    apsChanOneToNr.setStatus("current")

apsTotalsGroupR = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 3, 1, 8)
)
apsTotalsGroupR.setObjects(
      *(("APS-R-MIB", "apsConfigGroupsR"),
        ("APS-R-MIB", "apsChanLTEsR"))
)
if mibBuilder.loadTexts:
    apsTotalsGroupR.setStatus("current")

apsMapGroupR = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 3, 1, 9)
)
apsMapGroupR.setObjects(
      *(("APS-R-MIB", "apsMapGroupNameR"),
        ("APS-R-MIB", "apsMapChanNumberR"))
)
if mibBuilder.loadTexts:
    apsMapGroupR.setStatus("current")


# Notification objects

apsTrapSwitchoverR = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 2, 0, 1)
)
apsTrapSwitchoverR.setObjects(
      *(("APS-R-MIB", "apsChanSwitchoversR"),
        ("APS-R-MIB", "apsChanStatusR"))
)
if mibBuilder.loadTexts:
    apsTrapSwitchoverR.setStatus(
        "current"
    )

apsTrapModeMismatchR = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 2, 0, 2)
)
apsTrapModeMismatchR.setObjects(
      *(("APS-R-MIB", "apsStatusModeMismatchesR"),
        ("APS-R-MIB", "apsStatusCurrentR"))
)
if mibBuilder.loadTexts:
    apsTrapModeMismatchR.setStatus(
        "current"
    )

apsTrapChannelMismatchR = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 2, 0, 3)
)
apsTrapChannelMismatchR.setObjects(
      *(("APS-R-MIB", "apsStatusChannelMismatchesR"),
        ("APS-R-MIB", "apsStatusCurrentR"))
)
if mibBuilder.loadTexts:
    apsTrapChannelMismatchR.setStatus(
        "current"
    )

apsTrapPSBFr = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 2, 0, 4)
)
apsTrapPSBFr.setObjects(
      *(("APS-R-MIB", "apsStatusPSBFsR"),
        ("APS-R-MIB", "apsStatusCurrentR"))
)
if mibBuilder.loadTexts:
    apsTrapPSBFr.setStatus(
        "current"
    )

apsTrapFEPLFr = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 2, 0, 5)
)
apsTrapFEPLFr.setObjects(
      *(("APS-R-MIB", "apsStatusFEPLFsR"),
        ("APS-R-MIB", "apsStatusCurrentR"))
)
if mibBuilder.loadTexts:
    apsTrapFEPLFr.setStatus(
        "current"
    )


# Notifications groups

apsTrapOptionalR = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 3, 1, 10)
)
apsTrapOptionalR.setObjects(
      *(("APS-R-MIB", "apsTrapSwitchoverR"),
        ("APS-R-MIB", "apsTrapModeMismatchR"),
        ("APS-R-MIB", "apsTrapChannelMismatchR"),
        ("APS-R-MIB", "apsTrapPSBFr"),
        ("APS-R-MIB", "apsTrapFEPLFr"))
)
if mibBuilder.loadTexts:
    apsTrapOptionalR.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

apsComplianceR = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 164, 20, 2, 3, 2, 1)
)
apsComplianceR.setObjects(
      *(("APS-R-MIB", "apsConfigGeneralR"),
        ("APS-R-MIB", "apsStatusGeneralR"),
        ("APS-R-MIB", "apsChanGeneralR"))
)
if mibBuilder.loadTexts:
    apsComplianceR.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APS-R-MIB",
    **{"ApsK1K2": ApsK1K2,
       "ApsSwitchCommand": ApsSwitchCommand,
       "ApsControlCommand": ApsControlCommand,
       "apsMIBr": apsMIBr,
       "apsMIBObjectsR": apsMIBObjectsR,
       "apsConfigR": apsConfigR,
       "apsConfigGroupsR": apsConfigGroupsR,
       "apsConfigTableR": apsConfigTableR,
       "apsConfigEntryR": apsConfigEntryR,
       "apsConfigNameR": apsConfigNameR,
       "apsConfigRowStatusR": apsConfigRowStatusR,
       "apsConfigModeR": apsConfigModeR,
       "apsConfigSdBerThresholdR": apsConfigSdBerThresholdR,
       "apsConfigSfBerThresholdR": apsConfigSfBerThresholdR,
       "apsConfigWaitToRestoreR": apsConfigWaitToRestoreR,
       "apsConfigCreationTimeR": apsConfigCreationTimeR,
       "apsConfigOperDelayR": apsConfigOperDelayR,
       "apsStatusTableR": apsStatusTableR,
       "apsStatusEntryR": apsStatusEntryR,
       "apsStatusK1K2RcvR": apsStatusK1K2RcvR,
       "apsStatusK1K2TransR": apsStatusK1K2TransR,
       "apsStatusCurrentR": apsStatusCurrentR,
       "apsStatusModeMismatchesR": apsStatusModeMismatchesR,
       "apsStatusChannelMismatchesR": apsStatusChannelMismatchesR,
       "apsStatusPSBFsR": apsStatusPSBFsR,
       "apsStatusFEPLFsR": apsStatusFEPLFsR,
       "apsMapR": apsMapR,
       "apsChanLTEsR": apsChanLTEsR,
       "apsMapTableR": apsMapTableR,
       "apsMapEntryR": apsMapEntryR,
       "apsMapIfIndexR": apsMapIfIndexR,
       "apsMapGroupNameR": apsMapGroupNameR,
       "apsMapChanNumberR": apsMapChanNumberR,
       "apsChanConfigTableR": apsChanConfigTableR,
       "apsChanConfigEntryR": apsChanConfigEntryR,
       "apsChanGroupNameR": apsChanGroupNameR,
       "apsChanNumberR": apsChanNumberR,
       "apsChanRowStatusR": apsChanRowStatusR,
       "apsChanIfIndexR": apsChanIfIndexR,
       "apsChanPriorityR": apsChanPriorityR,
       "apsCommandTableR": apsCommandTableR,
       "apsCommandEntryR": apsCommandEntryR,
       "apsCommandSwitchR": apsCommandSwitchR,
       "apsCommandControlR": apsCommandControlR,
       "apsChanStatusTableR": apsChanStatusTableR,
       "apsChanStatusEntryR": apsChanStatusEntryR,
       "apsChanStatusR": apsChanStatusR,
       "apsChanSignalDegradesR": apsChanSignalDegradesR,
       "apsChanSignalFailuresR": apsChanSignalFailuresR,
       "apsChanSwitchoversR": apsChanSwitchoversR,
       "apsChanLastSwitchoverR": apsChanLastSwitchoverR,
       "apsMIBNotificationsR": apsMIBNotificationsR,
       "apsNotificationsPrefixR": apsNotificationsPrefixR,
       "apsTrapSwitchoverR": apsTrapSwitchoverR,
       "apsTrapModeMismatchR": apsTrapModeMismatchR,
       "apsTrapChannelMismatchR": apsTrapChannelMismatchR,
       "apsTrapPSBFr": apsTrapPSBFr,
       "apsTrapFEPLFr": apsTrapFEPLFr,
       "apsMIBConformanceR": apsMIBConformanceR,
       "apsGroupsR": apsGroupsR,
       "apsConfigGeneralR": apsConfigGeneralR,
       "apsConfigOneToNr": apsConfigOneToNr,
       "apsCommandOnePlusOneR": apsCommandOnePlusOneR,
       "apsCommandOneToNr": apsCommandOneToNr,
       "apsStatusGeneralR": apsStatusGeneralR,
       "apsChanGeneralR": apsChanGeneralR,
       "apsChanOneToNr": apsChanOneToNr,
       "apsTotalsGroupR": apsTotalsGroupR,
       "apsMapGroupR": apsMapGroupR,
       "apsTrapOptionalR": apsTrapOptionalR,
       "apsCompliancesR": apsCompliancesR,
       "apsComplianceR": apsComplianceR}
)
