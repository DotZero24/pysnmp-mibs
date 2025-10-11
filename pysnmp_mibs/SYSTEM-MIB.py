# SNMP MIB module (SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/SYSTEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:20:05 2025
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

(ntEnterpriseDataTasmanMgmt,) = mibBuilder.importSymbols(
    "NT-ENTERPRISE-DATA-MIB",
    "ntEnterpriseDataTasmanMgmt")

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


# MODULE-IDENTITY

nnsystemMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    nnsystemMib.setRevisions(
        ("1900-08-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SntpEnabled(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-enabled", 1),
          ("enabled", 2))
    )



# MIB Managed Objects in the order of their OIDs

_NnsystemObjects_ObjectIdentity = ObjectIdentity
nnsystemObjects = _NnsystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 1)
)
_NnsysIpAddr_Type = IpAddress
_NnsysIpAddr_Object = MibScalar
nnsysIpAddr = _NnsysIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 1, 1),
    _NnsysIpAddr_Type()
)
nnsysIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnsysIpAddr.setStatus("current")
_NnsysNetMask_Type = IpAddress
_NnsysNetMask_Object = MibScalar
nnsysNetMask = _NnsysNetMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 1, 2),
    _NnsysNetMask_Type()
)
nnsysNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnsysNetMask.setStatus("current")
_NnsysBroadcast_Type = IpAddress
_NnsysBroadcast_Object = MibScalar
nnsysBroadcast = _NnsysBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 1, 3),
    _NnsysBroadcast_Type()
)
nnsysBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnsysBroadcast.setStatus("current")


class _NnsysVersion_Type(DisplayString):
    """Custom type nnsysVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NnsysVersion_Type.__name__ = "DisplayString"
_NnsysVersion_Object = MibScalar
nnsysVersion = _NnsysVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 1, 4),
    _NnsysVersion_Type()
)
nnsysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnsysVersion.setStatus("current")


class _NnsysHostName_Type(DisplayString):
    """Custom type nnsysHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NnsysHostName_Type.__name__ = "DisplayString"
_NnsysHostName_Object = MibScalar
nnsysHostName = _NnsysHostName_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 1, 6),
    _NnsysHostName_Type()
)
nnsysHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnsysHostName.setStatus("current")


class _NnsysDomainName_Type(DisplayString):
    """Custom type nnsysDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NnsysDomainName_Type.__name__ = "DisplayString"
_NnsysDomainName_Object = MibScalar
nnsysDomainName = _NnsysDomainName_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 1, 7),
    _NnsysDomainName_Type()
)
nnsysDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnsysDomainName.setStatus("current")


class _NnsysAlarmStatus_Type(Integer32):
    """Custom type nnsysAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("minor", 2),
          ("major", 3))
    )


_NnsysAlarmStatus_Type.__name__ = "Integer32"
_NnsysAlarmStatus_Object = MibScalar
nnsysAlarmStatus = _NnsysAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 1, 8),
    _NnsysAlarmStatus_Type()
)
nnsysAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnsysAlarmStatus.setStatus("current")


class _NnsysReset_Type(Integer32):
    """Custom type nnsysReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_NnsysReset_Type.__name__ = "Integer32"
_NnsysReset_Object = MibScalar
nnsysReset = _NnsysReset_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 1, 10),
    _NnsysReset_Type()
)
nnsysReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnsysReset.setStatus("current")


class _NnsysDateTime_Type(OctetString):
    """Custom type nnsysDateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_NnsysDateTime_Type.__name__ = "OctetString"
_NnsysDateTime_Object = MibScalar
nnsysDateTime = _NnsysDateTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 1, 11),
    _NnsysDateTime_Type()
)
nnsysDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnsysDateTime.setStatus("current")
_NnarpClearAtTable_Type = Integer32
_NnarpClearAtTable_Object = MibScalar
nnarpClearAtTable = _NnarpClearAtTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 1, 12),
    _NnarpClearAtTable_Type()
)
nnarpClearAtTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnarpClearAtTable.setStatus("current")
_NnipClearRouteTable_Type = Integer32
_NnipClearRouteTable_Object = MibScalar
nnipClearRouteTable = _NnipClearRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 1, 13),
    _NnipClearRouteTable_Type()
)
nnipClearRouteTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnipClearRouteTable.setStatus("current")


class _NnarpTimeOut_Type(Integer32):
    """Custom type nnarpTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 28800),
    )


_NnarpTimeOut_Type.__name__ = "Integer32"
_NnarpTimeOut_Object = MibScalar
nnarpTimeOut = _NnarpTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 1, 14),
    _NnarpTimeOut_Type()
)
nnarpTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnarpTimeOut.setStatus("current")
_NndnsGroup_ObjectIdentity = ObjectIdentity
nndnsGroup = _NndnsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 2)
)


class _NndnsEnable_Type(Integer32):
    """Custom type nndnsEnable based on Integer32"""
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


_NndnsEnable_Type.__name__ = "Integer32"
_NndnsEnable_Object = MibScalar
nndnsEnable = _NndnsEnable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 2, 1),
    _NndnsEnable_Type()
)
nndnsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndnsEnable.setStatus("current")
_NndnsServerTable_Object = MibTable
nndnsServerTable = _NndnsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    nndnsServerTable.setStatus("current")
_NndnsServerEntry_Object = MibTableRow
nndnsServerEntry = _NndnsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 2, 2, 1)
)
nndnsServerEntry.setIndexNames(
    (0, "SYSTEM-MIB", "nndnsServerAddr"),
)
if mibBuilder.loadTexts:
    nndnsServerEntry.setStatus("current")


class _NndnsServerEntryType_Type(Integer32):
    """Custom type nndnsServerEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("primary", 2),
          ("other", 3))
    )


_NndnsServerEntryType_Type.__name__ = "Integer32"
_NndnsServerEntryType_Object = MibTableColumn
nndnsServerEntryType = _NndnsServerEntryType_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 2, 2, 1, 1),
    _NndnsServerEntryType_Type()
)
nndnsServerEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndnsServerEntryType.setStatus("current")
_NndnsServerAddr_Type = IpAddress
_NndnsServerAddr_Object = MibTableColumn
nndnsServerAddr = _NndnsServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 2, 2, 1, 2),
    _NndnsServerAddr_Type()
)
nndnsServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nndnsServerAddr.setStatus("current")
_NnsystemEnableNotification_ObjectIdentity = ObjectIdentity
nnsystemEnableNotification = _NnsystemEnableNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 3)
)


class _NnenableSysShutDownNotification_Type(TruthValue):
    """Custom type nnenableSysShutDownNotification based on TruthValue"""
    defaultValue = 1


_NnenableSysShutDownNotification_Type.__name__ = "TruthValue"
_NnenableSysShutDownNotification_Object = MibScalar
nnenableSysShutDownNotification = _NnenableSysShutDownNotification_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 3, 1),
    _NnenableSysShutDownNotification_Type()
)
nnenableSysShutDownNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnenableSysShutDownNotification.setStatus("current")


class _NnenableUserLoginNotification_Type(TruthValue):
    """Custom type nnenableUserLoginNotification based on TruthValue"""
    defaultValue = 1


_NnenableUserLoginNotification_Type.__name__ = "TruthValue"
_NnenableUserLoginNotification_Object = MibScalar
nnenableUserLoginNotification = _NnenableUserLoginNotification_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 3, 2),
    _NnenableUserLoginNotification_Type()
)
nnenableUserLoginNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnenableUserLoginNotification.setStatus("current")


class _NnenableUserLogOffNotification_Type(TruthValue):
    """Custom type nnenableUserLogOffNotification based on TruthValue"""
    defaultValue = 1


_NnenableUserLogOffNotification_Type.__name__ = "TruthValue"
_NnenableUserLogOffNotification_Object = MibScalar
nnenableUserLogOffNotification = _NnenableUserLogOffNotification_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 3, 3),
    _NnenableUserLogOffNotification_Type()
)
nnenableUserLogOffNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnenableUserLogOffNotification.setStatus("current")


class _NnenableUserLoginFailNotification_Type(TruthValue):
    """Custom type nnenableUserLoginFailNotification based on TruthValue"""
    defaultValue = 1


_NnenableUserLoginFailNotification_Type.__name__ = "TruthValue"
_NnenableUserLoginFailNotification_Object = MibScalar
nnenableUserLoginFailNotification = _NnenableUserLoginFailNotification_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 3, 4),
    _NnenableUserLoginFailNotification_Type()
)
nnenableUserLoginFailNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnenableUserLoginFailNotification.setStatus("current")


class _NnenableAuthenticationLoginFailNotification_Type(TruthValue):
    """Custom type nnenableAuthenticationLoginFailNotification based on TruthValue"""
    defaultValue = 1


_NnenableAuthenticationLoginFailNotification_Type.__name__ = "TruthValue"
_NnenableAuthenticationLoginFailNotification_Object = MibScalar
nnenableAuthenticationLoginFailNotification = _NnenableAuthenticationLoginFailNotification_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 3, 5),
    _NnenableAuthenticationLoginFailNotification_Type()
)
nnenableAuthenticationLoginFailNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnenableAuthenticationLoginFailNotification.setStatus("current")


class _NnenableAuthenticationLoginSuccessNotification_Type(TruthValue):
    """Custom type nnenableAuthenticationLoginSuccessNotification based on TruthValue"""
    defaultValue = 1


_NnenableAuthenticationLoginSuccessNotification_Type.__name__ = "TruthValue"
_NnenableAuthenticationLoginSuccessNotification_Object = MibScalar
nnenableAuthenticationLoginSuccessNotification = _NnenableAuthenticationLoginSuccessNotification_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 3, 6),
    _NnenableAuthenticationLoginSuccessNotification_Type()
)
nnenableAuthenticationLoginSuccessNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnenableAuthenticationLoginSuccessNotification.setStatus("current")


class _NnenableLogoutNotification_Type(TruthValue):
    """Custom type nnenableLogoutNotification based on TruthValue"""
    defaultValue = 1


_NnenableLogoutNotification_Type.__name__ = "TruthValue"
_NnenableLogoutNotification_Object = MibScalar
nnenableLogoutNotification = _NnenableLogoutNotification_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 3, 7),
    _NnenableLogoutNotification_Type()
)
nnenableLogoutNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnenableLogoutNotification.setStatus("current")
_NnsystemNotifications_ObjectIdentity = ObjectIdentity
nnsystemNotifications = _NnsystemNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 4)
)
_NnsystemTraps_ObjectIdentity = ObjectIdentity
nnsystemTraps = _NnsystemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 4, 0)
)
_NnuserAdminGroup_ObjectIdentity = ObjectIdentity
nnuserAdminGroup = _NnuserAdminGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 5)
)


class _NnuserName_Type(DisplayString):
    """Custom type nnuserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NnuserName_Type.__name__ = "DisplayString"
_NnuserName_Object = MibScalar
nnuserName = _NnuserName_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 5, 1),
    _NnuserName_Type()
)
nnuserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nnuserName.setStatus("current")
_NnsntpGroup_ObjectIdentity = ObjectIdentity
nnsntpGroup = _NnsntpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 10)
)


class _NnsntpClieenabled_Type(SntpEnabled):
    """Custom type nnsntpClieenabled based on SntpEnabled"""
    defaultValue = 1


_NnsntpClieenabled_Type.__name__ = "SntpEnabled"
_NnsntpClieenabled_Object = MibScalar
nnsntpClieenabled = _NnsntpClieenabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 10, 1),
    _NnsntpClieenabled_Type()
)
nnsntpClieenabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnsntpClieenabled.setStatus("current")


class _NnsntpServerAddr_Type(DisplayString):
    """Custom type nnsntpServerAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NnsntpServerAddr_Type.__name__ = "DisplayString"
_NnsntpServerAddr_Object = MibScalar
nnsntpServerAddr = _NnsntpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 10, 2),
    _NnsntpServerAddr_Type()
)
nnsntpServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnsntpServerAddr.setStatus("current")


class _NnsntpTimeout_Type(Integer32):
    """Custom type nnsntpTimeout based on Integer32"""
    defaultValue = 1024


_NnsntpTimeout_Type.__name__ = "Integer32"
_NnsntpTimeout_Object = MibScalar
nnsntpTimeout = _NnsntpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 10, 3),
    _NnsntpTimeout_Type()
)
nnsntpTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnsntpTimeout.setStatus("current")
_NnsntpNotificationEnables_ObjectIdentity = ObjectIdentity
nnsntpNotificationEnables = _NnsntpNotificationEnables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 11)
)


class _NnenableSntpNotification_Type(TruthValue):
    """Custom type nnenableSntpNotification based on TruthValue"""
    defaultValue = 1


_NnenableSntpNotification_Type.__name__ = "TruthValue"
_NnenableSntpNotification_Object = MibScalar
nnenableSntpNotification = _NnenableSntpNotification_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 11, 1),
    _NnenableSntpNotification_Type()
)
nnenableSntpNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnenableSntpNotification.setStatus("current")
_NnsntpNotifications_ObjectIdentity = ObjectIdentity
nnsntpNotifications = _NnsntpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 12)
)
_NnsntpTraps_ObjectIdentity = ObjectIdentity
nnsntpTraps = _NnsntpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 12, 0)
)
_NnenableBgpNotifications_ObjectIdentity = ObjectIdentity
nnenableBgpNotifications = _NnenableBgpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 14)
)


class _NnenableBgpEstablishedNotification_Type(TruthValue):
    """Custom type nnenableBgpEstablishedNotification based on TruthValue"""
    defaultValue = 1


_NnenableBgpEstablishedNotification_Type.__name__ = "TruthValue"
_NnenableBgpEstablishedNotification_Object = MibScalar
nnenableBgpEstablishedNotification = _NnenableBgpEstablishedNotification_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 14, 1),
    _NnenableBgpEstablishedNotification_Type()
)
nnenableBgpEstablishedNotification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnenableBgpEstablishedNotification.setStatus("current")


class _NnenableBgpBackwardNotification_Type(TruthValue):
    """Custom type nnenableBgpBackwardNotification based on TruthValue"""
    defaultValue = 1


_NnenableBgpBackwardNotification_Type.__name__ = "TruthValue"
_NnenableBgpBackwardNotification_Object = MibScalar
nnenableBgpBackwardNotification = _NnenableBgpBackwardNotification_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 14, 2),
    _NnenableBgpBackwardNotification_Type()
)
nnenableBgpBackwardNotification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnenableBgpBackwardNotification.setStatus("current")
_NnsystemNotificationsVars_ObjectIdentity = ObjectIdentity
nnsystemNotificationsVars = _NnsystemNotificationsVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 15)
)


class _NnsysRestartMsg_Type(DisplayString):
    """Custom type nnsysRestartMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NnsysRestartMsg_Type.__name__ = "DisplayString"
_NnsysRestartMsg_Object = MibScalar
nnsysRestartMsg = _NnsysRestartMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 15, 1),
    _NnsysRestartMsg_Type()
)
nnsysRestartMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnsysRestartMsg.setStatus("current")


class _NnsysLoginMsg_Type(DisplayString):
    """Custom type nnsysLoginMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NnsysLoginMsg_Type.__name__ = "DisplayString"
_NnsysLoginMsg_Object = MibScalar
nnsysLoginMsg = _NnsysLoginMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 15, 2),
    _NnsysLoginMsg_Type()
)
nnsysLoginMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnsysLoginMsg.setStatus("current")


class _NnsysLogoutMsg_Type(DisplayString):
    """Custom type nnsysLogoutMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NnsysLogoutMsg_Type.__name__ = "DisplayString"
_NnsysLogoutMsg_Object = MibScalar
nnsysLogoutMsg = _NnsysLogoutMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 15, 3),
    _NnsysLogoutMsg_Type()
)
nnsysLogoutMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnsysLogoutMsg.setStatus("current")


class _NnsysLoginFailMsg_Type(DisplayString):
    """Custom type nnsysLoginFailMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NnsysLoginFailMsg_Type.__name__ = "DisplayString"
_NnsysLoginFailMsg_Object = MibScalar
nnsysLoginFailMsg = _NnsysLoginFailMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 15, 4),
    _NnsysLoginFailMsg_Type()
)
nnsysLoginFailMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnsysLoginFailMsg.setStatus("current")


class _NnprotocolType_Type(Integer32):
    """Custom type nnprotocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("gui", 1),
          ("ssh", 2),
          ("other", 3))
    )


_NnprotocolType_Type.__name__ = "Integer32"
_NnprotocolType_Object = MibScalar
nnprotocolType = _NnprotocolType_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 15, 5),
    _NnprotocolType_Type()
)
nnprotocolType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnprotocolType.setStatus("current")


class _NnclientIpAddress_Type(DisplayString):
    """Custom type nnclientIpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NnclientIpAddress_Type.__name__ = "DisplayString"
_NnclientIpAddress_Object = MibScalar
nnclientIpAddress = _NnclientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 15, 6),
    _NnclientIpAddress_Type()
)
nnclientIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnclientIpAddress.setStatus("current")


class _NntimeStamp_Type(DisplayString):
    """Custom type nntimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NntimeStamp_Type.__name__ = "DisplayString"
_NntimeStamp_Object = MibScalar
nntimeStamp = _NntimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 15, 7),
    _NntimeStamp_Type()
)
nntimeStamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nntimeStamp.setStatus("current")


class _NnreasonForFailure_Type(Integer32):
    """Custom type nnreasonForFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("username", 1),
          ("password", 2),
          ("other", 3))
    )


_NnreasonForFailure_Type.__name__ = "Integer32"
_NnreasonForFailure_Object = MibScalar
nnreasonForFailure = _NnreasonForFailure_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 15, 8),
    _NnreasonForFailure_Type()
)
nnreasonForFailure.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnreasonForFailure.setStatus("current")
_NnsysDst_ObjectIdentity = ObjectIdentity
nnsysDst = _NnsysDst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 20)
)


class _NnsysDstLocation_Type(DisplayString):
    """Custom type nnsysDstLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NnsysDstLocation_Type.__name__ = "DisplayString"
_NnsysDstLocation_Object = MibScalar
nnsysDstLocation = _NnsysDstLocation_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 20, 1),
    _NnsysDstLocation_Type()
)
nnsysDstLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnsysDstLocation.setStatus("current")


class _NnsysDstCurTimeZone_Type(OctetString):
    """Custom type nnsysDstCurTimeZone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_NnsysDstCurTimeZone_Type.__name__ = "OctetString"
_NnsysDstCurTimeZone_Object = MibScalar
nnsysDstCurTimeZone = _NnsysDstCurTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 20, 2),
    _NnsysDstCurTimeZone_Type()
)
nnsysDstCurTimeZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnsysDstCurTimeZone.setStatus("current")


class _NnsysDstCurTime_Type(OctetString):
    """Custom type nnsysDstCurTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_NnsysDstCurTime_Type.__name__ = "OctetString"
_NnsysDstCurTime_Object = MibScalar
nnsysDstCurTime = _NnsysDstCurTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 20, 3),
    _NnsysDstCurTime_Type()
)
nnsysDstCurTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnsysDstCurTime.setStatus("current")


class _NnsysDstAutomated_Type(Integer32):
    """Custom type nnsysDstAutomated based on Integer32"""
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


_NnsysDstAutomated_Type.__name__ = "Integer32"
_NnsysDstAutomated_Object = MibScalar
nnsysDstAutomated = _NnsysDstAutomated_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 20, 4),
    _NnsysDstAutomated_Type()
)
nnsysDstAutomated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnsysDstAutomated.setStatus("current")


class _NnsysDstStatus_Type(Integer32):
    """Custom type nnsysDstStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notactive", 2))
    )


_NnsysDstStatus_Type.__name__ = "Integer32"
_NnsysDstStatus_Object = MibScalar
nnsysDstStatus = _NnsysDstStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 20, 5),
    _NnsysDstStatus_Type()
)
nnsysDstStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnsysDstStatus.setStatus("current")


class _NnsysDstStart_Type(OctetString):
    """Custom type nnsysDstStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )
    fixed_length = 7


_NnsysDstStart_Type.__name__ = "OctetString"
_NnsysDstStart_Object = MibScalar
nnsysDstStart = _NnsysDstStart_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 20, 6),
    _NnsysDstStart_Type()
)
nnsysDstStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnsysDstStart.setStatus("current")


class _NnsysDstEnd_Type(OctetString):
    """Custom type nnsysDstEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )
    fixed_length = 7


_NnsysDstEnd_Type.__name__ = "OctetString"
_NnsysDstEnd_Object = MibScalar
nnsysDstEnd = _NnsysDstEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 20, 7),
    _NnsysDstEnd_Type()
)
nnsysDstEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnsysDstEnd.setStatus("current")


class _NnsysDstDuration_Type(OctetString):
    """Custom type nnsysDstDuration based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_NnsysDstDuration_Type.__name__ = "OctetString"
_NnsysDstDuration_Object = MibScalar
nnsysDstDuration = _NnsysDstDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 20, 8),
    _NnsysDstDuration_Type()
)
nnsysDstDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnsysDstDuration.setStatus("current")
_NnssmTraps_ObjectIdentity = ObjectIdentity
nnssmTraps = _NnssmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 21)
)
_NnssmNotifications_ObjectIdentity = ObjectIdentity
nnssmNotifications = _NnssmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 21, 0)
)
_NnssmTrapVariables_ObjectIdentity = ObjectIdentity
nnssmTrapVariables = _NnssmTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 21, 1)
)


class _NnssmCurrentState_Type(DisplayString):
    """Custom type nnssmCurrentState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_NnssmCurrentState_Type.__name__ = "DisplayString"
_NnssmCurrentState_Object = MibScalar
nnssmCurrentState = _NnssmCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 21, 1, 1),
    _NnssmCurrentState_Type()
)
nnssmCurrentState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnssmCurrentState.setStatus("current")


class _NnssmPreviousState_Type(DisplayString):
    """Custom type nnssmPreviousState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_NnssmPreviousState_Type.__name__ = "DisplayString"
_NnssmPreviousState_Object = MibScalar
nnssmPreviousState = _NnssmPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 21, 1, 2),
    _NnssmPreviousState_Type()
)
nnssmPreviousState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnssmPreviousState.setStatus("current")


class _NnenableSsmModeNotification_Type(TruthValue):
    """Custom type nnenableSsmModeNotification based on TruthValue"""
    defaultValue = 1


_NnenableSsmModeNotification_Type.__name__ = "TruthValue"
_NnenableSsmModeNotification_Object = MibScalar
nnenableSsmModeNotification = _NnenableSsmModeNotification_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 21, 2),
    _NnenableSsmModeNotification_Type()
)
nnenableSsmModeNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnenableSsmModeNotification.setStatus("current")

# Managed Objects groups


# Notification objects

nnshutDownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 4, 0, 1)
)
nnshutDownNotification.setObjects(
    ("SYSTEM-MIB", "nnsysRestartMsg")
)
if mibBuilder.loadTexts:
    nnshutDownNotification.setStatus(
        "current"
    )

nnuserLoginNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 4, 0, 2)
)
nnuserLoginNotification.setObjects(
    ("SYSTEM-MIB", "nnsysLoginMsg")
)
if mibBuilder.loadTexts:
    nnuserLoginNotification.setStatus(
        "current"
    )

nnuserLogOffNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 4, 0, 3)
)
nnuserLogOffNotification.setObjects(
    ("SYSTEM-MIB", "nnsysLogoutMsg")
)
if mibBuilder.loadTexts:
    nnuserLogOffNotification.setStatus(
        "current"
    )

nnuserLoginFailNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 4, 0, 4)
)
nnuserLoginFailNotification.setObjects(
    ("SYSTEM-MIB", "nnsysLoginFailMsg")
)
if mibBuilder.loadTexts:
    nnuserLoginFailNotification.setStatus(
        "current"
    )

nnauthenticationFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 4, 0, 5)
)
nnauthenticationFailureNotification.setObjects(
      *(("SYSTEM-MIB", "nnprotocolType"),
        ("SYSTEM-MIB", "nnclientIpAddress"),
        ("SYSTEM-MIB", "nntimeStamp"),
        ("SYSTEM-MIB", "nnreasonForFailure"))
)
if mibBuilder.loadTexts:
    nnauthenticationFailureNotification.setStatus(
        "current"
    )

nnauthenticationLoginSuccessNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 4, 0, 6)
)
nnauthenticationLoginSuccessNotification.setObjects(
      *(("SYSTEM-MIB", "nnprotocolType"),
        ("SYSTEM-MIB", "nnclientIpAddress"),
        ("SYSTEM-MIB", "nntimeStamp"))
)
if mibBuilder.loadTexts:
    nnauthenticationLoginSuccessNotification.setStatus(
        "current"
    )

nnlogoutNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 4, 0, 7)
)
nnlogoutNotification.setObjects(
      *(("SYSTEM-MIB", "nnprotocolType"),
        ("SYSTEM-MIB", "nnclientIpAddress"),
        ("SYSTEM-MIB", "nntimeStamp"))
)
if mibBuilder.loadTexts:
    nnlogoutNotification.setStatus(
        "current"
    )

nnsntpEnableNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 12, 0, 1)
)
nnsntpEnableNotification.setObjects(
      *(("SYSTEM-MIB", "nnsntpServerAddr"),
        ("SYSTEM-MIB", "nnsntpTimeout"))
)
if mibBuilder.loadTexts:
    nnsntpEnableNotification.setStatus(
        "current"
    )

nnsntpDisableNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 12, 0, 2)
)
nnsntpDisableNotification.setObjects(
      *(("SYSTEM-MIB", "nnsntpServerAddr"),
        ("SYSTEM-MIB", "nnsntpTimeout"))
)
if mibBuilder.loadTexts:
    nnsntpDisableNotification.setStatus(
        "current"
    )

nnsntpSuccessNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 12, 0, 3)
)
nnsntpSuccessNotification.setObjects(
      *(("SYSTEM-MIB", "nnsntpServerAddr"),
        ("SYSTEM-MIB", "nnsntpTimeout"))
)
if mibBuilder.loadTexts:
    nnsntpSuccessNotification.setStatus(
        "current"
    )

nnsntpErrorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 12, 0, 4)
)
nnsntpErrorNotification.setObjects(
      *(("SYSTEM-MIB", "nnsntpServerAddr"),
        ("SYSTEM-MIB", "nnsntpTimeout"))
)
if mibBuilder.loadTexts:
    nnsntpErrorNotification.setStatus(
        "current"
    )

nnssmFromNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 21, 0, 1)
)
nnssmFromNormalTrap.setObjects(
    ("SYSTEM-MIB", "nnssmCurrentState")
)
if mibBuilder.loadTexts:
    nnssmFromNormalTrap.setStatus(
        "current"
    )

nnssmToNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 21, 0, 2)
)
nnssmToNormalTrap.setObjects(
    ("SYSTEM-MIB", "nnssmPreviousState")
)
if mibBuilder.loadTexts:
    nnssmToNormalTrap.setStatus(
        "current"
    )


# Notifications groups

nnsystemNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 18)
)
nnsystemNotificationGroup.setObjects(
      *(("SYSTEM-MIB", "nnshutDownNotification"),
        ("SYSTEM-MIB", "nnuserLoginNotification"),
        ("SYSTEM-MIB", "nnuserLogOffNotification"),
        ("SYSTEM-MIB", "nnuserLoginFailNotification"),
        ("SYSTEM-MIB", "nnauthenticationFailureNotification"),
        ("SYSTEM-MIB", "nnauthenticationLoginSuccessNotification"),
        ("SYSTEM-MIB", "nnlogoutNotification"))
)
if mibBuilder.loadTexts:
    nnsystemNotificationGroup.setStatus(
        "current"
    )

nnsntpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 1, 19)
)
nnsntpNotificationGroup.setObjects(
      *(("SYSTEM-MIB", "nnsntpEnableNotification"),
        ("SYSTEM-MIB", "nnsntpDisableNotification"),
        ("SYSTEM-MIB", "nnsntpSuccessNotification"),
        ("SYSTEM-MIB", "nnsntpErrorNotification"))
)
if mibBuilder.loadTexts:
    nnsntpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYSTEM-MIB",
    **{"SntpEnabled": SntpEnabled,
       "nnsystemMib": nnsystemMib,
       "nnsystemObjects": nnsystemObjects,
       "nnsysIpAddr": nnsysIpAddr,
       "nnsysNetMask": nnsysNetMask,
       "nnsysBroadcast": nnsysBroadcast,
       "nnsysVersion": nnsysVersion,
       "nnsysHostName": nnsysHostName,
       "nnsysDomainName": nnsysDomainName,
       "nnsysAlarmStatus": nnsysAlarmStatus,
       "nnsysReset": nnsysReset,
       "nnsysDateTime": nnsysDateTime,
       "nnarpClearAtTable": nnarpClearAtTable,
       "nnipClearRouteTable": nnipClearRouteTable,
       "nnarpTimeOut": nnarpTimeOut,
       "nndnsGroup": nndnsGroup,
       "nndnsEnable": nndnsEnable,
       "nndnsServerTable": nndnsServerTable,
       "nndnsServerEntry": nndnsServerEntry,
       "nndnsServerEntryType": nndnsServerEntryType,
       "nndnsServerAddr": nndnsServerAddr,
       "nnsystemEnableNotification": nnsystemEnableNotification,
       "nnenableSysShutDownNotification": nnenableSysShutDownNotification,
       "nnenableUserLoginNotification": nnenableUserLoginNotification,
       "nnenableUserLogOffNotification": nnenableUserLogOffNotification,
       "nnenableUserLoginFailNotification": nnenableUserLoginFailNotification,
       "nnenableAuthenticationLoginFailNotification": nnenableAuthenticationLoginFailNotification,
       "nnenableAuthenticationLoginSuccessNotification": nnenableAuthenticationLoginSuccessNotification,
       "nnenableLogoutNotification": nnenableLogoutNotification,
       "nnsystemNotifications": nnsystemNotifications,
       "nnsystemTraps": nnsystemTraps,
       "nnshutDownNotification": nnshutDownNotification,
       "nnuserLoginNotification": nnuserLoginNotification,
       "nnuserLogOffNotification": nnuserLogOffNotification,
       "nnuserLoginFailNotification": nnuserLoginFailNotification,
       "nnauthenticationFailureNotification": nnauthenticationFailureNotification,
       "nnauthenticationLoginSuccessNotification": nnauthenticationLoginSuccessNotification,
       "nnlogoutNotification": nnlogoutNotification,
       "nnuserAdminGroup": nnuserAdminGroup,
       "nnuserName": nnuserName,
       "nnsntpGroup": nnsntpGroup,
       "nnsntpClieenabled": nnsntpClieenabled,
       "nnsntpServerAddr": nnsntpServerAddr,
       "nnsntpTimeout": nnsntpTimeout,
       "nnsntpNotificationEnables": nnsntpNotificationEnables,
       "nnenableSntpNotification": nnenableSntpNotification,
       "nnsntpNotifications": nnsntpNotifications,
       "nnsntpTraps": nnsntpTraps,
       "nnsntpEnableNotification": nnsntpEnableNotification,
       "nnsntpDisableNotification": nnsntpDisableNotification,
       "nnsntpSuccessNotification": nnsntpSuccessNotification,
       "nnsntpErrorNotification": nnsntpErrorNotification,
       "nnenableBgpNotifications": nnenableBgpNotifications,
       "nnenableBgpEstablishedNotification": nnenableBgpEstablishedNotification,
       "nnenableBgpBackwardNotification": nnenableBgpBackwardNotification,
       "nnsystemNotificationsVars": nnsystemNotificationsVars,
       "nnsysRestartMsg": nnsysRestartMsg,
       "nnsysLoginMsg": nnsysLoginMsg,
       "nnsysLogoutMsg": nnsysLogoutMsg,
       "nnsysLoginFailMsg": nnsysLoginFailMsg,
       "nnprotocolType": nnprotocolType,
       "nnclientIpAddress": nnclientIpAddress,
       "nntimeStamp": nntimeStamp,
       "nnreasonForFailure": nnreasonForFailure,
       "nnsystemNotificationGroup": nnsystemNotificationGroup,
       "nnsntpNotificationGroup": nnsntpNotificationGroup,
       "nnsysDst": nnsysDst,
       "nnsysDstLocation": nnsysDstLocation,
       "nnsysDstCurTimeZone": nnsysDstCurTimeZone,
       "nnsysDstCurTime": nnsysDstCurTime,
       "nnsysDstAutomated": nnsysDstAutomated,
       "nnsysDstStatus": nnsysDstStatus,
       "nnsysDstStart": nnsysDstStart,
       "nnsysDstEnd": nnsysDstEnd,
       "nnsysDstDuration": nnsysDstDuration,
       "nnssmTraps": nnssmTraps,
       "nnssmNotifications": nnssmNotifications,
       "nnssmFromNormalTrap": nnssmFromNormalTrap,
       "nnssmToNormalTrap": nnssmToNormalTrap,
       "nnssmTrapVariables": nnssmTrapVariables,
       "nnssmCurrentState": nnssmCurrentState,
       "nnssmPreviousState": nnssmPreviousState,
       "nnenableSsmModeNotification": nnenableSsmModeNotification}
)
