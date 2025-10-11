# SNMP MIB module (ZTE-AN-NNI-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-NNI-QOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:54 2025
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

(ZxAnIfindex,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "ZxAnIfindex",
    "zxAn")


# MODULE-IDENTITY

zxAnNniQosMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnNniQosObjects_ObjectIdentity = ObjectIdentity
zxAnNniQosObjects = _ZxAnNniQosObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1)
)
_ZxAnNniQosGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnNniQosGlobalObjects = _ZxAnNniQosGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 1)
)


class _ZxAnNniQosCos2Queue_Type(OctetString):
    """Custom type zxAnNniQosCos2Queue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_ZxAnNniQosCos2Queue_Type.__name__ = "OctetString"
_ZxAnNniQosCos2Queue_Object = MibScalar
zxAnNniQosCos2Queue = _ZxAnNniQosCos2Queue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 1, 1),
    _ZxAnNniQosCos2Queue_Type()
)
zxAnNniQosCos2Queue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnNniQosCos2Queue.setStatus("current")


class _ZxAnNniQosCos2Drop_Type(OctetString):
    """Custom type zxAnNniQosCos2Drop based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_ZxAnNniQosCos2Drop_Type.__name__ = "OctetString"
_ZxAnNniQosCos2Drop_Object = MibScalar
zxAnNniQosCos2Drop = _ZxAnNniQosCos2Drop_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 1, 8),
    _ZxAnNniQosCos2Drop_Type()
)
zxAnNniQosCos2Drop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnNniQosCos2Drop.setStatus("current")


class _ZxAnNniQosTrustMode_Type(Integer32):
    """Custom type zxAnNniQosTrustMode based on Integer32"""
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


_ZxAnNniQosTrustMode_Type.__name__ = "Integer32"
_ZxAnNniQosTrustMode_Object = MibScalar
zxAnNniQosTrustMode = _ZxAnNniQosTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 1, 9),
    _ZxAnNniQosTrustMode_Type()
)
zxAnNniQosTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnNniQosTrustMode.setStatus("current")
_ZxAnNniQosQueueSchedTable_Object = MibTable
zxAnNniQosQueueSchedTable = _ZxAnNniQosQueueSchedTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 2)
)
if mibBuilder.loadTexts:
    zxAnNniQosQueueSchedTable.setStatus("current")
_ZxAnNniQosQueueSchedEntry_Object = MibTableRow
zxAnNniQosQueueSchedEntry = _ZxAnNniQosQueueSchedEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 2, 1)
)
zxAnNniQosQueueSchedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnNniQosQueueSchedEntry.setStatus("current")


class _ZxAnNniQosQueueSchedAlgorithm_Type(Integer32):
    """Custom type zxAnNniQosQueueSchedAlgorithm based on Integer32"""
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


_ZxAnNniQosQueueSchedAlgorithm_Type.__name__ = "Integer32"
_ZxAnNniQosQueueSchedAlgorithm_Object = MibTableColumn
zxAnNniQosQueueSchedAlgorithm = _ZxAnNniQosQueueSchedAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 2, 1, 1),
    _ZxAnNniQosQueueSchedAlgorithm_Type()
)
zxAnNniQosQueueSchedAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnNniQosQueueSchedAlgorithm.setStatus("current")


class _ZxAnNniQosQueueSchedWeight_Type(OctetString):
    """Custom type zxAnNniQosQueueSchedWeight based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_ZxAnNniQosQueueSchedWeight_Type.__name__ = "OctetString"
_ZxAnNniQosQueueSchedWeight_Object = MibTableColumn
zxAnNniQosQueueSchedWeight = _ZxAnNniQosQueueSchedWeight_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 2, 1, 2),
    _ZxAnNniQosQueueSchedWeight_Type()
)
zxAnNniQosQueueSchedWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnNniQosQueueSchedWeight.setStatus("current")
_ZxAnNniQosQueueSchedMinRate_Type = ObjectIdentifier
_ZxAnNniQosQueueSchedMinRate_Object = MibTableColumn
zxAnNniQosQueueSchedMinRate = _ZxAnNniQosQueueSchedMinRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 2, 1, 3),
    _ZxAnNniQosQueueSchedMinRate_Type()
)
zxAnNniQosQueueSchedMinRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnNniQosQueueSchedMinRate.setStatus("current")
_ZxAnNniQosQueueSchedMaxRate_Type = ObjectIdentifier
_ZxAnNniQosQueueSchedMaxRate_Object = MibTableColumn
zxAnNniQosQueueSchedMaxRate = _ZxAnNniQosQueueSchedMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 2, 1, 4),
    _ZxAnNniQosQueueSchedMaxRate_Type()
)
zxAnNniQosQueueSchedMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnNniQosQueueSchedMaxRate.setStatus("current")
_ZxAnNniQosQueueSchedRowStatus_Type = RowStatus
_ZxAnNniQosQueueSchedRowStatus_Object = MibTableColumn
zxAnNniQosQueueSchedRowStatus = _ZxAnNniQosQueueSchedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 2, 1, 10),
    _ZxAnNniQosQueueSchedRowStatus_Type()
)
zxAnNniQosQueueSchedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnNniQosQueueSchedRowStatus.setStatus("current")
_ZxAnNniQosAclBindTable_Object = MibTable
zxAnNniQosAclBindTable = _ZxAnNniQosAclBindTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 3)
)
if mibBuilder.loadTexts:
    zxAnNniQosAclBindTable.setStatus("current")
_ZxAnNniQosAclBindEntry_Object = MibTableRow
zxAnNniQosAclBindEntry = _ZxAnNniQosAclBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 3, 1)
)
zxAnNniQosAclBindEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnNniQosAclBindEntry.setStatus("current")


class _ZxAnNniQosAclIndex_Type(Integer32):
    """Custom type zxAnNniQosAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 349),
    )


_ZxAnNniQosAclIndex_Type.__name__ = "Integer32"
_ZxAnNniQosAclIndex_Object = MibTableColumn
zxAnNniQosAclIndex = _ZxAnNniQosAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 3, 1, 1),
    _ZxAnNniQosAclIndex_Type()
)
zxAnNniQosAclIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnNniQosAclIndex.setStatus("current")


class _ZxAnNniQosAclBindDir_Type(Integer32):
    """Custom type zxAnNniQosAclBindDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_ZxAnNniQosAclBindDir_Type.__name__ = "Integer32"
_ZxAnNniQosAclBindDir_Object = MibTableColumn
zxAnNniQosAclBindDir = _ZxAnNniQosAclBindDir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 3, 1, 2),
    _ZxAnNniQosAclBindDir_Type()
)
zxAnNniQosAclBindDir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnNniQosAclBindDir.setStatus("current")
_ZxAnNniQosAclBindRowStatus_Type = RowStatus
_ZxAnNniQosAclBindRowStatus_Object = MibTableColumn
zxAnNniQosAclBindRowStatus = _ZxAnNniQosAclBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 3, 1, 10),
    _ZxAnNniQosAclBindRowStatus_Type()
)
zxAnNniQosAclBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnNniQosAclBindRowStatus.setStatus("current")
_ZxAnNniQosShapeTable_Object = MibTable
zxAnNniQosShapeTable = _ZxAnNniQosShapeTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 4)
)
if mibBuilder.loadTexts:
    zxAnNniQosShapeTable.setStatus("current")
_ZxAnNniQosShapeEntry_Object = MibTableRow
zxAnNniQosShapeEntry = _ZxAnNniQosShapeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 4, 1)
)
zxAnNniQosShapeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnNniQosShapeEntry.setStatus("current")
_ZxAnNniQosShapeRate_Type = Integer32
_ZxAnNniQosShapeRate_Object = MibTableColumn
zxAnNniQosShapeRate = _ZxAnNniQosShapeRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 4, 1, 1),
    _ZxAnNniQosShapeRate_Type()
)
zxAnNniQosShapeRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnNniQosShapeRate.setStatus("current")
_ZxAnNniQosShapeBurstSize_Type = Integer32
_ZxAnNniQosShapeBurstSize_Object = MibTableColumn
zxAnNniQosShapeBurstSize = _ZxAnNniQosShapeBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 4, 1, 2),
    _ZxAnNniQosShapeBurstSize_Type()
)
zxAnNniQosShapeBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnNniQosShapeBurstSize.setStatus("current")


class _ZxAnNniQosShapeDir_Type(Integer32):
    """Custom type zxAnNniQosShapeDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_ZxAnNniQosShapeDir_Type.__name__ = "Integer32"
_ZxAnNniQosShapeDir_Object = MibTableColumn
zxAnNniQosShapeDir = _ZxAnNniQosShapeDir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 4, 1, 3),
    _ZxAnNniQosShapeDir_Type()
)
zxAnNniQosShapeDir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnNniQosShapeDir.setStatus("current")
_ZxAnNniQosShapeRowStatus_Type = RowStatus
_ZxAnNniQosShapeRowStatus_Object = MibTableColumn
zxAnNniQosShapeRowStatus = _ZxAnNniQosShapeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 4, 1, 10),
    _ZxAnNniQosShapeRowStatus_Type()
)
zxAnNniQosShapeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnNniQosShapeRowStatus.setStatus("current")
_ZxAnNniQosShapeConfTable_Object = MibTable
zxAnNniQosShapeConfTable = _ZxAnNniQosShapeConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 5)
)
if mibBuilder.loadTexts:
    zxAnNniQosShapeConfTable.setStatus("current")
_ZxAnNniQosShapeConfEntry_Object = MibTableRow
zxAnNniQosShapeConfEntry = _ZxAnNniQosShapeConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 5, 1)
)
zxAnNniQosShapeConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZTE-AN-NNI-QOS-MIB", "zxAnNniQosShapeConfDir"),
)
if mibBuilder.loadTexts:
    zxAnNniQosShapeConfEntry.setStatus("current")


class _ZxAnNniQosShapeConfDir_Type(Integer32):
    """Custom type zxAnNniQosShapeConfDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_ZxAnNniQosShapeConfDir_Type.__name__ = "Integer32"
_ZxAnNniQosShapeConfDir_Object = MibTableColumn
zxAnNniQosShapeConfDir = _ZxAnNniQosShapeConfDir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 5, 1, 1),
    _ZxAnNniQosShapeConfDir_Type()
)
zxAnNniQosShapeConfDir.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnNniQosShapeConfDir.setStatus("current")
_ZxAnNniQosShapeConfRate_Type = Integer32
_ZxAnNniQosShapeConfRate_Object = MibTableColumn
zxAnNniQosShapeConfRate = _ZxAnNniQosShapeConfRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 5, 1, 2),
    _ZxAnNniQosShapeConfRate_Type()
)
zxAnNniQosShapeConfRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnNniQosShapeConfRate.setStatus("current")
_ZxAnNniQosShapeConfBurstSize_Type = Integer32
_ZxAnNniQosShapeConfBurstSize_Object = MibTableColumn
zxAnNniQosShapeConfBurstSize = _ZxAnNniQosShapeConfBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 5, 1, 3),
    _ZxAnNniQosShapeConfBurstSize_Type()
)
zxAnNniQosShapeConfBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnNniQosShapeConfBurstSize.setStatus("current")
_ZxAnNniQosShapeConfRowStatus_Type = RowStatus
_ZxAnNniQosShapeConfRowStatus_Object = MibTableColumn
zxAnNniQosShapeConfRowStatus = _ZxAnNniQosShapeConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 5, 1, 10),
    _ZxAnNniQosShapeConfRowStatus_Type()
)
zxAnNniQosShapeConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnNniQosShapeConfRowStatus.setStatus("current")
_ZxAnNniQosTrustTable_Object = MibTable
zxAnNniQosTrustTable = _ZxAnNniQosTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 6)
)
if mibBuilder.loadTexts:
    zxAnNniQosTrustTable.setStatus("current")
_ZxAnNniQosTrustEntry_Object = MibTableRow
zxAnNniQosTrustEntry = _ZxAnNniQosTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 6, 1)
)
zxAnNniQosTrustEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnNniQosTrustEntry.setStatus("current")


class _ZxAnNniQosTrustDscp_Type(Integer32):
    """Custom type zxAnNniQosTrustDscp based on Integer32"""
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


_ZxAnNniQosTrustDscp_Type.__name__ = "Integer32"
_ZxAnNniQosTrustDscp_Object = MibTableColumn
zxAnNniQosTrustDscp = _ZxAnNniQosTrustDscp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 6, 1, 1),
    _ZxAnNniQosTrustDscp_Type()
)
zxAnNniQosTrustDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnNniQosTrustDscp.setStatus("current")


class _ZxAnNniQosTrustCos_Type(Integer32):
    """Custom type zxAnNniQosTrustCos based on Integer32"""
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


_ZxAnNniQosTrustCos_Type.__name__ = "Integer32"
_ZxAnNniQosTrustCos_Object = MibTableColumn
zxAnNniQosTrustCos = _ZxAnNniQosTrustCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 6, 1, 2),
    _ZxAnNniQosTrustCos_Type()
)
zxAnNniQosTrustCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnNniQosTrustCos.setStatus("current")
_ZxAnNniQosConformDscpTable_Object = MibTable
zxAnNniQosConformDscpTable = _ZxAnNniQosConformDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 7)
)
if mibBuilder.loadTexts:
    zxAnNniQosConformDscpTable.setStatus("current")
_ZxAnNniQosConformDscpEntry_Object = MibTableRow
zxAnNniQosConformDscpEntry = _ZxAnNniQosConformDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 7, 1)
)
zxAnNniQosConformDscpEntry.setIndexNames(
    (0, "ZTE-AN-NNI-QOS-MIB", "zxAnNniQosConformDscpDscp"),
)
if mibBuilder.loadTexts:
    zxAnNniQosConformDscpEntry.setStatus("current")


class _ZxAnNniQosConformDscpDscp_Type(Integer32):
    """Custom type zxAnNniQosConformDscpDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ZxAnNniQosConformDscpDscp_Type.__name__ = "Integer32"
_ZxAnNniQosConformDscpDscp_Object = MibTableColumn
zxAnNniQosConformDscpDscp = _ZxAnNniQosConformDscpDscp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 7, 1, 1),
    _ZxAnNniQosConformDscpDscp_Type()
)
zxAnNniQosConformDscpDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnNniQosConformDscpDscp.setStatus("current")


class _ZxAnNniQosConformDscpNewDscp_Type(Integer32):
    """Custom type zxAnNniQosConformDscpNewDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ZxAnNniQosConformDscpNewDscp_Type.__name__ = "Integer32"
_ZxAnNniQosConformDscpNewDscp_Object = MibTableColumn
zxAnNniQosConformDscpNewDscp = _ZxAnNniQosConformDscpNewDscp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 7, 1, 2),
    _ZxAnNniQosConformDscpNewDscp_Type()
)
zxAnNniQosConformDscpNewDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnNniQosConformDscpNewDscp.setStatus("current")


class _ZxAnNniQosConformDscpNewCos_Type(Integer32):
    """Custom type zxAnNniQosConformDscpNewCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnNniQosConformDscpNewCos_Type.__name__ = "Integer32"
_ZxAnNniQosConformDscpNewCos_Object = MibTableColumn
zxAnNniQosConformDscpNewCos = _ZxAnNniQosConformDscpNewCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 7, 1, 3),
    _ZxAnNniQosConformDscpNewCos_Type()
)
zxAnNniQosConformDscpNewCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnNniQosConformDscpNewCos.setStatus("current")


class _ZxAnNniQosConformDscpNewDp_Type(Integer32):
    """Custom type zxAnNniQosConformDscpNewDp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ZxAnNniQosConformDscpNewDp_Type.__name__ = "Integer32"
_ZxAnNniQosConformDscpNewDp_Object = MibTableColumn
zxAnNniQosConformDscpNewDp = _ZxAnNniQosConformDscpNewDp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 7, 1, 4),
    _ZxAnNniQosConformDscpNewDp_Type()
)
zxAnNniQosConformDscpNewDp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnNniQosConformDscpNewDp.setStatus("current")
_ZxAnNniQosConformDscpRowStatus_Type = RowStatus
_ZxAnNniQosConformDscpRowStatus_Object = MibTableColumn
zxAnNniQosConformDscpRowStatus = _ZxAnNniQosConformDscpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 1, 7, 1, 10),
    _ZxAnNniQosConformDscpRowStatus_Type()
)
zxAnNniQosConformDscpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnNniQosConformDscpRowStatus.setStatus("current")
_ZxAnNniQosTrapObjects_ObjectIdentity = ObjectIdentity
zxAnNniQosTrapObjects = _ZxAnNniQosTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 22, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-NNI-QOS-MIB",
    **{"zxAnNniQosMib": zxAnNniQosMib,
       "zxAnNniQosObjects": zxAnNniQosObjects,
       "zxAnNniQosGlobalObjects": zxAnNniQosGlobalObjects,
       "zxAnNniQosCos2Queue": zxAnNniQosCos2Queue,
       "zxAnNniQosCos2Drop": zxAnNniQosCos2Drop,
       "zxAnNniQosTrustMode": zxAnNniQosTrustMode,
       "zxAnNniQosQueueSchedTable": zxAnNniQosQueueSchedTable,
       "zxAnNniQosQueueSchedEntry": zxAnNniQosQueueSchedEntry,
       "zxAnNniQosQueueSchedAlgorithm": zxAnNniQosQueueSchedAlgorithm,
       "zxAnNniQosQueueSchedWeight": zxAnNniQosQueueSchedWeight,
       "zxAnNniQosQueueSchedMinRate": zxAnNniQosQueueSchedMinRate,
       "zxAnNniQosQueueSchedMaxRate": zxAnNniQosQueueSchedMaxRate,
       "zxAnNniQosQueueSchedRowStatus": zxAnNniQosQueueSchedRowStatus,
       "zxAnNniQosAclBindTable": zxAnNniQosAclBindTable,
       "zxAnNniQosAclBindEntry": zxAnNniQosAclBindEntry,
       "zxAnNniQosAclIndex": zxAnNniQosAclIndex,
       "zxAnNniQosAclBindDir": zxAnNniQosAclBindDir,
       "zxAnNniQosAclBindRowStatus": zxAnNniQosAclBindRowStatus,
       "zxAnNniQosShapeTable": zxAnNniQosShapeTable,
       "zxAnNniQosShapeEntry": zxAnNniQosShapeEntry,
       "zxAnNniQosShapeRate": zxAnNniQosShapeRate,
       "zxAnNniQosShapeBurstSize": zxAnNniQosShapeBurstSize,
       "zxAnNniQosShapeDir": zxAnNniQosShapeDir,
       "zxAnNniQosShapeRowStatus": zxAnNniQosShapeRowStatus,
       "zxAnNniQosShapeConfTable": zxAnNniQosShapeConfTable,
       "zxAnNniQosShapeConfEntry": zxAnNniQosShapeConfEntry,
       "zxAnNniQosShapeConfDir": zxAnNniQosShapeConfDir,
       "zxAnNniQosShapeConfRate": zxAnNniQosShapeConfRate,
       "zxAnNniQosShapeConfBurstSize": zxAnNniQosShapeConfBurstSize,
       "zxAnNniQosShapeConfRowStatus": zxAnNniQosShapeConfRowStatus,
       "zxAnNniQosTrustTable": zxAnNniQosTrustTable,
       "zxAnNniQosTrustEntry": zxAnNniQosTrustEntry,
       "zxAnNniQosTrustDscp": zxAnNniQosTrustDscp,
       "zxAnNniQosTrustCos": zxAnNniQosTrustCos,
       "zxAnNniQosConformDscpTable": zxAnNniQosConformDscpTable,
       "zxAnNniQosConformDscpEntry": zxAnNniQosConformDscpEntry,
       "zxAnNniQosConformDscpDscp": zxAnNniQosConformDscpDscp,
       "zxAnNniQosConformDscpNewDscp": zxAnNniQosConformDscpNewDscp,
       "zxAnNniQosConformDscpNewCos": zxAnNniQosConformDscpNewCos,
       "zxAnNniQosConformDscpNewDp": zxAnNniQosConformDscpNewDp,
       "zxAnNniQosConformDscpRowStatus": zxAnNniQosConformDscpRowStatus,
       "zxAnNniQosTrapObjects": zxAnNniQosTrapObjects}
)
