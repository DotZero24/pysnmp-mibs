# SNMP MIB module (MAIPU-WRED-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MAIPU-WRED-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:04 2025
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

maipuWredMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



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
_MaipuWredMIBObjects_ObjectIdentity = ObjectIdentity
maipuWredMIBObjects = _MaipuWredMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1)
)
_MpWredConfig_ObjectIdentity = ObjectIdentity
mpWredConfig = _MpWredConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1)
)
_MpWredGroupCfgTable_Object = MibTable
mpWredGroupCfgTable = _MpWredGroupCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mpWredGroupCfgTable.setStatus("current")
_MpWredGroupCfgEntry_Object = MibTableRow
mpWredGroupCfgEntry = _MpWredGroupCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 1, 1)
)
mpWredGroupCfgEntry.setIndexNames(
    (0, "MAIPU-WRED-MIB", "mpWredGroupCfgName"),
)
if mibBuilder.loadTexts:
    mpWredGroupCfgEntry.setStatus("current")


class _MpWredGroupCfgName_Type(DisplayString):
    """Custom type mpWredGroupCfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpWredGroupCfgName_Type.__name__ = "DisplayString"
_MpWredGroupCfgName_Object = MibTableColumn
mpWredGroupCfgName = _MpWredGroupCfgName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 1, 1, 1),
    _MpWredGroupCfgName_Type()
)
mpWredGroupCfgName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpWredGroupCfgName.setStatus("current")


class _MpWredGroupCfgDscpPrec_Type(Integer32):
    """Custom type mpWredGroupCfgDscpPrec based on Integer32"""
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
        *(("precedence", 1),
          ("dscp", 2),
          ("discardClass", 3),
          ("l2Cos", 4),
          ("atmClp", 5),
          ("mplsExp", 6),
          ("redDefault", 7),
          ("redUserDefault", 8))
    )


_MpWredGroupCfgDscpPrec_Type.__name__ = "Integer32"
_MpWredGroupCfgDscpPrec_Object = MibTableColumn
mpWredGroupCfgDscpPrec = _MpWredGroupCfgDscpPrec_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 1, 1, 2),
    _MpWredGroupCfgDscpPrec_Type()
)
mpWredGroupCfgDscpPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredGroupCfgDscpPrec.setStatus("current")


class _MpWredGroupCfgExponWeight_Type(Integer32):
    """Custom type mpWredGroupCfgExponWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MpWredGroupCfgExponWeight_Type.__name__ = "Integer32"
_MpWredGroupCfgExponWeight_Object = MibTableColumn
mpWredGroupCfgExponWeight = _MpWredGroupCfgExponWeight_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 1, 1, 3),
    _MpWredGroupCfgExponWeight_Type()
)
mpWredGroupCfgExponWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredGroupCfgExponWeight.setStatus("current")
_MpWredGroupPrecCfgTable_Object = MibTable
mpWredGroupPrecCfgTable = _MpWredGroupPrecCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mpWredGroupPrecCfgTable.setStatus("current")
_MpWredGroupPrecCfgEntry_Object = MibTableRow
mpWredGroupPrecCfgEntry = _MpWredGroupPrecCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 2, 1)
)
mpWredGroupPrecCfgEntry.setIndexNames(
    (0, "MAIPU-WRED-MIB", "mpWredGroupCfgName"),
    (0, "MAIPU-WRED-MIB", "mpWredGroupPrecCfgValue"),
)
if mibBuilder.loadTexts:
    mpWredGroupPrecCfgEntry.setStatus("current")


class _MpWredGroupPrecCfgValue_Type(Integer32):
    """Custom type mpWredGroupPrecCfgValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_MpWredGroupPrecCfgValue_Type.__name__ = "Integer32"
_MpWredGroupPrecCfgValue_Object = MibTableColumn
mpWredGroupPrecCfgValue = _MpWredGroupPrecCfgValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 2, 1, 1),
    _MpWredGroupPrecCfgValue_Type()
)
mpWredGroupPrecCfgValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpWredGroupPrecCfgValue.setStatus("current")
_MpWredGroupPrecCfgMinThreshold_Type = Unsigned32
_MpWredGroupPrecCfgMinThreshold_Object = MibTableColumn
mpWredGroupPrecCfgMinThreshold = _MpWredGroupPrecCfgMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 2, 1, 2),
    _MpWredGroupPrecCfgMinThreshold_Type()
)
mpWredGroupPrecCfgMinThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredGroupPrecCfgMinThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mpWredGroupPrecCfgMinThreshold.setUnits("packets")
_MpWredGroupPrecCfgMaxThreshold_Type = Unsigned32
_MpWredGroupPrecCfgMaxThreshold_Object = MibTableColumn
mpWredGroupPrecCfgMaxThreshold = _MpWredGroupPrecCfgMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 2, 1, 3),
    _MpWredGroupPrecCfgMaxThreshold_Type()
)
mpWredGroupPrecCfgMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredGroupPrecCfgMaxThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mpWredGroupPrecCfgMaxThreshold.setUnits("packets")


class _MpWredGroupPrecCfgPktDropProb_Type(Integer32):
    """Custom type mpWredGroupPrecCfgPktDropProb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_MpWredGroupPrecCfgPktDropProb_Type.__name__ = "Integer32"
_MpWredGroupPrecCfgPktDropProb_Object = MibTableColumn
mpWredGroupPrecCfgPktDropProb = _MpWredGroupPrecCfgPktDropProb_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 2, 1, 4),
    _MpWredGroupPrecCfgPktDropProb_Type()
)
mpWredGroupPrecCfgPktDropProb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredGroupPrecCfgPktDropProb.setStatus("current")
_MpWredInterfaceCfgTable_Object = MibTable
mpWredInterfaceCfgTable = _MpWredInterfaceCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mpWredInterfaceCfgTable.setStatus("current")
_MpWredInterfaceCfgEntry_Object = MibTableRow
mpWredInterfaceCfgEntry = _MpWredInterfaceCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 3, 1)
)
mpWredInterfaceCfgEntry.setIndexNames(
    (0, "MAIPU-WRED-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mpWredInterfaceCfgEntry.setStatus("current")


class _MpWredIFCfgGroupName_Type(DisplayString):
    """Custom type mpWredIFCfgGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpWredIFCfgGroupName_Type.__name__ = "DisplayString"
_MpWredIFCfgGroupName_Object = MibTableColumn
mpWredIFCfgGroupName = _MpWredIFCfgGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 3, 1, 1),
    _MpWredIFCfgGroupName_Type()
)
mpWredIFCfgGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredIFCfgGroupName.setStatus("current")


class _MpWredIFCfgDscpPrec_Type(Integer32):
    """Custom type mpWredIFCfgDscpPrec based on Integer32"""
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
        *(("precedence", 1),
          ("dscp", 2),
          ("discardClass", 3),
          ("l2Cos", 4),
          ("atmClp", 5),
          ("mplsExp", 6),
          ("redDefault", 7),
          ("redUserDefault", 8))
    )


_MpWredIFCfgDscpPrec_Type.__name__ = "Integer32"
_MpWredIFCfgDscpPrec_Object = MibTableColumn
mpWredIFCfgDscpPrec = _MpWredIFCfgDscpPrec_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 3, 1, 2),
    _MpWredIFCfgDscpPrec_Type()
)
mpWredIFCfgDscpPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredIFCfgDscpPrec.setStatus("current")


class _MpWredIFCfgExponWeight_Type(Integer32):
    """Custom type mpWredIFCfgExponWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MpWredIFCfgExponWeight_Type.__name__ = "Integer32"
_MpWredIFCfgExponWeight_Object = MibTableColumn
mpWredIFCfgExponWeight = _MpWredIFCfgExponWeight_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 3, 1, 3),
    _MpWredIFCfgExponWeight_Type()
)
mpWredIFCfgExponWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredIFCfgExponWeight.setStatus("current")
_MpWredFrameRelayVCCfgTable_Object = MibTable
mpWredFrameRelayVCCfgTable = _MpWredFrameRelayVCCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    mpWredFrameRelayVCCfgTable.setStatus("current")
_MpWredFrameRelayVCCfgEntry_Object = MibTableRow
mpWredFrameRelayVCCfgEntry = _MpWredFrameRelayVCCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 4, 1)
)
mpWredFrameRelayVCCfgEntry.setIndexNames(
    (0, "MAIPU-WRED-MIB", "ifIndex"),
    (0, "MAIPU-WRED-MIB", "mpWredFRCfgDLCI"),
)
if mibBuilder.loadTexts:
    mpWredFrameRelayVCCfgEntry.setStatus("current")


class _MpWredFRCfgDLCI_Type(Unsigned32):
    """Custom type mpWredFRCfgDLCI based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1007),
    )


_MpWredFRCfgDLCI_Type.__name__ = "Unsigned32"
_MpWredFRCfgDLCI_Object = MibTableColumn
mpWredFRCfgDLCI = _MpWredFRCfgDLCI_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 4, 1, 1),
    _MpWredFRCfgDLCI_Type()
)
mpWredFRCfgDLCI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpWredFRCfgDLCI.setStatus("current")


class _MpWredFRCfgGroupName_Type(DisplayString):
    """Custom type mpWredFRCfgGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpWredFRCfgGroupName_Type.__name__ = "DisplayString"
_MpWredFRCfgGroupName_Object = MibTableColumn
mpWredFRCfgGroupName = _MpWredFRCfgGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 4, 1, 2),
    _MpWredFRCfgGroupName_Type()
)
mpWredFRCfgGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredFRCfgGroupName.setStatus("current")


class _MpWredFRCfgDscpPrec_Type(Integer32):
    """Custom type mpWredFRCfgDscpPrec based on Integer32"""
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
        *(("precedence", 1),
          ("dscp", 2),
          ("discardClass", 3),
          ("l2Cos", 4),
          ("atmClp", 5),
          ("mplsExp", 6),
          ("redDefault", 7),
          ("redUserDefault", 8))
    )


_MpWredFRCfgDscpPrec_Type.__name__ = "Integer32"
_MpWredFRCfgDscpPrec_Object = MibTableColumn
mpWredFRCfgDscpPrec = _MpWredFRCfgDscpPrec_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 4, 1, 3),
    _MpWredFRCfgDscpPrec_Type()
)
mpWredFRCfgDscpPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredFRCfgDscpPrec.setStatus("current")


class _MpWredFRCfgExponWeight_Type(Integer32):
    """Custom type mpWredFRCfgExponWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MpWredFRCfgExponWeight_Type.__name__ = "Integer32"
_MpWredFRCfgExponWeight_Object = MibTableColumn
mpWredFRCfgExponWeight = _MpWredFRCfgExponWeight_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 4, 1, 4),
    _MpWredFRCfgExponWeight_Type()
)
mpWredFRCfgExponWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredFRCfgExponWeight.setStatus("current")
_MpWredATMPVCCfgTable_Object = MibTable
mpWredATMPVCCfgTable = _MpWredATMPVCCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    mpWredATMPVCCfgTable.setStatus("current")
_MpWredATMPVCCfgEntry_Object = MibTableRow
mpWredATMPVCCfgEntry = _MpWredATMPVCCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 5, 1)
)
mpWredATMPVCCfgEntry.setIndexNames(
    (0, "MAIPU-WRED-MIB", "ifIndex"),
    (0, "MAIPU-WRED-MIB", "mpWredATMCfgVPI"),
    (0, "MAIPU-WRED-MIB", "mpWredATMCfgVCI"),
)
if mibBuilder.loadTexts:
    mpWredATMPVCCfgEntry.setStatus("current")


class _MpWredATMCfgVPI_Type(Unsigned32):
    """Custom type mpWredATMCfgVPI based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MpWredATMCfgVPI_Type.__name__ = "Unsigned32"
_MpWredATMCfgVPI_Object = MibTableColumn
mpWredATMCfgVPI = _MpWredATMCfgVPI_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 5, 1, 1),
    _MpWredATMCfgVPI_Type()
)
mpWredATMCfgVPI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpWredATMCfgVPI.setStatus("current")


class _MpWredATMCfgVCI_Type(Unsigned32):
    """Custom type mpWredATMCfgVCI based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpWredATMCfgVCI_Type.__name__ = "Unsigned32"
_MpWredATMCfgVCI_Object = MibTableColumn
mpWredATMCfgVCI = _MpWredATMCfgVCI_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 5, 1, 2),
    _MpWredATMCfgVCI_Type()
)
mpWredATMCfgVCI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpWredATMCfgVCI.setStatus("current")


class _MpWredATMCfgGroupName_Type(DisplayString):
    """Custom type mpWredATMCfgGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpWredATMCfgGroupName_Type.__name__ = "DisplayString"
_MpWredATMCfgGroupName_Object = MibTableColumn
mpWredATMCfgGroupName = _MpWredATMCfgGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 5, 1, 3),
    _MpWredATMCfgGroupName_Type()
)
mpWredATMCfgGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredATMCfgGroupName.setStatus("current")


class _MpWredATMCfgDscpPrec_Type(Integer32):
    """Custom type mpWredATMCfgDscpPrec based on Integer32"""
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
        *(("precedence", 1),
          ("dscp", 2),
          ("discardClass", 3),
          ("l2Cos", 4),
          ("atmClp", 5),
          ("mplsExp", 6),
          ("redDefault", 7),
          ("redUserDefault", 8))
    )


_MpWredATMCfgDscpPrec_Type.__name__ = "Integer32"
_MpWredATMCfgDscpPrec_Object = MibTableColumn
mpWredATMCfgDscpPrec = _MpWredATMCfgDscpPrec_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 5, 1, 4),
    _MpWredATMCfgDscpPrec_Type()
)
mpWredATMCfgDscpPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredATMCfgDscpPrec.setStatus("current")


class _MpWredATMCfgExponWeight_Type(Integer32):
    """Custom type mpWredATMCfgExponWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MpWredATMCfgExponWeight_Type.__name__ = "Integer32"
_MpWredATMCfgExponWeight_Object = MibTableColumn
mpWredATMCfgExponWeight = _MpWredATMCfgExponWeight_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 5, 1, 5),
    _MpWredATMCfgExponWeight_Type()
)
mpWredATMCfgExponWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredATMCfgExponWeight.setStatus("current")
_MpWredCfgInterfacePrecTable_Object = MibTable
mpWredCfgInterfacePrecTable = _MpWredCfgInterfacePrecTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    mpWredCfgInterfacePrecTable.setStatus("current")
_MpWredCfgInterfacePrecEntry_Object = MibTableRow
mpWredCfgInterfacePrecEntry = _MpWredCfgInterfacePrecEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 6, 1)
)
mpWredCfgInterfacePrecEntry.setIndexNames(
    (0, "MAIPU-WRED-MIB", "ifIndex"),
    (0, "MAIPU-WRED-MIB", "mpWredIFPrecCfgValue"),
)
if mibBuilder.loadTexts:
    mpWredCfgInterfacePrecEntry.setStatus("current")


class _MpWredIFPrecCfgValue_Type(Integer32):
    """Custom type mpWredIFPrecCfgValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_MpWredIFPrecCfgValue_Type.__name__ = "Integer32"
_MpWredIFPrecCfgValue_Object = MibTableColumn
mpWredIFPrecCfgValue = _MpWredIFPrecCfgValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 6, 1, 1),
    _MpWredIFPrecCfgValue_Type()
)
mpWredIFPrecCfgValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpWredIFPrecCfgValue.setStatus("current")
_MpWredIFPrecCfgMinThreshold_Type = Unsigned32
_MpWredIFPrecCfgMinThreshold_Object = MibTableColumn
mpWredIFPrecCfgMinThreshold = _MpWredIFPrecCfgMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 6, 1, 2),
    _MpWredIFPrecCfgMinThreshold_Type()
)
mpWredIFPrecCfgMinThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredIFPrecCfgMinThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mpWredIFPrecCfgMinThreshold.setUnits("packets")
_MpWredIFPrecCfgMaxThreshold_Type = Unsigned32
_MpWredIFPrecCfgMaxThreshold_Object = MibTableColumn
mpWredIFPrecCfgMaxThreshold = _MpWredIFPrecCfgMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 6, 1, 3),
    _MpWredIFPrecCfgMaxThreshold_Type()
)
mpWredIFPrecCfgMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredIFPrecCfgMaxThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mpWredIFPrecCfgMaxThreshold.setUnits("packets")


class _MpWredIFPrecCfgPktDropProb_Type(Integer32):
    """Custom type mpWredIFPrecCfgPktDropProb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_MpWredIFPrecCfgPktDropProb_Type.__name__ = "Integer32"
_MpWredIFPrecCfgPktDropProb_Object = MibTableColumn
mpWredIFPrecCfgPktDropProb = _MpWredIFPrecCfgPktDropProb_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 6, 1, 4),
    _MpWredIFPrecCfgPktDropProb_Type()
)
mpWredIFPrecCfgPktDropProb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredIFPrecCfgPktDropProb.setStatus("current")
_MpWredCfgFrameRelayVCPrecTable_Object = MibTable
mpWredCfgFrameRelayVCPrecTable = _MpWredCfgFrameRelayVCPrecTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 7)
)
if mibBuilder.loadTexts:
    mpWredCfgFrameRelayVCPrecTable.setStatus("current")
_MpWredCfgFrameRelayVCPrecEntry_Object = MibTableRow
mpWredCfgFrameRelayVCPrecEntry = _MpWredCfgFrameRelayVCPrecEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 7, 1)
)
mpWredCfgFrameRelayVCPrecEntry.setIndexNames(
    (0, "MAIPU-WRED-MIB", "ifIndex"),
    (0, "MAIPU-WRED-MIB", "mpWredFRCfgDLCI"),
    (0, "MAIPU-WRED-MIB", "mpWredFRPrecCfgValue"),
)
if mibBuilder.loadTexts:
    mpWredCfgFrameRelayVCPrecEntry.setStatus("current")


class _MpWredFRPrecCfgValue_Type(Integer32):
    """Custom type mpWredFRPrecCfgValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_MpWredFRPrecCfgValue_Type.__name__ = "Integer32"
_MpWredFRPrecCfgValue_Object = MibTableColumn
mpWredFRPrecCfgValue = _MpWredFRPrecCfgValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 7, 1, 1),
    _MpWredFRPrecCfgValue_Type()
)
mpWredFRPrecCfgValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpWredFRPrecCfgValue.setStatus("current")
_MpWredFRPrecCfgMinThreshold_Type = Unsigned32
_MpWredFRPrecCfgMinThreshold_Object = MibTableColumn
mpWredFRPrecCfgMinThreshold = _MpWredFRPrecCfgMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 7, 1, 2),
    _MpWredFRPrecCfgMinThreshold_Type()
)
mpWredFRPrecCfgMinThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredFRPrecCfgMinThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mpWredFRPrecCfgMinThreshold.setUnits("packets")
_MpWredFRPrecCfgMaxThreshold_Type = Unsigned32
_MpWredFRPrecCfgMaxThreshold_Object = MibTableColumn
mpWredFRPrecCfgMaxThreshold = _MpWredFRPrecCfgMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 7, 1, 3),
    _MpWredFRPrecCfgMaxThreshold_Type()
)
mpWredFRPrecCfgMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredFRPrecCfgMaxThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mpWredFRPrecCfgMaxThreshold.setUnits("packets")


class _MpWredFRPrecCfgPktDropProb_Type(Integer32):
    """Custom type mpWredFRPrecCfgPktDropProb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_MpWredFRPrecCfgPktDropProb_Type.__name__ = "Integer32"
_MpWredFRPrecCfgPktDropProb_Object = MibTableColumn
mpWredFRPrecCfgPktDropProb = _MpWredFRPrecCfgPktDropProb_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 7, 1, 4),
    _MpWredFRPrecCfgPktDropProb_Type()
)
mpWredFRPrecCfgPktDropProb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredFRPrecCfgPktDropProb.setStatus("current")
_MpWredCfgATMPVCPrecTable_Object = MibTable
mpWredCfgATMPVCPrecTable = _MpWredCfgATMPVCPrecTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 8)
)
if mibBuilder.loadTexts:
    mpWredCfgATMPVCPrecTable.setStatus("current")
_MpWredCfgATMPVCPrecEntry_Object = MibTableRow
mpWredCfgATMPVCPrecEntry = _MpWredCfgATMPVCPrecEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 8, 1)
)
mpWredCfgATMPVCPrecEntry.setIndexNames(
    (0, "MAIPU-WRED-MIB", "ifIndex"),
    (0, "MAIPU-WRED-MIB", "mpWredATMCfgVPI"),
    (0, "MAIPU-WRED-MIB", "mpWredATMCfgVCI"),
    (0, "MAIPU-WRED-MIB", "mpWredATMPrecCfgValue"),
)
if mibBuilder.loadTexts:
    mpWredCfgATMPVCPrecEntry.setStatus("current")


class _MpWredATMPrecCfgValue_Type(Integer32):
    """Custom type mpWredATMPrecCfgValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_MpWredATMPrecCfgValue_Type.__name__ = "Integer32"
_MpWredATMPrecCfgValue_Object = MibTableColumn
mpWredATMPrecCfgValue = _MpWredATMPrecCfgValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 8, 1, 1),
    _MpWredATMPrecCfgValue_Type()
)
mpWredATMPrecCfgValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpWredATMPrecCfgValue.setStatus("current")
_MpWredATMPrecCfgMinThreshold_Type = Unsigned32
_MpWredATMPrecCfgMinThreshold_Object = MibTableColumn
mpWredATMPrecCfgMinThreshold = _MpWredATMPrecCfgMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 8, 1, 2),
    _MpWredATMPrecCfgMinThreshold_Type()
)
mpWredATMPrecCfgMinThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredATMPrecCfgMinThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mpWredATMPrecCfgMinThreshold.setUnits("packets")
_MpWredATMPrecCfgMaxThreshold_Type = Unsigned32
_MpWredATMPrecCfgMaxThreshold_Object = MibTableColumn
mpWredATMPrecCfgMaxThreshold = _MpWredATMPrecCfgMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 8, 1, 3),
    _MpWredATMPrecCfgMaxThreshold_Type()
)
mpWredATMPrecCfgMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredATMPrecCfgMaxThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mpWredATMPrecCfgMaxThreshold.setUnits("packets")


class _MpWredATMPrecCfgPktDropProb_Type(Integer32):
    """Custom type mpWredATMPrecCfgPktDropProb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_MpWredATMPrecCfgPktDropProb_Type.__name__ = "Integer32"
_MpWredATMPrecCfgPktDropProb_Object = MibTableColumn
mpWredATMPrecCfgPktDropProb = _MpWredATMPrecCfgPktDropProb_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 1, 8, 1, 4),
    _MpWredATMPrecCfgPktDropProb_Type()
)
mpWredATMPrecCfgPktDropProb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredATMPrecCfgPktDropProb.setStatus("current")
_MpWredStats_ObjectIdentity = ObjectIdentity
mpWredStats = _MpWredStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 2)
)
_MpWredInterfaceStatTable_Object = MibTable
mpWredInterfaceStatTable = _MpWredInterfaceStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mpWredInterfaceStatTable.setStatus("current")
_MpWredInterfaceStatEntry_Object = MibTableRow
mpWredInterfaceStatEntry = _MpWredInterfaceStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 2, 1, 1)
)
mpWredInterfaceStatEntry.setIndexNames(
    (0, "MAIPU-WRED-MIB", "ifIndex"),
    (0, "MAIPU-WRED-MIB", "mpWredIFStatPrecValue"),
)
if mibBuilder.loadTexts:
    mpWredInterfaceStatEntry.setStatus("current")


class _MpWredIFStatPrecValue_Type(Integer32):
    """Custom type mpWredIFStatPrecValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_MpWredIFStatPrecValue_Type.__name__ = "Integer32"
_MpWredIFStatPrecValue_Object = MibTableColumn
mpWredIFStatPrecValue = _MpWredIFStatPrecValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 2, 1, 1, 1),
    _MpWredIFStatPrecValue_Type()
)
mpWredIFStatPrecValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpWredIFStatPrecValue.setStatus("current")
_MpWredIFStatRandomDropPkt64_Type = Counter64
_MpWredIFStatRandomDropPkt64_Object = MibTableColumn
mpWredIFStatRandomDropPkt64 = _MpWredIFStatRandomDropPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 2, 1, 1, 2),
    _MpWredIFStatRandomDropPkt64_Type()
)
mpWredIFStatRandomDropPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredIFStatRandomDropPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpWredIFStatRandomDropPkt64.setUnits("packets")
_MpWredIFStatTailDropPkt64_Type = Counter64
_MpWredIFStatTailDropPkt64_Object = MibTableColumn
mpWredIFStatTailDropPkt64 = _MpWredIFStatTailDropPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 2, 1, 1, 3),
    _MpWredIFStatTailDropPkt64_Type()
)
mpWredIFStatTailDropPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredIFStatTailDropPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpWredIFStatTailDropPkt64.setUnits("packets")
_MpWredIFStatTransmitPkt64_Type = Counter64
_MpWredIFStatTransmitPkt64_Object = MibTableColumn
mpWredIFStatTransmitPkt64 = _MpWredIFStatTransmitPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 2, 1, 1, 4),
    _MpWredIFStatTransmitPkt64_Type()
)
mpWredIFStatTransmitPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredIFStatTransmitPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpWredIFStatTransmitPkt64.setUnits("packets")
_MpWredFrameRelayVCStatTable_Object = MibTable
mpWredFrameRelayVCStatTable = _MpWredFrameRelayVCStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mpWredFrameRelayVCStatTable.setStatus("current")
_MpWredFrameRelayVCStatEntry_Object = MibTableRow
mpWredFrameRelayVCStatEntry = _MpWredFrameRelayVCStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 2, 2, 1)
)
mpWredFrameRelayVCStatEntry.setIndexNames(
    (0, "MAIPU-WRED-MIB", "ifIndex"),
    (0, "MAIPU-WRED-MIB", "mpWredFRCfgDLCI"),
    (0, "MAIPU-WRED-MIB", "mpWredFRStatPrecValue"),
)
if mibBuilder.loadTexts:
    mpWredFrameRelayVCStatEntry.setStatus("current")


class _MpWredFRStatPrecValue_Type(Integer32):
    """Custom type mpWredFRStatPrecValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_MpWredFRStatPrecValue_Type.__name__ = "Integer32"
_MpWredFRStatPrecValue_Object = MibTableColumn
mpWredFRStatPrecValue = _MpWredFRStatPrecValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 2, 2, 1, 1),
    _MpWredFRStatPrecValue_Type()
)
mpWredFRStatPrecValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpWredFRStatPrecValue.setStatus("current")
_MpWredFRStatRandomDropPkt64_Type = Counter64
_MpWredFRStatRandomDropPkt64_Object = MibTableColumn
mpWredFRStatRandomDropPkt64 = _MpWredFRStatRandomDropPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 2, 2, 1, 2),
    _MpWredFRStatRandomDropPkt64_Type()
)
mpWredFRStatRandomDropPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredFRStatRandomDropPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpWredFRStatRandomDropPkt64.setUnits("packets")
_MpWredFRStatTailDropPkt64_Type = Counter64
_MpWredFRStatTailDropPkt64_Object = MibTableColumn
mpWredFRStatTailDropPkt64 = _MpWredFRStatTailDropPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 2, 2, 1, 3),
    _MpWredFRStatTailDropPkt64_Type()
)
mpWredFRStatTailDropPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredFRStatTailDropPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpWredFRStatTailDropPkt64.setUnits("packets")
_MpWredFRStatTransmitPkt64_Type = Counter64
_MpWredFRStatTransmitPkt64_Object = MibTableColumn
mpWredFRStatTransmitPkt64 = _MpWredFRStatTransmitPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 2, 2, 1, 4),
    _MpWredFRStatTransmitPkt64_Type()
)
mpWredFRStatTransmitPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredFRStatTransmitPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpWredFRStatTransmitPkt64.setUnits("packets")
_MpWredATMPVCStatTable_Object = MibTable
mpWredATMPVCStatTable = _MpWredATMPVCStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mpWredATMPVCStatTable.setStatus("current")
_MpWredATMPVCStatEntry_Object = MibTableRow
mpWredATMPVCStatEntry = _MpWredATMPVCStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 2, 3, 1)
)
mpWredATMPVCStatEntry.setIndexNames(
    (0, "MAIPU-WRED-MIB", "ifIndex"),
    (0, "MAIPU-WRED-MIB", "mpWredATMCfgVPI"),
    (0, "MAIPU-WRED-MIB", "mpWredATMCfgVCI"),
    (0, "MAIPU-WRED-MIB", "mpWredATMStatPrecValue"),
)
if mibBuilder.loadTexts:
    mpWredATMPVCStatEntry.setStatus("current")


class _MpWredATMStatPrecValue_Type(Integer32):
    """Custom type mpWredATMStatPrecValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_MpWredATMStatPrecValue_Type.__name__ = "Integer32"
_MpWredATMStatPrecValue_Object = MibTableColumn
mpWredATMStatPrecValue = _MpWredATMStatPrecValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 2, 3, 1, 1),
    _MpWredATMStatPrecValue_Type()
)
mpWredATMStatPrecValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpWredATMStatPrecValue.setStatus("current")
_MpWredATMStatRandomDropPkt64_Type = Counter64
_MpWredATMStatRandomDropPkt64_Object = MibTableColumn
mpWredATMStatRandomDropPkt64 = _MpWredATMStatRandomDropPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 2, 3, 1, 2),
    _MpWredATMStatRandomDropPkt64_Type()
)
mpWredATMStatRandomDropPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredATMStatRandomDropPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpWredATMStatRandomDropPkt64.setUnits("packets")
_MpWredATMStatTailDropPkt64_Type = Counter64
_MpWredATMStatTailDropPkt64_Object = MibTableColumn
mpWredATMStatTailDropPkt64 = _MpWredATMStatTailDropPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 2, 3, 1, 3),
    _MpWredATMStatTailDropPkt64_Type()
)
mpWredATMStatTailDropPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredATMStatTailDropPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpWredATMStatTailDropPkt64.setUnits("packets")
_MpWredATMStatTransmitPkt64_Type = Counter64
_MpWredATMStatTransmitPkt64_Object = MibTableColumn
mpWredATMStatTransmitPkt64 = _MpWredATMStatTransmitPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 2, 1, 2, 3, 1, 4),
    _MpWredATMStatTransmitPkt64_Type()
)
mpWredATMStatTransmitPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpWredATMStatTransmitPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpWredATMStatTransmitPkt64.setUnits("packets")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MAIPU-WRED-MIB",
    **{"maipu": maipu,
       "mpMgmt2": mpMgmt2,
       "mpRouterTech": mpRouterTech,
       "mpRtQoSv2": mpRtQoSv2,
       "maipuWredMIB": maipuWredMIB,
       "maipuWredMIBObjects": maipuWredMIBObjects,
       "mpWredConfig": mpWredConfig,
       "mpWredGroupCfgTable": mpWredGroupCfgTable,
       "mpWredGroupCfgEntry": mpWredGroupCfgEntry,
       "mpWredGroupCfgName": mpWredGroupCfgName,
       "mpWredGroupCfgDscpPrec": mpWredGroupCfgDscpPrec,
       "mpWredGroupCfgExponWeight": mpWredGroupCfgExponWeight,
       "mpWredGroupPrecCfgTable": mpWredGroupPrecCfgTable,
       "mpWredGroupPrecCfgEntry": mpWredGroupPrecCfgEntry,
       "mpWredGroupPrecCfgValue": mpWredGroupPrecCfgValue,
       "mpWredGroupPrecCfgMinThreshold": mpWredGroupPrecCfgMinThreshold,
       "mpWredGroupPrecCfgMaxThreshold": mpWredGroupPrecCfgMaxThreshold,
       "mpWredGroupPrecCfgPktDropProb": mpWredGroupPrecCfgPktDropProb,
       "mpWredInterfaceCfgTable": mpWredInterfaceCfgTable,
       "mpWredInterfaceCfgEntry": mpWredInterfaceCfgEntry,
       "mpWredIFCfgGroupName": mpWredIFCfgGroupName,
       "mpWredIFCfgDscpPrec": mpWredIFCfgDscpPrec,
       "mpWredIFCfgExponWeight": mpWredIFCfgExponWeight,
       "mpWredFrameRelayVCCfgTable": mpWredFrameRelayVCCfgTable,
       "mpWredFrameRelayVCCfgEntry": mpWredFrameRelayVCCfgEntry,
       "mpWredFRCfgDLCI": mpWredFRCfgDLCI,
       "mpWredFRCfgGroupName": mpWredFRCfgGroupName,
       "mpWredFRCfgDscpPrec": mpWredFRCfgDscpPrec,
       "mpWredFRCfgExponWeight": mpWredFRCfgExponWeight,
       "mpWredATMPVCCfgTable": mpWredATMPVCCfgTable,
       "mpWredATMPVCCfgEntry": mpWredATMPVCCfgEntry,
       "mpWredATMCfgVPI": mpWredATMCfgVPI,
       "mpWredATMCfgVCI": mpWredATMCfgVCI,
       "mpWredATMCfgGroupName": mpWredATMCfgGroupName,
       "mpWredATMCfgDscpPrec": mpWredATMCfgDscpPrec,
       "mpWredATMCfgExponWeight": mpWredATMCfgExponWeight,
       "mpWredCfgInterfacePrecTable": mpWredCfgInterfacePrecTable,
       "mpWredCfgInterfacePrecEntry": mpWredCfgInterfacePrecEntry,
       "mpWredIFPrecCfgValue": mpWredIFPrecCfgValue,
       "mpWredIFPrecCfgMinThreshold": mpWredIFPrecCfgMinThreshold,
       "mpWredIFPrecCfgMaxThreshold": mpWredIFPrecCfgMaxThreshold,
       "mpWredIFPrecCfgPktDropProb": mpWredIFPrecCfgPktDropProb,
       "mpWredCfgFrameRelayVCPrecTable": mpWredCfgFrameRelayVCPrecTable,
       "mpWredCfgFrameRelayVCPrecEntry": mpWredCfgFrameRelayVCPrecEntry,
       "mpWredFRPrecCfgValue": mpWredFRPrecCfgValue,
       "mpWredFRPrecCfgMinThreshold": mpWredFRPrecCfgMinThreshold,
       "mpWredFRPrecCfgMaxThreshold": mpWredFRPrecCfgMaxThreshold,
       "mpWredFRPrecCfgPktDropProb": mpWredFRPrecCfgPktDropProb,
       "mpWredCfgATMPVCPrecTable": mpWredCfgATMPVCPrecTable,
       "mpWredCfgATMPVCPrecEntry": mpWredCfgATMPVCPrecEntry,
       "mpWredATMPrecCfgValue": mpWredATMPrecCfgValue,
       "mpWredATMPrecCfgMinThreshold": mpWredATMPrecCfgMinThreshold,
       "mpWredATMPrecCfgMaxThreshold": mpWredATMPrecCfgMaxThreshold,
       "mpWredATMPrecCfgPktDropProb": mpWredATMPrecCfgPktDropProb,
       "mpWredStats": mpWredStats,
       "mpWredInterfaceStatTable": mpWredInterfaceStatTable,
       "mpWredInterfaceStatEntry": mpWredInterfaceStatEntry,
       "mpWredIFStatPrecValue": mpWredIFStatPrecValue,
       "mpWredIFStatRandomDropPkt64": mpWredIFStatRandomDropPkt64,
       "mpWredIFStatTailDropPkt64": mpWredIFStatTailDropPkt64,
       "mpWredIFStatTransmitPkt64": mpWredIFStatTransmitPkt64,
       "mpWredFrameRelayVCStatTable": mpWredFrameRelayVCStatTable,
       "mpWredFrameRelayVCStatEntry": mpWredFrameRelayVCStatEntry,
       "mpWredFRStatPrecValue": mpWredFRStatPrecValue,
       "mpWredFRStatRandomDropPkt64": mpWredFRStatRandomDropPkt64,
       "mpWredFRStatTailDropPkt64": mpWredFRStatTailDropPkt64,
       "mpWredFRStatTransmitPkt64": mpWredFRStatTransmitPkt64,
       "mpWredATMPVCStatTable": mpWredATMPVCStatTable,
       "mpWredATMPVCStatEntry": mpWredATMPVCStatEntry,
       "mpWredATMStatPrecValue": mpWredATMStatPrecValue,
       "mpWredATMStatRandomDropPkt64": mpWredATMStatRandomDropPkt64,
       "mpWredATMStatTailDropPkt64": mpWredATMStatTailDropPkt64,
       "mpWredATMStatTransmitPkt64": mpWredATMStatTransmitPkt64}
)
