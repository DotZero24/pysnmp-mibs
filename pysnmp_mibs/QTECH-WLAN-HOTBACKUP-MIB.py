# SNMP MIB module (QTECH-WLAN-HOTBACKUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-WLAN-HOTBACKUP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:43 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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

qtechWlanHotbackupMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 115)
)
if mibBuilder.loadTexts:
    qtechWlanHotbackupMIB.setRevisions(
        ("2012-07-31 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechWlanHotbackupMIBObjects_ObjectIdentity = ObjectIdentity
qtechWlanHotbackupMIBObjects = _QtechWlanHotbackupMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 115, 1)
)
_QtechWlanHotbackupPeerTable_Object = MibTable
qtechWlanHotbackupPeerTable = _QtechWlanHotbackupPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 115, 1, 1)
)
if mibBuilder.loadTexts:
    qtechWlanHotbackupPeerTable.setStatus("current")
_QtechWlanHotbackupPeerEntry_Object = MibTableRow
qtechWlanHotbackupPeerEntry = _QtechWlanHotbackupPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 115, 1, 1, 1)
)
qtechWlanHotbackupPeerEntry.setIndexNames(
    (0, "QTECH-WLAN-HOTBACKUP-MIB", "qtechWlanHotbackupIpAddress"),
)
if mibBuilder.loadTexts:
    qtechWlanHotbackupPeerEntry.setStatus("current")
_QtechWlanHotbackupIpAddress_Type = IpAddress
_QtechWlanHotbackupIpAddress_Object = MibTableColumn
qtechWlanHotbackupIpAddress = _QtechWlanHotbackupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 115, 1, 1, 1, 1),
    _QtechWlanHotbackupIpAddress_Type()
)
qtechWlanHotbackupIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechWlanHotbackupIpAddress.setStatus("current")


class _QtechWlanHotbackupIsEnabled_Type(Integer32):
    """Custom type qtechWlanHotbackupIsEnabled based on Integer32"""
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


_QtechWlanHotbackupIsEnabled_Type.__name__ = "Integer32"
_QtechWlanHotbackupIsEnabled_Object = MibTableColumn
qtechWlanHotbackupIsEnabled = _QtechWlanHotbackupIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 115, 1, 1, 1, 2),
    _QtechWlanHotbackupIsEnabled_Type()
)
qtechWlanHotbackupIsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWlanHotbackupIsEnabled.setStatus("current")


class _QtechWlanHotbackupState_Type(Integer32):
    """Custom type qtechWlanHotbackupState based on Integer32"""
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
        *(("hb-disable", 1),
          ("probe", 2),
          ("hdsk", 3),
          ("tcp-connect", 4),
          ("sulking", 5),
          ("channel-up", 6))
    )


_QtechWlanHotbackupState_Type.__name__ = "Integer32"
_QtechWlanHotbackupState_Object = MibTableColumn
qtechWlanHotbackupState = _QtechWlanHotbackupState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 115, 1, 1, 1, 3),
    _QtechWlanHotbackupState_Type()
)
qtechWlanHotbackupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWlanHotbackupState.setStatus("current")
_QtechWlanHotbackupContextTable_Object = MibTable
qtechWlanHotbackupContextTable = _QtechWlanHotbackupContextTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 115, 1, 2)
)
if mibBuilder.loadTexts:
    qtechWlanHotbackupContextTable.setStatus("current")
_QtechWlanHotbackupContextEntry_Object = MibTableRow
qtechWlanHotbackupContextEntry = _QtechWlanHotbackupContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 115, 1, 2, 1)
)
qtechWlanHotbackupContextEntry.setIndexNames(
    (0, "QTECH-WLAN-HOTBACKUP-MIB", "qtechWlanHotbackupCtxIpAddress"),
    (0, "QTECH-WLAN-HOTBACKUP-MIB", "qtechWlanHotbackupContextId"),
)
if mibBuilder.loadTexts:
    qtechWlanHotbackupContextEntry.setStatus("current")
_QtechWlanHotbackupCtxIpAddress_Type = IpAddress
_QtechWlanHotbackupCtxIpAddress_Object = MibTableColumn
qtechWlanHotbackupCtxIpAddress = _QtechWlanHotbackupCtxIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 115, 1, 2, 1, 1),
    _QtechWlanHotbackupCtxIpAddress_Type()
)
qtechWlanHotbackupCtxIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWlanHotbackupCtxIpAddress.setStatus("current")
_QtechWlanHotbackupContextId_Type = Integer32
_QtechWlanHotbackupContextId_Object = MibTableColumn
qtechWlanHotbackupContextId = _QtechWlanHotbackupContextId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 115, 1, 2, 1, 2),
    _QtechWlanHotbackupContextId_Type()
)
qtechWlanHotbackupContextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWlanHotbackupContextId.setStatus("current")


class _QtechWlanHotbackupContextState_Type(Integer32):
    """Custom type qtechWlanHotbackupContextState based on Integer32"""
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
        *(("disable", 0),
          ("unknown", 1),
          ("single-active", 2),
          ("single-standby", 3),
          ("pair-active", 4),
          ("pair-standby", 5))
    )


_QtechWlanHotbackupContextState_Type.__name__ = "Integer32"
_QtechWlanHotbackupContextState_Object = MibTableColumn
qtechWlanHotbackupContextState = _QtechWlanHotbackupContextState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 115, 1, 2, 1, 3),
    _QtechWlanHotbackupContextState_Type()
)
qtechWlanHotbackupContextState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWlanHotbackupContextState.setStatus("current")
_QtechWlanHotbackupNotificationsMIBObjects_ObjectIdentity = ObjectIdentity
qtechWlanHotbackupNotificationsMIBObjects = _QtechWlanHotbackupNotificationsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 115, 2)
)
_QtechWlanHotbackupNtfObjects_ObjectIdentity = ObjectIdentity
qtechWlanHotbackupNtfObjects = _QtechWlanHotbackupNtfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 115, 2, 1)
)
_QtechNotifyPeerIpType_Type = InetAddressType
_QtechNotifyPeerIpType_Object = MibScalar
qtechNotifyPeerIpType = _QtechNotifyPeerIpType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 115, 2, 1, 1),
    _QtechNotifyPeerIpType_Type()
)
qtechNotifyPeerIpType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyPeerIpType.setStatus("current")
_QtechNotifyPeerIp_Type = InetAddress
_QtechNotifyPeerIp_Object = MibScalar
qtechNotifyPeerIp = _QtechNotifyPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 115, 2, 1, 2),
    _QtechNotifyPeerIp_Type()
)
qtechNotifyPeerIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyPeerIp.setStatus("current")


class _QtechNotifyCtxId_Type(Integer32):
    """Custom type qtechNotifyCtxId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechNotifyCtxId_Type.__name__ = "Integer32"
_QtechNotifyCtxId_Object = MibScalar
qtechNotifyCtxId = _QtechNotifyCtxId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 115, 2, 1, 3),
    _QtechNotifyCtxId_Type()
)
qtechNotifyCtxId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyCtxId.setStatus("current")


class _QtechNotifyOldState_Type(Integer32):
    """Custom type qtechNotifyOldState based on Integer32"""
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
        *(("disable", 0),
          ("unknown", 1),
          ("single-active", 2),
          ("single-standby", 3),
          ("pair-active", 4),
          ("pair-standby", 5))
    )


_QtechNotifyOldState_Type.__name__ = "Integer32"
_QtechNotifyOldState_Object = MibScalar
qtechNotifyOldState = _QtechNotifyOldState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 115, 2, 1, 4),
    _QtechNotifyOldState_Type()
)
qtechNotifyOldState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyOldState.setStatus("current")


class _QtechNotifyNewState_Type(Integer32):
    """Custom type qtechNotifyNewState based on Integer32"""
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
        *(("disable", 0),
          ("unknown", 1),
          ("single-active", 2),
          ("single-standby", 3),
          ("pair-active", 4),
          ("pair-standby", 5))
    )


_QtechNotifyNewState_Type.__name__ = "Integer32"
_QtechNotifyNewState_Object = MibScalar
qtechNotifyNewState = _QtechNotifyNewState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 115, 2, 1, 5),
    _QtechNotifyNewState_Type()
)
qtechNotifyNewState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechNotifyNewState.setStatus("current")
_QtechWlanHotbackupNotifications_ObjectIdentity = ObjectIdentity
qtechWlanHotbackupNotifications = _QtechWlanHotbackupNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 115, 2, 2)
)

# Managed Objects groups


# Notification objects

qtechNotifyWlanHBChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 115, 2, 2, 1)
)
qtechNotifyWlanHBChange.setObjects(
      *(("QTECH-WLAN-HOTBACKUP-MIB", "qtechNotifyPeerIpType"),
        ("QTECH-WLAN-HOTBACKUP-MIB", "qtechNotifyPeerIp"),
        ("QTECH-WLAN-HOTBACKUP-MIB", "qtechNotifyCtxId"),
        ("QTECH-WLAN-HOTBACKUP-MIB", "qtechNotifyOldState"),
        ("QTECH-WLAN-HOTBACKUP-MIB", "qtechNotifyNewState"))
)
if mibBuilder.loadTexts:
    qtechNotifyWlanHBChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-WLAN-HOTBACKUP-MIB",
    **{"qtechWlanHotbackupMIB": qtechWlanHotbackupMIB,
       "qtechWlanHotbackupMIBObjects": qtechWlanHotbackupMIBObjects,
       "qtechWlanHotbackupPeerTable": qtechWlanHotbackupPeerTable,
       "qtechWlanHotbackupPeerEntry": qtechWlanHotbackupPeerEntry,
       "qtechWlanHotbackupIpAddress": qtechWlanHotbackupIpAddress,
       "qtechWlanHotbackupIsEnabled": qtechWlanHotbackupIsEnabled,
       "qtechWlanHotbackupState": qtechWlanHotbackupState,
       "qtechWlanHotbackupContextTable": qtechWlanHotbackupContextTable,
       "qtechWlanHotbackupContextEntry": qtechWlanHotbackupContextEntry,
       "qtechWlanHotbackupCtxIpAddress": qtechWlanHotbackupCtxIpAddress,
       "qtechWlanHotbackupContextId": qtechWlanHotbackupContextId,
       "qtechWlanHotbackupContextState": qtechWlanHotbackupContextState,
       "qtechWlanHotbackupNotificationsMIBObjects": qtechWlanHotbackupNotificationsMIBObjects,
       "qtechWlanHotbackupNtfObjects": qtechWlanHotbackupNtfObjects,
       "qtechNotifyPeerIpType": qtechNotifyPeerIpType,
       "qtechNotifyPeerIp": qtechNotifyPeerIp,
       "qtechNotifyCtxId": qtechNotifyCtxId,
       "qtechNotifyOldState": qtechNotifyOldState,
       "qtechNotifyNewState": qtechNotifyNewState,
       "qtechWlanHotbackupNotifications": qtechWlanHotbackupNotifications,
       "qtechNotifyWlanHBChange": qtechNotifyWlanHBChange}
)
