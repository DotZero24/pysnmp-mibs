# SNMP MIB module (ADTRAN-GENSIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENSIP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:30:50 2025
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

(AdGenVoipTrunkName,
 AdGenVoipUserNumber) = mibBuilder.importSymbols(
    "ADTRAN-GENVOIP-MIB",
    "AdGenVoipTrunkName",
    "AdGenVoipUserNumber")

(adGenSip,
 adGenSipID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenSip",
    "adGenSipID")

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

adGenSipIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 21, 1)
)
if mibBuilder.loadTexts:
    adGenSipIdentity.setRevisions(
        ("2018-04-11 00:00",
         "2011-05-04 00:00",
         "2010-12-22 00:00",
         "2009-10-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenSipProvisioning_ObjectIdentity = ObjectIdentity
adGenSipProvisioning = _AdGenSipProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1)
)
_AdGenSipTrunkProv_ObjectIdentity = ObjectIdentity
adGenSipTrunkProv = _AdGenSipTrunkProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1)
)
_AdGenSipTrunkProvCurrentNumber_Type = Integer32
_AdGenSipTrunkProvCurrentNumber_Object = MibScalar
adGenSipTrunkProvCurrentNumber = _AdGenSipTrunkProvCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 1),
    _AdGenSipTrunkProvCurrentNumber_Type()
)
adGenSipTrunkProvCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSipTrunkProvCurrentNumber.setStatus("current")
_AdGenSipTrunkProvLastCreateError_Type = DisplayString
_AdGenSipTrunkProvLastCreateError_Object = MibScalar
adGenSipTrunkProvLastCreateError = _AdGenSipTrunkProvLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 2),
    _AdGenSipTrunkProvLastCreateError_Type()
)
adGenSipTrunkProvLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSipTrunkProvLastCreateError.setStatus("current")
_AdGenSipTrunkProvTable_Object = MibTable
adGenSipTrunkProvTable = _AdGenSipTrunkProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3)
)
if mibBuilder.loadTexts:
    adGenSipTrunkProvTable.setStatus("current")
_AdGenSipTrunkProvEntry_Object = MibTableRow
adGenSipTrunkProvEntry = _AdGenSipTrunkProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1)
)
adGenSipTrunkProvEntry.setIndexNames(
    (0, "ADTRAN-GENSIP-MIB", "adGenSipTrunkEntryIndex"),
)
if mibBuilder.loadTexts:
    adGenSipTrunkProvEntry.setStatus("current")
_AdGenSipTrunkEntryIndex_Type = AdGenVoipTrunkName
_AdGenSipTrunkEntryIndex_Object = MibTableColumn
adGenSipTrunkEntryIndex = _AdGenSipTrunkEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 1),
    _AdGenSipTrunkEntryIndex_Type()
)
adGenSipTrunkEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenSipTrunkEntryIndex.setStatus("current")
_AdGenSipTrunkRowStatus_Type = RowStatus
_AdGenSipTrunkRowStatus_Object = MibTableColumn
adGenSipTrunkRowStatus = _AdGenSipTrunkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 2),
    _AdGenSipTrunkRowStatus_Type()
)
adGenSipTrunkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkRowStatus.setStatus("current")
_AdGenSipTrunkLastErrorString_Type = DisplayString
_AdGenSipTrunkLastErrorString_Object = MibTableColumn
adGenSipTrunkLastErrorString = _AdGenSipTrunkLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 3),
    _AdGenSipTrunkLastErrorString_Type()
)
adGenSipTrunkLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSipTrunkLastErrorString.setStatus("current")
_AdGenSipTrunkSipProxyPrimary_Type = DisplayString
_AdGenSipTrunkSipProxyPrimary_Object = MibTableColumn
adGenSipTrunkSipProxyPrimary = _AdGenSipTrunkSipProxyPrimary_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 4),
    _AdGenSipTrunkSipProxyPrimary_Type()
)
adGenSipTrunkSipProxyPrimary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkSipProxyPrimary.setStatus("current")


class _AdGenSipTrunkSipProxyPrimaryUdp_Type(Integer32):
    """Custom type adGenSipTrunkSipProxyPrimaryUdp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdGenSipTrunkSipProxyPrimaryUdp_Type.__name__ = "Integer32"
_AdGenSipTrunkSipProxyPrimaryUdp_Object = MibTableColumn
adGenSipTrunkSipProxyPrimaryUdp = _AdGenSipTrunkSipProxyPrimaryUdp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 5),
    _AdGenSipTrunkSipProxyPrimaryUdp_Type()
)
adGenSipTrunkSipProxyPrimaryUdp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkSipProxyPrimaryUdp.setStatus("current")
_AdGenSipTrunkSipProxySecondary_Type = DisplayString
_AdGenSipTrunkSipProxySecondary_Object = MibTableColumn
adGenSipTrunkSipProxySecondary = _AdGenSipTrunkSipProxySecondary_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 6),
    _AdGenSipTrunkSipProxySecondary_Type()
)
adGenSipTrunkSipProxySecondary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkSipProxySecondary.setStatus("current")


class _AdGenSipTrunkSipProxySecondaryUdp_Type(Integer32):
    """Custom type adGenSipTrunkSipProxySecondaryUdp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdGenSipTrunkSipProxySecondaryUdp_Type.__name__ = "Integer32"
_AdGenSipTrunkSipProxySecondaryUdp_Object = MibTableColumn
adGenSipTrunkSipProxySecondaryUdp = _AdGenSipTrunkSipProxySecondaryUdp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 7),
    _AdGenSipTrunkSipProxySecondaryUdp_Type()
)
adGenSipTrunkSipProxySecondaryUdp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkSipProxySecondaryUdp.setStatus("current")
_AdGenSipTrunkSipOutboundProxyPrimary_Type = DisplayString
_AdGenSipTrunkSipOutboundProxyPrimary_Object = MibTableColumn
adGenSipTrunkSipOutboundProxyPrimary = _AdGenSipTrunkSipOutboundProxyPrimary_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 8),
    _AdGenSipTrunkSipOutboundProxyPrimary_Type()
)
adGenSipTrunkSipOutboundProxyPrimary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkSipOutboundProxyPrimary.setStatus("current")


class _AdGenSipTrunkSipOutboundProxyPrimaryUdp_Type(Integer32):
    """Custom type adGenSipTrunkSipOutboundProxyPrimaryUdp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdGenSipTrunkSipOutboundProxyPrimaryUdp_Type.__name__ = "Integer32"
_AdGenSipTrunkSipOutboundProxyPrimaryUdp_Object = MibTableColumn
adGenSipTrunkSipOutboundProxyPrimaryUdp = _AdGenSipTrunkSipOutboundProxyPrimaryUdp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 9),
    _AdGenSipTrunkSipOutboundProxyPrimaryUdp_Type()
)
adGenSipTrunkSipOutboundProxyPrimaryUdp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkSipOutboundProxyPrimaryUdp.setStatus("current")
_AdGenSipTrunkSipOutboundProxySecondary_Type = DisplayString
_AdGenSipTrunkSipOutboundProxySecondary_Object = MibTableColumn
adGenSipTrunkSipOutboundProxySecondary = _AdGenSipTrunkSipOutboundProxySecondary_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 10),
    _AdGenSipTrunkSipOutboundProxySecondary_Type()
)
adGenSipTrunkSipOutboundProxySecondary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkSipOutboundProxySecondary.setStatus("current")


class _AdGenSipTrunkSipOutboundProxySecondaryUdp_Type(Integer32):
    """Custom type adGenSipTrunkSipOutboundProxySecondaryUdp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdGenSipTrunkSipOutboundProxySecondaryUdp_Type.__name__ = "Integer32"
_AdGenSipTrunkSipOutboundProxySecondaryUdp_Object = MibTableColumn
adGenSipTrunkSipOutboundProxySecondaryUdp = _AdGenSipTrunkSipOutboundProxySecondaryUdp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 11),
    _AdGenSipTrunkSipOutboundProxySecondaryUdp_Type()
)
adGenSipTrunkSipOutboundProxySecondaryUdp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkSipOutboundProxySecondaryUdp.setStatus("current")


class _AdGenSipTrunkSipDomain_Type(DisplayString):
    """Custom type adGenSipTrunkSipDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_AdGenSipTrunkSipDomain_Type.__name__ = "DisplayString"
_AdGenSipTrunkSipDomain_Object = MibTableColumn
adGenSipTrunkSipDomain = _AdGenSipTrunkSipDomain_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 12),
    _AdGenSipTrunkSipDomain_Type()
)
adGenSipTrunkSipDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkSipDomain.setStatus("current")
_AdGenSipTrunkSipTrustDomain_Type = TruthValue
_AdGenSipTrunkSipTrustDomain_Object = MibTableColumn
adGenSipTrunkSipTrustDomain = _AdGenSipTrunkSipTrustDomain_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 13),
    _AdGenSipTrunkSipTrustDomain_Type()
)
adGenSipTrunkSipTrustDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkSipTrustDomain.setStatus("current")
_AdGenSipTrunkSipTrustDomainPAssertedIdReq_Type = TruthValue
_AdGenSipTrunkSipTrustDomainPAssertedIdReq_Object = MibTableColumn
adGenSipTrunkSipTrustDomainPAssertedIdReq = _AdGenSipTrunkSipTrustDomainPAssertedIdReq_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 14),
    _AdGenSipTrunkSipTrustDomainPAssertedIdReq_Type()
)
adGenSipTrunkSipTrustDomainPAssertedIdReq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkSipTrustDomainPAssertedIdReq.setStatus("current")
_AdGenSipTrunkSipAuthenticate_Type = TruthValue
_AdGenSipTrunkSipAuthenticate_Object = MibTableColumn
adGenSipTrunkSipAuthenticate = _AdGenSipTrunkSipAuthenticate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 15),
    _AdGenSipTrunkSipAuthenticate_Type()
)
adGenSipTrunkSipAuthenticate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkSipAuthenticate.setStatus("current")


class _AdGenSipTrunkSipDialStringSource_Type(Integer32):
    """Custom type adGenSipTrunkSipDialStringSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("requestUri", 1),
          ("to", 2))
    )


_AdGenSipTrunkSipDialStringSource_Type.__name__ = "Integer32"
_AdGenSipTrunkSipDialStringSource_Object = MibTableColumn
adGenSipTrunkSipDialStringSource = _AdGenSipTrunkSipDialStringSource_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 16),
    _AdGenSipTrunkSipDialStringSource_Type()
)
adGenSipTrunkSipDialStringSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkSipDialStringSource.setStatus("current")


class _AdGenSipTrunkSipKeepAliveMethod_Type(Integer32):
    """Custom type adGenSipTrunkSipKeepAliveMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("info", 2),
          ("options", 3))
    )


_AdGenSipTrunkSipKeepAliveMethod_Type.__name__ = "Integer32"
_AdGenSipTrunkSipKeepAliveMethod_Object = MibTableColumn
adGenSipTrunkSipKeepAliveMethod = _AdGenSipTrunkSipKeepAliveMethod_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 17),
    _AdGenSipTrunkSipKeepAliveMethod_Type()
)
adGenSipTrunkSipKeepAliveMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkSipKeepAliveMethod.setStatus("current")


class _AdGenSipTrunkSipKeepAliveInterval_Type(Integer32):
    """Custom type adGenSipTrunkSipKeepAliveInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_AdGenSipTrunkSipKeepAliveInterval_Type.__name__ = "Integer32"
_AdGenSipTrunkSipKeepAliveInterval_Object = MibTableColumn
adGenSipTrunkSipKeepAliveInterval = _AdGenSipTrunkSipKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 18),
    _AdGenSipTrunkSipKeepAliveInterval_Type()
)
adGenSipTrunkSipKeepAliveInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkSipKeepAliveInterval.setStatus("current")


class _AdGenSipTrunkTimerRegFailRetry_Type(Integer32):
    """Custom type adGenSipTrunkTimerRegFailRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 604800),
    )


_AdGenSipTrunkTimerRegFailRetry_Type.__name__ = "Integer32"
_AdGenSipTrunkTimerRegFailRetry_Object = MibTableColumn
adGenSipTrunkTimerRegFailRetry = _AdGenSipTrunkTimerRegFailRetry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 19),
    _AdGenSipTrunkTimerRegFailRetry_Type()
)
adGenSipTrunkTimerRegFailRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkTimerRegFailRetry.setStatus("current")


class _AdGenSipTrunkTimerRollover_Type(Integer32):
    """Custom type adGenSipTrunkTimerRollover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AdGenSipTrunkTimerRollover_Type.__name__ = "Integer32"
_AdGenSipTrunkTimerRollover_Object = MibTableColumn
adGenSipTrunkTimerRollover = _AdGenSipTrunkTimerRollover_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 20),
    _AdGenSipTrunkTimerRollover_Type()
)
adGenSipTrunkTimerRollover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkTimerRollover.setStatus("current")
_AdGenSipTrunkPrivacy_Type = TruthValue
_AdGenSipTrunkPrivacy_Object = MibTableColumn
adGenSipTrunkPrivacy = _AdGenSipTrunkPrivacy_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 21),
    _AdGenSipTrunkPrivacy_Type()
)
adGenSipTrunkPrivacy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkPrivacy.setStatus("current")
_AdGenSipTrunkGrammarRequestUriResolve_Type = TruthValue
_AdGenSipTrunkGrammarRequestUriResolve_Object = MibTableColumn
adGenSipTrunkGrammarRequestUriResolve = _AdGenSipTrunkGrammarRequestUriResolve_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 22),
    _AdGenSipTrunkGrammarRequestUriResolve_Type()
)
adGenSipTrunkGrammarRequestUriResolve.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkGrammarRequestUriResolve.setStatus("current")


class _AdGenSipTrunkGrammarRequestUriHost_Type(Integer32):
    """Custom type adGenSipTrunkGrammarRequestUriHost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sipOutboundProxy", 1),
          ("sipProxy", 2),
          ("domain", 3))
    )


_AdGenSipTrunkGrammarRequestUriHost_Type.__name__ = "Integer32"
_AdGenSipTrunkGrammarRequestUriHost_Object = MibTableColumn
adGenSipTrunkGrammarRequestUriHost = _AdGenSipTrunkGrammarRequestUriHost_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 23),
    _AdGenSipTrunkGrammarRequestUriHost_Type()
)
adGenSipTrunkGrammarRequestUriHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkGrammarRequestUriHost.setStatus("current")


class _AdGenSipTrunkGrammarFromHost_Type(Integer32):
    """Custom type adGenSipTrunkGrammarFromHost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("outboundProxy", 1),
          ("proxy", 2),
          ("domain", 3),
          ("local", 4))
    )


_AdGenSipTrunkGrammarFromHost_Type.__name__ = "Integer32"
_AdGenSipTrunkGrammarFromHost_Object = MibTableColumn
adGenSipTrunkGrammarFromHost = _AdGenSipTrunkGrammarFromHost_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 24),
    _AdGenSipTrunkGrammarFromHost_Type()
)
adGenSipTrunkGrammarFromHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkGrammarFromHost.setStatus("current")


class _AdGenSipTrunkGrammarFromUser_Type(Integer32):
    """Custom type adGenSipTrunkGrammarFromUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("domestic", 1),
          ("international", 2))
    )


_AdGenSipTrunkGrammarFromUser_Type.__name__ = "Integer32"
_AdGenSipTrunkGrammarFromUser_Object = MibTableColumn
adGenSipTrunkGrammarFromUser = _AdGenSipTrunkGrammarFromUser_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 25),
    _AdGenSipTrunkGrammarFromUser_Type()
)
adGenSipTrunkGrammarFromUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkGrammarFromUser.setStatus("current")


class _AdGenSipTrunkGrammarPAssertedIdHost_Type(Integer32):
    """Custom type adGenSipTrunkGrammarPAssertedIdHost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("outboundProxy", 1),
          ("proxy", 2),
          ("domain", 3),
          ("local", 4))
    )


_AdGenSipTrunkGrammarPAssertedIdHost_Type.__name__ = "Integer32"
_AdGenSipTrunkGrammarPAssertedIdHost_Object = MibTableColumn
adGenSipTrunkGrammarPAssertedIdHost = _AdGenSipTrunkGrammarPAssertedIdHost_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 26),
    _AdGenSipTrunkGrammarPAssertedIdHost_Type()
)
adGenSipTrunkGrammarPAssertedIdHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkGrammarPAssertedIdHost.setStatus("current")


class _AdGenSipTrunkGrammarToHost_Type(Integer32):
    """Custom type adGenSipTrunkGrammarToHost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("server", 1),
          ("domain", 2))
    )


_AdGenSipTrunkGrammarToHost_Type.__name__ = "Integer32"
_AdGenSipTrunkGrammarToHost_Object = MibTableColumn
adGenSipTrunkGrammarToHost = _AdGenSipTrunkGrammarToHost_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 27),
    _AdGenSipTrunkGrammarToHost_Type()
)
adGenSipTrunkGrammarToHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkGrammarToHost.setStatus("current")
_AdGenSipTrunkGrammarAlertInfoUrl_Type = DisplayString
_AdGenSipTrunkGrammarAlertInfoUrl_Object = MibTableColumn
adGenSipTrunkGrammarAlertInfoUrl = _AdGenSipTrunkGrammarAlertInfoUrl_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 28),
    _AdGenSipTrunkGrammarAlertInfoUrl_Type()
)
adGenSipTrunkGrammarAlertInfoUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkGrammarAlertInfoUrl.setStatus("current")
_AdGenSipTrunkGrammarSupported100Rel_Type = TruthValue
_AdGenSipTrunkGrammarSupported100Rel_Object = MibTableColumn
adGenSipTrunkGrammarSupported100Rel = _AdGenSipTrunkGrammarSupported100Rel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 29),
    _AdGenSipTrunkGrammarSupported100Rel_Type()
)
adGenSipTrunkGrammarSupported100Rel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkGrammarSupported100Rel.setStatus("current")
_AdGenSipTrunkGrammarProxyRequirePrivacy_Type = TruthValue
_AdGenSipTrunkGrammarProxyRequirePrivacy_Object = MibTableColumn
adGenSipTrunkGrammarProxyRequirePrivacy = _AdGenSipTrunkGrammarProxyRequirePrivacy_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 30),
    _AdGenSipTrunkGrammarProxyRequirePrivacy_Type()
)
adGenSipTrunkGrammarProxyRequirePrivacy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkGrammarProxyRequirePrivacy.setStatus("current")
_AdGenSipTrunkGrammarRequire100rel_Type = TruthValue
_AdGenSipTrunkGrammarRequire100rel_Object = MibTableColumn
adGenSipTrunkGrammarRequire100rel = _AdGenSipTrunkGrammarRequire100rel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 31),
    _AdGenSipTrunkGrammarRequire100rel_Type()
)
adGenSipTrunkGrammarRequire100rel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkGrammarRequire100rel.setStatus("current")


class _AdGenSipTrunkGrammarUserAgent_Type(DisplayString):
    """Custom type adGenSipTrunkGrammarUserAgent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AdGenSipTrunkGrammarUserAgent_Type.__name__ = "DisplayString"
_AdGenSipTrunkGrammarUserAgent_Object = MibTableColumn
adGenSipTrunkGrammarUserAgent = _AdGenSipTrunkGrammarUserAgent_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 32),
    _AdGenSipTrunkGrammarUserAgent_Type()
)
adGenSipTrunkGrammarUserAgent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkGrammarUserAgent.setStatus("current")


class _AdGenSipTrunkGrammarSdpHold_Type(Integer32):
    """Custom type adGenSipTrunkGrammarSdpHold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rfc2543", 1),
          ("rfc3264", 2))
    )


_AdGenSipTrunkGrammarSdpHold_Type.__name__ = "Integer32"
_AdGenSipTrunkGrammarSdpHold_Object = MibTableColumn
adGenSipTrunkGrammarSdpHold = _AdGenSipTrunkGrammarSdpHold_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 33),
    _AdGenSipTrunkGrammarSdpHold_Type()
)
adGenSipTrunkGrammarSdpHold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkGrammarSdpHold.setStatus("current")
_AdGenSipTrunkSipRegistrarPrimary_Type = DisplayString
_AdGenSipTrunkSipRegistrarPrimary_Object = MibTableColumn
adGenSipTrunkSipRegistrarPrimary = _AdGenSipTrunkSipRegistrarPrimary_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 34),
    _AdGenSipTrunkSipRegistrarPrimary_Type()
)
adGenSipTrunkSipRegistrarPrimary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkSipRegistrarPrimary.setStatus("current")


class _AdGenSipTrunkSipRegistrarPrimaryUdp_Type(Integer32):
    """Custom type adGenSipTrunkSipRegistrarPrimaryUdp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdGenSipTrunkSipRegistrarPrimaryUdp_Type.__name__ = "Integer32"
_AdGenSipTrunkSipRegistrarPrimaryUdp_Object = MibTableColumn
adGenSipTrunkSipRegistrarPrimaryUdp = _AdGenSipTrunkSipRegistrarPrimaryUdp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 35),
    _AdGenSipTrunkSipRegistrarPrimaryUdp_Type()
)
adGenSipTrunkSipRegistrarPrimaryUdp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkSipRegistrarPrimaryUdp.setStatus("current")
_AdGenSipTrunkSipRegistrarSecondary_Type = DisplayString
_AdGenSipTrunkSipRegistrarSecondary_Object = MibTableColumn
adGenSipTrunkSipRegistrarSecondary = _AdGenSipTrunkSipRegistrarSecondary_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 36),
    _AdGenSipTrunkSipRegistrarSecondary_Type()
)
adGenSipTrunkSipRegistrarSecondary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkSipRegistrarSecondary.setStatus("current")


class _AdGenSipTrunkSipRegistrarSecondaryUdp_Type(Integer32):
    """Custom type adGenSipTrunkSipRegistrarSecondaryUdp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdGenSipTrunkSipRegistrarSecondaryUdp_Type.__name__ = "Integer32"
_AdGenSipTrunkSipRegistrarSecondaryUdp_Object = MibTableColumn
adGenSipTrunkSipRegistrarSecondaryUdp = _AdGenSipTrunkSipRegistrarSecondaryUdp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 37),
    _AdGenSipTrunkSipRegistrarSecondaryUdp_Type()
)
adGenSipTrunkSipRegistrarSecondaryUdp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkSipRegistrarSecondaryUdp.setStatus("current")


class _AdGenSipTrunkSipRegistrarThresholdType_Type(Integer32):
    """Custom type adGenSipTrunkSipRegistrarThresholdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("percentage", 1),
          ("absolute", 2))
    )


_AdGenSipTrunkSipRegistrarThresholdType_Type.__name__ = "Integer32"
_AdGenSipTrunkSipRegistrarThresholdType_Object = MibTableColumn
adGenSipTrunkSipRegistrarThresholdType = _AdGenSipTrunkSipRegistrarThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 38),
    _AdGenSipTrunkSipRegistrarThresholdType_Type()
)
adGenSipTrunkSipRegistrarThresholdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkSipRegistrarThresholdType.setStatus("current")


class _AdGenSipTrunkSipRegistrarThresholdValue_Type(Integer32):
    """Custom type adGenSipTrunkSipRegistrarThresholdValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_AdGenSipTrunkSipRegistrarThresholdValue_Type.__name__ = "Integer32"
_AdGenSipTrunkSipRegistrarThresholdValue_Object = MibTableColumn
adGenSipTrunkSipRegistrarThresholdValue = _AdGenSipTrunkSipRegistrarThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 39),
    _AdGenSipTrunkSipRegistrarThresholdValue_Type()
)
adGenSipTrunkSipRegistrarThresholdValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkSipRegistrarThresholdValue.setStatus("current")


class _AdGenSipTrunkSipRegistrarMaxConcurrentReg_Type(Integer32):
    """Custom type adGenSipTrunkSipRegistrarMaxConcurrentReg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AdGenSipTrunkSipRegistrarMaxConcurrentReg_Type.__name__ = "Integer32"
_AdGenSipTrunkSipRegistrarMaxConcurrentReg_Object = MibTableColumn
adGenSipTrunkSipRegistrarMaxConcurrentReg = _AdGenSipTrunkSipRegistrarMaxConcurrentReg_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 40),
    _AdGenSipTrunkSipRegistrarMaxConcurrentReg_Type()
)
adGenSipTrunkSipRegistrarMaxConcurrentReg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkSipRegistrarMaxConcurrentReg.setStatus("current")


class _AdGenSipTrunkSipRegistrarExpireTime_Type(Integer32):
    """Custom type adGenSipTrunkSipRegistrarExpireTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AdGenSipTrunkSipRegistrarExpireTime_Type.__name__ = "Integer32"
_AdGenSipTrunkSipRegistrarExpireTime_Object = MibTableColumn
adGenSipTrunkSipRegistrarExpireTime = _AdGenSipTrunkSipRegistrarExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 41),
    _AdGenSipTrunkSipRegistrarExpireTime_Type()
)
adGenSipTrunkSipRegistrarExpireTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkSipRegistrarExpireTime.setStatus("current")
_AdGenSipTrunkSipRegistrarRequireExpires_Type = TruthValue
_AdGenSipTrunkSipRegistrarRequireExpires_Object = MibTableColumn
adGenSipTrunkSipRegistrarRequireExpires = _AdGenSipTrunkSipRegistrarRequireExpires_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 42),
    _AdGenSipTrunkSipRegistrarRequireExpires_Type()
)
adGenSipTrunkSipRegistrarRequireExpires.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkSipRegistrarRequireExpires.setStatus("current")


class _AdGenSipTrunkSipDscp_Type(Integer32):
    """Custom type adGenSipTrunkSipDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AdGenSipTrunkSipDscp_Type.__name__ = "Integer32"
_AdGenSipTrunkSipDscp_Object = MibTableColumn
adGenSipTrunkSipDscp = _AdGenSipTrunkSipDscp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 43),
    _AdGenSipTrunkSipDscp_Type()
)
adGenSipTrunkSipDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkSipDscp.setStatus("current")


class _AdGenSipTrunkRtpDscp_Type(Integer32):
    """Custom type adGenSipTrunkRtpDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AdGenSipTrunkRtpDscp_Type.__name__ = "Integer32"
_AdGenSipTrunkRtpDscp_Object = MibTableColumn
adGenSipTrunkRtpDscp = _AdGenSipTrunkRtpDscp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 44),
    _AdGenSipTrunkRtpDscp_Type()
)
adGenSipTrunkRtpDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkRtpDscp.setStatus("current")


class _AdGenSipTrunkGrammarAddressScheme_Type(Integer32):
    """Custom type adGenSipTrunkGrammarAddressScheme based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sipUri", 1),
          ("telUri", 2))
    )


_AdGenSipTrunkGrammarAddressScheme_Type.__name__ = "Integer32"
_AdGenSipTrunkGrammarAddressScheme_Object = MibTableColumn
adGenSipTrunkGrammarAddressScheme = _AdGenSipTrunkGrammarAddressScheme_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 1, 3, 1, 45),
    _AdGenSipTrunkGrammarAddressScheme_Type()
)
adGenSipTrunkGrammarAddressScheme.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipTrunkGrammarAddressScheme.setStatus("current")
_AdGenSipIdentityProv_ObjectIdentity = ObjectIdentity
adGenSipIdentityProv = _AdGenSipIdentityProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 2)
)
_AdGenSipIdentityProvCurrentNumber_Type = Integer32
_AdGenSipIdentityProvCurrentNumber_Object = MibScalar
adGenSipIdentityProvCurrentNumber = _AdGenSipIdentityProvCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 2, 1),
    _AdGenSipIdentityProvCurrentNumber_Type()
)
adGenSipIdentityProvCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSipIdentityProvCurrentNumber.setStatus("current")
_AdGenSipIdentityProvLastCreateError_Type = DisplayString
_AdGenSipIdentityProvLastCreateError_Object = MibScalar
adGenSipIdentityProvLastCreateError = _AdGenSipIdentityProvLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 2, 2),
    _AdGenSipIdentityProvLastCreateError_Type()
)
adGenSipIdentityProvLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSipIdentityProvLastCreateError.setStatus("current")
_AdGenSipIdentityProvTable_Object = MibTable
adGenSipIdentityProvTable = _AdGenSipIdentityProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 2, 3)
)
if mibBuilder.loadTexts:
    adGenSipIdentityProvTable.setStatus("current")
_AdGenSipIdentityProvEntry_Object = MibTableRow
adGenSipIdentityProvEntry = _AdGenSipIdentityProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 2, 3, 1)
)
adGenSipIdentityProvEntry.setIndexNames(
    (0, "ADTRAN-GENSIP-MIB", "adGenSipIdentityUserIndex"),
    (0, "ADTRAN-GENSIP-MIB", "adGenSipIdentityTrunkIndex"),
    (1, "ADTRAN-GENSIP-MIB", "adGenSipIdentityEntryIndex"),
)
if mibBuilder.loadTexts:
    adGenSipIdentityProvEntry.setStatus("current")
_AdGenSipIdentityUserIndex_Type = AdGenVoipUserNumber
_AdGenSipIdentityUserIndex_Object = MibTableColumn
adGenSipIdentityUserIndex = _AdGenSipIdentityUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 2, 3, 1, 1),
    _AdGenSipIdentityUserIndex_Type()
)
adGenSipIdentityUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenSipIdentityUserIndex.setStatus("current")
_AdGenSipIdentityTrunkIndex_Type = AdGenVoipTrunkName
_AdGenSipIdentityTrunkIndex_Object = MibTableColumn
adGenSipIdentityTrunkIndex = _AdGenSipIdentityTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 2, 3, 1, 2),
    _AdGenSipIdentityTrunkIndex_Type()
)
adGenSipIdentityTrunkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenSipIdentityTrunkIndex.setStatus("current")


class _AdGenSipIdentityEntryIndex_Type(DisplayString):
    """Custom type adGenSipIdentityEntryIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_AdGenSipIdentityEntryIndex_Type.__name__ = "DisplayString"
_AdGenSipIdentityEntryIndex_Object = MibTableColumn
adGenSipIdentityEntryIndex = _AdGenSipIdentityEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 2, 3, 1, 3),
    _AdGenSipIdentityEntryIndex_Type()
)
adGenSipIdentityEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenSipIdentityEntryIndex.setStatus("current")
_AdGenSipIdentityRowStatus_Type = RowStatus
_AdGenSipIdentityRowStatus_Object = MibTableColumn
adGenSipIdentityRowStatus = _AdGenSipIdentityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 2, 3, 1, 4),
    _AdGenSipIdentityRowStatus_Type()
)
adGenSipIdentityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipIdentityRowStatus.setStatus("current")
_AdGenSipIdentityLastErrorString_Type = DisplayString
_AdGenSipIdentityLastErrorString_Object = MibTableColumn
adGenSipIdentityLastErrorString = _AdGenSipIdentityLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 2, 3, 1, 5),
    _AdGenSipIdentityLastErrorString_Type()
)
adGenSipIdentityLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSipIdentityLastErrorString.setStatus("current")
_AdGenSipIdentityRegister_Type = TruthValue
_AdGenSipIdentityRegister_Object = MibTableColumn
adGenSipIdentityRegister = _AdGenSipIdentityRegister_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 2, 3, 1, 6),
    _AdGenSipIdentityRegister_Type()
)
adGenSipIdentityRegister.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipIdentityRegister.setStatus("current")


class _AdGenSipIdentityAuthName_Type(DisplayString):
    """Custom type adGenSipIdentityAuthName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_AdGenSipIdentityAuthName_Type.__name__ = "DisplayString"
_AdGenSipIdentityAuthName_Object = MibTableColumn
adGenSipIdentityAuthName = _AdGenSipIdentityAuthName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 2, 3, 1, 7),
    _AdGenSipIdentityAuthName_Type()
)
adGenSipIdentityAuthName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipIdentityAuthName.setStatus("current")


class _AdGenSipIdentityPassword_Type(DisplayString):
    """Custom type adGenSipIdentityPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_AdGenSipIdentityPassword_Type.__name__ = "DisplayString"
_AdGenSipIdentityPassword_Object = MibTableColumn
adGenSipIdentityPassword = _AdGenSipIdentityPassword_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 1, 2, 3, 1, 8),
    _AdGenSipIdentityPassword_Type()
)
adGenSipIdentityPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSipIdentityPassword.setStatus("current")
_AdGenSipMgmnt_ObjectIdentity = ObjectIdentity
adGenSipMgmnt = _AdGenSipMgmnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 2)
)
_AdGenSipMgmntActions_ObjectIdentity = ObjectIdentity
adGenSipMgmntActions = _AdGenSipMgmntActions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 2, 1)
)
_AdGenSipMgmntTable_Object = MibTable
adGenSipMgmntTable = _AdGenSipMgmntTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 2, 1, 1)
)
if mibBuilder.loadTexts:
    adGenSipMgmntTable.setStatus("current")
_AdGenSipMgmntEntry_Object = MibTableRow
adGenSipMgmntEntry = _AdGenSipMgmntEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 2, 1, 1, 1)
)
adGenSipMgmntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENSIP-MIB", "adGenSipMgmntTrunkIndex"),
    (1, "ADTRAN-GENSIP-MIB", "adGenSipMgmntIdentityIndex"),
)
if mibBuilder.loadTexts:
    adGenSipMgmntEntry.setStatus("current")
_AdGenSipMgmntTrunkIndex_Type = AdGenVoipTrunkName
_AdGenSipMgmntTrunkIndex_Object = MibTableColumn
adGenSipMgmntTrunkIndex = _AdGenSipMgmntTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 2, 1, 1, 1, 1),
    _AdGenSipMgmntTrunkIndex_Type()
)
adGenSipMgmntTrunkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenSipMgmntTrunkIndex.setStatus("current")


class _AdGenSipMgmntIdentityIndex_Type(DisplayString):
    """Custom type adGenSipMgmntIdentityIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_AdGenSipMgmntIdentityIndex_Type.__name__ = "DisplayString"
_AdGenSipMgmntIdentityIndex_Object = MibTableColumn
adGenSipMgmntIdentityIndex = _AdGenSipMgmntIdentityIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 2, 1, 1, 1, 2),
    _AdGenSipMgmntIdentityIndex_Type()
)
adGenSipMgmntIdentityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenSipMgmntIdentityIndex.setStatus("current")


class _AdGenSipMgmntForceReg_Type(Integer32):
    """Custom type adGenSipMgmntForceReg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("force", 1)
    )


_AdGenSipMgmntForceReg_Type.__name__ = "Integer32"
_AdGenSipMgmntForceReg_Object = MibTableColumn
adGenSipMgmntForceReg = _AdGenSipMgmntForceReg_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 2, 1, 1, 1, 3),
    _AdGenSipMgmntForceReg_Type()
)
adGenSipMgmntForceReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSipMgmntForceReg.setStatus("current")


class _AdGenSipMgmntClearReg_Type(Integer32):
    """Custom type adGenSipMgmntClearReg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AdGenSipMgmntClearReg_Type.__name__ = "Integer32"
_AdGenSipMgmntClearReg_Object = MibTableColumn
adGenSipMgmntClearReg = _AdGenSipMgmntClearReg_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 2, 1, 1, 1, 4),
    _AdGenSipMgmntClearReg_Type()
)
adGenSipMgmntClearReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSipMgmntClearReg.setStatus("current")
_AdGenSipStatus_ObjectIdentity = ObjectIdentity
adGenSipStatus = _AdGenSipStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 3)
)
_AdGenSipStatusRegistration_ObjectIdentity = ObjectIdentity
adGenSipStatusRegistration = _AdGenSipStatusRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 3, 1)
)
_AdGenSipStatusRegistrationTable_Object = MibTable
adGenSipStatusRegistrationTable = _AdGenSipStatusRegistrationTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 3, 1, 1)
)
if mibBuilder.loadTexts:
    adGenSipStatusRegistrationTable.setStatus("current")
_AdGenSipStatusRegistrationEntry_Object = MibTableRow
adGenSipStatusRegistrationEntry = _AdGenSipStatusRegistrationEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 3, 1, 1, 1)
)
adGenSipStatusRegistrationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENSIP-MIB", "adGenSipRegistrationTrunkIndex"),
    (1, "ADTRAN-GENSIP-MIB", "adGenSipRegistrationIdentityIndex"),
)
if mibBuilder.loadTexts:
    adGenSipStatusRegistrationEntry.setStatus("current")
_AdGenSipRegistrationTrunkIndex_Type = AdGenVoipTrunkName
_AdGenSipRegistrationTrunkIndex_Object = MibTableColumn
adGenSipRegistrationTrunkIndex = _AdGenSipRegistrationTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 3, 1, 1, 1, 1),
    _AdGenSipRegistrationTrunkIndex_Type()
)
adGenSipRegistrationTrunkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenSipRegistrationTrunkIndex.setStatus("current")


class _AdGenSipRegistrationIdentityIndex_Type(DisplayString):
    """Custom type adGenSipRegistrationIdentityIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_AdGenSipRegistrationIdentityIndex_Type.__name__ = "DisplayString"
_AdGenSipRegistrationIdentityIndex_Object = MibTableColumn
adGenSipRegistrationIdentityIndex = _AdGenSipRegistrationIdentityIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 3, 1, 1, 1, 2),
    _AdGenSipRegistrationIdentityIndex_Type()
)
adGenSipRegistrationIdentityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenSipRegistrationIdentityIndex.setStatus("current")


class _AdGenSipStatusRegistrationStatus_Type(Integer32):
    """Custom type adGenSipStatusRegistrationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AdGenSipStatusRegistrationStatus_Type.__name__ = "Integer32"
_AdGenSipStatusRegistrationStatus_Object = MibTableColumn
adGenSipStatusRegistrationStatus = _AdGenSipStatusRegistrationStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 3, 1, 1, 1, 3),
    _AdGenSipStatusRegistrationStatus_Type()
)
adGenSipStatusRegistrationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSipStatusRegistrationStatus.setStatus("current")
_AdGenSipStatusRegistrationGrant_Type = Unsigned32
_AdGenSipStatusRegistrationGrant_Object = MibTableColumn
adGenSipStatusRegistrationGrant = _AdGenSipStatusRegistrationGrant_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 3, 1, 1, 1, 4),
    _AdGenSipStatusRegistrationGrant_Type()
)
adGenSipStatusRegistrationGrant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSipStatusRegistrationGrant.setStatus("current")
_AdGenSipStatusRegistrationExpires_Type = Unsigned32
_AdGenSipStatusRegistrationExpires_Object = MibTableColumn
adGenSipStatusRegistrationExpires = _AdGenSipStatusRegistrationExpires_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 3, 1, 1, 1, 5),
    _AdGenSipStatusRegistrationExpires_Type()
)
adGenSipStatusRegistrationExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSipStatusRegistrationExpires.setStatus("current")
_AdGenSipStatusRegistrationSuccess_Type = Unsigned32
_AdGenSipStatusRegistrationSuccess_Object = MibTableColumn
adGenSipStatusRegistrationSuccess = _AdGenSipStatusRegistrationSuccess_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 3, 1, 1, 1, 6),
    _AdGenSipStatusRegistrationSuccess_Type()
)
adGenSipStatusRegistrationSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSipStatusRegistrationSuccess.setStatus("current")
_AdGenSipStatusRegistrationFail_Type = Unsigned32
_AdGenSipStatusRegistrationFail_Object = MibTableColumn
adGenSipStatusRegistrationFail = _AdGenSipStatusRegistrationFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 3, 1, 1, 1, 7),
    _AdGenSipStatusRegistrationFail_Type()
)
adGenSipStatusRegistrationFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSipStatusRegistrationFail.setStatus("current")
_AdGenSipStatusRegistrationRequests_Type = Unsigned32
_AdGenSipStatusRegistrationRequests_Object = MibTableColumn
adGenSipStatusRegistrationRequests = _AdGenSipStatusRegistrationRequests_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 3, 1, 1, 1, 8),
    _AdGenSipStatusRegistrationRequests_Type()
)
adGenSipStatusRegistrationRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSipStatusRegistrationRequests.setStatus("current")
_AdGenSipStatusRegistrationChallenges_Type = Unsigned32
_AdGenSipStatusRegistrationChallenges_Object = MibTableColumn
adGenSipStatusRegistrationChallenges = _AdGenSipStatusRegistrationChallenges_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 3, 1, 1, 1, 9),
    _AdGenSipStatusRegistrationChallenges_Type()
)
adGenSipStatusRegistrationChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSipStatusRegistrationChallenges.setStatus("current")
_AdGenSipStatusRegistrationRollovers_Type = Unsigned32
_AdGenSipStatusRegistrationRollovers_Object = MibTableColumn
adGenSipStatusRegistrationRollovers = _AdGenSipStatusRegistrationRollovers_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 21, 3, 1, 1, 1, 10),
    _AdGenSipStatusRegistrationRollovers_Type()
)
adGenSipStatusRegistrationRollovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSipStatusRegistrationRollovers.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENSIP-MIB",
    **{"adGenSipProvisioning": adGenSipProvisioning,
       "adGenSipTrunkProv": adGenSipTrunkProv,
       "adGenSipTrunkProvCurrentNumber": adGenSipTrunkProvCurrentNumber,
       "adGenSipTrunkProvLastCreateError": adGenSipTrunkProvLastCreateError,
       "adGenSipTrunkProvTable": adGenSipTrunkProvTable,
       "adGenSipTrunkProvEntry": adGenSipTrunkProvEntry,
       "adGenSipTrunkEntryIndex": adGenSipTrunkEntryIndex,
       "adGenSipTrunkRowStatus": adGenSipTrunkRowStatus,
       "adGenSipTrunkLastErrorString": adGenSipTrunkLastErrorString,
       "adGenSipTrunkSipProxyPrimary": adGenSipTrunkSipProxyPrimary,
       "adGenSipTrunkSipProxyPrimaryUdp": adGenSipTrunkSipProxyPrimaryUdp,
       "adGenSipTrunkSipProxySecondary": adGenSipTrunkSipProxySecondary,
       "adGenSipTrunkSipProxySecondaryUdp": adGenSipTrunkSipProxySecondaryUdp,
       "adGenSipTrunkSipOutboundProxyPrimary": adGenSipTrunkSipOutboundProxyPrimary,
       "adGenSipTrunkSipOutboundProxyPrimaryUdp": adGenSipTrunkSipOutboundProxyPrimaryUdp,
       "adGenSipTrunkSipOutboundProxySecondary": adGenSipTrunkSipOutboundProxySecondary,
       "adGenSipTrunkSipOutboundProxySecondaryUdp": adGenSipTrunkSipOutboundProxySecondaryUdp,
       "adGenSipTrunkSipDomain": adGenSipTrunkSipDomain,
       "adGenSipTrunkSipTrustDomain": adGenSipTrunkSipTrustDomain,
       "adGenSipTrunkSipTrustDomainPAssertedIdReq": adGenSipTrunkSipTrustDomainPAssertedIdReq,
       "adGenSipTrunkSipAuthenticate": adGenSipTrunkSipAuthenticate,
       "adGenSipTrunkSipDialStringSource": adGenSipTrunkSipDialStringSource,
       "adGenSipTrunkSipKeepAliveMethod": adGenSipTrunkSipKeepAliveMethod,
       "adGenSipTrunkSipKeepAliveInterval": adGenSipTrunkSipKeepAliveInterval,
       "adGenSipTrunkTimerRegFailRetry": adGenSipTrunkTimerRegFailRetry,
       "adGenSipTrunkTimerRollover": adGenSipTrunkTimerRollover,
       "adGenSipTrunkPrivacy": adGenSipTrunkPrivacy,
       "adGenSipTrunkGrammarRequestUriResolve": adGenSipTrunkGrammarRequestUriResolve,
       "adGenSipTrunkGrammarRequestUriHost": adGenSipTrunkGrammarRequestUriHost,
       "adGenSipTrunkGrammarFromHost": adGenSipTrunkGrammarFromHost,
       "adGenSipTrunkGrammarFromUser": adGenSipTrunkGrammarFromUser,
       "adGenSipTrunkGrammarPAssertedIdHost": adGenSipTrunkGrammarPAssertedIdHost,
       "adGenSipTrunkGrammarToHost": adGenSipTrunkGrammarToHost,
       "adGenSipTrunkGrammarAlertInfoUrl": adGenSipTrunkGrammarAlertInfoUrl,
       "adGenSipTrunkGrammarSupported100Rel": adGenSipTrunkGrammarSupported100Rel,
       "adGenSipTrunkGrammarProxyRequirePrivacy": adGenSipTrunkGrammarProxyRequirePrivacy,
       "adGenSipTrunkGrammarRequire100rel": adGenSipTrunkGrammarRequire100rel,
       "adGenSipTrunkGrammarUserAgent": adGenSipTrunkGrammarUserAgent,
       "adGenSipTrunkGrammarSdpHold": adGenSipTrunkGrammarSdpHold,
       "adGenSipTrunkSipRegistrarPrimary": adGenSipTrunkSipRegistrarPrimary,
       "adGenSipTrunkSipRegistrarPrimaryUdp": adGenSipTrunkSipRegistrarPrimaryUdp,
       "adGenSipTrunkSipRegistrarSecondary": adGenSipTrunkSipRegistrarSecondary,
       "adGenSipTrunkSipRegistrarSecondaryUdp": adGenSipTrunkSipRegistrarSecondaryUdp,
       "adGenSipTrunkSipRegistrarThresholdType": adGenSipTrunkSipRegistrarThresholdType,
       "adGenSipTrunkSipRegistrarThresholdValue": adGenSipTrunkSipRegistrarThresholdValue,
       "adGenSipTrunkSipRegistrarMaxConcurrentReg": adGenSipTrunkSipRegistrarMaxConcurrentReg,
       "adGenSipTrunkSipRegistrarExpireTime": adGenSipTrunkSipRegistrarExpireTime,
       "adGenSipTrunkSipRegistrarRequireExpires": adGenSipTrunkSipRegistrarRequireExpires,
       "adGenSipTrunkSipDscp": adGenSipTrunkSipDscp,
       "adGenSipTrunkRtpDscp": adGenSipTrunkRtpDscp,
       "adGenSipTrunkGrammarAddressScheme": adGenSipTrunkGrammarAddressScheme,
       "adGenSipIdentityProv": adGenSipIdentityProv,
       "adGenSipIdentityProvCurrentNumber": adGenSipIdentityProvCurrentNumber,
       "adGenSipIdentityProvLastCreateError": adGenSipIdentityProvLastCreateError,
       "adGenSipIdentityProvTable": adGenSipIdentityProvTable,
       "adGenSipIdentityProvEntry": adGenSipIdentityProvEntry,
       "adGenSipIdentityUserIndex": adGenSipIdentityUserIndex,
       "adGenSipIdentityTrunkIndex": adGenSipIdentityTrunkIndex,
       "adGenSipIdentityEntryIndex": adGenSipIdentityEntryIndex,
       "adGenSipIdentityRowStatus": adGenSipIdentityRowStatus,
       "adGenSipIdentityLastErrorString": adGenSipIdentityLastErrorString,
       "adGenSipIdentityRegister": adGenSipIdentityRegister,
       "adGenSipIdentityAuthName": adGenSipIdentityAuthName,
       "adGenSipIdentityPassword": adGenSipIdentityPassword,
       "adGenSipMgmnt": adGenSipMgmnt,
       "adGenSipMgmntActions": adGenSipMgmntActions,
       "adGenSipMgmntTable": adGenSipMgmntTable,
       "adGenSipMgmntEntry": adGenSipMgmntEntry,
       "adGenSipMgmntTrunkIndex": adGenSipMgmntTrunkIndex,
       "adGenSipMgmntIdentityIndex": adGenSipMgmntIdentityIndex,
       "adGenSipMgmntForceReg": adGenSipMgmntForceReg,
       "adGenSipMgmntClearReg": adGenSipMgmntClearReg,
       "adGenSipStatus": adGenSipStatus,
       "adGenSipStatusRegistration": adGenSipStatusRegistration,
       "adGenSipStatusRegistrationTable": adGenSipStatusRegistrationTable,
       "adGenSipStatusRegistrationEntry": adGenSipStatusRegistrationEntry,
       "adGenSipRegistrationTrunkIndex": adGenSipRegistrationTrunkIndex,
       "adGenSipRegistrationIdentityIndex": adGenSipRegistrationIdentityIndex,
       "adGenSipStatusRegistrationStatus": adGenSipStatusRegistrationStatus,
       "adGenSipStatusRegistrationGrant": adGenSipStatusRegistrationGrant,
       "adGenSipStatusRegistrationExpires": adGenSipStatusRegistrationExpires,
       "adGenSipStatusRegistrationSuccess": adGenSipStatusRegistrationSuccess,
       "adGenSipStatusRegistrationFail": adGenSipStatusRegistrationFail,
       "adGenSipStatusRegistrationRequests": adGenSipStatusRegistrationRequests,
       "adGenSipStatusRegistrationChallenges": adGenSipStatusRegistrationChallenges,
       "adGenSipStatusRegistrationRollovers": adGenSipStatusRegistrationRollovers,
       "adGenSipIdentity": adGenSipIdentity}
)
