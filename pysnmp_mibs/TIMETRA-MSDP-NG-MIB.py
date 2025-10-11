# SNMP MIB module (TIMETRA-MSDP-NG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-MSDP-NG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:01:59 2025
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
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TNamedItem,
 TNamedItemOrEmpty,
 TPolicyStatementNameOrEmpty,
 TmnxAdminState) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPolicyStatementNameOrEmpty",
    "TmnxAdminState")

(vRtrID,) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID")


# MODULE-IDENTITY

timetraMsdpNgMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 104)
)
if mibBuilder.loadTexts:
    timetraMsdpNgMIBModule.setRevisions(
        ("2016-01-01 00:00",
         "2014-11-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxMsdpNgConformance_ObjectIdentity = ObjectIdentity
tmnxMsdpNgConformance = _TmnxMsdpNgConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 104)
)
_TmnxMsdpNgCompliances_ObjectIdentity = ObjectIdentity
tmnxMsdpNgCompliances = _TmnxMsdpNgCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 104, 1)
)
_TmnxMsdpNgGroups_ObjectIdentity = ObjectIdentity
tmnxMsdpNgGroups = _TmnxMsdpNgGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 104, 2)
)
_TmnxMsdpNgObjects_ObjectIdentity = ObjectIdentity
tmnxMsdpNgObjects = _TmnxMsdpNgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104)
)
_TmnxMsdpNgGlobals_ObjectIdentity = ObjectIdentity
tmnxMsdpNgGlobals = _TmnxMsdpNgGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 1)
)
_TmnxMsdpNgGeneralTableLstChanged_Type = TimeStamp
_TmnxMsdpNgGeneralTableLstChanged_Object = MibScalar
tmnxMsdpNgGeneralTableLstChanged = _TmnxMsdpNgGeneralTableLstChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 1, 1),
    _TmnxMsdpNgGeneralTableLstChanged_Type()
)
tmnxMsdpNgGeneralTableLstChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgGeneralTableLstChanged.setStatus("current")
_TmnxMsdpNgGeneralTable_Object = MibTable
tmnxMsdpNgGeneralTable = _TmnxMsdpNgGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2)
)
if mibBuilder.loadTexts:
    tmnxMsdpNgGeneralTable.setStatus("current")
_TmnxMsdpNgGeneralEntry_Object = MibTableRow
tmnxMsdpNgGeneralEntry = _TmnxMsdpNgGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2, 1)
)
tmnxMsdpNgGeneralEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    tmnxMsdpNgGeneralEntry.setStatus("current")


class _TmnxMsdpNgMaxActiveSources_Type(Integer32):
    """Custom type tmnxMsdpNgMaxActiveSources based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1000000),
    )


_TmnxMsdpNgMaxActiveSources_Type.__name__ = "Integer32"
_TmnxMsdpNgMaxActiveSources_Object = MibTableColumn
tmnxMsdpNgMaxActiveSources = _TmnxMsdpNgMaxActiveSources_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2, 1, 1),
    _TmnxMsdpNgMaxActiveSources_Type()
)
tmnxMsdpNgMaxActiveSources.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMsdpNgMaxActiveSources.setStatus("current")


class _TmnxMsdpNgMsgRcvRate_Type(Unsigned32):
    """Custom type tmnxMsdpNgMsgRcvRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 10000),
    )


_TmnxMsdpNgMsgRcvRate_Type.__name__ = "Unsigned32"
_TmnxMsdpNgMsgRcvRate_Object = MibTableColumn
tmnxMsdpNgMsgRcvRate = _TmnxMsdpNgMsgRcvRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2, 1, 2),
    _TmnxMsdpNgMsgRcvRate_Type()
)
tmnxMsdpNgMsgRcvRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMsdpNgMsgRcvRate.setStatus("current")


class _TmnxMsdpNgMsgRcvRateTime_Type(Unsigned32):
    """Custom type tmnxMsdpNgMsgRcvRateTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 600),
    )


_TmnxMsdpNgMsgRcvRateTime_Type.__name__ = "Unsigned32"
_TmnxMsdpNgMsgRcvRateTime_Object = MibTableColumn
tmnxMsdpNgMsgRcvRateTime = _TmnxMsdpNgMsgRcvRateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2, 1, 3),
    _TmnxMsdpNgMsgRcvRateTime_Type()
)
tmnxMsdpNgMsgRcvRateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMsdpNgMsgRcvRateTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMsdpNgMsgRcvRateTime.setUnits("seconds")


class _TmnxMsdpNgMsgRcvRateThd_Type(Gauge32):
    """Custom type tmnxMsdpNgMsgRcvRateThd based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000000),
    )


_TmnxMsdpNgMsgRcvRateThd_Type.__name__ = "Gauge32"
_TmnxMsdpNgMsgRcvRateThd_Object = MibTableColumn
tmnxMsdpNgMsgRcvRateThd = _TmnxMsdpNgMsgRcvRateThd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2, 1, 4),
    _TmnxMsdpNgMsgRcvRateThd_Type()
)
tmnxMsdpNgMsgRcvRateThd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMsdpNgMsgRcvRateThd.setStatus("current")


class _TmnxMsdpNgDataEncapsulation_Type(TruthValue):
    """Custom type tmnxMsdpNgDataEncapsulation based on TruthValue"""
    defaultValue = 1


_TmnxMsdpNgDataEncapsulation_Type.__name__ = "TruthValue"
_TmnxMsdpNgDataEncapsulation_Object = MibTableColumn
tmnxMsdpNgDataEncapsulation = _TmnxMsdpNgDataEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2, 1, 5),
    _TmnxMsdpNgDataEncapsulation_Type()
)
tmnxMsdpNgDataEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMsdpNgDataEncapsulation.setStatus("current")


class _TmnxMsdpNgAdminState_Type(TmnxAdminState):
    """Custom type tmnxMsdpNgAdminState based on TmnxAdminState"""
    defaultValue = 2


_TmnxMsdpNgAdminState_Type.__name__ = "TmnxAdminState"
_TmnxMsdpNgAdminState_Object = MibTableColumn
tmnxMsdpNgAdminState = _TmnxMsdpNgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2, 1, 6),
    _TmnxMsdpNgAdminState_Type()
)
tmnxMsdpNgAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMsdpNgAdminState.setStatus("current")


class _TmnxMsdpNgExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgExportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgExportPolicy1_Object = MibTableColumn
tmnxMsdpNgExportPolicy1 = _TmnxMsdpNgExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2, 1, 7),
    _TmnxMsdpNgExportPolicy1_Type()
)
tmnxMsdpNgExportPolicy1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMsdpNgExportPolicy1.setStatus("current")


class _TmnxMsdpNgExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgExportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgExportPolicy2_Object = MibTableColumn
tmnxMsdpNgExportPolicy2 = _TmnxMsdpNgExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2, 1, 8),
    _TmnxMsdpNgExportPolicy2_Type()
)
tmnxMsdpNgExportPolicy2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMsdpNgExportPolicy2.setStatus("current")


class _TmnxMsdpNgExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgExportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgExportPolicy3_Object = MibTableColumn
tmnxMsdpNgExportPolicy3 = _TmnxMsdpNgExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2, 1, 9),
    _TmnxMsdpNgExportPolicy3_Type()
)
tmnxMsdpNgExportPolicy3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMsdpNgExportPolicy3.setStatus("current")


class _TmnxMsdpNgExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgExportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgExportPolicy4_Object = MibTableColumn
tmnxMsdpNgExportPolicy4 = _TmnxMsdpNgExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2, 1, 10),
    _TmnxMsdpNgExportPolicy4_Type()
)
tmnxMsdpNgExportPolicy4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMsdpNgExportPolicy4.setStatus("current")


class _TmnxMsdpNgExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgExportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgExportPolicy5_Object = MibTableColumn
tmnxMsdpNgExportPolicy5 = _TmnxMsdpNgExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2, 1, 11),
    _TmnxMsdpNgExportPolicy5_Type()
)
tmnxMsdpNgExportPolicy5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMsdpNgExportPolicy5.setStatus("current")


class _TmnxMsdpNgImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgImportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgImportPolicy1_Object = MibTableColumn
tmnxMsdpNgImportPolicy1 = _TmnxMsdpNgImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2, 1, 12),
    _TmnxMsdpNgImportPolicy1_Type()
)
tmnxMsdpNgImportPolicy1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMsdpNgImportPolicy1.setStatus("current")


class _TmnxMsdpNgImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgImportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgImportPolicy2_Object = MibTableColumn
tmnxMsdpNgImportPolicy2 = _TmnxMsdpNgImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2, 1, 13),
    _TmnxMsdpNgImportPolicy2_Type()
)
tmnxMsdpNgImportPolicy2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMsdpNgImportPolicy2.setStatus("current")


class _TmnxMsdpNgImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgImportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgImportPolicy3_Object = MibTableColumn
tmnxMsdpNgImportPolicy3 = _TmnxMsdpNgImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2, 1, 14),
    _TmnxMsdpNgImportPolicy3_Type()
)
tmnxMsdpNgImportPolicy3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMsdpNgImportPolicy3.setStatus("current")


class _TmnxMsdpNgImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgImportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgImportPolicy4_Object = MibTableColumn
tmnxMsdpNgImportPolicy4 = _TmnxMsdpNgImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2, 1, 15),
    _TmnxMsdpNgImportPolicy4_Type()
)
tmnxMsdpNgImportPolicy4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMsdpNgImportPolicy4.setStatus("current")


class _TmnxMsdpNgImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgImportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgImportPolicy5_Object = MibTableColumn
tmnxMsdpNgImportPolicy5 = _TmnxMsdpNgImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2, 1, 16),
    _TmnxMsdpNgImportPolicy5_Type()
)
tmnxMsdpNgImportPolicy5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMsdpNgImportPolicy5.setStatus("current")


class _TmnxMsdpNgLocalAddressType_Type(InetAddressType):
    """Custom type tmnxMsdpNgLocalAddressType based on InetAddressType"""
    defaultValue = 0


_TmnxMsdpNgLocalAddressType_Type.__name__ = "InetAddressType"
_TmnxMsdpNgLocalAddressType_Object = MibTableColumn
tmnxMsdpNgLocalAddressType = _TmnxMsdpNgLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2, 1, 17),
    _TmnxMsdpNgLocalAddressType_Type()
)
tmnxMsdpNgLocalAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMsdpNgLocalAddressType.setStatus("current")


class _TmnxMsdpNgLocalAddress_Type(InetAddress):
    """Custom type tmnxMsdpNgLocalAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpNgLocalAddress_Type.__name__ = "InetAddress"
_TmnxMsdpNgLocalAddress_Object = MibTableColumn
tmnxMsdpNgLocalAddress = _TmnxMsdpNgLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2, 1, 18),
    _TmnxMsdpNgLocalAddress_Type()
)
tmnxMsdpNgLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMsdpNgLocalAddress.setStatus("current")
_TmnxMsdpNgStatusPeerCount_Type = Gauge32
_TmnxMsdpNgStatusPeerCount_Object = MibTableColumn
tmnxMsdpNgStatusPeerCount = _TmnxMsdpNgStatusPeerCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2, 1, 19),
    _TmnxMsdpNgStatusPeerCount_Type()
)
tmnxMsdpNgStatusPeerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgStatusPeerCount.setStatus("current")
_TmnxMsdpNgStatusPeersEstablished_Type = Gauge32
_TmnxMsdpNgStatusPeersEstablished_Object = MibTableColumn
tmnxMsdpNgStatusPeersEstablished = _TmnxMsdpNgStatusPeersEstablished_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2, 1, 20),
    _TmnxMsdpNgStatusPeersEstablished_Type()
)
tmnxMsdpNgStatusPeersEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgStatusPeersEstablished.setStatus("current")
_TmnxMsdpNgStatusSACount_Type = Gauge32
_TmnxMsdpNgStatusSACount_Object = MibTableColumn
tmnxMsdpNgStatusSACount = _TmnxMsdpNgStatusSACount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2, 1, 21),
    _TmnxMsdpNgStatusSACount_Type()
)
tmnxMsdpNgStatusSACount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgStatusSACount.setStatus("current")
_TmnxMsdpNgStatusLastTimeUp_Type = TimeStamp
_TmnxMsdpNgStatusLastTimeUp_Object = MibTableColumn
tmnxMsdpNgStatusLastTimeUp = _TmnxMsdpNgStatusLastTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2, 1, 22),
    _TmnxMsdpNgStatusLastTimeUp_Type()
)
tmnxMsdpNgStatusLastTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgStatusLastTimeUp.setStatus("current")
_TmnxMsdpNgStatusActSrcLimExceed_Type = Counter32
_TmnxMsdpNgStatusActSrcLimExceed_Object = MibTableColumn
tmnxMsdpNgStatusActSrcLimExceed = _TmnxMsdpNgStatusActSrcLimExceed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2, 1, 23),
    _TmnxMsdpNgStatusActSrcLimExceed_Type()
)
tmnxMsdpNgStatusActSrcLimExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgStatusActSrcLimExceed.setStatus("current")


class _TmnxMsdpNgRpfLookupSequence_Type(Integer32):
    """Custom type tmnxMsdpNgRpfLookupSequence based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mucastRouteTable", 0),
          ("ucastRouteTable", 1),
          ("both", 2))
    )


_TmnxMsdpNgRpfLookupSequence_Type.__name__ = "Integer32"
_TmnxMsdpNgRpfLookupSequence_Object = MibTableColumn
tmnxMsdpNgRpfLookupSequence = _TmnxMsdpNgRpfLookupSequence_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2, 1, 24),
    _TmnxMsdpNgRpfLookupSequence_Type()
)
tmnxMsdpNgRpfLookupSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMsdpNgRpfLookupSequence.setStatus("current")


class _TmnxMsdpNgSACacheLifetime_Type(Unsigned32):
    """Custom type tmnxMsdpNgSACacheLifetime based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 600),
    )


_TmnxMsdpNgSACacheLifetime_Type.__name__ = "Unsigned32"
_TmnxMsdpNgSACacheLifetime_Object = MibTableColumn
tmnxMsdpNgSACacheLifetime = _TmnxMsdpNgSACacheLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2, 1, 25),
    _TmnxMsdpNgSACacheLifetime_Type()
)
tmnxMsdpNgSACacheLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMsdpNgSACacheLifetime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMsdpNgSACacheLifetime.setUnits("seconds")
_TmnxMsdpNgSARejectExportPolicy_Type = Counter32
_TmnxMsdpNgSARejectExportPolicy_Object = MibTableColumn
tmnxMsdpNgSARejectExportPolicy = _TmnxMsdpNgSARejectExportPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2, 1, 26),
    _TmnxMsdpNgSARejectExportPolicy_Type()
)
tmnxMsdpNgSARejectExportPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgSARejectExportPolicy.setStatus("current")
_TmnxMsdpNgSARejectImportPolicy_Type = Counter32
_TmnxMsdpNgSARejectImportPolicy_Object = MibTableColumn
tmnxMsdpNgSARejectImportPolicy = _TmnxMsdpNgSARejectImportPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 2, 1, 27),
    _TmnxMsdpNgSARejectImportPolicy_Type()
)
tmnxMsdpNgSARejectImportPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgSARejectImportPolicy.setStatus("current")
_TmnxMsdpNgPeerTable_Object = MibTable
tmnxMsdpNgPeerTable = _TmnxMsdpNgPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3)
)
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerTable.setStatus("current")
_TmnxMsdpNgPeerEntry_Object = MibTableRow
tmnxMsdpNgPeerEntry = _TmnxMsdpNgPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1)
)
tmnxMsdpNgPeerEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerAddressType"),
    (0, "TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerAddress"),
)
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerEntry.setStatus("current")
_TmnxMsdpNgPeerAddressType_Type = InetAddressType
_TmnxMsdpNgPeerAddressType_Object = MibTableColumn
tmnxMsdpNgPeerAddressType = _TmnxMsdpNgPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 1),
    _TmnxMsdpNgPeerAddressType_Type()
)
tmnxMsdpNgPeerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerAddressType.setStatus("current")


class _TmnxMsdpNgPeerAddress_Type(InetAddress):
    """Custom type tmnxMsdpNgPeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpNgPeerAddress_Type.__name__ = "InetAddress"
_TmnxMsdpNgPeerAddress_Object = MibTableColumn
tmnxMsdpNgPeerAddress = _TmnxMsdpNgPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 2),
    _TmnxMsdpNgPeerAddress_Type()
)
tmnxMsdpNgPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerAddress.setStatus("current")
_TmnxMsdpNgPeerRowStatus_Type = RowStatus
_TmnxMsdpNgPeerRowStatus_Object = MibTableColumn
tmnxMsdpNgPeerRowStatus = _TmnxMsdpNgPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 3),
    _TmnxMsdpNgPeerRowStatus_Type()
)
tmnxMsdpNgPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerRowStatus.setStatus("current")


class _TmnxMsdpNgPeerMaxActiveSources_Type(Integer32):
    """Custom type tmnxMsdpNgPeerMaxActiveSources based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1000000),
    )


_TmnxMsdpNgPeerMaxActiveSources_Type.__name__ = "Integer32"
_TmnxMsdpNgPeerMaxActiveSources_Object = MibTableColumn
tmnxMsdpNgPeerMaxActiveSources = _TmnxMsdpNgPeerMaxActiveSources_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 4),
    _TmnxMsdpNgPeerMaxActiveSources_Type()
)
tmnxMsdpNgPeerMaxActiveSources.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerMaxActiveSources.setStatus("current")


class _TmnxMsdpNgPeerMsgRcvRate_Type(Unsigned32):
    """Custom type tmnxMsdpNgPeerMsgRcvRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 10000),
    )


_TmnxMsdpNgPeerMsgRcvRate_Type.__name__ = "Unsigned32"
_TmnxMsdpNgPeerMsgRcvRate_Object = MibTableColumn
tmnxMsdpNgPeerMsgRcvRate = _TmnxMsdpNgPeerMsgRcvRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 5),
    _TmnxMsdpNgPeerMsgRcvRate_Type()
)
tmnxMsdpNgPeerMsgRcvRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerMsgRcvRate.setStatus("current")


class _TmnxMsdpNgPeerMsgRcvRateTime_Type(Unsigned32):
    """Custom type tmnxMsdpNgPeerMsgRcvRateTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 600),
    )


_TmnxMsdpNgPeerMsgRcvRateTime_Type.__name__ = "Unsigned32"
_TmnxMsdpNgPeerMsgRcvRateTime_Object = MibTableColumn
tmnxMsdpNgPeerMsgRcvRateTime = _TmnxMsdpNgPeerMsgRcvRateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 6),
    _TmnxMsdpNgPeerMsgRcvRateTime_Type()
)
tmnxMsdpNgPeerMsgRcvRateTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerMsgRcvRateTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerMsgRcvRateTime.setUnits("seconds")


class _TmnxMsdpNgPeerMsgRcvRateThd_Type(Gauge32):
    """Custom type tmnxMsdpNgPeerMsgRcvRateThd based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000000),
    )


_TmnxMsdpNgPeerMsgRcvRateThd_Type.__name__ = "Gauge32"
_TmnxMsdpNgPeerMsgRcvRateThd_Object = MibTableColumn
tmnxMsdpNgPeerMsgRcvRateThd = _TmnxMsdpNgPeerMsgRcvRateThd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 7),
    _TmnxMsdpNgPeerMsgRcvRateThd_Type()
)
tmnxMsdpNgPeerMsgRcvRateThd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerMsgRcvRateThd.setStatus("current")


class _TmnxMsdpNgPeerAuthKey_Type(OctetString):
    """Custom type tmnxMsdpNgPeerAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TmnxMsdpNgPeerAuthKey_Type.__name__ = "OctetString"
_TmnxMsdpNgPeerAuthKey_Object = MibTableColumn
tmnxMsdpNgPeerAuthKey = _TmnxMsdpNgPeerAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 8),
    _TmnxMsdpNgPeerAuthKey_Type()
)
tmnxMsdpNgPeerAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerAuthKey.setStatus("current")


class _TmnxMsdpNgPeerAuthKeyEncrypted_Type(TruthValue):
    """Custom type tmnxMsdpNgPeerAuthKeyEncrypted based on TruthValue"""
    defaultValue = 1


_TmnxMsdpNgPeerAuthKeyEncrypted_Type.__name__ = "TruthValue"
_TmnxMsdpNgPeerAuthKeyEncrypted_Object = MibTableColumn
tmnxMsdpNgPeerAuthKeyEncrypted = _TmnxMsdpNgPeerAuthKeyEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 9),
    _TmnxMsdpNgPeerAuthKeyEncrypted_Type()
)
tmnxMsdpNgPeerAuthKeyEncrypted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerAuthKeyEncrypted.setStatus("current")


class _TmnxMsdpNgPeerDefaultPeer_Type(TruthValue):
    """Custom type tmnxMsdpNgPeerDefaultPeer based on TruthValue"""
    defaultValue = 2


_TmnxMsdpNgPeerDefaultPeer_Type.__name__ = "TruthValue"
_TmnxMsdpNgPeerDefaultPeer_Object = MibTableColumn
tmnxMsdpNgPeerDefaultPeer = _TmnxMsdpNgPeerDefaultPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 10),
    _TmnxMsdpNgPeerDefaultPeer_Type()
)
tmnxMsdpNgPeerDefaultPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerDefaultPeer.setStatus("current")


class _TmnxMsdpNgPeerAdminState_Type(TmnxAdminState):
    """Custom type tmnxMsdpNgPeerAdminState based on TmnxAdminState"""
    defaultValue = 2


_TmnxMsdpNgPeerAdminState_Type.__name__ = "TmnxAdminState"
_TmnxMsdpNgPeerAdminState_Object = MibTableColumn
tmnxMsdpNgPeerAdminState = _TmnxMsdpNgPeerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 11),
    _TmnxMsdpNgPeerAdminState_Type()
)
tmnxMsdpNgPeerAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerAdminState.setStatus("current")


class _TmnxMsdpNgPeerExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerExportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerExportPolicy1_Object = MibTableColumn
tmnxMsdpNgPeerExportPolicy1 = _TmnxMsdpNgPeerExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 12),
    _TmnxMsdpNgPeerExportPolicy1_Type()
)
tmnxMsdpNgPeerExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerExportPolicy1.setStatus("current")


class _TmnxMsdpNgPeerExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerExportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerExportPolicy2_Object = MibTableColumn
tmnxMsdpNgPeerExportPolicy2 = _TmnxMsdpNgPeerExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 13),
    _TmnxMsdpNgPeerExportPolicy2_Type()
)
tmnxMsdpNgPeerExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerExportPolicy2.setStatus("current")


class _TmnxMsdpNgPeerExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerExportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerExportPolicy3_Object = MibTableColumn
tmnxMsdpNgPeerExportPolicy3 = _TmnxMsdpNgPeerExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 14),
    _TmnxMsdpNgPeerExportPolicy3_Type()
)
tmnxMsdpNgPeerExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerExportPolicy3.setStatus("current")


class _TmnxMsdpNgPeerExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerExportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerExportPolicy4_Object = MibTableColumn
tmnxMsdpNgPeerExportPolicy4 = _TmnxMsdpNgPeerExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 15),
    _TmnxMsdpNgPeerExportPolicy4_Type()
)
tmnxMsdpNgPeerExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerExportPolicy4.setStatus("current")


class _TmnxMsdpNgPeerExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerExportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerExportPolicy5_Object = MibTableColumn
tmnxMsdpNgPeerExportPolicy5 = _TmnxMsdpNgPeerExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 16),
    _TmnxMsdpNgPeerExportPolicy5_Type()
)
tmnxMsdpNgPeerExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerExportPolicy5.setStatus("current")


class _TmnxMsdpNgPeerImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerImportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerImportPolicy1_Object = MibTableColumn
tmnxMsdpNgPeerImportPolicy1 = _TmnxMsdpNgPeerImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 17),
    _TmnxMsdpNgPeerImportPolicy1_Type()
)
tmnxMsdpNgPeerImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerImportPolicy1.setStatus("current")


class _TmnxMsdpNgPeerImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerImportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerImportPolicy2_Object = MibTableColumn
tmnxMsdpNgPeerImportPolicy2 = _TmnxMsdpNgPeerImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 18),
    _TmnxMsdpNgPeerImportPolicy2_Type()
)
tmnxMsdpNgPeerImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerImportPolicy2.setStatus("current")


class _TmnxMsdpNgPeerImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerImportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerImportPolicy3_Object = MibTableColumn
tmnxMsdpNgPeerImportPolicy3 = _TmnxMsdpNgPeerImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 19),
    _TmnxMsdpNgPeerImportPolicy3_Type()
)
tmnxMsdpNgPeerImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerImportPolicy3.setStatus("current")


class _TmnxMsdpNgPeerImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerImportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerImportPolicy4_Object = MibTableColumn
tmnxMsdpNgPeerImportPolicy4 = _TmnxMsdpNgPeerImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 20),
    _TmnxMsdpNgPeerImportPolicy4_Type()
)
tmnxMsdpNgPeerImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerImportPolicy4.setStatus("current")


class _TmnxMsdpNgPeerImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerImportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerImportPolicy5_Object = MibTableColumn
tmnxMsdpNgPeerImportPolicy5 = _TmnxMsdpNgPeerImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 21),
    _TmnxMsdpNgPeerImportPolicy5_Type()
)
tmnxMsdpNgPeerImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerImportPolicy5.setStatus("current")


class _TmnxMsdpNgPeerLocalAddressType_Type(InetAddressType):
    """Custom type tmnxMsdpNgPeerLocalAddressType based on InetAddressType"""
    defaultValue = 0


_TmnxMsdpNgPeerLocalAddressType_Type.__name__ = "InetAddressType"
_TmnxMsdpNgPeerLocalAddressType_Object = MibTableColumn
tmnxMsdpNgPeerLocalAddressType = _TmnxMsdpNgPeerLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 22),
    _TmnxMsdpNgPeerLocalAddressType_Type()
)
tmnxMsdpNgPeerLocalAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerLocalAddressType.setStatus("current")


class _TmnxMsdpNgPeerLocalAddress_Type(InetAddress):
    """Custom type tmnxMsdpNgPeerLocalAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpNgPeerLocalAddress_Type.__name__ = "InetAddress"
_TmnxMsdpNgPeerLocalAddress_Object = MibTableColumn
tmnxMsdpNgPeerLocalAddress = _TmnxMsdpNgPeerLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 23),
    _TmnxMsdpNgPeerLocalAddress_Type()
)
tmnxMsdpNgPeerLocalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerLocalAddress.setStatus("current")


class _TmnxMsdpNgPeerState_Type(Integer32):
    """Custom type tmnxMsdpNgPeerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("listen", 0),
          ("established", 1),
          ("inactive", 2),
          ("disabled", 3),
          ("connecting", 4))
    )


_TmnxMsdpNgPeerState_Type.__name__ = "Integer32"
_TmnxMsdpNgPeerState_Object = MibTableColumn
tmnxMsdpNgPeerState = _TmnxMsdpNgPeerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 24),
    _TmnxMsdpNgPeerState_Type()
)
tmnxMsdpNgPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerState.setStatus("current")
_TmnxMsdpNgPeerLastUpOrDown_Type = TimeStamp
_TmnxMsdpNgPeerLastUpOrDown_Object = MibTableColumn
tmnxMsdpNgPeerLastUpOrDown = _TmnxMsdpNgPeerLastUpOrDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 25),
    _TmnxMsdpNgPeerLastUpOrDown_Type()
)
tmnxMsdpNgPeerLastUpOrDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerLastUpOrDown.setStatus("current")
_TmnxMsdpNgPeerConRetry_Type = Counter32
_TmnxMsdpNgPeerConRetry_Object = MibTableColumn
tmnxMsdpNgPeerConRetry = _TmnxMsdpNgPeerConRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 26),
    _TmnxMsdpNgPeerConRetry_Type()
)
tmnxMsdpNgPeerConRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerConRetry.setStatus("current")
_TmnxMsdpNgPeerStateTimer_Type = Unsigned32
_TmnxMsdpNgPeerStateTimer_Object = MibTableColumn
tmnxMsdpNgPeerStateTimer = _TmnxMsdpNgPeerStateTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 27),
    _TmnxMsdpNgPeerStateTimer_Type()
)
tmnxMsdpNgPeerStateTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerStateTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerStateTimer.setUnits("seconds")
_TmnxMsdpNgPeerTimeout_Type = Unsigned32
_TmnxMsdpNgPeerTimeout_Object = MibTableColumn
tmnxMsdpNgPeerTimeout = _TmnxMsdpNgPeerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 28),
    _TmnxMsdpNgPeerTimeout_Type()
)
tmnxMsdpNgPeerTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerTimeout.setUnits("seconds")
_TmnxMsdpNgPeerSAAccepted_Type = Gauge32
_TmnxMsdpNgPeerSAAccepted_Object = MibTableColumn
tmnxMsdpNgPeerSAAccepted = _TmnxMsdpNgPeerSAAccepted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 29),
    _TmnxMsdpNgPeerSAAccepted_Type()
)
tmnxMsdpNgPeerSAAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerSAAccepted.setStatus("current")
_TmnxMsdpNgPeerSARx_Type = Gauge32
_TmnxMsdpNgPeerSARx_Object = MibTableColumn
tmnxMsdpNgPeerSARx = _TmnxMsdpNgPeerSARx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 30),
    _TmnxMsdpNgPeerSARx_Type()
)
tmnxMsdpNgPeerSARx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerSARx.setStatus("current")
_TmnxMsdpNgPeerLastASLimit_Type = TimeStamp
_TmnxMsdpNgPeerLastASLimit_Object = MibTableColumn
tmnxMsdpNgPeerLastASLimit = _TmnxMsdpNgPeerLastASLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 31),
    _TmnxMsdpNgPeerLastASLimit_Type()
)
tmnxMsdpNgPeerLastASLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerLastASLimit.setStatus("current")
_TmnxMsdpNgPeerOperLclAddrType_Type = InetAddressType
_TmnxMsdpNgPeerOperLclAddrType_Object = MibTableColumn
tmnxMsdpNgPeerOperLclAddrType = _TmnxMsdpNgPeerOperLclAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 32),
    _TmnxMsdpNgPeerOperLclAddrType_Type()
)
tmnxMsdpNgPeerOperLclAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerOperLclAddrType.setStatus("current")


class _TmnxMsdpNgPeerOperLclAddr_Type(InetAddress):
    """Custom type tmnxMsdpNgPeerOperLclAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpNgPeerOperLclAddr_Type.__name__ = "InetAddress"
_TmnxMsdpNgPeerOperLclAddr_Object = MibTableColumn
tmnxMsdpNgPeerOperLclAddr = _TmnxMsdpNgPeerOperLclAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 3, 1, 33),
    _TmnxMsdpNgPeerOperLclAddr_Type()
)
tmnxMsdpNgPeerOperLclAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerOperLclAddr.setStatus("current")
_TmnxMsdpNgPeerGroupTable_Object = MibTable
tmnxMsdpNgPeerGroupTable = _TmnxMsdpNgPeerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 4)
)
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGroupTable.setStatus("current")
_TmnxMsdpNgPeerGroupEntry_Object = MibTableRow
tmnxMsdpNgPeerGroupEntry = _TmnxMsdpNgPeerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 4, 1)
)
tmnxMsdpNgPeerGroupEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGroupName"),
)
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGroupEntry.setStatus("current")
_TmnxMsdpNgPeerGroupName_Type = TNamedItem
_TmnxMsdpNgPeerGroupName_Object = MibTableColumn
tmnxMsdpNgPeerGroupName = _TmnxMsdpNgPeerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 4, 1, 1),
    _TmnxMsdpNgPeerGroupName_Type()
)
tmnxMsdpNgPeerGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGroupName.setStatus("current")
_TmnxMsdpNgPeerGroupRowStatus_Type = RowStatus
_TmnxMsdpNgPeerGroupRowStatus_Object = MibTableColumn
tmnxMsdpNgPeerGroupRowStatus = _TmnxMsdpNgPeerGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 4, 1, 2),
    _TmnxMsdpNgPeerGroupRowStatus_Type()
)
tmnxMsdpNgPeerGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGroupRowStatus.setStatus("current")


class _TmnxMsdpNgPeerGroupMsgRcvRate_Type(Unsigned32):
    """Custom type tmnxMsdpNgPeerGroupMsgRcvRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 10000),
    )


_TmnxMsdpNgPeerGroupMsgRcvRate_Type.__name__ = "Unsigned32"
_TmnxMsdpNgPeerGroupMsgRcvRate_Object = MibTableColumn
tmnxMsdpNgPeerGroupMsgRcvRate = _TmnxMsdpNgPeerGroupMsgRcvRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 4, 1, 3),
    _TmnxMsdpNgPeerGroupMsgRcvRate_Type()
)
tmnxMsdpNgPeerGroupMsgRcvRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGroupMsgRcvRate.setStatus("current")


class _TmnxMsdpNgPeerGrpMsgRcvRateTime_Type(Unsigned32):
    """Custom type tmnxMsdpNgPeerGrpMsgRcvRateTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 600),
    )


_TmnxMsdpNgPeerGrpMsgRcvRateTime_Type.__name__ = "Unsigned32"
_TmnxMsdpNgPeerGrpMsgRcvRateTime_Object = MibTableColumn
tmnxMsdpNgPeerGrpMsgRcvRateTime = _TmnxMsdpNgPeerGrpMsgRcvRateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 4, 1, 4),
    _TmnxMsdpNgPeerGrpMsgRcvRateTime_Type()
)
tmnxMsdpNgPeerGrpMsgRcvRateTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpMsgRcvRateTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpMsgRcvRateTime.setUnits("seconds")


class _TmnxMsdpNgPeerGroupMsgRcvRateThd_Type(Gauge32):
    """Custom type tmnxMsdpNgPeerGroupMsgRcvRateThd based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000000),
    )


_TmnxMsdpNgPeerGroupMsgRcvRateThd_Type.__name__ = "Gauge32"
_TmnxMsdpNgPeerGroupMsgRcvRateThd_Object = MibTableColumn
tmnxMsdpNgPeerGroupMsgRcvRateThd = _TmnxMsdpNgPeerGroupMsgRcvRateThd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 4, 1, 5),
    _TmnxMsdpNgPeerGroupMsgRcvRateThd_Type()
)
tmnxMsdpNgPeerGroupMsgRcvRateThd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGroupMsgRcvRateThd.setStatus("current")


class _TmnxMsdpNgPeerGroupAdminState_Type(TmnxAdminState):
    """Custom type tmnxMsdpNgPeerGroupAdminState based on TmnxAdminState"""
    defaultValue = 2


_TmnxMsdpNgPeerGroupAdminState_Type.__name__ = "TmnxAdminState"
_TmnxMsdpNgPeerGroupAdminState_Object = MibTableColumn
tmnxMsdpNgPeerGroupAdminState = _TmnxMsdpNgPeerGroupAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 4, 1, 6),
    _TmnxMsdpNgPeerGroupAdminState_Type()
)
tmnxMsdpNgPeerGroupAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGroupAdminState.setStatus("current")


class _TmnxMsdpNgPeerGroupExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerGroupExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerGroupExportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerGroupExportPolicy1_Object = MibTableColumn
tmnxMsdpNgPeerGroupExportPolicy1 = _TmnxMsdpNgPeerGroupExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 4, 1, 7),
    _TmnxMsdpNgPeerGroupExportPolicy1_Type()
)
tmnxMsdpNgPeerGroupExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGroupExportPolicy1.setStatus("current")


class _TmnxMsdpNgPeerGroupExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerGroupExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerGroupExportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerGroupExportPolicy2_Object = MibTableColumn
tmnxMsdpNgPeerGroupExportPolicy2 = _TmnxMsdpNgPeerGroupExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 4, 1, 8),
    _TmnxMsdpNgPeerGroupExportPolicy2_Type()
)
tmnxMsdpNgPeerGroupExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGroupExportPolicy2.setStatus("current")


class _TmnxMsdpNgPeerGroupExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerGroupExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerGroupExportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerGroupExportPolicy3_Object = MibTableColumn
tmnxMsdpNgPeerGroupExportPolicy3 = _TmnxMsdpNgPeerGroupExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 4, 1, 9),
    _TmnxMsdpNgPeerGroupExportPolicy3_Type()
)
tmnxMsdpNgPeerGroupExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGroupExportPolicy3.setStatus("current")


class _TmnxMsdpNgPeerGroupExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerGroupExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerGroupExportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerGroupExportPolicy4_Object = MibTableColumn
tmnxMsdpNgPeerGroupExportPolicy4 = _TmnxMsdpNgPeerGroupExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 4, 1, 10),
    _TmnxMsdpNgPeerGroupExportPolicy4_Type()
)
tmnxMsdpNgPeerGroupExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGroupExportPolicy4.setStatus("current")


class _TmnxMsdpNgPeerGroupExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerGroupExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerGroupExportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerGroupExportPolicy5_Object = MibTableColumn
tmnxMsdpNgPeerGroupExportPolicy5 = _TmnxMsdpNgPeerGroupExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 4, 1, 11),
    _TmnxMsdpNgPeerGroupExportPolicy5_Type()
)
tmnxMsdpNgPeerGroupExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGroupExportPolicy5.setStatus("current")


class _TmnxMsdpNgPeerGroupImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerGroupImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerGroupImportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerGroupImportPolicy1_Object = MibTableColumn
tmnxMsdpNgPeerGroupImportPolicy1 = _TmnxMsdpNgPeerGroupImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 4, 1, 12),
    _TmnxMsdpNgPeerGroupImportPolicy1_Type()
)
tmnxMsdpNgPeerGroupImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGroupImportPolicy1.setStatus("current")


class _TmnxMsdpNgPeerGroupImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerGroupImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerGroupImportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerGroupImportPolicy2_Object = MibTableColumn
tmnxMsdpNgPeerGroupImportPolicy2 = _TmnxMsdpNgPeerGroupImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 4, 1, 13),
    _TmnxMsdpNgPeerGroupImportPolicy2_Type()
)
tmnxMsdpNgPeerGroupImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGroupImportPolicy2.setStatus("current")


class _TmnxMsdpNgPeerGroupImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerGroupImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerGroupImportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerGroupImportPolicy3_Object = MibTableColumn
tmnxMsdpNgPeerGroupImportPolicy3 = _TmnxMsdpNgPeerGroupImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 4, 1, 14),
    _TmnxMsdpNgPeerGroupImportPolicy3_Type()
)
tmnxMsdpNgPeerGroupImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGroupImportPolicy3.setStatus("current")


class _TmnxMsdpNgPeerGroupImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerGroupImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerGroupImportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerGroupImportPolicy4_Object = MibTableColumn
tmnxMsdpNgPeerGroupImportPolicy4 = _TmnxMsdpNgPeerGroupImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 4, 1, 15),
    _TmnxMsdpNgPeerGroupImportPolicy4_Type()
)
tmnxMsdpNgPeerGroupImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGroupImportPolicy4.setStatus("current")


class _TmnxMsdpNgPeerGroupImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerGroupImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerGroupImportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerGroupImportPolicy5_Object = MibTableColumn
tmnxMsdpNgPeerGroupImportPolicy5 = _TmnxMsdpNgPeerGroupImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 4, 1, 16),
    _TmnxMsdpNgPeerGroupImportPolicy5_Type()
)
tmnxMsdpNgPeerGroupImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGroupImportPolicy5.setStatus("current")


class _TmnxMsdpNgPeerGroupLocalAddrType_Type(InetAddressType):
    """Custom type tmnxMsdpNgPeerGroupLocalAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxMsdpNgPeerGroupLocalAddrType_Type.__name__ = "InetAddressType"
_TmnxMsdpNgPeerGroupLocalAddrType_Object = MibTableColumn
tmnxMsdpNgPeerGroupLocalAddrType = _TmnxMsdpNgPeerGroupLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 4, 1, 17),
    _TmnxMsdpNgPeerGroupLocalAddrType_Type()
)
tmnxMsdpNgPeerGroupLocalAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGroupLocalAddrType.setStatus("current")


class _TmnxMsdpNgPeerGroupLocalAddress_Type(InetAddress):
    """Custom type tmnxMsdpNgPeerGroupLocalAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpNgPeerGroupLocalAddress_Type.__name__ = "InetAddress"
_TmnxMsdpNgPeerGroupLocalAddress_Object = MibTableColumn
tmnxMsdpNgPeerGroupLocalAddress = _TmnxMsdpNgPeerGroupLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 4, 1, 18),
    _TmnxMsdpNgPeerGroupLocalAddress_Type()
)
tmnxMsdpNgPeerGroupLocalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGroupLocalAddress.setStatus("current")


class _TmnxMsdpNgPeerGroupMode_Type(Integer32):
    """Custom type tmnxMsdpNgPeerGroupMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standard", 1),
          ("mesh-group", 2))
    )


_TmnxMsdpNgPeerGroupMode_Type.__name__ = "Integer32"
_TmnxMsdpNgPeerGroupMode_Object = MibTableColumn
tmnxMsdpNgPeerGroupMode = _TmnxMsdpNgPeerGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 4, 1, 19),
    _TmnxMsdpNgPeerGroupMode_Type()
)
tmnxMsdpNgPeerGroupMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGroupMode.setStatus("current")


class _TmnxMsdpNgPeerGroupMaxActSources_Type(Integer32):
    """Custom type tmnxMsdpNgPeerGroupMaxActSources based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1000000),
    )


_TmnxMsdpNgPeerGroupMaxActSources_Type.__name__ = "Integer32"
_TmnxMsdpNgPeerGroupMaxActSources_Object = MibTableColumn
tmnxMsdpNgPeerGroupMaxActSources = _TmnxMsdpNgPeerGroupMaxActSources_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 4, 1, 20),
    _TmnxMsdpNgPeerGroupMaxActSources_Type()
)
tmnxMsdpNgPeerGroupMaxActSources.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGroupMaxActSources.setStatus("current")
_TmnxMsdpNgPeerGroupActMsgsExMax_Type = Counter32
_TmnxMsdpNgPeerGroupActMsgsExMax_Object = MibTableColumn
tmnxMsdpNgPeerGroupActMsgsExMax = _TmnxMsdpNgPeerGroupActMsgsExMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 4, 1, 21),
    _TmnxMsdpNgPeerGroupActMsgsExMax_Type()
)
tmnxMsdpNgPeerGroupActMsgsExMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGroupActMsgsExMax.setStatus("current")
_TmnxMsdpNgPeerGrpSARejExpPolicy_Type = Counter32
_TmnxMsdpNgPeerGrpSARejExpPolicy_Object = MibTableColumn
tmnxMsdpNgPeerGrpSARejExpPolicy = _TmnxMsdpNgPeerGrpSARejExpPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 4, 1, 22),
    _TmnxMsdpNgPeerGrpSARejExpPolicy_Type()
)
tmnxMsdpNgPeerGrpSARejExpPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpSARejExpPolicy.setStatus("current")
_TmnxMsdpNgPeerGrpSARejImpPolicy_Type = Counter32
_TmnxMsdpNgPeerGrpSARejImpPolicy_Object = MibTableColumn
tmnxMsdpNgPeerGrpSARejImpPolicy = _TmnxMsdpNgPeerGrpSARejImpPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 4, 1, 23),
    _TmnxMsdpNgPeerGrpSARejImpPolicy_Type()
)
tmnxMsdpNgPeerGrpSARejImpPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpSARejImpPolicy.setStatus("current")
_TmnxMsdpNgPeerGrpPeerTable_Object = MibTable
tmnxMsdpNgPeerGrpPeerTable = _TmnxMsdpNgPeerGrpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5)
)
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerTable.setStatus("current")
_TmnxMsdpNgPeerGrpPeerEntry_Object = MibTableRow
tmnxMsdpNgPeerGrpPeerEntry = _TmnxMsdpNgPeerGrpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1)
)
tmnxMsdpNgPeerGrpPeerEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGroupName"),
    (0, "TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerAddressType"),
    (0, "TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerAddress"),
)
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerEntry.setStatus("current")
_TmnxMsdpNgPeerGrpPeerAddressType_Type = InetAddressType
_TmnxMsdpNgPeerGrpPeerAddressType_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerAddressType = _TmnxMsdpNgPeerGrpPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 1),
    _TmnxMsdpNgPeerGrpPeerAddressType_Type()
)
tmnxMsdpNgPeerGrpPeerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerAddressType.setStatus("current")


class _TmnxMsdpNgPeerGrpPeerAddress_Type(InetAddress):
    """Custom type tmnxMsdpNgPeerGrpPeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpNgPeerGrpPeerAddress_Type.__name__ = "InetAddress"
_TmnxMsdpNgPeerGrpPeerAddress_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerAddress = _TmnxMsdpNgPeerGrpPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 2),
    _TmnxMsdpNgPeerGrpPeerAddress_Type()
)
tmnxMsdpNgPeerGrpPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerAddress.setStatus("current")
_TmnxMsdpNgPeerGrpPeerRowStatus_Type = RowStatus
_TmnxMsdpNgPeerGrpPeerRowStatus_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerRowStatus = _TmnxMsdpNgPeerGrpPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 3),
    _TmnxMsdpNgPeerGrpPeerRowStatus_Type()
)
tmnxMsdpNgPeerGrpPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerRowStatus.setStatus("current")


class _TmnxMsdpNgPeerGrpPeerMaxActSrcs_Type(Integer32):
    """Custom type tmnxMsdpNgPeerGrpPeerMaxActSrcs based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1000000),
    )


_TmnxMsdpNgPeerGrpPeerMaxActSrcs_Type.__name__ = "Integer32"
_TmnxMsdpNgPeerGrpPeerMaxActSrcs_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerMaxActSrcs = _TmnxMsdpNgPeerGrpPeerMaxActSrcs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 4),
    _TmnxMsdpNgPeerGrpPeerMaxActSrcs_Type()
)
tmnxMsdpNgPeerGrpPeerMaxActSrcs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerMaxActSrcs.setStatus("current")


class _TmnxMsdpNgPeerGrpPeerMsgRcvRt_Type(Unsigned32):
    """Custom type tmnxMsdpNgPeerGrpPeerMsgRcvRt based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 10000),
    )


_TmnxMsdpNgPeerGrpPeerMsgRcvRt_Type.__name__ = "Unsigned32"
_TmnxMsdpNgPeerGrpPeerMsgRcvRt_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerMsgRcvRt = _TmnxMsdpNgPeerGrpPeerMsgRcvRt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 5),
    _TmnxMsdpNgPeerGrpPeerMsgRcvRt_Type()
)
tmnxMsdpNgPeerGrpPeerMsgRcvRt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerMsgRcvRt.setStatus("current")


class _TmnxMsdpNgPeerGrpPeerMsgRxRtTime_Type(Unsigned32):
    """Custom type tmnxMsdpNgPeerGrpPeerMsgRxRtTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 600),
    )


_TmnxMsdpNgPeerGrpPeerMsgRxRtTime_Type.__name__ = "Unsigned32"
_TmnxMsdpNgPeerGrpPeerMsgRxRtTime_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerMsgRxRtTime = _TmnxMsdpNgPeerGrpPeerMsgRxRtTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 6),
    _TmnxMsdpNgPeerGrpPeerMsgRxRtTime_Type()
)
tmnxMsdpNgPeerGrpPeerMsgRxRtTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerMsgRxRtTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerMsgRxRtTime.setUnits("seconds")


class _TmnxMsdpNgPeerGrpPeerMsgRcvRtThd_Type(Gauge32):
    """Custom type tmnxMsdpNgPeerGrpPeerMsgRcvRtThd based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000000),
    )


_TmnxMsdpNgPeerGrpPeerMsgRcvRtThd_Type.__name__ = "Gauge32"
_TmnxMsdpNgPeerGrpPeerMsgRcvRtThd_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerMsgRcvRtThd = _TmnxMsdpNgPeerGrpPeerMsgRcvRtThd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 7),
    _TmnxMsdpNgPeerGrpPeerMsgRcvRtThd_Type()
)
tmnxMsdpNgPeerGrpPeerMsgRcvRtThd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerMsgRcvRtThd.setStatus("current")


class _TmnxMsdpNgPeerGrpPeerAuthKey_Type(OctetString):
    """Custom type tmnxMsdpNgPeerGrpPeerAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TmnxMsdpNgPeerGrpPeerAuthKey_Type.__name__ = "OctetString"
_TmnxMsdpNgPeerGrpPeerAuthKey_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerAuthKey = _TmnxMsdpNgPeerGrpPeerAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 8),
    _TmnxMsdpNgPeerGrpPeerAuthKey_Type()
)
tmnxMsdpNgPeerGrpPeerAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerAuthKey.setStatus("current")


class _TmnxMsdpNgPeerGrpPeerAKeyEncrypt_Type(TruthValue):
    """Custom type tmnxMsdpNgPeerGrpPeerAKeyEncrypt based on TruthValue"""
    defaultValue = 1


_TmnxMsdpNgPeerGrpPeerAKeyEncrypt_Type.__name__ = "TruthValue"
_TmnxMsdpNgPeerGrpPeerAKeyEncrypt_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerAKeyEncrypt = _TmnxMsdpNgPeerGrpPeerAKeyEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 9),
    _TmnxMsdpNgPeerGrpPeerAKeyEncrypt_Type()
)
tmnxMsdpNgPeerGrpPeerAKeyEncrypt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerAKeyEncrypt.setStatus("current")


class _TmnxMsdpNgPeerGrpPeerDefaultPeer_Type(TruthValue):
    """Custom type tmnxMsdpNgPeerGrpPeerDefaultPeer based on TruthValue"""
    defaultValue = 2


_TmnxMsdpNgPeerGrpPeerDefaultPeer_Type.__name__ = "TruthValue"
_TmnxMsdpNgPeerGrpPeerDefaultPeer_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerDefaultPeer = _TmnxMsdpNgPeerGrpPeerDefaultPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 10),
    _TmnxMsdpNgPeerGrpPeerDefaultPeer_Type()
)
tmnxMsdpNgPeerGrpPeerDefaultPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerDefaultPeer.setStatus("current")


class _TmnxMsdpNgPeerGrpPeerAdminState_Type(TmnxAdminState):
    """Custom type tmnxMsdpNgPeerGrpPeerAdminState based on TmnxAdminState"""
    defaultValue = 2


_TmnxMsdpNgPeerGrpPeerAdminState_Type.__name__ = "TmnxAdminState"
_TmnxMsdpNgPeerGrpPeerAdminState_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerAdminState = _TmnxMsdpNgPeerGrpPeerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 11),
    _TmnxMsdpNgPeerGrpPeerAdminState_Type()
)
tmnxMsdpNgPeerGrpPeerAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerAdminState.setStatus("current")


class _TmnxMsdpNgPeerGrpPeerExportPlcy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerGrpPeerExportPlcy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerGrpPeerExportPlcy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerGrpPeerExportPlcy1_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerExportPlcy1 = _TmnxMsdpNgPeerGrpPeerExportPlcy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 12),
    _TmnxMsdpNgPeerGrpPeerExportPlcy1_Type()
)
tmnxMsdpNgPeerGrpPeerExportPlcy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerExportPlcy1.setStatus("current")


class _TmnxMsdpNgPeerGrpPeerExportPlcy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerGrpPeerExportPlcy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerGrpPeerExportPlcy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerGrpPeerExportPlcy2_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerExportPlcy2 = _TmnxMsdpNgPeerGrpPeerExportPlcy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 13),
    _TmnxMsdpNgPeerGrpPeerExportPlcy2_Type()
)
tmnxMsdpNgPeerGrpPeerExportPlcy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerExportPlcy2.setStatus("current")


class _TmnxMsdpNgPeerGrpPeerExportPlcy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerGrpPeerExportPlcy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerGrpPeerExportPlcy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerGrpPeerExportPlcy3_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerExportPlcy3 = _TmnxMsdpNgPeerGrpPeerExportPlcy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 14),
    _TmnxMsdpNgPeerGrpPeerExportPlcy3_Type()
)
tmnxMsdpNgPeerGrpPeerExportPlcy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerExportPlcy3.setStatus("current")


class _TmnxMsdpNgPeerGrpPeerExportPlcy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerGrpPeerExportPlcy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerGrpPeerExportPlcy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerGrpPeerExportPlcy4_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerExportPlcy4 = _TmnxMsdpNgPeerGrpPeerExportPlcy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 15),
    _TmnxMsdpNgPeerGrpPeerExportPlcy4_Type()
)
tmnxMsdpNgPeerGrpPeerExportPlcy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerExportPlcy4.setStatus("current")


class _TmnxMsdpNgPeerGrpPeerExportPlcy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerGrpPeerExportPlcy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerGrpPeerExportPlcy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerGrpPeerExportPlcy5_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerExportPlcy5 = _TmnxMsdpNgPeerGrpPeerExportPlcy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 16),
    _TmnxMsdpNgPeerGrpPeerExportPlcy5_Type()
)
tmnxMsdpNgPeerGrpPeerExportPlcy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerExportPlcy5.setStatus("current")


class _TmnxMsdpNgPeerGrpPeerImportPlcy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerGrpPeerImportPlcy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerGrpPeerImportPlcy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerGrpPeerImportPlcy1_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerImportPlcy1 = _TmnxMsdpNgPeerGrpPeerImportPlcy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 17),
    _TmnxMsdpNgPeerGrpPeerImportPlcy1_Type()
)
tmnxMsdpNgPeerGrpPeerImportPlcy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerImportPlcy1.setStatus("current")


class _TmnxMsdpNgPeerGrpPeerImportPlcy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerGrpPeerImportPlcy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerGrpPeerImportPlcy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerGrpPeerImportPlcy2_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerImportPlcy2 = _TmnxMsdpNgPeerGrpPeerImportPlcy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 18),
    _TmnxMsdpNgPeerGrpPeerImportPlcy2_Type()
)
tmnxMsdpNgPeerGrpPeerImportPlcy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerImportPlcy2.setStatus("current")


class _TmnxMsdpNgPeerGrpPeerImportPlcy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerGrpPeerImportPlcy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerGrpPeerImportPlcy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerGrpPeerImportPlcy3_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerImportPlcy3 = _TmnxMsdpNgPeerGrpPeerImportPlcy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 19),
    _TmnxMsdpNgPeerGrpPeerImportPlcy3_Type()
)
tmnxMsdpNgPeerGrpPeerImportPlcy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerImportPlcy3.setStatus("current")


class _TmnxMsdpNgPeerGrpPeerImportPlcy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerGrpPeerImportPlcy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerGrpPeerImportPlcy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerGrpPeerImportPlcy4_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerImportPlcy4 = _TmnxMsdpNgPeerGrpPeerImportPlcy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 20),
    _TmnxMsdpNgPeerGrpPeerImportPlcy4_Type()
)
tmnxMsdpNgPeerGrpPeerImportPlcy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerImportPlcy4.setStatus("current")


class _TmnxMsdpNgPeerGrpPeerImportPlcy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxMsdpNgPeerGrpPeerImportPlcy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxMsdpNgPeerGrpPeerImportPlcy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxMsdpNgPeerGrpPeerImportPlcy5_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerImportPlcy5 = _TmnxMsdpNgPeerGrpPeerImportPlcy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 21),
    _TmnxMsdpNgPeerGrpPeerImportPlcy5_Type()
)
tmnxMsdpNgPeerGrpPeerImportPlcy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerImportPlcy5.setStatus("current")


class _TmnxMsdpNgPeerGrpPeerLocAddrType_Type(InetAddressType):
    """Custom type tmnxMsdpNgPeerGrpPeerLocAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxMsdpNgPeerGrpPeerLocAddrType_Type.__name__ = "InetAddressType"
_TmnxMsdpNgPeerGrpPeerLocAddrType_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerLocAddrType = _TmnxMsdpNgPeerGrpPeerLocAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 22),
    _TmnxMsdpNgPeerGrpPeerLocAddrType_Type()
)
tmnxMsdpNgPeerGrpPeerLocAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerLocAddrType.setStatus("current")


class _TmnxMsdpNgPeerGrpPeerLocalAddr_Type(InetAddress):
    """Custom type tmnxMsdpNgPeerGrpPeerLocalAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpNgPeerGrpPeerLocalAddr_Type.__name__ = "InetAddress"
_TmnxMsdpNgPeerGrpPeerLocalAddr_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerLocalAddr = _TmnxMsdpNgPeerGrpPeerLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 23),
    _TmnxMsdpNgPeerGrpPeerLocalAddr_Type()
)
tmnxMsdpNgPeerGrpPeerLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerLocalAddr.setStatus("current")


class _TmnxMsdpNgPeerGrpPeerState_Type(Integer32):
    """Custom type tmnxMsdpNgPeerGrpPeerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("listen", 0),
          ("established", 1),
          ("inactive", 2),
          ("disabled", 3),
          ("connecting", 4))
    )


_TmnxMsdpNgPeerGrpPeerState_Type.__name__ = "Integer32"
_TmnxMsdpNgPeerGrpPeerState_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerState = _TmnxMsdpNgPeerGrpPeerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 24),
    _TmnxMsdpNgPeerGrpPeerState_Type()
)
tmnxMsdpNgPeerGrpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerState.setStatus("current")
_TmnxMsdpNgPeerGrpPeerLstUpOrDwn_Type = TimeStamp
_TmnxMsdpNgPeerGrpPeerLstUpOrDwn_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerLstUpOrDwn = _TmnxMsdpNgPeerGrpPeerLstUpOrDwn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 25),
    _TmnxMsdpNgPeerGrpPeerLstUpOrDwn_Type()
)
tmnxMsdpNgPeerGrpPeerLstUpOrDwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerLstUpOrDwn.setStatus("current")
_TmnxMsdpNgPeerGrpPeerConRetry_Type = Counter32
_TmnxMsdpNgPeerGrpPeerConRetry_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerConRetry = _TmnxMsdpNgPeerGrpPeerConRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 26),
    _TmnxMsdpNgPeerGrpPeerConRetry_Type()
)
tmnxMsdpNgPeerGrpPeerConRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerConRetry.setStatus("current")
_TmnxMsdpNgPeerGrpPeerStateTimer_Type = Unsigned32
_TmnxMsdpNgPeerGrpPeerStateTimer_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerStateTimer = _TmnxMsdpNgPeerGrpPeerStateTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 27),
    _TmnxMsdpNgPeerGrpPeerStateTimer_Type()
)
tmnxMsdpNgPeerGrpPeerStateTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerStateTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerStateTimer.setUnits("seconds")
_TmnxMsdpNgPeerGrpPeerTimeout_Type = Unsigned32
_TmnxMsdpNgPeerGrpPeerTimeout_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerTimeout = _TmnxMsdpNgPeerGrpPeerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 28),
    _TmnxMsdpNgPeerGrpPeerTimeout_Type()
)
tmnxMsdpNgPeerGrpPeerTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerTimeout.setUnits("seconds")
_TmnxMsdpNgPeerGrpPeerSAAccepted_Type = Gauge32
_TmnxMsdpNgPeerGrpPeerSAAccepted_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerSAAccepted = _TmnxMsdpNgPeerGrpPeerSAAccepted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 29),
    _TmnxMsdpNgPeerGrpPeerSAAccepted_Type()
)
tmnxMsdpNgPeerGrpPeerSAAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerSAAccepted.setStatus("current")
_TmnxMsdpNgPeerGrpPeerSARx_Type = Gauge32
_TmnxMsdpNgPeerGrpPeerSARx_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerSARx = _TmnxMsdpNgPeerGrpPeerSARx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 30),
    _TmnxMsdpNgPeerGrpPeerSARx_Type()
)
tmnxMsdpNgPeerGrpPeerSARx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerSARx.setStatus("current")
_TmnxMsdpNgPeerGrpPeerLastASLimit_Type = TimeStamp
_TmnxMsdpNgPeerGrpPeerLastASLimit_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerLastASLimit = _TmnxMsdpNgPeerGrpPeerLastASLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 31),
    _TmnxMsdpNgPeerGrpPeerLastASLimit_Type()
)
tmnxMsdpNgPeerGrpPeerLastASLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerLastASLimit.setStatus("current")
_TmnxMsdpNgPeerGrpPeerOpAddrType_Type = InetAddressType
_TmnxMsdpNgPeerGrpPeerOpAddrType_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerOpAddrType = _TmnxMsdpNgPeerGrpPeerOpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 32),
    _TmnxMsdpNgPeerGrpPeerOpAddrType_Type()
)
tmnxMsdpNgPeerGrpPeerOpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerOpAddrType.setStatus("current")


class _TmnxMsdpNgPeerGrpPeerOpAddr_Type(InetAddress):
    """Custom type tmnxMsdpNgPeerGrpPeerOpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpNgPeerGrpPeerOpAddr_Type.__name__ = "InetAddress"
_TmnxMsdpNgPeerGrpPeerOpAddr_Object = MibTableColumn
tmnxMsdpNgPeerGrpPeerOpAddr = _TmnxMsdpNgPeerGrpPeerOpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 5, 1, 33),
    _TmnxMsdpNgPeerGrpPeerOpAddr_Type()
)
tmnxMsdpNgPeerGrpPeerOpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGrpPeerOpAddr.setStatus("current")
_TmnxMsdpNgSourceTable_Object = MibTable
tmnxMsdpNgSourceTable = _TmnxMsdpNgSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 6)
)
if mibBuilder.loadTexts:
    tmnxMsdpNgSourceTable.setStatus("current")
_TmnxMsdpNgSourceEntry_Object = MibTableRow
tmnxMsdpNgSourceEntry = _TmnxMsdpNgSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 6, 1)
)
tmnxMsdpNgSourceEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSourcePrefixType"),
    (0, "TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSourcePrefix"),
    (0, "TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSourceMask"),
)
if mibBuilder.loadTexts:
    tmnxMsdpNgSourceEntry.setStatus("current")
_TmnxMsdpNgSourcePrefixType_Type = InetAddressType
_TmnxMsdpNgSourcePrefixType_Object = MibTableColumn
tmnxMsdpNgSourcePrefixType = _TmnxMsdpNgSourcePrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 6, 1, 1),
    _TmnxMsdpNgSourcePrefixType_Type()
)
tmnxMsdpNgSourcePrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpNgSourcePrefixType.setStatus("current")


class _TmnxMsdpNgSourcePrefix_Type(InetAddress):
    """Custom type tmnxMsdpNgSourcePrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpNgSourcePrefix_Type.__name__ = "InetAddress"
_TmnxMsdpNgSourcePrefix_Object = MibTableColumn
tmnxMsdpNgSourcePrefix = _TmnxMsdpNgSourcePrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 6, 1, 2),
    _TmnxMsdpNgSourcePrefix_Type()
)
tmnxMsdpNgSourcePrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpNgSourcePrefix.setStatus("current")


class _TmnxMsdpNgSourceMask_Type(InetAddressPrefixLength):
    """Custom type tmnxMsdpNgSourceMask based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxMsdpNgSourceMask_Type.__name__ = "InetAddressPrefixLength"
_TmnxMsdpNgSourceMask_Object = MibTableColumn
tmnxMsdpNgSourceMask = _TmnxMsdpNgSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 6, 1, 3),
    _TmnxMsdpNgSourceMask_Type()
)
tmnxMsdpNgSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpNgSourceMask.setStatus("current")
_TmnxMsdpNgSourceRowStatus_Type = RowStatus
_TmnxMsdpNgSourceRowStatus_Object = MibTableColumn
tmnxMsdpNgSourceRowStatus = _TmnxMsdpNgSourceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 6, 1, 4),
    _TmnxMsdpNgSourceRowStatus_Type()
)
tmnxMsdpNgSourceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgSourceRowStatus.setStatus("current")


class _TmnxMsdpNgSourceMaxActiveSources_Type(Integer32):
    """Custom type tmnxMsdpNgSourceMaxActiveSources based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1000000),
    )


_TmnxMsdpNgSourceMaxActiveSources_Type.__name__ = "Integer32"
_TmnxMsdpNgSourceMaxActiveSources_Object = MibTableColumn
tmnxMsdpNgSourceMaxActiveSources = _TmnxMsdpNgSourceMaxActiveSources_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 6, 1, 5),
    _TmnxMsdpNgSourceMaxActiveSources_Type()
)
tmnxMsdpNgSourceMaxActiveSources.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMsdpNgSourceMaxActiveSources.setStatus("current")


class _TmnxMsdpNgSourceDiscMethod_Type(Integer32):
    """Custom type tmnxMsdpNgSourceDiscMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 0),
          ("configured", 1))
    )


_TmnxMsdpNgSourceDiscMethod_Type.__name__ = "Integer32"
_TmnxMsdpNgSourceDiscMethod_Object = MibTableColumn
tmnxMsdpNgSourceDiscMethod = _TmnxMsdpNgSourceDiscMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 6, 1, 6),
    _TmnxMsdpNgSourceDiscMethod_Type()
)
tmnxMsdpNgSourceDiscMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgSourceDiscMethod.setStatus("current")
_TmnxMsdpNgSourceSrcActMsgsExMax_Type = Counter32
_TmnxMsdpNgSourceSrcActMsgsExMax_Object = MibTableColumn
tmnxMsdpNgSourceSrcActMsgsExMax = _TmnxMsdpNgSourceSrcActMsgsExMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 6, 1, 7),
    _TmnxMsdpNgSourceSrcActMsgsExMax_Type()
)
tmnxMsdpNgSourceSrcActMsgsExMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgSourceSrcActMsgsExMax.setStatus("current")
_TmnxMsdpNgSourceLastExEventTime_Type = TimeStamp
_TmnxMsdpNgSourceLastExEventTime_Object = MibTableColumn
tmnxMsdpNgSourceLastExEventTime = _TmnxMsdpNgSourceLastExEventTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 6, 1, 8),
    _TmnxMsdpNgSourceLastExEventTime_Type()
)
tmnxMsdpNgSourceLastExEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgSourceLastExEventTime.setStatus("current")
_TmnxMsdpNgSATable_Object = MibTable
tmnxMsdpNgSATable = _TmnxMsdpNgSATable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 7)
)
if mibBuilder.loadTexts:
    tmnxMsdpNgSATable.setStatus("current")
_TmnxMsdpNgSAEntry_Object = MibTableRow
tmnxMsdpNgSAEntry = _TmnxMsdpNgSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 7, 1)
)
tmnxMsdpNgSAEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSAGroupAddrType"),
    (0, "TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSAGroupAddr"),
    (0, "TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSASourceAddrType"),
    (0, "TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSASourceAddr"),
    (0, "TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSAOriginRPType"),
    (0, "TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSAOriginRP"),
)
if mibBuilder.loadTexts:
    tmnxMsdpNgSAEntry.setStatus("current")
_TmnxMsdpNgSAGroupAddrType_Type = InetAddressType
_TmnxMsdpNgSAGroupAddrType_Object = MibTableColumn
tmnxMsdpNgSAGroupAddrType = _TmnxMsdpNgSAGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 7, 1, 1),
    _TmnxMsdpNgSAGroupAddrType_Type()
)
tmnxMsdpNgSAGroupAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpNgSAGroupAddrType.setStatus("current")


class _TmnxMsdpNgSAGroupAddr_Type(InetAddress):
    """Custom type tmnxMsdpNgSAGroupAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpNgSAGroupAddr_Type.__name__ = "InetAddress"
_TmnxMsdpNgSAGroupAddr_Object = MibTableColumn
tmnxMsdpNgSAGroupAddr = _TmnxMsdpNgSAGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 7, 1, 2),
    _TmnxMsdpNgSAGroupAddr_Type()
)
tmnxMsdpNgSAGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpNgSAGroupAddr.setStatus("current")
_TmnxMsdpNgSASourceAddrType_Type = InetAddressType
_TmnxMsdpNgSASourceAddrType_Object = MibTableColumn
tmnxMsdpNgSASourceAddrType = _TmnxMsdpNgSASourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 7, 1, 3),
    _TmnxMsdpNgSASourceAddrType_Type()
)
tmnxMsdpNgSASourceAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpNgSASourceAddrType.setStatus("current")


class _TmnxMsdpNgSASourceAddr_Type(InetAddress):
    """Custom type tmnxMsdpNgSASourceAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpNgSASourceAddr_Type.__name__ = "InetAddress"
_TmnxMsdpNgSASourceAddr_Object = MibTableColumn
tmnxMsdpNgSASourceAddr = _TmnxMsdpNgSASourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 7, 1, 4),
    _TmnxMsdpNgSASourceAddr_Type()
)
tmnxMsdpNgSASourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpNgSASourceAddr.setStatus("current")
_TmnxMsdpNgSAOriginRPType_Type = InetAddressType
_TmnxMsdpNgSAOriginRPType_Object = MibTableColumn
tmnxMsdpNgSAOriginRPType = _TmnxMsdpNgSAOriginRPType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 7, 1, 5),
    _TmnxMsdpNgSAOriginRPType_Type()
)
tmnxMsdpNgSAOriginRPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpNgSAOriginRPType.setStatus("current")


class _TmnxMsdpNgSAOriginRP_Type(InetAddress):
    """Custom type tmnxMsdpNgSAOriginRP based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpNgSAOriginRP_Type.__name__ = "InetAddress"
_TmnxMsdpNgSAOriginRP_Object = MibTableColumn
tmnxMsdpNgSAOriginRP = _TmnxMsdpNgSAOriginRP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 7, 1, 6),
    _TmnxMsdpNgSAOriginRP_Type()
)
tmnxMsdpNgSAOriginRP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpNgSAOriginRP.setStatus("current")
_TmnxMsdpNgSAPrLearnFrType_Type = InetAddressType
_TmnxMsdpNgSAPrLearnFrType_Object = MibTableColumn
tmnxMsdpNgSAPrLearnFrType = _TmnxMsdpNgSAPrLearnFrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 7, 1, 7),
    _TmnxMsdpNgSAPrLearnFrType_Type()
)
tmnxMsdpNgSAPrLearnFrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgSAPrLearnFrType.setStatus("current")


class _TmnxMsdpNgSAPeerLearntFrom_Type(InetAddress):
    """Custom type tmnxMsdpNgSAPeerLearntFrom based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpNgSAPeerLearntFrom_Type.__name__ = "InetAddress"
_TmnxMsdpNgSAPeerLearntFrom_Object = MibTableColumn
tmnxMsdpNgSAPeerLearntFrom = _TmnxMsdpNgSAPeerLearntFrom_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 7, 1, 8),
    _TmnxMsdpNgSAPeerLearntFrom_Type()
)
tmnxMsdpNgSAPeerLearntFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgSAPeerLearntFrom.setStatus("current")
_TmnxMsdpNgSARPFPeerType_Type = InetAddressType
_TmnxMsdpNgSARPFPeerType_Object = MibTableColumn
tmnxMsdpNgSARPFPeerType = _TmnxMsdpNgSARPFPeerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 7, 1, 9),
    _TmnxMsdpNgSARPFPeerType_Type()
)
tmnxMsdpNgSARPFPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgSARPFPeerType.setStatus("current")


class _TmnxMsdpNgSARPFPeer_Type(InetAddress):
    """Custom type tmnxMsdpNgSARPFPeer based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpNgSARPFPeer_Type.__name__ = "InetAddress"
_TmnxMsdpNgSARPFPeer_Object = MibTableColumn
tmnxMsdpNgSARPFPeer = _TmnxMsdpNgSARPFPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 7, 1, 10),
    _TmnxMsdpNgSARPFPeer_Type()
)
tmnxMsdpNgSARPFPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgSARPFPeer.setStatus("current")
_TmnxMsdpNgSAUpTime_Type = TimeInterval
_TmnxMsdpNgSAUpTime_Object = MibTableColumn
tmnxMsdpNgSAUpTime = _TmnxMsdpNgSAUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 7, 1, 11),
    _TmnxMsdpNgSAUpTime_Type()
)
tmnxMsdpNgSAUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgSAUpTime.setStatus("current")
_TmnxMsdpNgSAExpiryTime_Type = TimeInterval
_TmnxMsdpNgSAExpiryTime_Object = MibTableColumn
tmnxMsdpNgSAExpiryTime = _TmnxMsdpNgSAExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 7, 1, 12),
    _TmnxMsdpNgSAExpiryTime_Type()
)
tmnxMsdpNgSAExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgSAExpiryTime.setStatus("current")
_TmnxMsdpNgPeerStatsTable_Object = MibTable
tmnxMsdpNgPeerStatsTable = _TmnxMsdpNgPeerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 8)
)
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerStatsTable.setStatus("current")
_TmnxMsdpNgPeerStatsEntry_Object = MibTableRow
tmnxMsdpNgPeerStatsEntry = _TmnxMsdpNgPeerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 8, 1)
)
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerStatsEntry.setStatus("current")
_TmnxMsdpNgPeerStatsActSrcLimExcd_Type = Counter32
_TmnxMsdpNgPeerStatsActSrcLimExcd_Object = MibTableColumn
tmnxMsdpNgPeerStatsActSrcLimExcd = _TmnxMsdpNgPeerStatsActSrcLimExcd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 8, 1, 1),
    _TmnxMsdpNgPeerStatsActSrcLimExcd_Type()
)
tmnxMsdpNgPeerStatsActSrcLimExcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerStatsActSrcLimExcd.setStatus("current")
_TmnxMsdpNgPeerStatsLastStChange_Type = TimeInterval
_TmnxMsdpNgPeerStatsLastStChange_Object = MibTableColumn
tmnxMsdpNgPeerStatsLastStChange = _TmnxMsdpNgPeerStatsLastStChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 8, 1, 2),
    _TmnxMsdpNgPeerStatsLastStChange_Type()
)
tmnxMsdpNgPeerStatsLastStChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerStatsLastStChange.setStatus("current")
_TmnxMsdpNgPeerStatsLastMsgPeer_Type = TimeInterval
_TmnxMsdpNgPeerStatsLastMsgPeer_Object = MibTableColumn
tmnxMsdpNgPeerStatsLastMsgPeer = _TmnxMsdpNgPeerStatsLastMsgPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 8, 1, 3),
    _TmnxMsdpNgPeerStatsLastMsgPeer_Type()
)
tmnxMsdpNgPeerStatsLastMsgPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerStatsLastMsgPeer.setStatus("current")
_TmnxMsdpNgPeerStatsRPFFailures_Type = Counter32
_TmnxMsdpNgPeerStatsRPFFailures_Object = MibTableColumn
tmnxMsdpNgPeerStatsRPFFailures = _TmnxMsdpNgPeerStatsRPFFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 8, 1, 4),
    _TmnxMsdpNgPeerStatsRPFFailures_Type()
)
tmnxMsdpNgPeerStatsRPFFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerStatsRPFFailures.setStatus("current")
_TmnxMsdpNgPeerStatsRemoteCloses_Type = Counter32
_TmnxMsdpNgPeerStatsRemoteCloses_Object = MibTableColumn
tmnxMsdpNgPeerStatsRemoteCloses = _TmnxMsdpNgPeerStatsRemoteCloses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 8, 1, 5),
    _TmnxMsdpNgPeerStatsRemoteCloses_Type()
)
tmnxMsdpNgPeerStatsRemoteCloses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerStatsRemoteCloses.setStatus("current")
_TmnxMsdpNgPeerStatsPeerTimeouts_Type = Counter32
_TmnxMsdpNgPeerStatsPeerTimeouts_Object = MibTableColumn
tmnxMsdpNgPeerStatsPeerTimeouts = _TmnxMsdpNgPeerStatsPeerTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 8, 1, 6),
    _TmnxMsdpNgPeerStatsPeerTimeouts_Type()
)
tmnxMsdpNgPeerStatsPeerTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerStatsPeerTimeouts.setStatus("current")
_TmnxMsdpNgPeerStatsSAMsgsSent_Type = Counter32
_TmnxMsdpNgPeerStatsSAMsgsSent_Object = MibTableColumn
tmnxMsdpNgPeerStatsSAMsgsSent = _TmnxMsdpNgPeerStatsSAMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 8, 1, 7),
    _TmnxMsdpNgPeerStatsSAMsgsSent_Type()
)
tmnxMsdpNgPeerStatsSAMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerStatsSAMsgsSent.setStatus("current")
_TmnxMsdpNgPeerStatsSAMsgsRx_Type = Counter32
_TmnxMsdpNgPeerStatsSAMsgsRx_Object = MibTableColumn
tmnxMsdpNgPeerStatsSAMsgsRx = _TmnxMsdpNgPeerStatsSAMsgsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 8, 1, 8),
    _TmnxMsdpNgPeerStatsSAMsgsRx_Type()
)
tmnxMsdpNgPeerStatsSAMsgsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerStatsSAMsgsRx.setStatus("current")
_TmnxMsdpNgPeerStatsSAReqMsgsSent_Type = Counter32
_TmnxMsdpNgPeerStatsSAReqMsgsSent_Object = MibTableColumn
tmnxMsdpNgPeerStatsSAReqMsgsSent = _TmnxMsdpNgPeerStatsSAReqMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 8, 1, 9),
    _TmnxMsdpNgPeerStatsSAReqMsgsSent_Type()
)
tmnxMsdpNgPeerStatsSAReqMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerStatsSAReqMsgsSent.setStatus("current")
_TmnxMsdpNgPeerStatsSAReqMsgsRx_Type = Counter32
_TmnxMsdpNgPeerStatsSAReqMsgsRx_Object = MibTableColumn
tmnxMsdpNgPeerStatsSAReqMsgsRx = _TmnxMsdpNgPeerStatsSAReqMsgsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 8, 1, 10),
    _TmnxMsdpNgPeerStatsSAReqMsgsRx_Type()
)
tmnxMsdpNgPeerStatsSAReqMsgsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerStatsSAReqMsgsRx.setStatus("current")
_TmnxMsdpNgPeerStatsSAResMsgsSent_Type = Counter32
_TmnxMsdpNgPeerStatsSAResMsgsSent_Object = MibTableColumn
tmnxMsdpNgPeerStatsSAResMsgsSent = _TmnxMsdpNgPeerStatsSAResMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 8, 1, 11),
    _TmnxMsdpNgPeerStatsSAResMsgsSent_Type()
)
tmnxMsdpNgPeerStatsSAResMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerStatsSAResMsgsSent.setStatus("current")
_TmnxMsdpNgPeerStatsSAResMsgsRx_Type = Counter32
_TmnxMsdpNgPeerStatsSAResMsgsRx_Object = MibTableColumn
tmnxMsdpNgPeerStatsSAResMsgsRx = _TmnxMsdpNgPeerStatsSAResMsgsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 8, 1, 12),
    _TmnxMsdpNgPeerStatsSAResMsgsRx_Type()
)
tmnxMsdpNgPeerStatsSAResMsgsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerStatsSAResMsgsRx.setStatus("current")
_TmnxMsdpNgPeerStatsKAMsgsSent_Type = Counter32
_TmnxMsdpNgPeerStatsKAMsgsSent_Object = MibTableColumn
tmnxMsdpNgPeerStatsKAMsgsSent = _TmnxMsdpNgPeerStatsKAMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 8, 1, 13),
    _TmnxMsdpNgPeerStatsKAMsgsSent_Type()
)
tmnxMsdpNgPeerStatsKAMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerStatsKAMsgsSent.setStatus("current")
_TmnxMsdpNgPeerStatsKAMsgsRx_Type = Counter32
_TmnxMsdpNgPeerStatsKAMsgsRx_Object = MibTableColumn
tmnxMsdpNgPeerStatsKAMsgsRx = _TmnxMsdpNgPeerStatsKAMsgsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 8, 1, 14),
    _TmnxMsdpNgPeerStatsKAMsgsRx_Type()
)
tmnxMsdpNgPeerStatsKAMsgsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerStatsKAMsgsRx.setStatus("current")
_TmnxMsdpNgPeerStatsUnknMsgsRx_Type = Counter32
_TmnxMsdpNgPeerStatsUnknMsgsRx_Object = MibTableColumn
tmnxMsdpNgPeerStatsUnknMsgsRx = _TmnxMsdpNgPeerStatsUnknMsgsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 8, 1, 15),
    _TmnxMsdpNgPeerStatsUnknMsgsRx_Type()
)
tmnxMsdpNgPeerStatsUnknMsgsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerStatsUnknMsgsRx.setStatus("current")
_TmnxMsdpNgPeerStatsErrMsgsRx_Type = Counter32
_TmnxMsdpNgPeerStatsErrMsgsRx_Object = MibTableColumn
tmnxMsdpNgPeerStatsErrMsgsRx = _TmnxMsdpNgPeerStatsErrMsgsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 8, 1, 16),
    _TmnxMsdpNgPeerStatsErrMsgsRx_Type()
)
tmnxMsdpNgPeerStatsErrMsgsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerStatsErrMsgsRx.setStatus("current")
_TmnxMsdpNgPeerStatsSALearnt_Type = Gauge32
_TmnxMsdpNgPeerStatsSALearnt_Object = MibTableColumn
tmnxMsdpNgPeerStatsSALearnt = _TmnxMsdpNgPeerStatsSALearnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 8, 1, 17),
    _TmnxMsdpNgPeerStatsSALearnt_Type()
)
tmnxMsdpNgPeerStatsSALearnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerStatsSALearnt.setStatus("current")
_TmnxMsdpNgPeerStatsSARejExpPlcy_Type = Counter32
_TmnxMsdpNgPeerStatsSARejExpPlcy_Object = MibTableColumn
tmnxMsdpNgPeerStatsSARejExpPlcy = _TmnxMsdpNgPeerStatsSARejExpPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 8, 1, 18),
    _TmnxMsdpNgPeerStatsSARejExpPlcy_Type()
)
tmnxMsdpNgPeerStatsSARejExpPlcy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerStatsSARejExpPlcy.setStatus("current")
_TmnxMsdpNgPeerStatsSARejImpPlcy_Type = Counter32
_TmnxMsdpNgPeerStatsSARejImpPlcy_Object = MibTableColumn
tmnxMsdpNgPeerStatsSARejImpPlcy = _TmnxMsdpNgPeerStatsSARejImpPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 8, 1, 19),
    _TmnxMsdpNgPeerStatsSARejImpPlcy_Type()
)
tmnxMsdpNgPeerStatsSARejImpPlcy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerStatsSARejImpPlcy.setStatus("current")
_TmnxMsdpNgPeerStatsResvMsgsRx_Type = Counter32
_TmnxMsdpNgPeerStatsResvMsgsRx_Object = MibTableColumn
tmnxMsdpNgPeerStatsResvMsgsRx = _TmnxMsdpNgPeerStatsResvMsgsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 8, 1, 20),
    _TmnxMsdpNgPeerStatsResvMsgsRx_Type()
)
tmnxMsdpNgPeerStatsResvMsgsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerStatsResvMsgsRx.setStatus("current")
_TmnxMsdpNgSrcActRejTable_Object = MibTable
tmnxMsdpNgSrcActRejTable = _TmnxMsdpNgSrcActRejTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 9)
)
if mibBuilder.loadTexts:
    tmnxMsdpNgSrcActRejTable.setStatus("current")
_TmnxMsdpNgSrcActRejEntry_Object = MibTableRow
tmnxMsdpNgSrcActRejEntry = _TmnxMsdpNgSrcActRejEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 9, 1)
)
tmnxMsdpNgSrcActRejEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSARejPeerGroupName"),
    (0, "TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSARejGroupAddrType"),
    (0, "TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSARejGroupAddr"),
    (0, "TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSARejSourceAddrType"),
    (0, "TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSARejSourceAddr"),
    (0, "TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSARejOriginRPType"),
    (0, "TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSARejOriginRP"),
    (0, "TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSARejPeerAddrType"),
    (0, "TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSARejPeerAddr"),
)
if mibBuilder.loadTexts:
    tmnxMsdpNgSrcActRejEntry.setStatus("current")
_TmnxMsdpNgSARejPeerGroupName_Type = TNamedItemOrEmpty
_TmnxMsdpNgSARejPeerGroupName_Object = MibTableColumn
tmnxMsdpNgSARejPeerGroupName = _TmnxMsdpNgSARejPeerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 9, 1, 1),
    _TmnxMsdpNgSARejPeerGroupName_Type()
)
tmnxMsdpNgSARejPeerGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpNgSARejPeerGroupName.setStatus("current")
_TmnxMsdpNgSARejGroupAddrType_Type = InetAddressType
_TmnxMsdpNgSARejGroupAddrType_Object = MibTableColumn
tmnxMsdpNgSARejGroupAddrType = _TmnxMsdpNgSARejGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 9, 1, 2),
    _TmnxMsdpNgSARejGroupAddrType_Type()
)
tmnxMsdpNgSARejGroupAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpNgSARejGroupAddrType.setStatus("current")


class _TmnxMsdpNgSARejGroupAddr_Type(InetAddress):
    """Custom type tmnxMsdpNgSARejGroupAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpNgSARejGroupAddr_Type.__name__ = "InetAddress"
_TmnxMsdpNgSARejGroupAddr_Object = MibTableColumn
tmnxMsdpNgSARejGroupAddr = _TmnxMsdpNgSARejGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 9, 1, 3),
    _TmnxMsdpNgSARejGroupAddr_Type()
)
tmnxMsdpNgSARejGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpNgSARejGroupAddr.setStatus("current")
_TmnxMsdpNgSARejSourceAddrType_Type = InetAddressType
_TmnxMsdpNgSARejSourceAddrType_Object = MibTableColumn
tmnxMsdpNgSARejSourceAddrType = _TmnxMsdpNgSARejSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 9, 1, 4),
    _TmnxMsdpNgSARejSourceAddrType_Type()
)
tmnxMsdpNgSARejSourceAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpNgSARejSourceAddrType.setStatus("current")


class _TmnxMsdpNgSARejSourceAddr_Type(InetAddress):
    """Custom type tmnxMsdpNgSARejSourceAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpNgSARejSourceAddr_Type.__name__ = "InetAddress"
_TmnxMsdpNgSARejSourceAddr_Object = MibTableColumn
tmnxMsdpNgSARejSourceAddr = _TmnxMsdpNgSARejSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 9, 1, 5),
    _TmnxMsdpNgSARejSourceAddr_Type()
)
tmnxMsdpNgSARejSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpNgSARejSourceAddr.setStatus("current")
_TmnxMsdpNgSARejOriginRPType_Type = InetAddressType
_TmnxMsdpNgSARejOriginRPType_Object = MibTableColumn
tmnxMsdpNgSARejOriginRPType = _TmnxMsdpNgSARejOriginRPType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 9, 1, 6),
    _TmnxMsdpNgSARejOriginRPType_Type()
)
tmnxMsdpNgSARejOriginRPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpNgSARejOriginRPType.setStatus("current")


class _TmnxMsdpNgSARejOriginRP_Type(InetAddress):
    """Custom type tmnxMsdpNgSARejOriginRP based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpNgSARejOriginRP_Type.__name__ = "InetAddress"
_TmnxMsdpNgSARejOriginRP_Object = MibTableColumn
tmnxMsdpNgSARejOriginRP = _TmnxMsdpNgSARejOriginRP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 9, 1, 7),
    _TmnxMsdpNgSARejOriginRP_Type()
)
tmnxMsdpNgSARejOriginRP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpNgSARejOriginRP.setStatus("current")
_TmnxMsdpNgSARejPeerAddrType_Type = InetAddressType
_TmnxMsdpNgSARejPeerAddrType_Object = MibTableColumn
tmnxMsdpNgSARejPeerAddrType = _TmnxMsdpNgSARejPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 9, 1, 8),
    _TmnxMsdpNgSARejPeerAddrType_Type()
)
tmnxMsdpNgSARejPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpNgSARejPeerAddrType.setStatus("current")


class _TmnxMsdpNgSARejPeerAddr_Type(InetAddress):
    """Custom type tmnxMsdpNgSARejPeerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMsdpNgSARejPeerAddr_Type.__name__ = "InetAddress"
_TmnxMsdpNgSARejPeerAddr_Object = MibTableColumn
tmnxMsdpNgSARejPeerAddr = _TmnxMsdpNgSARejPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 9, 1, 9),
    _TmnxMsdpNgSARejPeerAddr_Type()
)
tmnxMsdpNgSARejPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMsdpNgSARejPeerAddr.setStatus("current")


class _TmnxMsdpNgSARejFailureReason_Type(Integer32):
    """Custom type tmnxMsdpNgSARejFailureReason based on Integer32"""
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
        *(("importPolicyFailure", 1),
          ("exportPolicyFailure", 2),
          ("rpfFailure", 3),
          ("actSrcLimitExceeded", 4),
          ("srcActSrcLimitExceeded", 5),
          ("peerActSrcLimitExceeded", 6),
          ("groupActSrcLimitExceeded", 7),
          ("groupPeerActSrcLimitExceeded", 8))
    )


_TmnxMsdpNgSARejFailureReason_Type.__name__ = "Integer32"
_TmnxMsdpNgSARejFailureReason_Object = MibTableColumn
tmnxMsdpNgSARejFailureReason = _TmnxMsdpNgSARejFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 104, 9, 1, 10),
    _TmnxMsdpNgSARejFailureReason_Type()
)
tmnxMsdpNgSARejFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMsdpNgSARejFailureReason.setStatus("current")
_TmnxMsdpNgNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxMsdpNgNotifyPrefix = _TmnxMsdpNgNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 104)
)
_TmnxMsdpNgNotifications_ObjectIdentity = ObjectIdentity
tmnxMsdpNgNotifications = _TmnxMsdpNgNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 104, 0)
)
tmnxMsdpNgPeerEntry.registerAugmentions(
    ("TIMETRA-MSDP-NG-MIB",
     "tmnxMsdpNgPeerStatsEntry")
)
tmnxMsdpNgPeerStatsEntry.setIndexNames(*tmnxMsdpNgPeerEntry.getIndexNames())

# Managed Objects groups

tmnxMsdpNgGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 104, 2, 1)
)
tmnxMsdpNgGeneralGroup.setObjects(
      *(("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgGeneralTableLstChanged"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgMaxActiveSources"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgMsgRcvRate"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgMsgRcvRateTime"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgMsgRcvRateThd"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgDataEncapsulation"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgAdminState"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgExportPolicy1"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgExportPolicy2"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgExportPolicy3"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgExportPolicy4"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgExportPolicy5"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgImportPolicy1"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgImportPolicy2"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgImportPolicy3"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgImportPolicy4"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgImportPolicy5"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgLocalAddress"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgLocalAddressType"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgStatusPeerCount"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgStatusPeersEstablished"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgStatusSACount"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgStatusLastTimeUp"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgStatusActSrcLimExceed"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgRpfLookupSequence"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSACacheLifetime"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSARejectExportPolicy"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSARejectImportPolicy"))
)
if mibBuilder.loadTexts:
    tmnxMsdpNgGeneralGroup.setStatus("current")

tmnxMsdpNgPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 104, 2, 2)
)
tmnxMsdpNgPeerGroup.setObjects(
      *(("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerRowStatus"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerMaxActiveSources"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerMsgRcvRate"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerMsgRcvRateTime"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerMsgRcvRateThd"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerAuthKey"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerAuthKeyEncrypted"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerDefaultPeer"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerAdminState"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerExportPolicy1"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerExportPolicy2"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerExportPolicy3"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerExportPolicy4"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerExportPolicy5"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerImportPolicy1"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerImportPolicy2"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerImportPolicy3"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerImportPolicy4"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerImportPolicy5"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerLocalAddressType"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerLocalAddress"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerRowStatus"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerMaxActSrcs"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerMsgRcvRt"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerMsgRxRtTime"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerMsgRcvRtThd"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerAuthKey"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerAKeyEncrypt"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerDefaultPeer"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerAdminState"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerExportPlcy1"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerExportPlcy2"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerExportPlcy3"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerExportPlcy4"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerExportPlcy5"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerImportPlcy1"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerImportPlcy2"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerImportPlcy3"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerImportPlcy4"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerImportPlcy5"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerLocAddrType"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerLocalAddr"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerStatsActSrcLimExcd"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerStatsLastStChange"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerStatsLastMsgPeer"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerStatsRPFFailures"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerStatsRemoteCloses"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerStatsPeerTimeouts"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerStatsSAMsgsSent"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerStatsSAMsgsRx"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerStatsSAReqMsgsSent"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerStatsSAReqMsgsRx"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerStatsSAResMsgsSent"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerStatsSAResMsgsRx"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerStatsKAMsgsSent"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerStatsKAMsgsRx"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerStatsUnknMsgsRx"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerStatsErrMsgsRx"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerStatsSALearnt"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerStatsSARejExpPlcy"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerStatsSARejImpPlcy"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerStatsResvMsgsRx"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerState"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerLastUpOrDown"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerConRetry"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerStateTimer"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerTimeout"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerSAAccepted"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerSARx"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerLastASLimit"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerOperLclAddrType"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerOperLclAddr"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerState"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerLstUpOrDwn"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerConRetry"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerStateTimer"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerTimeout"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerSAAccepted"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerSARx"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerLastASLimit"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerOpAddrType"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpPeerOpAddr"))
)
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGroup.setStatus("current")

tmnxMsdpNgPeerGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 104, 2, 3)
)
tmnxMsdpNgPeerGroupGroup.setObjects(
      *(("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGroupRowStatus"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGroupMsgRcvRate"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpMsgRcvRateTime"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGroupMsgRcvRateThd"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGroupAdminState"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGroupExportPolicy1"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGroupExportPolicy2"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGroupExportPolicy3"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGroupExportPolicy4"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGroupExportPolicy5"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGroupImportPolicy1"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGroupImportPolicy2"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGroupImportPolicy3"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGroupImportPolicy4"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGroupImportPolicy5"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGroupLocalAddrType"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGroupLocalAddress"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGroupMode"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGroupMaxActSources"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGroupActMsgsExMax"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpSARejExpPolicy"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGrpSARejImpPolicy"))
)
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerGroupGroup.setStatus("current")

tmnxMsdpNgSourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 104, 2, 4)
)
tmnxMsdpNgSourceGroup.setObjects(
      *(("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSourceRowStatus"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSourceMaxActiveSources"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSourceDiscMethod"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSourceSrcActMsgsExMax"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSourceLastExEventTime"))
)
if mibBuilder.loadTexts:
    tmnxMsdpNgSourceGroup.setStatus("current")

tmnxMsdpNgSAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 104, 2, 5)
)
tmnxMsdpNgSAGroup.setObjects(
      *(("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSAPrLearnFrType"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSAPeerLearntFrom"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSARPFPeerType"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSARPFPeer"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSAUpTime"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSAExpiryTime"))
)
if mibBuilder.loadTexts:
    tmnxMsdpNgSAGroup.setStatus("current")

tmnxMsdpNgSARejGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 104, 2, 7)
)
tmnxMsdpNgSARejGroup.setObjects(
    ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSARejFailureReason")
)
if mibBuilder.loadTexts:
    tmnxMsdpNgSARejGroup.setStatus("current")


# Notification objects

tmnxMsdpNgActSrcLimExcd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 104, 0, 1)
)
tmnxMsdpNgActSrcLimExcd.setObjects(
      *(("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgMaxActiveSources"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgStatusActSrcLimExceed"))
)
if mibBuilder.loadTexts:
    tmnxMsdpNgActSrcLimExcd.setStatus(
        "current"
    )

tmnxMsdpNgPeerActSrcLimExcd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 104, 0, 2)
)
tmnxMsdpNgPeerActSrcLimExcd.setObjects(
    ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerStatsActSrcLimExcd")
)
if mibBuilder.loadTexts:
    tmnxMsdpNgPeerActSrcLimExcd.setStatus(
        "current"
    )

tmnxMsdpNgRPFFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 104, 0, 3)
)
tmnxMsdpNgRPFFailure.setObjects(
      *(("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSARPFPeerType"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSARPFPeer"))
)
if mibBuilder.loadTexts:
    tmnxMsdpNgRPFFailure.setStatus(
        "current"
    )

tmnxMsdpNgSourceSrcActMsgsExcd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 104, 0, 4)
)
tmnxMsdpNgSourceSrcActMsgsExcd.setObjects(
      *(("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSourceMaxActiveSources"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSourceSrcActMsgsExMax"))
)
if mibBuilder.loadTexts:
    tmnxMsdpNgSourceSrcActMsgsExcd.setStatus(
        "current"
    )

tmnxMsdpNgGroupSrcActMsgsExcd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 104, 0, 5)
)
tmnxMsdpNgGroupSrcActMsgsExcd.setObjects(
      *(("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGroupMaxActSources"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGroupActMsgsExMax"))
)
if mibBuilder.loadTexts:
    tmnxMsdpNgGroupSrcActMsgsExcd.setStatus(
        "current"
    )


# Notifications groups

tmnxMsdpNgNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 104, 2, 6)
)
tmnxMsdpNgNotificationGroup.setObjects(
      *(("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgActSrcLimExcd"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerActSrcLimExcd"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgRPFFailure"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSourceSrcActMsgsExcd"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgGroupSrcActMsgsExcd"))
)
if mibBuilder.loadTexts:
    tmnxMsdpNgNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxMsdpNgV13v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 104, 1, 1)
)
tmnxMsdpNgV13v0Compliance.setObjects(
      *(("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgGeneralGroup"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGroup"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgPeerGroupGroup"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSourceGroup"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSAGroup"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgSARejGroup"),
        ("TIMETRA-MSDP-NG-MIB", "tmnxMsdpNgNotificationGroup"))
)
if mibBuilder.loadTexts:
    tmnxMsdpNgV13v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-MSDP-NG-MIB",
    **{"timetraMsdpNgMIBModule": timetraMsdpNgMIBModule,
       "tmnxMsdpNgConformance": tmnxMsdpNgConformance,
       "tmnxMsdpNgCompliances": tmnxMsdpNgCompliances,
       "tmnxMsdpNgV13v0Compliance": tmnxMsdpNgV13v0Compliance,
       "tmnxMsdpNgGroups": tmnxMsdpNgGroups,
       "tmnxMsdpNgGeneralGroup": tmnxMsdpNgGeneralGroup,
       "tmnxMsdpNgPeerGroup": tmnxMsdpNgPeerGroup,
       "tmnxMsdpNgPeerGroupGroup": tmnxMsdpNgPeerGroupGroup,
       "tmnxMsdpNgSourceGroup": tmnxMsdpNgSourceGroup,
       "tmnxMsdpNgSAGroup": tmnxMsdpNgSAGroup,
       "tmnxMsdpNgNotificationGroup": tmnxMsdpNgNotificationGroup,
       "tmnxMsdpNgSARejGroup": tmnxMsdpNgSARejGroup,
       "tmnxMsdpNgObjects": tmnxMsdpNgObjects,
       "tmnxMsdpNgGlobals": tmnxMsdpNgGlobals,
       "tmnxMsdpNgGeneralTableLstChanged": tmnxMsdpNgGeneralTableLstChanged,
       "tmnxMsdpNgGeneralTable": tmnxMsdpNgGeneralTable,
       "tmnxMsdpNgGeneralEntry": tmnxMsdpNgGeneralEntry,
       "tmnxMsdpNgMaxActiveSources": tmnxMsdpNgMaxActiveSources,
       "tmnxMsdpNgMsgRcvRate": tmnxMsdpNgMsgRcvRate,
       "tmnxMsdpNgMsgRcvRateTime": tmnxMsdpNgMsgRcvRateTime,
       "tmnxMsdpNgMsgRcvRateThd": tmnxMsdpNgMsgRcvRateThd,
       "tmnxMsdpNgDataEncapsulation": tmnxMsdpNgDataEncapsulation,
       "tmnxMsdpNgAdminState": tmnxMsdpNgAdminState,
       "tmnxMsdpNgExportPolicy1": tmnxMsdpNgExportPolicy1,
       "tmnxMsdpNgExportPolicy2": tmnxMsdpNgExportPolicy2,
       "tmnxMsdpNgExportPolicy3": tmnxMsdpNgExportPolicy3,
       "tmnxMsdpNgExportPolicy4": tmnxMsdpNgExportPolicy4,
       "tmnxMsdpNgExportPolicy5": tmnxMsdpNgExportPolicy5,
       "tmnxMsdpNgImportPolicy1": tmnxMsdpNgImportPolicy1,
       "tmnxMsdpNgImportPolicy2": tmnxMsdpNgImportPolicy2,
       "tmnxMsdpNgImportPolicy3": tmnxMsdpNgImportPolicy3,
       "tmnxMsdpNgImportPolicy4": tmnxMsdpNgImportPolicy4,
       "tmnxMsdpNgImportPolicy5": tmnxMsdpNgImportPolicy5,
       "tmnxMsdpNgLocalAddressType": tmnxMsdpNgLocalAddressType,
       "tmnxMsdpNgLocalAddress": tmnxMsdpNgLocalAddress,
       "tmnxMsdpNgStatusPeerCount": tmnxMsdpNgStatusPeerCount,
       "tmnxMsdpNgStatusPeersEstablished": tmnxMsdpNgStatusPeersEstablished,
       "tmnxMsdpNgStatusSACount": tmnxMsdpNgStatusSACount,
       "tmnxMsdpNgStatusLastTimeUp": tmnxMsdpNgStatusLastTimeUp,
       "tmnxMsdpNgStatusActSrcLimExceed": tmnxMsdpNgStatusActSrcLimExceed,
       "tmnxMsdpNgRpfLookupSequence": tmnxMsdpNgRpfLookupSequence,
       "tmnxMsdpNgSACacheLifetime": tmnxMsdpNgSACacheLifetime,
       "tmnxMsdpNgSARejectExportPolicy": tmnxMsdpNgSARejectExportPolicy,
       "tmnxMsdpNgSARejectImportPolicy": tmnxMsdpNgSARejectImportPolicy,
       "tmnxMsdpNgPeerTable": tmnxMsdpNgPeerTable,
       "tmnxMsdpNgPeerEntry": tmnxMsdpNgPeerEntry,
       "tmnxMsdpNgPeerAddressType": tmnxMsdpNgPeerAddressType,
       "tmnxMsdpNgPeerAddress": tmnxMsdpNgPeerAddress,
       "tmnxMsdpNgPeerRowStatus": tmnxMsdpNgPeerRowStatus,
       "tmnxMsdpNgPeerMaxActiveSources": tmnxMsdpNgPeerMaxActiveSources,
       "tmnxMsdpNgPeerMsgRcvRate": tmnxMsdpNgPeerMsgRcvRate,
       "tmnxMsdpNgPeerMsgRcvRateTime": tmnxMsdpNgPeerMsgRcvRateTime,
       "tmnxMsdpNgPeerMsgRcvRateThd": tmnxMsdpNgPeerMsgRcvRateThd,
       "tmnxMsdpNgPeerAuthKey": tmnxMsdpNgPeerAuthKey,
       "tmnxMsdpNgPeerAuthKeyEncrypted": tmnxMsdpNgPeerAuthKeyEncrypted,
       "tmnxMsdpNgPeerDefaultPeer": tmnxMsdpNgPeerDefaultPeer,
       "tmnxMsdpNgPeerAdminState": tmnxMsdpNgPeerAdminState,
       "tmnxMsdpNgPeerExportPolicy1": tmnxMsdpNgPeerExportPolicy1,
       "tmnxMsdpNgPeerExportPolicy2": tmnxMsdpNgPeerExportPolicy2,
       "tmnxMsdpNgPeerExportPolicy3": tmnxMsdpNgPeerExportPolicy3,
       "tmnxMsdpNgPeerExportPolicy4": tmnxMsdpNgPeerExportPolicy4,
       "tmnxMsdpNgPeerExportPolicy5": tmnxMsdpNgPeerExportPolicy5,
       "tmnxMsdpNgPeerImportPolicy1": tmnxMsdpNgPeerImportPolicy1,
       "tmnxMsdpNgPeerImportPolicy2": tmnxMsdpNgPeerImportPolicy2,
       "tmnxMsdpNgPeerImportPolicy3": tmnxMsdpNgPeerImportPolicy3,
       "tmnxMsdpNgPeerImportPolicy4": tmnxMsdpNgPeerImportPolicy4,
       "tmnxMsdpNgPeerImportPolicy5": tmnxMsdpNgPeerImportPolicy5,
       "tmnxMsdpNgPeerLocalAddressType": tmnxMsdpNgPeerLocalAddressType,
       "tmnxMsdpNgPeerLocalAddress": tmnxMsdpNgPeerLocalAddress,
       "tmnxMsdpNgPeerState": tmnxMsdpNgPeerState,
       "tmnxMsdpNgPeerLastUpOrDown": tmnxMsdpNgPeerLastUpOrDown,
       "tmnxMsdpNgPeerConRetry": tmnxMsdpNgPeerConRetry,
       "tmnxMsdpNgPeerStateTimer": tmnxMsdpNgPeerStateTimer,
       "tmnxMsdpNgPeerTimeout": tmnxMsdpNgPeerTimeout,
       "tmnxMsdpNgPeerSAAccepted": tmnxMsdpNgPeerSAAccepted,
       "tmnxMsdpNgPeerSARx": tmnxMsdpNgPeerSARx,
       "tmnxMsdpNgPeerLastASLimit": tmnxMsdpNgPeerLastASLimit,
       "tmnxMsdpNgPeerOperLclAddrType": tmnxMsdpNgPeerOperLclAddrType,
       "tmnxMsdpNgPeerOperLclAddr": tmnxMsdpNgPeerOperLclAddr,
       "tmnxMsdpNgPeerGroupTable": tmnxMsdpNgPeerGroupTable,
       "tmnxMsdpNgPeerGroupEntry": tmnxMsdpNgPeerGroupEntry,
       "tmnxMsdpNgPeerGroupName": tmnxMsdpNgPeerGroupName,
       "tmnxMsdpNgPeerGroupRowStatus": tmnxMsdpNgPeerGroupRowStatus,
       "tmnxMsdpNgPeerGroupMsgRcvRate": tmnxMsdpNgPeerGroupMsgRcvRate,
       "tmnxMsdpNgPeerGrpMsgRcvRateTime": tmnxMsdpNgPeerGrpMsgRcvRateTime,
       "tmnxMsdpNgPeerGroupMsgRcvRateThd": tmnxMsdpNgPeerGroupMsgRcvRateThd,
       "tmnxMsdpNgPeerGroupAdminState": tmnxMsdpNgPeerGroupAdminState,
       "tmnxMsdpNgPeerGroupExportPolicy1": tmnxMsdpNgPeerGroupExportPolicy1,
       "tmnxMsdpNgPeerGroupExportPolicy2": tmnxMsdpNgPeerGroupExportPolicy2,
       "tmnxMsdpNgPeerGroupExportPolicy3": tmnxMsdpNgPeerGroupExportPolicy3,
       "tmnxMsdpNgPeerGroupExportPolicy4": tmnxMsdpNgPeerGroupExportPolicy4,
       "tmnxMsdpNgPeerGroupExportPolicy5": tmnxMsdpNgPeerGroupExportPolicy5,
       "tmnxMsdpNgPeerGroupImportPolicy1": tmnxMsdpNgPeerGroupImportPolicy1,
       "tmnxMsdpNgPeerGroupImportPolicy2": tmnxMsdpNgPeerGroupImportPolicy2,
       "tmnxMsdpNgPeerGroupImportPolicy3": tmnxMsdpNgPeerGroupImportPolicy3,
       "tmnxMsdpNgPeerGroupImportPolicy4": tmnxMsdpNgPeerGroupImportPolicy4,
       "tmnxMsdpNgPeerGroupImportPolicy5": tmnxMsdpNgPeerGroupImportPolicy5,
       "tmnxMsdpNgPeerGroupLocalAddrType": tmnxMsdpNgPeerGroupLocalAddrType,
       "tmnxMsdpNgPeerGroupLocalAddress": tmnxMsdpNgPeerGroupLocalAddress,
       "tmnxMsdpNgPeerGroupMode": tmnxMsdpNgPeerGroupMode,
       "tmnxMsdpNgPeerGroupMaxActSources": tmnxMsdpNgPeerGroupMaxActSources,
       "tmnxMsdpNgPeerGroupActMsgsExMax": tmnxMsdpNgPeerGroupActMsgsExMax,
       "tmnxMsdpNgPeerGrpSARejExpPolicy": tmnxMsdpNgPeerGrpSARejExpPolicy,
       "tmnxMsdpNgPeerGrpSARejImpPolicy": tmnxMsdpNgPeerGrpSARejImpPolicy,
       "tmnxMsdpNgPeerGrpPeerTable": tmnxMsdpNgPeerGrpPeerTable,
       "tmnxMsdpNgPeerGrpPeerEntry": tmnxMsdpNgPeerGrpPeerEntry,
       "tmnxMsdpNgPeerGrpPeerAddressType": tmnxMsdpNgPeerGrpPeerAddressType,
       "tmnxMsdpNgPeerGrpPeerAddress": tmnxMsdpNgPeerGrpPeerAddress,
       "tmnxMsdpNgPeerGrpPeerRowStatus": tmnxMsdpNgPeerGrpPeerRowStatus,
       "tmnxMsdpNgPeerGrpPeerMaxActSrcs": tmnxMsdpNgPeerGrpPeerMaxActSrcs,
       "tmnxMsdpNgPeerGrpPeerMsgRcvRt": tmnxMsdpNgPeerGrpPeerMsgRcvRt,
       "tmnxMsdpNgPeerGrpPeerMsgRxRtTime": tmnxMsdpNgPeerGrpPeerMsgRxRtTime,
       "tmnxMsdpNgPeerGrpPeerMsgRcvRtThd": tmnxMsdpNgPeerGrpPeerMsgRcvRtThd,
       "tmnxMsdpNgPeerGrpPeerAuthKey": tmnxMsdpNgPeerGrpPeerAuthKey,
       "tmnxMsdpNgPeerGrpPeerAKeyEncrypt": tmnxMsdpNgPeerGrpPeerAKeyEncrypt,
       "tmnxMsdpNgPeerGrpPeerDefaultPeer": tmnxMsdpNgPeerGrpPeerDefaultPeer,
       "tmnxMsdpNgPeerGrpPeerAdminState": tmnxMsdpNgPeerGrpPeerAdminState,
       "tmnxMsdpNgPeerGrpPeerExportPlcy1": tmnxMsdpNgPeerGrpPeerExportPlcy1,
       "tmnxMsdpNgPeerGrpPeerExportPlcy2": tmnxMsdpNgPeerGrpPeerExportPlcy2,
       "tmnxMsdpNgPeerGrpPeerExportPlcy3": tmnxMsdpNgPeerGrpPeerExportPlcy3,
       "tmnxMsdpNgPeerGrpPeerExportPlcy4": tmnxMsdpNgPeerGrpPeerExportPlcy4,
       "tmnxMsdpNgPeerGrpPeerExportPlcy5": tmnxMsdpNgPeerGrpPeerExportPlcy5,
       "tmnxMsdpNgPeerGrpPeerImportPlcy1": tmnxMsdpNgPeerGrpPeerImportPlcy1,
       "tmnxMsdpNgPeerGrpPeerImportPlcy2": tmnxMsdpNgPeerGrpPeerImportPlcy2,
       "tmnxMsdpNgPeerGrpPeerImportPlcy3": tmnxMsdpNgPeerGrpPeerImportPlcy3,
       "tmnxMsdpNgPeerGrpPeerImportPlcy4": tmnxMsdpNgPeerGrpPeerImportPlcy4,
       "tmnxMsdpNgPeerGrpPeerImportPlcy5": tmnxMsdpNgPeerGrpPeerImportPlcy5,
       "tmnxMsdpNgPeerGrpPeerLocAddrType": tmnxMsdpNgPeerGrpPeerLocAddrType,
       "tmnxMsdpNgPeerGrpPeerLocalAddr": tmnxMsdpNgPeerGrpPeerLocalAddr,
       "tmnxMsdpNgPeerGrpPeerState": tmnxMsdpNgPeerGrpPeerState,
       "tmnxMsdpNgPeerGrpPeerLstUpOrDwn": tmnxMsdpNgPeerGrpPeerLstUpOrDwn,
       "tmnxMsdpNgPeerGrpPeerConRetry": tmnxMsdpNgPeerGrpPeerConRetry,
       "tmnxMsdpNgPeerGrpPeerStateTimer": tmnxMsdpNgPeerGrpPeerStateTimer,
       "tmnxMsdpNgPeerGrpPeerTimeout": tmnxMsdpNgPeerGrpPeerTimeout,
       "tmnxMsdpNgPeerGrpPeerSAAccepted": tmnxMsdpNgPeerGrpPeerSAAccepted,
       "tmnxMsdpNgPeerGrpPeerSARx": tmnxMsdpNgPeerGrpPeerSARx,
       "tmnxMsdpNgPeerGrpPeerLastASLimit": tmnxMsdpNgPeerGrpPeerLastASLimit,
       "tmnxMsdpNgPeerGrpPeerOpAddrType": tmnxMsdpNgPeerGrpPeerOpAddrType,
       "tmnxMsdpNgPeerGrpPeerOpAddr": tmnxMsdpNgPeerGrpPeerOpAddr,
       "tmnxMsdpNgSourceTable": tmnxMsdpNgSourceTable,
       "tmnxMsdpNgSourceEntry": tmnxMsdpNgSourceEntry,
       "tmnxMsdpNgSourcePrefixType": tmnxMsdpNgSourcePrefixType,
       "tmnxMsdpNgSourcePrefix": tmnxMsdpNgSourcePrefix,
       "tmnxMsdpNgSourceMask": tmnxMsdpNgSourceMask,
       "tmnxMsdpNgSourceRowStatus": tmnxMsdpNgSourceRowStatus,
       "tmnxMsdpNgSourceMaxActiveSources": tmnxMsdpNgSourceMaxActiveSources,
       "tmnxMsdpNgSourceDiscMethod": tmnxMsdpNgSourceDiscMethod,
       "tmnxMsdpNgSourceSrcActMsgsExMax": tmnxMsdpNgSourceSrcActMsgsExMax,
       "tmnxMsdpNgSourceLastExEventTime": tmnxMsdpNgSourceLastExEventTime,
       "tmnxMsdpNgSATable": tmnxMsdpNgSATable,
       "tmnxMsdpNgSAEntry": tmnxMsdpNgSAEntry,
       "tmnxMsdpNgSAGroupAddrType": tmnxMsdpNgSAGroupAddrType,
       "tmnxMsdpNgSAGroupAddr": tmnxMsdpNgSAGroupAddr,
       "tmnxMsdpNgSASourceAddrType": tmnxMsdpNgSASourceAddrType,
       "tmnxMsdpNgSASourceAddr": tmnxMsdpNgSASourceAddr,
       "tmnxMsdpNgSAOriginRPType": tmnxMsdpNgSAOriginRPType,
       "tmnxMsdpNgSAOriginRP": tmnxMsdpNgSAOriginRP,
       "tmnxMsdpNgSAPrLearnFrType": tmnxMsdpNgSAPrLearnFrType,
       "tmnxMsdpNgSAPeerLearntFrom": tmnxMsdpNgSAPeerLearntFrom,
       "tmnxMsdpNgSARPFPeerType": tmnxMsdpNgSARPFPeerType,
       "tmnxMsdpNgSARPFPeer": tmnxMsdpNgSARPFPeer,
       "tmnxMsdpNgSAUpTime": tmnxMsdpNgSAUpTime,
       "tmnxMsdpNgSAExpiryTime": tmnxMsdpNgSAExpiryTime,
       "tmnxMsdpNgPeerStatsTable": tmnxMsdpNgPeerStatsTable,
       "tmnxMsdpNgPeerStatsEntry": tmnxMsdpNgPeerStatsEntry,
       "tmnxMsdpNgPeerStatsActSrcLimExcd": tmnxMsdpNgPeerStatsActSrcLimExcd,
       "tmnxMsdpNgPeerStatsLastStChange": tmnxMsdpNgPeerStatsLastStChange,
       "tmnxMsdpNgPeerStatsLastMsgPeer": tmnxMsdpNgPeerStatsLastMsgPeer,
       "tmnxMsdpNgPeerStatsRPFFailures": tmnxMsdpNgPeerStatsRPFFailures,
       "tmnxMsdpNgPeerStatsRemoteCloses": tmnxMsdpNgPeerStatsRemoteCloses,
       "tmnxMsdpNgPeerStatsPeerTimeouts": tmnxMsdpNgPeerStatsPeerTimeouts,
       "tmnxMsdpNgPeerStatsSAMsgsSent": tmnxMsdpNgPeerStatsSAMsgsSent,
       "tmnxMsdpNgPeerStatsSAMsgsRx": tmnxMsdpNgPeerStatsSAMsgsRx,
       "tmnxMsdpNgPeerStatsSAReqMsgsSent": tmnxMsdpNgPeerStatsSAReqMsgsSent,
       "tmnxMsdpNgPeerStatsSAReqMsgsRx": tmnxMsdpNgPeerStatsSAReqMsgsRx,
       "tmnxMsdpNgPeerStatsSAResMsgsSent": tmnxMsdpNgPeerStatsSAResMsgsSent,
       "tmnxMsdpNgPeerStatsSAResMsgsRx": tmnxMsdpNgPeerStatsSAResMsgsRx,
       "tmnxMsdpNgPeerStatsKAMsgsSent": tmnxMsdpNgPeerStatsKAMsgsSent,
       "tmnxMsdpNgPeerStatsKAMsgsRx": tmnxMsdpNgPeerStatsKAMsgsRx,
       "tmnxMsdpNgPeerStatsUnknMsgsRx": tmnxMsdpNgPeerStatsUnknMsgsRx,
       "tmnxMsdpNgPeerStatsErrMsgsRx": tmnxMsdpNgPeerStatsErrMsgsRx,
       "tmnxMsdpNgPeerStatsSALearnt": tmnxMsdpNgPeerStatsSALearnt,
       "tmnxMsdpNgPeerStatsSARejExpPlcy": tmnxMsdpNgPeerStatsSARejExpPlcy,
       "tmnxMsdpNgPeerStatsSARejImpPlcy": tmnxMsdpNgPeerStatsSARejImpPlcy,
       "tmnxMsdpNgPeerStatsResvMsgsRx": tmnxMsdpNgPeerStatsResvMsgsRx,
       "tmnxMsdpNgSrcActRejTable": tmnxMsdpNgSrcActRejTable,
       "tmnxMsdpNgSrcActRejEntry": tmnxMsdpNgSrcActRejEntry,
       "tmnxMsdpNgSARejPeerGroupName": tmnxMsdpNgSARejPeerGroupName,
       "tmnxMsdpNgSARejGroupAddrType": tmnxMsdpNgSARejGroupAddrType,
       "tmnxMsdpNgSARejGroupAddr": tmnxMsdpNgSARejGroupAddr,
       "tmnxMsdpNgSARejSourceAddrType": tmnxMsdpNgSARejSourceAddrType,
       "tmnxMsdpNgSARejSourceAddr": tmnxMsdpNgSARejSourceAddr,
       "tmnxMsdpNgSARejOriginRPType": tmnxMsdpNgSARejOriginRPType,
       "tmnxMsdpNgSARejOriginRP": tmnxMsdpNgSARejOriginRP,
       "tmnxMsdpNgSARejPeerAddrType": tmnxMsdpNgSARejPeerAddrType,
       "tmnxMsdpNgSARejPeerAddr": tmnxMsdpNgSARejPeerAddr,
       "tmnxMsdpNgSARejFailureReason": tmnxMsdpNgSARejFailureReason,
       "tmnxMsdpNgNotifyPrefix": tmnxMsdpNgNotifyPrefix,
       "tmnxMsdpNgNotifications": tmnxMsdpNgNotifications,
       "tmnxMsdpNgActSrcLimExcd": tmnxMsdpNgActSrcLimExcd,
       "tmnxMsdpNgPeerActSrcLimExcd": tmnxMsdpNgPeerActSrcLimExcd,
       "tmnxMsdpNgRPFFailure": tmnxMsdpNgRPFFailure,
       "tmnxMsdpNgSourceSrcActMsgsExcd": tmnxMsdpNgSourceSrcActMsgsExcd,
       "tmnxMsdpNgGroupSrcActMsgsExcd": tmnxMsdpNgGroupSrcActMsgsExcd}
)
