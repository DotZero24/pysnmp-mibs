# SNMP MIB module (NEWTEC-FANCONTROLLER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-FANCONTROLLER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:12 2025
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

(ntcFunction,) = mibBuilder.importSymbols(
    "NEWTEC-MAIN-MIB",
    "ntcFunction")

(NtcAlarmState,) = mibBuilder.importSymbols(
    "NEWTEC-TC-MIB",
    "NtcAlarmState")

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

ntcFanController = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3500)
)
if mibBuilder.loadTexts:
    ntcFanController.setRevisions(
        ("2013-07-05 06:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcFanCObjects_ObjectIdentity = ObjectIdentity
ntcFanCObjects = _NtcFanCObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3500, 1)
)
if mibBuilder.loadTexts:
    ntcFanCObjects.setStatus("current")
_NtcFanAlarm_ObjectIdentity = ObjectIdentity
ntcFanAlarm = _NtcFanAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3500, 1, 1)
)
if mibBuilder.loadTexts:
    ntcFanAlarm.setStatus("current")
_NtcFanCAlmFanFailure_Type = NtcAlarmState
_NtcFanCAlmFanFailure_Object = MibScalar
ntcFanCAlmFanFailure = _NtcFanCAlmFanFailure_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3500, 1, 1, 1),
    _NtcFanCAlmFanFailure_Type()
)
ntcFanCAlmFanFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcFanCAlmFanFailure.setStatus("current")
_NtcFanCConformance_ObjectIdentity = ObjectIdentity
ntcFanCConformance = _NtcFanCConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3500, 2)
)
if mibBuilder.loadTexts:
    ntcFanCConformance.setStatus("current")
_NtcFanCConfCompliance_ObjectIdentity = ObjectIdentity
ntcFanCConfCompliance = _NtcFanCConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3500, 2, 1)
)
if mibBuilder.loadTexts:
    ntcFanCConfCompliance.setStatus("current")
_NtcFanCConfGroup_ObjectIdentity = ObjectIdentity
ntcFanCConfGroup = _NtcFanCConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3500, 2, 2)
)
if mibBuilder.loadTexts:
    ntcFanCConfGroup.setStatus("current")

# Managed Objects groups

ntcFanCConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3500, 2, 2, 1)
)
ntcFanCConfGrpV1Standard.setObjects(
    ("NEWTEC-FANCONTROLLER-MIB", "ntcFanCAlmFanFailure")
)
if mibBuilder.loadTexts:
    ntcFanCConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcFanCConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3500, 2, 1, 1)
)
ntcFanCConfCompV1Standard.setObjects(
    ("NEWTEC-FANCONTROLLER-MIB", "ntcFanCConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcFanCConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-FANCONTROLLER-MIB",
    **{"ntcFanController": ntcFanController,
       "ntcFanCObjects": ntcFanCObjects,
       "ntcFanAlarm": ntcFanAlarm,
       "ntcFanCAlmFanFailure": ntcFanCAlmFanFailure,
       "ntcFanCConformance": ntcFanCConformance,
       "ntcFanCConfCompliance": ntcFanCConfCompliance,
       "ntcFanCConfCompV1Standard": ntcFanCConfCompV1Standard,
       "ntcFanCConfGroup": ntcFanCConfGroup,
       "ntcFanCConfGrpV1Standard": ntcFanCConfGrpV1Standard}
)
