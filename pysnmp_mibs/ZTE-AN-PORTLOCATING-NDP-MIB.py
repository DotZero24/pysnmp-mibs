# SNMP MIB module (ZTE-AN-PORTLOCATING-NDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-PORTLOCATING-NDP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:55 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(zxAnPortLocatingMib,) = mibBuilder.importSymbols(
    "ZTE-AN-PORT-LOCATING-MIB",
    "zxAnPortLocatingMib")

(zxAn,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "zxAn")


# MODULE-IDENTITY

zxAnPortLocatingNdpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 45)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnPortLocatingNdpGlobal_ObjectIdentity = ObjectIdentity
zxAnPortLocatingNdpGlobal = _ZxAnPortLocatingNdpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 45, 1)
)


class _ZxAnNdpLioEnable_Type(Integer32):
    """Custom type zxAnNdpLioEnable based on Integer32"""
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


_ZxAnNdpLioEnable_Type.__name__ = "Integer32"
_ZxAnNdpLioEnable_Object = MibScalar
zxAnNdpLioEnable = _ZxAnNdpLioEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 45, 1, 1),
    _ZxAnNdpLioEnable_Type()
)
zxAnNdpLioEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnNdpLioEnable.setStatus("current")
_ZxAnPortLocatingNdpTable_Object = MibTable
zxAnPortLocatingNdpTable = _ZxAnPortLocatingNdpTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 45, 2)
)
if mibBuilder.loadTexts:
    zxAnPortLocatingNdpTable.setStatus("current")
_ZxAnPortLocatingNdpEntry_Object = MibTableRow
zxAnPortLocatingNdpEntry = _ZxAnPortLocatingNdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 45, 2, 1)
)
zxAnPortLocatingNdpEntry.setIndexNames(
    (0, "ZTE-AN-PORTLOCATING-NDP-MIB", "zxAnPortLocatingNdpRack"),
    (0, "ZTE-AN-PORTLOCATING-NDP-MIB", "zxAnPortLocatingNdpShelf"),
    (0, "ZTE-AN-PORTLOCATING-NDP-MIB", "zxAnPortLocatingNdpSlot"),
    (0, "ZTE-AN-PORTLOCATING-NDP-MIB", "zxAnPortLocatingNdpPort"),
    (0, "ZTE-AN-PORTLOCATING-NDP-MIB", "zxAnPortLocatingNdpOnu"),
    (0, "ZTE-AN-PORTLOCATING-NDP-MIB", "zxAnPortLocatingNdpIfType"),
    (0, "ZTE-AN-PORTLOCATING-NDP-MIB", "zxAnPortLocatingNdpLogicalId"),
)
if mibBuilder.loadTexts:
    zxAnPortLocatingNdpEntry.setStatus("current")
_ZxAnPortLocatingNdpRack_Type = Integer32
_ZxAnPortLocatingNdpRack_Object = MibTableColumn
zxAnPortLocatingNdpRack = _ZxAnPortLocatingNdpRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 45, 2, 1, 1),
    _ZxAnPortLocatingNdpRack_Type()
)
zxAnPortLocatingNdpRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPortLocatingNdpRack.setStatus("current")
_ZxAnPortLocatingNdpShelf_Type = Integer32
_ZxAnPortLocatingNdpShelf_Object = MibTableColumn
zxAnPortLocatingNdpShelf = _ZxAnPortLocatingNdpShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 45, 2, 1, 2),
    _ZxAnPortLocatingNdpShelf_Type()
)
zxAnPortLocatingNdpShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPortLocatingNdpShelf.setStatus("current")
_ZxAnPortLocatingNdpSlot_Type = Integer32
_ZxAnPortLocatingNdpSlot_Object = MibTableColumn
zxAnPortLocatingNdpSlot = _ZxAnPortLocatingNdpSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 45, 2, 1, 3),
    _ZxAnPortLocatingNdpSlot_Type()
)
zxAnPortLocatingNdpSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPortLocatingNdpSlot.setStatus("current")
_ZxAnPortLocatingNdpPort_Type = Integer32
_ZxAnPortLocatingNdpPort_Object = MibTableColumn
zxAnPortLocatingNdpPort = _ZxAnPortLocatingNdpPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 45, 2, 1, 4),
    _ZxAnPortLocatingNdpPort_Type()
)
zxAnPortLocatingNdpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPortLocatingNdpPort.setStatus("current")
_ZxAnPortLocatingNdpOnu_Type = Integer32
_ZxAnPortLocatingNdpOnu_Object = MibTableColumn
zxAnPortLocatingNdpOnu = _ZxAnPortLocatingNdpOnu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 45, 2, 1, 5),
    _ZxAnPortLocatingNdpOnu_Type()
)
zxAnPortLocatingNdpOnu.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPortLocatingNdpOnu.setStatus("current")


class _ZxAnPortLocatingNdpIfType_Type(Integer32):
    """Custom type zxAnPortLocatingNdpIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bridgePort", 2),
          ("ponVPort", 4))
    )


_ZxAnPortLocatingNdpIfType_Type.__name__ = "Integer32"
_ZxAnPortLocatingNdpIfType_Object = MibTableColumn
zxAnPortLocatingNdpIfType = _ZxAnPortLocatingNdpIfType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 45, 2, 1, 6),
    _ZxAnPortLocatingNdpIfType_Type()
)
zxAnPortLocatingNdpIfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPortLocatingNdpIfType.setStatus("current")
_ZxAnPortLocatingNdpLogicalId_Type = ObjectIdentifier
_ZxAnPortLocatingNdpLogicalId_Object = MibTableColumn
zxAnPortLocatingNdpLogicalId = _ZxAnPortLocatingNdpLogicalId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 45, 2, 1, 7),
    _ZxAnPortLocatingNdpLogicalId_Type()
)
zxAnPortLocatingNdpLogicalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPortLocatingNdpLogicalId.setStatus("current")


class _ZxAnNdpLioIfConfEnable_Type(Integer32):
    """Custom type zxAnNdpLioIfConfEnable based on Integer32"""
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


_ZxAnNdpLioIfConfEnable_Type.__name__ = "Integer32"
_ZxAnNdpLioIfConfEnable_Object = MibTableColumn
zxAnNdpLioIfConfEnable = _ZxAnNdpLioIfConfEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 45, 2, 1, 8),
    _ZxAnNdpLioIfConfEnable_Type()
)
zxAnNdpLioIfConfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnNdpLioIfConfEnable.setStatus("current")


class _ZxAnNdpLioIfConfTrust_Type(TruthValue):
    """Custom type zxAnNdpLioIfConfTrust based on TruthValue"""
    defaultValue = 2


_ZxAnNdpLioIfConfTrust_Type.__name__ = "TruthValue"
_ZxAnNdpLioIfConfTrust_Object = MibTableColumn
zxAnNdpLioIfConfTrust = _ZxAnNdpLioIfConfTrust_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 45, 2, 1, 9),
    _ZxAnNdpLioIfConfTrust_Type()
)
zxAnNdpLioIfConfTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnNdpLioIfConfTrust.setStatus("current")


class _ZxAnNdpLioIfConfPolicy_Type(Integer32):
    """Custom type zxAnNdpLioIfConfPolicy based on Integer32"""
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
        *(("keep", 1),
          ("replace", 2),
          ("discard", 3),
          ("add", 4))
    )


_ZxAnNdpLioIfConfPolicy_Type.__name__ = "Integer32"
_ZxAnNdpLioIfConfPolicy_Object = MibTableColumn
zxAnNdpLioIfConfPolicy = _ZxAnNdpLioIfConfPolicy_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 45, 2, 1, 10),
    _ZxAnNdpLioIfConfPolicy_Type()
)
zxAnNdpLioIfConfPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnNdpLioIfConfPolicy.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-PORTLOCATING-NDP-MIB",
    **{"zxAnPortLocatingNdpMib": zxAnPortLocatingNdpMib,
       "zxAnPortLocatingNdpGlobal": zxAnPortLocatingNdpGlobal,
       "zxAnNdpLioEnable": zxAnNdpLioEnable,
       "zxAnPortLocatingNdpTable": zxAnPortLocatingNdpTable,
       "zxAnPortLocatingNdpEntry": zxAnPortLocatingNdpEntry,
       "zxAnPortLocatingNdpRack": zxAnPortLocatingNdpRack,
       "zxAnPortLocatingNdpShelf": zxAnPortLocatingNdpShelf,
       "zxAnPortLocatingNdpSlot": zxAnPortLocatingNdpSlot,
       "zxAnPortLocatingNdpPort": zxAnPortLocatingNdpPort,
       "zxAnPortLocatingNdpOnu": zxAnPortLocatingNdpOnu,
       "zxAnPortLocatingNdpIfType": zxAnPortLocatingNdpIfType,
       "zxAnPortLocatingNdpLogicalId": zxAnPortLocatingNdpLogicalId,
       "zxAnNdpLioIfConfEnable": zxAnNdpLioIfConfEnable,
       "zxAnNdpLioIfConfTrust": zxAnNdpLioIfConfTrust,
       "zxAnNdpLioIfConfPolicy": zxAnNdpLioIfConfPolicy}
)
