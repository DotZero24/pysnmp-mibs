# SNMP MIB module (MAIPU-CAR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MAIPU-CAR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:09 2025
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

maipuCarMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Unsigned64(TextualConvention, Counter64):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Maipu_ObjectIdentity = ObjectIdentity
maipu = _Maipu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651)
)
_MpMgmt2_ObjectIdentity = ObjectIdentity
mpMgmt2 = _MpMgmt2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6)
)
_MpRouterTech_ObjectIdentity = ObjectIdentity
mpRouterTech = _MpRouterTech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2)
)
_MpRtQoSv2_ObjectIdentity = ObjectIdentity
mpRtQoSv2 = _MpRtQoSv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3)
)
_MaipuCarMIBObjects_ObjectIdentity = ObjectIdentity
maipuCarMIBObjects = _MaipuCarMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1)
)
_MpCarConfigs_ObjectIdentity = ObjectIdentity
mpCarConfigs = _MpCarConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1)
)
_MpCarInterfaceCfgTable_Object = MibTable
mpCarInterfaceCfgTable = _MpCarInterfaceCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mpCarInterfaceCfgTable.setStatus("current")
_MpCarInterfaceCfgEntry_Object = MibTableRow
mpCarInterfaceCfgEntry = _MpCarInterfaceCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 1, 1)
)
mpCarInterfaceCfgEntry.setIndexNames(
    (0, "MAIPU-CAR-MIB", "ifIndex"),
    (0, "MAIPU-CAR-MIB", "mpCarIFCfgDirection"),
    (0, "MAIPU-CAR-MIB", "mpCarIFCfgRowIndex"),
)
if mibBuilder.loadTexts:
    mpCarInterfaceCfgEntry.setStatus("current")


class _MpCarIFCfgDirection_Type(Integer32):
    """Custom type mpCarIFCfgDirection based on Integer32"""
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


_MpCarIFCfgDirection_Type.__name__ = "Integer32"
_MpCarIFCfgDirection_Object = MibTableColumn
mpCarIFCfgDirection = _MpCarIFCfgDirection_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 1, 1, 1),
    _MpCarIFCfgDirection_Type()
)
mpCarIFCfgDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpCarIFCfgDirection.setStatus("current")


class _MpCarIFCfgRowIndex_Type(Integer32):
    """Custom type mpCarIFCfgRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MpCarIFCfgRowIndex_Type.__name__ = "Integer32"
_MpCarIFCfgRowIndex_Object = MibTableColumn
mpCarIFCfgRowIndex = _MpCarIFCfgRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 1, 1, 2),
    _MpCarIFCfgRowIndex_Type()
)
mpCarIFCfgRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpCarIFCfgRowIndex.setStatus("current")


class _MpCarIFCfgType_Type(Integer32):
    """Custom type mpCarIFCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("accessList", 2))
    )


_MpCarIFCfgType_Type.__name__ = "Integer32"
_MpCarIFCfgType_Object = MibTableColumn
mpCarIFCfgType = _MpCarIFCfgType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 1, 1, 3),
    _MpCarIFCfgType_Type()
)
mpCarIFCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarIFCfgType.setStatus("current")


class _MpCarIFCfgAclName_Type(DisplayString):
    """Custom type mpCarIFCfgAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpCarIFCfgAclName_Type.__name__ = "DisplayString"
_MpCarIFCfgAclName_Object = MibTableColumn
mpCarIFCfgAclName = _MpCarIFCfgAclName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 1, 1, 4),
    _MpCarIFCfgAclName_Type()
)
mpCarIFCfgAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarIFCfgAclName.setStatus("current")
_MpCarIFCfgRate64_Type = Unsigned64
_MpCarIFCfgRate64_Object = MibTableColumn
mpCarIFCfgRate64 = _MpCarIFCfgRate64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 1, 1, 5),
    _MpCarIFCfgRate64_Type()
)
mpCarIFCfgRate64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarIFCfgRate64.setStatus("current")
if mibBuilder.loadTexts:
    mpCarIFCfgRate64.setUnits("bits/second")
_MpCarIFCfgBurstSize_Type = Integer32
_MpCarIFCfgBurstSize_Object = MibTableColumn
mpCarIFCfgBurstSize = _MpCarIFCfgBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 1, 1, 6),
    _MpCarIFCfgBurstSize_Type()
)
mpCarIFCfgBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarIFCfgBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mpCarIFCfgBurstSize.setUnits("bytes")
_MpCarIFCfgExtBurstSize_Type = Integer32
_MpCarIFCfgExtBurstSize_Object = MibTableColumn
mpCarIFCfgExtBurstSize = _MpCarIFCfgExtBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 1, 1, 7),
    _MpCarIFCfgExtBurstSize_Type()
)
mpCarIFCfgExtBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarIFCfgExtBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mpCarIFCfgExtBurstSize.setUnits("bytes")


class _MpCarIFCfgConformAction_Type(Integer32):
    """Custom type mpCarIFCfgConformAction based on Integer32"""
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
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("xmit", 2),
          ("continue", 3),
          ("precXmit", 4),
          ("precCont", 5),
          ("dscpXmit", 6),
          ("dscpCont", 7),
          ("mplsExpXmit", 8),
          ("mplsExpCont", 9),
          ("qosGroupXmit", 10),
          ("qosGroupCont", 11))
    )


_MpCarIFCfgConformAction_Type.__name__ = "Integer32"
_MpCarIFCfgConformAction_Object = MibTableColumn
mpCarIFCfgConformAction = _MpCarIFCfgConformAction_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 1, 1, 8),
    _MpCarIFCfgConformAction_Type()
)
mpCarIFCfgConformAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarIFCfgConformAction.setStatus("current")
_MpCarIFCfgConformSetValue_Type = Integer32
_MpCarIFCfgConformSetValue_Object = MibTableColumn
mpCarIFCfgConformSetValue = _MpCarIFCfgConformSetValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 1, 1, 9),
    _MpCarIFCfgConformSetValue_Type()
)
mpCarIFCfgConformSetValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarIFCfgConformSetValue.setStatus("current")


class _MpCarIFCfgExceedAction_Type(Integer32):
    """Custom type mpCarIFCfgExceedAction based on Integer32"""
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
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("xmit", 2),
          ("continue", 3),
          ("precXmit", 4),
          ("precCont", 5),
          ("dscpXmit", 6),
          ("dscpCont", 7),
          ("mplsExpXmit", 8),
          ("mplsExpCont", 9),
          ("qosGroupXmit", 10),
          ("qosGroupCont", 11))
    )


_MpCarIFCfgExceedAction_Type.__name__ = "Integer32"
_MpCarIFCfgExceedAction_Object = MibTableColumn
mpCarIFCfgExceedAction = _MpCarIFCfgExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 1, 1, 10),
    _MpCarIFCfgExceedAction_Type()
)
mpCarIFCfgExceedAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarIFCfgExceedAction.setStatus("current")
_MpCarIFCfgExceedSetValue_Type = Integer32
_MpCarIFCfgExceedSetValue_Object = MibTableColumn
mpCarIFCfgExceedSetValue = _MpCarIFCfgExceedSetValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 1, 1, 11),
    _MpCarIFCfgExceedSetValue_Type()
)
mpCarIFCfgExceedSetValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarIFCfgExceedSetValue.setStatus("current")


class _MpCarIFCfgColorMode_Type(Integer32):
    """Custom type mpCarIFCfgColorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("colorKeep", 2))
    )


_MpCarIFCfgColorMode_Type.__name__ = "Integer32"
_MpCarIFCfgColorMode_Object = MibTableColumn
mpCarIFCfgColorMode = _MpCarIFCfgColorMode_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 1, 1, 12),
    _MpCarIFCfgColorMode_Type()
)
mpCarIFCfgColorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarIFCfgColorMode.setStatus("current")
_MpCarFrameRelayVCCfgTable_Object = MibTable
mpCarFrameRelayVCCfgTable = _MpCarFrameRelayVCCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mpCarFrameRelayVCCfgTable.setStatus("current")
_MpCarFrameRelayVCCfgEntry_Object = MibTableRow
mpCarFrameRelayVCCfgEntry = _MpCarFrameRelayVCCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 2, 1)
)
mpCarFrameRelayVCCfgEntry.setIndexNames(
    (0, "MAIPU-CAR-MIB", "ifIndex"),
    (0, "MAIPU-CAR-MIB", "mpCarFRCfgDLCI"),
    (0, "MAIPU-CAR-MIB", "mpCarFRCfgDirection"),
    (0, "MAIPU-CAR-MIB", "mpCarFRCfgRowIndex"),
)
if mibBuilder.loadTexts:
    mpCarFrameRelayVCCfgEntry.setStatus("current")


class _MpCarFRCfgDLCI_Type(Unsigned32):
    """Custom type mpCarFRCfgDLCI based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1007),
    )


_MpCarFRCfgDLCI_Type.__name__ = "Unsigned32"
_MpCarFRCfgDLCI_Object = MibTableColumn
mpCarFRCfgDLCI = _MpCarFRCfgDLCI_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 2, 1, 1),
    _MpCarFRCfgDLCI_Type()
)
mpCarFRCfgDLCI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpCarFRCfgDLCI.setStatus("current")


class _MpCarFRCfgDirection_Type(Integer32):
    """Custom type mpCarFRCfgDirection based on Integer32"""
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


_MpCarFRCfgDirection_Type.__name__ = "Integer32"
_MpCarFRCfgDirection_Object = MibTableColumn
mpCarFRCfgDirection = _MpCarFRCfgDirection_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 2, 1, 2),
    _MpCarFRCfgDirection_Type()
)
mpCarFRCfgDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpCarFRCfgDirection.setStatus("current")


class _MpCarFRCfgRowIndex_Type(Integer32):
    """Custom type mpCarFRCfgRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MpCarFRCfgRowIndex_Type.__name__ = "Integer32"
_MpCarFRCfgRowIndex_Object = MibTableColumn
mpCarFRCfgRowIndex = _MpCarFRCfgRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 2, 1, 3),
    _MpCarFRCfgRowIndex_Type()
)
mpCarFRCfgRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpCarFRCfgRowIndex.setStatus("current")


class _MpCarFRCfgType_Type(Integer32):
    """Custom type mpCarFRCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("accessList", 2))
    )


_MpCarFRCfgType_Type.__name__ = "Integer32"
_MpCarFRCfgType_Object = MibTableColumn
mpCarFRCfgType = _MpCarFRCfgType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 2, 1, 4),
    _MpCarFRCfgType_Type()
)
mpCarFRCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarFRCfgType.setStatus("current")


class _MpCarFRCfgAclName_Type(DisplayString):
    """Custom type mpCarFRCfgAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpCarFRCfgAclName_Type.__name__ = "DisplayString"
_MpCarFRCfgAclName_Object = MibTableColumn
mpCarFRCfgAclName = _MpCarFRCfgAclName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 2, 1, 5),
    _MpCarFRCfgAclName_Type()
)
mpCarFRCfgAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarFRCfgAclName.setStatus("current")
_MpCarFRCfgRate64_Type = Unsigned64
_MpCarFRCfgRate64_Object = MibTableColumn
mpCarFRCfgRate64 = _MpCarFRCfgRate64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 2, 1, 6),
    _MpCarFRCfgRate64_Type()
)
mpCarFRCfgRate64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarFRCfgRate64.setStatus("current")
if mibBuilder.loadTexts:
    mpCarFRCfgRate64.setUnits("bits/second")
_MpCarFRCfgBurstSize_Type = Integer32
_MpCarFRCfgBurstSize_Object = MibTableColumn
mpCarFRCfgBurstSize = _MpCarFRCfgBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 2, 1, 7),
    _MpCarFRCfgBurstSize_Type()
)
mpCarFRCfgBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarFRCfgBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mpCarFRCfgBurstSize.setUnits("bytes")
_MpCarFRCfgExtBurstSize_Type = Integer32
_MpCarFRCfgExtBurstSize_Object = MibTableColumn
mpCarFRCfgExtBurstSize = _MpCarFRCfgExtBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 2, 1, 8),
    _MpCarFRCfgExtBurstSize_Type()
)
mpCarFRCfgExtBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarFRCfgExtBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mpCarFRCfgExtBurstSize.setUnits("bytes")


class _MpCarFRCfgConformAction_Type(Integer32):
    """Custom type mpCarFRCfgConformAction based on Integer32"""
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
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("xmit", 2),
          ("continue", 3),
          ("precXmit", 4),
          ("precCont", 5),
          ("dscpXmit", 6),
          ("dscpCont", 7),
          ("mplsExpXmit", 8),
          ("mplsExpCont", 9),
          ("qosGroupXmit", 10),
          ("qosGroupCont", 11))
    )


_MpCarFRCfgConformAction_Type.__name__ = "Integer32"
_MpCarFRCfgConformAction_Object = MibTableColumn
mpCarFRCfgConformAction = _MpCarFRCfgConformAction_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 2, 1, 9),
    _MpCarFRCfgConformAction_Type()
)
mpCarFRCfgConformAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarFRCfgConformAction.setStatus("current")
_MpCarFRCfgConformSetValue_Type = Integer32
_MpCarFRCfgConformSetValue_Object = MibTableColumn
mpCarFRCfgConformSetValue = _MpCarFRCfgConformSetValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 2, 1, 10),
    _MpCarFRCfgConformSetValue_Type()
)
mpCarFRCfgConformSetValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarFRCfgConformSetValue.setStatus("current")


class _MpCarFRCfgExceedAction_Type(Integer32):
    """Custom type mpCarFRCfgExceedAction based on Integer32"""
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
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("xmit", 2),
          ("continue", 3),
          ("precXmit", 4),
          ("precCont", 5),
          ("dscpXmit", 6),
          ("dscpCont", 7),
          ("mplsExpXmit", 8),
          ("mplsExpCont", 9),
          ("qosGroupXmit", 10),
          ("qosGroupCont", 11))
    )


_MpCarFRCfgExceedAction_Type.__name__ = "Integer32"
_MpCarFRCfgExceedAction_Object = MibTableColumn
mpCarFRCfgExceedAction = _MpCarFRCfgExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 2, 1, 11),
    _MpCarFRCfgExceedAction_Type()
)
mpCarFRCfgExceedAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarFRCfgExceedAction.setStatus("current")
_MpCarFRCfgExceedSetValue_Type = Integer32
_MpCarFRCfgExceedSetValue_Object = MibTableColumn
mpCarFRCfgExceedSetValue = _MpCarFRCfgExceedSetValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 2, 1, 12),
    _MpCarFRCfgExceedSetValue_Type()
)
mpCarFRCfgExceedSetValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarFRCfgExceedSetValue.setStatus("current")


class _MpCarFRCfgColorMode_Type(Integer32):
    """Custom type mpCarFRCfgColorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("colorKeep", 2))
    )


_MpCarFRCfgColorMode_Type.__name__ = "Integer32"
_MpCarFRCfgColorMode_Object = MibTableColumn
mpCarFRCfgColorMode = _MpCarFRCfgColorMode_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 2, 1, 13),
    _MpCarFRCfgColorMode_Type()
)
mpCarFRCfgColorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarFRCfgColorMode.setStatus("current")
_MpCarATMPVCCfgTable_Object = MibTable
mpCarATMPVCCfgTable = _MpCarATMPVCCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mpCarATMPVCCfgTable.setStatus("current")
_MpCarATMPVCCfgEntry_Object = MibTableRow
mpCarATMPVCCfgEntry = _MpCarATMPVCCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 3, 1)
)
mpCarATMPVCCfgEntry.setIndexNames(
    (0, "MAIPU-CAR-MIB", "ifIndex"),
    (0, "MAIPU-CAR-MIB", "mpCarATMCfgVPI"),
    (0, "MAIPU-CAR-MIB", "mpCarATMCfgVCI"),
    (0, "MAIPU-CAR-MIB", "mpCarATMCfgDirection"),
    (0, "MAIPU-CAR-MIB", "mpCarATMCfgRowIndex"),
)
if mibBuilder.loadTexts:
    mpCarATMPVCCfgEntry.setStatus("current")


class _MpCarATMCfgVPI_Type(Unsigned32):
    """Custom type mpCarATMCfgVPI based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MpCarATMCfgVPI_Type.__name__ = "Unsigned32"
_MpCarATMCfgVPI_Object = MibTableColumn
mpCarATMCfgVPI = _MpCarATMCfgVPI_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 3, 1, 1),
    _MpCarATMCfgVPI_Type()
)
mpCarATMCfgVPI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpCarATMCfgVPI.setStatus("current")


class _MpCarATMCfgVCI_Type(Unsigned32):
    """Custom type mpCarATMCfgVCI based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpCarATMCfgVCI_Type.__name__ = "Unsigned32"
_MpCarATMCfgVCI_Object = MibTableColumn
mpCarATMCfgVCI = _MpCarATMCfgVCI_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 3, 1, 2),
    _MpCarATMCfgVCI_Type()
)
mpCarATMCfgVCI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpCarATMCfgVCI.setStatus("current")


class _MpCarATMCfgDirection_Type(Integer32):
    """Custom type mpCarATMCfgDirection based on Integer32"""
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


_MpCarATMCfgDirection_Type.__name__ = "Integer32"
_MpCarATMCfgDirection_Object = MibTableColumn
mpCarATMCfgDirection = _MpCarATMCfgDirection_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 3, 1, 3),
    _MpCarATMCfgDirection_Type()
)
mpCarATMCfgDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpCarATMCfgDirection.setStatus("current")


class _MpCarATMCfgRowIndex_Type(Integer32):
    """Custom type mpCarATMCfgRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MpCarATMCfgRowIndex_Type.__name__ = "Integer32"
_MpCarATMCfgRowIndex_Object = MibTableColumn
mpCarATMCfgRowIndex = _MpCarATMCfgRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 3, 1, 4),
    _MpCarATMCfgRowIndex_Type()
)
mpCarATMCfgRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpCarATMCfgRowIndex.setStatus("current")


class _MpCarATMCfgType_Type(Integer32):
    """Custom type mpCarATMCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("accessList", 2))
    )


_MpCarATMCfgType_Type.__name__ = "Integer32"
_MpCarATMCfgType_Object = MibTableColumn
mpCarATMCfgType = _MpCarATMCfgType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 3, 1, 5),
    _MpCarATMCfgType_Type()
)
mpCarATMCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarATMCfgType.setStatus("current")


class _MpCarATMCfgAclName_Type(DisplayString):
    """Custom type mpCarATMCfgAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpCarATMCfgAclName_Type.__name__ = "DisplayString"
_MpCarATMCfgAclName_Object = MibTableColumn
mpCarATMCfgAclName = _MpCarATMCfgAclName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 3, 1, 6),
    _MpCarATMCfgAclName_Type()
)
mpCarATMCfgAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarATMCfgAclName.setStatus("current")
_MpCarATMCfgRate64_Type = Unsigned64
_MpCarATMCfgRate64_Object = MibTableColumn
mpCarATMCfgRate64 = _MpCarATMCfgRate64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 3, 1, 7),
    _MpCarATMCfgRate64_Type()
)
mpCarATMCfgRate64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarATMCfgRate64.setStatus("current")
if mibBuilder.loadTexts:
    mpCarATMCfgRate64.setUnits("bits/second")
_MpCarATMCfgBurstSize_Type = Integer32
_MpCarATMCfgBurstSize_Object = MibTableColumn
mpCarATMCfgBurstSize = _MpCarATMCfgBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 3, 1, 8),
    _MpCarATMCfgBurstSize_Type()
)
mpCarATMCfgBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarATMCfgBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mpCarATMCfgBurstSize.setUnits("bytes")
_MpCarATMCfgExtBurstSize_Type = Integer32
_MpCarATMCfgExtBurstSize_Object = MibTableColumn
mpCarATMCfgExtBurstSize = _MpCarATMCfgExtBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 3, 1, 9),
    _MpCarATMCfgExtBurstSize_Type()
)
mpCarATMCfgExtBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarATMCfgExtBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mpCarATMCfgExtBurstSize.setUnits("bytes")


class _MpCarATMCfgConformAction_Type(Integer32):
    """Custom type mpCarATMCfgConformAction based on Integer32"""
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
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("xmit", 2),
          ("continue", 3),
          ("precXmit", 4),
          ("precCont", 5),
          ("dscpXmit", 6),
          ("dscpCont", 7),
          ("mplsExpXmit", 8),
          ("mplsExpCont", 9),
          ("qosGroupXmit", 10),
          ("qosGroupCont", 11))
    )


_MpCarATMCfgConformAction_Type.__name__ = "Integer32"
_MpCarATMCfgConformAction_Object = MibTableColumn
mpCarATMCfgConformAction = _MpCarATMCfgConformAction_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 3, 1, 10),
    _MpCarATMCfgConformAction_Type()
)
mpCarATMCfgConformAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarATMCfgConformAction.setStatus("current")
_MpCarATMCfgConformSetValue_Type = Integer32
_MpCarATMCfgConformSetValue_Object = MibTableColumn
mpCarATMCfgConformSetValue = _MpCarATMCfgConformSetValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 3, 1, 11),
    _MpCarATMCfgConformSetValue_Type()
)
mpCarATMCfgConformSetValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarATMCfgConformSetValue.setStatus("current")


class _MpCarATMCfgExceedAction_Type(Integer32):
    """Custom type mpCarATMCfgExceedAction based on Integer32"""
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
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("xmit", 2),
          ("continue", 3),
          ("precXmit", 4),
          ("precCont", 5),
          ("dscpXmit", 6),
          ("dscpCont", 7),
          ("mplsExpXmit", 8),
          ("mplsExpCont", 9),
          ("qosGroupXmit", 10),
          ("qosGroupCont", 11))
    )


_MpCarATMCfgExceedAction_Type.__name__ = "Integer32"
_MpCarATMCfgExceedAction_Object = MibTableColumn
mpCarATMCfgExceedAction = _MpCarATMCfgExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 3, 1, 12),
    _MpCarATMCfgExceedAction_Type()
)
mpCarATMCfgExceedAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarATMCfgExceedAction.setStatus("current")
_MpCarATMCfgExceedSetValue_Type = Integer32
_MpCarATMCfgExceedSetValue_Object = MibTableColumn
mpCarATMCfgExceedSetValue = _MpCarATMCfgExceedSetValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 3, 1, 13),
    _MpCarATMCfgExceedSetValue_Type()
)
mpCarATMCfgExceedSetValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarATMCfgExceedSetValue.setStatus("current")


class _MpCarATMCfgColorMode_Type(Integer32):
    """Custom type mpCarATMCfgColorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("colorKeep", 2))
    )


_MpCarATMCfgColorMode_Type.__name__ = "Integer32"
_MpCarATMCfgColorMode_Object = MibTableColumn
mpCarATMCfgColorMode = _MpCarATMCfgColorMode_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 1, 3, 1, 14),
    _MpCarATMCfgColorMode_Type()
)
mpCarATMCfgColorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarATMCfgColorMode.setStatus("current")
_MpCarStats_ObjectIdentity = ObjectIdentity
mpCarStats = _MpCarStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 2)
)
_MpCarInterfaceStatTable_Object = MibTable
mpCarInterfaceStatTable = _MpCarInterfaceStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mpCarInterfaceStatTable.setStatus("current")
_MpCarInterfaceStatEntry_Object = MibTableRow
mpCarInterfaceStatEntry = _MpCarInterfaceStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 2, 1, 1)
)
mpCarInterfaceStatEntry.setIndexNames(
    (0, "MAIPU-CAR-MIB", "ifIndex"),
    (0, "MAIPU-CAR-MIB", "mpCarIFCfgDirection"),
    (0, "MAIPU-CAR-MIB", "mpCarIFCfgRowIndex"),
)
if mibBuilder.loadTexts:
    mpCarInterfaceStatEntry.setStatus("current")
_MpCarIFStatSwitchedPkts64_Type = Counter64
_MpCarIFStatSwitchedPkts64_Object = MibTableColumn
mpCarIFStatSwitchedPkts64 = _MpCarIFStatSwitchedPkts64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 2, 1, 1, 1),
    _MpCarIFStatSwitchedPkts64_Type()
)
mpCarIFStatSwitchedPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarIFStatSwitchedPkts64.setStatus("current")
if mibBuilder.loadTexts:
    mpCarIFStatSwitchedPkts64.setUnits("packets")
_MpCarIFStatSwitchedBytes64_Type = Counter64
_MpCarIFStatSwitchedBytes64_Object = MibTableColumn
mpCarIFStatSwitchedBytes64 = _MpCarIFStatSwitchedBytes64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 2, 1, 1, 2),
    _MpCarIFStatSwitchedBytes64_Type()
)
mpCarIFStatSwitchedBytes64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarIFStatSwitchedBytes64.setStatus("current")
if mibBuilder.loadTexts:
    mpCarIFStatSwitchedBytes64.setUnits("bytes")
_MpCarIFStatFilteredPkts64_Type = Counter64
_MpCarIFStatFilteredPkts64_Object = MibTableColumn
mpCarIFStatFilteredPkts64 = _MpCarIFStatFilteredPkts64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 2, 1, 1, 3),
    _MpCarIFStatFilteredPkts64_Type()
)
mpCarIFStatFilteredPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarIFStatFilteredPkts64.setStatus("current")
if mibBuilder.loadTexts:
    mpCarIFStatFilteredPkts64.setUnits("packets")
_MpCarIFStatFilteredBytes64_Type = Counter64
_MpCarIFStatFilteredBytes64_Object = MibTableColumn
mpCarIFStatFilteredBytes64 = _MpCarIFStatFilteredBytes64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 2, 1, 1, 4),
    _MpCarIFStatFilteredBytes64_Type()
)
mpCarIFStatFilteredBytes64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarIFStatFilteredBytes64.setStatus("current")
if mibBuilder.loadTexts:
    mpCarIFStatFilteredBytes64.setUnits("bytes")
_MpCarIFStatCurBurst_Type = Gauge32
_MpCarIFStatCurBurst_Object = MibTableColumn
mpCarIFStatCurBurst = _MpCarIFStatCurBurst_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 2, 1, 1, 5),
    _MpCarIFStatCurBurst_Type()
)
mpCarIFStatCurBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarIFStatCurBurst.setStatus("current")
if mibBuilder.loadTexts:
    mpCarIFStatCurBurst.setUnits("bytes")
_MpCarFrameRelayVCStatTable_Object = MibTable
mpCarFrameRelayVCStatTable = _MpCarFrameRelayVCStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mpCarFrameRelayVCStatTable.setStatus("current")
_MpCarFrameRelayVCStatEntry_Object = MibTableRow
mpCarFrameRelayVCStatEntry = _MpCarFrameRelayVCStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 2, 2, 1)
)
mpCarFrameRelayVCStatEntry.setIndexNames(
    (0, "MAIPU-CAR-MIB", "ifIndex"),
    (0, "MAIPU-CAR-MIB", "mpCarFRCfgDLCI"),
    (0, "MAIPU-CAR-MIB", "mpCarFRCfgDirection"),
    (0, "MAIPU-CAR-MIB", "mpCarFRCfgRowIndex"),
)
if mibBuilder.loadTexts:
    mpCarFrameRelayVCStatEntry.setStatus("current")
_MpCarFRStatSwitchedPkts64_Type = Counter64
_MpCarFRStatSwitchedPkts64_Object = MibTableColumn
mpCarFRStatSwitchedPkts64 = _MpCarFRStatSwitchedPkts64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 2, 2, 1, 1),
    _MpCarFRStatSwitchedPkts64_Type()
)
mpCarFRStatSwitchedPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarFRStatSwitchedPkts64.setStatus("current")
if mibBuilder.loadTexts:
    mpCarFRStatSwitchedPkts64.setUnits("packets")
_MpCarFRStatSwitchedBytes64_Type = Counter64
_MpCarFRStatSwitchedBytes64_Object = MibTableColumn
mpCarFRStatSwitchedBytes64 = _MpCarFRStatSwitchedBytes64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 2, 2, 1, 2),
    _MpCarFRStatSwitchedBytes64_Type()
)
mpCarFRStatSwitchedBytes64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarFRStatSwitchedBytes64.setStatus("current")
if mibBuilder.loadTexts:
    mpCarFRStatSwitchedBytes64.setUnits("bytes")
_MpCarFRStatFilteredPkts64_Type = Counter64
_MpCarFRStatFilteredPkts64_Object = MibTableColumn
mpCarFRStatFilteredPkts64 = _MpCarFRStatFilteredPkts64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 2, 2, 1, 3),
    _MpCarFRStatFilteredPkts64_Type()
)
mpCarFRStatFilteredPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarFRStatFilteredPkts64.setStatus("current")
if mibBuilder.loadTexts:
    mpCarFRStatFilteredPkts64.setUnits("packets")
_MpCarFRStatFilteredBytes64_Type = Counter64
_MpCarFRStatFilteredBytes64_Object = MibTableColumn
mpCarFRStatFilteredBytes64 = _MpCarFRStatFilteredBytes64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 2, 2, 1, 4),
    _MpCarFRStatFilteredBytes64_Type()
)
mpCarFRStatFilteredBytes64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarFRStatFilteredBytes64.setStatus("current")
if mibBuilder.loadTexts:
    mpCarFRStatFilteredBytes64.setUnits("bytes")
_MpCarFRStatCurBurst_Type = Gauge32
_MpCarFRStatCurBurst_Object = MibTableColumn
mpCarFRStatCurBurst = _MpCarFRStatCurBurst_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 2, 2, 1, 5),
    _MpCarFRStatCurBurst_Type()
)
mpCarFRStatCurBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarFRStatCurBurst.setStatus("current")
if mibBuilder.loadTexts:
    mpCarFRStatCurBurst.setUnits("bytes")
_MpCarATMPVCStatTable_Object = MibTable
mpCarATMPVCStatTable = _MpCarATMPVCStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mpCarATMPVCStatTable.setStatus("current")
_MpCarATMPVCStatEntry_Object = MibTableRow
mpCarATMPVCStatEntry = _MpCarATMPVCStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 2, 3, 1)
)
mpCarATMPVCStatEntry.setIndexNames(
    (0, "MAIPU-CAR-MIB", "ifIndex"),
    (0, "MAIPU-CAR-MIB", "mpCarATMCfgVPI"),
    (0, "MAIPU-CAR-MIB", "mpCarATMCfgVCI"),
    (0, "MAIPU-CAR-MIB", "mpCarATMCfgDirection"),
    (0, "MAIPU-CAR-MIB", "mpCarATMCfgRowIndex"),
)
if mibBuilder.loadTexts:
    mpCarATMPVCStatEntry.setStatus("current")
_MpCarATMStatSwitchedPkts64_Type = Counter64
_MpCarATMStatSwitchedPkts64_Object = MibTableColumn
mpCarATMStatSwitchedPkts64 = _MpCarATMStatSwitchedPkts64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 2, 3, 1, 1),
    _MpCarATMStatSwitchedPkts64_Type()
)
mpCarATMStatSwitchedPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarATMStatSwitchedPkts64.setStatus("current")
if mibBuilder.loadTexts:
    mpCarATMStatSwitchedPkts64.setUnits("packets")
_MpCarATMStatSwitchedBytes64_Type = Counter64
_MpCarATMStatSwitchedBytes64_Object = MibTableColumn
mpCarATMStatSwitchedBytes64 = _MpCarATMStatSwitchedBytes64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 2, 3, 1, 2),
    _MpCarATMStatSwitchedBytes64_Type()
)
mpCarATMStatSwitchedBytes64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarATMStatSwitchedBytes64.setStatus("current")
if mibBuilder.loadTexts:
    mpCarATMStatSwitchedBytes64.setUnits("bytes")
_MpCarATMStatFilteredPkts64_Type = Counter64
_MpCarATMStatFilteredPkts64_Object = MibTableColumn
mpCarATMStatFilteredPkts64 = _MpCarATMStatFilteredPkts64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 2, 3, 1, 3),
    _MpCarATMStatFilteredPkts64_Type()
)
mpCarATMStatFilteredPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarATMStatFilteredPkts64.setStatus("current")
if mibBuilder.loadTexts:
    mpCarATMStatFilteredPkts64.setUnits("packets")
_MpCarATMStatFilteredBytes64_Type = Counter64
_MpCarATMStatFilteredBytes64_Object = MibTableColumn
mpCarATMStatFilteredBytes64 = _MpCarATMStatFilteredBytes64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 2, 3, 1, 4),
    _MpCarATMStatFilteredBytes64_Type()
)
mpCarATMStatFilteredBytes64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarATMStatFilteredBytes64.setStatus("current")
if mibBuilder.loadTexts:
    mpCarATMStatFilteredBytes64.setUnits("bytes")
_MpCarATMStatCurBurst_Type = Gauge32
_MpCarATMStatCurBurst_Object = MibTableColumn
mpCarATMStatCurBurst = _MpCarATMStatCurBurst_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 1, 1, 2, 3, 1, 5),
    _MpCarATMStatCurBurst_Type()
)
mpCarATMStatCurBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCarATMStatCurBurst.setStatus("current")
if mibBuilder.loadTexts:
    mpCarATMStatCurBurst.setUnits("bytes")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MAIPU-CAR-MIB",
    **{"Unsigned64": Unsigned64,
       "maipu": maipu,
       "mpMgmt2": mpMgmt2,
       "mpRouterTech": mpRouterTech,
       "mpRtQoSv2": mpRtQoSv2,
       "maipuCarMIB": maipuCarMIB,
       "maipuCarMIBObjects": maipuCarMIBObjects,
       "mpCarConfigs": mpCarConfigs,
       "mpCarInterfaceCfgTable": mpCarInterfaceCfgTable,
       "mpCarInterfaceCfgEntry": mpCarInterfaceCfgEntry,
       "mpCarIFCfgDirection": mpCarIFCfgDirection,
       "mpCarIFCfgRowIndex": mpCarIFCfgRowIndex,
       "mpCarIFCfgType": mpCarIFCfgType,
       "mpCarIFCfgAclName": mpCarIFCfgAclName,
       "mpCarIFCfgRate64": mpCarIFCfgRate64,
       "mpCarIFCfgBurstSize": mpCarIFCfgBurstSize,
       "mpCarIFCfgExtBurstSize": mpCarIFCfgExtBurstSize,
       "mpCarIFCfgConformAction": mpCarIFCfgConformAction,
       "mpCarIFCfgConformSetValue": mpCarIFCfgConformSetValue,
       "mpCarIFCfgExceedAction": mpCarIFCfgExceedAction,
       "mpCarIFCfgExceedSetValue": mpCarIFCfgExceedSetValue,
       "mpCarIFCfgColorMode": mpCarIFCfgColorMode,
       "mpCarFrameRelayVCCfgTable": mpCarFrameRelayVCCfgTable,
       "mpCarFrameRelayVCCfgEntry": mpCarFrameRelayVCCfgEntry,
       "mpCarFRCfgDLCI": mpCarFRCfgDLCI,
       "mpCarFRCfgDirection": mpCarFRCfgDirection,
       "mpCarFRCfgRowIndex": mpCarFRCfgRowIndex,
       "mpCarFRCfgType": mpCarFRCfgType,
       "mpCarFRCfgAclName": mpCarFRCfgAclName,
       "mpCarFRCfgRate64": mpCarFRCfgRate64,
       "mpCarFRCfgBurstSize": mpCarFRCfgBurstSize,
       "mpCarFRCfgExtBurstSize": mpCarFRCfgExtBurstSize,
       "mpCarFRCfgConformAction": mpCarFRCfgConformAction,
       "mpCarFRCfgConformSetValue": mpCarFRCfgConformSetValue,
       "mpCarFRCfgExceedAction": mpCarFRCfgExceedAction,
       "mpCarFRCfgExceedSetValue": mpCarFRCfgExceedSetValue,
       "mpCarFRCfgColorMode": mpCarFRCfgColorMode,
       "mpCarATMPVCCfgTable": mpCarATMPVCCfgTable,
       "mpCarATMPVCCfgEntry": mpCarATMPVCCfgEntry,
       "mpCarATMCfgVPI": mpCarATMCfgVPI,
       "mpCarATMCfgVCI": mpCarATMCfgVCI,
       "mpCarATMCfgDirection": mpCarATMCfgDirection,
       "mpCarATMCfgRowIndex": mpCarATMCfgRowIndex,
       "mpCarATMCfgType": mpCarATMCfgType,
       "mpCarATMCfgAclName": mpCarATMCfgAclName,
       "mpCarATMCfgRate64": mpCarATMCfgRate64,
       "mpCarATMCfgBurstSize": mpCarATMCfgBurstSize,
       "mpCarATMCfgExtBurstSize": mpCarATMCfgExtBurstSize,
       "mpCarATMCfgConformAction": mpCarATMCfgConformAction,
       "mpCarATMCfgConformSetValue": mpCarATMCfgConformSetValue,
       "mpCarATMCfgExceedAction": mpCarATMCfgExceedAction,
       "mpCarATMCfgExceedSetValue": mpCarATMCfgExceedSetValue,
       "mpCarATMCfgColorMode": mpCarATMCfgColorMode,
       "mpCarStats": mpCarStats,
       "mpCarInterfaceStatTable": mpCarInterfaceStatTable,
       "mpCarInterfaceStatEntry": mpCarInterfaceStatEntry,
       "mpCarIFStatSwitchedPkts64": mpCarIFStatSwitchedPkts64,
       "mpCarIFStatSwitchedBytes64": mpCarIFStatSwitchedBytes64,
       "mpCarIFStatFilteredPkts64": mpCarIFStatFilteredPkts64,
       "mpCarIFStatFilteredBytes64": mpCarIFStatFilteredBytes64,
       "mpCarIFStatCurBurst": mpCarIFStatCurBurst,
       "mpCarFrameRelayVCStatTable": mpCarFrameRelayVCStatTable,
       "mpCarFrameRelayVCStatEntry": mpCarFrameRelayVCStatEntry,
       "mpCarFRStatSwitchedPkts64": mpCarFRStatSwitchedPkts64,
       "mpCarFRStatSwitchedBytes64": mpCarFRStatSwitchedBytes64,
       "mpCarFRStatFilteredPkts64": mpCarFRStatFilteredPkts64,
       "mpCarFRStatFilteredBytes64": mpCarFRStatFilteredBytes64,
       "mpCarFRStatCurBurst": mpCarFRStatCurBurst,
       "mpCarATMPVCStatTable": mpCarATMPVCStatTable,
       "mpCarATMPVCStatEntry": mpCarATMPVCStatEntry,
       "mpCarATMStatSwitchedPkts64": mpCarATMStatSwitchedPkts64,
       "mpCarATMStatSwitchedBytes64": mpCarATMStatSwitchedBytes64,
       "mpCarATMStatFilteredPkts64": mpCarATMStatFilteredPkts64,
       "mpCarATMStatFilteredBytes64": mpCarATMStatFilteredBytes64,
       "mpCarATMStatCurBurst": mpCarATMStatCurBurst}
)
