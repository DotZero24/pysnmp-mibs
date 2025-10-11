# SNMP MIB module (BIANCA-BRICK-PPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/bintec/BIANCA-BRICK-PPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:06:53 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Vpn_ObjectIdentity = ObjectIdentity
vpn = _Vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 23)
)
_PptpProfileTable_Object = MibTable
pptpProfileTable = _PptpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 1)
)
if mibBuilder.loadTexts:
    pptpProfileTable.setStatus("mandatory")
_PptpProfileEntry_Object = MibTableRow
pptpProfileEntry = _PptpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 1, 1)
)
pptpProfileEntry.setIndexNames(
    (0, "BIANCA-BRICK-PPTP-MIB", "pptpProfileId"),
)
if mibBuilder.loadTexts:
    pptpProfileEntry.setStatus("mandatory")


class _PptpProfileId_Type(Integer32):
    """Custom type pptpProfileId based on Integer32"""
    defaultValue = 0


_PptpProfileId_Type.__name__ = "Integer32"
_PptpProfileId_Object = MibTableColumn
pptpProfileId = _PptpProfileId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 1, 1, 1),
    _PptpProfileId_Type()
)
pptpProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpProfileId.setStatus("mandatory")


class _PptpProfileKeepalive_Type(Integer32):
    """Custom type pptpProfileKeepalive based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("delete", 3))
    )


_PptpProfileKeepalive_Type.__name__ = "Integer32"
_PptpProfileKeepalive_Object = MibTableColumn
pptpProfileKeepalive = _PptpProfileKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 1, 1, 2),
    _PptpProfileKeepalive_Type()
)
pptpProfileKeepalive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpProfileKeepalive.setStatus("mandatory")


class _PptpProfileMaxRequests_Type(Integer32):
    """Custom type pptpProfileMaxRequests based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PptpProfileMaxRequests_Type.__name__ = "Integer32"
_PptpProfileMaxRequests_Object = MibTableColumn
pptpProfileMaxRequests = _PptpProfileMaxRequests_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 1, 1, 3),
    _PptpProfileMaxRequests_Type()
)
pptpProfileMaxRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpProfileMaxRequests.setStatus("mandatory")


class _PptpProfileMaxBlockTime_Type(Integer32):
    """Custom type pptpProfileMaxBlockTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_PptpProfileMaxBlockTime_Type.__name__ = "Integer32"
_PptpProfileMaxBlockTime_Object = MibTableColumn
pptpProfileMaxBlockTime = _PptpProfileMaxBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 1, 1, 4),
    _PptpProfileMaxBlockTime_Type()
)
pptpProfileMaxBlockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpProfileMaxBlockTime.setStatus("mandatory")


class _PptpProfileMaxAckTimeout_Type(Integer32):
    """Custom type pptpProfileMaxAckTimeout based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 5000),
    )


_PptpProfileMaxAckTimeout_Type.__name__ = "Integer32"
_PptpProfileMaxAckTimeout_Object = MibTableColumn
pptpProfileMaxAckTimeout = _PptpProfileMaxAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 1, 1, 5),
    _PptpProfileMaxAckTimeout_Type()
)
pptpProfileMaxAckTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpProfileMaxAckTimeout.setStatus("mandatory")


class _PptpProfileReassemblyTimeout_Type(Integer32):
    """Custom type pptpProfileReassemblyTimeout based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_PptpProfileReassemblyTimeout_Type.__name__ = "Integer32"
_PptpProfileReassemblyTimeout_Object = MibTableColumn
pptpProfileReassemblyTimeout = _PptpProfileReassemblyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 1, 1, 6),
    _PptpProfileReassemblyTimeout_Type()
)
pptpProfileReassemblyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpProfileReassemblyTimeout.setStatus("mandatory")


class _PptpProfileMaxSWin_Type(Integer32):
    """Custom type pptpProfileMaxSWin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_PptpProfileMaxSWin_Type.__name__ = "Integer32"
_PptpProfileMaxSWin_Object = MibTableColumn
pptpProfileMaxSWin = _PptpProfileMaxSWin_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 1, 1, 7),
    _PptpProfileMaxSWin_Type()
)
pptpProfileMaxSWin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpProfileMaxSWin.setStatus("mandatory")


class _PptpProfileXmitWaitTime_Type(Integer32):
    """Custom type pptpProfileXmitWaitTime based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_PptpProfileXmitWaitTime_Type.__name__ = "Integer32"
_PptpProfileXmitWaitTime_Object = MibTableColumn
pptpProfileXmitWaitTime = _PptpProfileXmitWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 1, 1, 8),
    _PptpProfileXmitWaitTime_Type()
)
pptpProfileXmitWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpProfileXmitWaitTime.setStatus("mandatory")


class _PptpProfileMaxCtlConn_Type(Integer32):
    """Custom type pptpProfileMaxCtlConn based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_PptpProfileMaxCtlConn_Type.__name__ = "Integer32"
_PptpProfileMaxCtlConn_Object = MibTableColumn
pptpProfileMaxCtlConn = _PptpProfileMaxCtlConn_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 1, 1, 9),
    _PptpProfileMaxCtlConn_Type()
)
pptpProfileMaxCtlConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpProfileMaxCtlConn.setStatus("mandatory")


class _PptpProfileGreWindowAdaption_Type(Integer32):
    """Custom type pptpProfileGreWindowAdaption based on Integer32"""
    defaultValue = 1

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


_PptpProfileGreWindowAdaption_Type.__name__ = "Integer32"
_PptpProfileGreWindowAdaption_Object = MibTableColumn
pptpProfileGreWindowAdaption = _PptpProfileGreWindowAdaption_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 1, 1, 10),
    _PptpProfileGreWindowAdaption_Type()
)
pptpProfileGreWindowAdaption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpProfileGreWindowAdaption.setStatus("mandatory")
_PptpProfileHost_Type = DisplayString
_PptpProfileHost_Object = MibTableColumn
pptpProfileHost = _PptpProfileHost_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 1, 1, 11),
    _PptpProfileHost_Type()
)
pptpProfileHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpProfileHost.setStatus("mandatory")
_PptpProfileVendor_Type = DisplayString
_PptpProfileVendor_Object = MibTableColumn
pptpProfileVendor = _PptpProfileVendor_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 1, 1, 12),
    _PptpProfileVendor_Type()
)
pptpProfileVendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpProfileVendor.setStatus("mandatory")


class _PptpProfileFirmRev_Type(Integer32):
    """Custom type pptpProfileFirmRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 999),
    )


_PptpProfileFirmRev_Type.__name__ = "Integer32"
_PptpProfileFirmRev_Object = MibTableColumn
pptpProfileFirmRev = _PptpProfileFirmRev_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 1, 1, 13),
    _PptpProfileFirmRev_Type()
)
pptpProfileFirmRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpProfileFirmRev.setStatus("mandatory")
_PptpCtlConnTable_Object = MibTable
pptpCtlConnTable = _PptpCtlConnTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2)
)
if mibBuilder.loadTexts:
    pptpCtlConnTable.setStatus("mandatory")
_PptpCtlConnEntry_Object = MibTableRow
pptpCtlConnEntry = _PptpCtlConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1)
)
pptpCtlConnEntry.setIndexNames(
    (0, "BIANCA-BRICK-PPTP-MIB", "pptpCtlConnOriginator"),
)
if mibBuilder.loadTexts:
    pptpCtlConnEntry.setStatus("mandatory")


class _PptpCtlConnOriginator_Type(Integer32):
    """Custom type pptpCtlConnOriginator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_PptpCtlConnOriginator_Type.__name__ = "Integer32"
_PptpCtlConnOriginator_Object = MibTableColumn
pptpCtlConnOriginator = _PptpCtlConnOriginator_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 1),
    _PptpCtlConnOriginator_Type()
)
pptpCtlConnOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCtlConnOriginator.setStatus("mandatory")
_PptpCtlConnAge_Type = TimeTicks
_PptpCtlConnAge_Object = MibTableColumn
pptpCtlConnAge = _PptpCtlConnAge_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 2),
    _PptpCtlConnAge_Type()
)
pptpCtlConnAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCtlConnAge.setStatus("mandatory")


class _PptpCtlConnState_Type(Integer32):
    """Custom type pptpCtlConnState based on Integer32"""
    defaultValue = 1

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
        *(("idle", 1),
          ("wait-ctl-reply", 2),
          ("established", 3),
          ("wait-stop-reply", 4),
          ("close", 5),
          ("delete", 6))
    )


_PptpCtlConnState_Type.__name__ = "Integer32"
_PptpCtlConnState_Object = MibTableColumn
pptpCtlConnState = _PptpCtlConnState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 3),
    _PptpCtlConnState_Type()
)
pptpCtlConnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpCtlConnState.setStatus("mandatory")
_PptpCtlConnRemoteIpAddress_Type = IpAddress
_PptpCtlConnRemoteIpAddress_Object = MibTableColumn
pptpCtlConnRemoteIpAddress = _PptpCtlConnRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 4),
    _PptpCtlConnRemoteIpAddress_Type()
)
pptpCtlConnRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCtlConnRemoteIpAddress.setStatus("mandatory")
_PptpCtlConnLocalIpAddress_Type = IpAddress
_PptpCtlConnLocalIpAddress_Object = MibTableColumn
pptpCtlConnLocalIpAddress = _PptpCtlConnLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 5),
    _PptpCtlConnLocalIpAddress_Type()
)
pptpCtlConnLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCtlConnLocalIpAddress.setStatus("mandatory")
_PptpCtlConnVersion_Type = Integer32
_PptpCtlConnVersion_Object = MibTableColumn
pptpCtlConnVersion = _PptpCtlConnVersion_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 6),
    _PptpCtlConnVersion_Type()
)
pptpCtlConnVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCtlConnVersion.setStatus("mandatory")
_PptpCtlConnHost_Type = DisplayString
_PptpCtlConnHost_Object = MibTableColumn
pptpCtlConnHost = _PptpCtlConnHost_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 7),
    _PptpCtlConnHost_Type()
)
pptpCtlConnHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCtlConnHost.setStatus("mandatory")
_PptpCtlConnVendor_Type = DisplayString
_PptpCtlConnVendor_Object = MibTableColumn
pptpCtlConnVendor = _PptpCtlConnVendor_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 8),
    _PptpCtlConnVendor_Type()
)
pptpCtlConnVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCtlConnVendor.setStatus("mandatory")
_PptpCtlConnFirmRev_Type = Integer32
_PptpCtlConnFirmRev_Object = MibTableColumn
pptpCtlConnFirmRev = _PptpCtlConnFirmRev_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 9),
    _PptpCtlConnFirmRev_Type()
)
pptpCtlConnFirmRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCtlConnFirmRev.setStatus("mandatory")
_PptpCtlConnMaxChan_Type = Integer32
_PptpCtlConnMaxChan_Object = MibTableColumn
pptpCtlConnMaxChan = _PptpCtlConnMaxChan_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 10),
    _PptpCtlConnMaxChan_Type()
)
pptpCtlConnMaxChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCtlConnMaxChan.setStatus("mandatory")
_PptpCtlConnOutgoingCalls_Type = Integer32
_PptpCtlConnOutgoingCalls_Object = MibTableColumn
pptpCtlConnOutgoingCalls = _PptpCtlConnOutgoingCalls_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 11),
    _PptpCtlConnOutgoingCalls_Type()
)
pptpCtlConnOutgoingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCtlConnOutgoingCalls.setStatus("mandatory")
_PptpCtlConnIncomingCalls_Type = Integer32
_PptpCtlConnIncomingCalls_Object = MibTableColumn
pptpCtlConnIncomingCalls = _PptpCtlConnIncomingCalls_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 12),
    _PptpCtlConnIncomingCalls_Type()
)
pptpCtlConnIncomingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCtlConnIncomingCalls.setStatus("mandatory")
_PptpCtlConnOutgoingFails_Type = Integer32
_PptpCtlConnOutgoingFails_Object = MibTableColumn
pptpCtlConnOutgoingFails = _PptpCtlConnOutgoingFails_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 13),
    _PptpCtlConnOutgoingFails_Type()
)
pptpCtlConnOutgoingFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCtlConnOutgoingFails.setStatus("mandatory")
_PptpCtlConnIncomingFails_Type = Integer32
_PptpCtlConnIncomingFails_Object = MibTableColumn
pptpCtlConnIncomingFails = _PptpCtlConnIncomingFails_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 14),
    _PptpCtlConnIncomingFails_Type()
)
pptpCtlConnIncomingFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCtlConnIncomingFails.setStatus("mandatory")
_PptpCtlConnEchoReqSent_Type = Integer32
_PptpCtlConnEchoReqSent_Object = MibTableColumn
pptpCtlConnEchoReqSent = _PptpCtlConnEchoReqSent_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 15),
    _PptpCtlConnEchoReqSent_Type()
)
pptpCtlConnEchoReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCtlConnEchoReqSent.setStatus("mandatory")
_PptpCtlConnEchoReqRcvd_Type = Integer32
_PptpCtlConnEchoReqRcvd_Object = MibTableColumn
pptpCtlConnEchoReqRcvd = _PptpCtlConnEchoReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 16),
    _PptpCtlConnEchoReqRcvd_Type()
)
pptpCtlConnEchoReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCtlConnEchoReqRcvd.setStatus("mandatory")
_PptpCtlConnEchoRepSent_Type = Integer32
_PptpCtlConnEchoRepSent_Object = MibTableColumn
pptpCtlConnEchoRepSent = _PptpCtlConnEchoRepSent_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 17),
    _PptpCtlConnEchoRepSent_Type()
)
pptpCtlConnEchoRepSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCtlConnEchoRepSent.setStatus("mandatory")
_PptpCtlConnEchoRepRcvd_Type = Integer32
_PptpCtlConnEchoRepRcvd_Object = MibTableColumn
pptpCtlConnEchoRepRcvd = _PptpCtlConnEchoRepRcvd_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 18),
    _PptpCtlConnEchoRepRcvd_Type()
)
pptpCtlConnEchoRepRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCtlConnEchoRepRcvd.setStatus("mandatory")
_PptpCtlConnEchoReqPending_Type = Integer32
_PptpCtlConnEchoReqPending_Object = MibTableColumn
pptpCtlConnEchoReqPending = _PptpCtlConnEchoReqPending_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 19),
    _PptpCtlConnEchoReqPending_Type()
)
pptpCtlConnEchoReqPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCtlConnEchoReqPending.setStatus("mandatory")
_PptpCallTable_Object = MibTable
pptpCallTable = _PptpCallTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3)
)
if mibBuilder.loadTexts:
    pptpCallTable.setStatus("mandatory")
_PptpCallEntry_Object = MibTableRow
pptpCallEntry = _PptpCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1)
)
pptpCallEntry.setIndexNames(
    (0, "BIANCA-BRICK-PPTP-MIB", "pptpCallType"),
)
if mibBuilder.loadTexts:
    pptpCallEntry.setStatus("mandatory")


class _PptpCallType_Type(Integer32):
    """Custom type pptpCallType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pac", 1),
          ("pns", 2))
    )


_PptpCallType_Type.__name__ = "Integer32"
_PptpCallType_Object = MibTableColumn
pptpCallType = _PptpCallType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 1),
    _PptpCallType_Type()
)
pptpCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallType.setStatus("mandatory")


class _PptpCallDirection_Type(Integer32):
    """Custom type pptpCallDirection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2))
    )


_PptpCallDirection_Type.__name__ = "Integer32"
_PptpCallDirection_Object = MibTableColumn
pptpCallDirection = _PptpCallDirection_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 2),
    _PptpCallDirection_Type()
)
pptpCallDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallDirection.setStatus("mandatory")
_PptpCallAge_Type = TimeTicks
_PptpCallAge_Object = MibTableColumn
pptpCallAge = _PptpCallAge_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 3),
    _PptpCallAge_Type()
)
pptpCallAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallAge.setStatus("mandatory")


class _PptpCallState_Type(Integer32):
    """Custom type pptpCallState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("wait-cs-ans", 2),
          ("wait-reply", 3),
          ("wait-connect", 4),
          ("established", 5),
          ("wait-disc", 6),
          ("close", 7),
          ("delete", 8))
    )


_PptpCallState_Type.__name__ = "Integer32"
_PptpCallState_Object = MibTableColumn
pptpCallState = _PptpCallState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 4),
    _PptpCallState_Type()
)
pptpCallState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpCallState.setStatus("mandatory")
_PptpCallRemoteIpAddress_Type = IpAddress
_PptpCallRemoteIpAddress_Object = MibTableColumn
pptpCallRemoteIpAddress = _PptpCallRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 5),
    _PptpCallRemoteIpAddress_Type()
)
pptpCallRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallRemoteIpAddress.setStatus("mandatory")
_PptpCallLocalIpAddress_Type = IpAddress
_PptpCallLocalIpAddress_Object = MibTableColumn
pptpCallLocalIpAddress = _PptpCallLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 6),
    _PptpCallLocalIpAddress_Type()
)
pptpCallLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallLocalIpAddress.setStatus("mandatory")
_PptpCallReceivedPackets_Type = Counter32
_PptpCallReceivedPackets_Object = MibTableColumn
pptpCallReceivedPackets = _PptpCallReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 7),
    _PptpCallReceivedPackets_Type()
)
pptpCallReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallReceivedPackets.setStatus("mandatory")
_PptpCallReceivedOctets_Type = Counter32
_PptpCallReceivedOctets_Object = MibTableColumn
pptpCallReceivedOctets = _PptpCallReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 8),
    _PptpCallReceivedOctets_Type()
)
pptpCallReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallReceivedOctets.setStatus("mandatory")
_PptpCallReceivedErrors_Type = Counter32
_PptpCallReceivedErrors_Object = MibTableColumn
pptpCallReceivedErrors = _PptpCallReceivedErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 9),
    _PptpCallReceivedErrors_Type()
)
pptpCallReceivedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallReceivedErrors.setStatus("mandatory")
_PptpCallTransmitPackets_Type = Counter32
_PptpCallTransmitPackets_Object = MibTableColumn
pptpCallTransmitPackets = _PptpCallTransmitPackets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 10),
    _PptpCallTransmitPackets_Type()
)
pptpCallTransmitPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallTransmitPackets.setStatus("mandatory")
_PptpCallTransmitOctets_Type = Counter32
_PptpCallTransmitOctets_Object = MibTableColumn
pptpCallTransmitOctets = _PptpCallTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 11),
    _PptpCallTransmitOctets_Type()
)
pptpCallTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallTransmitOctets.setStatus("mandatory")
_PptpCallTransmitErrors_Type = Counter32
_PptpCallTransmitErrors_Object = MibTableColumn
pptpCallTransmitErrors = _PptpCallTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 12),
    _PptpCallTransmitErrors_Type()
)
pptpCallTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallTransmitErrors.setStatus("mandatory")
_PptpCallInfo_Type = DisplayString
_PptpCallInfo_Object = MibTableColumn
pptpCallInfo = _PptpCallInfo_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 13),
    _PptpCallInfo_Type()
)
pptpCallInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallInfo.setStatus("mandatory")
_PptpCallLocId_Type = Integer32
_PptpCallLocId_Object = MibTableColumn
pptpCallLocId = _PptpCallLocId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 14),
    _PptpCallLocId_Type()
)
pptpCallLocId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallLocId.setStatus("mandatory")
_PptpCallRemId_Type = Integer32
_PptpCallRemId_Object = MibTableColumn
pptpCallRemId = _PptpCallRemId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 15),
    _PptpCallRemId_Type()
)
pptpCallRemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallRemId.setStatus("mandatory")
_PptpCallSerial_Type = Integer32
_PptpCallSerial_Object = MibTableColumn
pptpCallSerial = _PptpCallSerial_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 16),
    _PptpCallSerial_Type()
)
pptpCallSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallSerial.setStatus("mandatory")


class _PptpCallSWin_Type(Integer32):
    """Custom type pptpCallSWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_PptpCallSWin_Type.__name__ = "Integer32"
_PptpCallSWin_Object = MibTableColumn
pptpCallSWin = _PptpCallSWin_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 17),
    _PptpCallSWin_Type()
)
pptpCallSWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallSWin.setStatus("mandatory")


class _PptpCallGreWindowAdaption_Type(Integer32):
    """Custom type pptpCallGreWindowAdaption based on Integer32"""
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


_PptpCallGreWindowAdaption_Type.__name__ = "Integer32"
_PptpCallGreWindowAdaption_Object = MibTableColumn
pptpCallGreWindowAdaption = _PptpCallGreWindowAdaption_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 18),
    _PptpCallGreWindowAdaption_Type()
)
pptpCallGreWindowAdaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallGreWindowAdaption.setStatus("mandatory")
_PptpCallAssociatedIfIndex_Type = Integer32
_PptpCallAssociatedIfIndex_Object = MibTableColumn
pptpCallAssociatedIfIndex = _PptpCallAssociatedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 19),
    _PptpCallAssociatedIfIndex_Type()
)
pptpCallAssociatedIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pptpCallAssociatedIfIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-PPTP-MIB",
    **{"bintec": bintec,
       "bibo": bibo,
       "vpn": vpn,
       "pptpProfileTable": pptpProfileTable,
       "pptpProfileEntry": pptpProfileEntry,
       "pptpProfileId": pptpProfileId,
       "pptpProfileKeepalive": pptpProfileKeepalive,
       "pptpProfileMaxRequests": pptpProfileMaxRequests,
       "pptpProfileMaxBlockTime": pptpProfileMaxBlockTime,
       "pptpProfileMaxAckTimeout": pptpProfileMaxAckTimeout,
       "pptpProfileReassemblyTimeout": pptpProfileReassemblyTimeout,
       "pptpProfileMaxSWin": pptpProfileMaxSWin,
       "pptpProfileXmitWaitTime": pptpProfileXmitWaitTime,
       "pptpProfileMaxCtlConn": pptpProfileMaxCtlConn,
       "pptpProfileGreWindowAdaption": pptpProfileGreWindowAdaption,
       "pptpProfileHost": pptpProfileHost,
       "pptpProfileVendor": pptpProfileVendor,
       "pptpProfileFirmRev": pptpProfileFirmRev,
       "pptpCtlConnTable": pptpCtlConnTable,
       "pptpCtlConnEntry": pptpCtlConnEntry,
       "pptpCtlConnOriginator": pptpCtlConnOriginator,
       "pptpCtlConnAge": pptpCtlConnAge,
       "pptpCtlConnState": pptpCtlConnState,
       "pptpCtlConnRemoteIpAddress": pptpCtlConnRemoteIpAddress,
       "pptpCtlConnLocalIpAddress": pptpCtlConnLocalIpAddress,
       "pptpCtlConnVersion": pptpCtlConnVersion,
       "pptpCtlConnHost": pptpCtlConnHost,
       "pptpCtlConnVendor": pptpCtlConnVendor,
       "pptpCtlConnFirmRev": pptpCtlConnFirmRev,
       "pptpCtlConnMaxChan": pptpCtlConnMaxChan,
       "pptpCtlConnOutgoingCalls": pptpCtlConnOutgoingCalls,
       "pptpCtlConnIncomingCalls": pptpCtlConnIncomingCalls,
       "pptpCtlConnOutgoingFails": pptpCtlConnOutgoingFails,
       "pptpCtlConnIncomingFails": pptpCtlConnIncomingFails,
       "pptpCtlConnEchoReqSent": pptpCtlConnEchoReqSent,
       "pptpCtlConnEchoReqRcvd": pptpCtlConnEchoReqRcvd,
       "pptpCtlConnEchoRepSent": pptpCtlConnEchoRepSent,
       "pptpCtlConnEchoRepRcvd": pptpCtlConnEchoRepRcvd,
       "pptpCtlConnEchoReqPending": pptpCtlConnEchoReqPending,
       "pptpCallTable": pptpCallTable,
       "pptpCallEntry": pptpCallEntry,
       "pptpCallType": pptpCallType,
       "pptpCallDirection": pptpCallDirection,
       "pptpCallAge": pptpCallAge,
       "pptpCallState": pptpCallState,
       "pptpCallRemoteIpAddress": pptpCallRemoteIpAddress,
       "pptpCallLocalIpAddress": pptpCallLocalIpAddress,
       "pptpCallReceivedPackets": pptpCallReceivedPackets,
       "pptpCallReceivedOctets": pptpCallReceivedOctets,
       "pptpCallReceivedErrors": pptpCallReceivedErrors,
       "pptpCallTransmitPackets": pptpCallTransmitPackets,
       "pptpCallTransmitOctets": pptpCallTransmitOctets,
       "pptpCallTransmitErrors": pptpCallTransmitErrors,
       "pptpCallInfo": pptpCallInfo,
       "pptpCallLocId": pptpCallLocId,
       "pptpCallRemId": pptpCallRemId,
       "pptpCallSerial": pptpCallSerial,
       "pptpCallSWin": pptpCallSWin,
       "pptpCallGreWindowAdaption": pptpCallGreWindowAdaption,
       "pptpCallAssociatedIfIndex": pptpCallAssociatedIfIndex}
)
