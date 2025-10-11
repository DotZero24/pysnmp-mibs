# SNMP MIB module (ZTE-AN-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-VLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:09 2025
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(VlanId,
 ZxAnIfindex,
 ZxAnPortList,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "VlanId",
    "ZxAnIfindex",
    "ZxAnPortList",
    "zxAn")


# MODULE-IDENTITY

zxAnVlanMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20)
)
if mibBuilder.loadTexts:
    zxAnVlanMib.setRevisions(
        ("1911-06-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnVlanNum_Type = Integer32
_ZxAnVlanNum_Object = MibScalar
zxAnVlanNum = _ZxAnVlanNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 1),
    _ZxAnVlanNum_Type()
)
zxAnVlanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanNum.setStatus("current")
_ZxAnVlanTable_Object = MibTable
zxAnVlanTable = _ZxAnVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 2)
)
if mibBuilder.loadTexts:
    zxAnVlanTable.setStatus("current")
_ZxAnVlanEntry_Object = MibTableRow
zxAnVlanEntry = _ZxAnVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 2, 1)
)
zxAnVlanEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanId"),
)
if mibBuilder.loadTexts:
    zxAnVlanEntry.setStatus("current")
_ZxAnVlanId_Type = VlanId
_ZxAnVlanId_Object = MibTableColumn
zxAnVlanId = _ZxAnVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 2, 1, 1),
    _ZxAnVlanId_Type()
)
zxAnVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVlanId.setStatus("current")


class _ZxAnVlanName_Type(DisplayString):
    """Custom type zxAnVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnVlanName_Type.__name__ = "DisplayString"
_ZxAnVlanName_Object = MibTableColumn
zxAnVlanName = _ZxAnVlanName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 2, 1, 2),
    _ZxAnVlanName_Type()
)
zxAnVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanName.setStatus("current")


class _ZxAnVlanTransparent_Type(Integer32):
    """Custom type zxAnVlanTransparent based on Integer32"""
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
          ("disable", 2))
    )


_ZxAnVlanTransparent_Type.__name__ = "Integer32"
_ZxAnVlanTransparent_Object = MibTableColumn
zxAnVlanTransparent = _ZxAnVlanTransparent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 2, 1, 3),
    _ZxAnVlanTransparent_Type()
)
zxAnVlanTransparent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanTransparent.setStatus("current")
_ZxAnVlanRowStatus_Type = RowStatus
_ZxAnVlanRowStatus_Object = MibTableColumn
zxAnVlanRowStatus = _ZxAnVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 2, 1, 4),
    _ZxAnVlanRowStatus_Type()
)
zxAnVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanRowStatus.setStatus("current")


class _ZxAnVlanXconnect_Type(Integer32):
    """Custom type zxAnVlanXconnect based on Integer32"""
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
          ("disable", 2))
    )


_ZxAnVlanXconnect_Type.__name__ = "Integer32"
_ZxAnVlanXconnect_Object = MibTableColumn
zxAnVlanXconnect = _ZxAnVlanXconnect_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 2, 1, 5),
    _ZxAnVlanXconnect_Type()
)
zxAnVlanXconnect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanXconnect.setStatus("current")


class _ZxAnVlanDesc_Type(DisplayString):
    """Custom type zxAnVlanDesc based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnVlanDesc_Type.__name__ = "DisplayString"
_ZxAnVlanDesc_Object = MibTableColumn
zxAnVlanDesc = _ZxAnVlanDesc_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 2, 1, 6),
    _ZxAnVlanDesc_Type()
)
zxAnVlanDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanDesc.setStatus("current")
_ZxAnVlanPortTable_Object = MibTable
zxAnVlanPortTable = _ZxAnVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 3)
)
if mibBuilder.loadTexts:
    zxAnVlanPortTable.setStatus("current")
_ZxAnVlanPortEntry_Object = MibTableRow
zxAnVlanPortEntry = _ZxAnVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 3, 1)
)
zxAnVlanPortEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanPortIndex"),
)
if mibBuilder.loadTexts:
    zxAnVlanPortEntry.setStatus("current")
_ZxAnVlanPortIndex_Type = ZxAnIfindex
_ZxAnVlanPortIndex_Object = MibTableColumn
zxAnVlanPortIndex = _ZxAnVlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 3, 1, 1),
    _ZxAnVlanPortIndex_Type()
)
zxAnVlanPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVlanPortIndex.setStatus("current")


class _ZxAnVlanIfConfMode_Type(Integer32):
    """Custom type zxAnVlanIfConfMode based on Integer32"""
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
        *(("access", 1),
          ("trunk", 2),
          ("hybrid", 3),
          ("transparent", 4))
    )


_ZxAnVlanIfConfMode_Type.__name__ = "Integer32"
_ZxAnVlanIfConfMode_Object = MibTableColumn
zxAnVlanIfConfMode = _ZxAnVlanIfConfMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 3, 1, 2),
    _ZxAnVlanIfConfMode_Type()
)
zxAnVlanIfConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanIfConfMode.setStatus("current")


class _ZxAnVlanIfConfTlsEnable_Type(Integer32):
    """Custom type zxAnVlanIfConfTlsEnable based on Integer32"""
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
          ("disable", 2))
    )


_ZxAnVlanIfConfTlsEnable_Type.__name__ = "Integer32"
_ZxAnVlanIfConfTlsEnable_Object = MibTableColumn
zxAnVlanIfConfTlsEnable = _ZxAnVlanIfConfTlsEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 3, 1, 3),
    _ZxAnVlanIfConfTlsEnable_Type()
)
zxAnVlanIfConfTlsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanIfConfTlsEnable.setStatus("current")


class _ZxAnVlanIfConfTlsSVid_Type(Integer32):
    """Custom type zxAnVlanIfConfTlsSVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ZxAnVlanIfConfTlsSVid_Type.__name__ = "Integer32"
_ZxAnVlanIfConfTlsSVid_Object = MibTableColumn
zxAnVlanIfConfTlsSVid = _ZxAnVlanIfConfTlsSVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 3, 1, 4),
    _ZxAnVlanIfConfTlsSVid_Type()
)
zxAnVlanIfConfTlsSVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanIfConfTlsSVid.setStatus("current")
_ZxAnVlanIfConfDefaultVid_Type = VlanId
_ZxAnVlanIfConfDefaultVid_Object = MibTableColumn
zxAnVlanIfConfDefaultVid = _ZxAnVlanIfConfDefaultVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 3, 1, 5),
    _ZxAnVlanIfConfDefaultVid_Type()
)
zxAnVlanIfConfDefaultVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanIfConfDefaultVid.setStatus("current")


class _ZxAnVlanIfConfDefaultCVid_Type(Integer32):
    """Custom type zxAnVlanIfConfDefaultCVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ZxAnVlanIfConfDefaultCVid_Type.__name__ = "Integer32"
_ZxAnVlanIfConfDefaultCVid_Object = MibTableColumn
zxAnVlanIfConfDefaultCVid = _ZxAnVlanIfConfDefaultCVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 3, 1, 6),
    _ZxAnVlanIfConfDefaultCVid_Type()
)
zxAnVlanIfConfDefaultCVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanIfConfDefaultCVid.setStatus("current")
_ZxAnVlanIfConfUntaggedVlanList_Type = DisplayString
_ZxAnVlanIfConfUntaggedVlanList_Object = MibTableColumn
zxAnVlanIfConfUntaggedVlanList = _ZxAnVlanIfConfUntaggedVlanList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 3, 1, 7),
    _ZxAnVlanIfConfUntaggedVlanList_Type()
)
zxAnVlanIfConfUntaggedVlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanIfConfUntaggedVlanList.setStatus("current")
_ZxAnVlanIfConfTaggedVlanList_Type = DisplayString
_ZxAnVlanIfConfTaggedVlanList_Object = MibTableColumn
zxAnVlanIfConfTaggedVlanList = _ZxAnVlanIfConfTaggedVlanList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 3, 1, 8),
    _ZxAnVlanIfConfTaggedVlanList_Type()
)
zxAnVlanIfConfTaggedVlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanIfConfTaggedVlanList.setStatus("current")


class _ZxAnVlanIfConfTpid_Type(Integer32):
    """Custom type zxAnVlanIfConfTpid based on Integer32"""
    defaultValue = 33024


_ZxAnVlanIfConfTpid_Type.__name__ = "Integer32"
_ZxAnVlanIfConfTpid_Object = MibTableColumn
zxAnVlanIfConfTpid = _ZxAnVlanIfConfTpid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 3, 1, 9),
    _ZxAnVlanIfConfTpid_Type()
)
zxAnVlanIfConfTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanIfConfTpid.setStatus("current")


class _ZxAnVlanIfIngressFilterEnable_Type(Integer32):
    """Custom type zxAnVlanIfIngressFilterEnable based on Integer32"""
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


_ZxAnVlanIfIngressFilterEnable_Type.__name__ = "Integer32"
_ZxAnVlanIfIngressFilterEnable_Object = MibTableColumn
zxAnVlanIfIngressFilterEnable = _ZxAnVlanIfIngressFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 3, 1, 10),
    _ZxAnVlanIfIngressFilterEnable_Type()
)
zxAnVlanIfIngressFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanIfIngressFilterEnable.setStatus("current")


class _ZxAnVlanIfAcceptableFrameTypes_Type(Integer32):
    """Custom type zxAnVlanIfAcceptableFrameTypes based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("admitAll", 1),
          ("admitOnlyVlanTagged", 2),
          ("admitOnlyVlanUntagged", 3),
          ("admitOnlyVlanSingleTagged", 4),
          ("admitOnlyVlanMaxDoubleTagged", 5),
          ("admitOnlyVlanMaxSingleTagged", 6),
          ("admitOnlyVlanDoubleTagged", 7))
    )


_ZxAnVlanIfAcceptableFrameTypes_Type.__name__ = "Integer32"
_ZxAnVlanIfAcceptableFrameTypes_Object = MibTableColumn
zxAnVlanIfAcceptableFrameTypes = _ZxAnVlanIfAcceptableFrameTypes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 3, 1, 11),
    _ZxAnVlanIfAcceptableFrameTypes_Type()
)
zxAnVlanIfAcceptableFrameTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanIfAcceptableFrameTypes.setStatus("current")


class _ZxAnVlanIfConfTpidEnable_Type(Integer32):
    """Custom type zxAnVlanIfConfTpidEnable based on Integer32"""
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


_ZxAnVlanIfConfTpidEnable_Type.__name__ = "Integer32"
_ZxAnVlanIfConfTpidEnable_Object = MibTableColumn
zxAnVlanIfConfTpidEnable = _ZxAnVlanIfConfTpidEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 3, 1, 12),
    _ZxAnVlanIfConfTpidEnable_Type()
)
zxAnVlanIfConfTpidEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanIfConfTpidEnable.setStatus("current")
_ZxAnVlanIfConfVlanCmdTable_Object = MibTable
zxAnVlanIfConfVlanCmdTable = _ZxAnVlanIfConfVlanCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 4)
)
if mibBuilder.loadTexts:
    zxAnVlanIfConfVlanCmdTable.setStatus("current")
_ZxAnVlanIfConfVlanCmdEntry_Object = MibTableRow
zxAnVlanIfConfVlanCmdEntry = _ZxAnVlanIfConfVlanCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 4, 1)
)
zxAnVlanIfConfVlanCmdEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanPortIndex"),
)
if mibBuilder.loadTexts:
    zxAnVlanIfConfVlanCmdEntry.setStatus("current")


class _ZxAnVlanIfConfVlanCmd_Type(Integer32):
    """Custom type zxAnVlanIfConfVlanCmd based on Integer32"""
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
        *(("addTaggedVlan", 1),
          ("delTaggedVlan", 2),
          ("addUntaggedVlan", 3),
          ("delUntaggedVlan", 4),
          ("addDefaultVlan", 5),
          ("delDefaultVlan", 6))
    )


_ZxAnVlanIfConfVlanCmd_Type.__name__ = "Integer32"
_ZxAnVlanIfConfVlanCmd_Object = MibTableColumn
zxAnVlanIfConfVlanCmd = _ZxAnVlanIfConfVlanCmd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 4, 1, 1),
    _ZxAnVlanIfConfVlanCmd_Type()
)
zxAnVlanIfConfVlanCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanIfConfVlanCmd.setStatus("current")
_ZxAnVlanIfConfVlanList_Type = VlanId
_ZxAnVlanIfConfVlanList_Object = MibTableColumn
zxAnVlanIfConfVlanList = _ZxAnVlanIfConfVlanList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 4, 1, 2),
    _ZxAnVlanIfConfVlanList_Type()
)
zxAnVlanIfConfVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanIfConfVlanList.setStatus("current")
_ZxAnVlanIfTransTable_Object = MibTable
zxAnVlanIfTransTable = _ZxAnVlanIfTransTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 5)
)
if mibBuilder.loadTexts:
    zxAnVlanIfTransTable.setStatus("current")
_ZxAnVlanIfTransEntry_Object = MibTableRow
zxAnVlanIfTransEntry = _ZxAnVlanIfTransEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 5, 1)
)
zxAnVlanIfTransEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanTranslatePortId"),
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanIfTransUserVid"),
)
if mibBuilder.loadTexts:
    zxAnVlanIfTransEntry.setStatus("current")
_ZxAnVlanTranslatePortId_Type = Integer32
_ZxAnVlanTranslatePortId_Object = MibTableColumn
zxAnVlanTranslatePortId = _ZxAnVlanTranslatePortId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 5, 1, 1),
    _ZxAnVlanTranslatePortId_Type()
)
zxAnVlanTranslatePortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVlanTranslatePortId.setStatus("current")
_ZxAnVlanIfTransUserVid_Type = VlanId
_ZxAnVlanIfTransUserVid_Object = MibTableColumn
zxAnVlanIfTransUserVid = _ZxAnVlanIfTransUserVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 5, 1, 2),
    _ZxAnVlanIfTransUserVid_Type()
)
zxAnVlanIfTransUserVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVlanIfTransUserVid.setStatus("current")


class _ZxAnVlanIfTransCVid_Type(Integer32):
    """Custom type zxAnVlanIfTransCVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ZxAnVlanIfTransCVid_Type.__name__ = "Integer32"
_ZxAnVlanIfTransCVid_Object = MibTableColumn
zxAnVlanIfTransCVid = _ZxAnVlanIfTransCVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 5, 1, 3),
    _ZxAnVlanIfTransCVid_Type()
)
zxAnVlanIfTransCVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanIfTransCVid.setStatus("current")
_ZxAnVlanIfTransSVid_Type = VlanId
_ZxAnVlanIfTransSVid_Object = MibTableColumn
zxAnVlanIfTransSVid = _ZxAnVlanIfTransSVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 5, 1, 4),
    _ZxAnVlanIfTransSVid_Type()
)
zxAnVlanIfTransSVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanIfTransSVid.setStatus("current")
_ZxAnVlanIfTransRowStatus_Type = RowStatus
_ZxAnVlanIfTransRowStatus_Object = MibTableColumn
zxAnVlanIfTransRowStatus = _ZxAnVlanIfTransRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 5, 1, 5),
    _ZxAnVlanIfTransRowStatus_Type()
)
zxAnVlanIfTransRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanIfTransRowStatus.setStatus("current")


class _ZxAnVlanIfTransVlanMerge_Type(Integer32):
    """Custom type zxAnVlanIfTransVlanMerge based on Integer32"""
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


_ZxAnVlanIfTransVlanMerge_Type.__name__ = "Integer32"
_ZxAnVlanIfTransVlanMerge_Object = MibTableColumn
zxAnVlanIfTransVlanMerge = _ZxAnVlanIfTransVlanMerge_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 5, 1, 6),
    _ZxAnVlanIfTransVlanMerge_Type()
)
zxAnVlanIfTransVlanMerge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanIfTransVlanMerge.setStatus("current")
_ZxAnVlanPortListTable_Object = MibTable
zxAnVlanPortListTable = _ZxAnVlanPortListTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 6)
)
if mibBuilder.loadTexts:
    zxAnVlanPortListTable.setStatus("current")
_ZxAnVlanPortListEntry_Object = MibTableRow
zxAnVlanPortListEntry = _ZxAnVlanPortListEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 6, 1)
)
zxAnVlanPortListEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanIndex"),
    (0, "ZTE-AN-VLAN-MIB", "zxAnShelfIndex"),
    (0, "ZTE-AN-VLAN-MIB", "zxAnSlotIndex"),
)
if mibBuilder.loadTexts:
    zxAnVlanPortListEntry.setStatus("current")
_ZxAnVlanIndex_Type = VlanId
_ZxAnVlanIndex_Object = MibTableColumn
zxAnVlanIndex = _ZxAnVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 6, 1, 1),
    _ZxAnVlanIndex_Type()
)
zxAnVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVlanIndex.setStatus("current")
_ZxAnShelfIndex_Type = Integer32
_ZxAnShelfIndex_Object = MibTableColumn
zxAnShelfIndex = _ZxAnShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 6, 1, 2),
    _ZxAnShelfIndex_Type()
)
zxAnShelfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnShelfIndex.setStatus("current")
_ZxAnSlotIndex_Type = Integer32
_ZxAnSlotIndex_Object = MibTableColumn
zxAnSlotIndex = _ZxAnSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 6, 1, 3),
    _ZxAnSlotIndex_Type()
)
zxAnSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSlotIndex.setStatus("current")
_ZxAnVlanPortListSlotIfType_Type = Integer32
_ZxAnVlanPortListSlotIfType_Object = MibTableColumn
zxAnVlanPortListSlotIfType = _ZxAnVlanPortListSlotIfType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 6, 1, 4),
    _ZxAnVlanPortListSlotIfType_Type()
)
zxAnVlanPortListSlotIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanPortListSlotIfType.setStatus("current")
_ZxAnVlanPortUntaggedPortList_Type = ZxAnPortList
_ZxAnVlanPortUntaggedPortList_Object = MibTableColumn
zxAnVlanPortUntaggedPortList = _ZxAnVlanPortUntaggedPortList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 6, 1, 5),
    _ZxAnVlanPortUntaggedPortList_Type()
)
zxAnVlanPortUntaggedPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanPortUntaggedPortList.setStatus("current")
_ZxAnVlanPortTaggedPortList_Type = ZxAnPortList
_ZxAnVlanPortTaggedPortList_Object = MibTableColumn
zxAnVlanPortTaggedPortList = _ZxAnVlanPortTaggedPortList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 6, 1, 6),
    _ZxAnVlanPortTaggedPortList_Type()
)
zxAnVlanPortTaggedPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanPortTaggedPortList.setStatus("current")
_ZxAnVlanGlobalTransTable_Object = MibTable
zxAnVlanGlobalTransTable = _ZxAnVlanGlobalTransTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 7)
)
if mibBuilder.loadTexts:
    zxAnVlanGlobalTransTable.setStatus("current")
_ZxAnVlanGlobalTransEntry_Object = MibTableRow
zxAnVlanGlobalTransEntry = _ZxAnVlanGlobalTransEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 7, 1)
)
zxAnVlanGlobalTransEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanGlobalTransSessionNo"),
)
if mibBuilder.loadTexts:
    zxAnVlanGlobalTransEntry.setStatus("current")


class _ZxAnVlanGlobalTransSessionNo_Type(Integer32):
    """Custom type zxAnVlanGlobalTransSessionNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_ZxAnVlanGlobalTransSessionNo_Type.__name__ = "Integer32"
_ZxAnVlanGlobalTransSessionNo_Object = MibTableColumn
zxAnVlanGlobalTransSessionNo = _ZxAnVlanGlobalTransSessionNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 7, 1, 1),
    _ZxAnVlanGlobalTransSessionNo_Type()
)
zxAnVlanGlobalTransSessionNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVlanGlobalTransSessionNo.setStatus("current")
_ZxAnVlanMpTranslatePortId_Type = Integer32
_ZxAnVlanMpTranslatePortId_Object = MibTableColumn
zxAnVlanMpTranslatePortId = _ZxAnVlanMpTranslatePortId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 7, 1, 2),
    _ZxAnVlanMpTranslatePortId_Type()
)
zxAnVlanMpTranslatePortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanMpTranslatePortId.setStatus("current")
_ZxAnVlanGlobalTransVid_Type = VlanId
_ZxAnVlanGlobalTransVid_Object = MibTableColumn
zxAnVlanGlobalTransVid = _ZxAnVlanGlobalTransVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 7, 1, 3),
    _ZxAnVlanGlobalTransVid_Type()
)
zxAnVlanGlobalTransVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanGlobalTransVid.setStatus("current")


class _ZxAnVlanGlobalTransCVid_Type(Integer32):
    """Custom type zxAnVlanGlobalTransCVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnVlanGlobalTransCVid_Type.__name__ = "Integer32"
_ZxAnVlanGlobalTransCVid_Object = MibTableColumn
zxAnVlanGlobalTransCVid = _ZxAnVlanGlobalTransCVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 7, 1, 4),
    _ZxAnVlanGlobalTransCVid_Type()
)
zxAnVlanGlobalTransCVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanGlobalTransCVid.setStatus("current")


class _ZxAnVlanGlobalTransSVid_Type(Integer32):
    """Custom type zxAnVlanGlobalTransSVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ZxAnVlanGlobalTransSVid_Type.__name__ = "Integer32"
_ZxAnVlanGlobalTransSVid_Object = MibTableColumn
zxAnVlanGlobalTransSVid = _ZxAnVlanGlobalTransSVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 7, 1, 5),
    _ZxAnVlanGlobalTransSVid_Type()
)
zxAnVlanGlobalTransSVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanGlobalTransSVid.setStatus("current")


class _ZxAnVlanMpTranslateDirection_Type(Integer32):
    """Custom type zxAnVlanMpTranslateDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("upStream", 1),
          ("downStream", 2))
    )


_ZxAnVlanMpTranslateDirection_Type.__name__ = "Integer32"
_ZxAnVlanMpTranslateDirection_Object = MibTableColumn
zxAnVlanMpTranslateDirection = _ZxAnVlanMpTranslateDirection_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 7, 1, 6),
    _ZxAnVlanMpTranslateDirection_Type()
)
zxAnVlanMpTranslateDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanMpTranslateDirection.setStatus("current")
_ZxAnVlanGlobalTransRowStatus_Type = RowStatus
_ZxAnVlanGlobalTransRowStatus_Object = MibTableColumn
zxAnVlanGlobalTransRowStatus = _ZxAnVlanGlobalTransRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 7, 1, 7),
    _ZxAnVlanGlobalTransRowStatus_Type()
)
zxAnVlanGlobalTransRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanGlobalTransRowStatus.setStatus("current")


class _ZxAnVlanGlobalTransVlanMerge_Type(Integer32):
    """Custom type zxAnVlanGlobalTransVlanMerge based on Integer32"""
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


_ZxAnVlanGlobalTransVlanMerge_Type.__name__ = "Integer32"
_ZxAnVlanGlobalTransVlanMerge_Object = MibTableColumn
zxAnVlanGlobalTransVlanMerge = _ZxAnVlanGlobalTransVlanMerge_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 7, 1, 8),
    _ZxAnVlanGlobalTransVlanMerge_Type()
)
zxAnVlanGlobalTransVlanMerge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanGlobalTransVlanMerge.setStatus("current")
_ZxAnVlanMpExQinQTable_Object = MibTable
zxAnVlanMpExQinQTable = _ZxAnVlanMpExQinQTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 8)
)
if mibBuilder.loadTexts:
    zxAnVlanMpExQinQTable.setStatus("current")
_ZxAnVlanMpExQinQEntry_Object = MibTableRow
zxAnVlanMpExQinQEntry = _ZxAnVlanMpExQinQEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 8, 1)
)
zxAnVlanMpExQinQEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanExQinQSessionNo"),
)
if mibBuilder.loadTexts:
    zxAnVlanMpExQinQEntry.setStatus("current")
_ZxAnVlanExQinQSessionNo_Type = Integer32
_ZxAnVlanExQinQSessionNo_Object = MibTableColumn
zxAnVlanExQinQSessionNo = _ZxAnVlanExQinQSessionNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 8, 1, 1),
    _ZxAnVlanExQinQSessionNo_Type()
)
zxAnVlanExQinQSessionNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVlanExQinQSessionNo.setStatus("current")
_ZxAnVlanSmartQinQIfIndex_Type = Integer32
_ZxAnVlanSmartQinQIfIndex_Object = MibTableColumn
zxAnVlanSmartQinQIfIndex = _ZxAnVlanSmartQinQIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 8, 1, 2),
    _ZxAnVlanSmartQinQIfIndex_Type()
)
zxAnVlanSmartQinQIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanSmartQinQIfIndex.setStatus("current")
_ZxAnVlanSmartQinQUserVid_Type = Integer32
_ZxAnVlanSmartQinQUserVid_Object = MibTableColumn
zxAnVlanSmartQinQUserVid = _ZxAnVlanSmartQinQUserVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 8, 1, 3),
    _ZxAnVlanSmartQinQUserVid_Type()
)
zxAnVlanSmartQinQUserVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanSmartQinQUserVid.setStatus("current")


class _ZxAnVlanSmartQinQSelectiveType_Type(Integer32):
    """Custom type zxAnVlanSmartQinQSelectiveType based on Integer32"""
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
        *(("cvlanscope", 1),
          ("ethertype", 2),
          ("cos", 3),
          ("cvlancos", 4),
          ("cvlanethertype", 5),
          ("cvlantransparent", 6))
    )


_ZxAnVlanSmartQinQSelectiveType_Type.__name__ = "Integer32"
_ZxAnVlanSmartQinQSelectiveType_Object = MibTableColumn
zxAnVlanSmartQinQSelectiveType = _ZxAnVlanSmartQinQSelectiveType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 8, 1, 4),
    _ZxAnVlanSmartQinQSelectiveType_Type()
)
zxAnVlanSmartQinQSelectiveType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanSmartQinQSelectiveType.setStatus("current")
_ZxAnVlanSmartQinQStartUserVid_Type = Integer32
_ZxAnVlanSmartQinQStartUserVid_Object = MibTableColumn
zxAnVlanSmartQinQStartUserVid = _ZxAnVlanSmartQinQStartUserVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 8, 1, 5),
    _ZxAnVlanSmartQinQStartUserVid_Type()
)
zxAnVlanSmartQinQStartUserVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanSmartQinQStartUserVid.setStatus("current")
_ZxAnVlanSmartQinQEndUserVid_Type = Integer32
_ZxAnVlanSmartQinQEndUserVid_Object = MibTableColumn
zxAnVlanSmartQinQEndUserVid = _ZxAnVlanSmartQinQEndUserVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 8, 1, 6),
    _ZxAnVlanSmartQinQEndUserVid_Type()
)
zxAnVlanSmartQinQEndUserVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanSmartQinQEndUserVid.setStatus("current")
_ZxAnVlanExQinQInCVlanMask_Type = Integer32
_ZxAnVlanExQinQInCVlanMask_Object = MibTableColumn
zxAnVlanExQinQInCVlanMask = _ZxAnVlanExQinQInCVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 8, 1, 7),
    _ZxAnVlanExQinQInCVlanMask_Type()
)
zxAnVlanExQinQInCVlanMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanExQinQInCVlanMask.setStatus("current")
_ZxAnVlanSmartQinQEtherType_Type = Integer32
_ZxAnVlanSmartQinQEtherType_Object = MibTableColumn
zxAnVlanSmartQinQEtherType = _ZxAnVlanSmartQinQEtherType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 8, 1, 8),
    _ZxAnVlanSmartQinQEtherType_Type()
)
zxAnVlanSmartQinQEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanSmartQinQEtherType.setStatus("current")


class _ZxAnVlanSmartQinQUserCos_Type(Integer32):
    """Custom type zxAnVlanSmartQinQUserCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_ZxAnVlanSmartQinQUserCos_Type.__name__ = "Integer32"
_ZxAnVlanSmartQinQUserCos_Object = MibTableColumn
zxAnVlanSmartQinQUserCos = _ZxAnVlanSmartQinQUserCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 8, 1, 9),
    _ZxAnVlanSmartQinQUserCos_Type()
)
zxAnVlanSmartQinQUserCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanSmartQinQUserCos.setStatus("current")
_ZxAnVlanSmartQinQSVid_Type = VlanId
_ZxAnVlanSmartQinQSVid_Object = MibTableColumn
zxAnVlanSmartQinQSVid = _ZxAnVlanSmartQinQSVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 8, 1, 10),
    _ZxAnVlanSmartQinQSVid_Type()
)
zxAnVlanSmartQinQSVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanSmartQinQSVid.setStatus("current")


class _ZxAnVlanSmartQinQStagCos_Type(Integer32):
    """Custom type zxAnVlanSmartQinQStagCos based on Integer32"""
    defaultValue = 255


_ZxAnVlanSmartQinQStagCos_Type.__name__ = "Integer32"
_ZxAnVlanSmartQinQStagCos_Object = MibTableColumn
zxAnVlanSmartQinQStagCos = _ZxAnVlanSmartQinQStagCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 8, 1, 11),
    _ZxAnVlanSmartQinQStagCos_Type()
)
zxAnVlanSmartQinQStagCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanSmartQinQStagCos.setStatus("current")


class _ZxAnVlanExQinQRefOnuGroupId_Type(Integer32):
    """Custom type zxAnVlanExQinQRefOnuGroupId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ZxAnVlanExQinQRefOnuGroupId_Type.__name__ = "Integer32"
_ZxAnVlanExQinQRefOnuGroupId_Object = MibTableColumn
zxAnVlanExQinQRefOnuGroupId = _ZxAnVlanExQinQRefOnuGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 8, 1, 12),
    _ZxAnVlanExQinQRefOnuGroupId_Type()
)
zxAnVlanExQinQRefOnuGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanExQinQRefOnuGroupId.setStatus("current")
_ZxAnVlanSmartQinQRowStatus_Type = RowStatus
_ZxAnVlanSmartQinQRowStatus_Object = MibTableColumn
zxAnVlanSmartQinQRowStatus = _ZxAnVlanSmartQinQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 8, 1, 50),
    _ZxAnVlanSmartQinQRowStatus_Type()
)
zxAnVlanSmartQinQRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanSmartQinQRowStatus.setStatus("current")
_ZxAnVlanVoipConfTable_Object = MibTable
zxAnVlanVoipConfTable = _ZxAnVlanVoipConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 9)
)
if mibBuilder.loadTexts:
    zxAnVlanVoipConfTable.setStatus("current")
_ZxAnVlanVoipConfEntry_Object = MibTableRow
zxAnVlanVoipConfEntry = _ZxAnVlanVoipConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 9, 1)
)
zxAnVlanVoipConfEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanVoipVlanId"),
)
if mibBuilder.loadTexts:
    zxAnVlanVoipConfEntry.setStatus("current")
_ZxAnVlanVoipVlanId_Type = VlanId
_ZxAnVlanVoipVlanId_Object = MibTableColumn
zxAnVlanVoipVlanId = _ZxAnVlanVoipVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 9, 1, 1),
    _ZxAnVlanVoipVlanId_Type()
)
zxAnVlanVoipVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVlanVoipVlanId.setStatus("current")


class _ZxAnVoipVlanUsages_Type(Bits):
    """Custom type zxAnVoipVlanUsages based on Bits"""
    namedValues = NamedValues(
        *(("media", 0),
          ("signal", 1))
    )

_ZxAnVoipVlanUsages_Type.__name__ = "Bits"
_ZxAnVoipVlanUsages_Object = MibTableColumn
zxAnVoipVlanUsages = _ZxAnVoipVlanUsages_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 9, 1, 2),
    _ZxAnVoipVlanUsages_Type()
)
zxAnVoipVlanUsages.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVoipVlanUsages.setStatus("current")
_ZxAnVlanVoipRowStatus_Type = RowStatus
_ZxAnVlanVoipRowStatus_Object = MibTableColumn
zxAnVlanVoipRowStatus = _ZxAnVlanVoipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 9, 1, 50),
    _ZxAnVlanVoipRowStatus_Type()
)
zxAnVlanVoipRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanVoipRowStatus.setStatus("current")


class _ZxAnVlanSmartQinQEnable_Type(Integer32):
    """Custom type zxAnVlanSmartQinQEnable based on Integer32"""
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
        *(("enableGlobal", 1),
          ("disablGlobal", 2),
          ("enableEIGMP", 3),
          ("disablEIGMP", 4),
          ("enableV2", 5),
          ("disableV2", 6),
          ("enableV3", 7),
          ("disableV3", 8))
    )


_ZxAnVlanSmartQinQEnable_Type.__name__ = "Integer32"
_ZxAnVlanSmartQinQEnable_Object = MibScalar
zxAnVlanSmartQinQEnable = _ZxAnVlanSmartQinQEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 10),
    _ZxAnVlanSmartQinQEnable_Type()
)
zxAnVlanSmartQinQEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanSmartQinQEnable.setStatus("current")
_ZxAnReservedVlan_Type = DisplayString
_ZxAnReservedVlan_Object = MibScalar
zxAnReservedVlan = _ZxAnReservedVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 11),
    _ZxAnReservedVlan_Type()
)
zxAnReservedVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnReservedVlan.setStatus("current")
_ZxAnVlanMpExQinQPortTable_Object = MibTable
zxAnVlanMpExQinQPortTable = _ZxAnVlanMpExQinQPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 12)
)
if mibBuilder.loadTexts:
    zxAnVlanMpExQinQPortTable.setStatus("current")
_ZxAnVlanMpExQinQPortEntry_Object = MibTableRow
zxAnVlanMpExQinQPortEntry = _ZxAnVlanMpExQinQPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 12, 1)
)
zxAnVlanMpExQinQPortEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanExQinQPortIndex"),
)
if mibBuilder.loadTexts:
    zxAnVlanMpExQinQPortEntry.setStatus("current")
_ZxAnVlanExQinQPortIndex_Type = ZxAnIfindex
_ZxAnVlanExQinQPortIndex_Object = MibTableColumn
zxAnVlanExQinQPortIndex = _ZxAnVlanExQinQPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 12, 1, 1),
    _ZxAnVlanExQinQPortIndex_Type()
)
zxAnVlanExQinQPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVlanExQinQPortIndex.setStatus("current")


class _ZxAnVlanSmartQinQIfEnable_Type(Integer32):
    """Custom type zxAnVlanSmartQinQIfEnable based on Integer32"""
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


_ZxAnVlanSmartQinQIfEnable_Type.__name__ = "Integer32"
_ZxAnVlanSmartQinQIfEnable_Object = MibTableColumn
zxAnVlanSmartQinQIfEnable = _ZxAnVlanSmartQinQIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 12, 1, 2),
    _ZxAnVlanSmartQinQIfEnable_Type()
)
zxAnVlanSmartQinQIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanSmartQinQIfEnable.setStatus("current")


class _ZxAnVlanExQinQOnuMapGroupId_Type(Integer32):
    """Custom type zxAnVlanExQinQOnuMapGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ZxAnVlanExQinQOnuMapGroupId_Type.__name__ = "Integer32"
_ZxAnVlanExQinQOnuMapGroupId_Object = MibTableColumn
zxAnVlanExQinQOnuMapGroupId = _ZxAnVlanExQinQOnuMapGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 12, 1, 3),
    _ZxAnVlanExQinQOnuMapGroupId_Type()
)
zxAnVlanExQinQOnuMapGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanExQinQOnuMapGroupId.setStatus("current")


class _ZxAnVlanExQinQPortResVlan_Type(Integer32):
    """Custom type zxAnVlanExQinQPortResVlan based on Integer32"""
    defaultValue = 4094

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4055, 4094),
    )


_ZxAnVlanExQinQPortResVlan_Type.__name__ = "Integer32"
_ZxAnVlanExQinQPortResVlan_Object = MibTableColumn
zxAnVlanExQinQPortResVlan = _ZxAnVlanExQinQPortResVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 12, 1, 4),
    _ZxAnVlanExQinQPortResVlan_Type()
)
zxAnVlanExQinQPortResVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanExQinQPortResVlan.setStatus("current")
_ZxAnVlanMpExTranslatePortTable_Object = MibTable
zxAnVlanMpExTranslatePortTable = _ZxAnVlanMpExTranslatePortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 13)
)
if mibBuilder.loadTexts:
    zxAnVlanMpExTranslatePortTable.setStatus("current")
_ZxAnVlanMpExTranslatePortEntry_Object = MibTableRow
zxAnVlanMpExTranslatePortEntry = _ZxAnVlanMpExTranslatePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 13, 1)
)
zxAnVlanMpExTranslatePortEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanExTranslatePortIndex"),
)
if mibBuilder.loadTexts:
    zxAnVlanMpExTranslatePortEntry.setStatus("current")
_ZxAnVlanExTranslatePortIndex_Type = ZxAnIfindex
_ZxAnVlanExTranslatePortIndex_Object = MibTableColumn
zxAnVlanExTranslatePortIndex = _ZxAnVlanExTranslatePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 13, 1, 1),
    _ZxAnVlanExTranslatePortIndex_Type()
)
zxAnVlanExTranslatePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVlanExTranslatePortIndex.setStatus("current")


class _ZxAnVlanExTranslatePortEnabled_Type(Integer32):
    """Custom type zxAnVlanExTranslatePortEnabled based on Integer32"""
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


_ZxAnVlanExTranslatePortEnabled_Type.__name__ = "Integer32"
_ZxAnVlanExTranslatePortEnabled_Object = MibTableColumn
zxAnVlanExTranslatePortEnabled = _ZxAnVlanExTranslatePortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 13, 1, 2),
    _ZxAnVlanExTranslatePortEnabled_Type()
)
zxAnVlanExTranslatePortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanExTranslatePortEnabled.setStatus("current")


class _ZxAnVlanTranslateMode_Type(Integer32):
    """Custom type zxAnVlanTranslateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ntoone", 1),
          ("hybrid", 2))
    )


_ZxAnVlanTranslateMode_Type.__name__ = "Integer32"
_ZxAnVlanTranslateMode_Object = MibScalar
zxAnVlanTranslateMode = _ZxAnVlanTranslateMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 14),
    _ZxAnVlanTranslateMode_Type()
)
zxAnVlanTranslateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanTranslateMode.setStatus("current")
_ZxAnProtocolVlanMapTable_Object = MibTable
zxAnProtocolVlanMapTable = _ZxAnProtocolVlanMapTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 16)
)
if mibBuilder.loadTexts:
    zxAnProtocolVlanMapTable.setStatus("current")
_ZxAnProtocolVlanMapEntry_Object = MibTableRow
zxAnProtocolVlanMapEntry = _ZxAnProtocolVlanMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 16, 1)
)
zxAnProtocolVlanMapEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnProtocolVlanPortIndex"),
    (0, "ZTE-AN-VLAN-MIB", "zxAnEtherProtocolType"),
)
if mibBuilder.loadTexts:
    zxAnProtocolVlanMapEntry.setStatus("current")
_ZxAnProtocolVlanPortIndex_Type = ZxAnIfindex
_ZxAnProtocolVlanPortIndex_Object = MibTableColumn
zxAnProtocolVlanPortIndex = _ZxAnProtocolVlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 16, 1, 1),
    _ZxAnProtocolVlanPortIndex_Type()
)
zxAnProtocolVlanPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnProtocolVlanPortIndex.setStatus("current")
_ZxAnEtherProtocolType_Type = Integer32
_ZxAnEtherProtocolType_Object = MibTableColumn
zxAnEtherProtocolType = _ZxAnEtherProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 16, 1, 2),
    _ZxAnEtherProtocolType_Type()
)
zxAnEtherProtocolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEtherProtocolType.setStatus("current")
_ZxAnVlanIfProtoMapVid_Type = VlanId
_ZxAnVlanIfProtoMapVid_Object = MibTableColumn
zxAnVlanIfProtoMapVid = _ZxAnVlanIfProtoMapVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 16, 1, 3),
    _ZxAnVlanIfProtoMapVid_Type()
)
zxAnVlanIfProtoMapVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanIfProtoMapVid.setStatus("current")


class _ZxAnVlanIfProtoMapCos_Type(Integer32):
    """Custom type zxAnVlanIfProtoMapCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnVlanIfProtoMapCos_Type.__name__ = "Integer32"
_ZxAnVlanIfProtoMapCos_Object = MibTableColumn
zxAnVlanIfProtoMapCos = _ZxAnVlanIfProtoMapCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 16, 1, 4),
    _ZxAnVlanIfProtoMapCos_Type()
)
zxAnVlanIfProtoMapCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanIfProtoMapCos.setStatus("current")


class _ZxAnVlanIfProtoMapCVid_Type(Integer32):
    """Custom type zxAnVlanIfProtoMapCVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ZxAnVlanIfProtoMapCVid_Type.__name__ = "Integer32"
_ZxAnVlanIfProtoMapCVid_Object = MibTableColumn
zxAnVlanIfProtoMapCVid = _ZxAnVlanIfProtoMapCVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 16, 1, 5),
    _ZxAnVlanIfProtoMapCVid_Type()
)
zxAnVlanIfProtoMapCVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanIfProtoMapCVid.setStatus("current")


class _ZxAnVlanIfProtoMapCtagCos_Type(Integer32):
    """Custom type zxAnVlanIfProtoMapCtagCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnVlanIfProtoMapCtagCos_Type.__name__ = "Integer32"
_ZxAnVlanIfProtoMapCtagCos_Object = MibTableColumn
zxAnVlanIfProtoMapCtagCos = _ZxAnVlanIfProtoMapCtagCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 16, 1, 6),
    _ZxAnVlanIfProtoMapCtagCos_Type()
)
zxAnVlanIfProtoMapCtagCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanIfProtoMapCtagCos.setStatus("current")
_ZxAnVlanIfProtoMapRowStatus_Type = RowStatus
_ZxAnVlanIfProtoMapRowStatus_Object = MibTableColumn
zxAnVlanIfProtoMapRowStatus = _ZxAnVlanIfProtoMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 16, 1, 100),
    _ZxAnVlanIfProtoMapRowStatus_Type()
)
zxAnVlanIfProtoMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanIfProtoMapRowStatus.setStatus("current")
_ZxAnBatchVLANObjects_ObjectIdentity = ObjectIdentity
zxAnBatchVLANObjects = _ZxAnBatchVLANObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 17)
)
_ZxAnVlanBatchConfVlanList_Type = DisplayString
_ZxAnVlanBatchConfVlanList_Object = MibScalar
zxAnVlanBatchConfVlanList = _ZxAnVlanBatchConfVlanList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 17, 1),
    _ZxAnVlanBatchConfVlanList_Type()
)
zxAnVlanBatchConfVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanBatchConfVlanList.setStatus("current")


class _ZxAnVlanBatchConfPrefixName_Type(DisplayString):
    """Custom type zxAnVlanBatchConfPrefixName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnVlanBatchConfPrefixName_Type.__name__ = "DisplayString"
_ZxAnVlanBatchConfPrefixName_Object = MibScalar
zxAnVlanBatchConfPrefixName = _ZxAnVlanBatchConfPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 17, 2),
    _ZxAnVlanBatchConfPrefixName_Type()
)
zxAnVlanBatchConfPrefixName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanBatchConfPrefixName.setStatus("current")


class _ZxAnBatchVlanTransparent_Type(Integer32):
    """Custom type zxAnBatchVlanTransparent based on Integer32"""
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
          ("disable", 2))
    )


_ZxAnBatchVlanTransparent_Type.__name__ = "Integer32"
_ZxAnBatchVlanTransparent_Object = MibScalar
zxAnBatchVlanTransparent = _ZxAnBatchVlanTransparent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 17, 3),
    _ZxAnBatchVlanTransparent_Type()
)
zxAnBatchVlanTransparent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnBatchVlanTransparent.setStatus("current")


class _ZxAnVlanBatchConfType_Type(Integer32):
    """Custom type zxAnVlanBatchConfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_ZxAnVlanBatchConfType_Type.__name__ = "Integer32"
_ZxAnVlanBatchConfType_Object = MibScalar
zxAnVlanBatchConfType = _ZxAnVlanBatchConfType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 17, 4),
    _ZxAnVlanBatchConfType_Type()
)
zxAnVlanBatchConfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanBatchConfType.setStatus("current")


class _ZxAnVlanBatchConfStatus_Type(Integer32):
    """Custom type zxAnVlanBatchConfStatus based on Integer32"""
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
        *(("notstarted", 1),
          ("inprogress", 2),
          ("success", 3),
          ("failed", 4))
    )


_ZxAnVlanBatchConfStatus_Type.__name__ = "Integer32"
_ZxAnVlanBatchConfStatus_Object = MibScalar
zxAnVlanBatchConfStatus = _ZxAnVlanBatchConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 17, 5),
    _ZxAnVlanBatchConfStatus_Type()
)
zxAnVlanBatchConfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanBatchConfStatus.setStatus("current")
_ZxAnVlanBatchConfFailedVlanList_Type = DisplayString
_ZxAnVlanBatchConfFailedVlanList_Object = MibScalar
zxAnVlanBatchConfFailedVlanList = _ZxAnVlanBatchConfFailedVlanList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 17, 6),
    _ZxAnVlanBatchConfFailedVlanList_Type()
)
zxAnVlanBatchConfFailedVlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanBatchConfFailedVlanList.setStatus("current")
_ZxAnVlanBatchConfCurrVlanList_Type = DisplayString
_ZxAnVlanBatchConfCurrVlanList_Object = MibScalar
zxAnVlanBatchConfCurrVlanList = _ZxAnVlanBatchConfCurrVlanList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 17, 7),
    _ZxAnVlanBatchConfCurrVlanList_Type()
)
zxAnVlanBatchConfCurrVlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanBatchConfCurrVlanList.setStatus("current")
_ZxAnXconnectTable_Object = MibTable
zxAnXconnectTable = _ZxAnXconnectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 18)
)
if mibBuilder.loadTexts:
    zxAnXconnectTable.setStatus("current")
_ZxAnXconnectEntry_Object = MibTableRow
zxAnXconnectEntry = _ZxAnXconnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 18, 1)
)
zxAnXconnectEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnXconnectPortIndex"),
    (0, "ZTE-AN-VLAN-MIB", "zxAnXconnectLocationIndex"),
)
if mibBuilder.loadTexts:
    zxAnXconnectEntry.setStatus("current")
_ZxAnXconnectPortIndex_Type = ZxAnIfindex
_ZxAnXconnectPortIndex_Object = MibTableColumn
zxAnXconnectPortIndex = _ZxAnXconnectPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 18, 1, 1),
    _ZxAnXconnectPortIndex_Type()
)
zxAnXconnectPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnXconnectPortIndex.setStatus("current")
_ZxAnXconnectLocationIndex_Type = Integer32
_ZxAnXconnectLocationIndex_Object = MibTableColumn
zxAnXconnectLocationIndex = _ZxAnXconnectLocationIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 18, 1, 2),
    _ZxAnXconnectLocationIndex_Type()
)
zxAnXconnectLocationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnXconnectLocationIndex.setStatus("current")


class _ZxAnXconnectMode_Type(Integer32):
    """Custom type zxAnXconnectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tlsvlan", 1),
          ("cvlan", 2),
          ("svlan", 3))
    )


_ZxAnXconnectMode_Type.__name__ = "Integer32"
_ZxAnXconnectMode_Object = MibTableColumn
zxAnXconnectMode = _ZxAnXconnectMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 18, 1, 3),
    _ZxAnXconnectMode_Type()
)
zxAnXconnectMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnXconnectMode.setStatus("current")
_ZxAnVlanBasedFwdSVid_Type = VlanId
_ZxAnVlanBasedFwdSVid_Object = MibTableColumn
zxAnVlanBasedFwdSVid = _ZxAnVlanBasedFwdSVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 18, 1, 4),
    _ZxAnVlanBasedFwdSVid_Type()
)
zxAnVlanBasedFwdSVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanBasedFwdSVid.setStatus("current")
_ZxAnVlanBasedFwdCVid_Type = VlanId
_ZxAnVlanBasedFwdCVid_Object = MibTableColumn
zxAnVlanBasedFwdCVid = _ZxAnVlanBasedFwdCVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 18, 1, 5),
    _ZxAnVlanBasedFwdCVid_Type()
)
zxAnVlanBasedFwdCVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanBasedFwdCVid.setStatus("current")
_ZxAnXconnectNewCvlanId_Type = VlanId
_ZxAnXconnectNewCvlanId_Object = MibTableColumn
zxAnXconnectNewCvlanId = _ZxAnXconnectNewCvlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 18, 1, 6),
    _ZxAnXconnectNewCvlanId_Type()
)
zxAnXconnectNewCvlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnXconnectNewCvlanId.setStatus("current")
_ZxAnXconnectNewSvlanId_Type = VlanId
_ZxAnXconnectNewSvlanId_Object = MibTableColumn
zxAnXconnectNewSvlanId = _ZxAnXconnectNewSvlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 18, 1, 7),
    _ZxAnXconnectNewSvlanId_Type()
)
zxAnXconnectNewSvlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnXconnectNewSvlanId.setStatus("current")
_ZxAnVlanBasedFwdUplinkPort_Type = ZxAnIfindex
_ZxAnVlanBasedFwdUplinkPort_Object = MibTableColumn
zxAnVlanBasedFwdUplinkPort = _ZxAnVlanBasedFwdUplinkPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 18, 1, 8),
    _ZxAnVlanBasedFwdUplinkPort_Type()
)
zxAnVlanBasedFwdUplinkPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanBasedFwdUplinkPort.setStatus("current")
_ZxAnVlanBasedFwdRowStatus_Type = RowStatus
_ZxAnVlanBasedFwdRowStatus_Object = MibTableColumn
zxAnVlanBasedFwdRowStatus = _ZxAnVlanBasedFwdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 18, 1, 100),
    _ZxAnVlanBasedFwdRowStatus_Type()
)
zxAnVlanBasedFwdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanBasedFwdRowStatus.setStatus("current")
_ZxAnVlanExQinQSupportEIGMP_Type = TruthValue
_ZxAnVlanExQinQSupportEIGMP_Object = MibScalar
zxAnVlanExQinQSupportEIGMP = _ZxAnVlanExQinQSupportEIGMP_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 22),
    _ZxAnVlanExQinQSupportEIGMP_Type()
)
zxAnVlanExQinQSupportEIGMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanExQinQSupportEIGMP.setStatus("current")


class _ZxAnVlanGlobalCtagTpid_Type(DisplayString):
    """Custom type zxAnVlanGlobalCtagTpid based on DisplayString"""
    defaultValue = OctetString("0x8100")


_ZxAnVlanGlobalCtagTpid_Type.__name__ = "DisplayString"
_ZxAnVlanGlobalCtagTpid_Object = MibScalar
zxAnVlanGlobalCtagTpid = _ZxAnVlanGlobalCtagTpid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 23),
    _ZxAnVlanGlobalCtagTpid_Type()
)
zxAnVlanGlobalCtagTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanGlobalCtagTpid.setStatus("current")


class _ZxAnVlanGlobalTpid_Type(DisplayString):
    """Custom type zxAnVlanGlobalTpid based on DisplayString"""
    defaultValue = OctetString("0x8100")


_ZxAnVlanGlobalTpid_Type.__name__ = "DisplayString"
_ZxAnVlanGlobalTpid_Object = MibScalar
zxAnVlanGlobalTpid = _ZxAnVlanGlobalTpid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 24),
    _ZxAnVlanGlobalTpid_Type()
)
zxAnVlanGlobalTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanGlobalTpid.setStatus("current")
_ZxAnOnuMngVlanTable_Object = MibTable
zxAnOnuMngVlanTable = _ZxAnOnuMngVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 25)
)
if mibBuilder.loadTexts:
    zxAnOnuMngVlanTable.setStatus("current")
_ZxAnOnuMngVlanEntry_Object = MibTableRow
zxAnOnuMngVlanEntry = _ZxAnOnuMngVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 25, 1)
)
zxAnOnuMngVlanEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnOnuMngVlan"),
)
if mibBuilder.loadTexts:
    zxAnOnuMngVlanEntry.setStatus("current")
_ZxAnOnuMngVlan_Type = VlanId
_ZxAnOnuMngVlan_Object = MibTableColumn
zxAnOnuMngVlan = _ZxAnOnuMngVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 25, 1, 1),
    _ZxAnOnuMngVlan_Type()
)
zxAnOnuMngVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnOnuMngVlan.setStatus("current")
_ZxAnOnuMngVlanRowStatus_Type = RowStatus
_ZxAnOnuMngVlanRowStatus_Object = MibTableColumn
zxAnOnuMngVlanRowStatus = _ZxAnOnuMngVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 25, 1, 20),
    _ZxAnOnuMngVlanRowStatus_Type()
)
zxAnOnuMngVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOnuMngVlanRowStatus.setStatus("current")
_ZxAnIpRouteVlanTable_Object = MibTable
zxAnIpRouteVlanTable = _ZxAnIpRouteVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 26)
)
if mibBuilder.loadTexts:
    zxAnIpRouteVlanTable.setStatus("current")
_ZxAnIpRouteVlanEntry_Object = MibTableRow
zxAnIpRouteVlanEntry = _ZxAnIpRouteVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 26, 1)
)
zxAnIpRouteVlanEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnIpRouteVlan"),
)
if mibBuilder.loadTexts:
    zxAnIpRouteVlanEntry.setStatus("current")
_ZxAnIpRouteVlan_Type = VlanId
_ZxAnIpRouteVlan_Object = MibTableColumn
zxAnIpRouteVlan = _ZxAnIpRouteVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 26, 1, 1),
    _ZxAnIpRouteVlan_Type()
)
zxAnIpRouteVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIpRouteVlan.setStatus("current")
_ZxAnIpRouteVlanRowStatus_Type = RowStatus
_ZxAnIpRouteVlanRowStatus_Object = MibTableColumn
zxAnIpRouteVlanRowStatus = _ZxAnIpRouteVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 26, 1, 20),
    _ZxAnIpRouteVlanRowStatus_Type()
)
zxAnIpRouteVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIpRouteVlanRowStatus.setStatus("current")
_ZxAnVlanInterfaceTable_Object = MibTable
zxAnVlanInterfaceTable = _ZxAnVlanInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 27)
)
if mibBuilder.loadTexts:
    zxAnVlanInterfaceTable.setStatus("current")
_ZxAnVlanInterfaceEntry_Object = MibTableRow
zxAnVlanInterfaceEntry = _ZxAnVlanInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 27, 1)
)
zxAnVlanInterfaceEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanInterfaceVlanId"),
)
if mibBuilder.loadTexts:
    zxAnVlanInterfaceEntry.setStatus("current")
_ZxAnVlanInterfaceVlanId_Type = VlanId
_ZxAnVlanInterfaceVlanId_Object = MibTableColumn
zxAnVlanInterfaceVlanId = _ZxAnVlanInterfaceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 27, 1, 1),
    _ZxAnVlanInterfaceVlanId_Type()
)
zxAnVlanInterfaceVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVlanInterfaceVlanId.setStatus("current")
_ZxAnVlanBroadcastRateLimit_Type = Integer32
_ZxAnVlanBroadcastRateLimit_Object = MibTableColumn
zxAnVlanBroadcastRateLimit = _ZxAnVlanBroadcastRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 27, 1, 5),
    _ZxAnVlanBroadcastRateLimit_Type()
)
zxAnVlanBroadcastRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanBroadcastRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVlanBroadcastRateLimit.setUnits("kbps")
_ZxAnPortMvlanTranslateTable_Object = MibTable
zxAnPortMvlanTranslateTable = _ZxAnPortMvlanTranslateTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 28)
)
if mibBuilder.loadTexts:
    zxAnPortMvlanTranslateTable.setStatus("current")
_ZxAnPortMvlanTranslateEntry_Object = MibTableRow
zxAnPortMvlanTranslateEntry = _ZxAnPortMvlanTranslateEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 28, 1)
)
zxAnPortMvlanTranslateEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnPortMvlanTranslateIfIndex"),
    (0, "ZTE-AN-VLAN-MIB", "zxAnPortMvlanTranslateMvlan"),
    (0, "ZTE-AN-VLAN-MIB", "zxAnPortMvlanTranslateCvlan"),
)
if mibBuilder.loadTexts:
    zxAnPortMvlanTranslateEntry.setStatus("current")
_ZxAnPortMvlanTranslateIfIndex_Type = ZxAnIfindex
_ZxAnPortMvlanTranslateIfIndex_Object = MibTableColumn
zxAnPortMvlanTranslateIfIndex = _ZxAnPortMvlanTranslateIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 28, 1, 1),
    _ZxAnPortMvlanTranslateIfIndex_Type()
)
zxAnPortMvlanTranslateIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPortMvlanTranslateIfIndex.setStatus("current")
_ZxAnPortMvlanTranslateMvlan_Type = VlanId
_ZxAnPortMvlanTranslateMvlan_Object = MibTableColumn
zxAnPortMvlanTranslateMvlan = _ZxAnPortMvlanTranslateMvlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 28, 1, 2),
    _ZxAnPortMvlanTranslateMvlan_Type()
)
zxAnPortMvlanTranslateMvlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPortMvlanTranslateMvlan.setStatus("current")


class _ZxAnPortMvlanTranslateCvlan_Type(Integer32):
    """Custom type zxAnPortMvlanTranslateCvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ZxAnPortMvlanTranslateCvlan_Type.__name__ = "Integer32"
_ZxAnPortMvlanTranslateCvlan_Object = MibTableColumn
zxAnPortMvlanTranslateCvlan = _ZxAnPortMvlanTranslateCvlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 28, 1, 3),
    _ZxAnPortMvlanTranslateCvlan_Type()
)
zxAnPortMvlanTranslateCvlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPortMvlanTranslateCvlan.setStatus("current")
_ZxAnMVlanIfTransRowStatus_Type = RowStatus
_ZxAnMVlanIfTransRowStatus_Object = MibTableColumn
zxAnMVlanIfTransRowStatus = _ZxAnMVlanIfTransRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 28, 1, 10),
    _ZxAnMVlanIfTransRowStatus_Type()
)
zxAnMVlanIfTransRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMVlanIfTransRowStatus.setStatus("current")
_ZxAnVlanIfProtoMapEnableTable_Object = MibTable
zxAnVlanIfProtoMapEnableTable = _ZxAnVlanIfProtoMapEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 29)
)
if mibBuilder.loadTexts:
    zxAnVlanIfProtoMapEnableTable.setStatus("current")
_ZxAnVlanIfProtoMapEnableEntry_Object = MibTableRow
zxAnVlanIfProtoMapEnableEntry = _ZxAnVlanIfProtoMapEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 29, 1)
)
zxAnVlanIfProtoMapEnableEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnProtocolVlanPortIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnVlanIfProtoMapEnableEntry.setStatus("current")
_ZxAnProtocolVlanPortIfIndex_Type = ZxAnIfindex
_ZxAnProtocolVlanPortIfIndex_Object = MibTableColumn
zxAnProtocolVlanPortIfIndex = _ZxAnProtocolVlanPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 29, 1, 1),
    _ZxAnProtocolVlanPortIfIndex_Type()
)
zxAnProtocolVlanPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnProtocolVlanPortIfIndex.setStatus("current")


class _ZxAnVlanIfProtoMapEnable_Type(TruthValue):
    """Custom type zxAnVlanIfProtoMapEnable based on TruthValue"""
    defaultValue = 2


_ZxAnVlanIfProtoMapEnable_Type.__name__ = "TruthValue"
_ZxAnVlanIfProtoMapEnable_Object = MibTableColumn
zxAnVlanIfProtoMapEnable = _ZxAnVlanIfProtoMapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 29, 1, 2),
    _ZxAnVlanIfProtoMapEnable_Type()
)
zxAnVlanIfProtoMapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanIfProtoMapEnable.setStatus("current")
_ZxAnInternalVlanTable_Object = MibTable
zxAnInternalVlanTable = _ZxAnInternalVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 30)
)
if mibBuilder.loadTexts:
    zxAnInternalVlanTable.setStatus("current")
_ZxAnInternalVlanEntry_Object = MibTableRow
zxAnInternalVlanEntry = _ZxAnInternalVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 30, 1)
)
zxAnInternalVlanEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnInternalVlanServiceType"),
)
if mibBuilder.loadTexts:
    zxAnInternalVlanEntry.setStatus("current")


class _ZxAnInternalVlanServiceType_Type(Integer32):
    """Custom type zxAnInternalVlanServiceType based on Integer32"""
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
        *(("vpn", 1),
          ("voipUpstream", 2),
          ("voipDownstream", 3),
          ("ieee1588", 4),
          ("gpon", 5))
    )


_ZxAnInternalVlanServiceType_Type.__name__ = "Integer32"
_ZxAnInternalVlanServiceType_Object = MibTableColumn
zxAnInternalVlanServiceType = _ZxAnInternalVlanServiceType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 30, 1, 1),
    _ZxAnInternalVlanServiceType_Type()
)
zxAnInternalVlanServiceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnInternalVlanServiceType.setStatus("current")
_ZxAnInternalVlanList_Type = DisplayString
_ZxAnInternalVlanList_Object = MibTableColumn
zxAnInternalVlanList = _ZxAnInternalVlanList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 30, 1, 2),
    _ZxAnInternalVlanList_Type()
)
zxAnInternalVlanList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnInternalVlanList.setStatus("current")
_ZxAnInternalVlanRowStatus_Type = RowStatus
_ZxAnInternalVlanRowStatus_Object = MibTableColumn
zxAnInternalVlanRowStatus = _ZxAnInternalVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 30, 1, 20),
    _ZxAnInternalVlanRowStatus_Type()
)
zxAnInternalVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnInternalVlanRowStatus.setStatus("current")
_ZxAnVlanExQinQOnuGroupTable_Object = MibTable
zxAnVlanExQinQOnuGroupTable = _ZxAnVlanExQinQOnuGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 31)
)
if mibBuilder.loadTexts:
    zxAnVlanExQinQOnuGroupTable.setStatus("current")
_ZxAnVlanExQinQOnuGroupEntry_Object = MibTableRow
zxAnVlanExQinQOnuGroupEntry = _ZxAnVlanExQinQOnuGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 31, 1)
)
zxAnVlanExQinQOnuGroupEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanExQinQPonPortIndex"),
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanExQinQOnuGroupId"),
)
if mibBuilder.loadTexts:
    zxAnVlanExQinQOnuGroupEntry.setStatus("current")
_ZxAnVlanExQinQPonPortIndex_Type = ZxAnIfindex
_ZxAnVlanExQinQPonPortIndex_Object = MibTableColumn
zxAnVlanExQinQPonPortIndex = _ZxAnVlanExQinQPonPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 31, 1, 1),
    _ZxAnVlanExQinQPonPortIndex_Type()
)
zxAnVlanExQinQPonPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVlanExQinQPonPortIndex.setStatus("current")


class _ZxAnVlanExQinQOnuGroupId_Type(Integer32):
    """Custom type zxAnVlanExQinQOnuGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ZxAnVlanExQinQOnuGroupId_Type.__name__ = "Integer32"
_ZxAnVlanExQinQOnuGroupId_Object = MibTableColumn
zxAnVlanExQinQOnuGroupId = _ZxAnVlanExQinQOnuGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 31, 1, 2),
    _ZxAnVlanExQinQOnuGroupId_Type()
)
zxAnVlanExQinQOnuGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVlanExQinQOnuGroupId.setStatus("current")


class _ZxAnVlanExQinQOnuGroupName_Type(DisplayString):
    """Custom type zxAnVlanExQinQOnuGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnVlanExQinQOnuGroupName_Type.__name__ = "DisplayString"
_ZxAnVlanExQinQOnuGroupName_Object = MibTableColumn
zxAnVlanExQinQOnuGroupName = _ZxAnVlanExQinQOnuGroupName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 31, 1, 3),
    _ZxAnVlanExQinQOnuGroupName_Type()
)
zxAnVlanExQinQOnuGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanExQinQOnuGroupName.setStatus("current")
_ZxAnVlanExQinQOnuGroupResVlan_Type = Integer32
_ZxAnVlanExQinQOnuGroupResVlan_Object = MibTableColumn
zxAnVlanExQinQOnuGroupResVlan = _ZxAnVlanExQinQOnuGroupResVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 31, 1, 4),
    _ZxAnVlanExQinQOnuGroupResVlan_Type()
)
zxAnVlanExQinQOnuGroupResVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanExQinQOnuGroupResVlan.setStatus("current")
_ZxAnVlanExQinQOnuGroupMembers_Type = DisplayString
_ZxAnVlanExQinQOnuGroupMembers_Object = MibTableColumn
zxAnVlanExQinQOnuGroupMembers = _ZxAnVlanExQinQOnuGroupMembers_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 31, 1, 5),
    _ZxAnVlanExQinQOnuGroupMembers_Type()
)
zxAnVlanExQinQOnuGroupMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanExQinQOnuGroupMembers.setStatus("current")
_ZxAnVlanTpidObjects_ObjectIdentity = ObjectIdentity
zxAnVlanTpidObjects = _ZxAnVlanTpidObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 32)
)
_ZxAnVlanTpidTable_Object = MibTable
zxAnVlanTpidTable = _ZxAnVlanTpidTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 32, 2)
)
if mibBuilder.loadTexts:
    zxAnVlanTpidTable.setStatus("deprecated")
_ZxAnVlanTpidEntry_Object = MibTableRow
zxAnVlanTpidEntry = _ZxAnVlanTpidEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 32, 2, 1)
)
zxAnVlanTpidEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanPortIndex"),
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanTpidSVlanId"),
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanTpidCVlanId"),
)
if mibBuilder.loadTexts:
    zxAnVlanTpidEntry.setStatus("current")


class _ZxAnVlanTpidSVlanId_Type(Integer32):
    """Custom type zxAnVlanTpidSVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnVlanTpidSVlanId_Type.__name__ = "Integer32"
_ZxAnVlanTpidSVlanId_Object = MibTableColumn
zxAnVlanTpidSVlanId = _ZxAnVlanTpidSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 32, 2, 1, 1),
    _ZxAnVlanTpidSVlanId_Type()
)
zxAnVlanTpidSVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVlanTpidSVlanId.setStatus("current")


class _ZxAnVlanTpidCVlanId_Type(Integer32):
    """Custom type zxAnVlanTpidCVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ZxAnVlanTpidCVlanId_Type.__name__ = "Integer32"
_ZxAnVlanTpidCVlanId_Object = MibTableColumn
zxAnVlanTpidCVlanId = _ZxAnVlanTpidCVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 32, 2, 1, 2),
    _ZxAnVlanTpidCVlanId_Type()
)
zxAnVlanTpidCVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVlanTpidCVlanId.setStatus("current")


class _ZxAnVlanTpid_Type(Integer32):
    """Custom type zxAnVlanTpid based on Integer32"""
    defaultValue = 33024


_ZxAnVlanTpid_Type.__name__ = "Integer32"
_ZxAnVlanTpid_Object = MibTableColumn
zxAnVlanTpid = _ZxAnVlanTpid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 32, 2, 1, 3),
    _ZxAnVlanTpid_Type()
)
zxAnVlanTpid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanTpid.setStatus("current")
_ZxAnVlanTpidRowStatus_Type = RowStatus
_ZxAnVlanTpidRowStatus_Object = MibTableColumn
zxAnVlanTpidRowStatus = _ZxAnVlanTpidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 32, 2, 1, 50),
    _ZxAnVlanTpidRowStatus_Type()
)
zxAnVlanTpidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanTpidRowStatus.setStatus("current")
_ZxAnIeee1588VlanTable_Object = MibTable
zxAnIeee1588VlanTable = _ZxAnIeee1588VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 33)
)
if mibBuilder.loadTexts:
    zxAnIeee1588VlanTable.setStatus("current")
_ZxAnIeee1588VlanEntry_Object = MibTableRow
zxAnIeee1588VlanEntry = _ZxAnIeee1588VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 33, 1)
)
zxAnIeee1588VlanEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnIeee1588Vlan"),
)
if mibBuilder.loadTexts:
    zxAnIeee1588VlanEntry.setStatus("current")
_ZxAnIeee1588Vlan_Type = VlanId
_ZxAnIeee1588Vlan_Object = MibTableColumn
zxAnIeee1588Vlan = _ZxAnIeee1588Vlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 33, 1, 1),
    _ZxAnIeee1588Vlan_Type()
)
zxAnIeee1588Vlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIeee1588Vlan.setStatus("current")
_ZxAnIeee1588VlanRowStatus_Type = RowStatus
_ZxAnIeee1588VlanRowStatus_Object = MibTableColumn
zxAnIeee1588VlanRowStatus = _ZxAnIeee1588VlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 33, 1, 50),
    _ZxAnIeee1588VlanRowStatus_Type()
)
zxAnIeee1588VlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIeee1588VlanRowStatus.setStatus("current")
_ZxAnMVlanGlobalTransTable_Object = MibTable
zxAnMVlanGlobalTransTable = _ZxAnMVlanGlobalTransTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 34)
)
if mibBuilder.loadTexts:
    zxAnMVlanGlobalTransTable.setStatus("current")
_ZxAnMVlanGlobalTransEntry_Object = MibTableRow
zxAnMVlanGlobalTransEntry = _ZxAnMVlanGlobalTransEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 34, 1)
)
zxAnMVlanGlobalTransEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnMVlanGlobalTransMVid"),
)
if mibBuilder.loadTexts:
    zxAnMVlanGlobalTransEntry.setStatus("current")
_ZxAnMVlanGlobalTransMVid_Type = VlanId
_ZxAnMVlanGlobalTransMVid_Object = MibTableColumn
zxAnMVlanGlobalTransMVid = _ZxAnMVlanGlobalTransMVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 34, 1, 1),
    _ZxAnMVlanGlobalTransMVid_Type()
)
zxAnMVlanGlobalTransMVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMVlanGlobalTransMVid.setStatus("current")


class _ZxAnMVlanGlobalTransCVid_Type(Integer32):
    """Custom type zxAnMVlanGlobalTransCVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ZxAnMVlanGlobalTransCVid_Type.__name__ = "Integer32"
_ZxAnMVlanGlobalTransCVid_Object = MibTableColumn
zxAnMVlanGlobalTransCVid = _ZxAnMVlanGlobalTransCVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 34, 1, 2),
    _ZxAnMVlanGlobalTransCVid_Type()
)
zxAnMVlanGlobalTransCVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMVlanGlobalTransCVid.setStatus("current")
_ZxAnMVlanGlobalTransRowStatus_Type = RowStatus
_ZxAnMVlanGlobalTransRowStatus_Object = MibTableColumn
zxAnMVlanGlobalTransRowStatus = _ZxAnMVlanGlobalTransRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 34, 1, 20),
    _ZxAnMVlanGlobalTransRowStatus_Type()
)
zxAnMVlanGlobalTransRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMVlanGlobalTransRowStatus.setStatus("current")
_ZxAnVlanStormCtrlTable_Object = MibTable
zxAnVlanStormCtrlTable = _ZxAnVlanStormCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 35)
)
if mibBuilder.loadTexts:
    zxAnVlanStormCtrlTable.setStatus("current")
_ZxAnVlanStormCtrlEntry_Object = MibTableRow
zxAnVlanStormCtrlEntry = _ZxAnVlanStormCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 35, 1)
)
zxAnVlanStormCtrlEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanId"),
)
if mibBuilder.loadTexts:
    zxAnVlanStormCtrlEntry.setStatus("current")


class _ZxAnVlanMulticastFloodCtrl_Type(Integer32):
    """Custom type zxAnVlanMulticastFloodCtrl based on Integer32"""
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
        *(("floodUnknown", 1),
          ("dropUnknown", 2),
          ("floodAll", 3))
    )


_ZxAnVlanMulticastFloodCtrl_Type.__name__ = "Integer32"
_ZxAnVlanMulticastFloodCtrl_Object = MibTableColumn
zxAnVlanMulticastFloodCtrl = _ZxAnVlanMulticastFloodCtrl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 35, 1, 1),
    _ZxAnVlanMulticastFloodCtrl_Type()
)
zxAnVlanMulticastFloodCtrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanMulticastFloodCtrl.setStatus("current")
_ZxAnVlanTagPortListTable_Object = MibTable
zxAnVlanTagPortListTable = _ZxAnVlanTagPortListTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 36)
)
if mibBuilder.loadTexts:
    zxAnVlanTagPortListTable.setStatus("current")
_ZxAnVlanTagPortListEntry_Object = MibTableRow
zxAnVlanTagPortListEntry = _ZxAnVlanTagPortListEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 36, 1)
)
zxAnVlanTagPortListEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanStag"),
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanCtag"),
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanTagShelf"),
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanTagSlot"),
)
if mibBuilder.loadTexts:
    zxAnVlanTagPortListEntry.setStatus("current")


class _ZxAnVlanStag_Type(Integer32):
    """Custom type zxAnVlanStag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ZxAnVlanStag_Type.__name__ = "Integer32"
_ZxAnVlanStag_Object = MibTableColumn
zxAnVlanStag = _ZxAnVlanStag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 36, 1, 1),
    _ZxAnVlanStag_Type()
)
zxAnVlanStag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVlanStag.setStatus("current")


class _ZxAnVlanCtag_Type(Integer32):
    """Custom type zxAnVlanCtag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ZxAnVlanCtag_Type.__name__ = "Integer32"
_ZxAnVlanCtag_Object = MibTableColumn
zxAnVlanCtag = _ZxAnVlanCtag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 36, 1, 2),
    _ZxAnVlanCtag_Type()
)
zxAnVlanCtag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVlanCtag.setStatus("current")
_ZxAnVlanTagShelf_Type = Integer32
_ZxAnVlanTagShelf_Object = MibTableColumn
zxAnVlanTagShelf = _ZxAnVlanTagShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 36, 1, 3),
    _ZxAnVlanTagShelf_Type()
)
zxAnVlanTagShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVlanTagShelf.setStatus("current")
_ZxAnVlanTagSlot_Type = Integer32
_ZxAnVlanTagSlot_Object = MibTableColumn
zxAnVlanTagSlot = _ZxAnVlanTagSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 36, 1, 4),
    _ZxAnVlanTagSlot_Type()
)
zxAnVlanTagSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVlanTagSlot.setStatus("current")
_ZxAnVlanTagPortList_Type = ZxAnPortList
_ZxAnVlanTagPortList_Object = MibTableColumn
zxAnVlanTagPortList = _ZxAnVlanTagPortList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 36, 1, 5),
    _ZxAnVlanTagPortList_Type()
)
zxAnVlanTagPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanTagPortList.setStatus("current")
_ZxAnVlanConfTpidTable_Object = MibTable
zxAnVlanConfTpidTable = _ZxAnVlanConfTpidTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 37)
)
if mibBuilder.loadTexts:
    zxAnVlanConfTpidTable.setStatus("current")
_ZxAnVlanConfTpidEntry_Object = MibTableRow
zxAnVlanConfTpidEntry = _ZxAnVlanConfTpidEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 37, 1)
)
zxAnVlanConfTpidEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanId"),
)
if mibBuilder.loadTexts:
    zxAnVlanConfTpidEntry.setStatus("current")
_ZxAnVlanTpidConfTpid_Type = Integer32
_ZxAnVlanTpidConfTpid_Object = MibTableColumn
zxAnVlanTpidConfTpid = _ZxAnVlanTpidConfTpid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 37, 1, 1),
    _ZxAnVlanTpidConfTpid_Type()
)
zxAnVlanTpidConfTpid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanTpidConfTpid.setStatus("current")
_ZxAnVlanTpidConfRowStatus_Type = RowStatus
_ZxAnVlanTpidConfRowStatus_Object = MibTableColumn
zxAnVlanTpidConfRowStatus = _ZxAnVlanTpidConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 37, 1, 50),
    _ZxAnVlanTpidConfRowStatus_Type()
)
zxAnVlanTpidConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanTpidConfRowStatus.setStatus("current")
_ZxAnVlanRuledTransGroup_ObjectIdentity = ObjectIdentity
zxAnVlanRuledTransGroup = _ZxAnVlanRuledTransGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 38)
)
_ZxAnVlanRuledTransTable_Object = MibTable
zxAnVlanRuledTransTable = _ZxAnVlanRuledTransTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 38, 2)
)
if mibBuilder.loadTexts:
    zxAnVlanRuledTransTable.setStatus("current")
_ZxAnVlanRuledTransEntry_Object = MibTableRow
zxAnVlanRuledTransEntry = _ZxAnVlanRuledTransEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 38, 2, 1)
)
zxAnVlanRuledTransEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanPortIndex"),
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanRuledTransSVid"),
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanRuledTransCVid"),
)
if mibBuilder.loadTexts:
    zxAnVlanRuledTransEntry.setStatus("current")


class _ZxAnVlanRuledTransSVid_Type(Integer32):
    """Custom type zxAnVlanRuledTransSVid based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ZxAnVlanRuledTransSVid_Type.__name__ = "Integer32"
_ZxAnVlanRuledTransSVid_Object = MibTableColumn
zxAnVlanRuledTransSVid = _ZxAnVlanRuledTransSVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 38, 2, 1, 1),
    _ZxAnVlanRuledTransSVid_Type()
)
zxAnVlanRuledTransSVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVlanRuledTransSVid.setStatus("current")


class _ZxAnVlanRuledTransCVid_Type(Integer32):
    """Custom type zxAnVlanRuledTransCVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ZxAnVlanRuledTransCVid_Type.__name__ = "Integer32"
_ZxAnVlanRuledTransCVid_Object = MibTableColumn
zxAnVlanRuledTransCVid = _ZxAnVlanRuledTransCVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 38, 2, 1, 2),
    _ZxAnVlanRuledTransCVid_Type()
)
zxAnVlanRuledTransCVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVlanRuledTransCVid.setStatus("current")


class _ZxAnVlanRuledTransUserVid_Type(Integer32):
    """Custom type zxAnVlanRuledTransUserVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ZxAnVlanRuledTransUserVid_Type.__name__ = "Integer32"
_ZxAnVlanRuledTransUserVid_Object = MibTableColumn
zxAnVlanRuledTransUserVid = _ZxAnVlanRuledTransUserVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 38, 2, 1, 3),
    _ZxAnVlanRuledTransUserVid_Type()
)
zxAnVlanRuledTransUserVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanRuledTransUserVid.setStatus("current")
_ZxAnVlanRuledTransRowStatus_Type = RowStatus
_ZxAnVlanRuledTransRowStatus_Object = MibTableColumn
zxAnVlanRuledTransRowStatus = _ZxAnVlanRuledTransRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 38, 2, 1, 50),
    _ZxAnVlanRuledTransRowStatus_Type()
)
zxAnVlanRuledTransRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanRuledTransRowStatus.setStatus("current")
_ZxAnVlanIfCosMapObjects_ObjectIdentity = ObjectIdentity
zxAnVlanIfCosMapObjects = _ZxAnVlanIfCosMapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 39)
)
_ZxAnVlanIfCosMapEnableTable_Object = MibTable
zxAnVlanIfCosMapEnableTable = _ZxAnVlanIfCosMapEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 39, 2)
)
if mibBuilder.loadTexts:
    zxAnVlanIfCosMapEnableTable.setStatus("current")
_ZxAnVlanIfCosMapEnableEntry_Object = MibTableRow
zxAnVlanIfCosMapEnableEntry = _ZxAnVlanIfCosMapEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 39, 2, 1)
)
zxAnVlanIfCosMapEnableEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanPortIndex"),
)
if mibBuilder.loadTexts:
    zxAnVlanIfCosMapEnableEntry.setStatus("current")


class _ZxAnVlanIfCosMapEnable_Type(Integer32):
    """Custom type zxAnVlanIfCosMapEnable based on Integer32"""
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


_ZxAnVlanIfCosMapEnable_Type.__name__ = "Integer32"
_ZxAnVlanIfCosMapEnable_Object = MibTableColumn
zxAnVlanIfCosMapEnable = _ZxAnVlanIfCosMapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 39, 2, 1, 1),
    _ZxAnVlanIfCosMapEnable_Type()
)
zxAnVlanIfCosMapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanIfCosMapEnable.setStatus("current")
_ZxAnVlanIfCosMapTable_Object = MibTable
zxAnVlanIfCosMapTable = _ZxAnVlanIfCosMapTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 39, 3)
)
if mibBuilder.loadTexts:
    zxAnVlanIfCosMapTable.setStatus("current")
_ZxAnVlanIfCosMapEntry_Object = MibTableRow
zxAnVlanIfCosMapEntry = _ZxAnVlanIfCosMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 39, 3, 1)
)
zxAnVlanIfCosMapEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanPortIndex"),
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanIfCosMapCos"),
)
if mibBuilder.loadTexts:
    zxAnVlanIfCosMapEntry.setStatus("current")


class _ZxAnVlanIfCosMapCos_Type(Integer32):
    """Custom type zxAnVlanIfCosMapCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnVlanIfCosMapCos_Type.__name__ = "Integer32"
_ZxAnVlanIfCosMapCos_Object = MibTableColumn
zxAnVlanIfCosMapCos = _ZxAnVlanIfCosMapCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 39, 3, 1, 1),
    _ZxAnVlanIfCosMapCos_Type()
)
zxAnVlanIfCosMapCos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVlanIfCosMapCos.setStatus("current")


class _ZxAnVlanIfCosMapSVid_Type(Integer32):
    """Custom type zxAnVlanIfCosMapSVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnVlanIfCosMapSVid_Type.__name__ = "Integer32"
_ZxAnVlanIfCosMapSVid_Object = MibTableColumn
zxAnVlanIfCosMapSVid = _ZxAnVlanIfCosMapSVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 39, 3, 1, 2),
    _ZxAnVlanIfCosMapSVid_Type()
)
zxAnVlanIfCosMapSVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanIfCosMapSVid.setStatus("current")


class _ZxAnVlanIfCosMapCVid_Type(Integer32):
    """Custom type zxAnVlanIfCosMapCVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ZxAnVlanIfCosMapCVid_Type.__name__ = "Integer32"
_ZxAnVlanIfCosMapCVid_Object = MibTableColumn
zxAnVlanIfCosMapCVid = _ZxAnVlanIfCosMapCVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 39, 3, 1, 3),
    _ZxAnVlanIfCosMapCVid_Type()
)
zxAnVlanIfCosMapCVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanIfCosMapCVid.setStatus("current")
_ZxAnVlanIfCosMapRowStatus_Type = RowStatus
_ZxAnVlanIfCosMapRowStatus_Object = MibTableColumn
zxAnVlanIfCosMapRowStatus = _ZxAnVlanIfCosMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 39, 3, 1, 50),
    _ZxAnVlanIfCosMapRowStatus_Type()
)
zxAnVlanIfCosMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanIfCosMapRowStatus.setStatus("current")
_ZxAnVlanBasedForwardObjects_ObjectIdentity = ObjectIdentity
zxAnVlanBasedForwardObjects = _ZxAnVlanBasedForwardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 40)
)
_ZxAnVlanBasedForwardTable_Object = MibTable
zxAnVlanBasedForwardTable = _ZxAnVlanBasedForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 40, 2)
)
if mibBuilder.loadTexts:
    zxAnVlanBasedForwardTable.setStatus("current")
_ZxAnVlanBasedForwardEntry_Object = MibTableRow
zxAnVlanBasedForwardEntry = _ZxAnVlanBasedForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 40, 2, 1)
)
zxAnVlanBasedForwardEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanBasedForwardSVid"),
    (0, "ZTE-AN-VLAN-MIB", "zxAnVlanBasedForwardCVid"),
)
if mibBuilder.loadTexts:
    zxAnVlanBasedForwardEntry.setStatus("current")
_ZxAnVlanBasedForwardSVid_Type = VlanId
_ZxAnVlanBasedForwardSVid_Object = MibTableColumn
zxAnVlanBasedForwardSVid = _ZxAnVlanBasedForwardSVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 40, 2, 1, 1),
    _ZxAnVlanBasedForwardSVid_Type()
)
zxAnVlanBasedForwardSVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVlanBasedForwardSVid.setStatus("current")


class _ZxAnVlanBasedForwardCVid_Type(Integer32):
    """Custom type zxAnVlanBasedForwardCVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ZxAnVlanBasedForwardCVid_Type.__name__ = "Integer32"
_ZxAnVlanBasedForwardCVid_Object = MibTableColumn
zxAnVlanBasedForwardCVid = _ZxAnVlanBasedForwardCVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 40, 2, 1, 2),
    _ZxAnVlanBasedForwardCVid_Type()
)
zxAnVlanBasedForwardCVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVlanBasedForwardCVid.setStatus("current")
_ZxAnVlanBasedForwardIfIndex_Type = ZxAnIfindex
_ZxAnVlanBasedForwardIfIndex_Object = MibTableColumn
zxAnVlanBasedForwardIfIndex = _ZxAnVlanBasedForwardIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 40, 2, 1, 3),
    _ZxAnVlanBasedForwardIfIndex_Type()
)
zxAnVlanBasedForwardIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanBasedForwardIfIndex.setStatus("current")
_ZxAnVlanBasedForwardUplinkPort_Type = ZxAnIfindex
_ZxAnVlanBasedForwardUplinkPort_Object = MibTableColumn
zxAnVlanBasedForwardUplinkPort = _ZxAnVlanBasedForwardUplinkPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 40, 2, 1, 4),
    _ZxAnVlanBasedForwardUplinkPort_Type()
)
zxAnVlanBasedForwardUplinkPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanBasedForwardUplinkPort.setStatus("current")
_ZxAnVlanBasedForwardRowStatus_Type = RowStatus
_ZxAnVlanBasedForwardRowStatus_Object = MibTableColumn
zxAnVlanBasedForwardRowStatus = _ZxAnVlanBasedForwardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 40, 2, 1, 50),
    _ZxAnVlanBasedForwardRowStatus_Type()
)
zxAnVlanBasedForwardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanBasedForwardRowStatus.setStatus("current")
_ZxAnVlanGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnVlanGlobalObjects = _ZxAnVlanGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 99)
)


class _ZxAnVlanCapabilities_Type(Bits):
    """Custom type zxAnVlanCapabilities based on Bits"""
    namedValues = NamedValues(
        ("supportBasedForwardObjects", 0)
    )

_ZxAnVlanCapabilities_Type.__name__ = "Bits"
_ZxAnVlanCapabilities_Object = MibScalar
zxAnVlanCapabilities = _ZxAnVlanCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 99, 1),
    _ZxAnVlanCapabilities_Type()
)
zxAnVlanCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanCapabilities.setStatus("current")
_ZxAnVlanMibEnd_Type = Integer32
_ZxAnVlanMibEnd_Object = MibScalar
zxAnVlanMibEnd = _ZxAnVlanMibEnd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 20, 100),
    _ZxAnVlanMibEnd_Type()
)
zxAnVlanMibEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanMibEnd.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-VLAN-MIB",
    **{"zxAnVlanMib": zxAnVlanMib,
       "zxAnVlanNum": zxAnVlanNum,
       "zxAnVlanTable": zxAnVlanTable,
       "zxAnVlanEntry": zxAnVlanEntry,
       "zxAnVlanId": zxAnVlanId,
       "zxAnVlanName": zxAnVlanName,
       "zxAnVlanTransparent": zxAnVlanTransparent,
       "zxAnVlanRowStatus": zxAnVlanRowStatus,
       "zxAnVlanXconnect": zxAnVlanXconnect,
       "zxAnVlanDesc": zxAnVlanDesc,
       "zxAnVlanPortTable": zxAnVlanPortTable,
       "zxAnVlanPortEntry": zxAnVlanPortEntry,
       "zxAnVlanPortIndex": zxAnVlanPortIndex,
       "zxAnVlanIfConfMode": zxAnVlanIfConfMode,
       "zxAnVlanIfConfTlsEnable": zxAnVlanIfConfTlsEnable,
       "zxAnVlanIfConfTlsSVid": zxAnVlanIfConfTlsSVid,
       "zxAnVlanIfConfDefaultVid": zxAnVlanIfConfDefaultVid,
       "zxAnVlanIfConfDefaultCVid": zxAnVlanIfConfDefaultCVid,
       "zxAnVlanIfConfUntaggedVlanList": zxAnVlanIfConfUntaggedVlanList,
       "zxAnVlanIfConfTaggedVlanList": zxAnVlanIfConfTaggedVlanList,
       "zxAnVlanIfConfTpid": zxAnVlanIfConfTpid,
       "zxAnVlanIfIngressFilterEnable": zxAnVlanIfIngressFilterEnable,
       "zxAnVlanIfAcceptableFrameTypes": zxAnVlanIfAcceptableFrameTypes,
       "zxAnVlanIfConfTpidEnable": zxAnVlanIfConfTpidEnable,
       "zxAnVlanIfConfVlanCmdTable": zxAnVlanIfConfVlanCmdTable,
       "zxAnVlanIfConfVlanCmdEntry": zxAnVlanIfConfVlanCmdEntry,
       "zxAnVlanIfConfVlanCmd": zxAnVlanIfConfVlanCmd,
       "zxAnVlanIfConfVlanList": zxAnVlanIfConfVlanList,
       "zxAnVlanIfTransTable": zxAnVlanIfTransTable,
       "zxAnVlanIfTransEntry": zxAnVlanIfTransEntry,
       "zxAnVlanTranslatePortId": zxAnVlanTranslatePortId,
       "zxAnVlanIfTransUserVid": zxAnVlanIfTransUserVid,
       "zxAnVlanIfTransCVid": zxAnVlanIfTransCVid,
       "zxAnVlanIfTransSVid": zxAnVlanIfTransSVid,
       "zxAnVlanIfTransRowStatus": zxAnVlanIfTransRowStatus,
       "zxAnVlanIfTransVlanMerge": zxAnVlanIfTransVlanMerge,
       "zxAnVlanPortListTable": zxAnVlanPortListTable,
       "zxAnVlanPortListEntry": zxAnVlanPortListEntry,
       "zxAnVlanIndex": zxAnVlanIndex,
       "zxAnShelfIndex": zxAnShelfIndex,
       "zxAnSlotIndex": zxAnSlotIndex,
       "zxAnVlanPortListSlotIfType": zxAnVlanPortListSlotIfType,
       "zxAnVlanPortUntaggedPortList": zxAnVlanPortUntaggedPortList,
       "zxAnVlanPortTaggedPortList": zxAnVlanPortTaggedPortList,
       "zxAnVlanGlobalTransTable": zxAnVlanGlobalTransTable,
       "zxAnVlanGlobalTransEntry": zxAnVlanGlobalTransEntry,
       "zxAnVlanGlobalTransSessionNo": zxAnVlanGlobalTransSessionNo,
       "zxAnVlanMpTranslatePortId": zxAnVlanMpTranslatePortId,
       "zxAnVlanGlobalTransVid": zxAnVlanGlobalTransVid,
       "zxAnVlanGlobalTransCVid": zxAnVlanGlobalTransCVid,
       "zxAnVlanGlobalTransSVid": zxAnVlanGlobalTransSVid,
       "zxAnVlanMpTranslateDirection": zxAnVlanMpTranslateDirection,
       "zxAnVlanGlobalTransRowStatus": zxAnVlanGlobalTransRowStatus,
       "zxAnVlanGlobalTransVlanMerge": zxAnVlanGlobalTransVlanMerge,
       "zxAnVlanMpExQinQTable": zxAnVlanMpExQinQTable,
       "zxAnVlanMpExQinQEntry": zxAnVlanMpExQinQEntry,
       "zxAnVlanExQinQSessionNo": zxAnVlanExQinQSessionNo,
       "zxAnVlanSmartQinQIfIndex": zxAnVlanSmartQinQIfIndex,
       "zxAnVlanSmartQinQUserVid": zxAnVlanSmartQinQUserVid,
       "zxAnVlanSmartQinQSelectiveType": zxAnVlanSmartQinQSelectiveType,
       "zxAnVlanSmartQinQStartUserVid": zxAnVlanSmartQinQStartUserVid,
       "zxAnVlanSmartQinQEndUserVid": zxAnVlanSmartQinQEndUserVid,
       "zxAnVlanExQinQInCVlanMask": zxAnVlanExQinQInCVlanMask,
       "zxAnVlanSmartQinQEtherType": zxAnVlanSmartQinQEtherType,
       "zxAnVlanSmartQinQUserCos": zxAnVlanSmartQinQUserCos,
       "zxAnVlanSmartQinQSVid": zxAnVlanSmartQinQSVid,
       "zxAnVlanSmartQinQStagCos": zxAnVlanSmartQinQStagCos,
       "zxAnVlanExQinQRefOnuGroupId": zxAnVlanExQinQRefOnuGroupId,
       "zxAnVlanSmartQinQRowStatus": zxAnVlanSmartQinQRowStatus,
       "zxAnVlanVoipConfTable": zxAnVlanVoipConfTable,
       "zxAnVlanVoipConfEntry": zxAnVlanVoipConfEntry,
       "zxAnVlanVoipVlanId": zxAnVlanVoipVlanId,
       "zxAnVoipVlanUsages": zxAnVoipVlanUsages,
       "zxAnVlanVoipRowStatus": zxAnVlanVoipRowStatus,
       "zxAnVlanSmartQinQEnable": zxAnVlanSmartQinQEnable,
       "zxAnReservedVlan": zxAnReservedVlan,
       "zxAnVlanMpExQinQPortTable": zxAnVlanMpExQinQPortTable,
       "zxAnVlanMpExQinQPortEntry": zxAnVlanMpExQinQPortEntry,
       "zxAnVlanExQinQPortIndex": zxAnVlanExQinQPortIndex,
       "zxAnVlanSmartQinQIfEnable": zxAnVlanSmartQinQIfEnable,
       "zxAnVlanExQinQOnuMapGroupId": zxAnVlanExQinQOnuMapGroupId,
       "zxAnVlanExQinQPortResVlan": zxAnVlanExQinQPortResVlan,
       "zxAnVlanMpExTranslatePortTable": zxAnVlanMpExTranslatePortTable,
       "zxAnVlanMpExTranslatePortEntry": zxAnVlanMpExTranslatePortEntry,
       "zxAnVlanExTranslatePortIndex": zxAnVlanExTranslatePortIndex,
       "zxAnVlanExTranslatePortEnabled": zxAnVlanExTranslatePortEnabled,
       "zxAnVlanTranslateMode": zxAnVlanTranslateMode,
       "zxAnProtocolVlanMapTable": zxAnProtocolVlanMapTable,
       "zxAnProtocolVlanMapEntry": zxAnProtocolVlanMapEntry,
       "zxAnProtocolVlanPortIndex": zxAnProtocolVlanPortIndex,
       "zxAnEtherProtocolType": zxAnEtherProtocolType,
       "zxAnVlanIfProtoMapVid": zxAnVlanIfProtoMapVid,
       "zxAnVlanIfProtoMapCos": zxAnVlanIfProtoMapCos,
       "zxAnVlanIfProtoMapCVid": zxAnVlanIfProtoMapCVid,
       "zxAnVlanIfProtoMapCtagCos": zxAnVlanIfProtoMapCtagCos,
       "zxAnVlanIfProtoMapRowStatus": zxAnVlanIfProtoMapRowStatus,
       "zxAnBatchVLANObjects": zxAnBatchVLANObjects,
       "zxAnVlanBatchConfVlanList": zxAnVlanBatchConfVlanList,
       "zxAnVlanBatchConfPrefixName": zxAnVlanBatchConfPrefixName,
       "zxAnBatchVlanTransparent": zxAnBatchVlanTransparent,
       "zxAnVlanBatchConfType": zxAnVlanBatchConfType,
       "zxAnVlanBatchConfStatus": zxAnVlanBatchConfStatus,
       "zxAnVlanBatchConfFailedVlanList": zxAnVlanBatchConfFailedVlanList,
       "zxAnVlanBatchConfCurrVlanList": zxAnVlanBatchConfCurrVlanList,
       "zxAnXconnectTable": zxAnXconnectTable,
       "zxAnXconnectEntry": zxAnXconnectEntry,
       "zxAnXconnectPortIndex": zxAnXconnectPortIndex,
       "zxAnXconnectLocationIndex": zxAnXconnectLocationIndex,
       "zxAnXconnectMode": zxAnXconnectMode,
       "zxAnVlanBasedFwdSVid": zxAnVlanBasedFwdSVid,
       "zxAnVlanBasedFwdCVid": zxAnVlanBasedFwdCVid,
       "zxAnXconnectNewCvlanId": zxAnXconnectNewCvlanId,
       "zxAnXconnectNewSvlanId": zxAnXconnectNewSvlanId,
       "zxAnVlanBasedFwdUplinkPort": zxAnVlanBasedFwdUplinkPort,
       "zxAnVlanBasedFwdRowStatus": zxAnVlanBasedFwdRowStatus,
       "zxAnVlanExQinQSupportEIGMP": zxAnVlanExQinQSupportEIGMP,
       "zxAnVlanGlobalCtagTpid": zxAnVlanGlobalCtagTpid,
       "zxAnVlanGlobalTpid": zxAnVlanGlobalTpid,
       "zxAnOnuMngVlanTable": zxAnOnuMngVlanTable,
       "zxAnOnuMngVlanEntry": zxAnOnuMngVlanEntry,
       "zxAnOnuMngVlan": zxAnOnuMngVlan,
       "zxAnOnuMngVlanRowStatus": zxAnOnuMngVlanRowStatus,
       "zxAnIpRouteVlanTable": zxAnIpRouteVlanTable,
       "zxAnIpRouteVlanEntry": zxAnIpRouteVlanEntry,
       "zxAnIpRouteVlan": zxAnIpRouteVlan,
       "zxAnIpRouteVlanRowStatus": zxAnIpRouteVlanRowStatus,
       "zxAnVlanInterfaceTable": zxAnVlanInterfaceTable,
       "zxAnVlanInterfaceEntry": zxAnVlanInterfaceEntry,
       "zxAnVlanInterfaceVlanId": zxAnVlanInterfaceVlanId,
       "zxAnVlanBroadcastRateLimit": zxAnVlanBroadcastRateLimit,
       "zxAnPortMvlanTranslateTable": zxAnPortMvlanTranslateTable,
       "zxAnPortMvlanTranslateEntry": zxAnPortMvlanTranslateEntry,
       "zxAnPortMvlanTranslateIfIndex": zxAnPortMvlanTranslateIfIndex,
       "zxAnPortMvlanTranslateMvlan": zxAnPortMvlanTranslateMvlan,
       "zxAnPortMvlanTranslateCvlan": zxAnPortMvlanTranslateCvlan,
       "zxAnMVlanIfTransRowStatus": zxAnMVlanIfTransRowStatus,
       "zxAnVlanIfProtoMapEnableTable": zxAnVlanIfProtoMapEnableTable,
       "zxAnVlanIfProtoMapEnableEntry": zxAnVlanIfProtoMapEnableEntry,
       "zxAnProtocolVlanPortIfIndex": zxAnProtocolVlanPortIfIndex,
       "zxAnVlanIfProtoMapEnable": zxAnVlanIfProtoMapEnable,
       "zxAnInternalVlanTable": zxAnInternalVlanTable,
       "zxAnInternalVlanEntry": zxAnInternalVlanEntry,
       "zxAnInternalVlanServiceType": zxAnInternalVlanServiceType,
       "zxAnInternalVlanList": zxAnInternalVlanList,
       "zxAnInternalVlanRowStatus": zxAnInternalVlanRowStatus,
       "zxAnVlanExQinQOnuGroupTable": zxAnVlanExQinQOnuGroupTable,
       "zxAnVlanExQinQOnuGroupEntry": zxAnVlanExQinQOnuGroupEntry,
       "zxAnVlanExQinQPonPortIndex": zxAnVlanExQinQPonPortIndex,
       "zxAnVlanExQinQOnuGroupId": zxAnVlanExQinQOnuGroupId,
       "zxAnVlanExQinQOnuGroupName": zxAnVlanExQinQOnuGroupName,
       "zxAnVlanExQinQOnuGroupResVlan": zxAnVlanExQinQOnuGroupResVlan,
       "zxAnVlanExQinQOnuGroupMembers": zxAnVlanExQinQOnuGroupMembers,
       "zxAnVlanTpidObjects": zxAnVlanTpidObjects,
       "zxAnVlanTpidTable": zxAnVlanTpidTable,
       "zxAnVlanTpidEntry": zxAnVlanTpidEntry,
       "zxAnVlanTpidSVlanId": zxAnVlanTpidSVlanId,
       "zxAnVlanTpidCVlanId": zxAnVlanTpidCVlanId,
       "zxAnVlanTpid": zxAnVlanTpid,
       "zxAnVlanTpidRowStatus": zxAnVlanTpidRowStatus,
       "zxAnIeee1588VlanTable": zxAnIeee1588VlanTable,
       "zxAnIeee1588VlanEntry": zxAnIeee1588VlanEntry,
       "zxAnIeee1588Vlan": zxAnIeee1588Vlan,
       "zxAnIeee1588VlanRowStatus": zxAnIeee1588VlanRowStatus,
       "zxAnMVlanGlobalTransTable": zxAnMVlanGlobalTransTable,
       "zxAnMVlanGlobalTransEntry": zxAnMVlanGlobalTransEntry,
       "zxAnMVlanGlobalTransMVid": zxAnMVlanGlobalTransMVid,
       "zxAnMVlanGlobalTransCVid": zxAnMVlanGlobalTransCVid,
       "zxAnMVlanGlobalTransRowStatus": zxAnMVlanGlobalTransRowStatus,
       "zxAnVlanStormCtrlTable": zxAnVlanStormCtrlTable,
       "zxAnVlanStormCtrlEntry": zxAnVlanStormCtrlEntry,
       "zxAnVlanMulticastFloodCtrl": zxAnVlanMulticastFloodCtrl,
       "zxAnVlanTagPortListTable": zxAnVlanTagPortListTable,
       "zxAnVlanTagPortListEntry": zxAnVlanTagPortListEntry,
       "zxAnVlanStag": zxAnVlanStag,
       "zxAnVlanCtag": zxAnVlanCtag,
       "zxAnVlanTagShelf": zxAnVlanTagShelf,
       "zxAnVlanTagSlot": zxAnVlanTagSlot,
       "zxAnVlanTagPortList": zxAnVlanTagPortList,
       "zxAnVlanConfTpidTable": zxAnVlanConfTpidTable,
       "zxAnVlanConfTpidEntry": zxAnVlanConfTpidEntry,
       "zxAnVlanTpidConfTpid": zxAnVlanTpidConfTpid,
       "zxAnVlanTpidConfRowStatus": zxAnVlanTpidConfRowStatus,
       "zxAnVlanRuledTransGroup": zxAnVlanRuledTransGroup,
       "zxAnVlanRuledTransTable": zxAnVlanRuledTransTable,
       "zxAnVlanRuledTransEntry": zxAnVlanRuledTransEntry,
       "zxAnVlanRuledTransSVid": zxAnVlanRuledTransSVid,
       "zxAnVlanRuledTransCVid": zxAnVlanRuledTransCVid,
       "zxAnVlanRuledTransUserVid": zxAnVlanRuledTransUserVid,
       "zxAnVlanRuledTransRowStatus": zxAnVlanRuledTransRowStatus,
       "zxAnVlanIfCosMapObjects": zxAnVlanIfCosMapObjects,
       "zxAnVlanIfCosMapEnableTable": zxAnVlanIfCosMapEnableTable,
       "zxAnVlanIfCosMapEnableEntry": zxAnVlanIfCosMapEnableEntry,
       "zxAnVlanIfCosMapEnable": zxAnVlanIfCosMapEnable,
       "zxAnVlanIfCosMapTable": zxAnVlanIfCosMapTable,
       "zxAnVlanIfCosMapEntry": zxAnVlanIfCosMapEntry,
       "zxAnVlanIfCosMapCos": zxAnVlanIfCosMapCos,
       "zxAnVlanIfCosMapSVid": zxAnVlanIfCosMapSVid,
       "zxAnVlanIfCosMapCVid": zxAnVlanIfCosMapCVid,
       "zxAnVlanIfCosMapRowStatus": zxAnVlanIfCosMapRowStatus,
       "zxAnVlanBasedForwardObjects": zxAnVlanBasedForwardObjects,
       "zxAnVlanBasedForwardTable": zxAnVlanBasedForwardTable,
       "zxAnVlanBasedForwardEntry": zxAnVlanBasedForwardEntry,
       "zxAnVlanBasedForwardSVid": zxAnVlanBasedForwardSVid,
       "zxAnVlanBasedForwardCVid": zxAnVlanBasedForwardCVid,
       "zxAnVlanBasedForwardIfIndex": zxAnVlanBasedForwardIfIndex,
       "zxAnVlanBasedForwardUplinkPort": zxAnVlanBasedForwardUplinkPort,
       "zxAnVlanBasedForwardRowStatus": zxAnVlanBasedForwardRowStatus,
       "zxAnVlanGlobalObjects": zxAnVlanGlobalObjects,
       "zxAnVlanCapabilities": zxAnVlanCapabilities,
       "zxAnVlanMibEnd": zxAnVlanMibEnd}
)
