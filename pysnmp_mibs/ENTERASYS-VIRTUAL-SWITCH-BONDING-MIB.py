# SNMP MIB module (ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:47:14 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

etsysVirtualSwitchBondingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83)
)
if mibBuilder.loadTexts:
    etsysVirtualSwitchBondingMIB.setRevisions(
        ("2012-03-13 19:14",
         "2012-02-07 15:53",
         "2011-12-13 20:31")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VsbId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )



class VsbChassisStatus(TextualConvention, Integer32):
    status = "current"
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
          ("incomplete", 3),
          ("inactive", 4))
    )



class VsbSlotList(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_EtsysVsbObjects_ObjectIdentity = ObjectIdentity
etsysVsbObjects = _EtsysVsbObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1)
)
_EtsysVsbSystem_ObjectIdentity = ObjectIdentity
etsysVsbSystem = _EtsysVsbSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 1)
)


class _EtsysVsbSystemEnable_Type(Integer32):
    """Custom type etsysVsbSystemEnable based on Integer32"""
    defaultValue = 2

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


_EtsysVsbSystemEnable_Type.__name__ = "Integer32"
_EtsysVsbSystemEnable_Object = MibScalar
etsysVsbSystemEnable = _EtsysVsbSystemEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 1, 1),
    _EtsysVsbSystemEnable_Type()
)
etsysVsbSystemEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysVsbSystemEnable.setStatus("current")
_EtsysVsbSystemMaxChassis_Type = Unsigned32
_EtsysVsbSystemMaxChassis_Object = MibScalar
etsysVsbSystemMaxChassis = _EtsysVsbSystemMaxChassis_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 1, 2),
    _EtsysVsbSystemMaxChassis_Type()
)
etsysVsbSystemMaxChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysVsbSystemMaxChassis.setStatus("current")
_EtsysVsbSystemMaxSlotNumber_Type = Unsigned32
_EtsysVsbSystemMaxSlotNumber_Object = MibScalar
etsysVsbSystemMaxSlotNumber = _EtsysVsbSystemMaxSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 1, 3),
    _EtsysVsbSystemMaxSlotNumber_Type()
)
etsysVsbSystemMaxSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysVsbSystemMaxSlotNumber.setStatus("current")
_EtsysVsbAdministrativeMacAddress_Type = MacAddress
_EtsysVsbAdministrativeMacAddress_Object = MibScalar
etsysVsbAdministrativeMacAddress = _EtsysVsbAdministrativeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 1, 4),
    _EtsysVsbAdministrativeMacAddress_Type()
)
etsysVsbAdministrativeMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysVsbAdministrativeMacAddress.setStatus("current")
_EtsysVsbOperationalMacAddress_Type = MacAddress
_EtsysVsbOperationalMacAddress_Object = MibScalar
etsysVsbOperationalMacAddress = _EtsysVsbOperationalMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 1, 5),
    _EtsysVsbOperationalMacAddress_Type()
)
etsysVsbOperationalMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysVsbOperationalMacAddress.setStatus("current")


class _EtsysVsbSystemLinkFailureResponse_Type(Integer32):
    """Custom type etsysVsbSystemLinkFailureResponse based on Integer32"""
    defaultValue = 2

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


_EtsysVsbSystemLinkFailureResponse_Type.__name__ = "Integer32"
_EtsysVsbSystemLinkFailureResponse_Object = MibScalar
etsysVsbSystemLinkFailureResponse = _EtsysVsbSystemLinkFailureResponse_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 1, 6),
    _EtsysVsbSystemLinkFailureResponse_Type()
)
etsysVsbSystemLinkFailureResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysVsbSystemLinkFailureResponse.setStatus("current")
_EtsysVsbChassis_ObjectIdentity = ObjectIdentity
etsysVsbChassis = _EtsysVsbChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 2)
)
_EtsysVsbChassisTable_Object = MibTable
etsysVsbChassisTable = _EtsysVsbChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysVsbChassisTable.setStatus("current")
_EtsysVsbChassisEntry_Object = MibTableRow
etsysVsbChassisEntry = _EtsysVsbChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 2, 1, 1)
)
etsysVsbChassisEntry.setIndexNames(
    (0, "ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisIndex"),
)
if mibBuilder.loadTexts:
    etsysVsbChassisEntry.setStatus("current")
_EtsysVsbChassisIndex_Type = Unsigned32
_EtsysVsbChassisIndex_Object = MibTableColumn
etsysVsbChassisIndex = _EtsysVsbChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 2, 1, 1, 1),
    _EtsysVsbChassisIndex_Type()
)
etsysVsbChassisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysVsbChassisIndex.setStatus("current")
_EtsysVsbChassisSystemId_Type = VsbId
_EtsysVsbChassisSystemId_Object = MibTableColumn
etsysVsbChassisSystemId = _EtsysVsbChassisSystemId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 2, 1, 1, 2),
    _EtsysVsbChassisSystemId_Type()
)
etsysVsbChassisSystemId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysVsbChassisSystemId.setStatus("current")


class _EtsysVsbChassisSerialNum_Type(SnmpAdminString):
    """Custom type etsysVsbChassisSerialNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EtsysVsbChassisSerialNum_Type.__name__ = "SnmpAdminString"
_EtsysVsbChassisSerialNum_Object = MibTableColumn
etsysVsbChassisSerialNum = _EtsysVsbChassisSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 2, 1, 1, 3),
    _EtsysVsbChassisSerialNum_Type()
)
etsysVsbChassisSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysVsbChassisSerialNum.setStatus("current")


class _EtsysVsbChassisFirstSlotNumber_Type(Unsigned32):
    """Custom type etsysVsbChassisFirstSlotNumber based on Unsigned32"""
    defaultValue = 0


_EtsysVsbChassisFirstSlotNumber_Type.__name__ = "Unsigned32"
_EtsysVsbChassisFirstSlotNumber_Object = MibTableColumn
etsysVsbChassisFirstSlotNumber = _EtsysVsbChassisFirstSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 2, 1, 1, 4),
    _EtsysVsbChassisFirstSlotNumber_Type()
)
etsysVsbChassisFirstSlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysVsbChassisFirstSlotNumber.setStatus("current")
_EtsysVsbChassisLocalSlotList_Type = VsbSlotList
_EtsysVsbChassisLocalSlotList_Object = MibTableColumn
etsysVsbChassisLocalSlotList = _EtsysVsbChassisLocalSlotList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 2, 1, 1, 5),
    _EtsysVsbChassisLocalSlotList_Type()
)
etsysVsbChassisLocalSlotList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysVsbChassisLocalSlotList.setStatus("current")
_EtsysVsbChassisSystemSlotList_Type = VsbSlotList
_EtsysVsbChassisSystemSlotList_Object = MibTableColumn
etsysVsbChassisSystemSlotList = _EtsysVsbChassisSystemSlotList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 2, 1, 1, 6),
    _EtsysVsbChassisSystemSlotList_Type()
)
etsysVsbChassisSystemSlotList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysVsbChassisSystemSlotList.setStatus("current")
_EtsysVsbChassisStatus_Type = VsbChassisStatus
_EtsysVsbChassisStatus_Object = MibTableColumn
etsysVsbChassisStatus = _EtsysVsbChassisStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 2, 1, 1, 7),
    _EtsysVsbChassisStatus_Type()
)
etsysVsbChassisStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysVsbChassisStatus.setStatus("current")
_EtsysVsbChassisLastBondTime_Type = TimeStamp
_EtsysVsbChassisLastBondTime_Object = MibTableColumn
etsysVsbChassisLastBondTime = _EtsysVsbChassisLastBondTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 2, 1, 1, 8),
    _EtsysVsbChassisLastBondTime_Type()
)
etsysVsbChassisLastBondTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysVsbChassisLastBondTime.setStatus("current")


class _EtsysVsbChassisSharedSecret_Type(SnmpAdminString):
    """Custom type etsysVsbChassisSharedSecret based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EtsysVsbChassisSharedSecret_Type.__name__ = "SnmpAdminString"
_EtsysVsbChassisSharedSecret_Object = MibTableColumn
etsysVsbChassisSharedSecret = _EtsysVsbChassisSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 2, 1, 1, 9),
    _EtsysVsbChassisSharedSecret_Type()
)
etsysVsbChassisSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysVsbChassisSharedSecret.setStatus("current")
_EtsysVsbChassisSecretEntered_Type = TruthValue
_EtsysVsbChassisSecretEntered_Object = MibTableColumn
etsysVsbChassisSecretEntered = _EtsysVsbChassisSecretEntered_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 2, 1, 1, 10),
    _EtsysVsbChassisSecretEntered_Type()
)
etsysVsbChassisSecretEntered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysVsbChassisSecretEntered.setStatus("current")
_EtsysVsbChassisLfrOperPriority_Type = Unsigned32
_EtsysVsbChassisLfrOperPriority_Object = MibTableColumn
etsysVsbChassisLfrOperPriority = _EtsysVsbChassisLfrOperPriority_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 2, 1, 1, 11),
    _EtsysVsbChassisLfrOperPriority_Type()
)
etsysVsbChassisLfrOperPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysVsbChassisLfrOperPriority.setStatus("current")
_EtsysVsbPort_ObjectIdentity = ObjectIdentity
etsysVsbPort = _EtsysVsbPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 3)
)
_EtsysVsbPortTable_Object = MibTable
etsysVsbPortTable = _EtsysVsbPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 3, 1)
)
if mibBuilder.loadTexts:
    etsysVsbPortTable.setStatus("current")
_EtsysVsbPortEntry_Object = MibTableRow
etsysVsbPortEntry = _EtsysVsbPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 3, 1, 1)
)
etsysVsbPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysVsbPortEntry.setStatus("current")


class _EtsysVsbPortAdminStatus_Type(Integer32):
    """Custom type etsysVsbPortAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_EtsysVsbPortAdminStatus_Type.__name__ = "Integer32"
_EtsysVsbPortAdminStatus_Object = MibTableColumn
etsysVsbPortAdminStatus = _EtsysVsbPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 3, 1, 1, 1),
    _EtsysVsbPortAdminStatus_Type()
)
etsysVsbPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysVsbPortAdminStatus.setStatus("current")


class _EtsysVsbPortOperStatus_Type(Integer32):
    """Custom type etsysVsbPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("highLatency", 3),
          ("probeLoop", 4),
          ("probeTimeout", 5),
          ("portInstability", 6))
    )


_EtsysVsbPortOperStatus_Type.__name__ = "Integer32"
_EtsysVsbPortOperStatus_Object = MibTableColumn
etsysVsbPortOperStatus = _EtsysVsbPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 3, 1, 1, 2),
    _EtsysVsbPortOperStatus_Type()
)
etsysVsbPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysVsbPortOperStatus.setStatus("current")
_EtsysVsbConformance_ObjectIdentity = ObjectIdentity
etsysVsbConformance = _EtsysVsbConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 2)
)
_EtsysVsbGroups_ObjectIdentity = ObjectIdentity
etsysVsbGroups = _EtsysVsbGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 2, 1)
)
_EtsysVsbCompliances_ObjectIdentity = ObjectIdentity
etsysVsbCompliances = _EtsysVsbCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 2, 2)
)

# Managed Objects groups

etsysVsbSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 2, 1, 1)
)
etsysVsbSystemGroup.setObjects(
      *(("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbSystemEnable"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbSystemMaxChassis"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbSystemMaxSlotNumber"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbAdministrativeMacAddress"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbOperationalMacAddress"))
)
if mibBuilder.loadTexts:
    etsysVsbSystemGroup.setStatus("deprecated")

etsysVsbChassisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 2, 1, 2)
)
etsysVsbChassisGroup.setObjects(
      *(("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisSystemId"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisSerialNum"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisFirstSlotNumber"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisLocalSlotList"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisSystemSlotList"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisStatus"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisLastBondTime"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisSharedSecret"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisSecretEntered"))
)
if mibBuilder.loadTexts:
    etsysVsbChassisGroup.setStatus("deprecated")

etsysVsbPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 2, 1, 3)
)
etsysVsbPortGroup.setObjects(
      *(("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbPortAdminStatus"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbPortOperStatus"))
)
if mibBuilder.loadTexts:
    etsysVsbPortGroup.setStatus("current")

etsysVsbSystemGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 2, 1, 4)
)
etsysVsbSystemGroup2.setObjects(
      *(("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbSystemEnable"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbSystemMaxChassis"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbSystemMaxSlotNumber"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbAdministrativeMacAddress"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbOperationalMacAddress"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbSystemLinkFailureResponse"))
)
if mibBuilder.loadTexts:
    etsysVsbSystemGroup2.setStatus("current")

etsysVsbChassisGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 2, 1, 5)
)
etsysVsbChassisGroup2.setObjects(
      *(("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisSystemId"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisSerialNum"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisFirstSlotNumber"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisLocalSlotList"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisSystemSlotList"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisStatus"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisLastBondTime"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisSharedSecret"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisSecretEntered"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisLfrOperPriority"))
)
if mibBuilder.loadTexts:
    etsysVsbChassisGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysVsbCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 2, 2, 1)
)
etsysVsbCompliance.setObjects(
      *(("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbSystemGroup"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisGroup"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbPortGroup"))
)
if mibBuilder.loadTexts:
    etsysVsbCompliance.setStatus(
        "deprecated"
    )

etsysVsbCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 2, 2, 2)
)
etsysVsbCompliance2.setObjects(
      *(("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbSystemGroup2"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisGroup2"),
        ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbPortGroup"))
)
if mibBuilder.loadTexts:
    etsysVsbCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB",
    **{"VsbId": VsbId,
       "VsbChassisStatus": VsbChassisStatus,
       "VsbSlotList": VsbSlotList,
       "etsysVirtualSwitchBondingMIB": etsysVirtualSwitchBondingMIB,
       "etsysVsbObjects": etsysVsbObjects,
       "etsysVsbSystem": etsysVsbSystem,
       "etsysVsbSystemEnable": etsysVsbSystemEnable,
       "etsysVsbSystemMaxChassis": etsysVsbSystemMaxChassis,
       "etsysVsbSystemMaxSlotNumber": etsysVsbSystemMaxSlotNumber,
       "etsysVsbAdministrativeMacAddress": etsysVsbAdministrativeMacAddress,
       "etsysVsbOperationalMacAddress": etsysVsbOperationalMacAddress,
       "etsysVsbSystemLinkFailureResponse": etsysVsbSystemLinkFailureResponse,
       "etsysVsbChassis": etsysVsbChassis,
       "etsysVsbChassisTable": etsysVsbChassisTable,
       "etsysVsbChassisEntry": etsysVsbChassisEntry,
       "etsysVsbChassisIndex": etsysVsbChassisIndex,
       "etsysVsbChassisSystemId": etsysVsbChassisSystemId,
       "etsysVsbChassisSerialNum": etsysVsbChassisSerialNum,
       "etsysVsbChassisFirstSlotNumber": etsysVsbChassisFirstSlotNumber,
       "etsysVsbChassisLocalSlotList": etsysVsbChassisLocalSlotList,
       "etsysVsbChassisSystemSlotList": etsysVsbChassisSystemSlotList,
       "etsysVsbChassisStatus": etsysVsbChassisStatus,
       "etsysVsbChassisLastBondTime": etsysVsbChassisLastBondTime,
       "etsysVsbChassisSharedSecret": etsysVsbChassisSharedSecret,
       "etsysVsbChassisSecretEntered": etsysVsbChassisSecretEntered,
       "etsysVsbChassisLfrOperPriority": etsysVsbChassisLfrOperPriority,
       "etsysVsbPort": etsysVsbPort,
       "etsysVsbPortTable": etsysVsbPortTable,
       "etsysVsbPortEntry": etsysVsbPortEntry,
       "etsysVsbPortAdminStatus": etsysVsbPortAdminStatus,
       "etsysVsbPortOperStatus": etsysVsbPortOperStatus,
       "etsysVsbConformance": etsysVsbConformance,
       "etsysVsbGroups": etsysVsbGroups,
       "etsysVsbSystemGroup": etsysVsbSystemGroup,
       "etsysVsbChassisGroup": etsysVsbChassisGroup,
       "etsysVsbPortGroup": etsysVsbPortGroup,
       "etsysVsbSystemGroup2": etsysVsbSystemGroup2,
       "etsysVsbChassisGroup2": etsysVsbChassisGroup2,
       "etsysVsbCompliances": etsysVsbCompliances,
       "etsysVsbCompliance": etsysVsbCompliance,
       "etsysVsbCompliance2": etsysVsbCompliance2}
)
