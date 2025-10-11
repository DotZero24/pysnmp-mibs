# SNMP MIB module (H3C-OBJP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-OBJP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:19:37 2025
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

h3cObjp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 155)
)
if mibBuilder.loadTexts:
    h3cObjp.setRevisions(
        ("2014-03-10 15:36",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cObjpZonePairObjects_ObjectIdentity = ObjectIdentity
h3cObjpZonePairObjects = _H3cObjpZonePairObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 155, 1)
)
_H3cObjpZonePairRunningInfoTable_Object = MibTable
h3cObjpZonePairRunningInfoTable = _H3cObjpZonePairRunningInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 155, 1, 1)
)
if mibBuilder.loadTexts:
    h3cObjpZonePairRunningInfoTable.setStatus("current")
_H3cObjpZonePairRunningInfoEntry_Object = MibTableRow
h3cObjpZonePairRunningInfoEntry = _H3cObjpZonePairRunningInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 155, 1, 1, 1)
)
h3cObjpZonePairRunningInfoEntry.setIndexNames(
    (0, "H3C-OBJP-MIB", "h3cObjpZonePairSrcZone"),
    (0, "H3C-OBJP-MIB", "h3cObjpZonePairDstZone"),
    (0, "H3C-OBJP-MIB", "h3cObjpZonePairIPVersion"),
    (0, "H3C-OBJP-MIB", "h3cObjpZonePairRuleID"),
)
if mibBuilder.loadTexts:
    h3cObjpZonePairRunningInfoEntry.setStatus("current")


class _H3cObjpZonePairSrcZone_Type(OctetString):
    """Custom type h3cObjpZonePairSrcZone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cObjpZonePairSrcZone_Type.__name__ = "OctetString"
_H3cObjpZonePairSrcZone_Object = MibTableColumn
h3cObjpZonePairSrcZone = _H3cObjpZonePairSrcZone_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 155, 1, 1, 1, 1),
    _H3cObjpZonePairSrcZone_Type()
)
h3cObjpZonePairSrcZone.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cObjpZonePairSrcZone.setStatus("current")


class _H3cObjpZonePairDstZone_Type(OctetString):
    """Custom type h3cObjpZonePairDstZone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cObjpZonePairDstZone_Type.__name__ = "OctetString"
_H3cObjpZonePairDstZone_Object = MibTableColumn
h3cObjpZonePairDstZone = _H3cObjpZonePairDstZone_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 155, 1, 1, 1, 2),
    _H3cObjpZonePairDstZone_Type()
)
h3cObjpZonePairDstZone.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cObjpZonePairDstZone.setStatus("current")


class _H3cObjpZonePairIPVersion_Type(Integer32):
    """Custom type h3cObjpZonePairIPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_H3cObjpZonePairIPVersion_Type.__name__ = "Integer32"
_H3cObjpZonePairIPVersion_Object = MibTableColumn
h3cObjpZonePairIPVersion = _H3cObjpZonePairIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 155, 1, 1, 1, 3),
    _H3cObjpZonePairIPVersion_Type()
)
h3cObjpZonePairIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cObjpZonePairIPVersion.setStatus("current")


class _H3cObjpZonePairRuleID_Type(Unsigned32):
    """Custom type h3cObjpZonePairRuleID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_H3cObjpZonePairRuleID_Type.__name__ = "Unsigned32"
_H3cObjpZonePairRuleID_Object = MibTableColumn
h3cObjpZonePairRuleID = _H3cObjpZonePairRuleID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 155, 1, 1, 1, 4),
    _H3cObjpZonePairRuleID_Type()
)
h3cObjpZonePairRuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cObjpZonePairRuleID.setStatus("current")
_H3cObjpZonePairMatchPacketCount_Type = Counter64
_H3cObjpZonePairMatchPacketCount_Object = MibTableColumn
h3cObjpZonePairMatchPacketCount = _H3cObjpZonePairMatchPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 155, 1, 1, 1, 5),
    _H3cObjpZonePairMatchPacketCount_Type()
)
h3cObjpZonePairMatchPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cObjpZonePairMatchPacketCount.setStatus("current")
_H3cObjpZonePairLastMatchTime_Type = Unsigned32
_H3cObjpZonePairLastMatchTime_Object = MibTableColumn
h3cObjpZonePairLastMatchTime = _H3cObjpZonePairLastMatchTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 155, 1, 1, 1, 6),
    _H3cObjpZonePairLastMatchTime_Type()
)
h3cObjpZonePairLastMatchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cObjpZonePairLastMatchTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-OBJP-MIB",
    **{"h3cObjp": h3cObjp,
       "h3cObjpZonePairObjects": h3cObjpZonePairObjects,
       "h3cObjpZonePairRunningInfoTable": h3cObjpZonePairRunningInfoTable,
       "h3cObjpZonePairRunningInfoEntry": h3cObjpZonePairRunningInfoEntry,
       "h3cObjpZonePairSrcZone": h3cObjpZonePairSrcZone,
       "h3cObjpZonePairDstZone": h3cObjpZonePairDstZone,
       "h3cObjpZonePairIPVersion": h3cObjpZonePairIPVersion,
       "h3cObjpZonePairRuleID": h3cObjpZonePairRuleID,
       "h3cObjpZonePairMatchPacketCount": h3cObjpZonePairMatchPacketCount,
       "h3cObjpZonePairLastMatchTime": h3cObjpZonePairLastMatchTime}
)
