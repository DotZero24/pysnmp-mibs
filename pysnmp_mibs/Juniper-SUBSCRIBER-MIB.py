# SNMP MIB module (Juniper-SUBSCRIBER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/junose/JUNIPER-SUBSCRIBER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:38:09 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniEnable,) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniEnable")

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

juniSubscriberMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49)
)
if mibBuilder.loadTexts:
    juniSubscriberMIB.setRevisions(
        ("2002-09-16 21:44",
         "2002-05-10 19:53",
         "2000-11-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniSubscrEncaps(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              19)
        )
    )
    namedValues = NamedValues(
        *(("ip", 0),
          ("bridgedEthernet", 19))
    )



# MIB Managed Objects in the order of their OIDs

_JuniSubscrObjects_ObjectIdentity = ObjectIdentity
juniSubscrObjects = _JuniSubscrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1)
)
_JuniSubscrLocal_ObjectIdentity = ObjectIdentity
juniSubscrLocal = _JuniSubscrLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1)
)
_JuniSubscrLocalTable_Object = MibTable
juniSubscrLocalTable = _JuniSubscrLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1)
)
if mibBuilder.loadTexts:
    juniSubscrLocalTable.setStatus("current")
_JuniSubscrLocalEntry_Object = MibTableRow
juniSubscrLocalEntry = _JuniSubscrLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1)
)
juniSubscrLocalEntry.setIndexNames(
    (0, "Juniper-SUBSCRIBER-MIB", "juniSubscrLocalIfIndex"),
    (0, "Juniper-SUBSCRIBER-MIB", "juniSubscrLocalEncaps"),
)
if mibBuilder.loadTexts:
    juniSubscrLocalEntry.setStatus("current")
_JuniSubscrLocalIfIndex_Type = InterfaceIndex
_JuniSubscrLocalIfIndex_Object = MibTableColumn
juniSubscrLocalIfIndex = _JuniSubscrLocalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 1),
    _JuniSubscrLocalIfIndex_Type()
)
juniSubscrLocalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniSubscrLocalIfIndex.setStatus("current")
_JuniSubscrLocalEncaps_Type = JuniSubscrEncaps
_JuniSubscrLocalEncaps_Object = MibTableColumn
juniSubscrLocalEncaps = _JuniSubscrLocalEncaps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 2),
    _JuniSubscrLocalEncaps_Type()
)
juniSubscrLocalEncaps.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniSubscrLocalEncaps.setStatus("current")


class _JuniSubscrLocalControl_Type(Integer32):
    """Custom type juniSubscrLocalControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("clear", 1))
    )


_JuniSubscrLocalControl_Type.__name__ = "Integer32"
_JuniSubscrLocalControl_Object = MibTableColumn
juniSubscrLocalControl = _JuniSubscrLocalControl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 3),
    _JuniSubscrLocalControl_Type()
)
juniSubscrLocalControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSubscrLocalControl.setStatus("current")
_JuniSubscrLocalNamePrefix_Type = JuniEnable
_JuniSubscrLocalNamePrefix_Object = MibTableColumn
juniSubscrLocalNamePrefix = _JuniSubscrLocalNamePrefix_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 4),
    _JuniSubscrLocalNamePrefix_Type()
)
juniSubscrLocalNamePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSubscrLocalNamePrefix.setStatus("current")


class _JuniSubscrLocalName_Type(DisplayString):
    """Custom type juniSubscrLocalName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_JuniSubscrLocalName_Type.__name__ = "DisplayString"
_JuniSubscrLocalName_Object = MibTableColumn
juniSubscrLocalName = _JuniSubscrLocalName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 5),
    _JuniSubscrLocalName_Type()
)
juniSubscrLocalName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSubscrLocalName.setStatus("current")
_JuniSubscrLocalPasswordPrefix_Type = JuniEnable
_JuniSubscrLocalPasswordPrefix_Object = MibTableColumn
juniSubscrLocalPasswordPrefix = _JuniSubscrLocalPasswordPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 6),
    _JuniSubscrLocalPasswordPrefix_Type()
)
juniSubscrLocalPasswordPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSubscrLocalPasswordPrefix.setStatus("current")


class _JuniSubscrLocalPassword_Type(DisplayString):
    """Custom type juniSubscrLocalPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_JuniSubscrLocalPassword_Type.__name__ = "DisplayString"
_JuniSubscrLocalPassword_Object = MibTableColumn
juniSubscrLocalPassword = _JuniSubscrLocalPassword_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 7),
    _JuniSubscrLocalPassword_Type()
)
juniSubscrLocalPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSubscrLocalPassword.setStatus("current")


class _JuniSubscrLocalDomain_Type(DisplayString):
    """Custom type juniSubscrLocalDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_JuniSubscrLocalDomain_Type.__name__ = "DisplayString"
_JuniSubscrLocalDomain_Object = MibTableColumn
juniSubscrLocalDomain = _JuniSubscrLocalDomain_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 8),
    _JuniSubscrLocalDomain_Type()
)
juniSubscrLocalDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSubscrLocalDomain.setStatus("current")


class _JuniSubscrLocalAuthentication_Type(JuniEnable):
    """Custom type juniSubscrLocalAuthentication based on JuniEnable"""
    defaultValue = 1


_JuniSubscrLocalAuthentication_Type.__name__ = "JuniEnable"
_JuniSubscrLocalAuthentication_Object = MibTableColumn
juniSubscrLocalAuthentication = _JuniSubscrLocalAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 9),
    _JuniSubscrLocalAuthentication_Type()
)
juniSubscrLocalAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSubscrLocalAuthentication.setStatus("current")
_JuniSubscriberMIBConformance_ObjectIdentity = ObjectIdentity
juniSubscriberMIBConformance = _JuniSubscriberMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4)
)
_JuniSubscriberMIBCompliances_ObjectIdentity = ObjectIdentity
juniSubscriberMIBCompliances = _JuniSubscriberMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 1)
)
_JuniSubscriberMIBGroups_ObjectIdentity = ObjectIdentity
juniSubscriberMIBGroups = _JuniSubscriberMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 2)
)

# Managed Objects groups

juniSubscriberLocalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 2, 1)
)
juniSubscriberLocalGroup.setObjects(
      *(("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalControl"),
        ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalNamePrefix"),
        ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalName"),
        ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalPasswordPrefix"),
        ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalPassword"),
        ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalDomain"))
)
if mibBuilder.loadTexts:
    juniSubscriberLocalGroup.setStatus("obsolete")

juniSubscriberLocalGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 2, 2)
)
juniSubscriberLocalGroup2.setObjects(
      *(("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalControl"),
        ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalNamePrefix"),
        ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalName"),
        ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalPasswordPrefix"),
        ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalPassword"),
        ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalDomain"),
        ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalAuthentication"))
)
if mibBuilder.loadTexts:
    juniSubscriberLocalGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniSubscriberCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 1, 1)
)
juniSubscriberCompliance.setObjects(
    ("Juniper-SUBSCRIBER-MIB", "juniSubscriberLocalGroup")
)
if mibBuilder.loadTexts:
    juniSubscriberCompliance.setStatus(
        "obsolete"
    )

juniSubscriberCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 1, 2)
)
juniSubscriberCompliance2.setObjects(
    ("Juniper-SUBSCRIBER-MIB", "juniSubscriberLocalGroup2")
)
if mibBuilder.loadTexts:
    juniSubscriberCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-SUBSCRIBER-MIB",
    **{"JuniSubscrEncaps": JuniSubscrEncaps,
       "juniSubscriberMIB": juniSubscriberMIB,
       "juniSubscrObjects": juniSubscrObjects,
       "juniSubscrLocal": juniSubscrLocal,
       "juniSubscrLocalTable": juniSubscrLocalTable,
       "juniSubscrLocalEntry": juniSubscrLocalEntry,
       "juniSubscrLocalIfIndex": juniSubscrLocalIfIndex,
       "juniSubscrLocalEncaps": juniSubscrLocalEncaps,
       "juniSubscrLocalControl": juniSubscrLocalControl,
       "juniSubscrLocalNamePrefix": juniSubscrLocalNamePrefix,
       "juniSubscrLocalName": juniSubscrLocalName,
       "juniSubscrLocalPasswordPrefix": juniSubscrLocalPasswordPrefix,
       "juniSubscrLocalPassword": juniSubscrLocalPassword,
       "juniSubscrLocalDomain": juniSubscrLocalDomain,
       "juniSubscrLocalAuthentication": juniSubscrLocalAuthentication,
       "juniSubscriberMIBConformance": juniSubscriberMIBConformance,
       "juniSubscriberMIBCompliances": juniSubscriberMIBCompliances,
       "juniSubscriberCompliance": juniSubscriberCompliance,
       "juniSubscriberCompliance2": juniSubscriberCompliance2,
       "juniSubscriberMIBGroups": juniSubscriberMIBGroups,
       "juniSubscriberLocalGroup": juniSubscriberLocalGroup,
       "juniSubscriberLocalGroup2": juniSubscriberLocalGroup2}
)
