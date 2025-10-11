# SNMP MIB module (LUM-FPU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-FPU-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:51 2025
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

(lumFpuMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumFpuMIB",
    "lumModules")

(MgmtNameString,) = mibBuilder.importSymbols(
    "LUM-TC",
    "MgmtNameString")

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

lumFpuMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 66)
)
if mibBuilder.loadTexts:
    lumFpuMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2015-11-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FpuWavelengthBand(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1310,
              1550,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("cwdm1310", 1310),
          ("dwdm1550", 1550),
          ("notApplicable", 2147483647))
    )



# MIB Managed Objects in the order of their OIDs

_LumFpuConfs_ObjectIdentity = ObjectIdentity
lumFpuConfs = _LumFpuConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 66, 1)
)
_LumFpuGroups_ObjectIdentity = ObjectIdentity
lumFpuGroups = _LumFpuGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 66, 1, 1)
)
_LumFpuCompl_ObjectIdentity = ObjectIdentity
lumFpuCompl = _LumFpuCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 66, 1, 2)
)
_LumFpuMIBObjects_ObjectIdentity = ObjectIdentity
lumFpuMIBObjects = _LumFpuMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 66, 2)
)
_FpuGeneral_ObjectIdentity = ObjectIdentity
fpuGeneral = _FpuGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 66, 2, 1)
)
_FpuGeneralConfigLastChangeTime_Type = DateAndTime
_FpuGeneralConfigLastChangeTime_Object = MibScalar
fpuGeneralConfigLastChangeTime = _FpuGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 66, 2, 1, 1),
    _FpuGeneralConfigLastChangeTime_Type()
)
fpuGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpuGeneralConfigLastChangeTime.setStatus("current")
_FpuGeneralStateLastChangeTime_Type = DateAndTime
_FpuGeneralStateLastChangeTime_Object = MibScalar
fpuGeneralStateLastChangeTime = _FpuGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 66, 2, 1, 2),
    _FpuGeneralStateLastChangeTime_Type()
)
fpuGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpuGeneralStateLastChangeTime.setStatus("current")
_FpuGeneralFpuApplicationTableSize_Type = Unsigned32
_FpuGeneralFpuApplicationTableSize_Object = MibScalar
fpuGeneralFpuApplicationTableSize = _FpuGeneralFpuApplicationTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 66, 2, 1, 3),
    _FpuGeneralFpuApplicationTableSize_Type()
)
fpuGeneralFpuApplicationTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpuGeneralFpuApplicationTableSize.setStatus("current")
_FpuGeneralFpuApplicationConfigLastChangeTime_Type = DateAndTime
_FpuGeneralFpuApplicationConfigLastChangeTime_Object = MibScalar
fpuGeneralFpuApplicationConfigLastChangeTime = _FpuGeneralFpuApplicationConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 66, 2, 1, 4),
    _FpuGeneralFpuApplicationConfigLastChangeTime_Type()
)
fpuGeneralFpuApplicationConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpuGeneralFpuApplicationConfigLastChangeTime.setStatus("current")
_FpuGeneralFpuApplicationStateLastChangeTime_Type = DateAndTime
_FpuGeneralFpuApplicationStateLastChangeTime_Object = MibScalar
fpuGeneralFpuApplicationStateLastChangeTime = _FpuGeneralFpuApplicationStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 66, 2, 1, 5),
    _FpuGeneralFpuApplicationStateLastChangeTime_Type()
)
fpuGeneralFpuApplicationStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpuGeneralFpuApplicationStateLastChangeTime.setStatus("current")
_FpuApplicationList_ObjectIdentity = ObjectIdentity
fpuApplicationList = _FpuApplicationList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 66, 2, 2)
)
_FpuApplicationTable_Object = MibTable
fpuApplicationTable = _FpuApplicationTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 66, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fpuApplicationTable.setStatus("current")
_FpuApplicationEntry_Object = MibTableRow
fpuApplicationEntry = _FpuApplicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 66, 2, 2, 1, 1)
)
fpuApplicationEntry.setIndexNames(
    (0, "LUM-FPU-MIB", "fpuApplicationIndex"),
)
if mibBuilder.loadTexts:
    fpuApplicationEntry.setStatus("current")
_FpuApplicationIndex_Type = Unsigned32
_FpuApplicationIndex_Object = MibTableColumn
fpuApplicationIndex = _FpuApplicationIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 66, 2, 2, 1, 1, 1),
    _FpuApplicationIndex_Type()
)
fpuApplicationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpuApplicationIndex.setStatus("current")
_FpuApplicationName_Type = MgmtNameString
_FpuApplicationName_Object = MibTableColumn
fpuApplicationName = _FpuApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 66, 2, 2, 1, 1, 2),
    _FpuApplicationName_Type()
)
fpuApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpuApplicationName.setStatus("current")


class _FpuApplicationWavelengthBand_Type(FpuWavelengthBand):
    """Custom type fpuApplicationWavelengthBand based on FpuWavelengthBand"""
    defaultValue = 1550


_FpuApplicationWavelengthBand_Type.__name__ = "FpuWavelengthBand"
_FpuApplicationWavelengthBand_Object = MibTableColumn
fpuApplicationWavelengthBand = _FpuApplicationWavelengthBand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 66, 2, 2, 1, 1, 3),
    _FpuApplicationWavelengthBand_Type()
)
fpuApplicationWavelengthBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpuApplicationWavelengthBand.setStatus("current")

# Managed Objects groups

fpuGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 66, 1, 1, 1)
)
fpuGeneralGroupV1.setObjects(
      *(("LUM-FPU-MIB", "fpuGeneralConfigLastChangeTime"),
        ("LUM-FPU-MIB", "fpuGeneralStateLastChangeTime"),
        ("LUM-FPU-MIB", "fpuGeneralFpuApplicationTableSize"),
        ("LUM-FPU-MIB", "fpuGeneralFpuApplicationConfigLastChangeTime"),
        ("LUM-FPU-MIB", "fpuGeneralFpuApplicationStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    fpuGeneralGroupV1.setStatus("current")

fpuApplicationGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 66, 1, 1, 2)
)
fpuApplicationGroupV1.setObjects(
      *(("LUM-FPU-MIB", "fpuApplicationIndex"),
        ("LUM-FPU-MIB", "fpuApplicationName"),
        ("LUM-FPU-MIB", "fpuApplicationWavelengthBand"))
)
if mibBuilder.loadTexts:
    fpuApplicationGroupV1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumFpuComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 66, 1, 2, 1)
)
lumFpuComplV1.setObjects(
      *(("LUM-FPU-MIB", "fpuGeneralGroupV1"),
        ("LUM-FPU-MIB", "fpuApplicationGroupV1"))
)
if mibBuilder.loadTexts:
    lumFpuComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-FPU-MIB",
    **{"FpuWavelengthBand": FpuWavelengthBand,
       "lumFpuMIBModule": lumFpuMIBModule,
       "lumFpuConfs": lumFpuConfs,
       "lumFpuGroups": lumFpuGroups,
       "fpuGeneralGroupV1": fpuGeneralGroupV1,
       "fpuApplicationGroupV1": fpuApplicationGroupV1,
       "lumFpuCompl": lumFpuCompl,
       "lumFpuComplV1": lumFpuComplV1,
       "lumFpuMIBObjects": lumFpuMIBObjects,
       "fpuGeneral": fpuGeneral,
       "fpuGeneralConfigLastChangeTime": fpuGeneralConfigLastChangeTime,
       "fpuGeneralStateLastChangeTime": fpuGeneralStateLastChangeTime,
       "fpuGeneralFpuApplicationTableSize": fpuGeneralFpuApplicationTableSize,
       "fpuGeneralFpuApplicationConfigLastChangeTime": fpuGeneralFpuApplicationConfigLastChangeTime,
       "fpuGeneralFpuApplicationStateLastChangeTime": fpuGeneralFpuApplicationStateLastChangeTime,
       "fpuApplicationList": fpuApplicationList,
       "fpuApplicationTable": fpuApplicationTable,
       "fpuApplicationEntry": fpuApplicationEntry,
       "fpuApplicationIndex": fpuApplicationIndex,
       "fpuApplicationName": fpuApplicationName,
       "fpuApplicationWavelengthBand": fpuApplicationWavelengthBand}
)
