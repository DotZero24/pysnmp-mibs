# SNMP MIB module (OPTIX-GLOBAL-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/huawei/OPTIX-GLOBAL-TRAPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:30:14 2025
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
 DataPmEventType,
 ObjType,
 PerformanceEventType,
 ValidflagType) = mibBuilder.importSymbols(
    "OPTIX-GLOBAL-TC-MIB",
    "AlarmEventType",
    "AlmDataNtfcnCdeType",
    "AlmDataSrvEffType",
    "DataPmEventType",
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

optixGlobalTrap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40)
)
if mibBuilder.loadTexts:
    optixGlobalTrap.setRevisions(
        ("2008-05-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OptixTrapsCommon_ObjectIdentity = ObjectIdentity
optixTrapsCommon = _OptixTrapsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 10)
)
_RptAlmName_Type = AlarmEventType
_RptAlmName_Object = MibScalar
rptAlmName = _RptAlmName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 10, 10),
    _RptAlmName_Type()
)
rptAlmName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptAlmName.setStatus("current")
_RptEvtDateTime_Type = DateAndTime
_RptEvtDateTime_Object = MibScalar
rptEvtDateTime = _RptEvtDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 10, 40),
    _RptEvtDateTime_Type()
)
rptEvtDateTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtDateTime.setStatus("current")
_RptEvtSrvEff_Type = AlmDataSrvEffType
_RptEvtSrvEff_Object = MibScalar
rptEvtSrvEff = _RptEvtSrvEff_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 10, 50),
    _RptEvtSrvEff_Type()
)
rptEvtSrvEff.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtSrvEff.setStatus("current")
_RptEvtNtfcnCde_Type = AlmDataNtfcnCdeType
_RptEvtNtfcnCde_Object = MibScalar
rptEvtNtfcnCde = _RptEvtNtfcnCde_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 10, 60),
    _RptEvtNtfcnCde_Type()
)
rptEvtNtfcnCde.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtNtfcnCde.setStatus("current")
_RptEvtMonValue_Type = Counter64
_RptEvtMonValue_Object = MibScalar
rptEvtMonValue = _RptEvtMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 10, 90),
    _RptEvtMonValue_Type()
)
rptEvtMonValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtMonValue.setStatus("current")
_RptEvtThValue_Type = Counter64
_RptEvtThValue_Object = MibScalar
rptEvtThValue = _RptEvtThValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 10, 100),
    _RptEvtThValue_Type()
)
rptEvtThValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtThValue.setStatus("current")
_RptEvtNumber_Type = Unsigned32
_RptEvtNumber_Object = MibScalar
rptEvtNumber = _RptEvtNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 10, 120),
    _RptEvtNumber_Type()
)
rptEvtNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtNumber.setStatus("current")


class _RptEvtPeriod_Type(Integer32):
    """Custom type rptEvtPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("period15m", 1),
          ("period1day", 2))
    )


_RptEvtPeriod_Type.__name__ = "Integer32"
_RptEvtPeriod_Object = MibScalar
rptEvtPeriod = _RptEvtPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 10, 130),
    _RptEvtPeriod_Type()
)
rptEvtPeriod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtPeriod.setStatus("current")
_RptEvtVldty_Type = ValidflagType
_RptEvtVldty_Object = MibScalar
rptEvtVldty = _RptEvtVldty_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 10, 140),
    _RptEvtVldty_Type()
)
rptEvtVldty.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtVldty.setStatus("current")


class _RptEvtState_Type(Integer32):
    """Custom type rptEvtState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("clear", 3))
    )


_RptEvtState_Type.__name__ = "Integer32"
_RptEvtState_Object = MibScalar
rptEvtState = _RptEvtState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 10, 160),
    _RptEvtState_Type()
)
rptEvtState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtState.setStatus("current")
_RptPmName_Type = PerformanceEventType
_RptPmName_Object = MibScalar
rptPmName = _RptPmName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 10, 190),
    _RptPmName_Type()
)
rptPmName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptPmName.setStatus("current")
_RptEvtValue_Type = DisplayString
_RptEvtValue_Object = MibScalar
rptEvtValue = _RptEvtValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 10, 210),
    _RptEvtValue_Type()
)
rptEvtValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtValue.setStatus("current")
_RptEvtObjType_Type = ObjType
_RptEvtObjType_Object = MibScalar
rptEvtObjType = _RptEvtObjType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 10, 220),
    _RptEvtObjType_Type()
)
rptEvtObjType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtObjType.setStatus("current")
_RptEvtParaLen_Type = Counter32
_RptEvtParaLen_Object = MibScalar
rptEvtParaLen = _RptEvtParaLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 10, 230),
    _RptEvtParaLen_Type()
)
rptEvtParaLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtParaLen.setStatus("current")
_RptEvtPara_Type = DisplayString
_RptEvtPara_Object = MibScalar
rptEvtPara = _RptEvtPara_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 10, 240),
    _RptEvtPara_Type()
)
rptEvtPara.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtPara.setStatus("current")
_RptEvtStartTime_Type = DateAndTime
_RptEvtStartTime_Object = MibScalar
rptEvtStartTime = _RptEvtStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 10, 250),
    _RptEvtStartTime_Type()
)
rptEvtStartTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtStartTime.setStatus("current")
_RptEvtEndTime_Type = DateAndTime
_RptEvtEndTime_Object = MibScalar
rptEvtEndTime = _RptEvtEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 10, 260),
    _RptEvtEndTime_Type()
)
rptEvtEndTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtEndTime.setStatus("current")
_RptEvtDataPmName_Type = DataPmEventType
_RptEvtDataPmName_Object = MibScalar
rptEvtDataPmName = _RptEvtDataPmName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 10, 270),
    _RptEvtDataPmName_Type()
)
rptEvtDataPmName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtDataPmName.setStatus("current")
_OptixTrapsPM_ObjectIdentity = ObjectIdentity
optixTrapsPM = _OptixTrapsPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 20)
)
_OptixTrapsTrPer_ObjectIdentity = ObjectIdentity
optixTrapsTrPer = _OptixTrapsTrPer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 40, 50)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPTIX-GLOBAL-TRAPS-MIB",
    **{"optixGlobalTrap": optixGlobalTrap,
       "optixTrapsCommon": optixTrapsCommon,
       "rptAlmName": rptAlmName,
       "rptEvtDateTime": rptEvtDateTime,
       "rptEvtSrvEff": rptEvtSrvEff,
       "rptEvtNtfcnCde": rptEvtNtfcnCde,
       "rptEvtMonValue": rptEvtMonValue,
       "rptEvtThValue": rptEvtThValue,
       "rptEvtNumber": rptEvtNumber,
       "rptEvtPeriod": rptEvtPeriod,
       "rptEvtVldty": rptEvtVldty,
       "rptEvtState": rptEvtState,
       "rptPmName": rptPmName,
       "rptEvtValue": rptEvtValue,
       "rptEvtObjType": rptEvtObjType,
       "rptEvtParaLen": rptEvtParaLen,
       "rptEvtPara": rptEvtPara,
       "rptEvtStartTime": rptEvtStartTime,
       "rptEvtEndTime": rptEvtEndTime,
       "rptEvtDataPmName": rptEvtDataPmName,
       "optixTrapsPM": optixTrapsPM,
       "optixTrapsTrPer": optixTrapsTrPer}
)
