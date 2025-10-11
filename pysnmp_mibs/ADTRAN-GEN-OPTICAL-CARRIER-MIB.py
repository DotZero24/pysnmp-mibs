# SNMP MIB module (ADTRAN-GEN-OPTICAL-CARRIER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GEN-OPTICAL-CARRIER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:13 2025
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

(adGenSubSlotProdInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-SUB-MODULE-MIB",
    "adGenSubSlotProdInfoIndex")

(adGenOpticalCarrier,
 adGenOpticalCarrierID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenOpticalCarrier",
    "adGenOpticalCarrierID")

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

adGenOpticalCarrierMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 40, 1)
)
if mibBuilder.loadTexts:
    adGenOpticalCarrierMIB.setRevisions(
        ("2012-01-12 00:00",
         "2011-05-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenOpticalCarrierProduct_ObjectIdentity = ObjectIdentity
adGenOpticalCarrierProduct = _AdGenOpticalCarrierProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 40, 1)
)
_AdGenOpticalCarrierProductTable_Object = MibTable
adGenOpticalCarrierProductTable = _AdGenOpticalCarrierProductTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 40, 1, 1)
)
if mibBuilder.loadTexts:
    adGenOpticalCarrierProductTable.setStatus("current")
_AdGenOpticalCarrierProductEntry_Object = MibTableRow
adGenOpticalCarrierProductEntry = _AdGenOpticalCarrierProductEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 40, 1, 1, 1)
)
adGenOpticalCarrierProductEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENSLOT-SUB-MODULE-MIB", "adGenSubSlotProdInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenOpticalCarrierProductEntry.setStatus("current")


class _AdGenOpticalCarrierProdType_Type(Integer32):
    """Custom type adGenOpticalCarrierProdType based on Integer32"""
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
        *(("invalid", 1),
          ("cwdmMUX", 2),
          ("dwdmMUX", 3),
          ("cwdmDEMUX", 4),
          ("dwdmDEMUX", 5),
          ("cwdmOADM", 6),
          ("dwdmOADM", 7),
          ("oscFILTER", 8))
    )


_AdGenOpticalCarrierProdType_Type.__name__ = "Integer32"
_AdGenOpticalCarrierProdType_Object = MibTableColumn
adGenOpticalCarrierProdType = _AdGenOpticalCarrierProdType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 40, 1, 1, 1, 1),
    _AdGenOpticalCarrierProdType_Type()
)
adGenOpticalCarrierProdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalCarrierProdType.setStatus("current")


class _AdGenOpticalCarrierProdGridSpacing_Type(Integer32):
    """Custom type adGenOpticalCarrierProdGridSpacing based on Integer32"""
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
        *(("invalid", 1),
          ("allRange", 2),
          ("twentyFiveGHz", 3),
          ("fiftyGHz", 4),
          ("oneHundredGHz", 5))
    )


_AdGenOpticalCarrierProdGridSpacing_Type.__name__ = "Integer32"
_AdGenOpticalCarrierProdGridSpacing_Object = MibTableColumn
adGenOpticalCarrierProdGridSpacing = _AdGenOpticalCarrierProdGridSpacing_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 40, 1, 1, 1, 2),
    _AdGenOpticalCarrierProdGridSpacing_Type()
)
adGenOpticalCarrierProdGridSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalCarrierProdGridSpacing.setStatus("current")
_AdGenOpticalCarrierProdNumOfPorts_Type = Integer32
_AdGenOpticalCarrierProdNumOfPorts_Object = MibTableColumn
adGenOpticalCarrierProdNumOfPorts = _AdGenOpticalCarrierProdNumOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 40, 1, 1, 1, 3),
    _AdGenOpticalCarrierProdNumOfPorts_Type()
)
adGenOpticalCarrierProdNumOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalCarrierProdNumOfPorts.setStatus("current")
_AdGenOpticalCarrierProductPortTable_Object = MibTable
adGenOpticalCarrierProductPortTable = _AdGenOpticalCarrierProductPortTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 40, 1, 2)
)
if mibBuilder.loadTexts:
    adGenOpticalCarrierProductPortTable.setStatus("current")
_AdGenOpticalCarrierProductPortEntry_Object = MibTableRow
adGenOpticalCarrierProductPortEntry = _AdGenOpticalCarrierProductPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 40, 1, 2, 1)
)
adGenOpticalCarrierProductPortEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENSLOT-SUB-MODULE-MIB", "adGenSubSlotProdInfoIndex"),
    (0, "ADTRAN-GEN-OPTICAL-CARRIER-MIB", "adGenOpticalCarrierProdPortInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenOpticalCarrierProductPortEntry.setStatus("current")
_AdGenOpticalCarrierProdPortInfoIndex_Type = Integer32
_AdGenOpticalCarrierProdPortInfoIndex_Object = MibTableColumn
adGenOpticalCarrierProdPortInfoIndex = _AdGenOpticalCarrierProdPortInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 40, 1, 2, 1, 1),
    _AdGenOpticalCarrierProdPortInfoIndex_Type()
)
adGenOpticalCarrierProdPortInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenOpticalCarrierProdPortInfoIndex.setStatus("current")


class _AdGenOpticalCarrierProdPortType_Type(Integer32):
    """Custom type adGenOpticalCarrierProdPortType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("add", 2),
          ("drop", 3),
          ("commonMUX", 4),
          ("commonDEMUX", 5),
          ("expressMUX", 6),
          ("expressDEMUX", 7),
          ("commonRX", 8),
          ("commonTX", 9),
          ("osc", 10))
    )


_AdGenOpticalCarrierProdPortType_Type.__name__ = "Integer32"
_AdGenOpticalCarrierProdPortType_Object = MibTableColumn
adGenOpticalCarrierProdPortType = _AdGenOpticalCarrierProdPortType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 40, 1, 2, 1, 2),
    _AdGenOpticalCarrierProdPortType_Type()
)
adGenOpticalCarrierProdPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalCarrierProdPortType.setStatus("current")


class _AdGenOpticalCarrierProdPortDirection_Type(Integer32):
    """Custom type adGenOpticalCarrierProdPortDirection based on Integer32"""
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
        *(("invalid", 1),
          ("in", 2),
          ("out", 3),
          ("biDirection", 4))
    )


_AdGenOpticalCarrierProdPortDirection_Type.__name__ = "Integer32"
_AdGenOpticalCarrierProdPortDirection_Object = MibTableColumn
adGenOpticalCarrierProdPortDirection = _AdGenOpticalCarrierProdPortDirection_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 40, 1, 2, 1, 3),
    _AdGenOpticalCarrierProdPortDirection_Type()
)
adGenOpticalCarrierProdPortDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalCarrierProdPortDirection.setStatus("current")
_AdGenOpticalCarrierProdPortMinWaveLengthPicoMeter_Type = Integer32
_AdGenOpticalCarrierProdPortMinWaveLengthPicoMeter_Object = MibTableColumn
adGenOpticalCarrierProdPortMinWaveLengthPicoMeter = _AdGenOpticalCarrierProdPortMinWaveLengthPicoMeter_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 40, 1, 2, 1, 4),
    _AdGenOpticalCarrierProdPortMinWaveLengthPicoMeter_Type()
)
adGenOpticalCarrierProdPortMinWaveLengthPicoMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalCarrierProdPortMinWaveLengthPicoMeter.setStatus("current")
_AdGenOpticalCarrierProdPortMaxWaveLengthPicoMeter_Type = Integer32
_AdGenOpticalCarrierProdPortMaxWaveLengthPicoMeter_Object = MibTableColumn
adGenOpticalCarrierProdPortMaxWaveLengthPicoMeter = _AdGenOpticalCarrierProdPortMaxWaveLengthPicoMeter_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 40, 1, 2, 1, 5),
    _AdGenOpticalCarrierProdPortMaxWaveLengthPicoMeter_Type()
)
adGenOpticalCarrierProdPortMaxWaveLengthPicoMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalCarrierProdPortMaxWaveLengthPicoMeter.setStatus("current")
_AdGenOpticalCarrierProdPortInsertionLossDB_Type = Integer32
_AdGenOpticalCarrierProdPortInsertionLossDB_Object = MibTableColumn
adGenOpticalCarrierProdPortInsertionLossDB = _AdGenOpticalCarrierProdPortInsertionLossDB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 40, 1, 2, 1, 6),
    _AdGenOpticalCarrierProdPortInsertionLossDB_Type()
)
adGenOpticalCarrierProdPortInsertionLossDB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalCarrierProdPortInsertionLossDB.setStatus("current")
_AdGenOpticalCarrierProdPortIfIndexReference_Type = InterfaceIndex
_AdGenOpticalCarrierProdPortIfIndexReference_Object = MibTableColumn
adGenOpticalCarrierProdPortIfIndexReference = _AdGenOpticalCarrierProdPortIfIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 40, 1, 2, 1, 7),
    _AdGenOpticalCarrierProdPortIfIndexReference_Type()
)
adGenOpticalCarrierProdPortIfIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalCarrierProdPortIfIndexReference.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GEN-OPTICAL-CARRIER-MIB",
    **{"adGenOpticalCarrierProduct": adGenOpticalCarrierProduct,
       "adGenOpticalCarrierProductTable": adGenOpticalCarrierProductTable,
       "adGenOpticalCarrierProductEntry": adGenOpticalCarrierProductEntry,
       "adGenOpticalCarrierProdType": adGenOpticalCarrierProdType,
       "adGenOpticalCarrierProdGridSpacing": adGenOpticalCarrierProdGridSpacing,
       "adGenOpticalCarrierProdNumOfPorts": adGenOpticalCarrierProdNumOfPorts,
       "adGenOpticalCarrierProductPortTable": adGenOpticalCarrierProductPortTable,
       "adGenOpticalCarrierProductPortEntry": adGenOpticalCarrierProductPortEntry,
       "adGenOpticalCarrierProdPortInfoIndex": adGenOpticalCarrierProdPortInfoIndex,
       "adGenOpticalCarrierProdPortType": adGenOpticalCarrierProdPortType,
       "adGenOpticalCarrierProdPortDirection": adGenOpticalCarrierProdPortDirection,
       "adGenOpticalCarrierProdPortMinWaveLengthPicoMeter": adGenOpticalCarrierProdPortMinWaveLengthPicoMeter,
       "adGenOpticalCarrierProdPortMaxWaveLengthPicoMeter": adGenOpticalCarrierProdPortMaxWaveLengthPicoMeter,
       "adGenOpticalCarrierProdPortInsertionLossDB": adGenOpticalCarrierProdPortInsertionLossDB,
       "adGenOpticalCarrierProdPortIfIndexReference": adGenOpticalCarrierProdPortIfIndexReference,
       "adGenOpticalCarrierMIB": adGenOpticalCarrierMIB}
)
