# SNMP MIB module (POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/avaya/POLICY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:04:42 2025
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

(lannet,) = mibBuilder.importSymbols(
    "GEN-MIB",
    "lannet")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ipPolicyMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 81, 36)
)
if mibBuilder.loadTexts:
    ipPolicyMgmt.setRevisions(
        ("2006-09-05 13:58",
         "2005-11-17 11:49",
         "2005-04-25 11:34",
         "2005-04-13 16:19",
         "2005-03-15 18:28",
         "2004-10-19 16:53",
         "2005-02-09 12:19",
         "2004-09-23 13:33",
         "2003-06-29 09:58",
         "2003-06-25 21:19",
         "2003-06-18 11:58",
         "2003-06-18 10:56",
         "2003-06-16 19:27",
         "2003-06-03 10:36",
         "2003-05-05 15:25",
         "2003-05-01 10:16",
         "2002-07-21 12:33",
         "2001-12-06 10:17",
         "2003-05-28 17:24",
         "2003-10-27 14:57",
         "2003-12-01 10:08")
    )


# Types definitions



class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("notReady", 3),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )





class SubContextTypes(Integer32):
    """Custom type SubContextTypes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2))
    )




# TEXTUAL-CONVENTIONS



class TruthValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )



# MIB Managed Objects in the order of their OIDs

_IpPolicyListTable_Object = MibTable
ipPolicyListTable = _IpPolicyListTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1)
)
if mibBuilder.loadTexts:
    ipPolicyListTable.setStatus("current")
_IpPolicyListEntry_Object = MibTableRow
ipPolicyListEntry = _IpPolicyListEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1)
)
ipPolicyListEntry.setIndexNames(
    (0, "POLICY-MIB", "ipPolicyListSlot"),
    (0, "POLICY-MIB", "ipPolicyListID"),
)
if mibBuilder.loadTexts:
    ipPolicyListEntry.setStatus("current")


class _IpPolicyListSlot_Type(Integer32):
    """Custom type ipPolicyListSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyListSlot_Type.__name__ = "Integer32"
_IpPolicyListSlot_Object = MibTableColumn
ipPolicyListSlot = _IpPolicyListSlot_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 1),
    _IpPolicyListSlot_Type()
)
ipPolicyListSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyListSlot.setStatus("current")


class _IpPolicyListID_Type(Integer32):
    """Custom type ipPolicyListID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyListID_Type.__name__ = "Integer32"
_IpPolicyListID_Object = MibTableColumn
ipPolicyListID = _IpPolicyListID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 2),
    _IpPolicyListID_Type()
)
ipPolicyListID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyListID.setStatus("current")


class _IpPolicyListName_Type(DisplayString):
    """Custom type ipPolicyListName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IpPolicyListName_Type.__name__ = "DisplayString"
_IpPolicyListName_Object = MibTableColumn
ipPolicyListName = _IpPolicyListName_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 3),
    _IpPolicyListName_Type()
)
ipPolicyListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyListName.setStatus("current")


class _IpPolicyListValidityStatus_Type(Integer32):
    """Custom type ipPolicyListValidityStatus based on Integer32"""
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
        *(("valid", 1),
          ("partiallyValid", 2),
          ("invalid", 3),
          ("validationInProgress", 4))
    )


_IpPolicyListValidityStatus_Type.__name__ = "Integer32"
_IpPolicyListValidityStatus_Object = MibTableColumn
ipPolicyListValidityStatus = _IpPolicyListValidityStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 4),
    _IpPolicyListValidityStatus_Type()
)
ipPolicyListValidityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyListValidityStatus.setStatus("obsolete")
_IpPolicyListChecksum_Type = Integer32
_IpPolicyListChecksum_Object = MibTableColumn
ipPolicyListChecksum = _IpPolicyListChecksum_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 5),
    _IpPolicyListChecksum_Type()
)
ipPolicyListChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyListChecksum.setStatus("obsolete")
_IpPolicyListRowStatus_Type = RowStatus
_IpPolicyListRowStatus_Object = MibTableColumn
ipPolicyListRowStatus = _IpPolicyListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 6),
    _IpPolicyListRowStatus_Type()
)
ipPolicyListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyListRowStatus.setStatus("current")


class _IpPolicyListDefaultOperation_Type(Integer32):
    """Custom type ipPolicyListDefaultOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_IpPolicyListDefaultOperation_Type.__name__ = "Integer32"
_IpPolicyListDefaultOperation_Object = MibTableColumn
ipPolicyListDefaultOperation = _IpPolicyListDefaultOperation_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 7),
    _IpPolicyListDefaultOperation_Type()
)
ipPolicyListDefaultOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyListDefaultOperation.setStatus("current")


class _IpPolicyListCookie_Type(Integer32):
    """Custom type ipPolicyListCookie based on Integer32"""
    defaultValue = 0


_IpPolicyListCookie_Type.__name__ = "Integer32"
_IpPolicyListCookie_Object = MibTableColumn
ipPolicyListCookie = _IpPolicyListCookie_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 8),
    _IpPolicyListCookie_Type()
)
ipPolicyListCookie.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyListCookie.setStatus("current")


class _IpPolicyListTrackChanges_Type(Integer32):
    """Custom type ipPolicyListTrackChanges based on Integer32"""
    defaultValue = 0


_IpPolicyListTrackChanges_Type.__name__ = "Integer32"
_IpPolicyListTrackChanges_Object = MibTableColumn
ipPolicyListTrackChanges = _IpPolicyListTrackChanges_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 9),
    _IpPolicyListTrackChanges_Type()
)
ipPolicyListTrackChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyListTrackChanges.setStatus("current")


class _IpPolicyListOwner_Type(DisplayString):
    """Custom type ipPolicyListOwner based on DisplayString"""
    defaultValue = OctetString("other")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IpPolicyListOwner_Type.__name__ = "DisplayString"
_IpPolicyListOwner_Object = MibTableColumn
ipPolicyListOwner = _IpPolicyListOwner_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 10),
    _IpPolicyListOwner_Type()
)
ipPolicyListOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyListOwner.setStatus("current")


class _IpPolicyListErrMsg_Type(DisplayString):
    """Custom type ipPolicyListErrMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IpPolicyListErrMsg_Type.__name__ = "DisplayString"
_IpPolicyListErrMsg_Object = MibTableColumn
ipPolicyListErrMsg = _IpPolicyListErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 11),
    _IpPolicyListErrMsg_Type()
)
ipPolicyListErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyListErrMsg.setStatus("obsolete")


class _IpPolicyListTrustedFields_Type(Integer32):
    """Custom type ipPolicyListTrustedFields based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              256)
        )
    )
    namedValues = NamedValues(
        *(("cos", 1),
          ("dscp", 2),
          ("cos-dscp", 3),
          ("untrust", 4),
          ("not-supported", 256))
    )


_IpPolicyListTrustedFields_Type.__name__ = "Integer32"
_IpPolicyListTrustedFields_Object = MibTableColumn
ipPolicyListTrustedFields = _IpPolicyListTrustedFields_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 12),
    _IpPolicyListTrustedFields_Type()
)
ipPolicyListTrustedFields.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyListTrustedFields.setStatus("current")


class _IpPolicyListScope_Type(Integer32):
    """Custom type ipPolicyListScope based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("forwardAndControl", 2))
    )


_IpPolicyListScope_Type.__name__ = "Integer32"
_IpPolicyListScope_Object = MibTableColumn
ipPolicyListScope = _IpPolicyListScope_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 13),
    _IpPolicyListScope_Type()
)
ipPolicyListScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyListScope.setStatus("obsolete")


class _IpPolicyListIpOptionOperation_Type(Integer32):
    """Custom type ipPolicyListIpOptionOperation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2),
          ("deny-and-notify", 3),
          ("deny-and-reset-connection", 4),
          ("deny-and-notify-and-reset-connection", 5),
          ("not-supported", 255))
    )


_IpPolicyListIpOptionOperation_Type.__name__ = "Integer32"
_IpPolicyListIpOptionOperation_Object = MibTableColumn
ipPolicyListIpOptionOperation = _IpPolicyListIpOptionOperation_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 14),
    _IpPolicyListIpOptionOperation_Type()
)
ipPolicyListIpOptionOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyListIpOptionOperation.setStatus("current")


class _IpPolicyListIpFragmentationOperation_Type(Integer32):
    """Custom type ipPolicyListIpFragmentationOperation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2),
          ("deny-and-notify", 3),
          ("deny-and-reset-connection", 4),
          ("deny-and-notify-and-reset-connection", 5),
          ("not-supported", 255))
    )


_IpPolicyListIpFragmentationOperation_Type.__name__ = "Integer32"
_IpPolicyListIpFragmentationOperation_Object = MibTableColumn
ipPolicyListIpFragmentationOperation = _IpPolicyListIpFragmentationOperation_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 15),
    _IpPolicyListIpFragmentationOperation_Type()
)
ipPolicyListIpFragmentationOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyListIpFragmentationOperation.setStatus("current")


class _IpPolicyListType_Type(Integer32):
    """Custom type ipPolicyListType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("acl-and-qos", 1),
          ("acl", 2),
          ("qos", 3),
          ("source-nat", 4),
          ("capture", 5),
          ("anti-spoofing", 6),
          ("policy-based-routing", 7),
          ("crypto", 8))
    )


_IpPolicyListType_Type.__name__ = "Integer32"
_IpPolicyListType_Object = MibTableColumn
ipPolicyListType = _IpPolicyListType_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 16),
    _IpPolicyListType_Type()
)
ipPolicyListType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyListType.setStatus("current")


class _IpPolicyListEtherTypeDefaultOperation_Type(Integer32):
    """Custom type ipPolicyListEtherTypeDefaultOperation based on Integer32"""
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
        *(("permit", 1),
          ("deny", 2),
          ("deny-and-notify", 3))
    )


_IpPolicyListEtherTypeDefaultOperation_Type.__name__ = "Integer32"
_IpPolicyListEtherTypeDefaultOperation_Object = MibTableColumn
ipPolicyListEtherTypeDefaultOperation = _IpPolicyListEtherTypeDefaultOperation_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 17),
    _IpPolicyListEtherTypeDefaultOperation_Type()
)
ipPolicyListEtherTypeDefaultOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyListEtherTypeDefaultOperation.setStatus("current")


class _IpPolicyListLocalAddress_Type(OctetString):
    """Custom type ipPolicyListLocalAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_IpPolicyListLocalAddress_Type.__name__ = "OctetString"
_IpPolicyListLocalAddress_Object = MibTableColumn
ipPolicyListLocalAddress = _IpPolicyListLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 18),
    _IpPolicyListLocalAddress_Type()
)
ipPolicyListLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyListLocalAddress.setStatus("current")


class _IpPolicyListNATPoolListIndex_Type(Integer32):
    """Custom type ipPolicyListNATPoolListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyListNATPoolListIndex_Type.__name__ = "Integer32"
_IpPolicyListNATPoolListIndex_Object = MibTableColumn
ipPolicyListNATPoolListIndex = _IpPolicyListNATPoolListIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 19),
    _IpPolicyListNATPoolListIndex_Type()
)
ipPolicyListNATPoolListIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyListNATPoolListIndex.setStatus("current")
_IpPolicyRuleTable_Object = MibTable
ipPolicyRuleTable = _IpPolicyRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2)
)
if mibBuilder.loadTexts:
    ipPolicyRuleTable.setStatus("current")
_IpPolicyRuleEntry_Object = MibTableRow
ipPolicyRuleEntry = _IpPolicyRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1)
)
ipPolicyRuleEntry.setIndexNames(
    (0, "POLICY-MIB", "ipPolicyRuleSlot"),
    (0, "POLICY-MIB", "ipPolicyRuleListID"),
    (0, "POLICY-MIB", "ipPolicyRuleID"),
)
if mibBuilder.loadTexts:
    ipPolicyRuleEntry.setStatus("current")


class _IpPolicyRuleSlot_Type(Integer32):
    """Custom type ipPolicyRuleSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyRuleSlot_Type.__name__ = "Integer32"
_IpPolicyRuleSlot_Object = MibTableColumn
ipPolicyRuleSlot = _IpPolicyRuleSlot_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 1),
    _IpPolicyRuleSlot_Type()
)
ipPolicyRuleSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyRuleSlot.setStatus("current")


class _IpPolicyRuleListID_Type(Integer32):
    """Custom type ipPolicyRuleListID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyRuleListID_Type.__name__ = "Integer32"
_IpPolicyRuleListID_Object = MibTableColumn
ipPolicyRuleListID = _IpPolicyRuleListID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 2),
    _IpPolicyRuleListID_Type()
)
ipPolicyRuleListID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyRuleListID.setStatus("current")


class _IpPolicyRuleID_Type(Integer32):
    """Custom type ipPolicyRuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_IpPolicyRuleID_Type.__name__ = "Integer32"
_IpPolicyRuleID_Object = MibTableColumn
ipPolicyRuleID = _IpPolicyRuleID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 3),
    _IpPolicyRuleID_Type()
)
ipPolicyRuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyRuleID.setStatus("current")


class _IpPolicyRuleSrcAddr_Type(IpAddress):
    """Custom type ipPolicyRuleSrcAddr based on IpAddress"""
    defaultHexValue = "00000000"


_IpPolicyRuleSrcAddr_Type.__name__ = "IpAddress"
_IpPolicyRuleSrcAddr_Object = MibTableColumn
ipPolicyRuleSrcAddr = _IpPolicyRuleSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 4),
    _IpPolicyRuleSrcAddr_Type()
)
ipPolicyRuleSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleSrcAddr.setStatus("current")


class _IpPolicyRuleSrcAddrWild_Type(IpAddress):
    """Custom type ipPolicyRuleSrcAddrWild based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_IpPolicyRuleSrcAddrWild_Type.__name__ = "IpAddress"
_IpPolicyRuleSrcAddrWild_Object = MibTableColumn
ipPolicyRuleSrcAddrWild = _IpPolicyRuleSrcAddrWild_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 5),
    _IpPolicyRuleSrcAddrWild_Type()
)
ipPolicyRuleSrcAddrWild.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleSrcAddrWild.setStatus("current")


class _IpPolicyRuleDstAddr_Type(IpAddress):
    """Custom type ipPolicyRuleDstAddr based on IpAddress"""
    defaultHexValue = "00000000"


_IpPolicyRuleDstAddr_Type.__name__ = "IpAddress"
_IpPolicyRuleDstAddr_Object = MibTableColumn
ipPolicyRuleDstAddr = _IpPolicyRuleDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 6),
    _IpPolicyRuleDstAddr_Type()
)
ipPolicyRuleDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleDstAddr.setStatus("current")


class _IpPolicyRuleDstAddrWild_Type(IpAddress):
    """Custom type ipPolicyRuleDstAddrWild based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_IpPolicyRuleDstAddrWild_Type.__name__ = "IpAddress"
_IpPolicyRuleDstAddrWild_Object = MibTableColumn
ipPolicyRuleDstAddrWild = _IpPolicyRuleDstAddrWild_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 7),
    _IpPolicyRuleDstAddrWild_Type()
)
ipPolicyRuleDstAddrWild.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleDstAddrWild.setStatus("current")


class _IpPolicyRuleProtocol_Type(Integer32):
    """Custom type ipPolicyRuleProtocol based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IpPolicyRuleProtocol_Type.__name__ = "Integer32"
_IpPolicyRuleProtocol_Object = MibTableColumn
ipPolicyRuleProtocol = _IpPolicyRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 8),
    _IpPolicyRuleProtocol_Type()
)
ipPolicyRuleProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleProtocol.setStatus("current")


class _IpPolicyRuleL4SrcPortMin_Type(Integer32):
    """Custom type ipPolicyRuleL4SrcPortMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpPolicyRuleL4SrcPortMin_Type.__name__ = "Integer32"
_IpPolicyRuleL4SrcPortMin_Object = MibTableColumn
ipPolicyRuleL4SrcPortMin = _IpPolicyRuleL4SrcPortMin_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 9),
    _IpPolicyRuleL4SrcPortMin_Type()
)
ipPolicyRuleL4SrcPortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleL4SrcPortMin.setStatus("current")


class _IpPolicyRuleL4SrcPortMax_Type(Integer32):
    """Custom type ipPolicyRuleL4SrcPortMax based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpPolicyRuleL4SrcPortMax_Type.__name__ = "Integer32"
_IpPolicyRuleL4SrcPortMax_Object = MibTableColumn
ipPolicyRuleL4SrcPortMax = _IpPolicyRuleL4SrcPortMax_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 10),
    _IpPolicyRuleL4SrcPortMax_Type()
)
ipPolicyRuleL4SrcPortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleL4SrcPortMax.setStatus("current")


class _IpPolicyRuleL4DestPortMin_Type(Integer32):
    """Custom type ipPolicyRuleL4DestPortMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpPolicyRuleL4DestPortMin_Type.__name__ = "Integer32"
_IpPolicyRuleL4DestPortMin_Object = MibTableColumn
ipPolicyRuleL4DestPortMin = _IpPolicyRuleL4DestPortMin_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 11),
    _IpPolicyRuleL4DestPortMin_Type()
)
ipPolicyRuleL4DestPortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleL4DestPortMin.setStatus("current")


class _IpPolicyRuleL4DestPortMax_Type(Integer32):
    """Custom type ipPolicyRuleL4DestPortMax based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpPolicyRuleL4DestPortMax_Type.__name__ = "Integer32"
_IpPolicyRuleL4DestPortMax_Object = MibTableColumn
ipPolicyRuleL4DestPortMax = _IpPolicyRuleL4DestPortMax_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 12),
    _IpPolicyRuleL4DestPortMax_Type()
)
ipPolicyRuleL4DestPortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleL4DestPortMax.setStatus("current")


class _IpPolicyRuleEstablished_Type(Integer32):
    """Custom type ipPolicyRuleEstablished based on Integer32"""
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
          ("dontCare", 2))
    )


_IpPolicyRuleEstablished_Type.__name__ = "Integer32"
_IpPolicyRuleEstablished_Object = MibTableColumn
ipPolicyRuleEstablished = _IpPolicyRuleEstablished_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 13),
    _IpPolicyRuleEstablished_Type()
)
ipPolicyRuleEstablished.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleEstablished.setStatus("current")


class _IpPolicyRuleOperation_Type(Integer32):
    """Custom type ipPolicyRuleOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_IpPolicyRuleOperation_Type.__name__ = "Integer32"
_IpPolicyRuleOperation_Object = MibTableColumn
ipPolicyRuleOperation = _IpPolicyRuleOperation_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 14),
    _IpPolicyRuleOperation_Type()
)
ipPolicyRuleOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleOperation.setStatus("current")


class _IpPolicyRuleApplicabilityPrecedence_Type(Integer32):
    """Custom type ipPolicyRuleApplicabilityPrecedence based on Integer32"""
    defaultValue = 9999

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_IpPolicyRuleApplicabilityPrecedence_Type.__name__ = "Integer32"
_IpPolicyRuleApplicabilityPrecedence_Object = MibTableColumn
ipPolicyRuleApplicabilityPrecedence = _IpPolicyRuleApplicabilityPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 15),
    _IpPolicyRuleApplicabilityPrecedence_Type()
)
ipPolicyRuleApplicabilityPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleApplicabilityPrecedence.setStatus("current")


class _IpPolicyRuleApplicabilityStatus_Type(Integer32):
    """Custom type ipPolicyRuleApplicabilityStatus based on Integer32"""
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
        *(("applicable", 1),
          ("partiallyApplicable", 2),
          ("notApplicable", 3),
          ("unknown", 4))
    )


_IpPolicyRuleApplicabilityStatus_Type.__name__ = "Integer32"
_IpPolicyRuleApplicabilityStatus_Object = MibTableColumn
ipPolicyRuleApplicabilityStatus = _IpPolicyRuleApplicabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 16),
    _IpPolicyRuleApplicabilityStatus_Type()
)
ipPolicyRuleApplicabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyRuleApplicabilityStatus.setStatus("obsolete")


class _IpPolicyRuleApplicabilityType_Type(Integer32):
    """Custom type ipPolicyRuleApplicabilityType based on Integer32"""
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
        *(("static", 1),
          ("quasiStatic", 2),
          ("dynamic", 3),
          ("unknown", 4))
    )


_IpPolicyRuleApplicabilityType_Type.__name__ = "Integer32"
_IpPolicyRuleApplicabilityType_Object = MibTableColumn
ipPolicyRuleApplicabilityType = _IpPolicyRuleApplicabilityType_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 17),
    _IpPolicyRuleApplicabilityType_Type()
)
ipPolicyRuleApplicabilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyRuleApplicabilityType.setStatus("obsolete")


class _IpPolicyRuleErrMsg_Type(DisplayString):
    """Custom type ipPolicyRuleErrMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IpPolicyRuleErrMsg_Type.__name__ = "DisplayString"
_IpPolicyRuleErrMsg_Object = MibTableColumn
ipPolicyRuleErrMsg = _IpPolicyRuleErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 18),
    _IpPolicyRuleErrMsg_Type()
)
ipPolicyRuleErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyRuleErrMsg.setStatus("obsolete")
_IpPolicyRuleStatus_Type = RowStatus
_IpPolicyRuleStatus_Object = MibTableColumn
ipPolicyRuleStatus = _IpPolicyRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 19),
    _IpPolicyRuleStatus_Type()
)
ipPolicyRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleStatus.setStatus("current")


class _IpPolicyRuleDSCPOperation_Type(Integer32):
    """Custom type ipPolicyRuleDSCPOperation based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_IpPolicyRuleDSCPOperation_Type.__name__ = "Integer32"
_IpPolicyRuleDSCPOperation_Object = MibTableColumn
ipPolicyRuleDSCPOperation = _IpPolicyRuleDSCPOperation_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 20),
    _IpPolicyRuleDSCPOperation_Type()
)
ipPolicyRuleDSCPOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleDSCPOperation.setStatus("obsolete")


class _IpPolicyRuleDSCPFilter_Type(Integer32):
    """Custom type ipPolicyRuleDSCPFilter based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_IpPolicyRuleDSCPFilter_Type.__name__ = "Integer32"
_IpPolicyRuleDSCPFilter_Object = MibTableColumn
ipPolicyRuleDSCPFilter = _IpPolicyRuleDSCPFilter_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 21),
    _IpPolicyRuleDSCPFilter_Type()
)
ipPolicyRuleDSCPFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleDSCPFilter.setStatus("current")


class _IpPolicyRuleDSCPFilterWild_Type(Integer32):
    """Custom type ipPolicyRuleDSCPFilterWild based on Integer32"""
    defaultValue = 63

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_IpPolicyRuleDSCPFilterWild_Type.__name__ = "Integer32"
_IpPolicyRuleDSCPFilterWild_Object = MibTableColumn
ipPolicyRuleDSCPFilterWild = _IpPolicyRuleDSCPFilterWild_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 22),
    _IpPolicyRuleDSCPFilterWild_Type()
)
ipPolicyRuleDSCPFilterWild.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleDSCPFilterWild.setStatus("current")


class _IpPolicyRuleIcmpTypeCode_Type(Integer32):
    """Custom type ipPolicyRuleIcmpTypeCode based on Integer32"""
    defaultValue = 262144

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              768,
              769,
              770,
              771,
              772,
              773,
              774,
              775,
              777,
              779,
              780,
              781,
              782,
              783,
              1024,
              1280,
              1283,
              2048,
              2304,
              2817,
              3072,
              3073,
              3328,
              3584,
              4352,
              4608,
              7680,
              7681,
              9472,
              9728,
              9984,
              66304,
              66816,
              68352,
              68608,
              73216,
              73472,
              73728,
              73984,
              74240,
              74496,
              74752,
              75776,
              196608,
              262144)
        )
    )
    namedValues = NamedValues(
        *(("echo-reply", 0),
          ("netwrok-unreachable", 768),
          ("host-unreachable", 769),
          ("protocol-unreachable", 770),
          ("port-unreachable", 771),
          ("fragmentation-needed-but-df-bit-set", 772),
          ("source-route-failed", 773),
          ("destination-network-unknown", 774),
          ("destination-host-unknown", 775),
          ("destination-network-admin-prohibited", 777),
          ("network-unreachable-for-tos", 779),
          ("host-unreachable-for-tos", 780),
          ("communication-admin-prohibited-filtering", 781),
          ("host-precedence-violation", 782),
          ("precedence-cutoff-in-effect", 783),
          ("source-quench", 1024),
          ("redirect-for-network", 1280),
          ("redirect-for-type-of-service-and-host", 1283),
          ("echo-request", 2048),
          ("router-advertisement", 2304),
          ("time-to-live-equals-0-during-reassembly", 2817),
          ("bad-ip-header", 3072),
          ("required-option-missing", 3073),
          ("timestamp-requested", 3328),
          ("timestamp-reply", 3584),
          ("address-mask-request", 4352),
          ("address-mask-reply", 4608),
          ("traceroute-outbound-packet-successfully-fw", 7680),
          ("traceroute-no-route-for-outbound-packet", 7681),
          ("domain-name-request", 9472),
          ("domain-name-reply", 9728),
          ("skip-algorithm-discovery-protocol", 9984),
          ("unreachable", 66304),
          ("redirect", 66816),
          ("time-exceeded", 68352),
          ("parameters-problem", 68608),
          ("traceroute", 73216),
          ("conversion-errors", 73472),
          ("mobile-host-redirect", 73728),
          ("ipv6-where-are-you", 73984),
          ("ipv6-I-am-here", 74240),
          ("mobile-registration-request", 74496),
          ("mobile-registration-reply", 74752),
          ("security-failure", 75776),
          ("any", 196608),
          ("not-supported", 262144))
    )


_IpPolicyRuleIcmpTypeCode_Type.__name__ = "Integer32"
_IpPolicyRuleIcmpTypeCode_Object = MibTableColumn
ipPolicyRuleIcmpTypeCode = _IpPolicyRuleIcmpTypeCode_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 23),
    _IpPolicyRuleIcmpTypeCode_Type()
)
ipPolicyRuleIcmpTypeCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleIcmpTypeCode.setStatus("current")


class _IpPolicyRuleSrcAddrNot_Type(Integer32):
    """Custom type ipPolicyRuleSrcAddrNot based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("not-source-ip-address", 2))
    )


_IpPolicyRuleSrcAddrNot_Type.__name__ = "Integer32"
_IpPolicyRuleSrcAddrNot_Object = MibTableColumn
ipPolicyRuleSrcAddrNot = _IpPolicyRuleSrcAddrNot_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 24),
    _IpPolicyRuleSrcAddrNot_Type()
)
ipPolicyRuleSrcAddrNot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleSrcAddrNot.setStatus("current")


class _IpPolicyRuleDstAddrNot_Type(Integer32):
    """Custom type ipPolicyRuleDstAddrNot based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("not-destination-ip-address", 2))
    )


_IpPolicyRuleDstAddrNot_Type.__name__ = "Integer32"
_IpPolicyRuleDstAddrNot_Object = MibTableColumn
ipPolicyRuleDstAddrNot = _IpPolicyRuleDstAddrNot_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 25),
    _IpPolicyRuleDstAddrNot_Type()
)
ipPolicyRuleDstAddrNot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleDstAddrNot.setStatus("current")


class _IpPolicyRuleProtocolNot_Type(Integer32):
    """Custom type ipPolicyRuleProtocolNot based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("not-ip-protocol", 2))
    )


_IpPolicyRuleProtocolNot_Type.__name__ = "Integer32"
_IpPolicyRuleProtocolNot_Object = MibTableColumn
ipPolicyRuleProtocolNot = _IpPolicyRuleProtocolNot_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 26),
    _IpPolicyRuleProtocolNot_Type()
)
ipPolicyRuleProtocolNot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleProtocolNot.setStatus("current")


class _IpPolicyRuleL4SrcPortNot_Type(Integer32):
    """Custom type ipPolicyRuleL4SrcPortNot based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("not-source-port", 2))
    )


_IpPolicyRuleL4SrcPortNot_Type.__name__ = "Integer32"
_IpPolicyRuleL4SrcPortNot_Object = MibTableColumn
ipPolicyRuleL4SrcPortNot = _IpPolicyRuleL4SrcPortNot_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 27),
    _IpPolicyRuleL4SrcPortNot_Type()
)
ipPolicyRuleL4SrcPortNot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleL4SrcPortNot.setStatus("current")


class _IpPolicyRuleL4DestPortNot_Type(Integer32):
    """Custom type ipPolicyRuleL4DestPortNot based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("not-destination-port", 2))
    )


_IpPolicyRuleL4DestPortNot_Type.__name__ = "Integer32"
_IpPolicyRuleL4DestPortNot_Object = MibTableColumn
ipPolicyRuleL4DestPortNot = _IpPolicyRuleL4DestPortNot_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 28),
    _IpPolicyRuleL4DestPortNot_Type()
)
ipPolicyRuleL4DestPortNot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleL4DestPortNot.setStatus("current")


class _IpPolicyRuleIcmpTypeCodeNot_Type(Integer32):
    """Custom type ipPolicyRuleIcmpTypeCodeNot based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("not-icmp-type-code", 2))
    )


_IpPolicyRuleIcmpTypeCodeNot_Type.__name__ = "Integer32"
_IpPolicyRuleIcmpTypeCodeNot_Object = MibTableColumn
ipPolicyRuleIcmpTypeCodeNot = _IpPolicyRuleIcmpTypeCodeNot_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 29),
    _IpPolicyRuleIcmpTypeCodeNot_Type()
)
ipPolicyRuleIcmpTypeCodeNot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleIcmpTypeCodeNot.setStatus("current")


class _IpPolicyRuleSrcPolicyUserGroupName_Type(DisplayString):
    """Custom type ipPolicyRuleSrcPolicyUserGroupName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpPolicyRuleSrcPolicyUserGroupName_Type.__name__ = "DisplayString"
_IpPolicyRuleSrcPolicyUserGroupName_Object = MibTableColumn
ipPolicyRuleSrcPolicyUserGroupName = _IpPolicyRuleSrcPolicyUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 30),
    _IpPolicyRuleSrcPolicyUserGroupName_Type()
)
ipPolicyRuleSrcPolicyUserGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleSrcPolicyUserGroupName.setStatus("current")


class _IpPolicyRuleDstPolicyUserGroupName_Type(DisplayString):
    """Custom type ipPolicyRuleDstPolicyUserGroupName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpPolicyRuleDstPolicyUserGroupName_Type.__name__ = "DisplayString"
_IpPolicyRuleDstPolicyUserGroupName_Object = MibTableColumn
ipPolicyRuleDstPolicyUserGroupName = _IpPolicyRuleDstPolicyUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 31),
    _IpPolicyRuleDstPolicyUserGroupName_Type()
)
ipPolicyRuleDstPolicyUserGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleDstPolicyUserGroupName.setStatus("current")


class _IpPolicyRuleDSCPFilterNot_Type(Integer32):
    """Custom type ipPolicyRuleDSCPFilterNot based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("not-dscp", 2))
    )


_IpPolicyRuleDSCPFilterNot_Type.__name__ = "Integer32"
_IpPolicyRuleDSCPFilterNot_Object = MibTableColumn
ipPolicyRuleDSCPFilterNot = _IpPolicyRuleDSCPFilterNot_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 32),
    _IpPolicyRuleDSCPFilterNot_Type()
)
ipPolicyRuleDSCPFilterNot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleDSCPFilterNot.setStatus("current")


class _IpPolicyRuleDescription_Type(DisplayString):
    """Custom type ipPolicyRuleDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_IpPolicyRuleDescription_Type.__name__ = "DisplayString"
_IpPolicyRuleDescription_Object = MibTableColumn
ipPolicyRuleDescription = _IpPolicyRuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 33),
    _IpPolicyRuleDescription_Type()
)
ipPolicyRuleDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleDescription.setStatus("current")


class _IpPolicyRuleFragment_Type(Integer32):
    """Custom type ipPolicyRuleFragment based on Integer32"""
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
          ("dontCare", 2))
    )


_IpPolicyRuleFragment_Type.__name__ = "Integer32"
_IpPolicyRuleFragment_Object = MibTableColumn
ipPolicyRuleFragment = _IpPolicyRuleFragment_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 34),
    _IpPolicyRuleFragment_Type()
)
ipPolicyRuleFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleFragment.setStatus("current")


class _IpPolicyRuleDoSClass_Type(Integer32):
    """Custom type ipPolicyRuleDoSClass based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              9,
              11,
              100,
              101,
              102,
              103,
              104,
              105,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ipPolicySmurf-AttackRule", 8),
          ("ipPolicyFraggleAttackRule", 9),
          ("ipPolicypSpoofingRule", 11),
          ("ipPolicyUsedDefinedDoS100", 100),
          ("ipPolicyUsedDefinedDoS101", 101),
          ("ipPolicyUsedDefinedDoS102", 102),
          ("ipPolicyUsedDefinedDoS103", 103),
          ("ipPolicyUsedDefinedDoS104", 104),
          ("ipPolicyUsedDefinedDoS105", 105),
          ("ipPolicyNonApplicable", 255))
    )


_IpPolicyRuleDoSClass_Type.__name__ = "Integer32"
_IpPolicyRuleDoSClass_Object = MibTableColumn
ipPolicyRuleDoSClass = _IpPolicyRuleDoSClass_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 35),
    _IpPolicyRuleDoSClass_Type()
)
ipPolicyRuleDoSClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleDoSClass.setStatus("current")
_IpPolicyControlTable_Object = MibTable
ipPolicyControlTable = _IpPolicyControlTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 3)
)
if mibBuilder.loadTexts:
    ipPolicyControlTable.setStatus("current")
_IpPolicyControlEntry_Object = MibTableRow
ipPolicyControlEntry = _IpPolicyControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 3, 1)
)
ipPolicyControlEntry.setIndexNames(
    (0, "POLICY-MIB", "ipPolicyControlSlot"),
)
if mibBuilder.loadTexts:
    ipPolicyControlEntry.setStatus("current")


class _IpPolicyControlSlot_Type(Integer32):
    """Custom type ipPolicyControlSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyControlSlot_Type.__name__ = "Integer32"
_IpPolicyControlSlot_Object = MibTableColumn
ipPolicyControlSlot = _IpPolicyControlSlot_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 3, 1, 1),
    _IpPolicyControlSlot_Type()
)
ipPolicyControlSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyControlSlot.setStatus("current")


class _IpPolicyControlActiveGeneralList_Type(Integer32):
    """Custom type ipPolicyControlActiveGeneralList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyControlActiveGeneralList_Type.__name__ = "Integer32"
_IpPolicyControlActiveGeneralList_Object = MibTableColumn
ipPolicyControlActiveGeneralList = _IpPolicyControlActiveGeneralList_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 3, 1, 2),
    _IpPolicyControlActiveGeneralList_Type()
)
ipPolicyControlActiveGeneralList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyControlActiveGeneralList.setStatus("obsolete")


class _IpPolicyControlAllowedPolicyManagers_Type(Integer32):
    """Custom type ipPolicyControlAllowedPolicyManagers based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_IpPolicyControlAllowedPolicyManagers_Type.__name__ = "Integer32"
_IpPolicyControlAllowedPolicyManagers_Object = MibTableColumn
ipPolicyControlAllowedPolicyManagers = _IpPolicyControlAllowedPolicyManagers_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 3, 1, 3),
    _IpPolicyControlAllowedPolicyManagers_Type()
)
ipPolicyControlAllowedPolicyManagers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyControlAllowedPolicyManagers.setStatus("current")
_IpPolicyControlCurrentChecksum_Type = Integer32
_IpPolicyControlCurrentChecksum_Object = MibTableColumn
ipPolicyControlCurrentChecksum = _IpPolicyControlCurrentChecksum_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 3, 1, 4),
    _IpPolicyControlCurrentChecksum_Type()
)
ipPolicyControlCurrentChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyControlCurrentChecksum.setStatus("current")


class _IpPolicyControlMinimalPolicyManagmentVersion_Type(OctetString):
    """Custom type ipPolicyControlMinimalPolicyManagmentVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )
    fixed_length = 25


_IpPolicyControlMinimalPolicyManagmentVersion_Type.__name__ = "OctetString"
_IpPolicyControlMinimalPolicyManagmentVersion_Object = MibTableColumn
ipPolicyControlMinimalPolicyManagmentVersion = _IpPolicyControlMinimalPolicyManagmentVersion_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 3, 1, 5),
    _IpPolicyControlMinimalPolicyManagmentVersion_Type()
)
ipPolicyControlMinimalPolicyManagmentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyControlMinimalPolicyManagmentVersion.setStatus("obsolete")


class _IpPolicyControlMaximalPolicyManagmentVersion_Type(OctetString):
    """Custom type ipPolicyControlMaximalPolicyManagmentVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )
    fixed_length = 25


_IpPolicyControlMaximalPolicyManagmentVersion_Type.__name__ = "OctetString"
_IpPolicyControlMaximalPolicyManagmentVersion_Object = MibTableColumn
ipPolicyControlMaximalPolicyManagmentVersion = _IpPolicyControlMaximalPolicyManagmentVersion_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 3, 1, 6),
    _IpPolicyControlMaximalPolicyManagmentVersion_Type()
)
ipPolicyControlMaximalPolicyManagmentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyControlMaximalPolicyManagmentVersion.setStatus("obsolete")
_IpPolicyControlMIBversion_Type = Integer32
_IpPolicyControlMIBversion_Object = MibTableColumn
ipPolicyControlMIBversion = _IpPolicyControlMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 3, 1, 7),
    _IpPolicyControlMIBversion_Type()
)
ipPolicyControlMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyControlMIBversion.setStatus("current")
_IpPolicyControlCapabilitiesGeneral_Type = OctetString
_IpPolicyControlCapabilitiesGeneral_Object = MibTableColumn
ipPolicyControlCapabilitiesGeneral = _IpPolicyControlCapabilitiesGeneral_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 3, 1, 8),
    _IpPolicyControlCapabilitiesGeneral_Type()
)
ipPolicyControlCapabilitiesGeneral.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyControlCapabilitiesGeneral.setStatus("current")
_IpPolicyControlCopySourceList_Type = Integer32
_IpPolicyControlCopySourceList_Object = MibTableColumn
ipPolicyControlCopySourceList = _IpPolicyControlCopySourceList_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 3, 1, 9),
    _IpPolicyControlCopySourceList_Type()
)
ipPolicyControlCopySourceList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyControlCopySourceList.setStatus("current")
_IpPolicyControlCopyDestinationList_Type = Integer32
_IpPolicyControlCopyDestinationList_Object = MibTableColumn
ipPolicyControlCopyDestinationList = _IpPolicyControlCopyDestinationList_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 3, 1, 10),
    _IpPolicyControlCopyDestinationList_Type()
)
ipPolicyControlCopyDestinationList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyControlCopyDestinationList.setStatus("current")


class _IpPolicyControlCopyOperation_Type(Integer32):
    """Custom type ipPolicyControlCopyOperation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("copy", 2))
    )


_IpPolicyControlCopyOperation_Type.__name__ = "Integer32"
_IpPolicyControlCopyOperation_Object = MibTableColumn
ipPolicyControlCopyOperation = _IpPolicyControlCopyOperation_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 3, 1, 11),
    _IpPolicyControlCopyOperation_Type()
)
ipPolicyControlCopyOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyControlCopyOperation.setStatus("current")


class _IpPolicyControlCopyOperationLastStatus_Type(Integer32):
    """Custom type ipPolicyControlCopyOperationLastStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("error", 2))
    )


_IpPolicyControlCopyOperationLastStatus_Type.__name__ = "Integer32"
_IpPolicyControlCopyOperationLastStatus_Object = MibTableColumn
ipPolicyControlCopyOperationLastStatus = _IpPolicyControlCopyOperationLastStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 3, 1, 12),
    _IpPolicyControlCopyOperationLastStatus_Type()
)
ipPolicyControlCopyOperationLastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyControlCopyOperationLastStatus.setStatus("current")


class _IpPolicyControlCopyOperationLastFailureDisplay_Type(DisplayString):
    """Custom type ipPolicyControlCopyOperationLastFailureDisplay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IpPolicyControlCopyOperationLastFailureDisplay_Type.__name__ = "DisplayString"
_IpPolicyControlCopyOperationLastFailureDisplay_Object = MibTableColumn
ipPolicyControlCopyOperationLastFailureDisplay = _IpPolicyControlCopyOperationLastFailureDisplay_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 3, 1, 13),
    _IpPolicyControlCopyOperationLastFailureDisplay_Type()
)
ipPolicyControlCopyOperationLastFailureDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyControlCopyOperationLastFailureDisplay.setStatus("current")
_IpPolicyDiffServTable_Object = MibTable
ipPolicyDiffServTable = _IpPolicyDiffServTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 4)
)
if mibBuilder.loadTexts:
    ipPolicyDiffServTable.setStatus("obsolete")
_IpPolicyDiffServEntry_Object = MibTableRow
ipPolicyDiffServEntry = _IpPolicyDiffServEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 4, 1)
)
ipPolicyDiffServEntry.setIndexNames(
    (0, "POLICY-MIB", "ipPolicyDiffServSlot"),
    (0, "POLICY-MIB", "ipPolicyDiffServDSCP"),
)
if mibBuilder.loadTexts:
    ipPolicyDiffServEntry.setStatus("obsolete")


class _IpPolicyDiffServSlot_Type(Integer32):
    """Custom type ipPolicyDiffServSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyDiffServSlot_Type.__name__ = "Integer32"
_IpPolicyDiffServSlot_Object = MibTableColumn
ipPolicyDiffServSlot = _IpPolicyDiffServSlot_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 4, 1, 1),
    _IpPolicyDiffServSlot_Type()
)
ipPolicyDiffServSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyDiffServSlot.setStatus("obsolete")


class _IpPolicyDiffServDSCP_Type(Integer32):
    """Custom type ipPolicyDiffServDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_IpPolicyDiffServDSCP_Type.__name__ = "Integer32"
_IpPolicyDiffServDSCP_Object = MibTableColumn
ipPolicyDiffServDSCP = _IpPolicyDiffServDSCP_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 4, 1, 2),
    _IpPolicyDiffServDSCP_Type()
)
ipPolicyDiffServDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyDiffServDSCP.setStatus("obsolete")


class _IpPolicyDiffServOperation_Type(Integer32):
    """Custom type ipPolicyDiffServOperation based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_IpPolicyDiffServOperation_Type.__name__ = "Integer32"
_IpPolicyDiffServOperation_Object = MibTableColumn
ipPolicyDiffServOperation = _IpPolicyDiffServOperation_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 4, 1, 3),
    _IpPolicyDiffServOperation_Type()
)
ipPolicyDiffServOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyDiffServOperation.setStatus("obsolete")


class _IpPolicyDiffServName_Type(DisplayString):
    """Custom type ipPolicyDiffServName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_IpPolicyDiffServName_Type.__name__ = "DisplayString"
_IpPolicyDiffServName_Object = MibTableColumn
ipPolicyDiffServName = _IpPolicyDiffServName_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 4, 1, 4),
    _IpPolicyDiffServName_Type()
)
ipPolicyDiffServName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyDiffServName.setStatus("obsolete")


class _IpPolicyDiffServAggIndex_Type(Integer32):
    """Custom type ipPolicyDiffServAggIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_IpPolicyDiffServAggIndex_Type.__name__ = "Integer32"
_IpPolicyDiffServAggIndex_Object = MibTableColumn
ipPolicyDiffServAggIndex = _IpPolicyDiffServAggIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 4, 1, 5),
    _IpPolicyDiffServAggIndex_Type()
)
ipPolicyDiffServAggIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyDiffServAggIndex.setStatus("obsolete")


class _IpPolicyDiffServApplicabilityPrecedence_Type(Integer32):
    """Custom type ipPolicyDiffServApplicabilityPrecedence based on Integer32"""
    defaultValue = 9999

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_IpPolicyDiffServApplicabilityPrecedence_Type.__name__ = "Integer32"
_IpPolicyDiffServApplicabilityPrecedence_Object = MibTableColumn
ipPolicyDiffServApplicabilityPrecedence = _IpPolicyDiffServApplicabilityPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 4, 1, 6),
    _IpPolicyDiffServApplicabilityPrecedence_Type()
)
ipPolicyDiffServApplicabilityPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyDiffServApplicabilityPrecedence.setStatus("obsolete")


class _IpPolicyDiffServApplicabilityStatus_Type(Integer32):
    """Custom type ipPolicyDiffServApplicabilityStatus based on Integer32"""
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
        *(("applicable", 1),
          ("partiallyApplicable", 2),
          ("notApplicable", 3),
          ("unknown", 4))
    )


_IpPolicyDiffServApplicabilityStatus_Type.__name__ = "Integer32"
_IpPolicyDiffServApplicabilityStatus_Object = MibTableColumn
ipPolicyDiffServApplicabilityStatus = _IpPolicyDiffServApplicabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 4, 1, 7),
    _IpPolicyDiffServApplicabilityStatus_Type()
)
ipPolicyDiffServApplicabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyDiffServApplicabilityStatus.setStatus("obsolete")


class _IpPolicyDiffServApplicabilityType_Type(Integer32):
    """Custom type ipPolicyDiffServApplicabilityType based on Integer32"""
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
        *(("static", 1),
          ("quasiStatic", 2),
          ("dynamic", 3),
          ("unknown", 4))
    )


_IpPolicyDiffServApplicabilityType_Type.__name__ = "Integer32"
_IpPolicyDiffServApplicabilityType_Object = MibTableColumn
ipPolicyDiffServApplicabilityType = _IpPolicyDiffServApplicabilityType_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 4, 1, 8),
    _IpPolicyDiffServApplicabilityType_Type()
)
ipPolicyDiffServApplicabilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyDiffServApplicabilityType.setStatus("obsolete")


class _IpPolicyDiffServErrMsg_Type(DisplayString):
    """Custom type ipPolicyDiffServErrMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IpPolicyDiffServErrMsg_Type.__name__ = "DisplayString"
_IpPolicyDiffServErrMsg_Object = MibTableColumn
ipPolicyDiffServErrMsg = _IpPolicyDiffServErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 4, 1, 9),
    _IpPolicyDiffServErrMsg_Type()
)
ipPolicyDiffServErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyDiffServErrMsg.setStatus("obsolete")
_IpPolicyQueryTable_Object = MibTable
ipPolicyQueryTable = _IpPolicyQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5)
)
if mibBuilder.loadTexts:
    ipPolicyQueryTable.setStatus("current")
_IpPolicyQueryEntry_Object = MibTableRow
ipPolicyQueryEntry = _IpPolicyQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1)
)
ipPolicyQueryEntry.setIndexNames(
    (0, "POLICY-MIB", "ipPolicyQuerySlot"),
)
if mibBuilder.loadTexts:
    ipPolicyQueryEntry.setStatus("current")


class _IpPolicyQuerySlot_Type(Integer32):
    """Custom type ipPolicyQuerySlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyQuerySlot_Type.__name__ = "Integer32"
_IpPolicyQuerySlot_Object = MibTableColumn
ipPolicyQuerySlot = _IpPolicyQuerySlot_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 1),
    _IpPolicyQuerySlot_Type()
)
ipPolicyQuerySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyQuerySlot.setStatus("current")


class _IpPolicyQueryListID_Type(Integer32):
    """Custom type ipPolicyQueryListID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyQueryListID_Type.__name__ = "Integer32"
_IpPolicyQueryListID_Object = MibTableColumn
ipPolicyQueryListID = _IpPolicyQueryListID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 2),
    _IpPolicyQueryListID_Type()
)
ipPolicyQueryListID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyQueryListID.setStatus("current")
_IpPolicyQuerySrcAddr_Type = IpAddress
_IpPolicyQuerySrcAddr_Object = MibTableColumn
ipPolicyQuerySrcAddr = _IpPolicyQuerySrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 3),
    _IpPolicyQuerySrcAddr_Type()
)
ipPolicyQuerySrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyQuerySrcAddr.setStatus("current")
_IpPolicyQueryDstAddr_Type = IpAddress
_IpPolicyQueryDstAddr_Object = MibTableColumn
ipPolicyQueryDstAddr = _IpPolicyQueryDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 4),
    _IpPolicyQueryDstAddr_Type()
)
ipPolicyQueryDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyQueryDstAddr.setStatus("current")


class _IpPolicyQueryProtocol_Type(Integer32):
    """Custom type ipPolicyQueryProtocol based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IpPolicyQueryProtocol_Type.__name__ = "Integer32"
_IpPolicyQueryProtocol_Object = MibTableColumn
ipPolicyQueryProtocol = _IpPolicyQueryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 5),
    _IpPolicyQueryProtocol_Type()
)
ipPolicyQueryProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyQueryProtocol.setStatus("current")


class _IpPolicyQueryL4SrcPort_Type(Integer32):
    """Custom type ipPolicyQueryL4SrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_IpPolicyQueryL4SrcPort_Type.__name__ = "Integer32"
_IpPolicyQueryL4SrcPort_Object = MibTableColumn
ipPolicyQueryL4SrcPort = _IpPolicyQueryL4SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 6),
    _IpPolicyQueryL4SrcPort_Type()
)
ipPolicyQueryL4SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyQueryL4SrcPort.setStatus("current")


class _IpPolicyQueryL4DestPort_Type(Integer32):
    """Custom type ipPolicyQueryL4DestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpPolicyQueryL4DestPort_Type.__name__ = "Integer32"
_IpPolicyQueryL4DestPort_Object = MibTableColumn
ipPolicyQueryL4DestPort = _IpPolicyQueryL4DestPort_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 7),
    _IpPolicyQueryL4DestPort_Type()
)
ipPolicyQueryL4DestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyQueryL4DestPort.setStatus("current")


class _IpPolicyQueryEstablished_Type(Integer32):
    """Custom type ipPolicyQueryEstablished based on Integer32"""
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


_IpPolicyQueryEstablished_Type.__name__ = "Integer32"
_IpPolicyQueryEstablished_Object = MibTableColumn
ipPolicyQueryEstablished = _IpPolicyQueryEstablished_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 8),
    _IpPolicyQueryEstablished_Type()
)
ipPolicyQueryEstablished.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyQueryEstablished.setStatus("current")


class _IpPolicyQueryDSCP_Type(Integer32):
    """Custom type ipPolicyQueryDSCP based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_IpPolicyQueryDSCP_Type.__name__ = "Integer32"
_IpPolicyQueryDSCP_Object = MibTableColumn
ipPolicyQueryDSCP = _IpPolicyQueryDSCP_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 9),
    _IpPolicyQueryDSCP_Type()
)
ipPolicyQueryDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyQueryDSCP.setStatus("current")


class _IpPolicyQueryOperation_Type(Integer32):
    """Custom type ipPolicyQueryOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_IpPolicyQueryOperation_Type.__name__ = "Integer32"
_IpPolicyQueryOperation_Object = MibTableColumn
ipPolicyQueryOperation = _IpPolicyQueryOperation_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 10),
    _IpPolicyQueryOperation_Type()
)
ipPolicyQueryOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyQueryOperation.setStatus("current")


class _IpPolicyQueryRuleID_Type(Integer32):
    """Custom type ipPolicyQueryRuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_IpPolicyQueryRuleID_Type.__name__ = "Integer32"
_IpPolicyQueryRuleID_Object = MibTableColumn
ipPolicyQueryRuleID = _IpPolicyQueryRuleID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 11),
    _IpPolicyQueryRuleID_Type()
)
ipPolicyQueryRuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyQueryRuleID.setStatus("current")


class _IpPolicyQueryDSCPOperation_Type(Integer32):
    """Custom type ipPolicyQueryDSCPOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65),
    )


_IpPolicyQueryDSCPOperation_Type.__name__ = "Integer32"
_IpPolicyQueryDSCPOperation_Object = MibTableColumn
ipPolicyQueryDSCPOperation = _IpPolicyQueryDSCPOperation_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 12),
    _IpPolicyQueryDSCPOperation_Type()
)
ipPolicyQueryDSCPOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyQueryDSCPOperation.setStatus("current")


class _IpPolicyQueryPriority_Type(Integer32):
    """Custom type ipPolicyQueryPriority based on Integer32"""
    defaultValue = 99

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
              99)
        )
    )
    namedValues = NamedValues(
        *(("forwardPriority0", 1),
          ("forwardPriority1", 2),
          ("forwardPriority2", 3),
          ("forwardPriority3", 4),
          ("forwardPriority4", 5),
          ("forwardPriority5", 6),
          ("forwardPriority6", 7),
          ("forwardPriority7", 8),
          ("dontCare", 99))
    )


_IpPolicyQueryPriority_Type.__name__ = "Integer32"
_IpPolicyQueryPriority_Object = MibTableColumn
ipPolicyQueryPriority = _IpPolicyQueryPriority_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 13),
    _IpPolicyQueryPriority_Type()
)
ipPolicyQueryPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyQueryPriority.setStatus("current")


class _IpPolicyQueryIfIndex_Type(Integer32):
    """Custom type ipPolicyQueryIfIndex based on Integer32"""
    defaultValue = 0


_IpPolicyQueryIfIndex_Type.__name__ = "Integer32"
_IpPolicyQueryIfIndex_Object = MibTableColumn
ipPolicyQueryIfIndex = _IpPolicyQueryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 14),
    _IpPolicyQueryIfIndex_Type()
)
ipPolicyQueryIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyQueryIfIndex.setStatus("current")


class _IpPolicyQuerySubContext_Type(SubContextTypes):
    """Custom type ipPolicyQuerySubContext based on SubContextTypes"""
    defaultValue = 1


_IpPolicyQuerySubContext_Type.__name__ = "SubContextTypes"
_IpPolicyQuerySubContext_Object = MibTableColumn
ipPolicyQuerySubContext = _IpPolicyQuerySubContext_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 15),
    _IpPolicyQuerySubContext_Type()
)
ipPolicyQuerySubContext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyQuerySubContext.setStatus("current")


class _IpPolicyQueryIcmpTypeCode_Type(Integer32):
    """Custom type ipPolicyQueryIcmpTypeCode based on Integer32"""
    defaultValue = 262144

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              768,
              769,
              770,
              771,
              772,
              773,
              774,
              775,
              777,
              779,
              780,
              781,
              782,
              783,
              1024,
              1280,
              1283,
              2048,
              2304,
              2817,
              3072,
              3073,
              3328,
              3584,
              4352,
              4608,
              7680,
              7681,
              9472,
              9728,
              9984,
              66304,
              66816,
              68352,
              68608,
              73216,
              73472,
              73728,
              73984,
              74240,
              74496,
              74752,
              75776,
              196608,
              262144)
        )
    )
    namedValues = NamedValues(
        *(("echo-reply", 0),
          ("netwrok-unreachable", 768),
          ("host-unreachable", 769),
          ("protocol-unreachable", 770),
          ("port-unreachable", 771),
          ("fragmentation-needed-but-df-bit-set", 772),
          ("source-route-failed", 773),
          ("destination-network-unknown", 774),
          ("destination-host-unknown", 775),
          ("destination-network-admin-prohibited", 777),
          ("network-unreachable-for-tos", 779),
          ("host-unreachable-for-tos", 780),
          ("communication-admin-prohibited-filtering", 781),
          ("host-precedence-violation", 782),
          ("precedence-cutoff-in-effect", 783),
          ("source-quench", 1024),
          ("redirect-for-network", 1280),
          ("redirect-for-type-of-service-and-host", 1283),
          ("echo-request", 2048),
          ("router-advertisement", 2304),
          ("time-to-live-equals-0-during-reassembly", 2817),
          ("bad-ip-header", 3072),
          ("required-option-missing", 3073),
          ("timestamp-requested", 3328),
          ("timestamp-reply", 3584),
          ("address-mask-request", 4352),
          ("address-mask-reply", 4608),
          ("traceroute-outbound-packet-successfully-fw", 7680),
          ("traceroute-no-route-for-outbound-packet", 7681),
          ("domain-name-request", 9472),
          ("domain-name-reply", 9728),
          ("skip-algorithm-discovery-protocol", 9984),
          ("unreachable", 66304),
          ("redirect", 66816),
          ("time-exceeded", 68352),
          ("parameters-problem", 68608),
          ("traceroute", 73216),
          ("conversion-errors", 73472),
          ("mobile-host-redirect", 73728),
          ("ipv6-where-are-you", 73984),
          ("ipv6-I-am-here", 74240),
          ("mobile-registration-request", 74496),
          ("mobile-registration-reply", 74752),
          ("security-failure", 75776),
          ("any", 196608),
          ("not-supported", 262144))
    )


_IpPolicyQueryIcmpTypeCode_Type.__name__ = "Integer32"
_IpPolicyQueryIcmpTypeCode_Object = MibTableColumn
ipPolicyQueryIcmpTypeCode = _IpPolicyQueryIcmpTypeCode_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 16),
    _IpPolicyQueryIcmpTypeCode_Type()
)
ipPolicyQueryIcmpTypeCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyQueryIcmpTypeCode.setStatus("current")


class _IpPolicyQueryIpFragments_Type(Integer32):
    """Custom type ipPolicyQueryIpFragments based on Integer32"""
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
        *(("not-fragment", 1),
          ("fragment-first-packet", 2),
          ("fragment-non-first-packet", 3))
    )


_IpPolicyQueryIpFragments_Type.__name__ = "Integer32"
_IpPolicyQueryIpFragments_Object = MibTableColumn
ipPolicyQueryIpFragments = _IpPolicyQueryIpFragments_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 17),
    _IpPolicyQueryIpFragments_Type()
)
ipPolicyQueryIpFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyQueryIpFragments.setStatus("current")


class _IpPolicyQueryIpOption_Type(TruthValue):
    """Custom type ipPolicyQueryIpOption based on TruthValue"""
    defaultValue = 2


_IpPolicyQueryIpOption_Type.__name__ = "TruthValue"
_IpPolicyQueryIpOption_Object = MibTableColumn
ipPolicyQueryIpOption = _IpPolicyQueryIpOption_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 18),
    _IpPolicyQueryIpOption_Type()
)
ipPolicyQueryIpOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyQueryIpOption.setStatus("current")


class _IpPolicyQueryAccessOperation_Type(Integer32):
    """Custom type ipPolicyQueryAccessOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-supported", 0),
          ("permit", 1),
          ("deny", 2))
    )


_IpPolicyQueryAccessOperation_Type.__name__ = "Integer32"
_IpPolicyQueryAccessOperation_Object = MibTableColumn
ipPolicyQueryAccessOperation = _IpPolicyQueryAccessOperation_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 19),
    _IpPolicyQueryAccessOperation_Type()
)
ipPolicyQueryAccessOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyQueryAccessOperation.setStatus("current")


class _IpPolicyQueryNotifyOperation_Type(Integer32):
    """Custom type ipPolicyQueryNotifyOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-supported", 0),
          ("ignore", 1),
          ("notify", 2))
    )


_IpPolicyQueryNotifyOperation_Type.__name__ = "Integer32"
_IpPolicyQueryNotifyOperation_Object = MibTableColumn
ipPolicyQueryNotifyOperation = _IpPolicyQueryNotifyOperation_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 20),
    _IpPolicyQueryNotifyOperation_Type()
)
ipPolicyQueryNotifyOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyQueryNotifyOperation.setStatus("current")


class _IpPolicyQueryErrorReplyOperation_Type(Integer32):
    """Custom type ipPolicyQueryErrorReplyOperation based on Integer32"""
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
        *(("not-supported", 0),
          ("disable", 1),
          ("tcp-reset", 2),
          ("icmp-unreachable", 3))
    )


_IpPolicyQueryErrorReplyOperation_Type.__name__ = "Integer32"
_IpPolicyQueryErrorReplyOperation_Object = MibTableColumn
ipPolicyQueryErrorReplyOperation = _IpPolicyQueryErrorReplyOperation_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 21),
    _IpPolicyQueryErrorReplyOperation_Type()
)
ipPolicyQueryErrorReplyOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyQueryErrorReplyOperation.setStatus("current")


class _IpPolicyQueryCoSOperation_Type(Integer32):
    """Custom type ipPolicyQueryCoSOperation based on Integer32"""
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
        *(("not-supported", 0),
          ("cos0", 1),
          ("cos1", 2),
          ("cos2", 3),
          ("cos3", 4),
          ("cos4", 5),
          ("cos5", 6),
          ("cos6", 7),
          ("cos7", 8),
          ("no-change", 9))
    )


_IpPolicyQueryCoSOperation_Type.__name__ = "Integer32"
_IpPolicyQueryCoSOperation_Object = MibTableColumn
ipPolicyQueryCoSOperation = _IpPolicyQueryCoSOperation_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 22),
    _IpPolicyQueryCoSOperation_Type()
)
ipPolicyQueryCoSOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyQueryCoSOperation.setStatus("current")
_IpPolicyDiffServControlTable_Object = MibTable
ipPolicyDiffServControlTable = _IpPolicyDiffServControlTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 6)
)
if mibBuilder.loadTexts:
    ipPolicyDiffServControlTable.setStatus("obsolete")
_IpPolicyDiffServControlEntry_Object = MibTableRow
ipPolicyDiffServControlEntry = _IpPolicyDiffServControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 6, 1)
)
ipPolicyDiffServControlEntry.setIndexNames(
    (0, "POLICY-MIB", "ipPolicyDiffServSlot"),
)
if mibBuilder.loadTexts:
    ipPolicyDiffServControlEntry.setStatus("obsolete")


class _IpPolicyDiffServControlSlot_Type(Integer32):
    """Custom type ipPolicyDiffServControlSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyDiffServControlSlot_Type.__name__ = "Integer32"
_IpPolicyDiffServControlSlot_Object = MibTableColumn
ipPolicyDiffServControlSlot = _IpPolicyDiffServControlSlot_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 6, 1, 1),
    _IpPolicyDiffServControlSlot_Type()
)
ipPolicyDiffServControlSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyDiffServControlSlot.setStatus("obsolete")
_IpPolicyDiffServControlChecksum_Type = Integer32
_IpPolicyDiffServControlChecksum_Object = MibTableColumn
ipPolicyDiffServControlChecksum = _IpPolicyDiffServControlChecksum_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 6, 1, 2),
    _IpPolicyDiffServControlChecksum_Type()
)
ipPolicyDiffServControlChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyDiffServControlChecksum.setStatus("obsolete")


class _IpPolicyDiffServControlTrustedFields_Type(Integer32):
    """Custom type ipPolicyDiffServControlTrustedFields based on Integer32"""
    defaultValue = 2

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
        *(("cos", 1),
          ("dscp", 2),
          ("cos-dscp", 3),
          ("untrust", 4))
    )


_IpPolicyDiffServControlTrustedFields_Type.__name__ = "Integer32"
_IpPolicyDiffServControlTrustedFields_Object = MibTableColumn
ipPolicyDiffServControlTrustedFields = _IpPolicyDiffServControlTrustedFields_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 6, 1, 3),
    _IpPolicyDiffServControlTrustedFields_Type()
)
ipPolicyDiffServControlTrustedFields.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyDiffServControlTrustedFields.setStatus("obsolete")


class _IpPolicyDiffServControlValidityStatus_Type(Integer32):
    """Custom type ipPolicyDiffServControlValidityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_IpPolicyDiffServControlValidityStatus_Type.__name__ = "Integer32"
_IpPolicyDiffServControlValidityStatus_Object = MibTableColumn
ipPolicyDiffServControlValidityStatus = _IpPolicyDiffServControlValidityStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 6, 1, 4),
    _IpPolicyDiffServControlValidityStatus_Type()
)
ipPolicyDiffServControlValidityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyDiffServControlValidityStatus.setStatus("obsolete")


class _IpPolicyDiffServControlErrMsg_Type(DisplayString):
    """Custom type ipPolicyDiffServControlErrMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IpPolicyDiffServControlErrMsg_Type.__name__ = "DisplayString"
_IpPolicyDiffServControlErrMsg_Object = MibTableColumn
ipPolicyDiffServControlErrMsg = _IpPolicyDiffServControlErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 6, 1, 5),
    _IpPolicyDiffServControlErrMsg_Type()
)
ipPolicyDiffServControlErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyDiffServControlErrMsg.setStatus("obsolete")
_IpPolicyAccessControlViolationTable_Object = MibTable
ipPolicyAccessControlViolationTable = _IpPolicyAccessControlViolationTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 7)
)
if mibBuilder.loadTexts:
    ipPolicyAccessControlViolationTable.setStatus("current")
_IpPolicyAccessControlViolationEntry_Object = MibTableRow
ipPolicyAccessControlViolationEntry = _IpPolicyAccessControlViolationEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 7, 1)
)
ipPolicyAccessControlViolationEntry.setIndexNames(
    (0, "POLICY-MIB", "ipPolicyAccessControlViolationEntID"),
)
if mibBuilder.loadTexts:
    ipPolicyAccessControlViolationEntry.setStatus("current")


class _IpPolicyAccessControlViolationEntID_Type(Integer32):
    """Custom type ipPolicyAccessControlViolationEntID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyAccessControlViolationEntID_Type.__name__ = "Integer32"
_IpPolicyAccessControlViolationEntID_Object = MibTableColumn
ipPolicyAccessControlViolationEntID = _IpPolicyAccessControlViolationEntID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 7, 1, 1),
    _IpPolicyAccessControlViolationEntID_Type()
)
ipPolicyAccessControlViolationEntID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyAccessControlViolationEntID.setStatus("current")
_IpPolicyAccessControlViolationSrcAddr_Type = IpAddress
_IpPolicyAccessControlViolationSrcAddr_Object = MibTableColumn
ipPolicyAccessControlViolationSrcAddr = _IpPolicyAccessControlViolationSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 7, 1, 2),
    _IpPolicyAccessControlViolationSrcAddr_Type()
)
ipPolicyAccessControlViolationSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyAccessControlViolationSrcAddr.setStatus("current")
_IpPolicyAccessControlViolationDstAddr_Type = IpAddress
_IpPolicyAccessControlViolationDstAddr_Object = MibTableColumn
ipPolicyAccessControlViolationDstAddr = _IpPolicyAccessControlViolationDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 7, 1, 3),
    _IpPolicyAccessControlViolationDstAddr_Type()
)
ipPolicyAccessControlViolationDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyAccessControlViolationDstAddr.setStatus("current")


class _IpPolicyAccessControlViolationProtocol_Type(Integer32):
    """Custom type ipPolicyAccessControlViolationProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IpPolicyAccessControlViolationProtocol_Type.__name__ = "Integer32"
_IpPolicyAccessControlViolationProtocol_Object = MibTableColumn
ipPolicyAccessControlViolationProtocol = _IpPolicyAccessControlViolationProtocol_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 7, 1, 4),
    _IpPolicyAccessControlViolationProtocol_Type()
)
ipPolicyAccessControlViolationProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyAccessControlViolationProtocol.setStatus("current")


class _IpPolicyAccessControlViolationL4SrcPort_Type(Integer32):
    """Custom type ipPolicyAccessControlViolationL4SrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_IpPolicyAccessControlViolationL4SrcPort_Type.__name__ = "Integer32"
_IpPolicyAccessControlViolationL4SrcPort_Object = MibTableColumn
ipPolicyAccessControlViolationL4SrcPort = _IpPolicyAccessControlViolationL4SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 7, 1, 5),
    _IpPolicyAccessControlViolationL4SrcPort_Type()
)
ipPolicyAccessControlViolationL4SrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyAccessControlViolationL4SrcPort.setStatus("current")


class _IpPolicyAccessControlViolationL4DstPort_Type(Integer32):
    """Custom type ipPolicyAccessControlViolationL4DstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpPolicyAccessControlViolationL4DstPort_Type.__name__ = "Integer32"
_IpPolicyAccessControlViolationL4DstPort_Object = MibTableColumn
ipPolicyAccessControlViolationL4DstPort = _IpPolicyAccessControlViolationL4DstPort_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 7, 1, 6),
    _IpPolicyAccessControlViolationL4DstPort_Type()
)
ipPolicyAccessControlViolationL4DstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyAccessControlViolationL4DstPort.setStatus("current")


class _IpPolicyAccessControlViolationEstablished_Type(Integer32):
    """Custom type ipPolicyAccessControlViolationEstablished based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("dontCare", 2),
          ("no", 3))
    )


_IpPolicyAccessControlViolationEstablished_Type.__name__ = "Integer32"
_IpPolicyAccessControlViolationEstablished_Object = MibTableColumn
ipPolicyAccessControlViolationEstablished = _IpPolicyAccessControlViolationEstablished_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 7, 1, 7),
    _IpPolicyAccessControlViolationEstablished_Type()
)
ipPolicyAccessControlViolationEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyAccessControlViolationEstablished.setStatus("current")


class _IpPolicyAccessControlViolationDSCP_Type(Integer32):
    """Custom type ipPolicyAccessControlViolationDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_IpPolicyAccessControlViolationDSCP_Type.__name__ = "Integer32"
_IpPolicyAccessControlViolationDSCP_Object = MibTableColumn
ipPolicyAccessControlViolationDSCP = _IpPolicyAccessControlViolationDSCP_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 7, 1, 8),
    _IpPolicyAccessControlViolationDSCP_Type()
)
ipPolicyAccessControlViolationDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyAccessControlViolationDSCP.setStatus("current")
_IpPolicyAccessControlViolationIfIndex_Type = Integer32
_IpPolicyAccessControlViolationIfIndex_Object = MibTableColumn
ipPolicyAccessControlViolationIfIndex = _IpPolicyAccessControlViolationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 7, 1, 9),
    _IpPolicyAccessControlViolationIfIndex_Type()
)
ipPolicyAccessControlViolationIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyAccessControlViolationIfIndex.setStatus("current")


class _IpPolicyAccessControlViolationSubCtxt_Type(Integer32):
    """Custom type ipPolicyAccessControlViolationSubCtxt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2))
    )


_IpPolicyAccessControlViolationSubCtxt_Type.__name__ = "Integer32"
_IpPolicyAccessControlViolationSubCtxt_Object = MibTableColumn
ipPolicyAccessControlViolationSubCtxt = _IpPolicyAccessControlViolationSubCtxt_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 7, 1, 10),
    _IpPolicyAccessControlViolationSubCtxt_Type()
)
ipPolicyAccessControlViolationSubCtxt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyAccessControlViolationSubCtxt.setStatus("current")
_IpPolicyAccessControlViolationTime_Type = TimeTicks
_IpPolicyAccessControlViolationTime_Object = MibTableColumn
ipPolicyAccessControlViolationTime = _IpPolicyAccessControlViolationTime_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 7, 1, 11),
    _IpPolicyAccessControlViolationTime_Type()
)
ipPolicyAccessControlViolationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyAccessControlViolationTime.setStatus("current")


class _IpPolicyAccessControlViolationRuleType_Type(Integer32):
    """Custom type ipPolicyAccessControlViolationRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ruleEntry", 1),
          ("ipOptionOperation", 2),
          ("ipFragmentationOperation", 3))
    )


_IpPolicyAccessControlViolationRuleType_Type.__name__ = "Integer32"
_IpPolicyAccessControlViolationRuleType_Object = MibTableColumn
ipPolicyAccessControlViolationRuleType = _IpPolicyAccessControlViolationRuleType_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 7, 1, 12),
    _IpPolicyAccessControlViolationRuleType_Type()
)
ipPolicyAccessControlViolationRuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyAccessControlViolationRuleType.setStatus("current")
_IpPolicyCompositeOpTable_Object = MibTable
ipPolicyCompositeOpTable = _IpPolicyCompositeOpTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 8)
)
if mibBuilder.loadTexts:
    ipPolicyCompositeOpTable.setStatus("current")
_IpPolicyCompositeOpEntry_Object = MibTableRow
ipPolicyCompositeOpEntry = _IpPolicyCompositeOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 8, 1)
)
ipPolicyCompositeOpEntry.setIndexNames(
    (0, "POLICY-MIB", "ipPolicyCompositeOpEntID"),
    (0, "POLICY-MIB", "ipPolicyCompositeOpListID"),
    (0, "POLICY-MIB", "ipPolicyCompositeOpID"),
)
if mibBuilder.loadTexts:
    ipPolicyCompositeOpEntry.setStatus("current")


class _IpPolicyCompositeOpEntID_Type(Integer32):
    """Custom type ipPolicyCompositeOpEntID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_IpPolicyCompositeOpEntID_Type.__name__ = "Integer32"
_IpPolicyCompositeOpEntID_Object = MibTableColumn
ipPolicyCompositeOpEntID = _IpPolicyCompositeOpEntID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 8, 1, 1),
    _IpPolicyCompositeOpEntID_Type()
)
ipPolicyCompositeOpEntID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyCompositeOpEntID.setStatus("current")


class _IpPolicyCompositeOpListID_Type(Integer32):
    """Custom type ipPolicyCompositeOpListID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyCompositeOpListID_Type.__name__ = "Integer32"
_IpPolicyCompositeOpListID_Object = MibTableColumn
ipPolicyCompositeOpListID = _IpPolicyCompositeOpListID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 8, 1, 2),
    _IpPolicyCompositeOpListID_Type()
)
ipPolicyCompositeOpListID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyCompositeOpListID.setStatus("current")


class _IpPolicyCompositeOpID_Type(Integer32):
    """Custom type ipPolicyCompositeOpID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_IpPolicyCompositeOpID_Type.__name__ = "Integer32"
_IpPolicyCompositeOpID_Object = MibTableColumn
ipPolicyCompositeOpID = _IpPolicyCompositeOpID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 8, 1, 3),
    _IpPolicyCompositeOpID_Type()
)
ipPolicyCompositeOpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyCompositeOpID.setStatus("current")


class _IpPolicyCompositeOpName_Type(DisplayString):
    """Custom type ipPolicyCompositeOpName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IpPolicyCompositeOpName_Type.__name__ = "DisplayString"
_IpPolicyCompositeOpName_Object = MibTableColumn
ipPolicyCompositeOpName = _IpPolicyCompositeOpName_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 8, 1, 4),
    _IpPolicyCompositeOpName_Type()
)
ipPolicyCompositeOpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyCompositeOpName.setStatus("current")


class _IpPolicyCompositeOp802priority_Type(Integer32):
    """Custom type ipPolicyCompositeOp802priority based on Integer32"""
    defaultValue = 9

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
              255)
        )
    )
    namedValues = NamedValues(
        *(("cos0", 1),
          ("cos1", 2),
          ("cos2", 3),
          ("cos3", 4),
          ("cos4", 5),
          ("cos5", 6),
          ("cos6", 7),
          ("cos7", 8),
          ("no-change", 9),
          ("not-supported", 255))
    )


_IpPolicyCompositeOp802priority_Type.__name__ = "Integer32"
_IpPolicyCompositeOp802priority_Object = MibTableColumn
ipPolicyCompositeOp802priority = _IpPolicyCompositeOp802priority_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 8, 1, 5),
    _IpPolicyCompositeOp802priority_Type()
)
ipPolicyCompositeOp802priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyCompositeOp802priority.setStatus("current")


class _IpPolicyCompositeOpAccess_Type(Integer32):
    """Custom type ipPolicyCompositeOpAccess based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2),
          ("not-supported", 255))
    )


_IpPolicyCompositeOpAccess_Type.__name__ = "Integer32"
_IpPolicyCompositeOpAccess_Object = MibTableColumn
ipPolicyCompositeOpAccess = _IpPolicyCompositeOpAccess_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 8, 1, 6),
    _IpPolicyCompositeOpAccess_Type()
)
ipPolicyCompositeOpAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyCompositeOpAccess.setStatus("current")


class _IpPolicyCompositeOpDscp_Type(Integer32):
    """Custom type ipPolicyCompositeOpDscp based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
        ValueRangeConstraint(255, 255),
    )


_IpPolicyCompositeOpDscp_Type.__name__ = "Integer32"
_IpPolicyCompositeOpDscp_Object = MibTableColumn
ipPolicyCompositeOpDscp = _IpPolicyCompositeOpDscp_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 8, 1, 7),
    _IpPolicyCompositeOpDscp_Type()
)
ipPolicyCompositeOpDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyCompositeOpDscp.setStatus("current")


class _IpPolicyCompositeOpRSGQualityClass_Type(Integer32):
    """Custom type ipPolicyCompositeOpRSGQualityClass based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpPolicyCompositeOpRSGQualityClass_Type.__name__ = "Integer32"
_IpPolicyCompositeOpRSGQualityClass_Object = MibTableColumn
ipPolicyCompositeOpRSGQualityClass = _IpPolicyCompositeOpRSGQualityClass_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 8, 1, 8),
    _IpPolicyCompositeOpRSGQualityClass_Type()
)
ipPolicyCompositeOpRSGQualityClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyCompositeOpRSGQualityClass.setStatus("current")


class _IpPolicyCompositeOpNotify_Type(Integer32):
    """Custom type ipPolicyCompositeOpNotify based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("notify", 2),
          ("not-supported", 255))
    )


_IpPolicyCompositeOpNotify_Type.__name__ = "Integer32"
_IpPolicyCompositeOpNotify_Object = MibTableColumn
ipPolicyCompositeOpNotify = _IpPolicyCompositeOpNotify_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 8, 1, 9),
    _IpPolicyCompositeOpNotify_Type()
)
ipPolicyCompositeOpNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyCompositeOpNotify.setStatus("current")
_IpPolicyCompositeOpRowStatus_Type = RowStatus
_IpPolicyCompositeOpRowStatus_Object = MibTableColumn
ipPolicyCompositeOpRowStatus = _IpPolicyCompositeOpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 8, 1, 10),
    _IpPolicyCompositeOpRowStatus_Type()
)
ipPolicyCompositeOpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyCompositeOpRowStatus.setStatus("current")


class _IpPolicyCompositeOpErrorReply_Type(Integer32):
    """Custom type ipPolicyCompositeOpErrorReply based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("auto", 2),
          ("not-supported", 255))
    )


_IpPolicyCompositeOpErrorReply_Type.__name__ = "Integer32"
_IpPolicyCompositeOpErrorReply_Object = MibTableColumn
ipPolicyCompositeOpErrorReply = _IpPolicyCompositeOpErrorReply_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 8, 1, 11),
    _IpPolicyCompositeOpErrorReply_Type()
)
ipPolicyCompositeOpErrorReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyCompositeOpErrorReply.setStatus("current")


class _IpPolicyCompositeOpTrustDscp_Type(Integer32):
    """Custom type ipPolicyCompositeOpTrustDscp based on Integer32"""
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
        *(("no", 1),
          ("dscp-only", 2),
          ("dscp-and-cos", 3))
    )


_IpPolicyCompositeOpTrustDscp_Type.__name__ = "Integer32"
_IpPolicyCompositeOpTrustDscp_Object = MibTableColumn
ipPolicyCompositeOpTrustDscp = _IpPolicyCompositeOpTrustDscp_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 8, 1, 12),
    _IpPolicyCompositeOpTrustDscp_Type()
)
ipPolicyCompositeOpTrustDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyCompositeOpTrustDscp.setStatus("current")
_IpPolicyDSCPmapTable_Object = MibTable
ipPolicyDSCPmapTable = _IpPolicyDSCPmapTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 9)
)
if mibBuilder.loadTexts:
    ipPolicyDSCPmapTable.setStatus("current")
_IpPolicyDSCPmapEntry_Object = MibTableRow
ipPolicyDSCPmapEntry = _IpPolicyDSCPmapEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 9, 1)
)
ipPolicyDSCPmapEntry.setIndexNames(
    (0, "POLICY-MIB", "ipPolicyDSCPmapEntID"),
    (0, "POLICY-MIB", "ipPolicyDSCPmapListID"),
    (0, "POLICY-MIB", "ipPolicyDSCPmapDSCP"),
)
if mibBuilder.loadTexts:
    ipPolicyDSCPmapEntry.setStatus("current")


class _IpPolicyDSCPmapEntID_Type(Integer32):
    """Custom type ipPolicyDSCPmapEntID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyDSCPmapEntID_Type.__name__ = "Integer32"
_IpPolicyDSCPmapEntID_Object = MibTableColumn
ipPolicyDSCPmapEntID = _IpPolicyDSCPmapEntID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 9, 1, 1),
    _IpPolicyDSCPmapEntID_Type()
)
ipPolicyDSCPmapEntID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyDSCPmapEntID.setStatus("current")


class _IpPolicyDSCPmapListID_Type(Integer32):
    """Custom type ipPolicyDSCPmapListID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_IpPolicyDSCPmapListID_Type.__name__ = "Integer32"
_IpPolicyDSCPmapListID_Object = MibTableColumn
ipPolicyDSCPmapListID = _IpPolicyDSCPmapListID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 9, 1, 2),
    _IpPolicyDSCPmapListID_Type()
)
ipPolicyDSCPmapListID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyDSCPmapListID.setStatus("current")


class _IpPolicyDSCPmapDSCP_Type(Integer32):
    """Custom type ipPolicyDSCPmapDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_IpPolicyDSCPmapDSCP_Type.__name__ = "Integer32"
_IpPolicyDSCPmapDSCP_Object = MibTableColumn
ipPolicyDSCPmapDSCP = _IpPolicyDSCPmapDSCP_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 9, 1, 3),
    _IpPolicyDSCPmapDSCP_Type()
)
ipPolicyDSCPmapDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyDSCPmapDSCP.setStatus("current")


class _IpPolicyDSCPmapOperation_Type(Integer32):
    """Custom type ipPolicyDSCPmapOperation based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_IpPolicyDSCPmapOperation_Type.__name__ = "Integer32"
_IpPolicyDSCPmapOperation_Object = MibTableColumn
ipPolicyDSCPmapOperation = _IpPolicyDSCPmapOperation_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 9, 1, 4),
    _IpPolicyDSCPmapOperation_Type()
)
ipPolicyDSCPmapOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyDSCPmapOperation.setStatus("current")


class _IpPolicyDSCPmapName_Type(DisplayString):
    """Custom type ipPolicyDSCPmapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpPolicyDSCPmapName_Type.__name__ = "DisplayString"
_IpPolicyDSCPmapName_Object = MibTableColumn
ipPolicyDSCPmapName = _IpPolicyDSCPmapName_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 9, 1, 5),
    _IpPolicyDSCPmapName_Type()
)
ipPolicyDSCPmapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyDSCPmapName.setStatus("current")


class _IpPolicyDSCPmapApplicabilityPrecedence_Type(Integer32):
    """Custom type ipPolicyDSCPmapApplicabilityPrecedence based on Integer32"""
    defaultValue = 9999

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_IpPolicyDSCPmapApplicabilityPrecedence_Type.__name__ = "Integer32"
_IpPolicyDSCPmapApplicabilityPrecedence_Object = MibTableColumn
ipPolicyDSCPmapApplicabilityPrecedence = _IpPolicyDSCPmapApplicabilityPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 9, 1, 6),
    _IpPolicyDSCPmapApplicabilityPrecedence_Type()
)
ipPolicyDSCPmapApplicabilityPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyDSCPmapApplicabilityPrecedence.setStatus("current")


class _IpPolicyDSCPmapApplicabilityStatus_Type(Integer32):
    """Custom type ipPolicyDSCPmapApplicabilityStatus based on Integer32"""
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
        *(("applicable", 1),
          ("partiallyApplicable", 2),
          ("notApplicable", 3),
          ("unknown", 4))
    )


_IpPolicyDSCPmapApplicabilityStatus_Type.__name__ = "Integer32"
_IpPolicyDSCPmapApplicabilityStatus_Object = MibTableColumn
ipPolicyDSCPmapApplicabilityStatus = _IpPolicyDSCPmapApplicabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 9, 1, 7),
    _IpPolicyDSCPmapApplicabilityStatus_Type()
)
ipPolicyDSCPmapApplicabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyDSCPmapApplicabilityStatus.setStatus("obsolete")


class _IpPolicyDSCPmapApplicabilityType_Type(Integer32):
    """Custom type ipPolicyDSCPmapApplicabilityType based on Integer32"""
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
        *(("static", 1),
          ("quasiStatic", 2),
          ("dynamic", 3),
          ("unknown", 4))
    )


_IpPolicyDSCPmapApplicabilityType_Type.__name__ = "Integer32"
_IpPolicyDSCPmapApplicabilityType_Object = MibTableColumn
ipPolicyDSCPmapApplicabilityType = _IpPolicyDSCPmapApplicabilityType_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 9, 1, 8),
    _IpPolicyDSCPmapApplicabilityType_Type()
)
ipPolicyDSCPmapApplicabilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyDSCPmapApplicabilityType.setStatus("obsolete")


class _IpPolicyDSCPmapErrMsg_Type(DisplayString):
    """Custom type ipPolicyDSCPmapErrMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IpPolicyDSCPmapErrMsg_Type.__name__ = "DisplayString"
_IpPolicyDSCPmapErrMsg_Object = MibTableColumn
ipPolicyDSCPmapErrMsg = _IpPolicyDSCPmapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 9, 1, 9),
    _IpPolicyDSCPmapErrMsg_Type()
)
ipPolicyDSCPmapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyDSCPmapErrMsg.setStatus("obsolete")
_IpPolicyActivationTable_Object = MibTable
ipPolicyActivationTable = _IpPolicyActivationTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 10)
)
if mibBuilder.loadTexts:
    ipPolicyActivationTable.setStatus("current")
_IpPolicyActivationEntry_Object = MibTableRow
ipPolicyActivationEntry = _IpPolicyActivationEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 10, 1)
)
ipPolicyActivationEntry.setIndexNames(
    (0, "POLICY-MIB", "ipPolicyActivationEntID"),
    (0, "POLICY-MIB", "ipPolicyActivationifIndex"),
    (0, "POLICY-MIB", "ipPolicyActivationSubContext"),
)
if mibBuilder.loadTexts:
    ipPolicyActivationEntry.setStatus("current")


class _IpPolicyActivationEntID_Type(Integer32):
    """Custom type ipPolicyActivationEntID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyActivationEntID_Type.__name__ = "Integer32"
_IpPolicyActivationEntID_Object = MibTableColumn
ipPolicyActivationEntID = _IpPolicyActivationEntID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 10, 1, 1),
    _IpPolicyActivationEntID_Type()
)
ipPolicyActivationEntID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyActivationEntID.setStatus("current")


class _IpPolicyActivationifIndex_Type(Integer32):
    """Custom type ipPolicyActivationifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyActivationifIndex_Type.__name__ = "Integer32"
_IpPolicyActivationifIndex_Object = MibTableColumn
ipPolicyActivationifIndex = _IpPolicyActivationifIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 10, 1, 2),
    _IpPolicyActivationifIndex_Type()
)
ipPolicyActivationifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyActivationifIndex.setStatus("current")
_IpPolicyActivationSubContext_Type = SubContextTypes
_IpPolicyActivationSubContext_Object = MibTableColumn
ipPolicyActivationSubContext = _IpPolicyActivationSubContext_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 10, 1, 3),
    _IpPolicyActivationSubContext_Type()
)
ipPolicyActivationSubContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyActivationSubContext.setStatus("current")
_IpPolicyActivationSubContextName_Type = OctetString
_IpPolicyActivationSubContextName_Object = MibTableColumn
ipPolicyActivationSubContextName = _IpPolicyActivationSubContextName_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 10, 1, 4),
    _IpPolicyActivationSubContextName_Type()
)
ipPolicyActivationSubContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyActivationSubContextName.setStatus("current")


class _IpPolicyActivationList_Type(Integer32):
    """Custom type ipPolicyActivationList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyActivationList_Type.__name__ = "Integer32"
_IpPolicyActivationList_Object = MibTableColumn
ipPolicyActivationList = _IpPolicyActivationList_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 10, 1, 5),
    _IpPolicyActivationList_Type()
)
ipPolicyActivationList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyActivationList.setStatus("current")


class _IpPolicyActivationAclList_Type(Integer32):
    """Custom type ipPolicyActivationAclList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyActivationAclList_Type.__name__ = "Integer32"
_IpPolicyActivationAclList_Object = MibTableColumn
ipPolicyActivationAclList = _IpPolicyActivationAclList_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 10, 1, 6),
    _IpPolicyActivationAclList_Type()
)
ipPolicyActivationAclList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyActivationAclList.setStatus("current")


class _IpPolicyActivationQoSList_Type(Integer32):
    """Custom type ipPolicyActivationQoSList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyActivationQoSList_Type.__name__ = "Integer32"
_IpPolicyActivationQoSList_Object = MibTableColumn
ipPolicyActivationQoSList = _IpPolicyActivationQoSList_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 10, 1, 7),
    _IpPolicyActivationQoSList_Type()
)
ipPolicyActivationQoSList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyActivationQoSList.setStatus("current")


class _IpPolicyActivationSourceNatList_Type(Integer32):
    """Custom type ipPolicyActivationSourceNatList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyActivationSourceNatList_Type.__name__ = "Integer32"
_IpPolicyActivationSourceNatList_Object = MibTableColumn
ipPolicyActivationSourceNatList = _IpPolicyActivationSourceNatList_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 10, 1, 8),
    _IpPolicyActivationSourceNatList_Type()
)
ipPolicyActivationSourceNatList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyActivationSourceNatList.setStatus("current")


class _IpPolicyActivationDestinationNatList_Type(Integer32):
    """Custom type ipPolicyActivationDestinationNatList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyActivationDestinationNatList_Type.__name__ = "Integer32"
_IpPolicyActivationDestinationNatList_Object = MibTableColumn
ipPolicyActivationDestinationNatList = _IpPolicyActivationDestinationNatList_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 10, 1, 9),
    _IpPolicyActivationDestinationNatList_Type()
)
ipPolicyActivationDestinationNatList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyActivationDestinationNatList.setStatus("current")


class _IpPolicyActivationAntiSpoofignList_Type(Integer32):
    """Custom type ipPolicyActivationAntiSpoofignList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyActivationAntiSpoofignList_Type.__name__ = "Integer32"
_IpPolicyActivationAntiSpoofignList_Object = MibTableColumn
ipPolicyActivationAntiSpoofignList = _IpPolicyActivationAntiSpoofignList_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 10, 1, 10),
    _IpPolicyActivationAntiSpoofignList_Type()
)
ipPolicyActivationAntiSpoofignList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyActivationAntiSpoofignList.setStatus("current")


class _IpPolicyActivationPBRList_Type(Integer32):
    """Custom type ipPolicyActivationPBRList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyActivationPBRList_Type.__name__ = "Integer32"
_IpPolicyActivationPBRList_Object = MibTableColumn
ipPolicyActivationPBRList = _IpPolicyActivationPBRList_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 10, 1, 11),
    _IpPolicyActivationPBRList_Type()
)
ipPolicyActivationPBRList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyActivationPBRList.setStatus("current")


class _IpPolicyActivationCryptoList_Type(Integer32):
    """Custom type ipPolicyActivationCryptoList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyActivationCryptoList_Type.__name__ = "Integer32"
_IpPolicyActivationCryptoList_Object = MibTableColumn
ipPolicyActivationCryptoList = _IpPolicyActivationCryptoList_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 10, 1, 12),
    _IpPolicyActivationCryptoList_Type()
)
ipPolicyActivationCryptoList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyActivationCryptoList.setStatus("current")
_IpPolicyValidation_ObjectIdentity = ObjectIdentity
ipPolicyValidation = _IpPolicyValidation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 36, 11)
)
_IpPolicyValidListTable_Object = MibTable
ipPolicyValidListTable = _IpPolicyValidListTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 1)
)
if mibBuilder.loadTexts:
    ipPolicyValidListTable.setStatus("current")
_IpPolicyValidListEntry_Object = MibTableRow
ipPolicyValidListEntry = _IpPolicyValidListEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 1, 1)
)
ipPolicyValidListEntry.setIndexNames(
    (0, "POLICY-MIB", "ipPolicyValidListEntID"),
    (0, "POLICY-MIB", "ipPolicyValidListIfIndex"),
    (0, "POLICY-MIB", "ipPolicyValidListSubContext"),
    (0, "POLICY-MIB", "ipPolicyValidListListID"),
)
if mibBuilder.loadTexts:
    ipPolicyValidListEntry.setStatus("current")


class _IpPolicyValidListEntID_Type(Integer32):
    """Custom type ipPolicyValidListEntID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyValidListEntID_Type.__name__ = "Integer32"
_IpPolicyValidListEntID_Object = MibTableColumn
ipPolicyValidListEntID = _IpPolicyValidListEntID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 1, 1, 1),
    _IpPolicyValidListEntID_Type()
)
ipPolicyValidListEntID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidListEntID.setStatus("current")


class _IpPolicyValidListIfIndex_Type(Integer32):
    """Custom type ipPolicyValidListIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyValidListIfIndex_Type.__name__ = "Integer32"
_IpPolicyValidListIfIndex_Object = MibTableColumn
ipPolicyValidListIfIndex = _IpPolicyValidListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 1, 1, 2),
    _IpPolicyValidListIfIndex_Type()
)
ipPolicyValidListIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidListIfIndex.setStatus("current")
_IpPolicyValidListSubContext_Type = SubContextTypes
_IpPolicyValidListSubContext_Object = MibTableColumn
ipPolicyValidListSubContext = _IpPolicyValidListSubContext_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 1, 1, 3),
    _IpPolicyValidListSubContext_Type()
)
ipPolicyValidListSubContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidListSubContext.setStatus("current")


class _IpPolicyValidListListID_Type(Integer32):
    """Custom type ipPolicyValidListListID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyValidListListID_Type.__name__ = "Integer32"
_IpPolicyValidListListID_Object = MibTableColumn
ipPolicyValidListListID = _IpPolicyValidListListID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 1, 1, 4),
    _IpPolicyValidListListID_Type()
)
ipPolicyValidListListID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidListListID.setStatus("current")


class _IpPolicyValidListStatus_Type(Integer32):
    """Custom type ipPolicyValidListStatus based on Integer32"""
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
        *(("valid", 1),
          ("partiallyValid", 2),
          ("invalid", 3),
          ("validationInProgress", 4))
    )


_IpPolicyValidListStatus_Type.__name__ = "Integer32"
_IpPolicyValidListStatus_Object = MibTableColumn
ipPolicyValidListStatus = _IpPolicyValidListStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 1, 1, 5),
    _IpPolicyValidListStatus_Type()
)
ipPolicyValidListStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidListStatus.setStatus("current")


class _IpPolicyValidListErrMsg_Type(DisplayString):
    """Custom type ipPolicyValidListErrMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IpPolicyValidListErrMsg_Type.__name__ = "DisplayString"
_IpPolicyValidListErrMsg_Object = MibTableColumn
ipPolicyValidListErrMsg = _IpPolicyValidListErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 1, 1, 6),
    _IpPolicyValidListErrMsg_Type()
)
ipPolicyValidListErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidListErrMsg.setStatus("current")
_IpPolicyValidListIpOption_Type = TruthValue
_IpPolicyValidListIpOption_Object = MibTableColumn
ipPolicyValidListIpOption = _IpPolicyValidListIpOption_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 1, 1, 7),
    _IpPolicyValidListIpOption_Type()
)
ipPolicyValidListIpOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidListIpOption.setStatus("current")
_IpPolicyValidListIpFragmentation_Type = TruthValue
_IpPolicyValidListIpFragmentation_Object = MibTableColumn
ipPolicyValidListIpFragmentation = _IpPolicyValidListIpFragmentation_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 1, 1, 8),
    _IpPolicyValidListIpFragmentation_Type()
)
ipPolicyValidListIpFragmentation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidListIpFragmentation.setStatus("current")
_IpPolicyValidRuleTable_Object = MibTable
ipPolicyValidRuleTable = _IpPolicyValidRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 2)
)
if mibBuilder.loadTexts:
    ipPolicyValidRuleTable.setStatus("current")
_IpPolicyValidRuleEntry_Object = MibTableRow
ipPolicyValidRuleEntry = _IpPolicyValidRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 2, 1)
)
ipPolicyValidRuleEntry.setIndexNames(
    (0, "POLICY-MIB", "ipPolicyValidRuleEntID"),
    (0, "POLICY-MIB", "ipPolicyValidRuleIfIndex"),
    (0, "POLICY-MIB", "ipPolicyValidRuleSubContext"),
    (0, "POLICY-MIB", "ipPolicyValidRuleListID"),
    (0, "POLICY-MIB", "ipPolicyValidRuleRuleID"),
)
if mibBuilder.loadTexts:
    ipPolicyValidRuleEntry.setStatus("current")


class _IpPolicyValidRuleEntID_Type(Integer32):
    """Custom type ipPolicyValidRuleEntID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyValidRuleEntID_Type.__name__ = "Integer32"
_IpPolicyValidRuleEntID_Object = MibTableColumn
ipPolicyValidRuleEntID = _IpPolicyValidRuleEntID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 2, 1, 1),
    _IpPolicyValidRuleEntID_Type()
)
ipPolicyValidRuleEntID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidRuleEntID.setStatus("current")


class _IpPolicyValidRuleIfIndex_Type(Integer32):
    """Custom type ipPolicyValidRuleIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyValidRuleIfIndex_Type.__name__ = "Integer32"
_IpPolicyValidRuleIfIndex_Object = MibTableColumn
ipPolicyValidRuleIfIndex = _IpPolicyValidRuleIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 2, 1, 2),
    _IpPolicyValidRuleIfIndex_Type()
)
ipPolicyValidRuleIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidRuleIfIndex.setStatus("current")
_IpPolicyValidRuleSubContext_Type = SubContextTypes
_IpPolicyValidRuleSubContext_Object = MibTableColumn
ipPolicyValidRuleSubContext = _IpPolicyValidRuleSubContext_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 2, 1, 3),
    _IpPolicyValidRuleSubContext_Type()
)
ipPolicyValidRuleSubContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidRuleSubContext.setStatus("current")


class _IpPolicyValidRuleListID_Type(Integer32):
    """Custom type ipPolicyValidRuleListID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyValidRuleListID_Type.__name__ = "Integer32"
_IpPolicyValidRuleListID_Object = MibTableColumn
ipPolicyValidRuleListID = _IpPolicyValidRuleListID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 2, 1, 4),
    _IpPolicyValidRuleListID_Type()
)
ipPolicyValidRuleListID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidRuleListID.setStatus("current")


class _IpPolicyValidRuleRuleID_Type(Integer32):
    """Custom type ipPolicyValidRuleRuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyValidRuleRuleID_Type.__name__ = "Integer32"
_IpPolicyValidRuleRuleID_Object = MibTableColumn
ipPolicyValidRuleRuleID = _IpPolicyValidRuleRuleID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 2, 1, 5),
    _IpPolicyValidRuleRuleID_Type()
)
ipPolicyValidRuleRuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidRuleRuleID.setStatus("current")


class _IpPolicyValidRuleStatus_Type(Integer32):
    """Custom type ipPolicyValidRuleStatus based on Integer32"""
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
        *(("applicable", 1),
          ("partiallyApplicable", 2),
          ("notApplicable", 3),
          ("unknown", 4))
    )


_IpPolicyValidRuleStatus_Type.__name__ = "Integer32"
_IpPolicyValidRuleStatus_Object = MibTableColumn
ipPolicyValidRuleStatus = _IpPolicyValidRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 2, 1, 6),
    _IpPolicyValidRuleStatus_Type()
)
ipPolicyValidRuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidRuleStatus.setStatus("current")


class _IpPolicyValidRuleApplicabilityType_Type(Integer32):
    """Custom type ipPolicyValidRuleApplicabilityType based on Integer32"""
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
        *(("static", 1),
          ("quasiStatic", 2),
          ("dynamic", 3),
          ("unknown", 4))
    )


_IpPolicyValidRuleApplicabilityType_Type.__name__ = "Integer32"
_IpPolicyValidRuleApplicabilityType_Object = MibTableColumn
ipPolicyValidRuleApplicabilityType = _IpPolicyValidRuleApplicabilityType_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 2, 1, 7),
    _IpPolicyValidRuleApplicabilityType_Type()
)
ipPolicyValidRuleApplicabilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidRuleApplicabilityType.setStatus("current")


class _IpPolicyValidRuleErrMsg_Type(DisplayString):
    """Custom type ipPolicyValidRuleErrMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IpPolicyValidRuleErrMsg_Type.__name__ = "DisplayString"
_IpPolicyValidRuleErrMsg_Object = MibTableColumn
ipPolicyValidRuleErrMsg = _IpPolicyValidRuleErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 2, 1, 8),
    _IpPolicyValidRuleErrMsg_Type()
)
ipPolicyValidRuleErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidRuleErrMsg.setStatus("current")
_IpPolicyValidDSCPTable_Object = MibTable
ipPolicyValidDSCPTable = _IpPolicyValidDSCPTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 3)
)
if mibBuilder.loadTexts:
    ipPolicyValidDSCPTable.setStatus("current")
_IpPolicyValidDSCPEntry_Object = MibTableRow
ipPolicyValidDSCPEntry = _IpPolicyValidDSCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 3, 1)
)
ipPolicyValidDSCPEntry.setIndexNames(
    (0, "POLICY-MIB", "ipPolicyValidDSCPEntID"),
    (0, "POLICY-MIB", "ipPolicyValidDSCPIfIndex"),
    (0, "POLICY-MIB", "ipPolicyValidDSCPSubContext"),
    (0, "POLICY-MIB", "ipPolicyValidDSCPListID"),
    (0, "POLICY-MIB", "ipPolicyValidDSCPvalue"),
)
if mibBuilder.loadTexts:
    ipPolicyValidDSCPEntry.setStatus("current")


class _IpPolicyValidDSCPEntID_Type(Integer32):
    """Custom type ipPolicyValidDSCPEntID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyValidDSCPEntID_Type.__name__ = "Integer32"
_IpPolicyValidDSCPEntID_Object = MibTableColumn
ipPolicyValidDSCPEntID = _IpPolicyValidDSCPEntID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 3, 1, 1),
    _IpPolicyValidDSCPEntID_Type()
)
ipPolicyValidDSCPEntID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidDSCPEntID.setStatus("current")


class _IpPolicyValidDSCPIfIndex_Type(Integer32):
    """Custom type ipPolicyValidDSCPIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyValidDSCPIfIndex_Type.__name__ = "Integer32"
_IpPolicyValidDSCPIfIndex_Object = MibTableColumn
ipPolicyValidDSCPIfIndex = _IpPolicyValidDSCPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 3, 1, 2),
    _IpPolicyValidDSCPIfIndex_Type()
)
ipPolicyValidDSCPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidDSCPIfIndex.setStatus("current")
_IpPolicyValidDSCPSubContext_Type = SubContextTypes
_IpPolicyValidDSCPSubContext_Object = MibTableColumn
ipPolicyValidDSCPSubContext = _IpPolicyValidDSCPSubContext_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 3, 1, 3),
    _IpPolicyValidDSCPSubContext_Type()
)
ipPolicyValidDSCPSubContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidDSCPSubContext.setStatus("current")


class _IpPolicyValidDSCPListID_Type(Integer32):
    """Custom type ipPolicyValidDSCPListID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyValidDSCPListID_Type.__name__ = "Integer32"
_IpPolicyValidDSCPListID_Object = MibTableColumn
ipPolicyValidDSCPListID = _IpPolicyValidDSCPListID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 3, 1, 4),
    _IpPolicyValidDSCPListID_Type()
)
ipPolicyValidDSCPListID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidDSCPListID.setStatus("current")


class _IpPolicyValidDSCPvalue_Type(Integer32):
    """Custom type ipPolicyValidDSCPvalue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyValidDSCPvalue_Type.__name__ = "Integer32"
_IpPolicyValidDSCPvalue_Object = MibTableColumn
ipPolicyValidDSCPvalue = _IpPolicyValidDSCPvalue_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 3, 1, 5),
    _IpPolicyValidDSCPvalue_Type()
)
ipPolicyValidDSCPvalue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidDSCPvalue.setStatus("current")


class _IpPolicyValidDSCPStatus_Type(Integer32):
    """Custom type ipPolicyValidDSCPStatus based on Integer32"""
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
        *(("applicable", 1),
          ("partiallyApplicable", 2),
          ("notApplicable", 3),
          ("unknown", 4))
    )


_IpPolicyValidDSCPStatus_Type.__name__ = "Integer32"
_IpPolicyValidDSCPStatus_Object = MibTableColumn
ipPolicyValidDSCPStatus = _IpPolicyValidDSCPStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 3, 1, 6),
    _IpPolicyValidDSCPStatus_Type()
)
ipPolicyValidDSCPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidDSCPStatus.setStatus("current")


class _IpPolicyValidDSCPApplicabilityType_Type(Integer32):
    """Custom type ipPolicyValidDSCPApplicabilityType based on Integer32"""
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
        *(("static", 1),
          ("quasiStatic", 2),
          ("dynamic", 3),
          ("unknown", 4))
    )


_IpPolicyValidDSCPApplicabilityType_Type.__name__ = "Integer32"
_IpPolicyValidDSCPApplicabilityType_Object = MibTableColumn
ipPolicyValidDSCPApplicabilityType = _IpPolicyValidDSCPApplicabilityType_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 3, 1, 7),
    _IpPolicyValidDSCPApplicabilityType_Type()
)
ipPolicyValidDSCPApplicabilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidDSCPApplicabilityType.setStatus("current")


class _IpPolicyValidDSCPErrMsg_Type(DisplayString):
    """Custom type ipPolicyValidDSCPErrMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IpPolicyValidDSCPErrMsg_Type.__name__ = "DisplayString"
_IpPolicyValidDSCPErrMsg_Object = MibTableColumn
ipPolicyValidDSCPErrMsg = _IpPolicyValidDSCPErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 3, 1, 8),
    _IpPolicyValidDSCPErrMsg_Type()
)
ipPolicyValidDSCPErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidDSCPErrMsg.setStatus("current")
_IpPolicyValidEtherTypeRuleTable_Object = MibTable
ipPolicyValidEtherTypeRuleTable = _IpPolicyValidEtherTypeRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 4)
)
if mibBuilder.loadTexts:
    ipPolicyValidEtherTypeRuleTable.setStatus("current")
_IpPolicyValidEtherTypeRuleEntry_Object = MibTableRow
ipPolicyValidEtherTypeRuleEntry = _IpPolicyValidEtherTypeRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 4, 1)
)
ipPolicyValidEtherTypeRuleEntry.setIndexNames(
    (0, "POLICY-MIB", "ipPolicyValidRuleEntID"),
    (0, "POLICY-MIB", "ipPolicyValidRuleIfIndex"),
    (0, "POLICY-MIB", "ipPolicyValidRuleSubContext"),
    (0, "POLICY-MIB", "ipPolicyValidRuleListID"),
    (0, "POLICY-MIB", "ipPolicyValidRuleRuleID"),
)
if mibBuilder.loadTexts:
    ipPolicyValidEtherTypeRuleEntry.setStatus("current")


class _IpPolicyValidEtherTypeRuleEntID_Type(Integer32):
    """Custom type ipPolicyValidEtherTypeRuleEntID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyValidEtherTypeRuleEntID_Type.__name__ = "Integer32"
_IpPolicyValidEtherTypeRuleEntID_Object = MibTableColumn
ipPolicyValidEtherTypeRuleEntID = _IpPolicyValidEtherTypeRuleEntID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 4, 1, 1),
    _IpPolicyValidEtherTypeRuleEntID_Type()
)
ipPolicyValidEtherTypeRuleEntID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidEtherTypeRuleEntID.setStatus("current")


class _IpPolicyValidEtherTypeRuleIfIndex_Type(Integer32):
    """Custom type ipPolicyValidEtherTypeRuleIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyValidEtherTypeRuleIfIndex_Type.__name__ = "Integer32"
_IpPolicyValidEtherTypeRuleIfIndex_Object = MibTableColumn
ipPolicyValidEtherTypeRuleIfIndex = _IpPolicyValidEtherTypeRuleIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 4, 1, 2),
    _IpPolicyValidEtherTypeRuleIfIndex_Type()
)
ipPolicyValidEtherTypeRuleIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidEtherTypeRuleIfIndex.setStatus("current")
_IpPolicyValidEtherTypeRuleSubContext_Type = SubContextTypes
_IpPolicyValidEtherTypeRuleSubContext_Object = MibTableColumn
ipPolicyValidEtherTypeRuleSubContext = _IpPolicyValidEtherTypeRuleSubContext_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 4, 1, 3),
    _IpPolicyValidEtherTypeRuleSubContext_Type()
)
ipPolicyValidEtherTypeRuleSubContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidEtherTypeRuleSubContext.setStatus("current")


class _IpPolicyValidEtherTypeRuleListID_Type(Integer32):
    """Custom type ipPolicyValidEtherTypeRuleListID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyValidEtherTypeRuleListID_Type.__name__ = "Integer32"
_IpPolicyValidEtherTypeRuleListID_Object = MibTableColumn
ipPolicyValidEtherTypeRuleListID = _IpPolicyValidEtherTypeRuleListID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 4, 1, 4),
    _IpPolicyValidEtherTypeRuleListID_Type()
)
ipPolicyValidEtherTypeRuleListID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidEtherTypeRuleListID.setStatus("current")


class _IpPolicyValidEtherTypeRuleRuleID_Type(Integer32):
    """Custom type ipPolicyValidEtherTypeRuleRuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyValidEtherTypeRuleRuleID_Type.__name__ = "Integer32"
_IpPolicyValidEtherTypeRuleRuleID_Object = MibTableColumn
ipPolicyValidEtherTypeRuleRuleID = _IpPolicyValidEtherTypeRuleRuleID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 4, 1, 5),
    _IpPolicyValidEtherTypeRuleRuleID_Type()
)
ipPolicyValidEtherTypeRuleRuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidEtherTypeRuleRuleID.setStatus("current")


class _IpPolicyValidEtherTypeRuleStatus_Type(Integer32):
    """Custom type ipPolicyValidEtherTypeRuleStatus based on Integer32"""
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
        *(("applicable", 1),
          ("partiallyApplicable", 2),
          ("notApplicable", 3),
          ("unknown", 4))
    )


_IpPolicyValidEtherTypeRuleStatus_Type.__name__ = "Integer32"
_IpPolicyValidEtherTypeRuleStatus_Object = MibTableColumn
ipPolicyValidEtherTypeRuleStatus = _IpPolicyValidEtherTypeRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 4, 1, 6),
    _IpPolicyValidEtherTypeRuleStatus_Type()
)
ipPolicyValidEtherTypeRuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidEtherTypeRuleStatus.setStatus("current")


class _IpPolicyValidEtherTypeRuleApplicabilityType_Type(Integer32):
    """Custom type ipPolicyValidEtherTypeRuleApplicabilityType based on Integer32"""
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
        *(("static", 1),
          ("quasiStatic", 2),
          ("dynamic", 3),
          ("unknown", 4))
    )


_IpPolicyValidEtherTypeRuleApplicabilityType_Type.__name__ = "Integer32"
_IpPolicyValidEtherTypeRuleApplicabilityType_Object = MibTableColumn
ipPolicyValidEtherTypeRuleApplicabilityType = _IpPolicyValidEtherTypeRuleApplicabilityType_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 4, 1, 7),
    _IpPolicyValidEtherTypeRuleApplicabilityType_Type()
)
ipPolicyValidEtherTypeRuleApplicabilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidEtherTypeRuleApplicabilityType.setStatus("current")


class _IpPolicyValidEtherTypeRuleErrMsg_Type(DisplayString):
    """Custom type ipPolicyValidEtherTypeRuleErrMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IpPolicyValidEtherTypeRuleErrMsg_Type.__name__ = "DisplayString"
_IpPolicyValidEtherTypeRuleErrMsg_Object = MibTableColumn
ipPolicyValidEtherTypeRuleErrMsg = _IpPolicyValidEtherTypeRuleErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 11, 4, 1, 8),
    _IpPolicyValidEtherTypeRuleErrMsg_Type()
)
ipPolicyValidEtherTypeRuleErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyValidEtherTypeRuleErrMsg.setStatus("current")
_EtherTypeRuleTable_Object = MibTable
etherTypeRuleTable = _EtherTypeRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 12)
)
if mibBuilder.loadTexts:
    etherTypeRuleTable.setStatus("current")
_EtherTypeRuleEntry_Object = MibTableRow
etherTypeRuleEntry = _EtherTypeRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 12, 1)
)
etherTypeRuleEntry.setIndexNames(
    (0, "POLICY-MIB", "ipPolicyEtherTypeRuleSlot"),
    (0, "POLICY-MIB", "ipPolicyEtherTypeRuleListID"),
    (0, "POLICY-MIB", "ipPolicyEtherTypeRuleID"),
)
if mibBuilder.loadTexts:
    etherTypeRuleEntry.setStatus("current")


class _IpPolicyEtherTypeRuleSlot_Type(Integer32):
    """Custom type ipPolicyEtherTypeRuleSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyEtherTypeRuleSlot_Type.__name__ = "Integer32"
_IpPolicyEtherTypeRuleSlot_Object = MibTableColumn
ipPolicyEtherTypeRuleSlot = _IpPolicyEtherTypeRuleSlot_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 12, 1, 1),
    _IpPolicyEtherTypeRuleSlot_Type()
)
ipPolicyEtherTypeRuleSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyEtherTypeRuleSlot.setStatus("current")


class _IpPolicyEtherTypeRuleListID_Type(Integer32):
    """Custom type ipPolicyEtherTypeRuleListID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpPolicyEtherTypeRuleListID_Type.__name__ = "Integer32"
_IpPolicyEtherTypeRuleListID_Object = MibTableColumn
ipPolicyEtherTypeRuleListID = _IpPolicyEtherTypeRuleListID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 12, 1, 2),
    _IpPolicyEtherTypeRuleListID_Type()
)
ipPolicyEtherTypeRuleListID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyEtherTypeRuleListID.setStatus("current")


class _IpPolicyEtherTypeRuleID_Type(Integer32):
    """Custom type ipPolicyEtherTypeRuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_IpPolicyEtherTypeRuleID_Type.__name__ = "Integer32"
_IpPolicyEtherTypeRuleID_Object = MibTableColumn
ipPolicyEtherTypeRuleID = _IpPolicyEtherTypeRuleID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 12, 1, 3),
    _IpPolicyEtherTypeRuleID_Type()
)
ipPolicyEtherTypeRuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyEtherTypeRuleID.setStatus("current")


class _IpPolicyEtherTypeRuleEtherType_Type(Integer32):
    """Custom type ipPolicyEtherTypeRuleEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpPolicyEtherTypeRuleEtherType_Type.__name__ = "Integer32"
_IpPolicyEtherTypeRuleEtherType_Object = MibTableColumn
ipPolicyEtherTypeRuleEtherType = _IpPolicyEtherTypeRuleEtherType_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 12, 1, 4),
    _IpPolicyEtherTypeRuleEtherType_Type()
)
ipPolicyEtherTypeRuleEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyEtherTypeRuleEtherType.setStatus("current")


class _IpPolicyEtherTypeRuleTrafficType_Type(Integer32):
    """Custom type ipPolicyEtherTypeRuleTrafficType based on Integer32"""
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
        *(("all", 1),
          ("broadcasts", 2),
          ("multicasts", 3),
          ("broadcasts-and-multicasts", 4),
          ("unicast", 5))
    )


_IpPolicyEtherTypeRuleTrafficType_Type.__name__ = "Integer32"
_IpPolicyEtherTypeRuleTrafficType_Object = MibTableColumn
ipPolicyEtherTypeRuleTrafficType = _IpPolicyEtherTypeRuleTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 12, 1, 5),
    _IpPolicyEtherTypeRuleTrafficType_Type()
)
ipPolicyEtherTypeRuleTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyEtherTypeRuleTrafficType.setStatus("current")


class _IpPolicyEtherTypeRuleOperation_Type(Integer32):
    """Custom type ipPolicyEtherTypeRuleOperation based on Integer32"""
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
        *(("permit", 1),
          ("deny", 2),
          ("deny-and-notify", 3))
    )


_IpPolicyEtherTypeRuleOperation_Type.__name__ = "Integer32"
_IpPolicyEtherTypeRuleOperation_Object = MibTableColumn
ipPolicyEtherTypeRuleOperation = _IpPolicyEtherTypeRuleOperation_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 12, 1, 6),
    _IpPolicyEtherTypeRuleOperation_Type()
)
ipPolicyEtherTypeRuleOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyEtherTypeRuleOperation.setStatus("current")
_IpPolicyEtherTypeRowStatus_Type = RowStatus
_IpPolicyEtherTypeRowStatus_Object = MibTableColumn
ipPolicyEtherTypeRowStatus = _IpPolicyEtherTypeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 12, 1, 7),
    _IpPolicyEtherTypeRowStatus_Type()
)
ipPolicyEtherTypeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyEtherTypeRowStatus.setStatus("current")
_EtherTypePolicyQueryTable_Object = MibTable
etherTypePolicyQueryTable = _EtherTypePolicyQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 13)
)
if mibBuilder.loadTexts:
    etherTypePolicyQueryTable.setStatus("current")
_EtherTypePolicyQueryEntry_Object = MibTableRow
etherTypePolicyQueryEntry = _EtherTypePolicyQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 13, 1)
)
etherTypePolicyQueryEntry.setIndexNames(
    (0, "POLICY-MIB", "etherTypePolicyQuerySlot"),
)
if mibBuilder.loadTexts:
    etherTypePolicyQueryEntry.setStatus("current")


class _EtherTypePolicyQuerySlot_Type(Integer32):
    """Custom type etherTypePolicyQuerySlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EtherTypePolicyQuerySlot_Type.__name__ = "Integer32"
_EtherTypePolicyQuerySlot_Object = MibTableColumn
etherTypePolicyQuerySlot = _EtherTypePolicyQuerySlot_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 13, 1, 1),
    _EtherTypePolicyQuerySlot_Type()
)
etherTypePolicyQuerySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherTypePolicyQuerySlot.setStatus("current")


class _EtherTypePolicyQueryListID_Type(Integer32):
    """Custom type etherTypePolicyQueryListID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EtherTypePolicyQueryListID_Type.__name__ = "Integer32"
_EtherTypePolicyQueryListID_Object = MibTableColumn
etherTypePolicyQueryListID = _EtherTypePolicyQueryListID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 13, 1, 2),
    _EtherTypePolicyQueryListID_Type()
)
etherTypePolicyQueryListID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherTypePolicyQueryListID.setStatus("current")


class _EtherTypePolicyQueryIfIndex_Type(Integer32):
    """Custom type etherTypePolicyQueryIfIndex based on Integer32"""
    defaultValue = 0


_EtherTypePolicyQueryIfIndex_Type.__name__ = "Integer32"
_EtherTypePolicyQueryIfIndex_Object = MibTableColumn
etherTypePolicyQueryIfIndex = _EtherTypePolicyQueryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 13, 1, 3),
    _EtherTypePolicyQueryIfIndex_Type()
)
etherTypePolicyQueryIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherTypePolicyQueryIfIndex.setStatus("current")


class _EtherTypePolicyQuerySubContext_Type(SubContextTypes):
    """Custom type etherTypePolicyQuerySubContext based on SubContextTypes"""
    defaultValue = 1


_EtherTypePolicyQuerySubContext_Type.__name__ = "SubContextTypes"
_EtherTypePolicyQuerySubContext_Object = MibTableColumn
etherTypePolicyQuerySubContext = _EtherTypePolicyQuerySubContext_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 13, 1, 4),
    _EtherTypePolicyQuerySubContext_Type()
)
etherTypePolicyQuerySubContext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherTypePolicyQuerySubContext.setStatus("current")


class _EtherTypePolicyQueryType_Type(Integer32):
    """Custom type etherTypePolicyQueryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EtherTypePolicyQueryType_Type.__name__ = "Integer32"
_EtherTypePolicyQueryType_Object = MibTableColumn
etherTypePolicyQueryType = _EtherTypePolicyQueryType_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 13, 1, 5),
    _EtherTypePolicyQueryType_Type()
)
etherTypePolicyQueryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherTypePolicyQueryType.setStatus("current")


class _EtherTypePolicyQueryTrafficType_Type(Integer32):
    """Custom type etherTypePolicyQueryTrafficType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("broadcasts", 2),
          ("multicasts", 3))
    )


_EtherTypePolicyQueryTrafficType_Type.__name__ = "Integer32"
_EtherTypePolicyQueryTrafficType_Object = MibTableColumn
etherTypePolicyQueryTrafficType = _EtherTypePolicyQueryTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 13, 1, 6),
    _EtherTypePolicyQueryTrafficType_Type()
)
etherTypePolicyQueryTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherTypePolicyQueryTrafficType.setStatus("current")


class _EtherTypePolicyQueryOperation_Type(Integer32):
    """Custom type etherTypePolicyQueryOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_EtherTypePolicyQueryOperation_Type.__name__ = "Integer32"
_EtherTypePolicyQueryOperation_Object = MibTableColumn
etherTypePolicyQueryOperation = _EtherTypePolicyQueryOperation_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 13, 1, 7),
    _EtherTypePolicyQueryOperation_Type()
)
etherTypePolicyQueryOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherTypePolicyQueryOperation.setStatus("current")


class _EtherTypePolicyQueryRuleID_Type(Integer32):
    """Custom type etherTypePolicyQueryRuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EtherTypePolicyQueryRuleID_Type.__name__ = "Integer32"
_EtherTypePolicyQueryRuleID_Object = MibTableColumn
etherTypePolicyQueryRuleID = _EtherTypePolicyQueryRuleID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 13, 1, 8),
    _EtherTypePolicyQueryRuleID_Type()
)
etherTypePolicyQueryRuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherTypePolicyQueryRuleID.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "POLICY-MIB",
    **{"RowStatus": RowStatus,
       "SubContextTypes": SubContextTypes,
       "TruthValue": TruthValue,
       "ipPolicyMgmt": ipPolicyMgmt,
       "ipPolicyListTable": ipPolicyListTable,
       "ipPolicyListEntry": ipPolicyListEntry,
       "ipPolicyListSlot": ipPolicyListSlot,
       "ipPolicyListID": ipPolicyListID,
       "ipPolicyListName": ipPolicyListName,
       "ipPolicyListValidityStatus": ipPolicyListValidityStatus,
       "ipPolicyListChecksum": ipPolicyListChecksum,
       "ipPolicyListRowStatus": ipPolicyListRowStatus,
       "ipPolicyListDefaultOperation": ipPolicyListDefaultOperation,
       "ipPolicyListCookie": ipPolicyListCookie,
       "ipPolicyListTrackChanges": ipPolicyListTrackChanges,
       "ipPolicyListOwner": ipPolicyListOwner,
       "ipPolicyListErrMsg": ipPolicyListErrMsg,
       "ipPolicyListTrustedFields": ipPolicyListTrustedFields,
       "ipPolicyListScope": ipPolicyListScope,
       "ipPolicyListIpOptionOperation": ipPolicyListIpOptionOperation,
       "ipPolicyListIpFragmentationOperation": ipPolicyListIpFragmentationOperation,
       "ipPolicyListType": ipPolicyListType,
       "ipPolicyListEtherTypeDefaultOperation": ipPolicyListEtherTypeDefaultOperation,
       "ipPolicyListLocalAddress": ipPolicyListLocalAddress,
       "ipPolicyListNATPoolListIndex": ipPolicyListNATPoolListIndex,
       "ipPolicyRuleTable": ipPolicyRuleTable,
       "ipPolicyRuleEntry": ipPolicyRuleEntry,
       "ipPolicyRuleSlot": ipPolicyRuleSlot,
       "ipPolicyRuleListID": ipPolicyRuleListID,
       "ipPolicyRuleID": ipPolicyRuleID,
       "ipPolicyRuleSrcAddr": ipPolicyRuleSrcAddr,
       "ipPolicyRuleSrcAddrWild": ipPolicyRuleSrcAddrWild,
       "ipPolicyRuleDstAddr": ipPolicyRuleDstAddr,
       "ipPolicyRuleDstAddrWild": ipPolicyRuleDstAddrWild,
       "ipPolicyRuleProtocol": ipPolicyRuleProtocol,
       "ipPolicyRuleL4SrcPortMin": ipPolicyRuleL4SrcPortMin,
       "ipPolicyRuleL4SrcPortMax": ipPolicyRuleL4SrcPortMax,
       "ipPolicyRuleL4DestPortMin": ipPolicyRuleL4DestPortMin,
       "ipPolicyRuleL4DestPortMax": ipPolicyRuleL4DestPortMax,
       "ipPolicyRuleEstablished": ipPolicyRuleEstablished,
       "ipPolicyRuleOperation": ipPolicyRuleOperation,
       "ipPolicyRuleApplicabilityPrecedence": ipPolicyRuleApplicabilityPrecedence,
       "ipPolicyRuleApplicabilityStatus": ipPolicyRuleApplicabilityStatus,
       "ipPolicyRuleApplicabilityType": ipPolicyRuleApplicabilityType,
       "ipPolicyRuleErrMsg": ipPolicyRuleErrMsg,
       "ipPolicyRuleStatus": ipPolicyRuleStatus,
       "ipPolicyRuleDSCPOperation": ipPolicyRuleDSCPOperation,
       "ipPolicyRuleDSCPFilter": ipPolicyRuleDSCPFilter,
       "ipPolicyRuleDSCPFilterWild": ipPolicyRuleDSCPFilterWild,
       "ipPolicyRuleIcmpTypeCode": ipPolicyRuleIcmpTypeCode,
       "ipPolicyRuleSrcAddrNot": ipPolicyRuleSrcAddrNot,
       "ipPolicyRuleDstAddrNot": ipPolicyRuleDstAddrNot,
       "ipPolicyRuleProtocolNot": ipPolicyRuleProtocolNot,
       "ipPolicyRuleL4SrcPortNot": ipPolicyRuleL4SrcPortNot,
       "ipPolicyRuleL4DestPortNot": ipPolicyRuleL4DestPortNot,
       "ipPolicyRuleIcmpTypeCodeNot": ipPolicyRuleIcmpTypeCodeNot,
       "ipPolicyRuleSrcPolicyUserGroupName": ipPolicyRuleSrcPolicyUserGroupName,
       "ipPolicyRuleDstPolicyUserGroupName": ipPolicyRuleDstPolicyUserGroupName,
       "ipPolicyRuleDSCPFilterNot": ipPolicyRuleDSCPFilterNot,
       "ipPolicyRuleDescription": ipPolicyRuleDescription,
       "ipPolicyRuleFragment": ipPolicyRuleFragment,
       "ipPolicyRuleDoSClass": ipPolicyRuleDoSClass,
       "ipPolicyControlTable": ipPolicyControlTable,
       "ipPolicyControlEntry": ipPolicyControlEntry,
       "ipPolicyControlSlot": ipPolicyControlSlot,
       "ipPolicyControlActiveGeneralList": ipPolicyControlActiveGeneralList,
       "ipPolicyControlAllowedPolicyManagers": ipPolicyControlAllowedPolicyManagers,
       "ipPolicyControlCurrentChecksum": ipPolicyControlCurrentChecksum,
       "ipPolicyControlMinimalPolicyManagmentVersion": ipPolicyControlMinimalPolicyManagmentVersion,
       "ipPolicyControlMaximalPolicyManagmentVersion": ipPolicyControlMaximalPolicyManagmentVersion,
       "ipPolicyControlMIBversion": ipPolicyControlMIBversion,
       "ipPolicyControlCapabilitiesGeneral": ipPolicyControlCapabilitiesGeneral,
       "ipPolicyControlCopySourceList": ipPolicyControlCopySourceList,
       "ipPolicyControlCopyDestinationList": ipPolicyControlCopyDestinationList,
       "ipPolicyControlCopyOperation": ipPolicyControlCopyOperation,
       "ipPolicyControlCopyOperationLastStatus": ipPolicyControlCopyOperationLastStatus,
       "ipPolicyControlCopyOperationLastFailureDisplay": ipPolicyControlCopyOperationLastFailureDisplay,
       "ipPolicyDiffServTable": ipPolicyDiffServTable,
       "ipPolicyDiffServEntry": ipPolicyDiffServEntry,
       "ipPolicyDiffServSlot": ipPolicyDiffServSlot,
       "ipPolicyDiffServDSCP": ipPolicyDiffServDSCP,
       "ipPolicyDiffServOperation": ipPolicyDiffServOperation,
       "ipPolicyDiffServName": ipPolicyDiffServName,
       "ipPolicyDiffServAggIndex": ipPolicyDiffServAggIndex,
       "ipPolicyDiffServApplicabilityPrecedence": ipPolicyDiffServApplicabilityPrecedence,
       "ipPolicyDiffServApplicabilityStatus": ipPolicyDiffServApplicabilityStatus,
       "ipPolicyDiffServApplicabilityType": ipPolicyDiffServApplicabilityType,
       "ipPolicyDiffServErrMsg": ipPolicyDiffServErrMsg,
       "ipPolicyQueryTable": ipPolicyQueryTable,
       "ipPolicyQueryEntry": ipPolicyQueryEntry,
       "ipPolicyQuerySlot": ipPolicyQuerySlot,
       "ipPolicyQueryListID": ipPolicyQueryListID,
       "ipPolicyQuerySrcAddr": ipPolicyQuerySrcAddr,
       "ipPolicyQueryDstAddr": ipPolicyQueryDstAddr,
       "ipPolicyQueryProtocol": ipPolicyQueryProtocol,
       "ipPolicyQueryL4SrcPort": ipPolicyQueryL4SrcPort,
       "ipPolicyQueryL4DestPort": ipPolicyQueryL4DestPort,
       "ipPolicyQueryEstablished": ipPolicyQueryEstablished,
       "ipPolicyQueryDSCP": ipPolicyQueryDSCP,
       "ipPolicyQueryOperation": ipPolicyQueryOperation,
       "ipPolicyQueryRuleID": ipPolicyQueryRuleID,
       "ipPolicyQueryDSCPOperation": ipPolicyQueryDSCPOperation,
       "ipPolicyQueryPriority": ipPolicyQueryPriority,
       "ipPolicyQueryIfIndex": ipPolicyQueryIfIndex,
       "ipPolicyQuerySubContext": ipPolicyQuerySubContext,
       "ipPolicyQueryIcmpTypeCode": ipPolicyQueryIcmpTypeCode,
       "ipPolicyQueryIpFragments": ipPolicyQueryIpFragments,
       "ipPolicyQueryIpOption": ipPolicyQueryIpOption,
       "ipPolicyQueryAccessOperation": ipPolicyQueryAccessOperation,
       "ipPolicyQueryNotifyOperation": ipPolicyQueryNotifyOperation,
       "ipPolicyQueryErrorReplyOperation": ipPolicyQueryErrorReplyOperation,
       "ipPolicyQueryCoSOperation": ipPolicyQueryCoSOperation,
       "ipPolicyDiffServControlTable": ipPolicyDiffServControlTable,
       "ipPolicyDiffServControlEntry": ipPolicyDiffServControlEntry,
       "ipPolicyDiffServControlSlot": ipPolicyDiffServControlSlot,
       "ipPolicyDiffServControlChecksum": ipPolicyDiffServControlChecksum,
       "ipPolicyDiffServControlTrustedFields": ipPolicyDiffServControlTrustedFields,
       "ipPolicyDiffServControlValidityStatus": ipPolicyDiffServControlValidityStatus,
       "ipPolicyDiffServControlErrMsg": ipPolicyDiffServControlErrMsg,
       "ipPolicyAccessControlViolationTable": ipPolicyAccessControlViolationTable,
       "ipPolicyAccessControlViolationEntry": ipPolicyAccessControlViolationEntry,
       "ipPolicyAccessControlViolationEntID": ipPolicyAccessControlViolationEntID,
       "ipPolicyAccessControlViolationSrcAddr": ipPolicyAccessControlViolationSrcAddr,
       "ipPolicyAccessControlViolationDstAddr": ipPolicyAccessControlViolationDstAddr,
       "ipPolicyAccessControlViolationProtocol": ipPolicyAccessControlViolationProtocol,
       "ipPolicyAccessControlViolationL4SrcPort": ipPolicyAccessControlViolationL4SrcPort,
       "ipPolicyAccessControlViolationL4DstPort": ipPolicyAccessControlViolationL4DstPort,
       "ipPolicyAccessControlViolationEstablished": ipPolicyAccessControlViolationEstablished,
       "ipPolicyAccessControlViolationDSCP": ipPolicyAccessControlViolationDSCP,
       "ipPolicyAccessControlViolationIfIndex": ipPolicyAccessControlViolationIfIndex,
       "ipPolicyAccessControlViolationSubCtxt": ipPolicyAccessControlViolationSubCtxt,
       "ipPolicyAccessControlViolationTime": ipPolicyAccessControlViolationTime,
       "ipPolicyAccessControlViolationRuleType": ipPolicyAccessControlViolationRuleType,
       "ipPolicyCompositeOpTable": ipPolicyCompositeOpTable,
       "ipPolicyCompositeOpEntry": ipPolicyCompositeOpEntry,
       "ipPolicyCompositeOpEntID": ipPolicyCompositeOpEntID,
       "ipPolicyCompositeOpListID": ipPolicyCompositeOpListID,
       "ipPolicyCompositeOpID": ipPolicyCompositeOpID,
       "ipPolicyCompositeOpName": ipPolicyCompositeOpName,
       "ipPolicyCompositeOp802priority": ipPolicyCompositeOp802priority,
       "ipPolicyCompositeOpAccess": ipPolicyCompositeOpAccess,
       "ipPolicyCompositeOpDscp": ipPolicyCompositeOpDscp,
       "ipPolicyCompositeOpRSGQualityClass": ipPolicyCompositeOpRSGQualityClass,
       "ipPolicyCompositeOpNotify": ipPolicyCompositeOpNotify,
       "ipPolicyCompositeOpRowStatus": ipPolicyCompositeOpRowStatus,
       "ipPolicyCompositeOpErrorReply": ipPolicyCompositeOpErrorReply,
       "ipPolicyCompositeOpTrustDscp": ipPolicyCompositeOpTrustDscp,
       "ipPolicyDSCPmapTable": ipPolicyDSCPmapTable,
       "ipPolicyDSCPmapEntry": ipPolicyDSCPmapEntry,
       "ipPolicyDSCPmapEntID": ipPolicyDSCPmapEntID,
       "ipPolicyDSCPmapListID": ipPolicyDSCPmapListID,
       "ipPolicyDSCPmapDSCP": ipPolicyDSCPmapDSCP,
       "ipPolicyDSCPmapOperation": ipPolicyDSCPmapOperation,
       "ipPolicyDSCPmapName": ipPolicyDSCPmapName,
       "ipPolicyDSCPmapApplicabilityPrecedence": ipPolicyDSCPmapApplicabilityPrecedence,
       "ipPolicyDSCPmapApplicabilityStatus": ipPolicyDSCPmapApplicabilityStatus,
       "ipPolicyDSCPmapApplicabilityType": ipPolicyDSCPmapApplicabilityType,
       "ipPolicyDSCPmapErrMsg": ipPolicyDSCPmapErrMsg,
       "ipPolicyActivationTable": ipPolicyActivationTable,
       "ipPolicyActivationEntry": ipPolicyActivationEntry,
       "ipPolicyActivationEntID": ipPolicyActivationEntID,
       "ipPolicyActivationifIndex": ipPolicyActivationifIndex,
       "ipPolicyActivationSubContext": ipPolicyActivationSubContext,
       "ipPolicyActivationSubContextName": ipPolicyActivationSubContextName,
       "ipPolicyActivationList": ipPolicyActivationList,
       "ipPolicyActivationAclList": ipPolicyActivationAclList,
       "ipPolicyActivationQoSList": ipPolicyActivationQoSList,
       "ipPolicyActivationSourceNatList": ipPolicyActivationSourceNatList,
       "ipPolicyActivationDestinationNatList": ipPolicyActivationDestinationNatList,
       "ipPolicyActivationAntiSpoofignList": ipPolicyActivationAntiSpoofignList,
       "ipPolicyActivationPBRList": ipPolicyActivationPBRList,
       "ipPolicyActivationCryptoList": ipPolicyActivationCryptoList,
       "ipPolicyValidation": ipPolicyValidation,
       "ipPolicyValidListTable": ipPolicyValidListTable,
       "ipPolicyValidListEntry": ipPolicyValidListEntry,
       "ipPolicyValidListEntID": ipPolicyValidListEntID,
       "ipPolicyValidListIfIndex": ipPolicyValidListIfIndex,
       "ipPolicyValidListSubContext": ipPolicyValidListSubContext,
       "ipPolicyValidListListID": ipPolicyValidListListID,
       "ipPolicyValidListStatus": ipPolicyValidListStatus,
       "ipPolicyValidListErrMsg": ipPolicyValidListErrMsg,
       "ipPolicyValidListIpOption": ipPolicyValidListIpOption,
       "ipPolicyValidListIpFragmentation": ipPolicyValidListIpFragmentation,
       "ipPolicyValidRuleTable": ipPolicyValidRuleTable,
       "ipPolicyValidRuleEntry": ipPolicyValidRuleEntry,
       "ipPolicyValidRuleEntID": ipPolicyValidRuleEntID,
       "ipPolicyValidRuleIfIndex": ipPolicyValidRuleIfIndex,
       "ipPolicyValidRuleSubContext": ipPolicyValidRuleSubContext,
       "ipPolicyValidRuleListID": ipPolicyValidRuleListID,
       "ipPolicyValidRuleRuleID": ipPolicyValidRuleRuleID,
       "ipPolicyValidRuleStatus": ipPolicyValidRuleStatus,
       "ipPolicyValidRuleApplicabilityType": ipPolicyValidRuleApplicabilityType,
       "ipPolicyValidRuleErrMsg": ipPolicyValidRuleErrMsg,
       "ipPolicyValidDSCPTable": ipPolicyValidDSCPTable,
       "ipPolicyValidDSCPEntry": ipPolicyValidDSCPEntry,
       "ipPolicyValidDSCPEntID": ipPolicyValidDSCPEntID,
       "ipPolicyValidDSCPIfIndex": ipPolicyValidDSCPIfIndex,
       "ipPolicyValidDSCPSubContext": ipPolicyValidDSCPSubContext,
       "ipPolicyValidDSCPListID": ipPolicyValidDSCPListID,
       "ipPolicyValidDSCPvalue": ipPolicyValidDSCPvalue,
       "ipPolicyValidDSCPStatus": ipPolicyValidDSCPStatus,
       "ipPolicyValidDSCPApplicabilityType": ipPolicyValidDSCPApplicabilityType,
       "ipPolicyValidDSCPErrMsg": ipPolicyValidDSCPErrMsg,
       "ipPolicyValidEtherTypeRuleTable": ipPolicyValidEtherTypeRuleTable,
       "ipPolicyValidEtherTypeRuleEntry": ipPolicyValidEtherTypeRuleEntry,
       "ipPolicyValidEtherTypeRuleEntID": ipPolicyValidEtherTypeRuleEntID,
       "ipPolicyValidEtherTypeRuleIfIndex": ipPolicyValidEtherTypeRuleIfIndex,
       "ipPolicyValidEtherTypeRuleSubContext": ipPolicyValidEtherTypeRuleSubContext,
       "ipPolicyValidEtherTypeRuleListID": ipPolicyValidEtherTypeRuleListID,
       "ipPolicyValidEtherTypeRuleRuleID": ipPolicyValidEtherTypeRuleRuleID,
       "ipPolicyValidEtherTypeRuleStatus": ipPolicyValidEtherTypeRuleStatus,
       "ipPolicyValidEtherTypeRuleApplicabilityType": ipPolicyValidEtherTypeRuleApplicabilityType,
       "ipPolicyValidEtherTypeRuleErrMsg": ipPolicyValidEtherTypeRuleErrMsg,
       "etherTypeRuleTable": etherTypeRuleTable,
       "etherTypeRuleEntry": etherTypeRuleEntry,
       "ipPolicyEtherTypeRuleSlot": ipPolicyEtherTypeRuleSlot,
       "ipPolicyEtherTypeRuleListID": ipPolicyEtherTypeRuleListID,
       "ipPolicyEtherTypeRuleID": ipPolicyEtherTypeRuleID,
       "ipPolicyEtherTypeRuleEtherType": ipPolicyEtherTypeRuleEtherType,
       "ipPolicyEtherTypeRuleTrafficType": ipPolicyEtherTypeRuleTrafficType,
       "ipPolicyEtherTypeRuleOperation": ipPolicyEtherTypeRuleOperation,
       "ipPolicyEtherTypeRowStatus": ipPolicyEtherTypeRowStatus,
       "etherTypePolicyQueryTable": etherTypePolicyQueryTable,
       "etherTypePolicyQueryEntry": etherTypePolicyQueryEntry,
       "etherTypePolicyQuerySlot": etherTypePolicyQuerySlot,
       "etherTypePolicyQueryListID": etherTypePolicyQueryListID,
       "etherTypePolicyQueryIfIndex": etherTypePolicyQueryIfIndex,
       "etherTypePolicyQuerySubContext": etherTypePolicyQuerySubContext,
       "etherTypePolicyQueryType": etherTypePolicyQueryType,
       "etherTypePolicyQueryTrafficType": etherTypePolicyQueryTrafficType,
       "etherTypePolicyQueryOperation": etherTypePolicyQueryOperation,
       "etherTypePolicyQueryRuleID": etherTypePolicyQueryRuleID}
)
