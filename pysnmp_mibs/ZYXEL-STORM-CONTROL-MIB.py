# SNMP MIB module (ZYXEL-STORM-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zyxel/ZYXEL-STORM-CONTROL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:02:46 2025
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelStormControl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 78)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelStormControlSetup_ObjectIdentity = ObjectIdentity
zyxelStormControlSetup = _ZyxelStormControlSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 78, 1)
)
_ZyStromControlState_Type = EnabledStatus
_ZyStromControlState_Object = MibScalar
zyStromControlState = _ZyStromControlState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 78, 1, 1),
    _ZyStromControlState_Type()
)
zyStromControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyStromControlState.setStatus("current")
_ZyxelStromControlPortTable_Object = MibTable
zyxelStromControlPortTable = _ZyxelStromControlPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 78, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelStromControlPortTable.setStatus("current")
_ZyxelStromControlPortEntry_Object = MibTableRow
zyxelStromControlPortEntry = _ZyxelStromControlPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 78, 1, 2, 1)
)
zyxelStromControlPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelStromControlPortEntry.setStatus("current")
_ZyStromControlPortBroadcastState_Type = EnabledStatus
_ZyStromControlPortBroadcastState_Object = MibTableColumn
zyStromControlPortBroadcastState = _ZyStromControlPortBroadcastState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 78, 1, 2, 1, 1),
    _ZyStromControlPortBroadcastState_Type()
)
zyStromControlPortBroadcastState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyStromControlPortBroadcastState.setStatus("current")
_ZyStromControlPortBroadcastRate_Type = Integer32
_ZyStromControlPortBroadcastRate_Object = MibTableColumn
zyStromControlPortBroadcastRate = _ZyStromControlPortBroadcastRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 78, 1, 2, 1, 2),
    _ZyStromControlPortBroadcastRate_Type()
)
zyStromControlPortBroadcastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyStromControlPortBroadcastRate.setStatus("current")
_ZyStromControlPortMulticastState_Type = EnabledStatus
_ZyStromControlPortMulticastState_Object = MibTableColumn
zyStromControlPortMulticastState = _ZyStromControlPortMulticastState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 78, 1, 2, 1, 3),
    _ZyStromControlPortMulticastState_Type()
)
zyStromControlPortMulticastState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyStromControlPortMulticastState.setStatus("current")
_ZyStromControlPortMulticastRate_Type = Integer32
_ZyStromControlPortMulticastRate_Object = MibTableColumn
zyStromControlPortMulticastRate = _ZyStromControlPortMulticastRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 78, 1, 2, 1, 4),
    _ZyStromControlPortMulticastRate_Type()
)
zyStromControlPortMulticastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyStromControlPortMulticastRate.setStatus("current")
_ZyStromControlPortDlfState_Type = EnabledStatus
_ZyStromControlPortDlfState_Object = MibTableColumn
zyStromControlPortDlfState = _ZyStromControlPortDlfState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 78, 1, 2, 1, 5),
    _ZyStromControlPortDlfState_Type()
)
zyStromControlPortDlfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyStromControlPortDlfState.setStatus("current")
_ZyStromControlPortDlfRate_Type = Integer32
_ZyStromControlPortDlfRate_Object = MibTableColumn
zyStromControlPortDlfRate = _ZyStromControlPortDlfRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 78, 1, 2, 1, 6),
    _ZyStromControlPortDlfRate_Type()
)
zyStromControlPortDlfRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyStromControlPortDlfRate.setStatus("current")
_ZyxelStormControlNotifications_ObjectIdentity = ObjectIdentity
zyxelStormControlNotifications = _ZyxelStormControlNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 78, 2)
)
_ZyxelStormControlTrapInfoObject_ObjectIdentity = ObjectIdentity
zyxelStormControlTrapInfoObject = _ZyxelStormControlTrapInfoObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 78, 3)
)


class _ZyStormControlType_Type(Integer32):
    """Custom type zyStormControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcast-storm", 1),
          ("multicast-storm", 2))
    )


_ZyStormControlType_Type.__name__ = "Integer32"
_ZyStormControlType_Object = MibScalar
zyStormControlType = _ZyStormControlType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 78, 3, 1),
    _ZyStormControlType_Type()
)
zyStormControlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyStormControlType.setStatus("current")

# Managed Objects groups


# Notification objects

zyPortStormControlTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 78, 2, 1)
)
zyPortStormControlTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZYXEL-STORM-CONTROL-MIB", "zyStormControlType"))
)
if mibBuilder.loadTexts:
    zyPortStormControlTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-STORM-CONTROL-MIB",
    **{"zyxelStormControl": zyxelStormControl,
       "zyxelStormControlSetup": zyxelStormControlSetup,
       "zyStromControlState": zyStromControlState,
       "zyxelStromControlPortTable": zyxelStromControlPortTable,
       "zyxelStromControlPortEntry": zyxelStromControlPortEntry,
       "zyStromControlPortBroadcastState": zyStromControlPortBroadcastState,
       "zyStromControlPortBroadcastRate": zyStromControlPortBroadcastRate,
       "zyStromControlPortMulticastState": zyStromControlPortMulticastState,
       "zyStromControlPortMulticastRate": zyStromControlPortMulticastRate,
       "zyStromControlPortDlfState": zyStromControlPortDlfState,
       "zyStromControlPortDlfRate": zyStromControlPortDlfRate,
       "zyxelStormControlNotifications": zyxelStormControlNotifications,
       "zyPortStormControlTrap": zyPortStormControlTrap,
       "zyxelStormControlTrapInfoObject": zyxelStormControlTrapInfoObject,
       "zyStormControlType": zyStormControlType}
)
