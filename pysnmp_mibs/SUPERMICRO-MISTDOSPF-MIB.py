# SNMP MIB module (SUPERMICRO-MISTDOSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-MISTDOSPF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:05:19 2025
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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsMIStdOspf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146)
)
if mibBuilder.loadTexts:
    fsMIStdOspf.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AreaID(TextualConvention, IpAddress):
    status = "current"


class RouterID(TextualConvention, IpAddress):
    status = "current"


class Metric(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class BigMetric(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )



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



class PositiveInteger(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class HelloRange(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class UpToMaxAge(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )



class DesignatedRouterPriority(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TOSType(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )



# MIB Managed Objects in the order of their OIDs

_FsMIStdOspfGeneralGroup_ObjectIdentity = ObjectIdentity
fsMIStdOspfGeneralGroup = _FsMIStdOspfGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 1)
)
_FsMIStdOspfTable_Object = MibTable
fsMIStdOspfTable = _FsMIStdOspfTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 1, 1)
)
if mibBuilder.loadTexts:
    fsMIStdOspfTable.setStatus("current")
_FsMIStdOspfEntry_Object = MibTableRow
fsMIStdOspfEntry = _FsMIStdOspfEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 1, 1, 1)
)
fsMIStdOspfEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
)
if mibBuilder.loadTexts:
    fsMIStdOspfEntry.setStatus("current")


class _FsMIStdOspfContextId_Type(Integer32):
    """Custom type fsMIStdOspfContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIStdOspfContextId_Type.__name__ = "Integer32"
_FsMIStdOspfContextId_Object = MibTableColumn
fsMIStdOspfContextId = _FsMIStdOspfContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 1, 1, 1, 1),
    _FsMIStdOspfContextId_Type()
)
fsMIStdOspfContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdOspfContextId.setStatus("current")
_FsMIStdOspfRouterId_Type = RouterID
_FsMIStdOspfRouterId_Object = MibTableColumn
fsMIStdOspfRouterId = _FsMIStdOspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 1, 1, 1, 2),
    _FsMIStdOspfRouterId_Type()
)
fsMIStdOspfRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIStdOspfRouterId.setStatus("current")
_FsMIStdOspfAdminStat_Type = Status
_FsMIStdOspfAdminStat_Object = MibTableColumn
fsMIStdOspfAdminStat = _FsMIStdOspfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 1, 1, 1, 3),
    _FsMIStdOspfAdminStat_Type()
)
fsMIStdOspfAdminStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIStdOspfAdminStat.setStatus("current")


class _FsMIStdOspfVersionNumber_Type(Integer32):
    """Custom type fsMIStdOspfVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("version2", 2)
    )


_FsMIStdOspfVersionNumber_Type.__name__ = "Integer32"
_FsMIStdOspfVersionNumber_Object = MibTableColumn
fsMIStdOspfVersionNumber = _FsMIStdOspfVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 1, 1, 1, 4),
    _FsMIStdOspfVersionNumber_Type()
)
fsMIStdOspfVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfVersionNumber.setStatus("current")
_FsMIStdOspfAreaBdrRtrStatus_Type = TruthValue
_FsMIStdOspfAreaBdrRtrStatus_Object = MibTableColumn
fsMIStdOspfAreaBdrRtrStatus = _FsMIStdOspfAreaBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 1, 1, 1, 5),
    _FsMIStdOspfAreaBdrRtrStatus_Type()
)
fsMIStdOspfAreaBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfAreaBdrRtrStatus.setStatus("current")
_FsMIStdOspfASBdrRtrStatus_Type = TruthValue
_FsMIStdOspfASBdrRtrStatus_Object = MibTableColumn
fsMIStdOspfASBdrRtrStatus = _FsMIStdOspfASBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 1, 1, 1, 6),
    _FsMIStdOspfASBdrRtrStatus_Type()
)
fsMIStdOspfASBdrRtrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIStdOspfASBdrRtrStatus.setStatus("current")
_FsMIStdOspfExternLsaCount_Type = Gauge32
_FsMIStdOspfExternLsaCount_Object = MibTableColumn
fsMIStdOspfExternLsaCount = _FsMIStdOspfExternLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 1, 1, 1, 7),
    _FsMIStdOspfExternLsaCount_Type()
)
fsMIStdOspfExternLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfExternLsaCount.setStatus("current")
_FsMIStdOspfExternLsaCksumSum_Type = Integer32
_FsMIStdOspfExternLsaCksumSum_Object = MibTableColumn
fsMIStdOspfExternLsaCksumSum = _FsMIStdOspfExternLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 1, 1, 1, 8),
    _FsMIStdOspfExternLsaCksumSum_Type()
)
fsMIStdOspfExternLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfExternLsaCksumSum.setStatus("current")
_FsMIStdOspfTOSSupport_Type = TruthValue
_FsMIStdOspfTOSSupport_Object = MibTableColumn
fsMIStdOspfTOSSupport = _FsMIStdOspfTOSSupport_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 1, 1, 1, 9),
    _FsMIStdOspfTOSSupport_Type()
)
fsMIStdOspfTOSSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIStdOspfTOSSupport.setStatus("current")
_FsMIStdOspfOriginateNewLsas_Type = Counter32
_FsMIStdOspfOriginateNewLsas_Object = MibTableColumn
fsMIStdOspfOriginateNewLsas = _FsMIStdOspfOriginateNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 1, 1, 1, 10),
    _FsMIStdOspfOriginateNewLsas_Type()
)
fsMIStdOspfOriginateNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfOriginateNewLsas.setStatus("current")
_FsMIStdOspfRxNewLsas_Type = Counter32
_FsMIStdOspfRxNewLsas_Object = MibTableColumn
fsMIStdOspfRxNewLsas = _FsMIStdOspfRxNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 1, 1, 1, 11),
    _FsMIStdOspfRxNewLsas_Type()
)
fsMIStdOspfRxNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfRxNewLsas.setStatus("current")


class _FsMIStdOspfExtLsdbLimit_Type(Integer32):
    """Custom type fsMIStdOspfExtLsdbLimit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_FsMIStdOspfExtLsdbLimit_Type.__name__ = "Integer32"
_FsMIStdOspfExtLsdbLimit_Object = MibTableColumn
fsMIStdOspfExtLsdbLimit = _FsMIStdOspfExtLsdbLimit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 1, 1, 1, 12),
    _FsMIStdOspfExtLsdbLimit_Type()
)
fsMIStdOspfExtLsdbLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIStdOspfExtLsdbLimit.setStatus("current")


class _FsMIStdOspfMulticastExtensions_Type(Integer32):
    """Custom type fsMIStdOspfMulticastExtensions based on Integer32"""
    defaultValue = 0


_FsMIStdOspfMulticastExtensions_Type.__name__ = "Integer32"
_FsMIStdOspfMulticastExtensions_Object = MibTableColumn
fsMIStdOspfMulticastExtensions = _FsMIStdOspfMulticastExtensions_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 1, 1, 1, 13),
    _FsMIStdOspfMulticastExtensions_Type()
)
fsMIStdOspfMulticastExtensions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIStdOspfMulticastExtensions.setStatus("current")


class _FsMIStdOspfExitOverflowInterval_Type(PositiveInteger):
    """Custom type fsMIStdOspfExitOverflowInterval based on PositiveInteger"""
    defaultValue = 0


_FsMIStdOspfExitOverflowInterval_Type.__name__ = "PositiveInteger"
_FsMIStdOspfExitOverflowInterval_Object = MibTableColumn
fsMIStdOspfExitOverflowInterval = _FsMIStdOspfExitOverflowInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 1, 1, 1, 14),
    _FsMIStdOspfExitOverflowInterval_Type()
)
fsMIStdOspfExitOverflowInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIStdOspfExitOverflowInterval.setStatus("current")
_FsMIStdOspfDemandExtensions_Type = TruthValue
_FsMIStdOspfDemandExtensions_Object = MibTableColumn
fsMIStdOspfDemandExtensions = _FsMIStdOspfDemandExtensions_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 1, 1, 1, 15),
    _FsMIStdOspfDemandExtensions_Type()
)
fsMIStdOspfDemandExtensions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIStdOspfDemandExtensions.setStatus("current")
_FsMIStdOspfStatus_Type = RowStatus
_FsMIStdOspfStatus_Object = MibTableColumn
fsMIStdOspfStatus = _FsMIStdOspfStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 1, 1, 1, 16),
    _FsMIStdOspfStatus_Type()
)
fsMIStdOspfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIStdOspfStatus.setStatus("current")
_FsMIStdOspfAreaTable_Object = MibTable
fsMIStdOspfAreaTable = _FsMIStdOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 2)
)
if mibBuilder.loadTexts:
    fsMIStdOspfAreaTable.setStatus("current")
_FsMIStdOspfAreaEntry_Object = MibTableRow
fsMIStdOspfAreaEntry = _FsMIStdOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 2, 1)
)
fsMIStdOspfAreaEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfAreaId"),
)
if mibBuilder.loadTexts:
    fsMIStdOspfAreaEntry.setStatus("current")
_FsMIStdOspfAreaId_Type = AreaID
_FsMIStdOspfAreaId_Object = MibTableColumn
fsMIStdOspfAreaId = _FsMIStdOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 2, 1, 1),
    _FsMIStdOspfAreaId_Type()
)
fsMIStdOspfAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdOspfAreaId.setStatus("current")


class _FsMIStdOspfImportAsExtern_Type(Integer32):
    """Custom type fsMIStdOspfImportAsExtern based on Integer32"""
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
        *(("importExternal", 1),
          ("importNoExternal", 2),
          ("importNssa", 3))
    )


_FsMIStdOspfImportAsExtern_Type.__name__ = "Integer32"
_FsMIStdOspfImportAsExtern_Object = MibTableColumn
fsMIStdOspfImportAsExtern = _FsMIStdOspfImportAsExtern_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 2, 1, 3),
    _FsMIStdOspfImportAsExtern_Type()
)
fsMIStdOspfImportAsExtern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfImportAsExtern.setStatus("current")
_FsMIStdOspfSpfRuns_Type = Counter32
_FsMIStdOspfSpfRuns_Object = MibTableColumn
fsMIStdOspfSpfRuns = _FsMIStdOspfSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 2, 1, 4),
    _FsMIStdOspfSpfRuns_Type()
)
fsMIStdOspfSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfSpfRuns.setStatus("current")
_FsMIStdOspfAreaBdrRtrCount_Type = Gauge32
_FsMIStdOspfAreaBdrRtrCount_Object = MibTableColumn
fsMIStdOspfAreaBdrRtrCount = _FsMIStdOspfAreaBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 2, 1, 5),
    _FsMIStdOspfAreaBdrRtrCount_Type()
)
fsMIStdOspfAreaBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfAreaBdrRtrCount.setStatus("current")
_FsMIStdOspfAsBdrRtrCount_Type = Gauge32
_FsMIStdOspfAsBdrRtrCount_Object = MibTableColumn
fsMIStdOspfAsBdrRtrCount = _FsMIStdOspfAsBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 2, 1, 6),
    _FsMIStdOspfAsBdrRtrCount_Type()
)
fsMIStdOspfAsBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfAsBdrRtrCount.setStatus("current")
_FsMIStdOspfAreaLsaCount_Type = Gauge32
_FsMIStdOspfAreaLsaCount_Object = MibTableColumn
fsMIStdOspfAreaLsaCount = _FsMIStdOspfAreaLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 2, 1, 7),
    _FsMIStdOspfAreaLsaCount_Type()
)
fsMIStdOspfAreaLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfAreaLsaCount.setStatus("current")


class _FsMIStdOspfAreaLsaCksumSum_Type(Integer32):
    """Custom type fsMIStdOspfAreaLsaCksumSum based on Integer32"""
    defaultValue = 0


_FsMIStdOspfAreaLsaCksumSum_Type.__name__ = "Integer32"
_FsMIStdOspfAreaLsaCksumSum_Object = MibTableColumn
fsMIStdOspfAreaLsaCksumSum = _FsMIStdOspfAreaLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 2, 1, 8),
    _FsMIStdOspfAreaLsaCksumSum_Type()
)
fsMIStdOspfAreaLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfAreaLsaCksumSum.setStatus("current")


class _FsMIStdOspfAreaSummary_Type(Integer32):
    """Custom type fsMIStdOspfAreaSummary based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAreaSummary", 1),
          ("sendAreaSummary", 2))
    )


_FsMIStdOspfAreaSummary_Type.__name__ = "Integer32"
_FsMIStdOspfAreaSummary_Object = MibTableColumn
fsMIStdOspfAreaSummary = _FsMIStdOspfAreaSummary_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 2, 1, 9),
    _FsMIStdOspfAreaSummary_Type()
)
fsMIStdOspfAreaSummary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfAreaSummary.setStatus("current")
_FsMIStdOspfAreaStatus_Type = RowStatus
_FsMIStdOspfAreaStatus_Object = MibTableColumn
fsMIStdOspfAreaStatus = _FsMIStdOspfAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 2, 1, 10),
    _FsMIStdOspfAreaStatus_Type()
)
fsMIStdOspfAreaStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfAreaStatus.setStatus("current")
_FsMIStdOspfStubAreaTable_Object = MibTable
fsMIStdOspfStubAreaTable = _FsMIStdOspfStubAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 3)
)
if mibBuilder.loadTexts:
    fsMIStdOspfStubAreaTable.setStatus("current")
_FsMIStdOspfStubAreaEntry_Object = MibTableRow
fsMIStdOspfStubAreaEntry = _FsMIStdOspfStubAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 3, 1)
)
fsMIStdOspfStubAreaEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfStubAreaId"),
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfStubTOS"),
)
if mibBuilder.loadTexts:
    fsMIStdOspfStubAreaEntry.setStatus("current")
_FsMIStdOspfStubAreaId_Type = AreaID
_FsMIStdOspfStubAreaId_Object = MibTableColumn
fsMIStdOspfStubAreaId = _FsMIStdOspfStubAreaId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 3, 1, 1),
    _FsMIStdOspfStubAreaId_Type()
)
fsMIStdOspfStubAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdOspfStubAreaId.setStatus("current")
_FsMIStdOspfStubTOS_Type = TOSType
_FsMIStdOspfStubTOS_Object = MibTableColumn
fsMIStdOspfStubTOS = _FsMIStdOspfStubTOS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 3, 1, 2),
    _FsMIStdOspfStubTOS_Type()
)
fsMIStdOspfStubTOS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdOspfStubTOS.setStatus("current")
_FsMIStdOspfStubMetric_Type = BigMetric
_FsMIStdOspfStubMetric_Object = MibTableColumn
fsMIStdOspfStubMetric = _FsMIStdOspfStubMetric_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 3, 1, 3),
    _FsMIStdOspfStubMetric_Type()
)
fsMIStdOspfStubMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfStubMetric.setStatus("current")
_FsMIStdOspfStubStatus_Type = RowStatus
_FsMIStdOspfStubStatus_Object = MibTableColumn
fsMIStdOspfStubStatus = _FsMIStdOspfStubStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 3, 1, 4),
    _FsMIStdOspfStubStatus_Type()
)
fsMIStdOspfStubStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfStubStatus.setStatus("current")


class _FsMIStdOspfStubMetricType_Type(Integer32):
    """Custom type fsMIStdOspfStubMetricType based on Integer32"""
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
        *(("ospfMetric", 1),
          ("comparableCost", 2),
          ("nonComparable", 3))
    )


_FsMIStdOspfStubMetricType_Type.__name__ = "Integer32"
_FsMIStdOspfStubMetricType_Object = MibTableColumn
fsMIStdOspfStubMetricType = _FsMIStdOspfStubMetricType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 3, 1, 5),
    _FsMIStdOspfStubMetricType_Type()
)
fsMIStdOspfStubMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfStubMetricType.setStatus("current")
_FsMIStdOspfLsdbTable_Object = MibTable
fsMIStdOspfLsdbTable = _FsMIStdOspfLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 4)
)
if mibBuilder.loadTexts:
    fsMIStdOspfLsdbTable.setStatus("current")
_FsMIStdOspfLsdbEntry_Object = MibTableRow
fsMIStdOspfLsdbEntry = _FsMIStdOspfLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 4, 1)
)
fsMIStdOspfLsdbEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfLsdbAreaId"),
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfLsdbType"),
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfLsdbLsid"),
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfLsdbRouterId"),
)
if mibBuilder.loadTexts:
    fsMIStdOspfLsdbEntry.setStatus("current")
_FsMIStdOspfLsdbAreaId_Type = AreaID
_FsMIStdOspfLsdbAreaId_Object = MibTableColumn
fsMIStdOspfLsdbAreaId = _FsMIStdOspfLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 4, 1, 1),
    _FsMIStdOspfLsdbAreaId_Type()
)
fsMIStdOspfLsdbAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdOspfLsdbAreaId.setStatus("current")


class _FsMIStdOspfLsdbType_Type(Integer32):
    """Custom type fsMIStdOspfLsdbType based on Integer32"""
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
        *(("routerLink", 1),
          ("networkLink", 2),
          ("summaryLink", 3),
          ("asSummaryLink", 4),
          ("asExternalLink", 5),
          ("multicastLink", 6),
          ("nssaExternalLink", 7))
    )


_FsMIStdOspfLsdbType_Type.__name__ = "Integer32"
_FsMIStdOspfLsdbType_Object = MibTableColumn
fsMIStdOspfLsdbType = _FsMIStdOspfLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 4, 1, 2),
    _FsMIStdOspfLsdbType_Type()
)
fsMIStdOspfLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdOspfLsdbType.setStatus("current")
_FsMIStdOspfLsdbLsid_Type = IpAddress
_FsMIStdOspfLsdbLsid_Object = MibTableColumn
fsMIStdOspfLsdbLsid = _FsMIStdOspfLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 4, 1, 3),
    _FsMIStdOspfLsdbLsid_Type()
)
fsMIStdOspfLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdOspfLsdbLsid.setStatus("current")
_FsMIStdOspfLsdbRouterId_Type = RouterID
_FsMIStdOspfLsdbRouterId_Object = MibTableColumn
fsMIStdOspfLsdbRouterId = _FsMIStdOspfLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 4, 1, 4),
    _FsMIStdOspfLsdbRouterId_Type()
)
fsMIStdOspfLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdOspfLsdbRouterId.setStatus("current")
_FsMIStdOspfLsdbSequence_Type = Integer32
_FsMIStdOspfLsdbSequence_Object = MibTableColumn
fsMIStdOspfLsdbSequence = _FsMIStdOspfLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 4, 1, 5),
    _FsMIStdOspfLsdbSequence_Type()
)
fsMIStdOspfLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfLsdbSequence.setStatus("current")
_FsMIStdOspfLsdbAge_Type = Integer32
_FsMIStdOspfLsdbAge_Object = MibTableColumn
fsMIStdOspfLsdbAge = _FsMIStdOspfLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 4, 1, 6),
    _FsMIStdOspfLsdbAge_Type()
)
fsMIStdOspfLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfLsdbAge.setStatus("current")
_FsMIStdOspfLsdbChecksum_Type = Integer32
_FsMIStdOspfLsdbChecksum_Object = MibTableColumn
fsMIStdOspfLsdbChecksum = _FsMIStdOspfLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 4, 1, 7),
    _FsMIStdOspfLsdbChecksum_Type()
)
fsMIStdOspfLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfLsdbChecksum.setStatus("current")


class _FsMIStdOspfLsdbAdvertisement_Type(OctetString):
    """Custom type fsMIStdOspfLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_FsMIStdOspfLsdbAdvertisement_Type.__name__ = "OctetString"
_FsMIStdOspfLsdbAdvertisement_Object = MibTableColumn
fsMIStdOspfLsdbAdvertisement = _FsMIStdOspfLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 4, 1, 8),
    _FsMIStdOspfLsdbAdvertisement_Type()
)
fsMIStdOspfLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfLsdbAdvertisement.setStatus("current")
_FsMIStdOspfHostTable_Object = MibTable
fsMIStdOspfHostTable = _FsMIStdOspfHostTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 5)
)
if mibBuilder.loadTexts:
    fsMIStdOspfHostTable.setStatus("current")
_FsMIStdOspfHostEntry_Object = MibTableRow
fsMIStdOspfHostEntry = _FsMIStdOspfHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 5, 1)
)
fsMIStdOspfHostEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfHostIpAddress"),
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfHostTOS"),
)
if mibBuilder.loadTexts:
    fsMIStdOspfHostEntry.setStatus("current")
_FsMIStdOspfHostIpAddress_Type = IpAddress
_FsMIStdOspfHostIpAddress_Object = MibTableColumn
fsMIStdOspfHostIpAddress = _FsMIStdOspfHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 5, 1, 1),
    _FsMIStdOspfHostIpAddress_Type()
)
fsMIStdOspfHostIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdOspfHostIpAddress.setStatus("current")
_FsMIStdOspfHostTOS_Type = TOSType
_FsMIStdOspfHostTOS_Object = MibTableColumn
fsMIStdOspfHostTOS = _FsMIStdOspfHostTOS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 5, 1, 2),
    _FsMIStdOspfHostTOS_Type()
)
fsMIStdOspfHostTOS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdOspfHostTOS.setStatus("current")
_FsMIStdOspfHostMetric_Type = Metric
_FsMIStdOspfHostMetric_Object = MibTableColumn
fsMIStdOspfHostMetric = _FsMIStdOspfHostMetric_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 5, 1, 3),
    _FsMIStdOspfHostMetric_Type()
)
fsMIStdOspfHostMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfHostMetric.setStatus("current")
_FsMIStdOspfHostStatus_Type = RowStatus
_FsMIStdOspfHostStatus_Object = MibTableColumn
fsMIStdOspfHostStatus = _FsMIStdOspfHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 5, 1, 4),
    _FsMIStdOspfHostStatus_Type()
)
fsMIStdOspfHostStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfHostStatus.setStatus("current")
_FsMIStdOspfHostAreaID_Type = AreaID
_FsMIStdOspfHostAreaID_Object = MibTableColumn
fsMIStdOspfHostAreaID = _FsMIStdOspfHostAreaID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 5, 1, 5),
    _FsMIStdOspfHostAreaID_Type()
)
fsMIStdOspfHostAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfHostAreaID.setStatus("current")
_FsMIStdOspfIfTable_Object = MibTable
fsMIStdOspfIfTable = _FsMIStdOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 6)
)
if mibBuilder.loadTexts:
    fsMIStdOspfIfTable.setStatus("current")
_FsMIStdOspfIfEntry_Object = MibTableRow
fsMIStdOspfIfEntry = _FsMIStdOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 6, 1)
)
fsMIStdOspfIfEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfIfIpAddress"),
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfAddressLessIf"),
)
if mibBuilder.loadTexts:
    fsMIStdOspfIfEntry.setStatus("current")
_FsMIStdOspfIfIpAddress_Type = IpAddress
_FsMIStdOspfIfIpAddress_Object = MibTableColumn
fsMIStdOspfIfIpAddress = _FsMIStdOspfIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 6, 1, 1),
    _FsMIStdOspfIfIpAddress_Type()
)
fsMIStdOspfIfIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdOspfIfIpAddress.setStatus("current")


class _FsMIStdOspfAddressLessIf_Type(Integer32):
    """Custom type fsMIStdOspfAddressLessIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIStdOspfAddressLessIf_Type.__name__ = "Integer32"
_FsMIStdOspfAddressLessIf_Object = MibTableColumn
fsMIStdOspfAddressLessIf = _FsMIStdOspfAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 6, 1, 2),
    _FsMIStdOspfAddressLessIf_Type()
)
fsMIStdOspfAddressLessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdOspfAddressLessIf.setStatus("current")


class _FsMIStdOspfIfAreaId_Type(AreaID):
    """Custom type fsMIStdOspfIfAreaId based on AreaID"""
    defaultHexValue = "00000000"


_FsMIStdOspfIfAreaId_Type.__name__ = "AreaID"
_FsMIStdOspfIfAreaId_Object = MibTableColumn
fsMIStdOspfIfAreaId = _FsMIStdOspfIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 6, 1, 3),
    _FsMIStdOspfIfAreaId_Type()
)
fsMIStdOspfIfAreaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfIfAreaId.setStatus("current")


class _FsMIStdOspfIfType_Type(Integer32):
    """Custom type fsMIStdOspfIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("nbma", 2),
          ("pointToPoint", 3),
          ("pointToMultipoint", 5))
    )


_FsMIStdOspfIfType_Type.__name__ = "Integer32"
_FsMIStdOspfIfType_Object = MibTableColumn
fsMIStdOspfIfType = _FsMIStdOspfIfType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 6, 1, 4),
    _FsMIStdOspfIfType_Type()
)
fsMIStdOspfIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfIfType.setStatus("current")


class _FsMIStdOspfIfAdminStat_Type(Status):
    """Custom type fsMIStdOspfIfAdminStat based on Status"""
    defaultValue = 1


_FsMIStdOspfIfAdminStat_Type.__name__ = "Status"
_FsMIStdOspfIfAdminStat_Object = MibTableColumn
fsMIStdOspfIfAdminStat = _FsMIStdOspfIfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 6, 1, 5),
    _FsMIStdOspfIfAdminStat_Type()
)
fsMIStdOspfIfAdminStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfIfAdminStat.setStatus("current")


class _FsMIStdOspfIfRtrPriority_Type(DesignatedRouterPriority):
    """Custom type fsMIStdOspfIfRtrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_FsMIStdOspfIfRtrPriority_Type.__name__ = "DesignatedRouterPriority"
_FsMIStdOspfIfRtrPriority_Object = MibTableColumn
fsMIStdOspfIfRtrPriority = _FsMIStdOspfIfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 6, 1, 6),
    _FsMIStdOspfIfRtrPriority_Type()
)
fsMIStdOspfIfRtrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfIfRtrPriority.setStatus("current")


class _FsMIStdOspfIfTransitDelay_Type(UpToMaxAge):
    """Custom type fsMIStdOspfIfTransitDelay based on UpToMaxAge"""
    defaultValue = 1


_FsMIStdOspfIfTransitDelay_Type.__name__ = "UpToMaxAge"
_FsMIStdOspfIfTransitDelay_Object = MibTableColumn
fsMIStdOspfIfTransitDelay = _FsMIStdOspfIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 6, 1, 7),
    _FsMIStdOspfIfTransitDelay_Type()
)
fsMIStdOspfIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfIfTransitDelay.setStatus("current")


class _FsMIStdOspfIfRetransInterval_Type(UpToMaxAge):
    """Custom type fsMIStdOspfIfRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_FsMIStdOspfIfRetransInterval_Type.__name__ = "UpToMaxAge"
_FsMIStdOspfIfRetransInterval_Object = MibTableColumn
fsMIStdOspfIfRetransInterval = _FsMIStdOspfIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 6, 1, 8),
    _FsMIStdOspfIfRetransInterval_Type()
)
fsMIStdOspfIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfIfRetransInterval.setStatus("current")


class _FsMIStdOspfIfHelloInterval_Type(HelloRange):
    """Custom type fsMIStdOspfIfHelloInterval based on HelloRange"""
    defaultValue = 10


_FsMIStdOspfIfHelloInterval_Type.__name__ = "HelloRange"
_FsMIStdOspfIfHelloInterval_Object = MibTableColumn
fsMIStdOspfIfHelloInterval = _FsMIStdOspfIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 6, 1, 9),
    _FsMIStdOspfIfHelloInterval_Type()
)
fsMIStdOspfIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfIfHelloInterval.setStatus("current")


class _FsMIStdOspfIfRtrDeadInterval_Type(PositiveInteger):
    """Custom type fsMIStdOspfIfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 40


_FsMIStdOspfIfRtrDeadInterval_Type.__name__ = "PositiveInteger"
_FsMIStdOspfIfRtrDeadInterval_Object = MibTableColumn
fsMIStdOspfIfRtrDeadInterval = _FsMIStdOspfIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 6, 1, 10),
    _FsMIStdOspfIfRtrDeadInterval_Type()
)
fsMIStdOspfIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfIfRtrDeadInterval.setStatus("current")


class _FsMIStdOspfIfPollInterval_Type(PositiveInteger):
    """Custom type fsMIStdOspfIfPollInterval based on PositiveInteger"""
    defaultValue = 120


_FsMIStdOspfIfPollInterval_Type.__name__ = "PositiveInteger"
_FsMIStdOspfIfPollInterval_Object = MibTableColumn
fsMIStdOspfIfPollInterval = _FsMIStdOspfIfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 6, 1, 11),
    _FsMIStdOspfIfPollInterval_Type()
)
fsMIStdOspfIfPollInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfIfPollInterval.setStatus("current")


class _FsMIStdOspfIfState_Type(Integer32):
    """Custom type fsMIStdOspfIfState based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("loopback", 2),
          ("waiting", 3),
          ("pointToPoint", 4),
          ("designatedRouter", 5),
          ("backupDesignatedRouter", 6),
          ("otherDesignatedRouter", 7))
    )


_FsMIStdOspfIfState_Type.__name__ = "Integer32"
_FsMIStdOspfIfState_Object = MibTableColumn
fsMIStdOspfIfState = _FsMIStdOspfIfState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 6, 1, 12),
    _FsMIStdOspfIfState_Type()
)
fsMIStdOspfIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfIfState.setStatus("current")


class _FsMIStdOspfIfDesignatedRouter_Type(IpAddress):
    """Custom type fsMIStdOspfIfDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_FsMIStdOspfIfDesignatedRouter_Type.__name__ = "IpAddress"
_FsMIStdOspfIfDesignatedRouter_Object = MibTableColumn
fsMIStdOspfIfDesignatedRouter = _FsMIStdOspfIfDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 6, 1, 13),
    _FsMIStdOspfIfDesignatedRouter_Type()
)
fsMIStdOspfIfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfIfDesignatedRouter.setStatus("current")


class _FsMIStdOspfIfBackupDesignatedRouter_Type(IpAddress):
    """Custom type fsMIStdOspfIfBackupDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_FsMIStdOspfIfBackupDesignatedRouter_Type.__name__ = "IpAddress"
_FsMIStdOspfIfBackupDesignatedRouter_Object = MibTableColumn
fsMIStdOspfIfBackupDesignatedRouter = _FsMIStdOspfIfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 6, 1, 14),
    _FsMIStdOspfIfBackupDesignatedRouter_Type()
)
fsMIStdOspfIfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfIfBackupDesignatedRouter.setStatus("current")
_FsMIStdOspfIfEvents_Type = Counter32
_FsMIStdOspfIfEvents_Object = MibTableColumn
fsMIStdOspfIfEvents = _FsMIStdOspfIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 6, 1, 15),
    _FsMIStdOspfIfEvents_Type()
)
fsMIStdOspfIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfIfEvents.setStatus("current")


class _FsMIStdOspfIfAuthKey_Type(OctetString):
    """Custom type fsMIStdOspfIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FsMIStdOspfIfAuthKey_Type.__name__ = "OctetString"
_FsMIStdOspfIfAuthKey_Object = MibTableColumn
fsMIStdOspfIfAuthKey = _FsMIStdOspfIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 6, 1, 16),
    _FsMIStdOspfIfAuthKey_Type()
)
fsMIStdOspfIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfIfAuthKey.setStatus("current")
_FsMIStdOspfIfStatus_Type = RowStatus
_FsMIStdOspfIfStatus_Object = MibTableColumn
fsMIStdOspfIfStatus = _FsMIStdOspfIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 6, 1, 17),
    _FsMIStdOspfIfStatus_Type()
)
fsMIStdOspfIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfIfStatus.setStatus("current")


class _FsMIStdOspfIfMulticastForwarding_Type(Integer32):
    """Custom type fsMIStdOspfIfMulticastForwarding based on Integer32"""
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
        *(("blocked", 1),
          ("multicast", 2),
          ("unicast", 3))
    )


_FsMIStdOspfIfMulticastForwarding_Type.__name__ = "Integer32"
_FsMIStdOspfIfMulticastForwarding_Object = MibTableColumn
fsMIStdOspfIfMulticastForwarding = _FsMIStdOspfIfMulticastForwarding_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 6, 1, 18),
    _FsMIStdOspfIfMulticastForwarding_Type()
)
fsMIStdOspfIfMulticastForwarding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfIfMulticastForwarding.setStatus("current")


class _FsMIStdOspfIfDemand_Type(TruthValue):
    """Custom type fsMIStdOspfIfDemand based on TruthValue"""
    defaultValue = 2


_FsMIStdOspfIfDemand_Type.__name__ = "TruthValue"
_FsMIStdOspfIfDemand_Object = MibTableColumn
fsMIStdOspfIfDemand = _FsMIStdOspfIfDemand_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 6, 1, 19),
    _FsMIStdOspfIfDemand_Type()
)
fsMIStdOspfIfDemand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfIfDemand.setStatus("current")


class _FsMIStdOspfIfAuthType_Type(Integer32):
    """Custom type fsMIStdOspfIfAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIStdOspfIfAuthType_Type.__name__ = "Integer32"
_FsMIStdOspfIfAuthType_Object = MibTableColumn
fsMIStdOspfIfAuthType = _FsMIStdOspfIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 6, 1, 20),
    _FsMIStdOspfIfAuthType_Type()
)
fsMIStdOspfIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfIfAuthType.setStatus("current")


class _FsMIStdOspfIfCryptoAuthType_Type(Integer32):
    """Custom type fsMIStdOspfIfCryptoAuthType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIStdOspfIfCryptoAuthType_Type.__name__ = "Integer32"
_FsMIStdOspfIfCryptoAuthType_Object = MibTableColumn
fsMIStdOspfIfCryptoAuthType = _FsMIStdOspfIfCryptoAuthType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 6, 1, 21),
    _FsMIStdOspfIfCryptoAuthType_Type()
)
fsMIStdOspfIfCryptoAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfIfCryptoAuthType.setStatus("current")
_FsMIStdOspfIfMetricTable_Object = MibTable
fsMIStdOspfIfMetricTable = _FsMIStdOspfIfMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 7)
)
if mibBuilder.loadTexts:
    fsMIStdOspfIfMetricTable.setStatus("current")
_FsMIStdOspfIfMetricEntry_Object = MibTableRow
fsMIStdOspfIfMetricEntry = _FsMIStdOspfIfMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 7, 1)
)
fsMIStdOspfIfMetricEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfIfMetricIpAddress"),
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfIfMetricAddressLessIf"),
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfIfMetricTOS"),
)
if mibBuilder.loadTexts:
    fsMIStdOspfIfMetricEntry.setStatus("current")
_FsMIStdOspfIfMetricIpAddress_Type = IpAddress
_FsMIStdOspfIfMetricIpAddress_Object = MibTableColumn
fsMIStdOspfIfMetricIpAddress = _FsMIStdOspfIfMetricIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 7, 1, 1),
    _FsMIStdOspfIfMetricIpAddress_Type()
)
fsMIStdOspfIfMetricIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdOspfIfMetricIpAddress.setStatus("current")


class _FsMIStdOspfIfMetricAddressLessIf_Type(Integer32):
    """Custom type fsMIStdOspfIfMetricAddressLessIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIStdOspfIfMetricAddressLessIf_Type.__name__ = "Integer32"
_FsMIStdOspfIfMetricAddressLessIf_Object = MibTableColumn
fsMIStdOspfIfMetricAddressLessIf = _FsMIStdOspfIfMetricAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 7, 1, 2),
    _FsMIStdOspfIfMetricAddressLessIf_Type()
)
fsMIStdOspfIfMetricAddressLessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdOspfIfMetricAddressLessIf.setStatus("current")
_FsMIStdOspfIfMetricTOS_Type = TOSType
_FsMIStdOspfIfMetricTOS_Object = MibTableColumn
fsMIStdOspfIfMetricTOS = _FsMIStdOspfIfMetricTOS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 7, 1, 3),
    _FsMIStdOspfIfMetricTOS_Type()
)
fsMIStdOspfIfMetricTOS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdOspfIfMetricTOS.setStatus("current")
_FsMIStdOspfIfMetricValue_Type = Metric
_FsMIStdOspfIfMetricValue_Object = MibTableColumn
fsMIStdOspfIfMetricValue = _FsMIStdOspfIfMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 7, 1, 4),
    _FsMIStdOspfIfMetricValue_Type()
)
fsMIStdOspfIfMetricValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfIfMetricValue.setStatus("current")
_FsMIStdOspfIfMetricStatus_Type = RowStatus
_FsMIStdOspfIfMetricStatus_Object = MibTableColumn
fsMIStdOspfIfMetricStatus = _FsMIStdOspfIfMetricStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 7, 1, 5),
    _FsMIStdOspfIfMetricStatus_Type()
)
fsMIStdOspfIfMetricStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfIfMetricStatus.setStatus("current")
_FsMIStdOspfVirtIfTable_Object = MibTable
fsMIStdOspfVirtIfTable = _FsMIStdOspfVirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 8)
)
if mibBuilder.loadTexts:
    fsMIStdOspfVirtIfTable.setStatus("current")
_FsMIStdOspfVirtIfEntry_Object = MibTableRow
fsMIStdOspfVirtIfEntry = _FsMIStdOspfVirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 8, 1)
)
fsMIStdOspfVirtIfEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfVirtIfAreaId"),
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfVirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    fsMIStdOspfVirtIfEntry.setStatus("current")
_FsMIStdOspfVirtIfAreaId_Type = AreaID
_FsMIStdOspfVirtIfAreaId_Object = MibTableColumn
fsMIStdOspfVirtIfAreaId = _FsMIStdOspfVirtIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 8, 1, 1),
    _FsMIStdOspfVirtIfAreaId_Type()
)
fsMIStdOspfVirtIfAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdOspfVirtIfAreaId.setStatus("current")
_FsMIStdOspfVirtIfNeighbor_Type = RouterID
_FsMIStdOspfVirtIfNeighbor_Object = MibTableColumn
fsMIStdOspfVirtIfNeighbor = _FsMIStdOspfVirtIfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 8, 1, 2),
    _FsMIStdOspfVirtIfNeighbor_Type()
)
fsMIStdOspfVirtIfNeighbor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdOspfVirtIfNeighbor.setStatus("current")


class _FsMIStdOspfVirtIfTransitDelay_Type(UpToMaxAge):
    """Custom type fsMIStdOspfVirtIfTransitDelay based on UpToMaxAge"""
    defaultValue = 1


_FsMIStdOspfVirtIfTransitDelay_Type.__name__ = "UpToMaxAge"
_FsMIStdOspfVirtIfTransitDelay_Object = MibTableColumn
fsMIStdOspfVirtIfTransitDelay = _FsMIStdOspfVirtIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 8, 1, 3),
    _FsMIStdOspfVirtIfTransitDelay_Type()
)
fsMIStdOspfVirtIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfVirtIfTransitDelay.setStatus("current")


class _FsMIStdOspfVirtIfRetransInterval_Type(UpToMaxAge):
    """Custom type fsMIStdOspfVirtIfRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_FsMIStdOspfVirtIfRetransInterval_Type.__name__ = "UpToMaxAge"
_FsMIStdOspfVirtIfRetransInterval_Object = MibTableColumn
fsMIStdOspfVirtIfRetransInterval = _FsMIStdOspfVirtIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 8, 1, 4),
    _FsMIStdOspfVirtIfRetransInterval_Type()
)
fsMIStdOspfVirtIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfVirtIfRetransInterval.setStatus("current")


class _FsMIStdOspfVirtIfHelloInterval_Type(HelloRange):
    """Custom type fsMIStdOspfVirtIfHelloInterval based on HelloRange"""
    defaultValue = 10


_FsMIStdOspfVirtIfHelloInterval_Type.__name__ = "HelloRange"
_FsMIStdOspfVirtIfHelloInterval_Object = MibTableColumn
fsMIStdOspfVirtIfHelloInterval = _FsMIStdOspfVirtIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 8, 1, 5),
    _FsMIStdOspfVirtIfHelloInterval_Type()
)
fsMIStdOspfVirtIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfVirtIfHelloInterval.setStatus("current")


class _FsMIStdOspfVirtIfRtrDeadInterval_Type(PositiveInteger):
    """Custom type fsMIStdOspfVirtIfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 60


_FsMIStdOspfVirtIfRtrDeadInterval_Type.__name__ = "PositiveInteger"
_FsMIStdOspfVirtIfRtrDeadInterval_Object = MibTableColumn
fsMIStdOspfVirtIfRtrDeadInterval = _FsMIStdOspfVirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 8, 1, 6),
    _FsMIStdOspfVirtIfRtrDeadInterval_Type()
)
fsMIStdOspfVirtIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfVirtIfRtrDeadInterval.setStatus("current")


class _FsMIStdOspfVirtIfState_Type(Integer32):
    """Custom type fsMIStdOspfVirtIfState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("pointToPoint", 4))
    )


_FsMIStdOspfVirtIfState_Type.__name__ = "Integer32"
_FsMIStdOspfVirtIfState_Object = MibTableColumn
fsMIStdOspfVirtIfState = _FsMIStdOspfVirtIfState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 8, 1, 7),
    _FsMIStdOspfVirtIfState_Type()
)
fsMIStdOspfVirtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfVirtIfState.setStatus("current")
_FsMIStdOspfVirtIfEvents_Type = Counter32
_FsMIStdOspfVirtIfEvents_Object = MibTableColumn
fsMIStdOspfVirtIfEvents = _FsMIStdOspfVirtIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 8, 1, 8),
    _FsMIStdOspfVirtIfEvents_Type()
)
fsMIStdOspfVirtIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfVirtIfEvents.setStatus("current")


class _FsMIStdOspfVirtIfAuthKey_Type(OctetString):
    """Custom type fsMIStdOspfVirtIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FsMIStdOspfVirtIfAuthKey_Type.__name__ = "OctetString"
_FsMIStdOspfVirtIfAuthKey_Object = MibTableColumn
fsMIStdOspfVirtIfAuthKey = _FsMIStdOspfVirtIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 8, 1, 9),
    _FsMIStdOspfVirtIfAuthKey_Type()
)
fsMIStdOspfVirtIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfVirtIfAuthKey.setStatus("current")
_FsMIStdOspfVirtIfStatus_Type = RowStatus
_FsMIStdOspfVirtIfStatus_Object = MibTableColumn
fsMIStdOspfVirtIfStatus = _FsMIStdOspfVirtIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 8, 1, 10),
    _FsMIStdOspfVirtIfStatus_Type()
)
fsMIStdOspfVirtIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfVirtIfStatus.setStatus("current")


class _FsMIStdOspfVirtIfAuthType_Type(Integer32):
    """Custom type fsMIStdOspfVirtIfAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIStdOspfVirtIfAuthType_Type.__name__ = "Integer32"
_FsMIStdOspfVirtIfAuthType_Object = MibTableColumn
fsMIStdOspfVirtIfAuthType = _FsMIStdOspfVirtIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 8, 1, 11),
    _FsMIStdOspfVirtIfAuthType_Type()
)
fsMIStdOspfVirtIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfVirtIfAuthType.setStatus("current")


class _FsMIStdOspfVirtIfCryptoAuthType_Type(Integer32):
    """Custom type fsMIStdOspfVirtIfCryptoAuthType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIStdOspfVirtIfCryptoAuthType_Type.__name__ = "Integer32"
_FsMIStdOspfVirtIfCryptoAuthType_Object = MibTableColumn
fsMIStdOspfVirtIfCryptoAuthType = _FsMIStdOspfVirtIfCryptoAuthType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 8, 1, 12),
    _FsMIStdOspfVirtIfCryptoAuthType_Type()
)
fsMIStdOspfVirtIfCryptoAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfVirtIfCryptoAuthType.setStatus("current")
_FsMIStdOspfNbrTable_Object = MibTable
fsMIStdOspfNbrTable = _FsMIStdOspfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 9)
)
if mibBuilder.loadTexts:
    fsMIStdOspfNbrTable.setStatus("current")
_FsMIStdOspfNbrEntry_Object = MibTableRow
fsMIStdOspfNbrEntry = _FsMIStdOspfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 9, 1)
)
fsMIStdOspfNbrEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfNbrIpAddr"),
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    fsMIStdOspfNbrEntry.setStatus("current")
_FsMIStdOspfNbrIpAddr_Type = IpAddress
_FsMIStdOspfNbrIpAddr_Object = MibTableColumn
fsMIStdOspfNbrIpAddr = _FsMIStdOspfNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 9, 1, 1),
    _FsMIStdOspfNbrIpAddr_Type()
)
fsMIStdOspfNbrIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdOspfNbrIpAddr.setStatus("current")


class _FsMIStdOspfNbrAddressLessIndex_Type(Integer32):
    """Custom type fsMIStdOspfNbrAddressLessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIStdOspfNbrAddressLessIndex_Type.__name__ = "Integer32"
_FsMIStdOspfNbrAddressLessIndex_Object = MibTableColumn
fsMIStdOspfNbrAddressLessIndex = _FsMIStdOspfNbrAddressLessIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 9, 1, 2),
    _FsMIStdOspfNbrAddressLessIndex_Type()
)
fsMIStdOspfNbrAddressLessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdOspfNbrAddressLessIndex.setStatus("current")


class _FsMIStdOspfNbrRtrId_Type(RouterID):
    """Custom type fsMIStdOspfNbrRtrId based on RouterID"""
    defaultHexValue = "00000000"


_FsMIStdOspfNbrRtrId_Type.__name__ = "RouterID"
_FsMIStdOspfNbrRtrId_Object = MibTableColumn
fsMIStdOspfNbrRtrId = _FsMIStdOspfNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 9, 1, 3),
    _FsMIStdOspfNbrRtrId_Type()
)
fsMIStdOspfNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfNbrRtrId.setStatus("current")


class _FsMIStdOspfNbrOptions_Type(Integer32):
    """Custom type fsMIStdOspfNbrOptions based on Integer32"""
    defaultValue = 0


_FsMIStdOspfNbrOptions_Type.__name__ = "Integer32"
_FsMIStdOspfNbrOptions_Object = MibTableColumn
fsMIStdOspfNbrOptions = _FsMIStdOspfNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 9, 1, 4),
    _FsMIStdOspfNbrOptions_Type()
)
fsMIStdOspfNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfNbrOptions.setStatus("current")


class _FsMIStdOspfNbrPriority_Type(DesignatedRouterPriority):
    """Custom type fsMIStdOspfNbrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_FsMIStdOspfNbrPriority_Type.__name__ = "DesignatedRouterPriority"
_FsMIStdOspfNbrPriority_Object = MibTableColumn
fsMIStdOspfNbrPriority = _FsMIStdOspfNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 9, 1, 5),
    _FsMIStdOspfNbrPriority_Type()
)
fsMIStdOspfNbrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfNbrPriority.setStatus("current")


class _FsMIStdOspfNbrState_Type(Integer32):
    """Custom type fsMIStdOspfNbrState based on Integer32"""
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
        *(("down", 1),
          ("attempt", 2),
          ("init", 3),
          ("twoWay", 4),
          ("exchangeStart", 5),
          ("exchange", 6),
          ("loading", 7),
          ("full", 8))
    )


_FsMIStdOspfNbrState_Type.__name__ = "Integer32"
_FsMIStdOspfNbrState_Object = MibTableColumn
fsMIStdOspfNbrState = _FsMIStdOspfNbrState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 9, 1, 6),
    _FsMIStdOspfNbrState_Type()
)
fsMIStdOspfNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfNbrState.setStatus("current")
_FsMIStdOspfNbrEvents_Type = Counter32
_FsMIStdOspfNbrEvents_Object = MibTableColumn
fsMIStdOspfNbrEvents = _FsMIStdOspfNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 9, 1, 7),
    _FsMIStdOspfNbrEvents_Type()
)
fsMIStdOspfNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfNbrEvents.setStatus("current")
_FsMIStdOspfNbrLsRetransQLen_Type = Gauge32
_FsMIStdOspfNbrLsRetransQLen_Object = MibTableColumn
fsMIStdOspfNbrLsRetransQLen = _FsMIStdOspfNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 9, 1, 8),
    _FsMIStdOspfNbrLsRetransQLen_Type()
)
fsMIStdOspfNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfNbrLsRetransQLen.setStatus("current")
_FsMIStdOspfNbmaNbrStatus_Type = RowStatus
_FsMIStdOspfNbmaNbrStatus_Object = MibTableColumn
fsMIStdOspfNbmaNbrStatus = _FsMIStdOspfNbmaNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 9, 1, 9),
    _FsMIStdOspfNbmaNbrStatus_Type()
)
fsMIStdOspfNbmaNbrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfNbmaNbrStatus.setStatus("current")


class _FsMIStdOspfNbmaNbrPermanence_Type(Integer32):
    """Custom type fsMIStdOspfNbmaNbrPermanence based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("permanent", 2))
    )


_FsMIStdOspfNbmaNbrPermanence_Type.__name__ = "Integer32"
_FsMIStdOspfNbmaNbrPermanence_Object = MibTableColumn
fsMIStdOspfNbmaNbrPermanence = _FsMIStdOspfNbmaNbrPermanence_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 9, 1, 10),
    _FsMIStdOspfNbmaNbrPermanence_Type()
)
fsMIStdOspfNbmaNbrPermanence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfNbmaNbrPermanence.setStatus("current")
_FsMIStdOspfNbrHelloSuppressed_Type = TruthValue
_FsMIStdOspfNbrHelloSuppressed_Object = MibTableColumn
fsMIStdOspfNbrHelloSuppressed = _FsMIStdOspfNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 9, 1, 11),
    _FsMIStdOspfNbrHelloSuppressed_Type()
)
fsMIStdOspfNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfNbrHelloSuppressed.setStatus("current")
_FsMIStdOspfVirtNbrTable_Object = MibTable
fsMIStdOspfVirtNbrTable = _FsMIStdOspfVirtNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 10)
)
if mibBuilder.loadTexts:
    fsMIStdOspfVirtNbrTable.setStatus("current")
_FsMIStdOspfVirtNbrEntry_Object = MibTableRow
fsMIStdOspfVirtNbrEntry = _FsMIStdOspfVirtNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 10, 1)
)
fsMIStdOspfVirtNbrEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfVirtNbrArea"),
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfVirtNbrRtrId"),
)
if mibBuilder.loadTexts:
    fsMIStdOspfVirtNbrEntry.setStatus("current")
_FsMIStdOspfVirtNbrArea_Type = AreaID
_FsMIStdOspfVirtNbrArea_Object = MibTableColumn
fsMIStdOspfVirtNbrArea = _FsMIStdOspfVirtNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 10, 1, 1),
    _FsMIStdOspfVirtNbrArea_Type()
)
fsMIStdOspfVirtNbrArea.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdOspfVirtNbrArea.setStatus("current")
_FsMIStdOspfVirtNbrRtrId_Type = RouterID
_FsMIStdOspfVirtNbrRtrId_Object = MibTableColumn
fsMIStdOspfVirtNbrRtrId = _FsMIStdOspfVirtNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 10, 1, 2),
    _FsMIStdOspfVirtNbrRtrId_Type()
)
fsMIStdOspfVirtNbrRtrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdOspfVirtNbrRtrId.setStatus("current")
_FsMIStdOspfVirtNbrIpAddr_Type = IpAddress
_FsMIStdOspfVirtNbrIpAddr_Object = MibTableColumn
fsMIStdOspfVirtNbrIpAddr = _FsMIStdOspfVirtNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 10, 1, 3),
    _FsMIStdOspfVirtNbrIpAddr_Type()
)
fsMIStdOspfVirtNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfVirtNbrIpAddr.setStatus("current")
_FsMIStdOspfVirtNbrOptions_Type = Integer32
_FsMIStdOspfVirtNbrOptions_Object = MibTableColumn
fsMIStdOspfVirtNbrOptions = _FsMIStdOspfVirtNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 10, 1, 4),
    _FsMIStdOspfVirtNbrOptions_Type()
)
fsMIStdOspfVirtNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfVirtNbrOptions.setStatus("current")


class _FsMIStdOspfVirtNbrState_Type(Integer32):
    """Custom type fsMIStdOspfVirtNbrState based on Integer32"""
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
        *(("down", 1),
          ("attempt", 2),
          ("init", 3),
          ("twoWay", 4),
          ("exchangeStart", 5),
          ("exchange", 6),
          ("loading", 7),
          ("full", 8))
    )


_FsMIStdOspfVirtNbrState_Type.__name__ = "Integer32"
_FsMIStdOspfVirtNbrState_Object = MibTableColumn
fsMIStdOspfVirtNbrState = _FsMIStdOspfVirtNbrState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 10, 1, 5),
    _FsMIStdOspfVirtNbrState_Type()
)
fsMIStdOspfVirtNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfVirtNbrState.setStatus("current")
_FsMIStdOspfVirtNbrEvents_Type = Counter32
_FsMIStdOspfVirtNbrEvents_Object = MibTableColumn
fsMIStdOspfVirtNbrEvents = _FsMIStdOspfVirtNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 10, 1, 6),
    _FsMIStdOspfVirtNbrEvents_Type()
)
fsMIStdOspfVirtNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfVirtNbrEvents.setStatus("current")
_FsMIStdOspfVirtNbrLsRetransQLen_Type = Gauge32
_FsMIStdOspfVirtNbrLsRetransQLen_Object = MibTableColumn
fsMIStdOspfVirtNbrLsRetransQLen = _FsMIStdOspfVirtNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 10, 1, 7),
    _FsMIStdOspfVirtNbrLsRetransQLen_Type()
)
fsMIStdOspfVirtNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfVirtNbrLsRetransQLen.setStatus("current")
_FsMIStdOspfVirtNbrHelloSuppressed_Type = TruthValue
_FsMIStdOspfVirtNbrHelloSuppressed_Object = MibTableColumn
fsMIStdOspfVirtNbrHelloSuppressed = _FsMIStdOspfVirtNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 10, 1, 8),
    _FsMIStdOspfVirtNbrHelloSuppressed_Type()
)
fsMIStdOspfVirtNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfVirtNbrHelloSuppressed.setStatus("current")
_FsMIStdOspfExtLsdbTable_Object = MibTable
fsMIStdOspfExtLsdbTable = _FsMIStdOspfExtLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 11)
)
if mibBuilder.loadTexts:
    fsMIStdOspfExtLsdbTable.setStatus("current")
_FsMIStdOspfExtLsdbEntry_Object = MibTableRow
fsMIStdOspfExtLsdbEntry = _FsMIStdOspfExtLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 11, 1)
)
fsMIStdOspfExtLsdbEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfExtLsdbType"),
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfExtLsdbLsid"),
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfExtLsdbRouterId"),
)
if mibBuilder.loadTexts:
    fsMIStdOspfExtLsdbEntry.setStatus("current")


class _FsMIStdOspfExtLsdbType_Type(Integer32):
    """Custom type fsMIStdOspfExtLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("asExternalLink", 5)
    )


_FsMIStdOspfExtLsdbType_Type.__name__ = "Integer32"
_FsMIStdOspfExtLsdbType_Object = MibTableColumn
fsMIStdOspfExtLsdbType = _FsMIStdOspfExtLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 11, 1, 1),
    _FsMIStdOspfExtLsdbType_Type()
)
fsMIStdOspfExtLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdOspfExtLsdbType.setStatus("current")
_FsMIStdOspfExtLsdbLsid_Type = IpAddress
_FsMIStdOspfExtLsdbLsid_Object = MibTableColumn
fsMIStdOspfExtLsdbLsid = _FsMIStdOspfExtLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 11, 1, 2),
    _FsMIStdOspfExtLsdbLsid_Type()
)
fsMIStdOspfExtLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdOspfExtLsdbLsid.setStatus("current")
_FsMIStdOspfExtLsdbRouterId_Type = RouterID
_FsMIStdOspfExtLsdbRouterId_Object = MibTableColumn
fsMIStdOspfExtLsdbRouterId = _FsMIStdOspfExtLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 11, 1, 3),
    _FsMIStdOspfExtLsdbRouterId_Type()
)
fsMIStdOspfExtLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdOspfExtLsdbRouterId.setStatus("current")
_FsMIStdOspfExtLsdbSequence_Type = Integer32
_FsMIStdOspfExtLsdbSequence_Object = MibTableColumn
fsMIStdOspfExtLsdbSequence = _FsMIStdOspfExtLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 11, 1, 4),
    _FsMIStdOspfExtLsdbSequence_Type()
)
fsMIStdOspfExtLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfExtLsdbSequence.setStatus("current")
_FsMIStdOspfExtLsdbAge_Type = Integer32
_FsMIStdOspfExtLsdbAge_Object = MibTableColumn
fsMIStdOspfExtLsdbAge = _FsMIStdOspfExtLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 11, 1, 5),
    _FsMIStdOspfExtLsdbAge_Type()
)
fsMIStdOspfExtLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfExtLsdbAge.setStatus("current")
_FsMIStdOspfExtLsdbChecksum_Type = Integer32
_FsMIStdOspfExtLsdbChecksum_Object = MibTableColumn
fsMIStdOspfExtLsdbChecksum = _FsMIStdOspfExtLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 11, 1, 6),
    _FsMIStdOspfExtLsdbChecksum_Type()
)
fsMIStdOspfExtLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfExtLsdbChecksum.setStatus("current")


class _FsMIStdOspfExtLsdbAdvertisement_Type(OctetString):
    """Custom type fsMIStdOspfExtLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(36, 36),
    )
    fixed_length = 36


_FsMIStdOspfExtLsdbAdvertisement_Type.__name__ = "OctetString"
_FsMIStdOspfExtLsdbAdvertisement_Object = MibTableColumn
fsMIStdOspfExtLsdbAdvertisement = _FsMIStdOspfExtLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 11, 1, 7),
    _FsMIStdOspfExtLsdbAdvertisement_Type()
)
fsMIStdOspfExtLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfExtLsdbAdvertisement.setStatus("current")
_FsMIStdOspfRouteGroup_ObjectIdentity = ObjectIdentity
fsMIStdOspfRouteGroup = _FsMIStdOspfRouteGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 12)
)
_FsMIStdOspfIntraArea_ObjectIdentity = ObjectIdentity
fsMIStdOspfIntraArea = _FsMIStdOspfIntraArea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 12, 1)
)
_FsMIStdOspfInterArea_ObjectIdentity = ObjectIdentity
fsMIStdOspfInterArea = _FsMIStdOspfInterArea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 12, 2)
)
_FsMIStdOspfExternalType1_ObjectIdentity = ObjectIdentity
fsMIStdOspfExternalType1 = _FsMIStdOspfExternalType1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 12, 3)
)
_FsMIStdOspfExternalType2_ObjectIdentity = ObjectIdentity
fsMIStdOspfExternalType2 = _FsMIStdOspfExternalType2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 12, 4)
)
_FsMIStdOspfAreaAggregateTable_Object = MibTable
fsMIStdOspfAreaAggregateTable = _FsMIStdOspfAreaAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 13)
)
if mibBuilder.loadTexts:
    fsMIStdOspfAreaAggregateTable.setStatus("current")
_FsMIStdOspfAreaAggregateEntry_Object = MibTableRow
fsMIStdOspfAreaAggregateEntry = _FsMIStdOspfAreaAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 13, 1)
)
fsMIStdOspfAreaAggregateEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfAreaAggregateAreaID"),
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfAreaAggregateLsdbType"),
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfAreaAggregateNet"),
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfAreaAggregateMask"),
)
if mibBuilder.loadTexts:
    fsMIStdOspfAreaAggregateEntry.setStatus("current")
_FsMIStdOspfAreaAggregateAreaID_Type = AreaID
_FsMIStdOspfAreaAggregateAreaID_Object = MibTableColumn
fsMIStdOspfAreaAggregateAreaID = _FsMIStdOspfAreaAggregateAreaID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 13, 1, 1),
    _FsMIStdOspfAreaAggregateAreaID_Type()
)
fsMIStdOspfAreaAggregateAreaID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdOspfAreaAggregateAreaID.setStatus("current")


class _FsMIStdOspfAreaAggregateLsdbType_Type(Integer32):
    """Custom type fsMIStdOspfAreaAggregateLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("summaryLink", 3),
          ("nssaExternalLink", 7))
    )


_FsMIStdOspfAreaAggregateLsdbType_Type.__name__ = "Integer32"
_FsMIStdOspfAreaAggregateLsdbType_Object = MibTableColumn
fsMIStdOspfAreaAggregateLsdbType = _FsMIStdOspfAreaAggregateLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 13, 1, 2),
    _FsMIStdOspfAreaAggregateLsdbType_Type()
)
fsMIStdOspfAreaAggregateLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdOspfAreaAggregateLsdbType.setStatus("current")
_FsMIStdOspfAreaAggregateNet_Type = IpAddress
_FsMIStdOspfAreaAggregateNet_Object = MibTableColumn
fsMIStdOspfAreaAggregateNet = _FsMIStdOspfAreaAggregateNet_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 13, 1, 3),
    _FsMIStdOspfAreaAggregateNet_Type()
)
fsMIStdOspfAreaAggregateNet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdOspfAreaAggregateNet.setStatus("current")
_FsMIStdOspfAreaAggregateMask_Type = IpAddress
_FsMIStdOspfAreaAggregateMask_Object = MibTableColumn
fsMIStdOspfAreaAggregateMask = _FsMIStdOspfAreaAggregateMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 13, 1, 4),
    _FsMIStdOspfAreaAggregateMask_Type()
)
fsMIStdOspfAreaAggregateMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdOspfAreaAggregateMask.setStatus("current")
_FsMIStdOspfAreaAggregateStatus_Type = RowStatus
_FsMIStdOspfAreaAggregateStatus_Object = MibTableColumn
fsMIStdOspfAreaAggregateStatus = _FsMIStdOspfAreaAggregateStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 13, 1, 5),
    _FsMIStdOspfAreaAggregateStatus_Type()
)
fsMIStdOspfAreaAggregateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfAreaAggregateStatus.setStatus("current")


class _FsMIStdOspfAreaAggregateEffect_Type(Integer32):
    """Custom type fsMIStdOspfAreaAggregateEffect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertiseMatching", 1),
          ("doNotAdvertiseMatching", 2))
    )


_FsMIStdOspfAreaAggregateEffect_Type.__name__ = "Integer32"
_FsMIStdOspfAreaAggregateEffect_Object = MibTableColumn
fsMIStdOspfAreaAggregateEffect = _FsMIStdOspfAreaAggregateEffect_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 146, 13, 1, 6),
    _FsMIStdOspfAreaAggregateEffect_Type()
)
fsMIStdOspfAreaAggregateEffect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdOspfAreaAggregateEffect.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-MISTDOSPF-MIB",
    **{"AreaID": AreaID,
       "RouterID": RouterID,
       "Metric": Metric,
       "BigMetric": BigMetric,
       "Status": Status,
       "PositiveInteger": PositiveInteger,
       "HelloRange": HelloRange,
       "UpToMaxAge": UpToMaxAge,
       "DesignatedRouterPriority": DesignatedRouterPriority,
       "TOSType": TOSType,
       "fsMIStdOspf": fsMIStdOspf,
       "fsMIStdOspfGeneralGroup": fsMIStdOspfGeneralGroup,
       "fsMIStdOspfTable": fsMIStdOspfTable,
       "fsMIStdOspfEntry": fsMIStdOspfEntry,
       "fsMIStdOspfContextId": fsMIStdOspfContextId,
       "fsMIStdOspfRouterId": fsMIStdOspfRouterId,
       "fsMIStdOspfAdminStat": fsMIStdOspfAdminStat,
       "fsMIStdOspfVersionNumber": fsMIStdOspfVersionNumber,
       "fsMIStdOspfAreaBdrRtrStatus": fsMIStdOspfAreaBdrRtrStatus,
       "fsMIStdOspfASBdrRtrStatus": fsMIStdOspfASBdrRtrStatus,
       "fsMIStdOspfExternLsaCount": fsMIStdOspfExternLsaCount,
       "fsMIStdOspfExternLsaCksumSum": fsMIStdOspfExternLsaCksumSum,
       "fsMIStdOspfTOSSupport": fsMIStdOspfTOSSupport,
       "fsMIStdOspfOriginateNewLsas": fsMIStdOspfOriginateNewLsas,
       "fsMIStdOspfRxNewLsas": fsMIStdOspfRxNewLsas,
       "fsMIStdOspfExtLsdbLimit": fsMIStdOspfExtLsdbLimit,
       "fsMIStdOspfMulticastExtensions": fsMIStdOspfMulticastExtensions,
       "fsMIStdOspfExitOverflowInterval": fsMIStdOspfExitOverflowInterval,
       "fsMIStdOspfDemandExtensions": fsMIStdOspfDemandExtensions,
       "fsMIStdOspfStatus": fsMIStdOspfStatus,
       "fsMIStdOspfAreaTable": fsMIStdOspfAreaTable,
       "fsMIStdOspfAreaEntry": fsMIStdOspfAreaEntry,
       "fsMIStdOspfAreaId": fsMIStdOspfAreaId,
       "fsMIStdOspfImportAsExtern": fsMIStdOspfImportAsExtern,
       "fsMIStdOspfSpfRuns": fsMIStdOspfSpfRuns,
       "fsMIStdOspfAreaBdrRtrCount": fsMIStdOspfAreaBdrRtrCount,
       "fsMIStdOspfAsBdrRtrCount": fsMIStdOspfAsBdrRtrCount,
       "fsMIStdOspfAreaLsaCount": fsMIStdOspfAreaLsaCount,
       "fsMIStdOspfAreaLsaCksumSum": fsMIStdOspfAreaLsaCksumSum,
       "fsMIStdOspfAreaSummary": fsMIStdOspfAreaSummary,
       "fsMIStdOspfAreaStatus": fsMIStdOspfAreaStatus,
       "fsMIStdOspfStubAreaTable": fsMIStdOspfStubAreaTable,
       "fsMIStdOspfStubAreaEntry": fsMIStdOspfStubAreaEntry,
       "fsMIStdOspfStubAreaId": fsMIStdOspfStubAreaId,
       "fsMIStdOspfStubTOS": fsMIStdOspfStubTOS,
       "fsMIStdOspfStubMetric": fsMIStdOspfStubMetric,
       "fsMIStdOspfStubStatus": fsMIStdOspfStubStatus,
       "fsMIStdOspfStubMetricType": fsMIStdOspfStubMetricType,
       "fsMIStdOspfLsdbTable": fsMIStdOspfLsdbTable,
       "fsMIStdOspfLsdbEntry": fsMIStdOspfLsdbEntry,
       "fsMIStdOspfLsdbAreaId": fsMIStdOspfLsdbAreaId,
       "fsMIStdOspfLsdbType": fsMIStdOspfLsdbType,
       "fsMIStdOspfLsdbLsid": fsMIStdOspfLsdbLsid,
       "fsMIStdOspfLsdbRouterId": fsMIStdOspfLsdbRouterId,
       "fsMIStdOspfLsdbSequence": fsMIStdOspfLsdbSequence,
       "fsMIStdOspfLsdbAge": fsMIStdOspfLsdbAge,
       "fsMIStdOspfLsdbChecksum": fsMIStdOspfLsdbChecksum,
       "fsMIStdOspfLsdbAdvertisement": fsMIStdOspfLsdbAdvertisement,
       "fsMIStdOspfHostTable": fsMIStdOspfHostTable,
       "fsMIStdOspfHostEntry": fsMIStdOspfHostEntry,
       "fsMIStdOspfHostIpAddress": fsMIStdOspfHostIpAddress,
       "fsMIStdOspfHostTOS": fsMIStdOspfHostTOS,
       "fsMIStdOspfHostMetric": fsMIStdOspfHostMetric,
       "fsMIStdOspfHostStatus": fsMIStdOspfHostStatus,
       "fsMIStdOspfHostAreaID": fsMIStdOspfHostAreaID,
       "fsMIStdOspfIfTable": fsMIStdOspfIfTable,
       "fsMIStdOspfIfEntry": fsMIStdOspfIfEntry,
       "fsMIStdOspfIfIpAddress": fsMIStdOspfIfIpAddress,
       "fsMIStdOspfAddressLessIf": fsMIStdOspfAddressLessIf,
       "fsMIStdOspfIfAreaId": fsMIStdOspfIfAreaId,
       "fsMIStdOspfIfType": fsMIStdOspfIfType,
       "fsMIStdOspfIfAdminStat": fsMIStdOspfIfAdminStat,
       "fsMIStdOspfIfRtrPriority": fsMIStdOspfIfRtrPriority,
       "fsMIStdOspfIfTransitDelay": fsMIStdOspfIfTransitDelay,
       "fsMIStdOspfIfRetransInterval": fsMIStdOspfIfRetransInterval,
       "fsMIStdOspfIfHelloInterval": fsMIStdOspfIfHelloInterval,
       "fsMIStdOspfIfRtrDeadInterval": fsMIStdOspfIfRtrDeadInterval,
       "fsMIStdOspfIfPollInterval": fsMIStdOspfIfPollInterval,
       "fsMIStdOspfIfState": fsMIStdOspfIfState,
       "fsMIStdOspfIfDesignatedRouter": fsMIStdOspfIfDesignatedRouter,
       "fsMIStdOspfIfBackupDesignatedRouter": fsMIStdOspfIfBackupDesignatedRouter,
       "fsMIStdOspfIfEvents": fsMIStdOspfIfEvents,
       "fsMIStdOspfIfAuthKey": fsMIStdOspfIfAuthKey,
       "fsMIStdOspfIfStatus": fsMIStdOspfIfStatus,
       "fsMIStdOspfIfMulticastForwarding": fsMIStdOspfIfMulticastForwarding,
       "fsMIStdOspfIfDemand": fsMIStdOspfIfDemand,
       "fsMIStdOspfIfAuthType": fsMIStdOspfIfAuthType,
       "fsMIStdOspfIfCryptoAuthType": fsMIStdOspfIfCryptoAuthType,
       "fsMIStdOspfIfMetricTable": fsMIStdOspfIfMetricTable,
       "fsMIStdOspfIfMetricEntry": fsMIStdOspfIfMetricEntry,
       "fsMIStdOspfIfMetricIpAddress": fsMIStdOspfIfMetricIpAddress,
       "fsMIStdOspfIfMetricAddressLessIf": fsMIStdOspfIfMetricAddressLessIf,
       "fsMIStdOspfIfMetricTOS": fsMIStdOspfIfMetricTOS,
       "fsMIStdOspfIfMetricValue": fsMIStdOspfIfMetricValue,
       "fsMIStdOspfIfMetricStatus": fsMIStdOspfIfMetricStatus,
       "fsMIStdOspfVirtIfTable": fsMIStdOspfVirtIfTable,
       "fsMIStdOspfVirtIfEntry": fsMIStdOspfVirtIfEntry,
       "fsMIStdOspfVirtIfAreaId": fsMIStdOspfVirtIfAreaId,
       "fsMIStdOspfVirtIfNeighbor": fsMIStdOspfVirtIfNeighbor,
       "fsMIStdOspfVirtIfTransitDelay": fsMIStdOspfVirtIfTransitDelay,
       "fsMIStdOspfVirtIfRetransInterval": fsMIStdOspfVirtIfRetransInterval,
       "fsMIStdOspfVirtIfHelloInterval": fsMIStdOspfVirtIfHelloInterval,
       "fsMIStdOspfVirtIfRtrDeadInterval": fsMIStdOspfVirtIfRtrDeadInterval,
       "fsMIStdOspfVirtIfState": fsMIStdOspfVirtIfState,
       "fsMIStdOspfVirtIfEvents": fsMIStdOspfVirtIfEvents,
       "fsMIStdOspfVirtIfAuthKey": fsMIStdOspfVirtIfAuthKey,
       "fsMIStdOspfVirtIfStatus": fsMIStdOspfVirtIfStatus,
       "fsMIStdOspfVirtIfAuthType": fsMIStdOspfVirtIfAuthType,
       "fsMIStdOspfVirtIfCryptoAuthType": fsMIStdOspfVirtIfCryptoAuthType,
       "fsMIStdOspfNbrTable": fsMIStdOspfNbrTable,
       "fsMIStdOspfNbrEntry": fsMIStdOspfNbrEntry,
       "fsMIStdOspfNbrIpAddr": fsMIStdOspfNbrIpAddr,
       "fsMIStdOspfNbrAddressLessIndex": fsMIStdOspfNbrAddressLessIndex,
       "fsMIStdOspfNbrRtrId": fsMIStdOspfNbrRtrId,
       "fsMIStdOspfNbrOptions": fsMIStdOspfNbrOptions,
       "fsMIStdOspfNbrPriority": fsMIStdOspfNbrPriority,
       "fsMIStdOspfNbrState": fsMIStdOspfNbrState,
       "fsMIStdOspfNbrEvents": fsMIStdOspfNbrEvents,
       "fsMIStdOspfNbrLsRetransQLen": fsMIStdOspfNbrLsRetransQLen,
       "fsMIStdOspfNbmaNbrStatus": fsMIStdOspfNbmaNbrStatus,
       "fsMIStdOspfNbmaNbrPermanence": fsMIStdOspfNbmaNbrPermanence,
       "fsMIStdOspfNbrHelloSuppressed": fsMIStdOspfNbrHelloSuppressed,
       "fsMIStdOspfVirtNbrTable": fsMIStdOspfVirtNbrTable,
       "fsMIStdOspfVirtNbrEntry": fsMIStdOspfVirtNbrEntry,
       "fsMIStdOspfVirtNbrArea": fsMIStdOspfVirtNbrArea,
       "fsMIStdOspfVirtNbrRtrId": fsMIStdOspfVirtNbrRtrId,
       "fsMIStdOspfVirtNbrIpAddr": fsMIStdOspfVirtNbrIpAddr,
       "fsMIStdOspfVirtNbrOptions": fsMIStdOspfVirtNbrOptions,
       "fsMIStdOspfVirtNbrState": fsMIStdOspfVirtNbrState,
       "fsMIStdOspfVirtNbrEvents": fsMIStdOspfVirtNbrEvents,
       "fsMIStdOspfVirtNbrLsRetransQLen": fsMIStdOspfVirtNbrLsRetransQLen,
       "fsMIStdOspfVirtNbrHelloSuppressed": fsMIStdOspfVirtNbrHelloSuppressed,
       "fsMIStdOspfExtLsdbTable": fsMIStdOspfExtLsdbTable,
       "fsMIStdOspfExtLsdbEntry": fsMIStdOspfExtLsdbEntry,
       "fsMIStdOspfExtLsdbType": fsMIStdOspfExtLsdbType,
       "fsMIStdOspfExtLsdbLsid": fsMIStdOspfExtLsdbLsid,
       "fsMIStdOspfExtLsdbRouterId": fsMIStdOspfExtLsdbRouterId,
       "fsMIStdOspfExtLsdbSequence": fsMIStdOspfExtLsdbSequence,
       "fsMIStdOspfExtLsdbAge": fsMIStdOspfExtLsdbAge,
       "fsMIStdOspfExtLsdbChecksum": fsMIStdOspfExtLsdbChecksum,
       "fsMIStdOspfExtLsdbAdvertisement": fsMIStdOspfExtLsdbAdvertisement,
       "fsMIStdOspfRouteGroup": fsMIStdOspfRouteGroup,
       "fsMIStdOspfIntraArea": fsMIStdOspfIntraArea,
       "fsMIStdOspfInterArea": fsMIStdOspfInterArea,
       "fsMIStdOspfExternalType1": fsMIStdOspfExternalType1,
       "fsMIStdOspfExternalType2": fsMIStdOspfExternalType2,
       "fsMIStdOspfAreaAggregateTable": fsMIStdOspfAreaAggregateTable,
       "fsMIStdOspfAreaAggregateEntry": fsMIStdOspfAreaAggregateEntry,
       "fsMIStdOspfAreaAggregateAreaID": fsMIStdOspfAreaAggregateAreaID,
       "fsMIStdOspfAreaAggregateLsdbType": fsMIStdOspfAreaAggregateLsdbType,
       "fsMIStdOspfAreaAggregateNet": fsMIStdOspfAreaAggregateNet,
       "fsMIStdOspfAreaAggregateMask": fsMIStdOspfAreaAggregateMask,
       "fsMIStdOspfAreaAggregateStatus": fsMIStdOspfAreaAggregateStatus,
       "fsMIStdOspfAreaAggregateEffect": fsMIStdOspfAreaAggregateEffect}
)
