# SNMP MIB module (IPE-PW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nec/IPE-PW-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:53:51 2025
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
 Opaque,
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
    "Opaque",
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


# Types definitions


# TEXTUAL-CONVENTIONS



class IpeEnableDisableValue(TextualConvention, Integer32):
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
        *(("invalid", 0),
          ("disabled", 1),
          ("enabled", 2))
    )



class IpePwIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )



class IpeVlanIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



# MIB Managed Objects in the order of their OIDs

_Nec_ObjectIdentity = ObjectIdentity
nec = _Nec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119)
)
_Nec_mib_ObjectIdentity = ObjectIdentity
nec_mib = _Nec_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2)
)
_NecProductDepend_ObjectIdentity = ObjectIdentity
necProductDepend = _NecProductDepend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3)
)
_RadioEquipment_ObjectIdentity = ObjectIdentity
radioEquipment = _RadioEquipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69)
)
_PasoNeoIpe_common_ObjectIdentity = ObjectIdentity
pasoNeoIpe_common = _PasoNeoIpe_common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501)
)
_ProvisioningGroup_ObjectIdentity = ObjectIdentity
provisioningGroup = _ProvisioningGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5)
)
_ProvPwGroup_ObjectIdentity = ObjectIdentity
provPwGroup = _ProvPwGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42)
)
_ProvPwTdmLineTable_Object = MibTable
provPwTdmLineTable = _ProvPwTdmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 4)
)
if mibBuilder.loadTexts:
    provPwTdmLineTable.setStatus("current")
_ProvPwTdmLineEntry_Object = MibTableRow
provPwTdmLineEntry = _ProvPwTdmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 4, 1)
)
provPwTdmLineEntry.setIndexNames(
    (0, "IPE-PW-MIB", "provPwTdmLineIfIndex"),
)
if mibBuilder.loadTexts:
    provPwTdmLineEntry.setStatus("current")
_ProvPwTdmLineIfIndex_Type = InterfaceIndex
_ProvPwTdmLineIfIndex_Object = MibTableColumn
provPwTdmLineIfIndex = _ProvPwTdmLineIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 4, 1, 1),
    _ProvPwTdmLineIfIndex_Type()
)
provPwTdmLineIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provPwTdmLineIfIndex.setStatus("current")
_ProvPwTdmLineNEAddress_Type = IpAddress
_ProvPwTdmLineNEAddress_Object = MibTableColumn
provPwTdmLineNEAddress = _ProvPwTdmLineNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 4, 1, 2),
    _ProvPwTdmLineNEAddress_Type()
)
provPwTdmLineNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provPwTdmLineNEAddress.setStatus("current")


class _ProvPwTdmLineFrameMode_Type(Integer32):
    """Custom type provPwTdmLineFrameMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("unframed", 1))
    )


_ProvPwTdmLineFrameMode_Type.__name__ = "Integer32"
_ProvPwTdmLineFrameMode_Object = MibTableColumn
provPwTdmLineFrameMode = _ProvPwTdmLineFrameMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 4, 1, 3),
    _ProvPwTdmLineFrameMode_Type()
)
provPwTdmLineFrameMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provPwTdmLineFrameMode.setStatus("current")


class _ProvPwTdmLineCasMode_Type(IpeEnableDisableValue):
    """Custom type provPwTdmLineCasMode based on IpeEnableDisableValue"""
    defaultValue = 1


_ProvPwTdmLineCasMode_Type.__name__ = "IpeEnableDisableValue"
_ProvPwTdmLineCasMode_Object = MibTableColumn
provPwTdmLineCasMode = _ProvPwTdmLineCasMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 4, 1, 4),
    _ProvPwTdmLineCasMode_Type()
)
provPwTdmLineCasMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provPwTdmLineCasMode.setStatus("current")


class _ProvPwTdmLineCrc4Mode_Type(IpeEnableDisableValue):
    """Custom type provPwTdmLineCrc4Mode based on IpeEnableDisableValue"""
    defaultValue = 1


_ProvPwTdmLineCrc4Mode_Type.__name__ = "IpeEnableDisableValue"
_ProvPwTdmLineCrc4Mode_Object = MibTableColumn
provPwTdmLineCrc4Mode = _ProvPwTdmLineCrc4Mode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 4, 1, 5),
    _ProvPwTdmLineCrc4Mode_Type()
)
provPwTdmLineCrc4Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provPwTdmLineCrc4Mode.setStatus("current")


class _ProvPwTdmLineJtrBfrDepth_Type(Integer32):
    """Custom type provPwTdmLineJtrBfrDepth based on Integer32"""
    defaultValue = 3

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
              7)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("jtr2ms", 1),
          ("jtr4ms", 2),
          ("jtr8ms", 3),
          ("jtr16ms", 4),
          ("jtr32ms", 5),
          ("jtr64ms", 6),
          ("jtr128ms", 7))
    )


_ProvPwTdmLineJtrBfrDepth_Type.__name__ = "Integer32"
_ProvPwTdmLineJtrBfrDepth_Object = MibTableColumn
provPwTdmLineJtrBfrDepth = _ProvPwTdmLineJtrBfrDepth_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 4, 1, 6),
    _ProvPwTdmLineJtrBfrDepth_Type()
)
provPwTdmLineJtrBfrDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provPwTdmLineJtrBfrDepth.setStatus("current")


class _ProvPwTdmLineDstMacCheck_Type(IpeEnableDisableValue):
    """Custom type provPwTdmLineDstMacCheck based on IpeEnableDisableValue"""
    defaultValue = 2


_ProvPwTdmLineDstMacCheck_Type.__name__ = "IpeEnableDisableValue"
_ProvPwTdmLineDstMacCheck_Object = MibTableColumn
provPwTdmLineDstMacCheck = _ProvPwTdmLineDstMacCheck_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 4, 1, 7),
    _ProvPwTdmLineDstMacCheck_Type()
)
provPwTdmLineDstMacCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provPwTdmLineDstMacCheck.setStatus("current")
_ProvPwTdmTable_Object = MibTable
provPwTdmTable = _ProvPwTdmTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 5)
)
if mibBuilder.loadTexts:
    provPwTdmTable.setStatus("current")
_ProvPwTdmEntry_Object = MibTableRow
provPwTdmEntry = _ProvPwTdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 5, 1)
)
provPwTdmEntry.setIndexNames(
    (0, "IPE-PW-MIB", "provPwTdmPwIndex"),
)
if mibBuilder.loadTexts:
    provPwTdmEntry.setStatus("current")
_ProvPwTdmPwIndex_Type = IpePwIndex
_ProvPwTdmPwIndex_Object = MibTableColumn
provPwTdmPwIndex = _ProvPwTdmPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 5, 1, 1),
    _ProvPwTdmPwIndex_Type()
)
provPwTdmPwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provPwTdmPwIndex.setStatus("current")
_ProvPwTdmNEAddress_Type = IpAddress
_ProvPwTdmNEAddress_Object = MibTableColumn
provPwTdmNEAddress = _ProvPwTdmNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 5, 1, 2),
    _ProvPwTdmNEAddress_Type()
)
provPwTdmNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provPwTdmNEAddress.setStatus("current")
_ProvPwTdmIfIndex_Type = InterfaceIndex
_ProvPwTdmIfIndex_Object = MibTableColumn
provPwTdmIfIndex = _ProvPwTdmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 5, 1, 3),
    _ProvPwTdmIfIndex_Type()
)
provPwTdmIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provPwTdmIfIndex.setStatus("current")


class _ProvPwTdmRtpHdrUsed_Type(IpeEnableDisableValue):
    """Custom type provPwTdmRtpHdrUsed based on IpeEnableDisableValue"""
    defaultValue = 1


_ProvPwTdmRtpHdrUsed_Type.__name__ = "IpeEnableDisableValue"
_ProvPwTdmRtpHdrUsed_Object = MibTableColumn
provPwTdmRtpHdrUsed = _ProvPwTdmRtpHdrUsed_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 5, 1, 4),
    _ProvPwTdmRtpHdrUsed_Type()
)
provPwTdmRtpHdrUsed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provPwTdmRtpHdrUsed.setStatus("current")


class _ProvPwTdmFrameLength_Type(Integer32):
    """Custom type provPwTdmFrameLength based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ProvPwTdmFrameLength_Type.__name__ = "Integer32"
_ProvPwTdmFrameLength_Object = MibTableColumn
provPwTdmFrameLength = _ProvPwTdmFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 5, 1, 5),
    _ProvPwTdmFrameLength_Type()
)
provPwTdmFrameLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provPwTdmFrameLength.setStatus("current")


class _ProvPwTdmEncapMode_Type(Integer32):
    """Custom type provPwTdmEncapMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("tdmOverEther", 1))
    )


_ProvPwTdmEncapMode_Type.__name__ = "Integer32"
_ProvPwTdmEncapMode_Object = MibTableColumn
provPwTdmEncapMode = _ProvPwTdmEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 5, 1, 6),
    _ProvPwTdmEncapMode_Type()
)
provPwTdmEncapMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provPwTdmEncapMode.setStatus("current")
_ProvPwTdmRowStatus_Type = RowStatus
_ProvPwTdmRowStatus_Object = MibTableColumn
provPwTdmRowStatus = _ProvPwTdmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 5, 1, 7),
    _ProvPwTdmRowStatus_Type()
)
provPwTdmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provPwTdmRowStatus.setStatus("current")


class _ProvPwTdmAdaptiveClkSource_Type(IpeEnableDisableValue):
    """Custom type provPwTdmAdaptiveClkSource based on IpeEnableDisableValue"""
    defaultValue = 1


_ProvPwTdmAdaptiveClkSource_Type.__name__ = "IpeEnableDisableValue"
_ProvPwTdmAdaptiveClkSource_Object = MibTableColumn
provPwTdmAdaptiveClkSource = _ProvPwTdmAdaptiveClkSource_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 5, 1, 8),
    _ProvPwTdmAdaptiveClkSource_Type()
)
provPwTdmAdaptiveClkSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provPwTdmAdaptiveClkSource.setStatus("current")
_ProvPwOverEthTable_Object = MibTable
provPwOverEthTable = _ProvPwOverEthTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 11)
)
if mibBuilder.loadTexts:
    provPwOverEthTable.setStatus("current")
_ProvPwOverEthEntry_Object = MibTableRow
provPwOverEthEntry = _ProvPwOverEthEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 11, 1)
)
provPwOverEthEntry.setIndexNames(
    (0, "IPE-PW-MIB", "provPwOverEthPwIndex"),
)
if mibBuilder.loadTexts:
    provPwOverEthEntry.setStatus("current")
_ProvPwOverEthPwIndex_Type = IpePwIndex
_ProvPwOverEthPwIndex_Object = MibTableColumn
provPwOverEthPwIndex = _ProvPwOverEthPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 11, 1, 1),
    _ProvPwOverEthPwIndex_Type()
)
provPwOverEthPwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provPwOverEthPwIndex.setStatus("current")
_ProvPwOverEthNEAddress_Type = IpAddress
_ProvPwOverEthNEAddress_Object = MibTableColumn
provPwOverEthNEAddress = _ProvPwOverEthNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 11, 1, 2),
    _ProvPwOverEthNEAddress_Type()
)
provPwOverEthNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provPwOverEthNEAddress.setStatus("current")
_ProvPwOverEthVlanId_Type = IpeVlanIndex
_ProvPwOverEthVlanId_Object = MibTableColumn
provPwOverEthVlanId = _ProvPwOverEthVlanId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 11, 1, 3),
    _ProvPwOverEthVlanId_Type()
)
provPwOverEthVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provPwOverEthVlanId.setStatus("current")


class _ProvPwOverEthTpid_Type(OctetString):
    """Custom type provPwOverEthTpid based on OctetString"""
    defaultHexValue = "ff00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_ProvPwOverEthTpid_Type.__name__ = "OctetString"
_ProvPwOverEthTpid_Object = MibTableColumn
provPwOverEthTpid = _ProvPwOverEthTpid_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 11, 1, 4),
    _ProvPwOverEthTpid_Type()
)
provPwOverEthTpid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provPwOverEthTpid.setStatus("obsolete")


class _ProvPwOverEthCosValue_Type(Integer32):
    """Custom type provPwOverEthCosValue based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ProvPwOverEthCosValue_Type.__name__ = "Integer32"
_ProvPwOverEthCosValue_Object = MibTableColumn
provPwOverEthCosValue = _ProvPwOverEthCosValue_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 11, 1, 5),
    _ProvPwOverEthCosValue_Type()
)
provPwOverEthCosValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provPwOverEthCosValue.setStatus("current")


class _ProvPwOverEthEcid_Type(Integer32):
    """Custom type provPwOverEthEcid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048575),
    )


_ProvPwOverEthEcid_Type.__name__ = "Integer32"
_ProvPwOverEthEcid_Object = MibTableColumn
provPwOverEthEcid = _ProvPwOverEthEcid_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 11, 1, 6),
    _ProvPwOverEthEcid_Type()
)
provPwOverEthEcid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provPwOverEthEcid.setStatus("current")


class _ProvPwOverEthName_Type(DisplayString):
    """Custom type provPwOverEthName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProvPwOverEthName_Type.__name__ = "DisplayString"
_ProvPwOverEthName_Object = MibTableColumn
provPwOverEthName = _ProvPwOverEthName_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 11, 1, 7),
    _ProvPwOverEthName_Type()
)
provPwOverEthName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provPwOverEthName.setStatus("current")
_ProvPwOverEthDstMacAddress_Type = MacAddress
_ProvPwOverEthDstMacAddress_Object = MibTableColumn
provPwOverEthDstMacAddress = _ProvPwOverEthDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 42, 11, 1, 8),
    _ProvPwOverEthDstMacAddress_Type()
)
provPwOverEthDstMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provPwOverEthDstMacAddress.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPE-PW-MIB",
    **{"IpeEnableDisableValue": IpeEnableDisableValue,
       "IpePwIndex": IpePwIndex,
       "IpeVlanIndex": IpeVlanIndex,
       "nec": nec,
       "nec-mib": nec_mib,
       "necProductDepend": necProductDepend,
       "radioEquipment": radioEquipment,
       "pasoNeoIpe-common": pasoNeoIpe_common,
       "provisioningGroup": provisioningGroup,
       "provPwGroup": provPwGroup,
       "provPwTdmLineTable": provPwTdmLineTable,
       "provPwTdmLineEntry": provPwTdmLineEntry,
       "provPwTdmLineIfIndex": provPwTdmLineIfIndex,
       "provPwTdmLineNEAddress": provPwTdmLineNEAddress,
       "provPwTdmLineFrameMode": provPwTdmLineFrameMode,
       "provPwTdmLineCasMode": provPwTdmLineCasMode,
       "provPwTdmLineCrc4Mode": provPwTdmLineCrc4Mode,
       "provPwTdmLineJtrBfrDepth": provPwTdmLineJtrBfrDepth,
       "provPwTdmLineDstMacCheck": provPwTdmLineDstMacCheck,
       "provPwTdmTable": provPwTdmTable,
       "provPwTdmEntry": provPwTdmEntry,
       "provPwTdmPwIndex": provPwTdmPwIndex,
       "provPwTdmNEAddress": provPwTdmNEAddress,
       "provPwTdmIfIndex": provPwTdmIfIndex,
       "provPwTdmRtpHdrUsed": provPwTdmRtpHdrUsed,
       "provPwTdmFrameLength": provPwTdmFrameLength,
       "provPwTdmEncapMode": provPwTdmEncapMode,
       "provPwTdmRowStatus": provPwTdmRowStatus,
       "provPwTdmAdaptiveClkSource": provPwTdmAdaptiveClkSource,
       "provPwOverEthTable": provPwOverEthTable,
       "provPwOverEthEntry": provPwOverEthEntry,
       "provPwOverEthPwIndex": provPwOverEthPwIndex,
       "provPwOverEthNEAddress": provPwOverEthNEAddress,
       "provPwOverEthVlanId": provPwOverEthVlanId,
       "provPwOverEthTpid": provPwOverEthTpid,
       "provPwOverEthCosValue": provPwOverEthCosValue,
       "provPwOverEthEcid": provPwOverEthEcid,
       "provPwOverEthName": provPwOverEthName,
       "provPwOverEthDstMacAddress": provPwOverEthDstMacAddress}
)
