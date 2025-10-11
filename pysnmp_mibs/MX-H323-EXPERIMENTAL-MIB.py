# SNMP MIB module (MX-H323-EXPERIMENTAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-H323-EXPERIMENTAL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:47 2025
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

(mediatrixExperimental,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixExperimental")

(MxEnableState,
 MxIpHostName) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState",
    "MxIpHostName")

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

h323ExperimentalMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 60)
)
if mibBuilder.loadTexts:
    h323ExperimentalMIB.setRevisions(
        ("2007-04-06 00:00",
         "2005-03-25 00:00",
         "2005-03-25 00:00",
         "2004-10-04 00:00",
         "2004-08-03 00:00",
         "2003-10-20 00:00",
         "2003-10-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H323ExperimentalMIBObjects_ObjectIdentity = ObjectIdentity
h323ExperimentalMIBObjects = _H323ExperimentalMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 60, 1)
)
_H323Interop_ObjectIdentity = ObjectIdentity
h323Interop = _H323Interop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 60, 1, 5)
)


class _H323RegAsGateway_Type(MxEnableState):
    """Custom type h323RegAsGateway based on MxEnableState"""
    defaultValue = 0


_H323RegAsGateway_Type.__name__ = "MxEnableState"
_H323RegAsGateway_Object = MibScalar
h323RegAsGateway = _H323RegAsGateway_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 60, 1, 5, 5),
    _H323RegAsGateway_Type()
)
h323RegAsGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323RegAsGateway.setStatus("current")


class _H323AliasTypeRestriction_Type(MxEnableState):
    """Custom type h323AliasTypeRestriction based on MxEnableState"""
    defaultValue = 1


_H323AliasTypeRestriction_Type.__name__ = "MxEnableState"
_H323AliasTypeRestriction_Object = MibScalar
h323AliasTypeRestriction = _H323AliasTypeRestriction_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 60, 1, 5, 15),
    _H323AliasTypeRestriction_Type()
)
h323AliasTypeRestriction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323AliasTypeRestriction.setStatus("current")


class _H323AcceleratedRequestedLogicalChannel_Type(MxEnableState):
    """Custom type h323AcceleratedRequestedLogicalChannel based on MxEnableState"""
    defaultValue = 0


_H323AcceleratedRequestedLogicalChannel_Type.__name__ = "MxEnableState"
_H323AcceleratedRequestedLogicalChannel_Object = MibScalar
h323AcceleratedRequestedLogicalChannel = _H323AcceleratedRequestedLogicalChannel_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 60, 1, 5, 18),
    _H323AcceleratedRequestedLogicalChannel_Type()
)
h323AcceleratedRequestedLogicalChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323AcceleratedRequestedLogicalChannel.setStatus("current")
_H323VoiceIfCodecTable_Object = MibTable
h323VoiceIfCodecTable = _H323VoiceIfCodecTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 60, 1, 5, 20)
)
if mibBuilder.loadTexts:
    h323VoiceIfCodecTable.setStatus("current")
_H323VoiceIfCodecEntry_Object = MibTableRow
h323VoiceIfCodecEntry = _H323VoiceIfCodecEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 60, 1, 5, 20, 1)
)
h323VoiceIfCodecEntry.setIndexNames(
    (0, "MX-H323-EXPERIMENTAL-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h323VoiceIfCodecEntry.setStatus("current")


class _H323VoiceIfCodecG729Enable_Type(MxEnableState):
    """Custom type h323VoiceIfCodecG729Enable based on MxEnableState"""
    defaultValue = 0


_H323VoiceIfCodecG729Enable_Type.__name__ = "MxEnableState"
_H323VoiceIfCodecG729Enable_Object = MibTableColumn
h323VoiceIfCodecG729Enable = _H323VoiceIfCodecG729Enable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 60, 1, 5, 20, 1, 5),
    _H323VoiceIfCodecG729Enable_Type()
)
h323VoiceIfCodecG729Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323VoiceIfCodecG729Enable.setStatus("current")


class _H323AddT38MediaControlChannel_Type(MxEnableState):
    """Custom type h323AddT38MediaControlChannel based on MxEnableState"""
    defaultValue = 0


_H323AddT38MediaControlChannel_Type.__name__ = "MxEnableState"
_H323AddT38MediaControlChannel_Object = MibScalar
h323AddT38MediaControlChannel = _H323AddT38MediaControlChannel_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 60, 1, 5, 50),
    _H323AddT38MediaControlChannel_Type()
)
h323AddT38MediaControlChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323AddT38MediaControlChannel.setStatus("current")


class _H323UseEvenT38Port_Type(MxEnableState):
    """Custom type h323UseEvenT38Port based on MxEnableState"""
    defaultValue = 0


_H323UseEvenT38Port_Type.__name__ = "MxEnableState"
_H323UseEvenT38Port_Object = MibScalar
h323UseEvenT38Port = _H323UseEvenT38Port_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 60, 1, 5, 100),
    _H323UseEvenT38Port_Type()
)
h323UseEvenT38Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323UseEvenT38Port.setStatus("current")
_H323ExperimentalConformance_ObjectIdentity = ObjectIdentity
h323ExperimentalConformance = _H323ExperimentalConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 60, 2)
)
_H323ExperimentalCompliances_ObjectIdentity = ObjectIdentity
h323ExperimentalCompliances = _H323ExperimentalCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 60, 2, 1)
)
_H323ExperimentalGroups_ObjectIdentity = ObjectIdentity
h323ExperimentalGroups = _H323ExperimentalGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 60, 2, 2)
)

# Managed Objects groups

h323ExperimentalGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 99, 60, 2, 2, 5)
)
h323ExperimentalGroupVer1.setObjects(
      *(("MX-H323-EXPERIMENTAL-MIB", "h323RegAsGateway"),
        ("MX-H323-EXPERIMENTAL-MIB", "h323AddT38MediaControlChannel"),
        ("MX-H323-EXPERIMENTAL-MIB", "h323UseEvenT38Port"),
        ("MX-H323-EXPERIMENTAL-MIB", "h323VoiceIfCodecG729Enable"),
        ("MX-H323-EXPERIMENTAL-MIB", "h323AliasTypeRestriction"),
        ("MX-H323-EXPERIMENTAL-MIB", "h323AcceleratedRequestedLogicalChannel"))
)
if mibBuilder.loadTexts:
    h323ExperimentalGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

h323ExperimentalBasicComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 99, 60, 2, 1, 5)
)
h323ExperimentalBasicComplVer1.setObjects(
    ("MX-H323-EXPERIMENTAL-MIB", "h323ExperimentalGroupVer1")
)
if mibBuilder.loadTexts:
    h323ExperimentalBasicComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-H323-EXPERIMENTAL-MIB",
    **{"h323ExperimentalMIB": h323ExperimentalMIB,
       "h323ExperimentalMIBObjects": h323ExperimentalMIBObjects,
       "h323Interop": h323Interop,
       "h323RegAsGateway": h323RegAsGateway,
       "h323AliasTypeRestriction": h323AliasTypeRestriction,
       "h323AcceleratedRequestedLogicalChannel": h323AcceleratedRequestedLogicalChannel,
       "h323VoiceIfCodecTable": h323VoiceIfCodecTable,
       "h323VoiceIfCodecEntry": h323VoiceIfCodecEntry,
       "h323VoiceIfCodecG729Enable": h323VoiceIfCodecG729Enable,
       "h323AddT38MediaControlChannel": h323AddT38MediaControlChannel,
       "h323UseEvenT38Port": h323UseEvenT38Port,
       "h323ExperimentalConformance": h323ExperimentalConformance,
       "h323ExperimentalCompliances": h323ExperimentalCompliances,
       "h323ExperimentalBasicComplVer1": h323ExperimentalBasicComplVer1,
       "h323ExperimentalGroups": h323ExperimentalGroups,
       "h323ExperimentalGroupVer1": h323ExperimentalGroupVer1}
)
