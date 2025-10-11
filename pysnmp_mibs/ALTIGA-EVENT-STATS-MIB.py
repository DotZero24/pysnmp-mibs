# SNMP MIB module (ALTIGA-EVENT-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cisco/ALTIGA-EVENT-STATS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:16:34 2025
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

(alEventMibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alEventMibModule")

(alEventGroup,
 alStatsEvent) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alEventGroup",
    "alStatsEvent")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

altigaEventStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2)
)
if mibBuilder.loadTexts:
    altigaEventStatsMibModule.setRevisions(
        ("2003-01-13 00:00",
         "2002-07-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AltigaEventStatsMibConformance_ObjectIdentity = ObjectIdentity
altigaEventStatsMibConformance = _AltigaEventStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2, 1)
)
_AltigaEventStatsMibCompliances_ObjectIdentity = ObjectIdentity
altigaEventStatsMibCompliances = _AltigaEventStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2, 1, 1)
)
_AlStatsEventGlobal_ObjectIdentity = ObjectIdentity
alStatsEventGlobal = _AlStatsEventGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 1)
)
_AlStatsEventNotificationId_Type = DisplayString
_AlStatsEventNotificationId_Object = MibScalar
alStatsEventNotificationId = _AlStatsEventNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 1, 1),
    _AlStatsEventNotificationId_Type()
)
alStatsEventNotificationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alStatsEventNotificationId.setStatus("current")
_AlEventStatsTable_Object = MibTable
alEventStatsTable = _AlEventStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    alEventStatsTable.setStatus("current")
_AlEventStatsEntry_Object = MibTableRow
alEventStatsEntry = _AlEventStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2, 1)
)
alEventStatsEntry.setIndexNames(
    (0, "ALTIGA-EVENT-STATS-MIB", "alEventStatsClass"),
    (0, "ALTIGA-EVENT-STATS-MIB", "alEventStatsEventNumber"),
)
if mibBuilder.loadTexts:
    alEventStatsEntry.setStatus("current")


class _AlEventStatsClass_Type(Integer32):
    """Custom type alEventStatsClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlEventStatsClass_Type.__name__ = "Integer32"
_AlEventStatsClass_Object = MibTableColumn
alEventStatsClass = _AlEventStatsClass_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2, 1, 1),
    _AlEventStatsClass_Type()
)
alEventStatsClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alEventStatsClass.setStatus("current")


class _AlEventStatsEventNumber_Type(Integer32):
    """Custom type alEventStatsEventNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlEventStatsEventNumber_Type.__name__ = "Integer32"
_AlEventStatsEventNumber_Object = MibTableColumn
alEventStatsEventNumber = _AlEventStatsEventNumber_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2, 1, 2),
    _AlEventStatsEventNumber_Type()
)
alEventStatsEventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alEventStatsEventNumber.setStatus("current")
_AlEventStatsCount_Type = Counter32
_AlEventStatsCount_Object = MibTableColumn
alEventStatsCount = _AlEventStatsCount_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2, 1, 3),
    _AlEventStatsCount_Type()
)
alEventStatsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alEventStatsCount.setStatus("current")

# Managed Objects groups

altigaEventStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 4, 2)
)
altigaEventStatsGroup.setObjects(
      *(("ALTIGA-EVENT-STATS-MIB", "alEventStatsClass"),
        ("ALTIGA-EVENT-STATS-MIB", "alEventStatsEventNumber"),
        ("ALTIGA-EVENT-STATS-MIB", "alEventStatsCount"))
)
if mibBuilder.loadTexts:
    altigaEventStatsGroup.setStatus("deprecated")

altigaEventStatsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 4, 3)
)
altigaEventStatsGroupRev1.setObjects(
      *(("ALTIGA-EVENT-STATS-MIB", "alEventStatsClass"),
        ("ALTIGA-EVENT-STATS-MIB", "alEventStatsEventNumber"),
        ("ALTIGA-EVENT-STATS-MIB", "alEventStatsCount"),
        ("ALTIGA-EVENT-STATS-MIB", "alStatsEventNotificationId"))
)
if mibBuilder.loadTexts:
    altigaEventStatsGroupRev1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaEventStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2, 1, 1, 1)
)
altigaEventStatsMibCompliance.setObjects(
    ("ALTIGA-EVENT-STATS-MIB", "altigaEventStatsGroup")
)
if mibBuilder.loadTexts:
    altigaEventStatsMibCompliance.setStatus(
        "deprecated"
    )

altigaEventStatsMibComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2, 1, 1, 2)
)
altigaEventStatsMibComplianceRev1.setObjects(
    ("ALTIGA-EVENT-STATS-MIB", "altigaEventStatsGroupRev1")
)
if mibBuilder.loadTexts:
    altigaEventStatsMibComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-EVENT-STATS-MIB",
    **{"altigaEventStatsMibModule": altigaEventStatsMibModule,
       "altigaEventStatsMibConformance": altigaEventStatsMibConformance,
       "altigaEventStatsMibCompliances": altigaEventStatsMibCompliances,
       "altigaEventStatsMibCompliance": altigaEventStatsMibCompliance,
       "altigaEventStatsMibComplianceRev1": altigaEventStatsMibComplianceRev1,
       "altigaEventStatsGroup": altigaEventStatsGroup,
       "altigaEventStatsGroupRev1": altigaEventStatsGroupRev1,
       "alStatsEventGlobal": alStatsEventGlobal,
       "alStatsEventNotificationId": alStatsEventNotificationId,
       "alEventStatsTable": alEventStatsTable,
       "alEventStatsEntry": alEventStatsEntry,
       "alEventStatsClass": alEventStatsClass,
       "alEventStatsEventNumber": alEventStatsEventNumber,
       "alEventStatsCount": alEventStatsCount}
)
