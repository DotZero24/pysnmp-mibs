# SNMP MIB module (QTECH-CPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-CPP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:13 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

qtechCPPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 132)
)
if mibBuilder.loadTexts:
    qtechCPPMIB.setRevisions(
        ("2014-12-19 21:00",
         "2014-12-19 21:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechCPPMIBObjects_ObjectIdentity = ObjectIdentity
qtechCPPMIBObjects = _QtechCPPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 132, 1)
)
_QtechCPPTable_Object = MibTable
qtechCPPTable = _QtechCPPTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 132, 1, 1)
)
if mibBuilder.loadTexts:
    qtechCPPTable.setStatus("current")
_QtechCPPEntry_Object = MibTableRow
qtechCPPEntry = _QtechCPPEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 132, 1, 1, 1)
)
qtechCPPEntry.setIndexNames(
    (0, "QTECH-CPP-MIB", "cppIndex"),
)
if mibBuilder.loadTexts:
    qtechCPPEntry.setStatus("current")


class _CppIndex_Type(Integer32):
    """Custom type cppIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CppIndex_Type.__name__ = "Integer32"
_CppIndex_Object = MibTableColumn
cppIndex = _CppIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 132, 1, 1, 1, 1),
    _CppIndex_Type()
)
cppIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppIndex.setStatus("current")


class _CppDeviceId_Type(Integer32):
    """Custom type cppDeviceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CppDeviceId_Type.__name__ = "Integer32"
_CppDeviceId_Object = MibTableColumn
cppDeviceId = _CppDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 132, 1, 1, 1, 2),
    _CppDeviceId_Type()
)
cppDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppDeviceId.setStatus("current")


class _CppSlotId_Type(Integer32):
    """Custom type cppSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CppSlotId_Type.__name__ = "Integer32"
_CppSlotId_Object = MibTableColumn
cppSlotId = _CppSlotId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 132, 1, 1, 1, 3),
    _CppSlotId_Type()
)
cppSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppSlotId.setStatus("current")


class _CppCardIndex_Type(DisplayString):
    """Custom type cppCardIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CppCardIndex_Type.__name__ = "DisplayString"
_CppCardIndex_Object = MibTableColumn
cppCardIndex = _CppCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 132, 1, 1, 1, 4),
    _CppCardIndex_Type()
)
cppCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppCardIndex.setStatus("current")


class _CppPacketType_Type(DisplayString):
    """Custom type cppPacketType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CppPacketType_Type.__name__ = "DisplayString"
_CppPacketType_Object = MibTableColumn
cppPacketType = _CppPacketType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 132, 1, 1, 1, 5),
    _CppPacketType_Type()
)
cppPacketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppPacketType.setStatus("current")


class _CppTrafficClass_Type(Integer32):
    """Custom type cppTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CppTrafficClass_Type.__name__ = "Integer32"
_CppTrafficClass_Object = MibTableColumn
cppTrafficClass = _CppTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 132, 1, 1, 1, 6),
    _CppTrafficClass_Type()
)
cppTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppTrafficClass.setStatus("current")


class _CppBandwidth_Type(Integer32):
    """Custom type cppBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CppBandwidth_Type.__name__ = "Integer32"
_CppBandwidth_Object = MibTableColumn
cppBandwidth = _CppBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 132, 1, 1, 1, 7),
    _CppBandwidth_Type()
)
cppBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppBandwidth.setStatus("current")


class _CppRate_Type(Integer32):
    """Custom type cppRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CppRate_Type.__name__ = "Integer32"
_CppRate_Object = MibTableColumn
cppRate = _CppRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 132, 1, 1, 1, 8),
    _CppRate_Type()
)
cppRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppRate.setStatus("current")


class _CppDrop_Type(Integer32):
    """Custom type cppDrop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CppDrop_Type.__name__ = "Integer32"
_CppDrop_Object = MibTableColumn
cppDrop = _CppDrop_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 132, 1, 1, 1, 9),
    _CppDrop_Type()
)
cppDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppDrop.setStatus("current")


class _CppTotal_Type(Integer32):
    """Custom type cppTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CppTotal_Type.__name__ = "Integer32"
_CppTotal_Object = MibTableColumn
cppTotal = _CppTotal_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 132, 1, 1, 1, 10),
    _CppTotal_Type()
)
cppTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppTotal.setStatus("current")


class _CppTotalDrop_Type(Integer32):
    """Custom type cppTotalDrop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CppTotalDrop_Type.__name__ = "Integer32"
_CppTotalDrop_Object = MibTableColumn
cppTotalDrop = _CppTotalDrop_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 132, 1, 1, 1, 11),
    _CppTotalDrop_Type()
)
cppTotalDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppTotalDrop.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-CPP-MIB",
    **{"qtechCPPMIB": qtechCPPMIB,
       "qtechCPPMIBObjects": qtechCPPMIBObjects,
       "qtechCPPTable": qtechCPPTable,
       "qtechCPPEntry": qtechCPPEntry,
       "cppIndex": cppIndex,
       "cppDeviceId": cppDeviceId,
       "cppSlotId": cppSlotId,
       "cppCardIndex": cppCardIndex,
       "cppPacketType": cppPacketType,
       "cppTrafficClass": cppTrafficClass,
       "cppBandwidth": cppBandwidth,
       "cppRate": cppRate,
       "cppDrop": cppDrop,
       "cppTotal": cppTotal,
       "cppTotalDrop": cppTotalDrop}
)
