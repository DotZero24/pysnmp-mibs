# SNMP MIB module (CAMBIUM-NETWORKS-RPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cambium/CAMBIUM-NETWORKS-RPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:07:35 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

cnRPSMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 24, 6)
)
if mibBuilder.loadTexts:
    cnRPSMib.setRevisions(
        ("2022-09-08 20:00",
         "2020-07-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CnRPSTable_Object = MibTable
cnRPSTable = _CnRPSTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 6, 1)
)
if mibBuilder.loadTexts:
    cnRPSTable.setStatus("current")
_CnRPSTableEntry_Object = MibTableRow
cnRPSTableEntry = _CnRPSTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 6, 1, 1)
)
cnRPSTableEntry.setIndexNames(
    (0, "CAMBIUM-NETWORKS-RPS-MIB", "cnRPSIndex"),
)
if mibBuilder.loadTexts:
    cnRPSTableEntry.setStatus("current")


class _CnRPSIndex_Type(Integer32):
    """Custom type cnRPSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CnRPSIndex_Type.__name__ = "Integer32"
_CnRPSIndex_Object = MibTableColumn
cnRPSIndex = _CnRPSIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 6, 1, 1, 1),
    _CnRPSIndex_Type()
)
cnRPSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnRPSIndex.setStatus("current")
_CnRPSMaximumVoltage_Type = Integer32
_CnRPSMaximumVoltage_Object = MibTableColumn
cnRPSMaximumVoltage = _CnRPSMaximumVoltage_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 6, 1, 1, 2),
    _CnRPSMaximumVoltage_Type()
)
cnRPSMaximumVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnRPSMaximumVoltage.setStatus("current")
if mibBuilder.loadTexts:
    cnRPSMaximumVoltage.setUnits("volts")
_CnRPSMaximumCurrent_Type = Integer32
_CnRPSMaximumCurrent_Object = MibTableColumn
cnRPSMaximumCurrent = _CnRPSMaximumCurrent_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 6, 1, 1, 3),
    _CnRPSMaximumCurrent_Type()
)
cnRPSMaximumCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnRPSMaximumCurrent.setStatus("current")
if mibBuilder.loadTexts:
    cnRPSMaximumCurrent.setUnits("amps")
_CnRPSMaximumWatts_Type = Integer32
_CnRPSMaximumWatts_Object = MibTableColumn
cnRPSMaximumWatts = _CnRPSMaximumWatts_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 6, 1, 1, 4),
    _CnRPSMaximumWatts_Type()
)
cnRPSMaximumWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnRPSMaximumWatts.setStatus("current")
if mibBuilder.loadTexts:
    cnRPSMaximumWatts.setUnits("watts")


class _CnRPSStatus_Type(Integer32):
    """Custom type cnRPSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("error", 2),
          ("notpresent", 3))
    )


_CnRPSStatus_Type.__name__ = "Integer32"
_CnRPSStatus_Object = MibTableColumn
cnRPSStatus = _CnRPSStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 6, 1, 1, 5),
    _CnRPSStatus_Type()
)
cnRPSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnRPSStatus.setStatus("current")
_CnRPSCurrentInputVoltage_Type = Integer32
_CnRPSCurrentInputVoltage_Object = MibTableColumn
cnRPSCurrentInputVoltage = _CnRPSCurrentInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 6, 1, 1, 6),
    _CnRPSCurrentInputVoltage_Type()
)
cnRPSCurrentInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnRPSCurrentInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    cnRPSCurrentInputVoltage.setUnits("volts")

# Managed Objects groups


# Notification objects

cnRPSTrapMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 24, 6, 2)
)
cnRPSTrapMsg.setObjects(
      *(("CAMBIUM-NETWORKS-RPS-MIB", "cnRPSMaximumWatts"),
        ("CAMBIUM-NETWORKS-RPS-MIB", "cnRPSStatus"),
        ("CAMBIUM-NETWORKS-RPS-MIB", "cnRPSIndex"))
)
if mibBuilder.loadTexts:
    cnRPSTrapMsg.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAMBIUM-NETWORKS-RPS-MIB",
    **{"cnRPSMib": cnRPSMib,
       "cnRPSTable": cnRPSTable,
       "cnRPSTableEntry": cnRPSTableEntry,
       "cnRPSIndex": cnRPSIndex,
       "cnRPSMaximumVoltage": cnRPSMaximumVoltage,
       "cnRPSMaximumCurrent": cnRPSMaximumCurrent,
       "cnRPSMaximumWatts": cnRPSMaximumWatts,
       "cnRPSStatus": cnRPSStatus,
       "cnRPSCurrentInputVoltage": cnRPSCurrentInputVoltage,
       "cnRPSTrapMsg": cnRPSTrapMsg}
)
