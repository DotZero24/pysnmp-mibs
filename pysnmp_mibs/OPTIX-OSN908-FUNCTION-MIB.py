# SNMP MIB module (OPTIX-OSN908-FUNCTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/huawei/OPTIX-OSN908-FUNCTION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:24:38 2025
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

(optixProvisionWDM,) = mibBuilder.importSymbols(
    "OPTIX-OID-MIB",
    "optixProvisionWDM")

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

_OptixWDMFunction_ObjectIdentity = ObjectIdentity
optixWDMFunction = _OptixWDMFunction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 70, 10)
)
_OptixWDMBdinfo_ObjectIdentity = ObjectIdentity
optixWDMBdinfo = _OptixWDMBdinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 70, 10, 20)
)
_OptixWDMGetBdInfoTable_Object = MibTable
optixWDMGetBdInfoTable = _OptixWDMGetBdInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 70, 10, 20, 10)
)
if mibBuilder.loadTexts:
    optixWDMGetBdInfoTable.setStatus("current")
_OptixWDMGetBdInfoEntry_Object = MibTableRow
optixWDMGetBdInfoEntry = _OptixWDMGetBdInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 70, 10, 20, 10, 1)
)
optixWDMGetBdInfoEntry.setIndexNames(
    (0, "OPTIX-OSN908-FUNCTION-MIB", "optixWDMGetBdInfoBID"),
)
if mibBuilder.loadTexts:
    optixWDMGetBdInfoEntry.setStatus("current")


class _OptixWDMGetBdInfoBID_Type(OctetString):
    """Custom type optixWDMGetBdInfoBID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OptixWDMGetBdInfoBID_Type.__name__ = "OctetString"
_OptixWDMGetBdInfoBID_Object = MibTableColumn
optixWDMGetBdInfoBID = _OptixWDMGetBdInfoBID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 70, 10, 20, 10, 1, 1),
    _OptixWDMGetBdInfoBID_Type()
)
optixWDMGetBdInfoBID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optixWDMGetBdInfoBID.setStatus("current")


class _OptixWDMGetBdInfoData_Type(OctetString):
    """Custom type optixWDMGetBdInfoData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4620),
    )


_OptixWDMGetBdInfoData_Type.__name__ = "OctetString"
_OptixWDMGetBdInfoData_Object = MibTableColumn
optixWDMGetBdInfoData = _OptixWDMGetBdInfoData_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 70, 10, 20, 10, 1, 2),
    _OptixWDMGetBdInfoData_Type()
)
optixWDMGetBdInfoData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optixWDMGetBdInfoData.setStatus("current")
_OptixWDMDeviceMgr_ObjectIdentity = ObjectIdentity
optixWDMDeviceMgr = _OptixWDMDeviceMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 70, 20)
)
_OptixWDMFanMgr_ObjectIdentity = ObjectIdentity
optixWDMFanMgr = _OptixWDMFanMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 70, 20, 10)
)
_OptixWDMFanTable_Object = MibTable
optixWDMFanTable = _OptixWDMFanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 70, 20, 10, 10)
)
if mibBuilder.loadTexts:
    optixWDMFanTable.setStatus("current")
_OptixWDMFanEntry_Object = MibTableRow
optixWDMFanEntry = _OptixWDMFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 70, 20, 10, 10, 1)
)
optixWDMFanEntry.setIndexNames(
    (0, "OPTIX-OSN908-FUNCTION-MIB", "optixWDMGetFanBID"),
)
if mibBuilder.loadTexts:
    optixWDMFanEntry.setStatus("current")


class _OptixWDMGetFanBID_Type(Integer32):
    """Custom type optixWDMGetFanBID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OptixWDMGetFanBID_Type.__name__ = "Integer32"
_OptixWDMGetFanBID_Object = MibTableColumn
optixWDMGetFanBID = _OptixWDMGetFanBID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 70, 20, 10, 10, 1, 1),
    _OptixWDMGetFanBID_Type()
)
optixWDMGetFanBID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optixWDMGetFanBID.setStatus("current")


class _OptixWDMGetFanSpeed_Type(Integer32):
    """Custom type optixWDMGetFanSpeed based on Integer32"""
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
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("mid", 2),
          ("high", 3),
          ("stop", 4),
          ("auto-low", 5),
          ("auto-mid", 6),
          ("auto-high", 7),
          ("auto", 9),
          ("mid-low", 10),
          ("mid-high", 11))
    )


_OptixWDMGetFanSpeed_Type.__name__ = "Integer32"
_OptixWDMGetFanSpeed_Object = MibTableColumn
optixWDMGetFanSpeed = _OptixWDMGetFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 70, 20, 10, 10, 1, 2),
    _OptixWDMGetFanSpeed_Type()
)
optixWDMGetFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optixWDMGetFanSpeed.setStatus("current")
_OptixWDMPsuMgr_ObjectIdentity = ObjectIdentity
optixWDMPsuMgr = _OptixWDMPsuMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 70, 20, 20)
)
_OptixWDMPsuTable_Object = MibTable
optixWDMPsuTable = _OptixWDMPsuTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 70, 20, 20, 10)
)
if mibBuilder.loadTexts:
    optixWDMPsuTable.setStatus("current")
_OptixWDMPsuEntry_Object = MibTableRow
optixWDMPsuEntry = _OptixWDMPsuEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 70, 20, 20, 10, 1)
)
optixWDMPsuEntry.setIndexNames(
    (0, "OPTIX-OSN908-FUNCTION-MIB", "optixWDMGetPsuBID"),
)
if mibBuilder.loadTexts:
    optixWDMPsuEntry.setStatus("current")


class _OptixWDMGetPsuBID_Type(Integer32):
    """Custom type optixWDMGetPsuBID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OptixWDMGetPsuBID_Type.__name__ = "Integer32"
_OptixWDMGetPsuBID_Object = MibTableColumn
optixWDMGetPsuBID = _OptixWDMGetPsuBID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 70, 20, 20, 10, 1, 1),
    _OptixWDMGetPsuBID_Type()
)
optixWDMGetPsuBID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optixWDMGetPsuBID.setStatus("current")


class _OptixWDMGetPsuPowerConsumption_Type(Integer32):
    """Custom type optixWDMGetPsuPowerConsumption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OptixWDMGetPsuPowerConsumption_Type.__name__ = "Integer32"
_OptixWDMGetPsuPowerConsumption_Object = MibTableColumn
optixWDMGetPsuPowerConsumption = _OptixWDMGetPsuPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 70, 20, 20, 10, 1, 2),
    _OptixWDMGetPsuPowerConsumption_Type()
)
optixWDMGetPsuPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optixWDMGetPsuPowerConsumption.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPTIX-OSN908-FUNCTION-MIB",
    **{"optixWDMFunction": optixWDMFunction,
       "optixWDMBdinfo": optixWDMBdinfo,
       "optixWDMGetBdInfoTable": optixWDMGetBdInfoTable,
       "optixWDMGetBdInfoEntry": optixWDMGetBdInfoEntry,
       "optixWDMGetBdInfoBID": optixWDMGetBdInfoBID,
       "optixWDMGetBdInfoData": optixWDMGetBdInfoData,
       "optixWDMDeviceMgr": optixWDMDeviceMgr,
       "optixWDMFanMgr": optixWDMFanMgr,
       "optixWDMFanTable": optixWDMFanTable,
       "optixWDMFanEntry": optixWDMFanEntry,
       "optixWDMGetFanBID": optixWDMGetFanBID,
       "optixWDMGetFanSpeed": optixWDMGetFanSpeed,
       "optixWDMPsuMgr": optixWDMPsuMgr,
       "optixWDMPsuTable": optixWDMPsuTable,
       "optixWDMPsuEntry": optixWDMPsuEntry,
       "optixWDMGetPsuBID": optixWDMGetPsuBID,
       "optixWDMGetPsuPowerConsumption": optixWDMGetPsuPowerConsumption}
)
