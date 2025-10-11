# SNMP MIB module (BAY-STACK-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/BAY-STACK-NTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:21:07 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackNtpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 49)
)
if mibBuilder.loadTexts:
    bayStackNtpMib.setRevisions(
        ("2018-09-27 00:00",
         "2017-07-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BsNtpNotifications_ObjectIdentity = ObjectIdentity
bsNtpNotifications = _BsNtpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 49, 0)
)
_BsNtpObjects_ObjectIdentity = ObjectIdentity
bsNtpObjects = _BsNtpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 49, 1)
)
_BsNtpGlobal_ObjectIdentity = ObjectIdentity
bsNtpGlobal = _BsNtpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 49, 1, 1)
)


class _BsNtpGlobalEnable_Type(TruthValue):
    """Custom type bsNtpGlobalEnable based on TruthValue"""
    defaultValue = 2


_BsNtpGlobalEnable_Type.__name__ = "TruthValue"
_BsNtpGlobalEnable_Object = MibScalar
bsNtpGlobalEnable = _BsNtpGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 49, 1, 1, 1),
    _BsNtpGlobalEnable_Type()
)
bsNtpGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsNtpGlobalEnable.setStatus("current")
_BsNtpServerTable_Object = MibTable
bsNtpServerTable = _BsNtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 49, 1, 2)
)
if mibBuilder.loadTexts:
    bsNtpServerTable.setStatus("current")
_BsNtpServerEntry_Object = MibTableRow
bsNtpServerEntry = _BsNtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 49, 1, 2, 1)
)
bsNtpServerEntry.setIndexNames(
    (0, "BAY-STACK-NTP-MIB", "bsNtpServerAddressType"),
    (0, "BAY-STACK-NTP-MIB", "bsNtpServerAddress"),
)
if mibBuilder.loadTexts:
    bsNtpServerEntry.setStatus("current")
_BsNtpServerAddressType_Type = InetAddressType
_BsNtpServerAddressType_Object = MibTableColumn
bsNtpServerAddressType = _BsNtpServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 49, 1, 2, 1, 1),
    _BsNtpServerAddressType_Type()
)
bsNtpServerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsNtpServerAddressType.setStatus("current")
_BsNtpServerAddress_Type = InetAddress
_BsNtpServerAddress_Object = MibTableColumn
bsNtpServerAddress = _BsNtpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 49, 1, 2, 1, 2),
    _BsNtpServerAddress_Type()
)
bsNtpServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsNtpServerAddress.setStatus("current")


class _BsNtpServerEnable_Type(TruthValue):
    """Custom type bsNtpServerEnable based on TruthValue"""
    defaultValue = 1


_BsNtpServerEnable_Type.__name__ = "TruthValue"
_BsNtpServerEnable_Object = MibTableColumn
bsNtpServerEnable = _BsNtpServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 49, 1, 2, 1, 3),
    _BsNtpServerEnable_Type()
)
bsNtpServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsNtpServerEnable.setStatus("current")


class _BsNtpServerAuthEnable_Type(TruthValue):
    """Custom type bsNtpServerAuthEnable based on TruthValue"""
    defaultValue = 2


_BsNtpServerAuthEnable_Type.__name__ = "TruthValue"
_BsNtpServerAuthEnable_Object = MibTableColumn
bsNtpServerAuthEnable = _BsNtpServerAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 49, 1, 2, 1, 4),
    _BsNtpServerAuthEnable_Type()
)
bsNtpServerAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsNtpServerAuthEnable.setStatus("current")


class _BsNtpServerKeyId_Type(Integer32):
    """Custom type bsNtpServerKeyId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BsNtpServerKeyId_Type.__name__ = "Integer32"
_BsNtpServerKeyId_Object = MibTableColumn
bsNtpServerKeyId = _BsNtpServerKeyId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 49, 1, 2, 1, 5),
    _BsNtpServerKeyId_Type()
)
bsNtpServerKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsNtpServerKeyId.setStatus("current")


class _BsNtpServerAutokeyEnable_Type(TruthValue):
    """Custom type bsNtpServerAutokeyEnable based on TruthValue"""
    defaultValue = 2


_BsNtpServerAutokeyEnable_Type.__name__ = "TruthValue"
_BsNtpServerAutokeyEnable_Object = MibTableColumn
bsNtpServerAutokeyEnable = _BsNtpServerAutokeyEnable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 49, 1, 2, 1, 6),
    _BsNtpServerAutokeyEnable_Type()
)
bsNtpServerAutokeyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsNtpServerAutokeyEnable.setStatus("current")
_BsNtpServerVersion_Type = Unsigned32
_BsNtpServerVersion_Object = MibTableColumn
bsNtpServerVersion = _BsNtpServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 49, 1, 2, 1, 7),
    _BsNtpServerVersion_Type()
)
bsNtpServerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsNtpServerVersion.setStatus("current")
_BsNtpServerStratum_Type = Unsigned32
_BsNtpServerStratum_Object = MibTableColumn
bsNtpServerStratum = _BsNtpServerStratum_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 49, 1, 2, 1, 8),
    _BsNtpServerStratum_Type()
)
bsNtpServerStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsNtpServerStratum.setStatus("current")


class _BsNtpServerRootDelay_Type(DisplayString):
    """Custom type bsNtpServerRootDelay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BsNtpServerRootDelay_Type.__name__ = "DisplayString"
_BsNtpServerRootDelay_Object = MibTableColumn
bsNtpServerRootDelay = _BsNtpServerRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 49, 1, 2, 1, 9),
    _BsNtpServerRootDelay_Type()
)
bsNtpServerRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsNtpServerRootDelay.setStatus("current")
_BsNtpServerPrecision_Type = Integer32
_BsNtpServerPrecision_Object = MibTableColumn
bsNtpServerPrecision = _BsNtpServerPrecision_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 49, 1, 2, 1, 10),
    _BsNtpServerPrecision_Type()
)
bsNtpServerPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsNtpServerPrecision.setStatus("current")


class _BsNtpServerReachable_Type(DisplayString):
    """Custom type bsNtpServerReachable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BsNtpServerReachable_Type.__name__ = "DisplayString"
_BsNtpServerReachable_Object = MibTableColumn
bsNtpServerReachable = _BsNtpServerReachable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 49, 1, 2, 1, 11),
    _BsNtpServerReachable_Type()
)
bsNtpServerReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsNtpServerReachable.setStatus("current")


class _BsNtpServerSynchronized_Type(DisplayString):
    """Custom type bsNtpServerSynchronized based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BsNtpServerSynchronized_Type.__name__ = "DisplayString"
_BsNtpServerSynchronized_Object = MibTableColumn
bsNtpServerSynchronized = _BsNtpServerSynchronized_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 49, 1, 2, 1, 12),
    _BsNtpServerSynchronized_Type()
)
bsNtpServerSynchronized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsNtpServerSynchronized.setStatus("current")
_BsNtpServerPckSent_Type = Counter32
_BsNtpServerPckSent_Object = MibTableColumn
bsNtpServerPckSent = _BsNtpServerPckSent_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 49, 1, 2, 1, 13),
    _BsNtpServerPckSent_Type()
)
bsNtpServerPckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsNtpServerPckSent.setStatus("current")
_BsNtpServerPckProcessed_Type = Counter32
_BsNtpServerPckProcessed_Object = MibTableColumn
bsNtpServerPckProcessed = _BsNtpServerPckProcessed_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 49, 1, 2, 1, 14),
    _BsNtpServerPckProcessed_Type()
)
bsNtpServerPckProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsNtpServerPckProcessed.setStatus("current")
_BsNtpServerPckDiscarded_Type = Counter32
_BsNtpServerPckDiscarded_Object = MibTableColumn
bsNtpServerPckDiscarded = _BsNtpServerPckDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 49, 1, 2, 1, 15),
    _BsNtpServerPckDiscarded_Type()
)
bsNtpServerPckDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsNtpServerPckDiscarded.setStatus("current")
_BsNtpServerRowStatus_Type = RowStatus
_BsNtpServerRowStatus_Object = MibTableColumn
bsNtpServerRowStatus = _BsNtpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 49, 1, 2, 1, 16),
    _BsNtpServerRowStatus_Type()
)
bsNtpServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsNtpServerRowStatus.setStatus("current")
_BsNtpKeyTable_Object = MibTable
bsNtpKeyTable = _BsNtpKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 49, 1, 3)
)
if mibBuilder.loadTexts:
    bsNtpKeyTable.setStatus("current")
_BsNtpKeyEntry_Object = MibTableRow
bsNtpKeyEntry = _BsNtpKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 49, 1, 3, 1)
)
bsNtpKeyEntry.setIndexNames(
    (0, "BAY-STACK-NTP-MIB", "bsNtpKeyId"),
)
if mibBuilder.loadTexts:
    bsNtpKeyEntry.setStatus("current")


class _BsNtpKeyId_Type(Integer32):
    """Custom type bsNtpKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BsNtpKeyId_Type.__name__ = "Integer32"
_BsNtpKeyId_Object = MibTableColumn
bsNtpKeyId = _BsNtpKeyId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 49, 1, 3, 1, 1),
    _BsNtpKeyId_Type()
)
bsNtpKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsNtpKeyId.setStatus("current")


class _BsNtpKeyType_Type(Integer32):
    """Custom type bsNtpKeyType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha1", 2))
    )


_BsNtpKeyType_Type.__name__ = "Integer32"
_BsNtpKeyType_Object = MibTableColumn
bsNtpKeyType = _BsNtpKeyType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 49, 1, 3, 1, 2),
    _BsNtpKeyType_Type()
)
bsNtpKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsNtpKeyType.setStatus("current")


class _BsNtpKeySecret_Type(DisplayString):
    """Custom type bsNtpKeySecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BsNtpKeySecret_Type.__name__ = "DisplayString"
_BsNtpKeySecret_Object = MibTableColumn
bsNtpKeySecret = _BsNtpKeySecret_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 49, 1, 3, 1, 3),
    _BsNtpKeySecret_Type()
)
bsNtpKeySecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsNtpKeySecret.setStatus("current")
_BsNtpKeyRowStatus_Type = RowStatus
_BsNtpKeyRowStatus_Object = MibTableColumn
bsNtpKeyRowStatus = _BsNtpKeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 49, 1, 3, 1, 4),
    _BsNtpKeyRowStatus_Type()
)
bsNtpKeyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsNtpKeyRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-NTP-MIB",
    **{"bayStackNtpMib": bayStackNtpMib,
       "bsNtpNotifications": bsNtpNotifications,
       "bsNtpObjects": bsNtpObjects,
       "bsNtpGlobal": bsNtpGlobal,
       "bsNtpGlobalEnable": bsNtpGlobalEnable,
       "bsNtpServerTable": bsNtpServerTable,
       "bsNtpServerEntry": bsNtpServerEntry,
       "bsNtpServerAddressType": bsNtpServerAddressType,
       "bsNtpServerAddress": bsNtpServerAddress,
       "bsNtpServerEnable": bsNtpServerEnable,
       "bsNtpServerAuthEnable": bsNtpServerAuthEnable,
       "bsNtpServerKeyId": bsNtpServerKeyId,
       "bsNtpServerAutokeyEnable": bsNtpServerAutokeyEnable,
       "bsNtpServerVersion": bsNtpServerVersion,
       "bsNtpServerStratum": bsNtpServerStratum,
       "bsNtpServerRootDelay": bsNtpServerRootDelay,
       "bsNtpServerPrecision": bsNtpServerPrecision,
       "bsNtpServerReachable": bsNtpServerReachable,
       "bsNtpServerSynchronized": bsNtpServerSynchronized,
       "bsNtpServerPckSent": bsNtpServerPckSent,
       "bsNtpServerPckProcessed": bsNtpServerPckProcessed,
       "bsNtpServerPckDiscarded": bsNtpServerPckDiscarded,
       "bsNtpServerRowStatus": bsNtpServerRowStatus,
       "bsNtpKeyTable": bsNtpKeyTable,
       "bsNtpKeyEntry": bsNtpKeyEntry,
       "bsNtpKeyId": bsNtpKeyId,
       "bsNtpKeyType": bsNtpKeyType,
       "bsNtpKeySecret": bsNtpKeySecret,
       "bsNtpKeyRowStatus": bsNtpKeyRowStatus}
)
