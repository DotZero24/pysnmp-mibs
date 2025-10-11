# SNMP MIB module (NEWTEC-MAIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-MAIN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:18 2025
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ntcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835)
)
if mibBuilder.loadTexts:
    ntcMIB.setRevisions(
        ("2015-11-20 12:00",
         "2013-09-02 12:00",
         "2012-06-28 12:00",
         "2004-05-04 11:00",
         "2000-03-27 14:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcSems_ObjectIdentity = ObjectIdentity
ntcSems = _NtcSems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 1)
)
if mibBuilder.loadTexts:
    ntcSems.setStatus("current")
_NtcPlex_ObjectIdentity = ObjectIdentity
ntcPlex = _NtcPlex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 2)
)
if mibBuilder.loadTexts:
    ntcPlex.setStatus("obsolete")
_NtcDevices_ObjectIdentity = ObjectIdentity
ntcDevices = _NtcDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 3)
)
if mibBuilder.loadTexts:
    ntcDevices.setStatus("current")
_NtcSecurity_ObjectIdentity = ObjectIdentity
ntcSecurity = _NtcSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 4)
)
if mibBuilder.loadTexts:
    ntcSecurity.setStatus("obsolete")
_NtcPublic_ObjectIdentity = ObjectIdentity
ntcPublic = _NtcPublic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5)
)
if mibBuilder.loadTexts:
    ntcPublic.setStatus("current")
_NtcGeneric_ObjectIdentity = ObjectIdentity
ntcGeneric = _NtcGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 1)
)
if mibBuilder.loadTexts:
    ntcGeneric.setStatus("current")
_NtcFunction_ObjectIdentity = ObjectIdentity
ntcFunction = _NtcFunction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2)
)
if mibBuilder.loadTexts:
    ntcFunction.setStatus("current")
_NtcEvent_ObjectIdentity = ObjectIdentity
ntcEvent = _NtcEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 3)
)
if mibBuilder.loadTexts:
    ntcEvent.setStatus("current")
_NtcExperimental_ObjectIdentity = ObjectIdentity
ntcExperimental = _NtcExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 6)
)
if mibBuilder.loadTexts:
    ntcExperimental.setStatus("current")
_NtcLDAP_ObjectIdentity = ObjectIdentity
ntcLDAP = _NtcLDAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 7)
)
if mibBuilder.loadTexts:
    ntcLDAP.setStatus("current")
_NtcSystems_ObjectIdentity = ObjectIdentity
ntcSystems = _NtcSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 8)
)
if mibBuilder.loadTexts:
    ntcSystems.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-MAIN-MIB",
    **{"ntcMIB": ntcMIB,
       "ntcSems": ntcSems,
       "ntcPlex": ntcPlex,
       "ntcDevices": ntcDevices,
       "ntcSecurity": ntcSecurity,
       "ntcPublic": ntcPublic,
       "ntcGeneric": ntcGeneric,
       "ntcFunction": ntcFunction,
       "ntcEvent": ntcEvent,
       "ntcExperimental": ntcExperimental,
       "ntcLDAP": ntcLDAP,
       "ntcSystems": ntcSystems}
)
