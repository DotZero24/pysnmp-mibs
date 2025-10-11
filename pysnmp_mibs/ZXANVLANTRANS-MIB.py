# SNMP MIB module (ZXANVLANTRANS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZXANVLANTRANS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:43 2025
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(VlanId,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "VlanId")

(zxAnPonMib,) = mibBuilder.importSymbols(
    "ZTE-MASTER-MIB",
    "zxAnPonMib")


# MODULE-IDENTITY

zxAnVlanTrans = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnVlanTransRuleTable_Object = MibTable
zxAnVlanTransRuleTable = _ZxAnVlanTransRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 10, 1)
)
if mibBuilder.loadTexts:
    zxAnVlanTransRuleTable.setStatus("current")
_ZxAnVlanTransRuleEntry_Object = MibTableRow
zxAnVlanTransRuleEntry = _ZxAnVlanTransRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 10, 1, 1)
)
zxAnVlanTransRuleEntry.setIndexNames(
    (0, "ZXANVLANTRANS-MIB", "zxAnPonOnuId"),
    (0, "ZXANVLANTRANS-MIB", "zxAnOnuPortId"),
    (0, "ZXANVLANTRANS-MIB", "zxAnVlanTransOriginalCvlan"),
)
if mibBuilder.loadTexts:
    zxAnVlanTransRuleEntry.setStatus("current")
_ZxAnPonOnuId_Type = Integer32
_ZxAnPonOnuId_Object = MibTableColumn
zxAnPonOnuId = _ZxAnPonOnuId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 10, 1, 1, 1),
    _ZxAnPonOnuId_Type()
)
zxAnPonOnuId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPonOnuId.setStatus("current")
_ZxAnOnuPortId_Type = Integer32
_ZxAnOnuPortId_Object = MibTableColumn
zxAnOnuPortId = _ZxAnOnuPortId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 10, 1, 1, 2),
    _ZxAnOnuPortId_Type()
)
zxAnOnuPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnOnuPortId.setStatus("current")
_ZxAnVlanTransOriginalCvlan_Type = VlanId
_ZxAnVlanTransOriginalCvlan_Object = MibTableColumn
zxAnVlanTransOriginalCvlan = _ZxAnVlanTransOriginalCvlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 10, 1, 1, 3),
    _ZxAnVlanTransOriginalCvlan_Type()
)
zxAnVlanTransOriginalCvlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVlanTransOriginalCvlan.setStatus("current")
_ZxAnVlanTransNewCvlan_Type = VlanId
_ZxAnVlanTransNewCvlan_Object = MibTableColumn
zxAnVlanTransNewCvlan = _ZxAnVlanTransNewCvlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 10, 1, 1, 4),
    _ZxAnVlanTransNewCvlan_Type()
)
zxAnVlanTransNewCvlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanTransNewCvlan.setStatus("current")


class _ZxAnVlanTransBroadcast_Type(Integer32):
    """Custom type zxAnVlanTransBroadcast based on Integer32"""
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


_ZxAnVlanTransBroadcast_Type.__name__ = "Integer32"
_ZxAnVlanTransBroadcast_Object = MibTableColumn
zxAnVlanTransBroadcast = _ZxAnVlanTransBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 10, 1, 1, 5),
    _ZxAnVlanTransBroadcast_Type()
)
zxAnVlanTransBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanTransBroadcast.setStatus("current")


class _ZxAnVlanTransMode_Type(Integer32):
    """Custom type zxAnVlanTransMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneToOne", 1),
          ("nToOne", 2))
    )


_ZxAnVlanTransMode_Type.__name__ = "Integer32"
_ZxAnVlanTransMode_Object = MibTableColumn
zxAnVlanTransMode = _ZxAnVlanTransMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 10, 1, 1, 6),
    _ZxAnVlanTransMode_Type()
)
zxAnVlanTransMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanTransMode.setStatus("current")
_ZxAnVlanTransEntryStatus_Type = RowStatus
_ZxAnVlanTransEntryStatus_Object = MibTableColumn
zxAnVlanTransEntryStatus = _ZxAnVlanTransEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 10, 1, 1, 10),
    _ZxAnVlanTransEntryStatus_Type()
)
zxAnVlanTransEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanTransEntryStatus.setStatus("current")
_ZxAnVlanTransGlobalTable_Object = MibTable
zxAnVlanTransGlobalTable = _ZxAnVlanTransGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 10, 2)
)
if mibBuilder.loadTexts:
    zxAnVlanTransGlobalTable.setStatus("current")
_ZxAnVlanTransGlobalEntry_Object = MibTableRow
zxAnVlanTransGlobalEntry = _ZxAnVlanTransGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 10, 2, 1)
)
zxAnVlanTransGlobalEntry.setIndexNames(
    (0, "ZXANVLANTRANS-MIB", "zxAnPonOnuId"),
)
if mibBuilder.loadTexts:
    zxAnVlanTransGlobalEntry.setStatus("current")
_ZxAnVlanTransSvlanBase_Type = VlanId
_ZxAnVlanTransSvlanBase_Object = MibTableColumn
zxAnVlanTransSvlanBase = _ZxAnVlanTransSvlanBase_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 10, 2, 1, 1),
    _ZxAnVlanTransSvlanBase_Type()
)
zxAnVlanTransSvlanBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanTransSvlanBase.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXANVLANTRANS-MIB",
    **{"zxAnVlanTrans": zxAnVlanTrans,
       "zxAnVlanTransRuleTable": zxAnVlanTransRuleTable,
       "zxAnVlanTransRuleEntry": zxAnVlanTransRuleEntry,
       "zxAnPonOnuId": zxAnPonOnuId,
       "zxAnOnuPortId": zxAnOnuPortId,
       "zxAnVlanTransOriginalCvlan": zxAnVlanTransOriginalCvlan,
       "zxAnVlanTransNewCvlan": zxAnVlanTransNewCvlan,
       "zxAnVlanTransBroadcast": zxAnVlanTransBroadcast,
       "zxAnVlanTransMode": zxAnVlanTransMode,
       "zxAnVlanTransEntryStatus": zxAnVlanTransEntryStatus,
       "zxAnVlanTransGlobalTable": zxAnVlanTransGlobalTable,
       "zxAnVlanTransGlobalEntry": zxAnVlanTransGlobalEntry,
       "zxAnVlanTransSvlanBase": zxAnVlanTransSvlanBase}
)
