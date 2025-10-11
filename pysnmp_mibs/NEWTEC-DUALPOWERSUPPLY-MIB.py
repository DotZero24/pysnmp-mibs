# SNMP MIB module (NEWTEC-DUALPOWERSUPPLY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-DUALPOWERSUPPLY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:10 2025
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

ntcDualPowerSupply = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3000)
)
if mibBuilder.loadTexts:
    ntcDualPowerSupply.setRevisions(
        ("2012-11-13 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcDualPSObjects_ObjectIdentity = ObjectIdentity
ntcDualPSObjects = _NtcDualPSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3000, 1)
)
if mibBuilder.loadTexts:
    ntcDualPSObjects.setStatus("current")
_NtcDualPSAlarm_ObjectIdentity = ObjectIdentity
ntcDualPSAlarm = _NtcDualPSAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3000, 1, 1)
)
if mibBuilder.loadTexts:
    ntcDualPSAlarm.setStatus("current")
_NtcDualPSAlmPowerSupplyAFailure_Type = NtcAlarmState
_NtcDualPSAlmPowerSupplyAFailure_Object = MibScalar
ntcDualPSAlmPowerSupplyAFailure = _NtcDualPSAlmPowerSupplyAFailure_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3000, 1, 1, 1),
    _NtcDualPSAlmPowerSupplyAFailure_Type()
)
ntcDualPSAlmPowerSupplyAFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDualPSAlmPowerSupplyAFailure.setStatus("current")
_NtcDualPSAlmPowerSupplyBFailure_Type = NtcAlarmState
_NtcDualPSAlmPowerSupplyBFailure_Object = MibScalar
ntcDualPSAlmPowerSupplyBFailure = _NtcDualPSAlmPowerSupplyBFailure_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3000, 1, 1, 2),
    _NtcDualPSAlmPowerSupplyBFailure_Type()
)
ntcDualPSAlmPowerSupplyBFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDualPSAlmPowerSupplyBFailure.setStatus("current")
_NtcDualPSConformance_ObjectIdentity = ObjectIdentity
ntcDualPSConformance = _NtcDualPSConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3000, 2)
)
if mibBuilder.loadTexts:
    ntcDualPSConformance.setStatus("current")
_NtcDualPSConfCompliance_ObjectIdentity = ObjectIdentity
ntcDualPSConfCompliance = _NtcDualPSConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3000, 2, 1)
)
if mibBuilder.loadTexts:
    ntcDualPSConfCompliance.setStatus("current")
_NtcDualPSConfGroup_ObjectIdentity = ObjectIdentity
ntcDualPSConfGroup = _NtcDualPSConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3000, 2, 2)
)
if mibBuilder.loadTexts:
    ntcDualPSConfGroup.setStatus("current")

# Managed Objects groups

ntcDualPSConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3000, 2, 2, 1)
)
ntcDualPSConfGrpV1Standard.setObjects(
      *(("NEWTEC-DUALPOWERSUPPLY-MIB", "ntcDualPSAlmPowerSupplyAFailure"),
        ("NEWTEC-DUALPOWERSUPPLY-MIB", "ntcDualPSAlmPowerSupplyBFailure"))
)
if mibBuilder.loadTexts:
    ntcDualPSConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcDualPSConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3000, 2, 1, 1)
)
ntcDualPSConfCompV1Standard.setObjects(
    ("NEWTEC-DUALPOWERSUPPLY-MIB", "ntcDualPSConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcDualPSConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-DUALPOWERSUPPLY-MIB",
    **{"ntcDualPowerSupply": ntcDualPowerSupply,
       "ntcDualPSObjects": ntcDualPSObjects,
       "ntcDualPSAlarm": ntcDualPSAlarm,
       "ntcDualPSAlmPowerSupplyAFailure": ntcDualPSAlmPowerSupplyAFailure,
       "ntcDualPSAlmPowerSupplyBFailure": ntcDualPSAlmPowerSupplyBFailure,
       "ntcDualPSConformance": ntcDualPSConformance,
       "ntcDualPSConfCompliance": ntcDualPSConfCompliance,
       "ntcDualPSConfCompV1Standard": ntcDualPSConfCompV1Standard,
       "ntcDualPSConfGroup": ntcDualPSConfGroup,
       "ntcDualPSConfGrpV1Standard": ntcDualPSConfGrpV1Standard}
)
