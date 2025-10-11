# SNMP MIB module (ARICENT-ESAT-CFG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-ESAT-CFG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:49 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsEsat = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88)
)
if mibBuilder.loadTexts:
    fsEsat.setRevisions(
        ("2014-06-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _FsEsatSystemControl_Type(Integer32):
    """Custom type fsEsatSystemControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_FsEsatSystemControl_Type.__name__ = "Integer32"
_FsEsatSystemControl_Object = MibScalar
fsEsatSystemControl = _FsEsatSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 1),
    _FsEsatSystemControl_Type()
)
fsEsatSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatSystemControl.setStatus("current")


class _FsEsatTraceOption_Type(Integer32):
    """Custom type fsEsatTraceOption based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsEsatTraceOption_Type.__name__ = "Integer32"
_FsEsatTraceOption_Object = MibScalar
fsEsatTraceOption = _FsEsatTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 2),
    _FsEsatTraceOption_Type()
)
fsEsatTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatTraceOption.setStatus("current")
_FsEsatSlaTable_Object = MibTable
fsEsatSlaTable = _FsEsatSlaTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 3)
)
if mibBuilder.loadTexts:
    fsEsatSlaTable.setStatus("current")
_FsEsatSlaEntry_Object = MibTableRow
fsEsatSlaEntry = _FsEsatSlaEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 3, 1)
)
fsEsatSlaEntry.setIndexNames(
    (0, "ARICENT-ESAT-CFG-MIB", "fsEsatSlaId"),
)
if mibBuilder.loadTexts:
    fsEsatSlaEntry.setStatus("current")


class _FsEsatSlaId_Type(Unsigned32):
    """Custom type fsEsatSlaId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsEsatSlaId_Type.__name__ = "Unsigned32"
_FsEsatSlaId_Object = MibTableColumn
fsEsatSlaId = _FsEsatSlaId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 3, 1, 1),
    _FsEsatSlaId_Type()
)
fsEsatSlaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsEsatSlaId.setStatus("current")
_FsEsatSlaIfIndex_Type = InterfaceIndex
_FsEsatSlaIfIndex_Object = MibTableColumn
fsEsatSlaIfIndex = _FsEsatSlaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 3, 1, 2),
    _FsEsatSlaIfIndex_Type()
)
fsEsatSlaIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatSlaIfIndex.setStatus("current")
_FsEsatSlaEvcIndex_Type = VlanId
_FsEsatSlaEvcIndex_Object = MibTableColumn
fsEsatSlaEvcIndex = _FsEsatSlaEvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 3, 1, 3),
    _FsEsatSlaEvcIndex_Type()
)
fsEsatSlaEvcIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatSlaEvcIndex.setStatus("current")
_FsEsatSlaMEG_Type = Unsigned32
_FsEsatSlaMEG_Object = MibTableColumn
fsEsatSlaMEG = _FsEsatSlaMEG_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 3, 1, 4),
    _FsEsatSlaMEG_Type()
)
fsEsatSlaMEG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatSlaMEG.setStatus("current")
_FsEsatSlaME_Type = Unsigned32
_FsEsatSlaME_Object = MibTableColumn
fsEsatSlaME = _FsEsatSlaME_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 3, 1, 5),
    _FsEsatSlaME_Type()
)
fsEsatSlaME.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatSlaME.setStatus("current")


class _FsEsatSlaMEP_Type(Unsigned32):
    """Custom type fsEsatSlaMEP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_FsEsatSlaMEP_Type.__name__ = "Unsigned32"
_FsEsatSlaMEP_Object = MibTableColumn
fsEsatSlaMEP = _FsEsatSlaMEP_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 3, 1, 6),
    _FsEsatSlaMEP_Type()
)
fsEsatSlaMEP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatSlaMEP.setStatus("current")


class _FsEsatSlaRateStep_Type(Integer32):
    """Custom type fsEsatSlaRateStep based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_FsEsatSlaRateStep_Type.__name__ = "Integer32"
_FsEsatSlaRateStep_Object = MibTableColumn
fsEsatSlaRateStep = _FsEsatSlaRateStep_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 3, 1, 7),
    _FsEsatSlaRateStep_Type()
)
fsEsatSlaRateStep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatSlaRateStep.setStatus("current")


class _FsEsatSlaFreqDelay_Type(Integer32):
    """Custom type fsEsatSlaFreqDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_FsEsatSlaFreqDelay_Type.__name__ = "Integer32"
_FsEsatSlaFreqDelay_Object = MibTableColumn
fsEsatSlaFreqDelay = _FsEsatSlaFreqDelay_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 3, 1, 8),
    _FsEsatSlaFreqDelay_Type()
)
fsEsatSlaFreqDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatSlaFreqDelay.setStatus("current")


class _FsEsatSlaDuration_Type(Integer32):
    """Custom type fsEsatSlaDuration based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_FsEsatSlaDuration_Type.__name__ = "Integer32"
_FsEsatSlaDuration_Object = MibTableColumn
fsEsatSlaDuration = _FsEsatSlaDuration_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 3, 1, 9),
    _FsEsatSlaDuration_Type()
)
fsEsatSlaDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatSlaDuration.setStatus("current")


class _FsEsatSlaDirection_Type(Integer32):
    """Custom type fsEsatSlaDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 2))
    )


_FsEsatSlaDirection_Type.__name__ = "Integer32"
_FsEsatSlaDirection_Object = MibTableColumn
fsEsatSlaDirection = _FsEsatSlaDirection_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 3, 1, 10),
    _FsEsatSlaDirection_Type()
)
fsEsatSlaDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatSlaDirection.setStatus("current")


class _FsEsatSlaTrafProfileId_Type(Integer32):
    """Custom type fsEsatSlaTrafProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsEsatSlaTrafProfileId_Type.__name__ = "Integer32"
_FsEsatSlaTrafProfileId_Object = MibTableColumn
fsEsatSlaTrafProfileId = _FsEsatSlaTrafProfileId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 3, 1, 11),
    _FsEsatSlaTrafProfileId_Type()
)
fsEsatSlaTrafProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatSlaTrafProfileId.setStatus("current")


class _FsEsatSlaSacId_Type(Integer32):
    """Custom type fsEsatSlaSacId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsEsatSlaSacId_Type.__name__ = "Integer32"
_FsEsatSlaSacId_Object = MibTableColumn
fsEsatSlaSacId = _FsEsatSlaSacId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 3, 1, 12),
    _FsEsatSlaSacId_Type()
)
fsEsatSlaSacId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatSlaSacId.setStatus("current")


class _FsEsatSlaStatus_Type(Integer32):
    """Custom type fsEsatSlaStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_FsEsatSlaStatus_Type.__name__ = "Integer32"
_FsEsatSlaStatus_Object = MibTableColumn
fsEsatSlaStatus = _FsEsatSlaStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 3, 1, 13),
    _FsEsatSlaStatus_Type()
)
fsEsatSlaStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatSlaStatus.setStatus("current")
_FsEsatSlaRowStatus_Type = RowStatus
_FsEsatSlaRowStatus_Object = MibTableColumn
fsEsatSlaRowStatus = _FsEsatSlaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 3, 1, 14),
    _FsEsatSlaRowStatus_Type()
)
fsEsatSlaRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatSlaRowStatus.setStatus("current")
_FsEsatTrafProfTable_Object = MibTable
fsEsatTrafProfTable = _FsEsatTrafProfTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 4)
)
if mibBuilder.loadTexts:
    fsEsatTrafProfTable.setStatus("current")
_FsEsatTrafProfEntry_Object = MibTableRow
fsEsatTrafProfEntry = _FsEsatTrafProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 4, 1)
)
fsEsatTrafProfEntry.setIndexNames(
    (0, "ARICENT-ESAT-CFG-MIB", "fsEsatTrafProfId"),
)
if mibBuilder.loadTexts:
    fsEsatTrafProfEntry.setStatus("current")


class _FsEsatTrafProfId_Type(Unsigned32):
    """Custom type fsEsatTrafProfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsEsatTrafProfId_Type.__name__ = "Unsigned32"
_FsEsatTrafProfId_Object = MibTableColumn
fsEsatTrafProfId = _FsEsatTrafProfId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 4, 1, 1),
    _FsEsatTrafProfId_Type()
)
fsEsatTrafProfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsEsatTrafProfId.setStatus("current")


class _FsEsatTrafProfDir_Type(Integer32):
    """Custom type fsEsatTrafProfDir based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 2))
    )


_FsEsatTrafProfDir_Type.__name__ = "Integer32"
_FsEsatTrafProfDir_Object = MibTableColumn
fsEsatTrafProfDir = _FsEsatTrafProfDir_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 4, 1, 2),
    _FsEsatTrafProfDir_Type()
)
fsEsatTrafProfDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatTrafProfDir.setStatus("current")


class _FsEsatTrafProfTagType_Type(Integer32):
    """Custom type fsEsatTrafProfTagType based on Integer32"""
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
        *(("untagged", 1),
          ("singletagged", 2),
          ("doubletagged", 3),
          ("prioritytagged", 4))
    )


_FsEsatTrafProfTagType_Type.__name__ = "Integer32"
_FsEsatTrafProfTagType_Object = MibTableColumn
fsEsatTrafProfTagType = _FsEsatTrafProfTagType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 4, 1, 3),
    _FsEsatTrafProfTagType_Type()
)
fsEsatTrafProfTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatTrafProfTagType.setStatus("current")
_FsEsatTrafProfInVlan_Type = VlanId
_FsEsatTrafProfInVlan_Object = MibTableColumn
fsEsatTrafProfInVlan = _FsEsatTrafProfInVlan_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 4, 1, 4),
    _FsEsatTrafProfInVlan_Type()
)
fsEsatTrafProfInVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatTrafProfInVlan.setStatus("current")
_FsEsatTrafProfOutVlan_Type = VlanId
_FsEsatTrafProfOutVlan_Object = MibTableColumn
fsEsatTrafProfOutVlan = _FsEsatTrafProfOutVlan_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 4, 1, 5),
    _FsEsatTrafProfOutVlan_Type()
)
fsEsatTrafProfOutVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatTrafProfOutVlan.setStatus("current")


class _FsEsatTrafProfInCos_Type(Integer32):
    """Custom type fsEsatTrafProfInCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsEsatTrafProfInCos_Type.__name__ = "Integer32"
_FsEsatTrafProfInCos_Object = MibTableColumn
fsEsatTrafProfInCos = _FsEsatTrafProfInCos_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 4, 1, 6),
    _FsEsatTrafProfInCos_Type()
)
fsEsatTrafProfInCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatTrafProfInCos.setStatus("current")


class _FsEsatTrafProfOutCos_Type(Integer32):
    """Custom type fsEsatTrafProfOutCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsEsatTrafProfOutCos_Type.__name__ = "Integer32"
_FsEsatTrafProfOutCos_Object = MibTableColumn
fsEsatTrafProfOutCos = _FsEsatTrafProfOutCos_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 4, 1, 7),
    _FsEsatTrafProfOutCos_Type()
)
fsEsatTrafProfOutCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatTrafProfOutCos.setStatus("current")


class _FsEsatTrafProfPktSize_Type(Integer32):
    """Custom type fsEsatTrafProfPktSize based on Integer32"""
    defaultValue = 512

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1518),
    )


_FsEsatTrafProfPktSize_Type.__name__ = "Integer32"
_FsEsatTrafProfPktSize_Object = MibTableColumn
fsEsatTrafProfPktSize = _FsEsatTrafProfPktSize_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 4, 1, 8),
    _FsEsatTrafProfPktSize_Type()
)
fsEsatTrafProfPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatTrafProfPktSize.setStatus("current")
_FsEsatTrafProfSrcMac_Type = MacAddress
_FsEsatTrafProfSrcMac_Object = MibTableColumn
fsEsatTrafProfSrcMac = _FsEsatTrafProfSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 4, 1, 9),
    _FsEsatTrafProfSrcMac_Type()
)
fsEsatTrafProfSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatTrafProfSrcMac.setStatus("current")
_FsEsatTrafProfDestMac_Type = MacAddress
_FsEsatTrafProfDestMac_Object = MibTableColumn
fsEsatTrafProfDestMac = _FsEsatTrafProfDestMac_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 4, 1, 10),
    _FsEsatTrafProfDestMac_Type()
)
fsEsatTrafProfDestMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatTrafProfDestMac.setStatus("current")


class _FsEsatTrafProfPayload_Type(OctetString):
    """Custom type fsEsatTrafProfPayload based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FsEsatTrafProfPayload_Type.__name__ = "OctetString"
_FsEsatTrafProfPayload_Object = MibTableColumn
fsEsatTrafProfPayload = _FsEsatTrafProfPayload_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 4, 1, 11),
    _FsEsatTrafProfPayload_Type()
)
fsEsatTrafProfPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatTrafProfPayload.setStatus("current")
_FsEsatTrafProfRowStatus_Type = RowStatus
_FsEsatTrafProfRowStatus_Object = MibTableColumn
fsEsatTrafProfRowStatus = _FsEsatTrafProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 4, 1, 12),
    _FsEsatTrafProfRowStatus_Type()
)
fsEsatTrafProfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatTrafProfRowStatus.setStatus("current")
_FsEsatSacTable_Object = MibTable
fsEsatSacTable = _FsEsatSacTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 5)
)
if mibBuilder.loadTexts:
    fsEsatSacTable.setStatus("current")
_FsEsatSacEntry_Object = MibTableRow
fsEsatSacEntry = _FsEsatSacEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 5, 1)
)
fsEsatSacEntry.setIndexNames(
    (0, "ARICENT-ESAT-CFG-MIB", "fsEsatSacId"),
)
if mibBuilder.loadTexts:
    fsEsatSacEntry.setStatus("current")


class _FsEsatSacId_Type(Unsigned32):
    """Custom type fsEsatSacId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsEsatSacId_Type.__name__ = "Unsigned32"
_FsEsatSacId_Object = MibTableColumn
fsEsatSacId = _FsEsatSacId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 5, 1, 1),
    _FsEsatSacId_Type()
)
fsEsatSacId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsEsatSacId.setStatus("current")
_FsEsatSacInfoRate_Type = Integer32
_FsEsatSacInfoRate_Object = MibTableColumn
fsEsatSacInfoRate = _FsEsatSacInfoRate_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 5, 1, 2),
    _FsEsatSacInfoRate_Type()
)
fsEsatSacInfoRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatSacInfoRate.setStatus("current")


class _FsEsatSacFrLossRatio_Type(Integer32):
    """Custom type fsEsatSacFrLossRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsEsatSacFrLossRatio_Type.__name__ = "Integer32"
_FsEsatSacFrLossRatio_Object = MibTableColumn
fsEsatSacFrLossRatio = _FsEsatSacFrLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 5, 1, 3),
    _FsEsatSacFrLossRatio_Type()
)
fsEsatSacFrLossRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatSacFrLossRatio.setStatus("current")
_FsEsatSacFrTxDelay_Type = Integer32
_FsEsatSacFrTxDelay_Object = MibTableColumn
fsEsatSacFrTxDelay = _FsEsatSacFrTxDelay_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 5, 1, 4),
    _FsEsatSacFrTxDelay_Type()
)
fsEsatSacFrTxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatSacFrTxDelay.setStatus("current")
_FsEsatSacFrDelayVar_Type = Integer32
_FsEsatSacFrDelayVar_Object = MibTableColumn
fsEsatSacFrDelayVar = _FsEsatSacFrDelayVar_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 5, 1, 5),
    _FsEsatSacFrDelayVar_Type()
)
fsEsatSacFrDelayVar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatSacFrDelayVar.setStatus("current")
_FsEsatSacRowStatus_Type = RowStatus
_FsEsatSacRowStatus_Object = MibTableColumn
fsEsatSacRowStatus = _FsEsatSacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 5, 1, 6),
    _FsEsatSacRowStatus_Type()
)
fsEsatSacRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEsatSacRowStatus.setStatus("current")
_FsEsatStatsTable_Object = MibTable
fsEsatStatsTable = _FsEsatStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6)
)
if mibBuilder.loadTexts:
    fsEsatStatsTable.setStatus("current")
_FsEsatStatsEntry_Object = MibTableRow
fsEsatStatsEntry = _FsEsatStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1)
)
fsEsatStatsEntry.setIndexNames(
    (0, "ARICENT-ESAT-CFG-MIB", "fsEsatSlaId"),
    (0, "ARICENT-ESAT-CFG-MIB", "fsEsatStatsStepId"),
)
if mibBuilder.loadTexts:
    fsEsatStatsEntry.setStatus("current")


class _FsEsatStatsStepId_Type(Integer32):
    """Custom type fsEsatStatsStepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FsEsatStatsStepId_Type.__name__ = "Integer32"
_FsEsatStatsStepId_Object = MibTableColumn
fsEsatStatsStepId = _FsEsatStatsStepId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 1),
    _FsEsatStatsStepId_Type()
)
fsEsatStatsStepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsEsatStatsStepId.setStatus("current")


class _FsEsatStatsResult_Type(Integer32):
    """Custom type fsEsatStatsResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("fail", 2))
    )


_FsEsatStatsResult_Type.__name__ = "Integer32"
_FsEsatStatsResult_Object = MibTableColumn
fsEsatStatsResult = _FsEsatStatsResult_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 2),
    _FsEsatStatsResult_Type()
)
fsEsatStatsResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEsatStatsResult.setStatus("current")
_FsEsatStatsDuration_Type = Unsigned32
_FsEsatStatsDuration_Object = MibTableColumn
fsEsatStatsDuration = _FsEsatStatsDuration_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 3),
    _FsEsatStatsDuration_Type()
)
fsEsatStatsDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEsatStatsDuration.setStatus("current")
_FsEsatStatsTxPkts_Type = Unsigned32
_FsEsatStatsTxPkts_Object = MibTableColumn
fsEsatStatsTxPkts = _FsEsatStatsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 4),
    _FsEsatStatsTxPkts_Type()
)
fsEsatStatsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEsatStatsTxPkts.setStatus("current")
_FsEsatStatsTxBytes_Type = Counter64
_FsEsatStatsTxBytes_Object = MibTableColumn
fsEsatStatsTxBytes = _FsEsatStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 5),
    _FsEsatStatsTxBytes_Type()
)
fsEsatStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEsatStatsTxBytes.setStatus("current")
_FsEsatStatsRxPkts_Type = Unsigned32
_FsEsatStatsRxPkts_Object = MibTableColumn
fsEsatStatsRxPkts = _FsEsatStatsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 6),
    _FsEsatStatsRxPkts_Type()
)
fsEsatStatsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEsatStatsRxPkts.setStatus("current")
_FsEsatStatsRxBytes_Type = Counter64
_FsEsatStatsRxBytes_Object = MibTableColumn
fsEsatStatsRxBytes = _FsEsatStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 7),
    _FsEsatStatsRxBytes_Type()
)
fsEsatStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEsatStatsRxBytes.setStatus("current")
_FsEsatStatsIrMin_Type = Integer32
_FsEsatStatsIrMin_Object = MibTableColumn
fsEsatStatsIrMin = _FsEsatStatsIrMin_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 8),
    _FsEsatStatsIrMin_Type()
)
fsEsatStatsIrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEsatStatsIrMin.setStatus("current")
_FsEsatStatsIrMean_Type = Integer32
_FsEsatStatsIrMean_Object = MibTableColumn
fsEsatStatsIrMean = _FsEsatStatsIrMean_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 9),
    _FsEsatStatsIrMean_Type()
)
fsEsatStatsIrMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEsatStatsIrMean.setStatus("current")
_FsEsatStatsIrMax_Type = Integer32
_FsEsatStatsIrMax_Object = MibTableColumn
fsEsatStatsIrMax = _FsEsatStatsIrMax_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 10),
    _FsEsatStatsIrMax_Type()
)
fsEsatStatsIrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEsatStatsIrMax.setStatus("current")
_FsEsatStatsFrLossCnt_Type = Integer32
_FsEsatStatsFrLossCnt_Object = MibTableColumn
fsEsatStatsFrLossCnt = _FsEsatStatsFrLossCnt_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 11),
    _FsEsatStatsFrLossCnt_Type()
)
fsEsatStatsFrLossCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEsatStatsFrLossCnt.setStatus("current")
_FsEsatStatsFrLossRatio_Type = Integer32
_FsEsatStatsFrLossRatio_Object = MibTableColumn
fsEsatStatsFrLossRatio = _FsEsatStatsFrLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 12),
    _FsEsatStatsFrLossRatio_Type()
)
fsEsatStatsFrLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEsatStatsFrLossRatio.setStatus("current")
_FsEsatStatsFrTxDelayMin_Type = Integer32
_FsEsatStatsFrTxDelayMin_Object = MibTableColumn
fsEsatStatsFrTxDelayMin = _FsEsatStatsFrTxDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 13),
    _FsEsatStatsFrTxDelayMin_Type()
)
fsEsatStatsFrTxDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEsatStatsFrTxDelayMin.setStatus("current")
_FsEsatStatsFrTxDelayMean_Type = Integer32
_FsEsatStatsFrTxDelayMean_Object = MibTableColumn
fsEsatStatsFrTxDelayMean = _FsEsatStatsFrTxDelayMean_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 14),
    _FsEsatStatsFrTxDelayMean_Type()
)
fsEsatStatsFrTxDelayMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEsatStatsFrTxDelayMean.setStatus("current")
_FsEsatStatsFrTxDelayMax_Type = Integer32
_FsEsatStatsFrTxDelayMax_Object = MibTableColumn
fsEsatStatsFrTxDelayMax = _FsEsatStatsFrTxDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 15),
    _FsEsatStatsFrTxDelayMax_Type()
)
fsEsatStatsFrTxDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEsatStatsFrTxDelayMax.setStatus("current")
_FsEsatStatsFrDelayVarMin_Type = Integer32
_FsEsatStatsFrDelayVarMin_Object = MibTableColumn
fsEsatStatsFrDelayVarMin = _FsEsatStatsFrDelayVarMin_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 16),
    _FsEsatStatsFrDelayVarMin_Type()
)
fsEsatStatsFrDelayVarMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEsatStatsFrDelayVarMin.setStatus("current")
_FsEsatStatsFrDelayVarMean_Type = Integer32
_FsEsatStatsFrDelayVarMean_Object = MibTableColumn
fsEsatStatsFrDelayVarMean = _FsEsatStatsFrDelayVarMean_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 17),
    _FsEsatStatsFrDelayVarMean_Type()
)
fsEsatStatsFrDelayVarMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEsatStatsFrDelayVarMean.setStatus("current")
_FsEsatStatsFrDelayVarMax_Type = Integer32
_FsEsatStatsFrDelayVarMax_Object = MibTableColumn
fsEsatStatsFrDelayVarMax = _FsEsatStatsFrDelayVarMax_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 18),
    _FsEsatStatsFrDelayVarMax_Type()
)
fsEsatStatsFrDelayVarMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEsatStatsFrDelayVarMax.setStatus("current")
_FsEsatStatsPortStateCounter_Type = Integer32
_FsEsatStatsPortStateCounter_Object = MibTableColumn
fsEsatStatsPortStateCounter = _FsEsatStatsPortStateCounter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 88, 6, 1, 19),
    _FsEsatStatsPortStateCounter_Type()
)
fsEsatStatsPortStateCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEsatStatsPortStateCounter.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-ESAT-CFG-MIB",
    **{"fsEsat": fsEsat,
       "fsEsatSystemControl": fsEsatSystemControl,
       "fsEsatTraceOption": fsEsatTraceOption,
       "fsEsatSlaTable": fsEsatSlaTable,
       "fsEsatSlaEntry": fsEsatSlaEntry,
       "fsEsatSlaId": fsEsatSlaId,
       "fsEsatSlaIfIndex": fsEsatSlaIfIndex,
       "fsEsatSlaEvcIndex": fsEsatSlaEvcIndex,
       "fsEsatSlaMEG": fsEsatSlaMEG,
       "fsEsatSlaME": fsEsatSlaME,
       "fsEsatSlaMEP": fsEsatSlaMEP,
       "fsEsatSlaRateStep": fsEsatSlaRateStep,
       "fsEsatSlaFreqDelay": fsEsatSlaFreqDelay,
       "fsEsatSlaDuration": fsEsatSlaDuration,
       "fsEsatSlaDirection": fsEsatSlaDirection,
       "fsEsatSlaTrafProfileId": fsEsatSlaTrafProfileId,
       "fsEsatSlaSacId": fsEsatSlaSacId,
       "fsEsatSlaStatus": fsEsatSlaStatus,
       "fsEsatSlaRowStatus": fsEsatSlaRowStatus,
       "fsEsatTrafProfTable": fsEsatTrafProfTable,
       "fsEsatTrafProfEntry": fsEsatTrafProfEntry,
       "fsEsatTrafProfId": fsEsatTrafProfId,
       "fsEsatTrafProfDir": fsEsatTrafProfDir,
       "fsEsatTrafProfTagType": fsEsatTrafProfTagType,
       "fsEsatTrafProfInVlan": fsEsatTrafProfInVlan,
       "fsEsatTrafProfOutVlan": fsEsatTrafProfOutVlan,
       "fsEsatTrafProfInCos": fsEsatTrafProfInCos,
       "fsEsatTrafProfOutCos": fsEsatTrafProfOutCos,
       "fsEsatTrafProfPktSize": fsEsatTrafProfPktSize,
       "fsEsatTrafProfSrcMac": fsEsatTrafProfSrcMac,
       "fsEsatTrafProfDestMac": fsEsatTrafProfDestMac,
       "fsEsatTrafProfPayload": fsEsatTrafProfPayload,
       "fsEsatTrafProfRowStatus": fsEsatTrafProfRowStatus,
       "fsEsatSacTable": fsEsatSacTable,
       "fsEsatSacEntry": fsEsatSacEntry,
       "fsEsatSacId": fsEsatSacId,
       "fsEsatSacInfoRate": fsEsatSacInfoRate,
       "fsEsatSacFrLossRatio": fsEsatSacFrLossRatio,
       "fsEsatSacFrTxDelay": fsEsatSacFrTxDelay,
       "fsEsatSacFrDelayVar": fsEsatSacFrDelayVar,
       "fsEsatSacRowStatus": fsEsatSacRowStatus,
       "fsEsatStatsTable": fsEsatStatsTable,
       "fsEsatStatsEntry": fsEsatStatsEntry,
       "fsEsatStatsStepId": fsEsatStatsStepId,
       "fsEsatStatsResult": fsEsatStatsResult,
       "fsEsatStatsDuration": fsEsatStatsDuration,
       "fsEsatStatsTxPkts": fsEsatStatsTxPkts,
       "fsEsatStatsTxBytes": fsEsatStatsTxBytes,
       "fsEsatStatsRxPkts": fsEsatStatsRxPkts,
       "fsEsatStatsRxBytes": fsEsatStatsRxBytes,
       "fsEsatStatsIrMin": fsEsatStatsIrMin,
       "fsEsatStatsIrMean": fsEsatStatsIrMean,
       "fsEsatStatsIrMax": fsEsatStatsIrMax,
       "fsEsatStatsFrLossCnt": fsEsatStatsFrLossCnt,
       "fsEsatStatsFrLossRatio": fsEsatStatsFrLossRatio,
       "fsEsatStatsFrTxDelayMin": fsEsatStatsFrTxDelayMin,
       "fsEsatStatsFrTxDelayMean": fsEsatStatsFrTxDelayMean,
       "fsEsatStatsFrTxDelayMax": fsEsatStatsFrTxDelayMax,
       "fsEsatStatsFrDelayVarMin": fsEsatStatsFrDelayVarMin,
       "fsEsatStatsFrDelayVarMean": fsEsatStatsFrDelayVarMean,
       "fsEsatStatsFrDelayVarMax": fsEsatStatsFrDelayVarMax,
       "fsEsatStatsPortStateCounter": fsEsatStatsPortStateCounter}
)
