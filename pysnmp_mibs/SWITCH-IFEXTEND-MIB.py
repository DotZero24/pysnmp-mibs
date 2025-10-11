# SNMP MIB module (SWITCH-IFEXTEND-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/SWITCH-IFEXTEND-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:41 2025
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

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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

rcIfExtend = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 20)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcIfExtendMib_ObjectIdentity = ObjectIdentity
rcIfExtendMib = _RcIfExtendMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 20, 1)
)
_RcIfExtendTable_Object = MibTable
rcIfExtendTable = _RcIfExtendTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 20, 1, 1)
)
if mibBuilder.loadTexts:
    rcIfExtendTable.setStatus("current")
_RcIfExtendEntry_Object = MibTableRow
rcIfExtendEntry = _RcIfExtendEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 20, 1, 1, 1)
)
rcIfExtendEntry.setIndexNames(
    (0, "SWITCH-IFEXTEND-MIB", "rcIfindex"),
)
if mibBuilder.loadTexts:
    rcIfExtendEntry.setStatus("current")
_RcIfindex_Type = Integer32
_RcIfindex_Object = MibTableColumn
rcIfindex = _RcIfindex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 20, 1, 1, 1, 1),
    _RcIfindex_Type()
)
rcIfindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcIfindex.setStatus("current")
_RcIfDescription_Type = OctetString
_RcIfDescription_Object = MibTableColumn
rcIfDescription = _RcIfDescription_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 20, 1, 1, 1, 2),
    _RcIfDescription_Type()
)
rcIfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIfDescription.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-IFEXTEND-MIB",
    **{"rcIfExtend": rcIfExtend,
       "rcIfExtendMib": rcIfExtendMib,
       "rcIfExtendTable": rcIfExtendTable,
       "rcIfExtendEntry": rcIfExtendEntry,
       "rcIfindex": rcIfindex,
       "rcIfDescription": rcIfDescription}
)
