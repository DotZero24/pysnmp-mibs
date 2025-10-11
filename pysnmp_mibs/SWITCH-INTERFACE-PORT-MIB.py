# SNMP MIB module (SWITCH-INTERFACE-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/SWITCH-INTERFACE-PORT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:35:58 2025
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

(rcSystem,) = mibBuilder.importSymbols(
    "SWITCH-SYSTEM-MIB",
    "rcSystem")

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

rcIfPortInfoConfig = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7)
)
if mibBuilder.loadTexts:
    rcIfPortInfoConfig.setRevisions(
        ("1908-12-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcIfPortPHYInfoConfig_ObjectIdentity = ObjectIdentity
rcIfPortPHYInfoConfig = _RcIfPortPHYInfoConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1)
)
_RcIfPortPHYNotifications_ObjectIdentity = ObjectIdentity
rcIfPortPHYNotifications = _RcIfPortPHYNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 1)
)
_RcIfPortPHYInfomation_ObjectIdentity = ObjectIdentity
rcIfPortPHYInfomation = _RcIfPortPHYInfomation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2)
)
_RcIfPortPHYTable_Object = MibTable
rcIfPortPHYTable = _RcIfPortPHYTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rcIfPortPHYTable.setStatus("current")
_RcIfPortPHYEntry_Object = MibTableRow
rcIfPortPHYEntry = _RcIfPortPHYEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 1, 1)
)
rcIfPortPHYEntry.setIndexNames(
    (0, "SWITCH-INTERFACE-PORT-MIB", "rcIfPortPHYIndex"),
)
if mibBuilder.loadTexts:
    rcIfPortPHYEntry.setStatus("current")
_RcIfPortPHYIndex_Type = Integer32
_RcIfPortPHYIndex_Object = MibTableColumn
rcIfPortPHYIndex = _RcIfPortPHYIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 1, 1, 1),
    _RcIfPortPHYIndex_Type()
)
rcIfPortPHYIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIfPortPHYIndex.setStatus("current")
_RcIfPortPHYExistence_Type = TruthValue
_RcIfPortPHYExistence_Object = MibTableColumn
rcIfPortPHYExistence = _RcIfPortPHYExistence_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 1, 1, 2),
    _RcIfPortPHYExistence_Type()
)
rcIfPortPHYExistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIfPortPHYExistence.setStatus("current")
_RcIfPortPHYMAUNum_Type = Integer32
_RcIfPortPHYMAUNum_Object = MibTableColumn
rcIfPortPHYMAUNum = _RcIfPortPHYMAUNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 1, 1, 3),
    _RcIfPortPHYMAUNum_Type()
)
rcIfPortPHYMAUNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIfPortPHYMAUNum.setStatus("current")


class _RcIfPortPHYAdminStatus_Type(Integer32):
    """Custom type rcIfPortPHYAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_RcIfPortPHYAdminStatus_Type.__name__ = "Integer32"
_RcIfPortPHYAdminStatus_Object = MibTableColumn
rcIfPortPHYAdminStatus = _RcIfPortPHYAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 1, 1, 4),
    _RcIfPortPHYAdminStatus_Type()
)
rcIfPortPHYAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIfPortPHYAdminStatus.setStatus("current")


class _RcIfPortPHYOperStatus_Type(Integer32):
    """Custom type rcIfPortPHYOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_RcIfPortPHYOperStatus_Type.__name__ = "Integer32"
_RcIfPortPHYOperStatus_Object = MibTableColumn
rcIfPortPHYOperStatus = _RcIfPortPHYOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 1, 1, 5),
    _RcIfPortPHYOperStatus_Type()
)
rcIfPortPHYOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIfPortPHYOperStatus.setStatus("current")


class _RcIfPortPHYSpeedGet_Type(Integer32):
    """Custom type rcIfPortPHYSpeedGet based on Integer32"""
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
        *(("illegal", 0),
          ("unknown", 1),
          ("speed-10M", 2),
          ("speed-100M", 3),
          ("speed-1000M", 4),
          ("speed-10G", 5))
    )


_RcIfPortPHYSpeedGet_Type.__name__ = "Integer32"
_RcIfPortPHYSpeedGet_Object = MibTableColumn
rcIfPortPHYSpeedGet = _RcIfPortPHYSpeedGet_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 1, 1, 6),
    _RcIfPortPHYSpeedGet_Type()
)
rcIfPortPHYSpeedGet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIfPortPHYSpeedGet.setStatus("current")


class _RcIfPortPHYDuplexGet_Type(Integer32):
    """Custom type rcIfPortPHYDuplexGet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("illegal", 0),
          ("unknown", 1),
          ("half", 2),
          ("full", 3))
    )


_RcIfPortPHYDuplexGet_Type.__name__ = "Integer32"
_RcIfPortPHYDuplexGet_Object = MibTableColumn
rcIfPortPHYDuplexGet = _RcIfPortPHYDuplexGet_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 1, 1, 7),
    _RcIfPortPHYDuplexGet_Type()
)
rcIfPortPHYDuplexGet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIfPortPHYDuplexGet.setStatus("current")
_RcIfPortPHYFlowControlRecvStatus_Type = EnableVar
_RcIfPortPHYFlowControlRecvStatus_Object = MibTableColumn
rcIfPortPHYFlowControlRecvStatus = _RcIfPortPHYFlowControlRecvStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 1, 1, 8),
    _RcIfPortPHYFlowControlRecvStatus_Type()
)
rcIfPortPHYFlowControlRecvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIfPortPHYFlowControlRecvStatus.setStatus("current")
_RcIfPortPHYFlowControlSendStatus_Type = EnableVar
_RcIfPortPHYFlowControlSendStatus_Object = MibTableColumn
rcIfPortPHYFlowControlSendStatus = _RcIfPortPHYFlowControlSendStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 1, 1, 9),
    _RcIfPortPHYFlowControlSendStatus_Type()
)
rcIfPortPHYFlowControlSendStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIfPortPHYFlowControlSendStatus.setStatus("current")


class _RcIfPortPHYMdiStatus_Type(Integer32):
    """Custom type rcIfPortPHYMdiStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("illegal", 0),
          ("unknown", 1),
          ("normal", 2),
          ("xover", 3))
    )


_RcIfPortPHYMdiStatus_Type.__name__ = "Integer32"
_RcIfPortPHYMdiStatus_Object = MibTableColumn
rcIfPortPHYMdiStatus = _RcIfPortPHYMdiStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 1, 1, 10),
    _RcIfPortPHYMdiStatus_Type()
)
rcIfPortPHYMdiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIfPortPHYMdiStatus.setStatus("current")
_RcIfPortPHYActiveMAUIndex_Type = Integer32
_RcIfPortPHYActiveMAUIndex_Object = MibTableColumn
rcIfPortPHYActiveMAUIndex = _RcIfPortPHYActiveMAUIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 1, 1, 11),
    _RcIfPortPHYActiveMAUIndex_Type()
)
rcIfPortPHYActiveMAUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIfPortPHYActiveMAUIndex.setStatus("current")


class _RcComboPortMediaMode_Type(Integer32):
    """Custom type rcComboPortMediaMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-support", 0),
          ("auto", 1),
          ("fiber-forced", 2),
          ("copper-forced", 3))
    )


_RcComboPortMediaMode_Type.__name__ = "Integer32"
_RcComboPortMediaMode_Object = MibTableColumn
rcComboPortMediaMode = _RcComboPortMediaMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 1, 1, 12),
    _RcComboPortMediaMode_Type()
)
rcComboPortMediaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcComboPortMediaMode.setStatus("mandatory")


class _RcComboPortMediaPriority_Type(Integer32):
    """Custom type rcComboPortMediaPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-support", 0),
          ("fiber", 1),
          ("copper", 2))
    )


_RcComboPortMediaPriority_Type.__name__ = "Integer32"
_RcComboPortMediaPriority_Object = MibTableColumn
rcComboPortMediaPriority = _RcComboPortMediaPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 1, 1, 13),
    _RcComboPortMediaPriority_Type()
)
rcComboPortMediaPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcComboPortMediaPriority.setStatus("mandatory")


class _RcComboPortMediaActive_Type(Integer32):
    """Custom type rcComboPortMediaActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", 0),
          ("fiber", 1),
          ("copper", 2))
    )


_RcComboPortMediaActive_Type.__name__ = "Integer32"
_RcComboPortMediaActive_Object = MibTableColumn
rcComboPortMediaActive = _RcComboPortMediaActive_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 1, 1, 14),
    _RcComboPortMediaActive_Type()
)
rcComboPortMediaActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcComboPortMediaActive.setStatus("current")


class _RcIfPortSfpAutoDetect_Type(Integer32):
    """Custom type rcIfPortSfpAutoDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RcIfPortSfpAutoDetect_Type.__name__ = "Integer32"
_RcIfPortSfpAutoDetect_Object = MibTableColumn
rcIfPortSfpAutoDetect = _RcIfPortSfpAutoDetect_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 1, 1, 15),
    _RcIfPortSfpAutoDetect_Type()
)
rcIfPortSfpAutoDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIfPortSfpAutoDetect.setStatus("mandatory")


class _RcIfPortSfpPortTypeGet_Type(Integer32):
    """Custom type rcIfPortSfpPortTypeGet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("copper", 1),
          ("fiber100", 2),
          ("fiber1000", 3),
          ("fiber10000", 4))
    )


_RcIfPortSfpPortTypeGet_Type.__name__ = "Integer32"
_RcIfPortSfpPortTypeGet_Object = MibTableColumn
rcIfPortSfpPortTypeGet = _RcIfPortSfpPortTypeGet_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 1, 1, 16),
    _RcIfPortSfpPortTypeGet_Type()
)
rcIfPortSfpPortTypeGet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIfPortSfpPortTypeGet.setStatus("mandatory")


class _RcIfPortPHYEEEAutoGet_Type(Integer32):
    """Custom type rcIfPortPHYEEEAutoGet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-support", 0),
          ("enable", 1),
          ("disable", 2))
    )


_RcIfPortPHYEEEAutoGet_Type.__name__ = "Integer32"
_RcIfPortPHYEEEAutoGet_Object = MibTableColumn
rcIfPortPHYEEEAutoGet = _RcIfPortPHYEEEAutoGet_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 1, 1, 17),
    _RcIfPortPHYEEEAutoGet_Type()
)
rcIfPortPHYEEEAutoGet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIfPortPHYEEEAutoGet.setStatus("mandatory")
_RcIfPortMAUTable_Object = MibTable
rcIfPortMAUTable = _RcIfPortMAUTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 2)
)
if mibBuilder.loadTexts:
    rcIfPortMAUTable.setStatus("current")
_RcIfPortMAUEntry_Object = MibTableRow
rcIfPortMAUEntry = _RcIfPortMAUEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 2, 1)
)
rcIfPortMAUEntry.setIndexNames(
    (0, "SWITCH-INTERFACE-PORT-MIB", "rcIfPortPHYIndex"),
    (0, "SWITCH-INTERFACE-PORT-MIB", "rcIfPortMAUIndex"),
)
if mibBuilder.loadTexts:
    rcIfPortMAUEntry.setStatus("current")
_RcIfPortMAUIndex_Type = Integer32
_RcIfPortMAUIndex_Object = MibTableColumn
rcIfPortMAUIndex = _RcIfPortMAUIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 2, 1, 1),
    _RcIfPortMAUIndex_Type()
)
rcIfPortMAUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIfPortMAUIndex.setStatus("current")


class _RcIfPortMAUType_Type(Integer32):
    """Custom type rcIfPortMAUType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              5,
              16,
              18,
              22,
              30,
              31,
              33,
              37,
              99,
              100,
              101)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("dot3-10BASE-T", 5),
          ("dot3-100BASE-TX", 16),
          ("dot3-100BASE-FX", 18),
          ("dot3-1000BASE-X", 22),
          ("dot3-1000BASE-T", 30),
          ("dot3-10GBASE-X", 31),
          ("dot3-10GBASE-R", 33),
          ("dot3-10GBASE-W", 37),
          ("rc-1000BASE-P", 99),
          ("dot3-1000BASE-T1", 100),
          ("dot3-1000BASE-T2", 101))
    )


_RcIfPortMAUType_Type.__name__ = "Integer32"
_RcIfPortMAUType_Object = MibTableColumn
rcIfPortMAUType = _RcIfPortMAUType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 2, 1, 2),
    _RcIfPortMAUType_Type()
)
rcIfPortMAUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIfPortMAUType.setStatus("current")


class _RcIfPortMAUConnectorType_Type(Integer32):
    """Custom type rcIfPortMAUConnectorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("other", 1),
          ("sfp", 2),
          ("sfp-plus", 3))
    )


_RcIfPortMAUConnectorType_Type.__name__ = "Integer32"
_RcIfPortMAUConnectorType_Object = MibTableColumn
rcIfPortMAUConnectorType = _RcIfPortMAUConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 2, 1, 3),
    _RcIfPortMAUConnectorType_Type()
)
rcIfPortMAUConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIfPortMAUConnectorType.setStatus("current")


class _RcIfPortMAUConnectorStatus_Type(Integer32):
    """Custom type rcIfPortMAUConnectorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("error", 1),
          ("not-present", 2),
          ("present", 3))
    )


_RcIfPortMAUConnectorStatus_Type.__name__ = "Integer32"
_RcIfPortMAUConnectorStatus_Object = MibTableColumn
rcIfPortMAUConnectorStatus = _RcIfPortMAUConnectorStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 2, 1, 4),
    _RcIfPortMAUConnectorStatus_Type()
)
rcIfPortMAUConnectorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIfPortMAUConnectorStatus.setStatus("current")


class _RcIfPortMAUSpeedSet_Type(Integer32):
    """Custom type rcIfPortMAUSpeedSet based on Integer32"""
    defaultValue = 1

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
        *(("auto-negotiate", 1),
          ("speed-10M", 2),
          ("speed-100M", 3),
          ("speed-1000M", 4),
          ("speed-10G", 5))
    )


_RcIfPortMAUSpeedSet_Type.__name__ = "Integer32"
_RcIfPortMAUSpeedSet_Object = MibTableColumn
rcIfPortMAUSpeedSet = _RcIfPortMAUSpeedSet_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 2, 1, 5),
    _RcIfPortMAUSpeedSet_Type()
)
rcIfPortMAUSpeedSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIfPortMAUSpeedSet.setStatus("current")


class _RcIfPortMAUDuplexSet_Type(Integer32):
    """Custom type rcIfPortMAUDuplexSet based on Integer32"""
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
        *(("auto-negotiate", 1),
          ("half", 2),
          ("full", 3))
    )


_RcIfPortMAUDuplexSet_Type.__name__ = "Integer32"
_RcIfPortMAUDuplexSet_Object = MibTableColumn
rcIfPortMAUDuplexSet = _RcIfPortMAUDuplexSet_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 2, 1, 6),
    _RcIfPortMAUDuplexSet_Type()
)
rcIfPortMAUDuplexSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIfPortMAUDuplexSet.setStatus("current")


class _RcIfPortMAUFlowControlEnable_Type(EnableVar):
    """Custom type rcIfPortMAUFlowControlEnable based on EnableVar"""
    defaultValue = 2


_RcIfPortMAUFlowControlEnable_Type.__name__ = "EnableVar"
_RcIfPortMAUFlowControlEnable_Object = MibTableColumn
rcIfPortMAUFlowControlEnable = _RcIfPortMAUFlowControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 2, 1, 7),
    _RcIfPortMAUFlowControlEnable_Type()
)
rcIfPortMAUFlowControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIfPortMAUFlowControlEnable.setStatus("current")


class _RcIfPortMAUFlowControlRecvEnable_Type(EnableVar):
    """Custom type rcIfPortMAUFlowControlRecvEnable based on EnableVar"""
    defaultValue = 2


_RcIfPortMAUFlowControlRecvEnable_Type.__name__ = "EnableVar"
_RcIfPortMAUFlowControlRecvEnable_Object = MibTableColumn
rcIfPortMAUFlowControlRecvEnable = _RcIfPortMAUFlowControlRecvEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 2, 1, 8),
    _RcIfPortMAUFlowControlRecvEnable_Type()
)
rcIfPortMAUFlowControlRecvEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIfPortMAUFlowControlRecvEnable.setStatus("current")


class _RcIfPortMAUFlowControlSendEnable_Type(EnableVar):
    """Custom type rcIfPortMAUFlowControlSendEnable based on EnableVar"""
    defaultValue = 2


_RcIfPortMAUFlowControlSendEnable_Type.__name__ = "EnableVar"
_RcIfPortMAUFlowControlSendEnable_Object = MibTableColumn
rcIfPortMAUFlowControlSendEnable = _RcIfPortMAUFlowControlSendEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 2, 1, 9),
    _RcIfPortMAUFlowControlSendEnable_Type()
)
rcIfPortMAUFlowControlSendEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIfPortMAUFlowControlSendEnable.setStatus("current")


class _RcIfPortMAUMdiMode_Type(Integer32):
    """Custom type rcIfPortMAUMdiMode based on Integer32"""
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
        *(("auto-detect", 1),
          ("normal", 2),
          ("xover", 3))
    )


_RcIfPortMAUMdiMode_Type.__name__ = "Integer32"
_RcIfPortMAUMdiMode_Object = MibTableColumn
rcIfPortMAUMdiMode = _RcIfPortMAUMdiMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 2, 1, 10),
    _RcIfPortMAUMdiMode_Type()
)
rcIfPortMAUMdiMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIfPortMAUMdiMode.setStatus("current")


class _RcIfPortMAUStatus_Type(Integer32):
    """Custom type rcIfPortMAUStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("suspend", 2))
    )


_RcIfPortMAUStatus_Type.__name__ = "Integer32"
_RcIfPortMAUStatus_Object = MibTableColumn
rcIfPortMAUStatus = _RcIfPortMAUStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 2, 1, 11),
    _RcIfPortMAUStatus_Type()
)
rcIfPortMAUStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIfPortMAUStatus.setStatus("current")


class _RcIfPortMAUSfpPortType_Type(Integer32):
    """Custom type rcIfPortMAUSfpPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("autodetect", 0),
          ("copper", 1),
          ("fiber100", 2),
          ("fiber1000", 3),
          ("fiber10000", 4))
    )


_RcIfPortMAUSfpPortType_Type.__name__ = "Integer32"
_RcIfPortMAUSfpPortType_Object = MibTableColumn
rcIfPortMAUSfpPortType = _RcIfPortMAUSfpPortType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 2, 1, 12),
    _RcIfPortMAUSfpPortType_Type()
)
rcIfPortMAUSfpPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIfPortMAUSfpPortType.setStatus("mandatory")


class _RcIfPortEEEAutoMode_Type(Integer32):
    """Custom type rcIfPortEEEAutoMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-support", 0),
          ("enable", 1),
          ("disable", 2))
    )


_RcIfPortEEEAutoMode_Type.__name__ = "Integer32"
_RcIfPortEEEAutoMode_Object = MibTableColumn
rcIfPortEEEAutoMode = _RcIfPortEEEAutoMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 2, 1, 13),
    _RcIfPortEEEAutoMode_Type()
)
rcIfPortEEEAutoMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIfPortEEEAutoMode.setStatus("mandatory")
_RcComboMediaTable_Object = MibTable
rcComboMediaTable = _RcComboMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 3)
)
if mibBuilder.loadTexts:
    rcComboMediaTable.setStatus("current")
_RcComboMediaEntry_Object = MibTableRow
rcComboMediaEntry = _RcComboMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 3, 1)
)
rcComboMediaEntry.setIndexNames(
    (0, "SWITCH-INTERFACE-PORT-MIB", "rcComboPortId"),
    (0, "SWITCH-INTERFACE-PORT-MIB", "rcComboPortMedia"),
)
if mibBuilder.loadTexts:
    rcComboMediaEntry.setStatus("current")
_RcComboPortId_Type = Integer32
_RcComboPortId_Object = MibTableColumn
rcComboPortId = _RcComboPortId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 3, 1, 1),
    _RcComboPortId_Type()
)
rcComboPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcComboPortId.setStatus("current")


class _RcComboPortMedia_Type(Integer32):
    """Custom type rcComboPortMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-support", 0),
          ("fiber", 1),
          ("copper", 2))
    )


_RcComboPortMedia_Type.__name__ = "Integer32"
_RcComboPortMedia_Object = MibTableColumn
rcComboPortMedia = _RcComboPortMedia_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 3, 1, 2),
    _RcComboPortMedia_Type()
)
rcComboPortMedia.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcComboPortMedia.setStatus("current")


class _RcComboPortDescription_Type(OctetString):
    """Custom type rcComboPortDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RcComboPortDescription_Type.__name__ = "OctetString"
_RcComboPortDescription_Object = MibTableColumn
rcComboPortDescription = _RcComboPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 3, 1, 3),
    _RcComboPortDescription_Type()
)
rcComboPortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcComboPortDescription.setStatus("current")


class _RcComboPortSpeed_Type(Integer32):
    """Custom type rcComboPortSpeed based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("not-support", 0),
          ("Auto-negotiate", 1),
          ("speed-10M", 2),
          ("speed-100M", 3),
          ("speed-1000M", 4))
    )


_RcComboPortSpeed_Type.__name__ = "Integer32"
_RcComboPortSpeed_Object = MibTableColumn
rcComboPortSpeed = _RcComboPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 3, 1, 4),
    _RcComboPortSpeed_Type()
)
rcComboPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcComboPortSpeed.setStatus("current")


class _RcComboPortDuplex_Type(Integer32):
    """Custom type rcComboPortDuplex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-support", 0),
          ("auto-negotiate", 1),
          ("half", 2),
          ("full", 3))
    )


_RcComboPortDuplex_Type.__name__ = "Integer32"
_RcComboPortDuplex_Object = MibTableColumn
rcComboPortDuplex = _RcComboPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 3, 1, 5),
    _RcComboPortDuplex_Type()
)
rcComboPortDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcComboPortDuplex.setStatus("current")


class _RcComboPortFlowCtrl_Type(Integer32):
    """Custom type rcComboPortFlowCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-support", 0),
          ("enable", 1),
          ("disable", 2))
    )


_RcComboPortFlowCtrl_Type.__name__ = "Integer32"
_RcComboPortFlowCtrl_Object = MibTableColumn
rcComboPortFlowCtrl = _RcComboPortFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 3, 1, 6),
    _RcComboPortFlowCtrl_Type()
)
rcComboPortFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcComboPortFlowCtrl.setStatus("current")


class _RcComboPortSendFlowCtrl_Type(Integer32):
    """Custom type rcComboPortSendFlowCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-support", 0),
          ("enable", 1),
          ("disable", 2))
    )


_RcComboPortSendFlowCtrl_Type.__name__ = "Integer32"
_RcComboPortSendFlowCtrl_Object = MibTableColumn
rcComboPortSendFlowCtrl = _RcComboPortSendFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 3, 1, 7),
    _RcComboPortSendFlowCtrl_Type()
)
rcComboPortSendFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcComboPortSendFlowCtrl.setStatus("current")


class _RcComboPortRecvFlowCtrl_Type(Integer32):
    """Custom type rcComboPortRecvFlowCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-support", 0),
          ("enable", 1),
          ("disable", 2))
    )


_RcComboPortRecvFlowCtrl_Type.__name__ = "Integer32"
_RcComboPortRecvFlowCtrl_Object = MibTableColumn
rcComboPortRecvFlowCtrl = _RcComboPortRecvFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 3, 1, 8),
    _RcComboPortRecvFlowCtrl_Type()
)
rcComboPortRecvFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcComboPortRecvFlowCtrl.setStatus("current")


class _RcComboPortMdiXMode_Type(Integer32):
    """Custom type rcComboPortMdiXMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-support", 0),
          ("auto", 1),
          ("normal", 2),
          ("xover", 3))
    )


_RcComboPortMdiXMode_Type.__name__ = "Integer32"
_RcComboPortMdiXMode_Object = MibTableColumn
rcComboPortMdiXMode = _RcComboPortMdiXMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 2, 3, 1, 9),
    _RcComboPortMdiXMode_Type()
)
rcComboPortMdiXMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcComboPortMdiXMode.setStatus("current")

# Managed Objects groups


# Notification objects

rcIfPortConnectorInsertTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 1, 1)
)
rcIfPortConnectorInsertTrap.setObjects(
      *(("SWITCH-INTERFACE-PORT-MIB", "rcIfPortPHYIndex"),
        ("SWITCH-INTERFACE-PORT-MIB", "rcIfPortMAUIndex"))
)
if mibBuilder.loadTexts:
    rcIfPortConnectorInsertTrap.setStatus(
        "current"
    )

rcIfPortConnectorRemoveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 7, 1, 1, 2)
)
rcIfPortConnectorRemoveTrap.setObjects(
      *(("SWITCH-INTERFACE-PORT-MIB", "rcIfPortPHYIndex"),
        ("SWITCH-INTERFACE-PORT-MIB", "rcIfPortMAUIndex"))
)
if mibBuilder.loadTexts:
    rcIfPortConnectorRemoveTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-INTERFACE-PORT-MIB",
    **{"rcIfPortInfoConfig": rcIfPortInfoConfig,
       "rcIfPortPHYInfoConfig": rcIfPortPHYInfoConfig,
       "rcIfPortPHYNotifications": rcIfPortPHYNotifications,
       "rcIfPortConnectorInsertTrap": rcIfPortConnectorInsertTrap,
       "rcIfPortConnectorRemoveTrap": rcIfPortConnectorRemoveTrap,
       "rcIfPortPHYInfomation": rcIfPortPHYInfomation,
       "rcIfPortPHYTable": rcIfPortPHYTable,
       "rcIfPortPHYEntry": rcIfPortPHYEntry,
       "rcIfPortPHYIndex": rcIfPortPHYIndex,
       "rcIfPortPHYExistence": rcIfPortPHYExistence,
       "rcIfPortPHYMAUNum": rcIfPortPHYMAUNum,
       "rcIfPortPHYAdminStatus": rcIfPortPHYAdminStatus,
       "rcIfPortPHYOperStatus": rcIfPortPHYOperStatus,
       "rcIfPortPHYSpeedGet": rcIfPortPHYSpeedGet,
       "rcIfPortPHYDuplexGet": rcIfPortPHYDuplexGet,
       "rcIfPortPHYFlowControlRecvStatus": rcIfPortPHYFlowControlRecvStatus,
       "rcIfPortPHYFlowControlSendStatus": rcIfPortPHYFlowControlSendStatus,
       "rcIfPortPHYMdiStatus": rcIfPortPHYMdiStatus,
       "rcIfPortPHYActiveMAUIndex": rcIfPortPHYActiveMAUIndex,
       "rcComboPortMediaMode": rcComboPortMediaMode,
       "rcComboPortMediaPriority": rcComboPortMediaPriority,
       "rcComboPortMediaActive": rcComboPortMediaActive,
       "rcIfPortSfpAutoDetect": rcIfPortSfpAutoDetect,
       "rcIfPortSfpPortTypeGet": rcIfPortSfpPortTypeGet,
       "rcIfPortPHYEEEAutoGet": rcIfPortPHYEEEAutoGet,
       "rcIfPortMAUTable": rcIfPortMAUTable,
       "rcIfPortMAUEntry": rcIfPortMAUEntry,
       "rcIfPortMAUIndex": rcIfPortMAUIndex,
       "rcIfPortMAUType": rcIfPortMAUType,
       "rcIfPortMAUConnectorType": rcIfPortMAUConnectorType,
       "rcIfPortMAUConnectorStatus": rcIfPortMAUConnectorStatus,
       "rcIfPortMAUSpeedSet": rcIfPortMAUSpeedSet,
       "rcIfPortMAUDuplexSet": rcIfPortMAUDuplexSet,
       "rcIfPortMAUFlowControlEnable": rcIfPortMAUFlowControlEnable,
       "rcIfPortMAUFlowControlRecvEnable": rcIfPortMAUFlowControlRecvEnable,
       "rcIfPortMAUFlowControlSendEnable": rcIfPortMAUFlowControlSendEnable,
       "rcIfPortMAUMdiMode": rcIfPortMAUMdiMode,
       "rcIfPortMAUStatus": rcIfPortMAUStatus,
       "rcIfPortMAUSfpPortType": rcIfPortMAUSfpPortType,
       "rcIfPortEEEAutoMode": rcIfPortEEEAutoMode,
       "rcComboMediaTable": rcComboMediaTable,
       "rcComboMediaEntry": rcComboMediaEntry,
       "rcComboPortId": rcComboPortId,
       "rcComboPortMedia": rcComboPortMedia,
       "rcComboPortDescription": rcComboPortDescription,
       "rcComboPortSpeed": rcComboPortSpeed,
       "rcComboPortDuplex": rcComboPortDuplex,
       "rcComboPortFlowCtrl": rcComboPortFlowCtrl,
       "rcComboPortSendFlowCtrl": rcComboPortSendFlowCtrl,
       "rcComboPortRecvFlowCtrl": rcComboPortRecvFlowCtrl,
       "rcComboPortMdiXMode": rcComboPortMdiXMode}
)
