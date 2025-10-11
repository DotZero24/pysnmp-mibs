# SNMP MIB module (CAMBIUM-NETWORKS-MACSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cambium/CAMBIUM-NETWORKS-MACSEC-MIB
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

cnMacSecMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 24, 10)
)
if mibBuilder.loadTexts:
    cnMacSecMib.setRevisions(
        ("2021-11-28 00:00",
         "2021-06-04 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MacSecViolationMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("protect", 1),
          ("restrict", 2),
          ("shutdown", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CnMacSecPort_ObjectIdentity = ObjectIdentity
cnMacSecPort = _CnMacSecPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 24, 10, 1)
)
_CnMacSecPortTable_Object = MibTable
cnMacSecPortTable = _CnMacSecPortTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1)
)
if mibBuilder.loadTexts:
    cnMacSecPortTable.setStatus("current")
_CnMacSecPortEntry_Object = MibTableRow
cnMacSecPortEntry = _CnMacSecPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1, 1)
)
cnMacSecPortEntry.setIndexNames(
    (0, "CAMBIUM-NETWORKS-MACSEC-MIB", "cnMacSecPortIndex"),
)
if mibBuilder.loadTexts:
    cnMacSecPortEntry.setStatus("current")


class _CnMacSecPortIndex_Type(Integer32):
    """Custom type cnMacSecPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_CnMacSecPortIndex_Type.__name__ = "Integer32"
_CnMacSecPortIndex_Object = MibTableColumn
cnMacSecPortIndex = _CnMacSecPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1, 1, 1),
    _CnMacSecPortIndex_Type()
)
cnMacSecPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnMacSecPortIndex.setStatus("current")


class _CnMacSecPortStatus_Type(Integer32):
    """Custom type cnMacSecPortStatus based on Integer32"""
    defaultValue = 0


_CnMacSecPortStatus_Type.__name__ = "Integer32"
_CnMacSecPortStatus_Object = MibTableColumn
cnMacSecPortStatus = _CnMacSecPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1, 1, 2),
    _CnMacSecPortStatus_Type()
)
cnMacSecPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnMacSecPortStatus.setStatus("current")


class _CnMacSecPortMode_Type(MacSecViolationMode):
    """Custom type cnMacSecPortMode based on MacSecViolationMode"""
    defaultValue = 1


_CnMacSecPortMode_Type.__name__ = "MacSecViolationMode"
_CnMacSecPortMode_Object = MibTableColumn
cnMacSecPortMode = _CnMacSecPortMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1, 1, 3),
    _CnMacSecPortMode_Type()
)
cnMacSecPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnMacSecPortMode.setStatus("current")


class _CnMacSecPortMaxAddr_Type(Integer32):
    """Custom type cnMacSecPortMaxAddr based on Integer32"""
    defaultValue = 1


_CnMacSecPortMaxAddr_Type.__name__ = "Integer32"
_CnMacSecPortMaxAddr_Object = MibTableColumn
cnMacSecPortMaxAddr = _CnMacSecPortMaxAddr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1, 1, 4),
    _CnMacSecPortMaxAddr_Type()
)
cnMacSecPortMaxAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnMacSecPortMaxAddr.setStatus("current")
_CnMacSecPortNumAddr_Type = Integer32
_CnMacSecPortNumAddr_Object = MibTableColumn
cnMacSecPortNumAddr = _CnMacSecPortNumAddr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1, 1, 5),
    _CnMacSecPortNumAddr_Type()
)
cnMacSecPortNumAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMacSecPortNumAddr.setStatus("current")
_CnMacSecPortNumViolations_Type = Gauge32
_CnMacSecPortNumViolations_Object = MibTableColumn
cnMacSecPortNumViolations = _CnMacSecPortNumViolations_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1, 1, 6),
    _CnMacSecPortNumViolations_Type()
)
cnMacSecPortNumViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMacSecPortNumViolations.setStatus("current")
_CnMacSecPortLastViolationAddr_Type = MacAddress
_CnMacSecPortLastViolationAddr_Object = MibTableColumn
cnMacSecPortLastViolationAddr = _CnMacSecPortLastViolationAddr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1, 1, 7),
    _CnMacSecPortLastViolationAddr_Type()
)
cnMacSecPortLastViolationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMacSecPortLastViolationAddr.setStatus("current")
_CnMacSecPortLastViolationTime_Type = DateAndTime
_CnMacSecPortLastViolationTime_Object = MibTableColumn
cnMacSecPortLastViolationTime = _CnMacSecPortLastViolationTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1, 1, 8),
    _CnMacSecPortLastViolationTime_Type()
)
cnMacSecPortLastViolationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMacSecPortLastViolationTime.setStatus("current")
_CnMacSecGlobalDebug_Type = Integer32
_CnMacSecGlobalDebug_Object = MibScalar
cnMacSecGlobalDebug = _CnMacSecGlobalDebug_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 10, 2),
    _CnMacSecGlobalDebug_Type()
)
cnMacSecGlobalDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnMacSecGlobalDebug.setStatus("current")
_CnMacSecDebugOption_Type = Integer32
_CnMacSecDebugOption_Object = MibScalar
cnMacSecDebugOption = _CnMacSecDebugOption_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 10, 3),
    _CnMacSecDebugOption_Type()
)
cnMacSecDebugOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnMacSecDebugOption.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAMBIUM-NETWORKS-MACSEC-MIB",
    **{"MacSecViolationMode": MacSecViolationMode,
       "cnMacSecMib": cnMacSecMib,
       "cnMacSecPort": cnMacSecPort,
       "cnMacSecPortTable": cnMacSecPortTable,
       "cnMacSecPortEntry": cnMacSecPortEntry,
       "cnMacSecPortIndex": cnMacSecPortIndex,
       "cnMacSecPortStatus": cnMacSecPortStatus,
       "cnMacSecPortMode": cnMacSecPortMode,
       "cnMacSecPortMaxAddr": cnMacSecPortMaxAddr,
       "cnMacSecPortNumAddr": cnMacSecPortNumAddr,
       "cnMacSecPortNumViolations": cnMacSecPortNumViolations,
       "cnMacSecPortLastViolationAddr": cnMacSecPortLastViolationAddr,
       "cnMacSecPortLastViolationTime": cnMacSecPortLastViolationTime,
       "cnMacSecGlobalDebug": cnMacSecGlobalDebug,
       "cnMacSecDebugOption": cnMacSecDebugOption}
)
