# SNMP MIB module (TN-LOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TN-LOG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:00:22 2025
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

(TNamedItem,) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "TNamedItem")

(tnSRMIBModules,
 tnSRObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSRMIBModules",
    "tnSRObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnSRLogMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 12)
)
if mibBuilder.loadTexts:
    tnSRLogMIBModule.setRevisions(
        ("2012-12-05 00:00",
         "2009-02-28 00:00",
         "2008-01-01 00:00",
         "2007-01-01 00:00",
         "2006-03-15 00:00",
         "2005-01-24 00:00",
         "2004-05-27 00:00",
         "2004-01-15 00:00",
         "2003-08-15 00:00",
         "2003-01-20 00:00",
         "2001-11-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnSRLogObjs_ObjectIdentity = ObjectIdentity
tnSRLogObjs = _TnSRLogObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 12)
)
_TnEventAppTable_Object = MibTable
tnEventAppTable = _TnEventAppTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 12, 9)
)
if mibBuilder.loadTexts:
    tnEventAppTable.setStatus("current")
_TnEventAppEntry_Object = MibTableRow
tnEventAppEntry = _TnEventAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 12, 9, 1)
)
tnEventAppEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-LOG-MIB", "tnEventAppIndex"),
)
if mibBuilder.loadTexts:
    tnEventAppEntry.setStatus("current")
_TnEventAppIndex_Type = Unsigned32
_TnEventAppIndex_Object = MibTableColumn
tnEventAppIndex = _TnEventAppIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 12, 9, 1, 1),
    _TnEventAppIndex_Type()
)
tnEventAppIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEventAppIndex.setStatus("current")
_TnEventAppName_Type = TNamedItem
_TnEventAppName_Object = MibTableColumn
tnEventAppName = _TnEventAppName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 12, 9, 1, 2),
    _TnEventAppName_Type()
)
tnEventAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEventAppName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-LOG-MIB",
    **{"tnSRLogMIBModule": tnSRLogMIBModule,
       "tnSRLogObjs": tnSRLogObjs,
       "tnEventAppTable": tnEventAppTable,
       "tnEventAppEntry": tnEventAppEntry,
       "tnEventAppIndex": tnEventAppIndex,
       "tnEventAppName": tnEventAppName}
)
