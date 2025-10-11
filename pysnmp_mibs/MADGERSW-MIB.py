# SNMP MIB module (MADGERSW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cisco/MADGERSW-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:27:25 2025
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class INTEGER48(OctetString):
    """Custom type INTEGER48 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6





class LCDText(OctetString):
    """Custom type LCDText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )
    fixed_length = 50




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Madge_ObjectIdentity = ObjectIdentity
madge = _Madge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494)
)
_Ringswitch_ObjectIdentity = ObjectIdentity
ringswitch = _Ringswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 4)
)
_RingswitchBase_ObjectIdentity = ObjectIdentity
ringswitchBase = _RingswitchBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 4, 1)
)
_RingswitchBasePSFanSpeed_Type = Integer32
_RingswitchBasePSFanSpeed_Object = MibScalar
ringswitchBasePSFanSpeed = _RingswitchBasePSFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 1, 1),
    _RingswitchBasePSFanSpeed_Type()
)
ringswitchBasePSFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchBasePSFanSpeed.setStatus("mandatory")
_RingswitchBaseExtFanSpeed_Type = Integer32
_RingswitchBaseExtFanSpeed_Object = MibScalar
ringswitchBaseExtFanSpeed = _RingswitchBaseExtFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 1, 2),
    _RingswitchBaseExtFanSpeed_Type()
)
ringswitchBaseExtFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchBaseExtFanSpeed.setStatus("mandatory")


class _RingswitchBaseRipSapSuppression_Type(Integer32):
    """Custom type ringswitchBaseRipSapSuppression based on Integer32"""
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


_RingswitchBaseRipSapSuppression_Type.__name__ = "Integer32"
_RingswitchBaseRipSapSuppression_Object = MibScalar
ringswitchBaseRipSapSuppression = _RingswitchBaseRipSapSuppression_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 1, 3),
    _RingswitchBaseRipSapSuppression_Type()
)
ringswitchBaseRipSapSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchBaseRipSapSuppression.setStatus("mandatory")


class _RingswitchBaseAREConversion_Type(Integer32):
    """Custom type ringswitchBaseAREConversion based on Integer32"""
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
        *(("enable-first", 1),
          ("enable-all", 2),
          ("enable-bcast-first", 3),
          ("enable-bcast-all", 4),
          ("disable", 5))
    )


_RingswitchBaseAREConversion_Type.__name__ = "Integer32"
_RingswitchBaseAREConversion_Object = MibScalar
ringswitchBaseAREConversion = _RingswitchBaseAREConversion_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 1, 4),
    _RingswitchBaseAREConversion_Type()
)
ringswitchBaseAREConversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchBaseAREConversion.setStatus("mandatory")
_RingswitchPort_ObjectIdentity = ObjectIdentity
ringswitchPort = _RingswitchPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 4, 2)
)
_RingswitchPortTable_Object = MibTable
ringswitchPortTable = _RingswitchPortTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1)
)
if mibBuilder.loadTexts:
    ringswitchPortTable.setStatus("mandatory")
_RingswitchPortEntry_Object = MibTableRow
ringswitchPortEntry = _RingswitchPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1)
)
ringswitchPortEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchPortNum"),
)
if mibBuilder.loadTexts:
    ringswitchPortEntry.setStatus("mandatory")


class _RingswitchPortNum_Type(Integer32):
    """Custom type ringswitchPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchPortNum_Type.__name__ = "Integer32"
_RingswitchPortNum_Object = MibTableColumn
ringswitchPortNum = _RingswitchPortNum_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 1),
    _RingswitchPortNum_Type()
)
ringswitchPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortNum.setStatus("mandatory")


class _RingswitchPortRingStatus_Type(Integer32):
    """Custom type ringswitchPortRingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("single", 2),
          ("beaconing", 3))
    )


_RingswitchPortRingStatus_Type.__name__ = "Integer32"
_RingswitchPortRingStatus_Object = MibTableColumn
ringswitchPortRingStatus = _RingswitchPortRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 2),
    _RingswitchPortRingStatus_Type()
)
ringswitchPortRingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortRingStatus.setStatus("mandatory")


class _RingswitchPortAdapterStatus_Type(Integer32):
    """Custom type ringswitchPortAdapterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2),
          ("opening", 3))
    )


_RingswitchPortAdapterStatus_Type.__name__ = "Integer32"
_RingswitchPortAdapterStatus_Object = MibTableColumn
ringswitchPortAdapterStatus = _RingswitchPortAdapterStatus_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 3),
    _RingswitchPortAdapterStatus_Type()
)
ringswitchPortAdapterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortAdapterStatus.setStatus("mandatory")


class _RingswitchPortMediaType_Type(Integer32):
    """Custom type ringswitchPortMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tr-copper", 1),
          ("tr-fiber", 2),
          ("fddi-fiber", 3))
    )


_RingswitchPortMediaType_Type.__name__ = "Integer32"
_RingswitchPortMediaType_Object = MibTableColumn
ringswitchPortMediaType = _RingswitchPortMediaType_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 4),
    _RingswitchPortMediaType_Type()
)
ringswitchPortMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortMediaType.setStatus("mandatory")


class _RingswitchPortIfMode_Type(Integer32):
    """Custom type ringswitchPortIfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("node", 1),
          ("concentrator", 2))
    )


_RingswitchPortIfMode_Type.__name__ = "Integer32"
_RingswitchPortIfMode_Object = MibTableColumn
ringswitchPortIfMode = _RingswitchPortIfMode_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 5),
    _RingswitchPortIfMode_Type()
)
ringswitchPortIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchPortIfMode.setStatus("mandatory")


class _RingswitchPortRingSpeed_Type(Integer32):
    """Custom type ringswitchPortRingSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("four", 1),
          ("sixteen", 2),
          ("hundred", 3))
    )


_RingswitchPortRingSpeed_Type.__name__ = "Integer32"
_RingswitchPortRingSpeed_Object = MibTableColumn
ringswitchPortRingSpeed = _RingswitchPortRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 6),
    _RingswitchPortRingSpeed_Type()
)
ringswitchPortRingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchPortRingSpeed.setStatus("mandatory")


class _RingswitchPortTestState_Type(Integer32):
    """Custom type ringswitchPortTestState based on Integer32"""
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
        *(("disabled", 1),
          ("running", 2),
          ("failed", 3),
          ("ok", 4),
          ("unknown", 5))
    )


_RingswitchPortTestState_Type.__name__ = "Integer32"
_RingswitchPortTestState_Object = MibTableColumn
ringswitchPortTestState = _RingswitchPortTestState_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 7),
    _RingswitchPortTestState_Type()
)
ringswitchPortTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortTestState.setStatus("mandatory")


class _RingswitchPortTestError_Type(Integer32):
    """Custom type ringswitchPortTestError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("no-error", 1),
          ("same-ring", 2),
          ("duplicate-ring", 3),
          ("fail-nb", 4),
          ("bad-rnum", 5),
          ("fail-b", 6))
    )


_RingswitchPortTestError_Type.__name__ = "Integer32"
_RingswitchPortTestError_Object = MibTableColumn
ringswitchPortTestError = _RingswitchPortTestError_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 8),
    _RingswitchPortTestError_Type()
)
ringswitchPortTestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortTestError.setStatus("mandatory")


class _RingswitchPortTestPhase_Type(Integer32):
    """Custom type ringswitchPortTestPhase based on Integer32"""
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
        *(("not-running", 1),
          ("same-ring", 2),
          ("routed", 3),
          ("broadcast", 4),
          ("success", 5))
    )


_RingswitchPortTestPhase_Type.__name__ = "Integer32"
_RingswitchPortTestPhase_Object = MibTableColumn
ringswitchPortTestPhase = _RingswitchPortTestPhase_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 9),
    _RingswitchPortTestPhase_Type()
)
ringswitchPortTestPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortTestPhase.setStatus("mandatory")
_RingswitchPortSummary_Type = Integer32
_RingswitchPortSummary_Object = MibTableColumn
ringswitchPortSummary = _RingswitchPortSummary_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 10),
    _RingswitchPortSummary_Type()
)
ringswitchPortSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortSummary.setStatus("mandatory")
_RingswitchPortAddress_Type = PhysAddress
_RingswitchPortAddress_Object = MibTableColumn
ringswitchPortAddress = _RingswitchPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 11),
    _RingswitchPortAddress_Type()
)
ringswitchPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortAddress.setStatus("mandatory")
_RingswitchPortLAA_Type = PhysAddress
_RingswitchPortLAA_Object = MibTableColumn
ringswitchPortLAA = _RingswitchPortLAA_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 12),
    _RingswitchPortLAA_Type()
)
ringswitchPortLAA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchPortLAA.setStatus("mandatory")


class _RingswitchPortStationType_Type(Integer32):
    """Custom type ringswitchPortStationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("anything", 1),
          ("workstations", 2))
    )


_RingswitchPortStationType_Type.__name__ = "Integer32"
_RingswitchPortStationType_Object = MibTableColumn
ringswitchPortStationType = _RingswitchPortStationType_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 13),
    _RingswitchPortStationType_Type()
)
ringswitchPortStationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchPortStationType.setStatus("mandatory")


class _RingswitchPortRPSEnable_Type(Integer32):
    """Custom type ringswitchPortRPSEnable based on Integer32"""
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


_RingswitchPortRPSEnable_Type.__name__ = "Integer32"
_RingswitchPortRPSEnable_Object = MibTableColumn
ringswitchPortRPSEnable = _RingswitchPortRPSEnable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 14),
    _RingswitchPortRPSEnable_Type()
)
ringswitchPortRPSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchPortRPSEnable.setStatus("mandatory")


class _RingswitchPortCutThruEnable_Type(Integer32):
    """Custom type ringswitchPortCutThruEnable based on Integer32"""
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


_RingswitchPortCutThruEnable_Type.__name__ = "Integer32"
_RingswitchPortCutThruEnable_Object = MibTableColumn
ringswitchPortCutThruEnable = _RingswitchPortCutThruEnable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 15),
    _RingswitchPortCutThruEnable_Type()
)
ringswitchPortCutThruEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchPortCutThruEnable.setStatus("mandatory")
_RingswitchPortInOctets_Type = INTEGER48
_RingswitchPortInOctets_Object = MibTableColumn
ringswitchPortInOctets = _RingswitchPortInOctets_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 16),
    _RingswitchPortInOctets_Type()
)
ringswitchPortInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortInOctets.setStatus("mandatory")
_RingswitchPortOutOctets_Type = INTEGER48
_RingswitchPortOutOctets_Object = MibTableColumn
ringswitchPortOutOctets = _RingswitchPortOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 17),
    _RingswitchPortOutOctets_Type()
)
ringswitchPortOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortOutOctets.setStatus("mandatory")
_RingswitchPortSpecInFrames_Type = INTEGER48
_RingswitchPortSpecInFrames_Object = MibTableColumn
ringswitchPortSpecInFrames = _RingswitchPortSpecInFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 18),
    _RingswitchPortSpecInFrames_Type()
)
ringswitchPortSpecInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortSpecInFrames.setStatus("mandatory")
_RingswitchPortSpecOutFrames_Type = INTEGER48
_RingswitchPortSpecOutFrames_Object = MibTableColumn
ringswitchPortSpecOutFrames = _RingswitchPortSpecOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 19),
    _RingswitchPortSpecOutFrames_Type()
)
ringswitchPortSpecOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortSpecOutFrames.setStatus("mandatory")
_RingswitchPortApeInFrames_Type = INTEGER48
_RingswitchPortApeInFrames_Object = MibTableColumn
ringswitchPortApeInFrames = _RingswitchPortApeInFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 20),
    _RingswitchPortApeInFrames_Type()
)
ringswitchPortApeInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortApeInFrames.setStatus("mandatory")
_RingswitchPortApeOutFrames_Type = INTEGER48
_RingswitchPortApeOutFrames_Object = MibTableColumn
ringswitchPortApeOutFrames = _RingswitchPortApeOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 21),
    _RingswitchPortApeOutFrames_Type()
)
ringswitchPortApeOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortApeOutFrames.setStatus("mandatory")
_RingswitchPortSteInFrames_Type = INTEGER48
_RingswitchPortSteInFrames_Object = MibTableColumn
ringswitchPortSteInFrames = _RingswitchPortSteInFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 22),
    _RingswitchPortSteInFrames_Type()
)
ringswitchPortSteInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortSteInFrames.setStatus("mandatory")
_RingswitchPortSteOutFrames_Type = INTEGER48
_RingswitchPortSteOutFrames_Object = MibTableColumn
ringswitchPortSteOutFrames = _RingswitchPortSteOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 23),
    _RingswitchPortSteOutFrames_Type()
)
ringswitchPortSteOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortSteOutFrames.setStatus("mandatory")
_RingswitchSR_ObjectIdentity = ObjectIdentity
ringswitchSR = _RingswitchSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 4, 3)
)


class _RingswitchSRAdminState_Type(Integer32):
    """Custom type ringswitchSRAdminState based on Integer32"""
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


_RingswitchSRAdminState_Type.__name__ = "Integer32"
_RingswitchSRAdminState_Object = MibScalar
ringswitchSRAdminState = _RingswitchSRAdminState_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 1),
    _RingswitchSRAdminState_Type()
)
ringswitchSRAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchSRAdminState.setStatus("mandatory")


class _RingswitchSROperState_Type(Integer32):
    """Custom type ringswitchSROperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RingswitchSROperState_Type.__name__ = "Integer32"
_RingswitchSROperState_Object = MibScalar
ringswitchSROperState = _RingswitchSROperState_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 2),
    _RingswitchSROperState_Type()
)
ringswitchSROperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchSROperState.setStatus("mandatory")
_RingswitchLCD_ObjectIdentity = ObjectIdentity
ringswitchLCD = _RingswitchLCD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 4, 4)
)


class _RingswitchLCDTotalDisplays_Type(Integer32):
    """Custom type ringswitchLCDTotalDisplays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchLCDTotalDisplays_Type.__name__ = "Integer32"
_RingswitchLCDTotalDisplays_Object = MibScalar
ringswitchLCDTotalDisplays = _RingswitchLCDTotalDisplays_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 4, 1),
    _RingswitchLCDTotalDisplays_Type()
)
ringswitchLCDTotalDisplays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchLCDTotalDisplays.setStatus("mandatory")


class _RingswitchLCDCurrentDisplay_Type(Integer32):
    """Custom type ringswitchLCDCurrentDisplay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchLCDCurrentDisplay_Type.__name__ = "Integer32"
_RingswitchLCDCurrentDisplay_Object = MibScalar
ringswitchLCDCurrentDisplay = _RingswitchLCDCurrentDisplay_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 4, 2),
    _RingswitchLCDCurrentDisplay_Type()
)
ringswitchLCDCurrentDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchLCDCurrentDisplay.setStatus("mandatory")
_RingswitchLCDCurrentMsgText_Type = LCDText
_RingswitchLCDCurrentMsgText_Object = MibScalar
ringswitchLCDCurrentMsgText = _RingswitchLCDCurrentMsgText_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 4, 3),
    _RingswitchLCDCurrentMsgText_Type()
)
ringswitchLCDCurrentMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchLCDCurrentMsgText.setStatus("mandatory")
_RingswitchLCDTable_Object = MibTable
ringswitchLCDTable = _RingswitchLCDTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 4, 4)
)
if mibBuilder.loadTexts:
    ringswitchLCDTable.setStatus("mandatory")
_RingswitchLCDTableEntry_Object = MibTableRow
ringswitchLCDTableEntry = _RingswitchLCDTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 4, 4, 1)
)
ringswitchLCDTableEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchLCDNum"),
)
if mibBuilder.loadTexts:
    ringswitchLCDTableEntry.setStatus("mandatory")


class _RingswitchLCDNum_Type(Integer32):
    """Custom type ringswitchLCDNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchLCDNum_Type.__name__ = "Integer32"
_RingswitchLCDNum_Object = MibTableColumn
ringswitchLCDNum = _RingswitchLCDNum_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 4, 4, 1, 1),
    _RingswitchLCDNum_Type()
)
ringswitchLCDNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchLCDNum.setStatus("mandatory")
_RingswitchLCDMsgText_Type = LCDText
_RingswitchLCDMsgText_Object = MibTableColumn
ringswitchLCDMsgText = _RingswitchLCDMsgText_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 4, 4, 1, 2),
    _RingswitchLCDMsgText_Type()
)
ringswitchLCDMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchLCDMsgText.setStatus("mandatory")
_RingswitchLAN_ObjectIdentity = ObjectIdentity
ringswitchLAN = _RingswitchLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 4, 5)
)
_RingswitchLANTable_Object = MibTable
ringswitchLANTable = _RingswitchLANTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 5, 1)
)
if mibBuilder.loadTexts:
    ringswitchLANTable.setStatus("mandatory")
_RingswitchLANEntry_Object = MibTableRow
ringswitchLANEntry = _RingswitchLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 5, 1, 1)
)
ringswitchLANEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchLANIndex"),
)
if mibBuilder.loadTexts:
    ringswitchLANEntry.setStatus("mandatory")


class _RingswitchLANIndex_Type(Integer32):
    """Custom type ringswitchLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchLANIndex_Type.__name__ = "Integer32"
_RingswitchLANIndex_Object = MibTableColumn
ringswitchLANIndex = _RingswitchLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 5, 1, 1, 1),
    _RingswitchLANIndex_Type()
)
ringswitchLANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchLANIndex.setStatus("mandatory")
_RingswitchLANName_Type = DisplayString
_RingswitchLANName_Object = MibTableColumn
ringswitchLANName = _RingswitchLANName_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 5, 1, 1, 2),
    _RingswitchLANName_Type()
)
ringswitchLANName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchLANName.setStatus("mandatory")


class _RingswitchLANPermeable_Type(Integer32):
    """Custom type ringswitchLANPermeable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("impermeable", 1),
          ("permeable", 2))
    )


_RingswitchLANPermeable_Type.__name__ = "Integer32"
_RingswitchLANPermeable_Object = MibTableColumn
ringswitchLANPermeable = _RingswitchLANPermeable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 5, 1, 1, 3),
    _RingswitchLANPermeable_Type()
)
ringswitchLANPermeable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchLANPermeable.setStatus("mandatory")


class _RingswitchLANStatus_Type(Integer32):
    """Custom type ringswitchLANStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_RingswitchLANStatus_Type.__name__ = "Integer32"
_RingswitchLANStatus_Object = MibTableColumn
ringswitchLANStatus = _RingswitchLANStatus_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 5, 1, 1, 4),
    _RingswitchLANStatus_Type()
)
ringswitchLANStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchLANStatus.setStatus("mandatory")
_RingswitchLANRingTable_Object = MibTable
ringswitchLANRingTable = _RingswitchLANRingTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 5, 2)
)
if mibBuilder.loadTexts:
    ringswitchLANRingTable.setStatus("mandatory")
_RingswitchLANRingEntry_Object = MibTableRow
ringswitchLANRingEntry = _RingswitchLANRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 5, 2, 1)
)
ringswitchLANRingEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchLANRingGroup"),
    (0, "MADGERSW-MIB", "ringswitchLANRingIndex"),
)
if mibBuilder.loadTexts:
    ringswitchLANRingEntry.setStatus("mandatory")
_RingswitchLANRingGroup_Type = Integer32
_RingswitchLANRingGroup_Object = MibTableColumn
ringswitchLANRingGroup = _RingswitchLANRingGroup_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 5, 2, 1, 1),
    _RingswitchLANRingGroup_Type()
)
ringswitchLANRingGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchLANRingGroup.setStatus("mandatory")
_RingswitchLANRingIndex_Type = Integer32
_RingswitchLANRingIndex_Object = MibTableColumn
ringswitchLANRingIndex = _RingswitchLANRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 5, 2, 1, 2),
    _RingswitchLANRingIndex_Type()
)
ringswitchLANRingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchLANRingIndex.setStatus("mandatory")
_RingswitchLANRingNum_Type = Integer32
_RingswitchLANRingNum_Object = MibTableColumn
ringswitchLANRingNum = _RingswitchLANRingNum_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 5, 2, 1, 3),
    _RingswitchLANRingNum_Type()
)
ringswitchLANRingNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchLANRingNum.setStatus("mandatory")


class _RingswitchLANRingStatus_Type(Integer32):
    """Custom type ringswitchLANRingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_RingswitchLANRingStatus_Type.__name__ = "Integer32"
_RingswitchLANRingStatus_Object = MibTableColumn
ringswitchLANRingStatus = _RingswitchLANRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 5, 2, 1, 4),
    _RingswitchLANRingStatus_Type()
)
ringswitchLANRingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchLANRingStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

fanPSSpeedFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 4, 0, 1)
)
fanPSSpeedFailed.setObjects(
    ("MADGERSW-MIB", "ringswitchBasePSFanSpeed")
)
if mibBuilder.loadTexts:
    fanPSSpeedFailed.setStatus(
        ""
    )

fanExtSpeedFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 4, 0, 2)
)
fanExtSpeedFailed.setObjects(
    ("MADGERSW-MIB", "ringswitchBaseExtFanSpeed")
)
if mibBuilder.loadTexts:
    fanExtSpeedFailed.setStatus(
        ""
    )

portFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 4, 0, 3)
)
portFailed.setObjects(
    ("MADGERSW-MIB", "ringswitchPortAdapterStatus")
)
if mibBuilder.loadTexts:
    portFailed.setStatus(
        ""
    )

brTestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 4, 0, 4)
)
brTestFailed.setObjects(
    ("MADGERSW-MIB", "ringswitchPortTestError")
)
if mibBuilder.loadTexts:
    brTestFailed.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MADGERSW-MIB",
    **{"DisplayString": DisplayString,
       "INTEGER48": INTEGER48,
       "LCDText": LCDText,
       "madge": madge,
       "ringswitch": ringswitch,
       "fanPSSpeedFailed": fanPSSpeedFailed,
       "fanExtSpeedFailed": fanExtSpeedFailed,
       "portFailed": portFailed,
       "brTestFailed": brTestFailed,
       "ringswitchBase": ringswitchBase,
       "ringswitchBasePSFanSpeed": ringswitchBasePSFanSpeed,
       "ringswitchBaseExtFanSpeed": ringswitchBaseExtFanSpeed,
       "ringswitchBaseRipSapSuppression": ringswitchBaseRipSapSuppression,
       "ringswitchBaseAREConversion": ringswitchBaseAREConversion,
       "ringswitchPort": ringswitchPort,
       "ringswitchPortTable": ringswitchPortTable,
       "ringswitchPortEntry": ringswitchPortEntry,
       "ringswitchPortNum": ringswitchPortNum,
       "ringswitchPortRingStatus": ringswitchPortRingStatus,
       "ringswitchPortAdapterStatus": ringswitchPortAdapterStatus,
       "ringswitchPortMediaType": ringswitchPortMediaType,
       "ringswitchPortIfMode": ringswitchPortIfMode,
       "ringswitchPortRingSpeed": ringswitchPortRingSpeed,
       "ringswitchPortTestState": ringswitchPortTestState,
       "ringswitchPortTestError": ringswitchPortTestError,
       "ringswitchPortTestPhase": ringswitchPortTestPhase,
       "ringswitchPortSummary": ringswitchPortSummary,
       "ringswitchPortAddress": ringswitchPortAddress,
       "ringswitchPortLAA": ringswitchPortLAA,
       "ringswitchPortStationType": ringswitchPortStationType,
       "ringswitchPortRPSEnable": ringswitchPortRPSEnable,
       "ringswitchPortCutThruEnable": ringswitchPortCutThruEnable,
       "ringswitchPortInOctets": ringswitchPortInOctets,
       "ringswitchPortOutOctets": ringswitchPortOutOctets,
       "ringswitchPortSpecInFrames": ringswitchPortSpecInFrames,
       "ringswitchPortSpecOutFrames": ringswitchPortSpecOutFrames,
       "ringswitchPortApeInFrames": ringswitchPortApeInFrames,
       "ringswitchPortApeOutFrames": ringswitchPortApeOutFrames,
       "ringswitchPortSteInFrames": ringswitchPortSteInFrames,
       "ringswitchPortSteOutFrames": ringswitchPortSteOutFrames,
       "ringswitchSR": ringswitchSR,
       "ringswitchSRAdminState": ringswitchSRAdminState,
       "ringswitchSROperState": ringswitchSROperState,
       "ringswitchLCD": ringswitchLCD,
       "ringswitchLCDTotalDisplays": ringswitchLCDTotalDisplays,
       "ringswitchLCDCurrentDisplay": ringswitchLCDCurrentDisplay,
       "ringswitchLCDCurrentMsgText": ringswitchLCDCurrentMsgText,
       "ringswitchLCDTable": ringswitchLCDTable,
       "ringswitchLCDTableEntry": ringswitchLCDTableEntry,
       "ringswitchLCDNum": ringswitchLCDNum,
       "ringswitchLCDMsgText": ringswitchLCDMsgText,
       "ringswitchLAN": ringswitchLAN,
       "ringswitchLANTable": ringswitchLANTable,
       "ringswitchLANEntry": ringswitchLANEntry,
       "ringswitchLANIndex": ringswitchLANIndex,
       "ringswitchLANName": ringswitchLANName,
       "ringswitchLANPermeable": ringswitchLANPermeable,
       "ringswitchLANStatus": ringswitchLANStatus,
       "ringswitchLANRingTable": ringswitchLANRingTable,
       "ringswitchLANRingEntry": ringswitchLANRingEntry,
       "ringswitchLANRingGroup": ringswitchLANRingGroup,
       "ringswitchLANRingIndex": ringswitchLANRingIndex,
       "ringswitchLANRingNum": ringswitchLANRingNum,
       "ringswitchLANRingStatus": ringswitchLANRingStatus}
)
