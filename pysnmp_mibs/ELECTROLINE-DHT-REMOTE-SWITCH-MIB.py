# SNMP MIB module (ELECTROLINE-DHT-REMOTE-SWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/electroline/ELECTROLINE-DHT-REMOTE-SWITCH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:06:50 2025
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

(dhtExtensionsMibObjects,) = mibBuilder.importSymbols(
    "ELECTROLINE-DHT-EXTENSIONS-MIB",
    "dhtExtensionsMibObjects")

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

dhtRemoteSwitchMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 11)
)
if mibBuilder.loadTexts:
    dhtRemoteSwitchMib.setRevisions(
        ("2004-12-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DhtRemoteSwitchObjects_ObjectIdentity = ObjectIdentity
dhtRemoteSwitchObjects = _DhtRemoteSwitchObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 11, 1)
)
_DhtRemoteSwitchPresence_Type = TruthValue
_DhtRemoteSwitchPresence_Object = MibScalar
dhtRemoteSwitchPresence = _DhtRemoteSwitchPresence_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 11, 1, 1),
    _DhtRemoteSwitchPresence_Type()
)
dhtRemoteSwitchPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhtRemoteSwitchPresence.setStatus("current")
_DhtRemoteSwitchManagement_ObjectIdentity = ObjectIdentity
dhtRemoteSwitchManagement = _DhtRemoteSwitchManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 11, 1, 11)
)


class _DhtRemoteSwitchControl_Type(Integer32):
    """Custom type dhtRemoteSwitchControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_DhtRemoteSwitchControl_Type.__name__ = "Integer32"
_DhtRemoteSwitchControl_Object = MibScalar
dhtRemoteSwitchControl = _DhtRemoteSwitchControl_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 11, 1, 11, 1),
    _DhtRemoteSwitchControl_Type()
)
dhtRemoteSwitchControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhtRemoteSwitchControl.setStatus("current")


class _DhtRemoteSwitchAutoStopTimer_Type(Integer32):
    """Custom type dhtRemoteSwitchAutoStopTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 120),
    )


_DhtRemoteSwitchAutoStopTimer_Type.__name__ = "Integer32"
_DhtRemoteSwitchAutoStopTimer_Object = MibScalar
dhtRemoteSwitchAutoStopTimer = _DhtRemoteSwitchAutoStopTimer_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 11, 1, 11, 2),
    _DhtRemoteSwitchAutoStopTimer_Type()
)
dhtRemoteSwitchAutoStopTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhtRemoteSwitchAutoStopTimer.setStatus("current")


class _DhtRemoteSwitchStatus_Type(Integer32):
    """Custom type dhtRemoteSwitchStatus based on Integer32"""
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
        *(("on", 1),
          ("off", 2),
          ("mismatch", 3),
          ("timeout", 4))
    )


_DhtRemoteSwitchStatus_Type.__name__ = "Integer32"
_DhtRemoteSwitchStatus_Object = MibScalar
dhtRemoteSwitchStatus = _DhtRemoteSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 11, 1, 11, 3),
    _DhtRemoteSwitchStatus_Type()
)
dhtRemoteSwitchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhtRemoteSwitchStatus.setStatus("current")
_DhtRemoteSwitchOnTime_Type = Counter32
_DhtRemoteSwitchOnTime_Object = MibScalar
dhtRemoteSwitchOnTime = _DhtRemoteSwitchOnTime_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 11, 1, 11, 4),
    _DhtRemoteSwitchOnTime_Type()
)
dhtRemoteSwitchOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhtRemoteSwitchOnTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELECTROLINE-DHT-REMOTE-SWITCH-MIB",
    **{"dhtRemoteSwitchMib": dhtRemoteSwitchMib,
       "dhtRemoteSwitchObjects": dhtRemoteSwitchObjects,
       "dhtRemoteSwitchPresence": dhtRemoteSwitchPresence,
       "dhtRemoteSwitchManagement": dhtRemoteSwitchManagement,
       "dhtRemoteSwitchControl": dhtRemoteSwitchControl,
       "dhtRemoteSwitchAutoStopTimer": dhtRemoteSwitchAutoStopTimer,
       "dhtRemoteSwitchStatus": dhtRemoteSwitchStatus,
       "dhtRemoteSwitchOnTime": dhtRemoteSwitchOnTime}
)
