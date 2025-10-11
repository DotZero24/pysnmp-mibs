# SNMP MIB module (H3C-MACSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-MACSEC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:20:32 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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


# MODULE-IDENTITY

h3cMACsec = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 163)
)
if mibBuilder.loadTexts:
    h3cMACsec.setRevisions(
        ("2015-09-01 16:15",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cMACsecCFGObjects_ObjectIdentity = ObjectIdentity
h3cMACsecCFGObjects = _H3cMACsecCFGObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 163, 1)
)
_H3cMACsecCFGPortTable_Object = MibTable
h3cMACsecCFGPortTable = _H3cMACsecCFGPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 163, 1, 1)
)
if mibBuilder.loadTexts:
    h3cMACsecCFGPortTable.setStatus("current")
_H3cMACsecCFGPortEntry_Object = MibTableRow
h3cMACsecCFGPortEntry = _H3cMACsecCFGPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 163, 1, 1, 1)
)
h3cMACsecCFGPortEntry.setIndexNames(
    (0, "H3C-MACSEC-MIB", "h3cMACsecCFGPortIndex"),
)
if mibBuilder.loadTexts:
    h3cMACsecCFGPortEntry.setStatus("current")
_H3cMACsecCFGPortIndex_Type = InterfaceIndex
_H3cMACsecCFGPortIndex_Object = MibTableColumn
h3cMACsecCFGPortIndex = _H3cMACsecCFGPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 163, 1, 1, 1, 1),
    _H3cMACsecCFGPortIndex_Type()
)
h3cMACsecCFGPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMACsecCFGPortIndex.setStatus("current")


class _H3cMACsecCFGPortPSKCKNName_Type(OctetString):
    """Custom type h3cMACsecCFGPortPSKCKNName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_H3cMACsecCFGPortPSKCKNName_Type.__name__ = "OctetString"
_H3cMACsecCFGPortPSKCKNName_Object = MibTableColumn
h3cMACsecCFGPortPSKCKNName = _H3cMACsecCFGPortPSKCKNName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 163, 1, 1, 1, 2),
    _H3cMACsecCFGPortPSKCKNName_Type()
)
h3cMACsecCFGPortPSKCKNName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMACsecCFGPortPSKCKNName.setStatus("current")


class _H3cMACsecCFGPortPSKCAKValue_Type(OctetString):
    """Custom type h3cMACsecCFGPortPSKCAKValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_H3cMACsecCFGPortPSKCAKValue_Type.__name__ = "OctetString"
_H3cMACsecCFGPortPSKCAKValue_Object = MibTableColumn
h3cMACsecCFGPortPSKCAKValue = _H3cMACsecCFGPortPSKCAKValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 163, 1, 1, 1, 3),
    _H3cMACsecCFGPortPSKCAKValue_Type()
)
h3cMACsecCFGPortPSKCAKValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMACsecCFGPortPSKCAKValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-MACSEC-MIB",
    **{"h3cMACsec": h3cMACsec,
       "h3cMACsecCFGObjects": h3cMACsecCFGObjects,
       "h3cMACsecCFGPortTable": h3cMACsecCFGPortTable,
       "h3cMACsecCFGPortEntry": h3cMACsecCFGPortEntry,
       "h3cMACsecCFGPortIndex": h3cMACsecCFGPortIndex,
       "h3cMACsecCFGPortPSKCKNName": h3cMACsecCFGPortPSKCKNName,
       "h3cMACsecCFGPortPSKCAKValue": h3cMACsecCFGPortPSKCAKValue}
)
