# SNMP MIB module (HPNSASINFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPNSASINFO-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:36:46 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Hpnsa_ObjectIdentity = ObjectIdentity
hpnsa = _Hpnsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23)
)
_HpnsaSystemInfo_ObjectIdentity = ObjectIdentity
hpnsaSystemInfo = _HpnsaSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7)
)
_HpnsaSiMibRev_ObjectIdentity = ObjectIdentity
hpnsaSiMibRev = _HpnsaSiMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 1)
)


class _HpnsaSiMibRevMajor_Type(Integer32):
    """Custom type hpnsaSiMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnsaSiMibRevMajor_Type.__name__ = "Integer32"
_HpnsaSiMibRevMajor_Object = MibScalar
hpnsaSiMibRevMajor = _HpnsaSiMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 1, 1),
    _HpnsaSiMibRevMajor_Type()
)
hpnsaSiMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiMibRevMajor.setStatus("mandatory")


class _HpnsaSiMibRevMinor_Type(Integer32):
    """Custom type hpnsaSiMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaSiMibRevMinor_Type.__name__ = "Integer32"
_HpnsaSiMibRevMinor_Object = MibScalar
hpnsaSiMibRevMinor = _HpnsaSiMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 1, 2),
    _HpnsaSiMibRevMinor_Type()
)
hpnsaSiMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiMibRevMinor.setStatus("mandatory")
_HpnsaSiAgent_ObjectIdentity = ObjectIdentity
hpnsaSiAgent = _HpnsaSiAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 2)
)
_HpnsaSiAgentTable_Object = MibTable
hpnsaSiAgentTable = _HpnsaSiAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 2, 1)
)
if mibBuilder.loadTexts:
    hpnsaSiAgentTable.setStatus("mandatory")
_HpnsaSiAgentEntry_Object = MibTableRow
hpnsaSiAgentEntry = _HpnsaSiAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 2, 1, 1)
)
hpnsaSiAgentEntry.setIndexNames(
    (0, "HPNSASINFO-MIB", "hpnsaSiAgentIndex"),
)
if mibBuilder.loadTexts:
    hpnsaSiAgentEntry.setStatus("mandatory")


class _HpnsaSiAgentIndex_Type(Integer32):
    """Custom type hpnsaSiAgentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaSiAgentIndex_Type.__name__ = "Integer32"
_HpnsaSiAgentIndex_Object = MibTableColumn
hpnsaSiAgentIndex = _HpnsaSiAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 2, 1, 1, 1),
    _HpnsaSiAgentIndex_Type()
)
hpnsaSiAgentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiAgentIndex.setStatus("mandatory")


class _HpnsaSiAgentName_Type(DisplayString):
    """Custom type hpnsaSiAgentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaSiAgentName_Type.__name__ = "DisplayString"
_HpnsaSiAgentName_Object = MibTableColumn
hpnsaSiAgentName = _HpnsaSiAgentName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 2, 1, 1, 2),
    _HpnsaSiAgentName_Type()
)
hpnsaSiAgentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiAgentName.setStatus("mandatory")


class _HpnsaSiAgentVersion_Type(DisplayString):
    """Custom type hpnsaSiAgentVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HpnsaSiAgentVersion_Type.__name__ = "DisplayString"
_HpnsaSiAgentVersion_Object = MibTableColumn
hpnsaSiAgentVersion = _HpnsaSiAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 2, 1, 1, 3),
    _HpnsaSiAgentVersion_Type()
)
hpnsaSiAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiAgentVersion.setStatus("mandatory")


class _HpnsaSiAgentDate_Type(OctetString):
    """Custom type hpnsaSiAgentDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )
    fixed_length = 7


_HpnsaSiAgentDate_Type.__name__ = "OctetString"
_HpnsaSiAgentDate_Object = MibTableColumn
hpnsaSiAgentDate = _HpnsaSiAgentDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 2, 1, 1, 4),
    _HpnsaSiAgentDate_Type()
)
hpnsaSiAgentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiAgentDate.setStatus("mandatory")
_HpnsaSiBasicInfo_ObjectIdentity = ObjectIdentity
hpnsaSiBasicInfo = _HpnsaSiBasicInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3)
)


class _HpnsaSiModel_Type(Integer32):
    """Custom type hpnsaSiModel based on Integer32"""
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
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              32,
              35,
              36,
              40,
              42,
              52,
              54,
              61,
              63,
              65,
              66,
              67,
              68,
              69,
              71,
              72,
              73,
              75,
              79,
              80,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89)
        )
    )
    namedValues = NamedValues(
        *(("HP_Vectra_PC", 0),
          ("HP_Vectra_ES_12_PC", 1),
          ("HP_Vectra_RS_20_PC", 2),
          ("HP_Vectra_PortableCS_PC", 3),
          ("HP_Vectra_ES_PC", 4),
          ("HP_Vectra_CS_PC", 5),
          ("HP_Vectra_RS_16_PC", 6),
          ("HP_Vectra_QS_16_PC", 7),
          ("HP_Vectra_QS_20_PC", 8),
          ("HP_Vectra_RS_20C_PC", 9),
          ("HP_Vectra_RS_25C_PC", 10),
          ("HP_Vectra_LS_286_PC", 11),
          ("HP_Vectra_QS_16S_PC", 12),
          ("HP_Vectra_386_25_PC", 13),
          ("HP_Vectra_486_25T_PC", 14),
          ("HP_Vectra_286_12_PC", 15),
          ("HP_Vectra_486_33T_PC", 16),
          ("HP_Vectra_386_20_PC", 17),
          ("HP_Vectra_386_16N_PC", 18),
          ("HP_Vectra_386_20N_PC", 19),
          ("HP_Vectra_486s_20_PC", 20),
          ("HP_Vectra_386s_20_PC", 21),
          ("HP_Vectra_486_25U_PC", 22),
          ("HP_Vectra_486_33U_PC", 23),
          ("HP_Vectra_486_50U_PC", 24),
          ("HP_Vectra_486_66U_PC", 25),
          ("HP_Vectra_486_ST_Series", 26),
          ("HP_Vectra_386_25N", 27),
          ("HP_Vectra_486_N", 28),
          ("HP_Vectra_386s_25", 29),
          ("HP_Vectra_386_33N", 30),
          ("HP_Vectra_486_33N", 32),
          ("HP_NetServer_LE_Series", 35),
          ("HP_NetServer_LM_Series", 36),
          ("HP_NetServer_LF_Series", 40),
          ("HP_NetServer_LS_Series", 42),
          ("HP_NetServer_LD_Series", 52),
          ("HP_NetServer_Racks_Series", 54),
          ("HP_NetServer_LC_Series", 61),
          ("HP_NetServer_LH_Series", 63),
          ("HP_NetServer_LX_Series", 65),
          ("HP_NetServer_LH3000", 66),
          ("HP_NetServer_LH6000", 67),
          ("HP_NetServer_LC2000", 68),
          ("HP_NetServer_LT6000", 69),
          ("HP_NetServer_E_Series", 71),
          ("HP_NetServer_LP1000r", 72),
          ("HP_NetServer_LP2000r", 73),
          ("HP_NetServer_tc6100", 75),
          ("HP_NetServer_tc3100", 79),
          ("HP_NetServer_tc4100", 80),
          ("HP_NetServer_lh6000u3", 82),
          ("HP_NetServer_lt6000ru3", 83),
          ("HP_NetServer_lc2000u3", 84),
          ("HP_NetServer_lh3000u3", 85),
          ("HP_NetServer_lp1000r", 86),
          ("HP_NetServer_lp2000r", 87),
          ("HP_NetServer_tc7100", 88),
          ("HP_NetServer_rc7100", 89))
    )


_HpnsaSiModel_Type.__name__ = "Integer32"
_HpnsaSiModel_Object = MibScalar
hpnsaSiModel = _HpnsaSiModel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 1),
    _HpnsaSiModel_Type()
)
hpnsaSiModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiModel.setStatus("mandatory")


class _HpnsaSiBIOSVersion_Type(DisplayString):
    """Custom type hpnsaSiBIOSVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaSiBIOSVersion_Type.__name__ = "DisplayString"
_HpnsaSiBIOSVersion_Object = MibScalar
hpnsaSiBIOSVersion = _HpnsaSiBIOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 2),
    _HpnsaSiBIOSVersion_Type()
)
hpnsaSiBIOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiBIOSVersion.setStatus("mandatory")


class _HpnsaSiVideoBIOSVersion_Type(DisplayString):
    """Custom type hpnsaSiVideoBIOSVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaSiVideoBIOSVersion_Type.__name__ = "DisplayString"
_HpnsaSiVideoBIOSVersion_Object = MibScalar
hpnsaSiVideoBIOSVersion = _HpnsaSiVideoBIOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 3),
    _HpnsaSiVideoBIOSVersion_Type()
)
hpnsaSiVideoBIOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiVideoBIOSVersion.setStatus("optional")


class _HpnsaSiSCSIBIOSVersion_Type(DisplayString):
    """Custom type hpnsaSiSCSIBIOSVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaSiSCSIBIOSVersion_Type.__name__ = "DisplayString"
_HpnsaSiSCSIBIOSVersion_Object = MibScalar
hpnsaSiSCSIBIOSVersion = _HpnsaSiSCSIBIOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 4),
    _HpnsaSiSCSIBIOSVersion_Type()
)
hpnsaSiSCSIBIOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiSCSIBIOSVersion.setStatus("mandatory")
_HpnsaSiNumEISASlots_Type = Integer32
_HpnsaSiNumEISASlots_Object = MibScalar
hpnsaSiNumEISASlots = _HpnsaSiNumEISASlots_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 5),
    _HpnsaSiNumEISASlots_Type()
)
hpnsaSiNumEISASlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiNumEISASlots.setStatus("mandatory")
_HpnsaSiNumPCISlots_Type = Integer32
_HpnsaSiNumPCISlots_Object = MibScalar
hpnsaSiNumPCISlots = _HpnsaSiNumPCISlots_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 6),
    _HpnsaSiNumPCISlots_Type()
)
hpnsaSiNumPCISlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiNumPCISlots.setStatus("mandatory")
_HpnsaSiNumCPU_Type = Integer32
_HpnsaSiNumCPU_Object = MibScalar
hpnsaSiNumCPU = _HpnsaSiNumCPU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 7),
    _HpnsaSiNumCPU_Type()
)
hpnsaSiNumCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiNumCPU.setStatus("mandatory")
_HpnsaSiCPUTable_Object = MibTable
hpnsaSiCPUTable = _HpnsaSiCPUTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 8)
)
if mibBuilder.loadTexts:
    hpnsaSiCPUTable.setStatus("mandatory")
_HpnsaSiCPUEntry_Object = MibTableRow
hpnsaSiCPUEntry = _HpnsaSiCPUEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 8, 1)
)
hpnsaSiCPUEntry.setIndexNames(
    (0, "HPNSASINFO-MIB", "hpnsaSiCPUIndex"),
)
if mibBuilder.loadTexts:
    hpnsaSiCPUEntry.setStatus("mandatory")


class _HpnsaSiCPUIndex_Type(Integer32):
    """Custom type hpnsaSiCPUIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaSiCPUIndex_Type.__name__ = "Integer32"
_HpnsaSiCPUIndex_Object = MibTableColumn
hpnsaSiCPUIndex = _HpnsaSiCPUIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 8, 1, 1),
    _HpnsaSiCPUIndex_Type()
)
hpnsaSiCPUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiCPUIndex.setStatus("mandatory")


class _HpnsaSiCPUModel_Type(Integer32):
    """Custom type hpnsaSiCPUModel based on Integer32"""
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
              18,
              19,
              20,
              21,
              22,
              23,
              253,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("CPU_80286", 0),
          ("CPU_8088", 1),
          ("CPU_8086", 2),
          ("CPU_80386", 3),
          ("CPU_80386_SX", 4),
          ("CPU_486_DX", 5),
          ("CPU_486_SX", 6),
          ("CPU_486_DX2_or_OverDrive", 8),
          ("CPU_486_P23T", 9),
          ("CPU_487_SX", 10),
          ("CPU_Pentium", 11),
          ("CPU_Pentium_OverDrive", 12),
          ("CPU_486_24C", 13),
          ("CPU_Pentium_Series_P54C", 14),
          ("CPU_Pentium_Series_P54CT", 15),
          ("CPU_Pentium_Series_P54CM", 16),
          ("CPU_486_SX2", 17),
          ("CPU_486_SL", 18),
          ("CPU_Pentium_Series_P6", 19),
          ("CPU_Pentium_II", 20),
          ("CPU_Pentium_II_Xeon", 21),
          ("CPU_Pentium_III", 22),
          ("CPU_Pentium_III_Xeon", 23),
          ("notPresent", 253),
          ("CPU_Dual_Pentium", 254),
          ("CPU_Unknown", 255))
    )


_HpnsaSiCPUModel_Type.__name__ = "Integer32"
_HpnsaSiCPUModel_Object = MibTableColumn
hpnsaSiCPUModel = _HpnsaSiCPUModel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 8, 1, 2),
    _HpnsaSiCPUModel_Type()
)
hpnsaSiCPUModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiCPUModel.setStatus("mandatory")
_HpnsaSiCPUSpeed_Type = Integer32
_HpnsaSiCPUSpeed_Object = MibTableColumn
hpnsaSiCPUSpeed = _HpnsaSiCPUSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 8, 1, 3),
    _HpnsaSiCPUSpeed_Type()
)
hpnsaSiCPUSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiCPUSpeed.setStatus("mandatory")


class _HpnsaSiOpSysType_Type(DisplayString):
    """Custom type hpnsaSiOpSysType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaSiOpSysType_Type.__name__ = "DisplayString"
_HpnsaSiOpSysType_Object = MibScalar
hpnsaSiOpSysType = _HpnsaSiOpSysType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 9),
    _HpnsaSiOpSysType_Type()
)
hpnsaSiOpSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiOpSysType.setStatus("mandatory")


class _HpnsaSiOpSysVer_Type(DisplayString):
    """Custom type hpnsaSiOpSysVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaSiOpSysVer_Type.__name__ = "DisplayString"
_HpnsaSiOpSysVer_Object = MibScalar
hpnsaSiOpSysVer = _HpnsaSiOpSysVer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 10),
    _HpnsaSiOpSysVer_Type()
)
hpnsaSiOpSysVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiOpSysVer.setStatus("mandatory")


class _HpnsaSiSystemName_Type(DisplayString):
    """Custom type hpnsaSiSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaSiSystemName_Type.__name__ = "DisplayString"
_HpnsaSiSystemName_Object = MibScalar
hpnsaSiSystemName = _HpnsaSiSystemName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 11),
    _HpnsaSiSystemName_Type()
)
hpnsaSiSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiSystemName.setStatus("mandatory")


class _HpnsaSiSystemID_Type(DisplayString):
    """Custom type hpnsaSiSystemID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaSiSystemID_Type.__name__ = "DisplayString"
_HpnsaSiSystemID_Object = MibScalar
hpnsaSiSystemID = _HpnsaSiSystemID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 12),
    _HpnsaSiSystemID_Type()
)
hpnsaSiSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiSystemID.setStatus("optional")


class _HpnsaSiKbdType_Type(DisplayString):
    """Custom type hpnsaSiKbdType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaSiKbdType_Type.__name__ = "DisplayString"
_HpnsaSiKbdType_Object = MibScalar
hpnsaSiKbdType = _HpnsaSiKbdType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 13),
    _HpnsaSiKbdType_Type()
)
hpnsaSiKbdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiKbdType.setStatus("optional")


class _HpnsaSiMouseType_Type(DisplayString):
    """Custom type hpnsaSiMouseType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaSiMouseType_Type.__name__ = "DisplayString"
_HpnsaSiMouseType_Object = MibScalar
hpnsaSiMouseType = _HpnsaSiMouseType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 14),
    _HpnsaSiMouseType_Type()
)
hpnsaSiMouseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiMouseType.setStatus("optional")


class _HpnsaSiVideoType_Type(DisplayString):
    """Custom type hpnsaSiVideoType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaSiVideoType_Type.__name__ = "DisplayString"
_HpnsaSiVideoType_Object = MibScalar
hpnsaSiVideoType = _HpnsaSiVideoType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 15),
    _HpnsaSiVideoType_Type()
)
hpnsaSiVideoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiVideoType.setStatus("optional")
_HpnsaSiNumISASlots_Type = Integer32
_HpnsaSiNumISASlots_Object = MibScalar
hpnsaSiNumISASlots = _HpnsaSiNumISASlots_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 16),
    _HpnsaSiNumISASlots_Type()
)
hpnsaSiNumISASlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiNumISASlots.setStatus("mandatory")


class _HpnsaSiModelName_Type(DisplayString):
    """Custom type hpnsaSiModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaSiModelName_Type.__name__ = "DisplayString"
_HpnsaSiModelName_Object = MibScalar
hpnsaSiModelName = _HpnsaSiModelName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 17),
    _HpnsaSiModelName_Type()
)
hpnsaSiModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiModelName.setStatus("mandatory")


class _HpnsaSiOpSysDescription_Type(DisplayString):
    """Custom type hpnsaSiOpSysDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaSiOpSysDescription_Type.__name__ = "DisplayString"
_HpnsaSiOpSysDescription_Object = MibScalar
hpnsaSiOpSysDescription = _HpnsaSiOpSysDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 18),
    _HpnsaSiOpSysDescription_Type()
)
hpnsaSiOpSysDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiOpSysDescription.setStatus("mandatory")
_HpnsaSiSecurity_ObjectIdentity = ObjectIdentity
hpnsaSiSecurity = _HpnsaSiSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 4)
)


class _HpnsaSiPowerOnPassword_Type(Integer32):
    """Custom type hpnsaSiPowerOnPassword based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("n-a", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_HpnsaSiPowerOnPassword_Type.__name__ = "Integer32"
_HpnsaSiPowerOnPassword_Object = MibScalar
hpnsaSiPowerOnPassword = _HpnsaSiPowerOnPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 4, 1),
    _HpnsaSiPowerOnPassword_Type()
)
hpnsaSiPowerOnPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiPowerOnPassword.setStatus("mandatory")


class _HpnsaSiNetServerMode_Type(Integer32):
    """Custom type hpnsaSiNetServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("n-a", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_HpnsaSiNetServerMode_Type.__name__ = "Integer32"
_HpnsaSiNetServerMode_Object = MibScalar
hpnsaSiNetServerMode = _HpnsaSiNetServerMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 4, 2),
    _HpnsaSiNetServerMode_Type()
)
hpnsaSiNetServerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiNetServerMode.setStatus("mandatory")


class _HpnsaSiKeyboardLockPassword_Type(Integer32):
    """Custom type hpnsaSiKeyboardLockPassword based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("n-a", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_HpnsaSiKeyboardLockPassword_Type.__name__ = "Integer32"
_HpnsaSiKeyboardLockPassword_Object = MibScalar
hpnsaSiKeyboardLockPassword = _HpnsaSiKeyboardLockPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 4, 3),
    _HpnsaSiKeyboardLockPassword_Type()
)
hpnsaSiKeyboardLockPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiKeyboardLockPassword.setStatus("mandatory")


class _HpnsaSiVideoBlankMode_Type(Integer32):
    """Custom type hpnsaSiVideoBlankMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("n-a", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_HpnsaSiVideoBlankMode_Type.__name__ = "Integer32"
_HpnsaSiVideoBlankMode_Object = MibScalar
hpnsaSiVideoBlankMode = _HpnsaSiVideoBlankMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 4, 4),
    _HpnsaSiVideoBlankMode_Type()
)
hpnsaSiVideoBlankMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiVideoBlankMode.setStatus("mandatory")


class _HpnsaSiBootDiskPriority_Type(Integer32):
    """Custom type hpnsaSiBootDiskPriority based on Integer32"""
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
        *(("n-a", 0),
          ("c-then-a", 1),
          ("a-then-c", 2),
          ("c-only", 3),
          ("a-only", 4))
    )


_HpnsaSiBootDiskPriority_Type.__name__ = "Integer32"
_HpnsaSiBootDiskPriority_Object = MibScalar
hpnsaSiBootDiskPriority = _HpnsaSiBootDiskPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 4, 5),
    _HpnsaSiBootDiskPriority_Type()
)
hpnsaSiBootDiskPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiBootDiskPriority.setStatus("mandatory")


class _HpnsaSiWriteToFloppy_Type(Integer32):
    """Custom type hpnsaSiWriteToFloppy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("n-a", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_HpnsaSiWriteToFloppy_Type.__name__ = "Integer32"
_HpnsaSiWriteToFloppy_Object = MibScalar
hpnsaSiWriteToFloppy = _HpnsaSiWriteToFloppy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 4, 6),
    _HpnsaSiWriteToFloppy_Type()
)
hpnsaSiWriteToFloppy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiWriteToFloppy.setStatus("mandatory")


class _HpnsaSiKbdMouseInactivityTO_Type(Integer32):
    """Custom type hpnsaSiKbdMouseInactivityTO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("n-a", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_HpnsaSiKbdMouseInactivityTO_Type.__name__ = "Integer32"
_HpnsaSiKbdMouseInactivityTO_Object = MibScalar
hpnsaSiKbdMouseInactivityTO = _HpnsaSiKbdMouseInactivityTO_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 4, 7),
    _HpnsaSiKbdMouseInactivityTO_Type()
)
hpnsaSiKbdMouseInactivityTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiKbdMouseInactivityTO.setStatus("mandatory")
_HpnsaSiPort_ObjectIdentity = ObjectIdentity
hpnsaSiPort = _HpnsaSiPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 5)
)
_HpnsaSiPortTable_Object = MibTable
hpnsaSiPortTable = _HpnsaSiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 5, 1)
)
if mibBuilder.loadTexts:
    hpnsaSiPortTable.setStatus("mandatory")
_HpnsaSiPortEntry_Object = MibTableRow
hpnsaSiPortEntry = _HpnsaSiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 5, 1, 1)
)
hpnsaSiPortEntry.setIndexNames(
    (0, "HPNSASINFO-MIB", "hpnsaSiPortIndex"),
)
if mibBuilder.loadTexts:
    hpnsaSiPortEntry.setStatus("mandatory")
_HpnsaSiPortIndex_Type = Integer32
_HpnsaSiPortIndex_Object = MibTableColumn
hpnsaSiPortIndex = _HpnsaSiPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 5, 1, 1, 1),
    _HpnsaSiPortIndex_Type()
)
hpnsaSiPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiPortIndex.setStatus("mandatory")


class _HpnsaSiPortType_Type(Integer32):
    """Custom type hpnsaSiPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("serial", 1),
          ("parallel", 2))
    )


_HpnsaSiPortType_Type.__name__ = "Integer32"
_HpnsaSiPortType_Object = MibTableColumn
hpnsaSiPortType = _HpnsaSiPortType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 5, 1, 1, 2),
    _HpnsaSiPortType_Type()
)
hpnsaSiPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiPortType.setStatus("mandatory")
_HpnsaSiPortStartAddress_Type = Integer32
_HpnsaSiPortStartAddress_Object = MibTableColumn
hpnsaSiPortStartAddress = _HpnsaSiPortStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 5, 1, 1, 3),
    _HpnsaSiPortStartAddress_Type()
)
hpnsaSiPortStartAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiPortStartAddress.setStatus("mandatory")
_HpnsaSiPortEndAddress_Type = Integer32
_HpnsaSiPortEndAddress_Object = MibTableColumn
hpnsaSiPortEndAddress = _HpnsaSiPortEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 5, 1, 1, 4),
    _HpnsaSiPortEndAddress_Type()
)
hpnsaSiPortEndAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiPortEndAddress.setStatus("mandatory")
_HpnsaSiPortInterruptNum_Type = Integer32
_HpnsaSiPortInterruptNum_Object = MibTableColumn
hpnsaSiPortInterruptNum = _HpnsaSiPortInterruptNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 5, 1, 1, 5),
    _HpnsaSiPortInterruptNum_Type()
)
hpnsaSiPortInterruptNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiPortInterruptNum.setStatus("mandatory")
_HpnsaSiMemory_ObjectIdentity = ObjectIdentity
hpnsaSiMemory = _HpnsaSiMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 6)
)


class _HpnsaSiBaseMemSize_Type(Integer32):
    """Custom type hpnsaSiBaseMemSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnsaSiBaseMemSize_Type.__name__ = "Integer32"
_HpnsaSiBaseMemSize_Object = MibScalar
hpnsaSiBaseMemSize = _HpnsaSiBaseMemSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 6, 1),
    _HpnsaSiBaseMemSize_Type()
)
hpnsaSiBaseMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiBaseMemSize.setStatus("mandatory")


class _HpnsaSiExtMemSize_Type(Integer32):
    """Custom type hpnsaSiExtMemSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnsaSiExtMemSize_Type.__name__ = "Integer32"
_HpnsaSiExtMemSize_Object = MibScalar
hpnsaSiExtMemSize = _HpnsaSiExtMemSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 6, 2),
    _HpnsaSiExtMemSize_Type()
)
hpnsaSiExtMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiExtMemSize.setStatus("mandatory")


class _HpnsaSiMemType_Type(Integer32):
    """Custom type hpnsaSiMemType based on Integer32"""
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
        *(("other", 0),
          ("on-board", 1),
          ("singleWidthModule", 2),
          ("doubleWidthModule", 3),
          ("simm", 4))
    )


_HpnsaSiMemType_Type.__name__ = "Integer32"
_HpnsaSiMemType_Object = MibScalar
hpnsaSiMemType = _HpnsaSiMemType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 6, 3),
    _HpnsaSiMemType_Type()
)
hpnsaSiMemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiMemType.setStatus("optional")


class _HpnsaSiMemSpeed_Type(Integer32):
    """Custom type hpnsaSiMemSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaSiMemSpeed_Type.__name__ = "Integer32"
_HpnsaSiMemSpeed_Object = MibScalar
hpnsaSiMemSpeed = _HpnsaSiMemSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 6, 4),
    _HpnsaSiMemSpeed_Type()
)
hpnsaSiMemSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiMemSpeed.setStatus("optional")
_HpnsaSiFloppyDrive_ObjectIdentity = ObjectIdentity
hpnsaSiFloppyDrive = _HpnsaSiFloppyDrive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 8)
)
_HpnsaSiNumFloppyDrives_Type = Integer32
_HpnsaSiNumFloppyDrives_Object = MibScalar
hpnsaSiNumFloppyDrives = _HpnsaSiNumFloppyDrives_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 8, 1),
    _HpnsaSiNumFloppyDrives_Type()
)
hpnsaSiNumFloppyDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiNumFloppyDrives.setStatus("mandatory")
_HpnsaSiFloppyDriveTable_Object = MibTable
hpnsaSiFloppyDriveTable = _HpnsaSiFloppyDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 8, 2)
)
if mibBuilder.loadTexts:
    hpnsaSiFloppyDriveTable.setStatus("mandatory")
_HpnsaSiFloppyDriveEntry_Object = MibTableRow
hpnsaSiFloppyDriveEntry = _HpnsaSiFloppyDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 8, 2, 1)
)
hpnsaSiFloppyDriveEntry.setIndexNames(
    (0, "HPNSASINFO-MIB", "hpnsaSiFloppyDriveIndex"),
)
if mibBuilder.loadTexts:
    hpnsaSiFloppyDriveEntry.setStatus("mandatory")
_HpnsaSiFloppyDriveIndex_Type = Integer32
_HpnsaSiFloppyDriveIndex_Object = MibTableColumn
hpnsaSiFloppyDriveIndex = _HpnsaSiFloppyDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 8, 2, 1, 1),
    _HpnsaSiFloppyDriveIndex_Type()
)
hpnsaSiFloppyDriveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiFloppyDriveIndex.setStatus("mandatory")


class _HpnsaSiFloppyDriveType_Type(Integer32):
    """Custom type hpnsaSiFloppyDriveType based on Integer32"""
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
        *(("unknown", 0),
          ("m-360K", 1),
          ("m-1-2MB", 2),
          ("m-1-2-MB", 3),
          ("m-1-44MB", 4))
    )


_HpnsaSiFloppyDriveType_Type.__name__ = "Integer32"
_HpnsaSiFloppyDriveType_Object = MibTableColumn
hpnsaSiFloppyDriveType = _HpnsaSiFloppyDriveType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 8, 2, 1, 2),
    _HpnsaSiFloppyDriveType_Type()
)
hpnsaSiFloppyDriveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiFloppyDriveType.setStatus("mandatory")
_HpnsaSiRemoteLocatorLED_ObjectIdentity = ObjectIdentity
hpnsaSiRemoteLocatorLED = _HpnsaSiRemoteLocatorLED_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 9)
)


class _HpnsaSiRemoteLocatorLEDSupported_Type(Integer32):
    """Custom type hpnsaSiRemoteLocatorLEDSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("Supported", 1))
    )


_HpnsaSiRemoteLocatorLEDSupported_Type.__name__ = "Integer32"
_HpnsaSiRemoteLocatorLEDSupported_Object = MibScalar
hpnsaSiRemoteLocatorLEDSupported = _HpnsaSiRemoteLocatorLEDSupported_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 9, 1),
    _HpnsaSiRemoteLocatorLEDSupported_Type()
)
hpnsaSiRemoteLocatorLEDSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiRemoteLocatorLEDSupported.setStatus("mandatory")


class _HpnsaSiRemoteLocatorLEDStatus_Type(Integer32):
    """Custom type hpnsaSiRemoteLocatorLEDStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ledOFF", 0),
          ("ledON", 1))
    )


_HpnsaSiRemoteLocatorLEDStatus_Type.__name__ = "Integer32"
_HpnsaSiRemoteLocatorLEDStatus_Object = MibScalar
hpnsaSiRemoteLocatorLEDStatus = _HpnsaSiRemoteLocatorLEDStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 9, 2),
    _HpnsaSiRemoteLocatorLEDStatus_Type()
)
hpnsaSiRemoteLocatorLEDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiRemoteLocatorLEDStatus.setStatus("mandatory")


class _HpnsaSiRemoteLocatorLEDSet_Type(Integer32):
    """Custom type hpnsaSiRemoteLocatorLEDSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ledOFF", 0),
          ("ledON", 1))
    )


_HpnsaSiRemoteLocatorLEDSet_Type.__name__ = "Integer32"
_HpnsaSiRemoteLocatorLEDSet_Object = MibScalar
hpnsaSiRemoteLocatorLEDSet = _HpnsaSiRemoteLocatorLEDSet_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 9, 3),
    _HpnsaSiRemoteLocatorLEDSet_Type()
)
hpnsaSiRemoteLocatorLEDSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaSiRemoteLocatorLEDSet.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPNSASINFO-MIB",
    **{"hp": hp,
       "nm": nm,
       "hpnsa": hpnsa,
       "hpnsaSystemInfo": hpnsaSystemInfo,
       "hpnsaSiMibRev": hpnsaSiMibRev,
       "hpnsaSiMibRevMajor": hpnsaSiMibRevMajor,
       "hpnsaSiMibRevMinor": hpnsaSiMibRevMinor,
       "hpnsaSiAgent": hpnsaSiAgent,
       "hpnsaSiAgentTable": hpnsaSiAgentTable,
       "hpnsaSiAgentEntry": hpnsaSiAgentEntry,
       "hpnsaSiAgentIndex": hpnsaSiAgentIndex,
       "hpnsaSiAgentName": hpnsaSiAgentName,
       "hpnsaSiAgentVersion": hpnsaSiAgentVersion,
       "hpnsaSiAgentDate": hpnsaSiAgentDate,
       "hpnsaSiBasicInfo": hpnsaSiBasicInfo,
       "hpnsaSiModel": hpnsaSiModel,
       "hpnsaSiBIOSVersion": hpnsaSiBIOSVersion,
       "hpnsaSiVideoBIOSVersion": hpnsaSiVideoBIOSVersion,
       "hpnsaSiSCSIBIOSVersion": hpnsaSiSCSIBIOSVersion,
       "hpnsaSiNumEISASlots": hpnsaSiNumEISASlots,
       "hpnsaSiNumPCISlots": hpnsaSiNumPCISlots,
       "hpnsaSiNumCPU": hpnsaSiNumCPU,
       "hpnsaSiCPUTable": hpnsaSiCPUTable,
       "hpnsaSiCPUEntry": hpnsaSiCPUEntry,
       "hpnsaSiCPUIndex": hpnsaSiCPUIndex,
       "hpnsaSiCPUModel": hpnsaSiCPUModel,
       "hpnsaSiCPUSpeed": hpnsaSiCPUSpeed,
       "hpnsaSiOpSysType": hpnsaSiOpSysType,
       "hpnsaSiOpSysVer": hpnsaSiOpSysVer,
       "hpnsaSiSystemName": hpnsaSiSystemName,
       "hpnsaSiSystemID": hpnsaSiSystemID,
       "hpnsaSiKbdType": hpnsaSiKbdType,
       "hpnsaSiMouseType": hpnsaSiMouseType,
       "hpnsaSiVideoType": hpnsaSiVideoType,
       "hpnsaSiNumISASlots": hpnsaSiNumISASlots,
       "hpnsaSiModelName": hpnsaSiModelName,
       "hpnsaSiOpSysDescription": hpnsaSiOpSysDescription,
       "hpnsaSiSecurity": hpnsaSiSecurity,
       "hpnsaSiPowerOnPassword": hpnsaSiPowerOnPassword,
       "hpnsaSiNetServerMode": hpnsaSiNetServerMode,
       "hpnsaSiKeyboardLockPassword": hpnsaSiKeyboardLockPassword,
       "hpnsaSiVideoBlankMode": hpnsaSiVideoBlankMode,
       "hpnsaSiBootDiskPriority": hpnsaSiBootDiskPriority,
       "hpnsaSiWriteToFloppy": hpnsaSiWriteToFloppy,
       "hpnsaSiKbdMouseInactivityTO": hpnsaSiKbdMouseInactivityTO,
       "hpnsaSiPort": hpnsaSiPort,
       "hpnsaSiPortTable": hpnsaSiPortTable,
       "hpnsaSiPortEntry": hpnsaSiPortEntry,
       "hpnsaSiPortIndex": hpnsaSiPortIndex,
       "hpnsaSiPortType": hpnsaSiPortType,
       "hpnsaSiPortStartAddress": hpnsaSiPortStartAddress,
       "hpnsaSiPortEndAddress": hpnsaSiPortEndAddress,
       "hpnsaSiPortInterruptNum": hpnsaSiPortInterruptNum,
       "hpnsaSiMemory": hpnsaSiMemory,
       "hpnsaSiBaseMemSize": hpnsaSiBaseMemSize,
       "hpnsaSiExtMemSize": hpnsaSiExtMemSize,
       "hpnsaSiMemType": hpnsaSiMemType,
       "hpnsaSiMemSpeed": hpnsaSiMemSpeed,
       "hpnsaSiFloppyDrive": hpnsaSiFloppyDrive,
       "hpnsaSiNumFloppyDrives": hpnsaSiNumFloppyDrives,
       "hpnsaSiFloppyDriveTable": hpnsaSiFloppyDriveTable,
       "hpnsaSiFloppyDriveEntry": hpnsaSiFloppyDriveEntry,
       "hpnsaSiFloppyDriveIndex": hpnsaSiFloppyDriveIndex,
       "hpnsaSiFloppyDriveType": hpnsaSiFloppyDriveType,
       "hpnsaSiRemoteLocatorLED": hpnsaSiRemoteLocatorLED,
       "hpnsaSiRemoteLocatorLEDSupported": hpnsaSiRemoteLocatorLEDSupported,
       "hpnsaSiRemoteLocatorLEDStatus": hpnsaSiRemoteLocatorLEDStatus,
       "hpnsaSiRemoteLocatorLEDSet": hpnsaSiRemoteLocatorLEDSet}
)
