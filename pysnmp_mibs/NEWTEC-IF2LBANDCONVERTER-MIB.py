# SNMP MIB module (NEWTEC-IF2LBANDCONVERTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-IF2LBANDCONVERTER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:06 2025
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

ntcIF2LbandConverter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4600)
)
if mibBuilder.loadTexts:
    ntcIF2LbandConverter.setRevisions(
        ("2012-06-28 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcIF2LConvObjects_ObjectIdentity = ObjectIdentity
ntcIF2LConvObjects = _NtcIF2LConvObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4600, 1)
)
if mibBuilder.loadTexts:
    ntcIF2LConvObjects.setStatus("current")
_NtcIF2LConvAlarm_ObjectIdentity = ObjectIdentity
ntcIF2LConvAlarm = _NtcIF2LConvAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4600, 1, 1)
)
if mibBuilder.loadTexts:
    ntcIF2LConvAlarm.setStatus("current")
_NtcIF2LConvHardware_Type = NtcAlarmState
_NtcIF2LConvHardware_Object = MibScalar
ntcIF2LConvHardware = _NtcIF2LConvHardware_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4600, 1, 1, 1),
    _NtcIF2LConvHardware_Type()
)
ntcIF2LConvHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcIF2LConvHardware.setStatus("current")
_NtcIF2LConvCommunication_Type = NtcAlarmState
_NtcIF2LConvCommunication_Object = MibScalar
ntcIF2LConvCommunication = _NtcIF2LConvCommunication_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4600, 1, 1, 2),
    _NtcIF2LConvCommunication_Type()
)
ntcIF2LConvCommunication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcIF2LConvCommunication.setStatus("current")
_NtcIF2LConvConformance_ObjectIdentity = ObjectIdentity
ntcIF2LConvConformance = _NtcIF2LConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4600, 2)
)
if mibBuilder.loadTexts:
    ntcIF2LConvConformance.setStatus("current")
_NtcIF2LConvConfCompliance_ObjectIdentity = ObjectIdentity
ntcIF2LConvConfCompliance = _NtcIF2LConvConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4600, 2, 1)
)
if mibBuilder.loadTexts:
    ntcIF2LConvConfCompliance.setStatus("current")
_NtcIF2LConvConfGroup_ObjectIdentity = ObjectIdentity
ntcIF2LConvConfGroup = _NtcIF2LConvConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4600, 2, 2)
)
if mibBuilder.loadTexts:
    ntcIF2LConvConfGroup.setStatus("current")

# Managed Objects groups

ntcIF2LConvConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4600, 2, 2, 1)
)
ntcIF2LConvConfGrpV1Standard.setObjects(
      *(("NEWTEC-IF2LBANDCONVERTER-MIB", "ntcIF2LConvHardware"),
        ("NEWTEC-IF2LBANDCONVERTER-MIB", "ntcIF2LConvCommunication"))
)
if mibBuilder.loadTexts:
    ntcIF2LConvConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcIF2LConvConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4600, 2, 1, 1)
)
ntcIF2LConvConfCompV1Standard.setObjects(
    ("NEWTEC-IF2LBANDCONVERTER-MIB", "ntcIF2LConvConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcIF2LConvConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-IF2LBANDCONVERTER-MIB",
    **{"ntcIF2LbandConverter": ntcIF2LbandConverter,
       "ntcIF2LConvObjects": ntcIF2LConvObjects,
       "ntcIF2LConvAlarm": ntcIF2LConvAlarm,
       "ntcIF2LConvHardware": ntcIF2LConvHardware,
       "ntcIF2LConvCommunication": ntcIF2LConvCommunication,
       "ntcIF2LConvConformance": ntcIF2LConvConformance,
       "ntcIF2LConvConfCompliance": ntcIF2LConvConfCompliance,
       "ntcIF2LConvConfCompV1Standard": ntcIF2LConvConfCompV1Standard,
       "ntcIF2LConvConfGroup": ntcIF2LConvConfGroup,
       "ntcIF2LConvConfGrpV1Standard": ntcIF2LConvConfGrpV1Standard}
)
