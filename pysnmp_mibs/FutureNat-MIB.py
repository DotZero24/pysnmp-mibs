# SNMP MIB module (FutureNat-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/FutureNat-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:34 2025
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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

futureNatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14)
)
if mibBuilder.loadTexts:
    futureNatMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Status(TextualConvention, Integer32):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_Nat_ObjectIdentity = ObjectIdentity
nat = _Nat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1)
)
_NatStatInfo_ObjectIdentity = ObjectIdentity
natStatInfo = _NatStatInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 1)
)


class _NatEnable_Type(Status):
    """Custom type natEnable based on Status"""
    defaultValue = 1


_NatEnable_Type.__name__ = "Status"
_NatEnable_Object = MibScalar
natEnable = _NatEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 1, 1),
    _NatEnable_Type()
)
natEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natEnable.setStatus("current")


class _NatTypicalNumberOfEntries_Type(Integer32):
    """Custom type natTypicalNumberOfEntries based on Integer32"""
    defaultValue = 9000


_NatTypicalNumberOfEntries_Type.__name__ = "Integer32"
_NatTypicalNumberOfEntries_Object = MibScalar
natTypicalNumberOfEntries = _NatTypicalNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 1, 2),
    _NatTypicalNumberOfEntries_Type()
)
natTypicalNumberOfEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natTypicalNumberOfEntries.setStatus("current")


class _NatTranslatedLocalPortStart_Type(Integer32):
    """Custom type natTranslatedLocalPortStart based on Integer32"""
    defaultValue = 6001


_NatTranslatedLocalPortStart_Type.__name__ = "Integer32"
_NatTranslatedLocalPortStart_Object = MibScalar
natTranslatedLocalPortStart = _NatTranslatedLocalPortStart_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 1, 3),
    _NatTranslatedLocalPortStart_Type()
)
natTranslatedLocalPortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natTranslatedLocalPortStart.setStatus("current")


class _NatIdleTimeOut_Type(Integer32):
    """Custom type natIdleTimeOut based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_NatIdleTimeOut_Type.__name__ = "Integer32"
_NatIdleTimeOut_Object = MibScalar
natIdleTimeOut = _NatIdleTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 1, 4),
    _NatIdleTimeOut_Type()
)
natIdleTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natIdleTimeOut.setStatus("current")


class _NatTcpTimeOut_Type(Integer32):
    """Custom type natTcpTimeOut based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 86400),
    )


_NatTcpTimeOut_Type.__name__ = "Integer32"
_NatTcpTimeOut_Object = MibScalar
natTcpTimeOut = _NatTcpTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 1, 5),
    _NatTcpTimeOut_Type()
)
natTcpTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natTcpTimeOut.setStatus("current")


class _NatUdpTimeOut_Type(Integer32):
    """Custom type natUdpTimeOut based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 86400),
    )


_NatUdpTimeOut_Type.__name__ = "Integer32"
_NatUdpTimeOut_Object = MibScalar
natUdpTimeOut = _NatUdpTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 1, 6),
    _NatUdpTimeOut_Type()
)
natUdpTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natUdpTimeOut.setStatus("current")


class _NatTrcFlag_Type(Integer32):
    """Custom type natTrcFlag based on Integer32"""
    defaultValue = 0


_NatTrcFlag_Type.__name__ = "Integer32"
_NatTrcFlag_Object = MibScalar
natTrcFlag = _NatTrcFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 1, 7),
    _NatTrcFlag_Type()
)
natTrcFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natTrcFlag.setStatus("current")
_NatStatDynamicAllocFailureCount_Type = Counter32
_NatStatDynamicAllocFailureCount_Object = MibScalar
natStatDynamicAllocFailureCount = _NatStatDynamicAllocFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 1, 8),
    _NatStatDynamicAllocFailureCount_Type()
)
natStatDynamicAllocFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natStatDynamicAllocFailureCount.setStatus("current")
_NatStatTotalNumberOfTranslations_Type = Counter32
_NatStatTotalNumberOfTranslations_Object = MibScalar
natStatTotalNumberOfTranslations = _NatStatTotalNumberOfTranslations_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 1, 9),
    _NatStatTotalNumberOfTranslations_Type()
)
natStatTotalNumberOfTranslations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natStatTotalNumberOfTranslations.setStatus("current")
_NatStatTotalNumberOfActiveSessions_Type = Counter32
_NatStatTotalNumberOfActiveSessions_Object = MibScalar
natStatTotalNumberOfActiveSessions = _NatStatTotalNumberOfActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 1, 10),
    _NatStatTotalNumberOfActiveSessions_Type()
)
natStatTotalNumberOfActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natStatTotalNumberOfActiveSessions.setStatus("current")
_NatStatTotalNumberOfPktsDropped_Type = Counter32
_NatStatTotalNumberOfPktsDropped_Object = MibScalar
natStatTotalNumberOfPktsDropped = _NatStatTotalNumberOfPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 1, 11),
    _NatStatTotalNumberOfPktsDropped_Type()
)
natStatTotalNumberOfPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natStatTotalNumberOfPktsDropped.setStatus("current")
_NatStatTotalNumberOfSessionsClosed_Type = Counter32
_NatStatTotalNumberOfSessionsClosed_Object = MibScalar
natStatTotalNumberOfSessionsClosed = _NatStatTotalNumberOfSessionsClosed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 1, 12),
    _NatStatTotalNumberOfSessionsClosed_Type()
)
natStatTotalNumberOfSessionsClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natStatTotalNumberOfSessionsClosed.setStatus("current")


class _NatIKEPortTranslation_Type(Status):
    """Custom type natIKEPortTranslation based on Status"""
    defaultValue = 2


_NatIKEPortTranslation_Type.__name__ = "Status"
_NatIKEPortTranslation_Object = MibScalar
natIKEPortTranslation = _NatIKEPortTranslation_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 1, 13),
    _NatIKEPortTranslation_Type()
)
natIKEPortTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natIKEPortTranslation.setStatus("current")


class _NatIKETimeout_Type(Integer32):
    """Custom type natIKETimeout based on Integer32"""
    defaultValue = 28800


_NatIKETimeout_Type.__name__ = "Integer32"
_NatIKETimeout_Object = MibScalar
natIKETimeout = _NatIKETimeout_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 1, 14),
    _NatIKETimeout_Type()
)
natIKETimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natIKETimeout.setStatus("current")


class _NatIPSecTimeout_Type(Integer32):
    """Custom type natIPSecTimeout based on Integer32"""
    defaultValue = 28800


_NatIPSecTimeout_Type.__name__ = "Integer32"
_NatIPSecTimeout_Object = MibScalar
natIPSecTimeout = _NatIPSecTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 1, 15),
    _NatIPSecTimeout_Type()
)
natIPSecTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natIPSecTimeout.setStatus("current")


class _NatIPSecPendingTimeout_Type(Integer32):
    """Custom type natIPSecPendingTimeout based on Integer32"""
    defaultValue = 30


_NatIPSecPendingTimeout_Type.__name__ = "Integer32"
_NatIPSecPendingTimeout_Object = MibScalar
natIPSecPendingTimeout = _NatIPSecPendingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 1, 16),
    _NatIPSecPendingTimeout_Type()
)
natIPSecPendingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natIPSecPendingTimeout.setStatus("current")


class _NatIPSecMaxRetry_Type(Integer32):
    """Custom type natIPSecMaxRetry based on Integer32"""
    defaultValue = 3


_NatIPSecMaxRetry_Type.__name__ = "Integer32"
_NatIPSecMaxRetry_Object = MibScalar
natIPSecMaxRetry = _NatIPSecMaxRetry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 1, 17),
    _NatIPSecMaxRetry_Type()
)
natIPSecMaxRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natIPSecMaxRetry.setStatus("current")


class _SipAlgPort_Type(Integer32):
    """Custom type sipAlgPort based on Integer32"""
    defaultValue = 5060


_SipAlgPort_Type.__name__ = "Integer32"
_SipAlgPort_Object = MibScalar
sipAlgPort = _SipAlgPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 1, 18),
    _SipAlgPort_Type()
)
sipAlgPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipAlgPort.setStatus("current")


class _NatSipAlgPartialEntryTimeOut_Type(Integer32):
    """Custom type natSipAlgPartialEntryTimeOut based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(212, 86400),
    )


_NatSipAlgPartialEntryTimeOut_Type.__name__ = "Integer32"
_NatSipAlgPartialEntryTimeOut_Object = MibScalar
natSipAlgPartialEntryTimeOut = _NatSipAlgPartialEntryTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 1, 19),
    _NatSipAlgPartialEntryTimeOut_Type()
)
natSipAlgPartialEntryTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natSipAlgPartialEntryTimeOut.setStatus("current")
_NatDynamicTransTable_Object = MibTable
natDynamicTransTable = _NatDynamicTransTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 2)
)
if mibBuilder.loadTexts:
    natDynamicTransTable.setStatus("current")
_NatDynamicTransEntry_Object = MibTableRow
natDynamicTransEntry = _NatDynamicTransEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 2, 1)
)
natDynamicTransEntry.setIndexNames(
    (0, "FutureNat-MIB", "natDynamicTransInterfaceNum"),
    (0, "FutureNat-MIB", "natDynamicTransLocalIp"),
    (0, "FutureNat-MIB", "natDynamicTransLocalPort"),
    (0, "FutureNat-MIB", "natDynamicTransOutsideIp"),
    (0, "FutureNat-MIB", "natDynamicTransOutsidePort"),
)
if mibBuilder.loadTexts:
    natDynamicTransEntry.setStatus("current")


class _NatDynamicTransInterfaceNum_Type(Integer32):
    """Custom type natDynamicTransInterfaceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NatDynamicTransInterfaceNum_Type.__name__ = "Integer32"
_NatDynamicTransInterfaceNum_Object = MibTableColumn
natDynamicTransInterfaceNum = _NatDynamicTransInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 2, 1, 1),
    _NatDynamicTransInterfaceNum_Type()
)
natDynamicTransInterfaceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natDynamicTransInterfaceNum.setStatus("current")
_NatDynamicTransLocalIp_Type = IpAddress
_NatDynamicTransLocalIp_Object = MibTableColumn
natDynamicTransLocalIp = _NatDynamicTransLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 2, 1, 2),
    _NatDynamicTransLocalIp_Type()
)
natDynamicTransLocalIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natDynamicTransLocalIp.setStatus("current")
_NatDynamicTransTranslatedLocalIp_Type = IpAddress
_NatDynamicTransTranslatedLocalIp_Object = MibTableColumn
natDynamicTransTranslatedLocalIp = _NatDynamicTransTranslatedLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 2, 1, 3),
    _NatDynamicTransTranslatedLocalIp_Type()
)
natDynamicTransTranslatedLocalIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natDynamicTransTranslatedLocalIp.setStatus("current")


class _NatDynamicTransLocalPort_Type(Integer32):
    """Custom type natDynamicTransLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NatDynamicTransLocalPort_Type.__name__ = "Integer32"
_NatDynamicTransLocalPort_Object = MibTableColumn
natDynamicTransLocalPort = _NatDynamicTransLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 2, 1, 4),
    _NatDynamicTransLocalPort_Type()
)
natDynamicTransLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natDynamicTransLocalPort.setStatus("current")
_NatDynamicTransTranslatedLocalPort_Type = Integer32
_NatDynamicTransTranslatedLocalPort_Object = MibTableColumn
natDynamicTransTranslatedLocalPort = _NatDynamicTransTranslatedLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 2, 1, 5),
    _NatDynamicTransTranslatedLocalPort_Type()
)
natDynamicTransTranslatedLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natDynamicTransTranslatedLocalPort.setStatus("current")
_NatDynamicTransOutsideIp_Type = IpAddress
_NatDynamicTransOutsideIp_Object = MibTableColumn
natDynamicTransOutsideIp = _NatDynamicTransOutsideIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 2, 1, 6),
    _NatDynamicTransOutsideIp_Type()
)
natDynamicTransOutsideIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natDynamicTransOutsideIp.setStatus("current")


class _NatDynamicTransOutsidePort_Type(Integer32):
    """Custom type natDynamicTransOutsidePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NatDynamicTransOutsidePort_Type.__name__ = "Integer32"
_NatDynamicTransOutsidePort_Object = MibTableColumn
natDynamicTransOutsidePort = _NatDynamicTransOutsidePort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 2, 1, 7),
    _NatDynamicTransOutsidePort_Type()
)
natDynamicTransOutsidePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natDynamicTransOutsidePort.setStatus("current")
_NatDynamicTransLastUseTime_Type = Integer32
_NatDynamicTransLastUseTime_Object = MibTableColumn
natDynamicTransLastUseTime = _NatDynamicTransLastUseTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 2, 1, 8),
    _NatDynamicTransLastUseTime_Type()
)
natDynamicTransLastUseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natDynamicTransLastUseTime.setStatus("current")
_NatGlobalAddressTable_Object = MibTable
natGlobalAddressTable = _NatGlobalAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 3)
)
if mibBuilder.loadTexts:
    natGlobalAddressTable.setStatus("current")
_NatGlobalAddressEntry_Object = MibTableRow
natGlobalAddressEntry = _NatGlobalAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 3, 1)
)
natGlobalAddressEntry.setIndexNames(
    (0, "FutureNat-MIB", "natGlobalAddressInterfaceNum"),
    (0, "FutureNat-MIB", "natGlobalAddressTranslatedLocalIp"),
)
if mibBuilder.loadTexts:
    natGlobalAddressEntry.setStatus("current")


class _NatGlobalAddressInterfaceNum_Type(Integer32):
    """Custom type natGlobalAddressInterfaceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NatGlobalAddressInterfaceNum_Type.__name__ = "Integer32"
_NatGlobalAddressInterfaceNum_Object = MibTableColumn
natGlobalAddressInterfaceNum = _NatGlobalAddressInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 3, 1, 1),
    _NatGlobalAddressInterfaceNum_Type()
)
natGlobalAddressInterfaceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natGlobalAddressInterfaceNum.setStatus("current")
_NatGlobalAddressTranslatedLocalIp_Type = IpAddress
_NatGlobalAddressTranslatedLocalIp_Object = MibTableColumn
natGlobalAddressTranslatedLocalIp = _NatGlobalAddressTranslatedLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 3, 1, 2),
    _NatGlobalAddressTranslatedLocalIp_Type()
)
natGlobalAddressTranslatedLocalIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natGlobalAddressTranslatedLocalIp.setStatus("current")
_NatGlobalAddressMask_Type = IpAddress
_NatGlobalAddressMask_Object = MibTableColumn
natGlobalAddressMask = _NatGlobalAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 3, 1, 3),
    _NatGlobalAddressMask_Type()
)
natGlobalAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natGlobalAddressMask.setStatus("current")
_NatGlobalAddressEntryStatus_Type = RowStatus
_NatGlobalAddressEntryStatus_Object = MibTableColumn
natGlobalAddressEntryStatus = _NatGlobalAddressEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 3, 1, 4),
    _NatGlobalAddressEntryStatus_Type()
)
natGlobalAddressEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natGlobalAddressEntryStatus.setStatus("current")
_NatLocalAddressTable_Object = MibTable
natLocalAddressTable = _NatLocalAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 4)
)
if mibBuilder.loadTexts:
    natLocalAddressTable.setStatus("current")
_NatLocalAddressEntry_Object = MibTableRow
natLocalAddressEntry = _NatLocalAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 4, 1)
)
natLocalAddressEntry.setIndexNames(
    (0, "FutureNat-MIB", "natLocalAddressInterfaceNumber"),
    (0, "FutureNat-MIB", "natLocalAddressLocalIp"),
)
if mibBuilder.loadTexts:
    natLocalAddressEntry.setStatus("current")


class _NatLocalAddressInterfaceNumber_Type(Integer32):
    """Custom type natLocalAddressInterfaceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NatLocalAddressInterfaceNumber_Type.__name__ = "Integer32"
_NatLocalAddressInterfaceNumber_Object = MibTableColumn
natLocalAddressInterfaceNumber = _NatLocalAddressInterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 4, 1, 1),
    _NatLocalAddressInterfaceNumber_Type()
)
natLocalAddressInterfaceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natLocalAddressInterfaceNumber.setStatus("current")
_NatLocalAddressLocalIp_Type = IpAddress
_NatLocalAddressLocalIp_Object = MibTableColumn
natLocalAddressLocalIp = _NatLocalAddressLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 4, 1, 2),
    _NatLocalAddressLocalIp_Type()
)
natLocalAddressLocalIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natLocalAddressLocalIp.setStatus("current")
_NatLocalAddressMask_Type = IpAddress
_NatLocalAddressMask_Object = MibTableColumn
natLocalAddressMask = _NatLocalAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 4, 1, 3),
    _NatLocalAddressMask_Type()
)
natLocalAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natLocalAddressMask.setStatus("current")
_NatLocalAddressEntryStatus_Type = RowStatus
_NatLocalAddressEntryStatus_Object = MibTableColumn
natLocalAddressEntryStatus = _NatLocalAddressEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 4, 1, 4),
    _NatLocalAddressEntryStatus_Type()
)
natLocalAddressEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natLocalAddressEntryStatus.setStatus("current")
_NatStaticTable_Object = MibTable
natStaticTable = _NatStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 5)
)
if mibBuilder.loadTexts:
    natStaticTable.setStatus("current")
_NatStaticEntry_Object = MibTableRow
natStaticEntry = _NatStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 5, 1)
)
natStaticEntry.setIndexNames(
    (0, "FutureNat-MIB", "natStaticInterfaceNum"),
    (0, "FutureNat-MIB", "natStaticLocalIp"),
)
if mibBuilder.loadTexts:
    natStaticEntry.setStatus("current")


class _NatStaticInterfaceNum_Type(Integer32):
    """Custom type natStaticInterfaceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NatStaticInterfaceNum_Type.__name__ = "Integer32"
_NatStaticInterfaceNum_Object = MibTableColumn
natStaticInterfaceNum = _NatStaticInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 5, 1, 1),
    _NatStaticInterfaceNum_Type()
)
natStaticInterfaceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natStaticInterfaceNum.setStatus("current")
_NatStaticLocalIp_Type = IpAddress
_NatStaticLocalIp_Object = MibTableColumn
natStaticLocalIp = _NatStaticLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 5, 1, 2),
    _NatStaticLocalIp_Type()
)
natStaticLocalIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natStaticLocalIp.setStatus("current")
_NatStaticTranslatedLocalIp_Type = IpAddress
_NatStaticTranslatedLocalIp_Object = MibTableColumn
natStaticTranslatedLocalIp = _NatStaticTranslatedLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 5, 1, 3),
    _NatStaticTranslatedLocalIp_Type()
)
natStaticTranslatedLocalIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natStaticTranslatedLocalIp.setStatus("current")
_NatStaticEntryStatus_Type = RowStatus
_NatStaticEntryStatus_Object = MibTableColumn
natStaticEntryStatus = _NatStaticEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 5, 1, 4),
    _NatStaticEntryStatus_Type()
)
natStaticEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natStaticEntryStatus.setStatus("current")
_NatStaticNaptTable_Object = MibTable
natStaticNaptTable = _NatStaticNaptTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 6)
)
if mibBuilder.loadTexts:
    natStaticNaptTable.setStatus("current")
_NatStaticNaptEntry_Object = MibTableRow
natStaticNaptEntry = _NatStaticNaptEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 6, 1)
)
natStaticNaptEntry.setIndexNames(
    (0, "FutureNat-MIB", "natStaticNaptInterfaceNum"),
    (0, "FutureNat-MIB", "natStaticNaptLocalIp"),
    (0, "FutureNat-MIB", "natStaticNaptStartLocalPort"),
    (0, "FutureNat-MIB", "natStaticNaptEndLocalPort"),
    (0, "FutureNat-MIB", "natStaticNaptProtocolNumber"),
)
if mibBuilder.loadTexts:
    natStaticNaptEntry.setStatus("current")


class _NatStaticNaptInterfaceNum_Type(Integer32):
    """Custom type natStaticNaptInterfaceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NatStaticNaptInterfaceNum_Type.__name__ = "Integer32"
_NatStaticNaptInterfaceNum_Object = MibTableColumn
natStaticNaptInterfaceNum = _NatStaticNaptInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 6, 1, 1),
    _NatStaticNaptInterfaceNum_Type()
)
natStaticNaptInterfaceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natStaticNaptInterfaceNum.setStatus("current")
_NatStaticNaptLocalIp_Type = IpAddress
_NatStaticNaptLocalIp_Object = MibTableColumn
natStaticNaptLocalIp = _NatStaticNaptLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 6, 1, 2),
    _NatStaticNaptLocalIp_Type()
)
natStaticNaptLocalIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natStaticNaptLocalIp.setStatus("current")


class _NatStaticNaptStartLocalPort_Type(Integer32):
    """Custom type natStaticNaptStartLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NatStaticNaptStartLocalPort_Type.__name__ = "Integer32"
_NatStaticNaptStartLocalPort_Object = MibTableColumn
natStaticNaptStartLocalPort = _NatStaticNaptStartLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 6, 1, 3),
    _NatStaticNaptStartLocalPort_Type()
)
natStaticNaptStartLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natStaticNaptStartLocalPort.setStatus("current")


class _NatStaticNaptEndLocalPort_Type(Integer32):
    """Custom type natStaticNaptEndLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NatStaticNaptEndLocalPort_Type.__name__ = "Integer32"
_NatStaticNaptEndLocalPort_Object = MibTableColumn
natStaticNaptEndLocalPort = _NatStaticNaptEndLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 6, 1, 4),
    _NatStaticNaptEndLocalPort_Type()
)
natStaticNaptEndLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natStaticNaptEndLocalPort.setStatus("current")


class _NatStaticNaptProtocolNumber_Type(Integer32):
    """Custom type natStaticNaptProtocolNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              17,
              255)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 6),
          ("udp", 17),
          ("any", 255))
    )


_NatStaticNaptProtocolNumber_Type.__name__ = "Integer32"
_NatStaticNaptProtocolNumber_Object = MibTableColumn
natStaticNaptProtocolNumber = _NatStaticNaptProtocolNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 6, 1, 5),
    _NatStaticNaptProtocolNumber_Type()
)
natStaticNaptProtocolNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natStaticNaptProtocolNumber.setStatus("current")
_NatStaticNaptTranslatedLocalIp_Type = IpAddress
_NatStaticNaptTranslatedLocalIp_Object = MibTableColumn
natStaticNaptTranslatedLocalIp = _NatStaticNaptTranslatedLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 6, 1, 6),
    _NatStaticNaptTranslatedLocalIp_Type()
)
natStaticNaptTranslatedLocalIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natStaticNaptTranslatedLocalIp.setStatus("current")


class _NatStaticNaptTranslatedLocalPort_Type(Integer32):
    """Custom type natStaticNaptTranslatedLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NatStaticNaptTranslatedLocalPort_Type.__name__ = "Integer32"
_NatStaticNaptTranslatedLocalPort_Object = MibTableColumn
natStaticNaptTranslatedLocalPort = _NatStaticNaptTranslatedLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 6, 1, 7),
    _NatStaticNaptTranslatedLocalPort_Type()
)
natStaticNaptTranslatedLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natStaticNaptTranslatedLocalPort.setStatus("current")


class _NatStaticNaptDescription_Type(DisplayString):
    """Custom type natStaticNaptDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_NatStaticNaptDescription_Type.__name__ = "DisplayString"
_NatStaticNaptDescription_Object = MibTableColumn
natStaticNaptDescription = _NatStaticNaptDescription_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 6, 1, 8),
    _NatStaticNaptDescription_Type()
)
natStaticNaptDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natStaticNaptDescription.setStatus("current")
_NatStaticNaptEntryStatus_Type = RowStatus
_NatStaticNaptEntryStatus_Object = MibTableColumn
natStaticNaptEntryStatus = _NatStaticNaptEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 6, 1, 9),
    _NatStaticNaptEntryStatus_Type()
)
natStaticNaptEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natStaticNaptEntryStatus.setStatus("current")
_NatIfTable_Object = MibTable
natIfTable = _NatIfTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 7)
)
if mibBuilder.loadTexts:
    natIfTable.setStatus("current")
_NatIfEntry_Object = MibTableRow
natIfEntry = _NatIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 7, 1)
)
natIfEntry.setIndexNames(
    (0, "FutureNat-MIB", "natIfInterfaceNumber"),
)
if mibBuilder.loadTexts:
    natIfEntry.setStatus("current")


class _NatIfInterfaceNumber_Type(Integer32):
    """Custom type natIfInterfaceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NatIfInterfaceNumber_Type.__name__ = "Integer32"
_NatIfInterfaceNumber_Object = MibTableColumn
natIfInterfaceNumber = _NatIfInterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 7, 1, 1),
    _NatIfInterfaceNumber_Type()
)
natIfInterfaceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natIfInterfaceNumber.setStatus("current")


class _NatIfNat_Type(Status):
    """Custom type natIfNat based on Status"""
    defaultValue = 2


_NatIfNat_Type.__name__ = "Status"
_NatIfNat_Object = MibTableColumn
natIfNat = _NatIfNat_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 7, 1, 2),
    _NatIfNat_Type()
)
natIfNat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natIfNat.setStatus("current")


class _NatIfNapt_Type(Status):
    """Custom type natIfNapt based on Status"""
    defaultValue = 2


_NatIfNapt_Type.__name__ = "Status"
_NatIfNapt_Object = MibTableColumn
natIfNapt = _NatIfNapt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 7, 1, 3),
    _NatIfNapt_Type()
)
natIfNapt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natIfNapt.setStatus("current")


class _NatIfTwoWayNat_Type(Status):
    """Custom type natIfTwoWayNat based on Status"""
    defaultValue = 2


_NatIfTwoWayNat_Type.__name__ = "Status"
_NatIfTwoWayNat_Object = MibTableColumn
natIfTwoWayNat = _NatIfTwoWayNat_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 7, 1, 4),
    _NatIfTwoWayNat_Type()
)
natIfTwoWayNat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natIfTwoWayNat.setStatus("current")
_NatIfEntryStatus_Type = RowStatus
_NatIfEntryStatus_Object = MibTableColumn
natIfEntryStatus = _NatIfEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 7, 1, 5),
    _NatIfEntryStatus_Type()
)
natIfEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natIfEntryStatus.setStatus("current")
_NatIPSecSessionTable_Object = MibTable
natIPSecSessionTable = _NatIPSecSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 8)
)
if mibBuilder.loadTexts:
    natIPSecSessionTable.setStatus("current")
_NatIPSecSessionEntry_Object = MibTableRow
natIPSecSessionEntry = _NatIPSecSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 8, 1)
)
natIPSecSessionEntry.setIndexNames(
    (0, "FutureNat-MIB", "natIPSecSessionInterfaceNum"),
    (0, "FutureNat-MIB", "natIPSecSessionLocalIp"),
    (0, "FutureNat-MIB", "natIPSecSessionOutsideIp"),
    (0, "FutureNat-MIB", "natIPSecSessionSPIInside"),
    (0, "FutureNat-MIB", "natIPSecSessionSPIOutside"),
)
if mibBuilder.loadTexts:
    natIPSecSessionEntry.setStatus("current")


class _NatIPSecSessionInterfaceNum_Type(Integer32):
    """Custom type natIPSecSessionInterfaceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NatIPSecSessionInterfaceNum_Type.__name__ = "Integer32"
_NatIPSecSessionInterfaceNum_Object = MibTableColumn
natIPSecSessionInterfaceNum = _NatIPSecSessionInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 8, 1, 1),
    _NatIPSecSessionInterfaceNum_Type()
)
natIPSecSessionInterfaceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natIPSecSessionInterfaceNum.setStatus("current")
_NatIPSecSessionLocalIp_Type = IpAddress
_NatIPSecSessionLocalIp_Object = MibTableColumn
natIPSecSessionLocalIp = _NatIPSecSessionLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 8, 1, 2),
    _NatIPSecSessionLocalIp_Type()
)
natIPSecSessionLocalIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natIPSecSessionLocalIp.setStatus("current")
_NatIPSecSessionTranslatedLocalIp_Type = IpAddress
_NatIPSecSessionTranslatedLocalIp_Object = MibTableColumn
natIPSecSessionTranslatedLocalIp = _NatIPSecSessionTranslatedLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 8, 1, 3),
    _NatIPSecSessionTranslatedLocalIp_Type()
)
natIPSecSessionTranslatedLocalIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natIPSecSessionTranslatedLocalIp.setStatus("current")
_NatIPSecSessionOutsideIp_Type = IpAddress
_NatIPSecSessionOutsideIp_Object = MibTableColumn
natIPSecSessionOutsideIp = _NatIPSecSessionOutsideIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 8, 1, 4),
    _NatIPSecSessionOutsideIp_Type()
)
natIPSecSessionOutsideIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natIPSecSessionOutsideIp.setStatus("current")


class _NatIPSecSessionSPIInside_Type(Integer32):
    """Custom type natIPSecSessionSPIInside based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NatIPSecSessionSPIInside_Type.__name__ = "Integer32"
_NatIPSecSessionSPIInside_Object = MibTableColumn
natIPSecSessionSPIInside = _NatIPSecSessionSPIInside_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 8, 1, 5),
    _NatIPSecSessionSPIInside_Type()
)
natIPSecSessionSPIInside.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natIPSecSessionSPIInside.setStatus("current")


class _NatIPSecSessionSPIOutside_Type(Integer32):
    """Custom type natIPSecSessionSPIOutside based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NatIPSecSessionSPIOutside_Type.__name__ = "Integer32"
_NatIPSecSessionSPIOutside_Object = MibTableColumn
natIPSecSessionSPIOutside = _NatIPSecSessionSPIOutside_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 8, 1, 6),
    _NatIPSecSessionSPIOutside_Type()
)
natIPSecSessionSPIOutside.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natIPSecSessionSPIOutside.setStatus("current")
_NatIPSecSessionLastUseTime_Type = Integer32
_NatIPSecSessionLastUseTime_Object = MibTableColumn
natIPSecSessionLastUseTime = _NatIPSecSessionLastUseTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 8, 1, 7),
    _NatIPSecSessionLastUseTime_Type()
)
natIPSecSessionLastUseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natIPSecSessionLastUseTime.setStatus("current")
_NatIPSecSessionEntryStatus_Type = RowStatus
_NatIPSecSessionEntryStatus_Object = MibTableColumn
natIPSecSessionEntryStatus = _NatIPSecSessionEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 8, 1, 8),
    _NatIPSecSessionEntryStatus_Type()
)
natIPSecSessionEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natIPSecSessionEntryStatus.setStatus("current")
_NatIPSecPendingTable_Object = MibTable
natIPSecPendingTable = _NatIPSecPendingTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 9)
)
if mibBuilder.loadTexts:
    natIPSecPendingTable.setStatus("current")
_NatIPSecPendingEntry_Object = MibTableRow
natIPSecPendingEntry = _NatIPSecPendingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 9, 1)
)
natIPSecPendingEntry.setIndexNames(
    (0, "FutureNat-MIB", "natIPSecPendingInterfaceNum"),
    (0, "FutureNat-MIB", "natIPSecPendingLocalIp"),
    (0, "FutureNat-MIB", "natIPSecPendingOutsideIp"),
    (0, "FutureNat-MIB", "natIPSecPendingSPIInside"),
    (0, "FutureNat-MIB", "natIPSecPendingSPIOutside"),
)
if mibBuilder.loadTexts:
    natIPSecPendingEntry.setStatus("current")


class _NatIPSecPendingInterfaceNum_Type(Integer32):
    """Custom type natIPSecPendingInterfaceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NatIPSecPendingInterfaceNum_Type.__name__ = "Integer32"
_NatIPSecPendingInterfaceNum_Object = MibTableColumn
natIPSecPendingInterfaceNum = _NatIPSecPendingInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 9, 1, 1),
    _NatIPSecPendingInterfaceNum_Type()
)
natIPSecPendingInterfaceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natIPSecPendingInterfaceNum.setStatus("current")
_NatIPSecPendingLocalIp_Type = IpAddress
_NatIPSecPendingLocalIp_Object = MibTableColumn
natIPSecPendingLocalIp = _NatIPSecPendingLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 9, 1, 2),
    _NatIPSecPendingLocalIp_Type()
)
natIPSecPendingLocalIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natIPSecPendingLocalIp.setStatus("current")
_NatIPSecPendingTranslatedLocalIp_Type = IpAddress
_NatIPSecPendingTranslatedLocalIp_Object = MibTableColumn
natIPSecPendingTranslatedLocalIp = _NatIPSecPendingTranslatedLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 9, 1, 3),
    _NatIPSecPendingTranslatedLocalIp_Type()
)
natIPSecPendingTranslatedLocalIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natIPSecPendingTranslatedLocalIp.setStatus("current")
_NatIPSecPendingOutsideIp_Type = IpAddress
_NatIPSecPendingOutsideIp_Object = MibTableColumn
natIPSecPendingOutsideIp = _NatIPSecPendingOutsideIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 9, 1, 4),
    _NatIPSecPendingOutsideIp_Type()
)
natIPSecPendingOutsideIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natIPSecPendingOutsideIp.setStatus("current")


class _NatIPSecPendingSPIInside_Type(Integer32):
    """Custom type natIPSecPendingSPIInside based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NatIPSecPendingSPIInside_Type.__name__ = "Integer32"
_NatIPSecPendingSPIInside_Object = MibTableColumn
natIPSecPendingSPIInside = _NatIPSecPendingSPIInside_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 9, 1, 5),
    _NatIPSecPendingSPIInside_Type()
)
natIPSecPendingSPIInside.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natIPSecPendingSPIInside.setStatus("current")


class _NatIPSecPendingSPIOutside_Type(Integer32):
    """Custom type natIPSecPendingSPIOutside based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NatIPSecPendingSPIOutside_Type.__name__ = "Integer32"
_NatIPSecPendingSPIOutside_Object = MibTableColumn
natIPSecPendingSPIOutside = _NatIPSecPendingSPIOutside_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 9, 1, 6),
    _NatIPSecPendingSPIOutside_Type()
)
natIPSecPendingSPIOutside.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natIPSecPendingSPIOutside.setStatus("current")
_NatIPSecPendingLastUseTime_Type = Integer32
_NatIPSecPendingLastUseTime_Object = MibTableColumn
natIPSecPendingLastUseTime = _NatIPSecPendingLastUseTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 9, 1, 7),
    _NatIPSecPendingLastUseTime_Type()
)
natIPSecPendingLastUseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natIPSecPendingLastUseTime.setStatus("current")
_NatIPSecPendingNoOfRetry_Type = Integer32
_NatIPSecPendingNoOfRetry_Object = MibTableColumn
natIPSecPendingNoOfRetry = _NatIPSecPendingNoOfRetry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 9, 1, 8),
    _NatIPSecPendingNoOfRetry_Type()
)
natIPSecPendingNoOfRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natIPSecPendingNoOfRetry.setStatus("current")
_NatIPSecPendingEntryStatus_Type = RowStatus
_NatIPSecPendingEntryStatus_Object = MibTableColumn
natIPSecPendingEntryStatus = _NatIPSecPendingEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 9, 1, 9),
    _NatIPSecPendingEntryStatus_Type()
)
natIPSecPendingEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natIPSecPendingEntryStatus.setStatus("current")
_NatIKESessionTable_Object = MibTable
natIKESessionTable = _NatIKESessionTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 10)
)
if mibBuilder.loadTexts:
    natIKESessionTable.setStatus("current")
_NatIKESessionEntry_Object = MibTableRow
natIKESessionEntry = _NatIKESessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 10, 1)
)
natIKESessionEntry.setIndexNames(
    (0, "FutureNat-MIB", "natIKESessionInterfaceNum"),
    (0, "FutureNat-MIB", "natIKESessionLocalIp"),
    (0, "FutureNat-MIB", "natIKESessionOutsideIp"),
    (0, "FutureNat-MIB", "natIKESessionInitCookie"),
)
if mibBuilder.loadTexts:
    natIKESessionEntry.setStatus("current")


class _NatIKESessionInterfaceNum_Type(Integer32):
    """Custom type natIKESessionInterfaceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NatIKESessionInterfaceNum_Type.__name__ = "Integer32"
_NatIKESessionInterfaceNum_Object = MibTableColumn
natIKESessionInterfaceNum = _NatIKESessionInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 10, 1, 1),
    _NatIKESessionInterfaceNum_Type()
)
natIKESessionInterfaceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natIKESessionInterfaceNum.setStatus("current")
_NatIKESessionLocalIp_Type = IpAddress
_NatIKESessionLocalIp_Object = MibTableColumn
natIKESessionLocalIp = _NatIKESessionLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 10, 1, 2),
    _NatIKESessionLocalIp_Type()
)
natIKESessionLocalIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natIKESessionLocalIp.setStatus("current")
_NatIKESessionTranslatedLocalIp_Type = IpAddress
_NatIKESessionTranslatedLocalIp_Object = MibTableColumn
natIKESessionTranslatedLocalIp = _NatIKESessionTranslatedLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 10, 1, 3),
    _NatIKESessionTranslatedLocalIp_Type()
)
natIKESessionTranslatedLocalIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natIKESessionTranslatedLocalIp.setStatus("current")
_NatIKESessionOutsideIp_Type = IpAddress
_NatIKESessionOutsideIp_Object = MibTableColumn
natIKESessionOutsideIp = _NatIKESessionOutsideIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 10, 1, 4),
    _NatIKESessionOutsideIp_Type()
)
natIKESessionOutsideIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natIKESessionOutsideIp.setStatus("current")


class _NatIKESessionInitCookie_Type(OctetString):
    """Custom type natIKESessionInitCookie based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_NatIKESessionInitCookie_Type.__name__ = "OctetString"
_NatIKESessionInitCookie_Object = MibTableColumn
natIKESessionInitCookie = _NatIKESessionInitCookie_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 10, 1, 5),
    _NatIKESessionInitCookie_Type()
)
natIKESessionInitCookie.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natIKESessionInitCookie.setStatus("current")
_NatIKESessionLastUseTime_Type = Integer32
_NatIKESessionLastUseTime_Object = MibTableColumn
natIKESessionLastUseTime = _NatIKESessionLastUseTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 10, 1, 6),
    _NatIKESessionLastUseTime_Type()
)
natIKESessionLastUseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natIKESessionLastUseTime.setStatus("current")
_NatIKESessionEntryStatus_Type = RowStatus
_NatIKESessionEntryStatus_Object = MibTableColumn
natIKESessionEntryStatus = _NatIKESessionEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 10, 1, 7),
    _NatIKESessionEntryStatus_Type()
)
natIKESessionEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natIKESessionEntryStatus.setStatus("current")
_NatPortTrigInfoTable_Object = MibTable
natPortTrigInfoTable = _NatPortTrigInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 11)
)
if mibBuilder.loadTexts:
    natPortTrigInfoTable.setStatus("current")
_NatPortTrigInfoEntry_Object = MibTableRow
natPortTrigInfoEntry = _NatPortTrigInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 11, 1)
)
natPortTrigInfoEntry.setIndexNames(
    (0, "FutureNat-MIB", "natPortTrigInfoInBoundPortRange"),
    (0, "FutureNat-MIB", "natPortTrigInfoOutBoundPortRange"),
    (0, "FutureNat-MIB", "natPortTrigInfoProtocol"),
)
if mibBuilder.loadTexts:
    natPortTrigInfoEntry.setStatus("current")


class _NatPortTrigInfoAppName_Type(DisplayString):
    """Custom type natPortTrigInfoAppName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_NatPortTrigInfoAppName_Type.__name__ = "DisplayString"
_NatPortTrigInfoAppName_Object = MibTableColumn
natPortTrigInfoAppName = _NatPortTrigInfoAppName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 11, 1, 1),
    _NatPortTrigInfoAppName_Type()
)
natPortTrigInfoAppName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natPortTrigInfoAppName.setStatus("current")


class _NatPortTrigInfoInBoundPortRange_Type(DisplayString):
    """Custom type natPortTrigInfoInBoundPortRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 11),
    )


_NatPortTrigInfoInBoundPortRange_Type.__name__ = "DisplayString"
_NatPortTrigInfoInBoundPortRange_Object = MibTableColumn
natPortTrigInfoInBoundPortRange = _NatPortTrigInfoInBoundPortRange_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 11, 1, 2),
    _NatPortTrigInfoInBoundPortRange_Type()
)
natPortTrigInfoInBoundPortRange.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natPortTrigInfoInBoundPortRange.setStatus("current")


class _NatPortTrigInfoOutBoundPortRange_Type(DisplayString):
    """Custom type natPortTrigInfoOutBoundPortRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 11),
    )


_NatPortTrigInfoOutBoundPortRange_Type.__name__ = "DisplayString"
_NatPortTrigInfoOutBoundPortRange_Object = MibTableColumn
natPortTrigInfoOutBoundPortRange = _NatPortTrigInfoOutBoundPortRange_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 11, 1, 3),
    _NatPortTrigInfoOutBoundPortRange_Type()
)
natPortTrigInfoOutBoundPortRange.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natPortTrigInfoOutBoundPortRange.setStatus("current")


class _NatPortTrigInfoProtocol_Type(Integer32):
    """Custom type natPortTrigInfoProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              17,
              255)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 6),
          ("udp", 17),
          ("any", 255))
    )


_NatPortTrigInfoProtocol_Type.__name__ = "Integer32"
_NatPortTrigInfoProtocol_Object = MibTableColumn
natPortTrigInfoProtocol = _NatPortTrigInfoProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 11, 1, 4),
    _NatPortTrigInfoProtocol_Type()
)
natPortTrigInfoProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natPortTrigInfoProtocol.setStatus("current")
_NatPortTrigInfoEntryStatus_Type = RowStatus
_NatPortTrigInfoEntryStatus_Object = MibTableColumn
natPortTrigInfoEntryStatus = _NatPortTrigInfoEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 11, 1, 5),
    _NatPortTrigInfoEntryStatus_Type()
)
natPortTrigInfoEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natPortTrigInfoEntryStatus.setStatus("current")
_NatPolicyTable_Object = MibTable
natPolicyTable = _NatPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 12)
)
if mibBuilder.loadTexts:
    natPolicyTable.setStatus("current")
_NatPolicyEntry_Object = MibTableRow
natPolicyEntry = _NatPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 12, 1)
)
natPolicyEntry.setIndexNames(
    (0, "FutureNat-MIB", "natPolicyType"),
    (0, "FutureNat-MIB", "natPolicyId"),
    (0, "FutureNat-MIB", "natPolicyAclName"),
)
if mibBuilder.loadTexts:
    natPolicyEntry.setStatus("current")


class _NatPolicyType_Type(Integer32):
    """Custom type natPolicyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_NatPolicyType_Type.__name__ = "Integer32"
_NatPolicyType_Object = MibTableColumn
natPolicyType = _NatPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 12, 1, 1),
    _NatPolicyType_Type()
)
natPolicyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natPolicyType.setStatus("current")


class _NatPolicyId_Type(Integer32):
    """Custom type natPolicyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NatPolicyId_Type.__name__ = "Integer32"
_NatPolicyId_Object = MibTableColumn
natPolicyId = _NatPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 12, 1, 2),
    _NatPolicyId_Type()
)
natPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natPolicyId.setStatus("current")


class _NatPolicyAclName_Type(OctetString):
    """Custom type natPolicyAclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_NatPolicyAclName_Type.__name__ = "OctetString"
_NatPolicyAclName_Object = MibTableColumn
natPolicyAclName = _NatPolicyAclName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 12, 1, 3),
    _NatPolicyAclName_Type()
)
natPolicyAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natPolicyAclName.setStatus("current")
_NatPolicyTranslatedIp_Type = IpAddress
_NatPolicyTranslatedIp_Object = MibTableColumn
natPolicyTranslatedIp = _NatPolicyTranslatedIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 12, 1, 4),
    _NatPolicyTranslatedIp_Type()
)
natPolicyTranslatedIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natPolicyTranslatedIp.setStatus("current")
_NatPolicyEntryStatus_Type = RowStatus
_NatPolicyEntryStatus_Object = MibTableColumn
natPolicyEntryStatus = _NatPolicyEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 12, 1, 5),
    _NatPolicyEntryStatus_Type()
)
natPolicyEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natPolicyEntryStatus.setStatus("current")
_NatRsvdPortTrigInfoTable_Object = MibTable
natRsvdPortTrigInfoTable = _NatRsvdPortTrigInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 13)
)
if mibBuilder.loadTexts:
    natRsvdPortTrigInfoTable.setStatus("current")
_NatRsvdPortTrigInfoEntry_Object = MibTableRow
natRsvdPortTrigInfoEntry = _NatRsvdPortTrigInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 13, 1)
)
natRsvdPortTrigInfoEntry.setIndexNames(
    (0, "FutureNat-MIB", "natRsvdPortTrigInfoAppIndex"),
)
if mibBuilder.loadTexts:
    natRsvdPortTrigInfoEntry.setStatus("current")


class _NatRsvdPortTrigInfoAppIndex_Type(Integer32):
    """Custom type natRsvdPortTrigInfoAppIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_NatRsvdPortTrigInfoAppIndex_Type.__name__ = "Integer32"
_NatRsvdPortTrigInfoAppIndex_Object = MibTableColumn
natRsvdPortTrigInfoAppIndex = _NatRsvdPortTrigInfoAppIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 13, 1, 1),
    _NatRsvdPortTrigInfoAppIndex_Type()
)
natRsvdPortTrigInfoAppIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natRsvdPortTrigInfoAppIndex.setStatus("current")
_NatRsvdPortTrigInfoLocalIp_Type = IpAddress
_NatRsvdPortTrigInfoLocalIp_Object = MibTableColumn
natRsvdPortTrigInfoLocalIp = _NatRsvdPortTrigInfoLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 13, 1, 2),
    _NatRsvdPortTrigInfoLocalIp_Type()
)
natRsvdPortTrigInfoLocalIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natRsvdPortTrigInfoLocalIp.setStatus("current")
_NatRsvdPortTrigInfoRemoteIp_Type = IpAddress
_NatRsvdPortTrigInfoRemoteIp_Object = MibTableColumn
natRsvdPortTrigInfoRemoteIp = _NatRsvdPortTrigInfoRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 13, 1, 3),
    _NatRsvdPortTrigInfoRemoteIp_Type()
)
natRsvdPortTrigInfoRemoteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natRsvdPortTrigInfoRemoteIp.setStatus("current")


class _NatRsvdPortTrigInfoStartTime_Type(TimeStamp):
    """Custom type natRsvdPortTrigInfoStartTime based on TimeStamp"""
    defaultValue = 0


_NatRsvdPortTrigInfoStartTime_Type.__name__ = "TimeStamp"
_NatRsvdPortTrigInfoStartTime_Object = MibTableColumn
natRsvdPortTrigInfoStartTime = _NatRsvdPortTrigInfoStartTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 13, 1, 4),
    _NatRsvdPortTrigInfoStartTime_Type()
)
natRsvdPortTrigInfoStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natRsvdPortTrigInfoStartTime.setStatus("current")


class _NatRsvdPortTrigInfoAppName_Type(DisplayString):
    """Custom type natRsvdPortTrigInfoAppName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_NatRsvdPortTrigInfoAppName_Type.__name__ = "DisplayString"
_NatRsvdPortTrigInfoAppName_Object = MibTableColumn
natRsvdPortTrigInfoAppName = _NatRsvdPortTrigInfoAppName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 13, 1, 5),
    _NatRsvdPortTrigInfoAppName_Type()
)
natRsvdPortTrigInfoAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natRsvdPortTrigInfoAppName.setStatus("current")


class _NatRsvdPortTrigInfoInBoundPortRange_Type(DisplayString):
    """Custom type natRsvdPortTrigInfoInBoundPortRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 11),
    )


_NatRsvdPortTrigInfoInBoundPortRange_Type.__name__ = "DisplayString"
_NatRsvdPortTrigInfoInBoundPortRange_Object = MibTableColumn
natRsvdPortTrigInfoInBoundPortRange = _NatRsvdPortTrigInfoInBoundPortRange_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 13, 1, 6),
    _NatRsvdPortTrigInfoInBoundPortRange_Type()
)
natRsvdPortTrigInfoInBoundPortRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natRsvdPortTrigInfoInBoundPortRange.setStatus("current")


class _NatRsvdPortTrigInfoOutBoundPortRange_Type(DisplayString):
    """Custom type natRsvdPortTrigInfoOutBoundPortRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 11),
    )


_NatRsvdPortTrigInfoOutBoundPortRange_Type.__name__ = "DisplayString"
_NatRsvdPortTrigInfoOutBoundPortRange_Object = MibTableColumn
natRsvdPortTrigInfoOutBoundPortRange = _NatRsvdPortTrigInfoOutBoundPortRange_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 13, 1, 7),
    _NatRsvdPortTrigInfoOutBoundPortRange_Type()
)
natRsvdPortTrigInfoOutBoundPortRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natRsvdPortTrigInfoOutBoundPortRange.setStatus("current")


class _NatRsvdPortTrigInfoProtocol_Type(Integer32):
    """Custom type natRsvdPortTrigInfoProtocol based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              17,
              255)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 6),
          ("udp", 17),
          ("any", 255))
    )


_NatRsvdPortTrigInfoProtocol_Type.__name__ = "Integer32"
_NatRsvdPortTrigInfoProtocol_Object = MibTableColumn
natRsvdPortTrigInfoProtocol = _NatRsvdPortTrigInfoProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 14, 1, 13, 1, 8),
    _NatRsvdPortTrigInfoProtocol_Type()
)
natRsvdPortTrigInfoProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natRsvdPortTrigInfoProtocol.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FutureNat-MIB",
    **{"Status": Status,
       "futureNatMIB": futureNatMIB,
       "nat": nat,
       "natStatInfo": natStatInfo,
       "natEnable": natEnable,
       "natTypicalNumberOfEntries": natTypicalNumberOfEntries,
       "natTranslatedLocalPortStart": natTranslatedLocalPortStart,
       "natIdleTimeOut": natIdleTimeOut,
       "natTcpTimeOut": natTcpTimeOut,
       "natUdpTimeOut": natUdpTimeOut,
       "natTrcFlag": natTrcFlag,
       "natStatDynamicAllocFailureCount": natStatDynamicAllocFailureCount,
       "natStatTotalNumberOfTranslations": natStatTotalNumberOfTranslations,
       "natStatTotalNumberOfActiveSessions": natStatTotalNumberOfActiveSessions,
       "natStatTotalNumberOfPktsDropped": natStatTotalNumberOfPktsDropped,
       "natStatTotalNumberOfSessionsClosed": natStatTotalNumberOfSessionsClosed,
       "natIKEPortTranslation": natIKEPortTranslation,
       "natIKETimeout": natIKETimeout,
       "natIPSecTimeout": natIPSecTimeout,
       "natIPSecPendingTimeout": natIPSecPendingTimeout,
       "natIPSecMaxRetry": natIPSecMaxRetry,
       "sipAlgPort": sipAlgPort,
       "natSipAlgPartialEntryTimeOut": natSipAlgPartialEntryTimeOut,
       "natDynamicTransTable": natDynamicTransTable,
       "natDynamicTransEntry": natDynamicTransEntry,
       "natDynamicTransInterfaceNum": natDynamicTransInterfaceNum,
       "natDynamicTransLocalIp": natDynamicTransLocalIp,
       "natDynamicTransTranslatedLocalIp": natDynamicTransTranslatedLocalIp,
       "natDynamicTransLocalPort": natDynamicTransLocalPort,
       "natDynamicTransTranslatedLocalPort": natDynamicTransTranslatedLocalPort,
       "natDynamicTransOutsideIp": natDynamicTransOutsideIp,
       "natDynamicTransOutsidePort": natDynamicTransOutsidePort,
       "natDynamicTransLastUseTime": natDynamicTransLastUseTime,
       "natGlobalAddressTable": natGlobalAddressTable,
       "natGlobalAddressEntry": natGlobalAddressEntry,
       "natGlobalAddressInterfaceNum": natGlobalAddressInterfaceNum,
       "natGlobalAddressTranslatedLocalIp": natGlobalAddressTranslatedLocalIp,
       "natGlobalAddressMask": natGlobalAddressMask,
       "natGlobalAddressEntryStatus": natGlobalAddressEntryStatus,
       "natLocalAddressTable": natLocalAddressTable,
       "natLocalAddressEntry": natLocalAddressEntry,
       "natLocalAddressInterfaceNumber": natLocalAddressInterfaceNumber,
       "natLocalAddressLocalIp": natLocalAddressLocalIp,
       "natLocalAddressMask": natLocalAddressMask,
       "natLocalAddressEntryStatus": natLocalAddressEntryStatus,
       "natStaticTable": natStaticTable,
       "natStaticEntry": natStaticEntry,
       "natStaticInterfaceNum": natStaticInterfaceNum,
       "natStaticLocalIp": natStaticLocalIp,
       "natStaticTranslatedLocalIp": natStaticTranslatedLocalIp,
       "natStaticEntryStatus": natStaticEntryStatus,
       "natStaticNaptTable": natStaticNaptTable,
       "natStaticNaptEntry": natStaticNaptEntry,
       "natStaticNaptInterfaceNum": natStaticNaptInterfaceNum,
       "natStaticNaptLocalIp": natStaticNaptLocalIp,
       "natStaticNaptStartLocalPort": natStaticNaptStartLocalPort,
       "natStaticNaptEndLocalPort": natStaticNaptEndLocalPort,
       "natStaticNaptProtocolNumber": natStaticNaptProtocolNumber,
       "natStaticNaptTranslatedLocalIp": natStaticNaptTranslatedLocalIp,
       "natStaticNaptTranslatedLocalPort": natStaticNaptTranslatedLocalPort,
       "natStaticNaptDescription": natStaticNaptDescription,
       "natStaticNaptEntryStatus": natStaticNaptEntryStatus,
       "natIfTable": natIfTable,
       "natIfEntry": natIfEntry,
       "natIfInterfaceNumber": natIfInterfaceNumber,
       "natIfNat": natIfNat,
       "natIfNapt": natIfNapt,
       "natIfTwoWayNat": natIfTwoWayNat,
       "natIfEntryStatus": natIfEntryStatus,
       "natIPSecSessionTable": natIPSecSessionTable,
       "natIPSecSessionEntry": natIPSecSessionEntry,
       "natIPSecSessionInterfaceNum": natIPSecSessionInterfaceNum,
       "natIPSecSessionLocalIp": natIPSecSessionLocalIp,
       "natIPSecSessionTranslatedLocalIp": natIPSecSessionTranslatedLocalIp,
       "natIPSecSessionOutsideIp": natIPSecSessionOutsideIp,
       "natIPSecSessionSPIInside": natIPSecSessionSPIInside,
       "natIPSecSessionSPIOutside": natIPSecSessionSPIOutside,
       "natIPSecSessionLastUseTime": natIPSecSessionLastUseTime,
       "natIPSecSessionEntryStatus": natIPSecSessionEntryStatus,
       "natIPSecPendingTable": natIPSecPendingTable,
       "natIPSecPendingEntry": natIPSecPendingEntry,
       "natIPSecPendingInterfaceNum": natIPSecPendingInterfaceNum,
       "natIPSecPendingLocalIp": natIPSecPendingLocalIp,
       "natIPSecPendingTranslatedLocalIp": natIPSecPendingTranslatedLocalIp,
       "natIPSecPendingOutsideIp": natIPSecPendingOutsideIp,
       "natIPSecPendingSPIInside": natIPSecPendingSPIInside,
       "natIPSecPendingSPIOutside": natIPSecPendingSPIOutside,
       "natIPSecPendingLastUseTime": natIPSecPendingLastUseTime,
       "natIPSecPendingNoOfRetry": natIPSecPendingNoOfRetry,
       "natIPSecPendingEntryStatus": natIPSecPendingEntryStatus,
       "natIKESessionTable": natIKESessionTable,
       "natIKESessionEntry": natIKESessionEntry,
       "natIKESessionInterfaceNum": natIKESessionInterfaceNum,
       "natIKESessionLocalIp": natIKESessionLocalIp,
       "natIKESessionTranslatedLocalIp": natIKESessionTranslatedLocalIp,
       "natIKESessionOutsideIp": natIKESessionOutsideIp,
       "natIKESessionInitCookie": natIKESessionInitCookie,
       "natIKESessionLastUseTime": natIKESessionLastUseTime,
       "natIKESessionEntryStatus": natIKESessionEntryStatus,
       "natPortTrigInfoTable": natPortTrigInfoTable,
       "natPortTrigInfoEntry": natPortTrigInfoEntry,
       "natPortTrigInfoAppName": natPortTrigInfoAppName,
       "natPortTrigInfoInBoundPortRange": natPortTrigInfoInBoundPortRange,
       "natPortTrigInfoOutBoundPortRange": natPortTrigInfoOutBoundPortRange,
       "natPortTrigInfoProtocol": natPortTrigInfoProtocol,
       "natPortTrigInfoEntryStatus": natPortTrigInfoEntryStatus,
       "natPolicyTable": natPolicyTable,
       "natPolicyEntry": natPolicyEntry,
       "natPolicyType": natPolicyType,
       "natPolicyId": natPolicyId,
       "natPolicyAclName": natPolicyAclName,
       "natPolicyTranslatedIp": natPolicyTranslatedIp,
       "natPolicyEntryStatus": natPolicyEntryStatus,
       "natRsvdPortTrigInfoTable": natRsvdPortTrigInfoTable,
       "natRsvdPortTrigInfoEntry": natRsvdPortTrigInfoEntry,
       "natRsvdPortTrigInfoAppIndex": natRsvdPortTrigInfoAppIndex,
       "natRsvdPortTrigInfoLocalIp": natRsvdPortTrigInfoLocalIp,
       "natRsvdPortTrigInfoRemoteIp": natRsvdPortTrigInfoRemoteIp,
       "natRsvdPortTrigInfoStartTime": natRsvdPortTrigInfoStartTime,
       "natRsvdPortTrigInfoAppName": natRsvdPortTrigInfoAppName,
       "natRsvdPortTrigInfoInBoundPortRange": natRsvdPortTrigInfoInBoundPortRange,
       "natRsvdPortTrigInfoOutBoundPortRange": natRsvdPortTrigInfoOutBoundPortRange,
       "natRsvdPortTrigInfoProtocol": natRsvdPortTrigInfoProtocol}
)
