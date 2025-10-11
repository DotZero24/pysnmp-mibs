# SNMP MIB module (MAIPU-ROUTEMAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MAIPU-ROUTEMAP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:08 2025
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

(mpMgmt,) = mibBuilder.importSymbols(
    "MAIPU-SMI",
    "mpMgmt")

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


# MODULE-IDENTITY

mpRouteMapMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RtMapConf_ObjectIdentity = ObjectIdentity
rtMapConf = _RtMapConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1)
)
_RtMapMatchTable_Object = MibTable
rtMapMatchTable = _RtMapMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 1)
)
if mibBuilder.loadTexts:
    rtMapMatchTable.setStatus("current")
_RtMapMatchEntry_Object = MibTableRow
rtMapMatchEntry = _RtMapMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 1, 1)
)
rtMapMatchEntry.setIndexNames(
    (0, "MAIPU-ROUTEMAP-MIB", "rtMapMatchRMName"),
    (0, "MAIPU-ROUTEMAP-MIB", "rtMapMatchRMSeq"),
)
if mibBuilder.loadTexts:
    rtMapMatchEntry.setStatus("current")
_RtMapMatchRMName_Type = OctetString
_RtMapMatchRMName_Object = MibTableColumn
rtMapMatchRMName = _RtMapMatchRMName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 1, 1, 1),
    _RtMapMatchRMName_Type()
)
rtMapMatchRMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtMapMatchRMName.setStatus("current")


class _RtMapMatchRMSeq_Type(Integer32):
    """Custom type rtMapMatchRMSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RtMapMatchRMSeq_Type.__name__ = "Integer32"
_RtMapMatchRMSeq_Object = MibTableColumn
rtMapMatchRMSeq = _RtMapMatchRMSeq_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 1, 1, 2),
    _RtMapMatchRMSeq_Type()
)
rtMapMatchRMSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtMapMatchRMSeq.setStatus("current")


class _RtMapMatchAccess_Type(Integer32):
    """Custom type rtMapMatchAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_RtMapMatchAccess_Type.__name__ = "Integer32"
_RtMapMatchAccess_Object = MibTableColumn
rtMapMatchAccess = _RtMapMatchAccess_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 1, 1, 3),
    _RtMapMatchAccess_Type()
)
rtMapMatchAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapMatchAccess.setStatus("current")
_RtMapMatchAsPath_Type = OctetString
_RtMapMatchAsPath_Object = MibTableColumn
rtMapMatchAsPath = _RtMapMatchAsPath_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 1, 1, 4),
    _RtMapMatchAsPath_Type()
)
rtMapMatchAsPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapMatchAsPath.setStatus("current")
_RtMapMatchCom_Type = OctetString
_RtMapMatchCom_Object = MibTableColumn
rtMapMatchCom = _RtMapMatchCom_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 1, 1, 5),
    _RtMapMatchCom_Type()
)
rtMapMatchCom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapMatchCom.setStatus("current")
_RtMapMatchExtCom_Type = OctetString
_RtMapMatchExtCom_Object = MibTableColumn
rtMapMatchExtCom = _RtMapMatchExtCom_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 1, 1, 6),
    _RtMapMatchExtCom_Type()
)
rtMapMatchExtCom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapMatchExtCom.setStatus("current")
_RtMapMatchInt_Type = OctetString
_RtMapMatchInt_Object = MibTableColumn
rtMapMatchInt = _RtMapMatchInt_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 1, 1, 7),
    _RtMapMatchInt_Type()
)
rtMapMatchInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapMatchInt.setStatus("current")
_RtMapMatchIpAddr_Type = OctetString
_RtMapMatchIpAddr_Object = MibTableColumn
rtMapMatchIpAddr = _RtMapMatchIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 1, 1, 8),
    _RtMapMatchIpAddr_Type()
)
rtMapMatchIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapMatchIpAddr.setStatus("current")
_RtMapMatchIpNexthop_Type = OctetString
_RtMapMatchIpNexthop_Object = MibTableColumn
rtMapMatchIpNexthop = _RtMapMatchIpNexthop_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 1, 1, 9),
    _RtMapMatchIpNexthop_Type()
)
rtMapMatchIpNexthop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapMatchIpNexthop.setStatus("current")
_RtMapMatchIpRtSrc_Type = OctetString
_RtMapMatchIpRtSrc_Object = MibTableColumn
rtMapMatchIpRtSrc = _RtMapMatchIpRtSrc_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 1, 1, 10),
    _RtMapMatchIpRtSrc_Type()
)
rtMapMatchIpRtSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapMatchIpRtSrc.setStatus("current")
_RtMapMatchLenMin_Type = Integer32
_RtMapMatchLenMin_Object = MibTableColumn
rtMapMatchLenMin = _RtMapMatchLenMin_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 1, 1, 11),
    _RtMapMatchLenMin_Type()
)
rtMapMatchLenMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapMatchLenMin.setStatus("current")
_RtMapMatchLenMax_Type = Integer32
_RtMapMatchLenMax_Object = MibTableColumn
rtMapMatchLenMax = _RtMapMatchLenMax_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 1, 1, 12),
    _RtMapMatchLenMax_Type()
)
rtMapMatchLenMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapMatchLenMax.setStatus("current")
_RtMapMatchMetric_Type = OctetString
_RtMapMatchMetric_Object = MibTableColumn
rtMapMatchMetric = _RtMapMatchMetric_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 1, 1, 13),
    _RtMapMatchMetric_Type()
)
rtMapMatchMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapMatchMetric.setStatus("current")


class _RtMapMatchRtType_Type(Integer32):
    """Custom type rtMapMatchRtType based on Integer32"""
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
        *(("extType1", 1),
          ("extType2", 2),
          ("internal", 3),
          ("level1", 4),
          ("level2", 5),
          ("local", 6),
          ("nssaExtType1", 7),
          ("nssaExtType2", 8))
    )


_RtMapMatchRtType_Type.__name__ = "Integer32"
_RtMapMatchRtType_Object = MibTableColumn
rtMapMatchRtType = _RtMapMatchRtType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 1, 1, 14),
    _RtMapMatchRtType_Type()
)
rtMapMatchRtType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapMatchRtType.setStatus("current")
_RtMapMatchTag_Type = OctetString
_RtMapMatchTag_Object = MibTableColumn
rtMapMatchTag = _RtMapMatchTag_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 1, 1, 15),
    _RtMapMatchTag_Type()
)
rtMapMatchTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapMatchTag.setStatus("current")
_RtMapMatchStatus_Type = RowStatus
_RtMapMatchStatus_Object = MibTableColumn
rtMapMatchStatus = _RtMapMatchStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 1, 1, 16),
    _RtMapMatchStatus_Type()
)
rtMapMatchStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapMatchStatus.setStatus("current")


class _RtMapMatchComExact_Type(Integer32):
    """Custom type rtMapMatchComExact based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RtMapMatchComExact_Type.__name__ = "Integer32"
_RtMapMatchComExact_Object = MibTableColumn
rtMapMatchComExact = _RtMapMatchComExact_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 1, 1, 17),
    _RtMapMatchComExact_Type()
)
rtMapMatchComExact.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapMatchComExact.setStatus("current")
_RtMapSetTable_Object = MibTable
rtMapSetTable = _RtMapSetTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2)
)
if mibBuilder.loadTexts:
    rtMapSetTable.setStatus("current")
_RtMapSetEntry_Object = MibTableRow
rtMapSetEntry = _RtMapSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1)
)
rtMapSetEntry.setIndexNames(
    (0, "MAIPU-ROUTEMAP-MIB", "rtMapSetRMName"),
    (0, "MAIPU-ROUTEMAP-MIB", "rtMapSetRMSeq"),
)
if mibBuilder.loadTexts:
    rtMapSetEntry.setStatus("current")
_RtMapSetRMName_Type = OctetString
_RtMapSetRMName_Object = MibTableColumn
rtMapSetRMName = _RtMapSetRMName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 1),
    _RtMapSetRMName_Type()
)
rtMapSetRMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtMapSetRMName.setStatus("current")


class _RtMapSetRMSeq_Type(Integer32):
    """Custom type rtMapSetRMSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RtMapSetRMSeq_Type.__name__ = "Integer32"
_RtMapSetRMSeq_Object = MibTableColumn
rtMapSetRMSeq = _RtMapSetRMSeq_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 2),
    _RtMapSetRMSeq_Type()
)
rtMapSetRMSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtMapSetRMSeq.setStatus("current")
_RtMapSetAsPathPrepend_Type = OctetString
_RtMapSetAsPathPrepend_Object = MibTableColumn
rtMapSetAsPathPrepend = _RtMapSetAsPathPrepend_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 3),
    _RtMapSetAsPathPrepend_Type()
)
rtMapSetAsPathPrepend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetAsPathPrepend.setStatus("current")


class _RtMapSetAsPathTag_Type(Integer32):
    """Custom type rtMapSetAsPathTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RtMapSetAsPathTag_Type.__name__ = "Integer32"
_RtMapSetAsPathTag_Object = MibTableColumn
rtMapSetAsPathTag = _RtMapSetAsPathTag_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 4),
    _RtMapSetAsPathTag_Type()
)
rtMapSetAsPathTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetAsPathTag.setStatus("current")


class _RtMapSetAutoTag_Type(Integer32):
    """Custom type rtMapSetAutoTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RtMapSetAutoTag_Type.__name__ = "Integer32"
_RtMapSetAutoTag_Object = MibTableColumn
rtMapSetAutoTag = _RtMapSetAutoTag_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 5),
    _RtMapSetAutoTag_Type()
)
rtMapSetAutoTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetAutoTag.setStatus("current")
_RtMapSetCom_Type = Integer32
_RtMapSetCom_Object = MibTableColumn
rtMapSetCom = _RtMapSetCom_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 6),
    _RtMapSetCom_Type()
)
rtMapSetCom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetCom.setStatus("current")


class _RtMapSetDampHalfLife_Type(Integer32):
    """Custom type rtMapSetDampHalfLife based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 45),
    )


_RtMapSetDampHalfLife_Type.__name__ = "Integer32"
_RtMapSetDampHalfLife_Object = MibTableColumn
rtMapSetDampHalfLife = _RtMapSetDampHalfLife_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 7),
    _RtMapSetDampHalfLife_Type()
)
rtMapSetDampHalfLife.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetDampHalfLife.setStatus("current")


class _RtMapSetDampReuse_Type(Integer32):
    """Custom type rtMapSetDampReuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_RtMapSetDampReuse_Type.__name__ = "Integer32"
_RtMapSetDampReuse_Object = MibTableColumn
rtMapSetDampReuse = _RtMapSetDampReuse_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 8),
    _RtMapSetDampReuse_Type()
)
rtMapSetDampReuse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetDampReuse.setStatus("current")


class _RtMapSetDampSuppress_Type(Integer32):
    """Custom type rtMapSetDampSuppress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_RtMapSetDampSuppress_Type.__name__ = "Integer32"
_RtMapSetDampSuppress_Object = MibTableColumn
rtMapSetDampSuppress = _RtMapSetDampSuppress_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 9),
    _RtMapSetDampSuppress_Type()
)
rtMapSetDampSuppress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetDampSuppress.setStatus("current")


class _RtMapSetDampMaxDura_Type(Integer32):
    """Custom type rtMapSetDampMaxDura based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RtMapSetDampMaxDura_Type.__name__ = "Integer32"
_RtMapSetDampMaxDura_Object = MibTableColumn
rtMapSetDampMaxDura = _RtMapSetDampMaxDura_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 10),
    _RtMapSetDampMaxDura_Type()
)
rtMapSetDampMaxDura.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetDampMaxDura.setStatus("current")
_RtMapSetDefaultInt_Type = OctetString
_RtMapSetDefaultInt_Object = MibTableColumn
rtMapSetDefaultInt = _RtMapSetDefaultInt_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 11),
    _RtMapSetDefaultInt_Type()
)
rtMapSetDefaultInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetDefaultInt.setStatus("current")
_RtMapSetExtComRt_Type = OctetString
_RtMapSetExtComRt_Object = MibTableColumn
rtMapSetExtComRt = _RtMapSetExtComRt_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 12),
    _RtMapSetExtComRt_Type()
)
rtMapSetExtComRt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetExtComRt.setStatus("current")
_RtMapSetExtComSoo_Type = OctetString
_RtMapSetExtComSoo_Object = MibTableColumn
rtMapSetExtComSoo = _RtMapSetExtComSoo_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 13),
    _RtMapSetExtComSoo_Type()
)
rtMapSetExtComSoo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetExtComSoo.setStatus("current")
_RtMapSetInt_Type = OctetString
_RtMapSetInt_Object = MibTableColumn
rtMapSetInt = _RtMapSetInt_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 14),
    _RtMapSetInt_Type()
)
rtMapSetInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetInt.setStatus("current")
_RtMapSetIpDefNextHop_Type = OctetString
_RtMapSetIpDefNextHop_Object = MibTableColumn
rtMapSetIpDefNextHop = _RtMapSetIpDefNextHop_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 15),
    _RtMapSetIpDefNextHop_Type()
)
rtMapSetIpDefNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetIpDefNextHop.setStatus("current")


class _RtMapSetIpDF_Type(Integer32):
    """Custom type rtMapSetIpDF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RtMapSetIpDF_Type.__name__ = "Integer32"
_RtMapSetIpDF_Object = MibTableColumn
rtMapSetIpDF = _RtMapSetIpDF_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 16),
    _RtMapSetIpDF_Type()
)
rtMapSetIpDF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetIpDF.setStatus("current")
_RtMapSetIpNextHop_Type = OctetString
_RtMapSetIpNextHop_Object = MibTableColumn
rtMapSetIpNextHop = _RtMapSetIpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 17),
    _RtMapSetIpNextHop_Type()
)
rtMapSetIpNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetIpNextHop.setStatus("current")
_RtMapSetIpNextHopAttr_Type = Integer32
_RtMapSetIpNextHopAttr_Object = MibTableColumn
rtMapSetIpNextHopAttr = _RtMapSetIpNextHopAttr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 18),
    _RtMapSetIpNextHopAttr_Type()
)
rtMapSetIpNextHopAttr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetIpNextHopAttr.setStatus("current")


class _RtMapSetIpPre_Type(Integer32):
    """Custom type rtMapSetIpPre based on Integer32"""
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
        *(("routine", 1),
          ("priority", 2),
          ("immediate", 3),
          ("flash", 4),
          ("flash-override", 5),
          ("critical", 6),
          ("internet", 7),
          ("network", 8))
    )


_RtMapSetIpPre_Type.__name__ = "Integer32"
_RtMapSetIpPre_Object = MibTableColumn
rtMapSetIpPre = _RtMapSetIpPre_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 19),
    _RtMapSetIpPre_Type()
)
rtMapSetIpPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetIpPre.setStatus("current")


class _RtMapSetIpQosGrp_Type(Integer32):
    """Custom type rtMapSetIpQosGrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RtMapSetIpQosGrp_Type.__name__ = "Integer32"
_RtMapSetIpQosGrp_Object = MibTableColumn
rtMapSetIpQosGrp = _RtMapSetIpQosGrp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 20),
    _RtMapSetIpQosGrp_Type()
)
rtMapSetIpQosGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetIpQosGrp.setStatus("current")


class _RtMapSetIpTos_Type(Integer32):
    """Custom type rtMapSetIpTos based on Integer32"""
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
        *(("normal", 1),
          ("min-monetary-cost", 2),
          ("max-reliability", 3),
          ("max-throughput", 4),
          ("min-delay", 5))
    )


_RtMapSetIpTos_Type.__name__ = "Integer32"
_RtMapSetIpTos_Object = MibTableColumn
rtMapSetIpTos = _RtMapSetIpTos_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 21),
    _RtMapSetIpTos_Type()
)
rtMapSetIpTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetIpTos.setStatus("current")


class _RtMapSetLevel_Type(Integer32):
    """Custom type rtMapSetLevel based on Integer32"""
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
          ("level-1", 2),
          ("level-1-2", 3),
          ("level-2", 4),
          ("stub-area", 5))
    )


_RtMapSetLevel_Type.__name__ = "Integer32"
_RtMapSetLevel_Object = MibTableColumn
rtMapSetLevel = _RtMapSetLevel_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 22),
    _RtMapSetLevel_Type()
)
rtMapSetLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetLevel.setStatus("current")
_RtMapSetLocalPre_Type = Integer32
_RtMapSetLocalPre_Object = MibTableColumn
rtMapSetLocalPre = _RtMapSetLocalPre_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 23),
    _RtMapSetLocalPre_Type()
)
rtMapSetLocalPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetLocalPre.setStatus("current")
_RtMapSetMetricVal_Type = Integer32
_RtMapSetMetricVal_Object = MibTableColumn
rtMapSetMetricVal = _RtMapSetMetricVal_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 24),
    _RtMapSetMetricVal_Type()
)
rtMapSetMetricVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetMetricVal.setStatus("current")
_RtMapSetMetricIgrpDelay_Type = Integer32
_RtMapSetMetricIgrpDelay_Object = MibTableColumn
rtMapSetMetricIgrpDelay = _RtMapSetMetricIgrpDelay_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 25),
    _RtMapSetMetricIgrpDelay_Type()
)
rtMapSetMetricIgrpDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetMetricIgrpDelay.setStatus("current")
_RtMapSetMetricIgrpRelia_Type = Integer32
_RtMapSetMetricIgrpRelia_Object = MibTableColumn
rtMapSetMetricIgrpRelia = _RtMapSetMetricIgrpRelia_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 26),
    _RtMapSetMetricIgrpRelia_Type()
)
rtMapSetMetricIgrpRelia.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetMetricIgrpRelia.setStatus("current")
_RtMapSetMetricIgrpEffect_Type = Integer32
_RtMapSetMetricIgrpEffect_Object = MibTableColumn
rtMapSetMetricIgrpEffect = _RtMapSetMetricIgrpEffect_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 27),
    _RtMapSetMetricIgrpEffect_Type()
)
rtMapSetMetricIgrpEffect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetMetricIgrpEffect.setStatus("current")
_RtMapSetMetricIgrpMtu_Type = Integer32
_RtMapSetMetricIgrpMtu_Object = MibTableColumn
rtMapSetMetricIgrpMtu = _RtMapSetMetricIgrpMtu_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 28),
    _RtMapSetMetricIgrpMtu_Type()
)
rtMapSetMetricIgrpMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetMetricIgrpMtu.setStatus("current")


class _RtMapSetMetricType_Type(Integer32):
    """Custom type rtMapSetMetricType based on Integer32"""
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
        *(("external", 1),
          ("internal", 2),
          ("type-1", 3),
          ("type-2", 4))
    )


_RtMapSetMetricType_Type.__name__ = "Integer32"
_RtMapSetMetricType_Object = MibTableColumn
rtMapSetMetricType = _RtMapSetMetricType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 29),
    _RtMapSetMetricType_Type()
)
rtMapSetMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetMetricType.setStatus("current")


class _RtMapSetOrigin_Type(Integer32):
    """Custom type rtMapSetOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("egp", 1),
          ("igp", 2),
          ("incomplete", 3))
    )


_RtMapSetOrigin_Type.__name__ = "Integer32"
_RtMapSetOrigin_Object = MibTableColumn
rtMapSetOrigin = _RtMapSetOrigin_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 30),
    _RtMapSetOrigin_Type()
)
rtMapSetOrigin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetOrigin.setStatus("current")


class _RtMapSetOriEgpReAs_Type(Integer32):
    """Custom type rtMapSetOriEgpReAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RtMapSetOriEgpReAs_Type.__name__ = "Integer32"
_RtMapSetOriEgpReAs_Object = MibTableColumn
rtMapSetOriEgpReAs = _RtMapSetOriEgpReAs_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 31),
    _RtMapSetOriEgpReAs_Type()
)
rtMapSetOriEgpReAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetOriEgpReAs.setStatus("current")
_RtMapSetTag_Type = Integer32
_RtMapSetTag_Object = MibTableColumn
rtMapSetTag = _RtMapSetTag_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 32),
    _RtMapSetTag_Type()
)
rtMapSetTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetTag.setStatus("current")
_RtMapSetWeight_Type = Integer32
_RtMapSetWeight_Object = MibTableColumn
rtMapSetWeight = _RtMapSetWeight_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 33),
    _RtMapSetWeight_Type()
)
rtMapSetWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetWeight.setStatus("current")
_RtMapSetStatus_Type = RowStatus
_RtMapSetStatus_Object = MibTableColumn
rtMapSetStatus = _RtMapSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 34),
    _RtMapSetStatus_Type()
)
rtMapSetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetStatus.setStatus("current")
_RtMapSetComList_Type = OctetString
_RtMapSetComList_Object = MibTableColumn
rtMapSetComList = _RtMapSetComList_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 35),
    _RtMapSetComList_Type()
)
rtMapSetComList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetComList.setStatus("current")
_RtMapSetCommunity_Type = OctetString
_RtMapSetCommunity_Object = MibTableColumn
rtMapSetCommunity = _RtMapSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 36),
    _RtMapSetCommunity_Type()
)
rtMapSetCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetCommunity.setStatus("current")


class _RtMapSetAccess_Type(Integer32):
    """Custom type rtMapSetAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_RtMapSetAccess_Type.__name__ = "Integer32"
_RtMapSetAccess_Object = MibTableColumn
rtMapSetAccess = _RtMapSetAccess_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 33, 1, 2, 1, 37),
    _RtMapSetAccess_Type()
)
rtMapSetAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtMapSetAccess.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MAIPU-ROUTEMAP-MIB",
    **{"mpRouteMapMib": mpRouteMapMib,
       "rtMapConf": rtMapConf,
       "rtMapMatchTable": rtMapMatchTable,
       "rtMapMatchEntry": rtMapMatchEntry,
       "rtMapMatchRMName": rtMapMatchRMName,
       "rtMapMatchRMSeq": rtMapMatchRMSeq,
       "rtMapMatchAccess": rtMapMatchAccess,
       "rtMapMatchAsPath": rtMapMatchAsPath,
       "rtMapMatchCom": rtMapMatchCom,
       "rtMapMatchExtCom": rtMapMatchExtCom,
       "rtMapMatchInt": rtMapMatchInt,
       "rtMapMatchIpAddr": rtMapMatchIpAddr,
       "rtMapMatchIpNexthop": rtMapMatchIpNexthop,
       "rtMapMatchIpRtSrc": rtMapMatchIpRtSrc,
       "rtMapMatchLenMin": rtMapMatchLenMin,
       "rtMapMatchLenMax": rtMapMatchLenMax,
       "rtMapMatchMetric": rtMapMatchMetric,
       "rtMapMatchRtType": rtMapMatchRtType,
       "rtMapMatchTag": rtMapMatchTag,
       "rtMapMatchStatus": rtMapMatchStatus,
       "rtMapMatchComExact": rtMapMatchComExact,
       "rtMapSetTable": rtMapSetTable,
       "rtMapSetEntry": rtMapSetEntry,
       "rtMapSetRMName": rtMapSetRMName,
       "rtMapSetRMSeq": rtMapSetRMSeq,
       "rtMapSetAsPathPrepend": rtMapSetAsPathPrepend,
       "rtMapSetAsPathTag": rtMapSetAsPathTag,
       "rtMapSetAutoTag": rtMapSetAutoTag,
       "rtMapSetCom": rtMapSetCom,
       "rtMapSetDampHalfLife": rtMapSetDampHalfLife,
       "rtMapSetDampReuse": rtMapSetDampReuse,
       "rtMapSetDampSuppress": rtMapSetDampSuppress,
       "rtMapSetDampMaxDura": rtMapSetDampMaxDura,
       "rtMapSetDefaultInt": rtMapSetDefaultInt,
       "rtMapSetExtComRt": rtMapSetExtComRt,
       "rtMapSetExtComSoo": rtMapSetExtComSoo,
       "rtMapSetInt": rtMapSetInt,
       "rtMapSetIpDefNextHop": rtMapSetIpDefNextHop,
       "rtMapSetIpDF": rtMapSetIpDF,
       "rtMapSetIpNextHop": rtMapSetIpNextHop,
       "rtMapSetIpNextHopAttr": rtMapSetIpNextHopAttr,
       "rtMapSetIpPre": rtMapSetIpPre,
       "rtMapSetIpQosGrp": rtMapSetIpQosGrp,
       "rtMapSetIpTos": rtMapSetIpTos,
       "rtMapSetLevel": rtMapSetLevel,
       "rtMapSetLocalPre": rtMapSetLocalPre,
       "rtMapSetMetricVal": rtMapSetMetricVal,
       "rtMapSetMetricIgrpDelay": rtMapSetMetricIgrpDelay,
       "rtMapSetMetricIgrpRelia": rtMapSetMetricIgrpRelia,
       "rtMapSetMetricIgrpEffect": rtMapSetMetricIgrpEffect,
       "rtMapSetMetricIgrpMtu": rtMapSetMetricIgrpMtu,
       "rtMapSetMetricType": rtMapSetMetricType,
       "rtMapSetOrigin": rtMapSetOrigin,
       "rtMapSetOriEgpReAs": rtMapSetOriEgpReAs,
       "rtMapSetTag": rtMapSetTag,
       "rtMapSetWeight": rtMapSetWeight,
       "rtMapSetStatus": rtMapSetStatus,
       "rtMapSetComList": rtMapSetComList,
       "rtMapSetCommunity": rtMapSetCommunity,
       "rtMapSetAccess": rtMapSetAccess}
)
