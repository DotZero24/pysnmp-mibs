# SNMP MIB module (NEWTEC-MORFBUC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-MORFBUC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:03:59 2025
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

ntcMoRfBlockUpConv = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 10000)
)
if mibBuilder.loadTexts:
    ntcMoRfBlockUpConv.setRevisions(
        ("2016-05-17 09:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcMoRfBucObjects_ObjectIdentity = ObjectIdentity
ntcMoRfBucObjects = _NtcMoRfBucObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 10000, 1)
)
if mibBuilder.loadTexts:
    ntcMoRfBucObjects.setStatus("current")
_NtcMoRfBucAlarm_ObjectIdentity = ObjectIdentity
ntcMoRfBucAlarm = _NtcMoRfBucAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 10000, 1, 1)
)
if mibBuilder.loadTexts:
    ntcMoRfBucAlarm.setStatus("current")
_NtcMoRfBucHardware_Type = NtcAlarmState
_NtcMoRfBucHardware_Object = MibScalar
ntcMoRfBucHardware = _NtcMoRfBucHardware_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 10000, 1, 1, 1),
    _NtcMoRfBucHardware_Type()
)
ntcMoRfBucHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMoRfBucHardware.setStatus("current")
_NtcMoRfBucCommunication_Type = NtcAlarmState
_NtcMoRfBucCommunication_Object = MibScalar
ntcMoRfBucCommunication = _NtcMoRfBucCommunication_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 10000, 1, 1, 2),
    _NtcMoRfBucCommunication_Type()
)
ntcMoRfBucCommunication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMoRfBucCommunication.setStatus("current")
_NtcMoRfBucConformance_ObjectIdentity = ObjectIdentity
ntcMoRfBucConformance = _NtcMoRfBucConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 10000, 2)
)
if mibBuilder.loadTexts:
    ntcMoRfBucConformance.setStatus("current")
_NtcMoRfBucConfCompliance_ObjectIdentity = ObjectIdentity
ntcMoRfBucConfCompliance = _NtcMoRfBucConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 10000, 2, 1)
)
if mibBuilder.loadTexts:
    ntcMoRfBucConfCompliance.setStatus("current")
_NtcMoRfBucConfGroup_ObjectIdentity = ObjectIdentity
ntcMoRfBucConfGroup = _NtcMoRfBucConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 10000, 2, 2)
)
if mibBuilder.loadTexts:
    ntcMoRfBucConfGroup.setStatus("current")

# Managed Objects groups

ntcMoRfBucConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 10000, 2, 2, 1)
)
ntcMoRfBucConfGrpV1Standard.setObjects(
      *(("NEWTEC-MORFBUC-MIB", "ntcMoRfBucHardware"),
        ("NEWTEC-MORFBUC-MIB", "ntcMoRfBucCommunication"))
)
if mibBuilder.loadTexts:
    ntcMoRfBucConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcMoRfBucConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 10000, 2, 1, 1)
)
ntcMoRfBucConfCompV1Standard.setObjects(
    ("NEWTEC-MORFBUC-MIB", "ntcMoRfBucConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcMoRfBucConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-MORFBUC-MIB",
    **{"ntcMoRfBlockUpConv": ntcMoRfBlockUpConv,
       "ntcMoRfBucObjects": ntcMoRfBucObjects,
       "ntcMoRfBucAlarm": ntcMoRfBucAlarm,
       "ntcMoRfBucHardware": ntcMoRfBucHardware,
       "ntcMoRfBucCommunication": ntcMoRfBucCommunication,
       "ntcMoRfBucConformance": ntcMoRfBucConformance,
       "ntcMoRfBucConfCompliance": ntcMoRfBucConfCompliance,
       "ntcMoRfBucConfCompV1Standard": ntcMoRfBucConfCompV1Standard,
       "ntcMoRfBucConfGroup": ntcMoRfBucConfGroup,
       "ntcMoRfBucConfGrpV1Standard": ntcMoRfBucConfGrpV1Standard}
)
