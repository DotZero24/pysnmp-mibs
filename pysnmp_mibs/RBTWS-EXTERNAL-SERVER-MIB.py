# SNMP MIB module (RBTWS-EXTERNAL-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cabletron/RBTWS-EXTERNAL-SERVER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:56:17 2025
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

(rbtwsMibs,) = mibBuilder.importSymbols(
    "RBTWS-ROOT-MIB",
    "rbtwsMibs")

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

rbtwsExternalServerMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7)
)
if mibBuilder.loadTexts:
    rbtwsExternalServerMib.setRevisions(
        ("2006-07-31 00:04",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RbtwsIpPort(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class RbtwsSyslogServerEnable(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )



# MIB Managed Objects in the order of their OIDs

_RbtwsExternalServerObjects_ObjectIdentity = ObjectIdentity
rbtwsExternalServerObjects = _RbtwsExternalServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1)
)
_RbtwsExternalServerDataObjects_ObjectIdentity = ObjectIdentity
rbtwsExternalServerDataObjects = _RbtwsExternalServerDataObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 1)
)
_RbtwsExtServerSyslogTable_Object = MibTable
rbtwsExtServerSyslogTable = _RbtwsExtServerSyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rbtwsExtServerSyslogTable.setStatus("current")
_RbtwsExtServerSyslogEntry_Object = MibTableRow
rbtwsExtServerSyslogEntry = _RbtwsExtServerSyslogEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 1, 1, 1)
)
rbtwsExtServerSyslogEntry.setIndexNames(
    (0, "RBTWS-EXTERNAL-SERVER-MIB", "rbtwsExtServerSyslogIndex"),
)
if mibBuilder.loadTexts:
    rbtwsExtServerSyslogEntry.setStatus("current")
_RbtwsExtServerSyslogIndex_Type = Unsigned32
_RbtwsExtServerSyslogIndex_Object = MibTableColumn
rbtwsExtServerSyslogIndex = _RbtwsExtServerSyslogIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 1, 1, 1, 1),
    _RbtwsExtServerSyslogIndex_Type()
)
rbtwsExtServerSyslogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsExtServerSyslogIndex.setStatus("current")
_RbtwsExtServerSyslogAddress_Type = IpAddress
_RbtwsExtServerSyslogAddress_Object = MibTableColumn
rbtwsExtServerSyslogAddress = _RbtwsExtServerSyslogAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 1, 1, 1, 2),
    _RbtwsExtServerSyslogAddress_Type()
)
rbtwsExtServerSyslogAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsExtServerSyslogAddress.setStatus("current")
_RbtwsExtServerSyslogPort_Type = RbtwsIpPort
_RbtwsExtServerSyslogPort_Object = MibTableColumn
rbtwsExtServerSyslogPort = _RbtwsExtServerSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 1, 1, 1, 3),
    _RbtwsExtServerSyslogPort_Type()
)
rbtwsExtServerSyslogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsExtServerSyslogPort.setStatus("current")
_RbtwsExtServerSyslogEnable_Type = RbtwsSyslogServerEnable
_RbtwsExtServerSyslogEnable_Object = MibTableColumn
rbtwsExtServerSyslogEnable = _RbtwsExtServerSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 1, 1, 1, 4),
    _RbtwsExtServerSyslogEnable_Type()
)
rbtwsExtServerSyslogEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsExtServerSyslogEnable.setStatus("current")
_RbtwsExternalServerConformance_ObjectIdentity = ObjectIdentity
rbtwsExternalServerConformance = _RbtwsExternalServerConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 2)
)
_RbtwsExternalServerCompliances_ObjectIdentity = ObjectIdentity
rbtwsExternalServerCompliances = _RbtwsExternalServerCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 2, 1)
)
_RbtwsExternalServerGroups_ObjectIdentity = ObjectIdentity
rbtwsExternalServerGroups = _RbtwsExternalServerGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 2, 2)
)

# Managed Objects groups

rbtwsExternalServerConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 2, 2, 1)
)
rbtwsExternalServerConfigGroup.setObjects(
      *(("RBTWS-EXTERNAL-SERVER-MIB", "rbtwsExtServerSyslogAddress"),
        ("RBTWS-EXTERNAL-SERVER-MIB", "rbtwsExtServerSyslogPort"),
        ("RBTWS-EXTERNAL-SERVER-MIB", "rbtwsExtServerSyslogEnable"))
)
if mibBuilder.loadTexts:
    rbtwsExternalServerConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbtwsExternalServerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 2, 1, 1)
)
rbtwsExternalServerCompliance.setObjects(
    ("RBTWS-EXTERNAL-SERVER-MIB", "rbtwsExternalServerConfigGroup")
)
if mibBuilder.loadTexts:
    rbtwsExternalServerCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBTWS-EXTERNAL-SERVER-MIB",
    **{"RbtwsIpPort": RbtwsIpPort,
       "RbtwsSyslogServerEnable": RbtwsSyslogServerEnable,
       "rbtwsExternalServerMib": rbtwsExternalServerMib,
       "rbtwsExternalServerObjects": rbtwsExternalServerObjects,
       "rbtwsExternalServerDataObjects": rbtwsExternalServerDataObjects,
       "rbtwsExtServerSyslogTable": rbtwsExtServerSyslogTable,
       "rbtwsExtServerSyslogEntry": rbtwsExtServerSyslogEntry,
       "rbtwsExtServerSyslogIndex": rbtwsExtServerSyslogIndex,
       "rbtwsExtServerSyslogAddress": rbtwsExtServerSyslogAddress,
       "rbtwsExtServerSyslogPort": rbtwsExtServerSyslogPort,
       "rbtwsExtServerSyslogEnable": rbtwsExtServerSyslogEnable,
       "rbtwsExternalServerConformance": rbtwsExternalServerConformance,
       "rbtwsExternalServerCompliances": rbtwsExternalServerCompliances,
       "rbtwsExternalServerCompliance": rbtwsExternalServerCompliance,
       "rbtwsExternalServerGroups": rbtwsExternalServerGroups,
       "rbtwsExternalServerConfigGroup": rbtwsExternalServerConfigGroup}
)
