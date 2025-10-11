# SNMP MIB module (SUPERMICRO-ISIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-ISIS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:03:00 2025
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

fsIsis = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62)
)
if mibBuilder.loadTexts:
    fsIsis.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MetricType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2))
    )



# MIB Managed Objects in the order of their OIDs

_FsIsisScl_ObjectIdentity = ObjectIdentity
fsIsisScl = _FsIsisScl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 1)
)


class _FsIsisMaxInstances_Type(Integer32):
    """Custom type fsIsisMaxInstances based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsIsisMaxInstances_Type.__name__ = "Integer32"
_FsIsisMaxInstances_Object = MibScalar
fsIsisMaxInstances = _FsIsisMaxInstances_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 1, 1),
    _FsIsisMaxInstances_Type()
)
fsIsisMaxInstances.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisMaxInstances.setStatus("current")


class _FsIsisMaxCircuits_Type(Integer32):
    """Custom type fsIsisMaxCircuits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000),
    )


_FsIsisMaxCircuits_Type.__name__ = "Integer32"
_FsIsisMaxCircuits_Object = MibScalar
fsIsisMaxCircuits = _FsIsisMaxCircuits_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 1, 2),
    _FsIsisMaxCircuits_Type()
)
fsIsisMaxCircuits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisMaxCircuits.setStatus("current")


class _FsIsisMaxAreaAddrs_Type(Integer32):
    """Custom type fsIsisMaxAreaAddrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_FsIsisMaxAreaAddrs_Type.__name__ = "Integer32"
_FsIsisMaxAreaAddrs_Object = MibScalar
fsIsisMaxAreaAddrs = _FsIsisMaxAreaAddrs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 1, 3),
    _FsIsisMaxAreaAddrs_Type()
)
fsIsisMaxAreaAddrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisMaxAreaAddrs.setStatus("current")


class _FsIsisMaxAdjs_Type(Integer32):
    """Custom type fsIsisMaxAdjs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000),
    )


_FsIsisMaxAdjs_Type.__name__ = "Integer32"
_FsIsisMaxAdjs_Object = MibScalar
fsIsisMaxAdjs = _FsIsisMaxAdjs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 1, 4),
    _FsIsisMaxAdjs_Type()
)
fsIsisMaxAdjs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisMaxAdjs.setStatus("current")


class _FsIsisMaxIPRAs_Type(Integer32):
    """Custom type fsIsisMaxIPRAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000),
    )


_FsIsisMaxIPRAs_Type.__name__ = "Integer32"
_FsIsisMaxIPRAs_Object = MibScalar
fsIsisMaxIPRAs = _FsIsisMaxIPRAs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 1, 5),
    _FsIsisMaxIPRAs_Type()
)
fsIsisMaxIPRAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisMaxIPRAs.setStatus("current")


class _FsIsisMaxEvents_Type(Integer32):
    """Custom type fsIsisMaxEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000),
    )


_FsIsisMaxEvents_Type.__name__ = "Integer32"
_FsIsisMaxEvents_Object = MibScalar
fsIsisMaxEvents = _FsIsisMaxEvents_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 1, 6),
    _FsIsisMaxEvents_Type()
)
fsIsisMaxEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisMaxEvents.setStatus("current")


class _FsIsisMaxSummAddr_Type(Integer32):
    """Custom type fsIsisMaxSummAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000),
    )


_FsIsisMaxSummAddr_Type.__name__ = "Integer32"
_FsIsisMaxSummAddr_Object = MibScalar
fsIsisMaxSummAddr = _FsIsisMaxSummAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 1, 7),
    _FsIsisMaxSummAddr_Type()
)
fsIsisMaxSummAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisMaxSummAddr.setStatus("current")


class _FsIsisStatus_Type(Integer32):
    """Custom type fsIsisStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("shutdown", 2),
          ("reset", 3))
    )


_FsIsisStatus_Type.__name__ = "Integer32"
_FsIsisStatus_Object = MibScalar
fsIsisStatus = _FsIsisStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 1, 8),
    _FsIsisStatus_Type()
)
fsIsisStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisStatus.setStatus("current")


class _FsIsisMaxLSPEntries_Type(Integer32):
    """Custom type fsIsisMaxLSPEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000),
    )


_FsIsisMaxLSPEntries_Type.__name__ = "Integer32"
_FsIsisMaxLSPEntries_Object = MibScalar
fsIsisMaxLSPEntries = _FsIsisMaxLSPEntries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 1, 9),
    _FsIsisMaxLSPEntries_Type()
)
fsIsisMaxLSPEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisMaxLSPEntries.setStatus("current")


class _FsIsisMaxMAA_Type(Integer32):
    """Custom type fsIsisMaxMAA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_FsIsisMaxMAA_Type.__name__ = "Integer32"
_FsIsisMaxMAA_Object = MibScalar
fsIsisMaxMAA = _FsIsisMaxMAA_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 1, 10),
    _FsIsisMaxMAA_Type()
)
fsIsisMaxMAA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisMaxMAA.setStatus("current")


class _FsIsisFTStatus_Type(Integer32):
    """Custom type fsIsisFTStatus based on Integer32"""
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


_FsIsisFTStatus_Type.__name__ = "Integer32"
_FsIsisFTStatus_Object = MibScalar
fsIsisFTStatus = _FsIsisFTStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 1, 11),
    _FsIsisFTStatus_Type()
)
fsIsisFTStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisFTStatus.setStatus("current")


class _FsIsisFTState_Type(Integer32):
    """Custom type fsIsisFTState based on Integer32"""
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
        *(("ftEnable", 1),
          ("ftDisable", 2),
          ("ftOOS", 3),
          ("ftStandBy", 4),
          ("ftActive", 5),
          ("ftLSUEnable", 6),
          ("ftLSUDisable", 7))
    )


_FsIsisFTState_Type.__name__ = "Integer32"
_FsIsisFTState_Object = MibScalar
fsIsisFTState = _FsIsisFTState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 1, 12),
    _FsIsisFTState_Type()
)
fsIsisFTState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIsisFTState.setStatus("current")


class _FsIsisFactor_Type(Integer32):
    """Custom type fsIsisFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FsIsisFactor_Type.__name__ = "Integer32"
_FsIsisFactor_Object = MibScalar
fsIsisFactor = _FsIsisFactor_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 1, 13),
    _FsIsisFactor_Type()
)
fsIsisFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisFactor.setStatus("current")


class _FsIsisMaxRoutes_Type(Integer32):
    """Custom type fsIsisMaxRoutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000),
    )


_FsIsisMaxRoutes_Type.__name__ = "Integer32"
_FsIsisMaxRoutes_Object = MibScalar
fsIsisMaxRoutes = _FsIsisMaxRoutes_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 1, 14),
    _FsIsisMaxRoutes_Type()
)
fsIsisMaxRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisMaxRoutes.setStatus("current")


class _FsIsisRestartState_Type(Integer32):
    """Custom type fsIsisRestartState based on Integer32"""
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
        *(("running", 1),
          ("reStarting", 2),
          ("starting", 3),
          ("adjSeenRA", 4),
          ("adjSeenCsnp", 5),
          ("spfWait", 6),
          ("spfDone", 7),
          ("overloadBitSet", 8))
    )


_FsIsisRestartState_Type.__name__ = "Integer32"
_FsIsisRestartState_Object = MibScalar
fsIsisRestartState = _FsIsisRestartState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 1, 15),
    _FsIsisRestartState_Type()
)
fsIsisRestartState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIsisRestartState.setStatus("current")
_FsIsisExt_ObjectIdentity = ObjectIdentity
fsIsisExt = _FsIsisExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2)
)
_FsIsisExtSystem_ObjectIdentity = ObjectIdentity
fsIsisExtSystem = _FsIsisExtSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1)
)
if mibBuilder.loadTexts:
    fsIsisExtSystem.setStatus("current")
_FsIsisExtSysTable_Object = MibTable
fsIsisExtSysTable = _FsIsisExtSysTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fsIsisExtSysTable.setStatus("current")
_FsIsisExtSysEntry_Object = MibTableRow
fsIsisExtSysEntry = _FsIsisExtSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1)
)
fsIsisExtSysEntry.setIndexNames(
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtSysInstance"),
)
if mibBuilder.loadTexts:
    fsIsisExtSysEntry.setStatus("current")


class _FsIsisExtSysInstance_Type(Integer32):
    """Custom type fsIsisExtSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_FsIsisExtSysInstance_Type.__name__ = "Integer32"
_FsIsisExtSysInstance_Object = MibTableColumn
fsIsisExtSysInstance = _FsIsisExtSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 1),
    _FsIsisExtSysInstance_Type()
)
fsIsisExtSysInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIsisExtSysInstance.setStatus("current")


class _FsIsisExtSysAuthSupp_Type(Integer32):
    """Custom type fsIsisExtSysAuthSupp based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("txRxDisable", 4),
          ("txEnable", 5),
          ("rxEnable", 6),
          ("txRxEnable", 7))
    )


_FsIsisExtSysAuthSupp_Type.__name__ = "Integer32"
_FsIsisExtSysAuthSupp_Object = MibTableColumn
fsIsisExtSysAuthSupp = _FsIsisExtSysAuthSupp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 2),
    _FsIsisExtSysAuthSupp_Type()
)
fsIsisExtSysAuthSupp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIsisExtSysAuthSupp.setStatus("current")


class _FsIsisExtSysAreaAuthType_Type(Integer32):
    """Custom type fsIsisExtSysAreaAuthType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("passwdAuth", 1)
    )


_FsIsisExtSysAreaAuthType_Type.__name__ = "Integer32"
_FsIsisExtSysAreaAuthType_Object = MibTableColumn
fsIsisExtSysAreaAuthType = _FsIsisExtSysAreaAuthType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 3),
    _FsIsisExtSysAreaAuthType_Type()
)
fsIsisExtSysAreaAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtSysAreaAuthType.setStatus("current")


class _FsIsisExtSysDomainAuthType_Type(Integer32):
    """Custom type fsIsisExtSysDomainAuthType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("passwdAuth", 1)
    )


_FsIsisExtSysDomainAuthType_Type.__name__ = "Integer32"
_FsIsisExtSysDomainAuthType_Object = MibTableColumn
fsIsisExtSysDomainAuthType = _FsIsisExtSysDomainAuthType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 4),
    _FsIsisExtSysDomainAuthType_Type()
)
fsIsisExtSysDomainAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtSysDomainAuthType.setStatus("current")


class _FsIsisExtSysAreaTxPasswd_Type(OctetString):
    """Custom type fsIsisExtSysAreaTxPasswd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FsIsisExtSysAreaTxPasswd_Type.__name__ = "OctetString"
_FsIsisExtSysAreaTxPasswd_Object = MibTableColumn
fsIsisExtSysAreaTxPasswd = _FsIsisExtSysAreaTxPasswd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 5),
    _FsIsisExtSysAreaTxPasswd_Type()
)
fsIsisExtSysAreaTxPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtSysAreaTxPasswd.setStatus("current")


class _FsIsisExtSysDomainTxPasswd_Type(OctetString):
    """Custom type fsIsisExtSysDomainTxPasswd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FsIsisExtSysDomainTxPasswd_Type.__name__ = "OctetString"
_FsIsisExtSysDomainTxPasswd_Object = MibTableColumn
fsIsisExtSysDomainTxPasswd = _FsIsisExtSysDomainTxPasswd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 6),
    _FsIsisExtSysDomainTxPasswd_Type()
)
fsIsisExtSysDomainTxPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtSysDomainTxPasswd.setStatus("current")


class _FsIsisExtSysMinSPFSchTime_Type(Integer32):
    """Custom type fsIsisExtSysMinSPFSchTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FsIsisExtSysMinSPFSchTime_Type.__name__ = "Integer32"
_FsIsisExtSysMinSPFSchTime_Object = MibTableColumn
fsIsisExtSysMinSPFSchTime = _FsIsisExtSysMinSPFSchTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 7),
    _FsIsisExtSysMinSPFSchTime_Type()
)
fsIsisExtSysMinSPFSchTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtSysMinSPFSchTime.setStatus("current")


class _FsIsisExtSysMaxSPFSchTime_Type(Integer32):
    """Custom type fsIsisExtSysMaxSPFSchTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_FsIsisExtSysMaxSPFSchTime_Type.__name__ = "Integer32"
_FsIsisExtSysMaxSPFSchTime_Object = MibTableColumn
fsIsisExtSysMaxSPFSchTime = _FsIsisExtSysMaxSPFSchTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 8),
    _FsIsisExtSysMaxSPFSchTime_Type()
)
fsIsisExtSysMaxSPFSchTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtSysMaxSPFSchTime.setStatus("current")


class _FsIsisExtSysMinLSPMark_Type(Integer32):
    """Custom type fsIsisExtSysMinLSPMark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FsIsisExtSysMinLSPMark_Type.__name__ = "Integer32"
_FsIsisExtSysMinLSPMark_Object = MibTableColumn
fsIsisExtSysMinLSPMark = _FsIsisExtSysMinLSPMark_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 9),
    _FsIsisExtSysMinLSPMark_Type()
)
fsIsisExtSysMinLSPMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtSysMinLSPMark.setStatus("current")


class _FsIsisExtSysMaxLSPMark_Type(Integer32):
    """Custom type fsIsisExtSysMaxLSPMark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_FsIsisExtSysMaxLSPMark_Type.__name__ = "Integer32"
_FsIsisExtSysMaxLSPMark_Object = MibTableColumn
fsIsisExtSysMaxLSPMark = _FsIsisExtSysMaxLSPMark_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 10),
    _FsIsisExtSysMaxLSPMark_Type()
)
fsIsisExtSysMaxLSPMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtSysMaxLSPMark.setStatus("current")
_FsIsisExtSysDelMetSupp_Type = TruthValue
_FsIsisExtSysDelMetSupp_Object = MibTableColumn
fsIsisExtSysDelMetSupp = _FsIsisExtSysDelMetSupp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 11),
    _FsIsisExtSysDelMetSupp_Type()
)
fsIsisExtSysDelMetSupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtSysDelMetSupp.setStatus("current")
_FsIsisExtSysErrMetSupp_Type = TruthValue
_FsIsisExtSysErrMetSupp_Object = MibTableColumn
fsIsisExtSysErrMetSupp = _FsIsisExtSysErrMetSupp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 12),
    _FsIsisExtSysErrMetSupp_Type()
)
fsIsisExtSysErrMetSupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtSysErrMetSupp.setStatus("current")
_FsIsisExtSysExpMetSupp_Type = TruthValue
_FsIsisExtSysExpMetSupp_Object = MibTableColumn
fsIsisExtSysExpMetSupp = _FsIsisExtSysExpMetSupp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 13),
    _FsIsisExtSysExpMetSupp_Type()
)
fsIsisExtSysExpMetSupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtSysExpMetSupp.setStatus("current")
_FsIsisExtSysActSysType_Type = Integer32
_FsIsisExtSysActSysType_Object = MibTableColumn
fsIsisExtSysActSysType = _FsIsisExtSysActSysType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 14),
    _FsIsisExtSysActSysType_Type()
)
fsIsisExtSysActSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIsisExtSysActSysType.setStatus("current")
_FsIsisExtSysActMPS_Type = Integer32
_FsIsisExtSysActMPS_Object = MibTableColumn
fsIsisExtSysActMPS = _FsIsisExtSysActMPS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 15),
    _FsIsisExtSysActMPS_Type()
)
fsIsisExtSysActMPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIsisExtSysActMPS.setStatus("current")
_FsIsisExtSysActMaxAA_Type = Integer32
_FsIsisExtSysActMaxAA_Object = MibTableColumn
fsIsisExtSysActMaxAA = _FsIsisExtSysActMaxAA_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 16),
    _FsIsisExtSysActMaxAA_Type()
)
fsIsisExtSysActMaxAA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIsisExtSysActMaxAA.setStatus("current")
_FsIsisExtSysActSysIDLen_Type = Integer32
_FsIsisExtSysActSysIDLen_Object = MibTableColumn
fsIsisExtSysActSysIDLen = _FsIsisExtSysActSysIDLen_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 17),
    _FsIsisExtSysActSysIDLen_Type()
)
fsIsisExtSysActSysIDLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIsisExtSysActSysIDLen.setStatus("current")
_FsIsisExtSysActSysID_Type = OctetString
_FsIsisExtSysActSysID_Object = MibTableColumn
fsIsisExtSysActSysID = _FsIsisExtSysActSysID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 18),
    _FsIsisExtSysActSysID_Type()
)
fsIsisExtSysActSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIsisExtSysActSysID.setStatus("current")
_FsIsisExtSysActOrigL1LSPBufSize_Type = Integer32
_FsIsisExtSysActOrigL1LSPBufSize_Object = MibTableColumn
fsIsisExtSysActOrigL1LSPBufSize = _FsIsisExtSysActOrigL1LSPBufSize_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 19),
    _FsIsisExtSysActOrigL1LSPBufSize_Type()
)
fsIsisExtSysActOrigL1LSPBufSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIsisExtSysActOrigL1LSPBufSize.setStatus("current")
_FsIsisExtSysActOrigL2LSPBufSize_Type = Integer32
_FsIsisExtSysActOrigL2LSPBufSize_Object = MibTableColumn
fsIsisExtSysActOrigL2LSPBufSize = _FsIsisExtSysActOrigL2LSPBufSize_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 20),
    _FsIsisExtSysActOrigL2LSPBufSize_Type()
)
fsIsisExtSysActOrigL2LSPBufSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIsisExtSysActOrigL2LSPBufSize.setStatus("current")
_FsIsisExtSysRouterID_Type = OctetString
_FsIsisExtSysRouterID_Object = MibTableColumn
fsIsisExtSysRouterID = _FsIsisExtSysRouterID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 21),
    _FsIsisExtSysRouterID_Type()
)
fsIsisExtSysRouterID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtSysRouterID.setStatus("current")
_FsIsisExtSysCkts_Type = Integer32
_FsIsisExtSysCkts_Object = MibTableColumn
fsIsisExtSysCkts = _FsIsisExtSysCkts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 22),
    _FsIsisExtSysCkts_Type()
)
fsIsisExtSysCkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIsisExtSysCkts.setStatus("current")
_FsIsisExtSysActiveCkts_Type = Integer32
_FsIsisExtSysActiveCkts_Object = MibTableColumn
fsIsisExtSysActiveCkts = _FsIsisExtSysActiveCkts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 23),
    _FsIsisExtSysActiveCkts_Type()
)
fsIsisExtSysActiveCkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIsisExtSysActiveCkts.setStatus("current")
_FsIsisExtSysAdjs_Type = Integer32
_FsIsisExtSysAdjs_Object = MibTableColumn
fsIsisExtSysAdjs = _FsIsisExtSysAdjs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 24),
    _FsIsisExtSysAdjs_Type()
)
fsIsisExtSysAdjs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIsisExtSysAdjs.setStatus("current")
_FsIsisExtSysOperState_Type = Integer32
_FsIsisExtSysOperState_Object = MibTableColumn
fsIsisExtSysOperState = _FsIsisExtSysOperState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 25),
    _FsIsisExtSysOperState_Type()
)
fsIsisExtSysOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIsisExtSysOperState.setStatus("current")
_FsIsisExtSysDroppedPDUs_Type = Integer32
_FsIsisExtSysDroppedPDUs_Object = MibTableColumn
fsIsisExtSysDroppedPDUs = _FsIsisExtSysDroppedPDUs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 26),
    _FsIsisExtSysDroppedPDUs_Type()
)
fsIsisExtSysDroppedPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIsisExtSysDroppedPDUs.setStatus("current")


class _FsIsisExtRestartSupport_Type(Integer32):
    """Custom type fsIsisExtRestartSupport based on Integer32"""
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
          ("plannedOnly", 2),
          ("plannedAndUnplanned", 3))
    )


_FsIsisExtRestartSupport_Type.__name__ = "Integer32"
_FsIsisExtRestartSupport_Object = MibTableColumn
fsIsisExtRestartSupport = _FsIsisExtRestartSupport_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 27),
    _FsIsisExtRestartSupport_Type()
)
fsIsisExtRestartSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtRestartSupport.setStatus("current")


class _FsIsisExtGRRestartTimeInterval_Type(Integer32):
    """Custom type fsIsisExtGRRestartTimeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsIsisExtGRRestartTimeInterval_Type.__name__ = "Integer32"
_FsIsisExtGRRestartTimeInterval_Object = MibTableColumn
fsIsisExtGRRestartTimeInterval = _FsIsisExtGRRestartTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 28),
    _FsIsisExtGRRestartTimeInterval_Type()
)
fsIsisExtGRRestartTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtGRRestartTimeInterval.setStatus("current")


class _FsIsisExtGRT2TimeIntervalLevel1_Type(Integer32):
    """Custom type fsIsisExtGRT2TimeIntervalLevel1 based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_FsIsisExtGRT2TimeIntervalLevel1_Type.__name__ = "Integer32"
_FsIsisExtGRT2TimeIntervalLevel1_Object = MibTableColumn
fsIsisExtGRT2TimeIntervalLevel1 = _FsIsisExtGRT2TimeIntervalLevel1_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 29),
    _FsIsisExtGRT2TimeIntervalLevel1_Type()
)
fsIsisExtGRT2TimeIntervalLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtGRT2TimeIntervalLevel1.setStatus("current")


class _FsIsisExtGRT2TimeIntervalLevel2_Type(Integer32):
    """Custom type fsIsisExtGRT2TimeIntervalLevel2 based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_FsIsisExtGRT2TimeIntervalLevel2_Type.__name__ = "Integer32"
_FsIsisExtGRT2TimeIntervalLevel2_Object = MibTableColumn
fsIsisExtGRT2TimeIntervalLevel2 = _FsIsisExtGRT2TimeIntervalLevel2_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 30),
    _FsIsisExtGRT2TimeIntervalLevel2_Type()
)
fsIsisExtGRT2TimeIntervalLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtGRT2TimeIntervalLevel2.setStatus("current")


class _FsIsisExtGRT1TimeInterval_Type(Integer32):
    """Custom type fsIsisExtGRT1TimeInterval based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_FsIsisExtGRT1TimeInterval_Type.__name__ = "Integer32"
_FsIsisExtGRT1TimeInterval_Object = MibTableColumn
fsIsisExtGRT1TimeInterval = _FsIsisExtGRT1TimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 31),
    _FsIsisExtGRT1TimeInterval_Type()
)
fsIsisExtGRT1TimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtGRT1TimeInterval.setStatus("current")


class _FsIsisExtGRT1RetryCount_Type(Integer32):
    """Custom type fsIsisExtGRT1RetryCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_FsIsisExtGRT1RetryCount_Type.__name__ = "Integer32"
_FsIsisExtGRT1RetryCount_Object = MibTableColumn
fsIsisExtGRT1RetryCount = _FsIsisExtGRT1RetryCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 32),
    _FsIsisExtGRT1RetryCount_Type()
)
fsIsisExtGRT1RetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtGRT1RetryCount.setStatus("current")


class _FsIsisExtGRMode_Type(Integer32):
    """Custom type fsIsisExtGRMode based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("restarter", 2),
          ("helper", 3),
          ("helperdown", 4))
    )


_FsIsisExtGRMode_Type.__name__ = "Integer32"
_FsIsisExtGRMode_Object = MibTableColumn
fsIsisExtGRMode = _FsIsisExtGRMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 33),
    _FsIsisExtGRMode_Type()
)
fsIsisExtGRMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIsisExtGRMode.setStatus("current")


class _FsIsisExtRestartStatus_Type(Integer32):
    """Custom type fsIsisExtRestartStatus based on Integer32"""
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
          ("plannedRestart", 2),
          ("unplannedRestart", 3))
    )


_FsIsisExtRestartStatus_Type.__name__ = "Integer32"
_FsIsisExtRestartStatus_Object = MibTableColumn
fsIsisExtRestartStatus = _FsIsisExtRestartStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 34),
    _FsIsisExtRestartStatus_Type()
)
fsIsisExtRestartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIsisExtRestartStatus.setStatus("current")


class _FsIsisExtRestartExitReason_Type(Integer32):
    """Custom type fsIsisExtRestartExitReason based on Integer32"""
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
        *(("none", 1),
          ("inProgress", 2),
          ("completed", 3),
          ("timedOut", 4),
          ("topologyChanged", 5))
    )


_FsIsisExtRestartExitReason_Type.__name__ = "Integer32"
_FsIsisExtRestartExitReason_Object = MibTableColumn
fsIsisExtRestartExitReason = _FsIsisExtRestartExitReason_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 35),
    _FsIsisExtRestartExitReason_Type()
)
fsIsisExtRestartExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIsisExtRestartExitReason.setStatus("current")


class _FsIsisExtRestartReason_Type(Integer32):
    """Custom type fsIsisExtRestartReason based on Integer32"""
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
        *(("unknown", 1),
          ("softwareRestart", 2),
          ("swReloadUpgrade", 3),
          ("switchToRedundant", 4))
    )


_FsIsisExtRestartReason_Type.__name__ = "Integer32"
_FsIsisExtRestartReason_Object = MibTableColumn
fsIsisExtRestartReason = _FsIsisExtRestartReason_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 36),
    _FsIsisExtRestartReason_Type()
)
fsIsisExtRestartReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtRestartReason.setStatus("current")


class _FsIsisExtHelperSupport_Type(Integer32):
    """Custom type fsIsisExtHelperSupport based on Integer32"""
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
          ("restart", 2),
          ("bothRestartAndStart", 3))
    )


_FsIsisExtHelperSupport_Type.__name__ = "Integer32"
_FsIsisExtHelperSupport_Object = MibTableColumn
fsIsisExtHelperSupport = _FsIsisExtHelperSupport_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 37),
    _FsIsisExtHelperSupport_Type()
)
fsIsisExtHelperSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtHelperSupport.setStatus("current")


class _FsIsisExtHelperGraceTimeLimit_Type(Integer32):
    """Custom type fsIsisExtHelperGraceTimeLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(180, 65535),
    )


_FsIsisExtHelperGraceTimeLimit_Type.__name__ = "Integer32"
_FsIsisExtHelperGraceTimeLimit_Object = MibTableColumn
fsIsisExtHelperGraceTimeLimit = _FsIsisExtHelperGraceTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 1, 1, 38),
    _FsIsisExtHelperGraceTimeLimit_Type()
)
fsIsisExtHelperGraceTimeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtHelperGraceTimeLimit.setStatus("current")
_FsIsisExtSysAreaRxPasswdTable_Object = MibTable
fsIsisExtSysAreaRxPasswdTable = _FsIsisExtSysAreaRxPasswdTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 2)
)
if mibBuilder.loadTexts:
    fsIsisExtSysAreaRxPasswdTable.setStatus("current")
_FsIsisExtSysAreaRxPasswdEntry_Object = MibTableRow
fsIsisExtSysAreaRxPasswdEntry = _FsIsisExtSysAreaRxPasswdEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 2, 1)
)
fsIsisExtSysAreaRxPasswdEntry.setIndexNames(
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtSysInstance"),
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtSysAreaRxPasswd"),
)
if mibBuilder.loadTexts:
    fsIsisExtSysAreaRxPasswdEntry.setStatus("current")


class _FsIsisExtSysAreaRxPasswd_Type(OctetString):
    """Custom type fsIsisExtSysAreaRxPasswd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FsIsisExtSysAreaRxPasswd_Type.__name__ = "OctetString"
_FsIsisExtSysAreaRxPasswd_Object = MibTableColumn
fsIsisExtSysAreaRxPasswd = _FsIsisExtSysAreaRxPasswd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 2, 1, 1),
    _FsIsisExtSysAreaRxPasswd_Type()
)
fsIsisExtSysAreaRxPasswd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIsisExtSysAreaRxPasswd.setStatus("current")
_FsIsisExtSysAreaRxPasswdExistState_Type = RowStatus
_FsIsisExtSysAreaRxPasswdExistState_Object = MibTableColumn
fsIsisExtSysAreaRxPasswdExistState = _FsIsisExtSysAreaRxPasswdExistState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 2, 1, 2),
    _FsIsisExtSysAreaRxPasswdExistState_Type()
)
fsIsisExtSysAreaRxPasswdExistState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtSysAreaRxPasswdExistState.setStatus("current")
_FsIsisExtSysDomainRxPasswdTable_Object = MibTable
fsIsisExtSysDomainRxPasswdTable = _FsIsisExtSysDomainRxPasswdTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 3)
)
if mibBuilder.loadTexts:
    fsIsisExtSysDomainRxPasswdTable.setStatus("current")
_FsIsisExtSysDomainRxPasswdEntry_Object = MibTableRow
fsIsisExtSysDomainRxPasswdEntry = _FsIsisExtSysDomainRxPasswdEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 3, 1)
)
fsIsisExtSysDomainRxPasswdEntry.setIndexNames(
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtSysInstance"),
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtSysDomainRxPassword"),
)
if mibBuilder.loadTexts:
    fsIsisExtSysDomainRxPasswdEntry.setStatus("current")


class _FsIsisExtSysDomainRxPassword_Type(OctetString):
    """Custom type fsIsisExtSysDomainRxPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FsIsisExtSysDomainRxPassword_Type.__name__ = "OctetString"
_FsIsisExtSysDomainRxPassword_Object = MibTableColumn
fsIsisExtSysDomainRxPassword = _FsIsisExtSysDomainRxPassword_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 3, 1, 1),
    _FsIsisExtSysDomainRxPassword_Type()
)
fsIsisExtSysDomainRxPassword.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIsisExtSysDomainRxPassword.setStatus("current")
_FsIsisExtSysDomainRxPasswdExistState_Type = RowStatus
_FsIsisExtSysDomainRxPasswdExistState_Object = MibTableColumn
fsIsisExtSysDomainRxPasswdExistState = _FsIsisExtSysDomainRxPasswdExistState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 3, 1, 2),
    _FsIsisExtSysDomainRxPasswdExistState_Type()
)
fsIsisExtSysDomainRxPasswdExistState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtSysDomainRxPasswdExistState.setStatus("current")
_FsIsisExtSysEventTable_Object = MibTable
fsIsisExtSysEventTable = _FsIsisExtSysEventTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 4)
)
if mibBuilder.loadTexts:
    fsIsisExtSysEventTable.setStatus("current")
_FsIsisExtSysEventEntry_Object = MibTableRow
fsIsisExtSysEventEntry = _FsIsisExtSysEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 4, 1)
)
fsIsisExtSysEventEntry.setIndexNames(
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtSysInstance"),
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtSysEventIdx"),
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtSysEvent"),
)
if mibBuilder.loadTexts:
    fsIsisExtSysEventEntry.setStatus("current")


class _FsIsisExtSysEventIdx_Type(Integer32):
    """Custom type fsIsisExtSysEventIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_FsIsisExtSysEventIdx_Type.__name__ = "Integer32"
_FsIsisExtSysEventIdx_Object = MibTableColumn
fsIsisExtSysEventIdx = _FsIsisExtSysEventIdx_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 4, 1, 1),
    _FsIsisExtSysEventIdx_Type()
)
fsIsisExtSysEventIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIsisExtSysEventIdx.setStatus("current")


class _FsIsisExtSysEvent_Type(Integer32):
    """Custom type fsIsisExtSysEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_FsIsisExtSysEvent_Type.__name__ = "Integer32"
_FsIsisExtSysEvent_Object = MibTableColumn
fsIsisExtSysEvent = _FsIsisExtSysEvent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 4, 1, 2),
    _FsIsisExtSysEvent_Type()
)
fsIsisExtSysEvent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIsisExtSysEvent.setStatus("current")
_FsIsisExtSysEventStr_Type = DisplayString
_FsIsisExtSysEventStr_Object = MibTableColumn
fsIsisExtSysEventStr = _FsIsisExtSysEventStr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 1, 4, 1, 3),
    _FsIsisExtSysEventStr_Type()
)
fsIsisExtSysEventStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIsisExtSysEventStr.setStatus("current")
_FsIsisExtCirc_ObjectIdentity = ObjectIdentity
fsIsisExtCirc = _FsIsisExtCirc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2)
)
if mibBuilder.loadTexts:
    fsIsisExtCirc.setStatus("current")
_FsIsisExtCircTable_Object = MibTable
fsIsisExtCircTable = _FsIsisExtCircTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fsIsisExtCircTable.setStatus("current")
_FsIsisExtCircEntry_Object = MibTableRow
fsIsisExtCircEntry = _FsIsisExtCircEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 1, 1)
)
fsIsisExtCircEntry.setIndexNames(
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtSysInstance"),
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtCircIndex"),
)
if mibBuilder.loadTexts:
    fsIsisExtCircEntry.setStatus("current")


class _FsIsisExtCircIndex_Type(Integer32):
    """Custom type fsIsisExtCircIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_FsIsisExtCircIndex_Type.__name__ = "Integer32"
_FsIsisExtCircIndex_Object = MibTableColumn
fsIsisExtCircIndex = _FsIsisExtCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 1, 1, 1),
    _FsIsisExtCircIndex_Type()
)
fsIsisExtCircIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIsisExtCircIndex.setStatus("current")


class _FsIsisExtCircIfStatus_Type(Integer32):
    """Custom type fsIsisExtCircIfStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FsIsisExtCircIfStatus_Type.__name__ = "Integer32"
_FsIsisExtCircIfStatus_Object = MibTableColumn
fsIsisExtCircIfStatus = _FsIsisExtCircIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 1, 1, 2),
    _FsIsisExtCircIfStatus_Type()
)
fsIsisExtCircIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIsisExtCircIfStatus.setStatus("current")


class _FsIsisExtCircTxEnable_Type(TruthValue):
    """Custom type fsIsisExtCircTxEnable based on TruthValue"""
    defaultValue = 1


_FsIsisExtCircTxEnable_Type.__name__ = "TruthValue"
_FsIsisExtCircTxEnable_Object = MibTableColumn
fsIsisExtCircTxEnable = _FsIsisExtCircTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 1, 1, 3),
    _FsIsisExtCircTxEnable_Type()
)
fsIsisExtCircTxEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIsisExtCircTxEnable.setStatus("current")


class _FsIsisExtCircRxEnable_Type(TruthValue):
    """Custom type fsIsisExtCircRxEnable based on TruthValue"""
    defaultValue = 1


_FsIsisExtCircRxEnable_Type.__name__ = "TruthValue"
_FsIsisExtCircRxEnable_Object = MibTableColumn
fsIsisExtCircRxEnable = _FsIsisExtCircRxEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 1, 1, 4),
    _FsIsisExtCircRxEnable_Type()
)
fsIsisExtCircRxEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIsisExtCircRxEnable.setStatus("current")


class _FsIsisExtCircTxISHs_Type(Integer32):
    """Custom type fsIsisExtCircTxISHs based on Integer32"""
    defaultValue = 0


_FsIsisExtCircTxISHs_Type.__name__ = "Integer32"
_FsIsisExtCircTxISHs_Object = MibTableColumn
fsIsisExtCircTxISHs = _FsIsisExtCircTxISHs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 1, 1, 5),
    _FsIsisExtCircTxISHs_Type()
)
fsIsisExtCircTxISHs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIsisExtCircTxISHs.setStatus("current")


class _FsIsisExtCircRxISHs_Type(Integer32):
    """Custom type fsIsisExtCircRxISHs based on Integer32"""
    defaultValue = 0


_FsIsisExtCircRxISHs_Type.__name__ = "Integer32"
_FsIsisExtCircRxISHs_Object = MibTableColumn
fsIsisExtCircRxISHs = _FsIsisExtCircRxISHs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 1, 1, 6),
    _FsIsisExtCircRxISHs_Type()
)
fsIsisExtCircRxISHs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIsisExtCircRxISHs.setStatus("current")


class _FsIsisExtCircSNPA_Type(OctetString):
    """Custom type fsIsisExtCircSNPA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_FsIsisExtCircSNPA_Type.__name__ = "OctetString"
_FsIsisExtCircSNPA_Object = MibTableColumn
fsIsisExtCircSNPA = _FsIsisExtCircSNPA_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 1, 1, 7),
    _FsIsisExtCircSNPA_Type()
)
fsIsisExtCircSNPA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIsisExtCircSNPA.setStatus("current")
_FsIsisExtCircLevelTable_Object = MibTable
fsIsisExtCircLevelTable = _FsIsisExtCircLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 2)
)
if mibBuilder.loadTexts:
    fsIsisExtCircLevelTable.setStatus("current")
_FsIsisExtCircLevelEntry_Object = MibTableRow
fsIsisExtCircLevelEntry = _FsIsisExtCircLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 2, 1)
)
fsIsisExtCircLevelEntry.setIndexNames(
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtSysInstance"),
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtCircIndex"),
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtCircLevelIndex"),
)
if mibBuilder.loadTexts:
    fsIsisExtCircLevelEntry.setStatus("current")


class _FsIsisExtCircLevelIndex_Type(Integer32):
    """Custom type fsIsisExtCircLevelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1IS", 1),
          ("level2IS", 2))
    )


_FsIsisExtCircLevelIndex_Type.__name__ = "Integer32"
_FsIsisExtCircLevelIndex_Object = MibTableColumn
fsIsisExtCircLevelIndex = _FsIsisExtCircLevelIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 2, 1, 1),
    _FsIsisExtCircLevelIndex_Type()
)
fsIsisExtCircLevelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIsisExtCircLevelIndex.setStatus("current")


class _FsIsisExtCircLevelDelayMetric_Type(Integer32):
    """Custom type fsIsisExtCircLevelDelayMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_FsIsisExtCircLevelDelayMetric_Type.__name__ = "Integer32"
_FsIsisExtCircLevelDelayMetric_Object = MibTableColumn
fsIsisExtCircLevelDelayMetric = _FsIsisExtCircLevelDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 2, 1, 2),
    _FsIsisExtCircLevelDelayMetric_Type()
)
fsIsisExtCircLevelDelayMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIsisExtCircLevelDelayMetric.setStatus("current")


class _FsIsisExtCircLevelErrorMetric_Type(Integer32):
    """Custom type fsIsisExtCircLevelErrorMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_FsIsisExtCircLevelErrorMetric_Type.__name__ = "Integer32"
_FsIsisExtCircLevelErrorMetric_Object = MibTableColumn
fsIsisExtCircLevelErrorMetric = _FsIsisExtCircLevelErrorMetric_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 2, 1, 3),
    _FsIsisExtCircLevelErrorMetric_Type()
)
fsIsisExtCircLevelErrorMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIsisExtCircLevelErrorMetric.setStatus("current")


class _FsIsisExtCircLevelExpenseMetric_Type(Integer32):
    """Custom type fsIsisExtCircLevelExpenseMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_FsIsisExtCircLevelExpenseMetric_Type.__name__ = "Integer32"
_FsIsisExtCircLevelExpenseMetric_Object = MibTableColumn
fsIsisExtCircLevelExpenseMetric = _FsIsisExtCircLevelExpenseMetric_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 2, 1, 4),
    _FsIsisExtCircLevelExpenseMetric_Type()
)
fsIsisExtCircLevelExpenseMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIsisExtCircLevelExpenseMetric.setStatus("current")


class _FsIsisExtCircLevelTxPassword_Type(OctetString):
    """Custom type fsIsisExtCircLevelTxPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FsIsisExtCircLevelTxPassword_Type.__name__ = "OctetString"
_FsIsisExtCircLevelTxPassword_Object = MibTableColumn
fsIsisExtCircLevelTxPassword = _FsIsisExtCircLevelTxPassword_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 2, 1, 5),
    _FsIsisExtCircLevelTxPassword_Type()
)
fsIsisExtCircLevelTxPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtCircLevelTxPassword.setStatus("current")
_FsIsisExtIPRATable_Object = MibTable
fsIsisExtIPRATable = _FsIsisExtIPRATable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 3)
)
if mibBuilder.loadTexts:
    fsIsisExtIPRATable.setStatus("current")
_FsIsisExtIPRAEntry_Object = MibTableRow
fsIsisExtIPRAEntry = _FsIsisExtIPRAEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 3, 1)
)
fsIsisExtIPRAEntry.setIndexNames(
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtSysInstance"),
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtIPRAType"),
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtIPRAIndex"),
)
if mibBuilder.loadTexts:
    fsIsisExtIPRAEntry.setStatus("current")


class _FsIsisExtIPRAType_Type(Integer32):
    """Custom type fsIsisExtIPRAType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("automatic", 2))
    )


_FsIsisExtIPRAType_Type.__name__ = "Integer32"
_FsIsisExtIPRAType_Object = MibTableColumn
fsIsisExtIPRAType = _FsIsisExtIPRAType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 3, 1, 1),
    _FsIsisExtIPRAType_Type()
)
fsIsisExtIPRAType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIsisExtIPRAType.setStatus("current")


class _FsIsisExtIPRAIndex_Type(Integer32):
    """Custom type fsIsisExtIPRAIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_FsIsisExtIPRAIndex_Type.__name__ = "Integer32"
_FsIsisExtIPRAIndex_Object = MibTableColumn
fsIsisExtIPRAIndex = _FsIsisExtIPRAIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 3, 1, 2),
    _FsIsisExtIPRAIndex_Type()
)
fsIsisExtIPRAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIsisExtIPRAIndex.setStatus("current")


class _FsIsisExtIPRADelayMetric_Type(Integer32):
    """Custom type fsIsisExtIPRADelayMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_FsIsisExtIPRADelayMetric_Type.__name__ = "Integer32"
_FsIsisExtIPRADelayMetric_Object = MibTableColumn
fsIsisExtIPRADelayMetric = _FsIsisExtIPRADelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 3, 1, 3),
    _FsIsisExtIPRADelayMetric_Type()
)
fsIsisExtIPRADelayMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIsisExtIPRADelayMetric.setStatus("current")


class _FsIsisExtIPRAErrorMetric_Type(Integer32):
    """Custom type fsIsisExtIPRAErrorMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_FsIsisExtIPRAErrorMetric_Type.__name__ = "Integer32"
_FsIsisExtIPRAErrorMetric_Object = MibTableColumn
fsIsisExtIPRAErrorMetric = _FsIsisExtIPRAErrorMetric_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 3, 1, 4),
    _FsIsisExtIPRAErrorMetric_Type()
)
fsIsisExtIPRAErrorMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIsisExtIPRAErrorMetric.setStatus("current")


class _FsIsisExtIPRAExpenseMetric_Type(Integer32):
    """Custom type fsIsisExtIPRAExpenseMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_FsIsisExtIPRAExpenseMetric_Type.__name__ = "Integer32"
_FsIsisExtIPRAExpenseMetric_Object = MibTableColumn
fsIsisExtIPRAExpenseMetric = _FsIsisExtIPRAExpenseMetric_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 3, 1, 5),
    _FsIsisExtIPRAExpenseMetric_Type()
)
fsIsisExtIPRAExpenseMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIsisExtIPRAExpenseMetric.setStatus("current")
_FsIsisExtIPRADelayMetricType_Type = MetricType
_FsIsisExtIPRADelayMetricType_Object = MibTableColumn
fsIsisExtIPRADelayMetricType = _FsIsisExtIPRADelayMetricType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 3, 1, 6),
    _FsIsisExtIPRADelayMetricType_Type()
)
fsIsisExtIPRADelayMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIsisExtIPRADelayMetricType.setStatus("current")
_FsIsisExtIPRAErrorMetricType_Type = MetricType
_FsIsisExtIPRAErrorMetricType_Object = MibTableColumn
fsIsisExtIPRAErrorMetricType = _FsIsisExtIPRAErrorMetricType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 3, 1, 7),
    _FsIsisExtIPRAErrorMetricType_Type()
)
fsIsisExtIPRAErrorMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIsisExtIPRAErrorMetricType.setStatus("current")
_FsIsisExtIPRAExpenseMetricType_Type = MetricType
_FsIsisExtIPRAExpenseMetricType_Object = MibTableColumn
fsIsisExtIPRAExpenseMetricType = _FsIsisExtIPRAExpenseMetricType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 3, 1, 8),
    _FsIsisExtIPRAExpenseMetricType_Type()
)
fsIsisExtIPRAExpenseMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIsisExtIPRAExpenseMetricType.setStatus("current")
_FsIsisExtIPRANextHopType_Type = InetAddressType
_FsIsisExtIPRANextHopType_Object = MibTableColumn
fsIsisExtIPRANextHopType = _FsIsisExtIPRANextHopType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 3, 1, 9),
    _FsIsisExtIPRANextHopType_Type()
)
fsIsisExtIPRANextHopType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIsisExtIPRANextHopType.setStatus("current")


class _FsIsisExtIPRANextHop_Type(InetAddress):
    """Custom type fsIsisExtIPRANextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_FsIsisExtIPRANextHop_Type.__name__ = "InetAddress"
_FsIsisExtIPRANextHop_Object = MibTableColumn
fsIsisExtIPRANextHop = _FsIsisExtIPRANextHop_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 3, 1, 10),
    _FsIsisExtIPRANextHop_Type()
)
fsIsisExtIPRANextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIsisExtIPRANextHop.setStatus("current")
_FsIsisExtCircLevelRxPasswordTable_Object = MibTable
fsIsisExtCircLevelRxPasswordTable = _FsIsisExtCircLevelRxPasswordTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 4)
)
if mibBuilder.loadTexts:
    fsIsisExtCircLevelRxPasswordTable.setStatus("current")
_FsIsisExtCircLevelRxPasswordEntry_Object = MibTableRow
fsIsisExtCircLevelRxPasswordEntry = _FsIsisExtCircLevelRxPasswordEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 4, 1)
)
fsIsisExtCircLevelRxPasswordEntry.setIndexNames(
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtSysInstance"),
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtCircIndex"),
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtCircLevelIndex"),
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtCircLevelRxPassword"),
)
if mibBuilder.loadTexts:
    fsIsisExtCircLevelRxPasswordEntry.setStatus("current")


class _FsIsisExtCircLevelRxPassword_Type(OctetString):
    """Custom type fsIsisExtCircLevelRxPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FsIsisExtCircLevelRxPassword_Type.__name__ = "OctetString"
_FsIsisExtCircLevelRxPassword_Object = MibTableColumn
fsIsisExtCircLevelRxPassword = _FsIsisExtCircLevelRxPassword_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 4, 1, 1),
    _FsIsisExtCircLevelRxPassword_Type()
)
fsIsisExtCircLevelRxPassword.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIsisExtCircLevelRxPassword.setStatus("current")
_FsIsisExtCircLevelRxPasswordExistState_Type = RowStatus
_FsIsisExtCircLevelRxPasswordExistState_Object = MibTableColumn
fsIsisExtCircLevelRxPasswordExistState = _FsIsisExtCircLevelRxPasswordExistState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 2, 4, 1, 2),
    _FsIsisExtCircLevelRxPasswordExistState_Type()
)
fsIsisExtCircLevelRxPasswordExistState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtCircLevelRxPasswordExistState.setStatus("current")
_FsIsisExtSummAddr_ObjectIdentity = ObjectIdentity
fsIsisExtSummAddr = _FsIsisExtSummAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 3)
)
if mibBuilder.loadTexts:
    fsIsisExtSummAddr.setStatus("current")
_FsIsisExtSummAddrTable_Object = MibTable
fsIsisExtSummAddrTable = _FsIsisExtSummAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 3, 1)
)
if mibBuilder.loadTexts:
    fsIsisExtSummAddrTable.setStatus("current")
_FsIsisExtSummAddrEntry_Object = MibTableRow
fsIsisExtSummAddrEntry = _FsIsisExtSummAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 3, 1, 1)
)
fsIsisExtSummAddrEntry.setIndexNames(
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtSysInstance"),
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtSummAddressType"),
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtSummAddress"),
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtSummAddrPrefixLen"),
)
if mibBuilder.loadTexts:
    fsIsisExtSummAddrEntry.setStatus("current")
_FsIsisExtSummAddressType_Type = InetAddressType
_FsIsisExtSummAddressType_Object = MibTableColumn
fsIsisExtSummAddressType = _FsIsisExtSummAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 3, 1, 1, 1),
    _FsIsisExtSummAddressType_Type()
)
fsIsisExtSummAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIsisExtSummAddressType.setStatus("current")


class _FsIsisExtSummAddress_Type(InetAddress):
    """Custom type fsIsisExtSummAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_FsIsisExtSummAddress_Type.__name__ = "InetAddress"
_FsIsisExtSummAddress_Object = MibTableColumn
fsIsisExtSummAddress = _FsIsisExtSummAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 3, 1, 1, 2),
    _FsIsisExtSummAddress_Type()
)
fsIsisExtSummAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIsisExtSummAddress.setStatus("current")


class _FsIsisExtSummAddrPrefixLen_Type(InetAddressPrefixLength):
    """Custom type fsIsisExtSummAddrPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FsIsisExtSummAddrPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_FsIsisExtSummAddrPrefixLen_Object = MibTableColumn
fsIsisExtSummAddrPrefixLen = _FsIsisExtSummAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 3, 1, 1, 3),
    _FsIsisExtSummAddrPrefixLen_Type()
)
fsIsisExtSummAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIsisExtSummAddrPrefixLen.setStatus("current")


class _FsIsisExtSummAddrDelayMetric_Type(Integer32):
    """Custom type fsIsisExtSummAddrDelayMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_FsIsisExtSummAddrDelayMetric_Type.__name__ = "Integer32"
_FsIsisExtSummAddrDelayMetric_Object = MibTableColumn
fsIsisExtSummAddrDelayMetric = _FsIsisExtSummAddrDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 3, 1, 1, 4),
    _FsIsisExtSummAddrDelayMetric_Type()
)
fsIsisExtSummAddrDelayMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtSummAddrDelayMetric.setStatus("current")


class _FsIsisExtSummAddrErrorMetric_Type(Integer32):
    """Custom type fsIsisExtSummAddrErrorMetric based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_FsIsisExtSummAddrErrorMetric_Type.__name__ = "Integer32"
_FsIsisExtSummAddrErrorMetric_Object = MibTableColumn
fsIsisExtSummAddrErrorMetric = _FsIsisExtSummAddrErrorMetric_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 3, 1, 1, 5),
    _FsIsisExtSummAddrErrorMetric_Type()
)
fsIsisExtSummAddrErrorMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtSummAddrErrorMetric.setStatus("current")


class _FsIsisExtSummAddrExpenseMetric_Type(Integer32):
    """Custom type fsIsisExtSummAddrExpenseMetric based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_FsIsisExtSummAddrExpenseMetric_Type.__name__ = "Integer32"
_FsIsisExtSummAddrExpenseMetric_Object = MibTableColumn
fsIsisExtSummAddrExpenseMetric = _FsIsisExtSummAddrExpenseMetric_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 3, 1, 1, 6),
    _FsIsisExtSummAddrExpenseMetric_Type()
)
fsIsisExtSummAddrExpenseMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtSummAddrExpenseMetric.setStatus("current")
_FsIsisExtIPIf_ObjectIdentity = ObjectIdentity
fsIsisExtIPIf = _FsIsisExtIPIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 4)
)
if mibBuilder.loadTexts:
    fsIsisExtIPIf.setStatus("current")
_FsIsisExtIPIfAddrTable_Object = MibTable
fsIsisExtIPIfAddrTable = _FsIsisExtIPIfAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 4, 1)
)
if mibBuilder.loadTexts:
    fsIsisExtIPIfAddrTable.setStatus("current")
_FsIsisExtIPIfAddrEntry_Object = MibTableRow
fsIsisExtIPIfAddrEntry = _FsIsisExtIPIfAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 4, 1, 1)
)
fsIsisExtIPIfAddrEntry.setIndexNames(
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtSysInstance"),
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtIPIfIndex"),
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtIPIfSubIndex"),
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtIPIfAddrType"),
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtIPIfAddr"),
)
if mibBuilder.loadTexts:
    fsIsisExtIPIfAddrEntry.setStatus("current")


class _FsIsisExtIPIfIndex_Type(Integer32):
    """Custom type fsIsisExtIPIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_FsIsisExtIPIfIndex_Type.__name__ = "Integer32"
_FsIsisExtIPIfIndex_Object = MibTableColumn
fsIsisExtIPIfIndex = _FsIsisExtIPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 4, 1, 1, 1),
    _FsIsisExtIPIfIndex_Type()
)
fsIsisExtIPIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIsisExtIPIfIndex.setStatus("current")


class _FsIsisExtIPIfSubIndex_Type(Integer32):
    """Custom type fsIsisExtIPIfSubIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_FsIsisExtIPIfSubIndex_Type.__name__ = "Integer32"
_FsIsisExtIPIfSubIndex_Object = MibTableColumn
fsIsisExtIPIfSubIndex = _FsIsisExtIPIfSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 4, 1, 1, 2),
    _FsIsisExtIPIfSubIndex_Type()
)
fsIsisExtIPIfSubIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIsisExtIPIfSubIndex.setStatus("current")


class _FsIsisExtIPIfAddrType_Type(Integer32):
    """Custom type fsIsisExtIPIfAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_FsIsisExtIPIfAddrType_Type.__name__ = "Integer32"
_FsIsisExtIPIfAddrType_Object = MibTableColumn
fsIsisExtIPIfAddrType = _FsIsisExtIPIfAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 4, 1, 1, 3),
    _FsIsisExtIPIfAddrType_Type()
)
fsIsisExtIPIfAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIsisExtIPIfAddrType.setStatus("current")


class _FsIsisExtIPIfAddr_Type(OctetString):
    """Custom type fsIsisExtIPIfAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_FsIsisExtIPIfAddr_Type.__name__ = "OctetString"
_FsIsisExtIPIfAddr_Object = MibTableColumn
fsIsisExtIPIfAddr = _FsIsisExtIPIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 4, 1, 1, 4),
    _FsIsisExtIPIfAddr_Type()
)
fsIsisExtIPIfAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIsisExtIPIfAddr.setStatus("current")
_FsIsisExtIPIfExistState_Type = RowStatus
_FsIsisExtIPIfExistState_Object = MibTableColumn
fsIsisExtIPIfExistState = _FsIsisExtIPIfExistState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 4, 1, 1, 5),
    _FsIsisExtIPIfExistState_Type()
)
fsIsisExtIPIfExistState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtIPIfExistState.setStatus("current")
_FsIsisExtLog_ObjectIdentity = ObjectIdentity
fsIsisExtLog = _FsIsisExtLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 5)
)
if mibBuilder.loadTexts:
    fsIsisExtLog.setStatus("current")
_FsIsisExtLogTable_Object = MibTable
fsIsisExtLogTable = _FsIsisExtLogTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 5, 1)
)
if mibBuilder.loadTexts:
    fsIsisExtLogTable.setStatus("current")
_FsIsisExtLogEntry_Object = MibTableRow
fsIsisExtLogEntry = _FsIsisExtLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 5, 1, 1)
)
fsIsisExtLogEntry.setIndexNames(
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtLogModId"),
)
if mibBuilder.loadTexts:
    fsIsisExtLogEntry.setStatus("current")


class _FsIsisExtLogModId_Type(Integer32):
    """Custom type fsIsisExtLogModId based on Integer32"""
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
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("adjmodule", 0),
          ("ctlmodule", 1),
          ("updmodule", 2),
          ("decmodule", 3),
          ("tmrmodule", 4),
          ("fltmodule", 5),
          ("rtmmodule", 6),
          ("dllmodule", 7),
          ("bpcmodule", 8),
          ("fwdmodule", 9),
          ("trfmodule", 10),
          ("sbdmodule", 11),
          ("nmgmodule", 12),
          ("dbgmodule", 13),
          ("utlmodule", 14),
          ("grmodule", 15))
    )


_FsIsisExtLogModId_Type.__name__ = "Integer32"
_FsIsisExtLogModId_Object = MibTableColumn
fsIsisExtLogModId = _FsIsisExtLogModId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 5, 1, 1, 1),
    _FsIsisExtLogModId_Type()
)
fsIsisExtLogModId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIsisExtLogModId.setStatus("current")
_FsIsisExtLogLevel_Type = Integer32
_FsIsisExtLogLevel_Object = MibTableColumn
fsIsisExtLogLevel = _FsIsisExtLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 5, 1, 1, 2),
    _FsIsisExtLogLevel_Type()
)
fsIsisExtLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisExtLogLevel.setStatus("current")
_FsIsisExtAdj_ObjectIdentity = ObjectIdentity
fsIsisExtAdj = _FsIsisExtAdj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 6)
)
if mibBuilder.loadTexts:
    fsIsisExtAdj.setStatus("current")
_FsIsisExtAdjTable_Object = MibTable
fsIsisExtAdjTable = _FsIsisExtAdjTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 6, 1)
)
if mibBuilder.loadTexts:
    fsIsisExtAdjTable.setStatus("current")
_FsIsisExtAdjEntry_Object = MibTableRow
fsIsisExtAdjEntry = _FsIsisExtAdjEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 6, 1, 1)
)
fsIsisExtAdjEntry.setIndexNames(
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtSysInstance"),
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtCircIndex"),
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtAdjIndex"),
)
if mibBuilder.loadTexts:
    fsIsisExtAdjEntry.setStatus("current")


class _FsIsisExtAdjIndex_Type(Integer32):
    """Custom type fsIsisExtAdjIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_FsIsisExtAdjIndex_Type.__name__ = "Integer32"
_FsIsisExtAdjIndex_Object = MibTableColumn
fsIsisExtAdjIndex = _FsIsisExtAdjIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 6, 1, 1, 1),
    _FsIsisExtAdjIndex_Type()
)
fsIsisExtAdjIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIsisExtAdjIndex.setStatus("current")


class _FsIsisExtAdjNeighSysID_Type(OctetString):
    """Custom type fsIsisExtAdjNeighSysID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_FsIsisExtAdjNeighSysID_Type.__name__ = "OctetString"
_FsIsisExtAdjNeighSysID_Object = MibTableColumn
fsIsisExtAdjNeighSysID = _FsIsisExtAdjNeighSysID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 6, 1, 1, 2),
    _FsIsisExtAdjNeighSysID_Type()
)
fsIsisExtAdjNeighSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIsisExtAdjNeighSysID.setStatus("current")


class _FsIsisExtAdjHelperStatus_Type(Integer32):
    """Custom type fsIsisExtAdjHelperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notHelping", 1),
          ("helping", 2))
    )


_FsIsisExtAdjHelperStatus_Type.__name__ = "Integer32"
_FsIsisExtAdjHelperStatus_Object = MibTableColumn
fsIsisExtAdjHelperStatus = _FsIsisExtAdjHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 6, 1, 1, 3),
    _FsIsisExtAdjHelperStatus_Type()
)
fsIsisExtAdjHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIsisExtAdjHelperStatus.setStatus("current")


class _FsIsisExtAdjHelperExitReason_Type(Integer32):
    """Custom type fsIsisExtAdjHelperExitReason based on Integer32"""
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
        *(("none", 1),
          ("inProgress", 2),
          ("completed", 3),
          ("timedOut", 4),
          ("topologyChanged", 5))
    )


_FsIsisExtAdjHelperExitReason_Type.__name__ = "Integer32"
_FsIsisExtAdjHelperExitReason_Object = MibTableColumn
fsIsisExtAdjHelperExitReason = _FsIsisExtAdjHelperExitReason_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 2, 6, 1, 1, 4),
    _FsIsisExtAdjHelperExitReason_Type()
)
fsIsisExtAdjHelperExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIsisExtAdjHelperExitReason.setStatus("current")
_FsIsisNotifications_ObjectIdentity = ObjectIdentity
fsIsisNotifications = _FsIsisNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 3)
)
_FsIsisTraps_ObjectIdentity = ObjectIdentity
fsIsisTraps = _FsIsisTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 3, 0)
)
_FsisisDistInOutRouteMap_ObjectIdentity = ObjectIdentity
fsisisDistInOutRouteMap = _FsisisDistInOutRouteMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 4)
)
_FsIsisDistInOutRouteMapTable_Object = MibTable
fsIsisDistInOutRouteMapTable = _FsIsisDistInOutRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 4, 1)
)
if mibBuilder.loadTexts:
    fsIsisDistInOutRouteMapTable.setStatus("current")
_FsIsisDistInOutRouteMapEntry_Object = MibTableRow
fsIsisDistInOutRouteMapEntry = _FsIsisDistInOutRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 4, 1, 1)
)
fsIsisDistInOutRouteMapEntry.setIndexNames(
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtSysInstance"),
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisDistInOutRouteMapName"),
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisDistInOutRouteMapType"),
)
if mibBuilder.loadTexts:
    fsIsisDistInOutRouteMapEntry.setStatus("current")


class _FsIsisDistInOutRouteMapName_Type(DisplayString):
    """Custom type fsIsisDistInOutRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FsIsisDistInOutRouteMapName_Type.__name__ = "DisplayString"
_FsIsisDistInOutRouteMapName_Object = MibTableColumn
fsIsisDistInOutRouteMapName = _FsIsisDistInOutRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 4, 1, 1, 1),
    _FsIsisDistInOutRouteMapName_Type()
)
fsIsisDistInOutRouteMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIsisDistInOutRouteMapName.setStatus("current")


class _FsIsisDistInOutRouteMapType_Type(Integer32):
    """Custom type fsIsisDistInOutRouteMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FsIsisDistInOutRouteMapType_Type.__name__ = "Integer32"
_FsIsisDistInOutRouteMapType_Object = MibTableColumn
fsIsisDistInOutRouteMapType = _FsIsisDistInOutRouteMapType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 4, 1, 1, 2),
    _FsIsisDistInOutRouteMapType_Type()
)
fsIsisDistInOutRouteMapType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIsisDistInOutRouteMapType.setStatus("current")


class _FsIsisDistInOutRouteMapValue_Type(Integer32):
    """Custom type fsIsisDistInOutRouteMapValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsIsisDistInOutRouteMapValue_Type.__name__ = "Integer32"
_FsIsisDistInOutRouteMapValue_Object = MibTableColumn
fsIsisDistInOutRouteMapValue = _FsIsisDistInOutRouteMapValue_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 4, 1, 1, 3),
    _FsIsisDistInOutRouteMapValue_Type()
)
fsIsisDistInOutRouteMapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisDistInOutRouteMapValue.setStatus("current")
_FsIsisDistInOutRouteMapRowStatus_Type = RowStatus
_FsIsisDistInOutRouteMapRowStatus_Object = MibTableColumn
fsIsisDistInOutRouteMapRowStatus = _FsIsisDistInOutRouteMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 4, 1, 1, 4),
    _FsIsisDistInOutRouteMapRowStatus_Type()
)
fsIsisDistInOutRouteMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisDistInOutRouteMapRowStatus.setStatus("current")
_FsisisPreferenceGroup_ObjectIdentity = ObjectIdentity
fsisisPreferenceGroup = _FsisisPreferenceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 5)
)
_FsIsisPreferenceTable_Object = MibTable
fsIsisPreferenceTable = _FsIsisPreferenceTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 5, 1)
)
if mibBuilder.loadTexts:
    fsIsisPreferenceTable.setStatus("current")
_FsIsisPreferenceEntry_Object = MibTableRow
fsIsisPreferenceEntry = _FsIsisPreferenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 5, 1, 1)
)
fsIsisPreferenceEntry.setIndexNames(
    (0, "SUPERMICRO-ISIS-MIB", "fsIsisExtSysInstance"),
)
if mibBuilder.loadTexts:
    fsIsisPreferenceEntry.setStatus("current")


class _FsIsisPreferenceValue_Type(Integer32):
    """Custom type fsIsisPreferenceValue based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsIsisPreferenceValue_Type.__name__ = "Integer32"
_FsIsisPreferenceValue_Object = MibTableColumn
fsIsisPreferenceValue = _FsIsisPreferenceValue_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 5, 1, 1, 2),
    _FsIsisPreferenceValue_Type()
)
fsIsisPreferenceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisPreferenceValue.setStatus("current")
_FsIsisPreferenceRowStatus_Type = RowStatus
_FsIsisPreferenceRowStatus_Object = MibTableColumn
fsIsisPreferenceRowStatus = _FsIsisPreferenceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 5, 1, 1, 3),
    _FsIsisPreferenceRowStatus_Type()
)
fsIsisPreferenceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIsisPreferenceRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

fsIsisRestartStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 3, 0, 1)
)
fsIsisRestartStatusChange.setObjects(
      *(("SUPERMICRO-ISIS-MIB", "fsIsisExtSysActSysID"),
        ("SUPERMICRO-ISIS-MIB", "fsIsisExtRestartStatus"),
        ("SUPERMICRO-ISIS-MIB", "fsIsisExtGRRestartTimeInterval"),
        ("SUPERMICRO-ISIS-MIB", "fsIsisExtRestartExitReason"))
)
if mibBuilder.loadTexts:
    fsIsisRestartStatusChange.setStatus(
        "current"
    )

fsIsisHelperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 62, 3, 0, 2)
)
fsIsisHelperStatusChange.setObjects(
      *(("SUPERMICRO-ISIS-MIB", "fsIsisExtSysActSysID"),
        ("SUPERMICRO-ISIS-MIB", "fsIsisExtAdjNeighSysID"),
        ("SUPERMICRO-ISIS-MIB", "fsIsisExtAdjHelperStatus"),
        ("SUPERMICRO-ISIS-MIB", "fsIsisExtHelperGraceTimeLimit"),
        ("SUPERMICRO-ISIS-MIB", "fsIsisExtAdjHelperExitReason"))
)
if mibBuilder.loadTexts:
    fsIsisHelperStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-ISIS-MIB",
    **{"MetricType": MetricType,
       "fsIsis": fsIsis,
       "fsIsisScl": fsIsisScl,
       "fsIsisMaxInstances": fsIsisMaxInstances,
       "fsIsisMaxCircuits": fsIsisMaxCircuits,
       "fsIsisMaxAreaAddrs": fsIsisMaxAreaAddrs,
       "fsIsisMaxAdjs": fsIsisMaxAdjs,
       "fsIsisMaxIPRAs": fsIsisMaxIPRAs,
       "fsIsisMaxEvents": fsIsisMaxEvents,
       "fsIsisMaxSummAddr": fsIsisMaxSummAddr,
       "fsIsisStatus": fsIsisStatus,
       "fsIsisMaxLSPEntries": fsIsisMaxLSPEntries,
       "fsIsisMaxMAA": fsIsisMaxMAA,
       "fsIsisFTStatus": fsIsisFTStatus,
       "fsIsisFTState": fsIsisFTState,
       "fsIsisFactor": fsIsisFactor,
       "fsIsisMaxRoutes": fsIsisMaxRoutes,
       "fsIsisRestartState": fsIsisRestartState,
       "fsIsisExt": fsIsisExt,
       "fsIsisExtSystem": fsIsisExtSystem,
       "fsIsisExtSysTable": fsIsisExtSysTable,
       "fsIsisExtSysEntry": fsIsisExtSysEntry,
       "fsIsisExtSysInstance": fsIsisExtSysInstance,
       "fsIsisExtSysAuthSupp": fsIsisExtSysAuthSupp,
       "fsIsisExtSysAreaAuthType": fsIsisExtSysAreaAuthType,
       "fsIsisExtSysDomainAuthType": fsIsisExtSysDomainAuthType,
       "fsIsisExtSysAreaTxPasswd": fsIsisExtSysAreaTxPasswd,
       "fsIsisExtSysDomainTxPasswd": fsIsisExtSysDomainTxPasswd,
       "fsIsisExtSysMinSPFSchTime": fsIsisExtSysMinSPFSchTime,
       "fsIsisExtSysMaxSPFSchTime": fsIsisExtSysMaxSPFSchTime,
       "fsIsisExtSysMinLSPMark": fsIsisExtSysMinLSPMark,
       "fsIsisExtSysMaxLSPMark": fsIsisExtSysMaxLSPMark,
       "fsIsisExtSysDelMetSupp": fsIsisExtSysDelMetSupp,
       "fsIsisExtSysErrMetSupp": fsIsisExtSysErrMetSupp,
       "fsIsisExtSysExpMetSupp": fsIsisExtSysExpMetSupp,
       "fsIsisExtSysActSysType": fsIsisExtSysActSysType,
       "fsIsisExtSysActMPS": fsIsisExtSysActMPS,
       "fsIsisExtSysActMaxAA": fsIsisExtSysActMaxAA,
       "fsIsisExtSysActSysIDLen": fsIsisExtSysActSysIDLen,
       "fsIsisExtSysActSysID": fsIsisExtSysActSysID,
       "fsIsisExtSysActOrigL1LSPBufSize": fsIsisExtSysActOrigL1LSPBufSize,
       "fsIsisExtSysActOrigL2LSPBufSize": fsIsisExtSysActOrigL2LSPBufSize,
       "fsIsisExtSysRouterID": fsIsisExtSysRouterID,
       "fsIsisExtSysCkts": fsIsisExtSysCkts,
       "fsIsisExtSysActiveCkts": fsIsisExtSysActiveCkts,
       "fsIsisExtSysAdjs": fsIsisExtSysAdjs,
       "fsIsisExtSysOperState": fsIsisExtSysOperState,
       "fsIsisExtSysDroppedPDUs": fsIsisExtSysDroppedPDUs,
       "fsIsisExtRestartSupport": fsIsisExtRestartSupport,
       "fsIsisExtGRRestartTimeInterval": fsIsisExtGRRestartTimeInterval,
       "fsIsisExtGRT2TimeIntervalLevel1": fsIsisExtGRT2TimeIntervalLevel1,
       "fsIsisExtGRT2TimeIntervalLevel2": fsIsisExtGRT2TimeIntervalLevel2,
       "fsIsisExtGRT1TimeInterval": fsIsisExtGRT1TimeInterval,
       "fsIsisExtGRT1RetryCount": fsIsisExtGRT1RetryCount,
       "fsIsisExtGRMode": fsIsisExtGRMode,
       "fsIsisExtRestartStatus": fsIsisExtRestartStatus,
       "fsIsisExtRestartExitReason": fsIsisExtRestartExitReason,
       "fsIsisExtRestartReason": fsIsisExtRestartReason,
       "fsIsisExtHelperSupport": fsIsisExtHelperSupport,
       "fsIsisExtHelperGraceTimeLimit": fsIsisExtHelperGraceTimeLimit,
       "fsIsisExtSysAreaRxPasswdTable": fsIsisExtSysAreaRxPasswdTable,
       "fsIsisExtSysAreaRxPasswdEntry": fsIsisExtSysAreaRxPasswdEntry,
       "fsIsisExtSysAreaRxPasswd": fsIsisExtSysAreaRxPasswd,
       "fsIsisExtSysAreaRxPasswdExistState": fsIsisExtSysAreaRxPasswdExistState,
       "fsIsisExtSysDomainRxPasswdTable": fsIsisExtSysDomainRxPasswdTable,
       "fsIsisExtSysDomainRxPasswdEntry": fsIsisExtSysDomainRxPasswdEntry,
       "fsIsisExtSysDomainRxPassword": fsIsisExtSysDomainRxPassword,
       "fsIsisExtSysDomainRxPasswdExistState": fsIsisExtSysDomainRxPasswdExistState,
       "fsIsisExtSysEventTable": fsIsisExtSysEventTable,
       "fsIsisExtSysEventEntry": fsIsisExtSysEventEntry,
       "fsIsisExtSysEventIdx": fsIsisExtSysEventIdx,
       "fsIsisExtSysEvent": fsIsisExtSysEvent,
       "fsIsisExtSysEventStr": fsIsisExtSysEventStr,
       "fsIsisExtCirc": fsIsisExtCirc,
       "fsIsisExtCircTable": fsIsisExtCircTable,
       "fsIsisExtCircEntry": fsIsisExtCircEntry,
       "fsIsisExtCircIndex": fsIsisExtCircIndex,
       "fsIsisExtCircIfStatus": fsIsisExtCircIfStatus,
       "fsIsisExtCircTxEnable": fsIsisExtCircTxEnable,
       "fsIsisExtCircRxEnable": fsIsisExtCircRxEnable,
       "fsIsisExtCircTxISHs": fsIsisExtCircTxISHs,
       "fsIsisExtCircRxISHs": fsIsisExtCircRxISHs,
       "fsIsisExtCircSNPA": fsIsisExtCircSNPA,
       "fsIsisExtCircLevelTable": fsIsisExtCircLevelTable,
       "fsIsisExtCircLevelEntry": fsIsisExtCircLevelEntry,
       "fsIsisExtCircLevelIndex": fsIsisExtCircLevelIndex,
       "fsIsisExtCircLevelDelayMetric": fsIsisExtCircLevelDelayMetric,
       "fsIsisExtCircLevelErrorMetric": fsIsisExtCircLevelErrorMetric,
       "fsIsisExtCircLevelExpenseMetric": fsIsisExtCircLevelExpenseMetric,
       "fsIsisExtCircLevelTxPassword": fsIsisExtCircLevelTxPassword,
       "fsIsisExtIPRATable": fsIsisExtIPRATable,
       "fsIsisExtIPRAEntry": fsIsisExtIPRAEntry,
       "fsIsisExtIPRAType": fsIsisExtIPRAType,
       "fsIsisExtIPRAIndex": fsIsisExtIPRAIndex,
       "fsIsisExtIPRADelayMetric": fsIsisExtIPRADelayMetric,
       "fsIsisExtIPRAErrorMetric": fsIsisExtIPRAErrorMetric,
       "fsIsisExtIPRAExpenseMetric": fsIsisExtIPRAExpenseMetric,
       "fsIsisExtIPRADelayMetricType": fsIsisExtIPRADelayMetricType,
       "fsIsisExtIPRAErrorMetricType": fsIsisExtIPRAErrorMetricType,
       "fsIsisExtIPRAExpenseMetricType": fsIsisExtIPRAExpenseMetricType,
       "fsIsisExtIPRANextHopType": fsIsisExtIPRANextHopType,
       "fsIsisExtIPRANextHop": fsIsisExtIPRANextHop,
       "fsIsisExtCircLevelRxPasswordTable": fsIsisExtCircLevelRxPasswordTable,
       "fsIsisExtCircLevelRxPasswordEntry": fsIsisExtCircLevelRxPasswordEntry,
       "fsIsisExtCircLevelRxPassword": fsIsisExtCircLevelRxPassword,
       "fsIsisExtCircLevelRxPasswordExistState": fsIsisExtCircLevelRxPasswordExistState,
       "fsIsisExtSummAddr": fsIsisExtSummAddr,
       "fsIsisExtSummAddrTable": fsIsisExtSummAddrTable,
       "fsIsisExtSummAddrEntry": fsIsisExtSummAddrEntry,
       "fsIsisExtSummAddressType": fsIsisExtSummAddressType,
       "fsIsisExtSummAddress": fsIsisExtSummAddress,
       "fsIsisExtSummAddrPrefixLen": fsIsisExtSummAddrPrefixLen,
       "fsIsisExtSummAddrDelayMetric": fsIsisExtSummAddrDelayMetric,
       "fsIsisExtSummAddrErrorMetric": fsIsisExtSummAddrErrorMetric,
       "fsIsisExtSummAddrExpenseMetric": fsIsisExtSummAddrExpenseMetric,
       "fsIsisExtIPIf": fsIsisExtIPIf,
       "fsIsisExtIPIfAddrTable": fsIsisExtIPIfAddrTable,
       "fsIsisExtIPIfAddrEntry": fsIsisExtIPIfAddrEntry,
       "fsIsisExtIPIfIndex": fsIsisExtIPIfIndex,
       "fsIsisExtIPIfSubIndex": fsIsisExtIPIfSubIndex,
       "fsIsisExtIPIfAddrType": fsIsisExtIPIfAddrType,
       "fsIsisExtIPIfAddr": fsIsisExtIPIfAddr,
       "fsIsisExtIPIfExistState": fsIsisExtIPIfExistState,
       "fsIsisExtLog": fsIsisExtLog,
       "fsIsisExtLogTable": fsIsisExtLogTable,
       "fsIsisExtLogEntry": fsIsisExtLogEntry,
       "fsIsisExtLogModId": fsIsisExtLogModId,
       "fsIsisExtLogLevel": fsIsisExtLogLevel,
       "fsIsisExtAdj": fsIsisExtAdj,
       "fsIsisExtAdjTable": fsIsisExtAdjTable,
       "fsIsisExtAdjEntry": fsIsisExtAdjEntry,
       "fsIsisExtAdjIndex": fsIsisExtAdjIndex,
       "fsIsisExtAdjNeighSysID": fsIsisExtAdjNeighSysID,
       "fsIsisExtAdjHelperStatus": fsIsisExtAdjHelperStatus,
       "fsIsisExtAdjHelperExitReason": fsIsisExtAdjHelperExitReason,
       "fsIsisNotifications": fsIsisNotifications,
       "fsIsisTraps": fsIsisTraps,
       "fsIsisRestartStatusChange": fsIsisRestartStatusChange,
       "fsIsisHelperStatusChange": fsIsisHelperStatusChange,
       "fsisisDistInOutRouteMap": fsisisDistInOutRouteMap,
       "fsIsisDistInOutRouteMapTable": fsIsisDistInOutRouteMapTable,
       "fsIsisDistInOutRouteMapEntry": fsIsisDistInOutRouteMapEntry,
       "fsIsisDistInOutRouteMapName": fsIsisDistInOutRouteMapName,
       "fsIsisDistInOutRouteMapType": fsIsisDistInOutRouteMapType,
       "fsIsisDistInOutRouteMapValue": fsIsisDistInOutRouteMapValue,
       "fsIsisDistInOutRouteMapRowStatus": fsIsisDistInOutRouteMapRowStatus,
       "fsisisPreferenceGroup": fsisisPreferenceGroup,
       "fsIsisPreferenceTable": fsIsisPreferenceTable,
       "fsIsisPreferenceEntry": fsIsisPreferenceEntry,
       "fsIsisPreferenceValue": fsIsisPreferenceValue,
       "fsIsisPreferenceRowStatus": fsIsisPreferenceRowStatus}
)
