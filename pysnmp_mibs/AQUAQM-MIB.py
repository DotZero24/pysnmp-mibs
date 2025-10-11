# SNMP MIB module (AQUAQM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinet/AQUAQM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:05 2025
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

(wanflex,) = mibBuilder.importSymbols(
    "INFINET-MIB",
    "wanflex")

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

aquaqmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 4)
)
if mibBuilder.loadTexts:
    aquaqmMIB.setRevisions(
        ("2011-02-16 08:26",
         "2007-11-08 12:55",
         "2004-08-16 19:10")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QmTable_Object = MibTable
qmTable = _QmTable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    qmTable.setStatus("current")
_QmEntry_Object = MibTableRow
qmEntry = _QmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 4, 1, 1)
)
qmEntry.setIndexNames(
    (0, "AQUAQM-MIB", "qmChannel"),
)
if mibBuilder.loadTexts:
    qmEntry.setStatus("current")


class _QmChannel_Type(Integer32):
    """Custom type qmChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_QmChannel_Type.__name__ = "Integer32"
_QmChannel_Object = MibTableColumn
qmChannel = _QmChannel_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 4, 1, 1, 1),
    _QmChannel_Type()
)
qmChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmChannel.setStatus("current")


class _QmPriority_Type(Integer32):
    """Custom type qmPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QmPriority_Type.__name__ = "Integer32"
_QmPriority_Object = MibTableColumn
qmPriority = _QmPriority_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 4, 1, 1, 2),
    _QmPriority_Type()
)
qmPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmPriority.setStatus("current")


class _QmClass_Type(Integer32):
    """Custom type qmClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_QmClass_Type.__name__ = "Integer32"
_QmClass_Object = MibTableColumn
qmClass = _QmClass_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 4, 1, 1, 3),
    _QmClass_Type()
)
qmClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmClass.setStatus("current")
_QmTo_Type = IpAddress
_QmTo_Object = MibTableColumn
qmTo = _QmTo_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 4, 1, 1, 4),
    _QmTo_Type()
)
qmTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmTo.setStatus("current")


class _QmMax_Type(Integer32):
    """Custom type qmMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_QmMax_Type.__name__ = "Integer32"
_QmMax_Object = MibTableColumn
qmMax = _QmMax_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 4, 1, 1, 5),
    _QmMax_Type()
)
qmMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmMax.setStatus("current")


class _QmMaxPps_Type(Integer32):
    """Custom type qmMaxPps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QmMaxPps_Type.__name__ = "Integer32"
_QmMaxPps_Object = MibTableColumn
qmMaxPps = _QmMaxPps_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 4, 1, 1, 6),
    _QmMaxPps_Type()
)
qmMaxPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmMaxPps.setStatus("current")
_QmCur_Type = Integer32
_QmCur_Object = MibTableColumn
qmCur = _QmCur_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 4, 1, 1, 7),
    _QmCur_Type()
)
qmCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmCur.setStatus("current")
_QmCurPps_Type = Integer32
_QmCurPps_Object = MibTableColumn
qmCurPps = _QmCurPps_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 4, 1, 1, 8),
    _QmCurPps_Type()
)
qmCurPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmCurPps.setStatus("current")
_QmPackets_Type = Counter32
_QmPackets_Object = MibTableColumn
qmPackets = _QmPackets_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 4, 1, 1, 9),
    _QmPackets_Type()
)
qmPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmPackets.setStatus("current")
_QmPacketsDropped_Type = Counter32
_QmPacketsDropped_Object = MibTableColumn
qmPacketsDropped = _QmPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 4, 1, 1, 10),
    _QmPacketsDropped_Type()
)
qmPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmPacketsDropped.setStatus("current")
_QmBytes_Type = Counter32
_QmBytes_Object = MibTableColumn
qmBytes = _QmBytes_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 4, 1, 1, 11),
    _QmBytes_Type()
)
qmBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmBytes.setStatus("current")
_QmBytesDropped_Type = Counter32
_QmBytesDropped_Object = MibTableColumn
qmBytesDropped = _QmBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 4, 1, 1, 12),
    _QmBytesDropped_Type()
)
qmBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmBytesDropped.setStatus("current")
_QmHTB_ObjectIdentity = ObjectIdentity
qmHTB = _QmHTB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 4, 2)
)
_QmHtbCurrentQL_Type = Gauge32
_QmHtbCurrentQL_Object = MibScalar
qmHtbCurrentQL = _QmHtbCurrentQL_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 4, 2, 1),
    _QmHtbCurrentQL_Type()
)
qmHtbCurrentQL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmHtbCurrentQL.setStatus("current")
_QmHtbMaxQL_Type = Gauge32
_QmHtbMaxQL_Object = MibScalar
qmHtbMaxQL = _QmHtbMaxQL_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 4, 2, 2),
    _QmHtbMaxQL_Type()
)
qmHtbMaxQL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmHtbMaxQL.setStatus("current")
_QmHtbSystemDrop_Type = Gauge32
_QmHtbSystemDrop_Object = MibScalar
qmHtbSystemDrop = _QmHtbSystemDrop_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 4, 2, 3),
    _QmHtbSystemDrop_Type()
)
qmHtbSystemDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmHtbSystemDrop.setStatus("current")
_AquaqmMIBConformance_ObjectIdentity = ObjectIdentity
aquaqmMIBConformance = _AquaqmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 4, 3)
)
_AquaqmMIBCompliances_ObjectIdentity = ObjectIdentity
aquaqmMIBCompliances = _AquaqmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 4, 3, 1)
)
_AquaqmMIBGroups_ObjectIdentity = ObjectIdentity
aquaqmMIBGroups = _AquaqmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 4, 3, 2)
)

# Managed Objects groups

qmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 4, 3, 2, 1)
)
qmGroup.setObjects(
      *(("AQUAQM-MIB", "qmChannel"),
        ("AQUAQM-MIB", "qmPriority"),
        ("AQUAQM-MIB", "qmClass"),
        ("AQUAQM-MIB", "qmTo"),
        ("AQUAQM-MIB", "qmMax"),
        ("AQUAQM-MIB", "qmMaxPps"),
        ("AQUAQM-MIB", "qmCur"),
        ("AQUAQM-MIB", "qmCurPps"),
        ("AQUAQM-MIB", "qmPackets"),
        ("AQUAQM-MIB", "qmPacketsDropped"),
        ("AQUAQM-MIB", "qmBytes"),
        ("AQUAQM-MIB", "qmBytesDropped"),
        ("AQUAQM-MIB", "qmHtbCurrentQL"),
        ("AQUAQM-MIB", "qmHtbMaxQL"),
        ("AQUAQM-MIB", "qmHtbSystemDrop"))
)
if mibBuilder.loadTexts:
    qmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aquaqmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 4, 3, 1, 1)
)
aquaqmMIBCompliance.setObjects(
    ("AQUAQM-MIB", "qmGroup")
)
if mibBuilder.loadTexts:
    aquaqmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AQUAQM-MIB",
    **{"aquaqmMIB": aquaqmMIB,
       "qmTable": qmTable,
       "qmEntry": qmEntry,
       "qmChannel": qmChannel,
       "qmPriority": qmPriority,
       "qmClass": qmClass,
       "qmTo": qmTo,
       "qmMax": qmMax,
       "qmMaxPps": qmMaxPps,
       "qmCur": qmCur,
       "qmCurPps": qmCurPps,
       "qmPackets": qmPackets,
       "qmPacketsDropped": qmPacketsDropped,
       "qmBytes": qmBytes,
       "qmBytesDropped": qmBytesDropped,
       "qmHTB": qmHTB,
       "qmHtbCurrentQL": qmHtbCurrentQL,
       "qmHtbMaxQL": qmHtbMaxQL,
       "qmHtbSystemDrop": qmHtbSystemDrop,
       "aquaqmMIBConformance": aquaqmMIBConformance,
       "aquaqmMIBCompliances": aquaqmMIBCompliances,
       "aquaqmMIBCompliance": aquaqmMIBCompliance,
       "aquaqmMIBGroups": aquaqmMIBGroups,
       "qmGroup": qmGroup}
)
