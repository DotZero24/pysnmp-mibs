# SNMP MIB module (TIMETRA-TLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-TLS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:53:45 2025
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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")

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
 TTcpUdpPort,
 TmnxAdminState,
 TmnxOperState,
 TmnxVRtrID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TTcpUdpPort",
    "TmnxAdminState",
    "TmnxOperState",
    "TmnxVRtrID")


# MODULE-IDENTITY

timetraTlsMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 107)
)
if mibBuilder.loadTexts:
    timetraTlsMIBModule.setRevisions(
        ("2017-01-01 00:00",
         "2015-10-05 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TTlsCipherSuiteCode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10,
              47,
              53,
              59,
              60,
              61)
        )
    )
    namedValues = NamedValues(
        *(("tlsRsaWithNullMd5", 1),
          ("tlsRsaWithNullSha", 2),
          ("tlsRsaWith3desEdeCbcSha", 10),
          ("tlsRsaWithAes128CbcSha", 47),
          ("tlsRsaWithAes256CbcSha", 53),
          ("tlsRsaWithNullSha256", 59),
          ("tlsRsaWithAes128CbcSha256", 60),
          ("tlsRsaWithAes256CbcSha256", 61))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxTlsConformance_ObjectIdentity = ObjectIdentity
tmnxTlsConformance = _TmnxTlsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 107)
)
_TmnxTlsCompliances_ObjectIdentity = ObjectIdentity
tmnxTlsCompliances = _TmnxTlsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 107, 1)
)
_TmnxTlsGroups_ObjectIdentity = ObjectIdentity
tmnxTlsGroups = _TmnxTlsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 107, 2)
)
_TmnxTlsV14v1Groups_ObjectIdentity = ObjectIdentity
tmnxTlsV14v1Groups = _TmnxTlsV14v1Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 107, 2, 1)
)
_TmnxTlsV15v0Groups_ObjectIdentity = ObjectIdentity
tmnxTlsV15v0Groups = _TmnxTlsV15v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 107, 2, 2)
)
_TmnxTlsObjs_ObjectIdentity = ObjectIdentity
tmnxTlsObjs = _TmnxTlsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107)
)
_TmnxTlsScalarObjs_ObjectIdentity = ObjectIdentity
tmnxTlsScalarObjs = _TmnxTlsScalarObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 1)
)
_TmnxTlsConfigTimeStamps_ObjectIdentity = ObjectIdentity
tmnxTlsConfigTimeStamps = _TmnxTlsConfigTimeStamps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 1, 1)
)
_TTlsCertProfileTblLastChgd_Type = TimeStamp
_TTlsCertProfileTblLastChgd_Object = MibScalar
tTlsCertProfileTblLastChgd = _TTlsCertProfileTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 1, 1, 1),
    _TTlsCertProfileTblLastChgd_Type()
)
tTlsCertProfileTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsCertProfileTblLastChgd.setStatus("current")
_TTlsCertProfEntryIdTblLastChgd_Type = TimeStamp
_TTlsCertProfEntryIdTblLastChgd_Object = MibScalar
tTlsCertProfEntryIdTblLastChgd = _TTlsCertProfEntryIdTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 1, 1, 2),
    _TTlsCertProfEntryIdTblLastChgd_Type()
)
tTlsCertProfEntryIdTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsCertProfEntryIdTblLastChgd.setStatus("current")
_TTlsCertChainCAProfTblLastChgd_Type = TimeStamp
_TTlsCertChainCAProfTblLastChgd_Object = MibScalar
tTlsCertChainCAProfTblLastChgd = _TTlsCertChainCAProfTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 1, 1, 3),
    _TTlsCertChainCAProfTblLastChgd_Type()
)
tTlsCertChainCAProfTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsCertChainCAProfTblLastChgd.setStatus("current")
_TTlsTrustAnchorProfTblLastChgd_Type = TimeStamp
_TTlsTrustAnchorProfTblLastChgd_Object = MibScalar
tTlsTrustAnchorProfTblLastChgd = _TTlsTrustAnchorProfTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 1, 1, 4),
    _TTlsTrustAnchorProfTblLastChgd_Type()
)
tTlsTrustAnchorProfTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsTrustAnchorProfTblLastChgd.setStatus("current")
_TTlsTrustAnchorsTblLastChgd_Type = TimeStamp
_TTlsTrustAnchorsTblLastChgd_Object = MibScalar
tTlsTrustAnchorsTblLastChgd = _TTlsTrustAnchorsTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 1, 1, 5),
    _TTlsTrustAnchorsTblLastChgd_Type()
)
tTlsTrustAnchorsTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsTrustAnchorsTblLastChgd.setStatus("current")
_TTlsClientCiphListTblLastChgd_Type = TimeStamp
_TTlsClientCiphListTblLastChgd_Object = MibScalar
tTlsClientCiphListTblLastChgd = _TTlsClientCiphListTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 1, 1, 6),
    _TTlsClientCiphListTblLastChgd_Type()
)
tTlsClientCiphListTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsClientCiphListTblLastChgd.setStatus("current")
_TTlsClntCiphListParTblLastChgd_Type = TimeStamp
_TTlsClntCiphListParTblLastChgd_Object = MibScalar
tTlsClntCiphListParTblLastChgd = _TTlsClntCiphListParTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 1, 1, 7),
    _TTlsClntCiphListParTblLastChgd_Type()
)
tTlsClntCiphListParTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsClntCiphListParTblLastChgd.setStatus("current")
_TTlsClntProfileTblLastChgd_Type = TimeStamp
_TTlsClntProfileTblLastChgd_Object = MibScalar
tTlsClntProfileTblLastChgd = _TTlsClntProfileTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 1, 1, 8),
    _TTlsClntProfileTblLastChgd_Type()
)
tTlsClntProfileTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsClntProfileTblLastChgd.setStatus("current")
_TTlsServerCiphListTblLastChgd_Type = TimeStamp
_TTlsServerCiphListTblLastChgd_Object = MibScalar
tTlsServerCiphListTblLastChgd = _TTlsServerCiphListTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 1, 1, 9),
    _TTlsServerCiphListTblLastChgd_Type()
)
tTlsServerCiphListTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsServerCiphListTblLastChgd.setStatus("current")
_TTlsSrvCiphListParTblLastChgd_Type = TimeStamp
_TTlsSrvCiphListParTblLastChgd_Object = MibScalar
tTlsSrvCiphListParTblLastChgd = _TTlsSrvCiphListParTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 1, 1, 10),
    _TTlsSrvCiphListParTblLastChgd_Type()
)
tTlsSrvCiphListParTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsSrvCiphListParTblLastChgd.setStatus("current")
_TTlsSrvProfileTblLastChgd_Type = TimeStamp
_TTlsSrvProfileTblLastChgd_Object = MibScalar
tTlsSrvProfileTblLastChgd = _TTlsSrvProfileTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 1, 1, 11),
    _TTlsSrvProfileTblLastChgd_Type()
)
tTlsSrvProfileTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsSrvProfileTblLastChgd.setStatus("current")
_TmnxTlsConfigObjs_ObjectIdentity = ObjectIdentity
tmnxTlsConfigObjs = _TmnxTlsConfigObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2)
)
_TTlsCertProfileTable_Object = MibTable
tTlsCertProfileTable = _TTlsCertProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 1)
)
if mibBuilder.loadTexts:
    tTlsCertProfileTable.setStatus("current")
_TTlsCertProfileEntry_Object = MibTableRow
tTlsCertProfileEntry = _TTlsCertProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 1, 1)
)
tTlsCertProfileEntry.setIndexNames(
    (0, "TIMETRA-TLS-MIB", "tTlsCertProfileName"),
)
if mibBuilder.loadTexts:
    tTlsCertProfileEntry.setStatus("current")
_TTlsCertProfileName_Type = TNamedItem
_TTlsCertProfileName_Object = MibTableColumn
tTlsCertProfileName = _TTlsCertProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 1, 1, 1),
    _TTlsCertProfileName_Type()
)
tTlsCertProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tTlsCertProfileName.setStatus("current")
_TTlsCertProfileLastChgd_Type = TimeStamp
_TTlsCertProfileLastChgd_Object = MibTableColumn
tTlsCertProfileLastChgd = _TTlsCertProfileLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 1, 1, 2),
    _TTlsCertProfileLastChgd_Type()
)
tTlsCertProfileLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsCertProfileLastChgd.setStatus("current")
_TTlsCertProfileRowStatus_Type = RowStatus
_TTlsCertProfileRowStatus_Object = MibTableColumn
tTlsCertProfileRowStatus = _TTlsCertProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 1, 1, 3),
    _TTlsCertProfileRowStatus_Type()
)
tTlsCertProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTlsCertProfileRowStatus.setStatus("current")


class _TTlsCertProfileAdminState_Type(TmnxAdminState):
    """Custom type tTlsCertProfileAdminState based on TmnxAdminState"""
    defaultValue = 3


_TTlsCertProfileAdminState_Type.__name__ = "TmnxAdminState"
_TTlsCertProfileAdminState_Object = MibTableColumn
tTlsCertProfileAdminState = _TTlsCertProfileAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 1, 1, 4),
    _TTlsCertProfileAdminState_Type()
)
tTlsCertProfileAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTlsCertProfileAdminState.setStatus("current")
_TTlsCertProfileOperState_Type = TmnxOperState
_TTlsCertProfileOperState_Object = MibTableColumn
tTlsCertProfileOperState = _TTlsCertProfileOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 1, 1, 5),
    _TTlsCertProfileOperState_Type()
)
tTlsCertProfileOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsCertProfileOperState.setStatus("current")


class _TTlsCertProfileOperFlags_Type(Bits):
    """Custom type tTlsCertProfileOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("profileAdminDown", 0),
          ("invalidCertFile", 1),
          ("invalidKeyFile", 2),
          ("invalidCertKeyCombo", 3),
          ("caProfileOperDown", 4),
          ("invalidCAProfEntry", 5))
    )

_TTlsCertProfileOperFlags_Type.__name__ = "Bits"
_TTlsCertProfileOperFlags_Object = MibTableColumn
tTlsCertProfileOperFlags = _TTlsCertProfileOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 1, 1, 6),
    _TTlsCertProfileOperFlags_Type()
)
tTlsCertProfileOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsCertProfileOperFlags.setStatus("current")
_TTlsCertProfEntryIdTable_Object = MibTable
tTlsCertProfEntryIdTable = _TTlsCertProfEntryIdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 2)
)
if mibBuilder.loadTexts:
    tTlsCertProfEntryIdTable.setStatus("current")
_TTlsCertProfEntryIdEntry_Object = MibTableRow
tTlsCertProfEntryIdEntry = _TTlsCertProfEntryIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 2, 1)
)
tTlsCertProfEntryIdEntry.setIndexNames(
    (0, "TIMETRA-TLS-MIB", "tTlsCertProfileName"),
    (0, "TIMETRA-TLS-MIB", "tTlsCertProfEntryId"),
)
if mibBuilder.loadTexts:
    tTlsCertProfEntryIdEntry.setStatus("current")


class _TTlsCertProfEntryId_Type(Integer32):
    """Custom type tTlsCertProfEntryId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TTlsCertProfEntryId_Type.__name__ = "Integer32"
_TTlsCertProfEntryId_Object = MibTableColumn
tTlsCertProfEntryId = _TTlsCertProfEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 2, 1, 1),
    _TTlsCertProfEntryId_Type()
)
tTlsCertProfEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tTlsCertProfEntryId.setStatus("current")
_TTlsCertProfEntryIdLastChgd_Type = TimeStamp
_TTlsCertProfEntryIdLastChgd_Object = MibTableColumn
tTlsCertProfEntryIdLastChgd = _TTlsCertProfEntryIdLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 2, 1, 2),
    _TTlsCertProfEntryIdLastChgd_Type()
)
tTlsCertProfEntryIdLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsCertProfEntryIdLastChgd.setStatus("current")
_TTlsCertProfEntryIdRowStatus_Type = RowStatus
_TTlsCertProfEntryIdRowStatus_Object = MibTableColumn
tTlsCertProfEntryIdRowStatus = _TTlsCertProfEntryIdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 2, 1, 3),
    _TTlsCertProfEntryIdRowStatus_Type()
)
tTlsCertProfEntryIdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTlsCertProfEntryIdRowStatus.setStatus("current")


class _TTlsCertProfEntryIdCertFile_Type(DisplayString):
    """Custom type tTlsCertProfEntryIdCertFile based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 95),
    )


_TTlsCertProfEntryIdCertFile_Type.__name__ = "DisplayString"
_TTlsCertProfEntryIdCertFile_Object = MibTableColumn
tTlsCertProfEntryIdCertFile = _TTlsCertProfEntryIdCertFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 2, 1, 4),
    _TTlsCertProfEntryIdCertFile_Type()
)
tTlsCertProfEntryIdCertFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTlsCertProfEntryIdCertFile.setStatus("current")


class _TTlsCertProfEntryIdKeyFile_Type(DisplayString):
    """Custom type tTlsCertProfEntryIdKeyFile based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 95),
    )


_TTlsCertProfEntryIdKeyFile_Type.__name__ = "DisplayString"
_TTlsCertProfEntryIdKeyFile_Object = MibTableColumn
tTlsCertProfEntryIdKeyFile = _TTlsCertProfEntryIdKeyFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 2, 1, 5),
    _TTlsCertProfEntryIdKeyFile_Type()
)
tTlsCertProfEntryIdKeyFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTlsCertProfEntryIdKeyFile.setStatus("current")


class _TTlsCertProfEntryIdCompChain_Type(Integer32):
    """Custom type tTlsCertProfEntryIdCompChain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("partial", 1),
          ("complete", 2))
    )


_TTlsCertProfEntryIdCompChain_Type.__name__ = "Integer32"
_TTlsCertProfEntryIdCompChain_Object = MibTableColumn
tTlsCertProfEntryIdCompChain = _TTlsCertProfEntryIdCompChain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 2, 1, 6),
    _TTlsCertProfEntryIdCompChain_Type()
)
tTlsCertProfEntryIdCompChain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsCertProfEntryIdCompChain.setStatus("current")


class _TTlsCertProfEntryIdOperFlags_Type(Bits):
    """Custom type tTlsCertProfEntryIdOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("profileAdminDown", 0),
          ("invalidCertFile", 1),
          ("invalidKeyFile", 2),
          ("invalidCertKeyCombo", 3),
          ("caProfileOperDown", 4),
          ("invalidCAProfEntry", 5))
    )

_TTlsCertProfEntryIdOperFlags_Type.__name__ = "Bits"
_TTlsCertProfEntryIdOperFlags_Object = MibTableColumn
tTlsCertProfEntryIdOperFlags = _TTlsCertProfEntryIdOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 2, 1, 7),
    _TTlsCertProfEntryIdOperFlags_Type()
)
tTlsCertProfEntryIdOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsCertProfEntryIdOperFlags.setStatus("current")
_TTlsCompChainCAProfTable_Object = MibTable
tTlsCompChainCAProfTable = _TTlsCompChainCAProfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 3)
)
if mibBuilder.loadTexts:
    tTlsCompChainCAProfTable.setStatus("current")
_TTlsCompChainCAProfEntry_Object = MibTableRow
tTlsCompChainCAProfEntry = _TTlsCompChainCAProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 3, 1)
)
tTlsCompChainCAProfEntry.setIndexNames(
    (0, "TIMETRA-TLS-MIB", "tTlsCertProfileName"),
    (0, "TIMETRA-TLS-MIB", "tTlsCertProfEntryId"),
    (0, "TIMETRA-TLS-MIB", "tTlsCompChainCAProfOrder"),
)
if mibBuilder.loadTexts:
    tTlsCompChainCAProfEntry.setStatus("current")
_TTlsCompChainCAProfOrder_Type = Integer32
_TTlsCompChainCAProfOrder_Object = MibTableColumn
tTlsCompChainCAProfOrder = _TTlsCompChainCAProfOrder_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 3, 1, 1),
    _TTlsCompChainCAProfOrder_Type()
)
tTlsCompChainCAProfOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tTlsCompChainCAProfOrder.setStatus("current")
_TTlsCompChainCAProfName_Type = TNamedItem
_TTlsCompChainCAProfName_Object = MibTableColumn
tTlsCompChainCAProfName = _TTlsCompChainCAProfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 3, 1, 2),
    _TTlsCompChainCAProfName_Type()
)
tTlsCompChainCAProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsCompChainCAProfName.setStatus("current")
_TTlsCertChainCAProfTable_Object = MibTable
tTlsCertChainCAProfTable = _TTlsCertChainCAProfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 4)
)
if mibBuilder.loadTexts:
    tTlsCertChainCAProfTable.setStatus("current")
_TTlsCertChainCAProfEntry_Object = MibTableRow
tTlsCertChainCAProfEntry = _TTlsCertChainCAProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 4, 1)
)
tTlsCertChainCAProfEntry.setIndexNames(
    (0, "TIMETRA-TLS-MIB", "tTlsCertProfileName"),
    (0, "TIMETRA-TLS-MIB", "tTlsCertProfEntryId"),
    (0, "TIMETRA-TLS-MIB", "tTlsCertChainCAProfName"),
)
if mibBuilder.loadTexts:
    tTlsCertChainCAProfEntry.setStatus("current")
_TTlsCertChainCAProfName_Type = TNamedItem
_TTlsCertChainCAProfName_Object = MibTableColumn
tTlsCertChainCAProfName = _TTlsCertChainCAProfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 4, 1, 1),
    _TTlsCertChainCAProfName_Type()
)
tTlsCertChainCAProfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tTlsCertChainCAProfName.setStatus("current")
_TTlsCertChainCAProfLastChgd_Type = TimeStamp
_TTlsCertChainCAProfLastChgd_Object = MibTableColumn
tTlsCertChainCAProfLastChgd = _TTlsCertChainCAProfLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 4, 1, 2),
    _TTlsCertChainCAProfLastChgd_Type()
)
tTlsCertChainCAProfLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsCertChainCAProfLastChgd.setStatus("current")
_TTlsCertChainCAProfRowStatus_Type = RowStatus
_TTlsCertChainCAProfRowStatus_Object = MibTableColumn
tTlsCertChainCAProfRowStatus = _TTlsCertChainCAProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 4, 1, 3),
    _TTlsCertChainCAProfRowStatus_Type()
)
tTlsCertChainCAProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTlsCertChainCAProfRowStatus.setStatus("current")
_TTlsTrustAnchorProfTable_Object = MibTable
tTlsTrustAnchorProfTable = _TTlsTrustAnchorProfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 5)
)
if mibBuilder.loadTexts:
    tTlsTrustAnchorProfTable.setStatus("current")
_TTlsTrustAnchorProfEntry_Object = MibTableRow
tTlsTrustAnchorProfEntry = _TTlsTrustAnchorProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 5, 1)
)
tTlsTrustAnchorProfEntry.setIndexNames(
    (0, "TIMETRA-TLS-MIB", "tTlsTrustAnchorProfName"),
)
if mibBuilder.loadTexts:
    tTlsTrustAnchorProfEntry.setStatus("current")
_TTlsTrustAnchorProfName_Type = TNamedItem
_TTlsTrustAnchorProfName_Object = MibTableColumn
tTlsTrustAnchorProfName = _TTlsTrustAnchorProfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 5, 1, 1),
    _TTlsTrustAnchorProfName_Type()
)
tTlsTrustAnchorProfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tTlsTrustAnchorProfName.setStatus("current")
_TTlsTrustAnchorProfLastChgd_Type = TimeStamp
_TTlsTrustAnchorProfLastChgd_Object = MibTableColumn
tTlsTrustAnchorProfLastChgd = _TTlsTrustAnchorProfLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 5, 1, 2),
    _TTlsTrustAnchorProfLastChgd_Type()
)
tTlsTrustAnchorProfLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsTrustAnchorProfLastChgd.setStatus("current")
_TTlsTrustAnchorProfRowStatus_Type = RowStatus
_TTlsTrustAnchorProfRowStatus_Object = MibTableColumn
tTlsTrustAnchorProfRowStatus = _TTlsTrustAnchorProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 5, 1, 3),
    _TTlsTrustAnchorProfRowStatus_Type()
)
tTlsTrustAnchorProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTlsTrustAnchorProfRowStatus.setStatus("current")
_TTlsTrustAnchorCAProfDown_Type = Integer32
_TTlsTrustAnchorCAProfDown_Object = MibTableColumn
tTlsTrustAnchorCAProfDown = _TTlsTrustAnchorCAProfDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 5, 1, 4),
    _TTlsTrustAnchorCAProfDown_Type()
)
tTlsTrustAnchorCAProfDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsTrustAnchorCAProfDown.setStatus("current")
_TTlsTrustAnchorsTable_Object = MibTable
tTlsTrustAnchorsTable = _TTlsTrustAnchorsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 6)
)
if mibBuilder.loadTexts:
    tTlsTrustAnchorsTable.setStatus("current")
_TTlsTrustAnchorsEntry_Object = MibTableRow
tTlsTrustAnchorsEntry = _TTlsTrustAnchorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 6, 1)
)
tTlsTrustAnchorsEntry.setIndexNames(
    (0, "TIMETRA-TLS-MIB", "tTlsTrustAnchorProfName"),
    (0, "TIMETRA-TLS-MIB", "tTlsTrustAnchorsCAProfile"),
)
if mibBuilder.loadTexts:
    tTlsTrustAnchorsEntry.setStatus("current")
_TTlsTrustAnchorsCAProfile_Type = TNamedItem
_TTlsTrustAnchorsCAProfile_Object = MibTableColumn
tTlsTrustAnchorsCAProfile = _TTlsTrustAnchorsCAProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 6, 1, 1),
    _TTlsTrustAnchorsCAProfile_Type()
)
tTlsTrustAnchorsCAProfile.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tTlsTrustAnchorsCAProfile.setStatus("current")
_TTlsTrustAnchorsLastChgd_Type = TimeStamp
_TTlsTrustAnchorsLastChgd_Object = MibTableColumn
tTlsTrustAnchorsLastChgd = _TTlsTrustAnchorsLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 6, 1, 2),
    _TTlsTrustAnchorsLastChgd_Type()
)
tTlsTrustAnchorsLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsTrustAnchorsLastChgd.setStatus("current")
_TTlsTrustAnchorsRowStatus_Type = RowStatus
_TTlsTrustAnchorsRowStatus_Object = MibTableColumn
tTlsTrustAnchorsRowStatus = _TTlsTrustAnchorsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 6, 1, 3),
    _TTlsTrustAnchorsRowStatus_Type()
)
tTlsTrustAnchorsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTlsTrustAnchorsRowStatus.setStatus("current")
_TTlsClientCiphListTable_Object = MibTable
tTlsClientCiphListTable = _TTlsClientCiphListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 7)
)
if mibBuilder.loadTexts:
    tTlsClientCiphListTable.setStatus("current")
_TTlsClientCiphListEntry_Object = MibTableRow
tTlsClientCiphListEntry = _TTlsClientCiphListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 7, 1)
)
tTlsClientCiphListEntry.setIndexNames(
    (0, "TIMETRA-TLS-MIB", "tTlsClientCiphListName"),
)
if mibBuilder.loadTexts:
    tTlsClientCiphListEntry.setStatus("current")
_TTlsClientCiphListName_Type = TNamedItem
_TTlsClientCiphListName_Object = MibTableColumn
tTlsClientCiphListName = _TTlsClientCiphListName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 7, 1, 1),
    _TTlsClientCiphListName_Type()
)
tTlsClientCiphListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tTlsClientCiphListName.setStatus("current")
_TTlsClientCiphListLastChgd_Type = TimeStamp
_TTlsClientCiphListLastChgd_Object = MibTableColumn
tTlsClientCiphListLastChgd = _TTlsClientCiphListLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 7, 1, 2),
    _TTlsClientCiphListLastChgd_Type()
)
tTlsClientCiphListLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsClientCiphListLastChgd.setStatus("current")
_TTlsClientCiphListRowStatus_Type = RowStatus
_TTlsClientCiphListRowStatus_Object = MibTableColumn
tTlsClientCiphListRowStatus = _TTlsClientCiphListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 7, 1, 3),
    _TTlsClientCiphListRowStatus_Type()
)
tTlsClientCiphListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTlsClientCiphListRowStatus.setStatus("current")
_TTlsClntCiphListParamTable_Object = MibTable
tTlsClntCiphListParamTable = _TTlsClntCiphListParamTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 8)
)
if mibBuilder.loadTexts:
    tTlsClntCiphListParamTable.setStatus("current")
_TTlsClntCiphListParamEntry_Object = MibTableRow
tTlsClntCiphListParamEntry = _TTlsClntCiphListParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 8, 1)
)
tTlsClntCiphListParamEntry.setIndexNames(
    (0, "TIMETRA-TLS-MIB", "tTlsClientCiphListName"),
    (0, "TIMETRA-TLS-MIB", "tTlsClntCiphListParamIndex"),
)
if mibBuilder.loadTexts:
    tTlsClntCiphListParamEntry.setStatus("current")


class _TTlsClntCiphListParamIndex_Type(Unsigned32):
    """Custom type tTlsClntCiphListParamIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TTlsClntCiphListParamIndex_Type.__name__ = "Unsigned32"
_TTlsClntCiphListParamIndex_Object = MibTableColumn
tTlsClntCiphListParamIndex = _TTlsClntCiphListParamIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 8, 1, 1),
    _TTlsClntCiphListParamIndex_Type()
)
tTlsClntCiphListParamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tTlsClntCiphListParamIndex.setStatus("current")
_TTlsClntCiphListParamLastChgd_Type = TimeStamp
_TTlsClntCiphListParamLastChgd_Object = MibTableColumn
tTlsClntCiphListParamLastChgd = _TTlsClntCiphListParamLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 8, 1, 2),
    _TTlsClntCiphListParamLastChgd_Type()
)
tTlsClntCiphListParamLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsClntCiphListParamLastChgd.setStatus("current")
_TTlsClntCiphListParamRowStatus_Type = RowStatus
_TTlsClntCiphListParamRowStatus_Object = MibTableColumn
tTlsClntCiphListParamRowStatus = _TTlsClntCiphListParamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 8, 1, 3),
    _TTlsClntCiphListParamRowStatus_Type()
)
tTlsClntCiphListParamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTlsClntCiphListParamRowStatus.setStatus("current")
_TTlsClntCiphListParamSuiteCode_Type = TTlsCipherSuiteCode
_TTlsClntCiphListParamSuiteCode_Object = MibTableColumn
tTlsClntCiphListParamSuiteCode = _TTlsClntCiphListParamSuiteCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 8, 1, 4),
    _TTlsClntCiphListParamSuiteCode_Type()
)
tTlsClntCiphListParamSuiteCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTlsClntCiphListParamSuiteCode.setStatus("current")
_TTlsClntProfileTable_Object = MibTable
tTlsClntProfileTable = _TTlsClntProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 9)
)
if mibBuilder.loadTexts:
    tTlsClntProfileTable.setStatus("current")
_TTlsClntProfileEntry_Object = MibTableRow
tTlsClntProfileEntry = _TTlsClntProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 9, 1)
)
tTlsClntProfileEntry.setIndexNames(
    (0, "TIMETRA-TLS-MIB", "tTlsClntProfileName"),
)
if mibBuilder.loadTexts:
    tTlsClntProfileEntry.setStatus("current")
_TTlsClntProfileName_Type = TNamedItem
_TTlsClntProfileName_Object = MibTableColumn
tTlsClntProfileName = _TTlsClntProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 9, 1, 1),
    _TTlsClntProfileName_Type()
)
tTlsClntProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tTlsClntProfileName.setStatus("current")
_TTlsClntProfileLastChgd_Type = TimeStamp
_TTlsClntProfileLastChgd_Object = MibTableColumn
tTlsClntProfileLastChgd = _TTlsClntProfileLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 9, 1, 2),
    _TTlsClntProfileLastChgd_Type()
)
tTlsClntProfileLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsClntProfileLastChgd.setStatus("current")
_TTlsClntProfileRowStatus_Type = RowStatus
_TTlsClntProfileRowStatus_Object = MibTableColumn
tTlsClntProfileRowStatus = _TTlsClntProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 9, 1, 3),
    _TTlsClntProfileRowStatus_Type()
)
tTlsClntProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTlsClntProfileRowStatus.setStatus("current")


class _TTlsClntProfileAdminState_Type(TmnxAdminState):
    """Custom type tTlsClntProfileAdminState based on TmnxAdminState"""
    defaultValue = 3


_TTlsClntProfileAdminState_Type.__name__ = "TmnxAdminState"
_TTlsClntProfileAdminState_Object = MibTableColumn
tTlsClntProfileAdminState = _TTlsClntProfileAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 9, 1, 4),
    _TTlsClntProfileAdminState_Type()
)
tTlsClntProfileAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTlsClntProfileAdminState.setStatus("current")
_TTlsClntProfileOperState_Type = TmnxOperState
_TTlsClntProfileOperState_Object = MibTableColumn
tTlsClntProfileOperState = _TTlsClntProfileOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 9, 1, 5),
    _TTlsClntProfileOperState_Type()
)
tTlsClntProfileOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsClntProfileOperState.setStatus("current")


class _TTlsClntProfileCiphListName_Type(TNamedItemOrEmpty):
    """Custom type tTlsClntProfileCiphListName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TTlsClntProfileCiphListName_Type.__name__ = "TNamedItemOrEmpty"
_TTlsClntProfileCiphListName_Object = MibTableColumn
tTlsClntProfileCiphListName = _TTlsClntProfileCiphListName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 9, 1, 6),
    _TTlsClntProfileCiphListName_Type()
)
tTlsClntProfileCiphListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTlsClntProfileCiphListName.setStatus("current")


class _TTlsClntProfileCertProfile_Type(TNamedItemOrEmpty):
    """Custom type tTlsClntProfileCertProfile based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TTlsClntProfileCertProfile_Type.__name__ = "TNamedItemOrEmpty"
_TTlsClntProfileCertProfile_Object = MibTableColumn
tTlsClntProfileCertProfile = _TTlsClntProfileCertProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 9, 1, 7),
    _TTlsClntProfileCertProfile_Type()
)
tTlsClntProfileCertProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTlsClntProfileCertProfile.setStatus("current")


class _TTlsClntProfileTrstAnchrProf_Type(TNamedItemOrEmpty):
    """Custom type tTlsClntProfileTrstAnchrProf based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TTlsClntProfileTrstAnchrProf_Type.__name__ = "TNamedItemOrEmpty"
_TTlsClntProfileTrstAnchrProf_Object = MibTableColumn
tTlsClntProfileTrstAnchrProf = _TTlsClntProfileTrstAnchrProf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 9, 1, 8),
    _TTlsClntProfileTrstAnchrProf_Type()
)
tTlsClntProfileTrstAnchrProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTlsClntProfileTrstAnchrProf.setStatus("current")
_TTlsServerCiphListTable_Object = MibTable
tTlsServerCiphListTable = _TTlsServerCiphListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 10)
)
if mibBuilder.loadTexts:
    tTlsServerCiphListTable.setStatus("current")
_TTlsServerCiphListEntry_Object = MibTableRow
tTlsServerCiphListEntry = _TTlsServerCiphListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 10, 1)
)
tTlsServerCiphListEntry.setIndexNames(
    (0, "TIMETRA-TLS-MIB", "tTlsServerCiphListName"),
)
if mibBuilder.loadTexts:
    tTlsServerCiphListEntry.setStatus("current")
_TTlsServerCiphListName_Type = TNamedItem
_TTlsServerCiphListName_Object = MibTableColumn
tTlsServerCiphListName = _TTlsServerCiphListName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 10, 1, 1),
    _TTlsServerCiphListName_Type()
)
tTlsServerCiphListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tTlsServerCiphListName.setStatus("current")
_TTlsServerCiphListLastChgd_Type = TimeStamp
_TTlsServerCiphListLastChgd_Object = MibTableColumn
tTlsServerCiphListLastChgd = _TTlsServerCiphListLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 10, 1, 2),
    _TTlsServerCiphListLastChgd_Type()
)
tTlsServerCiphListLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsServerCiphListLastChgd.setStatus("current")
_TTlsServerCiphListRowStatus_Type = RowStatus
_TTlsServerCiphListRowStatus_Object = MibTableColumn
tTlsServerCiphListRowStatus = _TTlsServerCiphListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 10, 1, 3),
    _TTlsServerCiphListRowStatus_Type()
)
tTlsServerCiphListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTlsServerCiphListRowStatus.setStatus("current")
_TTlsSrvCiphListParamTable_Object = MibTable
tTlsSrvCiphListParamTable = _TTlsSrvCiphListParamTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 11)
)
if mibBuilder.loadTexts:
    tTlsSrvCiphListParamTable.setStatus("current")
_TTlsSrvCiphListParamEntry_Object = MibTableRow
tTlsSrvCiphListParamEntry = _TTlsSrvCiphListParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 11, 1)
)
tTlsSrvCiphListParamEntry.setIndexNames(
    (0, "TIMETRA-TLS-MIB", "tTlsServerCiphListName"),
    (0, "TIMETRA-TLS-MIB", "tTlsSrvCiphListParamIndex"),
)
if mibBuilder.loadTexts:
    tTlsSrvCiphListParamEntry.setStatus("current")


class _TTlsSrvCiphListParamIndex_Type(Unsigned32):
    """Custom type tTlsSrvCiphListParamIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TTlsSrvCiphListParamIndex_Type.__name__ = "Unsigned32"
_TTlsSrvCiphListParamIndex_Object = MibTableColumn
tTlsSrvCiphListParamIndex = _TTlsSrvCiphListParamIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 11, 1, 1),
    _TTlsSrvCiphListParamIndex_Type()
)
tTlsSrvCiphListParamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tTlsSrvCiphListParamIndex.setStatus("current")
_TTlsSrvCiphListParamLastChgd_Type = TimeStamp
_TTlsSrvCiphListParamLastChgd_Object = MibTableColumn
tTlsSrvCiphListParamLastChgd = _TTlsSrvCiphListParamLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 11, 1, 2),
    _TTlsSrvCiphListParamLastChgd_Type()
)
tTlsSrvCiphListParamLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsSrvCiphListParamLastChgd.setStatus("current")
_TTlsSrvCiphListParamRowStatus_Type = RowStatus
_TTlsSrvCiphListParamRowStatus_Object = MibTableColumn
tTlsSrvCiphListParamRowStatus = _TTlsSrvCiphListParamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 11, 1, 3),
    _TTlsSrvCiphListParamRowStatus_Type()
)
tTlsSrvCiphListParamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTlsSrvCiphListParamRowStatus.setStatus("current")
_TTlsSrvCiphListParamSuiteCode_Type = TTlsCipherSuiteCode
_TTlsSrvCiphListParamSuiteCode_Object = MibTableColumn
tTlsSrvCiphListParamSuiteCode = _TTlsSrvCiphListParamSuiteCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 11, 1, 4),
    _TTlsSrvCiphListParamSuiteCode_Type()
)
tTlsSrvCiphListParamSuiteCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTlsSrvCiphListParamSuiteCode.setStatus("current")
_TTlsSrvProfileTable_Object = MibTable
tTlsSrvProfileTable = _TTlsSrvProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 12)
)
if mibBuilder.loadTexts:
    tTlsSrvProfileTable.setStatus("current")
_TTlsSrvProfileEntry_Object = MibTableRow
tTlsSrvProfileEntry = _TTlsSrvProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 12, 1)
)
tTlsSrvProfileEntry.setIndexNames(
    (0, "TIMETRA-TLS-MIB", "tTlsSrvProfileName"),
)
if mibBuilder.loadTexts:
    tTlsSrvProfileEntry.setStatus("current")
_TTlsSrvProfileName_Type = TNamedItem
_TTlsSrvProfileName_Object = MibTableColumn
tTlsSrvProfileName = _TTlsSrvProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 12, 1, 1),
    _TTlsSrvProfileName_Type()
)
tTlsSrvProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tTlsSrvProfileName.setStatus("current")
_TTlsSrvProfileLastChgd_Type = TimeStamp
_TTlsSrvProfileLastChgd_Object = MibTableColumn
tTlsSrvProfileLastChgd = _TTlsSrvProfileLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 12, 1, 2),
    _TTlsSrvProfileLastChgd_Type()
)
tTlsSrvProfileLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsSrvProfileLastChgd.setStatus("current")
_TTlsSrvProfileRowStatus_Type = RowStatus
_TTlsSrvProfileRowStatus_Object = MibTableColumn
tTlsSrvProfileRowStatus = _TTlsSrvProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 12, 1, 3),
    _TTlsSrvProfileRowStatus_Type()
)
tTlsSrvProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTlsSrvProfileRowStatus.setStatus("current")


class _TTlsSrvProfileAdminState_Type(TmnxAdminState):
    """Custom type tTlsSrvProfileAdminState based on TmnxAdminState"""
    defaultValue = 3


_TTlsSrvProfileAdminState_Type.__name__ = "TmnxAdminState"
_TTlsSrvProfileAdminState_Object = MibTableColumn
tTlsSrvProfileAdminState = _TTlsSrvProfileAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 12, 1, 4),
    _TTlsSrvProfileAdminState_Type()
)
tTlsSrvProfileAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTlsSrvProfileAdminState.setStatus("current")
_TTlsSrvProfileOperState_Type = TmnxOperState
_TTlsSrvProfileOperState_Object = MibTableColumn
tTlsSrvProfileOperState = _TTlsSrvProfileOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 12, 1, 5),
    _TTlsSrvProfileOperState_Type()
)
tTlsSrvProfileOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tTlsSrvProfileOperState.setStatus("current")


class _TTlsSrvProfileCiphListName_Type(TNamedItemOrEmpty):
    """Custom type tTlsSrvProfileCiphListName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TTlsSrvProfileCiphListName_Type.__name__ = "TNamedItemOrEmpty"
_TTlsSrvProfileCiphListName_Object = MibTableColumn
tTlsSrvProfileCiphListName = _TTlsSrvProfileCiphListName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 12, 1, 6),
    _TTlsSrvProfileCiphListName_Type()
)
tTlsSrvProfileCiphListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTlsSrvProfileCiphListName.setStatus("current")


class _TTlsSrvProfileCertProfile_Type(TNamedItemOrEmpty):
    """Custom type tTlsSrvProfileCertProfile based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TTlsSrvProfileCertProfile_Type.__name__ = "TNamedItemOrEmpty"
_TTlsSrvProfileCertProfile_Object = MibTableColumn
tTlsSrvProfileCertProfile = _TTlsSrvProfileCertProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 12, 1, 7),
    _TTlsSrvProfileCertProfile_Type()
)
tTlsSrvProfileCertProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTlsSrvProfileCertProfile.setStatus("current")


class _TTlsSrvProfileTrstAnchrProf_Type(TNamedItemOrEmpty):
    """Custom type tTlsSrvProfileTrstAnchrProf based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TTlsSrvProfileTrstAnchrProf_Type.__name__ = "TNamedItemOrEmpty"
_TTlsSrvProfileTrstAnchrProf_Object = MibTableColumn
tTlsSrvProfileTrstAnchrProf = _TTlsSrvProfileTrstAnchrProf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 12, 1, 8),
    _TTlsSrvProfileTrstAnchrProf_Type()
)
tTlsSrvProfileTrstAnchrProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTlsSrvProfileTrstAnchrProf.setStatus("current")


class _TTlsSrvProfileReNegotiateTimer_Type(Unsigned32):
    """Custom type tTlsSrvProfileReNegotiateTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_TTlsSrvProfileReNegotiateTimer_Type.__name__ = "Unsigned32"
_TTlsSrvProfileReNegotiateTimer_Object = MibTableColumn
tTlsSrvProfileReNegotiateTimer = _TTlsSrvProfileReNegotiateTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 12, 1, 9),
    _TTlsSrvProfileReNegotiateTimer_Type()
)
tTlsSrvProfileReNegotiateTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTlsSrvProfileReNegotiateTimer.setStatus("current")


class _TTlsSrvProfileCnListName_Type(TNamedItemOrEmpty):
    """Custom type tTlsSrvProfileCnListName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TTlsSrvProfileCnListName_Type.__name__ = "TNamedItemOrEmpty"
_TTlsSrvProfileCnListName_Object = MibTableColumn
tTlsSrvProfileCnListName = _TTlsSrvProfileCnListName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 2, 12, 1, 10),
    _TTlsSrvProfileCnListName_Type()
)
tTlsSrvProfileCnListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tTlsSrvProfileCnListName.setStatus("current")
_TmnxTlsStatistics_ObjectIdentity = ObjectIdentity
tmnxTlsStatistics = _TmnxTlsStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 3)
)
_TmnxTlsNotifyObjects_ObjectIdentity = ObjectIdentity
tmnxTlsNotifyObjects = _TmnxTlsNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 10)
)
_TmnxTlsVRtrID_Type = TmnxVRtrID
_TmnxTlsVRtrID_Object = MibScalar
tmnxTlsVRtrID = _TmnxTlsVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 10, 1),
    _TmnxTlsVRtrID_Type()
)
tmnxTlsVRtrID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTlsVRtrID.setStatus("current")


class _TmnxTlsAppId_Type(Integer32):
    """Custom type tmnxTlsAppId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("ldap", 1),
          ("grpc", 2),
          ("openflow", 3),
          ("https", 4),
          ("dialout-telemetry", 5),
          ("remote-management", 6))
    )


_TmnxTlsAppId_Type.__name__ = "Integer32"
_TmnxTlsAppId_Object = MibScalar
tmnxTlsAppId = _TmnxTlsAppId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 10, 2),
    _TmnxTlsAppId_Type()
)
tmnxTlsAppId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTlsAppId.setStatus("current")


class _TmnxTlsRole_Type(Integer32):
    """Custom type tmnxTlsRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("server", 0),
          ("client", 1))
    )


_TmnxTlsRole_Type.__name__ = "Integer32"
_TmnxTlsRole_Object = MibScalar
tmnxTlsRole = _TmnxTlsRole_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 10, 3),
    _TmnxTlsRole_Type()
)
tmnxTlsRole.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTlsRole.setStatus("current")
_TmnxTlsLocalAddrType_Type = InetAddressType
_TmnxTlsLocalAddrType_Object = MibScalar
tmnxTlsLocalAddrType = _TmnxTlsLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 10, 4),
    _TmnxTlsLocalAddrType_Type()
)
tmnxTlsLocalAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTlsLocalAddrType.setStatus("current")
_TmnxTlsLocalAddr_Type = InetAddress
_TmnxTlsLocalAddr_Object = MibScalar
tmnxTlsLocalAddr = _TmnxTlsLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 10, 5),
    _TmnxTlsLocalAddr_Type()
)
tmnxTlsLocalAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTlsLocalAddr.setStatus("current")


class _TmnxTlsLocalPort_Type(TTcpUdpPort):
    """Custom type tmnxTlsLocalPort based on TTcpUdpPort"""
    subtypeSpec = TTcpUdpPort.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxTlsLocalPort_Type.__name__ = "TTcpUdpPort"
_TmnxTlsLocalPort_Object = MibScalar
tmnxTlsLocalPort = _TmnxTlsLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 10, 6),
    _TmnxTlsLocalPort_Type()
)
tmnxTlsLocalPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTlsLocalPort.setStatus("current")
_TmnxTlsRemoteAddrType_Type = InetAddressType
_TmnxTlsRemoteAddrType_Object = MibScalar
tmnxTlsRemoteAddrType = _TmnxTlsRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 10, 7),
    _TmnxTlsRemoteAddrType_Type()
)
tmnxTlsRemoteAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTlsRemoteAddrType.setStatus("current")
_TmnxTlsRemoteAddr_Type = InetAddress
_TmnxTlsRemoteAddr_Object = MibScalar
tmnxTlsRemoteAddr = _TmnxTlsRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 10, 8),
    _TmnxTlsRemoteAddr_Type()
)
tmnxTlsRemoteAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTlsRemoteAddr.setStatus("current")


class _TmnxTlsRemotePort_Type(TTcpUdpPort):
    """Custom type tmnxTlsRemotePort based on TTcpUdpPort"""
    subtypeSpec = TTcpUdpPort.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxTlsRemotePort_Type.__name__ = "TTcpUdpPort"
_TmnxTlsRemotePort_Object = MibScalar
tmnxTlsRemotePort = _TmnxTlsRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 10, 9),
    _TmnxTlsRemotePort_Type()
)
tmnxTlsRemotePort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTlsRemotePort.setStatus("current")


class _TmnxTlsConnectionState_Type(Integer32):
    """Custom type tmnxTlsConnectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("initiating", 0),
          ("connected", 1))
    )


_TmnxTlsConnectionState_Type.__name__ = "Integer32"
_TmnxTlsConnectionState_Object = MibScalar
tmnxTlsConnectionState = _TmnxTlsConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 10, 10),
    _TmnxTlsConnectionState_Type()
)
tmnxTlsConnectionState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTlsConnectionState.setStatus("current")


class _TmnxTlsFailureReason_Type(Integer32):
    """Custom type tmnxTlsFailureReason based on Integer32"""
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
        *(("lackOfResources", 0),
          ("profileNotOperational", 1),
          ("invalidCertificate", 2),
          ("handshakeFailure", 3),
          ("badPacket", 4),
          ("renegotiationFailure", 5))
    )


_TmnxTlsFailureReason_Type.__name__ = "Integer32"
_TmnxTlsFailureReason_Object = MibScalar
tmnxTlsFailureReason = _TmnxTlsFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 10, 11),
    _TmnxTlsFailureReason_Type()
)
tmnxTlsFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTlsFailureReason.setStatus("current")
_TmnxTlsProxyAddrType_Type = InetAddressType
_TmnxTlsProxyAddrType_Object = MibScalar
tmnxTlsProxyAddrType = _TmnxTlsProxyAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 10, 12),
    _TmnxTlsProxyAddrType_Type()
)
tmnxTlsProxyAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTlsProxyAddrType.setStatus("current")
_TmnxTlsProxyAddr_Type = InetAddress
_TmnxTlsProxyAddr_Object = MibScalar
tmnxTlsProxyAddr = _TmnxTlsProxyAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 10, 13),
    _TmnxTlsProxyAddr_Type()
)
tmnxTlsProxyAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTlsProxyAddr.setStatus("current")


class _TmnxTlsProxyPort_Type(TTcpUdpPort):
    """Custom type tmnxTlsProxyPort based on TTcpUdpPort"""
    subtypeSpec = TTcpUdpPort.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_TmnxTlsProxyPort_Type.__name__ = "TTcpUdpPort"
_TmnxTlsProxyPort_Object = MibScalar
tmnxTlsProxyPort = _TmnxTlsProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 107, 10, 14),
    _TmnxTlsProxyPort_Type()
)
tmnxTlsProxyPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTlsProxyPort.setStatus("current")
_TmnxTlsNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxTlsNotifyPrefix = _TmnxTlsNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 107)
)
_TmnxTlsNotifications_ObjectIdentity = ObjectIdentity
tmnxTlsNotifications = _TmnxTlsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 107, 0)
)

# Managed Objects groups

tmnxTlsX509CertMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 107, 2, 1, 1)
)
tmnxTlsX509CertMgmtGroup.setObjects(
      *(("TIMETRA-TLS-MIB", "tTlsCertProfileTblLastChgd"),
        ("TIMETRA-TLS-MIB", "tTlsCertProfileLastChgd"),
        ("TIMETRA-TLS-MIB", "tTlsCertProfileRowStatus"),
        ("TIMETRA-TLS-MIB", "tTlsCertProfileAdminState"),
        ("TIMETRA-TLS-MIB", "tTlsCertProfileOperState"),
        ("TIMETRA-TLS-MIB", "tTlsCertProfileOperFlags"),
        ("TIMETRA-TLS-MIB", "tTlsCertProfEntryIdTblLastChgd"),
        ("TIMETRA-TLS-MIB", "tTlsCertProfEntryIdLastChgd"),
        ("TIMETRA-TLS-MIB", "tTlsCertProfEntryIdRowStatus"),
        ("TIMETRA-TLS-MIB", "tTlsCertProfEntryIdCertFile"),
        ("TIMETRA-TLS-MIB", "tTlsCertProfEntryIdKeyFile"),
        ("TIMETRA-TLS-MIB", "tTlsCertProfEntryIdCompChain"),
        ("TIMETRA-TLS-MIB", "tTlsCertProfEntryIdOperFlags"),
        ("TIMETRA-TLS-MIB", "tTlsCompChainCAProfName"),
        ("TIMETRA-TLS-MIB", "tTlsCertChainCAProfTblLastChgd"),
        ("TIMETRA-TLS-MIB", "tTlsCertChainCAProfLastChgd"),
        ("TIMETRA-TLS-MIB", "tTlsCertChainCAProfRowStatus"),
        ("TIMETRA-TLS-MIB", "tTlsTrustAnchorProfTblLastChgd"),
        ("TIMETRA-TLS-MIB", "tTlsTrustAnchorProfLastChgd"),
        ("TIMETRA-TLS-MIB", "tTlsTrustAnchorProfRowStatus"),
        ("TIMETRA-TLS-MIB", "tTlsTrustAnchorCAProfDown"),
        ("TIMETRA-TLS-MIB", "tTlsTrustAnchorsTblLastChgd"),
        ("TIMETRA-TLS-MIB", "tTlsTrustAnchorsLastChgd"),
        ("TIMETRA-TLS-MIB", "tTlsTrustAnchorsRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxTlsX509CertMgmtGroup.setStatus("current")

tmnxTlsClientMgmtInitialGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 107, 2, 1, 2)
)
tmnxTlsClientMgmtInitialGroup.setObjects(
      *(("TIMETRA-TLS-MIB", "tTlsClientCiphListTblLastChgd"),
        ("TIMETRA-TLS-MIB", "tTlsClientCiphListLastChgd"),
        ("TIMETRA-TLS-MIB", "tTlsClientCiphListRowStatus"),
        ("TIMETRA-TLS-MIB", "tTlsClntCiphListParTblLastChgd"),
        ("TIMETRA-TLS-MIB", "tTlsClntCiphListParamLastChgd"),
        ("TIMETRA-TLS-MIB", "tTlsClntCiphListParamRowStatus"),
        ("TIMETRA-TLS-MIB", "tTlsClntCiphListParamSuiteCode"),
        ("TIMETRA-TLS-MIB", "tTlsClntProfileTblLastChgd"),
        ("TIMETRA-TLS-MIB", "tTlsClntProfileLastChgd"),
        ("TIMETRA-TLS-MIB", "tTlsClntProfileRowStatus"),
        ("TIMETRA-TLS-MIB", "tTlsClntProfileAdminState"),
        ("TIMETRA-TLS-MIB", "tTlsClntProfileOperState"),
        ("TIMETRA-TLS-MIB", "tTlsClntProfileCiphListName"),
        ("TIMETRA-TLS-MIB", "tTlsClntProfileCertProfile"),
        ("TIMETRA-TLS-MIB", "tTlsClntProfileTrstAnchrProf"))
)
if mibBuilder.loadTexts:
    tmnxTlsClientMgmtInitialGroup.setStatus("current")

tmnxTlsServerMgmtGroupV15v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 107, 2, 2, 1)
)
tmnxTlsServerMgmtGroupV15v0.setObjects(
      *(("TIMETRA-TLS-MIB", "tTlsServerCiphListTblLastChgd"),
        ("TIMETRA-TLS-MIB", "tTlsServerCiphListLastChgd"),
        ("TIMETRA-TLS-MIB", "tTlsServerCiphListRowStatus"),
        ("TIMETRA-TLS-MIB", "tTlsSrvCiphListParTblLastChgd"),
        ("TIMETRA-TLS-MIB", "tTlsSrvCiphListParamLastChgd"),
        ("TIMETRA-TLS-MIB", "tTlsSrvCiphListParamRowStatus"),
        ("TIMETRA-TLS-MIB", "tTlsSrvCiphListParamSuiteCode"),
        ("TIMETRA-TLS-MIB", "tTlsSrvProfileTblLastChgd"),
        ("TIMETRA-TLS-MIB", "tTlsSrvProfileLastChgd"),
        ("TIMETRA-TLS-MIB", "tTlsSrvProfileRowStatus"),
        ("TIMETRA-TLS-MIB", "tTlsSrvProfileAdminState"),
        ("TIMETRA-TLS-MIB", "tTlsSrvProfileOperState"),
        ("TIMETRA-TLS-MIB", "tTlsSrvProfileCiphListName"),
        ("TIMETRA-TLS-MIB", "tTlsSrvProfileCertProfile"),
        ("TIMETRA-TLS-MIB", "tTlsSrvProfileTrstAnchrProf"),
        ("TIMETRA-TLS-MIB", "tTlsSrvProfileReNegotiateTimer"),
        ("TIMETRA-TLS-MIB", "tTlsSrvProfileCnListName"))
)
if mibBuilder.loadTexts:
    tmnxTlsServerMgmtGroupV15v0.setStatus("current")

tmnxTlsNotifyObjsGroupV20v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 107, 2, 2, 2)
)
tmnxTlsNotifyObjsGroupV20v0.setObjects(
      *(("TIMETRA-TLS-MIB", "tmnxTlsVRtrID"),
        ("TIMETRA-TLS-MIB", "tmnxTlsAppId"),
        ("TIMETRA-TLS-MIB", "tmnxTlsRole"),
        ("TIMETRA-TLS-MIB", "tmnxTlsLocalAddrType"),
        ("TIMETRA-TLS-MIB", "tmnxTlsLocalAddr"),
        ("TIMETRA-TLS-MIB", "tmnxTlsLocalPort"),
        ("TIMETRA-TLS-MIB", "tmnxTlsRemoteAddrType"),
        ("TIMETRA-TLS-MIB", "tmnxTlsRemoteAddr"),
        ("TIMETRA-TLS-MIB", "tmnxTlsRemotePort"),
        ("TIMETRA-TLS-MIB", "tmnxTlsFailureReason"),
        ("TIMETRA-TLS-MIB", "tmnxTlsConnectionState"),
        ("TIMETRA-TLS-MIB", "tmnxTlsProxyAddrType"),
        ("TIMETRA-TLS-MIB", "tmnxTlsProxyAddr"),
        ("TIMETRA-TLS-MIB", "tmnxTlsProxyPort"))
)
if mibBuilder.loadTexts:
    tmnxTlsNotifyObjsGroupV20v0.setStatus("current")


# Notification objects

tmnxTlsInitiateSession = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 107, 0, 1)
)
tmnxTlsInitiateSession.setObjects(
      *(("TIMETRA-TLS-MIB", "tmnxTlsVRtrID"),
        ("TIMETRA-TLS-MIB", "tmnxTlsAppId"),
        ("TIMETRA-TLS-MIB", "tmnxTlsRole"),
        ("TIMETRA-TLS-MIB", "tmnxTlsLocalAddrType"),
        ("TIMETRA-TLS-MIB", "tmnxTlsLocalAddr"),
        ("TIMETRA-TLS-MIB", "tmnxTlsLocalPort"),
        ("TIMETRA-TLS-MIB", "tmnxTlsRemoteAddrType"),
        ("TIMETRA-TLS-MIB", "tmnxTlsRemoteAddr"),
        ("TIMETRA-TLS-MIB", "tmnxTlsRemotePort"),
        ("TIMETRA-TLS-MIB", "tmnxTlsProxyAddrType"),
        ("TIMETRA-TLS-MIB", "tmnxTlsProxyAddr"),
        ("TIMETRA-TLS-MIB", "tmnxTlsProxyPort"),
        ("TIMETRA-TLS-MIB", "tmnxTlsConnectionState"))
)
if mibBuilder.loadTexts:
    tmnxTlsInitiateSession.setStatus(
        "current"
    )

tmnxTlsTermination = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 107, 0, 2)
)
tmnxTlsTermination.setObjects(
      *(("TIMETRA-TLS-MIB", "tmnxTlsVRtrID"),
        ("TIMETRA-TLS-MIB", "tmnxTlsAppId"),
        ("TIMETRA-TLS-MIB", "tmnxTlsRole"),
        ("TIMETRA-TLS-MIB", "tmnxTlsLocalAddrType"),
        ("TIMETRA-TLS-MIB", "tmnxTlsLocalAddr"),
        ("TIMETRA-TLS-MIB", "tmnxTlsLocalPort"),
        ("TIMETRA-TLS-MIB", "tmnxTlsRemoteAddrType"),
        ("TIMETRA-TLS-MIB", "tmnxTlsRemoteAddr"),
        ("TIMETRA-TLS-MIB", "tmnxTlsRemotePort"),
        ("TIMETRA-TLS-MIB", "tmnxTlsProxyAddrType"),
        ("TIMETRA-TLS-MIB", "tmnxTlsProxyAddr"),
        ("TIMETRA-TLS-MIB", "tmnxTlsProxyPort"))
)
if mibBuilder.loadTexts:
    tmnxTlsTermination.setStatus(
        "current"
    )

tmnxTlsFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 107, 0, 3)
)
tmnxTlsFailure.setObjects(
      *(("TIMETRA-TLS-MIB", "tmnxTlsVRtrID"),
        ("TIMETRA-TLS-MIB", "tmnxTlsAppId"),
        ("TIMETRA-TLS-MIB", "tmnxTlsRole"),
        ("TIMETRA-TLS-MIB", "tmnxTlsLocalAddrType"),
        ("TIMETRA-TLS-MIB", "tmnxTlsLocalAddr"),
        ("TIMETRA-TLS-MIB", "tmnxTlsLocalPort"),
        ("TIMETRA-TLS-MIB", "tmnxTlsRemoteAddrType"),
        ("TIMETRA-TLS-MIB", "tmnxTlsRemoteAddr"),
        ("TIMETRA-TLS-MIB", "tmnxTlsRemotePort"),
        ("TIMETRA-TLS-MIB", "tmnxTlsProxyAddrType"),
        ("TIMETRA-TLS-MIB", "tmnxTlsProxyAddr"),
        ("TIMETRA-TLS-MIB", "tmnxTlsProxyPort"),
        ("TIMETRA-TLS-MIB", "tmnxTlsFailureReason"))
)
if mibBuilder.loadTexts:
    tmnxTlsFailure.setStatus(
        "current"
    )


# Notifications groups

tmnxTlsNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 107, 2, 2, 3)
)
tmnxTlsNotifyGroup.setObjects(
      *(("TIMETRA-TLS-MIB", "tmnxTlsInitiateSession"),
        ("TIMETRA-TLS-MIB", "tmnxTlsTermination"),
        ("TIMETRA-TLS-MIB", "tmnxTlsFailure"))
)
if mibBuilder.loadTexts:
    tmnxTlsNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxTlsComplianceV14v1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 107, 1, 1)
)
tmnxTlsComplianceV14v1.setObjects(
      *(("TIMETRA-TLS-MIB", "tmnxTlsX509CertMgmtGroup"),
        ("TIMETRA-TLS-MIB", "tmnxTlsClientMgmtInitialGroup"))
)
if mibBuilder.loadTexts:
    tmnxTlsComplianceV14v1.setStatus(
        "current"
    )

tmnxTlsComplianceV15v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 107, 1, 2)
)
tmnxTlsComplianceV15v0.setObjects(
      *(("TIMETRA-TLS-MIB", "tmnxTlsServerMgmtGroupV15v0"),
        ("TIMETRA-TLS-MIB", "tmnxTlsNotifyObjsGroupV20v0"),
        ("TIMETRA-TLS-MIB", "tmnxTlsNotifyGroup"))
)
if mibBuilder.loadTexts:
    tmnxTlsComplianceV15v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-TLS-MIB",
    **{"TTlsCipherSuiteCode": TTlsCipherSuiteCode,
       "timetraTlsMIBModule": timetraTlsMIBModule,
       "tmnxTlsConformance": tmnxTlsConformance,
       "tmnxTlsCompliances": tmnxTlsCompliances,
       "tmnxTlsComplianceV14v1": tmnxTlsComplianceV14v1,
       "tmnxTlsComplianceV15v0": tmnxTlsComplianceV15v0,
       "tmnxTlsGroups": tmnxTlsGroups,
       "tmnxTlsV14v1Groups": tmnxTlsV14v1Groups,
       "tmnxTlsX509CertMgmtGroup": tmnxTlsX509CertMgmtGroup,
       "tmnxTlsClientMgmtInitialGroup": tmnxTlsClientMgmtInitialGroup,
       "tmnxTlsV15v0Groups": tmnxTlsV15v0Groups,
       "tmnxTlsServerMgmtGroupV15v0": tmnxTlsServerMgmtGroupV15v0,
       "tmnxTlsNotifyObjsGroupV20v0": tmnxTlsNotifyObjsGroupV20v0,
       "tmnxTlsNotifyGroup": tmnxTlsNotifyGroup,
       "tmnxTlsObjs": tmnxTlsObjs,
       "tmnxTlsScalarObjs": tmnxTlsScalarObjs,
       "tmnxTlsConfigTimeStamps": tmnxTlsConfigTimeStamps,
       "tTlsCertProfileTblLastChgd": tTlsCertProfileTblLastChgd,
       "tTlsCertProfEntryIdTblLastChgd": tTlsCertProfEntryIdTblLastChgd,
       "tTlsCertChainCAProfTblLastChgd": tTlsCertChainCAProfTblLastChgd,
       "tTlsTrustAnchorProfTblLastChgd": tTlsTrustAnchorProfTblLastChgd,
       "tTlsTrustAnchorsTblLastChgd": tTlsTrustAnchorsTblLastChgd,
       "tTlsClientCiphListTblLastChgd": tTlsClientCiphListTblLastChgd,
       "tTlsClntCiphListParTblLastChgd": tTlsClntCiphListParTblLastChgd,
       "tTlsClntProfileTblLastChgd": tTlsClntProfileTblLastChgd,
       "tTlsServerCiphListTblLastChgd": tTlsServerCiphListTblLastChgd,
       "tTlsSrvCiphListParTblLastChgd": tTlsSrvCiphListParTblLastChgd,
       "tTlsSrvProfileTblLastChgd": tTlsSrvProfileTblLastChgd,
       "tmnxTlsConfigObjs": tmnxTlsConfigObjs,
       "tTlsCertProfileTable": tTlsCertProfileTable,
       "tTlsCertProfileEntry": tTlsCertProfileEntry,
       "tTlsCertProfileName": tTlsCertProfileName,
       "tTlsCertProfileLastChgd": tTlsCertProfileLastChgd,
       "tTlsCertProfileRowStatus": tTlsCertProfileRowStatus,
       "tTlsCertProfileAdminState": tTlsCertProfileAdminState,
       "tTlsCertProfileOperState": tTlsCertProfileOperState,
       "tTlsCertProfileOperFlags": tTlsCertProfileOperFlags,
       "tTlsCertProfEntryIdTable": tTlsCertProfEntryIdTable,
       "tTlsCertProfEntryIdEntry": tTlsCertProfEntryIdEntry,
       "tTlsCertProfEntryId": tTlsCertProfEntryId,
       "tTlsCertProfEntryIdLastChgd": tTlsCertProfEntryIdLastChgd,
       "tTlsCertProfEntryIdRowStatus": tTlsCertProfEntryIdRowStatus,
       "tTlsCertProfEntryIdCertFile": tTlsCertProfEntryIdCertFile,
       "tTlsCertProfEntryIdKeyFile": tTlsCertProfEntryIdKeyFile,
       "tTlsCertProfEntryIdCompChain": tTlsCertProfEntryIdCompChain,
       "tTlsCertProfEntryIdOperFlags": tTlsCertProfEntryIdOperFlags,
       "tTlsCompChainCAProfTable": tTlsCompChainCAProfTable,
       "tTlsCompChainCAProfEntry": tTlsCompChainCAProfEntry,
       "tTlsCompChainCAProfOrder": tTlsCompChainCAProfOrder,
       "tTlsCompChainCAProfName": tTlsCompChainCAProfName,
       "tTlsCertChainCAProfTable": tTlsCertChainCAProfTable,
       "tTlsCertChainCAProfEntry": tTlsCertChainCAProfEntry,
       "tTlsCertChainCAProfName": tTlsCertChainCAProfName,
       "tTlsCertChainCAProfLastChgd": tTlsCertChainCAProfLastChgd,
       "tTlsCertChainCAProfRowStatus": tTlsCertChainCAProfRowStatus,
       "tTlsTrustAnchorProfTable": tTlsTrustAnchorProfTable,
       "tTlsTrustAnchorProfEntry": tTlsTrustAnchorProfEntry,
       "tTlsTrustAnchorProfName": tTlsTrustAnchorProfName,
       "tTlsTrustAnchorProfLastChgd": tTlsTrustAnchorProfLastChgd,
       "tTlsTrustAnchorProfRowStatus": tTlsTrustAnchorProfRowStatus,
       "tTlsTrustAnchorCAProfDown": tTlsTrustAnchorCAProfDown,
       "tTlsTrustAnchorsTable": tTlsTrustAnchorsTable,
       "tTlsTrustAnchorsEntry": tTlsTrustAnchorsEntry,
       "tTlsTrustAnchorsCAProfile": tTlsTrustAnchorsCAProfile,
       "tTlsTrustAnchorsLastChgd": tTlsTrustAnchorsLastChgd,
       "tTlsTrustAnchorsRowStatus": tTlsTrustAnchorsRowStatus,
       "tTlsClientCiphListTable": tTlsClientCiphListTable,
       "tTlsClientCiphListEntry": tTlsClientCiphListEntry,
       "tTlsClientCiphListName": tTlsClientCiphListName,
       "tTlsClientCiphListLastChgd": tTlsClientCiphListLastChgd,
       "tTlsClientCiphListRowStatus": tTlsClientCiphListRowStatus,
       "tTlsClntCiphListParamTable": tTlsClntCiphListParamTable,
       "tTlsClntCiphListParamEntry": tTlsClntCiphListParamEntry,
       "tTlsClntCiphListParamIndex": tTlsClntCiphListParamIndex,
       "tTlsClntCiphListParamLastChgd": tTlsClntCiphListParamLastChgd,
       "tTlsClntCiphListParamRowStatus": tTlsClntCiphListParamRowStatus,
       "tTlsClntCiphListParamSuiteCode": tTlsClntCiphListParamSuiteCode,
       "tTlsClntProfileTable": tTlsClntProfileTable,
       "tTlsClntProfileEntry": tTlsClntProfileEntry,
       "tTlsClntProfileName": tTlsClntProfileName,
       "tTlsClntProfileLastChgd": tTlsClntProfileLastChgd,
       "tTlsClntProfileRowStatus": tTlsClntProfileRowStatus,
       "tTlsClntProfileAdminState": tTlsClntProfileAdminState,
       "tTlsClntProfileOperState": tTlsClntProfileOperState,
       "tTlsClntProfileCiphListName": tTlsClntProfileCiphListName,
       "tTlsClntProfileCertProfile": tTlsClntProfileCertProfile,
       "tTlsClntProfileTrstAnchrProf": tTlsClntProfileTrstAnchrProf,
       "tTlsServerCiphListTable": tTlsServerCiphListTable,
       "tTlsServerCiphListEntry": tTlsServerCiphListEntry,
       "tTlsServerCiphListName": tTlsServerCiphListName,
       "tTlsServerCiphListLastChgd": tTlsServerCiphListLastChgd,
       "tTlsServerCiphListRowStatus": tTlsServerCiphListRowStatus,
       "tTlsSrvCiphListParamTable": tTlsSrvCiphListParamTable,
       "tTlsSrvCiphListParamEntry": tTlsSrvCiphListParamEntry,
       "tTlsSrvCiphListParamIndex": tTlsSrvCiphListParamIndex,
       "tTlsSrvCiphListParamLastChgd": tTlsSrvCiphListParamLastChgd,
       "tTlsSrvCiphListParamRowStatus": tTlsSrvCiphListParamRowStatus,
       "tTlsSrvCiphListParamSuiteCode": tTlsSrvCiphListParamSuiteCode,
       "tTlsSrvProfileTable": tTlsSrvProfileTable,
       "tTlsSrvProfileEntry": tTlsSrvProfileEntry,
       "tTlsSrvProfileName": tTlsSrvProfileName,
       "tTlsSrvProfileLastChgd": tTlsSrvProfileLastChgd,
       "tTlsSrvProfileRowStatus": tTlsSrvProfileRowStatus,
       "tTlsSrvProfileAdminState": tTlsSrvProfileAdminState,
       "tTlsSrvProfileOperState": tTlsSrvProfileOperState,
       "tTlsSrvProfileCiphListName": tTlsSrvProfileCiphListName,
       "tTlsSrvProfileCertProfile": tTlsSrvProfileCertProfile,
       "tTlsSrvProfileTrstAnchrProf": tTlsSrvProfileTrstAnchrProf,
       "tTlsSrvProfileReNegotiateTimer": tTlsSrvProfileReNegotiateTimer,
       "tTlsSrvProfileCnListName": tTlsSrvProfileCnListName,
       "tmnxTlsStatistics": tmnxTlsStatistics,
       "tmnxTlsNotifyObjects": tmnxTlsNotifyObjects,
       "tmnxTlsVRtrID": tmnxTlsVRtrID,
       "tmnxTlsAppId": tmnxTlsAppId,
       "tmnxTlsRole": tmnxTlsRole,
       "tmnxTlsLocalAddrType": tmnxTlsLocalAddrType,
       "tmnxTlsLocalAddr": tmnxTlsLocalAddr,
       "tmnxTlsLocalPort": tmnxTlsLocalPort,
       "tmnxTlsRemoteAddrType": tmnxTlsRemoteAddrType,
       "tmnxTlsRemoteAddr": tmnxTlsRemoteAddr,
       "tmnxTlsRemotePort": tmnxTlsRemotePort,
       "tmnxTlsConnectionState": tmnxTlsConnectionState,
       "tmnxTlsFailureReason": tmnxTlsFailureReason,
       "tmnxTlsProxyAddrType": tmnxTlsProxyAddrType,
       "tmnxTlsProxyAddr": tmnxTlsProxyAddr,
       "tmnxTlsProxyPort": tmnxTlsProxyPort,
       "tmnxTlsNotifyPrefix": tmnxTlsNotifyPrefix,
       "tmnxTlsNotifications": tmnxTlsNotifications,
       "tmnxTlsInitiateSession": tmnxTlsInitiateSession,
       "tmnxTlsTermination": tmnxTlsTermination,
       "tmnxTlsFailure": tmnxTlsFailure}
)
