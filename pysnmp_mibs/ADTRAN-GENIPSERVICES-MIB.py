# SNMP MIB module (ADTRAN-GENIPSERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENIPSERVICES-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:31:54 2025
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

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adIdentityShared,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentityShared")

(AtmVcIdentifier,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVcIdentifier",
    "AtmVpIdentifier")

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

adGenCndIP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62)
)
if mibBuilder.loadTexts:
    adGenCndIP.setRevisions(
        ("2012-10-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )



# MIB Managed Objects in the order of their OIDs

_AdGenIpConfig_ObjectIdentity = ObjectIdentity
adGenIpConfig = _AdGenIpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 1)
)
_AdGenIpProv_ObjectIdentity = ObjectIdentity
adGenIpProv = _AdGenIpProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2)
)
_AdGenIpVlanVcMapProfileTable_Object = MibTable
adGenIpVlanVcMapProfileTable = _AdGenIpVlanVcMapProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1)
)
if mibBuilder.loadTexts:
    adGenIpVlanVcMapProfileTable.setStatus("current")
_AdGenIpVlanVcMapProfileEntry_Object = MibTableRow
adGenIpVlanVcMapProfileEntry = _AdGenIpVlanVcMapProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1)
)
adGenIpVlanVcMapProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENIPSERVICES-MIB", "adGenIpVlanVcVpi"),
    (0, "ADTRAN-GENIPSERVICES-MIB", "adGenIpVlanVcVci"),
    (0, "ADTRAN-GENIPSERVICES-MIB", "adGenIpVlanVcVID"),
)
if mibBuilder.loadTexts:
    adGenIpVlanVcMapProfileEntry.setStatus("current")
_AdGenIpVlanVcVpi_Type = AtmVpIdentifier
_AdGenIpVlanVcVpi_Object = MibTableColumn
adGenIpVlanVcVpi = _AdGenIpVlanVcVpi_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 1),
    _AdGenIpVlanVcVpi_Type()
)
adGenIpVlanVcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenIpVlanVcVpi.setStatus("current")
_AdGenIpVlanVcVci_Type = AtmVcIdentifier
_AdGenIpVlanVcVci_Object = MibTableColumn
adGenIpVlanVcVci = _AdGenIpVlanVcVci_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 2),
    _AdGenIpVlanVcVci_Type()
)
adGenIpVlanVcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenIpVlanVcVci.setStatus("current")
_AdGenIpVlanVcVID_Type = VlanId
_AdGenIpVlanVcVID_Object = MibTableColumn
adGenIpVlanVcVID = _AdGenIpVlanVcVID_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 3),
    _AdGenIpVlanVcVID_Type()
)
adGenIpVlanVcVID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenIpVlanVcVID.setStatus("current")


class _AdGenIpVlanVcMapProfileName_Type(DisplayString):
    """Custom type adGenIpVlanVcMapProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdGenIpVlanVcMapProfileName_Type.__name__ = "DisplayString"
_AdGenIpVlanVcMapProfileName_Object = MibTableColumn
adGenIpVlanVcMapProfileName = _AdGenIpVlanVcMapProfileName_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 4),
    _AdGenIpVlanVcMapProfileName_Type()
)
adGenIpVlanVcMapProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcMapProfileName.setStatus("current")


class _AdGenIpVlanVcEncapsMode_Type(Integer32):
    """Custom type adGenIpVlanVcEncapsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ipoe", 1),
          ("pppoe", 2),
          ("pppoa", 3),
          ("notApplicable", 4),
          ("atmoe", 5),
          ("pppoaVcMux", 6),
          ("autoDetect", 7))
    )


_AdGenIpVlanVcEncapsMode_Type.__name__ = "Integer32"
_AdGenIpVlanVcEncapsMode_Object = MibTableColumn
adGenIpVlanVcEncapsMode = _AdGenIpVlanVcEncapsMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 5),
    _AdGenIpVlanVcEncapsMode_Type()
)
adGenIpVlanVcEncapsMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcEncapsMode.setStatus("current")


class _AdGenIpVlanVcPBits_Type(Integer32):
    """Custom type adGenIpVlanVcPBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_AdGenIpVlanVcPBits_Type.__name__ = "Integer32"
_AdGenIpVlanVcPBits_Object = MibTableColumn
adGenIpVlanVcPBits = _AdGenIpVlanVcPBits_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 6),
    _AdGenIpVlanVcPBits_Type()
)
adGenIpVlanVcPBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcPBits.setStatus("current")


class _AdGenIpVlanVcManualAddrAging_Type(Integer32):
    """Custom type adGenIpVlanVcManualAddrAging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_AdGenIpVlanVcManualAddrAging_Type.__name__ = "Integer32"
_AdGenIpVlanVcManualAddrAging_Object = MibTableColumn
adGenIpVlanVcManualAddrAging = _AdGenIpVlanVcManualAddrAging_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 7),
    _AdGenIpVlanVcManualAddrAging_Type()
)
adGenIpVlanVcManualAddrAging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcManualAddrAging.setStatus("current")


class _AdGenIpVlanVcPPPoERelay_Type(Integer32):
    """Custom type adGenIpVlanVcPPPoERelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdGenIpVlanVcPPPoERelay_Type.__name__ = "Integer32"
_AdGenIpVlanVcPPPoERelay_Object = MibTableColumn
adGenIpVlanVcPPPoERelay = _AdGenIpVlanVcPPPoERelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 8),
    _AdGenIpVlanVcPPPoERelay_Type()
)
adGenIpVlanVcPPPoERelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcPPPoERelay.setStatus("deprecated")


class _AdGenIpVlanVcIntermedAgent_Type(Integer32):
    """Custom type adGenIpVlanVcIntermedAgent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdGenIpVlanVcIntermedAgent_Type.__name__ = "Integer32"
_AdGenIpVlanVcIntermedAgent_Object = MibTableColumn
adGenIpVlanVcIntermedAgent = _AdGenIpVlanVcIntermedAgent_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 9),
    _AdGenIpVlanVcIntermedAgent_Type()
)
adGenIpVlanVcIntermedAgent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcIntermedAgent.setStatus("current")


class _AdGenIpVlanVcDhcpRelay_Type(Integer32):
    """Custom type adGenIpVlanVcDhcpRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdGenIpVlanVcDhcpRelay_Type.__name__ = "Integer32"
_AdGenIpVlanVcDhcpRelay_Object = MibTableColumn
adGenIpVlanVcDhcpRelay = _AdGenIpVlanVcDhcpRelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 10),
    _AdGenIpVlanVcDhcpRelay_Type()
)
adGenIpVlanVcDhcpRelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcDhcpRelay.setStatus("current")


class _AdGenIpVlanVcOption82Insert_Type(Integer32):
    """Custom type adGenIpVlanVcOption82Insert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdGenIpVlanVcOption82Insert_Type.__name__ = "Integer32"
_AdGenIpVlanVcOption82Insert_Object = MibTableColumn
adGenIpVlanVcOption82Insert = _AdGenIpVlanVcOption82Insert_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 11),
    _AdGenIpVlanVcOption82Insert_Type()
)
adGenIpVlanVcOption82Insert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcOption82Insert.setStatus("current")


class _AdGenIpVlanVcLearnedIpAddrAgingMethod_Type(Integer32):
    """Custom type adGenIpVlanVcLearnedIpAddrAgingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lease", 1),
          ("fixed", 2),
          ("notApplicable", 3))
    )


_AdGenIpVlanVcLearnedIpAddrAgingMethod_Type.__name__ = "Integer32"
_AdGenIpVlanVcLearnedIpAddrAgingMethod_Object = MibTableColumn
adGenIpVlanVcLearnedIpAddrAgingMethod = _AdGenIpVlanVcLearnedIpAddrAgingMethod_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 12),
    _AdGenIpVlanVcLearnedIpAddrAgingMethod_Type()
)
adGenIpVlanVcLearnedIpAddrAgingMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcLearnedIpAddrAgingMethod.setStatus("current")


class _AdGenIpVlanVcIgmpProcessing_Type(Integer32):
    """Custom type adGenIpVlanVcIgmpProcessing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("forward", 2),
          ("snooping", 3),
          ("proxy", 4),
          ("notApplicable", 5))
    )


_AdGenIpVlanVcIgmpProcessing_Type.__name__ = "Integer32"
_AdGenIpVlanVcIgmpProcessing_Object = MibTableColumn
adGenIpVlanVcIgmpProcessing = _AdGenIpVlanVcIgmpProcessing_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 13),
    _AdGenIpVlanVcIgmpProcessing_Type()
)
adGenIpVlanVcIgmpProcessing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcIgmpProcessing.setStatus("current")


class _AdGenIpVlanVcIgmpVersion_Type(Integer32):
    """Custom type adGenIpVlanVcIgmpVersion based on Integer32"""
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
        *(("v1", 1),
          ("v2", 2),
          ("v3", 3),
          ("notApplicable", 4))
    )


_AdGenIpVlanVcIgmpVersion_Type.__name__ = "Integer32"
_AdGenIpVlanVcIgmpVersion_Object = MibTableColumn
adGenIpVlanVcIgmpVersion = _AdGenIpVlanVcIgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 14),
    _AdGenIpVlanVcIgmpVersion_Type()
)
adGenIpVlanVcIgmpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcIgmpVersion.setStatus("current")


class _AdGenIpVlanVcLastMemberQueryInterval_Type(Integer32):
    """Custom type adGenIpVlanVcLastMemberQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1500),
    )


_AdGenIpVlanVcLastMemberQueryInterval_Type.__name__ = "Integer32"
_AdGenIpVlanVcLastMemberQueryInterval_Object = MibTableColumn
adGenIpVlanVcLastMemberQueryInterval = _AdGenIpVlanVcLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 15),
    _AdGenIpVlanVcLastMemberQueryInterval_Type()
)
adGenIpVlanVcLastMemberQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcLastMemberQueryInterval.setStatus("current")


class _AdGenIpVlanVcLastMemberQueryCount_Type(Integer32):
    """Custom type adGenIpVlanVcLastMemberQueryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_AdGenIpVlanVcLastMemberQueryCount_Type.__name__ = "Integer32"
_AdGenIpVlanVcLastMemberQueryCount_Object = MibTableColumn
adGenIpVlanVcLastMemberQueryCount = _AdGenIpVlanVcLastMemberQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 16),
    _AdGenIpVlanVcLastMemberQueryCount_Type()
)
adGenIpVlanVcLastMemberQueryCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcLastMemberQueryCount.setStatus("current")


class _AdGenIpVlanVcImmediateLeave_Type(Integer32):
    """Custom type adGenIpVlanVcImmediateLeave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdGenIpVlanVcImmediateLeave_Type.__name__ = "Integer32"
_AdGenIpVlanVcImmediateLeave_Object = MibTableColumn
adGenIpVlanVcImmediateLeave = _AdGenIpVlanVcImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 17),
    _AdGenIpVlanVcImmediateLeave_Type()
)
adGenIpVlanVcImmediateLeave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcImmediateLeave.setStatus("current")


class _AdGenIpVlanVcMaxAllowedMcastSessions_Type(Integer32):
    """Custom type adGenIpVlanVcMaxAllowedMcastSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AdGenIpVlanVcMaxAllowedMcastSessions_Type.__name__ = "Integer32"
_AdGenIpVlanVcMaxAllowedMcastSessions_Object = MibTableColumn
adGenIpVlanVcMaxAllowedMcastSessions = _AdGenIpVlanVcMaxAllowedMcastSessions_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 18),
    _AdGenIpVlanVcMaxAllowedMcastSessions_Type()
)
adGenIpVlanVcMaxAllowedMcastSessions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcMaxAllowedMcastSessions.setStatus("current")


class _AdGenIpVlanVcL2L4Classifier_Type(Integer32):
    """Custom type adGenIpVlanVcL2L4Classifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ethertype", 1),
          ("protocolId", 2),
          ("reserved1", 3),
          ("reserved2", 4),
          ("notApplicable", 5))
    )


_AdGenIpVlanVcL2L4Classifier_Type.__name__ = "Integer32"
_AdGenIpVlanVcL2L4Classifier_Object = MibTableColumn
adGenIpVlanVcL2L4Classifier = _AdGenIpVlanVcL2L4Classifier_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 19),
    _AdGenIpVlanVcL2L4Classifier_Type()
)
adGenIpVlanVcL2L4Classifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcL2L4Classifier.setStatus("current")
_AdGenIpVlanVcL2L4Value_Type = Integer32
_AdGenIpVlanVcL2L4Value_Object = MibTableColumn
adGenIpVlanVcL2L4Value = _AdGenIpVlanVcL2L4Value_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 20),
    _AdGenIpVlanVcL2L4Value_Type()
)
adGenIpVlanVcL2L4Value.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcL2L4Value.setStatus("current")
_AdGenIpVlanVcMapProfileRowStatus_Type = RowStatus
_AdGenIpVlanVcMapProfileRowStatus_Object = MibTableColumn
adGenIpVlanVcMapProfileRowStatus = _AdGenIpVlanVcMapProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 21),
    _AdGenIpVlanVcMapProfileRowStatus_Type()
)
adGenIpVlanVcMapProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcMapProfileRowStatus.setStatus("current")


class _AdGenIpVlanVcDhcpTrustedInterface_Type(Integer32):
    """Custom type adGenIpVlanVcDhcpTrustedInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trusted", 1),
          ("untrusted", 2))
    )


_AdGenIpVlanVcDhcpTrustedInterface_Type.__name__ = "Integer32"
_AdGenIpVlanVcDhcpTrustedInterface_Object = MibTableColumn
adGenIpVlanVcDhcpTrustedInterface = _AdGenIpVlanVcDhcpTrustedInterface_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 22),
    _AdGenIpVlanVcDhcpTrustedInterface_Type()
)
adGenIpVlanVcDhcpTrustedInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcDhcpTrustedInterface.setStatus("current")


class _AdGenIpVlanVcDhcpPPPoERemoteId_Type(Integer32):
    """Custom type adGenIpVlanVcDhcpPPPoERemoteId based on Integer32"""
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


_AdGenIpVlanVcDhcpPPPoERemoteId_Type.__name__ = "Integer32"
_AdGenIpVlanVcDhcpPPPoERemoteId_Object = MibTableColumn
adGenIpVlanVcDhcpPPPoERemoteId = _AdGenIpVlanVcDhcpPPPoERemoteId_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 23),
    _AdGenIpVlanVcDhcpPPPoERemoteId_Type()
)
adGenIpVlanVcDhcpPPPoERemoteId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcDhcpPPPoERemoteId.setStatus("current")


class _AdGenIpVlanVcDhcpPPPoELoopCharacteristics_Type(Integer32):
    """Custom type adGenIpVlanVcDhcpPPPoELoopCharacteristics based on Integer32"""
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


_AdGenIpVlanVcDhcpPPPoELoopCharacteristics_Type.__name__ = "Integer32"
_AdGenIpVlanVcDhcpPPPoELoopCharacteristics_Object = MibTableColumn
adGenIpVlanVcDhcpPPPoELoopCharacteristics = _AdGenIpVlanVcDhcpPPPoELoopCharacteristics_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 24),
    _AdGenIpVlanVcDhcpPPPoELoopCharacteristics_Type()
)
adGenIpVlanVcDhcpPPPoELoopCharacteristics.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcDhcpPPPoELoopCharacteristics.setStatus("current")


class _AdGenIpVlanVcDhcpPPPoECircuitIdFormat_Type(DisplayString):
    """Custom type adGenIpVlanVcDhcpPPPoECircuitIdFormat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AdGenIpVlanVcDhcpPPPoECircuitIdFormat_Type.__name__ = "DisplayString"
_AdGenIpVlanVcDhcpPPPoECircuitIdFormat_Object = MibTableColumn
adGenIpVlanVcDhcpPPPoECircuitIdFormat = _AdGenIpVlanVcDhcpPPPoECircuitIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 25),
    _AdGenIpVlanVcDhcpPPPoECircuitIdFormat_Type()
)
adGenIpVlanVcDhcpPPPoECircuitIdFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcDhcpPPPoECircuitIdFormat.setStatus("current")
_AdGenIpVlanVcPPPoASessionTimeout_Type = Integer32
_AdGenIpVlanVcPPPoASessionTimeout_Object = MibTableColumn
adGenIpVlanVcPPPoASessionTimeout = _AdGenIpVlanVcPPPoASessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 26),
    _AdGenIpVlanVcPPPoASessionTimeout_Type()
)
adGenIpVlanVcPPPoASessionTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcPPPoASessionTimeout.setStatus("current")
_AdGenIpVlanVcCtagVID_Type = VlanId
_AdGenIpVlanVcCtagVID_Object = MibTableColumn
adGenIpVlanVcCtagVID = _AdGenIpVlanVcCtagVID_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 27),
    _AdGenIpVlanVcCtagVID_Type()
)
adGenIpVlanVcCtagVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcCtagVID.setStatus("current")


class _AdGenIpVlanVcCtagPbitsMethod_Type(Integer32):
    """Custom type adGenIpVlanVcCtagPbitsMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copyFromStag", 1),
          ("specifyFixedValue", 2))
    )


_AdGenIpVlanVcCtagPbitsMethod_Type.__name__ = "Integer32"
_AdGenIpVlanVcCtagPbitsMethod_Object = MibTableColumn
adGenIpVlanVcCtagPbitsMethod = _AdGenIpVlanVcCtagPbitsMethod_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 28),
    _AdGenIpVlanVcCtagPbitsMethod_Type()
)
adGenIpVlanVcCtagPbitsMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcCtagPbitsMethod.setStatus("current")


class _AdGenIpVlanVcCtagPbitsValue_Type(Integer32):
    """Custom type adGenIpVlanVcCtagPbitsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenIpVlanVcCtagPbitsValue_Type.__name__ = "Integer32"
_AdGenIpVlanVcCtagPbitsValue_Object = MibTableColumn
adGenIpVlanVcCtagPbitsValue = _AdGenIpVlanVcCtagPbitsValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 29),
    _AdGenIpVlanVcCtagPbitsValue_Type()
)
adGenIpVlanVcCtagPbitsValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcCtagPbitsValue.setStatus("current")


class _AdGenIpVlanVcMulticastVlanVID_Type(Integer32):
    """Custom type adGenIpVlanVcMulticastVlanVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4095),
    )


_AdGenIpVlanVcMulticastVlanVID_Type.__name__ = "Integer32"
_AdGenIpVlanVcMulticastVlanVID_Object = MibTableColumn
adGenIpVlanVcMulticastVlanVID = _AdGenIpVlanVcMulticastVlanVID_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 30),
    _AdGenIpVlanVcMulticastVlanVID_Type()
)
adGenIpVlanVcMulticastVlanVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcMulticastVlanVID.setStatus("current")


class _AdGenIpVlanVcMulticastVlanUpstreamPriority_Type(Integer32):
    """Custom type adGenIpVlanVcMulticastVlanUpstreamPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenIpVlanVcMulticastVlanUpstreamPriority_Type.__name__ = "Integer32"
_AdGenIpVlanVcMulticastVlanUpstreamPriority_Object = MibTableColumn
adGenIpVlanVcMulticastVlanUpstreamPriority = _AdGenIpVlanVcMulticastVlanUpstreamPriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 31),
    _AdGenIpVlanVcMulticastVlanUpstreamPriority_Type()
)
adGenIpVlanVcMulticastVlanUpstreamPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcMulticastVlanUpstreamPriority.setStatus("current")


class _AdGenIpVlanVcMulticastDownstreamVlanVID_Type(Integer32):
    """Custom type adGenIpVlanVcMulticastDownstreamVlanVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AdGenIpVlanVcMulticastDownstreamVlanVID_Type.__name__ = "Integer32"
_AdGenIpVlanVcMulticastDownstreamVlanVID_Object = MibTableColumn
adGenIpVlanVcMulticastDownstreamVlanVID = _AdGenIpVlanVcMulticastDownstreamVlanVID_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 32),
    _AdGenIpVlanVcMulticastDownstreamVlanVID_Type()
)
adGenIpVlanVcMulticastDownstreamVlanVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcMulticastDownstreamVlanVID.setStatus("current")


class _AdGenIpVlanVcDownstreamPolicer_Type(Integer32):
    """Custom type adGenIpVlanVcDownstreamPolicer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdGenIpVlanVcDownstreamPolicer_Type.__name__ = "Integer32"
_AdGenIpVlanVcDownstreamPolicer_Object = MibTableColumn
adGenIpVlanVcDownstreamPolicer = _AdGenIpVlanVcDownstreamPolicer_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 33),
    _AdGenIpVlanVcDownstreamPolicer_Type()
)
adGenIpVlanVcDownstreamPolicer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcDownstreamPolicer.setStatus("current")
_AdGenIpVlanVcDownstreamPolicerCIR_Type = Integer32
_AdGenIpVlanVcDownstreamPolicerCIR_Object = MibTableColumn
adGenIpVlanVcDownstreamPolicerCIR = _AdGenIpVlanVcDownstreamPolicerCIR_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 34),
    _AdGenIpVlanVcDownstreamPolicerCIR_Type()
)
adGenIpVlanVcDownstreamPolicerCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcDownstreamPolicerCIR.setStatus("current")
_AdGenIpVlanVcDownstreamPolicerCBS_Type = Integer32
_AdGenIpVlanVcDownstreamPolicerCBS_Object = MibTableColumn
adGenIpVlanVcDownstreamPolicerCBS = _AdGenIpVlanVcDownstreamPolicerCBS_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 35),
    _AdGenIpVlanVcDownstreamPolicerCBS_Type()
)
adGenIpVlanVcDownstreamPolicerCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcDownstreamPolicerCBS.setStatus("current")
_AdGenIpVlanVcDownstreamPolicerEIR_Type = Integer32
_AdGenIpVlanVcDownstreamPolicerEIR_Object = MibTableColumn
adGenIpVlanVcDownstreamPolicerEIR = _AdGenIpVlanVcDownstreamPolicerEIR_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 36),
    _AdGenIpVlanVcDownstreamPolicerEIR_Type()
)
adGenIpVlanVcDownstreamPolicerEIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcDownstreamPolicerEIR.setStatus("current")
_AdGenIpVlanVcDownstreamPolicerEBS_Type = Integer32
_AdGenIpVlanVcDownstreamPolicerEBS_Object = MibTableColumn
adGenIpVlanVcDownstreamPolicerEBS = _AdGenIpVlanVcDownstreamPolicerEBS_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 37),
    _AdGenIpVlanVcDownstreamPolicerEBS_Type()
)
adGenIpVlanVcDownstreamPolicerEBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcDownstreamPolicerEBS.setStatus("current")


class _AdGenIpVlanVcUpstreamPolicer_Type(Integer32):
    """Custom type adGenIpVlanVcUpstreamPolicer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdGenIpVlanVcUpstreamPolicer_Type.__name__ = "Integer32"
_AdGenIpVlanVcUpstreamPolicer_Object = MibTableColumn
adGenIpVlanVcUpstreamPolicer = _AdGenIpVlanVcUpstreamPolicer_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 38),
    _AdGenIpVlanVcUpstreamPolicer_Type()
)
adGenIpVlanVcUpstreamPolicer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcUpstreamPolicer.setStatus("current")
_AdGenIpVlanVcUpstreamPolicerCIR_Type = Integer32
_AdGenIpVlanVcUpstreamPolicerCIR_Object = MibTableColumn
adGenIpVlanVcUpstreamPolicerCIR = _AdGenIpVlanVcUpstreamPolicerCIR_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 39),
    _AdGenIpVlanVcUpstreamPolicerCIR_Type()
)
adGenIpVlanVcUpstreamPolicerCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcUpstreamPolicerCIR.setStatus("current")
_AdGenIpVlanVcUpstreamPolicerCBS_Type = Integer32
_AdGenIpVlanVcUpstreamPolicerCBS_Object = MibTableColumn
adGenIpVlanVcUpstreamPolicerCBS = _AdGenIpVlanVcUpstreamPolicerCBS_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 40),
    _AdGenIpVlanVcUpstreamPolicerCBS_Type()
)
adGenIpVlanVcUpstreamPolicerCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcUpstreamPolicerCBS.setStatus("current")
_AdGenIpVlanVcUpstreamPolicerEIR_Type = Integer32
_AdGenIpVlanVcUpstreamPolicerEIR_Object = MibTableColumn
adGenIpVlanVcUpstreamPolicerEIR = _AdGenIpVlanVcUpstreamPolicerEIR_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 41),
    _AdGenIpVlanVcUpstreamPolicerEIR_Type()
)
adGenIpVlanVcUpstreamPolicerEIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcUpstreamPolicerEIR.setStatus("current")
_AdGenIpVlanVcUpstreamPolicerEBS_Type = Integer32
_AdGenIpVlanVcUpstreamPolicerEBS_Object = MibTableColumn
adGenIpVlanVcUpstreamPolicerEBS = _AdGenIpVlanVcUpstreamPolicerEBS_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 42),
    _AdGenIpVlanVcUpstreamPolicerEBS_Type()
)
adGenIpVlanVcUpstreamPolicerEBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcUpstreamPolicerEBS.setStatus("current")
_AdGenIpVlanVcMCastSessionControlStartIP_Type = IpAddress
_AdGenIpVlanVcMCastSessionControlStartIP_Object = MibTableColumn
adGenIpVlanVcMCastSessionControlStartIP = _AdGenIpVlanVcMCastSessionControlStartIP_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 43),
    _AdGenIpVlanVcMCastSessionControlStartIP_Type()
)
adGenIpVlanVcMCastSessionControlStartIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcMCastSessionControlStartIP.setStatus("current")
_AdGenIpVlanVcMCastSessionControlEndIP_Type = IpAddress
_AdGenIpVlanVcMCastSessionControlEndIP_Object = MibTableColumn
adGenIpVlanVcMCastSessionControlEndIP = _AdGenIpVlanVcMCastSessionControlEndIP_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 44),
    _AdGenIpVlanVcMCastSessionControlEndIP_Type()
)
adGenIpVlanVcMCastSessionControlEndIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcMCastSessionControlEndIP.setStatus("current")
_AdGenIpVlanVcMCastSessionControlBitrate_Type = Integer32
_AdGenIpVlanVcMCastSessionControlBitrate_Object = MibTableColumn
adGenIpVlanVcMCastSessionControlBitrate = _AdGenIpVlanVcMCastSessionControlBitrate_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 45),
    _AdGenIpVlanVcMCastSessionControlBitrate_Type()
)
adGenIpVlanVcMCastSessionControlBitrate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcMCastSessionControlBitrate.setStatus("current")
_AdGenIpVlanVcPolicerStatus_Type = DisplayString
_AdGenIpVlanVcPolicerStatus_Object = MibTableColumn
adGenIpVlanVcPolicerStatus = _AdGenIpVlanVcPolicerStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 46),
    _AdGenIpVlanVcPolicerStatus_Type()
)
adGenIpVlanVcPolicerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcPolicerStatus.setStatus("current")


class _AdGenIpVlanVcUpstreamMACDAFilter_Type(Integer32):
    """Custom type adGenIpVlanVcUpstreamMACDAFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gatewayMACOnly", 1),
          ("allowAllValidMACs", 2))
    )


_AdGenIpVlanVcUpstreamMACDAFilter_Type.__name__ = "Integer32"
_AdGenIpVlanVcUpstreamMACDAFilter_Object = MibTableColumn
adGenIpVlanVcUpstreamMACDAFilter = _AdGenIpVlanVcUpstreamMACDAFilter_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 47),
    _AdGenIpVlanVcUpstreamMACDAFilter_Type()
)
adGenIpVlanVcUpstreamMACDAFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcUpstreamMACDAFilter.setStatus("current")
_AdGenIpVlanVcIgmpRouterIP_Type = IpAddress
_AdGenIpVlanVcIgmpRouterIP_Object = MibTableColumn
adGenIpVlanVcIgmpRouterIP = _AdGenIpVlanVcIgmpRouterIP_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 1, 1, 48),
    _AdGenIpVlanVcIgmpRouterIP_Type()
)
adGenIpVlanVcIgmpRouterIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpVlanVcIgmpRouterIP.setStatus("current")
_AdGenIpPortProfileTable_Object = MibTable
adGenIpPortProfileTable = _AdGenIpPortProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 2)
)
if mibBuilder.loadTexts:
    adGenIpPortProfileTable.setStatus("current")
_AdGenIpPortProfileEntry_Object = MibTableRow
adGenIpPortProfileEntry = _AdGenIpPortProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 2, 1)
)
adGenIpPortProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenIpPortProfileEntry.setStatus("current")


class _AdGenIpPortProfileName_Type(DisplayString):
    """Custom type adGenIpPortProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdGenIpPortProfileName_Type.__name__ = "DisplayString"
_AdGenIpPortProfileName_Object = MibTableColumn
adGenIpPortProfileName = _AdGenIpPortProfileName_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 2, 1, 1),
    _AdGenIpPortProfileName_Type()
)
adGenIpPortProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpPortProfileName.setStatus("current")


class _AdGenIpPortNetTrafficTags_Type(Integer32):
    """Custom type adGenIpPortNetTrafficTags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noTags", 1),
          ("singleTagged", 2),
          ("doubleTagged", 3))
    )


_AdGenIpPortNetTrafficTags_Type.__name__ = "Integer32"
_AdGenIpPortNetTrafficTags_Object = MibTableColumn
adGenIpPortNetTrafficTags = _AdGenIpPortNetTrafficTags_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 2, 1, 2),
    _AdGenIpPortNetTrafficTags_Type()
)
adGenIpPortNetTrafficTags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpPortNetTrafficTags.setStatus("current")


class _AdGenIpPortNetworkModel_Type(Integer32):
    """Custom type adGenIpPortNetworkModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("vlanPerServicePvcPerService", 1),
          ("vlanPerSubscriberPvcPerService", 2),
          ("vlanPerServiceSinglePvc", 3),
          ("vlanPerSubscriberSinglePvc", 4),
          ("noVlanTagsSinglePvc", 5))
    )


_AdGenIpPortNetworkModel_Type.__name__ = "Integer32"
_AdGenIpPortNetworkModel_Object = MibTableColumn
adGenIpPortNetworkModel = _AdGenIpPortNetworkModel_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 2, 1, 3),
    _AdGenIpPortNetworkModel_Type()
)
adGenIpPortNetworkModel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpPortNetworkModel.setStatus("current")
_AdGenIpPortSTagVID_Type = VlanId
_AdGenIpPortSTagVID_Object = MibTableColumn
adGenIpPortSTagVID = _AdGenIpPortSTagVID_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 2, 1, 4),
    _AdGenIpPortSTagVID_Type()
)
adGenIpPortSTagVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpPortSTagVID.setStatus("current")


class _AdGenIpPortSTagPBitsMethod_Type(Integer32):
    """Custom type adGenIpPortSTagPBitsMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copyFromCTag", 1),
          ("specifyFixedValue", 2))
    )


_AdGenIpPortSTagPBitsMethod_Type.__name__ = "Integer32"
_AdGenIpPortSTagPBitsMethod_Object = MibTableColumn
adGenIpPortSTagPBitsMethod = _AdGenIpPortSTagPBitsMethod_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 2, 1, 5),
    _AdGenIpPortSTagPBitsMethod_Type()
)
adGenIpPortSTagPBitsMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpPortSTagPBitsMethod.setStatus("current")


class _AdGenIpPortSTagPBitsValue_Type(Integer32):
    """Custom type adGenIpPortSTagPBitsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenIpPortSTagPBitsValue_Type.__name__ = "Integer32"
_AdGenIpPortSTagPBitsValue_Object = MibTableColumn
adGenIpPortSTagPBitsValue = _AdGenIpPortSTagPBitsValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 2, 1, 6),
    _AdGenIpPortSTagPBitsValue_Type()
)
adGenIpPortSTagPBitsValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpPortSTagPBitsValue.setStatus("current")


class _AdGenIpPortMaxMacAddr_Type(Integer32):
    """Custom type adGenIpPortMaxMacAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AdGenIpPortMaxMacAddr_Type.__name__ = "Integer32"
_AdGenIpPortMaxMacAddr_Object = MibTableColumn
adGenIpPortMaxMacAddr = _AdGenIpPortMaxMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 2, 1, 7),
    _AdGenIpPortMaxMacAddr_Type()
)
adGenIpPortMaxMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpPortMaxMacAddr.setStatus("current")


class _AdGenIpPortLearnAndLockAddr_Type(Integer32):
    """Custom type adGenIpPortLearnAndLockAddr based on Integer32"""
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


_AdGenIpPortLearnAndLockAddr_Type.__name__ = "Integer32"
_AdGenIpPortLearnAndLockAddr_Object = MibTableColumn
adGenIpPortLearnAndLockAddr = _AdGenIpPortLearnAndLockAddr_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 2, 1, 8),
    _AdGenIpPortLearnAndLockAddr_Type()
)
adGenIpPortLearnAndLockAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpPortLearnAndLockAddr.setStatus("current")
_AdGenIpPortIgmpLimit_Type = Integer32
_AdGenIpPortIgmpLimit_Object = MibTableColumn
adGenIpPortIgmpLimit = _AdGenIpPortIgmpLimit_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 2, 1, 9),
    _AdGenIpPortIgmpLimit_Type()
)
adGenIpPortIgmpLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpPortIgmpLimit.setStatus("current")
_AdGenIpPortIgmpLockout_Type = Integer32
_AdGenIpPortIgmpLockout_Object = MibTableColumn
adGenIpPortIgmpLockout = _AdGenIpPortIgmpLockout_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 2, 1, 10),
    _AdGenIpPortIgmpLockout_Type()
)
adGenIpPortIgmpLockout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpPortIgmpLockout.setStatus("current")
_AdGenIpPortArpLimit_Type = Integer32
_AdGenIpPortArpLimit_Object = MibTableColumn
adGenIpPortArpLimit = _AdGenIpPortArpLimit_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 2, 1, 11),
    _AdGenIpPortArpLimit_Type()
)
adGenIpPortArpLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpPortArpLimit.setStatus("current")
_AdGenIpPortArpLockout_Type = Integer32
_AdGenIpPortArpLockout_Object = MibTableColumn
adGenIpPortArpLockout = _AdGenIpPortArpLockout_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 2, 1, 12),
    _AdGenIpPortArpLockout_Type()
)
adGenIpPortArpLockout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpPortArpLockout.setStatus("current")
_AdGenIpPortDhcpLimit_Type = Integer32
_AdGenIpPortDhcpLimit_Object = MibTableColumn
adGenIpPortDhcpLimit = _AdGenIpPortDhcpLimit_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 2, 1, 13),
    _AdGenIpPortDhcpLimit_Type()
)
adGenIpPortDhcpLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpPortDhcpLimit.setStatus("current")
_AdGenIpPortDhcpLockout_Type = Integer32
_AdGenIpPortDhcpLockout_Object = MibTableColumn
adGenIpPortDhcpLockout = _AdGenIpPortDhcpLockout_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 2, 1, 14),
    _AdGenIpPortDhcpLockout_Type()
)
adGenIpPortDhcpLockout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpPortDhcpLockout.setStatus("current")
_AdGenIpPortPppoeLimit_Type = Integer32
_AdGenIpPortPppoeLimit_Object = MibTableColumn
adGenIpPortPppoeLimit = _AdGenIpPortPppoeLimit_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 2, 1, 15),
    _AdGenIpPortPppoeLimit_Type()
)
adGenIpPortPppoeLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpPortPppoeLimit.setStatus("current")
_AdGenIpPortPppoeLockout_Type = Integer32
_AdGenIpPortPppoeLockout_Object = MibTableColumn
adGenIpPortPppoeLockout = _AdGenIpPortPppoeLockout_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 2, 1, 16),
    _AdGenIpPortPppoeLockout_Type()
)
adGenIpPortPppoeLockout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpPortPppoeLockout.setStatus("current")
_AdGenIpPortMcastBcastLimit_Type = Integer32
_AdGenIpPortMcastBcastLimit_Object = MibTableColumn
adGenIpPortMcastBcastLimit = _AdGenIpPortMcastBcastLimit_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 2, 1, 17),
    _AdGenIpPortMcastBcastLimit_Type()
)
adGenIpPortMcastBcastLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpPortMcastBcastLimit.setStatus("current")
_AdGenIpPortMcastBcastLockout_Type = Integer32
_AdGenIpPortMcastBcastLockout_Object = MibTableColumn
adGenIpPortMcastBcastLockout = _AdGenIpPortMcastBcastLockout_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 2, 1, 18),
    _AdGenIpPortMcastBcastLockout_Type()
)
adGenIpPortMcastBcastLockout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpPortMcastBcastLockout.setStatus("current")
_AdGenIpPortUcastExceptionLimit_Type = Integer32
_AdGenIpPortUcastExceptionLimit_Object = MibTableColumn
adGenIpPortUcastExceptionLimit = _AdGenIpPortUcastExceptionLimit_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 2, 1, 19),
    _AdGenIpPortUcastExceptionLimit_Type()
)
adGenIpPortUcastExceptionLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpPortUcastExceptionLimit.setStatus("current")
_AdGenIpPortUcastExceptionLockout_Type = Integer32
_AdGenIpPortUcastExceptionLockout_Object = MibTableColumn
adGenIpPortUcastExceptionLockout = _AdGenIpPortUcastExceptionLockout_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 2, 1, 20),
    _AdGenIpPortUcastExceptionLockout_Type()
)
adGenIpPortUcastExceptionLockout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpPortUcastExceptionLockout.setStatus("current")
_AdGenIpPortProfileRowStatus_Type = RowStatus
_AdGenIpPortProfileRowStatus_Object = MibTableColumn
adGenIpPortProfileRowStatus = _AdGenIpPortProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 2, 1, 21),
    _AdGenIpPortProfileRowStatus_Type()
)
adGenIpPortProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpPortProfileRowStatus.setStatus("current")
_AdGenIpVlanPropertiesTable_Object = MibTable
adGenIpVlanPropertiesTable = _AdGenIpVlanPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 4)
)
if mibBuilder.loadTexts:
    adGenIpVlanPropertiesTable.setStatus("current")
_AdGenIpVlanPropertiesEntry_Object = MibTableRow
adGenIpVlanPropertiesEntry = _AdGenIpVlanPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 4, 1)
)
adGenIpVlanPropertiesEntry.setIndexNames(
    (0, "ADTRAN-GENIPSERVICES-MIB", "adGenIpVlanVcVID"),
)
if mibBuilder.loadTexts:
    adGenIpVlanPropertiesEntry.setStatus("current")
_AdGenIpVlanPropName_Type = DisplayString
_AdGenIpVlanPropName_Object = MibTableColumn
adGenIpVlanPropName = _AdGenIpVlanPropName_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 4, 1, 1),
    _AdGenIpVlanPropName_Type()
)
adGenIpVlanPropName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenIpVlanPropName.setStatus("current")
_AdGenIpSysProvTable_Object = MibTable
adGenIpSysProvTable = _AdGenIpSysProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 5)
)
if mibBuilder.loadTexts:
    adGenIpSysProvTable.setStatus("current")
_AdGenIpSysProvEntry_Object = MibTableRow
adGenIpSysProvEntry = _AdGenIpSysProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 5, 1)
)
adGenIpSysProvEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenIpSysProvEntry.setStatus("current")


class _AdGenIpSysProvMgmtVID_Type(Integer32):
    """Custom type adGenIpSysProvMgmtVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AdGenIpSysProvMgmtVID_Type.__name__ = "Integer32"
_AdGenIpSysProvMgmtVID_Object = MibTableColumn
adGenIpSysProvMgmtVID = _AdGenIpSysProvMgmtVID_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 5, 1, 1),
    _AdGenIpSysProvMgmtVID_Type()
)
adGenIpSysProvMgmtVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpSysProvMgmtVID.setStatus("current")


class _AdGenIpSysProvMgmtTagEnable_Type(Integer32):
    """Custom type adGenIpSysProvMgmtTagEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AdGenIpSysProvMgmtTagEnable_Type.__name__ = "Integer32"
_AdGenIpSysProvMgmtTagEnable_Object = MibTableColumn
adGenIpSysProvMgmtTagEnable = _AdGenIpSysProvMgmtTagEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 5, 1, 2),
    _AdGenIpSysProvMgmtTagEnable_Type()
)
adGenIpSysProvMgmtTagEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpSysProvMgmtTagEnable.setStatus("current")


class _AdGenIpSysProvMgmtPBits_Type(Integer32):
    """Custom type adGenIpSysProvMgmtPBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenIpSysProvMgmtPBits_Type.__name__ = "Integer32"
_AdGenIpSysProvMgmtPBits_Object = MibTableColumn
adGenIpSysProvMgmtPBits = _AdGenIpSysProvMgmtPBits_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 5, 1, 3),
    _AdGenIpSysProvMgmtPBits_Type()
)
adGenIpSysProvMgmtPBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpSysProvMgmtPBits.setStatus("current")


class _AdGenIpSysProvMacAgingTimeout_Type(Integer32):
    """Custom type adGenIpSysProvMacAgingTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenIpSysProvMacAgingTimeout_Type.__name__ = "Integer32"
_AdGenIpSysProvMacAgingTimeout_Object = MibTableColumn
adGenIpSysProvMacAgingTimeout = _AdGenIpSysProvMacAgingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 5, 1, 5),
    _AdGenIpSysProvMacAgingTimeout_Type()
)
adGenIpSysProvMacAgingTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpSysProvMacAgingTimeout.setStatus("current")


class _AdGenIpSysProvIgmpVID_Type(Integer32):
    """Custom type adGenIpSysProvIgmpVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AdGenIpSysProvIgmpVID_Type.__name__ = "Integer32"
_AdGenIpSysProvIgmpVID_Object = MibTableColumn
adGenIpSysProvIgmpVID = _AdGenIpSysProvIgmpVID_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 5, 1, 6),
    _AdGenIpSysProvIgmpVID_Type()
)
adGenIpSysProvIgmpVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpSysProvIgmpVID.setStatus("current")


class _AdGenIpSysProvIgmpTagEnable_Type(Integer32):
    """Custom type adGenIpSysProvIgmpTagEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AdGenIpSysProvIgmpTagEnable_Type.__name__ = "Integer32"
_AdGenIpSysProvIgmpTagEnable_Object = MibTableColumn
adGenIpSysProvIgmpTagEnable = _AdGenIpSysProvIgmpTagEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 5, 1, 7),
    _AdGenIpSysProvIgmpTagEnable_Type()
)
adGenIpSysProvIgmpTagEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpSysProvIgmpTagEnable.setStatus("current")


class _AdGenIpSysProvIgmpPBits_Type(Integer32):
    """Custom type adGenIpSysProvIgmpPBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenIpSysProvIgmpPBits_Type.__name__ = "Integer32"
_AdGenIpSysProvIgmpPBits_Object = MibTableColumn
adGenIpSysProvIgmpPBits = _AdGenIpSysProvIgmpPBits_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 5, 1, 8),
    _AdGenIpSysProvIgmpPBits_Type()
)
adGenIpSysProvIgmpPBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpSysProvIgmpPBits.setStatus("current")
_AdGenIpSysProvIgmpHostIP_Type = IpAddress
_AdGenIpSysProvIgmpHostIP_Object = MibTableColumn
adGenIpSysProvIgmpHostIP = _AdGenIpSysProvIgmpHostIP_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 5, 1, 9),
    _AdGenIpSysProvIgmpHostIP_Type()
)
adGenIpSysProvIgmpHostIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpSysProvIgmpHostIP.setStatus("current")
_AdGenIpVlanAndPortProvTable_Object = MibTable
adGenIpVlanAndPortProvTable = _AdGenIpVlanAndPortProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 6)
)
if mibBuilder.loadTexts:
    adGenIpVlanAndPortProvTable.setStatus("current")
_AdGenIpVlanAndPortProvEntry_Object = MibTableRow
adGenIpVlanAndPortProvEntry = _AdGenIpVlanAndPortProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 6, 1)
)
adGenIpVlanAndPortProvEntry.setIndexNames(
    (0, "ADTRAN-GENIPSERVICES-MIB", "adGenIpVlanVcVID"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenIpVlanAndPortProvEntry.setStatus("current")
_AdGenIpAccessPortVlanMemRowStatus_Type = RowStatus
_AdGenIpAccessPortVlanMemRowStatus_Object = MibTableColumn
adGenIpAccessPortVlanMemRowStatus = _AdGenIpAccessPortVlanMemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 2, 6, 1, 1),
    _AdGenIpAccessPortVlanMemRowStatus_Type()
)
adGenIpAccessPortVlanMemRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIpAccessPortVlanMemRowStatus.setStatus("current")
_AdGenIpStatus_ObjectIdentity = ObjectIdentity
adGenIpStatus = _AdGenIpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 3)
)
_AdGenIpVlanAndPortStatusTable_Object = MibTable
adGenIpVlanAndPortStatusTable = _AdGenIpVlanAndPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 3, 2)
)
if mibBuilder.loadTexts:
    adGenIpVlanAndPortStatusTable.setStatus("current")
_AdGenIpVlanAndPortStatusEntry_Object = MibTableRow
adGenIpVlanAndPortStatusEntry = _AdGenIpVlanAndPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 3, 2, 1)
)
adGenIpVlanAndPortStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENIPSERVICES-MIB", "adGenIpVlanVcVID"),
)
if mibBuilder.loadTexts:
    adGenIpVlanAndPortStatusEntry.setStatus("current")
_AdGenIpConfVlanMapping_Type = Counter32
_AdGenIpConfVlanMapping_Object = MibTableColumn
adGenIpConfVlanMapping = _AdGenIpConfVlanMapping_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 62, 3, 2, 1, 2),
    _AdGenIpConfVlanMapping_Type()
)
adGenIpConfVlanMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIpConfVlanMapping.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENIPSERVICES-MIB",
    **{"VlanId": VlanId,
       "adGenCndIP": adGenCndIP,
       "adGenIpConfig": adGenIpConfig,
       "adGenIpProv": adGenIpProv,
       "adGenIpVlanVcMapProfileTable": adGenIpVlanVcMapProfileTable,
       "adGenIpVlanVcMapProfileEntry": adGenIpVlanVcMapProfileEntry,
       "adGenIpVlanVcVpi": adGenIpVlanVcVpi,
       "adGenIpVlanVcVci": adGenIpVlanVcVci,
       "adGenIpVlanVcVID": adGenIpVlanVcVID,
       "adGenIpVlanVcMapProfileName": adGenIpVlanVcMapProfileName,
       "adGenIpVlanVcEncapsMode": adGenIpVlanVcEncapsMode,
       "adGenIpVlanVcPBits": adGenIpVlanVcPBits,
       "adGenIpVlanVcManualAddrAging": adGenIpVlanVcManualAddrAging,
       "adGenIpVlanVcPPPoERelay": adGenIpVlanVcPPPoERelay,
       "adGenIpVlanVcIntermedAgent": adGenIpVlanVcIntermedAgent,
       "adGenIpVlanVcDhcpRelay": adGenIpVlanVcDhcpRelay,
       "adGenIpVlanVcOption82Insert": adGenIpVlanVcOption82Insert,
       "adGenIpVlanVcLearnedIpAddrAgingMethod": adGenIpVlanVcLearnedIpAddrAgingMethod,
       "adGenIpVlanVcIgmpProcessing": adGenIpVlanVcIgmpProcessing,
       "adGenIpVlanVcIgmpVersion": adGenIpVlanVcIgmpVersion,
       "adGenIpVlanVcLastMemberQueryInterval": adGenIpVlanVcLastMemberQueryInterval,
       "adGenIpVlanVcLastMemberQueryCount": adGenIpVlanVcLastMemberQueryCount,
       "adGenIpVlanVcImmediateLeave": adGenIpVlanVcImmediateLeave,
       "adGenIpVlanVcMaxAllowedMcastSessions": adGenIpVlanVcMaxAllowedMcastSessions,
       "adGenIpVlanVcL2L4Classifier": adGenIpVlanVcL2L4Classifier,
       "adGenIpVlanVcL2L4Value": adGenIpVlanVcL2L4Value,
       "adGenIpVlanVcMapProfileRowStatus": adGenIpVlanVcMapProfileRowStatus,
       "adGenIpVlanVcDhcpTrustedInterface": adGenIpVlanVcDhcpTrustedInterface,
       "adGenIpVlanVcDhcpPPPoERemoteId": adGenIpVlanVcDhcpPPPoERemoteId,
       "adGenIpVlanVcDhcpPPPoELoopCharacteristics": adGenIpVlanVcDhcpPPPoELoopCharacteristics,
       "adGenIpVlanVcDhcpPPPoECircuitIdFormat": adGenIpVlanVcDhcpPPPoECircuitIdFormat,
       "adGenIpVlanVcPPPoASessionTimeout": adGenIpVlanVcPPPoASessionTimeout,
       "adGenIpVlanVcCtagVID": adGenIpVlanVcCtagVID,
       "adGenIpVlanVcCtagPbitsMethod": adGenIpVlanVcCtagPbitsMethod,
       "adGenIpVlanVcCtagPbitsValue": adGenIpVlanVcCtagPbitsValue,
       "adGenIpVlanVcMulticastVlanVID": adGenIpVlanVcMulticastVlanVID,
       "adGenIpVlanVcMulticastVlanUpstreamPriority": adGenIpVlanVcMulticastVlanUpstreamPriority,
       "adGenIpVlanVcMulticastDownstreamVlanVID": adGenIpVlanVcMulticastDownstreamVlanVID,
       "adGenIpVlanVcDownstreamPolicer": adGenIpVlanVcDownstreamPolicer,
       "adGenIpVlanVcDownstreamPolicerCIR": adGenIpVlanVcDownstreamPolicerCIR,
       "adGenIpVlanVcDownstreamPolicerCBS": adGenIpVlanVcDownstreamPolicerCBS,
       "adGenIpVlanVcDownstreamPolicerEIR": adGenIpVlanVcDownstreamPolicerEIR,
       "adGenIpVlanVcDownstreamPolicerEBS": adGenIpVlanVcDownstreamPolicerEBS,
       "adGenIpVlanVcUpstreamPolicer": adGenIpVlanVcUpstreamPolicer,
       "adGenIpVlanVcUpstreamPolicerCIR": adGenIpVlanVcUpstreamPolicerCIR,
       "adGenIpVlanVcUpstreamPolicerCBS": adGenIpVlanVcUpstreamPolicerCBS,
       "adGenIpVlanVcUpstreamPolicerEIR": adGenIpVlanVcUpstreamPolicerEIR,
       "adGenIpVlanVcUpstreamPolicerEBS": adGenIpVlanVcUpstreamPolicerEBS,
       "adGenIpVlanVcMCastSessionControlStartIP": adGenIpVlanVcMCastSessionControlStartIP,
       "adGenIpVlanVcMCastSessionControlEndIP": adGenIpVlanVcMCastSessionControlEndIP,
       "adGenIpVlanVcMCastSessionControlBitrate": adGenIpVlanVcMCastSessionControlBitrate,
       "adGenIpVlanVcPolicerStatus": adGenIpVlanVcPolicerStatus,
       "adGenIpVlanVcUpstreamMACDAFilter": adGenIpVlanVcUpstreamMACDAFilter,
       "adGenIpVlanVcIgmpRouterIP": adGenIpVlanVcIgmpRouterIP,
       "adGenIpPortProfileTable": adGenIpPortProfileTable,
       "adGenIpPortProfileEntry": adGenIpPortProfileEntry,
       "adGenIpPortProfileName": adGenIpPortProfileName,
       "adGenIpPortNetTrafficTags": adGenIpPortNetTrafficTags,
       "adGenIpPortNetworkModel": adGenIpPortNetworkModel,
       "adGenIpPortSTagVID": adGenIpPortSTagVID,
       "adGenIpPortSTagPBitsMethod": adGenIpPortSTagPBitsMethod,
       "adGenIpPortSTagPBitsValue": adGenIpPortSTagPBitsValue,
       "adGenIpPortMaxMacAddr": adGenIpPortMaxMacAddr,
       "adGenIpPortLearnAndLockAddr": adGenIpPortLearnAndLockAddr,
       "adGenIpPortIgmpLimit": adGenIpPortIgmpLimit,
       "adGenIpPortIgmpLockout": adGenIpPortIgmpLockout,
       "adGenIpPortArpLimit": adGenIpPortArpLimit,
       "adGenIpPortArpLockout": adGenIpPortArpLockout,
       "adGenIpPortDhcpLimit": adGenIpPortDhcpLimit,
       "adGenIpPortDhcpLockout": adGenIpPortDhcpLockout,
       "adGenIpPortPppoeLimit": adGenIpPortPppoeLimit,
       "adGenIpPortPppoeLockout": adGenIpPortPppoeLockout,
       "adGenIpPortMcastBcastLimit": adGenIpPortMcastBcastLimit,
       "adGenIpPortMcastBcastLockout": adGenIpPortMcastBcastLockout,
       "adGenIpPortUcastExceptionLimit": adGenIpPortUcastExceptionLimit,
       "adGenIpPortUcastExceptionLockout": adGenIpPortUcastExceptionLockout,
       "adGenIpPortProfileRowStatus": adGenIpPortProfileRowStatus,
       "adGenIpVlanPropertiesTable": adGenIpVlanPropertiesTable,
       "adGenIpVlanPropertiesEntry": adGenIpVlanPropertiesEntry,
       "adGenIpVlanPropName": adGenIpVlanPropName,
       "adGenIpSysProvTable": adGenIpSysProvTable,
       "adGenIpSysProvEntry": adGenIpSysProvEntry,
       "adGenIpSysProvMgmtVID": adGenIpSysProvMgmtVID,
       "adGenIpSysProvMgmtTagEnable": adGenIpSysProvMgmtTagEnable,
       "adGenIpSysProvMgmtPBits": adGenIpSysProvMgmtPBits,
       "adGenIpSysProvMacAgingTimeout": adGenIpSysProvMacAgingTimeout,
       "adGenIpSysProvIgmpVID": adGenIpSysProvIgmpVID,
       "adGenIpSysProvIgmpTagEnable": adGenIpSysProvIgmpTagEnable,
       "adGenIpSysProvIgmpPBits": adGenIpSysProvIgmpPBits,
       "adGenIpSysProvIgmpHostIP": adGenIpSysProvIgmpHostIP,
       "adGenIpVlanAndPortProvTable": adGenIpVlanAndPortProvTable,
       "adGenIpVlanAndPortProvEntry": adGenIpVlanAndPortProvEntry,
       "adGenIpAccessPortVlanMemRowStatus": adGenIpAccessPortVlanMemRowStatus,
       "adGenIpStatus": adGenIpStatus,
       "adGenIpVlanAndPortStatusTable": adGenIpVlanAndPortStatusTable,
       "adGenIpVlanAndPortStatusEntry": adGenIpVlanAndPortStatusEntry,
       "adGenIpConfVlanMapping": adGenIpConfVlanMapping}
)
