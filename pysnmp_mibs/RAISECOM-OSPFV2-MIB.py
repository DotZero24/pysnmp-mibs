# SNMP MIB module (RAISECOM-OSPFV2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-OSPFV2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:29 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

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

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

raisecomOspf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47)
)
if mibBuilder.loadTexts:
    raisecomOspf.setRevisions(
        ("2011-09-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ProcessID(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-0"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )



class AreaID(TextualConvention, IpAddress):
    status = "current"


class RouterID(TextualConvention, IpAddress):
    status = "current"


class Metric(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-0"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class BigMetric(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-0"
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
    displayHint = "d-0"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class HelloRange(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-0"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class UpToMaxAge(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-0"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )



class DesignatedRouterPriority(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-0"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class OspfAuthenticationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("simplePassword", 1),
          ("md5", 2))
    )



# MIB Managed Objects in the order of their OIDs

_RaisecomOspfNotifications_ObjectIdentity = ObjectIdentity
raisecomOspfNotifications = _RaisecomOspfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1)
)
_RaisecomOspfTrapControlTable_Object = MibTable
raisecomOspfTrapControlTable = _RaisecomOspfTrapControlTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 1)
)
if mibBuilder.loadTexts:
    raisecomOspfTrapControlTable.setStatus("current")
_RaisecomOspfTrapControlEntry_Object = MibTableRow
raisecomOspfTrapControlEntry = _RaisecomOspfTrapControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 1, 1)
)
raisecomOspfTrapControlEntry.setIndexNames(
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
)
if mibBuilder.loadTexts:
    raisecomOspfTrapControlEntry.setStatus("current")


class _RaisecomOspfSetTrap_Type(EnableVar):
    """Custom type raisecomOspfSetTrap based on EnableVar"""
    defaultValue = 2


_RaisecomOspfSetTrap_Type.__name__ = "EnableVar"
_RaisecomOspfSetTrap_Object = MibTableColumn
raisecomOspfSetTrap = _RaisecomOspfSetTrap_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 1, 1, 1),
    _RaisecomOspfSetTrap_Type()
)
raisecomOspfSetTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomOspfSetTrap.setStatus("current")


class _RaisecomOspfConfigErrorType_Type(Integer32):
    """Custom type raisecomOspfConfigErrorType based on Integer32"""
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
        *(("badVersion", 1),
          ("areaMismatch", 2),
          ("unknownNbmaNbr", 3),
          ("unknownVirtualNbr", 4),
          ("authTypeMismatch", 5),
          ("authFailure", 6),
          ("netMaskMismatch", 7),
          ("helloIntervalMismatch", 8),
          ("deadIntervalMismatch", 9),
          ("optionMismatch", 10))
    )


_RaisecomOspfConfigErrorType_Type.__name__ = "Integer32"
_RaisecomOspfConfigErrorType_Object = MibTableColumn
raisecomOspfConfigErrorType = _RaisecomOspfConfigErrorType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 1, 1, 2),
    _RaisecomOspfConfigErrorType_Type()
)
raisecomOspfConfigErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfConfigErrorType.setStatus("current")


class _RaisecomOspfPacketType_Type(Integer32):
    """Custom type raisecomOspfPacketType based on Integer32"""
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
        *(("hello", 1),
          ("dbDescript", 2),
          ("lsReq", 3),
          ("lsUpdate", 4),
          ("lsAck", 5))
    )


_RaisecomOspfPacketType_Type.__name__ = "Integer32"
_RaisecomOspfPacketType_Object = MibTableColumn
raisecomOspfPacketType = _RaisecomOspfPacketType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 1, 1, 3),
    _RaisecomOspfPacketType_Type()
)
raisecomOspfPacketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfPacketType.setStatus("current")
_RaisecomOspfPacketSrc_Type = IpAddress
_RaisecomOspfPacketSrc_Object = MibTableColumn
raisecomOspfPacketSrc = _RaisecomOspfPacketSrc_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 1, 1, 4),
    _RaisecomOspfPacketSrc_Type()
)
raisecomOspfPacketSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfPacketSrc.setStatus("current")
_RaisecomOspfTraps_ObjectIdentity = ObjectIdentity
raisecomOspfTraps = _RaisecomOspfTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 2)
)
_RaisecomOspfObjects_ObjectIdentity = ObjectIdentity
raisecomOspfObjects = _RaisecomOspfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2)
)
_RaisecomOspfGlobalTable_Object = MibTable
raisecomOspfGlobalTable = _RaisecomOspfGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1)
)
if mibBuilder.loadTexts:
    raisecomOspfGlobalTable.setStatus("current")
_RaisecomOspfGlobalEntry_Object = MibTableRow
raisecomOspfGlobalEntry = _RaisecomOspfGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1)
)
raisecomOspfGlobalEntry.setIndexNames(
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
)
if mibBuilder.loadTexts:
    raisecomOspfGlobalEntry.setStatus("current")
_RaisecomOspfProcessId_Type = ProcessID
_RaisecomOspfProcessId_Object = MibTableColumn
raisecomOspfProcessId = _RaisecomOspfProcessId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 1),
    _RaisecomOspfProcessId_Type()
)
raisecomOspfProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfProcessId.setStatus("current")
_RaisecomOspfRouterId_Type = RouterID
_RaisecomOspfRouterId_Object = MibTableColumn
raisecomOspfRouterId = _RaisecomOspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 2),
    _RaisecomOspfRouterId_Type()
)
raisecomOspfRouterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfRouterId.setStatus("current")


class _RaisecomOspfAdminStat_Type(EnableVar):
    """Custom type raisecomOspfAdminStat based on EnableVar"""
    defaultValue = 2


_RaisecomOspfAdminStat_Type.__name__ = "EnableVar"
_RaisecomOspfAdminStat_Object = MibTableColumn
raisecomOspfAdminStat = _RaisecomOspfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 3),
    _RaisecomOspfAdminStat_Type()
)
raisecomOspfAdminStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfAdminStat.setStatus("current")


class _RaisecomOspfVersionNumber_Type(Integer32):
    """Custom type raisecomOspfVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("version2", 2)
    )


_RaisecomOspfVersionNumber_Type.__name__ = "Integer32"
_RaisecomOspfVersionNumber_Object = MibTableColumn
raisecomOspfVersionNumber = _RaisecomOspfVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 4),
    _RaisecomOspfVersionNumber_Type()
)
raisecomOspfVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfVersionNumber.setStatus("current")
_RaisecomOspfAreaBdrRtrStatus_Type = TruthValue
_RaisecomOspfAreaBdrRtrStatus_Object = MibTableColumn
raisecomOspfAreaBdrRtrStatus = _RaisecomOspfAreaBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 5),
    _RaisecomOspfAreaBdrRtrStatus_Type()
)
raisecomOspfAreaBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfAreaBdrRtrStatus.setStatus("current")
_RaisecomOspfASBdrRtrStatus_Type = TruthValue
_RaisecomOspfASBdrRtrStatus_Object = MibTableColumn
raisecomOspfASBdrRtrStatus = _RaisecomOspfASBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 6),
    _RaisecomOspfASBdrRtrStatus_Type()
)
raisecomOspfASBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfASBdrRtrStatus.setStatus("current")
_RaisecomOspfExternLsaCount_Type = Gauge32
_RaisecomOspfExternLsaCount_Object = MibTableColumn
raisecomOspfExternLsaCount = _RaisecomOspfExternLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 7),
    _RaisecomOspfExternLsaCount_Type()
)
raisecomOspfExternLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfExternLsaCount.setStatus("current")
_RaisecomOspfExternLsaCksumSum_Type = Integer32
_RaisecomOspfExternLsaCksumSum_Object = MibTableColumn
raisecomOspfExternLsaCksumSum = _RaisecomOspfExternLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 8),
    _RaisecomOspfExternLsaCksumSum_Type()
)
raisecomOspfExternLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfExternLsaCksumSum.setStatus("current")
_RaisecomOspfOriginateNewLsas_Type = Counter32
_RaisecomOspfOriginateNewLsas_Object = MibTableColumn
raisecomOspfOriginateNewLsas = _RaisecomOspfOriginateNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 9),
    _RaisecomOspfOriginateNewLsas_Type()
)
raisecomOspfOriginateNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfOriginateNewLsas.setStatus("current")
_RaisecomOspfRxNewLsas_Type = Counter32
_RaisecomOspfRxNewLsas_Object = MibTableColumn
raisecomOspfRxNewLsas = _RaisecomOspfRxNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 10),
    _RaisecomOspfRxNewLsas_Type()
)
raisecomOspfRxNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfRxNewLsas.setStatus("current")


class _RaisecomOspfExtLsdbLimit_Type(Integer32):
    """Custom type raisecomOspfExtLsdbLimit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_RaisecomOspfExtLsdbLimit_Type.__name__ = "Integer32"
_RaisecomOspfExtLsdbLimit_Object = MibTableColumn
raisecomOspfExtLsdbLimit = _RaisecomOspfExtLsdbLimit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 11),
    _RaisecomOspfExtLsdbLimit_Type()
)
raisecomOspfExtLsdbLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfExtLsdbLimit.setStatus("current")


class _RaisecomOspfExitOverflowInterval_Type(PositiveInteger):
    """Custom type raisecomOspfExitOverflowInterval based on PositiveInteger"""
    defaultValue = 0


_RaisecomOspfExitOverflowInterval_Type.__name__ = "PositiveInteger"
_RaisecomOspfExitOverflowInterval_Object = MibTableColumn
raisecomOspfExitOverflowInterval = _RaisecomOspfExitOverflowInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 12),
    _RaisecomOspfExitOverflowInterval_Type()
)
raisecomOspfExitOverflowInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfExitOverflowInterval.setStatus("current")


class _RaisecomOspfReferenceBandwidth_Type(Unsigned32):
    """Custom type raisecomOspfReferenceBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4296967),
    )


_RaisecomOspfReferenceBandwidth_Type.__name__ = "Unsigned32"
_RaisecomOspfReferenceBandwidth_Object = MibTableColumn
raisecomOspfReferenceBandwidth = _RaisecomOspfReferenceBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 13),
    _RaisecomOspfReferenceBandwidth_Type()
)
raisecomOspfReferenceBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfReferenceBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    raisecomOspfReferenceBandwidth.setUnits("millionbits per second")
_RaisecomOspfAsLsaCount_Type = Gauge32
_RaisecomOspfAsLsaCount_Object = MibTableColumn
raisecomOspfAsLsaCount = _RaisecomOspfAsLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 14),
    _RaisecomOspfAsLsaCount_Type()
)
raisecomOspfAsLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfAsLsaCount.setStatus("current")
_RaisecomOspfAsLsaCksumSum_Type = Unsigned32
_RaisecomOspfAsLsaCksumSum_Object = MibTableColumn
raisecomOspfAsLsaCksumSum = _RaisecomOspfAsLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 15),
    _RaisecomOspfAsLsaCksumSum_Type()
)
raisecomOspfAsLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfAsLsaCksumSum.setStatus("current")
_RaisecomOspfStubRouterSupport_Type = TruthValue
_RaisecomOspfStubRouterSupport_Object = MibTableColumn
raisecomOspfStubRouterSupport = _RaisecomOspfStubRouterSupport_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 16),
    _RaisecomOspfStubRouterSupport_Type()
)
raisecomOspfStubRouterSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfStubRouterSupport.setStatus("current")


class _RaisecomOspfStubRouterAdvertisement_Type(Integer32):
    """Custom type raisecomOspfStubRouterAdvertisement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNotAdvertise", 1),
          ("advertise", 2))
    )


_RaisecomOspfStubRouterAdvertisement_Type.__name__ = "Integer32"
_RaisecomOspfStubRouterAdvertisement_Object = MibTableColumn
raisecomOspfStubRouterAdvertisement = _RaisecomOspfStubRouterAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 17),
    _RaisecomOspfStubRouterAdvertisement_Type()
)
raisecomOspfStubRouterAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfStubRouterAdvertisement.setStatus("current")


class _RaisecomOspfAdminDistance_Type(Integer32):
    """Custom type raisecomOspfAdminDistance based on Integer32"""
    defaultValue = 110

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RaisecomOspfAdminDistance_Type.__name__ = "Integer32"
_RaisecomOspfAdminDistance_Object = MibTableColumn
raisecomOspfAdminDistance = _RaisecomOspfAdminDistance_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 18),
    _RaisecomOspfAdminDistance_Type()
)
raisecomOspfAdminDistance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfAdminDistance.setStatus("current")


class _RaisecomOspfSpfInterval_Type(Integer32):
    """Custom type raisecomOspfSpfInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_RaisecomOspfSpfInterval_Type.__name__ = "Integer32"
_RaisecomOspfSpfInterval_Object = MibTableColumn
raisecomOspfSpfInterval = _RaisecomOspfSpfInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 19),
    _RaisecomOspfSpfInterval_Type()
)
raisecomOspfSpfInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfSpfInterval.setStatus("current")


class _RaisecomOspfReset_Type(TruthValue):
    """Custom type raisecomOspfReset based on TruthValue"""
    defaultValue = 2


_RaisecomOspfReset_Type.__name__ = "TruthValue"
_RaisecomOspfReset_Object = MibTableColumn
raisecomOspfReset = _RaisecomOspfReset_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 20),
    _RaisecomOspfReset_Type()
)
raisecomOspfReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfReset.setStatus("current")


class _RaisecomOspfExportMetric_Type(Integer32):
    """Custom type raisecomOspfExportMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_RaisecomOspfExportMetric_Type.__name__ = "Integer32"
_RaisecomOspfExportMetric_Object = MibTableColumn
raisecomOspfExportMetric = _RaisecomOspfExportMetric_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 21),
    _RaisecomOspfExportMetric_Type()
)
raisecomOspfExportMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfExportMetric.setStatus("current")
_RaisecomOspfExportTag_Type = Integer32
_RaisecomOspfExportTag_Object = MibTableColumn
raisecomOspfExportTag = _RaisecomOspfExportTag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 22),
    _RaisecomOspfExportTag_Type()
)
raisecomOspfExportTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfExportTag.setStatus("current")


class _RaisecomOspfExportType_Type(Integer32):
    """Custom type raisecomOspfExportType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type1", 1),
          ("type2", 2))
    )


_RaisecomOspfExportType_Type.__name__ = "Integer32"
_RaisecomOspfExportType_Object = MibTableColumn
raisecomOspfExportType = _RaisecomOspfExportType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 23),
    _RaisecomOspfExportType_Type()
)
raisecomOspfExportType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfExportType.setStatus("current")
_RaisecomOspfNetCounts_Type = Integer32
_RaisecomOspfNetCounts_Object = MibTableColumn
raisecomOspfNetCounts = _RaisecomOspfNetCounts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 24),
    _RaisecomOspfNetCounts_Type()
)
raisecomOspfNetCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfNetCounts.setStatus("current")
_RaisecomOspfAreaCounts_Type = Integer32
_RaisecomOspfAreaCounts_Object = MibTableColumn
raisecomOspfAreaCounts = _RaisecomOspfAreaCounts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 25),
    _RaisecomOspfAreaCounts_Type()
)
raisecomOspfAreaCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfAreaCounts.setStatus("current")
_RaisecomOspfNssaAreaCounts_Type = Integer32
_RaisecomOspfNssaAreaCounts_Object = MibTableColumn
raisecomOspfNssaAreaCounts = _RaisecomOspfNssaAreaCounts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 26),
    _RaisecomOspfNssaAreaCounts_Type()
)
raisecomOspfNssaAreaCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfNssaAreaCounts.setStatus("current")
_RaisecomOspfSpfCounts_Type = Integer32
_RaisecomOspfSpfCounts_Object = MibTableColumn
raisecomOspfSpfCounts = _RaisecomOspfSpfCounts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 27),
    _RaisecomOspfSpfCounts_Type()
)
raisecomOspfSpfCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfSpfCounts.setStatus("current")
_RaisecomOspfGlobalStatus_Type = RowStatus
_RaisecomOspfGlobalStatus_Object = MibTableColumn
raisecomOspfGlobalStatus = _RaisecomOspfGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 28),
    _RaisecomOspfGlobalStatus_Type()
)
raisecomOspfGlobalStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfGlobalStatus.setStatus("current")


class _RaisecomOspfRedistributeRouteLimit_Type(Integer32):
    """Custom type raisecomOspfRedistributeRouteLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RaisecomOspfRedistributeRouteLimit_Type.__name__ = "Integer32"
_RaisecomOspfRedistributeRouteLimit_Object = MibTableColumn
raisecomOspfRedistributeRouteLimit = _RaisecomOspfRedistributeRouteLimit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 1, 1, 29),
    _RaisecomOspfRedistributeRouteLimit_Type()
)
raisecomOspfRedistributeRouteLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfRedistributeRouteLimit.setStatus("current")
_RaisecomOspfAreaTable_Object = MibTable
raisecomOspfAreaTable = _RaisecomOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 2)
)
if mibBuilder.loadTexts:
    raisecomOspfAreaTable.setStatus("current")
_RaisecomOspfAreaEntry_Object = MibTableRow
raisecomOspfAreaEntry = _RaisecomOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 2, 1)
)
raisecomOspfAreaEntry.setIndexNames(
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfAreaId"),
)
if mibBuilder.loadTexts:
    raisecomOspfAreaEntry.setStatus("current")
_RaisecomOspfAreaId_Type = AreaID
_RaisecomOspfAreaId_Object = MibTableColumn
raisecomOspfAreaId = _RaisecomOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 2, 1, 1),
    _RaisecomOspfAreaId_Type()
)
raisecomOspfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfAreaId.setStatus("current")


class _RaisecomOspfAuthType_Type(OspfAuthenticationType):
    """Custom type raisecomOspfAuthType based on OspfAuthenticationType"""
    defaultValue = 0


_RaisecomOspfAuthType_Type.__name__ = "OspfAuthenticationType"
_RaisecomOspfAuthType_Object = MibTableColumn
raisecomOspfAuthType = _RaisecomOspfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 2, 1, 2),
    _RaisecomOspfAuthType_Type()
)
raisecomOspfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfAuthType.setStatus("current")


class _RaisecomOspfImportAsExtern_Type(Integer32):
    """Custom type raisecomOspfImportAsExtern based on Integer32"""
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


_RaisecomOspfImportAsExtern_Type.__name__ = "Integer32"
_RaisecomOspfImportAsExtern_Object = MibTableColumn
raisecomOspfImportAsExtern = _RaisecomOspfImportAsExtern_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 2, 1, 3),
    _RaisecomOspfImportAsExtern_Type()
)
raisecomOspfImportAsExtern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfImportAsExtern.setStatus("current")
_RaisecomOspfSpfRuns_Type = Counter32
_RaisecomOspfSpfRuns_Object = MibTableColumn
raisecomOspfSpfRuns = _RaisecomOspfSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 2, 1, 4),
    _RaisecomOspfSpfRuns_Type()
)
raisecomOspfSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfSpfRuns.setStatus("current")
_RaisecomOspfAreaBdrRtrCount_Type = Gauge32
_RaisecomOspfAreaBdrRtrCount_Object = MibTableColumn
raisecomOspfAreaBdrRtrCount = _RaisecomOspfAreaBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 2, 1, 5),
    _RaisecomOspfAreaBdrRtrCount_Type()
)
raisecomOspfAreaBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfAreaBdrRtrCount.setStatus("current")
_RaisecomOspfAsBdrRtrCount_Type = Gauge32
_RaisecomOspfAsBdrRtrCount_Object = MibTableColumn
raisecomOspfAsBdrRtrCount = _RaisecomOspfAsBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 2, 1, 6),
    _RaisecomOspfAsBdrRtrCount_Type()
)
raisecomOspfAsBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfAsBdrRtrCount.setStatus("current")
_RaisecomOspfAreaLsaCount_Type = Gauge32
_RaisecomOspfAreaLsaCount_Object = MibTableColumn
raisecomOspfAreaLsaCount = _RaisecomOspfAreaLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 2, 1, 7),
    _RaisecomOspfAreaLsaCount_Type()
)
raisecomOspfAreaLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfAreaLsaCount.setStatus("current")


class _RaisecomOspfAreaLsaCksumSum_Type(Integer32):
    """Custom type raisecomOspfAreaLsaCksumSum based on Integer32"""
    defaultValue = 0


_RaisecomOspfAreaLsaCksumSum_Type.__name__ = "Integer32"
_RaisecomOspfAreaLsaCksumSum_Object = MibTableColumn
raisecomOspfAreaLsaCksumSum = _RaisecomOspfAreaLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 2, 1, 8),
    _RaisecomOspfAreaLsaCksumSum_Type()
)
raisecomOspfAreaLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfAreaLsaCksumSum.setStatus("current")


class _RaisecomOspfAreaSummary_Type(Integer32):
    """Custom type raisecomOspfAreaSummary based on Integer32"""
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


_RaisecomOspfAreaSummary_Type.__name__ = "Integer32"
_RaisecomOspfAreaSummary_Object = MibTableColumn
raisecomOspfAreaSummary = _RaisecomOspfAreaSummary_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 2, 1, 9),
    _RaisecomOspfAreaSummary_Type()
)
raisecomOspfAreaSummary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfAreaSummary.setStatus("current")


class _RaisecomOspfAreaNssaTranslatorRole_Type(Integer32):
    """Custom type raisecomOspfAreaNssaTranslatorRole based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always", 1),
          ("candidate", 2))
    )


_RaisecomOspfAreaNssaTranslatorRole_Type.__name__ = "Integer32"
_RaisecomOspfAreaNssaTranslatorRole_Object = MibTableColumn
raisecomOspfAreaNssaTranslatorRole = _RaisecomOspfAreaNssaTranslatorRole_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 2, 1, 10),
    _RaisecomOspfAreaNssaTranslatorRole_Type()
)
raisecomOspfAreaNssaTranslatorRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfAreaNssaTranslatorRole.setStatus("current")


class _RaisecomOspfAreaNssaTranslatorState_Type(Integer32):
    """Custom type raisecomOspfAreaNssaTranslatorState based on Integer32"""
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
          ("elected", 2),
          ("disabled", 3))
    )


_RaisecomOspfAreaNssaTranslatorState_Type.__name__ = "Integer32"
_RaisecomOspfAreaNssaTranslatorState_Object = MibTableColumn
raisecomOspfAreaNssaTranslatorState = _RaisecomOspfAreaNssaTranslatorState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 2, 1, 11),
    _RaisecomOspfAreaNssaTranslatorState_Type()
)
raisecomOspfAreaNssaTranslatorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfAreaNssaTranslatorState.setStatus("current")


class _RaisecomOspfAreaNssaTranslatorStabilityInterval_Type(PositiveInteger):
    """Custom type raisecomOspfAreaNssaTranslatorStabilityInterval based on PositiveInteger"""
    defaultValue = 40


_RaisecomOspfAreaNssaTranslatorStabilityInterval_Type.__name__ = "PositiveInteger"
_RaisecomOspfAreaNssaTranslatorStabilityInterval_Object = MibTableColumn
raisecomOspfAreaNssaTranslatorStabilityInterval = _RaisecomOspfAreaNssaTranslatorStabilityInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 2, 1, 12),
    _RaisecomOspfAreaNssaTranslatorStabilityInterval_Type()
)
raisecomOspfAreaNssaTranslatorStabilityInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfAreaNssaTranslatorStabilityInterval.setStatus("current")
if mibBuilder.loadTexts:
    raisecomOspfAreaNssaTranslatorStabilityInterval.setUnits("seconds")
_RaisecomOspfAreaNssaTranslatorEvents_Type = Counter32
_RaisecomOspfAreaNssaTranslatorEvents_Object = MibTableColumn
raisecomOspfAreaNssaTranslatorEvents = _RaisecomOspfAreaNssaTranslatorEvents_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 2, 1, 13),
    _RaisecomOspfAreaNssaTranslatorEvents_Type()
)
raisecomOspfAreaNssaTranslatorEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfAreaNssaTranslatorEvents.setStatus("current")


class _RaisecomOspfAreaDefaultCost_Type(BigMetric):
    """Custom type raisecomOspfAreaDefaultCost based on BigMetric"""
    defaultValue = 1


_RaisecomOspfAreaDefaultCost_Type.__name__ = "BigMetric"
_RaisecomOspfAreaDefaultCost_Object = MibTableColumn
raisecomOspfAreaDefaultCost = _RaisecomOspfAreaDefaultCost_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 2, 1, 14),
    _RaisecomOspfAreaDefaultCost_Type()
)
raisecomOspfAreaDefaultCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfAreaDefaultCost.setStatus("current")


class _RaisecomOspfAreaType_Type(Integer32):
    """Custom type raisecomOspfAreaType based on Integer32"""
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
        *(("backbone", 1),
          ("normal", 2),
          ("stub", 3),
          ("nssa", 4),
          ("transmit", 5))
    )


_RaisecomOspfAreaType_Type.__name__ = "Integer32"
_RaisecomOspfAreaType_Object = MibTableColumn
raisecomOspfAreaType = _RaisecomOspfAreaType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 2, 1, 15),
    _RaisecomOspfAreaType_Type()
)
raisecomOspfAreaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfAreaType.setStatus("current")
_RaisecomOspfAreaAbrCount_Type = Integer32
_RaisecomOspfAreaAbrCount_Object = MibTableColumn
raisecomOspfAreaAbrCount = _RaisecomOspfAreaAbrCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 2, 1, 16),
    _RaisecomOspfAreaAbrCount_Type()
)
raisecomOspfAreaAbrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfAreaAbrCount.setStatus("current")
_RaisecomOspfAreaAsbrCount_Type = Integer32
_RaisecomOspfAreaAsbrCount_Object = MibTableColumn
raisecomOspfAreaAsbrCount = _RaisecomOspfAreaAsbrCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 2, 1, 17),
    _RaisecomOspfAreaAsbrCount_Type()
)
raisecomOspfAreaAsbrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfAreaAsbrCount.setStatus("current")
_RaisecomOspfAreaStatus_Type = RowStatus
_RaisecomOspfAreaStatus_Object = MibTableColumn
raisecomOspfAreaStatus = _RaisecomOspfAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 2, 1, 18),
    _RaisecomOspfAreaStatus_Type()
)
raisecomOspfAreaStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfAreaStatus.setStatus("current")


class _RaisecomOspfAreaFilterInIpPrefixListName_Type(OctetString):
    """Custom type raisecomOspfAreaFilterInIpPrefixListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_RaisecomOspfAreaFilterInIpPrefixListName_Type.__name__ = "OctetString"
_RaisecomOspfAreaFilterInIpPrefixListName_Object = MibTableColumn
raisecomOspfAreaFilterInIpPrefixListName = _RaisecomOspfAreaFilterInIpPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 2, 1, 19),
    _RaisecomOspfAreaFilterInIpPrefixListName_Type()
)
raisecomOspfAreaFilterInIpPrefixListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfAreaFilterInIpPrefixListName.setStatus("current")


class _RaisecomOspfAreaFilterOutIpPrefixListName_Type(OctetString):
    """Custom type raisecomOspfAreaFilterOutIpPrefixListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_RaisecomOspfAreaFilterOutIpPrefixListName_Type.__name__ = "OctetString"
_RaisecomOspfAreaFilterOutIpPrefixListName_Object = MibTableColumn
raisecomOspfAreaFilterOutIpPrefixListName = _RaisecomOspfAreaFilterOutIpPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 2, 1, 20),
    _RaisecomOspfAreaFilterOutIpPrefixListName_Type()
)
raisecomOspfAreaFilterOutIpPrefixListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfAreaFilterOutIpPrefixListName.setStatus("current")
_RaisecomOspfNetWorkTable_Object = MibTable
raisecomOspfNetWorkTable = _RaisecomOspfNetWorkTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 3)
)
if mibBuilder.loadTexts:
    raisecomOspfNetWorkTable.setStatus("current")
_RaisecomOspfNetWorkEntry_Object = MibTableRow
raisecomOspfNetWorkEntry = _RaisecomOspfNetWorkEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 3, 1)
)
raisecomOspfNetWorkEntry.setIndexNames(
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfAreaId"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfNet"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfMask"),
)
if mibBuilder.loadTexts:
    raisecomOspfNetWorkEntry.setStatus("current")
_RaisecomOspfNet_Type = IpAddress
_RaisecomOspfNet_Object = MibTableColumn
raisecomOspfNet = _RaisecomOspfNet_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 3, 1, 1),
    _RaisecomOspfNet_Type()
)
raisecomOspfNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfNet.setStatus("current")
_RaisecomOspfMask_Type = IpAddress
_RaisecomOspfMask_Object = MibTableColumn
raisecomOspfMask = _RaisecomOspfMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 3, 1, 2),
    _RaisecomOspfMask_Type()
)
raisecomOspfMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfMask.setStatus("current")
_RaisecomOspfNetWorkStatus_Type = RowStatus
_RaisecomOspfNetWorkStatus_Object = MibTableColumn
raisecomOspfNetWorkStatus = _RaisecomOspfNetWorkStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 3, 1, 3),
    _RaisecomOspfNetWorkStatus_Type()
)
raisecomOspfNetWorkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfNetWorkStatus.setStatus("current")
_RaisecomOspfStubAreaTable_Object = MibTable
raisecomOspfStubAreaTable = _RaisecomOspfStubAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 4)
)
if mibBuilder.loadTexts:
    raisecomOspfStubAreaTable.setStatus("current")
_RaisecomOspfStubAreaEntry_Object = MibTableRow
raisecomOspfStubAreaEntry = _RaisecomOspfStubAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 4, 1)
)
raisecomOspfStubAreaEntry.setIndexNames(
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfStubAreaId"),
)
if mibBuilder.loadTexts:
    raisecomOspfStubAreaEntry.setStatus("current")
_RaisecomOspfStubAreaId_Type = AreaID
_RaisecomOspfStubAreaId_Object = MibTableColumn
raisecomOspfStubAreaId = _RaisecomOspfStubAreaId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 4, 1, 1),
    _RaisecomOspfStubAreaId_Type()
)
raisecomOspfStubAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfStubAreaId.setStatus("current")
_RaisecomOspfStubAreaOption_Type = TruthValue
_RaisecomOspfStubAreaOption_Object = MibTableColumn
raisecomOspfStubAreaOption = _RaisecomOspfStubAreaOption_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 4, 1, 2),
    _RaisecomOspfStubAreaOption_Type()
)
raisecomOspfStubAreaOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfStubAreaOption.setStatus("current")
_RaisecomOspfStubAreaStatus_Type = RowStatus
_RaisecomOspfStubAreaStatus_Object = MibTableColumn
raisecomOspfStubAreaStatus = _RaisecomOspfStubAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 4, 1, 3),
    _RaisecomOspfStubAreaStatus_Type()
)
raisecomOspfStubAreaStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfStubAreaStatus.setStatus("current")
_RaisecomOspfNssaAreaTable_Object = MibTable
raisecomOspfNssaAreaTable = _RaisecomOspfNssaAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 5)
)
if mibBuilder.loadTexts:
    raisecomOspfNssaAreaTable.setStatus("current")
_RaisecomOspfNssaAreaEntry_Object = MibTableRow
raisecomOspfNssaAreaEntry = _RaisecomOspfNssaAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 5, 1)
)
raisecomOspfNssaAreaEntry.setIndexNames(
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfNssaAreaId"),
)
if mibBuilder.loadTexts:
    raisecomOspfNssaAreaEntry.setStatus("current")
_RaisecomOspfNssaAreaId_Type = AreaID
_RaisecomOspfNssaAreaId_Object = MibTableColumn
raisecomOspfNssaAreaId = _RaisecomOspfNssaAreaId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 5, 1, 1),
    _RaisecomOspfNssaAreaId_Type()
)
raisecomOspfNssaAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfNssaAreaId.setStatus("current")


class _RaisecomOspfNssaAreaOption_Type(Integer32):
    """Custom type raisecomOspfNssaAreaOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RaisecomOspfNssaAreaOption_Type.__name__ = "Integer32"
_RaisecomOspfNssaAreaOption_Object = MibTableColumn
raisecomOspfNssaAreaOption = _RaisecomOspfNssaAreaOption_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 5, 1, 2),
    _RaisecomOspfNssaAreaOption_Type()
)
raisecomOspfNssaAreaOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfNssaAreaOption.setStatus("current")
_RaisecomOspfNssaAreaStatus_Type = RowStatus
_RaisecomOspfNssaAreaStatus_Object = MibTableColumn
raisecomOspfNssaAreaStatus = _RaisecomOspfNssaAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 5, 1, 3),
    _RaisecomOspfNssaAreaStatus_Type()
)
raisecomOspfNssaAreaStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfNssaAreaStatus.setStatus("current")
_RaisecomOspfIfTable_Object = MibTable
raisecomOspfIfTable = _RaisecomOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6)
)
if mibBuilder.loadTexts:
    raisecomOspfIfTable.setStatus("current")
_RaisecomOspfIfEntry_Object = MibTableRow
raisecomOspfIfEntry = _RaisecomOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1)
)
raisecomOspfIfEntry.setIndexNames(
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfAddressLessIf"),
)
if mibBuilder.loadTexts:
    raisecomOspfIfEntry.setStatus("current")
_RaisecomOspfAddressLessIf_Type = InterfaceIndexOrZero
_RaisecomOspfAddressLessIf_Object = MibTableColumn
raisecomOspfAddressLessIf = _RaisecomOspfAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 1),
    _RaisecomOspfAddressLessIf_Type()
)
raisecomOspfAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfAddressLessIf.setStatus("current")
_RaisecomOspfIfIpAddress_Type = IpAddress
_RaisecomOspfIfIpAddress_Object = MibTableColumn
raisecomOspfIfIpAddress = _RaisecomOspfIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 2),
    _RaisecomOspfIfIpAddress_Type()
)
raisecomOspfIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfIfIpAddress.setStatus("current")


class _RaisecomOspfIfAreaId_Type(AreaID):
    """Custom type raisecomOspfIfAreaId based on AreaID"""
    defaultHexValue = "00000000"


_RaisecomOspfIfAreaId_Type.__name__ = "AreaID"
_RaisecomOspfIfAreaId_Object = MibTableColumn
raisecomOspfIfAreaId = _RaisecomOspfIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 3),
    _RaisecomOspfIfAreaId_Type()
)
raisecomOspfIfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfIfAreaId.setStatus("current")


class _RaisecomOspfIfType_Type(Integer32):
    """Custom type raisecomOspfIfType based on Integer32"""
    defaultValue = 1

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


_RaisecomOspfIfType_Type.__name__ = "Integer32"
_RaisecomOspfIfType_Object = MibTableColumn
raisecomOspfIfType = _RaisecomOspfIfType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 4),
    _RaisecomOspfIfType_Type()
)
raisecomOspfIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfIfType.setStatus("current")


class _RaisecomOspfIfAdminStat_Type(Status):
    """Custom type raisecomOspfIfAdminStat based on Status"""
    defaultValue = 1


_RaisecomOspfIfAdminStat_Type.__name__ = "Status"
_RaisecomOspfIfAdminStat_Object = MibTableColumn
raisecomOspfIfAdminStat = _RaisecomOspfIfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 5),
    _RaisecomOspfIfAdminStat_Type()
)
raisecomOspfIfAdminStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfIfAdminStat.setStatus("current")


class _RaisecomOspfIfRtrPriority_Type(DesignatedRouterPriority):
    """Custom type raisecomOspfIfRtrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_RaisecomOspfIfRtrPriority_Type.__name__ = "DesignatedRouterPriority"
_RaisecomOspfIfRtrPriority_Object = MibTableColumn
raisecomOspfIfRtrPriority = _RaisecomOspfIfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 6),
    _RaisecomOspfIfRtrPriority_Type()
)
raisecomOspfIfRtrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfIfRtrPriority.setStatus("current")


class _RaisecomOspfIfTransitDelay_Type(UpToMaxAge):
    """Custom type raisecomOspfIfTransitDelay based on UpToMaxAge"""
    defaultValue = 1


_RaisecomOspfIfTransitDelay_Type.__name__ = "UpToMaxAge"
_RaisecomOspfIfTransitDelay_Object = MibTableColumn
raisecomOspfIfTransitDelay = _RaisecomOspfIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 7),
    _RaisecomOspfIfTransitDelay_Type()
)
raisecomOspfIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfIfTransitDelay.setStatus("current")
if mibBuilder.loadTexts:
    raisecomOspfIfTransitDelay.setUnits("seconds")


class _RaisecomOspfIfRetransInterval_Type(UpToMaxAge):
    """Custom type raisecomOspfIfRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_RaisecomOspfIfRetransInterval_Type.__name__ = "UpToMaxAge"
_RaisecomOspfIfRetransInterval_Object = MibTableColumn
raisecomOspfIfRetransInterval = _RaisecomOspfIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 8),
    _RaisecomOspfIfRetransInterval_Type()
)
raisecomOspfIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfIfRetransInterval.setStatus("current")
if mibBuilder.loadTexts:
    raisecomOspfIfRetransInterval.setUnits("seconds")


class _RaisecomOspfIfHelloInterval_Type(HelloRange):
    """Custom type raisecomOspfIfHelloInterval based on HelloRange"""
    defaultValue = 10


_RaisecomOspfIfHelloInterval_Type.__name__ = "HelloRange"
_RaisecomOspfIfHelloInterval_Object = MibTableColumn
raisecomOspfIfHelloInterval = _RaisecomOspfIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 9),
    _RaisecomOspfIfHelloInterval_Type()
)
raisecomOspfIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfIfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    raisecomOspfIfHelloInterval.setUnits("seconds")


class _RaisecomOspfIfRtrDeadInterval_Type(PositiveInteger):
    """Custom type raisecomOspfIfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 40


_RaisecomOspfIfRtrDeadInterval_Type.__name__ = "PositiveInteger"
_RaisecomOspfIfRtrDeadInterval_Object = MibTableColumn
raisecomOspfIfRtrDeadInterval = _RaisecomOspfIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 10),
    _RaisecomOspfIfRtrDeadInterval_Type()
)
raisecomOspfIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfIfRtrDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    raisecomOspfIfRtrDeadInterval.setUnits("seconds")


class _RaisecomOspfIfPollInterval_Type(PositiveInteger):
    """Custom type raisecomOspfIfPollInterval based on PositiveInteger"""
    defaultValue = 120


_RaisecomOspfIfPollInterval_Type.__name__ = "PositiveInteger"
_RaisecomOspfIfPollInterval_Object = MibTableColumn
raisecomOspfIfPollInterval = _RaisecomOspfIfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 11),
    _RaisecomOspfIfPollInterval_Type()
)
raisecomOspfIfPollInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfIfPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    raisecomOspfIfPollInterval.setUnits("seconds")


class _RaisecomOspfIfState_Type(Integer32):
    """Custom type raisecomOspfIfState based on Integer32"""
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


_RaisecomOspfIfState_Type.__name__ = "Integer32"
_RaisecomOspfIfState_Object = MibTableColumn
raisecomOspfIfState = _RaisecomOspfIfState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 12),
    _RaisecomOspfIfState_Type()
)
raisecomOspfIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfIfState.setStatus("current")


class _RaisecomOspfIfDesignatedRouter_Type(IpAddress):
    """Custom type raisecomOspfIfDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_RaisecomOspfIfDesignatedRouter_Type.__name__ = "IpAddress"
_RaisecomOspfIfDesignatedRouter_Object = MibTableColumn
raisecomOspfIfDesignatedRouter = _RaisecomOspfIfDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 13),
    _RaisecomOspfIfDesignatedRouter_Type()
)
raisecomOspfIfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfIfDesignatedRouter.setStatus("current")


class _RaisecomOspfIfBackupDesignatedRouter_Type(IpAddress):
    """Custom type raisecomOspfIfBackupDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_RaisecomOspfIfBackupDesignatedRouter_Type.__name__ = "IpAddress"
_RaisecomOspfIfBackupDesignatedRouter_Object = MibTableColumn
raisecomOspfIfBackupDesignatedRouter = _RaisecomOspfIfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 14),
    _RaisecomOspfIfBackupDesignatedRouter_Type()
)
raisecomOspfIfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfIfBackupDesignatedRouter.setStatus("current")
_RaisecomOspfIfEvents_Type = Counter32
_RaisecomOspfIfEvents_Object = MibTableColumn
raisecomOspfIfEvents = _RaisecomOspfIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 15),
    _RaisecomOspfIfEvents_Type()
)
raisecomOspfIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfIfEvents.setStatus("current")


class _RaisecomOspfIfAuthKeyId_Type(Integer32):
    """Custom type raisecomOspfIfAuthKeyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RaisecomOspfIfAuthKeyId_Type.__name__ = "Integer32"
_RaisecomOspfIfAuthKeyId_Object = MibTableColumn
raisecomOspfIfAuthKeyId = _RaisecomOspfIfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 16),
    _RaisecomOspfIfAuthKeyId_Type()
)
raisecomOspfIfAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfIfAuthKeyId.setStatus("current")


class _RaisecomOspfIfAuthSimpleKeyType_Type(Integer32):
    """Custom type raisecomOspfIfAuthSimpleKeyType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              7)
        )
    )
    namedValues = NamedValues(
        *(("plain", 0),
          ("cipher", 7))
    )


_RaisecomOspfIfAuthSimpleKeyType_Type.__name__ = "Integer32"
_RaisecomOspfIfAuthSimpleKeyType_Object = MibTableColumn
raisecomOspfIfAuthSimpleKeyType = _RaisecomOspfIfAuthSimpleKeyType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 17),
    _RaisecomOspfIfAuthSimpleKeyType_Type()
)
raisecomOspfIfAuthSimpleKeyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfIfAuthSimpleKeyType.setStatus("current")


class _RaisecomOspfIfAuthMd5KeyType_Type(Integer32):
    """Custom type raisecomOspfIfAuthMd5KeyType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              7)
        )
    )
    namedValues = NamedValues(
        *(("plain", 0),
          ("cipher", 7))
    )


_RaisecomOspfIfAuthMd5KeyType_Type.__name__ = "Integer32"
_RaisecomOspfIfAuthMd5KeyType_Object = MibTableColumn
raisecomOspfIfAuthMd5KeyType = _RaisecomOspfIfAuthMd5KeyType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 18),
    _RaisecomOspfIfAuthMd5KeyType_Type()
)
raisecomOspfIfAuthMd5KeyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfIfAuthMd5KeyType.setStatus("current")


class _RaisecomOspfIfAuthSimpleKey_Type(OctetString):
    """Custom type raisecomOspfIfAuthSimpleKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 68),
    )


_RaisecomOspfIfAuthSimpleKey_Type.__name__ = "OctetString"
_RaisecomOspfIfAuthSimpleKey_Object = MibTableColumn
raisecomOspfIfAuthSimpleKey = _RaisecomOspfIfAuthSimpleKey_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 19),
    _RaisecomOspfIfAuthSimpleKey_Type()
)
raisecomOspfIfAuthSimpleKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfIfAuthSimpleKey.setStatus("current")


class _RaisecomOspfIfAuthMd5Key_Type(OctetString):
    """Custom type raisecomOspfIfAuthMd5Key based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 68),
    )


_RaisecomOspfIfAuthMd5Key_Type.__name__ = "OctetString"
_RaisecomOspfIfAuthMd5Key_Object = MibTableColumn
raisecomOspfIfAuthMd5Key = _RaisecomOspfIfAuthMd5Key_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 20),
    _RaisecomOspfIfAuthMd5Key_Type()
)
raisecomOspfIfAuthMd5Key.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfIfAuthMd5Key.setStatus("current")


class _RaisecomOspfIfAuthKeyChain_Type(OctetString):
    """Custom type raisecomOspfIfAuthKeyChain based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RaisecomOspfIfAuthKeyChain_Type.__name__ = "OctetString"
_RaisecomOspfIfAuthKeyChain_Object = MibTableColumn
raisecomOspfIfAuthKeyChain = _RaisecomOspfIfAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 21),
    _RaisecomOspfIfAuthKeyChain_Type()
)
raisecomOspfIfAuthKeyChain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfIfAuthKeyChain.setStatus("current")


class _RaisecomOspfIfAuthType_Type(OspfAuthenticationType):
    """Custom type raisecomOspfIfAuthType based on OspfAuthenticationType"""
    defaultValue = 0


_RaisecomOspfIfAuthType_Type.__name__ = "OspfAuthenticationType"
_RaisecomOspfIfAuthType_Object = MibTableColumn
raisecomOspfIfAuthType = _RaisecomOspfIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 22),
    _RaisecomOspfIfAuthType_Type()
)
raisecomOspfIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfIfAuthType.setStatus("current")
_RaisecomOspfIfLsaCount_Type = Gauge32
_RaisecomOspfIfLsaCount_Object = MibTableColumn
raisecomOspfIfLsaCount = _RaisecomOspfIfLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 23),
    _RaisecomOspfIfLsaCount_Type()
)
raisecomOspfIfLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfIfLsaCount.setStatus("current")
_RaisecomOspfIfLsaCksumSum_Type = Unsigned32
_RaisecomOspfIfLsaCksumSum_Object = MibTableColumn
raisecomOspfIfLsaCksumSum = _RaisecomOspfIfLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 24),
    _RaisecomOspfIfLsaCksumSum_Type()
)
raisecomOspfIfLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfIfLsaCksumSum.setStatus("current")
_RaisecomOspfIfDesignatedRouterId_Type = RouterID
_RaisecomOspfIfDesignatedRouterId_Object = MibTableColumn
raisecomOspfIfDesignatedRouterId = _RaisecomOspfIfDesignatedRouterId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 25),
    _RaisecomOspfIfDesignatedRouterId_Type()
)
raisecomOspfIfDesignatedRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfIfDesignatedRouterId.setStatus("current")
_RaisecomOspfIfBackupDesignatedRouterId_Type = RouterID
_RaisecomOspfIfBackupDesignatedRouterId_Object = MibTableColumn
raisecomOspfIfBackupDesignatedRouterId = _RaisecomOspfIfBackupDesignatedRouterId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 26),
    _RaisecomOspfIfBackupDesignatedRouterId_Type()
)
raisecomOspfIfBackupDesignatedRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfIfBackupDesignatedRouterId.setStatus("current")


class _RaisecomOspfIfPassive_Type(EnableVar):
    """Custom type raisecomOspfIfPassive based on EnableVar"""
    defaultValue = 2


_RaisecomOspfIfPassive_Type.__name__ = "EnableVar"
_RaisecomOspfIfPassive_Object = MibTableColumn
raisecomOspfIfPassive = _RaisecomOspfIfPassive_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 27),
    _RaisecomOspfIfPassive_Type()
)
raisecomOspfIfPassive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfIfPassive.setStatus("current")


class _RaisecomOspfIfMtu_Type(EnableVar):
    """Custom type raisecomOspfIfMtu based on EnableVar"""
    defaultValue = 1


_RaisecomOspfIfMtu_Type.__name__ = "EnableVar"
_RaisecomOspfIfMtu_Object = MibTableColumn
raisecomOspfIfMtu = _RaisecomOspfIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 28),
    _RaisecomOspfIfMtu_Type()
)
raisecomOspfIfMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfIfMtu.setStatus("current")
_RaisecomOspfIfMetric_Type = Metric
_RaisecomOspfIfMetric_Object = MibTableColumn
raisecomOspfIfMetric = _RaisecomOspfIfMetric_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 6, 1, 29),
    _RaisecomOspfIfMetric_Type()
)
raisecomOspfIfMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfIfMetric.setStatus("current")
_RaisecomOspfVirtIfTable_Object = MibTable
raisecomOspfVirtIfTable = _RaisecomOspfVirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 7)
)
if mibBuilder.loadTexts:
    raisecomOspfVirtIfTable.setStatus("current")
_RaisecomOspfVirtIfEntry_Object = MibTableRow
raisecomOspfVirtIfEntry = _RaisecomOspfVirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 7, 1)
)
raisecomOspfVirtIfEntry.setIndexNames(
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfVirtIfAreaId"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfVirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    raisecomOspfVirtIfEntry.setStatus("current")
_RaisecomOspfVirtIfAreaId_Type = AreaID
_RaisecomOspfVirtIfAreaId_Object = MibTableColumn
raisecomOspfVirtIfAreaId = _RaisecomOspfVirtIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 7, 1, 1),
    _RaisecomOspfVirtIfAreaId_Type()
)
raisecomOspfVirtIfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfVirtIfAreaId.setStatus("current")
_RaisecomOspfVirtIfNeighbor_Type = RouterID
_RaisecomOspfVirtIfNeighbor_Object = MibTableColumn
raisecomOspfVirtIfNeighbor = _RaisecomOspfVirtIfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 7, 1, 2),
    _RaisecomOspfVirtIfNeighbor_Type()
)
raisecomOspfVirtIfNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfVirtIfNeighbor.setStatus("current")


class _RaisecomOspfVirtIfTransitDelay_Type(UpToMaxAge):
    """Custom type raisecomOspfVirtIfTransitDelay based on UpToMaxAge"""
    defaultValue = 1


_RaisecomOspfVirtIfTransitDelay_Type.__name__ = "UpToMaxAge"
_RaisecomOspfVirtIfTransitDelay_Object = MibTableColumn
raisecomOspfVirtIfTransitDelay = _RaisecomOspfVirtIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 7, 1, 3),
    _RaisecomOspfVirtIfTransitDelay_Type()
)
raisecomOspfVirtIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfVirtIfTransitDelay.setStatus("current")
if mibBuilder.loadTexts:
    raisecomOspfVirtIfTransitDelay.setUnits("seconds")


class _RaisecomOspfVirtIfRetransInterval_Type(UpToMaxAge):
    """Custom type raisecomOspfVirtIfRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_RaisecomOspfVirtIfRetransInterval_Type.__name__ = "UpToMaxAge"
_RaisecomOspfVirtIfRetransInterval_Object = MibTableColumn
raisecomOspfVirtIfRetransInterval = _RaisecomOspfVirtIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 7, 1, 4),
    _RaisecomOspfVirtIfRetransInterval_Type()
)
raisecomOspfVirtIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfVirtIfRetransInterval.setStatus("current")
if mibBuilder.loadTexts:
    raisecomOspfVirtIfRetransInterval.setUnits("seconds")


class _RaisecomOspfVirtIfHelloInterval_Type(HelloRange):
    """Custom type raisecomOspfVirtIfHelloInterval based on HelloRange"""
    defaultValue = 10


_RaisecomOspfVirtIfHelloInterval_Type.__name__ = "HelloRange"
_RaisecomOspfVirtIfHelloInterval_Object = MibTableColumn
raisecomOspfVirtIfHelloInterval = _RaisecomOspfVirtIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 7, 1, 5),
    _RaisecomOspfVirtIfHelloInterval_Type()
)
raisecomOspfVirtIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfVirtIfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    raisecomOspfVirtIfHelloInterval.setUnits("seconds")


class _RaisecomOspfVirtIfRtrDeadInterval_Type(PositiveInteger):
    """Custom type raisecomOspfVirtIfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 60


_RaisecomOspfVirtIfRtrDeadInterval_Type.__name__ = "PositiveInteger"
_RaisecomOspfVirtIfRtrDeadInterval_Object = MibTableColumn
raisecomOspfVirtIfRtrDeadInterval = _RaisecomOspfVirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 7, 1, 6),
    _RaisecomOspfVirtIfRtrDeadInterval_Type()
)
raisecomOspfVirtIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfVirtIfRtrDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    raisecomOspfVirtIfRtrDeadInterval.setUnits("seconds")


class _RaisecomOspfVirtIfState_Type(Integer32):
    """Custom type raisecomOspfVirtIfState based on Integer32"""
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


_RaisecomOspfVirtIfState_Type.__name__ = "Integer32"
_RaisecomOspfVirtIfState_Object = MibTableColumn
raisecomOspfVirtIfState = _RaisecomOspfVirtIfState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 7, 1, 7),
    _RaisecomOspfVirtIfState_Type()
)
raisecomOspfVirtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfVirtIfState.setStatus("current")
_RaisecomOspfVirtIfEvents_Type = Counter32
_RaisecomOspfVirtIfEvents_Object = MibTableColumn
raisecomOspfVirtIfEvents = _RaisecomOspfVirtIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 7, 1, 8),
    _RaisecomOspfVirtIfEvents_Type()
)
raisecomOspfVirtIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfVirtIfEvents.setStatus("current")


class _RaisecomOspfVirtIfAuthKeyId_Type(Integer32):
    """Custom type raisecomOspfVirtIfAuthKeyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RaisecomOspfVirtIfAuthKeyId_Type.__name__ = "Integer32"
_RaisecomOspfVirtIfAuthKeyId_Object = MibTableColumn
raisecomOspfVirtIfAuthKeyId = _RaisecomOspfVirtIfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 7, 1, 9),
    _RaisecomOspfVirtIfAuthKeyId_Type()
)
raisecomOspfVirtIfAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfVirtIfAuthKeyId.setStatus("current")


class _RaisecomOspfVirtIfAuthSimpleKeyType_Type(Integer32):
    """Custom type raisecomOspfVirtIfAuthSimpleKeyType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              7)
        )
    )
    namedValues = NamedValues(
        *(("plain", 0),
          ("cipher", 7))
    )


_RaisecomOspfVirtIfAuthSimpleKeyType_Type.__name__ = "Integer32"
_RaisecomOspfVirtIfAuthSimpleKeyType_Object = MibTableColumn
raisecomOspfVirtIfAuthSimpleKeyType = _RaisecomOspfVirtIfAuthSimpleKeyType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 7, 1, 10),
    _RaisecomOspfVirtIfAuthSimpleKeyType_Type()
)
raisecomOspfVirtIfAuthSimpleKeyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfVirtIfAuthSimpleKeyType.setStatus("current")


class _RaisecomOspfVirtIfAuthMd5KeyType_Type(Integer32):
    """Custom type raisecomOspfVirtIfAuthMd5KeyType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              7)
        )
    )
    namedValues = NamedValues(
        *(("plain", 0),
          ("cipher", 7))
    )


_RaisecomOspfVirtIfAuthMd5KeyType_Type.__name__ = "Integer32"
_RaisecomOspfVirtIfAuthMd5KeyType_Object = MibTableColumn
raisecomOspfVirtIfAuthMd5KeyType = _RaisecomOspfVirtIfAuthMd5KeyType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 7, 1, 11),
    _RaisecomOspfVirtIfAuthMd5KeyType_Type()
)
raisecomOspfVirtIfAuthMd5KeyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfVirtIfAuthMd5KeyType.setStatus("current")


class _RaisecomOspfVirtIfAuthSimpleKey_Type(OctetString):
    """Custom type raisecomOspfVirtIfAuthSimpleKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 68),
    )


_RaisecomOspfVirtIfAuthSimpleKey_Type.__name__ = "OctetString"
_RaisecomOspfVirtIfAuthSimpleKey_Object = MibTableColumn
raisecomOspfVirtIfAuthSimpleKey = _RaisecomOspfVirtIfAuthSimpleKey_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 7, 1, 12),
    _RaisecomOspfVirtIfAuthSimpleKey_Type()
)
raisecomOspfVirtIfAuthSimpleKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfVirtIfAuthSimpleKey.setStatus("current")


class _RaisecomOspfVirtIfAuthMd5Key_Type(OctetString):
    """Custom type raisecomOspfVirtIfAuthMd5Key based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 68),
    )


_RaisecomOspfVirtIfAuthMd5Key_Type.__name__ = "OctetString"
_RaisecomOspfVirtIfAuthMd5Key_Object = MibTableColumn
raisecomOspfVirtIfAuthMd5Key = _RaisecomOspfVirtIfAuthMd5Key_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 7, 1, 13),
    _RaisecomOspfVirtIfAuthMd5Key_Type()
)
raisecomOspfVirtIfAuthMd5Key.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfVirtIfAuthMd5Key.setStatus("current")


class _RaisecomOspfVirtIfAuthKeyChain_Type(OctetString):
    """Custom type raisecomOspfVirtIfAuthKeyChain based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RaisecomOspfVirtIfAuthKeyChain_Type.__name__ = "OctetString"
_RaisecomOspfVirtIfAuthKeyChain_Object = MibTableColumn
raisecomOspfVirtIfAuthKeyChain = _RaisecomOspfVirtIfAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 7, 1, 14),
    _RaisecomOspfVirtIfAuthKeyChain_Type()
)
raisecomOspfVirtIfAuthKeyChain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfVirtIfAuthKeyChain.setStatus("current")


class _RaisecomOspfVirtIfAuthType_Type(OspfAuthenticationType):
    """Custom type raisecomOspfVirtIfAuthType based on OspfAuthenticationType"""
    defaultValue = 0


_RaisecomOspfVirtIfAuthType_Type.__name__ = "OspfAuthenticationType"
_RaisecomOspfVirtIfAuthType_Object = MibTableColumn
raisecomOspfVirtIfAuthType = _RaisecomOspfVirtIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 7, 1, 15),
    _RaisecomOspfVirtIfAuthType_Type()
)
raisecomOspfVirtIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfVirtIfAuthType.setStatus("current")
_RaisecomOspfVirtIfLsaCount_Type = Gauge32
_RaisecomOspfVirtIfLsaCount_Object = MibTableColumn
raisecomOspfVirtIfLsaCount = _RaisecomOspfVirtIfLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 7, 1, 16),
    _RaisecomOspfVirtIfLsaCount_Type()
)
raisecomOspfVirtIfLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfVirtIfLsaCount.setStatus("current")
_RaisecomOspfVirtIfLsaCksumSum_Type = Unsigned32
_RaisecomOspfVirtIfLsaCksumSum_Object = MibTableColumn
raisecomOspfVirtIfLsaCksumSum = _RaisecomOspfVirtIfLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 7, 1, 17),
    _RaisecomOspfVirtIfLsaCksumSum_Type()
)
raisecomOspfVirtIfLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfVirtIfLsaCksumSum.setStatus("current")


class _RaisecomOspfVirtIfCost_Type(Integer32):
    """Custom type raisecomOspfVirtIfCost based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RaisecomOspfVirtIfCost_Type.__name__ = "Integer32"
_RaisecomOspfVirtIfCost_Object = MibTableColumn
raisecomOspfVirtIfCost = _RaisecomOspfVirtIfCost_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 7, 1, 18),
    _RaisecomOspfVirtIfCost_Type()
)
raisecomOspfVirtIfCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfVirtIfCost.setStatus("current")
_RaisecomOspfVirtIfStatus_Type = RowStatus
_RaisecomOspfVirtIfStatus_Object = MibTableColumn
raisecomOspfVirtIfStatus = _RaisecomOspfVirtIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 7, 1, 19),
    _RaisecomOspfVirtIfStatus_Type()
)
raisecomOspfVirtIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfVirtIfStatus.setStatus("current")
_RaisecomOspfNbrTable_Object = MibTable
raisecomOspfNbrTable = _RaisecomOspfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 8)
)
if mibBuilder.loadTexts:
    raisecomOspfNbrTable.setStatus("current")
_RaisecomOspfNbrEntry_Object = MibTableRow
raisecomOspfNbrEntry = _RaisecomOspfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 8, 1)
)
raisecomOspfNbrEntry.setIndexNames(
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfNbrIpAddr"),
)
if mibBuilder.loadTexts:
    raisecomOspfNbrEntry.setStatus("current")
_RaisecomOspfNbrIpAddr_Type = IpAddress
_RaisecomOspfNbrIpAddr_Object = MibTableColumn
raisecomOspfNbrIpAddr = _RaisecomOspfNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 8, 1, 1),
    _RaisecomOspfNbrIpAddr_Type()
)
raisecomOspfNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfNbrIpAddr.setStatus("current")
_RaisecomOspfNbrAddressLessIndex_Type = InterfaceIndexOrZero
_RaisecomOspfNbrAddressLessIndex_Object = MibTableColumn
raisecomOspfNbrAddressLessIndex = _RaisecomOspfNbrAddressLessIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 8, 1, 2),
    _RaisecomOspfNbrAddressLessIndex_Type()
)
raisecomOspfNbrAddressLessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfNbrAddressLessIndex.setStatus("current")


class _RaisecomOspfNbrRtrId_Type(RouterID):
    """Custom type raisecomOspfNbrRtrId based on RouterID"""
    defaultHexValue = "00000000"


_RaisecomOspfNbrRtrId_Type.__name__ = "RouterID"
_RaisecomOspfNbrRtrId_Object = MibTableColumn
raisecomOspfNbrRtrId = _RaisecomOspfNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 8, 1, 3),
    _RaisecomOspfNbrRtrId_Type()
)
raisecomOspfNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfNbrRtrId.setStatus("current")


class _RaisecomOspfNbrOptions_Type(Integer32):
    """Custom type raisecomOspfNbrOptions based on Integer32"""
    defaultValue = 0


_RaisecomOspfNbrOptions_Type.__name__ = "Integer32"
_RaisecomOspfNbrOptions_Object = MibTableColumn
raisecomOspfNbrOptions = _RaisecomOspfNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 8, 1, 4),
    _RaisecomOspfNbrOptions_Type()
)
raisecomOspfNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfNbrOptions.setStatus("current")


class _RaisecomOspfNbrPriority_Type(DesignatedRouterPriority):
    """Custom type raisecomOspfNbrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_RaisecomOspfNbrPriority_Type.__name__ = "DesignatedRouterPriority"
_RaisecomOspfNbrPriority_Object = MibTableColumn
raisecomOspfNbrPriority = _RaisecomOspfNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 8, 1, 5),
    _RaisecomOspfNbrPriority_Type()
)
raisecomOspfNbrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfNbrPriority.setStatus("current")


class _RaisecomOspfNbrState_Type(Integer32):
    """Custom type raisecomOspfNbrState based on Integer32"""
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


_RaisecomOspfNbrState_Type.__name__ = "Integer32"
_RaisecomOspfNbrState_Object = MibTableColumn
raisecomOspfNbrState = _RaisecomOspfNbrState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 8, 1, 6),
    _RaisecomOspfNbrState_Type()
)
raisecomOspfNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfNbrState.setStatus("current")
_RaisecomOspfNbrEvents_Type = Counter32
_RaisecomOspfNbrEvents_Object = MibTableColumn
raisecomOspfNbrEvents = _RaisecomOspfNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 8, 1, 7),
    _RaisecomOspfNbrEvents_Type()
)
raisecomOspfNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfNbrEvents.setStatus("current")
_RaisecomOspfNbrLsRetransQLen_Type = Gauge32
_RaisecomOspfNbrLsRetransQLen_Object = MibTableColumn
raisecomOspfNbrLsRetransQLen = _RaisecomOspfNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 8, 1, 8),
    _RaisecomOspfNbrLsRetransQLen_Type()
)
raisecomOspfNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfNbrLsRetransQLen.setStatus("current")


class _RaisecomOspfNbrMode_Type(Integer32):
    """Custom type raisecomOspfNbrMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("slave", 1),
          ("master", 2))
    )


_RaisecomOspfNbrMode_Type.__name__ = "Integer32"
_RaisecomOspfNbrMode_Object = MibTableColumn
raisecomOspfNbrMode = _RaisecomOspfNbrMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 8, 1, 9),
    _RaisecomOspfNbrMode_Type()
)
raisecomOspfNbrMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfNbrMode.setStatus("current")
_RaisecomOspfNbmaCfgNbrTable_Object = MibTable
raisecomOspfNbmaCfgNbrTable = _RaisecomOspfNbmaCfgNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 9)
)
if mibBuilder.loadTexts:
    raisecomOspfNbmaCfgNbrTable.setStatus("current")
_RaisecomOspfNbmaCfgNbrEntry_Object = MibTableRow
raisecomOspfNbmaCfgNbrEntry = _RaisecomOspfNbmaCfgNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 9, 1)
)
raisecomOspfNbmaCfgNbrEntry.setIndexNames(
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfNbmaCfgNbrIpAddr"),
)
if mibBuilder.loadTexts:
    raisecomOspfNbmaCfgNbrEntry.setStatus("current")
_RaisecomOspfNbmaCfgNbrIpAddr_Type = IpAddress
_RaisecomOspfNbmaCfgNbrIpAddr_Object = MibTableColumn
raisecomOspfNbmaCfgNbrIpAddr = _RaisecomOspfNbmaCfgNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 9, 1, 1),
    _RaisecomOspfNbmaCfgNbrIpAddr_Type()
)
raisecomOspfNbmaCfgNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfNbmaCfgNbrIpAddr.setStatus("current")


class _RaisecomOspfNbmaCfgNbrPriority_Type(DesignatedRouterPriority):
    """Custom type raisecomOspfNbmaCfgNbrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_RaisecomOspfNbmaCfgNbrPriority_Type.__name__ = "DesignatedRouterPriority"
_RaisecomOspfNbmaCfgNbrPriority_Object = MibTableColumn
raisecomOspfNbmaCfgNbrPriority = _RaisecomOspfNbmaCfgNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 9, 1, 2),
    _RaisecomOspfNbmaCfgNbrPriority_Type()
)
raisecomOspfNbmaCfgNbrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfNbmaCfgNbrPriority.setStatus("current")
_RaisecomOspfNbmaCfgNbrStatus_Type = RowStatus
_RaisecomOspfNbmaCfgNbrStatus_Object = MibTableColumn
raisecomOspfNbmaCfgNbrStatus = _RaisecomOspfNbmaCfgNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 9, 1, 3),
    _RaisecomOspfNbmaCfgNbrStatus_Type()
)
raisecomOspfNbmaCfgNbrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfNbmaCfgNbrStatus.setStatus("current")
_RaisecomOspfVirtNbrTable_Object = MibTable
raisecomOspfVirtNbrTable = _RaisecomOspfVirtNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 10)
)
if mibBuilder.loadTexts:
    raisecomOspfVirtNbrTable.setStatus("current")
_RaisecomOspfVirtNbrEntry_Object = MibTableRow
raisecomOspfVirtNbrEntry = _RaisecomOspfVirtNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 10, 1)
)
raisecomOspfVirtNbrEntry.setIndexNames(
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfVirtNbrArea"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfVirtNbrRtrId"),
)
if mibBuilder.loadTexts:
    raisecomOspfVirtNbrEntry.setStatus("current")
_RaisecomOspfVirtNbrArea_Type = AreaID
_RaisecomOspfVirtNbrArea_Object = MibTableColumn
raisecomOspfVirtNbrArea = _RaisecomOspfVirtNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 10, 1, 1),
    _RaisecomOspfVirtNbrArea_Type()
)
raisecomOspfVirtNbrArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfVirtNbrArea.setStatus("current")
_RaisecomOspfVirtNbrRtrId_Type = RouterID
_RaisecomOspfVirtNbrRtrId_Object = MibTableColumn
raisecomOspfVirtNbrRtrId = _RaisecomOspfVirtNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 10, 1, 2),
    _RaisecomOspfVirtNbrRtrId_Type()
)
raisecomOspfVirtNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfVirtNbrRtrId.setStatus("current")
_RaisecomOspfVirtNbrIpAddr_Type = IpAddress
_RaisecomOspfVirtNbrIpAddr_Object = MibTableColumn
raisecomOspfVirtNbrIpAddr = _RaisecomOspfVirtNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 10, 1, 3),
    _RaisecomOspfVirtNbrIpAddr_Type()
)
raisecomOspfVirtNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfVirtNbrIpAddr.setStatus("current")
_RaisecomOspfVirtNbrOptions_Type = Integer32
_RaisecomOspfVirtNbrOptions_Object = MibTableColumn
raisecomOspfVirtNbrOptions = _RaisecomOspfVirtNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 10, 1, 4),
    _RaisecomOspfVirtNbrOptions_Type()
)
raisecomOspfVirtNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfVirtNbrOptions.setStatus("current")


class _RaisecomOspfVirtNbrState_Type(Integer32):
    """Custom type raisecomOspfVirtNbrState based on Integer32"""
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


_RaisecomOspfVirtNbrState_Type.__name__ = "Integer32"
_RaisecomOspfVirtNbrState_Object = MibTableColumn
raisecomOspfVirtNbrState = _RaisecomOspfVirtNbrState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 10, 1, 5),
    _RaisecomOspfVirtNbrState_Type()
)
raisecomOspfVirtNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfVirtNbrState.setStatus("current")
_RaisecomOspfVirtNbrEvents_Type = Counter32
_RaisecomOspfVirtNbrEvents_Object = MibTableColumn
raisecomOspfVirtNbrEvents = _RaisecomOspfVirtNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 10, 1, 6),
    _RaisecomOspfVirtNbrEvents_Type()
)
raisecomOspfVirtNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfVirtNbrEvents.setStatus("current")
_RaisecomOspfVirtNbrLsRetransQLen_Type = Gauge32
_RaisecomOspfVirtNbrLsRetransQLen_Object = MibTableColumn
raisecomOspfVirtNbrLsRetransQLen = _RaisecomOspfVirtNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 10, 1, 7),
    _RaisecomOspfVirtNbrLsRetransQLen_Type()
)
raisecomOspfVirtNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfVirtNbrLsRetransQLen.setStatus("current")
_RaisecomOspfVirtNbrLessIf_Type = Integer32
_RaisecomOspfVirtNbrLessIf_Object = MibTableColumn
raisecomOspfVirtNbrLessIf = _RaisecomOspfVirtNbrLessIf_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 10, 1, 8),
    _RaisecomOspfVirtNbrLessIf_Type()
)
raisecomOspfVirtNbrLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfVirtNbrLessIf.setStatus("current")


class _RaisecomOspfVirtNbrMode_Type(Integer32):
    """Custom type raisecomOspfVirtNbrMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("slave", 1),
          ("master", 2))
    )


_RaisecomOspfVirtNbrMode_Type.__name__ = "Integer32"
_RaisecomOspfVirtNbrMode_Object = MibTableColumn
raisecomOspfVirtNbrMode = _RaisecomOspfVirtNbrMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 10, 1, 9),
    _RaisecomOspfVirtNbrMode_Type()
)
raisecomOspfVirtNbrMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfVirtNbrMode.setStatus("current")
_RaisecomOspfAreaAggregateTable_Object = MibTable
raisecomOspfAreaAggregateTable = _RaisecomOspfAreaAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 11)
)
if mibBuilder.loadTexts:
    raisecomOspfAreaAggregateTable.setStatus("current")
_RaisecomOspfAreaAggregateEntry_Object = MibTableRow
raisecomOspfAreaAggregateEntry = _RaisecomOspfAreaAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 11, 1)
)
raisecomOspfAreaAggregateEntry.setIndexNames(
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfAreaAggregateAreaID"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfAreaAggregateLsdbType"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfAreaAggregateNet"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfAreaAggregateMask"),
)
if mibBuilder.loadTexts:
    raisecomOspfAreaAggregateEntry.setStatus("current")
_RaisecomOspfAreaAggregateAreaID_Type = AreaID
_RaisecomOspfAreaAggregateAreaID_Object = MibTableColumn
raisecomOspfAreaAggregateAreaID = _RaisecomOspfAreaAggregateAreaID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 11, 1, 1),
    _RaisecomOspfAreaAggregateAreaID_Type()
)
raisecomOspfAreaAggregateAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfAreaAggregateAreaID.setStatus("current")


class _RaisecomOspfAreaAggregateLsdbType_Type(Integer32):
    """Custom type raisecomOspfAreaAggregateLsdbType based on Integer32"""
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


_RaisecomOspfAreaAggregateLsdbType_Type.__name__ = "Integer32"
_RaisecomOspfAreaAggregateLsdbType_Object = MibTableColumn
raisecomOspfAreaAggregateLsdbType = _RaisecomOspfAreaAggregateLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 11, 1, 2),
    _RaisecomOspfAreaAggregateLsdbType_Type()
)
raisecomOspfAreaAggregateLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfAreaAggregateLsdbType.setStatus("current")
_RaisecomOspfAreaAggregateNet_Type = IpAddress
_RaisecomOspfAreaAggregateNet_Object = MibTableColumn
raisecomOspfAreaAggregateNet = _RaisecomOspfAreaAggregateNet_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 11, 1, 3),
    _RaisecomOspfAreaAggregateNet_Type()
)
raisecomOspfAreaAggregateNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfAreaAggregateNet.setStatus("current")
_RaisecomOspfAreaAggregateMask_Type = IpAddress
_RaisecomOspfAreaAggregateMask_Object = MibTableColumn
raisecomOspfAreaAggregateMask = _RaisecomOspfAreaAggregateMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 11, 1, 4),
    _RaisecomOspfAreaAggregateMask_Type()
)
raisecomOspfAreaAggregateMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfAreaAggregateMask.setStatus("current")


class _RaisecomOspfAreaAggregateEffect_Type(Integer32):
    """Custom type raisecomOspfAreaAggregateEffect based on Integer32"""
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


_RaisecomOspfAreaAggregateEffect_Type.__name__ = "Integer32"
_RaisecomOspfAreaAggregateEffect_Object = MibTableColumn
raisecomOspfAreaAggregateEffect = _RaisecomOspfAreaAggregateEffect_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 11, 1, 5),
    _RaisecomOspfAreaAggregateEffect_Type()
)
raisecomOspfAreaAggregateEffect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfAreaAggregateEffect.setStatus("current")
_RaisecomOspfAreaAggregateStatus_Type = RowStatus
_RaisecomOspfAreaAggregateStatus_Object = MibTableColumn
raisecomOspfAreaAggregateStatus = _RaisecomOspfAreaAggregateStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 11, 1, 6),
    _RaisecomOspfAreaAggregateStatus_Type()
)
raisecomOspfAreaAggregateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfAreaAggregateStatus.setStatus("current")
_RaisecomOspfExternalAggregateTable_Object = MibTable
raisecomOspfExternalAggregateTable = _RaisecomOspfExternalAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 12)
)
if mibBuilder.loadTexts:
    raisecomOspfExternalAggregateTable.setStatus("current")
_RaisecomOspfExternalAggregateEntry_Object = MibTableRow
raisecomOspfExternalAggregateEntry = _RaisecomOspfExternalAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 12, 1)
)
raisecomOspfExternalAggregateEntry.setIndexNames(
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfExternalAggregateNet"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfExternalAggregateMask"),
)
if mibBuilder.loadTexts:
    raisecomOspfExternalAggregateEntry.setStatus("current")
_RaisecomOspfExternalAggregateNet_Type = IpAddress
_RaisecomOspfExternalAggregateNet_Object = MibTableColumn
raisecomOspfExternalAggregateNet = _RaisecomOspfExternalAggregateNet_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 12, 1, 1),
    _RaisecomOspfExternalAggregateNet_Type()
)
raisecomOspfExternalAggregateNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfExternalAggregateNet.setStatus("current")
_RaisecomOspfExternalAggregateMask_Type = IpAddress
_RaisecomOspfExternalAggregateMask_Object = MibTableColumn
raisecomOspfExternalAggregateMask = _RaisecomOspfExternalAggregateMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 12, 1, 2),
    _RaisecomOspfExternalAggregateMask_Type()
)
raisecomOspfExternalAggregateMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfExternalAggregateMask.setStatus("current")


class _RaisecomOspfExternalAggregateEffect_Type(Integer32):
    """Custom type raisecomOspfExternalAggregateEffect based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNotAdvertise", 1),
          ("advertise", 2))
    )


_RaisecomOspfExternalAggregateEffect_Type.__name__ = "Integer32"
_RaisecomOspfExternalAggregateEffect_Object = MibTableColumn
raisecomOspfExternalAggregateEffect = _RaisecomOspfExternalAggregateEffect_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 12, 1, 3),
    _RaisecomOspfExternalAggregateEffect_Type()
)
raisecomOspfExternalAggregateEffect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfExternalAggregateEffect.setStatus("current")


class _RaisecomOspfExternalAggregateCost_Type(BigMetric):
    """Custom type raisecomOspfExternalAggregateCost based on BigMetric"""
    defaultValue = 1


_RaisecomOspfExternalAggregateCost_Type.__name__ = "BigMetric"
_RaisecomOspfExternalAggregateCost_Object = MibTableColumn
raisecomOspfExternalAggregateCost = _RaisecomOspfExternalAggregateCost_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 12, 1, 4),
    _RaisecomOspfExternalAggregateCost_Type()
)
raisecomOspfExternalAggregateCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfExternalAggregateCost.setStatus("current")
_RaisecomOspfExternalAggregateStatus_Type = RowStatus
_RaisecomOspfExternalAggregateStatus_Object = MibTableColumn
raisecomOspfExternalAggregateStatus = _RaisecomOspfExternalAggregateStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 12, 1, 5),
    _RaisecomOspfExternalAggregateStatus_Type()
)
raisecomOspfExternalAggregateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfExternalAggregateStatus.setStatus("current")
_RaisecomOspfLsdbTable_Object = MibTable
raisecomOspfLsdbTable = _RaisecomOspfLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 13)
)
if mibBuilder.loadTexts:
    raisecomOspfLsdbTable.setStatus("current")
_RaisecomOspfLsdbEntry_Object = MibTableRow
raisecomOspfLsdbEntry = _RaisecomOspfLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 13, 1)
)
raisecomOspfLsdbEntry.setIndexNames(
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfLsdbAreaId"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfLsdbType"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfLsdbLsId"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfLsdbRouterId"),
)
if mibBuilder.loadTexts:
    raisecomOspfLsdbEntry.setStatus("current")
_RaisecomOspfLsdbAreaId_Type = AreaID
_RaisecomOspfLsdbAreaId_Object = MibTableColumn
raisecomOspfLsdbAreaId = _RaisecomOspfLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 13, 1, 1),
    _RaisecomOspfLsdbAreaId_Type()
)
raisecomOspfLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfLsdbAreaId.setStatus("current")


class _RaisecomOspfLsdbType_Type(Integer32):
    """Custom type raisecomOspfLsdbType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("routerLink", 1),
          ("networkLink", 2),
          ("summaryLink", 3),
          ("asSummaryLink", 4),
          ("asExternalLink", 5),
          ("multicastLink", 6),
          ("nssaExternalLink", 7),
          ("areaOpaqueLink", 10))
    )


_RaisecomOspfLsdbType_Type.__name__ = "Integer32"
_RaisecomOspfLsdbType_Object = MibTableColumn
raisecomOspfLsdbType = _RaisecomOspfLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 13, 1, 2),
    _RaisecomOspfLsdbType_Type()
)
raisecomOspfLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfLsdbType.setStatus("current")
_RaisecomOspfLsdbLsId_Type = IpAddress
_RaisecomOspfLsdbLsId_Object = MibTableColumn
raisecomOspfLsdbLsId = _RaisecomOspfLsdbLsId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 13, 1, 3),
    _RaisecomOspfLsdbLsId_Type()
)
raisecomOspfLsdbLsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfLsdbLsId.setStatus("current")
_RaisecomOspfLsdbRouterId_Type = RouterID
_RaisecomOspfLsdbRouterId_Object = MibTableColumn
raisecomOspfLsdbRouterId = _RaisecomOspfLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 13, 1, 4),
    _RaisecomOspfLsdbRouterId_Type()
)
raisecomOspfLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfLsdbRouterId.setStatus("current")
_RaisecomOspfLsdbSequence_Type = Integer32
_RaisecomOspfLsdbSequence_Object = MibTableColumn
raisecomOspfLsdbSequence = _RaisecomOspfLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 13, 1, 5),
    _RaisecomOspfLsdbSequence_Type()
)
raisecomOspfLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfLsdbSequence.setStatus("current")
_RaisecomOspfLsdbAge_Type = Integer32
_RaisecomOspfLsdbAge_Object = MibTableColumn
raisecomOspfLsdbAge = _RaisecomOspfLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 13, 1, 6),
    _RaisecomOspfLsdbAge_Type()
)
raisecomOspfLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    raisecomOspfLsdbAge.setUnits("seconds")
_RaisecomOspfLsdbChecksum_Type = Integer32
_RaisecomOspfLsdbChecksum_Object = MibTableColumn
raisecomOspfLsdbChecksum = _RaisecomOspfLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 13, 1, 7),
    _RaisecomOspfLsdbChecksum_Type()
)
raisecomOspfLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfLsdbChecksum.setStatus("current")


class _RaisecomOspfLsdbAdvertisement_Type(OctetString):
    """Custom type raisecomOspfLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_RaisecomOspfLsdbAdvertisement_Type.__name__ = "OctetString"
_RaisecomOspfLsdbAdvertisement_Object = MibTableColumn
raisecomOspfLsdbAdvertisement = _RaisecomOspfLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 13, 1, 8),
    _RaisecomOspfLsdbAdvertisement_Type()
)
raisecomOspfLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfLsdbAdvertisement.setStatus("current")
_RaisecomOspfAsLsdbTable_Object = MibTable
raisecomOspfAsLsdbTable = _RaisecomOspfAsLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 14)
)
if mibBuilder.loadTexts:
    raisecomOspfAsLsdbTable.setStatus("current")
_RaisecomOspfAsLsdbEntry_Object = MibTableRow
raisecomOspfAsLsdbEntry = _RaisecomOspfAsLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 14, 1)
)
raisecomOspfAsLsdbEntry.setIndexNames(
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfAsLsdbType"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfAsLsdbLsId"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfAsLsdbRouterId"),
)
if mibBuilder.loadTexts:
    raisecomOspfAsLsdbEntry.setStatus("current")


class _RaisecomOspfAsLsdbType_Type(Integer32):
    """Custom type raisecomOspfAsLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("asExternalLink", 5)
    )


_RaisecomOspfAsLsdbType_Type.__name__ = "Integer32"
_RaisecomOspfAsLsdbType_Object = MibTableColumn
raisecomOspfAsLsdbType = _RaisecomOspfAsLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 14, 1, 1),
    _RaisecomOspfAsLsdbType_Type()
)
raisecomOspfAsLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomOspfAsLsdbType.setStatus("current")
_RaisecomOspfAsLsdbLsId_Type = IpAddress
_RaisecomOspfAsLsdbLsId_Object = MibTableColumn
raisecomOspfAsLsdbLsId = _RaisecomOspfAsLsdbLsId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 14, 1, 2),
    _RaisecomOspfAsLsdbLsId_Type()
)
raisecomOspfAsLsdbLsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomOspfAsLsdbLsId.setStatus("current")
_RaisecomOspfAsLsdbRouterId_Type = RouterID
_RaisecomOspfAsLsdbRouterId_Object = MibTableColumn
raisecomOspfAsLsdbRouterId = _RaisecomOspfAsLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 14, 1, 3),
    _RaisecomOspfAsLsdbRouterId_Type()
)
raisecomOspfAsLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomOspfAsLsdbRouterId.setStatus("current")
_RaisecomOspfAsLsdbSequence_Type = Integer32
_RaisecomOspfAsLsdbSequence_Object = MibTableColumn
raisecomOspfAsLsdbSequence = _RaisecomOspfAsLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 14, 1, 4),
    _RaisecomOspfAsLsdbSequence_Type()
)
raisecomOspfAsLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfAsLsdbSequence.setStatus("current")
_RaisecomOspfAsLsdbAge_Type = Integer32
_RaisecomOspfAsLsdbAge_Object = MibTableColumn
raisecomOspfAsLsdbAge = _RaisecomOspfAsLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 14, 1, 5),
    _RaisecomOspfAsLsdbAge_Type()
)
raisecomOspfAsLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfAsLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    raisecomOspfAsLsdbAge.setUnits("seconds")
_RaisecomOspfAsLsdbChecksum_Type = Integer32
_RaisecomOspfAsLsdbChecksum_Object = MibTableColumn
raisecomOspfAsLsdbChecksum = _RaisecomOspfAsLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 14, 1, 6),
    _RaisecomOspfAsLsdbChecksum_Type()
)
raisecomOspfAsLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfAsLsdbChecksum.setStatus("current")


class _RaisecomOspfAsLsdbAdvertisement_Type(OctetString):
    """Custom type raisecomOspfAsLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_RaisecomOspfAsLsdbAdvertisement_Type.__name__ = "OctetString"
_RaisecomOspfAsLsdbAdvertisement_Object = MibTableColumn
raisecomOspfAsLsdbAdvertisement = _RaisecomOspfAsLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 14, 1, 7),
    _RaisecomOspfAsLsdbAdvertisement_Type()
)
raisecomOspfAsLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfAsLsdbAdvertisement.setStatus("current")
_RaisecomOspfAreaLsaCountTable_Object = MibTable
raisecomOspfAreaLsaCountTable = _RaisecomOspfAreaLsaCountTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 15)
)
if mibBuilder.loadTexts:
    raisecomOspfAreaLsaCountTable.setStatus("current")
_RaisecomOspfAreaLsaCountEntry_Object = MibTableRow
raisecomOspfAreaLsaCountEntry = _RaisecomOspfAreaLsaCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 15, 1)
)
raisecomOspfAreaLsaCountEntry.setIndexNames(
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfAreaLsaCountAreaId"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfAreaLsaCountLsaType"),
)
if mibBuilder.loadTexts:
    raisecomOspfAreaLsaCountEntry.setStatus("current")
_RaisecomOspfAreaLsaCountAreaId_Type = AreaID
_RaisecomOspfAreaLsaCountAreaId_Object = MibTableColumn
raisecomOspfAreaLsaCountAreaId = _RaisecomOspfAreaLsaCountAreaId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 15, 1, 1),
    _RaisecomOspfAreaLsaCountAreaId_Type()
)
raisecomOspfAreaLsaCountAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfAreaLsaCountAreaId.setStatus("current")


class _RaisecomOspfAreaLsaCountLsaType_Type(Integer32):
    """Custom type raisecomOspfAreaLsaCountLsaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              10)
        )
    )
    namedValues = NamedValues(
        *(("routerLink", 1),
          ("networkLink", 2),
          ("summaryLink", 3),
          ("asSummaryLink", 4),
          ("multicastLink", 6),
          ("nssaExternalLink", 7),
          ("areaOpaqueLink", 10))
    )


_RaisecomOspfAreaLsaCountLsaType_Type.__name__ = "Integer32"
_RaisecomOspfAreaLsaCountLsaType_Object = MibTableColumn
raisecomOspfAreaLsaCountLsaType = _RaisecomOspfAreaLsaCountLsaType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 15, 1, 2),
    _RaisecomOspfAreaLsaCountLsaType_Type()
)
raisecomOspfAreaLsaCountLsaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfAreaLsaCountLsaType.setStatus("current")
_RaisecomOspfAreaLsaCountNumber_Type = Gauge32
_RaisecomOspfAreaLsaCountNumber_Object = MibTableColumn
raisecomOspfAreaLsaCountNumber = _RaisecomOspfAreaLsaCountNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 15, 1, 3),
    _RaisecomOspfAreaLsaCountNumber_Type()
)
raisecomOspfAreaLsaCountNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfAreaLsaCountNumber.setStatus("current")
_RaisecomOspfRedistributeTable_Object = MibTable
raisecomOspfRedistributeTable = _RaisecomOspfRedistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 16)
)
if mibBuilder.loadTexts:
    raisecomOspfRedistributeTable.setStatus("current")
_RaisecomOspfRedistributeEntry_Object = MibTableRow
raisecomOspfRedistributeEntry = _RaisecomOspfRedistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 16, 1)
)
raisecomOspfRedistributeEntry.setIndexNames(
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfRedistributeProtocol"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfRedistributeProcessId"),
)
if mibBuilder.loadTexts:
    raisecomOspfRedistributeEntry.setStatus("current")


class _RaisecomOspfRedistributeProtocol_Type(Integer32):
    """Custom type raisecomOspfRedistributeProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              8,
              13)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("netmgmt", 3),
          ("rip", 8),
          ("ospf", 13))
    )


_RaisecomOspfRedistributeProtocol_Type.__name__ = "Integer32"
_RaisecomOspfRedistributeProtocol_Object = MibTableColumn
raisecomOspfRedistributeProtocol = _RaisecomOspfRedistributeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 16, 1, 1),
    _RaisecomOspfRedistributeProtocol_Type()
)
raisecomOspfRedistributeProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfRedistributeProtocol.setStatus("current")
_RaisecomOspfRedistributeProcessId_Type = ProcessID
_RaisecomOspfRedistributeProcessId_Object = MibTableColumn
raisecomOspfRedistributeProcessId = _RaisecomOspfRedistributeProcessId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 16, 1, 2),
    _RaisecomOspfRedistributeProcessId_Type()
)
raisecomOspfRedistributeProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfRedistributeProcessId.setStatus("current")


class _RaisecomOspfRedistributeCost_Type(BigMetric):
    """Custom type raisecomOspfRedistributeCost based on BigMetric"""
    defaultValue = 1


_RaisecomOspfRedistributeCost_Type.__name__ = "BigMetric"
_RaisecomOspfRedistributeCost_Object = MibTableColumn
raisecomOspfRedistributeCost = _RaisecomOspfRedistributeCost_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 16, 1, 3),
    _RaisecomOspfRedistributeCost_Type()
)
raisecomOspfRedistributeCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfRedistributeCost.setStatus("current")


class _RaisecomOspfRedistributeType_Type(Integer32):
    """Custom type raisecomOspfRedistributeType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1", 1),
          ("e2", 2))
    )


_RaisecomOspfRedistributeType_Type.__name__ = "Integer32"
_RaisecomOspfRedistributeType_Object = MibTableColumn
raisecomOspfRedistributeType = _RaisecomOspfRedistributeType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 16, 1, 4),
    _RaisecomOspfRedistributeType_Type()
)
raisecomOspfRedistributeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfRedistributeType.setStatus("current")
_RaisecomOspfRedistributeStatus_Type = RowStatus
_RaisecomOspfRedistributeStatus_Object = MibTableColumn
raisecomOspfRedistributeStatus = _RaisecomOspfRedistributeStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 16, 1, 5),
    _RaisecomOspfRedistributeStatus_Type()
)
raisecomOspfRedistributeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfRedistributeStatus.setStatus("current")


class _RaisecomOspfRedistributeRouteMapName_Type(OctetString):
    """Custom type raisecomOspfRedistributeRouteMapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_RaisecomOspfRedistributeRouteMapName_Type.__name__ = "OctetString"
_RaisecomOspfRedistributeRouteMapName_Object = MibTableColumn
raisecomOspfRedistributeRouteMapName = _RaisecomOspfRedistributeRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 16, 1, 6),
    _RaisecomOspfRedistributeRouteMapName_Type()
)
raisecomOspfRedistributeRouteMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfRedistributeRouteMapName.setStatus("current")


class _RaisecomOspfRedistributeTag_Type(Integer32):
    """Custom type raisecomOspfRedistributeTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RaisecomOspfRedistributeTag_Type.__name__ = "Integer32"
_RaisecomOspfRedistributeTag_Object = MibTableColumn
raisecomOspfRedistributeTag = _RaisecomOspfRedistributeTag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 16, 1, 7),
    _RaisecomOspfRedistributeTag_Type()
)
raisecomOspfRedistributeTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfRedistributeTag.setStatus("current")
_RaisecomOspfDefaultInfoTable_Object = MibTable
raisecomOspfDefaultInfoTable = _RaisecomOspfDefaultInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 17)
)
if mibBuilder.loadTexts:
    raisecomOspfDefaultInfoTable.setStatus("current")
_RaisecomOspfDefaultInfoEntry_Object = MibTableRow
raisecomOspfDefaultInfoEntry = _RaisecomOspfDefaultInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 17, 1)
)
raisecomOspfDefaultInfoEntry.setIndexNames(
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
)
if mibBuilder.loadTexts:
    raisecomOspfDefaultInfoEntry.setStatus("current")


class _RaisecomOspfDefaultInfoAlways_Type(TruthValue):
    """Custom type raisecomOspfDefaultInfoAlways based on TruthValue"""
    defaultValue = 2


_RaisecomOspfDefaultInfoAlways_Type.__name__ = "TruthValue"
_RaisecomOspfDefaultInfoAlways_Object = MibTableColumn
raisecomOspfDefaultInfoAlways = _RaisecomOspfDefaultInfoAlways_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 17, 1, 1),
    _RaisecomOspfDefaultInfoAlways_Type()
)
raisecomOspfDefaultInfoAlways.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfDefaultInfoAlways.setStatus("current")


class _RaisecomOspfDefaultInfoCost_Type(BigMetric):
    """Custom type raisecomOspfDefaultInfoCost based on BigMetric"""
    defaultValue = 1


_RaisecomOspfDefaultInfoCost_Type.__name__ = "BigMetric"
_RaisecomOspfDefaultInfoCost_Object = MibTableColumn
raisecomOspfDefaultInfoCost = _RaisecomOspfDefaultInfoCost_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 17, 1, 2),
    _RaisecomOspfDefaultInfoCost_Type()
)
raisecomOspfDefaultInfoCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfDefaultInfoCost.setStatus("current")


class _RaisecomOspfDefaultInfoType_Type(Integer32):
    """Custom type raisecomOspfDefaultInfoType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1", 1),
          ("e2", 2))
    )


_RaisecomOspfDefaultInfoType_Type.__name__ = "Integer32"
_RaisecomOspfDefaultInfoType_Object = MibTableColumn
raisecomOspfDefaultInfoType = _RaisecomOspfDefaultInfoType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 17, 1, 3),
    _RaisecomOspfDefaultInfoType_Type()
)
raisecomOspfDefaultInfoType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfDefaultInfoType.setStatus("current")
_RaisecomOspfDefaultInfoStatus_Type = RowStatus
_RaisecomOspfDefaultInfoStatus_Object = MibTableColumn
raisecomOspfDefaultInfoStatus = _RaisecomOspfDefaultInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 17, 1, 4),
    _RaisecomOspfDefaultInfoStatus_Type()
)
raisecomOspfDefaultInfoStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfDefaultInfoStatus.setStatus("current")
_RaisecomOspfPacketIoStatisTable_Object = MibTable
raisecomOspfPacketIoStatisTable = _RaisecomOspfPacketIoStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 18)
)
if mibBuilder.loadTexts:
    raisecomOspfPacketIoStatisTable.setStatus("current")
_RaisecomOspfPacketIoStatisEntry_Object = MibTableRow
raisecomOspfPacketIoStatisEntry = _RaisecomOspfPacketIoStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 18, 1)
)
raisecomOspfPacketIoStatisEntry.setIndexNames(
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfPacketIoStatisIoType"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfPacketIoStatisPktType"),
)
if mibBuilder.loadTexts:
    raisecomOspfPacketIoStatisEntry.setStatus("current")


class _RaisecomOspfPacketIoStatisIoType_Type(Integer32):
    """Custom type raisecomOspfPacketIoStatisIoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_RaisecomOspfPacketIoStatisIoType_Type.__name__ = "Integer32"
_RaisecomOspfPacketIoStatisIoType_Object = MibTableColumn
raisecomOspfPacketIoStatisIoType = _RaisecomOspfPacketIoStatisIoType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 18, 1, 1),
    _RaisecomOspfPacketIoStatisIoType_Type()
)
raisecomOspfPacketIoStatisIoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfPacketIoStatisIoType.setStatus("current")


class _RaisecomOspfPacketIoStatisPktType_Type(Integer32):
    """Custom type raisecomOspfPacketIoStatisPktType based on Integer32"""
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
        *(("hello", 1),
          ("dbDescript", 2),
          ("lsReq", 3),
          ("lsUpdate", 4),
          ("lsAck", 5))
    )


_RaisecomOspfPacketIoStatisPktType_Type.__name__ = "Integer32"
_RaisecomOspfPacketIoStatisPktType_Object = MibTableColumn
raisecomOspfPacketIoStatisPktType = _RaisecomOspfPacketIoStatisPktType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 18, 1, 2),
    _RaisecomOspfPacketIoStatisPktType_Type()
)
raisecomOspfPacketIoStatisPktType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfPacketIoStatisPktType.setStatus("current")
_RaisecomOspfPacketIoStatisNumber_Type = Integer32
_RaisecomOspfPacketIoStatisNumber_Object = MibTableColumn
raisecomOspfPacketIoStatisNumber = _RaisecomOspfPacketIoStatisNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 18, 1, 3),
    _RaisecomOspfPacketIoStatisNumber_Type()
)
raisecomOspfPacketIoStatisNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfPacketIoStatisNumber.setStatus("current")
_RaisecomOspfRouteTable_Object = MibTable
raisecomOspfRouteTable = _RaisecomOspfRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 19)
)
if mibBuilder.loadTexts:
    raisecomOspfRouteTable.setStatus("current")
_RaisecomOspfRouteEntry_Object = MibTableRow
raisecomOspfRouteEntry = _RaisecomOspfRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 19, 1)
)
raisecomOspfRouteEntry.setIndexNames(
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfRouteDest"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfRouteMask"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfRouteType"),
)
if mibBuilder.loadTexts:
    raisecomOspfRouteEntry.setStatus("current")
_RaisecomOspfRouteDest_Type = IpAddress
_RaisecomOspfRouteDest_Object = MibTableColumn
raisecomOspfRouteDest = _RaisecomOspfRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 19, 1, 1),
    _RaisecomOspfRouteDest_Type()
)
raisecomOspfRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfRouteDest.setStatus("current")
_RaisecomOspfRouteMask_Type = IpAddress
_RaisecomOspfRouteMask_Object = MibTableColumn
raisecomOspfRouteMask = _RaisecomOspfRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 19, 1, 2),
    _RaisecomOspfRouteMask_Type()
)
raisecomOspfRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfRouteMask.setStatus("current")


class _RaisecomOspfRouteType_Type(Integer32):
    """Custom type raisecomOspfRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("network", 1),
          ("ase", 2),
          ("nssa", 3))
    )


_RaisecomOspfRouteType_Type.__name__ = "Integer32"
_RaisecomOspfRouteType_Object = MibTableColumn
raisecomOspfRouteType = _RaisecomOspfRouteType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 19, 1, 3),
    _RaisecomOspfRouteType_Type()
)
raisecomOspfRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfRouteType.setStatus("current")


class _RaisecomOspfRouteLsType_Type(Integer32):
    """Custom type raisecomOspfRouteLsType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("stub", 0),
          ("routerLink", 1),
          ("networkLink", 2),
          ("summaryLink", 3),
          ("asSummaryLink", 4),
          ("asExternalLink", 5),
          ("multicastLink", 6),
          ("nssaExternalLink", 7),
          ("areaOpaqueLink", 10))
    )


_RaisecomOspfRouteLsType_Type.__name__ = "Integer32"
_RaisecomOspfRouteLsType_Object = MibTableColumn
raisecomOspfRouteLsType = _RaisecomOspfRouteLsType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 19, 1, 4),
    _RaisecomOspfRouteLsType_Type()
)
raisecomOspfRouteLsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfRouteLsType.setStatus("current")
_RaisecomOspfRouteMetric_Type = Integer32
_RaisecomOspfRouteMetric_Object = MibTableColumn
raisecomOspfRouteMetric = _RaisecomOspfRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 19, 1, 5),
    _RaisecomOspfRouteMetric_Type()
)
raisecomOspfRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfRouteMetric.setStatus("current")
_RaisecomOspfRouteNextHop_Type = IpAddress
_RaisecomOspfRouteNextHop_Object = MibTableColumn
raisecomOspfRouteNextHop = _RaisecomOspfRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 19, 1, 6),
    _RaisecomOspfRouteNextHop_Type()
)
raisecomOspfRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfRouteNextHop.setStatus("current")
_RaisecomOspfRouteAdvRtr_Type = IpAddress
_RaisecomOspfRouteAdvRtr_Object = MibTableColumn
raisecomOspfRouteAdvRtr = _RaisecomOspfRouteAdvRtr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 19, 1, 7),
    _RaisecomOspfRouteAdvRtr_Type()
)
raisecomOspfRouteAdvRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfRouteAdvRtr.setStatus("current")
_RaisecomOspfRouteArea_Type = Integer32
_RaisecomOspfRouteArea_Object = MibTableColumn
raisecomOspfRouteArea = _RaisecomOspfRouteArea_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 19, 1, 8),
    _RaisecomOspfRouteArea_Type()
)
raisecomOspfRouteArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfRouteArea.setStatus("current")
_RaisecomOspfBdrRouteTable_Object = MibTable
raisecomOspfBdrRouteTable = _RaisecomOspfBdrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 20)
)
if mibBuilder.loadTexts:
    raisecomOspfBdrRouteTable.setStatus("current")
_RaisecomOspfBdrRouteEntry_Object = MibTableRow
raisecomOspfBdrRouteEntry = _RaisecomOspfBdrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 20, 1)
)
raisecomOspfBdrRouteEntry.setIndexNames(
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfBdrRouteRtrType"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfBdrRouteArea"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfBdrRouteDest"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfBdrRouteNextHop"),
)
if mibBuilder.loadTexts:
    raisecomOspfBdrRouteEntry.setStatus("current")


class _RaisecomOspfBdrRouteRtrType_Type(Integer32):
    """Custom type raisecomOspfBdrRouteRtrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asbr", 1),
          ("abr", 2),
          ("sumasbr", 3))
    )


_RaisecomOspfBdrRouteRtrType_Type.__name__ = "Integer32"
_RaisecomOspfBdrRouteRtrType_Object = MibTableColumn
raisecomOspfBdrRouteRtrType = _RaisecomOspfBdrRouteRtrType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 20, 1, 1),
    _RaisecomOspfBdrRouteRtrType_Type()
)
raisecomOspfBdrRouteRtrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfBdrRouteRtrType.setStatus("current")
_RaisecomOspfBdrRouteArea_Type = IpAddress
_RaisecomOspfBdrRouteArea_Object = MibTableColumn
raisecomOspfBdrRouteArea = _RaisecomOspfBdrRouteArea_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 20, 1, 2),
    _RaisecomOspfBdrRouteArea_Type()
)
raisecomOspfBdrRouteArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfBdrRouteArea.setStatus("current")
_RaisecomOspfBdrRouteDest_Type = IpAddress
_RaisecomOspfBdrRouteDest_Object = MibTableColumn
raisecomOspfBdrRouteDest = _RaisecomOspfBdrRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 20, 1, 3),
    _RaisecomOspfBdrRouteDest_Type()
)
raisecomOspfBdrRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfBdrRouteDest.setStatus("current")
_RaisecomOspfBdrRouteNextHop_Type = IpAddress
_RaisecomOspfBdrRouteNextHop_Object = MibTableColumn
raisecomOspfBdrRouteNextHop = _RaisecomOspfBdrRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 20, 1, 4),
    _RaisecomOspfBdrRouteNextHop_Type()
)
raisecomOspfBdrRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfBdrRouteNextHop.setStatus("current")


class _RaisecomOspfBdrRouteLsType_Type(Integer32):
    """Custom type raisecomOspfBdrRouteLsType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("routerLink", 1),
          ("networkLink", 2),
          ("summaryLink", 3),
          ("asSummaryLink", 4),
          ("asExternalLink", 5),
          ("multicastLink", 6),
          ("nssaExternalLink", 7),
          ("areaOpaqueLink", 10))
    )


_RaisecomOspfBdrRouteLsType_Type.__name__ = "Integer32"
_RaisecomOspfBdrRouteLsType_Object = MibTableColumn
raisecomOspfBdrRouteLsType = _RaisecomOspfBdrRouteLsType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 20, 1, 5),
    _RaisecomOspfBdrRouteLsType_Type()
)
raisecomOspfBdrRouteLsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfBdrRouteLsType.setStatus("current")
_RaisecomOspfBdrRouteMetric_Type = Integer32
_RaisecomOspfBdrRouteMetric_Object = MibTableColumn
raisecomOspfBdrRouteMetric = _RaisecomOspfBdrRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 20, 1, 6),
    _RaisecomOspfBdrRouteMetric_Type()
)
raisecomOspfBdrRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfBdrRouteMetric.setStatus("current")
_RaisecomOspfDistributeListGroup_ObjectIdentity = ObjectIdentity
raisecomOspfDistributeListGroup = _RaisecomOspfDistributeListGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 21)
)
_RaisecomOspfDistributeListInTable_Object = MibTable
raisecomOspfDistributeListInTable = _RaisecomOspfDistributeListInTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 21, 1)
)
if mibBuilder.loadTexts:
    raisecomOspfDistributeListInTable.setStatus("current")
_RaisecomOspfDistributeListInEntry_Object = MibTableRow
raisecomOspfDistributeListInEntry = _RaisecomOspfDistributeListInEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 21, 1, 1)
)
raisecomOspfDistributeListInEntry.setIndexNames(
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
)
if mibBuilder.loadTexts:
    raisecomOspfDistributeListInEntry.setStatus("current")


class _RaisecomOspfDistrInIpPrefixListName_Type(OctetString):
    """Custom type raisecomOspfDistrInIpPrefixListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_RaisecomOspfDistrInIpPrefixListName_Type.__name__ = "OctetString"
_RaisecomOspfDistrInIpPrefixListName_Object = MibTableColumn
raisecomOspfDistrInIpPrefixListName = _RaisecomOspfDistrInIpPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 21, 1, 1, 1),
    _RaisecomOspfDistrInIpPrefixListName_Type()
)
raisecomOspfDistrInIpPrefixListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfDistrInIpPrefixListName.setStatus("current")
_RaisecomOspfDistrInAclNum_Type = Integer32
_RaisecomOspfDistrInAclNum_Object = MibTableColumn
raisecomOspfDistrInAclNum = _RaisecomOspfDistrInAclNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 21, 1, 1, 2),
    _RaisecomOspfDistrInAclNum_Type()
)
raisecomOspfDistrInAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfDistrInAclNum.setStatus("current")
_RaisecomOspfDistrInRowStatus_Type = RowStatus
_RaisecomOspfDistrInRowStatus_Object = MibTableColumn
raisecomOspfDistrInRowStatus = _RaisecomOspfDistrInRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 21, 1, 1, 3),
    _RaisecomOspfDistrInRowStatus_Type()
)
raisecomOspfDistrInRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfDistrInRowStatus.setStatus("current")
_RaisecomOspfDistributeListOutTable_Object = MibTable
raisecomOspfDistributeListOutTable = _RaisecomOspfDistributeListOutTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 21, 2)
)
if mibBuilder.loadTexts:
    raisecomOspfDistributeListOutTable.setStatus("current")
_RaisecomOspfDistributeListOutEntry_Object = MibTableRow
raisecomOspfDistributeListOutEntry = _RaisecomOspfDistributeListOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 21, 2, 1)
)
raisecomOspfDistributeListOutEntry.setIndexNames(
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
)
if mibBuilder.loadTexts:
    raisecomOspfDistributeListOutEntry.setStatus("current")


class _RaisecomOspfDistrOutIpPrefixListName_Type(OctetString):
    """Custom type raisecomOspfDistrOutIpPrefixListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_RaisecomOspfDistrOutIpPrefixListName_Type.__name__ = "OctetString"
_RaisecomOspfDistrOutIpPrefixListName_Object = MibTableColumn
raisecomOspfDistrOutIpPrefixListName = _RaisecomOspfDistrOutIpPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 21, 2, 1, 1),
    _RaisecomOspfDistrOutIpPrefixListName_Type()
)
raisecomOspfDistrOutIpPrefixListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfDistrOutIpPrefixListName.setStatus("current")
_RaisecomOspfDistrOutAclNum_Type = Integer32
_RaisecomOspfDistrOutAclNum_Object = MibTableColumn
raisecomOspfDistrOutAclNum = _RaisecomOspfDistrOutAclNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 21, 2, 1, 2),
    _RaisecomOspfDistrOutAclNum_Type()
)
raisecomOspfDistrOutAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfDistrOutAclNum.setStatus("current")
_RaisecomOspfDistrOutRowStatus_Type = RowStatus
_RaisecomOspfDistrOutRowStatus_Object = MibTableColumn
raisecomOspfDistrOutRowStatus = _RaisecomOspfDistrOutRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 21, 2, 1, 3),
    _RaisecomOspfDistrOutRowStatus_Type()
)
raisecomOspfDistrOutRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfDistrOutRowStatus.setStatus("current")
_RaisecomOspfDistributeListOutProtocolTable_Object = MibTable
raisecomOspfDistributeListOutProtocolTable = _RaisecomOspfDistributeListOutProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 21, 3)
)
if mibBuilder.loadTexts:
    raisecomOspfDistributeListOutProtocolTable.setStatus("current")
_RaisecomOspfDistributeListOutProtocolEntry_Object = MibTableRow
raisecomOspfDistributeListOutProtocolEntry = _RaisecomOspfDistributeListOutProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 21, 3, 1)
)
raisecomOspfDistributeListOutProtocolEntry.setIndexNames(
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfDistrOutProtocol"),
    (0, "RAISECOM-OSPFV2-MIB", "raisecomOspfDistrOutProcessId"),
)
if mibBuilder.loadTexts:
    raisecomOspfDistributeListOutProtocolEntry.setStatus("current")


class _RaisecomOspfDistrOutProtocol_Type(Integer32):
    """Custom type raisecomOspfDistrOutProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              8,
              13)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("netmgmt", 3),
          ("rip", 8),
          ("ospf", 13))
    )


_RaisecomOspfDistrOutProtocol_Type.__name__ = "Integer32"
_RaisecomOspfDistrOutProtocol_Object = MibTableColumn
raisecomOspfDistrOutProtocol = _RaisecomOspfDistrOutProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 21, 3, 1, 1),
    _RaisecomOspfDistrOutProtocol_Type()
)
raisecomOspfDistrOutProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfDistrOutProtocol.setStatus("current")
_RaisecomOspfDistrOutProcessId_Type = ProcessID
_RaisecomOspfDistrOutProcessId_Object = MibTableColumn
raisecomOspfDistrOutProcessId = _RaisecomOspfDistrOutProcessId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 21, 3, 1, 2),
    _RaisecomOspfDistrOutProcessId_Type()
)
raisecomOspfDistrOutProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomOspfDistrOutProcessId.setStatus("current")


class _RaisecomOspfDistrOutProIpPrefixListName_Type(OctetString):
    """Custom type raisecomOspfDistrOutProIpPrefixListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_RaisecomOspfDistrOutProIpPrefixListName_Type.__name__ = "OctetString"
_RaisecomOspfDistrOutProIpPrefixListName_Object = MibTableColumn
raisecomOspfDistrOutProIpPrefixListName = _RaisecomOspfDistrOutProIpPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 21, 3, 1, 3),
    _RaisecomOspfDistrOutProIpPrefixListName_Type()
)
raisecomOspfDistrOutProIpPrefixListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfDistrOutProIpPrefixListName.setStatus("current")
_RaisecomOspfDistrOutProAclNum_Type = Integer32
_RaisecomOspfDistrOutProAclNum_Object = MibTableColumn
raisecomOspfDistrOutProAclNum = _RaisecomOspfDistrOutProAclNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 21, 3, 1, 4),
    _RaisecomOspfDistrOutProAclNum_Type()
)
raisecomOspfDistrOutProAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfDistrOutProAclNum.setStatus("current")
_RaisecomOspfDistrOutProRowStatus_Type = RowStatus
_RaisecomOspfDistrOutProRowStatus_Object = MibTableColumn
raisecomOspfDistrOutProRowStatus = _RaisecomOspfDistrOutProRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 2, 21, 3, 1, 5),
    _RaisecomOspfDistrOutProRowStatus_Type()
)
raisecomOspfDistrOutProRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomOspfDistrOutProRowStatus.setStatus("current")
_RaisecomOspfConformance_ObjectIdentity = ObjectIdentity
raisecomOspfConformance = _RaisecomOspfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 3)
)

# Managed Objects groups


# Notification objects

raisecomOspfIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 2, 1)
)
raisecomOspfIfStateChange.setObjects(
      *(("RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfRouterId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfIfIpAddress"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfAddressLessIf"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfIfState"))
)
if mibBuilder.loadTexts:
    raisecomOspfIfStateChange.setStatus(
        "current"
    )

raisecomOspfVirtIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 2, 2)
)
raisecomOspfVirtIfStateChange.setObjects(
      *(("RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfRouterId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfVirtIfAreaId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfVirtIfNeighbor"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfVirtIfState"))
)
if mibBuilder.loadTexts:
    raisecomOspfVirtIfStateChange.setStatus(
        "current"
    )

raisecomOspfNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 2, 3)
)
raisecomOspfNbrStateChange.setObjects(
      *(("RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfRouterId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfNbrIpAddr"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfNbrAddressLessIndex"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfNbrRtrId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfNbrState"))
)
if mibBuilder.loadTexts:
    raisecomOspfNbrStateChange.setStatus(
        "current"
    )

raisecomOspfVirtNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 2, 4)
)
raisecomOspfVirtNbrStateChange.setObjects(
      *(("RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfRouterId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfVirtNbrArea"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfVirtNbrRtrId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfVirtNbrState"))
)
if mibBuilder.loadTexts:
    raisecomOspfVirtNbrStateChange.setStatus(
        "current"
    )

raisecomOspfIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 2, 5)
)
raisecomOspfIfConfigError.setObjects(
      *(("RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfRouterId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfIfIpAddress"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfAddressLessIf"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfPacketSrc"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfConfigErrorType"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfPacketType"))
)
if mibBuilder.loadTexts:
    raisecomOspfIfConfigError.setStatus(
        "current"
    )

raisecomOspfVirtIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 2, 6)
)
raisecomOspfVirtIfConfigError.setObjects(
      *(("RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfRouterId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfVirtIfAreaId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfVirtIfNeighbor"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfConfigErrorType"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfPacketType"))
)
if mibBuilder.loadTexts:
    raisecomOspfVirtIfConfigError.setStatus(
        "current"
    )

raisecomOspfIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 2, 7)
)
raisecomOspfIfAuthFailure.setObjects(
      *(("RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfRouterId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfIfIpAddress"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfAddressLessIf"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfPacketSrc"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfConfigErrorType"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfPacketType"))
)
if mibBuilder.loadTexts:
    raisecomOspfIfAuthFailure.setStatus(
        "current"
    )

raisecomOspfVirtIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 2, 8)
)
raisecomOspfVirtIfAuthFailure.setObjects(
      *(("RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfRouterId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfVirtIfAreaId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfVirtIfNeighbor"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfConfigErrorType"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfPacketType"))
)
if mibBuilder.loadTexts:
    raisecomOspfVirtIfAuthFailure.setStatus(
        "current"
    )

raisecomOspfIfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 2, 9)
)
raisecomOspfIfRxBadPacket.setObjects(
      *(("RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfRouterId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfIfIpAddress"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfAddressLessIf"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfPacketSrc"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfPacketType"))
)
if mibBuilder.loadTexts:
    raisecomOspfIfRxBadPacket.setStatus(
        "current"
    )

raisecomOspfVirtIfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 2, 10)
)
raisecomOspfVirtIfRxBadPacket.setObjects(
      *(("RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfRouterId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfVirtIfAreaId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfVirtIfNeighbor"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfPacketType"))
)
if mibBuilder.loadTexts:
    raisecomOspfVirtIfRxBadPacket.setStatus(
        "current"
    )

raisecomOspfTxRetransmit = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 2, 11)
)
raisecomOspfTxRetransmit.setObjects(
      *(("RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfRouterId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfIfIpAddress"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfAddressLessIf"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfNbrRtrId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfPacketType"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfLsdbType"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfLsdbLsId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    raisecomOspfTxRetransmit.setStatus(
        "current"
    )

raisecomOspfVirtIfTxRetransmit = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 2, 12)
)
raisecomOspfVirtIfTxRetransmit.setObjects(
      *(("RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfRouterId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfVirtIfAreaId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfVirtIfNeighbor"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfPacketType"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfLsdbType"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfLsdbLsId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    raisecomOspfVirtIfTxRetransmit.setStatus(
        "current"
    )

raisecomOspfOriginateLsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 2, 13)
)
raisecomOspfOriginateLsa.setObjects(
      *(("RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfRouterId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfLsdbAreaId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfLsdbType"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfLsdbLsId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    raisecomOspfOriginateLsa.setStatus(
        "current"
    )

raisecomOspfMaxAgeLsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 2, 14)
)
raisecomOspfMaxAgeLsa.setObjects(
      *(("RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfRouterId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfLsdbAreaId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfLsdbType"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfLsdbLsId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    raisecomOspfMaxAgeLsa.setStatus(
        "current"
    )

raisecomOspfLsdbOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 2, 15)
)
raisecomOspfLsdbOverflow.setObjects(
      *(("RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfRouterId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfExtLsdbLimit"))
)
if mibBuilder.loadTexts:
    raisecomOspfLsdbOverflow.setStatus(
        "current"
    )

raisecomOspfLsdbApproachingOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 2, 16)
)
raisecomOspfLsdbApproachingOverflow.setObjects(
      *(("RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfRouterId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfExtLsdbLimit"))
)
if mibBuilder.loadTexts:
    raisecomOspfLsdbApproachingOverflow.setStatus(
        "current"
    )

raisecomOspfIfKeyValid = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 2, 17)
)
raisecomOspfIfKeyValid.setObjects(
      *(("RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfRouterId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfIfIpAddress"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfAddressLessIf"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfIfAuthKeyChain"))
)
if mibBuilder.loadTexts:
    raisecomOspfIfKeyValid.setStatus(
        "current"
    )

raisecomOspfIfLastKeyExpiration = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 2, 18)
)
raisecomOspfIfLastKeyExpiration.setObjects(
      *(("RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfRouterId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfIfIpAddress"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfAddressLessIf"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfIfAuthKeyChain"))
)
if mibBuilder.loadTexts:
    raisecomOspfIfLastKeyExpiration.setStatus(
        "current"
    )

raisecomOspfVirtIfKeyValid = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 2, 19)
)
raisecomOspfVirtIfKeyValid.setObjects(
      *(("RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfRouterId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfVirtIfAreaId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfVirtIfNeighbor"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfVirtIfAuthKeyChain"))
)
if mibBuilder.loadTexts:
    raisecomOspfVirtIfKeyValid.setStatus(
        "current"
    )

raisecomOspfVirtIfLastKeyExpiration = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 2, 20)
)
raisecomOspfVirtIfLastKeyExpiration.setObjects(
      *(("RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfRouterId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfVirtIfAreaId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfVirtIfNeighbor"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfVirtIfAuthKeyChain"))
)
if mibBuilder.loadTexts:
    raisecomOspfVirtIfLastKeyExpiration.setStatus(
        "current"
    )

raisecomOspfRedistributeOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 2, 21)
)
raisecomOspfRedistributeOverflow.setObjects(
      *(("RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfRedistributeProtocol"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfRedistributeProcessId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfRedistributeRouteLimit"))
)
if mibBuilder.loadTexts:
    raisecomOspfRedistributeOverflow.setStatus(
        "current"
    )

raisecomOspfRedistributeNotOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 47, 1, 2, 22)
)
raisecomOspfRedistributeNotOverflow.setObjects(
      *(("RAISECOM-OSPFV2-MIB", "raisecomOspfProcessId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfRedistributeProtocol"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfRedistributeProcessId"),
        ("RAISECOM-OSPFV2-MIB", "raisecomOspfRedistributeRouteLimit"))
)
if mibBuilder.loadTexts:
    raisecomOspfRedistributeNotOverflow.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-OSPFV2-MIB",
    **{"ProcessID": ProcessID,
       "AreaID": AreaID,
       "RouterID": RouterID,
       "Metric": Metric,
       "BigMetric": BigMetric,
       "Status": Status,
       "PositiveInteger": PositiveInteger,
       "HelloRange": HelloRange,
       "UpToMaxAge": UpToMaxAge,
       "DesignatedRouterPriority": DesignatedRouterPriority,
       "OspfAuthenticationType": OspfAuthenticationType,
       "raisecomOspf": raisecomOspf,
       "raisecomOspfNotifications": raisecomOspfNotifications,
       "raisecomOspfTrapControlTable": raisecomOspfTrapControlTable,
       "raisecomOspfTrapControlEntry": raisecomOspfTrapControlEntry,
       "raisecomOspfSetTrap": raisecomOspfSetTrap,
       "raisecomOspfConfigErrorType": raisecomOspfConfigErrorType,
       "raisecomOspfPacketType": raisecomOspfPacketType,
       "raisecomOspfPacketSrc": raisecomOspfPacketSrc,
       "raisecomOspfTraps": raisecomOspfTraps,
       "raisecomOspfIfStateChange": raisecomOspfIfStateChange,
       "raisecomOspfVirtIfStateChange": raisecomOspfVirtIfStateChange,
       "raisecomOspfNbrStateChange": raisecomOspfNbrStateChange,
       "raisecomOspfVirtNbrStateChange": raisecomOspfVirtNbrStateChange,
       "raisecomOspfIfConfigError": raisecomOspfIfConfigError,
       "raisecomOspfVirtIfConfigError": raisecomOspfVirtIfConfigError,
       "raisecomOspfIfAuthFailure": raisecomOspfIfAuthFailure,
       "raisecomOspfVirtIfAuthFailure": raisecomOspfVirtIfAuthFailure,
       "raisecomOspfIfRxBadPacket": raisecomOspfIfRxBadPacket,
       "raisecomOspfVirtIfRxBadPacket": raisecomOspfVirtIfRxBadPacket,
       "raisecomOspfTxRetransmit": raisecomOspfTxRetransmit,
       "raisecomOspfVirtIfTxRetransmit": raisecomOspfVirtIfTxRetransmit,
       "raisecomOspfOriginateLsa": raisecomOspfOriginateLsa,
       "raisecomOspfMaxAgeLsa": raisecomOspfMaxAgeLsa,
       "raisecomOspfLsdbOverflow": raisecomOspfLsdbOverflow,
       "raisecomOspfLsdbApproachingOverflow": raisecomOspfLsdbApproachingOverflow,
       "raisecomOspfIfKeyValid": raisecomOspfIfKeyValid,
       "raisecomOspfIfLastKeyExpiration": raisecomOspfIfLastKeyExpiration,
       "raisecomOspfVirtIfKeyValid": raisecomOspfVirtIfKeyValid,
       "raisecomOspfVirtIfLastKeyExpiration": raisecomOspfVirtIfLastKeyExpiration,
       "raisecomOspfRedistributeOverflow": raisecomOspfRedistributeOverflow,
       "raisecomOspfRedistributeNotOverflow": raisecomOspfRedistributeNotOverflow,
       "raisecomOspfObjects": raisecomOspfObjects,
       "raisecomOspfGlobalTable": raisecomOspfGlobalTable,
       "raisecomOspfGlobalEntry": raisecomOspfGlobalEntry,
       "raisecomOspfProcessId": raisecomOspfProcessId,
       "raisecomOspfRouterId": raisecomOspfRouterId,
       "raisecomOspfAdminStat": raisecomOspfAdminStat,
       "raisecomOspfVersionNumber": raisecomOspfVersionNumber,
       "raisecomOspfAreaBdrRtrStatus": raisecomOspfAreaBdrRtrStatus,
       "raisecomOspfASBdrRtrStatus": raisecomOspfASBdrRtrStatus,
       "raisecomOspfExternLsaCount": raisecomOspfExternLsaCount,
       "raisecomOspfExternLsaCksumSum": raisecomOspfExternLsaCksumSum,
       "raisecomOspfOriginateNewLsas": raisecomOspfOriginateNewLsas,
       "raisecomOspfRxNewLsas": raisecomOspfRxNewLsas,
       "raisecomOspfExtLsdbLimit": raisecomOspfExtLsdbLimit,
       "raisecomOspfExitOverflowInterval": raisecomOspfExitOverflowInterval,
       "raisecomOspfReferenceBandwidth": raisecomOspfReferenceBandwidth,
       "raisecomOspfAsLsaCount": raisecomOspfAsLsaCount,
       "raisecomOspfAsLsaCksumSum": raisecomOspfAsLsaCksumSum,
       "raisecomOspfStubRouterSupport": raisecomOspfStubRouterSupport,
       "raisecomOspfStubRouterAdvertisement": raisecomOspfStubRouterAdvertisement,
       "raisecomOspfAdminDistance": raisecomOspfAdminDistance,
       "raisecomOspfSpfInterval": raisecomOspfSpfInterval,
       "raisecomOspfReset": raisecomOspfReset,
       "raisecomOspfExportMetric": raisecomOspfExportMetric,
       "raisecomOspfExportTag": raisecomOspfExportTag,
       "raisecomOspfExportType": raisecomOspfExportType,
       "raisecomOspfNetCounts": raisecomOspfNetCounts,
       "raisecomOspfAreaCounts": raisecomOspfAreaCounts,
       "raisecomOspfNssaAreaCounts": raisecomOspfNssaAreaCounts,
       "raisecomOspfSpfCounts": raisecomOspfSpfCounts,
       "raisecomOspfGlobalStatus": raisecomOspfGlobalStatus,
       "raisecomOspfRedistributeRouteLimit": raisecomOspfRedistributeRouteLimit,
       "raisecomOspfAreaTable": raisecomOspfAreaTable,
       "raisecomOspfAreaEntry": raisecomOspfAreaEntry,
       "raisecomOspfAreaId": raisecomOspfAreaId,
       "raisecomOspfAuthType": raisecomOspfAuthType,
       "raisecomOspfImportAsExtern": raisecomOspfImportAsExtern,
       "raisecomOspfSpfRuns": raisecomOspfSpfRuns,
       "raisecomOspfAreaBdrRtrCount": raisecomOspfAreaBdrRtrCount,
       "raisecomOspfAsBdrRtrCount": raisecomOspfAsBdrRtrCount,
       "raisecomOspfAreaLsaCount": raisecomOspfAreaLsaCount,
       "raisecomOspfAreaLsaCksumSum": raisecomOspfAreaLsaCksumSum,
       "raisecomOspfAreaSummary": raisecomOspfAreaSummary,
       "raisecomOspfAreaNssaTranslatorRole": raisecomOspfAreaNssaTranslatorRole,
       "raisecomOspfAreaNssaTranslatorState": raisecomOspfAreaNssaTranslatorState,
       "raisecomOspfAreaNssaTranslatorStabilityInterval": raisecomOspfAreaNssaTranslatorStabilityInterval,
       "raisecomOspfAreaNssaTranslatorEvents": raisecomOspfAreaNssaTranslatorEvents,
       "raisecomOspfAreaDefaultCost": raisecomOspfAreaDefaultCost,
       "raisecomOspfAreaType": raisecomOspfAreaType,
       "raisecomOspfAreaAbrCount": raisecomOspfAreaAbrCount,
       "raisecomOspfAreaAsbrCount": raisecomOspfAreaAsbrCount,
       "raisecomOspfAreaStatus": raisecomOspfAreaStatus,
       "raisecomOspfAreaFilterInIpPrefixListName": raisecomOspfAreaFilterInIpPrefixListName,
       "raisecomOspfAreaFilterOutIpPrefixListName": raisecomOspfAreaFilterOutIpPrefixListName,
       "raisecomOspfNetWorkTable": raisecomOspfNetWorkTable,
       "raisecomOspfNetWorkEntry": raisecomOspfNetWorkEntry,
       "raisecomOspfNet": raisecomOspfNet,
       "raisecomOspfMask": raisecomOspfMask,
       "raisecomOspfNetWorkStatus": raisecomOspfNetWorkStatus,
       "raisecomOspfStubAreaTable": raisecomOspfStubAreaTable,
       "raisecomOspfStubAreaEntry": raisecomOspfStubAreaEntry,
       "raisecomOspfStubAreaId": raisecomOspfStubAreaId,
       "raisecomOspfStubAreaOption": raisecomOspfStubAreaOption,
       "raisecomOspfStubAreaStatus": raisecomOspfStubAreaStatus,
       "raisecomOspfNssaAreaTable": raisecomOspfNssaAreaTable,
       "raisecomOspfNssaAreaEntry": raisecomOspfNssaAreaEntry,
       "raisecomOspfNssaAreaId": raisecomOspfNssaAreaId,
       "raisecomOspfNssaAreaOption": raisecomOspfNssaAreaOption,
       "raisecomOspfNssaAreaStatus": raisecomOspfNssaAreaStatus,
       "raisecomOspfIfTable": raisecomOspfIfTable,
       "raisecomOspfIfEntry": raisecomOspfIfEntry,
       "raisecomOspfAddressLessIf": raisecomOspfAddressLessIf,
       "raisecomOspfIfIpAddress": raisecomOspfIfIpAddress,
       "raisecomOspfIfAreaId": raisecomOspfIfAreaId,
       "raisecomOspfIfType": raisecomOspfIfType,
       "raisecomOspfIfAdminStat": raisecomOspfIfAdminStat,
       "raisecomOspfIfRtrPriority": raisecomOspfIfRtrPriority,
       "raisecomOspfIfTransitDelay": raisecomOspfIfTransitDelay,
       "raisecomOspfIfRetransInterval": raisecomOspfIfRetransInterval,
       "raisecomOspfIfHelloInterval": raisecomOspfIfHelloInterval,
       "raisecomOspfIfRtrDeadInterval": raisecomOspfIfRtrDeadInterval,
       "raisecomOspfIfPollInterval": raisecomOspfIfPollInterval,
       "raisecomOspfIfState": raisecomOspfIfState,
       "raisecomOspfIfDesignatedRouter": raisecomOspfIfDesignatedRouter,
       "raisecomOspfIfBackupDesignatedRouter": raisecomOspfIfBackupDesignatedRouter,
       "raisecomOspfIfEvents": raisecomOspfIfEvents,
       "raisecomOspfIfAuthKeyId": raisecomOspfIfAuthKeyId,
       "raisecomOspfIfAuthSimpleKeyType": raisecomOspfIfAuthSimpleKeyType,
       "raisecomOspfIfAuthMd5KeyType": raisecomOspfIfAuthMd5KeyType,
       "raisecomOspfIfAuthSimpleKey": raisecomOspfIfAuthSimpleKey,
       "raisecomOspfIfAuthMd5Key": raisecomOspfIfAuthMd5Key,
       "raisecomOspfIfAuthKeyChain": raisecomOspfIfAuthKeyChain,
       "raisecomOspfIfAuthType": raisecomOspfIfAuthType,
       "raisecomOspfIfLsaCount": raisecomOspfIfLsaCount,
       "raisecomOspfIfLsaCksumSum": raisecomOspfIfLsaCksumSum,
       "raisecomOspfIfDesignatedRouterId": raisecomOspfIfDesignatedRouterId,
       "raisecomOspfIfBackupDesignatedRouterId": raisecomOspfIfBackupDesignatedRouterId,
       "raisecomOspfIfPassive": raisecomOspfIfPassive,
       "raisecomOspfIfMtu": raisecomOspfIfMtu,
       "raisecomOspfIfMetric": raisecomOspfIfMetric,
       "raisecomOspfVirtIfTable": raisecomOspfVirtIfTable,
       "raisecomOspfVirtIfEntry": raisecomOspfVirtIfEntry,
       "raisecomOspfVirtIfAreaId": raisecomOspfVirtIfAreaId,
       "raisecomOspfVirtIfNeighbor": raisecomOspfVirtIfNeighbor,
       "raisecomOspfVirtIfTransitDelay": raisecomOspfVirtIfTransitDelay,
       "raisecomOspfVirtIfRetransInterval": raisecomOspfVirtIfRetransInterval,
       "raisecomOspfVirtIfHelloInterval": raisecomOspfVirtIfHelloInterval,
       "raisecomOspfVirtIfRtrDeadInterval": raisecomOspfVirtIfRtrDeadInterval,
       "raisecomOspfVirtIfState": raisecomOspfVirtIfState,
       "raisecomOspfVirtIfEvents": raisecomOspfVirtIfEvents,
       "raisecomOspfVirtIfAuthKeyId": raisecomOspfVirtIfAuthKeyId,
       "raisecomOspfVirtIfAuthSimpleKeyType": raisecomOspfVirtIfAuthSimpleKeyType,
       "raisecomOspfVirtIfAuthMd5KeyType": raisecomOspfVirtIfAuthMd5KeyType,
       "raisecomOspfVirtIfAuthSimpleKey": raisecomOspfVirtIfAuthSimpleKey,
       "raisecomOspfVirtIfAuthMd5Key": raisecomOspfVirtIfAuthMd5Key,
       "raisecomOspfVirtIfAuthKeyChain": raisecomOspfVirtIfAuthKeyChain,
       "raisecomOspfVirtIfAuthType": raisecomOspfVirtIfAuthType,
       "raisecomOspfVirtIfLsaCount": raisecomOspfVirtIfLsaCount,
       "raisecomOspfVirtIfLsaCksumSum": raisecomOspfVirtIfLsaCksumSum,
       "raisecomOspfVirtIfCost": raisecomOspfVirtIfCost,
       "raisecomOspfVirtIfStatus": raisecomOspfVirtIfStatus,
       "raisecomOspfNbrTable": raisecomOspfNbrTable,
       "raisecomOspfNbrEntry": raisecomOspfNbrEntry,
       "raisecomOspfNbrIpAddr": raisecomOspfNbrIpAddr,
       "raisecomOspfNbrAddressLessIndex": raisecomOspfNbrAddressLessIndex,
       "raisecomOspfNbrRtrId": raisecomOspfNbrRtrId,
       "raisecomOspfNbrOptions": raisecomOspfNbrOptions,
       "raisecomOspfNbrPriority": raisecomOspfNbrPriority,
       "raisecomOspfNbrState": raisecomOspfNbrState,
       "raisecomOspfNbrEvents": raisecomOspfNbrEvents,
       "raisecomOspfNbrLsRetransQLen": raisecomOspfNbrLsRetransQLen,
       "raisecomOspfNbrMode": raisecomOspfNbrMode,
       "raisecomOspfNbmaCfgNbrTable": raisecomOspfNbmaCfgNbrTable,
       "raisecomOspfNbmaCfgNbrEntry": raisecomOspfNbmaCfgNbrEntry,
       "raisecomOspfNbmaCfgNbrIpAddr": raisecomOspfNbmaCfgNbrIpAddr,
       "raisecomOspfNbmaCfgNbrPriority": raisecomOspfNbmaCfgNbrPriority,
       "raisecomOspfNbmaCfgNbrStatus": raisecomOspfNbmaCfgNbrStatus,
       "raisecomOspfVirtNbrTable": raisecomOspfVirtNbrTable,
       "raisecomOspfVirtNbrEntry": raisecomOspfVirtNbrEntry,
       "raisecomOspfVirtNbrArea": raisecomOspfVirtNbrArea,
       "raisecomOspfVirtNbrRtrId": raisecomOspfVirtNbrRtrId,
       "raisecomOspfVirtNbrIpAddr": raisecomOspfVirtNbrIpAddr,
       "raisecomOspfVirtNbrOptions": raisecomOspfVirtNbrOptions,
       "raisecomOspfVirtNbrState": raisecomOspfVirtNbrState,
       "raisecomOspfVirtNbrEvents": raisecomOspfVirtNbrEvents,
       "raisecomOspfVirtNbrLsRetransQLen": raisecomOspfVirtNbrLsRetransQLen,
       "raisecomOspfVirtNbrLessIf": raisecomOspfVirtNbrLessIf,
       "raisecomOspfVirtNbrMode": raisecomOspfVirtNbrMode,
       "raisecomOspfAreaAggregateTable": raisecomOspfAreaAggregateTable,
       "raisecomOspfAreaAggregateEntry": raisecomOspfAreaAggregateEntry,
       "raisecomOspfAreaAggregateAreaID": raisecomOspfAreaAggregateAreaID,
       "raisecomOspfAreaAggregateLsdbType": raisecomOspfAreaAggregateLsdbType,
       "raisecomOspfAreaAggregateNet": raisecomOspfAreaAggregateNet,
       "raisecomOspfAreaAggregateMask": raisecomOspfAreaAggregateMask,
       "raisecomOspfAreaAggregateEffect": raisecomOspfAreaAggregateEffect,
       "raisecomOspfAreaAggregateStatus": raisecomOspfAreaAggregateStatus,
       "raisecomOspfExternalAggregateTable": raisecomOspfExternalAggregateTable,
       "raisecomOspfExternalAggregateEntry": raisecomOspfExternalAggregateEntry,
       "raisecomOspfExternalAggregateNet": raisecomOspfExternalAggregateNet,
       "raisecomOspfExternalAggregateMask": raisecomOspfExternalAggregateMask,
       "raisecomOspfExternalAggregateEffect": raisecomOspfExternalAggregateEffect,
       "raisecomOspfExternalAggregateCost": raisecomOspfExternalAggregateCost,
       "raisecomOspfExternalAggregateStatus": raisecomOspfExternalAggregateStatus,
       "raisecomOspfLsdbTable": raisecomOspfLsdbTable,
       "raisecomOspfLsdbEntry": raisecomOspfLsdbEntry,
       "raisecomOspfLsdbAreaId": raisecomOspfLsdbAreaId,
       "raisecomOspfLsdbType": raisecomOspfLsdbType,
       "raisecomOspfLsdbLsId": raisecomOspfLsdbLsId,
       "raisecomOspfLsdbRouterId": raisecomOspfLsdbRouterId,
       "raisecomOspfLsdbSequence": raisecomOspfLsdbSequence,
       "raisecomOspfLsdbAge": raisecomOspfLsdbAge,
       "raisecomOspfLsdbChecksum": raisecomOspfLsdbChecksum,
       "raisecomOspfLsdbAdvertisement": raisecomOspfLsdbAdvertisement,
       "raisecomOspfAsLsdbTable": raisecomOspfAsLsdbTable,
       "raisecomOspfAsLsdbEntry": raisecomOspfAsLsdbEntry,
       "raisecomOspfAsLsdbType": raisecomOspfAsLsdbType,
       "raisecomOspfAsLsdbLsId": raisecomOspfAsLsdbLsId,
       "raisecomOspfAsLsdbRouterId": raisecomOspfAsLsdbRouterId,
       "raisecomOspfAsLsdbSequence": raisecomOspfAsLsdbSequence,
       "raisecomOspfAsLsdbAge": raisecomOspfAsLsdbAge,
       "raisecomOspfAsLsdbChecksum": raisecomOspfAsLsdbChecksum,
       "raisecomOspfAsLsdbAdvertisement": raisecomOspfAsLsdbAdvertisement,
       "raisecomOspfAreaLsaCountTable": raisecomOspfAreaLsaCountTable,
       "raisecomOspfAreaLsaCountEntry": raisecomOspfAreaLsaCountEntry,
       "raisecomOspfAreaLsaCountAreaId": raisecomOspfAreaLsaCountAreaId,
       "raisecomOspfAreaLsaCountLsaType": raisecomOspfAreaLsaCountLsaType,
       "raisecomOspfAreaLsaCountNumber": raisecomOspfAreaLsaCountNumber,
       "raisecomOspfRedistributeTable": raisecomOspfRedistributeTable,
       "raisecomOspfRedistributeEntry": raisecomOspfRedistributeEntry,
       "raisecomOspfRedistributeProtocol": raisecomOspfRedistributeProtocol,
       "raisecomOspfRedistributeProcessId": raisecomOspfRedistributeProcessId,
       "raisecomOspfRedistributeCost": raisecomOspfRedistributeCost,
       "raisecomOspfRedistributeType": raisecomOspfRedistributeType,
       "raisecomOspfRedistributeStatus": raisecomOspfRedistributeStatus,
       "raisecomOspfRedistributeRouteMapName": raisecomOspfRedistributeRouteMapName,
       "raisecomOspfRedistributeTag": raisecomOspfRedistributeTag,
       "raisecomOspfDefaultInfoTable": raisecomOspfDefaultInfoTable,
       "raisecomOspfDefaultInfoEntry": raisecomOspfDefaultInfoEntry,
       "raisecomOspfDefaultInfoAlways": raisecomOspfDefaultInfoAlways,
       "raisecomOspfDefaultInfoCost": raisecomOspfDefaultInfoCost,
       "raisecomOspfDefaultInfoType": raisecomOspfDefaultInfoType,
       "raisecomOspfDefaultInfoStatus": raisecomOspfDefaultInfoStatus,
       "raisecomOspfPacketIoStatisTable": raisecomOspfPacketIoStatisTable,
       "raisecomOspfPacketIoStatisEntry": raisecomOspfPacketIoStatisEntry,
       "raisecomOspfPacketIoStatisIoType": raisecomOspfPacketIoStatisIoType,
       "raisecomOspfPacketIoStatisPktType": raisecomOspfPacketIoStatisPktType,
       "raisecomOspfPacketIoStatisNumber": raisecomOspfPacketIoStatisNumber,
       "raisecomOspfRouteTable": raisecomOspfRouteTable,
       "raisecomOspfRouteEntry": raisecomOspfRouteEntry,
       "raisecomOspfRouteDest": raisecomOspfRouteDest,
       "raisecomOspfRouteMask": raisecomOspfRouteMask,
       "raisecomOspfRouteType": raisecomOspfRouteType,
       "raisecomOspfRouteLsType": raisecomOspfRouteLsType,
       "raisecomOspfRouteMetric": raisecomOspfRouteMetric,
       "raisecomOspfRouteNextHop": raisecomOspfRouteNextHop,
       "raisecomOspfRouteAdvRtr": raisecomOspfRouteAdvRtr,
       "raisecomOspfRouteArea": raisecomOspfRouteArea,
       "raisecomOspfBdrRouteTable": raisecomOspfBdrRouteTable,
       "raisecomOspfBdrRouteEntry": raisecomOspfBdrRouteEntry,
       "raisecomOspfBdrRouteRtrType": raisecomOspfBdrRouteRtrType,
       "raisecomOspfBdrRouteArea": raisecomOspfBdrRouteArea,
       "raisecomOspfBdrRouteDest": raisecomOspfBdrRouteDest,
       "raisecomOspfBdrRouteNextHop": raisecomOspfBdrRouteNextHop,
       "raisecomOspfBdrRouteLsType": raisecomOspfBdrRouteLsType,
       "raisecomOspfBdrRouteMetric": raisecomOspfBdrRouteMetric,
       "raisecomOspfDistributeListGroup": raisecomOspfDistributeListGroup,
       "raisecomOspfDistributeListInTable": raisecomOspfDistributeListInTable,
       "raisecomOspfDistributeListInEntry": raisecomOspfDistributeListInEntry,
       "raisecomOspfDistrInIpPrefixListName": raisecomOspfDistrInIpPrefixListName,
       "raisecomOspfDistrInAclNum": raisecomOspfDistrInAclNum,
       "raisecomOspfDistrInRowStatus": raisecomOspfDistrInRowStatus,
       "raisecomOspfDistributeListOutTable": raisecomOspfDistributeListOutTable,
       "raisecomOspfDistributeListOutEntry": raisecomOspfDistributeListOutEntry,
       "raisecomOspfDistrOutIpPrefixListName": raisecomOspfDistrOutIpPrefixListName,
       "raisecomOspfDistrOutAclNum": raisecomOspfDistrOutAclNum,
       "raisecomOspfDistrOutRowStatus": raisecomOspfDistrOutRowStatus,
       "raisecomOspfDistributeListOutProtocolTable": raisecomOspfDistributeListOutProtocolTable,
       "raisecomOspfDistributeListOutProtocolEntry": raisecomOspfDistributeListOutProtocolEntry,
       "raisecomOspfDistrOutProtocol": raisecomOspfDistrOutProtocol,
       "raisecomOspfDistrOutProcessId": raisecomOspfDistrOutProcessId,
       "raisecomOspfDistrOutProIpPrefixListName": raisecomOspfDistrOutProIpPrefixListName,
       "raisecomOspfDistrOutProAclNum": raisecomOspfDistrOutProAclNum,
       "raisecomOspfDistrOutProRowStatus": raisecomOspfDistrOutProRowStatus,
       "raisecomOspfConformance": raisecomOspfConformance}
)
