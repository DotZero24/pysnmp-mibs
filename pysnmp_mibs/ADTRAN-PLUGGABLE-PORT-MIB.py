# SNMP MIB module (ADTRAN-PLUGGABLE-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-PLUGGABLE-PORT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:31:06 2025
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

(adGenPortTrapIdentifier,) = mibBuilder.importSymbols(
    "ADTRAN-GENPORT-MIB",
    "adGenPortTrapIdentifier")

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adIdentity,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity")

(adGenPluggablePort,
 adGenPluggablePortID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenPluggablePort",
    "adGenPluggablePortID")

(adTAeSCUTrapAlarmLevel,) = mibBuilder.importSymbols(
    "ADTRAN-TAeSCUEXT1-MIB",
    "adTAeSCUTrapAlarmLevel")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adGenPluggablePortMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 4, 1)
)
if mibBuilder.loadTexts:
    adGenPluggablePortMIB.setRevisions(
        ("2020-03-19 00:00",
         "2019-08-14 00:00",
         "2019-05-31 00:00",
         "2016-04-15 00:00",
         "2013-06-13 00:00",
         "2012-01-23 00:00",
         "2011-03-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PluggablePortPowerUnits(TextualConvention, Integer32):
    status = "current"
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
        *(("dBm", 1),
          ("tenthsDBm", 2),
          ("microWatts", 3),
          ("tenthsMicroWatts", 4))
    )



# MIB Managed Objects in the order of their OIDs

_AdGenPluggablePortObjects_ObjectIdentity = ObjectIdentity
adGenPluggablePortObjects = _AdGenPluggablePortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1)
)
_AdGenPluggablePortTable_Object = MibTable
adGenPluggablePortTable = _AdGenPluggablePortTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1)
)
if mibBuilder.loadTexts:
    adGenPluggablePortTable.setStatus("current")
_AdGenPluggablePortEntry_Object = MibTableRow
adGenPluggablePortEntry = _AdGenPluggablePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1)
)
adGenPluggablePortEntry.setIndexNames(
    (0, "ADTRAN-PLUGGABLE-PORT-MIB", "adGenPluggablePortIndex"),
)
if mibBuilder.loadTexts:
    adGenPluggablePortEntry.setStatus("current")
_AdGenPluggablePortIndex_Type = InterfaceIndex
_AdGenPluggablePortIndex_Object = MibTableColumn
adGenPluggablePortIndex = _AdGenPluggablePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 1),
    _AdGenPluggablePortIndex_Type()
)
adGenPluggablePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenPluggablePortIndex.setStatus("current")


class _AdGenPluggablePortPluggableType_Type(Integer32):
    """Custom type adGenPluggablePortPluggableType based on Integer32"""
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
        *(("none", 1),
          ("sfp", 2),
          ("xfp", 3),
          ("unknown", 4),
          ("qsfp", 5))
    )


_AdGenPluggablePortPluggableType_Type.__name__ = "Integer32"
_AdGenPluggablePortPluggableType_Object = MibTableColumn
adGenPluggablePortPluggableType = _AdGenPluggablePortPluggableType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 2),
    _AdGenPluggablePortPluggableType_Type()
)
adGenPluggablePortPluggableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortPluggableType.setStatus("current")


class _AdGenPluggablePortConnectorType_Type(Integer32):
    """Custom type adGenPluggablePortConnectorType based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("fiberLC", 2),
          ("fiberSC", 3),
          ("mtrj", 4),
          ("hssdc", 5),
          ("copperRJ45", 6),
          ("none", 7),
          ("copperPigtail", 8),
          ("opticalPigtail", 9),
          ("mpo", 10),
          ("noSeparable", 11))
    )


_AdGenPluggablePortConnectorType_Type.__name__ = "Integer32"
_AdGenPluggablePortConnectorType_Object = MibTableColumn
adGenPluggablePortConnectorType = _AdGenPluggablePortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 3),
    _AdGenPluggablePortConnectorType_Type()
)
adGenPluggablePortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortConnectorType.setStatus("current")


class _AdGenPluggablePortCapabilities_Type(Bits):
    """Custom type adGenPluggablePortCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("pluggable", 0),
          ("berReadable", 1),
          ("voltageReadable", 2),
          ("wavelengthReadable", 3),
          ("diagnosticsAvailable", 4),
          ("wavelengthProvisionable", 5))
    )

_AdGenPluggablePortCapabilities_Type.__name__ = "Bits"
_AdGenPluggablePortCapabilities_Object = MibTableColumn
adGenPluggablePortCapabilities = _AdGenPluggablePortCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 4),
    _AdGenPluggablePortCapabilities_Type()
)
adGenPluggablePortCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortCapabilities.setStatus("current")


class _AdGenPluggablePortState_Type(Bits):
    """Custom type adGenPluggablePortState based on Bits"""
    namedValues = NamedValues(
        *(("portUnsupported", 0),
          ("portUp", 1),
          ("portDown", 2),
          ("portLos", 3),
          ("portLol", 4),
          ("portSignalDegrade", 5),
          ("portSignalFail", 6),
          ("portMissing", 7),
          ("cardMissing", 8))
    )

_AdGenPluggablePortState_Type.__name__ = "Bits"
_AdGenPluggablePortState_Object = MibTableColumn
adGenPluggablePortState = _AdGenPluggablePortState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 5),
    _AdGenPluggablePortState_Type()
)
adGenPluggablePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortState.setStatus("current")


class _AdGenPluggablePortStatusBits_Type(Bits):
    """Custom type adGenPluggablePortStatusBits based on Bits"""
    namedValues = NamedValues(
        *(("isPresent", 0),
          ("isValid", 1),
          ("isSupported", 2),
          ("isMismatched", 3),
          ("isTxEnabled", 4),
          ("isTxFault", 5),
          ("isWavelengthMismatch", 6))
    )

_AdGenPluggablePortStatusBits_Type.__name__ = "Bits"
_AdGenPluggablePortStatusBits_Object = MibTableColumn
adGenPluggablePortStatusBits = _AdGenPluggablePortStatusBits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 6),
    _AdGenPluggablePortStatusBits_Type()
)
adGenPluggablePortStatusBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortStatusBits.setStatus("current")


class _AdGenPluggablePortAlarmBits_Type(Bits):
    """Custom type adGenPluggablePortAlarmBits based on Bits"""
    namedValues = NamedValues(
        *(("txFault", 0),
          ("missing", 1),
          ("unsupported", 2),
          ("speedMismatch", 3),
          ("highTemp", 4),
          ("wavelengthMismatch", 5))
    )

_AdGenPluggablePortAlarmBits_Type.__name__ = "Bits"
_AdGenPluggablePortAlarmBits_Object = MibTableColumn
adGenPluggablePortAlarmBits = _AdGenPluggablePortAlarmBits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 7),
    _AdGenPluggablePortAlarmBits_Type()
)
adGenPluggablePortAlarmBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortAlarmBits.setStatus("current")


class _AdGenPluggablePortAlarmsSuppressed_Type(Bits):
    """Custom type adGenPluggablePortAlarmsSuppressed based on Bits"""
    namedValues = NamedValues(
        *(("txFault", 0),
          ("missing", 1),
          ("unsupported", 2),
          ("speedMismatch", 3),
          ("highTemp", 4),
          ("wavelengthMismacth", 5))
    )

_AdGenPluggablePortAlarmsSuppressed_Type.__name__ = "Bits"
_AdGenPluggablePortAlarmsSuppressed_Object = MibTableColumn
adGenPluggablePortAlarmsSuppressed = _AdGenPluggablePortAlarmsSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 8),
    _AdGenPluggablePortAlarmsSuppressed_Type()
)
adGenPluggablePortAlarmsSuppressed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPluggablePortAlarmsSuppressed.setStatus("current")
_AdGenPluggablePortBer_Type = Unsigned32
_AdGenPluggablePortBer_Object = MibTableColumn
adGenPluggablePortBer = _AdGenPluggablePortBer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 9),
    _AdGenPluggablePortBer_Type()
)
adGenPluggablePortBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortBer.setStatus("current")


class _AdGenPluggablePortVendorName_Type(OctetString):
    """Custom type adGenPluggablePortVendorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdGenPluggablePortVendorName_Type.__name__ = "OctetString"
_AdGenPluggablePortVendorName_Object = MibTableColumn
adGenPluggablePortVendorName = _AdGenPluggablePortVendorName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 10),
    _AdGenPluggablePortVendorName_Type()
)
adGenPluggablePortVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortVendorName.setStatus("current")


class _AdGenPluggablePortVendorPartNumber_Type(OctetString):
    """Custom type adGenPluggablePortVendorPartNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdGenPluggablePortVendorPartNumber_Type.__name__ = "OctetString"
_AdGenPluggablePortVendorPartNumber_Object = MibTableColumn
adGenPluggablePortVendorPartNumber = _AdGenPluggablePortVendorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 11),
    _AdGenPluggablePortVendorPartNumber_Type()
)
adGenPluggablePortVendorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortVendorPartNumber.setStatus("current")


class _AdGenPluggablePortVendorSerialNumber_Type(OctetString):
    """Custom type adGenPluggablePortVendorSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdGenPluggablePortVendorSerialNumber_Type.__name__ = "OctetString"
_AdGenPluggablePortVendorSerialNumber_Object = MibTableColumn
adGenPluggablePortVendorSerialNumber = _AdGenPluggablePortVendorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 12),
    _AdGenPluggablePortVendorSerialNumber_Type()
)
adGenPluggablePortVendorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortVendorSerialNumber.setStatus("current")


class _AdGenPluggablePortAdtranName_Type(OctetString):
    """Custom type adGenPluggablePortAdtranName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdGenPluggablePortAdtranName_Type.__name__ = "OctetString"
_AdGenPluggablePortAdtranName_Object = MibTableColumn
adGenPluggablePortAdtranName = _AdGenPluggablePortAdtranName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 13),
    _AdGenPluggablePortAdtranName_Type()
)
adGenPluggablePortAdtranName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortAdtranName.setStatus("current")


class _AdGenPluggablePortAdtranPartNumber_Type(OctetString):
    """Custom type adGenPluggablePortAdtranPartNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdGenPluggablePortAdtranPartNumber_Type.__name__ = "OctetString"
_AdGenPluggablePortAdtranPartNumber_Object = MibTableColumn
adGenPluggablePortAdtranPartNumber = _AdGenPluggablePortAdtranPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 14),
    _AdGenPluggablePortAdtranPartNumber_Type()
)
adGenPluggablePortAdtranPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortAdtranPartNumber.setStatus("current")


class _AdGenPluggablePortAdtranClei_Type(OctetString):
    """Custom type adGenPluggablePortAdtranClei based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdGenPluggablePortAdtranClei_Type.__name__ = "OctetString"
_AdGenPluggablePortAdtranClei_Object = MibTableColumn
adGenPluggablePortAdtranClei = _AdGenPluggablePortAdtranClei_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 15),
    _AdGenPluggablePortAdtranClei_Type()
)
adGenPluggablePortAdtranClei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortAdtranClei.setStatus("current")
_AdGenPluggablePortWavelength_Type = Unsigned32
_AdGenPluggablePortWavelength_Object = MibTableColumn
adGenPluggablePortWavelength = _AdGenPluggablePortWavelength_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 16),
    _AdGenPluggablePortWavelength_Type()
)
adGenPluggablePortWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortWavelength.setStatus("current")
_AdGenPluggablePortMinBitRate_Type = Unsigned32
_AdGenPluggablePortMinBitRate_Object = MibTableColumn
adGenPluggablePortMinBitRate = _AdGenPluggablePortMinBitRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 17),
    _AdGenPluggablePortMinBitRate_Type()
)
adGenPluggablePortMinBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortMinBitRate.setStatus("current")
_AdGenPluggablePortMaxBitRate_Type = Unsigned32
_AdGenPluggablePortMaxBitRate_Object = MibTableColumn
adGenPluggablePortMaxBitRate = _AdGenPluggablePortMaxBitRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 18),
    _AdGenPluggablePortMaxBitRate_Type()
)
adGenPluggablePortMaxBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortMaxBitRate.setStatus("current")
_AdGenPluggablePortReachLength_Type = Unsigned32
_AdGenPluggablePortReachLength_Object = MibTableColumn
adGenPluggablePortReachLength = _AdGenPluggablePortReachLength_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 19),
    _AdGenPluggablePortReachLength_Type()
)
adGenPluggablePortReachLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortReachLength.setStatus("current")


class _AdGenPluggablePortReachUnits_Type(Integer32):
    """Custom type adGenPluggablePortReachUnits based on Integer32"""
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
        *(("reachUnit1Kmfor09um", 1),
          ("reachUnit100mfor09um", 2),
          ("reachUnit10mfor50um", 3),
          ("reachUnit10mfor62um", 4),
          ("reachUnit1mforCu", 5),
          ("reachUnit1KmforSmf", 6),
          ("reachUnit2mforEBW", 7),
          ("reachUnit1mfor50um", 8),
          ("reachUnit1mfor62um", 9))
    )


_AdGenPluggablePortReachUnits_Type.__name__ = "Integer32"
_AdGenPluggablePortReachUnits_Object = MibTableColumn
adGenPluggablePortReachUnits = _AdGenPluggablePortReachUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 20),
    _AdGenPluggablePortReachUnits_Type()
)
adGenPluggablePortReachUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortReachUnits.setStatus("current")
_AdGenPluggablePortRxPower_Type = Integer32
_AdGenPluggablePortRxPower_Object = MibTableColumn
adGenPluggablePortRxPower = _AdGenPluggablePortRxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 21),
    _AdGenPluggablePortRxPower_Type()
)
adGenPluggablePortRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortRxPower.setStatus("deprecated")
_AdGenPluggablePortRxPowerUnits_Type = PluggablePortPowerUnits
_AdGenPluggablePortRxPowerUnits_Object = MibTableColumn
adGenPluggablePortRxPowerUnits = _AdGenPluggablePortRxPowerUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 22),
    _AdGenPluggablePortRxPowerUnits_Type()
)
adGenPluggablePortRxPowerUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortRxPowerUnits.setStatus("deprecated")
_AdGenPluggablePortTxPower_Type = Integer32
_AdGenPluggablePortTxPower_Object = MibTableColumn
adGenPluggablePortTxPower = _AdGenPluggablePortTxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 23),
    _AdGenPluggablePortTxPower_Type()
)
adGenPluggablePortTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortTxPower.setStatus("deprecated")
_AdGenPluggablePortTxPowerUnits_Type = PluggablePortPowerUnits
_AdGenPluggablePortTxPowerUnits_Object = MibTableColumn
adGenPluggablePortTxPowerUnits = _AdGenPluggablePortTxPowerUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 24),
    _AdGenPluggablePortTxPowerUnits_Type()
)
adGenPluggablePortTxPowerUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortTxPowerUnits.setStatus("deprecated")
_AdGenPluggablePortTxBias_Type = Integer32
_AdGenPluggablePortTxBias_Object = MibTableColumn
adGenPluggablePortTxBias = _AdGenPluggablePortTxBias_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 25),
    _AdGenPluggablePortTxBias_Type()
)
adGenPluggablePortTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortTxBias.setStatus("deprecated")


class _AdGenPluggablePortTxBiasUnits_Type(Integer32):
    """Custom type adGenPluggablePortTxBiasUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("milliAmps", 1)
    )


_AdGenPluggablePortTxBiasUnits_Type.__name__ = "Integer32"
_AdGenPluggablePortTxBiasUnits_Object = MibTableColumn
adGenPluggablePortTxBiasUnits = _AdGenPluggablePortTxBiasUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 26),
    _AdGenPluggablePortTxBiasUnits_Type()
)
adGenPluggablePortTxBiasUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortTxBiasUnits.setStatus("deprecated")
_AdGenPluggablePortTemperature_Type = Integer32
_AdGenPluggablePortTemperature_Object = MibTableColumn
adGenPluggablePortTemperature = _AdGenPluggablePortTemperature_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 27),
    _AdGenPluggablePortTemperature_Type()
)
adGenPluggablePortTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortTemperature.setStatus("current")


class _AdGenPluggablePortTemperatureUnits_Type(Integer32):
    """Custom type adGenPluggablePortTemperatureUnits based on Integer32"""
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
        *(("celsius", 1),
          ("tenthsCelsius", 2),
          ("fahrenheit", 3),
          ("tenthsFahrenheit", 4))
    )


_AdGenPluggablePortTemperatureUnits_Type.__name__ = "Integer32"
_AdGenPluggablePortTemperatureUnits_Object = MibTableColumn
adGenPluggablePortTemperatureUnits = _AdGenPluggablePortTemperatureUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 28),
    _AdGenPluggablePortTemperatureUnits_Type()
)
adGenPluggablePortTemperatureUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortTemperatureUnits.setStatus("current")
_AdGenPluggablePortVoltage_Type = Integer32
_AdGenPluggablePortVoltage_Object = MibTableColumn
adGenPluggablePortVoltage = _AdGenPluggablePortVoltage_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 29),
    _AdGenPluggablePortVoltage_Type()
)
adGenPluggablePortVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortVoltage.setStatus("current")


class _AdGenPluggablePortVendorRevision_Type(OctetString):
    """Custom type adGenPluggablePortVendorRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_AdGenPluggablePortVendorRevision_Type.__name__ = "OctetString"
_AdGenPluggablePortVendorRevision_Object = MibTableColumn
adGenPluggablePortVendorRevision = _AdGenPluggablePortVendorRevision_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 30),
    _AdGenPluggablePortVendorRevision_Type()
)
adGenPluggablePortVendorRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortVendorRevision.setStatus("current")
_AdGenPluggablePortWavelengthPicoMeter_Type = Unsigned32
_AdGenPluggablePortWavelengthPicoMeter_Object = MibTableColumn
adGenPluggablePortWavelengthPicoMeter = _AdGenPluggablePortWavelengthPicoMeter_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 31),
    _AdGenPluggablePortWavelengthPicoMeter_Type()
)
adGenPluggablePortWavelengthPicoMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortWavelengthPicoMeter.setStatus("current")
_AdGenPluggableNumberOfXcvrChannels_Type = Integer32
_AdGenPluggableNumberOfXcvrChannels_Object = MibTableColumn
adGenPluggableNumberOfXcvrChannels = _AdGenPluggableNumberOfXcvrChannels_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 1, 1, 32),
    _AdGenPluggableNumberOfXcvrChannels_Type()
)
adGenPluggableNumberOfXcvrChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggableNumberOfXcvrChannels.setStatus("current")
_AdGenPluggablePortChannelTable_Object = MibTable
adGenPluggablePortChannelTable = _AdGenPluggablePortChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 2)
)
if mibBuilder.loadTexts:
    adGenPluggablePortChannelTable.setStatus("current")
_AdGenPluggablePortChannelEntry_Object = MibTableRow
adGenPluggablePortChannelEntry = _AdGenPluggablePortChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 2, 1)
)
adGenPluggablePortChannelEntry.setIndexNames(
    (0, "ADTRAN-PLUGGABLE-PORT-MIB", "adGenPluggablePortIndex"),
    (0, "ADTRAN-PLUGGABLE-PORT-MIB", "adGenPluggablePortChannelXcvrIndex"),
)
if mibBuilder.loadTexts:
    adGenPluggablePortChannelEntry.setStatus("current")
_AdGenPluggablePortChannelModuleIndex_Type = InterfaceIndex
_AdGenPluggablePortChannelModuleIndex_Object = MibTableColumn
adGenPluggablePortChannelModuleIndex = _AdGenPluggablePortChannelModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 2, 1, 1),
    _AdGenPluggablePortChannelModuleIndex_Type()
)
adGenPluggablePortChannelModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenPluggablePortChannelModuleIndex.setStatus("current")
_AdGenPluggablePortChannelXcvrIndex_Type = Unsigned32
_AdGenPluggablePortChannelXcvrIndex_Object = MibTableColumn
adGenPluggablePortChannelXcvrIndex = _AdGenPluggablePortChannelXcvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 2, 1, 2),
    _AdGenPluggablePortChannelXcvrIndex_Type()
)
adGenPluggablePortChannelXcvrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenPluggablePortChannelXcvrIndex.setStatus("current")
_AdGenPluggablePortChannelRxPower_Type = Integer32
_AdGenPluggablePortChannelRxPower_Object = MibTableColumn
adGenPluggablePortChannelRxPower = _AdGenPluggablePortChannelRxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 2, 1, 3),
    _AdGenPluggablePortChannelRxPower_Type()
)
adGenPluggablePortChannelRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortChannelRxPower.setStatus("current")
_AdGenPluggablePortChannelRxPowerUnits_Type = PluggablePortPowerUnits
_AdGenPluggablePortChannelRxPowerUnits_Object = MibTableColumn
adGenPluggablePortChannelRxPowerUnits = _AdGenPluggablePortChannelRxPowerUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 2, 1, 4),
    _AdGenPluggablePortChannelRxPowerUnits_Type()
)
adGenPluggablePortChannelRxPowerUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortChannelRxPowerUnits.setStatus("current")
_AdGenPluggablePortChannelTxPower_Type = Integer32
_AdGenPluggablePortChannelTxPower_Object = MibTableColumn
adGenPluggablePortChannelTxPower = _AdGenPluggablePortChannelTxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 2, 1, 5),
    _AdGenPluggablePortChannelTxPower_Type()
)
adGenPluggablePortChannelTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortChannelTxPower.setStatus("current")
_AdGenPluggablePortChannelTxPowerUnits_Type = PluggablePortPowerUnits
_AdGenPluggablePortChannelTxPowerUnits_Object = MibTableColumn
adGenPluggablePortChannelTxPowerUnits = _AdGenPluggablePortChannelTxPowerUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 2, 1, 6),
    _AdGenPluggablePortChannelTxPowerUnits_Type()
)
adGenPluggablePortChannelTxPowerUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortChannelTxPowerUnits.setStatus("current")
_AdGenPluggablePortChannelTxBias_Type = Integer32
_AdGenPluggablePortChannelTxBias_Object = MibTableColumn
adGenPluggablePortChannelTxBias = _AdGenPluggablePortChannelTxBias_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 2, 1, 7),
    _AdGenPluggablePortChannelTxBias_Type()
)
adGenPluggablePortChannelTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortChannelTxBias.setStatus("current")


class _AdGenPluggablePortChannelTxBiasUnits_Type(Integer32):
    """Custom type adGenPluggablePortChannelTxBiasUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("milliAmps", 1)
    )


_AdGenPluggablePortChannelTxBiasUnits_Type.__name__ = "Integer32"
_AdGenPluggablePortChannelTxBiasUnits_Object = MibTableColumn
adGenPluggablePortChannelTxBiasUnits = _AdGenPluggablePortChannelTxBiasUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 1, 2, 1, 8),
    _AdGenPluggablePortChannelTxBiasUnits_Type()
)
adGenPluggablePortChannelTxBiasUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortChannelTxBiasUnits.setStatus("current")
_AdGenPluggablePortStats_ObjectIdentity = ObjectIdentity
adGenPluggablePortStats = _AdGenPluggablePortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2)
)
_AdGenPluggablePortTotalStatsTable_Object = MibTable
adGenPluggablePortTotalStatsTable = _AdGenPluggablePortTotalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 1)
)
if mibBuilder.loadTexts:
    adGenPluggablePortTotalStatsTable.setStatus("current")
_AdGenPluggablePortTotalStatsEntry_Object = MibTableRow
adGenPluggablePortTotalStatsEntry = _AdGenPluggablePortTotalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 1, 1)
)
adGenPluggablePortTotalStatsEntry.setIndexNames(
    (0, "ADTRAN-PLUGGABLE-PORT-MIB", "adGenPluggablePortTotalStatsIndex"),
)
if mibBuilder.loadTexts:
    adGenPluggablePortTotalStatsEntry.setStatus("current")
_AdGenPluggablePortTotalStatsIndex_Type = InterfaceIndex
_AdGenPluggablePortTotalStatsIndex_Object = MibTableColumn
adGenPluggablePortTotalStatsIndex = _AdGenPluggablePortTotalStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 1, 1, 1),
    _AdGenPluggablePortTotalStatsIndex_Type()
)
adGenPluggablePortTotalStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenPluggablePortTotalStatsIndex.setStatus("current")
_AdGenPluggablePortTotalStatsMaxRxPower_Type = Integer32
_AdGenPluggablePortTotalStatsMaxRxPower_Object = MibTableColumn
adGenPluggablePortTotalStatsMaxRxPower = _AdGenPluggablePortTotalStatsMaxRxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 1, 1, 2),
    _AdGenPluggablePortTotalStatsMaxRxPower_Type()
)
adGenPluggablePortTotalStatsMaxRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortTotalStatsMaxRxPower.setStatus("current")
_AdGenPluggablePortTotalStatsMinRxPower_Type = Integer32
_AdGenPluggablePortTotalStatsMinRxPower_Object = MibTableColumn
adGenPluggablePortTotalStatsMinRxPower = _AdGenPluggablePortTotalStatsMinRxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 1, 1, 3),
    _AdGenPluggablePortTotalStatsMinRxPower_Type()
)
adGenPluggablePortTotalStatsMinRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortTotalStatsMinRxPower.setStatus("current")
_AdGenPluggablePortTotalStatsAvgRxPower_Type = Integer32
_AdGenPluggablePortTotalStatsAvgRxPower_Object = MibTableColumn
adGenPluggablePortTotalStatsAvgRxPower = _AdGenPluggablePortTotalStatsAvgRxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 1, 1, 4),
    _AdGenPluggablePortTotalStatsAvgRxPower_Type()
)
adGenPluggablePortTotalStatsAvgRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortTotalStatsAvgRxPower.setStatus("current")
_AdGenPluggablePortTotalStatsMaxTxPower_Type = Integer32
_AdGenPluggablePortTotalStatsMaxTxPower_Object = MibTableColumn
adGenPluggablePortTotalStatsMaxTxPower = _AdGenPluggablePortTotalStatsMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 1, 1, 5),
    _AdGenPluggablePortTotalStatsMaxTxPower_Type()
)
adGenPluggablePortTotalStatsMaxTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortTotalStatsMaxTxPower.setStatus("current")
_AdGenPluggablePortTotalStatsMinTxPower_Type = Integer32
_AdGenPluggablePortTotalStatsMinTxPower_Object = MibTableColumn
adGenPluggablePortTotalStatsMinTxPower = _AdGenPluggablePortTotalStatsMinTxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 1, 1, 6),
    _AdGenPluggablePortTotalStatsMinTxPower_Type()
)
adGenPluggablePortTotalStatsMinTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortTotalStatsMinTxPower.setStatus("current")
_AdGenPluggablePortTotalStatsAvgTxPower_Type = Integer32
_AdGenPluggablePortTotalStatsAvgTxPower_Object = MibTableColumn
adGenPluggablePortTotalStatsAvgTxPower = _AdGenPluggablePortTotalStatsAvgTxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 1, 1, 7),
    _AdGenPluggablePortTotalStatsAvgTxPower_Type()
)
adGenPluggablePortTotalStatsAvgTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortTotalStatsAvgTxPower.setStatus("current")
_AdGenPluggablePortCurrentStatsTable_Object = MibTable
adGenPluggablePortCurrentStatsTable = _AdGenPluggablePortCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 2)
)
if mibBuilder.loadTexts:
    adGenPluggablePortCurrentStatsTable.setStatus("current")
_AdGenPluggablePortCurrentStatsEntry_Object = MibTableRow
adGenPluggablePortCurrentStatsEntry = _AdGenPluggablePortCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 2, 1)
)
adGenPluggablePortCurrentStatsEntry.setIndexNames(
    (0, "ADTRAN-PLUGGABLE-PORT-MIB", "adGenPluggablePortCurrentStatsIndex"),
)
if mibBuilder.loadTexts:
    adGenPluggablePortCurrentStatsEntry.setStatus("current")
_AdGenPluggablePortCurrentStatsIndex_Type = InterfaceIndex
_AdGenPluggablePortCurrentStatsIndex_Object = MibTableColumn
adGenPluggablePortCurrentStatsIndex = _AdGenPluggablePortCurrentStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 2, 1, 1),
    _AdGenPluggablePortCurrentStatsIndex_Type()
)
adGenPluggablePortCurrentStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenPluggablePortCurrentStatsIndex.setStatus("current")
_AdGenPluggablePortCurrentStatsMaxRxPower_Type = Integer32
_AdGenPluggablePortCurrentStatsMaxRxPower_Object = MibTableColumn
adGenPluggablePortCurrentStatsMaxRxPower = _AdGenPluggablePortCurrentStatsMaxRxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 2, 1, 2),
    _AdGenPluggablePortCurrentStatsMaxRxPower_Type()
)
adGenPluggablePortCurrentStatsMaxRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortCurrentStatsMaxRxPower.setStatus("current")
_AdGenPluggablePortCurrentStatsMinRxPower_Type = Integer32
_AdGenPluggablePortCurrentStatsMinRxPower_Object = MibTableColumn
adGenPluggablePortCurrentStatsMinRxPower = _AdGenPluggablePortCurrentStatsMinRxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 2, 1, 3),
    _AdGenPluggablePortCurrentStatsMinRxPower_Type()
)
adGenPluggablePortCurrentStatsMinRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortCurrentStatsMinRxPower.setStatus("current")
_AdGenPluggablePortCurrentStatsAvgRxPower_Type = Integer32
_AdGenPluggablePortCurrentStatsAvgRxPower_Object = MibTableColumn
adGenPluggablePortCurrentStatsAvgRxPower = _AdGenPluggablePortCurrentStatsAvgRxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 2, 1, 4),
    _AdGenPluggablePortCurrentStatsAvgRxPower_Type()
)
adGenPluggablePortCurrentStatsAvgRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortCurrentStatsAvgRxPower.setStatus("current")
_AdGenPluggablePortCurrentStatsMaxTxPower_Type = Integer32
_AdGenPluggablePortCurrentStatsMaxTxPower_Object = MibTableColumn
adGenPluggablePortCurrentStatsMaxTxPower = _AdGenPluggablePortCurrentStatsMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 2, 1, 5),
    _AdGenPluggablePortCurrentStatsMaxTxPower_Type()
)
adGenPluggablePortCurrentStatsMaxTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortCurrentStatsMaxTxPower.setStatus("current")
_AdGenPluggablePortCurrentStatsMinTxPower_Type = Integer32
_AdGenPluggablePortCurrentStatsMinTxPower_Object = MibTableColumn
adGenPluggablePortCurrentStatsMinTxPower = _AdGenPluggablePortCurrentStatsMinTxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 2, 1, 6),
    _AdGenPluggablePortCurrentStatsMinTxPower_Type()
)
adGenPluggablePortCurrentStatsMinTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortCurrentStatsMinTxPower.setStatus("current")
_AdGenPluggablePortCurrentStatsAvgTxPower_Type = Integer32
_AdGenPluggablePortCurrentStatsAvgTxPower_Object = MibTableColumn
adGenPluggablePortCurrentStatsAvgTxPower = _AdGenPluggablePortCurrentStatsAvgTxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 2, 1, 7),
    _AdGenPluggablePortCurrentStatsAvgTxPower_Type()
)
adGenPluggablePortCurrentStatsAvgTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortCurrentStatsAvgTxPower.setStatus("current")
_AdGenPluggablePortDayStatsTable_Object = MibTable
adGenPluggablePortDayStatsTable = _AdGenPluggablePortDayStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 3)
)
if mibBuilder.loadTexts:
    adGenPluggablePortDayStatsTable.setStatus("current")
_AdGenPluggablePortDayStatsEntry_Object = MibTableRow
adGenPluggablePortDayStatsEntry = _AdGenPluggablePortDayStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 3, 1)
)
adGenPluggablePortDayStatsEntry.setIndexNames(
    (0, "ADTRAN-PLUGGABLE-PORT-MIB", "adGenPluggablePortDayStatsIndex"),
)
if mibBuilder.loadTexts:
    adGenPluggablePortDayStatsEntry.setStatus("current")
_AdGenPluggablePortDayStatsIndex_Type = InterfaceIndex
_AdGenPluggablePortDayStatsIndex_Object = MibTableColumn
adGenPluggablePortDayStatsIndex = _AdGenPluggablePortDayStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 3, 1, 1),
    _AdGenPluggablePortDayStatsIndex_Type()
)
adGenPluggablePortDayStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenPluggablePortDayStatsIndex.setStatus("current")
_AdGenPluggablePortDayStatsMaxRxPower_Type = Integer32
_AdGenPluggablePortDayStatsMaxRxPower_Object = MibTableColumn
adGenPluggablePortDayStatsMaxRxPower = _AdGenPluggablePortDayStatsMaxRxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 3, 1, 2),
    _AdGenPluggablePortDayStatsMaxRxPower_Type()
)
adGenPluggablePortDayStatsMaxRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortDayStatsMaxRxPower.setStatus("current")
_AdGenPluggablePortDayStatsMinRxPower_Type = Integer32
_AdGenPluggablePortDayStatsMinRxPower_Object = MibTableColumn
adGenPluggablePortDayStatsMinRxPower = _AdGenPluggablePortDayStatsMinRxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 3, 1, 3),
    _AdGenPluggablePortDayStatsMinRxPower_Type()
)
adGenPluggablePortDayStatsMinRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortDayStatsMinRxPower.setStatus("current")
_AdGenPluggablePortDayStatsAvgRxPower_Type = Integer32
_AdGenPluggablePortDayStatsAvgRxPower_Object = MibTableColumn
adGenPluggablePortDayStatsAvgRxPower = _AdGenPluggablePortDayStatsAvgRxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 3, 1, 4),
    _AdGenPluggablePortDayStatsAvgRxPower_Type()
)
adGenPluggablePortDayStatsAvgRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortDayStatsAvgRxPower.setStatus("current")
_AdGenPluggablePortDayStatsMaxTxPower_Type = Integer32
_AdGenPluggablePortDayStatsMaxTxPower_Object = MibTableColumn
adGenPluggablePortDayStatsMaxTxPower = _AdGenPluggablePortDayStatsMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 3, 1, 5),
    _AdGenPluggablePortDayStatsMaxTxPower_Type()
)
adGenPluggablePortDayStatsMaxTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortDayStatsMaxTxPower.setStatus("current")
_AdGenPluggablePortDayStatsMinTxPower_Type = Integer32
_AdGenPluggablePortDayStatsMinTxPower_Object = MibTableColumn
adGenPluggablePortDayStatsMinTxPower = _AdGenPluggablePortDayStatsMinTxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 3, 1, 6),
    _AdGenPluggablePortDayStatsMinTxPower_Type()
)
adGenPluggablePortDayStatsMinTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortDayStatsMinTxPower.setStatus("current")
_AdGenPluggablePortDayStatsAvgTxPower_Type = Integer32
_AdGenPluggablePortDayStatsAvgTxPower_Object = MibTableColumn
adGenPluggablePortDayStatsAvgTxPower = _AdGenPluggablePortDayStatsAvgTxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 3, 1, 7),
    _AdGenPluggablePortDayStatsAvgTxPower_Type()
)
adGenPluggablePortDayStatsAvgTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortDayStatsAvgTxPower.setStatus("current")
_AdGenPluggablePortIntervalStatsTable_Object = MibTable
adGenPluggablePortIntervalStatsTable = _AdGenPluggablePortIntervalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 4)
)
if mibBuilder.loadTexts:
    adGenPluggablePortIntervalStatsTable.setStatus("current")
_AdGenPluggablePortIntervalStatsEntry_Object = MibTableRow
adGenPluggablePortIntervalStatsEntry = _AdGenPluggablePortIntervalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 4, 1)
)
adGenPluggablePortIntervalStatsEntry.setIndexNames(
    (0, "ADTRAN-PLUGGABLE-PORT-MIB", "adGenPluggablePortIntervalStatsIndex"),
    (0, "ADTRAN-PLUGGABLE-PORT-MIB", "adGenPluggablePortIntervalStatsInterval"),
)
if mibBuilder.loadTexts:
    adGenPluggablePortIntervalStatsEntry.setStatus("current")
_AdGenPluggablePortIntervalStatsIndex_Type = InterfaceIndex
_AdGenPluggablePortIntervalStatsIndex_Object = MibTableColumn
adGenPluggablePortIntervalStatsIndex = _AdGenPluggablePortIntervalStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 4, 1, 1),
    _AdGenPluggablePortIntervalStatsIndex_Type()
)
adGenPluggablePortIntervalStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenPluggablePortIntervalStatsIndex.setStatus("current")


class _AdGenPluggablePortIntervalStatsInterval_Type(Unsigned32):
    """Custom type adGenPluggablePortIntervalStatsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AdGenPluggablePortIntervalStatsInterval_Type.__name__ = "Unsigned32"
_AdGenPluggablePortIntervalStatsInterval_Object = MibTableColumn
adGenPluggablePortIntervalStatsInterval = _AdGenPluggablePortIntervalStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 4, 1, 2),
    _AdGenPluggablePortIntervalStatsInterval_Type()
)
adGenPluggablePortIntervalStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenPluggablePortIntervalStatsInterval.setStatus("current")
_AdGenPluggablePortIntervalStatsMaxRxPower_Type = Integer32
_AdGenPluggablePortIntervalStatsMaxRxPower_Object = MibTableColumn
adGenPluggablePortIntervalStatsMaxRxPower = _AdGenPluggablePortIntervalStatsMaxRxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 4, 1, 3),
    _AdGenPluggablePortIntervalStatsMaxRxPower_Type()
)
adGenPluggablePortIntervalStatsMaxRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortIntervalStatsMaxRxPower.setStatus("current")
_AdGenPluggablePortIntervalStatsMinRxPower_Type = Integer32
_AdGenPluggablePortIntervalStatsMinRxPower_Object = MibTableColumn
adGenPluggablePortIntervalStatsMinRxPower = _AdGenPluggablePortIntervalStatsMinRxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 4, 1, 4),
    _AdGenPluggablePortIntervalStatsMinRxPower_Type()
)
adGenPluggablePortIntervalStatsMinRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortIntervalStatsMinRxPower.setStatus("current")
_AdGenPluggablePortIntervalStatsAvgRxPower_Type = Integer32
_AdGenPluggablePortIntervalStatsAvgRxPower_Object = MibTableColumn
adGenPluggablePortIntervalStatsAvgRxPower = _AdGenPluggablePortIntervalStatsAvgRxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 4, 1, 5),
    _AdGenPluggablePortIntervalStatsAvgRxPower_Type()
)
adGenPluggablePortIntervalStatsAvgRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortIntervalStatsAvgRxPower.setStatus("current")
_AdGenPluggablePortIntervalStatsMaxTxPower_Type = Integer32
_AdGenPluggablePortIntervalStatsMaxTxPower_Object = MibTableColumn
adGenPluggablePortIntervalStatsMaxTxPower = _AdGenPluggablePortIntervalStatsMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 4, 1, 6),
    _AdGenPluggablePortIntervalStatsMaxTxPower_Type()
)
adGenPluggablePortIntervalStatsMaxTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortIntervalStatsMaxTxPower.setStatus("current")
_AdGenPluggablePortIntervalStatsMinTxPower_Type = Integer32
_AdGenPluggablePortIntervalStatsMinTxPower_Object = MibTableColumn
adGenPluggablePortIntervalStatsMinTxPower = _AdGenPluggablePortIntervalStatsMinTxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 4, 1, 7),
    _AdGenPluggablePortIntervalStatsMinTxPower_Type()
)
adGenPluggablePortIntervalStatsMinTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortIntervalStatsMinTxPower.setStatus("current")
_AdGenPluggablePortIntervalStatsAvgTxPower_Type = Integer32
_AdGenPluggablePortIntervalStatsAvgTxPower_Object = MibTableColumn
adGenPluggablePortIntervalStatsAvgTxPower = _AdGenPluggablePortIntervalStatsAvgTxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 2, 4, 1, 8),
    _AdGenPluggablePortIntervalStatsAvgTxPower_Type()
)
adGenPluggablePortIntervalStatsAvgTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortIntervalStatsAvgTxPower.setStatus("current")
_AdGenPluggablePortScalars_ObjectIdentity = ObjectIdentity
adGenPluggablePortScalars = _AdGenPluggablePortScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 3)
)


class _AdGenPluggablePortAlarmLevel_Type(Integer32):
    """Custom type adGenPluggablePortAlarmLevel based on Integer32"""
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
        *(("disabled", 1),
          ("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdGenPluggablePortAlarmLevel_Type.__name__ = "Integer32"
_AdGenPluggablePortAlarmLevel_Object = MibScalar
adGenPluggablePortAlarmLevel = _AdGenPluggablePortAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 3, 1),
    _AdGenPluggablePortAlarmLevel_Type()
)
adGenPluggablePortAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPluggablePortAlarmLevel.setStatus("deprecated")
_AdGenPluggablePortTraps_ObjectIdentity = ObjectIdentity
adGenPluggablePortTraps = _AdGenPluggablePortTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 4)
)
_AdGenPluggablePortAlarms_ObjectIdentity = ObjectIdentity
adGenPluggablePortAlarms = _AdGenPluggablePortAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 4, 0)
)
_AdGenPluggablePortProv_ObjectIdentity = ObjectIdentity
adGenPluggablePortProv = _AdGenPluggablePortProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 5)
)
_AdGenPluggablePortProvTable_Object = MibTable
adGenPluggablePortProvTable = _AdGenPluggablePortProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 5, 1)
)
if mibBuilder.loadTexts:
    adGenPluggablePortProvTable.setStatus("current")
_AdGenPluggablePortProvEntry_Object = MibTableRow
adGenPluggablePortProvEntry = _AdGenPluggablePortProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 5, 1, 1)
)
adGenPluggablePortProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenPluggablePortProvEntry.setStatus("current")
_AdGenPluggablePortProvWaveLength_Type = Integer32
_AdGenPluggablePortProvWaveLength_Object = MibTableColumn
adGenPluggablePortProvWaveLength = _AdGenPluggablePortProvWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 5, 1, 1, 1),
    _AdGenPluggablePortProvWaveLength_Type()
)
adGenPluggablePortProvWaveLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPluggablePortProvWaveLength.setStatus("current")
_AdGenPluggablePortProvChannelNumber_Type = Integer32
_AdGenPluggablePortProvChannelNumber_Object = MibTableColumn
adGenPluggablePortProvChannelNumber = _AdGenPluggablePortProvChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 5, 1, 1, 2),
    _AdGenPluggablePortProvChannelNumber_Type()
)
adGenPluggablePortProvChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPluggablePortProvChannelNumber.setStatus("current")
_AdGenPluggableAlarmSlotProvTable_Object = MibTable
adGenPluggableAlarmSlotProvTable = _AdGenPluggableAlarmSlotProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 5, 2)
)
if mibBuilder.loadTexts:
    adGenPluggableAlarmSlotProvTable.setStatus("current")
_AdGenPluggableAlarmSlotProvEntry_Object = MibTableRow
adGenPluggableAlarmSlotProvEntry = _AdGenPluggableAlarmSlotProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 5, 2, 1)
)
adGenPluggableAlarmSlotProvEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenPluggableAlarmSlotProvEntry.setStatus("current")


class _AdGenPluggableAlarmSlotTxFaultLevel_Type(Integer32):
    """Custom type adGenPluggableAlarmSlotTxFaultLevel based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdGenPluggableAlarmSlotTxFaultLevel_Type.__name__ = "Integer32"
_AdGenPluggableAlarmSlotTxFaultLevel_Object = MibTableColumn
adGenPluggableAlarmSlotTxFaultLevel = _AdGenPluggableAlarmSlotTxFaultLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 5, 2, 1, 1),
    _AdGenPluggableAlarmSlotTxFaultLevel_Type()
)
adGenPluggableAlarmSlotTxFaultLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPluggableAlarmSlotTxFaultLevel.setStatus("current")


class _AdGenPluggableAlarmSlotMissingLevel_Type(Integer32):
    """Custom type adGenPluggableAlarmSlotMissingLevel based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdGenPluggableAlarmSlotMissingLevel_Type.__name__ = "Integer32"
_AdGenPluggableAlarmSlotMissingLevel_Object = MibTableColumn
adGenPluggableAlarmSlotMissingLevel = _AdGenPluggableAlarmSlotMissingLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 5, 2, 1, 2),
    _AdGenPluggableAlarmSlotMissingLevel_Type()
)
adGenPluggableAlarmSlotMissingLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPluggableAlarmSlotMissingLevel.setStatus("current")

# Managed Objects groups


# Notification objects

adGenPluggablePortTxFaultClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 4, 0, 2)
)
adGenPluggablePortTxFaultClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    adGenPluggablePortTxFaultClear.setStatus(
        "current"
    )

adGenPluggablePortTxFaultSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 4, 0, 3)
)
adGenPluggablePortTxFaultSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    adGenPluggablePortTxFaultSet.setStatus(
        "current"
    )

adGenPluggablePortMissingClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 4, 0, 4)
)
adGenPluggablePortMissingClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    adGenPluggablePortMissingClear.setStatus(
        "current"
    )

adGenPluggablePortMissingSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 4, 0, 5)
)
adGenPluggablePortMissingSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    adGenPluggablePortMissingSet.setStatus(
        "current"
    )

adGenPluggablePortUnsupportedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 4, 0, 6)
)
adGenPluggablePortUnsupportedClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    adGenPluggablePortUnsupportedClear.setStatus(
        "current"
    )

adGenPluggablePortUnsupportedSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 4, 0, 7)
)
adGenPluggablePortUnsupportedSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    adGenPluggablePortUnsupportedSet.setStatus(
        "current"
    )

adGenPluggablePortMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 4, 0, 8)
)
adGenPluggablePortMismatchClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    adGenPluggablePortMismatchClear.setStatus(
        "current"
    )

adGenPluggablePortMismatchSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 4, 0, 9)
)
adGenPluggablePortMismatchSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    adGenPluggablePortMismatchSet.setStatus(
        "current"
    )

adGenPluggablePortTempClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 4, 0, 10)
)
adGenPluggablePortTempClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    adGenPluggablePortTempClear.setStatus(
        "current"
    )

adGenPluggablePortTempSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 4, 0, 11)
)
adGenPluggablePortTempSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    adGenPluggablePortTempSet.setStatus(
        "current"
    )

adGenPluggablePortProvWavelengthMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 4, 0, 12)
)
adGenPluggablePortProvWavelengthMismatchClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    adGenPluggablePortProvWavelengthMismatchClear.setStatus(
        "current"
    )

adGenPluggablePortProvWavelengthMismatchSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 4, 4, 0, 13)
)
adGenPluggablePortProvWavelengthMismatchSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    adGenPluggablePortProvWavelengthMismatchSet.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-PLUGGABLE-PORT-MIB",
    **{"PluggablePortPowerUnits": PluggablePortPowerUnits,
       "adGenPluggablePortObjects": adGenPluggablePortObjects,
       "adGenPluggablePortTable": adGenPluggablePortTable,
       "adGenPluggablePortEntry": adGenPluggablePortEntry,
       "adGenPluggablePortIndex": adGenPluggablePortIndex,
       "adGenPluggablePortPluggableType": adGenPluggablePortPluggableType,
       "adGenPluggablePortConnectorType": adGenPluggablePortConnectorType,
       "adGenPluggablePortCapabilities": adGenPluggablePortCapabilities,
       "adGenPluggablePortState": adGenPluggablePortState,
       "adGenPluggablePortStatusBits": adGenPluggablePortStatusBits,
       "adGenPluggablePortAlarmBits": adGenPluggablePortAlarmBits,
       "adGenPluggablePortAlarmsSuppressed": adGenPluggablePortAlarmsSuppressed,
       "adGenPluggablePortBer": adGenPluggablePortBer,
       "adGenPluggablePortVendorName": adGenPluggablePortVendorName,
       "adGenPluggablePortVendorPartNumber": adGenPluggablePortVendorPartNumber,
       "adGenPluggablePortVendorSerialNumber": adGenPluggablePortVendorSerialNumber,
       "adGenPluggablePortAdtranName": adGenPluggablePortAdtranName,
       "adGenPluggablePortAdtranPartNumber": adGenPluggablePortAdtranPartNumber,
       "adGenPluggablePortAdtranClei": adGenPluggablePortAdtranClei,
       "adGenPluggablePortWavelength": adGenPluggablePortWavelength,
       "adGenPluggablePortMinBitRate": adGenPluggablePortMinBitRate,
       "adGenPluggablePortMaxBitRate": adGenPluggablePortMaxBitRate,
       "adGenPluggablePortReachLength": adGenPluggablePortReachLength,
       "adGenPluggablePortReachUnits": adGenPluggablePortReachUnits,
       "adGenPluggablePortRxPower": adGenPluggablePortRxPower,
       "adGenPluggablePortRxPowerUnits": adGenPluggablePortRxPowerUnits,
       "adGenPluggablePortTxPower": adGenPluggablePortTxPower,
       "adGenPluggablePortTxPowerUnits": adGenPluggablePortTxPowerUnits,
       "adGenPluggablePortTxBias": adGenPluggablePortTxBias,
       "adGenPluggablePortTxBiasUnits": adGenPluggablePortTxBiasUnits,
       "adGenPluggablePortTemperature": adGenPluggablePortTemperature,
       "adGenPluggablePortTemperatureUnits": adGenPluggablePortTemperatureUnits,
       "adGenPluggablePortVoltage": adGenPluggablePortVoltage,
       "adGenPluggablePortVendorRevision": adGenPluggablePortVendorRevision,
       "adGenPluggablePortWavelengthPicoMeter": adGenPluggablePortWavelengthPicoMeter,
       "adGenPluggableNumberOfXcvrChannels": adGenPluggableNumberOfXcvrChannels,
       "adGenPluggablePortChannelTable": adGenPluggablePortChannelTable,
       "adGenPluggablePortChannelEntry": adGenPluggablePortChannelEntry,
       "adGenPluggablePortChannelModuleIndex": adGenPluggablePortChannelModuleIndex,
       "adGenPluggablePortChannelXcvrIndex": adGenPluggablePortChannelXcvrIndex,
       "adGenPluggablePortChannelRxPower": adGenPluggablePortChannelRxPower,
       "adGenPluggablePortChannelRxPowerUnits": adGenPluggablePortChannelRxPowerUnits,
       "adGenPluggablePortChannelTxPower": adGenPluggablePortChannelTxPower,
       "adGenPluggablePortChannelTxPowerUnits": adGenPluggablePortChannelTxPowerUnits,
       "adGenPluggablePortChannelTxBias": adGenPluggablePortChannelTxBias,
       "adGenPluggablePortChannelTxBiasUnits": adGenPluggablePortChannelTxBiasUnits,
       "adGenPluggablePortStats": adGenPluggablePortStats,
       "adGenPluggablePortTotalStatsTable": adGenPluggablePortTotalStatsTable,
       "adGenPluggablePortTotalStatsEntry": adGenPluggablePortTotalStatsEntry,
       "adGenPluggablePortTotalStatsIndex": adGenPluggablePortTotalStatsIndex,
       "adGenPluggablePortTotalStatsMaxRxPower": adGenPluggablePortTotalStatsMaxRxPower,
       "adGenPluggablePortTotalStatsMinRxPower": adGenPluggablePortTotalStatsMinRxPower,
       "adGenPluggablePortTotalStatsAvgRxPower": adGenPluggablePortTotalStatsAvgRxPower,
       "adGenPluggablePortTotalStatsMaxTxPower": adGenPluggablePortTotalStatsMaxTxPower,
       "adGenPluggablePortTotalStatsMinTxPower": adGenPluggablePortTotalStatsMinTxPower,
       "adGenPluggablePortTotalStatsAvgTxPower": adGenPluggablePortTotalStatsAvgTxPower,
       "adGenPluggablePortCurrentStatsTable": adGenPluggablePortCurrentStatsTable,
       "adGenPluggablePortCurrentStatsEntry": adGenPluggablePortCurrentStatsEntry,
       "adGenPluggablePortCurrentStatsIndex": adGenPluggablePortCurrentStatsIndex,
       "adGenPluggablePortCurrentStatsMaxRxPower": adGenPluggablePortCurrentStatsMaxRxPower,
       "adGenPluggablePortCurrentStatsMinRxPower": adGenPluggablePortCurrentStatsMinRxPower,
       "adGenPluggablePortCurrentStatsAvgRxPower": adGenPluggablePortCurrentStatsAvgRxPower,
       "adGenPluggablePortCurrentStatsMaxTxPower": adGenPluggablePortCurrentStatsMaxTxPower,
       "adGenPluggablePortCurrentStatsMinTxPower": adGenPluggablePortCurrentStatsMinTxPower,
       "adGenPluggablePortCurrentStatsAvgTxPower": adGenPluggablePortCurrentStatsAvgTxPower,
       "adGenPluggablePortDayStatsTable": adGenPluggablePortDayStatsTable,
       "adGenPluggablePortDayStatsEntry": adGenPluggablePortDayStatsEntry,
       "adGenPluggablePortDayStatsIndex": adGenPluggablePortDayStatsIndex,
       "adGenPluggablePortDayStatsMaxRxPower": adGenPluggablePortDayStatsMaxRxPower,
       "adGenPluggablePortDayStatsMinRxPower": adGenPluggablePortDayStatsMinRxPower,
       "adGenPluggablePortDayStatsAvgRxPower": adGenPluggablePortDayStatsAvgRxPower,
       "adGenPluggablePortDayStatsMaxTxPower": adGenPluggablePortDayStatsMaxTxPower,
       "adGenPluggablePortDayStatsMinTxPower": adGenPluggablePortDayStatsMinTxPower,
       "adGenPluggablePortDayStatsAvgTxPower": adGenPluggablePortDayStatsAvgTxPower,
       "adGenPluggablePortIntervalStatsTable": adGenPluggablePortIntervalStatsTable,
       "adGenPluggablePortIntervalStatsEntry": adGenPluggablePortIntervalStatsEntry,
       "adGenPluggablePortIntervalStatsIndex": adGenPluggablePortIntervalStatsIndex,
       "adGenPluggablePortIntervalStatsInterval": adGenPluggablePortIntervalStatsInterval,
       "adGenPluggablePortIntervalStatsMaxRxPower": adGenPluggablePortIntervalStatsMaxRxPower,
       "adGenPluggablePortIntervalStatsMinRxPower": adGenPluggablePortIntervalStatsMinRxPower,
       "adGenPluggablePortIntervalStatsAvgRxPower": adGenPluggablePortIntervalStatsAvgRxPower,
       "adGenPluggablePortIntervalStatsMaxTxPower": adGenPluggablePortIntervalStatsMaxTxPower,
       "adGenPluggablePortIntervalStatsMinTxPower": adGenPluggablePortIntervalStatsMinTxPower,
       "adGenPluggablePortIntervalStatsAvgTxPower": adGenPluggablePortIntervalStatsAvgTxPower,
       "adGenPluggablePortScalars": adGenPluggablePortScalars,
       "adGenPluggablePortAlarmLevel": adGenPluggablePortAlarmLevel,
       "adGenPluggablePortTraps": adGenPluggablePortTraps,
       "adGenPluggablePortAlarms": adGenPluggablePortAlarms,
       "adGenPluggablePortTxFaultClear": adGenPluggablePortTxFaultClear,
       "adGenPluggablePortTxFaultSet": adGenPluggablePortTxFaultSet,
       "adGenPluggablePortMissingClear": adGenPluggablePortMissingClear,
       "adGenPluggablePortMissingSet": adGenPluggablePortMissingSet,
       "adGenPluggablePortUnsupportedClear": adGenPluggablePortUnsupportedClear,
       "adGenPluggablePortUnsupportedSet": adGenPluggablePortUnsupportedSet,
       "adGenPluggablePortMismatchClear": adGenPluggablePortMismatchClear,
       "adGenPluggablePortMismatchSet": adGenPluggablePortMismatchSet,
       "adGenPluggablePortTempClear": adGenPluggablePortTempClear,
       "adGenPluggablePortTempSet": adGenPluggablePortTempSet,
       "adGenPluggablePortProvWavelengthMismatchClear": adGenPluggablePortProvWavelengthMismatchClear,
       "adGenPluggablePortProvWavelengthMismatchSet": adGenPluggablePortProvWavelengthMismatchSet,
       "adGenPluggablePortProv": adGenPluggablePortProv,
       "adGenPluggablePortProvTable": adGenPluggablePortProvTable,
       "adGenPluggablePortProvEntry": adGenPluggablePortProvEntry,
       "adGenPluggablePortProvWaveLength": adGenPluggablePortProvWaveLength,
       "adGenPluggablePortProvChannelNumber": adGenPluggablePortProvChannelNumber,
       "adGenPluggableAlarmSlotProvTable": adGenPluggableAlarmSlotProvTable,
       "adGenPluggableAlarmSlotProvEntry": adGenPluggableAlarmSlotProvEntry,
       "adGenPluggableAlarmSlotTxFaultLevel": adGenPluggableAlarmSlotTxFaultLevel,
       "adGenPluggableAlarmSlotMissingLevel": adGenPluggableAlarmSlotMissingLevel,
       "adGenPluggablePortMIB": adGenPluggablePortMIB}
)
