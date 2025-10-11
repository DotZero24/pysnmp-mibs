# SNMP MIB module (ENTERASYS-TRACKED-OBJECTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-TRACKED-OBJECTS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:47:57 2025
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

etsysTrackedObjectsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79)
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsMIB.setRevisions(
        ("2013-02-07 15:59",
         "2012-02-08 14:29",
         "2011-05-18 15:06")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysTrackedObjects_ObjectIdentity = ObjectIdentity
etsysTrackedObjects = _EtsysTrackedObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1)
)
_EtsysTrackedObjectsGlobals_ObjectIdentity = ObjectIdentity
etsysTrackedObjectsGlobals = _EtsysTrackedObjectsGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 1)
)
_EtsysTrackedObjectsMaxObjects_Type = Unsigned32
_EtsysTrackedObjectsMaxObjects_Object = MibScalar
etsysTrackedObjectsMaxObjects = _EtsysTrackedObjectsMaxObjects_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 1, 1),
    _EtsysTrackedObjectsMaxObjects_Type()
)
etsysTrackedObjectsMaxObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedObjectsMaxObjects.setStatus("current")
_EtsysTrackedObjectsObjectsUsed_Type = Gauge32
_EtsysTrackedObjectsObjectsUsed_Object = MibScalar
etsysTrackedObjectsObjectsUsed = _EtsysTrackedObjectsObjectsUsed_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 1, 2),
    _EtsysTrackedObjectsObjectsUsed_Type()
)
etsysTrackedObjectsObjectsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedObjectsObjectsUsed.setStatus("current")
_EtsysTrackedObjectsMaxProbes_Type = Unsigned32
_EtsysTrackedObjectsMaxProbes_Object = MibScalar
etsysTrackedObjectsMaxProbes = _EtsysTrackedObjectsMaxProbes_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 1, 3),
    _EtsysTrackedObjectsMaxProbes_Type()
)
etsysTrackedObjectsMaxProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedObjectsMaxProbes.setStatus("current")
_EtsysTrackedObjectsProbesUsed_Type = Gauge32
_EtsysTrackedObjectsProbesUsed_Object = MibScalar
etsysTrackedObjectsProbesUsed = _EtsysTrackedObjectsProbesUsed_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 1, 4),
    _EtsysTrackedObjectsProbesUsed_Type()
)
etsysTrackedObjectsProbesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbesUsed.setStatus("current")
_EtsysTrackedObjectsMaxAcvProbes_Type = Unsigned32
_EtsysTrackedObjectsMaxAcvProbes_Object = MibScalar
etsysTrackedObjectsMaxAcvProbes = _EtsysTrackedObjectsMaxAcvProbes_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 1, 5),
    _EtsysTrackedObjectsMaxAcvProbes_Type()
)
etsysTrackedObjectsMaxAcvProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedObjectsMaxAcvProbes.setStatus("current")
_EtsysTrackedObjectsAcvProbesUsed_Type = Gauge32
_EtsysTrackedObjectsAcvProbesUsed_Object = MibScalar
etsysTrackedObjectsAcvProbesUsed = _EtsysTrackedObjectsAcvProbesUsed_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 1, 6),
    _EtsysTrackedObjectsAcvProbesUsed_Type()
)
etsysTrackedObjectsAcvProbesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedObjectsAcvProbesUsed.setStatus("current")
_EtsysTrackedObjectsMaxSessions_Type = Unsigned32
_EtsysTrackedObjectsMaxSessions_Object = MibScalar
etsysTrackedObjectsMaxSessions = _EtsysTrackedObjectsMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 1, 7),
    _EtsysTrackedObjectsMaxSessions_Type()
)
etsysTrackedObjectsMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedObjectsMaxSessions.setStatus("current")
_EtsysTrackedObjectsSessionsUsed_Type = Gauge32
_EtsysTrackedObjectsSessionsUsed_Object = MibScalar
etsysTrackedObjectsSessionsUsed = _EtsysTrackedObjectsSessionsUsed_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 1, 8),
    _EtsysTrackedObjectsSessionsUsed_Type()
)
etsysTrackedObjectsSessionsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedObjectsSessionsUsed.setStatus("current")
_EtsysTrackedObjectsMaxIntfAssoc_Type = Unsigned32
_EtsysTrackedObjectsMaxIntfAssoc_Object = MibScalar
etsysTrackedObjectsMaxIntfAssoc = _EtsysTrackedObjectsMaxIntfAssoc_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 1, 9),
    _EtsysTrackedObjectsMaxIntfAssoc_Type()
)
etsysTrackedObjectsMaxIntfAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedObjectsMaxIntfAssoc.setStatus("current")
_EtsysTrackedObjectsIntfAssocUsed_Type = Gauge32
_EtsysTrackedObjectsIntfAssocUsed_Object = MibScalar
etsysTrackedObjectsIntfAssocUsed = _EtsysTrackedObjectsIntfAssocUsed_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 1, 10),
    _EtsysTrackedObjectsIntfAssocUsed_Type()
)
etsysTrackedObjectsIntfAssocUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedObjectsIntfAssocUsed.setStatus("current")
_EtsysTrackedObjectsTables_ObjectIdentity = ObjectIdentity
etsysTrackedObjectsTables = _EtsysTrackedObjectsTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2)
)
_EtsysTrackedObjectsProbeTable_Object = MibTable
etsysTrackedObjectsProbeTable = _EtsysTrackedObjectsProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeTable.setStatus("current")
_EtsysTrackedObjectsProbeEntry_Object = MibTableRow
etsysTrackedObjectsProbeEntry = _EtsysTrackedObjectsProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 1, 1)
)
etsysTrackedObjectsProbeEntry.setIndexNames(
    (1, "ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsProbeName"),
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeEntry.setStatus("current")


class _EtsysTrackedObjectsProbeName_Type(SnmpAdminString):
    """Custom type etsysTrackedObjectsProbeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_EtsysTrackedObjectsProbeName_Type.__name__ = "SnmpAdminString"
_EtsysTrackedObjectsProbeName_Object = MibTableColumn
etsysTrackedObjectsProbeName = _EtsysTrackedObjectsProbeName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 1, 1, 1),
    _EtsysTrackedObjectsProbeName_Type()
)
etsysTrackedObjectsProbeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeName.setStatus("current")
_EtsysTrackedObjectsProbeIndex_Type = Unsigned32
_EtsysTrackedObjectsProbeIndex_Object = MibTableColumn
etsysTrackedObjectsProbeIndex = _EtsysTrackedObjectsProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 1, 1, 2),
    _EtsysTrackedObjectsProbeIndex_Type()
)
etsysTrackedObjectsProbeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeIndex.setStatus("current")
_EtsysTrackedObjectsProbeDefault_Type = TruthValue
_EtsysTrackedObjectsProbeDefault_Object = MibTableColumn
etsysTrackedObjectsProbeDefault = _EtsysTrackedObjectsProbeDefault_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 1, 1, 3),
    _EtsysTrackedObjectsProbeDefault_Type()
)
etsysTrackedObjectsProbeDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeDefault.setStatus("current")


class _EtsysTrackedObjectsProbeType_Type(Integer32):
    """Custom type etsysTrackedObjectsProbeType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("udp", 2),
          ("tcp", 3),
          ("icmpTs", 4))
    )


_EtsysTrackedObjectsProbeType_Type.__name__ = "Integer32"
_EtsysTrackedObjectsProbeType_Object = MibTableColumn
etsysTrackedObjectsProbeType = _EtsysTrackedObjectsProbeType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 1, 1, 4),
    _EtsysTrackedObjectsProbeType_Type()
)
etsysTrackedObjectsProbeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeType.setStatus("current")


class _EtsysTrackedObjectsProbeAcvClose_Type(SnmpAdminString):
    """Custom type etsysTrackedObjectsProbeAcvClose based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_EtsysTrackedObjectsProbeAcvClose_Type.__name__ = "SnmpAdminString"
_EtsysTrackedObjectsProbeAcvClose_Object = MibTableColumn
etsysTrackedObjectsProbeAcvClose = _EtsysTrackedObjectsProbeAcvClose_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 1, 1, 5),
    _EtsysTrackedObjectsProbeAcvClose_Type()
)
etsysTrackedObjectsProbeAcvClose.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeAcvClose.setStatus("current")


class _EtsysTrackedObjectsProbeAcvReply_Type(SnmpAdminString):
    """Custom type etsysTrackedObjectsProbeAcvReply based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_EtsysTrackedObjectsProbeAcvReply_Type.__name__ = "SnmpAdminString"
_EtsysTrackedObjectsProbeAcvReply_Object = MibTableColumn
etsysTrackedObjectsProbeAcvReply = _EtsysTrackedObjectsProbeAcvReply_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 1, 1, 6),
    _EtsysTrackedObjectsProbeAcvReply_Type()
)
etsysTrackedObjectsProbeAcvReply.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeAcvReply.setStatus("current")


class _EtsysTrackedObjectsProbeAcvRequest_Type(SnmpAdminString):
    """Custom type etsysTrackedObjectsProbeAcvRequest based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_EtsysTrackedObjectsProbeAcvRequest_Type.__name__ = "SnmpAdminString"
_EtsysTrackedObjectsProbeAcvRequest_Object = MibTableColumn
etsysTrackedObjectsProbeAcvRequest = _EtsysTrackedObjectsProbeAcvRequest_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 1, 1, 7),
    _EtsysTrackedObjectsProbeAcvRequest_Type()
)
etsysTrackedObjectsProbeAcvRequest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeAcvRequest.setStatus("current")


class _EtsysTrackedObjectsProbeAcvDepth_Type(Unsigned32):
    """Custom type etsysTrackedObjectsProbeAcvDepth based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EtsysTrackedObjectsProbeAcvDepth_Type.__name__ = "Unsigned32"
_EtsysTrackedObjectsProbeAcvDepth_Object = MibTableColumn
etsysTrackedObjectsProbeAcvDepth = _EtsysTrackedObjectsProbeAcvDepth_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 1, 1, 8),
    _EtsysTrackedObjectsProbeAcvDepth_Type()
)
etsysTrackedObjectsProbeAcvDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeAcvDepth.setStatus("current")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeAcvDepth.setUnits("characters")


class _EtsysTrackedObjectsProbeFdCount_Type(Unsigned32):
    """Custom type etsysTrackedObjectsProbeFdCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysTrackedObjectsProbeFdCount_Type.__name__ = "Unsigned32"
_EtsysTrackedObjectsProbeFdCount_Object = MibTableColumn
etsysTrackedObjectsProbeFdCount = _EtsysTrackedObjectsProbeFdCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 1, 1, 9),
    _EtsysTrackedObjectsProbeFdCount_Type()
)
etsysTrackedObjectsProbeFdCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeFdCount.setStatus("current")


class _EtsysTrackedObjectsProbeFdInterval_Type(Unsigned32):
    """Custom type etsysTrackedObjectsProbeFdInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 300),
    )


_EtsysTrackedObjectsProbeFdInterval_Type.__name__ = "Unsigned32"
_EtsysTrackedObjectsProbeFdInterval_Object = MibTableColumn
etsysTrackedObjectsProbeFdInterval = _EtsysTrackedObjectsProbeFdInterval_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 1, 1, 10),
    _EtsysTrackedObjectsProbeFdInterval_Type()
)
etsysTrackedObjectsProbeFdInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeFdInterval.setStatus("current")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeFdInterval.setUnits("seconds")


class _EtsysTrackedObjectsProbePdCount_Type(Unsigned32):
    """Custom type etsysTrackedObjectsProbePdCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysTrackedObjectsProbePdCount_Type.__name__ = "Unsigned32"
_EtsysTrackedObjectsProbePdCount_Object = MibTableColumn
etsysTrackedObjectsProbePdCount = _EtsysTrackedObjectsProbePdCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 1, 1, 11),
    _EtsysTrackedObjectsProbePdCount_Type()
)
etsysTrackedObjectsProbePdCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbePdCount.setStatus("current")


class _EtsysTrackedObjectsProbePdInterval_Type(Unsigned32):
    """Custom type etsysTrackedObjectsProbePdInterval based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 300),
    )


_EtsysTrackedObjectsProbePdInterval_Type.__name__ = "Unsigned32"
_EtsysTrackedObjectsProbePdInterval_Object = MibTableColumn
etsysTrackedObjectsProbePdInterval = _EtsysTrackedObjectsProbePdInterval_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 1, 1, 12),
    _EtsysTrackedObjectsProbePdInterval_Type()
)
etsysTrackedObjectsProbePdInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbePdInterval.setStatus("current")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbePdInterval.setUnits("seconds")


class _EtsysTrackedObjectsProbeOpen_Type(Unsigned32):
    """Custom type etsysTrackedObjectsProbeOpen based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_EtsysTrackedObjectsProbeOpen_Type.__name__ = "Unsigned32"
_EtsysTrackedObjectsProbeOpen_Object = MibTableColumn
etsysTrackedObjectsProbeOpen = _EtsysTrackedObjectsProbeOpen_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 1, 1, 13),
    _EtsysTrackedObjectsProbeOpen_Type()
)
etsysTrackedObjectsProbeOpen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeOpen.setStatus("current")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeOpen.setUnits("seconds")


class _EtsysTrackedObjectsProbeReceive_Type(Unsigned32):
    """Custom type etsysTrackedObjectsProbeReceive based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysTrackedObjectsProbeReceive_Type.__name__ = "Unsigned32"
_EtsysTrackedObjectsProbeReceive_Object = MibTableColumn
etsysTrackedObjectsProbeReceive = _EtsysTrackedObjectsProbeReceive_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 1, 1, 14),
    _EtsysTrackedObjectsProbeReceive_Type()
)
etsysTrackedObjectsProbeReceive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeReceive.setStatus("current")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeReceive.setUnits("seconds")


class _EtsysTrackedObjectsProbeInservice_Type(TruthValue):
    """Custom type etsysTrackedObjectsProbeInservice based on TruthValue"""
    defaultValue = 2


_EtsysTrackedObjectsProbeInservice_Type.__name__ = "TruthValue"
_EtsysTrackedObjectsProbeInservice_Object = MibTableColumn
etsysTrackedObjectsProbeInservice = _EtsysTrackedObjectsProbeInservice_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 1, 1, 15),
    _EtsysTrackedObjectsProbeInservice_Type()
)
etsysTrackedObjectsProbeInservice.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeInservice.setStatus("current")


class _EtsysTrackedObjectsProbeDescription_Type(SnmpAdminString):
    """Custom type etsysTrackedObjectsProbeDescription based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_EtsysTrackedObjectsProbeDescription_Type.__name__ = "SnmpAdminString"
_EtsysTrackedObjectsProbeDescription_Object = MibTableColumn
etsysTrackedObjectsProbeDescription = _EtsysTrackedObjectsProbeDescription_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 1, 1, 16),
    _EtsysTrackedObjectsProbeDescription_Type()
)
etsysTrackedObjectsProbeDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeDescription.setStatus("current")
_EtsysTrackedObjectsProbeStatus_Type = RowStatus
_EtsysTrackedObjectsProbeStatus_Object = MibTableColumn
etsysTrackedObjectsProbeStatus = _EtsysTrackedObjectsProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 1, 1, 17),
    _EtsysTrackedObjectsProbeStatus_Type()
)
etsysTrackedObjectsProbeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeStatus.setStatus("current")
_EtsysTrackedObjectsSessionTable_Object = MibTable
etsysTrackedObjectsSessionTable = _EtsysTrackedObjectsSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 2)
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsSessionTable.setStatus("current")
_EtsysTrackedObjectsSessionEntry_Object = MibTableRow
etsysTrackedObjectsSessionEntry = _EtsysTrackedObjectsSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 2, 1)
)
etsysTrackedObjectsSessionEntry.setIndexNames(
    (0, "ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsProbeIndex"),
    (0, "ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsSessionType"),
    (0, "ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsSessionAddr"),
    (0, "ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsSessionPort"),
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsSessionEntry.setStatus("current")
_EtsysTrackedObjectsSessionType_Type = InetAddressType
_EtsysTrackedObjectsSessionType_Object = MibTableColumn
etsysTrackedObjectsSessionType = _EtsysTrackedObjectsSessionType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 2, 1, 1),
    _EtsysTrackedObjectsSessionType_Type()
)
etsysTrackedObjectsSessionType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysTrackedObjectsSessionType.setStatus("current")
_EtsysTrackedObjectsSessionAddr_Type = InetAddress
_EtsysTrackedObjectsSessionAddr_Object = MibTableColumn
etsysTrackedObjectsSessionAddr = _EtsysTrackedObjectsSessionAddr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 2, 1, 2),
    _EtsysTrackedObjectsSessionAddr_Type()
)
etsysTrackedObjectsSessionAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysTrackedObjectsSessionAddr.setStatus("current")
_EtsysTrackedObjectsSessionPort_Type = InetPortNumber
_EtsysTrackedObjectsSessionPort_Object = MibTableColumn
etsysTrackedObjectsSessionPort = _EtsysTrackedObjectsSessionPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 2, 1, 3),
    _EtsysTrackedObjectsSessionPort_Type()
)
etsysTrackedObjectsSessionPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysTrackedObjectsSessionPort.setStatus("current")


class _EtsysTrackedObjectsSessionState_Type(Integer32):
    """Custom type etsysTrackedObjectsSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("pending", 3),
          ("disabled", 4),
          ("collect", 5))
    )


_EtsysTrackedObjectsSessionState_Type.__name__ = "Integer32"
_EtsysTrackedObjectsSessionState_Object = MibTableColumn
etsysTrackedObjectsSessionState = _EtsysTrackedObjectsSessionState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 2, 1, 4),
    _EtsysTrackedObjectsSessionState_Type()
)
etsysTrackedObjectsSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedObjectsSessionState.setStatus("current")
_EtsysTrackedObjectsSessionStateChanges_Type = Counter32
_EtsysTrackedObjectsSessionStateChanges_Object = MibTableColumn
etsysTrackedObjectsSessionStateChanges = _EtsysTrackedObjectsSessionStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 2, 1, 5),
    _EtsysTrackedObjectsSessionStateChanges_Type()
)
etsysTrackedObjectsSessionStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedObjectsSessionStateChanges.setStatus("current")
_EtsysTrackedObjectsSessionLastChange_Type = TimeTicks
_EtsysTrackedObjectsSessionLastChange_Object = MibTableColumn
etsysTrackedObjectsSessionLastChange = _EtsysTrackedObjectsSessionLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 2, 1, 6),
    _EtsysTrackedObjectsSessionLastChange_Type()
)
etsysTrackedObjectsSessionLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedObjectsSessionLastChange.setStatus("current")
_EtsysTrackedObjectsCommonTable_Object = MibTable
etsysTrackedObjectsCommonTable = _EtsysTrackedObjectsCommonTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 3)
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsCommonTable.setStatus("current")
_EtsysTrackedObjectsCommonEntry_Object = MibTableRow
etsysTrackedObjectsCommonEntry = _EtsysTrackedObjectsCommonEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 3, 1)
)
etsysTrackedObjectsCommonEntry.setIndexNames(
    (1, "ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsCommonName"),
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsCommonEntry.setStatus("current")


class _EtsysTrackedObjectsCommonName_Type(SnmpAdminString):
    """Custom type etsysTrackedObjectsCommonName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_EtsysTrackedObjectsCommonName_Type.__name__ = "SnmpAdminString"
_EtsysTrackedObjectsCommonName_Object = MibTableColumn
etsysTrackedObjectsCommonName = _EtsysTrackedObjectsCommonName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 3, 1, 1),
    _EtsysTrackedObjectsCommonName_Type()
)
etsysTrackedObjectsCommonName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysTrackedObjectsCommonName.setStatus("current")


class _EtsysTrackedObjectsCommonType_Type(Integer32):
    """Custom type etsysTrackedObjectsCommonType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("ipRoute", 2),
          ("portGroup", 3),
          ("portIfspeed", 4))
    )


_EtsysTrackedObjectsCommonType_Type.__name__ = "Integer32"
_EtsysTrackedObjectsCommonType_Object = MibTableColumn
etsysTrackedObjectsCommonType = _EtsysTrackedObjectsCommonType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 3, 1, 2),
    _EtsysTrackedObjectsCommonType_Type()
)
etsysTrackedObjectsCommonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedObjectsCommonType.setStatus("current")


class _EtsysTrackedObjectsCommonState_Type(Integer32):
    """Custom type etsysTrackedObjectsCommonState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("disabled", 4))
    )


_EtsysTrackedObjectsCommonState_Type.__name__ = "Integer32"
_EtsysTrackedObjectsCommonState_Object = MibTableColumn
etsysTrackedObjectsCommonState = _EtsysTrackedObjectsCommonState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 3, 1, 3),
    _EtsysTrackedObjectsCommonState_Type()
)
etsysTrackedObjectsCommonState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedObjectsCommonState.setStatus("current")


class _EtsysTrackedObjectsCommonDelayUp_Type(Unsigned32):
    """Custom type etsysTrackedObjectsCommonDelayUp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_EtsysTrackedObjectsCommonDelayUp_Type.__name__ = "Unsigned32"
_EtsysTrackedObjectsCommonDelayUp_Object = MibTableColumn
etsysTrackedObjectsCommonDelayUp = _EtsysTrackedObjectsCommonDelayUp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 3, 1, 4),
    _EtsysTrackedObjectsCommonDelayUp_Type()
)
etsysTrackedObjectsCommonDelayUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTrackedObjectsCommonDelayUp.setStatus("current")
if mibBuilder.loadTexts:
    etsysTrackedObjectsCommonDelayUp.setUnits("seconds")


class _EtsysTrackedObjectsCommonDelayDown_Type(Unsigned32):
    """Custom type etsysTrackedObjectsCommonDelayDown based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_EtsysTrackedObjectsCommonDelayDown_Type.__name__ = "Unsigned32"
_EtsysTrackedObjectsCommonDelayDown_Object = MibTableColumn
etsysTrackedObjectsCommonDelayDown = _EtsysTrackedObjectsCommonDelayDown_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 3, 1, 5),
    _EtsysTrackedObjectsCommonDelayDown_Type()
)
etsysTrackedObjectsCommonDelayDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTrackedObjectsCommonDelayDown.setStatus("current")
if mibBuilder.loadTexts:
    etsysTrackedObjectsCommonDelayDown.setUnits("seconds")


class _EtsysTrackedObjectsCommonDescription_Type(SnmpAdminString):
    """Custom type etsysTrackedObjectsCommonDescription based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_EtsysTrackedObjectsCommonDescription_Type.__name__ = "SnmpAdminString"
_EtsysTrackedObjectsCommonDescription_Object = MibTableColumn
etsysTrackedObjectsCommonDescription = _EtsysTrackedObjectsCommonDescription_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 3, 1, 6),
    _EtsysTrackedObjectsCommonDescription_Type()
)
etsysTrackedObjectsCommonDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTrackedObjectsCommonDescription.setStatus("current")
_EtsysTrackedObjectsCommonInservice_Type = TruthValue
_EtsysTrackedObjectsCommonInservice_Object = MibTableColumn
etsysTrackedObjectsCommonInservice = _EtsysTrackedObjectsCommonInservice_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 3, 1, 7),
    _EtsysTrackedObjectsCommonInservice_Type()
)
etsysTrackedObjectsCommonInservice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTrackedObjectsCommonInservice.setStatus("current")
_EtsysTrackedObjectsCommonActionUp_Type = SnmpAdminString
_EtsysTrackedObjectsCommonActionUp_Object = MibTableColumn
etsysTrackedObjectsCommonActionUp = _EtsysTrackedObjectsCommonActionUp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 3, 1, 8),
    _EtsysTrackedObjectsCommonActionUp_Type()
)
etsysTrackedObjectsCommonActionUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTrackedObjectsCommonActionUp.setStatus("current")
_EtsysTrackedObjectsCommonActionDown_Type = SnmpAdminString
_EtsysTrackedObjectsCommonActionDown_Object = MibTableColumn
etsysTrackedObjectsCommonActionDown = _EtsysTrackedObjectsCommonActionDown_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 3, 1, 9),
    _EtsysTrackedObjectsCommonActionDown_Type()
)
etsysTrackedObjectsCommonActionDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTrackedObjectsCommonActionDown.setStatus("current")
_EtsysTrackedObjectsIntfTable_Object = MibTable
etsysTrackedObjectsIntfTable = _EtsysTrackedObjectsIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 4)
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsIntfTable.setStatus("current")
_EtsysTrackedObjectsIntfEntry_Object = MibTableRow
etsysTrackedObjectsIntfEntry = _EtsysTrackedObjectsIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 4, 1)
)
etsysTrackedObjectsIntfEntry.setIndexNames(
    (1, "ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsCommonName"),
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsIntfEntry.setStatus("current")
_EtsysTrackedObjectsIntfIndex_Type = InterfaceIndex
_EtsysTrackedObjectsIntfIndex_Object = MibTableColumn
etsysTrackedObjectsIntfIndex = _EtsysTrackedObjectsIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 4, 1, 1),
    _EtsysTrackedObjectsIntfIndex_Type()
)
etsysTrackedObjectsIntfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTrackedObjectsIntfIndex.setStatus("current")


class _EtsysTrackedObjectsIntfOption_Type(Integer32):
    """Custom type etsysTrackedObjectsIntfOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("lineProtocol", 1)
    )


_EtsysTrackedObjectsIntfOption_Type.__name__ = "Integer32"
_EtsysTrackedObjectsIntfOption_Object = MibTableColumn
etsysTrackedObjectsIntfOption = _EtsysTrackedObjectsIntfOption_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 4, 1, 2),
    _EtsysTrackedObjectsIntfOption_Type()
)
etsysTrackedObjectsIntfOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTrackedObjectsIntfOption.setStatus("current")
_EtsysTrackedObjectsIntfStatus_Type = RowStatus
_EtsysTrackedObjectsIntfStatus_Object = MibTableColumn
etsysTrackedObjectsIntfStatus = _EtsysTrackedObjectsIntfStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 4, 1, 3),
    _EtsysTrackedObjectsIntfStatus_Type()
)
etsysTrackedObjectsIntfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTrackedObjectsIntfStatus.setStatus("current")
_EtsysTrackedObjectsRouteTable_Object = MibTable
etsysTrackedObjectsRouteTable = _EtsysTrackedObjectsRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 5)
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsRouteTable.setStatus("current")
_EtsysTrackedObjectsRouteEntry_Object = MibTableRow
etsysTrackedObjectsRouteEntry = _EtsysTrackedObjectsRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 5, 1)
)
etsysTrackedObjectsRouteEntry.setIndexNames(
    (1, "ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsCommonName"),
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsRouteEntry.setStatus("current")


class _EtsysTrackedObjectsRouteType_Type(InetAddressType):
    """Custom type etsysTrackedObjectsRouteType based on InetAddressType"""
    defaultValue = 1


_EtsysTrackedObjectsRouteType_Type.__name__ = "InetAddressType"
_EtsysTrackedObjectsRouteType_Object = MibTableColumn
etsysTrackedObjectsRouteType = _EtsysTrackedObjectsRouteType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 5, 1, 1),
    _EtsysTrackedObjectsRouteType_Type()
)
etsysTrackedObjectsRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTrackedObjectsRouteType.setStatus("current")
_EtsysTrackedObjectsRoutePrefix_Type = InetAddressPrefixLength
_EtsysTrackedObjectsRoutePrefix_Object = MibTableColumn
etsysTrackedObjectsRoutePrefix = _EtsysTrackedObjectsRoutePrefix_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 5, 1, 2),
    _EtsysTrackedObjectsRoutePrefix_Type()
)
etsysTrackedObjectsRoutePrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTrackedObjectsRoutePrefix.setStatus("current")
_EtsysTrackedObjectsRoute_Type = InetAddress
_EtsysTrackedObjectsRoute_Object = MibTableColumn
etsysTrackedObjectsRoute = _EtsysTrackedObjectsRoute_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 5, 1, 3),
    _EtsysTrackedObjectsRoute_Type()
)
etsysTrackedObjectsRoute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTrackedObjectsRoute.setStatus("current")


class _EtsysTrackedObjectsRouteOption_Type(Integer32):
    """Custom type etsysTrackedObjectsRouteOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reachability", 1),
          ("metric", 2))
    )


_EtsysTrackedObjectsRouteOption_Type.__name__ = "Integer32"
_EtsysTrackedObjectsRouteOption_Object = MibTableColumn
etsysTrackedObjectsRouteOption = _EtsysTrackedObjectsRouteOption_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 5, 1, 4),
    _EtsysTrackedObjectsRouteOption_Type()
)
etsysTrackedObjectsRouteOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTrackedObjectsRouteOption.setStatus("current")


class _EtsysTrackedObjectsRouteMetricUpThresh_Type(Unsigned32):
    """Custom type etsysTrackedObjectsRouteMetricUpThresh based on Unsigned32"""
    defaultValue = 254

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_EtsysTrackedObjectsRouteMetricUpThresh_Type.__name__ = "Unsigned32"
_EtsysTrackedObjectsRouteMetricUpThresh_Object = MibTableColumn
etsysTrackedObjectsRouteMetricUpThresh = _EtsysTrackedObjectsRouteMetricUpThresh_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 5, 1, 5),
    _EtsysTrackedObjectsRouteMetricUpThresh_Type()
)
etsysTrackedObjectsRouteMetricUpThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTrackedObjectsRouteMetricUpThresh.setStatus("current")


class _EtsysTrackedObjectsRouteMetricDownThresh_Type(Unsigned32):
    """Custom type etsysTrackedObjectsRouteMetricDownThresh based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EtsysTrackedObjectsRouteMetricDownThresh_Type.__name__ = "Unsigned32"
_EtsysTrackedObjectsRouteMetricDownThresh_Object = MibTableColumn
etsysTrackedObjectsRouteMetricDownThresh = _EtsysTrackedObjectsRouteMetricDownThresh_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 5, 1, 6),
    _EtsysTrackedObjectsRouteMetricDownThresh_Type()
)
etsysTrackedObjectsRouteMetricDownThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTrackedObjectsRouteMetricDownThresh.setStatus("current")
_EtsysTrackedObjectsRouteStatus_Type = RowStatus
_EtsysTrackedObjectsRouteStatus_Object = MibTableColumn
etsysTrackedObjectsRouteStatus = _EtsysTrackedObjectsRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 5, 1, 7),
    _EtsysTrackedObjectsRouteStatus_Type()
)
etsysTrackedObjectsRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTrackedObjectsRouteStatus.setStatus("current")
_EtsysTrackedObjectsPortGroupTable_Object = MibTable
etsysTrackedObjectsPortGroupTable = _EtsysTrackedObjectsPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 6)
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsPortGroupTable.setStatus("current")
_EtsysTrackedObjectsPortGroupEntry_Object = MibTableRow
etsysTrackedObjectsPortGroupEntry = _EtsysTrackedObjectsPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 6, 1)
)
etsysTrackedObjectsPortGroupEntry.setIndexNames(
    (1, "ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsCommonName"),
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsPortGroupEntry.setStatus("current")
_EtsysTrackedObjectsPortGroupMemberMax_Type = Unsigned32
_EtsysTrackedObjectsPortGroupMemberMax_Object = MibTableColumn
etsysTrackedObjectsPortGroupMemberMax = _EtsysTrackedObjectsPortGroupMemberMax_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 6, 1, 1),
    _EtsysTrackedObjectsPortGroupMemberMax_Type()
)
etsysTrackedObjectsPortGroupMemberMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedObjectsPortGroupMemberMax.setStatus("current")
_EtsysTrackedObjectsPortGroupMemberCount_Type = Gauge32
_EtsysTrackedObjectsPortGroupMemberCount_Object = MibTableColumn
etsysTrackedObjectsPortGroupMemberCount = _EtsysTrackedObjectsPortGroupMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 6, 1, 2),
    _EtsysTrackedObjectsPortGroupMemberCount_Type()
)
etsysTrackedObjectsPortGroupMemberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedObjectsPortGroupMemberCount.setStatus("current")
_EtsysTrackedObjectsPortGroupStatus_Type = RowStatus
_EtsysTrackedObjectsPortGroupStatus_Object = MibTableColumn
etsysTrackedObjectsPortGroupStatus = _EtsysTrackedObjectsPortGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 6, 1, 3),
    _EtsysTrackedObjectsPortGroupStatus_Type()
)
etsysTrackedObjectsPortGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTrackedObjectsPortGroupStatus.setStatus("current")
_EtsysTrackedObjectsPortGroupUpCount_Type = Gauge32
_EtsysTrackedObjectsPortGroupUpCount_Object = MibTableColumn
etsysTrackedObjectsPortGroupUpCount = _EtsysTrackedObjectsPortGroupUpCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 6, 1, 4),
    _EtsysTrackedObjectsPortGroupUpCount_Type()
)
etsysTrackedObjectsPortGroupUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedObjectsPortGroupUpCount.setStatus("current")
_EtsysTrackedObjectsPortGroupDownCount_Type = Gauge32
_EtsysTrackedObjectsPortGroupDownCount_Object = MibTableColumn
etsysTrackedObjectsPortGroupDownCount = _EtsysTrackedObjectsPortGroupDownCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 6, 1, 5),
    _EtsysTrackedObjectsPortGroupDownCount_Type()
)
etsysTrackedObjectsPortGroupDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedObjectsPortGroupDownCount.setStatus("current")


class _EtsysTrackedObjectsPortGroupUpThresh_Type(Unsigned32):
    """Custom type etsysTrackedObjectsPortGroupUpThresh based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EtsysTrackedObjectsPortGroupUpThresh_Type.__name__ = "Unsigned32"
_EtsysTrackedObjectsPortGroupUpThresh_Object = MibTableColumn
etsysTrackedObjectsPortGroupUpThresh = _EtsysTrackedObjectsPortGroupUpThresh_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 6, 1, 6),
    _EtsysTrackedObjectsPortGroupUpThresh_Type()
)
etsysTrackedObjectsPortGroupUpThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTrackedObjectsPortGroupUpThresh.setStatus("current")


class _EtsysTrackedObjectsPortGroupDownThresh_Type(Unsigned32):
    """Custom type etsysTrackedObjectsPortGroupDownThresh based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_EtsysTrackedObjectsPortGroupDownThresh_Type.__name__ = "Unsigned32"
_EtsysTrackedObjectsPortGroupDownThresh_Object = MibTableColumn
etsysTrackedObjectsPortGroupDownThresh = _EtsysTrackedObjectsPortGroupDownThresh_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 6, 1, 7),
    _EtsysTrackedObjectsPortGroupDownThresh_Type()
)
etsysTrackedObjectsPortGroupDownThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTrackedObjectsPortGroupDownThresh.setStatus("current")
_EtsysTrackedObjectsPortTable_Object = MibTable
etsysTrackedObjectsPortTable = _EtsysTrackedObjectsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 7)
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsPortTable.setStatus("current")
_EtsysTrackedObjectsPortEntry_Object = MibTableRow
etsysTrackedObjectsPortEntry = _EtsysTrackedObjectsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 7, 1)
)
etsysTrackedObjectsPortEntry.setIndexNames(
    (0, "ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsPortIfIndex"),
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsPortEntry.setStatus("current")
_EtsysTrackedObjectsPortIfIndex_Type = InterfaceIndex
_EtsysTrackedObjectsPortIfIndex_Object = MibTableColumn
etsysTrackedObjectsPortIfIndex = _EtsysTrackedObjectsPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 7, 1, 1),
    _EtsysTrackedObjectsPortIfIndex_Type()
)
etsysTrackedObjectsPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysTrackedObjectsPortIfIndex.setStatus("current")


class _EtsysTrackedObjectsPortGroupName_Type(SnmpAdminString):
    """Custom type etsysTrackedObjectsPortGroupName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_EtsysTrackedObjectsPortGroupName_Type.__name__ = "SnmpAdminString"
_EtsysTrackedObjectsPortGroupName_Object = MibTableColumn
etsysTrackedObjectsPortGroupName = _EtsysTrackedObjectsPortGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 7, 1, 2),
    _EtsysTrackedObjectsPortGroupName_Type()
)
etsysTrackedObjectsPortGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTrackedObjectsPortGroupName.setStatus("current")


class _EtsysTrackedObjectsPortState_Type(Integer32):
    """Custom type etsysTrackedObjectsPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("notTracked", 4))
    )


_EtsysTrackedObjectsPortState_Type.__name__ = "Integer32"
_EtsysTrackedObjectsPortState_Object = MibTableColumn
etsysTrackedObjectsPortState = _EtsysTrackedObjectsPortState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 7, 1, 3),
    _EtsysTrackedObjectsPortState_Type()
)
etsysTrackedObjectsPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedObjectsPortState.setStatus("current")


class _EtsysTrackedObjectsPortIfSpeedName_Type(SnmpAdminString):
    """Custom type etsysTrackedObjectsPortIfSpeedName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_EtsysTrackedObjectsPortIfSpeedName_Type.__name__ = "SnmpAdminString"
_EtsysTrackedObjectsPortIfSpeedName_Object = MibTableColumn
etsysTrackedObjectsPortIfSpeedName = _EtsysTrackedObjectsPortIfSpeedName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 7, 1, 4),
    _EtsysTrackedObjectsPortIfSpeedName_Type()
)
etsysTrackedObjectsPortIfSpeedName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTrackedObjectsPortIfSpeedName.setStatus("current")
_EtsysTrackedObjectsProbeTsTable_Object = MibTable
etsysTrackedObjectsProbeTsTable = _EtsysTrackedObjectsProbeTsTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 8)
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeTsTable.setStatus("current")
_EtsysTrackedObjectsProbeTsEntry_Object = MibTableRow
etsysTrackedObjectsProbeTsEntry = _EtsysTrackedObjectsProbeTsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 8, 1)
)
etsysTrackedObjectsProbeTsEntry.setIndexNames(
    (1, "ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsProbeName"),
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeTsEntry.setStatus("current")


class _EtsysTrackedObjectsProbeTsInterval_Type(Unsigned32):
    """Custom type etsysTrackedObjectsProbeTsInterval based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 30000),
    )


_EtsysTrackedObjectsProbeTsInterval_Type.__name__ = "Unsigned32"
_EtsysTrackedObjectsProbeTsInterval_Object = MibTableColumn
etsysTrackedObjectsProbeTsInterval = _EtsysTrackedObjectsProbeTsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 8, 1, 1),
    _EtsysTrackedObjectsProbeTsInterval_Type()
)
etsysTrackedObjectsProbeTsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeTsInterval.setStatus("current")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeTsInterval.setUnits("milliseconds")


class _EtsysTrackedObjectsProbeTsRecvWait_Type(Unsigned32):
    """Custom type etsysTrackedObjectsProbeTsRecvWait based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 29900),
    )


_EtsysTrackedObjectsProbeTsRecvWait_Type.__name__ = "Unsigned32"
_EtsysTrackedObjectsProbeTsRecvWait_Object = MibTableColumn
etsysTrackedObjectsProbeTsRecvWait = _EtsysTrackedObjectsProbeTsRecvWait_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 8, 1, 2),
    _EtsysTrackedObjectsProbeTsRecvWait_Type()
)
etsysTrackedObjectsProbeTsRecvWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeTsRecvWait.setStatus("current")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeTsRecvWait.setUnits("milliseconds")


class _EtsysTrackedObjectsProbeTsTOS_Type(Unsigned32):
    """Custom type etsysTrackedObjectsProbeTsTOS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_EtsysTrackedObjectsProbeTsTOS_Type.__name__ = "Unsigned32"
_EtsysTrackedObjectsProbeTsTOS_Object = MibTableColumn
etsysTrackedObjectsProbeTsTOS = _EtsysTrackedObjectsProbeTsTOS_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 8, 1, 3),
    _EtsysTrackedObjectsProbeTsTOS_Type()
)
etsysTrackedObjectsProbeTsTOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeTsTOS.setStatus("current")


class _EtsysTrackedObjectsProbeTsPCP_Type(Unsigned32):
    """Custom type etsysTrackedObjectsProbeTsPCP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_EtsysTrackedObjectsProbeTsPCP_Type.__name__ = "Unsigned32"
_EtsysTrackedObjectsProbeTsPCP_Object = MibTableColumn
etsysTrackedObjectsProbeTsPCP = _EtsysTrackedObjectsProbeTsPCP_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 8, 1, 4),
    _EtsysTrackedObjectsProbeTsPCP_Type()
)
etsysTrackedObjectsProbeTsPCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeTsPCP.setStatus("current")
_EtsysTrackedObjectsPortIfSpeedTable_Object = MibTable
etsysTrackedObjectsPortIfSpeedTable = _EtsysTrackedObjectsPortIfSpeedTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 9)
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsPortIfSpeedTable.setStatus("current")
_EtsysTrackedObjectsPortIfSpeedEntry_Object = MibTableRow
etsysTrackedObjectsPortIfSpeedEntry = _EtsysTrackedObjectsPortIfSpeedEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 9, 1)
)
etsysTrackedObjectsPortIfSpeedEntry.setIndexNames(
    (1, "ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsCommonName"),
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsPortIfSpeedEntry.setStatus("current")
_EtsysTrackedObjectsPortIfSpeedMemberMax_Type = Unsigned32
_EtsysTrackedObjectsPortIfSpeedMemberMax_Object = MibTableColumn
etsysTrackedObjectsPortIfSpeedMemberMax = _EtsysTrackedObjectsPortIfSpeedMemberMax_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 9, 1, 1),
    _EtsysTrackedObjectsPortIfSpeedMemberMax_Type()
)
etsysTrackedObjectsPortIfSpeedMemberMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedObjectsPortIfSpeedMemberMax.setStatus("current")
_EtsysTrackedObjectsPortIfSpeedMemberCount_Type = Gauge32
_EtsysTrackedObjectsPortIfSpeedMemberCount_Object = MibTableColumn
etsysTrackedObjectsPortIfSpeedMemberCount = _EtsysTrackedObjectsPortIfSpeedMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 9, 1, 2),
    _EtsysTrackedObjectsPortIfSpeedMemberCount_Type()
)
etsysTrackedObjectsPortIfSpeedMemberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedObjectsPortIfSpeedMemberCount.setStatus("current")
_EtsysTrackedObjectsPortIfSpeedLow_Type = Gauge32
_EtsysTrackedObjectsPortIfSpeedLow_Object = MibTableColumn
etsysTrackedObjectsPortIfSpeedLow = _EtsysTrackedObjectsPortIfSpeedLow_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 9, 1, 3),
    _EtsysTrackedObjectsPortIfSpeedLow_Type()
)
etsysTrackedObjectsPortIfSpeedLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedObjectsPortIfSpeedLow.setStatus("current")
if mibBuilder.loadTexts:
    etsysTrackedObjectsPortIfSpeedLow.setUnits("Megabits per second")
_EtsysTrackedObjectsPortIfSpeedHigh_Type = Gauge32
_EtsysTrackedObjectsPortIfSpeedHigh_Object = MibTableColumn
etsysTrackedObjectsPortIfSpeedHigh = _EtsysTrackedObjectsPortIfSpeedHigh_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 9, 1, 4),
    _EtsysTrackedObjectsPortIfSpeedHigh_Type()
)
etsysTrackedObjectsPortIfSpeedHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedObjectsPortIfSpeedHigh.setStatus("current")
if mibBuilder.loadTexts:
    etsysTrackedObjectsPortIfSpeedHigh.setUnits("Megabits per second")
_EtsysTrackedObjectsPortIfSpeedStatus_Type = RowStatus
_EtsysTrackedObjectsPortIfSpeedStatus_Object = MibTableColumn
etsysTrackedObjectsPortIfSpeedStatus = _EtsysTrackedObjectsPortIfSpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 1, 2, 9, 1, 5),
    _EtsysTrackedObjectsPortIfSpeedStatus_Type()
)
etsysTrackedObjectsPortIfSpeedStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTrackedObjectsPortIfSpeedStatus.setStatus("current")
_EtsysTrackedObjectsConformance_ObjectIdentity = ObjectIdentity
etsysTrackedObjectsConformance = _EtsysTrackedObjectsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 2)
)
_EtsysTrackedObjectsGroups_ObjectIdentity = ObjectIdentity
etsysTrackedObjectsGroups = _EtsysTrackedObjectsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 2, 1)
)
_EtsysTrackedObjectsCompliances_ObjectIdentity = ObjectIdentity
etsysTrackedObjectsCompliances = _EtsysTrackedObjectsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 2, 2)
)

# Managed Objects groups

etsysTrackedObjectsGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 2, 1, 1)
)
etsysTrackedObjectsGlobalGroup.setObjects(
      *(("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsMaxObjects"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsObjectsUsed"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsMaxProbes"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsProbesUsed"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsMaxAcvProbes"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsAcvProbesUsed"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsMaxSessions"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsSessionsUsed"))
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsGlobalGroup.setStatus("deprecated")

etsysTrackedObjectsProbeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 2, 1, 2)
)
etsysTrackedObjectsProbeGroup.setObjects(
      *(("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsProbeIndex"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsProbeDefault"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsProbeType"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsProbeAcvClose"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsProbeAcvReply"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsProbeAcvRequest"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsProbeAcvDepth"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsProbeFdCount"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsProbeFdInterval"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsProbePdCount"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsProbePdInterval"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsProbeOpen"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsProbeReceive"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsProbeInservice"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsProbeDescription"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsProbeStatus"))
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeGroup.setStatus("current")

etsysTrackedObjectsSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 2, 1, 3)
)
etsysTrackedObjectsSessionGroup.setObjects(
      *(("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsSessionState"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsSessionStateChanges"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsSessionLastChange"))
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsSessionGroup.setStatus("current")

etsysTrackedObjectsCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 2, 1, 4)
)
etsysTrackedObjectsCommonGroup.setObjects(
      *(("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsCommonType"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsCommonState"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsCommonDelayUp"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsCommonDelayDown"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsCommonDescription"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsCommonInservice"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsCommonActionUp"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsCommonActionDown"))
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsCommonGroup.setStatus("current")

etsysTrackedObjectsIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 2, 1, 5)
)
etsysTrackedObjectsIfGroup.setObjects(
      *(("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsIntfIndex"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsIntfOption"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsIntfStatus"))
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsIfGroup.setStatus("current")

etsysTrackedObjectsRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 2, 1, 6)
)
etsysTrackedObjectsRouteGroup.setObjects(
      *(("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsRouteType"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsRoutePrefix"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsRoute"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsRouteOption"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsRouteMetricUpThresh"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsRouteMetricDownThresh"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsRouteStatus"))
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsRouteGroup.setStatus("current")

etsysTrackedObjectsPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 2, 1, 7)
)
etsysTrackedObjectsPortGroup.setObjects(
      *(("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsPortGroupMemberMax"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsPortGroupMemberCount"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsPortGroupStatus"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsPortGroupName"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsPortState"))
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsPortGroup.setStatus("current")

etsysTrackedObjectsPortGroupThresh = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 2, 1, 8)
)
etsysTrackedObjectsPortGroupThresh.setObjects(
      *(("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsPortGroupUpCount"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsPortGroupDownCount"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsPortGroupUpThresh"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsPortGroupDownThresh"))
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsPortGroupThresh.setStatus("current")

etsysTrackedObjectsProbeTsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 2, 1, 9)
)
etsysTrackedObjectsProbeTsGroup.setObjects(
      *(("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsProbeTsInterval"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsProbeTsRecvWait"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsProbeTsTOS"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsProbeTsPCP"))
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsProbeTsGroup.setStatus("current")

etsysTrackedObjectsPortIfSpeedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 2, 1, 10)
)
etsysTrackedObjectsPortIfSpeedGroup.setObjects(
      *(("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsPortIfSpeedMemberMax"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsPortIfSpeedMemberCount"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsPortIfSpeedLow"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsPortIfSpeedHigh"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsPortIfSpeedStatus"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsPortIfSpeedName"))
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsPortIfSpeedGroup.setStatus("current")

etsysTrackedObjectsGlobalGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 2, 1, 11)
)
etsysTrackedObjectsGlobalGroup2.setObjects(
      *(("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsMaxObjects"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsObjectsUsed"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsMaxProbes"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsProbesUsed"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsMaxAcvProbes"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsAcvProbesUsed"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsMaxSessions"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsSessionsUsed"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsMaxIntfAssoc"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsIntfAssocUsed"))
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsGlobalGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysTrackedObjectsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 2, 2, 1)
)
etsysTrackedObjectsCompliance.setObjects(
      *(("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsGlobalGroup"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsProbeGroup"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsSessionGroup"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsCommonGroup"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsIfGroup"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsRouteGroup"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsPortGroup"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsPortGroupThresh"))
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsCompliance.setStatus(
        "deprecated"
    )

etsysTrackedObjectsCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 79, 2, 2, 2)
)
etsysTrackedObjectsCompliance2.setObjects(
      *(("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsGlobalGroup2"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsProbeGroup"),
        ("ENTERASYS-TRACKED-OBJECTS-MIB", "etsysTrackedObjectsSessionGroup"))
)
if mibBuilder.loadTexts:
    etsysTrackedObjectsCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-TRACKED-OBJECTS-MIB",
    **{"etsysTrackedObjectsMIB": etsysTrackedObjectsMIB,
       "etsysTrackedObjects": etsysTrackedObjects,
       "etsysTrackedObjectsGlobals": etsysTrackedObjectsGlobals,
       "etsysTrackedObjectsMaxObjects": etsysTrackedObjectsMaxObjects,
       "etsysTrackedObjectsObjectsUsed": etsysTrackedObjectsObjectsUsed,
       "etsysTrackedObjectsMaxProbes": etsysTrackedObjectsMaxProbes,
       "etsysTrackedObjectsProbesUsed": etsysTrackedObjectsProbesUsed,
       "etsysTrackedObjectsMaxAcvProbes": etsysTrackedObjectsMaxAcvProbes,
       "etsysTrackedObjectsAcvProbesUsed": etsysTrackedObjectsAcvProbesUsed,
       "etsysTrackedObjectsMaxSessions": etsysTrackedObjectsMaxSessions,
       "etsysTrackedObjectsSessionsUsed": etsysTrackedObjectsSessionsUsed,
       "etsysTrackedObjectsMaxIntfAssoc": etsysTrackedObjectsMaxIntfAssoc,
       "etsysTrackedObjectsIntfAssocUsed": etsysTrackedObjectsIntfAssocUsed,
       "etsysTrackedObjectsTables": etsysTrackedObjectsTables,
       "etsysTrackedObjectsProbeTable": etsysTrackedObjectsProbeTable,
       "etsysTrackedObjectsProbeEntry": etsysTrackedObjectsProbeEntry,
       "etsysTrackedObjectsProbeName": etsysTrackedObjectsProbeName,
       "etsysTrackedObjectsProbeIndex": etsysTrackedObjectsProbeIndex,
       "etsysTrackedObjectsProbeDefault": etsysTrackedObjectsProbeDefault,
       "etsysTrackedObjectsProbeType": etsysTrackedObjectsProbeType,
       "etsysTrackedObjectsProbeAcvClose": etsysTrackedObjectsProbeAcvClose,
       "etsysTrackedObjectsProbeAcvReply": etsysTrackedObjectsProbeAcvReply,
       "etsysTrackedObjectsProbeAcvRequest": etsysTrackedObjectsProbeAcvRequest,
       "etsysTrackedObjectsProbeAcvDepth": etsysTrackedObjectsProbeAcvDepth,
       "etsysTrackedObjectsProbeFdCount": etsysTrackedObjectsProbeFdCount,
       "etsysTrackedObjectsProbeFdInterval": etsysTrackedObjectsProbeFdInterval,
       "etsysTrackedObjectsProbePdCount": etsysTrackedObjectsProbePdCount,
       "etsysTrackedObjectsProbePdInterval": etsysTrackedObjectsProbePdInterval,
       "etsysTrackedObjectsProbeOpen": etsysTrackedObjectsProbeOpen,
       "etsysTrackedObjectsProbeReceive": etsysTrackedObjectsProbeReceive,
       "etsysTrackedObjectsProbeInservice": etsysTrackedObjectsProbeInservice,
       "etsysTrackedObjectsProbeDescription": etsysTrackedObjectsProbeDescription,
       "etsysTrackedObjectsProbeStatus": etsysTrackedObjectsProbeStatus,
       "etsysTrackedObjectsSessionTable": etsysTrackedObjectsSessionTable,
       "etsysTrackedObjectsSessionEntry": etsysTrackedObjectsSessionEntry,
       "etsysTrackedObjectsSessionType": etsysTrackedObjectsSessionType,
       "etsysTrackedObjectsSessionAddr": etsysTrackedObjectsSessionAddr,
       "etsysTrackedObjectsSessionPort": etsysTrackedObjectsSessionPort,
       "etsysTrackedObjectsSessionState": etsysTrackedObjectsSessionState,
       "etsysTrackedObjectsSessionStateChanges": etsysTrackedObjectsSessionStateChanges,
       "etsysTrackedObjectsSessionLastChange": etsysTrackedObjectsSessionLastChange,
       "etsysTrackedObjectsCommonTable": etsysTrackedObjectsCommonTable,
       "etsysTrackedObjectsCommonEntry": etsysTrackedObjectsCommonEntry,
       "etsysTrackedObjectsCommonName": etsysTrackedObjectsCommonName,
       "etsysTrackedObjectsCommonType": etsysTrackedObjectsCommonType,
       "etsysTrackedObjectsCommonState": etsysTrackedObjectsCommonState,
       "etsysTrackedObjectsCommonDelayUp": etsysTrackedObjectsCommonDelayUp,
       "etsysTrackedObjectsCommonDelayDown": etsysTrackedObjectsCommonDelayDown,
       "etsysTrackedObjectsCommonDescription": etsysTrackedObjectsCommonDescription,
       "etsysTrackedObjectsCommonInservice": etsysTrackedObjectsCommonInservice,
       "etsysTrackedObjectsCommonActionUp": etsysTrackedObjectsCommonActionUp,
       "etsysTrackedObjectsCommonActionDown": etsysTrackedObjectsCommonActionDown,
       "etsysTrackedObjectsIntfTable": etsysTrackedObjectsIntfTable,
       "etsysTrackedObjectsIntfEntry": etsysTrackedObjectsIntfEntry,
       "etsysTrackedObjectsIntfIndex": etsysTrackedObjectsIntfIndex,
       "etsysTrackedObjectsIntfOption": etsysTrackedObjectsIntfOption,
       "etsysTrackedObjectsIntfStatus": etsysTrackedObjectsIntfStatus,
       "etsysTrackedObjectsRouteTable": etsysTrackedObjectsRouteTable,
       "etsysTrackedObjectsRouteEntry": etsysTrackedObjectsRouteEntry,
       "etsysTrackedObjectsRouteType": etsysTrackedObjectsRouteType,
       "etsysTrackedObjectsRoutePrefix": etsysTrackedObjectsRoutePrefix,
       "etsysTrackedObjectsRoute": etsysTrackedObjectsRoute,
       "etsysTrackedObjectsRouteOption": etsysTrackedObjectsRouteOption,
       "etsysTrackedObjectsRouteMetricUpThresh": etsysTrackedObjectsRouteMetricUpThresh,
       "etsysTrackedObjectsRouteMetricDownThresh": etsysTrackedObjectsRouteMetricDownThresh,
       "etsysTrackedObjectsRouteStatus": etsysTrackedObjectsRouteStatus,
       "etsysTrackedObjectsPortGroupTable": etsysTrackedObjectsPortGroupTable,
       "etsysTrackedObjectsPortGroupEntry": etsysTrackedObjectsPortGroupEntry,
       "etsysTrackedObjectsPortGroupMemberMax": etsysTrackedObjectsPortGroupMemberMax,
       "etsysTrackedObjectsPortGroupMemberCount": etsysTrackedObjectsPortGroupMemberCount,
       "etsysTrackedObjectsPortGroupStatus": etsysTrackedObjectsPortGroupStatus,
       "etsysTrackedObjectsPortGroupUpCount": etsysTrackedObjectsPortGroupUpCount,
       "etsysTrackedObjectsPortGroupDownCount": etsysTrackedObjectsPortGroupDownCount,
       "etsysTrackedObjectsPortGroupUpThresh": etsysTrackedObjectsPortGroupUpThresh,
       "etsysTrackedObjectsPortGroupDownThresh": etsysTrackedObjectsPortGroupDownThresh,
       "etsysTrackedObjectsPortTable": etsysTrackedObjectsPortTable,
       "etsysTrackedObjectsPortEntry": etsysTrackedObjectsPortEntry,
       "etsysTrackedObjectsPortIfIndex": etsysTrackedObjectsPortIfIndex,
       "etsysTrackedObjectsPortGroupName": etsysTrackedObjectsPortGroupName,
       "etsysTrackedObjectsPortState": etsysTrackedObjectsPortState,
       "etsysTrackedObjectsPortIfSpeedName": etsysTrackedObjectsPortIfSpeedName,
       "etsysTrackedObjectsProbeTsTable": etsysTrackedObjectsProbeTsTable,
       "etsysTrackedObjectsProbeTsEntry": etsysTrackedObjectsProbeTsEntry,
       "etsysTrackedObjectsProbeTsInterval": etsysTrackedObjectsProbeTsInterval,
       "etsysTrackedObjectsProbeTsRecvWait": etsysTrackedObjectsProbeTsRecvWait,
       "etsysTrackedObjectsProbeTsTOS": etsysTrackedObjectsProbeTsTOS,
       "etsysTrackedObjectsProbeTsPCP": etsysTrackedObjectsProbeTsPCP,
       "etsysTrackedObjectsPortIfSpeedTable": etsysTrackedObjectsPortIfSpeedTable,
       "etsysTrackedObjectsPortIfSpeedEntry": etsysTrackedObjectsPortIfSpeedEntry,
       "etsysTrackedObjectsPortIfSpeedMemberMax": etsysTrackedObjectsPortIfSpeedMemberMax,
       "etsysTrackedObjectsPortIfSpeedMemberCount": etsysTrackedObjectsPortIfSpeedMemberCount,
       "etsysTrackedObjectsPortIfSpeedLow": etsysTrackedObjectsPortIfSpeedLow,
       "etsysTrackedObjectsPortIfSpeedHigh": etsysTrackedObjectsPortIfSpeedHigh,
       "etsysTrackedObjectsPortIfSpeedStatus": etsysTrackedObjectsPortIfSpeedStatus,
       "etsysTrackedObjectsConformance": etsysTrackedObjectsConformance,
       "etsysTrackedObjectsGroups": etsysTrackedObjectsGroups,
       "etsysTrackedObjectsGlobalGroup": etsysTrackedObjectsGlobalGroup,
       "etsysTrackedObjectsProbeGroup": etsysTrackedObjectsProbeGroup,
       "etsysTrackedObjectsSessionGroup": etsysTrackedObjectsSessionGroup,
       "etsysTrackedObjectsCommonGroup": etsysTrackedObjectsCommonGroup,
       "etsysTrackedObjectsIfGroup": etsysTrackedObjectsIfGroup,
       "etsysTrackedObjectsRouteGroup": etsysTrackedObjectsRouteGroup,
       "etsysTrackedObjectsPortGroup": etsysTrackedObjectsPortGroup,
       "etsysTrackedObjectsPortGroupThresh": etsysTrackedObjectsPortGroupThresh,
       "etsysTrackedObjectsProbeTsGroup": etsysTrackedObjectsProbeTsGroup,
       "etsysTrackedObjectsPortIfSpeedGroup": etsysTrackedObjectsPortIfSpeedGroup,
       "etsysTrackedObjectsGlobalGroup2": etsysTrackedObjectsGlobalGroup2,
       "etsysTrackedObjectsCompliances": etsysTrackedObjectsCompliances,
       "etsysTrackedObjectsCompliance": etsysTrackedObjectsCompliance,
       "etsysTrackedObjectsCompliance2": etsysTrackedObjectsCompliance2}
)
