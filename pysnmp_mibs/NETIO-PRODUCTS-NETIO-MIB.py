# SNMP MIB module (NETIO-PRODUCTS-NETIO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/netio/NETIO-PRODUCTS-NETIO-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:03:18 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

netioProducts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47952)
)
if mibBuilder.loadTexts:
    netioProducts.setRevisions(
        ("2017-03-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Netio4_ObjectIdentity = ObjectIdentity
netio4 = _Netio4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47952, 1)
)
_NetioOutputTable_Object = MibTable
netioOutputTable = _NetioOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 47952, 1, 1)
)
if mibBuilder.loadTexts:
    netioOutputTable.setStatus("current")
_NetioOutputEntry_Object = MibTableRow
netioOutputEntry = _NetioOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 47952, 1, 1, 1)
)
netioOutputEntry.setIndexNames(
    (0, "NETIO-PRODUCTS-NETIO-MIB", "netioOutputID"),
)
if mibBuilder.loadTexts:
    netioOutputEntry.setStatus("current")


class _NetioOutputID_Type(Integer32):
    """Custom type netioOutputID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_NetioOutputID_Type.__name__ = "Integer32"
_NetioOutputID_Object = MibTableColumn
netioOutputID = _NetioOutputID_Object(
    (1, 3, 6, 1, 4, 1, 47952, 1, 1, 1, 1),
    _NetioOutputID_Type()
)
netioOutputID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netioOutputID.setStatus("current")


class _NetioOutputName_Type(OctetString):
    """Custom type netioOutputName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NetioOutputName_Type.__name__ = "OctetString"
_NetioOutputName_Object = MibTableColumn
netioOutputName = _NetioOutputName_Object(
    (1, 3, 6, 1, 4, 1, 47952, 1, 1, 1, 2),
    _NetioOutputName_Type()
)
netioOutputName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netioOutputName.setStatus("current")


class _NetioOutputState_Type(Integer32):
    """Custom type netioOutputState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NetioOutputState_Type.__name__ = "Integer32"
_NetioOutputState_Object = MibTableColumn
netioOutputState = _NetioOutputState_Object(
    (1, 3, 6, 1, 4, 1, 47952, 1, 1, 1, 3),
    _NetioOutputState_Type()
)
netioOutputState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netioOutputState.setStatus("current")


class _NetioOutputStateString_Type(OctetString):
    """Custom type netioOutputStateString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NetioOutputStateString_Type.__name__ = "OctetString"
_NetioOutputStateString_Object = MibTableColumn
netioOutputStateString = _NetioOutputStateString_Object(
    (1, 3, 6, 1, 4, 1, 47952, 1, 1, 1, 4),
    _NetioOutputStateString_Type()
)
netioOutputStateString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netioOutputStateString.setStatus("current")


class _NetioOutputAction_Type(Integer32):
    """Custom type netioOutputAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("reset", 2),
          ("shortOn", 3),
          ("switch", 4),
          ("idle", 5))
    )


_NetioOutputAction_Type.__name__ = "Integer32"
_NetioOutputAction_Object = MibTableColumn
netioOutputAction = _NetioOutputAction_Object(
    (1, 3, 6, 1, 4, 1, 47952, 1, 1, 1, 5),
    _NetioOutputAction_Type()
)
netioOutputAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netioOutputAction.setStatus("current")


class _NetioOutputLoad_Type(Integer32):
    """Custom type netioOutputLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NetioOutputLoad_Type.__name__ = "Integer32"
_NetioOutputLoad_Object = MibTableColumn
netioOutputLoad = _NetioOutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 47952, 1, 1, 1, 25),
    _NetioOutputLoad_Type()
)
netioOutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netioOutputLoad.setStatus("current")


class _NetioOutputEnergy_Type(Integer32):
    """Custom type netioOutputEnergy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9223372036854775807),
    )


_NetioOutputEnergy_Type.__name__ = "Integer32"
_NetioOutputEnergy_Object = MibTableColumn
netioOutputEnergy = _NetioOutputEnergy_Object(
    (1, 3, 6, 1, 4, 1, 47952, 1, 1, 1, 26),
    _NetioOutputEnergy_Type()
)
netioOutputEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netioOutputEnergy.setStatus("current")
_NetioOutputEnergyStart_Type = DateAndTime
_NetioOutputEnergyStart_Object = MibTableColumn
netioOutputEnergyStart = _NetioOutputEnergyStart_Object(
    (1, 3, 6, 1, 4, 1, 47952, 1, 1, 1, 27),
    _NetioOutputEnergyStart_Type()
)
netioOutputEnergyStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netioOutputEnergyStart.setStatus("current")


class _NetioOutputCurrent_Type(Integer32):
    """Custom type netioOutputCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NetioOutputCurrent_Type.__name__ = "Integer32"
_NetioOutputCurrent_Object = MibTableColumn
netioOutputCurrent = _NetioOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 47952, 1, 1, 1, 28),
    _NetioOutputCurrent_Type()
)
netioOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netioOutputCurrent.setStatus("current")


class _NetioOutputPowerFactor_Type(Integer32):
    """Custom type netioOutputPowerFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_NetioOutputPowerFactor_Type.__name__ = "Integer32"
_NetioOutputPowerFactor_Object = MibTableColumn
netioOutputPowerFactor = _NetioOutputPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 47952, 1, 1, 1, 29),
    _NetioOutputPowerFactor_Type()
)
netioOutputPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netioOutputPowerFactor.setStatus("current")
_NetioGlobalMeasure_ObjectIdentity = ObjectIdentity
netioGlobalMeasure = _NetioGlobalMeasure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47952, 1, 2)
)


class _NetioVoltage_Type(Integer32):
    """Custom type netioVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NetioVoltage_Type.__name__ = "Integer32"
_NetioVoltage_Object = MibScalar
netioVoltage = _NetioVoltage_Object(
    (1, 3, 6, 1, 4, 1, 47952, 1, 2, 1),
    _NetioVoltage_Type()
)
netioVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netioVoltage.setStatus("current")


class _NetioFrequency_Type(Integer32):
    """Custom type netioFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NetioFrequency_Type.__name__ = "Integer32"
_NetioFrequency_Object = MibScalar
netioFrequency = _NetioFrequency_Object(
    (1, 3, 6, 1, 4, 1, 47952, 1, 2, 2),
    _NetioFrequency_Type()
)
netioFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netioFrequency.setStatus("current")


class _NetioTotalCurrent_Type(Integer32):
    """Custom type netioTotalCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NetioTotalCurrent_Type.__name__ = "Integer32"
_NetioTotalCurrent_Object = MibScalar
netioTotalCurrent = _NetioTotalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 47952, 1, 2, 3),
    _NetioTotalCurrent_Type()
)
netioTotalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netioTotalCurrent.setStatus("current")


class _NetioOverallPowerFactor_Type(Integer32):
    """Custom type netioOverallPowerFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_NetioOverallPowerFactor_Type.__name__ = "Integer32"
_NetioOverallPowerFactor_Object = MibScalar
netioOverallPowerFactor = _NetioOverallPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 47952, 1, 2, 4),
    _NetioOverallPowerFactor_Type()
)
netioOverallPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netioOverallPowerFactor.setStatus("current")


class _NetioTotalLoad_Type(Integer32):
    """Custom type netioTotalLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NetioTotalLoad_Type.__name__ = "Integer32"
_NetioTotalLoad_Object = MibScalar
netioTotalLoad = _NetioTotalLoad_Object(
    (1, 3, 6, 1, 4, 1, 47952, 1, 2, 5),
    _NetioTotalLoad_Type()
)
netioTotalLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netioTotalLoad.setStatus("current")


class _NetioTotalEnergy_Type(Integer32):
    """Custom type netioTotalEnergy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NetioTotalEnergy_Type.__name__ = "Integer32"
_NetioTotalEnergy_Object = MibScalar
netioTotalEnergy = _NetioTotalEnergy_Object(
    (1, 3, 6, 1, 4, 1, 47952, 1, 2, 6),
    _NetioTotalEnergy_Type()
)
netioTotalEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netioTotalEnergy.setStatus("current")
_NetioEnergyStart_Type = DateAndTime
_NetioEnergyStart_Object = MibScalar
netioEnergyStart = _NetioEnergyStart_Object(
    (1, 3, 6, 1, 4, 1, 47952, 1, 2, 7),
    _NetioEnergyStart_Type()
)
netioEnergyStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netioEnergyStart.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETIO-PRODUCTS-NETIO-MIB",
    **{"netioProducts": netioProducts,
       "netio4": netio4,
       "netioOutputTable": netioOutputTable,
       "netioOutputEntry": netioOutputEntry,
       "netioOutputID": netioOutputID,
       "netioOutputName": netioOutputName,
       "netioOutputState": netioOutputState,
       "netioOutputStateString": netioOutputStateString,
       "netioOutputAction": netioOutputAction,
       "netioOutputLoad": netioOutputLoad,
       "netioOutputEnergy": netioOutputEnergy,
       "netioOutputEnergyStart": netioOutputEnergyStart,
       "netioOutputCurrent": netioOutputCurrent,
       "netioOutputPowerFactor": netioOutputPowerFactor,
       "netioGlobalMeasure": netioGlobalMeasure,
       "netioVoltage": netioVoltage,
       "netioFrequency": netioFrequency,
       "netioTotalCurrent": netioTotalCurrent,
       "netioOverallPowerFactor": netioOverallPowerFactor,
       "netioTotalLoad": netioTotalLoad,
       "netioTotalEnergy": netioTotalEnergy,
       "netioEnergyStart": netioEnergyStart}
)
