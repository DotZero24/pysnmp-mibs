# SNMP MIB module (STS_SEQUENZ-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltek/STS_SEQUENZ-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:17:00 2025
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

sts_system = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 16460, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Convertronic_ObjectIdentity = ObjectIdentity
convertronic = _Convertronic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16460)
)
_MeasureValues_ObjectIdentity = ObjectIdentity
measureValues = _MeasureValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1)
)
_Sts_measureValues_ObjectIdentity = ObjectIdentity
sts_measureValues = _Sts_measureValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 1)
)


class _SVal_UN_Type(Integer32):
    """Custom type sVal_UN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SVal_UN_Type.__name__ = "Integer32"
_SVal_UN_Object = MibScalar
sVal_UN = _SVal_UN_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 1, 1),
    _SVal_UN_Type()
)
sVal_UN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sVal_UN.setStatus("mandatory")


class _SVal_FreqNetz_Type(Integer32):
    """Custom type sVal_FreqNetz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SVal_FreqNetz_Type.__name__ = "Integer32"
_SVal_FreqNetz_Object = MibScalar
sVal_FreqNetz = _SVal_FreqNetz_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 1, 2),
    _SVal_FreqNetz_Type()
)
sVal_FreqNetz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sVal_FreqNetz.setStatus("mandatory")


class _SVal_UWR_Type(Integer32):
    """Custom type sVal_UWR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SVal_UWR_Type.__name__ = "Integer32"
_SVal_UWR_Object = MibScalar
sVal_UWR = _SVal_UWR_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 1, 3),
    _SVal_UWR_Type()
)
sVal_UWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sVal_UWR.setStatus("mandatory")


class _SVal_FreqWR_Type(Integer32):
    """Custom type sVal_FreqWR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SVal_FreqWR_Type.__name__ = "Integer32"
_SVal_FreqWR_Object = MibScalar
sVal_FreqWR = _SVal_FreqWR_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 1, 4),
    _SVal_FreqWR_Type()
)
sVal_FreqWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sVal_FreqWR.setStatus("mandatory")


class _SVal_UDC_Type(Integer32):
    """Custom type sVal_UDC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SVal_UDC_Type.__name__ = "Integer32"
_SVal_UDC_Object = MibScalar
sVal_UDC = _SVal_UDC_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 1, 5),
    _SVal_UDC_Type()
)
sVal_UDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sVal_UDC.setStatus("mandatory")


class _SVal_U10_Type(Integer32):
    """Custom type sVal_U10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SVal_U10_Type.__name__ = "Integer32"
_SVal_U10_Object = MibScalar
sVal_U10 = _SVal_U10_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 1, 6),
    _SVal_U10_Type()
)
sVal_U10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sVal_U10.setStatus("mandatory")


class _SVal_IO1_Type(Integer32):
    """Custom type sVal_IO1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SVal_IO1_Type.__name__ = "Integer32"
_SVal_IO1_Object = MibScalar
sVal_IO1 = _SVal_IO1_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 1, 7),
    _SVal_IO1_Type()
)
sVal_IO1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sVal_IO1.setStatus("mandatory")


class _SVal_P_Type(Integer32):
    """Custom type sVal_P based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SVal_P_Type.__name__ = "Integer32"
_SVal_P_Object = MibScalar
sVal_P = _SVal_P_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 1, 8),
    _SVal_P_Type()
)
sVal_P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sVal_P.setStatus("mandatory")


class _SVal_S_Type(Integer32):
    """Custom type sVal_S based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SVal_S_Type.__name__ = "Integer32"
_SVal_S_Object = MibScalar
sVal_S = _SVal_S_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 1, 9),
    _SVal_S_Type()
)
sVal_S.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sVal_S.setStatus("mandatory")


class _SVal_FAN1_Type(Integer32):
    """Custom type sVal_FAN1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SVal_FAN1_Type.__name__ = "Integer32"
_SVal_FAN1_Object = MibScalar
sVal_FAN1 = _SVal_FAN1_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 1, 10),
    _SVal_FAN1_Type()
)
sVal_FAN1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sVal_FAN1.setStatus("mandatory")


class _SVal_FAN2_Type(Integer32):
    """Custom type sVal_FAN2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SVal_FAN2_Type.__name__ = "Integer32"
_SVal_FAN2_Object = MibScalar
sVal_FAN2 = _SVal_FAN2_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 1, 11),
    _SVal_FAN2_Type()
)
sVal_FAN2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sVal_FAN2.setStatus("mandatory")


class _SVal_TK_Type(Integer32):
    """Custom type sVal_TK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SVal_TK_Type.__name__ = "Integer32"
_SVal_TK_Object = MibScalar
sVal_TK = _SVal_TK_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 1, 12),
    _SVal_TK_Type()
)
sVal_TK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sVal_TK.setStatus("mandatory")


class _SVal_IO2_Type(Integer32):
    """Custom type sVal_IO2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SVal_IO2_Type.__name__ = "Integer32"
_SVal_IO2_Object = MibScalar
sVal_IO2 = _SVal_IO2_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 1, 13),
    _SVal_IO2_Type()
)
sVal_IO2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sVal_IO2.setStatus("mandatory")


class _SVal_IDC_Type(Integer32):
    """Custom type sVal_IDC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SVal_IDC_Type.__name__ = "Integer32"
_SVal_IDC_Object = MibScalar
sVal_IDC = _SVal_IDC_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 1, 14),
    _SVal_IDC_Type()
)
sVal_IDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sVal_IDC.setStatus("mandatory")
_Inverter_measureValues_ObjectIdentity = ObjectIdentity
inverter_measureValues = _Inverter_measureValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 2)
)
_Inverter_Table_Object = MibTable
inverter_Table = _Inverter_Table_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    inverter_Table.setStatus("mandatory")
_Inverter_Entry_Object = MibTableRow
inverter_Entry = _Inverter_Entry_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 2, 1, 1)
)
inverter_Entry.setIndexNames(
    (0, "STS_SEQUENZ-MIB", "inv_Index"),
)
if mibBuilder.loadTexts:
    inverter_Entry.setStatus("optional")


class _Inv_Index_Type(Integer32):
    """Custom type inv_Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Inv_Index_Type.__name__ = "Integer32"
_Inv_Index_Object = MibTableColumn
inv_Index = _Inv_Index_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 2, 1, 1, 0),
    _Inv_Index_Type()
)
inv_Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inv_Index.setStatus("current")
if mibBuilder.loadTexts:
    inv_Index.setUnits("NA")


class _Inv_Nbr_Type(Integer32):
    """Custom type inv_Nbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Inv_Nbr_Type.__name__ = "Integer32"
_Inv_Nbr_Object = MibTableColumn
inv_Nbr = _Inv_Nbr_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 2, 1, 1, 1),
    _Inv_Nbr_Type()
)
inv_Nbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inv_Nbr.setStatus("mandatory")


class _Inv_InCurrent_Type(Integer32):
    """Custom type inv_InCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Inv_InCurrent_Type.__name__ = "Integer32"
_Inv_InCurrent_Object = MibTableColumn
inv_InCurrent = _Inv_InCurrent_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 2, 1, 1, 2),
    _Inv_InCurrent_Type()
)
inv_InCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inv_InCurrent.setStatus("mandatory")


class _Inv_OutCurrent_Type(Integer32):
    """Custom type inv_OutCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Inv_OutCurrent_Type.__name__ = "Integer32"
_Inv_OutCurrent_Object = MibTableColumn
inv_OutCurrent = _Inv_OutCurrent_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 2, 1, 1, 3),
    _Inv_OutCurrent_Type()
)
inv_OutCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inv_OutCurrent.setStatus("mandatory")


class _Inv_Temperature_Type(Integer32):
    """Custom type inv_Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Inv_Temperature_Type.__name__ = "Integer32"
_Inv_Temperature_Object = MibTableColumn
inv_Temperature = _Inv_Temperature_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 2, 1, 1, 4),
    _Inv_Temperature_Type()
)
inv_Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inv_Temperature.setStatus("mandatory")


class _Inv_InputVoltage_Type(Integer32):
    """Custom type inv_InputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Inv_InputVoltage_Type.__name__ = "Integer32"
_Inv_InputVoltage_Object = MibTableColumn
inv_InputVoltage = _Inv_InputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 2, 1, 1, 5),
    _Inv_InputVoltage_Type()
)
inv_InputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inv_InputVoltage.setStatus("mandatory")


class _Inv_STi_great_Type(Integer32):
    """Custom type inv_STi_great based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Inv_STi_great_Type.__name__ = "Integer32"
_Inv_STi_great_Object = MibTableColumn
inv_STi_great = _Inv_STi_great_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 2, 1, 1, 6),
    _Inv_STi_great_Type()
)
inv_STi_great.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inv_STi_great.setStatus("mandatory")


class _Inv_Fan_Type(Integer32):
    """Custom type inv_Fan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Inv_Fan_Type.__name__ = "Integer32"
_Inv_Fan_Object = MibTableColumn
inv_Fan = _Inv_Fan_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 2, 1, 1, 7),
    _Inv_Fan_Type()
)
inv_Fan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inv_Fan.setStatus("mandatory")


class _Inv_RemoteOffCan_Type(Integer32):
    """Custom type inv_RemoteOffCan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Inv_RemoteOffCan_Type.__name__ = "Integer32"
_Inv_RemoteOffCan_Object = MibTableColumn
inv_RemoteOffCan = _Inv_RemoteOffCan_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 2, 1, 1, 8),
    _Inv_RemoteOffCan_Type()
)
inv_RemoteOffCan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inv_RemoteOffCan.setStatus("mandatory")


class _Inv_UoutOff_Type(Integer32):
    """Custom type inv_UoutOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Inv_UoutOff_Type.__name__ = "Integer32"
_Inv_UoutOff_Object = MibTableColumn
inv_UoutOff = _Inv_UoutOff_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 2, 1, 1, 9),
    _Inv_UoutOff_Type()
)
inv_UoutOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inv_UoutOff.setStatus("mandatory")


class _Inv_Bit_ShortCircuit_Type(Integer32):
    """Custom type inv_Bit_ShortCircuit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Inv_Bit_ShortCircuit_Type.__name__ = "Integer32"
_Inv_Bit_ShortCircuit_Object = MibTableColumn
inv_Bit_ShortCircuit = _Inv_Bit_ShortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 2, 1, 1, 10),
    _Inv_Bit_ShortCircuit_Type()
)
inv_Bit_ShortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inv_Bit_ShortCircuit.setStatus("mandatory")


class _Inv_Bit_OutputVoltage_Type(Integer32):
    """Custom type inv_Bit_OutputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Inv_Bit_OutputVoltage_Type.__name__ = "Integer32"
_Inv_Bit_OutputVoltage_Object = MibTableColumn
inv_Bit_OutputVoltage = _Inv_Bit_OutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 2, 1, 1, 11),
    _Inv_Bit_OutputVoltage_Type()
)
inv_Bit_OutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inv_Bit_OutputVoltage.setStatus("mandatory")


class _Inv_Bit_InputVoltLow_Type(Integer32):
    """Custom type inv_Bit_InputVoltLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Inv_Bit_InputVoltLow_Type.__name__ = "Integer32"
_Inv_Bit_InputVoltLow_Object = MibTableColumn
inv_Bit_InputVoltLow = _Inv_Bit_InputVoltLow_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 2, 1, 1, 12),
    _Inv_Bit_InputVoltLow_Type()
)
inv_Bit_InputVoltLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inv_Bit_InputVoltLow.setStatus("mandatory")


class _Inv_Bit_InputVoltHigh_Type(Integer32):
    """Custom type inv_Bit_InputVoltHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Inv_Bit_InputVoltHigh_Type.__name__ = "Integer32"
_Inv_Bit_InputVoltHigh_Object = MibTableColumn
inv_Bit_InputVoltHigh = _Inv_Bit_InputVoltHigh_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 2, 1, 1, 13),
    _Inv_Bit_InputVoltHigh_Type()
)
inv_Bit_InputVoltHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inv_Bit_InputVoltHigh.setStatus("mandatory")


class _Inv_Bit_OutputVoltLow_Type(Integer32):
    """Custom type inv_Bit_OutputVoltLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Inv_Bit_OutputVoltLow_Type.__name__ = "Integer32"
_Inv_Bit_OutputVoltLow_Object = MibTableColumn
inv_Bit_OutputVoltLow = _Inv_Bit_OutputVoltLow_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 2, 1, 1, 14),
    _Inv_Bit_OutputVoltLow_Type()
)
inv_Bit_OutputVoltLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inv_Bit_OutputVoltLow.setStatus("mandatory")


class _Inv_Bit_OutputVoltHigh_Type(Integer32):
    """Custom type inv_Bit_OutputVoltHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Inv_Bit_OutputVoltHigh_Type.__name__ = "Integer32"
_Inv_Bit_OutputVoltHigh_Object = MibTableColumn
inv_Bit_OutputVoltHigh = _Inv_Bit_OutputVoltHigh_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 2, 1, 1, 15),
    _Inv_Bit_OutputVoltHigh_Type()
)
inv_Bit_OutputVoltHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inv_Bit_OutputVoltHigh.setStatus("mandatory")


class _Inv_Bit_OutputCurrHigh_Type(Integer32):
    """Custom type inv_Bit_OutputCurrHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Inv_Bit_OutputCurrHigh_Type.__name__ = "Integer32"
_Inv_Bit_OutputCurrHigh_Object = MibTableColumn
inv_Bit_OutputCurrHigh = _Inv_Bit_OutputCurrHigh_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 2, 1, 1, 16),
    _Inv_Bit_OutputCurrHigh_Type()
)
inv_Bit_OutputCurrHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inv_Bit_OutputCurrHigh.setStatus("mandatory")


class _Inv_Bit_RemoteOff_Type(Integer32):
    """Custom type inv_Bit_RemoteOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Inv_Bit_RemoteOff_Type.__name__ = "Integer32"
_Inv_Bit_RemoteOff_Object = MibTableColumn
inv_Bit_RemoteOff = _Inv_Bit_RemoteOff_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 2, 1, 1, 17),
    _Inv_Bit_RemoteOff_Type()
)
inv_Bit_RemoteOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inv_Bit_RemoteOff.setStatus("mandatory")


class _Inv_Bit_CentralAlarm_Type(Integer32):
    """Custom type inv_Bit_CentralAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Inv_Bit_CentralAlarm_Type.__name__ = "Integer32"
_Inv_Bit_CentralAlarm_Object = MibTableColumn
inv_Bit_CentralAlarm = _Inv_Bit_CentralAlarm_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 2, 1, 1, 18),
    _Inv_Bit_CentralAlarm_Type()
)
inv_Bit_CentralAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inv_Bit_CentralAlarm.setStatus("mandatory")


class _Inv_Type_Type(DisplayString):
    """Custom type inv_Type based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Inv_Type_Type.__name__ = "DisplayString"
_Inv_Type_Object = MibTableColumn
inv_Type = _Inv_Type_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 2, 1, 1, 19),
    _Inv_Type_Type()
)
inv_Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inv_Type.setStatus("mandatory")


class _Inv_Mat_CD_Type(DisplayString):
    """Custom type inv_Mat_CD based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Inv_Mat_CD_Type.__name__ = "DisplayString"
_Inv_Mat_CD_Object = MibTableColumn
inv_Mat_CD = _Inv_Mat_CD_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 2, 1, 1, 20),
    _Inv_Mat_CD_Type()
)
inv_Mat_CD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inv_Mat_CD.setStatus("mandatory")


class _Inv_SerialNo_Type(DisplayString):
    """Custom type inv_SerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Inv_SerialNo_Type.__name__ = "DisplayString"
_Inv_SerialNo_Object = MibTableColumn
inv_SerialNo = _Inv_SerialNo_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 2, 1, 1, 21),
    _Inv_SerialNo_Type()
)
inv_SerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inv_SerialNo.setStatus("mandatory")


class _Inv_HardwareVersion_Type(DisplayString):
    """Custom type inv_HardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Inv_HardwareVersion_Type.__name__ = "DisplayString"
_Inv_HardwareVersion_Object = MibTableColumn
inv_HardwareVersion = _Inv_HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 2, 1, 1, 22),
    _Inv_HardwareVersion_Type()
)
inv_HardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inv_HardwareVersion.setStatus("mandatory")


class _Inv_SoftwareVersion_Type(DisplayString):
    """Custom type inv_SoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Inv_SoftwareVersion_Type.__name__ = "DisplayString"
_Inv_SoftwareVersion_Object = MibTableColumn
inv_SoftwareVersion = _Inv_SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 1, 2, 1, 1, 23),
    _Inv_SoftwareVersion_Type()
)
inv_SoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inv_SoftwareVersion.setStatus("mandatory")
_Settings_ObjectIdentity = ObjectIdentity
settings = _Settings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2)
)
_NetworkSettings_ObjectIdentity = ObjectIdentity
networkSettings = _NetworkSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1)
)
_BaseSettings_ObjectIdentity = ObjectIdentity
baseSettings = _BaseSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 1)
)


class _BETHSpeed_Type(Integer32):
    """Custom type bETHSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BETHSpeed_Type.__name__ = "Integer32"
_BETHSpeed_Object = MibScalar
bETHSpeed = _BETHSpeed_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 1, 1),
    _BETHSpeed_Type()
)
bETHSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bETHSpeed.setStatus("mandatory")
_BLocalIP_Type = IpAddress
_BLocalIP_Object = MibScalar
bLocalIP = _BLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 1, 2),
    _BLocalIP_Type()
)
bLocalIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bLocalIP.setStatus("mandatory")
_BSubnetMask_Type = IpAddress
_BSubnetMask_Object = MibScalar
bSubnetMask = _BSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 1, 3),
    _BSubnetMask_Type()
)
bSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bSubnetMask.setStatus("mandatory")
_BGateway_Type = IpAddress
_BGateway_Object = MibScalar
bGateway = _BGateway_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 1, 4),
    _BGateway_Type()
)
bGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bGateway.setStatus("mandatory")
_BDNSServer_Type = IpAddress
_BDNSServer_Object = MibScalar
bDNSServer = _BDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 1, 5),
    _BDNSServer_Type()
)
bDNSServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bDNSServer.setStatus("mandatory")


class _BDHCPServer_Type(DisplayString):
    """Custom type bDHCPServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BDHCPServer_Type.__name__ = "DisplayString"
_BDHCPServer_Object = MibScalar
bDHCPServer = _BDHCPServer_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 1, 6),
    _BDHCPServer_Type()
)
bDHCPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bDHCPServer.setStatus("mandatory")


class _BFixedIP_OnOff_Type(Integer32):
    """Custom type bFixedIP_OnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BFixedIP_OnOff_Type.__name__ = "Integer32"
_BFixedIP_OnOff_Object = MibScalar
bFixedIP_OnOff = _BFixedIP_OnOff_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 1, 7),
    _BFixedIP_OnOff_Type()
)
bFixedIP_OnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bFixedIP_OnOff.setStatus("mandatory")


class _BDefaultIP_OnOff_Type(Integer32):
    """Custom type bDefaultIP_OnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BDefaultIP_OnOff_Type.__name__ = "Integer32"
_BDefaultIP_OnOff_Object = MibScalar
bDefaultIP_OnOff = _BDefaultIP_OnOff_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 1, 8),
    _BDefaultIP_OnOff_Type()
)
bDefaultIP_OnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bDefaultIP_OnOff.setStatus("mandatory")


class _BDHCP_OnOff_Type(Integer32):
    """Custom type bDHCP_OnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BDHCP_OnOff_Type.__name__ = "Integer32"
_BDHCP_OnOff_Object = MibScalar
bDHCP_OnOff = _BDHCP_OnOff_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 1, 9),
    _BDHCP_OnOff_Type()
)
bDHCP_OnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bDHCP_OnOff.setStatus("mandatory")


class _BBOOTP_OnOff_Type(Integer32):
    """Custom type bBOOTP_OnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BBOOTP_OnOff_Type.__name__ = "Integer32"
_BBOOTP_OnOff_Object = MibScalar
bBOOTP_OnOff = _BBOOTP_OnOff_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 1, 10),
    _BBOOTP_OnOff_Type()
)
bBOOTP_OnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bBOOTP_OnOff.setStatus("mandatory")


class _BLocation_Type(DisplayString):
    """Custom type bLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BLocation_Type.__name__ = "DisplayString"
_BLocation_Object = MibScalar
bLocation = _BLocation_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 1, 11),
    _BLocation_Type()
)
bLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bLocation.setStatus("mandatory")
_ServiceSettings_ObjectIdentity = ObjectIdentity
serviceSettings = _ServiceSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 2)
)


class _ServSNMP_OnOff_Type(Integer32):
    """Custom type servSNMP_OnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ServSNMP_OnOff_Type.__name__ = "Integer32"
_ServSNMP_OnOff_Object = MibScalar
servSNMP_OnOff = _ServSNMP_OnOff_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 2, 1),
    _ServSNMP_OnOff_Type()
)
servSNMP_OnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    servSNMP_OnOff.setStatus("mandatory")
_ServTrapReceiver1_Type = IpAddress
_ServTrapReceiver1_Object = MibScalar
servTrapReceiver1 = _ServTrapReceiver1_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 2, 2),
    _ServTrapReceiver1_Type()
)
servTrapReceiver1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    servTrapReceiver1.setStatus("mandatory")
_ServTrapReceiver2_Type = IpAddress
_ServTrapReceiver2_Object = MibScalar
servTrapReceiver2 = _ServTrapReceiver2_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 2, 3),
    _ServTrapReceiver2_Type()
)
servTrapReceiver2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    servTrapReceiver2.setStatus("mandatory")
_ServTrapReceiver3_Type = IpAddress
_ServTrapReceiver3_Object = MibScalar
servTrapReceiver3 = _ServTrapReceiver3_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 2, 4),
    _ServTrapReceiver3_Type()
)
servTrapReceiver3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    servTrapReceiver3.setStatus("mandatory")
_ServTrapReceiver4_Type = IpAddress
_ServTrapReceiver4_Object = MibScalar
servTrapReceiver4 = _ServTrapReceiver4_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 2, 5),
    _ServTrapReceiver4_Type()
)
servTrapReceiver4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    servTrapReceiver4.setStatus("mandatory")


class _ServReadCommunity_Type(DisplayString):
    """Custom type servReadCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_ServReadCommunity_Type.__name__ = "DisplayString"
_ServReadCommunity_Object = MibScalar
servReadCommunity = _ServReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 2, 6),
    _ServReadCommunity_Type()
)
servReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    servReadCommunity.setStatus("mandatory")


class _ServWriteCommunity_Type(DisplayString):
    """Custom type servWriteCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_ServWriteCommunity_Type.__name__ = "DisplayString"
_ServWriteCommunity_Object = MibScalar
servWriteCommunity = _ServWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 2, 7),
    _ServWriteCommunity_Type()
)
servWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    servWriteCommunity.setStatus("mandatory")


class _ServSMTP_OnOff_Type(Integer32):
    """Custom type servSMTP_OnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ServSMTP_OnOff_Type.__name__ = "Integer32"
_ServSMTP_OnOff_Object = MibScalar
servSMTP_OnOff = _ServSMTP_OnOff_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 2, 8),
    _ServSMTP_OnOff_Type()
)
servSMTP_OnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    servSMTP_OnOff.setStatus("mandatory")


class _ServMailServer_Type(DisplayString):
    """Custom type servMailServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_ServMailServer_Type.__name__ = "DisplayString"
_ServMailServer_Object = MibScalar
servMailServer = _ServMailServer_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 2, 9),
    _ServMailServer_Type()
)
servMailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    servMailServer.setStatus("mandatory")


class _ServMailUsername_Type(DisplayString):
    """Custom type servMailUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ServMailUsername_Type.__name__ = "DisplayString"
_ServMailUsername_Object = MibScalar
servMailUsername = _ServMailUsername_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 2, 10),
    _ServMailUsername_Type()
)
servMailUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    servMailUsername.setStatus("mandatory")


class _ServMailPassword_Type(DisplayString):
    """Custom type servMailPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ServMailPassword_Type.__name__ = "DisplayString"
_ServMailPassword_Object = MibScalar
servMailPassword = _ServMailPassword_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 2, 11),
    _ServMailPassword_Type()
)
servMailPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    servMailPassword.setStatus("mandatory")


class _ServMailReceiver1_Type(DisplayString):
    """Custom type servMailReceiver1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_ServMailReceiver1_Type.__name__ = "DisplayString"
_ServMailReceiver1_Object = MibScalar
servMailReceiver1 = _ServMailReceiver1_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 2, 12),
    _ServMailReceiver1_Type()
)
servMailReceiver1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    servMailReceiver1.setStatus("mandatory")


class _ServMailTrapLevel1_Type(Integer32):
    """Custom type servMailTrapLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ServMailTrapLevel1_Type.__name__ = "Integer32"
_ServMailTrapLevel1_Object = MibScalar
servMailTrapLevel1 = _ServMailTrapLevel1_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 2, 13),
    _ServMailTrapLevel1_Type()
)
servMailTrapLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    servMailTrapLevel1.setStatus("mandatory")


class _ServMailReceiver2_Type(DisplayString):
    """Custom type servMailReceiver2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_ServMailReceiver2_Type.__name__ = "DisplayString"
_ServMailReceiver2_Object = MibScalar
servMailReceiver2 = _ServMailReceiver2_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 2, 14),
    _ServMailReceiver2_Type()
)
servMailReceiver2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    servMailReceiver2.setStatus("mandatory")


class _ServMailTrapLevel2_Type(Integer32):
    """Custom type servMailTrapLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ServMailTrapLevel2_Type.__name__ = "Integer32"
_ServMailTrapLevel2_Object = MibScalar
servMailTrapLevel2 = _ServMailTrapLevel2_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 2, 15),
    _ServMailTrapLevel2_Type()
)
servMailTrapLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    servMailTrapLevel2.setStatus("mandatory")


class _ServSNTP_OnOff_Type(Integer32):
    """Custom type servSNTP_OnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ServSNTP_OnOff_Type.__name__ = "Integer32"
_ServSNTP_OnOff_Object = MibScalar
servSNTP_OnOff = _ServSNTP_OnOff_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 2, 16),
    _ServSNTP_OnOff_Type()
)
servSNTP_OnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    servSNTP_OnOff.setStatus("mandatory")


class _ServSNTPServer1_Type(DisplayString):
    """Custom type servSNTPServer1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_ServSNTPServer1_Type.__name__ = "DisplayString"
_ServSNTPServer1_Object = MibScalar
servSNTPServer1 = _ServSNTPServer1_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 2, 17),
    _ServSNTPServer1_Type()
)
servSNTPServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    servSNTPServer1.setStatus("mandatory")


class _ServSNTPServer2_Type(DisplayString):
    """Custom type servSNTPServer2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_ServSNTPServer2_Type.__name__ = "DisplayString"
_ServSNTPServer2_Object = MibScalar
servSNTPServer2 = _ServSNTPServer2_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 2, 18),
    _ServSNTPServer2_Type()
)
servSNTPServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    servSNTPServer2.setStatus("mandatory")


class _ServTelnet_OnOff_Type(Integer32):
    """Custom type servTelnet_OnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ServTelnet_OnOff_Type.__name__ = "Integer32"
_ServTelnet_OnOff_Object = MibScalar
servTelnet_OnOff = _ServTelnet_OnOff_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 2, 19),
    _ServTelnet_OnOff_Type()
)
servTelnet_OnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    servTelnet_OnOff.setStatus("mandatory")


class _ServSyslog_OnOff_Type(Integer32):
    """Custom type servSyslog_OnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ServSyslog_OnOff_Type.__name__ = "Integer32"
_ServSyslog_OnOff_Object = MibScalar
servSyslog_OnOff = _ServSyslog_OnOff_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 1, 2, 20),
    _ServSyslog_OnOff_Type()
)
servSyslog_OnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    servSyslog_OnOff.setStatus("mandatory")
_UnitSettings_ObjectIdentity = ObjectIdentity
unitSettings = _UnitSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2)
)
_BasicSettings_ObjectIdentity = ObjectIdentity
basicSettings = _BasicSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 1)
)


class _Sts_Version_Type(Integer32):
    """Custom type sts_Version based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Sts_Version_Type.__name__ = "Integer32"
_Sts_Version_Object = MibScalar
sts_Version = _Sts_Version_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 1, 1),
    _Sts_Version_Type()
)
sts_Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts_Version.setStatus("mandatory")


class _Sts_Inverter_Type(Integer32):
    """Custom type sts_Inverter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Sts_Inverter_Type.__name__ = "Integer32"
_Sts_Inverter_Object = MibScalar
sts_Inverter = _Sts_Inverter_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 1, 2),
    _Sts_Inverter_Type()
)
sts_Inverter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_Inverter.setStatus("mandatory")


class _Sts_SigCF_b0_Type(Integer32):
    """Custom type sts_SigCF_b0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigCF_b0_Type.__name__ = "Integer32"
_Sts_SigCF_b0_Object = MibScalar
sts_SigCF_b0 = _Sts_SigCF_b0_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 1, 3),
    _Sts_SigCF_b0_Type()
)
sts_SigCF_b0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigCF_b0.setStatus("mandatory")


class _Sts_SigCF_b1_Type(Integer32):
    """Custom type sts_SigCF_b1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigCF_b1_Type.__name__ = "Integer32"
_Sts_SigCF_b1_Object = MibScalar
sts_SigCF_b1 = _Sts_SigCF_b1_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 1, 4),
    _Sts_SigCF_b1_Type()
)
sts_SigCF_b1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigCF_b1.setStatus("mandatory")


class _Sts_SigCF_b2_Type(Integer32):
    """Custom type sts_SigCF_b2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigCF_b2_Type.__name__ = "Integer32"
_Sts_SigCF_b2_Object = MibScalar
sts_SigCF_b2 = _Sts_SigCF_b2_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 1, 5),
    _Sts_SigCF_b2_Type()
)
sts_SigCF_b2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigCF_b2.setStatus("mandatory")


class _Sts_SigCF_b3_Type(Integer32):
    """Custom type sts_SigCF_b3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigCF_b3_Type.__name__ = "Integer32"
_Sts_SigCF_b3_Object = MibScalar
sts_SigCF_b3 = _Sts_SigCF_b3_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 1, 6),
    _Sts_SigCF_b3_Type()
)
sts_SigCF_b3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigCF_b3.setStatus("mandatory")


class _Sts_SigCF_b4_Type(Integer32):
    """Custom type sts_SigCF_b4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigCF_b4_Type.__name__ = "Integer32"
_Sts_SigCF_b4_Object = MibScalar
sts_SigCF_b4 = _Sts_SigCF_b4_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 1, 7),
    _Sts_SigCF_b4_Type()
)
sts_SigCF_b4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigCF_b4.setStatus("mandatory")


class _Sts_SigCF_b5_Type(Integer32):
    """Custom type sts_SigCF_b5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigCF_b5_Type.__name__ = "Integer32"
_Sts_SigCF_b5_Object = MibScalar
sts_SigCF_b5 = _Sts_SigCF_b5_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 1, 8),
    _Sts_SigCF_b5_Type()
)
sts_SigCF_b5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigCF_b5.setStatus("mandatory")


class _Sts_SigCF_b6_Type(Integer32):
    """Custom type sts_SigCF_b6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigCF_b6_Type.__name__ = "Integer32"
_Sts_SigCF_b6_Object = MibScalar
sts_SigCF_b6 = _Sts_SigCF_b6_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 1, 9),
    _Sts_SigCF_b6_Type()
)
sts_SigCF_b6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigCF_b6.setStatus("mandatory")


class _Sts_SigCF_b7_Type(Integer32):
    """Custom type sts_SigCF_b7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigCF_b7_Type.__name__ = "Integer32"
_Sts_SigCF_b7_Object = MibScalar
sts_SigCF_b7 = _Sts_SigCF_b7_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 1, 10),
    _Sts_SigCF_b7_Type()
)
sts_SigCF_b7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigCF_b7.setStatus("mandatory")


class _Sts_SigCF_b8_Type(Integer32):
    """Custom type sts_SigCF_b8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigCF_b8_Type.__name__ = "Integer32"
_Sts_SigCF_b8_Object = MibScalar
sts_SigCF_b8 = _Sts_SigCF_b8_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 1, 11),
    _Sts_SigCF_b8_Type()
)
sts_SigCF_b8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigCF_b8.setStatus("mandatory")


class _Sts_SigCF_b9_Type(Integer32):
    """Custom type sts_SigCF_b9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigCF_b9_Type.__name__ = "Integer32"
_Sts_SigCF_b9_Object = MibScalar
sts_SigCF_b9 = _Sts_SigCF_b9_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 1, 12),
    _Sts_SigCF_b9_Type()
)
sts_SigCF_b9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigCF_b9.setStatus("mandatory")


class _Sts_SigCF_b10_Type(Integer32):
    """Custom type sts_SigCF_b10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigCF_b10_Type.__name__ = "Integer32"
_Sts_SigCF_b10_Object = MibScalar
sts_SigCF_b10 = _Sts_SigCF_b10_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 1, 13),
    _Sts_SigCF_b10_Type()
)
sts_SigCF_b10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigCF_b10.setStatus("mandatory")


class _Sts_SigCF_b11_Type(Integer32):
    """Custom type sts_SigCF_b11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigCF_b11_Type.__name__ = "Integer32"
_Sts_SigCF_b11_Object = MibScalar
sts_SigCF_b11 = _Sts_SigCF_b11_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 1, 14),
    _Sts_SigCF_b11_Type()
)
sts_SigCF_b11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigCF_b11.setStatus("mandatory")


class _Sts_SigCF_b12_Type(Integer32):
    """Custom type sts_SigCF_b12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigCF_b12_Type.__name__ = "Integer32"
_Sts_SigCF_b12_Object = MibScalar
sts_SigCF_b12 = _Sts_SigCF_b12_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 1, 15),
    _Sts_SigCF_b12_Type()
)
sts_SigCF_b12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigCF_b12.setStatus("mandatory")


class _Sts_SigCF_b13_Type(Integer32):
    """Custom type sts_SigCF_b13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigCF_b13_Type.__name__ = "Integer32"
_Sts_SigCF_b13_Object = MibScalar
sts_SigCF_b13 = _Sts_SigCF_b13_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 1, 16),
    _Sts_SigCF_b13_Type()
)
sts_SigCF_b13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigCF_b13.setStatus("mandatory")


class _Sts_SigCF_b14_Type(Integer32):
    """Custom type sts_SigCF_b14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigCF_b14_Type.__name__ = "Integer32"
_Sts_SigCF_b14_Object = MibScalar
sts_SigCF_b14 = _Sts_SigCF_b14_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 1, 17),
    _Sts_SigCF_b14_Type()
)
sts_SigCF_b14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigCF_b14.setStatus("mandatory")


class _Sts_SigCF_b15_Type(Integer32):
    """Custom type sts_SigCF_b15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigCF_b15_Type.__name__ = "Integer32"
_Sts_SigCF_b15_Object = MibScalar
sts_SigCF_b15 = _Sts_SigCF_b15_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 1, 18),
    _Sts_SigCF_b15_Type()
)
sts_SigCF_b15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigCF_b15.setStatus("mandatory")


class _Sts_DelayRelCA_Type(Integer32):
    """Custom type sts_DelayRelCA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Sts_DelayRelCA_Type.__name__ = "Integer32"
_Sts_DelayRelCA_Object = MibScalar
sts_DelayRelCA = _Sts_DelayRelCA_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 1, 19),
    _Sts_DelayRelCA_Type()
)
sts_DelayRelCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_DelayRelCA.setStatus("mandatory")


class _Sts_DelayLEDCA_Type(Integer32):
    """Custom type sts_DelayLEDCA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Sts_DelayLEDCA_Type.__name__ = "Integer32"
_Sts_DelayLEDCA_Object = MibScalar
sts_DelayLEDCA = _Sts_DelayLEDCA_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 1, 20),
    _Sts_DelayLEDCA_Type()
)
sts_DelayLEDCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_DelayLEDCA.setStatus("mandatory")


class _Sts_LCDContrast_Type(Integer32):
    """Custom type sts_LCDContrast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Sts_LCDContrast_Type.__name__ = "Integer32"
_Sts_LCDContrast_Object = MibScalar
sts_LCDContrast = _Sts_LCDContrast_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 1, 21),
    _Sts_LCDContrast_Type()
)
sts_LCDContrast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_LCDContrast.setStatus("mandatory")


class _Sts_Language_Type(Integer32):
    """Custom type sts_Language based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Sts_Language_Type.__name__ = "Integer32"
_Sts_Language_Object = MibScalar
sts_Language = _Sts_Language_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 1, 22),
    _Sts_Language_Type()
)
sts_Language.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_Language.setStatus("mandatory")
_AdvancedSettings_ObjectIdentity = ObjectIdentity
advancedSettings = _AdvancedSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 2)
)


class _Sts_OpMode_Type(Integer32):
    """Custom type sts_OpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_OpMode_Type.__name__ = "Integer32"
_Sts_OpMode_Object = MibScalar
sts_OpMode = _Sts_OpMode_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 2, 1),
    _Sts_OpMode_Type()
)
sts_OpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_OpMode.setStatus("mandatory")


class _Sts_UpperSwitchLimS1_Type(Integer32):
    """Custom type sts_UpperSwitchLimS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_Sts_UpperSwitchLimS1_Type.__name__ = "Integer32"
_Sts_UpperSwitchLimS1_Object = MibScalar
sts_UpperSwitchLimS1 = _Sts_UpperSwitchLimS1_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 2, 2),
    _Sts_UpperSwitchLimS1_Type()
)
sts_UpperSwitchLimS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_UpperSwitchLimS1.setStatus("mandatory")


class _Sts_LowerSwitchLimS1_Type(Integer32):
    """Custom type sts_LowerSwitchLimS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_Sts_LowerSwitchLimS1_Type.__name__ = "Integer32"
_Sts_LowerSwitchLimS1_Object = MibScalar
sts_LowerSwitchLimS1 = _Sts_LowerSwitchLimS1_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 2, 3),
    _Sts_LowerSwitchLimS1_Type()
)
sts_LowerSwitchLimS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_LowerSwitchLimS1.setStatus("mandatory")


class _Sts_SwitchDelayS1_Type(Integer32):
    """Custom type sts_SwitchDelayS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Sts_SwitchDelayS1_Type.__name__ = "Integer32"
_Sts_SwitchDelayS1_Object = MibScalar
sts_SwitchDelayS1 = _Sts_SwitchDelayS1_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 2, 4),
    _Sts_SwitchDelayS1_Type()
)
sts_SwitchDelayS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SwitchDelayS1.setStatus("mandatory")


class _Sts_UpperSwitchLimS2_Type(Integer32):
    """Custom type sts_UpperSwitchLimS2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_Sts_UpperSwitchLimS2_Type.__name__ = "Integer32"
_Sts_UpperSwitchLimS2_Object = MibScalar
sts_UpperSwitchLimS2 = _Sts_UpperSwitchLimS2_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 2, 5),
    _Sts_UpperSwitchLimS2_Type()
)
sts_UpperSwitchLimS2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_UpperSwitchLimS2.setStatus("mandatory")


class _Sts_LowerSwitchLimS2_Type(Integer32):
    """Custom type sts_LowerSwitchLimS2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_Sts_LowerSwitchLimS2_Type.__name__ = "Integer32"
_Sts_LowerSwitchLimS2_Object = MibScalar
sts_LowerSwitchLimS2 = _Sts_LowerSwitchLimS2_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 2, 6),
    _Sts_LowerSwitchLimS2_Type()
)
sts_LowerSwitchLimS2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_LowerSwitchLimS2.setStatus("mandatory")


class _Sts_SwitchDelayS2_Type(Integer32):
    """Custom type sts_SwitchDelayS2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Sts_SwitchDelayS2_Type.__name__ = "Integer32"
_Sts_SwitchDelayS2_Object = MibScalar
sts_SwitchDelayS2 = _Sts_SwitchDelayS2_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 2, 7),
    _Sts_SwitchDelayS2_Type()
)
sts_SwitchDelayS2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SwitchDelayS2.setStatus("mandatory")


class _Sts_MaxCellVolt1_Type(Integer32):
    """Custom type sts_MaxCellVolt1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 300),
    )


_Sts_MaxCellVolt1_Type.__name__ = "Integer32"
_Sts_MaxCellVolt1_Object = MibScalar
sts_MaxCellVolt1 = _Sts_MaxCellVolt1_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 2, 8),
    _Sts_MaxCellVolt1_Type()
)
sts_MaxCellVolt1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_MaxCellVolt1.setStatus("mandatory")


class _Sts_MinCellVolt1_Type(Integer32):
    """Custom type sts_MinCellVolt1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(70, 250),
    )


_Sts_MinCellVolt1_Type.__name__ = "Integer32"
_Sts_MinCellVolt1_Object = MibScalar
sts_MinCellVolt1 = _Sts_MinCellVolt1_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 2, 9),
    _Sts_MinCellVolt1_Type()
)
sts_MinCellVolt1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_MinCellVolt1.setStatus("mandatory")


class _Sts_MinCellVolt2_Type(Integer32):
    """Custom type sts_MinCellVolt2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 250),
    )


_Sts_MinCellVolt2_Type.__name__ = "Integer32"
_Sts_MinCellVolt2_Object = MibScalar
sts_MinCellVolt2 = _Sts_MinCellVolt2_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 2, 10),
    _Sts_MinCellVolt2_Type()
)
sts_MinCellVolt2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_MinCellVolt2.setStatus("mandatory")


class _Sts_MinULimit_Type(Integer32):
    """Custom type sts_MinULimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(170, 210),
    )


_Sts_MinULimit_Type.__name__ = "Integer32"
_Sts_MinULimit_Object = MibScalar
sts_MinULimit = _Sts_MinULimit_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 2, 11),
    _Sts_MinULimit_Type()
)
sts_MinULimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_MinULimit.setStatus("mandatory")


class _Sts_MaxULimit_Type(Integer32):
    """Custom type sts_MaxULimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(220, 250),
    )


_Sts_MaxULimit_Type.__name__ = "Integer32"
_Sts_MaxULimit_Object = MibScalar
sts_MaxULimit = _Sts_MaxULimit_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 2, 12),
    _Sts_MaxULimit_Type()
)
sts_MaxULimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_MaxULimit.setStatus("mandatory")
_AdvancedSettings2_ObjectIdentity = ObjectIdentity
advancedSettings2 = _AdvancedSettings2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 3)
)


class _Sts_NomPower_Type(Integer32):
    """Custom type sts_NomPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 500),
    )


_Sts_NomPower_Type.__name__ = "Integer32"
_Sts_NomPower_Object = MibScalar
sts_NomPower = _Sts_NomPower_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 3, 1),
    _Sts_NomPower_Type()
)
sts_NomPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_NomPower.setStatus("mandatory")


class _Sts_NomVolt_Type(Integer32):
    """Custom type sts_NomVolt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 250),
    )


_Sts_NomVolt_Type.__name__ = "Integer32"
_Sts_NomVolt_Object = MibScalar
sts_NomVolt = _Sts_NomVolt_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 3, 2),
    _Sts_NomVolt_Type()
)
sts_NomVolt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_NomVolt.setStatus("mandatory")


class _Sts_NomFreq_Type(Integer32):
    """Custom type sts_NomFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_NomFreq_Type.__name__ = "Integer32"
_Sts_NomFreq_Object = MibScalar
sts_NomFreq = _Sts_NomFreq_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 3, 3),
    _Sts_NomFreq_Type()
)
sts_NomFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_NomFreq.setStatus("mandatory")


class _Sts_FreqRange_Type(Integer32):
    """Custom type sts_FreqRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Sts_FreqRange_Type.__name__ = "Integer32"
_Sts_FreqRange_Object = MibScalar
sts_FreqRange = _Sts_FreqRange_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 3, 4),
    _Sts_FreqRange_Type()
)
sts_FreqRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_FreqRange.setStatus("mandatory")


class _Sts_MaxCurrent_Type(Integer32):
    """Custom type sts_MaxCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2500),
    )


_Sts_MaxCurrent_Type.__name__ = "Integer32"
_Sts_MaxCurrent_Object = MibScalar
sts_MaxCurrent = _Sts_MaxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 3, 5),
    _Sts_MaxCurrent_Type()
)
sts_MaxCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_MaxCurrent.setStatus("mandatory")


class _Sts_PresentCell_Type(Integer32):
    """Custom type sts_PresentCell based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(12, 200),
    )


_Sts_PresentCell_Type.__name__ = "Integer32"
_Sts_PresentCell_Object = MibScalar
sts_PresentCell = _Sts_PresentCell_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 3, 6),
    _Sts_PresentCell_Type()
)
sts_PresentCell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_PresentCell.setStatus("mandatory")


class _Sts_CellVoltage_Type(Integer32):
    """Custom type sts_CellVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_CellVoltage_Type.__name__ = "Integer32"
_Sts_CellVoltage_Object = MibScalar
sts_CellVoltage = _Sts_CellVoltage_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 3, 7),
    _Sts_CellVoltage_Type()
)
sts_CellVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_CellVoltage.setStatus("mandatory")


class _Sts_Adress_Type(Integer32):
    """Custom type sts_Adress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Sts_Adress_Type.__name__ = "Integer32"
_Sts_Adress_Object = MibScalar
sts_Adress = _Sts_Adress_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 3, 8),
    _Sts_Adress_Type()
)
sts_Adress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_Adress.setStatus("mandatory")


class _Sts_SigRel2_b0_Type(Integer32):
    """Custom type sts_SigRel2_b0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigRel2_b0_Type.__name__ = "Integer32"
_Sts_SigRel2_b0_Object = MibScalar
sts_SigRel2_b0 = _Sts_SigRel2_b0_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 3, 9),
    _Sts_SigRel2_b0_Type()
)
sts_SigRel2_b0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigRel2_b0.setStatus("mandatory")


class _Sts_SigRel2_b1_Type(Integer32):
    """Custom type sts_SigRel2_b1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigRel2_b1_Type.__name__ = "Integer32"
_Sts_SigRel2_b1_Object = MibScalar
sts_SigRel2_b1 = _Sts_SigRel2_b1_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 3, 10),
    _Sts_SigRel2_b1_Type()
)
sts_SigRel2_b1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigRel2_b1.setStatus("mandatory")


class _Sts_SigRel2_b2_Type(Integer32):
    """Custom type sts_SigRel2_b2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigRel2_b2_Type.__name__ = "Integer32"
_Sts_SigRel2_b2_Object = MibScalar
sts_SigRel2_b2 = _Sts_SigRel2_b2_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 3, 11),
    _Sts_SigRel2_b2_Type()
)
sts_SigRel2_b2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigRel2_b2.setStatus("mandatory")


class _Sts_SigRel2_b3_Type(Integer32):
    """Custom type sts_SigRel2_b3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigRel2_b3_Type.__name__ = "Integer32"
_Sts_SigRel2_b3_Object = MibScalar
sts_SigRel2_b3 = _Sts_SigRel2_b3_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 3, 12),
    _Sts_SigRel2_b3_Type()
)
sts_SigRel2_b3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigRel2_b3.setStatus("mandatory")


class _Sts_SigRel2_b4_Type(Integer32):
    """Custom type sts_SigRel2_b4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigRel2_b4_Type.__name__ = "Integer32"
_Sts_SigRel2_b4_Object = MibScalar
sts_SigRel2_b4 = _Sts_SigRel2_b4_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 3, 13),
    _Sts_SigRel2_b4_Type()
)
sts_SigRel2_b4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigRel2_b4.setStatus("mandatory")


class _Sts_SigRel2_b5_Type(Integer32):
    """Custom type sts_SigRel2_b5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigRel2_b5_Type.__name__ = "Integer32"
_Sts_SigRel2_b5_Object = MibScalar
sts_SigRel2_b5 = _Sts_SigRel2_b5_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 3, 14),
    _Sts_SigRel2_b5_Type()
)
sts_SigRel2_b5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigRel2_b5.setStatus("mandatory")


class _Sts_SigRel2_b6_Type(Integer32):
    """Custom type sts_SigRel2_b6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigRel2_b6_Type.__name__ = "Integer32"
_Sts_SigRel2_b6_Object = MibScalar
sts_SigRel2_b6 = _Sts_SigRel2_b6_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 3, 15),
    _Sts_SigRel2_b6_Type()
)
sts_SigRel2_b6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigRel2_b6.setStatus("mandatory")


class _Sts_SigRel2_b7_Type(Integer32):
    """Custom type sts_SigRel2_b7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigRel2_b7_Type.__name__ = "Integer32"
_Sts_SigRel2_b7_Object = MibScalar
sts_SigRel2_b7 = _Sts_SigRel2_b7_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 3, 16),
    _Sts_SigRel2_b7_Type()
)
sts_SigRel2_b7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigRel2_b7.setStatus("mandatory")


class _Sts_SigRel2_b8_Type(Integer32):
    """Custom type sts_SigRel2_b8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigRel2_b8_Type.__name__ = "Integer32"
_Sts_SigRel2_b8_Object = MibScalar
sts_SigRel2_b8 = _Sts_SigRel2_b8_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 3, 17),
    _Sts_SigRel2_b8_Type()
)
sts_SigRel2_b8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigRel2_b8.setStatus("mandatory")


class _Sts_SigRel2_b9_Type(Integer32):
    """Custom type sts_SigRel2_b9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigRel2_b9_Type.__name__ = "Integer32"
_Sts_SigRel2_b9_Object = MibScalar
sts_SigRel2_b9 = _Sts_SigRel2_b9_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 3, 18),
    _Sts_SigRel2_b9_Type()
)
sts_SigRel2_b9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigRel2_b9.setStatus("mandatory")


class _Sts_SigRel2_b10_Type(Integer32):
    """Custom type sts_SigRel2_b10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigRel2_b10_Type.__name__ = "Integer32"
_Sts_SigRel2_b10_Object = MibScalar
sts_SigRel2_b10 = _Sts_SigRel2_b10_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 3, 19),
    _Sts_SigRel2_b10_Type()
)
sts_SigRel2_b10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigRel2_b10.setStatus("mandatory")


class _Sts_SigRel2_b11_Type(Integer32):
    """Custom type sts_SigRel2_b11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigRel2_b11_Type.__name__ = "Integer32"
_Sts_SigRel2_b11_Object = MibScalar
sts_SigRel2_b11 = _Sts_SigRel2_b11_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 3, 20),
    _Sts_SigRel2_b11_Type()
)
sts_SigRel2_b11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigRel2_b11.setStatus("mandatory")


class _Sts_SigRel2_b12_Type(Integer32):
    """Custom type sts_SigRel2_b12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigRel2_b12_Type.__name__ = "Integer32"
_Sts_SigRel2_b12_Object = MibScalar
sts_SigRel2_b12 = _Sts_SigRel2_b12_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 3, 21),
    _Sts_SigRel2_b12_Type()
)
sts_SigRel2_b12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigRel2_b12.setStatus("mandatory")


class _Sts_SigRel2_b13_Type(Integer32):
    """Custom type sts_SigRel2_b13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigRel2_b13_Type.__name__ = "Integer32"
_Sts_SigRel2_b13_Object = MibScalar
sts_SigRel2_b13 = _Sts_SigRel2_b13_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 3, 22),
    _Sts_SigRel2_b13_Type()
)
sts_SigRel2_b13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigRel2_b13.setStatus("mandatory")


class _Sts_SigRel2_b14_Type(Integer32):
    """Custom type sts_SigRel2_b14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigRel2_b14_Type.__name__ = "Integer32"
_Sts_SigRel2_b14_Object = MibScalar
sts_SigRel2_b14 = _Sts_SigRel2_b14_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 3, 23),
    _Sts_SigRel2_b14_Type()
)
sts_SigRel2_b14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigRel2_b14.setStatus("mandatory")


class _Sts_SigRel2_b15_Type(Integer32):
    """Custom type sts_SigRel2_b15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_SigRel2_b15_Type.__name__ = "Integer32"
_Sts_SigRel2_b15_Object = MibScalar
sts_SigRel2_b15 = _Sts_SigRel2_b15_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 3, 24),
    _Sts_SigRel2_b15_Type()
)
sts_SigRel2_b15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_SigRel2_b15.setStatus("mandatory")


class _Sts_ModeRel2_Type(Integer32):
    """Custom type sts_ModeRel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sts_ModeRel2_Type.__name__ = "Integer32"
_Sts_ModeRel2_Object = MibScalar
sts_ModeRel2 = _Sts_ModeRel2_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 3, 25),
    _Sts_ModeRel2_Type()
)
sts_ModeRel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_ModeRel2.setStatus("mandatory")


class _Sts_DelayRel2_Type(Integer32):
    """Custom type sts_DelayRel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Sts_DelayRel2_Type.__name__ = "Integer32"
_Sts_DelayRel2_Object = MibScalar
sts_DelayRel2 = _Sts_DelayRel2_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 3, 26),
    _Sts_DelayRel2_Type()
)
sts_DelayRel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts_DelayRel2.setStatus("mandatory")


class _Sts_OverTemp_Type(Integer32):
    """Custom type sts_OverTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(358, 358),
    )


_Sts_OverTemp_Type.__name__ = "Integer32"
_Sts_OverTemp_Object = MibScalar
sts_OverTemp = _Sts_OverTemp_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 2, 2, 3, 27),
    _Sts_OverTemp_Type()
)
sts_OverTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts_OverTemp.setStatus("mandatory")
_ExtendedSettings_ObjectIdentity = ObjectIdentity
extendedSettings = _ExtendedSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16460, 4, 3)
)
_NetSyncronisationSet_ObjectIdentity = ObjectIdentity
netSyncronisationSet = _NetSyncronisationSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16460, 4, 3, 1)
)


class _Net_EdgeDetectionDelay_Type(Integer32):
    """Custom type net_EdgeDetectionDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_Net_EdgeDetectionDelay_Type.__name__ = "Integer32"
_Net_EdgeDetectionDelay_Object = MibScalar
net_EdgeDetectionDelay = _Net_EdgeDetectionDelay_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 3, 1, 1),
    _Net_EdgeDetectionDelay_Type()
)
net_EdgeDetectionDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    net_EdgeDetectionDelay.setStatus("mandatory")


class _Net_TimeOutDelay_Type(Integer32):
    """Custom type net_TimeOutDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_Net_TimeOutDelay_Type.__name__ = "Integer32"
_Net_TimeOutDelay_Object = MibScalar
net_TimeOutDelay = _Net_TimeOutDelay_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 3, 1, 2),
    _Net_TimeOutDelay_Type()
)
net_TimeOutDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    net_TimeOutDelay.setStatus("mandatory")


class _Net_MaxCorrPhi_Type(Integer32):
    """Custom type net_MaxCorrPhi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Net_MaxCorrPhi_Type.__name__ = "Integer32"
_Net_MaxCorrPhi_Object = MibScalar
net_MaxCorrPhi = _Net_MaxCorrPhi_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 3, 1, 3),
    _Net_MaxCorrPhi_Type()
)
net_MaxCorrPhi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    net_MaxCorrPhi.setStatus("mandatory")


class _Net_DivDeltaPhi_Type(Integer32):
    """Custom type net_DivDeltaPhi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Net_DivDeltaPhi_Type.__name__ = "Integer32"
_Net_DivDeltaPhi_Object = MibScalar
net_DivDeltaPhi = _Net_DivDeltaPhi_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 3, 1, 4),
    _Net_DivDeltaPhi_Type()
)
net_DivDeltaPhi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    net_DivDeltaPhi.setStatus("mandatory")


class _Net_DivCorrPhi_I_Type(Integer32):
    """Custom type net_DivCorrPhi_I based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Net_DivCorrPhi_I_Type.__name__ = "Integer32"
_Net_DivCorrPhi_I_Object = MibScalar
net_DivCorrPhi_I = _Net_DivCorrPhi_I_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 3, 1, 5),
    _Net_DivCorrPhi_I_Type()
)
net_DivCorrPhi_I.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    net_DivCorrPhi_I.setStatus("mandatory")


class _Net_MaxCorrT_Type(Integer32):
    """Custom type net_MaxCorrT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Net_MaxCorrT_Type.__name__ = "Integer32"
_Net_MaxCorrT_Object = MibScalar
net_MaxCorrT = _Net_MaxCorrT_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 3, 1, 6),
    _Net_MaxCorrT_Type()
)
net_MaxCorrT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    net_MaxCorrT.setStatus("mandatory")


class _Net_DivDeltaT_Type(Integer32):
    """Custom type net_DivDeltaT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Net_DivDeltaT_Type.__name__ = "Integer32"
_Net_DivDeltaT_Object = MibScalar
net_DivDeltaT = _Net_DivDeltaT_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 3, 1, 7),
    _Net_DivDeltaT_Type()
)
net_DivDeltaT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    net_DivDeltaT.setStatus("mandatory")


class _Net_SyncOKNr_Type(Integer32):
    """Custom type net_SyncOKNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Net_SyncOKNr_Type.__name__ = "Integer32"
_Net_SyncOKNr_Object = MibScalar
net_SyncOKNr = _Net_SyncOKNr_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 3, 1, 8),
    _Net_SyncOKNr_Type()
)
net_SyncOKNr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    net_SyncOKNr.setStatus("mandatory")


class _Net_SyncErrorNr_Type(Integer32):
    """Custom type net_SyncErrorNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Net_SyncErrorNr_Type.__name__ = "Integer32"
_Net_SyncErrorNr_Object = MibScalar
net_SyncErrorNr = _Net_SyncErrorNr_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 3, 1, 9),
    _Net_SyncErrorNr_Type()
)
net_SyncErrorNr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    net_SyncErrorNr.setStatus("mandatory")


class _Net_P_Diff_Type(Integer32):
    """Custom type net_P_Diff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 15000),
    )


_Net_P_Diff_Type.__name__ = "Integer32"
_Net_P_Diff_Object = MibScalar
net_P_Diff = _Net_P_Diff_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 3, 1, 10),
    _Net_P_Diff_Type()
)
net_P_Diff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    net_P_Diff.setStatus("mandatory")
_AdjustValues_ObjectIdentity = ObjectIdentity
adjustValues = _AdjustValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16460, 4, 3, 2)
)


class _Adj_UMains_Type(Integer32):
    """Custom type adj_UMains based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(368, 432),
    )


_Adj_UMains_Type.__name__ = "Integer32"
_Adj_UMains_Object = MibScalar
adj_UMains = _Adj_UMains_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 3, 2, 1),
    _Adj_UMains_Type()
)
adj_UMains.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adj_UMains.setStatus("mandatory")


class _Adj_UInv_Type(Integer32):
    """Custom type adj_UInv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(368, 432),
    )


_Adj_UInv_Type.__name__ = "Integer32"
_Adj_UInv_Object = MibScalar
adj_UInv = _Adj_UInv_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 3, 2, 2),
    _Adj_UInv_Type()
)
adj_UInv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adj_UInv.setStatus("mandatory")


class _Adj_UDC_Type(Integer32):
    """Custom type adj_UDC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1372, 1628),
    )


_Adj_UDC_Type.__name__ = "Integer32"
_Adj_UDC_Object = MibScalar
adj_UDC = _Adj_UDC_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 3, 2, 3),
    _Adj_UDC_Type()
)
adj_UDC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adj_UDC.setStatus("mandatory")


class _Adj_Uout_Type(Integer32):
    """Custom type adj_Uout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(368, 432),
    )


_Adj_Uout_Type.__name__ = "Integer32"
_Adj_Uout_Object = MibScalar
adj_Uout = _Adj_Uout_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 3, 2, 4),
    _Adj_Uout_Type()
)
adj_Uout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adj_Uout.setStatus("mandatory")


class _Adj_Iout_Type(Integer32):
    """Custom type adj_Iout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1988, 3012),
    )


_Adj_Iout_Type.__name__ = "Integer32"
_Adj_Iout_Object = MibScalar
adj_Iout = _Adj_Iout_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 3, 2, 5),
    _Adj_Iout_Type()
)
adj_Iout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adj_Iout.setStatus("mandatory")
_Tables_ObjectIdentity = ObjectIdentity
tables = _Tables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16460, 4, 4)
)
_HistoryTable_Object = MibTable
historyTable = _HistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 4, 1)
)
if mibBuilder.loadTexts:
    historyTable.setStatus("mandatory")
_HistoryEntry_Object = MibTableRow
historyEntry = _HistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 4, 1, 1)
)
historyEntry.setIndexNames(
    (0, "STS_SEQUENZ-MIB", "histIndex"),
)
if mibBuilder.loadTexts:
    historyEntry.setStatus("optional")


class _HistIndex_Type(Integer32):
    """Custom type histIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_HistIndex_Type.__name__ = "Integer32"
_HistIndex_Object = MibTableColumn
histIndex = _HistIndex_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 4, 1, 1, 0),
    _HistIndex_Type()
)
histIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    histIndex.setStatus("current")
if mibBuilder.loadTexts:
    histIndex.setUnits("NA")


class _HistInd_Type(Integer32):
    """Custom type histInd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HistInd_Type.__name__ = "Integer32"
_HistInd_Object = MibTableColumn
histInd = _HistInd_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 4, 1, 1, 1),
    _HistInd_Type()
)
histInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histInd.setStatus("mandatory")


class _HistDateTime_Type(Integer32):
    """Custom type histDateTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 400000000),
    )


_HistDateTime_Type.__name__ = "Integer32"
_HistDateTime_Object = MibTableColumn
histDateTime = _HistDateTime_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 4, 1, 1, 2),
    _HistDateTime_Type()
)
histDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histDateTime.setStatus("mandatory")


class _HistEvent_Type(Integer32):
    """Custom type histEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HistEvent_Type.__name__ = "Integer32"
_HistEvent_Object = MibTableColumn
histEvent = _HistEvent_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 4, 1, 1, 3),
    _HistEvent_Type()
)
histEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histEvent.setStatus("mandatory")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5)
)
_TrapLastMessageStringTest_Type = OctetString
_TrapLastMessageStringTest_Object = MibScalar
trapLastMessageStringTest = _TrapLastMessageStringTest_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 1),
    _TrapLastMessageStringTest_Type()
)
trapLastMessageStringTest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapLastMessageStringTest.setStatus("mandatory")


class _TrapLastMessageNbrTest_Type(Integer32):
    """Custom type trapLastMessageNbrTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 46),
    )


_TrapLastMessageNbrTest_Type.__name__ = "Integer32"
_TrapLastMessageNbrTest_Object = MibScalar
trapLastMessageNbrTest = _TrapLastMessageNbrTest_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 2),
    _TrapLastMessageNbrTest_Type()
)
trapLastMessageNbrTest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapLastMessageNbrTest.setStatus("mandatory")
_TrapSourceIPTest_Type = IpAddress
_TrapSourceIPTest_Object = MibScalar
trapSourceIPTest = _TrapSourceIPTest_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 3),
    _TrapSourceIPTest_Type()
)
trapSourceIPTest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapSourceIPTest.setStatus("mandatory")


class _Trap_source_mains_failue_present_Type(Integer32):
    """Custom type trap_source_mains_failue_present based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_source_mains_failue_present_Type.__name__ = "Integer32"
_Trap_source_mains_failue_present_Object = MibScalar
trap_source_mains_failue_present = _Trap_source_mains_failue_present_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 17),
    _Trap_source_mains_failue_present_Type()
)
trap_source_mains_failue_present.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_source_mains_failue_present.setStatus("mandatory")


class _Trap_source_inverter_failure_present_Type(Integer32):
    """Custom type trap_source_inverter_failure_present based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_source_inverter_failure_present_Type.__name__ = "Integer32"
_Trap_source_inverter_failure_present_Object = MibScalar
trap_source_inverter_failure_present = _Trap_source_inverter_failure_present_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 18),
    _Trap_source_inverter_failure_present_Type()
)
trap_source_inverter_failure_present.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_source_inverter_failure_present.setStatus("mandatory")


class _Trap_syncronisation_error_present_Type(Integer32):
    """Custom type trap_syncronisation_error_present based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_syncronisation_error_present_Type.__name__ = "Integer32"
_Trap_syncronisation_error_present_Object = MibScalar
trap_syncronisation_error_present = _Trap_syncronisation_error_present_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 19),
    _Trap_syncronisation_error_present_Type()
)
trap_syncronisation_error_present.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_syncronisation_error_present.setStatus("mandatory")


class _Trap_inverter_failure_present_Type(Integer32):
    """Custom type trap_inverter_failure_present based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_inverter_failure_present_Type.__name__ = "Integer32"
_Trap_inverter_failure_present_Object = MibScalar
trap_inverter_failure_present = _Trap_inverter_failure_present_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 20),
    _Trap_inverter_failure_present_Type()
)
trap_inverter_failure_present.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_inverter_failure_present.setStatus("mandatory")


class _Trap_no_redundant_inverter_present_Type(Integer32):
    """Custom type trap_no_redundant_inverter_present based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_no_redundant_inverter_present_Type.__name__ = "Integer32"
_Trap_no_redundant_inverter_present_Object = MibScalar
trap_no_redundant_inverter_present = _Trap_no_redundant_inverter_present_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 21),
    _Trap_no_redundant_inverter_present_Type()
)
trap_no_redundant_inverter_present.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_no_redundant_inverter_present.setStatus("mandatory")


class _Trap_critical_inverter_quantity_present_Type(Integer32):
    """Custom type trap_critical_inverter_quantity_present based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_critical_inverter_quantity_present_Type.__name__ = "Integer32"
_Trap_critical_inverter_quantity_present_Object = MibScalar
trap_critical_inverter_quantity_present = _Trap_critical_inverter_quantity_present_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 22),
    _Trap_critical_inverter_quantity_present_Type()
)
trap_critical_inverter_quantity_present.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_critical_inverter_quantity_present.setStatus("mandatory")


class _Trap_sts_overtemperature_present_Type(Integer32):
    """Custom type trap_sts_overtemperature_present based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_sts_overtemperature_present_Type.__name__ = "Integer32"
_Trap_sts_overtemperature_present_Object = MibScalar
trap_sts_overtemperature_present = _Trap_sts_overtemperature_present_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 23),
    _Trap_sts_overtemperature_present_Type()
)
trap_sts_overtemperature_present.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_sts_overtemperature_present.setStatus("mandatory")


class _Trap_sts_overload_present_Type(Integer32):
    """Custom type trap_sts_overload_present based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_sts_overload_present_Type.__name__ = "Integer32"
_Trap_sts_overload_present_Object = MibScalar
trap_sts_overload_present = _Trap_sts_overload_present_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 24),
    _Trap_sts_overload_present_Type()
)
trap_sts_overload_present.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_sts_overload_present.setStatus("mandatory")


class _Trap_inverter_overload_present_Type(Integer32):
    """Custom type trap_inverter_overload_present based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_inverter_overload_present_Type.__name__ = "Integer32"
_Trap_inverter_overload_present_Object = MibScalar
trap_inverter_overload_present = _Trap_inverter_overload_present_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 25),
    _Trap_inverter_overload_present_Type()
)
trap_inverter_overload_present.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_inverter_overload_present.setStatus("mandatory")


class _Trap_sts_current_need_redandancy_present_Type(Integer32):
    """Custom type trap_sts_current_need_redandancy_present based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_sts_current_need_redandancy_present_Type.__name__ = "Integer32"
_Trap_sts_current_need_redandancy_present_Object = MibScalar
trap_sts_current_need_redandancy_present = _Trap_sts_current_need_redandancy_present_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 26),
    _Trap_sts_current_need_redandancy_present_Type()
)
trap_sts_current_need_redandancy_present.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_sts_current_need_redandancy_present.setStatus("mandatory")


class _Trap_dc_voltage_low_present_Type(Integer32):
    """Custom type trap_dc_voltage_low_present based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_dc_voltage_low_present_Type.__name__ = "Integer32"
_Trap_dc_voltage_low_present_Object = MibScalar
trap_dc_voltage_low_present = _Trap_dc_voltage_low_present_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 27),
    _Trap_dc_voltage_low_present_Type()
)
trap_dc_voltage_low_present.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_dc_voltage_low_present.setStatus("mandatory")


class _Trap_dc_voltage_high_present_Type(Integer32):
    """Custom type trap_dc_voltage_high_present based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_dc_voltage_high_present_Type.__name__ = "Integer32"
_Trap_dc_voltage_high_present_Object = MibScalar
trap_dc_voltage_high_present = _Trap_dc_voltage_high_present_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 28),
    _Trap_dc_voltage_high_present_Type()
)
trap_dc_voltage_high_present.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_dc_voltage_high_present.setStatus("mandatory")


class _Trap_fan_error_present_Type(Integer32):
    """Custom type trap_fan_error_present based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_fan_error_present_Type.__name__ = "Integer32"
_Trap_fan_error_present_Object = MibScalar
trap_fan_error_present = _Trap_fan_error_present_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 29),
    _Trap_fan_error_present_Type()
)
trap_fan_error_present.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_fan_error_present.setStatus("mandatory")


class _Trap_uout_low_present_Type(Integer32):
    """Custom type trap_uout_low_present based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_uout_low_present_Type.__name__ = "Integer32"
_Trap_uout_low_present_Object = MibScalar
trap_uout_low_present = _Trap_uout_low_present_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 30),
    _Trap_uout_low_present_Type()
)
trap_uout_low_present.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_uout_low_present.setStatus("mandatory")


class _Trap_u_batterie_lower_warning_present_Type(Integer32):
    """Custom type trap_u_batterie_lower_warning_present based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_u_batterie_lower_warning_present_Type.__name__ = "Integer32"
_Trap_u_batterie_lower_warning_present_Object = MibScalar
trap_u_batterie_lower_warning_present = _Trap_u_batterie_lower_warning_present_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 31),
    _Trap_u_batterie_lower_warning_present_Type()
)
trap_u_batterie_lower_warning_present.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_u_batterie_lower_warning_present.setStatus("mandatory")


class _Trap_u_batterie_higher_warning_present_Type(Integer32):
    """Custom type trap_u_batterie_higher_warning_present based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_u_batterie_higher_warning_present_Type.__name__ = "Integer32"
_Trap_u_batterie_higher_warning_present_Object = MibScalar
trap_u_batterie_higher_warning_present = _Trap_u_batterie_higher_warning_present_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 32),
    _Trap_u_batterie_higher_warning_present_Type()
)
trap_u_batterie_higher_warning_present.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_u_batterie_higher_warning_present.setStatus("mandatory")


class _Trap_source_mains_failure_removed_Type(Integer32):
    """Custom type trap_source_mains_failure_removed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_source_mains_failure_removed_Type.__name__ = "Integer32"
_Trap_source_mains_failure_removed_Object = MibScalar
trap_source_mains_failure_removed = _Trap_source_mains_failure_removed_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 33),
    _Trap_source_mains_failure_removed_Type()
)
trap_source_mains_failure_removed.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_source_mains_failure_removed.setStatus("mandatory")


class _Trap_source_inverter_failure_removed_Type(Integer32):
    """Custom type trap_source_inverter_failure_removed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_source_inverter_failure_removed_Type.__name__ = "Integer32"
_Trap_source_inverter_failure_removed_Object = MibScalar
trap_source_inverter_failure_removed = _Trap_source_inverter_failure_removed_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 34),
    _Trap_source_inverter_failure_removed_Type()
)
trap_source_inverter_failure_removed.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_source_inverter_failure_removed.setStatus("mandatory")


class _Trap_syncronisation_error_removed_Type(Integer32):
    """Custom type trap_syncronisation_error_removed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_syncronisation_error_removed_Type.__name__ = "Integer32"
_Trap_syncronisation_error_removed_Object = MibScalar
trap_syncronisation_error_removed = _Trap_syncronisation_error_removed_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 35),
    _Trap_syncronisation_error_removed_Type()
)
trap_syncronisation_error_removed.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_syncronisation_error_removed.setStatus("mandatory")


class _Trap_inverter_failure_removed_Type(Integer32):
    """Custom type trap_inverter_failure_removed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_inverter_failure_removed_Type.__name__ = "Integer32"
_Trap_inverter_failure_removed_Object = MibScalar
trap_inverter_failure_removed = _Trap_inverter_failure_removed_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 36),
    _Trap_inverter_failure_removed_Type()
)
trap_inverter_failure_removed.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_inverter_failure_removed.setStatus("mandatory")


class _Trap_no_redundant_inverter_removed_Type(Integer32):
    """Custom type trap_no_redundant_inverter_removed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_no_redundant_inverter_removed_Type.__name__ = "Integer32"
_Trap_no_redundant_inverter_removed_Object = MibScalar
trap_no_redundant_inverter_removed = _Trap_no_redundant_inverter_removed_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 37),
    _Trap_no_redundant_inverter_removed_Type()
)
trap_no_redundant_inverter_removed.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_no_redundant_inverter_removed.setStatus("mandatory")


class _Trap_critical_inverter_quantity_removed_Type(Integer32):
    """Custom type trap_critical_inverter_quantity_removed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_critical_inverter_quantity_removed_Type.__name__ = "Integer32"
_Trap_critical_inverter_quantity_removed_Object = MibScalar
trap_critical_inverter_quantity_removed = _Trap_critical_inverter_quantity_removed_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 38),
    _Trap_critical_inverter_quantity_removed_Type()
)
trap_critical_inverter_quantity_removed.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_critical_inverter_quantity_removed.setStatus("mandatory")


class _Trap_sts_overtemperature_removed_Type(Integer32):
    """Custom type trap_sts_overtemperature_removed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_sts_overtemperature_removed_Type.__name__ = "Integer32"
_Trap_sts_overtemperature_removed_Object = MibScalar
trap_sts_overtemperature_removed = _Trap_sts_overtemperature_removed_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 39),
    _Trap_sts_overtemperature_removed_Type()
)
trap_sts_overtemperature_removed.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_sts_overtemperature_removed.setStatus("mandatory")


class _Trap_sts_overload_removed_Type(Integer32):
    """Custom type trap_sts_overload_removed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_sts_overload_removed_Type.__name__ = "Integer32"
_Trap_sts_overload_removed_Object = MibScalar
trap_sts_overload_removed = _Trap_sts_overload_removed_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 40),
    _Trap_sts_overload_removed_Type()
)
trap_sts_overload_removed.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_sts_overload_removed.setStatus("mandatory")


class _Trap_inverter_overload_removed_Type(Integer32):
    """Custom type trap_inverter_overload_removed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_inverter_overload_removed_Type.__name__ = "Integer32"
_Trap_inverter_overload_removed_Object = MibScalar
trap_inverter_overload_removed = _Trap_inverter_overload_removed_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 41),
    _Trap_inverter_overload_removed_Type()
)
trap_inverter_overload_removed.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_inverter_overload_removed.setStatus("mandatory")


class _Trap_sts_current_need_redandancy_removed_Type(Integer32):
    """Custom type trap_sts_current_need_redandancy_removed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_sts_current_need_redandancy_removed_Type.__name__ = "Integer32"
_Trap_sts_current_need_redandancy_removed_Object = MibScalar
trap_sts_current_need_redandancy_removed = _Trap_sts_current_need_redandancy_removed_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 42),
    _Trap_sts_current_need_redandancy_removed_Type()
)
trap_sts_current_need_redandancy_removed.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_sts_current_need_redandancy_removed.setStatus("mandatory")


class _Trap_dc_voltage_low_removed_Type(Integer32):
    """Custom type trap_dc_voltage_low_removed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_dc_voltage_low_removed_Type.__name__ = "Integer32"
_Trap_dc_voltage_low_removed_Object = MibScalar
trap_dc_voltage_low_removed = _Trap_dc_voltage_low_removed_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 43),
    _Trap_dc_voltage_low_removed_Type()
)
trap_dc_voltage_low_removed.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_dc_voltage_low_removed.setStatus("mandatory")


class _Trap_dc_voltage_high_added_removed_Type(Integer32):
    """Custom type trap_dc_voltage_high_added_removed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_dc_voltage_high_added_removed_Type.__name__ = "Integer32"
_Trap_dc_voltage_high_added_removed_Object = MibScalar
trap_dc_voltage_high_added_removed = _Trap_dc_voltage_high_added_removed_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 44),
    _Trap_dc_voltage_high_added_removed_Type()
)
trap_dc_voltage_high_added_removed.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_dc_voltage_high_added_removed.setStatus("mandatory")


class _Trap_fan_error_removed_Type(Integer32):
    """Custom type trap_fan_error_removed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_fan_error_removed_Type.__name__ = "Integer32"
_Trap_fan_error_removed_Object = MibScalar
trap_fan_error_removed = _Trap_fan_error_removed_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 45),
    _Trap_fan_error_removed_Type()
)
trap_fan_error_removed.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_fan_error_removed.setStatus("mandatory")


class _Trap_uout_low_removed_Type(Integer32):
    """Custom type trap_uout_low_removed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_uout_low_removed_Type.__name__ = "Integer32"
_Trap_uout_low_removed_Object = MibScalar
trap_uout_low_removed = _Trap_uout_low_removed_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 46),
    _Trap_uout_low_removed_Type()
)
trap_uout_low_removed.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_uout_low_removed.setStatus("mandatory")


class _Trap_u_batterie_lower_warning_removed_Type(Integer32):
    """Custom type trap_u_batterie_lower_warning_removed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_u_batterie_lower_warning_removed_Type.__name__ = "Integer32"
_Trap_u_batterie_lower_warning_removed_Object = MibScalar
trap_u_batterie_lower_warning_removed = _Trap_u_batterie_lower_warning_removed_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 47),
    _Trap_u_batterie_lower_warning_removed_Type()
)
trap_u_batterie_lower_warning_removed.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_u_batterie_lower_warning_removed.setStatus("mandatory")


class _Trap_u_batterie_higher_warning_removed_Type(Integer32):
    """Custom type trap_u_batterie_higher_warning_removed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Trap_u_batterie_higher_warning_removed_Type.__name__ = "Integer32"
_Trap_u_batterie_higher_warning_removed_Object = MibScalar
trap_u_batterie_higher_warning_removed = _Trap_u_batterie_higher_warning_removed_Object(
    (1, 3, 6, 1, 4, 1, 16460, 4, 5, 48),
    _Trap_u_batterie_higher_warning_removed_Type()
)
trap_u_batterie_higher_warning_removed.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_u_batterie_higher_warning_removed.setStatus("mandatory")

# Managed Objects groups


# Notification objects

source_mains_failue_present_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 16)
)
source_mains_failue_present_trap.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_source_mains_failue_present"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    source_mains_failue_present_trap.setStatus(
        ""
    )

source_inverter_failure_present = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 17)
)
source_inverter_failure_present.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_source_inverter_failure_present"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    source_inverter_failure_present.setStatus(
        ""
    )

syncronisation_error_present = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 18)
)
syncronisation_error_present.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_syncronisation_error_present"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    syncronisation_error_present.setStatus(
        ""
    )

inverter_failure_present = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 19)
)
inverter_failure_present.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_inverter_failure_present"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    inverter_failure_present.setStatus(
        ""
    )

no_redundant_inverter_present = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 20)
)
no_redundant_inverter_present.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_no_redundant_inverter_present"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    no_redundant_inverter_present.setStatus(
        ""
    )

critical_inverter_quantity_present = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 21)
)
critical_inverter_quantity_present.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_critical_inverter_quantity_present"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    critical_inverter_quantity_present.setStatus(
        ""
    )

sts_overtemperature_present = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 22)
)
sts_overtemperature_present.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_sts_overtemperature_present"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    sts_overtemperature_present.setStatus(
        ""
    )

sts_overload_present = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 23)
)
sts_overload_present.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_sts_overload_present"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    sts_overload_present.setStatus(
        ""
    )

inverter_overload_present = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 24)
)
inverter_overload_present.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_inverter_overload_present"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    inverter_overload_present.setStatus(
        ""
    )

sts_current_need_redandancy_present = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 25)
)
sts_current_need_redandancy_present.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_sts_current_need_redandancy_present"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    sts_current_need_redandancy_present.setStatus(
        ""
    )

dc_voltage_low_present = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 26)
)
dc_voltage_low_present.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_dc_voltage_low_present"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    dc_voltage_low_present.setStatus(
        ""
    )

dc_voltage_high_present = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 27)
)
dc_voltage_high_present.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_dc_voltage_high_present"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    dc_voltage_high_present.setStatus(
        ""
    )

fan_error_present = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 28)
)
fan_error_present.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_fan_error_present"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    fan_error_present.setStatus(
        ""
    )

uout_low_present = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 29)
)
uout_low_present.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_uout_low_present"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    uout_low_present.setStatus(
        ""
    )

u_batterie_lower_warning_present = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 30)
)
u_batterie_lower_warning_present.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_u_batterie_lower_warning_present"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    u_batterie_lower_warning_present.setStatus(
        ""
    )

u_batterie_higher_warning_present = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 31)
)
u_batterie_higher_warning_present.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_u_batterie_higher_warning_present"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    u_batterie_higher_warning_present.setStatus(
        ""
    )

source_mains_failure_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 32)
)
source_mains_failure_removed.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_source_mains_failure_removed"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    source_mains_failure_removed.setStatus(
        ""
    )

source_inverter_failure_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 33)
)
source_inverter_failure_removed.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_source_inverter_failure_removed"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    source_inverter_failure_removed.setStatus(
        ""
    )

syncronisation_error_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 34)
)
syncronisation_error_removed.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_syncronisation_error_removed"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    syncronisation_error_removed.setStatus(
        ""
    )

inverter_failure_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 35)
)
inverter_failure_removed.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_inverter_failure_removed"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    inverter_failure_removed.setStatus(
        ""
    )

no_redundant_inverter_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 36)
)
no_redundant_inverter_removed.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_no_redundant_inverter_removed"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    no_redundant_inverter_removed.setStatus(
        ""
    )

critical_inverter_quantity_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 37)
)
critical_inverter_quantity_removed.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_critical_inverter_quantity_removed"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    critical_inverter_quantity_removed.setStatus(
        ""
    )

sts_overtemperature_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 38)
)
sts_overtemperature_removed.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_sts_overtemperature_removed"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    sts_overtemperature_removed.setStatus(
        ""
    )

sts_overload_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 39)
)
sts_overload_removed.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_sts_overload_removed"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    sts_overload_removed.setStatus(
        ""
    )

inverter_overload_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 40)
)
inverter_overload_removed.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_inverter_overload_removed"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    inverter_overload_removed.setStatus(
        ""
    )

sts_current_need_redandancy_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 41)
)
sts_current_need_redandancy_removed.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_sts_current_need_redandancy_removed"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    sts_current_need_redandancy_removed.setStatus(
        ""
    )

dc_voltage_low_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 42)
)
dc_voltage_low_removed.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_dc_voltage_low_removed"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    dc_voltage_low_removed.setStatus(
        ""
    )

dc_voltage_high_added_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 43)
)
dc_voltage_high_added_removed.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_dc_voltage_high_added_removed"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    dc_voltage_high_added_removed.setStatus(
        ""
    )

fan_error_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 44)
)
fan_error_removed.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_fan_error_removed"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    fan_error_removed.setStatus(
        ""
    )

uout_low_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 45)
)
uout_low_removed.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_uout_low_removed"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    uout_low_removed.setStatus(
        ""
    )

u_batterie_lower_warning_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 46)
)
u_batterie_lower_warning_removed.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_u_batterie_lower_warning_removed"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    u_batterie_lower_warning_removed.setStatus(
        ""
    )

u_batterie_higher_warning_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 16460, 0, 47)
)
u_batterie_higher_warning_removed.setObjects(
      *(("STS_SEQUENZ-MIB", "trap_u_batterie_higher_warning_removed"),
        ("STS_SEQUENZ-MIB", "trapLastMessageStringTest"),
        ("STS_SEQUENZ-MIB", "trapLastMessageNbrTest"),
        ("STS_SEQUENZ-MIB", "trapSourceIPTest"))
)
if mibBuilder.loadTexts:
    u_batterie_higher_warning_removed.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STS_SEQUENZ-MIB",
    **{"convertronic": convertronic,
       "source_mains_failue_present_trap": source_mains_failue_present_trap,
       "source_inverter_failure_present": source_inverter_failure_present,
       "syncronisation_error_present": syncronisation_error_present,
       "inverter_failure_present": inverter_failure_present,
       "no_redundant_inverter_present": no_redundant_inverter_present,
       "critical_inverter_quantity_present": critical_inverter_quantity_present,
       "sts_overtemperature_present": sts_overtemperature_present,
       "sts_overload_present": sts_overload_present,
       "inverter_overload_present": inverter_overload_present,
       "sts_current_need_redandancy_present": sts_current_need_redandancy_present,
       "dc_voltage_low_present": dc_voltage_low_present,
       "dc_voltage_high_present": dc_voltage_high_present,
       "fan_error_present": fan_error_present,
       "uout_low_present": uout_low_present,
       "u_batterie_lower_warning_present": u_batterie_lower_warning_present,
       "u_batterie_higher_warning_present": u_batterie_higher_warning_present,
       "source_mains_failure_removed": source_mains_failure_removed,
       "source_inverter_failure_removed": source_inverter_failure_removed,
       "syncronisation_error_removed": syncronisation_error_removed,
       "inverter_failure_removed": inverter_failure_removed,
       "no_redundant_inverter_removed": no_redundant_inverter_removed,
       "critical_inverter_quantity_removed": critical_inverter_quantity_removed,
       "sts_overtemperature_removed": sts_overtemperature_removed,
       "sts_overload_removed": sts_overload_removed,
       "inverter_overload_removed": inverter_overload_removed,
       "sts_current_need_redandancy_removed": sts_current_need_redandancy_removed,
       "dc_voltage_low_removed": dc_voltage_low_removed,
       "dc_voltage_high_added_removed": dc_voltage_high_added_removed,
       "fan_error_removed": fan_error_removed,
       "uout_low_removed": uout_low_removed,
       "u_batterie_lower_warning_removed": u_batterie_lower_warning_removed,
       "u_batterie_higher_warning_removed": u_batterie_higher_warning_removed,
       "sts_system": sts_system,
       "measureValues": measureValues,
       "sts_measureValues": sts_measureValues,
       "sVal_UN": sVal_UN,
       "sVal_FreqNetz": sVal_FreqNetz,
       "sVal_UWR": sVal_UWR,
       "sVal_FreqWR": sVal_FreqWR,
       "sVal_UDC": sVal_UDC,
       "sVal_U10": sVal_U10,
       "sVal_IO1": sVal_IO1,
       "sVal_P": sVal_P,
       "sVal_S": sVal_S,
       "sVal_FAN1": sVal_FAN1,
       "sVal_FAN2": sVal_FAN2,
       "sVal_TK": sVal_TK,
       "sVal_IO2": sVal_IO2,
       "sVal_IDC": sVal_IDC,
       "inverter_measureValues": inverter_measureValues,
       "inverter_Table": inverter_Table,
       "inverter_Entry": inverter_Entry,
       "inv_Index": inv_Index,
       "inv_Nbr": inv_Nbr,
       "inv_InCurrent": inv_InCurrent,
       "inv_OutCurrent": inv_OutCurrent,
       "inv_Temperature": inv_Temperature,
       "inv_InputVoltage": inv_InputVoltage,
       "inv_STi_great": inv_STi_great,
       "inv_Fan": inv_Fan,
       "inv_RemoteOffCan": inv_RemoteOffCan,
       "inv_UoutOff": inv_UoutOff,
       "inv_Bit_ShortCircuit": inv_Bit_ShortCircuit,
       "inv_Bit_OutputVoltage": inv_Bit_OutputVoltage,
       "inv_Bit_InputVoltLow": inv_Bit_InputVoltLow,
       "inv_Bit_InputVoltHigh": inv_Bit_InputVoltHigh,
       "inv_Bit_OutputVoltLow": inv_Bit_OutputVoltLow,
       "inv_Bit_OutputVoltHigh": inv_Bit_OutputVoltHigh,
       "inv_Bit_OutputCurrHigh": inv_Bit_OutputCurrHigh,
       "inv_Bit_RemoteOff": inv_Bit_RemoteOff,
       "inv_Bit_CentralAlarm": inv_Bit_CentralAlarm,
       "inv_Type": inv_Type,
       "inv_Mat_CD": inv_Mat_CD,
       "inv_SerialNo": inv_SerialNo,
       "inv_HardwareVersion": inv_HardwareVersion,
       "inv_SoftwareVersion": inv_SoftwareVersion,
       "settings": settings,
       "networkSettings": networkSettings,
       "baseSettings": baseSettings,
       "bETHSpeed": bETHSpeed,
       "bLocalIP": bLocalIP,
       "bSubnetMask": bSubnetMask,
       "bGateway": bGateway,
       "bDNSServer": bDNSServer,
       "bDHCPServer": bDHCPServer,
       "bFixedIP_OnOff": bFixedIP_OnOff,
       "bDefaultIP_OnOff": bDefaultIP_OnOff,
       "bDHCP_OnOff": bDHCP_OnOff,
       "bBOOTP_OnOff": bBOOTP_OnOff,
       "bLocation": bLocation,
       "serviceSettings": serviceSettings,
       "servSNMP_OnOff": servSNMP_OnOff,
       "servTrapReceiver1": servTrapReceiver1,
       "servTrapReceiver2": servTrapReceiver2,
       "servTrapReceiver3": servTrapReceiver3,
       "servTrapReceiver4": servTrapReceiver4,
       "servReadCommunity": servReadCommunity,
       "servWriteCommunity": servWriteCommunity,
       "servSMTP_OnOff": servSMTP_OnOff,
       "servMailServer": servMailServer,
       "servMailUsername": servMailUsername,
       "servMailPassword": servMailPassword,
       "servMailReceiver1": servMailReceiver1,
       "servMailTrapLevel1": servMailTrapLevel1,
       "servMailReceiver2": servMailReceiver2,
       "servMailTrapLevel2": servMailTrapLevel2,
       "servSNTP_OnOff": servSNTP_OnOff,
       "servSNTPServer1": servSNTPServer1,
       "servSNTPServer2": servSNTPServer2,
       "servTelnet_OnOff": servTelnet_OnOff,
       "servSyslog_OnOff": servSyslog_OnOff,
       "unitSettings": unitSettings,
       "basicSettings": basicSettings,
       "sts_Version": sts_Version,
       "sts_Inverter": sts_Inverter,
       "sts_SigCF_b0": sts_SigCF_b0,
       "sts_SigCF_b1": sts_SigCF_b1,
       "sts_SigCF_b2": sts_SigCF_b2,
       "sts_SigCF_b3": sts_SigCF_b3,
       "sts_SigCF_b4": sts_SigCF_b4,
       "sts_SigCF_b5": sts_SigCF_b5,
       "sts_SigCF_b6": sts_SigCF_b6,
       "sts_SigCF_b7": sts_SigCF_b7,
       "sts_SigCF_b8": sts_SigCF_b8,
       "sts_SigCF_b9": sts_SigCF_b9,
       "sts_SigCF_b10": sts_SigCF_b10,
       "sts_SigCF_b11": sts_SigCF_b11,
       "sts_SigCF_b12": sts_SigCF_b12,
       "sts_SigCF_b13": sts_SigCF_b13,
       "sts_SigCF_b14": sts_SigCF_b14,
       "sts_SigCF_b15": sts_SigCF_b15,
       "sts_DelayRelCA": sts_DelayRelCA,
       "sts_DelayLEDCA": sts_DelayLEDCA,
       "sts_LCDContrast": sts_LCDContrast,
       "sts_Language": sts_Language,
       "advancedSettings": advancedSettings,
       "sts_OpMode": sts_OpMode,
       "sts_UpperSwitchLimS1": sts_UpperSwitchLimS1,
       "sts_LowerSwitchLimS1": sts_LowerSwitchLimS1,
       "sts_SwitchDelayS1": sts_SwitchDelayS1,
       "sts_UpperSwitchLimS2": sts_UpperSwitchLimS2,
       "sts_LowerSwitchLimS2": sts_LowerSwitchLimS2,
       "sts_SwitchDelayS2": sts_SwitchDelayS2,
       "sts_MaxCellVolt1": sts_MaxCellVolt1,
       "sts_MinCellVolt1": sts_MinCellVolt1,
       "sts_MinCellVolt2": sts_MinCellVolt2,
       "sts_MinULimit": sts_MinULimit,
       "sts_MaxULimit": sts_MaxULimit,
       "advancedSettings2": advancedSettings2,
       "sts_NomPower": sts_NomPower,
       "sts_NomVolt": sts_NomVolt,
       "sts_NomFreq": sts_NomFreq,
       "sts_FreqRange": sts_FreqRange,
       "sts_MaxCurrent": sts_MaxCurrent,
       "sts_PresentCell": sts_PresentCell,
       "sts_CellVoltage": sts_CellVoltage,
       "sts_Adress": sts_Adress,
       "sts_SigRel2_b0": sts_SigRel2_b0,
       "sts_SigRel2_b1": sts_SigRel2_b1,
       "sts_SigRel2_b2": sts_SigRel2_b2,
       "sts_SigRel2_b3": sts_SigRel2_b3,
       "sts_SigRel2_b4": sts_SigRel2_b4,
       "sts_SigRel2_b5": sts_SigRel2_b5,
       "sts_SigRel2_b6": sts_SigRel2_b6,
       "sts_SigRel2_b7": sts_SigRel2_b7,
       "sts_SigRel2_b8": sts_SigRel2_b8,
       "sts_SigRel2_b9": sts_SigRel2_b9,
       "sts_SigRel2_b10": sts_SigRel2_b10,
       "sts_SigRel2_b11": sts_SigRel2_b11,
       "sts_SigRel2_b12": sts_SigRel2_b12,
       "sts_SigRel2_b13": sts_SigRel2_b13,
       "sts_SigRel2_b14": sts_SigRel2_b14,
       "sts_SigRel2_b15": sts_SigRel2_b15,
       "sts_ModeRel2": sts_ModeRel2,
       "sts_DelayRel2": sts_DelayRel2,
       "sts_OverTemp": sts_OverTemp,
       "extendedSettings": extendedSettings,
       "netSyncronisationSet": netSyncronisationSet,
       "net_EdgeDetectionDelay": net_EdgeDetectionDelay,
       "net_TimeOutDelay": net_TimeOutDelay,
       "net_MaxCorrPhi": net_MaxCorrPhi,
       "net_DivDeltaPhi": net_DivDeltaPhi,
       "net_DivCorrPhi_I": net_DivCorrPhi_I,
       "net_MaxCorrT": net_MaxCorrT,
       "net_DivDeltaT": net_DivDeltaT,
       "net_SyncOKNr": net_SyncOKNr,
       "net_SyncErrorNr": net_SyncErrorNr,
       "net_P_Diff": net_P_Diff,
       "adjustValues": adjustValues,
       "adj_UMains": adj_UMains,
       "adj_UInv": adj_UInv,
       "adj_UDC": adj_UDC,
       "adj_Uout": adj_Uout,
       "adj_Iout": adj_Iout,
       "tables": tables,
       "historyTable": historyTable,
       "historyEntry": historyEntry,
       "histIndex": histIndex,
       "histInd": histInd,
       "histDateTime": histDateTime,
       "histEvent": histEvent,
       "traps": traps,
       "trapLastMessageStringTest": trapLastMessageStringTest,
       "trapLastMessageNbrTest": trapLastMessageNbrTest,
       "trapSourceIPTest": trapSourceIPTest,
       "trap_source_mains_failue_present": trap_source_mains_failue_present,
       "trap_source_inverter_failure_present": trap_source_inverter_failure_present,
       "trap_syncronisation_error_present": trap_syncronisation_error_present,
       "trap_inverter_failure_present": trap_inverter_failure_present,
       "trap_no_redundant_inverter_present": trap_no_redundant_inverter_present,
       "trap_critical_inverter_quantity_present": trap_critical_inverter_quantity_present,
       "trap_sts_overtemperature_present": trap_sts_overtemperature_present,
       "trap_sts_overload_present": trap_sts_overload_present,
       "trap_inverter_overload_present": trap_inverter_overload_present,
       "trap_sts_current_need_redandancy_present": trap_sts_current_need_redandancy_present,
       "trap_dc_voltage_low_present": trap_dc_voltage_low_present,
       "trap_dc_voltage_high_present": trap_dc_voltage_high_present,
       "trap_fan_error_present": trap_fan_error_present,
       "trap_uout_low_present": trap_uout_low_present,
       "trap_u_batterie_lower_warning_present": trap_u_batterie_lower_warning_present,
       "trap_u_batterie_higher_warning_present": trap_u_batterie_higher_warning_present,
       "trap_source_mains_failure_removed": trap_source_mains_failure_removed,
       "trap_source_inverter_failure_removed": trap_source_inverter_failure_removed,
       "trap_syncronisation_error_removed": trap_syncronisation_error_removed,
       "trap_inverter_failure_removed": trap_inverter_failure_removed,
       "trap_no_redundant_inverter_removed": trap_no_redundant_inverter_removed,
       "trap_critical_inverter_quantity_removed": trap_critical_inverter_quantity_removed,
       "trap_sts_overtemperature_removed": trap_sts_overtemperature_removed,
       "trap_sts_overload_removed": trap_sts_overload_removed,
       "trap_inverter_overload_removed": trap_inverter_overload_removed,
       "trap_sts_current_need_redandancy_removed": trap_sts_current_need_redandancy_removed,
       "trap_dc_voltage_low_removed": trap_dc_voltage_low_removed,
       "trap_dc_voltage_high_added_removed": trap_dc_voltage_high_added_removed,
       "trap_fan_error_removed": trap_fan_error_removed,
       "trap_uout_low_removed": trap_uout_low_removed,
       "trap_u_batterie_lower_warning_removed": trap_u_batterie_lower_warning_removed,
       "trap_u_batterie_higher_warning_removed": trap_u_batterie_higher_warning_removed}
)
