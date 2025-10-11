# SNMP MIB module (FS-WLAN-HOTBACKUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-WLAN-HOTBACKUP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:27 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

fsWlanHotbackupMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 115)
)
if mibBuilder.loadTexts:
    fsWlanHotbackupMIB.setRevisions(
        ("2012-07-31 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsWlanHotbackupMIBObjects_ObjectIdentity = ObjectIdentity
fsWlanHotbackupMIBObjects = _FsWlanHotbackupMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 115, 1)
)
_FsWlanHotbackupPeerTable_Object = MibTable
fsWlanHotbackupPeerTable = _FsWlanHotbackupPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 115, 1, 1)
)
if mibBuilder.loadTexts:
    fsWlanHotbackupPeerTable.setStatus("current")
_FsWlanHotbackupPeerEntry_Object = MibTableRow
fsWlanHotbackupPeerEntry = _FsWlanHotbackupPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 115, 1, 1, 1)
)
fsWlanHotbackupPeerEntry.setIndexNames(
    (0, "FS-WLAN-HOTBACKUP-MIB", "fsWlanHotbackupIpAddress"),
)
if mibBuilder.loadTexts:
    fsWlanHotbackupPeerEntry.setStatus("current")
_FsWlanHotbackupIpAddress_Type = IpAddress
_FsWlanHotbackupIpAddress_Object = MibTableColumn
fsWlanHotbackupIpAddress = _FsWlanHotbackupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 115, 1, 1, 1, 1),
    _FsWlanHotbackupIpAddress_Type()
)
fsWlanHotbackupIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsWlanHotbackupIpAddress.setStatus("current")


class _FsWlanHotbackupIsEnabled_Type(Integer32):
    """Custom type fsWlanHotbackupIsEnabled based on Integer32"""
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


_FsWlanHotbackupIsEnabled_Type.__name__ = "Integer32"
_FsWlanHotbackupIsEnabled_Object = MibTableColumn
fsWlanHotbackupIsEnabled = _FsWlanHotbackupIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 115, 1, 1, 1, 2),
    _FsWlanHotbackupIsEnabled_Type()
)
fsWlanHotbackupIsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWlanHotbackupIsEnabled.setStatus("current")


class _FsWlanHotbackupState_Type(Integer32):
    """Custom type fsWlanHotbackupState based on Integer32"""
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


_FsWlanHotbackupState_Type.__name__ = "Integer32"
_FsWlanHotbackupState_Object = MibTableColumn
fsWlanHotbackupState = _FsWlanHotbackupState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 115, 1, 1, 1, 3),
    _FsWlanHotbackupState_Type()
)
fsWlanHotbackupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWlanHotbackupState.setStatus("current")
_FsWlanHotbackupContextTable_Object = MibTable
fsWlanHotbackupContextTable = _FsWlanHotbackupContextTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 115, 1, 2)
)
if mibBuilder.loadTexts:
    fsWlanHotbackupContextTable.setStatus("current")
_FsWlanHotbackupContextEntry_Object = MibTableRow
fsWlanHotbackupContextEntry = _FsWlanHotbackupContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 115, 1, 2, 1)
)
fsWlanHotbackupContextEntry.setIndexNames(
    (0, "FS-WLAN-HOTBACKUP-MIB", "fsWlanHotbackupCtxIpAddress"),
    (0, "FS-WLAN-HOTBACKUP-MIB", "fsWlanHotbackupContextId"),
)
if mibBuilder.loadTexts:
    fsWlanHotbackupContextEntry.setStatus("current")
_FsWlanHotbackupCtxIpAddress_Type = IpAddress
_FsWlanHotbackupCtxIpAddress_Object = MibTableColumn
fsWlanHotbackupCtxIpAddress = _FsWlanHotbackupCtxIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 115, 1, 2, 1, 1),
    _FsWlanHotbackupCtxIpAddress_Type()
)
fsWlanHotbackupCtxIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWlanHotbackupCtxIpAddress.setStatus("current")
_FsWlanHotbackupContextId_Type = Integer32
_FsWlanHotbackupContextId_Object = MibTableColumn
fsWlanHotbackupContextId = _FsWlanHotbackupContextId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 115, 1, 2, 1, 2),
    _FsWlanHotbackupContextId_Type()
)
fsWlanHotbackupContextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWlanHotbackupContextId.setStatus("current")


class _FsWlanHotbackupContextState_Type(Integer32):
    """Custom type fsWlanHotbackupContextState based on Integer32"""
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


_FsWlanHotbackupContextState_Type.__name__ = "Integer32"
_FsWlanHotbackupContextState_Object = MibTableColumn
fsWlanHotbackupContextState = _FsWlanHotbackupContextState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 115, 1, 2, 1, 3),
    _FsWlanHotbackupContextState_Type()
)
fsWlanHotbackupContextState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWlanHotbackupContextState.setStatus("current")
_FsWlanHotbackupNotificationsMIBObjects_ObjectIdentity = ObjectIdentity
fsWlanHotbackupNotificationsMIBObjects = _FsWlanHotbackupNotificationsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 115, 2)
)
_FsWlanHotbackupNtfObjects_ObjectIdentity = ObjectIdentity
fsWlanHotbackupNtfObjects = _FsWlanHotbackupNtfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 115, 2, 1)
)
_FsNotifyPeerIpType_Type = InetAddressType
_FsNotifyPeerIpType_Object = MibScalar
fsNotifyPeerIpType = _FsNotifyPeerIpType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 115, 2, 1, 1),
    _FsNotifyPeerIpType_Type()
)
fsNotifyPeerIpType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsNotifyPeerIpType.setStatus("current")
_FsNotifyPeerIp_Type = InetAddress
_FsNotifyPeerIp_Object = MibScalar
fsNotifyPeerIp = _FsNotifyPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 115, 2, 1, 2),
    _FsNotifyPeerIp_Type()
)
fsNotifyPeerIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsNotifyPeerIp.setStatus("current")


class _FsNotifyCtxId_Type(Integer32):
    """Custom type fsNotifyCtxId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsNotifyCtxId_Type.__name__ = "Integer32"
_FsNotifyCtxId_Object = MibScalar
fsNotifyCtxId = _FsNotifyCtxId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 115, 2, 1, 3),
    _FsNotifyCtxId_Type()
)
fsNotifyCtxId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsNotifyCtxId.setStatus("current")


class _FsNotifyOldState_Type(Integer32):
    """Custom type fsNotifyOldState based on Integer32"""
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


_FsNotifyOldState_Type.__name__ = "Integer32"
_FsNotifyOldState_Object = MibScalar
fsNotifyOldState = _FsNotifyOldState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 115, 2, 1, 4),
    _FsNotifyOldState_Type()
)
fsNotifyOldState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsNotifyOldState.setStatus("current")


class _FsNotifyNewState_Type(Integer32):
    """Custom type fsNotifyNewState based on Integer32"""
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


_FsNotifyNewState_Type.__name__ = "Integer32"
_FsNotifyNewState_Object = MibScalar
fsNotifyNewState = _FsNotifyNewState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 115, 2, 1, 5),
    _FsNotifyNewState_Type()
)
fsNotifyNewState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsNotifyNewState.setStatus("current")
_FsWlanHotbackupNotifications_ObjectIdentity = ObjectIdentity
fsWlanHotbackupNotifications = _FsWlanHotbackupNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 115, 2, 2)
)

# Managed Objects groups


# Notification objects

fsNotifyWlanHBChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 115, 2, 2, 1)
)
fsNotifyWlanHBChange.setObjects(
      *(("FS-WLAN-HOTBACKUP-MIB", "fsNotifyPeerIpType"),
        ("FS-WLAN-HOTBACKUP-MIB", "fsNotifyPeerIp"),
        ("FS-WLAN-HOTBACKUP-MIB", "fsNotifyCtxId"),
        ("FS-WLAN-HOTBACKUP-MIB", "fsNotifyOldState"),
        ("FS-WLAN-HOTBACKUP-MIB", "fsNotifyNewState"))
)
if mibBuilder.loadTexts:
    fsNotifyWlanHBChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-WLAN-HOTBACKUP-MIB",
    **{"fsWlanHotbackupMIB": fsWlanHotbackupMIB,
       "fsWlanHotbackupMIBObjects": fsWlanHotbackupMIBObjects,
       "fsWlanHotbackupPeerTable": fsWlanHotbackupPeerTable,
       "fsWlanHotbackupPeerEntry": fsWlanHotbackupPeerEntry,
       "fsWlanHotbackupIpAddress": fsWlanHotbackupIpAddress,
       "fsWlanHotbackupIsEnabled": fsWlanHotbackupIsEnabled,
       "fsWlanHotbackupState": fsWlanHotbackupState,
       "fsWlanHotbackupContextTable": fsWlanHotbackupContextTable,
       "fsWlanHotbackupContextEntry": fsWlanHotbackupContextEntry,
       "fsWlanHotbackupCtxIpAddress": fsWlanHotbackupCtxIpAddress,
       "fsWlanHotbackupContextId": fsWlanHotbackupContextId,
       "fsWlanHotbackupContextState": fsWlanHotbackupContextState,
       "fsWlanHotbackupNotificationsMIBObjects": fsWlanHotbackupNotificationsMIBObjects,
       "fsWlanHotbackupNtfObjects": fsWlanHotbackupNtfObjects,
       "fsNotifyPeerIpType": fsNotifyPeerIpType,
       "fsNotifyPeerIp": fsNotifyPeerIp,
       "fsNotifyCtxId": fsNotifyCtxId,
       "fsNotifyOldState": fsNotifyOldState,
       "fsNotifyNewState": fsNotifyNewState,
       "fsWlanHotbackupNotifications": fsWlanHotbackupNotifications,
       "fsNotifyWlanHBChange": fsNotifyWlanHBChange}
)
