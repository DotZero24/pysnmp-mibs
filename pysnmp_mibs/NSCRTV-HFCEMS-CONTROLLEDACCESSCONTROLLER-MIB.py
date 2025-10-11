# SNMP MIB module (NSCRTV-HFCEMS-CONTROLLEDACCESSCONTROLLER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nscrtv/NSCRTV-HFCEMS-CONTROLLEDACCESSCONTROLLER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:21:36 2025
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

(cacIdent,) = mibBuilder.importSymbols(
    "NSCRTV-ROOT",
    "cacIdent")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CacVendorOID_Type = ObjectIdentifier
_CacVendorOID_Object = MibScalar
cacVendorOID = _CacVendorOID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 13, 1),
    _CacVendorOID_Type()
)
cacVendorOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacVendorOID.setStatus("optional")


class _CacPowerType_Type(Integer32):
    """Custom type cacPowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v60", 1),
          ("v220", 2),
          ("other", 3))
    )


_CacPowerType_Type.__name__ = "Integer32"
_CacPowerType_Object = MibScalar
cacPowerType = _CacPowerType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 13, 2),
    _CacPowerType_Type()
)
cacPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacPowerType.setStatus("mandatory")


class _CacACPowerVoltage_Type(Integer32):
    """Custom type cacACPowerVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_CacACPowerVoltage_Type.__name__ = "Integer32"
_CacACPowerVoltage_Object = MibScalar
cacACPowerVoltage = _CacACPowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 13, 3),
    _CacACPowerVoltage_Type()
)
cacACPowerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacACPowerVoltage.setStatus("optional")


class _CacMainDCPowerVoltage_Type(Integer32):
    """Custom type cacMainDCPowerVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_CacMainDCPowerVoltage_Type.__name__ = "Integer32"
_CacMainDCPowerVoltage_Object = MibScalar
cacMainDCPowerVoltage = _CacMainDCPowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 13, 4),
    _CacMainDCPowerVoltage_Type()
)
cacMainDCPowerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacMainDCPowerVoltage.setStatus("mandatory")


class _CacInsideAmpOutputRFLevel_Type(Integer32):
    """Custom type cacInsideAmpOutputRFLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CacInsideAmpOutputRFLevel_Type.__name__ = "Integer32"
_CacInsideAmpOutputRFLevel_Object = MibScalar
cacInsideAmpOutputRFLevel = _CacInsideAmpOutputRFLevel_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 13, 5),
    _CacInsideAmpOutputRFLevel_Type()
)
cacInsideAmpOutputRFLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacInsideAmpOutputRFLevel.setStatus("mandatory")


class _CacUpStreamControl_Type(Integer32):
    """Custom type cacUpStreamControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_CacUpStreamControl_Type.__name__ = "Integer32"
_CacUpStreamControl_Object = MibScalar
cacUpStreamControl = _CacUpStreamControl_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 13, 6),
    _CacUpStreamControl_Type()
)
cacUpStreamControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cacUpStreamControl.setStatus("mandatory")


class _CacOutputPortNumber_Type(Integer32):
    """Custom type cacOutputPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_CacOutputPortNumber_Type.__name__ = "Integer32"
_CacOutputPortNumber_Object = MibScalar
cacOutputPortNumber = _CacOutputPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 13, 7),
    _CacOutputPortNumber_Type()
)
cacOutputPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacOutputPortNumber.setStatus("mandatory")
_CacPortTable_Object = MibTable
cacPortTable = _CacPortTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 13, 8)
)
if mibBuilder.loadTexts:
    cacPortTable.setStatus("mandatory")
_CacPortTableEntry_Object = MibTableRow
cacPortTableEntry = _CacPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 13, 8, 1)
)
cacPortTableEntry.setIndexNames(
    (0, "NSCRTV-HFCEMS-CONTROLLEDACCESSCONTROLLER-MIB", "cacPortIndex"),
)
if mibBuilder.loadTexts:
    cacPortTableEntry.setStatus("mandatory")


class _CacPortIndex_Type(Integer32):
    """Custom type cacPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_CacPortIndex_Type.__name__ = "Integer32"
_CacPortIndex_Object = MibTableColumn
cacPortIndex = _CacPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 13, 8, 1, 1),
    _CacPortIndex_Type()
)
cacPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacPortIndex.setStatus("mandatory")
_CacPortControl_Type = OctetString
_CacPortControl_Object = MibTableColumn
cacPortControl = _CacPortControl_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 13, 8, 1, 2),
    _CacPortControl_Type()
)
cacPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cacPortControl.setStatus("mandatory")


class _CacPortRFLevel_Type(Integer32):
    """Custom type cacPortRFLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CacPortRFLevel_Type.__name__ = "Integer32"
_CacPortRFLevel_Object = MibTableColumn
cacPortRFLevel = _CacPortRFLevel_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 13, 8, 1, 3),
    _CacPortRFLevel_Type()
)
cacPortRFLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacPortRFLevel.setStatus("optional")


class _CacAllPortsState_Type(OctetString):
    """Custom type cacAllPortsState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CacAllPortsState_Type.__name__ = "OctetString"
_CacAllPortsState_Object = MibScalar
cacAllPortsState = _CacAllPortsState_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 13, 9),
    _CacAllPortsState_Type()
)
cacAllPortsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cacAllPortsState.setStatus("optional")
_CacPortStateReset_Type = Integer32
_CacPortStateReset_Object = MibScalar
cacPortStateReset = _CacPortStateReset_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 13, 10),
    _CacPortStateReset_Type()
)
cacPortStateReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cacPortStateReset.setStatus("optional")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCRTV-HFCEMS-CONTROLLEDACCESSCONTROLLER-MIB",
    **{"cacVendorOID": cacVendorOID,
       "cacPowerType": cacPowerType,
       "cacACPowerVoltage": cacACPowerVoltage,
       "cacMainDCPowerVoltage": cacMainDCPowerVoltage,
       "cacInsideAmpOutputRFLevel": cacInsideAmpOutputRFLevel,
       "cacUpStreamControl": cacUpStreamControl,
       "cacOutputPortNumber": cacOutputPortNumber,
       "cacPortTable": cacPortTable,
       "cacPortTableEntry": cacPortTableEntry,
       "cacPortIndex": cacPortIndex,
       "cacPortControl": cacPortControl,
       "cacPortRFLevel": cacPortRFLevel,
       "cacAllPortsState": cacAllPortsState,
       "cacPortStateReset": cacPortStateReset}
)
