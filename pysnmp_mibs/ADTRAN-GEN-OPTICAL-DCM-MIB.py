# SNMP MIB module (ADTRAN-GEN-OPTICAL-DCM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GEN-OPTICAL-DCM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:34 2025
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

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adGenOpticalDCM,
 adGenOpticalDCMID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenOpticalDCM",
    "adGenOpticalDCMID")

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

adGenOpticalDCMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 42, 1)
)
if mibBuilder.loadTexts:
    adGenOpticalDCMMIB.setRevisions(
        ("2012-01-12 00:00",
         "2011-05-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenOpticalDCMProduct_ObjectIdentity = ObjectIdentity
adGenOpticalDCMProduct = _AdGenOpticalDCMProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 42, 1)
)
_AdGenOpticalDCMTable_Object = MibTable
adGenOpticalDCMTable = _AdGenOpticalDCMTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 42, 1, 1)
)
if mibBuilder.loadTexts:
    adGenOpticalDCMTable.setStatus("current")
_AdGenOpticalDCMEntry_Object = MibTableRow
adGenOpticalDCMEntry = _AdGenOpticalDCMEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 42, 1, 1, 1)
)
adGenOpticalDCMEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenOpticalDCMEntry.setStatus("current")


class _AdGenOpticalDCMType_Type(Integer32):
    """Custom type adGenOpticalDCMType based on Integer32"""
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
        *(("dcmFTwentyKM", 1),
          ("dcmFFortyKM", 2),
          ("dcmFSixtyKM", 3),
          ("dcmFEightyKM", 4),
          ("dcmBTwentyKM", 5),
          ("dcmBFortyKM", 6),
          ("dcmBSixtyKM", 7),
          ("dcmBEightyKM", 8))
    )


_AdGenOpticalDCMType_Type.__name__ = "Integer32"
_AdGenOpticalDCMType_Object = MibTableColumn
adGenOpticalDCMType = _AdGenOpticalDCMType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 42, 1, 1, 1, 1),
    _AdGenOpticalDCMType_Type()
)
adGenOpticalDCMType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalDCMType.setStatus("current")


class _AdGenOpticalDCMGridSpacing_Type(Integer32):
    """Custom type adGenOpticalDCMGridSpacing based on Integer32"""
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
        *(("allRange", 1),
          ("twentyFiveGHz", 2),
          ("fiftyGHz", 3),
          ("oneHundredGHz", 4))
    )


_AdGenOpticalDCMGridSpacing_Type.__name__ = "Integer32"
_AdGenOpticalDCMGridSpacing_Object = MibTableColumn
adGenOpticalDCMGridSpacing = _AdGenOpticalDCMGridSpacing_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 42, 1, 1, 1, 2),
    _AdGenOpticalDCMGridSpacing_Type()
)
adGenOpticalDCMGridSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalDCMGridSpacing.setStatus("current")
_AdGenOpticalDCMNumOfPorts_Type = Integer32
_AdGenOpticalDCMNumOfPorts_Object = MibTableColumn
adGenOpticalDCMNumOfPorts = _AdGenOpticalDCMNumOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 42, 1, 1, 1, 3),
    _AdGenOpticalDCMNumOfPorts_Type()
)
adGenOpticalDCMNumOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalDCMNumOfPorts.setStatus("current")
_AdGenOpticalDCMPortTable_Object = MibTable
adGenOpticalDCMPortTable = _AdGenOpticalDCMPortTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 42, 1, 2)
)
if mibBuilder.loadTexts:
    adGenOpticalDCMPortTable.setStatus("current")
_AdGenOpticalDCMPortEntry_Object = MibTableRow
adGenOpticalDCMPortEntry = _AdGenOpticalDCMPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 42, 1, 2, 1)
)
adGenOpticalDCMPortEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GEN-OPTICAL-DCM-MIB", "adGenOpticalDCMPortInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenOpticalDCMPortEntry.setStatus("current")
_AdGenOpticalDCMPortInfoIndex_Type = Integer32
_AdGenOpticalDCMPortInfoIndex_Object = MibTableColumn
adGenOpticalDCMPortInfoIndex = _AdGenOpticalDCMPortInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 42, 1, 2, 1, 1),
    _AdGenOpticalDCMPortInfoIndex_Type()
)
adGenOpticalDCMPortInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenOpticalDCMPortInfoIndex.setStatus("current")


class _AdGenOpticalDCMPortType_Type(Integer32):
    """Custom type adGenOpticalDCMPortType based on Integer32"""
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


_AdGenOpticalDCMPortType_Type.__name__ = "Integer32"
_AdGenOpticalDCMPortType_Object = MibTableColumn
adGenOpticalDCMPortType = _AdGenOpticalDCMPortType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 42, 1, 2, 1, 2),
    _AdGenOpticalDCMPortType_Type()
)
adGenOpticalDCMPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalDCMPortType.setStatus("current")


class _AdGenOpticalDCMPortDirection_Type(Integer32):
    """Custom type adGenOpticalDCMPortDirection based on Integer32"""
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


_AdGenOpticalDCMPortDirection_Type.__name__ = "Integer32"
_AdGenOpticalDCMPortDirection_Object = MibTableColumn
adGenOpticalDCMPortDirection = _AdGenOpticalDCMPortDirection_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 42, 1, 2, 1, 3),
    _AdGenOpticalDCMPortDirection_Type()
)
adGenOpticalDCMPortDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalDCMPortDirection.setStatus("current")
_AdGenOpticalDCMPortMinWaveLengthPicoMeter_Type = Integer32
_AdGenOpticalDCMPortMinWaveLengthPicoMeter_Object = MibTableColumn
adGenOpticalDCMPortMinWaveLengthPicoMeter = _AdGenOpticalDCMPortMinWaveLengthPicoMeter_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 42, 1, 2, 1, 4),
    _AdGenOpticalDCMPortMinWaveLengthPicoMeter_Type()
)
adGenOpticalDCMPortMinWaveLengthPicoMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalDCMPortMinWaveLengthPicoMeter.setStatus("current")
_AdGenOpticalDCMPortMaxWaveLengthPicoMeter_Type = Integer32
_AdGenOpticalDCMPortMaxWaveLengthPicoMeter_Object = MibTableColumn
adGenOpticalDCMPortMaxWaveLengthPicoMeter = _AdGenOpticalDCMPortMaxWaveLengthPicoMeter_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 42, 1, 2, 1, 5),
    _AdGenOpticalDCMPortMaxWaveLengthPicoMeter_Type()
)
adGenOpticalDCMPortMaxWaveLengthPicoMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalDCMPortMaxWaveLengthPicoMeter.setStatus("current")
_AdGenOpticalDCMPortInsertionLossDB_Type = Integer32
_AdGenOpticalDCMPortInsertionLossDB_Object = MibTableColumn
adGenOpticalDCMPortInsertionLossDB = _AdGenOpticalDCMPortInsertionLossDB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 42, 1, 2, 1, 6),
    _AdGenOpticalDCMPortInsertionLossDB_Type()
)
adGenOpticalDCMPortInsertionLossDB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalDCMPortInsertionLossDB.setStatus("current")
_AdGenOpticalDCMPortIfIndexReference_Type = InterfaceIndex
_AdGenOpticalDCMPortIfIndexReference_Object = MibTableColumn
adGenOpticalDCMPortIfIndexReference = _AdGenOpticalDCMPortIfIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 42, 1, 2, 1, 7),
    _AdGenOpticalDCMPortIfIndexReference_Type()
)
adGenOpticalDCMPortIfIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalDCMPortIfIndexReference.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GEN-OPTICAL-DCM-MIB",
    **{"adGenOpticalDCMProduct": adGenOpticalDCMProduct,
       "adGenOpticalDCMTable": adGenOpticalDCMTable,
       "adGenOpticalDCMEntry": adGenOpticalDCMEntry,
       "adGenOpticalDCMType": adGenOpticalDCMType,
       "adGenOpticalDCMGridSpacing": adGenOpticalDCMGridSpacing,
       "adGenOpticalDCMNumOfPorts": adGenOpticalDCMNumOfPorts,
       "adGenOpticalDCMPortTable": adGenOpticalDCMPortTable,
       "adGenOpticalDCMPortEntry": adGenOpticalDCMPortEntry,
       "adGenOpticalDCMPortInfoIndex": adGenOpticalDCMPortInfoIndex,
       "adGenOpticalDCMPortType": adGenOpticalDCMPortType,
       "adGenOpticalDCMPortDirection": adGenOpticalDCMPortDirection,
       "adGenOpticalDCMPortMinWaveLengthPicoMeter": adGenOpticalDCMPortMinWaveLengthPicoMeter,
       "adGenOpticalDCMPortMaxWaveLengthPicoMeter": adGenOpticalDCMPortMaxWaveLengthPicoMeter,
       "adGenOpticalDCMPortInsertionLossDB": adGenOpticalDCMPortInsertionLossDB,
       "adGenOpticalDCMPortIfIndexReference": adGenOpticalDCMPortIfIndexReference,
       "adGenOpticalDCMMIB": adGenOpticalDCMMIB}
)
