# SNMP MIB module (ZTE-AN-ETH-EFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-ETH-EFM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:33 2025
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

(zxAn,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "zxAn")


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

_ZxAnEthOamObjects_ObjectIdentity = ObjectIdentity
zxAnEthOamObjects = _ZxAnEthOamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61)
)
_ZxAnEthOamTable_Object = MibTable
zxAnEthOamTable = _ZxAnEthOamTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 1)
)
if mibBuilder.loadTexts:
    zxAnEthOamTable.setStatus("current")
_ZxAnEthOamEntry_Object = MibTableRow
zxAnEthOamEntry = _ZxAnEthOamEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 1, 1)
)
zxAnEthOamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnEthOamEntry.setStatus("current")


class _ZxAnEthOamAdminState_Type(Integer32):
    """Custom type zxAnEthOamAdminState based on Integer32"""
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


_ZxAnEthOamAdminState_Type.__name__ = "Integer32"
_ZxAnEthOamAdminState_Object = MibTableColumn
zxAnEthOamAdminState = _ZxAnEthOamAdminState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 1, 1, 1),
    _ZxAnEthOamAdminState_Type()
)
zxAnEthOamAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEthOamAdminState.setStatus("current")


class _ZxAnEthOamOperStatus_Type(Integer32):
    """Custom type zxAnEthOamOperStatus based on Integer32"""
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


_ZxAnEthOamOperStatus_Type.__name__ = "Integer32"
_ZxAnEthOamOperStatus_Object = MibTableColumn
zxAnEthOamOperStatus = _ZxAnEthOamOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 1, 1, 2),
    _ZxAnEthOamOperStatus_Type()
)
zxAnEthOamOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamOperStatus.setStatus("current")


class _ZxAnEthOamMode_Type(Integer32):
    """Custom type zxAnEthOamMode based on Integer32"""
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


_ZxAnEthOamMode_Type.__name__ = "Integer32"
_ZxAnEthOamMode_Object = MibTableColumn
zxAnEthOamMode = _ZxAnEthOamMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 1, 1, 3),
    _ZxAnEthOamMode_Type()
)
zxAnEthOamMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEthOamMode.setStatus("current")


class _ZxAnEthOamMaxOamPduSize_Type(Unsigned32):
    """Custom type zxAnEthOamMaxOamPduSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1518),
    )


_ZxAnEthOamMaxOamPduSize_Type.__name__ = "Unsigned32"
_ZxAnEthOamMaxOamPduSize_Object = MibTableColumn
zxAnEthOamMaxOamPduSize = _ZxAnEthOamMaxOamPduSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 1, 1, 4),
    _ZxAnEthOamMaxOamPduSize_Type()
)
zxAnEthOamMaxOamPduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamMaxOamPduSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamMaxOamPduSize.setUnits("octets")


class _ZxAnEthOamConfigRevision_Type(Unsigned32):
    """Custom type zxAnEthOamConfigRevision based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnEthOamConfigRevision_Type.__name__ = "Unsigned32"
_ZxAnEthOamConfigRevision_Object = MibTableColumn
zxAnEthOamConfigRevision = _ZxAnEthOamConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 1, 1, 5),
    _ZxAnEthOamConfigRevision_Type()
)
zxAnEthOamConfigRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamConfigRevision.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamConfigRevision.setUnits("octets")


class _ZxAnEthOamFunctionsSupported_Type(Bits):
    """Custom type zxAnEthOamFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        *(("unidirectionalSupport", 0),
          ("loopbackSupport", 1),
          ("eventSupport", 2),
          ("variableSupport", 3))
    )

_ZxAnEthOamFunctionsSupported_Type.__name__ = "Bits"
_ZxAnEthOamFunctionsSupported_Object = MibTableColumn
zxAnEthOamFunctionsSupported = _ZxAnEthOamFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 1, 1, 6),
    _ZxAnEthOamFunctionsSupported_Type()
)
zxAnEthOamFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamFunctionsSupported.setStatus("current")


class _ZxAnEthOamHardwareInfo_Type(DisplayString):
    """Custom type zxAnEthOamHardwareInfo based on DisplayString"""
    defaultValue = OctetString("Hardware Info")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZxAnEthOamHardwareInfo_Type.__name__ = "DisplayString"
_ZxAnEthOamHardwareInfo_Object = MibTableColumn
zxAnEthOamHardwareInfo = _ZxAnEthOamHardwareInfo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 1, 1, 7),
    _ZxAnEthOamHardwareInfo_Type()
)
zxAnEthOamHardwareInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamHardwareInfo.setStatus("current")


class _ZxAnEthOamSoftwareInfo_Type(DisplayString):
    """Custom type zxAnEthOamSoftwareInfo based on DisplayString"""
    defaultValue = OctetString("Software Info")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZxAnEthOamSoftwareInfo_Type.__name__ = "DisplayString"
_ZxAnEthOamSoftwareInfo_Object = MibTableColumn
zxAnEthOamSoftwareInfo = _ZxAnEthOamSoftwareInfo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 1, 1, 8),
    _ZxAnEthOamSoftwareInfo_Type()
)
zxAnEthOamSoftwareInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamSoftwareInfo.setStatus("current")
_ZxAnEthOamPeerTable_Object = MibTable
zxAnEthOamPeerTable = _ZxAnEthOamPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 2)
)
if mibBuilder.loadTexts:
    zxAnEthOamPeerTable.setStatus("current")
_ZxAnEthOamPeerEntry_Object = MibTableRow
zxAnEthOamPeerEntry = _ZxAnEthOamPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 2, 1)
)
zxAnEthOamPeerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnEthOamPeerEntry.setStatus("current")
_ZxAnEthOamPeerMacAddress_Type = MacAddress
_ZxAnEthOamPeerMacAddress_Object = MibTableColumn
zxAnEthOamPeerMacAddress = _ZxAnEthOamPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 2, 1, 1),
    _ZxAnEthOamPeerMacAddress_Type()
)
zxAnEthOamPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamPeerMacAddress.setStatus("current")
_ZxAnEthOamPeerVendorOui_Type = Dot3Oui
_ZxAnEthOamPeerVendorOui_Object = MibTableColumn
zxAnEthOamPeerVendorOui = _ZxAnEthOamPeerVendorOui_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 2, 1, 2),
    _ZxAnEthOamPeerVendorOui_Type()
)
zxAnEthOamPeerVendorOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamPeerVendorOui.setStatus("current")
_ZxAnEthOamPeerVendorInfo_Type = Unsigned32
_ZxAnEthOamPeerVendorInfo_Object = MibTableColumn
zxAnEthOamPeerVendorInfo = _ZxAnEthOamPeerVendorInfo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 2, 1, 3),
    _ZxAnEthOamPeerVendorInfo_Type()
)
zxAnEthOamPeerVendorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamPeerVendorInfo.setStatus("current")


class _ZxAnEthOamPeerMode_Type(Integer32):
    """Custom type zxAnEthOamPeerMode based on Integer32"""
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


_ZxAnEthOamPeerMode_Type.__name__ = "Integer32"
_ZxAnEthOamPeerMode_Object = MibTableColumn
zxAnEthOamPeerMode = _ZxAnEthOamPeerMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 2, 1, 4),
    _ZxAnEthOamPeerMode_Type()
)
zxAnEthOamPeerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamPeerMode.setStatus("current")


class _ZxAnEthOamPeerMaxOamPduSize_Type(Unsigned32):
    """Custom type zxAnEthOamPeerMaxOamPduSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 1518),
    )


_ZxAnEthOamPeerMaxOamPduSize_Type.__name__ = "Unsigned32"
_ZxAnEthOamPeerMaxOamPduSize_Object = MibTableColumn
zxAnEthOamPeerMaxOamPduSize = _ZxAnEthOamPeerMaxOamPduSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 2, 1, 5),
    _ZxAnEthOamPeerMaxOamPduSize_Type()
)
zxAnEthOamPeerMaxOamPduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamPeerMaxOamPduSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamPeerMaxOamPduSize.setUnits("octets")


class _ZxAnEthOamPeerConfigRevision_Type(Unsigned32):
    """Custom type zxAnEthOamPeerConfigRevision based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnEthOamPeerConfigRevision_Type.__name__ = "Unsigned32"
_ZxAnEthOamPeerConfigRevision_Object = MibTableColumn
zxAnEthOamPeerConfigRevision = _ZxAnEthOamPeerConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 2, 1, 6),
    _ZxAnEthOamPeerConfigRevision_Type()
)
zxAnEthOamPeerConfigRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamPeerConfigRevision.setStatus("current")


class _ZxAnEthOamPeerFunctionsSupported_Type(Bits):
    """Custom type zxAnEthOamPeerFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        *(("unidirectionalSupport", 0),
          ("loopbackSupport", 1),
          ("eventSupport", 2),
          ("variableSupport", 3))
    )

_ZxAnEthOamPeerFunctionsSupported_Type.__name__ = "Bits"
_ZxAnEthOamPeerFunctionsSupported_Object = MibTableColumn
zxAnEthOamPeerFunctionsSupported = _ZxAnEthOamPeerFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 2, 1, 7),
    _ZxAnEthOamPeerFunctionsSupported_Type()
)
zxAnEthOamPeerFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamPeerFunctionsSupported.setStatus("current")
_ZxAnEthOamLoopbackTable_Object = MibTable
zxAnEthOamLoopbackTable = _ZxAnEthOamLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 3)
)
if mibBuilder.loadTexts:
    zxAnEthOamLoopbackTable.setStatus("current")
_ZxAnEthOamLoopbackEntry_Object = MibTableRow
zxAnEthOamLoopbackEntry = _ZxAnEthOamLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 3, 1)
)
zxAnEthOamLoopbackEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnEthOamLoopbackEntry.setStatus("current")


class _ZxAnEthOamLoopbackStatus_Type(Integer32):
    """Custom type zxAnEthOamLoopbackStatus based on Integer32"""
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


_ZxAnEthOamLoopbackStatus_Type.__name__ = "Integer32"
_ZxAnEthOamLoopbackStatus_Object = MibTableColumn
zxAnEthOamLoopbackStatus = _ZxAnEthOamLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 3, 1, 1),
    _ZxAnEthOamLoopbackStatus_Type()
)
zxAnEthOamLoopbackStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEthOamLoopbackStatus.setStatus("current")


class _ZxAnEthOamLoopbackIgnoreRx_Type(Integer32):
    """Custom type zxAnEthOamLoopbackIgnoreRx based on Integer32"""
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


_ZxAnEthOamLoopbackIgnoreRx_Type.__name__ = "Integer32"
_ZxAnEthOamLoopbackIgnoreRx_Object = MibTableColumn
zxAnEthOamLoopbackIgnoreRx = _ZxAnEthOamLoopbackIgnoreRx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 3, 1, 2),
    _ZxAnEthOamLoopbackIgnoreRx_Type()
)
zxAnEthOamLoopbackIgnoreRx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEthOamLoopbackIgnoreRx.setStatus("current")


class _ZxAnEthOamLoopbackResult_Type(Integer32):
    """Custom type zxAnEthOamLoopbackResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("noResult", 0),
          ("success", 1),
          ("generalFailed", 2),
          ("noSupport", 3),
          ("unkown", 4),
          ("noSuchPort", 5),
          ("loopBackFailed", 6),
          ("portNotActive", 7),
          ("portInTesting", 8),
          ("portInService", 9),
          ("portFailures", 10),
          ("cardFailures", 11),
          ("noPvcFound", 12),
          ("unknownTestType", 13))
    )


_ZxAnEthOamLoopbackResult_Type.__name__ = "Integer32"
_ZxAnEthOamLoopbackResult_Object = MibTableColumn
zxAnEthOamLoopbackResult = _ZxAnEthOamLoopbackResult_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 3, 1, 3),
    _ZxAnEthOamLoopbackResult_Type()
)
zxAnEthOamLoopbackResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamLoopbackResult.setStatus("current")
_ZxAnEthOamLoopbackSend_Type = Integer32
_ZxAnEthOamLoopbackSend_Object = MibTableColumn
zxAnEthOamLoopbackSend = _ZxAnEthOamLoopbackSend_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 3, 1, 4),
    _ZxAnEthOamLoopbackSend_Type()
)
zxAnEthOamLoopbackSend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEthOamLoopbackSend.setStatus("current")
_ZxAnEthOamLoopbackRecv_Type = Integer32
_ZxAnEthOamLoopbackRecv_Object = MibTableColumn
zxAnEthOamLoopbackRecv = _ZxAnEthOamLoopbackRecv_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 3, 1, 5),
    _ZxAnEthOamLoopbackRecv_Type()
)
zxAnEthOamLoopbackRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamLoopbackRecv.setStatus("current")
_ZxAnEthOamStatsTable_Object = MibTable
zxAnEthOamStatsTable = _ZxAnEthOamStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 4)
)
if mibBuilder.loadTexts:
    zxAnEthOamStatsTable.setStatus("current")
_ZxAnEthOamStatsEntry_Object = MibTableRow
zxAnEthOamStatsEntry = _ZxAnEthOamStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 4, 1)
)
zxAnEthOamStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnEthOamStatsEntry.setStatus("current")
_ZxAnEthOamInformationTx_Type = Counter32
_ZxAnEthOamInformationTx_Object = MibTableColumn
zxAnEthOamInformationTx = _ZxAnEthOamInformationTx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 4, 1, 1),
    _ZxAnEthOamInformationTx_Type()
)
zxAnEthOamInformationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamInformationTx.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamInformationTx.setUnits("frames")
_ZxAnEthOamInformationRx_Type = Counter32
_ZxAnEthOamInformationRx_Object = MibTableColumn
zxAnEthOamInformationRx = _ZxAnEthOamInformationRx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 4, 1, 2),
    _ZxAnEthOamInformationRx_Type()
)
zxAnEthOamInformationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamInformationRx.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamInformationRx.setUnits("frames")
_ZxAnEthOamUniqueEventNotificationTx_Type = Counter32
_ZxAnEthOamUniqueEventNotificationTx_Object = MibTableColumn
zxAnEthOamUniqueEventNotificationTx = _ZxAnEthOamUniqueEventNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 4, 1, 3),
    _ZxAnEthOamUniqueEventNotificationTx_Type()
)
zxAnEthOamUniqueEventNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamUniqueEventNotificationTx.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamUniqueEventNotificationTx.setUnits("frames")
_ZxAnEthOamUniqueEventNotificationRx_Type = Counter32
_ZxAnEthOamUniqueEventNotificationRx_Object = MibTableColumn
zxAnEthOamUniqueEventNotificationRx = _ZxAnEthOamUniqueEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 4, 1, 4),
    _ZxAnEthOamUniqueEventNotificationRx_Type()
)
zxAnEthOamUniqueEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamUniqueEventNotificationRx.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamUniqueEventNotificationRx.setUnits("frames")
_ZxAnEthOamDuplicateEventNotificationTx_Type = Counter32
_ZxAnEthOamDuplicateEventNotificationTx_Object = MibTableColumn
zxAnEthOamDuplicateEventNotificationTx = _ZxAnEthOamDuplicateEventNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 4, 1, 5),
    _ZxAnEthOamDuplicateEventNotificationTx_Type()
)
zxAnEthOamDuplicateEventNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamDuplicateEventNotificationTx.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamDuplicateEventNotificationTx.setUnits("frames")
_ZxAnEthOamDuplicateEventNotificationRx_Type = Counter32
_ZxAnEthOamDuplicateEventNotificationRx_Object = MibTableColumn
zxAnEthOamDuplicateEventNotificationRx = _ZxAnEthOamDuplicateEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 4, 1, 6),
    _ZxAnEthOamDuplicateEventNotificationRx_Type()
)
zxAnEthOamDuplicateEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamDuplicateEventNotificationRx.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamDuplicateEventNotificationRx.setUnits("frames")
_ZxAnEthOamLoopbackControlTx_Type = Counter32
_ZxAnEthOamLoopbackControlTx_Object = MibTableColumn
zxAnEthOamLoopbackControlTx = _ZxAnEthOamLoopbackControlTx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 4, 1, 7),
    _ZxAnEthOamLoopbackControlTx_Type()
)
zxAnEthOamLoopbackControlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamLoopbackControlTx.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamLoopbackControlTx.setUnits("frames")
_ZxAnEthOamLoopbackControlRx_Type = Counter32
_ZxAnEthOamLoopbackControlRx_Object = MibTableColumn
zxAnEthOamLoopbackControlRx = _ZxAnEthOamLoopbackControlRx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 4, 1, 8),
    _ZxAnEthOamLoopbackControlRx_Type()
)
zxAnEthOamLoopbackControlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamLoopbackControlRx.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamLoopbackControlRx.setUnits("frames")
_ZxAnEthOamVariableRequestTx_Type = Counter32
_ZxAnEthOamVariableRequestTx_Object = MibTableColumn
zxAnEthOamVariableRequestTx = _ZxAnEthOamVariableRequestTx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 4, 1, 9),
    _ZxAnEthOamVariableRequestTx_Type()
)
zxAnEthOamVariableRequestTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamVariableRequestTx.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamVariableRequestTx.setUnits("frames")
_ZxAnEthOamVariableRequestRx_Type = Counter32
_ZxAnEthOamVariableRequestRx_Object = MibTableColumn
zxAnEthOamVariableRequestRx = _ZxAnEthOamVariableRequestRx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 4, 1, 10),
    _ZxAnEthOamVariableRequestRx_Type()
)
zxAnEthOamVariableRequestRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamVariableRequestRx.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamVariableRequestRx.setUnits("frames")
_ZxAnEthOamVariableResponseTx_Type = Counter32
_ZxAnEthOamVariableResponseTx_Object = MibTableColumn
zxAnEthOamVariableResponseTx = _ZxAnEthOamVariableResponseTx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 4, 1, 11),
    _ZxAnEthOamVariableResponseTx_Type()
)
zxAnEthOamVariableResponseTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamVariableResponseTx.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamVariableResponseTx.setUnits("frames")
_ZxAnEthOamVariableResponseRx_Type = Counter32
_ZxAnEthOamVariableResponseRx_Object = MibTableColumn
zxAnEthOamVariableResponseRx = _ZxAnEthOamVariableResponseRx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 4, 1, 12),
    _ZxAnEthOamVariableResponseRx_Type()
)
zxAnEthOamVariableResponseRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamVariableResponseRx.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamVariableResponseRx.setUnits("frames")
_ZxAnEthOamOrgSpecificTx_Type = Counter32
_ZxAnEthOamOrgSpecificTx_Object = MibTableColumn
zxAnEthOamOrgSpecificTx = _ZxAnEthOamOrgSpecificTx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 4, 1, 13),
    _ZxAnEthOamOrgSpecificTx_Type()
)
zxAnEthOamOrgSpecificTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamOrgSpecificTx.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamOrgSpecificTx.setUnits("frames")
_ZxAnEthOamOrgSpecificRx_Type = Counter32
_ZxAnEthOamOrgSpecificRx_Object = MibTableColumn
zxAnEthOamOrgSpecificRx = _ZxAnEthOamOrgSpecificRx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 4, 1, 14),
    _ZxAnEthOamOrgSpecificRx_Type()
)
zxAnEthOamOrgSpecificRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamOrgSpecificRx.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamOrgSpecificRx.setUnits("frames")
_ZxAnEthOamUnsupportedCodesTx_Type = Counter32
_ZxAnEthOamUnsupportedCodesTx_Object = MibTableColumn
zxAnEthOamUnsupportedCodesTx = _ZxAnEthOamUnsupportedCodesTx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 4, 1, 15),
    _ZxAnEthOamUnsupportedCodesTx_Type()
)
zxAnEthOamUnsupportedCodesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamUnsupportedCodesTx.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamUnsupportedCodesTx.setUnits("frames")
_ZxAnEthOamUnsupportedCodesRx_Type = Counter32
_ZxAnEthOamUnsupportedCodesRx_Object = MibTableColumn
zxAnEthOamUnsupportedCodesRx = _ZxAnEthOamUnsupportedCodesRx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 4, 1, 16),
    _ZxAnEthOamUnsupportedCodesRx_Type()
)
zxAnEthOamUnsupportedCodesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamUnsupportedCodesRx.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamUnsupportedCodesRx.setUnits("frames")
_ZxAnEthOamFramesLostDueToOam_Type = Counter32
_ZxAnEthOamFramesLostDueToOam_Object = MibTableColumn
zxAnEthOamFramesLostDueToOam = _ZxAnEthOamFramesLostDueToOam_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 4, 1, 17),
    _ZxAnEthOamFramesLostDueToOam_Type()
)
zxAnEthOamFramesLostDueToOam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamFramesLostDueToOam.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamFramesLostDueToOam.setUnits("frames")
_ZxAnEthOamEventConfigTable_Object = MibTable
zxAnEthOamEventConfigTable = _ZxAnEthOamEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 5)
)
if mibBuilder.loadTexts:
    zxAnEthOamEventConfigTable.setStatus("current")
_ZxAnEthOamEventConfigEntry_Object = MibTableRow
zxAnEthOamEventConfigEntry = _ZxAnEthOamEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 5, 1)
)
zxAnEthOamEventConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnEthOamEventConfigEntry.setStatus("current")
_ZxAnEthOamErrSymPeriodWindowHi_Type = Unsigned32
_ZxAnEthOamErrSymPeriodWindowHi_Object = MibTableColumn
zxAnEthOamErrSymPeriodWindowHi = _ZxAnEthOamErrSymPeriodWindowHi_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 5, 1, 1),
    _ZxAnEthOamErrSymPeriodWindowHi_Type()
)
zxAnEthOamErrSymPeriodWindowHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEthOamErrSymPeriodWindowHi.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamErrSymPeriodWindowHi.setUnits("2^32 symbols")
_ZxAnEthOamErrSymPeriodWindowLo_Type = Unsigned32
_ZxAnEthOamErrSymPeriodWindowLo_Object = MibTableColumn
zxAnEthOamErrSymPeriodWindowLo = _ZxAnEthOamErrSymPeriodWindowLo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 5, 1, 2),
    _ZxAnEthOamErrSymPeriodWindowLo_Type()
)
zxAnEthOamErrSymPeriodWindowLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEthOamErrSymPeriodWindowLo.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamErrSymPeriodWindowLo.setUnits("symbols")
_ZxAnEthOamErrSymPeriodThresholdHi_Type = Unsigned32
_ZxAnEthOamErrSymPeriodThresholdHi_Object = MibTableColumn
zxAnEthOamErrSymPeriodThresholdHi = _ZxAnEthOamErrSymPeriodThresholdHi_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 5, 1, 3),
    _ZxAnEthOamErrSymPeriodThresholdHi_Type()
)
zxAnEthOamErrSymPeriodThresholdHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEthOamErrSymPeriodThresholdHi.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamErrSymPeriodThresholdHi.setUnits("2^32 symbols")
_ZxAnEthOamErrSymPeriodThresholdLo_Type = Unsigned32
_ZxAnEthOamErrSymPeriodThresholdLo_Object = MibTableColumn
zxAnEthOamErrSymPeriodThresholdLo = _ZxAnEthOamErrSymPeriodThresholdLo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 5, 1, 4),
    _ZxAnEthOamErrSymPeriodThresholdLo_Type()
)
zxAnEthOamErrSymPeriodThresholdLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEthOamErrSymPeriodThresholdLo.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamErrSymPeriodThresholdLo.setUnits("symbols")
_ZxAnEthOamErrSymPeriodEvNotifEnable_Type = TruthValue
_ZxAnEthOamErrSymPeriodEvNotifEnable_Object = MibTableColumn
zxAnEthOamErrSymPeriodEvNotifEnable = _ZxAnEthOamErrSymPeriodEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 5, 1, 5),
    _ZxAnEthOamErrSymPeriodEvNotifEnable_Type()
)
zxAnEthOamErrSymPeriodEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEthOamErrSymPeriodEvNotifEnable.setStatus("current")
_ZxAnEthOamErrFramePeriodWindow_Type = Unsigned32
_ZxAnEthOamErrFramePeriodWindow_Object = MibTableColumn
zxAnEthOamErrFramePeriodWindow = _ZxAnEthOamErrFramePeriodWindow_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 5, 1, 6),
    _ZxAnEthOamErrFramePeriodWindow_Type()
)
zxAnEthOamErrFramePeriodWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEthOamErrFramePeriodWindow.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamErrFramePeriodWindow.setUnits("frames")
_ZxAnEthOamErrFramePeriodThreshold_Type = Unsigned32
_ZxAnEthOamErrFramePeriodThreshold_Object = MibTableColumn
zxAnEthOamErrFramePeriodThreshold = _ZxAnEthOamErrFramePeriodThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 5, 1, 7),
    _ZxAnEthOamErrFramePeriodThreshold_Type()
)
zxAnEthOamErrFramePeriodThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEthOamErrFramePeriodThreshold.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamErrFramePeriodThreshold.setUnits("frames")
_ZxAnEthOamErrFramePeriodEvNotifEnable_Type = TruthValue
_ZxAnEthOamErrFramePeriodEvNotifEnable_Object = MibTableColumn
zxAnEthOamErrFramePeriodEvNotifEnable = _ZxAnEthOamErrFramePeriodEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 5, 1, 8),
    _ZxAnEthOamErrFramePeriodEvNotifEnable_Type()
)
zxAnEthOamErrFramePeriodEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEthOamErrFramePeriodEvNotifEnable.setStatus("current")
_ZxAnEthOamErrFrameWindow_Type = Unsigned32
_ZxAnEthOamErrFrameWindow_Object = MibTableColumn
zxAnEthOamErrFrameWindow = _ZxAnEthOamErrFrameWindow_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 5, 1, 9),
    _ZxAnEthOamErrFrameWindow_Type()
)
zxAnEthOamErrFrameWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEthOamErrFrameWindow.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamErrFrameWindow.setUnits("tenths of a second")
_ZxAnEthOamErrFrameThreshold_Type = Unsigned32
_ZxAnEthOamErrFrameThreshold_Object = MibTableColumn
zxAnEthOamErrFrameThreshold = _ZxAnEthOamErrFrameThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 5, 1, 10),
    _ZxAnEthOamErrFrameThreshold_Type()
)
zxAnEthOamErrFrameThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEthOamErrFrameThreshold.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamErrFrameThreshold.setUnits("frames")
_ZxAnEthOamErrFrameEvNotifEnable_Type = TruthValue
_ZxAnEthOamErrFrameEvNotifEnable_Object = MibTableColumn
zxAnEthOamErrFrameEvNotifEnable = _ZxAnEthOamErrFrameEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 5, 1, 11),
    _ZxAnEthOamErrFrameEvNotifEnable_Type()
)
zxAnEthOamErrFrameEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEthOamErrFrameEvNotifEnable.setStatus("current")


class _ZxAnEthOamErrFrameSecsSummaryWindow_Type(Integer32):
    """Custom type zxAnEthOamErrFrameSecsSummaryWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 9000),
    )


_ZxAnEthOamErrFrameSecsSummaryWindow_Type.__name__ = "Integer32"
_ZxAnEthOamErrFrameSecsSummaryWindow_Object = MibTableColumn
zxAnEthOamErrFrameSecsSummaryWindow = _ZxAnEthOamErrFrameSecsSummaryWindow_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 5, 1, 12),
    _ZxAnEthOamErrFrameSecsSummaryWindow_Type()
)
zxAnEthOamErrFrameSecsSummaryWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEthOamErrFrameSecsSummaryWindow.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamErrFrameSecsSummaryWindow.setUnits("tenths of a second")


class _ZxAnEthOamErrFrameSecsSummaryThreshold_Type(Integer32):
    """Custom type zxAnEthOamErrFrameSecsSummaryThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_ZxAnEthOamErrFrameSecsSummaryThreshold_Type.__name__ = "Integer32"
_ZxAnEthOamErrFrameSecsSummaryThreshold_Object = MibTableColumn
zxAnEthOamErrFrameSecsSummaryThreshold = _ZxAnEthOamErrFrameSecsSummaryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 5, 1, 13),
    _ZxAnEthOamErrFrameSecsSummaryThreshold_Type()
)
zxAnEthOamErrFrameSecsSummaryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEthOamErrFrameSecsSummaryThreshold.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEthOamErrFrameSecsSummaryThreshold.setUnits("errored frame seconds")
_ZxAnEthOamErrFrameSecsEvNotifEnable_Type = TruthValue
_ZxAnEthOamErrFrameSecsEvNotifEnable_Object = MibTableColumn
zxAnEthOamErrFrameSecsEvNotifEnable = _ZxAnEthOamErrFrameSecsEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 5, 1, 14),
    _ZxAnEthOamErrFrameSecsEvNotifEnable_Type()
)
zxAnEthOamErrFrameSecsEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEthOamErrFrameSecsEvNotifEnable.setStatus("current")
_ZxAnEthOamDyingGaspEnable_Type = TruthValue
_ZxAnEthOamDyingGaspEnable_Object = MibTableColumn
zxAnEthOamDyingGaspEnable = _ZxAnEthOamDyingGaspEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 5, 1, 15),
    _ZxAnEthOamDyingGaspEnable_Type()
)
zxAnEthOamDyingGaspEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEthOamDyingGaspEnable.setStatus("current")
_ZxAnEthOamCriticalEventEnable_Type = TruthValue
_ZxAnEthOamCriticalEventEnable_Object = MibTableColumn
zxAnEthOamCriticalEventEnable = _ZxAnEthOamCriticalEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 5, 1, 16),
    _ZxAnEthOamCriticalEventEnable_Type()
)
zxAnEthOamCriticalEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEthOamCriticalEventEnable.setStatus("current")
_ZxAnEthOamEventLogTable_Object = MibTable
zxAnEthOamEventLogTable = _ZxAnEthOamEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 6)
)
if mibBuilder.loadTexts:
    zxAnEthOamEventLogTable.setStatus("current")
_ZxAnEthOamEventLogEntry_Object = MibTableRow
zxAnEthOamEventLogEntry = _ZxAnEthOamEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 6, 1)
)
zxAnEthOamEventLogEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZTE-AN-ETH-EFM-MIB", "zxAnEthOamEventLogIndex"),
)
if mibBuilder.loadTexts:
    zxAnEthOamEventLogEntry.setStatus("current")
_ZxAnEthOamEventLogIndex_Type = Unsigned32
_ZxAnEthOamEventLogIndex_Object = MibTableColumn
zxAnEthOamEventLogIndex = _ZxAnEthOamEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 6, 1, 1),
    _ZxAnEthOamEventLogIndex_Type()
)
zxAnEthOamEventLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEthOamEventLogIndex.setStatus("current")
_ZxAnEthOamEventLogTimestamp_Type = TimeStamp
_ZxAnEthOamEventLogTimestamp_Object = MibTableColumn
zxAnEthOamEventLogTimestamp = _ZxAnEthOamEventLogTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 6, 1, 2),
    _ZxAnEthOamEventLogTimestamp_Type()
)
zxAnEthOamEventLogTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamEventLogTimestamp.setStatus("current")
_ZxAnEthOamEventLogOui_Type = Dot3Oui
_ZxAnEthOamEventLogOui_Object = MibTableColumn
zxAnEthOamEventLogOui = _ZxAnEthOamEventLogOui_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 6, 1, 3),
    _ZxAnEthOamEventLogOui_Type()
)
zxAnEthOamEventLogOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamEventLogOui.setStatus("current")
_ZxAnEthOamEventLogType_Type = Unsigned32
_ZxAnEthOamEventLogType_Object = MibTableColumn
zxAnEthOamEventLogType = _ZxAnEthOamEventLogType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 6, 1, 4),
    _ZxAnEthOamEventLogType_Type()
)
zxAnEthOamEventLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamEventLogType.setStatus("current")


class _ZxAnEthOamEventLogLocation_Type(Integer32):
    """Custom type zxAnEthOamEventLogLocation based on Integer32"""
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


_ZxAnEthOamEventLogLocation_Type.__name__ = "Integer32"
_ZxAnEthOamEventLogLocation_Object = MibTableColumn
zxAnEthOamEventLogLocation = _ZxAnEthOamEventLogLocation_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 6, 1, 5),
    _ZxAnEthOamEventLogLocation_Type()
)
zxAnEthOamEventLogLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamEventLogLocation.setStatus("current")
_ZxAnEthOamEventLogWindowHi_Type = Unsigned32
_ZxAnEthOamEventLogWindowHi_Object = MibTableColumn
zxAnEthOamEventLogWindowHi = _ZxAnEthOamEventLogWindowHi_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 6, 1, 6),
    _ZxAnEthOamEventLogWindowHi_Type()
)
zxAnEthOamEventLogWindowHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamEventLogWindowHi.setStatus("current")
_ZxAnEthOamEventLogWindowLo_Type = Unsigned32
_ZxAnEthOamEventLogWindowLo_Object = MibTableColumn
zxAnEthOamEventLogWindowLo = _ZxAnEthOamEventLogWindowLo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 6, 1, 7),
    _ZxAnEthOamEventLogWindowLo_Type()
)
zxAnEthOamEventLogWindowLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamEventLogWindowLo.setStatus("current")
_ZxAnEthOamEventLogThresholdHi_Type = Unsigned32
_ZxAnEthOamEventLogThresholdHi_Object = MibTableColumn
zxAnEthOamEventLogThresholdHi = _ZxAnEthOamEventLogThresholdHi_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 6, 1, 8),
    _ZxAnEthOamEventLogThresholdHi_Type()
)
zxAnEthOamEventLogThresholdHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamEventLogThresholdHi.setStatus("current")
_ZxAnEthOamEventLogThresholdLo_Type = Unsigned32
_ZxAnEthOamEventLogThresholdLo_Object = MibTableColumn
zxAnEthOamEventLogThresholdLo = _ZxAnEthOamEventLogThresholdLo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 6, 1, 9),
    _ZxAnEthOamEventLogThresholdLo_Type()
)
zxAnEthOamEventLogThresholdLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamEventLogThresholdLo.setStatus("current")
_ZxAnEthOamEventLogValue_Type = CounterBasedGauge64
_ZxAnEthOamEventLogValue_Object = MibTableColumn
zxAnEthOamEventLogValue = _ZxAnEthOamEventLogValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 6, 1, 10),
    _ZxAnEthOamEventLogValue_Type()
)
zxAnEthOamEventLogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamEventLogValue.setStatus("current")
_ZxAnEthOamEventLogRunningTotal_Type = CounterBasedGauge64
_ZxAnEthOamEventLogRunningTotal_Object = MibTableColumn
zxAnEthOamEventLogRunningTotal = _ZxAnEthOamEventLogRunningTotal_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 6, 1, 11),
    _ZxAnEthOamEventLogRunningTotal_Type()
)
zxAnEthOamEventLogRunningTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamEventLogRunningTotal.setStatus("current")
_ZxAnEthOamEventLogEventTotal_Type = Unsigned32
_ZxAnEthOamEventLogEventTotal_Object = MibTableColumn
zxAnEthOamEventLogEventTotal = _ZxAnEthOamEventLogEventTotal_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 6, 1, 12),
    _ZxAnEthOamEventLogEventTotal_Type()
)
zxAnEthOamEventLogEventTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEthOamEventLogEventTotal.setStatus("current")
_ZxAnEthOamGlobalEnable_Type = TruthValue
_ZxAnEthOamGlobalEnable_Object = MibScalar
zxAnEthOamGlobalEnable = _ZxAnEthOamGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 61, 7),
    _ZxAnEthOamGlobalEnable_Type()
)
zxAnEthOamGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEthOamGlobalEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-ETH-EFM-MIB",
    **{"Dot3Oui": Dot3Oui,
       "zxAnEthOamObjects": zxAnEthOamObjects,
       "zxAnEthOamTable": zxAnEthOamTable,
       "zxAnEthOamEntry": zxAnEthOamEntry,
       "zxAnEthOamAdminState": zxAnEthOamAdminState,
       "zxAnEthOamOperStatus": zxAnEthOamOperStatus,
       "zxAnEthOamMode": zxAnEthOamMode,
       "zxAnEthOamMaxOamPduSize": zxAnEthOamMaxOamPduSize,
       "zxAnEthOamConfigRevision": zxAnEthOamConfigRevision,
       "zxAnEthOamFunctionsSupported": zxAnEthOamFunctionsSupported,
       "zxAnEthOamHardwareInfo": zxAnEthOamHardwareInfo,
       "zxAnEthOamSoftwareInfo": zxAnEthOamSoftwareInfo,
       "zxAnEthOamPeerTable": zxAnEthOamPeerTable,
       "zxAnEthOamPeerEntry": zxAnEthOamPeerEntry,
       "zxAnEthOamPeerMacAddress": zxAnEthOamPeerMacAddress,
       "zxAnEthOamPeerVendorOui": zxAnEthOamPeerVendorOui,
       "zxAnEthOamPeerVendorInfo": zxAnEthOamPeerVendorInfo,
       "zxAnEthOamPeerMode": zxAnEthOamPeerMode,
       "zxAnEthOamPeerMaxOamPduSize": zxAnEthOamPeerMaxOamPduSize,
       "zxAnEthOamPeerConfigRevision": zxAnEthOamPeerConfigRevision,
       "zxAnEthOamPeerFunctionsSupported": zxAnEthOamPeerFunctionsSupported,
       "zxAnEthOamLoopbackTable": zxAnEthOamLoopbackTable,
       "zxAnEthOamLoopbackEntry": zxAnEthOamLoopbackEntry,
       "zxAnEthOamLoopbackStatus": zxAnEthOamLoopbackStatus,
       "zxAnEthOamLoopbackIgnoreRx": zxAnEthOamLoopbackIgnoreRx,
       "zxAnEthOamLoopbackResult": zxAnEthOamLoopbackResult,
       "zxAnEthOamLoopbackSend": zxAnEthOamLoopbackSend,
       "zxAnEthOamLoopbackRecv": zxAnEthOamLoopbackRecv,
       "zxAnEthOamStatsTable": zxAnEthOamStatsTable,
       "zxAnEthOamStatsEntry": zxAnEthOamStatsEntry,
       "zxAnEthOamInformationTx": zxAnEthOamInformationTx,
       "zxAnEthOamInformationRx": zxAnEthOamInformationRx,
       "zxAnEthOamUniqueEventNotificationTx": zxAnEthOamUniqueEventNotificationTx,
       "zxAnEthOamUniqueEventNotificationRx": zxAnEthOamUniqueEventNotificationRx,
       "zxAnEthOamDuplicateEventNotificationTx": zxAnEthOamDuplicateEventNotificationTx,
       "zxAnEthOamDuplicateEventNotificationRx": zxAnEthOamDuplicateEventNotificationRx,
       "zxAnEthOamLoopbackControlTx": zxAnEthOamLoopbackControlTx,
       "zxAnEthOamLoopbackControlRx": zxAnEthOamLoopbackControlRx,
       "zxAnEthOamVariableRequestTx": zxAnEthOamVariableRequestTx,
       "zxAnEthOamVariableRequestRx": zxAnEthOamVariableRequestRx,
       "zxAnEthOamVariableResponseTx": zxAnEthOamVariableResponseTx,
       "zxAnEthOamVariableResponseRx": zxAnEthOamVariableResponseRx,
       "zxAnEthOamOrgSpecificTx": zxAnEthOamOrgSpecificTx,
       "zxAnEthOamOrgSpecificRx": zxAnEthOamOrgSpecificRx,
       "zxAnEthOamUnsupportedCodesTx": zxAnEthOamUnsupportedCodesTx,
       "zxAnEthOamUnsupportedCodesRx": zxAnEthOamUnsupportedCodesRx,
       "zxAnEthOamFramesLostDueToOam": zxAnEthOamFramesLostDueToOam,
       "zxAnEthOamEventConfigTable": zxAnEthOamEventConfigTable,
       "zxAnEthOamEventConfigEntry": zxAnEthOamEventConfigEntry,
       "zxAnEthOamErrSymPeriodWindowHi": zxAnEthOamErrSymPeriodWindowHi,
       "zxAnEthOamErrSymPeriodWindowLo": zxAnEthOamErrSymPeriodWindowLo,
       "zxAnEthOamErrSymPeriodThresholdHi": zxAnEthOamErrSymPeriodThresholdHi,
       "zxAnEthOamErrSymPeriodThresholdLo": zxAnEthOamErrSymPeriodThresholdLo,
       "zxAnEthOamErrSymPeriodEvNotifEnable": zxAnEthOamErrSymPeriodEvNotifEnable,
       "zxAnEthOamErrFramePeriodWindow": zxAnEthOamErrFramePeriodWindow,
       "zxAnEthOamErrFramePeriodThreshold": zxAnEthOamErrFramePeriodThreshold,
       "zxAnEthOamErrFramePeriodEvNotifEnable": zxAnEthOamErrFramePeriodEvNotifEnable,
       "zxAnEthOamErrFrameWindow": zxAnEthOamErrFrameWindow,
       "zxAnEthOamErrFrameThreshold": zxAnEthOamErrFrameThreshold,
       "zxAnEthOamErrFrameEvNotifEnable": zxAnEthOamErrFrameEvNotifEnable,
       "zxAnEthOamErrFrameSecsSummaryWindow": zxAnEthOamErrFrameSecsSummaryWindow,
       "zxAnEthOamErrFrameSecsSummaryThreshold": zxAnEthOamErrFrameSecsSummaryThreshold,
       "zxAnEthOamErrFrameSecsEvNotifEnable": zxAnEthOamErrFrameSecsEvNotifEnable,
       "zxAnEthOamDyingGaspEnable": zxAnEthOamDyingGaspEnable,
       "zxAnEthOamCriticalEventEnable": zxAnEthOamCriticalEventEnable,
       "zxAnEthOamEventLogTable": zxAnEthOamEventLogTable,
       "zxAnEthOamEventLogEntry": zxAnEthOamEventLogEntry,
       "zxAnEthOamEventLogIndex": zxAnEthOamEventLogIndex,
       "zxAnEthOamEventLogTimestamp": zxAnEthOamEventLogTimestamp,
       "zxAnEthOamEventLogOui": zxAnEthOamEventLogOui,
       "zxAnEthOamEventLogType": zxAnEthOamEventLogType,
       "zxAnEthOamEventLogLocation": zxAnEthOamEventLogLocation,
       "zxAnEthOamEventLogWindowHi": zxAnEthOamEventLogWindowHi,
       "zxAnEthOamEventLogWindowLo": zxAnEthOamEventLogWindowLo,
       "zxAnEthOamEventLogThresholdHi": zxAnEthOamEventLogThresholdHi,
       "zxAnEthOamEventLogThresholdLo": zxAnEthOamEventLogThresholdLo,
       "zxAnEthOamEventLogValue": zxAnEthOamEventLogValue,
       "zxAnEthOamEventLogRunningTotal": zxAnEthOamEventLogRunningTotal,
       "zxAnEthOamEventLogEventTotal": zxAnEthOamEventLogEventTotal,
       "zxAnEthOamGlobalEnable": zxAnEthOamGlobalEnable}
)
