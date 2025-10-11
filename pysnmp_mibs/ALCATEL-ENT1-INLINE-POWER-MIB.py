# SNMP MIB module (ALCATEL-ENT1-INLINE-POWER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel-ent1/ALCATEL-ENT1-INLINE-POWER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:10:01 2025
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

(softentIND1InLinePower,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-BASE",
    "softentIND1InLinePower")

(pethMainPseEntry,
 pethMainPsePower,
 pethPsePortEntry,
 pethPsePortGroupIndex,
 pethPsePortIndex) = mibBuilder.importSymbols(
    "POWER-ETHERNET-MIB",
    "pethMainPseEntry",
    "pethMainPsePower",
    "pethPsePortEntry",
    "pethPsePortGroupIndex",
    "pethPsePortIndex")

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

alcatelIND1INLINEPOWERMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1INLINEPOWERMIB.setRevisions(
        ("2007-04-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlaPethNotificationObjects_ObjectIdentity = ObjectIdentity
alaPethNotificationObjects = _AlaPethNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 0)
)
_AlaPethObjects_ObjectIdentity = ObjectIdentity
alaPethObjects = _AlaPethObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1)
)
_AlaPethPsePortTable_Object = MibTable
alaPethPsePortTable = _AlaPethPsePortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaPethPsePortTable.setStatus("current")
_AlaPethPsePortEntry_Object = MibTableRow
alaPethPsePortEntry = _AlaPethPsePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaPethPsePortEntry.setStatus("current")


class _AlaPethPsePortPowerMaximum_Type(Integer32):
    """Custom type alaPethPsePortPowerMaximum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3000, 60000),
    )


_AlaPethPsePortPowerMaximum_Type.__name__ = "Integer32"
_AlaPethPsePortPowerMaximum_Object = MibTableColumn
alaPethPsePortPowerMaximum = _AlaPethPsePortPowerMaximum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 1, 1, 1),
    _AlaPethPsePortPowerMaximum_Type()
)
alaPethPsePortPowerMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPethPsePortPowerMaximum.setStatus("current")


class _AlaPethPsePortPowerActual_Type(Integer32):
    """Custom type alaPethPsePortPowerActual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_AlaPethPsePortPowerActual_Type.__name__ = "Integer32"
_AlaPethPsePortPowerActual_Object = MibTableColumn
alaPethPsePortPowerActual = _AlaPethPsePortPowerActual_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 1, 1, 2),
    _AlaPethPsePortPowerActual_Type()
)
alaPethPsePortPowerActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPethPsePortPowerActual.setStatus("current")


class _AlaPethPsePortPowerStatus_Type(Integer32):
    """Custom type alaPethPsePortPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerOn", 1),
          ("powerOff", 2))
    )


_AlaPethPsePortPowerStatus_Type.__name__ = "Integer32"
_AlaPethPsePortPowerStatus_Object = MibTableColumn
alaPethPsePortPowerStatus = _AlaPethPsePortPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 1, 1, 3),
    _AlaPethPsePortPowerStatus_Type()
)
alaPethPsePortPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPethPsePortPowerStatus.setStatus("current")


class _AlaPethPsePortPowerClass_Type(Integer32):
    """Custom type alaPethPsePortPowerClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3),
          ("class4", 4),
          ("class5", 5))
    )


_AlaPethPsePortPowerClass_Type.__name__ = "Integer32"
_AlaPethPsePortPowerClass_Object = MibTableColumn
alaPethPsePortPowerClass = _AlaPethPsePortPowerClass_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 1, 1, 4),
    _AlaPethPsePortPowerClass_Type()
)
alaPethPsePortPowerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPethPsePortPowerClass.setStatus("current")
_AlaPethMainPseTable_Object = MibTable
alaPethMainPseTable = _AlaPethMainPseTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaPethMainPseTable.setStatus("current")
_AlaPethMainPseEntry_Object = MibTableRow
alaPethMainPseEntry = _AlaPethMainPseEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaPethMainPseEntry.setStatus("current")


class _AlaPethMainPseAdminStatus_Type(Integer32):
    """Custom type alaPethMainPseAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_AlaPethMainPseAdminStatus_Type.__name__ = "Integer32"
_AlaPethMainPseAdminStatus_Object = MibTableColumn
alaPethMainPseAdminStatus = _AlaPethMainPseAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 2, 1, 1),
    _AlaPethMainPseAdminStatus_Type()
)
alaPethMainPseAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPethMainPseAdminStatus.setStatus("current")


class _AlaPethMainPseMaxPower_Type(Integer32):
    """Custom type alaPethMainPseMaxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(37, 1500),
    )


_AlaPethMainPseMaxPower_Type.__name__ = "Integer32"
_AlaPethMainPseMaxPower_Object = MibTableColumn
alaPethMainPseMaxPower = _AlaPethMainPseMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 2, 1, 2),
    _AlaPethMainPseMaxPower_Type()
)
alaPethMainPseMaxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPethMainPseMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    alaPethMainPseMaxPower.setUnits("Watts")


class _AlaPethMainPsePriorityDisconnect_Type(Integer32):
    """Custom type alaPethMainPsePriorityDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPethMainPsePriorityDisconnect_Type.__name__ = "Integer32"
_AlaPethMainPsePriorityDisconnect_Object = MibTableColumn
alaPethMainPsePriorityDisconnect = _AlaPethMainPsePriorityDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 2, 1, 3),
    _AlaPethMainPsePriorityDisconnect_Type()
)
alaPethMainPsePriorityDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPethMainPsePriorityDisconnect.setStatus("current")


class _AlaPethMainPseCapacitorDetect_Type(Integer32):
    """Custom type alaPethMainPseCapacitorDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPethMainPseCapacitorDetect_Type.__name__ = "Integer32"
_AlaPethMainPseCapacitorDetect_Object = MibTableColumn
alaPethMainPseCapacitorDetect = _AlaPethMainPseCapacitorDetect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 2, 1, 4),
    _AlaPethMainPseCapacitorDetect_Type()
)
alaPethMainPseCapacitorDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPethMainPseCapacitorDetect.setStatus("current")


class _AlaPethMainPsePriority_Type(Integer32):
    """Custom type alaPethMainPsePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("high", 2),
          ("low", 3))
    )


_AlaPethMainPsePriority_Type.__name__ = "Integer32"
_AlaPethMainPsePriority_Object = MibTableColumn
alaPethMainPsePriority = _AlaPethMainPsePriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 2, 1, 5),
    _AlaPethMainPsePriority_Type()
)
alaPethMainPsePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPethMainPsePriority.setStatus("current")


class _AlaPethMainPseComboPort_Type(Integer32):
    """Custom type alaPethMainPseComboPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPethMainPseComboPort_Type.__name__ = "Integer32"
_AlaPethMainPseComboPort_Object = MibTableColumn
alaPethMainPseComboPort = _AlaPethMainPseComboPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 2, 1, 6),
    _AlaPethMainPseComboPort_Type()
)
alaPethMainPseComboPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPethMainPseComboPort.setStatus("current")


class _AlaPethMainPseClassDetection_Type(Integer32):
    """Custom type alaPethMainPseClassDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPethMainPseClassDetection_Type.__name__ = "Integer32"
_AlaPethMainPseClassDetection_Object = MibTableColumn
alaPethMainPseClassDetection = _AlaPethMainPseClassDetection_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 2, 1, 7),
    _AlaPethMainPseClassDetection_Type()
)
alaPethMainPseClassDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPethMainPseClassDetection.setStatus("current")
_AlaPethMainChassisTable_Object = MibTable
alaPethMainChassisTable = _AlaPethMainChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaPethMainChassisTable.setStatus("current")
_AlaPethMainChassisEntry_Object = MibTableRow
alaPethMainChassisEntry = _AlaPethMainChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 3, 1)
)
alaPethMainChassisEntry.setIndexNames(
    (0, "ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethMainChassisId"),
)
if mibBuilder.loadTexts:
    alaPethMainChassisEntry.setStatus("current")


class _AlaPethMainChassisId_Type(Integer32):
    """Custom type alaPethMainChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlaPethMainChassisId_Type.__name__ = "Integer32"
_AlaPethMainChassisId_Object = MibTableColumn
alaPethMainChassisId = _AlaPethMainChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 3, 1, 1),
    _AlaPethMainChassisId_Type()
)
alaPethMainChassisId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPethMainChassisId.setStatus("current")


class _AlaPethMainChassisPowerRedundancy_Type(Integer32):
    """Custom type alaPethMainChassisPowerRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPethMainChassisPowerRedundancy_Type.__name__ = "Integer32"
_AlaPethMainChassisPowerRedundancy_Object = MibTableColumn
alaPethMainChassisPowerRedundancy = _AlaPethMainChassisPowerRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 3, 1, 2),
    _AlaPethMainChassisPowerRedundancy_Type()
)
alaPethMainChassisPowerRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPethMainChassisPowerRedundancy.setStatus("current")


class _AlaPethMainChassisDynamicPowerManagement_Type(Integer32):
    """Custom type alaPethMainChassisDynamicPowerManagement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPethMainChassisDynamicPowerManagement_Type.__name__ = "Integer32"
_AlaPethMainChassisDynamicPowerManagement_Object = MibTableColumn
alaPethMainChassisDynamicPowerManagement = _AlaPethMainChassisDynamicPowerManagement_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 3, 1, 3),
    _AlaPethMainChassisDynamicPowerManagement_Type()
)
alaPethMainChassisDynamicPowerManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPethMainChassisDynamicPowerManagement.setStatus("current")


class _AlaPethMainChassisNumberOfPowerSupply_Type(Integer32):
    """Custom type alaPethMainChassisNumberOfPowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AlaPethMainChassisNumberOfPowerSupply_Type.__name__ = "Integer32"
_AlaPethMainChassisNumberOfPowerSupply_Object = MibTableColumn
alaPethMainChassisNumberOfPowerSupply = _AlaPethMainChassisNumberOfPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 3, 1, 4),
    _AlaPethMainChassisNumberOfPowerSupply_Type()
)
alaPethMainChassisNumberOfPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPethMainChassisNumberOfPowerSupply.setStatus("current")
if mibBuilder.loadTexts:
    alaPethMainChassisNumberOfPowerSupply.setUnits("scaler")
_AlaPethMainChassisAvailableReservePower_Type = Integer32
_AlaPethMainChassisAvailableReservePower_Object = MibTableColumn
alaPethMainChassisAvailableReservePower = _AlaPethMainChassisAvailableReservePower_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 3, 1, 5),
    _AlaPethMainChassisAvailableReservePower_Type()
)
alaPethMainChassisAvailableReservePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPethMainChassisAvailableReservePower.setStatus("current")
if mibBuilder.loadTexts:
    alaPethMainChassisAvailableReservePower.setUnits("watts")
_AlaPethPowerRuleTable_Object = MibTable
alaPethPowerRuleTable = _AlaPethPowerRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaPethPowerRuleTable.setStatus("current")
_AlaPethPowerRuleEntry_Object = MibTableRow
alaPethPowerRuleEntry = _AlaPethPowerRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 4, 1)
)
alaPethPowerRuleEntry.setIndexNames(
    (0, "ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPowerRuleName"),
)
if mibBuilder.loadTexts:
    alaPethPowerRuleEntry.setStatus("current")


class _AlaPethPowerRuleName_Type(SnmpAdminString):
    """Custom type alaPethPowerRuleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaPethPowerRuleName_Type.__name__ = "SnmpAdminString"
_AlaPethPowerRuleName_Object = MibTableColumn
alaPethPowerRuleName = _AlaPethPowerRuleName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 4, 1, 1),
    _AlaPethPowerRuleName_Type()
)
alaPethPowerRuleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPethPowerRuleName.setStatus("current")


class _AlaPethPowerRuleAdminStatus_Type(Integer32):
    """Custom type alaPethPowerRuleAdminStatus based on Integer32"""
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


_AlaPethPowerRuleAdminStatus_Type.__name__ = "Integer32"
_AlaPethPowerRuleAdminStatus_Object = MibTableColumn
alaPethPowerRuleAdminStatus = _AlaPethPowerRuleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 4, 1, 2),
    _AlaPethPowerRuleAdminStatus_Type()
)
alaPethPowerRuleAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPethPowerRuleAdminStatus.setStatus("current")


class _AlaPethPowerRulePowerStatus_Type(Integer32):
    """Custom type alaPethPowerRulePowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_AlaPethPowerRulePowerStatus_Type.__name__ = "Integer32"
_AlaPethPowerRulePowerStatus_Object = MibTableColumn
alaPethPowerRulePowerStatus = _AlaPethPowerRulePowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 4, 1, 3),
    _AlaPethPowerRulePowerStatus_Type()
)
alaPethPowerRulePowerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPethPowerRulePowerStatus.setStatus("current")


class _AlaPethPowerRuleAtMinute_Type(Integer32):
    """Custom type alaPethPowerRuleAtMinute based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 59),
    )


_AlaPethPowerRuleAtMinute_Type.__name__ = "Integer32"
_AlaPethPowerRuleAtMinute_Object = MibTableColumn
alaPethPowerRuleAtMinute = _AlaPethPowerRuleAtMinute_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 4, 1, 4),
    _AlaPethPowerRuleAtMinute_Type()
)
alaPethPowerRuleAtMinute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPethPowerRuleAtMinute.setStatus("current")
if mibBuilder.loadTexts:
    alaPethPowerRuleAtMinute.setUnits("minutes")


class _AlaPethPowerRuleAtTime_Type(Integer32):
    """Custom type alaPethPowerRuleAtTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1439),
    )


_AlaPethPowerRuleAtTime_Type.__name__ = "Integer32"
_AlaPethPowerRuleAtTime_Object = MibTableColumn
alaPethPowerRuleAtTime = _AlaPethPowerRuleAtTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 4, 1, 5),
    _AlaPethPowerRuleAtTime_Type()
)
alaPethPowerRuleAtTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPethPowerRuleAtTime.setStatus("current")
if mibBuilder.loadTexts:
    alaPethPowerRuleAtTime.setUnits("minutes")


class _AlaPethPowerRuleDaysOfWeek_Type(Bits):
    """Custom type alaPethPowerRuleDaysOfWeek based on Bits"""
    defaultBinValue = "1111111"

    namedValues = NamedValues(
        *(("sun", 0),
          ("mon", 1),
          ("tue", 2),
          ("wed", 3),
          ("thu", 4),
          ("fri", 5),
          ("sat", 6))
    )

_AlaPethPowerRuleDaysOfWeek_Type.__name__ = "Bits"
_AlaPethPowerRuleDaysOfWeek_Object = MibTableColumn
alaPethPowerRuleDaysOfWeek = _AlaPethPowerRuleDaysOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 4, 1, 6),
    _AlaPethPowerRuleDaysOfWeek_Type()
)
alaPethPowerRuleDaysOfWeek.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPethPowerRuleDaysOfWeek.setStatus("current")


class _AlaPethPowerRuleDaysOfMonth_Type(Bits):
    """Custom type alaPethPowerRuleDaysOfMonth based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("d1", 0),
          ("d2", 1),
          ("d3", 2),
          ("d4", 3),
          ("d5", 4),
          ("d6", 5),
          ("d7", 6),
          ("d8", 7),
          ("d9", 8),
          ("d10", 9),
          ("d11", 10),
          ("d12", 11),
          ("d13", 12),
          ("d14", 13),
          ("d15", 14),
          ("d16", 15),
          ("d17", 16),
          ("d18", 17),
          ("d19", 18),
          ("d20", 19),
          ("d21", 20),
          ("d22", 21),
          ("d23", 22),
          ("d24", 23),
          ("d25", 24),
          ("d26", 25),
          ("d27", 26),
          ("d28", 27),
          ("d29", 28),
          ("d30", 29),
          ("d31", 30))
    )

_AlaPethPowerRuleDaysOfMonth_Type.__name__ = "Bits"
_AlaPethPowerRuleDaysOfMonth_Object = MibTableColumn
alaPethPowerRuleDaysOfMonth = _AlaPethPowerRuleDaysOfMonth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 4, 1, 7),
    _AlaPethPowerRuleDaysOfMonth_Type()
)
alaPethPowerRuleDaysOfMonth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPethPowerRuleDaysOfMonth.setStatus("current")


class _AlaPethPowerRuleMonths_Type(Bits):
    """Custom type alaPethPowerRuleMonths based on Bits"""
    defaultBinValue = "111111111111"

    namedValues = NamedValues(
        *(("jan", 0),
          ("feb", 1),
          ("mar", 2),
          ("apr", 3),
          ("may", 4),
          ("jun", 5),
          ("jul", 6),
          ("aug", 7),
          ("sep", 8),
          ("oct", 9),
          ("nov", 10),
          ("dec", 11))
    )

_AlaPethPowerRuleMonths_Type.__name__ = "Bits"
_AlaPethPowerRuleMonths_Object = MibTableColumn
alaPethPowerRuleMonths = _AlaPethPowerRuleMonths_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 4, 1, 8),
    _AlaPethPowerRuleMonths_Type()
)
alaPethPowerRuleMonths.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPethPowerRuleMonths.setStatus("current")


class _AlaPethPowerRuleTimezone_Type(Integer32):
    """Custom type alaPethPowerRuleTimezone based on Integer32"""
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
        *(("localServer", 1),
          ("originatorServer", 2),
          ("utc", 3))
    )


_AlaPethPowerRuleTimezone_Type.__name__ = "Integer32"
_AlaPethPowerRuleTimezone_Object = MibTableColumn
alaPethPowerRuleTimezone = _AlaPethPowerRuleTimezone_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 4, 1, 9),
    _AlaPethPowerRuleTimezone_Type()
)
alaPethPowerRuleTimezone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPethPowerRuleTimezone.setStatus("current")
_AlaPethPowerRuleRowStatus_Type = RowStatus
_AlaPethPowerRuleRowStatus_Object = MibTableColumn
alaPethPowerRuleRowStatus = _AlaPethPowerRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 4, 1, 10),
    _AlaPethPowerRuleRowStatus_Type()
)
alaPethPowerRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPethPowerRuleRowStatus.setStatus("current")
_AlaPethPowerPolicyTable_Object = MibTable
alaPethPowerPolicyTable = _AlaPethPowerPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 5)
)
if mibBuilder.loadTexts:
    alaPethPowerPolicyTable.setStatus("current")
_AlaPethPowerPolicyEntry_Object = MibTableRow
alaPethPowerPolicyEntry = _AlaPethPowerPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 5, 1)
)
alaPethPowerPolicyEntry.setIndexNames(
    (0, "ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPowerPolicyName"),
    (0, "ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPowerRuleName"),
)
if mibBuilder.loadTexts:
    alaPethPowerPolicyEntry.setStatus("current")


class _AlaPethPowerPolicyName_Type(SnmpAdminString):
    """Custom type alaPethPowerPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaPethPowerPolicyName_Type.__name__ = "SnmpAdminString"
_AlaPethPowerPolicyName_Object = MibTableColumn
alaPethPowerPolicyName = _AlaPethPowerPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 5, 1, 1),
    _AlaPethPowerPolicyName_Type()
)
alaPethPowerPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPethPowerPolicyName.setStatus("current")
_AlaPethPowerPolicyRowStatus_Type = RowStatus
_AlaPethPowerPolicyRowStatus_Object = MibTableColumn
alaPethPowerPolicyRowStatus = _AlaPethPowerPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 5, 1, 2),
    _AlaPethPowerPolicyRowStatus_Type()
)
alaPethPowerPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPethPowerPolicyRowStatus.setStatus("current")
_AlaPethPowerPortTable_Object = MibTable
alaPethPowerPortTable = _AlaPethPowerPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 6)
)
if mibBuilder.loadTexts:
    alaPethPowerPortTable.setStatus("current")
_AlaPethPowerPortEntry_Object = MibTableRow
alaPethPowerPortEntry = _AlaPethPowerPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 6, 1)
)
alaPethPowerPortEntry.setIndexNames(
    (0, "POWER-ETHERNET-MIB", "pethPsePortGroupIndex"),
    (0, "POWER-ETHERNET-MIB", "pethPsePortIndex"),
)
if mibBuilder.loadTexts:
    alaPethPowerPortEntry.setStatus("current")


class _AlaPethPowerPortPolicyName_Type(SnmpAdminString):
    """Custom type alaPethPowerPortPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaPethPowerPortPolicyName_Type.__name__ = "SnmpAdminString"
_AlaPethPowerPortPolicyName_Object = MibTableColumn
alaPethPowerPortPolicyName = _AlaPethPowerPortPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 6, 1, 1),
    _AlaPethPowerPortPolicyName_Type()
)
alaPethPowerPortPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPethPowerPortPolicyName.setStatus("current")
_AlaPethPowerPortRowStatus_Type = RowStatus
_AlaPethPowerPortRowStatus_Object = MibTableColumn
alaPethPowerPortRowStatus = _AlaPethPowerPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 6, 1, 2),
    _AlaPethPowerPortRowStatus_Type()
)
alaPethPowerPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPethPowerPortRowStatus.setStatus("current")
_AlaPethPowerSlotTable_Object = MibTable
alaPethPowerSlotTable = _AlaPethPowerSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 7)
)
if mibBuilder.loadTexts:
    alaPethPowerSlotTable.setStatus("current")
_AlaPethPowerSlotEntry_Object = MibTableRow
alaPethPowerSlotEntry = _AlaPethPowerSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 7, 1)
)
alaPethPowerSlotEntry.setIndexNames(
    (0, "POWER-ETHERNET-MIB", "pethPsePortGroupIndex"),
)
if mibBuilder.loadTexts:
    alaPethPowerSlotEntry.setStatus("current")


class _AlaPethPowerSlotPolicyName_Type(SnmpAdminString):
    """Custom type alaPethPowerSlotPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaPethPowerSlotPolicyName_Type.__name__ = "SnmpAdminString"
_AlaPethPowerSlotPolicyName_Object = MibTableColumn
alaPethPowerSlotPolicyName = _AlaPethPowerSlotPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 7, 1, 1),
    _AlaPethPowerSlotPolicyName_Type()
)
alaPethPowerSlotPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPethPowerSlotPolicyName.setStatus("current")
_AlaPethPowerSlotRowStatus_Type = RowStatus
_AlaPethPowerSlotRowStatus_Object = MibTableColumn
alaPethPowerSlotRowStatus = _AlaPethPowerSlotRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 7, 1, 2),
    _AlaPethPowerSlotRowStatus_Type()
)
alaPethPowerSlotRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPethPowerSlotRowStatus.setStatus("current")
_AlaPethUpdate_ObjectIdentity = ObjectIdentity
alaPethUpdate = _AlaPethUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 8)
)


class _AlaPethUpdatePortGroupIndex_Type(Integer32):
    """Custom type alaPethUpdatePortGroupIndex based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_AlaPethUpdatePortGroupIndex_Type.__name__ = "Integer32"
_AlaPethUpdatePortGroupIndex_Object = MibScalar
alaPethUpdatePortGroupIndex = _AlaPethUpdatePortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 8, 1),
    _AlaPethUpdatePortGroupIndex_Type()
)
alaPethUpdatePortGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPethUpdatePortGroupIndex.setStatus("current")


class _AlaPethUpdateFilename_Type(SnmpAdminString):
    """Custom type alaPethUpdateFilename based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaPethUpdateFilename_Type.__name__ = "SnmpAdminString"
_AlaPethUpdateFilename_Object = MibScalar
alaPethUpdateFilename = _AlaPethUpdateFilename_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 8, 2),
    _AlaPethUpdateFilename_Type()
)
alaPethUpdateFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPethUpdateFilename.setStatus("current")


class _AlaPethUpdateAction_Type(Integer32):
    """Custom type alaPethUpdateAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("doUpdate", 2))
    )


_AlaPethUpdateAction_Type.__name__ = "Integer32"
_AlaPethUpdateAction_Object = MibScalar
alaPethUpdateAction = _AlaPethUpdateAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 8, 3),
    _AlaPethUpdateAction_Type()
)
alaPethUpdateAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPethUpdateAction.setStatus("current")


class _AlaPethUpdateStatus_Type(Integer32):
    """Custom type alaPethUpdateStatus based on Integer32"""
    defaultValue = 4

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
        *(("inProgress", 1),
          ("doneOk", 2),
          ("doneNotOk", 3),
          ("noOp", 4))
    )


_AlaPethUpdateStatus_Type.__name__ = "Integer32"
_AlaPethUpdateStatus_Object = MibScalar
alaPethUpdateStatus = _AlaPethUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 8, 4),
    _AlaPethUpdateStatus_Type()
)
alaPethUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPethUpdateStatus.setStatus("current")


class _AlaPethUpdateErrorCode_Type(Integer32):
    """Custom type alaPethUpdateErrorCode based on Integer32"""
    defaultValue = 1

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
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("notAllSlotsUpdated", 2),
          ("noUpdateStatusErr", 3),
          ("programmingImageBadErr", 4),
          ("programmingFailed", 5),
          ("controllerFileChecksumErr", 6),
          ("controllerFileReadErr", 7),
          ("controllerFileStatusErr", 8),
          ("controllerFileWriteErr", 9),
          ("dataErr", 10),
          ("dataConflictErr", 11),
          ("invalidResponseErr", 12),
          ("programUndefinedErr", 13))
    )


_AlaPethUpdateErrorCode_Type.__name__ = "Integer32"
_AlaPethUpdateErrorCode_Object = MibScalar
alaPethUpdateErrorCode = _AlaPethUpdateErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 8, 5),
    _AlaPethUpdateErrorCode_Type()
)
alaPethUpdateErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPethUpdateErrorCode.setStatus("current")


class _AlaPethUpdateErrorString_Type(SnmpAdminString):
    """Custom type alaPethUpdateErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaPethUpdateErrorString_Type.__name__ = "SnmpAdminString"
_AlaPethUpdateErrorString_Object = MibScalar
alaPethUpdateErrorString = _AlaPethUpdateErrorString_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 1, 8, 6),
    _AlaPethUpdateErrorString_Type()
)
alaPethUpdateErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPethUpdateErrorString.setStatus("current")
_AlaPethConformance_ObjectIdentity = ObjectIdentity
alaPethConformance = _AlaPethConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 2)
)
_AlaPethCompliances_ObjectIdentity = ObjectIdentity
alaPethCompliances = _AlaPethCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 2, 1)
)
_AlaPethGroups_ObjectIdentity = ObjectIdentity
alaPethGroups = _AlaPethGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 2, 2)
)
pethPsePortEntry.registerAugmentions(
    ("ALCATEL-ENT1-INLINE-POWER-MIB",
     "alaPethPsePortEntry")
)
alaPethPsePortEntry.setIndexNames(*pethPsePortEntry.getIndexNames())
pethMainPseEntry.registerAugmentions(
    ("ALCATEL-ENT1-INLINE-POWER-MIB",
     "alaPethMainPseEntry")
)
alaPethMainPseEntry.setIndexNames(*pethMainPseEntry.getIndexNames())

# Managed Objects groups

alaPethPsePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 2, 2, 1)
)
alaPethPsePortGroup.setObjects(
      *(("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPsePortPowerMaximum"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPsePortPowerActual"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPsePortPowerStatus"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPsePortPowerClass"))
)
if mibBuilder.loadTexts:
    alaPethPsePortGroup.setStatus("current")

alaPethMainPseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 2, 2, 2)
)
alaPethMainPseGroup.setObjects(
      *(("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethMainPseAdminStatus"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethMainPseMaxPower"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethMainPsePriorityDisconnect"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethMainPseCapacitorDetect"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethMainPsePriority"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethMainPseComboPort"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethMainPseClassDetection"))
)
if mibBuilder.loadTexts:
    alaPethMainPseGroup.setStatus("current")

alaPethMainChassisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 2, 2, 3)
)
alaPethMainChassisGroup.setObjects(
      *(("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethMainChassisPowerRedundancy"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethMainChassisDynamicPowerManagement"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethMainChassisNumberOfPowerSupply"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethMainChassisAvailableReservePower"))
)
if mibBuilder.loadTexts:
    alaPethMainChassisGroup.setStatus("current")

alaPethPowerRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 2, 2, 4)
)
alaPethPowerRuleGroup.setObjects(
      *(("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPowerRuleName"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPowerRuleAdminStatus"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPowerRulePowerStatus"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPowerRuleAtMinute"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPowerRuleDaysOfWeek"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPowerRuleDaysOfMonth"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPowerRuleMonths"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPowerRuleTimezone"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPowerRuleRowStatus"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPowerRuleAtTime"))
)
if mibBuilder.loadTexts:
    alaPethPowerRuleGroup.setStatus("current")

alaPethPowerPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 2, 2, 5)
)
alaPethPowerPolicyGroup.setObjects(
    ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPowerPolicyRowStatus")
)
if mibBuilder.loadTexts:
    alaPethPowerPolicyGroup.setStatus("current")

alaPethPowerPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 2, 2, 6)
)
alaPethPowerPortGroup.setObjects(
      *(("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPowerPortPolicyName"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPowerPortRowStatus"))
)
if mibBuilder.loadTexts:
    alaPethPowerPortGroup.setStatus("current")

alaPethPowerSlotGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 2, 2, 7)
)
alaPethPowerSlotGroup.setObjects(
      *(("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPowerSlotPolicyName"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPowerSlotRowStatus"))
)
if mibBuilder.loadTexts:
    alaPethPowerSlotGroup.setStatus("current")

alaPethUpdateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 2, 2, 8)
)
alaPethUpdateGroup.setObjects(
      *(("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethUpdatePortGroupIndex"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethUpdateFilename"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethUpdateAction"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethUpdateStatus"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethUpdateErrorCode"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethUpdateErrorString"))
)
if mibBuilder.loadTexts:
    alaPethUpdateGroup.setStatus("current")


# Notification objects

alaPethPwrSupplyConflictTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 0, 1)
)
alaPethPwrSupplyConflictTrap.setObjects(
    ("POWER-ETHERNET-MIB", "pethPsePortGroupIndex")
)
if mibBuilder.loadTexts:
    alaPethPwrSupplyConflictTrap.setStatus(
        "current"
    )

alaPethPwrSupplyNotSupportedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 0, 2)
)
alaPethPwrSupplyNotSupportedTrap.setObjects(
      *(("POWER-ETHERNET-MIB", "pethPsePortGroupIndex"),
        ("POWER-ETHERNET-MIB", "pethPsePortIndex"))
)
if mibBuilder.loadTexts:
    alaPethPwrSupplyNotSupportedTrap.setStatus(
        "current"
    )

pethMainPowerUsageNIFailNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 0, 3)
)
pethMainPowerUsageNIFailNotification.setObjects(
      *(("POWER-ETHERNET-MIB", "pethPsePortGroupIndex"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethMainChassisNumberOfPowerSupply"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethMainChassisPowerRedundancy"),
        ("POWER-ETHERNET-MIB", "pethMainPsePower"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethMainPseMaxPower"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethMainChassisAvailableReservePower"))
)
if mibBuilder.loadTexts:
    pethMainPowerUsageNIFailNotification.setStatus(
        "current"
    )


# Notifications groups

pethTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 2, 2, 9)
)
pethTrapsGroup.setObjects(
      *(("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPwrSupplyConflictTrap"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPwrSupplyNotSupportedTrap"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "pethMainPowerUsageNIFailNotification"))
)
if mibBuilder.loadTexts:
    pethTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alaPethCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 2, 1, 1)
)
alaPethCompliance.setObjects(
      *(("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPsePortGroup"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethMainPseGroup"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethMainChassisGroup"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPowerRuleGroup"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPowerPolicyGroup"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPowerPortGroup"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPowerSlotGroup"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethUpdateGroup"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "pethTrapsGroup"))
)
if mibBuilder.loadTexts:
    alaPethCompliance.setStatus(
        "current"
    )

alaPethPseCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 1, 2, 1, 2)
)
alaPethPseCompliance.setObjects(
      *(("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPsePortGroup"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethMainPseGroup"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethMainChassisGroup"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPowerRuleGroup"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPowerPolicyGroup"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPowerPortGroup"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethPowerSlotGroup"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "alaPethUpdateGroup"),
        ("ALCATEL-ENT1-INLINE-POWER-MIB", "pethTrapsGroup"))
)
if mibBuilder.loadTexts:
    alaPethPseCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-ENT1-INLINE-POWER-MIB",
    **{"alcatelIND1INLINEPOWERMIB": alcatelIND1INLINEPOWERMIB,
       "alaPethNotificationObjects": alaPethNotificationObjects,
       "alaPethPwrSupplyConflictTrap": alaPethPwrSupplyConflictTrap,
       "alaPethPwrSupplyNotSupportedTrap": alaPethPwrSupplyNotSupportedTrap,
       "pethMainPowerUsageNIFailNotification": pethMainPowerUsageNIFailNotification,
       "alaPethObjects": alaPethObjects,
       "alaPethPsePortTable": alaPethPsePortTable,
       "alaPethPsePortEntry": alaPethPsePortEntry,
       "alaPethPsePortPowerMaximum": alaPethPsePortPowerMaximum,
       "alaPethPsePortPowerActual": alaPethPsePortPowerActual,
       "alaPethPsePortPowerStatus": alaPethPsePortPowerStatus,
       "alaPethPsePortPowerClass": alaPethPsePortPowerClass,
       "alaPethMainPseTable": alaPethMainPseTable,
       "alaPethMainPseEntry": alaPethMainPseEntry,
       "alaPethMainPseAdminStatus": alaPethMainPseAdminStatus,
       "alaPethMainPseMaxPower": alaPethMainPseMaxPower,
       "alaPethMainPsePriorityDisconnect": alaPethMainPsePriorityDisconnect,
       "alaPethMainPseCapacitorDetect": alaPethMainPseCapacitorDetect,
       "alaPethMainPsePriority": alaPethMainPsePriority,
       "alaPethMainPseComboPort": alaPethMainPseComboPort,
       "alaPethMainPseClassDetection": alaPethMainPseClassDetection,
       "alaPethMainChassisTable": alaPethMainChassisTable,
       "alaPethMainChassisEntry": alaPethMainChassisEntry,
       "alaPethMainChassisId": alaPethMainChassisId,
       "alaPethMainChassisPowerRedundancy": alaPethMainChassisPowerRedundancy,
       "alaPethMainChassisDynamicPowerManagement": alaPethMainChassisDynamicPowerManagement,
       "alaPethMainChassisNumberOfPowerSupply": alaPethMainChassisNumberOfPowerSupply,
       "alaPethMainChassisAvailableReservePower": alaPethMainChassisAvailableReservePower,
       "alaPethPowerRuleTable": alaPethPowerRuleTable,
       "alaPethPowerRuleEntry": alaPethPowerRuleEntry,
       "alaPethPowerRuleName": alaPethPowerRuleName,
       "alaPethPowerRuleAdminStatus": alaPethPowerRuleAdminStatus,
       "alaPethPowerRulePowerStatus": alaPethPowerRulePowerStatus,
       "alaPethPowerRuleAtMinute": alaPethPowerRuleAtMinute,
       "alaPethPowerRuleAtTime": alaPethPowerRuleAtTime,
       "alaPethPowerRuleDaysOfWeek": alaPethPowerRuleDaysOfWeek,
       "alaPethPowerRuleDaysOfMonth": alaPethPowerRuleDaysOfMonth,
       "alaPethPowerRuleMonths": alaPethPowerRuleMonths,
       "alaPethPowerRuleTimezone": alaPethPowerRuleTimezone,
       "alaPethPowerRuleRowStatus": alaPethPowerRuleRowStatus,
       "alaPethPowerPolicyTable": alaPethPowerPolicyTable,
       "alaPethPowerPolicyEntry": alaPethPowerPolicyEntry,
       "alaPethPowerPolicyName": alaPethPowerPolicyName,
       "alaPethPowerPolicyRowStatus": alaPethPowerPolicyRowStatus,
       "alaPethPowerPortTable": alaPethPowerPortTable,
       "alaPethPowerPortEntry": alaPethPowerPortEntry,
       "alaPethPowerPortPolicyName": alaPethPowerPortPolicyName,
       "alaPethPowerPortRowStatus": alaPethPowerPortRowStatus,
       "alaPethPowerSlotTable": alaPethPowerSlotTable,
       "alaPethPowerSlotEntry": alaPethPowerSlotEntry,
       "alaPethPowerSlotPolicyName": alaPethPowerSlotPolicyName,
       "alaPethPowerSlotRowStatus": alaPethPowerSlotRowStatus,
       "alaPethUpdate": alaPethUpdate,
       "alaPethUpdatePortGroupIndex": alaPethUpdatePortGroupIndex,
       "alaPethUpdateFilename": alaPethUpdateFilename,
       "alaPethUpdateAction": alaPethUpdateAction,
       "alaPethUpdateStatus": alaPethUpdateStatus,
       "alaPethUpdateErrorCode": alaPethUpdateErrorCode,
       "alaPethUpdateErrorString": alaPethUpdateErrorString,
       "alaPethConformance": alaPethConformance,
       "alaPethCompliances": alaPethCompliances,
       "alaPethCompliance": alaPethCompliance,
       "alaPethPseCompliance": alaPethPseCompliance,
       "alaPethGroups": alaPethGroups,
       "alaPethPsePortGroup": alaPethPsePortGroup,
       "alaPethMainPseGroup": alaPethMainPseGroup,
       "alaPethMainChassisGroup": alaPethMainChassisGroup,
       "alaPethPowerRuleGroup": alaPethPowerRuleGroup,
       "alaPethPowerPolicyGroup": alaPethPowerPolicyGroup,
       "alaPethPowerPortGroup": alaPethPowerPortGroup,
       "alaPethPowerSlotGroup": alaPethPowerSlotGroup,
       "alaPethUpdateGroup": alaPethUpdateGroup,
       "pethTrapsGroup": pethTrapsGroup}
)
