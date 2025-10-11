# SNMP MIB module (NTWS-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/NTWS-PORT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:18:59 2025
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

(NtwsPhysPortNumber,
 NtwsPhysPortNumberOrZero) = mibBuilder.importSymbols(
    "NTWS-BASIC-TC",
    "NtwsPhysPortNumber",
    "NtwsPhysPortNumberOrZero")

(ntwsMibs,) = mibBuilder.importSymbols(
    "NTWS-ROOT-MIB",
    "ntwsMibs")

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

ntwsPortMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6)
)
if mibBuilder.loadTexts:
    ntwsPortMib.setRevisions(
        ("2008-10-23 00:10",
         "2008-05-19 00:04",
         "2007-08-16 00:02",
         "2006-11-09 00:01",
         "2006-04-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NtwsPortMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("directAttachAP", 1),
          ("networkPort", 2),
          ("wired", 3))
    )



class NtwsPortPoeMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("poeEnable", 1),
          ("poeDisable", 2))
    )



# MIB Managed Objects in the order of their OIDs

_NtwsPortObjects_ObjectIdentity = ObjectIdentity
ntwsPortObjects = _NtwsPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1)
)
_NtwsPortDataObjects_ObjectIdentity = ObjectIdentity
ntwsPortDataObjects = _NtwsPortDataObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 1)
)
_NtwsPortConfigTable_Object = MibTable
ntwsPortConfigTable = _NtwsPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ntwsPortConfigTable.setStatus("current")
_NtwsPortConfigEntry_Object = MibTableRow
ntwsPortConfigEntry = _NtwsPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 1, 1, 1)
)
ntwsPortConfigEntry.setIndexNames(
    (0, "NTWS-PORT-MIB", "ntwsPortConfigPortNumber"),
)
if mibBuilder.loadTexts:
    ntwsPortConfigEntry.setStatus("current")
_NtwsPortConfigPortNumber_Type = NtwsPhysPortNumber
_NtwsPortConfigPortNumber_Object = MibTableColumn
ntwsPortConfigPortNumber = _NtwsPortConfigPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 1, 1, 1, 1),
    _NtwsPortConfigPortNumber_Type()
)
ntwsPortConfigPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsPortConfigPortNumber.setStatus("current")
_NtwsPortConfigPortMode_Type = NtwsPortMode
_NtwsPortConfigPortMode_Object = MibTableColumn
ntwsPortConfigPortMode = _NtwsPortConfigPortMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 1, 1, 1, 2),
    _NtwsPortConfigPortMode_Type()
)
ntwsPortConfigPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsPortConfigPortMode.setStatus("current")
_NtwsPortConfigPoeMode_Type = NtwsPortPoeMode
_NtwsPortConfigPoeMode_Object = MibTableColumn
ntwsPortConfigPoeMode = _NtwsPortConfigPoeMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 1, 1, 1, 3),
    _NtwsPortConfigPoeMode_Type()
)
ntwsPortConfigPoeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsPortConfigPoeMode.setStatus("current")
_NtwsPortConfigTrunkMaster_Type = NtwsPhysPortNumberOrZero
_NtwsPortConfigTrunkMaster_Object = MibTableColumn
ntwsPortConfigTrunkMaster = _NtwsPortConfigTrunkMaster_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 1, 1, 1, 4),
    _NtwsPortConfigTrunkMaster_Type()
)
ntwsPortConfigTrunkMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsPortConfigTrunkMaster.setStatus("current")
_NtwsPortConformance_ObjectIdentity = ObjectIdentity
ntwsPortConformance = _NtwsPortConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 2)
)
_NtwsPortCompliances_ObjectIdentity = ObjectIdentity
ntwsPortCompliances = _NtwsPortCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 2, 1)
)
_NtwsPortGroups_ObjectIdentity = ObjectIdentity
ntwsPortGroups = _NtwsPortGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 2, 2)
)

# Managed Objects groups

ntwsPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 2, 2, 1)
)
ntwsPortConfigGroup.setObjects(
      *(("NTWS-PORT-MIB", "ntwsPortConfigPortMode"),
        ("NTWS-PORT-MIB", "ntwsPortConfigPoeMode"),
        ("NTWS-PORT-MIB", "ntwsPortConfigTrunkMaster"))
)
if mibBuilder.loadTexts:
    ntwsPortConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntwsPortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 2, 1, 1)
)
ntwsPortCompliance.setObjects(
    ("NTWS-PORT-MIB", "ntwsPortConfigGroup")
)
if mibBuilder.loadTexts:
    ntwsPortCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTWS-PORT-MIB",
    **{"NtwsPortMode": NtwsPortMode,
       "NtwsPortPoeMode": NtwsPortPoeMode,
       "ntwsPortMib": ntwsPortMib,
       "ntwsPortObjects": ntwsPortObjects,
       "ntwsPortDataObjects": ntwsPortDataObjects,
       "ntwsPortConfigTable": ntwsPortConfigTable,
       "ntwsPortConfigEntry": ntwsPortConfigEntry,
       "ntwsPortConfigPortNumber": ntwsPortConfigPortNumber,
       "ntwsPortConfigPortMode": ntwsPortConfigPortMode,
       "ntwsPortConfigPoeMode": ntwsPortConfigPoeMode,
       "ntwsPortConfigTrunkMaster": ntwsPortConfigTrunkMaster,
       "ntwsPortConformance": ntwsPortConformance,
       "ntwsPortCompliances": ntwsPortCompliances,
       "ntwsPortCompliance": ntwsPortCompliance,
       "ntwsPortGroups": ntwsPortGroups,
       "ntwsPortConfigGroup": ntwsPortConfigGroup}
)
