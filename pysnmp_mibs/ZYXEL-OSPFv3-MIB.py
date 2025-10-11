# SNMP MIB module (ZYXEL-OSPFv3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zyxel/ZYXEL-OSPFv3-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:01:31 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelOspfv3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 117)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelOspfv3Setup_ObjectIdentity = ObjectIdentity
zyxelOspfv3Setup = _ZyxelOspfv3Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 117, 1)
)
_ZyxelOspfv3RedistributeRouteTable_Object = MibTable
zyxelOspfv3RedistributeRouteTable = _ZyxelOspfv3RedistributeRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 117, 1, 1)
)
if mibBuilder.loadTexts:
    zyxelOspfv3RedistributeRouteTable.setStatus("current")
_ZyxelOspfv3RedistributeRouteEntry_Object = MibTableRow
zyxelOspfv3RedistributeRouteEntry = _ZyxelOspfv3RedistributeRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 117, 1, 1, 1)
)
zyxelOspfv3RedistributeRouteEntry.setIndexNames(
    (0, "ZYXEL-OSPFv3-MIB", "zyOspfv3RedistributeRouteProtocol"),
)
if mibBuilder.loadTexts:
    zyxelOspfv3RedistributeRouteEntry.setStatus("current")


class _ZyOspfv3RedistributeRouteProtocol_Type(Integer32):
    """Custom type zyOspfv3RedistributeRouteProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ripng", 1),
          ("static", 2))
    )


_ZyOspfv3RedistributeRouteProtocol_Type.__name__ = "Integer32"
_ZyOspfv3RedistributeRouteProtocol_Object = MibTableColumn
zyOspfv3RedistributeRouteProtocol = _ZyOspfv3RedistributeRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 117, 1, 1, 1, 1),
    _ZyOspfv3RedistributeRouteProtocol_Type()
)
zyOspfv3RedistributeRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyOspfv3RedistributeRouteProtocol.setStatus("current")
_ZyOspfv3RedistributeRouteState_Type = EnabledStatus
_ZyOspfv3RedistributeRouteState_Object = MibTableColumn
zyOspfv3RedistributeRouteState = _ZyOspfv3RedistributeRouteState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 117, 1, 1, 1, 2),
    _ZyOspfv3RedistributeRouteState_Type()
)
zyOspfv3RedistributeRouteState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyOspfv3RedistributeRouteState.setStatus("current")
_ZyOspfv3RedistributeRouteType_Type = Integer32
_ZyOspfv3RedistributeRouteType_Object = MibTableColumn
zyOspfv3RedistributeRouteType = _ZyOspfv3RedistributeRouteType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 117, 1, 1, 1, 3),
    _ZyOspfv3RedistributeRouteType_Type()
)
zyOspfv3RedistributeRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyOspfv3RedistributeRouteType.setStatus("current")
_ZyOspfv3RedistributeRouteMetric_Type = Integer32
_ZyOspfv3RedistributeRouteMetric_Object = MibTableColumn
zyOspfv3RedistributeRouteMetric = _ZyOspfv3RedistributeRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 117, 1, 1, 1, 4),
    _ZyOspfv3RedistributeRouteMetric_Type()
)
zyOspfv3RedistributeRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyOspfv3RedistributeRouteMetric.setStatus("current")
_ZyxelOspfv3GeneralGroup_ObjectIdentity = ObjectIdentity
zyxelOspfv3GeneralGroup = _ZyxelOspfv3GeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 117, 1, 2)
)
_ZyOspfv3Distance_Type = Integer32
_ZyOspfv3Distance_Object = MibScalar
zyOspfv3Distance = _ZyOspfv3Distance_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 117, 1, 2, 1),
    _ZyOspfv3Distance_Type()
)
zyOspfv3Distance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyOspfv3Distance.setStatus("current")
_ZyxelOspfv3Notifications_ObjectIdentity = ObjectIdentity
zyxelOspfv3Notifications = _ZyxelOspfv3Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 117, 4)
)

# Managed Objects groups


# Notification objects

zyOspfv3ExceedMaxDynamicRoutePath = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 117, 4, 1)
)
if mibBuilder.loadTexts:
    zyOspfv3ExceedMaxDynamicRoutePath.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-OSPFv3-MIB",
    **{"zyxelOspfv3": zyxelOspfv3,
       "zyxelOspfv3Setup": zyxelOspfv3Setup,
       "zyxelOspfv3RedistributeRouteTable": zyxelOspfv3RedistributeRouteTable,
       "zyxelOspfv3RedistributeRouteEntry": zyxelOspfv3RedistributeRouteEntry,
       "zyOspfv3RedistributeRouteProtocol": zyOspfv3RedistributeRouteProtocol,
       "zyOspfv3RedistributeRouteState": zyOspfv3RedistributeRouteState,
       "zyOspfv3RedistributeRouteType": zyOspfv3RedistributeRouteType,
       "zyOspfv3RedistributeRouteMetric": zyOspfv3RedistributeRouteMetric,
       "zyxelOspfv3GeneralGroup": zyxelOspfv3GeneralGroup,
       "zyOspfv3Distance": zyOspfv3Distance,
       "zyxelOspfv3Notifications": zyxelOspfv3Notifications,
       "zyOspfv3ExceedMaxDynamicRoutePath": zyOspfv3ExceedMaxDynamicRoutePath}
)
