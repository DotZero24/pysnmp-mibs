# SNMP MIB module (ADTRAN-GENERIC-OTN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENERIC-OTN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:30:11 2025
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

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adGenOtn,
 adGenOtnID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenOtn",
    "adGenOtnID")

(adTAeSCUTrapAlarmLevel,) = mibBuilder.importSymbols(
    "ADTRAN-TAeSCUEXT1-MIB",
    "adTAeSCUTrapAlarmLevel")

(Unsigned64TC,) = mibBuilder.importSymbols(
    "APPLICATION-MIB",
    "Unsigned64TC")

(InterfaceIndex,
 ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifDescr",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adGenOtnIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 44, 1)
)
if mibBuilder.loadTexts:
    adGenOtnIdentity.setRevisions(
        ("2014-10-17 00:00",
         "2014-09-09 00:00",
         "2013-06-10 00:00",
         "2013-01-08 00:00",
         "2012-12-04 00:00",
         "2012-10-19 00:00",
         "2012-08-21 00:00",
         "2012-07-19 00:00",
         "2012-03-08 00:00",
         "2012-01-17 00:00",
         "2011-12-20 00:00",
         "2011-12-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AdGenOtnOduInterface(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d 1d 1d 1d 1d 1d 1d 2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )
    fixed_length = 9



class OtnProtGrpInterface(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d 1d 1d 1d 1d 1d 1d 1d 2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10



class OtnPayloadTypes(TextualConvention, Integer32):
    status = "current"
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("otnPort", 2),
          ("odu4", 3),
          ("odu3", 4),
          ("odu3e1", 5),
          ("odu3e2", 6),
          ("odu2", 7),
          ("odu2e", 8),
          ("odu2f", 9),
          ("odu1e", 10),
          ("odu1f", 11),
          ("odu1", 12),
          ("odu0", 13),
          ("oduflex", 14),
          ("timeslot", 15))
    )



# MIB Managed Objects in the order of their OIDs

_AdGenOtnProv_ObjectIdentity = ObjectIdentity
adGenOtnProv = _AdGenOtnProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1)
)
_AdGenOtnOtuProvTable_Object = MibTable
adGenOtnOtuProvTable = _AdGenOtnOtuProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 1)
)
if mibBuilder.loadTexts:
    adGenOtnOtuProvTable.setStatus("current")
_AdGenOtnOtuProvEntry_Object = MibTableRow
adGenOtnOtuProvEntry = _AdGenOtnOtuProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 1, 1)
)
adGenOtnOtuProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenOtnOtuProvEntry.setStatus("current")
_AdGenOtnOtuLastError_Type = DisplayString
_AdGenOtnOtuLastError_Object = MibTableColumn
adGenOtnOtuLastError = _AdGenOtnOtuLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 1, 1, 1),
    _AdGenOtnOtuLastError_Type()
)
adGenOtnOtuLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuLastError.setStatus("current")


class _AdGenOtnOtuMode_Type(Integer32):
    """Custom type adGenOtnOtuMode based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("otu1", 1),
          ("otu1e", 2),
          ("otu1f", 3),
          ("otu2", 4),
          ("otu2e", 5),
          ("otu2f", 6),
          ("otu3", 7),
          ("otu3e1", 8),
          ("otu3e2", 9),
          ("otu4", 10),
          ("otu2gfpf", 11),
          ("otu2gfpfs", 12))
    )


_AdGenOtnOtuMode_Type.__name__ = "Integer32"
_AdGenOtnOtuMode_Object = MibTableColumn
adGenOtnOtuMode = _AdGenOtnOtuMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 1, 1, 2),
    _AdGenOtnOtuMode_Type()
)
adGenOtnOtuMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuMode.setStatus("current")


class _AdGenOtnOtuSupportedModes_Type(Bits):
    """Custom type adGenOtnOtuSupportedModes based on Bits"""
    namedValues = NamedValues(
        *(("otu1", 0),
          ("otu1e", 1),
          ("otu1f", 2),
          ("otu2", 3),
          ("otu2e", 4),
          ("otu2f", 5),
          ("otu3", 6),
          ("otu3e1", 7),
          ("otu3e2", 8),
          ("otu4", 9),
          ("otu2gfpf", 10),
          ("otu2gfpfs", 11))
    )

_AdGenOtnOtuSupportedModes_Type.__name__ = "Bits"
_AdGenOtnOtuSupportedModes_Object = MibTableColumn
adGenOtnOtuSupportedModes = _AdGenOtnOtuSupportedModes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 1, 1, 3),
    _AdGenOtnOtuSupportedModes_Type()
)
adGenOtnOtuSupportedModes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuSupportedModes.setStatus("current")


class _AdGenOtnOtuDegradeMonitor_Type(Integer32):
    """Custom type adGenOtnOtuDegradeMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_AdGenOtnOtuDegradeMonitor_Type.__name__ = "Integer32"
_AdGenOtnOtuDegradeMonitor_Object = MibTableColumn
adGenOtnOtuDegradeMonitor = _AdGenOtnOtuDegradeMonitor_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 1, 1, 4),
    _AdGenOtnOtuDegradeMonitor_Type()
)
adGenOtnOtuDegradeMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuDegradeMonitor.setStatus("current")


class _AdGenOtnOtuDegradeThres_Type(Integer32):
    """Custom type adGenOtnOtuDegradeThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AdGenOtnOtuDegradeThres_Type.__name__ = "Integer32"
_AdGenOtnOtuDegradeThres_Object = MibTableColumn
adGenOtnOtuDegradeThres = _AdGenOtnOtuDegradeThres_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 1, 1, 5),
    _AdGenOtnOtuDegradeThres_Type()
)
adGenOtnOtuDegradeThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuDegradeThres.setStatus("current")


class _AdGenOtnOtuTraceTxSapi_Type(DisplayString):
    """Custom type adGenOtnOtuTraceTxSapi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AdGenOtnOtuTraceTxSapi_Type.__name__ = "DisplayString"
_AdGenOtnOtuTraceTxSapi_Object = MibTableColumn
adGenOtnOtuTraceTxSapi = _AdGenOtnOtuTraceTxSapi_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 1, 1, 6),
    _AdGenOtnOtuTraceTxSapi_Type()
)
adGenOtnOtuTraceTxSapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuTraceTxSapi.setStatus("current")


class _AdGenOtnOtuTraceTxDapi_Type(DisplayString):
    """Custom type adGenOtnOtuTraceTxDapi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AdGenOtnOtuTraceTxDapi_Type.__name__ = "DisplayString"
_AdGenOtnOtuTraceTxDapi_Object = MibTableColumn
adGenOtnOtuTraceTxDapi = _AdGenOtnOtuTraceTxDapi_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 1, 1, 7),
    _AdGenOtnOtuTraceTxDapi_Type()
)
adGenOtnOtuTraceTxDapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuTraceTxDapi.setStatus("current")


class _AdGenOtnOtuTraceTxOperatorSpec_Type(DisplayString):
    """Custom type adGenOtnOtuTraceTxOperatorSpec based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AdGenOtnOtuTraceTxOperatorSpec_Type.__name__ = "DisplayString"
_AdGenOtnOtuTraceTxOperatorSpec_Object = MibTableColumn
adGenOtnOtuTraceTxOperatorSpec = _AdGenOtnOtuTraceTxOperatorSpec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 1, 1, 8),
    _AdGenOtnOtuTraceTxOperatorSpec_Type()
)
adGenOtnOtuTraceTxOperatorSpec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuTraceTxOperatorSpec.setStatus("current")


class _AdGenOtnOtuTraceRxSapi_Type(DisplayString):
    """Custom type adGenOtnOtuTraceRxSapi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AdGenOtnOtuTraceRxSapi_Type.__name__ = "DisplayString"
_AdGenOtnOtuTraceRxSapi_Object = MibTableColumn
adGenOtnOtuTraceRxSapi = _AdGenOtnOtuTraceRxSapi_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 1, 1, 9),
    _AdGenOtnOtuTraceRxSapi_Type()
)
adGenOtnOtuTraceRxSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuTraceRxSapi.setStatus("current")


class _AdGenOtnOtuTraceRxDapi_Type(DisplayString):
    """Custom type adGenOtnOtuTraceRxDapi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AdGenOtnOtuTraceRxDapi_Type.__name__ = "DisplayString"
_AdGenOtnOtuTraceRxDapi_Object = MibTableColumn
adGenOtnOtuTraceRxDapi = _AdGenOtnOtuTraceRxDapi_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 1, 1, 10),
    _AdGenOtnOtuTraceRxDapi_Type()
)
adGenOtnOtuTraceRxDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuTraceRxDapi.setStatus("current")


class _AdGenOtnOtuTraceRxOperatorSpec_Type(DisplayString):
    """Custom type adGenOtnOtuTraceRxOperatorSpec based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AdGenOtnOtuTraceRxOperatorSpec_Type.__name__ = "DisplayString"
_AdGenOtnOtuTraceRxOperatorSpec_Object = MibTableColumn
adGenOtnOtuTraceRxOperatorSpec = _AdGenOtnOtuTraceRxOperatorSpec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 1, 1, 11),
    _AdGenOtnOtuTraceRxOperatorSpec_Type()
)
adGenOtnOtuTraceRxOperatorSpec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuTraceRxOperatorSpec.setStatus("current")


class _AdGenOtnOtuTraceExpectedSapi_Type(DisplayString):
    """Custom type adGenOtnOtuTraceExpectedSapi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AdGenOtnOtuTraceExpectedSapi_Type.__name__ = "DisplayString"
_AdGenOtnOtuTraceExpectedSapi_Object = MibTableColumn
adGenOtnOtuTraceExpectedSapi = _AdGenOtnOtuTraceExpectedSapi_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 1, 1, 12),
    _AdGenOtnOtuTraceExpectedSapi_Type()
)
adGenOtnOtuTraceExpectedSapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuTraceExpectedSapi.setStatus("current")


class _AdGenOtnOtuTraceExpectedDapi_Type(DisplayString):
    """Custom type adGenOtnOtuTraceExpectedDapi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AdGenOtnOtuTraceExpectedDapi_Type.__name__ = "DisplayString"
_AdGenOtnOtuTraceExpectedDapi_Object = MibTableColumn
adGenOtnOtuTraceExpectedDapi = _AdGenOtnOtuTraceExpectedDapi_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 1, 1, 13),
    _AdGenOtnOtuTraceExpectedDapi_Type()
)
adGenOtnOtuTraceExpectedDapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuTraceExpectedDapi.setStatus("current")


class _AdGenOtnOtuTraceAlarmControl_Type(Integer32):
    """Custom type adGenOtnOtuTraceAlarmControl based on Integer32"""
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
        *(("disabled", 1),
          ("sapiOnly", 2),
          ("dapiOnly", 3),
          ("either", 4))
    )


_AdGenOtnOtuTraceAlarmControl_Type.__name__ = "Integer32"
_AdGenOtnOtuTraceAlarmControl_Object = MibTableColumn
adGenOtnOtuTraceAlarmControl = _AdGenOtnOtuTraceAlarmControl_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 1, 1, 14),
    _AdGenOtnOtuTraceAlarmControl_Type()
)
adGenOtnOtuTraceAlarmControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuTraceAlarmControl.setStatus("current")
_AdGenOtnOtuTraceInsertAisEnable_Type = TruthValue
_AdGenOtnOtuTraceInsertAisEnable_Object = MibTableColumn
adGenOtnOtuTraceInsertAisEnable = _AdGenOtnOtuTraceInsertAisEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 1, 1, 15),
    _AdGenOtnOtuTraceInsertAisEnable_Type()
)
adGenOtnOtuTraceInsertAisEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuTraceInsertAisEnable.setStatus("current")


class _AdGenOtnOtuFecType_Type(Integer32):
    """Custom type adGenOtnOtuFecType based on Integer32"""
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
        *(("noFec", 1),
          ("gFec", 2),
          ("eFec", 3),
          ("ufec", 4))
    )


_AdGenOtnOtuFecType_Type.__name__ = "Integer32"
_AdGenOtnOtuFecType_Object = MibTableColumn
adGenOtnOtuFecType = _AdGenOtnOtuFecType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 1, 1, 16),
    _AdGenOtnOtuFecType_Type()
)
adGenOtnOtuFecType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuFecType.setStatus("current")


class _AdGenOtnOtuSupportedFecType_Type(Bits):
    """Custom type adGenOtnOtuSupportedFecType based on Bits"""
    namedValues = NamedValues(
        *(("noFec", 0),
          ("gFec", 1),
          ("eFec", 2),
          ("ufec", 3))
    )

_AdGenOtnOtuSupportedFecType_Type.__name__ = "Bits"
_AdGenOtnOtuSupportedFecType_Object = MibTableColumn
adGenOtnOtuSupportedFecType = _AdGenOtnOtuSupportedFecType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 1, 1, 17),
    _AdGenOtnOtuSupportedFecType_Type()
)
adGenOtnOtuSupportedFecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuSupportedFecType.setStatus("current")
_AdGenOtnOtuTraceAutoTxOperatorSpecEnable_Type = TruthValue
_AdGenOtnOtuTraceAutoTxOperatorSpecEnable_Object = MibTableColumn
adGenOtnOtuTraceAutoTxOperatorSpecEnable = _AdGenOtnOtuTraceAutoTxOperatorSpecEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 1, 1, 18),
    _AdGenOtnOtuTraceAutoTxOperatorSpecEnable_Type()
)
adGenOtnOtuTraceAutoTxOperatorSpecEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuTraceAutoTxOperatorSpecEnable.setStatus("current")


class _AdGenOtnOtuTraceTxOperatorSpecActual_Type(DisplayString):
    """Custom type adGenOtnOtuTraceTxOperatorSpecActual based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AdGenOtnOtuTraceTxOperatorSpecActual_Type.__name__ = "DisplayString"
_AdGenOtnOtuTraceTxOperatorSpecActual_Object = MibTableColumn
adGenOtnOtuTraceTxOperatorSpecActual = _AdGenOtnOtuTraceTxOperatorSpecActual_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 1, 1, 19),
    _AdGenOtnOtuTraceTxOperatorSpecActual_Type()
)
adGenOtnOtuTraceTxOperatorSpecActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuTraceTxOperatorSpecActual.setStatus("current")
_AdGenOtnOduProvTable_Object = MibTable
adGenOtnOduProvTable = _AdGenOtnOduProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 2)
)
if mibBuilder.loadTexts:
    adGenOtnOduProvTable.setStatus("current")
_AdGenOtnOduProvEntry_Object = MibTableRow
adGenOtnOduProvEntry = _AdGenOtnOduProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 2, 1)
)
adGenOtnOduProvEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
)
if mibBuilder.loadTexts:
    adGenOtnOduProvEntry.setStatus("current")
_AdGenOtnOduIndex_Type = AdGenOtnOduInterface
_AdGenOtnOduIndex_Object = MibTableColumn
adGenOtnOduIndex = _AdGenOtnOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 2, 1, 1),
    _AdGenOtnOduIndex_Type()
)
adGenOtnOduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduIndex.setStatus("current")
_AdGenOtnOduLastError_Type = DisplayString
_AdGenOtnOduLastError_Object = MibTableColumn
adGenOtnOduLastError = _AdGenOtnOduLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 2, 1, 2),
    _AdGenOtnOduLastError_Type()
)
adGenOtnOduLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduLastError.setStatus("current")


class _AdGenOtnOduAdminStatus_Type(Integer32):
    """Custom type adGenOtnOduAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_AdGenOtnOduAdminStatus_Type.__name__ = "Integer32"
_AdGenOtnOduAdminStatus_Object = MibTableColumn
adGenOtnOduAdminStatus = _AdGenOtnOduAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 2, 1, 3),
    _AdGenOtnOduAdminStatus_Type()
)
adGenOtnOduAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOtnOduAdminStatus.setStatus("current")


class _AdGenOtnOduOperStatus_Type(Integer32):
    """Custom type adGenOtnOduOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_AdGenOtnOduOperStatus_Type.__name__ = "Integer32"
_AdGenOtnOduOperStatus_Object = MibTableColumn
adGenOtnOduOperStatus = _AdGenOtnOduOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 2, 1, 4),
    _AdGenOtnOduOperStatus_Type()
)
adGenOtnOduOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduOperStatus.setStatus("current")


class _AdGenOtnOduMode_Type(Integer32):
    """Custom type adGenOtnOduMode based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("timeslot", 1),
          ("oduFlex", 2),
          ("odu0", 3),
          ("odu1", 4),
          ("odu1e", 5),
          ("odu1f", 6),
          ("odu2", 7),
          ("odu2e", 8),
          ("odu2f", 9),
          ("odu3", 10),
          ("odu3e1", 11),
          ("odu3e2", 12),
          ("odu4", 13),
          ("odu2gfpf", 14),
          ("odu2gfpfs", 15))
    )


_AdGenOtnOduMode_Type.__name__ = "Integer32"
_AdGenOtnOduMode_Object = MibTableColumn
adGenOtnOduMode = _AdGenOtnOduMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 2, 1, 5),
    _AdGenOtnOduMode_Type()
)
adGenOtnOduMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOtnOduMode.setStatus("current")


class _AdGenOtnOduSupportedModes_Type(Integer32):
    """Custom type adGenOtnOduSupportedModes based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("timeslot", 1),
          ("oduFlex", 2),
          ("odu0", 3),
          ("odu1", 4),
          ("odu1e", 5),
          ("odu1f", 6),
          ("odu2", 7),
          ("odu2e", 8),
          ("odu2f", 9),
          ("odu3", 10),
          ("odu3e1", 11),
          ("odu3e2", 12),
          ("odu4", 13),
          ("odu2gfpf", 14),
          ("odu2gfpfs", 15))
    )


_AdGenOtnOduSupportedModes_Type.__name__ = "Integer32"
_AdGenOtnOduSupportedModes_Object = MibTableColumn
adGenOtnOduSupportedModes = _AdGenOtnOduSupportedModes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 2, 1, 6),
    _AdGenOtnOduSupportedModes_Type()
)
adGenOtnOduSupportedModes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduSupportedModes.setStatus("current")


class _AdGenOtnOduTimeslotBandwidth_Type(Integer32):
    """Custom type adGenOtnOduTimeslotBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AdGenOtnOduTimeslotBandwidth_Type.__name__ = "Integer32"
_AdGenOtnOduTimeslotBandwidth_Object = MibTableColumn
adGenOtnOduTimeslotBandwidth = _AdGenOtnOduTimeslotBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 2, 1, 7),
    _AdGenOtnOduTimeslotBandwidth_Type()
)
adGenOtnOduTimeslotBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOtnOduTimeslotBandwidth.setStatus("current")


class _AdGenOtnOduRxPayloadLabel_Type(Integer32):
    """Custom type adGenOtnOduRxPayloadLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenOtnOduRxPayloadLabel_Type.__name__ = "Integer32"
_AdGenOtnOduRxPayloadLabel_Object = MibTableColumn
adGenOtnOduRxPayloadLabel = _AdGenOtnOduRxPayloadLabel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 2, 1, 8),
    _AdGenOtnOduRxPayloadLabel_Type()
)
adGenOtnOduRxPayloadLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduRxPayloadLabel.setStatus("current")


class _AdGenOtnOduTxPayloadLabel_Type(Integer32):
    """Custom type adGenOtnOduTxPayloadLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenOtnOduTxPayloadLabel_Type.__name__ = "Integer32"
_AdGenOtnOduTxPayloadLabel_Object = MibTableColumn
adGenOtnOduTxPayloadLabel = _AdGenOtnOduTxPayloadLabel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 2, 1, 9),
    _AdGenOtnOduTxPayloadLabel_Type()
)
adGenOtnOduTxPayloadLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduTxPayloadLabel.setStatus("current")


class _AdGenOtnOduProprietaryPayloadLabel_Type(Integer32):
    """Custom type adGenOtnOduProprietaryPayloadLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 143),
    )


_AdGenOtnOduProprietaryPayloadLabel_Type.__name__ = "Integer32"
_AdGenOtnOduProprietaryPayloadLabel_Object = MibTableColumn
adGenOtnOduProprietaryPayloadLabel = _AdGenOtnOduProprietaryPayloadLabel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 2, 1, 10),
    _AdGenOtnOduProprietaryPayloadLabel_Type()
)
adGenOtnOduProprietaryPayloadLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOtnOduProprietaryPayloadLabel.setStatus("current")


class _AdGenOtnOduDegradeMonitor_Type(Integer32):
    """Custom type adGenOtnOduDegradeMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_AdGenOtnOduDegradeMonitor_Type.__name__ = "Integer32"
_AdGenOtnOduDegradeMonitor_Object = MibTableColumn
adGenOtnOduDegradeMonitor = _AdGenOtnOduDegradeMonitor_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 2, 1, 11),
    _AdGenOtnOduDegradeMonitor_Type()
)
adGenOtnOduDegradeMonitor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOtnOduDegradeMonitor.setStatus("current")


class _AdGenOtnOduDegradeThres_Type(Integer32):
    """Custom type adGenOtnOduDegradeThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AdGenOtnOduDegradeThres_Type.__name__ = "Integer32"
_AdGenOtnOduDegradeThres_Object = MibTableColumn
adGenOtnOduDegradeThres = _AdGenOtnOduDegradeThres_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 2, 1, 12),
    _AdGenOtnOduDegradeThres_Type()
)
adGenOtnOduDegradeThres.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOtnOduDegradeThres.setStatus("current")


class _AdGenOtnOduTraceTxSapi_Type(DisplayString):
    """Custom type adGenOtnOduTraceTxSapi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AdGenOtnOduTraceTxSapi_Type.__name__ = "DisplayString"
_AdGenOtnOduTraceTxSapi_Object = MibTableColumn
adGenOtnOduTraceTxSapi = _AdGenOtnOduTraceTxSapi_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 2, 1, 13),
    _AdGenOtnOduTraceTxSapi_Type()
)
adGenOtnOduTraceTxSapi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOtnOduTraceTxSapi.setStatus("current")


class _AdGenOtnOduTraceTxDapi_Type(DisplayString):
    """Custom type adGenOtnOduTraceTxDapi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AdGenOtnOduTraceTxDapi_Type.__name__ = "DisplayString"
_AdGenOtnOduTraceTxDapi_Object = MibTableColumn
adGenOtnOduTraceTxDapi = _AdGenOtnOduTraceTxDapi_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 2, 1, 14),
    _AdGenOtnOduTraceTxDapi_Type()
)
adGenOtnOduTraceTxDapi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOtnOduTraceTxDapi.setStatus("current")


class _AdGenOtnOduTraceTxOperatorSpec_Type(DisplayString):
    """Custom type adGenOtnOduTraceTxOperatorSpec based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AdGenOtnOduTraceTxOperatorSpec_Type.__name__ = "DisplayString"
_AdGenOtnOduTraceTxOperatorSpec_Object = MibTableColumn
adGenOtnOduTraceTxOperatorSpec = _AdGenOtnOduTraceTxOperatorSpec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 2, 1, 15),
    _AdGenOtnOduTraceTxOperatorSpec_Type()
)
adGenOtnOduTraceTxOperatorSpec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOtnOduTraceTxOperatorSpec.setStatus("current")


class _AdGenOtnOduTraceRxSapi_Type(DisplayString):
    """Custom type adGenOtnOduTraceRxSapi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AdGenOtnOduTraceRxSapi_Type.__name__ = "DisplayString"
_AdGenOtnOduTraceRxSapi_Object = MibTableColumn
adGenOtnOduTraceRxSapi = _AdGenOtnOduTraceRxSapi_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 2, 1, 16),
    _AdGenOtnOduTraceRxSapi_Type()
)
adGenOtnOduTraceRxSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduTraceRxSapi.setStatus("current")


class _AdGenOtnOduTraceRxDapi_Type(DisplayString):
    """Custom type adGenOtnOduTraceRxDapi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AdGenOtnOduTraceRxDapi_Type.__name__ = "DisplayString"
_AdGenOtnOduTraceRxDapi_Object = MibTableColumn
adGenOtnOduTraceRxDapi = _AdGenOtnOduTraceRxDapi_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 2, 1, 17),
    _AdGenOtnOduTraceRxDapi_Type()
)
adGenOtnOduTraceRxDapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduTraceRxDapi.setStatus("current")


class _AdGenOtnOduTraceRxOperatorSpec_Type(DisplayString):
    """Custom type adGenOtnOduTraceRxOperatorSpec based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AdGenOtnOduTraceRxOperatorSpec_Type.__name__ = "DisplayString"
_AdGenOtnOduTraceRxOperatorSpec_Object = MibTableColumn
adGenOtnOduTraceRxOperatorSpec = _AdGenOtnOduTraceRxOperatorSpec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 2, 1, 18),
    _AdGenOtnOduTraceRxOperatorSpec_Type()
)
adGenOtnOduTraceRxOperatorSpec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduTraceRxOperatorSpec.setStatus("current")


class _AdGenOtnOduTraceExpectedSapi_Type(DisplayString):
    """Custom type adGenOtnOduTraceExpectedSapi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AdGenOtnOduTraceExpectedSapi_Type.__name__ = "DisplayString"
_AdGenOtnOduTraceExpectedSapi_Object = MibTableColumn
adGenOtnOduTraceExpectedSapi = _AdGenOtnOduTraceExpectedSapi_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 2, 1, 19),
    _AdGenOtnOduTraceExpectedSapi_Type()
)
adGenOtnOduTraceExpectedSapi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOtnOduTraceExpectedSapi.setStatus("current")


class _AdGenOtnOduTraceExpectedDapi_Type(DisplayString):
    """Custom type adGenOtnOduTraceExpectedDapi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AdGenOtnOduTraceExpectedDapi_Type.__name__ = "DisplayString"
_AdGenOtnOduTraceExpectedDapi_Object = MibTableColumn
adGenOtnOduTraceExpectedDapi = _AdGenOtnOduTraceExpectedDapi_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 2, 1, 20),
    _AdGenOtnOduTraceExpectedDapi_Type()
)
adGenOtnOduTraceExpectedDapi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOtnOduTraceExpectedDapi.setStatus("current")


class _AdGenOtnOduTraceAlarmControl_Type(Integer32):
    """Custom type adGenOtnOduTraceAlarmControl based on Integer32"""
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
        *(("disabled", 1),
          ("sapiOnly", 2),
          ("dapiOnly", 3),
          ("either", 4))
    )


_AdGenOtnOduTraceAlarmControl_Type.__name__ = "Integer32"
_AdGenOtnOduTraceAlarmControl_Object = MibTableColumn
adGenOtnOduTraceAlarmControl = _AdGenOtnOduTraceAlarmControl_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 2, 1, 21),
    _AdGenOtnOduTraceAlarmControl_Type()
)
adGenOtnOduTraceAlarmControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOtnOduTraceAlarmControl.setStatus("current")
_AdGenOtnOduTraceInsertAisEnable_Type = TruthValue
_AdGenOtnOduTraceInsertAisEnable_Object = MibTableColumn
adGenOtnOduTraceInsertAisEnable = _AdGenOtnOduTraceInsertAisEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 2, 1, 22),
    _AdGenOtnOduTraceInsertAisEnable_Type()
)
adGenOtnOduTraceInsertAisEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOtnOduTraceInsertAisEnable.setStatus("current")
_AdGenOtnOduRowStatus_Type = RowStatus
_AdGenOtnOduRowStatus_Object = MibTableColumn
adGenOtnOduRowStatus = _AdGenOtnOduRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 2, 1, 23),
    _AdGenOtnOduRowStatus_Type()
)
adGenOtnOduRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOtnOduRowStatus.setStatus("current")


class _AdGenOtnOdu2Odu3AutoPayloadType_Type(Integer32):
    """Custom type adGenOtnOdu2Odu3AutoPayloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 1),
          ("enable", 2),
          ("disable", 3))
    )


_AdGenOtnOdu2Odu3AutoPayloadType_Type.__name__ = "Integer32"
_AdGenOtnOdu2Odu3AutoPayloadType_Object = MibTableColumn
adGenOtnOdu2Odu3AutoPayloadType = _AdGenOtnOdu2Odu3AutoPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 2, 1, 24),
    _AdGenOtnOdu2Odu3AutoPayloadType_Type()
)
adGenOtnOdu2Odu3AutoPayloadType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOtnOdu2Odu3AutoPayloadType.setStatus("current")
_AdGenOtnSlotProvTable_Object = MibTable
adGenOtnSlotProvTable = _AdGenOtnSlotProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 3)
)
if mibBuilder.loadTexts:
    adGenOtnSlotProvTable.setStatus("current")
_AdGenOtnSlotProvEntry_Object = MibTableRow
adGenOtnSlotProvEntry = _AdGenOtnSlotProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 3, 1)
)
adGenOtnSlotProvEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenOtnSlotProvEntry.setStatus("current")


class _AdGenOtnSlotOtuAlarmEnable_Type(Bits):
    """Custom type adGenOtnSlotOtuAlarmEnable based on Bits"""
    namedValues = NamedValues(
        *(("lossOfSignal", 0),
          ("lossOfFrame", 1),
          ("lossOfMultiFrame", 2),
          ("alarmIndicationSignal", 3),
          ("backwardDefectIndication", 4),
          ("traceIdentifierMismatch", 5),
          ("degradedSignal", 6))
    )

_AdGenOtnSlotOtuAlarmEnable_Type.__name__ = "Bits"
_AdGenOtnSlotOtuAlarmEnable_Object = MibTableColumn
adGenOtnSlotOtuAlarmEnable = _AdGenOtnSlotOtuAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 3, 1, 1),
    _AdGenOtnSlotOtuAlarmEnable_Type()
)
adGenOtnSlotOtuAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnSlotOtuAlarmEnable.setStatus("current")


class _AdGenOtnSlotOduAlarmEnable_Type(Bits):
    """Custom type adGenOtnSlotOduAlarmEnable based on Bits"""
    namedValues = NamedValues(
        *(("lossOfFrameAndMultiFrame", 0),
          ("backwardDefectIndication", 1),
          ("openConnectionIndication", 2),
          ("traceIdentifierMismatch", 3),
          ("degradedSignal", 4),
          ("payloadLabelMismatch", 5),
          ("lock", 6),
          ("alarmIndicationSignal", 7),
          ("multiplexStructureIdentifierMismatch", 8),
          ("clientSignalFail", 9),
          ("lossOfOpuMultiFrameIdentifier", 10))
    )

_AdGenOtnSlotOduAlarmEnable_Type.__name__ = "Bits"
_AdGenOtnSlotOduAlarmEnable_Object = MibTableColumn
adGenOtnSlotOduAlarmEnable = _AdGenOtnSlotOduAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 3, 1, 2),
    _AdGenOtnSlotOduAlarmEnable_Type()
)
adGenOtnSlotOduAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnSlotOduAlarmEnable.setStatus("current")
_AdGenOtnProtGroupTable_Object = MibTable
adGenOtnProtGroupTable = _AdGenOtnProtGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 4)
)
if mibBuilder.loadTexts:
    adGenOtnProtGroupTable.setStatus("current")
_AdGenOtnProtGroupEntry_Object = MibTableRow
adGenOtnProtGroupEntry = _AdGenOtnProtGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 4, 1)
)
adGenOtnProtGroupEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (1, "ADTRAN-GENERIC-OTN-MIB", "adGenOtnProtGroupName"),
)
if mibBuilder.loadTexts:
    adGenOtnProtGroupEntry.setStatus("current")


class _AdGenOtnProtGroupName_Type(DisplayString):
    """Custom type adGenOtnProtGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenOtnProtGroupName_Type.__name__ = "DisplayString"
_AdGenOtnProtGroupName_Object = MibTableColumn
adGenOtnProtGroupName = _AdGenOtnProtGroupName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 4, 1, 1),
    _AdGenOtnProtGroupName_Type()
)
adGenOtnProtGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenOtnProtGroupName.setStatus("current")


class _AdGenOtnProtGroupType_Type(Integer32):
    """Custom type adGenOtnProtGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snci", 1),
          ("sncn", 2),
          ("yCable", 3))
    )


_AdGenOtnProtGroupType_Type.__name__ = "Integer32"
_AdGenOtnProtGroupType_Object = MibTableColumn
adGenOtnProtGroupType = _AdGenOtnProtGroupType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 4, 1, 2),
    _AdGenOtnProtGroupType_Type()
)
adGenOtnProtGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOtnProtGroupType.setStatus("current")
_AdGenOtnProtGroupWorkingType_Type = OtnPayloadTypes
_AdGenOtnProtGroupWorkingType_Object = MibTableColumn
adGenOtnProtGroupWorkingType = _AdGenOtnProtGroupWorkingType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 4, 1, 3),
    _AdGenOtnProtGroupWorkingType_Type()
)
adGenOtnProtGroupWorkingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnProtGroupWorkingType.setStatus("current")
_AdGenOtnProtGroupWorkingInterface_Type = OtnProtGrpInterface
_AdGenOtnProtGroupWorkingInterface_Object = MibTableColumn
adGenOtnProtGroupWorkingInterface = _AdGenOtnProtGroupWorkingInterface_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 4, 1, 4),
    _AdGenOtnProtGroupWorkingInterface_Type()
)
adGenOtnProtGroupWorkingInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOtnProtGroupWorkingInterface.setStatus("current")
_AdGenOtnProtGroupProtectingType_Type = OtnPayloadTypes
_AdGenOtnProtGroupProtectingType_Object = MibTableColumn
adGenOtnProtGroupProtectingType = _AdGenOtnProtGroupProtectingType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 4, 1, 5),
    _AdGenOtnProtGroupProtectingType_Type()
)
adGenOtnProtGroupProtectingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOtnProtGroupProtectingType.setStatus("current")
_AdGenOtnProtGroupProtectingInterface_Type = OtnProtGrpInterface
_AdGenOtnProtGroupProtectingInterface_Object = MibTableColumn
adGenOtnProtGroupProtectingInterface = _AdGenOtnProtGroupProtectingInterface_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 4, 1, 6),
    _AdGenOtnProtGroupProtectingInterface_Type()
)
adGenOtnProtGroupProtectingInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOtnProtGroupProtectingInterface.setStatus("current")
_AdGenOtnProtGroupRowStatus_Type = RowStatus
_AdGenOtnProtGroupRowStatus_Object = MibTableColumn
adGenOtnProtGroupRowStatus = _AdGenOtnProtGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 4, 1, 7),
    _AdGenOtnProtGroupRowStatus_Type()
)
adGenOtnProtGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOtnProtGroupRowStatus.setStatus("current")
_AdGenOtnProtGroupLastProvError_Type = DisplayString
_AdGenOtnProtGroupLastProvError_Object = MibTableColumn
adGenOtnProtGroupLastProvError = _AdGenOtnProtGroupLastProvError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 4, 1, 8),
    _AdGenOtnProtGroupLastProvError_Type()
)
adGenOtnProtGroupLastProvError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnProtGroupLastProvError.setStatus("current")
_AdGenOtnProtGroupWorkIsOnline_Type = TruthValue
_AdGenOtnProtGroupWorkIsOnline_Object = MibTableColumn
adGenOtnProtGroupWorkIsOnline = _AdGenOtnProtGroupWorkIsOnline_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 4, 1, 9),
    _AdGenOtnProtGroupWorkIsOnline_Type()
)
adGenOtnProtGroupWorkIsOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnProtGroupWorkIsOnline.setStatus("current")


class _AdGenOtnProtGroupSwitchCommands_Type(Integer32):
    """Custom type adGenOtnProtGroupSwitchCommands based on Integer32"""
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
        *(("clear", 1),
          ("manualSwitchToWork", 2),
          ("manualSwitchToProt", 3),
          ("forceSwitchToWork", 4),
          ("forceSwitchToProt", 5),
          ("lockout", 6))
    )


_AdGenOtnProtGroupSwitchCommands_Type.__name__ = "Integer32"
_AdGenOtnProtGroupSwitchCommands_Object = MibTableColumn
adGenOtnProtGroupSwitchCommands = _AdGenOtnProtGroupSwitchCommands_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 4, 1, 10),
    _AdGenOtnProtGroupSwitchCommands_Type()
)
adGenOtnProtGroupSwitchCommands.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOtnProtGroupSwitchCommands.setStatus("current")


class _AdGenOtnProtGroupWorkEntityStatus_Type(Integer32):
    """Custom type adGenOtnProtGroupWorkEntityStatus based on Integer32"""
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
        *(("clear", 1),
          ("signalFaulty", 2),
          ("signalDegraded", 3),
          ("down", 4))
    )


_AdGenOtnProtGroupWorkEntityStatus_Type.__name__ = "Integer32"
_AdGenOtnProtGroupWorkEntityStatus_Object = MibTableColumn
adGenOtnProtGroupWorkEntityStatus = _AdGenOtnProtGroupWorkEntityStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 4, 1, 11),
    _AdGenOtnProtGroupWorkEntityStatus_Type()
)
adGenOtnProtGroupWorkEntityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnProtGroupWorkEntityStatus.setStatus("current")


class _AdGenOtnProtGroupProtectEntityStatus_Type(Integer32):
    """Custom type adGenOtnProtGroupProtectEntityStatus based on Integer32"""
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
        *(("clear", 1),
          ("signalFaulty", 2),
          ("signalDegraded", 3),
          ("down", 4))
    )


_AdGenOtnProtGroupProtectEntityStatus_Type.__name__ = "Integer32"
_AdGenOtnProtGroupProtectEntityStatus_Object = MibTableColumn
adGenOtnProtGroupProtectEntityStatus = _AdGenOtnProtGroupProtectEntityStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 4, 1, 12),
    _AdGenOtnProtGroupProtectEntityStatus_Type()
)
adGenOtnProtGroupProtectEntityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnProtGroupProtectEntityStatus.setStatus("current")
_AdGenOtnProtGroupRevertiveEnable_Type = TruthValue
_AdGenOtnProtGroupRevertiveEnable_Object = MibTableColumn
adGenOtnProtGroupRevertiveEnable = _AdGenOtnProtGroupRevertiveEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 4, 1, 13),
    _AdGenOtnProtGroupRevertiveEnable_Type()
)
adGenOtnProtGroupRevertiveEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOtnProtGroupRevertiveEnable.setStatus("current")


class _AdGenOtnProtGroupWaitToRestoreTime_Type(Integer32):
    """Custom type adGenOtnProtGroupWaitToRestoreTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_AdGenOtnProtGroupWaitToRestoreTime_Type.__name__ = "Integer32"
_AdGenOtnProtGroupWaitToRestoreTime_Object = MibTableColumn
adGenOtnProtGroupWaitToRestoreTime = _AdGenOtnProtGroupWaitToRestoreTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 4, 1, 14),
    _AdGenOtnProtGroupWaitToRestoreTime_Type()
)
adGenOtnProtGroupWaitToRestoreTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOtnProtGroupWaitToRestoreTime.setStatus("current")


class _AdGenOtnProtGroupOperStatus_Type(Integer32):
    """Custom type adGenOtnProtGroupOperStatus based on Integer32"""
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


_AdGenOtnProtGroupOperStatus_Type.__name__ = "Integer32"
_AdGenOtnProtGroupOperStatus_Object = MibTableColumn
adGenOtnProtGroupOperStatus = _AdGenOtnProtGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 4, 1, 15),
    _AdGenOtnProtGroupOperStatus_Type()
)
adGenOtnProtGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnProtGroupOperStatus.setStatus("current")
_AdGenOtnProtGroupStatusString_Type = DisplayString
_AdGenOtnProtGroupStatusString_Object = MibTableColumn
adGenOtnProtGroupStatusString = _AdGenOtnProtGroupStatusString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 4, 1, 16),
    _AdGenOtnProtGroupStatusString_Type()
)
adGenOtnProtGroupStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnProtGroupStatusString.setStatus("current")


class _AdGenOtnProtGroupWaitToRestoreRemainingTime_Type(Unsigned32):
    """Custom type adGenOtnProtGroupWaitToRestoreRemainingTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_AdGenOtnProtGroupWaitToRestoreRemainingTime_Type.__name__ = "Unsigned32"
_AdGenOtnProtGroupWaitToRestoreRemainingTime_Object = MibTableColumn
adGenOtnProtGroupWaitToRestoreRemainingTime = _AdGenOtnProtGroupWaitToRestoreRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 4, 1, 17),
    _AdGenOtnProtGroupWaitToRestoreRemainingTime_Type()
)
adGenOtnProtGroupWaitToRestoreRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnProtGroupWaitToRestoreRemainingTime.setStatus("current")
if mibBuilder.loadTexts:
    adGenOtnProtGroupWaitToRestoreRemainingTime.setUnits("seconds")
_AdGenOtnProtGroupLastCreateErrorTable_Object = MibTable
adGenOtnProtGroupLastCreateErrorTable = _AdGenOtnProtGroupLastCreateErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 5)
)
if mibBuilder.loadTexts:
    adGenOtnProtGroupLastCreateErrorTable.setStatus("current")
_AdGenOtnProtGroupLastCreateErrorEntry_Object = MibTableRow
adGenOtnProtGroupLastCreateErrorEntry = _AdGenOtnProtGroupLastCreateErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 5, 1)
)
adGenOtnProtGroupLastCreateErrorEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenOtnProtGroupLastCreateErrorEntry.setStatus("current")
_AdGenOtnProtGroupLastCreateError_Type = DisplayString
_AdGenOtnProtGroupLastCreateError_Object = MibTableColumn
adGenOtnProtGroupLastCreateError = _AdGenOtnProtGroupLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 1, 5, 1, 1),
    _AdGenOtnProtGroupLastCreateError_Type()
)
adGenOtnProtGroupLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnProtGroupLastCreateError.setStatus("current")
_AdGenOtnStatus_ObjectIdentity = ObjectIdentity
adGenOtnStatus = _AdGenOtnStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 2)
)
_AdGenOtnOtuStatusTable_Object = MibTable
adGenOtnOtuStatusTable = _AdGenOtnOtuStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 2, 1)
)
if mibBuilder.loadTexts:
    adGenOtnOtuStatusTable.setStatus("current")
_AdGenOtnOtuStatusEntry_Object = MibTableRow
adGenOtnOtuStatusEntry = _AdGenOtnOtuStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 2, 1, 1)
)
adGenOtnOtuStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenOtnOtuStatusEntry.setStatus("current")


class _AdGenOtnOtuAlarmStatus_Type(Bits):
    """Custom type adGenOtnOtuAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("lossOfSignal", 0),
          ("lossOfFrame", 1),
          ("lossOfMultiFrame", 2),
          ("alarmIndicationSignal", 3),
          ("backwardDefectIndication", 4),
          ("traceIdentifierMismatch", 5),
          ("degradedSignal", 6),
          ("traceIdentifierMismatchWithConsequence", 7))
    )

_AdGenOtnOtuAlarmStatus_Type.__name__ = "Bits"
_AdGenOtnOtuAlarmStatus_Object = MibTableColumn
adGenOtnOtuAlarmStatus = _AdGenOtnOtuAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 2, 1, 1, 1),
    _AdGenOtnOtuAlarmStatus_Type()
)
adGenOtnOtuAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuAlarmStatus.setStatus("current")
_AdGenOtnOduStatusTable_Object = MibTable
adGenOtnOduStatusTable = _AdGenOtnOduStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 2, 2)
)
if mibBuilder.loadTexts:
    adGenOtnOduStatusTable.setStatus("current")
_AdGenOtnOduStatusEntry_Object = MibTableRow
adGenOtnOduStatusEntry = _AdGenOtnOduStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 2, 2, 1)
)
adGenOtnOduStatusEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
)
if mibBuilder.loadTexts:
    adGenOtnOduStatusEntry.setStatus("current")


class _AdGenOtnOduAlarmStatus_Type(Bits):
    """Custom type adGenOtnOduAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("lossOfFrameAndMultiFrame", 0),
          ("backwardDefectIndication", 1),
          ("openConnectionIndication", 2),
          ("traceIdentifierMismatch", 3),
          ("degradedSignal", 4),
          ("payloadLabelMismatch", 5),
          ("lock", 6),
          ("alarmIndicationSignal", 7),
          ("multiplexStructureIdentifierMismatch", 8),
          ("traceIdentifierMismatchWithConsequence", 9),
          ("clientSignalFail", 10),
          ("lossOfOpuMultiFrameIdentifier", 11))
    )

_AdGenOtnOduAlarmStatus_Type.__name__ = "Bits"
_AdGenOtnOduAlarmStatus_Object = MibTableColumn
adGenOtnOduAlarmStatus = _AdGenOtnOduAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 2, 2, 1, 1),
    _AdGenOtnOduAlarmStatus_Type()
)
adGenOtnOduAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduAlarmStatus.setStatus("current")


class _AdGenOtnOduStatus_Type(Bits):
    """Custom type adGenOtnOduStatus based on Bits"""
    namedValues = NamedValues(
        *(("fault", 0),
          ("superordinateFault", 1),
          ("subordinateFault", 2),
          ("superordinateUnassigned", 3),
          ("subordinateInserviceOrMaintenance", 4),
          ("protected", 5),
          ("superordinateProtected", 6),
          ("subordinateProtected", 7),
          ("mapped", 8),
          ("superordinateMapped", 9),
          ("subordinateMapped", 10),
          ("crossconnected", 11),
          ("superordinateCrossConnected", 12),
          ("subordinateCrossConnected", 13))
    )

_AdGenOtnOduStatus_Type.__name__ = "Bits"
_AdGenOtnOduStatus_Object = MibTableColumn
adGenOtnOduStatus = _AdGenOtnOduStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 2, 2, 1, 2),
    _AdGenOtnOduStatus_Type()
)
adGenOtnOduStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduStatus.setStatus("current")


class _AdGenOtnOduProtGrpName_Type(DisplayString):
    """Custom type adGenOtnOduProtGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenOtnOduProtGrpName_Type.__name__ = "DisplayString"
_AdGenOtnOduProtGrpName_Object = MibTableColumn
adGenOtnOduProtGrpName = _AdGenOtnOduProtGrpName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 2, 2, 1, 3),
    _AdGenOtnOduProtGrpName_Type()
)
adGenOtnOduProtGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduProtGrpName.setStatus("current")
_AdGenOtnOduCrossConnectStatusTable_Object = MibTable
adGenOtnOduCrossConnectStatusTable = _AdGenOtnOduCrossConnectStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 2, 3)
)
if mibBuilder.loadTexts:
    adGenOtnOduCrossConnectStatusTable.setStatus("current")
_AdGenOtnOduCrossConnectStatusEntry_Object = MibTableRow
adGenOtnOduCrossConnectStatusEntry = _AdGenOtnOduCrossConnectStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 2, 3, 1)
)
adGenOtnOduCrossConnectStatusEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
    (0, "ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduCrossConnectName"),
)
if mibBuilder.loadTexts:
    adGenOtnOduCrossConnectStatusEntry.setStatus("current")


class _AdGenOtnOduCrossConnectName_Type(DisplayString):
    """Custom type adGenOtnOduCrossConnectName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenOtnOduCrossConnectName_Type.__name__ = "DisplayString"
_AdGenOtnOduCrossConnectName_Object = MibTableColumn
adGenOtnOduCrossConnectName = _AdGenOtnOduCrossConnectName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 2, 3, 1, 1),
    _AdGenOtnOduCrossConnectName_Type()
)
adGenOtnOduCrossConnectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduCrossConnectName.setStatus("current")


class _AdGenOtnOduCrossConnectStatus_Type(Integer32):
    """Custom type adGenOtnOduCrossConnectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("source", 1),
          ("destination", 2),
          ("sourceAndDestination", 3))
    )


_AdGenOtnOduCrossConnectStatus_Type.__name__ = "Integer32"
_AdGenOtnOduCrossConnectStatus_Object = MibTableColumn
adGenOtnOduCrossConnectStatus = _AdGenOtnOduCrossConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 2, 3, 1, 2),
    _AdGenOtnOduCrossConnectStatus_Type()
)
adGenOtnOduCrossConnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduCrossConnectStatus.setStatus("current")
_AdGenOtnOduMappingStatusTable_Object = MibTable
adGenOtnOduMappingStatusTable = _AdGenOtnOduMappingStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 2, 4)
)
if mibBuilder.loadTexts:
    adGenOtnOduMappingStatusTable.setStatus("current")
_AdGenOtnOduMappingStatusEntry_Object = MibTableRow
adGenOtnOduMappingStatusEntry = _AdGenOtnOduMappingStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 2, 4, 1)
)
adGenOtnOduMappingStatusEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
    (0, "ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduMappingName"),
)
if mibBuilder.loadTexts:
    adGenOtnOduMappingStatusEntry.setStatus("current")


class _AdGenOtnOduMappingName_Type(DisplayString):
    """Custom type adGenOtnOduMappingName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenOtnOduMappingName_Type.__name__ = "DisplayString"
_AdGenOtnOduMappingName_Object = MibTableColumn
adGenOtnOduMappingName = _AdGenOtnOduMappingName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 2, 4, 1, 1),
    _AdGenOtnOduMappingName_Type()
)
adGenOtnOduMappingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduMappingName.setStatus("current")


class _AdGenOtnOduMappingStatus_Type(Integer32):
    """Custom type adGenOtnOduMappingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("source", 1),
          ("destination", 2),
          ("sourceAndDestination", 3))
    )


_AdGenOtnOduMappingStatus_Type.__name__ = "Integer32"
_AdGenOtnOduMappingStatus_Object = MibTableColumn
adGenOtnOduMappingStatus = _AdGenOtnOduMappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 2, 4, 1, 2),
    _AdGenOtnOduMappingStatus_Type()
)
adGenOtnOduMappingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduMappingStatus.setStatus("current")
_AdGenOtnPmThres_ObjectIdentity = ObjectIdentity
adGenOtnPmThres = _AdGenOtnPmThres_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3)
)
_AdGenOtnOtuPmThres15MinTable_Object = MibTable
adGenOtnOtuPmThres15MinTable = _AdGenOtnOtuPmThres15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 1)
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinTable.setStatus("current")
_AdGenOtnOtuPmThres15MinEntry_Object = MibTableRow
adGenOtnOtuPmThres15MinEntry = _AdGenOtnOtuPmThres15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 1, 1)
)
adGenOtnOtuPmThres15MinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinEntry.setStatus("current")


class _AdGenOtnOtuPmThres15MinNeEB_Type(Integer32):
    """Custom type adGenOtnOtuPmThres15MinNeEB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 700000),
    )


_AdGenOtnOtuPmThres15MinNeEB_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres15MinNeEB_Object = MibTableColumn
adGenOtnOtuPmThres15MinNeEB = _AdGenOtnOtuPmThres15MinNeEB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 1, 1, 1),
    _AdGenOtnOtuPmThres15MinNeEB_Type()
)
adGenOtnOtuPmThres15MinNeEB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinNeEB.setStatus("current")


class _AdGenOtnOtuPmThres15MinNeBBE_Type(Integer32):
    """Custom type adGenOtnOtuPmThres15MinNeBBE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 700000),
    )


_AdGenOtnOtuPmThres15MinNeBBE_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres15MinNeBBE_Object = MibTableColumn
adGenOtnOtuPmThres15MinNeBBE = _AdGenOtnOtuPmThres15MinNeBBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 1, 1, 2),
    _AdGenOtnOtuPmThres15MinNeBBE_Type()
)
adGenOtnOtuPmThres15MinNeBBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinNeBBE.setStatus("current")


class _AdGenOtnOtuPmThres15MinNeBBER_Type(Integer32):
    """Custom type adGenOtnOtuPmThres15MinNeBBER based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("oneExpMinusThree", 2),
          ("oneExpMinusFour", 3),
          ("oneExpMinusFive", 4),
          ("oneExpMinusSix", 5),
          ("oneExpMinusSeven", 6),
          ("oneExpMinusEight", 7),
          ("oneExpMinusNine", 8),
          ("oneExpMinusTen", 9))
    )


_AdGenOtnOtuPmThres15MinNeBBER_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres15MinNeBBER_Object = MibTableColumn
adGenOtnOtuPmThres15MinNeBBER = _AdGenOtnOtuPmThres15MinNeBBER_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 1, 1, 3),
    _AdGenOtnOtuPmThres15MinNeBBER_Type()
)
adGenOtnOtuPmThres15MinNeBBER.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinNeBBER.setStatus("current")


class _AdGenOtnOtuPmThres15MinNeES_Type(Integer32):
    """Custom type adGenOtnOtuPmThres15MinNeES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdGenOtnOtuPmThres15MinNeES_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres15MinNeES_Object = MibTableColumn
adGenOtnOtuPmThres15MinNeES = _AdGenOtnOtuPmThres15MinNeES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 1, 1, 4),
    _AdGenOtnOtuPmThres15MinNeES_Type()
)
adGenOtnOtuPmThres15MinNeES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinNeES.setStatus("current")


class _AdGenOtnOtuPmThres15MinNeSES_Type(Integer32):
    """Custom type adGenOtnOtuPmThres15MinNeSES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdGenOtnOtuPmThres15MinNeSES_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres15MinNeSES_Object = MibTableColumn
adGenOtnOtuPmThres15MinNeSES = _AdGenOtnOtuPmThres15MinNeSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 1, 1, 5),
    _AdGenOtnOtuPmThres15MinNeSES_Type()
)
adGenOtnOtuPmThres15MinNeSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinNeSES.setStatus("current")


class _AdGenOtnOtuPmThres15MinNeESR_Type(Integer32):
    """Custom type adGenOtnOtuPmThres15MinNeESR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AdGenOtnOtuPmThres15MinNeESR_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres15MinNeESR_Object = MibTableColumn
adGenOtnOtuPmThres15MinNeESR = _AdGenOtnOtuPmThres15MinNeESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 1, 1, 6),
    _AdGenOtnOtuPmThres15MinNeESR_Type()
)
adGenOtnOtuPmThres15MinNeESR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinNeESR.setStatus("current")


class _AdGenOtnOtuPmThres15MinNeSESR_Type(Integer32):
    """Custom type adGenOtnOtuPmThres15MinNeSESR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AdGenOtnOtuPmThres15MinNeSESR_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres15MinNeSESR_Object = MibTableColumn
adGenOtnOtuPmThres15MinNeSESR = _AdGenOtnOtuPmThres15MinNeSESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 1, 1, 7),
    _AdGenOtnOtuPmThres15MinNeSESR_Type()
)
adGenOtnOtuPmThres15MinNeSESR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinNeSESR.setStatus("current")


class _AdGenOtnOtuPmThres15MinNeUAS_Type(Integer32):
    """Custom type adGenOtnOtuPmThres15MinNeUAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdGenOtnOtuPmThres15MinNeUAS_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres15MinNeUAS_Object = MibTableColumn
adGenOtnOtuPmThres15MinNeUAS = _AdGenOtnOtuPmThres15MinNeUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 1, 1, 8),
    _AdGenOtnOtuPmThres15MinNeUAS_Type()
)
adGenOtnOtuPmThres15MinNeUAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinNeUAS.setStatus("current")


class _AdGenOtnOtuPmThres15MinFeEB_Type(Integer32):
    """Custom type adGenOtnOtuPmThres15MinFeEB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 700000),
    )


_AdGenOtnOtuPmThres15MinFeEB_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres15MinFeEB_Object = MibTableColumn
adGenOtnOtuPmThres15MinFeEB = _AdGenOtnOtuPmThres15MinFeEB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 1, 1, 9),
    _AdGenOtnOtuPmThres15MinFeEB_Type()
)
adGenOtnOtuPmThres15MinFeEB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinFeEB.setStatus("current")


class _AdGenOtnOtuPmThres15MinFeBBE_Type(Integer32):
    """Custom type adGenOtnOtuPmThres15MinFeBBE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 700000),
    )


_AdGenOtnOtuPmThres15MinFeBBE_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres15MinFeBBE_Object = MibTableColumn
adGenOtnOtuPmThres15MinFeBBE = _AdGenOtnOtuPmThres15MinFeBBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 1, 1, 10),
    _AdGenOtnOtuPmThres15MinFeBBE_Type()
)
adGenOtnOtuPmThres15MinFeBBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinFeBBE.setStatus("current")


class _AdGenOtnOtuPmThres15MinFeBBER_Type(Integer32):
    """Custom type adGenOtnOtuPmThres15MinFeBBER based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("oneExpMinusThree", 2),
          ("oneExpMinusFour", 3),
          ("oneExpMinusFive", 4),
          ("oneExpMinusSix", 5),
          ("oneExpMinusSeven", 6),
          ("oneExpMinusEight", 7),
          ("oneExpMinusNine", 8),
          ("oneExpMinusTen", 9))
    )


_AdGenOtnOtuPmThres15MinFeBBER_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres15MinFeBBER_Object = MibTableColumn
adGenOtnOtuPmThres15MinFeBBER = _AdGenOtnOtuPmThres15MinFeBBER_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 1, 1, 11),
    _AdGenOtnOtuPmThres15MinFeBBER_Type()
)
adGenOtnOtuPmThres15MinFeBBER.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinFeBBER.setStatus("current")


class _AdGenOtnOtuPmThres15MinFeES_Type(Integer32):
    """Custom type adGenOtnOtuPmThres15MinFeES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdGenOtnOtuPmThres15MinFeES_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres15MinFeES_Object = MibTableColumn
adGenOtnOtuPmThres15MinFeES = _AdGenOtnOtuPmThres15MinFeES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 1, 1, 12),
    _AdGenOtnOtuPmThres15MinFeES_Type()
)
adGenOtnOtuPmThres15MinFeES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinFeES.setStatus("current")


class _AdGenOtnOtuPmThres15MinFeSES_Type(Integer32):
    """Custom type adGenOtnOtuPmThres15MinFeSES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdGenOtnOtuPmThres15MinFeSES_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres15MinFeSES_Object = MibTableColumn
adGenOtnOtuPmThres15MinFeSES = _AdGenOtnOtuPmThres15MinFeSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 1, 1, 13),
    _AdGenOtnOtuPmThres15MinFeSES_Type()
)
adGenOtnOtuPmThres15MinFeSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinFeSES.setStatus("current")


class _AdGenOtnOtuPmThres15MinFeESR_Type(Integer32):
    """Custom type adGenOtnOtuPmThres15MinFeESR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AdGenOtnOtuPmThres15MinFeESR_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres15MinFeESR_Object = MibTableColumn
adGenOtnOtuPmThres15MinFeESR = _AdGenOtnOtuPmThres15MinFeESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 1, 1, 14),
    _AdGenOtnOtuPmThres15MinFeESR_Type()
)
adGenOtnOtuPmThres15MinFeESR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinFeESR.setStatus("current")


class _AdGenOtnOtuPmThres15MinFeSESR_Type(Integer32):
    """Custom type adGenOtnOtuPmThres15MinFeSESR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AdGenOtnOtuPmThres15MinFeSESR_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres15MinFeSESR_Object = MibTableColumn
adGenOtnOtuPmThres15MinFeSESR = _AdGenOtnOtuPmThres15MinFeSESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 1, 1, 15),
    _AdGenOtnOtuPmThres15MinFeSESR_Type()
)
adGenOtnOtuPmThres15MinFeSESR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinFeSESR.setStatus("current")


class _AdGenOtnOtuPmThres15MinFeUAS_Type(Integer32):
    """Custom type adGenOtnOtuPmThres15MinFeUAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdGenOtnOtuPmThres15MinFeUAS_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres15MinFeUAS_Object = MibTableColumn
adGenOtnOtuPmThres15MinFeUAS = _AdGenOtnOtuPmThres15MinFeUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 1, 1, 16),
    _AdGenOtnOtuPmThres15MinFeUAS_Type()
)
adGenOtnOtuPmThres15MinFeUAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinFeUAS.setStatus("current")
_AdGenOtnOtuPmThres15MinFecCorrBits_Type = Unsigned64TC
_AdGenOtnOtuPmThres15MinFecCorrBits_Object = MibTableColumn
adGenOtnOtuPmThres15MinFecCorrBits = _AdGenOtnOtuPmThres15MinFecCorrBits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 1, 1, 17),
    _AdGenOtnOtuPmThres15MinFecCorrBits_Type()
)
adGenOtnOtuPmThres15MinFecCorrBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinFecCorrBits.setStatus("current")
_AdGenOtnOtuPmThres15MinFecCorrOnes_Type = Unsigned64TC
_AdGenOtnOtuPmThres15MinFecCorrOnes_Object = MibTableColumn
adGenOtnOtuPmThres15MinFecCorrOnes = _AdGenOtnOtuPmThres15MinFecCorrOnes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 1, 1, 18),
    _AdGenOtnOtuPmThres15MinFecCorrOnes_Type()
)
adGenOtnOtuPmThres15MinFecCorrOnes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinFecCorrOnes.setStatus("current")
_AdGenOtnOtuPmThres15MinFecCorrZeros_Type = Unsigned64TC
_AdGenOtnOtuPmThres15MinFecCorrZeros_Object = MibTableColumn
adGenOtnOtuPmThres15MinFecCorrZeros = _AdGenOtnOtuPmThres15MinFecCorrZeros_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 1, 1, 19),
    _AdGenOtnOtuPmThres15MinFecCorrZeros_Type()
)
adGenOtnOtuPmThres15MinFecCorrZeros.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinFecCorrZeros.setStatus("current")
_AdGenOtnOtuPmThres15MinFecUnCorrBlks_Type = Unsigned64TC
_AdGenOtnOtuPmThres15MinFecUnCorrBlks_Object = MibTableColumn
adGenOtnOtuPmThres15MinFecUnCorrBlks = _AdGenOtnOtuPmThres15MinFecUnCorrBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 1, 1, 20),
    _AdGenOtnOtuPmThres15MinFecUnCorrBlks_Type()
)
adGenOtnOtuPmThres15MinFecUnCorrBlks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinFecUnCorrBlks.setStatus("current")


class _AdGenOtnOtuPmThres15MinFecCorrBer_Type(Integer32):
    """Custom type adGenOtnOtuPmThres15MinFecCorrBer based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("oneExpMinusThree", 2),
          ("oneExpMinusFour", 3),
          ("oneExpMinusFive", 4),
          ("oneExpMinusSix", 5),
          ("oneExpMinusSeven", 6),
          ("oneExpMinusEight", 7),
          ("oneExpMinusNine", 8),
          ("oneExpMinusTen", 9))
    )


_AdGenOtnOtuPmThres15MinFecCorrBer_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres15MinFecCorrBer_Object = MibTableColumn
adGenOtnOtuPmThres15MinFecCorrBer = _AdGenOtnOtuPmThres15MinFecCorrBer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 1, 1, 21),
    _AdGenOtnOtuPmThres15MinFecCorrBer_Type()
)
adGenOtnOtuPmThres15MinFecCorrBer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinFecCorrBer.setStatus("current")
_AdGenOtnOtuPmThres24HrTable_Object = MibTable
adGenOtnOtuPmThres24HrTable = _AdGenOtnOtuPmThres24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 2)
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrTable.setStatus("current")
_AdGenOtnOtuPmThres24HrEntry_Object = MibTableRow
adGenOtnOtuPmThres24HrEntry = _AdGenOtnOtuPmThres24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 2, 1)
)
adGenOtnOtuPmThres24HrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrEntry.setStatus("current")


class _AdGenOtnOtuPmThres24HrNeEB_Type(Integer32):
    """Custom type adGenOtnOtuPmThres24HrNeEB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 70000000),
    )


_AdGenOtnOtuPmThres24HrNeEB_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres24HrNeEB_Object = MibTableColumn
adGenOtnOtuPmThres24HrNeEB = _AdGenOtnOtuPmThres24HrNeEB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 2, 1, 1),
    _AdGenOtnOtuPmThres24HrNeEB_Type()
)
adGenOtnOtuPmThres24HrNeEB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrNeEB.setStatus("current")


class _AdGenOtnOtuPmThres24HrNeBBE_Type(Integer32):
    """Custom type adGenOtnOtuPmThres24HrNeBBE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 70000000),
    )


_AdGenOtnOtuPmThres24HrNeBBE_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres24HrNeBBE_Object = MibTableColumn
adGenOtnOtuPmThres24HrNeBBE = _AdGenOtnOtuPmThres24HrNeBBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 2, 1, 2),
    _AdGenOtnOtuPmThres24HrNeBBE_Type()
)
adGenOtnOtuPmThres24HrNeBBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrNeBBE.setStatus("current")


class _AdGenOtnOtuPmThres24HrNeBBER_Type(Integer32):
    """Custom type adGenOtnOtuPmThres24HrNeBBER based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("oneExpMinusThree", 2),
          ("oneExpMinusFour", 3),
          ("oneExpMinusFive", 4),
          ("oneExpMinusSix", 5),
          ("oneExpMinusSeven", 6),
          ("oneExpMinusEight", 7),
          ("oneExpMinusNine", 8),
          ("oneExpMinusTen", 9))
    )


_AdGenOtnOtuPmThres24HrNeBBER_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres24HrNeBBER_Object = MibTableColumn
adGenOtnOtuPmThres24HrNeBBER = _AdGenOtnOtuPmThres24HrNeBBER_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 2, 1, 3),
    _AdGenOtnOtuPmThres24HrNeBBER_Type()
)
adGenOtnOtuPmThres24HrNeBBER.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrNeBBER.setStatus("current")


class _AdGenOtnOtuPmThres24HrNeES_Type(Integer32):
    """Custom type adGenOtnOtuPmThres24HrNeES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AdGenOtnOtuPmThres24HrNeES_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres24HrNeES_Object = MibTableColumn
adGenOtnOtuPmThres24HrNeES = _AdGenOtnOtuPmThres24HrNeES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 2, 1, 4),
    _AdGenOtnOtuPmThres24HrNeES_Type()
)
adGenOtnOtuPmThres24HrNeES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrNeES.setStatus("current")


class _AdGenOtnOtuPmThres24HrNeSES_Type(Integer32):
    """Custom type adGenOtnOtuPmThres24HrNeSES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AdGenOtnOtuPmThres24HrNeSES_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres24HrNeSES_Object = MibTableColumn
adGenOtnOtuPmThres24HrNeSES = _AdGenOtnOtuPmThres24HrNeSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 2, 1, 5),
    _AdGenOtnOtuPmThres24HrNeSES_Type()
)
adGenOtnOtuPmThres24HrNeSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrNeSES.setStatus("current")


class _AdGenOtnOtuPmThres24HrNeESR_Type(Integer32):
    """Custom type adGenOtnOtuPmThres24HrNeESR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AdGenOtnOtuPmThres24HrNeESR_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres24HrNeESR_Object = MibTableColumn
adGenOtnOtuPmThres24HrNeESR = _AdGenOtnOtuPmThres24HrNeESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 2, 1, 6),
    _AdGenOtnOtuPmThres24HrNeESR_Type()
)
adGenOtnOtuPmThres24HrNeESR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrNeESR.setStatus("current")


class _AdGenOtnOtuPmThres24HrNeSESR_Type(Integer32):
    """Custom type adGenOtnOtuPmThres24HrNeSESR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AdGenOtnOtuPmThres24HrNeSESR_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres24HrNeSESR_Object = MibTableColumn
adGenOtnOtuPmThres24HrNeSESR = _AdGenOtnOtuPmThres24HrNeSESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 2, 1, 7),
    _AdGenOtnOtuPmThres24HrNeSESR_Type()
)
adGenOtnOtuPmThres24HrNeSESR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrNeSESR.setStatus("current")


class _AdGenOtnOtuPmThres24HrNeUAS_Type(Integer32):
    """Custom type adGenOtnOtuPmThres24HrNeUAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AdGenOtnOtuPmThres24HrNeUAS_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres24HrNeUAS_Object = MibTableColumn
adGenOtnOtuPmThres24HrNeUAS = _AdGenOtnOtuPmThres24HrNeUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 2, 1, 8),
    _AdGenOtnOtuPmThres24HrNeUAS_Type()
)
adGenOtnOtuPmThres24HrNeUAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrNeUAS.setStatus("current")


class _AdGenOtnOtuPmThres24HrFeEB_Type(Integer32):
    """Custom type adGenOtnOtuPmThres24HrFeEB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 70000000),
    )


_AdGenOtnOtuPmThres24HrFeEB_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres24HrFeEB_Object = MibTableColumn
adGenOtnOtuPmThres24HrFeEB = _AdGenOtnOtuPmThres24HrFeEB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 2, 1, 9),
    _AdGenOtnOtuPmThres24HrFeEB_Type()
)
adGenOtnOtuPmThres24HrFeEB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrFeEB.setStatus("current")


class _AdGenOtnOtuPmThres24HrFeBBE_Type(Integer32):
    """Custom type adGenOtnOtuPmThres24HrFeBBE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 70000000),
    )


_AdGenOtnOtuPmThres24HrFeBBE_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres24HrFeBBE_Object = MibTableColumn
adGenOtnOtuPmThres24HrFeBBE = _AdGenOtnOtuPmThres24HrFeBBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 2, 1, 10),
    _AdGenOtnOtuPmThres24HrFeBBE_Type()
)
adGenOtnOtuPmThres24HrFeBBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrFeBBE.setStatus("current")


class _AdGenOtnOtuPmThres24HrFeBBER_Type(Integer32):
    """Custom type adGenOtnOtuPmThres24HrFeBBER based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("oneExpMinusThree", 2),
          ("oneExpMinusFour", 3),
          ("oneExpMinusFive", 4),
          ("oneExpMinusSix", 5),
          ("oneExpMinusSeven", 6),
          ("oneExpMinusEight", 7),
          ("oneExpMinusNine", 8),
          ("oneExpMinusTen", 9))
    )


_AdGenOtnOtuPmThres24HrFeBBER_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres24HrFeBBER_Object = MibTableColumn
adGenOtnOtuPmThres24HrFeBBER = _AdGenOtnOtuPmThres24HrFeBBER_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 2, 1, 11),
    _AdGenOtnOtuPmThres24HrFeBBER_Type()
)
adGenOtnOtuPmThres24HrFeBBER.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrFeBBER.setStatus("current")


class _AdGenOtnOtuPmThres24HrFeES_Type(Integer32):
    """Custom type adGenOtnOtuPmThres24HrFeES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AdGenOtnOtuPmThres24HrFeES_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres24HrFeES_Object = MibTableColumn
adGenOtnOtuPmThres24HrFeES = _AdGenOtnOtuPmThres24HrFeES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 2, 1, 12),
    _AdGenOtnOtuPmThres24HrFeES_Type()
)
adGenOtnOtuPmThres24HrFeES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrFeES.setStatus("current")


class _AdGenOtnOtuPmThres24HrFeSES_Type(Integer32):
    """Custom type adGenOtnOtuPmThres24HrFeSES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AdGenOtnOtuPmThres24HrFeSES_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres24HrFeSES_Object = MibTableColumn
adGenOtnOtuPmThres24HrFeSES = _AdGenOtnOtuPmThres24HrFeSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 2, 1, 13),
    _AdGenOtnOtuPmThres24HrFeSES_Type()
)
adGenOtnOtuPmThres24HrFeSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrFeSES.setStatus("current")


class _AdGenOtnOtuPmThres24HrFeESR_Type(Integer32):
    """Custom type adGenOtnOtuPmThres24HrFeESR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AdGenOtnOtuPmThres24HrFeESR_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres24HrFeESR_Object = MibTableColumn
adGenOtnOtuPmThres24HrFeESR = _AdGenOtnOtuPmThres24HrFeESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 2, 1, 14),
    _AdGenOtnOtuPmThres24HrFeESR_Type()
)
adGenOtnOtuPmThres24HrFeESR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrFeESR.setStatus("current")


class _AdGenOtnOtuPmThres24HrFeSESR_Type(Integer32):
    """Custom type adGenOtnOtuPmThres24HrFeSESR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AdGenOtnOtuPmThres24HrFeSESR_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres24HrFeSESR_Object = MibTableColumn
adGenOtnOtuPmThres24HrFeSESR = _AdGenOtnOtuPmThres24HrFeSESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 2, 1, 15),
    _AdGenOtnOtuPmThres24HrFeSESR_Type()
)
adGenOtnOtuPmThres24HrFeSESR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrFeSESR.setStatus("current")


class _AdGenOtnOtuPmThres24HrFeUAS_Type(Integer32):
    """Custom type adGenOtnOtuPmThres24HrFeUAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AdGenOtnOtuPmThres24HrFeUAS_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres24HrFeUAS_Object = MibTableColumn
adGenOtnOtuPmThres24HrFeUAS = _AdGenOtnOtuPmThres24HrFeUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 2, 1, 16),
    _AdGenOtnOtuPmThres24HrFeUAS_Type()
)
adGenOtnOtuPmThres24HrFeUAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrFeUAS.setStatus("current")
_AdGenOtnOtuPmThres24HrFecCorrBits_Type = Unsigned64TC
_AdGenOtnOtuPmThres24HrFecCorrBits_Object = MibTableColumn
adGenOtnOtuPmThres24HrFecCorrBits = _AdGenOtnOtuPmThres24HrFecCorrBits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 2, 1, 17),
    _AdGenOtnOtuPmThres24HrFecCorrBits_Type()
)
adGenOtnOtuPmThres24HrFecCorrBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrFecCorrBits.setStatus("current")
_AdGenOtnOtuPmThres24HrFecCorrOnes_Type = Unsigned64TC
_AdGenOtnOtuPmThres24HrFecCorrOnes_Object = MibTableColumn
adGenOtnOtuPmThres24HrFecCorrOnes = _AdGenOtnOtuPmThres24HrFecCorrOnes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 2, 1, 18),
    _AdGenOtnOtuPmThres24HrFecCorrOnes_Type()
)
adGenOtnOtuPmThres24HrFecCorrOnes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrFecCorrOnes.setStatus("current")
_AdGenOtnOtuPmThres24HrFecCorrZeros_Type = Unsigned64TC
_AdGenOtnOtuPmThres24HrFecCorrZeros_Object = MibTableColumn
adGenOtnOtuPmThres24HrFecCorrZeros = _AdGenOtnOtuPmThres24HrFecCorrZeros_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 2, 1, 19),
    _AdGenOtnOtuPmThres24HrFecCorrZeros_Type()
)
adGenOtnOtuPmThres24HrFecCorrZeros.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrFecCorrZeros.setStatus("current")
_AdGenOtnOtuPmThres24HrFecUnCorrBlks_Type = Unsigned64TC
_AdGenOtnOtuPmThres24HrFecUnCorrBlks_Object = MibTableColumn
adGenOtnOtuPmThres24HrFecUnCorrBlks = _AdGenOtnOtuPmThres24HrFecUnCorrBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 2, 1, 20),
    _AdGenOtnOtuPmThres24HrFecUnCorrBlks_Type()
)
adGenOtnOtuPmThres24HrFecUnCorrBlks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrFecUnCorrBlks.setStatus("current")


class _AdGenOtnOtuPmThres24HrFecCorrBer_Type(Integer32):
    """Custom type adGenOtnOtuPmThres24HrFecCorrBer based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("oneExpMinusThree", 2),
          ("oneExpMinusFour", 3),
          ("oneExpMinusFive", 4),
          ("oneExpMinusSix", 5),
          ("oneExpMinusSeven", 6),
          ("oneExpMinusEight", 7),
          ("oneExpMinusNine", 8),
          ("oneExpMinusTen", 9))
    )


_AdGenOtnOtuPmThres24HrFecCorrBer_Type.__name__ = "Integer32"
_AdGenOtnOtuPmThres24HrFecCorrBer_Object = MibTableColumn
adGenOtnOtuPmThres24HrFecCorrBer = _AdGenOtnOtuPmThres24HrFecCorrBer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 2, 1, 21),
    _AdGenOtnOtuPmThres24HrFecCorrBer_Type()
)
adGenOtnOtuPmThres24HrFecCorrBer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrFecCorrBer.setStatus("current")
_AdGenOtnOduPmThres15MinTable_Object = MibTable
adGenOtnOduPmThres15MinTable = _AdGenOtnOduPmThres15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 3)
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinTable.setStatus("current")
_AdGenOtnOduPmThres15MinEntry_Object = MibTableRow
adGenOtnOduPmThres15MinEntry = _AdGenOtnOduPmThres15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 3, 1)
)
adGenOtnOduPmThres15MinEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinEntry.setStatus("current")


class _AdGenOtnOduPmThres15MinNeEB_Type(Integer32):
    """Custom type adGenOtnOduPmThres15MinNeEB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 700000),
    )


_AdGenOtnOduPmThres15MinNeEB_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres15MinNeEB_Object = MibTableColumn
adGenOtnOduPmThres15MinNeEB = _AdGenOtnOduPmThres15MinNeEB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 3, 1, 1),
    _AdGenOtnOduPmThres15MinNeEB_Type()
)
adGenOtnOduPmThres15MinNeEB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinNeEB.setStatus("current")


class _AdGenOtnOduPmThres15MinNeBBE_Type(Integer32):
    """Custom type adGenOtnOduPmThres15MinNeBBE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 700000),
    )


_AdGenOtnOduPmThres15MinNeBBE_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres15MinNeBBE_Object = MibTableColumn
adGenOtnOduPmThres15MinNeBBE = _AdGenOtnOduPmThres15MinNeBBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 3, 1, 2),
    _AdGenOtnOduPmThres15MinNeBBE_Type()
)
adGenOtnOduPmThres15MinNeBBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinNeBBE.setStatus("current")


class _AdGenOtnOduPmThres15MinNeBBER_Type(Integer32):
    """Custom type adGenOtnOduPmThres15MinNeBBER based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("oneExpMinusThree", 2),
          ("oneExpMinusFour", 3),
          ("oneExpMinusFive", 4),
          ("oneExpMinusSix", 5),
          ("oneExpMinusSeven", 6),
          ("oneExpMinusEight", 7),
          ("oneExpMinusNine", 8),
          ("oneExpMinusTen", 9))
    )


_AdGenOtnOduPmThres15MinNeBBER_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres15MinNeBBER_Object = MibTableColumn
adGenOtnOduPmThres15MinNeBBER = _AdGenOtnOduPmThres15MinNeBBER_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 3, 1, 3),
    _AdGenOtnOduPmThres15MinNeBBER_Type()
)
adGenOtnOduPmThres15MinNeBBER.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinNeBBER.setStatus("current")


class _AdGenOtnOduPmThres15MinNeES_Type(Integer32):
    """Custom type adGenOtnOduPmThres15MinNeES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdGenOtnOduPmThres15MinNeES_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres15MinNeES_Object = MibTableColumn
adGenOtnOduPmThres15MinNeES = _AdGenOtnOduPmThres15MinNeES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 3, 1, 4),
    _AdGenOtnOduPmThres15MinNeES_Type()
)
adGenOtnOduPmThres15MinNeES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinNeES.setStatus("current")


class _AdGenOtnOduPmThres15MinNeSES_Type(Integer32):
    """Custom type adGenOtnOduPmThres15MinNeSES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdGenOtnOduPmThres15MinNeSES_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres15MinNeSES_Object = MibTableColumn
adGenOtnOduPmThres15MinNeSES = _AdGenOtnOduPmThres15MinNeSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 3, 1, 5),
    _AdGenOtnOduPmThres15MinNeSES_Type()
)
adGenOtnOduPmThres15MinNeSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinNeSES.setStatus("current")


class _AdGenOtnOduPmThres15MinNeESR_Type(Integer32):
    """Custom type adGenOtnOduPmThres15MinNeESR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AdGenOtnOduPmThres15MinNeESR_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres15MinNeESR_Object = MibTableColumn
adGenOtnOduPmThres15MinNeESR = _AdGenOtnOduPmThres15MinNeESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 3, 1, 6),
    _AdGenOtnOduPmThres15MinNeESR_Type()
)
adGenOtnOduPmThres15MinNeESR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinNeESR.setStatus("current")


class _AdGenOtnOduPmThres15MinNeSESR_Type(Integer32):
    """Custom type adGenOtnOduPmThres15MinNeSESR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AdGenOtnOduPmThres15MinNeSESR_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres15MinNeSESR_Object = MibTableColumn
adGenOtnOduPmThres15MinNeSESR = _AdGenOtnOduPmThres15MinNeSESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 3, 1, 7),
    _AdGenOtnOduPmThres15MinNeSESR_Type()
)
adGenOtnOduPmThres15MinNeSESR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinNeSESR.setStatus("current")


class _AdGenOtnOduPmThres15MinNeUAS_Type(Integer32):
    """Custom type adGenOtnOduPmThres15MinNeUAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdGenOtnOduPmThres15MinNeUAS_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres15MinNeUAS_Object = MibTableColumn
adGenOtnOduPmThres15MinNeUAS = _AdGenOtnOduPmThres15MinNeUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 3, 1, 8),
    _AdGenOtnOduPmThres15MinNeUAS_Type()
)
adGenOtnOduPmThres15MinNeUAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinNeUAS.setStatus("current")


class _AdGenOtnOduPmThres15MinFeEB_Type(Integer32):
    """Custom type adGenOtnOduPmThres15MinFeEB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 700000),
    )


_AdGenOtnOduPmThres15MinFeEB_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres15MinFeEB_Object = MibTableColumn
adGenOtnOduPmThres15MinFeEB = _AdGenOtnOduPmThres15MinFeEB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 3, 1, 9),
    _AdGenOtnOduPmThres15MinFeEB_Type()
)
adGenOtnOduPmThres15MinFeEB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinFeEB.setStatus("current")


class _AdGenOtnOduPmThres15MinFeBBE_Type(Integer32):
    """Custom type adGenOtnOduPmThres15MinFeBBE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 700000),
    )


_AdGenOtnOduPmThres15MinFeBBE_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres15MinFeBBE_Object = MibTableColumn
adGenOtnOduPmThres15MinFeBBE = _AdGenOtnOduPmThres15MinFeBBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 3, 1, 10),
    _AdGenOtnOduPmThres15MinFeBBE_Type()
)
adGenOtnOduPmThres15MinFeBBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinFeBBE.setStatus("current")


class _AdGenOtnOduPmThres15MinFeBBER_Type(Integer32):
    """Custom type adGenOtnOduPmThres15MinFeBBER based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("oneExpMinusThree", 2),
          ("oneExpMinusFour", 3),
          ("oneExpMinusFive", 4),
          ("oneExpMinusSix", 5),
          ("oneExpMinusSeven", 6),
          ("oneExpMinusEight", 7),
          ("oneExpMinusNine", 8),
          ("oneExpMinusTen", 9))
    )


_AdGenOtnOduPmThres15MinFeBBER_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres15MinFeBBER_Object = MibTableColumn
adGenOtnOduPmThres15MinFeBBER = _AdGenOtnOduPmThres15MinFeBBER_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 3, 1, 11),
    _AdGenOtnOduPmThres15MinFeBBER_Type()
)
adGenOtnOduPmThres15MinFeBBER.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinFeBBER.setStatus("current")


class _AdGenOtnOduPmThres15MinFeES_Type(Integer32):
    """Custom type adGenOtnOduPmThres15MinFeES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdGenOtnOduPmThres15MinFeES_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres15MinFeES_Object = MibTableColumn
adGenOtnOduPmThres15MinFeES = _AdGenOtnOduPmThres15MinFeES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 3, 1, 12),
    _AdGenOtnOduPmThres15MinFeES_Type()
)
adGenOtnOduPmThres15MinFeES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinFeES.setStatus("current")


class _AdGenOtnOduPmThres15MinFeSES_Type(Integer32):
    """Custom type adGenOtnOduPmThres15MinFeSES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdGenOtnOduPmThres15MinFeSES_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres15MinFeSES_Object = MibTableColumn
adGenOtnOduPmThres15MinFeSES = _AdGenOtnOduPmThres15MinFeSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 3, 1, 13),
    _AdGenOtnOduPmThres15MinFeSES_Type()
)
adGenOtnOduPmThres15MinFeSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinFeSES.setStatus("current")


class _AdGenOtnOduPmThres15MinFeESR_Type(Integer32):
    """Custom type adGenOtnOduPmThres15MinFeESR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AdGenOtnOduPmThres15MinFeESR_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres15MinFeESR_Object = MibTableColumn
adGenOtnOduPmThres15MinFeESR = _AdGenOtnOduPmThres15MinFeESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 3, 1, 14),
    _AdGenOtnOduPmThres15MinFeESR_Type()
)
adGenOtnOduPmThres15MinFeESR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinFeESR.setStatus("current")


class _AdGenOtnOduPmThres15MinFeSESR_Type(Integer32):
    """Custom type adGenOtnOduPmThres15MinFeSESR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AdGenOtnOduPmThres15MinFeSESR_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres15MinFeSESR_Object = MibTableColumn
adGenOtnOduPmThres15MinFeSESR = _AdGenOtnOduPmThres15MinFeSESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 3, 1, 15),
    _AdGenOtnOduPmThres15MinFeSESR_Type()
)
adGenOtnOduPmThres15MinFeSESR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinFeSESR.setStatus("current")


class _AdGenOtnOduPmThres15MinFeUAS_Type(Integer32):
    """Custom type adGenOtnOduPmThres15MinFeUAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdGenOtnOduPmThres15MinFeUAS_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres15MinFeUAS_Object = MibTableColumn
adGenOtnOduPmThres15MinFeUAS = _AdGenOtnOduPmThres15MinFeUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 3, 1, 16),
    _AdGenOtnOduPmThres15MinFeUAS_Type()
)
adGenOtnOduPmThres15MinFeUAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinFeUAS.setStatus("current")
_AdGenOtnOduPmThres24HrTable_Object = MibTable
adGenOtnOduPmThres24HrTable = _AdGenOtnOduPmThres24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 4)
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrTable.setStatus("current")
_AdGenOtnOduPmThres24HrEntry_Object = MibTableRow
adGenOtnOduPmThres24HrEntry = _AdGenOtnOduPmThres24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 4, 1)
)
adGenOtnOduPmThres24HrEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrEntry.setStatus("current")


class _AdGenOtnOduPmThres24HrNeEB_Type(Integer32):
    """Custom type adGenOtnOduPmThres24HrNeEB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 70000000),
    )


_AdGenOtnOduPmThres24HrNeEB_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres24HrNeEB_Object = MibTableColumn
adGenOtnOduPmThres24HrNeEB = _AdGenOtnOduPmThres24HrNeEB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 4, 1, 1),
    _AdGenOtnOduPmThres24HrNeEB_Type()
)
adGenOtnOduPmThres24HrNeEB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrNeEB.setStatus("current")


class _AdGenOtnOduPmThres24HrNeBBE_Type(Integer32):
    """Custom type adGenOtnOduPmThres24HrNeBBE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 70000000),
    )


_AdGenOtnOduPmThres24HrNeBBE_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres24HrNeBBE_Object = MibTableColumn
adGenOtnOduPmThres24HrNeBBE = _AdGenOtnOduPmThres24HrNeBBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 4, 1, 2),
    _AdGenOtnOduPmThres24HrNeBBE_Type()
)
adGenOtnOduPmThres24HrNeBBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrNeBBE.setStatus("current")


class _AdGenOtnOduPmThres24HrNeBBER_Type(Integer32):
    """Custom type adGenOtnOduPmThres24HrNeBBER based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("oneExpMinusThree", 2),
          ("oneExpMinusFour", 3),
          ("oneExpMinusFive", 4),
          ("oneExpMinusSix", 5),
          ("oneExpMinusSeven", 6),
          ("oneExpMinusEight", 7),
          ("oneExpMinusNine", 8),
          ("oneExpMinusTen", 9))
    )


_AdGenOtnOduPmThres24HrNeBBER_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres24HrNeBBER_Object = MibTableColumn
adGenOtnOduPmThres24HrNeBBER = _AdGenOtnOduPmThres24HrNeBBER_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 4, 1, 3),
    _AdGenOtnOduPmThres24HrNeBBER_Type()
)
adGenOtnOduPmThres24HrNeBBER.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrNeBBER.setStatus("current")


class _AdGenOtnOduPmThres24HrNeES_Type(Integer32):
    """Custom type adGenOtnOduPmThres24HrNeES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AdGenOtnOduPmThres24HrNeES_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres24HrNeES_Object = MibTableColumn
adGenOtnOduPmThres24HrNeES = _AdGenOtnOduPmThres24HrNeES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 4, 1, 4),
    _AdGenOtnOduPmThres24HrNeES_Type()
)
adGenOtnOduPmThres24HrNeES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrNeES.setStatus("current")


class _AdGenOtnOduPmThres24HrNeSES_Type(Integer32):
    """Custom type adGenOtnOduPmThres24HrNeSES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AdGenOtnOduPmThres24HrNeSES_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres24HrNeSES_Object = MibTableColumn
adGenOtnOduPmThres24HrNeSES = _AdGenOtnOduPmThres24HrNeSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 4, 1, 5),
    _AdGenOtnOduPmThres24HrNeSES_Type()
)
adGenOtnOduPmThres24HrNeSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrNeSES.setStatus("current")


class _AdGenOtnOduPmThres24HrNeESR_Type(Integer32):
    """Custom type adGenOtnOduPmThres24HrNeESR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AdGenOtnOduPmThres24HrNeESR_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres24HrNeESR_Object = MibTableColumn
adGenOtnOduPmThres24HrNeESR = _AdGenOtnOduPmThres24HrNeESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 4, 1, 6),
    _AdGenOtnOduPmThres24HrNeESR_Type()
)
adGenOtnOduPmThres24HrNeESR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrNeESR.setStatus("current")


class _AdGenOtnOduPmThres24HrNeSESR_Type(Integer32):
    """Custom type adGenOtnOduPmThres24HrNeSESR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AdGenOtnOduPmThres24HrNeSESR_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres24HrNeSESR_Object = MibTableColumn
adGenOtnOduPmThres24HrNeSESR = _AdGenOtnOduPmThres24HrNeSESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 4, 1, 7),
    _AdGenOtnOduPmThres24HrNeSESR_Type()
)
adGenOtnOduPmThres24HrNeSESR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrNeSESR.setStatus("current")


class _AdGenOtnOduPmThres24HrNeUAS_Type(Integer32):
    """Custom type adGenOtnOduPmThres24HrNeUAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AdGenOtnOduPmThres24HrNeUAS_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres24HrNeUAS_Object = MibTableColumn
adGenOtnOduPmThres24HrNeUAS = _AdGenOtnOduPmThres24HrNeUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 4, 1, 8),
    _AdGenOtnOduPmThres24HrNeUAS_Type()
)
adGenOtnOduPmThres24HrNeUAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrNeUAS.setStatus("current")


class _AdGenOtnOduPmThres24HrFeEB_Type(Integer32):
    """Custom type adGenOtnOduPmThres24HrFeEB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 70000000),
    )


_AdGenOtnOduPmThres24HrFeEB_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres24HrFeEB_Object = MibTableColumn
adGenOtnOduPmThres24HrFeEB = _AdGenOtnOduPmThres24HrFeEB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 4, 1, 9),
    _AdGenOtnOduPmThres24HrFeEB_Type()
)
adGenOtnOduPmThres24HrFeEB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrFeEB.setStatus("current")


class _AdGenOtnOduPmThres24HrFeBBE_Type(Integer32):
    """Custom type adGenOtnOduPmThres24HrFeBBE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 70000000),
    )


_AdGenOtnOduPmThres24HrFeBBE_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres24HrFeBBE_Object = MibTableColumn
adGenOtnOduPmThres24HrFeBBE = _AdGenOtnOduPmThres24HrFeBBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 4, 1, 10),
    _AdGenOtnOduPmThres24HrFeBBE_Type()
)
adGenOtnOduPmThres24HrFeBBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrFeBBE.setStatus("current")


class _AdGenOtnOduPmThres24HrFeBBER_Type(Integer32):
    """Custom type adGenOtnOduPmThres24HrFeBBER based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("oneExpMinusThree", 2),
          ("oneExpMinusFour", 3),
          ("oneExpMinusFive", 4),
          ("oneExpMinusSix", 5),
          ("oneExpMinusSeven", 6),
          ("oneExpMinusEight", 7),
          ("oneExpMinusNine", 8),
          ("oneExpMinusTen", 9))
    )


_AdGenOtnOduPmThres24HrFeBBER_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres24HrFeBBER_Object = MibTableColumn
adGenOtnOduPmThres24HrFeBBER = _AdGenOtnOduPmThres24HrFeBBER_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 4, 1, 11),
    _AdGenOtnOduPmThres24HrFeBBER_Type()
)
adGenOtnOduPmThres24HrFeBBER.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrFeBBER.setStatus("current")


class _AdGenOtnOduPmThres24HrFeES_Type(Integer32):
    """Custom type adGenOtnOduPmThres24HrFeES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AdGenOtnOduPmThres24HrFeES_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres24HrFeES_Object = MibTableColumn
adGenOtnOduPmThres24HrFeES = _AdGenOtnOduPmThres24HrFeES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 4, 1, 12),
    _AdGenOtnOduPmThres24HrFeES_Type()
)
adGenOtnOduPmThres24HrFeES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrFeES.setStatus("current")


class _AdGenOtnOduPmThres24HrFeSES_Type(Integer32):
    """Custom type adGenOtnOduPmThres24HrFeSES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AdGenOtnOduPmThres24HrFeSES_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres24HrFeSES_Object = MibTableColumn
adGenOtnOduPmThres24HrFeSES = _AdGenOtnOduPmThres24HrFeSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 4, 1, 13),
    _AdGenOtnOduPmThres24HrFeSES_Type()
)
adGenOtnOduPmThres24HrFeSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrFeSES.setStatus("current")


class _AdGenOtnOduPmThres24HrFeESR_Type(Integer32):
    """Custom type adGenOtnOduPmThres24HrFeESR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AdGenOtnOduPmThres24HrFeESR_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres24HrFeESR_Object = MibTableColumn
adGenOtnOduPmThres24HrFeESR = _AdGenOtnOduPmThres24HrFeESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 4, 1, 14),
    _AdGenOtnOduPmThres24HrFeESR_Type()
)
adGenOtnOduPmThres24HrFeESR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrFeESR.setStatus("current")


class _AdGenOtnOduPmThres24HrFeSESR_Type(Integer32):
    """Custom type adGenOtnOduPmThres24HrFeSESR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AdGenOtnOduPmThres24HrFeSESR_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres24HrFeSESR_Object = MibTableColumn
adGenOtnOduPmThres24HrFeSESR = _AdGenOtnOduPmThres24HrFeSESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 4, 1, 15),
    _AdGenOtnOduPmThres24HrFeSESR_Type()
)
adGenOtnOduPmThres24HrFeSESR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrFeSESR.setStatus("current")


class _AdGenOtnOduPmThres24HrFeUAS_Type(Integer32):
    """Custom type adGenOtnOduPmThres24HrFeUAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AdGenOtnOduPmThres24HrFeUAS_Type.__name__ = "Integer32"
_AdGenOtnOduPmThres24HrFeUAS_Object = MibTableColumn
adGenOtnOduPmThres24HrFeUAS = _AdGenOtnOduPmThres24HrFeUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 3, 4, 1, 16),
    _AdGenOtnOduPmThres24HrFeUAS_Type()
)
adGenOtnOduPmThres24HrFeUAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrFeUAS.setStatus("current")
_AdGenOtnPm_ObjectIdentity = ObjectIdentity
adGenOtnPm = _AdGenOtnPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4)
)
_AdGenOtnOtuPm15MinCurrentTable_Object = MibTable
adGenOtnOtuPm15MinCurrentTable = _AdGenOtnOtuPm15MinCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 1)
)
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinCurrentTable.setStatus("current")
_AdGenOtnOtuPm15MinCurrentEntry_Object = MibTableRow
adGenOtnOtuPm15MinCurrentEntry = _AdGenOtnOtuPm15MinCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 1, 1)
)
adGenOtnOtuPm15MinCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinCurrentEntry.setStatus("current")
_AdGenOtnOtuPm15MinCurrentNeEB_Type = Counter32
_AdGenOtnOtuPm15MinCurrentNeEB_Object = MibTableColumn
adGenOtnOtuPm15MinCurrentNeEB = _AdGenOtnOtuPm15MinCurrentNeEB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 1, 1, 1),
    _AdGenOtnOtuPm15MinCurrentNeEB_Type()
)
adGenOtnOtuPm15MinCurrentNeEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinCurrentNeEB.setStatus("current")
_AdGenOtnOtuPm15MinCurrentNeBBE_Type = Counter32
_AdGenOtnOtuPm15MinCurrentNeBBE_Object = MibTableColumn
adGenOtnOtuPm15MinCurrentNeBBE = _AdGenOtnOtuPm15MinCurrentNeBBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 1, 1, 2),
    _AdGenOtnOtuPm15MinCurrentNeBBE_Type()
)
adGenOtnOtuPm15MinCurrentNeBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinCurrentNeBBE.setStatus("current")


class _AdGenOtnOtuPm15MinCurrentNeBBER_Type(DisplayString):
    """Custom type adGenOtnOtuPm15MinCurrentNeBBER based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_AdGenOtnOtuPm15MinCurrentNeBBER_Type.__name__ = "DisplayString"
_AdGenOtnOtuPm15MinCurrentNeBBER_Object = MibTableColumn
adGenOtnOtuPm15MinCurrentNeBBER = _AdGenOtnOtuPm15MinCurrentNeBBER_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 1, 1, 3),
    _AdGenOtnOtuPm15MinCurrentNeBBER_Type()
)
adGenOtnOtuPm15MinCurrentNeBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinCurrentNeBBER.setStatus("current")
_AdGenOtnOtuPm15MinCurrentNeES_Type = Counter32
_AdGenOtnOtuPm15MinCurrentNeES_Object = MibTableColumn
adGenOtnOtuPm15MinCurrentNeES = _AdGenOtnOtuPm15MinCurrentNeES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 1, 1, 4),
    _AdGenOtnOtuPm15MinCurrentNeES_Type()
)
adGenOtnOtuPm15MinCurrentNeES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinCurrentNeES.setStatus("current")
_AdGenOtnOtuPm15MinCurrentNeSES_Type = Counter32
_AdGenOtnOtuPm15MinCurrentNeSES_Object = MibTableColumn
adGenOtnOtuPm15MinCurrentNeSES = _AdGenOtnOtuPm15MinCurrentNeSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 1, 1, 5),
    _AdGenOtnOtuPm15MinCurrentNeSES_Type()
)
adGenOtnOtuPm15MinCurrentNeSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinCurrentNeSES.setStatus("current")
_AdGenOtnOtuPm15MinCurrentNeESR_Type = Counter32
_AdGenOtnOtuPm15MinCurrentNeESR_Object = MibTableColumn
adGenOtnOtuPm15MinCurrentNeESR = _AdGenOtnOtuPm15MinCurrentNeESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 1, 1, 6),
    _AdGenOtnOtuPm15MinCurrentNeESR_Type()
)
adGenOtnOtuPm15MinCurrentNeESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinCurrentNeESR.setStatus("current")
_AdGenOtnOtuPm15MinCurrentNeSESR_Type = Counter32
_AdGenOtnOtuPm15MinCurrentNeSESR_Object = MibTableColumn
adGenOtnOtuPm15MinCurrentNeSESR = _AdGenOtnOtuPm15MinCurrentNeSESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 1, 1, 7),
    _AdGenOtnOtuPm15MinCurrentNeSESR_Type()
)
adGenOtnOtuPm15MinCurrentNeSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinCurrentNeSESR.setStatus("current")
_AdGenOtnOtuPm15MinCurrentNeUAS_Type = Counter32
_AdGenOtnOtuPm15MinCurrentNeUAS_Object = MibTableColumn
adGenOtnOtuPm15MinCurrentNeUAS = _AdGenOtnOtuPm15MinCurrentNeUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 1, 1, 8),
    _AdGenOtnOtuPm15MinCurrentNeUAS_Type()
)
adGenOtnOtuPm15MinCurrentNeUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinCurrentNeUAS.setStatus("current")
_AdGenOtnOtuPm15MinCurrentFeEB_Type = Counter32
_AdGenOtnOtuPm15MinCurrentFeEB_Object = MibTableColumn
adGenOtnOtuPm15MinCurrentFeEB = _AdGenOtnOtuPm15MinCurrentFeEB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 1, 1, 9),
    _AdGenOtnOtuPm15MinCurrentFeEB_Type()
)
adGenOtnOtuPm15MinCurrentFeEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinCurrentFeEB.setStatus("current")
_AdGenOtnOtuPm15MinCurrentFeBBE_Type = Counter32
_AdGenOtnOtuPm15MinCurrentFeBBE_Object = MibTableColumn
adGenOtnOtuPm15MinCurrentFeBBE = _AdGenOtnOtuPm15MinCurrentFeBBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 1, 1, 10),
    _AdGenOtnOtuPm15MinCurrentFeBBE_Type()
)
adGenOtnOtuPm15MinCurrentFeBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinCurrentFeBBE.setStatus("current")


class _AdGenOtnOtuPm15MinCurrentFeBBER_Type(DisplayString):
    """Custom type adGenOtnOtuPm15MinCurrentFeBBER based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_AdGenOtnOtuPm15MinCurrentFeBBER_Type.__name__ = "DisplayString"
_AdGenOtnOtuPm15MinCurrentFeBBER_Object = MibTableColumn
adGenOtnOtuPm15MinCurrentFeBBER = _AdGenOtnOtuPm15MinCurrentFeBBER_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 1, 1, 11),
    _AdGenOtnOtuPm15MinCurrentFeBBER_Type()
)
adGenOtnOtuPm15MinCurrentFeBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinCurrentFeBBER.setStatus("current")
_AdGenOtnOtuPm15MinCurrentFeES_Type = Counter32
_AdGenOtnOtuPm15MinCurrentFeES_Object = MibTableColumn
adGenOtnOtuPm15MinCurrentFeES = _AdGenOtnOtuPm15MinCurrentFeES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 1, 1, 12),
    _AdGenOtnOtuPm15MinCurrentFeES_Type()
)
adGenOtnOtuPm15MinCurrentFeES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinCurrentFeES.setStatus("current")
_AdGenOtnOtuPm15MinCurrentFeSES_Type = Counter32
_AdGenOtnOtuPm15MinCurrentFeSES_Object = MibTableColumn
adGenOtnOtuPm15MinCurrentFeSES = _AdGenOtnOtuPm15MinCurrentFeSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 1, 1, 13),
    _AdGenOtnOtuPm15MinCurrentFeSES_Type()
)
adGenOtnOtuPm15MinCurrentFeSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinCurrentFeSES.setStatus("current")
_AdGenOtnOtuPm15MinCurrentFeESR_Type = Counter32
_AdGenOtnOtuPm15MinCurrentFeESR_Object = MibTableColumn
adGenOtnOtuPm15MinCurrentFeESR = _AdGenOtnOtuPm15MinCurrentFeESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 1, 1, 14),
    _AdGenOtnOtuPm15MinCurrentFeESR_Type()
)
adGenOtnOtuPm15MinCurrentFeESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinCurrentFeESR.setStatus("current")
_AdGenOtnOtuPm15MinCurrentFeSESR_Type = Counter32
_AdGenOtnOtuPm15MinCurrentFeSESR_Object = MibTableColumn
adGenOtnOtuPm15MinCurrentFeSESR = _AdGenOtnOtuPm15MinCurrentFeSESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 1, 1, 15),
    _AdGenOtnOtuPm15MinCurrentFeSESR_Type()
)
adGenOtnOtuPm15MinCurrentFeSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinCurrentFeSESR.setStatus("current")
_AdGenOtnOtuPm15MinCurrentFeUAS_Type = Counter32
_AdGenOtnOtuPm15MinCurrentFeUAS_Object = MibTableColumn
adGenOtnOtuPm15MinCurrentFeUAS = _AdGenOtnOtuPm15MinCurrentFeUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 1, 1, 16),
    _AdGenOtnOtuPm15MinCurrentFeUAS_Type()
)
adGenOtnOtuPm15MinCurrentFeUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinCurrentFeUAS.setStatus("current")
_AdGenOtnOtuPm15MinCurrentFecCorrBits_Type = Counter64
_AdGenOtnOtuPm15MinCurrentFecCorrBits_Object = MibTableColumn
adGenOtnOtuPm15MinCurrentFecCorrBits = _AdGenOtnOtuPm15MinCurrentFecCorrBits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 1, 1, 17),
    _AdGenOtnOtuPm15MinCurrentFecCorrBits_Type()
)
adGenOtnOtuPm15MinCurrentFecCorrBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinCurrentFecCorrBits.setStatus("current")
_AdGenOtnOtuPm15MinCurrentFecCorrOnes_Type = Counter64
_AdGenOtnOtuPm15MinCurrentFecCorrOnes_Object = MibTableColumn
adGenOtnOtuPm15MinCurrentFecCorrOnes = _AdGenOtnOtuPm15MinCurrentFecCorrOnes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 1, 1, 18),
    _AdGenOtnOtuPm15MinCurrentFecCorrOnes_Type()
)
adGenOtnOtuPm15MinCurrentFecCorrOnes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinCurrentFecCorrOnes.setStatus("current")
_AdGenOtnOtuPm15MinCurrentFecCorrZeros_Type = Counter64
_AdGenOtnOtuPm15MinCurrentFecCorrZeros_Object = MibTableColumn
adGenOtnOtuPm15MinCurrentFecCorrZeros = _AdGenOtnOtuPm15MinCurrentFecCorrZeros_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 1, 1, 19),
    _AdGenOtnOtuPm15MinCurrentFecCorrZeros_Type()
)
adGenOtnOtuPm15MinCurrentFecCorrZeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinCurrentFecCorrZeros.setStatus("current")
_AdGenOtnOtuPm15MinCurrentFecUnCorrBlks_Type = Counter64
_AdGenOtnOtuPm15MinCurrentFecUnCorrBlks_Object = MibTableColumn
adGenOtnOtuPm15MinCurrentFecUnCorrBlks = _AdGenOtnOtuPm15MinCurrentFecUnCorrBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 1, 1, 20),
    _AdGenOtnOtuPm15MinCurrentFecUnCorrBlks_Type()
)
adGenOtnOtuPm15MinCurrentFecUnCorrBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinCurrentFecUnCorrBlks.setStatus("current")


class _AdGenOtnOtuPm15MinCurrentFecCorrBer_Type(DisplayString):
    """Custom type adGenOtnOtuPm15MinCurrentFecCorrBer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_AdGenOtnOtuPm15MinCurrentFecCorrBer_Type.__name__ = "DisplayString"
_AdGenOtnOtuPm15MinCurrentFecCorrBer_Object = MibTableColumn
adGenOtnOtuPm15MinCurrentFecCorrBer = _AdGenOtnOtuPm15MinCurrentFecCorrBer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 1, 1, 21),
    _AdGenOtnOtuPm15MinCurrentFecCorrBer_Type()
)
adGenOtnOtuPm15MinCurrentFecCorrBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinCurrentFecCorrBer.setStatus("current")
_AdGenOtnOtuPm15MinIntervalTable_Object = MibTable
adGenOtnOtuPm15MinIntervalTable = _AdGenOtnOtuPm15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 2)
)
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinIntervalTable.setStatus("current")
_AdGenOtnOtuPm15MinIntervalEntry_Object = MibTableRow
adGenOtnOtuPm15MinIntervalEntry = _AdGenOtnOtuPm15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 2, 1)
)
adGenOtnOtuPm15MinIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENERIC-OTN-MIB", "adGenOtnOtuPm15MinInterval"),
)
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinIntervalEntry.setStatus("current")


class _AdGenOtnOtuPm15MinInterval_Type(Integer32):
    """Custom type adGenOtnOtuPm15MinInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AdGenOtnOtuPm15MinInterval_Type.__name__ = "Integer32"
_AdGenOtnOtuPm15MinInterval_Object = MibTableColumn
adGenOtnOtuPm15MinInterval = _AdGenOtnOtuPm15MinInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 2, 1, 1),
    _AdGenOtnOtuPm15MinInterval_Type()
)
adGenOtnOtuPm15MinInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinInterval.setStatus("current")
_AdGenOtnOtuPm15MinIntervalNeEB_Type = Counter32
_AdGenOtnOtuPm15MinIntervalNeEB_Object = MibTableColumn
adGenOtnOtuPm15MinIntervalNeEB = _AdGenOtnOtuPm15MinIntervalNeEB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 2, 1, 2),
    _AdGenOtnOtuPm15MinIntervalNeEB_Type()
)
adGenOtnOtuPm15MinIntervalNeEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinIntervalNeEB.setStatus("current")
_AdGenOtnOtuPm15MinIntervalNeBBE_Type = Counter32
_AdGenOtnOtuPm15MinIntervalNeBBE_Object = MibTableColumn
adGenOtnOtuPm15MinIntervalNeBBE = _AdGenOtnOtuPm15MinIntervalNeBBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 2, 1, 3),
    _AdGenOtnOtuPm15MinIntervalNeBBE_Type()
)
adGenOtnOtuPm15MinIntervalNeBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinIntervalNeBBE.setStatus("current")


class _AdGenOtnOtuPm15MinIntervalNeBBER_Type(DisplayString):
    """Custom type adGenOtnOtuPm15MinIntervalNeBBER based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_AdGenOtnOtuPm15MinIntervalNeBBER_Type.__name__ = "DisplayString"
_AdGenOtnOtuPm15MinIntervalNeBBER_Object = MibTableColumn
adGenOtnOtuPm15MinIntervalNeBBER = _AdGenOtnOtuPm15MinIntervalNeBBER_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 2, 1, 4),
    _AdGenOtnOtuPm15MinIntervalNeBBER_Type()
)
adGenOtnOtuPm15MinIntervalNeBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinIntervalNeBBER.setStatus("current")
_AdGenOtnOtuPm15MinIntervalNeES_Type = Counter32
_AdGenOtnOtuPm15MinIntervalNeES_Object = MibTableColumn
adGenOtnOtuPm15MinIntervalNeES = _AdGenOtnOtuPm15MinIntervalNeES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 2, 1, 5),
    _AdGenOtnOtuPm15MinIntervalNeES_Type()
)
adGenOtnOtuPm15MinIntervalNeES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinIntervalNeES.setStatus("current")
_AdGenOtnOtuPm15MinIntervalNeSES_Type = Counter32
_AdGenOtnOtuPm15MinIntervalNeSES_Object = MibTableColumn
adGenOtnOtuPm15MinIntervalNeSES = _AdGenOtnOtuPm15MinIntervalNeSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 2, 1, 6),
    _AdGenOtnOtuPm15MinIntervalNeSES_Type()
)
adGenOtnOtuPm15MinIntervalNeSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinIntervalNeSES.setStatus("current")
_AdGenOtnOtuPm15MinIntervalNeESR_Type = Counter32
_AdGenOtnOtuPm15MinIntervalNeESR_Object = MibTableColumn
adGenOtnOtuPm15MinIntervalNeESR = _AdGenOtnOtuPm15MinIntervalNeESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 2, 1, 7),
    _AdGenOtnOtuPm15MinIntervalNeESR_Type()
)
adGenOtnOtuPm15MinIntervalNeESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinIntervalNeESR.setStatus("current")
_AdGenOtnOtuPm15MinIntervalNeSESR_Type = Counter32
_AdGenOtnOtuPm15MinIntervalNeSESR_Object = MibTableColumn
adGenOtnOtuPm15MinIntervalNeSESR = _AdGenOtnOtuPm15MinIntervalNeSESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 2, 1, 8),
    _AdGenOtnOtuPm15MinIntervalNeSESR_Type()
)
adGenOtnOtuPm15MinIntervalNeSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinIntervalNeSESR.setStatus("current")
_AdGenOtnOtuPm15MinIntervalNeUAS_Type = Counter32
_AdGenOtnOtuPm15MinIntervalNeUAS_Object = MibTableColumn
adGenOtnOtuPm15MinIntervalNeUAS = _AdGenOtnOtuPm15MinIntervalNeUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 2, 1, 9),
    _AdGenOtnOtuPm15MinIntervalNeUAS_Type()
)
adGenOtnOtuPm15MinIntervalNeUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinIntervalNeUAS.setStatus("current")
_AdGenOtnOtuPm15MinIntervalFeEB_Type = Counter32
_AdGenOtnOtuPm15MinIntervalFeEB_Object = MibTableColumn
adGenOtnOtuPm15MinIntervalFeEB = _AdGenOtnOtuPm15MinIntervalFeEB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 2, 1, 10),
    _AdGenOtnOtuPm15MinIntervalFeEB_Type()
)
adGenOtnOtuPm15MinIntervalFeEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinIntervalFeEB.setStatus("current")
_AdGenOtnOtuPm15MinIntervalFeBBE_Type = Counter32
_AdGenOtnOtuPm15MinIntervalFeBBE_Object = MibTableColumn
adGenOtnOtuPm15MinIntervalFeBBE = _AdGenOtnOtuPm15MinIntervalFeBBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 2, 1, 11),
    _AdGenOtnOtuPm15MinIntervalFeBBE_Type()
)
adGenOtnOtuPm15MinIntervalFeBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinIntervalFeBBE.setStatus("current")


class _AdGenOtnOtuPm15MinIntervalFeBBER_Type(DisplayString):
    """Custom type adGenOtnOtuPm15MinIntervalFeBBER based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_AdGenOtnOtuPm15MinIntervalFeBBER_Type.__name__ = "DisplayString"
_AdGenOtnOtuPm15MinIntervalFeBBER_Object = MibTableColumn
adGenOtnOtuPm15MinIntervalFeBBER = _AdGenOtnOtuPm15MinIntervalFeBBER_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 2, 1, 12),
    _AdGenOtnOtuPm15MinIntervalFeBBER_Type()
)
adGenOtnOtuPm15MinIntervalFeBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinIntervalFeBBER.setStatus("current")
_AdGenOtnOtuPm15MinIntervalFeES_Type = Counter32
_AdGenOtnOtuPm15MinIntervalFeES_Object = MibTableColumn
adGenOtnOtuPm15MinIntervalFeES = _AdGenOtnOtuPm15MinIntervalFeES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 2, 1, 13),
    _AdGenOtnOtuPm15MinIntervalFeES_Type()
)
adGenOtnOtuPm15MinIntervalFeES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinIntervalFeES.setStatus("current")
_AdGenOtnOtuPm15MinIntervalFeSES_Type = Counter32
_AdGenOtnOtuPm15MinIntervalFeSES_Object = MibTableColumn
adGenOtnOtuPm15MinIntervalFeSES = _AdGenOtnOtuPm15MinIntervalFeSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 2, 1, 14),
    _AdGenOtnOtuPm15MinIntervalFeSES_Type()
)
adGenOtnOtuPm15MinIntervalFeSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinIntervalFeSES.setStatus("current")
_AdGenOtnOtuPm15MinIntervalFeESR_Type = Counter32
_AdGenOtnOtuPm15MinIntervalFeESR_Object = MibTableColumn
adGenOtnOtuPm15MinIntervalFeESR = _AdGenOtnOtuPm15MinIntervalFeESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 2, 1, 15),
    _AdGenOtnOtuPm15MinIntervalFeESR_Type()
)
adGenOtnOtuPm15MinIntervalFeESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinIntervalFeESR.setStatus("current")
_AdGenOtnOtuPm15MinIntervalFeSESR_Type = Counter32
_AdGenOtnOtuPm15MinIntervalFeSESR_Object = MibTableColumn
adGenOtnOtuPm15MinIntervalFeSESR = _AdGenOtnOtuPm15MinIntervalFeSESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 2, 1, 16),
    _AdGenOtnOtuPm15MinIntervalFeSESR_Type()
)
adGenOtnOtuPm15MinIntervalFeSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinIntervalFeSESR.setStatus("current")
_AdGenOtnOtuPm15MinIntervalFeUAS_Type = Counter32
_AdGenOtnOtuPm15MinIntervalFeUAS_Object = MibTableColumn
adGenOtnOtuPm15MinIntervalFeUAS = _AdGenOtnOtuPm15MinIntervalFeUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 2, 1, 17),
    _AdGenOtnOtuPm15MinIntervalFeUAS_Type()
)
adGenOtnOtuPm15MinIntervalFeUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinIntervalFeUAS.setStatus("current")
_AdGenOtnOtuPm15MinIntervalFecCorrBits_Type = Counter64
_AdGenOtnOtuPm15MinIntervalFecCorrBits_Object = MibTableColumn
adGenOtnOtuPm15MinIntervalFecCorrBits = _AdGenOtnOtuPm15MinIntervalFecCorrBits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 2, 1, 18),
    _AdGenOtnOtuPm15MinIntervalFecCorrBits_Type()
)
adGenOtnOtuPm15MinIntervalFecCorrBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinIntervalFecCorrBits.setStatus("current")
_AdGenOtnOtuPm15MinIntervalFecCorrOnes_Type = Counter64
_AdGenOtnOtuPm15MinIntervalFecCorrOnes_Object = MibTableColumn
adGenOtnOtuPm15MinIntervalFecCorrOnes = _AdGenOtnOtuPm15MinIntervalFecCorrOnes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 2, 1, 19),
    _AdGenOtnOtuPm15MinIntervalFecCorrOnes_Type()
)
adGenOtnOtuPm15MinIntervalFecCorrOnes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinIntervalFecCorrOnes.setStatus("current")
_AdGenOtnOtuPm15MinIntervalFecCorrZeros_Type = Counter64
_AdGenOtnOtuPm15MinIntervalFecCorrZeros_Object = MibTableColumn
adGenOtnOtuPm15MinIntervalFecCorrZeros = _AdGenOtnOtuPm15MinIntervalFecCorrZeros_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 2, 1, 20),
    _AdGenOtnOtuPm15MinIntervalFecCorrZeros_Type()
)
adGenOtnOtuPm15MinIntervalFecCorrZeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinIntervalFecCorrZeros.setStatus("current")
_AdGenOtnOtuPm15MinIntervalFecUnCorrBlks_Type = Counter64
_AdGenOtnOtuPm15MinIntervalFecUnCorrBlks_Object = MibTableColumn
adGenOtnOtuPm15MinIntervalFecUnCorrBlks = _AdGenOtnOtuPm15MinIntervalFecUnCorrBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 2, 1, 21),
    _AdGenOtnOtuPm15MinIntervalFecUnCorrBlks_Type()
)
adGenOtnOtuPm15MinIntervalFecUnCorrBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinIntervalFecUnCorrBlks.setStatus("current")


class _AdGenOtnOtuPm15MinIntervalFecCorrBer_Type(DisplayString):
    """Custom type adGenOtnOtuPm15MinIntervalFecCorrBer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_AdGenOtnOtuPm15MinIntervalFecCorrBer_Type.__name__ = "DisplayString"
_AdGenOtnOtuPm15MinIntervalFecCorrBer_Object = MibTableColumn
adGenOtnOtuPm15MinIntervalFecCorrBer = _AdGenOtnOtuPm15MinIntervalFecCorrBer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 2, 1, 22),
    _AdGenOtnOtuPm15MinIntervalFecCorrBer_Type()
)
adGenOtnOtuPm15MinIntervalFecCorrBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinIntervalFecCorrBer.setStatus("current")
_AdGenOtnOtuPm15MinIntervalNeValidData_Type = TruthValue
_AdGenOtnOtuPm15MinIntervalNeValidData_Object = MibTableColumn
adGenOtnOtuPm15MinIntervalNeValidData = _AdGenOtnOtuPm15MinIntervalNeValidData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 2, 1, 23),
    _AdGenOtnOtuPm15MinIntervalNeValidData_Type()
)
adGenOtnOtuPm15MinIntervalNeValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinIntervalNeValidData.setStatus("current")
_AdGenOtnOtuPm15MinIntervalFeValidData_Type = TruthValue
_AdGenOtnOtuPm15MinIntervalFeValidData_Object = MibTableColumn
adGenOtnOtuPm15MinIntervalFeValidData = _AdGenOtnOtuPm15MinIntervalFeValidData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 2, 1, 24),
    _AdGenOtnOtuPm15MinIntervalFeValidData_Type()
)
adGenOtnOtuPm15MinIntervalFeValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm15MinIntervalFeValidData.setStatus("current")
_AdGenOtnOtuPm24HrCurrentTable_Object = MibTable
adGenOtnOtuPm24HrCurrentTable = _AdGenOtnOtuPm24HrCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 3)
)
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrCurrentTable.setStatus("current")
_AdGenOtnOtuPm24HrCurrentEntry_Object = MibTableRow
adGenOtnOtuPm24HrCurrentEntry = _AdGenOtnOtuPm24HrCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 3, 1)
)
adGenOtnOtuPm24HrCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrCurrentEntry.setStatus("current")
_AdGenOtnOtuPm24HrCurrentNeEB_Type = Counter32
_AdGenOtnOtuPm24HrCurrentNeEB_Object = MibTableColumn
adGenOtnOtuPm24HrCurrentNeEB = _AdGenOtnOtuPm24HrCurrentNeEB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 3, 1, 1),
    _AdGenOtnOtuPm24HrCurrentNeEB_Type()
)
adGenOtnOtuPm24HrCurrentNeEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrCurrentNeEB.setStatus("current")
_AdGenOtnOtuPm24HrCurrentNeBBE_Type = Counter32
_AdGenOtnOtuPm24HrCurrentNeBBE_Object = MibTableColumn
adGenOtnOtuPm24HrCurrentNeBBE = _AdGenOtnOtuPm24HrCurrentNeBBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 3, 1, 2),
    _AdGenOtnOtuPm24HrCurrentNeBBE_Type()
)
adGenOtnOtuPm24HrCurrentNeBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrCurrentNeBBE.setStatus("current")


class _AdGenOtnOtuPm24HrCurrentNeBBER_Type(DisplayString):
    """Custom type adGenOtnOtuPm24HrCurrentNeBBER based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_AdGenOtnOtuPm24HrCurrentNeBBER_Type.__name__ = "DisplayString"
_AdGenOtnOtuPm24HrCurrentNeBBER_Object = MibTableColumn
adGenOtnOtuPm24HrCurrentNeBBER = _AdGenOtnOtuPm24HrCurrentNeBBER_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 3, 1, 3),
    _AdGenOtnOtuPm24HrCurrentNeBBER_Type()
)
adGenOtnOtuPm24HrCurrentNeBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrCurrentNeBBER.setStatus("current")
_AdGenOtnOtuPm24HrCurrentNeES_Type = Counter32
_AdGenOtnOtuPm24HrCurrentNeES_Object = MibTableColumn
adGenOtnOtuPm24HrCurrentNeES = _AdGenOtnOtuPm24HrCurrentNeES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 3, 1, 4),
    _AdGenOtnOtuPm24HrCurrentNeES_Type()
)
adGenOtnOtuPm24HrCurrentNeES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrCurrentNeES.setStatus("current")
_AdGenOtnOtuPm24HrCurrentNeSES_Type = Counter32
_AdGenOtnOtuPm24HrCurrentNeSES_Object = MibTableColumn
adGenOtnOtuPm24HrCurrentNeSES = _AdGenOtnOtuPm24HrCurrentNeSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 3, 1, 5),
    _AdGenOtnOtuPm24HrCurrentNeSES_Type()
)
adGenOtnOtuPm24HrCurrentNeSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrCurrentNeSES.setStatus("current")
_AdGenOtnOtuPm24HrCurrentNeESR_Type = Counter32
_AdGenOtnOtuPm24HrCurrentNeESR_Object = MibTableColumn
adGenOtnOtuPm24HrCurrentNeESR = _AdGenOtnOtuPm24HrCurrentNeESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 3, 1, 6),
    _AdGenOtnOtuPm24HrCurrentNeESR_Type()
)
adGenOtnOtuPm24HrCurrentNeESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrCurrentNeESR.setStatus("current")
_AdGenOtnOtuPm24HrCurrentNeSESR_Type = Counter32
_AdGenOtnOtuPm24HrCurrentNeSESR_Object = MibTableColumn
adGenOtnOtuPm24HrCurrentNeSESR = _AdGenOtnOtuPm24HrCurrentNeSESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 3, 1, 7),
    _AdGenOtnOtuPm24HrCurrentNeSESR_Type()
)
adGenOtnOtuPm24HrCurrentNeSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrCurrentNeSESR.setStatus("current")
_AdGenOtnOtuPm24HrCurrentNeUAS_Type = Counter32
_AdGenOtnOtuPm24HrCurrentNeUAS_Object = MibTableColumn
adGenOtnOtuPm24HrCurrentNeUAS = _AdGenOtnOtuPm24HrCurrentNeUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 3, 1, 8),
    _AdGenOtnOtuPm24HrCurrentNeUAS_Type()
)
adGenOtnOtuPm24HrCurrentNeUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrCurrentNeUAS.setStatus("current")
_AdGenOtnOtuPm24HrCurrentFeEB_Type = Counter32
_AdGenOtnOtuPm24HrCurrentFeEB_Object = MibTableColumn
adGenOtnOtuPm24HrCurrentFeEB = _AdGenOtnOtuPm24HrCurrentFeEB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 3, 1, 9),
    _AdGenOtnOtuPm24HrCurrentFeEB_Type()
)
adGenOtnOtuPm24HrCurrentFeEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrCurrentFeEB.setStatus("current")
_AdGenOtnOtuPm24HrCurrentFeBBE_Type = Counter32
_AdGenOtnOtuPm24HrCurrentFeBBE_Object = MibTableColumn
adGenOtnOtuPm24HrCurrentFeBBE = _AdGenOtnOtuPm24HrCurrentFeBBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 3, 1, 10),
    _AdGenOtnOtuPm24HrCurrentFeBBE_Type()
)
adGenOtnOtuPm24HrCurrentFeBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrCurrentFeBBE.setStatus("current")


class _AdGenOtnOtuPm24HrCurrentFeBBER_Type(DisplayString):
    """Custom type adGenOtnOtuPm24HrCurrentFeBBER based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_AdGenOtnOtuPm24HrCurrentFeBBER_Type.__name__ = "DisplayString"
_AdGenOtnOtuPm24HrCurrentFeBBER_Object = MibTableColumn
adGenOtnOtuPm24HrCurrentFeBBER = _AdGenOtnOtuPm24HrCurrentFeBBER_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 3, 1, 11),
    _AdGenOtnOtuPm24HrCurrentFeBBER_Type()
)
adGenOtnOtuPm24HrCurrentFeBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrCurrentFeBBER.setStatus("current")
_AdGenOtnOtuPm24HrCurrentFeES_Type = Counter32
_AdGenOtnOtuPm24HrCurrentFeES_Object = MibTableColumn
adGenOtnOtuPm24HrCurrentFeES = _AdGenOtnOtuPm24HrCurrentFeES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 3, 1, 12),
    _AdGenOtnOtuPm24HrCurrentFeES_Type()
)
adGenOtnOtuPm24HrCurrentFeES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrCurrentFeES.setStatus("current")
_AdGenOtnOtuPm24HrCurrentFeSES_Type = Counter32
_AdGenOtnOtuPm24HrCurrentFeSES_Object = MibTableColumn
adGenOtnOtuPm24HrCurrentFeSES = _AdGenOtnOtuPm24HrCurrentFeSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 3, 1, 13),
    _AdGenOtnOtuPm24HrCurrentFeSES_Type()
)
adGenOtnOtuPm24HrCurrentFeSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrCurrentFeSES.setStatus("current")
_AdGenOtnOtuPm24HrCurrentFeESR_Type = Counter32
_AdGenOtnOtuPm24HrCurrentFeESR_Object = MibTableColumn
adGenOtnOtuPm24HrCurrentFeESR = _AdGenOtnOtuPm24HrCurrentFeESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 3, 1, 14),
    _AdGenOtnOtuPm24HrCurrentFeESR_Type()
)
adGenOtnOtuPm24HrCurrentFeESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrCurrentFeESR.setStatus("current")
_AdGenOtnOtuPm24HrCurrentFeSESR_Type = Counter32
_AdGenOtnOtuPm24HrCurrentFeSESR_Object = MibTableColumn
adGenOtnOtuPm24HrCurrentFeSESR = _AdGenOtnOtuPm24HrCurrentFeSESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 3, 1, 15),
    _AdGenOtnOtuPm24HrCurrentFeSESR_Type()
)
adGenOtnOtuPm24HrCurrentFeSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrCurrentFeSESR.setStatus("current")
_AdGenOtnOtuPm24HrCurrentFeUAS_Type = Counter32
_AdGenOtnOtuPm24HrCurrentFeUAS_Object = MibTableColumn
adGenOtnOtuPm24HrCurrentFeUAS = _AdGenOtnOtuPm24HrCurrentFeUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 3, 1, 16),
    _AdGenOtnOtuPm24HrCurrentFeUAS_Type()
)
adGenOtnOtuPm24HrCurrentFeUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrCurrentFeUAS.setStatus("current")
_AdGenOtnOtuPm24HrCurrentFecCorrBits_Type = Counter64
_AdGenOtnOtuPm24HrCurrentFecCorrBits_Object = MibTableColumn
adGenOtnOtuPm24HrCurrentFecCorrBits = _AdGenOtnOtuPm24HrCurrentFecCorrBits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 3, 1, 17),
    _AdGenOtnOtuPm24HrCurrentFecCorrBits_Type()
)
adGenOtnOtuPm24HrCurrentFecCorrBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrCurrentFecCorrBits.setStatus("current")
_AdGenOtnOtuPm24HrCurrentFecCorrOnes_Type = Counter64
_AdGenOtnOtuPm24HrCurrentFecCorrOnes_Object = MibTableColumn
adGenOtnOtuPm24HrCurrentFecCorrOnes = _AdGenOtnOtuPm24HrCurrentFecCorrOnes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 3, 1, 18),
    _AdGenOtnOtuPm24HrCurrentFecCorrOnes_Type()
)
adGenOtnOtuPm24HrCurrentFecCorrOnes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrCurrentFecCorrOnes.setStatus("current")
_AdGenOtnOtuPm24HrCurrentFecCorrZeros_Type = Counter64
_AdGenOtnOtuPm24HrCurrentFecCorrZeros_Object = MibTableColumn
adGenOtnOtuPm24HrCurrentFecCorrZeros = _AdGenOtnOtuPm24HrCurrentFecCorrZeros_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 3, 1, 19),
    _AdGenOtnOtuPm24HrCurrentFecCorrZeros_Type()
)
adGenOtnOtuPm24HrCurrentFecCorrZeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrCurrentFecCorrZeros.setStatus("current")
_AdGenOtnOtuPm24HrCurrentFecUnCorrBlks_Type = Counter64
_AdGenOtnOtuPm24HrCurrentFecUnCorrBlks_Object = MibTableColumn
adGenOtnOtuPm24HrCurrentFecUnCorrBlks = _AdGenOtnOtuPm24HrCurrentFecUnCorrBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 3, 1, 20),
    _AdGenOtnOtuPm24HrCurrentFecUnCorrBlks_Type()
)
adGenOtnOtuPm24HrCurrentFecUnCorrBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrCurrentFecUnCorrBlks.setStatus("current")


class _AdGenOtnOtuPm24HrCurrentFecCorrBer_Type(DisplayString):
    """Custom type adGenOtnOtuPm24HrCurrentFecCorrBer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_AdGenOtnOtuPm24HrCurrentFecCorrBer_Type.__name__ = "DisplayString"
_AdGenOtnOtuPm24HrCurrentFecCorrBer_Object = MibTableColumn
adGenOtnOtuPm24HrCurrentFecCorrBer = _AdGenOtnOtuPm24HrCurrentFecCorrBer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 3, 1, 21),
    _AdGenOtnOtuPm24HrCurrentFecCorrBer_Type()
)
adGenOtnOtuPm24HrCurrentFecCorrBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrCurrentFecCorrBer.setStatus("current")
_AdGenOtnOtuPm24HrIntervalTable_Object = MibTable
adGenOtnOtuPm24HrIntervalTable = _AdGenOtnOtuPm24HrIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 4)
)
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrIntervalTable.setStatus("current")
_AdGenOtnOtuPm24HrIntervalEntry_Object = MibTableRow
adGenOtnOtuPm24HrIntervalEntry = _AdGenOtnOtuPm24HrIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 4, 1)
)
adGenOtnOtuPm24HrIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENERIC-OTN-MIB", "adGenOtnOtuPm24HrInterval"),
)
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrIntervalEntry.setStatus("current")


class _AdGenOtnOtuPm24HrInterval_Type(Integer32):
    """Custom type adGenOtnOtuPm24HrInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AdGenOtnOtuPm24HrInterval_Type.__name__ = "Integer32"
_AdGenOtnOtuPm24HrInterval_Object = MibTableColumn
adGenOtnOtuPm24HrInterval = _AdGenOtnOtuPm24HrInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 4, 1, 1),
    _AdGenOtnOtuPm24HrInterval_Type()
)
adGenOtnOtuPm24HrInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrInterval.setStatus("current")
_AdGenOtnOtuPm24HrIntervalNeEB_Type = Counter32
_AdGenOtnOtuPm24HrIntervalNeEB_Object = MibTableColumn
adGenOtnOtuPm24HrIntervalNeEB = _AdGenOtnOtuPm24HrIntervalNeEB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 4, 1, 2),
    _AdGenOtnOtuPm24HrIntervalNeEB_Type()
)
adGenOtnOtuPm24HrIntervalNeEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrIntervalNeEB.setStatus("current")
_AdGenOtnOtuPm24HrIntervalNeBBE_Type = Counter32
_AdGenOtnOtuPm24HrIntervalNeBBE_Object = MibTableColumn
adGenOtnOtuPm24HrIntervalNeBBE = _AdGenOtnOtuPm24HrIntervalNeBBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 4, 1, 3),
    _AdGenOtnOtuPm24HrIntervalNeBBE_Type()
)
adGenOtnOtuPm24HrIntervalNeBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrIntervalNeBBE.setStatus("current")


class _AdGenOtnOtuPm24HrIntervalNeBBER_Type(DisplayString):
    """Custom type adGenOtnOtuPm24HrIntervalNeBBER based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_AdGenOtnOtuPm24HrIntervalNeBBER_Type.__name__ = "DisplayString"
_AdGenOtnOtuPm24HrIntervalNeBBER_Object = MibTableColumn
adGenOtnOtuPm24HrIntervalNeBBER = _AdGenOtnOtuPm24HrIntervalNeBBER_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 4, 1, 4),
    _AdGenOtnOtuPm24HrIntervalNeBBER_Type()
)
adGenOtnOtuPm24HrIntervalNeBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrIntervalNeBBER.setStatus("current")
_AdGenOtnOtuPm24HrIntervalNeES_Type = Counter32
_AdGenOtnOtuPm24HrIntervalNeES_Object = MibTableColumn
adGenOtnOtuPm24HrIntervalNeES = _AdGenOtnOtuPm24HrIntervalNeES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 4, 1, 5),
    _AdGenOtnOtuPm24HrIntervalNeES_Type()
)
adGenOtnOtuPm24HrIntervalNeES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrIntervalNeES.setStatus("current")
_AdGenOtnOtuPm24HrIntervalNeSES_Type = Counter32
_AdGenOtnOtuPm24HrIntervalNeSES_Object = MibTableColumn
adGenOtnOtuPm24HrIntervalNeSES = _AdGenOtnOtuPm24HrIntervalNeSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 4, 1, 6),
    _AdGenOtnOtuPm24HrIntervalNeSES_Type()
)
adGenOtnOtuPm24HrIntervalNeSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrIntervalNeSES.setStatus("current")
_AdGenOtnOtuPm24HrIntervalNeESR_Type = Counter32
_AdGenOtnOtuPm24HrIntervalNeESR_Object = MibTableColumn
adGenOtnOtuPm24HrIntervalNeESR = _AdGenOtnOtuPm24HrIntervalNeESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 4, 1, 7),
    _AdGenOtnOtuPm24HrIntervalNeESR_Type()
)
adGenOtnOtuPm24HrIntervalNeESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrIntervalNeESR.setStatus("current")
_AdGenOtnOtuPm24HrIntervalNeSESR_Type = Counter32
_AdGenOtnOtuPm24HrIntervalNeSESR_Object = MibTableColumn
adGenOtnOtuPm24HrIntervalNeSESR = _AdGenOtnOtuPm24HrIntervalNeSESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 4, 1, 8),
    _AdGenOtnOtuPm24HrIntervalNeSESR_Type()
)
adGenOtnOtuPm24HrIntervalNeSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrIntervalNeSESR.setStatus("current")
_AdGenOtnOtuPm24HrIntervalNeUAS_Type = Counter32
_AdGenOtnOtuPm24HrIntervalNeUAS_Object = MibTableColumn
adGenOtnOtuPm24HrIntervalNeUAS = _AdGenOtnOtuPm24HrIntervalNeUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 4, 1, 9),
    _AdGenOtnOtuPm24HrIntervalNeUAS_Type()
)
adGenOtnOtuPm24HrIntervalNeUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrIntervalNeUAS.setStatus("current")
_AdGenOtnOtuPm24HrIntervalFeEB_Type = Counter32
_AdGenOtnOtuPm24HrIntervalFeEB_Object = MibTableColumn
adGenOtnOtuPm24HrIntervalFeEB = _AdGenOtnOtuPm24HrIntervalFeEB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 4, 1, 10),
    _AdGenOtnOtuPm24HrIntervalFeEB_Type()
)
adGenOtnOtuPm24HrIntervalFeEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrIntervalFeEB.setStatus("current")
_AdGenOtnOtuPm24HrIntervalFeBBE_Type = Counter32
_AdGenOtnOtuPm24HrIntervalFeBBE_Object = MibTableColumn
adGenOtnOtuPm24HrIntervalFeBBE = _AdGenOtnOtuPm24HrIntervalFeBBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 4, 1, 11),
    _AdGenOtnOtuPm24HrIntervalFeBBE_Type()
)
adGenOtnOtuPm24HrIntervalFeBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrIntervalFeBBE.setStatus("current")
_AdGenOtnOtuPm24HrIntervalFeBBER_Type = DisplayString
_AdGenOtnOtuPm24HrIntervalFeBBER_Object = MibTableColumn
adGenOtnOtuPm24HrIntervalFeBBER = _AdGenOtnOtuPm24HrIntervalFeBBER_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 4, 1, 12),
    _AdGenOtnOtuPm24HrIntervalFeBBER_Type()
)
adGenOtnOtuPm24HrIntervalFeBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrIntervalFeBBER.setStatus("current")
_AdGenOtnOtuPm24HrIntervalFeES_Type = Counter32
_AdGenOtnOtuPm24HrIntervalFeES_Object = MibTableColumn
adGenOtnOtuPm24HrIntervalFeES = _AdGenOtnOtuPm24HrIntervalFeES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 4, 1, 13),
    _AdGenOtnOtuPm24HrIntervalFeES_Type()
)
adGenOtnOtuPm24HrIntervalFeES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrIntervalFeES.setStatus("current")
_AdGenOtnOtuPm24HrIntervalFeSES_Type = Counter32
_AdGenOtnOtuPm24HrIntervalFeSES_Object = MibTableColumn
adGenOtnOtuPm24HrIntervalFeSES = _AdGenOtnOtuPm24HrIntervalFeSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 4, 1, 14),
    _AdGenOtnOtuPm24HrIntervalFeSES_Type()
)
adGenOtnOtuPm24HrIntervalFeSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrIntervalFeSES.setStatus("current")
_AdGenOtnOtuPm24HrIntervalFeESR_Type = Counter32
_AdGenOtnOtuPm24HrIntervalFeESR_Object = MibTableColumn
adGenOtnOtuPm24HrIntervalFeESR = _AdGenOtnOtuPm24HrIntervalFeESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 4, 1, 15),
    _AdGenOtnOtuPm24HrIntervalFeESR_Type()
)
adGenOtnOtuPm24HrIntervalFeESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrIntervalFeESR.setStatus("current")
_AdGenOtnOtuPm24HrIntervalFeSESR_Type = Counter32
_AdGenOtnOtuPm24HrIntervalFeSESR_Object = MibTableColumn
adGenOtnOtuPm24HrIntervalFeSESR = _AdGenOtnOtuPm24HrIntervalFeSESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 4, 1, 16),
    _AdGenOtnOtuPm24HrIntervalFeSESR_Type()
)
adGenOtnOtuPm24HrIntervalFeSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrIntervalFeSESR.setStatus("current")
_AdGenOtnOtuPm24HrIntervalFeUAS_Type = Counter32
_AdGenOtnOtuPm24HrIntervalFeUAS_Object = MibTableColumn
adGenOtnOtuPm24HrIntervalFeUAS = _AdGenOtnOtuPm24HrIntervalFeUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 4, 1, 17),
    _AdGenOtnOtuPm24HrIntervalFeUAS_Type()
)
adGenOtnOtuPm24HrIntervalFeUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrIntervalFeUAS.setStatus("current")
_AdGenOtnOtuPm24HrIntervalFecCorrBits_Type = Counter64
_AdGenOtnOtuPm24HrIntervalFecCorrBits_Object = MibTableColumn
adGenOtnOtuPm24HrIntervalFecCorrBits = _AdGenOtnOtuPm24HrIntervalFecCorrBits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 4, 1, 18),
    _AdGenOtnOtuPm24HrIntervalFecCorrBits_Type()
)
adGenOtnOtuPm24HrIntervalFecCorrBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrIntervalFecCorrBits.setStatus("current")
_AdGenOtnOtuPm24HrIntervalFecCorrOnes_Type = Counter64
_AdGenOtnOtuPm24HrIntervalFecCorrOnes_Object = MibTableColumn
adGenOtnOtuPm24HrIntervalFecCorrOnes = _AdGenOtnOtuPm24HrIntervalFecCorrOnes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 4, 1, 19),
    _AdGenOtnOtuPm24HrIntervalFecCorrOnes_Type()
)
adGenOtnOtuPm24HrIntervalFecCorrOnes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrIntervalFecCorrOnes.setStatus("current")
_AdGenOtnOtuPm24HrIntervalFecCorrZeros_Type = Counter64
_AdGenOtnOtuPm24HrIntervalFecCorrZeros_Object = MibTableColumn
adGenOtnOtuPm24HrIntervalFecCorrZeros = _AdGenOtnOtuPm24HrIntervalFecCorrZeros_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 4, 1, 20),
    _AdGenOtnOtuPm24HrIntervalFecCorrZeros_Type()
)
adGenOtnOtuPm24HrIntervalFecCorrZeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrIntervalFecCorrZeros.setStatus("current")
_AdGenOtnOtuPm24HrIntervalFecUnCorrBlks_Type = Counter64
_AdGenOtnOtuPm24HrIntervalFecUnCorrBlks_Object = MibTableColumn
adGenOtnOtuPm24HrIntervalFecUnCorrBlks = _AdGenOtnOtuPm24HrIntervalFecUnCorrBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 4, 1, 21),
    _AdGenOtnOtuPm24HrIntervalFecUnCorrBlks_Type()
)
adGenOtnOtuPm24HrIntervalFecUnCorrBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrIntervalFecUnCorrBlks.setStatus("current")
_AdGenOtnOtuPm24HrIntervalFecCorrBer_Type = DisplayString
_AdGenOtnOtuPm24HrIntervalFecCorrBer_Object = MibTableColumn
adGenOtnOtuPm24HrIntervalFecCorrBer = _AdGenOtnOtuPm24HrIntervalFecCorrBer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 4, 1, 22),
    _AdGenOtnOtuPm24HrIntervalFecCorrBer_Type()
)
adGenOtnOtuPm24HrIntervalFecCorrBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrIntervalFecCorrBer.setStatus("current")
_AdGenOtnOtuPm24HrIntervalNeValidData_Type = TruthValue
_AdGenOtnOtuPm24HrIntervalNeValidData_Object = MibTableColumn
adGenOtnOtuPm24HrIntervalNeValidData = _AdGenOtnOtuPm24HrIntervalNeValidData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 4, 1, 23),
    _AdGenOtnOtuPm24HrIntervalNeValidData_Type()
)
adGenOtnOtuPm24HrIntervalNeValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrIntervalNeValidData.setStatus("current")
_AdGenOtnOtuPm24HrIntervalFeValidData_Type = TruthValue
_AdGenOtnOtuPm24HrIntervalFeValidData_Object = MibTableColumn
adGenOtnOtuPm24HrIntervalFeValidData = _AdGenOtnOtuPm24HrIntervalFeValidData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 4, 1, 24),
    _AdGenOtnOtuPm24HrIntervalFeValidData_Type()
)
adGenOtnOtuPm24HrIntervalFeValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuPm24HrIntervalFeValidData.setStatus("current")
_AdGenOtnOduPm15MinCurrentTable_Object = MibTable
adGenOtnOduPm15MinCurrentTable = _AdGenOtnOduPm15MinCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 5)
)
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinCurrentTable.setStatus("current")
_AdGenOtnOduPm15MinCurrentEntry_Object = MibTableRow
adGenOtnOduPm15MinCurrentEntry = _AdGenOtnOduPm15MinCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 5, 1)
)
adGenOtnOduPm15MinCurrentEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
)
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinCurrentEntry.setStatus("current")
_AdGenOtnOduPm15MinCurrentNeEB_Type = Counter32
_AdGenOtnOduPm15MinCurrentNeEB_Object = MibTableColumn
adGenOtnOduPm15MinCurrentNeEB = _AdGenOtnOduPm15MinCurrentNeEB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 5, 1, 1),
    _AdGenOtnOduPm15MinCurrentNeEB_Type()
)
adGenOtnOduPm15MinCurrentNeEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinCurrentNeEB.setStatus("current")
_AdGenOtnOduPm15MinCurrentNeBBE_Type = Counter32
_AdGenOtnOduPm15MinCurrentNeBBE_Object = MibTableColumn
adGenOtnOduPm15MinCurrentNeBBE = _AdGenOtnOduPm15MinCurrentNeBBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 5, 1, 2),
    _AdGenOtnOduPm15MinCurrentNeBBE_Type()
)
adGenOtnOduPm15MinCurrentNeBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinCurrentNeBBE.setStatus("current")


class _AdGenOtnOduPm15MinCurrentNeBBER_Type(DisplayString):
    """Custom type adGenOtnOduPm15MinCurrentNeBBER based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_AdGenOtnOduPm15MinCurrentNeBBER_Type.__name__ = "DisplayString"
_AdGenOtnOduPm15MinCurrentNeBBER_Object = MibTableColumn
adGenOtnOduPm15MinCurrentNeBBER = _AdGenOtnOduPm15MinCurrentNeBBER_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 5, 1, 3),
    _AdGenOtnOduPm15MinCurrentNeBBER_Type()
)
adGenOtnOduPm15MinCurrentNeBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinCurrentNeBBER.setStatus("current")
_AdGenOtnOduPm15MinCurrentNeES_Type = Counter32
_AdGenOtnOduPm15MinCurrentNeES_Object = MibTableColumn
adGenOtnOduPm15MinCurrentNeES = _AdGenOtnOduPm15MinCurrentNeES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 5, 1, 4),
    _AdGenOtnOduPm15MinCurrentNeES_Type()
)
adGenOtnOduPm15MinCurrentNeES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinCurrentNeES.setStatus("current")
_AdGenOtnOduPm15MinCurrentNeSES_Type = Counter32
_AdGenOtnOduPm15MinCurrentNeSES_Object = MibTableColumn
adGenOtnOduPm15MinCurrentNeSES = _AdGenOtnOduPm15MinCurrentNeSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 5, 1, 5),
    _AdGenOtnOduPm15MinCurrentNeSES_Type()
)
adGenOtnOduPm15MinCurrentNeSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinCurrentNeSES.setStatus("current")
_AdGenOtnOduPm15MinCurrentNeESR_Type = Counter32
_AdGenOtnOduPm15MinCurrentNeESR_Object = MibTableColumn
adGenOtnOduPm15MinCurrentNeESR = _AdGenOtnOduPm15MinCurrentNeESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 5, 1, 6),
    _AdGenOtnOduPm15MinCurrentNeESR_Type()
)
adGenOtnOduPm15MinCurrentNeESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinCurrentNeESR.setStatus("current")
_AdGenOtnOduPm15MinCurrentNeSESR_Type = Counter32
_AdGenOtnOduPm15MinCurrentNeSESR_Object = MibTableColumn
adGenOtnOduPm15MinCurrentNeSESR = _AdGenOtnOduPm15MinCurrentNeSESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 5, 1, 7),
    _AdGenOtnOduPm15MinCurrentNeSESR_Type()
)
adGenOtnOduPm15MinCurrentNeSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinCurrentNeSESR.setStatus("current")
_AdGenOtnOduPm15MinCurrentNeUAS_Type = Counter32
_AdGenOtnOduPm15MinCurrentNeUAS_Object = MibTableColumn
adGenOtnOduPm15MinCurrentNeUAS = _AdGenOtnOduPm15MinCurrentNeUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 5, 1, 8),
    _AdGenOtnOduPm15MinCurrentNeUAS_Type()
)
adGenOtnOduPm15MinCurrentNeUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinCurrentNeUAS.setStatus("current")
_AdGenOtnOduPm15MinCurrentFeEB_Type = Counter32
_AdGenOtnOduPm15MinCurrentFeEB_Object = MibTableColumn
adGenOtnOduPm15MinCurrentFeEB = _AdGenOtnOduPm15MinCurrentFeEB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 5, 1, 9),
    _AdGenOtnOduPm15MinCurrentFeEB_Type()
)
adGenOtnOduPm15MinCurrentFeEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinCurrentFeEB.setStatus("current")
_AdGenOtnOduPm15MinCurrentFeBBE_Type = Counter32
_AdGenOtnOduPm15MinCurrentFeBBE_Object = MibTableColumn
adGenOtnOduPm15MinCurrentFeBBE = _AdGenOtnOduPm15MinCurrentFeBBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 5, 1, 10),
    _AdGenOtnOduPm15MinCurrentFeBBE_Type()
)
adGenOtnOduPm15MinCurrentFeBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinCurrentFeBBE.setStatus("current")


class _AdGenOtnOduPm15MinCurrentFeBBER_Type(DisplayString):
    """Custom type adGenOtnOduPm15MinCurrentFeBBER based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_AdGenOtnOduPm15MinCurrentFeBBER_Type.__name__ = "DisplayString"
_AdGenOtnOduPm15MinCurrentFeBBER_Object = MibTableColumn
adGenOtnOduPm15MinCurrentFeBBER = _AdGenOtnOduPm15MinCurrentFeBBER_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 5, 1, 11),
    _AdGenOtnOduPm15MinCurrentFeBBER_Type()
)
adGenOtnOduPm15MinCurrentFeBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinCurrentFeBBER.setStatus("current")
_AdGenOtnOduPm15MinCurrentFeES_Type = Counter32
_AdGenOtnOduPm15MinCurrentFeES_Object = MibTableColumn
adGenOtnOduPm15MinCurrentFeES = _AdGenOtnOduPm15MinCurrentFeES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 5, 1, 12),
    _AdGenOtnOduPm15MinCurrentFeES_Type()
)
adGenOtnOduPm15MinCurrentFeES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinCurrentFeES.setStatus("current")
_AdGenOtnOduPm15MinCurrentFeSES_Type = Counter32
_AdGenOtnOduPm15MinCurrentFeSES_Object = MibTableColumn
adGenOtnOduPm15MinCurrentFeSES = _AdGenOtnOduPm15MinCurrentFeSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 5, 1, 13),
    _AdGenOtnOduPm15MinCurrentFeSES_Type()
)
adGenOtnOduPm15MinCurrentFeSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinCurrentFeSES.setStatus("current")
_AdGenOtnOduPm15MinCurrentFeESR_Type = Counter32
_AdGenOtnOduPm15MinCurrentFeESR_Object = MibTableColumn
adGenOtnOduPm15MinCurrentFeESR = _AdGenOtnOduPm15MinCurrentFeESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 5, 1, 14),
    _AdGenOtnOduPm15MinCurrentFeESR_Type()
)
adGenOtnOduPm15MinCurrentFeESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinCurrentFeESR.setStatus("current")
_AdGenOtnOduPm15MinCurrentFeSESR_Type = Counter32
_AdGenOtnOduPm15MinCurrentFeSESR_Object = MibTableColumn
adGenOtnOduPm15MinCurrentFeSESR = _AdGenOtnOduPm15MinCurrentFeSESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 5, 1, 15),
    _AdGenOtnOduPm15MinCurrentFeSESR_Type()
)
adGenOtnOduPm15MinCurrentFeSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinCurrentFeSESR.setStatus("current")
_AdGenOtnOduPm15MinCurrentFeUAS_Type = Counter32
_AdGenOtnOduPm15MinCurrentFeUAS_Object = MibTableColumn
adGenOtnOduPm15MinCurrentFeUAS = _AdGenOtnOduPm15MinCurrentFeUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 5, 1, 16),
    _AdGenOtnOduPm15MinCurrentFeUAS_Type()
)
adGenOtnOduPm15MinCurrentFeUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinCurrentFeUAS.setStatus("current")
_AdGenOtnOduPm15MinIntervalTable_Object = MibTable
adGenOtnOduPm15MinIntervalTable = _AdGenOtnOduPm15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 6)
)
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinIntervalTable.setStatus("current")
_AdGenOtnOduPm15MinIntervalEntry_Object = MibTableRow
adGenOtnOduPm15MinIntervalEntry = _AdGenOtnOduPm15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 6, 1)
)
adGenOtnOduPm15MinIntervalEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
    (0, "ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduPm15MinInterval"),
)
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinIntervalEntry.setStatus("current")


class _AdGenOtnOduPm15MinInterval_Type(Integer32):
    """Custom type adGenOtnOduPm15MinInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AdGenOtnOduPm15MinInterval_Type.__name__ = "Integer32"
_AdGenOtnOduPm15MinInterval_Object = MibTableColumn
adGenOtnOduPm15MinInterval = _AdGenOtnOduPm15MinInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 6, 1, 1),
    _AdGenOtnOduPm15MinInterval_Type()
)
adGenOtnOduPm15MinInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinInterval.setStatus("current")
_AdGenOtnOduPm15MinIntervalNeEB_Type = Counter32
_AdGenOtnOduPm15MinIntervalNeEB_Object = MibTableColumn
adGenOtnOduPm15MinIntervalNeEB = _AdGenOtnOduPm15MinIntervalNeEB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 6, 1, 2),
    _AdGenOtnOduPm15MinIntervalNeEB_Type()
)
adGenOtnOduPm15MinIntervalNeEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinIntervalNeEB.setStatus("current")
_AdGenOtnOduPm15MinIntervalNeBBE_Type = Counter32
_AdGenOtnOduPm15MinIntervalNeBBE_Object = MibTableColumn
adGenOtnOduPm15MinIntervalNeBBE = _AdGenOtnOduPm15MinIntervalNeBBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 6, 1, 3),
    _AdGenOtnOduPm15MinIntervalNeBBE_Type()
)
adGenOtnOduPm15MinIntervalNeBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinIntervalNeBBE.setStatus("current")
_AdGenOtnOduPm15MinIntervalNeBBER_Type = DisplayString
_AdGenOtnOduPm15MinIntervalNeBBER_Object = MibTableColumn
adGenOtnOduPm15MinIntervalNeBBER = _AdGenOtnOduPm15MinIntervalNeBBER_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 6, 1, 4),
    _AdGenOtnOduPm15MinIntervalNeBBER_Type()
)
adGenOtnOduPm15MinIntervalNeBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinIntervalNeBBER.setStatus("current")
_AdGenOtnOduPm15MinIntervalNeES_Type = Counter32
_AdGenOtnOduPm15MinIntervalNeES_Object = MibTableColumn
adGenOtnOduPm15MinIntervalNeES = _AdGenOtnOduPm15MinIntervalNeES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 6, 1, 5),
    _AdGenOtnOduPm15MinIntervalNeES_Type()
)
adGenOtnOduPm15MinIntervalNeES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinIntervalNeES.setStatus("current")
_AdGenOtnOduPm15MinIntervalNeSES_Type = Counter32
_AdGenOtnOduPm15MinIntervalNeSES_Object = MibTableColumn
adGenOtnOduPm15MinIntervalNeSES = _AdGenOtnOduPm15MinIntervalNeSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 6, 1, 6),
    _AdGenOtnOduPm15MinIntervalNeSES_Type()
)
adGenOtnOduPm15MinIntervalNeSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinIntervalNeSES.setStatus("current")
_AdGenOtnOduPm15MinIntervalNeESR_Type = Counter32
_AdGenOtnOduPm15MinIntervalNeESR_Object = MibTableColumn
adGenOtnOduPm15MinIntervalNeESR = _AdGenOtnOduPm15MinIntervalNeESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 6, 1, 7),
    _AdGenOtnOduPm15MinIntervalNeESR_Type()
)
adGenOtnOduPm15MinIntervalNeESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinIntervalNeESR.setStatus("current")
_AdGenOtnOduPm15MinIntervalNeSESR_Type = Counter32
_AdGenOtnOduPm15MinIntervalNeSESR_Object = MibTableColumn
adGenOtnOduPm15MinIntervalNeSESR = _AdGenOtnOduPm15MinIntervalNeSESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 6, 1, 8),
    _AdGenOtnOduPm15MinIntervalNeSESR_Type()
)
adGenOtnOduPm15MinIntervalNeSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinIntervalNeSESR.setStatus("current")
_AdGenOtnOduPm15MinIntervalNeUAS_Type = Counter32
_AdGenOtnOduPm15MinIntervalNeUAS_Object = MibTableColumn
adGenOtnOduPm15MinIntervalNeUAS = _AdGenOtnOduPm15MinIntervalNeUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 6, 1, 9),
    _AdGenOtnOduPm15MinIntervalNeUAS_Type()
)
adGenOtnOduPm15MinIntervalNeUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinIntervalNeUAS.setStatus("current")
_AdGenOtnOduPm15MinIntervalFeEB_Type = Counter32
_AdGenOtnOduPm15MinIntervalFeEB_Object = MibTableColumn
adGenOtnOduPm15MinIntervalFeEB = _AdGenOtnOduPm15MinIntervalFeEB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 6, 1, 10),
    _AdGenOtnOduPm15MinIntervalFeEB_Type()
)
adGenOtnOduPm15MinIntervalFeEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinIntervalFeEB.setStatus("current")
_AdGenOtnOduPm15MinIntervalFeBBE_Type = Counter32
_AdGenOtnOduPm15MinIntervalFeBBE_Object = MibTableColumn
adGenOtnOduPm15MinIntervalFeBBE = _AdGenOtnOduPm15MinIntervalFeBBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 6, 1, 11),
    _AdGenOtnOduPm15MinIntervalFeBBE_Type()
)
adGenOtnOduPm15MinIntervalFeBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinIntervalFeBBE.setStatus("current")


class _AdGenOtnOduPm15MinIntervalFeBBER_Type(DisplayString):
    """Custom type adGenOtnOduPm15MinIntervalFeBBER based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_AdGenOtnOduPm15MinIntervalFeBBER_Type.__name__ = "DisplayString"
_AdGenOtnOduPm15MinIntervalFeBBER_Object = MibTableColumn
adGenOtnOduPm15MinIntervalFeBBER = _AdGenOtnOduPm15MinIntervalFeBBER_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 6, 1, 12),
    _AdGenOtnOduPm15MinIntervalFeBBER_Type()
)
adGenOtnOduPm15MinIntervalFeBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinIntervalFeBBER.setStatus("current")
_AdGenOtnOduPm15MinIntervalFeES_Type = Counter32
_AdGenOtnOduPm15MinIntervalFeES_Object = MibTableColumn
adGenOtnOduPm15MinIntervalFeES = _AdGenOtnOduPm15MinIntervalFeES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 6, 1, 13),
    _AdGenOtnOduPm15MinIntervalFeES_Type()
)
adGenOtnOduPm15MinIntervalFeES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinIntervalFeES.setStatus("current")
_AdGenOtnOduPm15MinIntervalFeSES_Type = Counter32
_AdGenOtnOduPm15MinIntervalFeSES_Object = MibTableColumn
adGenOtnOduPm15MinIntervalFeSES = _AdGenOtnOduPm15MinIntervalFeSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 6, 1, 14),
    _AdGenOtnOduPm15MinIntervalFeSES_Type()
)
adGenOtnOduPm15MinIntervalFeSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinIntervalFeSES.setStatus("current")
_AdGenOtnOduPm15MinIntervalFeESR_Type = Counter32
_AdGenOtnOduPm15MinIntervalFeESR_Object = MibTableColumn
adGenOtnOduPm15MinIntervalFeESR = _AdGenOtnOduPm15MinIntervalFeESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 6, 1, 15),
    _AdGenOtnOduPm15MinIntervalFeESR_Type()
)
adGenOtnOduPm15MinIntervalFeESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinIntervalFeESR.setStatus("current")
_AdGenOtnOduPm15MinIntervalFeSESR_Type = Counter32
_AdGenOtnOduPm15MinIntervalFeSESR_Object = MibTableColumn
adGenOtnOduPm15MinIntervalFeSESR = _AdGenOtnOduPm15MinIntervalFeSESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 6, 1, 16),
    _AdGenOtnOduPm15MinIntervalFeSESR_Type()
)
adGenOtnOduPm15MinIntervalFeSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinIntervalFeSESR.setStatus("current")
_AdGenOtnOduPm15MinIntervalFeUAS_Type = Counter32
_AdGenOtnOduPm15MinIntervalFeUAS_Object = MibTableColumn
adGenOtnOduPm15MinIntervalFeUAS = _AdGenOtnOduPm15MinIntervalFeUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 6, 1, 17),
    _AdGenOtnOduPm15MinIntervalFeUAS_Type()
)
adGenOtnOduPm15MinIntervalFeUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinIntervalFeUAS.setStatus("current")
_AdGenOtnOduPm15MinIntervalNeValidData_Type = TruthValue
_AdGenOtnOduPm15MinIntervalNeValidData_Object = MibTableColumn
adGenOtnOduPm15MinIntervalNeValidData = _AdGenOtnOduPm15MinIntervalNeValidData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 6, 1, 18),
    _AdGenOtnOduPm15MinIntervalNeValidData_Type()
)
adGenOtnOduPm15MinIntervalNeValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinIntervalNeValidData.setStatus("current")
_AdGenOtnOduPm15MinIntervalFeValidData_Type = TruthValue
_AdGenOtnOduPm15MinIntervalFeValidData_Object = MibTableColumn
adGenOtnOduPm15MinIntervalFeValidData = _AdGenOtnOduPm15MinIntervalFeValidData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 6, 1, 19),
    _AdGenOtnOduPm15MinIntervalFeValidData_Type()
)
adGenOtnOduPm15MinIntervalFeValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm15MinIntervalFeValidData.setStatus("current")
_AdGenOtnOduPm24HrCurrentTable_Object = MibTable
adGenOtnOduPm24HrCurrentTable = _AdGenOtnOduPm24HrCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 7)
)
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrCurrentTable.setStatus("current")
_AdGenOtnOduPm24HrCurrentEntry_Object = MibTableRow
adGenOtnOduPm24HrCurrentEntry = _AdGenOtnOduPm24HrCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 7, 1)
)
adGenOtnOduPm24HrCurrentEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
)
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrCurrentEntry.setStatus("current")
_AdGenOtnOduPm24HrCurrentNeEB_Type = Counter32
_AdGenOtnOduPm24HrCurrentNeEB_Object = MibTableColumn
adGenOtnOduPm24HrCurrentNeEB = _AdGenOtnOduPm24HrCurrentNeEB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 7, 1, 1),
    _AdGenOtnOduPm24HrCurrentNeEB_Type()
)
adGenOtnOduPm24HrCurrentNeEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrCurrentNeEB.setStatus("current")
_AdGenOtnOduPm24HrCurrentNeBBE_Type = Counter32
_AdGenOtnOduPm24HrCurrentNeBBE_Object = MibTableColumn
adGenOtnOduPm24HrCurrentNeBBE = _AdGenOtnOduPm24HrCurrentNeBBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 7, 1, 2),
    _AdGenOtnOduPm24HrCurrentNeBBE_Type()
)
adGenOtnOduPm24HrCurrentNeBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrCurrentNeBBE.setStatus("current")


class _AdGenOtnOduPm24HrCurrentNeBBER_Type(DisplayString):
    """Custom type adGenOtnOduPm24HrCurrentNeBBER based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_AdGenOtnOduPm24HrCurrentNeBBER_Type.__name__ = "DisplayString"
_AdGenOtnOduPm24HrCurrentNeBBER_Object = MibTableColumn
adGenOtnOduPm24HrCurrentNeBBER = _AdGenOtnOduPm24HrCurrentNeBBER_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 7, 1, 3),
    _AdGenOtnOduPm24HrCurrentNeBBER_Type()
)
adGenOtnOduPm24HrCurrentNeBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrCurrentNeBBER.setStatus("current")
_AdGenOtnOduPm24HrCurrentNeES_Type = Counter32
_AdGenOtnOduPm24HrCurrentNeES_Object = MibTableColumn
adGenOtnOduPm24HrCurrentNeES = _AdGenOtnOduPm24HrCurrentNeES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 7, 1, 4),
    _AdGenOtnOduPm24HrCurrentNeES_Type()
)
adGenOtnOduPm24HrCurrentNeES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrCurrentNeES.setStatus("current")
_AdGenOtnOduPm24HrCurrentNeSES_Type = Counter32
_AdGenOtnOduPm24HrCurrentNeSES_Object = MibTableColumn
adGenOtnOduPm24HrCurrentNeSES = _AdGenOtnOduPm24HrCurrentNeSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 7, 1, 5),
    _AdGenOtnOduPm24HrCurrentNeSES_Type()
)
adGenOtnOduPm24HrCurrentNeSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrCurrentNeSES.setStatus("current")
_AdGenOtnOduPm24HrCurrentNeESR_Type = Counter32
_AdGenOtnOduPm24HrCurrentNeESR_Object = MibTableColumn
adGenOtnOduPm24HrCurrentNeESR = _AdGenOtnOduPm24HrCurrentNeESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 7, 1, 6),
    _AdGenOtnOduPm24HrCurrentNeESR_Type()
)
adGenOtnOduPm24HrCurrentNeESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrCurrentNeESR.setStatus("current")
_AdGenOtnOduPm24HrCurrentNeSESR_Type = Counter32
_AdGenOtnOduPm24HrCurrentNeSESR_Object = MibTableColumn
adGenOtnOduPm24HrCurrentNeSESR = _AdGenOtnOduPm24HrCurrentNeSESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 7, 1, 7),
    _AdGenOtnOduPm24HrCurrentNeSESR_Type()
)
adGenOtnOduPm24HrCurrentNeSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrCurrentNeSESR.setStatus("current")
_AdGenOtnOduPm24HrCurrentNeUAS_Type = Counter32
_AdGenOtnOduPm24HrCurrentNeUAS_Object = MibTableColumn
adGenOtnOduPm24HrCurrentNeUAS = _AdGenOtnOduPm24HrCurrentNeUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 7, 1, 8),
    _AdGenOtnOduPm24HrCurrentNeUAS_Type()
)
adGenOtnOduPm24HrCurrentNeUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrCurrentNeUAS.setStatus("current")
_AdGenOtnOduPm24HrCurrentFeEB_Type = Counter32
_AdGenOtnOduPm24HrCurrentFeEB_Object = MibTableColumn
adGenOtnOduPm24HrCurrentFeEB = _AdGenOtnOduPm24HrCurrentFeEB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 7, 1, 9),
    _AdGenOtnOduPm24HrCurrentFeEB_Type()
)
adGenOtnOduPm24HrCurrentFeEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrCurrentFeEB.setStatus("current")
_AdGenOtnOduPm24HrCurrentFeBBE_Type = Counter32
_AdGenOtnOduPm24HrCurrentFeBBE_Object = MibTableColumn
adGenOtnOduPm24HrCurrentFeBBE = _AdGenOtnOduPm24HrCurrentFeBBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 7, 1, 10),
    _AdGenOtnOduPm24HrCurrentFeBBE_Type()
)
adGenOtnOduPm24HrCurrentFeBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrCurrentFeBBE.setStatus("current")


class _AdGenOtnOduPm24HrCurrentFeBBER_Type(DisplayString):
    """Custom type adGenOtnOduPm24HrCurrentFeBBER based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_AdGenOtnOduPm24HrCurrentFeBBER_Type.__name__ = "DisplayString"
_AdGenOtnOduPm24HrCurrentFeBBER_Object = MibTableColumn
adGenOtnOduPm24HrCurrentFeBBER = _AdGenOtnOduPm24HrCurrentFeBBER_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 7, 1, 11),
    _AdGenOtnOduPm24HrCurrentFeBBER_Type()
)
adGenOtnOduPm24HrCurrentFeBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrCurrentFeBBER.setStatus("current")
_AdGenOtnOduPm24HrCurrentFeES_Type = Counter32
_AdGenOtnOduPm24HrCurrentFeES_Object = MibTableColumn
adGenOtnOduPm24HrCurrentFeES = _AdGenOtnOduPm24HrCurrentFeES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 7, 1, 12),
    _AdGenOtnOduPm24HrCurrentFeES_Type()
)
adGenOtnOduPm24HrCurrentFeES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrCurrentFeES.setStatus("current")
_AdGenOtnOduPm24HrCurrentFeSES_Type = Counter32
_AdGenOtnOduPm24HrCurrentFeSES_Object = MibTableColumn
adGenOtnOduPm24HrCurrentFeSES = _AdGenOtnOduPm24HrCurrentFeSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 7, 1, 13),
    _AdGenOtnOduPm24HrCurrentFeSES_Type()
)
adGenOtnOduPm24HrCurrentFeSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrCurrentFeSES.setStatus("current")
_AdGenOtnOduPm24HrCurrentFeESR_Type = Counter32
_AdGenOtnOduPm24HrCurrentFeESR_Object = MibTableColumn
adGenOtnOduPm24HrCurrentFeESR = _AdGenOtnOduPm24HrCurrentFeESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 7, 1, 14),
    _AdGenOtnOduPm24HrCurrentFeESR_Type()
)
adGenOtnOduPm24HrCurrentFeESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrCurrentFeESR.setStatus("current")
_AdGenOtnOduPm24HrCurrentFeSESR_Type = Counter32
_AdGenOtnOduPm24HrCurrentFeSESR_Object = MibTableColumn
adGenOtnOduPm24HrCurrentFeSESR = _AdGenOtnOduPm24HrCurrentFeSESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 7, 1, 15),
    _AdGenOtnOduPm24HrCurrentFeSESR_Type()
)
adGenOtnOduPm24HrCurrentFeSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrCurrentFeSESR.setStatus("current")
_AdGenOtnOduPm24HrCurrentFeUAS_Type = Counter32
_AdGenOtnOduPm24HrCurrentFeUAS_Object = MibTableColumn
adGenOtnOduPm24HrCurrentFeUAS = _AdGenOtnOduPm24HrCurrentFeUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 7, 1, 16),
    _AdGenOtnOduPm24HrCurrentFeUAS_Type()
)
adGenOtnOduPm24HrCurrentFeUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrCurrentFeUAS.setStatus("current")
_AdGenOtnOduPm24HrIntervalTable_Object = MibTable
adGenOtnOduPm24HrIntervalTable = _AdGenOtnOduPm24HrIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 8)
)
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrIntervalTable.setStatus("current")
_AdGenOtnOduPm24HrIntervalEntry_Object = MibTableRow
adGenOtnOduPm24HrIntervalEntry = _AdGenOtnOduPm24HrIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 8, 1)
)
adGenOtnOduPm24HrIntervalEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
    (0, "ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduPm24HrInterval"),
)
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrIntervalEntry.setStatus("current")


class _AdGenOtnOduPm24HrInterval_Type(Integer32):
    """Custom type adGenOtnOduPm24HrInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AdGenOtnOduPm24HrInterval_Type.__name__ = "Integer32"
_AdGenOtnOduPm24HrInterval_Object = MibTableColumn
adGenOtnOduPm24HrInterval = _AdGenOtnOduPm24HrInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 8, 1, 1),
    _AdGenOtnOduPm24HrInterval_Type()
)
adGenOtnOduPm24HrInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrInterval.setStatus("current")
_AdGenOtnOduPm24HrIntervalNeEB_Type = Counter32
_AdGenOtnOduPm24HrIntervalNeEB_Object = MibTableColumn
adGenOtnOduPm24HrIntervalNeEB = _AdGenOtnOduPm24HrIntervalNeEB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 8, 1, 2),
    _AdGenOtnOduPm24HrIntervalNeEB_Type()
)
adGenOtnOduPm24HrIntervalNeEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrIntervalNeEB.setStatus("current")
_AdGenOtnOduPm24HrIntervalNeBBE_Type = Counter32
_AdGenOtnOduPm24HrIntervalNeBBE_Object = MibTableColumn
adGenOtnOduPm24HrIntervalNeBBE = _AdGenOtnOduPm24HrIntervalNeBBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 8, 1, 3),
    _AdGenOtnOduPm24HrIntervalNeBBE_Type()
)
adGenOtnOduPm24HrIntervalNeBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrIntervalNeBBE.setStatus("current")


class _AdGenOtnOduPm24HrIntervalNeBBER_Type(DisplayString):
    """Custom type adGenOtnOduPm24HrIntervalNeBBER based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_AdGenOtnOduPm24HrIntervalNeBBER_Type.__name__ = "DisplayString"
_AdGenOtnOduPm24HrIntervalNeBBER_Object = MibTableColumn
adGenOtnOduPm24HrIntervalNeBBER = _AdGenOtnOduPm24HrIntervalNeBBER_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 8, 1, 4),
    _AdGenOtnOduPm24HrIntervalNeBBER_Type()
)
adGenOtnOduPm24HrIntervalNeBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrIntervalNeBBER.setStatus("current")
_AdGenOtnOduPm24HrIntervalNeES_Type = Counter32
_AdGenOtnOduPm24HrIntervalNeES_Object = MibTableColumn
adGenOtnOduPm24HrIntervalNeES = _AdGenOtnOduPm24HrIntervalNeES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 8, 1, 5),
    _AdGenOtnOduPm24HrIntervalNeES_Type()
)
adGenOtnOduPm24HrIntervalNeES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrIntervalNeES.setStatus("current")
_AdGenOtnOduPm24HrIntervalNeSES_Type = Counter32
_AdGenOtnOduPm24HrIntervalNeSES_Object = MibTableColumn
adGenOtnOduPm24HrIntervalNeSES = _AdGenOtnOduPm24HrIntervalNeSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 8, 1, 6),
    _AdGenOtnOduPm24HrIntervalNeSES_Type()
)
adGenOtnOduPm24HrIntervalNeSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrIntervalNeSES.setStatus("current")
_AdGenOtnOduPm24HrIntervalNeESR_Type = Counter32
_AdGenOtnOduPm24HrIntervalNeESR_Object = MibTableColumn
adGenOtnOduPm24HrIntervalNeESR = _AdGenOtnOduPm24HrIntervalNeESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 8, 1, 7),
    _AdGenOtnOduPm24HrIntervalNeESR_Type()
)
adGenOtnOduPm24HrIntervalNeESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrIntervalNeESR.setStatus("current")
_AdGenOtnOduPm24HrIntervalNeSESR_Type = Counter32
_AdGenOtnOduPm24HrIntervalNeSESR_Object = MibTableColumn
adGenOtnOduPm24HrIntervalNeSESR = _AdGenOtnOduPm24HrIntervalNeSESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 8, 1, 8),
    _AdGenOtnOduPm24HrIntervalNeSESR_Type()
)
adGenOtnOduPm24HrIntervalNeSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrIntervalNeSESR.setStatus("current")
_AdGenOtnOduPm24HrIntervalNeUAS_Type = Counter32
_AdGenOtnOduPm24HrIntervalNeUAS_Object = MibTableColumn
adGenOtnOduPm24HrIntervalNeUAS = _AdGenOtnOduPm24HrIntervalNeUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 8, 1, 9),
    _AdGenOtnOduPm24HrIntervalNeUAS_Type()
)
adGenOtnOduPm24HrIntervalNeUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrIntervalNeUAS.setStatus("current")
_AdGenOtnOduPm24HrIntervalFeEB_Type = Counter32
_AdGenOtnOduPm24HrIntervalFeEB_Object = MibTableColumn
adGenOtnOduPm24HrIntervalFeEB = _AdGenOtnOduPm24HrIntervalFeEB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 8, 1, 10),
    _AdGenOtnOduPm24HrIntervalFeEB_Type()
)
adGenOtnOduPm24HrIntervalFeEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrIntervalFeEB.setStatus("current")
_AdGenOtnOduPm24HrIntervalFeBBE_Type = Counter32
_AdGenOtnOduPm24HrIntervalFeBBE_Object = MibTableColumn
adGenOtnOduPm24HrIntervalFeBBE = _AdGenOtnOduPm24HrIntervalFeBBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 8, 1, 11),
    _AdGenOtnOduPm24HrIntervalFeBBE_Type()
)
adGenOtnOduPm24HrIntervalFeBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrIntervalFeBBE.setStatus("current")


class _AdGenOtnOduPm24HrIntervalFeBBER_Type(DisplayString):
    """Custom type adGenOtnOduPm24HrIntervalFeBBER based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_AdGenOtnOduPm24HrIntervalFeBBER_Type.__name__ = "DisplayString"
_AdGenOtnOduPm24HrIntervalFeBBER_Object = MibTableColumn
adGenOtnOduPm24HrIntervalFeBBER = _AdGenOtnOduPm24HrIntervalFeBBER_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 8, 1, 12),
    _AdGenOtnOduPm24HrIntervalFeBBER_Type()
)
adGenOtnOduPm24HrIntervalFeBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrIntervalFeBBER.setStatus("current")
_AdGenOtnOduPm24HrIntervalFeES_Type = Counter32
_AdGenOtnOduPm24HrIntervalFeES_Object = MibTableColumn
adGenOtnOduPm24HrIntervalFeES = _AdGenOtnOduPm24HrIntervalFeES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 8, 1, 13),
    _AdGenOtnOduPm24HrIntervalFeES_Type()
)
adGenOtnOduPm24HrIntervalFeES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrIntervalFeES.setStatus("current")
_AdGenOtnOduPm24HrIntervalFeSES_Type = Counter32
_AdGenOtnOduPm24HrIntervalFeSES_Object = MibTableColumn
adGenOtnOduPm24HrIntervalFeSES = _AdGenOtnOduPm24HrIntervalFeSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 8, 1, 14),
    _AdGenOtnOduPm24HrIntervalFeSES_Type()
)
adGenOtnOduPm24HrIntervalFeSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrIntervalFeSES.setStatus("current")
_AdGenOtnOduPm24HrIntervalFeESR_Type = Counter32
_AdGenOtnOduPm24HrIntervalFeESR_Object = MibTableColumn
adGenOtnOduPm24HrIntervalFeESR = _AdGenOtnOduPm24HrIntervalFeESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 8, 1, 15),
    _AdGenOtnOduPm24HrIntervalFeESR_Type()
)
adGenOtnOduPm24HrIntervalFeESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrIntervalFeESR.setStatus("current")
_AdGenOtnOduPm24HrIntervalFeSESR_Type = Counter32
_AdGenOtnOduPm24HrIntervalFeSESR_Object = MibTableColumn
adGenOtnOduPm24HrIntervalFeSESR = _AdGenOtnOduPm24HrIntervalFeSESR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 8, 1, 16),
    _AdGenOtnOduPm24HrIntervalFeSESR_Type()
)
adGenOtnOduPm24HrIntervalFeSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrIntervalFeSESR.setStatus("current")
_AdGenOtnOduPm24HrIntervalFeUAS_Type = Counter32
_AdGenOtnOduPm24HrIntervalFeUAS_Object = MibTableColumn
adGenOtnOduPm24HrIntervalFeUAS = _AdGenOtnOduPm24HrIntervalFeUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 8, 1, 17),
    _AdGenOtnOduPm24HrIntervalFeUAS_Type()
)
adGenOtnOduPm24HrIntervalFeUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrIntervalFeUAS.setStatus("current")
_AdGenOtnOduPm24HrIntervalNeValidData_Type = TruthValue
_AdGenOtnOduPm24HrIntervalNeValidData_Object = MibTableColumn
adGenOtnOduPm24HrIntervalNeValidData = _AdGenOtnOduPm24HrIntervalNeValidData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 8, 1, 18),
    _AdGenOtnOduPm24HrIntervalNeValidData_Type()
)
adGenOtnOduPm24HrIntervalNeValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrIntervalNeValidData.setStatus("current")
_AdGenOtnOduPm24HrIntervalFeValidData_Type = TruthValue
_AdGenOtnOduPm24HrIntervalFeValidData_Object = MibTableColumn
adGenOtnOduPm24HrIntervalFeValidData = _AdGenOtnOduPm24HrIntervalFeValidData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 8, 1, 19),
    _AdGenOtnOduPm24HrIntervalFeValidData_Type()
)
adGenOtnOduPm24HrIntervalFeValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduPm24HrIntervalFeValidData.setStatus("current")
_AdGenOtnOtuCountersTable_Object = MibTable
adGenOtnOtuCountersTable = _AdGenOtnOtuCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 9)
)
if mibBuilder.loadTexts:
    adGenOtnOtuCountersTable.setStatus("current")
_AdGenOtnOtuCountersEntry_Object = MibTableRow
adGenOtnOtuCountersEntry = _AdGenOtnOtuCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 9, 1)
)
adGenOtnOtuCountersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenOtnOtuCountersEntry.setStatus("current")
_AdGenOtnOtuCounterNeEB_Type = Counter64
_AdGenOtnOtuCounterNeEB_Object = MibTableColumn
adGenOtnOtuCounterNeEB = _AdGenOtnOtuCounterNeEB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 9, 1, 1),
    _AdGenOtnOtuCounterNeEB_Type()
)
adGenOtnOtuCounterNeEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuCounterNeEB.setStatus("current")
_AdGenOtnOtuCounterNeBBE_Type = Counter64
_AdGenOtnOtuCounterNeBBE_Object = MibTableColumn
adGenOtnOtuCounterNeBBE = _AdGenOtnOtuCounterNeBBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 9, 1, 2),
    _AdGenOtnOtuCounterNeBBE_Type()
)
adGenOtnOtuCounterNeBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuCounterNeBBE.setStatus("current")
_AdGenOtnOtuCounterNeES_Type = Counter64
_AdGenOtnOtuCounterNeES_Object = MibTableColumn
adGenOtnOtuCounterNeES = _AdGenOtnOtuCounterNeES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 9, 1, 3),
    _AdGenOtnOtuCounterNeES_Type()
)
adGenOtnOtuCounterNeES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuCounterNeES.setStatus("current")
_AdGenOtnOtuCounterNeSES_Type = Counter64
_AdGenOtnOtuCounterNeSES_Object = MibTableColumn
adGenOtnOtuCounterNeSES = _AdGenOtnOtuCounterNeSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 9, 1, 4),
    _AdGenOtnOtuCounterNeSES_Type()
)
adGenOtnOtuCounterNeSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuCounterNeSES.setStatus("current")
_AdGenOtnOtuCounterNeUAS_Type = Counter64
_AdGenOtnOtuCounterNeUAS_Object = MibTableColumn
adGenOtnOtuCounterNeUAS = _AdGenOtnOtuCounterNeUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 9, 1, 5),
    _AdGenOtnOtuCounterNeUAS_Type()
)
adGenOtnOtuCounterNeUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuCounterNeUAS.setStatus("current")
_AdGenOtnOtuCounterFeEB_Type = Counter64
_AdGenOtnOtuCounterFeEB_Object = MibTableColumn
adGenOtnOtuCounterFeEB = _AdGenOtnOtuCounterFeEB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 9, 1, 6),
    _AdGenOtnOtuCounterFeEB_Type()
)
adGenOtnOtuCounterFeEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuCounterFeEB.setStatus("current")
_AdGenOtnOtuCounterFeBBE_Type = Counter64
_AdGenOtnOtuCounterFeBBE_Object = MibTableColumn
adGenOtnOtuCounterFeBBE = _AdGenOtnOtuCounterFeBBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 9, 1, 7),
    _AdGenOtnOtuCounterFeBBE_Type()
)
adGenOtnOtuCounterFeBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuCounterFeBBE.setStatus("current")
_AdGenOtnOtuCounterFeES_Type = Counter64
_AdGenOtnOtuCounterFeES_Object = MibTableColumn
adGenOtnOtuCounterFeES = _AdGenOtnOtuCounterFeES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 9, 1, 8),
    _AdGenOtnOtuCounterFeES_Type()
)
adGenOtnOtuCounterFeES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuCounterFeES.setStatus("current")
_AdGenOtnOtuCounterFeSES_Type = Counter64
_AdGenOtnOtuCounterFeSES_Object = MibTableColumn
adGenOtnOtuCounterFeSES = _AdGenOtnOtuCounterFeSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 9, 1, 9),
    _AdGenOtnOtuCounterFeSES_Type()
)
adGenOtnOtuCounterFeSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuCounterFeSES.setStatus("current")
_AdGenOtnOtuCounterFeUAS_Type = Counter64
_AdGenOtnOtuCounterFeUAS_Object = MibTableColumn
adGenOtnOtuCounterFeUAS = _AdGenOtnOtuCounterFeUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 9, 1, 10),
    _AdGenOtnOtuCounterFeUAS_Type()
)
adGenOtnOtuCounterFeUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuCounterFeUAS.setStatus("current")
_AdGenOtnOtuCounterFecCorrBits_Type = Counter64
_AdGenOtnOtuCounterFecCorrBits_Object = MibTableColumn
adGenOtnOtuCounterFecCorrBits = _AdGenOtnOtuCounterFecCorrBits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 9, 1, 11),
    _AdGenOtnOtuCounterFecCorrBits_Type()
)
adGenOtnOtuCounterFecCorrBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuCounterFecCorrBits.setStatus("current")
_AdGenOtnOtuCounterFecUnCorrBlks_Type = Counter64
_AdGenOtnOtuCounterFecUnCorrBlks_Object = MibTableColumn
adGenOtnOtuCounterFecUnCorrBlks = _AdGenOtnOtuCounterFecUnCorrBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 9, 1, 12),
    _AdGenOtnOtuCounterFecUnCorrBlks_Type()
)
adGenOtnOtuCounterFecUnCorrBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOtuCounterFecUnCorrBlks.setStatus("current")
_AdGenOtnOduCountersTable_Object = MibTable
adGenOtnOduCountersTable = _AdGenOtnOduCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 10)
)
if mibBuilder.loadTexts:
    adGenOtnOduCountersTable.setStatus("current")
_AdGenOtnOduCountersEntry_Object = MibTableRow
adGenOtnOduCountersEntry = _AdGenOtnOduCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 10, 1)
)
adGenOtnOduCountersEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
)
if mibBuilder.loadTexts:
    adGenOtnOduCountersEntry.setStatus("current")
_AdGenOtnOduCounterNeEB_Type = Counter64
_AdGenOtnOduCounterNeEB_Object = MibTableColumn
adGenOtnOduCounterNeEB = _AdGenOtnOduCounterNeEB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 10, 1, 1),
    _AdGenOtnOduCounterNeEB_Type()
)
adGenOtnOduCounterNeEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduCounterNeEB.setStatus("current")
_AdGenOtnOduCounterNeBBE_Type = Counter64
_AdGenOtnOduCounterNeBBE_Object = MibTableColumn
adGenOtnOduCounterNeBBE = _AdGenOtnOduCounterNeBBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 10, 1, 2),
    _AdGenOtnOduCounterNeBBE_Type()
)
adGenOtnOduCounterNeBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduCounterNeBBE.setStatus("current")
_AdGenOtnOduCounterNeES_Type = Counter64
_AdGenOtnOduCounterNeES_Object = MibTableColumn
adGenOtnOduCounterNeES = _AdGenOtnOduCounterNeES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 10, 1, 3),
    _AdGenOtnOduCounterNeES_Type()
)
adGenOtnOduCounterNeES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduCounterNeES.setStatus("current")
_AdGenOtnOduCounterNeSES_Type = Counter64
_AdGenOtnOduCounterNeSES_Object = MibTableColumn
adGenOtnOduCounterNeSES = _AdGenOtnOduCounterNeSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 10, 1, 4),
    _AdGenOtnOduCounterNeSES_Type()
)
adGenOtnOduCounterNeSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduCounterNeSES.setStatus("current")
_AdGenOtnOduCounterNeUAS_Type = Counter64
_AdGenOtnOduCounterNeUAS_Object = MibTableColumn
adGenOtnOduCounterNeUAS = _AdGenOtnOduCounterNeUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 10, 1, 5),
    _AdGenOtnOduCounterNeUAS_Type()
)
adGenOtnOduCounterNeUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduCounterNeUAS.setStatus("current")
_AdGenOtnOduCounterFeEB_Type = Counter64
_AdGenOtnOduCounterFeEB_Object = MibTableColumn
adGenOtnOduCounterFeEB = _AdGenOtnOduCounterFeEB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 10, 1, 6),
    _AdGenOtnOduCounterFeEB_Type()
)
adGenOtnOduCounterFeEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduCounterFeEB.setStatus("current")
_AdGenOtnOduCounterFeBBE_Type = Counter64
_AdGenOtnOduCounterFeBBE_Object = MibTableColumn
adGenOtnOduCounterFeBBE = _AdGenOtnOduCounterFeBBE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 10, 1, 7),
    _AdGenOtnOduCounterFeBBE_Type()
)
adGenOtnOduCounterFeBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduCounterFeBBE.setStatus("current")
_AdGenOtnOduCounterFeES_Type = Counter64
_AdGenOtnOduCounterFeES_Object = MibTableColumn
adGenOtnOduCounterFeES = _AdGenOtnOduCounterFeES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 10, 1, 8),
    _AdGenOtnOduCounterFeES_Type()
)
adGenOtnOduCounterFeES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduCounterFeES.setStatus("current")
_AdGenOtnOduCounterFeSES_Type = Counter64
_AdGenOtnOduCounterFeSES_Object = MibTableColumn
adGenOtnOduCounterFeSES = _AdGenOtnOduCounterFeSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 10, 1, 9),
    _AdGenOtnOduCounterFeSES_Type()
)
adGenOtnOduCounterFeSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduCounterFeSES.setStatus("current")
_AdGenOtnOduCounterFeUAS_Type = Counter64
_AdGenOtnOduCounterFeUAS_Object = MibTableColumn
adGenOtnOduCounterFeUAS = _AdGenOtnOduCounterFeUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 4, 10, 1, 10),
    _AdGenOtnOduCounterFeUAS_Type()
)
adGenOtnOduCounterFeUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnOduCounterFeUAS.setStatus("current")
_AdGenOtnPmInterface_ObjectIdentity = ObjectIdentity
adGenOtnPmInterface = _AdGenOtnPmInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 5)
)
_AdGenOtnPmInterfaceTable_Object = MibTable
adGenOtnPmInterfaceTable = _AdGenOtnPmInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 5, 1)
)
if mibBuilder.loadTexts:
    adGenOtnPmInterfaceTable.setStatus("current")
_AdGenOtnPmInterfaceEntry_Object = MibTableRow
adGenOtnPmInterfaceEntry = _AdGenOtnPmInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 5, 1, 1)
)
adGenOtnPmInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenOtnPmInterfaceEntry.setStatus("current")


class _AdGenOtnPmInterface15MinValidIntervals_Type(Integer32):
    """Custom type adGenOtnPmInterface15MinValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdGenOtnPmInterface15MinValidIntervals_Type.__name__ = "Integer32"
_AdGenOtnPmInterface15MinValidIntervals_Object = MibTableColumn
adGenOtnPmInterface15MinValidIntervals = _AdGenOtnPmInterface15MinValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 5, 1, 1, 1),
    _AdGenOtnPmInterface15MinValidIntervals_Type()
)
adGenOtnPmInterface15MinValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnPmInterface15MinValidIntervals.setStatus("current")


class _AdGenOtnPmInterface24HrValidIntervals_Type(Integer32):
    """Custom type adGenOtnPmInterface24HrValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenOtnPmInterface24HrValidIntervals_Type.__name__ = "Integer32"
_AdGenOtnPmInterface24HrValidIntervals_Object = MibTableColumn
adGenOtnPmInterface24HrValidIntervals = _AdGenOtnPmInterface24HrValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 5, 1, 1, 2),
    _AdGenOtnPmInterface24HrValidIntervals_Type()
)
adGenOtnPmInterface24HrValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOtnPmInterface24HrValidIntervals.setStatus("current")


class _AdGenOtnPmInterfaceResetPM_Type(Integer32):
    """Custom type adGenOtnPmInterfaceResetPM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenOtnPmInterfaceResetPM_Type.__name__ = "Integer32"
_AdGenOtnPmInterfaceResetPM_Object = MibTableColumn
adGenOtnPmInterfaceResetPM = _AdGenOtnPmInterfaceResetPM_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 5, 1, 1, 3),
    _AdGenOtnPmInterfaceResetPM_Type()
)
adGenOtnPmInterfaceResetPM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnPmInterfaceResetPM.setStatus("current")
_AdGenOtnPmSlot_ObjectIdentity = ObjectIdentity
adGenOtnPmSlot = _AdGenOtnPmSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 6)
)
_AdGenOtnPmSlotTable_Object = MibTable
adGenOtnPmSlotTable = _AdGenOtnPmSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 6, 1)
)
if mibBuilder.loadTexts:
    adGenOtnPmSlotTable.setStatus("current")
_AdGenOtnPmSlotEntry_Object = MibTableRow
adGenOtnPmSlotEntry = _AdGenOtnPmSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 6, 1, 1)
)
adGenOtnPmSlotEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenOtnPmSlotEntry.setStatus("current")


class _AdGenOtnPmResetAllPMData_Type(Integer32):
    """Custom type adGenOtnPmResetAllPMData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenOtnPmResetAllPMData_Type.__name__ = "Integer32"
_AdGenOtnPmResetAllPMData_Object = MibTableColumn
adGenOtnPmResetAllPMData = _AdGenOtnPmResetAllPMData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 6, 1, 1, 1),
    _AdGenOtnPmResetAllPMData_Type()
)
adGenOtnPmResetAllPMData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOtnPmResetAllPMData.setStatus("current")
_AdGenOtnOtuAlms_ObjectIdentity = ObjectIdentity
adGenOtnOtuAlms = _AdGenOtnOtuAlms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 10)
)
_AdGenOtnOtuAlarms_ObjectIdentity = ObjectIdentity
adGenOtnOtuAlarms = _AdGenOtnOtuAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 10, 0)
)
_AdGenOtnOduAlms_ObjectIdentity = ObjectIdentity
adGenOtnOduAlms = _AdGenOtnOduAlms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 11)
)
_AdGenOtnOduAlarms_ObjectIdentity = ObjectIdentity
adGenOtnOduAlarms = _AdGenOtnOduAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 11, 0)
)
_AdGenOtnOtuPmThres15MinAlms_ObjectIdentity = ObjectIdentity
adGenOtnOtuPmThres15MinAlms = _AdGenOtnOtuPmThres15MinAlms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 12)
)
_AdGenOtnOtuPmThres15MinAlarms_ObjectIdentity = ObjectIdentity
adGenOtnOtuPmThres15MinAlarms = _AdGenOtnOtuPmThres15MinAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 12, 0)
)
_AdGenOtnOtuPmThres24HrAlms_ObjectIdentity = ObjectIdentity
adGenOtnOtuPmThres24HrAlms = _AdGenOtnOtuPmThres24HrAlms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 13)
)
_AdGenOtnOtuPmThres24HrAlarms_ObjectIdentity = ObjectIdentity
adGenOtnOtuPmThres24HrAlarms = _AdGenOtnOtuPmThres24HrAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 13, 0)
)
_AdGenOtnOduPmThres15MinAlms_ObjectIdentity = ObjectIdentity
adGenOtnOduPmThres15MinAlms = _AdGenOtnOduPmThres15MinAlms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 14)
)
_AdGenOtnOduPmThres15MinAlarms_ObjectIdentity = ObjectIdentity
adGenOtnOduPmThres15MinAlarms = _AdGenOtnOduPmThres15MinAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 14, 0)
)
_AdGenOtnOduPmThres24HrAlms_ObjectIdentity = ObjectIdentity
adGenOtnOduPmThres24HrAlms = _AdGenOtnOduPmThres24HrAlms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 15)
)
_AdGenOtnOduPmThres24HrAlarms_ObjectIdentity = ObjectIdentity
adGenOtnOduPmThres24HrAlarms = _AdGenOtnOduPmThres24HrAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 15, 0)
)

# Managed Objects groups


# Notification objects

adGenOtnOtuLosClrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 10, 0, 2)
)
adGenOtnOtuLosClrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuLosClrAlm.setStatus(
        "current"
    )

adGenOtnOtuLosActAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 10, 0, 3)
)
adGenOtnOtuLosActAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuLosActAlm.setStatus(
        "current"
    )

adGenOtnOtuLofClrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 10, 0, 4)
)
adGenOtnOtuLofClrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuLofClrAlm.setStatus(
        "current"
    )

adGenOtnOtuLofActAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 10, 0, 5)
)
adGenOtnOtuLofActAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuLofActAlm.setStatus(
        "current"
    )

adGenOtnOtuLomClrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 10, 0, 6)
)
adGenOtnOtuLomClrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuLomClrAlm.setStatus(
        "current"
    )

adGenOtnOtuLomActAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 10, 0, 7)
)
adGenOtnOtuLomActAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuLomActAlm.setStatus(
        "current"
    )

adGenOtnOtuAisClrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 10, 0, 8)
)
adGenOtnOtuAisClrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuAisClrAlm.setStatus(
        "current"
    )

adGenOtnOtuAisActAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 10, 0, 9)
)
adGenOtnOtuAisActAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuAisActAlm.setStatus(
        "current"
    )

adGenOtnOtuBdiClrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 10, 0, 10)
)
adGenOtnOtuBdiClrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuBdiClrAlm.setStatus(
        "current"
    )

adGenOtnOtuBdiActAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 10, 0, 11)
)
adGenOtnOtuBdiActAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuBdiActAlm.setStatus(
        "current"
    )

adGenOtnOtuTimClrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 10, 0, 12)
)
adGenOtnOtuTimClrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuTimClrAlm.setStatus(
        "current"
    )

adGenOtnOtuTimActAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 10, 0, 13)
)
adGenOtnOtuTimActAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuTimActAlm.setStatus(
        "current"
    )

adGenOtnOtuDegClrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 10, 0, 14)
)
adGenOtnOtuDegClrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuDegClrAlm.setStatus(
        "current"
    )

adGenOtnOtuDegActAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 10, 0, 15)
)
adGenOtnOtuDegActAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuDegActAlm.setStatus(
        "current"
    )

adGenOtnOduLofLomClrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 11, 0, 2)
)
adGenOtnOduLofLomClrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduLofLomClrAlm.setStatus(
        "current"
    )

adGenOtnOduLofLomActAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 11, 0, 3)
)
adGenOtnOduLofLomActAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduLofLomActAlm.setStatus(
        "current"
    )

adGenOtnOduBdiClrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 11, 0, 4)
)
adGenOtnOduBdiClrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduBdiClrAlm.setStatus(
        "current"
    )

adGenOtnOduBdiActAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 11, 0, 5)
)
adGenOtnOduBdiActAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduBdiActAlm.setStatus(
        "current"
    )

adGenOtnOduOciClrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 11, 0, 6)
)
adGenOtnOduOciClrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduOciClrAlm.setStatus(
        "current"
    )

adGenOtnOduOciActAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 11, 0, 7)
)
adGenOtnOduOciActAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduOciActAlm.setStatus(
        "current"
    )

adGenOtnOduTimClrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 11, 0, 8)
)
adGenOtnOduTimClrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduTimClrAlm.setStatus(
        "current"
    )

adGenOtnOduTimActAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 11, 0, 9)
)
adGenOtnOduTimActAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduTimActAlm.setStatus(
        "current"
    )

adGenOtnOduDegClrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 11, 0, 10)
)
adGenOtnOduDegClrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduDegClrAlm.setStatus(
        "current"
    )

adGenOtnOduDegActAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 11, 0, 11)
)
adGenOtnOduDegActAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduDegActAlm.setStatus(
        "current"
    )

adGenOtnOduPlmClrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 11, 0, 12)
)
adGenOtnOduPlmClrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPlmClrAlm.setStatus(
        "current"
    )

adGenOtnOduPlmActAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 11, 0, 13)
)
adGenOtnOduPlmActAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPlmActAlm.setStatus(
        "current"
    )

adGenOtnOduLckClrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 11, 0, 14)
)
adGenOtnOduLckClrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduLckClrAlm.setStatus(
        "current"
    )

adGenOtnOduLckActAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 11, 0, 15)
)
adGenOtnOduLckActAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduLckActAlm.setStatus(
        "current"
    )

adGenOtnOduAisClrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 11, 0, 16)
)
adGenOtnOduAisClrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduAisClrAlm.setStatus(
        "current"
    )

adGenOtnOduAisActAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 11, 0, 17)
)
adGenOtnOduAisActAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduAisActAlm.setStatus(
        "current"
    )

adGenOtnOduMsimClrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 11, 0, 18)
)
adGenOtnOduMsimClrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduMsimClrAlm.setStatus(
        "current"
    )

adGenOtnOduMsimActAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 11, 0, 19)
)
adGenOtnOduMsimActAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduMsimActAlm.setStatus(
        "current"
    )

adGenOtnOduCsfClrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 11, 0, 20)
)
adGenOtnOduCsfClrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduCsfClrAlm.setStatus(
        "current"
    )

adGenOtnOduCsfActAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 11, 0, 21)
)
adGenOtnOduCsfActAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduCsfActAlm.setStatus(
        "current"
    )

adGenOtnOduLoomfiClrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 11, 0, 22)
)
adGenOtnOduLoomfiClrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduLoomfiClrAlm.setStatus(
        "current"
    )

adGenOtnOduLoomfiActAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 11, 0, 23)
)
adGenOtnOduLoomfiActAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduLoomfiActAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres15MinNeEbAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 12, 0, 3)
)
adGenOtnOtuPmThres15MinNeEbAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinNeEbAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres15MinNeBbeAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 12, 0, 5)
)
adGenOtnOtuPmThres15MinNeBbeAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinNeBbeAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres15MinNeBberAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 12, 0, 7)
)
adGenOtnOtuPmThres15MinNeBberAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinNeBberAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres15MinNeEsAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 12, 0, 9)
)
adGenOtnOtuPmThres15MinNeEsAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinNeEsAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres15MinNeSesAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 12, 0, 11)
)
adGenOtnOtuPmThres15MinNeSesAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinNeSesAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres15MinNeEsrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 12, 0, 13)
)
adGenOtnOtuPmThres15MinNeEsrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinNeEsrAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres15MinNeSesrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 12, 0, 15)
)
adGenOtnOtuPmThres15MinNeSesrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinNeSesrAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres15MinNeUasAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 12, 0, 17)
)
adGenOtnOtuPmThres15MinNeUasAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinNeUasAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres15MinFeEbAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 12, 0, 19)
)
adGenOtnOtuPmThres15MinFeEbAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinFeEbAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres15MinFeBbeAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 12, 0, 21)
)
adGenOtnOtuPmThres15MinFeBbeAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinFeBbeAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres15MinFeBberAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 12, 0, 23)
)
adGenOtnOtuPmThres15MinFeBberAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinFeBberAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres15MinFeEsAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 12, 0, 25)
)
adGenOtnOtuPmThres15MinFeEsAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinFeEsAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres15MinFeSesAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 12, 0, 27)
)
adGenOtnOtuPmThres15MinFeSesAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinFeSesAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres15MinFeEsrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 12, 0, 29)
)
adGenOtnOtuPmThres15MinFeEsrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinFeEsrAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres15MinFeSesrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 12, 0, 31)
)
adGenOtnOtuPmThres15MinFeSesrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinFeSesrAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres15MinFeUasAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 12, 0, 33)
)
adGenOtnOtuPmThres15MinFeUasAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinFeUasAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres15MinFecCorrBitsAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 12, 0, 35)
)
adGenOtnOtuPmThres15MinFecCorrBitsAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinFecCorrBitsAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres15MinFecCorrOnesAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 12, 0, 37)
)
adGenOtnOtuPmThres15MinFecCorrOnesAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinFecCorrOnesAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres15MinFecCorrZerosAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 12, 0, 39)
)
adGenOtnOtuPmThres15MinFecCorrZerosAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinFecCorrZerosAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres15MinFecUncorrBlksAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 12, 0, 41)
)
adGenOtnOtuPmThres15MinFecUncorrBlksAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinFecUncorrBlksAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres15MinFecCorrBerAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 12, 0, 43)
)
adGenOtnOtuPmThres15MinFecCorrBerAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres15MinFecCorrBerAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres24HrNeEbAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 13, 0, 3)
)
adGenOtnOtuPmThres24HrNeEbAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrNeEbAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres24HrNeBbeAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 13, 0, 5)
)
adGenOtnOtuPmThres24HrNeBbeAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrNeBbeAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres24HrNeBberAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 13, 0, 7)
)
adGenOtnOtuPmThres24HrNeBberAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrNeBberAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres24HrNeEsAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 13, 0, 9)
)
adGenOtnOtuPmThres24HrNeEsAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrNeEsAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres24HrNeSesAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 13, 0, 11)
)
adGenOtnOtuPmThres24HrNeSesAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrNeSesAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres24HrNeEsrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 13, 0, 13)
)
adGenOtnOtuPmThres24HrNeEsrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrNeEsrAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres24HrNeSesrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 13, 0, 15)
)
adGenOtnOtuPmThres24HrNeSesrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrNeSesrAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres24HrNeUasAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 13, 0, 17)
)
adGenOtnOtuPmThres24HrNeUasAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrNeUasAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres24HrFeEbAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 13, 0, 19)
)
adGenOtnOtuPmThres24HrFeEbAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrFeEbAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres24HrFeBbeAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 13, 0, 21)
)
adGenOtnOtuPmThres24HrFeBbeAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrFeBbeAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres24HrFeBberAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 13, 0, 23)
)
adGenOtnOtuPmThres24HrFeBberAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrFeBberAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres24HrFeEsAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 13, 0, 25)
)
adGenOtnOtuPmThres24HrFeEsAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrFeEsAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres24HrFeSesAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 13, 0, 27)
)
adGenOtnOtuPmThres24HrFeSesAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrFeSesAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres24HrFeEsrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 13, 0, 29)
)
adGenOtnOtuPmThres24HrFeEsrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrFeEsrAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres24HrFeSesrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 13, 0, 31)
)
adGenOtnOtuPmThres24HrFeSesrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrFeSesrAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres24HrFeUasAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 13, 0, 33)
)
adGenOtnOtuPmThres24HrFeUasAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrFeUasAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres24HrFecCorrBitsAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 13, 0, 35)
)
adGenOtnOtuPmThres24HrFecCorrBitsAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrFecCorrBitsAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres24HrFecCorrOnesAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 13, 0, 37)
)
adGenOtnOtuPmThres24HrFecCorrOnesAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrFecCorrOnesAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres24HrFecCorrZerosAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 13, 0, 39)
)
adGenOtnOtuPmThres24HrFecCorrZerosAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrFecCorrZerosAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres24HrFecUncorrBlksAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 13, 0, 41)
)
adGenOtnOtuPmThres24HrFecUncorrBlksAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrFecUncorrBlksAlm.setStatus(
        "current"
    )

adGenOtnOtuPmThres24HrFecCorrBerAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 13, 0, 43)
)
adGenOtnOtuPmThres24HrFecCorrBerAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOtuPmThres24HrFecCorrBerAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres15MinNeEbAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 14, 0, 3)
)
adGenOtnOduPmThres15MinNeEbAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinNeEbAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres15MinNeBbeAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 14, 0, 5)
)
adGenOtnOduPmThres15MinNeBbeAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinNeBbeAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres15MinNeBberAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 14, 0, 7)
)
adGenOtnOduPmThres15MinNeBberAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinNeBberAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres15MinNeEsAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 14, 0, 9)
)
adGenOtnOduPmThres15MinNeEsAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinNeEsAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres15MinNeSesAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 14, 0, 11)
)
adGenOtnOduPmThres15MinNeSesAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinNeSesAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres15MinNeEsrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 14, 0, 13)
)
adGenOtnOduPmThres15MinNeEsrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinNeEsrAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres15MinNeSesrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 14, 0, 15)
)
adGenOtnOduPmThres15MinNeSesrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinNeSesrAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres15MinNeUasAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 14, 0, 17)
)
adGenOtnOduPmThres15MinNeUasAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinNeUasAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres15MinFeEbAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 14, 0, 19)
)
adGenOtnOduPmThres15MinFeEbAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinFeEbAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres15MinFeBbeAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 14, 0, 21)
)
adGenOtnOduPmThres15MinFeBbeAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinFeBbeAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres15MinFeBberAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 14, 0, 23)
)
adGenOtnOduPmThres15MinFeBberAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinFeBberAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres15MinFeEsAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 14, 0, 25)
)
adGenOtnOduPmThres15MinFeEsAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinFeEsAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres15MinFeSesAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 14, 0, 27)
)
adGenOtnOduPmThres15MinFeSesAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinFeSesAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres15MinFeEsrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 14, 0, 29)
)
adGenOtnOduPmThres15MinFeEsrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinFeEsrAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres15MinFeSesrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 14, 0, 31)
)
adGenOtnOduPmThres15MinFeSesrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinFeSesrAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres15MinFeUasAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 14, 0, 33)
)
adGenOtnOduPmThres15MinFeUasAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres15MinFeUasAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres24HrNeEbAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 15, 0, 3)
)
adGenOtnOduPmThres24HrNeEbAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrNeEbAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres24HrNeBbeAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 15, 0, 5)
)
adGenOtnOduPmThres24HrNeBbeAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrNeBbeAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres24HrNeBberAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 15, 0, 7)
)
adGenOtnOduPmThres24HrNeBberAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrNeBberAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres24HrNeEsAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 15, 0, 9)
)
adGenOtnOduPmThres24HrNeEsAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrNeEsAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres24HrNeSesAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 15, 0, 11)
)
adGenOtnOduPmThres24HrNeSesAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrNeSesAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres24HrNeEsrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 15, 0, 13)
)
adGenOtnOduPmThres24HrNeEsrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrNeEsrAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres24HrNeSesrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 15, 0, 15)
)
adGenOtnOduPmThres24HrNeSesrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrNeSesrAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres24HrNeUasAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 15, 0, 17)
)
adGenOtnOduPmThres24HrNeUasAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrNeUasAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres24HrFeEbAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 15, 0, 19)
)
adGenOtnOduPmThres24HrFeEbAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrFeEbAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres24HrFeBbeAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 15, 0, 21)
)
adGenOtnOduPmThres24HrFeBbeAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrFeBbeAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres24HrFeBberAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 15, 0, 23)
)
adGenOtnOduPmThres24HrFeBberAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrFeBberAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres24HrFeEsAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 15, 0, 25)
)
adGenOtnOduPmThres24HrFeEsAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrFeEsAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres24HrFeSesAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 15, 0, 27)
)
adGenOtnOduPmThres24HrFeSesAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrFeSesAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres24HrFeEsrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 15, 0, 29)
)
adGenOtnOduPmThres24HrFeEsrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrFeEsrAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres24HrFeSesrAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 15, 0, 31)
)
adGenOtnOduPmThres24HrFeSesrAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrFeSesrAlm.setStatus(
        "current"
    )

adGenOtnOduPmThres24HrFeUasAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 44, 15, 0, 33)
)
adGenOtnOduPmThres24HrFeUasAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENERIC-OTN-MIB", "adGenOtnOduIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenOtnOduPmThres24HrFeUasAlm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENERIC-OTN-MIB",
    **{"AdGenOtnOduInterface": AdGenOtnOduInterface,
       "OtnProtGrpInterface": OtnProtGrpInterface,
       "OtnPayloadTypes": OtnPayloadTypes,
       "adGenOtnProv": adGenOtnProv,
       "adGenOtnOtuProvTable": adGenOtnOtuProvTable,
       "adGenOtnOtuProvEntry": adGenOtnOtuProvEntry,
       "adGenOtnOtuLastError": adGenOtnOtuLastError,
       "adGenOtnOtuMode": adGenOtnOtuMode,
       "adGenOtnOtuSupportedModes": adGenOtnOtuSupportedModes,
       "adGenOtnOtuDegradeMonitor": adGenOtnOtuDegradeMonitor,
       "adGenOtnOtuDegradeThres": adGenOtnOtuDegradeThres,
       "adGenOtnOtuTraceTxSapi": adGenOtnOtuTraceTxSapi,
       "adGenOtnOtuTraceTxDapi": adGenOtnOtuTraceTxDapi,
       "adGenOtnOtuTraceTxOperatorSpec": adGenOtnOtuTraceTxOperatorSpec,
       "adGenOtnOtuTraceRxSapi": adGenOtnOtuTraceRxSapi,
       "adGenOtnOtuTraceRxDapi": adGenOtnOtuTraceRxDapi,
       "adGenOtnOtuTraceRxOperatorSpec": adGenOtnOtuTraceRxOperatorSpec,
       "adGenOtnOtuTraceExpectedSapi": adGenOtnOtuTraceExpectedSapi,
       "adGenOtnOtuTraceExpectedDapi": adGenOtnOtuTraceExpectedDapi,
       "adGenOtnOtuTraceAlarmControl": adGenOtnOtuTraceAlarmControl,
       "adGenOtnOtuTraceInsertAisEnable": adGenOtnOtuTraceInsertAisEnable,
       "adGenOtnOtuFecType": adGenOtnOtuFecType,
       "adGenOtnOtuSupportedFecType": adGenOtnOtuSupportedFecType,
       "adGenOtnOtuTraceAutoTxOperatorSpecEnable": adGenOtnOtuTraceAutoTxOperatorSpecEnable,
       "adGenOtnOtuTraceTxOperatorSpecActual": adGenOtnOtuTraceTxOperatorSpecActual,
       "adGenOtnOduProvTable": adGenOtnOduProvTable,
       "adGenOtnOduProvEntry": adGenOtnOduProvEntry,
       "adGenOtnOduIndex": adGenOtnOduIndex,
       "adGenOtnOduLastError": adGenOtnOduLastError,
       "adGenOtnOduAdminStatus": adGenOtnOduAdminStatus,
       "adGenOtnOduOperStatus": adGenOtnOduOperStatus,
       "adGenOtnOduMode": adGenOtnOduMode,
       "adGenOtnOduSupportedModes": adGenOtnOduSupportedModes,
       "adGenOtnOduTimeslotBandwidth": adGenOtnOduTimeslotBandwidth,
       "adGenOtnOduRxPayloadLabel": adGenOtnOduRxPayloadLabel,
       "adGenOtnOduTxPayloadLabel": adGenOtnOduTxPayloadLabel,
       "adGenOtnOduProprietaryPayloadLabel": adGenOtnOduProprietaryPayloadLabel,
       "adGenOtnOduDegradeMonitor": adGenOtnOduDegradeMonitor,
       "adGenOtnOduDegradeThres": adGenOtnOduDegradeThres,
       "adGenOtnOduTraceTxSapi": adGenOtnOduTraceTxSapi,
       "adGenOtnOduTraceTxDapi": adGenOtnOduTraceTxDapi,
       "adGenOtnOduTraceTxOperatorSpec": adGenOtnOduTraceTxOperatorSpec,
       "adGenOtnOduTraceRxSapi": adGenOtnOduTraceRxSapi,
       "adGenOtnOduTraceRxDapi": adGenOtnOduTraceRxDapi,
       "adGenOtnOduTraceRxOperatorSpec": adGenOtnOduTraceRxOperatorSpec,
       "adGenOtnOduTraceExpectedSapi": adGenOtnOduTraceExpectedSapi,
       "adGenOtnOduTraceExpectedDapi": adGenOtnOduTraceExpectedDapi,
       "adGenOtnOduTraceAlarmControl": adGenOtnOduTraceAlarmControl,
       "adGenOtnOduTraceInsertAisEnable": adGenOtnOduTraceInsertAisEnable,
       "adGenOtnOduRowStatus": adGenOtnOduRowStatus,
       "adGenOtnOdu2Odu3AutoPayloadType": adGenOtnOdu2Odu3AutoPayloadType,
       "adGenOtnSlotProvTable": adGenOtnSlotProvTable,
       "adGenOtnSlotProvEntry": adGenOtnSlotProvEntry,
       "adGenOtnSlotOtuAlarmEnable": adGenOtnSlotOtuAlarmEnable,
       "adGenOtnSlotOduAlarmEnable": adGenOtnSlotOduAlarmEnable,
       "adGenOtnProtGroupTable": adGenOtnProtGroupTable,
       "adGenOtnProtGroupEntry": adGenOtnProtGroupEntry,
       "adGenOtnProtGroupName": adGenOtnProtGroupName,
       "adGenOtnProtGroupType": adGenOtnProtGroupType,
       "adGenOtnProtGroupWorkingType": adGenOtnProtGroupWorkingType,
       "adGenOtnProtGroupWorkingInterface": adGenOtnProtGroupWorkingInterface,
       "adGenOtnProtGroupProtectingType": adGenOtnProtGroupProtectingType,
       "adGenOtnProtGroupProtectingInterface": adGenOtnProtGroupProtectingInterface,
       "adGenOtnProtGroupRowStatus": adGenOtnProtGroupRowStatus,
       "adGenOtnProtGroupLastProvError": adGenOtnProtGroupLastProvError,
       "adGenOtnProtGroupWorkIsOnline": adGenOtnProtGroupWorkIsOnline,
       "adGenOtnProtGroupSwitchCommands": adGenOtnProtGroupSwitchCommands,
       "adGenOtnProtGroupWorkEntityStatus": adGenOtnProtGroupWorkEntityStatus,
       "adGenOtnProtGroupProtectEntityStatus": adGenOtnProtGroupProtectEntityStatus,
       "adGenOtnProtGroupRevertiveEnable": adGenOtnProtGroupRevertiveEnable,
       "adGenOtnProtGroupWaitToRestoreTime": adGenOtnProtGroupWaitToRestoreTime,
       "adGenOtnProtGroupOperStatus": adGenOtnProtGroupOperStatus,
       "adGenOtnProtGroupStatusString": adGenOtnProtGroupStatusString,
       "adGenOtnProtGroupWaitToRestoreRemainingTime": adGenOtnProtGroupWaitToRestoreRemainingTime,
       "adGenOtnProtGroupLastCreateErrorTable": adGenOtnProtGroupLastCreateErrorTable,
       "adGenOtnProtGroupLastCreateErrorEntry": adGenOtnProtGroupLastCreateErrorEntry,
       "adGenOtnProtGroupLastCreateError": adGenOtnProtGroupLastCreateError,
       "adGenOtnStatus": adGenOtnStatus,
       "adGenOtnOtuStatusTable": adGenOtnOtuStatusTable,
       "adGenOtnOtuStatusEntry": adGenOtnOtuStatusEntry,
       "adGenOtnOtuAlarmStatus": adGenOtnOtuAlarmStatus,
       "adGenOtnOduStatusTable": adGenOtnOduStatusTable,
       "adGenOtnOduStatusEntry": adGenOtnOduStatusEntry,
       "adGenOtnOduAlarmStatus": adGenOtnOduAlarmStatus,
       "adGenOtnOduStatus": adGenOtnOduStatus,
       "adGenOtnOduProtGrpName": adGenOtnOduProtGrpName,
       "adGenOtnOduCrossConnectStatusTable": adGenOtnOduCrossConnectStatusTable,
       "adGenOtnOduCrossConnectStatusEntry": adGenOtnOduCrossConnectStatusEntry,
       "adGenOtnOduCrossConnectName": adGenOtnOduCrossConnectName,
       "adGenOtnOduCrossConnectStatus": adGenOtnOduCrossConnectStatus,
       "adGenOtnOduMappingStatusTable": adGenOtnOduMappingStatusTable,
       "adGenOtnOduMappingStatusEntry": adGenOtnOduMappingStatusEntry,
       "adGenOtnOduMappingName": adGenOtnOduMappingName,
       "adGenOtnOduMappingStatus": adGenOtnOduMappingStatus,
       "adGenOtnPmThres": adGenOtnPmThres,
       "adGenOtnOtuPmThres15MinTable": adGenOtnOtuPmThres15MinTable,
       "adGenOtnOtuPmThres15MinEntry": adGenOtnOtuPmThres15MinEntry,
       "adGenOtnOtuPmThres15MinNeEB": adGenOtnOtuPmThres15MinNeEB,
       "adGenOtnOtuPmThres15MinNeBBE": adGenOtnOtuPmThres15MinNeBBE,
       "adGenOtnOtuPmThres15MinNeBBER": adGenOtnOtuPmThres15MinNeBBER,
       "adGenOtnOtuPmThres15MinNeES": adGenOtnOtuPmThres15MinNeES,
       "adGenOtnOtuPmThres15MinNeSES": adGenOtnOtuPmThres15MinNeSES,
       "adGenOtnOtuPmThres15MinNeESR": adGenOtnOtuPmThres15MinNeESR,
       "adGenOtnOtuPmThres15MinNeSESR": adGenOtnOtuPmThres15MinNeSESR,
       "adGenOtnOtuPmThres15MinNeUAS": adGenOtnOtuPmThres15MinNeUAS,
       "adGenOtnOtuPmThres15MinFeEB": adGenOtnOtuPmThres15MinFeEB,
       "adGenOtnOtuPmThres15MinFeBBE": adGenOtnOtuPmThres15MinFeBBE,
       "adGenOtnOtuPmThres15MinFeBBER": adGenOtnOtuPmThres15MinFeBBER,
       "adGenOtnOtuPmThres15MinFeES": adGenOtnOtuPmThres15MinFeES,
       "adGenOtnOtuPmThres15MinFeSES": adGenOtnOtuPmThres15MinFeSES,
       "adGenOtnOtuPmThres15MinFeESR": adGenOtnOtuPmThres15MinFeESR,
       "adGenOtnOtuPmThres15MinFeSESR": adGenOtnOtuPmThres15MinFeSESR,
       "adGenOtnOtuPmThres15MinFeUAS": adGenOtnOtuPmThres15MinFeUAS,
       "adGenOtnOtuPmThres15MinFecCorrBits": adGenOtnOtuPmThres15MinFecCorrBits,
       "adGenOtnOtuPmThres15MinFecCorrOnes": adGenOtnOtuPmThres15MinFecCorrOnes,
       "adGenOtnOtuPmThres15MinFecCorrZeros": adGenOtnOtuPmThres15MinFecCorrZeros,
       "adGenOtnOtuPmThres15MinFecUnCorrBlks": adGenOtnOtuPmThres15MinFecUnCorrBlks,
       "adGenOtnOtuPmThres15MinFecCorrBer": adGenOtnOtuPmThres15MinFecCorrBer,
       "adGenOtnOtuPmThres24HrTable": adGenOtnOtuPmThres24HrTable,
       "adGenOtnOtuPmThres24HrEntry": adGenOtnOtuPmThres24HrEntry,
       "adGenOtnOtuPmThres24HrNeEB": adGenOtnOtuPmThres24HrNeEB,
       "adGenOtnOtuPmThres24HrNeBBE": adGenOtnOtuPmThres24HrNeBBE,
       "adGenOtnOtuPmThres24HrNeBBER": adGenOtnOtuPmThres24HrNeBBER,
       "adGenOtnOtuPmThres24HrNeES": adGenOtnOtuPmThres24HrNeES,
       "adGenOtnOtuPmThres24HrNeSES": adGenOtnOtuPmThres24HrNeSES,
       "adGenOtnOtuPmThres24HrNeESR": adGenOtnOtuPmThres24HrNeESR,
       "adGenOtnOtuPmThres24HrNeSESR": adGenOtnOtuPmThres24HrNeSESR,
       "adGenOtnOtuPmThres24HrNeUAS": adGenOtnOtuPmThres24HrNeUAS,
       "adGenOtnOtuPmThres24HrFeEB": adGenOtnOtuPmThres24HrFeEB,
       "adGenOtnOtuPmThres24HrFeBBE": adGenOtnOtuPmThres24HrFeBBE,
       "adGenOtnOtuPmThres24HrFeBBER": adGenOtnOtuPmThres24HrFeBBER,
       "adGenOtnOtuPmThres24HrFeES": adGenOtnOtuPmThres24HrFeES,
       "adGenOtnOtuPmThres24HrFeSES": adGenOtnOtuPmThres24HrFeSES,
       "adGenOtnOtuPmThres24HrFeESR": adGenOtnOtuPmThres24HrFeESR,
       "adGenOtnOtuPmThres24HrFeSESR": adGenOtnOtuPmThres24HrFeSESR,
       "adGenOtnOtuPmThres24HrFeUAS": adGenOtnOtuPmThres24HrFeUAS,
       "adGenOtnOtuPmThres24HrFecCorrBits": adGenOtnOtuPmThres24HrFecCorrBits,
       "adGenOtnOtuPmThres24HrFecCorrOnes": adGenOtnOtuPmThres24HrFecCorrOnes,
       "adGenOtnOtuPmThres24HrFecCorrZeros": adGenOtnOtuPmThres24HrFecCorrZeros,
       "adGenOtnOtuPmThres24HrFecUnCorrBlks": adGenOtnOtuPmThres24HrFecUnCorrBlks,
       "adGenOtnOtuPmThres24HrFecCorrBer": adGenOtnOtuPmThres24HrFecCorrBer,
       "adGenOtnOduPmThres15MinTable": adGenOtnOduPmThres15MinTable,
       "adGenOtnOduPmThres15MinEntry": adGenOtnOduPmThres15MinEntry,
       "adGenOtnOduPmThres15MinNeEB": adGenOtnOduPmThres15MinNeEB,
       "adGenOtnOduPmThres15MinNeBBE": adGenOtnOduPmThres15MinNeBBE,
       "adGenOtnOduPmThres15MinNeBBER": adGenOtnOduPmThres15MinNeBBER,
       "adGenOtnOduPmThres15MinNeES": adGenOtnOduPmThres15MinNeES,
       "adGenOtnOduPmThres15MinNeSES": adGenOtnOduPmThres15MinNeSES,
       "adGenOtnOduPmThres15MinNeESR": adGenOtnOduPmThres15MinNeESR,
       "adGenOtnOduPmThres15MinNeSESR": adGenOtnOduPmThres15MinNeSESR,
       "adGenOtnOduPmThres15MinNeUAS": adGenOtnOduPmThres15MinNeUAS,
       "adGenOtnOduPmThres15MinFeEB": adGenOtnOduPmThres15MinFeEB,
       "adGenOtnOduPmThres15MinFeBBE": adGenOtnOduPmThres15MinFeBBE,
       "adGenOtnOduPmThres15MinFeBBER": adGenOtnOduPmThres15MinFeBBER,
       "adGenOtnOduPmThres15MinFeES": adGenOtnOduPmThres15MinFeES,
       "adGenOtnOduPmThres15MinFeSES": adGenOtnOduPmThres15MinFeSES,
       "adGenOtnOduPmThres15MinFeESR": adGenOtnOduPmThres15MinFeESR,
       "adGenOtnOduPmThres15MinFeSESR": adGenOtnOduPmThres15MinFeSESR,
       "adGenOtnOduPmThres15MinFeUAS": adGenOtnOduPmThres15MinFeUAS,
       "adGenOtnOduPmThres24HrTable": adGenOtnOduPmThres24HrTable,
       "adGenOtnOduPmThres24HrEntry": adGenOtnOduPmThres24HrEntry,
       "adGenOtnOduPmThres24HrNeEB": adGenOtnOduPmThres24HrNeEB,
       "adGenOtnOduPmThres24HrNeBBE": adGenOtnOduPmThres24HrNeBBE,
       "adGenOtnOduPmThres24HrNeBBER": adGenOtnOduPmThres24HrNeBBER,
       "adGenOtnOduPmThres24HrNeES": adGenOtnOduPmThres24HrNeES,
       "adGenOtnOduPmThres24HrNeSES": adGenOtnOduPmThres24HrNeSES,
       "adGenOtnOduPmThres24HrNeESR": adGenOtnOduPmThres24HrNeESR,
       "adGenOtnOduPmThres24HrNeSESR": adGenOtnOduPmThres24HrNeSESR,
       "adGenOtnOduPmThres24HrNeUAS": adGenOtnOduPmThres24HrNeUAS,
       "adGenOtnOduPmThres24HrFeEB": adGenOtnOduPmThres24HrFeEB,
       "adGenOtnOduPmThres24HrFeBBE": adGenOtnOduPmThres24HrFeBBE,
       "adGenOtnOduPmThres24HrFeBBER": adGenOtnOduPmThres24HrFeBBER,
       "adGenOtnOduPmThres24HrFeES": adGenOtnOduPmThres24HrFeES,
       "adGenOtnOduPmThres24HrFeSES": adGenOtnOduPmThres24HrFeSES,
       "adGenOtnOduPmThres24HrFeESR": adGenOtnOduPmThres24HrFeESR,
       "adGenOtnOduPmThres24HrFeSESR": adGenOtnOduPmThres24HrFeSESR,
       "adGenOtnOduPmThres24HrFeUAS": adGenOtnOduPmThres24HrFeUAS,
       "adGenOtnPm": adGenOtnPm,
       "adGenOtnOtuPm15MinCurrentTable": adGenOtnOtuPm15MinCurrentTable,
       "adGenOtnOtuPm15MinCurrentEntry": adGenOtnOtuPm15MinCurrentEntry,
       "adGenOtnOtuPm15MinCurrentNeEB": adGenOtnOtuPm15MinCurrentNeEB,
       "adGenOtnOtuPm15MinCurrentNeBBE": adGenOtnOtuPm15MinCurrentNeBBE,
       "adGenOtnOtuPm15MinCurrentNeBBER": adGenOtnOtuPm15MinCurrentNeBBER,
       "adGenOtnOtuPm15MinCurrentNeES": adGenOtnOtuPm15MinCurrentNeES,
       "adGenOtnOtuPm15MinCurrentNeSES": adGenOtnOtuPm15MinCurrentNeSES,
       "adGenOtnOtuPm15MinCurrentNeESR": adGenOtnOtuPm15MinCurrentNeESR,
       "adGenOtnOtuPm15MinCurrentNeSESR": adGenOtnOtuPm15MinCurrentNeSESR,
       "adGenOtnOtuPm15MinCurrentNeUAS": adGenOtnOtuPm15MinCurrentNeUAS,
       "adGenOtnOtuPm15MinCurrentFeEB": adGenOtnOtuPm15MinCurrentFeEB,
       "adGenOtnOtuPm15MinCurrentFeBBE": adGenOtnOtuPm15MinCurrentFeBBE,
       "adGenOtnOtuPm15MinCurrentFeBBER": adGenOtnOtuPm15MinCurrentFeBBER,
       "adGenOtnOtuPm15MinCurrentFeES": adGenOtnOtuPm15MinCurrentFeES,
       "adGenOtnOtuPm15MinCurrentFeSES": adGenOtnOtuPm15MinCurrentFeSES,
       "adGenOtnOtuPm15MinCurrentFeESR": adGenOtnOtuPm15MinCurrentFeESR,
       "adGenOtnOtuPm15MinCurrentFeSESR": adGenOtnOtuPm15MinCurrentFeSESR,
       "adGenOtnOtuPm15MinCurrentFeUAS": adGenOtnOtuPm15MinCurrentFeUAS,
       "adGenOtnOtuPm15MinCurrentFecCorrBits": adGenOtnOtuPm15MinCurrentFecCorrBits,
       "adGenOtnOtuPm15MinCurrentFecCorrOnes": adGenOtnOtuPm15MinCurrentFecCorrOnes,
       "adGenOtnOtuPm15MinCurrentFecCorrZeros": adGenOtnOtuPm15MinCurrentFecCorrZeros,
       "adGenOtnOtuPm15MinCurrentFecUnCorrBlks": adGenOtnOtuPm15MinCurrentFecUnCorrBlks,
       "adGenOtnOtuPm15MinCurrentFecCorrBer": adGenOtnOtuPm15MinCurrentFecCorrBer,
       "adGenOtnOtuPm15MinIntervalTable": adGenOtnOtuPm15MinIntervalTable,
       "adGenOtnOtuPm15MinIntervalEntry": adGenOtnOtuPm15MinIntervalEntry,
       "adGenOtnOtuPm15MinInterval": adGenOtnOtuPm15MinInterval,
       "adGenOtnOtuPm15MinIntervalNeEB": adGenOtnOtuPm15MinIntervalNeEB,
       "adGenOtnOtuPm15MinIntervalNeBBE": adGenOtnOtuPm15MinIntervalNeBBE,
       "adGenOtnOtuPm15MinIntervalNeBBER": adGenOtnOtuPm15MinIntervalNeBBER,
       "adGenOtnOtuPm15MinIntervalNeES": adGenOtnOtuPm15MinIntervalNeES,
       "adGenOtnOtuPm15MinIntervalNeSES": adGenOtnOtuPm15MinIntervalNeSES,
       "adGenOtnOtuPm15MinIntervalNeESR": adGenOtnOtuPm15MinIntervalNeESR,
       "adGenOtnOtuPm15MinIntervalNeSESR": adGenOtnOtuPm15MinIntervalNeSESR,
       "adGenOtnOtuPm15MinIntervalNeUAS": adGenOtnOtuPm15MinIntervalNeUAS,
       "adGenOtnOtuPm15MinIntervalFeEB": adGenOtnOtuPm15MinIntervalFeEB,
       "adGenOtnOtuPm15MinIntervalFeBBE": adGenOtnOtuPm15MinIntervalFeBBE,
       "adGenOtnOtuPm15MinIntervalFeBBER": adGenOtnOtuPm15MinIntervalFeBBER,
       "adGenOtnOtuPm15MinIntervalFeES": adGenOtnOtuPm15MinIntervalFeES,
       "adGenOtnOtuPm15MinIntervalFeSES": adGenOtnOtuPm15MinIntervalFeSES,
       "adGenOtnOtuPm15MinIntervalFeESR": adGenOtnOtuPm15MinIntervalFeESR,
       "adGenOtnOtuPm15MinIntervalFeSESR": adGenOtnOtuPm15MinIntervalFeSESR,
       "adGenOtnOtuPm15MinIntervalFeUAS": adGenOtnOtuPm15MinIntervalFeUAS,
       "adGenOtnOtuPm15MinIntervalFecCorrBits": adGenOtnOtuPm15MinIntervalFecCorrBits,
       "adGenOtnOtuPm15MinIntervalFecCorrOnes": adGenOtnOtuPm15MinIntervalFecCorrOnes,
       "adGenOtnOtuPm15MinIntervalFecCorrZeros": adGenOtnOtuPm15MinIntervalFecCorrZeros,
       "adGenOtnOtuPm15MinIntervalFecUnCorrBlks": adGenOtnOtuPm15MinIntervalFecUnCorrBlks,
       "adGenOtnOtuPm15MinIntervalFecCorrBer": adGenOtnOtuPm15MinIntervalFecCorrBer,
       "adGenOtnOtuPm15MinIntervalNeValidData": adGenOtnOtuPm15MinIntervalNeValidData,
       "adGenOtnOtuPm15MinIntervalFeValidData": adGenOtnOtuPm15MinIntervalFeValidData,
       "adGenOtnOtuPm24HrCurrentTable": adGenOtnOtuPm24HrCurrentTable,
       "adGenOtnOtuPm24HrCurrentEntry": adGenOtnOtuPm24HrCurrentEntry,
       "adGenOtnOtuPm24HrCurrentNeEB": adGenOtnOtuPm24HrCurrentNeEB,
       "adGenOtnOtuPm24HrCurrentNeBBE": adGenOtnOtuPm24HrCurrentNeBBE,
       "adGenOtnOtuPm24HrCurrentNeBBER": adGenOtnOtuPm24HrCurrentNeBBER,
       "adGenOtnOtuPm24HrCurrentNeES": adGenOtnOtuPm24HrCurrentNeES,
       "adGenOtnOtuPm24HrCurrentNeSES": adGenOtnOtuPm24HrCurrentNeSES,
       "adGenOtnOtuPm24HrCurrentNeESR": adGenOtnOtuPm24HrCurrentNeESR,
       "adGenOtnOtuPm24HrCurrentNeSESR": adGenOtnOtuPm24HrCurrentNeSESR,
       "adGenOtnOtuPm24HrCurrentNeUAS": adGenOtnOtuPm24HrCurrentNeUAS,
       "adGenOtnOtuPm24HrCurrentFeEB": adGenOtnOtuPm24HrCurrentFeEB,
       "adGenOtnOtuPm24HrCurrentFeBBE": adGenOtnOtuPm24HrCurrentFeBBE,
       "adGenOtnOtuPm24HrCurrentFeBBER": adGenOtnOtuPm24HrCurrentFeBBER,
       "adGenOtnOtuPm24HrCurrentFeES": adGenOtnOtuPm24HrCurrentFeES,
       "adGenOtnOtuPm24HrCurrentFeSES": adGenOtnOtuPm24HrCurrentFeSES,
       "adGenOtnOtuPm24HrCurrentFeESR": adGenOtnOtuPm24HrCurrentFeESR,
       "adGenOtnOtuPm24HrCurrentFeSESR": adGenOtnOtuPm24HrCurrentFeSESR,
       "adGenOtnOtuPm24HrCurrentFeUAS": adGenOtnOtuPm24HrCurrentFeUAS,
       "adGenOtnOtuPm24HrCurrentFecCorrBits": adGenOtnOtuPm24HrCurrentFecCorrBits,
       "adGenOtnOtuPm24HrCurrentFecCorrOnes": adGenOtnOtuPm24HrCurrentFecCorrOnes,
       "adGenOtnOtuPm24HrCurrentFecCorrZeros": adGenOtnOtuPm24HrCurrentFecCorrZeros,
       "adGenOtnOtuPm24HrCurrentFecUnCorrBlks": adGenOtnOtuPm24HrCurrentFecUnCorrBlks,
       "adGenOtnOtuPm24HrCurrentFecCorrBer": adGenOtnOtuPm24HrCurrentFecCorrBer,
       "adGenOtnOtuPm24HrIntervalTable": adGenOtnOtuPm24HrIntervalTable,
       "adGenOtnOtuPm24HrIntervalEntry": adGenOtnOtuPm24HrIntervalEntry,
       "adGenOtnOtuPm24HrInterval": adGenOtnOtuPm24HrInterval,
       "adGenOtnOtuPm24HrIntervalNeEB": adGenOtnOtuPm24HrIntervalNeEB,
       "adGenOtnOtuPm24HrIntervalNeBBE": adGenOtnOtuPm24HrIntervalNeBBE,
       "adGenOtnOtuPm24HrIntervalNeBBER": adGenOtnOtuPm24HrIntervalNeBBER,
       "adGenOtnOtuPm24HrIntervalNeES": adGenOtnOtuPm24HrIntervalNeES,
       "adGenOtnOtuPm24HrIntervalNeSES": adGenOtnOtuPm24HrIntervalNeSES,
       "adGenOtnOtuPm24HrIntervalNeESR": adGenOtnOtuPm24HrIntervalNeESR,
       "adGenOtnOtuPm24HrIntervalNeSESR": adGenOtnOtuPm24HrIntervalNeSESR,
       "adGenOtnOtuPm24HrIntervalNeUAS": adGenOtnOtuPm24HrIntervalNeUAS,
       "adGenOtnOtuPm24HrIntervalFeEB": adGenOtnOtuPm24HrIntervalFeEB,
       "adGenOtnOtuPm24HrIntervalFeBBE": adGenOtnOtuPm24HrIntervalFeBBE,
       "adGenOtnOtuPm24HrIntervalFeBBER": adGenOtnOtuPm24HrIntervalFeBBER,
       "adGenOtnOtuPm24HrIntervalFeES": adGenOtnOtuPm24HrIntervalFeES,
       "adGenOtnOtuPm24HrIntervalFeSES": adGenOtnOtuPm24HrIntervalFeSES,
       "adGenOtnOtuPm24HrIntervalFeESR": adGenOtnOtuPm24HrIntervalFeESR,
       "adGenOtnOtuPm24HrIntervalFeSESR": adGenOtnOtuPm24HrIntervalFeSESR,
       "adGenOtnOtuPm24HrIntervalFeUAS": adGenOtnOtuPm24HrIntervalFeUAS,
       "adGenOtnOtuPm24HrIntervalFecCorrBits": adGenOtnOtuPm24HrIntervalFecCorrBits,
       "adGenOtnOtuPm24HrIntervalFecCorrOnes": adGenOtnOtuPm24HrIntervalFecCorrOnes,
       "adGenOtnOtuPm24HrIntervalFecCorrZeros": adGenOtnOtuPm24HrIntervalFecCorrZeros,
       "adGenOtnOtuPm24HrIntervalFecUnCorrBlks": adGenOtnOtuPm24HrIntervalFecUnCorrBlks,
       "adGenOtnOtuPm24HrIntervalFecCorrBer": adGenOtnOtuPm24HrIntervalFecCorrBer,
       "adGenOtnOtuPm24HrIntervalNeValidData": adGenOtnOtuPm24HrIntervalNeValidData,
       "adGenOtnOtuPm24HrIntervalFeValidData": adGenOtnOtuPm24HrIntervalFeValidData,
       "adGenOtnOduPm15MinCurrentTable": adGenOtnOduPm15MinCurrentTable,
       "adGenOtnOduPm15MinCurrentEntry": adGenOtnOduPm15MinCurrentEntry,
       "adGenOtnOduPm15MinCurrentNeEB": adGenOtnOduPm15MinCurrentNeEB,
       "adGenOtnOduPm15MinCurrentNeBBE": adGenOtnOduPm15MinCurrentNeBBE,
       "adGenOtnOduPm15MinCurrentNeBBER": adGenOtnOduPm15MinCurrentNeBBER,
       "adGenOtnOduPm15MinCurrentNeES": adGenOtnOduPm15MinCurrentNeES,
       "adGenOtnOduPm15MinCurrentNeSES": adGenOtnOduPm15MinCurrentNeSES,
       "adGenOtnOduPm15MinCurrentNeESR": adGenOtnOduPm15MinCurrentNeESR,
       "adGenOtnOduPm15MinCurrentNeSESR": adGenOtnOduPm15MinCurrentNeSESR,
       "adGenOtnOduPm15MinCurrentNeUAS": adGenOtnOduPm15MinCurrentNeUAS,
       "adGenOtnOduPm15MinCurrentFeEB": adGenOtnOduPm15MinCurrentFeEB,
       "adGenOtnOduPm15MinCurrentFeBBE": adGenOtnOduPm15MinCurrentFeBBE,
       "adGenOtnOduPm15MinCurrentFeBBER": adGenOtnOduPm15MinCurrentFeBBER,
       "adGenOtnOduPm15MinCurrentFeES": adGenOtnOduPm15MinCurrentFeES,
       "adGenOtnOduPm15MinCurrentFeSES": adGenOtnOduPm15MinCurrentFeSES,
       "adGenOtnOduPm15MinCurrentFeESR": adGenOtnOduPm15MinCurrentFeESR,
       "adGenOtnOduPm15MinCurrentFeSESR": adGenOtnOduPm15MinCurrentFeSESR,
       "adGenOtnOduPm15MinCurrentFeUAS": adGenOtnOduPm15MinCurrentFeUAS,
       "adGenOtnOduPm15MinIntervalTable": adGenOtnOduPm15MinIntervalTable,
       "adGenOtnOduPm15MinIntervalEntry": adGenOtnOduPm15MinIntervalEntry,
       "adGenOtnOduPm15MinInterval": adGenOtnOduPm15MinInterval,
       "adGenOtnOduPm15MinIntervalNeEB": adGenOtnOduPm15MinIntervalNeEB,
       "adGenOtnOduPm15MinIntervalNeBBE": adGenOtnOduPm15MinIntervalNeBBE,
       "adGenOtnOduPm15MinIntervalNeBBER": adGenOtnOduPm15MinIntervalNeBBER,
       "adGenOtnOduPm15MinIntervalNeES": adGenOtnOduPm15MinIntervalNeES,
       "adGenOtnOduPm15MinIntervalNeSES": adGenOtnOduPm15MinIntervalNeSES,
       "adGenOtnOduPm15MinIntervalNeESR": adGenOtnOduPm15MinIntervalNeESR,
       "adGenOtnOduPm15MinIntervalNeSESR": adGenOtnOduPm15MinIntervalNeSESR,
       "adGenOtnOduPm15MinIntervalNeUAS": adGenOtnOduPm15MinIntervalNeUAS,
       "adGenOtnOduPm15MinIntervalFeEB": adGenOtnOduPm15MinIntervalFeEB,
       "adGenOtnOduPm15MinIntervalFeBBE": adGenOtnOduPm15MinIntervalFeBBE,
       "adGenOtnOduPm15MinIntervalFeBBER": adGenOtnOduPm15MinIntervalFeBBER,
       "adGenOtnOduPm15MinIntervalFeES": adGenOtnOduPm15MinIntervalFeES,
       "adGenOtnOduPm15MinIntervalFeSES": adGenOtnOduPm15MinIntervalFeSES,
       "adGenOtnOduPm15MinIntervalFeESR": adGenOtnOduPm15MinIntervalFeESR,
       "adGenOtnOduPm15MinIntervalFeSESR": adGenOtnOduPm15MinIntervalFeSESR,
       "adGenOtnOduPm15MinIntervalFeUAS": adGenOtnOduPm15MinIntervalFeUAS,
       "adGenOtnOduPm15MinIntervalNeValidData": adGenOtnOduPm15MinIntervalNeValidData,
       "adGenOtnOduPm15MinIntervalFeValidData": adGenOtnOduPm15MinIntervalFeValidData,
       "adGenOtnOduPm24HrCurrentTable": adGenOtnOduPm24HrCurrentTable,
       "adGenOtnOduPm24HrCurrentEntry": adGenOtnOduPm24HrCurrentEntry,
       "adGenOtnOduPm24HrCurrentNeEB": adGenOtnOduPm24HrCurrentNeEB,
       "adGenOtnOduPm24HrCurrentNeBBE": adGenOtnOduPm24HrCurrentNeBBE,
       "adGenOtnOduPm24HrCurrentNeBBER": adGenOtnOduPm24HrCurrentNeBBER,
       "adGenOtnOduPm24HrCurrentNeES": adGenOtnOduPm24HrCurrentNeES,
       "adGenOtnOduPm24HrCurrentNeSES": adGenOtnOduPm24HrCurrentNeSES,
       "adGenOtnOduPm24HrCurrentNeESR": adGenOtnOduPm24HrCurrentNeESR,
       "adGenOtnOduPm24HrCurrentNeSESR": adGenOtnOduPm24HrCurrentNeSESR,
       "adGenOtnOduPm24HrCurrentNeUAS": adGenOtnOduPm24HrCurrentNeUAS,
       "adGenOtnOduPm24HrCurrentFeEB": adGenOtnOduPm24HrCurrentFeEB,
       "adGenOtnOduPm24HrCurrentFeBBE": adGenOtnOduPm24HrCurrentFeBBE,
       "adGenOtnOduPm24HrCurrentFeBBER": adGenOtnOduPm24HrCurrentFeBBER,
       "adGenOtnOduPm24HrCurrentFeES": adGenOtnOduPm24HrCurrentFeES,
       "adGenOtnOduPm24HrCurrentFeSES": adGenOtnOduPm24HrCurrentFeSES,
       "adGenOtnOduPm24HrCurrentFeESR": adGenOtnOduPm24HrCurrentFeESR,
       "adGenOtnOduPm24HrCurrentFeSESR": adGenOtnOduPm24HrCurrentFeSESR,
       "adGenOtnOduPm24HrCurrentFeUAS": adGenOtnOduPm24HrCurrentFeUAS,
       "adGenOtnOduPm24HrIntervalTable": adGenOtnOduPm24HrIntervalTable,
       "adGenOtnOduPm24HrIntervalEntry": adGenOtnOduPm24HrIntervalEntry,
       "adGenOtnOduPm24HrInterval": adGenOtnOduPm24HrInterval,
       "adGenOtnOduPm24HrIntervalNeEB": adGenOtnOduPm24HrIntervalNeEB,
       "adGenOtnOduPm24HrIntervalNeBBE": adGenOtnOduPm24HrIntervalNeBBE,
       "adGenOtnOduPm24HrIntervalNeBBER": adGenOtnOduPm24HrIntervalNeBBER,
       "adGenOtnOduPm24HrIntervalNeES": adGenOtnOduPm24HrIntervalNeES,
       "adGenOtnOduPm24HrIntervalNeSES": adGenOtnOduPm24HrIntervalNeSES,
       "adGenOtnOduPm24HrIntervalNeESR": adGenOtnOduPm24HrIntervalNeESR,
       "adGenOtnOduPm24HrIntervalNeSESR": adGenOtnOduPm24HrIntervalNeSESR,
       "adGenOtnOduPm24HrIntervalNeUAS": adGenOtnOduPm24HrIntervalNeUAS,
       "adGenOtnOduPm24HrIntervalFeEB": adGenOtnOduPm24HrIntervalFeEB,
       "adGenOtnOduPm24HrIntervalFeBBE": adGenOtnOduPm24HrIntervalFeBBE,
       "adGenOtnOduPm24HrIntervalFeBBER": adGenOtnOduPm24HrIntervalFeBBER,
       "adGenOtnOduPm24HrIntervalFeES": adGenOtnOduPm24HrIntervalFeES,
       "adGenOtnOduPm24HrIntervalFeSES": adGenOtnOduPm24HrIntervalFeSES,
       "adGenOtnOduPm24HrIntervalFeESR": adGenOtnOduPm24HrIntervalFeESR,
       "adGenOtnOduPm24HrIntervalFeSESR": adGenOtnOduPm24HrIntervalFeSESR,
       "adGenOtnOduPm24HrIntervalFeUAS": adGenOtnOduPm24HrIntervalFeUAS,
       "adGenOtnOduPm24HrIntervalNeValidData": adGenOtnOduPm24HrIntervalNeValidData,
       "adGenOtnOduPm24HrIntervalFeValidData": adGenOtnOduPm24HrIntervalFeValidData,
       "adGenOtnOtuCountersTable": adGenOtnOtuCountersTable,
       "adGenOtnOtuCountersEntry": adGenOtnOtuCountersEntry,
       "adGenOtnOtuCounterNeEB": adGenOtnOtuCounterNeEB,
       "adGenOtnOtuCounterNeBBE": adGenOtnOtuCounterNeBBE,
       "adGenOtnOtuCounterNeES": adGenOtnOtuCounterNeES,
       "adGenOtnOtuCounterNeSES": adGenOtnOtuCounterNeSES,
       "adGenOtnOtuCounterNeUAS": adGenOtnOtuCounterNeUAS,
       "adGenOtnOtuCounterFeEB": adGenOtnOtuCounterFeEB,
       "adGenOtnOtuCounterFeBBE": adGenOtnOtuCounterFeBBE,
       "adGenOtnOtuCounterFeES": adGenOtnOtuCounterFeES,
       "adGenOtnOtuCounterFeSES": adGenOtnOtuCounterFeSES,
       "adGenOtnOtuCounterFeUAS": adGenOtnOtuCounterFeUAS,
       "adGenOtnOtuCounterFecCorrBits": adGenOtnOtuCounterFecCorrBits,
       "adGenOtnOtuCounterFecUnCorrBlks": adGenOtnOtuCounterFecUnCorrBlks,
       "adGenOtnOduCountersTable": adGenOtnOduCountersTable,
       "adGenOtnOduCountersEntry": adGenOtnOduCountersEntry,
       "adGenOtnOduCounterNeEB": adGenOtnOduCounterNeEB,
       "adGenOtnOduCounterNeBBE": adGenOtnOduCounterNeBBE,
       "adGenOtnOduCounterNeES": adGenOtnOduCounterNeES,
       "adGenOtnOduCounterNeSES": adGenOtnOduCounterNeSES,
       "adGenOtnOduCounterNeUAS": adGenOtnOduCounterNeUAS,
       "adGenOtnOduCounterFeEB": adGenOtnOduCounterFeEB,
       "adGenOtnOduCounterFeBBE": adGenOtnOduCounterFeBBE,
       "adGenOtnOduCounterFeES": adGenOtnOduCounterFeES,
       "adGenOtnOduCounterFeSES": adGenOtnOduCounterFeSES,
       "adGenOtnOduCounterFeUAS": adGenOtnOduCounterFeUAS,
       "adGenOtnPmInterface": adGenOtnPmInterface,
       "adGenOtnPmInterfaceTable": adGenOtnPmInterfaceTable,
       "adGenOtnPmInterfaceEntry": adGenOtnPmInterfaceEntry,
       "adGenOtnPmInterface15MinValidIntervals": adGenOtnPmInterface15MinValidIntervals,
       "adGenOtnPmInterface24HrValidIntervals": adGenOtnPmInterface24HrValidIntervals,
       "adGenOtnPmInterfaceResetPM": adGenOtnPmInterfaceResetPM,
       "adGenOtnPmSlot": adGenOtnPmSlot,
       "adGenOtnPmSlotTable": adGenOtnPmSlotTable,
       "adGenOtnPmSlotEntry": adGenOtnPmSlotEntry,
       "adGenOtnPmResetAllPMData": adGenOtnPmResetAllPMData,
       "adGenOtnOtuAlms": adGenOtnOtuAlms,
       "adGenOtnOtuAlarms": adGenOtnOtuAlarms,
       "adGenOtnOtuLosClrAlm": adGenOtnOtuLosClrAlm,
       "adGenOtnOtuLosActAlm": adGenOtnOtuLosActAlm,
       "adGenOtnOtuLofClrAlm": adGenOtnOtuLofClrAlm,
       "adGenOtnOtuLofActAlm": adGenOtnOtuLofActAlm,
       "adGenOtnOtuLomClrAlm": adGenOtnOtuLomClrAlm,
       "adGenOtnOtuLomActAlm": adGenOtnOtuLomActAlm,
       "adGenOtnOtuAisClrAlm": adGenOtnOtuAisClrAlm,
       "adGenOtnOtuAisActAlm": adGenOtnOtuAisActAlm,
       "adGenOtnOtuBdiClrAlm": adGenOtnOtuBdiClrAlm,
       "adGenOtnOtuBdiActAlm": adGenOtnOtuBdiActAlm,
       "adGenOtnOtuTimClrAlm": adGenOtnOtuTimClrAlm,
       "adGenOtnOtuTimActAlm": adGenOtnOtuTimActAlm,
       "adGenOtnOtuDegClrAlm": adGenOtnOtuDegClrAlm,
       "adGenOtnOtuDegActAlm": adGenOtnOtuDegActAlm,
       "adGenOtnOduAlms": adGenOtnOduAlms,
       "adGenOtnOduAlarms": adGenOtnOduAlarms,
       "adGenOtnOduLofLomClrAlm": adGenOtnOduLofLomClrAlm,
       "adGenOtnOduLofLomActAlm": adGenOtnOduLofLomActAlm,
       "adGenOtnOduBdiClrAlm": adGenOtnOduBdiClrAlm,
       "adGenOtnOduBdiActAlm": adGenOtnOduBdiActAlm,
       "adGenOtnOduOciClrAlm": adGenOtnOduOciClrAlm,
       "adGenOtnOduOciActAlm": adGenOtnOduOciActAlm,
       "adGenOtnOduTimClrAlm": adGenOtnOduTimClrAlm,
       "adGenOtnOduTimActAlm": adGenOtnOduTimActAlm,
       "adGenOtnOduDegClrAlm": adGenOtnOduDegClrAlm,
       "adGenOtnOduDegActAlm": adGenOtnOduDegActAlm,
       "adGenOtnOduPlmClrAlm": adGenOtnOduPlmClrAlm,
       "adGenOtnOduPlmActAlm": adGenOtnOduPlmActAlm,
       "adGenOtnOduLckClrAlm": adGenOtnOduLckClrAlm,
       "adGenOtnOduLckActAlm": adGenOtnOduLckActAlm,
       "adGenOtnOduAisClrAlm": adGenOtnOduAisClrAlm,
       "adGenOtnOduAisActAlm": adGenOtnOduAisActAlm,
       "adGenOtnOduMsimClrAlm": adGenOtnOduMsimClrAlm,
       "adGenOtnOduMsimActAlm": adGenOtnOduMsimActAlm,
       "adGenOtnOduCsfClrAlm": adGenOtnOduCsfClrAlm,
       "adGenOtnOduCsfActAlm": adGenOtnOduCsfActAlm,
       "adGenOtnOduLoomfiClrAlm": adGenOtnOduLoomfiClrAlm,
       "adGenOtnOduLoomfiActAlm": adGenOtnOduLoomfiActAlm,
       "adGenOtnOtuPmThres15MinAlms": adGenOtnOtuPmThres15MinAlms,
       "adGenOtnOtuPmThres15MinAlarms": adGenOtnOtuPmThres15MinAlarms,
       "adGenOtnOtuPmThres15MinNeEbAlm": adGenOtnOtuPmThres15MinNeEbAlm,
       "adGenOtnOtuPmThres15MinNeBbeAlm": adGenOtnOtuPmThres15MinNeBbeAlm,
       "adGenOtnOtuPmThres15MinNeBberAlm": adGenOtnOtuPmThres15MinNeBberAlm,
       "adGenOtnOtuPmThres15MinNeEsAlm": adGenOtnOtuPmThres15MinNeEsAlm,
       "adGenOtnOtuPmThres15MinNeSesAlm": adGenOtnOtuPmThres15MinNeSesAlm,
       "adGenOtnOtuPmThres15MinNeEsrAlm": adGenOtnOtuPmThres15MinNeEsrAlm,
       "adGenOtnOtuPmThres15MinNeSesrAlm": adGenOtnOtuPmThres15MinNeSesrAlm,
       "adGenOtnOtuPmThres15MinNeUasAlm": adGenOtnOtuPmThres15MinNeUasAlm,
       "adGenOtnOtuPmThres15MinFeEbAlm": adGenOtnOtuPmThres15MinFeEbAlm,
       "adGenOtnOtuPmThres15MinFeBbeAlm": adGenOtnOtuPmThres15MinFeBbeAlm,
       "adGenOtnOtuPmThres15MinFeBberAlm": adGenOtnOtuPmThres15MinFeBberAlm,
       "adGenOtnOtuPmThres15MinFeEsAlm": adGenOtnOtuPmThres15MinFeEsAlm,
       "adGenOtnOtuPmThres15MinFeSesAlm": adGenOtnOtuPmThres15MinFeSesAlm,
       "adGenOtnOtuPmThres15MinFeEsrAlm": adGenOtnOtuPmThres15MinFeEsrAlm,
       "adGenOtnOtuPmThres15MinFeSesrAlm": adGenOtnOtuPmThres15MinFeSesrAlm,
       "adGenOtnOtuPmThres15MinFeUasAlm": adGenOtnOtuPmThres15MinFeUasAlm,
       "adGenOtnOtuPmThres15MinFecCorrBitsAlm": adGenOtnOtuPmThres15MinFecCorrBitsAlm,
       "adGenOtnOtuPmThres15MinFecCorrOnesAlm": adGenOtnOtuPmThres15MinFecCorrOnesAlm,
       "adGenOtnOtuPmThres15MinFecCorrZerosAlm": adGenOtnOtuPmThres15MinFecCorrZerosAlm,
       "adGenOtnOtuPmThres15MinFecUncorrBlksAlm": adGenOtnOtuPmThres15MinFecUncorrBlksAlm,
       "adGenOtnOtuPmThres15MinFecCorrBerAlm": adGenOtnOtuPmThres15MinFecCorrBerAlm,
       "adGenOtnOtuPmThres24HrAlms": adGenOtnOtuPmThres24HrAlms,
       "adGenOtnOtuPmThres24HrAlarms": adGenOtnOtuPmThres24HrAlarms,
       "adGenOtnOtuPmThres24HrNeEbAlm": adGenOtnOtuPmThres24HrNeEbAlm,
       "adGenOtnOtuPmThres24HrNeBbeAlm": adGenOtnOtuPmThres24HrNeBbeAlm,
       "adGenOtnOtuPmThres24HrNeBberAlm": adGenOtnOtuPmThres24HrNeBberAlm,
       "adGenOtnOtuPmThres24HrNeEsAlm": adGenOtnOtuPmThres24HrNeEsAlm,
       "adGenOtnOtuPmThres24HrNeSesAlm": adGenOtnOtuPmThres24HrNeSesAlm,
       "adGenOtnOtuPmThres24HrNeEsrAlm": adGenOtnOtuPmThres24HrNeEsrAlm,
       "adGenOtnOtuPmThres24HrNeSesrAlm": adGenOtnOtuPmThres24HrNeSesrAlm,
       "adGenOtnOtuPmThres24HrNeUasAlm": adGenOtnOtuPmThres24HrNeUasAlm,
       "adGenOtnOtuPmThres24HrFeEbAlm": adGenOtnOtuPmThres24HrFeEbAlm,
       "adGenOtnOtuPmThres24HrFeBbeAlm": adGenOtnOtuPmThres24HrFeBbeAlm,
       "adGenOtnOtuPmThres24HrFeBberAlm": adGenOtnOtuPmThres24HrFeBberAlm,
       "adGenOtnOtuPmThres24HrFeEsAlm": adGenOtnOtuPmThres24HrFeEsAlm,
       "adGenOtnOtuPmThres24HrFeSesAlm": adGenOtnOtuPmThres24HrFeSesAlm,
       "adGenOtnOtuPmThres24HrFeEsrAlm": adGenOtnOtuPmThres24HrFeEsrAlm,
       "adGenOtnOtuPmThres24HrFeSesrAlm": adGenOtnOtuPmThres24HrFeSesrAlm,
       "adGenOtnOtuPmThres24HrFeUasAlm": adGenOtnOtuPmThres24HrFeUasAlm,
       "adGenOtnOtuPmThres24HrFecCorrBitsAlm": adGenOtnOtuPmThres24HrFecCorrBitsAlm,
       "adGenOtnOtuPmThres24HrFecCorrOnesAlm": adGenOtnOtuPmThres24HrFecCorrOnesAlm,
       "adGenOtnOtuPmThres24HrFecCorrZerosAlm": adGenOtnOtuPmThres24HrFecCorrZerosAlm,
       "adGenOtnOtuPmThres24HrFecUncorrBlksAlm": adGenOtnOtuPmThres24HrFecUncorrBlksAlm,
       "adGenOtnOtuPmThres24HrFecCorrBerAlm": adGenOtnOtuPmThres24HrFecCorrBerAlm,
       "adGenOtnOduPmThres15MinAlms": adGenOtnOduPmThres15MinAlms,
       "adGenOtnOduPmThres15MinAlarms": adGenOtnOduPmThres15MinAlarms,
       "adGenOtnOduPmThres15MinNeEbAlm": adGenOtnOduPmThres15MinNeEbAlm,
       "adGenOtnOduPmThres15MinNeBbeAlm": adGenOtnOduPmThres15MinNeBbeAlm,
       "adGenOtnOduPmThres15MinNeBberAlm": adGenOtnOduPmThres15MinNeBberAlm,
       "adGenOtnOduPmThres15MinNeEsAlm": adGenOtnOduPmThres15MinNeEsAlm,
       "adGenOtnOduPmThres15MinNeSesAlm": adGenOtnOduPmThres15MinNeSesAlm,
       "adGenOtnOduPmThres15MinNeEsrAlm": adGenOtnOduPmThres15MinNeEsrAlm,
       "adGenOtnOduPmThres15MinNeSesrAlm": adGenOtnOduPmThres15MinNeSesrAlm,
       "adGenOtnOduPmThres15MinNeUasAlm": adGenOtnOduPmThres15MinNeUasAlm,
       "adGenOtnOduPmThres15MinFeEbAlm": adGenOtnOduPmThres15MinFeEbAlm,
       "adGenOtnOduPmThres15MinFeBbeAlm": adGenOtnOduPmThres15MinFeBbeAlm,
       "adGenOtnOduPmThres15MinFeBberAlm": adGenOtnOduPmThres15MinFeBberAlm,
       "adGenOtnOduPmThres15MinFeEsAlm": adGenOtnOduPmThres15MinFeEsAlm,
       "adGenOtnOduPmThres15MinFeSesAlm": adGenOtnOduPmThres15MinFeSesAlm,
       "adGenOtnOduPmThres15MinFeEsrAlm": adGenOtnOduPmThres15MinFeEsrAlm,
       "adGenOtnOduPmThres15MinFeSesrAlm": adGenOtnOduPmThres15MinFeSesrAlm,
       "adGenOtnOduPmThres15MinFeUasAlm": adGenOtnOduPmThres15MinFeUasAlm,
       "adGenOtnOduPmThres24HrAlms": adGenOtnOduPmThres24HrAlms,
       "adGenOtnOduPmThres24HrAlarms": adGenOtnOduPmThres24HrAlarms,
       "adGenOtnOduPmThres24HrNeEbAlm": adGenOtnOduPmThres24HrNeEbAlm,
       "adGenOtnOduPmThres24HrNeBbeAlm": adGenOtnOduPmThres24HrNeBbeAlm,
       "adGenOtnOduPmThres24HrNeBberAlm": adGenOtnOduPmThres24HrNeBberAlm,
       "adGenOtnOduPmThres24HrNeEsAlm": adGenOtnOduPmThres24HrNeEsAlm,
       "adGenOtnOduPmThres24HrNeSesAlm": adGenOtnOduPmThres24HrNeSesAlm,
       "adGenOtnOduPmThres24HrNeEsrAlm": adGenOtnOduPmThres24HrNeEsrAlm,
       "adGenOtnOduPmThres24HrNeSesrAlm": adGenOtnOduPmThres24HrNeSesrAlm,
       "adGenOtnOduPmThres24HrNeUasAlm": adGenOtnOduPmThres24HrNeUasAlm,
       "adGenOtnOduPmThres24HrFeEbAlm": adGenOtnOduPmThres24HrFeEbAlm,
       "adGenOtnOduPmThres24HrFeBbeAlm": adGenOtnOduPmThres24HrFeBbeAlm,
       "adGenOtnOduPmThres24HrFeBberAlm": adGenOtnOduPmThres24HrFeBberAlm,
       "adGenOtnOduPmThres24HrFeEsAlm": adGenOtnOduPmThres24HrFeEsAlm,
       "adGenOtnOduPmThres24HrFeSesAlm": adGenOtnOduPmThres24HrFeSesAlm,
       "adGenOtnOduPmThres24HrFeEsrAlm": adGenOtnOduPmThres24HrFeEsrAlm,
       "adGenOtnOduPmThres24HrFeSesrAlm": adGenOtnOduPmThres24HrFeSesrAlm,
       "adGenOtnOduPmThres24HrFeUasAlm": adGenOtnOduPmThres24HrFeUasAlm,
       "adGenOtnIdentity": adGenOtnIdentity}
)
