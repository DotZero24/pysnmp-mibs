# SNMP MIB module (BRCM-CABLEDATA-ENGINEERING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/broadcom/BRCM-CABLEDATA-ENGINEERING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:08:20 2025
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

(cableDataPrivateMIBObjects,) = mibBuilder.importSymbols(
    "BRCM-CABLEDATA-PRIVATE-MIB",
    "cableDataPrivateMIBObjects")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cableDataEngineering = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cableDataEngineering.setRevisions(
        ("2007-02-05 00:00",
         "2006-11-17 00:00",
         "2002-06-04 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CableDataEngineeringBase_ObjectIdentity = ObjectIdentity
cableDataEngineeringBase = _CableDataEngineeringBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 1)
)
_CdEngrMemAccessAddress_Type = Unsigned32
_CdEngrMemAccessAddress_Object = MibScalar
cdEngrMemAccessAddress = _CdEngrMemAccessAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 1, 1),
    _CdEngrMemAccessAddress_Type()
)
cdEngrMemAccessAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdEngrMemAccessAddress.setStatus("current")


class _CdEngrMemAccessNumBytes_Type(Unsigned32):
    """Custom type cdEngrMemAccessNumBytes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CdEngrMemAccessNumBytes_Type.__name__ = "Unsigned32"
_CdEngrMemAccessNumBytes_Object = MibScalar
cdEngrMemAccessNumBytes = _CdEngrMemAccessNumBytes_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 1, 2),
    _CdEngrMemAccessNumBytes_Type()
)
cdEngrMemAccessNumBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdEngrMemAccessNumBytes.setStatus("current")
_CdEngrMemAccessData_Type = Unsigned32
_CdEngrMemAccessData_Object = MibScalar
cdEngrMemAccessData = _CdEngrMemAccessData_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 1, 3),
    _CdEngrMemAccessData_Type()
)
cdEngrMemAccessData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdEngrMemAccessData.setStatus("current")


class _CdEngrMemAccessCommand_Type(Integer32):
    """Custom type cdEngrMemAccessCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("read", 0),
          ("write", 1))
    )


_CdEngrMemAccessCommand_Type.__name__ = "Integer32"
_CdEngrMemAccessCommand_Object = MibScalar
cdEngrMemAccessCommand = _CdEngrMemAccessCommand_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 1, 4),
    _CdEngrMemAccessCommand_Type()
)
cdEngrMemAccessCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdEngrMemAccessCommand.setStatus("current")
_CableDataEngineeringEjtag_ObjectIdentity = ObjectIdentity
cableDataEngineeringEjtag = _CableDataEngineeringEjtag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 1, 20)
)
_CdEngrEJTAGTPSelect_Type = Integer32
_CdEngrEJTAGTPSelect_Object = MibScalar
cdEngrEJTAGTPSelect = _CdEngrEJTAGTPSelect_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 1, 20, 1),
    _CdEngrEJTAGTPSelect_Type()
)
cdEngrEJTAGTPSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdEngrEJTAGTPSelect.setStatus("current")
_CdEngrEJTAGDisableAll_Type = TruthValue
_CdEngrEJTAGDisableAll_Object = MibScalar
cdEngrEJTAGDisableAll = _CdEngrEJTAGDisableAll_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 1, 20, 2),
    _CdEngrEJTAGDisableAll_Type()
)
cdEngrEJTAGDisableAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdEngrEJTAGDisableAll.setStatus("current")
_CdEngrEJTAGInstrBrkTable_Object = MibTable
cdEngrEJTAGInstrBrkTable = _CdEngrEJTAGInstrBrkTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 1, 20, 3)
)
if mibBuilder.loadTexts:
    cdEngrEJTAGInstrBrkTable.setStatus("current")
_CdEngrEJTAGInstrBrkEntry_Object = MibTableRow
cdEngrEJTAGInstrBrkEntry = _CdEngrEJTAGInstrBrkEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 1, 20, 3, 1)
)
cdEngrEJTAGInstrBrkEntry.setIndexNames(
    (0, "BRCM-CABLEDATA-ENGINEERING-MIB", "cdEngrEJTAGIBChannel"),
)
if mibBuilder.loadTexts:
    cdEngrEJTAGInstrBrkEntry.setStatus("current")


class _CdEngrEJTAGIBChannel_Type(Integer32):
    """Custom type cdEngrEJTAGIBChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CdEngrEJTAGIBChannel_Type.__name__ = "Integer32"
_CdEngrEJTAGIBChannel_Object = MibTableColumn
cdEngrEJTAGIBChannel = _CdEngrEJTAGIBChannel_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 1, 20, 3, 1, 1),
    _CdEngrEJTAGIBChannel_Type()
)
cdEngrEJTAGIBChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdEngrEJTAGIBChannel.setStatus("current")
_CdEngrEJTAGIBEnabled_Type = TruthValue
_CdEngrEJTAGIBEnabled_Object = MibTableColumn
cdEngrEJTAGIBEnabled = _CdEngrEJTAGIBEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 1, 20, 3, 1, 2),
    _CdEngrEJTAGIBEnabled_Type()
)
cdEngrEJTAGIBEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdEngrEJTAGIBEnabled.setStatus("current")
_CdEngrEJTAGIBAddress_Type = OctetString
_CdEngrEJTAGIBAddress_Object = MibTableColumn
cdEngrEJTAGIBAddress = _CdEngrEJTAGIBAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 1, 20, 3, 1, 3),
    _CdEngrEJTAGIBAddress_Type()
)
cdEngrEJTAGIBAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdEngrEJTAGIBAddress.setStatus("current")
_CdEngrEJTAGIBAddrMask_Type = OctetString
_CdEngrEJTAGIBAddrMask_Object = MibTableColumn
cdEngrEJTAGIBAddrMask = _CdEngrEJTAGIBAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 1, 20, 3, 1, 4),
    _CdEngrEJTAGIBAddrMask_Type()
)
cdEngrEJTAGIBAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdEngrEJTAGIBAddrMask.setStatus("current")
_CdEngrEJTAGIBControl_Type = OctetString
_CdEngrEJTAGIBControl_Object = MibTableColumn
cdEngrEJTAGIBControl = _CdEngrEJTAGIBControl_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 1, 20, 3, 1, 5),
    _CdEngrEJTAGIBControl_Type()
)
cdEngrEJTAGIBControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdEngrEJTAGIBControl.setStatus("current")
_CdEngrEJTAGDataBrkTable_Object = MibTable
cdEngrEJTAGDataBrkTable = _CdEngrEJTAGDataBrkTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 1, 20, 4)
)
if mibBuilder.loadTexts:
    cdEngrEJTAGDataBrkTable.setStatus("current")
_CdEngrEJTAGDataBrkEntry_Object = MibTableRow
cdEngrEJTAGDataBrkEntry = _CdEngrEJTAGDataBrkEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 1, 20, 4, 1)
)
cdEngrEJTAGDataBrkEntry.setIndexNames(
    (0, "BRCM-CABLEDATA-ENGINEERING-MIB", "cdEngrEJTAGDBChannel"),
)
if mibBuilder.loadTexts:
    cdEngrEJTAGDataBrkEntry.setStatus("current")


class _CdEngrEJTAGDBChannel_Type(Integer32):
    """Custom type cdEngrEJTAGDBChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CdEngrEJTAGDBChannel_Type.__name__ = "Integer32"
_CdEngrEJTAGDBChannel_Object = MibTableColumn
cdEngrEJTAGDBChannel = _CdEngrEJTAGDBChannel_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 1, 20, 4, 1, 1),
    _CdEngrEJTAGDBChannel_Type()
)
cdEngrEJTAGDBChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdEngrEJTAGDBChannel.setStatus("current")
_CdEngrEJTAGDBEnabled_Type = TruthValue
_CdEngrEJTAGDBEnabled_Object = MibTableColumn
cdEngrEJTAGDBEnabled = _CdEngrEJTAGDBEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 1, 20, 4, 1, 2),
    _CdEngrEJTAGDBEnabled_Type()
)
cdEngrEJTAGDBEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdEngrEJTAGDBEnabled.setStatus("current")
_CdEngrEJTAGDBAddress_Type = OctetString
_CdEngrEJTAGDBAddress_Object = MibTableColumn
cdEngrEJTAGDBAddress = _CdEngrEJTAGDBAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 1, 20, 4, 1, 3),
    _CdEngrEJTAGDBAddress_Type()
)
cdEngrEJTAGDBAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdEngrEJTAGDBAddress.setStatus("current")
_CdEngrEJTAGDBAddrMask_Type = OctetString
_CdEngrEJTAGDBAddrMask_Object = MibTableColumn
cdEngrEJTAGDBAddrMask = _CdEngrEJTAGDBAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 1, 20, 4, 1, 4),
    _CdEngrEJTAGDBAddrMask_Type()
)
cdEngrEJTAGDBAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdEngrEJTAGDBAddrMask.setStatus("current")
_CdEngrEJTAGDBDataVal_Type = OctetString
_CdEngrEJTAGDBDataVal_Object = MibTableColumn
cdEngrEJTAGDBDataVal = _CdEngrEJTAGDBDataVal_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 1, 20, 4, 1, 5),
    _CdEngrEJTAGDBDataVal_Type()
)
cdEngrEJTAGDBDataVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdEngrEJTAGDBDataVal.setStatus("current")
_CdEngrEJTAGDBDataMask_Type = OctetString
_CdEngrEJTAGDBDataMask_Object = MibTableColumn
cdEngrEJTAGDBDataMask = _CdEngrEJTAGDBDataMask_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 1, 20, 4, 1, 6),
    _CdEngrEJTAGDBDataMask_Type()
)
cdEngrEJTAGDBDataMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdEngrEJTAGDBDataMask.setStatus("current")
_CdEngrEJTAGDBControl_Type = OctetString
_CdEngrEJTAGDBControl_Object = MibTableColumn
cdEngrEJTAGDBControl = _CdEngrEJTAGDBControl_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 1, 20, 4, 1, 7),
    _CdEngrEJTAGDBControl_Type()
)
cdEngrEJTAGDBControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdEngrEJTAGDBControl.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRCM-CABLEDATA-ENGINEERING-MIB",
    **{"cableDataEngineering": cableDataEngineering,
       "cableDataEngineeringBase": cableDataEngineeringBase,
       "cdEngrMemAccessAddress": cdEngrMemAccessAddress,
       "cdEngrMemAccessNumBytes": cdEngrMemAccessNumBytes,
       "cdEngrMemAccessData": cdEngrMemAccessData,
       "cdEngrMemAccessCommand": cdEngrMemAccessCommand,
       "cableDataEngineeringEjtag": cableDataEngineeringEjtag,
       "cdEngrEJTAGTPSelect": cdEngrEJTAGTPSelect,
       "cdEngrEJTAGDisableAll": cdEngrEJTAGDisableAll,
       "cdEngrEJTAGInstrBrkTable": cdEngrEJTAGInstrBrkTable,
       "cdEngrEJTAGInstrBrkEntry": cdEngrEJTAGInstrBrkEntry,
       "cdEngrEJTAGIBChannel": cdEngrEJTAGIBChannel,
       "cdEngrEJTAGIBEnabled": cdEngrEJTAGIBEnabled,
       "cdEngrEJTAGIBAddress": cdEngrEJTAGIBAddress,
       "cdEngrEJTAGIBAddrMask": cdEngrEJTAGIBAddrMask,
       "cdEngrEJTAGIBControl": cdEngrEJTAGIBControl,
       "cdEngrEJTAGDataBrkTable": cdEngrEJTAGDataBrkTable,
       "cdEngrEJTAGDataBrkEntry": cdEngrEJTAGDataBrkEntry,
       "cdEngrEJTAGDBChannel": cdEngrEJTAGDBChannel,
       "cdEngrEJTAGDBEnabled": cdEngrEJTAGDBEnabled,
       "cdEngrEJTAGDBAddress": cdEngrEJTAGDBAddress,
       "cdEngrEJTAGDBAddrMask": cdEngrEJTAGDBAddrMask,
       "cdEngrEJTAGDBDataVal": cdEngrEJTAGDBDataVal,
       "cdEngrEJTAGDBDataMask": cdEngrEJTAGDBDataMask,
       "cdEngrEJTAGDBControl": cdEngrEJTAGDBControl}
)
