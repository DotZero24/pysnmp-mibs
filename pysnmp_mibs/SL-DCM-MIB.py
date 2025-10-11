# SNMP MIB module (SL-DCM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/smartoptics/SL-DCM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:11:12 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(CleiCode,) = mibBuilder.importSymbols(
    "SL-ENTITY-MIB",
    "CleiCode")

(sitelight,) = mibBuilder.importSymbols(
    "SL-NE-MIB",
    "sitelight")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

slDcm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DcmTable_Object = MibTable
dcmTable = _DcmTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 14, 1)
)
if mibBuilder.loadTexts:
    dcmTable.setStatus("current")
_DcmEntry_Object = MibTableRow
dcmEntry = _DcmEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 14, 1, 1)
)
dcmEntry.setIndexNames(
    (0, "SL-DCM-MIB", "dcmIndex"),
)
if mibBuilder.loadTexts:
    dcmEntry.setStatus("current")
_DcmIndex_Type = InterfaceIndex
_DcmIndex_Object = MibTableColumn
dcmIndex = _DcmIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 14, 1, 1, 1),
    _DcmIndex_Type()
)
dcmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcmIndex.setStatus("current")
_DcmRange_Type = Integer32
_DcmRange_Object = MibTableColumn
dcmRange = _DcmRange_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 14, 1, 1, 2),
    _DcmRange_Type()
)
dcmRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmRange.setStatus("current")
_DcmSpacing_Type = Integer32
_DcmSpacing_Object = MibTableColumn
dcmSpacing = _DcmSpacing_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 14, 1, 1, 3),
    _DcmSpacing_Type()
)
dcmSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcmSpacing.setStatus("current")
_DcmTemperature_Type = Integer32
_DcmTemperature_Object = MibTableColumn
dcmTemperature = _DcmTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 14, 1, 1, 4),
    _DcmTemperature_Type()
)
dcmTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcmTemperature.setStatus("current")
_DcmIsActive_Type = TruthValue
_DcmIsActive_Object = MibTableColumn
dcmIsActive = _DcmIsActive_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 14, 1, 1, 5),
    _DcmIsActive_Type()
)
dcmIsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcmIsActive.setStatus("current")
_DcmFiberCoefficient_Type = Integer32
_DcmFiberCoefficient_Object = MibTableColumn
dcmFiberCoefficient = _DcmFiberCoefficient_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 14, 1, 1, 6),
    _DcmFiberCoefficient_Type()
)
dcmFiberCoefficient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcmFiberCoefficient.setStatus("current")
_DcmMinDispersion_Type = Integer32
_DcmMinDispersion_Object = MibTableColumn
dcmMinDispersion = _DcmMinDispersion_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 14, 1, 1, 7),
    _DcmMinDispersion_Type()
)
dcmMinDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcmMinDispersion.setStatus("current")
_DcmMaxDispersion_Type = Integer32
_DcmMaxDispersion_Object = MibTableColumn
dcmMaxDispersion = _DcmMaxDispersion_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 14, 1, 1, 8),
    _DcmMaxDispersion_Type()
)
dcmMaxDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcmMaxDispersion.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-DCM-MIB",
    **{"slDcm": slDcm,
       "dcmTable": dcmTable,
       "dcmEntry": dcmEntry,
       "dcmIndex": dcmIndex,
       "dcmRange": dcmRange,
       "dcmSpacing": dcmSpacing,
       "dcmTemperature": dcmTemperature,
       "dcmIsActive": dcmIsActive,
       "dcmFiberCoefficient": dcmFiberCoefficient,
       "dcmMinDispersion": dcmMinDispersion,
       "dcmMaxDispersion": dcmMaxDispersion}
)
