# SNMP MIB module (ELTEX-MES-ISS-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-ISS-SYSLOG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:50:29 2025
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

(eltMesIss,) = mibBuilder.importSymbols(
    "ELTEX-MES-ISS-MIB",
    "eltMesIss")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltMesIssSyslogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 22)
)
if mibBuilder.loadTexts:
    eltMesIssSyslogMIB.setRevisions(
        ("2020-07-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesIssSyslogObjects_ObjectIdentity = ObjectIdentity
eltMesIssSyslogObjects = _EltMesIssSyslogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 22, 1)
)
_EltMesIssSyslogGlobals_ObjectIdentity = ObjectIdentity
eltMesIssSyslogGlobals = _EltMesIssSyslogGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 22, 1, 1)
)


class _EltMesIssSyslogVersionMode_Type(Integer32):
    """Custom type eltMesIssSyslogVersionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("empty", 1),
          ("present", 2))
    )


_EltMesIssSyslogVersionMode_Type.__name__ = "Integer32"
_EltMesIssSyslogVersionMode_Object = MibScalar
eltMesIssSyslogVersionMode = _EltMesIssSyslogVersionMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 22, 1, 1, 1),
    _EltMesIssSyslogVersionMode_Type()
)
eltMesIssSyslogVersionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssSyslogVersionMode.setStatus("current")


class _EltMesIssSyslogVersionString_Type(DisplayString):
    """Custom type eltMesIssSyslogVersionString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_EltMesIssSyslogVersionString_Type.__name__ = "DisplayString"
_EltMesIssSyslogVersionString_Object = MibScalar
eltMesIssSyslogVersionString = _EltMesIssSyslogVersionString_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 22, 1, 1, 2),
    _EltMesIssSyslogVersionString_Type()
)
eltMesIssSyslogVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssSyslogVersionString.setStatus("current")


class _EltMesIssSyslogTimestampMode_Type(Integer32):
    """Custom type eltMesIssSyslogTimestampMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("legacy", 1),
          ("rfc5424", 2))
    )


_EltMesIssSyslogTimestampMode_Type.__name__ = "Integer32"
_EltMesIssSyslogTimestampMode_Object = MibScalar
eltMesIssSyslogTimestampMode = _EltMesIssSyslogTimestampMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 22, 1, 1, 3),
    _EltMesIssSyslogTimestampMode_Type()
)
eltMesIssSyslogTimestampMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssSyslogTimestampMode.setStatus("current")


class _EltMesIssSyslogHostnameMode_Type(Integer32):
    """Custom type eltMesIssSyslogHostnameMode based on Integer32"""
    defaultValue = 1

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
        *(("empty", 1),
          ("string", 2),
          ("hostname", 3),
          ("ip", 4),
          ("ipv6", 5))
    )


_EltMesIssSyslogHostnameMode_Type.__name__ = "Integer32"
_EltMesIssSyslogHostnameMode_Object = MibScalar
eltMesIssSyslogHostnameMode = _EltMesIssSyslogHostnameMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 22, 1, 1, 4),
    _EltMesIssSyslogHostnameMode_Type()
)
eltMesIssSyslogHostnameMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssSyslogHostnameMode.setStatus("current")


class _EltMesIssSyslogHostnameString_Type(DisplayString):
    """Custom type eltMesIssSyslogHostnameString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltMesIssSyslogHostnameString_Type.__name__ = "DisplayString"
_EltMesIssSyslogHostnameString_Object = MibScalar
eltMesIssSyslogHostnameString = _EltMesIssSyslogHostnameString_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 22, 1, 1, 5),
    _EltMesIssSyslogHostnameString_Type()
)
eltMesIssSyslogHostnameString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssSyslogHostnameString.setStatus("current")
_EltMesIssSyslogNotifications_ObjectIdentity = ObjectIdentity
eltMesIssSyslogNotifications = _EltMesIssSyslogNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 22, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-SYSLOG-MIB",
    **{"eltMesIssSyslogMIB": eltMesIssSyslogMIB,
       "eltMesIssSyslogObjects": eltMesIssSyslogObjects,
       "eltMesIssSyslogGlobals": eltMesIssSyslogGlobals,
       "eltMesIssSyslogVersionMode": eltMesIssSyslogVersionMode,
       "eltMesIssSyslogVersionString": eltMesIssSyslogVersionString,
       "eltMesIssSyslogTimestampMode": eltMesIssSyslogTimestampMode,
       "eltMesIssSyslogHostnameMode": eltMesIssSyslogHostnameMode,
       "eltMesIssSyslogHostnameString": eltMesIssSyslogHostnameString,
       "eltMesIssSyslogNotifications": eltMesIssSyslogNotifications}
)
