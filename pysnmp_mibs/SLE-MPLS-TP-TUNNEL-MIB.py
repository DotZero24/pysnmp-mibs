# SNMP MIB module (SLE-MPLS-TP-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/dasan/SLE-MPLS-TP-TUNNEL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:11:40 2025
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

(sleMgmt,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "sleMgmt")

(InterfaceIndexOrZero,
 ifCounterDiscontinuityGroup,
 ifGeneralInformationGroup) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifCounterDiscontinuityGroup",
    "ifGeneralInformationGroup")

(MplsCcId,
 MplsIccId) = mibBuilder.importSymbols(
    "MPLS-TC-EXT-STD-MIB",
    "MplsCcId",
    "MplsIccId")

(MplsLabel,
 mplsStdMIB) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsLabel",
    "mplsStdMIB")

(SleControlRequestResultType,
 SleControlStatusType) = mibBuilder.importSymbols(
    "SLE-TC-MIB",
    "SleControlRequestResultType",
    "SleControlStatusType")

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
 iso,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "iso",
    "zeroDotZero")

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sleMplsTpTunnel = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14)
)
if mibBuilder.loadTexts:
    sleMplsTpTunnel.setRevisions(
        ("2004-06-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleMpls_ObjectIdentity = ObjectIdentity
sleMpls = _SleMpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16)
)
if mibBuilder.loadTexts:
    sleMpls.setStatus("current")
_SleMplsTpTunnelCfg_ObjectIdentity = ObjectIdentity
sleMplsTpTunnelCfg = _SleMplsTpTunnelCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1)
)
_SleMplsTpTunnelCfgInfoTable_Object = MibTable
sleMplsTpTunnelCfgInfoTable = _SleMplsTpTunnelCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1)
)
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoTable.setStatus("current")
_SleMplsTpTunnelCfgInfoEntry_Object = MibTableRow
sleMplsTpTunnelCfgInfoEntry = _SleMplsTpTunnelCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1)
)
sleMplsTpTunnelCfgInfoEntry.setIndexNames(
    (0, "SLE-MPLS-TP-TUNNEL-MIB", "sleMplsTpTunnelCfgInfoIndex"),
)
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoEntry.setStatus("current")


class _SleMplsTpTunnelCfgInfoIndex_Type(Unsigned32):
    """Custom type sleMplsTpTunnelCfgInfoIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleMplsTpTunnelCfgInfoIndex_Type.__name__ = "Unsigned32"
_SleMplsTpTunnelCfgInfoIndex_Object = MibTableColumn
sleMplsTpTunnelCfgInfoIndex = _SleMplsTpTunnelCfgInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 1),
    _SleMplsTpTunnelCfgInfoIndex_Type()
)
sleMplsTpTunnelCfgInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoIndex.setStatus("current")


class _SleMplsTpTunnelCfgInfoName_Type(OctetString):
    """Custom type sleMplsTpTunnelCfgInfoName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SleMplsTpTunnelCfgInfoName_Type.__name__ = "OctetString"
_SleMplsTpTunnelCfgInfoName_Object = MibTableColumn
sleMplsTpTunnelCfgInfoName = _SleMplsTpTunnelCfgInfoName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 2),
    _SleMplsTpTunnelCfgInfoName_Type()
)
sleMplsTpTunnelCfgInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoName.setStatus("current")


class _SleMplsTpTunnelCfgInfoId_Type(Unsigned32):
    """Custom type sleMplsTpTunnelCfgInfoId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleMplsTpTunnelCfgInfoId_Type.__name__ = "Unsigned32"
_SleMplsTpTunnelCfgInfoId_Object = MibTableColumn
sleMplsTpTunnelCfgInfoId = _SleMplsTpTunnelCfgInfoId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 3),
    _SleMplsTpTunnelCfgInfoId_Type()
)
sleMplsTpTunnelCfgInfoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoId.setStatus("current")


class _SleMplsTpTunnelCfgInfoSrcIdType_Type(Integer32):
    """Custom type sleMplsTpTunnelCfgInfoSrcIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ietf", 1),
          ("itut", 2))
    )


_SleMplsTpTunnelCfgInfoSrcIdType_Type.__name__ = "Integer32"
_SleMplsTpTunnelCfgInfoSrcIdType_Object = MibTableColumn
sleMplsTpTunnelCfgInfoSrcIdType = _SleMplsTpTunnelCfgInfoSrcIdType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 4),
    _SleMplsTpTunnelCfgInfoSrcIdType_Type()
)
sleMplsTpTunnelCfgInfoSrcIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoSrcIdType.setStatus("current")


class _SleMplsTpTunnelCfgInfoSrcGId_Type(Unsigned32):
    """Custom type sleMplsTpTunnelCfgInfoSrcGId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SleMplsTpTunnelCfgInfoSrcGId_Type.__name__ = "Unsigned32"
_SleMplsTpTunnelCfgInfoSrcGId_Object = MibTableColumn
sleMplsTpTunnelCfgInfoSrcGId = _SleMplsTpTunnelCfgInfoSrcGId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 5),
    _SleMplsTpTunnelCfgInfoSrcGId_Type()
)
sleMplsTpTunnelCfgInfoSrcGId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoSrcGId.setStatus("current")
_SleMplsTpTunnelCfgInfoSrcCc_Type = MplsCcId
_SleMplsTpTunnelCfgInfoSrcCc_Object = MibTableColumn
sleMplsTpTunnelCfgInfoSrcCc = _SleMplsTpTunnelCfgInfoSrcCc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 6),
    _SleMplsTpTunnelCfgInfoSrcCc_Type()
)
sleMplsTpTunnelCfgInfoSrcCc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoSrcCc.setStatus("current")
_SleMplsTpTunnelCfgInfoSrcIcc_Type = MplsIccId
_SleMplsTpTunnelCfgInfoSrcIcc_Object = MibTableColumn
sleMplsTpTunnelCfgInfoSrcIcc = _SleMplsTpTunnelCfgInfoSrcIcc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 7),
    _SleMplsTpTunnelCfgInfoSrcIcc_Type()
)
sleMplsTpTunnelCfgInfoSrcIcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoSrcIcc.setStatus("current")
_SleMplsTpTunnelCfgInfoSrcNodeId_Type = IpAddress
_SleMplsTpTunnelCfgInfoSrcNodeId_Object = MibTableColumn
sleMplsTpTunnelCfgInfoSrcNodeId = _SleMplsTpTunnelCfgInfoSrcNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 8),
    _SleMplsTpTunnelCfgInfoSrcNodeId_Type()
)
sleMplsTpTunnelCfgInfoSrcNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoSrcNodeId.setStatus("current")


class _SleMplsTpTunnelCfgInfoDestIdType_Type(Integer32):
    """Custom type sleMplsTpTunnelCfgInfoDestIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ietf", 1),
          ("itut", 2))
    )


_SleMplsTpTunnelCfgInfoDestIdType_Type.__name__ = "Integer32"
_SleMplsTpTunnelCfgInfoDestIdType_Object = MibTableColumn
sleMplsTpTunnelCfgInfoDestIdType = _SleMplsTpTunnelCfgInfoDestIdType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 9),
    _SleMplsTpTunnelCfgInfoDestIdType_Type()
)
sleMplsTpTunnelCfgInfoDestIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoDestIdType.setStatus("current")


class _SleMplsTpTunnelCfgInfoDestGId_Type(Unsigned32):
    """Custom type sleMplsTpTunnelCfgInfoDestGId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SleMplsTpTunnelCfgInfoDestGId_Type.__name__ = "Unsigned32"
_SleMplsTpTunnelCfgInfoDestGId_Object = MibTableColumn
sleMplsTpTunnelCfgInfoDestGId = _SleMplsTpTunnelCfgInfoDestGId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 10),
    _SleMplsTpTunnelCfgInfoDestGId_Type()
)
sleMplsTpTunnelCfgInfoDestGId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoDestGId.setStatus("current")
_SleMplsTpTunnelCfgInfoDestCc_Type = MplsCcId
_SleMplsTpTunnelCfgInfoDestCc_Object = MibTableColumn
sleMplsTpTunnelCfgInfoDestCc = _SleMplsTpTunnelCfgInfoDestCc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 11),
    _SleMplsTpTunnelCfgInfoDestCc_Type()
)
sleMplsTpTunnelCfgInfoDestCc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoDestCc.setStatus("current")
_SleMplsTpTunnelCfgInfoDestIcc_Type = MplsIccId
_SleMplsTpTunnelCfgInfoDestIcc_Object = MibTableColumn
sleMplsTpTunnelCfgInfoDestIcc = _SleMplsTpTunnelCfgInfoDestIcc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 12),
    _SleMplsTpTunnelCfgInfoDestIcc_Type()
)
sleMplsTpTunnelCfgInfoDestIcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoDestIcc.setStatus("current")
_SleMplsTpTunnelCfgInfoDestNodeId_Type = IpAddress
_SleMplsTpTunnelCfgInfoDestNodeId_Object = MibTableColumn
sleMplsTpTunnelCfgInfoDestNodeId = _SleMplsTpTunnelCfgInfoDestNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 13),
    _SleMplsTpTunnelCfgInfoDestNodeId_Type()
)
sleMplsTpTunnelCfgInfoDestNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoDestNodeId.setStatus("current")


class _SleMplsTpTunnelCfgInfoMode_Type(Integer32):
    """Custom type sleMplsTpTunnelCfgInfoMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("unidirectional", 1),
          ("bidirectional", 2),
          ("corouted", 3),
          ("associate", 4))
    )


_SleMplsTpTunnelCfgInfoMode_Type.__name__ = "Integer32"
_SleMplsTpTunnelCfgInfoMode_Object = MibTableColumn
sleMplsTpTunnelCfgInfoMode = _SleMplsTpTunnelCfgInfoMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 14),
    _SleMplsTpTunnelCfgInfoMode_Type()
)
sleMplsTpTunnelCfgInfoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoMode.setStatus("current")


class _SleMplsTpTunnelCfgInfoFwdInLabel_Type(MplsLabel):
    """Custom type sleMplsTpTunnelCfgInfoFwdInLabel based on MplsLabel"""
    defaultValue = 1048576


_SleMplsTpTunnelCfgInfoFwdInLabel_Type.__name__ = "MplsLabel"
_SleMplsTpTunnelCfgInfoFwdInLabel_Object = MibTableColumn
sleMplsTpTunnelCfgInfoFwdInLabel = _SleMplsTpTunnelCfgInfoFwdInLabel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 15),
    _SleMplsTpTunnelCfgInfoFwdInLabel_Type()
)
sleMplsTpTunnelCfgInfoFwdInLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoFwdInLabel.setStatus("current")
_SleMplsTpTunnelCfgInfoFwdInIfIndex_Type = InterfaceIndexOrZero
_SleMplsTpTunnelCfgInfoFwdInIfIndex_Object = MibTableColumn
sleMplsTpTunnelCfgInfoFwdInIfIndex = _SleMplsTpTunnelCfgInfoFwdInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 16),
    _SleMplsTpTunnelCfgInfoFwdInIfIndex_Type()
)
sleMplsTpTunnelCfgInfoFwdInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoFwdInIfIndex.setStatus("current")


class _SleMplsTpTunnelCfgInfoFwdOperation_Type(Integer32):
    """Custom type sleMplsTpTunnelCfgInfoFwdOperation based on Integer32"""
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
          ("push", 1),
          ("pop", 2),
          ("swap", 3))
    )


_SleMplsTpTunnelCfgInfoFwdOperation_Type.__name__ = "Integer32"
_SleMplsTpTunnelCfgInfoFwdOperation_Object = MibTableColumn
sleMplsTpTunnelCfgInfoFwdOperation = _SleMplsTpTunnelCfgInfoFwdOperation_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 17),
    _SleMplsTpTunnelCfgInfoFwdOperation_Type()
)
sleMplsTpTunnelCfgInfoFwdOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoFwdOperation.setStatus("current")


class _SleMplsTpTunnelCfgInfoFwdOutLabel_Type(MplsLabel):
    """Custom type sleMplsTpTunnelCfgInfoFwdOutLabel based on MplsLabel"""
    defaultValue = 1048576


_SleMplsTpTunnelCfgInfoFwdOutLabel_Type.__name__ = "MplsLabel"
_SleMplsTpTunnelCfgInfoFwdOutLabel_Object = MibTableColumn
sleMplsTpTunnelCfgInfoFwdOutLabel = _SleMplsTpTunnelCfgInfoFwdOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 18),
    _SleMplsTpTunnelCfgInfoFwdOutLabel_Type()
)
sleMplsTpTunnelCfgInfoFwdOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoFwdOutLabel.setStatus("current")
_SleMplsTpTunnelCfgInfoFwdOutIfIndex_Type = InterfaceIndexOrZero
_SleMplsTpTunnelCfgInfoFwdOutIfIndex_Object = MibTableColumn
sleMplsTpTunnelCfgInfoFwdOutIfIndex = _SleMplsTpTunnelCfgInfoFwdOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 19),
    _SleMplsTpTunnelCfgInfoFwdOutIfIndex_Type()
)
sleMplsTpTunnelCfgInfoFwdOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoFwdOutIfIndex.setStatus("current")
_SleMplsTpTunnelCfgInfoFwdOutMac_Type = MacAddress
_SleMplsTpTunnelCfgInfoFwdOutMac_Object = MibTableColumn
sleMplsTpTunnelCfgInfoFwdOutMac = _SleMplsTpTunnelCfgInfoFwdOutMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 20),
    _SleMplsTpTunnelCfgInfoFwdOutMac_Type()
)
sleMplsTpTunnelCfgInfoFwdOutMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoFwdOutMac.setStatus("current")


class _SleMplsTpTunnelCfgInfoRevInLabel_Type(MplsLabel):
    """Custom type sleMplsTpTunnelCfgInfoRevInLabel based on MplsLabel"""
    defaultValue = 1048576


_SleMplsTpTunnelCfgInfoRevInLabel_Type.__name__ = "MplsLabel"
_SleMplsTpTunnelCfgInfoRevInLabel_Object = MibTableColumn
sleMplsTpTunnelCfgInfoRevInLabel = _SleMplsTpTunnelCfgInfoRevInLabel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 21),
    _SleMplsTpTunnelCfgInfoRevInLabel_Type()
)
sleMplsTpTunnelCfgInfoRevInLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoRevInLabel.setStatus("current")
_SleMplsTpTunnelCfgInfoRevInIfIndex_Type = InterfaceIndexOrZero
_SleMplsTpTunnelCfgInfoRevInIfIndex_Object = MibTableColumn
sleMplsTpTunnelCfgInfoRevInIfIndex = _SleMplsTpTunnelCfgInfoRevInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 22),
    _SleMplsTpTunnelCfgInfoRevInIfIndex_Type()
)
sleMplsTpTunnelCfgInfoRevInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoRevInIfIndex.setStatus("current")


class _SleMplsTpTunnelCfgInfoRevOperation_Type(Integer32):
    """Custom type sleMplsTpTunnelCfgInfoRevOperation based on Integer32"""
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
          ("push", 1),
          ("pop", 2),
          ("swap", 3))
    )


_SleMplsTpTunnelCfgInfoRevOperation_Type.__name__ = "Integer32"
_SleMplsTpTunnelCfgInfoRevOperation_Object = MibTableColumn
sleMplsTpTunnelCfgInfoRevOperation = _SleMplsTpTunnelCfgInfoRevOperation_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 23),
    _SleMplsTpTunnelCfgInfoRevOperation_Type()
)
sleMplsTpTunnelCfgInfoRevOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoRevOperation.setStatus("current")


class _SleMplsTpTunnelCfgInfoRevOutLabel_Type(MplsLabel):
    """Custom type sleMplsTpTunnelCfgInfoRevOutLabel based on MplsLabel"""
    defaultValue = 1048576


_SleMplsTpTunnelCfgInfoRevOutLabel_Type.__name__ = "MplsLabel"
_SleMplsTpTunnelCfgInfoRevOutLabel_Object = MibTableColumn
sleMplsTpTunnelCfgInfoRevOutLabel = _SleMplsTpTunnelCfgInfoRevOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 24),
    _SleMplsTpTunnelCfgInfoRevOutLabel_Type()
)
sleMplsTpTunnelCfgInfoRevOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoRevOutLabel.setStatus("current")
_SleMplsTpTunnelCfgInfoRevOutIfIndex_Type = InterfaceIndexOrZero
_SleMplsTpTunnelCfgInfoRevOutIfIndex_Object = MibTableColumn
sleMplsTpTunnelCfgInfoRevOutIfIndex = _SleMplsTpTunnelCfgInfoRevOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 25),
    _SleMplsTpTunnelCfgInfoRevOutIfIndex_Type()
)
sleMplsTpTunnelCfgInfoRevOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoRevOutIfIndex.setStatus("current")
_SleMplsTpTunnelCfgInfoRevOutMac_Type = MacAddress
_SleMplsTpTunnelCfgInfoRevOutMac_Object = MibTableColumn
sleMplsTpTunnelCfgInfoRevOutMac = _SleMplsTpTunnelCfgInfoRevOutMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 26),
    _SleMplsTpTunnelCfgInfoRevOutMac_Type()
)
sleMplsTpTunnelCfgInfoRevOutMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoRevOutMac.setStatus("current")


class _SleMplsTpTunnelCfgInfoState_Type(Integer32):
    """Custom type sleMplsTpTunnelCfgInfoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_SleMplsTpTunnelCfgInfoState_Type.__name__ = "Integer32"
_SleMplsTpTunnelCfgInfoState_Object = MibTableColumn
sleMplsTpTunnelCfgInfoState = _SleMplsTpTunnelCfgInfoState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 27),
    _SleMplsTpTunnelCfgInfoState_Type()
)
sleMplsTpTunnelCfgInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoState.setStatus("current")


class _SleMplsTpTunnelCfgInfoRole_Type(Integer32):
    """Custom type sleMplsTpTunnelCfgInfoRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("source", 0),
          ("transist", 1),
          ("destination", 2))
    )


_SleMplsTpTunnelCfgInfoRole_Type.__name__ = "Integer32"
_SleMplsTpTunnelCfgInfoRole_Object = MibTableColumn
sleMplsTpTunnelCfgInfoRole = _SleMplsTpTunnelCfgInfoRole_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 28),
    _SleMplsTpTunnelCfgInfoRole_Type()
)
sleMplsTpTunnelCfgInfoRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoRole.setStatus("current")
_SleMplsTpTunnelCfgInfoAssociateTnlName_Type = OctetString
_SleMplsTpTunnelCfgInfoAssociateTnlName_Object = MibTableColumn
sleMplsTpTunnelCfgInfoAssociateTnlName = _SleMplsTpTunnelCfgInfoAssociateTnlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 29),
    _SleMplsTpTunnelCfgInfoAssociateTnlName_Type()
)
sleMplsTpTunnelCfgInfoAssociateTnlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoAssociateTnlName.setStatus("current")
_SleMplsTpTunnelCfgInfoDescription_Type = OctetString
_SleMplsTpTunnelCfgInfoDescription_Object = MibTableColumn
sleMplsTpTunnelCfgInfoDescription = _SleMplsTpTunnelCfgInfoDescription_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 30),
    _SleMplsTpTunnelCfgInfoDescription_Type()
)
sleMplsTpTunnelCfgInfoDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoDescription.setStatus("current")


class _SleMplsTpTunnelCfgInfoHlspRole_Type(Integer32):
    """Custom type sleMplsTpTunnelCfgInfoHlspRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("server", 1),
          ("client", 2))
    )


_SleMplsTpTunnelCfgInfoHlspRole_Type.__name__ = "Integer32"
_SleMplsTpTunnelCfgInfoHlspRole_Object = MibTableColumn
sleMplsTpTunnelCfgInfoHlspRole = _SleMplsTpTunnelCfgInfoHlspRole_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 31),
    _SleMplsTpTunnelCfgInfoHlspRole_Type()
)
sleMplsTpTunnelCfgInfoHlspRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoHlspRole.setStatus("current")
_SleMplsTpTunnelCfgInfoHlspServerTunnelName_Type = OctetString
_SleMplsTpTunnelCfgInfoHlspServerTunnelName_Object = MibTableColumn
sleMplsTpTunnelCfgInfoHlspServerTunnelName = _SleMplsTpTunnelCfgInfoHlspServerTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 32),
    _SleMplsTpTunnelCfgInfoHlspServerTunnelName_Type()
)
sleMplsTpTunnelCfgInfoHlspServerTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoHlspServerTunnelName.setStatus("current")
_SleMplsTpTunnelCfgInfoQosPolicyName_Type = OctetString
_SleMplsTpTunnelCfgInfoQosPolicyName_Object = MibTableColumn
sleMplsTpTunnelCfgInfoQosPolicyName = _SleMplsTpTunnelCfgInfoQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 1, 1, 33),
    _SleMplsTpTunnelCfgInfoQosPolicyName_Type()
)
sleMplsTpTunnelCfgInfoQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgInfoQosPolicyName.setStatus("current")
_SleMplsTpTunnelCfgControl_ObjectIdentity = ObjectIdentity
sleMplsTpTunnelCfgControl = _SleMplsTpTunnelCfgControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2)
)


class _SleMplsTpTunnelCfgControlRequest_Type(Integer32):
    """Custom type sleMplsTpTunnelCfgControlRequest based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("createMplsTpTunnelEntry", 1),
          ("deleteMplsTpTunnelEntry", 2),
          ("setMplsTpTunnelMode", 3),
          ("setNhlfe", 4),
          ("setIlmPop", 5),
          ("setIlmSwap", 6),
          ("setAssociateTunnel", 7),
          ("unsetNhlfe", 8),
          ("unsetIlmPop", 9),
          ("unsetIlmSwap", 10),
          ("unsetAssociateTunnel", 11),
          ("setDescription", 12),
          ("setHlspServerLsp", 13),
          ("setHlspClientLsp", 14),
          ("unsetHlspServerLsp", 15),
          ("unsetHlspClientLsp", 16),
          ("setTunnelQosPolicyName", 17),
          ("unsetTunnelQosPolicyName", 18))
    )


_SleMplsTpTunnelCfgControlRequest_Type.__name__ = "Integer32"
_SleMplsTpTunnelCfgControlRequest_Object = MibScalar
sleMplsTpTunnelCfgControlRequest = _SleMplsTpTunnelCfgControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 1),
    _SleMplsTpTunnelCfgControlRequest_Type()
)
sleMplsTpTunnelCfgControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlRequest.setStatus("current")
_SleMplsTpTunnelCfgControlStatus_Type = SleControlStatusType
_SleMplsTpTunnelCfgControlStatus_Object = MibScalar
sleMplsTpTunnelCfgControlStatus = _SleMplsTpTunnelCfgControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 2),
    _SleMplsTpTunnelCfgControlStatus_Type()
)
sleMplsTpTunnelCfgControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlStatus.setStatus("current")
_SleMplsTpTunnelCfgControlTimer_Type = Gauge32
_SleMplsTpTunnelCfgControlTimer_Object = MibScalar
sleMplsTpTunnelCfgControlTimer = _SleMplsTpTunnelCfgControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 3),
    _SleMplsTpTunnelCfgControlTimer_Type()
)
sleMplsTpTunnelCfgControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlTimer.setStatus("current")
_SleMplsTpTunnelCfgControlTimeStamp_Type = TimeTicks
_SleMplsTpTunnelCfgControlTimeStamp_Object = MibScalar
sleMplsTpTunnelCfgControlTimeStamp = _SleMplsTpTunnelCfgControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 4),
    _SleMplsTpTunnelCfgControlTimeStamp_Type()
)
sleMplsTpTunnelCfgControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlTimeStamp.setStatus("current")
_SleMplsTpTunnelCfgControlReqResult_Type = SleControlRequestResultType
_SleMplsTpTunnelCfgControlReqResult_Object = MibScalar
sleMplsTpTunnelCfgControlReqResult = _SleMplsTpTunnelCfgControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 5),
    _SleMplsTpTunnelCfgControlReqResult_Type()
)
sleMplsTpTunnelCfgControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlReqResult.setStatus("current")


class _SleMplsTpTunnelCfgControlName_Type(OctetString):
    """Custom type sleMplsTpTunnelCfgControlName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SleMplsTpTunnelCfgControlName_Type.__name__ = "OctetString"
_SleMplsTpTunnelCfgControlName_Object = MibScalar
sleMplsTpTunnelCfgControlName = _SleMplsTpTunnelCfgControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 6),
    _SleMplsTpTunnelCfgControlName_Type()
)
sleMplsTpTunnelCfgControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlName.setStatus("current")


class _SleMplsTpTunnelCfgControlId_Type(Unsigned32):
    """Custom type sleMplsTpTunnelCfgControlId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleMplsTpTunnelCfgControlId_Type.__name__ = "Unsigned32"
_SleMplsTpTunnelCfgControlId_Object = MibScalar
sleMplsTpTunnelCfgControlId = _SleMplsTpTunnelCfgControlId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 7),
    _SleMplsTpTunnelCfgControlId_Type()
)
sleMplsTpTunnelCfgControlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlId.setStatus("current")


class _SleMplsTpTunnelCfgControlSrcIdType_Type(Integer32):
    """Custom type sleMplsTpTunnelCfgControlSrcIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ietf", 1),
          ("itut", 2))
    )


_SleMplsTpTunnelCfgControlSrcIdType_Type.__name__ = "Integer32"
_SleMplsTpTunnelCfgControlSrcIdType_Object = MibScalar
sleMplsTpTunnelCfgControlSrcIdType = _SleMplsTpTunnelCfgControlSrcIdType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 8),
    _SleMplsTpTunnelCfgControlSrcIdType_Type()
)
sleMplsTpTunnelCfgControlSrcIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlSrcIdType.setStatus("current")


class _SleMplsTpTunnelCfgControlSrcGId_Type(Unsigned32):
    """Custom type sleMplsTpTunnelCfgControlSrcGId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SleMplsTpTunnelCfgControlSrcGId_Type.__name__ = "Unsigned32"
_SleMplsTpTunnelCfgControlSrcGId_Object = MibScalar
sleMplsTpTunnelCfgControlSrcGId = _SleMplsTpTunnelCfgControlSrcGId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 9),
    _SleMplsTpTunnelCfgControlSrcGId_Type()
)
sleMplsTpTunnelCfgControlSrcGId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlSrcGId.setStatus("current")
_SleMplsTpTunnelCfgControlSrcCc_Type = MplsCcId
_SleMplsTpTunnelCfgControlSrcCc_Object = MibScalar
sleMplsTpTunnelCfgControlSrcCc = _SleMplsTpTunnelCfgControlSrcCc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 10),
    _SleMplsTpTunnelCfgControlSrcCc_Type()
)
sleMplsTpTunnelCfgControlSrcCc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlSrcCc.setStatus("current")
_SleMplsTpTunnelCfgControlSrcIcc_Type = MplsIccId
_SleMplsTpTunnelCfgControlSrcIcc_Object = MibScalar
sleMplsTpTunnelCfgControlSrcIcc = _SleMplsTpTunnelCfgControlSrcIcc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 11),
    _SleMplsTpTunnelCfgControlSrcIcc_Type()
)
sleMplsTpTunnelCfgControlSrcIcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlSrcIcc.setStatus("current")
_SleMplsTpTunnelCfgControlSrcNodeId_Type = IpAddress
_SleMplsTpTunnelCfgControlSrcNodeId_Object = MibScalar
sleMplsTpTunnelCfgControlSrcNodeId = _SleMplsTpTunnelCfgControlSrcNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 12),
    _SleMplsTpTunnelCfgControlSrcNodeId_Type()
)
sleMplsTpTunnelCfgControlSrcNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlSrcNodeId.setStatus("current")


class _SleMplsTpTunnelCfgControlDestIdType_Type(Integer32):
    """Custom type sleMplsTpTunnelCfgControlDestIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ietf", 1),
          ("itut", 2))
    )


_SleMplsTpTunnelCfgControlDestIdType_Type.__name__ = "Integer32"
_SleMplsTpTunnelCfgControlDestIdType_Object = MibScalar
sleMplsTpTunnelCfgControlDestIdType = _SleMplsTpTunnelCfgControlDestIdType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 13),
    _SleMplsTpTunnelCfgControlDestIdType_Type()
)
sleMplsTpTunnelCfgControlDestIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlDestIdType.setStatus("current")


class _SleMplsTpTunnelCfgControlDestGId_Type(Unsigned32):
    """Custom type sleMplsTpTunnelCfgControlDestGId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SleMplsTpTunnelCfgControlDestGId_Type.__name__ = "Unsigned32"
_SleMplsTpTunnelCfgControlDestGId_Object = MibScalar
sleMplsTpTunnelCfgControlDestGId = _SleMplsTpTunnelCfgControlDestGId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 14),
    _SleMplsTpTunnelCfgControlDestGId_Type()
)
sleMplsTpTunnelCfgControlDestGId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlDestGId.setStatus("current")
_SleMplsTpTunnelCfgControlDestCc_Type = MplsCcId
_SleMplsTpTunnelCfgControlDestCc_Object = MibScalar
sleMplsTpTunnelCfgControlDestCc = _SleMplsTpTunnelCfgControlDestCc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 15),
    _SleMplsTpTunnelCfgControlDestCc_Type()
)
sleMplsTpTunnelCfgControlDestCc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlDestCc.setStatus("current")
_SleMplsTpTunnelCfgControlDestIcc_Type = MplsIccId
_SleMplsTpTunnelCfgControlDestIcc_Object = MibScalar
sleMplsTpTunnelCfgControlDestIcc = _SleMplsTpTunnelCfgControlDestIcc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 16),
    _SleMplsTpTunnelCfgControlDestIcc_Type()
)
sleMplsTpTunnelCfgControlDestIcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlDestIcc.setStatus("current")
_SleMplsTpTunnelCfgControlDestNodeId_Type = IpAddress
_SleMplsTpTunnelCfgControlDestNodeId_Object = MibScalar
sleMplsTpTunnelCfgControlDestNodeId = _SleMplsTpTunnelCfgControlDestNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 17),
    _SleMplsTpTunnelCfgControlDestNodeId_Type()
)
sleMplsTpTunnelCfgControlDestNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlDestNodeId.setStatus("current")


class _SleMplsTpTunnelCfgControlMode_Type(Integer32):
    """Custom type sleMplsTpTunnelCfgControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unidirectional", 1),
          ("bidirectional", 2))
    )


_SleMplsTpTunnelCfgControlMode_Type.__name__ = "Integer32"
_SleMplsTpTunnelCfgControlMode_Object = MibScalar
sleMplsTpTunnelCfgControlMode = _SleMplsTpTunnelCfgControlMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 18),
    _SleMplsTpTunnelCfgControlMode_Type()
)
sleMplsTpTunnelCfgControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlMode.setStatus("current")


class _SleMplsTpTunnelCfgControlPath_Type(Integer32):
    """Custom type sleMplsTpTunnelCfgControlPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwardPath", 1),
          ("reversePath", 2))
    )


_SleMplsTpTunnelCfgControlPath_Type.__name__ = "Integer32"
_SleMplsTpTunnelCfgControlPath_Object = MibScalar
sleMplsTpTunnelCfgControlPath = _SleMplsTpTunnelCfgControlPath_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 19),
    _SleMplsTpTunnelCfgControlPath_Type()
)
sleMplsTpTunnelCfgControlPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlPath.setStatus("current")
_SleMplsTpTunnelCfgControlInLabel_Type = MplsLabel
_SleMplsTpTunnelCfgControlInLabel_Object = MibScalar
sleMplsTpTunnelCfgControlInLabel = _SleMplsTpTunnelCfgControlInLabel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 20),
    _SleMplsTpTunnelCfgControlInLabel_Type()
)
sleMplsTpTunnelCfgControlInLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlInLabel.setStatus("current")
_SleMplsTpTunnelCfgControlInInterface_Type = InterfaceIndexOrZero
_SleMplsTpTunnelCfgControlInInterface_Object = MibScalar
sleMplsTpTunnelCfgControlInInterface = _SleMplsTpTunnelCfgControlInInterface_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 21),
    _SleMplsTpTunnelCfgControlInInterface_Type()
)
sleMplsTpTunnelCfgControlInInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlInInterface.setStatus("current")


class _SleMplsTpTunnelCfgControlOperation_Type(Integer32):
    """Custom type sleMplsTpTunnelCfgControlOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("push", 1),
          ("pop", 2),
          ("swap", 3))
    )


_SleMplsTpTunnelCfgControlOperation_Type.__name__ = "Integer32"
_SleMplsTpTunnelCfgControlOperation_Object = MibScalar
sleMplsTpTunnelCfgControlOperation = _SleMplsTpTunnelCfgControlOperation_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 22),
    _SleMplsTpTunnelCfgControlOperation_Type()
)
sleMplsTpTunnelCfgControlOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlOperation.setStatus("current")
_SleMplsTpTunnelCfgControlOutLabel_Type = MplsLabel
_SleMplsTpTunnelCfgControlOutLabel_Object = MibScalar
sleMplsTpTunnelCfgControlOutLabel = _SleMplsTpTunnelCfgControlOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 23),
    _SleMplsTpTunnelCfgControlOutLabel_Type()
)
sleMplsTpTunnelCfgControlOutLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlOutLabel.setStatus("current")
_SleMplsTpTunnelCfgControlOutInterface_Type = InterfaceIndexOrZero
_SleMplsTpTunnelCfgControlOutInterface_Object = MibScalar
sleMplsTpTunnelCfgControlOutInterface = _SleMplsTpTunnelCfgControlOutInterface_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 24),
    _SleMplsTpTunnelCfgControlOutInterface_Type()
)
sleMplsTpTunnelCfgControlOutInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlOutInterface.setStatus("current")
_SleMplsTpTunnelCfgControlOutMacAddress_Type = MacAddress
_SleMplsTpTunnelCfgControlOutMacAddress_Object = MibScalar
sleMplsTpTunnelCfgControlOutMacAddress = _SleMplsTpTunnelCfgControlOutMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 25),
    _SleMplsTpTunnelCfgControlOutMacAddress_Type()
)
sleMplsTpTunnelCfgControlOutMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlOutMacAddress.setStatus("current")
_SleMplsTpTunnelCfgControlAssociateTnlName_Type = OctetString
_SleMplsTpTunnelCfgControlAssociateTnlName_Object = MibScalar
sleMplsTpTunnelCfgControlAssociateTnlName = _SleMplsTpTunnelCfgControlAssociateTnlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 26),
    _SleMplsTpTunnelCfgControlAssociateTnlName_Type()
)
sleMplsTpTunnelCfgControlAssociateTnlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlAssociateTnlName.setStatus("current")
_SleMplsTpTunnelCfgControlDescription_Type = OctetString
_SleMplsTpTunnelCfgControlDescription_Object = MibScalar
sleMplsTpTunnelCfgControlDescription = _SleMplsTpTunnelCfgControlDescription_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 27),
    _SleMplsTpTunnelCfgControlDescription_Type()
)
sleMplsTpTunnelCfgControlDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlDescription.setStatus("current")
_SleMplsTpTunnelCfgControlHlspSeverTunnelName_Type = OctetString
_SleMplsTpTunnelCfgControlHlspSeverTunnelName_Object = MibScalar
sleMplsTpTunnelCfgControlHlspSeverTunnelName = _SleMplsTpTunnelCfgControlHlspSeverTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 28),
    _SleMplsTpTunnelCfgControlHlspSeverTunnelName_Type()
)
sleMplsTpTunnelCfgControlHlspSeverTunnelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlHlspSeverTunnelName.setStatus("current")
_SleMplsTpTunnelCfgControlQosPolicyName_Type = OctetString
_SleMplsTpTunnelCfgControlQosPolicyName_Object = MibScalar
sleMplsTpTunnelCfgControlQosPolicyName = _SleMplsTpTunnelCfgControlQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 14, 1, 2, 29),
    _SleMplsTpTunnelCfgControlQosPolicyName_Type()
)
sleMplsTpTunnelCfgControlQosPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpTunnelCfgControlQosPolicyName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-MPLS-TP-TUNNEL-MIB",
    **{"sleMpls": sleMpls,
       "sleMplsTpTunnel": sleMplsTpTunnel,
       "sleMplsTpTunnelCfg": sleMplsTpTunnelCfg,
       "sleMplsTpTunnelCfgInfoTable": sleMplsTpTunnelCfgInfoTable,
       "sleMplsTpTunnelCfgInfoEntry": sleMplsTpTunnelCfgInfoEntry,
       "sleMplsTpTunnelCfgInfoIndex": sleMplsTpTunnelCfgInfoIndex,
       "sleMplsTpTunnelCfgInfoName": sleMplsTpTunnelCfgInfoName,
       "sleMplsTpTunnelCfgInfoId": sleMplsTpTunnelCfgInfoId,
       "sleMplsTpTunnelCfgInfoSrcIdType": sleMplsTpTunnelCfgInfoSrcIdType,
       "sleMplsTpTunnelCfgInfoSrcGId": sleMplsTpTunnelCfgInfoSrcGId,
       "sleMplsTpTunnelCfgInfoSrcCc": sleMplsTpTunnelCfgInfoSrcCc,
       "sleMplsTpTunnelCfgInfoSrcIcc": sleMplsTpTunnelCfgInfoSrcIcc,
       "sleMplsTpTunnelCfgInfoSrcNodeId": sleMplsTpTunnelCfgInfoSrcNodeId,
       "sleMplsTpTunnelCfgInfoDestIdType": sleMplsTpTunnelCfgInfoDestIdType,
       "sleMplsTpTunnelCfgInfoDestGId": sleMplsTpTunnelCfgInfoDestGId,
       "sleMplsTpTunnelCfgInfoDestCc": sleMplsTpTunnelCfgInfoDestCc,
       "sleMplsTpTunnelCfgInfoDestIcc": sleMplsTpTunnelCfgInfoDestIcc,
       "sleMplsTpTunnelCfgInfoDestNodeId": sleMplsTpTunnelCfgInfoDestNodeId,
       "sleMplsTpTunnelCfgInfoMode": sleMplsTpTunnelCfgInfoMode,
       "sleMplsTpTunnelCfgInfoFwdInLabel": sleMplsTpTunnelCfgInfoFwdInLabel,
       "sleMplsTpTunnelCfgInfoFwdInIfIndex": sleMplsTpTunnelCfgInfoFwdInIfIndex,
       "sleMplsTpTunnelCfgInfoFwdOperation": sleMplsTpTunnelCfgInfoFwdOperation,
       "sleMplsTpTunnelCfgInfoFwdOutLabel": sleMplsTpTunnelCfgInfoFwdOutLabel,
       "sleMplsTpTunnelCfgInfoFwdOutIfIndex": sleMplsTpTunnelCfgInfoFwdOutIfIndex,
       "sleMplsTpTunnelCfgInfoFwdOutMac": sleMplsTpTunnelCfgInfoFwdOutMac,
       "sleMplsTpTunnelCfgInfoRevInLabel": sleMplsTpTunnelCfgInfoRevInLabel,
       "sleMplsTpTunnelCfgInfoRevInIfIndex": sleMplsTpTunnelCfgInfoRevInIfIndex,
       "sleMplsTpTunnelCfgInfoRevOperation": sleMplsTpTunnelCfgInfoRevOperation,
       "sleMplsTpTunnelCfgInfoRevOutLabel": sleMplsTpTunnelCfgInfoRevOutLabel,
       "sleMplsTpTunnelCfgInfoRevOutIfIndex": sleMplsTpTunnelCfgInfoRevOutIfIndex,
       "sleMplsTpTunnelCfgInfoRevOutMac": sleMplsTpTunnelCfgInfoRevOutMac,
       "sleMplsTpTunnelCfgInfoState": sleMplsTpTunnelCfgInfoState,
       "sleMplsTpTunnelCfgInfoRole": sleMplsTpTunnelCfgInfoRole,
       "sleMplsTpTunnelCfgInfoAssociateTnlName": sleMplsTpTunnelCfgInfoAssociateTnlName,
       "sleMplsTpTunnelCfgInfoDescription": sleMplsTpTunnelCfgInfoDescription,
       "sleMplsTpTunnelCfgInfoHlspRole": sleMplsTpTunnelCfgInfoHlspRole,
       "sleMplsTpTunnelCfgInfoHlspServerTunnelName": sleMplsTpTunnelCfgInfoHlspServerTunnelName,
       "sleMplsTpTunnelCfgInfoQosPolicyName": sleMplsTpTunnelCfgInfoQosPolicyName,
       "sleMplsTpTunnelCfgControl": sleMplsTpTunnelCfgControl,
       "sleMplsTpTunnelCfgControlRequest": sleMplsTpTunnelCfgControlRequest,
       "sleMplsTpTunnelCfgControlStatus": sleMplsTpTunnelCfgControlStatus,
       "sleMplsTpTunnelCfgControlTimer": sleMplsTpTunnelCfgControlTimer,
       "sleMplsTpTunnelCfgControlTimeStamp": sleMplsTpTunnelCfgControlTimeStamp,
       "sleMplsTpTunnelCfgControlReqResult": sleMplsTpTunnelCfgControlReqResult,
       "sleMplsTpTunnelCfgControlName": sleMplsTpTunnelCfgControlName,
       "sleMplsTpTunnelCfgControlId": sleMplsTpTunnelCfgControlId,
       "sleMplsTpTunnelCfgControlSrcIdType": sleMplsTpTunnelCfgControlSrcIdType,
       "sleMplsTpTunnelCfgControlSrcGId": sleMplsTpTunnelCfgControlSrcGId,
       "sleMplsTpTunnelCfgControlSrcCc": sleMplsTpTunnelCfgControlSrcCc,
       "sleMplsTpTunnelCfgControlSrcIcc": sleMplsTpTunnelCfgControlSrcIcc,
       "sleMplsTpTunnelCfgControlSrcNodeId": sleMplsTpTunnelCfgControlSrcNodeId,
       "sleMplsTpTunnelCfgControlDestIdType": sleMplsTpTunnelCfgControlDestIdType,
       "sleMplsTpTunnelCfgControlDestGId": sleMplsTpTunnelCfgControlDestGId,
       "sleMplsTpTunnelCfgControlDestCc": sleMplsTpTunnelCfgControlDestCc,
       "sleMplsTpTunnelCfgControlDestIcc": sleMplsTpTunnelCfgControlDestIcc,
       "sleMplsTpTunnelCfgControlDestNodeId": sleMplsTpTunnelCfgControlDestNodeId,
       "sleMplsTpTunnelCfgControlMode": sleMplsTpTunnelCfgControlMode,
       "sleMplsTpTunnelCfgControlPath": sleMplsTpTunnelCfgControlPath,
       "sleMplsTpTunnelCfgControlInLabel": sleMplsTpTunnelCfgControlInLabel,
       "sleMplsTpTunnelCfgControlInInterface": sleMplsTpTunnelCfgControlInInterface,
       "sleMplsTpTunnelCfgControlOperation": sleMplsTpTunnelCfgControlOperation,
       "sleMplsTpTunnelCfgControlOutLabel": sleMplsTpTunnelCfgControlOutLabel,
       "sleMplsTpTunnelCfgControlOutInterface": sleMplsTpTunnelCfgControlOutInterface,
       "sleMplsTpTunnelCfgControlOutMacAddress": sleMplsTpTunnelCfgControlOutMacAddress,
       "sleMplsTpTunnelCfgControlAssociateTnlName": sleMplsTpTunnelCfgControlAssociateTnlName,
       "sleMplsTpTunnelCfgControlDescription": sleMplsTpTunnelCfgControlDescription,
       "sleMplsTpTunnelCfgControlHlspSeverTunnelName": sleMplsTpTunnelCfgControlHlspSeverTunnelName,
       "sleMplsTpTunnelCfgControlQosPolicyName": sleMplsTpTunnelCfgControlQosPolicyName}
)
