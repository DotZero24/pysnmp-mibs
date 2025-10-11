# SNMP MIB module (ONEACCESS-ATM-AAL5-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/oneaccess/ONEACCESS-ATM-AAL5-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:44 2025
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

(atmVclVci,
 atmVclVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVclVci",
    "atmVclVpi")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(oacExpIMAtmAal5,
 oacMIBModules,
 oacRequirements) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMAtmAal5",
    "oacMIBModules",
    "oacRequirements")

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

oacAtmAal5MIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 100, 800)
)
if mibBuilder.loadTexts:
    oacAtmAal5MIBModule.setRevisions(
        ("2011-10-27 00:00",
         "2010-07-08 10:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OacExpIMAtmAal5Conformance_ObjectIdentity = ObjectIdentity
oacExpIMAtmAal5Conformance = _OacExpIMAtmAal5Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 5, 800)
)
_OacExpIMAtmAal5Groups_ObjectIdentity = ObjectIdentity
oacExpIMAtmAal5Groups = _OacExpIMAtmAal5Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 5, 800, 1)
)
_OacExpIMAtmAal5Compliances_ObjectIdentity = ObjectIdentity
oacExpIMAtmAal5Compliances = _OacExpIMAtmAal5Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 5, 800, 2)
)
_OacExpIMAtmAal5Objects_ObjectIdentity = ObjectIdentity
oacExpIMAtmAal5Objects = _OacExpIMAtmAal5Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 3, 1)
)
_OacExpIMAtmAal5VclLogicalIndexTable_Object = MibTable
oacExpIMAtmAal5VclLogicalIndexTable = _OacExpIMAtmAal5VclLogicalIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    oacExpIMAtmAal5VclLogicalIndexTable.setStatus("current")
_OacExpIMAtmAal5VclLogicalIndexEntry_Object = MibTableRow
oacExpIMAtmAal5VclLogicalIndexEntry = _OacExpIMAtmAal5VclLogicalIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 3, 1, 1, 1)
)
oacExpIMAtmAal5VclLogicalIndexEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    oacExpIMAtmAal5VclLogicalIndexEntry.setStatus("current")
_OacExpIMAtmAal5VclLogicalIndexIfIndex_Type = InterfaceIndex
_OacExpIMAtmAal5VclLogicalIndexIfIndex_Object = MibTableColumn
oacExpIMAtmAal5VclLogicalIndexIfIndex = _OacExpIMAtmAal5VclLogicalIndexIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 3, 1, 1, 1, 1),
    _OacExpIMAtmAal5VclLogicalIndexIfIndex_Type()
)
oacExpIMAtmAal5VclLogicalIndexIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacExpIMAtmAal5VclLogicalIndexIfIndex.setStatus("current")
_OacExpIMAtmAal5Notifications_ObjectIdentity = ObjectIdentity
oacExpIMAtmAal5Notifications = _OacExpIMAtmAal5Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 3, 2)
)

# Managed Objects groups

oacExpIMAtmAal5GeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13191, 5, 800, 1, 1)
)
oacExpIMAtmAal5GeneralGroup.setObjects(
    ("ONEACCESS-ATM-AAL5-MIB", "oacExpIMAtmAal5VclLogicalIndexIfIndex")
)
if mibBuilder.loadTexts:
    oacExpIMAtmAal5GeneralGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oacExpIMAtmAal5Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13191, 5, 800, 2, 1)
)
oacExpIMAtmAal5Compliance.setObjects(
    ("ONEACCESS-ATM-AAL5-MIB", "oacExpIMAtmAal5GeneralGroup")
)
if mibBuilder.loadTexts:
    oacExpIMAtmAal5Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEACCESS-ATM-AAL5-MIB",
    **{"oacAtmAal5MIBModule": oacAtmAal5MIBModule,
       "oacExpIMAtmAal5Conformance": oacExpIMAtmAal5Conformance,
       "oacExpIMAtmAal5Groups": oacExpIMAtmAal5Groups,
       "oacExpIMAtmAal5GeneralGroup": oacExpIMAtmAal5GeneralGroup,
       "oacExpIMAtmAal5Compliances": oacExpIMAtmAal5Compliances,
       "oacExpIMAtmAal5Compliance": oacExpIMAtmAal5Compliance,
       "oacExpIMAtmAal5Objects": oacExpIMAtmAal5Objects,
       "oacExpIMAtmAal5VclLogicalIndexTable": oacExpIMAtmAal5VclLogicalIndexTable,
       "oacExpIMAtmAal5VclLogicalIndexEntry": oacExpIMAtmAal5VclLogicalIndexEntry,
       "oacExpIMAtmAal5VclLogicalIndexIfIndex": oacExpIMAtmAal5VclLogicalIndexIfIndex,
       "oacExpIMAtmAal5Notifications": oacExpIMAtmAal5Notifications}
)
