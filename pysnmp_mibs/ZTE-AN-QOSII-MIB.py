# SNMP MIB module (ZTE-AN-QOSII-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-QOSII-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:28 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(zxAn,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "zxAn")


# MODULE-IDENTITY

zxAnQosMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnQosIIObjects_ObjectIdentity = ObjectIdentity
zxAnQosIIObjects = _ZxAnQosIIObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3)
)


class _ZxAnQosIINniCos2DropMap_Type(OctetString):
    """Custom type zxAnQosIINniCos2DropMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_ZxAnQosIINniCos2DropMap_Type.__name__ = "OctetString"
_ZxAnQosIINniCos2DropMap_Object = MibScalar
zxAnQosIINniCos2DropMap = _ZxAnQosIINniCos2DropMap_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 1),
    _ZxAnQosIINniCos2DropMap_Type()
)
zxAnQosIINniCos2DropMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQosIINniCos2DropMap.setStatus("current")


class _ZxAnQosIINniCos2LocalMap_Type(OctetString):
    """Custom type zxAnQosIINniCos2LocalMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_ZxAnQosIINniCos2LocalMap_Type.__name__ = "OctetString"
_ZxAnQosIINniCos2LocalMap_Object = MibScalar
zxAnQosIINniCos2LocalMap = _ZxAnQosIINniCos2LocalMap_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 2),
    _ZxAnQosIINniCos2LocalMap_Type()
)
zxAnQosIINniCos2LocalMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQosIINniCos2LocalMap.setStatus("current")
_ZxAnQosIINniDscpMappingTable_Object = MibTable
zxAnQosIINniDscpMappingTable = _ZxAnQosIINniDscpMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 3)
)
if mibBuilder.loadTexts:
    zxAnQosIINniDscpMappingTable.setStatus("current")
_ZxAnQosIINniDscpMappingEntry_Object = MibTableRow
zxAnQosIINniDscpMappingEntry = _ZxAnQosIINniDscpMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 3, 1)
)
zxAnQosIINniDscpMappingEntry.setIndexNames(
    (0, "ZTE-AN-QOSII-MIB", "zxAnQosIINniIngressDscp"),
)
if mibBuilder.loadTexts:
    zxAnQosIINniDscpMappingEntry.setStatus("current")


class _ZxAnQosIINniIngressDscp_Type(Integer32):
    """Custom type zxAnQosIINniIngressDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ZxAnQosIINniIngressDscp_Type.__name__ = "Integer32"
_ZxAnQosIINniIngressDscp_Object = MibTableColumn
zxAnQosIINniIngressDscp = _ZxAnQosIINniIngressDscp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 3, 1, 1),
    _ZxAnQosIINniIngressDscp_Type()
)
zxAnQosIINniIngressDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosIINniIngressDscp.setStatus("current")


class _ZxAnQosIINniEgressDscp_Type(Integer32):
    """Custom type zxAnQosIINniEgressDscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ZxAnQosIINniEgressDscp_Type.__name__ = "Integer32"
_ZxAnQosIINniEgressDscp_Object = MibTableColumn
zxAnQosIINniEgressDscp = _ZxAnQosIINniEgressDscp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 3, 1, 2),
    _ZxAnQosIINniEgressDscp_Type()
)
zxAnQosIINniEgressDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQosIINniEgressDscp.setStatus("current")


class _ZxAnQosIINniEgressCos_Type(Integer32):
    """Custom type zxAnQosIINniEgressCos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnQosIINniEgressCos_Type.__name__ = "Integer32"
_ZxAnQosIINniEgressCos_Object = MibTableColumn
zxAnQosIINniEgressCos = _ZxAnQosIINniEgressCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 3, 1, 3),
    _ZxAnQosIINniEgressCos_Type()
)
zxAnQosIINniEgressCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQosIINniEgressCos.setStatus("current")


class _ZxAnQosIINniEgressDropPrecedence_Type(Integer32):
    """Custom type zxAnQosIINniEgressDropPrecedence based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ZxAnQosIINniEgressDropPrecedence_Type.__name__ = "Integer32"
_ZxAnQosIINniEgressDropPrecedence_Object = MibTableColumn
zxAnQosIINniEgressDropPrecedence = _ZxAnQosIINniEgressDropPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 3, 1, 4),
    _ZxAnQosIINniEgressDropPrecedence_Type()
)
zxAnQosIINniEgressDropPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQosIINniEgressDropPrecedence.setStatus("current")
_ZxAnQosIINniPortCfgTable_Object = MibTable
zxAnQosIINniPortCfgTable = _ZxAnQosIINniPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 4)
)
if mibBuilder.loadTexts:
    zxAnQosIINniPortCfgTable.setStatus("current")
_ZxAnQosIINniPortCfgEntry_Object = MibTableRow
zxAnQosIINniPortCfgEntry = _ZxAnQosIINniPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 4, 1)
)
zxAnQosIINniPortCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnQosIINniPortCfgEntry.setStatus("current")


class _ZxAnQosIINniDefPriority_Type(Integer32):
    """Custom type zxAnQosIINniDefPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnQosIINniDefPriority_Type.__name__ = "Integer32"
_ZxAnQosIINniDefPriority_Object = MibTableColumn
zxAnQosIINniDefPriority = _ZxAnQosIINniDefPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 4, 1, 1),
    _ZxAnQosIINniDefPriority_Type()
)
zxAnQosIINniDefPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIINniDefPriority.setStatus("current")


class _ZxAnQosIINniTrustDscp_Type(Integer32):
    """Custom type zxAnQosIINniTrustDscp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("notsupport", 255))
    )


_ZxAnQosIINniTrustDscp_Type.__name__ = "Integer32"
_ZxAnQosIINniTrustDscp_Object = MibTableColumn
zxAnQosIINniTrustDscp = _ZxAnQosIINniTrustDscp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 4, 1, 2),
    _ZxAnQosIINniTrustDscp_Type()
)
zxAnQosIINniTrustDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIINniTrustDscp.setStatus("current")


class _ZxAnQosIINniTrustCos_Type(Integer32):
    """Custom type zxAnQosIINniTrustCos based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("notsupport", 255))
    )


_ZxAnQosIINniTrustCos_Type.__name__ = "Integer32"
_ZxAnQosIINniTrustCos_Object = MibTableColumn
zxAnQosIINniTrustCos = _ZxAnQosIINniTrustCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 4, 1, 3),
    _ZxAnQosIINniTrustCos_Type()
)
zxAnQosIINniTrustCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIINniTrustCos.setStatus("current")


class _ZxAnQosIINniQueuesAlgorithm_Type(Integer32):
    """Custom type zxAnQosIINniQueuesAlgorithm based on Integer32"""
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
        *(("sp", 1),
          ("wrr", 2),
          ("fq", 3))
    )


_ZxAnQosIINniQueuesAlgorithm_Type.__name__ = "Integer32"
_ZxAnQosIINniQueuesAlgorithm_Object = MibTableColumn
zxAnQosIINniQueuesAlgorithm = _ZxAnQosIINniQueuesAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 4, 1, 4),
    _ZxAnQosIINniQueuesAlgorithm_Type()
)
zxAnQosIINniQueuesAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIINniQueuesAlgorithm.setStatus("current")
_ZxAnQosIINniQueuesWeight_Type = ObjectIdentifier
_ZxAnQosIINniQueuesWeight_Object = MibTableColumn
zxAnQosIINniQueuesWeight = _ZxAnQosIINniQueuesWeight_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 4, 1, 5),
    _ZxAnQosIINniQueuesWeight_Type()
)
zxAnQosIINniQueuesWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIINniQueuesWeight.setStatus("current")
_ZxAnQosIINniQueuesMinRate_Type = ObjectIdentifier
_ZxAnQosIINniQueuesMinRate_Object = MibTableColumn
zxAnQosIINniQueuesMinRate = _ZxAnQosIINniQueuesMinRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 4, 1, 6),
    _ZxAnQosIINniQueuesMinRate_Type()
)
zxAnQosIINniQueuesMinRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIINniQueuesMinRate.setStatus("current")
_ZxAnQosIINniQueuesMaxRate_Type = ObjectIdentifier
_ZxAnQosIINniQueuesMaxRate_Object = MibTableColumn
zxAnQosIINniQueuesMaxRate = _ZxAnQosIINniQueuesMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 4, 1, 7),
    _ZxAnQosIINniQueuesMaxRate_Type()
)
zxAnQosIINniQueuesMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIINniQueuesMaxRate.setStatus("current")


class _ZxAnQosIINniShapeRateLimit_Type(Integer32):
    """Custom type zxAnQosIINniShapeRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 1000000),
    )


_ZxAnQosIINniShapeRateLimit_Type.__name__ = "Integer32"
_ZxAnQosIINniShapeRateLimit_Object = MibTableColumn
zxAnQosIINniShapeRateLimit = _ZxAnQosIINniShapeRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 4, 1, 8),
    _ZxAnQosIINniShapeRateLimit_Type()
)
zxAnQosIINniShapeRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIINniShapeRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    zxAnQosIINniShapeRateLimit.setUnits("kbps")


class _ZxAnQosIINniShapeBurstSize_Type(Integer32):
    """Custom type zxAnQosIINniShapeBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4, 16000),
    )


_ZxAnQosIINniShapeBurstSize_Type.__name__ = "Integer32"
_ZxAnQosIINniShapeBurstSize_Object = MibTableColumn
zxAnQosIINniShapeBurstSize = _ZxAnQosIINniShapeBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 4, 1, 9),
    _ZxAnQosIINniShapeBurstSize_Type()
)
zxAnQosIINniShapeBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIINniShapeBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnQosIINniShapeBurstSize.setUnits("kbps")
_ZxAnQosIINniQueuesDepth_Type = ObjectIdentifier
_ZxAnQosIINniQueuesDepth_Object = MibTableColumn
zxAnQosIINniQueuesDepth = _ZxAnQosIINniQueuesDepth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 4, 1, 10),
    _ZxAnQosIINniQueuesDepth_Type()
)
zxAnQosIINniQueuesDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIINniQueuesDepth.setStatus("current")
_ZxAnQosIINniGlobal_ObjectIdentity = ObjectIdentity
zxAnQosIINniGlobal = _ZxAnQosIINniGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 5)
)


class _ZxAnQosIINniGlobalTrustMode_Type(Integer32):
    """Custom type zxAnQosIINniGlobalTrustMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("untrust", 1),
          ("trustcosonly", 2),
          ("trustdscponly", 3),
          ("notsupport", 255))
    )


_ZxAnQosIINniGlobalTrustMode_Type.__name__ = "Integer32"
_ZxAnQosIINniGlobalTrustMode_Object = MibScalar
zxAnQosIINniGlobalTrustMode = _ZxAnQosIINniGlobalTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 5, 1),
    _ZxAnQosIINniGlobalTrustMode_Type()
)
zxAnQosIINniGlobalTrustMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIINniGlobalTrustMode.setStatus("current")
_ZxAnQosIICos2DscpTable_Object = MibTable
zxAnQosIICos2DscpTable = _ZxAnQosIICos2DscpTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 10)
)
if mibBuilder.loadTexts:
    zxAnQosIICos2DscpTable.setStatus("current")
_ZxAnQosIICos2DscpEntry_Object = MibTableRow
zxAnQosIICos2DscpEntry = _ZxAnQosIICos2DscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 10, 1)
)
zxAnQosIICos2DscpEntry.setIndexNames(
    (0, "ZTE-AN-QOSII-MIB", "zxAnQosIICos2DscpCosValue"),
)
if mibBuilder.loadTexts:
    zxAnQosIICos2DscpEntry.setStatus("current")


class _ZxAnQosIICos2DscpCosValue_Type(Integer32):
    """Custom type zxAnQosIICos2DscpCosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnQosIICos2DscpCosValue_Type.__name__ = "Integer32"
_ZxAnQosIICos2DscpCosValue_Object = MibTableColumn
zxAnQosIICos2DscpCosValue = _ZxAnQosIICos2DscpCosValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 10, 1, 1),
    _ZxAnQosIICos2DscpCosValue_Type()
)
zxAnQosIICos2DscpCosValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosIICos2DscpCosValue.setStatus("current")


class _ZxAnQosIICos2DscpDscpValue_Type(Integer32):
    """Custom type zxAnQosIICos2DscpDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ZxAnQosIICos2DscpDscpValue_Type.__name__ = "Integer32"
_ZxAnQosIICos2DscpDscpValue_Object = MibTableColumn
zxAnQosIICos2DscpDscpValue = _ZxAnQosIICos2DscpDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 10, 1, 2),
    _ZxAnQosIICos2DscpDscpValue_Type()
)
zxAnQosIICos2DscpDscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQosIICos2DscpDscpValue.setStatus("current")
_ZxAnQosIIDscp2CosTable_Object = MibTable
zxAnQosIIDscp2CosTable = _ZxAnQosIIDscp2CosTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 11)
)
if mibBuilder.loadTexts:
    zxAnQosIIDscp2CosTable.setStatus("current")
_ZxAnQosIIDscp2CosEntry_Object = MibTableRow
zxAnQosIIDscp2CosEntry = _ZxAnQosIIDscp2CosEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 11, 1)
)
zxAnQosIIDscp2CosEntry.setIndexNames(
    (0, "ZTE-AN-QOSII-MIB", "zxAnQosIIDscp2CosDscpValue"),
)
if mibBuilder.loadTexts:
    zxAnQosIIDscp2CosEntry.setStatus("current")


class _ZxAnQosIIDscp2CosDscpValue_Type(Integer32):
    """Custom type zxAnQosIIDscp2CosDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ZxAnQosIIDscp2CosDscpValue_Type.__name__ = "Integer32"
_ZxAnQosIIDscp2CosDscpValue_Object = MibTableColumn
zxAnQosIIDscp2CosDscpValue = _ZxAnQosIIDscp2CosDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 11, 1, 1),
    _ZxAnQosIIDscp2CosDscpValue_Type()
)
zxAnQosIIDscp2CosDscpValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosIIDscp2CosDscpValue.setStatus("current")


class _ZxAnQosIIDscp2CosCosValue_Type(Integer32):
    """Custom type zxAnQosIIDscp2CosCosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnQosIIDscp2CosCosValue_Type.__name__ = "Integer32"
_ZxAnQosIIDscp2CosCosValue_Object = MibTableColumn
zxAnQosIIDscp2CosCosValue = _ZxAnQosIIDscp2CosCosValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 11, 1, 2),
    _ZxAnQosIIDscp2CosCosValue_Type()
)
zxAnQosIIDscp2CosCosValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnQosIIDscp2CosCosValue.setStatus("current")
_ZxAnQosIICos2QueuesProfileTable_Object = MibTable
zxAnQosIICos2QueuesProfileTable = _ZxAnQosIICos2QueuesProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 13)
)
if mibBuilder.loadTexts:
    zxAnQosIICos2QueuesProfileTable.setStatus("current")
_ZxAnQosIICos2QueuesProfileEntry_Object = MibTableRow
zxAnQosIICos2QueuesProfileEntry = _ZxAnQosIICos2QueuesProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 13, 1)
)
zxAnQosIICos2QueuesProfileEntry.setIndexNames(
    (0, "ZTE-AN-QOSII-MIB", "zxAnQosIICos2QueuesPrfName"),
)
if mibBuilder.loadTexts:
    zxAnQosIICos2QueuesProfileEntry.setStatus("current")


class _ZxAnQosIICos2QueuesPrfName_Type(DisplayString):
    """Custom type zxAnQosIICos2QueuesPrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnQosIICos2QueuesPrfName_Type.__name__ = "DisplayString"
_ZxAnQosIICos2QueuesPrfName_Object = MibTableColumn
zxAnQosIICos2QueuesPrfName = _ZxAnQosIICos2QueuesPrfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 13, 1, 1),
    _ZxAnQosIICos2QueuesPrfName_Type()
)
zxAnQosIICos2QueuesPrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosIICos2QueuesPrfName.setStatus("current")
_ZxAnQosIICos2Queues_Type = ObjectIdentifier
_ZxAnQosIICos2Queues_Object = MibTableColumn
zxAnQosIICos2Queues = _ZxAnQosIICos2Queues_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 13, 1, 2),
    _ZxAnQosIICos2Queues_Type()
)
zxAnQosIICos2Queues.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIICos2Queues.setStatus("current")
_ZxAnQosIIDropPrecedence_Type = ObjectIdentifier
_ZxAnQosIIDropPrecedence_Object = MibTableColumn
zxAnQosIIDropPrecedence = _ZxAnQosIIDropPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 13, 1, 3),
    _ZxAnQosIIDropPrecedence_Type()
)
zxAnQosIIDropPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIDropPrecedence.setStatus("current")
_ZxAnQosIICos2QueuesRowStatus_Type = RowStatus
_ZxAnQosIICos2QueuesRowStatus_Object = MibTableColumn
zxAnQosIICos2QueuesRowStatus = _ZxAnQosIICos2QueuesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 13, 1, 20),
    _ZxAnQosIICos2QueuesRowStatus_Type()
)
zxAnQosIICos2QueuesRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIICos2QueuesRowStatus.setStatus("current")
_ZxAnQosIIQueuesBlockProfileTable_Object = MibTable
zxAnQosIIQueuesBlockProfileTable = _ZxAnQosIIQueuesBlockProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 14)
)
if mibBuilder.loadTexts:
    zxAnQosIIQueuesBlockProfileTable.setStatus("current")
_ZxAnQosIIQueuesBlockProfileEntry_Object = MibTableRow
zxAnQosIIQueuesBlockProfileEntry = _ZxAnQosIIQueuesBlockProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 14, 1)
)
zxAnQosIIQueuesBlockProfileEntry.setIndexNames(
    (0, "ZTE-AN-QOSII-MIB", "zxAnQosIIQueuesBlockPrfName"),
)
if mibBuilder.loadTexts:
    zxAnQosIIQueuesBlockProfileEntry.setStatus("current")


class _ZxAnQosIIQueuesBlockPrfName_Type(DisplayString):
    """Custom type zxAnQosIIQueuesBlockPrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnQosIIQueuesBlockPrfName_Type.__name__ = "DisplayString"
_ZxAnQosIIQueuesBlockPrfName_Object = MibTableColumn
zxAnQosIIQueuesBlockPrfName = _ZxAnQosIIQueuesBlockPrfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 14, 1, 1),
    _ZxAnQosIIQueuesBlockPrfName_Type()
)
zxAnQosIIQueuesBlockPrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosIIQueuesBlockPrfName.setStatus("current")
_ZxAnQosIIQueuesPriority_Type = ObjectIdentifier
_ZxAnQosIIQueuesPriority_Object = MibTableColumn
zxAnQosIIQueuesPriority = _ZxAnQosIIQueuesPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 14, 1, 2),
    _ZxAnQosIIQueuesPriority_Type()
)
zxAnQosIIQueuesPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIQueuesPriority.setStatus("current")
_ZxAnQosIIQueuesWeight_Type = ObjectIdentifier
_ZxAnQosIIQueuesWeight_Object = MibTableColumn
zxAnQosIIQueuesWeight = _ZxAnQosIIQueuesWeight_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 14, 1, 3),
    _ZxAnQosIIQueuesWeight_Type()
)
zxAnQosIIQueuesWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIQueuesWeight.setStatus("current")
_ZxAnQosIIQueuesDepth_Type = ObjectIdentifier
_ZxAnQosIIQueuesDepth_Object = MibTableColumn
zxAnQosIIQueuesDepth = _ZxAnQosIIQueuesDepth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 14, 1, 4),
    _ZxAnQosIIQueuesDepth_Type()
)
zxAnQosIIQueuesDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIQueuesDepth.setStatus("current")
_ZxAnQosIIQueuesBlockRowStatus_Type = RowStatus
_ZxAnQosIIQueuesBlockRowStatus_Object = MibTableColumn
zxAnQosIIQueuesBlockRowStatus = _ZxAnQosIIQueuesBlockRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 14, 1, 20),
    _ZxAnQosIIQueuesBlockRowStatus_Type()
)
zxAnQosIIQueuesBlockRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIQueuesBlockRowStatus.setStatus("current")
_ZxAnQosIICosRemarkProfileTable_Object = MibTable
zxAnQosIICosRemarkProfileTable = _ZxAnQosIICosRemarkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 15)
)
if mibBuilder.loadTexts:
    zxAnQosIICosRemarkProfileTable.setStatus("current")
_ZxAnQosIICosRemarkProfileEntry_Object = MibTableRow
zxAnQosIICosRemarkProfileEntry = _ZxAnQosIICosRemarkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 15, 1)
)
zxAnQosIICosRemarkProfileEntry.setIndexNames(
    (0, "ZTE-AN-QOSII-MIB", "zxAnQosIICosRemarkPrfName"),
)
if mibBuilder.loadTexts:
    zxAnQosIICosRemarkProfileEntry.setStatus("current")


class _ZxAnQosIICosRemarkPrfName_Type(DisplayString):
    """Custom type zxAnQosIICosRemarkPrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnQosIICosRemarkPrfName_Type.__name__ = "DisplayString"
_ZxAnQosIICosRemarkPrfName_Object = MibTableColumn
zxAnQosIICosRemarkPrfName = _ZxAnQosIICosRemarkPrfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 15, 1, 1),
    _ZxAnQosIICosRemarkPrfName_Type()
)
zxAnQosIICosRemarkPrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosIICosRemarkPrfName.setStatus("current")
_ZxAnQosIIEgressPriority_Type = ObjectIdentifier
_ZxAnQosIIEgressPriority_Object = MibTableColumn
zxAnQosIIEgressPriority = _ZxAnQosIIEgressPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 15, 1, 2),
    _ZxAnQosIIEgressPriority_Type()
)
zxAnQosIIEgressPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIEgressPriority.setStatus("current")
_ZxAnQosIICosRemarkRowStatus_Type = RowStatus
_ZxAnQosIICosRemarkRowStatus_Object = MibTableColumn
zxAnQosIICosRemarkRowStatus = _ZxAnQosIICosRemarkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 15, 1, 20),
    _ZxAnQosIICosRemarkRowStatus_Type()
)
zxAnQosIICosRemarkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIICosRemarkRowStatus.setStatus("current")
_ZxAnQosIITrafficProfileTable_Object = MibTable
zxAnQosIITrafficProfileTable = _ZxAnQosIITrafficProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 16)
)
if mibBuilder.loadTexts:
    zxAnQosIITrafficProfileTable.setStatus("current")
_ZxAnQosIITrafficProfileEntry_Object = MibTableRow
zxAnQosIITrafficProfileEntry = _ZxAnQosIITrafficProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 16, 1)
)
zxAnQosIITrafficProfileEntry.setIndexNames(
    (0, "ZTE-AN-QOSII-MIB", "zxAnQosIITrafficPrfName"),
)
if mibBuilder.loadTexts:
    zxAnQosIITrafficProfileEntry.setStatus("current")


class _ZxAnQosIITrafficPrfName_Type(DisplayString):
    """Custom type zxAnQosIITrafficPrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnQosIITrafficPrfName_Type.__name__ = "DisplayString"
_ZxAnQosIITrafficPrfName_Object = MibTableColumn
zxAnQosIITrafficPrfName = _ZxAnQosIITrafficPrfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 16, 1, 1),
    _ZxAnQosIITrafficPrfName_Type()
)
zxAnQosIITrafficPrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosIITrafficPrfName.setStatus("current")


class _ZxAnQosIITrafficConfCir_Type(Integer32):
    """Custom type zxAnQosIITrafficConfCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2621440),
    )


_ZxAnQosIITrafficConfCir_Type.__name__ = "Integer32"
_ZxAnQosIITrafficConfCir_Object = MibTableColumn
zxAnQosIITrafficConfCir = _ZxAnQosIITrafficConfCir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 16, 1, 2),
    _ZxAnQosIITrafficConfCir_Type()
)
zxAnQosIITrafficConfCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIITrafficConfCir.setStatus("current")
if mibBuilder.loadTexts:
    zxAnQosIITrafficConfCir.setUnits("kbps")


class _ZxAnQosIITrafficConfCbs_Type(Integer32):
    """Custom type zxAnQosIITrafficConfCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_ZxAnQosIITrafficConfCbs_Type.__name__ = "Integer32"
_ZxAnQosIITrafficConfCbs_Object = MibTableColumn
zxAnQosIITrafficConfCbs = _ZxAnQosIITrafficConfCbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 16, 1, 3),
    _ZxAnQosIITrafficConfCbs_Type()
)
zxAnQosIITrafficConfCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIITrafficConfCbs.setStatus("current")
if mibBuilder.loadTexts:
    zxAnQosIITrafficConfCbs.setUnits("kbytes")


class _ZxAnQosIITrafficConfPir_Type(Integer32):
    """Custom type zxAnQosIITrafficConfPir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2621440),
    )


_ZxAnQosIITrafficConfPir_Type.__name__ = "Integer32"
_ZxAnQosIITrafficConfPir_Object = MibTableColumn
zxAnQosIITrafficConfPir = _ZxAnQosIITrafficConfPir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 16, 1, 4),
    _ZxAnQosIITrafficConfPir_Type()
)
zxAnQosIITrafficConfPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIITrafficConfPir.setStatus("current")
if mibBuilder.loadTexts:
    zxAnQosIITrafficConfPir.setUnits("kbps")


class _ZxAnQosIITrafficConfPbs_Type(Integer32):
    """Custom type zxAnQosIITrafficConfPbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_ZxAnQosIITrafficConfPbs_Type.__name__ = "Integer32"
_ZxAnQosIITrafficConfPbs_Object = MibTableColumn
zxAnQosIITrafficConfPbs = _ZxAnQosIITrafficConfPbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 16, 1, 5),
    _ZxAnQosIITrafficConfPbs_Type()
)
zxAnQosIITrafficConfPbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIITrafficConfPbs.setStatus("current")
if mibBuilder.loadTexts:
    zxAnQosIITrafficConfPbs.setUnits("kbytes")


class _ZxAnQosIITrafficCosPriorityTrust_Type(Integer32):
    """Custom type zxAnQosIITrafficCosPriorityTrust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("override", 1),
          ("trust", 2),
          ("notSupport", 255))
    )


_ZxAnQosIITrafficCosPriorityTrust_Type.__name__ = "Integer32"
_ZxAnQosIITrafficCosPriorityTrust_Object = MibTableColumn
zxAnQosIITrafficCosPriorityTrust = _ZxAnQosIITrafficCosPriorityTrust_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 16, 1, 6),
    _ZxAnQosIITrafficCosPriorityTrust_Type()
)
zxAnQosIITrafficCosPriorityTrust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIITrafficCosPriorityTrust.setStatus("current")


class _ZxAnQosIITrafficCosPriority_Type(Integer32):
    """Custom type zxAnQosIITrafficCosPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_ZxAnQosIITrafficCosPriority_Type.__name__ = "Integer32"
_ZxAnQosIITrafficCosPriority_Object = MibTableColumn
zxAnQosIITrafficCosPriority = _ZxAnQosIITrafficCosPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 16, 1, 7),
    _ZxAnQosIITrafficCosPriority_Type()
)
zxAnQosIITrafficCosPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIITrafficCosPriority.setStatus("current")


class _ZxAnQosIITrafficDiscardMode_Type(Integer32):
    """Custom type zxAnQosIITrafficDiscardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noDistinction", 1),
          ("lowPriorityFirst", 2))
    )


_ZxAnQosIITrafficDiscardMode_Type.__name__ = "Integer32"
_ZxAnQosIITrafficDiscardMode_Object = MibTableColumn
zxAnQosIITrafficDiscardMode = _ZxAnQosIITrafficDiscardMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 16, 1, 8),
    _ZxAnQosIITrafficDiscardMode_Type()
)
zxAnQosIITrafficDiscardMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIITrafficDiscardMode.setStatus("current")
_ZxAnQosIITrafficRowStatus_Type = RowStatus
_ZxAnQosIITrafficRowStatus_Object = MibTableColumn
zxAnQosIITrafficRowStatus = _ZxAnQosIITrafficRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 16, 1, 20),
    _ZxAnQosIITrafficRowStatus_Type()
)
zxAnQosIITrafficRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIITrafficRowStatus.setStatus("current")
_ZxAnQosIIVPortProfileTable_Object = MibTable
zxAnQosIIVPortProfileTable = _ZxAnQosIIVPortProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 17)
)
if mibBuilder.loadTexts:
    zxAnQosIIVPortProfileTable.setStatus("current")
_ZxAnQosIIVPortProfileEntry_Object = MibTableRow
zxAnQosIIVPortProfileEntry = _ZxAnQosIIVPortProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 17, 1)
)
zxAnQosIIVPortProfileEntry.setIndexNames(
    (0, "ZTE-AN-QOSII-MIB", "zxAnQosIIVPortPrfName"),
)
if mibBuilder.loadTexts:
    zxAnQosIIVPortProfileEntry.setStatus("current")


class _ZxAnQosIIVPortPrfName_Type(DisplayString):
    """Custom type zxAnQosIIVPortPrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnQosIIVPortPrfName_Type.__name__ = "DisplayString"
_ZxAnQosIIVPortPrfName_Object = MibTableColumn
zxAnQosIIVPortPrfName = _ZxAnQosIIVPortPrfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 17, 1, 1),
    _ZxAnQosIIVPortPrfName_Type()
)
zxAnQosIIVPortPrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosIIVPortPrfName.setStatus("current")


class _ZxAnQosIIConfCosRemark_Type(DisplayString):
    """Custom type zxAnQosIIConfCosRemark based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnQosIIConfCosRemark_Type.__name__ = "DisplayString"
_ZxAnQosIIConfCosRemark_Object = MibTableColumn
zxAnQosIIConfCosRemark = _ZxAnQosIIConfCosRemark_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 17, 1, 2),
    _ZxAnQosIIConfCosRemark_Type()
)
zxAnQosIIConfCosRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIConfCosRemark.setStatus("current")


class _ZxAnQosIIConfDefCos_Type(Integer32):
    """Custom type zxAnQosIIConfDefCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_ZxAnQosIIConfDefCos_Type.__name__ = "Integer32"
_ZxAnQosIIConfDefCos_Object = MibTableColumn
zxAnQosIIConfDefCos = _ZxAnQosIIConfDefCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 17, 1, 3),
    _ZxAnQosIIConfDefCos_Type()
)
zxAnQosIIConfDefCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIConfDefCos.setStatus("current")


class _ZxAnQosIIConfDefCtagCos_Type(Integer32):
    """Custom type zxAnQosIIConfDefCtagCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_ZxAnQosIIConfDefCtagCos_Type.__name__ = "Integer32"
_ZxAnQosIIConfDefCtagCos_Object = MibTableColumn
zxAnQosIIConfDefCtagCos = _ZxAnQosIIConfDefCtagCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 17, 1, 4),
    _ZxAnQosIIConfDefCtagCos_Type()
)
zxAnQosIIConfDefCtagCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIConfDefCtagCos.setStatus("current")


class _ZxAnQosIIConfCosFilter_Type(Integer32):
    """Custom type zxAnQosIIConfCosFilter based on Integer32"""
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


_ZxAnQosIIConfCosFilter_Type.__name__ = "Integer32"
_ZxAnQosIIConfCosFilter_Object = MibTableColumn
zxAnQosIIConfCosFilter = _ZxAnQosIIConfCosFilter_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 17, 1, 5),
    _ZxAnQosIIConfCosFilter_Type()
)
zxAnQosIIConfCosFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIConfCosFilter.setStatus("current")


class _ZxAnQosIIConfCosMode_Type(Integer32):
    """Custom type zxAnQosIIConfCosMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("trust", 1),
          ("override", 2),
          ("remark", 3),
          ("trustDscpMap", 4),
          ("notsupport", 255))
    )


_ZxAnQosIIConfCosMode_Type.__name__ = "Integer32"
_ZxAnQosIIConfCosMode_Object = MibTableColumn
zxAnQosIIConfCosMode = _ZxAnQosIIConfCosMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 17, 1, 6),
    _ZxAnQosIIConfCosMode_Type()
)
zxAnQosIIConfCosMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIConfCosMode.setStatus("current")


class _ZxAnQosIIConfCtagCosMode_Type(Integer32):
    """Custom type zxAnQosIIConfCtagCosMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("trust", 1),
          ("override", 2),
          ("remark", 3),
          ("trustDscpMap", 4),
          ("notsupport", 255))
    )


_ZxAnQosIIConfCtagCosMode_Type.__name__ = "Integer32"
_ZxAnQosIIConfCtagCosMode_Object = MibTableColumn
zxAnQosIIConfCtagCosMode = _ZxAnQosIIConfCtagCosMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 17, 1, 7),
    _ZxAnQosIIConfCtagCosMode_Type()
)
zxAnQosIIConfCtagCosMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIConfCtagCosMode.setStatus("current")


class _ZxAnQosIIConfDscpMode_Type(Integer32):
    """Custom type zxAnQosIIConfDscpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("trust", 1),
          ("trustCosMap", 2),
          ("notsupport", 255))
    )


_ZxAnQosIIConfDscpMode_Type.__name__ = "Integer32"
_ZxAnQosIIConfDscpMode_Object = MibTableColumn
zxAnQosIIConfDscpMode = _ZxAnQosIIConfDscpMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 17, 1, 8),
    _ZxAnQosIIConfDscpMode_Type()
)
zxAnQosIIConfDscpMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIConfDscpMode.setStatus("current")


class _ZxAnQosIIConfDefScos_Type(Integer32):
    """Custom type zxAnQosIIConfDefScos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_ZxAnQosIIConfDefScos_Type.__name__ = "Integer32"
_ZxAnQosIIConfDefScos_Object = MibTableColumn
zxAnQosIIConfDefScos = _ZxAnQosIIConfDefScos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 17, 1, 9),
    _ZxAnQosIIConfDefScos_Type()
)
zxAnQosIIConfDefScos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIConfDefScos.setStatus("current")


class _ZxAnQosIIConfIngressCosMode_Type(Integer32):
    """Custom type zxAnQosIIConfIngressCosMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("trust", 1),
          ("scosOverride", 2),
          ("scosRemark", 3),
          ("ccosScosRemark", 4),
          ("ccosScosOverride", 5),
          ("notSupport", 255))
    )


_ZxAnQosIIConfIngressCosMode_Type.__name__ = "Integer32"
_ZxAnQosIIConfIngressCosMode_Object = MibTableColumn
zxAnQosIIConfIngressCosMode = _ZxAnQosIIConfIngressCosMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 17, 1, 10),
    _ZxAnQosIIConfIngressCosMode_Type()
)
zxAnQosIIConfIngressCosMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIConfIngressCosMode.setStatus("current")


class _ZxAnQosIIConfEgressCosMode_Type(Integer32):
    """Custom type zxAnQosIIConfEgressCosMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("trust", 1),
          ("remark", 2),
          ("trustDscpMap", 3),
          ("notSupport", 255))
    )


_ZxAnQosIIConfEgressCosMode_Type.__name__ = "Integer32"
_ZxAnQosIIConfEgressCosMode_Object = MibTableColumn
zxAnQosIIConfEgressCosMode = _ZxAnQosIIConfEgressCosMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 17, 1, 11),
    _ZxAnQosIIConfEgressCosMode_Type()
)
zxAnQosIIConfEgressCosMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIConfEgressCosMode.setStatus("current")


class _ZxAnQosIIConfIngressDscpMode_Type(Integer32):
    """Custom type zxAnQosIIConfIngressDscpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("trust", 1),
          ("trustCosMap", 2),
          ("notSupport", 255))
    )


_ZxAnQosIIConfIngressDscpMode_Type.__name__ = "Integer32"
_ZxAnQosIIConfIngressDscpMode_Object = MibTableColumn
zxAnQosIIConfIngressDscpMode = _ZxAnQosIIConfIngressDscpMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 17, 1, 12),
    _ZxAnQosIIConfIngressDscpMode_Type()
)
zxAnQosIIConfIngressDscpMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIConfIngressDscpMode.setStatus("current")


class _ZxAnQosIIVPortPrfType_Type(Integer32):
    """Custom type zxAnQosIIVPortPrfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pon", 1),
          ("dsl", 2))
    )


_ZxAnQosIIVPortPrfType_Type.__name__ = "Integer32"
_ZxAnQosIIVPortPrfType_Object = MibTableColumn
zxAnQosIIVPortPrfType = _ZxAnQosIIVPortPrfType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 17, 1, 13),
    _ZxAnQosIIVPortPrfType_Type()
)
zxAnQosIIVPortPrfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIVPortPrfType.setStatus("current")


class _ZxAnQosIIConfEgressCosRemark_Type(DisplayString):
    """Custom type zxAnQosIIConfEgressCosRemark based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnQosIIConfEgressCosRemark_Type.__name__ = "DisplayString"
_ZxAnQosIIConfEgressCosRemark_Object = MibTableColumn
zxAnQosIIConfEgressCosRemark = _ZxAnQosIIConfEgressCosRemark_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 17, 1, 14),
    _ZxAnQosIIConfEgressCosRemark_Type()
)
zxAnQosIIConfEgressCosRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIConfEgressCosRemark.setStatus("current")
_ZxAnQosIIVPortPrfRowStatus_Type = RowStatus
_ZxAnQosIIVPortPrfRowStatus_Object = MibTableColumn
zxAnQosIIVPortPrfRowStatus = _ZxAnQosIIVPortPrfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 17, 1, 20),
    _ZxAnQosIIVPortPrfRowStatus_Type()
)
zxAnQosIIVPortPrfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIVPortPrfRowStatus.setStatus("current")
_ZxAnQosIIPortCfgTable_Object = MibTable
zxAnQosIIPortCfgTable = _ZxAnQosIIPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 21)
)
if mibBuilder.loadTexts:
    zxAnQosIIPortCfgTable.setStatus("current")
_ZxAnQosIIPortCfgEntry_Object = MibTableRow
zxAnQosIIPortCfgEntry = _ZxAnQosIIPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 21, 1)
)
zxAnQosIIPortCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnQosIIPortCfgEntry.setStatus("current")


class _ZxAnQosIICosQueuePrf_Type(DisplayString):
    """Custom type zxAnQosIICosQueuePrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnQosIICosQueuePrf_Type.__name__ = "DisplayString"
_ZxAnQosIICosQueuePrf_Object = MibTableColumn
zxAnQosIICosQueuePrf = _ZxAnQosIICosQueuePrf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 21, 1, 1),
    _ZxAnQosIICosQueuePrf_Type()
)
zxAnQosIICosQueuePrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIICosQueuePrf.setStatus("current")


class _ZxAnQosIIQueueBlockPrf_Type(DisplayString):
    """Custom type zxAnQosIIQueueBlockPrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnQosIIQueueBlockPrf_Type.__name__ = "DisplayString"
_ZxAnQosIIQueueBlockPrf_Object = MibTableColumn
zxAnQosIIQueueBlockPrf = _ZxAnQosIIQueueBlockPrf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 21, 1, 2),
    _ZxAnQosIIQueueBlockPrf_Type()
)
zxAnQosIIQueueBlockPrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIQueueBlockPrf.setStatus("current")


class _ZxAnQosIICosRemarkPrf_Type(DisplayString):
    """Custom type zxAnQosIICosRemarkPrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnQosIICosRemarkPrf_Type.__name__ = "DisplayString"
_ZxAnQosIICosRemarkPrf_Object = MibTableColumn
zxAnQosIICosRemarkPrf = _ZxAnQosIICosRemarkPrf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 21, 1, 3),
    _ZxAnQosIICosRemarkPrf_Type()
)
zxAnQosIICosRemarkPrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIICosRemarkPrf.setStatus("current")
_ZxAnQosIIVPortCfgTable_Object = MibTable
zxAnQosIIVPortCfgTable = _ZxAnQosIIVPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 22)
)
if mibBuilder.loadTexts:
    zxAnQosIIVPortCfgTable.setStatus("current")
_ZxAnQosIIVPortCfgEntry_Object = MibTableRow
zxAnQosIIVPortCfgEntry = _ZxAnQosIIVPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 22, 1)
)
zxAnQosIIVPortCfgEntry.setIndexNames(
    (0, "ZTE-AN-QOSII-MIB", "zxAnQosIIRack"),
    (0, "ZTE-AN-QOSII-MIB", "zxAnQosIIShelf"),
    (0, "ZTE-AN-QOSII-MIB", "zxAnQosIISlot"),
    (0, "ZTE-AN-QOSII-MIB", "zxAnQosIIPort"),
    (0, "ZTE-AN-QOSII-MIB", "zxAnQosIIOnu"),
    (0, "ZTE-AN-QOSII-MIB", "zxAnQosIIVCircuitType"),
    (0, "ZTE-AN-QOSII-MIB", "zxAnQosIILogicalId"),
)
if mibBuilder.loadTexts:
    zxAnQosIIVPortCfgEntry.setStatus("current")
_ZxAnQosIIRack_Type = Integer32
_ZxAnQosIIRack_Object = MibTableColumn
zxAnQosIIRack = _ZxAnQosIIRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 22, 1, 1),
    _ZxAnQosIIRack_Type()
)
zxAnQosIIRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosIIRack.setStatus("current")
_ZxAnQosIIShelf_Type = Integer32
_ZxAnQosIIShelf_Object = MibTableColumn
zxAnQosIIShelf = _ZxAnQosIIShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 22, 1, 2),
    _ZxAnQosIIShelf_Type()
)
zxAnQosIIShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosIIShelf.setStatus("current")
_ZxAnQosIISlot_Type = Integer32
_ZxAnQosIISlot_Object = MibTableColumn
zxAnQosIISlot = _ZxAnQosIISlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 22, 1, 3),
    _ZxAnQosIISlot_Type()
)
zxAnQosIISlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosIISlot.setStatus("current")
_ZxAnQosIIPort_Type = Integer32
_ZxAnQosIIPort_Object = MibTableColumn
zxAnQosIIPort = _ZxAnQosIIPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 22, 1, 4),
    _ZxAnQosIIPort_Type()
)
zxAnQosIIPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosIIPort.setStatus("current")
_ZxAnQosIIOnu_Type = Integer32
_ZxAnQosIIOnu_Object = MibTableColumn
zxAnQosIIOnu = _ZxAnQosIIOnu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 22, 1, 5),
    _ZxAnQosIIOnu_Type()
)
zxAnQosIIOnu.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosIIOnu.setStatus("current")


class _ZxAnQosIIVCircuitType_Type(Integer32):
    """Custom type zxAnQosIIVCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("physicalport", 1),
          ("bridgeport", 2),
          ("epononu", 3),
          ("gpon", 4),
          ("serviceport", 11),
          ("vlan", 12))
    )


_ZxAnQosIIVCircuitType_Type.__name__ = "Integer32"
_ZxAnQosIIVCircuitType_Object = MibTableColumn
zxAnQosIIVCircuitType = _ZxAnQosIIVCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 22, 1, 6),
    _ZxAnQosIIVCircuitType_Type()
)
zxAnQosIIVCircuitType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosIIVCircuitType.setStatus("current")
_ZxAnQosIILogicalId_Type = Integer32
_ZxAnQosIILogicalId_Object = MibTableColumn
zxAnQosIILogicalId = _ZxAnQosIILogicalId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 22, 1, 7),
    _ZxAnQosIILogicalId_Type()
)
zxAnQosIILogicalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosIILogicalId.setStatus("current")


class _ZxAnQosIIVPortCfgPrf_Type(DisplayString):
    """Custom type zxAnQosIIVPortCfgPrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnQosIIVPortCfgPrf_Type.__name__ = "DisplayString"
_ZxAnQosIIVPortCfgPrf_Object = MibTableColumn
zxAnQosIIVPortCfgPrf = _ZxAnQosIIVPortCfgPrf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 22, 1, 8),
    _ZxAnQosIIVPortCfgPrf_Type()
)
zxAnQosIIVPortCfgPrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIVPortCfgPrf.setStatus("current")


class _ZxAnQosIIVPortMapQueue_Type(Integer32):
    """Custom type zxAnQosIIVPortMapQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ZxAnQosIIVPortMapQueue_Type.__name__ = "Integer32"
_ZxAnQosIIVPortMapQueue_Object = MibTableColumn
zxAnQosIIVPortMapQueue = _ZxAnQosIIVPortMapQueue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 22, 1, 9),
    _ZxAnQosIIVPortMapQueue_Type()
)
zxAnQosIIVPortMapQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIVPortMapQueue.setStatus("current")


class _ZxAnQosIIVPortServiceCategory_Type(Integer32):
    """Custom type zxAnQosIIVPortServiceCategory based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 1),
          ("ubr", 2),
          ("vbr", 3),
          ("unconfigured", 255))
    )


_ZxAnQosIIVPortServiceCategory_Type.__name__ = "Integer32"
_ZxAnQosIIVPortServiceCategory_Object = MibTableColumn
zxAnQosIIVPortServiceCategory = _ZxAnQosIIVPortServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 22, 1, 10),
    _ZxAnQosIIVPortServiceCategory_Type()
)
zxAnQosIIVPortServiceCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIVPortServiceCategory.setStatus("current")


class _ZxAnQosIIVPortPcr_Type(Integer32):
    """Custom type zxAnQosIIVPortPcr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20480),
    )


_ZxAnQosIIVPortPcr_Type.__name__ = "Integer32"
_ZxAnQosIIVPortPcr_Object = MibTableColumn
zxAnQosIIVPortPcr = _ZxAnQosIIVPortPcr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 22, 1, 11),
    _ZxAnQosIIVPortPcr_Type()
)
zxAnQosIIVPortPcr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIVPortPcr.setStatus("current")
if mibBuilder.loadTexts:
    zxAnQosIIVPortPcr.setUnits("kbps")


class _ZxAnQosIIVPortMcr_Type(Integer32):
    """Custom type zxAnQosIIVPortMcr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20480),
    )


_ZxAnQosIIVPortMcr_Type.__name__ = "Integer32"
_ZxAnQosIIVPortMcr_Object = MibTableColumn
zxAnQosIIVPortMcr = _ZxAnQosIIVPortMcr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 22, 1, 12),
    _ZxAnQosIIVPortMcr_Type()
)
zxAnQosIIVPortMcr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIVPortMcr.setStatus("current")
if mibBuilder.loadTexts:
    zxAnQosIIVPortMcr.setUnits("kbps")


class _ZxAnQosIIVPortScr_Type(Integer32):
    """Custom type zxAnQosIIVPortScr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20480),
    )


_ZxAnQosIIVPortScr_Type.__name__ = "Integer32"
_ZxAnQosIIVPortScr_Object = MibTableColumn
zxAnQosIIVPortScr = _ZxAnQosIIVPortScr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 22, 1, 13),
    _ZxAnQosIIVPortScr_Type()
)
zxAnQosIIVPortScr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIVPortScr.setStatus("current")
if mibBuilder.loadTexts:
    zxAnQosIIVPortScr.setUnits("kbps")


class _ZxAnQosIIVPortPcrRemarkCos_Type(Integer32):
    """Custom type zxAnQosIIVPortPcrRemarkCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_ZxAnQosIIVPortPcrRemarkCos_Type.__name__ = "Integer32"
_ZxAnQosIIVPortPcrRemarkCos_Object = MibTableColumn
zxAnQosIIVPortPcrRemarkCos = _ZxAnQosIIVPortPcrRemarkCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 22, 1, 14),
    _ZxAnQosIIVPortPcrRemarkCos_Type()
)
zxAnQosIIVPortPcrRemarkCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIVPortPcrRemarkCos.setStatus("current")


class _ZxAnQosIIVPortMcrRemarkCos_Type(Integer32):
    """Custom type zxAnQosIIVPortMcrRemarkCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_ZxAnQosIIVPortMcrRemarkCos_Type.__name__ = "Integer32"
_ZxAnQosIIVPortMcrRemarkCos_Object = MibTableColumn
zxAnQosIIVPortMcrRemarkCos = _ZxAnQosIIVPortMcrRemarkCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 22, 1, 15),
    _ZxAnQosIIVPortMcrRemarkCos_Type()
)
zxAnQosIIVPortMcrRemarkCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIVPortMcrRemarkCos.setStatus("current")


class _ZxAnQosIIVPortScrRemarkCos_Type(Integer32):
    """Custom type zxAnQosIIVPortScrRemarkCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_ZxAnQosIIVPortScrRemarkCos_Type.__name__ = "Integer32"
_ZxAnQosIIVPortScrRemarkCos_Object = MibTableColumn
zxAnQosIIVPortScrRemarkCos = _ZxAnQosIIVPortScrRemarkCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 22, 1, 16),
    _ZxAnQosIIVPortScrRemarkCos_Type()
)
zxAnQosIIVPortScrRemarkCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIVPortScrRemarkCos.setStatus("current")
_ZxAnQosIITrafficCfgTable_Object = MibTable
zxAnQosIITrafficCfgTable = _ZxAnQosIITrafficCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 23)
)
if mibBuilder.loadTexts:
    zxAnQosIITrafficCfgTable.setStatus("current")
_ZxAnQosIITrafficCfgEntry_Object = MibTableRow
zxAnQosIITrafficCfgEntry = _ZxAnQosIITrafficCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 23, 1)
)
zxAnQosIITrafficCfgEntry.setIndexNames(
    (0, "ZTE-AN-QOSII-MIB", "zxAnQosIITrafficRack"),
    (0, "ZTE-AN-QOSII-MIB", "zxAnQosIITrafficShelf"),
    (0, "ZTE-AN-QOSII-MIB", "zxAnQosIITrafficSlot"),
    (0, "ZTE-AN-QOSII-MIB", "zxAnQosIITrafficPort"),
    (0, "ZTE-AN-QOSII-MIB", "zxAnQosIITrafficOnu"),
    (0, "ZTE-AN-QOSII-MIB", "zxAnQosIITrafficVCircuitType"),
    (0, "ZTE-AN-QOSII-MIB", "zxAnQosIITrafficLogicalId"),
    (0, "ZTE-AN-QOSII-MIB", "zxAnQosIITrafficDirection"),
)
if mibBuilder.loadTexts:
    zxAnQosIITrafficCfgEntry.setStatus("current")
_ZxAnQosIITrafficRack_Type = Integer32
_ZxAnQosIITrafficRack_Object = MibTableColumn
zxAnQosIITrafficRack = _ZxAnQosIITrafficRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 23, 1, 1),
    _ZxAnQosIITrafficRack_Type()
)
zxAnQosIITrafficRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosIITrafficRack.setStatus("current")
_ZxAnQosIITrafficShelf_Type = Integer32
_ZxAnQosIITrafficShelf_Object = MibTableColumn
zxAnQosIITrafficShelf = _ZxAnQosIITrafficShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 23, 1, 2),
    _ZxAnQosIITrafficShelf_Type()
)
zxAnQosIITrafficShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosIITrafficShelf.setStatus("current")
_ZxAnQosIITrafficSlot_Type = Integer32
_ZxAnQosIITrafficSlot_Object = MibTableColumn
zxAnQosIITrafficSlot = _ZxAnQosIITrafficSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 23, 1, 3),
    _ZxAnQosIITrafficSlot_Type()
)
zxAnQosIITrafficSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosIITrafficSlot.setStatus("current")
_ZxAnQosIITrafficPort_Type = Integer32
_ZxAnQosIITrafficPort_Object = MibTableColumn
zxAnQosIITrafficPort = _ZxAnQosIITrafficPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 23, 1, 4),
    _ZxAnQosIITrafficPort_Type()
)
zxAnQosIITrafficPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosIITrafficPort.setStatus("current")
_ZxAnQosIITrafficOnu_Type = Integer32
_ZxAnQosIITrafficOnu_Object = MibTableColumn
zxAnQosIITrafficOnu = _ZxAnQosIITrafficOnu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 23, 1, 5),
    _ZxAnQosIITrafficOnu_Type()
)
zxAnQosIITrafficOnu.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosIITrafficOnu.setStatus("current")


class _ZxAnQosIITrafficVCircuitType_Type(Integer32):
    """Custom type zxAnQosIITrafficVCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("physicalport", 1),
          ("bridgeport", 2),
          ("epononu", 3),
          ("gpon", 4),
          ("serviceport", 11),
          ("vlan", 12))
    )


_ZxAnQosIITrafficVCircuitType_Type.__name__ = "Integer32"
_ZxAnQosIITrafficVCircuitType_Object = MibTableColumn
zxAnQosIITrafficVCircuitType = _ZxAnQosIITrafficVCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 23, 1, 6),
    _ZxAnQosIITrafficVCircuitType_Type()
)
zxAnQosIITrafficVCircuitType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosIITrafficVCircuitType.setStatus("current")
_ZxAnQosIITrafficLogicalId_Type = ObjectIdentifier
_ZxAnQosIITrafficLogicalId_Object = MibTableColumn
zxAnQosIITrafficLogicalId = _ZxAnQosIITrafficLogicalId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 23, 1, 7),
    _ZxAnQosIITrafficLogicalId_Type()
)
zxAnQosIITrafficLogicalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosIITrafficLogicalId.setStatus("current")


class _ZxAnQosIITrafficDirection_Type(Integer32):
    """Custom type zxAnQosIITrafficDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2))
    )


_ZxAnQosIITrafficDirection_Type.__name__ = "Integer32"
_ZxAnQosIITrafficDirection_Object = MibTableColumn
zxAnQosIITrafficDirection = _ZxAnQosIITrafficDirection_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 23, 1, 8),
    _ZxAnQosIITrafficDirection_Type()
)
zxAnQosIITrafficDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosIITrafficDirection.setStatus("current")


class _ZxAnQosIITrafficSvcEncapType_Type(Integer32):
    """Custom type zxAnQosIITrafficSvcEncapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("pppoe", 1),
          ("ipoe", 2),
          ("all", 3),
          ("notsupport", 255))
    )


_ZxAnQosIITrafficSvcEncapType_Type.__name__ = "Integer32"
_ZxAnQosIITrafficSvcEncapType_Object = MibTableColumn
zxAnQosIITrafficSvcEncapType = _ZxAnQosIITrafficSvcEncapType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 23, 1, 9),
    _ZxAnQosIITrafficSvcEncapType_Type()
)
zxAnQosIITrafficSvcEncapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIITrafficSvcEncapType.setStatus("current")
_ZxAnQosIITrafficPrf_Type = DisplayString
_ZxAnQosIITrafficPrf_Object = MibTableColumn
zxAnQosIITrafficPrf = _ZxAnQosIITrafficPrf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 23, 1, 10),
    _ZxAnQosIITrafficPrf_Type()
)
zxAnQosIITrafficPrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIITrafficPrf.setStatus("current")
_ZxAnQosIITrafficCfgRowStatus_Type = RowStatus
_ZxAnQosIITrafficCfgRowStatus_Object = MibTableColumn
zxAnQosIITrafficCfgRowStatus = _ZxAnQosIITrafficCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 23, 1, 20),
    _ZxAnQosIITrafficCfgRowStatus_Type()
)
zxAnQosIITrafficCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIITrafficCfgRowStatus.setStatus("current")
_ZxAnQosIITrafficBandwidthTable_Object = MibTable
zxAnQosIITrafficBandwidthTable = _ZxAnQosIITrafficBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 24)
)
if mibBuilder.loadTexts:
    zxAnQosIITrafficBandwidthTable.setStatus("current")
_ZxAnQosIITrafficBandwidthEntry_Object = MibTableRow
zxAnQosIITrafficBandwidthEntry = _ZxAnQosIITrafficBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 24, 1)
)
zxAnQosIITrafficBandwidthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnQosIITrafficBandwidthEntry.setStatus("current")
_ZxAnQosIITrafficTotalBandwidth_Type = Integer32
_ZxAnQosIITrafficTotalBandwidth_Object = MibTableColumn
zxAnQosIITrafficTotalBandwidth = _ZxAnQosIITrafficTotalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 24, 1, 1),
    _ZxAnQosIITrafficTotalBandwidth_Type()
)
zxAnQosIITrafficTotalBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnQosIITrafficTotalBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    zxAnQosIITrafficTotalBandwidth.setUnits("kbps")
_ZxAnQosIITrafficRemainBandwidth_Type = Integer32
_ZxAnQosIITrafficRemainBandwidth_Object = MibTableColumn
zxAnQosIITrafficRemainBandwidth = _ZxAnQosIITrafficRemainBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 24, 1, 2),
    _ZxAnQosIITrafficRemainBandwidth_Type()
)
zxAnQosIITrafficRemainBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnQosIITrafficRemainBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    zxAnQosIITrafficRemainBandwidth.setUnits("kbps")
_ZxAnQosIIMVlan2CosTable_Object = MibTable
zxAnQosIIMVlan2CosTable = _ZxAnQosIIMVlan2CosTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 25)
)
if mibBuilder.loadTexts:
    zxAnQosIIMVlan2CosTable.setStatus("current")
_ZxAnQosIIMVlan2CosEntry_Object = MibTableRow
zxAnQosIIMVlan2CosEntry = _ZxAnQosIIMVlan2CosEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 25, 1)
)
zxAnQosIIMVlan2CosEntry.setIndexNames(
    (0, "ZTE-AN-QOSII-MIB", "zxAnQosIIMVlan2CosMVlanValue"),
)
if mibBuilder.loadTexts:
    zxAnQosIIMVlan2CosEntry.setStatus("current")


class _ZxAnQosIIMVlan2CosMVlanValue_Type(Integer32):
    """Custom type zxAnQosIIMVlan2CosMVlanValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_ZxAnQosIIMVlan2CosMVlanValue_Type.__name__ = "Integer32"
_ZxAnQosIIMVlan2CosMVlanValue_Object = MibTableColumn
zxAnQosIIMVlan2CosMVlanValue = _ZxAnQosIIMVlan2CosMVlanValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 25, 1, 1),
    _ZxAnQosIIMVlan2CosMVlanValue_Type()
)
zxAnQosIIMVlan2CosMVlanValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnQosIIMVlan2CosMVlanValue.setStatus("current")


class _ZxAnQosIIMVlan2CosCosValue_Type(Integer32):
    """Custom type zxAnQosIIMVlan2CosCosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnQosIIMVlan2CosCosValue_Type.__name__ = "Integer32"
_ZxAnQosIIMVlan2CosCosValue_Object = MibTableColumn
zxAnQosIIMVlan2CosCosValue = _ZxAnQosIIMVlan2CosCosValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 25, 1, 2),
    _ZxAnQosIIMVlan2CosCosValue_Type()
)
zxAnQosIIMVlan2CosCosValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIMVlan2CosCosValue.setStatus("current")
_ZxAnQosIIMVlan2CosRowStatus_Type = RowStatus
_ZxAnQosIIMVlan2CosRowStatus_Object = MibTableColumn
zxAnQosIIMVlan2CosRowStatus = _ZxAnQosIIMVlan2CosRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 21, 3, 25, 1, 20),
    _ZxAnQosIIMVlan2CosRowStatus_Type()
)
zxAnQosIIMVlan2CosRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnQosIIMVlan2CosRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-QOSII-MIB",
    **{"zxAnQosMib": zxAnQosMib,
       "zxAnQosIIObjects": zxAnQosIIObjects,
       "zxAnQosIINniCos2DropMap": zxAnQosIINniCos2DropMap,
       "zxAnQosIINniCos2LocalMap": zxAnQosIINniCos2LocalMap,
       "zxAnQosIINniDscpMappingTable": zxAnQosIINniDscpMappingTable,
       "zxAnQosIINniDscpMappingEntry": zxAnQosIINniDscpMappingEntry,
       "zxAnQosIINniIngressDscp": zxAnQosIINniIngressDscp,
       "zxAnQosIINniEgressDscp": zxAnQosIINniEgressDscp,
       "zxAnQosIINniEgressCos": zxAnQosIINniEgressCos,
       "zxAnQosIINniEgressDropPrecedence": zxAnQosIINniEgressDropPrecedence,
       "zxAnQosIINniPortCfgTable": zxAnQosIINniPortCfgTable,
       "zxAnQosIINniPortCfgEntry": zxAnQosIINniPortCfgEntry,
       "zxAnQosIINniDefPriority": zxAnQosIINniDefPriority,
       "zxAnQosIINniTrustDscp": zxAnQosIINniTrustDscp,
       "zxAnQosIINniTrustCos": zxAnQosIINniTrustCos,
       "zxAnQosIINniQueuesAlgorithm": zxAnQosIINniQueuesAlgorithm,
       "zxAnQosIINniQueuesWeight": zxAnQosIINniQueuesWeight,
       "zxAnQosIINniQueuesMinRate": zxAnQosIINniQueuesMinRate,
       "zxAnQosIINniQueuesMaxRate": zxAnQosIINniQueuesMaxRate,
       "zxAnQosIINniShapeRateLimit": zxAnQosIINniShapeRateLimit,
       "zxAnQosIINniShapeBurstSize": zxAnQosIINniShapeBurstSize,
       "zxAnQosIINniQueuesDepth": zxAnQosIINniQueuesDepth,
       "zxAnQosIINniGlobal": zxAnQosIINniGlobal,
       "zxAnQosIINniGlobalTrustMode": zxAnQosIINniGlobalTrustMode,
       "zxAnQosIICos2DscpTable": zxAnQosIICos2DscpTable,
       "zxAnQosIICos2DscpEntry": zxAnQosIICos2DscpEntry,
       "zxAnQosIICos2DscpCosValue": zxAnQosIICos2DscpCosValue,
       "zxAnQosIICos2DscpDscpValue": zxAnQosIICos2DscpDscpValue,
       "zxAnQosIIDscp2CosTable": zxAnQosIIDscp2CosTable,
       "zxAnQosIIDscp2CosEntry": zxAnQosIIDscp2CosEntry,
       "zxAnQosIIDscp2CosDscpValue": zxAnQosIIDscp2CosDscpValue,
       "zxAnQosIIDscp2CosCosValue": zxAnQosIIDscp2CosCosValue,
       "zxAnQosIICos2QueuesProfileTable": zxAnQosIICos2QueuesProfileTable,
       "zxAnQosIICos2QueuesProfileEntry": zxAnQosIICos2QueuesProfileEntry,
       "zxAnQosIICos2QueuesPrfName": zxAnQosIICos2QueuesPrfName,
       "zxAnQosIICos2Queues": zxAnQosIICos2Queues,
       "zxAnQosIIDropPrecedence": zxAnQosIIDropPrecedence,
       "zxAnQosIICos2QueuesRowStatus": zxAnQosIICos2QueuesRowStatus,
       "zxAnQosIIQueuesBlockProfileTable": zxAnQosIIQueuesBlockProfileTable,
       "zxAnQosIIQueuesBlockProfileEntry": zxAnQosIIQueuesBlockProfileEntry,
       "zxAnQosIIQueuesBlockPrfName": zxAnQosIIQueuesBlockPrfName,
       "zxAnQosIIQueuesPriority": zxAnQosIIQueuesPriority,
       "zxAnQosIIQueuesWeight": zxAnQosIIQueuesWeight,
       "zxAnQosIIQueuesDepth": zxAnQosIIQueuesDepth,
       "zxAnQosIIQueuesBlockRowStatus": zxAnQosIIQueuesBlockRowStatus,
       "zxAnQosIICosRemarkProfileTable": zxAnQosIICosRemarkProfileTable,
       "zxAnQosIICosRemarkProfileEntry": zxAnQosIICosRemarkProfileEntry,
       "zxAnQosIICosRemarkPrfName": zxAnQosIICosRemarkPrfName,
       "zxAnQosIIEgressPriority": zxAnQosIIEgressPriority,
       "zxAnQosIICosRemarkRowStatus": zxAnQosIICosRemarkRowStatus,
       "zxAnQosIITrafficProfileTable": zxAnQosIITrafficProfileTable,
       "zxAnQosIITrafficProfileEntry": zxAnQosIITrafficProfileEntry,
       "zxAnQosIITrafficPrfName": zxAnQosIITrafficPrfName,
       "zxAnQosIITrafficConfCir": zxAnQosIITrafficConfCir,
       "zxAnQosIITrafficConfCbs": zxAnQosIITrafficConfCbs,
       "zxAnQosIITrafficConfPir": zxAnQosIITrafficConfPir,
       "zxAnQosIITrafficConfPbs": zxAnQosIITrafficConfPbs,
       "zxAnQosIITrafficCosPriorityTrust": zxAnQosIITrafficCosPriorityTrust,
       "zxAnQosIITrafficCosPriority": zxAnQosIITrafficCosPriority,
       "zxAnQosIITrafficDiscardMode": zxAnQosIITrafficDiscardMode,
       "zxAnQosIITrafficRowStatus": zxAnQosIITrafficRowStatus,
       "zxAnQosIIVPortProfileTable": zxAnQosIIVPortProfileTable,
       "zxAnQosIIVPortProfileEntry": zxAnQosIIVPortProfileEntry,
       "zxAnQosIIVPortPrfName": zxAnQosIIVPortPrfName,
       "zxAnQosIIConfCosRemark": zxAnQosIIConfCosRemark,
       "zxAnQosIIConfDefCos": zxAnQosIIConfDefCos,
       "zxAnQosIIConfDefCtagCos": zxAnQosIIConfDefCtagCos,
       "zxAnQosIIConfCosFilter": zxAnQosIIConfCosFilter,
       "zxAnQosIIConfCosMode": zxAnQosIIConfCosMode,
       "zxAnQosIIConfCtagCosMode": zxAnQosIIConfCtagCosMode,
       "zxAnQosIIConfDscpMode": zxAnQosIIConfDscpMode,
       "zxAnQosIIConfDefScos": zxAnQosIIConfDefScos,
       "zxAnQosIIConfIngressCosMode": zxAnQosIIConfIngressCosMode,
       "zxAnQosIIConfEgressCosMode": zxAnQosIIConfEgressCosMode,
       "zxAnQosIIConfIngressDscpMode": zxAnQosIIConfIngressDscpMode,
       "zxAnQosIIVPortPrfType": zxAnQosIIVPortPrfType,
       "zxAnQosIIConfEgressCosRemark": zxAnQosIIConfEgressCosRemark,
       "zxAnQosIIVPortPrfRowStatus": zxAnQosIIVPortPrfRowStatus,
       "zxAnQosIIPortCfgTable": zxAnQosIIPortCfgTable,
       "zxAnQosIIPortCfgEntry": zxAnQosIIPortCfgEntry,
       "zxAnQosIICosQueuePrf": zxAnQosIICosQueuePrf,
       "zxAnQosIIQueueBlockPrf": zxAnQosIIQueueBlockPrf,
       "zxAnQosIICosRemarkPrf": zxAnQosIICosRemarkPrf,
       "zxAnQosIIVPortCfgTable": zxAnQosIIVPortCfgTable,
       "zxAnQosIIVPortCfgEntry": zxAnQosIIVPortCfgEntry,
       "zxAnQosIIRack": zxAnQosIIRack,
       "zxAnQosIIShelf": zxAnQosIIShelf,
       "zxAnQosIISlot": zxAnQosIISlot,
       "zxAnQosIIPort": zxAnQosIIPort,
       "zxAnQosIIOnu": zxAnQosIIOnu,
       "zxAnQosIIVCircuitType": zxAnQosIIVCircuitType,
       "zxAnQosIILogicalId": zxAnQosIILogicalId,
       "zxAnQosIIVPortCfgPrf": zxAnQosIIVPortCfgPrf,
       "zxAnQosIIVPortMapQueue": zxAnQosIIVPortMapQueue,
       "zxAnQosIIVPortServiceCategory": zxAnQosIIVPortServiceCategory,
       "zxAnQosIIVPortPcr": zxAnQosIIVPortPcr,
       "zxAnQosIIVPortMcr": zxAnQosIIVPortMcr,
       "zxAnQosIIVPortScr": zxAnQosIIVPortScr,
       "zxAnQosIIVPortPcrRemarkCos": zxAnQosIIVPortPcrRemarkCos,
       "zxAnQosIIVPortMcrRemarkCos": zxAnQosIIVPortMcrRemarkCos,
       "zxAnQosIIVPortScrRemarkCos": zxAnQosIIVPortScrRemarkCos,
       "zxAnQosIITrafficCfgTable": zxAnQosIITrafficCfgTable,
       "zxAnQosIITrafficCfgEntry": zxAnQosIITrafficCfgEntry,
       "zxAnQosIITrafficRack": zxAnQosIITrafficRack,
       "zxAnQosIITrafficShelf": zxAnQosIITrafficShelf,
       "zxAnQosIITrafficSlot": zxAnQosIITrafficSlot,
       "zxAnQosIITrafficPort": zxAnQosIITrafficPort,
       "zxAnQosIITrafficOnu": zxAnQosIITrafficOnu,
       "zxAnQosIITrafficVCircuitType": zxAnQosIITrafficVCircuitType,
       "zxAnQosIITrafficLogicalId": zxAnQosIITrafficLogicalId,
       "zxAnQosIITrafficDirection": zxAnQosIITrafficDirection,
       "zxAnQosIITrafficSvcEncapType": zxAnQosIITrafficSvcEncapType,
       "zxAnQosIITrafficPrf": zxAnQosIITrafficPrf,
       "zxAnQosIITrafficCfgRowStatus": zxAnQosIITrafficCfgRowStatus,
       "zxAnQosIITrafficBandwidthTable": zxAnQosIITrafficBandwidthTable,
       "zxAnQosIITrafficBandwidthEntry": zxAnQosIITrafficBandwidthEntry,
       "zxAnQosIITrafficTotalBandwidth": zxAnQosIITrafficTotalBandwidth,
       "zxAnQosIITrafficRemainBandwidth": zxAnQosIITrafficRemainBandwidth,
       "zxAnQosIIMVlan2CosTable": zxAnQosIIMVlan2CosTable,
       "zxAnQosIIMVlan2CosEntry": zxAnQosIIMVlan2CosEntry,
       "zxAnQosIIMVlan2CosMVlanValue": zxAnQosIIMVlan2CosMVlanValue,
       "zxAnQosIIMVlan2CosCosValue": zxAnQosIIMVlan2CosCosValue,
       "zxAnQosIIMVlan2CosRowStatus": zxAnQosIIMVlan2CosRowStatus}
)
