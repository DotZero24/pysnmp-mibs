# SNMP MIB module (ALLOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/allot/ALLOT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:53:58 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "VariablePointer")


# MODULE-IDENTITY

alRegMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2603)
)
if mibBuilder.loadTexts:
    alRegMIB.setRevisions(
        ("2011-11-20 14:00",
         "2011-11-17 17:00",
         "2011-09-21 12:00",
         "2011-09-11 12:00",
         "2011-08-09 11:00",
         "2011-07-24 11:00",
         "2011-07-21 13:00",
         "2011-06-22 11:00",
         "2011-06-21 11:00",
         "2011-06-14 13:00",
         "2011-05-04 16:08",
         "2011-03-22 10:00",
         "2010-11-18 10:00",
         "2009-12-22 13:26",
         "2009-12-01 15:18",
         "2009-10-29 09:48",
         "2009-09-02 13:33",
         "2009-08-12 09:59",
         "2009-02-24 11:35",
         "2007-11-27 15:45",
         "2007-09-23 15:21",
         "2007-08-20 08:33",
         "2007-06-12 15:07",
         "2007-05-14 12:06",
         "2007-02-28 07:27",
         "2006-08-10 08:53",
         "2006-05-31 11:36",
         "2006-05-10 11:50",
         "2006-03-23 10:55",
         "2005-11-14 10:58",
         "2005-08-24 14:59",
         "2005-08-14 12:49",
         "2005-08-14 12:13",
         "2005-07-28 13:52",
         "2005-07-20 16:06",
         "2005-07-20 12:25",
         "2005-07-17 15:02",
         "2005-06-08 14:25",
         "2005-05-04 12:05",
         "2005-04-06 12:08",
         "2005-03-22 12:08",
         "2005-03-10 11:21",
         "2005-03-09 11:50",
         "2005-03-06 12:11",
         "2005-03-01 11:03",
         "2005-02-02 18:59",
         "2005-01-23 13:56",
         "2005-01-04 10:32",
         "2004-12-28 10:46",
         "2004-12-27 12:45",
         "2004-12-27 11:40",
         "2004-12-22 14:02",
         "2004-12-15 14:29",
         "2004-11-14 11:19",
         "2004-10-21 11:56",
         "2004-09-20 15:39",
         "2004-08-24 18:04",
         "2004-08-17 16:57",
         "2004-08-11 16:37",
         "2004-07-25 21:45",
         "2004-05-31 19:38",
         "2004-04-13 22:05")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AlActiveStandbyStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("bypass", 1),
          ("nonBypass", 2),
          ("standBy", 3),
          ("partialBypass", 4))
    )



class AlConfigCommand(TextualConvention, Integer32):
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
        *(("create", 1),
          ("update", 2),
          ("delete", 3))
    )



class AlEnableDisable(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )



class AlEnableDisableNA(TextualConvention, Integer32):
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
        *(("enabled", 1),
          ("disabled", 2),
          ("notAplicable", 3))
    )



class AlInstanceStatus(TextualConvention, Integer32):
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
        *(("active", 1),
          ("disabled", 2),
          ("removed", 3))
    )



class AlUrlOperationMode(TextualConvention, Integer32):
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
        *(("always", 1),
          ("policybased", 2),
          ("disable", 3))
    )



# MIB Managed Objects in the order of their OIDs

_AlEvents_ObjectIdentity = ObjectIdentity
alEvents = _AlEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 0)
)
_AlActivation_ObjectIdentity = ObjectIdentity
alActivation = _AlActivation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 4)
)
_AlActivationKey_Type = DisplayString
_AlActivationKey_Object = MibScalar
alActivationKey = _AlActivationKey_Object(
    (1, 3, 6, 1, 4, 1, 2603, 4, 1),
    _AlActivationKey_Type()
)
alActivationKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alActivationKey.setStatus("current")
_AlActivationModel_Type = DisplayString
_AlActivationModel_Object = MibScalar
alActivationModel = _AlActivationModel_Object(
    (1, 3, 6, 1, 4, 1, 2603, 4, 2),
    _AlActivationModel_Type()
)
alActivationModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActivationModel.setStatus("current")
_AlSysExpirationDate_Type = DateAndTime
_AlSysExpirationDate_Object = MibScalar
alSysExpirationDate = _AlSysExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 2603, 4, 3),
    _AlSysExpirationDate_Type()
)
alSysExpirationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSysExpirationDate.setStatus("current")
_AlQoSIsEnabled_Type = AlEnableDisable
_AlQoSIsEnabled_Object = MibScalar
alQoSIsEnabled = _AlQoSIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2603, 4, 4),
    _AlQoSIsEnabled_Type()
)
alQoSIsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alQoSIsEnabled.setStatus("current")
_AlQoSExpirationDateEnable_Type = AlEnableDisable
_AlQoSExpirationDateEnable_Object = MibScalar
alQoSExpirationDateEnable = _AlQoSExpirationDateEnable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 4, 5),
    _AlQoSExpirationDateEnable_Type()
)
alQoSExpirationDateEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alQoSExpirationDateEnable.setStatus("current")
_AlCacheIsEnabled_Type = AlEnableDisable
_AlCacheIsEnabled_Object = MibScalar
alCacheIsEnabled = _AlCacheIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2603, 4, 6),
    _AlCacheIsEnabled_Type()
)
alCacheIsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCacheIsEnabled.setStatus("current")
_AlCacheExpirationDateEnable_Type = AlEnableDisable
_AlCacheExpirationDateEnable_Object = MibScalar
alCacheExpirationDateEnable = _AlCacheExpirationDateEnable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 4, 7),
    _AlCacheExpirationDateEnable_Type()
)
alCacheExpirationDateEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCacheExpirationDateEnable.setStatus("current")
_AlLoadBalancingIsEnabled_Type = AlEnableDisable
_AlLoadBalancingIsEnabled_Object = MibScalar
alLoadBalancingIsEnabled = _AlLoadBalancingIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2603, 4, 8),
    _AlLoadBalancingIsEnabled_Type()
)
alLoadBalancingIsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLoadBalancingIsEnabled.setStatus("current")
_AlLoadBalancingExpirationDateEnable_Type = AlEnableDisable
_AlLoadBalancingExpirationDateEnable_Object = MibScalar
alLoadBalancingExpirationDateEnable = _AlLoadBalancingExpirationDateEnable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 4, 9),
    _AlLoadBalancingExpirationDateEnable_Type()
)
alLoadBalancingExpirationDateEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLoadBalancingExpirationDateEnable.setStatus("current")
_AlActivationLimits_ObjectIdentity = ObjectIdentity
alActivationLimits = _AlActivationLimits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 4, 10)
)
_AlLinePerPolicy_Type = Unsigned32
_AlLinePerPolicy_Object = MibScalar
alLinePerPolicy = _AlLinePerPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2603, 4, 10, 1),
    _AlLinePerPolicy_Type()
)
alLinePerPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLinePerPolicy.setStatus("current")
_AlPipePerPolicy_Type = Unsigned32
_AlPipePerPolicy_Object = MibScalar
alPipePerPolicy = _AlPipePerPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2603, 4, 10, 2),
    _AlPipePerPolicy_Type()
)
alPipePerPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPipePerPolicy.setStatus("current")
_AlVcPerPolicy_Type = Unsigned32
_AlVcPerPolicy_Object = MibScalar
alVcPerPolicy = _AlVcPerPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2603, 4, 10, 3),
    _AlVcPerPolicy_Type()
)
alVcPerPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVcPerPolicy.setStatus("current")
_AlMaxBandwidth_Type = Counter64
_AlMaxBandwidth_Object = MibScalar
alMaxBandwidth = _AlMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2603, 4, 10, 4),
    _AlMaxBandwidth_Type()
)
alMaxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMaxBandwidth.setStatus("current")
_AlMaxConnections_Type = Unsigned32
_AlMaxConnections_Object = MibScalar
alMaxConnections = _AlMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 2603, 4, 10, 5),
    _AlMaxConnections_Type()
)
alMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMaxConnections.setStatus("current")
_AlLTCollectionEnabled_Type = AlEnableDisable
_AlLTCollectionEnabled_Object = MibScalar
alLTCollectionEnabled = _AlLTCollectionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2603, 4, 11),
    _AlLTCollectionEnabled_Type()
)
alLTCollectionEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLTCollectionEnabled.setStatus("current")
_AlWebUpdateIsEnabled_Type = AlEnableDisable
_AlWebUpdateIsEnabled_Object = MibScalar
alWebUpdateIsEnabled = _AlWebUpdateIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2603, 4, 12),
    _AlWebUpdateIsEnabled_Type()
)
alWebUpdateIsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alWebUpdateIsEnabled.setStatus("current")
_AlWebUpdateExpirationDateEnable_Type = AlEnableDisable
_AlWebUpdateExpirationDateEnable_Object = MibScalar
alWebUpdateExpirationDateEnable = _AlWebUpdateExpirationDateEnable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 4, 13),
    _AlWebUpdateExpirationDateEnable_Type()
)
alWebUpdateExpirationDateEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alWebUpdateExpirationDateEnable.setStatus("current")
_AlLicenseInfoTable_Object = MibTable
alLicenseInfoTable = _AlLicenseInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 4, 14)
)
if mibBuilder.loadTexts:
    alLicenseInfoTable.setStatus("current")
_AlLicenseInfoEntry_Object = MibTableRow
alLicenseInfoEntry = _AlLicenseInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2603, 4, 14, 1)
)
alLicenseInfoEntry.setIndexNames(
    (0, "ALLOT-MIB", "alLicenseAttrType"),
    (0, "ALLOT-MIB", "alLicenseLimitType"),
)
if mibBuilder.loadTexts:
    alLicenseInfoEntry.setStatus("current")


class _AlLicenseAttrType_Type(Integer32):
    """Custom type alLicenseAttrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111)
        )
    )
    namedValues = NamedValues(
        *(("global", 0),
          ("qos", 1),
          ("rtReportMode", 2),
          ("ltReportMode", 3),
          ("vcNumber", 4),
          ("pipeNumber", 5),
          ("lineNumber", 6),
          ("apu", 7),
          ("websafeEnforce", 8),
          ("websafeUpdate", 9),
          ("trafficSteering", 10),
          ("spMitigation", 11),
          ("mediaSwift", 12),
          ("spSensor", 13),
          ("mobileReports", 14),
          ("statExport", 15),
          ("tethering", 16),
          ("numOfSupportedDevices", 101),
          ("npp", 102),
          ("countryClassificationSubscr", 103),
          ("netAccounting", 104),
          ("nmsApu", 105),
          ("tieredServices", 106),
          ("tieredServicesGx", 107),
          ("quotaManagement", 108),
          ("volumeReporting", 109),
          ("onlineCharging", 110),
          ("offlineCharging", 111))
    )


_AlLicenseAttrType_Type.__name__ = "Integer32"
_AlLicenseAttrType_Object = MibTableColumn
alLicenseAttrType = _AlLicenseAttrType_Object(
    (1, 3, 6, 1, 4, 1, 2603, 4, 14, 1, 1),
    _AlLicenseAttrType_Type()
)
alLicenseAttrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLicenseAttrType.setStatus("current")


class _AlLicenseLimitType_Type(Integer32):
    """Custom type alLicenseLimitType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("featureState", 1),
          ("noOfSgcc", 2),
          ("bandwidth", 3),
          ("numberOfActiveElements", 4),
          ("numberOfSubscribers", 5),
          ("expirationDate", 6),
          ("activeSubscribersIp", 7),
          ("activeSubscribers", 8))
    )


_AlLicenseLimitType_Type.__name__ = "Integer32"
_AlLicenseLimitType_Object = MibTableColumn
alLicenseLimitType = _AlLicenseLimitType_Object(
    (1, 3, 6, 1, 4, 1, 2603, 4, 14, 1, 2),
    _AlLicenseLimitType_Type()
)
alLicenseLimitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLicenseLimitType.setStatus("current")
_AlLicenseAttrName_Type = DisplayString
_AlLicenseAttrName_Object = MibTableColumn
alLicenseAttrName = _AlLicenseAttrName_Object(
    (1, 3, 6, 1, 4, 1, 2603, 4, 14, 1, 3),
    _AlLicenseAttrName_Type()
)
alLicenseAttrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLicenseAttrName.setStatus("current")
_AlLimitValue_Type = Counter64
_AlLimitValue_Object = MibTableColumn
alLimitValue = _AlLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 2603, 4, 14, 1, 4),
    _AlLimitValue_Type()
)
alLimitValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLimitValue.setStatus("current")


class _AlLicenseStatus_Type(Integer32):
    """Custom type alLicenseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("licenseValid", 1),
          ("licenseExpired", 2),
          ("licenseAbsence", 3),
          ("licenseInvalid", 4))
    )


_AlLicenseStatus_Type.__name__ = "Integer32"
_AlLicenseStatus_Object = MibTableColumn
alLicenseStatus = _AlLicenseStatus_Object(
    (1, 3, 6, 1, 4, 1, 2603, 4, 14, 1, 5),
    _AlLicenseStatus_Type()
)
alLicenseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLicenseStatus.setStatus("current")
_AlLicenseIsCurrValue_Type = AlEnableDisable
_AlLicenseIsCurrValue_Object = MibTableColumn
alLicenseIsCurrValue = _AlLicenseIsCurrValue_Object(
    (1, 3, 6, 1, 4, 1, 2603, 4, 14, 1, 6),
    _AlLicenseIsCurrValue_Type()
)
alLicenseIsCurrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLicenseIsCurrValue.setStatus("current")
_AlLicenseCurrValue_Type = Counter64
_AlLicenseCurrValue_Object = MibTableColumn
alLicenseCurrValue = _AlLicenseCurrValue_Object(
    (1, 3, 6, 1, 4, 1, 2603, 4, 14, 1, 7),
    _AlLicenseCurrValue_Type()
)
alLicenseCurrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLicenseCurrValue.setStatus("current")


class _AlLicenseEventType_Type(Integer32):
    """Custom type alLicenseEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("noLicense", 1),
          ("licenseExpired", 2),
          ("licenseExprWarn", 3),
          ("invalidLicense", 4),
          ("licenseLimitBreachWarn", 5),
          ("licenseLimitBreachSet", 6),
          ("licenseLimitBreachUnSet", 7))
    )


_AlLicenseEventType_Type.__name__ = "Integer32"
_AlLicenseEventType_Object = MibScalar
alLicenseEventType = _AlLicenseEventType_Object(
    (1, 3, 6, 1, 4, 1, 2603, 4, 15),
    _AlLicenseEventType_Type()
)
alLicenseEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLicenseEventType.setStatus("current")
_AlObjects_ObjectIdentity = ObjectIdentity
alObjects = _AlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5)
)
_AlProducts_ObjectIdentity = ObjectIdentity
alProducts = _AlProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 1)
)
_AlAC200_ObjectIdentity = ObjectIdentity
alAC200 = _AlAC200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 1, 1)
)
if mibBuilder.loadTexts:
    alAC200.setStatus("current")
_AlAC400_ObjectIdentity = ObjectIdentity
alAC400 = _AlAC400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 1, 2)
)
if mibBuilder.loadTexts:
    alAC400.setStatus("current")
_AlAC800_ObjectIdentity = ObjectIdentity
alAC800 = _AlAC800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 1, 3)
)
if mibBuilder.loadTexts:
    alAC800.setStatus("current")
_AlAC1000_ObjectIdentity = ObjectIdentity
alAC1000 = _AlAC1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 1, 4)
)
if mibBuilder.loadTexts:
    alAC1000.setStatus("current")
_AlAC2500_ObjectIdentity = ObjectIdentity
alAC2500 = _AlAC2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 1, 5)
)
if mibBuilder.loadTexts:
    alAC2500.setStatus("current")
_AlMediationDevice_ObjectIdentity = ObjectIdentity
alMediationDevice = _AlMediationDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 1, 6)
)
if mibBuilder.loadTexts:
    alMediationDevice.setStatus("current")
_AlSG20_ObjectIdentity = ObjectIdentity
alSG20 = _AlSG20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 1, 7)
)
if mibBuilder.loadTexts:
    alSG20.setStatus("current")
_AlAC10000_ObjectIdentity = ObjectIdentity
alAC10000 = _AlAC10000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 1, 8)
)
if mibBuilder.loadTexts:
    alAC10000.setStatus("current")
_AlACSigma_ObjectIdentity = ObjectIdentity
alACSigma = _AlACSigma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 1, 9)
)
if mibBuilder.loadTexts:
    alACSigma.setStatus("current")
_AlAC5K_ObjectIdentity = ObjectIdentity
alAC5K = _AlAC5K_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 1, 10)
)
if mibBuilder.loadTexts:
    alAC5K.setStatus("current")
_AlAC3K_ObjectIdentity = ObjectIdentity
alAC3K = _AlAC3K_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 1, 11)
)
if mibBuilder.loadTexts:
    alAC3K.setStatus("current")
_AlAC10K_ObjectIdentity = ObjectIdentity
alAC10K = _AlAC10K_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 1, 12)
)
if mibBuilder.loadTexts:
    alAC10K.setStatus("current")
_AlAC1K_ObjectIdentity = ObjectIdentity
alAC1K = _AlAC1K_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 1, 13)
)
if mibBuilder.loadTexts:
    alAC1K.setStatus("current")
_AlACSigmaE14_ObjectIdentity = ObjectIdentity
alACSigmaE14 = _AlACSigmaE14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 1, 14)
)
if mibBuilder.loadTexts:
    alACSigmaE14.setStatus("current")
_AlAC500_ObjectIdentity = ObjectIdentity
alAC500 = _AlAC500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 1, 15)
)
if mibBuilder.loadTexts:
    alAC500.setStatus("current")
_AlACSigmaE6_ObjectIdentity = ObjectIdentity
alACSigmaE6 = _AlACSigmaE6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 1, 16)
)
if mibBuilder.loadTexts:
    alACSigmaE6.setStatus("current")
_AlGeneric_ObjectIdentity = ObjectIdentity
alGeneric = _AlGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2)
)
_AlConfigurationName_Type = DisplayString
_AlConfigurationName_Object = MibScalar
alConfigurationName = _AlConfigurationName_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 1),
    _AlConfigurationName_Type()
)
alConfigurationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alConfigurationName.setStatus("current")
_AlDoubleSession_Type = AlEnableDisableNA
_AlDoubleSession_Object = MibScalar
alDoubleSession = _AlDoubleSession_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 3),
    _AlDoubleSession_Type()
)
alDoubleSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alDoubleSession.setStatus("current")
_AlGeneralSystem_ObjectIdentity = ObjectIdentity
alGeneralSystem = _AlGeneralSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6)
)
_AlDateTime_Type = DateAndTime
_AlDateTime_Object = MibScalar
alDateTime = _AlDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 1),
    _AlDateTime_Type()
)
alDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alDateTime.setStatus("current")
_AlTimeZone_Type = DisplayString
_AlTimeZone_Object = MibScalar
alTimeZone = _AlTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 2),
    _AlTimeZone_Type()
)
alTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alTimeZone.setStatus("current")
_AlIfXTable_Object = MibTable
alIfXTable = _AlIfXTable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 3)
)
if mibBuilder.loadTexts:
    alIfXTable.setStatus("current")
_AlIfXEntry_Object = MibTableRow
alIfXEntry = _AlIfXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 3, 1)
)
alIfXEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    alIfXEntry.setStatus("current")


class _AlIfXMode_Type(Integer32):
    """Custom type alIfXMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("fullDuplex", 2),
          ("halfDuplex", 3))
    )


_AlIfXMode_Type.__name__ = "Integer32"
_AlIfXMode_Object = MibTableColumn
alIfXMode = _AlIfXMode_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 3, 1, 1),
    _AlIfXMode_Type()
)
alIfXMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alIfXMode.setStatus("current")


class _AlIfXType_Type(Integer32):
    """Custom type alIfXType based on Integer32"""
    defaultValue = 1

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2),
          ("management", 3),
          ("bridgeLink", 4),
          ("tapLink", 5),
          ("cloneLink", 6),
          ("other", 7),
          ("service", 8))
    )


_AlIfXType_Type.__name__ = "Integer32"
_AlIfXType_Object = MibTableColumn
alIfXType = _AlIfXType_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 3, 1, 2),
    _AlIfXType_Type()
)
alIfXType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alIfXType.setStatus("current")


class _AlIfXSpeed_Type(Integer32):
    """Custom type alIfXSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("ten", 2),
          ("hundred", 3),
          ("thousand", 4),
          ("tenThousand", 5))
    )


_AlIfXSpeed_Type.__name__ = "Integer32"
_AlIfXSpeed_Object = MibTableColumn
alIfXSpeed = _AlIfXSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 3, 1, 3),
    _AlIfXSpeed_Type()
)
alIfXSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alIfXSpeed.setStatus("current")
_AlIfXOrder_Type = InterfaceIndexOrZero
_AlIfXOrder_Object = MibTableColumn
alIfXOrder = _AlIfXOrder_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 3, 1, 4),
    _AlIfXOrder_Type()
)
alIfXOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alIfXOrder.setStatus("current")
_AlIfXLabel_Type = OctetString
_AlIfXLabel_Object = MibTableColumn
alIfXLabel = _AlIfXLabel_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 3, 1, 5),
    _AlIfXLabel_Type()
)
alIfXLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alIfXLabel.setStatus("current")
_AlIfXSupported_Type = Unsigned32
_AlIfXSupported_Object = MibTableColumn
alIfXSupported = _AlIfXSupported_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 3, 1, 6),
    _AlIfXSupported_Type()
)
alIfXSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alIfXSupported.setStatus("current")


class _AlIfXActualMode_Type(Integer32):
    """Custom type alIfXActualMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("fullDuplex", 2),
          ("halfDuplex", 3))
    )


_AlIfXActualMode_Type.__name__ = "Integer32"
_AlIfXActualMode_Object = MibTableColumn
alIfXActualMode = _AlIfXActualMode_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 3, 1, 7),
    _AlIfXActualMode_Type()
)
alIfXActualMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alIfXActualMode.setStatus("current")


class _AlIfXAction_Type(Integer32):
    """Custom type alIfXAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("pair", 2),
          ("all", 3),
          ("bypass", 4))
    )


_AlIfXAction_Type.__name__ = "Integer32"
_AlIfXAction_Object = MibTableColumn
alIfXAction = _AlIfXAction_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 3, 1, 8),
    _AlIfXAction_Type()
)
alIfXAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alIfXAction.setStatus("current")


class _AlIfXUsage_Type(Integer32):
    """Custom type alIfXUsage based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("network", 2),
          ("indirectRedirect", 3),
          ("directRedirect", 4),
          ("clone", 5),
          ("storage", 6),
          ("asymmetry", 7),
          ("management", 8),
          ("system", 9),
          ("coreControler", 10),
          ("flowBalancer", 11),
          ("host", 12),
          ("sfc", 13),
          ("byp", 14))
    )


_AlIfXUsage_Type.__name__ = "Integer32"
_AlIfXUsage_Object = MibTableColumn
alIfXUsage = _AlIfXUsage_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 3, 1, 9),
    _AlIfXUsage_Type()
)
alIfXUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alIfXUsage.setStatus("current")
_AlIfXSwitchId_Type = Unsigned32
_AlIfXSwitchId_Object = MibTableColumn
alIfXSwitchId = _AlIfXSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 3, 1, 10),
    _AlIfXSwitchId_Type()
)
alIfXSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alIfXSwitchId.setStatus("current")
_AlIfXSwitchPort_Type = Unsigned32
_AlIfXSwitchPort_Object = MibTableColumn
alIfXSwitchPort = _AlIfXSwitchPort_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 3, 1, 11),
    _AlIfXSwitchPort_Type()
)
alIfXSwitchPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alIfXSwitchPort.setStatus("current")
_AlIfXUsageCapability_Type = Unsigned32
_AlIfXUsageCapability_Object = MibTableColumn
alIfXUsageCapability = _AlIfXUsageCapability_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 3, 1, 12),
    _AlIfXUsageCapability_Type()
)
alIfXUsageCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alIfXUsageCapability.setStatus("current")
_AlIfXThroughputTX_Type = Counter64
_AlIfXThroughputTX_Object = MibTableColumn
alIfXThroughputTX = _AlIfXThroughputTX_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 3, 1, 13),
    _AlIfXThroughputTX_Type()
)
alIfXThroughputTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alIfXThroughputTX.setStatus("current")
_AlIfXThroughputRX_Type = Counter64
_AlIfXThroughputRX_Object = MibTableColumn
alIfXThroughputRX = _AlIfXThroughputRX_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 3, 1, 14),
    _AlIfXThroughputRX_Type()
)
alIfXThroughputRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alIfXThroughputRX.setStatus("current")
_AlIfXPacketPerSecondTX_Type = Counter64
_AlIfXPacketPerSecondTX_Object = MibTableColumn
alIfXPacketPerSecondTX = _AlIfXPacketPerSecondTX_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 3, 1, 15),
    _AlIfXPacketPerSecondTX_Type()
)
alIfXPacketPerSecondTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alIfXPacketPerSecondTX.setStatus("current")
_AlIfXPacketPerSecondRX_Type = Counter64
_AlIfXPacketPerSecondRX_Object = MibTableColumn
alIfXPacketPerSecondRX = _AlIfXPacketPerSecondRX_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 3, 1, 16),
    _AlIfXPacketPerSecondRX_Type()
)
alIfXPacketPerSecondRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alIfXPacketPerSecondRX.setStatus("current")
_AlIfXSTPStatus_Type = AlEnableDisableNA
_AlIfXSTPStatus_Object = MibTableColumn
alIfXSTPStatus = _AlIfXSTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 3, 1, 17),
    _AlIfXSTPStatus_Type()
)
alIfXSTPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alIfXSTPStatus.setStatus("current")
_AlIfXSTPSupport_Type = Unsigned32
_AlIfXSTPSupport_Object = MibTableColumn
alIfXSTPSupport = _AlIfXSTPSupport_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 3, 1, 18),
    _AlIfXSTPSupport_Type()
)
alIfXSTPSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alIfXSTPSupport.setStatus("current")
_AlSystemNetwork_ObjectIdentity = ObjectIdentity
alSystemNetwork = _AlSystemNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 4)
)
_AlHostname_Type = DisplayString
_AlHostname_Object = MibScalar
alHostname = _AlHostname_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 4, 1),
    _AlHostname_Type()
)
alHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alHostname.setStatus("current")
_AlDomainName_Type = DisplayString
_AlDomainName_Object = MibScalar
alDomainName = _AlDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 4, 2),
    _AlDomainName_Type()
)
alDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alDomainName.setStatus("current")
_AlInBandGateway_Type = IpAddress
_AlInBandGateway_Object = MibScalar
alInBandGateway = _AlInBandGateway_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 4, 3),
    _AlInBandGateway_Type()
)
alInBandGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alInBandGateway.setStatus("current")
_AlOutOfBandGateway_Type = IpAddress
_AlOutOfBandGateway_Object = MibScalar
alOutOfBandGateway = _AlOutOfBandGateway_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 4, 4),
    _AlOutOfBandGateway_Type()
)
alOutOfBandGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alOutOfBandGateway.setStatus("current")
_AlConnRouteTable_Object = MibTable
alConnRouteTable = _AlConnRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 4, 5)
)
if mibBuilder.loadTexts:
    alConnRouteTable.setStatus("current")
_AlConnRouteEntry_Object = MibTableRow
alConnRouteEntry = _AlConnRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 4, 5, 1)
)
alConnRouteEntry.setIndexNames(
    (0, "ALLOT-MIB", "alConnRouteAddress"),
)
if mibBuilder.loadTexts:
    alConnRouteEntry.setStatus("current")
_AlConnRouteAddress_Type = IpAddress
_AlConnRouteAddress_Object = MibTableColumn
alConnRouteAddress = _AlConnRouteAddress_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 4, 5, 1, 1),
    _AlConnRouteAddress_Type()
)
alConnRouteAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alConnRouteAddress.setStatus("current")
_AlConnRouteNetMask_Type = IpAddress
_AlConnRouteNetMask_Object = MibTableColumn
alConnRouteNetMask = _AlConnRouteNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 4, 5, 1, 2),
    _AlConnRouteNetMask_Type()
)
alConnRouteNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alConnRouteNetMask.setStatus("current")
_AlConnRouteGateway_Type = IpAddress
_AlConnRouteGateway_Object = MibTableColumn
alConnRouteGateway = _AlConnRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 4, 5, 1, 3),
    _AlConnRouteGateway_Type()
)
alConnRouteGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alConnRouteGateway.setStatus("current")


class _AlConnRouteIfIndex_Type(Integer32):
    """Custom type alConnRouteIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlConnRouteIfIndex_Type.__name__ = "Integer32"
_AlConnRouteIfIndex_Object = MibTableColumn
alConnRouteIfIndex = _AlConnRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 4, 5, 1, 4),
    _AlConnRouteIfIndex_Type()
)
alConnRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alConnRouteIfIndex.setStatus("current")


class _AlConnRouteType_Type(Integer32):
    """Custom type alConnRouteType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("net", 2))
    )


_AlConnRouteType_Type.__name__ = "Integer32"
_AlConnRouteType_Object = MibTableColumn
alConnRouteType = _AlConnRouteType_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 4, 5, 1, 5),
    _AlConnRouteType_Type()
)
alConnRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alConnRouteType.setStatus("current")


class _AlConnRouteEntryStatus_Type(RowStatus):
    """Custom type alConnRouteEntryStatus based on RowStatus"""
    defaultValue = 1


_AlConnRouteEntryStatus_Type.__name__ = "RowStatus"
_AlConnRouteEntryStatus_Object = MibTableColumn
alConnRouteEntryStatus = _AlConnRouteEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 4, 5, 1, 6),
    _AlConnRouteEntryStatus_Type()
)
alConnRouteEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alConnRouteEntryStatus.setStatus("current")
_AlSystemStatus_ObjectIdentity = ObjectIdentity
alSystemStatus = _AlSystemStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 5)
)


class _AlBypassSetting_Type(Integer32):
    """Custom type alBypassSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("standAlone", 1),
          ("primary", 2),
          ("secondary", 3),
          ("notConnected", 4))
    )


_AlBypassSetting_Type.__name__ = "Integer32"
_AlBypassSetting_Object = MibScalar
alBypassSetting = _AlBypassSetting_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 5, 1),
    _AlBypassSetting_Type()
)
alBypassSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBypassSetting.setStatus("current")


class _AlPower_Type(Integer32):
    """Custom type alPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("problem0", 2),
          ("problem1", 3),
          ("notApplicable", 4))
    )


_AlPower_Type.__name__ = "Integer32"
_AlPower_Object = MibScalar
alPower = _AlPower_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 5, 2),
    _AlPower_Type()
)
alPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPower.setStatus("current")


class _AlFan_Type(Integer32):
    """Custom type alFan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ok", 2),
          ("problem", 3))
    )


_AlFan_Type.__name__ = "Integer32"
_AlFan_Object = MibScalar
alFan = _AlFan_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 5, 3),
    _AlFan_Type()
)
alFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFan.setStatus("current")
_AlRemoteBypass_Type = AlActiveStandbyStatus
_AlRemoteBypass_Object = MibScalar
alRemoteBypass = _AlRemoteBypass_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 5, 4),
    _AlRemoteBypass_Type()
)
alRemoteBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRemoteBypass.setStatus("current")
_AlBypass_Type = AlActiveStandbyStatus
_AlBypass_Object = MibScalar
alBypass = _AlBypass_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 5, 5),
    _AlBypass_Type()
)
alBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBypass.setStatus("current")
_AlSystemSecurity_ObjectIdentity = ObjectIdentity
alSystemSecurity = _AlSystemSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 6)
)
_AlHTTPConnectionMode_Type = AlEnableDisableNA
_AlHTTPConnectionMode_Object = MibScalar
alHTTPConnectionMode = _AlHTTPConnectionMode_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 6, 1),
    _AlHTTPConnectionMode_Type()
)
alHTTPConnectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alHTTPConnectionMode.setStatus("current")
_AlTelnetAccess_Type = AlEnableDisable
_AlTelnetAccess_Object = MibScalar
alTelnetAccess = _AlTelnetAccess_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 6, 2),
    _AlTelnetAccess_Type()
)
alTelnetAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alTelnetAccess.setStatus("current")
_AlPingReply_Type = AlEnableDisable
_AlPingReply_Object = MibScalar
alPingReply = _AlPingReply_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 6, 3),
    _AlPingReply_Type()
)
alPingReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alPingReply.setStatus("current")
_AlEnhancedTcpSecurity_Type = AlEnableDisable
_AlEnhancedTcpSecurity_Object = MibScalar
alEnhancedTcpSecurity = _AlEnhancedTcpSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 6, 4),
    _AlEnhancedTcpSecurity_Type()
)
alEnhancedTcpSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alEnhancedTcpSecurity.setStatus("current")
_AlLcdConfigEnable_Type = AlEnableDisableNA
_AlLcdConfigEnable_Object = MibScalar
alLcdConfigEnable = _AlLcdConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 6, 5),
    _AlLcdConfigEnable_Type()
)
alLcdConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alLcdConfigEnable.setStatus("current")
_AlConnectionTimeout_Type = Integer32
_AlConnectionTimeout_Object = MibScalar
alConnectionTimeout = _AlConnectionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 6, 6),
    _AlConnectionTimeout_Type()
)
alConnectionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alConnectionTimeout.setStatus("current")
_AlACTable_Object = MibTable
alACTable = _AlACTable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 6, 7)
)
if mibBuilder.loadTexts:
    alACTable.setStatus("current")
_AlACEntry_Object = MibTableRow
alACEntry = _AlACEntry_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 6, 7, 1)
)
alACEntry.setIndexNames(
    (0, "ALLOT-MIB", "alACIPAddr"),
)
if mibBuilder.loadTexts:
    alACEntry.setStatus("current")
_AlACIPAddr_Type = IpAddress
_AlACIPAddr_Object = MibTableColumn
alACIPAddr = _AlACIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 6, 7, 1, 1),
    _AlACIPAddr_Type()
)
alACIPAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alACIPAddr.setStatus("current")
_AlACDescr_Type = DisplayString
_AlACDescr_Object = MibTableColumn
alACDescr = _AlACDescr_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 6, 7, 1, 2),
    _AlACDescr_Type()
)
alACDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alACDescr.setStatus("current")
_AlACRowStatus_Type = RowStatus
_AlACRowStatus_Object = MibTableColumn
alACRowStatus = _AlACRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 6, 7, 1, 3),
    _AlACRowStatus_Type()
)
alACRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alACRowStatus.setStatus("current")
_AlSshSecurity_Type = AlEnableDisable
_AlSshSecurity_Object = MibScalar
alSshSecurity = _AlSshSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 6, 8),
    _AlSshSecurity_Type()
)
alSshSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alSshSecurity.setStatus("current")
_AlIpXAddrTable_Object = MibTable
alIpXAddrTable = _AlIpXAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 7)
)
if mibBuilder.loadTexts:
    alIpXAddrTable.setStatus("current")
_AlIpXAddrEntry_Object = MibTableRow
alIpXAddrEntry = _AlIpXAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 7, 1)
)
alIpXAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    alIpXAddrEntry.setStatus("current")
_AlIpXAddr_Type = IpAddress
_AlIpXAddr_Object = MibTableColumn
alIpXAddr = _AlIpXAddr_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 7, 1, 1),
    _AlIpXAddr_Type()
)
alIpXAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alIpXAddr.setStatus("current")
_AlIpXNetMask_Type = IpAddress
_AlIpXNetMask_Object = MibTableColumn
alIpXNetMask = _AlIpXNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 7, 1, 2),
    _AlIpXNetMask_Type()
)
alIpXNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alIpXNetMask.setStatus("current")
_AlIpXVlan_Type = Integer32
_AlIpXVlan_Object = MibTableColumn
alIpXVlan = _AlIpXVlan_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 7, 1, 3),
    _AlIpXVlan_Type()
)
alIpXVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alIpXVlan.setStatus("current")


class _AlIpXEntryStatus_Type(RowStatus):
    """Custom type alIpXEntryStatus based on RowStatus"""
    defaultValue = 1


_AlIpXEntryStatus_Type.__name__ = "RowStatus"
_AlIpXEntryStatus_Object = MibTableColumn
alIpXEntryStatus = _AlIpXEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 7, 1, 4),
    _AlIpXEntryStatus_Type()
)
alIpXEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alIpXEntryStatus.setStatus("current")


class _AlMode_Type(Integer32):
    """Custom type alMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("regular", 1),
          ("tap", 2),
          ("nonApplicable", 3))
    )


_AlMode_Type.__name__ = "Integer32"
_AlMode_Object = MibScalar
alMode = _AlMode_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 8),
    _AlMode_Type()
)
alMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alMode.setStatus("current")
_AlLearningBridge_Type = AlEnableDisableNA
_AlLearningBridge_Object = MibScalar
alLearningBridge = _AlLearningBridge_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 9),
    _AlLearningBridge_Type()
)
alLearningBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alLearningBridge.setStatus("current")
_AlSPTStatus_Type = AlEnableDisableNA
_AlSPTStatus_Object = MibScalar
alSPTStatus = _AlSPTStatus_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 10),
    _AlSPTStatus_Type()
)
alSPTStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alSPTStatus.setStatus("current")


class _AlRedunduncyMode_Type(Integer32):
    """Custom type alRedunduncyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("standalone", 1),
          ("parallel", 2),
          ("serial", 3),
          ("active", 4))
    )


_AlRedunduncyMode_Type.__name__ = "Integer32"
_AlRedunduncyMode_Object = MibScalar
alRedunduncyMode = _AlRedunduncyMode_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 11),
    _AlRedunduncyMode_Type()
)
alRedunduncyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alRedunduncyMode.setStatus("current")
_AlBoxSerialNumber_Type = DisplayString
_AlBoxSerialNumber_Object = MibScalar
alBoxSerialNumber = _AlBoxSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 12),
    _AlBoxSerialNumber_Type()
)
alBoxSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBoxSerialNumber.setStatus("current")
_AlSoftwareVersion_Type = DisplayString
_AlSoftwareVersion_Object = MibScalar
alSoftwareVersion = _AlSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 13),
    _AlSoftwareVersion_Type()
)
alSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSoftwareVersion.setStatus("current")
_AlBackplaneVersion_Type = DisplayString
_AlBackplaneVersion_Object = MibScalar
alBackplaneVersion = _AlBackplaneVersion_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 14),
    _AlBackplaneVersion_Type()
)
alBackplaneVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBackplaneVersion.setStatus("current")
_AlPosIfTable_Object = MibTable
alPosIfTable = _AlPosIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 15)
)
if mibBuilder.loadTexts:
    alPosIfTable.setStatus("current")
_AlPosIfEntry_Object = MibTableRow
alPosIfEntry = _AlPosIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 15, 1)
)
alPosIfEntry.setIndexNames(
    (0, "ALLOT-MIB", "alPosIfIndex"),
)
if mibBuilder.loadTexts:
    alPosIfEntry.setStatus("current")
_AlPosIfIndex_Type = Unsigned32
_AlPosIfIndex_Object = MibTableColumn
alPosIfIndex = _AlPosIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 15, 1, 1),
    _AlPosIfIndex_Type()
)
alPosIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alPosIfIndex.setStatus("current")


class _AlPosIfType_Type(Integer32):
    """Custom type alPosIfType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("oc3", 1),
          ("oc12c", 2),
          ("oc12", 3),
          ("oc48c", 4),
          ("oc48", 5))
    )


_AlPosIfType_Type.__name__ = "Integer32"
_AlPosIfType_Object = MibTableColumn
alPosIfType = _AlPosIfType_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 15, 1, 2),
    _AlPosIfType_Type()
)
alPosIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alPosIfType.setStatus("current")


class _AlPosIfFraming_Type(Integer32):
    """Custom type alPosIfFraming based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdh", 1),
          ("sonet", 2))
    )


_AlPosIfFraming_Type.__name__ = "Integer32"
_AlPosIfFraming_Object = MibTableColumn
alPosIfFraming = _AlPosIfFraming_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 15, 1, 3),
    _AlPosIfFraming_Type()
)
alPosIfFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alPosIfFraming.setStatus("current")


class _AlPosIfCrc_Type(Integer32):
    """Custom type alPosIfCrc based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("crc16", 16),
          ("crc32", 32))
    )


_AlPosIfCrc_Type.__name__ = "Integer32"
_AlPosIfCrc_Object = MibTableColumn
alPosIfCrc = _AlPosIfCrc_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 15, 1, 4),
    _AlPosIfCrc_Type()
)
alPosIfCrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alPosIfCrc.setStatus("current")


class _AlPosIfClocking_Type(Integer32):
    """Custom type alPosIfClocking based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external0", 2),
          ("external1", 3))
    )


_AlPosIfClocking_Type.__name__ = "Integer32"
_AlPosIfClocking_Object = MibTableColumn
alPosIfClocking = _AlPosIfClocking_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 15, 1, 5),
    _AlPosIfClocking_Type()
)
alPosIfClocking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alPosIfClocking.setStatus("current")


class _AlPosIfScrambling_Type(AlEnableDisable):
    """Custom type alPosIfScrambling based on AlEnableDisable"""
    defaultValue = 1


_AlPosIfScrambling_Type.__name__ = "AlEnableDisable"
_AlPosIfScrambling_Object = MibTableColumn
alPosIfScrambling = _AlPosIfScrambling_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 15, 1, 6),
    _AlPosIfScrambling_Type()
)
alPosIfScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alPosIfScrambling.setStatus("current")


class _AlPosIfEncapsulation_Type(Integer32):
    """Custom type alPosIfEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ppp", 1),
          ("chdlc", 2),
          ("frameRelay", 3))
    )


_AlPosIfEncapsulation_Type.__name__ = "Integer32"
_AlPosIfEncapsulation_Object = MibTableColumn
alPosIfEncapsulation = _AlPosIfEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 15, 1, 7),
    _AlPosIfEncapsulation_Type()
)
alPosIfEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alPosIfEncapsulation.setStatus("current")


class _AlPosIfMtu_Type(Integer32):
    """Custom type alPosIfMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 14336),
    )


_AlPosIfMtu_Type.__name__ = "Integer32"
_AlPosIfMtu_Object = MibTableColumn
alPosIfMtu = _AlPosIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 15, 1, 8),
    _AlPosIfMtu_Type()
)
alPosIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alPosIfMtu.setStatus("current")
_AlRedundancyCap_Type = Integer32
_AlRedundancyCap_Object = MibScalar
alRedundancyCap = _AlRedundancyCap_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 16),
    _AlRedundancyCap_Type()
)
alRedundancyCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRedundancyCap.setStatus("current")
_AlBypassUnit_Type = AlEnableDisable
_AlBypassUnit_Object = MibScalar
alBypassUnit = _AlBypassUnit_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 17),
    _AlBypassUnit_Type()
)
alBypassUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alBypassUnit.setStatus("current")
_AlDeviceBWLimits_ObjectIdentity = ObjectIdentity
alDeviceBWLimits = _AlDeviceBWLimits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 18)
)


class _AlDeviceBWLimitsType_Type(Integer32):
    """Custom type alDeviceBWLimitsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplexEach", 1),
          ("fullDuplexBoth", 2),
          ("halfDuplex", 3))
    )


_AlDeviceBWLimitsType_Type.__name__ = "Integer32"
_AlDeviceBWLimitsType_Object = MibScalar
alDeviceBWLimitsType = _AlDeviceBWLimitsType_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 18, 1),
    _AlDeviceBWLimitsType_Type()
)
alDeviceBWLimitsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alDeviceBWLimitsType.setStatus("current")
_AlDeviceBWLimitsOutbound_Type = Integer32
_AlDeviceBWLimitsOutbound_Object = MibScalar
alDeviceBWLimitsOutbound = _AlDeviceBWLimitsOutbound_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 18, 2),
    _AlDeviceBWLimitsOutbound_Type()
)
alDeviceBWLimitsOutbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alDeviceBWLimitsOutbound.setStatus("current")
_AlDeviceBWLimitsInbound_Type = Integer32
_AlDeviceBWLimitsInbound_Object = MibScalar
alDeviceBWLimitsInbound = _AlDeviceBWLimitsInbound_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 18, 3),
    _AlDeviceBWLimitsInbound_Type()
)
alDeviceBWLimitsInbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alDeviceBWLimitsInbound.setStatus("current")
_AlSystemCOC_ObjectIdentity = ObjectIdentity
alSystemCOC = _AlSystemCOC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 19)
)


class _AlCocServerTimeOut_Type(Integer32):
    """Custom type alCocServerTimeOut based on Integer32"""
    defaultValue = 0


_AlCocServerTimeOut_Type.__name__ = "Integer32"
_AlCocServerTimeOut_Object = MibScalar
alCocServerTimeOut = _AlCocServerTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 19, 1),
    _AlCocServerTimeOut_Type()
)
alCocServerTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alCocServerTimeOut.setStatus("current")


class _AlCocServerRetries_Type(Integer32):
    """Custom type alCocServerRetries based on Integer32"""
    defaultValue = 0


_AlCocServerRetries_Type.__name__ = "Integer32"
_AlCocServerRetries_Object = MibScalar
alCocServerRetries = _AlCocServerRetries_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 19, 2),
    _AlCocServerRetries_Type()
)
alCocServerRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alCocServerRetries.setStatus("current")


class _AlCocServerPeriod_Type(Integer32):
    """Custom type alCocServerPeriod based on Integer32"""
    defaultValue = 0


_AlCocServerPeriod_Type.__name__ = "Integer32"
_AlCocServerPeriod_Object = MibScalar
alCocServerPeriod = _AlCocServerPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 19, 3),
    _AlCocServerPeriod_Type()
)
alCocServerPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alCocServerPeriod.setStatus("current")


class _AlCocServiceTimeOut_Type(Integer32):
    """Custom type alCocServiceTimeOut based on Integer32"""
    defaultValue = 0


_AlCocServiceTimeOut_Type.__name__ = "Integer32"
_AlCocServiceTimeOut_Object = MibScalar
alCocServiceTimeOut = _AlCocServiceTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 19, 4),
    _AlCocServiceTimeOut_Type()
)
alCocServiceTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alCocServiceTimeOut.setStatus("current")


class _AlCocServiceRetries_Type(Integer32):
    """Custom type alCocServiceRetries based on Integer32"""
    defaultValue = 0


_AlCocServiceRetries_Type.__name__ = "Integer32"
_AlCocServiceRetries_Object = MibScalar
alCocServiceRetries = _AlCocServiceRetries_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 19, 5),
    _AlCocServiceRetries_Type()
)
alCocServiceRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alCocServiceRetries.setStatus("current")


class _AlCocServicerPeriod_Type(Integer32):
    """Custom type alCocServicerPeriod based on Integer32"""
    defaultValue = 0


_AlCocServicerPeriod_Type.__name__ = "Integer32"
_AlCocServicerPeriod_Object = MibScalar
alCocServicerPeriod = _AlCocServicerPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 19, 6),
    _AlCocServicerPeriod_Type()
)
alCocServicerPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alCocServicerPeriod.setStatus("current")
_AlCocTrackerMAC_Type = OctetString
_AlCocTrackerMAC_Object = MibScalar
alCocTrackerMAC = _AlCocTrackerMAC_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 19, 7),
    _AlCocTrackerMAC_Type()
)
alCocTrackerMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alCocTrackerMAC.setStatus("current")
_AlCocRedirectionMAC_Type = OctetString
_AlCocRedirectionMAC_Object = MibScalar
alCocRedirectionMAC = _AlCocRedirectionMAC_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 19, 8),
    _AlCocRedirectionMAC_Type()
)
alCocRedirectionMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alCocRedirectionMAC.setStatus("current")


class _AlCocUseIp_Type(AlEnableDisableNA):
    """Custom type alCocUseIp based on AlEnableDisableNA"""
    defaultValue = 3


_AlCocUseIp_Type.__name__ = "AlEnableDisableNA"
_AlCocUseIp_Object = MibScalar
alCocUseIp = _AlCocUseIp_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 19, 9),
    _AlCocUseIp_Type()
)
alCocUseIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alCocUseIp.setStatus("current")


class _AlCocRedirectionPort_Type(AlEnableDisable):
    """Custom type alCocRedirectionPort based on AlEnableDisable"""
    defaultValue = 2


_AlCocRedirectionPort_Type.__name__ = "AlEnableDisable"
_AlCocRedirectionPort_Object = MibScalar
alCocRedirectionPort = _AlCocRedirectionPort_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 19, 10),
    _AlCocRedirectionPort_Type()
)
alCocRedirectionPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alCocRedirectionPort.setStatus("current")
_AlInternalRedundancy_ObjectIdentity = ObjectIdentity
alInternalRedundancy = _AlInternalRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 20)
)
_AlBoardTable_Object = MibTable
alBoardTable = _AlBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 20, 1)
)
if mibBuilder.loadTexts:
    alBoardTable.setStatus("current")
_AlBoardEntry_Object = MibTableRow
alBoardEntry = _AlBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 20, 1, 1)
)
alBoardEntry.setIndexNames(
    (0, "ALLOT-MIB", "alBoardId"),
)
if mibBuilder.loadTexts:
    alBoardEntry.setStatus("current")
_AlBoardId_Type = Unsigned32
_AlBoardId_Object = MibTableColumn
alBoardId = _AlBoardId_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 20, 1, 1, 1),
    _AlBoardId_Type()
)
alBoardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alBoardId.setStatus("current")


class _AlBoardType_Type(Integer32):
    """Custom type alBoardType based on Integer32"""
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
              8,
              9,
              10,
              11,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("thirdParty", 1),
          ("apc", 2),
          ("dpic", 3),
          ("host", 4),
          ("byc", 5),
          ("spider", 6),
          ("scorpion", 7),
          ("switch", 8),
          ("dispatcher", 9),
          ("byp", 10),
          ("vas", 11),
          ("exc-cc", 13),
          ("exc-sbh", 14),
          ("nex-1", 15))
    )


_AlBoardType_Type.__name__ = "Integer32"
_AlBoardType_Object = MibTableColumn
alBoardType = _AlBoardType_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 20, 1, 1, 2),
    _AlBoardType_Type()
)
alBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBoardType.setStatus("current")
_AlBoardSerialNumber_Type = DisplayString
_AlBoardSerialNumber_Object = MibTableColumn
alBoardSerialNumber = _AlBoardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 20, 1, 1, 3),
    _AlBoardSerialNumber_Type()
)
alBoardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBoardSerialNumber.setStatus("current")
_AlBoardSoftwareVersion_Type = DisplayString
_AlBoardSoftwareVersion_Object = MibTableColumn
alBoardSoftwareVersion = _AlBoardSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 20, 1, 1, 4),
    _AlBoardSoftwareVersion_Type()
)
alBoardSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBoardSoftwareVersion.setStatus("current")
_AlBoardHardwareVersion_Type = DisplayString
_AlBoardHardwareVersion_Object = MibTableColumn
alBoardHardwareVersion = _AlBoardHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 20, 1, 1, 5),
    _AlBoardHardwareVersion_Type()
)
alBoardHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBoardHardwareVersion.setStatus("current")


class _AlBoardSoftwareStatus_Type(Integer32):
    """Custom type alBoardSoftwareStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("active", 2),
          ("standBy", 3),
          ("notApplicable", 4))
    )


_AlBoardSoftwareStatus_Type.__name__ = "Integer32"
_AlBoardSoftwareStatus_Object = MibTableColumn
alBoardSoftwareStatus = _AlBoardSoftwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 20, 1, 1, 6),
    _AlBoardSoftwareStatus_Type()
)
alBoardSoftwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBoardSoftwareStatus.setStatus("current")


class _AlBoardHWStatus_Type(Integer32):
    """Custom type alBoardHWStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AlBoardHWStatus_Type.__name__ = "Integer32"
_AlBoardHWStatus_Object = MibTableColumn
alBoardHWStatus = _AlBoardHWStatus_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 20, 1, 1, 7),
    _AlBoardHWStatus_Type()
)
alBoardHWStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBoardHWStatus.setStatus("current")


class _AlBoardTemperatureRange_Type(Integer32):
    """Custom type alBoardTemperatureRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("middle", 2),
          ("high", 3))
    )


_AlBoardTemperatureRange_Type.__name__ = "Integer32"
_AlBoardTemperatureRange_Object = MibTableColumn
alBoardTemperatureRange = _AlBoardTemperatureRange_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 20, 1, 1, 8),
    _AlBoardTemperatureRange_Type()
)
alBoardTemperatureRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBoardTemperatureRange.setStatus("current")


class _AlInternalDispatchMode_Type(Integer32):
    """Custom type alInternalDispatchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamicDispatch", 1),
          ("staticDispatch", 2))
    )


_AlInternalDispatchMode_Type.__name__ = "Integer32"
_AlInternalDispatchMode_Object = MibScalar
alInternalDispatchMode = _AlInternalDispatchMode_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 20, 2),
    _AlInternalDispatchMode_Type()
)
alInternalDispatchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alInternalDispatchMode.setStatus("current")
_AlInternalMinDevNum_Type = Integer32
_AlInternalMinDevNum_Object = MibScalar
alInternalMinDevNum = _AlInternalMinDevNum_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 20, 3),
    _AlInternalMinDevNum_Type()
)
alInternalMinDevNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alInternalMinDevNum.setStatus("current")
_AlInternalRedundancyDevNum_Type = Integer32
_AlInternalRedundancyDevNum_Object = MibScalar
alInternalRedundancyDevNum = _AlInternalRedundancyDevNum_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 20, 4),
    _AlInternalRedundancyDevNum_Type()
)
alInternalRedundancyDevNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alInternalRedundancyDevNum.setStatus("current")
_AlInternalActiveDevNum_Type = Integer32
_AlInternalActiveDevNum_Object = MibScalar
alInternalActiveDevNum = _AlInternalActiveDevNum_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 20, 5),
    _AlInternalActiveDevNum_Type()
)
alInternalActiveDevNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alInternalActiveDevNum.setStatus("current")
_AlInternalRateLimit_Type = Integer32
_AlInternalRateLimit_Object = MibScalar
alInternalRateLimit = _AlInternalRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 20, 6),
    _AlInternalRateLimit_Type()
)
alInternalRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alInternalRateLimit.setStatus("current")
_AlWebUpdate_ObjectIdentity = ObjectIdentity
alWebUpdate = _AlWebUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 21)
)
_AlBaseVersion_Type = DisplayString
_AlBaseVersion_Object = MibScalar
alBaseVersion = _AlBaseVersion_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 21, 1),
    _AlBaseVersion_Type()
)
alBaseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBaseVersion.setStatus("current")
_AlCurrentVersion_Type = Integer32
_AlCurrentVersion_Object = MibScalar
alCurrentVersion = _AlCurrentVersion_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 21, 2),
    _AlCurrentVersion_Type()
)
alCurrentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCurrentVersion.setStatus("current")


class _AlLastUpdateStatus_Type(Integer32):
    """Custom type alLastUpdateStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("generalError", 2),
          ("wrongVersion", 3),
          ("wrongFormat", 4),
          ("binaryFileCorrupted", 5),
          ("aSyncSwapRequest", 6),
          ("requestTimeout", 7))
    )


_AlLastUpdateStatus_Type.__name__ = "Integer32"
_AlLastUpdateStatus_Object = MibScalar
alLastUpdateStatus = _AlLastUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 21, 3),
    _AlLastUpdateStatus_Type()
)
alLastUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLastUpdateStatus.setStatus("current")
_AlUserDefinedSignature_ObjectIdentity = ObjectIdentity
alUserDefinedSignature = _AlUserDefinedSignature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 22)
)


class _AlUDSState_Type(AlEnableDisable):
    """Custom type alUDSState based on AlEnableDisable"""
    defaultValue = 2


_AlUDSState_Type.__name__ = "AlEnableDisable"
_AlUDSState_Object = MibScalar
alUDSState = _AlUDSState_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 22, 1),
    _AlUDSState_Type()
)
alUDSState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alUDSState.setStatus("current")
_AlAsymmetric_ObjectIdentity = ObjectIdentity
alAsymmetric = _AlAsymmetric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 23)
)


class _AlAsymmetricGroupId_Type(Integer32):
    """Custom type alAsymmetricGroupId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_AlAsymmetricGroupId_Type.__name__ = "Integer32"
_AlAsymmetricGroupId_Object = MibScalar
alAsymmetricGroupId = _AlAsymmetricGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 23, 1),
    _AlAsymmetricGroupId_Type()
)
alAsymmetricGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alAsymmetricGroupId.setStatus("current")
_AlAsymmetricOwnDeviceId_Type = Integer32
_AlAsymmetricOwnDeviceId_Object = MibScalar
alAsymmetricOwnDeviceId = _AlAsymmetricOwnDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 23, 2),
    _AlAsymmetricOwnDeviceId_Type()
)
alAsymmetricOwnDeviceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alAsymmetricOwnDeviceId.setStatus("current")


class _AlAsymmetricHealthCheck_Type(AlEnableDisable):
    """Custom type alAsymmetricHealthCheck based on AlEnableDisable"""
    defaultValue = 2


_AlAsymmetricHealthCheck_Type.__name__ = "AlEnableDisable"
_AlAsymmetricHealthCheck_Object = MibScalar
alAsymmetricHealthCheck = _AlAsymmetricHealthCheck_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 23, 3),
    _AlAsymmetricHealthCheck_Type()
)
alAsymmetricHealthCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alAsymmetricHealthCheck.setStatus("current")


class _AlAsymmetricTransportType_Type(Integer32):
    """Custom type alAsymmetricTransportType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("point2point", 1),
          ("mac", 2),
          ("ip", 3))
    )


_AlAsymmetricTransportType_Type.__name__ = "Integer32"
_AlAsymmetricTransportType_Object = MibScalar
alAsymmetricTransportType = _AlAsymmetricTransportType_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 23, 5),
    _AlAsymmetricTransportType_Type()
)
alAsymmetricTransportType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alAsymmetricTransportType.setStatus("current")


class _AlAsymmetricEnable_Type(AlEnableDisable):
    """Custom type alAsymmetricEnable based on AlEnableDisable"""
    defaultValue = 2


_AlAsymmetricEnable_Type.__name__ = "AlEnableDisable"
_AlAsymmetricEnable_Object = MibScalar
alAsymmetricEnable = _AlAsymmetricEnable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 23, 6),
    _AlAsymmetricEnable_Type()
)
alAsymmetricEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alAsymmetricEnable.setStatus("current")
_AlAsymmetricDeviceTable_Object = MibTable
alAsymmetricDeviceTable = _AlAsymmetricDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 23, 7)
)
if mibBuilder.loadTexts:
    alAsymmetricDeviceTable.setStatus("current")
_AlAsymmetricDeviceEntry_Object = MibTableRow
alAsymmetricDeviceEntry = _AlAsymmetricDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 23, 7, 1)
)
alAsymmetricDeviceEntry.setIndexNames(
    (0, "ALLOT-MIB", "alAsymmetricRemoteDeviceId"),
)
if mibBuilder.loadTexts:
    alAsymmetricDeviceEntry.setStatus("current")
_AlAsymmetricRemoteDeviceId_Type = Unsigned32
_AlAsymmetricRemoteDeviceId_Object = MibTableColumn
alAsymmetricRemoteDeviceId = _AlAsymmetricRemoteDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 23, 7, 1, 1),
    _AlAsymmetricRemoteDeviceId_Type()
)
alAsymmetricRemoteDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alAsymmetricRemoteDeviceId.setStatus("current")
_AlAsymmetricControlVLAN_Type = Integer32
_AlAsymmetricControlVLAN_Object = MibTableColumn
alAsymmetricControlVLAN = _AlAsymmetricControlVLAN_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 23, 7, 1, 2),
    _AlAsymmetricControlVLAN_Type()
)
alAsymmetricControlVLAN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alAsymmetricControlVLAN.setStatus("current")
_AlAsymmetricPort_Type = Integer32
_AlAsymmetricPort_Object = MibTableColumn
alAsymmetricPort = _AlAsymmetricPort_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 23, 7, 1, 4),
    _AlAsymmetricPort_Type()
)
alAsymmetricPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alAsymmetricPort.setStatus("current")


class _AlAsymmetricMAC_Type(OctetString):
    """Custom type alAsymmetricMAC based on OctetString"""
    defaultValue = OctetString("00 00 00 00 00")


_AlAsymmetricMAC_Type.__name__ = "OctetString"
_AlAsymmetricMAC_Object = MibTableColumn
alAsymmetricMAC = _AlAsymmetricMAC_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 23, 7, 1, 5),
    _AlAsymmetricMAC_Type()
)
alAsymmetricMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alAsymmetricMAC.setStatus("current")
_AlAsymmetricIP_Type = IpAddress
_AlAsymmetricIP_Object = MibTableColumn
alAsymmetricIP = _AlAsymmetricIP_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 23, 7, 1, 6),
    _AlAsymmetricIP_Type()
)
alAsymmetricIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alAsymmetricIP.setStatus("current")


class _AlAsymmetricHealthCheckStatus_Type(Integer32):
    """Custom type alAsymmetricHealthCheckStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("up", 2),
          ("down", 3))
    )


_AlAsymmetricHealthCheckStatus_Type.__name__ = "Integer32"
_AlAsymmetricHealthCheckStatus_Object = MibTableColumn
alAsymmetricHealthCheckStatus = _AlAsymmetricHealthCheckStatus_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 23, 7, 1, 7),
    _AlAsymmetricHealthCheckStatus_Type()
)
alAsymmetricHealthCheckStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAsymmetricHealthCheckStatus.setStatus("current")
_AlAsymmetricEntryStatus_Type = RowStatus
_AlAsymmetricEntryStatus_Object = MibTableColumn
alAsymmetricEntryStatus = _AlAsymmetricEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 23, 7, 1, 8),
    _AlAsymmetricEntryStatus_Type()
)
alAsymmetricEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alAsymmetricEntryStatus.setStatus("current")
_AlServiceActivation_ObjectIdentity = ObjectIdentity
alServiceActivation = _AlServiceActivation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 24)
)
_AlURLFiltering_ObjectIdentity = ObjectIdentity
alURLFiltering = _AlURLFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 24, 1)
)
_AlUrlFOperationMode_Type = AlUrlOperationMode
_AlUrlFOperationMode_Object = MibScalar
alUrlFOperationMode = _AlUrlFOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 24, 1, 1),
    _AlUrlFOperationMode_Type()
)
alUrlFOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alUrlFOperationMode.setStatus("current")


class _AlUrlFAction_Type(Integer32):
    """Custom type alUrlFAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("reportOnly", 1),
          ("block", 2),
          ("redirect", 3),
          ("respond", 4))
    )


_AlUrlFAction_Type.__name__ = "Integer32"
_AlUrlFAction_Object = MibScalar
alUrlFAction = _AlUrlFAction_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 24, 1, 2),
    _AlUrlFAction_Type()
)
alUrlFAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alUrlFAction.setStatus("current")
_AlUrlFPortal_Type = OctetString
_AlUrlFPortal_Object = MibScalar
alUrlFPortal = _AlUrlFPortal_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 24, 1, 3),
    _AlUrlFPortal_Type()
)
alUrlFPortal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alUrlFPortal.setStatus("current")


class _AlUrlFLastUpdateStatus_Type(Integer32):
    """Custom type alUrlFLastUpdateStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("generalError", 2),
          ("wrongFormat", 3),
          ("binaryFileCorrupted", 4),
          ("requestTimeout", 5),
          ("missingFiles", 6))
    )


_AlUrlFLastUpdateStatus_Type.__name__ = "Integer32"
_AlUrlFLastUpdateStatus_Object = MibScalar
alUrlFLastUpdateStatus = _AlUrlFLastUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 24, 1, 4),
    _AlUrlFLastUpdateStatus_Type()
)
alUrlFLastUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alUrlFLastUpdateStatus.setStatus("current")
_AlURLMonitoring_ObjectIdentity = ObjectIdentity
alURLMonitoring = _AlURLMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 24, 2)
)
_AlUrlMOperatonMode_Type = AlUrlOperationMode
_AlUrlMOperatonMode_Object = MibScalar
alUrlMOperatonMode = _AlUrlMOperatonMode_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 24, 2, 1),
    _AlUrlMOperatonMode_Type()
)
alUrlMOperatonMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alUrlMOperatonMode.setStatus("current")
_AlCaptivePortal_ObjectIdentity = ObjectIdentity
alCaptivePortal = _AlCaptivePortal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 24, 3)
)


class _AlCaptivePortalRedirectionTechnique_Type(Integer32):
    """Custom type alCaptivePortalRedirectionTechnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("request", 2),
          ("reply", 3))
    )


_AlCaptivePortalRedirectionTechnique_Type.__name__ = "Integer32"
_AlCaptivePortalRedirectionTechnique_Object = MibScalar
alCaptivePortalRedirectionTechnique = _AlCaptivePortalRedirectionTechnique_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 24, 3, 1),
    _AlCaptivePortalRedirectionTechnique_Type()
)
alCaptivePortalRedirectionTechnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alCaptivePortalRedirectionTechnique.setStatus("current")
_AlCaptivePortalPassPhrase_Type = OctetString
_AlCaptivePortalPassPhrase_Object = MibScalar
alCaptivePortalPassPhrase = _AlCaptivePortalPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 24, 3, 2),
    _AlCaptivePortalPassPhrase_Type()
)
alCaptivePortalPassPhrase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCaptivePortalPassPhrase.setStatus("current")
_AlVoipReportingActivation_Type = AlEnableDisable
_AlVoipReportingActivation_Object = MibScalar
alVoipReportingActivation = _AlVoipReportingActivation_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 24, 4),
    _AlVoipReportingActivation_Type()
)
alVoipReportingActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alVoipReportingActivation.setStatus("current")
_AlSPSensorActivation_Type = AlEnableDisable
_AlSPSensorActivation_Object = MibScalar
alSPSensorActivation = _AlSPSensorActivation_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 24, 5),
    _AlSPSensorActivation_Type()
)
alSPSensorActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alSPSensorActivation.setStatus("current")
_AlFupProtocolVersion_Type = Integer32
_AlFupProtocolVersion_Object = MibScalar
alFupProtocolVersion = _AlFupProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 25),
    _AlFupProtocolVersion_Type()
)
alFupProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFupProtocolVersion.setStatus("current")
_AlPredictiveDPI_ObjectIdentity = ObjectIdentity
alPredictiveDPI = _AlPredictiveDPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 26)
)
_AlPDPIState_Type = AlEnableDisable
_AlPDPIState_Object = MibScalar
alPDPIState = _AlPDPIState_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 26, 1),
    _AlPDPIState_Type()
)
alPDPIState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alPDPIState.setStatus("current")


class _AlIPv6State_Type(AlEnableDisable):
    """Custom type alIPv6State based on AlEnableDisable"""
    defaultValue = 2


_AlIPv6State_Type.__name__ = "AlEnableDisable"
_AlIPv6State_Object = MibScalar
alIPv6State = _AlIPv6State_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 27),
    _AlIPv6State_Type()
)
alIPv6State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alIPv6State.setStatus("current")
_AlSelectiveBypass_ObjectIdentity = ObjectIdentity
alSelectiveBypass = _AlSelectiveBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 28)
)


class _AlSelectiveBypassActivation_Type(AlEnableDisable):
    """Custom type alSelectiveBypassActivation based on AlEnableDisable"""
    defaultValue = 2


_AlSelectiveBypassActivation_Type.__name__ = "AlEnableDisable"
_AlSelectiveBypassActivation_Object = MibScalar
alSelectiveBypassActivation = _AlSelectiveBypassActivation_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 28, 1),
    _AlSelectiveBypassActivation_Type()
)
alSelectiveBypassActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alSelectiveBypassActivation.setStatus("current")


class _AlSelectiveBypassVlanGroup_Type(Integer32):
    """Custom type alSelectiveBypassVlanGroup based on Integer32"""
    defaultValue = 0


_AlSelectiveBypassVlanGroup_Type.__name__ = "Integer32"
_AlSelectiveBypassVlanGroup_Object = MibScalar
alSelectiveBypassVlanGroup = _AlSelectiveBypassVlanGroup_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 28, 2),
    _AlSelectiveBypassVlanGroup_Type()
)
alSelectiveBypassVlanGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alSelectiveBypassVlanGroup.setStatus("current")
_AlTetherDetectState_Type = AlEnableDisable
_AlTetherDetectState_Object = MibScalar
alTetherDetectState = _AlTetherDetectState_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 6, 29),
    _AlTetherDetectState_Type()
)
alTetherDetectState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alTetherDetectState.setStatus("current")
_AlGenericLastChangeVar_Type = VariablePointer
_AlGenericLastChangeVar_Object = MibScalar
alGenericLastChangeVar = _AlGenericLastChangeVar_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 8),
    _AlGenericLastChangeVar_Type()
)
alGenericLastChangeVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alGenericLastChangeVar.setStatus("current")
_AlGenericLastChangeIntVal_Type = Integer32
_AlGenericLastChangeIntVal_Object = MibScalar
alGenericLastChangeIntVal = _AlGenericLastChangeIntVal_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 9),
    _AlGenericLastChangeIntVal_Type()
)
alGenericLastChangeIntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alGenericLastChangeIntVal.setStatus("current")
_AlGenericLastChangeTimestamp_Type = TimeStamp
_AlGenericLastChangeTimestamp_Object = MibScalar
alGenericLastChangeTimestamp = _AlGenericLastChangeTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 10),
    _AlGenericLastChangeTimestamp_Type()
)
alGenericLastChangeTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alGenericLastChangeTimestamp.setStatus("current")
_AlGenericConfigTrapEnable_Type = AlEnableDisable
_AlGenericConfigTrapEnable_Object = MibScalar
alGenericConfigTrapEnable = _AlGenericConfigTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 11),
    _AlGenericConfigTrapEnable_Type()
)
alGenericConfigTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alGenericConfigTrapEnable.setStatus("current")


class _AlRebootRequest_Type(Integer32):
    """Custom type alRebootRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("reboot", 1),
          ("shutdown", 2),
          ("indeterminate", 3))
    )


_AlRebootRequest_Type.__name__ = "Integer32"
_AlRebootRequest_Object = MibScalar
alRebootRequest = _AlRebootRequest_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 12),
    _AlRebootRequest_Type()
)
alRebootRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alRebootRequest.setStatus("current")
_AlGenericLastChangeStrVal_Type = OctetString
_AlGenericLastChangeStrVal_Object = MibScalar
alGenericLastChangeStrVal = _AlGenericLastChangeStrVal_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 13),
    _AlGenericLastChangeStrVal_Type()
)
alGenericLastChangeStrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alGenericLastChangeStrVal.setStatus("current")
_AlGenericLastChangeAddrVal_Type = IpAddress
_AlGenericLastChangeAddrVal_Object = MibScalar
alGenericLastChangeAddrVal = _AlGenericLastChangeAddrVal_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 2, 14),
    _AlGenericLastChangeAddrVal_Type()
)
alGenericLastChangeAddrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alGenericLastChangeAddrVal.setStatus("current")
_AlProvisioning_ObjectIdentity = ObjectIdentity
alProvisioning = _AlProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3)
)
_AlCatalogs_ObjectIdentity = ObjectIdentity
alCatalogs = _AlCatalogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 1)
)
_AlCatalogsLastChangeTimestamp_Type = TimeStamp
_AlCatalogsLastChangeTimestamp_Object = MibScalar
alCatalogsLastChangeTimestamp = _AlCatalogsLastChangeTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 1, 1),
    _AlCatalogsLastChangeTimestamp_Type()
)
alCatalogsLastChangeTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCatalogsLastChangeTimestamp.setStatus("current")
_AlCatalogsLastChangeRequest_Type = Integer32
_AlCatalogsLastChangeRequest_Object = MibScalar
alCatalogsLastChangeRequest = _AlCatalogsLastChangeRequest_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 1, 2),
    _AlCatalogsLastChangeRequest_Type()
)
alCatalogsLastChangeRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCatalogsLastChangeRequest.setStatus("current")
_AlCatalogListTable_Object = MibTable
alCatalogListTable = _AlCatalogListTable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 1, 3)
)
if mibBuilder.loadTexts:
    alCatalogListTable.setStatus("current")
_AlCatalogListEntry_Object = MibTableRow
alCatalogListEntry = _AlCatalogListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 1, 3, 1)
)
alCatalogListEntry.setIndexNames(
    (0, "ALLOT-MIB", "alCatalogId"),
)
if mibBuilder.loadTexts:
    alCatalogListEntry.setStatus("current")
_AlCatalogId_Type = Unsigned32
_AlCatalogId_Object = MibTableColumn
alCatalogId = _AlCatalogId_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 1, 3, 1, 1),
    _AlCatalogId_Type()
)
alCatalogId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alCatalogId.setStatus("current")
_AlCatalogName_Type = DisplayString
_AlCatalogName_Object = MibTableColumn
alCatalogName = _AlCatalogName_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 1, 3, 1, 2),
    _AlCatalogName_Type()
)
alCatalogName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCatalogName.setStatus("current")
_AlCatalogsTable_Object = MibTable
alCatalogsTable = _AlCatalogsTable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 1, 4)
)
if mibBuilder.loadTexts:
    alCatalogsTable.setStatus("current")
_AlCatalogsEntry_Object = MibTableRow
alCatalogsEntry = _AlCatalogsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 1, 4, 1)
)
alCatalogsEntry.setIndexNames(
    (0, "ALLOT-MIB", "alCatalogId"),
    (0, "ALLOT-MIB", "alCatalogInstance"),
)
if mibBuilder.loadTexts:
    alCatalogsEntry.setStatus("current")
_AlCatalogInstance_Type = Unsigned32
_AlCatalogInstance_Object = MibTableColumn
alCatalogInstance = _AlCatalogInstance_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 1, 4, 1, 1),
    _AlCatalogInstance_Type()
)
alCatalogInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alCatalogInstance.setStatus("current")
_AlCatalogLastCommand_Type = AlConfigCommand
_AlCatalogLastCommand_Object = MibTableColumn
alCatalogLastCommand = _AlCatalogLastCommand_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 1, 4, 1, 2),
    _AlCatalogLastCommand_Type()
)
alCatalogLastCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCatalogLastCommand.setStatus("current")
_AlCatalogTimestamp_Type = TimeStamp
_AlCatalogTimestamp_Object = MibTableColumn
alCatalogTimestamp = _AlCatalogTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 1, 4, 1, 3),
    _AlCatalogTimestamp_Type()
)
alCatalogTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCatalogTimestamp.setStatus("current")
_AlCatalogData_Type = OctetString
_AlCatalogData_Object = MibTableColumn
alCatalogData = _AlCatalogData_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 1, 4, 1, 4),
    _AlCatalogData_Type()
)
alCatalogData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCatalogData.setStatus("current")
_AlCatalogCheckSum_Type = Unsigned32
_AlCatalogCheckSum_Object = MibTableColumn
alCatalogCheckSum = _AlCatalogCheckSum_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 1, 4, 1, 5),
    _AlCatalogCheckSum_Type()
)
alCatalogCheckSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCatalogCheckSum.setStatus("current")
_AlCatalogInstanceStatus_Type = AlInstanceStatus
_AlCatalogInstanceStatus_Object = MibTableColumn
alCatalogInstanceStatus = _AlCatalogInstanceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 1, 4, 1, 6),
    _AlCatalogInstanceStatus_Type()
)
alCatalogInstanceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCatalogInstanceStatus.setStatus("current")
_AlCatalogLastChangeOrigin_Type = Unsigned32
_AlCatalogLastChangeOrigin_Object = MibTableColumn
alCatalogLastChangeOrigin = _AlCatalogLastChangeOrigin_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 1, 4, 1, 7),
    _AlCatalogLastChangeOrigin_Type()
)
alCatalogLastChangeOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCatalogLastChangeOrigin.setStatus("current")
_AlPolicies_ObjectIdentity = ObjectIdentity
alPolicies = _AlPolicies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2)
)
_AlLineLastChange_Type = TimeStamp
_AlLineLastChange_Object = MibScalar
alLineLastChange = _AlLineLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 1),
    _AlLineLastChange_Type()
)
alLineLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLineLastChange.setStatus("current")
_AlLineTable_Object = MibTable
alLineTable = _AlLineTable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 2)
)
if mibBuilder.loadTexts:
    alLineTable.setStatus("current")
_AlLineEntry_Object = MibTableRow
alLineEntry = _AlLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 2, 1)
)
alLineEntry.setIndexNames(
    (0, "ALLOT-MIB", "alLineId"),
)
if mibBuilder.loadTexts:
    alLineEntry.setStatus("current")
_AlLineId_Type = Unsigned32
_AlLineId_Object = MibTableColumn
alLineId = _AlLineId_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 2, 1, 1),
    _AlLineId_Type()
)
alLineId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alLineId.setStatus("current")
_AlLineLastCommand_Type = AlConfigCommand
_AlLineLastCommand_Object = MibTableColumn
alLineLastCommand = _AlLineLastCommand_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 2, 1, 2),
    _AlLineLastCommand_Type()
)
alLineLastCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLineLastCommand.setStatus("current")
_AlLineTimestamp_Type = TimeStamp
_AlLineTimestamp_Object = MibTableColumn
alLineTimestamp = _AlLineTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 2, 1, 3),
    _AlLineTimestamp_Type()
)
alLineTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLineTimestamp.setStatus("current")
_AlLineData_Type = OctetString
_AlLineData_Object = MibTableColumn
alLineData = _AlLineData_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 2, 1, 4),
    _AlLineData_Type()
)
alLineData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLineData.setStatus("current")
_AlLineCheckSum_Type = Unsigned32
_AlLineCheckSum_Object = MibTableColumn
alLineCheckSum = _AlLineCheckSum_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 2, 1, 5),
    _AlLineCheckSum_Type()
)
alLineCheckSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLineCheckSum.setStatus("current")
_AlLineInstanceStatus_Type = AlInstanceStatus
_AlLineInstanceStatus_Object = MibTableColumn
alLineInstanceStatus = _AlLineInstanceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 2, 1, 6),
    _AlLineInstanceStatus_Type()
)
alLineInstanceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLineInstanceStatus.setStatus("current")
_AlLineLastChangeOrigin_Type = Unsigned32
_AlLineLastChangeOrigin_Object = MibTableColumn
alLineLastChangeOrigin = _AlLineLastChangeOrigin_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 2, 1, 7),
    _AlLineLastChangeOrigin_Type()
)
alLineLastChangeOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLineLastChangeOrigin.setStatus("current")
_AlPipeLastChange_Type = TimeStamp
_AlPipeLastChange_Object = MibScalar
alPipeLastChange = _AlPipeLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 3),
    _AlPipeLastChange_Type()
)
alPipeLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPipeLastChange.setStatus("current")
_AlPipeTable_Object = MibTable
alPipeTable = _AlPipeTable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 4)
)
if mibBuilder.loadTexts:
    alPipeTable.setStatus("current")
_AlPipeEntry_Object = MibTableRow
alPipeEntry = _AlPipeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 4, 1)
)
alPipeEntry.setIndexNames(
    (0, "ALLOT-MIB", "alLineId"),
    (0, "ALLOT-MIB", "alPipeId"),
)
if mibBuilder.loadTexts:
    alPipeEntry.setStatus("current")
_AlPipeId_Type = Unsigned32
_AlPipeId_Object = MibTableColumn
alPipeId = _AlPipeId_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 4, 1, 1),
    _AlPipeId_Type()
)
alPipeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alPipeId.setStatus("current")
_AlPipeLastCommand_Type = AlConfigCommand
_AlPipeLastCommand_Object = MibTableColumn
alPipeLastCommand = _AlPipeLastCommand_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 4, 1, 2),
    _AlPipeLastCommand_Type()
)
alPipeLastCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPipeLastCommand.setStatus("current")
_AlPipeTimestamp_Type = TimeStamp
_AlPipeTimestamp_Object = MibTableColumn
alPipeTimestamp = _AlPipeTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 4, 1, 3),
    _AlPipeTimestamp_Type()
)
alPipeTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPipeTimestamp.setStatus("current")
_AlPipeData_Type = OctetString
_AlPipeData_Object = MibTableColumn
alPipeData = _AlPipeData_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 4, 1, 4),
    _AlPipeData_Type()
)
alPipeData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPipeData.setStatus("current")
_AlPipeCheckSum_Type = Unsigned32
_AlPipeCheckSum_Object = MibTableColumn
alPipeCheckSum = _AlPipeCheckSum_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 4, 1, 5),
    _AlPipeCheckSum_Type()
)
alPipeCheckSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPipeCheckSum.setStatus("current")


class _AlPipeIsTemplate_Type(Integer32):
    """Custom type alPipeIsTemplate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("regular", 1),
          ("template", 2))
    )


_AlPipeIsTemplate_Type.__name__ = "Integer32"
_AlPipeIsTemplate_Object = MibTableColumn
alPipeIsTemplate = _AlPipeIsTemplate_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 4, 1, 6),
    _AlPipeIsTemplate_Type()
)
alPipeIsTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPipeIsTemplate.setStatus("current")
_AlPipeStatus_Type = AlInstanceStatus
_AlPipeStatus_Object = MibTableColumn
alPipeStatus = _AlPipeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 4, 1, 7),
    _AlPipeStatus_Type()
)
alPipeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPipeStatus.setStatus("current")
_AlPipeLastChangeOrigin_Type = Unsigned32
_AlPipeLastChangeOrigin_Object = MibTableColumn
alPipeLastChangeOrigin = _AlPipeLastChangeOrigin_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 4, 1, 8),
    _AlPipeLastChangeOrigin_Type()
)
alPipeLastChangeOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPipeLastChangeOrigin.setStatus("current")
_AlVCLastChange_Type = TimeStamp
_AlVCLastChange_Object = MibScalar
alVCLastChange = _AlVCLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 5),
    _AlVCLastChange_Type()
)
alVCLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVCLastChange.setStatus("current")
_AlVCTable_Object = MibTable
alVCTable = _AlVCTable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 6)
)
if mibBuilder.loadTexts:
    alVCTable.setStatus("current")
_AlVCEntry_Object = MibTableRow
alVCEntry = _AlVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 6, 1)
)
alVCEntry.setIndexNames(
    (0, "ALLOT-MIB", "alLineId"),
    (0, "ALLOT-MIB", "alPipeId"),
    (0, "ALLOT-MIB", "alVCId"),
)
if mibBuilder.loadTexts:
    alVCEntry.setStatus("current")
_AlVCId_Type = Unsigned32
_AlVCId_Object = MibTableColumn
alVCId = _AlVCId_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 6, 1, 1),
    _AlVCId_Type()
)
alVCId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alVCId.setStatus("current")
_AlVCLastCommand_Type = AlConfigCommand
_AlVCLastCommand_Object = MibTableColumn
alVCLastCommand = _AlVCLastCommand_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 6, 1, 2),
    _AlVCLastCommand_Type()
)
alVCLastCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVCLastCommand.setStatus("current")
_AlVCTimestamp_Type = TimeStamp
_AlVCTimestamp_Object = MibTableColumn
alVCTimestamp = _AlVCTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 6, 1, 3),
    _AlVCTimestamp_Type()
)
alVCTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVCTimestamp.setStatus("current")
_AlVCData_Type = OctetString
_AlVCData_Object = MibTableColumn
alVCData = _AlVCData_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 6, 1, 4),
    _AlVCData_Type()
)
alVCData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVCData.setStatus("current")
_AlVCCheckSum_Type = Unsigned32
_AlVCCheckSum_Object = MibTableColumn
alVCCheckSum = _AlVCCheckSum_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 6, 1, 5),
    _AlVCCheckSum_Type()
)
alVCCheckSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVCCheckSum.setStatus("current")


class _AlVCIsTemplate_Type(Integer32):
    """Custom type alVCIsTemplate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("regular", 1),
          ("template", 2))
    )


_AlVCIsTemplate_Type.__name__ = "Integer32"
_AlVCIsTemplate_Object = MibTableColumn
alVCIsTemplate = _AlVCIsTemplate_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 6, 1, 6),
    _AlVCIsTemplate_Type()
)
alVCIsTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVCIsTemplate.setStatus("current")
_AlVCStatus_Type = AlInstanceStatus
_AlVCStatus_Object = MibTableColumn
alVCStatus = _AlVCStatus_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 6, 1, 7),
    _AlVCStatus_Type()
)
alVCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVCStatus.setStatus("current")
_AlVCLastChangeOrigin_Type = Unsigned32
_AlVCLastChangeOrigin_Object = MibTableColumn
alVCLastChangeOrigin = _AlVCLastChangeOrigin_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 6, 1, 8),
    _AlVCLastChangeOrigin_Type()
)
alVCLastChangeOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVCLastChangeOrigin.setStatus("current")
_AlLineConfTrapEnable_Type = AlEnableDisable
_AlLineConfTrapEnable_Object = MibScalar
alLineConfTrapEnable = _AlLineConfTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 7),
    _AlLineConfTrapEnable_Type()
)
alLineConfTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alLineConfTrapEnable.setStatus("current")
_AlPipeConfTrapEnable_Type = AlEnableDisable
_AlPipeConfTrapEnable_Object = MibScalar
alPipeConfTrapEnable = _AlPipeConfTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 8),
    _AlPipeConfTrapEnable_Type()
)
alPipeConfTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alPipeConfTrapEnable.setStatus("current")
_AlVcConfTrapEnable_Type = AlEnableDisable
_AlVcConfTrapEnable_Object = MibScalar
alVcConfTrapEnable = _AlVcConfTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 9),
    _AlVcConfTrapEnable_Type()
)
alVcConfTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alVcConfTrapEnable.setStatus("current")


class _AlPolicyModificationTag_Type(Integer32):
    """Custom type alPolicyModificationTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("inSync", 1),
          ("snmpNotInSync", 2),
          ("dataSrvNotInSync", 3),
          ("rescuePerformed", 4),
          ("unknown", 5))
    )


_AlPolicyModificationTag_Type.__name__ = "Integer32"
_AlPolicyModificationTag_Object = MibScalar
alPolicyModificationTag = _AlPolicyModificationTag_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 3, 2, 10),
    _AlPolicyModificationTag_Type()
)
alPolicyModificationTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPolicyModificationTag.setStatus("current")
_AlStatistics_ObjectIdentity = ObjectIdentity
alStatistics = _AlStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4)
)
_AlStatCntlTable_Object = MibTable
alStatCntlTable = _AlStatCntlTable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4, 1)
)
if mibBuilder.loadTexts:
    alStatCntlTable.setStatus("current")
_AlStatCntlEntry_Object = MibTableRow
alStatCntlEntry = _AlStatCntlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4, 1, 1)
)
alStatCntlEntry.setIndexNames(
    (0, "ALLOT-MIB", "alStatCntlLine"),
    (0, "ALLOT-MIB", "alStatCntlPipe"),
    (0, "ALLOT-MIB", "alStatCntlVC"),
    (1, "ALLOT-MIB", "alStatCntlUserInstance"),
)
if mibBuilder.loadTexts:
    alStatCntlEntry.setStatus("current")
_AlStatCntlLine_Type = Unsigned32
_AlStatCntlLine_Object = MibTableColumn
alStatCntlLine = _AlStatCntlLine_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4, 1, 1, 1),
    _AlStatCntlLine_Type()
)
alStatCntlLine.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alStatCntlLine.setStatus("current")
_AlStatCntlPipe_Type = Unsigned32
_AlStatCntlPipe_Object = MibTableColumn
alStatCntlPipe = _AlStatCntlPipe_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4, 1, 1, 2),
    _AlStatCntlPipe_Type()
)
alStatCntlPipe.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alStatCntlPipe.setStatus("current")
_AlStatCntlVC_Type = Unsigned32
_AlStatCntlVC_Object = MibTableColumn
alStatCntlVC = _AlStatCntlVC_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4, 1, 1, 3),
    _AlStatCntlVC_Type()
)
alStatCntlVC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alStatCntlVC.setStatus("current")
_AlStatCntlUserInstance_Type = DisplayString
_AlStatCntlUserInstance_Object = MibTableColumn
alStatCntlUserInstance = _AlStatCntlUserInstance_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4, 1, 1, 4),
    _AlStatCntlUserInstance_Type()
)
alStatCntlUserInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alStatCntlUserInstance.setStatus("current")


class _AlStatCntlIsTemplate_Type(Integer32):
    """Custom type alStatCntlIsTemplate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("specific", 1),
          ("all", 2))
    )


_AlStatCntlIsTemplate_Type.__name__ = "Integer32"
_AlStatCntlIsTemplate_Object = MibTableColumn
alStatCntlIsTemplate = _AlStatCntlIsTemplate_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4, 1, 1, 5),
    _AlStatCntlIsTemplate_Type()
)
alStatCntlIsTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alStatCntlIsTemplate.setStatus("current")
_AlStatCntlStartedAt_Type = DateAndTime
_AlStatCntlStartedAt_Object = MibTableColumn
alStatCntlStartedAt = _AlStatCntlStartedAt_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4, 1, 1, 6),
    _AlStatCntlStartedAt_Type()
)
alStatCntlStartedAt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alStatCntlStartedAt.setStatus("current")
_AlStatCntlIsView_Type = AlEnableDisable
_AlStatCntlIsView_Object = MibTableColumn
alStatCntlIsView = _AlStatCntlIsView_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4, 1, 1, 7),
    _AlStatCntlIsView_Type()
)
alStatCntlIsView.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alStatCntlIsView.setStatus("current")
_AlStatCntlIsAlert_Type = AlEnableDisable
_AlStatCntlIsAlert_Object = MibTableColumn
alStatCntlIsAlert = _AlStatCntlIsAlert_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4, 1, 1, 8),
    _AlStatCntlIsAlert_Type()
)
alStatCntlIsAlert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alStatCntlIsAlert.setStatus("current")
_AlStatCntlStatus_Type = RowStatus
_AlStatCntlStatus_Object = MibTableColumn
alStatCntlStatus = _AlStatCntlStatus_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4, 1, 1, 9),
    _AlStatCntlStatus_Type()
)
alStatCntlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alStatCntlStatus.setStatus("current")
_AlStatTable_Object = MibTable
alStatTable = _AlStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4, 2)
)
if mibBuilder.loadTexts:
    alStatTable.setStatus("current")
_AlStatEntry_Object = MibTableRow
alStatEntry = _AlStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4, 2, 1)
)
alStatEntry.setIndexNames(
    (0, "ALLOT-MIB", "alStatCntlLine"),
    (0, "ALLOT-MIB", "alStatCntlPipe"),
    (0, "ALLOT-MIB", "alStatCntlVC"),
    (1, "ALLOT-MIB", "alStatCntlUserInstance"),
)
if mibBuilder.loadTexts:
    alStatEntry.setStatus("current")
_AlStatLiveConn_Type = Counter32
_AlStatLiveConn_Object = MibTableColumn
alStatLiveConn = _AlStatLiveConn_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4, 2, 1, 5),
    _AlStatLiveConn_Type()
)
alStatLiveConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alStatLiveConn.setStatus("current")
_AlStatNewConn_Type = Counter32
_AlStatNewConn_Object = MibTableColumn
alStatNewConn = _AlStatNewConn_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4, 2, 1, 6),
    _AlStatNewConn_Type()
)
alStatNewConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alStatNewConn.setStatus("current")
_AlStatDropConn_Type = Counter32
_AlStatDropConn_Object = MibTableColumn
alStatDropConn = _AlStatDropConn_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4, 2, 1, 7),
    _AlStatDropConn_Type()
)
alStatDropConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alStatDropConn.setStatus("current")
_AlStatOctetsIn_Type = Counter64
_AlStatOctetsIn_Object = MibTableColumn
alStatOctetsIn = _AlStatOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4, 2, 1, 8),
    _AlStatOctetsIn_Type()
)
alStatOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alStatOctetsIn.setStatus("current")
_AlStatOctetsOut_Type = Counter64
_AlStatOctetsOut_Object = MibTableColumn
alStatOctetsOut = _AlStatOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4, 2, 1, 9),
    _AlStatOctetsOut_Type()
)
alStatOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alStatOctetsOut.setStatus("current")
_AlStatOctetsTotal_Type = Counter64
_AlStatOctetsTotal_Object = MibTableColumn
alStatOctetsTotal = _AlStatOctetsTotal_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4, 2, 1, 10),
    _AlStatOctetsTotal_Type()
)
alStatOctetsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alStatOctetsTotal.setStatus("current")
_AlStatPacketsIn_Type = Counter64
_AlStatPacketsIn_Object = MibTableColumn
alStatPacketsIn = _AlStatPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4, 2, 1, 11),
    _AlStatPacketsIn_Type()
)
alStatPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alStatPacketsIn.setStatus("current")
_AlStatPacketsOut_Type = Counter64
_AlStatPacketsOut_Object = MibTableColumn
alStatPacketsOut = _AlStatPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4, 2, 1, 12),
    _AlStatPacketsOut_Type()
)
alStatPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alStatPacketsOut.setStatus("current")
_AlStatPacketsTotal_Type = Counter64
_AlStatPacketsTotal_Object = MibTableColumn
alStatPacketsTotal = _AlStatPacketsTotal_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4, 2, 1, 13),
    _AlStatPacketsTotal_Type()
)
alStatPacketsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alStatPacketsTotal.setStatus("current")
_AlStatPipes_Type = Counter32
_AlStatPipes_Object = MibScalar
alStatPipes = _AlStatPipes_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4, 3),
    _AlStatPipes_Type()
)
alStatPipes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alStatPipes.setStatus("current")
_AlStatVCs_Type = Counter32
_AlStatVCs_Object = MibScalar
alStatVCs = _AlStatVCs_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4, 4),
    _AlStatVCs_Type()
)
alStatVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alStatVCs.setStatus("current")
_AlStatLines_Type = Counter32
_AlStatLines_Object = MibScalar
alStatLines = _AlStatLines_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4, 5),
    _AlStatLines_Type()
)
alStatLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alStatLines.setStatus("current")
_AlNumberEstConnections_Type = Counter32
_AlNumberEstConnections_Object = MibScalar
alNumberEstConnections = _AlNumberEstConnections_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4, 6),
    _AlNumberEstConnections_Type()
)
alNumberEstConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNumberEstConnections.setStatus("current")
_AlConnectionEstRate_Type = Counter32
_AlConnectionEstRate_Object = MibScalar
alConnectionEstRate = _AlConnectionEstRate_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4, 7),
    _AlConnectionEstRate_Type()
)
alConnectionEstRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alConnectionEstRate.setStatus("current")
_AlActiveSubscribers_Type = Counter32
_AlActiveSubscribers_Object = MibScalar
alActiveSubscribers = _AlActiveSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 4, 8),
    _AlActiveSubscribers_Type()
)
alActiveSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alActiveSubscribers.setStatus("current")
_AlAlerts_ObjectIdentity = ObjectIdentity
alAlerts = _AlAlerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5)
)
_AlDataSourceTable_Object = MibTable
alDataSourceTable = _AlDataSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 1)
)
if mibBuilder.loadTexts:
    alDataSourceTable.setStatus("current")
_AlDataSourceEntry_Object = MibTableRow
alDataSourceEntry = _AlDataSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 1, 1)
)
alDataSourceEntry.setIndexNames(
    (0, "ALLOT-MIB", "alDataSourceType"),
    (0, "ALLOT-MIB", "alDataSourcePriorityOrder"),
)
if mibBuilder.loadTexts:
    alDataSourceEntry.setStatus("current")


class _AlDataSourceType_Type(Integer32):
    """Custom type alDataSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dns", 1),
          ("dhcp", 2),
          ("ldap", 3),
          ("radius", 4),
          ("tftp", 5),
          ("ntp", 6))
    )


_AlDataSourceType_Type.__name__ = "Integer32"
_AlDataSourceType_Object = MibTableColumn
alDataSourceType = _AlDataSourceType_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 1, 1, 1),
    _AlDataSourceType_Type()
)
alDataSourceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alDataSourceType.setStatus("current")
_AlDataSourcePriorityOrder_Type = Unsigned32
_AlDataSourcePriorityOrder_Object = MibTableColumn
alDataSourcePriorityOrder = _AlDataSourcePriorityOrder_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 1, 1, 2),
    _AlDataSourcePriorityOrder_Type()
)
alDataSourcePriorityOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alDataSourcePriorityOrder.setStatus("current")
_AlDataSourceIPAddr_Type = IpAddress
_AlDataSourceIPAddr_Object = MibTableColumn
alDataSourceIPAddr = _AlDataSourceIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 1, 1, 3),
    _AlDataSourceIPAddr_Type()
)
alDataSourceIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alDataSourceIPAddr.setStatus("current")
_AlDataSourceDescr_Type = DisplayString
_AlDataSourceDescr_Object = MibTableColumn
alDataSourceDescr = _AlDataSourceDescr_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 1, 1, 4),
    _AlDataSourceDescr_Type()
)
alDataSourceDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alDataSourceDescr.setStatus("current")


class _AlDataSourceStatus_Type(Integer32):
    """Custom type alDataSourceStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("on", 2),
          ("off", 3))
    )


_AlDataSourceStatus_Type.__name__ = "Integer32"
_AlDataSourceStatus_Object = MibTableColumn
alDataSourceStatus = _AlDataSourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 1, 1, 5),
    _AlDataSourceStatus_Type()
)
alDataSourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDataSourceStatus.setStatus("current")
_AlDataSourceRowStatus_Type = RowStatus
_AlDataSourceRowStatus_Object = MibTableColumn
alDataSourceRowStatus = _AlDataSourceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 1, 1, 6),
    _AlDataSourceRowStatus_Type()
)
alDataSourceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alDataSourceRowStatus.setStatus("current")
_AlDataSourceLastChange_Type = TimeStamp
_AlDataSourceLastChange_Object = MibScalar
alDataSourceLastChange = _AlDataSourceLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 2),
    _AlDataSourceLastChange_Type()
)
alDataSourceLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDataSourceLastChange.setStatus("current")


class _AlSevereSoftwareProblem_Type(Integer32):
    """Custom type alSevereSoftwareProblem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              11,
              12,
              13,
              21)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("reboot", 2),
          ("processUp", 3),
          ("processDown", 4),
          ("processStuck", 5),
          ("picoCheckSuccess", 11),
          ("picoCheckFalure", 12),
          ("picoSaveFalure", 13),
          ("wrongTrapOrder", 21))
    )


_AlSevereSoftwareProblem_Type.__name__ = "Integer32"
_AlSevereSoftwareProblem_Object = MibScalar
alSevereSoftwareProblem = _AlSevereSoftwareProblem_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 3),
    _AlSevereSoftwareProblem_Type()
)
alSevereSoftwareProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSevereSoftwareProblem.setStatus("current")
_AlMemoryUsage_Type = Gauge32
_AlMemoryUsage_Object = MibScalar
alMemoryUsage = _AlMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 4),
    _AlMemoryUsage_Type()
)
alMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMemoryUsage.setStatus("current")
_AlDiskUsage_Type = Gauge32
_AlDiskUsage_Object = MibScalar
alDiskUsage = _AlDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 5),
    _AlDiskUsage_Type()
)
alDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDiskUsage.setStatus("current")
_AlTemperature_Type = Gauge32
_AlTemperature_Object = MibScalar
alTemperature = _AlTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 6),
    _AlTemperature_Type()
)
alTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTemperature.setStatus("current")
_AlAlertConfTable_Object = MibTable
alAlertConfTable = _AlAlertConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 7)
)
if mibBuilder.loadTexts:
    alAlertConfTable.setStatus("current")
_AlAlertConfEntry_Object = MibTableRow
alAlertConfEntry = _AlAlertConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 7, 1)
)
alAlertConfEntry.setIndexNames(
    (0, "ALLOT-MIB", "alAlertConfId"),
    (1, "ALLOT-MIB", "alAlertConfVariable"),
)
if mibBuilder.loadTexts:
    alAlertConfEntry.setStatus("current")
_AlAlertConfId_Type = Unsigned32
_AlAlertConfId_Object = MibTableColumn
alAlertConfId = _AlAlertConfId_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 7, 1, 1),
    _AlAlertConfId_Type()
)
alAlertConfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alAlertConfId.setStatus("current")
_AlAlertConfVariable_Type = VariablePointer
_AlAlertConfVariable_Object = MibTableColumn
alAlertConfVariable = _AlAlertConfVariable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 7, 1, 2),
    _AlAlertConfVariable_Type()
)
alAlertConfVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAlertConfVariable.setStatus("current")
_AlAlertConfValue_Type = Integer32
_AlAlertConfValue_Object = MibTableColumn
alAlertConfValue = _AlAlertConfValue_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 7, 1, 3),
    _AlAlertConfValue_Type()
)
alAlertConfValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAlertConfValue.setStatus("current")
_AlAlertConfThreshold_Type = Integer32
_AlAlertConfThreshold_Object = MibTableColumn
alAlertConfThreshold = _AlAlertConfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 7, 1, 4),
    _AlAlertConfThreshold_Type()
)
alAlertConfThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAlertConfThreshold.setStatus("current")
_AlAlertConfNormal_Type = Integer32
_AlAlertConfNormal_Object = MibTableColumn
alAlertConfNormal = _AlAlertConfNormal_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 7, 1, 5),
    _AlAlertConfNormal_Type()
)
alAlertConfNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAlertConfNormal.setStatus("current")
_AlAlertConfRegInterval_Type = Integer32
_AlAlertConfRegInterval_Object = MibTableColumn
alAlertConfRegInterval = _AlAlertConfRegInterval_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 7, 1, 6),
    _AlAlertConfRegInterval_Type()
)
alAlertConfRegInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAlertConfRegInterval.setStatus("current")
_AlAlertConfUnRegInterval_Type = Integer32
_AlAlertConfUnRegInterval_Object = MibTableColumn
alAlertConfUnRegInterval = _AlAlertConfUnRegInterval_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 7, 1, 7),
    _AlAlertConfUnRegInterval_Type()
)
alAlertConfUnRegInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAlertConfUnRegInterval.setStatus("current")


class _AlAlertConfThresholdDirection_Type(Integer32):
    """Custom type alAlertConfThresholdDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equal", 0),
          ("greater", 1),
          ("less", 2),
          ("notEqual", 3))
    )


_AlAlertConfThresholdDirection_Type.__name__ = "Integer32"
_AlAlertConfThresholdDirection_Object = MibTableColumn
alAlertConfThresholdDirection = _AlAlertConfThresholdDirection_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 7, 1, 8),
    _AlAlertConfThresholdDirection_Type()
)
alAlertConfThresholdDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAlertConfThresholdDirection.setStatus("current")
_AlAlertLastChange_Type = TimeStamp
_AlAlertLastChange_Object = MibScalar
alAlertLastChange = _AlAlertLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 8),
    _AlAlertLastChange_Type()
)
alAlertLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAlertLastChange.setStatus("current")
_AlLastAccessViolation_Type = TimeStamp
_AlLastAccessViolation_Object = MibScalar
alLastAccessViolation = _AlLastAccessViolation_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 9),
    _AlLastAccessViolation_Type()
)
alLastAccessViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLastAccessViolation.setStatus("current")
_AlAlertsTrapsEnable_Type = AlEnableDisable
_AlAlertsTrapsEnable_Object = MibScalar
alAlertsTrapsEnable = _AlAlertsTrapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 10),
    _AlAlertsTrapsEnable_Type()
)
alAlertsTrapsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alAlertsTrapsEnable.setStatus("current")
_AlDataSourceTrapEnable_Type = AlEnableDisable
_AlDataSourceTrapEnable_Object = MibScalar
alDataSourceTrapEnable = _AlDataSourceTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 11),
    _AlDataSourceTrapEnable_Type()
)
alDataSourceTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alDataSourceTrapEnable.setStatus("current")
_AlAccessViolationTrapEnable_Type = AlEnableDisable
_AlAccessViolationTrapEnable_Object = MibScalar
alAccessViolationTrapEnable = _AlAccessViolationTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 12),
    _AlAccessViolationTrapEnable_Type()
)
alAccessViolationTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alAccessViolationTrapEnable.setStatus("current")
_AllDOSAttackTable_Object = MibTable
allDOSAttackTable = _AllDOSAttackTable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 13)
)
if mibBuilder.loadTexts:
    allDOSAttackTable.setStatus("current")
_AllDOSAttackEntry_Object = MibTableRow
allDOSAttackEntry = _AllDOSAttackEntry_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 13, 1)
)
allDOSAttackEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ALLOT-MIB", "alDOSAttackType"),
)
if mibBuilder.loadTexts:
    allDOSAttackEntry.setStatus("current")


class _AlDOSAttackType_Type(Integer32):
    """Custom type alDOSAttackType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2),
          ("icmp", 3),
          ("otherIP", 4),
          ("nonIP", 5))
    )


_AlDOSAttackType_Type.__name__ = "Integer32"
_AlDOSAttackType_Object = MibTableColumn
alDOSAttackType = _AlDOSAttackType_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 13, 1, 1),
    _AlDOSAttackType_Type()
)
alDOSAttackType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alDOSAttackType.setStatus("current")
_AlDOSAttackPort_Type = Unsigned32
_AlDOSAttackPort_Object = MibTableColumn
alDOSAttackPort = _AlDOSAttackPort_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 13, 1, 2),
    _AlDOSAttackPort_Type()
)
alDOSAttackPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDOSAttackPort.setStatus("current")


class _AlDOSAttackStatus_Type(Integer32):
    """Custom type alDOSAttackStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("finish", 2))
    )


_AlDOSAttackStatus_Type.__name__ = "Integer32"
_AlDOSAttackStatus_Object = MibTableColumn
alDOSAttackStatus = _AlDOSAttackStatus_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 13, 1, 3),
    _AlDOSAttackStatus_Type()
)
alDOSAttackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDOSAttackStatus.setStatus("current")


class _AlDOSTrapEnable_Type(AlEnableDisable):
    """Custom type alDOSTrapEnable based on AlEnableDisable"""
    defaultValue = 1


_AlDOSTrapEnable_Type.__name__ = "AlEnableDisable"
_AlDOSTrapEnable_Object = MibScalar
alDOSTrapEnable = _AlDOSTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 14),
    _AlDOSTrapEnable_Type()
)
alDOSTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alDOSTrapEnable.setStatus("current")


class _AlCpuUsage_Type(Integer32):
    """Custom type alCpuUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AlCpuUsage_Type.__name__ = "Integer32"
_AlCpuUsage_Object = MibScalar
alCpuUsage = _AlCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 15),
    _AlCpuUsage_Type()
)
alCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCpuUsage.setStatus("current")
_AlLastMessage_Type = OctetString
_AlLastMessage_Object = MibScalar
alLastMessage = _AlLastMessage_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 16),
    _AlLastMessage_Type()
)
alLastMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLastMessage.setStatus("current")


class _AlCpuPicoUsage_Type(Integer32):
    """Custom type alCpuPicoUsage based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AlCpuPicoUsage_Type.__name__ = "Integer32"
_AlCpuPicoUsage_Object = MibScalar
alCpuPicoUsage = _AlCpuPicoUsage_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 17),
    _AlCpuPicoUsage_Type()
)
alCpuPicoUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCpuPicoUsage.setStatus("current")
_AlSensorTable_Object = MibTable
alSensorTable = _AlSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 18)
)
if mibBuilder.loadTexts:
    alSensorTable.setStatus("current")
_AlSensorEntry_Object = MibTableRow
alSensorEntry = _AlSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 18, 1)
)
alSensorEntry.setIndexNames(
    (0, "ALLOT-MIB", "alBoardId"),
    (0, "ALLOT-MIB", "alSensorId"),
)
if mibBuilder.loadTexts:
    alSensorEntry.setStatus("current")
_AlSensorId_Type = Unsigned32
_AlSensorId_Object = MibTableColumn
alSensorId = _AlSensorId_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 18, 1, 1),
    _AlSensorId_Type()
)
alSensorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alSensorId.setStatus("current")


class _AlSensorType_Type(Integer32):
    """Custom type alSensorType based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("temperature", 1),
          ("fan", 2),
          ("powerSupply", 3),
          ("cpu", 4),
          ("memory", 5),
          ("storage", 6),
          ("voltage", 7),
          ("telco", 8),
          ("picoCpu", 9),
          ("cer", 10),
          ("noc", 11),
          ("activeLines", 12),
          ("activePipes", 13),
          ("activeVcs", 14),
          ("registerSubscr", 15))
    )


_AlSensorType_Type.__name__ = "Integer32"
_AlSensorType_Object = MibTableColumn
alSensorType = _AlSensorType_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 18, 1, 2),
    _AlSensorType_Type()
)
alSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSensorType.setStatus("current")
_AlSensorRawValue_Type = Integer32
_AlSensorRawValue_Object = MibTableColumn
alSensorRawValue = _AlSensorRawValue_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 5, 18, 1, 3),
    _AlSensorRawValue_Type()
)
alSensorRawValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSensorRawValue.setStatus("current")
_AlLoadConfig_ObjectIdentity = ObjectIdentity
alLoadConfig = _AlLoadConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 5, 6)
)
_AlSaveConfig_Type = DisplayString
_AlSaveConfig_Object = MibScalar
alSaveConfig = _AlSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 6, 1),
    _AlSaveConfig_Type()
)
alSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alSaveConfig.setStatus("current")
_AlRestoreConfig_Type = DisplayString
_AlRestoreConfig_Object = MibScalar
alRestoreConfig = _AlRestoreConfig_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 6, 2),
    _AlRestoreConfig_Type()
)
alRestoreConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alRestoreConfig.setStatus("current")
_AlPoliciesStatusTable_Object = MibTable
alPoliciesStatusTable = _AlPoliciesStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 6, 3)
)
if mibBuilder.loadTexts:
    alPoliciesStatusTable.setStatus("current")
_AlPoliciesStatusEntry_Object = MibTableRow
alPoliciesStatusEntry = _AlPoliciesStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 6, 3, 1)
)
alPoliciesStatusEntry.setIndexNames(
    (0, "ALLOT-MIB", "alPolicyName"),
)
if mibBuilder.loadTexts:
    alPoliciesStatusEntry.setStatus("current")
_AlPolicyName_Type = OctetString
_AlPolicyName_Object = MibTableColumn
alPolicyName = _AlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 6, 3, 1, 1),
    _AlPolicyName_Type()
)
alPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPolicyName.setStatus("current")
_AlPolicyTimestamp_Type = DateAndTime
_AlPolicyTimestamp_Object = MibTableColumn
alPolicyTimestamp = _AlPolicyTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 6, 3, 1, 2),
    _AlPolicyTimestamp_Type()
)
alPolicyTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPolicyTimestamp.setStatus("current")


class _AlPolicyStatus_Type(Integer32):
    """Custom type alPolicyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2),
          ("doMakeActive", 3))
    )


_AlPolicyStatus_Type.__name__ = "Integer32"
_AlPolicyStatus_Object = MibTableColumn
alPolicyStatus = _AlPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2603, 5, 6, 3, 1, 3),
    _AlPolicyStatus_Type()
)
alPolicyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alPolicyStatus.setStatus("current")
_AlConf_ObjectIdentity = ObjectIdentity
alConf = _AlConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 6)
)
_AlGroups_ObjectIdentity = ObjectIdentity
alGroups = _AlGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 6, 1)
)
_AlCompls_ObjectIdentity = ObjectIdentity
alCompls = _AlCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 6, 2)
)

# Managed Objects groups

alGenericGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2603, 6, 1, 1)
)
alGenericGroup.setObjects(
      *(("ALLOT-MIB", "alBoxSerialNumber"),
        ("ALLOT-MIB", "alSoftwareVersion"),
        ("ALLOT-MIB", "alDateTime"),
        ("ALLOT-MIB", "alTimeZone"),
        ("ALLOT-MIB", "alConfigurationName"),
        ("ALLOT-MIB", "alMode"),
        ("ALLOT-MIB", "alPosIfEncapsulation"),
        ("ALLOT-MIB", "alSPTStatus"),
        ("ALLOT-MIB", "alLearningBridge"),
        ("ALLOT-MIB", "alHTTPConnectionMode"),
        ("ALLOT-MIB", "alTelnetAccess"),
        ("ALLOT-MIB", "alPingReply"),
        ("ALLOT-MIB", "alConnectionTimeout"),
        ("ALLOT-MIB", "alACDescr"),
        ("ALLOT-MIB", "alACRowStatus"),
        ("ALLOT-MIB", "alIfXMode"),
        ("ALLOT-MIB", "alIfXType"),
        ("ALLOT-MIB", "alGenericLastChangeVar"),
        ("ALLOT-MIB", "alGenericLastChangeIntVal"),
        ("ALLOT-MIB", "alGenericLastChangeTimestamp"),
        ("ALLOT-MIB", "alGenericConfigTrapEnable"),
        ("ALLOT-MIB", "alBackplaneVersion"),
        ("ALLOT-MIB", "alQoSIsEnabled"),
        ("ALLOT-MIB", "alQoSExpirationDateEnable"),
        ("ALLOT-MIB", "alCacheIsEnabled"),
        ("ALLOT-MIB", "alCacheExpirationDateEnable"),
        ("ALLOT-MIB", "alLoadBalancingIsEnabled"),
        ("ALLOT-MIB", "alLoadBalancingExpirationDateEnable"),
        ("ALLOT-MIB", "alActivationKey"),
        ("ALLOT-MIB", "alIfXSpeed"),
        ("ALLOT-MIB", "alLcdConfigEnable"),
        ("ALLOT-MIB", "alRebootRequest"),
        ("ALLOT-MIB", "alConnRouteNetMask"),
        ("ALLOT-MIB", "alConnRouteGateway"),
        ("ALLOT-MIB", "alConnRouteIfIndex"),
        ("ALLOT-MIB", "alConnRouteType"),
        ("ALLOT-MIB", "alConnRouteEntryStatus"),
        ("ALLOT-MIB", "alIpXNetMask"),
        ("ALLOT-MIB", "alIpXVlan"),
        ("ALLOT-MIB", "alIpXEntryStatus"),
        ("ALLOT-MIB", "alIfXOrder"),
        ("ALLOT-MIB", "alActivationModel"),
        ("ALLOT-MIB", "alLinePerPolicy"),
        ("ALLOT-MIB", "alPipePerPolicy"),
        ("ALLOT-MIB", "alVcPerPolicy"),
        ("ALLOT-MIB", "alMaxBandwidth"),
        ("ALLOT-MIB", "alMaxConnections"),
        ("ALLOT-MIB", "alHostname"),
        ("ALLOT-MIB", "alDomainName"),
        ("ALLOT-MIB", "alInBandGateway"),
        ("ALLOT-MIB", "alOutOfBandGateway"),
        ("ALLOT-MIB", "alPower"),
        ("ALLOT-MIB", "alFan"),
        ("ALLOT-MIB", "alEnhancedTcpSecurity"),
        ("ALLOT-MIB", "alDoubleSession"),
        ("ALLOT-MIB", "alSysExpirationDate"),
        ("ALLOT-MIB", "alPosIfCrc"),
        ("ALLOT-MIB", "alPosIfClocking"),
        ("ALLOT-MIB", "alPosIfScrambling"),
        ("ALLOT-MIB", "alPosIfFraming"),
        ("ALLOT-MIB", "alPosIfType"),
        ("ALLOT-MIB", "alBypass"),
        ("ALLOT-MIB", "alRedunduncyMode"),
        ("ALLOT-MIB", "alIpXAddr"),
        ("ALLOT-MIB", "alPosIfMtu"),
        ("ALLOT-MIB", "alIfXLabel"),
        ("ALLOT-MIB", "alIfXSupported"),
        ("ALLOT-MIB", "alSshSecurity"),
        ("ALLOT-MIB", "alGenericLastChangeStrVal"),
        ("ALLOT-MIB", "alGenericLastChangeAddrVal"),
        ("ALLOT-MIB", "alLTCollectionEnabled"),
        ("ALLOT-MIB", "alDeviceBWLimitsType"),
        ("ALLOT-MIB", "alDeviceBWLimitsOutbound"),
        ("ALLOT-MIB", "alDeviceBWLimitsInbound"),
        ("ALLOT-MIB", "alIfXActualMode"),
        ("ALLOT-MIB", "alIfXAction"),
        ("ALLOT-MIB", "alRemoteBypass"),
        ("ALLOT-MIB", "alRedundancyCap"),
        ("ALLOT-MIB", "alBypassUnit"),
        ("ALLOT-MIB", "alBypassSetting"),
        ("ALLOT-MIB", "alCocServerTimeOut"),
        ("ALLOT-MIB", "alCocServerRetries"),
        ("ALLOT-MIB", "alCocServerPeriod"),
        ("ALLOT-MIB", "alCocServiceTimeOut"),
        ("ALLOT-MIB", "alCocServiceRetries"),
        ("ALLOT-MIB", "alCocServicerPeriod"),
        ("ALLOT-MIB", "alCocTrackerMAC"),
        ("ALLOT-MIB", "alCocRedirectionMAC"),
        ("ALLOT-MIB", "alCocUseIp"),
        ("ALLOT-MIB", "alBoardType"),
        ("ALLOT-MIB", "alBoardSerialNumber"),
        ("ALLOT-MIB", "alBoardSoftwareVersion"),
        ("ALLOT-MIB", "alBoardHardwareVersion"),
        ("ALLOT-MIB", "alBoardSoftwareStatus"),
        ("ALLOT-MIB", "alBoardHWStatus"),
        ("ALLOT-MIB", "alCocRedirectionPort"),
        ("ALLOT-MIB", "alBaseVersion"),
        ("ALLOT-MIB", "alCurrentVersion"),
        ("ALLOT-MIB", "alLastUpdateStatus"),
        ("ALLOT-MIB", "alInternalDispatchMode"),
        ("ALLOT-MIB", "alInternalMinDevNum"),
        ("ALLOT-MIB", "alInternalRedundancyDevNum"),
        ("ALLOT-MIB", "alInternalActiveDevNum"),
        ("ALLOT-MIB", "alInternalRateLimit"),
        ("ALLOT-MIB", "alWebUpdateIsEnabled"),
        ("ALLOT-MIB", "alWebUpdateExpirationDateEnable"),
        ("ALLOT-MIB", "alUDSState"),
        ("ALLOT-MIB", "alAsymmetricGroupId"),
        ("ALLOT-MIB", "alAsymmetricOwnDeviceId"),
        ("ALLOT-MIB", "alAsymmetricHealthCheck"),
        ("ALLOT-MIB", "alAsymmetricTransportType"),
        ("ALLOT-MIB", "alAsymmetricControlVLAN"),
        ("ALLOT-MIB", "alAsymmetricMAC"),
        ("ALLOT-MIB", "alAsymmetricIP"),
        ("ALLOT-MIB", "alAsymmetricHealthCheckStatus"),
        ("ALLOT-MIB", "alAsymmetricEntryStatus"),
        ("ALLOT-MIB", "alAsymmetricEnable"),
        ("ALLOT-MIB", "alAsymmetricPort"),
        ("ALLOT-MIB", "alUrlFOperationMode"),
        ("ALLOT-MIB", "alUrlFAction"),
        ("ALLOT-MIB", "alUrlFPortal"),
        ("ALLOT-MIB", "alUrlFLastUpdateStatus"),
        ("ALLOT-MIB", "alUrlMOperatonMode"),
        ("ALLOT-MIB", "alCaptivePortalRedirectionTechnique"),
        ("ALLOT-MIB", "alVoipReportingActivation"),
        ("ALLOT-MIB", "alSPSensorActivation"),
        ("ALLOT-MIB", "alIfXUsage"),
        ("ALLOT-MIB", "alIfXSwitchId"),
        ("ALLOT-MIB", "alIfXSwitchPort"),
        ("ALLOT-MIB", "alIfXUsageCapability"),
        ("ALLOT-MIB", "alLicenseAttrType"),
        ("ALLOT-MIB", "alLicenseLimitType"),
        ("ALLOT-MIB", "alLicenseAttrName"),
        ("ALLOT-MIB", "alLimitValue"),
        ("ALLOT-MIB", "alLicenseStatus"),
        ("ALLOT-MIB", "alLicenseIsCurrValue"),
        ("ALLOT-MIB", "alLicenseCurrValue"),
        ("ALLOT-MIB", "alLicenseEventType"),
        ("ALLOT-MIB", "alBoardTemperatureRange"),
        ("ALLOT-MIB", "alIfXThroughputTX"),
        ("ALLOT-MIB", "alIfXThroughputRX"),
        ("ALLOT-MIB", "alIfXPacketPerSecondTX"),
        ("ALLOT-MIB", "alIfXPacketPerSecondRX"),
        ("ALLOT-MIB", "alIfXSTPStatus"),
        ("ALLOT-MIB", "alIfXSTPSupport"),
        ("ALLOT-MIB", "alFupProtocolVersion"),
        ("ALLOT-MIB", "alPDPIState"),
        ("ALLOT-MIB", "alIPv6State"),
        ("ALLOT-MIB", "alSelectiveBypassVlanGroup"),
        ("ALLOT-MIB", "alSelectiveBypassActivation"),
        ("ALLOT-MIB", "alTetherDetectState"),
        ("ALLOT-MIB", "alCaptivePortalPassPhrase"))
)
if mibBuilder.loadTexts:
    alGenericGroup.setStatus("current")

alProvisioningGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2603, 6, 1, 2)
)
alProvisioningGroup.setObjects(
      *(("ALLOT-MIB", "alCatalogsLastChangeTimestamp"),
        ("ALLOT-MIB", "alCatalogsLastChangeRequest"),
        ("ALLOT-MIB", "alCatalogName"),
        ("ALLOT-MIB", "alCatalogLastCommand"),
        ("ALLOT-MIB", "alCatalogTimestamp"),
        ("ALLOT-MIB", "alCatalogData"),
        ("ALLOT-MIB", "alCatalogCheckSum"),
        ("ALLOT-MIB", "alCatalogInstanceStatus"),
        ("ALLOT-MIB", "alLineLastChange"),
        ("ALLOT-MIB", "alLineLastCommand"),
        ("ALLOT-MIB", "alLineTimestamp"),
        ("ALLOT-MIB", "alLineData"),
        ("ALLOT-MIB", "alLineCheckSum"),
        ("ALLOT-MIB", "alLineInstanceStatus"),
        ("ALLOT-MIB", "alPipeLastChange"),
        ("ALLOT-MIB", "alPipeLastCommand"),
        ("ALLOT-MIB", "alPipeTimestamp"),
        ("ALLOT-MIB", "alPipeData"),
        ("ALLOT-MIB", "alPipeCheckSum"),
        ("ALLOT-MIB", "alPipeStatus"),
        ("ALLOT-MIB", "alVCLastChange"),
        ("ALLOT-MIB", "alVCLastCommand"),
        ("ALLOT-MIB", "alVCTimestamp"),
        ("ALLOT-MIB", "alVCData"),
        ("ALLOT-MIB", "alVCCheckSum"),
        ("ALLOT-MIB", "alVCStatus"),
        ("ALLOT-MIB", "alLineConfTrapEnable"),
        ("ALLOT-MIB", "alPipeIsTemplate"),
        ("ALLOT-MIB", "alVCIsTemplate"),
        ("ALLOT-MIB", "alCatalogLastChangeOrigin"),
        ("ALLOT-MIB", "alLineLastChangeOrigin"),
        ("ALLOT-MIB", "alPipeLastChangeOrigin"),
        ("ALLOT-MIB", "alVcConfTrapEnable"),
        ("ALLOT-MIB", "alVCLastChangeOrigin"),
        ("ALLOT-MIB", "alPipeConfTrapEnable"),
        ("ALLOT-MIB", "alPolicyModificationTag"))
)
if mibBuilder.loadTexts:
    alProvisioningGroup.setStatus("current")

alStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2603, 6, 1, 3)
)
alStatisticsGroup.setObjects(
      *(("ALLOT-MIB", "alStatLiveConn"),
        ("ALLOT-MIB", "alStatNewConn"),
        ("ALLOT-MIB", "alStatDropConn"),
        ("ALLOT-MIB", "alStatOctetsIn"),
        ("ALLOT-MIB", "alStatOctetsOut"),
        ("ALLOT-MIB", "alStatOctetsTotal"),
        ("ALLOT-MIB", "alStatPacketsIn"),
        ("ALLOT-MIB", "alStatPacketsOut"),
        ("ALLOT-MIB", "alStatPacketsTotal"),
        ("ALLOT-MIB", "alStatCntlIsTemplate"),
        ("ALLOT-MIB", "alStatCntlStartedAt"),
        ("ALLOT-MIB", "alStatCntlStatus"),
        ("ALLOT-MIB", "alStatCntlIsView"),
        ("ALLOT-MIB", "alStatCntlIsAlert"),
        ("ALLOT-MIB", "alStatPipes"),
        ("ALLOT-MIB", "alStatVCs"),
        ("ALLOT-MIB", "alStatLines"),
        ("ALLOT-MIB", "alNumberEstConnections"),
        ("ALLOT-MIB", "alConnectionEstRate"),
        ("ALLOT-MIB", "alActiveSubscribers"))
)
if mibBuilder.loadTexts:
    alStatisticsGroup.setStatus("current")

alAlertsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2603, 6, 1, 4)
)
alAlertsGroup.setObjects(
      *(("ALLOT-MIB", "alDataSourceIPAddr"),
        ("ALLOT-MIB", "alDataSourceStatus"),
        ("ALLOT-MIB", "alDataSourceDescr"),
        ("ALLOT-MIB", "alSevereSoftwareProblem"),
        ("ALLOT-MIB", "alDataSourceLastChange"),
        ("ALLOT-MIB", "alMemoryUsage"),
        ("ALLOT-MIB", "alDiskUsage"),
        ("ALLOT-MIB", "alTemperature"),
        ("ALLOT-MIB", "alAlertConfVariable"),
        ("ALLOT-MIB", "alAlertConfValue"),
        ("ALLOT-MIB", "alAlertConfThreshold"),
        ("ALLOT-MIB", "alAlertConfNormal"),
        ("ALLOT-MIB", "alAlertConfRegInterval"),
        ("ALLOT-MIB", "alAlertConfUnRegInterval"),
        ("ALLOT-MIB", "alAlertConfThresholdDirection"),
        ("ALLOT-MIB", "alAlertLastChange"),
        ("ALLOT-MIB", "alAlertsTrapsEnable"),
        ("ALLOT-MIB", "alLastAccessViolation"),
        ("ALLOT-MIB", "alDataSourceTrapEnable"),
        ("ALLOT-MIB", "alAccessViolationTrapEnable"),
        ("ALLOT-MIB", "alDataSourceRowStatus"),
        ("ALLOT-MIB", "alDOSAttackPort"),
        ("ALLOT-MIB", "alDOSAttackStatus"),
        ("ALLOT-MIB", "alDOSTrapEnable"),
        ("ALLOT-MIB", "alCpuUsage"),
        ("ALLOT-MIB", "alLastMessage"),
        ("ALLOT-MIB", "alCpuPicoUsage"),
        ("ALLOT-MIB", "alSensorRawValue"),
        ("ALLOT-MIB", "alSensorType"))
)
if mibBuilder.loadTexts:
    alAlertsGroup.setStatus("current")

alLoadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2603, 6, 1, 5)
)
alLoadGroup.setObjects(
      *(("ALLOT-MIB", "alSaveConfig"),
        ("ALLOT-MIB", "alPolicyName"),
        ("ALLOT-MIB", "alPolicyTimestamp"),
        ("ALLOT-MIB", "alPolicyStatus"),
        ("ALLOT-MIB", "alRestoreConfig"))
)
if mibBuilder.loadTexts:
    alLoadGroup.setStatus("current")


# Notification objects

alDeviceConfChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 0, 1)
)
alDeviceConfChangeTrap.setObjects(
      *(("ALLOT-MIB", "alGenericLastChangeVar"),
        ("ALLOT-MIB", "alGenericLastChangeIntVal"),
        ("ALLOT-MIB", "alGenericLastChangeStrVal"),
        ("ALLOT-MIB", "alGenericLastChangeAddrVal"))
)
if mibBuilder.loadTexts:
    alDeviceConfChangeTrap.setStatus(
        "current"
    )

alCatalogConfChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 0, 2)
)
alCatalogConfChangeTrap.setObjects(
      *(("ALLOT-MIB", "alCatalogLastCommand"),
        ("ALLOT-MIB", "alCatalogLastChangeOrigin"))
)
if mibBuilder.loadTexts:
    alCatalogConfChangeTrap.setStatus(
        "current"
    )

alLineConfChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 0, 3)
)
alLineConfChangeTrap.setObjects(
      *(("ALLOT-MIB", "alLineLastCommand"),
        ("ALLOT-MIB", "alLineLastChangeOrigin"))
)
if mibBuilder.loadTexts:
    alLineConfChangeTrap.setStatus(
        "current"
    )

alPipeConfChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 0, 4)
)
alPipeConfChangeTrap.setObjects(
      *(("ALLOT-MIB", "alPipeLastCommand"),
        ("ALLOT-MIB", "alPipeLastChangeOrigin"))
)
if mibBuilder.loadTexts:
    alPipeConfChangeTrap.setStatus(
        "current"
    )

alVCConfChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 0, 5)
)
alVCConfChangeTrap.setObjects(
      *(("ALLOT-MIB", "alVCLastCommand"),
        ("ALLOT-MIB", "alVCLastChangeOrigin"))
)
if mibBuilder.loadTexts:
    alVCConfChangeTrap.setStatus(
        "current"
    )

alAlertRisingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 0, 6)
)
alAlertRisingTrap.setObjects(
      *(("ALLOT-MIB", "alAlertConfVariable"),
        ("ALLOT-MIB", "alAlertConfValue"),
        ("ALLOT-MIB", "alAlertConfThreshold"),
        ("ALLOT-MIB", "alAlertConfRegInterval"))
)
if mibBuilder.loadTexts:
    alAlertRisingTrap.setStatus(
        "current"
    )

alAlertFallingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 0, 7)
)
alAlertFallingTrap.setObjects(
      *(("ALLOT-MIB", "alAlertConfVariable"),
        ("ALLOT-MIB", "alAlertConfValue"),
        ("ALLOT-MIB", "alAlertConfNormal"),
        ("ALLOT-MIB", "alAlertConfUnRegInterval"))
)
if mibBuilder.loadTexts:
    alAlertFallingTrap.setStatus(
        "current"
    )

alDosAttackOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 0, 8)
)
alDosAttackOnTrap.setObjects(
    ("ALLOT-MIB", "alDOSAttackStatus")
)
if mibBuilder.loadTexts:
    alDosAttackOnTrap.setStatus(
        "current"
    )

alDosAttackOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 0, 9)
)
alDosAttackOffTrap.setObjects(
    ("ALLOT-MIB", "alDOSAttackStatus")
)
if mibBuilder.loadTexts:
    alDosAttackOffTrap.setStatus(
        "current"
    )

alDataSourceDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 0, 10)
)
alDataSourceDownTrap.setObjects(
      *(("ALLOT-MIB", "alDataSourceIPAddr"),
        ("ALLOT-MIB", "alDataSourceType"))
)
if mibBuilder.loadTexts:
    alDataSourceDownTrap.setStatus(
        "current"
    )

alDataSourceUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 0, 11)
)
alDataSourceUpTrap.setObjects(
      *(("ALLOT-MIB", "alDataSourceIPAddr"),
        ("ALLOT-MIB", "alDataSourceType"))
)
if mibBuilder.loadTexts:
    alDataSourceUpTrap.setStatus(
        "current"
    )

alSoftwareProblemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 0, 12)
)
alSoftwareProblemTrap.setObjects(
      *(("ALLOT-MIB", "alSevereSoftwareProblem"),
        ("ALLOT-MIB", "alLastMessage"))
)
if mibBuilder.loadTexts:
    alSoftwareProblemTrap.setStatus(
        "current"
    )

alAccessViolationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 0, 13)
)
alAccessViolationTrap.setObjects(
    ("ALLOT-MIB", "alLastMessage")
)
if mibBuilder.loadTexts:
    alAccessViolationTrap.setStatus(
        "current"
    )

alIpAddrConfChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 0, 14)
)
alIpAddrConfChangeTrap.setObjects(
      *(("ALLOT-MIB", "alIpXEntryStatus"),
        ("ALLOT-MIB", "alIpXAddr"))
)
if mibBuilder.loadTexts:
    alIpAddrConfChangeTrap.setStatus(
        "current"
    )

alConnRouteConfChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 0, 15)
)
alConnRouteConfChangeTrap.setObjects(
      *(("ALLOT-MIB", "alConnRouteEntryStatus"),
        ("ALLOT-MIB", "alConnRouteIfIndex"))
)
if mibBuilder.loadTexts:
    alConnRouteConfChangeTrap.setStatus(
        "current"
    )

alDeviceStatusUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 0, 16)
)
alDeviceStatusUpTrap.setObjects(
      *(("ALLOT-MIB", "alGenericLastChangeVar"),
        ("ALLOT-MIB", "alGenericLastChangeIntVal"))
)
if mibBuilder.loadTexts:
    alDeviceStatusUpTrap.setStatus(
        "current"
    )

alDeviceStatusDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 0, 17)
)
alDeviceStatusDownTrap.setObjects(
      *(("ALLOT-MIB", "alGenericLastChangeVar"),
        ("ALLOT-MIB", "alGenericLastChangeIntVal"))
)
if mibBuilder.loadTexts:
    alDeviceStatusDownTrap.setStatus(
        "current"
    )

alApplicationInfoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 0, 18)
)
alApplicationInfoTrap.setObjects(
    ("ALLOT-MIB", "alLastMessage")
)
if mibBuilder.loadTexts:
    alApplicationInfoTrap.setStatus(
        "current"
    )

alBoardStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 0, 19)
)
alBoardStatusChangeTrap.setObjects(
      *(("ALLOT-MIB", "alBoardType"),
        ("ALLOT-MIB", "alBoardSoftwareStatus"),
        ("ALLOT-MIB", "alBoardHWStatus"))
)
if mibBuilder.loadTexts:
    alBoardStatusChangeTrap.setStatus(
        "current"
    )

alWebUpdateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 0, 20)
)
alWebUpdateTrap.setObjects(
      *(("ALLOT-MIB", "alCurrentVersion"),
        ("ALLOT-MIB", "alLastUpdateStatus"))
)
if mibBuilder.loadTexts:
    alWebUpdateTrap.setStatus(
        "current"
    )

alAsymmetricRemoteDeviceConfTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 0, 21)
)
alAsymmetricRemoteDeviceConfTrap.setObjects(
      *(("ALLOT-MIB", "alAsymmetricGroupId"),
        ("ALLOT-MIB", "alAsymmetricEntryStatus"))
)
if mibBuilder.loadTexts:
    alAsymmetricRemoteDeviceConfTrap.setStatus(
        "current"
    )

alAsymmetricRemoteDeviceStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 0, 22)
)
alAsymmetricRemoteDeviceStatusTrap.setObjects(
      *(("ALLOT-MIB", "alAsymmetricGroupId"),
        ("ALLOT-MIB", "alAsymmetricOwnDeviceId"),
        ("ALLOT-MIB", "alAsymmetricHealthCheckStatus"))
)
if mibBuilder.loadTexts:
    alAsymmetricRemoteDeviceStatusTrap.setStatus(
        "current"
    )

alLicenseWarnEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 0, 23)
)
alLicenseWarnEventTrap.setObjects(
      *(("ALLOT-MIB", "alLicenseAttrType"),
        ("ALLOT-MIB", "alLicenseLimitType"),
        ("ALLOT-MIB", "alLicenseEventType"),
        ("ALLOT-MIB", "alLastMessage"))
)
if mibBuilder.loadTexts:
    alLicenseWarnEventTrap.setStatus(
        "current"
    )

alLicenseCritEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 0, 24)
)
alLicenseCritEventTrap.setObjects(
      *(("ALLOT-MIB", "alLicenseAttrType"),
        ("ALLOT-MIB", "alLicenseLimitType"),
        ("ALLOT-MIB", "alLicenseEventType"),
        ("ALLOT-MIB", "alLastMessage"))
)
if mibBuilder.loadTexts:
    alLicenseCritEventTrap.setStatus(
        "current"
    )

alBoardTemperatureStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 0, 25)
)
alBoardTemperatureStatusTrap.setObjects(
      *(("ALLOT-MIB", "alBoardType"),
        ("ALLOT-MIB", "alBoardTemperatureRange"))
)
if mibBuilder.loadTexts:
    alBoardTemperatureStatusTrap.setStatus(
        "current"
    )

alURLFilteringUpdateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 0, 26)
)
alURLFilteringUpdateTrap.setObjects(
    ("ALLOT-MIB", "alUrlFLastUpdateStatus")
)
if mibBuilder.loadTexts:
    alURLFilteringUpdateTrap.setStatus(
        "current"
    )


# Notifications groups

alEventsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2603, 6, 1, 6)
)
alEventsGroup.setObjects(
      *(("ALLOT-MIB", "alDeviceConfChangeTrap"),
        ("ALLOT-MIB", "alCatalogConfChangeTrap"),
        ("ALLOT-MIB", "alLineConfChangeTrap"),
        ("ALLOT-MIB", "alPipeConfChangeTrap"),
        ("ALLOT-MIB", "alVCConfChangeTrap"),
        ("ALLOT-MIB", "alAlertRisingTrap"),
        ("ALLOT-MIB", "alAlertFallingTrap"),
        ("ALLOT-MIB", "alDosAttackOnTrap"),
        ("ALLOT-MIB", "alDosAttackOffTrap"),
        ("ALLOT-MIB", "alDataSourceDownTrap"),
        ("ALLOT-MIB", "alDataSourceUpTrap"),
        ("ALLOT-MIB", "alSoftwareProblemTrap"),
        ("ALLOT-MIB", "alAccessViolationTrap"),
        ("ALLOT-MIB", "alIpAddrConfChangeTrap"),
        ("ALLOT-MIB", "alConnRouteConfChangeTrap"),
        ("ALLOT-MIB", "alDeviceStatusUpTrap"),
        ("ALLOT-MIB", "alDeviceStatusDownTrap"),
        ("ALLOT-MIB", "alApplicationInfoTrap"),
        ("ALLOT-MIB", "alBoardStatusChangeTrap"),
        ("ALLOT-MIB", "alWebUpdateTrap"),
        ("ALLOT-MIB", "alAsymmetricRemoteDeviceConfTrap"),
        ("ALLOT-MIB", "alAsymmetricRemoteDeviceStatusTrap"),
        ("ALLOT-MIB", "alLicenseWarnEventTrap"),
        ("ALLOT-MIB", "alLicenseCritEventTrap"),
        ("ALLOT-MIB", "alBoardTemperatureStatusTrap"),
        ("ALLOT-MIB", "alURLFilteringUpdateTrap"))
)
if mibBuilder.loadTexts:
    alEventsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2603, 6, 2, 1)
)
alCompliance.setObjects(
      *(("ALLOT-MIB", "alGenericGroup"),
        ("ALLOT-MIB", "alProvisioningGroup"),
        ("ALLOT-MIB", "alStatisticsGroup"),
        ("ALLOT-MIB", "alAlertsGroup"),
        ("ALLOT-MIB", "alEventsGroup"),
        ("ALLOT-MIB", "alLoadGroup"))
)
if mibBuilder.loadTexts:
    alCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALLOT-MIB",
    **{"AlActiveStandbyStatus": AlActiveStandbyStatus,
       "AlConfigCommand": AlConfigCommand,
       "AlEnableDisable": AlEnableDisable,
       "AlEnableDisableNA": AlEnableDisableNA,
       "AlInstanceStatus": AlInstanceStatus,
       "AlUrlOperationMode": AlUrlOperationMode,
       "alRegMIB": alRegMIB,
       "alEvents": alEvents,
       "alDeviceConfChangeTrap": alDeviceConfChangeTrap,
       "alCatalogConfChangeTrap": alCatalogConfChangeTrap,
       "alLineConfChangeTrap": alLineConfChangeTrap,
       "alPipeConfChangeTrap": alPipeConfChangeTrap,
       "alVCConfChangeTrap": alVCConfChangeTrap,
       "alAlertRisingTrap": alAlertRisingTrap,
       "alAlertFallingTrap": alAlertFallingTrap,
       "alDosAttackOnTrap": alDosAttackOnTrap,
       "alDosAttackOffTrap": alDosAttackOffTrap,
       "alDataSourceDownTrap": alDataSourceDownTrap,
       "alDataSourceUpTrap": alDataSourceUpTrap,
       "alSoftwareProblemTrap": alSoftwareProblemTrap,
       "alAccessViolationTrap": alAccessViolationTrap,
       "alIpAddrConfChangeTrap": alIpAddrConfChangeTrap,
       "alConnRouteConfChangeTrap": alConnRouteConfChangeTrap,
       "alDeviceStatusUpTrap": alDeviceStatusUpTrap,
       "alDeviceStatusDownTrap": alDeviceStatusDownTrap,
       "alApplicationInfoTrap": alApplicationInfoTrap,
       "alBoardStatusChangeTrap": alBoardStatusChangeTrap,
       "alWebUpdateTrap": alWebUpdateTrap,
       "alAsymmetricRemoteDeviceConfTrap": alAsymmetricRemoteDeviceConfTrap,
       "alAsymmetricRemoteDeviceStatusTrap": alAsymmetricRemoteDeviceStatusTrap,
       "alLicenseWarnEventTrap": alLicenseWarnEventTrap,
       "alLicenseCritEventTrap": alLicenseCritEventTrap,
       "alBoardTemperatureStatusTrap": alBoardTemperatureStatusTrap,
       "alURLFilteringUpdateTrap": alURLFilteringUpdateTrap,
       "alActivation": alActivation,
       "alActivationKey": alActivationKey,
       "alActivationModel": alActivationModel,
       "alSysExpirationDate": alSysExpirationDate,
       "alQoSIsEnabled": alQoSIsEnabled,
       "alQoSExpirationDateEnable": alQoSExpirationDateEnable,
       "alCacheIsEnabled": alCacheIsEnabled,
       "alCacheExpirationDateEnable": alCacheExpirationDateEnable,
       "alLoadBalancingIsEnabled": alLoadBalancingIsEnabled,
       "alLoadBalancingExpirationDateEnable": alLoadBalancingExpirationDateEnable,
       "alActivationLimits": alActivationLimits,
       "alLinePerPolicy": alLinePerPolicy,
       "alPipePerPolicy": alPipePerPolicy,
       "alVcPerPolicy": alVcPerPolicy,
       "alMaxBandwidth": alMaxBandwidth,
       "alMaxConnections": alMaxConnections,
       "alLTCollectionEnabled": alLTCollectionEnabled,
       "alWebUpdateIsEnabled": alWebUpdateIsEnabled,
       "alWebUpdateExpirationDateEnable": alWebUpdateExpirationDateEnable,
       "alLicenseInfoTable": alLicenseInfoTable,
       "alLicenseInfoEntry": alLicenseInfoEntry,
       "alLicenseAttrType": alLicenseAttrType,
       "alLicenseLimitType": alLicenseLimitType,
       "alLicenseAttrName": alLicenseAttrName,
       "alLimitValue": alLimitValue,
       "alLicenseStatus": alLicenseStatus,
       "alLicenseIsCurrValue": alLicenseIsCurrValue,
       "alLicenseCurrValue": alLicenseCurrValue,
       "alLicenseEventType": alLicenseEventType,
       "alObjects": alObjects,
       "alProducts": alProducts,
       "alAC200": alAC200,
       "alAC400": alAC400,
       "alAC800": alAC800,
       "alAC1000": alAC1000,
       "alAC2500": alAC2500,
       "alMediationDevice": alMediationDevice,
       "alSG20": alSG20,
       "alAC10000": alAC10000,
       "alACSigma": alACSigma,
       "alAC5K": alAC5K,
       "alAC3K": alAC3K,
       "alAC10K": alAC10K,
       "alAC1K": alAC1K,
       "alACSigmaE14": alACSigmaE14,
       "alAC500": alAC500,
       "alACSigmaE6": alACSigmaE6,
       "alGeneric": alGeneric,
       "alConfigurationName": alConfigurationName,
       "alDoubleSession": alDoubleSession,
       "alGeneralSystem": alGeneralSystem,
       "alDateTime": alDateTime,
       "alTimeZone": alTimeZone,
       "alIfXTable": alIfXTable,
       "alIfXEntry": alIfXEntry,
       "alIfXMode": alIfXMode,
       "alIfXType": alIfXType,
       "alIfXSpeed": alIfXSpeed,
       "alIfXOrder": alIfXOrder,
       "alIfXLabel": alIfXLabel,
       "alIfXSupported": alIfXSupported,
       "alIfXActualMode": alIfXActualMode,
       "alIfXAction": alIfXAction,
       "alIfXUsage": alIfXUsage,
       "alIfXSwitchId": alIfXSwitchId,
       "alIfXSwitchPort": alIfXSwitchPort,
       "alIfXUsageCapability": alIfXUsageCapability,
       "alIfXThroughputTX": alIfXThroughputTX,
       "alIfXThroughputRX": alIfXThroughputRX,
       "alIfXPacketPerSecondTX": alIfXPacketPerSecondTX,
       "alIfXPacketPerSecondRX": alIfXPacketPerSecondRX,
       "alIfXSTPStatus": alIfXSTPStatus,
       "alIfXSTPSupport": alIfXSTPSupport,
       "alSystemNetwork": alSystemNetwork,
       "alHostname": alHostname,
       "alDomainName": alDomainName,
       "alInBandGateway": alInBandGateway,
       "alOutOfBandGateway": alOutOfBandGateway,
       "alConnRouteTable": alConnRouteTable,
       "alConnRouteEntry": alConnRouteEntry,
       "alConnRouteAddress": alConnRouteAddress,
       "alConnRouteNetMask": alConnRouteNetMask,
       "alConnRouteGateway": alConnRouteGateway,
       "alConnRouteIfIndex": alConnRouteIfIndex,
       "alConnRouteType": alConnRouteType,
       "alConnRouteEntryStatus": alConnRouteEntryStatus,
       "alSystemStatus": alSystemStatus,
       "alBypassSetting": alBypassSetting,
       "alPower": alPower,
       "alFan": alFan,
       "alRemoteBypass": alRemoteBypass,
       "alBypass": alBypass,
       "alSystemSecurity": alSystemSecurity,
       "alHTTPConnectionMode": alHTTPConnectionMode,
       "alTelnetAccess": alTelnetAccess,
       "alPingReply": alPingReply,
       "alEnhancedTcpSecurity": alEnhancedTcpSecurity,
       "alLcdConfigEnable": alLcdConfigEnable,
       "alConnectionTimeout": alConnectionTimeout,
       "alACTable": alACTable,
       "alACEntry": alACEntry,
       "alACIPAddr": alACIPAddr,
       "alACDescr": alACDescr,
       "alACRowStatus": alACRowStatus,
       "alSshSecurity": alSshSecurity,
       "alIpXAddrTable": alIpXAddrTable,
       "alIpXAddrEntry": alIpXAddrEntry,
       "alIpXAddr": alIpXAddr,
       "alIpXNetMask": alIpXNetMask,
       "alIpXVlan": alIpXVlan,
       "alIpXEntryStatus": alIpXEntryStatus,
       "alMode": alMode,
       "alLearningBridge": alLearningBridge,
       "alSPTStatus": alSPTStatus,
       "alRedunduncyMode": alRedunduncyMode,
       "alBoxSerialNumber": alBoxSerialNumber,
       "alSoftwareVersion": alSoftwareVersion,
       "alBackplaneVersion": alBackplaneVersion,
       "alPosIfTable": alPosIfTable,
       "alPosIfEntry": alPosIfEntry,
       "alPosIfIndex": alPosIfIndex,
       "alPosIfType": alPosIfType,
       "alPosIfFraming": alPosIfFraming,
       "alPosIfCrc": alPosIfCrc,
       "alPosIfClocking": alPosIfClocking,
       "alPosIfScrambling": alPosIfScrambling,
       "alPosIfEncapsulation": alPosIfEncapsulation,
       "alPosIfMtu": alPosIfMtu,
       "alRedundancyCap": alRedundancyCap,
       "alBypassUnit": alBypassUnit,
       "alDeviceBWLimits": alDeviceBWLimits,
       "alDeviceBWLimitsType": alDeviceBWLimitsType,
       "alDeviceBWLimitsOutbound": alDeviceBWLimitsOutbound,
       "alDeviceBWLimitsInbound": alDeviceBWLimitsInbound,
       "alSystemCOC": alSystemCOC,
       "alCocServerTimeOut": alCocServerTimeOut,
       "alCocServerRetries": alCocServerRetries,
       "alCocServerPeriod": alCocServerPeriod,
       "alCocServiceTimeOut": alCocServiceTimeOut,
       "alCocServiceRetries": alCocServiceRetries,
       "alCocServicerPeriod": alCocServicerPeriod,
       "alCocTrackerMAC": alCocTrackerMAC,
       "alCocRedirectionMAC": alCocRedirectionMAC,
       "alCocUseIp": alCocUseIp,
       "alCocRedirectionPort": alCocRedirectionPort,
       "alInternalRedundancy": alInternalRedundancy,
       "alBoardTable": alBoardTable,
       "alBoardEntry": alBoardEntry,
       "alBoardId": alBoardId,
       "alBoardType": alBoardType,
       "alBoardSerialNumber": alBoardSerialNumber,
       "alBoardSoftwareVersion": alBoardSoftwareVersion,
       "alBoardHardwareVersion": alBoardHardwareVersion,
       "alBoardSoftwareStatus": alBoardSoftwareStatus,
       "alBoardHWStatus": alBoardHWStatus,
       "alBoardTemperatureRange": alBoardTemperatureRange,
       "alInternalDispatchMode": alInternalDispatchMode,
       "alInternalMinDevNum": alInternalMinDevNum,
       "alInternalRedundancyDevNum": alInternalRedundancyDevNum,
       "alInternalActiveDevNum": alInternalActiveDevNum,
       "alInternalRateLimit": alInternalRateLimit,
       "alWebUpdate": alWebUpdate,
       "alBaseVersion": alBaseVersion,
       "alCurrentVersion": alCurrentVersion,
       "alLastUpdateStatus": alLastUpdateStatus,
       "alUserDefinedSignature": alUserDefinedSignature,
       "alUDSState": alUDSState,
       "alAsymmetric": alAsymmetric,
       "alAsymmetricGroupId": alAsymmetricGroupId,
       "alAsymmetricOwnDeviceId": alAsymmetricOwnDeviceId,
       "alAsymmetricHealthCheck": alAsymmetricHealthCheck,
       "alAsymmetricTransportType": alAsymmetricTransportType,
       "alAsymmetricEnable": alAsymmetricEnable,
       "alAsymmetricDeviceTable": alAsymmetricDeviceTable,
       "alAsymmetricDeviceEntry": alAsymmetricDeviceEntry,
       "alAsymmetricRemoteDeviceId": alAsymmetricRemoteDeviceId,
       "alAsymmetricControlVLAN": alAsymmetricControlVLAN,
       "alAsymmetricPort": alAsymmetricPort,
       "alAsymmetricMAC": alAsymmetricMAC,
       "alAsymmetricIP": alAsymmetricIP,
       "alAsymmetricHealthCheckStatus": alAsymmetricHealthCheckStatus,
       "alAsymmetricEntryStatus": alAsymmetricEntryStatus,
       "alServiceActivation": alServiceActivation,
       "alURLFiltering": alURLFiltering,
       "alUrlFOperationMode": alUrlFOperationMode,
       "alUrlFAction": alUrlFAction,
       "alUrlFPortal": alUrlFPortal,
       "alUrlFLastUpdateStatus": alUrlFLastUpdateStatus,
       "alURLMonitoring": alURLMonitoring,
       "alUrlMOperatonMode": alUrlMOperatonMode,
       "alCaptivePortal": alCaptivePortal,
       "alCaptivePortalRedirectionTechnique": alCaptivePortalRedirectionTechnique,
       "alCaptivePortalPassPhrase": alCaptivePortalPassPhrase,
       "alVoipReportingActivation": alVoipReportingActivation,
       "alSPSensorActivation": alSPSensorActivation,
       "alFupProtocolVersion": alFupProtocolVersion,
       "alPredictiveDPI": alPredictiveDPI,
       "alPDPIState": alPDPIState,
       "alIPv6State": alIPv6State,
       "alSelectiveBypass": alSelectiveBypass,
       "alSelectiveBypassActivation": alSelectiveBypassActivation,
       "alSelectiveBypassVlanGroup": alSelectiveBypassVlanGroup,
       "alTetherDetectState": alTetherDetectState,
       "alGenericLastChangeVar": alGenericLastChangeVar,
       "alGenericLastChangeIntVal": alGenericLastChangeIntVal,
       "alGenericLastChangeTimestamp": alGenericLastChangeTimestamp,
       "alGenericConfigTrapEnable": alGenericConfigTrapEnable,
       "alRebootRequest": alRebootRequest,
       "alGenericLastChangeStrVal": alGenericLastChangeStrVal,
       "alGenericLastChangeAddrVal": alGenericLastChangeAddrVal,
       "alProvisioning": alProvisioning,
       "alCatalogs": alCatalogs,
       "alCatalogsLastChangeTimestamp": alCatalogsLastChangeTimestamp,
       "alCatalogsLastChangeRequest": alCatalogsLastChangeRequest,
       "alCatalogListTable": alCatalogListTable,
       "alCatalogListEntry": alCatalogListEntry,
       "alCatalogId": alCatalogId,
       "alCatalogName": alCatalogName,
       "alCatalogsTable": alCatalogsTable,
       "alCatalogsEntry": alCatalogsEntry,
       "alCatalogInstance": alCatalogInstance,
       "alCatalogLastCommand": alCatalogLastCommand,
       "alCatalogTimestamp": alCatalogTimestamp,
       "alCatalogData": alCatalogData,
       "alCatalogCheckSum": alCatalogCheckSum,
       "alCatalogInstanceStatus": alCatalogInstanceStatus,
       "alCatalogLastChangeOrigin": alCatalogLastChangeOrigin,
       "alPolicies": alPolicies,
       "alLineLastChange": alLineLastChange,
       "alLineTable": alLineTable,
       "alLineEntry": alLineEntry,
       "alLineId": alLineId,
       "alLineLastCommand": alLineLastCommand,
       "alLineTimestamp": alLineTimestamp,
       "alLineData": alLineData,
       "alLineCheckSum": alLineCheckSum,
       "alLineInstanceStatus": alLineInstanceStatus,
       "alLineLastChangeOrigin": alLineLastChangeOrigin,
       "alPipeLastChange": alPipeLastChange,
       "alPipeTable": alPipeTable,
       "alPipeEntry": alPipeEntry,
       "alPipeId": alPipeId,
       "alPipeLastCommand": alPipeLastCommand,
       "alPipeTimestamp": alPipeTimestamp,
       "alPipeData": alPipeData,
       "alPipeCheckSum": alPipeCheckSum,
       "alPipeIsTemplate": alPipeIsTemplate,
       "alPipeStatus": alPipeStatus,
       "alPipeLastChangeOrigin": alPipeLastChangeOrigin,
       "alVCLastChange": alVCLastChange,
       "alVCTable": alVCTable,
       "alVCEntry": alVCEntry,
       "alVCId": alVCId,
       "alVCLastCommand": alVCLastCommand,
       "alVCTimestamp": alVCTimestamp,
       "alVCData": alVCData,
       "alVCCheckSum": alVCCheckSum,
       "alVCIsTemplate": alVCIsTemplate,
       "alVCStatus": alVCStatus,
       "alVCLastChangeOrigin": alVCLastChangeOrigin,
       "alLineConfTrapEnable": alLineConfTrapEnable,
       "alPipeConfTrapEnable": alPipeConfTrapEnable,
       "alVcConfTrapEnable": alVcConfTrapEnable,
       "alPolicyModificationTag": alPolicyModificationTag,
       "alStatistics": alStatistics,
       "alStatCntlTable": alStatCntlTable,
       "alStatCntlEntry": alStatCntlEntry,
       "alStatCntlLine": alStatCntlLine,
       "alStatCntlPipe": alStatCntlPipe,
       "alStatCntlVC": alStatCntlVC,
       "alStatCntlUserInstance": alStatCntlUserInstance,
       "alStatCntlIsTemplate": alStatCntlIsTemplate,
       "alStatCntlStartedAt": alStatCntlStartedAt,
       "alStatCntlIsView": alStatCntlIsView,
       "alStatCntlIsAlert": alStatCntlIsAlert,
       "alStatCntlStatus": alStatCntlStatus,
       "alStatTable": alStatTable,
       "alStatEntry": alStatEntry,
       "alStatLiveConn": alStatLiveConn,
       "alStatNewConn": alStatNewConn,
       "alStatDropConn": alStatDropConn,
       "alStatOctetsIn": alStatOctetsIn,
       "alStatOctetsOut": alStatOctetsOut,
       "alStatOctetsTotal": alStatOctetsTotal,
       "alStatPacketsIn": alStatPacketsIn,
       "alStatPacketsOut": alStatPacketsOut,
       "alStatPacketsTotal": alStatPacketsTotal,
       "alStatPipes": alStatPipes,
       "alStatVCs": alStatVCs,
       "alStatLines": alStatLines,
       "alNumberEstConnections": alNumberEstConnections,
       "alConnectionEstRate": alConnectionEstRate,
       "alActiveSubscribers": alActiveSubscribers,
       "alAlerts": alAlerts,
       "alDataSourceTable": alDataSourceTable,
       "alDataSourceEntry": alDataSourceEntry,
       "alDataSourceType": alDataSourceType,
       "alDataSourcePriorityOrder": alDataSourcePriorityOrder,
       "alDataSourceIPAddr": alDataSourceIPAddr,
       "alDataSourceDescr": alDataSourceDescr,
       "alDataSourceStatus": alDataSourceStatus,
       "alDataSourceRowStatus": alDataSourceRowStatus,
       "alDataSourceLastChange": alDataSourceLastChange,
       "alSevereSoftwareProblem": alSevereSoftwareProblem,
       "alMemoryUsage": alMemoryUsage,
       "alDiskUsage": alDiskUsage,
       "alTemperature": alTemperature,
       "alAlertConfTable": alAlertConfTable,
       "alAlertConfEntry": alAlertConfEntry,
       "alAlertConfId": alAlertConfId,
       "alAlertConfVariable": alAlertConfVariable,
       "alAlertConfValue": alAlertConfValue,
       "alAlertConfThreshold": alAlertConfThreshold,
       "alAlertConfNormal": alAlertConfNormal,
       "alAlertConfRegInterval": alAlertConfRegInterval,
       "alAlertConfUnRegInterval": alAlertConfUnRegInterval,
       "alAlertConfThresholdDirection": alAlertConfThresholdDirection,
       "alAlertLastChange": alAlertLastChange,
       "alLastAccessViolation": alLastAccessViolation,
       "alAlertsTrapsEnable": alAlertsTrapsEnable,
       "alDataSourceTrapEnable": alDataSourceTrapEnable,
       "alAccessViolationTrapEnable": alAccessViolationTrapEnable,
       "allDOSAttackTable": allDOSAttackTable,
       "allDOSAttackEntry": allDOSAttackEntry,
       "alDOSAttackType": alDOSAttackType,
       "alDOSAttackPort": alDOSAttackPort,
       "alDOSAttackStatus": alDOSAttackStatus,
       "alDOSTrapEnable": alDOSTrapEnable,
       "alCpuUsage": alCpuUsage,
       "alLastMessage": alLastMessage,
       "alCpuPicoUsage": alCpuPicoUsage,
       "alSensorTable": alSensorTable,
       "alSensorEntry": alSensorEntry,
       "alSensorId": alSensorId,
       "alSensorType": alSensorType,
       "alSensorRawValue": alSensorRawValue,
       "alLoadConfig": alLoadConfig,
       "alSaveConfig": alSaveConfig,
       "alRestoreConfig": alRestoreConfig,
       "alPoliciesStatusTable": alPoliciesStatusTable,
       "alPoliciesStatusEntry": alPoliciesStatusEntry,
       "alPolicyName": alPolicyName,
       "alPolicyTimestamp": alPolicyTimestamp,
       "alPolicyStatus": alPolicyStatus,
       "alConf": alConf,
       "alGroups": alGroups,
       "alGenericGroup": alGenericGroup,
       "alProvisioningGroup": alProvisioningGroup,
       "alStatisticsGroup": alStatisticsGroup,
       "alAlertsGroup": alAlertsGroup,
       "alLoadGroup": alLoadGroup,
       "alEventsGroup": alEventsGroup,
       "alCompls": alCompls,
       "alCompliance": alCompliance}
)
