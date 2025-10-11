# SNMP MIB module (ARRIS-MTA-DOC30-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/arris/ARRIS-MTA-DOC30-DEVICE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:10:18 2025
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

(arrisProdIdCM,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "arrisProdIdCM")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

arrisMtaDoc30Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 5)
)
if mibBuilder.loadTexts:
    arrisMtaDoc30Mib.setRevisions(
        ("1910-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArrisMtaDoc30MibObjects_ObjectIdentity = ObjectIdentity
arrisMtaDoc30MibObjects = _ArrisMtaDoc30MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 5, 1)
)
_ArrisMtaDoc30Base_ObjectIdentity = ObjectIdentity
arrisMtaDoc30Base = _ArrisMtaDoc30Base_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 5, 1, 1)
)
_ArrisMtaDoc30Setup_ObjectIdentity = ObjectIdentity
arrisMtaDoc30Setup = _ArrisMtaDoc30Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 5, 1, 2)
)


class _ArrisMtaDoc30EmergencyNumber_Type(DisplayString):
    """Custom type arrisMtaDoc30EmergencyNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_ArrisMtaDoc30EmergencyNumber_Type.__name__ = "DisplayString"
_ArrisMtaDoc30EmergencyNumber_Object = MibScalar
arrisMtaDoc30EmergencyNumber = _ArrisMtaDoc30EmergencyNumber_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 5, 1, 2, 1),
    _ArrisMtaDoc30EmergencyNumber_Type()
)
arrisMtaDoc30EmergencyNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDoc30EmergencyNumber.setStatus("current")


class _ArrisMtaDoc30RootCertType_Type(Integer32):
    """Custom type arrisMtaDoc30RootCertType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("testRoot", 1),
          ("realRoot", 2))
    )


_ArrisMtaDoc30RootCertType_Type.__name__ = "Integer32"
_ArrisMtaDoc30RootCertType_Object = MibScalar
arrisMtaDoc30RootCertType = _ArrisMtaDoc30RootCertType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 5, 1, 2, 2),
    _ArrisMtaDoc30RootCertType_Type()
)
arrisMtaDoc30RootCertType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDoc30RootCertType.setStatus("current")


class _ArrisMtaDoc30AdjustCallpFeatureSwitch_Type(Integer32):
    """Custom type arrisMtaDoc30AdjustCallpFeatureSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ArrisMtaDoc30AdjustCallpFeatureSwitch_Type.__name__ = "Integer32"
_ArrisMtaDoc30AdjustCallpFeatureSwitch_Object = MibScalar
arrisMtaDoc30AdjustCallpFeatureSwitch = _ArrisMtaDoc30AdjustCallpFeatureSwitch_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 5, 1, 2, 3),
    _ArrisMtaDoc30AdjustCallpFeatureSwitch_Type()
)
arrisMtaDoc30AdjustCallpFeatureSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDoc30AdjustCallpFeatureSwitch.setStatus("current")


class _ArrisMtaDoc30InvalidateTickets_Type(Integer32):
    """Custom type arrisMtaDoc30InvalidateTickets based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ArrisMtaDoc30InvalidateTickets_Type.__name__ = "Integer32"
_ArrisMtaDoc30InvalidateTickets_Object = MibScalar
arrisMtaDoc30InvalidateTickets = _ArrisMtaDoc30InvalidateTickets_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 5, 1, 2, 4),
    _ArrisMtaDoc30InvalidateTickets_Type()
)
arrisMtaDoc30InvalidateTickets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMtaDoc30InvalidateTickets.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-MTA-DOC30-DEVICE-MIB",
    **{"arrisMtaDoc30Mib": arrisMtaDoc30Mib,
       "arrisMtaDoc30MibObjects": arrisMtaDoc30MibObjects,
       "arrisMtaDoc30Base": arrisMtaDoc30Base,
       "arrisMtaDoc30Setup": arrisMtaDoc30Setup,
       "arrisMtaDoc30EmergencyNumber": arrisMtaDoc30EmergencyNumber,
       "arrisMtaDoc30RootCertType": arrisMtaDoc30RootCertType,
       "arrisMtaDoc30AdjustCallpFeatureSwitch": arrisMtaDoc30AdjustCallpFeatureSwitch,
       "arrisMtaDoc30InvalidateTickets": arrisMtaDoc30InvalidateTickets}
)
