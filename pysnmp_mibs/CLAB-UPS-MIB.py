# SNMP MIB module (CLAB-UPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rfc/CLAB-UPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:18:33 2025
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

(clabCommonMibs,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabCommonMibs")

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

clabUpsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 1)
)
if mibBuilder.loadTexts:
    clabUpsMib.setRevisions(
        ("2018-01-18 00:00",
         "2010-04-28 00:00",
         "2009-05-06 00:00",
         "2007-01-19 17:00",
         "2005-01-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ClabUpsNotifications_ObjectIdentity = ObjectIdentity
clabUpsNotifications = _ClabUpsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 1, 0)
)
_ClabUpsObjects_ObjectIdentity = ObjectIdentity
clabUpsObjects = _ClabUpsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 1, 1)
)
_ClabSupplemtalGroup_ObjectIdentity = ObjectIdentity
clabSupplemtalGroup = _ClabSupplemtalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 1, 1, 1)
)


class _MtaDevPwrSupplyBatteryTest_Type(Integer32):
    """Custom type mtaDevPwrSupplyBatteryTest based on Integer32"""
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
        *(("disableAutoTesting", 1),
          ("testScheduled", 2),
          ("testInProgress", 3),
          ("testPending", 4))
    )


_MtaDevPwrSupplyBatteryTest_Type.__name__ = "Integer32"
_MtaDevPwrSupplyBatteryTest_Object = MibScalar
mtaDevPwrSupplyBatteryTest = _MtaDevPwrSupplyBatteryTest_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 1, 1, 1, 1),
    _MtaDevPwrSupplyBatteryTest_Type()
)
mtaDevPwrSupplyBatteryTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtaDevPwrSupplyBatteryTest.setStatus("current")
_MtaDevPwrSupplyConfigRunTime_Type = Integer32
_MtaDevPwrSupplyConfigRunTime_Object = MibScalar
mtaDevPwrSupplyConfigRunTime = _MtaDevPwrSupplyConfigRunTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 1, 1, 1, 2),
    _MtaDevPwrSupplyConfigRunTime_Type()
)
mtaDevPwrSupplyConfigRunTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtaDevPwrSupplyConfigRunTime.setStatus("current")
if mibBuilder.loadTexts:
    mtaDevPwrSupplyConfigRunTime.setUnits("minutes")
_MtaDevPwrSupplyRatedMinutes_Type = Integer32
_MtaDevPwrSupplyRatedMinutes_Object = MibScalar
mtaDevPwrSupplyRatedMinutes = _MtaDevPwrSupplyRatedMinutes_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 1, 1, 1, 3),
    _MtaDevPwrSupplyRatedMinutes_Type()
)
mtaDevPwrSupplyRatedMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaDevPwrSupplyRatedMinutes.setStatus("current")
if mibBuilder.loadTexts:
    mtaDevPwrSupplyRatedMinutes.setUnits("minutes")
_MtaDevPwrSupplyAvailableMinutes_Type = Integer32
_MtaDevPwrSupplyAvailableMinutes_Object = MibScalar
mtaDevPwrSupplyAvailableMinutes = _MtaDevPwrSupplyAvailableMinutes_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 1, 1, 1, 4),
    _MtaDevPwrSupplyAvailableMinutes_Type()
)
mtaDevPwrSupplyAvailableMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaDevPwrSupplyAvailableMinutes.setStatus("current")
if mibBuilder.loadTexts:
    mtaDevPwrSupplyAvailableMinutes.setUnits("minutes")
_MtaDevPwrSupplyConfigReplaceBatteryTime_Type = Integer32
_MtaDevPwrSupplyConfigReplaceBatteryTime_Object = MibScalar
mtaDevPwrSupplyConfigReplaceBatteryTime = _MtaDevPwrSupplyConfigReplaceBatteryTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 1, 1, 1, 5),
    _MtaDevPwrSupplyConfigReplaceBatteryTime_Type()
)
mtaDevPwrSupplyConfigReplaceBatteryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtaDevPwrSupplyConfigReplaceBatteryTime.setStatus("current")
if mibBuilder.loadTexts:
    mtaDevPwrSupplyConfigReplaceBatteryTime.setUnits("minutes")
_MtaDevPwrSupplyFullChargeTime_Type = Integer32
_MtaDevPwrSupplyFullChargeTime_Object = MibScalar
mtaDevPwrSupplyFullChargeTime = _MtaDevPwrSupplyFullChargeTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 1, 1, 1, 6),
    _MtaDevPwrSupplyFullChargeTime_Type()
)
mtaDevPwrSupplyFullChargeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtaDevPwrSupplyFullChargeTime.setStatus("current")
_MtaDevPwrSupplyBatteryTestTime_Type = Integer32
_MtaDevPwrSupplyBatteryTestTime_Object = MibScalar
mtaDevPwrSupplyBatteryTestTime = _MtaDevPwrSupplyBatteryTestTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 1, 1, 1, 7),
    _MtaDevPwrSupplyBatteryTestTime_Type()
)
mtaDevPwrSupplyBatteryTestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaDevPwrSupplyBatteryTestTime.setStatus("current")
_ClabUpsConformance_ObjectIdentity = ObjectIdentity
clabUpsConformance = _ClabUpsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 1, 2)
)
_ClabUpsCompliances_ObjectIdentity = ObjectIdentity
clabUpsCompliances = _ClabUpsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 1, 2, 1)
)
_ClabUpsGroups_ObjectIdentity = ObjectIdentity
clabUpsGroups = _ClabUpsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 1, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

clabUpsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 4, 1, 2, 2, 1)
)
clabUpsMibCompliance.setObjects(
      *(("UPS-MIB", "upsSubsetIdentGroup"),
        ("UPS-MIB", "upsFullBatteryGroup"),
        ("UPS-MIB", "upsBasicInputGroup"),
        ("UPS-MIB", "upsBasicOutputGroup"),
        ("UPS-MIB", "upsBasicAlarmGroup"),
        ("UPS-MIB", "upsBasicControlGroup"),
        ("UPS-MIB", "upsBasicConfigGroup"))
)
if mibBuilder.loadTexts:
    clabUpsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CLAB-UPS-MIB",
    **{"clabUpsMib": clabUpsMib,
       "clabUpsNotifications": clabUpsNotifications,
       "clabUpsObjects": clabUpsObjects,
       "clabSupplemtalGroup": clabSupplemtalGroup,
       "mtaDevPwrSupplyBatteryTest": mtaDevPwrSupplyBatteryTest,
       "mtaDevPwrSupplyConfigRunTime": mtaDevPwrSupplyConfigRunTime,
       "mtaDevPwrSupplyRatedMinutes": mtaDevPwrSupplyRatedMinutes,
       "mtaDevPwrSupplyAvailableMinutes": mtaDevPwrSupplyAvailableMinutes,
       "mtaDevPwrSupplyConfigReplaceBatteryTime": mtaDevPwrSupplyConfigReplaceBatteryTime,
       "mtaDevPwrSupplyFullChargeTime": mtaDevPwrSupplyFullChargeTime,
       "mtaDevPwrSupplyBatteryTestTime": mtaDevPwrSupplyBatteryTestTime,
       "clabUpsConformance": clabUpsConformance,
       "clabUpsCompliances": clabUpsCompliances,
       "clabUpsGroups": clabUpsGroups,
       "clabUpsMibCompliance": clabUpsMibCompliance}
)
