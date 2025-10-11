# SNMP MIB module (SUPERMICRO-MPLS-RSVP-TE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-MPLS-RSVP-TE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:03:35 2025
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
 StorageType,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

fsMplsRsvpTeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2)
)
if mibBuilder.loadTexts:
    fsMplsRsvpTeMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MplsLsrIdentifier(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4



class AtmVpIdentifier(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



class AtmVcIdentifier(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_FsMplsRsvpTeObjects_ObjectIdentity = ObjectIdentity
fsMplsRsvpTeObjects = _FsMplsRsvpTeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1)
)
_FsMplsRsvpTeIfTable_Object = MibTable
fsMplsRsvpTeIfTable = _FsMplsRsvpTeIfTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfTable.setStatus("current")
_FsMplsRsvpTeIfEntry_Object = MibTableRow
fsMplsRsvpTeIfEntry = _FsMplsRsvpTeIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 1, 1)
)
fsMplsRsvpTeIfEntry.setIndexNames(
    (0, "SUPERMICRO-MPLS-RSVP-TE-MIB", "fsMplsRsvpTeIfIndex"),
)
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfEntry.setStatus("current")
_FsMplsRsvpTeIfIndex_Type = InterfaceIndex
_FsMplsRsvpTeIfIndex_Object = MibTableColumn
fsMplsRsvpTeIfIndex = _FsMplsRsvpTeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 1, 1, 1),
    _FsMplsRsvpTeIfIndex_Type()
)
fsMplsRsvpTeIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfIndex.setStatus("current")


class _FsMplsRsvpTeIfLblSpace_Type(Integer32):
    """Custom type fsMplsRsvpTeIfLblSpace based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("perPlatform", 1),
          ("perInterface", 2))
    )


_FsMplsRsvpTeIfLblSpace_Type.__name__ = "Integer32"
_FsMplsRsvpTeIfLblSpace_Object = MibTableColumn
fsMplsRsvpTeIfLblSpace = _FsMplsRsvpTeIfLblSpace_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 1, 1, 2),
    _FsMplsRsvpTeIfLblSpace_Type()
)
fsMplsRsvpTeIfLblSpace.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfLblSpace.setStatus("current")


class _FsMplsRsvpTeIfLblType_Type(Integer32):
    """Custom type fsMplsRsvpTeIfLblType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rsvpTeIfEth", 1),
          ("rsvpTeIfAtm", 2),
          ("rsvpTeIfFr", 3))
    )


_FsMplsRsvpTeIfLblType_Type.__name__ = "Integer32"
_FsMplsRsvpTeIfLblType_Object = MibTableColumn
fsMplsRsvpTeIfLblType = _FsMplsRsvpTeIfLblType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 1, 1, 3),
    _FsMplsRsvpTeIfLblType_Type()
)
fsMplsRsvpTeIfLblType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfLblType.setStatus("current")


class _FsMplsRsvpTeAtmMergeCap_Type(Integer32):
    """Custom type fsMplsRsvpTeAtmMergeCap based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("vcMerge", 2))
    )


_FsMplsRsvpTeAtmMergeCap_Type.__name__ = "Integer32"
_FsMplsRsvpTeAtmMergeCap_Object = MibTableColumn
fsMplsRsvpTeAtmMergeCap = _FsMplsRsvpTeAtmMergeCap_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 1, 1, 4),
    _FsMplsRsvpTeAtmMergeCap_Type()
)
fsMplsRsvpTeAtmMergeCap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsRsvpTeAtmMergeCap.setStatus("current")


class _FsMplsRsvpTeAtmVcDirection_Type(Integer32):
    """Custom type fsMplsRsvpTeAtmVcDirection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("biDirectional", 0),
          ("oddUniDirectional", 1),
          ("evenUniDirectional", 2))
    )


_FsMplsRsvpTeAtmVcDirection_Type.__name__ = "Integer32"
_FsMplsRsvpTeAtmVcDirection_Object = MibTableColumn
fsMplsRsvpTeAtmVcDirection = _FsMplsRsvpTeAtmVcDirection_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 1, 1, 5),
    _FsMplsRsvpTeAtmVcDirection_Type()
)
fsMplsRsvpTeAtmVcDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsRsvpTeAtmVcDirection.setStatus("current")


class _FsMplsRsvpTeAtmMinVpi_Type(AtmVpIdentifier):
    """Custom type fsMplsRsvpTeAtmMinVpi based on AtmVpIdentifier"""
    defaultValue = 0


_FsMplsRsvpTeAtmMinVpi_Type.__name__ = "AtmVpIdentifier"
_FsMplsRsvpTeAtmMinVpi_Object = MibTableColumn
fsMplsRsvpTeAtmMinVpi = _FsMplsRsvpTeAtmMinVpi_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 1, 1, 6),
    _FsMplsRsvpTeAtmMinVpi_Type()
)
fsMplsRsvpTeAtmMinVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsRsvpTeAtmMinVpi.setStatus("current")


class _FsMplsRsvpTeAtmMinVci_Type(AtmVcIdentifier):
    """Custom type fsMplsRsvpTeAtmMinVci based on AtmVcIdentifier"""
    defaultValue = 33


_FsMplsRsvpTeAtmMinVci_Type.__name__ = "AtmVcIdentifier"
_FsMplsRsvpTeAtmMinVci_Object = MibTableColumn
fsMplsRsvpTeAtmMinVci = _FsMplsRsvpTeAtmMinVci_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 1, 1, 7),
    _FsMplsRsvpTeAtmMinVci_Type()
)
fsMplsRsvpTeAtmMinVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsRsvpTeAtmMinVci.setStatus("current")


class _FsMplsRsvpTeAtmMaxVpi_Type(AtmVpIdentifier):
    """Custom type fsMplsRsvpTeAtmMaxVpi based on AtmVpIdentifier"""
    defaultValue = 0


_FsMplsRsvpTeAtmMaxVpi_Type.__name__ = "AtmVpIdentifier"
_FsMplsRsvpTeAtmMaxVpi_Object = MibTableColumn
fsMplsRsvpTeAtmMaxVpi = _FsMplsRsvpTeAtmMaxVpi_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 1, 1, 8),
    _FsMplsRsvpTeAtmMaxVpi_Type()
)
fsMplsRsvpTeAtmMaxVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsRsvpTeAtmMaxVpi.setStatus("current")


class _FsMplsRsvpTeAtmMaxVci_Type(AtmVcIdentifier):
    """Custom type fsMplsRsvpTeAtmMaxVci based on AtmVcIdentifier"""
    defaultValue = 160


_FsMplsRsvpTeAtmMaxVci_Type.__name__ = "AtmVcIdentifier"
_FsMplsRsvpTeAtmMaxVci_Object = MibTableColumn
fsMplsRsvpTeAtmMaxVci = _FsMplsRsvpTeAtmMaxVci_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 1, 1, 9),
    _FsMplsRsvpTeAtmMaxVci_Type()
)
fsMplsRsvpTeAtmMaxVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsRsvpTeAtmMaxVci.setStatus("current")


class _FsMplsRsvpTeIfMtu_Type(Integer32):
    """Custom type fsMplsRsvpTeIfMtu based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 4096),
    )


_FsMplsRsvpTeIfMtu_Type.__name__ = "Integer32"
_FsMplsRsvpTeIfMtu_Object = MibTableColumn
fsMplsRsvpTeIfMtu = _FsMplsRsvpTeIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 1, 1, 10),
    _FsMplsRsvpTeIfMtu_Type()
)
fsMplsRsvpTeIfMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfMtu.setStatus("current")
_FsMplsRsvpTeIfUdpNbrs_Type = Counter32
_FsMplsRsvpTeIfUdpNbrs_Object = MibTableColumn
fsMplsRsvpTeIfUdpNbrs = _FsMplsRsvpTeIfUdpNbrs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 1, 1, 11),
    _FsMplsRsvpTeIfUdpNbrs_Type()
)
fsMplsRsvpTeIfUdpNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfUdpNbrs.setStatus("current")
_FsMplsRsvpTeIfIpNbrs_Type = Counter32
_FsMplsRsvpTeIfIpNbrs_Object = MibTableColumn
fsMplsRsvpTeIfIpNbrs = _FsMplsRsvpTeIfIpNbrs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 1, 1, 12),
    _FsMplsRsvpTeIfIpNbrs_Type()
)
fsMplsRsvpTeIfIpNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfIpNbrs.setStatus("current")
_FsMplsRsvpTeIfNbrs_Type = Counter32
_FsMplsRsvpTeIfNbrs_Object = MibTableColumn
fsMplsRsvpTeIfNbrs = _FsMplsRsvpTeIfNbrs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 1, 1, 13),
    _FsMplsRsvpTeIfNbrs_Type()
)
fsMplsRsvpTeIfNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNbrs.setStatus("current")


class _FsMplsRsvpTeIfRefreshMultiple_Type(Integer32):
    """Custom type fsMplsRsvpTeIfRefreshMultiple based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_FsMplsRsvpTeIfRefreshMultiple_Type.__name__ = "Integer32"
_FsMplsRsvpTeIfRefreshMultiple_Object = MibTableColumn
fsMplsRsvpTeIfRefreshMultiple = _FsMplsRsvpTeIfRefreshMultiple_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 1, 1, 14),
    _FsMplsRsvpTeIfRefreshMultiple_Type()
)
fsMplsRsvpTeIfRefreshMultiple.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfRefreshMultiple.setStatus("current")


class _FsMplsRsvpTeIfTTL_Type(Integer32):
    """Custom type fsMplsRsvpTeIfTTL based on Integer32"""
    defaultValue = 64


_FsMplsRsvpTeIfTTL_Type.__name__ = "Integer32"
_FsMplsRsvpTeIfTTL_Object = MibTableColumn
fsMplsRsvpTeIfTTL = _FsMplsRsvpTeIfTTL_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 1, 1, 15),
    _FsMplsRsvpTeIfTTL_Type()
)
fsMplsRsvpTeIfTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfTTL.setStatus("current")


class _FsMplsRsvpTeIfRefreshInterval_Type(TimeInterval):
    """Custom type fsMplsRsvpTeIfRefreshInterval based on TimeInterval"""
    defaultValue = 30000


_FsMplsRsvpTeIfRefreshInterval_Type.__name__ = "TimeInterval"
_FsMplsRsvpTeIfRefreshInterval_Object = MibTableColumn
fsMplsRsvpTeIfRefreshInterval = _FsMplsRsvpTeIfRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 1, 1, 16),
    _FsMplsRsvpTeIfRefreshInterval_Type()
)
fsMplsRsvpTeIfRefreshInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfRefreshInterval.setStatus("current")


class _FsMplsRsvpTeIfRouteDelay_Type(TimeInterval):
    """Custom type fsMplsRsvpTeIfRouteDelay based on TimeInterval"""
    defaultValue = 2


_FsMplsRsvpTeIfRouteDelay_Type.__name__ = "TimeInterval"
_FsMplsRsvpTeIfRouteDelay_Object = MibTableColumn
fsMplsRsvpTeIfRouteDelay = _FsMplsRsvpTeIfRouteDelay_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 1, 1, 17),
    _FsMplsRsvpTeIfRouteDelay_Type()
)
fsMplsRsvpTeIfRouteDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfRouteDelay.setStatus("current")


class _FsMplsRsvpTeIfUdpRequired_Type(TruthValue):
    """Custom type fsMplsRsvpTeIfUdpRequired based on TruthValue"""
    defaultValue = 2


_FsMplsRsvpTeIfUdpRequired_Type.__name__ = "TruthValue"
_FsMplsRsvpTeIfUdpRequired_Object = MibTableColumn
fsMplsRsvpTeIfUdpRequired = _FsMplsRsvpTeIfUdpRequired_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 1, 1, 18),
    _FsMplsRsvpTeIfUdpRequired_Type()
)
fsMplsRsvpTeIfUdpRequired.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfUdpRequired.setStatus("current")


class _FsMplsRsvpTeIfHelloSupported_Type(TruthValue):
    """Custom type fsMplsRsvpTeIfHelloSupported based on TruthValue"""
    defaultValue = 2


_FsMplsRsvpTeIfHelloSupported_Type.__name__ = "TruthValue"
_FsMplsRsvpTeIfHelloSupported_Object = MibTableColumn
fsMplsRsvpTeIfHelloSupported = _FsMplsRsvpTeIfHelloSupported_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 1, 1, 19),
    _FsMplsRsvpTeIfHelloSupported_Type()
)
fsMplsRsvpTeIfHelloSupported.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfHelloSupported.setStatus("current")


class _FsMplsRsvpTeIfLinkAttr_Type(Integer32):
    """Custom type fsMplsRsvpTeIfLinkAttr based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMplsRsvpTeIfLinkAttr_Type.__name__ = "Integer32"
_FsMplsRsvpTeIfLinkAttr_Object = MibTableColumn
fsMplsRsvpTeIfLinkAttr = _FsMplsRsvpTeIfLinkAttr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 1, 1, 20),
    _FsMplsRsvpTeIfLinkAttr_Type()
)
fsMplsRsvpTeIfLinkAttr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfLinkAttr.setStatus("current")
_FsMplsRsvpTeIfStatus_Type = RowStatus
_FsMplsRsvpTeIfStatus_Object = MibTableColumn
fsMplsRsvpTeIfStatus = _FsMplsRsvpTeIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 1, 1, 21),
    _FsMplsRsvpTeIfStatus_Type()
)
fsMplsRsvpTeIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfStatus.setStatus("current")
_FsMplsRsvpTeIfPlrId_Type = MplsLsrIdentifier
_FsMplsRsvpTeIfPlrId_Object = MibTableColumn
fsMplsRsvpTeIfPlrId = _FsMplsRsvpTeIfPlrId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 1, 1, 22),
    _FsMplsRsvpTeIfPlrId_Type()
)
fsMplsRsvpTeIfPlrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfPlrId.setStatus("current")
_FsMplsRsvpTeIfAvoidNodeId_Type = MplsLsrIdentifier
_FsMplsRsvpTeIfAvoidNodeId_Object = MibTableColumn
fsMplsRsvpTeIfAvoidNodeId = _FsMplsRsvpTeIfAvoidNodeId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 1, 1, 23),
    _FsMplsRsvpTeIfAvoidNodeId_Type()
)
fsMplsRsvpTeIfAvoidNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfAvoidNodeId.setStatus("current")


class _FsMplsRsvpTeIfStorageType_Type(StorageType):
    """Custom type fsMplsRsvpTeIfStorageType based on StorageType"""
    defaultValue = 3


_FsMplsRsvpTeIfStorageType_Type.__name__ = "StorageType"
_FsMplsRsvpTeIfStorageType_Object = MibTableColumn
fsMplsRsvpTeIfStorageType = _FsMplsRsvpTeIfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 1, 1, 24),
    _FsMplsRsvpTeIfStorageType_Type()
)
fsMplsRsvpTeIfStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfStorageType.setStatus("current")
_FsMplsRsvpTeIfStatsTable_Object = MibTable
fsMplsRsvpTeIfStatsTable = _FsMplsRsvpTeIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2)
)
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfStatsTable.setStatus("current")
_FsMplsRsvpTeIfStatsEntry_Object = MibTableRow
fsMplsRsvpTeIfStatsEntry = _FsMplsRsvpTeIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfStatsEntry.setStatus("current")
_FsMplsRsvpTeIfNumTnls_Type = Counter32
_FsMplsRsvpTeIfNumTnls_Object = MibTableColumn
fsMplsRsvpTeIfNumTnls = _FsMplsRsvpTeIfNumTnls_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 1),
    _FsMplsRsvpTeIfNumTnls_Type()
)
fsMplsRsvpTeIfNumTnls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumTnls.setStatus("current")
_FsMplsRsvpTeIfNumMsgSent_Type = Counter32
_FsMplsRsvpTeIfNumMsgSent_Object = MibTableColumn
fsMplsRsvpTeIfNumMsgSent = _FsMplsRsvpTeIfNumMsgSent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 2),
    _FsMplsRsvpTeIfNumMsgSent_Type()
)
fsMplsRsvpTeIfNumMsgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumMsgSent.setStatus("current")
_FsMplsRsvpTeIfNumMsgRcvd_Type = Counter32
_FsMplsRsvpTeIfNumMsgRcvd_Object = MibTableColumn
fsMplsRsvpTeIfNumMsgRcvd = _FsMplsRsvpTeIfNumMsgRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 3),
    _FsMplsRsvpTeIfNumMsgRcvd_Type()
)
fsMplsRsvpTeIfNumMsgRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumMsgRcvd.setStatus("current")
_FsMplsRsvpTeIfNumHelloSent_Type = Counter32
_FsMplsRsvpTeIfNumHelloSent_Object = MibTableColumn
fsMplsRsvpTeIfNumHelloSent = _FsMplsRsvpTeIfNumHelloSent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 4),
    _FsMplsRsvpTeIfNumHelloSent_Type()
)
fsMplsRsvpTeIfNumHelloSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumHelloSent.setStatus("current")
_FsMplsRsvpTeIfNumHelloRcvd_Type = Counter32
_FsMplsRsvpTeIfNumHelloRcvd_Object = MibTableColumn
fsMplsRsvpTeIfNumHelloRcvd = _FsMplsRsvpTeIfNumHelloRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 5),
    _FsMplsRsvpTeIfNumHelloRcvd_Type()
)
fsMplsRsvpTeIfNumHelloRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumHelloRcvd.setStatus("current")
_FsMplsRsvpTeIfNumPathErrSent_Type = Counter32
_FsMplsRsvpTeIfNumPathErrSent_Object = MibTableColumn
fsMplsRsvpTeIfNumPathErrSent = _FsMplsRsvpTeIfNumPathErrSent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 6),
    _FsMplsRsvpTeIfNumPathErrSent_Type()
)
fsMplsRsvpTeIfNumPathErrSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumPathErrSent.setStatus("current")
_FsMplsRsvpTeIfNumPathErrRcvd_Type = Counter32
_FsMplsRsvpTeIfNumPathErrRcvd_Object = MibTableColumn
fsMplsRsvpTeIfNumPathErrRcvd = _FsMplsRsvpTeIfNumPathErrRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 7),
    _FsMplsRsvpTeIfNumPathErrRcvd_Type()
)
fsMplsRsvpTeIfNumPathErrRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumPathErrRcvd.setStatus("current")
_FsMplsRsvpTeIfNumPathTearSent_Type = Counter32
_FsMplsRsvpTeIfNumPathTearSent_Object = MibTableColumn
fsMplsRsvpTeIfNumPathTearSent = _FsMplsRsvpTeIfNumPathTearSent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 8),
    _FsMplsRsvpTeIfNumPathTearSent_Type()
)
fsMplsRsvpTeIfNumPathTearSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumPathTearSent.setStatus("current")
_FsMplsRsvpTeIfNumPathTearRcvd_Type = Counter32
_FsMplsRsvpTeIfNumPathTearRcvd_Object = MibTableColumn
fsMplsRsvpTeIfNumPathTearRcvd = _FsMplsRsvpTeIfNumPathTearRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 9),
    _FsMplsRsvpTeIfNumPathTearRcvd_Type()
)
fsMplsRsvpTeIfNumPathTearRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumPathTearRcvd.setStatus("current")
_FsMplsRsvpTeIfNumResvErrSent_Type = Counter32
_FsMplsRsvpTeIfNumResvErrSent_Object = MibTableColumn
fsMplsRsvpTeIfNumResvErrSent = _FsMplsRsvpTeIfNumResvErrSent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 10),
    _FsMplsRsvpTeIfNumResvErrSent_Type()
)
fsMplsRsvpTeIfNumResvErrSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumResvErrSent.setStatus("current")
_FsMplsRsvpTeIfNumResvErrRcvd_Type = Counter32
_FsMplsRsvpTeIfNumResvErrRcvd_Object = MibTableColumn
fsMplsRsvpTeIfNumResvErrRcvd = _FsMplsRsvpTeIfNumResvErrRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 11),
    _FsMplsRsvpTeIfNumResvErrRcvd_Type()
)
fsMplsRsvpTeIfNumResvErrRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumResvErrRcvd.setStatus("current")
_FsMplsRsvpTeIfNumResvTearSent_Type = Counter32
_FsMplsRsvpTeIfNumResvTearSent_Object = MibTableColumn
fsMplsRsvpTeIfNumResvTearSent = _FsMplsRsvpTeIfNumResvTearSent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 12),
    _FsMplsRsvpTeIfNumResvTearSent_Type()
)
fsMplsRsvpTeIfNumResvTearSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumResvTearSent.setStatus("current")
_FsMplsRsvpTeIfNumResvTearRcvd_Type = Counter32
_FsMplsRsvpTeIfNumResvTearRcvd_Object = MibTableColumn
fsMplsRsvpTeIfNumResvTearRcvd = _FsMplsRsvpTeIfNumResvTearRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 13),
    _FsMplsRsvpTeIfNumResvTearRcvd_Type()
)
fsMplsRsvpTeIfNumResvTearRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumResvTearRcvd.setStatus("current")
_FsMplsRsvpTeIfNumResvConfSent_Type = Counter32
_FsMplsRsvpTeIfNumResvConfSent_Object = MibTableColumn
fsMplsRsvpTeIfNumResvConfSent = _FsMplsRsvpTeIfNumResvConfSent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 14),
    _FsMplsRsvpTeIfNumResvConfSent_Type()
)
fsMplsRsvpTeIfNumResvConfSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumResvConfSent.setStatus("current")
_FsMplsRsvpTeIfNumResvConfRcvd_Type = Counter32
_FsMplsRsvpTeIfNumResvConfRcvd_Object = MibTableColumn
fsMplsRsvpTeIfNumResvConfRcvd = _FsMplsRsvpTeIfNumResvConfRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 15),
    _FsMplsRsvpTeIfNumResvConfRcvd_Type()
)
fsMplsRsvpTeIfNumResvConfRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumResvConfRcvd.setStatus("current")
_FsMplsRsvpTeIfNumBundleMsgSent_Type = Counter32
_FsMplsRsvpTeIfNumBundleMsgSent_Object = MibTableColumn
fsMplsRsvpTeIfNumBundleMsgSent = _FsMplsRsvpTeIfNumBundleMsgSent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 16),
    _FsMplsRsvpTeIfNumBundleMsgSent_Type()
)
fsMplsRsvpTeIfNumBundleMsgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumBundleMsgSent.setStatus("current")
_FsMplsRsvpTeIfNumBundleMsgRcvd_Type = Counter32
_FsMplsRsvpTeIfNumBundleMsgRcvd_Object = MibTableColumn
fsMplsRsvpTeIfNumBundleMsgRcvd = _FsMplsRsvpTeIfNumBundleMsgRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 17),
    _FsMplsRsvpTeIfNumBundleMsgRcvd_Type()
)
fsMplsRsvpTeIfNumBundleMsgRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumBundleMsgRcvd.setStatus("current")
_FsMplsRsvpTeIfNumSRefreshMsgSent_Type = Counter32
_FsMplsRsvpTeIfNumSRefreshMsgSent_Object = MibTableColumn
fsMplsRsvpTeIfNumSRefreshMsgSent = _FsMplsRsvpTeIfNumSRefreshMsgSent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 18),
    _FsMplsRsvpTeIfNumSRefreshMsgSent_Type()
)
fsMplsRsvpTeIfNumSRefreshMsgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumSRefreshMsgSent.setStatus("current")
_FsMplsRsvpTeIfNumSRefreshMsgRcvd_Type = Counter32
_FsMplsRsvpTeIfNumSRefreshMsgRcvd_Object = MibTableColumn
fsMplsRsvpTeIfNumSRefreshMsgRcvd = _FsMplsRsvpTeIfNumSRefreshMsgRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 19),
    _FsMplsRsvpTeIfNumSRefreshMsgRcvd_Type()
)
fsMplsRsvpTeIfNumSRefreshMsgRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumSRefreshMsgRcvd.setStatus("current")
_FsMplsRsvpTeIfNumPathSent_Type = Counter32
_FsMplsRsvpTeIfNumPathSent_Object = MibTableColumn
fsMplsRsvpTeIfNumPathSent = _FsMplsRsvpTeIfNumPathSent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 20),
    _FsMplsRsvpTeIfNumPathSent_Type()
)
fsMplsRsvpTeIfNumPathSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumPathSent.setStatus("current")
_FsMplsRsvpTeIfNumPathRcvd_Type = Counter32
_FsMplsRsvpTeIfNumPathRcvd_Object = MibTableColumn
fsMplsRsvpTeIfNumPathRcvd = _FsMplsRsvpTeIfNumPathRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 21),
    _FsMplsRsvpTeIfNumPathRcvd_Type()
)
fsMplsRsvpTeIfNumPathRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumPathRcvd.setStatus("current")
_FsMplsRsvpTeIfNumResvSent_Type = Counter32
_FsMplsRsvpTeIfNumResvSent_Object = MibTableColumn
fsMplsRsvpTeIfNumResvSent = _FsMplsRsvpTeIfNumResvSent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 22),
    _FsMplsRsvpTeIfNumResvSent_Type()
)
fsMplsRsvpTeIfNumResvSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumResvSent.setStatus("current")
_FsMplsRsvpTeIfNumResvRcvd_Type = Counter32
_FsMplsRsvpTeIfNumResvRcvd_Object = MibTableColumn
fsMplsRsvpTeIfNumResvRcvd = _FsMplsRsvpTeIfNumResvRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 23),
    _FsMplsRsvpTeIfNumResvRcvd_Type()
)
fsMplsRsvpTeIfNumResvRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumResvRcvd.setStatus("current")
_FsMplsRsvpTeIfNumNotifyMsgSent_Type = Counter32
_FsMplsRsvpTeIfNumNotifyMsgSent_Object = MibTableColumn
fsMplsRsvpTeIfNumNotifyMsgSent = _FsMplsRsvpTeIfNumNotifyMsgSent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 24),
    _FsMplsRsvpTeIfNumNotifyMsgSent_Type()
)
fsMplsRsvpTeIfNumNotifyMsgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumNotifyMsgSent.setStatus("current")
_FsMplsRsvpTeIfNumNotifyMsgRcvd_Type = Counter32
_FsMplsRsvpTeIfNumNotifyMsgRcvd_Object = MibTableColumn
fsMplsRsvpTeIfNumNotifyMsgRcvd = _FsMplsRsvpTeIfNumNotifyMsgRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 25),
    _FsMplsRsvpTeIfNumNotifyMsgRcvd_Type()
)
fsMplsRsvpTeIfNumNotifyMsgRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumNotifyMsgRcvd.setStatus("current")
_FsMplsRsvpTeIfNumRecoveryPathSent_Type = Counter32
_FsMplsRsvpTeIfNumRecoveryPathSent_Object = MibTableColumn
fsMplsRsvpTeIfNumRecoveryPathSent = _FsMplsRsvpTeIfNumRecoveryPathSent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 26),
    _FsMplsRsvpTeIfNumRecoveryPathSent_Type()
)
fsMplsRsvpTeIfNumRecoveryPathSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumRecoveryPathSent.setStatus("current")
_FsMplsRsvpTeIfNumRecoveryPathRcvd_Type = Counter32
_FsMplsRsvpTeIfNumRecoveryPathRcvd_Object = MibTableColumn
fsMplsRsvpTeIfNumRecoveryPathRcvd = _FsMplsRsvpTeIfNumRecoveryPathRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 27),
    _FsMplsRsvpTeIfNumRecoveryPathRcvd_Type()
)
fsMplsRsvpTeIfNumRecoveryPathRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumRecoveryPathRcvd.setStatus("current")
_FsMplsRsvpTeIfNumPathSentWithRecoveryLbl_Type = Counter32
_FsMplsRsvpTeIfNumPathSentWithRecoveryLbl_Object = MibTableColumn
fsMplsRsvpTeIfNumPathSentWithRecoveryLbl = _FsMplsRsvpTeIfNumPathSentWithRecoveryLbl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 28),
    _FsMplsRsvpTeIfNumPathSentWithRecoveryLbl_Type()
)
fsMplsRsvpTeIfNumPathSentWithRecoveryLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumPathSentWithRecoveryLbl.setStatus("current")
_FsMplsRsvpTeIfNumPathRcvdWithRecoveryLbl_Type = Counter32
_FsMplsRsvpTeIfNumPathRcvdWithRecoveryLbl_Object = MibTableColumn
fsMplsRsvpTeIfNumPathRcvdWithRecoveryLbl = _FsMplsRsvpTeIfNumPathRcvdWithRecoveryLbl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 29),
    _FsMplsRsvpTeIfNumPathRcvdWithRecoveryLbl_Type()
)
fsMplsRsvpTeIfNumPathRcvdWithRecoveryLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumPathRcvdWithRecoveryLbl.setStatus("current")
_FsMplsRsvpTeIfNumPathSentWithSuggestedLbl_Type = Counter32
_FsMplsRsvpTeIfNumPathSentWithSuggestedLbl_Object = MibTableColumn
fsMplsRsvpTeIfNumPathSentWithSuggestedLbl = _FsMplsRsvpTeIfNumPathSentWithSuggestedLbl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 30),
    _FsMplsRsvpTeIfNumPathSentWithSuggestedLbl_Type()
)
fsMplsRsvpTeIfNumPathSentWithSuggestedLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumPathSentWithSuggestedLbl.setStatus("current")
_FsMplsRsvpTeIfNumPathRcvdWithSuggestedLbl_Type = Counter32
_FsMplsRsvpTeIfNumPathRcvdWithSuggestedLbl_Object = MibTableColumn
fsMplsRsvpTeIfNumPathRcvdWithSuggestedLbl = _FsMplsRsvpTeIfNumPathRcvdWithSuggestedLbl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 31),
    _FsMplsRsvpTeIfNumPathRcvdWithSuggestedLbl_Type()
)
fsMplsRsvpTeIfNumPathRcvdWithSuggestedLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumPathRcvdWithSuggestedLbl.setStatus("current")
_FsMplsRsvpTeIfNumHelloSentWithRestartCap_Type = Counter32
_FsMplsRsvpTeIfNumHelloSentWithRestartCap_Object = MibTableColumn
fsMplsRsvpTeIfNumHelloSentWithRestartCap = _FsMplsRsvpTeIfNumHelloSentWithRestartCap_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 32),
    _FsMplsRsvpTeIfNumHelloSentWithRestartCap_Type()
)
fsMplsRsvpTeIfNumHelloSentWithRestartCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumHelloSentWithRestartCap.setStatus("current")
_FsMplsRsvpTeIfNumHelloRcvdWithRestartCap_Type = Counter32
_FsMplsRsvpTeIfNumHelloRcvdWithRestartCap_Object = MibTableColumn
fsMplsRsvpTeIfNumHelloRcvdWithRestartCap = _FsMplsRsvpTeIfNumHelloRcvdWithRestartCap_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 33),
    _FsMplsRsvpTeIfNumHelloRcvdWithRestartCap_Type()
)
fsMplsRsvpTeIfNumHelloRcvdWithRestartCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumHelloRcvdWithRestartCap.setStatus("current")
_FsMplsRsvpTeIfNumHelloSentWithCapability_Type = Counter32
_FsMplsRsvpTeIfNumHelloSentWithCapability_Object = MibTableColumn
fsMplsRsvpTeIfNumHelloSentWithCapability = _FsMplsRsvpTeIfNumHelloSentWithCapability_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 34),
    _FsMplsRsvpTeIfNumHelloSentWithCapability_Type()
)
fsMplsRsvpTeIfNumHelloSentWithCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumHelloSentWithCapability.setStatus("current")
_FsMplsRsvpTeIfNumHelloRcvdWithCapability_Type = Counter32
_FsMplsRsvpTeIfNumHelloRcvdWithCapability_Object = MibTableColumn
fsMplsRsvpTeIfNumHelloRcvdWithCapability = _FsMplsRsvpTeIfNumHelloRcvdWithCapability_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 2, 1, 35),
    _FsMplsRsvpTeIfNumHelloRcvdWithCapability_Type()
)
fsMplsRsvpTeIfNumHelloRcvdWithCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeIfNumHelloRcvdWithCapability.setStatus("current")
_FsMplsRsvpTeNbrTable_Object = MibTable
fsMplsRsvpTeNbrTable = _FsMplsRsvpTeNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 3)
)
if mibBuilder.loadTexts:
    fsMplsRsvpTeNbrTable.setStatus("current")
_FsMplsRsvpTeNbrEntry_Object = MibTableRow
fsMplsRsvpTeNbrEntry = _FsMplsRsvpTeNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 3, 1)
)
fsMplsRsvpTeNbrEntry.setIndexNames(
    (0, "SUPERMICRO-MPLS-RSVP-TE-MIB", "fsMplsRsvpTeIfIndex"),
    (0, "SUPERMICRO-MPLS-RSVP-TE-MIB", "fsMplsRsvpTeNbrIfAddr"),
)
if mibBuilder.loadTexts:
    fsMplsRsvpTeNbrEntry.setStatus("current")
_FsMplsRsvpTeNbrIfAddr_Type = IpAddress
_FsMplsRsvpTeNbrIfAddr_Object = MibTableColumn
fsMplsRsvpTeNbrIfAddr = _FsMplsRsvpTeNbrIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 3, 1, 1),
    _FsMplsRsvpTeNbrIfAddr_Type()
)
fsMplsRsvpTeNbrIfAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMplsRsvpTeNbrIfAddr.setStatus("current")


class _FsMplsRsvpTeNbrRRCapable_Type(Integer32):
    """Custom type fsMplsRsvpTeNbrRRCapable based on Integer32"""
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


_FsMplsRsvpTeNbrRRCapable_Type.__name__ = "Integer32"
_FsMplsRsvpTeNbrRRCapable_Object = MibTableColumn
fsMplsRsvpTeNbrRRCapable = _FsMplsRsvpTeNbrRRCapable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 3, 1, 2),
    _FsMplsRsvpTeNbrRRCapable_Type()
)
fsMplsRsvpTeNbrRRCapable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsRsvpTeNbrRRCapable.setStatus("current")


class _FsMplsRsvpTeNbrRRState_Type(Integer32):
    """Custom type fsMplsRsvpTeNbrRRState based on Integer32"""
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


_FsMplsRsvpTeNbrRRState_Type.__name__ = "Integer32"
_FsMplsRsvpTeNbrRRState_Object = MibTableColumn
fsMplsRsvpTeNbrRRState = _FsMplsRsvpTeNbrRRState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 3, 1, 3),
    _FsMplsRsvpTeNbrRRState_Type()
)
fsMplsRsvpTeNbrRRState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeNbrRRState.setStatus("current")


class _FsMplsRsvpTeNbrRMDCapable_Type(Integer32):
    """Custom type fsMplsRsvpTeNbrRMDCapable based on Integer32"""
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


_FsMplsRsvpTeNbrRMDCapable_Type.__name__ = "Integer32"
_FsMplsRsvpTeNbrRMDCapable_Object = MibTableColumn
fsMplsRsvpTeNbrRMDCapable = _FsMplsRsvpTeNbrRMDCapable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 3, 1, 4),
    _FsMplsRsvpTeNbrRMDCapable_Type()
)
fsMplsRsvpTeNbrRMDCapable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsRsvpTeNbrRMDCapable.setStatus("current")


class _FsMplsRsvpTeNbrEncapsType_Type(Integer32):
    """Custom type fsMplsRsvpTeNbrEncapsType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipencap", 1),
          ("udpencap", 2),
          ("both", 3))
    )


_FsMplsRsvpTeNbrEncapsType_Type.__name__ = "Integer32"
_FsMplsRsvpTeNbrEncapsType_Object = MibTableColumn
fsMplsRsvpTeNbrEncapsType = _FsMplsRsvpTeNbrEncapsType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 3, 1, 5),
    _FsMplsRsvpTeNbrEncapsType_Type()
)
fsMplsRsvpTeNbrEncapsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsRsvpTeNbrEncapsType.setStatus("current")


class _FsMplsRsvpTeNbrHelloSupport_Type(Integer32):
    """Custom type fsMplsRsvpTeNbrHelloSupport based on Integer32"""
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


_FsMplsRsvpTeNbrHelloSupport_Type.__name__ = "Integer32"
_FsMplsRsvpTeNbrHelloSupport_Object = MibTableColumn
fsMplsRsvpTeNbrHelloSupport = _FsMplsRsvpTeNbrHelloSupport_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 3, 1, 6),
    _FsMplsRsvpTeNbrHelloSupport_Type()
)
fsMplsRsvpTeNbrHelloSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsRsvpTeNbrHelloSupport.setStatus("current")


class _FsMplsRsvpTeNbrHelloState_Type(Integer32):
    """Custom type fsMplsRsvpTeNbrHelloState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("supported", 1),
          ("notSupported", 2),
          ("supportReset", 3))
    )


_FsMplsRsvpTeNbrHelloState_Type.__name__ = "Integer32"
_FsMplsRsvpTeNbrHelloState_Object = MibTableColumn
fsMplsRsvpTeNbrHelloState = _FsMplsRsvpTeNbrHelloState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 3, 1, 7),
    _FsMplsRsvpTeNbrHelloState_Type()
)
fsMplsRsvpTeNbrHelloState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeNbrHelloState.setStatus("current")


class _FsMplsRsvpTeNbrHelloRelation_Type(Integer32):
    """Custom type fsMplsRsvpTeNbrHelloRelation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_FsMplsRsvpTeNbrHelloRelation_Type.__name__ = "Integer32"
_FsMplsRsvpTeNbrHelloRelation_Object = MibTableColumn
fsMplsRsvpTeNbrHelloRelation = _FsMplsRsvpTeNbrHelloRelation_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 3, 1, 8),
    _FsMplsRsvpTeNbrHelloRelation_Type()
)
fsMplsRsvpTeNbrHelloRelation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeNbrHelloRelation.setStatus("current")
_FsMplsRsvpTeNbrSrcInstInfo_Type = Integer32
_FsMplsRsvpTeNbrSrcInstInfo_Object = MibTableColumn
fsMplsRsvpTeNbrSrcInstInfo = _FsMplsRsvpTeNbrSrcInstInfo_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 3, 1, 9),
    _FsMplsRsvpTeNbrSrcInstInfo_Type()
)
fsMplsRsvpTeNbrSrcInstInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeNbrSrcInstInfo.setStatus("current")
_FsMplsRsvpTeNbrDestInstInfo_Type = Integer32
_FsMplsRsvpTeNbrDestInstInfo_Object = MibTableColumn
fsMplsRsvpTeNbrDestInstInfo = _FsMplsRsvpTeNbrDestInstInfo_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 3, 1, 10),
    _FsMplsRsvpTeNbrDestInstInfo_Type()
)
fsMplsRsvpTeNbrDestInstInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeNbrDestInstInfo.setStatus("current")
_FsMplsRsvpTeNbrCreationTime_Type = TimeStamp
_FsMplsRsvpTeNbrCreationTime_Object = MibTableColumn
fsMplsRsvpTeNbrCreationTime = _FsMplsRsvpTeNbrCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 3, 1, 11),
    _FsMplsRsvpTeNbrCreationTime_Type()
)
fsMplsRsvpTeNbrCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeNbrCreationTime.setStatus("current")
_FsMplsRsvpTeNbrLclRprDetectionTime_Type = TimeStamp
_FsMplsRsvpTeNbrLclRprDetectionTime_Object = MibTableColumn
fsMplsRsvpTeNbrLclRprDetectionTime = _FsMplsRsvpTeNbrLclRprDetectionTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 3, 1, 12),
    _FsMplsRsvpTeNbrLclRprDetectionTime_Type()
)
fsMplsRsvpTeNbrLclRprDetectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeNbrLclRprDetectionTime.setStatus("current")
_FsMplsRsvpTeNbrNumTunnels_Type = Counter32
_FsMplsRsvpTeNbrNumTunnels_Object = MibTableColumn
fsMplsRsvpTeNbrNumTunnels = _FsMplsRsvpTeNbrNumTunnels_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 3, 1, 13),
    _FsMplsRsvpTeNbrNumTunnels_Type()
)
fsMplsRsvpTeNbrNumTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeNbrNumTunnels.setStatus("current")
_FsMplsRsvpTeNbrStatus_Type = RowStatus
_FsMplsRsvpTeNbrStatus_Object = MibTableColumn
fsMplsRsvpTeNbrStatus = _FsMplsRsvpTeNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 3, 1, 14),
    _FsMplsRsvpTeNbrStatus_Type()
)
fsMplsRsvpTeNbrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsRsvpTeNbrStatus.setStatus("current")


class _FsMplsRsvpTeNbrGrRecoveryPathCapability_Type(Bits):
    """Custom type fsMplsRsvpTeNbrGrRecoveryPathCapability based on Bits"""
    namedValues = NamedValues(
        *(("recoveryPathTransmit", 0),
          ("recoveryPathReceive", 1),
          ("recoveryPathSRefresh", 2))
    )

_FsMplsRsvpTeNbrGrRecoveryPathCapability_Type.__name__ = "Bits"
_FsMplsRsvpTeNbrGrRecoveryPathCapability_Object = MibTableColumn
fsMplsRsvpTeNbrGrRecoveryPathCapability = _FsMplsRsvpTeNbrGrRecoveryPathCapability_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 3, 1, 15),
    _FsMplsRsvpTeNbrGrRecoveryPathCapability_Type()
)
fsMplsRsvpTeNbrGrRecoveryPathCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeNbrGrRecoveryPathCapability.setStatus("current")
_FsMplsRsvpTeNbrGrRestartTime_Type = Integer32
_FsMplsRsvpTeNbrGrRestartTime_Object = MibTableColumn
fsMplsRsvpTeNbrGrRestartTime = _FsMplsRsvpTeNbrGrRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 3, 1, 16),
    _FsMplsRsvpTeNbrGrRestartTime_Type()
)
fsMplsRsvpTeNbrGrRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeNbrGrRestartTime.setStatus("current")
_FsMplsRsvpTeNbrGrRecoveryTime_Type = Integer32
_FsMplsRsvpTeNbrGrRecoveryTime_Object = MibTableColumn
fsMplsRsvpTeNbrGrRecoveryTime = _FsMplsRsvpTeNbrGrRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 3, 1, 17),
    _FsMplsRsvpTeNbrGrRecoveryTime_Type()
)
fsMplsRsvpTeNbrGrRecoveryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeNbrGrRecoveryTime.setStatus("current")
_FsMplsRsvpTeNbrGrProgressStatus_Type = Integer32
_FsMplsRsvpTeNbrGrProgressStatus_Object = MibTableColumn
fsMplsRsvpTeNbrGrProgressStatus = _FsMplsRsvpTeNbrGrProgressStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 3, 1, 18),
    _FsMplsRsvpTeNbrGrProgressStatus_Type()
)
fsMplsRsvpTeNbrGrProgressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeNbrGrProgressStatus.setStatus("current")


class _FsMplsRsvpTeNbrStorageType_Type(StorageType):
    """Custom type fsMplsRsvpTeNbrStorageType based on StorageType"""
    defaultValue = 3


_FsMplsRsvpTeNbrStorageType_Type.__name__ = "StorageType"
_FsMplsRsvpTeNbrStorageType_Object = MibTableColumn
fsMplsRsvpTeNbrStorageType = _FsMplsRsvpTeNbrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 1, 3, 1, 19),
    _FsMplsRsvpTeNbrStorageType_Type()
)
fsMplsRsvpTeNbrStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsRsvpTeNbrStorageType.setStatus("current")
_FsMplsRsvpTeGenObjects_ObjectIdentity = ObjectIdentity
fsMplsRsvpTeGenObjects = _FsMplsRsvpTeGenObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2)
)
_FsMplsRsvpTeLsrID_Type = MplsLsrIdentifier
_FsMplsRsvpTeLsrID_Object = MibScalar
fsMplsRsvpTeLsrID = _FsMplsRsvpTeLsrID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 1),
    _FsMplsRsvpTeLsrID_Type()
)
fsMplsRsvpTeLsrID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeLsrID.setStatus("current")


class _FsMplsRsvpTeMaxTnls_Type(Integer32):
    """Custom type fsMplsRsvpTeMaxTnls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMplsRsvpTeMaxTnls_Type.__name__ = "Integer32"
_FsMplsRsvpTeMaxTnls_Object = MibScalar
fsMplsRsvpTeMaxTnls = _FsMplsRsvpTeMaxTnls_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 2),
    _FsMplsRsvpTeMaxTnls_Type()
)
fsMplsRsvpTeMaxTnls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeMaxTnls.setStatus("current")


class _FsMplsRsvpTeMaxErhopsPerTnl_Type(Integer32):
    """Custom type fsMplsRsvpTeMaxErhopsPerTnl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMplsRsvpTeMaxErhopsPerTnl_Type.__name__ = "Integer32"
_FsMplsRsvpTeMaxErhopsPerTnl_Object = MibScalar
fsMplsRsvpTeMaxErhopsPerTnl = _FsMplsRsvpTeMaxErhopsPerTnl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 3),
    _FsMplsRsvpTeMaxErhopsPerTnl_Type()
)
fsMplsRsvpTeMaxErhopsPerTnl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeMaxErhopsPerTnl.setStatus("current")


class _FsMplsRsvpTeMaxActRoutePerTnl_Type(Integer32):
    """Custom type fsMplsRsvpTeMaxActRoutePerTnl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMplsRsvpTeMaxActRoutePerTnl_Type.__name__ = "Integer32"
_FsMplsRsvpTeMaxActRoutePerTnl_Object = MibScalar
fsMplsRsvpTeMaxActRoutePerTnl = _FsMplsRsvpTeMaxActRoutePerTnl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 4),
    _FsMplsRsvpTeMaxActRoutePerTnl_Type()
)
fsMplsRsvpTeMaxActRoutePerTnl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeMaxActRoutePerTnl.setStatus("current")


class _FsMplsRsvpTeMaxIfaces_Type(Integer32):
    """Custom type fsMplsRsvpTeMaxIfaces based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMplsRsvpTeMaxIfaces_Type.__name__ = "Integer32"
_FsMplsRsvpTeMaxIfaces_Object = MibScalar
fsMplsRsvpTeMaxIfaces = _FsMplsRsvpTeMaxIfaces_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 5),
    _FsMplsRsvpTeMaxIfaces_Type()
)
fsMplsRsvpTeMaxIfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeMaxIfaces.setStatus("current")


class _FsMplsRsvpTeMaxNbrs_Type(Integer32):
    """Custom type fsMplsRsvpTeMaxNbrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMplsRsvpTeMaxNbrs_Type.__name__ = "Integer32"
_FsMplsRsvpTeMaxNbrs_Object = MibScalar
fsMplsRsvpTeMaxNbrs = _FsMplsRsvpTeMaxNbrs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 6),
    _FsMplsRsvpTeMaxNbrs_Type()
)
fsMplsRsvpTeMaxNbrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeMaxNbrs.setStatus("current")


class _FsMplsRsvpTeSockSupprtd_Type(TruthValue):
    """Custom type fsMplsRsvpTeSockSupprtd based on TruthValue"""
    defaultValue = 1


_FsMplsRsvpTeSockSupprtd_Type.__name__ = "TruthValue"
_FsMplsRsvpTeSockSupprtd_Object = MibScalar
fsMplsRsvpTeSockSupprtd = _FsMplsRsvpTeSockSupprtd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 7),
    _FsMplsRsvpTeSockSupprtd_Type()
)
fsMplsRsvpTeSockSupprtd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeSockSupprtd.setStatus("current")


class _FsMplsRsvpTeHelloSupprtd_Type(TruthValue):
    """Custom type fsMplsRsvpTeHelloSupprtd based on TruthValue"""
    defaultValue = 2


_FsMplsRsvpTeHelloSupprtd_Type.__name__ = "TruthValue"
_FsMplsRsvpTeHelloSupprtd_Object = MibScalar
fsMplsRsvpTeHelloSupprtd = _FsMplsRsvpTeHelloSupprtd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 8),
    _FsMplsRsvpTeHelloSupprtd_Type()
)
fsMplsRsvpTeHelloSupprtd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeHelloSupprtd.setStatus("current")


class _FsMplsRsvpTeHelloIntervalTime_Type(Integer32):
    """Custom type fsMplsRsvpTeHelloIntervalTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30000),
    )


_FsMplsRsvpTeHelloIntervalTime_Type.__name__ = "Integer32"
_FsMplsRsvpTeHelloIntervalTime_Object = MibScalar
fsMplsRsvpTeHelloIntervalTime = _FsMplsRsvpTeHelloIntervalTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 9),
    _FsMplsRsvpTeHelloIntervalTime_Type()
)
fsMplsRsvpTeHelloIntervalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeHelloIntervalTime.setStatus("current")


class _FsMplsRsvpTeRRCapable_Type(Integer32):
    """Custom type fsMplsRsvpTeRRCapable based on Integer32"""
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


_FsMplsRsvpTeRRCapable_Type.__name__ = "Integer32"
_FsMplsRsvpTeRRCapable_Object = MibScalar
fsMplsRsvpTeRRCapable = _FsMplsRsvpTeRRCapable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 10),
    _FsMplsRsvpTeRRCapable_Type()
)
fsMplsRsvpTeRRCapable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeRRCapable.setStatus("current")


class _FsMplsRsvpTeMsgIdCapable_Type(Integer32):
    """Custom type fsMplsRsvpTeMsgIdCapable based on Integer32"""
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


_FsMplsRsvpTeMsgIdCapable_Type.__name__ = "Integer32"
_FsMplsRsvpTeMsgIdCapable_Object = MibScalar
fsMplsRsvpTeMsgIdCapable = _FsMplsRsvpTeMsgIdCapable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 11),
    _FsMplsRsvpTeMsgIdCapable_Type()
)
fsMplsRsvpTeMsgIdCapable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeMsgIdCapable.setStatus("current")


class _FsMplsRsvpTeRMDPolicyObject_Type(Bits):
    """Custom type fsMplsRsvpTeRMDPolicyObject based on Bits"""
    namedValues = NamedValues(
        *(("path", 0),
          ("resv", 1),
          ("pathErr", 2),
          ("resvErr", 3),
          ("pathTear", 4),
          ("resvTear", 5),
          ("notify", 6))
    )

_FsMplsRsvpTeRMDPolicyObject_Type.__name__ = "Bits"
_FsMplsRsvpTeRMDPolicyObject_Object = MibScalar
fsMplsRsvpTeRMDPolicyObject = _FsMplsRsvpTeRMDPolicyObject_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 12),
    _FsMplsRsvpTeRMDPolicyObject_Type()
)
fsMplsRsvpTeRMDPolicyObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeRMDPolicyObject.setStatus("current")


class _FsMplsRsvpTeGenLblSpaceMinLbl_Type(Integer32):
    """Custom type fsMplsRsvpTeGenLblSpaceMinLbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100001, 160000),
    )


_FsMplsRsvpTeGenLblSpaceMinLbl_Type.__name__ = "Integer32"
_FsMplsRsvpTeGenLblSpaceMinLbl_Object = MibScalar
fsMplsRsvpTeGenLblSpaceMinLbl = _FsMplsRsvpTeGenLblSpaceMinLbl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 13),
    _FsMplsRsvpTeGenLblSpaceMinLbl_Type()
)
fsMplsRsvpTeGenLblSpaceMinLbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeGenLblSpaceMinLbl.setStatus("current")


class _FsMplsRsvpTeGenLblSpaceMaxLbl_Type(Integer32):
    """Custom type fsMplsRsvpTeGenLblSpaceMaxLbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100001, 160000),
    )


_FsMplsRsvpTeGenLblSpaceMaxLbl_Type.__name__ = "Integer32"
_FsMplsRsvpTeGenLblSpaceMaxLbl_Object = MibScalar
fsMplsRsvpTeGenLblSpaceMaxLbl = _FsMplsRsvpTeGenLblSpaceMaxLbl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 14),
    _FsMplsRsvpTeGenLblSpaceMaxLbl_Type()
)
fsMplsRsvpTeGenLblSpaceMaxLbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeGenLblSpaceMaxLbl.setStatus("current")


class _FsMplsRsvpTeGenDebugFlag_Type(Unsigned32):
    """Custom type fsMplsRsvpTeGenDebugFlag based on Unsigned32"""
    defaultValue = 0


_FsMplsRsvpTeGenDebugFlag_Type.__name__ = "Unsigned32"
_FsMplsRsvpTeGenDebugFlag_Object = MibScalar
fsMplsRsvpTeGenDebugFlag = _FsMplsRsvpTeGenDebugFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 15),
    _FsMplsRsvpTeGenDebugFlag_Type()
)
fsMplsRsvpTeGenDebugFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeGenDebugFlag.setStatus("current")


class _FsMplsRsvpTeGenPduDumpLevel_Type(Integer32):
    """Custom type fsMplsRsvpTeGenPduDumpLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("min", 1),
          ("max", 2),
          ("hdr", 4))
    )


_FsMplsRsvpTeGenPduDumpLevel_Type.__name__ = "Integer32"
_FsMplsRsvpTeGenPduDumpLevel_Object = MibScalar
fsMplsRsvpTeGenPduDumpLevel = _FsMplsRsvpTeGenPduDumpLevel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 16),
    _FsMplsRsvpTeGenPduDumpLevel_Type()
)
fsMplsRsvpTeGenPduDumpLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeGenPduDumpLevel.setStatus("current")
_FsMplsRsvpTeGenPduDumpMsgType_Type = Integer32
_FsMplsRsvpTeGenPduDumpMsgType_Object = MibScalar
fsMplsRsvpTeGenPduDumpMsgType = _FsMplsRsvpTeGenPduDumpMsgType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 17),
    _FsMplsRsvpTeGenPduDumpMsgType_Type()
)
fsMplsRsvpTeGenPduDumpMsgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeGenPduDumpMsgType.setStatus("current")


class _FsMplsRsvpTeGenPduDumpDirection_Type(Integer32):
    """Custom type fsMplsRsvpTeGenPduDumpDirection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("in", 1),
          ("out", 2),
          ("inout", 3))
    )


_FsMplsRsvpTeGenPduDumpDirection_Type.__name__ = "Integer32"
_FsMplsRsvpTeGenPduDumpDirection_Object = MibScalar
fsMplsRsvpTeGenPduDumpDirection = _FsMplsRsvpTeGenPduDumpDirection_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 18),
    _FsMplsRsvpTeGenPduDumpDirection_Type()
)
fsMplsRsvpTeGenPduDumpDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeGenPduDumpDirection.setStatus("current")


class _FsMplsRsvpTeOperStatus_Type(Integer32):
    """Custom type fsMplsRsvpTeOperStatus based on Integer32"""
    defaultValue = 2

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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("upinprgrs", 4),
          ("downinprgrs", 5))
    )


_FsMplsRsvpTeOperStatus_Type.__name__ = "Integer32"
_FsMplsRsvpTeOperStatus_Object = MibScalar
fsMplsRsvpTeOperStatus = _FsMplsRsvpTeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 19),
    _FsMplsRsvpTeOperStatus_Type()
)
fsMplsRsvpTeOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeOperStatus.setStatus("current")


class _FsMplsRsvpTeOverRideOption_Type(TruthValue):
    """Custom type fsMplsRsvpTeOverRideOption based on TruthValue"""
    defaultValue = 2


_FsMplsRsvpTeOverRideOption_Type.__name__ = "TruthValue"
_FsMplsRsvpTeOverRideOption_Object = MibScalar
fsMplsRsvpTeOverRideOption = _FsMplsRsvpTeOverRideOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 20),
    _FsMplsRsvpTeOverRideOption_Type()
)
fsMplsRsvpTeOverRideOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeOverRideOption.setStatus("current")


class _FsMplsRsvpTeMinTnlsWithMsgId_Type(Unsigned32):
    """Custom type fsMplsRsvpTeMinTnlsWithMsgId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMplsRsvpTeMinTnlsWithMsgId_Type.__name__ = "Unsigned32"
_FsMplsRsvpTeMinTnlsWithMsgId_Object = MibScalar
fsMplsRsvpTeMinTnlsWithMsgId = _FsMplsRsvpTeMinTnlsWithMsgId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 21),
    _FsMplsRsvpTeMinTnlsWithMsgId_Type()
)
fsMplsRsvpTeMinTnlsWithMsgId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeMinTnlsWithMsgId.setStatus("current")


class _FsMplsRsvpTeNotificationEnabled_Type(Integer32):
    """Custom type fsMplsRsvpTeNotificationEnabled based on Integer32"""
    defaultValue = 1

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


_FsMplsRsvpTeNotificationEnabled_Type.__name__ = "Integer32"
_FsMplsRsvpTeNotificationEnabled_Object = MibScalar
fsMplsRsvpTeNotificationEnabled = _FsMplsRsvpTeNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 22),
    _FsMplsRsvpTeNotificationEnabled_Type()
)
fsMplsRsvpTeNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeNotificationEnabled.setStatus("current")


class _FsMplsRsvpTeNotifyMsgRetransmitIntvl_Type(Unsigned32):
    """Custom type fsMplsRsvpTeNotifyMsgRetransmitIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30000),
    )


_FsMplsRsvpTeNotifyMsgRetransmitIntvl_Type.__name__ = "Unsigned32"
_FsMplsRsvpTeNotifyMsgRetransmitIntvl_Object = MibScalar
fsMplsRsvpTeNotifyMsgRetransmitIntvl = _FsMplsRsvpTeNotifyMsgRetransmitIntvl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 23),
    _FsMplsRsvpTeNotifyMsgRetransmitIntvl_Type()
)
fsMplsRsvpTeNotifyMsgRetransmitIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeNotifyMsgRetransmitIntvl.setStatus("current")


class _FsMplsRsvpTeNotifyMsgRetransmitDecay_Type(Unsigned32):
    """Custom type fsMplsRsvpTeNotifyMsgRetransmitDecay based on Unsigned32"""
    defaultValue = 0


_FsMplsRsvpTeNotifyMsgRetransmitDecay_Type.__name__ = "Unsigned32"
_FsMplsRsvpTeNotifyMsgRetransmitDecay_Object = MibScalar
fsMplsRsvpTeNotifyMsgRetransmitDecay = _FsMplsRsvpTeNotifyMsgRetransmitDecay_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 24),
    _FsMplsRsvpTeNotifyMsgRetransmitDecay_Type()
)
fsMplsRsvpTeNotifyMsgRetransmitDecay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeNotifyMsgRetransmitDecay.setStatus("current")


class _FsMplsRsvpTeNotifyMsgRetransmitLimit_Type(Unsigned32):
    """Custom type fsMplsRsvpTeNotifyMsgRetransmitLimit based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FsMplsRsvpTeNotifyMsgRetransmitLimit_Type.__name__ = "Unsigned32"
_FsMplsRsvpTeNotifyMsgRetransmitLimit_Object = MibScalar
fsMplsRsvpTeNotifyMsgRetransmitLimit = _FsMplsRsvpTeNotifyMsgRetransmitLimit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 25),
    _FsMplsRsvpTeNotifyMsgRetransmitLimit_Type()
)
fsMplsRsvpTeNotifyMsgRetransmitLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeNotifyMsgRetransmitLimit.setStatus("current")


class _FsMplsRsvpTeAdminStatusTimeIntvl_Type(Unsigned32):
    """Custom type fsMplsRsvpTeAdminStatusTimeIntvl based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_FsMplsRsvpTeAdminStatusTimeIntvl_Type.__name__ = "Unsigned32"
_FsMplsRsvpTeAdminStatusTimeIntvl_Object = MibScalar
fsMplsRsvpTeAdminStatusTimeIntvl = _FsMplsRsvpTeAdminStatusTimeIntvl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 26),
    _FsMplsRsvpTeAdminStatusTimeIntvl_Type()
)
fsMplsRsvpTeAdminStatusTimeIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeAdminStatusTimeIntvl.setStatus("current")


class _FsMplsRsvpTePathStateRemovedSupport_Type(Integer32):
    """Custom type fsMplsRsvpTePathStateRemovedSupport based on Integer32"""
    defaultValue = 2

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


_FsMplsRsvpTePathStateRemovedSupport_Type.__name__ = "Integer32"
_FsMplsRsvpTePathStateRemovedSupport_Object = MibScalar
fsMplsRsvpTePathStateRemovedSupport = _FsMplsRsvpTePathStateRemovedSupport_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 27),
    _FsMplsRsvpTePathStateRemovedSupport_Type()
)
fsMplsRsvpTePathStateRemovedSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTePathStateRemovedSupport.setStatus("current")


class _FsMplsRsvpTeLabelSetEnabled_Type(Integer32):
    """Custom type fsMplsRsvpTeLabelSetEnabled based on Integer32"""
    defaultValue = 2

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


_FsMplsRsvpTeLabelSetEnabled_Type.__name__ = "Integer32"
_FsMplsRsvpTeLabelSetEnabled_Object = MibScalar
fsMplsRsvpTeLabelSetEnabled = _FsMplsRsvpTeLabelSetEnabled_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 28),
    _FsMplsRsvpTeLabelSetEnabled_Type()
)
fsMplsRsvpTeLabelSetEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeLabelSetEnabled.setStatus("current")


class _FsMplsRsvpTeAdminStatusCapability_Type(Integer32):
    """Custom type fsMplsRsvpTeAdminStatusCapability based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_FsMplsRsvpTeAdminStatusCapability_Type.__name__ = "Integer32"
_FsMplsRsvpTeAdminStatusCapability_Object = MibScalar
fsMplsRsvpTeAdminStatusCapability = _FsMplsRsvpTeAdminStatusCapability_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 29),
    _FsMplsRsvpTeAdminStatusCapability_Type()
)
fsMplsRsvpTeAdminStatusCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeAdminStatusCapability.setStatus("current")


class _FsMplsRsvpTeGrCapability_Type(Integer32):
    """Custom type fsMplsRsvpTeGrCapability based on Integer32"""
    defaultValue = 1

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
          ("full", 2),
          ("helper", 3))
    )


_FsMplsRsvpTeGrCapability_Type.__name__ = "Integer32"
_FsMplsRsvpTeGrCapability_Object = MibScalar
fsMplsRsvpTeGrCapability = _FsMplsRsvpTeGrCapability_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 30),
    _FsMplsRsvpTeGrCapability_Type()
)
fsMplsRsvpTeGrCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeGrCapability.setStatus("current")


class _FsMplsRsvpTeGrRecoveryPathCapability_Type(Bits):
    """Custom type fsMplsRsvpTeGrRecoveryPathCapability based on Bits"""
    defaultHexValue = ""

    namedValues = NamedValues(
        *(("recoveryPathTransmit", 0),
          ("recoveryPathReceive", 1),
          ("recoveryPathSRefresh", 2))
    )

_FsMplsRsvpTeGrRecoveryPathCapability_Type.__name__ = "Bits"
_FsMplsRsvpTeGrRecoveryPathCapability_Object = MibScalar
fsMplsRsvpTeGrRecoveryPathCapability = _FsMplsRsvpTeGrRecoveryPathCapability_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 31),
    _FsMplsRsvpTeGrRecoveryPathCapability_Type()
)
fsMplsRsvpTeGrRecoveryPathCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeGrRecoveryPathCapability.setStatus("current")


class _FsMplsRsvpTeGrRestartTime_Type(Integer32):
    """Custom type fsMplsRsvpTeGrRestartTime based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_FsMplsRsvpTeGrRestartTime_Type.__name__ = "Integer32"
_FsMplsRsvpTeGrRestartTime_Object = MibScalar
fsMplsRsvpTeGrRestartTime = _FsMplsRsvpTeGrRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 32),
    _FsMplsRsvpTeGrRestartTime_Type()
)
fsMplsRsvpTeGrRestartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeGrRestartTime.setStatus("current")


class _FsMplsRsvpTeGrRecoveryTime_Type(Integer32):
    """Custom type fsMplsRsvpTeGrRecoveryTime based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 480),
    )


_FsMplsRsvpTeGrRecoveryTime_Type.__name__ = "Integer32"
_FsMplsRsvpTeGrRecoveryTime_Object = MibScalar
fsMplsRsvpTeGrRecoveryTime = _FsMplsRsvpTeGrRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 33),
    _FsMplsRsvpTeGrRecoveryTime_Type()
)
fsMplsRsvpTeGrRecoveryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsRsvpTeGrRecoveryTime.setStatus("current")
_FsMplsRsvpTeGrProgressStatus_Type = Integer32
_FsMplsRsvpTeGrProgressStatus_Object = MibScalar
fsMplsRsvpTeGrProgressStatus = _FsMplsRsvpTeGrProgressStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 2, 2, 34),
    _FsMplsRsvpTeGrProgressStatus_Type()
)
fsMplsRsvpTeGrProgressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsRsvpTeGrProgressStatus.setStatus("current")
fsMplsRsvpTeIfEntry.registerAugmentions(
    ("SUPERMICRO-MPLS-RSVP-TE-MIB",
     "fsMplsRsvpTeIfStatsEntry")
)
fsMplsRsvpTeIfStatsEntry.setIndexNames(*fsMplsRsvpTeIfEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-MPLS-RSVP-TE-MIB",
    **{"MplsLsrIdentifier": MplsLsrIdentifier,
       "AtmVpIdentifier": AtmVpIdentifier,
       "AtmVcIdentifier": AtmVcIdentifier,
       "fsMplsRsvpTeMIB": fsMplsRsvpTeMIB,
       "fsMplsRsvpTeObjects": fsMplsRsvpTeObjects,
       "fsMplsRsvpTeIfTable": fsMplsRsvpTeIfTable,
       "fsMplsRsvpTeIfEntry": fsMplsRsvpTeIfEntry,
       "fsMplsRsvpTeIfIndex": fsMplsRsvpTeIfIndex,
       "fsMplsRsvpTeIfLblSpace": fsMplsRsvpTeIfLblSpace,
       "fsMplsRsvpTeIfLblType": fsMplsRsvpTeIfLblType,
       "fsMplsRsvpTeAtmMergeCap": fsMplsRsvpTeAtmMergeCap,
       "fsMplsRsvpTeAtmVcDirection": fsMplsRsvpTeAtmVcDirection,
       "fsMplsRsvpTeAtmMinVpi": fsMplsRsvpTeAtmMinVpi,
       "fsMplsRsvpTeAtmMinVci": fsMplsRsvpTeAtmMinVci,
       "fsMplsRsvpTeAtmMaxVpi": fsMplsRsvpTeAtmMaxVpi,
       "fsMplsRsvpTeAtmMaxVci": fsMplsRsvpTeAtmMaxVci,
       "fsMplsRsvpTeIfMtu": fsMplsRsvpTeIfMtu,
       "fsMplsRsvpTeIfUdpNbrs": fsMplsRsvpTeIfUdpNbrs,
       "fsMplsRsvpTeIfIpNbrs": fsMplsRsvpTeIfIpNbrs,
       "fsMplsRsvpTeIfNbrs": fsMplsRsvpTeIfNbrs,
       "fsMplsRsvpTeIfRefreshMultiple": fsMplsRsvpTeIfRefreshMultiple,
       "fsMplsRsvpTeIfTTL": fsMplsRsvpTeIfTTL,
       "fsMplsRsvpTeIfRefreshInterval": fsMplsRsvpTeIfRefreshInterval,
       "fsMplsRsvpTeIfRouteDelay": fsMplsRsvpTeIfRouteDelay,
       "fsMplsRsvpTeIfUdpRequired": fsMplsRsvpTeIfUdpRequired,
       "fsMplsRsvpTeIfHelloSupported": fsMplsRsvpTeIfHelloSupported,
       "fsMplsRsvpTeIfLinkAttr": fsMplsRsvpTeIfLinkAttr,
       "fsMplsRsvpTeIfStatus": fsMplsRsvpTeIfStatus,
       "fsMplsRsvpTeIfPlrId": fsMplsRsvpTeIfPlrId,
       "fsMplsRsvpTeIfAvoidNodeId": fsMplsRsvpTeIfAvoidNodeId,
       "fsMplsRsvpTeIfStorageType": fsMplsRsvpTeIfStorageType,
       "fsMplsRsvpTeIfStatsTable": fsMplsRsvpTeIfStatsTable,
       "fsMplsRsvpTeIfStatsEntry": fsMplsRsvpTeIfStatsEntry,
       "fsMplsRsvpTeIfNumTnls": fsMplsRsvpTeIfNumTnls,
       "fsMplsRsvpTeIfNumMsgSent": fsMplsRsvpTeIfNumMsgSent,
       "fsMplsRsvpTeIfNumMsgRcvd": fsMplsRsvpTeIfNumMsgRcvd,
       "fsMplsRsvpTeIfNumHelloSent": fsMplsRsvpTeIfNumHelloSent,
       "fsMplsRsvpTeIfNumHelloRcvd": fsMplsRsvpTeIfNumHelloRcvd,
       "fsMplsRsvpTeIfNumPathErrSent": fsMplsRsvpTeIfNumPathErrSent,
       "fsMplsRsvpTeIfNumPathErrRcvd": fsMplsRsvpTeIfNumPathErrRcvd,
       "fsMplsRsvpTeIfNumPathTearSent": fsMplsRsvpTeIfNumPathTearSent,
       "fsMplsRsvpTeIfNumPathTearRcvd": fsMplsRsvpTeIfNumPathTearRcvd,
       "fsMplsRsvpTeIfNumResvErrSent": fsMplsRsvpTeIfNumResvErrSent,
       "fsMplsRsvpTeIfNumResvErrRcvd": fsMplsRsvpTeIfNumResvErrRcvd,
       "fsMplsRsvpTeIfNumResvTearSent": fsMplsRsvpTeIfNumResvTearSent,
       "fsMplsRsvpTeIfNumResvTearRcvd": fsMplsRsvpTeIfNumResvTearRcvd,
       "fsMplsRsvpTeIfNumResvConfSent": fsMplsRsvpTeIfNumResvConfSent,
       "fsMplsRsvpTeIfNumResvConfRcvd": fsMplsRsvpTeIfNumResvConfRcvd,
       "fsMplsRsvpTeIfNumBundleMsgSent": fsMplsRsvpTeIfNumBundleMsgSent,
       "fsMplsRsvpTeIfNumBundleMsgRcvd": fsMplsRsvpTeIfNumBundleMsgRcvd,
       "fsMplsRsvpTeIfNumSRefreshMsgSent": fsMplsRsvpTeIfNumSRefreshMsgSent,
       "fsMplsRsvpTeIfNumSRefreshMsgRcvd": fsMplsRsvpTeIfNumSRefreshMsgRcvd,
       "fsMplsRsvpTeIfNumPathSent": fsMplsRsvpTeIfNumPathSent,
       "fsMplsRsvpTeIfNumPathRcvd": fsMplsRsvpTeIfNumPathRcvd,
       "fsMplsRsvpTeIfNumResvSent": fsMplsRsvpTeIfNumResvSent,
       "fsMplsRsvpTeIfNumResvRcvd": fsMplsRsvpTeIfNumResvRcvd,
       "fsMplsRsvpTeIfNumNotifyMsgSent": fsMplsRsvpTeIfNumNotifyMsgSent,
       "fsMplsRsvpTeIfNumNotifyMsgRcvd": fsMplsRsvpTeIfNumNotifyMsgRcvd,
       "fsMplsRsvpTeIfNumRecoveryPathSent": fsMplsRsvpTeIfNumRecoveryPathSent,
       "fsMplsRsvpTeIfNumRecoveryPathRcvd": fsMplsRsvpTeIfNumRecoveryPathRcvd,
       "fsMplsRsvpTeIfNumPathSentWithRecoveryLbl": fsMplsRsvpTeIfNumPathSentWithRecoveryLbl,
       "fsMplsRsvpTeIfNumPathRcvdWithRecoveryLbl": fsMplsRsvpTeIfNumPathRcvdWithRecoveryLbl,
       "fsMplsRsvpTeIfNumPathSentWithSuggestedLbl": fsMplsRsvpTeIfNumPathSentWithSuggestedLbl,
       "fsMplsRsvpTeIfNumPathRcvdWithSuggestedLbl": fsMplsRsvpTeIfNumPathRcvdWithSuggestedLbl,
       "fsMplsRsvpTeIfNumHelloSentWithRestartCap": fsMplsRsvpTeIfNumHelloSentWithRestartCap,
       "fsMplsRsvpTeIfNumHelloRcvdWithRestartCap": fsMplsRsvpTeIfNumHelloRcvdWithRestartCap,
       "fsMplsRsvpTeIfNumHelloSentWithCapability": fsMplsRsvpTeIfNumHelloSentWithCapability,
       "fsMplsRsvpTeIfNumHelloRcvdWithCapability": fsMplsRsvpTeIfNumHelloRcvdWithCapability,
       "fsMplsRsvpTeNbrTable": fsMplsRsvpTeNbrTable,
       "fsMplsRsvpTeNbrEntry": fsMplsRsvpTeNbrEntry,
       "fsMplsRsvpTeNbrIfAddr": fsMplsRsvpTeNbrIfAddr,
       "fsMplsRsvpTeNbrRRCapable": fsMplsRsvpTeNbrRRCapable,
       "fsMplsRsvpTeNbrRRState": fsMplsRsvpTeNbrRRState,
       "fsMplsRsvpTeNbrRMDCapable": fsMplsRsvpTeNbrRMDCapable,
       "fsMplsRsvpTeNbrEncapsType": fsMplsRsvpTeNbrEncapsType,
       "fsMplsRsvpTeNbrHelloSupport": fsMplsRsvpTeNbrHelloSupport,
       "fsMplsRsvpTeNbrHelloState": fsMplsRsvpTeNbrHelloState,
       "fsMplsRsvpTeNbrHelloRelation": fsMplsRsvpTeNbrHelloRelation,
       "fsMplsRsvpTeNbrSrcInstInfo": fsMplsRsvpTeNbrSrcInstInfo,
       "fsMplsRsvpTeNbrDestInstInfo": fsMplsRsvpTeNbrDestInstInfo,
       "fsMplsRsvpTeNbrCreationTime": fsMplsRsvpTeNbrCreationTime,
       "fsMplsRsvpTeNbrLclRprDetectionTime": fsMplsRsvpTeNbrLclRprDetectionTime,
       "fsMplsRsvpTeNbrNumTunnels": fsMplsRsvpTeNbrNumTunnels,
       "fsMplsRsvpTeNbrStatus": fsMplsRsvpTeNbrStatus,
       "fsMplsRsvpTeNbrGrRecoveryPathCapability": fsMplsRsvpTeNbrGrRecoveryPathCapability,
       "fsMplsRsvpTeNbrGrRestartTime": fsMplsRsvpTeNbrGrRestartTime,
       "fsMplsRsvpTeNbrGrRecoveryTime": fsMplsRsvpTeNbrGrRecoveryTime,
       "fsMplsRsvpTeNbrGrProgressStatus": fsMplsRsvpTeNbrGrProgressStatus,
       "fsMplsRsvpTeNbrStorageType": fsMplsRsvpTeNbrStorageType,
       "fsMplsRsvpTeGenObjects": fsMplsRsvpTeGenObjects,
       "fsMplsRsvpTeLsrID": fsMplsRsvpTeLsrID,
       "fsMplsRsvpTeMaxTnls": fsMplsRsvpTeMaxTnls,
       "fsMplsRsvpTeMaxErhopsPerTnl": fsMplsRsvpTeMaxErhopsPerTnl,
       "fsMplsRsvpTeMaxActRoutePerTnl": fsMplsRsvpTeMaxActRoutePerTnl,
       "fsMplsRsvpTeMaxIfaces": fsMplsRsvpTeMaxIfaces,
       "fsMplsRsvpTeMaxNbrs": fsMplsRsvpTeMaxNbrs,
       "fsMplsRsvpTeSockSupprtd": fsMplsRsvpTeSockSupprtd,
       "fsMplsRsvpTeHelloSupprtd": fsMplsRsvpTeHelloSupprtd,
       "fsMplsRsvpTeHelloIntervalTime": fsMplsRsvpTeHelloIntervalTime,
       "fsMplsRsvpTeRRCapable": fsMplsRsvpTeRRCapable,
       "fsMplsRsvpTeMsgIdCapable": fsMplsRsvpTeMsgIdCapable,
       "fsMplsRsvpTeRMDPolicyObject": fsMplsRsvpTeRMDPolicyObject,
       "fsMplsRsvpTeGenLblSpaceMinLbl": fsMplsRsvpTeGenLblSpaceMinLbl,
       "fsMplsRsvpTeGenLblSpaceMaxLbl": fsMplsRsvpTeGenLblSpaceMaxLbl,
       "fsMplsRsvpTeGenDebugFlag": fsMplsRsvpTeGenDebugFlag,
       "fsMplsRsvpTeGenPduDumpLevel": fsMplsRsvpTeGenPduDumpLevel,
       "fsMplsRsvpTeGenPduDumpMsgType": fsMplsRsvpTeGenPduDumpMsgType,
       "fsMplsRsvpTeGenPduDumpDirection": fsMplsRsvpTeGenPduDumpDirection,
       "fsMplsRsvpTeOperStatus": fsMplsRsvpTeOperStatus,
       "fsMplsRsvpTeOverRideOption": fsMplsRsvpTeOverRideOption,
       "fsMplsRsvpTeMinTnlsWithMsgId": fsMplsRsvpTeMinTnlsWithMsgId,
       "fsMplsRsvpTeNotificationEnabled": fsMplsRsvpTeNotificationEnabled,
       "fsMplsRsvpTeNotifyMsgRetransmitIntvl": fsMplsRsvpTeNotifyMsgRetransmitIntvl,
       "fsMplsRsvpTeNotifyMsgRetransmitDecay": fsMplsRsvpTeNotifyMsgRetransmitDecay,
       "fsMplsRsvpTeNotifyMsgRetransmitLimit": fsMplsRsvpTeNotifyMsgRetransmitLimit,
       "fsMplsRsvpTeAdminStatusTimeIntvl": fsMplsRsvpTeAdminStatusTimeIntvl,
       "fsMplsRsvpTePathStateRemovedSupport": fsMplsRsvpTePathStateRemovedSupport,
       "fsMplsRsvpTeLabelSetEnabled": fsMplsRsvpTeLabelSetEnabled,
       "fsMplsRsvpTeAdminStatusCapability": fsMplsRsvpTeAdminStatusCapability,
       "fsMplsRsvpTeGrCapability": fsMplsRsvpTeGrCapability,
       "fsMplsRsvpTeGrRecoveryPathCapability": fsMplsRsvpTeGrRecoveryPathCapability,
       "fsMplsRsvpTeGrRestartTime": fsMplsRsvpTeGrRestartTime,
       "fsMplsRsvpTeGrRecoveryTime": fsMplsRsvpTeGrRecoveryTime,
       "fsMplsRsvpTeGrProgressStatus": fsMplsRsvpTeGrProgressStatus}
)
