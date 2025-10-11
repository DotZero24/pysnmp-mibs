# SNMP MIB module (NEWTEC-MOIF2LBANDCONVERTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-MOIF2LBANDCONVERTER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:09 2025
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

ntcMoIF2LbandConverter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8600)
)
if mibBuilder.loadTexts:
    ntcMoIF2LbandConverter.setRevisions(
        ("2015-02-19 09:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcMoIF2LConvObjects_ObjectIdentity = ObjectIdentity
ntcMoIF2LConvObjects = _NtcMoIF2LConvObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8600, 1)
)
if mibBuilder.loadTexts:
    ntcMoIF2LConvObjects.setStatus("current")
_NtcMoIF2LConvAlarm_ObjectIdentity = ObjectIdentity
ntcMoIF2LConvAlarm = _NtcMoIF2LConvAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8600, 1, 1)
)
if mibBuilder.loadTexts:
    ntcMoIF2LConvAlarm.setStatus("current")
_NtcMoIF2LConvHardware_Type = NtcAlarmState
_NtcMoIF2LConvHardware_Object = MibScalar
ntcMoIF2LConvHardware = _NtcMoIF2LConvHardware_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8600, 1, 1, 1),
    _NtcMoIF2LConvHardware_Type()
)
ntcMoIF2LConvHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMoIF2LConvHardware.setStatus("current")
_NtcMoIF2LConvCommunication_Type = NtcAlarmState
_NtcMoIF2LConvCommunication_Object = MibScalar
ntcMoIF2LConvCommunication = _NtcMoIF2LConvCommunication_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8600, 1, 1, 2),
    _NtcMoIF2LConvCommunication_Type()
)
ntcMoIF2LConvCommunication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMoIF2LConvCommunication.setStatus("current")
_NtcMoIF2LConvConformance_ObjectIdentity = ObjectIdentity
ntcMoIF2LConvConformance = _NtcMoIF2LConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8600, 2)
)
if mibBuilder.loadTexts:
    ntcMoIF2LConvConformance.setStatus("current")
_NtcMoIF2LConvConfCompliance_ObjectIdentity = ObjectIdentity
ntcMoIF2LConvConfCompliance = _NtcMoIF2LConvConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8600, 2, 1)
)
if mibBuilder.loadTexts:
    ntcMoIF2LConvConfCompliance.setStatus("current")
_NtcMoIF2LConvConfGroup_ObjectIdentity = ObjectIdentity
ntcMoIF2LConvConfGroup = _NtcMoIF2LConvConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8600, 2, 2)
)
if mibBuilder.loadTexts:
    ntcMoIF2LConvConfGroup.setStatus("current")

# Managed Objects groups

ntcMoIF2LConvConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8600, 2, 2, 1)
)
ntcMoIF2LConvConfGrpV1Standard.setObjects(
      *(("NEWTEC-MOIF2LBANDCONVERTER-MIB", "ntcMoIF2LConvHardware"),
        ("NEWTEC-MOIF2LBANDCONVERTER-MIB", "ntcMoIF2LConvCommunication"))
)
if mibBuilder.loadTexts:
    ntcMoIF2LConvConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcMoIF2LConvConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8600, 2, 1, 1)
)
ntcMoIF2LConvConfCompV1Standard.setObjects(
    ("NEWTEC-MOIF2LBANDCONVERTER-MIB", "ntcMoIF2LConvConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcMoIF2LConvConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-MOIF2LBANDCONVERTER-MIB",
    **{"ntcMoIF2LbandConverter": ntcMoIF2LbandConverter,
       "ntcMoIF2LConvObjects": ntcMoIF2LConvObjects,
       "ntcMoIF2LConvAlarm": ntcMoIF2LConvAlarm,
       "ntcMoIF2LConvHardware": ntcMoIF2LConvHardware,
       "ntcMoIF2LConvCommunication": ntcMoIF2LConvCommunication,
       "ntcMoIF2LConvConformance": ntcMoIF2LConvConformance,
       "ntcMoIF2LConvConfCompliance": ntcMoIF2LConvConfCompliance,
       "ntcMoIF2LConvConfCompV1Standard": ntcMoIF2LConvConfCompV1Standard,
       "ntcMoIF2LConvConfGroup": ntcMoIF2LConvConfGroup,
       "ntcMoIF2LConvConfGrpV1Standard": ntcMoIF2LConvConfGrpV1Standard}
)
