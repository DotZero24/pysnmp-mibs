# SNMP MIB module (MX-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-ATM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:50 2025
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

(mediatrixConfig,
 mediatrixMgmt) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixConfig",
    "mediatrixMgmt")

(MxEnableState,) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

atmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300)
)
if mibBuilder.loadTexts:
    atmMIB.setRevisions(
        ("2008-08-25 00:00",
         "2005-01-27 00:00",
         "2005-01-31 00:00",
         "2005-02-08 00:00",
         "2005-09-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtmStatus_ObjectIdentity = ObjectIdentity
atmStatus = _AtmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 150)
)
_Aal5Stats_ObjectIdentity = ObjectIdentity
aal5Stats = _Aal5Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 150, 200)
)
_Aal5TxPdu_Type = Unsigned32
_Aal5TxPdu_Object = MibScalar
aal5TxPdu = _Aal5TxPdu_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 150, 200, 50),
    _Aal5TxPdu_Type()
)
aal5TxPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5TxPdu.setStatus("current")
_Aal5RxPdu_Type = Unsigned32
_Aal5RxPdu_Object = MibScalar
aal5RxPdu = _Aal5RxPdu_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 150, 200, 100),
    _Aal5RxPdu_Type()
)
aal5RxPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5RxPdu.setStatus("current")
_Aal5TxTotalBytes_Type = Unsigned32
_Aal5TxTotalBytes_Object = MibScalar
aal5TxTotalBytes = _Aal5TxTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 150, 200, 150),
    _Aal5TxTotalBytes_Type()
)
aal5TxTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5TxTotalBytes.setStatus("current")
_Aal5RxTotalBytes_Type = Unsigned32
_Aal5RxTotalBytes_Object = MibScalar
aal5RxTotalBytes = _Aal5RxTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 150, 200, 200),
    _Aal5RxTotalBytes_Type()
)
aal5RxTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5RxTotalBytes.setStatus("current")
_Aal5TxTotalErrorCounts_Type = Unsigned32
_Aal5TxTotalErrorCounts_Object = MibScalar
aal5TxTotalErrorCounts = _Aal5TxTotalErrorCounts_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 150, 200, 250),
    _Aal5TxTotalErrorCounts_Type()
)
aal5TxTotalErrorCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5TxTotalErrorCounts.setStatus("current")
_Aal5RxTotalErrorCounts_Type = Unsigned32
_Aal5RxTotalErrorCounts_Object = MibScalar
aal5RxTotalErrorCounts = _Aal5RxTotalErrorCounts_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 150, 200, 300),
    _Aal5RxTotalErrorCounts_Type()
)
aal5RxTotalErrorCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5RxTotalErrorCounts.setStatus("current")
_OamStats_ObjectIdentity = ObjectIdentity
oamStats = _OamStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 150, 250)
)
_OamNearEndF5LoopBackCount_Type = Unsigned32
_OamNearEndF5LoopBackCount_Object = MibScalar
oamNearEndF5LoopBackCount = _OamNearEndF5LoopBackCount_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 150, 250, 50),
    _OamNearEndF5LoopBackCount_Type()
)
oamNearEndF5LoopBackCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oamNearEndF5LoopBackCount.setStatus("current")
_OamNearEndF4LoopBackCount_Type = Unsigned32
_OamNearEndF4LoopBackCount_Object = MibScalar
oamNearEndF4LoopBackCount = _OamNearEndF4LoopBackCount_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 150, 250, 100),
    _OamNearEndF4LoopBackCount_Type()
)
oamNearEndF4LoopBackCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oamNearEndF4LoopBackCount.setStatus("current")
_OamFarEndF5LoopBackCount_Type = Unsigned32
_OamFarEndF5LoopBackCount_Object = MibScalar
oamFarEndF5LoopBackCount = _OamFarEndF5LoopBackCount_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 150, 250, 150),
    _OamFarEndF5LoopBackCount_Type()
)
oamFarEndF5LoopBackCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oamFarEndF5LoopBackCount.setStatus("current")
_OamFarEndF4LoopBackCount_Type = Unsigned32
_OamFarEndF4LoopBackCount_Object = MibScalar
oamFarEndF4LoopBackCount = _OamFarEndF4LoopBackCount_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 150, 250, 200),
    _OamFarEndF4LoopBackCount_Type()
)
oamFarEndF4LoopBackCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oamFarEndF4LoopBackCount.setStatus("current")
_AtmMIBObjects_ObjectIdentity = ObjectIdentity
atmMIBObjects = _AtmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1)
)
_AtmVcTable_Object = MibTable
atmVcTable = _AtmVcTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 50)
)
if mibBuilder.loadTexts:
    atmVcTable.setStatus("current")
_AtmVcEntry_Object = MibTableRow
atmVcEntry = _AtmVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 50, 5)
)
atmVcEntry.setIndexNames(
    (0, "MX-ATM-MIB", "atmVcIndex"),
)
if mibBuilder.loadTexts:
    atmVcEntry.setStatus("current")
_AtmVcIndex_Type = Unsigned32
_AtmVcIndex_Object = MibTableColumn
atmVcIndex = _AtmVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 50, 5, 50),
    _AtmVcIndex_Type()
)
atmVcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcIndex.setStatus("current")


class _AtmVcName_Type(OctetString):
    """Custom type atmVcName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtmVcName_Type.__name__ = "OctetString"
_AtmVcName_Object = MibTableColumn
atmVcName = _AtmVcName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 50, 5, 55),
    _AtmVcName_Type()
)
atmVcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmVcName.setStatus("current")


class _AtmVcEnable_Type(MxEnableState):
    """Custom type atmVcEnable based on MxEnableState"""
    defaultValue = 0


_AtmVcEnable_Type.__name__ = "MxEnableState"
_AtmVcEnable_Object = MibTableColumn
atmVcEnable = _AtmVcEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 50, 5, 60),
    _AtmVcEnable_Type()
)
atmVcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmVcEnable.setStatus("current")


class _AtmVcType_Type(Integer32):
    """Custom type atmVcType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 0),
          ("wan", 1))
    )


_AtmVcType_Type.__name__ = "Integer32"
_AtmVcType_Object = MibTableColumn
atmVcType = _AtmVcType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 50, 5, 65),
    _AtmVcType_Type()
)
atmVcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmVcType.setStatus("current")


class _AtmVcInUse_Type(Integer32):
    """Custom type atmVcInUse based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notUsed", 0),
          ("inUse", 1))
    )


_AtmVcInUse_Type.__name__ = "Integer32"
_AtmVcInUse_Object = MibTableColumn
atmVcInUse = _AtmVcInUse_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 50, 5, 75),
    _AtmVcInUse_Type()
)
atmVcInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcInUse.setStatus("current")


class _AtmVpi_Type(Unsigned32):
    """Custom type atmVpi based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmVpi_Type.__name__ = "Unsigned32"
_AtmVpi_Object = MibTableColumn
atmVpi = _AtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 50, 5, 100),
    _AtmVpi_Type()
)
atmVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmVpi.setStatus("current")


class _AtmVci_Type(Unsigned32):
    """Custom type atmVci based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65535),
    )


_AtmVci_Type.__name__ = "Unsigned32"
_AtmVci_Object = MibTableColumn
atmVci = _AtmVci_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 50, 5, 150),
    _AtmVci_Type()
)
atmVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmVci.setStatus("current")


class _AtmEncapsulation_Type(Integer32):
    """Custom type atmEncapsulation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("llcBridged", 0),
          ("vcMuxBridged", 1),
          ("llcRouted", 3),
          ("vcMuxRouted", 4))
    )


_AtmEncapsulation_Type.__name__ = "Integer32"
_AtmEncapsulation_Object = MibTableColumn
atmEncapsulation = _AtmEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 50, 5, 200),
    _AtmEncapsulation_Type()
)
atmEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEncapsulation.setStatus("current")


class _AtmTxTrafficClass_Type(Integer32):
    """Custom type atmTxTrafficClass based on Integer32"""
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
        *(("ubr", 1),
          ("cbr", 2),
          ("vbr", 3))
    )


_AtmTxTrafficClass_Type.__name__ = "Integer32"
_AtmTxTrafficClass_Object = MibTableColumn
atmTxTrafficClass = _AtmTxTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 50, 5, 250),
    _AtmTxTrafficClass_Type()
)
atmTxTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTxTrafficClass.setStatus("current")


class _AtmTxPeakCellRate_Type(Unsigned32):
    """Custom type atmTxPeakCellRate based on Unsigned32"""
    defaultValue = 0


_AtmTxPeakCellRate_Type.__name__ = "Unsigned32"
_AtmTxPeakCellRate_Object = MibTableColumn
atmTxPeakCellRate = _AtmTxPeakCellRate_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 50, 5, 300),
    _AtmTxPeakCellRate_Type()
)
atmTxPeakCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTxPeakCellRate.setStatus("current")


class _AtmTxSustainableCellRate_Type(Unsigned32):
    """Custom type atmTxSustainableCellRate based on Unsigned32"""
    defaultValue = 0


_AtmTxSustainableCellRate_Type.__name__ = "Unsigned32"
_AtmTxSustainableCellRate_Object = MibTableColumn
atmTxSustainableCellRate = _AtmTxSustainableCellRate_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 50, 5, 350),
    _AtmTxSustainableCellRate_Type()
)
atmTxSustainableCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTxSustainableCellRate.setStatus("current")


class _AtmTxMaximumBurstSize_Type(Unsigned32):
    """Custom type atmTxMaximumBurstSize based on Unsigned32"""
    defaultValue = 0


_AtmTxMaximumBurstSize_Type.__name__ = "Unsigned32"
_AtmTxMaximumBurstSize_Object = MibTableColumn
atmTxMaximumBurstSize = _AtmTxMaximumBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 50, 5, 400),
    _AtmTxMaximumBurstSize_Type()
)
atmTxMaximumBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTxMaximumBurstSize.setStatus("current")


class _AtmTxCellDelayVariationTolerance_Type(Unsigned32):
    """Custom type atmTxCellDelayVariationTolerance based on Unsigned32"""
    defaultValue = 0


_AtmTxCellDelayVariationTolerance_Type.__name__ = "Unsigned32"
_AtmTxCellDelayVariationTolerance_Object = MibTableColumn
atmTxCellDelayVariationTolerance = _AtmTxCellDelayVariationTolerance_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 50, 5, 450),
    _AtmTxCellDelayVariationTolerance_Type()
)
atmTxCellDelayVariationTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTxCellDelayVariationTolerance.setStatus("current")


class _AtmTxMinimumCellRate_Type(Unsigned32):
    """Custom type atmTxMinimumCellRate based on Unsigned32"""
    defaultValue = 0


_AtmTxMinimumCellRate_Type.__name__ = "Unsigned32"
_AtmTxMinimumCellRate_Object = MibTableColumn
atmTxMinimumCellRate = _AtmTxMinimumCellRate_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 50, 5, 500),
    _AtmTxMinimumCellRate_Type()
)
atmTxMinimumCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTxMinimumCellRate.setStatus("current")


class _AtmTxMaximumSdu_Type(Unsigned32):
    """Custom type atmTxMaximumSdu based on Unsigned32"""
    defaultValue = 1524


_AtmTxMaximumSdu_Type.__name__ = "Unsigned32"
_AtmTxMaximumSdu_Object = MibTableColumn
atmTxMaximumSdu = _AtmTxMaximumSdu_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 50, 5, 550),
    _AtmTxMaximumSdu_Type()
)
atmTxMaximumSdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTxMaximumSdu.setStatus("current")


class _AtmRxTrafficClass_Type(Integer32):
    """Custom type atmRxTrafficClass based on Integer32"""
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
        *(("ubr", 1),
          ("cbr", 2),
          ("vbr", 3))
    )


_AtmRxTrafficClass_Type.__name__ = "Integer32"
_AtmRxTrafficClass_Object = MibTableColumn
atmRxTrafficClass = _AtmRxTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 50, 5, 575),
    _AtmRxTrafficClass_Type()
)
atmRxTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmRxTrafficClass.setStatus("current")


class _AtmRxPeakCellRate_Type(Unsigned32):
    """Custom type atmRxPeakCellRate based on Unsigned32"""
    defaultValue = 0


_AtmRxPeakCellRate_Type.__name__ = "Unsigned32"
_AtmRxPeakCellRate_Object = MibTableColumn
atmRxPeakCellRate = _AtmRxPeakCellRate_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 50, 5, 600),
    _AtmRxPeakCellRate_Type()
)
atmRxPeakCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmRxPeakCellRate.setStatus("current")


class _AtmRxSustainableCellRate_Type(Unsigned32):
    """Custom type atmRxSustainableCellRate based on Unsigned32"""
    defaultValue = 0


_AtmRxSustainableCellRate_Type.__name__ = "Unsigned32"
_AtmRxSustainableCellRate_Object = MibTableColumn
atmRxSustainableCellRate = _AtmRxSustainableCellRate_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 50, 5, 650),
    _AtmRxSustainableCellRate_Type()
)
atmRxSustainableCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmRxSustainableCellRate.setStatus("current")


class _AtmRxMaximumBurstSize_Type(Unsigned32):
    """Custom type atmRxMaximumBurstSize based on Unsigned32"""
    defaultValue = 0


_AtmRxMaximumBurstSize_Type.__name__ = "Unsigned32"
_AtmRxMaximumBurstSize_Object = MibTableColumn
atmRxMaximumBurstSize = _AtmRxMaximumBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 50, 5, 700),
    _AtmRxMaximumBurstSize_Type()
)
atmRxMaximumBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmRxMaximumBurstSize.setStatus("current")


class _AtmRxCellDelayVariationTolerance_Type(Unsigned32):
    """Custom type atmRxCellDelayVariationTolerance based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_AtmRxCellDelayVariationTolerance_Type.__name__ = "Unsigned32"
_AtmRxCellDelayVariationTolerance_Object = MibTableColumn
atmRxCellDelayVariationTolerance = _AtmRxCellDelayVariationTolerance_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 50, 5, 750),
    _AtmRxCellDelayVariationTolerance_Type()
)
atmRxCellDelayVariationTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmRxCellDelayVariationTolerance.setStatus("current")


class _AtmRxMinimumCellRate_Type(Unsigned32):
    """Custom type atmRxMinimumCellRate based on Unsigned32"""
    defaultValue = 0


_AtmRxMinimumCellRate_Type.__name__ = "Unsigned32"
_AtmRxMinimumCellRate_Object = MibTableColumn
atmRxMinimumCellRate = _AtmRxMinimumCellRate_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 50, 5, 800),
    _AtmRxMinimumCellRate_Type()
)
atmRxMinimumCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmRxMinimumCellRate.setStatus("current")


class _AtmRxMaximumSdu_Type(Unsigned32):
    """Custom type atmRxMaximumSdu based on Unsigned32"""
    defaultValue = 1524


_AtmRxMaximumSdu_Type.__name__ = "Unsigned32"
_AtmRxMaximumSdu_Object = MibTableColumn
atmRxMaximumSdu = _AtmRxMaximumSdu_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 50, 5, 850),
    _AtmRxMaximumSdu_Type()
)
atmRxMaximumSdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmRxMaximumSdu.setStatus("current")
_OamTools_ObjectIdentity = ObjectIdentity
oamTools = _OamTools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 100)
)


class _OamResult_Type(Integer32):
    """Custom type oamResult based on Integer32"""
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
        *(("failed", 0),
          ("success", 1),
          ("pending", 2),
          ("notStarted", 3))
    )


_OamResult_Type.__name__ = "Integer32"
_OamResult_Object = MibScalar
oamResult = _OamResult_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 100, 50),
    _OamResult_Type()
)
oamResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oamResult.setStatus("current")


class _GenerateOamPing_Type(Integer32):
    """Custom type generateOamPing based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("ping", 1))
    )


_GenerateOamPing_Type.__name__ = "Integer32"
_GenerateOamPing_Object = MibScalar
generateOamPing = _GenerateOamPing_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 100, 100),
    _GenerateOamPing_Type()
)
generateOamPing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generateOamPing.setStatus("current")
_OamToolsParameters_ObjectIdentity = ObjectIdentity
oamToolsParameters = _OamToolsParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 100, 1000)
)


class _OamPingType_Type(Integer32):
    """Custom type oamPingType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("f4OamPing", 0),
          ("f5OamPing", 1))
    )


_OamPingType_Type.__name__ = "Integer32"
_OamPingType_Object = MibScalar
oamPingType = _OamPingType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 100, 1000, 100),
    _OamPingType_Type()
)
oamPingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oamPingType.setStatus("current")


class _OamVpi_Type(Unsigned32):
    """Custom type oamVpi based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OamVpi_Type.__name__ = "Unsigned32"
_OamVpi_Object = MibScalar
oamVpi = _OamVpi_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 100, 1000, 150),
    _OamVpi_Type()
)
oamVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oamVpi.setStatus("current")


class _OamVci_Type(Unsigned32):
    """Custom type oamVci based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OamVci_Type.__name__ = "Unsigned32"
_OamVci_Object = MibScalar
oamVci = _OamVci_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 100, 1000, 200),
    _OamVci_Type()
)
oamVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oamVci.setStatus("current")


class _OamMode_Type(Integer32):
    """Custom type oamMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("segmented", 0),
          ("endToEnd", 1))
    )


_OamMode_Type.__name__ = "Integer32"
_OamMode_Object = MibScalar
oamMode = _OamMode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 100, 1000, 250),
    _OamMode_Type()
)
oamMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oamMode.setStatus("current")


class _OamTimeOut_Type(Unsigned32):
    """Custom type oamTimeOut based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 60000),
    )


_OamTimeOut_Type.__name__ = "Unsigned32"
_OamTimeOut_Object = MibScalar
oamTimeOut = _OamTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 1, 100, 1000, 300),
    _OamTimeOut_Type()
)
oamTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oamTimeOut.setStatus("current")
_AtmConformance_ObjectIdentity = ObjectIdentity
atmConformance = _AtmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 2)
)
_AtmCompliances_ObjectIdentity = ObjectIdentity
atmCompliances = _AtmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 2, 1)
)
_AtmGroups_ObjectIdentity = ObjectIdentity
atmGroups = _AtmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 2, 5)
)

# Managed Objects groups

atmVcVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 2, 5, 50)
)
atmVcVer1.setObjects(
      *(("MX-ATM-MIB", "atmVcIndex"),
        ("MX-ATM-MIB", "atmVcInUse"),
        ("MX-ATM-MIB", "atmVpi"),
        ("MX-ATM-MIB", "atmVci"),
        ("MX-ATM-MIB", "atmEncapsulation"),
        ("MX-ATM-MIB", "atmTxTrafficClass"),
        ("MX-ATM-MIB", "atmTxPeakCellRate"),
        ("MX-ATM-MIB", "atmTxSustainableCellRate"),
        ("MX-ATM-MIB", "atmTxMaximumBurstSize"),
        ("MX-ATM-MIB", "atmTxCellDelayVariationTolerance"),
        ("MX-ATM-MIB", "atmTxMinimumCellRate"),
        ("MX-ATM-MIB", "atmTxMaximumSdu"),
        ("MX-ATM-MIB", "atmRxTrafficClass"),
        ("MX-ATM-MIB", "atmRxPeakCellRate"),
        ("MX-ATM-MIB", "atmRxSustainableCellRate"),
        ("MX-ATM-MIB", "atmRxMaximumBurstSize"),
        ("MX-ATM-MIB", "atmRxCellDelayVariationTolerance"),
        ("MX-ATM-MIB", "atmRxMinimumCellRate"),
        ("MX-ATM-MIB", "atmRxMaximumSdu"))
)
if mibBuilder.loadTexts:
    atmVcVer1.setStatus("current")

atmOamVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 2, 5, 100)
)
atmOamVer1.setObjects(
      *(("MX-ATM-MIB", "oamResult"),
        ("MX-ATM-MIB", "generateOamPing"),
        ("MX-ATM-MIB", "oamPingType"),
        ("MX-ATM-MIB", "oamVpi"),
        ("MX-ATM-MIB", "oamVci"),
        ("MX-ATM-MIB", "oamMode"),
        ("MX-ATM-MIB", "oamTimeOut"))
)
if mibBuilder.loadTexts:
    atmOamVer1.setStatus("current")

atmStatusVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 2, 5, 150)
)
atmStatusVer1.setObjects(
      *(("MX-ATM-MIB", "aal5TxPdu"),
        ("MX-ATM-MIB", "aal5RxPdu"),
        ("MX-ATM-MIB", "aal5TxTotalBytes"),
        ("MX-ATM-MIB", "aal5RxTotalBytes"),
        ("MX-ATM-MIB", "aal5TxTotalErrorCounts"),
        ("MX-ATM-MIB", "aal5RxTotalErrorCounts"),
        ("MX-ATM-MIB", "oamNearEndF5LoopBackCount"),
        ("MX-ATM-MIB", "oamNearEndF4LoopBackCount"),
        ("MX-ATM-MIB", "oamFarEndF5LoopBackCount"),
        ("MX-ATM-MIB", "oamFarEndF4LoopBackCount"))
)
if mibBuilder.loadTexts:
    atmStatusVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

atmComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 300, 2, 1, 1)
)
atmComplVer1.setObjects(
      *(("MX-ATM-MIB", "atmVcVer1"),
        ("MX-ATM-MIB", "atmOamVer1"),
        ("MX-ATM-MIB", "atmStatusVer1"))
)
if mibBuilder.loadTexts:
    atmComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-ATM-MIB",
    **{"atmStatus": atmStatus,
       "aal5Stats": aal5Stats,
       "aal5TxPdu": aal5TxPdu,
       "aal5RxPdu": aal5RxPdu,
       "aal5TxTotalBytes": aal5TxTotalBytes,
       "aal5RxTotalBytes": aal5RxTotalBytes,
       "aal5TxTotalErrorCounts": aal5TxTotalErrorCounts,
       "aal5RxTotalErrorCounts": aal5RxTotalErrorCounts,
       "oamStats": oamStats,
       "oamNearEndF5LoopBackCount": oamNearEndF5LoopBackCount,
       "oamNearEndF4LoopBackCount": oamNearEndF4LoopBackCount,
       "oamFarEndF5LoopBackCount": oamFarEndF5LoopBackCount,
       "oamFarEndF4LoopBackCount": oamFarEndF4LoopBackCount,
       "atmMIB": atmMIB,
       "atmMIBObjects": atmMIBObjects,
       "atmVcTable": atmVcTable,
       "atmVcEntry": atmVcEntry,
       "atmVcIndex": atmVcIndex,
       "atmVcName": atmVcName,
       "atmVcEnable": atmVcEnable,
       "atmVcType": atmVcType,
       "atmVcInUse": atmVcInUse,
       "atmVpi": atmVpi,
       "atmVci": atmVci,
       "atmEncapsulation": atmEncapsulation,
       "atmTxTrafficClass": atmTxTrafficClass,
       "atmTxPeakCellRate": atmTxPeakCellRate,
       "atmTxSustainableCellRate": atmTxSustainableCellRate,
       "atmTxMaximumBurstSize": atmTxMaximumBurstSize,
       "atmTxCellDelayVariationTolerance": atmTxCellDelayVariationTolerance,
       "atmTxMinimumCellRate": atmTxMinimumCellRate,
       "atmTxMaximumSdu": atmTxMaximumSdu,
       "atmRxTrafficClass": atmRxTrafficClass,
       "atmRxPeakCellRate": atmRxPeakCellRate,
       "atmRxSustainableCellRate": atmRxSustainableCellRate,
       "atmRxMaximumBurstSize": atmRxMaximumBurstSize,
       "atmRxCellDelayVariationTolerance": atmRxCellDelayVariationTolerance,
       "atmRxMinimumCellRate": atmRxMinimumCellRate,
       "atmRxMaximumSdu": atmRxMaximumSdu,
       "oamTools": oamTools,
       "oamResult": oamResult,
       "generateOamPing": generateOamPing,
       "oamToolsParameters": oamToolsParameters,
       "oamPingType": oamPingType,
       "oamVpi": oamVpi,
       "oamVci": oamVci,
       "oamMode": oamMode,
       "oamTimeOut": oamTimeOut,
       "atmConformance": atmConformance,
       "atmCompliances": atmCompliances,
       "atmComplVer1": atmComplVer1,
       "atmGroups": atmGroups,
       "atmVcVer1": atmVcVer1,
       "atmOamVer1": atmOamVer1,
       "atmStatusVer1": atmStatusVer1}
)
