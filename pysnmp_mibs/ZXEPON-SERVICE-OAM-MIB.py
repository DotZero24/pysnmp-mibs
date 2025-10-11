# SNMP MIB module (ZXEPON-SERVICE-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZXEPON-SERVICE-OAM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:40 2025
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(zxAnEponMib,) = mibBuilder.importSymbols(
    "ZTE-MASTER-MIB",
    "zxAnEponMib")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class Dot3Oui(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3



# MIB Managed Objects in the order of their OIDs

_Dot3OamObjects_ObjectIdentity = ObjectIdentity
dot3OamObjects = _Dot3OamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6)
)
_Dot3OamTable_Object = MibTable
dot3OamTable = _Dot3OamTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 1)
)
if mibBuilder.loadTexts:
    dot3OamTable.setStatus("current")
_Dot3OamEntry_Object = MibTableRow
dot3OamEntry = _Dot3OamEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 1, 1)
)
dot3OamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot3OamEntry.setStatus("current")


class _Dot3OamAdminState_Type(Integer32):
    """Custom type dot3OamAdminState based on Integer32"""
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


_Dot3OamAdminState_Type.__name__ = "Integer32"
_Dot3OamAdminState_Object = MibTableColumn
dot3OamAdminState = _Dot3OamAdminState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 1, 1, 1),
    _Dot3OamAdminState_Type()
)
dot3OamAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3OamAdminState.setStatus("current")


class _Dot3OamOperStatus_Type(Integer32):
    """Custom type dot3OamOperStatus based on Integer32"""
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
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("linkFault", 2),
          ("passiveWait", 3),
          ("activeSendLocal", 4),
          ("sendLocalAndRemote", 5),
          ("sendLocalAndRemoteOk", 6),
          ("oamPeeringLocallyRejected", 7),
          ("oamPeeringRemotelyRejected", 8),
          ("operational", 9),
          ("nonOperHalfDuplex", 10))
    )


_Dot3OamOperStatus_Type.__name__ = "Integer32"
_Dot3OamOperStatus_Object = MibTableColumn
dot3OamOperStatus = _Dot3OamOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 1, 1, 2),
    _Dot3OamOperStatus_Type()
)
dot3OamOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamOperStatus.setStatus("current")


class _Dot3OamMode_Type(Integer32):
    """Custom type dot3OamMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passive", 1),
          ("active", 2))
    )


_Dot3OamMode_Type.__name__ = "Integer32"
_Dot3OamMode_Object = MibTableColumn
dot3OamMode = _Dot3OamMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 1, 1, 3),
    _Dot3OamMode_Type()
)
dot3OamMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3OamMode.setStatus("current")


class _Dot3OamMaxOamPduSize_Type(Unsigned32):
    """Custom type dot3OamMaxOamPduSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1518),
    )


_Dot3OamMaxOamPduSize_Type.__name__ = "Unsigned32"
_Dot3OamMaxOamPduSize_Object = MibTableColumn
dot3OamMaxOamPduSize = _Dot3OamMaxOamPduSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 1, 1, 4),
    _Dot3OamMaxOamPduSize_Type()
)
dot3OamMaxOamPduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamMaxOamPduSize.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamMaxOamPduSize.setUnits("octets")


class _Dot3OamConfigRevision_Type(Unsigned32):
    """Custom type dot3OamConfigRevision based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3OamConfigRevision_Type.__name__ = "Unsigned32"
_Dot3OamConfigRevision_Object = MibTableColumn
dot3OamConfigRevision = _Dot3OamConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 1, 1, 5),
    _Dot3OamConfigRevision_Type()
)
dot3OamConfigRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamConfigRevision.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamConfigRevision.setUnits("octets")


class _Dot3OamFunctionsSupported_Type(Bits):
    """Custom type dot3OamFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        *(("unidirectionalSupport", 0),
          ("loopbackSupport", 1),
          ("eventSupport", 2),
          ("variableSupport", 3))
    )

_Dot3OamFunctionsSupported_Type.__name__ = "Bits"
_Dot3OamFunctionsSupported_Object = MibTableColumn
dot3OamFunctionsSupported = _Dot3OamFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 1, 1, 6),
    _Dot3OamFunctionsSupported_Type()
)
dot3OamFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamFunctionsSupported.setStatus("current")
_Dot3OamPeerTable_Object = MibTable
dot3OamPeerTable = _Dot3OamPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 2)
)
if mibBuilder.loadTexts:
    dot3OamPeerTable.setStatus("current")
_Dot3OamPeerEntry_Object = MibTableRow
dot3OamPeerEntry = _Dot3OamPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 2, 1)
)
dot3OamPeerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot3OamPeerEntry.setStatus("current")
_Dot3OamPeerMacAddress_Type = MacAddress
_Dot3OamPeerMacAddress_Object = MibTableColumn
dot3OamPeerMacAddress = _Dot3OamPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 2, 1, 1),
    _Dot3OamPeerMacAddress_Type()
)
dot3OamPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamPeerMacAddress.setStatus("current")
_Dot3OamPeerVendorOui_Type = Dot3Oui
_Dot3OamPeerVendorOui_Object = MibTableColumn
dot3OamPeerVendorOui = _Dot3OamPeerVendorOui_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 2, 1, 2),
    _Dot3OamPeerVendorOui_Type()
)
dot3OamPeerVendorOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamPeerVendorOui.setStatus("current")
_Dot3OamPeerVendorInfo_Type = Unsigned32
_Dot3OamPeerVendorInfo_Object = MibTableColumn
dot3OamPeerVendorInfo = _Dot3OamPeerVendorInfo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 2, 1, 3),
    _Dot3OamPeerVendorInfo_Type()
)
dot3OamPeerVendorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamPeerVendorInfo.setStatus("current")


class _Dot3OamPeerMode_Type(Integer32):
    """Custom type dot3OamPeerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("passive", 1),
          ("active", 2),
          ("unknown", 3))
    )


_Dot3OamPeerMode_Type.__name__ = "Integer32"
_Dot3OamPeerMode_Object = MibTableColumn
dot3OamPeerMode = _Dot3OamPeerMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 2, 1, 4),
    _Dot3OamPeerMode_Type()
)
dot3OamPeerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamPeerMode.setStatus("current")


class _Dot3OamPeerMaxOamPduSize_Type(Unsigned32):
    """Custom type dot3OamPeerMaxOamPduSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 1518),
    )


_Dot3OamPeerMaxOamPduSize_Type.__name__ = "Unsigned32"
_Dot3OamPeerMaxOamPduSize_Object = MibTableColumn
dot3OamPeerMaxOamPduSize = _Dot3OamPeerMaxOamPduSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 2, 1, 5),
    _Dot3OamPeerMaxOamPduSize_Type()
)
dot3OamPeerMaxOamPduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamPeerMaxOamPduSize.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamPeerMaxOamPduSize.setUnits("octets")


class _Dot3OamPeerConfigRevision_Type(Unsigned32):
    """Custom type dot3OamPeerConfigRevision based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3OamPeerConfigRevision_Type.__name__ = "Unsigned32"
_Dot3OamPeerConfigRevision_Object = MibTableColumn
dot3OamPeerConfigRevision = _Dot3OamPeerConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 2, 1, 6),
    _Dot3OamPeerConfigRevision_Type()
)
dot3OamPeerConfigRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamPeerConfigRevision.setStatus("current")


class _Dot3OamPeerFunctionsSupported_Type(Bits):
    """Custom type dot3OamPeerFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        *(("unidirectionalSupport", 0),
          ("loopbackSupport", 1),
          ("eventSupport", 2),
          ("variableSupport", 3))
    )

_Dot3OamPeerFunctionsSupported_Type.__name__ = "Bits"
_Dot3OamPeerFunctionsSupported_Object = MibTableColumn
dot3OamPeerFunctionsSupported = _Dot3OamPeerFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 2, 1, 7),
    _Dot3OamPeerFunctionsSupported_Type()
)
dot3OamPeerFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamPeerFunctionsSupported.setStatus("current")
_Dot3OamLoopbackTable_Object = MibTable
dot3OamLoopbackTable = _Dot3OamLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 3)
)
if mibBuilder.loadTexts:
    dot3OamLoopbackTable.setStatus("current")
_Dot3OamLoopbackEntry_Object = MibTableRow
dot3OamLoopbackEntry = _Dot3OamLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 3, 1)
)
dot3OamLoopbackEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot3OamLoopbackEntry.setStatus("current")


class _Dot3OamLoopbackStatus_Type(Integer32):
    """Custom type dot3OamLoopbackStatus based on Integer32"""
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
        *(("noLoopback", 1),
          ("initiatingLoopback", 2),
          ("remoteLoopback", 3),
          ("terminatingLoopback", 4),
          ("localLoopback", 5),
          ("unknown", 6))
    )


_Dot3OamLoopbackStatus_Type.__name__ = "Integer32"
_Dot3OamLoopbackStatus_Object = MibTableColumn
dot3OamLoopbackStatus = _Dot3OamLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 3, 1, 1),
    _Dot3OamLoopbackStatus_Type()
)
dot3OamLoopbackStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3OamLoopbackStatus.setStatus("current")


class _Dot3OamLoopbackIgnoreRx_Type(Integer32):
    """Custom type dot3OamLoopbackIgnoreRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("process", 2))
    )


_Dot3OamLoopbackIgnoreRx_Type.__name__ = "Integer32"
_Dot3OamLoopbackIgnoreRx_Object = MibTableColumn
dot3OamLoopbackIgnoreRx = _Dot3OamLoopbackIgnoreRx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 3, 1, 2),
    _Dot3OamLoopbackIgnoreRx_Type()
)
dot3OamLoopbackIgnoreRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3OamLoopbackIgnoreRx.setStatus("current")
_Dot3OamStatsTable_Object = MibTable
dot3OamStatsTable = _Dot3OamStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 4)
)
if mibBuilder.loadTexts:
    dot3OamStatsTable.setStatus("current")
_Dot3OamStatsEntry_Object = MibTableRow
dot3OamStatsEntry = _Dot3OamStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 4, 1)
)
dot3OamStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot3OamStatsEntry.setStatus("current")
_Dot3OamInformationTx_Type = Counter32
_Dot3OamInformationTx_Object = MibTableColumn
dot3OamInformationTx = _Dot3OamInformationTx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 4, 1, 1),
    _Dot3OamInformationTx_Type()
)
dot3OamInformationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamInformationTx.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamInformationTx.setUnits("frames")
_Dot3OamInformationRx_Type = Counter32
_Dot3OamInformationRx_Object = MibTableColumn
dot3OamInformationRx = _Dot3OamInformationRx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 4, 1, 2),
    _Dot3OamInformationRx_Type()
)
dot3OamInformationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamInformationRx.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamInformationRx.setUnits("frames")
_Dot3OamUniqueEventNotificationTx_Type = Counter32
_Dot3OamUniqueEventNotificationTx_Object = MibTableColumn
dot3OamUniqueEventNotificationTx = _Dot3OamUniqueEventNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 4, 1, 3),
    _Dot3OamUniqueEventNotificationTx_Type()
)
dot3OamUniqueEventNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamUniqueEventNotificationTx.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamUniqueEventNotificationTx.setUnits("frames")
_Dot3OamUniqueEventNotificationRx_Type = Counter32
_Dot3OamUniqueEventNotificationRx_Object = MibTableColumn
dot3OamUniqueEventNotificationRx = _Dot3OamUniqueEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 4, 1, 4),
    _Dot3OamUniqueEventNotificationRx_Type()
)
dot3OamUniqueEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamUniqueEventNotificationRx.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamUniqueEventNotificationRx.setUnits("frames")
_Dot3OamDuplicateEventNotificationTx_Type = Counter32
_Dot3OamDuplicateEventNotificationTx_Object = MibTableColumn
dot3OamDuplicateEventNotificationTx = _Dot3OamDuplicateEventNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 4, 1, 5),
    _Dot3OamDuplicateEventNotificationTx_Type()
)
dot3OamDuplicateEventNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamDuplicateEventNotificationTx.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamDuplicateEventNotificationTx.setUnits("frames")
_Dot3OamDuplicateEventNotificationRx_Type = Counter32
_Dot3OamDuplicateEventNotificationRx_Object = MibTableColumn
dot3OamDuplicateEventNotificationRx = _Dot3OamDuplicateEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 4, 1, 6),
    _Dot3OamDuplicateEventNotificationRx_Type()
)
dot3OamDuplicateEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamDuplicateEventNotificationRx.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamDuplicateEventNotificationRx.setUnits("frames")
_Dot3OamLoopbackControlTx_Type = Counter32
_Dot3OamLoopbackControlTx_Object = MibTableColumn
dot3OamLoopbackControlTx = _Dot3OamLoopbackControlTx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 4, 1, 7),
    _Dot3OamLoopbackControlTx_Type()
)
dot3OamLoopbackControlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamLoopbackControlTx.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamLoopbackControlTx.setUnits("frames")
_Dot3OamLoopbackControlRx_Type = Counter32
_Dot3OamLoopbackControlRx_Object = MibTableColumn
dot3OamLoopbackControlRx = _Dot3OamLoopbackControlRx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 4, 1, 8),
    _Dot3OamLoopbackControlRx_Type()
)
dot3OamLoopbackControlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamLoopbackControlRx.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamLoopbackControlRx.setUnits("frames")
_Dot3OamVariableRequestTx_Type = Counter32
_Dot3OamVariableRequestTx_Object = MibTableColumn
dot3OamVariableRequestTx = _Dot3OamVariableRequestTx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 4, 1, 9),
    _Dot3OamVariableRequestTx_Type()
)
dot3OamVariableRequestTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamVariableRequestTx.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamVariableRequestTx.setUnits("frames")
_Dot3OamVariableRequestRx_Type = Counter32
_Dot3OamVariableRequestRx_Object = MibTableColumn
dot3OamVariableRequestRx = _Dot3OamVariableRequestRx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 4, 1, 10),
    _Dot3OamVariableRequestRx_Type()
)
dot3OamVariableRequestRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamVariableRequestRx.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamVariableRequestRx.setUnits("frames")
_Dot3OamVariableResponseTx_Type = Counter32
_Dot3OamVariableResponseTx_Object = MibTableColumn
dot3OamVariableResponseTx = _Dot3OamVariableResponseTx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 4, 1, 11),
    _Dot3OamVariableResponseTx_Type()
)
dot3OamVariableResponseTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamVariableResponseTx.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamVariableResponseTx.setUnits("frames")
_Dot3OamVariableResponseRx_Type = Counter32
_Dot3OamVariableResponseRx_Object = MibTableColumn
dot3OamVariableResponseRx = _Dot3OamVariableResponseRx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 4, 1, 12),
    _Dot3OamVariableResponseRx_Type()
)
dot3OamVariableResponseRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamVariableResponseRx.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamVariableResponseRx.setUnits("frames")
_Dot3OamOrgSpecificTx_Type = Counter32
_Dot3OamOrgSpecificTx_Object = MibTableColumn
dot3OamOrgSpecificTx = _Dot3OamOrgSpecificTx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 4, 1, 13),
    _Dot3OamOrgSpecificTx_Type()
)
dot3OamOrgSpecificTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamOrgSpecificTx.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamOrgSpecificTx.setUnits("frames")
_Dot3OamOrgSpecificRx_Type = Counter32
_Dot3OamOrgSpecificRx_Object = MibTableColumn
dot3OamOrgSpecificRx = _Dot3OamOrgSpecificRx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 4, 1, 14),
    _Dot3OamOrgSpecificRx_Type()
)
dot3OamOrgSpecificRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamOrgSpecificRx.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamOrgSpecificRx.setUnits("frames")
_Dot3OamUnsupportedCodesTx_Type = Counter32
_Dot3OamUnsupportedCodesTx_Object = MibTableColumn
dot3OamUnsupportedCodesTx = _Dot3OamUnsupportedCodesTx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 4, 1, 15),
    _Dot3OamUnsupportedCodesTx_Type()
)
dot3OamUnsupportedCodesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamUnsupportedCodesTx.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamUnsupportedCodesTx.setUnits("frames")
_Dot3OamUnsupportedCodesRx_Type = Counter32
_Dot3OamUnsupportedCodesRx_Object = MibTableColumn
dot3OamUnsupportedCodesRx = _Dot3OamUnsupportedCodesRx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 4, 1, 16),
    _Dot3OamUnsupportedCodesRx_Type()
)
dot3OamUnsupportedCodesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamUnsupportedCodesRx.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamUnsupportedCodesRx.setUnits("frames")
_Dot3OamFramesLostDueToOam_Type = Counter32
_Dot3OamFramesLostDueToOam_Object = MibTableColumn
dot3OamFramesLostDueToOam = _Dot3OamFramesLostDueToOam_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 4, 1, 17),
    _Dot3OamFramesLostDueToOam_Type()
)
dot3OamFramesLostDueToOam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamFramesLostDueToOam.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamFramesLostDueToOam.setUnits("frames")
_Dot3OamEventConfigTable_Object = MibTable
dot3OamEventConfigTable = _Dot3OamEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 5)
)
if mibBuilder.loadTexts:
    dot3OamEventConfigTable.setStatus("current")
_Dot3OamEventConfigEntry_Object = MibTableRow
dot3OamEventConfigEntry = _Dot3OamEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 5, 1)
)
dot3OamEventConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot3OamEventConfigEntry.setStatus("current")
_Dot3OamErrSymPeriodWindowHi_Type = Unsigned32
_Dot3OamErrSymPeriodWindowHi_Object = MibTableColumn
dot3OamErrSymPeriodWindowHi = _Dot3OamErrSymPeriodWindowHi_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 5, 1, 1),
    _Dot3OamErrSymPeriodWindowHi_Type()
)
dot3OamErrSymPeriodWindowHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3OamErrSymPeriodWindowHi.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamErrSymPeriodWindowHi.setUnits("2^32 symbols")
_Dot3OamErrSymPeriodWindowLo_Type = Unsigned32
_Dot3OamErrSymPeriodWindowLo_Object = MibTableColumn
dot3OamErrSymPeriodWindowLo = _Dot3OamErrSymPeriodWindowLo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 5, 1, 2),
    _Dot3OamErrSymPeriodWindowLo_Type()
)
dot3OamErrSymPeriodWindowLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3OamErrSymPeriodWindowLo.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamErrSymPeriodWindowLo.setUnits("symbols")
_Dot3OamErrSymPeriodThresholdHi_Type = Unsigned32
_Dot3OamErrSymPeriodThresholdHi_Object = MibTableColumn
dot3OamErrSymPeriodThresholdHi = _Dot3OamErrSymPeriodThresholdHi_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 5, 1, 3),
    _Dot3OamErrSymPeriodThresholdHi_Type()
)
dot3OamErrSymPeriodThresholdHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3OamErrSymPeriodThresholdHi.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamErrSymPeriodThresholdHi.setUnits("2^32 symbols")
_Dot3OamErrSymPeriodThresholdLo_Type = Unsigned32
_Dot3OamErrSymPeriodThresholdLo_Object = MibTableColumn
dot3OamErrSymPeriodThresholdLo = _Dot3OamErrSymPeriodThresholdLo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 5, 1, 4),
    _Dot3OamErrSymPeriodThresholdLo_Type()
)
dot3OamErrSymPeriodThresholdLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3OamErrSymPeriodThresholdLo.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamErrSymPeriodThresholdLo.setUnits("symbols")
_Dot3OamErrSymPeriodEvNotifEnable_Type = TruthValue
_Dot3OamErrSymPeriodEvNotifEnable_Object = MibTableColumn
dot3OamErrSymPeriodEvNotifEnable = _Dot3OamErrSymPeriodEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 5, 1, 5),
    _Dot3OamErrSymPeriodEvNotifEnable_Type()
)
dot3OamErrSymPeriodEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3OamErrSymPeriodEvNotifEnable.setStatus("current")
_Dot3OamErrFramePeriodWindow_Type = Unsigned32
_Dot3OamErrFramePeriodWindow_Object = MibTableColumn
dot3OamErrFramePeriodWindow = _Dot3OamErrFramePeriodWindow_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 5, 1, 6),
    _Dot3OamErrFramePeriodWindow_Type()
)
dot3OamErrFramePeriodWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3OamErrFramePeriodWindow.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamErrFramePeriodWindow.setUnits("frames")
_Dot3OamErrFramePeriodThreshold_Type = Unsigned32
_Dot3OamErrFramePeriodThreshold_Object = MibTableColumn
dot3OamErrFramePeriodThreshold = _Dot3OamErrFramePeriodThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 5, 1, 7),
    _Dot3OamErrFramePeriodThreshold_Type()
)
dot3OamErrFramePeriodThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3OamErrFramePeriodThreshold.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamErrFramePeriodThreshold.setUnits("frames")
_Dot3OamErrFramePeriodEvNotifEnable_Type = TruthValue
_Dot3OamErrFramePeriodEvNotifEnable_Object = MibTableColumn
dot3OamErrFramePeriodEvNotifEnable = _Dot3OamErrFramePeriodEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 5, 1, 8),
    _Dot3OamErrFramePeriodEvNotifEnable_Type()
)
dot3OamErrFramePeriodEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3OamErrFramePeriodEvNotifEnable.setStatus("current")
_Dot3OamErrFrameWindow_Type = Unsigned32
_Dot3OamErrFrameWindow_Object = MibTableColumn
dot3OamErrFrameWindow = _Dot3OamErrFrameWindow_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 5, 1, 9),
    _Dot3OamErrFrameWindow_Type()
)
dot3OamErrFrameWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3OamErrFrameWindow.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamErrFrameWindow.setUnits("tenths of a second")
_Dot3OamErrFrameThreshold_Type = Unsigned32
_Dot3OamErrFrameThreshold_Object = MibTableColumn
dot3OamErrFrameThreshold = _Dot3OamErrFrameThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 5, 1, 10),
    _Dot3OamErrFrameThreshold_Type()
)
dot3OamErrFrameThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3OamErrFrameThreshold.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamErrFrameThreshold.setUnits("frames")
_Dot3OamErrFrameEvNotifEnable_Type = TruthValue
_Dot3OamErrFrameEvNotifEnable_Object = MibTableColumn
dot3OamErrFrameEvNotifEnable = _Dot3OamErrFrameEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 5, 1, 11),
    _Dot3OamErrFrameEvNotifEnable_Type()
)
dot3OamErrFrameEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3OamErrFrameEvNotifEnable.setStatus("current")


class _Dot3OamErrFrameSecsSummaryWindow_Type(Integer32):
    """Custom type dot3OamErrFrameSecsSummaryWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 9000),
    )


_Dot3OamErrFrameSecsSummaryWindow_Type.__name__ = "Integer32"
_Dot3OamErrFrameSecsSummaryWindow_Object = MibTableColumn
dot3OamErrFrameSecsSummaryWindow = _Dot3OamErrFrameSecsSummaryWindow_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 5, 1, 12),
    _Dot3OamErrFrameSecsSummaryWindow_Type()
)
dot3OamErrFrameSecsSummaryWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3OamErrFrameSecsSummaryWindow.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamErrFrameSecsSummaryWindow.setUnits("tenths of a second")


class _Dot3OamErrFrameSecsSummaryThreshold_Type(Integer32):
    """Custom type dot3OamErrFrameSecsSummaryThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_Dot3OamErrFrameSecsSummaryThreshold_Type.__name__ = "Integer32"
_Dot3OamErrFrameSecsSummaryThreshold_Object = MibTableColumn
dot3OamErrFrameSecsSummaryThreshold = _Dot3OamErrFrameSecsSummaryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 5, 1, 13),
    _Dot3OamErrFrameSecsSummaryThreshold_Type()
)
dot3OamErrFrameSecsSummaryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3OamErrFrameSecsSummaryThreshold.setStatus("current")
if mibBuilder.loadTexts:
    dot3OamErrFrameSecsSummaryThreshold.setUnits("errored frame seconds")
_Dot3OamErrFrameSecsEvNotifEnable_Type = TruthValue
_Dot3OamErrFrameSecsEvNotifEnable_Object = MibTableColumn
dot3OamErrFrameSecsEvNotifEnable = _Dot3OamErrFrameSecsEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 5, 1, 14),
    _Dot3OamErrFrameSecsEvNotifEnable_Type()
)
dot3OamErrFrameSecsEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3OamErrFrameSecsEvNotifEnable.setStatus("current")
_Dot3OamDyingGaspEnable_Type = TruthValue
_Dot3OamDyingGaspEnable_Object = MibTableColumn
dot3OamDyingGaspEnable = _Dot3OamDyingGaspEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 5, 1, 15),
    _Dot3OamDyingGaspEnable_Type()
)
dot3OamDyingGaspEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3OamDyingGaspEnable.setStatus("current")
_Dot3OamCriticalEventEnable_Type = TruthValue
_Dot3OamCriticalEventEnable_Object = MibTableColumn
dot3OamCriticalEventEnable = _Dot3OamCriticalEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 5, 1, 16),
    _Dot3OamCriticalEventEnable_Type()
)
dot3OamCriticalEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3OamCriticalEventEnable.setStatus("current")
_Dot3OamEventLogTable_Object = MibTable
dot3OamEventLogTable = _Dot3OamEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 6)
)
if mibBuilder.loadTexts:
    dot3OamEventLogTable.setStatus("current")
_Dot3OamEventLogEntry_Object = MibTableRow
dot3OamEventLogEntry = _Dot3OamEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 6, 1)
)
dot3OamEventLogEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZXEPON-SERVICE-OAM-MIB", "dot3OamEventLogIndex"),
)
if mibBuilder.loadTexts:
    dot3OamEventLogEntry.setStatus("current")
_Dot3OamEventLogIndex_Type = Unsigned32
_Dot3OamEventLogIndex_Object = MibTableColumn
dot3OamEventLogIndex = _Dot3OamEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 6, 1, 1),
    _Dot3OamEventLogIndex_Type()
)
dot3OamEventLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3OamEventLogIndex.setStatus("current")
_Dot3OamEventLogTimestamp_Type = TimeStamp
_Dot3OamEventLogTimestamp_Object = MibTableColumn
dot3OamEventLogTimestamp = _Dot3OamEventLogTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 6, 1, 2),
    _Dot3OamEventLogTimestamp_Type()
)
dot3OamEventLogTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamEventLogTimestamp.setStatus("current")
_Dot3OamEventLogOui_Type = Dot3Oui
_Dot3OamEventLogOui_Object = MibTableColumn
dot3OamEventLogOui = _Dot3OamEventLogOui_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 6, 1, 3),
    _Dot3OamEventLogOui_Type()
)
dot3OamEventLogOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamEventLogOui.setStatus("current")
_Dot3OamEventLogType_Type = Unsigned32
_Dot3OamEventLogType_Object = MibTableColumn
dot3OamEventLogType = _Dot3OamEventLogType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 6, 1, 4),
    _Dot3OamEventLogType_Type()
)
dot3OamEventLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamEventLogType.setStatus("current")


class _Dot3OamEventLogLocation_Type(Integer32):
    """Custom type dot3OamEventLogLocation based on Integer32"""
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


_Dot3OamEventLogLocation_Type.__name__ = "Integer32"
_Dot3OamEventLogLocation_Object = MibTableColumn
dot3OamEventLogLocation = _Dot3OamEventLogLocation_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 6, 1, 5),
    _Dot3OamEventLogLocation_Type()
)
dot3OamEventLogLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamEventLogLocation.setStatus("current")
_Dot3OamEventLogWindowHi_Type = Unsigned32
_Dot3OamEventLogWindowHi_Object = MibTableColumn
dot3OamEventLogWindowHi = _Dot3OamEventLogWindowHi_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 6, 1, 6),
    _Dot3OamEventLogWindowHi_Type()
)
dot3OamEventLogWindowHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamEventLogWindowHi.setStatus("current")
_Dot3OamEventLogWindowLo_Type = Unsigned32
_Dot3OamEventLogWindowLo_Object = MibTableColumn
dot3OamEventLogWindowLo = _Dot3OamEventLogWindowLo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 6, 1, 7),
    _Dot3OamEventLogWindowLo_Type()
)
dot3OamEventLogWindowLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamEventLogWindowLo.setStatus("current")
_Dot3OamEventLogThresholdHi_Type = Unsigned32
_Dot3OamEventLogThresholdHi_Object = MibTableColumn
dot3OamEventLogThresholdHi = _Dot3OamEventLogThresholdHi_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 6, 1, 8),
    _Dot3OamEventLogThresholdHi_Type()
)
dot3OamEventLogThresholdHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamEventLogThresholdHi.setStatus("current")
_Dot3OamEventLogThresholdLo_Type = Unsigned32
_Dot3OamEventLogThresholdLo_Object = MibTableColumn
dot3OamEventLogThresholdLo = _Dot3OamEventLogThresholdLo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 6, 1, 9),
    _Dot3OamEventLogThresholdLo_Type()
)
dot3OamEventLogThresholdLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamEventLogThresholdLo.setStatus("current")
_Dot3OamEventLogValue_Type = CounterBasedGauge64
_Dot3OamEventLogValue_Object = MibTableColumn
dot3OamEventLogValue = _Dot3OamEventLogValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 6, 1, 10),
    _Dot3OamEventLogValue_Type()
)
dot3OamEventLogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamEventLogValue.setStatus("current")
_Dot3OamEventLogRunningTotal_Type = CounterBasedGauge64
_Dot3OamEventLogRunningTotal_Object = MibTableColumn
dot3OamEventLogRunningTotal = _Dot3OamEventLogRunningTotal_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 6, 1, 11),
    _Dot3OamEventLogRunningTotal_Type()
)
dot3OamEventLogRunningTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamEventLogRunningTotal.setStatus("current")
_Dot3OamEventLogEventTotal_Type = Unsigned32
_Dot3OamEventLogEventTotal_Object = MibTableColumn
dot3OamEventLogEventTotal = _Dot3OamEventLogEventTotal_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 6, 6, 1, 12),
    _Dot3OamEventLogEventTotal_Type()
)
dot3OamEventLogEventTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamEventLogEventTotal.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXEPON-SERVICE-OAM-MIB",
    **{"Dot3Oui": Dot3Oui,
       "dot3OamObjects": dot3OamObjects,
       "dot3OamTable": dot3OamTable,
       "dot3OamEntry": dot3OamEntry,
       "dot3OamAdminState": dot3OamAdminState,
       "dot3OamOperStatus": dot3OamOperStatus,
       "dot3OamMode": dot3OamMode,
       "dot3OamMaxOamPduSize": dot3OamMaxOamPduSize,
       "dot3OamConfigRevision": dot3OamConfigRevision,
       "dot3OamFunctionsSupported": dot3OamFunctionsSupported,
       "dot3OamPeerTable": dot3OamPeerTable,
       "dot3OamPeerEntry": dot3OamPeerEntry,
       "dot3OamPeerMacAddress": dot3OamPeerMacAddress,
       "dot3OamPeerVendorOui": dot3OamPeerVendorOui,
       "dot3OamPeerVendorInfo": dot3OamPeerVendorInfo,
       "dot3OamPeerMode": dot3OamPeerMode,
       "dot3OamPeerMaxOamPduSize": dot3OamPeerMaxOamPduSize,
       "dot3OamPeerConfigRevision": dot3OamPeerConfigRevision,
       "dot3OamPeerFunctionsSupported": dot3OamPeerFunctionsSupported,
       "dot3OamLoopbackTable": dot3OamLoopbackTable,
       "dot3OamLoopbackEntry": dot3OamLoopbackEntry,
       "dot3OamLoopbackStatus": dot3OamLoopbackStatus,
       "dot3OamLoopbackIgnoreRx": dot3OamLoopbackIgnoreRx,
       "dot3OamStatsTable": dot3OamStatsTable,
       "dot3OamStatsEntry": dot3OamStatsEntry,
       "dot3OamInformationTx": dot3OamInformationTx,
       "dot3OamInformationRx": dot3OamInformationRx,
       "dot3OamUniqueEventNotificationTx": dot3OamUniqueEventNotificationTx,
       "dot3OamUniqueEventNotificationRx": dot3OamUniqueEventNotificationRx,
       "dot3OamDuplicateEventNotificationTx": dot3OamDuplicateEventNotificationTx,
       "dot3OamDuplicateEventNotificationRx": dot3OamDuplicateEventNotificationRx,
       "dot3OamLoopbackControlTx": dot3OamLoopbackControlTx,
       "dot3OamLoopbackControlRx": dot3OamLoopbackControlRx,
       "dot3OamVariableRequestTx": dot3OamVariableRequestTx,
       "dot3OamVariableRequestRx": dot3OamVariableRequestRx,
       "dot3OamVariableResponseTx": dot3OamVariableResponseTx,
       "dot3OamVariableResponseRx": dot3OamVariableResponseRx,
       "dot3OamOrgSpecificTx": dot3OamOrgSpecificTx,
       "dot3OamOrgSpecificRx": dot3OamOrgSpecificRx,
       "dot3OamUnsupportedCodesTx": dot3OamUnsupportedCodesTx,
       "dot3OamUnsupportedCodesRx": dot3OamUnsupportedCodesRx,
       "dot3OamFramesLostDueToOam": dot3OamFramesLostDueToOam,
       "dot3OamEventConfigTable": dot3OamEventConfigTable,
       "dot3OamEventConfigEntry": dot3OamEventConfigEntry,
       "dot3OamErrSymPeriodWindowHi": dot3OamErrSymPeriodWindowHi,
       "dot3OamErrSymPeriodWindowLo": dot3OamErrSymPeriodWindowLo,
       "dot3OamErrSymPeriodThresholdHi": dot3OamErrSymPeriodThresholdHi,
       "dot3OamErrSymPeriodThresholdLo": dot3OamErrSymPeriodThresholdLo,
       "dot3OamErrSymPeriodEvNotifEnable": dot3OamErrSymPeriodEvNotifEnable,
       "dot3OamErrFramePeriodWindow": dot3OamErrFramePeriodWindow,
       "dot3OamErrFramePeriodThreshold": dot3OamErrFramePeriodThreshold,
       "dot3OamErrFramePeriodEvNotifEnable": dot3OamErrFramePeriodEvNotifEnable,
       "dot3OamErrFrameWindow": dot3OamErrFrameWindow,
       "dot3OamErrFrameThreshold": dot3OamErrFrameThreshold,
       "dot3OamErrFrameEvNotifEnable": dot3OamErrFrameEvNotifEnable,
       "dot3OamErrFrameSecsSummaryWindow": dot3OamErrFrameSecsSummaryWindow,
       "dot3OamErrFrameSecsSummaryThreshold": dot3OamErrFrameSecsSummaryThreshold,
       "dot3OamErrFrameSecsEvNotifEnable": dot3OamErrFrameSecsEvNotifEnable,
       "dot3OamDyingGaspEnable": dot3OamDyingGaspEnable,
       "dot3OamCriticalEventEnable": dot3OamCriticalEventEnable,
       "dot3OamEventLogTable": dot3OamEventLogTable,
       "dot3OamEventLogEntry": dot3OamEventLogEntry,
       "dot3OamEventLogIndex": dot3OamEventLogIndex,
       "dot3OamEventLogTimestamp": dot3OamEventLogTimestamp,
       "dot3OamEventLogOui": dot3OamEventLogOui,
       "dot3OamEventLogType": dot3OamEventLogType,
       "dot3OamEventLogLocation": dot3OamEventLogLocation,
       "dot3OamEventLogWindowHi": dot3OamEventLogWindowHi,
       "dot3OamEventLogWindowLo": dot3OamEventLogWindowLo,
       "dot3OamEventLogThresholdHi": dot3OamEventLogThresholdHi,
       "dot3OamEventLogThresholdLo": dot3OamEventLogThresholdLo,
       "dot3OamEventLogValue": dot3OamEventLogValue,
       "dot3OamEventLogRunningTotal": dot3OamEventLogRunningTotal,
       "dot3OamEventLogEventTotal": dot3OamEventLogEventTotal}
)
