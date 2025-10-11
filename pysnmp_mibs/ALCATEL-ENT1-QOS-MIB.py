# SNMP MIB module (ALCATEL-ENT1-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel-ent1/ALCATEL-ENT1-QOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:10:38 2025
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

(softentIND1QoS,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-BASE",
    "softentIND1QoS")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(Ipv6Address,
 Ipv6IfIndexOrZero) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6IfIndexOrZero")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alaQoSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1)
)
if mibBuilder.loadTexts:
    alaQoSMIB.setRevisions(
        ("2014-07-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlaQoSMIBObjects_ObjectIdentity = ObjectIdentity
alaQoSMIBObjects = _AlaQoSMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1)
)
if mibBuilder.loadTexts:
    alaQoSMIBObjects.setStatus("current")
_AlaQoSRuleTable_Object = MibTable
alaQoSRuleTable = _AlaQoSRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaQoSRuleTable.setStatus("current")
_AlaQoSRuleEntry_Object = MibTableRow
alaQoSRuleEntry = _AlaQoSRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1)
)
alaQoSRuleEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSRuleName"),
)
if mibBuilder.loadTexts:
    alaQoSRuleEntry.setStatus("current")


class _AlaQoSRuleName_Type(SnmpAdminString):
    """Custom type alaQoSRuleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSRuleName_Type.__name__ = "SnmpAdminString"
_AlaQoSRuleName_Object = MibTableColumn
alaQoSRuleName = _AlaQoSRuleName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 1),
    _AlaQoSRuleName_Type()
)
alaQoSRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSRuleName.setStatus("current")


class _AlaQoSRuleEnabled_Type(Integer32):
    """Custom type alaQoSRuleEnabled based on Integer32"""
    defaultValue = 1

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


_AlaQoSRuleEnabled_Type.__name__ = "Integer32"
_AlaQoSRuleEnabled_Object = MibTableColumn
alaQoSRuleEnabled = _AlaQoSRuleEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 2),
    _AlaQoSRuleEnabled_Type()
)
alaQoSRuleEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleEnabled.setStatus("current")


class _AlaQoSRuleSource_Type(Integer32):
    """Custom type alaQoSRuleSource based on Integer32"""
    defaultValue = 2

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
        *(("ldap", 1),
          ("cli", 2),
          ("blt", 3),
          ("api", 4),
          ("imp", 5))
    )


_AlaQoSRuleSource_Type.__name__ = "Integer32"
_AlaQoSRuleSource_Object = MibTableColumn
alaQoSRuleSource = _AlaQoSRuleSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 3),
    _AlaQoSRuleSource_Type()
)
alaQoSRuleSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleSource.setStatus("current")


class _AlaQoSRulePrecedence_Type(Integer32):
    """Custom type alaQoSRulePrecedence based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSRulePrecedence_Type.__name__ = "Integer32"
_AlaQoSRulePrecedence_Object = MibTableColumn
alaQoSRulePrecedence = _AlaQoSRulePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 4),
    _AlaQoSRulePrecedence_Type()
)
alaQoSRulePrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRulePrecedence.setStatus("current")


class _AlaQoSRuleCondition_Type(SnmpAdminString):
    """Custom type alaQoSRuleCondition based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSRuleCondition_Type.__name__ = "SnmpAdminString"
_AlaQoSRuleCondition_Object = MibTableColumn
alaQoSRuleCondition = _AlaQoSRuleCondition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 5),
    _AlaQoSRuleCondition_Type()
)
alaQoSRuleCondition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleCondition.setStatus("current")


class _AlaQoSRuleAction_Type(SnmpAdminString):
    """Custom type alaQoSRuleAction based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSRuleAction_Type.__name__ = "SnmpAdminString"
_AlaQoSRuleAction_Object = MibTableColumn
alaQoSRuleAction = _AlaQoSRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 6),
    _AlaQoSRuleAction_Type()
)
alaQoSRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleAction.setStatus("current")


class _AlaQoSRuleReflexive_Type(Integer32):
    """Custom type alaQoSRuleReflexive based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSRuleReflexive_Type.__name__ = "Integer32"
_AlaQoSRuleReflexive_Object = MibTableColumn
alaQoSRuleReflexive = _AlaQoSRuleReflexive_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 7),
    _AlaQoSRuleReflexive_Type()
)
alaQoSRuleReflexive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleReflexive.setStatus("current")


class _AlaQoSRuleSave_Type(Integer32):
    """Custom type alaQoSRuleSave based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSRuleSave_Type.__name__ = "Integer32"
_AlaQoSRuleSave_Object = MibTableColumn
alaQoSRuleSave = _AlaQoSRuleSave_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 8),
    _AlaQoSRuleSave_Type()
)
alaQoSRuleSave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleSave.setStatus("current")


class _AlaQoSRuleLog_Type(Integer32):
    """Custom type alaQoSRuleLog based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSRuleLog_Type.__name__ = "Integer32"
_AlaQoSRuleLog_Object = MibTableColumn
alaQoSRuleLog = _AlaQoSRuleLog_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 9),
    _AlaQoSRuleLog_Type()
)
alaQoSRuleLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleLog.setStatus("current")


class _AlaQoSRuleEnforced_Type(Integer32):
    """Custom type alaQoSRuleEnforced based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSRuleEnforced_Type.__name__ = "Integer32"
_AlaQoSRuleEnforced_Object = MibTableColumn
alaQoSRuleEnforced = _AlaQoSRuleEnforced_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 10),
    _AlaQoSRuleEnforced_Type()
)
alaQoSRuleEnforced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRuleEnforced.setStatus("current")


class _AlaQoSRuleActive_Type(Integer32):
    """Custom type alaQoSRuleActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSRuleActive_Type.__name__ = "Integer32"
_AlaQoSRuleActive_Object = MibTableColumn
alaQoSRuleActive = _AlaQoSRuleActive_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 11),
    _AlaQoSRuleActive_Type()
)
alaQoSRuleActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRuleActive.setStatus("current")
_AlaQoSRuleRowStatus_Type = RowStatus
_AlaQoSRuleRowStatus_Object = MibTableColumn
alaQoSRuleRowStatus = _AlaQoSRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 12),
    _AlaQoSRuleRowStatus_Type()
)
alaQoSRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleRowStatus.setStatus("current")


class _AlaQoSRuleValidityPeriod_Type(SnmpAdminString):
    """Custom type alaQoSRuleValidityPeriod based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSRuleValidityPeriod_Type.__name__ = "SnmpAdminString"
_AlaQoSRuleValidityPeriod_Object = MibTableColumn
alaQoSRuleValidityPeriod = _AlaQoSRuleValidityPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 13),
    _AlaQoSRuleValidityPeriod_Type()
)
alaQoSRuleValidityPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleValidityPeriod.setStatus("current")


class _AlaQoSRuleValidityPeriodStatus_Type(Integer32):
    """Custom type alaQoSRuleValidityPeriodStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSRuleValidityPeriodStatus_Type.__name__ = "Integer32"
_AlaQoSRuleValidityPeriodStatus_Object = MibTableColumn
alaQoSRuleValidityPeriodStatus = _AlaQoSRuleValidityPeriodStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 14),
    _AlaQoSRuleValidityPeriodStatus_Type()
)
alaQoSRuleValidityPeriodStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleValidityPeriodStatus.setStatus("current")


class _AlaQoSRuleLogInterval_Type(Integer32):
    """Custom type alaQoSRuleLogInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AlaQoSRuleLogInterval_Type.__name__ = "Integer32"
_AlaQoSRuleLogInterval_Object = MibTableColumn
alaQoSRuleLogInterval = _AlaQoSRuleLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 15),
    _AlaQoSRuleLogInterval_Type()
)
alaQoSRuleLogInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleLogInterval.setStatus("current")


class _AlaQoSRuleCountType_Type(Integer32):
    """Custom type alaQoSRuleCountType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packets", 1),
          ("bytes", 2))
    )


_AlaQoSRuleCountType_Type.__name__ = "Integer32"
_AlaQoSRuleCountType_Object = MibTableColumn
alaQoSRuleCountType = _AlaQoSRuleCountType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 16),
    _AlaQoSRuleCountType_Type()
)
alaQoSRuleCountType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleCountType.setStatus("current")
_AlaQoSRulePacketCount_Type = Counter64
_AlaQoSRulePacketCount_Object = MibTableColumn
alaQoSRulePacketCount = _AlaQoSRulePacketCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 17),
    _AlaQoSRulePacketCount_Type()
)
alaQoSRulePacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRulePacketCount.setStatus("current")
_AlaQoSRuleByteCount_Type = Counter64
_AlaQoSRuleByteCount_Object = MibTableColumn
alaQoSRuleByteCount = _AlaQoSRuleByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 18),
    _AlaQoSRuleByteCount_Type()
)
alaQoSRuleByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRuleByteCount.setStatus("current")
_AlaQoSRuleType_Type = Integer32
_AlaQoSRuleType_Object = MibTableColumn
alaQoSRuleType = _AlaQoSRuleType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 19),
    _AlaQoSRuleType_Type()
)
alaQoSRuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRuleType.setStatus("current")


class _AlaQoSRuleTrapEvents_Type(Integer32):
    """Custom type alaQoSRuleTrapEvents based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSRuleTrapEvents_Type.__name__ = "Integer32"
_AlaQoSRuleTrapEvents_Object = MibTableColumn
alaQoSRuleTrapEvents = _AlaQoSRuleTrapEvents_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 20),
    _AlaQoSRuleTrapEvents_Type()
)
alaQoSRuleTrapEvents.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleTrapEvents.setStatus("current")


class _AlaQoSRuleDefaultList_Type(Integer32):
    """Custom type alaQoSRuleDefaultList based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSRuleDefaultList_Type.__name__ = "Integer32"
_AlaQoSRuleDefaultList_Object = MibTableColumn
alaQoSRuleDefaultList = _AlaQoSRuleDefaultList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 21),
    _AlaQoSRuleDefaultList_Type()
)
alaQoSRuleDefaultList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleDefaultList.setStatus("current")
_AlaQoSRuleGreenPacketCount_Type = Counter64
_AlaQoSRuleGreenPacketCount_Object = MibTableColumn
alaQoSRuleGreenPacketCount = _AlaQoSRuleGreenPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 22),
    _AlaQoSRuleGreenPacketCount_Type()
)
alaQoSRuleGreenPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRuleGreenPacketCount.setStatus("current")
_AlaQoSRuleYellowPacketCount_Type = Counter64
_AlaQoSRuleYellowPacketCount_Object = MibTableColumn
alaQoSRuleYellowPacketCount = _AlaQoSRuleYellowPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 23),
    _AlaQoSRuleYellowPacketCount_Type()
)
alaQoSRuleYellowPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRuleYellowPacketCount.setStatus("current")
_AlaQoSRuleRedPacketCount_Type = Counter64
_AlaQoSRuleRedPacketCount_Object = MibTableColumn
alaQoSRuleRedPacketCount = _AlaQoSRuleRedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 24),
    _AlaQoSRuleRedPacketCount_Type()
)
alaQoSRuleRedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRuleRedPacketCount.setStatus("current")
_AlaQoSRuleGreenByteCount_Type = Counter64
_AlaQoSRuleGreenByteCount_Object = MibTableColumn
alaQoSRuleGreenByteCount = _AlaQoSRuleGreenByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 25),
    _AlaQoSRuleGreenByteCount_Type()
)
alaQoSRuleGreenByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRuleGreenByteCount.setStatus("current")
_AlaQoSRuleYellowByteCount_Type = Counter64
_AlaQoSRuleYellowByteCount_Object = MibTableColumn
alaQoSRuleYellowByteCount = _AlaQoSRuleYellowByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 26),
    _AlaQoSRuleYellowByteCount_Type()
)
alaQoSRuleYellowByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRuleYellowByteCount.setStatus("current")
_AlaQoSRuleRedByteCount_Type = Counter64
_AlaQoSRuleRedByteCount_Object = MibTableColumn
alaQoSRuleRedByteCount = _AlaQoSRuleRedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 27),
    _AlaQoSRuleRedByteCount_Type()
)
alaQoSRuleRedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRuleRedByteCount.setStatus("current")
_AlaQoSAppliedRuleTable_Object = MibTable
alaQoSAppliedRuleTable = _AlaQoSAppliedRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaQoSAppliedRuleTable.setStatus("current")
_AlaQoSAppliedRuleEntry_Object = MibTableRow
alaQoSAppliedRuleEntry = _AlaQoSAppliedRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1)
)
alaQoSAppliedRuleEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleName"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedRuleEntry.setStatus("current")


class _AlaQoSAppliedRuleName_Type(SnmpAdminString):
    """Custom type alaQoSAppliedRuleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedRuleName_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedRuleName_Object = MibTableColumn
alaQoSAppliedRuleName = _AlaQoSAppliedRuleName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 1),
    _AlaQoSAppliedRuleName_Type()
)
alaQoSAppliedRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleName.setStatus("current")


class _AlaQoSAppliedRuleEnabled_Type(Integer32):
    """Custom type alaQoSAppliedRuleEnabled based on Integer32"""
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


_AlaQoSAppliedRuleEnabled_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleEnabled_Object = MibTableColumn
alaQoSAppliedRuleEnabled = _AlaQoSAppliedRuleEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 2),
    _AlaQoSAppliedRuleEnabled_Type()
)
alaQoSAppliedRuleEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleEnabled.setStatus("current")


class _AlaQoSAppliedRuleSource_Type(Integer32):
    """Custom type alaQoSAppliedRuleSource based on Integer32"""
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
        *(("ldap", 1),
          ("cli", 2),
          ("blt", 3),
          ("api", 4),
          ("imp", 5))
    )


_AlaQoSAppliedRuleSource_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleSource_Object = MibTableColumn
alaQoSAppliedRuleSource = _AlaQoSAppliedRuleSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 3),
    _AlaQoSAppliedRuleSource_Type()
)
alaQoSAppliedRuleSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleSource.setStatus("current")


class _AlaQoSAppliedRulePrecedence_Type(Integer32):
    """Custom type alaQoSAppliedRulePrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedRulePrecedence_Type.__name__ = "Integer32"
_AlaQoSAppliedRulePrecedence_Object = MibTableColumn
alaQoSAppliedRulePrecedence = _AlaQoSAppliedRulePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 4),
    _AlaQoSAppliedRulePrecedence_Type()
)
alaQoSAppliedRulePrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRulePrecedence.setStatus("current")


class _AlaQoSAppliedRuleCondition_Type(SnmpAdminString):
    """Custom type alaQoSAppliedRuleCondition based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedRuleCondition_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedRuleCondition_Object = MibTableColumn
alaQoSAppliedRuleCondition = _AlaQoSAppliedRuleCondition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 5),
    _AlaQoSAppliedRuleCondition_Type()
)
alaQoSAppliedRuleCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleCondition.setStatus("current")


class _AlaQoSAppliedRuleAction_Type(SnmpAdminString):
    """Custom type alaQoSAppliedRuleAction based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedRuleAction_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedRuleAction_Object = MibTableColumn
alaQoSAppliedRuleAction = _AlaQoSAppliedRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 6),
    _AlaQoSAppliedRuleAction_Type()
)
alaQoSAppliedRuleAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleAction.setStatus("current")


class _AlaQoSAppliedRuleReflexive_Type(Integer32):
    """Custom type alaQoSAppliedRuleReflexive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSAppliedRuleReflexive_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleReflexive_Object = MibTableColumn
alaQoSAppliedRuleReflexive = _AlaQoSAppliedRuleReflexive_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 7),
    _AlaQoSAppliedRuleReflexive_Type()
)
alaQoSAppliedRuleReflexive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleReflexive.setStatus("current")


class _AlaQoSAppliedRuleSave_Type(Integer32):
    """Custom type alaQoSAppliedRuleSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSAppliedRuleSave_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleSave_Object = MibTableColumn
alaQoSAppliedRuleSave = _AlaQoSAppliedRuleSave_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 8),
    _AlaQoSAppliedRuleSave_Type()
)
alaQoSAppliedRuleSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleSave.setStatus("current")


class _AlaQoSAppliedRuleLog_Type(Integer32):
    """Custom type alaQoSAppliedRuleLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSAppliedRuleLog_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleLog_Object = MibTableColumn
alaQoSAppliedRuleLog = _AlaQoSAppliedRuleLog_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 9),
    _AlaQoSAppliedRuleLog_Type()
)
alaQoSAppliedRuleLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleLog.setStatus("current")


class _AlaQoSAppliedRuleEnforced_Type(Integer32):
    """Custom type alaQoSAppliedRuleEnforced based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSAppliedRuleEnforced_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleEnforced_Object = MibTableColumn
alaQoSAppliedRuleEnforced = _AlaQoSAppliedRuleEnforced_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 10),
    _AlaQoSAppliedRuleEnforced_Type()
)
alaQoSAppliedRuleEnforced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleEnforced.setStatus("current")


class _AlaQoSAppliedRuleActive_Type(Integer32):
    """Custom type alaQoSAppliedRuleActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSAppliedRuleActive_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleActive_Object = MibTableColumn
alaQoSAppliedRuleActive = _AlaQoSAppliedRuleActive_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 11),
    _AlaQoSAppliedRuleActive_Type()
)
alaQoSAppliedRuleActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleActive.setStatus("current")
_AlaQoSAppliedRuleRowStatus_Type = RowStatus
_AlaQoSAppliedRuleRowStatus_Object = MibTableColumn
alaQoSAppliedRuleRowStatus = _AlaQoSAppliedRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 12),
    _AlaQoSAppliedRuleRowStatus_Type()
)
alaQoSAppliedRuleRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleRowStatus.setStatus("current")


class _AlaQoSAppliedRuleValidityPeriod_Type(SnmpAdminString):
    """Custom type alaQoSAppliedRuleValidityPeriod based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedRuleValidityPeriod_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedRuleValidityPeriod_Object = MibTableColumn
alaQoSAppliedRuleValidityPeriod = _AlaQoSAppliedRuleValidityPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 13),
    _AlaQoSAppliedRuleValidityPeriod_Type()
)
alaQoSAppliedRuleValidityPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleValidityPeriod.setStatus("current")


class _AlaQoSAppliedRuleValidityPeriodStatus_Type(Integer32):
    """Custom type alaQoSAppliedRuleValidityPeriodStatus based on Integer32"""
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


_AlaQoSAppliedRuleValidityPeriodStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleValidityPeriodStatus_Object = MibTableColumn
alaQoSAppliedRuleValidityPeriodStatus = _AlaQoSAppliedRuleValidityPeriodStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 14),
    _AlaQoSAppliedRuleValidityPeriodStatus_Type()
)
alaQoSAppliedRuleValidityPeriodStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleValidityPeriodStatus.setStatus("current")


class _AlaQoSAppliedRuleLogInterval_Type(Integer32):
    """Custom type alaQoSAppliedRuleLogInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AlaQoSAppliedRuleLogInterval_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleLogInterval_Object = MibTableColumn
alaQoSAppliedRuleLogInterval = _AlaQoSAppliedRuleLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 15),
    _AlaQoSAppliedRuleLogInterval_Type()
)
alaQoSAppliedRuleLogInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleLogInterval.setStatus("current")


class _AlaQoSAppliedRuleCountType_Type(Integer32):
    """Custom type alaQoSAppliedRuleCountType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packets", 1),
          ("bytes", 2))
    )


_AlaQoSAppliedRuleCountType_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleCountType_Object = MibTableColumn
alaQoSAppliedRuleCountType = _AlaQoSAppliedRuleCountType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 16),
    _AlaQoSAppliedRuleCountType_Type()
)
alaQoSAppliedRuleCountType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleCountType.setStatus("current")
_AlaQoSAppliedRulePacketCount_Type = Counter64
_AlaQoSAppliedRulePacketCount_Object = MibTableColumn
alaQoSAppliedRulePacketCount = _AlaQoSAppliedRulePacketCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 17),
    _AlaQoSAppliedRulePacketCount_Type()
)
alaQoSAppliedRulePacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRulePacketCount.setStatus("current")
_AlaQoSAppliedRuleByteCount_Type = Counter64
_AlaQoSAppliedRuleByteCount_Object = MibTableColumn
alaQoSAppliedRuleByteCount = _AlaQoSAppliedRuleByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 18),
    _AlaQoSAppliedRuleByteCount_Type()
)
alaQoSAppliedRuleByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleByteCount.setStatus("current")
_AlaQoSAppliedRuleType_Type = Integer32
_AlaQoSAppliedRuleType_Object = MibTableColumn
alaQoSAppliedRuleType = _AlaQoSAppliedRuleType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 19),
    _AlaQoSAppliedRuleType_Type()
)
alaQoSAppliedRuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleType.setStatus("current")


class _AlaQoSAppliedRuleTrapEvents_Type(Integer32):
    """Custom type alaQoSAppliedRuleTrapEvents based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSAppliedRuleTrapEvents_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleTrapEvents_Object = MibTableColumn
alaQoSAppliedRuleTrapEvents = _AlaQoSAppliedRuleTrapEvents_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 20),
    _AlaQoSAppliedRuleTrapEvents_Type()
)
alaQoSAppliedRuleTrapEvents.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleTrapEvents.setStatus("current")


class _AlaQoSAppliedRuleDefaultList_Type(Integer32):
    """Custom type alaQoSAppliedRuleDefaultList based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSAppliedRuleDefaultList_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleDefaultList_Object = MibTableColumn
alaQoSAppliedRuleDefaultList = _AlaQoSAppliedRuleDefaultList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 21),
    _AlaQoSAppliedRuleDefaultList_Type()
)
alaQoSAppliedRuleDefaultList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleDefaultList.setStatus("current")
_AlaQoSAppliedRuleGreenPacketCount_Type = Counter64
_AlaQoSAppliedRuleGreenPacketCount_Object = MibTableColumn
alaQoSAppliedRuleGreenPacketCount = _AlaQoSAppliedRuleGreenPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 22),
    _AlaQoSAppliedRuleGreenPacketCount_Type()
)
alaQoSAppliedRuleGreenPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGreenPacketCount.setStatus("current")
_AlaQoSAppliedRuleYellowPacketCount_Type = Counter64
_AlaQoSAppliedRuleYellowPacketCount_Object = MibTableColumn
alaQoSAppliedRuleYellowPacketCount = _AlaQoSAppliedRuleYellowPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 23),
    _AlaQoSAppliedRuleYellowPacketCount_Type()
)
alaQoSAppliedRuleYellowPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleYellowPacketCount.setStatus("current")
_AlaQoSAppliedRuleRedPacketCount_Type = Counter64
_AlaQoSAppliedRuleRedPacketCount_Object = MibTableColumn
alaQoSAppliedRuleRedPacketCount = _AlaQoSAppliedRuleRedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 24),
    _AlaQoSAppliedRuleRedPacketCount_Type()
)
alaQoSAppliedRuleRedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleRedPacketCount.setStatus("current")
_AlaQoSAppliedRuleGreenByteCount_Type = Counter64
_AlaQoSAppliedRuleGreenByteCount_Object = MibTableColumn
alaQoSAppliedRuleGreenByteCount = _AlaQoSAppliedRuleGreenByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 25),
    _AlaQoSAppliedRuleGreenByteCount_Type()
)
alaQoSAppliedRuleGreenByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGreenByteCount.setStatus("current")
_AlaQoSAppliedRuleYellowByteCount_Type = Counter64
_AlaQoSAppliedRuleYellowByteCount_Object = MibTableColumn
alaQoSAppliedRuleYellowByteCount = _AlaQoSAppliedRuleYellowByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 26),
    _AlaQoSAppliedRuleYellowByteCount_Type()
)
alaQoSAppliedRuleYellowByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleYellowByteCount.setStatus("current")
_AlaQoSAppliedRuleRedByteCount_Type = Counter64
_AlaQoSAppliedRuleRedByteCount_Object = MibTableColumn
alaQoSAppliedRuleRedByteCount = _AlaQoSAppliedRuleRedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 27),
    _AlaQoSAppliedRuleRedByteCount_Type()
)
alaQoSAppliedRuleRedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleRedByteCount.setStatus("current")
_AlaQoSConditionTable_Object = MibTable
alaQoSConditionTable = _AlaQoSConditionTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaQoSConditionTable.setStatus("current")
_AlaQoSConditionEntry_Object = MibTableRow
alaQoSConditionEntry = _AlaQoSConditionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1)
)
alaQoSConditionEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSConditionName"),
)
if mibBuilder.loadTexts:
    alaQoSConditionEntry.setStatus("current")


class _AlaQoSConditionName_Type(SnmpAdminString):
    """Custom type alaQoSConditionName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSConditionName_Type.__name__ = "SnmpAdminString"
_AlaQoSConditionName_Object = MibTableColumn
alaQoSConditionName = _AlaQoSConditionName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 1),
    _AlaQoSConditionName_Type()
)
alaQoSConditionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSConditionName.setStatus("current")


class _AlaQoSConditionSource_Type(Integer32):
    """Custom type alaQoSConditionSource based on Integer32"""
    defaultValue = 2

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
        *(("ldap", 1),
          ("cli", 2),
          ("blt", 3),
          ("api", 4),
          ("imp", 5))
    )


_AlaQoSConditionSource_Type.__name__ = "Integer32"
_AlaQoSConditionSource_Object = MibTableColumn
alaQoSConditionSource = _AlaQoSConditionSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 2),
    _AlaQoSConditionSource_Type()
)
alaQoSConditionSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSource.setStatus("current")


class _AlaQoSConditionSourceSlot_Type(Integer32):
    """Custom type alaQoSConditionSourceSlot based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSConditionSourceSlot_Type.__name__ = "Integer32"
_AlaQoSConditionSourceSlot_Object = MibTableColumn
alaQoSConditionSourceSlot = _AlaQoSConditionSourceSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 3),
    _AlaQoSConditionSourceSlot_Type()
)
alaQoSConditionSourceSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceSlot.setStatus("current")


class _AlaQoSConditionSourceSlotStatus_Type(Integer32):
    """Custom type alaQoSConditionSourceSlotStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionSourceSlotStatus_Type.__name__ = "Integer32"
_AlaQoSConditionSourceSlotStatus_Object = MibTableColumn
alaQoSConditionSourceSlotStatus = _AlaQoSConditionSourceSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 4),
    _AlaQoSConditionSourceSlotStatus_Type()
)
alaQoSConditionSourceSlotStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceSlotStatus.setStatus("current")


class _AlaQoSConditionSourcePort_Type(Integer32):
    """Custom type alaQoSConditionSourcePort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSConditionSourcePort_Type.__name__ = "Integer32"
_AlaQoSConditionSourcePort_Object = MibTableColumn
alaQoSConditionSourcePort = _AlaQoSConditionSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 5),
    _AlaQoSConditionSourcePort_Type()
)
alaQoSConditionSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourcePort.setStatus("current")


class _AlaQoSConditionSourcePortGroup_Type(SnmpAdminString):
    """Custom type alaQoSConditionSourcePortGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSConditionSourcePortGroup_Type.__name__ = "SnmpAdminString"
_AlaQoSConditionSourcePortGroup_Object = MibTableColumn
alaQoSConditionSourcePortGroup = _AlaQoSConditionSourcePortGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 6),
    _AlaQoSConditionSourcePortGroup_Type()
)
alaQoSConditionSourcePortGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourcePortGroup.setStatus("current")


class _AlaQoSConditionSourcePortGroupStatus_Type(Integer32):
    """Custom type alaQoSConditionSourcePortGroupStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionSourcePortGroupStatus_Type.__name__ = "Integer32"
_AlaQoSConditionSourcePortGroupStatus_Object = MibTableColumn
alaQoSConditionSourcePortGroupStatus = _AlaQoSConditionSourcePortGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 7),
    _AlaQoSConditionSourcePortGroupStatus_Type()
)
alaQoSConditionSourcePortGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourcePortGroupStatus.setStatus("current")


class _AlaQoSConditionDestinationSlot_Type(Integer32):
    """Custom type alaQoSConditionDestinationSlot based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSConditionDestinationSlot_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationSlot_Object = MibTableColumn
alaQoSConditionDestinationSlot = _AlaQoSConditionDestinationSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 8),
    _AlaQoSConditionDestinationSlot_Type()
)
alaQoSConditionDestinationSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationSlot.setStatus("current")


class _AlaQoSConditionDestinationSlotStatus_Type(Integer32):
    """Custom type alaQoSConditionDestinationSlotStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionDestinationSlotStatus_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationSlotStatus_Object = MibTableColumn
alaQoSConditionDestinationSlotStatus = _AlaQoSConditionDestinationSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 9),
    _AlaQoSConditionDestinationSlotStatus_Type()
)
alaQoSConditionDestinationSlotStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationSlotStatus.setStatus("current")


class _AlaQoSConditionDestinationPort_Type(Integer32):
    """Custom type alaQoSConditionDestinationPort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSConditionDestinationPort_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationPort_Object = MibTableColumn
alaQoSConditionDestinationPort = _AlaQoSConditionDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 10),
    _AlaQoSConditionDestinationPort_Type()
)
alaQoSConditionDestinationPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationPort.setStatus("current")


class _AlaQoSConditionDestinationPortGroup_Type(SnmpAdminString):
    """Custom type alaQoSConditionDestinationPortGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSConditionDestinationPortGroup_Type.__name__ = "SnmpAdminString"
_AlaQoSConditionDestinationPortGroup_Object = MibTableColumn
alaQoSConditionDestinationPortGroup = _AlaQoSConditionDestinationPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 11),
    _AlaQoSConditionDestinationPortGroup_Type()
)
alaQoSConditionDestinationPortGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationPortGroup.setStatus("current")


class _AlaQoSConditionDestinationPortGroupStatus_Type(Integer32):
    """Custom type alaQoSConditionDestinationPortGroupStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionDestinationPortGroupStatus_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationPortGroupStatus_Object = MibTableColumn
alaQoSConditionDestinationPortGroupStatus = _AlaQoSConditionDestinationPortGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 12),
    _AlaQoSConditionDestinationPortGroupStatus_Type()
)
alaQoSConditionDestinationPortGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationPortGroupStatus.setStatus("current")


class _AlaQoSConditionSourceMacAddr_Type(MacAddress):
    """Custom type alaQoSConditionSourceMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_AlaQoSConditionSourceMacAddr_Type.__name__ = "MacAddress"
_AlaQoSConditionSourceMacAddr_Object = MibTableColumn
alaQoSConditionSourceMacAddr = _AlaQoSConditionSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 13),
    _AlaQoSConditionSourceMacAddr_Type()
)
alaQoSConditionSourceMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceMacAddr.setStatus("current")


class _AlaQoSConditionSourceMacAddrStatus_Type(Integer32):
    """Custom type alaQoSConditionSourceMacAddrStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionSourceMacAddrStatus_Type.__name__ = "Integer32"
_AlaQoSConditionSourceMacAddrStatus_Object = MibTableColumn
alaQoSConditionSourceMacAddrStatus = _AlaQoSConditionSourceMacAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 14),
    _AlaQoSConditionSourceMacAddrStatus_Type()
)
alaQoSConditionSourceMacAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceMacAddrStatus.setStatus("current")


class _AlaQoSConditionSourceMacMask_Type(MacAddress):
    """Custom type alaQoSConditionSourceMacMask based on MacAddress"""
    defaultHexValue = "ffffffffffff"


_AlaQoSConditionSourceMacMask_Type.__name__ = "MacAddress"
_AlaQoSConditionSourceMacMask_Object = MibTableColumn
alaQoSConditionSourceMacMask = _AlaQoSConditionSourceMacMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 15),
    _AlaQoSConditionSourceMacMask_Type()
)
alaQoSConditionSourceMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceMacMask.setStatus("current")


class _AlaQoSConditionSourceMacGroup_Type(SnmpAdminString):
    """Custom type alaQoSConditionSourceMacGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSConditionSourceMacGroup_Type.__name__ = "SnmpAdminString"
_AlaQoSConditionSourceMacGroup_Object = MibTableColumn
alaQoSConditionSourceMacGroup = _AlaQoSConditionSourceMacGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 16),
    _AlaQoSConditionSourceMacGroup_Type()
)
alaQoSConditionSourceMacGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceMacGroup.setStatus("current")


class _AlaQoSConditionSourceMacGroupStatus_Type(Integer32):
    """Custom type alaQoSConditionSourceMacGroupStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionSourceMacGroupStatus_Type.__name__ = "Integer32"
_AlaQoSConditionSourceMacGroupStatus_Object = MibTableColumn
alaQoSConditionSourceMacGroupStatus = _AlaQoSConditionSourceMacGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 17),
    _AlaQoSConditionSourceMacGroupStatus_Type()
)
alaQoSConditionSourceMacGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceMacGroupStatus.setStatus("current")


class _AlaQoSConditionDestinationMacAddr_Type(MacAddress):
    """Custom type alaQoSConditionDestinationMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_AlaQoSConditionDestinationMacAddr_Type.__name__ = "MacAddress"
_AlaQoSConditionDestinationMacAddr_Object = MibTableColumn
alaQoSConditionDestinationMacAddr = _AlaQoSConditionDestinationMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 18),
    _AlaQoSConditionDestinationMacAddr_Type()
)
alaQoSConditionDestinationMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationMacAddr.setStatus("current")


class _AlaQoSConditionDestinationMacAddrStatus_Type(Integer32):
    """Custom type alaQoSConditionDestinationMacAddrStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionDestinationMacAddrStatus_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationMacAddrStatus_Object = MibTableColumn
alaQoSConditionDestinationMacAddrStatus = _AlaQoSConditionDestinationMacAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 19),
    _AlaQoSConditionDestinationMacAddrStatus_Type()
)
alaQoSConditionDestinationMacAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationMacAddrStatus.setStatus("current")


class _AlaQoSConditionDestinationMacMask_Type(MacAddress):
    """Custom type alaQoSConditionDestinationMacMask based on MacAddress"""
    defaultHexValue = "ffffffffffff"


_AlaQoSConditionDestinationMacMask_Type.__name__ = "MacAddress"
_AlaQoSConditionDestinationMacMask_Object = MibTableColumn
alaQoSConditionDestinationMacMask = _AlaQoSConditionDestinationMacMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 20),
    _AlaQoSConditionDestinationMacMask_Type()
)
alaQoSConditionDestinationMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationMacMask.setStatus("current")


class _AlaQoSConditionDestinationMacGroup_Type(SnmpAdminString):
    """Custom type alaQoSConditionDestinationMacGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSConditionDestinationMacGroup_Type.__name__ = "SnmpAdminString"
_AlaQoSConditionDestinationMacGroup_Object = MibTableColumn
alaQoSConditionDestinationMacGroup = _AlaQoSConditionDestinationMacGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 21),
    _AlaQoSConditionDestinationMacGroup_Type()
)
alaQoSConditionDestinationMacGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationMacGroup.setStatus("current")


class _AlaQoSConditionDestinationMacGroupStatus_Type(Integer32):
    """Custom type alaQoSConditionDestinationMacGroupStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionDestinationMacGroupStatus_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationMacGroupStatus_Object = MibTableColumn
alaQoSConditionDestinationMacGroupStatus = _AlaQoSConditionDestinationMacGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 22),
    _AlaQoSConditionDestinationMacGroupStatus_Type()
)
alaQoSConditionDestinationMacGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationMacGroupStatus.setStatus("current")


class _AlaQoSConditionSourceVlan_Type(Integer32):
    """Custom type alaQoSConditionSourceVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSConditionSourceVlan_Type.__name__ = "Integer32"
_AlaQoSConditionSourceVlan_Object = MibTableColumn
alaQoSConditionSourceVlan = _AlaQoSConditionSourceVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 23),
    _AlaQoSConditionSourceVlan_Type()
)
alaQoSConditionSourceVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceVlan.setStatus("current")


class _AlaQoSConditionSourceVlanStatus_Type(Integer32):
    """Custom type alaQoSConditionSourceVlanStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionSourceVlanStatus_Type.__name__ = "Integer32"
_AlaQoSConditionSourceVlanStatus_Object = MibTableColumn
alaQoSConditionSourceVlanStatus = _AlaQoSConditionSourceVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 24),
    _AlaQoSConditionSourceVlanStatus_Type()
)
alaQoSConditionSourceVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceVlanStatus.setStatus("current")


class _AlaQoSConditionDestinationVlan_Type(Integer32):
    """Custom type alaQoSConditionDestinationVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSConditionDestinationVlan_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationVlan_Object = MibTableColumn
alaQoSConditionDestinationVlan = _AlaQoSConditionDestinationVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 25),
    _AlaQoSConditionDestinationVlan_Type()
)
alaQoSConditionDestinationVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationVlan.setStatus("current")


class _AlaQoSConditionDestinationVlanStatus_Type(Integer32):
    """Custom type alaQoSConditionDestinationVlanStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionDestinationVlanStatus_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationVlanStatus_Object = MibTableColumn
alaQoSConditionDestinationVlanStatus = _AlaQoSConditionDestinationVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 26),
    _AlaQoSConditionDestinationVlanStatus_Type()
)
alaQoSConditionDestinationVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationVlanStatus.setStatus("current")


class _AlaQoSCondition8021p_Type(Integer32):
    """Custom type alaQoSCondition8021p based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSCondition8021p_Type.__name__ = "Integer32"
_AlaQoSCondition8021p_Object = MibTableColumn
alaQoSCondition8021p = _AlaQoSCondition8021p_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 27),
    _AlaQoSCondition8021p_Type()
)
alaQoSCondition8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSCondition8021p.setStatus("current")


class _AlaQoSCondition8021pStatus_Type(Integer32):
    """Custom type alaQoSCondition8021pStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSCondition8021pStatus_Type.__name__ = "Integer32"
_AlaQoSCondition8021pStatus_Object = MibTableColumn
alaQoSCondition8021pStatus = _AlaQoSCondition8021pStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 28),
    _AlaQoSCondition8021pStatus_Type()
)
alaQoSCondition8021pStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSCondition8021pStatus.setStatus("current")


class _AlaQoSConditionSourceIpAddr_Type(IpAddress):
    """Custom type alaQoSConditionSourceIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AlaQoSConditionSourceIpAddr_Type.__name__ = "IpAddress"
_AlaQoSConditionSourceIpAddr_Object = MibTableColumn
alaQoSConditionSourceIpAddr = _AlaQoSConditionSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 29),
    _AlaQoSConditionSourceIpAddr_Type()
)
alaQoSConditionSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceIpAddr.setStatus("current")


class _AlaQoSConditionSourceIpAddrStatus_Type(Integer32):
    """Custom type alaQoSConditionSourceIpAddrStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionSourceIpAddrStatus_Type.__name__ = "Integer32"
_AlaQoSConditionSourceIpAddrStatus_Object = MibTableColumn
alaQoSConditionSourceIpAddrStatus = _AlaQoSConditionSourceIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 30),
    _AlaQoSConditionSourceIpAddrStatus_Type()
)
alaQoSConditionSourceIpAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceIpAddrStatus.setStatus("current")


class _AlaQoSConditionSourceIpMask_Type(IpAddress):
    """Custom type alaQoSConditionSourceIpMask based on IpAddress"""
    defaultHexValue = "ffffffff"


_AlaQoSConditionSourceIpMask_Type.__name__ = "IpAddress"
_AlaQoSConditionSourceIpMask_Object = MibTableColumn
alaQoSConditionSourceIpMask = _AlaQoSConditionSourceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 31),
    _AlaQoSConditionSourceIpMask_Type()
)
alaQoSConditionSourceIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceIpMask.setStatus("current")


class _AlaQoSConditionSourceNetworkGroup_Type(SnmpAdminString):
    """Custom type alaQoSConditionSourceNetworkGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSConditionSourceNetworkGroup_Type.__name__ = "SnmpAdminString"
_AlaQoSConditionSourceNetworkGroup_Object = MibTableColumn
alaQoSConditionSourceNetworkGroup = _AlaQoSConditionSourceNetworkGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 32),
    _AlaQoSConditionSourceNetworkGroup_Type()
)
alaQoSConditionSourceNetworkGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceNetworkGroup.setStatus("current")


class _AlaQoSConditionSourceNetworkGroupStatus_Type(Integer32):
    """Custom type alaQoSConditionSourceNetworkGroupStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionSourceNetworkGroupStatus_Type.__name__ = "Integer32"
_AlaQoSConditionSourceNetworkGroupStatus_Object = MibTableColumn
alaQoSConditionSourceNetworkGroupStatus = _AlaQoSConditionSourceNetworkGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 33),
    _AlaQoSConditionSourceNetworkGroupStatus_Type()
)
alaQoSConditionSourceNetworkGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceNetworkGroupStatus.setStatus("current")


class _AlaQoSConditionDestinationIpAddr_Type(IpAddress):
    """Custom type alaQoSConditionDestinationIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AlaQoSConditionDestinationIpAddr_Type.__name__ = "IpAddress"
_AlaQoSConditionDestinationIpAddr_Object = MibTableColumn
alaQoSConditionDestinationIpAddr = _AlaQoSConditionDestinationIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 34),
    _AlaQoSConditionDestinationIpAddr_Type()
)
alaQoSConditionDestinationIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationIpAddr.setStatus("current")


class _AlaQoSConditionDestinationIpAddrStatus_Type(Integer32):
    """Custom type alaQoSConditionDestinationIpAddrStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionDestinationIpAddrStatus_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationIpAddrStatus_Object = MibTableColumn
alaQoSConditionDestinationIpAddrStatus = _AlaQoSConditionDestinationIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 35),
    _AlaQoSConditionDestinationIpAddrStatus_Type()
)
alaQoSConditionDestinationIpAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationIpAddrStatus.setStatus("current")


class _AlaQoSConditionDestinationIpMask_Type(IpAddress):
    """Custom type alaQoSConditionDestinationIpMask based on IpAddress"""
    defaultHexValue = "ffffffff"


_AlaQoSConditionDestinationIpMask_Type.__name__ = "IpAddress"
_AlaQoSConditionDestinationIpMask_Object = MibTableColumn
alaQoSConditionDestinationIpMask = _AlaQoSConditionDestinationIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 36),
    _AlaQoSConditionDestinationIpMask_Type()
)
alaQoSConditionDestinationIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationIpMask.setStatus("current")


class _AlaQoSConditionDestinationNetworkGroup_Type(SnmpAdminString):
    """Custom type alaQoSConditionDestinationNetworkGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSConditionDestinationNetworkGroup_Type.__name__ = "SnmpAdminString"
_AlaQoSConditionDestinationNetworkGroup_Object = MibTableColumn
alaQoSConditionDestinationNetworkGroup = _AlaQoSConditionDestinationNetworkGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 37),
    _AlaQoSConditionDestinationNetworkGroup_Type()
)
alaQoSConditionDestinationNetworkGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationNetworkGroup.setStatus("current")


class _AlaQoSConditionDestinationNetworkGroupStatus_Type(Integer32):
    """Custom type alaQoSConditionDestinationNetworkGroupStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionDestinationNetworkGroupStatus_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationNetworkGroupStatus_Object = MibTableColumn
alaQoSConditionDestinationNetworkGroupStatus = _AlaQoSConditionDestinationNetworkGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 38),
    _AlaQoSConditionDestinationNetworkGroupStatus_Type()
)
alaQoSConditionDestinationNetworkGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationNetworkGroupStatus.setStatus("current")


class _AlaQoSConditionMulticastIpAddr_Type(IpAddress):
    """Custom type alaQoSConditionMulticastIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AlaQoSConditionMulticastIpAddr_Type.__name__ = "IpAddress"
_AlaQoSConditionMulticastIpAddr_Object = MibTableColumn
alaQoSConditionMulticastIpAddr = _AlaQoSConditionMulticastIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 39),
    _AlaQoSConditionMulticastIpAddr_Type()
)
alaQoSConditionMulticastIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionMulticastIpAddr.setStatus("current")


class _AlaQoSConditionMulticastIpAddrStatus_Type(Integer32):
    """Custom type alaQoSConditionMulticastIpAddrStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionMulticastIpAddrStatus_Type.__name__ = "Integer32"
_AlaQoSConditionMulticastIpAddrStatus_Object = MibTableColumn
alaQoSConditionMulticastIpAddrStatus = _AlaQoSConditionMulticastIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 40),
    _AlaQoSConditionMulticastIpAddrStatus_Type()
)
alaQoSConditionMulticastIpAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionMulticastIpAddrStatus.setStatus("current")


class _AlaQoSConditionMulticastIpMask_Type(IpAddress):
    """Custom type alaQoSConditionMulticastIpMask based on IpAddress"""
    defaultHexValue = "ffffffff"


_AlaQoSConditionMulticastIpMask_Type.__name__ = "IpAddress"
_AlaQoSConditionMulticastIpMask_Object = MibTableColumn
alaQoSConditionMulticastIpMask = _AlaQoSConditionMulticastIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 41),
    _AlaQoSConditionMulticastIpMask_Type()
)
alaQoSConditionMulticastIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionMulticastIpMask.setStatus("current")


class _AlaQoSConditionMulticastNetworkGroup_Type(SnmpAdminString):
    """Custom type alaQoSConditionMulticastNetworkGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSConditionMulticastNetworkGroup_Type.__name__ = "SnmpAdminString"
_AlaQoSConditionMulticastNetworkGroup_Object = MibTableColumn
alaQoSConditionMulticastNetworkGroup = _AlaQoSConditionMulticastNetworkGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 42),
    _AlaQoSConditionMulticastNetworkGroup_Type()
)
alaQoSConditionMulticastNetworkGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionMulticastNetworkGroup.setStatus("current")


class _AlaQoSConditionMulticastNetworkGroupStatus_Type(Integer32):
    """Custom type alaQoSConditionMulticastNetworkGroupStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionMulticastNetworkGroupStatus_Type.__name__ = "Integer32"
_AlaQoSConditionMulticastNetworkGroupStatus_Object = MibTableColumn
alaQoSConditionMulticastNetworkGroupStatus = _AlaQoSConditionMulticastNetworkGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 43),
    _AlaQoSConditionMulticastNetworkGroupStatus_Type()
)
alaQoSConditionMulticastNetworkGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionMulticastNetworkGroupStatus.setStatus("current")


class _AlaQoSConditionTos_Type(Integer32):
    """Custom type alaQoSConditionTos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSConditionTos_Type.__name__ = "Integer32"
_AlaQoSConditionTos_Object = MibTableColumn
alaQoSConditionTos = _AlaQoSConditionTos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 44),
    _AlaQoSConditionTos_Type()
)
alaQoSConditionTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionTos.setStatus("current")


class _AlaQoSConditionTosStatus_Type(Integer32):
    """Custom type alaQoSConditionTosStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionTosStatus_Type.__name__ = "Integer32"
_AlaQoSConditionTosStatus_Object = MibTableColumn
alaQoSConditionTosStatus = _AlaQoSConditionTosStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 45),
    _AlaQoSConditionTosStatus_Type()
)
alaQoSConditionTosStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionTosStatus.setStatus("current")


class _AlaQoSConditionTosMask_Type(Integer32):
    """Custom type alaQoSConditionTosMask based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSConditionTosMask_Type.__name__ = "Integer32"
_AlaQoSConditionTosMask_Object = MibTableColumn
alaQoSConditionTosMask = _AlaQoSConditionTosMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 46),
    _AlaQoSConditionTosMask_Type()
)
alaQoSConditionTosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionTosMask.setStatus("current")


class _AlaQoSConditionDscp_Type(Integer32):
    """Custom type alaQoSConditionDscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSConditionDscp_Type.__name__ = "Integer32"
_AlaQoSConditionDscp_Object = MibTableColumn
alaQoSConditionDscp = _AlaQoSConditionDscp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 47),
    _AlaQoSConditionDscp_Type()
)
alaQoSConditionDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDscp.setStatus("current")


class _AlaQoSConditionDscpStatus_Type(Integer32):
    """Custom type alaQoSConditionDscpStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionDscpStatus_Type.__name__ = "Integer32"
_AlaQoSConditionDscpStatus_Object = MibTableColumn
alaQoSConditionDscpStatus = _AlaQoSConditionDscpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 48),
    _AlaQoSConditionDscpStatus_Type()
)
alaQoSConditionDscpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDscpStatus.setStatus("current")


class _AlaQoSConditionDscpMask_Type(Integer32):
    """Custom type alaQoSConditionDscpMask based on Integer32"""
    defaultValue = 63

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSConditionDscpMask_Type.__name__ = "Integer32"
_AlaQoSConditionDscpMask_Object = MibTableColumn
alaQoSConditionDscpMask = _AlaQoSConditionDscpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 49),
    _AlaQoSConditionDscpMask_Type()
)
alaQoSConditionDscpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDscpMask.setStatus("current")


class _AlaQoSConditionIpProtocol_Type(Integer32):
    """Custom type alaQoSConditionIpProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSConditionIpProtocol_Type.__name__ = "Integer32"
_AlaQoSConditionIpProtocol_Object = MibTableColumn
alaQoSConditionIpProtocol = _AlaQoSConditionIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 50),
    _AlaQoSConditionIpProtocol_Type()
)
alaQoSConditionIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionIpProtocol.setStatus("current")


class _AlaQoSConditionIpProtocolStatus_Type(Integer32):
    """Custom type alaQoSConditionIpProtocolStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionIpProtocolStatus_Type.__name__ = "Integer32"
_AlaQoSConditionIpProtocolStatus_Object = MibTableColumn
alaQoSConditionIpProtocolStatus = _AlaQoSConditionIpProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 51),
    _AlaQoSConditionIpProtocolStatus_Type()
)
alaQoSConditionIpProtocolStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionIpProtocolStatus.setStatus("current")


class _AlaQoSConditionSourceIpPort_Type(Integer32):
    """Custom type alaQoSConditionSourceIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSConditionSourceIpPort_Type.__name__ = "Integer32"
_AlaQoSConditionSourceIpPort_Object = MibTableColumn
alaQoSConditionSourceIpPort = _AlaQoSConditionSourceIpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 52),
    _AlaQoSConditionSourceIpPort_Type()
)
alaQoSConditionSourceIpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceIpPort.setStatus("current")


class _AlaQoSConditionSourceIpPortStatus_Type(Integer32):
    """Custom type alaQoSConditionSourceIpPortStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionSourceIpPortStatus_Type.__name__ = "Integer32"
_AlaQoSConditionSourceIpPortStatus_Object = MibTableColumn
alaQoSConditionSourceIpPortStatus = _AlaQoSConditionSourceIpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 53),
    _AlaQoSConditionSourceIpPortStatus_Type()
)
alaQoSConditionSourceIpPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceIpPortStatus.setStatus("current")


class _AlaQoSConditionDestinationIpPort_Type(Integer32):
    """Custom type alaQoSConditionDestinationIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSConditionDestinationIpPort_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationIpPort_Object = MibTableColumn
alaQoSConditionDestinationIpPort = _AlaQoSConditionDestinationIpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 54),
    _AlaQoSConditionDestinationIpPort_Type()
)
alaQoSConditionDestinationIpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationIpPort.setStatus("current")


class _AlaQoSConditionDestinationIpPortStatus_Type(Integer32):
    """Custom type alaQoSConditionDestinationIpPortStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionDestinationIpPortStatus_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationIpPortStatus_Object = MibTableColumn
alaQoSConditionDestinationIpPortStatus = _AlaQoSConditionDestinationIpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 55),
    _AlaQoSConditionDestinationIpPortStatus_Type()
)
alaQoSConditionDestinationIpPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationIpPortStatus.setStatus("current")


class _AlaQoSConditionService_Type(SnmpAdminString):
    """Custom type alaQoSConditionService based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSConditionService_Type.__name__ = "SnmpAdminString"
_AlaQoSConditionService_Object = MibTableColumn
alaQoSConditionService = _AlaQoSConditionService_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 56),
    _AlaQoSConditionService_Type()
)
alaQoSConditionService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionService.setStatus("current")


class _AlaQoSConditionServiceStatus_Type(Integer32):
    """Custom type alaQoSConditionServiceStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionServiceStatus_Type.__name__ = "Integer32"
_AlaQoSConditionServiceStatus_Object = MibTableColumn
alaQoSConditionServiceStatus = _AlaQoSConditionServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 57),
    _AlaQoSConditionServiceStatus_Type()
)
alaQoSConditionServiceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionServiceStatus.setStatus("current")


class _AlaQoSConditionServiceGroup_Type(SnmpAdminString):
    """Custom type alaQoSConditionServiceGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSConditionServiceGroup_Type.__name__ = "SnmpAdminString"
_AlaQoSConditionServiceGroup_Object = MibTableColumn
alaQoSConditionServiceGroup = _AlaQoSConditionServiceGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 58),
    _AlaQoSConditionServiceGroup_Type()
)
alaQoSConditionServiceGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionServiceGroup.setStatus("current")


class _AlaQoSConditionServiceGroupStatus_Type(Integer32):
    """Custom type alaQoSConditionServiceGroupStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionServiceGroupStatus_Type.__name__ = "Integer32"
_AlaQoSConditionServiceGroupStatus_Object = MibTableColumn
alaQoSConditionServiceGroupStatus = _AlaQoSConditionServiceGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 59),
    _AlaQoSConditionServiceGroupStatus_Type()
)
alaQoSConditionServiceGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionServiceGroupStatus.setStatus("current")


class _AlaQoSConditionIcmpType_Type(Integer32):
    """Custom type alaQoSConditionIcmpType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSConditionIcmpType_Type.__name__ = "Integer32"
_AlaQoSConditionIcmpType_Object = MibTableColumn
alaQoSConditionIcmpType = _AlaQoSConditionIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 60),
    _AlaQoSConditionIcmpType_Type()
)
alaQoSConditionIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionIcmpType.setStatus("current")


class _AlaQoSConditionIcmpTypeStatus_Type(Integer32):
    """Custom type alaQoSConditionIcmpTypeStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionIcmpTypeStatus_Type.__name__ = "Integer32"
_AlaQoSConditionIcmpTypeStatus_Object = MibTableColumn
alaQoSConditionIcmpTypeStatus = _AlaQoSConditionIcmpTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 61),
    _AlaQoSConditionIcmpTypeStatus_Type()
)
alaQoSConditionIcmpTypeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionIcmpTypeStatus.setStatus("current")


class _AlaQoSConditionIcmpCode_Type(Integer32):
    """Custom type alaQoSConditionIcmpCode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSConditionIcmpCode_Type.__name__ = "Integer32"
_AlaQoSConditionIcmpCode_Object = MibTableColumn
alaQoSConditionIcmpCode = _AlaQoSConditionIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 62),
    _AlaQoSConditionIcmpCode_Type()
)
alaQoSConditionIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionIcmpCode.setStatus("current")


class _AlaQoSConditionIcmpCodeStatus_Type(Integer32):
    """Custom type alaQoSConditionIcmpCodeStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionIcmpCodeStatus_Type.__name__ = "Integer32"
_AlaQoSConditionIcmpCodeStatus_Object = MibTableColumn
alaQoSConditionIcmpCodeStatus = _AlaQoSConditionIcmpCodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 63),
    _AlaQoSConditionIcmpCodeStatus_Type()
)
alaQoSConditionIcmpCodeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionIcmpCodeStatus.setStatus("current")
_AlaQoSConditionRowStatus_Type = RowStatus
_AlaQoSConditionRowStatus_Object = MibTableColumn
alaQoSConditionRowStatus = _AlaQoSConditionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 64),
    _AlaQoSConditionRowStatus_Type()
)
alaQoSConditionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionRowStatus.setStatus("current")


class _AlaQoSConditionSourcePortEnd_Type(Integer32):
    """Custom type alaQoSConditionSourcePortEnd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSConditionSourcePortEnd_Type.__name__ = "Integer32"
_AlaQoSConditionSourcePortEnd_Object = MibTableColumn
alaQoSConditionSourcePortEnd = _AlaQoSConditionSourcePortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 65),
    _AlaQoSConditionSourcePortEnd_Type()
)
alaQoSConditionSourcePortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourcePortEnd.setStatus("current")


class _AlaQoSConditionDestinationPortEnd_Type(Integer32):
    """Custom type alaQoSConditionDestinationPortEnd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSConditionDestinationPortEnd_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationPortEnd_Object = MibTableColumn
alaQoSConditionDestinationPortEnd = _AlaQoSConditionDestinationPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 66),
    _AlaQoSConditionDestinationPortEnd_Type()
)
alaQoSConditionDestinationPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationPortEnd.setStatus("current")


class _AlaQoSConditionSourceIpPortEnd_Type(Integer32):
    """Custom type alaQoSConditionSourceIpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSConditionSourceIpPortEnd_Type.__name__ = "Integer32"
_AlaQoSConditionSourceIpPortEnd_Object = MibTableColumn
alaQoSConditionSourceIpPortEnd = _AlaQoSConditionSourceIpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 67),
    _AlaQoSConditionSourceIpPortEnd_Type()
)
alaQoSConditionSourceIpPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceIpPortEnd.setStatus("current")


class _AlaQoSConditionDestinationIpPortEnd_Type(Integer32):
    """Custom type alaQoSConditionDestinationIpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSConditionDestinationIpPortEnd_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationIpPortEnd_Object = MibTableColumn
alaQoSConditionDestinationIpPortEnd = _AlaQoSConditionDestinationIpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 68),
    _AlaQoSConditionDestinationIpPortEnd_Type()
)
alaQoSConditionDestinationIpPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationIpPortEnd.setStatus("current")


class _AlaQoSConditionSourceTcpPort_Type(Integer32):
    """Custom type alaQoSConditionSourceTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSConditionSourceTcpPort_Type.__name__ = "Integer32"
_AlaQoSConditionSourceTcpPort_Object = MibTableColumn
alaQoSConditionSourceTcpPort = _AlaQoSConditionSourceTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 69),
    _AlaQoSConditionSourceTcpPort_Type()
)
alaQoSConditionSourceTcpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceTcpPort.setStatus("current")


class _AlaQoSConditionSourceTcpPortStatus_Type(Integer32):
    """Custom type alaQoSConditionSourceTcpPortStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionSourceTcpPortStatus_Type.__name__ = "Integer32"
_AlaQoSConditionSourceTcpPortStatus_Object = MibTableColumn
alaQoSConditionSourceTcpPortStatus = _AlaQoSConditionSourceTcpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 70),
    _AlaQoSConditionSourceTcpPortStatus_Type()
)
alaQoSConditionSourceTcpPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceTcpPortStatus.setStatus("current")


class _AlaQoSConditionSourceTcpPortEnd_Type(Integer32):
    """Custom type alaQoSConditionSourceTcpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSConditionSourceTcpPortEnd_Type.__name__ = "Integer32"
_AlaQoSConditionSourceTcpPortEnd_Object = MibTableColumn
alaQoSConditionSourceTcpPortEnd = _AlaQoSConditionSourceTcpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 71),
    _AlaQoSConditionSourceTcpPortEnd_Type()
)
alaQoSConditionSourceTcpPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceTcpPortEnd.setStatus("current")


class _AlaQoSConditionDestinationTcpPort_Type(Integer32):
    """Custom type alaQoSConditionDestinationTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSConditionDestinationTcpPort_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationTcpPort_Object = MibTableColumn
alaQoSConditionDestinationTcpPort = _AlaQoSConditionDestinationTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 72),
    _AlaQoSConditionDestinationTcpPort_Type()
)
alaQoSConditionDestinationTcpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationTcpPort.setStatus("current")


class _AlaQoSConditionDestinationTcpPortStatus_Type(Integer32):
    """Custom type alaQoSConditionDestinationTcpPortStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionDestinationTcpPortStatus_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationTcpPortStatus_Object = MibTableColumn
alaQoSConditionDestinationTcpPortStatus = _AlaQoSConditionDestinationTcpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 73),
    _AlaQoSConditionDestinationTcpPortStatus_Type()
)
alaQoSConditionDestinationTcpPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationTcpPortStatus.setStatus("current")


class _AlaQoSConditionDestinationTcpPortEnd_Type(Integer32):
    """Custom type alaQoSConditionDestinationTcpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSConditionDestinationTcpPortEnd_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationTcpPortEnd_Object = MibTableColumn
alaQoSConditionDestinationTcpPortEnd = _AlaQoSConditionDestinationTcpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 74),
    _AlaQoSConditionDestinationTcpPortEnd_Type()
)
alaQoSConditionDestinationTcpPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationTcpPortEnd.setStatus("current")


class _AlaQoSConditionSourceUdpPort_Type(Integer32):
    """Custom type alaQoSConditionSourceUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSConditionSourceUdpPort_Type.__name__ = "Integer32"
_AlaQoSConditionSourceUdpPort_Object = MibTableColumn
alaQoSConditionSourceUdpPort = _AlaQoSConditionSourceUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 75),
    _AlaQoSConditionSourceUdpPort_Type()
)
alaQoSConditionSourceUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceUdpPort.setStatus("current")


class _AlaQoSConditionSourceUdpPortStatus_Type(Integer32):
    """Custom type alaQoSConditionSourceUdpPortStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionSourceUdpPortStatus_Type.__name__ = "Integer32"
_AlaQoSConditionSourceUdpPortStatus_Object = MibTableColumn
alaQoSConditionSourceUdpPortStatus = _AlaQoSConditionSourceUdpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 76),
    _AlaQoSConditionSourceUdpPortStatus_Type()
)
alaQoSConditionSourceUdpPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceUdpPortStatus.setStatus("current")


class _AlaQoSConditionSourceUdpPortEnd_Type(Integer32):
    """Custom type alaQoSConditionSourceUdpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSConditionSourceUdpPortEnd_Type.__name__ = "Integer32"
_AlaQoSConditionSourceUdpPortEnd_Object = MibTableColumn
alaQoSConditionSourceUdpPortEnd = _AlaQoSConditionSourceUdpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 77),
    _AlaQoSConditionSourceUdpPortEnd_Type()
)
alaQoSConditionSourceUdpPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceUdpPortEnd.setStatus("current")


class _AlaQoSConditionDestinationUdpPort_Type(Integer32):
    """Custom type alaQoSConditionDestinationUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSConditionDestinationUdpPort_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationUdpPort_Object = MibTableColumn
alaQoSConditionDestinationUdpPort = _AlaQoSConditionDestinationUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 78),
    _AlaQoSConditionDestinationUdpPort_Type()
)
alaQoSConditionDestinationUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationUdpPort.setStatus("current")


class _AlaQoSConditionDestinationUdpPortStatus_Type(Integer32):
    """Custom type alaQoSConditionDestinationUdpPortStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionDestinationUdpPortStatus_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationUdpPortStatus_Object = MibTableColumn
alaQoSConditionDestinationUdpPortStatus = _AlaQoSConditionDestinationUdpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 79),
    _AlaQoSConditionDestinationUdpPortStatus_Type()
)
alaQoSConditionDestinationUdpPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationUdpPortStatus.setStatus("current")


class _AlaQoSConditionDestinationUdpPortEnd_Type(Integer32):
    """Custom type alaQoSConditionDestinationUdpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSConditionDestinationUdpPortEnd_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationUdpPortEnd_Object = MibTableColumn
alaQoSConditionDestinationUdpPortEnd = _AlaQoSConditionDestinationUdpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 80),
    _AlaQoSConditionDestinationUdpPortEnd_Type()
)
alaQoSConditionDestinationUdpPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationUdpPortEnd.setStatus("current")


class _AlaQoSConditionEthertype_Type(Integer32):
    """Custom type alaQoSConditionEthertype based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSConditionEthertype_Type.__name__ = "Integer32"
_AlaQoSConditionEthertype_Object = MibTableColumn
alaQoSConditionEthertype = _AlaQoSConditionEthertype_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 81),
    _AlaQoSConditionEthertype_Type()
)
alaQoSConditionEthertype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionEthertype.setStatus("current")


class _AlaQoSConditionEthertypeStatus_Type(Integer32):
    """Custom type alaQoSConditionEthertypeStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionEthertypeStatus_Type.__name__ = "Integer32"
_AlaQoSConditionEthertypeStatus_Object = MibTableColumn
alaQoSConditionEthertypeStatus = _AlaQoSConditionEthertypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 82),
    _AlaQoSConditionEthertypeStatus_Type()
)
alaQoSConditionEthertypeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionEthertypeStatus.setStatus("current")


class _AlaQoSConditionTcpFlags_Type(Integer32):
    """Custom type alaQoSConditionTcpFlags based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("any", 2))
    )


_AlaQoSConditionTcpFlags_Type.__name__ = "Integer32"
_AlaQoSConditionTcpFlags_Object = MibTableColumn
alaQoSConditionTcpFlags = _AlaQoSConditionTcpFlags_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 83),
    _AlaQoSConditionTcpFlags_Type()
)
alaQoSConditionTcpFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionTcpFlags.setStatus("current")


class _AlaQoSConditionTcpFlagsStatus_Type(Integer32):
    """Custom type alaQoSConditionTcpFlagsStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionTcpFlagsStatus_Type.__name__ = "Integer32"
_AlaQoSConditionTcpFlagsStatus_Object = MibTableColumn
alaQoSConditionTcpFlagsStatus = _AlaQoSConditionTcpFlagsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 84),
    _AlaQoSConditionTcpFlagsStatus_Type()
)
alaQoSConditionTcpFlagsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionTcpFlagsStatus.setStatus("current")
_AlaQoSConditionTcpFlagsVal_Type = Integer32
_AlaQoSConditionTcpFlagsVal_Object = MibTableColumn
alaQoSConditionTcpFlagsVal = _AlaQoSConditionTcpFlagsVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 85),
    _AlaQoSConditionTcpFlagsVal_Type()
)
alaQoSConditionTcpFlagsVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionTcpFlagsVal.setStatus("current")


class _AlaQoSConditionTcpFlagsValStatus_Type(Integer32):
    """Custom type alaQoSConditionTcpFlagsValStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionTcpFlagsValStatus_Type.__name__ = "Integer32"
_AlaQoSConditionTcpFlagsValStatus_Object = MibTableColumn
alaQoSConditionTcpFlagsValStatus = _AlaQoSConditionTcpFlagsValStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 86),
    _AlaQoSConditionTcpFlagsValStatus_Type()
)
alaQoSConditionTcpFlagsValStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionTcpFlagsValStatus.setStatus("current")
_AlaQoSConditionTcpFlagsMask_Type = Integer32
_AlaQoSConditionTcpFlagsMask_Object = MibTableColumn
alaQoSConditionTcpFlagsMask = _AlaQoSConditionTcpFlagsMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 87),
    _AlaQoSConditionTcpFlagsMask_Type()
)
alaQoSConditionTcpFlagsMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionTcpFlagsMask.setStatus("current")


class _AlaQoSConditionTcpFlagsMaskStatus_Type(Integer32):
    """Custom type alaQoSConditionTcpFlagsMaskStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionTcpFlagsMaskStatus_Type.__name__ = "Integer32"
_AlaQoSConditionTcpFlagsMaskStatus_Object = MibTableColumn
alaQoSConditionTcpFlagsMaskStatus = _AlaQoSConditionTcpFlagsMaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 88),
    _AlaQoSConditionTcpFlagsMaskStatus_Type()
)
alaQoSConditionTcpFlagsMaskStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionTcpFlagsMaskStatus.setStatus("current")


class _AlaQoSConditionTcpEstablished_Type(Integer32):
    """Custom type alaQoSConditionTcpEstablished based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSConditionTcpEstablished_Type.__name__ = "Integer32"
_AlaQoSConditionTcpEstablished_Object = MibTableColumn
alaQoSConditionTcpEstablished = _AlaQoSConditionTcpEstablished_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 89),
    _AlaQoSConditionTcpEstablished_Type()
)
alaQoSConditionTcpEstablished.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionTcpEstablished.setStatus("current")


class _AlaQoSConditionSourceIpv6Addr_Type(Ipv6Address):
    """Custom type alaQoSConditionSourceIpv6Addr based on Ipv6Address"""
    defaultHexValue = "00000000000000000000000000000000"


_AlaQoSConditionSourceIpv6Addr_Type.__name__ = "Ipv6Address"
_AlaQoSConditionSourceIpv6Addr_Object = MibTableColumn
alaQoSConditionSourceIpv6Addr = _AlaQoSConditionSourceIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 90),
    _AlaQoSConditionSourceIpv6Addr_Type()
)
alaQoSConditionSourceIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceIpv6Addr.setStatus("current")


class _AlaQoSConditionSourceIpv6AddrStatus_Type(Integer32):
    """Custom type alaQoSConditionSourceIpv6AddrStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionSourceIpv6AddrStatus_Type.__name__ = "Integer32"
_AlaQoSConditionSourceIpv6AddrStatus_Object = MibTableColumn
alaQoSConditionSourceIpv6AddrStatus = _AlaQoSConditionSourceIpv6AddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 91),
    _AlaQoSConditionSourceIpv6AddrStatus_Type()
)
alaQoSConditionSourceIpv6AddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceIpv6AddrStatus.setStatus("current")


class _AlaQoSConditionSourceIpv6Mask_Type(Ipv6Address):
    """Custom type alaQoSConditionSourceIpv6Mask based on Ipv6Address"""
    defaultHexValue = "ffffffffffffffffffffffffffffffff"


_AlaQoSConditionSourceIpv6Mask_Type.__name__ = "Ipv6Address"
_AlaQoSConditionSourceIpv6Mask_Object = MibTableColumn
alaQoSConditionSourceIpv6Mask = _AlaQoSConditionSourceIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 92),
    _AlaQoSConditionSourceIpv6Mask_Type()
)
alaQoSConditionSourceIpv6Mask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceIpv6Mask.setStatus("current")


class _AlaQoSConditionDestinationIpv6Addr_Type(Ipv6Address):
    """Custom type alaQoSConditionDestinationIpv6Addr based on Ipv6Address"""
    defaultHexValue = "00000000000000000000000000000000"


_AlaQoSConditionDestinationIpv6Addr_Type.__name__ = "Ipv6Address"
_AlaQoSConditionDestinationIpv6Addr_Object = MibTableColumn
alaQoSConditionDestinationIpv6Addr = _AlaQoSConditionDestinationIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 93),
    _AlaQoSConditionDestinationIpv6Addr_Type()
)
alaQoSConditionDestinationIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationIpv6Addr.setStatus("current")


class _AlaQoSConditionDestinationIpv6AddrStatus_Type(Integer32):
    """Custom type alaQoSConditionDestinationIpv6AddrStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionDestinationIpv6AddrStatus_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationIpv6AddrStatus_Object = MibTableColumn
alaQoSConditionDestinationIpv6AddrStatus = _AlaQoSConditionDestinationIpv6AddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 94),
    _AlaQoSConditionDestinationIpv6AddrStatus_Type()
)
alaQoSConditionDestinationIpv6AddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationIpv6AddrStatus.setStatus("current")


class _AlaQoSConditionDestinationIpv6Mask_Type(Ipv6Address):
    """Custom type alaQoSConditionDestinationIpv6Mask based on Ipv6Address"""
    defaultHexValue = "ffffffffffffffffffffffffffffffff"


_AlaQoSConditionDestinationIpv6Mask_Type.__name__ = "Ipv6Address"
_AlaQoSConditionDestinationIpv6Mask_Object = MibTableColumn
alaQoSConditionDestinationIpv6Mask = _AlaQoSConditionDestinationIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 95),
    _AlaQoSConditionDestinationIpv6Mask_Type()
)
alaQoSConditionDestinationIpv6Mask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationIpv6Mask.setStatus("current")


class _AlaQoSConditionIpv6Traffic_Type(Integer32):
    """Custom type alaQoSConditionIpv6Traffic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSConditionIpv6Traffic_Type.__name__ = "Integer32"
_AlaQoSConditionIpv6Traffic_Object = MibTableColumn
alaQoSConditionIpv6Traffic = _AlaQoSConditionIpv6Traffic_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 96),
    _AlaQoSConditionIpv6Traffic_Type()
)
alaQoSConditionIpv6Traffic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionIpv6Traffic.setStatus("current")


class _AlaQoSConditionIpv6NH_Type(Integer32):
    """Custom type alaQoSConditionIpv6NH based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSConditionIpv6NH_Type.__name__ = "Integer32"
_AlaQoSConditionIpv6NH_Object = MibTableColumn
alaQoSConditionIpv6NH = _AlaQoSConditionIpv6NH_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 97),
    _AlaQoSConditionIpv6NH_Type()
)
alaQoSConditionIpv6NH.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionIpv6NH.setStatus("current")


class _AlaQoSConditionIpv6NHStatus_Type(Integer32):
    """Custom type alaQoSConditionIpv6NHStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionIpv6NHStatus_Type.__name__ = "Integer32"
_AlaQoSConditionIpv6NHStatus_Object = MibTableColumn
alaQoSConditionIpv6NHStatus = _AlaQoSConditionIpv6NHStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 98),
    _AlaQoSConditionIpv6NHStatus_Type()
)
alaQoSConditionIpv6NHStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionIpv6NHStatus.setStatus("current")


class _AlaQoSConditionIpv6FlowLabel_Type(Integer32):
    """Custom type alaQoSConditionIpv6FlowLabel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_AlaQoSConditionIpv6FlowLabel_Type.__name__ = "Integer32"
_AlaQoSConditionIpv6FlowLabel_Object = MibTableColumn
alaQoSConditionIpv6FlowLabel = _AlaQoSConditionIpv6FlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 99),
    _AlaQoSConditionIpv6FlowLabel_Type()
)
alaQoSConditionIpv6FlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionIpv6FlowLabel.setStatus("current")


class _AlaQoSConditionIpv6FlowLabelStatus_Type(Integer32):
    """Custom type alaQoSConditionIpv6FlowLabelStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionIpv6FlowLabelStatus_Type.__name__ = "Integer32"
_AlaQoSConditionIpv6FlowLabelStatus_Object = MibTableColumn
alaQoSConditionIpv6FlowLabelStatus = _AlaQoSConditionIpv6FlowLabelStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 100),
    _AlaQoSConditionIpv6FlowLabelStatus_Type()
)
alaQoSConditionIpv6FlowLabelStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionIpv6FlowLabelStatus.setStatus("current")


class _AlaQoSConditionMcastIpv6Addr_Type(Ipv6Address):
    """Custom type alaQoSConditionMcastIpv6Addr based on Ipv6Address"""
    defaultHexValue = "00000000000000000000000000000000"


_AlaQoSConditionMcastIpv6Addr_Type.__name__ = "Ipv6Address"
_AlaQoSConditionMcastIpv6Addr_Object = MibTableColumn
alaQoSConditionMcastIpv6Addr = _AlaQoSConditionMcastIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 101),
    _AlaQoSConditionMcastIpv6Addr_Type()
)
alaQoSConditionMcastIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionMcastIpv6Addr.setStatus("current")


class _AlaQoSConditionMcastIpv6AddrStatus_Type(Integer32):
    """Custom type alaQoSConditionMcastIpv6AddrStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionMcastIpv6AddrStatus_Type.__name__ = "Integer32"
_AlaQoSConditionMcastIpv6AddrStatus_Object = MibTableColumn
alaQoSConditionMcastIpv6AddrStatus = _AlaQoSConditionMcastIpv6AddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 102),
    _AlaQoSConditionMcastIpv6AddrStatus_Type()
)
alaQoSConditionMcastIpv6AddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionMcastIpv6AddrStatus.setStatus("current")


class _AlaQoSConditionMcastIpv6Mask_Type(Ipv6Address):
    """Custom type alaQoSConditionMcastIpv6Mask based on Ipv6Address"""
    defaultHexValue = "ffffffffffffffffffffffffffffffff"


_AlaQoSConditionMcastIpv6Mask_Type.__name__ = "Ipv6Address"
_AlaQoSConditionMcastIpv6Mask_Object = MibTableColumn
alaQoSConditionMcastIpv6Mask = _AlaQoSConditionMcastIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 103),
    _AlaQoSConditionMcastIpv6Mask_Type()
)
alaQoSConditionMcastIpv6Mask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionMcastIpv6Mask.setStatus("current")


class _AlaQoSConditionDscpEnd_Type(Integer32):
    """Custom type alaQoSConditionDscpEnd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSConditionDscpEnd_Type.__name__ = "Integer32"
_AlaQoSConditionDscpEnd_Object = MibTableColumn
alaQoSConditionDscpEnd = _AlaQoSConditionDscpEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 104),
    _AlaQoSConditionDscpEnd_Type()
)
alaQoSConditionDscpEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDscpEnd.setStatus("current")


class _AlaQoSConditionInnerSourceVlan_Type(Integer32):
    """Custom type alaQoSConditionInnerSourceVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSConditionInnerSourceVlan_Type.__name__ = "Integer32"
_AlaQoSConditionInnerSourceVlan_Object = MibTableColumn
alaQoSConditionInnerSourceVlan = _AlaQoSConditionInnerSourceVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 105),
    _AlaQoSConditionInnerSourceVlan_Type()
)
alaQoSConditionInnerSourceVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionInnerSourceVlan.setStatus("current")


class _AlaQoSConditionInnerSourceVlanStatus_Type(Integer32):
    """Custom type alaQoSConditionInnerSourceVlanStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionInnerSourceVlanStatus_Type.__name__ = "Integer32"
_AlaQoSConditionInnerSourceVlanStatus_Object = MibTableColumn
alaQoSConditionInnerSourceVlanStatus = _AlaQoSConditionInnerSourceVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 106),
    _AlaQoSConditionInnerSourceVlanStatus_Type()
)
alaQoSConditionInnerSourceVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionInnerSourceVlanStatus.setStatus("current")


class _AlaQoSConditionInner8021p_Type(Integer32):
    """Custom type alaQoSConditionInner8021p based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSConditionInner8021p_Type.__name__ = "Integer32"
_AlaQoSConditionInner8021p_Object = MibTableColumn
alaQoSConditionInner8021p = _AlaQoSConditionInner8021p_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 107),
    _AlaQoSConditionInner8021p_Type()
)
alaQoSConditionInner8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionInner8021p.setStatus("current")


class _AlaQoSConditionInner8021pStatus_Type(Integer32):
    """Custom type alaQoSConditionInner8021pStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionInner8021pStatus_Type.__name__ = "Integer32"
_AlaQoSConditionInner8021pStatus_Object = MibTableColumn
alaQoSConditionInner8021pStatus = _AlaQoSConditionInner8021pStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 108),
    _AlaQoSConditionInner8021pStatus_Type()
)
alaQoSConditionInner8021pStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionInner8021pStatus.setStatus("current")


class _AlaQoSConditionVrfName_Type(SnmpAdminString):
    """Custom type alaQoSConditionVrfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSConditionVrfName_Type.__name__ = "SnmpAdminString"
_AlaQoSConditionVrfName_Object = MibTableColumn
alaQoSConditionVrfName = _AlaQoSConditionVrfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 109),
    _AlaQoSConditionVrfName_Type()
)
alaQoSConditionVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionVrfName.setStatus("current")


class _AlaQoSConditionVrfNameStatus_Type(Integer32):
    """Custom type alaQoSConditionVrfNameStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionVrfNameStatus_Type.__name__ = "Integer32"
_AlaQoSConditionVrfNameStatus_Object = MibTableColumn
alaQoSConditionVrfNameStatus = _AlaQoSConditionVrfNameStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 110),
    _AlaQoSConditionVrfNameStatus_Type()
)
alaQoSConditionVrfNameStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionVrfNameStatus.setStatus("current")


class _AlaQoSConditionFragments_Type(Integer32):
    """Custom type alaQoSConditionFragments based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSConditionFragments_Type.__name__ = "Integer32"
_AlaQoSConditionFragments_Object = MibTableColumn
alaQoSConditionFragments = _AlaQoSConditionFragments_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 111),
    _AlaQoSConditionFragments_Type()
)
alaQoSConditionFragments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionFragments.setStatus("current")


class _AlaQoSConditionSourceChassis_Type(Integer32):
    """Custom type alaQoSConditionSourceChassis based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSConditionSourceChassis_Type.__name__ = "Integer32"
_AlaQoSConditionSourceChassis_Object = MibTableColumn
alaQoSConditionSourceChassis = _AlaQoSConditionSourceChassis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 112),
    _AlaQoSConditionSourceChassis_Type()
)
alaQoSConditionSourceChassis.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceChassis.setStatus("current")


class _AlaQoSConditionDestinationChassis_Type(Integer32):
    """Custom type alaQoSConditionDestinationChassis based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSConditionDestinationChassis_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationChassis_Object = MibTableColumn
alaQoSConditionDestinationChassis = _AlaQoSConditionDestinationChassis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 113),
    _AlaQoSConditionDestinationChassis_Type()
)
alaQoSConditionDestinationChassis.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationChassis.setStatus("current")


class _AlaQoSConditionAppFpGroup_Type(SnmpAdminString):
    """Custom type alaQoSConditionAppFpGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_AlaQoSConditionAppFpGroup_Type.__name__ = "SnmpAdminString"
_AlaQoSConditionAppFpGroup_Object = MibTableColumn
alaQoSConditionAppFpGroup = _AlaQoSConditionAppFpGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 114),
    _AlaQoSConditionAppFpGroup_Type()
)
alaQoSConditionAppFpGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionAppFpGroup.setStatus("current")


class _AlaQoSConditionAppFpGroupStatus_Type(Integer32):
    """Custom type alaQoSConditionAppFpGroupStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionAppFpGroupStatus_Type.__name__ = "Integer32"
_AlaQoSConditionAppFpGroupStatus_Object = MibTableColumn
alaQoSConditionAppFpGroupStatus = _AlaQoSConditionAppFpGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 115),
    _AlaQoSConditionAppFpGroupStatus_Type()
)
alaQoSConditionAppFpGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionAppFpGroupStatus.setStatus("current")


class _AlaQoSConditionSIP_Type(Integer32):
    """Custom type alaQoSConditionSIP based on Integer32"""
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
        *(("audio", 1),
          ("video", 2),
          ("other", 3))
    )


_AlaQoSConditionSIP_Type.__name__ = "Integer32"
_AlaQoSConditionSIP_Object = MibTableColumn
alaQoSConditionSIP = _AlaQoSConditionSIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 116),
    _AlaQoSConditionSIP_Type()
)
alaQoSConditionSIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSIP.setStatus("current")


class _AlaQoSConditionSIPStatus_Type(Integer32):
    """Custom type alaQoSConditionSIPStatus based on Integer32"""
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


_AlaQoSConditionSIPStatus_Type.__name__ = "Integer32"
_AlaQoSConditionSIPStatus_Object = MibTableColumn
alaQoSConditionSIPStatus = _AlaQoSConditionSIPStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 117),
    _AlaQoSConditionSIPStatus_Type()
)
alaQoSConditionSIPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSIPStatus.setStatus("current")


class _AlaQoSConditionDPIAppName_Type(SnmpAdminString):
    """Custom type alaQoSConditionDPIAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaQoSConditionDPIAppName_Type.__name__ = "SnmpAdminString"
_AlaQoSConditionDPIAppName_Object = MibTableColumn
alaQoSConditionDPIAppName = _AlaQoSConditionDPIAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 118),
    _AlaQoSConditionDPIAppName_Type()
)
alaQoSConditionDPIAppName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDPIAppName.setStatus("current")


class _AlaQoSConditionDPIGrpName_Type(SnmpAdminString):
    """Custom type alaQoSConditionDPIGrpName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaQoSConditionDPIGrpName_Type.__name__ = "SnmpAdminString"
_AlaQoSConditionDPIGrpName_Object = MibTableColumn
alaQoSConditionDPIGrpName = _AlaQoSConditionDPIGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 119),
    _AlaQoSConditionDPIGrpName_Type()
)
alaQoSConditionDPIGrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDPIGrpName.setStatus("current")


class _AlaQoSConditionDPIAppNameStatus_Type(Integer32):
    """Custom type alaQoSConditionDPIAppNameStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionDPIAppNameStatus_Type.__name__ = "Integer32"
_AlaQoSConditionDPIAppNameStatus_Object = MibTableColumn
alaQoSConditionDPIAppNameStatus = _AlaQoSConditionDPIAppNameStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 120),
    _AlaQoSConditionDPIAppNameStatus_Type()
)
alaQoSConditionDPIAppNameStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDPIAppNameStatus.setStatus("current")


class _AlaQoSConditionDPIAppGroupStatus_Type(Integer32):
    """Custom type alaQoSConditionDPIAppGroupStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionDPIAppGroupStatus_Type.__name__ = "Integer32"
_AlaQoSConditionDPIAppGroupStatus_Object = MibTableColumn
alaQoSConditionDPIAppGroupStatus = _AlaQoSConditionDPIAppGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 121),
    _AlaQoSConditionDPIAppGroupStatus_Type()
)
alaQoSConditionDPIAppGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDPIAppGroupStatus.setStatus("current")


class _AlaQoSConditionVxlanVni_Type(Integer32):
    """Custom type alaQoSConditionVxlanVni based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_AlaQoSConditionVxlanVni_Type.__name__ = "Integer32"
_AlaQoSConditionVxlanVni_Object = MibTableColumn
alaQoSConditionVxlanVni = _AlaQoSConditionVxlanVni_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 122),
    _AlaQoSConditionVxlanVni_Type()
)
alaQoSConditionVxlanVni.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionVxlanVni.setStatus("current")


class _AlaQoSConditionVxlanVniStatus_Type(Integer32):
    """Custom type alaQoSConditionVxlanVniStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionVxlanVniStatus_Type.__name__ = "Integer32"
_AlaQoSConditionVxlanVniStatus_Object = MibTableColumn
alaQoSConditionVxlanVniStatus = _AlaQoSConditionVxlanVniStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 123),
    _AlaQoSConditionVxlanVniStatus_Type()
)
alaQoSConditionVxlanVniStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionVxlanVniStatus.setStatus("current")


class _AlaQoSConditionVxlanPort_Type(Integer32):
    """Custom type alaQoSConditionVxlanPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSConditionVxlanPort_Type.__name__ = "Integer32"
_AlaQoSConditionVxlanPort_Object = MibTableColumn
alaQoSConditionVxlanPort = _AlaQoSConditionVxlanPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 124),
    _AlaQoSConditionVxlanPort_Type()
)
alaQoSConditionVxlanPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionVxlanPort.setStatus("current")


class _AlaQoSConditionVxlanPortStatus_Type(Integer32):
    """Custom type alaQoSConditionVxlanPortStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionVxlanPortStatus_Type.__name__ = "Integer32"
_AlaQoSConditionVxlanPortStatus_Object = MibTableColumn
alaQoSConditionVxlanPortStatus = _AlaQoSConditionVxlanPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 125),
    _AlaQoSConditionVxlanPortStatus_Type()
)
alaQoSConditionVxlanPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionVxlanPortStatus.setStatus("current")


class _AlaQoSConditionVmSourceMacAddr_Type(MacAddress):
    """Custom type alaQoSConditionVmSourceMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_AlaQoSConditionVmSourceMacAddr_Type.__name__ = "MacAddress"
_AlaQoSConditionVmSourceMacAddr_Object = MibTableColumn
alaQoSConditionVmSourceMacAddr = _AlaQoSConditionVmSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 126),
    _AlaQoSConditionVmSourceMacAddr_Type()
)
alaQoSConditionVmSourceMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionVmSourceMacAddr.setStatus("current")


class _AlaQoSConditionVmSourceMacAddrStatus_Type(Integer32):
    """Custom type alaQoSConditionVmSourceMacAddrStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionVmSourceMacAddrStatus_Type.__name__ = "Integer32"
_AlaQoSConditionVmSourceMacAddrStatus_Object = MibTableColumn
alaQoSConditionVmSourceMacAddrStatus = _AlaQoSConditionVmSourceMacAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 127),
    _AlaQoSConditionVmSourceMacAddrStatus_Type()
)
alaQoSConditionVmSourceMacAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionVmSourceMacAddrStatus.setStatus("current")


class _AlaQoSConditionVmSourceMacMask_Type(MacAddress):
    """Custom type alaQoSConditionVmSourceMacMask based on MacAddress"""
    defaultHexValue = "ffffffffffff"


_AlaQoSConditionVmSourceMacMask_Type.__name__ = "MacAddress"
_AlaQoSConditionVmSourceMacMask_Object = MibTableColumn
alaQoSConditionVmSourceMacMask = _AlaQoSConditionVmSourceMacMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 128),
    _AlaQoSConditionVmSourceMacMask_Type()
)
alaQoSConditionVmSourceMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionVmSourceMacMask.setStatus("current")


class _AlaQoSConditionVmSourceIpAddr_Type(IpAddress):
    """Custom type alaQoSConditionVmSourceIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AlaQoSConditionVmSourceIpAddr_Type.__name__ = "IpAddress"
_AlaQoSConditionVmSourceIpAddr_Object = MibTableColumn
alaQoSConditionVmSourceIpAddr = _AlaQoSConditionVmSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 129),
    _AlaQoSConditionVmSourceIpAddr_Type()
)
alaQoSConditionVmSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionVmSourceIpAddr.setStatus("current")


class _AlaQoSConditionVmSourceIpAddrStatus_Type(Integer32):
    """Custom type alaQoSConditionVmSourceIpAddrStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionVmSourceIpAddrStatus_Type.__name__ = "Integer32"
_AlaQoSConditionVmSourceIpAddrStatus_Object = MibTableColumn
alaQoSConditionVmSourceIpAddrStatus = _AlaQoSConditionVmSourceIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 130),
    _AlaQoSConditionVmSourceIpAddrStatus_Type()
)
alaQoSConditionVmSourceIpAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionVmSourceIpAddrStatus.setStatus("current")


class _AlaQoSConditionVmSourceIpMask_Type(IpAddress):
    """Custom type alaQoSConditionVmSourceIpMask based on IpAddress"""
    defaultHexValue = "ffffffff"


_AlaQoSConditionVmSourceIpMask_Type.__name__ = "IpAddress"
_AlaQoSConditionVmSourceIpMask_Object = MibTableColumn
alaQoSConditionVmSourceIpMask = _AlaQoSConditionVmSourceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 131),
    _AlaQoSConditionVmSourceIpMask_Type()
)
alaQoSConditionVmSourceIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionVmSourceIpMask.setStatus("current")


class _AlaQoSConditionVmSourceIpv6IpAddr_Type(Ipv6Address):
    """Custom type alaQoSConditionVmSourceIpv6IpAddr based on Ipv6Address"""
    defaultHexValue = "00000000000000000000000000000000"


_AlaQoSConditionVmSourceIpv6IpAddr_Type.__name__ = "Ipv6Address"
_AlaQoSConditionVmSourceIpv6IpAddr_Object = MibTableColumn
alaQoSConditionVmSourceIpv6IpAddr = _AlaQoSConditionVmSourceIpv6IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 132),
    _AlaQoSConditionVmSourceIpv6IpAddr_Type()
)
alaQoSConditionVmSourceIpv6IpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionVmSourceIpv6IpAddr.setStatus("current")


class _AlaQoSConditionVmSourceIpv6IpAddrStatus_Type(Integer32):
    """Custom type alaQoSConditionVmSourceIpv6IpAddrStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionVmSourceIpv6IpAddrStatus_Type.__name__ = "Integer32"
_AlaQoSConditionVmSourceIpv6IpAddrStatus_Object = MibTableColumn
alaQoSConditionVmSourceIpv6IpAddrStatus = _AlaQoSConditionVmSourceIpv6IpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 133),
    _AlaQoSConditionVmSourceIpv6IpAddrStatus_Type()
)
alaQoSConditionVmSourceIpv6IpAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionVmSourceIpv6IpAddrStatus.setStatus("current")


class _AlaQoSConditionVmSourceIpv6IpMask_Type(Ipv6Address):
    """Custom type alaQoSConditionVmSourceIpv6IpMask based on Ipv6Address"""
    defaultHexValue = "ffffffffffffffffffffffffffffffff"


_AlaQoSConditionVmSourceIpv6IpMask_Type.__name__ = "Ipv6Address"
_AlaQoSConditionVmSourceIpv6IpMask_Object = MibTableColumn
alaQoSConditionVmSourceIpv6IpMask = _AlaQoSConditionVmSourceIpv6IpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 134),
    _AlaQoSConditionVmSourceIpv6IpMask_Type()
)
alaQoSConditionVmSourceIpv6IpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionVmSourceIpv6IpMask.setStatus("current")


class _AlaQoSConditionVmIpProtocol_Type(Integer32):
    """Custom type alaQoSConditionVmIpProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSConditionVmIpProtocol_Type.__name__ = "Integer32"
_AlaQoSConditionVmIpProtocol_Object = MibTableColumn
alaQoSConditionVmIpProtocol = _AlaQoSConditionVmIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 135),
    _AlaQoSConditionVmIpProtocol_Type()
)
alaQoSConditionVmIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionVmIpProtocol.setStatus("current")


class _AlaQoSConditionVmIpProtocolStatus_Type(Integer32):
    """Custom type alaQoSConditionVmIpProtocolStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionVmIpProtocolStatus_Type.__name__ = "Integer32"
_AlaQoSConditionVmIpProtocolStatus_Object = MibTableColumn
alaQoSConditionVmIpProtocolStatus = _AlaQoSConditionVmIpProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 136),
    _AlaQoSConditionVmIpProtocolStatus_Type()
)
alaQoSConditionVmIpProtocolStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionVmIpProtocolStatus.setStatus("current")


class _AlaQosConditionVmL4SourcePort_Type(Integer32):
    """Custom type alaQosConditionVmL4SourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQosConditionVmL4SourcePort_Type.__name__ = "Integer32"
_AlaQosConditionVmL4SourcePort_Object = MibTableColumn
alaQosConditionVmL4SourcePort = _AlaQosConditionVmL4SourcePort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 137),
    _AlaQosConditionVmL4SourcePort_Type()
)
alaQosConditionVmL4SourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQosConditionVmL4SourcePort.setStatus("current")


class _AlaQosConditionVmL4SourcePortStatus_Type(Integer32):
    """Custom type alaQosConditionVmL4SourcePortStatus based on Integer32"""
    defaultValue = 2

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


_AlaQosConditionVmL4SourcePortStatus_Type.__name__ = "Integer32"
_AlaQosConditionVmL4SourcePortStatus_Object = MibTableColumn
alaQosConditionVmL4SourcePortStatus = _AlaQosConditionVmL4SourcePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 138),
    _AlaQosConditionVmL4SourcePortStatus_Type()
)
alaQosConditionVmL4SourcePortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQosConditionVmL4SourcePortStatus.setStatus("current")


class _AlaQosConditionVmL4DestPort_Type(Integer32):
    """Custom type alaQosConditionVmL4DestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQosConditionVmL4DestPort_Type.__name__ = "Integer32"
_AlaQosConditionVmL4DestPort_Object = MibTableColumn
alaQosConditionVmL4DestPort = _AlaQosConditionVmL4DestPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 139),
    _AlaQosConditionVmL4DestPort_Type()
)
alaQosConditionVmL4DestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQosConditionVmL4DestPort.setStatus("current")


class _AlaQosConditionVmL4DestPortStatus_Type(Integer32):
    """Custom type alaQosConditionVmL4DestPortStatus based on Integer32"""
    defaultValue = 2

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


_AlaQosConditionVmL4DestPortStatus_Type.__name__ = "Integer32"
_AlaQosConditionVmL4DestPortStatus_Object = MibTableColumn
alaQosConditionVmL4DestPortStatus = _AlaQosConditionVmL4DestPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 140),
    _AlaQosConditionVmL4DestPortStatus_Type()
)
alaQosConditionVmL4DestPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQosConditionVmL4DestPortStatus.setStatus("current")


class _AlaQosConditionVxlanStatus_Type(Integer32):
    """Custom type alaQosConditionVxlanStatus based on Integer32"""
    defaultValue = 2

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


_AlaQosConditionVxlanStatus_Type.__name__ = "Integer32"
_AlaQosConditionVxlanStatus_Object = MibTableColumn
alaQosConditionVxlanStatus = _AlaQosConditionVxlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 141),
    _AlaQosConditionVxlanStatus_Type()
)
alaQosConditionVxlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQosConditionVxlanStatus.setStatus("current")


class _AlaQoSConditionSourcePortSplitGroup_Type(SnmpAdminString):
    """Custom type alaQoSConditionSourcePortSplitGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSConditionSourcePortSplitGroup_Type.__name__ = "SnmpAdminString"
_AlaQoSConditionSourcePortSplitGroup_Object = MibTableColumn
alaQoSConditionSourcePortSplitGroup = _AlaQoSConditionSourcePortSplitGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 142),
    _AlaQoSConditionSourcePortSplitGroup_Type()
)
alaQoSConditionSourcePortSplitGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourcePortSplitGroup.setStatus("current")


class _AlaQoSConditionSourcePortSplitGroupStatus_Type(Integer32):
    """Custom type alaQoSConditionSourcePortSplitGroupStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSConditionSourcePortSplitGroupStatus_Type.__name__ = "Integer32"
_AlaQoSConditionSourcePortSplitGroupStatus_Object = MibTableColumn
alaQoSConditionSourcePortSplitGroupStatus = _AlaQoSConditionSourcePortSplitGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 143),
    _AlaQoSConditionSourcePortSplitGroupStatus_Type()
)
alaQoSConditionSourcePortSplitGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourcePortSplitGroupStatus.setStatus("current")
_AlaQoSAppliedConditionTable_Object = MibTable
alaQoSAppliedConditionTable = _AlaQoSAppliedConditionTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaQoSAppliedConditionTable.setStatus("current")
_AlaQoSAppliedConditionEntry_Object = MibTableRow
alaQoSAppliedConditionEntry = _AlaQoSAppliedConditionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1)
)
alaQoSAppliedConditionEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionName"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedConditionEntry.setStatus("current")


class _AlaQoSAppliedConditionName_Type(SnmpAdminString):
    """Custom type alaQoSAppliedConditionName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedConditionName_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedConditionName_Object = MibTableColumn
alaQoSAppliedConditionName = _AlaQoSAppliedConditionName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 1),
    _AlaQoSAppliedConditionName_Type()
)
alaQoSAppliedConditionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionName.setStatus("current")


class _AlaQoSAppliedConditionSource_Type(Integer32):
    """Custom type alaQoSAppliedConditionSource based on Integer32"""
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
        *(("ldap", 1),
          ("cli", 2),
          ("blt", 3),
          ("api", 4),
          ("imp", 5))
    )


_AlaQoSAppliedConditionSource_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSource_Object = MibTableColumn
alaQoSAppliedConditionSource = _AlaQoSAppliedConditionSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 2),
    _AlaQoSAppliedConditionSource_Type()
)
alaQoSAppliedConditionSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSource.setStatus("current")


class _AlaQoSAppliedConditionSourceSlot_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSAppliedConditionSourceSlot_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceSlot_Object = MibTableColumn
alaQoSAppliedConditionSourceSlot = _AlaQoSAppliedConditionSourceSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 3),
    _AlaQoSAppliedConditionSourceSlot_Type()
)
alaQoSAppliedConditionSourceSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceSlot.setStatus("current")


class _AlaQoSAppliedConditionSourceSlotStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceSlotStatus based on Integer32"""
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


_AlaQoSAppliedConditionSourceSlotStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceSlotStatus_Object = MibTableColumn
alaQoSAppliedConditionSourceSlotStatus = _AlaQoSAppliedConditionSourceSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 4),
    _AlaQoSAppliedConditionSourceSlotStatus_Type()
)
alaQoSAppliedConditionSourceSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceSlotStatus.setStatus("current")


class _AlaQoSAppliedConditionSourcePort_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_AlaQoSAppliedConditionSourcePort_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourcePort_Object = MibTableColumn
alaQoSAppliedConditionSourcePort = _AlaQoSAppliedConditionSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 5),
    _AlaQoSAppliedConditionSourcePort_Type()
)
alaQoSAppliedConditionSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourcePort.setStatus("current")


class _AlaQoSAppliedConditionSourcePortGroup_Type(SnmpAdminString):
    """Custom type alaQoSAppliedConditionSourcePortGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedConditionSourcePortGroup_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedConditionSourcePortGroup_Object = MibTableColumn
alaQoSAppliedConditionSourcePortGroup = _AlaQoSAppliedConditionSourcePortGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 6),
    _AlaQoSAppliedConditionSourcePortGroup_Type()
)
alaQoSAppliedConditionSourcePortGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourcePortGroup.setStatus("current")


class _AlaQoSAppliedConditionSourcePortGroupStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourcePortGroupStatus based on Integer32"""
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


_AlaQoSAppliedConditionSourcePortGroupStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourcePortGroupStatus_Object = MibTableColumn
alaQoSAppliedConditionSourcePortGroupStatus = _AlaQoSAppliedConditionSourcePortGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 7),
    _AlaQoSAppliedConditionSourcePortGroupStatus_Type()
)
alaQoSAppliedConditionSourcePortGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourcePortGroupStatus.setStatus("current")


class _AlaQoSAppliedConditionDestinationSlot_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSAppliedConditionDestinationSlot_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationSlot_Object = MibTableColumn
alaQoSAppliedConditionDestinationSlot = _AlaQoSAppliedConditionDestinationSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 8),
    _AlaQoSAppliedConditionDestinationSlot_Type()
)
alaQoSAppliedConditionDestinationSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationSlot.setStatus("current")


class _AlaQoSAppliedConditionDestinationSlotStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationSlotStatus based on Integer32"""
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


_AlaQoSAppliedConditionDestinationSlotStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationSlotStatus_Object = MibTableColumn
alaQoSAppliedConditionDestinationSlotStatus = _AlaQoSAppliedConditionDestinationSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 9),
    _AlaQoSAppliedConditionDestinationSlotStatus_Type()
)
alaQoSAppliedConditionDestinationSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationSlotStatus.setStatus("current")


class _AlaQoSAppliedConditionDestinationPort_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_AlaQoSAppliedConditionDestinationPort_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationPort_Object = MibTableColumn
alaQoSAppliedConditionDestinationPort = _AlaQoSAppliedConditionDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 10),
    _AlaQoSAppliedConditionDestinationPort_Type()
)
alaQoSAppliedConditionDestinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationPort.setStatus("current")


class _AlaQoSAppliedConditionDestinationPortGroup_Type(SnmpAdminString):
    """Custom type alaQoSAppliedConditionDestinationPortGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedConditionDestinationPortGroup_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedConditionDestinationPortGroup_Object = MibTableColumn
alaQoSAppliedConditionDestinationPortGroup = _AlaQoSAppliedConditionDestinationPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 11),
    _AlaQoSAppliedConditionDestinationPortGroup_Type()
)
alaQoSAppliedConditionDestinationPortGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationPortGroup.setStatus("current")


class _AlaQoSAppliedConditionDestinationPortGroupStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationPortGroupStatus based on Integer32"""
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


_AlaQoSAppliedConditionDestinationPortGroupStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationPortGroupStatus_Object = MibTableColumn
alaQoSAppliedConditionDestinationPortGroupStatus = _AlaQoSAppliedConditionDestinationPortGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 12),
    _AlaQoSAppliedConditionDestinationPortGroupStatus_Type()
)
alaQoSAppliedConditionDestinationPortGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationPortGroupStatus.setStatus("current")
_AlaQoSAppliedConditionSourceMacAddr_Type = MacAddress
_AlaQoSAppliedConditionSourceMacAddr_Object = MibTableColumn
alaQoSAppliedConditionSourceMacAddr = _AlaQoSAppliedConditionSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 13),
    _AlaQoSAppliedConditionSourceMacAddr_Type()
)
alaQoSAppliedConditionSourceMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceMacAddr.setStatus("current")


class _AlaQoSAppliedConditionSourceMacAddrStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceMacAddrStatus based on Integer32"""
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


_AlaQoSAppliedConditionSourceMacAddrStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceMacAddrStatus_Object = MibTableColumn
alaQoSAppliedConditionSourceMacAddrStatus = _AlaQoSAppliedConditionSourceMacAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 14),
    _AlaQoSAppliedConditionSourceMacAddrStatus_Type()
)
alaQoSAppliedConditionSourceMacAddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceMacAddrStatus.setStatus("current")
_AlaQoSAppliedConditionSourceMacMask_Type = MacAddress
_AlaQoSAppliedConditionSourceMacMask_Object = MibTableColumn
alaQoSAppliedConditionSourceMacMask = _AlaQoSAppliedConditionSourceMacMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 15),
    _AlaQoSAppliedConditionSourceMacMask_Type()
)
alaQoSAppliedConditionSourceMacMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceMacMask.setStatus("current")


class _AlaQoSAppliedConditionSourceMacGroup_Type(SnmpAdminString):
    """Custom type alaQoSAppliedConditionSourceMacGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedConditionSourceMacGroup_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedConditionSourceMacGroup_Object = MibTableColumn
alaQoSAppliedConditionSourceMacGroup = _AlaQoSAppliedConditionSourceMacGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 16),
    _AlaQoSAppliedConditionSourceMacGroup_Type()
)
alaQoSAppliedConditionSourceMacGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceMacGroup.setStatus("current")


class _AlaQoSAppliedConditionSourceMacGroupStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceMacGroupStatus based on Integer32"""
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


_AlaQoSAppliedConditionSourceMacGroupStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceMacGroupStatus_Object = MibTableColumn
alaQoSAppliedConditionSourceMacGroupStatus = _AlaQoSAppliedConditionSourceMacGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 17),
    _AlaQoSAppliedConditionSourceMacGroupStatus_Type()
)
alaQoSAppliedConditionSourceMacGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceMacGroupStatus.setStatus("current")
_AlaQoSAppliedConditionDestinationMacAddr_Type = MacAddress
_AlaQoSAppliedConditionDestinationMacAddr_Object = MibTableColumn
alaQoSAppliedConditionDestinationMacAddr = _AlaQoSAppliedConditionDestinationMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 18),
    _AlaQoSAppliedConditionDestinationMacAddr_Type()
)
alaQoSAppliedConditionDestinationMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationMacAddr.setStatus("current")


class _AlaQoSAppliedConditionDestinationMacAddrStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationMacAddrStatus based on Integer32"""
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


_AlaQoSAppliedConditionDestinationMacAddrStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationMacAddrStatus_Object = MibTableColumn
alaQoSAppliedConditionDestinationMacAddrStatus = _AlaQoSAppliedConditionDestinationMacAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 19),
    _AlaQoSAppliedConditionDestinationMacAddrStatus_Type()
)
alaQoSAppliedConditionDestinationMacAddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationMacAddrStatus.setStatus("current")
_AlaQoSAppliedConditionDestinationMacMask_Type = MacAddress
_AlaQoSAppliedConditionDestinationMacMask_Object = MibTableColumn
alaQoSAppliedConditionDestinationMacMask = _AlaQoSAppliedConditionDestinationMacMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 20),
    _AlaQoSAppliedConditionDestinationMacMask_Type()
)
alaQoSAppliedConditionDestinationMacMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationMacMask.setStatus("current")


class _AlaQoSAppliedConditionDestinationMacGroup_Type(SnmpAdminString):
    """Custom type alaQoSAppliedConditionDestinationMacGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedConditionDestinationMacGroup_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedConditionDestinationMacGroup_Object = MibTableColumn
alaQoSAppliedConditionDestinationMacGroup = _AlaQoSAppliedConditionDestinationMacGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 21),
    _AlaQoSAppliedConditionDestinationMacGroup_Type()
)
alaQoSAppliedConditionDestinationMacGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationMacGroup.setStatus("current")


class _AlaQoSAppliedConditionDestinationMacGroupStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationMacGroupStatus based on Integer32"""
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


_AlaQoSAppliedConditionDestinationMacGroupStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationMacGroupStatus_Object = MibTableColumn
alaQoSAppliedConditionDestinationMacGroupStatus = _AlaQoSAppliedConditionDestinationMacGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 22),
    _AlaQoSAppliedConditionDestinationMacGroupStatus_Type()
)
alaQoSAppliedConditionDestinationMacGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationMacGroupStatus.setStatus("current")


class _AlaQoSAppliedConditionSourceVlan_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSAppliedConditionSourceVlan_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceVlan_Object = MibTableColumn
alaQoSAppliedConditionSourceVlan = _AlaQoSAppliedConditionSourceVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 23),
    _AlaQoSAppliedConditionSourceVlan_Type()
)
alaQoSAppliedConditionSourceVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceVlan.setStatus("current")


class _AlaQoSAppliedConditionSourceVlanStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceVlanStatus based on Integer32"""
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


_AlaQoSAppliedConditionSourceVlanStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceVlanStatus_Object = MibTableColumn
alaQoSAppliedConditionSourceVlanStatus = _AlaQoSAppliedConditionSourceVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 24),
    _AlaQoSAppliedConditionSourceVlanStatus_Type()
)
alaQoSAppliedConditionSourceVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceVlanStatus.setStatus("current")


class _AlaQoSAppliedConditionDestinationVlan_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSAppliedConditionDestinationVlan_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationVlan_Object = MibTableColumn
alaQoSAppliedConditionDestinationVlan = _AlaQoSAppliedConditionDestinationVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 25),
    _AlaQoSAppliedConditionDestinationVlan_Type()
)
alaQoSAppliedConditionDestinationVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationVlan.setStatus("current")


class _AlaQoSAppliedConditionDestinationVlanStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationVlanStatus based on Integer32"""
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


_AlaQoSAppliedConditionDestinationVlanStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationVlanStatus_Object = MibTableColumn
alaQoSAppliedConditionDestinationVlanStatus = _AlaQoSAppliedConditionDestinationVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 26),
    _AlaQoSAppliedConditionDestinationVlanStatus_Type()
)
alaQoSAppliedConditionDestinationVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationVlanStatus.setStatus("current")


class _AlaQoSAppliedCondition8021p_Type(Integer32):
    """Custom type alaQoSAppliedCondition8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSAppliedCondition8021p_Type.__name__ = "Integer32"
_AlaQoSAppliedCondition8021p_Object = MibTableColumn
alaQoSAppliedCondition8021p = _AlaQoSAppliedCondition8021p_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 27),
    _AlaQoSAppliedCondition8021p_Type()
)
alaQoSAppliedCondition8021p.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedCondition8021p.setStatus("current")


class _AlaQoSAppliedCondition8021pStatus_Type(Integer32):
    """Custom type alaQoSAppliedCondition8021pStatus based on Integer32"""
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


_AlaQoSAppliedCondition8021pStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedCondition8021pStatus_Object = MibTableColumn
alaQoSAppliedCondition8021pStatus = _AlaQoSAppliedCondition8021pStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 28),
    _AlaQoSAppliedCondition8021pStatus_Type()
)
alaQoSAppliedCondition8021pStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedCondition8021pStatus.setStatus("current")
_AlaQoSAppliedConditionSourceIpAddr_Type = IpAddress
_AlaQoSAppliedConditionSourceIpAddr_Object = MibTableColumn
alaQoSAppliedConditionSourceIpAddr = _AlaQoSAppliedConditionSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 29),
    _AlaQoSAppliedConditionSourceIpAddr_Type()
)
alaQoSAppliedConditionSourceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceIpAddr.setStatus("current")


class _AlaQoSAppliedConditionSourceIpAddrStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceIpAddrStatus based on Integer32"""
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


_AlaQoSAppliedConditionSourceIpAddrStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceIpAddrStatus_Object = MibTableColumn
alaQoSAppliedConditionSourceIpAddrStatus = _AlaQoSAppliedConditionSourceIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 30),
    _AlaQoSAppliedConditionSourceIpAddrStatus_Type()
)
alaQoSAppliedConditionSourceIpAddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceIpAddrStatus.setStatus("current")
_AlaQoSAppliedConditionSourceIpMask_Type = IpAddress
_AlaQoSAppliedConditionSourceIpMask_Object = MibTableColumn
alaQoSAppliedConditionSourceIpMask = _AlaQoSAppliedConditionSourceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 31),
    _AlaQoSAppliedConditionSourceIpMask_Type()
)
alaQoSAppliedConditionSourceIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceIpMask.setStatus("current")


class _AlaQoSAppliedConditionSourceNetworkGroup_Type(SnmpAdminString):
    """Custom type alaQoSAppliedConditionSourceNetworkGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedConditionSourceNetworkGroup_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedConditionSourceNetworkGroup_Object = MibTableColumn
alaQoSAppliedConditionSourceNetworkGroup = _AlaQoSAppliedConditionSourceNetworkGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 32),
    _AlaQoSAppliedConditionSourceNetworkGroup_Type()
)
alaQoSAppliedConditionSourceNetworkGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceNetworkGroup.setStatus("current")


class _AlaQoSAppliedConditionSourceNetworkGroupStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceNetworkGroupStatus based on Integer32"""
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


_AlaQoSAppliedConditionSourceNetworkGroupStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceNetworkGroupStatus_Object = MibTableColumn
alaQoSAppliedConditionSourceNetworkGroupStatus = _AlaQoSAppliedConditionSourceNetworkGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 33),
    _AlaQoSAppliedConditionSourceNetworkGroupStatus_Type()
)
alaQoSAppliedConditionSourceNetworkGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceNetworkGroupStatus.setStatus("current")
_AlaQoSAppliedConditionDestinationIpAddr_Type = IpAddress
_AlaQoSAppliedConditionDestinationIpAddr_Object = MibTableColumn
alaQoSAppliedConditionDestinationIpAddr = _AlaQoSAppliedConditionDestinationIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 34),
    _AlaQoSAppliedConditionDestinationIpAddr_Type()
)
alaQoSAppliedConditionDestinationIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationIpAddr.setStatus("current")


class _AlaQoSAppliedConditionDestinationIpAddrStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationIpAddrStatus based on Integer32"""
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


_AlaQoSAppliedConditionDestinationIpAddrStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationIpAddrStatus_Object = MibTableColumn
alaQoSAppliedConditionDestinationIpAddrStatus = _AlaQoSAppliedConditionDestinationIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 35),
    _AlaQoSAppliedConditionDestinationIpAddrStatus_Type()
)
alaQoSAppliedConditionDestinationIpAddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationIpAddrStatus.setStatus("current")
_AlaQoSAppliedConditionDestinationIpMask_Type = IpAddress
_AlaQoSAppliedConditionDestinationIpMask_Object = MibTableColumn
alaQoSAppliedConditionDestinationIpMask = _AlaQoSAppliedConditionDestinationIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 36),
    _AlaQoSAppliedConditionDestinationIpMask_Type()
)
alaQoSAppliedConditionDestinationIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationIpMask.setStatus("current")


class _AlaQoSAppliedConditionDestinationNetworkGroup_Type(SnmpAdminString):
    """Custom type alaQoSAppliedConditionDestinationNetworkGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedConditionDestinationNetworkGroup_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedConditionDestinationNetworkGroup_Object = MibTableColumn
alaQoSAppliedConditionDestinationNetworkGroup = _AlaQoSAppliedConditionDestinationNetworkGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 37),
    _AlaQoSAppliedConditionDestinationNetworkGroup_Type()
)
alaQoSAppliedConditionDestinationNetworkGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationNetworkGroup.setStatus("current")


class _AlaQoSAppliedConditionDestinationNetworkGroupStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationNetworkGroupStatus based on Integer32"""
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


_AlaQoSAppliedConditionDestinationNetworkGroupStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationNetworkGroupStatus_Object = MibTableColumn
alaQoSAppliedConditionDestinationNetworkGroupStatus = _AlaQoSAppliedConditionDestinationNetworkGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 38),
    _AlaQoSAppliedConditionDestinationNetworkGroupStatus_Type()
)
alaQoSAppliedConditionDestinationNetworkGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationNetworkGroupStatus.setStatus("current")
_AlaQoSAppliedConditionMulticastIpAddr_Type = IpAddress
_AlaQoSAppliedConditionMulticastIpAddr_Object = MibTableColumn
alaQoSAppliedConditionMulticastIpAddr = _AlaQoSAppliedConditionMulticastIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 39),
    _AlaQoSAppliedConditionMulticastIpAddr_Type()
)
alaQoSAppliedConditionMulticastIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionMulticastIpAddr.setStatus("current")


class _AlaQoSAppliedConditionMulticastIpAddrStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionMulticastIpAddrStatus based on Integer32"""
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


_AlaQoSAppliedConditionMulticastIpAddrStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionMulticastIpAddrStatus_Object = MibTableColumn
alaQoSAppliedConditionMulticastIpAddrStatus = _AlaQoSAppliedConditionMulticastIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 40),
    _AlaQoSAppliedConditionMulticastIpAddrStatus_Type()
)
alaQoSAppliedConditionMulticastIpAddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionMulticastIpAddrStatus.setStatus("current")
_AlaQoSAppliedConditionMulticastIpMask_Type = IpAddress
_AlaQoSAppliedConditionMulticastIpMask_Object = MibTableColumn
alaQoSAppliedConditionMulticastIpMask = _AlaQoSAppliedConditionMulticastIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 41),
    _AlaQoSAppliedConditionMulticastIpMask_Type()
)
alaQoSAppliedConditionMulticastIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionMulticastIpMask.setStatus("current")


class _AlaQoSAppliedConditionMulticastNetworkGroup_Type(SnmpAdminString):
    """Custom type alaQoSAppliedConditionMulticastNetworkGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedConditionMulticastNetworkGroup_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedConditionMulticastNetworkGroup_Object = MibTableColumn
alaQoSAppliedConditionMulticastNetworkGroup = _AlaQoSAppliedConditionMulticastNetworkGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 42),
    _AlaQoSAppliedConditionMulticastNetworkGroup_Type()
)
alaQoSAppliedConditionMulticastNetworkGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionMulticastNetworkGroup.setStatus("current")


class _AlaQoSAppliedConditionMulticastNetworkGroupStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionMulticastNetworkGroupStatus based on Integer32"""
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


_AlaQoSAppliedConditionMulticastNetworkGroupStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionMulticastNetworkGroupStatus_Object = MibTableColumn
alaQoSAppliedConditionMulticastNetworkGroupStatus = _AlaQoSAppliedConditionMulticastNetworkGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 43),
    _AlaQoSAppliedConditionMulticastNetworkGroupStatus_Type()
)
alaQoSAppliedConditionMulticastNetworkGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionMulticastNetworkGroupStatus.setStatus("current")


class _AlaQoSAppliedConditionTos_Type(Integer32):
    """Custom type alaQoSAppliedConditionTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSAppliedConditionTos_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionTos_Object = MibTableColumn
alaQoSAppliedConditionTos = _AlaQoSAppliedConditionTos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 44),
    _AlaQoSAppliedConditionTos_Type()
)
alaQoSAppliedConditionTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionTos.setStatus("current")


class _AlaQoSAppliedConditionTosStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionTosStatus based on Integer32"""
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


_AlaQoSAppliedConditionTosStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionTosStatus_Object = MibTableColumn
alaQoSAppliedConditionTosStatus = _AlaQoSAppliedConditionTosStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 45),
    _AlaQoSAppliedConditionTosStatus_Type()
)
alaQoSAppliedConditionTosStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionTosStatus.setStatus("current")


class _AlaQoSAppliedConditionTosMask_Type(Integer32):
    """Custom type alaQoSAppliedConditionTosMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSAppliedConditionTosMask_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionTosMask_Object = MibTableColumn
alaQoSAppliedConditionTosMask = _AlaQoSAppliedConditionTosMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 46),
    _AlaQoSAppliedConditionTosMask_Type()
)
alaQoSAppliedConditionTosMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionTosMask.setStatus("current")


class _AlaQoSAppliedConditionDscp_Type(Integer32):
    """Custom type alaQoSAppliedConditionDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSAppliedConditionDscp_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDscp_Object = MibTableColumn
alaQoSAppliedConditionDscp = _AlaQoSAppliedConditionDscp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 47),
    _AlaQoSAppliedConditionDscp_Type()
)
alaQoSAppliedConditionDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDscp.setStatus("current")


class _AlaQoSAppliedConditionDscpStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionDscpStatus based on Integer32"""
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


_AlaQoSAppliedConditionDscpStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDscpStatus_Object = MibTableColumn
alaQoSAppliedConditionDscpStatus = _AlaQoSAppliedConditionDscpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 48),
    _AlaQoSAppliedConditionDscpStatus_Type()
)
alaQoSAppliedConditionDscpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDscpStatus.setStatus("current")


class _AlaQoSAppliedConditionDscpMask_Type(Integer32):
    """Custom type alaQoSAppliedConditionDscpMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSAppliedConditionDscpMask_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDscpMask_Object = MibTableColumn
alaQoSAppliedConditionDscpMask = _AlaQoSAppliedConditionDscpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 49),
    _AlaQoSAppliedConditionDscpMask_Type()
)
alaQoSAppliedConditionDscpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDscpMask.setStatus("current")


class _AlaQoSAppliedConditionIpProtocol_Type(Integer32):
    """Custom type alaQoSAppliedConditionIpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSAppliedConditionIpProtocol_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionIpProtocol_Object = MibTableColumn
alaQoSAppliedConditionIpProtocol = _AlaQoSAppliedConditionIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 50),
    _AlaQoSAppliedConditionIpProtocol_Type()
)
alaQoSAppliedConditionIpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionIpProtocol.setStatus("current")


class _AlaQoSAppliedConditionIpProtocolStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionIpProtocolStatus based on Integer32"""
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


_AlaQoSAppliedConditionIpProtocolStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionIpProtocolStatus_Object = MibTableColumn
alaQoSAppliedConditionIpProtocolStatus = _AlaQoSAppliedConditionIpProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 51),
    _AlaQoSAppliedConditionIpProtocolStatus_Type()
)
alaQoSAppliedConditionIpProtocolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionIpProtocolStatus.setStatus("current")


class _AlaQoSAppliedConditionSourceIpPort_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedConditionSourceIpPort_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceIpPort_Object = MibTableColumn
alaQoSAppliedConditionSourceIpPort = _AlaQoSAppliedConditionSourceIpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 52),
    _AlaQoSAppliedConditionSourceIpPort_Type()
)
alaQoSAppliedConditionSourceIpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceIpPort.setStatus("current")


class _AlaQoSAppliedConditionSourceIpPortStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceIpPortStatus based on Integer32"""
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


_AlaQoSAppliedConditionSourceIpPortStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceIpPortStatus_Object = MibTableColumn
alaQoSAppliedConditionSourceIpPortStatus = _AlaQoSAppliedConditionSourceIpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 53),
    _AlaQoSAppliedConditionSourceIpPortStatus_Type()
)
alaQoSAppliedConditionSourceIpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceIpPortStatus.setStatus("current")


class _AlaQoSAppliedConditionDestinationIpPort_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedConditionDestinationIpPort_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationIpPort_Object = MibTableColumn
alaQoSAppliedConditionDestinationIpPort = _AlaQoSAppliedConditionDestinationIpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 54),
    _AlaQoSAppliedConditionDestinationIpPort_Type()
)
alaQoSAppliedConditionDestinationIpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationIpPort.setStatus("current")


class _AlaQoSAppliedConditionDestinationIpPortStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationIpPortStatus based on Integer32"""
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


_AlaQoSAppliedConditionDestinationIpPortStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationIpPortStatus_Object = MibTableColumn
alaQoSAppliedConditionDestinationIpPortStatus = _AlaQoSAppliedConditionDestinationIpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 55),
    _AlaQoSAppliedConditionDestinationIpPortStatus_Type()
)
alaQoSAppliedConditionDestinationIpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationIpPortStatus.setStatus("current")


class _AlaQoSAppliedConditionService_Type(SnmpAdminString):
    """Custom type alaQoSAppliedConditionService based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedConditionService_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedConditionService_Object = MibTableColumn
alaQoSAppliedConditionService = _AlaQoSAppliedConditionService_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 56),
    _AlaQoSAppliedConditionService_Type()
)
alaQoSAppliedConditionService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionService.setStatus("current")


class _AlaQoSAppliedConditionServiceStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionServiceStatus based on Integer32"""
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


_AlaQoSAppliedConditionServiceStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionServiceStatus_Object = MibTableColumn
alaQoSAppliedConditionServiceStatus = _AlaQoSAppliedConditionServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 57),
    _AlaQoSAppliedConditionServiceStatus_Type()
)
alaQoSAppliedConditionServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionServiceStatus.setStatus("current")


class _AlaQoSAppliedConditionServiceGroup_Type(SnmpAdminString):
    """Custom type alaQoSAppliedConditionServiceGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedConditionServiceGroup_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedConditionServiceGroup_Object = MibTableColumn
alaQoSAppliedConditionServiceGroup = _AlaQoSAppliedConditionServiceGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 58),
    _AlaQoSAppliedConditionServiceGroup_Type()
)
alaQoSAppliedConditionServiceGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionServiceGroup.setStatus("current")


class _AlaQoSAppliedConditionServiceGroupStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionServiceGroupStatus based on Integer32"""
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


_AlaQoSAppliedConditionServiceGroupStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionServiceGroupStatus_Object = MibTableColumn
alaQoSAppliedConditionServiceGroupStatus = _AlaQoSAppliedConditionServiceGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 59),
    _AlaQoSAppliedConditionServiceGroupStatus_Type()
)
alaQoSAppliedConditionServiceGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionServiceGroupStatus.setStatus("current")


class _AlaQoSAppliedConditionIcmpType_Type(Integer32):
    """Custom type alaQoSAppliedConditionIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSAppliedConditionIcmpType_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionIcmpType_Object = MibTableColumn
alaQoSAppliedConditionIcmpType = _AlaQoSAppliedConditionIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 60),
    _AlaQoSAppliedConditionIcmpType_Type()
)
alaQoSAppliedConditionIcmpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionIcmpType.setStatus("current")


class _AlaQoSAppliedConditionIcmpTypeStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionIcmpTypeStatus based on Integer32"""
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


_AlaQoSAppliedConditionIcmpTypeStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionIcmpTypeStatus_Object = MibTableColumn
alaQoSAppliedConditionIcmpTypeStatus = _AlaQoSAppliedConditionIcmpTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 61),
    _AlaQoSAppliedConditionIcmpTypeStatus_Type()
)
alaQoSAppliedConditionIcmpTypeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionIcmpTypeStatus.setStatus("current")


class _AlaQoSAppliedConditionIcmpCode_Type(Integer32):
    """Custom type alaQoSAppliedConditionIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSAppliedConditionIcmpCode_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionIcmpCode_Object = MibTableColumn
alaQoSAppliedConditionIcmpCode = _AlaQoSAppliedConditionIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 62),
    _AlaQoSAppliedConditionIcmpCode_Type()
)
alaQoSAppliedConditionIcmpCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionIcmpCode.setStatus("current")


class _AlaQoSAppliedConditionIcmpCodeStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionIcmpCodeStatus based on Integer32"""
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


_AlaQoSAppliedConditionIcmpCodeStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionIcmpCodeStatus_Object = MibTableColumn
alaQoSAppliedConditionIcmpCodeStatus = _AlaQoSAppliedConditionIcmpCodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 63),
    _AlaQoSAppliedConditionIcmpCodeStatus_Type()
)
alaQoSAppliedConditionIcmpCodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionIcmpCodeStatus.setStatus("current")
_AlaQoSAppliedConditionRowStatus_Type = RowStatus
_AlaQoSAppliedConditionRowStatus_Object = MibTableColumn
alaQoSAppliedConditionRowStatus = _AlaQoSAppliedConditionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 64),
    _AlaQoSAppliedConditionRowStatus_Type()
)
alaQoSAppliedConditionRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionRowStatus.setStatus("current")


class _AlaQoSAppliedConditionSourcePortEnd_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourcePortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_AlaQoSAppliedConditionSourcePortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourcePortEnd_Object = MibTableColumn
alaQoSAppliedConditionSourcePortEnd = _AlaQoSAppliedConditionSourcePortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 65),
    _AlaQoSAppliedConditionSourcePortEnd_Type()
)
alaQoSAppliedConditionSourcePortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourcePortEnd.setStatus("current")


class _AlaQoSAppliedConditionDestinationPortEnd_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_AlaQoSAppliedConditionDestinationPortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationPortEnd_Object = MibTableColumn
alaQoSAppliedConditionDestinationPortEnd = _AlaQoSAppliedConditionDestinationPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 66),
    _AlaQoSAppliedConditionDestinationPortEnd_Type()
)
alaQoSAppliedConditionDestinationPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationPortEnd.setStatus("current")


class _AlaQoSAppliedConditionSourceIpPortEnd_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceIpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedConditionSourceIpPortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceIpPortEnd_Object = MibTableColumn
alaQoSAppliedConditionSourceIpPortEnd = _AlaQoSAppliedConditionSourceIpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 67),
    _AlaQoSAppliedConditionSourceIpPortEnd_Type()
)
alaQoSAppliedConditionSourceIpPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceIpPortEnd.setStatus("current")


class _AlaQoSAppliedConditionDestinationIpPortEnd_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationIpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedConditionDestinationIpPortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationIpPortEnd_Object = MibTableColumn
alaQoSAppliedConditionDestinationIpPortEnd = _AlaQoSAppliedConditionDestinationIpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 68),
    _AlaQoSAppliedConditionDestinationIpPortEnd_Type()
)
alaQoSAppliedConditionDestinationIpPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationIpPortEnd.setStatus("current")


class _AlaQoSAppliedConditionSourceTcpPort_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedConditionSourceTcpPort_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceTcpPort_Object = MibTableColumn
alaQoSAppliedConditionSourceTcpPort = _AlaQoSAppliedConditionSourceTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 69),
    _AlaQoSAppliedConditionSourceTcpPort_Type()
)
alaQoSAppliedConditionSourceTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceTcpPort.setStatus("current")


class _AlaQoSAppliedConditionSourceTcpPortStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceTcpPortStatus based on Integer32"""
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


_AlaQoSAppliedConditionSourceTcpPortStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceTcpPortStatus_Object = MibTableColumn
alaQoSAppliedConditionSourceTcpPortStatus = _AlaQoSAppliedConditionSourceTcpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 70),
    _AlaQoSAppliedConditionSourceTcpPortStatus_Type()
)
alaQoSAppliedConditionSourceTcpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceTcpPortStatus.setStatus("current")


class _AlaQoSAppliedConditionSourceTcpPortEnd_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceTcpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedConditionSourceTcpPortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceTcpPortEnd_Object = MibTableColumn
alaQoSAppliedConditionSourceTcpPortEnd = _AlaQoSAppliedConditionSourceTcpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 71),
    _AlaQoSAppliedConditionSourceTcpPortEnd_Type()
)
alaQoSAppliedConditionSourceTcpPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceTcpPortEnd.setStatus("current")


class _AlaQoSAppliedConditionDestinationTcpPort_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedConditionDestinationTcpPort_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationTcpPort_Object = MibTableColumn
alaQoSAppliedConditionDestinationTcpPort = _AlaQoSAppliedConditionDestinationTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 72),
    _AlaQoSAppliedConditionDestinationTcpPort_Type()
)
alaQoSAppliedConditionDestinationTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationTcpPort.setStatus("current")


class _AlaQoSAppliedConditionDestinationTcpPortStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationTcpPortStatus based on Integer32"""
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


_AlaQoSAppliedConditionDestinationTcpPortStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationTcpPortStatus_Object = MibTableColumn
alaQoSAppliedConditionDestinationTcpPortStatus = _AlaQoSAppliedConditionDestinationTcpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 73),
    _AlaQoSAppliedConditionDestinationTcpPortStatus_Type()
)
alaQoSAppliedConditionDestinationTcpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationTcpPortStatus.setStatus("current")


class _AlaQoSAppliedConditionDestinationTcpPortEnd_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationTcpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedConditionDestinationTcpPortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationTcpPortEnd_Object = MibTableColumn
alaQoSAppliedConditionDestinationTcpPortEnd = _AlaQoSAppliedConditionDestinationTcpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 74),
    _AlaQoSAppliedConditionDestinationTcpPortEnd_Type()
)
alaQoSAppliedConditionDestinationTcpPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationTcpPortEnd.setStatus("current")


class _AlaQoSAppliedConditionSourceUdpPort_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedConditionSourceUdpPort_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceUdpPort_Object = MibTableColumn
alaQoSAppliedConditionSourceUdpPort = _AlaQoSAppliedConditionSourceUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 75),
    _AlaQoSAppliedConditionSourceUdpPort_Type()
)
alaQoSAppliedConditionSourceUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceUdpPort.setStatus("current")


class _AlaQoSAppliedConditionSourceUdpPortStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceUdpPortStatus based on Integer32"""
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


_AlaQoSAppliedConditionSourceUdpPortStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceUdpPortStatus_Object = MibTableColumn
alaQoSAppliedConditionSourceUdpPortStatus = _AlaQoSAppliedConditionSourceUdpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 76),
    _AlaQoSAppliedConditionSourceUdpPortStatus_Type()
)
alaQoSAppliedConditionSourceUdpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceUdpPortStatus.setStatus("current")


class _AlaQoSAppliedConditionSourceUdpPortEnd_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceUdpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedConditionSourceUdpPortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceUdpPortEnd_Object = MibTableColumn
alaQoSAppliedConditionSourceUdpPortEnd = _AlaQoSAppliedConditionSourceUdpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 77),
    _AlaQoSAppliedConditionSourceUdpPortEnd_Type()
)
alaQoSAppliedConditionSourceUdpPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceUdpPortEnd.setStatus("current")


class _AlaQoSAppliedConditionDestinationUdpPort_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedConditionDestinationUdpPort_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationUdpPort_Object = MibTableColumn
alaQoSAppliedConditionDestinationUdpPort = _AlaQoSAppliedConditionDestinationUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 78),
    _AlaQoSAppliedConditionDestinationUdpPort_Type()
)
alaQoSAppliedConditionDestinationUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationUdpPort.setStatus("current")


class _AlaQoSAppliedConditionDestinationUdpPortStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationUdpPortStatus based on Integer32"""
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


_AlaQoSAppliedConditionDestinationUdpPortStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationUdpPortStatus_Object = MibTableColumn
alaQoSAppliedConditionDestinationUdpPortStatus = _AlaQoSAppliedConditionDestinationUdpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 79),
    _AlaQoSAppliedConditionDestinationUdpPortStatus_Type()
)
alaQoSAppliedConditionDestinationUdpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationUdpPortStatus.setStatus("current")


class _AlaQoSAppliedConditionDestinationUdpPortEnd_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationUdpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedConditionDestinationUdpPortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationUdpPortEnd_Object = MibTableColumn
alaQoSAppliedConditionDestinationUdpPortEnd = _AlaQoSAppliedConditionDestinationUdpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 80),
    _AlaQoSAppliedConditionDestinationUdpPortEnd_Type()
)
alaQoSAppliedConditionDestinationUdpPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationUdpPortEnd.setStatus("current")


class _AlaQoSAppliedConditionEthertype_Type(Integer32):
    """Custom type alaQoSAppliedConditionEthertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedConditionEthertype_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionEthertype_Object = MibTableColumn
alaQoSAppliedConditionEthertype = _AlaQoSAppliedConditionEthertype_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 81),
    _AlaQoSAppliedConditionEthertype_Type()
)
alaQoSAppliedConditionEthertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionEthertype.setStatus("current")


class _AlaQoSAppliedConditionEthertypeStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionEthertypeStatus based on Integer32"""
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


_AlaQoSAppliedConditionEthertypeStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionEthertypeStatus_Object = MibTableColumn
alaQoSAppliedConditionEthertypeStatus = _AlaQoSAppliedConditionEthertypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 82),
    _AlaQoSAppliedConditionEthertypeStatus_Type()
)
alaQoSAppliedConditionEthertypeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionEthertypeStatus.setStatus("current")


class _AlaQoSAppliedConditionTcpFlags_Type(Integer32):
    """Custom type alaQoSAppliedConditionTcpFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("any", 2))
    )


_AlaQoSAppliedConditionTcpFlags_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionTcpFlags_Object = MibTableColumn
alaQoSAppliedConditionTcpFlags = _AlaQoSAppliedConditionTcpFlags_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 83),
    _AlaQoSAppliedConditionTcpFlags_Type()
)
alaQoSAppliedConditionTcpFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionTcpFlags.setStatus("current")


class _AlaQoSAppliedConditionTcpFlagsStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionTcpFlagsStatus based on Integer32"""
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


_AlaQoSAppliedConditionTcpFlagsStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionTcpFlagsStatus_Object = MibTableColumn
alaQoSAppliedConditionTcpFlagsStatus = _AlaQoSAppliedConditionTcpFlagsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 84),
    _AlaQoSAppliedConditionTcpFlagsStatus_Type()
)
alaQoSAppliedConditionTcpFlagsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionTcpFlagsStatus.setStatus("current")
_AlaQoSAppliedConditionTcpFlagsVal_Type = Integer32
_AlaQoSAppliedConditionTcpFlagsVal_Object = MibTableColumn
alaQoSAppliedConditionTcpFlagsVal = _AlaQoSAppliedConditionTcpFlagsVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 85),
    _AlaQoSAppliedConditionTcpFlagsVal_Type()
)
alaQoSAppliedConditionTcpFlagsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionTcpFlagsVal.setStatus("current")


class _AlaQoSAppliedConditionTcpFlagsValStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionTcpFlagsValStatus based on Integer32"""
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


_AlaQoSAppliedConditionTcpFlagsValStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionTcpFlagsValStatus_Object = MibTableColumn
alaQoSAppliedConditionTcpFlagsValStatus = _AlaQoSAppliedConditionTcpFlagsValStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 86),
    _AlaQoSAppliedConditionTcpFlagsValStatus_Type()
)
alaQoSAppliedConditionTcpFlagsValStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionTcpFlagsValStatus.setStatus("current")
_AlaQoSAppliedConditionTcpFlagsMask_Type = Integer32
_AlaQoSAppliedConditionTcpFlagsMask_Object = MibTableColumn
alaQoSAppliedConditionTcpFlagsMask = _AlaQoSAppliedConditionTcpFlagsMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 87),
    _AlaQoSAppliedConditionTcpFlagsMask_Type()
)
alaQoSAppliedConditionTcpFlagsMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionTcpFlagsMask.setStatus("current")


class _AlaQoSAppliedConditionTcpFlagsMaskStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionTcpFlagsMaskStatus based on Integer32"""
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


_AlaQoSAppliedConditionTcpFlagsMaskStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionTcpFlagsMaskStatus_Object = MibTableColumn
alaQoSAppliedConditionTcpFlagsMaskStatus = _AlaQoSAppliedConditionTcpFlagsMaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 88),
    _AlaQoSAppliedConditionTcpFlagsMaskStatus_Type()
)
alaQoSAppliedConditionTcpFlagsMaskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionTcpFlagsMaskStatus.setStatus("current")


class _AlaQoSAppliedConditionTcpEstablished_Type(Integer32):
    """Custom type alaQoSAppliedConditionTcpEstablished based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSAppliedConditionTcpEstablished_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionTcpEstablished_Object = MibTableColumn
alaQoSAppliedConditionTcpEstablished = _AlaQoSAppliedConditionTcpEstablished_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 89),
    _AlaQoSAppliedConditionTcpEstablished_Type()
)
alaQoSAppliedConditionTcpEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionTcpEstablished.setStatus("current")
_AlaQoSAppliedConditionSourceIpv6Addr_Type = Ipv6Address
_AlaQoSAppliedConditionSourceIpv6Addr_Object = MibTableColumn
alaQoSAppliedConditionSourceIpv6Addr = _AlaQoSAppliedConditionSourceIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 90),
    _AlaQoSAppliedConditionSourceIpv6Addr_Type()
)
alaQoSAppliedConditionSourceIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceIpv6Addr.setStatus("current")


class _AlaQoSAppliedConditionSourceIpv6AddrStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceIpv6AddrStatus based on Integer32"""
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


_AlaQoSAppliedConditionSourceIpv6AddrStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceIpv6AddrStatus_Object = MibTableColumn
alaQoSAppliedConditionSourceIpv6AddrStatus = _AlaQoSAppliedConditionSourceIpv6AddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 91),
    _AlaQoSAppliedConditionSourceIpv6AddrStatus_Type()
)
alaQoSAppliedConditionSourceIpv6AddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceIpv6AddrStatus.setStatus("current")
_AlaQoSAppliedConditionSourceIpv6Mask_Type = Ipv6Address
_AlaQoSAppliedConditionSourceIpv6Mask_Object = MibTableColumn
alaQoSAppliedConditionSourceIpv6Mask = _AlaQoSAppliedConditionSourceIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 92),
    _AlaQoSAppliedConditionSourceIpv6Mask_Type()
)
alaQoSAppliedConditionSourceIpv6Mask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceIpv6Mask.setStatus("current")
_AlaQoSAppliedConditionDestinationIpv6Addr_Type = Ipv6Address
_AlaQoSAppliedConditionDestinationIpv6Addr_Object = MibTableColumn
alaQoSAppliedConditionDestinationIpv6Addr = _AlaQoSAppliedConditionDestinationIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 93),
    _AlaQoSAppliedConditionDestinationIpv6Addr_Type()
)
alaQoSAppliedConditionDestinationIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationIpv6Addr.setStatus("current")


class _AlaQoSAppliedConditionDestinationIpv6AddrStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationIpv6AddrStatus based on Integer32"""
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


_AlaQoSAppliedConditionDestinationIpv6AddrStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationIpv6AddrStatus_Object = MibTableColumn
alaQoSAppliedConditionDestinationIpv6AddrStatus = _AlaQoSAppliedConditionDestinationIpv6AddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 94),
    _AlaQoSAppliedConditionDestinationIpv6AddrStatus_Type()
)
alaQoSAppliedConditionDestinationIpv6AddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationIpv6AddrStatus.setStatus("current")
_AlaQoSAppliedConditionDestinationIpv6Mask_Type = Ipv6Address
_AlaQoSAppliedConditionDestinationIpv6Mask_Object = MibTableColumn
alaQoSAppliedConditionDestinationIpv6Mask = _AlaQoSAppliedConditionDestinationIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 95),
    _AlaQoSAppliedConditionDestinationIpv6Mask_Type()
)
alaQoSAppliedConditionDestinationIpv6Mask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationIpv6Mask.setStatus("current")


class _AlaQoSAppliedConditionIpv6Traffic_Type(Integer32):
    """Custom type alaQoSAppliedConditionIpv6Traffic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSAppliedConditionIpv6Traffic_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionIpv6Traffic_Object = MibTableColumn
alaQoSAppliedConditionIpv6Traffic = _AlaQoSAppliedConditionIpv6Traffic_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 96),
    _AlaQoSAppliedConditionIpv6Traffic_Type()
)
alaQoSAppliedConditionIpv6Traffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionIpv6Traffic.setStatus("current")


class _AlaQoSAppliedConditionIpv6NH_Type(Integer32):
    """Custom type alaQoSAppliedConditionIpv6NH based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSAppliedConditionIpv6NH_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionIpv6NH_Object = MibTableColumn
alaQoSAppliedConditionIpv6NH = _AlaQoSAppliedConditionIpv6NH_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 97),
    _AlaQoSAppliedConditionIpv6NH_Type()
)
alaQoSAppliedConditionIpv6NH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionIpv6NH.setStatus("current")


class _AlaQoSAppliedConditionIpv6NHStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionIpv6NHStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSAppliedConditionIpv6NHStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionIpv6NHStatus_Object = MibTableColumn
alaQoSAppliedConditionIpv6NHStatus = _AlaQoSAppliedConditionIpv6NHStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 98),
    _AlaQoSAppliedConditionIpv6NHStatus_Type()
)
alaQoSAppliedConditionIpv6NHStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionIpv6NHStatus.setStatus("current")


class _AlaQoSAppliedConditionIpv6FlowLabel_Type(Integer32):
    """Custom type alaQoSAppliedConditionIpv6FlowLabel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_AlaQoSAppliedConditionIpv6FlowLabel_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionIpv6FlowLabel_Object = MibTableColumn
alaQoSAppliedConditionIpv6FlowLabel = _AlaQoSAppliedConditionIpv6FlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 99),
    _AlaQoSAppliedConditionIpv6FlowLabel_Type()
)
alaQoSAppliedConditionIpv6FlowLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionIpv6FlowLabel.setStatus("current")


class _AlaQoSAppliedConditionIpv6FlowLabelStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionIpv6FlowLabelStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSAppliedConditionIpv6FlowLabelStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionIpv6FlowLabelStatus_Object = MibTableColumn
alaQoSAppliedConditionIpv6FlowLabelStatus = _AlaQoSAppliedConditionIpv6FlowLabelStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 100),
    _AlaQoSAppliedConditionIpv6FlowLabelStatus_Type()
)
alaQoSAppliedConditionIpv6FlowLabelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionIpv6FlowLabelStatus.setStatus("current")


class _AlaQoSAppliedConditionMcastIpv6Addr_Type(Ipv6Address):
    """Custom type alaQoSAppliedConditionMcastIpv6Addr based on Ipv6Address"""
    defaultHexValue = "00000000000000000000000000000000"


_AlaQoSAppliedConditionMcastIpv6Addr_Type.__name__ = "Ipv6Address"
_AlaQoSAppliedConditionMcastIpv6Addr_Object = MibTableColumn
alaQoSAppliedConditionMcastIpv6Addr = _AlaQoSAppliedConditionMcastIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 101),
    _AlaQoSAppliedConditionMcastIpv6Addr_Type()
)
alaQoSAppliedConditionMcastIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionMcastIpv6Addr.setStatus("current")


class _AlaQoSAppliedConditionMcastIpv6AddrStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionMcastIpv6AddrStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSAppliedConditionMcastIpv6AddrStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionMcastIpv6AddrStatus_Object = MibTableColumn
alaQoSAppliedConditionMcastIpv6AddrStatus = _AlaQoSAppliedConditionMcastIpv6AddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 102),
    _AlaQoSAppliedConditionMcastIpv6AddrStatus_Type()
)
alaQoSAppliedConditionMcastIpv6AddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionMcastIpv6AddrStatus.setStatus("current")


class _AlaQoSAppliedConditionMcastIpv6Mask_Type(Ipv6Address):
    """Custom type alaQoSAppliedConditionMcastIpv6Mask based on Ipv6Address"""
    defaultHexValue = "ffffffffffffffffffffffffffffffff"


_AlaQoSAppliedConditionMcastIpv6Mask_Type.__name__ = "Ipv6Address"
_AlaQoSAppliedConditionMcastIpv6Mask_Object = MibTableColumn
alaQoSAppliedConditionMcastIpv6Mask = _AlaQoSAppliedConditionMcastIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 103),
    _AlaQoSAppliedConditionMcastIpv6Mask_Type()
)
alaQoSAppliedConditionMcastIpv6Mask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionMcastIpv6Mask.setStatus("current")


class _AlaQoSAppliedConditionDscpEnd_Type(Integer32):
    """Custom type alaQoSAppliedConditionDscpEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSAppliedConditionDscpEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDscpEnd_Object = MibTableColumn
alaQoSAppliedConditionDscpEnd = _AlaQoSAppliedConditionDscpEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 104),
    _AlaQoSAppliedConditionDscpEnd_Type()
)
alaQoSAppliedConditionDscpEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDscpEnd.setStatus("current")


class _AlaQoSAppliedConditionInnerSourceVlan_Type(Integer32):
    """Custom type alaQoSAppliedConditionInnerSourceVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSAppliedConditionInnerSourceVlan_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionInnerSourceVlan_Object = MibTableColumn
alaQoSAppliedConditionInnerSourceVlan = _AlaQoSAppliedConditionInnerSourceVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 105),
    _AlaQoSAppliedConditionInnerSourceVlan_Type()
)
alaQoSAppliedConditionInnerSourceVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionInnerSourceVlan.setStatus("current")


class _AlaQoSAppliedConditionInnerSourceVlanStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionInnerSourceVlanStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSAppliedConditionInnerSourceVlanStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionInnerSourceVlanStatus_Object = MibTableColumn
alaQoSAppliedConditionInnerSourceVlanStatus = _AlaQoSAppliedConditionInnerSourceVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 106),
    _AlaQoSAppliedConditionInnerSourceVlanStatus_Type()
)
alaQoSAppliedConditionInnerSourceVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionInnerSourceVlanStatus.setStatus("current")


class _AlaQoSAppliedConditionInner8021p_Type(Integer32):
    """Custom type alaQoSAppliedConditionInner8021p based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSAppliedConditionInner8021p_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionInner8021p_Object = MibTableColumn
alaQoSAppliedConditionInner8021p = _AlaQoSAppliedConditionInner8021p_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 107),
    _AlaQoSAppliedConditionInner8021p_Type()
)
alaQoSAppliedConditionInner8021p.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionInner8021p.setStatus("current")


class _AlaQoSAppliedConditionInner8021pStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionInner8021pStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSAppliedConditionInner8021pStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionInner8021pStatus_Object = MibTableColumn
alaQoSAppliedConditionInner8021pStatus = _AlaQoSAppliedConditionInner8021pStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 108),
    _AlaQoSAppliedConditionInner8021pStatus_Type()
)
alaQoSAppliedConditionInner8021pStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionInner8021pStatus.setStatus("current")


class _AlaQoSAppliedConditionVrfName_Type(SnmpAdminString):
    """Custom type alaQoSAppliedConditionVrfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedConditionVrfName_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedConditionVrfName_Object = MibTableColumn
alaQoSAppliedConditionVrfName = _AlaQoSAppliedConditionVrfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 109),
    _AlaQoSAppliedConditionVrfName_Type()
)
alaQoSAppliedConditionVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionVrfName.setStatus("current")


class _AlaQoSAppliedConditionVrfNameStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionVrfNameStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSAppliedConditionVrfNameStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionVrfNameStatus_Object = MibTableColumn
alaQoSAppliedConditionVrfNameStatus = _AlaQoSAppliedConditionVrfNameStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 110),
    _AlaQoSAppliedConditionVrfNameStatus_Type()
)
alaQoSAppliedConditionVrfNameStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionVrfNameStatus.setStatus("current")


class _AlaQoSAppliedConditionFragments_Type(Integer32):
    """Custom type alaQoSAppliedConditionFragments based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSAppliedConditionFragments_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionFragments_Object = MibTableColumn
alaQoSAppliedConditionFragments = _AlaQoSAppliedConditionFragments_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 111),
    _AlaQoSAppliedConditionFragments_Type()
)
alaQoSAppliedConditionFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionFragments.setStatus("current")


class _AlaQoSAppliedConditionSourceChassis_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSAppliedConditionSourceChassis_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceChassis_Object = MibTableColumn
alaQoSAppliedConditionSourceChassis = _AlaQoSAppliedConditionSourceChassis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 112),
    _AlaQoSAppliedConditionSourceChassis_Type()
)
alaQoSAppliedConditionSourceChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceChassis.setStatus("current")


class _AlaQoSAppliedConditionDestinationChassis_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSAppliedConditionDestinationChassis_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationChassis_Object = MibTableColumn
alaQoSAppliedConditionDestinationChassis = _AlaQoSAppliedConditionDestinationChassis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 113),
    _AlaQoSAppliedConditionDestinationChassis_Type()
)
alaQoSAppliedConditionDestinationChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationChassis.setStatus("current")


class _AlaQoSAppliedConditionAppFpGroup_Type(SnmpAdminString):
    """Custom type alaQoSAppliedConditionAppFpGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_AlaQoSAppliedConditionAppFpGroup_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedConditionAppFpGroup_Object = MibTableColumn
alaQoSAppliedConditionAppFpGroup = _AlaQoSAppliedConditionAppFpGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 114),
    _AlaQoSAppliedConditionAppFpGroup_Type()
)
alaQoSAppliedConditionAppFpGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionAppFpGroup.setStatus("current")


class _AlaQoSAppliedConditionAppFpGroupStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionAppFpGroupStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSAppliedConditionAppFpGroupStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionAppFpGroupStatus_Object = MibTableColumn
alaQoSAppliedConditionAppFpGroupStatus = _AlaQoSAppliedConditionAppFpGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 115),
    _AlaQoSAppliedConditionAppFpGroupStatus_Type()
)
alaQoSAppliedConditionAppFpGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionAppFpGroupStatus.setStatus("current")


class _AlaQoSAppliedConditionSIP_Type(Integer32):
    """Custom type alaQoSAppliedConditionSIP based on Integer32"""
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
        *(("audio", 1),
          ("video", 2),
          ("other", 3))
    )


_AlaQoSAppliedConditionSIP_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSIP_Object = MibTableColumn
alaQoSAppliedConditionSIP = _AlaQoSAppliedConditionSIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 116),
    _AlaQoSAppliedConditionSIP_Type()
)
alaQoSAppliedConditionSIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSIP.setStatus("current")


class _AlaQoSAppliedConditionSIPStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionSIPStatus based on Integer32"""
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


_AlaQoSAppliedConditionSIPStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSIPStatus_Object = MibTableColumn
alaQoSAppliedConditionSIPStatus = _AlaQoSAppliedConditionSIPStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 117),
    _AlaQoSAppliedConditionSIPStatus_Type()
)
alaQoSAppliedConditionSIPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSIPStatus.setStatus("current")


class _AlaQoSAppliedConditionDPIAppName_Type(SnmpAdminString):
    """Custom type alaQoSAppliedConditionDPIAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaQoSAppliedConditionDPIAppName_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedConditionDPIAppName_Object = MibTableColumn
alaQoSAppliedConditionDPIAppName = _AlaQoSAppliedConditionDPIAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 118),
    _AlaQoSAppliedConditionDPIAppName_Type()
)
alaQoSAppliedConditionDPIAppName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDPIAppName.setStatus("current")


class _AlaQoSAppliedConditionDPIAppGrp_Type(SnmpAdminString):
    """Custom type alaQoSAppliedConditionDPIAppGrp based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaQoSAppliedConditionDPIAppGrp_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedConditionDPIAppGrp_Object = MibTableColumn
alaQoSAppliedConditionDPIAppGrp = _AlaQoSAppliedConditionDPIAppGrp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 119),
    _AlaQoSAppliedConditionDPIAppGrp_Type()
)
alaQoSAppliedConditionDPIAppGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDPIAppGrp.setStatus("current")


class _AlaQoSAppliedConditionDPIAppNameStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionDPIAppNameStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSAppliedConditionDPIAppNameStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDPIAppNameStatus_Object = MibTableColumn
alaQoSAppliedConditionDPIAppNameStatus = _AlaQoSAppliedConditionDPIAppNameStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 120),
    _AlaQoSAppliedConditionDPIAppNameStatus_Type()
)
alaQoSAppliedConditionDPIAppNameStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDPIAppNameStatus.setStatus("current")


class _AlaQoSAppliedConditionDPIAppGroupStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionDPIAppGroupStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSAppliedConditionDPIAppGroupStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDPIAppGroupStatus_Object = MibTableColumn
alaQoSAppliedConditionDPIAppGroupStatus = _AlaQoSAppliedConditionDPIAppGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 121),
    _AlaQoSAppliedConditionDPIAppGroupStatus_Type()
)
alaQoSAppliedConditionDPIAppGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDPIAppGroupStatus.setStatus("current")
_AlaQoSAppliedConditionVxlanVni_Type = Integer32
_AlaQoSAppliedConditionVxlanVni_Object = MibTableColumn
alaQoSAppliedConditionVxlanVni = _AlaQoSAppliedConditionVxlanVni_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 122),
    _AlaQoSAppliedConditionVxlanVni_Type()
)
alaQoSAppliedConditionVxlanVni.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionVxlanVni.setStatus("current")


class _AlaQoSAppliedConditionVxlanVniStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionVxlanVniStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSAppliedConditionVxlanVniStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionVxlanVniStatus_Object = MibTableColumn
alaQoSAppliedConditionVxlanVniStatus = _AlaQoSAppliedConditionVxlanVniStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 123),
    _AlaQoSAppliedConditionVxlanVniStatus_Type()
)
alaQoSAppliedConditionVxlanVniStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionVxlanVniStatus.setStatus("current")
_AlaQoSAppliedConditionVxlanPort_Type = Integer32
_AlaQoSAppliedConditionVxlanPort_Object = MibTableColumn
alaQoSAppliedConditionVxlanPort = _AlaQoSAppliedConditionVxlanPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 124),
    _AlaQoSAppliedConditionVxlanPort_Type()
)
alaQoSAppliedConditionVxlanPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionVxlanPort.setStatus("current")


class _AlaQoSAppliedConditionVxlanPortStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionVxlanPortStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSAppliedConditionVxlanPortStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionVxlanPortStatus_Object = MibTableColumn
alaQoSAppliedConditionVxlanPortStatus = _AlaQoSAppliedConditionVxlanPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 125),
    _AlaQoSAppliedConditionVxlanPortStatus_Type()
)
alaQoSAppliedConditionVxlanPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionVxlanPortStatus.setStatus("current")


class _AlaQoSAppliedConditionVmSourceMacAddr_Type(MacAddress):
    """Custom type alaQoSAppliedConditionVmSourceMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_AlaQoSAppliedConditionVmSourceMacAddr_Type.__name__ = "MacAddress"
_AlaQoSAppliedConditionVmSourceMacAddr_Object = MibTableColumn
alaQoSAppliedConditionVmSourceMacAddr = _AlaQoSAppliedConditionVmSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 126),
    _AlaQoSAppliedConditionVmSourceMacAddr_Type()
)
alaQoSAppliedConditionVmSourceMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionVmSourceMacAddr.setStatus("current")


class _AlaQoSAppliedConditionVmSourceMacAddrStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionVmSourceMacAddrStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSAppliedConditionVmSourceMacAddrStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionVmSourceMacAddrStatus_Object = MibTableColumn
alaQoSAppliedConditionVmSourceMacAddrStatus = _AlaQoSAppliedConditionVmSourceMacAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 127),
    _AlaQoSAppliedConditionVmSourceMacAddrStatus_Type()
)
alaQoSAppliedConditionVmSourceMacAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionVmSourceMacAddrStatus.setStatus("current")


class _AlaQoSAppliedConditionVmSourceMacMask_Type(MacAddress):
    """Custom type alaQoSAppliedConditionVmSourceMacMask based on MacAddress"""
    defaultHexValue = "000000000000"


_AlaQoSAppliedConditionVmSourceMacMask_Type.__name__ = "MacAddress"
_AlaQoSAppliedConditionVmSourceMacMask_Object = MibTableColumn
alaQoSAppliedConditionVmSourceMacMask = _AlaQoSAppliedConditionVmSourceMacMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 128),
    _AlaQoSAppliedConditionVmSourceMacMask_Type()
)
alaQoSAppliedConditionVmSourceMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionVmSourceMacMask.setStatus("current")


class _AlaQoSAppliedConditionVmSourceIpAddr_Type(IpAddress):
    """Custom type alaQoSAppliedConditionVmSourceIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AlaQoSAppliedConditionVmSourceIpAddr_Type.__name__ = "IpAddress"
_AlaQoSAppliedConditionVmSourceIpAddr_Object = MibTableColumn
alaQoSAppliedConditionVmSourceIpAddr = _AlaQoSAppliedConditionVmSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 129),
    _AlaQoSAppliedConditionVmSourceIpAddr_Type()
)
alaQoSAppliedConditionVmSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionVmSourceIpAddr.setStatus("current")


class _AlaQoSAppliedConditionVmSourceIpAddrStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionVmSourceIpAddrStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSAppliedConditionVmSourceIpAddrStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionVmSourceIpAddrStatus_Object = MibTableColumn
alaQoSAppliedConditionVmSourceIpAddrStatus = _AlaQoSAppliedConditionVmSourceIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 130),
    _AlaQoSAppliedConditionVmSourceIpAddrStatus_Type()
)
alaQoSAppliedConditionVmSourceIpAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionVmSourceIpAddrStatus.setStatus("current")


class _AlaQoSAppliedConditionVmSourceIpMask_Type(IpAddress):
    """Custom type alaQoSAppliedConditionVmSourceIpMask based on IpAddress"""
    defaultHexValue = "ffffffff"


_AlaQoSAppliedConditionVmSourceIpMask_Type.__name__ = "IpAddress"
_AlaQoSAppliedConditionVmSourceIpMask_Object = MibTableColumn
alaQoSAppliedConditionVmSourceIpMask = _AlaQoSAppliedConditionVmSourceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 131),
    _AlaQoSAppliedConditionVmSourceIpMask_Type()
)
alaQoSAppliedConditionVmSourceIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionVmSourceIpMask.setStatus("current")


class _AlaQoSAppliedConditionVmSourceIpv6IpAddr_Type(Ipv6Address):
    """Custom type alaQoSAppliedConditionVmSourceIpv6IpAddr based on Ipv6Address"""
    defaultHexValue = "00000000000000000000000000000000"


_AlaQoSAppliedConditionVmSourceIpv6IpAddr_Type.__name__ = "Ipv6Address"
_AlaQoSAppliedConditionVmSourceIpv6IpAddr_Object = MibTableColumn
alaQoSAppliedConditionVmSourceIpv6IpAddr = _AlaQoSAppliedConditionVmSourceIpv6IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 132),
    _AlaQoSAppliedConditionVmSourceIpv6IpAddr_Type()
)
alaQoSAppliedConditionVmSourceIpv6IpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionVmSourceIpv6IpAddr.setStatus("current")


class _AlaQoSAppliedConditionVmSourceIpv6IpAddrStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionVmSourceIpv6IpAddrStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSAppliedConditionVmSourceIpv6IpAddrStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionVmSourceIpv6IpAddrStatus_Object = MibTableColumn
alaQoSAppliedConditionVmSourceIpv6IpAddrStatus = _AlaQoSAppliedConditionVmSourceIpv6IpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 133),
    _AlaQoSAppliedConditionVmSourceIpv6IpAddrStatus_Type()
)
alaQoSAppliedConditionVmSourceIpv6IpAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionVmSourceIpv6IpAddrStatus.setStatus("current")


class _AlaQoSAppliedConditionVmSourceIpv6IpMask_Type(Ipv6Address):
    """Custom type alaQoSAppliedConditionVmSourceIpv6IpMask based on Ipv6Address"""
    defaultHexValue = "ffffffffffffffffffffffffffffffff"


_AlaQoSAppliedConditionVmSourceIpv6IpMask_Type.__name__ = "Ipv6Address"
_AlaQoSAppliedConditionVmSourceIpv6IpMask_Object = MibTableColumn
alaQoSAppliedConditionVmSourceIpv6IpMask = _AlaQoSAppliedConditionVmSourceIpv6IpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 134),
    _AlaQoSAppliedConditionVmSourceIpv6IpMask_Type()
)
alaQoSAppliedConditionVmSourceIpv6IpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionVmSourceIpv6IpMask.setStatus("current")


class _AlaQoSAppliedConditionVmIpProtocol_Type(Integer32):
    """Custom type alaQoSAppliedConditionVmIpProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSAppliedConditionVmIpProtocol_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionVmIpProtocol_Object = MibTableColumn
alaQoSAppliedConditionVmIpProtocol = _AlaQoSAppliedConditionVmIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 135),
    _AlaQoSAppliedConditionVmIpProtocol_Type()
)
alaQoSAppliedConditionVmIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionVmIpProtocol.setStatus("current")


class _AlaQoSAppliedConditionVmIpProtocolStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionVmIpProtocolStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSAppliedConditionVmIpProtocolStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionVmIpProtocolStatus_Object = MibTableColumn
alaQoSAppliedConditionVmIpProtocolStatus = _AlaQoSAppliedConditionVmIpProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 136),
    _AlaQoSAppliedConditionVmIpProtocolStatus_Type()
)
alaQoSAppliedConditionVmIpProtocolStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionVmIpProtocolStatus.setStatus("current")


class _AlaQosAppliedConditionVmL4SourcePort_Type(Integer32):
    """Custom type alaQosAppliedConditionVmL4SourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQosAppliedConditionVmL4SourcePort_Type.__name__ = "Integer32"
_AlaQosAppliedConditionVmL4SourcePort_Object = MibTableColumn
alaQosAppliedConditionVmL4SourcePort = _AlaQosAppliedConditionVmL4SourcePort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 137),
    _AlaQosAppliedConditionVmL4SourcePort_Type()
)
alaQosAppliedConditionVmL4SourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQosAppliedConditionVmL4SourcePort.setStatus("current")


class _AlaQosAppliedConditionVmL4SourcePortStatus_Type(Integer32):
    """Custom type alaQosAppliedConditionVmL4SourcePortStatus based on Integer32"""
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


_AlaQosAppliedConditionVmL4SourcePortStatus_Type.__name__ = "Integer32"
_AlaQosAppliedConditionVmL4SourcePortStatus_Object = MibTableColumn
alaQosAppliedConditionVmL4SourcePortStatus = _AlaQosAppliedConditionVmL4SourcePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 138),
    _AlaQosAppliedConditionVmL4SourcePortStatus_Type()
)
alaQosAppliedConditionVmL4SourcePortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQosAppliedConditionVmL4SourcePortStatus.setStatus("current")


class _AlaQosAppliedConditionVmL4DestPort_Type(Integer32):
    """Custom type alaQosAppliedConditionVmL4DestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQosAppliedConditionVmL4DestPort_Type.__name__ = "Integer32"
_AlaQosAppliedConditionVmL4DestPort_Object = MibTableColumn
alaQosAppliedConditionVmL4DestPort = _AlaQosAppliedConditionVmL4DestPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 139),
    _AlaQosAppliedConditionVmL4DestPort_Type()
)
alaQosAppliedConditionVmL4DestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQosAppliedConditionVmL4DestPort.setStatus("current")


class _AlaQosAppliedConditionVmL4DestPortStatus_Type(Integer32):
    """Custom type alaQosAppliedConditionVmL4DestPortStatus based on Integer32"""
    defaultValue = 2

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


_AlaQosAppliedConditionVmL4DestPortStatus_Type.__name__ = "Integer32"
_AlaQosAppliedConditionVmL4DestPortStatus_Object = MibTableColumn
alaQosAppliedConditionVmL4DestPortStatus = _AlaQosAppliedConditionVmL4DestPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 140),
    _AlaQosAppliedConditionVmL4DestPortStatus_Type()
)
alaQosAppliedConditionVmL4DestPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQosAppliedConditionVmL4DestPortStatus.setStatus("current")


class _AlaQosAppliedConditionVxlanStatus_Type(Integer32):
    """Custom type alaQosAppliedConditionVxlanStatus based on Integer32"""
    defaultValue = 2

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


_AlaQosAppliedConditionVxlanStatus_Type.__name__ = "Integer32"
_AlaQosAppliedConditionVxlanStatus_Object = MibTableColumn
alaQosAppliedConditionVxlanStatus = _AlaQosAppliedConditionVxlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 141),
    _AlaQosAppliedConditionVxlanStatus_Type()
)
alaQosAppliedConditionVxlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQosAppliedConditionVxlanStatus.setStatus("current")


class _AlaQoSAppliedConditionSourcePortSplitGroup_Type(SnmpAdminString):
    """Custom type alaQoSAppliedConditionSourcePortSplitGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedConditionSourcePortSplitGroup_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedConditionSourcePortSplitGroup_Object = MibTableColumn
alaQoSAppliedConditionSourcePortSplitGroup = _AlaQoSAppliedConditionSourcePortSplitGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 142),
    _AlaQoSAppliedConditionSourcePortSplitGroup_Type()
)
alaQoSAppliedConditionSourcePortSplitGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourcePortSplitGroup.setStatus("current")


class _AlaQoSAppliedConditionSourcePortSplitGroupStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourcePortSplitGroupStatus based on Integer32"""
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


_AlaQoSAppliedConditionSourcePortSplitGroupStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourcePortSplitGroupStatus_Object = MibTableColumn
alaQoSAppliedConditionSourcePortSplitGroupStatus = _AlaQoSAppliedConditionSourcePortSplitGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 143),
    _AlaQoSAppliedConditionSourcePortSplitGroupStatus_Type()
)
alaQoSAppliedConditionSourcePortSplitGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourcePortSplitGroupStatus.setStatus("current")
_AlaQoSServiceTable_Object = MibTable
alaQoSServiceTable = _AlaQoSServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5)
)
if mibBuilder.loadTexts:
    alaQoSServiceTable.setStatus("current")
_AlaQoSServiceEntry_Object = MibTableRow
alaQoSServiceEntry = _AlaQoSServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1)
)
alaQoSServiceEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSServiceName"),
)
if mibBuilder.loadTexts:
    alaQoSServiceEntry.setStatus("current")


class _AlaQoSServiceName_Type(SnmpAdminString):
    """Custom type alaQoSServiceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSServiceName_Type.__name__ = "SnmpAdminString"
_AlaQoSServiceName_Object = MibTableColumn
alaQoSServiceName = _AlaQoSServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 1),
    _AlaQoSServiceName_Type()
)
alaQoSServiceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSServiceName.setStatus("current")


class _AlaQoSServiceSource_Type(Integer32):
    """Custom type alaQoSServiceSource based on Integer32"""
    defaultValue = 2

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
        *(("ldap", 1),
          ("cli", 2),
          ("blt", 3),
          ("api", 4),
          ("imp", 5))
    )


_AlaQoSServiceSource_Type.__name__ = "Integer32"
_AlaQoSServiceSource_Object = MibTableColumn
alaQoSServiceSource = _AlaQoSServiceSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 2),
    _AlaQoSServiceSource_Type()
)
alaQoSServiceSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceSource.setStatus("current")


class _AlaQoSServiceProtocol_Type(Integer32):
    """Custom type alaQoSServiceProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSServiceProtocol_Type.__name__ = "Integer32"
_AlaQoSServiceProtocol_Object = MibTableColumn
alaQoSServiceProtocol = _AlaQoSServiceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 3),
    _AlaQoSServiceProtocol_Type()
)
alaQoSServiceProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceProtocol.setStatus("current")


class _AlaQoSServiceSourceIpPort_Type(Integer32):
    """Custom type alaQoSServiceSourceIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSServiceSourceIpPort_Type.__name__ = "Integer32"
_AlaQoSServiceSourceIpPort_Object = MibTableColumn
alaQoSServiceSourceIpPort = _AlaQoSServiceSourceIpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 4),
    _AlaQoSServiceSourceIpPort_Type()
)
alaQoSServiceSourceIpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceSourceIpPort.setStatus("current")


class _AlaQoSServiceSourceIpPortStatus_Type(Integer32):
    """Custom type alaQoSServiceSourceIpPortStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSServiceSourceIpPortStatus_Type.__name__ = "Integer32"
_AlaQoSServiceSourceIpPortStatus_Object = MibTableColumn
alaQoSServiceSourceIpPortStatus = _AlaQoSServiceSourceIpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 5),
    _AlaQoSServiceSourceIpPortStatus_Type()
)
alaQoSServiceSourceIpPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceSourceIpPortStatus.setStatus("current")


class _AlaQoSServiceDestinationIpPort_Type(Integer32):
    """Custom type alaQoSServiceDestinationIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSServiceDestinationIpPort_Type.__name__ = "Integer32"
_AlaQoSServiceDestinationIpPort_Object = MibTableColumn
alaQoSServiceDestinationIpPort = _AlaQoSServiceDestinationIpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 6),
    _AlaQoSServiceDestinationIpPort_Type()
)
alaQoSServiceDestinationIpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceDestinationIpPort.setStatus("current")


class _AlaQoSServiceDestinationIpPortStatus_Type(Integer32):
    """Custom type alaQoSServiceDestinationIpPortStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSServiceDestinationIpPortStatus_Type.__name__ = "Integer32"
_AlaQoSServiceDestinationIpPortStatus_Object = MibTableColumn
alaQoSServiceDestinationIpPortStatus = _AlaQoSServiceDestinationIpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 7),
    _AlaQoSServiceDestinationIpPortStatus_Type()
)
alaQoSServiceDestinationIpPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceDestinationIpPortStatus.setStatus("current")
_AlaQoSServiceRowStatus_Type = RowStatus
_AlaQoSServiceRowStatus_Object = MibTableColumn
alaQoSServiceRowStatus = _AlaQoSServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 8),
    _AlaQoSServiceRowStatus_Type()
)
alaQoSServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceRowStatus.setStatus("current")


class _AlaQoSServiceSourceIpPortEnd_Type(Integer32):
    """Custom type alaQoSServiceSourceIpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSServiceSourceIpPortEnd_Type.__name__ = "Integer32"
_AlaQoSServiceSourceIpPortEnd_Object = MibTableColumn
alaQoSServiceSourceIpPortEnd = _AlaQoSServiceSourceIpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 9),
    _AlaQoSServiceSourceIpPortEnd_Type()
)
alaQoSServiceSourceIpPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceSourceIpPortEnd.setStatus("current")


class _AlaQoSServiceDestinationIpPortEnd_Type(Integer32):
    """Custom type alaQoSServiceDestinationIpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSServiceDestinationIpPortEnd_Type.__name__ = "Integer32"
_AlaQoSServiceDestinationIpPortEnd_Object = MibTableColumn
alaQoSServiceDestinationIpPortEnd = _AlaQoSServiceDestinationIpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 10),
    _AlaQoSServiceDestinationIpPortEnd_Type()
)
alaQoSServiceDestinationIpPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceDestinationIpPortEnd.setStatus("current")


class _AlaQoSServiceSourceTcpPort_Type(Integer32):
    """Custom type alaQoSServiceSourceTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSServiceSourceTcpPort_Type.__name__ = "Integer32"
_AlaQoSServiceSourceTcpPort_Object = MibTableColumn
alaQoSServiceSourceTcpPort = _AlaQoSServiceSourceTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 11),
    _AlaQoSServiceSourceTcpPort_Type()
)
alaQoSServiceSourceTcpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceSourceTcpPort.setStatus("current")


class _AlaQoSServiceSourceTcpPortStatus_Type(Integer32):
    """Custom type alaQoSServiceSourceTcpPortStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSServiceSourceTcpPortStatus_Type.__name__ = "Integer32"
_AlaQoSServiceSourceTcpPortStatus_Object = MibTableColumn
alaQoSServiceSourceTcpPortStatus = _AlaQoSServiceSourceTcpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 12),
    _AlaQoSServiceSourceTcpPortStatus_Type()
)
alaQoSServiceSourceTcpPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceSourceTcpPortStatus.setStatus("current")


class _AlaQoSServiceSourceTcpPortEnd_Type(Integer32):
    """Custom type alaQoSServiceSourceTcpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSServiceSourceTcpPortEnd_Type.__name__ = "Integer32"
_AlaQoSServiceSourceTcpPortEnd_Object = MibTableColumn
alaQoSServiceSourceTcpPortEnd = _AlaQoSServiceSourceTcpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 13),
    _AlaQoSServiceSourceTcpPortEnd_Type()
)
alaQoSServiceSourceTcpPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceSourceTcpPortEnd.setStatus("current")


class _AlaQoSServiceDestinationTcpPort_Type(Integer32):
    """Custom type alaQoSServiceDestinationTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSServiceDestinationTcpPort_Type.__name__ = "Integer32"
_AlaQoSServiceDestinationTcpPort_Object = MibTableColumn
alaQoSServiceDestinationTcpPort = _AlaQoSServiceDestinationTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 14),
    _AlaQoSServiceDestinationTcpPort_Type()
)
alaQoSServiceDestinationTcpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceDestinationTcpPort.setStatus("current")


class _AlaQoSServiceDestinationTcpPortStatus_Type(Integer32):
    """Custom type alaQoSServiceDestinationTcpPortStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSServiceDestinationTcpPortStatus_Type.__name__ = "Integer32"
_AlaQoSServiceDestinationTcpPortStatus_Object = MibTableColumn
alaQoSServiceDestinationTcpPortStatus = _AlaQoSServiceDestinationTcpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 15),
    _AlaQoSServiceDestinationTcpPortStatus_Type()
)
alaQoSServiceDestinationTcpPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceDestinationTcpPortStatus.setStatus("current")


class _AlaQoSServiceDestinationTcpPortEnd_Type(Integer32):
    """Custom type alaQoSServiceDestinationTcpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSServiceDestinationTcpPortEnd_Type.__name__ = "Integer32"
_AlaQoSServiceDestinationTcpPortEnd_Object = MibTableColumn
alaQoSServiceDestinationTcpPortEnd = _AlaQoSServiceDestinationTcpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 16),
    _AlaQoSServiceDestinationTcpPortEnd_Type()
)
alaQoSServiceDestinationTcpPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceDestinationTcpPortEnd.setStatus("current")


class _AlaQoSServiceSourceUdpPort_Type(Integer32):
    """Custom type alaQoSServiceSourceUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSServiceSourceUdpPort_Type.__name__ = "Integer32"
_AlaQoSServiceSourceUdpPort_Object = MibTableColumn
alaQoSServiceSourceUdpPort = _AlaQoSServiceSourceUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 17),
    _AlaQoSServiceSourceUdpPort_Type()
)
alaQoSServiceSourceUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceSourceUdpPort.setStatus("current")


class _AlaQoSServiceSourceUdpPortStatus_Type(Integer32):
    """Custom type alaQoSServiceSourceUdpPortStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSServiceSourceUdpPortStatus_Type.__name__ = "Integer32"
_AlaQoSServiceSourceUdpPortStatus_Object = MibTableColumn
alaQoSServiceSourceUdpPortStatus = _AlaQoSServiceSourceUdpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 18),
    _AlaQoSServiceSourceUdpPortStatus_Type()
)
alaQoSServiceSourceUdpPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceSourceUdpPortStatus.setStatus("current")


class _AlaQoSServiceSourceUdpPortEnd_Type(Integer32):
    """Custom type alaQoSServiceSourceUdpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSServiceSourceUdpPortEnd_Type.__name__ = "Integer32"
_AlaQoSServiceSourceUdpPortEnd_Object = MibTableColumn
alaQoSServiceSourceUdpPortEnd = _AlaQoSServiceSourceUdpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 19),
    _AlaQoSServiceSourceUdpPortEnd_Type()
)
alaQoSServiceSourceUdpPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceSourceUdpPortEnd.setStatus("current")


class _AlaQoSServiceDestinationUdpPort_Type(Integer32):
    """Custom type alaQoSServiceDestinationUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSServiceDestinationUdpPort_Type.__name__ = "Integer32"
_AlaQoSServiceDestinationUdpPort_Object = MibTableColumn
alaQoSServiceDestinationUdpPort = _AlaQoSServiceDestinationUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 20),
    _AlaQoSServiceDestinationUdpPort_Type()
)
alaQoSServiceDestinationUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceDestinationUdpPort.setStatus("current")


class _AlaQoSServiceDestinationUdpPortStatus_Type(Integer32):
    """Custom type alaQoSServiceDestinationUdpPortStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSServiceDestinationUdpPortStatus_Type.__name__ = "Integer32"
_AlaQoSServiceDestinationUdpPortStatus_Object = MibTableColumn
alaQoSServiceDestinationUdpPortStatus = _AlaQoSServiceDestinationUdpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 21),
    _AlaQoSServiceDestinationUdpPortStatus_Type()
)
alaQoSServiceDestinationUdpPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceDestinationUdpPortStatus.setStatus("current")


class _AlaQoSServiceDestinationUdpPortEnd_Type(Integer32):
    """Custom type alaQoSServiceDestinationUdpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSServiceDestinationUdpPortEnd_Type.__name__ = "Integer32"
_AlaQoSServiceDestinationUdpPortEnd_Object = MibTableColumn
alaQoSServiceDestinationUdpPortEnd = _AlaQoSServiceDestinationUdpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 22),
    _AlaQoSServiceDestinationUdpPortEnd_Type()
)
alaQoSServiceDestinationUdpPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceDestinationUdpPortEnd.setStatus("current")
_AlaQoSAppliedServiceTable_Object = MibTable
alaQoSAppliedServiceTable = _AlaQoSAppliedServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6)
)
if mibBuilder.loadTexts:
    alaQoSAppliedServiceTable.setStatus("current")
_AlaQoSAppliedServiceEntry_Object = MibTableRow
alaQoSAppliedServiceEntry = _AlaQoSAppliedServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1)
)
alaQoSAppliedServiceEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedServiceName"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedServiceEntry.setStatus("current")


class _AlaQoSAppliedServiceName_Type(SnmpAdminString):
    """Custom type alaQoSAppliedServiceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedServiceName_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedServiceName_Object = MibTableColumn
alaQoSAppliedServiceName = _AlaQoSAppliedServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 1),
    _AlaQoSAppliedServiceName_Type()
)
alaQoSAppliedServiceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceName.setStatus("current")


class _AlaQoSAppliedServiceSource_Type(Integer32):
    """Custom type alaQoSAppliedServiceSource based on Integer32"""
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
        *(("ldap", 1),
          ("cli", 2),
          ("blt", 3),
          ("api", 4),
          ("imp", 5))
    )


_AlaQoSAppliedServiceSource_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceSource_Object = MibTableColumn
alaQoSAppliedServiceSource = _AlaQoSAppliedServiceSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 2),
    _AlaQoSAppliedServiceSource_Type()
)
alaQoSAppliedServiceSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceSource.setStatus("current")


class _AlaQoSAppliedServiceProtocol_Type(Integer32):
    """Custom type alaQoSAppliedServiceProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSAppliedServiceProtocol_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceProtocol_Object = MibTableColumn
alaQoSAppliedServiceProtocol = _AlaQoSAppliedServiceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 3),
    _AlaQoSAppliedServiceProtocol_Type()
)
alaQoSAppliedServiceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceProtocol.setStatus("current")


class _AlaQoSAppliedServiceSourceIpPort_Type(Integer32):
    """Custom type alaQoSAppliedServiceSourceIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedServiceSourceIpPort_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceSourceIpPort_Object = MibTableColumn
alaQoSAppliedServiceSourceIpPort = _AlaQoSAppliedServiceSourceIpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 4),
    _AlaQoSAppliedServiceSourceIpPort_Type()
)
alaQoSAppliedServiceSourceIpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceSourceIpPort.setStatus("current")


class _AlaQoSAppliedServiceSourceIpPortStatus_Type(Integer32):
    """Custom type alaQoSAppliedServiceSourceIpPortStatus based on Integer32"""
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


_AlaQoSAppliedServiceSourceIpPortStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceSourceIpPortStatus_Object = MibTableColumn
alaQoSAppliedServiceSourceIpPortStatus = _AlaQoSAppliedServiceSourceIpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 5),
    _AlaQoSAppliedServiceSourceIpPortStatus_Type()
)
alaQoSAppliedServiceSourceIpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceSourceIpPortStatus.setStatus("current")


class _AlaQoSAppliedServiceDestinationIpPort_Type(Integer32):
    """Custom type alaQoSAppliedServiceDestinationIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedServiceDestinationIpPort_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceDestinationIpPort_Object = MibTableColumn
alaQoSAppliedServiceDestinationIpPort = _AlaQoSAppliedServiceDestinationIpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 6),
    _AlaQoSAppliedServiceDestinationIpPort_Type()
)
alaQoSAppliedServiceDestinationIpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceDestinationIpPort.setStatus("current")


class _AlaQoSAppliedServiceDestinationIpPortStatus_Type(Integer32):
    """Custom type alaQoSAppliedServiceDestinationIpPortStatus based on Integer32"""
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


_AlaQoSAppliedServiceDestinationIpPortStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceDestinationIpPortStatus_Object = MibTableColumn
alaQoSAppliedServiceDestinationIpPortStatus = _AlaQoSAppliedServiceDestinationIpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 7),
    _AlaQoSAppliedServiceDestinationIpPortStatus_Type()
)
alaQoSAppliedServiceDestinationIpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceDestinationIpPortStatus.setStatus("current")
_AlaQoSAppliedServiceRowStatus_Type = RowStatus
_AlaQoSAppliedServiceRowStatus_Object = MibTableColumn
alaQoSAppliedServiceRowStatus = _AlaQoSAppliedServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 8),
    _AlaQoSAppliedServiceRowStatus_Type()
)
alaQoSAppliedServiceRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceRowStatus.setStatus("current")


class _AlaQoSAppliedServiceSourceIpPortEnd_Type(Integer32):
    """Custom type alaQoSAppliedServiceSourceIpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedServiceSourceIpPortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceSourceIpPortEnd_Object = MibTableColumn
alaQoSAppliedServiceSourceIpPortEnd = _AlaQoSAppliedServiceSourceIpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 9),
    _AlaQoSAppliedServiceSourceIpPortEnd_Type()
)
alaQoSAppliedServiceSourceIpPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceSourceIpPortEnd.setStatus("current")


class _AlaQoSAppliedServiceDestinationIpPortEnd_Type(Integer32):
    """Custom type alaQoSAppliedServiceDestinationIpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedServiceDestinationIpPortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceDestinationIpPortEnd_Object = MibTableColumn
alaQoSAppliedServiceDestinationIpPortEnd = _AlaQoSAppliedServiceDestinationIpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 10),
    _AlaQoSAppliedServiceDestinationIpPortEnd_Type()
)
alaQoSAppliedServiceDestinationIpPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceDestinationIpPortEnd.setStatus("current")


class _AlaQoSAppliedServiceSourceTcpPort_Type(Integer32):
    """Custom type alaQoSAppliedServiceSourceTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedServiceSourceTcpPort_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceSourceTcpPort_Object = MibTableColumn
alaQoSAppliedServiceSourceTcpPort = _AlaQoSAppliedServiceSourceTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 11),
    _AlaQoSAppliedServiceSourceTcpPort_Type()
)
alaQoSAppliedServiceSourceTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceSourceTcpPort.setStatus("current")


class _AlaQoSAppliedServiceSourceTcpPortStatus_Type(Integer32):
    """Custom type alaQoSAppliedServiceSourceTcpPortStatus based on Integer32"""
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


_AlaQoSAppliedServiceSourceTcpPortStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceSourceTcpPortStatus_Object = MibTableColumn
alaQoSAppliedServiceSourceTcpPortStatus = _AlaQoSAppliedServiceSourceTcpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 12),
    _AlaQoSAppliedServiceSourceTcpPortStatus_Type()
)
alaQoSAppliedServiceSourceTcpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceSourceTcpPortStatus.setStatus("current")


class _AlaQoSAppliedServiceSourceTcpPortEnd_Type(Integer32):
    """Custom type alaQoSAppliedServiceSourceTcpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedServiceSourceTcpPortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceSourceTcpPortEnd_Object = MibTableColumn
alaQoSAppliedServiceSourceTcpPortEnd = _AlaQoSAppliedServiceSourceTcpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 13),
    _AlaQoSAppliedServiceSourceTcpPortEnd_Type()
)
alaQoSAppliedServiceSourceTcpPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceSourceTcpPortEnd.setStatus("current")


class _AlaQoSAppliedServiceDestinationTcpPort_Type(Integer32):
    """Custom type alaQoSAppliedServiceDestinationTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedServiceDestinationTcpPort_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceDestinationTcpPort_Object = MibTableColumn
alaQoSAppliedServiceDestinationTcpPort = _AlaQoSAppliedServiceDestinationTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 14),
    _AlaQoSAppliedServiceDestinationTcpPort_Type()
)
alaQoSAppliedServiceDestinationTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceDestinationTcpPort.setStatus("current")


class _AlaQoSAppliedServiceDestinationTcpPortStatus_Type(Integer32):
    """Custom type alaQoSAppliedServiceDestinationTcpPortStatus based on Integer32"""
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


_AlaQoSAppliedServiceDestinationTcpPortStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceDestinationTcpPortStatus_Object = MibTableColumn
alaQoSAppliedServiceDestinationTcpPortStatus = _AlaQoSAppliedServiceDestinationTcpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 15),
    _AlaQoSAppliedServiceDestinationTcpPortStatus_Type()
)
alaQoSAppliedServiceDestinationTcpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceDestinationTcpPortStatus.setStatus("current")


class _AlaQoSAppliedServiceDestinationTcpPortEnd_Type(Integer32):
    """Custom type alaQoSAppliedServiceDestinationTcpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedServiceDestinationTcpPortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceDestinationTcpPortEnd_Object = MibTableColumn
alaQoSAppliedServiceDestinationTcpPortEnd = _AlaQoSAppliedServiceDestinationTcpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 16),
    _AlaQoSAppliedServiceDestinationTcpPortEnd_Type()
)
alaQoSAppliedServiceDestinationTcpPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceDestinationTcpPortEnd.setStatus("current")


class _AlaQoSAppliedServiceSourceUdpPort_Type(Integer32):
    """Custom type alaQoSAppliedServiceSourceUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedServiceSourceUdpPort_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceSourceUdpPort_Object = MibTableColumn
alaQoSAppliedServiceSourceUdpPort = _AlaQoSAppliedServiceSourceUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 17),
    _AlaQoSAppliedServiceSourceUdpPort_Type()
)
alaQoSAppliedServiceSourceUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceSourceUdpPort.setStatus("current")


class _AlaQoSAppliedServiceSourceUdpPortStatus_Type(Integer32):
    """Custom type alaQoSAppliedServiceSourceUdpPortStatus based on Integer32"""
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


_AlaQoSAppliedServiceSourceUdpPortStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceSourceUdpPortStatus_Object = MibTableColumn
alaQoSAppliedServiceSourceUdpPortStatus = _AlaQoSAppliedServiceSourceUdpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 18),
    _AlaQoSAppliedServiceSourceUdpPortStatus_Type()
)
alaQoSAppliedServiceSourceUdpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceSourceUdpPortStatus.setStatus("current")


class _AlaQoSAppliedServiceSourceUdpPortEnd_Type(Integer32):
    """Custom type alaQoSAppliedServiceSourceUdpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedServiceSourceUdpPortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceSourceUdpPortEnd_Object = MibTableColumn
alaQoSAppliedServiceSourceUdpPortEnd = _AlaQoSAppliedServiceSourceUdpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 19),
    _AlaQoSAppliedServiceSourceUdpPortEnd_Type()
)
alaQoSAppliedServiceSourceUdpPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceSourceUdpPortEnd.setStatus("current")


class _AlaQoSAppliedServiceDestinationUdpPort_Type(Integer32):
    """Custom type alaQoSAppliedServiceDestinationUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedServiceDestinationUdpPort_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceDestinationUdpPort_Object = MibTableColumn
alaQoSAppliedServiceDestinationUdpPort = _AlaQoSAppliedServiceDestinationUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 20),
    _AlaQoSAppliedServiceDestinationUdpPort_Type()
)
alaQoSAppliedServiceDestinationUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceDestinationUdpPort.setStatus("current")


class _AlaQoSAppliedServiceDestinationUdpPortStatus_Type(Integer32):
    """Custom type alaQoSAppliedServiceDestinationUdpPortStatus based on Integer32"""
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


_AlaQoSAppliedServiceDestinationUdpPortStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceDestinationUdpPortStatus_Object = MibTableColumn
alaQoSAppliedServiceDestinationUdpPortStatus = _AlaQoSAppliedServiceDestinationUdpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 21),
    _AlaQoSAppliedServiceDestinationUdpPortStatus_Type()
)
alaQoSAppliedServiceDestinationUdpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceDestinationUdpPortStatus.setStatus("current")


class _AlaQoSAppliedServiceDestinationUdpPortEnd_Type(Integer32):
    """Custom type alaQoSAppliedServiceDestinationUdpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedServiceDestinationUdpPortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceDestinationUdpPortEnd_Object = MibTableColumn
alaQoSAppliedServiceDestinationUdpPortEnd = _AlaQoSAppliedServiceDestinationUdpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 22),
    _AlaQoSAppliedServiceDestinationUdpPortEnd_Type()
)
alaQoSAppliedServiceDestinationUdpPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceDestinationUdpPortEnd.setStatus("current")
_AlaQoSServiceGroupsTable_Object = MibTable
alaQoSServiceGroupsTable = _AlaQoSServiceGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 7)
)
if mibBuilder.loadTexts:
    alaQoSServiceGroupsTable.setStatus("current")
_AlaQoSServiceGroupsEntry_Object = MibTableRow
alaQoSServiceGroupsEntry = _AlaQoSServiceGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 7, 1)
)
alaQoSServiceGroupsEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSServiceGroupsName"),
)
if mibBuilder.loadTexts:
    alaQoSServiceGroupsEntry.setStatus("current")


class _AlaQoSServiceGroupsName_Type(SnmpAdminString):
    """Custom type alaQoSServiceGroupsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSServiceGroupsName_Type.__name__ = "SnmpAdminString"
_AlaQoSServiceGroupsName_Object = MibTableColumn
alaQoSServiceGroupsName = _AlaQoSServiceGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 7, 1, 1),
    _AlaQoSServiceGroupsName_Type()
)
alaQoSServiceGroupsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSServiceGroupsName.setStatus("current")


class _AlaQoSServiceGroupsSource_Type(Integer32):
    """Custom type alaQoSServiceGroupsSource based on Integer32"""
    defaultValue = 2

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
        *(("ldap", 1),
          ("cli", 2),
          ("blt", 3),
          ("api", 4),
          ("imp", 5))
    )


_AlaQoSServiceGroupsSource_Type.__name__ = "Integer32"
_AlaQoSServiceGroupsSource_Object = MibTableColumn
alaQoSServiceGroupsSource = _AlaQoSServiceGroupsSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 7, 1, 2),
    _AlaQoSServiceGroupsSource_Type()
)
alaQoSServiceGroupsSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceGroupsSource.setStatus("current")
_AlaQoSServiceGroupsStatus_Type = RowStatus
_AlaQoSServiceGroupsStatus_Object = MibTableColumn
alaQoSServiceGroupsStatus = _AlaQoSServiceGroupsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 7, 1, 3),
    _AlaQoSServiceGroupsStatus_Type()
)
alaQoSServiceGroupsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceGroupsStatus.setStatus("current")
_AlaQoSAppliedServiceGroupsTable_Object = MibTable
alaQoSAppliedServiceGroupsTable = _AlaQoSAppliedServiceGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 8)
)
if mibBuilder.loadTexts:
    alaQoSAppliedServiceGroupsTable.setStatus("current")
_AlaQoSAppliedServiceGroupsEntry_Object = MibTableRow
alaQoSAppliedServiceGroupsEntry = _AlaQoSAppliedServiceGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 8, 1)
)
alaQoSAppliedServiceGroupsEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedServiceGroupsName"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedServiceGroupsEntry.setStatus("current")


class _AlaQoSAppliedServiceGroupsName_Type(SnmpAdminString):
    """Custom type alaQoSAppliedServiceGroupsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedServiceGroupsName_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedServiceGroupsName_Object = MibTableColumn
alaQoSAppliedServiceGroupsName = _AlaQoSAppliedServiceGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 8, 1, 1),
    _AlaQoSAppliedServiceGroupsName_Type()
)
alaQoSAppliedServiceGroupsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceGroupsName.setStatus("current")


class _AlaQoSAppliedServiceGroupsSource_Type(Integer32):
    """Custom type alaQoSAppliedServiceGroupsSource based on Integer32"""
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
        *(("ldap", 1),
          ("cli", 2),
          ("blt", 3),
          ("api", 4),
          ("imp", 5))
    )


_AlaQoSAppliedServiceGroupsSource_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceGroupsSource_Object = MibTableColumn
alaQoSAppliedServiceGroupsSource = _AlaQoSAppliedServiceGroupsSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 8, 1, 2),
    _AlaQoSAppliedServiceGroupsSource_Type()
)
alaQoSAppliedServiceGroupsSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceGroupsSource.setStatus("current")
_AlaQoSAppliedServiceGroupsStatus_Type = RowStatus
_AlaQoSAppliedServiceGroupsStatus_Object = MibTableColumn
alaQoSAppliedServiceGroupsStatus = _AlaQoSAppliedServiceGroupsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 8, 1, 3),
    _AlaQoSAppliedServiceGroupsStatus_Type()
)
alaQoSAppliedServiceGroupsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceGroupsStatus.setStatus("current")
_AlaQoSServiceGroupTable_Object = MibTable
alaQoSServiceGroupTable = _AlaQoSServiceGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 9)
)
if mibBuilder.loadTexts:
    alaQoSServiceGroupTable.setStatus("current")
_AlaQoSServiceGroupEntry_Object = MibTableRow
alaQoSServiceGroupEntry = _AlaQoSServiceGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 9, 1)
)
alaQoSServiceGroupEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSServiceGroupsName"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSServiceGroupServiceName"),
)
if mibBuilder.loadTexts:
    alaQoSServiceGroupEntry.setStatus("current")


class _AlaQoSServiceGroupServiceName_Type(SnmpAdminString):
    """Custom type alaQoSServiceGroupServiceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSServiceGroupServiceName_Type.__name__ = "SnmpAdminString"
_AlaQoSServiceGroupServiceName_Object = MibTableColumn
alaQoSServiceGroupServiceName = _AlaQoSServiceGroupServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 9, 1, 1),
    _AlaQoSServiceGroupServiceName_Type()
)
alaQoSServiceGroupServiceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSServiceGroupServiceName.setStatus("current")
_AlaQoSServiceGroupStatus_Type = RowStatus
_AlaQoSServiceGroupStatus_Object = MibTableColumn
alaQoSServiceGroupStatus = _AlaQoSServiceGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 9, 1, 2),
    _AlaQoSServiceGroupStatus_Type()
)
alaQoSServiceGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceGroupStatus.setStatus("current")
_AlaQoSAppliedServiceGroupTable_Object = MibTable
alaQoSAppliedServiceGroupTable = _AlaQoSAppliedServiceGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 10)
)
if mibBuilder.loadTexts:
    alaQoSAppliedServiceGroupTable.setStatus("current")
_AlaQoSAppliedServiceGroupEntry_Object = MibTableRow
alaQoSAppliedServiceGroupEntry = _AlaQoSAppliedServiceGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 10, 1)
)
alaQoSAppliedServiceGroupEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedServiceGroupsName"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedServiceGroupServiceName"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedServiceGroupEntry.setStatus("current")


class _AlaQoSAppliedServiceGroupServiceName_Type(SnmpAdminString):
    """Custom type alaQoSAppliedServiceGroupServiceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedServiceGroupServiceName_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedServiceGroupServiceName_Object = MibTableColumn
alaQoSAppliedServiceGroupServiceName = _AlaQoSAppliedServiceGroupServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 10, 1, 1),
    _AlaQoSAppliedServiceGroupServiceName_Type()
)
alaQoSAppliedServiceGroupServiceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceGroupServiceName.setStatus("current")
_AlaQoSAppliedServiceGroupStatus_Type = RowStatus
_AlaQoSAppliedServiceGroupStatus_Object = MibTableColumn
alaQoSAppliedServiceGroupStatus = _AlaQoSAppliedServiceGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 10, 1, 2),
    _AlaQoSAppliedServiceGroupStatus_Type()
)
alaQoSAppliedServiceGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceGroupStatus.setStatus("current")
_AlaQoSNetworkGroupsTable_Object = MibTable
alaQoSNetworkGroupsTable = _AlaQoSNetworkGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 11)
)
if mibBuilder.loadTexts:
    alaQoSNetworkGroupsTable.setStatus("current")
_AlaQoSNetworkGroupsEntry_Object = MibTableRow
alaQoSNetworkGroupsEntry = _AlaQoSNetworkGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 11, 1)
)
alaQoSNetworkGroupsEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSNetworkGroupsName"),
)
if mibBuilder.loadTexts:
    alaQoSNetworkGroupsEntry.setStatus("current")


class _AlaQoSNetworkGroupsName_Type(SnmpAdminString):
    """Custom type alaQoSNetworkGroupsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSNetworkGroupsName_Type.__name__ = "SnmpAdminString"
_AlaQoSNetworkGroupsName_Object = MibTableColumn
alaQoSNetworkGroupsName = _AlaQoSNetworkGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 11, 1, 1),
    _AlaQoSNetworkGroupsName_Type()
)
alaQoSNetworkGroupsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSNetworkGroupsName.setStatus("current")


class _AlaQoSNetworkGroupsSource_Type(Integer32):
    """Custom type alaQoSNetworkGroupsSource based on Integer32"""
    defaultValue = 2

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
        *(("ldap", 1),
          ("cli", 2),
          ("blt", 3),
          ("api", 4),
          ("imp", 5))
    )


_AlaQoSNetworkGroupsSource_Type.__name__ = "Integer32"
_AlaQoSNetworkGroupsSource_Object = MibTableColumn
alaQoSNetworkGroupsSource = _AlaQoSNetworkGroupsSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 11, 1, 2),
    _AlaQoSNetworkGroupsSource_Type()
)
alaQoSNetworkGroupsSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSNetworkGroupsSource.setStatus("current")
_AlaQoSNetworkGroupsStatus_Type = RowStatus
_AlaQoSNetworkGroupsStatus_Object = MibTableColumn
alaQoSNetworkGroupsStatus = _AlaQoSNetworkGroupsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 11, 1, 3),
    _AlaQoSNetworkGroupsStatus_Type()
)
alaQoSNetworkGroupsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSNetworkGroupsStatus.setStatus("current")
_AlaQoSAppliedNetworkGroupsTable_Object = MibTable
alaQoSAppliedNetworkGroupsTable = _AlaQoSAppliedNetworkGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 12)
)
if mibBuilder.loadTexts:
    alaQoSAppliedNetworkGroupsTable.setStatus("current")
_AlaQoSAppliedNetworkGroupsEntry_Object = MibTableRow
alaQoSAppliedNetworkGroupsEntry = _AlaQoSAppliedNetworkGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 12, 1)
)
alaQoSAppliedNetworkGroupsEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedNetworkGroupsName"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedNetworkGroupsEntry.setStatus("current")


class _AlaQoSAppliedNetworkGroupsName_Type(SnmpAdminString):
    """Custom type alaQoSAppliedNetworkGroupsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedNetworkGroupsName_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedNetworkGroupsName_Object = MibTableColumn
alaQoSAppliedNetworkGroupsName = _AlaQoSAppliedNetworkGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 12, 1, 1),
    _AlaQoSAppliedNetworkGroupsName_Type()
)
alaQoSAppliedNetworkGroupsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedNetworkGroupsName.setStatus("current")


class _AlaQoSAppliedNetworkGroupsSource_Type(Integer32):
    """Custom type alaQoSAppliedNetworkGroupsSource based on Integer32"""
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
        *(("ldap", 1),
          ("cli", 2),
          ("blt", 3),
          ("api", 4),
          ("imp", 5))
    )


_AlaQoSAppliedNetworkGroupsSource_Type.__name__ = "Integer32"
_AlaQoSAppliedNetworkGroupsSource_Object = MibTableColumn
alaQoSAppliedNetworkGroupsSource = _AlaQoSAppliedNetworkGroupsSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 12, 1, 2),
    _AlaQoSAppliedNetworkGroupsSource_Type()
)
alaQoSAppliedNetworkGroupsSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedNetworkGroupsSource.setStatus("current")
_AlaQoSAppliedNetworkGroupsStatus_Type = RowStatus
_AlaQoSAppliedNetworkGroupsStatus_Object = MibTableColumn
alaQoSAppliedNetworkGroupsStatus = _AlaQoSAppliedNetworkGroupsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 12, 1, 3),
    _AlaQoSAppliedNetworkGroupsStatus_Type()
)
alaQoSAppliedNetworkGroupsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedNetworkGroupsStatus.setStatus("current")
_AlaQoSNetworkGroupTable_Object = MibTable
alaQoSNetworkGroupTable = _AlaQoSNetworkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 13)
)
if mibBuilder.loadTexts:
    alaQoSNetworkGroupTable.setStatus("current")
_AlaQoSNetworkGroupEntry_Object = MibTableRow
alaQoSNetworkGroupEntry = _AlaQoSNetworkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 13, 1)
)
alaQoSNetworkGroupEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSNetworkGroupsName"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSNetworkGroupIpAddr"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSNetworkGroupIpMask"),
)
if mibBuilder.loadTexts:
    alaQoSNetworkGroupEntry.setStatus("current")
_AlaQoSNetworkGroupIpAddr_Type = IpAddress
_AlaQoSNetworkGroupIpAddr_Object = MibTableColumn
alaQoSNetworkGroupIpAddr = _AlaQoSNetworkGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 13, 1, 1),
    _AlaQoSNetworkGroupIpAddr_Type()
)
alaQoSNetworkGroupIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSNetworkGroupIpAddr.setStatus("current")
_AlaQoSNetworkGroupIpMask_Type = IpAddress
_AlaQoSNetworkGroupIpMask_Object = MibTableColumn
alaQoSNetworkGroupIpMask = _AlaQoSNetworkGroupIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 13, 1, 2),
    _AlaQoSNetworkGroupIpMask_Type()
)
alaQoSNetworkGroupIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSNetworkGroupIpMask.setStatus("current")
_AlaQoSNetworkGroupStatus_Type = RowStatus
_AlaQoSNetworkGroupStatus_Object = MibTableColumn
alaQoSNetworkGroupStatus = _AlaQoSNetworkGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 13, 1, 3),
    _AlaQoSNetworkGroupStatus_Type()
)
alaQoSNetworkGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSNetworkGroupStatus.setStatus("current")
_AlaQoSAppliedNetworkGroupTable_Object = MibTable
alaQoSAppliedNetworkGroupTable = _AlaQoSAppliedNetworkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 14)
)
if mibBuilder.loadTexts:
    alaQoSAppliedNetworkGroupTable.setStatus("current")
_AlaQoSAppliedNetworkGroupEntry_Object = MibTableRow
alaQoSAppliedNetworkGroupEntry = _AlaQoSAppliedNetworkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 14, 1)
)
alaQoSAppliedNetworkGroupEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedNetworkGroupsName"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedNetworkGroupIpAddr"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedNetworkGroupIpMask"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedNetworkGroupEntry.setStatus("current")
_AlaQoSAppliedNetworkGroupIpAddr_Type = IpAddress
_AlaQoSAppliedNetworkGroupIpAddr_Object = MibTableColumn
alaQoSAppliedNetworkGroupIpAddr = _AlaQoSAppliedNetworkGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 14, 1, 1),
    _AlaQoSAppliedNetworkGroupIpAddr_Type()
)
alaQoSAppliedNetworkGroupIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedNetworkGroupIpAddr.setStatus("current")
_AlaQoSAppliedNetworkGroupIpMask_Type = IpAddress
_AlaQoSAppliedNetworkGroupIpMask_Object = MibTableColumn
alaQoSAppliedNetworkGroupIpMask = _AlaQoSAppliedNetworkGroupIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 14, 1, 2),
    _AlaQoSAppliedNetworkGroupIpMask_Type()
)
alaQoSAppliedNetworkGroupIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedNetworkGroupIpMask.setStatus("current")
_AlaQoSAppliedNetworkGroupStatus_Type = RowStatus
_AlaQoSAppliedNetworkGroupStatus_Object = MibTableColumn
alaQoSAppliedNetworkGroupStatus = _AlaQoSAppliedNetworkGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 14, 1, 3),
    _AlaQoSAppliedNetworkGroupStatus_Type()
)
alaQoSAppliedNetworkGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedNetworkGroupStatus.setStatus("current")
_AlaQoSMACGroupsTable_Object = MibTable
alaQoSMACGroupsTable = _AlaQoSMACGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 15)
)
if mibBuilder.loadTexts:
    alaQoSMACGroupsTable.setStatus("current")
_AlaQoSMACGroupsEntry_Object = MibTableRow
alaQoSMACGroupsEntry = _AlaQoSMACGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 15, 1)
)
alaQoSMACGroupsEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSMACGroupsName"),
)
if mibBuilder.loadTexts:
    alaQoSMACGroupsEntry.setStatus("current")


class _AlaQoSMACGroupsName_Type(SnmpAdminString):
    """Custom type alaQoSMACGroupsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSMACGroupsName_Type.__name__ = "SnmpAdminString"
_AlaQoSMACGroupsName_Object = MibTableColumn
alaQoSMACGroupsName = _AlaQoSMACGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 15, 1, 1),
    _AlaQoSMACGroupsName_Type()
)
alaQoSMACGroupsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSMACGroupsName.setStatus("current")


class _AlaQoSMACGroupsSource_Type(Integer32):
    """Custom type alaQoSMACGroupsSource based on Integer32"""
    defaultValue = 2

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
        *(("ldap", 1),
          ("cli", 2),
          ("blt", 3),
          ("api", 4),
          ("imp", 5))
    )


_AlaQoSMACGroupsSource_Type.__name__ = "Integer32"
_AlaQoSMACGroupsSource_Object = MibTableColumn
alaQoSMACGroupsSource = _AlaQoSMACGroupsSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 15, 1, 2),
    _AlaQoSMACGroupsSource_Type()
)
alaQoSMACGroupsSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSMACGroupsSource.setStatus("current")
_AlaQoSMACGroupsStatus_Type = RowStatus
_AlaQoSMACGroupsStatus_Object = MibTableColumn
alaQoSMACGroupsStatus = _AlaQoSMACGroupsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 15, 1, 3),
    _AlaQoSMACGroupsStatus_Type()
)
alaQoSMACGroupsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSMACGroupsStatus.setStatus("current")
_AlaQoSAppliedMACGroupsTable_Object = MibTable
alaQoSAppliedMACGroupsTable = _AlaQoSAppliedMACGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 16)
)
if mibBuilder.loadTexts:
    alaQoSAppliedMACGroupsTable.setStatus("current")
_AlaQoSAppliedMACGroupsEntry_Object = MibTableRow
alaQoSAppliedMACGroupsEntry = _AlaQoSAppliedMACGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 16, 1)
)
alaQoSAppliedMACGroupsEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedMACGroupsName"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedMACGroupsEntry.setStatus("current")


class _AlaQoSAppliedMACGroupsName_Type(SnmpAdminString):
    """Custom type alaQoSAppliedMACGroupsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedMACGroupsName_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedMACGroupsName_Object = MibTableColumn
alaQoSAppliedMACGroupsName = _AlaQoSAppliedMACGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 16, 1, 1),
    _AlaQoSAppliedMACGroupsName_Type()
)
alaQoSAppliedMACGroupsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedMACGroupsName.setStatus("current")


class _AlaQoSAppliedMACGroupsSource_Type(Integer32):
    """Custom type alaQoSAppliedMACGroupsSource based on Integer32"""
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
        *(("ldap", 1),
          ("cli", 2),
          ("blt", 3),
          ("api", 4),
          ("imp", 5))
    )


_AlaQoSAppliedMACGroupsSource_Type.__name__ = "Integer32"
_AlaQoSAppliedMACGroupsSource_Object = MibTableColumn
alaQoSAppliedMACGroupsSource = _AlaQoSAppliedMACGroupsSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 16, 1, 2),
    _AlaQoSAppliedMACGroupsSource_Type()
)
alaQoSAppliedMACGroupsSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedMACGroupsSource.setStatus("current")
_AlaQoSAppliedMACGroupsStatus_Type = RowStatus
_AlaQoSAppliedMACGroupsStatus_Object = MibTableColumn
alaQoSAppliedMACGroupsStatus = _AlaQoSAppliedMACGroupsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 16, 1, 3),
    _AlaQoSAppliedMACGroupsStatus_Type()
)
alaQoSAppliedMACGroupsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedMACGroupsStatus.setStatus("current")
_AlaQoSMACGroupTable_Object = MibTable
alaQoSMACGroupTable = _AlaQoSMACGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 17)
)
if mibBuilder.loadTexts:
    alaQoSMACGroupTable.setStatus("current")
_AlaQoSMACGroupEntry_Object = MibTableRow
alaQoSMACGroupEntry = _AlaQoSMACGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 17, 1)
)
alaQoSMACGroupEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSMACGroupsName"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSMACGroupMacAddr"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSMACGroupMacMask"),
)
if mibBuilder.loadTexts:
    alaQoSMACGroupEntry.setStatus("current")
_AlaQoSMACGroupMacAddr_Type = MacAddress
_AlaQoSMACGroupMacAddr_Object = MibTableColumn
alaQoSMACGroupMacAddr = _AlaQoSMACGroupMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 17, 1, 1),
    _AlaQoSMACGroupMacAddr_Type()
)
alaQoSMACGroupMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSMACGroupMacAddr.setStatus("current")
_AlaQoSMACGroupMacMask_Type = MacAddress
_AlaQoSMACGroupMacMask_Object = MibTableColumn
alaQoSMACGroupMacMask = _AlaQoSMACGroupMacMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 17, 1, 2),
    _AlaQoSMACGroupMacMask_Type()
)
alaQoSMACGroupMacMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSMACGroupMacMask.setStatus("current")
_AlaQoSMACGroupStatus_Type = RowStatus
_AlaQoSMACGroupStatus_Object = MibTableColumn
alaQoSMACGroupStatus = _AlaQoSMACGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 17, 1, 3),
    _AlaQoSMACGroupStatus_Type()
)
alaQoSMACGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSMACGroupStatus.setStatus("current")
_AlaQoSAppliedMACGroupTable_Object = MibTable
alaQoSAppliedMACGroupTable = _AlaQoSAppliedMACGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 18)
)
if mibBuilder.loadTexts:
    alaQoSAppliedMACGroupTable.setStatus("current")
_AlaQoSAppliedMACGroupEntry_Object = MibTableRow
alaQoSAppliedMACGroupEntry = _AlaQoSAppliedMACGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 18, 1)
)
alaQoSAppliedMACGroupEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedMACGroupsName"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedMACGroupMacAddr"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedMACGroupMacMask"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedMACGroupEntry.setStatus("current")
_AlaQoSAppliedMACGroupMacAddr_Type = MacAddress
_AlaQoSAppliedMACGroupMacAddr_Object = MibTableColumn
alaQoSAppliedMACGroupMacAddr = _AlaQoSAppliedMACGroupMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 18, 1, 1),
    _AlaQoSAppliedMACGroupMacAddr_Type()
)
alaQoSAppliedMACGroupMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedMACGroupMacAddr.setStatus("current")
_AlaQoSAppliedMACGroupMacMask_Type = MacAddress
_AlaQoSAppliedMACGroupMacMask_Object = MibTableColumn
alaQoSAppliedMACGroupMacMask = _AlaQoSAppliedMACGroupMacMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 18, 1, 2),
    _AlaQoSAppliedMACGroupMacMask_Type()
)
alaQoSAppliedMACGroupMacMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedMACGroupMacMask.setStatus("current")
_AlaQoSAppliedMACGroupStatus_Type = RowStatus
_AlaQoSAppliedMACGroupStatus_Object = MibTableColumn
alaQoSAppliedMACGroupStatus = _AlaQoSAppliedMACGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 18, 1, 3),
    _AlaQoSAppliedMACGroupStatus_Type()
)
alaQoSAppliedMACGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedMACGroupStatus.setStatus("current")
_AlaQoSPortGroupsTable_Object = MibTable
alaQoSPortGroupsTable = _AlaQoSPortGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 19)
)
if mibBuilder.loadTexts:
    alaQoSPortGroupsTable.setStatus("current")
_AlaQoSPortGroupsEntry_Object = MibTableRow
alaQoSPortGroupsEntry = _AlaQoSPortGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 19, 1)
)
alaQoSPortGroupsEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSPortGroupsName"),
)
if mibBuilder.loadTexts:
    alaQoSPortGroupsEntry.setStatus("current")


class _AlaQoSPortGroupsName_Type(SnmpAdminString):
    """Custom type alaQoSPortGroupsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSPortGroupsName_Type.__name__ = "SnmpAdminString"
_AlaQoSPortGroupsName_Object = MibTableColumn
alaQoSPortGroupsName = _AlaQoSPortGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 19, 1, 1),
    _AlaQoSPortGroupsName_Type()
)
alaQoSPortGroupsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSPortGroupsName.setStatus("current")


class _AlaQoSPortGroupsSource_Type(Integer32):
    """Custom type alaQoSPortGroupsSource based on Integer32"""
    defaultValue = 2

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
        *(("ldap", 1),
          ("cli", 2),
          ("blt", 3),
          ("api", 4),
          ("imp", 5))
    )


_AlaQoSPortGroupsSource_Type.__name__ = "Integer32"
_AlaQoSPortGroupsSource_Object = MibTableColumn
alaQoSPortGroupsSource = _AlaQoSPortGroupsSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 19, 1, 2),
    _AlaQoSPortGroupsSource_Type()
)
alaQoSPortGroupsSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortGroupsSource.setStatus("current")
_AlaQoSPortGroupsStatus_Type = RowStatus
_AlaQoSPortGroupsStatus_Object = MibTableColumn
alaQoSPortGroupsStatus = _AlaQoSPortGroupsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 19, 1, 3),
    _AlaQoSPortGroupsStatus_Type()
)
alaQoSPortGroupsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortGroupsStatus.setStatus("current")
_AlaQoSAppliedPortGroupsTable_Object = MibTable
alaQoSAppliedPortGroupsTable = _AlaQoSAppliedPortGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 20)
)
if mibBuilder.loadTexts:
    alaQoSAppliedPortGroupsTable.setStatus("current")
_AlaQoSAppliedPortGroupsEntry_Object = MibTableRow
alaQoSAppliedPortGroupsEntry = _AlaQoSAppliedPortGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 20, 1)
)
alaQoSAppliedPortGroupsEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedPortGroupsName"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedPortGroupsEntry.setStatus("current")


class _AlaQoSAppliedPortGroupsName_Type(SnmpAdminString):
    """Custom type alaQoSAppliedPortGroupsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedPortGroupsName_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedPortGroupsName_Object = MibTableColumn
alaQoSAppliedPortGroupsName = _AlaQoSAppliedPortGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 20, 1, 1),
    _AlaQoSAppliedPortGroupsName_Type()
)
alaQoSAppliedPortGroupsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedPortGroupsName.setStatus("current")


class _AlaQoSAppliedPortGroupsSource_Type(Integer32):
    """Custom type alaQoSAppliedPortGroupsSource based on Integer32"""
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
        *(("ldap", 1),
          ("cli", 2),
          ("blt", 3),
          ("api", 4),
          ("imp", 5))
    )


_AlaQoSAppliedPortGroupsSource_Type.__name__ = "Integer32"
_AlaQoSAppliedPortGroupsSource_Object = MibTableColumn
alaQoSAppliedPortGroupsSource = _AlaQoSAppliedPortGroupsSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 20, 1, 2),
    _AlaQoSAppliedPortGroupsSource_Type()
)
alaQoSAppliedPortGroupsSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedPortGroupsSource.setStatus("current")
_AlaQoSAppliedPortGroupsStatus_Type = RowStatus
_AlaQoSAppliedPortGroupsStatus_Object = MibTableColumn
alaQoSAppliedPortGroupsStatus = _AlaQoSAppliedPortGroupsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 20, 1, 3),
    _AlaQoSAppliedPortGroupsStatus_Type()
)
alaQoSAppliedPortGroupsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedPortGroupsStatus.setStatus("current")
_AlaQoSPortGroupTable_Object = MibTable
alaQoSPortGroupTable = _AlaQoSPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 21)
)
if mibBuilder.loadTexts:
    alaQoSPortGroupTable.setStatus("current")
_AlaQoSPortGroupEntry_Object = MibTableRow
alaQoSPortGroupEntry = _AlaQoSPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 21, 1)
)
alaQoSPortGroupEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSPortGroupsName"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSPortGroupSlot"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSPortGroupPort"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSPortGroupPortEnd"),
)
if mibBuilder.loadTexts:
    alaQoSPortGroupEntry.setStatus("current")


class _AlaQoSPortGroupSlot_Type(Integer32):
    """Custom type alaQoSPortGroupSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6016),
    )


_AlaQoSPortGroupSlot_Type.__name__ = "Integer32"
_AlaQoSPortGroupSlot_Object = MibTableColumn
alaQoSPortGroupSlot = _AlaQoSPortGroupSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 21, 1, 1),
    _AlaQoSPortGroupSlot_Type()
)
alaQoSPortGroupSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSPortGroupSlot.setStatus("current")


class _AlaQoSPortGroupPort_Type(Integer32):
    """Custom type alaQoSPortGroupPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSPortGroupPort_Type.__name__ = "Integer32"
_AlaQoSPortGroupPort_Object = MibTableColumn
alaQoSPortGroupPort = _AlaQoSPortGroupPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 21, 1, 2),
    _AlaQoSPortGroupPort_Type()
)
alaQoSPortGroupPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSPortGroupPort.setStatus("current")
_AlaQoSPortGroupStatus_Type = RowStatus
_AlaQoSPortGroupStatus_Object = MibTableColumn
alaQoSPortGroupStatus = _AlaQoSPortGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 21, 1, 3),
    _AlaQoSPortGroupStatus_Type()
)
alaQoSPortGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortGroupStatus.setStatus("current")


class _AlaQoSPortGroupPortEnd_Type(Integer32):
    """Custom type alaQoSPortGroupPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSPortGroupPortEnd_Type.__name__ = "Integer32"
_AlaQoSPortGroupPortEnd_Object = MibTableColumn
alaQoSPortGroupPortEnd = _AlaQoSPortGroupPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 21, 1, 4),
    _AlaQoSPortGroupPortEnd_Type()
)
alaQoSPortGroupPortEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSPortGroupPortEnd.setStatus("current")
_AlaQoSAppliedPortGroupTable_Object = MibTable
alaQoSAppliedPortGroupTable = _AlaQoSAppliedPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 22)
)
if mibBuilder.loadTexts:
    alaQoSAppliedPortGroupTable.setStatus("current")
_AlaQoSAppliedPortGroupEntry_Object = MibTableRow
alaQoSAppliedPortGroupEntry = _AlaQoSAppliedPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 22, 1)
)
alaQoSAppliedPortGroupEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedPortGroupsName"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedPortGroupSlot"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedPortGroupPort"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedPortGroupPortEnd"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedPortGroupEntry.setStatus("current")


class _AlaQoSAppliedPortGroupSlot_Type(Integer32):
    """Custom type alaQoSAppliedPortGroupSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6016),
    )


_AlaQoSAppliedPortGroupSlot_Type.__name__ = "Integer32"
_AlaQoSAppliedPortGroupSlot_Object = MibTableColumn
alaQoSAppliedPortGroupSlot = _AlaQoSAppliedPortGroupSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 22, 1, 1),
    _AlaQoSAppliedPortGroupSlot_Type()
)
alaQoSAppliedPortGroupSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedPortGroupSlot.setStatus("current")


class _AlaQoSAppliedPortGroupPort_Type(Integer32):
    """Custom type alaQoSAppliedPortGroupPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_AlaQoSAppliedPortGroupPort_Type.__name__ = "Integer32"
_AlaQoSAppliedPortGroupPort_Object = MibTableColumn
alaQoSAppliedPortGroupPort = _AlaQoSAppliedPortGroupPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 22, 1, 2),
    _AlaQoSAppliedPortGroupPort_Type()
)
alaQoSAppliedPortGroupPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedPortGroupPort.setStatus("current")
_AlaQoSAppliedPortGroupStatus_Type = RowStatus
_AlaQoSAppliedPortGroupStatus_Object = MibTableColumn
alaQoSAppliedPortGroupStatus = _AlaQoSAppliedPortGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 22, 1, 3),
    _AlaQoSAppliedPortGroupStatus_Type()
)
alaQoSAppliedPortGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedPortGroupStatus.setStatus("current")


class _AlaQoSAppliedPortGroupPortEnd_Type(Integer32):
    """Custom type alaQoSAppliedPortGroupPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_AlaQoSAppliedPortGroupPortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedPortGroupPortEnd_Object = MibTableColumn
alaQoSAppliedPortGroupPortEnd = _AlaQoSAppliedPortGroupPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 22, 1, 4),
    _AlaQoSAppliedPortGroupPortEnd_Type()
)
alaQoSAppliedPortGroupPortEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedPortGroupPortEnd.setStatus("current")
_AlaQoSMapGroupsTable_Object = MibTable
alaQoSMapGroupsTable = _AlaQoSMapGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 23)
)
if mibBuilder.loadTexts:
    alaQoSMapGroupsTable.setStatus("current")
_AlaQoSMapGroupsEntry_Object = MibTableRow
alaQoSMapGroupsEntry = _AlaQoSMapGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 23, 1)
)
alaQoSMapGroupsEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSMapGroupsName"),
)
if mibBuilder.loadTexts:
    alaQoSMapGroupsEntry.setStatus("current")


class _AlaQoSMapGroupsName_Type(SnmpAdminString):
    """Custom type alaQoSMapGroupsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSMapGroupsName_Type.__name__ = "SnmpAdminString"
_AlaQoSMapGroupsName_Object = MibTableColumn
alaQoSMapGroupsName = _AlaQoSMapGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 23, 1, 1),
    _AlaQoSMapGroupsName_Type()
)
alaQoSMapGroupsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSMapGroupsName.setStatus("current")


class _AlaQoSMapGroupsSource_Type(Integer32):
    """Custom type alaQoSMapGroupsSource based on Integer32"""
    defaultValue = 2

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
        *(("ldap", 1),
          ("cli", 2),
          ("blt", 3),
          ("api", 4),
          ("imp", 5))
    )


_AlaQoSMapGroupsSource_Type.__name__ = "Integer32"
_AlaQoSMapGroupsSource_Object = MibTableColumn
alaQoSMapGroupsSource = _AlaQoSMapGroupsSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 23, 1, 2),
    _AlaQoSMapGroupsSource_Type()
)
alaQoSMapGroupsSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSMapGroupsSource.setStatus("current")
_AlaQoSMapGroupsStatus_Type = RowStatus
_AlaQoSMapGroupsStatus_Object = MibTableColumn
alaQoSMapGroupsStatus = _AlaQoSMapGroupsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 23, 1, 3),
    _AlaQoSMapGroupsStatus_Type()
)
alaQoSMapGroupsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSMapGroupsStatus.setStatus("current")
_AlaQoSAppliedMapGroupsTable_Object = MibTable
alaQoSAppliedMapGroupsTable = _AlaQoSAppliedMapGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 24)
)
if mibBuilder.loadTexts:
    alaQoSAppliedMapGroupsTable.setStatus("current")
_AlaQoSAppliedMapGroupsEntry_Object = MibTableRow
alaQoSAppliedMapGroupsEntry = _AlaQoSAppliedMapGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 24, 1)
)
alaQoSAppliedMapGroupsEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedMapGroupsName"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedMapGroupsEntry.setStatus("current")


class _AlaQoSAppliedMapGroupsName_Type(SnmpAdminString):
    """Custom type alaQoSAppliedMapGroupsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedMapGroupsName_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedMapGroupsName_Object = MibTableColumn
alaQoSAppliedMapGroupsName = _AlaQoSAppliedMapGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 24, 1, 1),
    _AlaQoSAppliedMapGroupsName_Type()
)
alaQoSAppliedMapGroupsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedMapGroupsName.setStatus("current")


class _AlaQoSAppliedMapGroupsSource_Type(Integer32):
    """Custom type alaQoSAppliedMapGroupsSource based on Integer32"""
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
        *(("ldap", 1),
          ("cli", 2),
          ("blt", 3),
          ("api", 4),
          ("imp", 5))
    )


_AlaQoSAppliedMapGroupsSource_Type.__name__ = "Integer32"
_AlaQoSAppliedMapGroupsSource_Object = MibTableColumn
alaQoSAppliedMapGroupsSource = _AlaQoSAppliedMapGroupsSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 24, 1, 2),
    _AlaQoSAppliedMapGroupsSource_Type()
)
alaQoSAppliedMapGroupsSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedMapGroupsSource.setStatus("current")
_AlaQoSAppliedMapGroupsStatus_Type = RowStatus
_AlaQoSAppliedMapGroupsStatus_Object = MibTableColumn
alaQoSAppliedMapGroupsStatus = _AlaQoSAppliedMapGroupsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 24, 1, 3),
    _AlaQoSAppliedMapGroupsStatus_Type()
)
alaQoSAppliedMapGroupsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedMapGroupsStatus.setStatus("current")
_AlaQoSMapGroupTable_Object = MibTable
alaQoSMapGroupTable = _AlaQoSMapGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 25)
)
if mibBuilder.loadTexts:
    alaQoSMapGroupTable.setStatus("current")
_AlaQoSMapGroupEntry_Object = MibTableRow
alaQoSMapGroupEntry = _AlaQoSMapGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 25, 1)
)
alaQoSMapGroupEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSMapGroupsName"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSMapGroupKey"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSMapGroupKeyEnd"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSMapGroupValue"),
)
if mibBuilder.loadTexts:
    alaQoSMapGroupEntry.setStatus("current")


class _AlaQoSMapGroupKey_Type(Integer32):
    """Custom type alaQoSMapGroupKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSMapGroupKey_Type.__name__ = "Integer32"
_AlaQoSMapGroupKey_Object = MibTableColumn
alaQoSMapGroupKey = _AlaQoSMapGroupKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 25, 1, 1),
    _AlaQoSMapGroupKey_Type()
)
alaQoSMapGroupKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSMapGroupKey.setStatus("current")


class _AlaQoSMapGroupKeyEnd_Type(Integer32):
    """Custom type alaQoSMapGroupKeyEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSMapGroupKeyEnd_Type.__name__ = "Integer32"
_AlaQoSMapGroupKeyEnd_Object = MibTableColumn
alaQoSMapGroupKeyEnd = _AlaQoSMapGroupKeyEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 25, 1, 2),
    _AlaQoSMapGroupKeyEnd_Type()
)
alaQoSMapGroupKeyEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSMapGroupKeyEnd.setStatus("current")


class _AlaQoSMapGroupValue_Type(Integer32):
    """Custom type alaQoSMapGroupValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSMapGroupValue_Type.__name__ = "Integer32"
_AlaQoSMapGroupValue_Object = MibTableColumn
alaQoSMapGroupValue = _AlaQoSMapGroupValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 25, 1, 3),
    _AlaQoSMapGroupValue_Type()
)
alaQoSMapGroupValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSMapGroupValue.setStatus("current")
_AlaQoSMapGroupStatus_Type = RowStatus
_AlaQoSMapGroupStatus_Object = MibTableColumn
alaQoSMapGroupStatus = _AlaQoSMapGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 25, 1, 4),
    _AlaQoSMapGroupStatus_Type()
)
alaQoSMapGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSMapGroupStatus.setStatus("current")
_AlaQoSAppliedMapGroupTable_Object = MibTable
alaQoSAppliedMapGroupTable = _AlaQoSAppliedMapGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 26)
)
if mibBuilder.loadTexts:
    alaQoSAppliedMapGroupTable.setStatus("current")
_AlaQoSAppliedMapGroupEntry_Object = MibTableRow
alaQoSAppliedMapGroupEntry = _AlaQoSAppliedMapGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 26, 1)
)
alaQoSAppliedMapGroupEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedMapGroupsName"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedMapGroupKey"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedMapGroupKeyEnd"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedMapGroupValue"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedMapGroupEntry.setStatus("current")


class _AlaQoSAppliedMapGroupKey_Type(Integer32):
    """Custom type alaQoSAppliedMapGroupKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSAppliedMapGroupKey_Type.__name__ = "Integer32"
_AlaQoSAppliedMapGroupKey_Object = MibTableColumn
alaQoSAppliedMapGroupKey = _AlaQoSAppliedMapGroupKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 26, 1, 1),
    _AlaQoSAppliedMapGroupKey_Type()
)
alaQoSAppliedMapGroupKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedMapGroupKey.setStatus("current")


class _AlaQoSAppliedMapGroupKeyEnd_Type(Integer32):
    """Custom type alaQoSAppliedMapGroupKeyEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSAppliedMapGroupKeyEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedMapGroupKeyEnd_Object = MibTableColumn
alaQoSAppliedMapGroupKeyEnd = _AlaQoSAppliedMapGroupKeyEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 26, 1, 2),
    _AlaQoSAppliedMapGroupKeyEnd_Type()
)
alaQoSAppliedMapGroupKeyEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedMapGroupKeyEnd.setStatus("current")


class _AlaQoSAppliedMapGroupValue_Type(Integer32):
    """Custom type alaQoSAppliedMapGroupValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSAppliedMapGroupValue_Type.__name__ = "Integer32"
_AlaQoSAppliedMapGroupValue_Object = MibTableColumn
alaQoSAppliedMapGroupValue = _AlaQoSAppliedMapGroupValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 26, 1, 3),
    _AlaQoSAppliedMapGroupValue_Type()
)
alaQoSAppliedMapGroupValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedMapGroupValue.setStatus("current")
_AlaQoSAppliedMapGroupStatus_Type = RowStatus
_AlaQoSAppliedMapGroupStatus_Object = MibTableColumn
alaQoSAppliedMapGroupStatus = _AlaQoSAppliedMapGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 26, 1, 4),
    _AlaQoSAppliedMapGroupStatus_Type()
)
alaQoSAppliedMapGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedMapGroupStatus.setStatus("current")
_AlaQoSActionTable_Object = MibTable
alaQoSActionTable = _AlaQoSActionTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27)
)
if mibBuilder.loadTexts:
    alaQoSActionTable.setStatus("current")
_AlaQoSActionEntry_Object = MibTableRow
alaQoSActionEntry = _AlaQoSActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1)
)
alaQoSActionEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSActionName"),
)
if mibBuilder.loadTexts:
    alaQoSActionEntry.setStatus("current")


class _AlaQoSActionName_Type(SnmpAdminString):
    """Custom type alaQoSActionName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSActionName_Type.__name__ = "SnmpAdminString"
_AlaQoSActionName_Object = MibTableColumn
alaQoSActionName = _AlaQoSActionName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 1),
    _AlaQoSActionName_Type()
)
alaQoSActionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSActionName.setStatus("current")


class _AlaQoSActionSource_Type(Integer32):
    """Custom type alaQoSActionSource based on Integer32"""
    defaultValue = 2

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
        *(("ldap", 1),
          ("cli", 2),
          ("blt", 3),
          ("api", 4),
          ("imp", 5))
    )


_AlaQoSActionSource_Type.__name__ = "Integer32"
_AlaQoSActionSource_Object = MibTableColumn
alaQoSActionSource = _AlaQoSActionSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 2),
    _AlaQoSActionSource_Type()
)
alaQoSActionSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionSource.setStatus("current")


class _AlaQoSActionDisposition_Type(Integer32):
    """Custom type alaQoSActionDisposition based on Integer32"""
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
        *(("accept", 1),
          ("drop", 2),
          ("deny", 3))
    )


_AlaQoSActionDisposition_Type.__name__ = "Integer32"
_AlaQoSActionDisposition_Object = MibTableColumn
alaQoSActionDisposition = _AlaQoSActionDisposition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 3),
    _AlaQoSActionDisposition_Type()
)
alaQoSActionDisposition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionDisposition.setStatus("current")


class _AlaQoSActionMaximumBandwidth_Type(Integer32):
    """Custom type alaQoSActionMaximumBandwidth based on Integer32"""
    defaultValue = 0


_AlaQoSActionMaximumBandwidth_Type.__name__ = "Integer32"
_AlaQoSActionMaximumBandwidth_Object = MibTableColumn
alaQoSActionMaximumBandwidth = _AlaQoSActionMaximumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 4),
    _AlaQoSActionMaximumBandwidth_Type()
)
alaQoSActionMaximumBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMaximumBandwidth.setStatus("current")


class _AlaQoSActionMaximumBandwidthStatus_Type(Integer32):
    """Custom type alaQoSActionMaximumBandwidthStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSActionMaximumBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSActionMaximumBandwidthStatus_Object = MibTableColumn
alaQoSActionMaximumBandwidthStatus = _AlaQoSActionMaximumBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 5),
    _AlaQoSActionMaximumBandwidthStatus_Type()
)
alaQoSActionMaximumBandwidthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMaximumBandwidthStatus.setStatus("current")


class _AlaQoSActionPriority_Type(Integer32):
    """Custom type alaQoSActionPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_AlaQoSActionPriority_Type.__name__ = "Integer32"
_AlaQoSActionPriority_Object = MibTableColumn
alaQoSActionPriority = _AlaQoSActionPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 6),
    _AlaQoSActionPriority_Type()
)
alaQoSActionPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionPriority.setStatus("current")


class _AlaQoSActionPriorityStatus_Type(Integer32):
    """Custom type alaQoSActionPriorityStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSActionPriorityStatus_Type.__name__ = "Integer32"
_AlaQoSActionPriorityStatus_Object = MibTableColumn
alaQoSActionPriorityStatus = _AlaQoSActionPriorityStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 7),
    _AlaQoSActionPriorityStatus_Type()
)
alaQoSActionPriorityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionPriorityStatus.setStatus("current")


class _AlaQoSActionShared_Type(Integer32):
    """Custom type alaQoSActionShared based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSActionShared_Type.__name__ = "Integer32"
_AlaQoSActionShared_Object = MibTableColumn
alaQoSActionShared = _AlaQoSActionShared_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 8),
    _AlaQoSActionShared_Type()
)
alaQoSActionShared.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionShared.setStatus("current")


class _AlaQoSActionMaximumDepth_Type(Integer32):
    """Custom type alaQoSActionMaximumDepth based on Integer32"""
    defaultValue = 0


_AlaQoSActionMaximumDepth_Type.__name__ = "Integer32"
_AlaQoSActionMaximumDepth_Object = MibTableColumn
alaQoSActionMaximumDepth = _AlaQoSActionMaximumDepth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 9),
    _AlaQoSActionMaximumDepth_Type()
)
alaQoSActionMaximumDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMaximumDepth.setStatus("current")


class _AlaQoSActionMaximumDepthStatus_Type(Integer32):
    """Custom type alaQoSActionMaximumDepthStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSActionMaximumDepthStatus_Type.__name__ = "Integer32"
_AlaQoSActionMaximumDepthStatus_Object = MibTableColumn
alaQoSActionMaximumDepthStatus = _AlaQoSActionMaximumDepthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 10),
    _AlaQoSActionMaximumDepthStatus_Type()
)
alaQoSActionMaximumDepthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMaximumDepthStatus.setStatus("current")


class _AlaQoSAction8021p_Type(Integer32):
    """Custom type alaQoSAction8021p based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSAction8021p_Type.__name__ = "Integer32"
_AlaQoSAction8021p_Object = MibTableColumn
alaQoSAction8021p = _AlaQoSAction8021p_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 11),
    _AlaQoSAction8021p_Type()
)
alaQoSAction8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAction8021p.setStatus("current")


class _AlaQoSAction8021pStatus_Type(Integer32):
    """Custom type alaQoSAction8021pStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSAction8021pStatus_Type.__name__ = "Integer32"
_AlaQoSAction8021pStatus_Object = MibTableColumn
alaQoSAction8021pStatus = _AlaQoSAction8021pStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 12),
    _AlaQoSAction8021pStatus_Type()
)
alaQoSAction8021pStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAction8021pStatus.setStatus("current")


class _AlaQoSActionTos_Type(Integer32):
    """Custom type alaQoSActionTos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSActionTos_Type.__name__ = "Integer32"
_AlaQoSActionTos_Object = MibTableColumn
alaQoSActionTos = _AlaQoSActionTos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 13),
    _AlaQoSActionTos_Type()
)
alaQoSActionTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionTos.setStatus("current")


class _AlaQoSActionTosStatus_Type(Integer32):
    """Custom type alaQoSActionTosStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSActionTosStatus_Type.__name__ = "Integer32"
_AlaQoSActionTosStatus_Object = MibTableColumn
alaQoSActionTosStatus = _AlaQoSActionTosStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 14),
    _AlaQoSActionTosStatus_Type()
)
alaQoSActionTosStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionTosStatus.setStatus("current")


class _AlaQoSActionDscp_Type(Integer32):
    """Custom type alaQoSActionDscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSActionDscp_Type.__name__ = "Integer32"
_AlaQoSActionDscp_Object = MibTableColumn
alaQoSActionDscp = _AlaQoSActionDscp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 15),
    _AlaQoSActionDscp_Type()
)
alaQoSActionDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionDscp.setStatus("current")


class _AlaQoSActionDscpStatus_Type(Integer32):
    """Custom type alaQoSActionDscpStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSActionDscpStatus_Type.__name__ = "Integer32"
_AlaQoSActionDscpStatus_Object = MibTableColumn
alaQoSActionDscpStatus = _AlaQoSActionDscpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 16),
    _AlaQoSActionDscpStatus_Type()
)
alaQoSActionDscpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionDscpStatus.setStatus("current")


class _AlaQoSActionMapFrom_Type(Integer32):
    """Custom type alaQoSActionMapFrom based on Integer32"""
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
        *(("b8021p", 1),
          ("tos", 2),
          ("dscp", 3))
    )


_AlaQoSActionMapFrom_Type.__name__ = "Integer32"
_AlaQoSActionMapFrom_Object = MibTableColumn
alaQoSActionMapFrom = _AlaQoSActionMapFrom_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 17),
    _AlaQoSActionMapFrom_Type()
)
alaQoSActionMapFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMapFrom.setStatus("current")


class _AlaQoSActionMapTo_Type(Integer32):
    """Custom type alaQoSActionMapTo based on Integer32"""
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
        *(("b8021p", 1),
          ("tos", 2),
          ("dscp", 3))
    )


_AlaQoSActionMapTo_Type.__name__ = "Integer32"
_AlaQoSActionMapTo_Object = MibTableColumn
alaQoSActionMapTo = _AlaQoSActionMapTo_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 18),
    _AlaQoSActionMapTo_Type()
)
alaQoSActionMapTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMapTo.setStatus("current")


class _AlaQoSActionMapGroup_Type(SnmpAdminString):
    """Custom type alaQoSActionMapGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSActionMapGroup_Type.__name__ = "SnmpAdminString"
_AlaQoSActionMapGroup_Object = MibTableColumn
alaQoSActionMapGroup = _AlaQoSActionMapGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 19),
    _AlaQoSActionMapGroup_Type()
)
alaQoSActionMapGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMapGroup.setStatus("current")


class _AlaQoSActionMapGroupStatus_Type(Integer32):
    """Custom type alaQoSActionMapGroupStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSActionMapGroupStatus_Type.__name__ = "Integer32"
_AlaQoSActionMapGroupStatus_Object = MibTableColumn
alaQoSActionMapGroupStatus = _AlaQoSActionMapGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 20),
    _AlaQoSActionMapGroupStatus_Type()
)
alaQoSActionMapGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMapGroupStatus.setStatus("current")


class _AlaQoSActionLoadBalanceGroup_Type(SnmpAdminString):
    """Custom type alaQoSActionLoadBalanceGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_AlaQoSActionLoadBalanceGroup_Type.__name__ = "SnmpAdminString"
_AlaQoSActionLoadBalanceGroup_Object = MibTableColumn
alaQoSActionLoadBalanceGroup = _AlaQoSActionLoadBalanceGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 21),
    _AlaQoSActionLoadBalanceGroup_Type()
)
alaQoSActionLoadBalanceGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionLoadBalanceGroup.setStatus("current")


class _AlaQoSActionLoadBalanceGroupStatus_Type(Integer32):
    """Custom type alaQoSActionLoadBalanceGroupStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSActionLoadBalanceGroupStatus_Type.__name__ = "Integer32"
_AlaQoSActionLoadBalanceGroupStatus_Object = MibTableColumn
alaQoSActionLoadBalanceGroupStatus = _AlaQoSActionLoadBalanceGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 22),
    _AlaQoSActionLoadBalanceGroupStatus_Type()
)
alaQoSActionLoadBalanceGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionLoadBalanceGroupStatus.setStatus("current")


class _AlaQoSActionPermanentGatewayIpAddr_Type(IpAddress):
    """Custom type alaQoSActionPermanentGatewayIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AlaQoSActionPermanentGatewayIpAddr_Type.__name__ = "IpAddress"
_AlaQoSActionPermanentGatewayIpAddr_Object = MibTableColumn
alaQoSActionPermanentGatewayIpAddr = _AlaQoSActionPermanentGatewayIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 23),
    _AlaQoSActionPermanentGatewayIpAddr_Type()
)
alaQoSActionPermanentGatewayIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionPermanentGatewayIpAddr.setStatus("current")


class _AlaQoSActionPermanentGatewayIpAddrStatus_Type(Integer32):
    """Custom type alaQoSActionPermanentGatewayIpAddrStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSActionPermanentGatewayIpAddrStatus_Type.__name__ = "Integer32"
_AlaQoSActionPermanentGatewayIpAddrStatus_Object = MibTableColumn
alaQoSActionPermanentGatewayIpAddrStatus = _AlaQoSActionPermanentGatewayIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 24),
    _AlaQoSActionPermanentGatewayIpAddrStatus_Type()
)
alaQoSActionPermanentGatewayIpAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionPermanentGatewayIpAddrStatus.setStatus("current")


class _AlaQoSActionAlternateGatewayIpAddr_Type(IpAddress):
    """Custom type alaQoSActionAlternateGatewayIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AlaQoSActionAlternateGatewayIpAddr_Type.__name__ = "IpAddress"
_AlaQoSActionAlternateGatewayIpAddr_Object = MibTableColumn
alaQoSActionAlternateGatewayIpAddr = _AlaQoSActionAlternateGatewayIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 25),
    _AlaQoSActionAlternateGatewayIpAddr_Type()
)
alaQoSActionAlternateGatewayIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionAlternateGatewayIpAddr.setStatus("current")


class _AlaQoSActionAlternateGatewayIpAddrStatus_Type(Integer32):
    """Custom type alaQoSActionAlternateGatewayIpAddrStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSActionAlternateGatewayIpAddrStatus_Type.__name__ = "Integer32"
_AlaQoSActionAlternateGatewayIpAddrStatus_Object = MibTableColumn
alaQoSActionAlternateGatewayIpAddrStatus = _AlaQoSActionAlternateGatewayIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 26),
    _AlaQoSActionAlternateGatewayIpAddrStatus_Type()
)
alaQoSActionAlternateGatewayIpAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionAlternateGatewayIpAddrStatus.setStatus("current")
_AlaQoSActionRowStatus_Type = RowStatus
_AlaQoSActionRowStatus_Object = MibTableColumn
alaQoSActionRowStatus = _AlaQoSActionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 27),
    _AlaQoSActionRowStatus_Type()
)
alaQoSActionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionRowStatus.setStatus("current")


class _AlaQoSActionNocache_Type(Integer32):
    """Custom type alaQoSActionNocache based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSActionNocache_Type.__name__ = "Integer32"
_AlaQoSActionNocache_Object = MibTableColumn
alaQoSActionNocache = _AlaQoSActionNocache_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 28),
    _AlaQoSActionNocache_Type()
)
alaQoSActionNocache.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionNocache.setStatus("current")


class _AlaQoSActionPortdisable_Type(Integer32):
    """Custom type alaQoSActionPortdisable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSActionPortdisable_Type.__name__ = "Integer32"
_AlaQoSActionPortdisable_Object = MibTableColumn
alaQoSActionPortdisable = _AlaQoSActionPortdisable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 29),
    _AlaQoSActionPortdisable_Type()
)
alaQoSActionPortdisable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionPortdisable.setStatus("current")


class _AlaQoSActionRedirectSlot_Type(Integer32):
    """Custom type alaQoSActionRedirectSlot based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSActionRedirectSlot_Type.__name__ = "Integer32"
_AlaQoSActionRedirectSlot_Object = MibTableColumn
alaQoSActionRedirectSlot = _AlaQoSActionRedirectSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 30),
    _AlaQoSActionRedirectSlot_Type()
)
alaQoSActionRedirectSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionRedirectSlot.setStatus("current")


class _AlaQoSActionRedirectSlotStatus_Type(Integer32):
    """Custom type alaQoSActionRedirectSlotStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSActionRedirectSlotStatus_Type.__name__ = "Integer32"
_AlaQoSActionRedirectSlotStatus_Object = MibTableColumn
alaQoSActionRedirectSlotStatus = _AlaQoSActionRedirectSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 31),
    _AlaQoSActionRedirectSlotStatus_Type()
)
alaQoSActionRedirectSlotStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionRedirectSlotStatus.setStatus("current")


class _AlaQoSActionRedirectPort_Type(Integer32):
    """Custom type alaQoSActionRedirectPort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_AlaQoSActionRedirectPort_Type.__name__ = "Integer32"
_AlaQoSActionRedirectPort_Object = MibTableColumn
alaQoSActionRedirectPort = _AlaQoSActionRedirectPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 32),
    _AlaQoSActionRedirectPort_Type()
)
alaQoSActionRedirectPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionRedirectPort.setStatus("current")


class _AlaQoSActionRedirectAgg_Type(Integer32):
    """Custom type alaQoSActionRedirectAgg based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AlaQoSActionRedirectAgg_Type.__name__ = "Integer32"
_AlaQoSActionRedirectAgg_Object = MibTableColumn
alaQoSActionRedirectAgg = _AlaQoSActionRedirectAgg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 33),
    _AlaQoSActionRedirectAgg_Type()
)
alaQoSActionRedirectAgg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionRedirectAgg.setStatus("current")


class _AlaQoSActionRedirectAggStatus_Type(Integer32):
    """Custom type alaQoSActionRedirectAggStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSActionRedirectAggStatus_Type.__name__ = "Integer32"
_AlaQoSActionRedirectAggStatus_Object = MibTableColumn
alaQoSActionRedirectAggStatus = _AlaQoSActionRedirectAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 34),
    _AlaQoSActionRedirectAggStatus_Type()
)
alaQoSActionRedirectAggStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionRedirectAggStatus.setStatus("current")


class _AlaQoSActionMirrorSlot_Type(Integer32):
    """Custom type alaQoSActionMirrorSlot based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSActionMirrorSlot_Type.__name__ = "Integer32"
_AlaQoSActionMirrorSlot_Object = MibTableColumn
alaQoSActionMirrorSlot = _AlaQoSActionMirrorSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 35),
    _AlaQoSActionMirrorSlot_Type()
)
alaQoSActionMirrorSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMirrorSlot.setStatus("current")


class _AlaQoSActionMirrorPort_Type(Integer32):
    """Custom type alaQoSActionMirrorPort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_AlaQoSActionMirrorPort_Type.__name__ = "Integer32"
_AlaQoSActionMirrorPort_Object = MibTableColumn
alaQoSActionMirrorPort = _AlaQoSActionMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 36),
    _AlaQoSActionMirrorPort_Type()
)
alaQoSActionMirrorPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMirrorPort.setStatus("current")


class _AlaQoSActionMirrorMode_Type(Integer32):
    """Custom type alaQoSActionMirrorMode based on Integer32"""
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
        *(("ingress", 1),
          ("egress", 2),
          ("both", 3))
    )


_AlaQoSActionMirrorMode_Type.__name__ = "Integer32"
_AlaQoSActionMirrorMode_Object = MibTableColumn
alaQoSActionMirrorMode = _AlaQoSActionMirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 37),
    _AlaQoSActionMirrorMode_Type()
)
alaQoSActionMirrorMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMirrorMode.setStatus("current")


class _AlaQoSActionMirrorModeStatus_Type(Integer32):
    """Custom type alaQoSActionMirrorModeStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSActionMirrorModeStatus_Type.__name__ = "Integer32"
_AlaQoSActionMirrorModeStatus_Object = MibTableColumn
alaQoSActionMirrorModeStatus = _AlaQoSActionMirrorModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 38),
    _AlaQoSActionMirrorModeStatus_Type()
)
alaQoSActionMirrorModeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMirrorModeStatus.setStatus("current")


class _AlaQoSActionCIR_Type(Integer32):
    """Custom type alaQoSActionCIR based on Integer32"""
    defaultValue = 0


_AlaQoSActionCIR_Type.__name__ = "Integer32"
_AlaQoSActionCIR_Object = MibTableColumn
alaQoSActionCIR = _AlaQoSActionCIR_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 39),
    _AlaQoSActionCIR_Type()
)
alaQoSActionCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionCIR.setStatus("current")
if mibBuilder.loadTexts:
    alaQoSActionCIR.setUnits("kilobits per second")


class _AlaQoSActionCIRStatus_Type(Integer32):
    """Custom type alaQoSActionCIRStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSActionCIRStatus_Type.__name__ = "Integer32"
_AlaQoSActionCIRStatus_Object = MibTableColumn
alaQoSActionCIRStatus = _AlaQoSActionCIRStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 40),
    _AlaQoSActionCIRStatus_Type()
)
alaQoSActionCIRStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionCIRStatus.setStatus("current")


class _AlaQoSActionCBS_Type(Integer32):
    """Custom type alaQoSActionCBS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147450880),
    )


_AlaQoSActionCBS_Type.__name__ = "Integer32"
_AlaQoSActionCBS_Object = MibTableColumn
alaQoSActionCBS = _AlaQoSActionCBS_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 41),
    _AlaQoSActionCBS_Type()
)
alaQoSActionCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionCBS.setStatus("current")


class _AlaQoSActionCBSStatus_Type(Integer32):
    """Custom type alaQoSActionCBSStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSActionCBSStatus_Type.__name__ = "Integer32"
_AlaQoSActionCBSStatus_Object = MibTableColumn
alaQoSActionCBSStatus = _AlaQoSActionCBSStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 42),
    _AlaQoSActionCBSStatus_Type()
)
alaQoSActionCBSStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionCBSStatus.setStatus("current")


class _AlaQoSActionPIR_Type(Integer32):
    """Custom type alaQoSActionPIR based on Integer32"""
    defaultValue = 0


_AlaQoSActionPIR_Type.__name__ = "Integer32"
_AlaQoSActionPIR_Object = MibTableColumn
alaQoSActionPIR = _AlaQoSActionPIR_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 43),
    _AlaQoSActionPIR_Type()
)
alaQoSActionPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionPIR.setStatus("current")
if mibBuilder.loadTexts:
    alaQoSActionPIR.setUnits("kilobits per second")


class _AlaQoSActionPIRStatus_Type(Integer32):
    """Custom type alaQoSActionPIRStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSActionPIRStatus_Type.__name__ = "Integer32"
_AlaQoSActionPIRStatus_Object = MibTableColumn
alaQoSActionPIRStatus = _AlaQoSActionPIRStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 44),
    _AlaQoSActionPIRStatus_Type()
)
alaQoSActionPIRStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionPIRStatus.setStatus("current")


class _AlaQoSActionPBS_Type(Integer32):
    """Custom type alaQoSActionPBS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147450880),
    )


_AlaQoSActionPBS_Type.__name__ = "Integer32"
_AlaQoSActionPBS_Object = MibTableColumn
alaQoSActionPBS = _AlaQoSActionPBS_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 45),
    _AlaQoSActionPBS_Type()
)
alaQoSActionPBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionPBS.setStatus("current")


class _AlaQoSActionPBSStatus_Type(Integer32):
    """Custom type alaQoSActionPBSStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSActionPBSStatus_Type.__name__ = "Integer32"
_AlaQoSActionPBSStatus_Object = MibTableColumn
alaQoSActionPBSStatus = _AlaQoSActionPBSStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 46),
    _AlaQoSActionPBSStatus_Type()
)
alaQoSActionPBSStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionPBSStatus.setStatus("current")


class _AlaQoSActionCPUPriority_Type(Integer32):
    """Custom type alaQoSActionCPUPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSActionCPUPriority_Type.__name__ = "Integer32"
_AlaQoSActionCPUPriority_Object = MibTableColumn
alaQoSActionCPUPriority = _AlaQoSActionCPUPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 47),
    _AlaQoSActionCPUPriority_Type()
)
alaQoSActionCPUPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionCPUPriority.setStatus("current")


class _AlaQoSActionCPUPriorityStatus_Type(Integer32):
    """Custom type alaQoSActionCPUPriorityStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSActionCPUPriorityStatus_Type.__name__ = "Integer32"
_AlaQoSActionCPUPriorityStatus_Object = MibTableColumn
alaQoSActionCPUPriorityStatus = _AlaQoSActionCPUPriorityStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 48),
    _AlaQoSActionCPUPriorityStatus_Type()
)
alaQoSActionCPUPriorityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionCPUPriorityStatus.setStatus("current")


class _AlaQoSActionColorOnly_Type(Integer32):
    """Custom type alaQoSActionColorOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSActionColorOnly_Type.__name__ = "Integer32"
_AlaQoSActionColorOnly_Object = MibTableColumn
alaQoSActionColorOnly = _AlaQoSActionColorOnly_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 49),
    _AlaQoSActionColorOnly_Type()
)
alaQoSActionColorOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionColorOnly.setStatus("current")


class _AlaQoSActionRedirectChassis_Type(Integer32):
    """Custom type alaQoSActionRedirectChassis based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSActionRedirectChassis_Type.__name__ = "Integer32"
_AlaQoSActionRedirectChassis_Object = MibTableColumn
alaQoSActionRedirectChassis = _AlaQoSActionRedirectChassis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 50),
    _AlaQoSActionRedirectChassis_Type()
)
alaQoSActionRedirectChassis.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionRedirectChassis.setStatus("current")


class _AlaQoSActionMirrorChassis_Type(Integer32):
    """Custom type alaQoSActionMirrorChassis based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSActionMirrorChassis_Type.__name__ = "Integer32"
_AlaQoSActionMirrorChassis_Object = MibTableColumn
alaQoSActionMirrorChassis = _AlaQoSActionMirrorChassis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 51),
    _AlaQoSActionMirrorChassis_Type()
)
alaQoSActionMirrorChassis.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMirrorChassis.setStatus("current")


class _AlaQoSActionPermanentGatewayIpV6Addr_Type(Ipv6Address):
    """Custom type alaQoSActionPermanentGatewayIpV6Addr based on Ipv6Address"""
    defaultHexValue = "00000000000000000000000000000000"


_AlaQoSActionPermanentGatewayIpV6Addr_Type.__name__ = "Ipv6Address"
_AlaQoSActionPermanentGatewayIpV6Addr_Object = MibTableColumn
alaQoSActionPermanentGatewayIpV6Addr = _AlaQoSActionPermanentGatewayIpV6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 52),
    _AlaQoSActionPermanentGatewayIpV6Addr_Type()
)
alaQoSActionPermanentGatewayIpV6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionPermanentGatewayIpV6Addr.setStatus("current")


class _AlaQoSActionPermanentGatewayIpV6AddrStatus_Type(Integer32):
    """Custom type alaQoSActionPermanentGatewayIpV6AddrStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSActionPermanentGatewayIpV6AddrStatus_Type.__name__ = "Integer32"
_AlaQoSActionPermanentGatewayIpV6AddrStatus_Object = MibTableColumn
alaQoSActionPermanentGatewayIpV6AddrStatus = _AlaQoSActionPermanentGatewayIpV6AddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 53),
    _AlaQoSActionPermanentGatewayIpV6AddrStatus_Type()
)
alaQoSActionPermanentGatewayIpV6AddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionPermanentGatewayIpV6AddrStatus.setStatus("current")


class _AlaQoSActionPermanentGatewayIpV6IfIndex_Type(Ipv6IfIndexOrZero):
    """Custom type alaQoSActionPermanentGatewayIpV6IfIndex based on Ipv6IfIndexOrZero"""
    defaultValue = 0


_AlaQoSActionPermanentGatewayIpV6IfIndex_Type.__name__ = "Ipv6IfIndexOrZero"
_AlaQoSActionPermanentGatewayIpV6IfIndex_Object = MibTableColumn
alaQoSActionPermanentGatewayIpV6IfIndex = _AlaQoSActionPermanentGatewayIpV6IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 54),
    _AlaQoSActionPermanentGatewayIpV6IfIndex_Type()
)
alaQoSActionPermanentGatewayIpV6IfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionPermanentGatewayIpV6IfIndex.setStatus("current")


class _AlaQoSActionRTCPMonitor_Type(Integer32):
    """Custom type alaQoSActionRTCPMonitor based on Integer32"""
    defaultValue = 1

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


_AlaQoSActionRTCPMonitor_Type.__name__ = "Integer32"
_AlaQoSActionRTCPMonitor_Object = MibTableColumn
alaQoSActionRTCPMonitor = _AlaQoSActionRTCPMonitor_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 55),
    _AlaQoSActionRTCPMonitor_Type()
)
alaQoSActionRTCPMonitor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionRTCPMonitor.setStatus("current")


class _AlaQoSActionRTCPMonitorStatus_Type(Integer32):
    """Custom type alaQoSActionRTCPMonitorStatus based on Integer32"""
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


_AlaQoSActionRTCPMonitorStatus_Type.__name__ = "Integer32"
_AlaQoSActionRTCPMonitorStatus_Object = MibTableColumn
alaQoSActionRTCPMonitorStatus = _AlaQoSActionRTCPMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 56),
    _AlaQoSActionRTCPMonitorStatus_Type()
)
alaQoSActionRTCPMonitorStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionRTCPMonitorStatus.setStatus("current")
_AlaQoSActionRTCPDSCP_Type = Integer32
_AlaQoSActionRTCPDSCP_Object = MibTableColumn
alaQoSActionRTCPDSCP = _AlaQoSActionRTCPDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 57),
    _AlaQoSActionRTCPDSCP_Type()
)
alaQoSActionRTCPDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionRTCPDSCP.setStatus("current")


class _AlaQoSActionRTCPDSCPStatus_Type(Integer32):
    """Custom type alaQoSActionRTCPDSCPStatus based on Integer32"""
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


_AlaQoSActionRTCPDSCPStatus_Type.__name__ = "Integer32"
_AlaQoSActionRTCPDSCPStatus_Object = MibTableColumn
alaQoSActionRTCPDSCPStatus = _AlaQoSActionRTCPDSCPStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 58),
    _AlaQoSActionRTCPDSCPStatus_Type()
)
alaQoSActionRTCPDSCPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionRTCPDSCPStatus.setStatus("current")


class _AlaQoSActionTrustDSCP_Type(Integer32):
    """Custom type alaQoSActionTrustDSCP based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSActionTrustDSCP_Type.__name__ = "Integer32"
_AlaQoSActionTrustDSCP_Object = MibTableColumn
alaQoSActionTrustDSCP = _AlaQoSActionTrustDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 59),
    _AlaQoSActionTrustDSCP_Type()
)
alaQoSActionTrustDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionTrustDSCP.setStatus("current")


class _AlaQoSActionTrustDSCPStatus_Type(Integer32):
    """Custom type alaQoSActionTrustDSCPStatus based on Integer32"""
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


_AlaQoSActionTrustDSCPStatus_Type.__name__ = "Integer32"
_AlaQoSActionTrustDSCPStatus_Object = MibTableColumn
alaQoSActionTrustDSCPStatus = _AlaQoSActionTrustDSCPStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 60),
    _AlaQoSActionTrustDSCPStatus_Type()
)
alaQoSActionTrustDSCPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionTrustDSCPStatus.setStatus("current")


class _AlaQoSActionRedirectModule_Type(Integer32):
    """Custom type alaQoSActionRedirectModule based on Integer32"""
    defaultValue = 0

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
        *(("none", 0),
          ("qmr", 1),
          ("captivePortal", 2),
          ("unauthorized", 3),
          ("byod", 4))
    )


_AlaQoSActionRedirectModule_Type.__name__ = "Integer32"
_AlaQoSActionRedirectModule_Object = MibTableColumn
alaQoSActionRedirectModule = _AlaQoSActionRedirectModule_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 61),
    _AlaQoSActionRedirectModule_Type()
)
alaQoSActionRedirectModule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionRedirectModule.setStatus("current")
_AlaQoSAppliedActionTable_Object = MibTable
alaQoSAppliedActionTable = _AlaQoSAppliedActionTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28)
)
if mibBuilder.loadTexts:
    alaQoSAppliedActionTable.setStatus("current")
_AlaQoSAppliedActionEntry_Object = MibTableRow
alaQoSAppliedActionEntry = _AlaQoSAppliedActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1)
)
alaQoSAppliedActionEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionName"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedActionEntry.setStatus("current")


class _AlaQoSAppliedActionName_Type(SnmpAdminString):
    """Custom type alaQoSAppliedActionName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedActionName_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedActionName_Object = MibTableColumn
alaQoSAppliedActionName = _AlaQoSAppliedActionName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 1),
    _AlaQoSAppliedActionName_Type()
)
alaQoSAppliedActionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedActionName.setStatus("current")


class _AlaQoSAppliedActionSource_Type(Integer32):
    """Custom type alaQoSAppliedActionSource based on Integer32"""
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
        *(("ldap", 1),
          ("cli", 2),
          ("blt", 3),
          ("api", 4),
          ("imp", 5))
    )


_AlaQoSAppliedActionSource_Type.__name__ = "Integer32"
_AlaQoSAppliedActionSource_Object = MibTableColumn
alaQoSAppliedActionSource = _AlaQoSAppliedActionSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 2),
    _AlaQoSAppliedActionSource_Type()
)
alaQoSAppliedActionSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionSource.setStatus("current")


class _AlaQoSAppliedActionDisposition_Type(Integer32):
    """Custom type alaQoSAppliedActionDisposition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 2),
          ("deny", 3))
    )


_AlaQoSAppliedActionDisposition_Type.__name__ = "Integer32"
_AlaQoSAppliedActionDisposition_Object = MibTableColumn
alaQoSAppliedActionDisposition = _AlaQoSAppliedActionDisposition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 3),
    _AlaQoSAppliedActionDisposition_Type()
)
alaQoSAppliedActionDisposition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionDisposition.setStatus("current")
_AlaQoSAppliedActionMaximumBandwidth_Type = Integer32
_AlaQoSAppliedActionMaximumBandwidth_Object = MibTableColumn
alaQoSAppliedActionMaximumBandwidth = _AlaQoSAppliedActionMaximumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 4),
    _AlaQoSAppliedActionMaximumBandwidth_Type()
)
alaQoSAppliedActionMaximumBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMaximumBandwidth.setStatus("current")


class _AlaQoSAppliedActionMaximumBandwidthStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionMaximumBandwidthStatus based on Integer32"""
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


_AlaQoSAppliedActionMaximumBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionMaximumBandwidthStatus_Object = MibTableColumn
alaQoSAppliedActionMaximumBandwidthStatus = _AlaQoSAppliedActionMaximumBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 5),
    _AlaQoSAppliedActionMaximumBandwidthStatus_Type()
)
alaQoSAppliedActionMaximumBandwidthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMaximumBandwidthStatus.setStatus("current")


class _AlaQoSAppliedActionPriority_Type(Integer32):
    """Custom type alaQoSAppliedActionPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_AlaQoSAppliedActionPriority_Type.__name__ = "Integer32"
_AlaQoSAppliedActionPriority_Object = MibTableColumn
alaQoSAppliedActionPriority = _AlaQoSAppliedActionPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 6),
    _AlaQoSAppliedActionPriority_Type()
)
alaQoSAppliedActionPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionPriority.setStatus("current")


class _AlaQoSAppliedActionPriorityStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionPriorityStatus based on Integer32"""
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


_AlaQoSAppliedActionPriorityStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionPriorityStatus_Object = MibTableColumn
alaQoSAppliedActionPriorityStatus = _AlaQoSAppliedActionPriorityStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 7),
    _AlaQoSAppliedActionPriorityStatus_Type()
)
alaQoSAppliedActionPriorityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionPriorityStatus.setStatus("current")


class _AlaQoSAppliedActionShared_Type(Integer32):
    """Custom type alaQoSAppliedActionShared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSAppliedActionShared_Type.__name__ = "Integer32"
_AlaQoSAppliedActionShared_Object = MibTableColumn
alaQoSAppliedActionShared = _AlaQoSAppliedActionShared_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 8),
    _AlaQoSAppliedActionShared_Type()
)
alaQoSAppliedActionShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionShared.setStatus("current")
_AlaQoSAppliedActionMaximumDepth_Type = Integer32
_AlaQoSAppliedActionMaximumDepth_Object = MibTableColumn
alaQoSAppliedActionMaximumDepth = _AlaQoSAppliedActionMaximumDepth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 9),
    _AlaQoSAppliedActionMaximumDepth_Type()
)
alaQoSAppliedActionMaximumDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMaximumDepth.setStatus("current")


class _AlaQoSAppliedActionMaximumDepthStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionMaximumDepthStatus based on Integer32"""
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


_AlaQoSAppliedActionMaximumDepthStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionMaximumDepthStatus_Object = MibTableColumn
alaQoSAppliedActionMaximumDepthStatus = _AlaQoSAppliedActionMaximumDepthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 10),
    _AlaQoSAppliedActionMaximumDepthStatus_Type()
)
alaQoSAppliedActionMaximumDepthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMaximumDepthStatus.setStatus("current")


class _AlaQoSAppliedAction8021p_Type(Integer32):
    """Custom type alaQoSAppliedAction8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSAppliedAction8021p_Type.__name__ = "Integer32"
_AlaQoSAppliedAction8021p_Object = MibTableColumn
alaQoSAppliedAction8021p = _AlaQoSAppliedAction8021p_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 11),
    _AlaQoSAppliedAction8021p_Type()
)
alaQoSAppliedAction8021p.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedAction8021p.setStatus("current")


class _AlaQoSAppliedAction8021pStatus_Type(Integer32):
    """Custom type alaQoSAppliedAction8021pStatus based on Integer32"""
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


_AlaQoSAppliedAction8021pStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedAction8021pStatus_Object = MibTableColumn
alaQoSAppliedAction8021pStatus = _AlaQoSAppliedAction8021pStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 12),
    _AlaQoSAppliedAction8021pStatus_Type()
)
alaQoSAppliedAction8021pStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedAction8021pStatus.setStatus("current")


class _AlaQoSAppliedActionTos_Type(Integer32):
    """Custom type alaQoSAppliedActionTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSAppliedActionTos_Type.__name__ = "Integer32"
_AlaQoSAppliedActionTos_Object = MibTableColumn
alaQoSAppliedActionTos = _AlaQoSAppliedActionTos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 13),
    _AlaQoSAppliedActionTos_Type()
)
alaQoSAppliedActionTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionTos.setStatus("current")


class _AlaQoSAppliedActionTosStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionTosStatus based on Integer32"""
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


_AlaQoSAppliedActionTosStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionTosStatus_Object = MibTableColumn
alaQoSAppliedActionTosStatus = _AlaQoSAppliedActionTosStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 14),
    _AlaQoSAppliedActionTosStatus_Type()
)
alaQoSAppliedActionTosStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionTosStatus.setStatus("current")


class _AlaQoSAppliedActionDscp_Type(Integer32):
    """Custom type alaQoSAppliedActionDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSAppliedActionDscp_Type.__name__ = "Integer32"
_AlaQoSAppliedActionDscp_Object = MibTableColumn
alaQoSAppliedActionDscp = _AlaQoSAppliedActionDscp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 15),
    _AlaQoSAppliedActionDscp_Type()
)
alaQoSAppliedActionDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionDscp.setStatus("current")


class _AlaQoSAppliedActionDscpStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionDscpStatus based on Integer32"""
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


_AlaQoSAppliedActionDscpStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionDscpStatus_Object = MibTableColumn
alaQoSAppliedActionDscpStatus = _AlaQoSAppliedActionDscpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 16),
    _AlaQoSAppliedActionDscpStatus_Type()
)
alaQoSAppliedActionDscpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionDscpStatus.setStatus("current")


class _AlaQoSAppliedActionMapFrom_Type(Integer32):
    """Custom type alaQoSAppliedActionMapFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("b8021p", 1),
          ("tos", 2),
          ("dscp", 3))
    )


_AlaQoSAppliedActionMapFrom_Type.__name__ = "Integer32"
_AlaQoSAppliedActionMapFrom_Object = MibTableColumn
alaQoSAppliedActionMapFrom = _AlaQoSAppliedActionMapFrom_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 17),
    _AlaQoSAppliedActionMapFrom_Type()
)
alaQoSAppliedActionMapFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMapFrom.setStatus("current")


class _AlaQoSAppliedActionMapTo_Type(Integer32):
    """Custom type alaQoSAppliedActionMapTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("b8021p", 1),
          ("tos", 2),
          ("dscp", 3))
    )


_AlaQoSAppliedActionMapTo_Type.__name__ = "Integer32"
_AlaQoSAppliedActionMapTo_Object = MibTableColumn
alaQoSAppliedActionMapTo = _AlaQoSAppliedActionMapTo_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 18),
    _AlaQoSAppliedActionMapTo_Type()
)
alaQoSAppliedActionMapTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMapTo.setStatus("current")


class _AlaQoSAppliedActionMapGroup_Type(SnmpAdminString):
    """Custom type alaQoSAppliedActionMapGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedActionMapGroup_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedActionMapGroup_Object = MibTableColumn
alaQoSAppliedActionMapGroup = _AlaQoSAppliedActionMapGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 19),
    _AlaQoSAppliedActionMapGroup_Type()
)
alaQoSAppliedActionMapGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMapGroup.setStatus("current")


class _AlaQoSAppliedActionMapGroupStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionMapGroupStatus based on Integer32"""
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


_AlaQoSAppliedActionMapGroupStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionMapGroupStatus_Object = MibTableColumn
alaQoSAppliedActionMapGroupStatus = _AlaQoSAppliedActionMapGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 20),
    _AlaQoSAppliedActionMapGroupStatus_Type()
)
alaQoSAppliedActionMapGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMapGroupStatus.setStatus("current")


class _AlaQoSAppliedActionLoadBalanceGroup_Type(SnmpAdminString):
    """Custom type alaQoSAppliedActionLoadBalanceGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_AlaQoSAppliedActionLoadBalanceGroup_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedActionLoadBalanceGroup_Object = MibTableColumn
alaQoSAppliedActionLoadBalanceGroup = _AlaQoSAppliedActionLoadBalanceGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 21),
    _AlaQoSAppliedActionLoadBalanceGroup_Type()
)
alaQoSAppliedActionLoadBalanceGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionLoadBalanceGroup.setStatus("current")


class _AlaQoSAppliedActionLoadBalanceGroupStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionLoadBalanceGroupStatus based on Integer32"""
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


_AlaQoSAppliedActionLoadBalanceGroupStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionLoadBalanceGroupStatus_Object = MibTableColumn
alaQoSAppliedActionLoadBalanceGroupStatus = _AlaQoSAppliedActionLoadBalanceGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 22),
    _AlaQoSAppliedActionLoadBalanceGroupStatus_Type()
)
alaQoSAppliedActionLoadBalanceGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionLoadBalanceGroupStatus.setStatus("current")
_AlaQoSAppliedActionPermanentGatewayIpAddr_Type = IpAddress
_AlaQoSAppliedActionPermanentGatewayIpAddr_Object = MibTableColumn
alaQoSAppliedActionPermanentGatewayIpAddr = _AlaQoSAppliedActionPermanentGatewayIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 23),
    _AlaQoSAppliedActionPermanentGatewayIpAddr_Type()
)
alaQoSAppliedActionPermanentGatewayIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionPermanentGatewayIpAddr.setStatus("current")


class _AlaQoSAppliedActionPermanentGatewayIpAddrStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionPermanentGatewayIpAddrStatus based on Integer32"""
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


_AlaQoSAppliedActionPermanentGatewayIpAddrStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionPermanentGatewayIpAddrStatus_Object = MibTableColumn
alaQoSAppliedActionPermanentGatewayIpAddrStatus = _AlaQoSAppliedActionPermanentGatewayIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 24),
    _AlaQoSAppliedActionPermanentGatewayIpAddrStatus_Type()
)
alaQoSAppliedActionPermanentGatewayIpAddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionPermanentGatewayIpAddrStatus.setStatus("current")
_AlaQoSAppliedActionAlternateGatewayIpAddr_Type = IpAddress
_AlaQoSAppliedActionAlternateGatewayIpAddr_Object = MibTableColumn
alaQoSAppliedActionAlternateGatewayIpAddr = _AlaQoSAppliedActionAlternateGatewayIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 25),
    _AlaQoSAppliedActionAlternateGatewayIpAddr_Type()
)
alaQoSAppliedActionAlternateGatewayIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionAlternateGatewayIpAddr.setStatus("current")


class _AlaQoSAppliedActionAlternateGatewayIpAddrStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionAlternateGatewayIpAddrStatus based on Integer32"""
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


_AlaQoSAppliedActionAlternateGatewayIpAddrStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionAlternateGatewayIpAddrStatus_Object = MibTableColumn
alaQoSAppliedActionAlternateGatewayIpAddrStatus = _AlaQoSAppliedActionAlternateGatewayIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 26),
    _AlaQoSAppliedActionAlternateGatewayIpAddrStatus_Type()
)
alaQoSAppliedActionAlternateGatewayIpAddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionAlternateGatewayIpAddrStatus.setStatus("current")
_AlaQoSAppliedActionRowStatus_Type = RowStatus
_AlaQoSAppliedActionRowStatus_Object = MibTableColumn
alaQoSAppliedActionRowStatus = _AlaQoSAppliedActionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 27),
    _AlaQoSAppliedActionRowStatus_Type()
)
alaQoSAppliedActionRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionRowStatus.setStatus("current")


class _AlaQoSAppliedActionNocache_Type(Integer32):
    """Custom type alaQoSAppliedActionNocache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSAppliedActionNocache_Type.__name__ = "Integer32"
_AlaQoSAppliedActionNocache_Object = MibTableColumn
alaQoSAppliedActionNocache = _AlaQoSAppliedActionNocache_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 28),
    _AlaQoSAppliedActionNocache_Type()
)
alaQoSAppliedActionNocache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionNocache.setStatus("current")


class _AlaQoSAppliedActionPortdisable_Type(Integer32):
    """Custom type alaQoSAppliedActionPortdisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSAppliedActionPortdisable_Type.__name__ = "Integer32"
_AlaQoSAppliedActionPortdisable_Object = MibTableColumn
alaQoSAppliedActionPortdisable = _AlaQoSAppliedActionPortdisable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 29),
    _AlaQoSAppliedActionPortdisable_Type()
)
alaQoSAppliedActionPortdisable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionPortdisable.setStatus("current")


class _AlaQoSAppliedActionRedirectSlot_Type(Integer32):
    """Custom type alaQoSAppliedActionRedirectSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSAppliedActionRedirectSlot_Type.__name__ = "Integer32"
_AlaQoSAppliedActionRedirectSlot_Object = MibTableColumn
alaQoSAppliedActionRedirectSlot = _AlaQoSAppliedActionRedirectSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 30),
    _AlaQoSAppliedActionRedirectSlot_Type()
)
alaQoSAppliedActionRedirectSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionRedirectSlot.setStatus("current")


class _AlaQoSAppliedActionRedirectSlotStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionRedirectSlotStatus based on Integer32"""
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


_AlaQoSAppliedActionRedirectSlotStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionRedirectSlotStatus_Object = MibTableColumn
alaQoSAppliedActionRedirectSlotStatus = _AlaQoSAppliedActionRedirectSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 31),
    _AlaQoSAppliedActionRedirectSlotStatus_Type()
)
alaQoSAppliedActionRedirectSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionRedirectSlotStatus.setStatus("current")


class _AlaQoSAppliedActionRedirectPort_Type(Integer32):
    """Custom type alaQoSAppliedActionRedirectPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_AlaQoSAppliedActionRedirectPort_Type.__name__ = "Integer32"
_AlaQoSAppliedActionRedirectPort_Object = MibTableColumn
alaQoSAppliedActionRedirectPort = _AlaQoSAppliedActionRedirectPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 32),
    _AlaQoSAppliedActionRedirectPort_Type()
)
alaQoSAppliedActionRedirectPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionRedirectPort.setStatus("current")


class _AlaQoSAppliedActionRedirectAgg_Type(Integer32):
    """Custom type alaQoSAppliedActionRedirectAgg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AlaQoSAppliedActionRedirectAgg_Type.__name__ = "Integer32"
_AlaQoSAppliedActionRedirectAgg_Object = MibTableColumn
alaQoSAppliedActionRedirectAgg = _AlaQoSAppliedActionRedirectAgg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 33),
    _AlaQoSAppliedActionRedirectAgg_Type()
)
alaQoSAppliedActionRedirectAgg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionRedirectAgg.setStatus("current")


class _AlaQoSAppliedActionRedirectAggStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionRedirectAggStatus based on Integer32"""
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


_AlaQoSAppliedActionRedirectAggStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionRedirectAggStatus_Object = MibTableColumn
alaQoSAppliedActionRedirectAggStatus = _AlaQoSAppliedActionRedirectAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 34),
    _AlaQoSAppliedActionRedirectAggStatus_Type()
)
alaQoSAppliedActionRedirectAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionRedirectAggStatus.setStatus("current")


class _AlaQoSAppliedActionMirrorSlot_Type(Integer32):
    """Custom type alaQoSAppliedActionMirrorSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSAppliedActionMirrorSlot_Type.__name__ = "Integer32"
_AlaQoSAppliedActionMirrorSlot_Object = MibTableColumn
alaQoSAppliedActionMirrorSlot = _AlaQoSAppliedActionMirrorSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 35),
    _AlaQoSAppliedActionMirrorSlot_Type()
)
alaQoSAppliedActionMirrorSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMirrorSlot.setStatus("current")


class _AlaQoSAppliedActionMirrorPort_Type(Integer32):
    """Custom type alaQoSAppliedActionMirrorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_AlaQoSAppliedActionMirrorPort_Type.__name__ = "Integer32"
_AlaQoSAppliedActionMirrorPort_Object = MibTableColumn
alaQoSAppliedActionMirrorPort = _AlaQoSAppliedActionMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 36),
    _AlaQoSAppliedActionMirrorPort_Type()
)
alaQoSAppliedActionMirrorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMirrorPort.setStatus("current")


class _AlaQoSAppliedActionMirrorMode_Type(Integer32):
    """Custom type alaQoSAppliedActionMirrorMode based on Integer32"""
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
        *(("ingress", 1),
          ("egress", 2),
          ("both", 3))
    )


_AlaQoSAppliedActionMirrorMode_Type.__name__ = "Integer32"
_AlaQoSAppliedActionMirrorMode_Object = MibTableColumn
alaQoSAppliedActionMirrorMode = _AlaQoSAppliedActionMirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 37),
    _AlaQoSAppliedActionMirrorMode_Type()
)
alaQoSAppliedActionMirrorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMirrorMode.setStatus("current")


class _AlaQoSAppliedActionMirrorModeStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionMirrorModeStatus based on Integer32"""
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


_AlaQoSAppliedActionMirrorModeStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionMirrorModeStatus_Object = MibTableColumn
alaQoSAppliedActionMirrorModeStatus = _AlaQoSAppliedActionMirrorModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 38),
    _AlaQoSAppliedActionMirrorModeStatus_Type()
)
alaQoSAppliedActionMirrorModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMirrorModeStatus.setStatus("current")


class _AlaQoSAppliedActionCIR_Type(Integer32):
    """Custom type alaQoSAppliedActionCIR based on Integer32"""
    defaultValue = 0


_AlaQoSAppliedActionCIR_Type.__name__ = "Integer32"
_AlaQoSAppliedActionCIR_Object = MibTableColumn
alaQoSAppliedActionCIR = _AlaQoSAppliedActionCIR_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 39),
    _AlaQoSAppliedActionCIR_Type()
)
alaQoSAppliedActionCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionCIR.setStatus("current")
if mibBuilder.loadTexts:
    alaQoSAppliedActionCIR.setUnits("kilobits per second")


class _AlaQoSAppliedActionCIRStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionCIRStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSAppliedActionCIRStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionCIRStatus_Object = MibTableColumn
alaQoSAppliedActionCIRStatus = _AlaQoSAppliedActionCIRStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 40),
    _AlaQoSAppliedActionCIRStatus_Type()
)
alaQoSAppliedActionCIRStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionCIRStatus.setStatus("current")


class _AlaQoSAppliedActionCBS_Type(Integer32):
    """Custom type alaQoSAppliedActionCBS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147450880),
    )


_AlaQoSAppliedActionCBS_Type.__name__ = "Integer32"
_AlaQoSAppliedActionCBS_Object = MibTableColumn
alaQoSAppliedActionCBS = _AlaQoSAppliedActionCBS_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 41),
    _AlaQoSAppliedActionCBS_Type()
)
alaQoSAppliedActionCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionCBS.setStatus("current")


class _AlaQoSAppliedActionCBSStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionCBSStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSAppliedActionCBSStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionCBSStatus_Object = MibTableColumn
alaQoSAppliedActionCBSStatus = _AlaQoSAppliedActionCBSStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 42),
    _AlaQoSAppliedActionCBSStatus_Type()
)
alaQoSAppliedActionCBSStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionCBSStatus.setStatus("current")


class _AlaQoSAppliedActionPIR_Type(Integer32):
    """Custom type alaQoSAppliedActionPIR based on Integer32"""
    defaultValue = 0


_AlaQoSAppliedActionPIR_Type.__name__ = "Integer32"
_AlaQoSAppliedActionPIR_Object = MibTableColumn
alaQoSAppliedActionPIR = _AlaQoSAppliedActionPIR_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 43),
    _AlaQoSAppliedActionPIR_Type()
)
alaQoSAppliedActionPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionPIR.setStatus("current")
if mibBuilder.loadTexts:
    alaQoSAppliedActionPIR.setUnits("kilobits per second")


class _AlaQoSAppliedActionPIRStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionPIRStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSAppliedActionPIRStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionPIRStatus_Object = MibTableColumn
alaQoSAppliedActionPIRStatus = _AlaQoSAppliedActionPIRStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 44),
    _AlaQoSAppliedActionPIRStatus_Type()
)
alaQoSAppliedActionPIRStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionPIRStatus.setStatus("current")


class _AlaQoSAppliedActionPBS_Type(Integer32):
    """Custom type alaQoSAppliedActionPBS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147450880),
    )


_AlaQoSAppliedActionPBS_Type.__name__ = "Integer32"
_AlaQoSAppliedActionPBS_Object = MibTableColumn
alaQoSAppliedActionPBS = _AlaQoSAppliedActionPBS_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 45),
    _AlaQoSAppliedActionPBS_Type()
)
alaQoSAppliedActionPBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionPBS.setStatus("current")


class _AlaQoSAppliedActionPBSStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionPBSStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSAppliedActionPBSStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionPBSStatus_Object = MibTableColumn
alaQoSAppliedActionPBSStatus = _AlaQoSAppliedActionPBSStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 46),
    _AlaQoSAppliedActionPBSStatus_Type()
)
alaQoSAppliedActionPBSStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionPBSStatus.setStatus("current")


class _AlaQoSAppliedActionCPUPriority_Type(Integer32):
    """Custom type alaQoSAppliedActionCPUPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSAppliedActionCPUPriority_Type.__name__ = "Integer32"
_AlaQoSAppliedActionCPUPriority_Object = MibTableColumn
alaQoSAppliedActionCPUPriority = _AlaQoSAppliedActionCPUPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 47),
    _AlaQoSAppliedActionCPUPriority_Type()
)
alaQoSAppliedActionCPUPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionCPUPriority.setStatus("current")


class _AlaQoSAppliedActionCPUPriorityStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionCPUPriorityStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSAppliedActionCPUPriorityStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionCPUPriorityStatus_Object = MibTableColumn
alaQoSAppliedActionCPUPriorityStatus = _AlaQoSAppliedActionCPUPriorityStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 48),
    _AlaQoSAppliedActionCPUPriorityStatus_Type()
)
alaQoSAppliedActionCPUPriorityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionCPUPriorityStatus.setStatus("current")


class _AlaQoSAppliedActionColorOnly_Type(Integer32):
    """Custom type alaQoSAppliedActionColorOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSAppliedActionColorOnly_Type.__name__ = "Integer32"
_AlaQoSAppliedActionColorOnly_Object = MibTableColumn
alaQoSAppliedActionColorOnly = _AlaQoSAppliedActionColorOnly_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 49),
    _AlaQoSAppliedActionColorOnly_Type()
)
alaQoSAppliedActionColorOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionColorOnly.setStatus("current")


class _AlaQoSAppliedActionRedirectChassis_Type(Integer32):
    """Custom type alaQoSAppliedActionRedirectChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSAppliedActionRedirectChassis_Type.__name__ = "Integer32"
_AlaQoSAppliedActionRedirectChassis_Object = MibTableColumn
alaQoSAppliedActionRedirectChassis = _AlaQoSAppliedActionRedirectChassis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 50),
    _AlaQoSAppliedActionRedirectChassis_Type()
)
alaQoSAppliedActionRedirectChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionRedirectChassis.setStatus("current")


class _AlaQoSAppliedActionMirrorChassis_Type(Integer32):
    """Custom type alaQoSAppliedActionMirrorChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSAppliedActionMirrorChassis_Type.__name__ = "Integer32"
_AlaQoSAppliedActionMirrorChassis_Object = MibTableColumn
alaQoSAppliedActionMirrorChassis = _AlaQoSAppliedActionMirrorChassis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 51),
    _AlaQoSAppliedActionMirrorChassis_Type()
)
alaQoSAppliedActionMirrorChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMirrorChassis.setStatus("current")


class _AlaQoSAppliedActionPermanentGatewayIpV6Addr_Type(Ipv6Address):
    """Custom type alaQoSAppliedActionPermanentGatewayIpV6Addr based on Ipv6Address"""
    defaultHexValue = "00000000000000000000000000000000"


_AlaQoSAppliedActionPermanentGatewayIpV6Addr_Type.__name__ = "Ipv6Address"
_AlaQoSAppliedActionPermanentGatewayIpV6Addr_Object = MibTableColumn
alaQoSAppliedActionPermanentGatewayIpV6Addr = _AlaQoSAppliedActionPermanentGatewayIpV6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 52),
    _AlaQoSAppliedActionPermanentGatewayIpV6Addr_Type()
)
alaQoSAppliedActionPermanentGatewayIpV6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionPermanentGatewayIpV6Addr.setStatus("current")


class _AlaQoSAppliedActionPermanentGatewayIpV6AddrStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionPermanentGatewayIpV6AddrStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSAppliedActionPermanentGatewayIpV6AddrStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionPermanentGatewayIpV6AddrStatus_Object = MibTableColumn
alaQoSAppliedActionPermanentGatewayIpV6AddrStatus = _AlaQoSAppliedActionPermanentGatewayIpV6AddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 53),
    _AlaQoSAppliedActionPermanentGatewayIpV6AddrStatus_Type()
)
alaQoSAppliedActionPermanentGatewayIpV6AddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionPermanentGatewayIpV6AddrStatus.setStatus("current")


class _AlaQoSAppliedActionPermanentGatewayIpV6IfIndex_Type(Ipv6IfIndexOrZero):
    """Custom type alaQoSAppliedActionPermanentGatewayIpV6IfIndex based on Ipv6IfIndexOrZero"""
    defaultValue = 0


_AlaQoSAppliedActionPermanentGatewayIpV6IfIndex_Type.__name__ = "Ipv6IfIndexOrZero"
_AlaQoSAppliedActionPermanentGatewayIpV6IfIndex_Object = MibTableColumn
alaQoSAppliedActionPermanentGatewayIpV6IfIndex = _AlaQoSAppliedActionPermanentGatewayIpV6IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 54),
    _AlaQoSAppliedActionPermanentGatewayIpV6IfIndex_Type()
)
alaQoSAppliedActionPermanentGatewayIpV6IfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionPermanentGatewayIpV6IfIndex.setStatus("current")


class _AlaQoSAppliedActionRTCPMonitor_Type(Integer32):
    """Custom type alaQoSAppliedActionRTCPMonitor based on Integer32"""
    defaultValue = 1

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


_AlaQoSAppliedActionRTCPMonitor_Type.__name__ = "Integer32"
_AlaQoSAppliedActionRTCPMonitor_Object = MibTableColumn
alaQoSAppliedActionRTCPMonitor = _AlaQoSAppliedActionRTCPMonitor_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 55),
    _AlaQoSAppliedActionRTCPMonitor_Type()
)
alaQoSAppliedActionRTCPMonitor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionRTCPMonitor.setStatus("current")


class _AlaQoSAppliedActionRTCPMonitorStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionRTCPMonitorStatus based on Integer32"""
    defaultValue = 1

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


_AlaQoSAppliedActionRTCPMonitorStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionRTCPMonitorStatus_Object = MibTableColumn
alaQoSAppliedActionRTCPMonitorStatus = _AlaQoSAppliedActionRTCPMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 56),
    _AlaQoSAppliedActionRTCPMonitorStatus_Type()
)
alaQoSAppliedActionRTCPMonitorStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionRTCPMonitorStatus.setStatus("current")
_AlaQoSAppliedActionRTCPDSCP_Type = Integer32
_AlaQoSAppliedActionRTCPDSCP_Object = MibTableColumn
alaQoSAppliedActionRTCPDSCP = _AlaQoSAppliedActionRTCPDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 57),
    _AlaQoSAppliedActionRTCPDSCP_Type()
)
alaQoSAppliedActionRTCPDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionRTCPDSCP.setStatus("current")


class _AlaQoSAppliedActionRTCPDSCPStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionRTCPDSCPStatus based on Integer32"""
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


_AlaQoSAppliedActionRTCPDSCPStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionRTCPDSCPStatus_Object = MibTableColumn
alaQoSAppliedActionRTCPDSCPStatus = _AlaQoSAppliedActionRTCPDSCPStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 58),
    _AlaQoSAppliedActionRTCPDSCPStatus_Type()
)
alaQoSAppliedActionRTCPDSCPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionRTCPDSCPStatus.setStatus("current")


class _AlaQoSAppliedActionTrustDSCP_Type(Integer32):
    """Custom type alaQoSAppliedActionTrustDSCP based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSAppliedActionTrustDSCP_Type.__name__ = "Integer32"
_AlaQoSAppliedActionTrustDSCP_Object = MibTableColumn
alaQoSAppliedActionTrustDSCP = _AlaQoSAppliedActionTrustDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 59),
    _AlaQoSAppliedActionTrustDSCP_Type()
)
alaQoSAppliedActionTrustDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionTrustDSCP.setStatus("current")


class _AlaQoSAppliedActionTrustDSCPStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionTrustDSCPStatus based on Integer32"""
    defaultValue = 1

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


_AlaQoSAppliedActionTrustDSCPStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionTrustDSCPStatus_Object = MibTableColumn
alaQoSAppliedActionTrustDSCPStatus = _AlaQoSAppliedActionTrustDSCPStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 60),
    _AlaQoSAppliedActionTrustDSCPStatus_Type()
)
alaQoSAppliedActionTrustDSCPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionTrustDSCPStatus.setStatus("current")
_AlaQoSPortTable_Object = MibTable
alaQoSPortTable = _AlaQoSPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29)
)
if mibBuilder.loadTexts:
    alaQoSPortTable.setStatus("current")
_AlaQoSPortEntry_Object = MibTableRow
alaQoSPortEntry = _AlaQoSPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1)
)
alaQoSPortEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSPortSlot"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSPortPort"),
)
if mibBuilder.loadTexts:
    alaQoSPortEntry.setStatus("current")


class _AlaQoSPortSlot_Type(Integer32):
    """Custom type alaQoSPortSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6016),
    )


_AlaQoSPortSlot_Type.__name__ = "Integer32"
_AlaQoSPortSlot_Object = MibTableColumn
alaQoSPortSlot = _AlaQoSPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 1),
    _AlaQoSPortSlot_Type()
)
alaQoSPortSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSPortSlot.setStatus("current")


class _AlaQoSPortPort_Type(Integer32):
    """Custom type alaQoSPortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_AlaQoSPortPort_Type.__name__ = "Integer32"
_AlaQoSPortPort_Object = MibTableColumn
alaQoSPortPort = _AlaQoSPortPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 2),
    _AlaQoSPortPort_Type()
)
alaQoSPortPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSPortPort.setStatus("current")


class _AlaQoSPortInterfaceType_Type(Integer32):
    """Custom type alaQoSPortInterfaceType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("wan", 2),
          ("ethernet10", 3),
          ("ethernet100", 4),
          ("ethernet1G", 5),
          ("ethernet10G", 6),
          ("aggregate", 7),
          ("ethernet40G", 8),
          ("ethernet100G", 9))
    )


_AlaQoSPortInterfaceType_Type.__name__ = "Integer32"
_AlaQoSPortInterfaceType_Object = MibTableColumn
alaQoSPortInterfaceType = _AlaQoSPortInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 3),
    _AlaQoSPortInterfaceType_Type()
)
alaQoSPortInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortInterfaceType.setStatus("current")


class _AlaQoSPortTrusted_Type(Integer32):
    """Custom type alaQoSPortTrusted based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSPortTrusted_Type.__name__ = "Integer32"
_AlaQoSPortTrusted_Object = MibTableColumn
alaQoSPortTrusted = _AlaQoSPortTrusted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 4),
    _AlaQoSPortTrusted_Type()
)
alaQoSPortTrusted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortTrusted.setStatus("current")


class _AlaQoSPortDefault8021p_Type(Integer32):
    """Custom type alaQoSPortDefault8021p based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSPortDefault8021p_Type.__name__ = "Integer32"
_AlaQoSPortDefault8021p_Object = MibTableColumn
alaQoSPortDefault8021p = _AlaQoSPortDefault8021p_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 5),
    _AlaQoSPortDefault8021p_Type()
)
alaQoSPortDefault8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortDefault8021p.setStatus("current")


class _AlaQoSPortDefaultDSCP_Type(Integer32):
    """Custom type alaQoSPortDefaultDSCP based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSPortDefaultDSCP_Type.__name__ = "Integer32"
_AlaQoSPortDefaultDSCP_Object = MibTableColumn
alaQoSPortDefaultDSCP = _AlaQoSPortDefaultDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 6),
    _AlaQoSPortDefaultDSCP_Type()
)
alaQoSPortDefaultDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortDefaultDSCP.setStatus("current")


class _AlaQoSPortMaximumDefaultDepth_Type(Integer32):
    """Custom type alaQoSPortMaximumDefaultDepth based on Integer32"""
    defaultValue = 0


_AlaQoSPortMaximumDefaultDepth_Type.__name__ = "Integer32"
_AlaQoSPortMaximumDefaultDepth_Object = MibTableColumn
alaQoSPortMaximumDefaultDepth = _AlaQoSPortMaximumDefaultDepth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 7),
    _AlaQoSPortMaximumDefaultDepth_Type()
)
alaQoSPortMaximumDefaultDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortMaximumDefaultDepth.setStatus("current")


class _AlaQoSPortMaximumDefaultDepthStatus_Type(Integer32):
    """Custom type alaQoSPortMaximumDefaultDepthStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSPortMaximumDefaultDepthStatus_Type.__name__ = "Integer32"
_AlaQoSPortMaximumDefaultDepthStatus_Object = MibTableColumn
alaQoSPortMaximumDefaultDepthStatus = _AlaQoSPortMaximumDefaultDepthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 8),
    _AlaQoSPortMaximumDefaultDepthStatus_Type()
)
alaQoSPortMaximumDefaultDepthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortMaximumDefaultDepthStatus.setStatus("current")


class _AlaQoSPortReset_Type(Integer32):
    """Custom type alaQoSPortReset based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSPortReset_Type.__name__ = "Integer32"
_AlaQoSPortReset_Object = MibTableColumn
alaQoSPortReset = _AlaQoSPortReset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 9),
    _AlaQoSPortReset_Type()
)
alaQoSPortReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortReset.setStatus("current")
_AlaQoSPortPhysicalBandwidth_Type = Integer32
_AlaQoSPortPhysicalBandwidth_Object = MibTableColumn
alaQoSPortPhysicalBandwidth = _AlaQoSPortPhysicalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 10),
    _AlaQoSPortPhysicalBandwidth_Type()
)
alaQoSPortPhysicalBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortPhysicalBandwidth.setStatus("current")
_AlaQoSPortRowStatus_Type = RowStatus
_AlaQoSPortRowStatus_Object = MibTableColumn
alaQoSPortRowStatus = _AlaQoSPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 11),
    _AlaQoSPortRowStatus_Type()
)
alaQoSPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortRowStatus.setStatus("current")


class _AlaQoSPortDefaultClassification_Type(Integer32):
    """Custom type alaQoSPortDefaultClassification based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("b8021p", 1),
          ("tos", 2),
          ("dscp", 3))
    )


_AlaQoSPortDefaultClassification_Type.__name__ = "Integer32"
_AlaQoSPortDefaultClassification_Object = MibTableColumn
alaQoSPortDefaultClassification = _AlaQoSPortDefaultClassification_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 12),
    _AlaQoSPortDefaultClassification_Type()
)
alaQoSPortDefaultClassification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortDefaultClassification.setStatus("current")


class _AlaQoSPortMaximumBandwidth_Type(Integer32):
    """Custom type alaQoSPortMaximumBandwidth based on Integer32"""
    defaultValue = 0


_AlaQoSPortMaximumBandwidth_Type.__name__ = "Integer32"
_AlaQoSPortMaximumBandwidth_Object = MibTableColumn
alaQoSPortMaximumBandwidth = _AlaQoSPortMaximumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 13),
    _AlaQoSPortMaximumBandwidth_Type()
)
alaQoSPortMaximumBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortMaximumBandwidth.setStatus("current")


class _AlaQoSPortMaximumBandwidthStatus_Type(Integer32):
    """Custom type alaQoSPortMaximumBandwidthStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSPortMaximumBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSPortMaximumBandwidthStatus_Object = MibTableColumn
alaQoSPortMaximumBandwidthStatus = _AlaQoSPortMaximumBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 14),
    _AlaQoSPortMaximumBandwidthStatus_Type()
)
alaQoSPortMaximumBandwidthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortMaximumBandwidthStatus.setStatus("current")


class _AlaQoSPortMaximumIngBandwidth_Type(Integer32):
    """Custom type alaQoSPortMaximumIngBandwidth based on Integer32"""
    defaultValue = 0


_AlaQoSPortMaximumIngBandwidth_Type.__name__ = "Integer32"
_AlaQoSPortMaximumIngBandwidth_Object = MibTableColumn
alaQoSPortMaximumIngBandwidth = _AlaQoSPortMaximumIngBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 15),
    _AlaQoSPortMaximumIngBandwidth_Type()
)
alaQoSPortMaximumIngBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortMaximumIngBandwidth.setStatus("current")


class _AlaQoSPortMaximumIngBandwidthStatus_Type(Integer32):
    """Custom type alaQoSPortMaximumIngBandwidthStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSPortMaximumIngBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSPortMaximumIngBandwidthStatus_Object = MibTableColumn
alaQoSPortMaximumIngBandwidthStatus = _AlaQoSPortMaximumIngBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 16),
    _AlaQoSPortMaximumIngBandwidthStatus_Type()
)
alaQoSPortMaximumIngBandwidthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortMaximumIngBandwidthStatus.setStatus("current")


class _AlaQoSPortMaximumIngressDepth_Type(Integer32):
    """Custom type alaQoSPortMaximumIngressDepth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSPortMaximumIngressDepth_Type.__name__ = "Integer32"
_AlaQoSPortMaximumIngressDepth_Object = MibTableColumn
alaQoSPortMaximumIngressDepth = _AlaQoSPortMaximumIngressDepth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 17),
    _AlaQoSPortMaximumIngressDepth_Type()
)
alaQoSPortMaximumIngressDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortMaximumIngressDepth.setStatus("current")


class _AlaQoSPortMaximumIngressDepthStatus_Type(Integer32):
    """Custom type alaQoSPortMaximumIngressDepthStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSPortMaximumIngressDepthStatus_Type.__name__ = "Integer32"
_AlaQoSPortMaximumIngressDepthStatus_Object = MibTableColumn
alaQoSPortMaximumIngressDepthStatus = _AlaQoSPortMaximumIngressDepthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 18),
    _AlaQoSPortMaximumIngressDepthStatus_Type()
)
alaQoSPortMaximumIngressDepthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortMaximumIngressDepthStatus.setStatus("current")


class _AlaQoSPortDEIMarking_Type(Integer32):
    """Custom type alaQoSPortDEIMarking based on Integer32"""
    defaultValue = 2

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


_AlaQoSPortDEIMarking_Type.__name__ = "Integer32"
_AlaQoSPortDEIMarking_Object = MibTableColumn
alaQoSPortDEIMarking = _AlaQoSPortDEIMarking_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 19),
    _AlaQoSPortDEIMarking_Type()
)
alaQoSPortDEIMarking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortDEIMarking.setStatus("current")


class _AlaQoSPortDEIMapping_Type(Integer32):
    """Custom type alaQoSPortDEIMapping based on Integer32"""
    defaultValue = 2

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


_AlaQoSPortDEIMapping_Type.__name__ = "Integer32"
_AlaQoSPortDEIMapping_Object = MibTableColumn
alaQoSPortDEIMapping = _AlaQoSPortDEIMapping_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 20),
    _AlaQoSPortDEIMapping_Type()
)
alaQoSPortDEIMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortDEIMapping.setStatus("current")
_AlaQoSConfig_ObjectIdentity = ObjectIdentity
alaQoSConfig = _AlaQoSConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30)
)


class _AlaQoSConfigEnabled_Type(Integer32):
    """Custom type alaQoSConfigEnabled based on Integer32"""
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


_AlaQoSConfigEnabled_Type.__name__ = "Integer32"
_AlaQoSConfigEnabled_Object = MibScalar
alaQoSConfigEnabled = _AlaQoSConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 1),
    _AlaQoSConfigEnabled_Type()
)
alaQoSConfigEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigEnabled.setStatus("current")


class _AlaQoSConfigTrustPorts_Type(Integer32):
    """Custom type alaQoSConfigTrustPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSConfigTrustPorts_Type.__name__ = "Integer32"
_AlaQoSConfigTrustPorts_Object = MibScalar
alaQoSConfigTrustPorts = _AlaQoSConfigTrustPorts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 2),
    _AlaQoSConfigTrustPorts_Type()
)
alaQoSConfigTrustPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigTrustPorts.setStatus("current")


class _AlaQoSConfigStatsInterval_Type(Integer32):
    """Custom type alaQoSConfigStatsInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_AlaQoSConfigStatsInterval_Type.__name__ = "Integer32"
_AlaQoSConfigStatsInterval_Object = MibScalar
alaQoSConfigStatsInterval = _AlaQoSConfigStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 3),
    _AlaQoSConfigStatsInterval_Type()
)
alaQoSConfigStatsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigStatsInterval.setStatus("current")


class _AlaQoSConfigLogLines_Type(Integer32):
    """Custom type alaQoSConfigLogLines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10240),
    )


_AlaQoSConfigLogLines_Type.__name__ = "Integer32"
_AlaQoSConfigLogLines_Object = MibScalar
alaQoSConfigLogLines = _AlaQoSConfigLogLines_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 4),
    _AlaQoSConfigLogLines_Type()
)
alaQoSConfigLogLines.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigLogLines.setStatus("current")


class _AlaQoSConfigLogLevel_Type(Integer32):
    """Custom type alaQoSConfigLogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 9),
    )


_AlaQoSConfigLogLevel_Type.__name__ = "Integer32"
_AlaQoSConfigLogLevel_Object = MibScalar
alaQoSConfigLogLevel = _AlaQoSConfigLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 5),
    _AlaQoSConfigLogLevel_Type()
)
alaQoSConfigLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigLogLevel.setStatus("current")


class _AlaQoSConfigLogConsole_Type(Integer32):
    """Custom type alaQoSConfigLogConsole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSConfigLogConsole_Type.__name__ = "Integer32"
_AlaQoSConfigLogConsole_Object = MibScalar
alaQoSConfigLogConsole = _AlaQoSConfigLogConsole_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 6),
    _AlaQoSConfigLogConsole_Type()
)
alaQoSConfigLogConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigLogConsole.setStatus("current")


class _AlaQoSConfigForwardLog_Type(Integer32):
    """Custom type alaQoSConfigForwardLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSConfigForwardLog_Type.__name__ = "Integer32"
_AlaQoSConfigForwardLog_Object = MibScalar
alaQoSConfigForwardLog = _AlaQoSConfigForwardLog_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 7),
    _AlaQoSConfigForwardLog_Type()
)
alaQoSConfigForwardLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigForwardLog.setStatus("current")


class _AlaQoSConfigClearLog_Type(Integer32):
    """Custom type alaQoSConfigClearLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSConfigClearLog_Type.__name__ = "Integer32"
_AlaQoSConfigClearLog_Object = MibScalar
alaQoSConfigClearLog = _AlaQoSConfigClearLog_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 8),
    _AlaQoSConfigClearLog_Type()
)
alaQoSConfigClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigClearLog.setStatus("current")


class _AlaQoSConfigApply_Type(Integer32):
    """Custom type alaQoSConfigApply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSConfigApply_Type.__name__ = "Integer32"
_AlaQoSConfigApply_Object = MibScalar
alaQoSConfigApply = _AlaQoSConfigApply_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 9),
    _AlaQoSConfigApply_Type()
)
alaQoSConfigApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigApply.setStatus("current")


class _AlaQoSConfigRevert_Type(Integer32):
    """Custom type alaQoSConfigRevert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSConfigRevert_Type.__name__ = "Integer32"
_AlaQoSConfigRevert_Object = MibScalar
alaQoSConfigRevert = _AlaQoSConfigRevert_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 10),
    _AlaQoSConfigRevert_Type()
)
alaQoSConfigRevert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigRevert.setStatus("current")


class _AlaQoSConfigReset_Type(Integer32):
    """Custom type alaQoSConfigReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSConfigReset_Type.__name__ = "Integer32"
_AlaQoSConfigReset_Object = MibScalar
alaQoSConfigReset = _AlaQoSConfigReset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 11),
    _AlaQoSConfigReset_Type()
)
alaQoSConfigReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigReset.setStatus("current")


class _AlaQoSConfigStatsReset_Type(Integer32):
    """Custom type alaQoSConfigStatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSConfigStatsReset_Type.__name__ = "Integer32"
_AlaQoSConfigStatsReset_Object = MibScalar
alaQoSConfigStatsReset = _AlaQoSConfigStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 12),
    _AlaQoSConfigStatsReset_Type()
)
alaQoSConfigStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigStatsReset.setStatus("current")


class _AlaQoSConfigFlush_Type(Integer32):
    """Custom type alaQoSConfigFlush based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSConfigFlush_Type.__name__ = "Integer32"
_AlaQoSConfigFlush_Object = MibScalar
alaQoSConfigFlush = _AlaQoSConfigFlush_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 13),
    _AlaQoSConfigFlush_Type()
)
alaQoSConfigFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigFlush.setStatus("current")
_AlaQoSConfigDebug_Type = Integer32
_AlaQoSConfigDebug_Object = MibScalar
alaQoSConfigDebug = _AlaQoSConfigDebug_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 14),
    _AlaQoSConfigDebug_Type()
)
alaQoSConfigDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigDebug.setStatus("current")
_AlaQoSConfigUserportFilter_Type = Integer32
_AlaQoSConfigUserportFilter_Object = MibScalar
alaQoSConfigUserportFilter = _AlaQoSConfigUserportFilter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 15),
    _AlaQoSConfigUserportFilter_Type()
)
alaQoSConfigUserportFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConfigUserportFilter.setStatus("current")
_AlaQoSConfigAppliedUserportFilter_Type = Integer32
_AlaQoSConfigAppliedUserportFilter_Object = MibScalar
alaQoSConfigAppliedUserportFilter = _AlaQoSConfigAppliedUserportFilter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 16),
    _AlaQoSConfigAppliedUserportFilter_Type()
)
alaQoSConfigAppliedUserportFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSConfigAppliedUserportFilter.setStatus("current")
_AlaQoSConfigUserportShutdown_Type = Integer32
_AlaQoSConfigUserportShutdown_Object = MibScalar
alaQoSConfigUserportShutdown = _AlaQoSConfigUserportShutdown_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 17),
    _AlaQoSConfigUserportShutdown_Type()
)
alaQoSConfigUserportShutdown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConfigUserportShutdown.setStatus("current")
_AlaQoSConfigAppliedUserportShutdown_Type = Integer32
_AlaQoSConfigAppliedUserportShutdown_Object = MibScalar
alaQoSConfigAppliedUserportShutdown = _AlaQoSConfigAppliedUserportShutdown_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 18),
    _AlaQoSConfigAppliedUserportShutdown_Type()
)
alaQoSConfigAppliedUserportShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSConfigAppliedUserportShutdown.setStatus("current")


class _AlaQoSConfigAutoPhones_Type(Integer32):
    """Custom type alaQoSConfigAutoPhones based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("pri0", 0),
          ("pri1", 1),
          ("pri2", 2),
          ("pri3", 3),
          ("pri4", 4),
          ("pri5", 5),
          ("pri6", 6),
          ("pri7", 7),
          ("trusted", 8),
          ("disable", 9))
    )


_AlaQoSConfigAutoPhones_Type.__name__ = "Integer32"
_AlaQoSConfigAutoPhones_Object = MibScalar
alaQoSConfigAutoPhones = _AlaQoSConfigAutoPhones_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 19),
    _AlaQoSConfigAutoPhones_Type()
)
alaQoSConfigAutoPhones.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigAutoPhones.setStatus("current")


class _AlaQoSConfigQMPage_Type(Integer32):
    """Custom type alaQoSConfigQMPage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaQoSConfigQMPage_Type.__name__ = "Integer32"
_AlaQoSConfigQMPage_Object = MibScalar
alaQoSConfigQMPage = _AlaQoSConfigQMPage_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 20),
    _AlaQoSConfigQMPage_Type()
)
alaQoSConfigQMPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigQMPage.setStatus("current")


class _AlaQoSConfigQMMACGroup_Type(SnmpAdminString):
    """Custom type alaQoSConfigQMMACGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSConfigQMMACGroup_Type.__name__ = "SnmpAdminString"
_AlaQoSConfigQMMACGroup_Object = MibScalar
alaQoSConfigQMMACGroup = _AlaQoSConfigQMMACGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 21),
    _AlaQoSConfigQMMACGroup_Type()
)
alaQoSConfigQMMACGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigQMMACGroup.setStatus("current")


class _AlaQoSConfigQMPath_Type(SnmpAdminString):
    """Custom type alaQoSConfigQMPath based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaQoSConfigQMPath_Type.__name__ = "SnmpAdminString"
_AlaQoSConfigQMPath_Object = MibScalar
alaQoSConfigQMPath = _AlaQoSConfigQMPath_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 22),
    _AlaQoSConfigQMPath_Type()
)
alaQoSConfigQMPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigQMPath.setStatus("current")


class _AlaQoSConfigDEIMapping_Type(Integer32):
    """Custom type alaQoSConfigDEIMapping based on Integer32"""
    defaultValue = 2

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


_AlaQoSConfigDEIMapping_Type.__name__ = "Integer32"
_AlaQoSConfigDEIMapping_Object = MibScalar
alaQoSConfigDEIMapping = _AlaQoSConfigDEIMapping_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 23),
    _AlaQoSConfigDEIMapping_Type()
)
alaQoSConfigDEIMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConfigDEIMapping.setStatus("current")


class _AlaQoSConfigDEIMarking_Type(Integer32):
    """Custom type alaQoSConfigDEIMarking based on Integer32"""
    defaultValue = 2

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


_AlaQoSConfigDEIMarking_Type.__name__ = "Integer32"
_AlaQoSConfigDEIMarking_Object = MibScalar
alaQoSConfigDEIMarking = _AlaQoSConfigDEIMarking_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 24),
    _AlaQoSConfigDEIMarking_Type()
)
alaQoSConfigDEIMarking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConfigDEIMarking.setStatus("current")


class _AlaQoSConfigSwitchGroup_Type(Integer32):
    """Custom type alaQoSConfigSwitchGroup based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("expanded", 1),
          ("compact", 2))
    )


_AlaQoSConfigSwitchGroup_Type.__name__ = "Integer32"
_AlaQoSConfigSwitchGroup_Object = MibScalar
alaQoSConfigSwitchGroup = _AlaQoSConfigSwitchGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 25),
    _AlaQoSConfigSwitchGroup_Type()
)
alaQoSConfigSwitchGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigSwitchGroup.setStatus("current")


class _AlaQoSVmSnooping_Type(Integer32):
    """Custom type alaQoSVmSnooping based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disabled", 2))
    )


_AlaQoSVmSnooping_Type.__name__ = "Integer32"
_AlaQoSVmSnooping_Object = MibScalar
alaQoSVmSnooping = _AlaQoSVmSnooping_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 26),
    _AlaQoSVmSnooping_Type()
)
alaQoSVmSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSVmSnooping.setStatus("current")
_AlaQoSStats_ObjectIdentity = ObjectIdentity
alaQoSStats = _AlaQoSStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31)
)
_AlaQoSStatsSpoofedEvents_Type = Counter32
_AlaQoSStatsSpoofedEvents_Object = MibScalar
alaQoSStatsSpoofedEvents = _AlaQoSStatsSpoofedEvents_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 1),
    _AlaQoSStatsSpoofedEvents_Type()
)
alaQoSStatsSpoofedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsSpoofedEvents.setStatus("current")
_AlaQoSStatsNonSpoofedEvents_Type = Counter32
_AlaQoSStatsNonSpoofedEvents_Object = MibScalar
alaQoSStatsNonSpoofedEvents = _AlaQoSStatsNonSpoofedEvents_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 2),
    _AlaQoSStatsNonSpoofedEvents_Type()
)
alaQoSStatsNonSpoofedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsNonSpoofedEvents.setStatus("current")
_AlaQoSValidityPeriodTable_Object = MibTable
alaQoSValidityPeriodTable = _AlaQoSValidityPeriodTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32)
)
if mibBuilder.loadTexts:
    alaQoSValidityPeriodTable.setStatus("current")
_AlaQoSValidityPeriodEntry_Object = MibTableRow
alaQoSValidityPeriodEntry = _AlaQoSValidityPeriodEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1)
)
alaQoSValidityPeriodEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSValidityPeriodName"),
)
if mibBuilder.loadTexts:
    alaQoSValidityPeriodEntry.setStatus("current")


class _AlaQoSValidityPeriodName_Type(SnmpAdminString):
    """Custom type alaQoSValidityPeriodName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSValidityPeriodName_Type.__name__ = "SnmpAdminString"
_AlaQoSValidityPeriodName_Object = MibTableColumn
alaQoSValidityPeriodName = _AlaQoSValidityPeriodName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 1),
    _AlaQoSValidityPeriodName_Type()
)
alaQoSValidityPeriodName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSValidityPeriodName.setStatus("current")


class _AlaQoSValidityPeriodSource_Type(Integer32):
    """Custom type alaQoSValidityPeriodSource based on Integer32"""
    defaultValue = 2

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
        *(("ldap", 1),
          ("cli", 2),
          ("blt", 3),
          ("api", 4),
          ("imp", 5))
    )


_AlaQoSValidityPeriodSource_Type.__name__ = "Integer32"
_AlaQoSValidityPeriodSource_Object = MibTableColumn
alaQoSValidityPeriodSource = _AlaQoSValidityPeriodSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 2),
    _AlaQoSValidityPeriodSource_Type()
)
alaQoSValidityPeriodSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSValidityPeriodSource.setStatus("current")
_AlaQoSValidityPeriodDays_Type = Integer32
_AlaQoSValidityPeriodDays_Object = MibTableColumn
alaQoSValidityPeriodDays = _AlaQoSValidityPeriodDays_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 3),
    _AlaQoSValidityPeriodDays_Type()
)
alaQoSValidityPeriodDays.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSValidityPeriodDays.setStatus("current")


class _AlaQoSValidityPeriodDaysStatus_Type(Integer32):
    """Custom type alaQoSValidityPeriodDaysStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSValidityPeriodDaysStatus_Type.__name__ = "Integer32"
_AlaQoSValidityPeriodDaysStatus_Object = MibTableColumn
alaQoSValidityPeriodDaysStatus = _AlaQoSValidityPeriodDaysStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 4),
    _AlaQoSValidityPeriodDaysStatus_Type()
)
alaQoSValidityPeriodDaysStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSValidityPeriodDaysStatus.setStatus("current")
_AlaQoSValidityPeriodMonths_Type = Integer32
_AlaQoSValidityPeriodMonths_Object = MibTableColumn
alaQoSValidityPeriodMonths = _AlaQoSValidityPeriodMonths_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 5),
    _AlaQoSValidityPeriodMonths_Type()
)
alaQoSValidityPeriodMonths.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSValidityPeriodMonths.setStatus("current")


class _AlaQoSValidityPeriodMonthsStatus_Type(Integer32):
    """Custom type alaQoSValidityPeriodMonthsStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSValidityPeriodMonthsStatus_Type.__name__ = "Integer32"
_AlaQoSValidityPeriodMonthsStatus_Object = MibTableColumn
alaQoSValidityPeriodMonthsStatus = _AlaQoSValidityPeriodMonthsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 6),
    _AlaQoSValidityPeriodMonthsStatus_Type()
)
alaQoSValidityPeriodMonthsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSValidityPeriodMonthsStatus.setStatus("current")


class _AlaQoSValidityPeriodHour_Type(SnmpAdminString):
    """Custom type alaQoSValidityPeriodHour based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_AlaQoSValidityPeriodHour_Type.__name__ = "SnmpAdminString"
_AlaQoSValidityPeriodHour_Object = MibTableColumn
alaQoSValidityPeriodHour = _AlaQoSValidityPeriodHour_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 7),
    _AlaQoSValidityPeriodHour_Type()
)
alaQoSValidityPeriodHour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSValidityPeriodHour.setStatus("current")


class _AlaQoSValidityPeriodHourStatus_Type(Integer32):
    """Custom type alaQoSValidityPeriodHourStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSValidityPeriodHourStatus_Type.__name__ = "Integer32"
_AlaQoSValidityPeriodHourStatus_Object = MibTableColumn
alaQoSValidityPeriodHourStatus = _AlaQoSValidityPeriodHourStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 8),
    _AlaQoSValidityPeriodHourStatus_Type()
)
alaQoSValidityPeriodHourStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSValidityPeriodHourStatus.setStatus("current")


class _AlaQoSValidityPeriodEndHour_Type(SnmpAdminString):
    """Custom type alaQoSValidityPeriodEndHour based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_AlaQoSValidityPeriodEndHour_Type.__name__ = "SnmpAdminString"
_AlaQoSValidityPeriodEndHour_Object = MibTableColumn
alaQoSValidityPeriodEndHour = _AlaQoSValidityPeriodEndHour_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 9),
    _AlaQoSValidityPeriodEndHour_Type()
)
alaQoSValidityPeriodEndHour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSValidityPeriodEndHour.setStatus("current")


class _AlaQoSValidityPeriodInterval_Type(SnmpAdminString):
    """Custom type alaQoSValidityPeriodInterval based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_AlaQoSValidityPeriodInterval_Type.__name__ = "SnmpAdminString"
_AlaQoSValidityPeriodInterval_Object = MibTableColumn
alaQoSValidityPeriodInterval = _AlaQoSValidityPeriodInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 10),
    _AlaQoSValidityPeriodInterval_Type()
)
alaQoSValidityPeriodInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSValidityPeriodInterval.setStatus("current")


class _AlaQoSValidityPeriodIntervalStatus_Type(Integer32):
    """Custom type alaQoSValidityPeriodIntervalStatus based on Integer32"""
    defaultValue = 2

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


_AlaQoSValidityPeriodIntervalStatus_Type.__name__ = "Integer32"
_AlaQoSValidityPeriodIntervalStatus_Object = MibTableColumn
alaQoSValidityPeriodIntervalStatus = _AlaQoSValidityPeriodIntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 11),
    _AlaQoSValidityPeriodIntervalStatus_Type()
)
alaQoSValidityPeriodIntervalStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSValidityPeriodIntervalStatus.setStatus("current")


class _AlaQoSValidityPeriodEndInterval_Type(SnmpAdminString):
    """Custom type alaQoSValidityPeriodEndInterval based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_AlaQoSValidityPeriodEndInterval_Type.__name__ = "SnmpAdminString"
_AlaQoSValidityPeriodEndInterval_Object = MibTableColumn
alaQoSValidityPeriodEndInterval = _AlaQoSValidityPeriodEndInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 12),
    _AlaQoSValidityPeriodEndInterval_Type()
)
alaQoSValidityPeriodEndInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSValidityPeriodEndInterval.setStatus("current")
_AlaQoSValidityPeriodRowStatus_Type = RowStatus
_AlaQoSValidityPeriodRowStatus_Object = MibTableColumn
alaQoSValidityPeriodRowStatus = _AlaQoSValidityPeriodRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 13),
    _AlaQoSValidityPeriodRowStatus_Type()
)
alaQoSValidityPeriodRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSValidityPeriodRowStatus.setStatus("current")
_AlaQoSAppliedValidityPeriodTable_Object = MibTable
alaQoSAppliedValidityPeriodTable = _AlaQoSAppliedValidityPeriodTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33)
)
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodTable.setStatus("current")
_AlaQoSAppliedValidityPeriodEntry_Object = MibTableRow
alaQoSAppliedValidityPeriodEntry = _AlaQoSAppliedValidityPeriodEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1)
)
alaQoSAppliedValidityPeriodEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedValidityPeriodName"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodEntry.setStatus("current")


class _AlaQoSAppliedValidityPeriodName_Type(SnmpAdminString):
    """Custom type alaQoSAppliedValidityPeriodName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedValidityPeriodName_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedValidityPeriodName_Object = MibTableColumn
alaQoSAppliedValidityPeriodName = _AlaQoSAppliedValidityPeriodName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 1),
    _AlaQoSAppliedValidityPeriodName_Type()
)
alaQoSAppliedValidityPeriodName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodName.setStatus("current")


class _AlaQoSAppliedValidityPeriodSource_Type(Integer32):
    """Custom type alaQoSAppliedValidityPeriodSource based on Integer32"""
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
        *(("ldap", 1),
          ("cli", 2),
          ("blt", 3),
          ("api", 4),
          ("imp", 5))
    )


_AlaQoSAppliedValidityPeriodSource_Type.__name__ = "Integer32"
_AlaQoSAppliedValidityPeriodSource_Object = MibTableColumn
alaQoSAppliedValidityPeriodSource = _AlaQoSAppliedValidityPeriodSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 2),
    _AlaQoSAppliedValidityPeriodSource_Type()
)
alaQoSAppliedValidityPeriodSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodSource.setStatus("current")
_AlaQoSAppliedValidityPeriodDays_Type = Integer32
_AlaQoSAppliedValidityPeriodDays_Object = MibTableColumn
alaQoSAppliedValidityPeriodDays = _AlaQoSAppliedValidityPeriodDays_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 3),
    _AlaQoSAppliedValidityPeriodDays_Type()
)
alaQoSAppliedValidityPeriodDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodDays.setStatus("current")


class _AlaQoSAppliedValidityPeriodDaysStatus_Type(Integer32):
    """Custom type alaQoSAppliedValidityPeriodDaysStatus based on Integer32"""
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


_AlaQoSAppliedValidityPeriodDaysStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedValidityPeriodDaysStatus_Object = MibTableColumn
alaQoSAppliedValidityPeriodDaysStatus = _AlaQoSAppliedValidityPeriodDaysStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 4),
    _AlaQoSAppliedValidityPeriodDaysStatus_Type()
)
alaQoSAppliedValidityPeriodDaysStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodDaysStatus.setStatus("current")
_AlaQoSAppliedValidityPeriodMonths_Type = Integer32
_AlaQoSAppliedValidityPeriodMonths_Object = MibTableColumn
alaQoSAppliedValidityPeriodMonths = _AlaQoSAppliedValidityPeriodMonths_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 5),
    _AlaQoSAppliedValidityPeriodMonths_Type()
)
alaQoSAppliedValidityPeriodMonths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodMonths.setStatus("current")


class _AlaQoSAppliedValidityPeriodMonthsStatus_Type(Integer32):
    """Custom type alaQoSAppliedValidityPeriodMonthsStatus based on Integer32"""
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


_AlaQoSAppliedValidityPeriodMonthsStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedValidityPeriodMonthsStatus_Object = MibTableColumn
alaQoSAppliedValidityPeriodMonthsStatus = _AlaQoSAppliedValidityPeriodMonthsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 6),
    _AlaQoSAppliedValidityPeriodMonthsStatus_Type()
)
alaQoSAppliedValidityPeriodMonthsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodMonthsStatus.setStatus("current")


class _AlaQoSAppliedValidityPeriodHour_Type(SnmpAdminString):
    """Custom type alaQoSAppliedValidityPeriodHour based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_AlaQoSAppliedValidityPeriodHour_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedValidityPeriodHour_Object = MibTableColumn
alaQoSAppliedValidityPeriodHour = _AlaQoSAppliedValidityPeriodHour_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 7),
    _AlaQoSAppliedValidityPeriodHour_Type()
)
alaQoSAppliedValidityPeriodHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodHour.setStatus("current")


class _AlaQoSAppliedValidityPeriodHourStatus_Type(Integer32):
    """Custom type alaQoSAppliedValidityPeriodHourStatus based on Integer32"""
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


_AlaQoSAppliedValidityPeriodHourStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedValidityPeriodHourStatus_Object = MibTableColumn
alaQoSAppliedValidityPeriodHourStatus = _AlaQoSAppliedValidityPeriodHourStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 8),
    _AlaQoSAppliedValidityPeriodHourStatus_Type()
)
alaQoSAppliedValidityPeriodHourStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodHourStatus.setStatus("current")


class _AlaQoSAppliedValidityPeriodEndHour_Type(SnmpAdminString):
    """Custom type alaQoSAppliedValidityPeriodEndHour based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_AlaQoSAppliedValidityPeriodEndHour_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedValidityPeriodEndHour_Object = MibTableColumn
alaQoSAppliedValidityPeriodEndHour = _AlaQoSAppliedValidityPeriodEndHour_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 9),
    _AlaQoSAppliedValidityPeriodEndHour_Type()
)
alaQoSAppliedValidityPeriodEndHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodEndHour.setStatus("current")


class _AlaQoSAppliedValidityPeriodInterval_Type(SnmpAdminString):
    """Custom type alaQoSAppliedValidityPeriodInterval based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_AlaQoSAppliedValidityPeriodInterval_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedValidityPeriodInterval_Object = MibTableColumn
alaQoSAppliedValidityPeriodInterval = _AlaQoSAppliedValidityPeriodInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 10),
    _AlaQoSAppliedValidityPeriodInterval_Type()
)
alaQoSAppliedValidityPeriodInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodInterval.setStatus("current")


class _AlaQoSAppliedValidityPeriodIntervalStatus_Type(Integer32):
    """Custom type alaQoSAppliedValidityPeriodIntervalStatus based on Integer32"""
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


_AlaQoSAppliedValidityPeriodIntervalStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedValidityPeriodIntervalStatus_Object = MibTableColumn
alaQoSAppliedValidityPeriodIntervalStatus = _AlaQoSAppliedValidityPeriodIntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 11),
    _AlaQoSAppliedValidityPeriodIntervalStatus_Type()
)
alaQoSAppliedValidityPeriodIntervalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodIntervalStatus.setStatus("current")


class _AlaQoSAppliedValidityPeriodEndInterval_Type(SnmpAdminString):
    """Custom type alaQoSAppliedValidityPeriodEndInterval based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_AlaQoSAppliedValidityPeriodEndInterval_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedValidityPeriodEndInterval_Object = MibTableColumn
alaQoSAppliedValidityPeriodEndInterval = _AlaQoSAppliedValidityPeriodEndInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 12),
    _AlaQoSAppliedValidityPeriodEndInterval_Type()
)
alaQoSAppliedValidityPeriodEndInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodEndInterval.setStatus("current")
_AlaQoSAppliedValidityPeriodRowStatus_Type = RowStatus
_AlaQoSAppliedValidityPeriodRowStatus_Object = MibTableColumn
alaQoSAppliedValidityPeriodRowStatus = _AlaQoSAppliedValidityPeriodRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 13),
    _AlaQoSAppliedValidityPeriodRowStatus_Type()
)
alaQoSAppliedValidityPeriodRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodRowStatus.setStatus("current")
_AlaQoSRuleGroupsTable_Object = MibTable
alaQoSRuleGroupsTable = _AlaQoSRuleGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34)
)
if mibBuilder.loadTexts:
    alaQoSRuleGroupsTable.setStatus("current")
_AlaQoSRuleGroupsEntry_Object = MibTableRow
alaQoSRuleGroupsEntry = _AlaQoSRuleGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 1)
)
alaQoSRuleGroupsEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSRuleGroupsName"),
)
if mibBuilder.loadTexts:
    alaQoSRuleGroupsEntry.setStatus("current")


class _AlaQoSRuleGroupsName_Type(SnmpAdminString):
    """Custom type alaQoSRuleGroupsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSRuleGroupsName_Type.__name__ = "SnmpAdminString"
_AlaQoSRuleGroupsName_Object = MibTableColumn
alaQoSRuleGroupsName = _AlaQoSRuleGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 1, 1),
    _AlaQoSRuleGroupsName_Type()
)
alaQoSRuleGroupsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSRuleGroupsName.setStatus("current")


class _AlaQoSRuleGroupsSource_Type(Integer32):
    """Custom type alaQoSRuleGroupsSource based on Integer32"""
    defaultValue = 2

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
        *(("ldap", 1),
          ("cli", 2),
          ("blt", 3),
          ("api", 4),
          ("imp", 5))
    )


_AlaQoSRuleGroupsSource_Type.__name__ = "Integer32"
_AlaQoSRuleGroupsSource_Object = MibTableColumn
alaQoSRuleGroupsSource = _AlaQoSRuleGroupsSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 1, 2),
    _AlaQoSRuleGroupsSource_Type()
)
alaQoSRuleGroupsSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleGroupsSource.setStatus("current")


class _AlaQoSRuleGroupsType_Type(Integer32):
    """Custom type alaQoSRuleGroupsType based on Integer32"""
    defaultValue = 3

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
        *(("default", 1),
          ("egress", 2),
          ("unp", 3),
          ("appfp", 4),
          ("empacl", 5))
    )


_AlaQoSRuleGroupsType_Type.__name__ = "Integer32"
_AlaQoSRuleGroupsType_Object = MibTableColumn
alaQoSRuleGroupsType = _AlaQoSRuleGroupsType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 1, 3),
    _AlaQoSRuleGroupsType_Type()
)
alaQoSRuleGroupsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleGroupsType.setStatus("current")


class _AlaQoSRuleGroupsEnabled_Type(Integer32):
    """Custom type alaQoSRuleGroupsEnabled based on Integer32"""
    defaultValue = 1

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


_AlaQoSRuleGroupsEnabled_Type.__name__ = "Integer32"
_AlaQoSRuleGroupsEnabled_Object = MibTableColumn
alaQoSRuleGroupsEnabled = _AlaQoSRuleGroupsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 1, 4),
    _AlaQoSRuleGroupsEnabled_Type()
)
alaQoSRuleGroupsEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleGroupsEnabled.setStatus("current")
_AlaQoSRuleGroupsStatus_Type = RowStatus
_AlaQoSRuleGroupsStatus_Object = MibTableColumn
alaQoSRuleGroupsStatus = _AlaQoSRuleGroupsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 1, 5),
    _AlaQoSRuleGroupsStatus_Type()
)
alaQoSRuleGroupsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleGroupsStatus.setStatus("current")
_AlaQoSAppliedRuleGroupsTable_Object = MibTable
alaQoSAppliedRuleGroupsTable = _AlaQoSAppliedRuleGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 35)
)
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupsTable.setStatus("current")
_AlaQoSAppliedRuleGroupsEntry_Object = MibTableRow
alaQoSAppliedRuleGroupsEntry = _AlaQoSAppliedRuleGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 35, 1)
)
alaQoSAppliedRuleGroupsEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleGroupsName"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupsEntry.setStatus("current")


class _AlaQoSAppliedRuleGroupsName_Type(SnmpAdminString):
    """Custom type alaQoSAppliedRuleGroupsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedRuleGroupsName_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedRuleGroupsName_Object = MibTableColumn
alaQoSAppliedRuleGroupsName = _AlaQoSAppliedRuleGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 35, 1, 1),
    _AlaQoSAppliedRuleGroupsName_Type()
)
alaQoSAppliedRuleGroupsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupsName.setStatus("current")


class _AlaQoSAppliedRuleGroupsSource_Type(Integer32):
    """Custom type alaQoSAppliedRuleGroupsSource based on Integer32"""
    defaultValue = 2

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
        *(("ldap", 1),
          ("cli", 2),
          ("blt", 3),
          ("api", 4),
          ("imp", 5))
    )


_AlaQoSAppliedRuleGroupsSource_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleGroupsSource_Object = MibTableColumn
alaQoSAppliedRuleGroupsSource = _AlaQoSAppliedRuleGroupsSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 35, 1, 2),
    _AlaQoSAppliedRuleGroupsSource_Type()
)
alaQoSAppliedRuleGroupsSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupsSource.setStatus("current")


class _AlaQoSAppliedRuleGroupsType_Type(Integer32):
    """Custom type alaQoSAppliedRuleGroupsType based on Integer32"""
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
        *(("default", 1),
          ("egress", 2),
          ("unp", 3),
          ("appfp", 4))
    )


_AlaQoSAppliedRuleGroupsType_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleGroupsType_Object = MibTableColumn
alaQoSAppliedRuleGroupsType = _AlaQoSAppliedRuleGroupsType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 35, 1, 3),
    _AlaQoSAppliedRuleGroupsType_Type()
)
alaQoSAppliedRuleGroupsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupsType.setStatus("current")


class _AlaQoSAppliedRuleGroupsEnabled_Type(Integer32):
    """Custom type alaQoSAppliedRuleGroupsEnabled based on Integer32"""
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


_AlaQoSAppliedRuleGroupsEnabled_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleGroupsEnabled_Object = MibTableColumn
alaQoSAppliedRuleGroupsEnabled = _AlaQoSAppliedRuleGroupsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 35, 1, 4),
    _AlaQoSAppliedRuleGroupsEnabled_Type()
)
alaQoSAppliedRuleGroupsEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupsEnabled.setStatus("current")
_AlaQoSAppliedRuleGroupsStatus_Type = RowStatus
_AlaQoSAppliedRuleGroupsStatus_Object = MibTableColumn
alaQoSAppliedRuleGroupsStatus = _AlaQoSAppliedRuleGroupsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 35, 1, 5),
    _AlaQoSAppliedRuleGroupsStatus_Type()
)
alaQoSAppliedRuleGroupsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupsStatus.setStatus("current")
_AlaQoSRuleGroupTable_Object = MibTable
alaQoSRuleGroupTable = _AlaQoSRuleGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 36)
)
if mibBuilder.loadTexts:
    alaQoSRuleGroupTable.setStatus("current")
_AlaQoSRuleGroupEntry_Object = MibTableRow
alaQoSRuleGroupEntry = _AlaQoSRuleGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 36, 1)
)
alaQoSRuleGroupEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSRuleGroupsName"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSRuleGroupRuleName"),
)
if mibBuilder.loadTexts:
    alaQoSRuleGroupEntry.setStatus("current")


class _AlaQoSRuleGroupRuleName_Type(SnmpAdminString):
    """Custom type alaQoSRuleGroupRuleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSRuleGroupRuleName_Type.__name__ = "SnmpAdminString"
_AlaQoSRuleGroupRuleName_Object = MibTableColumn
alaQoSRuleGroupRuleName = _AlaQoSRuleGroupRuleName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 36, 1, 1),
    _AlaQoSRuleGroupRuleName_Type()
)
alaQoSRuleGroupRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSRuleGroupRuleName.setStatus("current")
_AlaQoSRuleGroupMatches_Type = Counter32
_AlaQoSRuleGroupMatches_Object = MibTableColumn
alaQoSRuleGroupMatches = _AlaQoSRuleGroupMatches_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 36, 1, 2),
    _AlaQoSRuleGroupMatches_Type()
)
alaQoSRuleGroupMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRuleGroupMatches.setStatus("current")


class _AlaQoSRuleGroupCountType_Type(Integer32):
    """Custom type alaQoSRuleGroupCountType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packets", 1),
          ("bytes", 2))
    )


_AlaQoSRuleGroupCountType_Type.__name__ = "Integer32"
_AlaQoSRuleGroupCountType_Object = MibTableColumn
alaQoSRuleGroupCountType = _AlaQoSRuleGroupCountType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 36, 1, 3),
    _AlaQoSRuleGroupCountType_Type()
)
alaQoSRuleGroupCountType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleGroupCountType.setStatus("current")
_AlaQoSRuleGroupPacketCount_Type = Counter64
_AlaQoSRuleGroupPacketCount_Object = MibTableColumn
alaQoSRuleGroupPacketCount = _AlaQoSRuleGroupPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 36, 1, 4),
    _AlaQoSRuleGroupPacketCount_Type()
)
alaQoSRuleGroupPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRuleGroupPacketCount.setStatus("current")
_AlaQoSRuleGroupByteCount_Type = Counter64
_AlaQoSRuleGroupByteCount_Object = MibTableColumn
alaQoSRuleGroupByteCount = _AlaQoSRuleGroupByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 36, 1, 5),
    _AlaQoSRuleGroupByteCount_Type()
)
alaQoSRuleGroupByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRuleGroupByteCount.setStatus("current")
_AlaQoSRuleGroupStatus_Type = RowStatus
_AlaQoSRuleGroupStatus_Object = MibTableColumn
alaQoSRuleGroupStatus = _AlaQoSRuleGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 36, 1, 6),
    _AlaQoSRuleGroupStatus_Type()
)
alaQoSRuleGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleGroupStatus.setStatus("current")
_AlaQoSAppliedRuleGroupTable_Object = MibTable
alaQoSAppliedRuleGroupTable = _AlaQoSAppliedRuleGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 37)
)
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupTable.setStatus("current")
_AlaQoSAppliedRuleGroupEntry_Object = MibTableRow
alaQoSAppliedRuleGroupEntry = _AlaQoSAppliedRuleGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 37, 1)
)
alaQoSAppliedRuleGroupEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleGroupsName"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleGroupRuleName"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupEntry.setStatus("current")


class _AlaQoSAppliedRuleGroupRuleName_Type(SnmpAdminString):
    """Custom type alaQoSAppliedRuleGroupRuleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedRuleGroupRuleName_Type.__name__ = "SnmpAdminString"
_AlaQoSAppliedRuleGroupRuleName_Object = MibTableColumn
alaQoSAppliedRuleGroupRuleName = _AlaQoSAppliedRuleGroupRuleName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 37, 1, 1),
    _AlaQoSAppliedRuleGroupRuleName_Type()
)
alaQoSAppliedRuleGroupRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupRuleName.setStatus("current")
_AlaQoSAppliedRuleGroupMatches_Type = Counter32
_AlaQoSAppliedRuleGroupMatches_Object = MibTableColumn
alaQoSAppliedRuleGroupMatches = _AlaQoSAppliedRuleGroupMatches_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 37, 1, 2),
    _AlaQoSAppliedRuleGroupMatches_Type()
)
alaQoSAppliedRuleGroupMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupMatches.setStatus("current")


class _AlaQoSAppliedRuleGroupCountType_Type(Integer32):
    """Custom type alaQoSAppliedRuleGroupCountType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packets", 1),
          ("bytes", 2))
    )


_AlaQoSAppliedRuleGroupCountType_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleGroupCountType_Object = MibTableColumn
alaQoSAppliedRuleGroupCountType = _AlaQoSAppliedRuleGroupCountType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 37, 1, 3),
    _AlaQoSAppliedRuleGroupCountType_Type()
)
alaQoSAppliedRuleGroupCountType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupCountType.setStatus("current")
_AlaQoSAppliedRuleGroupPacketCount_Type = Counter64
_AlaQoSAppliedRuleGroupPacketCount_Object = MibTableColumn
alaQoSAppliedRuleGroupPacketCount = _AlaQoSAppliedRuleGroupPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 37, 1, 4),
    _AlaQoSAppliedRuleGroupPacketCount_Type()
)
alaQoSAppliedRuleGroupPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupPacketCount.setStatus("current")
_AlaQoSAppliedRuleGroupByteCount_Type = Counter64
_AlaQoSAppliedRuleGroupByteCount_Object = MibTableColumn
alaQoSAppliedRuleGroupByteCount = _AlaQoSAppliedRuleGroupByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 37, 1, 5),
    _AlaQoSAppliedRuleGroupByteCount_Type()
)
alaQoSAppliedRuleGroupByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupByteCount.setStatus("current")
_AlaQoSAppliedRuleGroupStatus_Type = RowStatus
_AlaQoSAppliedRuleGroupStatus_Object = MibTableColumn
alaQoSAppliedRuleGroupStatus = _AlaQoSAppliedRuleGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 37, 1, 6),
    _AlaQoSAppliedRuleGroupStatus_Type()
)
alaQoSAppliedRuleGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupStatus.setStatus("current")
_AlaQoSV6NetworkGroupTable_Object = MibTable
alaQoSV6NetworkGroupTable = _AlaQoSV6NetworkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 40)
)
if mibBuilder.loadTexts:
    alaQoSV6NetworkGroupTable.setStatus("current")
_AlaQoSV6NetworkGroupEntry_Object = MibTableRow
alaQoSV6NetworkGroupEntry = _AlaQoSV6NetworkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 40, 1)
)
alaQoSV6NetworkGroupEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSNetworkGroupsName"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSV6NetworkGroupIpAddr"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSV6NetworkGroupIpMask"),
)
if mibBuilder.loadTexts:
    alaQoSV6NetworkGroupEntry.setStatus("current")
_AlaQoSV6NetworkGroupIpAddr_Type = Ipv6Address
_AlaQoSV6NetworkGroupIpAddr_Object = MibTableColumn
alaQoSV6NetworkGroupIpAddr = _AlaQoSV6NetworkGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 40, 1, 1),
    _AlaQoSV6NetworkGroupIpAddr_Type()
)
alaQoSV6NetworkGroupIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSV6NetworkGroupIpAddr.setStatus("current")
_AlaQoSV6NetworkGroupIpMask_Type = Ipv6Address
_AlaQoSV6NetworkGroupIpMask_Object = MibTableColumn
alaQoSV6NetworkGroupIpMask = _AlaQoSV6NetworkGroupIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 40, 1, 2),
    _AlaQoSV6NetworkGroupIpMask_Type()
)
alaQoSV6NetworkGroupIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSV6NetworkGroupIpMask.setStatus("current")
_AlaQoSV6NetworkGroupStatus_Type = RowStatus
_AlaQoSV6NetworkGroupStatus_Object = MibTableColumn
alaQoSV6NetworkGroupStatus = _AlaQoSV6NetworkGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 40, 1, 3),
    _AlaQoSV6NetworkGroupStatus_Type()
)
alaQoSV6NetworkGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSV6NetworkGroupStatus.setStatus("current")
_AlaQoSAppliedV6NetworkGroupTable_Object = MibTable
alaQoSAppliedV6NetworkGroupTable = _AlaQoSAppliedV6NetworkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 41)
)
if mibBuilder.loadTexts:
    alaQoSAppliedV6NetworkGroupTable.setStatus("current")
_AlaQoSAppliedV6NetworkGroupEntry_Object = MibTableRow
alaQoSAppliedV6NetworkGroupEntry = _AlaQoSAppliedV6NetworkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 41, 1)
)
alaQoSAppliedV6NetworkGroupEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedNetworkGroupsName"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedV6NetworkGroupIpAddr"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedV6NetworkGroupIpMask"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedV6NetworkGroupEntry.setStatus("current")
_AlaQoSAppliedV6NetworkGroupIpAddr_Type = Ipv6Address
_AlaQoSAppliedV6NetworkGroupIpAddr_Object = MibTableColumn
alaQoSAppliedV6NetworkGroupIpAddr = _AlaQoSAppliedV6NetworkGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 41, 1, 1),
    _AlaQoSAppliedV6NetworkGroupIpAddr_Type()
)
alaQoSAppliedV6NetworkGroupIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedV6NetworkGroupIpAddr.setStatus("current")
_AlaQoSAppliedV6NetworkGroupIpMask_Type = Ipv6Address
_AlaQoSAppliedV6NetworkGroupIpMask_Object = MibTableColumn
alaQoSAppliedV6NetworkGroupIpMask = _AlaQoSAppliedV6NetworkGroupIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 41, 1, 2),
    _AlaQoSAppliedV6NetworkGroupIpMask_Type()
)
alaQoSAppliedV6NetworkGroupIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedV6NetworkGroupIpMask.setStatus("current")
_AlaQoSAppliedV6NetworkGroupStatus_Type = RowStatus
_AlaQoSAppliedV6NetworkGroupStatus_Object = MibTableColumn
alaQoSAppliedV6NetworkGroupStatus = _AlaQoSAppliedV6NetworkGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 41, 1, 3),
    _AlaQoSAppliedV6NetworkGroupStatus_Type()
)
alaQoSAppliedV6NetworkGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedV6NetworkGroupStatus.setStatus("current")
_AlaQoSDSCPTable_Object = MibTable
alaQoSDSCPTable = _AlaQoSDSCPTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 55)
)
if mibBuilder.loadTexts:
    alaQoSDSCPTable.setStatus("current")
_AlaQoSDSCPEntry_Object = MibTableRow
alaQoSDSCPEntry = _AlaQoSDSCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 55, 1)
)
alaQoSDSCPEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSDSCPEntryNumber"),
)
if mibBuilder.loadTexts:
    alaQoSDSCPEntry.setStatus("current")


class _AlaQoSDSCPEntryNumber_Type(Integer32):
    """Custom type alaQoSDSCPEntryNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_AlaQoSDSCPEntryNumber_Type.__name__ = "Integer32"
_AlaQoSDSCPEntryNumber_Object = MibTableColumn
alaQoSDSCPEntryNumber = _AlaQoSDSCPEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 55, 1, 1),
    _AlaQoSDSCPEntryNumber_Type()
)
alaQoSDSCPEntryNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSDSCPEntryNumber.setStatus("current")
_AlaQoSDSCPPriority_Type = Integer32
_AlaQoSDSCPPriority_Object = MibTableColumn
alaQoSDSCPPriority = _AlaQoSDSCPPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 55, 1, 2),
    _AlaQoSDSCPPriority_Type()
)
alaQoSDSCPPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSDSCPPriority.setStatus("current")


class _AlaQoSDSCPDropPrecedence_Type(Integer32):
    """Custom type alaQoSDSCPDropPrecedence based on Integer32"""
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
        *(("low", 1),
          ("medium", 2),
          ("high", 3))
    )


_AlaQoSDSCPDropPrecedence_Type.__name__ = "Integer32"
_AlaQoSDSCPDropPrecedence_Object = MibTableColumn
alaQoSDSCPDropPrecedence = _AlaQoSDSCPDropPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 55, 1, 3),
    _AlaQoSDSCPDropPrecedence_Type()
)
alaQoSDSCPDropPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSDSCPDropPrecedence.setStatus("current")
_AlaQoSDSCPRowStatus_Type = RowStatus
_AlaQoSDSCPRowStatus_Object = MibTableColumn
alaQoSDSCPRowStatus = _AlaQoSDSCPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 55, 1, 4),
    _AlaQoSDSCPRowStatus_Type()
)
alaQoSDSCPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSDSCPRowStatus.setStatus("current")
_AlaQoSAutoMacRangeTable_Object = MibTable
alaQoSAutoMacRangeTable = _AlaQoSAutoMacRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 56)
)
if mibBuilder.loadTexts:
    alaQoSAutoMacRangeTable.setStatus("current")
_AlaQoSAutoMacRangeEntry_Object = MibTableRow
alaQoSAutoMacRangeEntry = _AlaQoSAutoMacRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 56, 1)
)
alaQoSAutoMacRangeEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSAutoMacRangeIndex"),
)
if mibBuilder.loadTexts:
    alaQoSAutoMacRangeEntry.setStatus("current")
_AlaQoSAutoMacRangeIndex_Type = Unsigned32
_AlaQoSAutoMacRangeIndex_Object = MibTableColumn
alaQoSAutoMacRangeIndex = _AlaQoSAutoMacRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 56, 1, 1),
    _AlaQoSAutoMacRangeIndex_Type()
)
alaQoSAutoMacRangeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAutoMacRangeIndex.setStatus("current")
_AlaQoSAutoMacRangeStart_Type = MacAddress
_AlaQoSAutoMacRangeStart_Object = MibTableColumn
alaQoSAutoMacRangeStart = _AlaQoSAutoMacRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 56, 1, 2),
    _AlaQoSAutoMacRangeStart_Type()
)
alaQoSAutoMacRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAutoMacRangeStart.setStatus("current")
_AlaQoSAutoMacRangeEnd_Type = MacAddress
_AlaQoSAutoMacRangeEnd_Object = MibTableColumn
alaQoSAutoMacRangeEnd = _AlaQoSAutoMacRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 56, 1, 3),
    _AlaQoSAutoMacRangeEnd_Type()
)
alaQoSAutoMacRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAutoMacRangeEnd.setStatus("current")
_AlaQoSExtendedRuleTable_Object = MibTable
alaQoSExtendedRuleTable = _AlaQoSExtendedRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 57)
)
if mibBuilder.loadTexts:
    alaQoSExtendedRuleTable.setStatus("current")
_AlaQoSExtendedRuleEntry_Object = MibTableRow
alaQoSExtendedRuleEntry = _AlaQoSExtendedRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 57, 1)
)
alaQoSExtendedRuleEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSRuleName"),
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSExtendedRuleSplitRuleID"),
)
if mibBuilder.loadTexts:
    alaQoSExtendedRuleEntry.setStatus("current")


class _AlaQoSExtendedRuleSplitRuleID_Type(Unsigned32):
    """Custom type alaQoSExtendedRuleSplitRuleID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_AlaQoSExtendedRuleSplitRuleID_Type.__name__ = "Unsigned32"
_AlaQoSExtendedRuleSplitRuleID_Object = MibTableColumn
alaQoSExtendedRuleSplitRuleID = _AlaQoSExtendedRuleSplitRuleID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 57, 1, 1),
    _AlaQoSExtendedRuleSplitRuleID_Type()
)
alaQoSExtendedRuleSplitRuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSExtendedRuleSplitRuleID.setStatus("current")


class _AlaQoSExtendedRuleChassis_Type(Integer32):
    """Custom type alaQoSExtendedRuleChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSExtendedRuleChassis_Type.__name__ = "Integer32"
_AlaQoSExtendedRuleChassis_Object = MibTableColumn
alaQoSExtendedRuleChassis = _AlaQoSExtendedRuleChassis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 57, 1, 2),
    _AlaQoSExtendedRuleChassis_Type()
)
alaQoSExtendedRuleChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSExtendedRuleChassis.setStatus("current")


class _AlaQoSExtendedRuleSlot_Type(Integer32):
    """Custom type alaQoSExtendedRuleSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSExtendedRuleSlot_Type.__name__ = "Integer32"
_AlaQoSExtendedRuleSlot_Object = MibTableColumn
alaQoSExtendedRuleSlot = _AlaQoSExtendedRuleSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 57, 1, 3),
    _AlaQoSExtendedRuleSlot_Type()
)
alaQoSExtendedRuleSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSExtendedRuleSlot.setStatus("current")


class _AlaQoSExtendedRulePort_Type(Integer32):
    """Custom type alaQoSExtendedRulePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_AlaQoSExtendedRulePort_Type.__name__ = "Integer32"
_AlaQoSExtendedRulePort_Object = MibTableColumn
alaQoSExtendedRulePort = _AlaQoSExtendedRulePort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 57, 1, 4),
    _AlaQoSExtendedRulePort_Type()
)
alaQoSExtendedRulePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSExtendedRulePort.setStatus("current")
_AlaQoSExtendedRulePacketCount_Type = Counter64
_AlaQoSExtendedRulePacketCount_Object = MibTableColumn
alaQoSExtendedRulePacketCount = _AlaQoSExtendedRulePacketCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 57, 1, 5),
    _AlaQoSExtendedRulePacketCount_Type()
)
alaQoSExtendedRulePacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSExtendedRulePacketCount.setStatus("current")
_AlaQoSExtendedRuleByteCount_Type = Counter64
_AlaQoSExtendedRuleByteCount_Object = MibTableColumn
alaQoSExtendedRuleByteCount = _AlaQoSExtendedRuleByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 57, 1, 6),
    _AlaQoSExtendedRuleByteCount_Type()
)
alaQoSExtendedRuleByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSExtendedRuleByteCount.setStatus("current")
_AlaQoSExtendedRuleGreenPacketCount_Type = Counter64
_AlaQoSExtendedRuleGreenPacketCount_Object = MibTableColumn
alaQoSExtendedRuleGreenPacketCount = _AlaQoSExtendedRuleGreenPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 57, 1, 7),
    _AlaQoSExtendedRuleGreenPacketCount_Type()
)
alaQoSExtendedRuleGreenPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSExtendedRuleGreenPacketCount.setStatus("current")
_AlaQoSExtendedRuleYellowPacketCount_Type = Counter64
_AlaQoSExtendedRuleYellowPacketCount_Object = MibTableColumn
alaQoSExtendedRuleYellowPacketCount = _AlaQoSExtendedRuleYellowPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 57, 1, 8),
    _AlaQoSExtendedRuleYellowPacketCount_Type()
)
alaQoSExtendedRuleYellowPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSExtendedRuleYellowPacketCount.setStatus("current")
_AlaQoSExtendedRuleRedPacketCount_Type = Counter64
_AlaQoSExtendedRuleRedPacketCount_Object = MibTableColumn
alaQoSExtendedRuleRedPacketCount = _AlaQoSExtendedRuleRedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 57, 1, 9),
    _AlaQoSExtendedRuleRedPacketCount_Type()
)
alaQoSExtendedRuleRedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSExtendedRuleRedPacketCount.setStatus("current")
_AlaQoSExtendedRuleGreenByteCount_Type = Counter64
_AlaQoSExtendedRuleGreenByteCount_Object = MibTableColumn
alaQoSExtendedRuleGreenByteCount = _AlaQoSExtendedRuleGreenByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 57, 1, 10),
    _AlaQoSExtendedRuleGreenByteCount_Type()
)
alaQoSExtendedRuleGreenByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSExtendedRuleGreenByteCount.setStatus("current")
_AlaQoSExtendedRuleYellowByteCount_Type = Counter64
_AlaQoSExtendedRuleYellowByteCount_Object = MibTableColumn
alaQoSExtendedRuleYellowByteCount = _AlaQoSExtendedRuleYellowByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 57, 1, 11),
    _AlaQoSExtendedRuleYellowByteCount_Type()
)
alaQoSExtendedRuleYellowByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSExtendedRuleYellowByteCount.setStatus("current")
_AlaQoSExtendedRuleRedByteCount_Type = Counter64
_AlaQoSExtendedRuleRedByteCount_Object = MibTableColumn
alaQoSExtendedRuleRedByteCount = _AlaQoSExtendedRuleRedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 57, 1, 12),
    _AlaQoSExtendedRuleRedByteCount_Type()
)
alaQoSExtendedRuleRedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSExtendedRuleRedByteCount.setStatus("current")
_AlaQoSIpNetworkSummaryTable_Object = MibTable
alaQoSIpNetworkSummaryTable = _AlaQoSIpNetworkSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 58)
)
if mibBuilder.loadTexts:
    alaQoSIpNetworkSummaryTable.setStatus("current")
_AlaQoSIpNetworkSummaryEntry_Object = MibTableRow
alaQoSIpNetworkSummaryEntry = _AlaQoSIpNetworkSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 58, 1)
)
alaQoSIpNetworkSummaryEntry.setIndexNames(
    (0, "ALCATEL-ENT1-QOS-MIB", "alaQoSRuleName"),
)
if mibBuilder.loadTexts:
    alaQoSIpNetworkSummaryEntry.setStatus("current")


class _AlaQoSIpNetworkSummaryProtocol_Type(SnmpAdminString):
    """Custom type alaQoSIpNetworkSummaryProtocol based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSIpNetworkSummaryProtocol_Type.__name__ = "SnmpAdminString"
_AlaQoSIpNetworkSummaryProtocol_Object = MibTableColumn
alaQoSIpNetworkSummaryProtocol = _AlaQoSIpNetworkSummaryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 58, 1, 1),
    _AlaQoSIpNetworkSummaryProtocol_Type()
)
alaQoSIpNetworkSummaryProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSIpNetworkSummaryProtocol.setStatus("current")


class _AlaQoSIpNetworkSummarySourceIpAddressType_Type(InetAddressType):
    """Custom type alaQoSIpNetworkSummarySourceIpAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_AlaQoSIpNetworkSummarySourceIpAddressType_Type.__name__ = "InetAddressType"
_AlaQoSIpNetworkSummarySourceIpAddressType_Object = MibTableColumn
alaQoSIpNetworkSummarySourceIpAddressType = _AlaQoSIpNetworkSummarySourceIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 58, 1, 2),
    _AlaQoSIpNetworkSummarySourceIpAddressType_Type()
)
alaQoSIpNetworkSummarySourceIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSIpNetworkSummarySourceIpAddressType.setStatus("current")


class _AlaQoSIpNetworkSummarySourceIpAddress_Type(InetAddress):
    """Custom type alaQoSIpNetworkSummarySourceIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaQoSIpNetworkSummarySourceIpAddress_Type.__name__ = "InetAddress"
_AlaQoSIpNetworkSummarySourceIpAddress_Object = MibTableColumn
alaQoSIpNetworkSummarySourceIpAddress = _AlaQoSIpNetworkSummarySourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 58, 1, 3),
    _AlaQoSIpNetworkSummarySourceIpAddress_Type()
)
alaQoSIpNetworkSummarySourceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSIpNetworkSummarySourceIpAddress.setStatus("current")


class _AlaQoSIpNetworkSummaryDestinationIpAddressType_Type(InetAddressType):
    """Custom type alaQoSIpNetworkSummaryDestinationIpAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_AlaQoSIpNetworkSummaryDestinationIpAddressType_Type.__name__ = "InetAddressType"
_AlaQoSIpNetworkSummaryDestinationIpAddressType_Object = MibTableColumn
alaQoSIpNetworkSummaryDestinationIpAddressType = _AlaQoSIpNetworkSummaryDestinationIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 58, 1, 4),
    _AlaQoSIpNetworkSummaryDestinationIpAddressType_Type()
)
alaQoSIpNetworkSummaryDestinationIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSIpNetworkSummaryDestinationIpAddressType.setStatus("current")


class _AlaQoSIpNetworkSummaryDestinationIpAddress_Type(InetAddress):
    """Custom type alaQoSIpNetworkSummaryDestinationIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaQoSIpNetworkSummaryDestinationIpAddress_Type.__name__ = "InetAddress"
_AlaQoSIpNetworkSummaryDestinationIpAddress_Object = MibTableColumn
alaQoSIpNetworkSummaryDestinationIpAddress = _AlaQoSIpNetworkSummaryDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 58, 1, 5),
    _AlaQoSIpNetworkSummaryDestinationIpAddress_Type()
)
alaQoSIpNetworkSummaryDestinationIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSIpNetworkSummaryDestinationIpAddress.setStatus("current")


class _AlaQoSIpNetworkSummarySourceGroup_Type(SnmpAdminString):
    """Custom type alaQoSIpNetworkSummarySourceGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSIpNetworkSummarySourceGroup_Type.__name__ = "SnmpAdminString"
_AlaQoSIpNetworkSummarySourceGroup_Object = MibTableColumn
alaQoSIpNetworkSummarySourceGroup = _AlaQoSIpNetworkSummarySourceGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 58, 1, 6),
    _AlaQoSIpNetworkSummarySourceGroup_Type()
)
alaQoSIpNetworkSummarySourceGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSIpNetworkSummarySourceGroup.setStatus("current")


class _AlaQoSIpNetworkSummaryDestinationGroup_Type(SnmpAdminString):
    """Custom type alaQoSIpNetworkSummaryDestinationGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSIpNetworkSummaryDestinationGroup_Type.__name__ = "SnmpAdminString"
_AlaQoSIpNetworkSummaryDestinationGroup_Object = MibTableColumn
alaQoSIpNetworkSummaryDestinationGroup = _AlaQoSIpNetworkSummaryDestinationGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 58, 1, 7),
    _AlaQoSIpNetworkSummaryDestinationGroup_Type()
)
alaQoSIpNetworkSummaryDestinationGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSIpNetworkSummaryDestinationGroup.setStatus("current")


class _AlaQoSIpNetworkSummaryVrfName_Type(SnmpAdminString):
    """Custom type alaQoSIpNetworkSummaryVrfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSIpNetworkSummaryVrfName_Type.__name__ = "SnmpAdminString"
_AlaQoSIpNetworkSummaryVrfName_Object = MibTableColumn
alaQoSIpNetworkSummaryVrfName = _AlaQoSIpNetworkSummaryVrfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 58, 1, 8),
    _AlaQoSIpNetworkSummaryVrfName_Type()
)
alaQoSIpNetworkSummaryVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSIpNetworkSummaryVrfName.setStatus("current")


class _AlaQoSIpNetworkSummaryAction_Type(Integer32):
    """Custom type alaQoSIpNetworkSummaryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("deny", 2))
    )


_AlaQoSIpNetworkSummaryAction_Type.__name__ = "Integer32"
_AlaQoSIpNetworkSummaryAction_Object = MibTableColumn
alaQoSIpNetworkSummaryAction = _AlaQoSIpNetworkSummaryAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 58, 1, 9),
    _AlaQoSIpNetworkSummaryAction_Type()
)
alaQoSIpNetworkSummaryAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSIpNetworkSummaryAction.setStatus("current")
_AlaQoSIpNetworkSummaryHitCount_Type = Counter64
_AlaQoSIpNetworkSummaryHitCount_Object = MibTableColumn
alaQoSIpNetworkSummaryHitCount = _AlaQoSIpNetworkSummaryHitCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 58, 1, 10),
    _AlaQoSIpNetworkSummaryHitCount_Type()
)
alaQoSIpNetworkSummaryHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSIpNetworkSummaryHitCount.setStatus("current")
_AlaQoSMIBConformance_ObjectIdentity = ObjectIdentity
alaQoSMIBConformance = _AlaQoSMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2)
)
if mibBuilder.loadTexts:
    alaQoSMIBConformance.setStatus("current")
_AlaQoSMIBGroups_ObjectIdentity = ObjectIdentity
alaQoSMIBGroups = _AlaQoSMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaQoSMIBGroups.setStatus("current")
_AlaQoSMIBCompliances_ObjectIdentity = ObjectIdentity
alaQoSMIBCompliances = _AlaQoSMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alaQoSMIBCompliances.setStatus("current")

# Managed Objects groups

alaQoSMIBRuleObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 1)
)
alaQoSMIBRuleObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleEnabled"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleSource"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRulePrecedence"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleCondition"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleAction"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleReflexive"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleSave"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleLog"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleEnforced"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleActive"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleRowStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleValidityPeriod"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleValidityPeriodStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleLogInterval"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleCountType"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRulePacketCount"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleByteCount"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleType"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleTrapEvents"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleDefaultList"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleGreenPacketCount"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleYellowPacketCount"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleRedPacketCount"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleGreenByteCount"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleYellowByteCount"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleRedByteCount"))
)
if mibBuilder.loadTexts:
    alaQoSMIBRuleObjects.setStatus("current")

alaQoSMIBAppliedRuleObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 2)
)
alaQoSMIBAppliedRuleObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleEnabled"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleSource"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRulePrecedence"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleCondition"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleAction"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleReflexive"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleSave"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleLog"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleEnforced"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleActive"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleRowStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleValidityPeriod"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleValidityPeriodStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleLogInterval"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleCountType"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRulePacketCount"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleByteCount"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleType"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleTrapEvents"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleDefaultList"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleGreenPacketCount"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleYellowPacketCount"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleRedPacketCount"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleGreenByteCount"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleYellowByteCount"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleRedByteCount"))
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedRuleObjects.setStatus("current")

alaQoSMIBConditionObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 3)
)
alaQoSMIBConditionObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSource"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourceSlot"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourceSlotStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourcePort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourcePortGroup"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourcePortGroupStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationSlot"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationSlotStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationPortGroup"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationPortGroupStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourceMacAddr"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourceMacAddrStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourceMacMask"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourceMacGroup"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourceMacGroupStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationMacAddr"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationMacAddrStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationMacMask"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationMacGroup"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationMacGroupStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourceVlan"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourceVlanStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationVlan"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationVlanStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSCondition8021p"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSCondition8021pStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourceIpAddr"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourceIpAddrStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourceIpMask"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourceNetworkGroup"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourceNetworkGroupStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationIpAddr"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationIpAddrStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationIpMask"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationNetworkGroup"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationNetworkGroupStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionMulticastIpAddr"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionMulticastIpAddrStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionMulticastIpMask"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionMulticastNetworkGroup"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionMulticastNetworkGroupStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionTos"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionTosStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionTosMask"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDscp"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDscpStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDscpMask"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionIpProtocol"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionIpProtocolStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourceIpPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourceIpPortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationIpPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationIpPortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionService"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionServiceStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionServiceGroup"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionServiceGroupStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionIcmpType"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionIcmpTypeStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionIcmpCode"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionIcmpCodeStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionRowStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourcePortEnd"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationPortEnd"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourceIpPortEnd"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationIpPortEnd"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourceTcpPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourceTcpPortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourceTcpPortEnd"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationTcpPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationTcpPortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationTcpPortEnd"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourceUdpPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourceUdpPortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourceUdpPortEnd"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationUdpPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationUdpPortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationUdpPortEnd"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionEthertype"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionEthertypeStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionTcpFlags"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionTcpFlagsStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionTcpFlagsVal"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionTcpFlagsValStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionTcpFlagsMask"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionTcpFlagsMaskStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionTcpEstablished"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourceIpv6Addr"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourceIpv6AddrStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourceIpv6Mask"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationIpv6Addr"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationIpv6AddrStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationIpv6Mask"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionIpv6Traffic"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionIpv6NH"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionIpv6NHStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionIpv6FlowLabel"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionIpv6FlowLabelStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionMcastIpv6Addr"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionMcastIpv6AddrStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionMcastIpv6Mask"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDscpEnd"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionInnerSourceVlan"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionInnerSourceVlanStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionInner8021p"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionInner8021pStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionVrfName"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionVrfNameStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionFragments"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourceChassis"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDestinationChassis"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionAppFpGroup"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionAppFpGroupStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSIP"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSIPStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDPIAppName"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDPIGrpName"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDPIAppNameStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionDPIAppGroupStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionVxlanVni"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionVxlanVniStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionVxlanPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionVxlanPortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionVmSourceMacAddr"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionVmSourceMacAddrStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionVmSourceMacMask"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionVmSourceIpAddr"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionVmSourceIpAddrStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionVmSourceIpMask"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionVmSourceIpv6IpAddr"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionVmSourceIpv6IpAddrStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionVmSourceIpv6IpMask"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionVmIpProtocol"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionVmIpProtocolStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQosConditionVmL4SourcePort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQosConditionVmL4SourcePortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQosConditionVmL4DestPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQosConditionVmL4DestPortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQosConditionVxlanStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourcePortSplitGroup"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConditionSourcePortSplitGroupStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBConditionObjects.setStatus("current")

alaQoSMIBAppliedConditionObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 4)
)
alaQoSMIBAppliedConditionObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSource"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourceSlot"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourceSlotStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourcePort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourcePortGroup"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourcePortGroupStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationSlot"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationSlotStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationPortGroup"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationPortGroupStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourceMacAddr"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourceMacAddrStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourceMacMask"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourceMacGroup"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourceMacGroupStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationMacAddr"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationMacAddrStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationMacMask"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationMacGroup"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationMacGroupStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourceVlan"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourceVlanStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationVlan"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationVlanStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedCondition8021p"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedCondition8021pStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourceIpAddr"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourceIpAddrStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourceIpMask"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourceNetworkGroup"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourceNetworkGroupStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationIpAddr"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationIpAddrStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationIpMask"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationNetworkGroup"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationNetworkGroupStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionMulticastIpAddr"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionMulticastIpAddrStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionMulticastIpMask"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionMulticastNetworkGroup"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionMulticastNetworkGroupStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionTos"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionTosStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionTosMask"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDscp"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDscpStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDscpMask"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionIpProtocol"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionIpProtocolStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourceIpPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourceIpPortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationIpPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationIpPortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionService"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionServiceStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionServiceGroup"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionServiceGroupStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionIcmpType"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionIcmpTypeStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionIcmpCode"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionIcmpCodeStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionRowStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourcePortEnd"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationPortEnd"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourceIpPortEnd"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationIpPortEnd"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourceTcpPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourceTcpPortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourceTcpPortEnd"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationTcpPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationTcpPortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationTcpPortEnd"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourceUdpPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourceUdpPortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourceUdpPortEnd"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationUdpPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationUdpPortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationUdpPortEnd"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionEthertype"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionEthertypeStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionTcpFlags"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionTcpFlagsStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionTcpFlagsVal"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionTcpFlagsValStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionTcpFlagsMask"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionTcpFlagsMaskStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionTcpEstablished"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourceIpv6Addr"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourceIpv6AddrStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourceIpv6Mask"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationIpv6Addr"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationIpv6AddrStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationIpv6Mask"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionIpv6Traffic"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionIpv6NH"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionIpv6NHStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionIpv6FlowLabel"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionIpv6FlowLabelStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionMcastIpv6Addr"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionMcastIpv6AddrStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionMcastIpv6Mask"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDscpEnd"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionInnerSourceVlan"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionInnerSourceVlanStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionInner8021p"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionInner8021pStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionVrfName"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionVrfNameStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionFragments"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourceChassis"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDestinationChassis"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionAppFpGroup"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionAppFpGroupStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSIP"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSIPStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDPIAppName"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDPIAppGrp"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDPIAppNameStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionDPIAppGroupStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionVxlanVni"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionVxlanVniStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionVxlanPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionVxlanPortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionVmSourceMacAddr"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionVmSourceMacAddrStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionVmSourceMacMask"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionVmSourceIpAddr"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionVmSourceIpAddrStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionVmSourceIpMask"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionVmSourceIpv6IpAddr"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionVmSourceIpv6IpAddrStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionVmSourceIpv6IpMask"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionVmIpProtocol"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionVmIpProtocolStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQosAppliedConditionVmL4SourcePort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQosAppliedConditionVmL4SourcePortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQosAppliedConditionVmL4DestPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQosAppliedConditionVmL4DestPortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQosAppliedConditionVxlanStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourcePortSplitGroup"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedConditionSourcePortSplitGroupStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedConditionObjects.setStatus("current")

alaQoSMIBServiceObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 5)
)
alaQoSMIBServiceObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSServiceSource"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSServiceProtocol"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSServiceSourceIpPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSServiceSourceIpPortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSServiceDestinationIpPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSServiceDestinationIpPortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSServiceRowStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSServiceSourceIpPortEnd"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSServiceDestinationIpPortEnd"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSServiceSourceTcpPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSServiceSourceTcpPortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSServiceSourceTcpPortEnd"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSServiceDestinationTcpPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSServiceDestinationTcpPortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSServiceDestinationTcpPortEnd"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSServiceSourceUdpPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSServiceSourceUdpPortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSServiceSourceUdpPortEnd"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSServiceDestinationUdpPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSServiceDestinationUdpPortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSServiceDestinationUdpPortEnd"))
)
if mibBuilder.loadTexts:
    alaQoSMIBServiceObjects.setStatus("current")

alaQoSMIBAppliedServiceObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 6)
)
alaQoSMIBAppliedServiceObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedServiceSource"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedServiceProtocol"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedServiceSourceIpPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedServiceSourceIpPortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedServiceDestinationIpPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedServiceDestinationIpPortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedServiceRowStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedServiceSourceIpPortEnd"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedServiceDestinationIpPortEnd"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedServiceSourceTcpPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedServiceSourceTcpPortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedServiceSourceTcpPortEnd"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedServiceDestinationTcpPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedServiceDestinationTcpPortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedServiceDestinationTcpPortEnd"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedServiceSourceUdpPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedServiceSourceUdpPortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedServiceSourceUdpPortEnd"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedServiceDestinationUdpPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedServiceDestinationUdpPortStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedServiceDestinationUdpPortEnd"))
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedServiceObjects.setStatus("current")

alaQoSMIBServiceGroupsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 7)
)
alaQoSMIBServiceGroupsObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSServiceGroupsSource"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSServiceGroupsStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBServiceGroupsObjects.setStatus("current")

alaQoSMIBAppliedServiceGroupsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 8)
)
alaQoSMIBAppliedServiceGroupsObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedServiceGroupsSource"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedServiceGroupsStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedServiceGroupsObjects.setStatus("current")

alaQoSMIBServiceGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 9)
)
alaQoSMIBServiceGroupObjects.setObjects(
    ("ALCATEL-ENT1-QOS-MIB", "alaQoSServiceGroupStatus")
)
if mibBuilder.loadTexts:
    alaQoSMIBServiceGroupObjects.setStatus("current")

alaQoSMIBAppliedServiceGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 10)
)
alaQoSMIBAppliedServiceGroupObjects.setObjects(
    ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedServiceGroupStatus")
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedServiceGroupObjects.setStatus("current")

alaQoSMIBNetworkGroupsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 11)
)
alaQoSMIBNetworkGroupsObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSNetworkGroupsSource"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSNetworkGroupsStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBNetworkGroupsObjects.setStatus("current")

alaQoSMIBAppliedNetworkGroupsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 12)
)
alaQoSMIBAppliedNetworkGroupsObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedNetworkGroupsSource"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedNetworkGroupsStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedNetworkGroupsObjects.setStatus("current")

alaQoSMIBNetworkGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 13)
)
alaQoSMIBNetworkGroupObjects.setObjects(
    ("ALCATEL-ENT1-QOS-MIB", "alaQoSNetworkGroupStatus")
)
if mibBuilder.loadTexts:
    alaQoSMIBNetworkGroupObjects.setStatus("current")

alaQoSMIBAppliedNetworkGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 14)
)
alaQoSMIBAppliedNetworkGroupObjects.setObjects(
    ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedNetworkGroupStatus")
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedNetworkGroupObjects.setStatus("current")

alaQoSMIBMACGroupsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 15)
)
alaQoSMIBMACGroupsObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSMACGroupsSource"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMACGroupsStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBMACGroupsObjects.setStatus("current")

alaQoSMIBAppliedMACGroupsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 16)
)
alaQoSMIBAppliedMACGroupsObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedMACGroupsSource"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedMACGroupsStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedMACGroupsObjects.setStatus("current")

alaQoSMIBMACGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 17)
)
alaQoSMIBMACGroupObjects.setObjects(
    ("ALCATEL-ENT1-QOS-MIB", "alaQoSMACGroupStatus")
)
if mibBuilder.loadTexts:
    alaQoSMIBMACGroupObjects.setStatus("current")

alaQoSMIBAppliedMACGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 18)
)
alaQoSMIBAppliedMACGroupObjects.setObjects(
    ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedMACGroupStatus")
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedMACGroupObjects.setStatus("current")

alaQoSMIBPortGroupsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 19)
)
alaQoSMIBPortGroupsObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSPortGroupsSource"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSPortGroupsStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBPortGroupsObjects.setStatus("current")

alaQoSMIBAppliedPortGroupsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 20)
)
alaQoSMIBAppliedPortGroupsObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedPortGroupsSource"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedPortGroupsStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedPortGroupsObjects.setStatus("current")

alaQoSMIBPortGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 21)
)
alaQoSMIBPortGroupObjects.setObjects(
    ("ALCATEL-ENT1-QOS-MIB", "alaQoSPortGroupStatus")
)
if mibBuilder.loadTexts:
    alaQoSMIBPortGroupObjects.setStatus("current")

alaQoSMIBAppliedPortGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 22)
)
alaQoSMIBAppliedPortGroupObjects.setObjects(
    ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedPortGroupStatus")
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedPortGroupObjects.setStatus("current")

alaQoSMIBMapGroupsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 23)
)
alaQoSMIBMapGroupsObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSMapGroupsSource"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMapGroupsStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBMapGroupsObjects.setStatus("current")

alaQoSMIBAppliedMapGroupsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 24)
)
alaQoSMIBAppliedMapGroupsObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedMapGroupsSource"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedMapGroupsStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedMapGroupsObjects.setStatus("current")

alaQoSMIBMapGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 25)
)
alaQoSMIBMapGroupObjects.setObjects(
    ("ALCATEL-ENT1-QOS-MIB", "alaQoSMapGroupStatus")
)
if mibBuilder.loadTexts:
    alaQoSMIBMapGroupObjects.setStatus("current")

alaQoSMIBAppliedMapGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 26)
)
alaQoSMIBAppliedMapGroupObjects.setObjects(
    ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedMapGroupStatus")
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedMapGroupObjects.setStatus("current")

alaQoSMIBActionObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 27)
)
alaQoSMIBActionObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSActionSource"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionDisposition"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionMaximumBandwidth"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionMaximumBandwidthStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionPriority"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionPriorityStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionShared"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionMaximumDepth"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionMaximumDepthStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAction8021p"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAction8021pStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionTos"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionTosStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionDscp"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionDscpStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionMapFrom"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionMapTo"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionMapGroup"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionMapGroupStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionLoadBalanceGroup"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionLoadBalanceGroupStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionPermanentGatewayIpAddr"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionPermanentGatewayIpAddrStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionAlternateGatewayIpAddr"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionAlternateGatewayIpAddrStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionRowStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionNocache"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionPortdisable"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionRedirectSlot"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionRedirectSlotStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionRedirectPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionRedirectAgg"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionRedirectAggStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionMirrorSlot"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionMirrorPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionMirrorMode"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionMirrorModeStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionCIR"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionCIRStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionCBS"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionCBSStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionPIR"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionPIRStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionPBS"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionPBSStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionCPUPriority"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionCPUPriorityStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionColorOnly"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionRedirectChassis"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionMirrorChassis"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionPermanentGatewayIpV6Addr"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionPermanentGatewayIpV6AddrStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionPermanentGatewayIpV6IfIndex"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionRTCPMonitor"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionRTCPMonitorStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionRTCPDSCP"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionRTCPDSCPStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionTrustDSCP"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionTrustDSCPStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSActionRedirectModule"))
)
if mibBuilder.loadTexts:
    alaQoSMIBActionObjects.setStatus("current")

alaQoSMIBAppliedActionObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 28)
)
alaQoSMIBAppliedActionObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionSource"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionDisposition"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionMaximumBandwidth"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionMaximumBandwidthStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionPriority"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionPriorityStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionShared"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionMaximumDepth"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionMaximumDepthStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedAction8021p"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedAction8021pStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionTos"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionTosStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionDscp"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionDscpStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionMapFrom"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionMapTo"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionMapGroup"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionMapGroupStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionLoadBalanceGroup"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionLoadBalanceGroupStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionPermanentGatewayIpAddr"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionPermanentGatewayIpAddrStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionAlternateGatewayIpAddr"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionAlternateGatewayIpAddrStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionRowStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionNocache"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionPortdisable"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionRedirectSlot"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionRedirectSlotStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionRedirectPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionRedirectAgg"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionRedirectAggStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionMirrorSlot"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionMirrorPort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionMirrorMode"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionMirrorModeStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionCIR"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionCIRStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionCBS"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionCBSStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionPIR"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionPIRStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionPBS"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionPBSStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionCPUPriority"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionCPUPriorityStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionColorOnly"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionRedirectChassis"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionMirrorChassis"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionPermanentGatewayIpV6Addr"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionPermanentGatewayIpV6AddrStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionPermanentGatewayIpV6IfIndex"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionRTCPMonitor"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionRTCPMonitorStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionRTCPDSCP"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionRTCPDSCPStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionTrustDSCP"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedActionTrustDSCPStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedActionObjects.setStatus("current")

alaQoSMIBPortObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 29)
)
alaQoSMIBPortObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSPortInterfaceType"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSPortTrusted"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSPortDefault8021p"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSPortDefaultDSCP"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSPortMaximumDefaultDepth"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSPortMaximumDefaultDepthStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSPortReset"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSPortPhysicalBandwidth"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSPortRowStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSPortDefaultClassification"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSPortMaximumBandwidth"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSPortMaximumBandwidthStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSPortMaximumIngBandwidth"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSPortMaximumIngBandwidthStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSPortMaximumIngressDepth"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSPortMaximumIngressDepthStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSPortDEIMarking"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSPortDEIMapping"))
)
if mibBuilder.loadTexts:
    alaQoSMIBPortObjects.setStatus("current")

alaQoSMIBConfigObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 30)
)
alaQoSMIBConfigObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSConfigEnabled"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConfigTrustPorts"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConfigStatsInterval"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConfigLogLines"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConfigLogLevel"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConfigLogConsole"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConfigForwardLog"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConfigClearLog"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConfigApply"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConfigRevert"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConfigReset"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConfigStatsReset"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConfigFlush"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConfigDebug"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConfigUserportFilter"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConfigAppliedUserportFilter"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConfigUserportShutdown"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConfigAppliedUserportShutdown"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConfigAutoPhones"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConfigQMPage"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConfigQMMACGroup"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConfigQMPath"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConfigDEIMapping"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConfigDEIMarking"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSConfigSwitchGroup"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSVmSnooping"))
)
if mibBuilder.loadTexts:
    alaQoSMIBConfigObjects.setStatus("current")

alaQoSMIBStatsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 31)
)
alaQoSMIBStatsObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSStatsSpoofedEvents"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSStatsNonSpoofedEvents"))
)
if mibBuilder.loadTexts:
    alaQoSMIBStatsObjects.setStatus("current")

alaQoSMIBRuleGroupsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 32)
)
alaQoSMIBRuleGroupsObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleGroupsSource"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleGroupsType"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleGroupsEnabled"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleGroupsStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBRuleGroupsObjects.setStatus("current")

alaQoSMIBAppliedRuleGroupsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 33)
)
alaQoSMIBAppliedRuleGroupsObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleGroupsSource"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleGroupsType"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleGroupsEnabled"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleGroupsStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedRuleGroupsObjects.setStatus("current")

alaQoSMIBRuleGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 34)
)
alaQoSMIBRuleGroupObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleGroupMatches"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleGroupCountType"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleGroupPacketCount"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleGroupByteCount"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleGroupStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBRuleGroupObjects.setStatus("current")

alaQoSMIBAppliedRuleGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 35)
)
alaQoSMIBAppliedRuleGroupObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleGroupMatches"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleGroupCountType"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleGroupPacketCount"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleGroupByteCount"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedRuleGroupStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedRuleGroupObjects.setStatus("current")

alaQoSMIBValidityPeriodObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 36)
)
alaQoSMIBValidityPeriodObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSValidityPeriodSource"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSValidityPeriodDays"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSValidityPeriodDaysStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSValidityPeriodMonths"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSValidityPeriodMonthsStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSValidityPeriodHour"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSValidityPeriodHourStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSValidityPeriodEndHour"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSValidityPeriodInterval"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSValidityPeriodIntervalStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSValidityPeriodEndInterval"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSValidityPeriodRowStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBValidityPeriodObjects.setStatus("current")

alaQoSMIBAppliedValidityPeriodObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 37)
)
alaQoSMIBAppliedValidityPeriodObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedValidityPeriodSource"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedValidityPeriodDays"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedValidityPeriodDaysStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedValidityPeriodMonths"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedValidityPeriodMonthsStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedValidityPeriodHour"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedValidityPeriodHourStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedValidityPeriodEndHour"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedValidityPeriodInterval"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedValidityPeriodIntervalStatus"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedValidityPeriodEndInterval"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedValidityPeriodRowStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedValidityPeriodObjects.setStatus("current")

alaQoSMIBDSCPGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 38)
)
alaQoSMIBDSCPGroupObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSDSCPPriority"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSDSCPDropPrecedence"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSDSCPRowStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBDSCPGroupObjects.setStatus("current")

alaQoSMIBAutoMacRangeGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 39)
)
alaQoSMIBAutoMacRangeGroupObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSAutoMacRangeStart"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSAutoMacRangeEnd"))
)
if mibBuilder.loadTexts:
    alaQoSMIBAutoMacRangeGroupObjects.setStatus("current")

alaQoSMIBV6NetworkGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 40)
)
alaQoSMIBV6NetworkGroupObjects.setObjects(
    ("ALCATEL-ENT1-QOS-MIB", "alaQoSV6NetworkGroupStatus")
)
if mibBuilder.loadTexts:
    alaQoSMIBV6NetworkGroupObjects.setStatus("current")

alaQoSMIBAppliedV6NetworkGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 41)
)
alaQoSMIBAppliedV6NetworkGroupObjects.setObjects(
    ("ALCATEL-ENT1-QOS-MIB", "alaQoSAppliedV6NetworkGroupStatus")
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedV6NetworkGroupObjects.setStatus("current")

alaQoSRuleExtendedObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 42)
)
alaQoSRuleExtendedObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSExtendedRuleChassis"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSExtendedRuleSlot"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSExtendedRulePort"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSExtendedRulePacketCount"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSExtendedRuleByteCount"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSExtendedRuleGreenPacketCount"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSExtendedRuleYellowPacketCount"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSExtendedRuleRedPacketCount"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSExtendedRuleGreenByteCount"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSExtendedRuleYellowByteCount"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSExtendedRuleRedByteCount"))
)
if mibBuilder.loadTexts:
    alaQoSRuleExtendedObjects.setStatus("current")

alaQoSIpNetworkSummaryGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 43)
)
alaQoSIpNetworkSummaryGroupObjects.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSIpNetworkSummaryProtocol"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSIpNetworkSummarySourceIpAddressType"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSIpNetworkSummarySourceIpAddress"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSIpNetworkSummaryDestinationIpAddressType"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSIpNetworkSummaryDestinationIpAddress"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSIpNetworkSummarySourceGroup"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSIpNetworkSummaryDestinationGroup"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSIpNetworkSummaryVrfName"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSIpNetworkSummaryAction"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSIpNetworkSummaryHitCount"))
)
if mibBuilder.loadTexts:
    alaQoSIpNetworkSummaryGroupObjects.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alaQoSMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 2, 1)
)
alaQoSMIBCompliance.setObjects(
      *(("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBRuleObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBAppliedRuleObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBConditionObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBAppliedConditionObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBServiceObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBAppliedServiceObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBServiceGroupsObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBAppliedServiceGroupsObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBServiceGroupObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBAppliedServiceGroupObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBNetworkGroupsObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBAppliedNetworkGroupsObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBNetworkGroupObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBAppliedNetworkGroupObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBMACGroupsObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBAppliedMACGroupsObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBMACGroupObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBAppliedMACGroupObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBPortGroupsObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBAppliedPortGroupsObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBPortGroupObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBAppliedPortGroupObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBMapGroupsObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBAppliedMapGroupsObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBMapGroupObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBAppliedMapGroupObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBActionObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBAppliedActionObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBPortObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBConfigObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBStatsObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBRuleGroupsObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBAppliedRuleGroupsObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBRuleGroupObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBAppliedRuleGroupObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBValidityPeriodObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBAppliedValidityPeriodObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBDSCPGroupObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBAutoMacRangeGroupObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBV6NetworkGroupObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSMIBAppliedV6NetworkGroupObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSRuleExtendedObjects"),
        ("ALCATEL-ENT1-QOS-MIB", "alaQoSIpNetworkSummaryGroupObjects"))
)
if mibBuilder.loadTexts:
    alaQoSMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-ENT1-QOS-MIB",
    **{"alaQoSMIB": alaQoSMIB,
       "alaQoSMIBObjects": alaQoSMIBObjects,
       "alaQoSRuleTable": alaQoSRuleTable,
       "alaQoSRuleEntry": alaQoSRuleEntry,
       "alaQoSRuleName": alaQoSRuleName,
       "alaQoSRuleEnabled": alaQoSRuleEnabled,
       "alaQoSRuleSource": alaQoSRuleSource,
       "alaQoSRulePrecedence": alaQoSRulePrecedence,
       "alaQoSRuleCondition": alaQoSRuleCondition,
       "alaQoSRuleAction": alaQoSRuleAction,
       "alaQoSRuleReflexive": alaQoSRuleReflexive,
       "alaQoSRuleSave": alaQoSRuleSave,
       "alaQoSRuleLog": alaQoSRuleLog,
       "alaQoSRuleEnforced": alaQoSRuleEnforced,
       "alaQoSRuleActive": alaQoSRuleActive,
       "alaQoSRuleRowStatus": alaQoSRuleRowStatus,
       "alaQoSRuleValidityPeriod": alaQoSRuleValidityPeriod,
       "alaQoSRuleValidityPeriodStatus": alaQoSRuleValidityPeriodStatus,
       "alaQoSRuleLogInterval": alaQoSRuleLogInterval,
       "alaQoSRuleCountType": alaQoSRuleCountType,
       "alaQoSRulePacketCount": alaQoSRulePacketCount,
       "alaQoSRuleByteCount": alaQoSRuleByteCount,
       "alaQoSRuleType": alaQoSRuleType,
       "alaQoSRuleTrapEvents": alaQoSRuleTrapEvents,
       "alaQoSRuleDefaultList": alaQoSRuleDefaultList,
       "alaQoSRuleGreenPacketCount": alaQoSRuleGreenPacketCount,
       "alaQoSRuleYellowPacketCount": alaQoSRuleYellowPacketCount,
       "alaQoSRuleRedPacketCount": alaQoSRuleRedPacketCount,
       "alaQoSRuleGreenByteCount": alaQoSRuleGreenByteCount,
       "alaQoSRuleYellowByteCount": alaQoSRuleYellowByteCount,
       "alaQoSRuleRedByteCount": alaQoSRuleRedByteCount,
       "alaQoSAppliedRuleTable": alaQoSAppliedRuleTable,
       "alaQoSAppliedRuleEntry": alaQoSAppliedRuleEntry,
       "alaQoSAppliedRuleName": alaQoSAppliedRuleName,
       "alaQoSAppliedRuleEnabled": alaQoSAppliedRuleEnabled,
       "alaQoSAppliedRuleSource": alaQoSAppliedRuleSource,
       "alaQoSAppliedRulePrecedence": alaQoSAppliedRulePrecedence,
       "alaQoSAppliedRuleCondition": alaQoSAppliedRuleCondition,
       "alaQoSAppliedRuleAction": alaQoSAppliedRuleAction,
       "alaQoSAppliedRuleReflexive": alaQoSAppliedRuleReflexive,
       "alaQoSAppliedRuleSave": alaQoSAppliedRuleSave,
       "alaQoSAppliedRuleLog": alaQoSAppliedRuleLog,
       "alaQoSAppliedRuleEnforced": alaQoSAppliedRuleEnforced,
       "alaQoSAppliedRuleActive": alaQoSAppliedRuleActive,
       "alaQoSAppliedRuleRowStatus": alaQoSAppliedRuleRowStatus,
       "alaQoSAppliedRuleValidityPeriod": alaQoSAppliedRuleValidityPeriod,
       "alaQoSAppliedRuleValidityPeriodStatus": alaQoSAppliedRuleValidityPeriodStatus,
       "alaQoSAppliedRuleLogInterval": alaQoSAppliedRuleLogInterval,
       "alaQoSAppliedRuleCountType": alaQoSAppliedRuleCountType,
       "alaQoSAppliedRulePacketCount": alaQoSAppliedRulePacketCount,
       "alaQoSAppliedRuleByteCount": alaQoSAppliedRuleByteCount,
       "alaQoSAppliedRuleType": alaQoSAppliedRuleType,
       "alaQoSAppliedRuleTrapEvents": alaQoSAppliedRuleTrapEvents,
       "alaQoSAppliedRuleDefaultList": alaQoSAppliedRuleDefaultList,
       "alaQoSAppliedRuleGreenPacketCount": alaQoSAppliedRuleGreenPacketCount,
       "alaQoSAppliedRuleYellowPacketCount": alaQoSAppliedRuleYellowPacketCount,
       "alaQoSAppliedRuleRedPacketCount": alaQoSAppliedRuleRedPacketCount,
       "alaQoSAppliedRuleGreenByteCount": alaQoSAppliedRuleGreenByteCount,
       "alaQoSAppliedRuleYellowByteCount": alaQoSAppliedRuleYellowByteCount,
       "alaQoSAppliedRuleRedByteCount": alaQoSAppliedRuleRedByteCount,
       "alaQoSConditionTable": alaQoSConditionTable,
       "alaQoSConditionEntry": alaQoSConditionEntry,
       "alaQoSConditionName": alaQoSConditionName,
       "alaQoSConditionSource": alaQoSConditionSource,
       "alaQoSConditionSourceSlot": alaQoSConditionSourceSlot,
       "alaQoSConditionSourceSlotStatus": alaQoSConditionSourceSlotStatus,
       "alaQoSConditionSourcePort": alaQoSConditionSourcePort,
       "alaQoSConditionSourcePortGroup": alaQoSConditionSourcePortGroup,
       "alaQoSConditionSourcePortGroupStatus": alaQoSConditionSourcePortGroupStatus,
       "alaQoSConditionDestinationSlot": alaQoSConditionDestinationSlot,
       "alaQoSConditionDestinationSlotStatus": alaQoSConditionDestinationSlotStatus,
       "alaQoSConditionDestinationPort": alaQoSConditionDestinationPort,
       "alaQoSConditionDestinationPortGroup": alaQoSConditionDestinationPortGroup,
       "alaQoSConditionDestinationPortGroupStatus": alaQoSConditionDestinationPortGroupStatus,
       "alaQoSConditionSourceMacAddr": alaQoSConditionSourceMacAddr,
       "alaQoSConditionSourceMacAddrStatus": alaQoSConditionSourceMacAddrStatus,
       "alaQoSConditionSourceMacMask": alaQoSConditionSourceMacMask,
       "alaQoSConditionSourceMacGroup": alaQoSConditionSourceMacGroup,
       "alaQoSConditionSourceMacGroupStatus": alaQoSConditionSourceMacGroupStatus,
       "alaQoSConditionDestinationMacAddr": alaQoSConditionDestinationMacAddr,
       "alaQoSConditionDestinationMacAddrStatus": alaQoSConditionDestinationMacAddrStatus,
       "alaQoSConditionDestinationMacMask": alaQoSConditionDestinationMacMask,
       "alaQoSConditionDestinationMacGroup": alaQoSConditionDestinationMacGroup,
       "alaQoSConditionDestinationMacGroupStatus": alaQoSConditionDestinationMacGroupStatus,
       "alaQoSConditionSourceVlan": alaQoSConditionSourceVlan,
       "alaQoSConditionSourceVlanStatus": alaQoSConditionSourceVlanStatus,
       "alaQoSConditionDestinationVlan": alaQoSConditionDestinationVlan,
       "alaQoSConditionDestinationVlanStatus": alaQoSConditionDestinationVlanStatus,
       "alaQoSCondition8021p": alaQoSCondition8021p,
       "alaQoSCondition8021pStatus": alaQoSCondition8021pStatus,
       "alaQoSConditionSourceIpAddr": alaQoSConditionSourceIpAddr,
       "alaQoSConditionSourceIpAddrStatus": alaQoSConditionSourceIpAddrStatus,
       "alaQoSConditionSourceIpMask": alaQoSConditionSourceIpMask,
       "alaQoSConditionSourceNetworkGroup": alaQoSConditionSourceNetworkGroup,
       "alaQoSConditionSourceNetworkGroupStatus": alaQoSConditionSourceNetworkGroupStatus,
       "alaQoSConditionDestinationIpAddr": alaQoSConditionDestinationIpAddr,
       "alaQoSConditionDestinationIpAddrStatus": alaQoSConditionDestinationIpAddrStatus,
       "alaQoSConditionDestinationIpMask": alaQoSConditionDestinationIpMask,
       "alaQoSConditionDestinationNetworkGroup": alaQoSConditionDestinationNetworkGroup,
       "alaQoSConditionDestinationNetworkGroupStatus": alaQoSConditionDestinationNetworkGroupStatus,
       "alaQoSConditionMulticastIpAddr": alaQoSConditionMulticastIpAddr,
       "alaQoSConditionMulticastIpAddrStatus": alaQoSConditionMulticastIpAddrStatus,
       "alaQoSConditionMulticastIpMask": alaQoSConditionMulticastIpMask,
       "alaQoSConditionMulticastNetworkGroup": alaQoSConditionMulticastNetworkGroup,
       "alaQoSConditionMulticastNetworkGroupStatus": alaQoSConditionMulticastNetworkGroupStatus,
       "alaQoSConditionTos": alaQoSConditionTos,
       "alaQoSConditionTosStatus": alaQoSConditionTosStatus,
       "alaQoSConditionTosMask": alaQoSConditionTosMask,
       "alaQoSConditionDscp": alaQoSConditionDscp,
       "alaQoSConditionDscpStatus": alaQoSConditionDscpStatus,
       "alaQoSConditionDscpMask": alaQoSConditionDscpMask,
       "alaQoSConditionIpProtocol": alaQoSConditionIpProtocol,
       "alaQoSConditionIpProtocolStatus": alaQoSConditionIpProtocolStatus,
       "alaQoSConditionSourceIpPort": alaQoSConditionSourceIpPort,
       "alaQoSConditionSourceIpPortStatus": alaQoSConditionSourceIpPortStatus,
       "alaQoSConditionDestinationIpPort": alaQoSConditionDestinationIpPort,
       "alaQoSConditionDestinationIpPortStatus": alaQoSConditionDestinationIpPortStatus,
       "alaQoSConditionService": alaQoSConditionService,
       "alaQoSConditionServiceStatus": alaQoSConditionServiceStatus,
       "alaQoSConditionServiceGroup": alaQoSConditionServiceGroup,
       "alaQoSConditionServiceGroupStatus": alaQoSConditionServiceGroupStatus,
       "alaQoSConditionIcmpType": alaQoSConditionIcmpType,
       "alaQoSConditionIcmpTypeStatus": alaQoSConditionIcmpTypeStatus,
       "alaQoSConditionIcmpCode": alaQoSConditionIcmpCode,
       "alaQoSConditionIcmpCodeStatus": alaQoSConditionIcmpCodeStatus,
       "alaQoSConditionRowStatus": alaQoSConditionRowStatus,
       "alaQoSConditionSourcePortEnd": alaQoSConditionSourcePortEnd,
       "alaQoSConditionDestinationPortEnd": alaQoSConditionDestinationPortEnd,
       "alaQoSConditionSourceIpPortEnd": alaQoSConditionSourceIpPortEnd,
       "alaQoSConditionDestinationIpPortEnd": alaQoSConditionDestinationIpPortEnd,
       "alaQoSConditionSourceTcpPort": alaQoSConditionSourceTcpPort,
       "alaQoSConditionSourceTcpPortStatus": alaQoSConditionSourceTcpPortStatus,
       "alaQoSConditionSourceTcpPortEnd": alaQoSConditionSourceTcpPortEnd,
       "alaQoSConditionDestinationTcpPort": alaQoSConditionDestinationTcpPort,
       "alaQoSConditionDestinationTcpPortStatus": alaQoSConditionDestinationTcpPortStatus,
       "alaQoSConditionDestinationTcpPortEnd": alaQoSConditionDestinationTcpPortEnd,
       "alaQoSConditionSourceUdpPort": alaQoSConditionSourceUdpPort,
       "alaQoSConditionSourceUdpPortStatus": alaQoSConditionSourceUdpPortStatus,
       "alaQoSConditionSourceUdpPortEnd": alaQoSConditionSourceUdpPortEnd,
       "alaQoSConditionDestinationUdpPort": alaQoSConditionDestinationUdpPort,
       "alaQoSConditionDestinationUdpPortStatus": alaQoSConditionDestinationUdpPortStatus,
       "alaQoSConditionDestinationUdpPortEnd": alaQoSConditionDestinationUdpPortEnd,
       "alaQoSConditionEthertype": alaQoSConditionEthertype,
       "alaQoSConditionEthertypeStatus": alaQoSConditionEthertypeStatus,
       "alaQoSConditionTcpFlags": alaQoSConditionTcpFlags,
       "alaQoSConditionTcpFlagsStatus": alaQoSConditionTcpFlagsStatus,
       "alaQoSConditionTcpFlagsVal": alaQoSConditionTcpFlagsVal,
       "alaQoSConditionTcpFlagsValStatus": alaQoSConditionTcpFlagsValStatus,
       "alaQoSConditionTcpFlagsMask": alaQoSConditionTcpFlagsMask,
       "alaQoSConditionTcpFlagsMaskStatus": alaQoSConditionTcpFlagsMaskStatus,
       "alaQoSConditionTcpEstablished": alaQoSConditionTcpEstablished,
       "alaQoSConditionSourceIpv6Addr": alaQoSConditionSourceIpv6Addr,
       "alaQoSConditionSourceIpv6AddrStatus": alaQoSConditionSourceIpv6AddrStatus,
       "alaQoSConditionSourceIpv6Mask": alaQoSConditionSourceIpv6Mask,
       "alaQoSConditionDestinationIpv6Addr": alaQoSConditionDestinationIpv6Addr,
       "alaQoSConditionDestinationIpv6AddrStatus": alaQoSConditionDestinationIpv6AddrStatus,
       "alaQoSConditionDestinationIpv6Mask": alaQoSConditionDestinationIpv6Mask,
       "alaQoSConditionIpv6Traffic": alaQoSConditionIpv6Traffic,
       "alaQoSConditionIpv6NH": alaQoSConditionIpv6NH,
       "alaQoSConditionIpv6NHStatus": alaQoSConditionIpv6NHStatus,
       "alaQoSConditionIpv6FlowLabel": alaQoSConditionIpv6FlowLabel,
       "alaQoSConditionIpv6FlowLabelStatus": alaQoSConditionIpv6FlowLabelStatus,
       "alaQoSConditionMcastIpv6Addr": alaQoSConditionMcastIpv6Addr,
       "alaQoSConditionMcastIpv6AddrStatus": alaQoSConditionMcastIpv6AddrStatus,
       "alaQoSConditionMcastIpv6Mask": alaQoSConditionMcastIpv6Mask,
       "alaQoSConditionDscpEnd": alaQoSConditionDscpEnd,
       "alaQoSConditionInnerSourceVlan": alaQoSConditionInnerSourceVlan,
       "alaQoSConditionInnerSourceVlanStatus": alaQoSConditionInnerSourceVlanStatus,
       "alaQoSConditionInner8021p": alaQoSConditionInner8021p,
       "alaQoSConditionInner8021pStatus": alaQoSConditionInner8021pStatus,
       "alaQoSConditionVrfName": alaQoSConditionVrfName,
       "alaQoSConditionVrfNameStatus": alaQoSConditionVrfNameStatus,
       "alaQoSConditionFragments": alaQoSConditionFragments,
       "alaQoSConditionSourceChassis": alaQoSConditionSourceChassis,
       "alaQoSConditionDestinationChassis": alaQoSConditionDestinationChassis,
       "alaQoSConditionAppFpGroup": alaQoSConditionAppFpGroup,
       "alaQoSConditionAppFpGroupStatus": alaQoSConditionAppFpGroupStatus,
       "alaQoSConditionSIP": alaQoSConditionSIP,
       "alaQoSConditionSIPStatus": alaQoSConditionSIPStatus,
       "alaQoSConditionDPIAppName": alaQoSConditionDPIAppName,
       "alaQoSConditionDPIGrpName": alaQoSConditionDPIGrpName,
       "alaQoSConditionDPIAppNameStatus": alaQoSConditionDPIAppNameStatus,
       "alaQoSConditionDPIAppGroupStatus": alaQoSConditionDPIAppGroupStatus,
       "alaQoSConditionVxlanVni": alaQoSConditionVxlanVni,
       "alaQoSConditionVxlanVniStatus": alaQoSConditionVxlanVniStatus,
       "alaQoSConditionVxlanPort": alaQoSConditionVxlanPort,
       "alaQoSConditionVxlanPortStatus": alaQoSConditionVxlanPortStatus,
       "alaQoSConditionVmSourceMacAddr": alaQoSConditionVmSourceMacAddr,
       "alaQoSConditionVmSourceMacAddrStatus": alaQoSConditionVmSourceMacAddrStatus,
       "alaQoSConditionVmSourceMacMask": alaQoSConditionVmSourceMacMask,
       "alaQoSConditionVmSourceIpAddr": alaQoSConditionVmSourceIpAddr,
       "alaQoSConditionVmSourceIpAddrStatus": alaQoSConditionVmSourceIpAddrStatus,
       "alaQoSConditionVmSourceIpMask": alaQoSConditionVmSourceIpMask,
       "alaQoSConditionVmSourceIpv6IpAddr": alaQoSConditionVmSourceIpv6IpAddr,
       "alaQoSConditionVmSourceIpv6IpAddrStatus": alaQoSConditionVmSourceIpv6IpAddrStatus,
       "alaQoSConditionVmSourceIpv6IpMask": alaQoSConditionVmSourceIpv6IpMask,
       "alaQoSConditionVmIpProtocol": alaQoSConditionVmIpProtocol,
       "alaQoSConditionVmIpProtocolStatus": alaQoSConditionVmIpProtocolStatus,
       "alaQosConditionVmL4SourcePort": alaQosConditionVmL4SourcePort,
       "alaQosConditionVmL4SourcePortStatus": alaQosConditionVmL4SourcePortStatus,
       "alaQosConditionVmL4DestPort": alaQosConditionVmL4DestPort,
       "alaQosConditionVmL4DestPortStatus": alaQosConditionVmL4DestPortStatus,
       "alaQosConditionVxlanStatus": alaQosConditionVxlanStatus,
       "alaQoSConditionSourcePortSplitGroup": alaQoSConditionSourcePortSplitGroup,
       "alaQoSConditionSourcePortSplitGroupStatus": alaQoSConditionSourcePortSplitGroupStatus,
       "alaQoSAppliedConditionTable": alaQoSAppliedConditionTable,
       "alaQoSAppliedConditionEntry": alaQoSAppliedConditionEntry,
       "alaQoSAppliedConditionName": alaQoSAppliedConditionName,
       "alaQoSAppliedConditionSource": alaQoSAppliedConditionSource,
       "alaQoSAppliedConditionSourceSlot": alaQoSAppliedConditionSourceSlot,
       "alaQoSAppliedConditionSourceSlotStatus": alaQoSAppliedConditionSourceSlotStatus,
       "alaQoSAppliedConditionSourcePort": alaQoSAppliedConditionSourcePort,
       "alaQoSAppliedConditionSourcePortGroup": alaQoSAppliedConditionSourcePortGroup,
       "alaQoSAppliedConditionSourcePortGroupStatus": alaQoSAppliedConditionSourcePortGroupStatus,
       "alaQoSAppliedConditionDestinationSlot": alaQoSAppliedConditionDestinationSlot,
       "alaQoSAppliedConditionDestinationSlotStatus": alaQoSAppliedConditionDestinationSlotStatus,
       "alaQoSAppliedConditionDestinationPort": alaQoSAppliedConditionDestinationPort,
       "alaQoSAppliedConditionDestinationPortGroup": alaQoSAppliedConditionDestinationPortGroup,
       "alaQoSAppliedConditionDestinationPortGroupStatus": alaQoSAppliedConditionDestinationPortGroupStatus,
       "alaQoSAppliedConditionSourceMacAddr": alaQoSAppliedConditionSourceMacAddr,
       "alaQoSAppliedConditionSourceMacAddrStatus": alaQoSAppliedConditionSourceMacAddrStatus,
       "alaQoSAppliedConditionSourceMacMask": alaQoSAppliedConditionSourceMacMask,
       "alaQoSAppliedConditionSourceMacGroup": alaQoSAppliedConditionSourceMacGroup,
       "alaQoSAppliedConditionSourceMacGroupStatus": alaQoSAppliedConditionSourceMacGroupStatus,
       "alaQoSAppliedConditionDestinationMacAddr": alaQoSAppliedConditionDestinationMacAddr,
       "alaQoSAppliedConditionDestinationMacAddrStatus": alaQoSAppliedConditionDestinationMacAddrStatus,
       "alaQoSAppliedConditionDestinationMacMask": alaQoSAppliedConditionDestinationMacMask,
       "alaQoSAppliedConditionDestinationMacGroup": alaQoSAppliedConditionDestinationMacGroup,
       "alaQoSAppliedConditionDestinationMacGroupStatus": alaQoSAppliedConditionDestinationMacGroupStatus,
       "alaQoSAppliedConditionSourceVlan": alaQoSAppliedConditionSourceVlan,
       "alaQoSAppliedConditionSourceVlanStatus": alaQoSAppliedConditionSourceVlanStatus,
       "alaQoSAppliedConditionDestinationVlan": alaQoSAppliedConditionDestinationVlan,
       "alaQoSAppliedConditionDestinationVlanStatus": alaQoSAppliedConditionDestinationVlanStatus,
       "alaQoSAppliedCondition8021p": alaQoSAppliedCondition8021p,
       "alaQoSAppliedCondition8021pStatus": alaQoSAppliedCondition8021pStatus,
       "alaQoSAppliedConditionSourceIpAddr": alaQoSAppliedConditionSourceIpAddr,
       "alaQoSAppliedConditionSourceIpAddrStatus": alaQoSAppliedConditionSourceIpAddrStatus,
       "alaQoSAppliedConditionSourceIpMask": alaQoSAppliedConditionSourceIpMask,
       "alaQoSAppliedConditionSourceNetworkGroup": alaQoSAppliedConditionSourceNetworkGroup,
       "alaQoSAppliedConditionSourceNetworkGroupStatus": alaQoSAppliedConditionSourceNetworkGroupStatus,
       "alaQoSAppliedConditionDestinationIpAddr": alaQoSAppliedConditionDestinationIpAddr,
       "alaQoSAppliedConditionDestinationIpAddrStatus": alaQoSAppliedConditionDestinationIpAddrStatus,
       "alaQoSAppliedConditionDestinationIpMask": alaQoSAppliedConditionDestinationIpMask,
       "alaQoSAppliedConditionDestinationNetworkGroup": alaQoSAppliedConditionDestinationNetworkGroup,
       "alaQoSAppliedConditionDestinationNetworkGroupStatus": alaQoSAppliedConditionDestinationNetworkGroupStatus,
       "alaQoSAppliedConditionMulticastIpAddr": alaQoSAppliedConditionMulticastIpAddr,
       "alaQoSAppliedConditionMulticastIpAddrStatus": alaQoSAppliedConditionMulticastIpAddrStatus,
       "alaQoSAppliedConditionMulticastIpMask": alaQoSAppliedConditionMulticastIpMask,
       "alaQoSAppliedConditionMulticastNetworkGroup": alaQoSAppliedConditionMulticastNetworkGroup,
       "alaQoSAppliedConditionMulticastNetworkGroupStatus": alaQoSAppliedConditionMulticastNetworkGroupStatus,
       "alaQoSAppliedConditionTos": alaQoSAppliedConditionTos,
       "alaQoSAppliedConditionTosStatus": alaQoSAppliedConditionTosStatus,
       "alaQoSAppliedConditionTosMask": alaQoSAppliedConditionTosMask,
       "alaQoSAppliedConditionDscp": alaQoSAppliedConditionDscp,
       "alaQoSAppliedConditionDscpStatus": alaQoSAppliedConditionDscpStatus,
       "alaQoSAppliedConditionDscpMask": alaQoSAppliedConditionDscpMask,
       "alaQoSAppliedConditionIpProtocol": alaQoSAppliedConditionIpProtocol,
       "alaQoSAppliedConditionIpProtocolStatus": alaQoSAppliedConditionIpProtocolStatus,
       "alaQoSAppliedConditionSourceIpPort": alaQoSAppliedConditionSourceIpPort,
       "alaQoSAppliedConditionSourceIpPortStatus": alaQoSAppliedConditionSourceIpPortStatus,
       "alaQoSAppliedConditionDestinationIpPort": alaQoSAppliedConditionDestinationIpPort,
       "alaQoSAppliedConditionDestinationIpPortStatus": alaQoSAppliedConditionDestinationIpPortStatus,
       "alaQoSAppliedConditionService": alaQoSAppliedConditionService,
       "alaQoSAppliedConditionServiceStatus": alaQoSAppliedConditionServiceStatus,
       "alaQoSAppliedConditionServiceGroup": alaQoSAppliedConditionServiceGroup,
       "alaQoSAppliedConditionServiceGroupStatus": alaQoSAppliedConditionServiceGroupStatus,
       "alaQoSAppliedConditionIcmpType": alaQoSAppliedConditionIcmpType,
       "alaQoSAppliedConditionIcmpTypeStatus": alaQoSAppliedConditionIcmpTypeStatus,
       "alaQoSAppliedConditionIcmpCode": alaQoSAppliedConditionIcmpCode,
       "alaQoSAppliedConditionIcmpCodeStatus": alaQoSAppliedConditionIcmpCodeStatus,
       "alaQoSAppliedConditionRowStatus": alaQoSAppliedConditionRowStatus,
       "alaQoSAppliedConditionSourcePortEnd": alaQoSAppliedConditionSourcePortEnd,
       "alaQoSAppliedConditionDestinationPortEnd": alaQoSAppliedConditionDestinationPortEnd,
       "alaQoSAppliedConditionSourceIpPortEnd": alaQoSAppliedConditionSourceIpPortEnd,
       "alaQoSAppliedConditionDestinationIpPortEnd": alaQoSAppliedConditionDestinationIpPortEnd,
       "alaQoSAppliedConditionSourceTcpPort": alaQoSAppliedConditionSourceTcpPort,
       "alaQoSAppliedConditionSourceTcpPortStatus": alaQoSAppliedConditionSourceTcpPortStatus,
       "alaQoSAppliedConditionSourceTcpPortEnd": alaQoSAppliedConditionSourceTcpPortEnd,
       "alaQoSAppliedConditionDestinationTcpPort": alaQoSAppliedConditionDestinationTcpPort,
       "alaQoSAppliedConditionDestinationTcpPortStatus": alaQoSAppliedConditionDestinationTcpPortStatus,
       "alaQoSAppliedConditionDestinationTcpPortEnd": alaQoSAppliedConditionDestinationTcpPortEnd,
       "alaQoSAppliedConditionSourceUdpPort": alaQoSAppliedConditionSourceUdpPort,
       "alaQoSAppliedConditionSourceUdpPortStatus": alaQoSAppliedConditionSourceUdpPortStatus,
       "alaQoSAppliedConditionSourceUdpPortEnd": alaQoSAppliedConditionSourceUdpPortEnd,
       "alaQoSAppliedConditionDestinationUdpPort": alaQoSAppliedConditionDestinationUdpPort,
       "alaQoSAppliedConditionDestinationUdpPortStatus": alaQoSAppliedConditionDestinationUdpPortStatus,
       "alaQoSAppliedConditionDestinationUdpPortEnd": alaQoSAppliedConditionDestinationUdpPortEnd,
       "alaQoSAppliedConditionEthertype": alaQoSAppliedConditionEthertype,
       "alaQoSAppliedConditionEthertypeStatus": alaQoSAppliedConditionEthertypeStatus,
       "alaQoSAppliedConditionTcpFlags": alaQoSAppliedConditionTcpFlags,
       "alaQoSAppliedConditionTcpFlagsStatus": alaQoSAppliedConditionTcpFlagsStatus,
       "alaQoSAppliedConditionTcpFlagsVal": alaQoSAppliedConditionTcpFlagsVal,
       "alaQoSAppliedConditionTcpFlagsValStatus": alaQoSAppliedConditionTcpFlagsValStatus,
       "alaQoSAppliedConditionTcpFlagsMask": alaQoSAppliedConditionTcpFlagsMask,
       "alaQoSAppliedConditionTcpFlagsMaskStatus": alaQoSAppliedConditionTcpFlagsMaskStatus,
       "alaQoSAppliedConditionTcpEstablished": alaQoSAppliedConditionTcpEstablished,
       "alaQoSAppliedConditionSourceIpv6Addr": alaQoSAppliedConditionSourceIpv6Addr,
       "alaQoSAppliedConditionSourceIpv6AddrStatus": alaQoSAppliedConditionSourceIpv6AddrStatus,
       "alaQoSAppliedConditionSourceIpv6Mask": alaQoSAppliedConditionSourceIpv6Mask,
       "alaQoSAppliedConditionDestinationIpv6Addr": alaQoSAppliedConditionDestinationIpv6Addr,
       "alaQoSAppliedConditionDestinationIpv6AddrStatus": alaQoSAppliedConditionDestinationIpv6AddrStatus,
       "alaQoSAppliedConditionDestinationIpv6Mask": alaQoSAppliedConditionDestinationIpv6Mask,
       "alaQoSAppliedConditionIpv6Traffic": alaQoSAppliedConditionIpv6Traffic,
       "alaQoSAppliedConditionIpv6NH": alaQoSAppliedConditionIpv6NH,
       "alaQoSAppliedConditionIpv6NHStatus": alaQoSAppliedConditionIpv6NHStatus,
       "alaQoSAppliedConditionIpv6FlowLabel": alaQoSAppliedConditionIpv6FlowLabel,
       "alaQoSAppliedConditionIpv6FlowLabelStatus": alaQoSAppliedConditionIpv6FlowLabelStatus,
       "alaQoSAppliedConditionMcastIpv6Addr": alaQoSAppliedConditionMcastIpv6Addr,
       "alaQoSAppliedConditionMcastIpv6AddrStatus": alaQoSAppliedConditionMcastIpv6AddrStatus,
       "alaQoSAppliedConditionMcastIpv6Mask": alaQoSAppliedConditionMcastIpv6Mask,
       "alaQoSAppliedConditionDscpEnd": alaQoSAppliedConditionDscpEnd,
       "alaQoSAppliedConditionInnerSourceVlan": alaQoSAppliedConditionInnerSourceVlan,
       "alaQoSAppliedConditionInnerSourceVlanStatus": alaQoSAppliedConditionInnerSourceVlanStatus,
       "alaQoSAppliedConditionInner8021p": alaQoSAppliedConditionInner8021p,
       "alaQoSAppliedConditionInner8021pStatus": alaQoSAppliedConditionInner8021pStatus,
       "alaQoSAppliedConditionVrfName": alaQoSAppliedConditionVrfName,
       "alaQoSAppliedConditionVrfNameStatus": alaQoSAppliedConditionVrfNameStatus,
       "alaQoSAppliedConditionFragments": alaQoSAppliedConditionFragments,
       "alaQoSAppliedConditionSourceChassis": alaQoSAppliedConditionSourceChassis,
       "alaQoSAppliedConditionDestinationChassis": alaQoSAppliedConditionDestinationChassis,
       "alaQoSAppliedConditionAppFpGroup": alaQoSAppliedConditionAppFpGroup,
       "alaQoSAppliedConditionAppFpGroupStatus": alaQoSAppliedConditionAppFpGroupStatus,
       "alaQoSAppliedConditionSIP": alaQoSAppliedConditionSIP,
       "alaQoSAppliedConditionSIPStatus": alaQoSAppliedConditionSIPStatus,
       "alaQoSAppliedConditionDPIAppName": alaQoSAppliedConditionDPIAppName,
       "alaQoSAppliedConditionDPIAppGrp": alaQoSAppliedConditionDPIAppGrp,
       "alaQoSAppliedConditionDPIAppNameStatus": alaQoSAppliedConditionDPIAppNameStatus,
       "alaQoSAppliedConditionDPIAppGroupStatus": alaQoSAppliedConditionDPIAppGroupStatus,
       "alaQoSAppliedConditionVxlanVni": alaQoSAppliedConditionVxlanVni,
       "alaQoSAppliedConditionVxlanVniStatus": alaQoSAppliedConditionVxlanVniStatus,
       "alaQoSAppliedConditionVxlanPort": alaQoSAppliedConditionVxlanPort,
       "alaQoSAppliedConditionVxlanPortStatus": alaQoSAppliedConditionVxlanPortStatus,
       "alaQoSAppliedConditionVmSourceMacAddr": alaQoSAppliedConditionVmSourceMacAddr,
       "alaQoSAppliedConditionVmSourceMacAddrStatus": alaQoSAppliedConditionVmSourceMacAddrStatus,
       "alaQoSAppliedConditionVmSourceMacMask": alaQoSAppliedConditionVmSourceMacMask,
       "alaQoSAppliedConditionVmSourceIpAddr": alaQoSAppliedConditionVmSourceIpAddr,
       "alaQoSAppliedConditionVmSourceIpAddrStatus": alaQoSAppliedConditionVmSourceIpAddrStatus,
       "alaQoSAppliedConditionVmSourceIpMask": alaQoSAppliedConditionVmSourceIpMask,
       "alaQoSAppliedConditionVmSourceIpv6IpAddr": alaQoSAppliedConditionVmSourceIpv6IpAddr,
       "alaQoSAppliedConditionVmSourceIpv6IpAddrStatus": alaQoSAppliedConditionVmSourceIpv6IpAddrStatus,
       "alaQoSAppliedConditionVmSourceIpv6IpMask": alaQoSAppliedConditionVmSourceIpv6IpMask,
       "alaQoSAppliedConditionVmIpProtocol": alaQoSAppliedConditionVmIpProtocol,
       "alaQoSAppliedConditionVmIpProtocolStatus": alaQoSAppliedConditionVmIpProtocolStatus,
       "alaQosAppliedConditionVmL4SourcePort": alaQosAppliedConditionVmL4SourcePort,
       "alaQosAppliedConditionVmL4SourcePortStatus": alaQosAppliedConditionVmL4SourcePortStatus,
       "alaQosAppliedConditionVmL4DestPort": alaQosAppliedConditionVmL4DestPort,
       "alaQosAppliedConditionVmL4DestPortStatus": alaQosAppliedConditionVmL4DestPortStatus,
       "alaQosAppliedConditionVxlanStatus": alaQosAppliedConditionVxlanStatus,
       "alaQoSAppliedConditionSourcePortSplitGroup": alaQoSAppliedConditionSourcePortSplitGroup,
       "alaQoSAppliedConditionSourcePortSplitGroupStatus": alaQoSAppliedConditionSourcePortSplitGroupStatus,
       "alaQoSServiceTable": alaQoSServiceTable,
       "alaQoSServiceEntry": alaQoSServiceEntry,
       "alaQoSServiceName": alaQoSServiceName,
       "alaQoSServiceSource": alaQoSServiceSource,
       "alaQoSServiceProtocol": alaQoSServiceProtocol,
       "alaQoSServiceSourceIpPort": alaQoSServiceSourceIpPort,
       "alaQoSServiceSourceIpPortStatus": alaQoSServiceSourceIpPortStatus,
       "alaQoSServiceDestinationIpPort": alaQoSServiceDestinationIpPort,
       "alaQoSServiceDestinationIpPortStatus": alaQoSServiceDestinationIpPortStatus,
       "alaQoSServiceRowStatus": alaQoSServiceRowStatus,
       "alaQoSServiceSourceIpPortEnd": alaQoSServiceSourceIpPortEnd,
       "alaQoSServiceDestinationIpPortEnd": alaQoSServiceDestinationIpPortEnd,
       "alaQoSServiceSourceTcpPort": alaQoSServiceSourceTcpPort,
       "alaQoSServiceSourceTcpPortStatus": alaQoSServiceSourceTcpPortStatus,
       "alaQoSServiceSourceTcpPortEnd": alaQoSServiceSourceTcpPortEnd,
       "alaQoSServiceDestinationTcpPort": alaQoSServiceDestinationTcpPort,
       "alaQoSServiceDestinationTcpPortStatus": alaQoSServiceDestinationTcpPortStatus,
       "alaQoSServiceDestinationTcpPortEnd": alaQoSServiceDestinationTcpPortEnd,
       "alaQoSServiceSourceUdpPort": alaQoSServiceSourceUdpPort,
       "alaQoSServiceSourceUdpPortStatus": alaQoSServiceSourceUdpPortStatus,
       "alaQoSServiceSourceUdpPortEnd": alaQoSServiceSourceUdpPortEnd,
       "alaQoSServiceDestinationUdpPort": alaQoSServiceDestinationUdpPort,
       "alaQoSServiceDestinationUdpPortStatus": alaQoSServiceDestinationUdpPortStatus,
       "alaQoSServiceDestinationUdpPortEnd": alaQoSServiceDestinationUdpPortEnd,
       "alaQoSAppliedServiceTable": alaQoSAppliedServiceTable,
       "alaQoSAppliedServiceEntry": alaQoSAppliedServiceEntry,
       "alaQoSAppliedServiceName": alaQoSAppliedServiceName,
       "alaQoSAppliedServiceSource": alaQoSAppliedServiceSource,
       "alaQoSAppliedServiceProtocol": alaQoSAppliedServiceProtocol,
       "alaQoSAppliedServiceSourceIpPort": alaQoSAppliedServiceSourceIpPort,
       "alaQoSAppliedServiceSourceIpPortStatus": alaQoSAppliedServiceSourceIpPortStatus,
       "alaQoSAppliedServiceDestinationIpPort": alaQoSAppliedServiceDestinationIpPort,
       "alaQoSAppliedServiceDestinationIpPortStatus": alaQoSAppliedServiceDestinationIpPortStatus,
       "alaQoSAppliedServiceRowStatus": alaQoSAppliedServiceRowStatus,
       "alaQoSAppliedServiceSourceIpPortEnd": alaQoSAppliedServiceSourceIpPortEnd,
       "alaQoSAppliedServiceDestinationIpPortEnd": alaQoSAppliedServiceDestinationIpPortEnd,
       "alaQoSAppliedServiceSourceTcpPort": alaQoSAppliedServiceSourceTcpPort,
       "alaQoSAppliedServiceSourceTcpPortStatus": alaQoSAppliedServiceSourceTcpPortStatus,
       "alaQoSAppliedServiceSourceTcpPortEnd": alaQoSAppliedServiceSourceTcpPortEnd,
       "alaQoSAppliedServiceDestinationTcpPort": alaQoSAppliedServiceDestinationTcpPort,
       "alaQoSAppliedServiceDestinationTcpPortStatus": alaQoSAppliedServiceDestinationTcpPortStatus,
       "alaQoSAppliedServiceDestinationTcpPortEnd": alaQoSAppliedServiceDestinationTcpPortEnd,
       "alaQoSAppliedServiceSourceUdpPort": alaQoSAppliedServiceSourceUdpPort,
       "alaQoSAppliedServiceSourceUdpPortStatus": alaQoSAppliedServiceSourceUdpPortStatus,
       "alaQoSAppliedServiceSourceUdpPortEnd": alaQoSAppliedServiceSourceUdpPortEnd,
       "alaQoSAppliedServiceDestinationUdpPort": alaQoSAppliedServiceDestinationUdpPort,
       "alaQoSAppliedServiceDestinationUdpPortStatus": alaQoSAppliedServiceDestinationUdpPortStatus,
       "alaQoSAppliedServiceDestinationUdpPortEnd": alaQoSAppliedServiceDestinationUdpPortEnd,
       "alaQoSServiceGroupsTable": alaQoSServiceGroupsTable,
       "alaQoSServiceGroupsEntry": alaQoSServiceGroupsEntry,
       "alaQoSServiceGroupsName": alaQoSServiceGroupsName,
       "alaQoSServiceGroupsSource": alaQoSServiceGroupsSource,
       "alaQoSServiceGroupsStatus": alaQoSServiceGroupsStatus,
       "alaQoSAppliedServiceGroupsTable": alaQoSAppliedServiceGroupsTable,
       "alaQoSAppliedServiceGroupsEntry": alaQoSAppliedServiceGroupsEntry,
       "alaQoSAppliedServiceGroupsName": alaQoSAppliedServiceGroupsName,
       "alaQoSAppliedServiceGroupsSource": alaQoSAppliedServiceGroupsSource,
       "alaQoSAppliedServiceGroupsStatus": alaQoSAppliedServiceGroupsStatus,
       "alaQoSServiceGroupTable": alaQoSServiceGroupTable,
       "alaQoSServiceGroupEntry": alaQoSServiceGroupEntry,
       "alaQoSServiceGroupServiceName": alaQoSServiceGroupServiceName,
       "alaQoSServiceGroupStatus": alaQoSServiceGroupStatus,
       "alaQoSAppliedServiceGroupTable": alaQoSAppliedServiceGroupTable,
       "alaQoSAppliedServiceGroupEntry": alaQoSAppliedServiceGroupEntry,
       "alaQoSAppliedServiceGroupServiceName": alaQoSAppliedServiceGroupServiceName,
       "alaQoSAppliedServiceGroupStatus": alaQoSAppliedServiceGroupStatus,
       "alaQoSNetworkGroupsTable": alaQoSNetworkGroupsTable,
       "alaQoSNetworkGroupsEntry": alaQoSNetworkGroupsEntry,
       "alaQoSNetworkGroupsName": alaQoSNetworkGroupsName,
       "alaQoSNetworkGroupsSource": alaQoSNetworkGroupsSource,
       "alaQoSNetworkGroupsStatus": alaQoSNetworkGroupsStatus,
       "alaQoSAppliedNetworkGroupsTable": alaQoSAppliedNetworkGroupsTable,
       "alaQoSAppliedNetworkGroupsEntry": alaQoSAppliedNetworkGroupsEntry,
       "alaQoSAppliedNetworkGroupsName": alaQoSAppliedNetworkGroupsName,
       "alaQoSAppliedNetworkGroupsSource": alaQoSAppliedNetworkGroupsSource,
       "alaQoSAppliedNetworkGroupsStatus": alaQoSAppliedNetworkGroupsStatus,
       "alaQoSNetworkGroupTable": alaQoSNetworkGroupTable,
       "alaQoSNetworkGroupEntry": alaQoSNetworkGroupEntry,
       "alaQoSNetworkGroupIpAddr": alaQoSNetworkGroupIpAddr,
       "alaQoSNetworkGroupIpMask": alaQoSNetworkGroupIpMask,
       "alaQoSNetworkGroupStatus": alaQoSNetworkGroupStatus,
       "alaQoSAppliedNetworkGroupTable": alaQoSAppliedNetworkGroupTable,
       "alaQoSAppliedNetworkGroupEntry": alaQoSAppliedNetworkGroupEntry,
       "alaQoSAppliedNetworkGroupIpAddr": alaQoSAppliedNetworkGroupIpAddr,
       "alaQoSAppliedNetworkGroupIpMask": alaQoSAppliedNetworkGroupIpMask,
       "alaQoSAppliedNetworkGroupStatus": alaQoSAppliedNetworkGroupStatus,
       "alaQoSMACGroupsTable": alaQoSMACGroupsTable,
       "alaQoSMACGroupsEntry": alaQoSMACGroupsEntry,
       "alaQoSMACGroupsName": alaQoSMACGroupsName,
       "alaQoSMACGroupsSource": alaQoSMACGroupsSource,
       "alaQoSMACGroupsStatus": alaQoSMACGroupsStatus,
       "alaQoSAppliedMACGroupsTable": alaQoSAppliedMACGroupsTable,
       "alaQoSAppliedMACGroupsEntry": alaQoSAppliedMACGroupsEntry,
       "alaQoSAppliedMACGroupsName": alaQoSAppliedMACGroupsName,
       "alaQoSAppliedMACGroupsSource": alaQoSAppliedMACGroupsSource,
       "alaQoSAppliedMACGroupsStatus": alaQoSAppliedMACGroupsStatus,
       "alaQoSMACGroupTable": alaQoSMACGroupTable,
       "alaQoSMACGroupEntry": alaQoSMACGroupEntry,
       "alaQoSMACGroupMacAddr": alaQoSMACGroupMacAddr,
       "alaQoSMACGroupMacMask": alaQoSMACGroupMacMask,
       "alaQoSMACGroupStatus": alaQoSMACGroupStatus,
       "alaQoSAppliedMACGroupTable": alaQoSAppliedMACGroupTable,
       "alaQoSAppliedMACGroupEntry": alaQoSAppliedMACGroupEntry,
       "alaQoSAppliedMACGroupMacAddr": alaQoSAppliedMACGroupMacAddr,
       "alaQoSAppliedMACGroupMacMask": alaQoSAppliedMACGroupMacMask,
       "alaQoSAppliedMACGroupStatus": alaQoSAppliedMACGroupStatus,
       "alaQoSPortGroupsTable": alaQoSPortGroupsTable,
       "alaQoSPortGroupsEntry": alaQoSPortGroupsEntry,
       "alaQoSPortGroupsName": alaQoSPortGroupsName,
       "alaQoSPortGroupsSource": alaQoSPortGroupsSource,
       "alaQoSPortGroupsStatus": alaQoSPortGroupsStatus,
       "alaQoSAppliedPortGroupsTable": alaQoSAppliedPortGroupsTable,
       "alaQoSAppliedPortGroupsEntry": alaQoSAppliedPortGroupsEntry,
       "alaQoSAppliedPortGroupsName": alaQoSAppliedPortGroupsName,
       "alaQoSAppliedPortGroupsSource": alaQoSAppliedPortGroupsSource,
       "alaQoSAppliedPortGroupsStatus": alaQoSAppliedPortGroupsStatus,
       "alaQoSPortGroupTable": alaQoSPortGroupTable,
       "alaQoSPortGroupEntry": alaQoSPortGroupEntry,
       "alaQoSPortGroupSlot": alaQoSPortGroupSlot,
       "alaQoSPortGroupPort": alaQoSPortGroupPort,
       "alaQoSPortGroupStatus": alaQoSPortGroupStatus,
       "alaQoSPortGroupPortEnd": alaQoSPortGroupPortEnd,
       "alaQoSAppliedPortGroupTable": alaQoSAppliedPortGroupTable,
       "alaQoSAppliedPortGroupEntry": alaQoSAppliedPortGroupEntry,
       "alaQoSAppliedPortGroupSlot": alaQoSAppliedPortGroupSlot,
       "alaQoSAppliedPortGroupPort": alaQoSAppliedPortGroupPort,
       "alaQoSAppliedPortGroupStatus": alaQoSAppliedPortGroupStatus,
       "alaQoSAppliedPortGroupPortEnd": alaQoSAppliedPortGroupPortEnd,
       "alaQoSMapGroupsTable": alaQoSMapGroupsTable,
       "alaQoSMapGroupsEntry": alaQoSMapGroupsEntry,
       "alaQoSMapGroupsName": alaQoSMapGroupsName,
       "alaQoSMapGroupsSource": alaQoSMapGroupsSource,
       "alaQoSMapGroupsStatus": alaQoSMapGroupsStatus,
       "alaQoSAppliedMapGroupsTable": alaQoSAppliedMapGroupsTable,
       "alaQoSAppliedMapGroupsEntry": alaQoSAppliedMapGroupsEntry,
       "alaQoSAppliedMapGroupsName": alaQoSAppliedMapGroupsName,
       "alaQoSAppliedMapGroupsSource": alaQoSAppliedMapGroupsSource,
       "alaQoSAppliedMapGroupsStatus": alaQoSAppliedMapGroupsStatus,
       "alaQoSMapGroupTable": alaQoSMapGroupTable,
       "alaQoSMapGroupEntry": alaQoSMapGroupEntry,
       "alaQoSMapGroupKey": alaQoSMapGroupKey,
       "alaQoSMapGroupKeyEnd": alaQoSMapGroupKeyEnd,
       "alaQoSMapGroupValue": alaQoSMapGroupValue,
       "alaQoSMapGroupStatus": alaQoSMapGroupStatus,
       "alaQoSAppliedMapGroupTable": alaQoSAppliedMapGroupTable,
       "alaQoSAppliedMapGroupEntry": alaQoSAppliedMapGroupEntry,
       "alaQoSAppliedMapGroupKey": alaQoSAppliedMapGroupKey,
       "alaQoSAppliedMapGroupKeyEnd": alaQoSAppliedMapGroupKeyEnd,
       "alaQoSAppliedMapGroupValue": alaQoSAppliedMapGroupValue,
       "alaQoSAppliedMapGroupStatus": alaQoSAppliedMapGroupStatus,
       "alaQoSActionTable": alaQoSActionTable,
       "alaQoSActionEntry": alaQoSActionEntry,
       "alaQoSActionName": alaQoSActionName,
       "alaQoSActionSource": alaQoSActionSource,
       "alaQoSActionDisposition": alaQoSActionDisposition,
       "alaQoSActionMaximumBandwidth": alaQoSActionMaximumBandwidth,
       "alaQoSActionMaximumBandwidthStatus": alaQoSActionMaximumBandwidthStatus,
       "alaQoSActionPriority": alaQoSActionPriority,
       "alaQoSActionPriorityStatus": alaQoSActionPriorityStatus,
       "alaQoSActionShared": alaQoSActionShared,
       "alaQoSActionMaximumDepth": alaQoSActionMaximumDepth,
       "alaQoSActionMaximumDepthStatus": alaQoSActionMaximumDepthStatus,
       "alaQoSAction8021p": alaQoSAction8021p,
       "alaQoSAction8021pStatus": alaQoSAction8021pStatus,
       "alaQoSActionTos": alaQoSActionTos,
       "alaQoSActionTosStatus": alaQoSActionTosStatus,
       "alaQoSActionDscp": alaQoSActionDscp,
       "alaQoSActionDscpStatus": alaQoSActionDscpStatus,
       "alaQoSActionMapFrom": alaQoSActionMapFrom,
       "alaQoSActionMapTo": alaQoSActionMapTo,
       "alaQoSActionMapGroup": alaQoSActionMapGroup,
       "alaQoSActionMapGroupStatus": alaQoSActionMapGroupStatus,
       "alaQoSActionLoadBalanceGroup": alaQoSActionLoadBalanceGroup,
       "alaQoSActionLoadBalanceGroupStatus": alaQoSActionLoadBalanceGroupStatus,
       "alaQoSActionPermanentGatewayIpAddr": alaQoSActionPermanentGatewayIpAddr,
       "alaQoSActionPermanentGatewayIpAddrStatus": alaQoSActionPermanentGatewayIpAddrStatus,
       "alaQoSActionAlternateGatewayIpAddr": alaQoSActionAlternateGatewayIpAddr,
       "alaQoSActionAlternateGatewayIpAddrStatus": alaQoSActionAlternateGatewayIpAddrStatus,
       "alaQoSActionRowStatus": alaQoSActionRowStatus,
       "alaQoSActionNocache": alaQoSActionNocache,
       "alaQoSActionPortdisable": alaQoSActionPortdisable,
       "alaQoSActionRedirectSlot": alaQoSActionRedirectSlot,
       "alaQoSActionRedirectSlotStatus": alaQoSActionRedirectSlotStatus,
       "alaQoSActionRedirectPort": alaQoSActionRedirectPort,
       "alaQoSActionRedirectAgg": alaQoSActionRedirectAgg,
       "alaQoSActionRedirectAggStatus": alaQoSActionRedirectAggStatus,
       "alaQoSActionMirrorSlot": alaQoSActionMirrorSlot,
       "alaQoSActionMirrorPort": alaQoSActionMirrorPort,
       "alaQoSActionMirrorMode": alaQoSActionMirrorMode,
       "alaQoSActionMirrorModeStatus": alaQoSActionMirrorModeStatus,
       "alaQoSActionCIR": alaQoSActionCIR,
       "alaQoSActionCIRStatus": alaQoSActionCIRStatus,
       "alaQoSActionCBS": alaQoSActionCBS,
       "alaQoSActionCBSStatus": alaQoSActionCBSStatus,
       "alaQoSActionPIR": alaQoSActionPIR,
       "alaQoSActionPIRStatus": alaQoSActionPIRStatus,
       "alaQoSActionPBS": alaQoSActionPBS,
       "alaQoSActionPBSStatus": alaQoSActionPBSStatus,
       "alaQoSActionCPUPriority": alaQoSActionCPUPriority,
       "alaQoSActionCPUPriorityStatus": alaQoSActionCPUPriorityStatus,
       "alaQoSActionColorOnly": alaQoSActionColorOnly,
       "alaQoSActionRedirectChassis": alaQoSActionRedirectChassis,
       "alaQoSActionMirrorChassis": alaQoSActionMirrorChassis,
       "alaQoSActionPermanentGatewayIpV6Addr": alaQoSActionPermanentGatewayIpV6Addr,
       "alaQoSActionPermanentGatewayIpV6AddrStatus": alaQoSActionPermanentGatewayIpV6AddrStatus,
       "alaQoSActionPermanentGatewayIpV6IfIndex": alaQoSActionPermanentGatewayIpV6IfIndex,
       "alaQoSActionRTCPMonitor": alaQoSActionRTCPMonitor,
       "alaQoSActionRTCPMonitorStatus": alaQoSActionRTCPMonitorStatus,
       "alaQoSActionRTCPDSCP": alaQoSActionRTCPDSCP,
       "alaQoSActionRTCPDSCPStatus": alaQoSActionRTCPDSCPStatus,
       "alaQoSActionTrustDSCP": alaQoSActionTrustDSCP,
       "alaQoSActionTrustDSCPStatus": alaQoSActionTrustDSCPStatus,
       "alaQoSActionRedirectModule": alaQoSActionRedirectModule,
       "alaQoSAppliedActionTable": alaQoSAppliedActionTable,
       "alaQoSAppliedActionEntry": alaQoSAppliedActionEntry,
       "alaQoSAppliedActionName": alaQoSAppliedActionName,
       "alaQoSAppliedActionSource": alaQoSAppliedActionSource,
       "alaQoSAppliedActionDisposition": alaQoSAppliedActionDisposition,
       "alaQoSAppliedActionMaximumBandwidth": alaQoSAppliedActionMaximumBandwidth,
       "alaQoSAppliedActionMaximumBandwidthStatus": alaQoSAppliedActionMaximumBandwidthStatus,
       "alaQoSAppliedActionPriority": alaQoSAppliedActionPriority,
       "alaQoSAppliedActionPriorityStatus": alaQoSAppliedActionPriorityStatus,
       "alaQoSAppliedActionShared": alaQoSAppliedActionShared,
       "alaQoSAppliedActionMaximumDepth": alaQoSAppliedActionMaximumDepth,
       "alaQoSAppliedActionMaximumDepthStatus": alaQoSAppliedActionMaximumDepthStatus,
       "alaQoSAppliedAction8021p": alaQoSAppliedAction8021p,
       "alaQoSAppliedAction8021pStatus": alaQoSAppliedAction8021pStatus,
       "alaQoSAppliedActionTos": alaQoSAppliedActionTos,
       "alaQoSAppliedActionTosStatus": alaQoSAppliedActionTosStatus,
       "alaQoSAppliedActionDscp": alaQoSAppliedActionDscp,
       "alaQoSAppliedActionDscpStatus": alaQoSAppliedActionDscpStatus,
       "alaQoSAppliedActionMapFrom": alaQoSAppliedActionMapFrom,
       "alaQoSAppliedActionMapTo": alaQoSAppliedActionMapTo,
       "alaQoSAppliedActionMapGroup": alaQoSAppliedActionMapGroup,
       "alaQoSAppliedActionMapGroupStatus": alaQoSAppliedActionMapGroupStatus,
       "alaQoSAppliedActionLoadBalanceGroup": alaQoSAppliedActionLoadBalanceGroup,
       "alaQoSAppliedActionLoadBalanceGroupStatus": alaQoSAppliedActionLoadBalanceGroupStatus,
       "alaQoSAppliedActionPermanentGatewayIpAddr": alaQoSAppliedActionPermanentGatewayIpAddr,
       "alaQoSAppliedActionPermanentGatewayIpAddrStatus": alaQoSAppliedActionPermanentGatewayIpAddrStatus,
       "alaQoSAppliedActionAlternateGatewayIpAddr": alaQoSAppliedActionAlternateGatewayIpAddr,
       "alaQoSAppliedActionAlternateGatewayIpAddrStatus": alaQoSAppliedActionAlternateGatewayIpAddrStatus,
       "alaQoSAppliedActionRowStatus": alaQoSAppliedActionRowStatus,
       "alaQoSAppliedActionNocache": alaQoSAppliedActionNocache,
       "alaQoSAppliedActionPortdisable": alaQoSAppliedActionPortdisable,
       "alaQoSAppliedActionRedirectSlot": alaQoSAppliedActionRedirectSlot,
       "alaQoSAppliedActionRedirectSlotStatus": alaQoSAppliedActionRedirectSlotStatus,
       "alaQoSAppliedActionRedirectPort": alaQoSAppliedActionRedirectPort,
       "alaQoSAppliedActionRedirectAgg": alaQoSAppliedActionRedirectAgg,
       "alaQoSAppliedActionRedirectAggStatus": alaQoSAppliedActionRedirectAggStatus,
       "alaQoSAppliedActionMirrorSlot": alaQoSAppliedActionMirrorSlot,
       "alaQoSAppliedActionMirrorPort": alaQoSAppliedActionMirrorPort,
       "alaQoSAppliedActionMirrorMode": alaQoSAppliedActionMirrorMode,
       "alaQoSAppliedActionMirrorModeStatus": alaQoSAppliedActionMirrorModeStatus,
       "alaQoSAppliedActionCIR": alaQoSAppliedActionCIR,
       "alaQoSAppliedActionCIRStatus": alaQoSAppliedActionCIRStatus,
       "alaQoSAppliedActionCBS": alaQoSAppliedActionCBS,
       "alaQoSAppliedActionCBSStatus": alaQoSAppliedActionCBSStatus,
       "alaQoSAppliedActionPIR": alaQoSAppliedActionPIR,
       "alaQoSAppliedActionPIRStatus": alaQoSAppliedActionPIRStatus,
       "alaQoSAppliedActionPBS": alaQoSAppliedActionPBS,
       "alaQoSAppliedActionPBSStatus": alaQoSAppliedActionPBSStatus,
       "alaQoSAppliedActionCPUPriority": alaQoSAppliedActionCPUPriority,
       "alaQoSAppliedActionCPUPriorityStatus": alaQoSAppliedActionCPUPriorityStatus,
       "alaQoSAppliedActionColorOnly": alaQoSAppliedActionColorOnly,
       "alaQoSAppliedActionRedirectChassis": alaQoSAppliedActionRedirectChassis,
       "alaQoSAppliedActionMirrorChassis": alaQoSAppliedActionMirrorChassis,
       "alaQoSAppliedActionPermanentGatewayIpV6Addr": alaQoSAppliedActionPermanentGatewayIpV6Addr,
       "alaQoSAppliedActionPermanentGatewayIpV6AddrStatus": alaQoSAppliedActionPermanentGatewayIpV6AddrStatus,
       "alaQoSAppliedActionPermanentGatewayIpV6IfIndex": alaQoSAppliedActionPermanentGatewayIpV6IfIndex,
       "alaQoSAppliedActionRTCPMonitor": alaQoSAppliedActionRTCPMonitor,
       "alaQoSAppliedActionRTCPMonitorStatus": alaQoSAppliedActionRTCPMonitorStatus,
       "alaQoSAppliedActionRTCPDSCP": alaQoSAppliedActionRTCPDSCP,
       "alaQoSAppliedActionRTCPDSCPStatus": alaQoSAppliedActionRTCPDSCPStatus,
       "alaQoSAppliedActionTrustDSCP": alaQoSAppliedActionTrustDSCP,
       "alaQoSAppliedActionTrustDSCPStatus": alaQoSAppliedActionTrustDSCPStatus,
       "alaQoSPortTable": alaQoSPortTable,
       "alaQoSPortEntry": alaQoSPortEntry,
       "alaQoSPortSlot": alaQoSPortSlot,
       "alaQoSPortPort": alaQoSPortPort,
       "alaQoSPortInterfaceType": alaQoSPortInterfaceType,
       "alaQoSPortTrusted": alaQoSPortTrusted,
       "alaQoSPortDefault8021p": alaQoSPortDefault8021p,
       "alaQoSPortDefaultDSCP": alaQoSPortDefaultDSCP,
       "alaQoSPortMaximumDefaultDepth": alaQoSPortMaximumDefaultDepth,
       "alaQoSPortMaximumDefaultDepthStatus": alaQoSPortMaximumDefaultDepthStatus,
       "alaQoSPortReset": alaQoSPortReset,
       "alaQoSPortPhysicalBandwidth": alaQoSPortPhysicalBandwidth,
       "alaQoSPortRowStatus": alaQoSPortRowStatus,
       "alaQoSPortDefaultClassification": alaQoSPortDefaultClassification,
       "alaQoSPortMaximumBandwidth": alaQoSPortMaximumBandwidth,
       "alaQoSPortMaximumBandwidthStatus": alaQoSPortMaximumBandwidthStatus,
       "alaQoSPortMaximumIngBandwidth": alaQoSPortMaximumIngBandwidth,
       "alaQoSPortMaximumIngBandwidthStatus": alaQoSPortMaximumIngBandwidthStatus,
       "alaQoSPortMaximumIngressDepth": alaQoSPortMaximumIngressDepth,
       "alaQoSPortMaximumIngressDepthStatus": alaQoSPortMaximumIngressDepthStatus,
       "alaQoSPortDEIMarking": alaQoSPortDEIMarking,
       "alaQoSPortDEIMapping": alaQoSPortDEIMapping,
       "alaQoSConfig": alaQoSConfig,
       "alaQoSConfigEnabled": alaQoSConfigEnabled,
       "alaQoSConfigTrustPorts": alaQoSConfigTrustPorts,
       "alaQoSConfigStatsInterval": alaQoSConfigStatsInterval,
       "alaQoSConfigLogLines": alaQoSConfigLogLines,
       "alaQoSConfigLogLevel": alaQoSConfigLogLevel,
       "alaQoSConfigLogConsole": alaQoSConfigLogConsole,
       "alaQoSConfigForwardLog": alaQoSConfigForwardLog,
       "alaQoSConfigClearLog": alaQoSConfigClearLog,
       "alaQoSConfigApply": alaQoSConfigApply,
       "alaQoSConfigRevert": alaQoSConfigRevert,
       "alaQoSConfigReset": alaQoSConfigReset,
       "alaQoSConfigStatsReset": alaQoSConfigStatsReset,
       "alaQoSConfigFlush": alaQoSConfigFlush,
       "alaQoSConfigDebug": alaQoSConfigDebug,
       "alaQoSConfigUserportFilter": alaQoSConfigUserportFilter,
       "alaQoSConfigAppliedUserportFilter": alaQoSConfigAppliedUserportFilter,
       "alaQoSConfigUserportShutdown": alaQoSConfigUserportShutdown,
       "alaQoSConfigAppliedUserportShutdown": alaQoSConfigAppliedUserportShutdown,
       "alaQoSConfigAutoPhones": alaQoSConfigAutoPhones,
       "alaQoSConfigQMPage": alaQoSConfigQMPage,
       "alaQoSConfigQMMACGroup": alaQoSConfigQMMACGroup,
       "alaQoSConfigQMPath": alaQoSConfigQMPath,
       "alaQoSConfigDEIMapping": alaQoSConfigDEIMapping,
       "alaQoSConfigDEIMarking": alaQoSConfigDEIMarking,
       "alaQoSConfigSwitchGroup": alaQoSConfigSwitchGroup,
       "alaQoSVmSnooping": alaQoSVmSnooping,
       "alaQoSStats": alaQoSStats,
       "alaQoSStatsSpoofedEvents": alaQoSStatsSpoofedEvents,
       "alaQoSStatsNonSpoofedEvents": alaQoSStatsNonSpoofedEvents,
       "alaQoSValidityPeriodTable": alaQoSValidityPeriodTable,
       "alaQoSValidityPeriodEntry": alaQoSValidityPeriodEntry,
       "alaQoSValidityPeriodName": alaQoSValidityPeriodName,
       "alaQoSValidityPeriodSource": alaQoSValidityPeriodSource,
       "alaQoSValidityPeriodDays": alaQoSValidityPeriodDays,
       "alaQoSValidityPeriodDaysStatus": alaQoSValidityPeriodDaysStatus,
       "alaQoSValidityPeriodMonths": alaQoSValidityPeriodMonths,
       "alaQoSValidityPeriodMonthsStatus": alaQoSValidityPeriodMonthsStatus,
       "alaQoSValidityPeriodHour": alaQoSValidityPeriodHour,
       "alaQoSValidityPeriodHourStatus": alaQoSValidityPeriodHourStatus,
       "alaQoSValidityPeriodEndHour": alaQoSValidityPeriodEndHour,
       "alaQoSValidityPeriodInterval": alaQoSValidityPeriodInterval,
       "alaQoSValidityPeriodIntervalStatus": alaQoSValidityPeriodIntervalStatus,
       "alaQoSValidityPeriodEndInterval": alaQoSValidityPeriodEndInterval,
       "alaQoSValidityPeriodRowStatus": alaQoSValidityPeriodRowStatus,
       "alaQoSAppliedValidityPeriodTable": alaQoSAppliedValidityPeriodTable,
       "alaQoSAppliedValidityPeriodEntry": alaQoSAppliedValidityPeriodEntry,
       "alaQoSAppliedValidityPeriodName": alaQoSAppliedValidityPeriodName,
       "alaQoSAppliedValidityPeriodSource": alaQoSAppliedValidityPeriodSource,
       "alaQoSAppliedValidityPeriodDays": alaQoSAppliedValidityPeriodDays,
       "alaQoSAppliedValidityPeriodDaysStatus": alaQoSAppliedValidityPeriodDaysStatus,
       "alaQoSAppliedValidityPeriodMonths": alaQoSAppliedValidityPeriodMonths,
       "alaQoSAppliedValidityPeriodMonthsStatus": alaQoSAppliedValidityPeriodMonthsStatus,
       "alaQoSAppliedValidityPeriodHour": alaQoSAppliedValidityPeriodHour,
       "alaQoSAppliedValidityPeriodHourStatus": alaQoSAppliedValidityPeriodHourStatus,
       "alaQoSAppliedValidityPeriodEndHour": alaQoSAppliedValidityPeriodEndHour,
       "alaQoSAppliedValidityPeriodInterval": alaQoSAppliedValidityPeriodInterval,
       "alaQoSAppliedValidityPeriodIntervalStatus": alaQoSAppliedValidityPeriodIntervalStatus,
       "alaQoSAppliedValidityPeriodEndInterval": alaQoSAppliedValidityPeriodEndInterval,
       "alaQoSAppliedValidityPeriodRowStatus": alaQoSAppliedValidityPeriodRowStatus,
       "alaQoSRuleGroupsTable": alaQoSRuleGroupsTable,
       "alaQoSRuleGroupsEntry": alaQoSRuleGroupsEntry,
       "alaQoSRuleGroupsName": alaQoSRuleGroupsName,
       "alaQoSRuleGroupsSource": alaQoSRuleGroupsSource,
       "alaQoSRuleGroupsType": alaQoSRuleGroupsType,
       "alaQoSRuleGroupsEnabled": alaQoSRuleGroupsEnabled,
       "alaQoSRuleGroupsStatus": alaQoSRuleGroupsStatus,
       "alaQoSAppliedRuleGroupsTable": alaQoSAppliedRuleGroupsTable,
       "alaQoSAppliedRuleGroupsEntry": alaQoSAppliedRuleGroupsEntry,
       "alaQoSAppliedRuleGroupsName": alaQoSAppliedRuleGroupsName,
       "alaQoSAppliedRuleGroupsSource": alaQoSAppliedRuleGroupsSource,
       "alaQoSAppliedRuleGroupsType": alaQoSAppliedRuleGroupsType,
       "alaQoSAppliedRuleGroupsEnabled": alaQoSAppliedRuleGroupsEnabled,
       "alaQoSAppliedRuleGroupsStatus": alaQoSAppliedRuleGroupsStatus,
       "alaQoSRuleGroupTable": alaQoSRuleGroupTable,
       "alaQoSRuleGroupEntry": alaQoSRuleGroupEntry,
       "alaQoSRuleGroupRuleName": alaQoSRuleGroupRuleName,
       "alaQoSRuleGroupMatches": alaQoSRuleGroupMatches,
       "alaQoSRuleGroupCountType": alaQoSRuleGroupCountType,
       "alaQoSRuleGroupPacketCount": alaQoSRuleGroupPacketCount,
       "alaQoSRuleGroupByteCount": alaQoSRuleGroupByteCount,
       "alaQoSRuleGroupStatus": alaQoSRuleGroupStatus,
       "alaQoSAppliedRuleGroupTable": alaQoSAppliedRuleGroupTable,
       "alaQoSAppliedRuleGroupEntry": alaQoSAppliedRuleGroupEntry,
       "alaQoSAppliedRuleGroupRuleName": alaQoSAppliedRuleGroupRuleName,
       "alaQoSAppliedRuleGroupMatches": alaQoSAppliedRuleGroupMatches,
       "alaQoSAppliedRuleGroupCountType": alaQoSAppliedRuleGroupCountType,
       "alaQoSAppliedRuleGroupPacketCount": alaQoSAppliedRuleGroupPacketCount,
       "alaQoSAppliedRuleGroupByteCount": alaQoSAppliedRuleGroupByteCount,
       "alaQoSAppliedRuleGroupStatus": alaQoSAppliedRuleGroupStatus,
       "alaQoSV6NetworkGroupTable": alaQoSV6NetworkGroupTable,
       "alaQoSV6NetworkGroupEntry": alaQoSV6NetworkGroupEntry,
       "alaQoSV6NetworkGroupIpAddr": alaQoSV6NetworkGroupIpAddr,
       "alaQoSV6NetworkGroupIpMask": alaQoSV6NetworkGroupIpMask,
       "alaQoSV6NetworkGroupStatus": alaQoSV6NetworkGroupStatus,
       "alaQoSAppliedV6NetworkGroupTable": alaQoSAppliedV6NetworkGroupTable,
       "alaQoSAppliedV6NetworkGroupEntry": alaQoSAppliedV6NetworkGroupEntry,
       "alaQoSAppliedV6NetworkGroupIpAddr": alaQoSAppliedV6NetworkGroupIpAddr,
       "alaQoSAppliedV6NetworkGroupIpMask": alaQoSAppliedV6NetworkGroupIpMask,
       "alaQoSAppliedV6NetworkGroupStatus": alaQoSAppliedV6NetworkGroupStatus,
       "alaQoSDSCPTable": alaQoSDSCPTable,
       "alaQoSDSCPEntry": alaQoSDSCPEntry,
       "alaQoSDSCPEntryNumber": alaQoSDSCPEntryNumber,
       "alaQoSDSCPPriority": alaQoSDSCPPriority,
       "alaQoSDSCPDropPrecedence": alaQoSDSCPDropPrecedence,
       "alaQoSDSCPRowStatus": alaQoSDSCPRowStatus,
       "alaQoSAutoMacRangeTable": alaQoSAutoMacRangeTable,
       "alaQoSAutoMacRangeEntry": alaQoSAutoMacRangeEntry,
       "alaQoSAutoMacRangeIndex": alaQoSAutoMacRangeIndex,
       "alaQoSAutoMacRangeStart": alaQoSAutoMacRangeStart,
       "alaQoSAutoMacRangeEnd": alaQoSAutoMacRangeEnd,
       "alaQoSExtendedRuleTable": alaQoSExtendedRuleTable,
       "alaQoSExtendedRuleEntry": alaQoSExtendedRuleEntry,
       "alaQoSExtendedRuleSplitRuleID": alaQoSExtendedRuleSplitRuleID,
       "alaQoSExtendedRuleChassis": alaQoSExtendedRuleChassis,
       "alaQoSExtendedRuleSlot": alaQoSExtendedRuleSlot,
       "alaQoSExtendedRulePort": alaQoSExtendedRulePort,
       "alaQoSExtendedRulePacketCount": alaQoSExtendedRulePacketCount,
       "alaQoSExtendedRuleByteCount": alaQoSExtendedRuleByteCount,
       "alaQoSExtendedRuleGreenPacketCount": alaQoSExtendedRuleGreenPacketCount,
       "alaQoSExtendedRuleYellowPacketCount": alaQoSExtendedRuleYellowPacketCount,
       "alaQoSExtendedRuleRedPacketCount": alaQoSExtendedRuleRedPacketCount,
       "alaQoSExtendedRuleGreenByteCount": alaQoSExtendedRuleGreenByteCount,
       "alaQoSExtendedRuleYellowByteCount": alaQoSExtendedRuleYellowByteCount,
       "alaQoSExtendedRuleRedByteCount": alaQoSExtendedRuleRedByteCount,
       "alaQoSIpNetworkSummaryTable": alaQoSIpNetworkSummaryTable,
       "alaQoSIpNetworkSummaryEntry": alaQoSIpNetworkSummaryEntry,
       "alaQoSIpNetworkSummaryProtocol": alaQoSIpNetworkSummaryProtocol,
       "alaQoSIpNetworkSummarySourceIpAddressType": alaQoSIpNetworkSummarySourceIpAddressType,
       "alaQoSIpNetworkSummarySourceIpAddress": alaQoSIpNetworkSummarySourceIpAddress,
       "alaQoSIpNetworkSummaryDestinationIpAddressType": alaQoSIpNetworkSummaryDestinationIpAddressType,
       "alaQoSIpNetworkSummaryDestinationIpAddress": alaQoSIpNetworkSummaryDestinationIpAddress,
       "alaQoSIpNetworkSummarySourceGroup": alaQoSIpNetworkSummarySourceGroup,
       "alaQoSIpNetworkSummaryDestinationGroup": alaQoSIpNetworkSummaryDestinationGroup,
       "alaQoSIpNetworkSummaryVrfName": alaQoSIpNetworkSummaryVrfName,
       "alaQoSIpNetworkSummaryAction": alaQoSIpNetworkSummaryAction,
       "alaQoSIpNetworkSummaryHitCount": alaQoSIpNetworkSummaryHitCount,
       "alaQoSMIBConformance": alaQoSMIBConformance,
       "alaQoSMIBGroups": alaQoSMIBGroups,
       "alaQoSMIBRuleObjects": alaQoSMIBRuleObjects,
       "alaQoSMIBAppliedRuleObjects": alaQoSMIBAppliedRuleObjects,
       "alaQoSMIBConditionObjects": alaQoSMIBConditionObjects,
       "alaQoSMIBAppliedConditionObjects": alaQoSMIBAppliedConditionObjects,
       "alaQoSMIBServiceObjects": alaQoSMIBServiceObjects,
       "alaQoSMIBAppliedServiceObjects": alaQoSMIBAppliedServiceObjects,
       "alaQoSMIBServiceGroupsObjects": alaQoSMIBServiceGroupsObjects,
       "alaQoSMIBAppliedServiceGroupsObjects": alaQoSMIBAppliedServiceGroupsObjects,
       "alaQoSMIBServiceGroupObjects": alaQoSMIBServiceGroupObjects,
       "alaQoSMIBAppliedServiceGroupObjects": alaQoSMIBAppliedServiceGroupObjects,
       "alaQoSMIBNetworkGroupsObjects": alaQoSMIBNetworkGroupsObjects,
       "alaQoSMIBAppliedNetworkGroupsObjects": alaQoSMIBAppliedNetworkGroupsObjects,
       "alaQoSMIBNetworkGroupObjects": alaQoSMIBNetworkGroupObjects,
       "alaQoSMIBAppliedNetworkGroupObjects": alaQoSMIBAppliedNetworkGroupObjects,
       "alaQoSMIBMACGroupsObjects": alaQoSMIBMACGroupsObjects,
       "alaQoSMIBAppliedMACGroupsObjects": alaQoSMIBAppliedMACGroupsObjects,
       "alaQoSMIBMACGroupObjects": alaQoSMIBMACGroupObjects,
       "alaQoSMIBAppliedMACGroupObjects": alaQoSMIBAppliedMACGroupObjects,
       "alaQoSMIBPortGroupsObjects": alaQoSMIBPortGroupsObjects,
       "alaQoSMIBAppliedPortGroupsObjects": alaQoSMIBAppliedPortGroupsObjects,
       "alaQoSMIBPortGroupObjects": alaQoSMIBPortGroupObjects,
       "alaQoSMIBAppliedPortGroupObjects": alaQoSMIBAppliedPortGroupObjects,
       "alaQoSMIBMapGroupsObjects": alaQoSMIBMapGroupsObjects,
       "alaQoSMIBAppliedMapGroupsObjects": alaQoSMIBAppliedMapGroupsObjects,
       "alaQoSMIBMapGroupObjects": alaQoSMIBMapGroupObjects,
       "alaQoSMIBAppliedMapGroupObjects": alaQoSMIBAppliedMapGroupObjects,
       "alaQoSMIBActionObjects": alaQoSMIBActionObjects,
       "alaQoSMIBAppliedActionObjects": alaQoSMIBAppliedActionObjects,
       "alaQoSMIBPortObjects": alaQoSMIBPortObjects,
       "alaQoSMIBConfigObjects": alaQoSMIBConfigObjects,
       "alaQoSMIBStatsObjects": alaQoSMIBStatsObjects,
       "alaQoSMIBRuleGroupsObjects": alaQoSMIBRuleGroupsObjects,
       "alaQoSMIBAppliedRuleGroupsObjects": alaQoSMIBAppliedRuleGroupsObjects,
       "alaQoSMIBRuleGroupObjects": alaQoSMIBRuleGroupObjects,
       "alaQoSMIBAppliedRuleGroupObjects": alaQoSMIBAppliedRuleGroupObjects,
       "alaQoSMIBValidityPeriodObjects": alaQoSMIBValidityPeriodObjects,
       "alaQoSMIBAppliedValidityPeriodObjects": alaQoSMIBAppliedValidityPeriodObjects,
       "alaQoSMIBDSCPGroupObjects": alaQoSMIBDSCPGroupObjects,
       "alaQoSMIBAutoMacRangeGroupObjects": alaQoSMIBAutoMacRangeGroupObjects,
       "alaQoSMIBV6NetworkGroupObjects": alaQoSMIBV6NetworkGroupObjects,
       "alaQoSMIBAppliedV6NetworkGroupObjects": alaQoSMIBAppliedV6NetworkGroupObjects,
       "alaQoSRuleExtendedObjects": alaQoSRuleExtendedObjects,
       "alaQoSIpNetworkSummaryGroupObjects": alaQoSIpNetworkSummaryGroupObjects,
       "alaQoSMIBCompliances": alaQoSMIBCompliances,
       "alaQoSMIBCompliance": alaQoSMIBCompliance}
)
