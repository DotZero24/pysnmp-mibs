# SNMP MIB module (ZTE-AN-VMAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-VMAC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:12 2025
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

(VlanId,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "VlanId",
    "zxAn")


# MODULE-IDENTITY

zxAnVmacMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 101)
)
if mibBuilder.loadTexts:
    zxAnVmacMib.setRevisions(
        ("1913-08-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnVmacObjects_ObjectIdentity = ObjectIdentity
zxAnVmacObjects = _ZxAnVmacObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 101, 2)
)
_ZxAnVmacVlanObjects_ObjectIdentity = ObjectIdentity
zxAnVmacVlanObjects = _ZxAnVmacVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 101, 2, 1)
)
_ZxAnVmacVlanTable_Object = MibTable
zxAnVmacVlanTable = _ZxAnVmacVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 101, 2, 1, 2)
)
if mibBuilder.loadTexts:
    zxAnVmacVlanTable.setStatus("current")
_ZxAnVmacVlanEntry_Object = MibTableRow
zxAnVmacVlanEntry = _ZxAnVmacVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 101, 2, 1, 2, 1)
)
zxAnVmacVlanEntry.setIndexNames(
    (0, "ZTE-AN-VMAC-MIB", "zxAnVmacVid"),
)
if mibBuilder.loadTexts:
    zxAnVmacVlanEntry.setStatus("current")
_ZxAnVmacVid_Type = VlanId
_ZxAnVmacVid_Object = MibTableColumn
zxAnVmacVid = _ZxAnVmacVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 101, 2, 1, 2, 1, 1),
    _ZxAnVmacVid_Type()
)
zxAnVmacVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVmacVid.setStatus("current")


class _ZxAnVmacMacPoolIndex_Type(Integer32):
    """Custom type zxAnVmacMacPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ZxAnVmacMacPoolIndex_Type.__name__ = "Integer32"
_ZxAnVmacMacPoolIndex_Object = MibTableColumn
zxAnVmacMacPoolIndex = _ZxAnVmacMacPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 101, 2, 1, 2, 1, 2),
    _ZxAnVmacMacPoolIndex_Type()
)
zxAnVmacMacPoolIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVmacMacPoolIndex.setStatus("current")
_ZxAnVmacVlanRowStatus_Type = RowStatus
_ZxAnVmacVlanRowStatus_Object = MibTableColumn
zxAnVmacVlanRowStatus = _ZxAnVmacVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 101, 2, 1, 2, 1, 50),
    _ZxAnVmacVlanRowStatus_Type()
)
zxAnVmacVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVmacVlanRowStatus.setStatus("current")
_ZxAnVmacIfObjects_ObjectIdentity = ObjectIdentity
zxAnVmacIfObjects = _ZxAnVmacIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 101, 2, 2)
)
_ZxAnVmacIfConfTable_Object = MibTable
zxAnVmacIfConfTable = _ZxAnVmacIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 101, 2, 2, 2)
)
if mibBuilder.loadTexts:
    zxAnVmacIfConfTable.setStatus("current")
_ZxAnVmacIfConfEntry_Object = MibTableRow
zxAnVmacIfConfEntry = _ZxAnVmacIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 101, 2, 2, 2, 1)
)
zxAnVmacIfConfEntry.setIndexNames(
    (0, "ZTE-AN-VMAC-MIB", "zxAnVmacIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnVmacIfConfEntry.setStatus("current")
_ZxAnVmacIfIndex_Type = InterfaceIndex
_ZxAnVmacIfIndex_Object = MibTableColumn
zxAnVmacIfIndex = _ZxAnVmacIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 101, 2, 2, 2, 1, 1),
    _ZxAnVmacIfIndex_Type()
)
zxAnVmacIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVmacIfIndex.setStatus("current")


class _ZxAnVmacIfConfTranslateEnable_Type(Integer32):
    """Custom type zxAnVmacIfConfTranslateEnable based on Integer32"""
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


_ZxAnVmacIfConfTranslateEnable_Type.__name__ = "Integer32"
_ZxAnVmacIfConfTranslateEnable_Object = MibTableColumn
zxAnVmacIfConfTranslateEnable = _ZxAnVmacIfConfTranslateEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 101, 2, 2, 2, 1, 2),
    _ZxAnVmacIfConfTranslateEnable_Type()
)
zxAnVmacIfConfTranslateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVmacIfConfTranslateEnable.setStatus("current")


class _ZxAnVmacIfConfTranslateLimit_Type(Integer32):
    """Custom type zxAnVmacIfConfTranslateLimit based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ZxAnVmacIfConfTranslateLimit_Type.__name__ = "Integer32"
_ZxAnVmacIfConfTranslateLimit_Object = MibTableColumn
zxAnVmacIfConfTranslateLimit = _ZxAnVmacIfConfTranslateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 101, 2, 2, 2, 1, 3),
    _ZxAnVmacIfConfTranslateLimit_Type()
)
zxAnVmacIfConfTranslateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVmacIfConfTranslateLimit.setStatus("current")
_ZxAnVmacIfTranslateTable_Object = MibTable
zxAnVmacIfTranslateTable = _ZxAnVmacIfTranslateTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 101, 2, 2, 3)
)
if mibBuilder.loadTexts:
    zxAnVmacIfTranslateTable.setStatus("current")
_ZxAnVmacIfTranslateEntry_Object = MibTableRow
zxAnVmacIfTranslateEntry = _ZxAnVmacIfTranslateEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 101, 2, 2, 3, 1)
)
zxAnVmacIfTranslateEntry.setIndexNames(
    (0, "ZTE-AN-VMAC-MIB", "zxAnVmacIfIndex"),
    (0, "ZTE-AN-VMAC-MIB", "zxAnVmacIfTranslateVid"),
    (0, "ZTE-AN-VMAC-MIB", "zxAnVmacIfTranslateSrcMac"),
)
if mibBuilder.loadTexts:
    zxAnVmacIfTranslateEntry.setStatus("current")
_ZxAnVmacIfTranslateVid_Type = VlanId
_ZxAnVmacIfTranslateVid_Object = MibTableColumn
zxAnVmacIfTranslateVid = _ZxAnVmacIfTranslateVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 101, 2, 2, 3, 1, 1),
    _ZxAnVmacIfTranslateVid_Type()
)
zxAnVmacIfTranslateVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVmacIfTranslateVid.setStatus("current")
_ZxAnVmacIfTranslateSrcMac_Type = MacAddress
_ZxAnVmacIfTranslateSrcMac_Object = MibTableColumn
zxAnVmacIfTranslateSrcMac = _ZxAnVmacIfTranslateSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 101, 2, 2, 3, 1, 2),
    _ZxAnVmacIfTranslateSrcMac_Type()
)
zxAnVmacIfTranslateSrcMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVmacIfTranslateSrcMac.setStatus("current")
_ZxAnVmacIfTranslateVmac_Type = MacAddress
_ZxAnVmacIfTranslateVmac_Object = MibTableColumn
zxAnVmacIfTranslateVmac = _ZxAnVmacIfTranslateVmac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 101, 2, 2, 3, 1, 3),
    _ZxAnVmacIfTranslateVmac_Type()
)
zxAnVmacIfTranslateVmac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVmacIfTranslateVmac.setStatus("current")
_ZxAnVmacIfTranslateRowStatus_Type = RowStatus
_ZxAnVmacIfTranslateRowStatus_Object = MibTableColumn
zxAnVmacIfTranslateRowStatus = _ZxAnVmacIfTranslateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 101, 2, 2, 3, 1, 50),
    _ZxAnVmacIfTranslateRowStatus_Type()
)
zxAnVmacIfTranslateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVmacIfTranslateRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-VMAC-MIB",
    **{"zxAnVmacMib": zxAnVmacMib,
       "zxAnVmacObjects": zxAnVmacObjects,
       "zxAnVmacVlanObjects": zxAnVmacVlanObjects,
       "zxAnVmacVlanTable": zxAnVmacVlanTable,
       "zxAnVmacVlanEntry": zxAnVmacVlanEntry,
       "zxAnVmacVid": zxAnVmacVid,
       "zxAnVmacMacPoolIndex": zxAnVmacMacPoolIndex,
       "zxAnVmacVlanRowStatus": zxAnVmacVlanRowStatus,
       "zxAnVmacIfObjects": zxAnVmacIfObjects,
       "zxAnVmacIfConfTable": zxAnVmacIfConfTable,
       "zxAnVmacIfConfEntry": zxAnVmacIfConfEntry,
       "zxAnVmacIfIndex": zxAnVmacIfIndex,
       "zxAnVmacIfConfTranslateEnable": zxAnVmacIfConfTranslateEnable,
       "zxAnVmacIfConfTranslateLimit": zxAnVmacIfConfTranslateLimit,
       "zxAnVmacIfTranslateTable": zxAnVmacIfTranslateTable,
       "zxAnVmacIfTranslateEntry": zxAnVmacIfTranslateEntry,
       "zxAnVmacIfTranslateVid": zxAnVmacIfTranslateVid,
       "zxAnVmacIfTranslateSrcMac": zxAnVmacIfTranslateSrcMac,
       "zxAnVmacIfTranslateVmac": zxAnVmacIfTranslateVmac,
       "zxAnVmacIfTranslateRowStatus": zxAnVmacIfTranslateRowStatus}
)
