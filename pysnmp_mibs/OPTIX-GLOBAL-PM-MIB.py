# SNMP MIB module (OPTIX-GLOBAL-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/huawei/OPTIX-GLOBAL-PM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:25:55 2025
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

(AlarmEventType,
 AlmDataNtfcnCdeType,
 AlmDataSrvEffType,
 ObjType,
 PerformanceEventType,
 ValidflagType) = mibBuilder.importSymbols(
    "OPTIX-GLOBAL-TC-MIB",
    "AlarmEventType",
    "AlmDataNtfcnCdeType",
    "AlmDataSrvEffType",
    "ObjType",
    "PerformanceEventType",
    "ValidflagType")

(optixCommonGlobal,) = mibBuilder.importSymbols(
    "OPTIX-OID-MIB",
    "optixCommonGlobal")

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

optixGlobalPM = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 10)
)
if mibBuilder.loadTexts:
    optixGlobalPM.setRevisions(
        ("2008-05-24 00:00",)
    )

optixGlobalPER = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 20)
)
if mibBuilder.loadTexts:
    optixGlobalPER.setRevisions(
        ("2008-05-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PmHistCtr_ObjectIdentity = ObjectIdentity
pmHistCtr = _PmHistCtr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 10, 10)
)
_PmHistCtrTable_Object = MibTable
pmHistCtrTable = _PmHistCtrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 10, 10, 10)
)
if mibBuilder.loadTexts:
    pmHistCtrTable.setStatus("current")
_PmHistCtrEntry_Object = MibTableRow
pmHistCtrEntry = _PmHistCtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 10, 10, 10, 1)
)
pmHistCtrEntry.setIndexNames(
    (0, "OPTIX-GLOBAL-PM-MIB", "pmHistCtrPeriod"),
)
if mibBuilder.loadTexts:
    pmHistCtrEntry.setStatus("current")


class _PmHistCtrPeriod_Type(Integer32):
    """Custom type pmHistCtrPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("period30s", 17),
          ("period30m", 18),
          ("periodPrdvar", 19),
          ("periodPrdvar2", 20))
    )


_PmHistCtrPeriod_Type.__name__ = "Integer32"
_PmHistCtrPeriod_Object = MibTableColumn
pmHistCtrPeriod = _PmHistCtrPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 10, 10, 10, 1, 1),
    _PmHistCtrPeriod_Type()
)
pmHistCtrPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmHistCtrPeriod.setStatus("current")
_PmHistCtrRecNum_Type = Integer32
_PmHistCtrRecNum_Object = MibTableColumn
pmHistCtrRecNum = _PmHistCtrRecNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 10, 10, 10, 1, 2),
    _PmHistCtrRecNum_Type()
)
pmHistCtrRecNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmHistCtrRecNum.setStatus("current")
_PmHistCtrInterval_Type = Integer32
_PmHistCtrInterval_Object = MibTableColumn
pmHistCtrInterval = _PmHistCtrInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 10, 10, 10, 1, 3),
    _PmHistCtrInterval_Type()
)
pmHistCtrInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmHistCtrInterval.setStatus("current")


class _PmHistCtrEnableFlag_Type(Integer32):
    """Custom type pmHistCtrEnableFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_PmHistCtrEnableFlag_Type.__name__ = "Integer32"
_PmHistCtrEnableFlag_Object = MibTableColumn
pmHistCtrEnableFlag = _PmHistCtrEnableFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 10, 10, 10, 1, 4),
    _PmHistCtrEnableFlag_Type()
)
pmHistCtrEnableFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmHistCtrEnableFlag.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPTIX-GLOBAL-PM-MIB",
    **{"optixGlobalPM": optixGlobalPM,
       "pmHistCtr": pmHistCtr,
       "pmHistCtrTable": pmHistCtrTable,
       "pmHistCtrEntry": pmHistCtrEntry,
       "pmHistCtrPeriod": pmHistCtrPeriod,
       "pmHistCtrRecNum": pmHistCtrRecNum,
       "pmHistCtrInterval": pmHistCtrInterval,
       "pmHistCtrEnableFlag": pmHistCtrEnableFlag,
       "optixGlobalPER": optixGlobalPER}
)
