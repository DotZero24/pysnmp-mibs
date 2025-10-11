# SNMP MIB module (BRCM-CM-MGMT-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/broadcom/BRCM-CM-MGMT-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:08:15 2025
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

(broadcomCableDataMgmt,) = mibBuilder.importSymbols(
    "BRCM-CABLEDATA-MGMT-MIB",
    "broadcomCableDataMgmt")

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

cmMgmtExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 99, 4413, 2)
)
if mibBuilder.loadTexts:
    cmMgmtExt.setRevisions(
        ("2007-02-05 00:00",
         "2005-04-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CmMgmtExtBase_ObjectIdentity = ObjectIdentity
cmMgmtExtBase = _CmMgmtExtBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 99, 4413, 2, 1)
)


class _CmMgmtExtBaseStandbySwitchStatus_Type(Integer32):
    """Custom type cmMgmtExtBaseStandbySwitchStatus based on Integer32"""
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


_CmMgmtExtBaseStandbySwitchStatus_Type.__name__ = "Integer32"
_CmMgmtExtBaseStandbySwitchStatus_Object = MibScalar
cmMgmtExtBaseStandbySwitchStatus = _CmMgmtExtBaseStandbySwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 99, 4413, 2, 1, 1),
    _CmMgmtExtBaseStandbySwitchStatus_Type()
)
cmMgmtExtBaseStandbySwitchStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmMgmtExtBaseStandbySwitchStatus.setStatus("current")
_CmMgmtExtScan_ObjectIdentity = ObjectIdentity
cmMgmtExtScan = _CmMgmtExtScan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 99, 4413, 2, 2)
)


class _CmScanPushFrequency_Type(Integer32):
    """Custom type cmScanPushFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CmScanPushFrequency_Type.__name__ = "Integer32"
_CmScanPushFrequency_Object = MibScalar
cmScanPushFrequency = _CmScanPushFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 99, 4413, 2, 2, 1),
    _CmScanPushFrequency_Type()
)
cmScanPushFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmScanPushFrequency.setStatus("current")
_CmScanTable_Object = MibTable
cmScanTable = _CmScanTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 99, 4413, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cmScanTable.setStatus("current")
_CmScanEntry_Object = MibTableRow
cmScanEntry = _CmScanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 99, 4413, 2, 2, 2, 1)
)
cmScanEntry.setIndexNames(
    (0, "BRCM-CM-MGMT-EXT-MIB", "cmScanIndex"),
)
if mibBuilder.loadTexts:
    cmScanEntry.setStatus("current")


class _CmScanIndex_Type(Integer32):
    """Custom type cmScanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CmScanIndex_Type.__name__ = "Integer32"
_CmScanIndex_Object = MibTableColumn
cmScanIndex = _CmScanIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 99, 4413, 2, 2, 2, 1, 1),
    _CmScanIndex_Type()
)
cmScanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmScanIndex.setStatus("current")
_CmScanFrequency_Type = Integer32
_CmScanFrequency_Object = MibTableColumn
cmScanFrequency = _CmScanFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 99, 4413, 2, 2, 2, 1, 2),
    _CmScanFrequency_Type()
)
cmScanFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmScanFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cmScanFrequency.setUnits("hertz")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRCM-CM-MGMT-EXT-MIB",
    **{"cmMgmtExt": cmMgmtExt,
       "cmMgmtExtBase": cmMgmtExtBase,
       "cmMgmtExtBaseStandbySwitchStatus": cmMgmtExtBaseStandbySwitchStatus,
       "cmMgmtExtScan": cmMgmtExtScan,
       "cmScanPushFrequency": cmScanPushFrequency,
       "cmScanTable": cmScanTable,
       "cmScanEntry": cmScanEntry,
       "cmScanIndex": cmScanIndex,
       "cmScanFrequency": cmScanFrequency}
)
