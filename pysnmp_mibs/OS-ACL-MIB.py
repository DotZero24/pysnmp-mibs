# SNMP MIB module (OS-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OS-ACL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:22 2025
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

(oaOptiSwitch,) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "oaOptiSwitch")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

osAcl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3)
)
if mibBuilder.loadTexts:
    osAcl.setRevisions(
        ("2014-05-27 00:00",
         "2008-01-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SupportValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )



class AdminStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("valid", 2),
          ("invalid", 3))
    )



class ParamType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("integer", 2),
          ("octetString", 3),
          ("displayString", 4),
          ("noParam", 5))
    )



class ConditionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("eq", 2),
          ("neq", 3),
          ("lt", 4),
          ("gt", 5),
          ("le", 6),
          ("ge", 7),
          ("mask", 8),
          ("none", 9))
    )



class VlanIdOrNone(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
        ValueRangeConstraint(5000, 5000),
    )



class PortIndexOrNone(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4999),
        ValueRangeConstraint(5000, 5000),
    )



# MIB Managed Objects in the order of their OIDs

_OsAclTable_Object = MibTable
osAclTable = _OsAclTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 1)
)
if mibBuilder.loadTexts:
    osAclTable.setStatus("current")
_OsAclEntry_Object = MibTableRow
osAclEntry = _OsAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 1, 1)
)
osAclEntry.setIndexNames(
    (0, "OS-ACL-MIB", "osAclName"),
)
if mibBuilder.loadTexts:
    osAclEntry.setStatus("current")


class _OsAclName_Type(DisplayString):
    """Custom type osAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_OsAclName_Type.__name__ = "DisplayString"
_OsAclName_Object = MibTableColumn
osAclName = _OsAclName_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 1, 1, 1),
    _OsAclName_Type()
)
osAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osAclName.setStatus("current")


class _OsAclType_Type(Integer32):
    """Custom type osAclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("extended", 2),
          ("flow", 3),
          ("protocols", 4))
    )


_OsAclType_Type.__name__ = "Integer32"
_OsAclType_Object = MibTableColumn
osAclType = _OsAclType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 1, 1, 2),
    _OsAclType_Type()
)
osAclType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osAclType.setStatus("current")


class _OsAclDefaultPolicy_Type(Integer32):
    """Custom type osAclDefaultPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 3),
          ("notSupported", 4))
    )


_OsAclDefaultPolicy_Type.__name__ = "Integer32"
_OsAclDefaultPolicy_Object = MibTableColumn
osAclDefaultPolicy = _OsAclDefaultPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 1, 1, 3),
    _OsAclDefaultPolicy_Type()
)
osAclDefaultPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osAclDefaultPolicy.setStatus("current")
_OsAclRemark_Type = DisplayString
_OsAclRemark_Object = MibTableColumn
osAclRemark = _OsAclRemark_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 1, 1, 4),
    _OsAclRemark_Type()
)
osAclRemark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osAclRemark.setStatus("current")


class _OsAclActive_Type(Integer32):
    """Custom type osAclActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_OsAclActive_Type.__name__ = "Integer32"
_OsAclActive_Object = MibTableColumn
osAclActive = _OsAclActive_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 1, 1, 5),
    _OsAclActive_Type()
)
osAclActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osAclActive.setStatus("current")
_OsAclAdminStatus_Type = AdminStatus
_OsAclAdminStatus_Object = MibTableColumn
osAclAdminStatus = _OsAclAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 1, 1, 6),
    _OsAclAdminStatus_Type()
)
osAclAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osAclAdminStatus.setStatus("current")
_OsAclRuleTable_Object = MibTable
osAclRuleTable = _OsAclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 2)
)
if mibBuilder.loadTexts:
    osAclRuleTable.setStatus("current")
_OsAclRuleEntry_Object = MibTableRow
osAclRuleEntry = _OsAclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 2, 1)
)
osAclRuleEntry.setIndexNames(
    (0, "OS-ACL-MIB", "osAclName"),
    (0, "OS-ACL-MIB", "osAclRuleIndex"),
)
if mibBuilder.loadTexts:
    osAclRuleEntry.setStatus("current")


class _OsAclRuleIndex_Type(Integer32):
    """Custom type osAclRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OsAclRuleIndex_Type.__name__ = "Integer32"
_OsAclRuleIndex_Object = MibTableColumn
osAclRuleIndex = _OsAclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 2, 1, 1),
    _OsAclRuleIndex_Type()
)
osAclRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osAclRuleIndex.setStatus("current")


class _OsAclRuleAdminStatus_Type(Integer32):
    """Custom type osAclRuleAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("disable", 3),
          ("invalid", 4))
    )


_OsAclRuleAdminStatus_Type.__name__ = "Integer32"
_OsAclRuleAdminStatus_Object = MibTableColumn
osAclRuleAdminStatus = _OsAclRuleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 2, 1, 2),
    _OsAclRuleAdminStatus_Type()
)
osAclRuleAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osAclRuleAdminStatus.setStatus("current")
_OsAclRuleActionTable_Object = MibTable
osAclRuleActionTable = _OsAclRuleActionTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 3)
)
if mibBuilder.loadTexts:
    osAclRuleActionTable.setStatus("current")
_OsAclRuleActionEntry_Object = MibTableRow
osAclRuleActionEntry = _OsAclRuleActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 3, 1)
)
osAclRuleActionEntry.setIndexNames(
    (0, "OS-ACL-MIB", "osAclName"),
    (0, "OS-ACL-MIB", "osAclRuleIndex"),
    (0, "OS-ACL-MIB", "osAclRuleActionType"),
)
if mibBuilder.loadTexts:
    osAclRuleActionEntry.setStatus("current")


class _OsAclRuleActionType_Type(Integer32):
    """Custom type osAclRuleActionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("osAclRuleActionDeny", 2),
          ("osAclRuleActionPermit", 3),
          ("osAclRuleActionLayer2Loopback", 4),
          ("osAclRuleActionTrapToCpu", 5),
          ("osAclRuleActionMirrorToCpu", 6),
          ("osAclRuleActionMirrorToAnalyser", 7),
          ("osAclRuleActionRedirectPort", 8),
          ("osAclRuleActionRedirectTag", 9),
          ("osAclRuleActionWithActionList", 10),
          ("osAclRuleActionMarkServiceLevel", 11),
          ("osAclRuleActionMarkDscp", 12),
          ("osAclRuleActionMarkVpt", 13),
          ("osAclRuleActionMarkByDiffserv", 14),
          ("osAclRuleActionMarkSlByDscp", 15),
          ("osAclRuleActionSwapVlan", 16),
          ("osAclRuleActionNestedVlan", 17),
          ("osAclRuleActionSwapToClientTag", 18),
          ("osAclRuleActionSwapToServerTag", 19),
          ("osAclRuleActionRedirectToCpu", 20))
    )


_OsAclRuleActionType_Type.__name__ = "Integer32"
_OsAclRuleActionType_Object = MibTableColumn
osAclRuleActionType = _OsAclRuleActionType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 3, 1, 1),
    _OsAclRuleActionType_Type()
)
osAclRuleActionType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osAclRuleActionType.setStatus("current")
_OsAclRuleActionParamType_Type = ParamType
_OsAclRuleActionParamType_Object = MibTableColumn
osAclRuleActionParamType = _OsAclRuleActionParamType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 3, 1, 2),
    _OsAclRuleActionParamType_Type()
)
osAclRuleActionParamType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osAclRuleActionParamType.setStatus("current")


class _OsAclRuleActionParamValue_Type(OctetString):
    """Custom type osAclRuleActionParamValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OsAclRuleActionParamValue_Type.__name__ = "OctetString"
_OsAclRuleActionParamValue_Object = MibTableColumn
osAclRuleActionParamValue = _OsAclRuleActionParamValue_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 3, 1, 3),
    _OsAclRuleActionParamValue_Type()
)
osAclRuleActionParamValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osAclRuleActionParamValue.setStatus("current")
_OsAclRuleActionAdminStatus_Type = AdminStatus
_OsAclRuleActionAdminStatus_Object = MibTableColumn
osAclRuleActionAdminStatus = _OsAclRuleActionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 3, 1, 4),
    _OsAclRuleActionAdminStatus_Type()
)
osAclRuleActionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osAclRuleActionAdminStatus.setStatus("current")
_OsAclRuleClassTable_Object = MibTable
osAclRuleClassTable = _OsAclRuleClassTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 4)
)
if mibBuilder.loadTexts:
    osAclRuleClassTable.setStatus("current")
_OsAclRuleClassEntry_Object = MibTableRow
osAclRuleClassEntry = _OsAclRuleClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 4, 1)
)
osAclRuleClassEntry.setIndexNames(
    (0, "OS-ACL-MIB", "osAclName"),
    (0, "OS-ACL-MIB", "osAclRuleIndex"),
    (0, "OS-ACL-MIB", "osAclRuleClassType"),
    (0, "OS-ACL-MIB", "osAclRuleClassCondition"),
)
if mibBuilder.loadTexts:
    osAclRuleClassEntry.setStatus("current")


class _OsAclRuleClassType_Type(Integer32):
    """Custom type osAclRuleClassType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("osAclRuleClassSrcIp", 2),
          ("osAclRuleClassDestIp", 3),
          ("osAclRuleClassSrcPort", 4),
          ("osAclRuleClassDestPort", 5),
          ("osAclRuleClassProtocol", 6),
          ("osAclRuleClassMacLookupResults", 7),
          ("osAclRuleClassMacDaType", 8),
          ("osAclRuleClassVpt", 9),
          ("osAclRuleClassClientVpt", 10),
          ("osAclRuleClassDscp", 11),
          ("osAclRuleClassMplsExp", 12),
          ("osAclRuleClassMplsExpTagged", 13),
          ("osAclRuleClassTag", 14),
          ("osAclRuleClassClientTag", 15),
          ("osAclRuleClassEthertype", 16),
          ("osAclRuleClassClientEthertype", 17),
          ("osAclRuleClassSrcMac", 18),
          ("osAclRuleClassDestMac", 19),
          ("osAclRuleClassSrcPhyPort", 20),
          ("osAclRuleClassArp", 21),
          ("osAclRuleClassTaggedArp", 22))
    )


_OsAclRuleClassType_Type.__name__ = "Integer32"
_OsAclRuleClassType_Object = MibTableColumn
osAclRuleClassType = _OsAclRuleClassType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 4, 1, 1),
    _OsAclRuleClassType_Type()
)
osAclRuleClassType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osAclRuleClassType.setStatus("current")
_OsAclRuleClassCondition_Type = ConditionType
_OsAclRuleClassCondition_Object = MibTableColumn
osAclRuleClassCondition = _OsAclRuleClassCondition_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 4, 1, 2),
    _OsAclRuleClassCondition_Type()
)
osAclRuleClassCondition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osAclRuleClassCondition.setStatus("current")
_OsAclRuleClassParamType_Type = ParamType
_OsAclRuleClassParamType_Object = MibTableColumn
osAclRuleClassParamType = _OsAclRuleClassParamType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 4, 1, 3),
    _OsAclRuleClassParamType_Type()
)
osAclRuleClassParamType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osAclRuleClassParamType.setStatus("current")


class _OsAclRuleClassParamValue_Type(OctetString):
    """Custom type osAclRuleClassParamValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OsAclRuleClassParamValue_Type.__name__ = "OctetString"
_OsAclRuleClassParamValue_Object = MibTableColumn
osAclRuleClassParamValue = _OsAclRuleClassParamValue_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 4, 1, 4),
    _OsAclRuleClassParamValue_Type()
)
osAclRuleClassParamValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osAclRuleClassParamValue.setStatus("current")
_OsAclRuleClassAdminStatus_Type = AdminStatus
_OsAclRuleClassAdminStatus_Object = MibTableColumn
osAclRuleClassAdminStatus = _OsAclRuleClassAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 4, 1, 5),
    _OsAclRuleClassAdminStatus_Type()
)
osAclRuleClassAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osAclRuleClassAdminStatus.setStatus("current")
_OsAclBindingTable_Object = MibTable
osAclBindingTable = _OsAclBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 5)
)
if mibBuilder.loadTexts:
    osAclBindingTable.setStatus("current")
_OsAclBindingEntry_Object = MibTableRow
osAclBindingEntry = _OsAclBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 5, 1)
)
osAclBindingEntry.setIndexNames(
    (0, "OS-ACL-MIB", "osAclBindingPort"),
    (0, "OS-ACL-MIB", "osAclBindingTag"),
)
if mibBuilder.loadTexts:
    osAclBindingEntry.setStatus("current")
_OsAclBindingPort_Type = PortIndexOrNone
_OsAclBindingPort_Object = MibTableColumn
osAclBindingPort = _OsAclBindingPort_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 5, 1, 1),
    _OsAclBindingPort_Type()
)
osAclBindingPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osAclBindingPort.setStatus("current")
_OsAclBindingTag_Type = VlanIdOrNone
_OsAclBindingTag_Object = MibTableColumn
osAclBindingTag = _OsAclBindingTag_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 5, 1, 2),
    _OsAclBindingTag_Type()
)
osAclBindingTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osAclBindingTag.setStatus("current")


class _OsAclBindingAclName_Type(DisplayString):
    """Custom type osAclBindingAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_OsAclBindingAclName_Type.__name__ = "DisplayString"
_OsAclBindingAclName_Object = MibTableColumn
osAclBindingAclName = _OsAclBindingAclName_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 5, 1, 3),
    _OsAclBindingAclName_Type()
)
osAclBindingAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osAclBindingAclName.setStatus("current")
_OsAclBindingAdminStatus_Type = AdminStatus
_OsAclBindingAdminStatus_Object = MibTableColumn
osAclBindingAdminStatus = _OsAclBindingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 5, 1, 4),
    _OsAclBindingAdminStatus_Type()
)
osAclBindingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osAclBindingAdminStatus.setStatus("current")
_OsAclMatchingCounterTable_Object = MibTable
osAclMatchingCounterTable = _OsAclMatchingCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 6)
)
if mibBuilder.loadTexts:
    osAclMatchingCounterTable.setStatus("current")
_OsAclMatchingCounterEntry_Object = MibTableRow
osAclMatchingCounterEntry = _OsAclMatchingCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 6, 1)
)
osAclMatchingCounterEntry.setIndexNames(
    (0, "OS-ACL-MIB", "osAclMatchingCounterIndex"),
)
if mibBuilder.loadTexts:
    osAclMatchingCounterEntry.setStatus("current")


class _OsAclMatchingCounterIndex_Type(Integer32):
    """Custom type osAclMatchingCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_OsAclMatchingCounterIndex_Type.__name__ = "Integer32"
_OsAclMatchingCounterIndex_Object = MibTableColumn
osAclMatchingCounterIndex = _OsAclMatchingCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 6, 1, 1),
    _OsAclMatchingCounterIndex_Type()
)
osAclMatchingCounterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osAclMatchingCounterIndex.setStatus("current")
_OsAclMatchingCounterPackets_Type = Counter64
_OsAclMatchingCounterPackets_Object = MibTableColumn
osAclMatchingCounterPackets = _OsAclMatchingCounterPackets_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 6, 1, 2),
    _OsAclMatchingCounterPackets_Type()
)
osAclMatchingCounterPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osAclMatchingCounterPackets.setStatus("current")
_OsAclMatchingCounterBytes_Type = Counter64
_OsAclMatchingCounterBytes_Object = MibTableColumn
osAclMatchingCounterBytes = _OsAclMatchingCounterBytes_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 6, 1, 3),
    _OsAclMatchingCounterBytes_Type()
)
osAclMatchingCounterBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osAclMatchingCounterBytes.setStatus("current")


class _OsAclMatchingCounterAdminStatus_Type(Integer32):
    """Custom type osAclMatchingCounterAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 1),
          ("clear", 2))
    )


_OsAclMatchingCounterAdminStatus_Type.__name__ = "Integer32"
_OsAclMatchingCounterAdminStatus_Object = MibTableColumn
osAclMatchingCounterAdminStatus = _OsAclMatchingCounterAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 6, 1, 98),
    _OsAclMatchingCounterAdminStatus_Type()
)
osAclMatchingCounterAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osAclMatchingCounterAdminStatus.setStatus("current")


class _OsAclMatchingCounterOperStatus_Type(Integer32):
    """Custom type osAclMatchingCounterOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_OsAclMatchingCounterOperStatus_Type.__name__ = "Integer32"
_OsAclMatchingCounterOperStatus_Object = MibTableColumn
osAclMatchingCounterOperStatus = _OsAclMatchingCounterOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 6, 1, 99),
    _OsAclMatchingCounterOperStatus_Type()
)
osAclMatchingCounterOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osAclMatchingCounterOperStatus.setStatus("current")
_OsAclGenConfGrp_ObjectIdentity = ObjectIdentity
osAclGenConfGrp = _OsAclGenConfGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 50)
)


class _OsAclGenConfExtendedProfile_Type(Integer32):
    """Custom type osAclGenConfExtendedProfile based on Integer32"""
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
        *(("notSupported", 0),
          ("normal", 1),
          ("doubleTag", 2),
          ("mplsExp", 3))
    )


_OsAclGenConfExtendedProfile_Type.__name__ = "Integer32"
_OsAclGenConfExtendedProfile_Object = MibScalar
osAclGenConfExtendedProfile = _OsAclGenConfExtendedProfile_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 50, 5),
    _OsAclGenConfExtendedProfile_Type()
)
osAclGenConfExtendedProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osAclGenConfExtendedProfile.setStatus("current")
_OsAclSupportGrp_ObjectIdentity = ObjectIdentity
osAclSupportGrp = _OsAclSupportGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 100)
)
_OsAclMibSupport_Type = SupportValue
_OsAclMibSupport_Object = MibScalar
osAclMibSupport = _OsAclMibSupport_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 100, 1),
    _OsAclMibSupport_Type()
)
osAclMibSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osAclMibSupport.setStatus("current")
_OsAclConformance_ObjectIdentity = ObjectIdentity
osAclConformance = _OsAclConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 101)
)
_OsAclMIBCompliances_ObjectIdentity = ObjectIdentity
osAclMIBCompliances = _OsAclMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 101, 1)
)
_OsAclMIBGroups_ObjectIdentity = ObjectIdentity
osAclMIBGroups = _OsAclMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 101, 2)
)

# Managed Objects groups

osAclMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 101, 2, 1)
)
osAclMandatoryGroup.setObjects(
      *(("OS-ACL-MIB", "osAclType"),
        ("OS-ACL-MIB", "osAclDefaultPolicy"),
        ("OS-ACL-MIB", "osAclRemark"),
        ("OS-ACL-MIB", "osAclActive"),
        ("OS-ACL-MIB", "osAclAdminStatus"),
        ("OS-ACL-MIB", "osAclRuleAdminStatus"),
        ("OS-ACL-MIB", "osAclRuleActionParamType"),
        ("OS-ACL-MIB", "osAclRuleActionParamValue"),
        ("OS-ACL-MIB", "osAclRuleActionAdminStatus"),
        ("OS-ACL-MIB", "osAclRuleClassParamType"),
        ("OS-ACL-MIB", "osAclRuleClassParamValue"),
        ("OS-ACL-MIB", "osAclRuleClassAdminStatus"),
        ("OS-ACL-MIB", "osAclBindingAclName"),
        ("OS-ACL-MIB", "osAclBindingAdminStatus"),
        ("OS-ACL-MIB", "osAclMatchingCounterPackets"),
        ("OS-ACL-MIB", "osAclMatchingCounterBytes"),
        ("OS-ACL-MIB", "osAclMatchingCounterAdminStatus"),
        ("OS-ACL-MIB", "osAclMatchingCounterOperStatus"),
        ("OS-ACL-MIB", "osAclMibSupport"),
        ("OS-ACL-MIB", "osAclGenConfExtendedProfile"))
)
if mibBuilder.loadTexts:
    osAclMandatoryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

osAclMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 2, 3, 101, 1, 1)
)
osAclMIBCompliance.setObjects(
    ("OS-ACL-MIB", "osAclMandatoryGroup")
)
if mibBuilder.loadTexts:
    osAclMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OS-ACL-MIB",
    **{"SupportValue": SupportValue,
       "AdminStatus": AdminStatus,
       "ParamType": ParamType,
       "ConditionType": ConditionType,
       "VlanIdOrNone": VlanIdOrNone,
       "PortIndexOrNone": PortIndexOrNone,
       "osAcl": osAcl,
       "osAclTable": osAclTable,
       "osAclEntry": osAclEntry,
       "osAclName": osAclName,
       "osAclType": osAclType,
       "osAclDefaultPolicy": osAclDefaultPolicy,
       "osAclRemark": osAclRemark,
       "osAclActive": osAclActive,
       "osAclAdminStatus": osAclAdminStatus,
       "osAclRuleTable": osAclRuleTable,
       "osAclRuleEntry": osAclRuleEntry,
       "osAclRuleIndex": osAclRuleIndex,
       "osAclRuleAdminStatus": osAclRuleAdminStatus,
       "osAclRuleActionTable": osAclRuleActionTable,
       "osAclRuleActionEntry": osAclRuleActionEntry,
       "osAclRuleActionType": osAclRuleActionType,
       "osAclRuleActionParamType": osAclRuleActionParamType,
       "osAclRuleActionParamValue": osAclRuleActionParamValue,
       "osAclRuleActionAdminStatus": osAclRuleActionAdminStatus,
       "osAclRuleClassTable": osAclRuleClassTable,
       "osAclRuleClassEntry": osAclRuleClassEntry,
       "osAclRuleClassType": osAclRuleClassType,
       "osAclRuleClassCondition": osAclRuleClassCondition,
       "osAclRuleClassParamType": osAclRuleClassParamType,
       "osAclRuleClassParamValue": osAclRuleClassParamValue,
       "osAclRuleClassAdminStatus": osAclRuleClassAdminStatus,
       "osAclBindingTable": osAclBindingTable,
       "osAclBindingEntry": osAclBindingEntry,
       "osAclBindingPort": osAclBindingPort,
       "osAclBindingTag": osAclBindingTag,
       "osAclBindingAclName": osAclBindingAclName,
       "osAclBindingAdminStatus": osAclBindingAdminStatus,
       "osAclMatchingCounterTable": osAclMatchingCounterTable,
       "osAclMatchingCounterEntry": osAclMatchingCounterEntry,
       "osAclMatchingCounterIndex": osAclMatchingCounterIndex,
       "osAclMatchingCounterPackets": osAclMatchingCounterPackets,
       "osAclMatchingCounterBytes": osAclMatchingCounterBytes,
       "osAclMatchingCounterAdminStatus": osAclMatchingCounterAdminStatus,
       "osAclMatchingCounterOperStatus": osAclMatchingCounterOperStatus,
       "osAclGenConfGrp": osAclGenConfGrp,
       "osAclGenConfExtendedProfile": osAclGenConfExtendedProfile,
       "osAclSupportGrp": osAclSupportGrp,
       "osAclMibSupport": osAclMibSupport,
       "osAclConformance": osAclConformance,
       "osAclMIBCompliances": osAclMIBCompliances,
       "osAclMIBCompliance": osAclMIBCompliance,
       "osAclMIBGroups": osAclMIBGroups,
       "osAclMandatoryGroup": osAclMandatoryGroup}
)
