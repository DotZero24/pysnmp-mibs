# SNMP MIB module (OnAccess2200-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/firstmile/OnAccess2200-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:09:20 2025
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Firstmilecom_ObjectIdentity = ObjectIdentity
firstmilecom = _Firstmilecom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28350)
)
_Mc_ObjectIdentity = ObjectIdentity
mc = _Mc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28350, 4)
)
_Onaccess2200_ObjectIdentity = ObjectIdentity
onaccess2200 = _Onaccess2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1)
)
_Mc2200_NMC_ObjectIdentity = ObjectIdentity
mc2200_NMC = _Mc2200_NMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1)
)
_Mc2200_SystemInfo_ObjectIdentity = ObjectIdentity
mc2200_SystemInfo = _Mc2200_SystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1, 0)
)
_Mc2200_SysIPAddress_Type = IpAddress
_Mc2200_SysIPAddress_Object = MibScalar
mc2200_SysIPAddress = _Mc2200_SysIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1, 0, 1),
    _Mc2200_SysIPAddress_Type()
)
mc2200_SysIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_SysIPAddress.setStatus("mandatory")
_Mc2200_SysSubnetMask_Type = IpAddress
_Mc2200_SysSubnetMask_Object = MibScalar
mc2200_SysSubnetMask = _Mc2200_SysSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1, 0, 2),
    _Mc2200_SysSubnetMask_Type()
)
mc2200_SysSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_SysSubnetMask.setStatus("mandatory")
_Mc2200_SysGateway_Type = IpAddress
_Mc2200_SysGateway_Object = MibScalar
mc2200_SysGateway = _Mc2200_SysGateway_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1, 0, 3),
    _Mc2200_SysGateway_Type()
)
mc2200_SysGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_SysGateway.setStatus("mandatory")
_Mc2200_SysMACAddress_Type = IpAddress
_Mc2200_SysMACAddress_Object = MibScalar
mc2200_SysMACAddress = _Mc2200_SysMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1, 0, 4),
    _Mc2200_SysMACAddress_Type()
)
mc2200_SysMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_SysMACAddress.setStatus("mandatory")
_Mc2200_SysContact_Type = DisplayString
_Mc2200_SysContact_Object = MibScalar
mc2200_SysContact = _Mc2200_SysContact_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1, 0, 5),
    _Mc2200_SysContact_Type()
)
mc2200_SysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_SysContact.setStatus("mandatory")
_Mc2200_SysName_Type = DisplayString
_Mc2200_SysName_Object = MibScalar
mc2200_SysName = _Mc2200_SysName_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1, 0, 6),
    _Mc2200_SysName_Type()
)
mc2200_SysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_SysName.setStatus("mandatory")
_Mc2200_SysLocation_Type = DisplayString
_Mc2200_SysLocation_Object = MibScalar
mc2200_SysLocation = _Mc2200_SysLocation_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1, 0, 7),
    _Mc2200_SysLocation_Type()
)
mc2200_SysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_SysLocation.setStatus("mandatory")
_Mc2200_SNMPTrapIP1_Type = IpAddress
_Mc2200_SNMPTrapIP1_Object = MibScalar
mc2200_SNMPTrapIP1 = _Mc2200_SNMPTrapIP1_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1, 0, 8),
    _Mc2200_SNMPTrapIP1_Type()
)
mc2200_SNMPTrapIP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_SNMPTrapIP1.setStatus("mandatory")
_Mc2200_SNMPTrapIP2_Type = IpAddress
_Mc2200_SNMPTrapIP2_Object = MibScalar
mc2200_SNMPTrapIP2 = _Mc2200_SNMPTrapIP2_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1, 0, 9),
    _Mc2200_SNMPTrapIP2_Type()
)
mc2200_SNMPTrapIP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_SNMPTrapIP2.setStatus("mandatory")
_Mc2200_SNMPTrapIP3_Type = IpAddress
_Mc2200_SNMPTrapIP3_Object = MibScalar
mc2200_SNMPTrapIP3 = _Mc2200_SNMPTrapIP3_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1, 0, 10),
    _Mc2200_SNMPTrapIP3_Type()
)
mc2200_SNMPTrapIP3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_SNMPTrapIP3.setStatus("mandatory")
_Mc2200_SNMPTrapIP4_Type = IpAddress
_Mc2200_SNMPTrapIP4_Object = MibScalar
mc2200_SNMPTrapIP4 = _Mc2200_SNMPTrapIP4_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1, 0, 11),
    _Mc2200_SNMPTrapIP4_Type()
)
mc2200_SNMPTrapIP4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_SNMPTrapIP4.setStatus("mandatory")
_Mc2200_SNMPTrapIP5_Type = IpAddress
_Mc2200_SNMPTrapIP5_Object = MibScalar
mc2200_SNMPTrapIP5 = _Mc2200_SNMPTrapIP5_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1, 0, 12),
    _Mc2200_SNMPTrapIP5_Type()
)
mc2200_SNMPTrapIP5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_SNMPTrapIP5.setStatus("mandatory")
_Mc2200_alarminfor_Type = DisplayString
_Mc2200_alarminfor_Object = MibScalar
mc2200_alarminfor = _Mc2200_alarminfor_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1, 0, 13),
    _Mc2200_alarminfor_Type()
)
mc2200_alarminfor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mc2200_alarminfor.setStatus("mandatory")
_Mc2200_Master_ObjectIdentity = ObjectIdentity
mc2200_Master = _Mc2200_Master_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1, 1)
)
_Mc2200_ch0ChassisDetail_ObjectIdentity = ObjectIdentity
mc2200_ch0ChassisDetail = _Mc2200_ch0ChassisDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1, 1, 0)
)


class _Mc2200_ch0Status_Type(Integer32):
    """Custom type mc2200_ch0Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 2))
    )


_Mc2200_ch0Status_Type.__name__ = "Integer32"
_Mc2200_ch0Status_Object = MibScalar
mc2200_ch0Status = _Mc2200_ch0Status_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1, 1, 0, 1),
    _Mc2200_ch0Status_Type()
)
mc2200_ch0Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_ch0Status.setStatus("current")


class _Mc2200_ch0LocalConverterNumber_Type(Integer32):
    """Custom type mc2200_ch0LocalConverterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Mc2200_ch0LocalConverterNumber_Type.__name__ = "Integer32"
_Mc2200_ch0LocalConverterNumber_Object = MibScalar
mc2200_ch0LocalConverterNumber = _Mc2200_ch0LocalConverterNumber_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1, 1, 0, 2),
    _Mc2200_ch0LocalConverterNumber_Type()
)
mc2200_ch0LocalConverterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_ch0LocalConverterNumber.setStatus("current")


class _Mc2200_ch0RemoteConverterNumber_Type(Integer32):
    """Custom type mc2200_ch0RemoteConverterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Mc2200_ch0RemoteConverterNumber_Type.__name__ = "Integer32"
_Mc2200_ch0RemoteConverterNumber_Object = MibScalar
mc2200_ch0RemoteConverterNumber = _Mc2200_ch0RemoteConverterNumber_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1, 1, 0, 3),
    _Mc2200_ch0RemoteConverterNumber_Type()
)
mc2200_ch0RemoteConverterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_ch0RemoteConverterNumber.setStatus("current")


class _Mc2200_ch0PowerA_Type(Integer32):
    """Custom type mc2200_ch0PowerA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2),
          ("down", 3))
    )


_Mc2200_ch0PowerA_Type.__name__ = "Integer32"
_Mc2200_ch0PowerA_Object = MibScalar
mc2200_ch0PowerA = _Mc2200_ch0PowerA_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1, 1, 0, 4),
    _Mc2200_ch0PowerA_Type()
)
mc2200_ch0PowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_ch0PowerA.setStatus("current")


class _Mc2200_ch0PowerB_Type(Integer32):
    """Custom type mc2200_ch0PowerB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2),
          ("down", 3))
    )


_Mc2200_ch0PowerB_Type.__name__ = "Integer32"
_Mc2200_ch0PowerB_Object = MibScalar
mc2200_ch0PowerB = _Mc2200_ch0PowerB_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1, 1, 0, 5),
    _Mc2200_ch0PowerB_Type()
)
mc2200_ch0PowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_ch0PowerB.setStatus("current")


class _Mc2200_ch0FanA_Type(Integer32):
    """Custom type mc2200_ch0FanA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("fault", 2))
    )


_Mc2200_ch0FanA_Type.__name__ = "Integer32"
_Mc2200_ch0FanA_Object = MibScalar
mc2200_ch0FanA = _Mc2200_ch0FanA_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1, 1, 0, 6),
    _Mc2200_ch0FanA_Type()
)
mc2200_ch0FanA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_ch0FanA.setStatus("current")


class _Mc2200_ch0FanB_Type(Integer32):
    """Custom type mc2200_ch0FanB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("fault", 2))
    )


_Mc2200_ch0FanB_Type.__name__ = "Integer32"
_Mc2200_ch0FanB_Object = MibScalar
mc2200_ch0FanB = _Mc2200_ch0FanB_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1, 1, 0, 7),
    _Mc2200_ch0FanB_Type()
)
mc2200_ch0FanB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_ch0FanB.setStatus("current")
_Mc2200_ch0HardwareVersion_Type = DisplayString
_Mc2200_ch0HardwareVersion_Object = MibScalar
mc2200_ch0HardwareVersion = _Mc2200_ch0HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1, 1, 0, 8),
    _Mc2200_ch0HardwareVersion_Type()
)
mc2200_ch0HardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_ch0HardwareVersion.setStatus("current")
_Mc2200_ch0Description_Type = DisplayString
_Mc2200_ch0Description_Object = MibScalar
mc2200_ch0Description = _Mc2200_ch0Description_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1, 1, 0, 9),
    _Mc2200_ch0Description_Type()
)
mc2200_ch0Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_ch0Description.setStatus("current")
_Mc2200_ch0AvailableConverterSlots_Type = Integer32
_Mc2200_ch0AvailableConverterSlots_Object = MibScalar
mc2200_ch0AvailableConverterSlots = _Mc2200_ch0AvailableConverterSlots_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1, 1, 0, 10),
    _Mc2200_ch0AvailableConverterSlots_Type()
)
mc2200_ch0AvailableConverterSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_ch0AvailableConverterSlots.setStatus("current")
_Mc2200_ch0OccupiedSlots_Type = Integer32
_Mc2200_ch0OccupiedSlots_Object = MibScalar
mc2200_ch0OccupiedSlots = _Mc2200_ch0OccupiedSlots_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1, 1, 0, 11),
    _Mc2200_ch0OccupiedSlots_Type()
)
mc2200_ch0OccupiedSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_ch0OccupiedSlots.setStatus("current")
_Mc2200_ch0EmptySlots_Type = Integer32
_Mc2200_ch0EmptySlots_Object = MibScalar
mc2200_ch0EmptySlots = _Mc2200_ch0EmptySlots_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 1, 1, 0, 12),
    _Mc2200_ch0EmptySlots_Type()
)
mc2200_ch0EmptySlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_ch0EmptySlots.setStatus("current")
_Mc2200_TrapID_ObjectIdentity = ObjectIdentity
mc2200_TrapID = _Mc2200_TrapID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2)
)
_Mc2200_GEmib_ObjectIdentity = ObjectIdentity
mc2200_GEmib = _Mc2200_GEmib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3)
)
_Mc2200_GEmux8Table_Object = MibTable
mc2200_GEmux8Table = _Mc2200_GEmux8Table_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mc2200_GEmux8Table.setStatus("current")
_Mc2200_GEmux8Entry_Object = MibTableRow
mc2200_GEmux8Entry = _Mc2200_GEmux8Entry_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1)
)
mc2200_GEmux8Entry.setIndexNames(
    (0, "OnAccess2200-MIB", "mc2200-GEmux8CardIndex"),
)
if mibBuilder.loadTexts:
    mc2200_GEmux8Entry.setStatus("current")


class _Mc2200_GEmux8CardIndex_Type(Integer32):
    """Custom type mc2200_GEmux8CardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("card01", 1),
          ("card02", 2),
          ("card03", 3),
          ("card04", 4),
          ("card05", 5),
          ("card06", 6),
          ("card07", 7),
          ("card08", 8),
          ("card09", 9),
          ("card10", 10),
          ("card11", 11),
          ("card12", 12),
          ("card13", 13),
          ("card14", 14),
          ("card15", 15))
    )


_Mc2200_GEmux8CardIndex_Type.__name__ = "Integer32"
_Mc2200_GEmux8CardIndex_Object = MibTableColumn
mc2200_GEmux8CardIndex = _Mc2200_GEmux8CardIndex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 2),
    _Mc2200_GEmux8CardIndex_Type()
)
mc2200_GEmux8CardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8CardIndex.setStatus("current")
_Mc2200_GEmux8LocalLANSFPInfo_Type = DisplayString
_Mc2200_GEmux8LocalLANSFPInfo_Object = MibTableColumn
mc2200_GEmux8LocalLANSFPInfo = _Mc2200_GEmux8LocalLANSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 3),
    _Mc2200_GEmux8LocalLANSFPInfo_Type()
)
mc2200_GEmux8LocalLANSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalLANSFPInfo.setStatus("current")


class _Mc2200_GEmux8LocalLANLink_Type(Integer32):
    """Custom type mc2200_GEmux8LocalLANLink based on Integer32"""
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
          ("active", 3),
          ("standby", 4))
    )


_Mc2200_GEmux8LocalLANLink_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalLANLink_Object = MibTableColumn
mc2200_GEmux8LocalLANLink = _Mc2200_GEmux8LocalLANLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 4),
    _Mc2200_GEmux8LocalLANLink_Type()
)
mc2200_GEmux8LocalLANLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalLANLink.setStatus("mandatory")
_Mc2200_GEmux8LocalWANSFPInfo_Type = DisplayString
_Mc2200_GEmux8LocalWANSFPInfo_Object = MibTableColumn
mc2200_GEmux8LocalWANSFPInfo = _Mc2200_GEmux8LocalWANSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 5),
    _Mc2200_GEmux8LocalWANSFPInfo_Type()
)
mc2200_GEmux8LocalWANSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalWANSFPInfo.setStatus("current")


class _Mc2200_GEmux8LocalWANLink_Type(Integer32):
    """Custom type mc2200_GEmux8LocalWANLink based on Integer32"""
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
          ("active", 3),
          ("standby", 4))
    )


_Mc2200_GEmux8LocalWANLink_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalWANLink_Object = MibTableColumn
mc2200_GEmux8LocalWANLink = _Mc2200_GEmux8LocalWANLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 6),
    _Mc2200_GEmux8LocalWANLink_Type()
)
mc2200_GEmux8LocalWANLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalWANLink.setStatus("current")


class _Mc2200_GEmux8APSActivePort_Type(Integer32):
    """Custom type mc2200_GEmux8APSActivePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("wan", 2)
    )


_Mc2200_GEmux8APSActivePort_Type.__name__ = "Integer32"
_Mc2200_GEmux8APSActivePort_Object = MibTableColumn
mc2200_GEmux8APSActivePort = _Mc2200_GEmux8APSActivePort_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 7),
    _Mc2200_GEmux8APSActivePort_Type()
)
mc2200_GEmux8APSActivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8APSActivePort.setStatus("current")


class _Mc2200_GEmux8LocalPort1Link_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort1Link based on Integer32"""
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


_Mc2200_GEmux8LocalPort1Link_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort1Link_Object = MibTableColumn
mc2200_GEmux8LocalPort1Link = _Mc2200_GEmux8LocalPort1Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 8),
    _Mc2200_GEmux8LocalPort1Link_Type()
)
mc2200_GEmux8LocalPort1Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort1Link.setStatus("current")


class _Mc2200_GEmux8LocalPort1Speed_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort1Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed100M", 1),
          ("speed10M", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8LocalPort1Speed_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort1Speed_Object = MibTableColumn
mc2200_GEmux8LocalPort1Speed = _Mc2200_GEmux8LocalPort1Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 9),
    _Mc2200_GEmux8LocalPort1Speed_Type()
)
mc2200_GEmux8LocalPort1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort1Speed.setStatus("current")


class _Mc2200_GEmux8LocalPort1Duplex_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort1Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8LocalPort1Duplex_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort1Duplex_Object = MibTableColumn
mc2200_GEmux8LocalPort1Duplex = _Mc2200_GEmux8LocalPort1Duplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 10),
    _Mc2200_GEmux8LocalPort1Duplex_Type()
)
mc2200_GEmux8LocalPort1Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort1Duplex.setStatus("current")


class _Mc2200_GEmux8LocalPort1TxRate_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort1TxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GEmux8LocalPort1TxRate_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort1TxRate_Object = MibTableColumn
mc2200_GEmux8LocalPort1TxRate = _Mc2200_GEmux8LocalPort1TxRate_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 11),
    _Mc2200_GEmux8LocalPort1TxRate_Type()
)
mc2200_GEmux8LocalPort1TxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort1TxRate.setStatus("current")


class _Mc2200_GEmux8LocalPort1RxRate_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort1RxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GEmux8LocalPort1RxRate_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort1RxRate_Object = MibTableColumn
mc2200_GEmux8LocalPort1RxRate = _Mc2200_GEmux8LocalPort1RxRate_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 12),
    _Mc2200_GEmux8LocalPort1RxRate_Type()
)
mc2200_GEmux8LocalPort1RxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort1RxRate.setStatus("current")


class _Mc2200_GEmux8LocalPort1Mode_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort1Mode based on Integer32"""
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
        *(("auto", 1),
          ("mode10MHALFDUPLEX", 2),
          ("mode10MFULLDUPLEX", 3),
          ("mode100MHALFDUPLEX", 4),
          ("mode100MFULLDUPLEX", 5))
    )


_Mc2200_GEmux8LocalPort1Mode_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort1Mode_Object = MibTableColumn
mc2200_GEmux8LocalPort1Mode = _Mc2200_GEmux8LocalPort1Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 13),
    _Mc2200_GEmux8LocalPort1Mode_Type()
)
mc2200_GEmux8LocalPort1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort1Mode.setStatus("current")


class _Mc2200_GEmux8LocalPort1MDIX_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort1MDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("mdi", 2),
          ("mdi-x", 3))
    )


_Mc2200_GEmux8LocalPort1MDIX_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort1MDIX_Object = MibTableColumn
mc2200_GEmux8LocalPort1MDIX = _Mc2200_GEmux8LocalPort1MDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 14),
    _Mc2200_GEmux8LocalPort1MDIX_Type()
)
mc2200_GEmux8LocalPort1MDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort1MDIX.setStatus("current")


class _Mc2200_GEmux8LocalPort2Link_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort2Link based on Integer32"""
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


_Mc2200_GEmux8LocalPort2Link_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort2Link_Object = MibTableColumn
mc2200_GEmux8LocalPort2Link = _Mc2200_GEmux8LocalPort2Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 15),
    _Mc2200_GEmux8LocalPort2Link_Type()
)
mc2200_GEmux8LocalPort2Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort2Link.setStatus("current")


class _Mc2200_GEmux8LocalPort2Speed_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort2Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed100M", 1),
          ("speed10M", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8LocalPort2Speed_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort2Speed_Object = MibTableColumn
mc2200_GEmux8LocalPort2Speed = _Mc2200_GEmux8LocalPort2Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 16),
    _Mc2200_GEmux8LocalPort2Speed_Type()
)
mc2200_GEmux8LocalPort2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort2Speed.setStatus("current")


class _Mc2200_GEmux8LocalPort2Duplex_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort2Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8LocalPort2Duplex_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort2Duplex_Object = MibTableColumn
mc2200_GEmux8LocalPort2Duplex = _Mc2200_GEmux8LocalPort2Duplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 17),
    _Mc2200_GEmux8LocalPort2Duplex_Type()
)
mc2200_GEmux8LocalPort2Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort2Duplex.setStatus("current")


class _Mc2200_GEmux8LocalPort2TxRate_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort2TxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GEmux8LocalPort2TxRate_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort2TxRate_Object = MibTableColumn
mc2200_GEmux8LocalPort2TxRate = _Mc2200_GEmux8LocalPort2TxRate_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 18),
    _Mc2200_GEmux8LocalPort2TxRate_Type()
)
mc2200_GEmux8LocalPort2TxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort2TxRate.setStatus("current")


class _Mc2200_GEmux8LocalPort2RxRate_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort2RxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GEmux8LocalPort2RxRate_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort2RxRate_Object = MibTableColumn
mc2200_GEmux8LocalPort2RxRate = _Mc2200_GEmux8LocalPort2RxRate_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 19),
    _Mc2200_GEmux8LocalPort2RxRate_Type()
)
mc2200_GEmux8LocalPort2RxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort2RxRate.setStatus("current")


class _Mc2200_GEmux8LocalPort2Mode_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort2Mode based on Integer32"""
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
        *(("auto", 1),
          ("mode10MHALFDUPLEX", 2),
          ("mode10MFULLDUPLEX", 3),
          ("mode100MHALFDUPLEX", 4),
          ("mode100MFULLDUPLEX", 5))
    )


_Mc2200_GEmux8LocalPort2Mode_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort2Mode_Object = MibTableColumn
mc2200_GEmux8LocalPort2Mode = _Mc2200_GEmux8LocalPort2Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 20),
    _Mc2200_GEmux8LocalPort2Mode_Type()
)
mc2200_GEmux8LocalPort2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort2Mode.setStatus("current")


class _Mc2200_GEmux8LocalPort2MDIX_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort2MDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("mdi", 2),
          ("mdi-x", 3))
    )


_Mc2200_GEmux8LocalPort2MDIX_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort2MDIX_Object = MibTableColumn
mc2200_GEmux8LocalPort2MDIX = _Mc2200_GEmux8LocalPort2MDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 21),
    _Mc2200_GEmux8LocalPort2MDIX_Type()
)
mc2200_GEmux8LocalPort2MDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort2MDIX.setStatus("current")


class _Mc2200_GEmux8LocalPort3Link_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort3Link based on Integer32"""
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


_Mc2200_GEmux8LocalPort3Link_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort3Link_Object = MibTableColumn
mc2200_GEmux8LocalPort3Link = _Mc2200_GEmux8LocalPort3Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 22),
    _Mc2200_GEmux8LocalPort3Link_Type()
)
mc2200_GEmux8LocalPort3Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort3Link.setStatus("current")


class _Mc2200_GEmux8LocalPort3Speed_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort3Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed100M", 1),
          ("speed10M", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8LocalPort3Speed_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort3Speed_Object = MibTableColumn
mc2200_GEmux8LocalPort3Speed = _Mc2200_GEmux8LocalPort3Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 23),
    _Mc2200_GEmux8LocalPort3Speed_Type()
)
mc2200_GEmux8LocalPort3Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort3Speed.setStatus("current")


class _Mc2200_GEmux8LocalPort3Duplex_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort3Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8LocalPort3Duplex_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort3Duplex_Object = MibTableColumn
mc2200_GEmux8LocalPort3Duplex = _Mc2200_GEmux8LocalPort3Duplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 24),
    _Mc2200_GEmux8LocalPort3Duplex_Type()
)
mc2200_GEmux8LocalPort3Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort3Duplex.setStatus("current")


class _Mc2200_GEmux8LocalPort3TxRate_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort3TxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GEmux8LocalPort3TxRate_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort3TxRate_Object = MibTableColumn
mc2200_GEmux8LocalPort3TxRate = _Mc2200_GEmux8LocalPort3TxRate_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 25),
    _Mc2200_GEmux8LocalPort3TxRate_Type()
)
mc2200_GEmux8LocalPort3TxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort3TxRate.setStatus("current")


class _Mc2200_GEmux8LocalPort3RxRate_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort3RxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GEmux8LocalPort3RxRate_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort3RxRate_Object = MibTableColumn
mc2200_GEmux8LocalPort3RxRate = _Mc2200_GEmux8LocalPort3RxRate_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 26),
    _Mc2200_GEmux8LocalPort3RxRate_Type()
)
mc2200_GEmux8LocalPort3RxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort3RxRate.setStatus("current")


class _Mc2200_GEmux8LocalPort3Mode_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort3Mode based on Integer32"""
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
        *(("auto", 1),
          ("mode10MHALFDUPLEX", 2),
          ("mode10MFULLDUPLEX", 3),
          ("mode100MHALFDUPLEX", 4),
          ("mode100MFULLDUPLEX", 5))
    )


_Mc2200_GEmux8LocalPort3Mode_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort3Mode_Object = MibTableColumn
mc2200_GEmux8LocalPort3Mode = _Mc2200_GEmux8LocalPort3Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 27),
    _Mc2200_GEmux8LocalPort3Mode_Type()
)
mc2200_GEmux8LocalPort3Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort3Mode.setStatus("current")


class _Mc2200_GEmux8LocalPort3MDIX_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort3MDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("mdi", 2),
          ("mdi-x", 3))
    )


_Mc2200_GEmux8LocalPort3MDIX_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort3MDIX_Object = MibTableColumn
mc2200_GEmux8LocalPort3MDIX = _Mc2200_GEmux8LocalPort3MDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 28),
    _Mc2200_GEmux8LocalPort3MDIX_Type()
)
mc2200_GEmux8LocalPort3MDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort3MDIX.setStatus("current")


class _Mc2200_GEmux8LocalPort4Link_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort4Link based on Integer32"""
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


_Mc2200_GEmux8LocalPort4Link_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort4Link_Object = MibTableColumn
mc2200_GEmux8LocalPort4Link = _Mc2200_GEmux8LocalPort4Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 29),
    _Mc2200_GEmux8LocalPort4Link_Type()
)
mc2200_GEmux8LocalPort4Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort4Link.setStatus("current")


class _Mc2200_GEmux8LocalPort4Speed_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort4Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed100M", 1),
          ("speed10M", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8LocalPort4Speed_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort4Speed_Object = MibTableColumn
mc2200_GEmux8LocalPort4Speed = _Mc2200_GEmux8LocalPort4Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 30),
    _Mc2200_GEmux8LocalPort4Speed_Type()
)
mc2200_GEmux8LocalPort4Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort4Speed.setStatus("current")


class _Mc2200_GEmux8LocalPort4Duplex_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort4Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8LocalPort4Duplex_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort4Duplex_Object = MibTableColumn
mc2200_GEmux8LocalPort4Duplex = _Mc2200_GEmux8LocalPort4Duplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 31),
    _Mc2200_GEmux8LocalPort4Duplex_Type()
)
mc2200_GEmux8LocalPort4Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort4Duplex.setStatus("current")


class _Mc2200_GEmux8LocalPort4TxRate_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort4TxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GEmux8LocalPort4TxRate_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort4TxRate_Object = MibTableColumn
mc2200_GEmux8LocalPort4TxRate = _Mc2200_GEmux8LocalPort4TxRate_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 32),
    _Mc2200_GEmux8LocalPort4TxRate_Type()
)
mc2200_GEmux8LocalPort4TxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort4TxRate.setStatus("current")


class _Mc2200_GEmux8LocalPort4RxRate_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort4RxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GEmux8LocalPort4RxRate_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort4RxRate_Object = MibTableColumn
mc2200_GEmux8LocalPort4RxRate = _Mc2200_GEmux8LocalPort4RxRate_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 33),
    _Mc2200_GEmux8LocalPort4RxRate_Type()
)
mc2200_GEmux8LocalPort4RxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort4RxRate.setStatus("current")


class _Mc2200_GEmux8LocalPort4Mode_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort4Mode based on Integer32"""
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
        *(("auto", 1),
          ("mode10MHALFDUPLEX", 2),
          ("mode10MFULLDUPLEX", 3),
          ("mode100MHALFDUPLEX", 4),
          ("mode100MFULLDUPLEX", 5))
    )


_Mc2200_GEmux8LocalPort4Mode_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort4Mode_Object = MibTableColumn
mc2200_GEmux8LocalPort4Mode = _Mc2200_GEmux8LocalPort4Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 34),
    _Mc2200_GEmux8LocalPort4Mode_Type()
)
mc2200_GEmux8LocalPort4Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort4Mode.setStatus("current")


class _Mc2200_GEmux8LocalPort4MDIX_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort4MDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("mdi", 2),
          ("mdi-x", 3))
    )


_Mc2200_GEmux8LocalPort4MDIX_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort4MDIX_Object = MibTableColumn
mc2200_GEmux8LocalPort4MDIX = _Mc2200_GEmux8LocalPort4MDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 35),
    _Mc2200_GEmux8LocalPort4MDIX_Type()
)
mc2200_GEmux8LocalPort4MDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort4MDIX.setStatus("current")


class _Mc2200_GEmux8LocalPort5Link_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort5Link based on Integer32"""
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


_Mc2200_GEmux8LocalPort5Link_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort5Link_Object = MibTableColumn
mc2200_GEmux8LocalPort5Link = _Mc2200_GEmux8LocalPort5Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 36),
    _Mc2200_GEmux8LocalPort5Link_Type()
)
mc2200_GEmux8LocalPort5Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort5Link.setStatus("current")


class _Mc2200_GEmux8LocalPort5Speed_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort5Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed100M", 1),
          ("speed10M", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8LocalPort5Speed_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort5Speed_Object = MibTableColumn
mc2200_GEmux8LocalPort5Speed = _Mc2200_GEmux8LocalPort5Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 37),
    _Mc2200_GEmux8LocalPort5Speed_Type()
)
mc2200_GEmux8LocalPort5Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort5Speed.setStatus("current")


class _Mc2200_GEmux8LocalPort5Duplex_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort5Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8LocalPort5Duplex_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort5Duplex_Object = MibTableColumn
mc2200_GEmux8LocalPort5Duplex = _Mc2200_GEmux8LocalPort5Duplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 38),
    _Mc2200_GEmux8LocalPort5Duplex_Type()
)
mc2200_GEmux8LocalPort5Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort5Duplex.setStatus("current")


class _Mc2200_GEmux8LocalPort5TxRate_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort5TxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GEmux8LocalPort5TxRate_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort5TxRate_Object = MibTableColumn
mc2200_GEmux8LocalPort5TxRate = _Mc2200_GEmux8LocalPort5TxRate_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 39),
    _Mc2200_GEmux8LocalPort5TxRate_Type()
)
mc2200_GEmux8LocalPort5TxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort5TxRate.setStatus("current")


class _Mc2200_GEmux8LocalPort5RxRate_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort5RxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GEmux8LocalPort5RxRate_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort5RxRate_Object = MibTableColumn
mc2200_GEmux8LocalPort5RxRate = _Mc2200_GEmux8LocalPort5RxRate_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 40),
    _Mc2200_GEmux8LocalPort5RxRate_Type()
)
mc2200_GEmux8LocalPort5RxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort5RxRate.setStatus("current")


class _Mc2200_GEmux8LocalPort5Mode_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort5Mode based on Integer32"""
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
        *(("auto", 1),
          ("mode10MHALFDUPLEX", 2),
          ("mode10MFULLDUPLEX", 3),
          ("mode100MHALFDUPLEX", 4),
          ("mode100MFULLDUPLEX", 5))
    )


_Mc2200_GEmux8LocalPort5Mode_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort5Mode_Object = MibTableColumn
mc2200_GEmux8LocalPort5Mode = _Mc2200_GEmux8LocalPort5Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 41),
    _Mc2200_GEmux8LocalPort5Mode_Type()
)
mc2200_GEmux8LocalPort5Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort5Mode.setStatus("current")


class _Mc2200_GEmux8LocalPort5MDIX_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort5MDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("mdi", 2),
          ("mdi-x", 3))
    )


_Mc2200_GEmux8LocalPort5MDIX_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort5MDIX_Object = MibTableColumn
mc2200_GEmux8LocalPort5MDIX = _Mc2200_GEmux8LocalPort5MDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 42),
    _Mc2200_GEmux8LocalPort5MDIX_Type()
)
mc2200_GEmux8LocalPort5MDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort5MDIX.setStatus("current")


class _Mc2200_GEmux8LocalPort6Link_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort6Link based on Integer32"""
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


_Mc2200_GEmux8LocalPort6Link_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort6Link_Object = MibTableColumn
mc2200_GEmux8LocalPort6Link = _Mc2200_GEmux8LocalPort6Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 43),
    _Mc2200_GEmux8LocalPort6Link_Type()
)
mc2200_GEmux8LocalPort6Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort6Link.setStatus("current")


class _Mc2200_GEmux8LocalPort6Speed_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort6Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed100M", 1),
          ("speed10M", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8LocalPort6Speed_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort6Speed_Object = MibTableColumn
mc2200_GEmux8LocalPort6Speed = _Mc2200_GEmux8LocalPort6Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 44),
    _Mc2200_GEmux8LocalPort6Speed_Type()
)
mc2200_GEmux8LocalPort6Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort6Speed.setStatus("current")


class _Mc2200_GEmux8LocalPort6Duplex_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort6Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8LocalPort6Duplex_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort6Duplex_Object = MibTableColumn
mc2200_GEmux8LocalPort6Duplex = _Mc2200_GEmux8LocalPort6Duplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 45),
    _Mc2200_GEmux8LocalPort6Duplex_Type()
)
mc2200_GEmux8LocalPort6Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort6Duplex.setStatus("current")


class _Mc2200_GEmux8LocalPort6TxRate_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort6TxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GEmux8LocalPort6TxRate_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort6TxRate_Object = MibTableColumn
mc2200_GEmux8LocalPort6TxRate = _Mc2200_GEmux8LocalPort6TxRate_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 46),
    _Mc2200_GEmux8LocalPort6TxRate_Type()
)
mc2200_GEmux8LocalPort6TxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort6TxRate.setStatus("current")


class _Mc2200_GEmux8LocalPort6RxRate_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort6RxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GEmux8LocalPort6RxRate_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort6RxRate_Object = MibTableColumn
mc2200_GEmux8LocalPort6RxRate = _Mc2200_GEmux8LocalPort6RxRate_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 47),
    _Mc2200_GEmux8LocalPort6RxRate_Type()
)
mc2200_GEmux8LocalPort6RxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort6RxRate.setStatus("current")


class _Mc2200_GEmux8LocalPort6Mode_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort6Mode based on Integer32"""
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
        *(("auto", 1),
          ("mode10MHALFDUPLEX", 2),
          ("mode10MFULLDUPLEX", 3),
          ("mode100MHALFDUPLEX", 4),
          ("mode100MFULLDUPLEX", 5))
    )


_Mc2200_GEmux8LocalPort6Mode_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort6Mode_Object = MibTableColumn
mc2200_GEmux8LocalPort6Mode = _Mc2200_GEmux8LocalPort6Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 48),
    _Mc2200_GEmux8LocalPort6Mode_Type()
)
mc2200_GEmux8LocalPort6Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort6Mode.setStatus("current")


class _Mc2200_GEmux8LocalPort6MDIX_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort6MDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("mdi", 2),
          ("mdi-x", 3))
    )


_Mc2200_GEmux8LocalPort6MDIX_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort6MDIX_Object = MibTableColumn
mc2200_GEmux8LocalPort6MDIX = _Mc2200_GEmux8LocalPort6MDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 49),
    _Mc2200_GEmux8LocalPort6MDIX_Type()
)
mc2200_GEmux8LocalPort6MDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort6MDIX.setStatus("current")


class _Mc2200_GEmux8LocalPort7Link_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort7Link based on Integer32"""
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


_Mc2200_GEmux8LocalPort7Link_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort7Link_Object = MibTableColumn
mc2200_GEmux8LocalPort7Link = _Mc2200_GEmux8LocalPort7Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 50),
    _Mc2200_GEmux8LocalPort7Link_Type()
)
mc2200_GEmux8LocalPort7Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort7Link.setStatus("current")


class _Mc2200_GEmux8LocalPort7Speed_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort7Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed100M", 1),
          ("speed10M", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8LocalPort7Speed_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort7Speed_Object = MibTableColumn
mc2200_GEmux8LocalPort7Speed = _Mc2200_GEmux8LocalPort7Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 51),
    _Mc2200_GEmux8LocalPort7Speed_Type()
)
mc2200_GEmux8LocalPort7Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort7Speed.setStatus("current")


class _Mc2200_GEmux8LocalPort7Duplex_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort7Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8LocalPort7Duplex_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort7Duplex_Object = MibTableColumn
mc2200_GEmux8LocalPort7Duplex = _Mc2200_GEmux8LocalPort7Duplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 52),
    _Mc2200_GEmux8LocalPort7Duplex_Type()
)
mc2200_GEmux8LocalPort7Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort7Duplex.setStatus("current")


class _Mc2200_GEmux8LocalPort7TxRate_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort7TxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GEmux8LocalPort7TxRate_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort7TxRate_Object = MibTableColumn
mc2200_GEmux8LocalPort7TxRate = _Mc2200_GEmux8LocalPort7TxRate_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 53),
    _Mc2200_GEmux8LocalPort7TxRate_Type()
)
mc2200_GEmux8LocalPort7TxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort7TxRate.setStatus("current")


class _Mc2200_GEmux8LocalPort7RxRate_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort7RxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GEmux8LocalPort7RxRate_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort7RxRate_Object = MibTableColumn
mc2200_GEmux8LocalPort7RxRate = _Mc2200_GEmux8LocalPort7RxRate_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 54),
    _Mc2200_GEmux8LocalPort7RxRate_Type()
)
mc2200_GEmux8LocalPort7RxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort7RxRate.setStatus("current")


class _Mc2200_GEmux8LocalPort7Mode_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort7Mode based on Integer32"""
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
        *(("auto", 1),
          ("speed10MHALFDUPLEX", 2),
          ("speed10MFULLDUPLEX", 3),
          ("speed100MHALFDUPLEX", 4),
          ("speed100MFULLDUPLEX", 5))
    )


_Mc2200_GEmux8LocalPort7Mode_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort7Mode_Object = MibTableColumn
mc2200_GEmux8LocalPort7Mode = _Mc2200_GEmux8LocalPort7Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 55),
    _Mc2200_GEmux8LocalPort7Mode_Type()
)
mc2200_GEmux8LocalPort7Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort7Mode.setStatus("current")


class _Mc2200_GEmux8LocalPort7MDIX_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort7MDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("mdi", 2),
          ("mdi-x", 3))
    )


_Mc2200_GEmux8LocalPort7MDIX_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort7MDIX_Object = MibTableColumn
mc2200_GEmux8LocalPort7MDIX = _Mc2200_GEmux8LocalPort7MDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 56),
    _Mc2200_GEmux8LocalPort7MDIX_Type()
)
mc2200_GEmux8LocalPort7MDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort7MDIX.setStatus("current")


class _Mc2200_GEmux8LocalPort8Link_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort8Link based on Integer32"""
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


_Mc2200_GEmux8LocalPort8Link_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort8Link_Object = MibTableColumn
mc2200_GEmux8LocalPort8Link = _Mc2200_GEmux8LocalPort8Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 57),
    _Mc2200_GEmux8LocalPort8Link_Type()
)
mc2200_GEmux8LocalPort8Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort8Link.setStatus("current")


class _Mc2200_GEmux8LocalPort8Speed_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort8Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed100M", 1),
          ("speed10M", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8LocalPort8Speed_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort8Speed_Object = MibTableColumn
mc2200_GEmux8LocalPort8Speed = _Mc2200_GEmux8LocalPort8Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 58),
    _Mc2200_GEmux8LocalPort8Speed_Type()
)
mc2200_GEmux8LocalPort8Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort8Speed.setStatus("current")


class _Mc2200_GEmux8LocalPort8Duplex_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort8Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8LocalPort8Duplex_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort8Duplex_Object = MibTableColumn
mc2200_GEmux8LocalPort8Duplex = _Mc2200_GEmux8LocalPort8Duplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 59),
    _Mc2200_GEmux8LocalPort8Duplex_Type()
)
mc2200_GEmux8LocalPort8Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort8Duplex.setStatus("current")


class _Mc2200_GEmux8LocalPort8TxRate_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort8TxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GEmux8LocalPort8TxRate_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort8TxRate_Object = MibTableColumn
mc2200_GEmux8LocalPort8TxRate = _Mc2200_GEmux8LocalPort8TxRate_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 60),
    _Mc2200_GEmux8LocalPort8TxRate_Type()
)
mc2200_GEmux8LocalPort8TxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort8TxRate.setStatus("current")


class _Mc2200_GEmux8LocalPort8RxRate_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort8RxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GEmux8LocalPort8RxRate_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort8RxRate_Object = MibTableColumn
mc2200_GEmux8LocalPort8RxRate = _Mc2200_GEmux8LocalPort8RxRate_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 61),
    _Mc2200_GEmux8LocalPort8RxRate_Type()
)
mc2200_GEmux8LocalPort8RxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort8RxRate.setStatus("current")


class _Mc2200_GEmux8LocalPort8Mode_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort8Mode based on Integer32"""
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
        *(("auto", 1),
          ("mode10MHALFDUPLEX", 2),
          ("mode10MFULLDUPLEX", 3),
          ("mode100MHALFDUPLEX", 4),
          ("mode100MFULLDUPLEX", 5))
    )


_Mc2200_GEmux8LocalPort8Mode_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort8Mode_Object = MibTableColumn
mc2200_GEmux8LocalPort8Mode = _Mc2200_GEmux8LocalPort8Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 62),
    _Mc2200_GEmux8LocalPort8Mode_Type()
)
mc2200_GEmux8LocalPort8Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort8Mode.setStatus("current")


class _Mc2200_GEmux8LocalPort8MDIX_Type(Integer32):
    """Custom type mc2200_GEmux8LocalPort8MDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("mdi", 2),
          ("mdi-x", 3))
    )


_Mc2200_GEmux8LocalPort8MDIX_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalPort8MDIX_Object = MibTableColumn
mc2200_GEmux8LocalPort8MDIX = _Mc2200_GEmux8LocalPort8MDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 63),
    _Mc2200_GEmux8LocalPort8MDIX_Type()
)
mc2200_GEmux8LocalPort8MDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalPort8MDIX.setStatus("current")
_Mc2200_GEmux8MibPort1RxGoodOctets_Type = Counter64
_Mc2200_GEmux8MibPort1RxGoodOctets_Object = MibTableColumn
mc2200_GEmux8MibPort1RxGoodOctets = _Mc2200_GEmux8MibPort1RxGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 64),
    _Mc2200_GEmux8MibPort1RxGoodOctets_Type()
)
mc2200_GEmux8MibPort1RxGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8MibPort1RxGoodOctets.setStatus("current")
_Mc2200_GEmux8MibPort1RxFCSErr_Type = Counter64
_Mc2200_GEmux8MibPort1RxFCSErr_Object = MibTableColumn
mc2200_GEmux8MibPort1RxFCSErr = _Mc2200_GEmux8MibPort1RxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 66),
    _Mc2200_GEmux8MibPort1RxFCSErr_Type()
)
mc2200_GEmux8MibPort1RxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8MibPort1RxFCSErr.setStatus("current")
_Mc2200_GEmux8MibPort1TxFCSErr_Type = Counter64
_Mc2200_GEmux8MibPort1TxFCSErr_Object = MibTableColumn
mc2200_GEmux8MibPort1TxFCSErr = _Mc2200_GEmux8MibPort1TxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 67),
    _Mc2200_GEmux8MibPort1TxFCSErr_Type()
)
mc2200_GEmux8MibPort1TxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8MibPort1TxFCSErr.setStatus("current")
_Mc2200_GEmux8MibPort2RxGoodOctets_Type = Counter64
_Mc2200_GEmux8MibPort2RxGoodOctets_Object = MibTableColumn
mc2200_GEmux8MibPort2RxGoodOctets = _Mc2200_GEmux8MibPort2RxGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 68),
    _Mc2200_GEmux8MibPort2RxGoodOctets_Type()
)
mc2200_GEmux8MibPort2RxGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8MibPort2RxGoodOctets.setStatus("current")
_Mc2200_GEmux8MibPort2RxFCSErr_Type = Counter64
_Mc2200_GEmux8MibPort2RxFCSErr_Object = MibTableColumn
mc2200_GEmux8MibPort2RxFCSErr = _Mc2200_GEmux8MibPort2RxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 70),
    _Mc2200_GEmux8MibPort2RxFCSErr_Type()
)
mc2200_GEmux8MibPort2RxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8MibPort2RxFCSErr.setStatus("current")
_Mc2200_GEmux8MibPort2TxFCSErr_Type = Counter64
_Mc2200_GEmux8MibPort2TxFCSErr_Object = MibTableColumn
mc2200_GEmux8MibPort2TxFCSErr = _Mc2200_GEmux8MibPort2TxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 71),
    _Mc2200_GEmux8MibPort2TxFCSErr_Type()
)
mc2200_GEmux8MibPort2TxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8MibPort2TxFCSErr.setStatus("current")
_Mc2200_GEmux8MibPort3RxGoodOctets_Type = Counter64
_Mc2200_GEmux8MibPort3RxGoodOctets_Object = MibTableColumn
mc2200_GEmux8MibPort3RxGoodOctets = _Mc2200_GEmux8MibPort3RxGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 72),
    _Mc2200_GEmux8MibPort3RxGoodOctets_Type()
)
mc2200_GEmux8MibPort3RxGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8MibPort3RxGoodOctets.setStatus("current")
_Mc2200_GEmux8MibPort3RxFCSErr_Type = Counter64
_Mc2200_GEmux8MibPort3RxFCSErr_Object = MibTableColumn
mc2200_GEmux8MibPort3RxFCSErr = _Mc2200_GEmux8MibPort3RxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 74),
    _Mc2200_GEmux8MibPort3RxFCSErr_Type()
)
mc2200_GEmux8MibPort3RxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8MibPort3RxFCSErr.setStatus("current")
_Mc2200_GEmux8MibPort3TxFCSErr_Type = Counter64
_Mc2200_GEmux8MibPort3TxFCSErr_Object = MibTableColumn
mc2200_GEmux8MibPort3TxFCSErr = _Mc2200_GEmux8MibPort3TxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 75),
    _Mc2200_GEmux8MibPort3TxFCSErr_Type()
)
mc2200_GEmux8MibPort3TxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8MibPort3TxFCSErr.setStatus("current")
_Mc2200_GEmux8MibPort4RxGoodOctets_Type = Counter64
_Mc2200_GEmux8MibPort4RxGoodOctets_Object = MibTableColumn
mc2200_GEmux8MibPort4RxGoodOctets = _Mc2200_GEmux8MibPort4RxGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 76),
    _Mc2200_GEmux8MibPort4RxGoodOctets_Type()
)
mc2200_GEmux8MibPort4RxGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8MibPort4RxGoodOctets.setStatus("current")
_Mc2200_GEmux8MibPort4RxFCSErr_Type = Counter64
_Mc2200_GEmux8MibPort4RxFCSErr_Object = MibTableColumn
mc2200_GEmux8MibPort4RxFCSErr = _Mc2200_GEmux8MibPort4RxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 78),
    _Mc2200_GEmux8MibPort4RxFCSErr_Type()
)
mc2200_GEmux8MibPort4RxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8MibPort4RxFCSErr.setStatus("current")
_Mc2200_GEmux8MibPort4TxFCSErr_Type = Counter64
_Mc2200_GEmux8MibPort4TxFCSErr_Object = MibTableColumn
mc2200_GEmux8MibPort4TxFCSErr = _Mc2200_GEmux8MibPort4TxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 79),
    _Mc2200_GEmux8MibPort4TxFCSErr_Type()
)
mc2200_GEmux8MibPort4TxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8MibPort4TxFCSErr.setStatus("current")
_Mc2200_GEmux8MibPort5RxGoodOctets_Type = Counter64
_Mc2200_GEmux8MibPort5RxGoodOctets_Object = MibTableColumn
mc2200_GEmux8MibPort5RxGoodOctets = _Mc2200_GEmux8MibPort5RxGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 80),
    _Mc2200_GEmux8MibPort5RxGoodOctets_Type()
)
mc2200_GEmux8MibPort5RxGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8MibPort5RxGoodOctets.setStatus("current")
_Mc2200_GEmux8MibPort5RxFCSErr_Type = Counter64
_Mc2200_GEmux8MibPort5RxFCSErr_Object = MibTableColumn
mc2200_GEmux8MibPort5RxFCSErr = _Mc2200_GEmux8MibPort5RxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 82),
    _Mc2200_GEmux8MibPort5RxFCSErr_Type()
)
mc2200_GEmux8MibPort5RxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8MibPort5RxFCSErr.setStatus("current")
_Mc2200_GEmux8MibPort5TxFCSErr_Type = Counter64
_Mc2200_GEmux8MibPort5TxFCSErr_Object = MibTableColumn
mc2200_GEmux8MibPort5TxFCSErr = _Mc2200_GEmux8MibPort5TxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 83),
    _Mc2200_GEmux8MibPort5TxFCSErr_Type()
)
mc2200_GEmux8MibPort5TxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8MibPort5TxFCSErr.setStatus("current")
_Mc2200_GEmux8MibPort6RxGoodOctets_Type = Counter64
_Mc2200_GEmux8MibPort6RxGoodOctets_Object = MibTableColumn
mc2200_GEmux8MibPort6RxGoodOctets = _Mc2200_GEmux8MibPort6RxGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 84),
    _Mc2200_GEmux8MibPort6RxGoodOctets_Type()
)
mc2200_GEmux8MibPort6RxGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8MibPort6RxGoodOctets.setStatus("current")
_Mc2200_GEmux8MibPort6RxFCSErr_Type = Counter64
_Mc2200_GEmux8MibPort6RxFCSErr_Object = MibTableColumn
mc2200_GEmux8MibPort6RxFCSErr = _Mc2200_GEmux8MibPort6RxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 86),
    _Mc2200_GEmux8MibPort6RxFCSErr_Type()
)
mc2200_GEmux8MibPort6RxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8MibPort6RxFCSErr.setStatus("current")
_Mc2200_GEmux8MibPort6TxFCSErr_Type = Counter64
_Mc2200_GEmux8MibPort6TxFCSErr_Object = MibTableColumn
mc2200_GEmux8MibPort6TxFCSErr = _Mc2200_GEmux8MibPort6TxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 87),
    _Mc2200_GEmux8MibPort6TxFCSErr_Type()
)
mc2200_GEmux8MibPort6TxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8MibPort6TxFCSErr.setStatus("current")
_Mc2200_GEmux8MibPort7RxGoodOctets_Type = Counter64
_Mc2200_GEmux8MibPort7RxGoodOctets_Object = MibTableColumn
mc2200_GEmux8MibPort7RxGoodOctets = _Mc2200_GEmux8MibPort7RxGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 88),
    _Mc2200_GEmux8MibPort7RxGoodOctets_Type()
)
mc2200_GEmux8MibPort7RxGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8MibPort7RxGoodOctets.setStatus("current")
_Mc2200_GEmux8MibPort7RxFCSErr_Type = Counter64
_Mc2200_GEmux8MibPort7RxFCSErr_Object = MibTableColumn
mc2200_GEmux8MibPort7RxFCSErr = _Mc2200_GEmux8MibPort7RxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 90),
    _Mc2200_GEmux8MibPort7RxFCSErr_Type()
)
mc2200_GEmux8MibPort7RxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8MibPort7RxFCSErr.setStatus("current")
_Mc2200_GEmux8MibPort7TxFCSErr_Type = Counter64
_Mc2200_GEmux8MibPort7TxFCSErr_Object = MibTableColumn
mc2200_GEmux8MibPort7TxFCSErr = _Mc2200_GEmux8MibPort7TxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 91),
    _Mc2200_GEmux8MibPort7TxFCSErr_Type()
)
mc2200_GEmux8MibPort7TxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8MibPort7TxFCSErr.setStatus("current")
_Mc2200_GEmux8MibPort8RxGoodOctets_Type = Counter64
_Mc2200_GEmux8MibPort8RxGoodOctets_Object = MibTableColumn
mc2200_GEmux8MibPort8RxGoodOctets = _Mc2200_GEmux8MibPort8RxGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 92),
    _Mc2200_GEmux8MibPort8RxGoodOctets_Type()
)
mc2200_GEmux8MibPort8RxGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8MibPort8RxGoodOctets.setStatus("current")
_Mc2200_GEmux8MibPort8RxFCSErr_Type = Counter64
_Mc2200_GEmux8MibPort8RxFCSErr_Object = MibTableColumn
mc2200_GEmux8MibPort8RxFCSErr = _Mc2200_GEmux8MibPort8RxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 94),
    _Mc2200_GEmux8MibPort8RxFCSErr_Type()
)
mc2200_GEmux8MibPort8RxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8MibPort8RxFCSErr.setStatus("current")
_Mc2200_GEmux8MibPort8TxFCSErr_Type = Counter64
_Mc2200_GEmux8MibPort8TxFCSErr_Object = MibTableColumn
mc2200_GEmux8MibPort8TxFCSErr = _Mc2200_GEmux8MibPort8TxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 95),
    _Mc2200_GEmux8MibPort8TxFCSErr_Type()
)
mc2200_GEmux8MibPort8TxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8MibPort8TxFCSErr.setStatus("current")
_Mc2200_GEmux8RemoteLANSFPInfo_Type = DisplayString
_Mc2200_GEmux8RemoteLANSFPInfo_Object = MibTableColumn
mc2200_GEmux8RemoteLANSFPInfo = _Mc2200_GEmux8RemoteLANSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 96),
    _Mc2200_GEmux8RemoteLANSFPInfo_Type()
)
mc2200_GEmux8RemoteLANSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemoteLANSFPInfo.setStatus("current")


class _Mc2200_GEmux8RemoteLANLink_Type(Integer32):
    """Custom type mc2200_GEmux8RemoteLANLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2),
          ("active", 3),
          ("standby", 4))
    )


_Mc2200_GEmux8RemoteLANLink_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemoteLANLink_Object = MibTableColumn
mc2200_GEmux8RemoteLANLink = _Mc2200_GEmux8RemoteLANLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 97),
    _Mc2200_GEmux8RemoteLANLink_Type()
)
mc2200_GEmux8RemoteLANLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemoteLANLink.setStatus("mandatory")
_Mc2200_GEmux8RemoteWANSFPInfo_Type = DisplayString
_Mc2200_GEmux8RemoteWANSFPInfo_Object = MibTableColumn
mc2200_GEmux8RemoteWANSFPInfo = _Mc2200_GEmux8RemoteWANSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 98),
    _Mc2200_GEmux8RemoteWANSFPInfo_Type()
)
mc2200_GEmux8RemoteWANSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemoteWANSFPInfo.setStatus("current")


class _Mc2200_GEmux8RemoteWANLink_Type(Integer32):
    """Custom type mc2200_GEmux8RemoteWANLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2),
          ("active", 3),
          ("standby", 4))
    )


_Mc2200_GEmux8RemoteWANLink_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemoteWANLink_Object = MibTableColumn
mc2200_GEmux8RemoteWANLink = _Mc2200_GEmux8RemoteWANLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 99),
    _Mc2200_GEmux8RemoteWANLink_Type()
)
mc2200_GEmux8RemoteWANLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemoteWANLink.setStatus("current")


class _Mc2200_GEmux8RemotePort1Link_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort1Link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_GEmux8RemotePort1Link_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort1Link_Object = MibTableColumn
mc2200_GEmux8RemotePort1Link = _Mc2200_GEmux8RemotePort1Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 100),
    _Mc2200_GEmux8RemotePort1Link_Type()
)
mc2200_GEmux8RemotePort1Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort1Link.setStatus("current")


class _Mc2200_GEmux8RemotePort1Speed_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort1Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("speed100M", 1),
          ("speed10M", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8RemotePort1Speed_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort1Speed_Object = MibTableColumn
mc2200_GEmux8RemotePort1Speed = _Mc2200_GEmux8RemotePort1Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 101),
    _Mc2200_GEmux8RemotePort1Speed_Type()
)
mc2200_GEmux8RemotePort1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort1Speed.setStatus("current")


class _Mc2200_GEmux8RemotePort1Duplex_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort1Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8RemotePort1Duplex_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort1Duplex_Object = MibTableColumn
mc2200_GEmux8RemotePort1Duplex = _Mc2200_GEmux8RemotePort1Duplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 102),
    _Mc2200_GEmux8RemotePort1Duplex_Type()
)
mc2200_GEmux8RemotePort1Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort1Duplex.setStatus("current")


class _Mc2200_GEmux8RemotePort1Mode_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort1Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mode10MHALFDUPLEX", 2),
          ("mode10MFULLDUPLEX", 3),
          ("mode100MHALFDUPLEX", 4),
          ("mode100MFULLDUPLEX", 5))
    )


_Mc2200_GEmux8RemotePort1Mode_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort1Mode_Object = MibTableColumn
mc2200_GEmux8RemotePort1Mode = _Mc2200_GEmux8RemotePort1Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 103),
    _Mc2200_GEmux8RemotePort1Mode_Type()
)
mc2200_GEmux8RemotePort1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort1Mode.setStatus("current")


class _Mc2200_GEmux8RemotePort1MDIX_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort1MDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mdi", 2),
          ("mdi-x", 3))
    )


_Mc2200_GEmux8RemotePort1MDIX_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort1MDIX_Object = MibTableColumn
mc2200_GEmux8RemotePort1MDIX = _Mc2200_GEmux8RemotePort1MDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 104),
    _Mc2200_GEmux8RemotePort1MDIX_Type()
)
mc2200_GEmux8RemotePort1MDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort1MDIX.setStatus("current")


class _Mc2200_GEmux8RemotePort2Link_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort2Link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_GEmux8RemotePort2Link_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort2Link_Object = MibTableColumn
mc2200_GEmux8RemotePort2Link = _Mc2200_GEmux8RemotePort2Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 105),
    _Mc2200_GEmux8RemotePort2Link_Type()
)
mc2200_GEmux8RemotePort2Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort2Link.setStatus("current")


class _Mc2200_GEmux8RemotePort2Speed_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort2Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("speed100M", 1),
          ("speed10M", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8RemotePort2Speed_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort2Speed_Object = MibTableColumn
mc2200_GEmux8RemotePort2Speed = _Mc2200_GEmux8RemotePort2Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 106),
    _Mc2200_GEmux8RemotePort2Speed_Type()
)
mc2200_GEmux8RemotePort2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort2Speed.setStatus("current")


class _Mc2200_GEmux8RemotePort2Duplex_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort2Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8RemotePort2Duplex_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort2Duplex_Object = MibTableColumn
mc2200_GEmux8RemotePort2Duplex = _Mc2200_GEmux8RemotePort2Duplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 107),
    _Mc2200_GEmux8RemotePort2Duplex_Type()
)
mc2200_GEmux8RemotePort2Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort2Duplex.setStatus("current")


class _Mc2200_GEmux8RemotePort2Mode_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort2Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mode10MHALFDUPLEX", 2),
          ("mode10MFULLDUPLEX", 3),
          ("mode100MHALFDUPLEX", 4),
          ("mode100MFULLDUPLEX", 5))
    )


_Mc2200_GEmux8RemotePort2Mode_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort2Mode_Object = MibTableColumn
mc2200_GEmux8RemotePort2Mode = _Mc2200_GEmux8RemotePort2Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 108),
    _Mc2200_GEmux8RemotePort2Mode_Type()
)
mc2200_GEmux8RemotePort2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort2Mode.setStatus("current")


class _Mc2200_GEmux8RemotePort2MDIX_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort2MDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mdi", 2),
          ("mdi-x", 3))
    )


_Mc2200_GEmux8RemotePort2MDIX_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort2MDIX_Object = MibTableColumn
mc2200_GEmux8RemotePort2MDIX = _Mc2200_GEmux8RemotePort2MDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 109),
    _Mc2200_GEmux8RemotePort2MDIX_Type()
)
mc2200_GEmux8RemotePort2MDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort2MDIX.setStatus("current")


class _Mc2200_GEmux8RemotePort3Link_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort3Link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_GEmux8RemotePort3Link_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort3Link_Object = MibTableColumn
mc2200_GEmux8RemotePort3Link = _Mc2200_GEmux8RemotePort3Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 110),
    _Mc2200_GEmux8RemotePort3Link_Type()
)
mc2200_GEmux8RemotePort3Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort3Link.setStatus("current")


class _Mc2200_GEmux8RemotePort3Speed_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort3Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("speed100M", 1),
          ("speed10M", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8RemotePort3Speed_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort3Speed_Object = MibTableColumn
mc2200_GEmux8RemotePort3Speed = _Mc2200_GEmux8RemotePort3Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 111),
    _Mc2200_GEmux8RemotePort3Speed_Type()
)
mc2200_GEmux8RemotePort3Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort3Speed.setStatus("current")


class _Mc2200_GEmux8RemotePort3Duplex_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort3Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8RemotePort3Duplex_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort3Duplex_Object = MibTableColumn
mc2200_GEmux8RemotePort3Duplex = _Mc2200_GEmux8RemotePort3Duplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 112),
    _Mc2200_GEmux8RemotePort3Duplex_Type()
)
mc2200_GEmux8RemotePort3Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort3Duplex.setStatus("current")


class _Mc2200_GEmux8RemotePort3Mode_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort3Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mode10MHALFDUPLEX", 2),
          ("mode10MFULLDUPLEX", 3),
          ("mode100MHALFDUPLEX", 4),
          ("mode100MFULLDUPLEX", 5))
    )


_Mc2200_GEmux8RemotePort3Mode_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort3Mode_Object = MibTableColumn
mc2200_GEmux8RemotePort3Mode = _Mc2200_GEmux8RemotePort3Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 113),
    _Mc2200_GEmux8RemotePort3Mode_Type()
)
mc2200_GEmux8RemotePort3Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort3Mode.setStatus("current")


class _Mc2200_GEmux8RemotePort3MDIX_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort3MDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mdi", 2),
          ("mdi-x", 3))
    )


_Mc2200_GEmux8RemotePort3MDIX_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort3MDIX_Object = MibTableColumn
mc2200_GEmux8RemotePort3MDIX = _Mc2200_GEmux8RemotePort3MDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 114),
    _Mc2200_GEmux8RemotePort3MDIX_Type()
)
mc2200_GEmux8RemotePort3MDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort3MDIX.setStatus("current")


class _Mc2200_GEmux8RemotePort4Link_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort4Link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_GEmux8RemotePort4Link_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort4Link_Object = MibTableColumn
mc2200_GEmux8RemotePort4Link = _Mc2200_GEmux8RemotePort4Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 115),
    _Mc2200_GEmux8RemotePort4Link_Type()
)
mc2200_GEmux8RemotePort4Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort4Link.setStatus("current")


class _Mc2200_GEmux8RemotePort4Speed_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort4Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("speed100M", 1),
          ("speed10M", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8RemotePort4Speed_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort4Speed_Object = MibTableColumn
mc2200_GEmux8RemotePort4Speed = _Mc2200_GEmux8RemotePort4Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 116),
    _Mc2200_GEmux8RemotePort4Speed_Type()
)
mc2200_GEmux8RemotePort4Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort4Speed.setStatus("current")


class _Mc2200_GEmux8RemotePort4Duplex_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort4Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8RemotePort4Duplex_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort4Duplex_Object = MibTableColumn
mc2200_GEmux8RemotePort4Duplex = _Mc2200_GEmux8RemotePort4Duplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 117),
    _Mc2200_GEmux8RemotePort4Duplex_Type()
)
mc2200_GEmux8RemotePort4Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort4Duplex.setStatus("current")


class _Mc2200_GEmux8RemotePort4Mode_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort4Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mode10MHALFDUPLEX", 2),
          ("mode10MFULLDUPLEX", 3),
          ("mode100MHALFDUPLEX", 4),
          ("mode100MFULLDUPLEX", 5))
    )


_Mc2200_GEmux8RemotePort4Mode_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort4Mode_Object = MibTableColumn
mc2200_GEmux8RemotePort4Mode = _Mc2200_GEmux8RemotePort4Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 118),
    _Mc2200_GEmux8RemotePort4Mode_Type()
)
mc2200_GEmux8RemotePort4Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort4Mode.setStatus("current")


class _Mc2200_GEmux8RemotePort4MDIX_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort4MDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mdi", 2),
          ("mdi-x", 3))
    )


_Mc2200_GEmux8RemotePort4MDIX_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort4MDIX_Object = MibTableColumn
mc2200_GEmux8RemotePort4MDIX = _Mc2200_GEmux8RemotePort4MDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 119),
    _Mc2200_GEmux8RemotePort4MDIX_Type()
)
mc2200_GEmux8RemotePort4MDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort4MDIX.setStatus("current")


class _Mc2200_GEmux8RemotePort5Link_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort5Link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_GEmux8RemotePort5Link_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort5Link_Object = MibTableColumn
mc2200_GEmux8RemotePort5Link = _Mc2200_GEmux8RemotePort5Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 120),
    _Mc2200_GEmux8RemotePort5Link_Type()
)
mc2200_GEmux8RemotePort5Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort5Link.setStatus("current")


class _Mc2200_GEmux8RemotePort5Speed_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort5Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("speed100M", 1),
          ("speed10M", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8RemotePort5Speed_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort5Speed_Object = MibTableColumn
mc2200_GEmux8RemotePort5Speed = _Mc2200_GEmux8RemotePort5Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 121),
    _Mc2200_GEmux8RemotePort5Speed_Type()
)
mc2200_GEmux8RemotePort5Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort5Speed.setStatus("current")


class _Mc2200_GEmux8RemotePort5Duplex_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort5Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8RemotePort5Duplex_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort5Duplex_Object = MibTableColumn
mc2200_GEmux8RemotePort5Duplex = _Mc2200_GEmux8RemotePort5Duplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 122),
    _Mc2200_GEmux8RemotePort5Duplex_Type()
)
mc2200_GEmux8RemotePort5Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort5Duplex.setStatus("current")


class _Mc2200_GEmux8RemotePort5Mode_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort5Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mode10MHALFDUPLEX", 2),
          ("mode10MFULLDUPLEX", 3),
          ("mode100MHALFDUPLEX", 4),
          ("mode100MFULLDUPLEX", 5))
    )


_Mc2200_GEmux8RemotePort5Mode_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort5Mode_Object = MibTableColumn
mc2200_GEmux8RemotePort5Mode = _Mc2200_GEmux8RemotePort5Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 123),
    _Mc2200_GEmux8RemotePort5Mode_Type()
)
mc2200_GEmux8RemotePort5Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort5Mode.setStatus("current")


class _Mc2200_GEmux8RemotePort5MDIX_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort5MDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mdi", 2),
          ("mdi-x", 3))
    )


_Mc2200_GEmux8RemotePort5MDIX_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort5MDIX_Object = MibTableColumn
mc2200_GEmux8RemotePort5MDIX = _Mc2200_GEmux8RemotePort5MDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 124),
    _Mc2200_GEmux8RemotePort5MDIX_Type()
)
mc2200_GEmux8RemotePort5MDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort5MDIX.setStatus("current")


class _Mc2200_GEmux8RemotePort6Link_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort6Link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_GEmux8RemotePort6Link_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort6Link_Object = MibTableColumn
mc2200_GEmux8RemotePort6Link = _Mc2200_GEmux8RemotePort6Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 125),
    _Mc2200_GEmux8RemotePort6Link_Type()
)
mc2200_GEmux8RemotePort6Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort6Link.setStatus("current")


class _Mc2200_GEmux8RemotePort6Speed_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort6Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("speed100M", 1),
          ("speed10M", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8RemotePort6Speed_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort6Speed_Object = MibTableColumn
mc2200_GEmux8RemotePort6Speed = _Mc2200_GEmux8RemotePort6Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 126),
    _Mc2200_GEmux8RemotePort6Speed_Type()
)
mc2200_GEmux8RemotePort6Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort6Speed.setStatus("current")


class _Mc2200_GEmux8RemotePort6Duplex_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort6Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8RemotePort6Duplex_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort6Duplex_Object = MibTableColumn
mc2200_GEmux8RemotePort6Duplex = _Mc2200_GEmux8RemotePort6Duplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 127),
    _Mc2200_GEmux8RemotePort6Duplex_Type()
)
mc2200_GEmux8RemotePort6Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort6Duplex.setStatus("current")


class _Mc2200_GEmux8RemotePort6Mode_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort6Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mode10MHALFDUPLEX", 2),
          ("mode10MFULLDUPLEX", 3),
          ("mode100MHALFDUPLEX", 4),
          ("mode100MFULLDUPLEX", 5))
    )


_Mc2200_GEmux8RemotePort6Mode_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort6Mode_Object = MibTableColumn
mc2200_GEmux8RemotePort6Mode = _Mc2200_GEmux8RemotePort6Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 128),
    _Mc2200_GEmux8RemotePort6Mode_Type()
)
mc2200_GEmux8RemotePort6Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort6Mode.setStatus("current")


class _Mc2200_GEmux8RemotePort6MDIX_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort6MDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mdi", 2),
          ("mdi-x", 3))
    )


_Mc2200_GEmux8RemotePort6MDIX_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort6MDIX_Object = MibTableColumn
mc2200_GEmux8RemotePort6MDIX = _Mc2200_GEmux8RemotePort6MDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 129),
    _Mc2200_GEmux8RemotePort6MDIX_Type()
)
mc2200_GEmux8RemotePort6MDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort6MDIX.setStatus("current")


class _Mc2200_GEmux8RemotePort7Link_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort7Link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_GEmux8RemotePort7Link_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort7Link_Object = MibTableColumn
mc2200_GEmux8RemotePort7Link = _Mc2200_GEmux8RemotePort7Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 130),
    _Mc2200_GEmux8RemotePort7Link_Type()
)
mc2200_GEmux8RemotePort7Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort7Link.setStatus("current")


class _Mc2200_GEmux8RemotePort7Speed_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort7Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("speed100M", 1),
          ("speed10M", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8RemotePort7Speed_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort7Speed_Object = MibTableColumn
mc2200_GEmux8RemotePort7Speed = _Mc2200_GEmux8RemotePort7Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 131),
    _Mc2200_GEmux8RemotePort7Speed_Type()
)
mc2200_GEmux8RemotePort7Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort7Speed.setStatus("current")


class _Mc2200_GEmux8RemotePort7Duplex_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort7Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8RemotePort7Duplex_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort7Duplex_Object = MibTableColumn
mc2200_GEmux8RemotePort7Duplex = _Mc2200_GEmux8RemotePort7Duplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 132),
    _Mc2200_GEmux8RemotePort7Duplex_Type()
)
mc2200_GEmux8RemotePort7Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort7Duplex.setStatus("current")


class _Mc2200_GEmux8RemotePort7Mode_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort7Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mode10MHALFDUPLEX", 2),
          ("mode10MFULLDUPLEX", 3),
          ("mode100MHALFDUPLEX", 4),
          ("mode100MFULLDUPLEX", 5))
    )


_Mc2200_GEmux8RemotePort7Mode_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort7Mode_Object = MibTableColumn
mc2200_GEmux8RemotePort7Mode = _Mc2200_GEmux8RemotePort7Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 133),
    _Mc2200_GEmux8RemotePort7Mode_Type()
)
mc2200_GEmux8RemotePort7Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort7Mode.setStatus("current")


class _Mc2200_GEmux8RemotePort7MDIX_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort7MDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mdi", 2),
          ("mdi-x", 3))
    )


_Mc2200_GEmux8RemotePort7MDIX_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort7MDIX_Object = MibTableColumn
mc2200_GEmux8RemotePort7MDIX = _Mc2200_GEmux8RemotePort7MDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 134),
    _Mc2200_GEmux8RemotePort7MDIX_Type()
)
mc2200_GEmux8RemotePort7MDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort7MDIX.setStatus("current")


class _Mc2200_GEmux8RemotePort8Link_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort8Link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_GEmux8RemotePort8Link_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort8Link_Object = MibTableColumn
mc2200_GEmux8RemotePort8Link = _Mc2200_GEmux8RemotePort8Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 135),
    _Mc2200_GEmux8RemotePort8Link_Type()
)
mc2200_GEmux8RemotePort8Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort8Link.setStatus("current")


class _Mc2200_GEmux8RemotePort8Speed_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort8Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("speed100M", 1),
          ("speed10M", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8RemotePort8Speed_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort8Speed_Object = MibTableColumn
mc2200_GEmux8RemotePort8Speed = _Mc2200_GEmux8RemotePort8Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 136),
    _Mc2200_GEmux8RemotePort8Speed_Type()
)
mc2200_GEmux8RemotePort8Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort8Speed.setStatus("current")


class _Mc2200_GEmux8RemotePort8Duplex_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort8Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_Mc2200_GEmux8RemotePort8Duplex_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort8Duplex_Object = MibTableColumn
mc2200_GEmux8RemotePort8Duplex = _Mc2200_GEmux8RemotePort8Duplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 137),
    _Mc2200_GEmux8RemotePort8Duplex_Type()
)
mc2200_GEmux8RemotePort8Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort8Duplex.setStatus("current")


class _Mc2200_GEmux8RemotePort8Mode_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort8Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mode10MHALFDUPLEX", 2),
          ("mode10MFULLDUPLEX", 3),
          ("mode100MHALFDUPLEX", 4),
          ("mode100MFULLDUPLEX", 5))
    )


_Mc2200_GEmux8RemotePort8Mode_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort8Mode_Object = MibTableColumn
mc2200_GEmux8RemotePort8Mode = _Mc2200_GEmux8RemotePort8Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 138),
    _Mc2200_GEmux8RemotePort8Mode_Type()
)
mc2200_GEmux8RemotePort8Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort8Mode.setStatus("current")


class _Mc2200_GEmux8RemotePort8MDIX_Type(Integer32):
    """Custom type mc2200_GEmux8RemotePort8MDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mdi", 2),
          ("mdi-x", 3))
    )


_Mc2200_GEmux8RemotePort8MDIX_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemotePort8MDIX_Object = MibTableColumn
mc2200_GEmux8RemotePort8MDIX = _Mc2200_GEmux8RemotePort8MDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 139),
    _Mc2200_GEmux8RemotePort8MDIX_Type()
)
mc2200_GEmux8RemotePort8MDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemotePort8MDIX.setStatus("current")
_Mc2200_GEmux8RemoteIPAddress_Type = IpAddress
_Mc2200_GEmux8RemoteIPAddress_Object = MibTableColumn
mc2200_GEmux8RemoteIPAddress = _Mc2200_GEmux8RemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 140),
    _Mc2200_GEmux8RemoteIPAddress_Type()
)
mc2200_GEmux8RemoteIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemoteIPAddress.setStatus("mandatory")
_Mc2200_GEmux8RemoteSubnetMask_Type = IpAddress
_Mc2200_GEmux8RemoteSubnetMask_Object = MibTableColumn
mc2200_GEmux8RemoteSubnetMask = _Mc2200_GEmux8RemoteSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 141),
    _Mc2200_GEmux8RemoteSubnetMask_Type()
)
mc2200_GEmux8RemoteSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemoteSubnetMask.setStatus("mandatory")
_Mc2200_GEmux8RemoteGateWay_Type = IpAddress
_Mc2200_GEmux8RemoteGateWay_Object = MibTableColumn
mc2200_GEmux8RemoteGateWay = _Mc2200_GEmux8RemoteGateWay_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 142),
    _Mc2200_GEmux8RemoteGateWay_Type()
)
mc2200_GEmux8RemoteGateWay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemoteGateWay.setStatus("mandatory")


class _Mc2200_GEmux8RemoteVLANEnable_Type(Integer32):
    """Custom type mc2200_GEmux8RemoteVLANEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("enable", 1),
          ("disable", 2))
    )


_Mc2200_GEmux8RemoteVLANEnable_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemoteVLANEnable_Object = MibTableColumn
mc2200_GEmux8RemoteVLANEnable = _Mc2200_GEmux8RemoteVLANEnable_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 143),
    _Mc2200_GEmux8RemoteVLANEnable_Type()
)
mc2200_GEmux8RemoteVLANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemoteVLANEnable.setStatus("mandatory")
_Mc2200_GEmux8RemoteVID_Type = Integer32
_Mc2200_GEmux8RemoteVID_Object = MibTableColumn
mc2200_GEmux8RemoteVID = _Mc2200_GEmux8RemoteVID_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 144),
    _Mc2200_GEmux8RemoteVID_Type()
)
mc2200_GEmux8RemoteVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemoteVID.setStatus("mandatory")


class _Mc2200_GEmux8RemoteAlarm_Type(Integer32):
    """Custom type mc2200_GEmux8RemoteAlarm based on Integer32"""
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


_Mc2200_GEmux8RemoteAlarm_Type.__name__ = "Integer32"
_Mc2200_GEmux8RemoteAlarm_Object = MibTableColumn
mc2200_GEmux8RemoteAlarm = _Mc2200_GEmux8RemoteAlarm_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 145),
    _Mc2200_GEmux8RemoteAlarm_Type()
)
mc2200_GEmux8RemoteAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8RemoteAlarm.setStatus("current")


class _Mc2200_GEmux8RFD_Type(Integer32):
    """Custom type mc2200_GEmux8RFD based on Integer32"""
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


_Mc2200_GEmux8RFD_Type.__name__ = "Integer32"
_Mc2200_GEmux8RFD_Object = MibTableColumn
mc2200_GEmux8RFD = _Mc2200_GEmux8RFD_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 146),
    _Mc2200_GEmux8RFD_Type()
)
mc2200_GEmux8RFD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8RFD.setStatus("current")
_Mc2200_GEmux8Default_Type = Integer32
_Mc2200_GEmux8Default_Object = MibTableColumn
mc2200_GEmux8Default = _Mc2200_GEmux8Default_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 147),
    _Mc2200_GEmux8Default_Type()
)
mc2200_GEmux8Default.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8Default.setStatus("current")
_Mc2200_GEmux8Reboot_Type = Integer32
_Mc2200_GEmux8Reboot_Object = MibTableColumn
mc2200_GEmux8Reboot = _Mc2200_GEmux8Reboot_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 148),
    _Mc2200_GEmux8Reboot_Type()
)
mc2200_GEmux8Reboot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mc2200_GEmux8Reboot.setStatus("current")


class _Mc2200_GEmux8LocalCardREMOTEMODE_Type(Integer32):
    """Custom type mc2200_GEmux8LocalCardREMOTEMODE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("remoteModeEnabled", 1),
          ("remoteModeDisabled", 2),
          ("noSetting", 3))
    )


_Mc2200_GEmux8LocalCardREMOTEMODE_Type.__name__ = "Integer32"
_Mc2200_GEmux8LocalCardREMOTEMODE_Object = MibTableColumn
mc2200_GEmux8LocalCardREMOTEMODE = _Mc2200_GEmux8LocalCardREMOTEMODE_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 149),
    _Mc2200_GEmux8LocalCardREMOTEMODE_Type()
)
mc2200_GEmux8LocalCardREMOTEMODE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8LocalCardREMOTEMODE.setStatus("current")
_Mc2200_GEmux8Localportuser1_Type = DisplayString
_Mc2200_GEmux8Localportuser1_Object = MibTableColumn
mc2200_GEmux8Localportuser1 = _Mc2200_GEmux8Localportuser1_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 150),
    _Mc2200_GEmux8Localportuser1_Type()
)
mc2200_GEmux8Localportuser1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8Localportuser1.setStatus("current")
_Mc2200_GEmux8Localportuser2_Type = DisplayString
_Mc2200_GEmux8Localportuser2_Object = MibTableColumn
mc2200_GEmux8Localportuser2 = _Mc2200_GEmux8Localportuser2_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 151),
    _Mc2200_GEmux8Localportuser2_Type()
)
mc2200_GEmux8Localportuser2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8Localportuser2.setStatus("current")
_Mc2200_GEmux8Localportuser3_Type = DisplayString
_Mc2200_GEmux8Localportuser3_Object = MibTableColumn
mc2200_GEmux8Localportuser3 = _Mc2200_GEmux8Localportuser3_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 152),
    _Mc2200_GEmux8Localportuser3_Type()
)
mc2200_GEmux8Localportuser3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8Localportuser3.setStatus("current")
_Mc2200_GEmux8Localportuser4_Type = DisplayString
_Mc2200_GEmux8Localportuser4_Object = MibTableColumn
mc2200_GEmux8Localportuser4 = _Mc2200_GEmux8Localportuser4_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 153),
    _Mc2200_GEmux8Localportuser4_Type()
)
mc2200_GEmux8Localportuser4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8Localportuser4.setStatus("current")
_Mc2200_GEmux8Localportuser5_Type = DisplayString
_Mc2200_GEmux8Localportuser5_Object = MibTableColumn
mc2200_GEmux8Localportuser5 = _Mc2200_GEmux8Localportuser5_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 154),
    _Mc2200_GEmux8Localportuser5_Type()
)
mc2200_GEmux8Localportuser5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8Localportuser5.setStatus("current")
_Mc2200_GEmux8Localportuser6_Type = DisplayString
_Mc2200_GEmux8Localportuser6_Object = MibTableColumn
mc2200_GEmux8Localportuser6 = _Mc2200_GEmux8Localportuser6_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 155),
    _Mc2200_GEmux8Localportuser6_Type()
)
mc2200_GEmux8Localportuser6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8Localportuser6.setStatus("current")
_Mc2200_GEmux8Localportuser7_Type = DisplayString
_Mc2200_GEmux8Localportuser7_Object = MibTableColumn
mc2200_GEmux8Localportuser7 = _Mc2200_GEmux8Localportuser7_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 156),
    _Mc2200_GEmux8Localportuser7_Type()
)
mc2200_GEmux8Localportuser7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8Localportuser7.setStatus("current")
_Mc2200_GEmux8Localportuser8_Type = DisplayString
_Mc2200_GEmux8Localportuser8_Object = MibTableColumn
mc2200_GEmux8Localportuser8 = _Mc2200_GEmux8Localportuser8_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 157),
    _Mc2200_GEmux8Localportuser8_Type()
)
mc2200_GEmux8Localportuser8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8Localportuser8.setStatus("current")
_Mc2200_GEmux8Remoteportuser1_Type = DisplayString
_Mc2200_GEmux8Remoteportuser1_Object = MibTableColumn
mc2200_GEmux8Remoteportuser1 = _Mc2200_GEmux8Remoteportuser1_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 158),
    _Mc2200_GEmux8Remoteportuser1_Type()
)
mc2200_GEmux8Remoteportuser1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8Remoteportuser1.setStatus("current")
_Mc2200_GEmux8Remoteportuser2_Type = DisplayString
_Mc2200_GEmux8Remoteportuser2_Object = MibTableColumn
mc2200_GEmux8Remoteportuser2 = _Mc2200_GEmux8Remoteportuser2_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 159),
    _Mc2200_GEmux8Remoteportuser2_Type()
)
mc2200_GEmux8Remoteportuser2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8Remoteportuser2.setStatus("current")
_Mc2200_GEmux8Remoteportuser3_Type = DisplayString
_Mc2200_GEmux8Remoteportuser3_Object = MibTableColumn
mc2200_GEmux8Remoteportuser3 = _Mc2200_GEmux8Remoteportuser3_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 160),
    _Mc2200_GEmux8Remoteportuser3_Type()
)
mc2200_GEmux8Remoteportuser3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8Remoteportuser3.setStatus("current")
_Mc2200_GEmux8Remoteportuser4_Type = DisplayString
_Mc2200_GEmux8Remoteportuser4_Object = MibTableColumn
mc2200_GEmux8Remoteportuser4 = _Mc2200_GEmux8Remoteportuser4_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 161),
    _Mc2200_GEmux8Remoteportuser4_Type()
)
mc2200_GEmux8Remoteportuser4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8Remoteportuser4.setStatus("current")
_Mc2200_GEmux8Remoteportuser5_Type = DisplayString
_Mc2200_GEmux8Remoteportuser5_Object = MibTableColumn
mc2200_GEmux8Remoteportuser5 = _Mc2200_GEmux8Remoteportuser5_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 162),
    _Mc2200_GEmux8Remoteportuser5_Type()
)
mc2200_GEmux8Remoteportuser5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8Remoteportuser5.setStatus("current")
_Mc2200_GEmux8Remoteportuser6_Type = DisplayString
_Mc2200_GEmux8Remoteportuser6_Object = MibTableColumn
mc2200_GEmux8Remoteportuser6 = _Mc2200_GEmux8Remoteportuser6_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 163),
    _Mc2200_GEmux8Remoteportuser6_Type()
)
mc2200_GEmux8Remoteportuser6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8Remoteportuser6.setStatus("current")
_Mc2200_GEmux8Remoteportuser7_Type = DisplayString
_Mc2200_GEmux8Remoteportuser7_Object = MibTableColumn
mc2200_GEmux8Remoteportuser7 = _Mc2200_GEmux8Remoteportuser7_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 164),
    _Mc2200_GEmux8Remoteportuser7_Type()
)
mc2200_GEmux8Remoteportuser7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8Remoteportuser7.setStatus("current")
_Mc2200_GEmux8Remoteportuser8_Type = DisplayString
_Mc2200_GEmux8Remoteportuser8_Object = MibTableColumn
mc2200_GEmux8Remoteportuser8 = _Mc2200_GEmux8Remoteportuser8_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 165),
    _Mc2200_GEmux8Remoteportuser8_Type()
)
mc2200_GEmux8Remoteportuser8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8Remoteportuser8.setStatus("current")


class _Mc2200_GEmux8TrapFilterLocalLAN_Type(Integer32):
    """Custom type mc2200_GEmux8TrapFilterLocalLAN based on Integer32"""
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


_Mc2200_GEmux8TrapFilterLocalLAN_Type.__name__ = "Integer32"
_Mc2200_GEmux8TrapFilterLocalLAN_Object = MibTableColumn
mc2200_GEmux8TrapFilterLocalLAN = _Mc2200_GEmux8TrapFilterLocalLAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 166),
    _Mc2200_GEmux8TrapFilterLocalLAN_Type()
)
mc2200_GEmux8TrapFilterLocalLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8TrapFilterLocalLAN.setStatus("current")


class _Mc2200_GEmux8TrapFilterLocalWAN_Type(Integer32):
    """Custom type mc2200_GEmux8TrapFilterLocalWAN based on Integer32"""
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


_Mc2200_GEmux8TrapFilterLocalWAN_Type.__name__ = "Integer32"
_Mc2200_GEmux8TrapFilterLocalWAN_Object = MibTableColumn
mc2200_GEmux8TrapFilterLocalWAN = _Mc2200_GEmux8TrapFilterLocalWAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 167),
    _Mc2200_GEmux8TrapFilterLocalWAN_Type()
)
mc2200_GEmux8TrapFilterLocalWAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8TrapFilterLocalWAN.setStatus("current")


class _Mc2200_GEmux8TrapFilterRemotePower_Type(Integer32):
    """Custom type mc2200_GEmux8TrapFilterRemotePower based on Integer32"""
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


_Mc2200_GEmux8TrapFilterRemotePower_Type.__name__ = "Integer32"
_Mc2200_GEmux8TrapFilterRemotePower_Object = MibTableColumn
mc2200_GEmux8TrapFilterRemotePower = _Mc2200_GEmux8TrapFilterRemotePower_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 168),
    _Mc2200_GEmux8TrapFilterRemotePower_Type()
)
mc2200_GEmux8TrapFilterRemotePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8TrapFilterRemotePower.setStatus("current")


class _Mc2200_GEmux8TrapFilterRemoteLAN_Type(Integer32):
    """Custom type mc2200_GEmux8TrapFilterRemoteLAN based on Integer32"""
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


_Mc2200_GEmux8TrapFilterRemoteLAN_Type.__name__ = "Integer32"
_Mc2200_GEmux8TrapFilterRemoteLAN_Object = MibTableColumn
mc2200_GEmux8TrapFilterRemoteLAN = _Mc2200_GEmux8TrapFilterRemoteLAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 169),
    _Mc2200_GEmux8TrapFilterRemoteLAN_Type()
)
mc2200_GEmux8TrapFilterRemoteLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8TrapFilterRemoteLAN.setStatus("current")


class _Mc2200_GEmux8TrapFilterRemoteWAN_Type(Integer32):
    """Custom type mc2200_GEmux8TrapFilterRemoteWAN based on Integer32"""
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


_Mc2200_GEmux8TrapFilterRemoteWAN_Type.__name__ = "Integer32"
_Mc2200_GEmux8TrapFilterRemoteWAN_Object = MibTableColumn
mc2200_GEmux8TrapFilterRemoteWAN = _Mc2200_GEmux8TrapFilterRemoteWAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 1, 1, 170),
    _Mc2200_GEmux8TrapFilterRemoteWAN_Type()
)
mc2200_GEmux8TrapFilterRemoteWAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEmux8TrapFilterRemoteWAN.setStatus("current")
_Mc2200_GEMC4Table_Object = MibTable
mc2200_GEMC4Table = _Mc2200_GEMC4Table_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5)
)
if mibBuilder.loadTexts:
    mc2200_GEMC4Table.setStatus("current")
_Mc2200_GEMC4Entry_Object = MibTableRow
mc2200_GEMC4Entry = _Mc2200_GEMC4Entry_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1)
)
mc2200_GEMC4Entry.setIndexNames(
    (0, "OnAccess2200-MIB", "mc2200-GEMC4CardIndex"),
)
if mibBuilder.loadTexts:
    mc2200_GEMC4Entry.setStatus("current")


class _Mc2200_GEMC4CardIndex_Type(Integer32):
    """Custom type mc2200_GEMC4CardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("card01", 1),
          ("card02", 2),
          ("card03", 3),
          ("card04", 4),
          ("card05", 5),
          ("card06", 6),
          ("card07", 7),
          ("card08", 8),
          ("card09", 9),
          ("card10", 10),
          ("card11", 11),
          ("card12", 12),
          ("card13", 13),
          ("card14", 14),
          ("card15", 15))
    )


_Mc2200_GEMC4CardIndex_Type.__name__ = "Integer32"
_Mc2200_GEMC4CardIndex_Object = MibTableColumn
mc2200_GEMC4CardIndex = _Mc2200_GEMC4CardIndex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 1),
    _Mc2200_GEMC4CardIndex_Type()
)
mc2200_GEMC4CardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4CardIndex.setStatus("current")


class _Mc2200_GEMC4CardMode_Type(Integer32):
    """Custom type mc2200_GEMC4CardMode based on Integer32"""
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
        *(("ge-MC2-2-STD", 1),
          ("ge-MC2-2-APS", 2),
          ("ge-MC1-2-APS", 3),
          ("ge-MC3-1-MUX", 4))
    )


_Mc2200_GEMC4CardMode_Type.__name__ = "Integer32"
_Mc2200_GEMC4CardMode_Object = MibTableColumn
mc2200_GEMC4CardMode = _Mc2200_GEMC4CardMode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 2),
    _Mc2200_GEMC4CardMode_Type()
)
mc2200_GEMC4CardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4CardMode.setStatus("mandatory")
_Mc2200_GEMC4LocalLAN1SFPInfo_Type = DisplayString
_Mc2200_GEMC4LocalLAN1SFPInfo_Object = MibTableColumn
mc2200_GEMC4LocalLAN1SFPInfo = _Mc2200_GEMC4LocalLAN1SFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 3),
    _Mc2200_GEMC4LocalLAN1SFPInfo_Type()
)
mc2200_GEMC4LocalLAN1SFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4LocalLAN1SFPInfo.setStatus("current")


class _Mc2200_GEMC4LocalLAN1Link_Type(Integer32):
    """Custom type mc2200_GEMC4LocalLAN1Link based on Integer32"""
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
          ("active", 3),
          ("standby", 4))
    )


_Mc2200_GEMC4LocalLAN1Link_Type.__name__ = "Integer32"
_Mc2200_GEMC4LocalLAN1Link_Object = MibTableColumn
mc2200_GEMC4LocalLAN1Link = _Mc2200_GEMC4LocalLAN1Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 4),
    _Mc2200_GEMC4LocalLAN1Link_Type()
)
mc2200_GEMC4LocalLAN1Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4LocalLAN1Link.setStatus("mandatory")
_Mc2200_GEMC4LocalLAN2SFPInfo_Type = DisplayString
_Mc2200_GEMC4LocalLAN2SFPInfo_Object = MibTableColumn
mc2200_GEMC4LocalLAN2SFPInfo = _Mc2200_GEMC4LocalLAN2SFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 5),
    _Mc2200_GEMC4LocalLAN2SFPInfo_Type()
)
mc2200_GEMC4LocalLAN2SFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4LocalLAN2SFPInfo.setStatus("current")


class _Mc2200_GEMC4LocalLAN2Link_Type(Integer32):
    """Custom type mc2200_GEMC4LocalLAN2Link based on Integer32"""
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


_Mc2200_GEMC4LocalLAN2Link_Type.__name__ = "Integer32"
_Mc2200_GEMC4LocalLAN2Link_Object = MibTableColumn
mc2200_GEMC4LocalLAN2Link = _Mc2200_GEMC4LocalLAN2Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 6),
    _Mc2200_GEMC4LocalLAN2Link_Type()
)
mc2200_GEMC4LocalLAN2Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4LocalLAN2Link.setStatus("mandatory")
_Mc2200_GEMC4LocalWAN1SFPInfo_Type = DisplayString
_Mc2200_GEMC4LocalWAN1SFPInfo_Object = MibTableColumn
mc2200_GEMC4LocalWAN1SFPInfo = _Mc2200_GEMC4LocalWAN1SFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 7),
    _Mc2200_GEMC4LocalWAN1SFPInfo_Type()
)
mc2200_GEMC4LocalWAN1SFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4LocalWAN1SFPInfo.setStatus("current")


class _Mc2200_GEMC4LocalWAN1Link_Type(Integer32):
    """Custom type mc2200_GEMC4LocalWAN1Link based on Integer32"""
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
          ("active", 3),
          ("standby", 4))
    )


_Mc2200_GEMC4LocalWAN1Link_Type.__name__ = "Integer32"
_Mc2200_GEMC4LocalWAN1Link_Object = MibTableColumn
mc2200_GEMC4LocalWAN1Link = _Mc2200_GEMC4LocalWAN1Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 8),
    _Mc2200_GEMC4LocalWAN1Link_Type()
)
mc2200_GEMC4LocalWAN1Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4LocalWAN1Link.setStatus("mandatory")
_Mc2200_GEMC4LocalWAN2LAN3SFPInfo_Type = DisplayString
_Mc2200_GEMC4LocalWAN2LAN3SFPInfo_Object = MibTableColumn
mc2200_GEMC4LocalWAN2LAN3SFPInfo = _Mc2200_GEMC4LocalWAN2LAN3SFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 9),
    _Mc2200_GEMC4LocalWAN2LAN3SFPInfo_Type()
)
mc2200_GEMC4LocalWAN2LAN3SFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4LocalWAN2LAN3SFPInfo.setStatus("current")


class _Mc2200_GEMC4LocalWAN2LAN3Link_Type(Integer32):
    """Custom type mc2200_GEMC4LocalWAN2LAN3Link based on Integer32"""
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
          ("active", 3),
          ("standby", 4))
    )


_Mc2200_GEMC4LocalWAN2LAN3Link_Type.__name__ = "Integer32"
_Mc2200_GEMC4LocalWAN2LAN3Link_Object = MibTableColumn
mc2200_GEMC4LocalWAN2LAN3Link = _Mc2200_GEMC4LocalWAN2LAN3Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 10),
    _Mc2200_GEMC4LocalWAN2LAN3Link_Type()
)
mc2200_GEMC4LocalWAN2LAN3Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4LocalWAN2LAN3Link.setStatus("mandatory")


class _Mc2200_GEMC4LocalLAN1DownStreamBW_Type(Integer32):
    """Custom type mc2200_GEMC4LocalLAN1DownStreamBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              30,
              40,
              50,
              60,
              70,
              80,
              90,
              100,
              150,
              200,
              250,
              300,
              350,
              400,
              450,
              500,
              550,
              600,
              650,
              700,
              750,
              800,
              850,
              900,
              950,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("rate10M", 10),
          ("rate20M", 20),
          ("rate30M", 30),
          ("rate40M", 40),
          ("rate50M", 50),
          ("rate60M", 60),
          ("rate70M", 70),
          ("rate80M", 80),
          ("rate90M", 90),
          ("rate100M", 100),
          ("rate150M", 150),
          ("rate200M", 200),
          ("rate250M", 250),
          ("rate300M", 300),
          ("rate350M", 350),
          ("rate400M", 400),
          ("rate450M", 450),
          ("rate500M", 500),
          ("rate550M", 550),
          ("rate600M", 600),
          ("rate650M", 650),
          ("rate700M", 700),
          ("rate750M", 750),
          ("rate800M", 800),
          ("rate850M", 850),
          ("rate900M", 900),
          ("rate950M", 950),
          ("rate1000M", 1000))
    )


_Mc2200_GEMC4LocalLAN1DownStreamBW_Type.__name__ = "Integer32"
_Mc2200_GEMC4LocalLAN1DownStreamBW_Object = MibTableColumn
mc2200_GEMC4LocalLAN1DownStreamBW = _Mc2200_GEMC4LocalLAN1DownStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 11),
    _Mc2200_GEMC4LocalLAN1DownStreamBW_Type()
)
mc2200_GEMC4LocalLAN1DownStreamBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4LocalLAN1DownStreamBW.setStatus("current")


class _Mc2200_GEMC4LocalLAN1UpStreamBW_Type(Integer32):
    """Custom type mc2200_GEMC4LocalLAN1UpStreamBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              30,
              40,
              50,
              60,
              70,
              80,
              90,
              100,
              150,
              200,
              250,
              300,
              350,
              400,
              450,
              500,
              550,
              600,
              650,
              700,
              750,
              800,
              850,
              900,
              950,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("rate10M", 10),
          ("rate20M", 20),
          ("rate30M", 30),
          ("rate40M", 40),
          ("rate50M", 50),
          ("rate60M", 60),
          ("rate70M", 70),
          ("rate80M", 80),
          ("rate90M", 90),
          ("rate100M", 100),
          ("rate150M", 150),
          ("rate200M", 200),
          ("rate250M", 250),
          ("rate300M", 300),
          ("rate350M", 350),
          ("rate400M", 400),
          ("rate450M", 450),
          ("rate500M", 500),
          ("rate550M", 550),
          ("rate600M", 600),
          ("rate650M", 650),
          ("rate700M", 700),
          ("rate750M", 750),
          ("rate800M", 800),
          ("rate850M", 850),
          ("rate900M", 900),
          ("rate950M", 950),
          ("rate1000M", 1000))
    )


_Mc2200_GEMC4LocalLAN1UpStreamBW_Type.__name__ = "Integer32"
_Mc2200_GEMC4LocalLAN1UpStreamBW_Object = MibTableColumn
mc2200_GEMC4LocalLAN1UpStreamBW = _Mc2200_GEMC4LocalLAN1UpStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 12),
    _Mc2200_GEMC4LocalLAN1UpStreamBW_Type()
)
mc2200_GEMC4LocalLAN1UpStreamBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4LocalLAN1UpStreamBW.setStatus("current")


class _Mc2200_GEMC4LocalLAN2DownStreamBW_Type(Integer32):
    """Custom type mc2200_GEMC4LocalLAN2DownStreamBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              30,
              40,
              50,
              60,
              70,
              80,
              90,
              100,
              150,
              200,
              250,
              300,
              350,
              400,
              450,
              500,
              550,
              600,
              650,
              700,
              750,
              800,
              850,
              900,
              950,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("rate10M", 10),
          ("rate20M", 20),
          ("rate30M", 30),
          ("rate40M", 40),
          ("rate50M", 50),
          ("rate60M", 60),
          ("rate70M", 70),
          ("rate80M", 80),
          ("rate90M", 90),
          ("rate100M", 100),
          ("rate150M", 150),
          ("rate200M", 200),
          ("rate250M", 250),
          ("rate300M", 300),
          ("rate350M", 350),
          ("rate400M", 400),
          ("rate450M", 450),
          ("rate500M", 500),
          ("rate550M", 550),
          ("rate600M", 600),
          ("rate650M", 650),
          ("rate700M", 700),
          ("rate750M", 750),
          ("rate800M", 800),
          ("rate850M", 850),
          ("rate900M", 900),
          ("rate950M", 950),
          ("rate1000M", 1000))
    )


_Mc2200_GEMC4LocalLAN2DownStreamBW_Type.__name__ = "Integer32"
_Mc2200_GEMC4LocalLAN2DownStreamBW_Object = MibTableColumn
mc2200_GEMC4LocalLAN2DownStreamBW = _Mc2200_GEMC4LocalLAN2DownStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 13),
    _Mc2200_GEMC4LocalLAN2DownStreamBW_Type()
)
mc2200_GEMC4LocalLAN2DownStreamBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4LocalLAN2DownStreamBW.setStatus("current")


class _Mc2200_GEMC4LocalLAN2UpStreamBW_Type(Integer32):
    """Custom type mc2200_GEMC4LocalLAN2UpStreamBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              30,
              40,
              50,
              60,
              70,
              80,
              90,
              100,
              150,
              200,
              250,
              300,
              350,
              400,
              450,
              500,
              550,
              600,
              650,
              700,
              750,
              800,
              850,
              900,
              950,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("rate10M", 10),
          ("rate20M", 20),
          ("rate30M", 30),
          ("rate40M", 40),
          ("rate50M", 50),
          ("rate60M", 60),
          ("rate70M", 70),
          ("rate80M", 80),
          ("rate90M", 90),
          ("rate100M", 100),
          ("rate150M", 150),
          ("rate200M", 200),
          ("rate250M", 250),
          ("rate300M", 300),
          ("rate350M", 350),
          ("rate400M", 400),
          ("rate450M", 450),
          ("rate500M", 500),
          ("rate550M", 550),
          ("rate600M", 600),
          ("rate650M", 650),
          ("rate700M", 700),
          ("rate750M", 750),
          ("rate800M", 800),
          ("rate850M", 850),
          ("rate900M", 900),
          ("rate950M", 950),
          ("rate1000M", 1000))
    )


_Mc2200_GEMC4LocalLAN2UpStreamBW_Type.__name__ = "Integer32"
_Mc2200_GEMC4LocalLAN2UpStreamBW_Object = MibTableColumn
mc2200_GEMC4LocalLAN2UpStreamBW = _Mc2200_GEMC4LocalLAN2UpStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 14),
    _Mc2200_GEMC4LocalLAN2UpStreamBW_Type()
)
mc2200_GEMC4LocalLAN2UpStreamBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4LocalLAN2UpStreamBW.setStatus("current")


class _Mc2200_GEMC4LocalLAN3DownStreamBW_Type(Integer32):
    """Custom type mc2200_GEMC4LocalLAN3DownStreamBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              30,
              40,
              50,
              60,
              70,
              80,
              90,
              100,
              150,
              200,
              250,
              300,
              350,
              400,
              450,
              500,
              550,
              600,
              650,
              700,
              750,
              800,
              850,
              900,
              950,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("rate10M", 10),
          ("rate20M", 20),
          ("rate30M", 30),
          ("rate40M", 40),
          ("rate50M", 50),
          ("rate60M", 60),
          ("rate70M", 70),
          ("rate80M", 80),
          ("rate90M", 90),
          ("rate100M", 100),
          ("rate150M", 150),
          ("rate200M", 200),
          ("rate250M", 250),
          ("rate300M", 300),
          ("rate350M", 350),
          ("rate400M", 400),
          ("rate450M", 450),
          ("rate500M", 500),
          ("rate550M", 550),
          ("rate600M", 600),
          ("rate650M", 650),
          ("rate700M", 700),
          ("rate750M", 750),
          ("rate800M", 800),
          ("rate850M", 850),
          ("rate900M", 900),
          ("rate950M", 950),
          ("rate1000M", 1000))
    )


_Mc2200_GEMC4LocalLAN3DownStreamBW_Type.__name__ = "Integer32"
_Mc2200_GEMC4LocalLAN3DownStreamBW_Object = MibTableColumn
mc2200_GEMC4LocalLAN3DownStreamBW = _Mc2200_GEMC4LocalLAN3DownStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 15),
    _Mc2200_GEMC4LocalLAN3DownStreamBW_Type()
)
mc2200_GEMC4LocalLAN3DownStreamBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4LocalLAN3DownStreamBW.setStatus("current")


class _Mc2200_GEMC4LocalLAN3UpStreamBW_Type(Integer32):
    """Custom type mc2200_GEMC4LocalLAN3UpStreamBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              30,
              40,
              50,
              60,
              70,
              80,
              90,
              100,
              150,
              200,
              250,
              300,
              350,
              400,
              450,
              500,
              550,
              600,
              650,
              700,
              750,
              800,
              850,
              900,
              950,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("rate10M", 10),
          ("rate20M", 20),
          ("rate30M", 30),
          ("rate40M", 40),
          ("rate50M", 50),
          ("rate60M", 60),
          ("rate70M", 70),
          ("rate80M", 80),
          ("rate90M", 90),
          ("rate100M", 100),
          ("rate150M", 150),
          ("rate200M", 200),
          ("rate250M", 250),
          ("rate300M", 300),
          ("rate350M", 350),
          ("rate400M", 400),
          ("rate450M", 450),
          ("rate500M", 500),
          ("rate550M", 550),
          ("rate600M", 600),
          ("rate650M", 650),
          ("rate700M", 700),
          ("rate750M", 750),
          ("rate800M", 800),
          ("rate850M", 850),
          ("rate900M", 900),
          ("rate950M", 950),
          ("rate1000M", 1000))
    )


_Mc2200_GEMC4LocalLAN3UpStreamBW_Type.__name__ = "Integer32"
_Mc2200_GEMC4LocalLAN3UpStreamBW_Object = MibTableColumn
mc2200_GEMC4LocalLAN3UpStreamBW = _Mc2200_GEMC4LocalLAN3UpStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 16),
    _Mc2200_GEMC4LocalLAN3UpStreamBW_Type()
)
mc2200_GEMC4LocalLAN3UpStreamBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4LocalLAN3UpStreamBW.setStatus("current")


class _Mc2200_GEMC4LocalLAN1Mode_Type(Integer32):
    """Custom type mc2200_GEMC4LocalLAN1Mode based on Integer32"""
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
        *(("auto-10-100-1000T", 1),
          ("mode1000Base-X-auto", 2),
          ("mode1000Base-T", 3),
          ("mode100Base-Tx", 4),
          ("mode10Base-T", 5),
          ("mode1000Base-X-1000F", 6))
    )


_Mc2200_GEMC4LocalLAN1Mode_Type.__name__ = "Integer32"
_Mc2200_GEMC4LocalLAN1Mode_Object = MibTableColumn
mc2200_GEMC4LocalLAN1Mode = _Mc2200_GEMC4LocalLAN1Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 17),
    _Mc2200_GEMC4LocalLAN1Mode_Type()
)
mc2200_GEMC4LocalLAN1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4LocalLAN1Mode.setStatus("current")


class _Mc2200_GEMC4LocalLAN2Mode_Type(Integer32):
    """Custom type mc2200_GEMC4LocalLAN2Mode based on Integer32"""
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
        *(("auto-10-100-1000T", 1),
          ("mode1000Base-X-auto", 2),
          ("mode1000Base-T", 3),
          ("mode100Base-Tx", 4),
          ("mode10Base-T", 5),
          ("mode1000Base-X-1000F", 6))
    )


_Mc2200_GEMC4LocalLAN2Mode_Type.__name__ = "Integer32"
_Mc2200_GEMC4LocalLAN2Mode_Object = MibTableColumn
mc2200_GEMC4LocalLAN2Mode = _Mc2200_GEMC4LocalLAN2Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 18),
    _Mc2200_GEMC4LocalLAN2Mode_Type()
)
mc2200_GEMC4LocalLAN2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4LocalLAN2Mode.setStatus("current")


class _Mc2200_GEMC4LocalLAN3Mode_Type(Integer32):
    """Custom type mc2200_GEMC4LocalLAN3Mode based on Integer32"""
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
        *(("auto-10-100-1000T", 1),
          ("mode1000Base-X-auto", 2),
          ("mode1000Base-T", 3),
          ("mode100Base-Tx", 4),
          ("mode10Base-T", 5),
          ("mode1000Base-X-1000F", 6))
    )


_Mc2200_GEMC4LocalLAN3Mode_Type.__name__ = "Integer32"
_Mc2200_GEMC4LocalLAN3Mode_Object = MibTableColumn
mc2200_GEMC4LocalLAN3Mode = _Mc2200_GEMC4LocalLAN3Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 19),
    _Mc2200_GEMC4LocalLAN3Mode_Type()
)
mc2200_GEMC4LocalLAN3Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4LocalLAN3Mode.setStatus("current")
_Mc2200_GEMC4MibCounter1_Type = Counter64
_Mc2200_GEMC4MibCounter1_Object = MibTableColumn
mc2200_GEMC4MibCounter1 = _Mc2200_GEMC4MibCounter1_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 20),
    _Mc2200_GEMC4MibCounter1_Type()
)
mc2200_GEMC4MibCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter1.setStatus("current")
_Mc2200_GEMC4MibCounter2_Type = Counter64
_Mc2200_GEMC4MibCounter2_Object = MibTableColumn
mc2200_GEMC4MibCounter2 = _Mc2200_GEMC4MibCounter2_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 21),
    _Mc2200_GEMC4MibCounter2_Type()
)
mc2200_GEMC4MibCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter2.setStatus("current")
_Mc2200_GEMC4MibCounter3_Type = Counter64
_Mc2200_GEMC4MibCounter3_Object = MibTableColumn
mc2200_GEMC4MibCounter3 = _Mc2200_GEMC4MibCounter3_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 22),
    _Mc2200_GEMC4MibCounter3_Type()
)
mc2200_GEMC4MibCounter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter3.setStatus("current")
_Mc2200_GEMC4MibCounter4_Type = Counter64
_Mc2200_GEMC4MibCounter4_Object = MibTableColumn
mc2200_GEMC4MibCounter4 = _Mc2200_GEMC4MibCounter4_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 23),
    _Mc2200_GEMC4MibCounter4_Type()
)
mc2200_GEMC4MibCounter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter4.setStatus("current")
_Mc2200_GEMC4MibCounter5_Type = Counter64
_Mc2200_GEMC4MibCounter5_Object = MibTableColumn
mc2200_GEMC4MibCounter5 = _Mc2200_GEMC4MibCounter5_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 24),
    _Mc2200_GEMC4MibCounter5_Type()
)
mc2200_GEMC4MibCounter5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter5.setStatus("current")
_Mc2200_GEMC4MibCounter6_Type = Counter64
_Mc2200_GEMC4MibCounter6_Object = MibTableColumn
mc2200_GEMC4MibCounter6 = _Mc2200_GEMC4MibCounter6_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 25),
    _Mc2200_GEMC4MibCounter6_Type()
)
mc2200_GEMC4MibCounter6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter6.setStatus("current")
_Mc2200_GEMC4MibCounter7_Type = Counter64
_Mc2200_GEMC4MibCounter7_Object = MibTableColumn
mc2200_GEMC4MibCounter7 = _Mc2200_GEMC4MibCounter7_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 26),
    _Mc2200_GEMC4MibCounter7_Type()
)
mc2200_GEMC4MibCounter7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter7.setStatus("current")
_Mc2200_GEMC4MibCounter8_Type = Counter64
_Mc2200_GEMC4MibCounter8_Object = MibTableColumn
mc2200_GEMC4MibCounter8 = _Mc2200_GEMC4MibCounter8_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 27),
    _Mc2200_GEMC4MibCounter8_Type()
)
mc2200_GEMC4MibCounter8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter8.setStatus("current")
_Mc2200_GEMC4MibCounter9_Type = Counter64
_Mc2200_GEMC4MibCounter9_Object = MibTableColumn
mc2200_GEMC4MibCounter9 = _Mc2200_GEMC4MibCounter9_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 28),
    _Mc2200_GEMC4MibCounter9_Type()
)
mc2200_GEMC4MibCounter9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter9.setStatus("current")
_Mc2200_GEMC4MibCounter10_Type = Counter64
_Mc2200_GEMC4MibCounter10_Object = MibTableColumn
mc2200_GEMC4MibCounter10 = _Mc2200_GEMC4MibCounter10_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 29),
    _Mc2200_GEMC4MibCounter10_Type()
)
mc2200_GEMC4MibCounter10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter10.setStatus("current")
_Mc2200_GEMC4MibCounter11_Type = Counter64
_Mc2200_GEMC4MibCounter11_Object = MibTableColumn
mc2200_GEMC4MibCounter11 = _Mc2200_GEMC4MibCounter11_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 30),
    _Mc2200_GEMC4MibCounter11_Type()
)
mc2200_GEMC4MibCounter11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter11.setStatus("current")
_Mc2200_GEMC4MibCounter12_Type = Counter64
_Mc2200_GEMC4MibCounter12_Object = MibTableColumn
mc2200_GEMC4MibCounter12 = _Mc2200_GEMC4MibCounter12_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 31),
    _Mc2200_GEMC4MibCounter12_Type()
)
mc2200_GEMC4MibCounter12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter12.setStatus("current")
_Mc2200_GEMC4MibCounter13_Type = Counter64
_Mc2200_GEMC4MibCounter13_Object = MibTableColumn
mc2200_GEMC4MibCounter13 = _Mc2200_GEMC4MibCounter13_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 32),
    _Mc2200_GEMC4MibCounter13_Type()
)
mc2200_GEMC4MibCounter13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter13.setStatus("current")
_Mc2200_GEMC4MibCounter14_Type = Counter64
_Mc2200_GEMC4MibCounter14_Object = MibTableColumn
mc2200_GEMC4MibCounter14 = _Mc2200_GEMC4MibCounter14_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 33),
    _Mc2200_GEMC4MibCounter14_Type()
)
mc2200_GEMC4MibCounter14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter14.setStatus("current")
_Mc2200_GEMC4MibCounter15_Type = Counter64
_Mc2200_GEMC4MibCounter15_Object = MibTableColumn
mc2200_GEMC4MibCounter15 = _Mc2200_GEMC4MibCounter15_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 34),
    _Mc2200_GEMC4MibCounter15_Type()
)
mc2200_GEMC4MibCounter15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter15.setStatus("current")
_Mc2200_GEMC4MibCounter16_Type = Counter64
_Mc2200_GEMC4MibCounter16_Object = MibTableColumn
mc2200_GEMC4MibCounter16 = _Mc2200_GEMC4MibCounter16_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 35),
    _Mc2200_GEMC4MibCounter16_Type()
)
mc2200_GEMC4MibCounter16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter16.setStatus("current")
_Mc2200_GEMC4MibCounter17_Type = Counter64
_Mc2200_GEMC4MibCounter17_Object = MibTableColumn
mc2200_GEMC4MibCounter17 = _Mc2200_GEMC4MibCounter17_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 36),
    _Mc2200_GEMC4MibCounter17_Type()
)
mc2200_GEMC4MibCounter17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter17.setStatus("current")
_Mc2200_GEMC4MibCounter18_Type = Counter64
_Mc2200_GEMC4MibCounter18_Object = MibTableColumn
mc2200_GEMC4MibCounter18 = _Mc2200_GEMC4MibCounter18_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 37),
    _Mc2200_GEMC4MibCounter18_Type()
)
mc2200_GEMC4MibCounter18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter18.setStatus("current")
_Mc2200_GEMC4MibCounter19_Type = Counter64
_Mc2200_GEMC4MibCounter19_Object = MibTableColumn
mc2200_GEMC4MibCounter19 = _Mc2200_GEMC4MibCounter19_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 38),
    _Mc2200_GEMC4MibCounter19_Type()
)
mc2200_GEMC4MibCounter19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter19.setStatus("current")
_Mc2200_GEMC4MibCounter20_Type = Counter64
_Mc2200_GEMC4MibCounter20_Object = MibTableColumn
mc2200_GEMC4MibCounter20 = _Mc2200_GEMC4MibCounter20_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 39),
    _Mc2200_GEMC4MibCounter20_Type()
)
mc2200_GEMC4MibCounter20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter20.setStatus("current")
_Mc2200_GEMC4MibCounter21_Type = Counter64
_Mc2200_GEMC4MibCounter21_Object = MibTableColumn
mc2200_GEMC4MibCounter21 = _Mc2200_GEMC4MibCounter21_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 40),
    _Mc2200_GEMC4MibCounter21_Type()
)
mc2200_GEMC4MibCounter21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter21.setStatus("current")
_Mc2200_GEMC4MibCounter22_Type = Counter64
_Mc2200_GEMC4MibCounter22_Object = MibTableColumn
mc2200_GEMC4MibCounter22 = _Mc2200_GEMC4MibCounter22_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 41),
    _Mc2200_GEMC4MibCounter22_Type()
)
mc2200_GEMC4MibCounter22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter22.setStatus("current")
_Mc2200_GEMC4MibCounter23_Type = Counter64
_Mc2200_GEMC4MibCounter23_Object = MibTableColumn
mc2200_GEMC4MibCounter23 = _Mc2200_GEMC4MibCounter23_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 42),
    _Mc2200_GEMC4MibCounter23_Type()
)
mc2200_GEMC4MibCounter23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter23.setStatus("current")
_Mc2200_GEMC4MibCounter24_Type = Counter64
_Mc2200_GEMC4MibCounter24_Object = MibTableColumn
mc2200_GEMC4MibCounter24 = _Mc2200_GEMC4MibCounter24_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 43),
    _Mc2200_GEMC4MibCounter24_Type()
)
mc2200_GEMC4MibCounter24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter24.setStatus("current")
_Mc2200_GEMC4MibCounter25_Type = Counter64
_Mc2200_GEMC4MibCounter25_Object = MibTableColumn
mc2200_GEMC4MibCounter25 = _Mc2200_GEMC4MibCounter25_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 44),
    _Mc2200_GEMC4MibCounter25_Type()
)
mc2200_GEMC4MibCounter25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter25.setStatus("current")
_Mc2200_GEMC4MibCounter26_Type = Counter64
_Mc2200_GEMC4MibCounter26_Object = MibTableColumn
mc2200_GEMC4MibCounter26 = _Mc2200_GEMC4MibCounter26_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 45),
    _Mc2200_GEMC4MibCounter26_Type()
)
mc2200_GEMC4MibCounter26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter26.setStatus("current")
_Mc2200_GEMC4MibCounter27_Type = Counter64
_Mc2200_GEMC4MibCounter27_Object = MibTableColumn
mc2200_GEMC4MibCounter27 = _Mc2200_GEMC4MibCounter27_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 46),
    _Mc2200_GEMC4MibCounter27_Type()
)
mc2200_GEMC4MibCounter27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter27.setStatus("current")
_Mc2200_GEMC4MibCounter28_Type = Counter64
_Mc2200_GEMC4MibCounter28_Object = MibTableColumn
mc2200_GEMC4MibCounter28 = _Mc2200_GEMC4MibCounter28_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 47),
    _Mc2200_GEMC4MibCounter28_Type()
)
mc2200_GEMC4MibCounter28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter28.setStatus("current")
_Mc2200_GEMC4MibCounter29_Type = Counter64
_Mc2200_GEMC4MibCounter29_Object = MibTableColumn
mc2200_GEMC4MibCounter29 = _Mc2200_GEMC4MibCounter29_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 48),
    _Mc2200_GEMC4MibCounter29_Type()
)
mc2200_GEMC4MibCounter29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter29.setStatus("current")
_Mc2200_GEMC4MibCounter30_Type = Counter64
_Mc2200_GEMC4MibCounter30_Object = MibTableColumn
mc2200_GEMC4MibCounter30 = _Mc2200_GEMC4MibCounter30_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 49),
    _Mc2200_GEMC4MibCounter30_Type()
)
mc2200_GEMC4MibCounter30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter30.setStatus("current")
_Mc2200_GEMC4MibCounter31_Type = Counter64
_Mc2200_GEMC4MibCounter31_Object = MibTableColumn
mc2200_GEMC4MibCounter31 = _Mc2200_GEMC4MibCounter31_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 50),
    _Mc2200_GEMC4MibCounter31_Type()
)
mc2200_GEMC4MibCounter31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter31.setStatus("current")
_Mc2200_GEMC4MibCounter32_Type = Counter64
_Mc2200_GEMC4MibCounter32_Object = MibTableColumn
mc2200_GEMC4MibCounter32 = _Mc2200_GEMC4MibCounter32_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 51),
    _Mc2200_GEMC4MibCounter32_Type()
)
mc2200_GEMC4MibCounter32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4MibCounter32.setStatus("current")
_Mc2200_GEMC4RemoteLAN1SFPInfo_Type = DisplayString
_Mc2200_GEMC4RemoteLAN1SFPInfo_Object = MibTableColumn
mc2200_GEMC4RemoteLAN1SFPInfo = _Mc2200_GEMC4RemoteLAN1SFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 52),
    _Mc2200_GEMC4RemoteLAN1SFPInfo_Type()
)
mc2200_GEMC4RemoteLAN1SFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4RemoteLAN1SFPInfo.setStatus("current")


class _Mc2200_GEMC4RemoteLAN1Link_Type(Integer32):
    """Custom type mc2200_GEMC4RemoteLAN1Link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-remotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_GEMC4RemoteLAN1Link_Type.__name__ = "Integer32"
_Mc2200_GEMC4RemoteLAN1Link_Object = MibTableColumn
mc2200_GEMC4RemoteLAN1Link = _Mc2200_GEMC4RemoteLAN1Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 53),
    _Mc2200_GEMC4RemoteLAN1Link_Type()
)
mc2200_GEMC4RemoteLAN1Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4RemoteLAN1Link.setStatus("mandatory")
_Mc2200_GEMC4RemoteLAN2SFPInfo_Type = DisplayString
_Mc2200_GEMC4RemoteLAN2SFPInfo_Object = MibTableColumn
mc2200_GEMC4RemoteLAN2SFPInfo = _Mc2200_GEMC4RemoteLAN2SFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 54),
    _Mc2200_GEMC4RemoteLAN2SFPInfo_Type()
)
mc2200_GEMC4RemoteLAN2SFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4RemoteLAN2SFPInfo.setStatus("current")


class _Mc2200_GEMC4RemoteLAN2Link_Type(Integer32):
    """Custom type mc2200_GEMC4RemoteLAN2Link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-remotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_GEMC4RemoteLAN2Link_Type.__name__ = "Integer32"
_Mc2200_GEMC4RemoteLAN2Link_Object = MibTableColumn
mc2200_GEMC4RemoteLAN2Link = _Mc2200_GEMC4RemoteLAN2Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 55),
    _Mc2200_GEMC4RemoteLAN2Link_Type()
)
mc2200_GEMC4RemoteLAN2Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4RemoteLAN2Link.setStatus("mandatory")
_Mc2200_GEMC4RemoteWAN1SFPInfo_Type = DisplayString
_Mc2200_GEMC4RemoteWAN1SFPInfo_Object = MibTableColumn
mc2200_GEMC4RemoteWAN1SFPInfo = _Mc2200_GEMC4RemoteWAN1SFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 56),
    _Mc2200_GEMC4RemoteWAN1SFPInfo_Type()
)
mc2200_GEMC4RemoteWAN1SFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4RemoteWAN1SFPInfo.setStatus("current")


class _Mc2200_GEMC4RemoteWAN1Link_Type(Integer32):
    """Custom type mc2200_GEMC4RemoteWAN1Link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("no-remotecard", 0),
          ("up", 1),
          ("down", 2),
          ("active", 3),
          ("standby", 4))
    )


_Mc2200_GEMC4RemoteWAN1Link_Type.__name__ = "Integer32"
_Mc2200_GEMC4RemoteWAN1Link_Object = MibTableColumn
mc2200_GEMC4RemoteWAN1Link = _Mc2200_GEMC4RemoteWAN1Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 57),
    _Mc2200_GEMC4RemoteWAN1Link_Type()
)
mc2200_GEMC4RemoteWAN1Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4RemoteWAN1Link.setStatus("mandatory")
_Mc2200_GEMC4RemoteWAN2LAN3SFPInfo_Type = DisplayString
_Mc2200_GEMC4RemoteWAN2LAN3SFPInfo_Object = MibTableColumn
mc2200_GEMC4RemoteWAN2LAN3SFPInfo = _Mc2200_GEMC4RemoteWAN2LAN3SFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 58),
    _Mc2200_GEMC4RemoteWAN2LAN3SFPInfo_Type()
)
mc2200_GEMC4RemoteWAN2LAN3SFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4RemoteWAN2LAN3SFPInfo.setStatus("current")


class _Mc2200_GEMC4RemoteWAN2LAN3Link_Type(Integer32):
    """Custom type mc2200_GEMC4RemoteWAN2LAN3Link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("no-remotecard", 0),
          ("up", 1),
          ("down", 2),
          ("active", 3),
          ("standby", 4))
    )


_Mc2200_GEMC4RemoteWAN2LAN3Link_Type.__name__ = "Integer32"
_Mc2200_GEMC4RemoteWAN2LAN3Link_Object = MibTableColumn
mc2200_GEMC4RemoteWAN2LAN3Link = _Mc2200_GEMC4RemoteWAN2LAN3Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 59),
    _Mc2200_GEMC4RemoteWAN2LAN3Link_Type()
)
mc2200_GEMC4RemoteWAN2LAN3Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4RemoteWAN2LAN3Link.setStatus("mandatory")


class _Mc2200_GEMC4RemoteLAN1Mode_Type(Integer32):
    """Custom type mc2200_GEMC4RemoteLAN1Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("no-remotecard", 0),
          ("auto-10-100-1000T", 1),
          ("mode1000Base-X-auto", 2),
          ("mode1000Base-T", 3),
          ("mode100Base-Tx", 4),
          ("mode10Base-T", 5),
          ("mode1000Base-X-1000F", 6))
    )


_Mc2200_GEMC4RemoteLAN1Mode_Type.__name__ = "Integer32"
_Mc2200_GEMC4RemoteLAN1Mode_Object = MibTableColumn
mc2200_GEMC4RemoteLAN1Mode = _Mc2200_GEMC4RemoteLAN1Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 60),
    _Mc2200_GEMC4RemoteLAN1Mode_Type()
)
mc2200_GEMC4RemoteLAN1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4RemoteLAN1Mode.setStatus("current")


class _Mc2200_GEMC4RemoteLAN2Mode_Type(Integer32):
    """Custom type mc2200_GEMC4RemoteLAN2Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("no-remotecard", 0),
          ("auto-10-100-1000T", 1),
          ("mode1000Base-X-auto", 2),
          ("mode1000Base-T", 3),
          ("mode100Base-Tx", 4),
          ("mode10Base-T", 5),
          ("mode1000Base-X-1000F", 6))
    )


_Mc2200_GEMC4RemoteLAN2Mode_Type.__name__ = "Integer32"
_Mc2200_GEMC4RemoteLAN2Mode_Object = MibTableColumn
mc2200_GEMC4RemoteLAN2Mode = _Mc2200_GEMC4RemoteLAN2Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 61),
    _Mc2200_GEMC4RemoteLAN2Mode_Type()
)
mc2200_GEMC4RemoteLAN2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4RemoteLAN2Mode.setStatus("current")


class _Mc2200_GEMC4RemoteLAN3Mode_Type(Integer32):
    """Custom type mc2200_GEMC4RemoteLAN3Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("no-remotecard", 0),
          ("auto-10-100-1000T", 1),
          ("mode1000Base-X-auto", 2),
          ("mode1000Base-T", 3),
          ("mode100Base-Tx", 4),
          ("mode10Base-T", 5),
          ("mode1000Base-X-1000F", 6))
    )


_Mc2200_GEMC4RemoteLAN3Mode_Type.__name__ = "Integer32"
_Mc2200_GEMC4RemoteLAN3Mode_Object = MibTableColumn
mc2200_GEMC4RemoteLAN3Mode = _Mc2200_GEMC4RemoteLAN3Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 62),
    _Mc2200_GEMC4RemoteLAN3Mode_Type()
)
mc2200_GEMC4RemoteLAN3Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4RemoteLAN3Mode.setStatus("current")
_Mc2200_GEMC4RemoteIPAddress_Type = IpAddress
_Mc2200_GEMC4RemoteIPAddress_Object = MibTableColumn
mc2200_GEMC4RemoteIPAddress = _Mc2200_GEMC4RemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 63),
    _Mc2200_GEMC4RemoteIPAddress_Type()
)
mc2200_GEMC4RemoteIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4RemoteIPAddress.setStatus("mandatory")
_Mc2200_GEMC4RemoteSubnetMask_Type = IpAddress
_Mc2200_GEMC4RemoteSubnetMask_Object = MibTableColumn
mc2200_GEMC4RemoteSubnetMask = _Mc2200_GEMC4RemoteSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 64),
    _Mc2200_GEMC4RemoteSubnetMask_Type()
)
mc2200_GEMC4RemoteSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4RemoteSubnetMask.setStatus("mandatory")
_Mc2200_GEMC4RemoteGateWay_Type = IpAddress
_Mc2200_GEMC4RemoteGateWay_Object = MibTableColumn
mc2200_GEMC4RemoteGateWay = _Mc2200_GEMC4RemoteGateWay_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 65),
    _Mc2200_GEMC4RemoteGateWay_Type()
)
mc2200_GEMC4RemoteGateWay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4RemoteGateWay.setStatus("mandatory")


class _Mc2200_GEMC4RemoteVLANEnable_Type(Integer32):
    """Custom type mc2200_GEMC4RemoteVLANEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-remotecard", 0),
          ("enable", 1),
          ("disable", 2))
    )


_Mc2200_GEMC4RemoteVLANEnable_Type.__name__ = "Integer32"
_Mc2200_GEMC4RemoteVLANEnable_Object = MibTableColumn
mc2200_GEMC4RemoteVLANEnable = _Mc2200_GEMC4RemoteVLANEnable_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 66),
    _Mc2200_GEMC4RemoteVLANEnable_Type()
)
mc2200_GEMC4RemoteVLANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4RemoteVLANEnable.setStatus("mandatory")
_Mc2200_GEMC4RemoteVID_Type = Integer32
_Mc2200_GEMC4RemoteVID_Object = MibTableColumn
mc2200_GEMC4RemoteVID = _Mc2200_GEMC4RemoteVID_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 67),
    _Mc2200_GEMC4RemoteVID_Type()
)
mc2200_GEMC4RemoteVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4RemoteVID.setStatus("mandatory")


class _Mc2200_GEMC4RemoteAlarm_Type(Integer32):
    """Custom type mc2200_GEMC4RemoteAlarm based on Integer32"""
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


_Mc2200_GEMC4RemoteAlarm_Type.__name__ = "Integer32"
_Mc2200_GEMC4RemoteAlarm_Object = MibTableColumn
mc2200_GEMC4RemoteAlarm = _Mc2200_GEMC4RemoteAlarm_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 68),
    _Mc2200_GEMC4RemoteAlarm_Type()
)
mc2200_GEMC4RemoteAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4RemoteAlarm.setStatus("current")


class _Mc2200_GEMC4RFD_Type(Integer32):
    """Custom type mc2200_GEMC4RFD based on Integer32"""
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


_Mc2200_GEMC4RFD_Type.__name__ = "Integer32"
_Mc2200_GEMC4RFD_Object = MibTableColumn
mc2200_GEMC4RFD = _Mc2200_GEMC4RFD_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 69),
    _Mc2200_GEMC4RFD_Type()
)
mc2200_GEMC4RFD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4RFD.setStatus("current")
_Mc2200_GEMC4Default_Type = Integer32
_Mc2200_GEMC4Default_Object = MibTableColumn
mc2200_GEMC4Default = _Mc2200_GEMC4Default_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 70),
    _Mc2200_GEMC4Default_Type()
)
mc2200_GEMC4Default.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4Default.setStatus("current")
_Mc2200_GEMC4Reboot_Type = Integer32
_Mc2200_GEMC4Reboot_Object = MibTableColumn
mc2200_GEMC4Reboot = _Mc2200_GEMC4Reboot_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 71),
    _Mc2200_GEMC4Reboot_Type()
)
mc2200_GEMC4Reboot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4Reboot.setStatus("current")


class _Mc2200_GEMC4LocalCardREMOTEMODE_Type(Integer32):
    """Custom type mc2200_GEMC4LocalCardREMOTEMODE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("remoteModeEnabled", 1),
          ("remoteMode-Disabled", 2),
          ("no-Setting", 3))
    )


_Mc2200_GEMC4LocalCardREMOTEMODE_Type.__name__ = "Integer32"
_Mc2200_GEMC4LocalCardREMOTEMODE_Object = MibTableColumn
mc2200_GEMC4LocalCardREMOTEMODE = _Mc2200_GEMC4LocalCardREMOTEMODE_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 72),
    _Mc2200_GEMC4LocalCardREMOTEMODE_Type()
)
mc2200_GEMC4LocalCardREMOTEMODE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4LocalCardREMOTEMODE.setStatus("current")


class _Mc2200_GEMC4LocalLAN1Speed_Type(Integer32):
    """Custom type mc2200_GEMC4LocalLAN1Speed based on Integer32"""
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
        *(("speed1000M", 1),
          ("speed100M", 2),
          ("speed10M", 3),
          ("down", 4))
    )


_Mc2200_GEMC4LocalLAN1Speed_Type.__name__ = "Integer32"
_Mc2200_GEMC4LocalLAN1Speed_Object = MibTableColumn
mc2200_GEMC4LocalLAN1Speed = _Mc2200_GEMC4LocalLAN1Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 73),
    _Mc2200_GEMC4LocalLAN1Speed_Type()
)
mc2200_GEMC4LocalLAN1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4LocalLAN1Speed.setStatus("mandatory")


class _Mc2200_GEMC4LocalLAN2Speed_Type(Integer32):
    """Custom type mc2200_GEMC4LocalLAN2Speed based on Integer32"""
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
        *(("speed1000M", 1),
          ("speed100M", 2),
          ("speed10M", 3),
          ("down", 4))
    )


_Mc2200_GEMC4LocalLAN2Speed_Type.__name__ = "Integer32"
_Mc2200_GEMC4LocalLAN2Speed_Object = MibTableColumn
mc2200_GEMC4LocalLAN2Speed = _Mc2200_GEMC4LocalLAN2Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 74),
    _Mc2200_GEMC4LocalLAN2Speed_Type()
)
mc2200_GEMC4LocalLAN2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4LocalLAN2Speed.setStatus("mandatory")


class _Mc2200_GEMC4LocalWAN2LAN3Speed_Type(Integer32):
    """Custom type mc2200_GEMC4LocalWAN2LAN3Speed based on Integer32"""
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
        *(("speed1000M", 1),
          ("speed100M", 2),
          ("speed10M", 3),
          ("down", 4))
    )


_Mc2200_GEMC4LocalWAN2LAN3Speed_Type.__name__ = "Integer32"
_Mc2200_GEMC4LocalWAN2LAN3Speed_Object = MibTableColumn
mc2200_GEMC4LocalWAN2LAN3Speed = _Mc2200_GEMC4LocalWAN2LAN3Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 75),
    _Mc2200_GEMC4LocalWAN2LAN3Speed_Type()
)
mc2200_GEMC4LocalWAN2LAN3Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4LocalWAN2LAN3Speed.setStatus("mandatory")


class _Mc2200_GEMC4RemoteLAN1Speed_Type(Integer32):
    """Custom type mc2200_GEMC4RemoteLAN1Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("no-remotecard", 0),
          ("speed1000M", 1),
          ("speed100M", 2),
          ("speed10M", 3),
          ("down", 4))
    )


_Mc2200_GEMC4RemoteLAN1Speed_Type.__name__ = "Integer32"
_Mc2200_GEMC4RemoteLAN1Speed_Object = MibTableColumn
mc2200_GEMC4RemoteLAN1Speed = _Mc2200_GEMC4RemoteLAN1Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 76),
    _Mc2200_GEMC4RemoteLAN1Speed_Type()
)
mc2200_GEMC4RemoteLAN1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4RemoteLAN1Speed.setStatus("mandatory")


class _Mc2200_GEMC4RemoteLAN2Speed_Type(Integer32):
    """Custom type mc2200_GEMC4RemoteLAN2Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("no-remotecard", 0),
          ("speed1000M", 1),
          ("speed100M", 2),
          ("speed10M", 3),
          ("down", 4))
    )


_Mc2200_GEMC4RemoteLAN2Speed_Type.__name__ = "Integer32"
_Mc2200_GEMC4RemoteLAN2Speed_Object = MibTableColumn
mc2200_GEMC4RemoteLAN2Speed = _Mc2200_GEMC4RemoteLAN2Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 77),
    _Mc2200_GEMC4RemoteLAN2Speed_Type()
)
mc2200_GEMC4RemoteLAN2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4RemoteLAN2Speed.setStatus("mandatory")


class _Mc2200_GEMC4RemoteWAN2LAN3Speed_Type(Integer32):
    """Custom type mc2200_GEMC4RemoteWAN2LAN3Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("no-remotecard", 0),
          ("speed1000M", 1),
          ("speed100M", 2),
          ("speed10M", 3),
          ("down", 4))
    )


_Mc2200_GEMC4RemoteWAN2LAN3Speed_Type.__name__ = "Integer32"
_Mc2200_GEMC4RemoteWAN2LAN3Speed_Object = MibTableColumn
mc2200_GEMC4RemoteWAN2LAN3Speed = _Mc2200_GEMC4RemoteWAN2LAN3Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 78),
    _Mc2200_GEMC4RemoteWAN2LAN3Speed_Type()
)
mc2200_GEMC4RemoteWAN2LAN3Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC4RemoteWAN2LAN3Speed.setStatus("mandatory")


class _Mc2200_GEMC4APSActivePort_Type(Integer32):
    """Custom type mc2200_GEMC4APSActivePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wan1", 1),
          ("wan2-lan3", 2),
          ("no-support-atciveport", 3))
    )


_Mc2200_GEMC4APSActivePort_Type.__name__ = "Integer32"
_Mc2200_GEMC4APSActivePort_Object = MibTableColumn
mc2200_GEMC4APSActivePort = _Mc2200_GEMC4APSActivePort_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 79),
    _Mc2200_GEMC4APSActivePort_Type()
)
mc2200_GEMC4APSActivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4APSActivePort.setStatus("current")
_Mc2200_GEMC4Localportuser1_Type = DisplayString
_Mc2200_GEMC4Localportuser1_Object = MibTableColumn
mc2200_GEMC4Localportuser1 = _Mc2200_GEMC4Localportuser1_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 80),
    _Mc2200_GEMC4Localportuser1_Type()
)
mc2200_GEMC4Localportuser1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4Localportuser1.setStatus("current")
_Mc2200_GEMC4Localportuser2_Type = DisplayString
_Mc2200_GEMC4Localportuser2_Object = MibTableColumn
mc2200_GEMC4Localportuser2 = _Mc2200_GEMC4Localportuser2_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 81),
    _Mc2200_GEMC4Localportuser2_Type()
)
mc2200_GEMC4Localportuser2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4Localportuser2.setStatus("current")
_Mc2200_GEMC4Localportuser3_Type = DisplayString
_Mc2200_GEMC4Localportuser3_Object = MibTableColumn
mc2200_GEMC4Localportuser3 = _Mc2200_GEMC4Localportuser3_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 82),
    _Mc2200_GEMC4Localportuser3_Type()
)
mc2200_GEMC4Localportuser3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4Localportuser3.setStatus("current")
_Mc2200_GEMC4Remoteportuser1_Type = DisplayString
_Mc2200_GEMC4Remoteportuser1_Object = MibTableColumn
mc2200_GEMC4Remoteportuser1 = _Mc2200_GEMC4Remoteportuser1_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 83),
    _Mc2200_GEMC4Remoteportuser1_Type()
)
mc2200_GEMC4Remoteportuser1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4Remoteportuser1.setStatus("current")
_Mc2200_GEMC4Remoteportuser2_Type = DisplayString
_Mc2200_GEMC4Remoteportuser2_Object = MibTableColumn
mc2200_GEMC4Remoteportuser2 = _Mc2200_GEMC4Remoteportuser2_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 84),
    _Mc2200_GEMC4Remoteportuser2_Type()
)
mc2200_GEMC4Remoteportuser2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4Remoteportuser2.setStatus("current")
_Mc2200_GEMC4Remoteportuser3_Type = DisplayString
_Mc2200_GEMC4Remoteportuser3_Object = MibTableColumn
mc2200_GEMC4Remoteportuser3 = _Mc2200_GEMC4Remoteportuser3_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 85),
    _Mc2200_GEMC4Remoteportuser3_Type()
)
mc2200_GEMC4Remoteportuser3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4Remoteportuser3.setStatus("current")


class _Mc2200_GEMC4TrapFilterLocalLAN_Type(Integer32):
    """Custom type mc2200_GEMC4TrapFilterLocalLAN based on Integer32"""
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


_Mc2200_GEMC4TrapFilterLocalLAN_Type.__name__ = "Integer32"
_Mc2200_GEMC4TrapFilterLocalLAN_Object = MibTableColumn
mc2200_GEMC4TrapFilterLocalLAN = _Mc2200_GEMC4TrapFilterLocalLAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 86),
    _Mc2200_GEMC4TrapFilterLocalLAN_Type()
)
mc2200_GEMC4TrapFilterLocalLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4TrapFilterLocalLAN.setStatus("current")


class _Mc2200_GEMC4TrapFilterLocalWAN_Type(Integer32):
    """Custom type mc2200_GEMC4TrapFilterLocalWAN based on Integer32"""
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


_Mc2200_GEMC4TrapFilterLocalWAN_Type.__name__ = "Integer32"
_Mc2200_GEMC4TrapFilterLocalWAN_Object = MibTableColumn
mc2200_GEMC4TrapFilterLocalWAN = _Mc2200_GEMC4TrapFilterLocalWAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 87),
    _Mc2200_GEMC4TrapFilterLocalWAN_Type()
)
mc2200_GEMC4TrapFilterLocalWAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4TrapFilterLocalWAN.setStatus("current")


class _Mc2200_GEMC4TrapFilterRemotePower_Type(Integer32):
    """Custom type mc2200_GEMC4TrapFilterRemotePower based on Integer32"""
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


_Mc2200_GEMC4TrapFilterRemotePower_Type.__name__ = "Integer32"
_Mc2200_GEMC4TrapFilterRemotePower_Object = MibTableColumn
mc2200_GEMC4TrapFilterRemotePower = _Mc2200_GEMC4TrapFilterRemotePower_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 88),
    _Mc2200_GEMC4TrapFilterRemotePower_Type()
)
mc2200_GEMC4TrapFilterRemotePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4TrapFilterRemotePower.setStatus("current")


class _Mc2200_GEMC4TrapFilterRemoteLAN_Type(Integer32):
    """Custom type mc2200_GEMC4TrapFilterRemoteLAN based on Integer32"""
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


_Mc2200_GEMC4TrapFilterRemoteLAN_Type.__name__ = "Integer32"
_Mc2200_GEMC4TrapFilterRemoteLAN_Object = MibTableColumn
mc2200_GEMC4TrapFilterRemoteLAN = _Mc2200_GEMC4TrapFilterRemoteLAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 89),
    _Mc2200_GEMC4TrapFilterRemoteLAN_Type()
)
mc2200_GEMC4TrapFilterRemoteLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4TrapFilterRemoteLAN.setStatus("current")


class _Mc2200_GEMC4TrapFilterRemoteWAN_Type(Integer32):
    """Custom type mc2200_GEMC4TrapFilterRemoteWAN based on Integer32"""
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


_Mc2200_GEMC4TrapFilterRemoteWAN_Type.__name__ = "Integer32"
_Mc2200_GEMC4TrapFilterRemoteWAN_Object = MibTableColumn
mc2200_GEMC4TrapFilterRemoteWAN = _Mc2200_GEMC4TrapFilterRemoteWAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 5, 1, 90),
    _Mc2200_GEMC4TrapFilterRemoteWAN_Type()
)
mc2200_GEMC4TrapFilterRemoteWAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC4TrapFilterRemoteWAN.setStatus("current")
_Mc2200_GEMC2Table_Object = MibTable
mc2200_GEMC2Table = _Mc2200_GEMC2Table_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6)
)
if mibBuilder.loadTexts:
    mc2200_GEMC2Table.setStatus("current")
_Mc2200_GEMC2Entry_Object = MibTableRow
mc2200_GEMC2Entry = _Mc2200_GEMC2Entry_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1)
)
mc2200_GEMC2Entry.setIndexNames(
    (0, "OnAccess2200-MIB", "mc2200-GEMC2CardIndex"),
)
if mibBuilder.loadTexts:
    mc2200_GEMC2Entry.setStatus("current")


class _Mc2200_GEMC2CardIndex_Type(Integer32):
    """Custom type mc2200_GEMC2CardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("card01", 1),
          ("card02", 2),
          ("card03", 3),
          ("card04", 4),
          ("card05", 5),
          ("card06", 6),
          ("card07", 7),
          ("card08", 8),
          ("card09", 9),
          ("card10", 10),
          ("card11", 11),
          ("card12", 12),
          ("card13", 13),
          ("card14", 14),
          ("card15", 15))
    )


_Mc2200_GEMC2CardIndex_Type.__name__ = "Integer32"
_Mc2200_GEMC2CardIndex_Object = MibTableColumn
mc2200_GEMC2CardIndex = _Mc2200_GEMC2CardIndex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 2),
    _Mc2200_GEMC2CardIndex_Type()
)
mc2200_GEMC2CardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2CardIndex.setStatus("current")
_Mc2200_GEMC2LocalLANSFPInfo_Type = DisplayString
_Mc2200_GEMC2LocalLANSFPInfo_Object = MibTableColumn
mc2200_GEMC2LocalLANSFPInfo = _Mc2200_GEMC2LocalLANSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 3),
    _Mc2200_GEMC2LocalLANSFPInfo_Type()
)
mc2200_GEMC2LocalLANSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2LocalLANSFPInfo.setStatus("current")


class _Mc2200_GEMC2LocalLANLink_Type(Integer32):
    """Custom type mc2200_GEMC2LocalLANLink based on Integer32"""
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


_Mc2200_GEMC2LocalLANLink_Type.__name__ = "Integer32"
_Mc2200_GEMC2LocalLANLink_Object = MibTableColumn
mc2200_GEMC2LocalLANLink = _Mc2200_GEMC2LocalLANLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 4),
    _Mc2200_GEMC2LocalLANLink_Type()
)
mc2200_GEMC2LocalLANLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2LocalLANLink.setStatus("mandatory")
_Mc2200_GEMC2LocalWANSFPInfo_Type = DisplayString
_Mc2200_GEMC2LocalWANSFPInfo_Object = MibTableColumn
mc2200_GEMC2LocalWANSFPInfo = _Mc2200_GEMC2LocalWANSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 5),
    _Mc2200_GEMC2LocalWANSFPInfo_Type()
)
mc2200_GEMC2LocalWANSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2LocalWANSFPInfo.setStatus("current")


class _Mc2200_GEMC2LocalWANLink_Type(Integer32):
    """Custom type mc2200_GEMC2LocalWANLink based on Integer32"""
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


_Mc2200_GEMC2LocalWANLink_Type.__name__ = "Integer32"
_Mc2200_GEMC2LocalWANLink_Object = MibTableColumn
mc2200_GEMC2LocalWANLink = _Mc2200_GEMC2LocalWANLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 6),
    _Mc2200_GEMC2LocalWANLink_Type()
)
mc2200_GEMC2LocalWANLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2LocalWANLink.setStatus("current")


class _Mc2200_GEMC2LocalLANDownStreamBW_Type(Integer32):
    """Custom type mc2200_GEMC2LocalLANDownStreamBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              30,
              40,
              50,
              60,
              70,
              80,
              90,
              100,
              150,
              200,
              250,
              300,
              350,
              400,
              450,
              500,
              550,
              600,
              650,
              700,
              750,
              800,
              850,
              900,
              950,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("rate10M", 10),
          ("rate20M", 20),
          ("rate30M", 30),
          ("rate40M", 40),
          ("rate50M", 50),
          ("rate60M", 60),
          ("rate70M", 70),
          ("rate80M", 80),
          ("rate90M", 90),
          ("rate100M", 100),
          ("rate150M", 150),
          ("rate200M", 200),
          ("rate250M", 250),
          ("rate300M", 300),
          ("rate350M", 350),
          ("rate400M", 400),
          ("rate450M", 450),
          ("rate500M", 500),
          ("rate550M", 550),
          ("rate600M", 600),
          ("rate650M", 650),
          ("rate700M", 700),
          ("rate750M", 750),
          ("rate800M", 800),
          ("rate850M", 850),
          ("rate900M", 900),
          ("rate950M", 950),
          ("rate1000M", 1000))
    )


_Mc2200_GEMC2LocalLANDownStreamBW_Type.__name__ = "Integer32"
_Mc2200_GEMC2LocalLANDownStreamBW_Object = MibTableColumn
mc2200_GEMC2LocalLANDownStreamBW = _Mc2200_GEMC2LocalLANDownStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 7),
    _Mc2200_GEMC2LocalLANDownStreamBW_Type()
)
mc2200_GEMC2LocalLANDownStreamBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC2LocalLANDownStreamBW.setStatus("current")


class _Mc2200_GEMC2LocalLANUpStreamBW_Type(Integer32):
    """Custom type mc2200_GEMC2LocalLANUpStreamBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              30,
              40,
              50,
              60,
              70,
              80,
              90,
              100,
              150,
              200,
              250,
              300,
              350,
              400,
              450,
              500,
              550,
              600,
              650,
              700,
              750,
              800,
              850,
              900,
              950,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("rate10M", 10),
          ("rate20M", 20),
          ("rate30M", 30),
          ("rate40M", 40),
          ("rate50M", 50),
          ("rate60M", 60),
          ("rate70M", 70),
          ("rate80M", 80),
          ("rate90M", 90),
          ("rate100M", 100),
          ("rate150M", 150),
          ("rate200M", 200),
          ("rate250M", 250),
          ("rate300M", 300),
          ("rate350M", 350),
          ("rate400M", 400),
          ("rate450M", 450),
          ("rate500M", 500),
          ("rate550M", 550),
          ("rate600M", 600),
          ("rate650M", 650),
          ("rate700M", 700),
          ("rate750M", 750),
          ("rate800M", 800),
          ("rate850M", 850),
          ("rate900M", 900),
          ("rate950M", 950),
          ("rate1000M", 1000))
    )


_Mc2200_GEMC2LocalLANUpStreamBW_Type.__name__ = "Integer32"
_Mc2200_GEMC2LocalLANUpStreamBW_Object = MibTableColumn
mc2200_GEMC2LocalLANUpStreamBW = _Mc2200_GEMC2LocalLANUpStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 8),
    _Mc2200_GEMC2LocalLANUpStreamBW_Type()
)
mc2200_GEMC2LocalLANUpStreamBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC2LocalLANUpStreamBW.setStatus("current")


class _Mc2200_GEMC2LocalLANMode_Type(Integer32):
    """Custom type mc2200_GEMC2LocalLANMode based on Integer32"""
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
        *(("auto-10-100-1000T", 1),
          ("mode1000Base-X-auto", 2),
          ("mode1000Base-T", 3),
          ("mode100Base-Tx", 4),
          ("mode10Base-T", 5),
          ("mode1000Base-X-1000F", 6))
    )


_Mc2200_GEMC2LocalLANMode_Type.__name__ = "Integer32"
_Mc2200_GEMC2LocalLANMode_Object = MibTableColumn
mc2200_GEMC2LocalLANMode = _Mc2200_GEMC2LocalLANMode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 9),
    _Mc2200_GEMC2LocalLANMode_Type()
)
mc2200_GEMC2LocalLANMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC2LocalLANMode.setStatus("current")
_Mc2200_GEMC2RxGoodOctets_Type = Counter64
_Mc2200_GEMC2RxGoodOctets_Object = MibTableColumn
mc2200_GEMC2RxGoodOctets = _Mc2200_GEMC2RxGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 10),
    _Mc2200_GEMC2RxGoodOctets_Type()
)
mc2200_GEMC2RxGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2RxGoodOctets.setStatus("current")
_Mc2200_GEMC2RxBadOctets_Type = Counter64
_Mc2200_GEMC2RxBadOctets_Object = MibTableColumn
mc2200_GEMC2RxBadOctets = _Mc2200_GEMC2RxBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 12),
    _Mc2200_GEMC2RxBadOctets_Type()
)
mc2200_GEMC2RxBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2RxBadOctets.setStatus("current")
_Mc2200_GEMC2TxFCSErr_Type = Counter64
_Mc2200_GEMC2TxFCSErr_Object = MibTableColumn
mc2200_GEMC2TxFCSErr = _Mc2200_GEMC2TxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 13),
    _Mc2200_GEMC2TxFCSErr_Type()
)
mc2200_GEMC2TxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2TxFCSErr.setStatus("current")
_Mc2200_GEMC2RxUnicast_Type = Counter64
_Mc2200_GEMC2RxUnicast_Object = MibTableColumn
mc2200_GEMC2RxUnicast = _Mc2200_GEMC2RxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 14),
    _Mc2200_GEMC2RxUnicast_Type()
)
mc2200_GEMC2RxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2RxUnicast.setStatus("current")
_Mc2200_GEMC2TxDeferred_Type = Counter64
_Mc2200_GEMC2TxDeferred_Object = MibTableColumn
mc2200_GEMC2TxDeferred = _Mc2200_GEMC2TxDeferred_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 15),
    _Mc2200_GEMC2TxDeferred_Type()
)
mc2200_GEMC2TxDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2TxDeferred.setStatus("current")
_Mc2200_GEMC2RxBroadcasts_Type = Counter64
_Mc2200_GEMC2RxBroadcasts_Object = MibTableColumn
mc2200_GEMC2RxBroadcasts = _Mc2200_GEMC2RxBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 16),
    _Mc2200_GEMC2RxBroadcasts_Type()
)
mc2200_GEMC2RxBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2RxBroadcasts.setStatus("current")
_Mc2200_GEMC2RxMulticasts_Type = Counter64
_Mc2200_GEMC2RxMulticasts_Object = MibTableColumn
mc2200_GEMC2RxMulticasts = _Mc2200_GEMC2RxMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 17),
    _Mc2200_GEMC2RxMulticasts_Type()
)
mc2200_GEMC2RxMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2RxMulticasts.setStatus("current")
_Mc2200_GEMC2Rx64Octets_Type = Counter64
_Mc2200_GEMC2Rx64Octets_Object = MibTableColumn
mc2200_GEMC2Rx64Octets = _Mc2200_GEMC2Rx64Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 18),
    _Mc2200_GEMC2Rx64Octets_Type()
)
mc2200_GEMC2Rx64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2Rx64Octets.setStatus("current")
_Mc2200_GEMC2Rx65to127Octets_Type = Counter64
_Mc2200_GEMC2Rx65to127Octets_Object = MibTableColumn
mc2200_GEMC2Rx65to127Octets = _Mc2200_GEMC2Rx65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 19),
    _Mc2200_GEMC2Rx65to127Octets_Type()
)
mc2200_GEMC2Rx65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2Rx65to127Octets.setStatus("current")
_Mc2200_GEMC2Rx128to255Octets_Type = Counter64
_Mc2200_GEMC2Rx128to255Octets_Object = MibTableColumn
mc2200_GEMC2Rx128to255Octets = _Mc2200_GEMC2Rx128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 20),
    _Mc2200_GEMC2Rx128to255Octets_Type()
)
mc2200_GEMC2Rx128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2Rx128to255Octets.setStatus("current")
_Mc2200_GEMC2Rx256to511Octets_Type = Counter64
_Mc2200_GEMC2Rx256to511Octets_Object = MibTableColumn
mc2200_GEMC2Rx256to511Octets = _Mc2200_GEMC2Rx256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 21),
    _Mc2200_GEMC2Rx256to511Octets_Type()
)
mc2200_GEMC2Rx256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2Rx256to511Octets.setStatus("current")
_Mc2200_GEMC2Rx512to1023Octets_Type = Counter64
_Mc2200_GEMC2Rx512to1023Octets_Object = MibTableColumn
mc2200_GEMC2Rx512to1023Octets = _Mc2200_GEMC2Rx512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 22),
    _Mc2200_GEMC2Rx512to1023Octets_Type()
)
mc2200_GEMC2Rx512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2Rx512to1023Octets.setStatus("current")
_Mc2200_GEMC2Rx1024toMaxOctets_Type = Counter64
_Mc2200_GEMC2Rx1024toMaxOctets_Object = MibTableColumn
mc2200_GEMC2Rx1024toMaxOctets = _Mc2200_GEMC2Rx1024toMaxOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 23),
    _Mc2200_GEMC2Rx1024toMaxOctets_Type()
)
mc2200_GEMC2Rx1024toMaxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2Rx1024toMaxOctets.setStatus("current")
_Mc2200_GEMC2TxOctets_Type = Counter64
_Mc2200_GEMC2TxOctets_Object = MibTableColumn
mc2200_GEMC2TxOctets = _Mc2200_GEMC2TxOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 24),
    _Mc2200_GEMC2TxOctets_Type()
)
mc2200_GEMC2TxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2TxOctets.setStatus("current")
_Mc2200_GEMC2TxUnicast_Type = Counter64
_Mc2200_GEMC2TxUnicast_Object = MibTableColumn
mc2200_GEMC2TxUnicast = _Mc2200_GEMC2TxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 26),
    _Mc2200_GEMC2TxUnicast_Type()
)
mc2200_GEMC2TxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2TxUnicast.setStatus("current")
_Mc2200_GEMC2TxExcessive_Type = Counter64
_Mc2200_GEMC2TxExcessive_Object = MibTableColumn
mc2200_GEMC2TxExcessive = _Mc2200_GEMC2TxExcessive_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 27),
    _Mc2200_GEMC2TxExcessive_Type()
)
mc2200_GEMC2TxExcessive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2TxExcessive.setStatus("current")
_Mc2200_GEMC2TxMulticasts_Type = Counter64
_Mc2200_GEMC2TxMulticasts_Object = MibTableColumn
mc2200_GEMC2TxMulticasts = _Mc2200_GEMC2TxMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 28),
    _Mc2200_GEMC2TxMulticasts_Type()
)
mc2200_GEMC2TxMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2TxMulticasts.setStatus("current")
_Mc2200_GEMC2TxBroadcasts_Type = Counter64
_Mc2200_GEMC2TxBroadcasts_Object = MibTableColumn
mc2200_GEMC2TxBroadcasts = _Mc2200_GEMC2TxBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 29),
    _Mc2200_GEMC2TxBroadcasts_Type()
)
mc2200_GEMC2TxBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2TxBroadcasts.setStatus("current")
_Mc2200_GEMC2TxSingle_Type = Counter64
_Mc2200_GEMC2TxSingle_Object = MibTableColumn
mc2200_GEMC2TxSingle = _Mc2200_GEMC2TxSingle_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 30),
    _Mc2200_GEMC2TxSingle_Type()
)
mc2200_GEMC2TxSingle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2TxSingle.setStatus("current")
_Mc2200_GEMC2TxPause_Type = Counter64
_Mc2200_GEMC2TxPause_Object = MibTableColumn
mc2200_GEMC2TxPause = _Mc2200_GEMC2TxPause_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 31),
    _Mc2200_GEMC2TxPause_Type()
)
mc2200_GEMC2TxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2TxPause.setStatus("current")
_Mc2200_GEMC2RxPause_Type = Counter64
_Mc2200_GEMC2RxPause_Object = MibTableColumn
mc2200_GEMC2RxPause = _Mc2200_GEMC2RxPause_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 32),
    _Mc2200_GEMC2RxPause_Type()
)
mc2200_GEMC2RxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2RxPause.setStatus("current")
_Mc2200_GEMC2TxMultiple_Type = Counter64
_Mc2200_GEMC2TxMultiple_Object = MibTableColumn
mc2200_GEMC2TxMultiple = _Mc2200_GEMC2TxMultiple_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 33),
    _Mc2200_GEMC2TxMultiple_Type()
)
mc2200_GEMC2TxMultiple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2TxMultiple.setStatus("current")
_Mc2200_GEMC2RxUndersize_Type = Counter64
_Mc2200_GEMC2RxUndersize_Object = MibTableColumn
mc2200_GEMC2RxUndersize = _Mc2200_GEMC2RxUndersize_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 34),
    _Mc2200_GEMC2RxUndersize_Type()
)
mc2200_GEMC2RxUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2RxUndersize.setStatus("current")
_Mc2200_GEMC2RxFragments_Type = Counter64
_Mc2200_GEMC2RxFragments_Object = MibTableColumn
mc2200_GEMC2RxFragments = _Mc2200_GEMC2RxFragments_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 35),
    _Mc2200_GEMC2RxFragments_Type()
)
mc2200_GEMC2RxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2RxFragments.setStatus("current")
_Mc2200_GEMC2RxOversize_Type = Counter64
_Mc2200_GEMC2RxOversize_Object = MibTableColumn
mc2200_GEMC2RxOversize = _Mc2200_GEMC2RxOversize_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 36),
    _Mc2200_GEMC2RxOversize_Type()
)
mc2200_GEMC2RxOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2RxOversize.setStatus("current")
_Mc2200_GEMC2RxJabber_Type = Counter64
_Mc2200_GEMC2RxJabber_Object = MibTableColumn
mc2200_GEMC2RxJabber = _Mc2200_GEMC2RxJabber_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 37),
    _Mc2200_GEMC2RxJabber_Type()
)
mc2200_GEMC2RxJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2RxJabber.setStatus("current")
_Mc2200_GEMC2RxErr_Type = Counter64
_Mc2200_GEMC2RxErr_Object = MibTableColumn
mc2200_GEMC2RxErr = _Mc2200_GEMC2RxErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 38),
    _Mc2200_GEMC2RxErr_Type()
)
mc2200_GEMC2RxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2RxErr.setStatus("current")
_Mc2200_GEMC2RxFCSErr_Type = Counter64
_Mc2200_GEMC2RxFCSErr_Object = MibTableColumn
mc2200_GEMC2RxFCSErr = _Mc2200_GEMC2RxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 39),
    _Mc2200_GEMC2RxFCSErr_Type()
)
mc2200_GEMC2RxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2RxFCSErr.setStatus("current")
_Mc2200_GEMC2TxCollisions_Type = Counter64
_Mc2200_GEMC2TxCollisions_Object = MibTableColumn
mc2200_GEMC2TxCollisions = _Mc2200_GEMC2TxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 40),
    _Mc2200_GEMC2TxCollisions_Type()
)
mc2200_GEMC2TxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2TxCollisions.setStatus("current")
_Mc2200_GEMC2TxLate_Type = Counter64
_Mc2200_GEMC2TxLate_Object = MibTableColumn
mc2200_GEMC2TxLate = _Mc2200_GEMC2TxLate_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 41),
    _Mc2200_GEMC2TxLate_Type()
)
mc2200_GEMC2TxLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2TxLate.setStatus("current")
_Mc2200_GEMC2RemoteLANSFPInfo_Type = DisplayString
_Mc2200_GEMC2RemoteLANSFPInfo_Object = MibTableColumn
mc2200_GEMC2RemoteLANSFPInfo = _Mc2200_GEMC2RemoteLANSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 42),
    _Mc2200_GEMC2RemoteLANSFPInfo_Type()
)
mc2200_GEMC2RemoteLANSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2RemoteLANSFPInfo.setStatus("current")


class _Mc2200_GEMC2RemoteLANLink_Type(Integer32):
    """Custom type mc2200_GEMC2RemoteLANLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-remotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_GEMC2RemoteLANLink_Type.__name__ = "Integer32"
_Mc2200_GEMC2RemoteLANLink_Object = MibTableColumn
mc2200_GEMC2RemoteLANLink = _Mc2200_GEMC2RemoteLANLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 43),
    _Mc2200_GEMC2RemoteLANLink_Type()
)
mc2200_GEMC2RemoteLANLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2RemoteLANLink.setStatus("mandatory")
_Mc2200_GEMC2RemoteWANSFPInfo_Type = DisplayString
_Mc2200_GEMC2RemoteWANSFPInfo_Object = MibTableColumn
mc2200_GEMC2RemoteWANSFPInfo = _Mc2200_GEMC2RemoteWANSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 44),
    _Mc2200_GEMC2RemoteWANSFPInfo_Type()
)
mc2200_GEMC2RemoteWANSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2RemoteWANSFPInfo.setStatus("current")


class _Mc2200_GEMC2RemoteWANLink_Type(Integer32):
    """Custom type mc2200_GEMC2RemoteWANLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-remotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_GEMC2RemoteWANLink_Type.__name__ = "Integer32"
_Mc2200_GEMC2RemoteWANLink_Object = MibTableColumn
mc2200_GEMC2RemoteWANLink = _Mc2200_GEMC2RemoteWANLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 45),
    _Mc2200_GEMC2RemoteWANLink_Type()
)
mc2200_GEMC2RemoteWANLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2RemoteWANLink.setStatus("current")


class _Mc2200_GEMC2RemoteLANMode_Type(Integer32):
    """Custom type mc2200_GEMC2RemoteLANMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("no-remotecard", 0),
          ("auto-10-100-1000T", 1),
          ("mode1000Base-X-auto", 2),
          ("mode1000Base-T", 3),
          ("mode100Base-Tx", 4),
          ("mode10Base-T", 5),
          ("mode1000Base-X-1000F", 6))
    )


_Mc2200_GEMC2RemoteLANMode_Type.__name__ = "Integer32"
_Mc2200_GEMC2RemoteLANMode_Object = MibTableColumn
mc2200_GEMC2RemoteLANMode = _Mc2200_GEMC2RemoteLANMode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 46),
    _Mc2200_GEMC2RemoteLANMode_Type()
)
mc2200_GEMC2RemoteLANMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC2RemoteLANMode.setStatus("current")
_Mc2200_GEMC2RemoteIPAddress_Type = IpAddress
_Mc2200_GEMC2RemoteIPAddress_Object = MibTableColumn
mc2200_GEMC2RemoteIPAddress = _Mc2200_GEMC2RemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 47),
    _Mc2200_GEMC2RemoteIPAddress_Type()
)
mc2200_GEMC2RemoteIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC2RemoteIPAddress.setStatus("mandatory")
_Mc2200_GEMC2RemoteSubnetMask_Type = IpAddress
_Mc2200_GEMC2RemoteSubnetMask_Object = MibTableColumn
mc2200_GEMC2RemoteSubnetMask = _Mc2200_GEMC2RemoteSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 48),
    _Mc2200_GEMC2RemoteSubnetMask_Type()
)
mc2200_GEMC2RemoteSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC2RemoteSubnetMask.setStatus("mandatory")
_Mc2200_GEMC2RemoteGateWay_Type = IpAddress
_Mc2200_GEMC2RemoteGateWay_Object = MibTableColumn
mc2200_GEMC2RemoteGateWay = _Mc2200_GEMC2RemoteGateWay_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 49),
    _Mc2200_GEMC2RemoteGateWay_Type()
)
mc2200_GEMC2RemoteGateWay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC2RemoteGateWay.setStatus("mandatory")


class _Mc2200_GEMC2RemoteVLANEnable_Type(Integer32):
    """Custom type mc2200_GEMC2RemoteVLANEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-remotecard", 0),
          ("enable", 1),
          ("disable", 2))
    )


_Mc2200_GEMC2RemoteVLANEnable_Type.__name__ = "Integer32"
_Mc2200_GEMC2RemoteVLANEnable_Object = MibTableColumn
mc2200_GEMC2RemoteVLANEnable = _Mc2200_GEMC2RemoteVLANEnable_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 50),
    _Mc2200_GEMC2RemoteVLANEnable_Type()
)
mc2200_GEMC2RemoteVLANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC2RemoteVLANEnable.setStatus("mandatory")
_Mc2200_GEMC2RemoteVID_Type = Integer32
_Mc2200_GEMC2RemoteVID_Object = MibTableColumn
mc2200_GEMC2RemoteVID = _Mc2200_GEMC2RemoteVID_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 51),
    _Mc2200_GEMC2RemoteVID_Type()
)
mc2200_GEMC2RemoteVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC2RemoteVID.setStatus("mandatory")


class _Mc2200_GEMC2RemoteAlarm_Type(Integer32):
    """Custom type mc2200_GEMC2RemoteAlarm based on Integer32"""
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


_Mc2200_GEMC2RemoteAlarm_Type.__name__ = "Integer32"
_Mc2200_GEMC2RemoteAlarm_Object = MibTableColumn
mc2200_GEMC2RemoteAlarm = _Mc2200_GEMC2RemoteAlarm_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 52),
    _Mc2200_GEMC2RemoteAlarm_Type()
)
mc2200_GEMC2RemoteAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC2RemoteAlarm.setStatus("current")


class _Mc2200_GEMC2RFD_Type(Integer32):
    """Custom type mc2200_GEMC2RFD based on Integer32"""
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


_Mc2200_GEMC2RFD_Type.__name__ = "Integer32"
_Mc2200_GEMC2RFD_Object = MibTableColumn
mc2200_GEMC2RFD = _Mc2200_GEMC2RFD_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 53),
    _Mc2200_GEMC2RFD_Type()
)
mc2200_GEMC2RFD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC2RFD.setStatus("current")
_Mc2200_GEMC2Default_Type = Integer32
_Mc2200_GEMC2Default_Object = MibTableColumn
mc2200_GEMC2Default = _Mc2200_GEMC2Default_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 54),
    _Mc2200_GEMC2Default_Type()
)
mc2200_GEMC2Default.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2Default.setStatus("current")
_Mc2200_GEMC2Reboot_Type = Integer32
_Mc2200_GEMC2Reboot_Object = MibTableColumn
mc2200_GEMC2Reboot = _Mc2200_GEMC2Reboot_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 55),
    _Mc2200_GEMC2Reboot_Type()
)
mc2200_GEMC2Reboot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2Reboot.setStatus("current")


class _Mc2200_GEMC2LocalCardREMOTEMODE_Type(Integer32):
    """Custom type mc2200_GEMC2LocalCardREMOTEMODE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("remoteMode-Enabled", 1),
          ("remoteMode-Disabled", 2),
          ("no-Setting", 3))
    )


_Mc2200_GEMC2LocalCardREMOTEMODE_Type.__name__ = "Integer32"
_Mc2200_GEMC2LocalCardREMOTEMODE_Object = MibTableColumn
mc2200_GEMC2LocalCardREMOTEMODE = _Mc2200_GEMC2LocalCardREMOTEMODE_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 56),
    _Mc2200_GEMC2LocalCardREMOTEMODE_Type()
)
mc2200_GEMC2LocalCardREMOTEMODE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC2LocalCardREMOTEMODE.setStatus("current")


class _Mc2200_GEMC2LocalLANSpeed_Type(Integer32):
    """Custom type mc2200_GEMC2LocalLANSpeed based on Integer32"""
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
        *(("speed1000M", 1),
          ("speed100M", 2),
          ("speed10M", 3),
          ("down", 4))
    )


_Mc2200_GEMC2LocalLANSpeed_Type.__name__ = "Integer32"
_Mc2200_GEMC2LocalLANSpeed_Object = MibTableColumn
mc2200_GEMC2LocalLANSpeed = _Mc2200_GEMC2LocalLANSpeed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 57),
    _Mc2200_GEMC2LocalLANSpeed_Type()
)
mc2200_GEMC2LocalLANSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2LocalLANSpeed.setStatus("mandatory")


class _Mc2200_GEMC2RemoteLANSpeed_Type(Integer32):
    """Custom type mc2200_GEMC2RemoteLANSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("no-remotecard", 0),
          ("speed1000M", 1),
          ("speed100M", 2),
          ("speed10M", 3),
          ("down", 4))
    )


_Mc2200_GEMC2RemoteLANSpeed_Type.__name__ = "Integer32"
_Mc2200_GEMC2RemoteLANSpeed_Object = MibTableColumn
mc2200_GEMC2RemoteLANSpeed = _Mc2200_GEMC2RemoteLANSpeed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 58),
    _Mc2200_GEMC2RemoteLANSpeed_Type()
)
mc2200_GEMC2RemoteLANSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC2RemoteLANSpeed.setStatus("mandatory")
_Mc2200_GEMC2Localportuser_Type = DisplayString
_Mc2200_GEMC2Localportuser_Object = MibTableColumn
mc2200_GEMC2Localportuser = _Mc2200_GEMC2Localportuser_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 59),
    _Mc2200_GEMC2Localportuser_Type()
)
mc2200_GEMC2Localportuser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC2Localportuser.setStatus("current")
_Mc2200_GEMC2Remoteportuser_Type = DisplayString
_Mc2200_GEMC2Remoteportuser_Object = MibTableColumn
mc2200_GEMC2Remoteportuser = _Mc2200_GEMC2Remoteportuser_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 60),
    _Mc2200_GEMC2Remoteportuser_Type()
)
mc2200_GEMC2Remoteportuser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC2Remoteportuser.setStatus("current")


class _Mc2200_GEMC2TrapFilterLocalLAN_Type(Integer32):
    """Custom type mc2200_GEMC2TrapFilterLocalLAN based on Integer32"""
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


_Mc2200_GEMC2TrapFilterLocalLAN_Type.__name__ = "Integer32"
_Mc2200_GEMC2TrapFilterLocalLAN_Object = MibTableColumn
mc2200_GEMC2TrapFilterLocalLAN = _Mc2200_GEMC2TrapFilterLocalLAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 61),
    _Mc2200_GEMC2TrapFilterLocalLAN_Type()
)
mc2200_GEMC2TrapFilterLocalLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC2TrapFilterLocalLAN.setStatus("current")


class _Mc2200_GEMC2TrapFilterLocalWAN_Type(Integer32):
    """Custom type mc2200_GEMC2TrapFilterLocalWAN based on Integer32"""
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


_Mc2200_GEMC2TrapFilterLocalWAN_Type.__name__ = "Integer32"
_Mc2200_GEMC2TrapFilterLocalWAN_Object = MibTableColumn
mc2200_GEMC2TrapFilterLocalWAN = _Mc2200_GEMC2TrapFilterLocalWAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 62),
    _Mc2200_GEMC2TrapFilterLocalWAN_Type()
)
mc2200_GEMC2TrapFilterLocalWAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC2TrapFilterLocalWAN.setStatus("current")


class _Mc2200_GEMC2TrapFilterRemotePower_Type(Integer32):
    """Custom type mc2200_GEMC2TrapFilterRemotePower based on Integer32"""
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


_Mc2200_GEMC2TrapFilterRemotePower_Type.__name__ = "Integer32"
_Mc2200_GEMC2TrapFilterRemotePower_Object = MibTableColumn
mc2200_GEMC2TrapFilterRemotePower = _Mc2200_GEMC2TrapFilterRemotePower_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 63),
    _Mc2200_GEMC2TrapFilterRemotePower_Type()
)
mc2200_GEMC2TrapFilterRemotePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC2TrapFilterRemotePower.setStatus("current")


class _Mc2200_GEMC2TrapFilterRemoteLAN_Type(Integer32):
    """Custom type mc2200_GEMC2TrapFilterRemoteLAN based on Integer32"""
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


_Mc2200_GEMC2TrapFilterRemoteLAN_Type.__name__ = "Integer32"
_Mc2200_GEMC2TrapFilterRemoteLAN_Object = MibTableColumn
mc2200_GEMC2TrapFilterRemoteLAN = _Mc2200_GEMC2TrapFilterRemoteLAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 64),
    _Mc2200_GEMC2TrapFilterRemoteLAN_Type()
)
mc2200_GEMC2TrapFilterRemoteLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC2TrapFilterRemoteLAN.setStatus("current")


class _Mc2200_GEMC2TrapFilterRemoteWAN_Type(Integer32):
    """Custom type mc2200_GEMC2TrapFilterRemoteWAN based on Integer32"""
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


_Mc2200_GEMC2TrapFilterRemoteWAN_Type.__name__ = "Integer32"
_Mc2200_GEMC2TrapFilterRemoteWAN_Object = MibTableColumn
mc2200_GEMC2TrapFilterRemoteWAN = _Mc2200_GEMC2TrapFilterRemoteWAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 6, 1, 65),
    _Mc2200_GEMC2TrapFilterRemoteWAN_Type()
)
mc2200_GEMC2TrapFilterRemoteWAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC2TrapFilterRemoteWAN.setStatus("current")
_Mc2200_FESFPTable_Object = MibTable
mc2200_FESFPTable = _Mc2200_FESFPTable_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11)
)
if mibBuilder.loadTexts:
    mc2200_FESFPTable.setStatus("current")
_Mc2200_FESFPEntry_Object = MibTableRow
mc2200_FESFPEntry = _Mc2200_FESFPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1)
)
mc2200_FESFPEntry.setIndexNames(
    (0, "OnAccess2200-MIB", "mc2200-FESFPCardIndex"),
)
if mibBuilder.loadTexts:
    mc2200_FESFPEntry.setStatus("current")


class _Mc2200_FESFPCardIndex_Type(Integer32):
    """Custom type mc2200_FESFPCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("card01", 1),
          ("card02", 2),
          ("card03", 3),
          ("card04", 4),
          ("card05", 5),
          ("card06", 6),
          ("card07", 7),
          ("card08", 8),
          ("card09", 9),
          ("card10", 10),
          ("card11", 11),
          ("card12", 12),
          ("card13", 13),
          ("card14", 14),
          ("card15", 15))
    )


_Mc2200_FESFPCardIndex_Type.__name__ = "Integer32"
_Mc2200_FESFPCardIndex_Object = MibTableColumn
mc2200_FESFPCardIndex = _Mc2200_FESFPCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 1),
    _Mc2200_FESFPCardIndex_Type()
)
mc2200_FESFPCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPCardIndex.setStatus("current")


class _Mc2200_FESFPLocalTXLink_Type(Integer32):
    """Custom type mc2200_FESFPLocalTXLink based on Integer32"""
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


_Mc2200_FESFPLocalTXLink_Type.__name__ = "Integer32"
_Mc2200_FESFPLocalTXLink_Object = MibTableColumn
mc2200_FESFPLocalTXLink = _Mc2200_FESFPLocalTXLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 2),
    _Mc2200_FESFPLocalTXLink_Type()
)
mc2200_FESFPLocalTXLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPLocalTXLink.setStatus("mandatory")
_Mc2200_FESFPLocalWANSFPInfo_Type = DisplayString
_Mc2200_FESFPLocalWANSFPInfo_Object = MibTableColumn
mc2200_FESFPLocalWANSFPInfo = _Mc2200_FESFPLocalWANSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 3),
    _Mc2200_FESFPLocalWANSFPInfo_Type()
)
mc2200_FESFPLocalWANSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPLocalWANSFPInfo.setStatus("current")


class _Mc2200_FESFPLocalWANLink_Type(Integer32):
    """Custom type mc2200_FESFPLocalWANLink based on Integer32"""
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


_Mc2200_FESFPLocalWANLink_Type.__name__ = "Integer32"
_Mc2200_FESFPLocalWANLink_Object = MibTableColumn
mc2200_FESFPLocalWANLink = _Mc2200_FESFPLocalWANLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 4),
    _Mc2200_FESFPLocalWANLink_Type()
)
mc2200_FESFPLocalWANLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPLocalWANLink.setStatus("current")


class _Mc2200_FESFPLocalTXDownStreamBW_Type(Integer32):
    """Custom type mc2200_FESFPLocalTXDownStreamBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              35,
              40,
              45,
              50,
              55,
              60,
              65,
              70,
              75,
              80,
              85,
              90,
              95,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate35M", 35),
          ("rate40M", 40),
          ("rate45M", 45),
          ("rate50M", 50),
          ("rate55M", 55),
          ("rate60M", 60),
          ("rate65M", 65),
          ("rate70M", 70),
          ("rate75M", 75),
          ("rate80M", 80),
          ("rate85M", 85),
          ("rate90M", 90),
          ("rate95M", 95),
          ("rate100M", 100))
    )


_Mc2200_FESFPLocalTXDownStreamBW_Type.__name__ = "Integer32"
_Mc2200_FESFPLocalTXDownStreamBW_Object = MibTableColumn
mc2200_FESFPLocalTXDownStreamBW = _Mc2200_FESFPLocalTXDownStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 5),
    _Mc2200_FESFPLocalTXDownStreamBW_Type()
)
mc2200_FESFPLocalTXDownStreamBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FESFPLocalTXDownStreamBW.setStatus("current")


class _Mc2200_FESFPLocalTXUpStreamBW_Type(Integer32):
    """Custom type mc2200_FESFPLocalTXUpStreamBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              35,
              40,
              45,
              50,
              55,
              60,
              65,
              70,
              75,
              80,
              85,
              90,
              95,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate35M", 35),
          ("rate40M", 40),
          ("rate45M", 45),
          ("rate50M", 50),
          ("rate55M", 55),
          ("rate60M", 60),
          ("rate65M", 65),
          ("rate70M", 70),
          ("rate75M", 75),
          ("rate80M", 80),
          ("rate85M", 85),
          ("rate90M", 90),
          ("rate95M", 95),
          ("rate100M", 100))
    )


_Mc2200_FESFPLocalTXUpStreamBW_Type.__name__ = "Integer32"
_Mc2200_FESFPLocalTXUpStreamBW_Object = MibTableColumn
mc2200_FESFPLocalTXUpStreamBW = _Mc2200_FESFPLocalTXUpStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 6),
    _Mc2200_FESFPLocalTXUpStreamBW_Type()
)
mc2200_FESFPLocalTXUpStreamBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FESFPLocalTXUpStreamBW.setStatus("current")


class _Mc2200_FESFPLocalTXMode_Type(Integer32):
    """Custom type mc2200_FESFPLocalTXMode based on Integer32"""
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
        *(("auto", 1),
          ("mode10MHALFDUPLEX", 2),
          ("mode10MFULLDUPLEX", 3),
          ("mode100MHALFDUPLEX", 4),
          ("mode100MFULLDUPLEX", 5))
    )


_Mc2200_FESFPLocalTXMode_Type.__name__ = "Integer32"
_Mc2200_FESFPLocalTXMode_Object = MibTableColumn
mc2200_FESFPLocalTXMode = _Mc2200_FESFPLocalTXMode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 7),
    _Mc2200_FESFPLocalTXMode_Type()
)
mc2200_FESFPLocalTXMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FESFPLocalTXMode.setStatus("current")


class _Mc2200_FESFPLocalTXMDIX_Type(Integer32):
    """Custom type mc2200_FESFPLocalTXMDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("mdi", 2),
          ("mdix", 3))
    )


_Mc2200_FESFPLocalTXMDIX_Type.__name__ = "Integer32"
_Mc2200_FESFPLocalTXMDIX_Object = MibTableColumn
mc2200_FESFPLocalTXMDIX = _Mc2200_FESFPLocalTXMDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 8),
    _Mc2200_FESFPLocalTXMDIX_Type()
)
mc2200_FESFPLocalTXMDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FESFPLocalTXMDIX.setStatus("current")
_Mc2200_FESFPRxGoodOctets_Type = Counter64
_Mc2200_FESFPRxGoodOctets_Object = MibTableColumn
mc2200_FESFPRxGoodOctets = _Mc2200_FESFPRxGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 9),
    _Mc2200_FESFPRxGoodOctets_Type()
)
mc2200_FESFPRxGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPRxGoodOctets.setStatus("current")
_Mc2200_FESFPRxBadOctets_Type = Counter64
_Mc2200_FESFPRxBadOctets_Object = MibTableColumn
mc2200_FESFPRxBadOctets = _Mc2200_FESFPRxBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 11),
    _Mc2200_FESFPRxBadOctets_Type()
)
mc2200_FESFPRxBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPRxBadOctets.setStatus("current")
_Mc2200_FESFPTxFCSErr_Type = Counter64
_Mc2200_FESFPTxFCSErr_Object = MibTableColumn
mc2200_FESFPTxFCSErr = _Mc2200_FESFPTxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 12),
    _Mc2200_FESFPTxFCSErr_Type()
)
mc2200_FESFPTxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPTxFCSErr.setStatus("current")
_Mc2200_FESFPRxUnicast_Type = Counter64
_Mc2200_FESFPRxUnicast_Object = MibTableColumn
mc2200_FESFPRxUnicast = _Mc2200_FESFPRxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 13),
    _Mc2200_FESFPRxUnicast_Type()
)
mc2200_FESFPRxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPRxUnicast.setStatus("current")
_Mc2200_FESFPTxDeferred_Type = Counter64
_Mc2200_FESFPTxDeferred_Object = MibTableColumn
mc2200_FESFPTxDeferred = _Mc2200_FESFPTxDeferred_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 14),
    _Mc2200_FESFPTxDeferred_Type()
)
mc2200_FESFPTxDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPTxDeferred.setStatus("current")
_Mc2200_FESFPRxBroadcasts_Type = Counter64
_Mc2200_FESFPRxBroadcasts_Object = MibTableColumn
mc2200_FESFPRxBroadcasts = _Mc2200_FESFPRxBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 15),
    _Mc2200_FESFPRxBroadcasts_Type()
)
mc2200_FESFPRxBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPRxBroadcasts.setStatus("current")
_Mc2200_FESFPRxMulticasts_Type = Counter64
_Mc2200_FESFPRxMulticasts_Object = MibTableColumn
mc2200_FESFPRxMulticasts = _Mc2200_FESFPRxMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 16),
    _Mc2200_FESFPRxMulticasts_Type()
)
mc2200_FESFPRxMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPRxMulticasts.setStatus("current")
_Mc2200_FESFPRx64Octets_Type = Counter64
_Mc2200_FESFPRx64Octets_Object = MibTableColumn
mc2200_FESFPRx64Octets = _Mc2200_FESFPRx64Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 17),
    _Mc2200_FESFPRx64Octets_Type()
)
mc2200_FESFPRx64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPRx64Octets.setStatus("current")
_Mc2200_FESFPRx65to127Octets_Type = Counter64
_Mc2200_FESFPRx65to127Octets_Object = MibTableColumn
mc2200_FESFPRx65to127Octets = _Mc2200_FESFPRx65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 18),
    _Mc2200_FESFPRx65to127Octets_Type()
)
mc2200_FESFPRx65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPRx65to127Octets.setStatus("current")
_Mc2200_FESFPRx128to255Octets_Type = Counter64
_Mc2200_FESFPRx128to255Octets_Object = MibTableColumn
mc2200_FESFPRx128to255Octets = _Mc2200_FESFPRx128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 19),
    _Mc2200_FESFPRx128to255Octets_Type()
)
mc2200_FESFPRx128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPRx128to255Octets.setStatus("current")
_Mc2200_FESFPRx256to511Octets_Type = Counter64
_Mc2200_FESFPRx256to511Octets_Object = MibTableColumn
mc2200_FESFPRx256to511Octets = _Mc2200_FESFPRx256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 20),
    _Mc2200_FESFPRx256to511Octets_Type()
)
mc2200_FESFPRx256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPRx256to511Octets.setStatus("current")
_Mc2200_FESFPRx512to1023Octets_Type = Counter64
_Mc2200_FESFPRx512to1023Octets_Object = MibTableColumn
mc2200_FESFPRx512to1023Octets = _Mc2200_FESFPRx512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 21),
    _Mc2200_FESFPRx512to1023Octets_Type()
)
mc2200_FESFPRx512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPRx512to1023Octets.setStatus("current")
_Mc2200_FESFPRx1024toMaxOctets_Type = Counter64
_Mc2200_FESFPRx1024toMaxOctets_Object = MibTableColumn
mc2200_FESFPRx1024toMaxOctets = _Mc2200_FESFPRx1024toMaxOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 22),
    _Mc2200_FESFPRx1024toMaxOctets_Type()
)
mc2200_FESFPRx1024toMaxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPRx1024toMaxOctets.setStatus("current")
_Mc2200_FESFPTxOctets_Type = Counter64
_Mc2200_FESFPTxOctets_Object = MibTableColumn
mc2200_FESFPTxOctets = _Mc2200_FESFPTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 23),
    _Mc2200_FESFPTxOctets_Type()
)
mc2200_FESFPTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPTxOctets.setStatus("current")
_Mc2200_FESFPTxUnicast_Type = Counter64
_Mc2200_FESFPTxUnicast_Object = MibTableColumn
mc2200_FESFPTxUnicast = _Mc2200_FESFPTxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 25),
    _Mc2200_FESFPTxUnicast_Type()
)
mc2200_FESFPTxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPTxUnicast.setStatus("current")
_Mc2200_FESFPTxExcessive_Type = Counter64
_Mc2200_FESFPTxExcessive_Object = MibTableColumn
mc2200_FESFPTxExcessive = _Mc2200_FESFPTxExcessive_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 26),
    _Mc2200_FESFPTxExcessive_Type()
)
mc2200_FESFPTxExcessive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPTxExcessive.setStatus("current")
_Mc2200_FESFPTxMulticasts_Type = Counter64
_Mc2200_FESFPTxMulticasts_Object = MibTableColumn
mc2200_FESFPTxMulticasts = _Mc2200_FESFPTxMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 27),
    _Mc2200_FESFPTxMulticasts_Type()
)
mc2200_FESFPTxMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPTxMulticasts.setStatus("current")
_Mc2200_FESFPTxBroadcasts_Type = Counter64
_Mc2200_FESFPTxBroadcasts_Object = MibTableColumn
mc2200_FESFPTxBroadcasts = _Mc2200_FESFPTxBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 28),
    _Mc2200_FESFPTxBroadcasts_Type()
)
mc2200_FESFPTxBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPTxBroadcasts.setStatus("current")
_Mc2200_FESFPTxSingle_Type = Counter64
_Mc2200_FESFPTxSingle_Object = MibTableColumn
mc2200_FESFPTxSingle = _Mc2200_FESFPTxSingle_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 29),
    _Mc2200_FESFPTxSingle_Type()
)
mc2200_FESFPTxSingle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPTxSingle.setStatus("current")
_Mc2200_FESFPTxPause_Type = Counter64
_Mc2200_FESFPTxPause_Object = MibTableColumn
mc2200_FESFPTxPause = _Mc2200_FESFPTxPause_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 30),
    _Mc2200_FESFPTxPause_Type()
)
mc2200_FESFPTxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPTxPause.setStatus("current")
_Mc2200_FESFPRxPause_Type = Counter64
_Mc2200_FESFPRxPause_Object = MibTableColumn
mc2200_FESFPRxPause = _Mc2200_FESFPRxPause_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 31),
    _Mc2200_FESFPRxPause_Type()
)
mc2200_FESFPRxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPRxPause.setStatus("current")
_Mc2200_FESFPTxMultiple_Type = Counter64
_Mc2200_FESFPTxMultiple_Object = MibTableColumn
mc2200_FESFPTxMultiple = _Mc2200_FESFPTxMultiple_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 32),
    _Mc2200_FESFPTxMultiple_Type()
)
mc2200_FESFPTxMultiple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPTxMultiple.setStatus("current")
_Mc2200_FESFPRxUndersize_Type = Counter64
_Mc2200_FESFPRxUndersize_Object = MibTableColumn
mc2200_FESFPRxUndersize = _Mc2200_FESFPRxUndersize_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 33),
    _Mc2200_FESFPRxUndersize_Type()
)
mc2200_FESFPRxUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPRxUndersize.setStatus("current")
_Mc2200_FESFPRxFragments_Type = Counter64
_Mc2200_FESFPRxFragments_Object = MibTableColumn
mc2200_FESFPRxFragments = _Mc2200_FESFPRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 34),
    _Mc2200_FESFPRxFragments_Type()
)
mc2200_FESFPRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPRxFragments.setStatus("current")
_Mc2200_FESFPRxOversize_Type = Counter64
_Mc2200_FESFPRxOversize_Object = MibTableColumn
mc2200_FESFPRxOversize = _Mc2200_FESFPRxOversize_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 35),
    _Mc2200_FESFPRxOversize_Type()
)
mc2200_FESFPRxOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPRxOversize.setStatus("current")
_Mc2200_FESFPRxJabber_Type = Counter64
_Mc2200_FESFPRxJabber_Object = MibTableColumn
mc2200_FESFPRxJabber = _Mc2200_FESFPRxJabber_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 36),
    _Mc2200_FESFPRxJabber_Type()
)
mc2200_FESFPRxJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPRxJabber.setStatus("current")
_Mc2200_FESFPRxErr_Type = Counter64
_Mc2200_FESFPRxErr_Object = MibTableColumn
mc2200_FESFPRxErr = _Mc2200_FESFPRxErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 37),
    _Mc2200_FESFPRxErr_Type()
)
mc2200_FESFPRxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPRxErr.setStatus("current")
_Mc2200_FESFPRxFCSErr_Type = Counter64
_Mc2200_FESFPRxFCSErr_Object = MibTableColumn
mc2200_FESFPRxFCSErr = _Mc2200_FESFPRxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 38),
    _Mc2200_FESFPRxFCSErr_Type()
)
mc2200_FESFPRxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPRxFCSErr.setStatus("current")
_Mc2200_FESFPTxCollisions_Type = Counter64
_Mc2200_FESFPTxCollisions_Object = MibTableColumn
mc2200_FESFPTxCollisions = _Mc2200_FESFPTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 39),
    _Mc2200_FESFPTxCollisions_Type()
)
mc2200_FESFPTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPTxCollisions.setStatus("current")
_Mc2200_FESFPTxLate_Type = Counter64
_Mc2200_FESFPTxLate_Object = MibTableColumn
mc2200_FESFPTxLate = _Mc2200_FESFPTxLate_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 40),
    _Mc2200_FESFPTxLate_Type()
)
mc2200_FESFPTxLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPTxLate.setStatus("current")


class _Mc2200_FESFPRemoteTXLink_Type(Integer32):
    """Custom type mc2200_FESFPRemoteTXLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_FESFPRemoteTXLink_Type.__name__ = "Integer32"
_Mc2200_FESFPRemoteTXLink_Object = MibTableColumn
mc2200_FESFPRemoteTXLink = _Mc2200_FESFPRemoteTXLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 41),
    _Mc2200_FESFPRemoteTXLink_Type()
)
mc2200_FESFPRemoteTXLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPRemoteTXLink.setStatus("mandatory")
_Mc2200_FESFPRemoteWANSFPInfo_Type = DisplayString
_Mc2200_FESFPRemoteWANSFPInfo_Object = MibTableColumn
mc2200_FESFPRemoteWANSFPInfo = _Mc2200_FESFPRemoteWANSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 42),
    _Mc2200_FESFPRemoteWANSFPInfo_Type()
)
mc2200_FESFPRemoteWANSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPRemoteWANSFPInfo.setStatus("current")


class _Mc2200_FESFPRemoteWANLink_Type(Integer32):
    """Custom type mc2200_FESFPRemoteWANLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_FESFPRemoteWANLink_Type.__name__ = "Integer32"
_Mc2200_FESFPRemoteWANLink_Object = MibTableColumn
mc2200_FESFPRemoteWANLink = _Mc2200_FESFPRemoteWANLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 43),
    _Mc2200_FESFPRemoteWANLink_Type()
)
mc2200_FESFPRemoteWANLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPRemoteWANLink.setStatus("current")


class _Mc2200_FESFPRemoteTXMode_Type(Integer32):
    """Custom type mc2200_FESFPRemoteTXMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mode10MHALFDUPLEX", 2),
          ("mode10MFULLDUPLEX", 3),
          ("mode100MHALFDUPLEX", 4),
          ("mode100MFULLDUPLEX", 5))
    )


_Mc2200_FESFPRemoteTXMode_Type.__name__ = "Integer32"
_Mc2200_FESFPRemoteTXMode_Object = MibTableColumn
mc2200_FESFPRemoteTXMode = _Mc2200_FESFPRemoteTXMode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 44),
    _Mc2200_FESFPRemoteTXMode_Type()
)
mc2200_FESFPRemoteTXMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FESFPRemoteTXMode.setStatus("current")


class _Mc2200_FESFPRemoteTXMDIX_Type(Integer32):
    """Custom type mc2200_FESFPRemoteTXMDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mdi", 2),
          ("mdix", 3))
    )


_Mc2200_FESFPRemoteTXMDIX_Type.__name__ = "Integer32"
_Mc2200_FESFPRemoteTXMDIX_Object = MibTableColumn
mc2200_FESFPRemoteTXMDIX = _Mc2200_FESFPRemoteTXMDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 45),
    _Mc2200_FESFPRemoteTXMDIX_Type()
)
mc2200_FESFPRemoteTXMDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FESFPRemoteTXMDIX.setStatus("current")
_Mc2200_FESFPRemoteIPAddress_Type = IpAddress
_Mc2200_FESFPRemoteIPAddress_Object = MibTableColumn
mc2200_FESFPRemoteIPAddress = _Mc2200_FESFPRemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 46),
    _Mc2200_FESFPRemoteIPAddress_Type()
)
mc2200_FESFPRemoteIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FESFPRemoteIPAddress.setStatus("mandatory")
_Mc2200_FESFPRemoteSubnetMask_Type = IpAddress
_Mc2200_FESFPRemoteSubnetMask_Object = MibTableColumn
mc2200_FESFPRemoteSubnetMask = _Mc2200_FESFPRemoteSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 47),
    _Mc2200_FESFPRemoteSubnetMask_Type()
)
mc2200_FESFPRemoteSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FESFPRemoteSubnetMask.setStatus("mandatory")
_Mc2200_FESFPRemoteGateWay_Type = IpAddress
_Mc2200_FESFPRemoteGateWay_Object = MibTableColumn
mc2200_FESFPRemoteGateWay = _Mc2200_FESFPRemoteGateWay_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 48),
    _Mc2200_FESFPRemoteGateWay_Type()
)
mc2200_FESFPRemoteGateWay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FESFPRemoteGateWay.setStatus("mandatory")


class _Mc2200_FESFPRemoteVLANEnable_Type(Integer32):
    """Custom type mc2200_FESFPRemoteVLANEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("enable", 1),
          ("disable", 2))
    )


_Mc2200_FESFPRemoteVLANEnable_Type.__name__ = "Integer32"
_Mc2200_FESFPRemoteVLANEnable_Object = MibTableColumn
mc2200_FESFPRemoteVLANEnable = _Mc2200_FESFPRemoteVLANEnable_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 49),
    _Mc2200_FESFPRemoteVLANEnable_Type()
)
mc2200_FESFPRemoteVLANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FESFPRemoteVLANEnable.setStatus("mandatory")
_Mc2200_FESFPRemoteVID_Type = Integer32
_Mc2200_FESFPRemoteVID_Object = MibTableColumn
mc2200_FESFPRemoteVID = _Mc2200_FESFPRemoteVID_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 50),
    _Mc2200_FESFPRemoteVID_Type()
)
mc2200_FESFPRemoteVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FESFPRemoteVID.setStatus("mandatory")


class _Mc2200_FESFPRemoteAlarm_Type(Integer32):
    """Custom type mc2200_FESFPRemoteAlarm based on Integer32"""
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


_Mc2200_FESFPRemoteAlarm_Type.__name__ = "Integer32"
_Mc2200_FESFPRemoteAlarm_Object = MibTableColumn
mc2200_FESFPRemoteAlarm = _Mc2200_FESFPRemoteAlarm_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 51),
    _Mc2200_FESFPRemoteAlarm_Type()
)
mc2200_FESFPRemoteAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FESFPRemoteAlarm.setStatus("current")


class _Mc2200_FESFPRFD_Type(Integer32):
    """Custom type mc2200_FESFPRFD based on Integer32"""
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


_Mc2200_FESFPRFD_Type.__name__ = "Integer32"
_Mc2200_FESFPRFD_Object = MibTableColumn
mc2200_FESFPRFD = _Mc2200_FESFPRFD_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 52),
    _Mc2200_FESFPRFD_Type()
)
mc2200_FESFPRFD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FESFPRFD.setStatus("current")
_Mc2200_FESFPDefault_Type = Integer32
_Mc2200_FESFPDefault_Object = MibTableColumn
mc2200_FESFPDefault = _Mc2200_FESFPDefault_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 53),
    _Mc2200_FESFPDefault_Type()
)
mc2200_FESFPDefault.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mc2200_FESFPDefault.setStatus("current")
_Mc2200_FESFPReboot_Type = Integer32
_Mc2200_FESFPReboot_Object = MibTableColumn
mc2200_FESFPReboot = _Mc2200_FESFPReboot_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 54),
    _Mc2200_FESFPReboot_Type()
)
mc2200_FESFPReboot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mc2200_FESFPReboot.setStatus("current")


class _Mc2200_FESFPLocalTXSpeed_Type(Integer32):
    """Custom type mc2200_FESFPLocalTXSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed100M", 1),
          ("speed10M", 2),
          ("down", 3))
    )


_Mc2200_FESFPLocalTXSpeed_Type.__name__ = "Integer32"
_Mc2200_FESFPLocalTXSpeed_Object = MibTableColumn
mc2200_FESFPLocalTXSpeed = _Mc2200_FESFPLocalTXSpeed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 55),
    _Mc2200_FESFPLocalTXSpeed_Type()
)
mc2200_FESFPLocalTXSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPLocalTXSpeed.setStatus("mandatory")


class _Mc2200_FESFPRemoteTXSpeed_Type(Integer32):
    """Custom type mc2200_FESFPRemoteTXSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("speed100M", 1),
          ("speed10M", 2),
          ("down", 3))
    )


_Mc2200_FESFPRemoteTXSpeed_Type.__name__ = "Integer32"
_Mc2200_FESFPRemoteTXSpeed_Object = MibTableColumn
mc2200_FESFPRemoteTXSpeed = _Mc2200_FESFPRemoteTXSpeed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 56),
    _Mc2200_FESFPRemoteTXSpeed_Type()
)
mc2200_FESFPRemoteTXSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPRemoteTXSpeed.setStatus("mandatory")
_Mc2200_FESFPLocalportuser_Type = DisplayString
_Mc2200_FESFPLocalportuser_Object = MibTableColumn
mc2200_FESFPLocalportuser = _Mc2200_FESFPLocalportuser_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 57),
    _Mc2200_FESFPLocalportuser_Type()
)
mc2200_FESFPLocalportuser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FESFPLocalportuser.setStatus("current")
_Mc2200_FESFPRemoteportuser_Type = DisplayString
_Mc2200_FESFPRemoteportuser_Object = MibTableColumn
mc2200_FESFPRemoteportuser = _Mc2200_FESFPRemoteportuser_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 58),
    _Mc2200_FESFPRemoteportuser_Type()
)
mc2200_FESFPRemoteportuser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FESFPRemoteportuser.setStatus("current")


class _Mc2200_FESFPLocalTXDuplex_Type(Integer32):
    """Custom type mc2200_FESFPLocalTXDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2),
          ("down", 3))
    )


_Mc2200_FESFPLocalTXDuplex_Type.__name__ = "Integer32"
_Mc2200_FESFPLocalTXDuplex_Object = MibTableColumn
mc2200_FESFPLocalTXDuplex = _Mc2200_FESFPLocalTXDuplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 59),
    _Mc2200_FESFPLocalTXDuplex_Type()
)
mc2200_FESFPLocalTXDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPLocalTXDuplex.setStatus("mandatory")


class _Mc2200_FESFPRemoteTXDuplex_Type(Integer32):
    """Custom type mc2200_FESFPRemoteTXDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("fullDuplex", 1),
          ("halfDuplex", 2),
          ("down", 3))
    )


_Mc2200_FESFPRemoteTXDuplex_Type.__name__ = "Integer32"
_Mc2200_FESFPRemoteTXDuplex_Object = MibTableColumn
mc2200_FESFPRemoteTXDuplex = _Mc2200_FESFPRemoteTXDuplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 60),
    _Mc2200_FESFPRemoteTXDuplex_Type()
)
mc2200_FESFPRemoteTXDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPRemoteTXDuplex.setStatus("mandatory")


class _Mc2200_FESFPFlowControl_Type(Integer32):
    """Custom type mc2200_FESFPFlowControl based on Integer32"""
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


_Mc2200_FESFPFlowControl_Type.__name__ = "Integer32"
_Mc2200_FESFPFlowControl_Object = MibTableColumn
mc2200_FESFPFlowControl = _Mc2200_FESFPFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 61),
    _Mc2200_FESFPFlowControl_Type()
)
mc2200_FESFPFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FESFPFlowControl.setStatus("current")


class _Mc2200_FESFPWANOpticalPowerCheck_Type(Integer32):
    """Custom type mc2200_FESFPWANOpticalPowerCheck based on Integer32"""
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


_Mc2200_FESFPWANOpticalPowerCheck_Type.__name__ = "Integer32"
_Mc2200_FESFPWANOpticalPowerCheck_Object = MibTableColumn
mc2200_FESFPWANOpticalPowerCheck = _Mc2200_FESFPWANOpticalPowerCheck_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 62),
    _Mc2200_FESFPWANOpticalPowerCheck_Type()
)
mc2200_FESFPWANOpticalPowerCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FESFPWANOpticalPowerCheck.setStatus("current")


class _Mc2200_FESFPWANThreshold_Type(Integer32):
    """Custom type mc2200_FESFPWANThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71)
        )
    )
    namedValues = NamedValues(
        *(("db-32", 1),
          ("db-31dot5", 2),
          ("db-31", 3),
          ("db-30dot5", 4),
          ("db-30", 5),
          ("db-29dot5", 6),
          ("db-29", 7),
          ("db-28dot5", 8),
          ("db-28", 9),
          ("db-27dot5", 10),
          ("db-27", 11),
          ("db-26dot5", 12),
          ("db-26", 13),
          ("db-25dot5", 14),
          ("db-25", 15),
          ("db-24dot5", 16),
          ("db-24", 17),
          ("db-23dot5", 18),
          ("db-23", 19),
          ("db-22dot5", 20),
          ("db-22", 21),
          ("db-21dot5", 22),
          ("db-21", 23),
          ("db-20dot5", 24),
          ("db-20", 25),
          ("db-19dot5", 26),
          ("db-19", 27),
          ("db-18dot5", 28),
          ("db-18", 29),
          ("db-17dot5", 30),
          ("db-17", 31),
          ("db-16dot5", 32),
          ("db-16", 33),
          ("db-15dot5", 34),
          ("db-15", 35),
          ("db-14dot5", 36),
          ("db-14", 37),
          ("db-13dot5", 38),
          ("db-13", 39),
          ("db-12dot5", 40),
          ("db-12", 41),
          ("db-11dot5", 42),
          ("db-11", 43),
          ("db-10dot5", 44),
          ("db-10", 45),
          ("db-9dot5", 46),
          ("db-9", 47),
          ("db-8dot5", 48),
          ("db-8", 49),
          ("db-7dot5", 50),
          ("db-7", 51),
          ("db-6dot5", 52),
          ("db-6", 53),
          ("db-5dot5", 54),
          ("db-5", 55),
          ("db-4dot5", 56),
          ("db-4", 57),
          ("db-3dot5", 58),
          ("db-3", 59),
          ("db-2dot5", 60),
          ("db-2", 61),
          ("db-1dot5", 62),
          ("db-1", 63),
          ("db-0dot5", 64),
          ("db-0", 65),
          ("db0dot5", 66),
          ("db1", 67),
          ("db1dot5", 68),
          ("db2", 69),
          ("db2dot5", 70),
          ("db3", 71))
    )


_Mc2200_FESFPWANThreshold_Type.__name__ = "Integer32"
_Mc2200_FESFPWANThreshold_Object = MibTableColumn
mc2200_FESFPWANThreshold = _Mc2200_FESFPWANThreshold_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 63),
    _Mc2200_FESFPWANThreshold_Type()
)
mc2200_FESFPWANThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FESFPWANThreshold.setStatus("current")


class _Mc2200_FESFPTrapFilterLocalLAN_Type(Integer32):
    """Custom type mc2200_FESFPTrapFilterLocalLAN based on Integer32"""
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


_Mc2200_FESFPTrapFilterLocalLAN_Type.__name__ = "Integer32"
_Mc2200_FESFPTrapFilterLocalLAN_Object = MibTableColumn
mc2200_FESFPTrapFilterLocalLAN = _Mc2200_FESFPTrapFilterLocalLAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 64),
    _Mc2200_FESFPTrapFilterLocalLAN_Type()
)
mc2200_FESFPTrapFilterLocalLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FESFPTrapFilterLocalLAN.setStatus("current")


class _Mc2200_FESFPTrapFilterLocalWAN_Type(Integer32):
    """Custom type mc2200_FESFPTrapFilterLocalWAN based on Integer32"""
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


_Mc2200_FESFPTrapFilterLocalWAN_Type.__name__ = "Integer32"
_Mc2200_FESFPTrapFilterLocalWAN_Object = MibTableColumn
mc2200_FESFPTrapFilterLocalWAN = _Mc2200_FESFPTrapFilterLocalWAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 65),
    _Mc2200_FESFPTrapFilterLocalWAN_Type()
)
mc2200_FESFPTrapFilterLocalWAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FESFPTrapFilterLocalWAN.setStatus("current")


class _Mc2200_FESFPTrapFilterRemotePower_Type(Integer32):
    """Custom type mc2200_FESFPTrapFilterRemotePower based on Integer32"""
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


_Mc2200_FESFPTrapFilterRemotePower_Type.__name__ = "Integer32"
_Mc2200_FESFPTrapFilterRemotePower_Object = MibTableColumn
mc2200_FESFPTrapFilterRemotePower = _Mc2200_FESFPTrapFilterRemotePower_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 66),
    _Mc2200_FESFPTrapFilterRemotePower_Type()
)
mc2200_FESFPTrapFilterRemotePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FESFPTrapFilterRemotePower.setStatus("current")


class _Mc2200_FESFPTrapFilterRemoteLAN_Type(Integer32):
    """Custom type mc2200_FESFPTrapFilterRemoteLAN based on Integer32"""
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


_Mc2200_FESFPTrapFilterRemoteLAN_Type.__name__ = "Integer32"
_Mc2200_FESFPTrapFilterRemoteLAN_Object = MibTableColumn
mc2200_FESFPTrapFilterRemoteLAN = _Mc2200_FESFPTrapFilterRemoteLAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 67),
    _Mc2200_FESFPTrapFilterRemoteLAN_Type()
)
mc2200_FESFPTrapFilterRemoteLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FESFPTrapFilterRemoteLAN.setStatus("current")


class _Mc2200_FESFPTrapFilterRemoteWAN_Type(Integer32):
    """Custom type mc2200_FESFPTrapFilterRemoteWAN based on Integer32"""
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


_Mc2200_FESFPTrapFilterRemoteWAN_Type.__name__ = "Integer32"
_Mc2200_FESFPTrapFilterRemoteWAN_Object = MibTableColumn
mc2200_FESFPTrapFilterRemoteWAN = _Mc2200_FESFPTrapFilterRemoteWAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 68),
    _Mc2200_FESFPTrapFilterRemoteWAN_Type()
)
mc2200_FESFPTrapFilterRemoteWAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FESFPTrapFilterRemoteWAN.setStatus("current")


class _Mc2200_FESFPLoopback_Type(Integer32):
    """Custom type mc2200_FESFPLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("local_lanouter", 2),
          ("local_laninner", 3),
          ("local_wanouter", 4),
          ("local_waninner", 5),
          ("remote_lanouter", 6),
          ("remote_laninner", 7))
    )


_Mc2200_FESFPLoopback_Type.__name__ = "Integer32"
_Mc2200_FESFPLoopback_Object = MibTableColumn
mc2200_FESFPLoopback = _Mc2200_FESFPLoopback_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 69),
    _Mc2200_FESFPLoopback_Type()
)
mc2200_FESFPLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FESFPLoopback.setStatus("mandatory")
_Mc2200_FESFPCardType_Type = DisplayString
_Mc2200_FESFPCardType_Object = MibTableColumn
mc2200_FESFPCardType = _Mc2200_FESFPCardType_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 11, 1, 70),
    _Mc2200_FESFPCardType_Type()
)
mc2200_FESFPCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FESFPCardType.setStatus("current")
_Mc2200_GESFPTable_Object = MibTable
mc2200_GESFPTable = _Mc2200_GESFPTable_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12)
)
if mibBuilder.loadTexts:
    mc2200_GESFPTable.setStatus("current")
_Mc2200_GESFPEntry_Object = MibTableRow
mc2200_GESFPEntry = _Mc2200_GESFPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1)
)
mc2200_GESFPEntry.setIndexNames(
    (0, "OnAccess2200-MIB", "mc2200-GESFPCardIndex"),
)
if mibBuilder.loadTexts:
    mc2200_GESFPEntry.setStatus("current")


class _Mc2200_GESFPCardIndex_Type(Integer32):
    """Custom type mc2200_GESFPCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("card01", 1),
          ("card02", 2),
          ("card03", 3),
          ("card04", 4),
          ("card05", 5),
          ("card06", 6),
          ("card07", 7),
          ("card08", 8),
          ("card09", 9),
          ("card10", 10),
          ("card11", 11),
          ("card12", 12),
          ("card13", 13),
          ("card14", 14),
          ("card15", 15))
    )


_Mc2200_GESFPCardIndex_Type.__name__ = "Integer32"
_Mc2200_GESFPCardIndex_Object = MibTableColumn
mc2200_GESFPCardIndex = _Mc2200_GESFPCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 1),
    _Mc2200_GESFPCardIndex_Type()
)
mc2200_GESFPCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPCardIndex.setStatus("current")


class _Mc2200_GESFPLocalTXLink_Type(Integer32):
    """Custom type mc2200_GESFPLocalTXLink based on Integer32"""
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


_Mc2200_GESFPLocalTXLink_Type.__name__ = "Integer32"
_Mc2200_GESFPLocalTXLink_Object = MibTableColumn
mc2200_GESFPLocalTXLink = _Mc2200_GESFPLocalTXLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 2),
    _Mc2200_GESFPLocalTXLink_Type()
)
mc2200_GESFPLocalTXLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPLocalTXLink.setStatus("mandatory")
_Mc2200_GESFPLocalWANSFPInfo_Type = DisplayString
_Mc2200_GESFPLocalWANSFPInfo_Object = MibTableColumn
mc2200_GESFPLocalWANSFPInfo = _Mc2200_GESFPLocalWANSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 3),
    _Mc2200_GESFPLocalWANSFPInfo_Type()
)
mc2200_GESFPLocalWANSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPLocalWANSFPInfo.setStatus("current")


class _Mc2200_GESFPLocalWANLink_Type(Integer32):
    """Custom type mc2200_GESFPLocalWANLink based on Integer32"""
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


_Mc2200_GESFPLocalWANLink_Type.__name__ = "Integer32"
_Mc2200_GESFPLocalWANLink_Object = MibTableColumn
mc2200_GESFPLocalWANLink = _Mc2200_GESFPLocalWANLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 4),
    _Mc2200_GESFPLocalWANLink_Type()
)
mc2200_GESFPLocalWANLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPLocalWANLink.setStatus("current")


class _Mc2200_GESFPLocalTXDownStreamBW_Type(Integer32):
    """Custom type mc2200_GESFPLocalTXDownStreamBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              35,
              40,
              45,
              50,
              55,
              60,
              65,
              70,
              75,
              80,
              85,
              90,
              95,
              100,
              150,
              200,
              250,
              300,
              350,
              400,
              450,
              500,
              550,
              600,
              650,
              700,
              750,
              800,
              850,
              900,
              950,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate35M", 35),
          ("rate40M", 40),
          ("rate45M", 45),
          ("rate50M", 50),
          ("rate55M", 55),
          ("rate60M", 60),
          ("rate65M", 65),
          ("rate70M", 70),
          ("rate75M", 75),
          ("rate80M", 80),
          ("rate85M", 85),
          ("rate90M", 90),
          ("rate95M", 95),
          ("rate100M", 100),
          ("rate150M", 150),
          ("rate200M", 200),
          ("rate250M", 250),
          ("rate300M", 300),
          ("rate350M", 350),
          ("rate400M", 400),
          ("rate450M", 450),
          ("rate500M", 500),
          ("rate550M", 550),
          ("rate600M", 600),
          ("rate650M", 650),
          ("rate700M", 700),
          ("rate750M", 750),
          ("rate800M", 800),
          ("rate850M", 850),
          ("rate900M", 900),
          ("rate950M", 950),
          ("rate1000M", 1000))
    )


_Mc2200_GESFPLocalTXDownStreamBW_Type.__name__ = "Integer32"
_Mc2200_GESFPLocalTXDownStreamBW_Object = MibTableColumn
mc2200_GESFPLocalTXDownStreamBW = _Mc2200_GESFPLocalTXDownStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 5),
    _Mc2200_GESFPLocalTXDownStreamBW_Type()
)
mc2200_GESFPLocalTXDownStreamBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPLocalTXDownStreamBW.setStatus("current")


class _Mc2200_GESFPLocalTXUpStreamBW_Type(Integer32):
    """Custom type mc2200_GESFPLocalTXUpStreamBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              35,
              40,
              45,
              50,
              55,
              60,
              65,
              70,
              75,
              80,
              85,
              90,
              95,
              100,
              150,
              200,
              250,
              300,
              350,
              400,
              450,
              500,
              550,
              600,
              650,
              700,
              750,
              800,
              850,
              900,
              950,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate35M", 35),
          ("rate40M", 40),
          ("rate45M", 45),
          ("rate50M", 50),
          ("rate55M", 55),
          ("rate60M", 60),
          ("rate65M", 65),
          ("rate70M", 70),
          ("rate75M", 75),
          ("rate80M", 80),
          ("rate85M", 85),
          ("rate90M", 90),
          ("rate95M", 95),
          ("rate100M", 100),
          ("rate150M", 150),
          ("rate200M", 200),
          ("rate250M", 250),
          ("rate300M", 300),
          ("rate350M", 350),
          ("rate400M", 400),
          ("rate450M", 450),
          ("rate500M", 500),
          ("rate550M", 550),
          ("rate600M", 600),
          ("rate650M", 650),
          ("rate700M", 700),
          ("rate750M", 750),
          ("rate800M", 800),
          ("rate850M", 850),
          ("rate900M", 900),
          ("rate950M", 950),
          ("rate1000M", 1000))
    )


_Mc2200_GESFPLocalTXUpStreamBW_Type.__name__ = "Integer32"
_Mc2200_GESFPLocalTXUpStreamBW_Object = MibTableColumn
mc2200_GESFPLocalTXUpStreamBW = _Mc2200_GESFPLocalTXUpStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 6),
    _Mc2200_GESFPLocalTXUpStreamBW_Type()
)
mc2200_GESFPLocalTXUpStreamBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPLocalTXUpStreamBW.setStatus("current")


class _Mc2200_GESFPLocalTXMode_Type(Integer32):
    """Custom type mc2200_GESFPLocalTXMode based on Integer32"""
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
        *(("auto-10-100-1000", 1),
          ("mode1000F", 2),
          ("mode100F", 3),
          ("mode10F", 4),
          ("mode100H", 5),
          ("mode10H", 6))
    )


_Mc2200_GESFPLocalTXMode_Type.__name__ = "Integer32"
_Mc2200_GESFPLocalTXMode_Object = MibTableColumn
mc2200_GESFPLocalTXMode = _Mc2200_GESFPLocalTXMode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 7),
    _Mc2200_GESFPLocalTXMode_Type()
)
mc2200_GESFPLocalTXMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPLocalTXMode.setStatus("current")


class _Mc2200_GESFPLocalTXMDIX_Type(Integer32):
    """Custom type mc2200_GESFPLocalTXMDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("mdi", 2),
          ("mdix", 3))
    )


_Mc2200_GESFPLocalTXMDIX_Type.__name__ = "Integer32"
_Mc2200_GESFPLocalTXMDIX_Object = MibTableColumn
mc2200_GESFPLocalTXMDIX = _Mc2200_GESFPLocalTXMDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 8),
    _Mc2200_GESFPLocalTXMDIX_Type()
)
mc2200_GESFPLocalTXMDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPLocalTXMDIX.setStatus("current")
_Mc2200_GESFPRxGoodOctets_Type = Counter64
_Mc2200_GESFPRxGoodOctets_Object = MibTableColumn
mc2200_GESFPRxGoodOctets = _Mc2200_GESFPRxGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 9),
    _Mc2200_GESFPRxGoodOctets_Type()
)
mc2200_GESFPRxGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPRxGoodOctets.setStatus("current")
_Mc2200_GESFPRxBadOctets_Type = Counter64
_Mc2200_GESFPRxBadOctets_Object = MibTableColumn
mc2200_GESFPRxBadOctets = _Mc2200_GESFPRxBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 11),
    _Mc2200_GESFPRxBadOctets_Type()
)
mc2200_GESFPRxBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPRxBadOctets.setStatus("current")
_Mc2200_GESFPTxFCSErr_Type = Counter64
_Mc2200_GESFPTxFCSErr_Object = MibTableColumn
mc2200_GESFPTxFCSErr = _Mc2200_GESFPTxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 12),
    _Mc2200_GESFPTxFCSErr_Type()
)
mc2200_GESFPTxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPTxFCSErr.setStatus("current")
_Mc2200_GESFPRxUnicast_Type = Counter64
_Mc2200_GESFPRxUnicast_Object = MibTableColumn
mc2200_GESFPRxUnicast = _Mc2200_GESFPRxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 13),
    _Mc2200_GESFPRxUnicast_Type()
)
mc2200_GESFPRxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPRxUnicast.setStatus("current")
_Mc2200_GESFPTxDeferred_Type = Counter64
_Mc2200_GESFPTxDeferred_Object = MibTableColumn
mc2200_GESFPTxDeferred = _Mc2200_GESFPTxDeferred_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 14),
    _Mc2200_GESFPTxDeferred_Type()
)
mc2200_GESFPTxDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPTxDeferred.setStatus("current")
_Mc2200_GESFPRxBroadcasts_Type = Counter64
_Mc2200_GESFPRxBroadcasts_Object = MibTableColumn
mc2200_GESFPRxBroadcasts = _Mc2200_GESFPRxBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 15),
    _Mc2200_GESFPRxBroadcasts_Type()
)
mc2200_GESFPRxBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPRxBroadcasts.setStatus("current")
_Mc2200_GESFPRxMulticasts_Type = Counter64
_Mc2200_GESFPRxMulticasts_Object = MibTableColumn
mc2200_GESFPRxMulticasts = _Mc2200_GESFPRxMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 16),
    _Mc2200_GESFPRxMulticasts_Type()
)
mc2200_GESFPRxMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPRxMulticasts.setStatus("current")
_Mc2200_GESFPRx64Octets_Type = Counter64
_Mc2200_GESFPRx64Octets_Object = MibTableColumn
mc2200_GESFPRx64Octets = _Mc2200_GESFPRx64Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 17),
    _Mc2200_GESFPRx64Octets_Type()
)
mc2200_GESFPRx64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPRx64Octets.setStatus("current")
_Mc2200_GESFPRx65to127Octets_Type = Counter64
_Mc2200_GESFPRx65to127Octets_Object = MibTableColumn
mc2200_GESFPRx65to127Octets = _Mc2200_GESFPRx65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 18),
    _Mc2200_GESFPRx65to127Octets_Type()
)
mc2200_GESFPRx65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPRx65to127Octets.setStatus("current")
_Mc2200_GESFPRx128to255Octets_Type = Counter64
_Mc2200_GESFPRx128to255Octets_Object = MibTableColumn
mc2200_GESFPRx128to255Octets = _Mc2200_GESFPRx128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 19),
    _Mc2200_GESFPRx128to255Octets_Type()
)
mc2200_GESFPRx128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPRx128to255Octets.setStatus("current")
_Mc2200_GESFPRx256to511Octets_Type = Counter64
_Mc2200_GESFPRx256to511Octets_Object = MibTableColumn
mc2200_GESFPRx256to511Octets = _Mc2200_GESFPRx256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 20),
    _Mc2200_GESFPRx256to511Octets_Type()
)
mc2200_GESFPRx256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPRx256to511Octets.setStatus("current")
_Mc2200_GESFPRx512to1023Octets_Type = Counter64
_Mc2200_GESFPRx512to1023Octets_Object = MibTableColumn
mc2200_GESFPRx512to1023Octets = _Mc2200_GESFPRx512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 21),
    _Mc2200_GESFPRx512to1023Octets_Type()
)
mc2200_GESFPRx512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPRx512to1023Octets.setStatus("current")
_Mc2200_GESFPRx1024toMaxOctets_Type = Counter64
_Mc2200_GESFPRx1024toMaxOctets_Object = MibTableColumn
mc2200_GESFPRx1024toMaxOctets = _Mc2200_GESFPRx1024toMaxOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 22),
    _Mc2200_GESFPRx1024toMaxOctets_Type()
)
mc2200_GESFPRx1024toMaxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPRx1024toMaxOctets.setStatus("current")
_Mc2200_GESFPTxOctets_Type = Counter64
_Mc2200_GESFPTxOctets_Object = MibTableColumn
mc2200_GESFPTxOctets = _Mc2200_GESFPTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 23),
    _Mc2200_GESFPTxOctets_Type()
)
mc2200_GESFPTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPTxOctets.setStatus("current")
_Mc2200_GESFPTxUnicast_Type = Counter64
_Mc2200_GESFPTxUnicast_Object = MibTableColumn
mc2200_GESFPTxUnicast = _Mc2200_GESFPTxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 25),
    _Mc2200_GESFPTxUnicast_Type()
)
mc2200_GESFPTxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPTxUnicast.setStatus("current")
_Mc2200_GESFPTxExcessive_Type = Counter64
_Mc2200_GESFPTxExcessive_Object = MibTableColumn
mc2200_GESFPTxExcessive = _Mc2200_GESFPTxExcessive_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 26),
    _Mc2200_GESFPTxExcessive_Type()
)
mc2200_GESFPTxExcessive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPTxExcessive.setStatus("current")
_Mc2200_GESFPTxMulticasts_Type = Counter64
_Mc2200_GESFPTxMulticasts_Object = MibTableColumn
mc2200_GESFPTxMulticasts = _Mc2200_GESFPTxMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 27),
    _Mc2200_GESFPTxMulticasts_Type()
)
mc2200_GESFPTxMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPTxMulticasts.setStatus("current")
_Mc2200_GESFPTxBroadcasts_Type = Counter64
_Mc2200_GESFPTxBroadcasts_Object = MibTableColumn
mc2200_GESFPTxBroadcasts = _Mc2200_GESFPTxBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 28),
    _Mc2200_GESFPTxBroadcasts_Type()
)
mc2200_GESFPTxBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPTxBroadcasts.setStatus("current")
_Mc2200_GESFPTxSingle_Type = Counter64
_Mc2200_GESFPTxSingle_Object = MibTableColumn
mc2200_GESFPTxSingle = _Mc2200_GESFPTxSingle_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 29),
    _Mc2200_GESFPTxSingle_Type()
)
mc2200_GESFPTxSingle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPTxSingle.setStatus("current")
_Mc2200_GESFPTxPause_Type = Counter64
_Mc2200_GESFPTxPause_Object = MibTableColumn
mc2200_GESFPTxPause = _Mc2200_GESFPTxPause_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 30),
    _Mc2200_GESFPTxPause_Type()
)
mc2200_GESFPTxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPTxPause.setStatus("current")
_Mc2200_GESFPRxPause_Type = Counter64
_Mc2200_GESFPRxPause_Object = MibTableColumn
mc2200_GESFPRxPause = _Mc2200_GESFPRxPause_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 31),
    _Mc2200_GESFPRxPause_Type()
)
mc2200_GESFPRxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPRxPause.setStatus("current")
_Mc2200_GESFPTxMultiple_Type = Counter64
_Mc2200_GESFPTxMultiple_Object = MibTableColumn
mc2200_GESFPTxMultiple = _Mc2200_GESFPTxMultiple_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 32),
    _Mc2200_GESFPTxMultiple_Type()
)
mc2200_GESFPTxMultiple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPTxMultiple.setStatus("current")
_Mc2200_GESFPRxUndersize_Type = Counter64
_Mc2200_GESFPRxUndersize_Object = MibTableColumn
mc2200_GESFPRxUndersize = _Mc2200_GESFPRxUndersize_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 33),
    _Mc2200_GESFPRxUndersize_Type()
)
mc2200_GESFPRxUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPRxUndersize.setStatus("current")
_Mc2200_GESFPRxFragments_Type = Counter64
_Mc2200_GESFPRxFragments_Object = MibTableColumn
mc2200_GESFPRxFragments = _Mc2200_GESFPRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 34),
    _Mc2200_GESFPRxFragments_Type()
)
mc2200_GESFPRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPRxFragments.setStatus("current")
_Mc2200_GESFPRxOversize_Type = Counter64
_Mc2200_GESFPRxOversize_Object = MibTableColumn
mc2200_GESFPRxOversize = _Mc2200_GESFPRxOversize_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 35),
    _Mc2200_GESFPRxOversize_Type()
)
mc2200_GESFPRxOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPRxOversize.setStatus("current")
_Mc2200_GESFPRxJabber_Type = Counter64
_Mc2200_GESFPRxJabber_Object = MibTableColumn
mc2200_GESFPRxJabber = _Mc2200_GESFPRxJabber_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 36),
    _Mc2200_GESFPRxJabber_Type()
)
mc2200_GESFPRxJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPRxJabber.setStatus("current")
_Mc2200_GESFPRxErr_Type = Counter64
_Mc2200_GESFPRxErr_Object = MibTableColumn
mc2200_GESFPRxErr = _Mc2200_GESFPRxErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 37),
    _Mc2200_GESFPRxErr_Type()
)
mc2200_GESFPRxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPRxErr.setStatus("current")
_Mc2200_GESFPRxFCSErr_Type = Counter64
_Mc2200_GESFPRxFCSErr_Object = MibTableColumn
mc2200_GESFPRxFCSErr = _Mc2200_GESFPRxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 38),
    _Mc2200_GESFPRxFCSErr_Type()
)
mc2200_GESFPRxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPRxFCSErr.setStatus("current")
_Mc2200_GESFPTxCollisions_Type = Counter64
_Mc2200_GESFPTxCollisions_Object = MibTableColumn
mc2200_GESFPTxCollisions = _Mc2200_GESFPTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 39),
    _Mc2200_GESFPTxCollisions_Type()
)
mc2200_GESFPTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPTxCollisions.setStatus("current")
_Mc2200_GESFPTxLate_Type = Counter64
_Mc2200_GESFPTxLate_Object = MibTableColumn
mc2200_GESFPTxLate = _Mc2200_GESFPTxLate_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 40),
    _Mc2200_GESFPTxLate_Type()
)
mc2200_GESFPTxLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPTxLate.setStatus("current")


class _Mc2200_GESFPRemoteTXLink_Type(Integer32):
    """Custom type mc2200_GESFPRemoteTXLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_GESFPRemoteTXLink_Type.__name__ = "Integer32"
_Mc2200_GESFPRemoteTXLink_Object = MibTableColumn
mc2200_GESFPRemoteTXLink = _Mc2200_GESFPRemoteTXLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 41),
    _Mc2200_GESFPRemoteTXLink_Type()
)
mc2200_GESFPRemoteTXLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPRemoteTXLink.setStatus("mandatory")
_Mc2200_GESFPRemoteWANSFPInfo_Type = DisplayString
_Mc2200_GESFPRemoteWANSFPInfo_Object = MibTableColumn
mc2200_GESFPRemoteWANSFPInfo = _Mc2200_GESFPRemoteWANSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 42),
    _Mc2200_GESFPRemoteWANSFPInfo_Type()
)
mc2200_GESFPRemoteWANSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPRemoteWANSFPInfo.setStatus("current")


class _Mc2200_GESFPRemoteWANLink_Type(Integer32):
    """Custom type mc2200_GESFPRemoteWANLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_GESFPRemoteWANLink_Type.__name__ = "Integer32"
_Mc2200_GESFPRemoteWANLink_Object = MibTableColumn
mc2200_GESFPRemoteWANLink = _Mc2200_GESFPRemoteWANLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 43),
    _Mc2200_GESFPRemoteWANLink_Type()
)
mc2200_GESFPRemoteWANLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPRemoteWANLink.setStatus("current")


class _Mc2200_GESFPRemoteTXMode_Type(Integer32):
    """Custom type mc2200_GESFPRemoteTXMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto-10-100-1000", 1),
          ("mode1000F", 2),
          ("mode100F", 3),
          ("mode10F", 4),
          ("mode100H", 5),
          ("mode10H", 6))
    )


_Mc2200_GESFPRemoteTXMode_Type.__name__ = "Integer32"
_Mc2200_GESFPRemoteTXMode_Object = MibTableColumn
mc2200_GESFPRemoteTXMode = _Mc2200_GESFPRemoteTXMode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 44),
    _Mc2200_GESFPRemoteTXMode_Type()
)
mc2200_GESFPRemoteTXMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPRemoteTXMode.setStatus("current")


class _Mc2200_GESFPRemoteTXMDIX_Type(Integer32):
    """Custom type mc2200_GESFPRemoteTXMDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mdi", 2),
          ("mdix", 3))
    )


_Mc2200_GESFPRemoteTXMDIX_Type.__name__ = "Integer32"
_Mc2200_GESFPRemoteTXMDIX_Object = MibTableColumn
mc2200_GESFPRemoteTXMDIX = _Mc2200_GESFPRemoteTXMDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 45),
    _Mc2200_GESFPRemoteTXMDIX_Type()
)
mc2200_GESFPRemoteTXMDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPRemoteTXMDIX.setStatus("current")
_Mc2200_GESFPRemoteIPAddress_Type = IpAddress
_Mc2200_GESFPRemoteIPAddress_Object = MibTableColumn
mc2200_GESFPRemoteIPAddress = _Mc2200_GESFPRemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 46),
    _Mc2200_GESFPRemoteIPAddress_Type()
)
mc2200_GESFPRemoteIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPRemoteIPAddress.setStatus("mandatory")
_Mc2200_GESFPRemoteSubnetMask_Type = IpAddress
_Mc2200_GESFPRemoteSubnetMask_Object = MibTableColumn
mc2200_GESFPRemoteSubnetMask = _Mc2200_GESFPRemoteSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 47),
    _Mc2200_GESFPRemoteSubnetMask_Type()
)
mc2200_GESFPRemoteSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPRemoteSubnetMask.setStatus("mandatory")
_Mc2200_GESFPRemoteGateWay_Type = IpAddress
_Mc2200_GESFPRemoteGateWay_Object = MibTableColumn
mc2200_GESFPRemoteGateWay = _Mc2200_GESFPRemoteGateWay_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 48),
    _Mc2200_GESFPRemoteGateWay_Type()
)
mc2200_GESFPRemoteGateWay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPRemoteGateWay.setStatus("mandatory")


class _Mc2200_GESFPRemoteVLANEnable_Type(Integer32):
    """Custom type mc2200_GESFPRemoteVLANEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("enable", 1),
          ("disable", 2))
    )


_Mc2200_GESFPRemoteVLANEnable_Type.__name__ = "Integer32"
_Mc2200_GESFPRemoteVLANEnable_Object = MibTableColumn
mc2200_GESFPRemoteVLANEnable = _Mc2200_GESFPRemoteVLANEnable_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 49),
    _Mc2200_GESFPRemoteVLANEnable_Type()
)
mc2200_GESFPRemoteVLANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPRemoteVLANEnable.setStatus("mandatory")
_Mc2200_GESFPRemoteVID_Type = Integer32
_Mc2200_GESFPRemoteVID_Object = MibTableColumn
mc2200_GESFPRemoteVID = _Mc2200_GESFPRemoteVID_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 50),
    _Mc2200_GESFPRemoteVID_Type()
)
mc2200_GESFPRemoteVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPRemoteVID.setStatus("mandatory")


class _Mc2200_GESFPRemoteAlarm_Type(Integer32):
    """Custom type mc2200_GESFPRemoteAlarm based on Integer32"""
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


_Mc2200_GESFPRemoteAlarm_Type.__name__ = "Integer32"
_Mc2200_GESFPRemoteAlarm_Object = MibTableColumn
mc2200_GESFPRemoteAlarm = _Mc2200_GESFPRemoteAlarm_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 51),
    _Mc2200_GESFPRemoteAlarm_Type()
)
mc2200_GESFPRemoteAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPRemoteAlarm.setStatus("current")


class _Mc2200_GESFPRFD_Type(Integer32):
    """Custom type mc2200_GESFPRFD based on Integer32"""
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


_Mc2200_GESFPRFD_Type.__name__ = "Integer32"
_Mc2200_GESFPRFD_Object = MibTableColumn
mc2200_GESFPRFD = _Mc2200_GESFPRFD_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 52),
    _Mc2200_GESFPRFD_Type()
)
mc2200_GESFPRFD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPRFD.setStatus("current")
_Mc2200_GESFPDefault_Type = Integer32
_Mc2200_GESFPDefault_Object = MibTableColumn
mc2200_GESFPDefault = _Mc2200_GESFPDefault_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 53),
    _Mc2200_GESFPDefault_Type()
)
mc2200_GESFPDefault.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mc2200_GESFPDefault.setStatus("current")
_Mc2200_GESFPReboot_Type = Integer32
_Mc2200_GESFPReboot_Object = MibTableColumn
mc2200_GESFPReboot = _Mc2200_GESFPReboot_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 54),
    _Mc2200_GESFPReboot_Type()
)
mc2200_GESFPReboot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mc2200_GESFPReboot.setStatus("current")


class _Mc2200_GESFPLocalTXSpeed_Type(Integer32):
    """Custom type mc2200_GESFPLocalTXSpeed based on Integer32"""
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
        *(("speed1000M", 1),
          ("speed100M", 2),
          ("speed10M", 3),
          ("down", 4))
    )


_Mc2200_GESFPLocalTXSpeed_Type.__name__ = "Integer32"
_Mc2200_GESFPLocalTXSpeed_Object = MibTableColumn
mc2200_GESFPLocalTXSpeed = _Mc2200_GESFPLocalTXSpeed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 55),
    _Mc2200_GESFPLocalTXSpeed_Type()
)
mc2200_GESFPLocalTXSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPLocalTXSpeed.setStatus("mandatory")


class _Mc2200_GESFPRemoteTXSpeed_Type(Integer32):
    """Custom type mc2200_GESFPRemoteTXSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("speed1000M", 1),
          ("speed100M", 2),
          ("speed10M", 3),
          ("down", 4))
    )


_Mc2200_GESFPRemoteTXSpeed_Type.__name__ = "Integer32"
_Mc2200_GESFPRemoteTXSpeed_Object = MibTableColumn
mc2200_GESFPRemoteTXSpeed = _Mc2200_GESFPRemoteTXSpeed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 56),
    _Mc2200_GESFPRemoteTXSpeed_Type()
)
mc2200_GESFPRemoteTXSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPRemoteTXSpeed.setStatus("mandatory")
_Mc2200_GESFPLocalportuser_Type = DisplayString
_Mc2200_GESFPLocalportuser_Object = MibTableColumn
mc2200_GESFPLocalportuser = _Mc2200_GESFPLocalportuser_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 57),
    _Mc2200_GESFPLocalportuser_Type()
)
mc2200_GESFPLocalportuser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPLocalportuser.setStatus("current")
_Mc2200_GESFPRemoteportuser_Type = DisplayString
_Mc2200_GESFPRemoteportuser_Object = MibTableColumn
mc2200_GESFPRemoteportuser = _Mc2200_GESFPRemoteportuser_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 58),
    _Mc2200_GESFPRemoteportuser_Type()
)
mc2200_GESFPRemoteportuser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPRemoteportuser.setStatus("current")


class _Mc2200_GESFPLocalTXDuplex_Type(Integer32):
    """Custom type mc2200_GESFPLocalTXDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2),
          ("down", 3))
    )


_Mc2200_GESFPLocalTXDuplex_Type.__name__ = "Integer32"
_Mc2200_GESFPLocalTXDuplex_Object = MibTableColumn
mc2200_GESFPLocalTXDuplex = _Mc2200_GESFPLocalTXDuplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 59),
    _Mc2200_GESFPLocalTXDuplex_Type()
)
mc2200_GESFPLocalTXDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPLocalTXDuplex.setStatus("mandatory")


class _Mc2200_GESFPRemoteTXDuplex_Type(Integer32):
    """Custom type mc2200_GESFPRemoteTXDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("fullDuplex", 1),
          ("halfDuplex", 2),
          ("down", 3))
    )


_Mc2200_GESFPRemoteTXDuplex_Type.__name__ = "Integer32"
_Mc2200_GESFPRemoteTXDuplex_Object = MibTableColumn
mc2200_GESFPRemoteTXDuplex = _Mc2200_GESFPRemoteTXDuplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 60),
    _Mc2200_GESFPRemoteTXDuplex_Type()
)
mc2200_GESFPRemoteTXDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPRemoteTXDuplex.setStatus("mandatory")


class _Mc2200_GESFPFlowControl_Type(Integer32):
    """Custom type mc2200_GESFPFlowControl based on Integer32"""
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


_Mc2200_GESFPFlowControl_Type.__name__ = "Integer32"
_Mc2200_GESFPFlowControl_Object = MibTableColumn
mc2200_GESFPFlowControl = _Mc2200_GESFPFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 61),
    _Mc2200_GESFPFlowControl_Type()
)
mc2200_GESFPFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPFlowControl.setStatus("current")


class _Mc2200_GESFPWANOpticalPowerCheck_Type(Integer32):
    """Custom type mc2200_GESFPWANOpticalPowerCheck based on Integer32"""
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


_Mc2200_GESFPWANOpticalPowerCheck_Type.__name__ = "Integer32"
_Mc2200_GESFPWANOpticalPowerCheck_Object = MibTableColumn
mc2200_GESFPWANOpticalPowerCheck = _Mc2200_GESFPWANOpticalPowerCheck_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 62),
    _Mc2200_GESFPWANOpticalPowerCheck_Type()
)
mc2200_GESFPWANOpticalPowerCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPWANOpticalPowerCheck.setStatus("current")


class _Mc2200_GESFPWANThreshold_Type(Integer32):
    """Custom type mc2200_GESFPWANThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71)
        )
    )
    namedValues = NamedValues(
        *(("db-32", 1),
          ("db-31dot5", 2),
          ("db-31", 3),
          ("db-30dot5", 4),
          ("db-30", 5),
          ("db-29dot5", 6),
          ("db-29", 7),
          ("db-28dot5", 8),
          ("db-28", 9),
          ("db-27dot5", 10),
          ("db-27", 11),
          ("db-26dot5", 12),
          ("db-26", 13),
          ("db-25dot5", 14),
          ("db-25", 15),
          ("db-24dot5", 16),
          ("db-24", 17),
          ("db-23dot5", 18),
          ("db-23", 19),
          ("db-22dot5", 20),
          ("db-22", 21),
          ("db-21dot5", 22),
          ("db-21", 23),
          ("db-20dot5", 24),
          ("db-20", 25),
          ("db-19dot5", 26),
          ("db-19", 27),
          ("db-18dot5", 28),
          ("db-18", 29),
          ("db-17dot5", 30),
          ("db-17", 31),
          ("db-16dot5", 32),
          ("db-16", 33),
          ("db-15dot5", 34),
          ("db-15", 35),
          ("db-14dot5", 36),
          ("db-14", 37),
          ("db-13dot5", 38),
          ("db-13", 39),
          ("db-12dot5", 40),
          ("db-12", 41),
          ("db-11dot5", 42),
          ("db-11", 43),
          ("db-10dot5", 44),
          ("db-10", 45),
          ("db-9dot5", 46),
          ("db-9", 47),
          ("db-8dot5", 48),
          ("db-8", 49),
          ("db-7dot5", 50),
          ("db-7", 51),
          ("db-6dot5", 52),
          ("db-6", 53),
          ("db-5dot5", 54),
          ("db-5", 55),
          ("db-4dot5", 56),
          ("db-4", 57),
          ("db-3dot5", 58),
          ("db-3", 59),
          ("db-2dot5", 60),
          ("db-2", 61),
          ("db-1dot5", 62),
          ("db-1", 63),
          ("db-0dot5", 64),
          ("db-0", 65),
          ("db0dot5", 66),
          ("db1", 67),
          ("db1dot5", 68),
          ("db2", 69),
          ("db2dot5", 70),
          ("db3", 71))
    )


_Mc2200_GESFPWANThreshold_Type.__name__ = "Integer32"
_Mc2200_GESFPWANThreshold_Object = MibTableColumn
mc2200_GESFPWANThreshold = _Mc2200_GESFPWANThreshold_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 63),
    _Mc2200_GESFPWANThreshold_Type()
)
mc2200_GESFPWANThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPWANThreshold.setStatus("current")


class _Mc2200_GESFPTrapFilterLocalLAN_Type(Integer32):
    """Custom type mc2200_GESFPTrapFilterLocalLAN based on Integer32"""
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


_Mc2200_GESFPTrapFilterLocalLAN_Type.__name__ = "Integer32"
_Mc2200_GESFPTrapFilterLocalLAN_Object = MibTableColumn
mc2200_GESFPTrapFilterLocalLAN = _Mc2200_GESFPTrapFilterLocalLAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 64),
    _Mc2200_GESFPTrapFilterLocalLAN_Type()
)
mc2200_GESFPTrapFilterLocalLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPTrapFilterLocalLAN.setStatus("current")


class _Mc2200_GESFPTrapFilterLocalWAN_Type(Integer32):
    """Custom type mc2200_GESFPTrapFilterLocalWAN based on Integer32"""
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


_Mc2200_GESFPTrapFilterLocalWAN_Type.__name__ = "Integer32"
_Mc2200_GESFPTrapFilterLocalWAN_Object = MibTableColumn
mc2200_GESFPTrapFilterLocalWAN = _Mc2200_GESFPTrapFilterLocalWAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 65),
    _Mc2200_GESFPTrapFilterLocalWAN_Type()
)
mc2200_GESFPTrapFilterLocalWAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPTrapFilterLocalWAN.setStatus("current")


class _Mc2200_GESFPTrapFilterRemotePower_Type(Integer32):
    """Custom type mc2200_GESFPTrapFilterRemotePower based on Integer32"""
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


_Mc2200_GESFPTrapFilterRemotePower_Type.__name__ = "Integer32"
_Mc2200_GESFPTrapFilterRemotePower_Object = MibTableColumn
mc2200_GESFPTrapFilterRemotePower = _Mc2200_GESFPTrapFilterRemotePower_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 66),
    _Mc2200_GESFPTrapFilterRemotePower_Type()
)
mc2200_GESFPTrapFilterRemotePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPTrapFilterRemotePower.setStatus("current")


class _Mc2200_GESFPTrapFilterRemoteLAN_Type(Integer32):
    """Custom type mc2200_GESFPTrapFilterRemoteLAN based on Integer32"""
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


_Mc2200_GESFPTrapFilterRemoteLAN_Type.__name__ = "Integer32"
_Mc2200_GESFPTrapFilterRemoteLAN_Object = MibTableColumn
mc2200_GESFPTrapFilterRemoteLAN = _Mc2200_GESFPTrapFilterRemoteLAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 67),
    _Mc2200_GESFPTrapFilterRemoteLAN_Type()
)
mc2200_GESFPTrapFilterRemoteLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPTrapFilterRemoteLAN.setStatus("current")


class _Mc2200_GESFPTrapFilterRemoteWAN_Type(Integer32):
    """Custom type mc2200_GESFPTrapFilterRemoteWAN based on Integer32"""
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


_Mc2200_GESFPTrapFilterRemoteWAN_Type.__name__ = "Integer32"
_Mc2200_GESFPTrapFilterRemoteWAN_Object = MibTableColumn
mc2200_GESFPTrapFilterRemoteWAN = _Mc2200_GESFPTrapFilterRemoteWAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 68),
    _Mc2200_GESFPTrapFilterRemoteWAN_Type()
)
mc2200_GESFPTrapFilterRemoteWAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPTrapFilterRemoteWAN.setStatus("current")


class _Mc2200_GESFPLoopback_Type(Integer32):
    """Custom type mc2200_GESFPLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("local_lanouter", 2),
          ("local_laninner", 3),
          ("local_wanouter", 4),
          ("local_waninner", 5),
          ("remote_lanouter", 6),
          ("remote_laninner", 7))
    )


_Mc2200_GESFPLoopback_Type.__name__ = "Integer32"
_Mc2200_GESFPLoopback_Object = MibTableColumn
mc2200_GESFPLoopback = _Mc2200_GESFPLoopback_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 69),
    _Mc2200_GESFPLoopback_Type()
)
mc2200_GESFPLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPLoopback.setStatus("mandatory")
_Mc2200_GESFPCardType_Type = DisplayString
_Mc2200_GESFPCardType_Object = MibTableColumn
mc2200_GESFPCardType = _Mc2200_GESFPCardType_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 12, 1, 70),
    _Mc2200_GESFPCardType_Type()
)
mc2200_GESFPCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPCardType.setStatus("current")
_Mc2200_GEMC3Table_Object = MibTable
mc2200_GEMC3Table = _Mc2200_GEMC3Table_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13)
)
if mibBuilder.loadTexts:
    mc2200_GEMC3Table.setStatus("current")
_Mc2200_GEMC3Entry_Object = MibTableRow
mc2200_GEMC3Entry = _Mc2200_GEMC3Entry_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1)
)
mc2200_GEMC3Entry.setIndexNames(
    (0, "OnAccess2200-MIB", "mc2200-GEMC3CardIndex"),
)
if mibBuilder.loadTexts:
    mc2200_GEMC3Entry.setStatus("current")


class _Mc2200_GEMC3CardIndex_Type(Integer32):
    """Custom type mc2200_GEMC3CardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("card01", 1),
          ("card02", 2),
          ("card03", 3),
          ("card04", 4),
          ("card05", 5),
          ("card06", 6),
          ("card07", 7),
          ("card08", 8),
          ("card09", 9),
          ("card10", 10),
          ("card11", 11),
          ("card12", 12),
          ("card13", 13),
          ("card14", 14),
          ("card15", 15))
    )


_Mc2200_GEMC3CardIndex_Type.__name__ = "Integer32"
_Mc2200_GEMC3CardIndex_Object = MibTableColumn
mc2200_GEMC3CardIndex = _Mc2200_GEMC3CardIndex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 1),
    _Mc2200_GEMC3CardIndex_Type()
)
mc2200_GEMC3CardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3CardIndex.setStatus("current")
_Mc2200_GEMC3LocalLANSFPInfo_Type = DisplayString
_Mc2200_GEMC3LocalLANSFPInfo_Object = MibTableColumn
mc2200_GEMC3LocalLANSFPInfo = _Mc2200_GEMC3LocalLANSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 2),
    _Mc2200_GEMC3LocalLANSFPInfo_Type()
)
mc2200_GEMC3LocalLANSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3LocalLANSFPInfo.setStatus("current")


class _Mc2200_GEMC3LocalLANLink_Type(Integer32):
    """Custom type mc2200_GEMC3LocalLANLink based on Integer32"""
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


_Mc2200_GEMC3LocalLANLink_Type.__name__ = "Integer32"
_Mc2200_GEMC3LocalLANLink_Object = MibTableColumn
mc2200_GEMC3LocalLANLink = _Mc2200_GEMC3LocalLANLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 3),
    _Mc2200_GEMC3LocalLANLink_Type()
)
mc2200_GEMC3LocalLANLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3LocalLANLink.setStatus("mandatory")
_Mc2200_GEMC3LocalWANSFPInfo_Type = DisplayString
_Mc2200_GEMC3LocalWANSFPInfo_Object = MibTableColumn
mc2200_GEMC3LocalWANSFPInfo = _Mc2200_GEMC3LocalWANSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 4),
    _Mc2200_GEMC3LocalWANSFPInfo_Type()
)
mc2200_GEMC3LocalWANSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3LocalWANSFPInfo.setStatus("current")


class _Mc2200_GEMC3LocalWANLink_Type(Integer32):
    """Custom type mc2200_GEMC3LocalWANLink based on Integer32"""
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


_Mc2200_GEMC3LocalWANLink_Type.__name__ = "Integer32"
_Mc2200_GEMC3LocalWANLink_Object = MibTableColumn
mc2200_GEMC3LocalWANLink = _Mc2200_GEMC3LocalWANLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 5),
    _Mc2200_GEMC3LocalWANLink_Type()
)
mc2200_GEMC3LocalWANLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3LocalWANLink.setStatus("current")


class _Mc2200_GEMC3LocalLANDownStreamBW_Type(Integer32):
    """Custom type mc2200_GEMC3LocalLANDownStreamBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              35,
              40,
              45,
              50,
              55,
              60,
              65,
              70,
              75,
              80,
              85,
              90,
              95,
              100,
              150,
              200,
              250,
              300,
              350,
              400,
              450,
              500,
              550,
              600,
              650,
              700,
              750,
              800,
              850,
              900,
              950,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate35M", 35),
          ("rate40M", 40),
          ("rate45M", 45),
          ("rate50M", 50),
          ("rate55M", 55),
          ("rate60M", 60),
          ("rate65M", 65),
          ("rate70M", 70),
          ("rate75M", 75),
          ("rate80M", 80),
          ("rate85M", 85),
          ("rate90M", 90),
          ("rate95M", 95),
          ("rate100M", 100),
          ("rate150M", 150),
          ("rate200M", 200),
          ("rate250M", 250),
          ("rate300M", 300),
          ("rate350M", 350),
          ("rate400M", 400),
          ("rate450M", 450),
          ("rate500M", 500),
          ("rate550M", 550),
          ("rate600M", 600),
          ("rate650M", 650),
          ("rate700M", 700),
          ("rate750M", 750),
          ("rate800M", 800),
          ("rate850M", 850),
          ("rate900M", 900),
          ("rate950M", 950),
          ("rate1000M", 1000))
    )


_Mc2200_GEMC3LocalLANDownStreamBW_Type.__name__ = "Integer32"
_Mc2200_GEMC3LocalLANDownStreamBW_Object = MibTableColumn
mc2200_GEMC3LocalLANDownStreamBW = _Mc2200_GEMC3LocalLANDownStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 6),
    _Mc2200_GEMC3LocalLANDownStreamBW_Type()
)
mc2200_GEMC3LocalLANDownStreamBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC3LocalLANDownStreamBW.setStatus("current")


class _Mc2200_GEMC3LocalLANUpStreamBW_Type(Integer32):
    """Custom type mc2200_GEMC3LocalLANUpStreamBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              35,
              40,
              45,
              50,
              55,
              60,
              65,
              70,
              75,
              80,
              85,
              90,
              95,
              100,
              150,
              200,
              250,
              300,
              350,
              400,
              450,
              500,
              550,
              600,
              650,
              700,
              750,
              800,
              850,
              900,
              950,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate35M", 35),
          ("rate40M", 40),
          ("rate45M", 45),
          ("rate50M", 50),
          ("rate55M", 55),
          ("rate60M", 60),
          ("rate65M", 65),
          ("rate70M", 70),
          ("rate75M", 75),
          ("rate80M", 80),
          ("rate85M", 85),
          ("rate90M", 90),
          ("rate95M", 95),
          ("rate100M", 100),
          ("rate150M", 150),
          ("rate200M", 200),
          ("rate250M", 250),
          ("rate300M", 300),
          ("rate350M", 350),
          ("rate400M", 400),
          ("rate450M", 450),
          ("rate500M", 500),
          ("rate550M", 550),
          ("rate600M", 600),
          ("rate650M", 650),
          ("rate700M", 700),
          ("rate750M", 750),
          ("rate800M", 800),
          ("rate850M", 850),
          ("rate900M", 900),
          ("rate950M", 950),
          ("rate1000M", 1000))
    )


_Mc2200_GEMC3LocalLANUpStreamBW_Type.__name__ = "Integer32"
_Mc2200_GEMC3LocalLANUpStreamBW_Object = MibTableColumn
mc2200_GEMC3LocalLANUpStreamBW = _Mc2200_GEMC3LocalLANUpStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 7),
    _Mc2200_GEMC3LocalLANUpStreamBW_Type()
)
mc2200_GEMC3LocalLANUpStreamBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC3LocalLANUpStreamBW.setStatus("current")


class _Mc2200_GEMC3LocalLANMode_Type(Integer32):
    """Custom type mc2200_GEMC3LocalLANMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("mode1000Base-X-auto", 1),
          ("mode1000Base-X-Force", 2),
          ("auto-10-100-1000T", 3),
          ("mode1000Base-T-full", 4),
          ("mode100Base-T-full", 5),
          ("mode100Base-T-Half", 6),
          ("mode10Base-T-full", 7),
          ("mode10Base-T-Half", 8))
    )


_Mc2200_GEMC3LocalLANMode_Type.__name__ = "Integer32"
_Mc2200_GEMC3LocalLANMode_Object = MibTableColumn
mc2200_GEMC3LocalLANMode = _Mc2200_GEMC3LocalLANMode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 8),
    _Mc2200_GEMC3LocalLANMode_Type()
)
mc2200_GEMC3LocalLANMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC3LocalLANMode.setStatus("current")
_Mc2200_GEMC3RxGoodOctets_Type = Counter64
_Mc2200_GEMC3RxGoodOctets_Object = MibTableColumn
mc2200_GEMC3RxGoodOctets = _Mc2200_GEMC3RxGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 9),
    _Mc2200_GEMC3RxGoodOctets_Type()
)
mc2200_GEMC3RxGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3RxGoodOctets.setStatus("current")
_Mc2200_GEMC3RxBadOctets_Type = Counter64
_Mc2200_GEMC3RxBadOctets_Object = MibTableColumn
mc2200_GEMC3RxBadOctets = _Mc2200_GEMC3RxBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 11),
    _Mc2200_GEMC3RxBadOctets_Type()
)
mc2200_GEMC3RxBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3RxBadOctets.setStatus("current")
_Mc2200_GEMC3TxFCSErr_Type = Counter64
_Mc2200_GEMC3TxFCSErr_Object = MibTableColumn
mc2200_GEMC3TxFCSErr = _Mc2200_GEMC3TxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 12),
    _Mc2200_GEMC3TxFCSErr_Type()
)
mc2200_GEMC3TxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3TxFCSErr.setStatus("current")
_Mc2200_GEMC3RxUnicast_Type = Counter64
_Mc2200_GEMC3RxUnicast_Object = MibTableColumn
mc2200_GEMC3RxUnicast = _Mc2200_GEMC3RxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 13),
    _Mc2200_GEMC3RxUnicast_Type()
)
mc2200_GEMC3RxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3RxUnicast.setStatus("current")
_Mc2200_GEMC3TxDeferred_Type = Counter64
_Mc2200_GEMC3TxDeferred_Object = MibTableColumn
mc2200_GEMC3TxDeferred = _Mc2200_GEMC3TxDeferred_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 14),
    _Mc2200_GEMC3TxDeferred_Type()
)
mc2200_GEMC3TxDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3TxDeferred.setStatus("current")
_Mc2200_GEMC3RxBroadcasts_Type = Counter64
_Mc2200_GEMC3RxBroadcasts_Object = MibTableColumn
mc2200_GEMC3RxBroadcasts = _Mc2200_GEMC3RxBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 15),
    _Mc2200_GEMC3RxBroadcasts_Type()
)
mc2200_GEMC3RxBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3RxBroadcasts.setStatus("current")
_Mc2200_GEMC3RxMulticasts_Type = Counter64
_Mc2200_GEMC3RxMulticasts_Object = MibTableColumn
mc2200_GEMC3RxMulticasts = _Mc2200_GEMC3RxMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 16),
    _Mc2200_GEMC3RxMulticasts_Type()
)
mc2200_GEMC3RxMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3RxMulticasts.setStatus("current")
_Mc2200_GEMC3Rx64Octets_Type = Counter64
_Mc2200_GEMC3Rx64Octets_Object = MibTableColumn
mc2200_GEMC3Rx64Octets = _Mc2200_GEMC3Rx64Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 17),
    _Mc2200_GEMC3Rx64Octets_Type()
)
mc2200_GEMC3Rx64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3Rx64Octets.setStatus("current")
_Mc2200_GEMC3Rx65to127Octets_Type = Counter64
_Mc2200_GEMC3Rx65to127Octets_Object = MibTableColumn
mc2200_GEMC3Rx65to127Octets = _Mc2200_GEMC3Rx65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 18),
    _Mc2200_GEMC3Rx65to127Octets_Type()
)
mc2200_GEMC3Rx65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3Rx65to127Octets.setStatus("current")
_Mc2200_GEMC3Rx128to255Octets_Type = Counter64
_Mc2200_GEMC3Rx128to255Octets_Object = MibTableColumn
mc2200_GEMC3Rx128to255Octets = _Mc2200_GEMC3Rx128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 19),
    _Mc2200_GEMC3Rx128to255Octets_Type()
)
mc2200_GEMC3Rx128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3Rx128to255Octets.setStatus("current")
_Mc2200_GEMC3Rx256to511Octets_Type = Counter64
_Mc2200_GEMC3Rx256to511Octets_Object = MibTableColumn
mc2200_GEMC3Rx256to511Octets = _Mc2200_GEMC3Rx256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 20),
    _Mc2200_GEMC3Rx256to511Octets_Type()
)
mc2200_GEMC3Rx256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3Rx256to511Octets.setStatus("current")
_Mc2200_GEMC3Rx512to1023Octets_Type = Counter64
_Mc2200_GEMC3Rx512to1023Octets_Object = MibTableColumn
mc2200_GEMC3Rx512to1023Octets = _Mc2200_GEMC3Rx512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 21),
    _Mc2200_GEMC3Rx512to1023Octets_Type()
)
mc2200_GEMC3Rx512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3Rx512to1023Octets.setStatus("current")
_Mc2200_GEMC3Rx1024toMaxOctets_Type = Counter64
_Mc2200_GEMC3Rx1024toMaxOctets_Object = MibTableColumn
mc2200_GEMC3Rx1024toMaxOctets = _Mc2200_GEMC3Rx1024toMaxOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 22),
    _Mc2200_GEMC3Rx1024toMaxOctets_Type()
)
mc2200_GEMC3Rx1024toMaxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3Rx1024toMaxOctets.setStatus("current")
_Mc2200_GEMC3TxOctets_Type = Counter64
_Mc2200_GEMC3TxOctets_Object = MibTableColumn
mc2200_GEMC3TxOctets = _Mc2200_GEMC3TxOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 23),
    _Mc2200_GEMC3TxOctets_Type()
)
mc2200_GEMC3TxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3TxOctets.setStatus("current")
_Mc2200_GEMC3TxUnicast_Type = Counter64
_Mc2200_GEMC3TxUnicast_Object = MibTableColumn
mc2200_GEMC3TxUnicast = _Mc2200_GEMC3TxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 25),
    _Mc2200_GEMC3TxUnicast_Type()
)
mc2200_GEMC3TxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3TxUnicast.setStatus("current")
_Mc2200_GEMC3TxExcessive_Type = Counter64
_Mc2200_GEMC3TxExcessive_Object = MibTableColumn
mc2200_GEMC3TxExcessive = _Mc2200_GEMC3TxExcessive_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 26),
    _Mc2200_GEMC3TxExcessive_Type()
)
mc2200_GEMC3TxExcessive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3TxExcessive.setStatus("current")
_Mc2200_GEMC3TxMulticasts_Type = Counter64
_Mc2200_GEMC3TxMulticasts_Object = MibTableColumn
mc2200_GEMC3TxMulticasts = _Mc2200_GEMC3TxMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 27),
    _Mc2200_GEMC3TxMulticasts_Type()
)
mc2200_GEMC3TxMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3TxMulticasts.setStatus("current")
_Mc2200_GEMC3TxBroadcasts_Type = Counter64
_Mc2200_GEMC3TxBroadcasts_Object = MibTableColumn
mc2200_GEMC3TxBroadcasts = _Mc2200_GEMC3TxBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 28),
    _Mc2200_GEMC3TxBroadcasts_Type()
)
mc2200_GEMC3TxBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3TxBroadcasts.setStatus("current")
_Mc2200_GEMC3TxSingle_Type = Counter64
_Mc2200_GEMC3TxSingle_Object = MibTableColumn
mc2200_GEMC3TxSingle = _Mc2200_GEMC3TxSingle_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 29),
    _Mc2200_GEMC3TxSingle_Type()
)
mc2200_GEMC3TxSingle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3TxSingle.setStatus("current")
_Mc2200_GEMC3TxPause_Type = Counter64
_Mc2200_GEMC3TxPause_Object = MibTableColumn
mc2200_GEMC3TxPause = _Mc2200_GEMC3TxPause_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 30),
    _Mc2200_GEMC3TxPause_Type()
)
mc2200_GEMC3TxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3TxPause.setStatus("current")
_Mc2200_GEMC3RxPause_Type = Counter64
_Mc2200_GEMC3RxPause_Object = MibTableColumn
mc2200_GEMC3RxPause = _Mc2200_GEMC3RxPause_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 31),
    _Mc2200_GEMC3RxPause_Type()
)
mc2200_GEMC3RxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3RxPause.setStatus("current")
_Mc2200_GEMC3TxMultiple_Type = Counter64
_Mc2200_GEMC3TxMultiple_Object = MibTableColumn
mc2200_GEMC3TxMultiple = _Mc2200_GEMC3TxMultiple_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 32),
    _Mc2200_GEMC3TxMultiple_Type()
)
mc2200_GEMC3TxMultiple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3TxMultiple.setStatus("current")
_Mc2200_GEMC3RxUndersize_Type = Counter64
_Mc2200_GEMC3RxUndersize_Object = MibTableColumn
mc2200_GEMC3RxUndersize = _Mc2200_GEMC3RxUndersize_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 33),
    _Mc2200_GEMC3RxUndersize_Type()
)
mc2200_GEMC3RxUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3RxUndersize.setStatus("current")
_Mc2200_GEMC3RxFragments_Type = Counter64
_Mc2200_GEMC3RxFragments_Object = MibTableColumn
mc2200_GEMC3RxFragments = _Mc2200_GEMC3RxFragments_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 34),
    _Mc2200_GEMC3RxFragments_Type()
)
mc2200_GEMC3RxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3RxFragments.setStatus("current")
_Mc2200_GEMC3RxOversize_Type = Counter64
_Mc2200_GEMC3RxOversize_Object = MibTableColumn
mc2200_GEMC3RxOversize = _Mc2200_GEMC3RxOversize_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 35),
    _Mc2200_GEMC3RxOversize_Type()
)
mc2200_GEMC3RxOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3RxOversize.setStatus("current")
_Mc2200_GEMC3RxJabber_Type = Counter64
_Mc2200_GEMC3RxJabber_Object = MibTableColumn
mc2200_GEMC3RxJabber = _Mc2200_GEMC3RxJabber_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 36),
    _Mc2200_GEMC3RxJabber_Type()
)
mc2200_GEMC3RxJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3RxJabber.setStatus("current")
_Mc2200_GEMC3RxErr_Type = Counter64
_Mc2200_GEMC3RxErr_Object = MibTableColumn
mc2200_GEMC3RxErr = _Mc2200_GEMC3RxErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 37),
    _Mc2200_GEMC3RxErr_Type()
)
mc2200_GEMC3RxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3RxErr.setStatus("current")
_Mc2200_GEMC3RxFCSErr_Type = Counter64
_Mc2200_GEMC3RxFCSErr_Object = MibTableColumn
mc2200_GEMC3RxFCSErr = _Mc2200_GEMC3RxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 38),
    _Mc2200_GEMC3RxFCSErr_Type()
)
mc2200_GEMC3RxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3RxFCSErr.setStatus("current")
_Mc2200_GEMC3TxCollisions_Type = Counter64
_Mc2200_GEMC3TxCollisions_Object = MibTableColumn
mc2200_GEMC3TxCollisions = _Mc2200_GEMC3TxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 39),
    _Mc2200_GEMC3TxCollisions_Type()
)
mc2200_GEMC3TxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3TxCollisions.setStatus("current")
_Mc2200_GEMC3TxLate_Type = Counter64
_Mc2200_GEMC3TxLate_Object = MibTableColumn
mc2200_GEMC3TxLate = _Mc2200_GEMC3TxLate_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 40),
    _Mc2200_GEMC3TxLate_Type()
)
mc2200_GEMC3TxLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3TxLate.setStatus("current")
_Mc2200_GEMC3RemoteLANSFPInfo_Type = DisplayString
_Mc2200_GEMC3RemoteLANSFPInfo_Object = MibTableColumn
mc2200_GEMC3RemoteLANSFPInfo = _Mc2200_GEMC3RemoteLANSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 41),
    _Mc2200_GEMC3RemoteLANSFPInfo_Type()
)
mc2200_GEMC3RemoteLANSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3RemoteLANSFPInfo.setStatus("current")


class _Mc2200_GEMC3RemoteLANLink_Type(Integer32):
    """Custom type mc2200_GEMC3RemoteLANLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_GEMC3RemoteLANLink_Type.__name__ = "Integer32"
_Mc2200_GEMC3RemoteLANLink_Object = MibTableColumn
mc2200_GEMC3RemoteLANLink = _Mc2200_GEMC3RemoteLANLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 42),
    _Mc2200_GEMC3RemoteLANLink_Type()
)
mc2200_GEMC3RemoteLANLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3RemoteLANLink.setStatus("mandatory")
_Mc2200_GEMC3RemoteWANSFPInfo_Type = DisplayString
_Mc2200_GEMC3RemoteWANSFPInfo_Object = MibTableColumn
mc2200_GEMC3RemoteWANSFPInfo = _Mc2200_GEMC3RemoteWANSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 43),
    _Mc2200_GEMC3RemoteWANSFPInfo_Type()
)
mc2200_GEMC3RemoteWANSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3RemoteWANSFPInfo.setStatus("current")


class _Mc2200_GEMC3RemoteWANLink_Type(Integer32):
    """Custom type mc2200_GEMC3RemoteWANLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_GEMC3RemoteWANLink_Type.__name__ = "Integer32"
_Mc2200_GEMC3RemoteWANLink_Object = MibTableColumn
mc2200_GEMC3RemoteWANLink = _Mc2200_GEMC3RemoteWANLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 44),
    _Mc2200_GEMC3RemoteWANLink_Type()
)
mc2200_GEMC3RemoteWANLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3RemoteWANLink.setStatus("current")


class _Mc2200_GEMC3RemoteLANMode_Type(Integer32):
    """Custom type mc2200_GEMC3RemoteLANMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("mode1000Base-X-auto", 1),
          ("mode1000Base-X-Force", 2),
          ("auto-10-100-1000T", 3),
          ("mode1000Base-T-full", 4),
          ("mode100Base-T-full", 5),
          ("mode100Base-T-Half", 6),
          ("mode10Base-T-full", 7),
          ("mode10Base-T-Half", 8))
    )


_Mc2200_GEMC3RemoteLANMode_Type.__name__ = "Integer32"
_Mc2200_GEMC3RemoteLANMode_Object = MibTableColumn
mc2200_GEMC3RemoteLANMode = _Mc2200_GEMC3RemoteLANMode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 45),
    _Mc2200_GEMC3RemoteLANMode_Type()
)
mc2200_GEMC3RemoteLANMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC3RemoteLANMode.setStatus("current")
_Mc2200_GEMC3RemoteIPAddress_Type = IpAddress
_Mc2200_GEMC3RemoteIPAddress_Object = MibTableColumn
mc2200_GEMC3RemoteIPAddress = _Mc2200_GEMC3RemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 46),
    _Mc2200_GEMC3RemoteIPAddress_Type()
)
mc2200_GEMC3RemoteIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC3RemoteIPAddress.setStatus("mandatory")
_Mc2200_GEMC3RemoteSubnetMask_Type = IpAddress
_Mc2200_GEMC3RemoteSubnetMask_Object = MibTableColumn
mc2200_GEMC3RemoteSubnetMask = _Mc2200_GEMC3RemoteSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 47),
    _Mc2200_GEMC3RemoteSubnetMask_Type()
)
mc2200_GEMC3RemoteSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC3RemoteSubnetMask.setStatus("mandatory")
_Mc2200_GEMC3RemoteGateWay_Type = IpAddress
_Mc2200_GEMC3RemoteGateWay_Object = MibTableColumn
mc2200_GEMC3RemoteGateWay = _Mc2200_GEMC3RemoteGateWay_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 48),
    _Mc2200_GEMC3RemoteGateWay_Type()
)
mc2200_GEMC3RemoteGateWay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC3RemoteGateWay.setStatus("mandatory")


class _Mc2200_GEMC3RemoteVLANEnable_Type(Integer32):
    """Custom type mc2200_GEMC3RemoteVLANEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("enable", 1),
          ("disable", 2))
    )


_Mc2200_GEMC3RemoteVLANEnable_Type.__name__ = "Integer32"
_Mc2200_GEMC3RemoteVLANEnable_Object = MibTableColumn
mc2200_GEMC3RemoteVLANEnable = _Mc2200_GEMC3RemoteVLANEnable_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 49),
    _Mc2200_GEMC3RemoteVLANEnable_Type()
)
mc2200_GEMC3RemoteVLANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC3RemoteVLANEnable.setStatus("mandatory")
_Mc2200_GEMC3RemoteVID_Type = Integer32
_Mc2200_GEMC3RemoteVID_Object = MibTableColumn
mc2200_GEMC3RemoteVID = _Mc2200_GEMC3RemoteVID_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 50),
    _Mc2200_GEMC3RemoteVID_Type()
)
mc2200_GEMC3RemoteVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC3RemoteVID.setStatus("mandatory")


class _Mc2200_GEMC3RemoteAlarm_Type(Integer32):
    """Custom type mc2200_GEMC3RemoteAlarm based on Integer32"""
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


_Mc2200_GEMC3RemoteAlarm_Type.__name__ = "Integer32"
_Mc2200_GEMC3RemoteAlarm_Object = MibTableColumn
mc2200_GEMC3RemoteAlarm = _Mc2200_GEMC3RemoteAlarm_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 51),
    _Mc2200_GEMC3RemoteAlarm_Type()
)
mc2200_GEMC3RemoteAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC3RemoteAlarm.setStatus("current")


class _Mc2200_GEMC3RFD_Type(Integer32):
    """Custom type mc2200_GEMC3RFD based on Integer32"""
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


_Mc2200_GEMC3RFD_Type.__name__ = "Integer32"
_Mc2200_GEMC3RFD_Object = MibTableColumn
mc2200_GEMC3RFD = _Mc2200_GEMC3RFD_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 52),
    _Mc2200_GEMC3RFD_Type()
)
mc2200_GEMC3RFD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC3RFD.setStatus("current")
_Mc2200_GEMC3Default_Type = Integer32
_Mc2200_GEMC3Default_Object = MibTableColumn
mc2200_GEMC3Default = _Mc2200_GEMC3Default_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 53),
    _Mc2200_GEMC3Default_Type()
)
mc2200_GEMC3Default.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3Default.setStatus("current")
_Mc2200_GEMC3Reboot_Type = Integer32
_Mc2200_GEMC3Reboot_Object = MibTableColumn
mc2200_GEMC3Reboot = _Mc2200_GEMC3Reboot_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 54),
    _Mc2200_GEMC3Reboot_Type()
)
mc2200_GEMC3Reboot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3Reboot.setStatus("current")


class _Mc2200_GEMC3LocalLANSpeed_Type(Integer32):
    """Custom type mc2200_GEMC3LocalLANSpeed based on Integer32"""
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
        *(("speed1000M", 1),
          ("speed100M", 2),
          ("speed10M", 3),
          ("down", 4))
    )


_Mc2200_GEMC3LocalLANSpeed_Type.__name__ = "Integer32"
_Mc2200_GEMC3LocalLANSpeed_Object = MibTableColumn
mc2200_GEMC3LocalLANSpeed = _Mc2200_GEMC3LocalLANSpeed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 55),
    _Mc2200_GEMC3LocalLANSpeed_Type()
)
mc2200_GEMC3LocalLANSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3LocalLANSpeed.setStatus("mandatory")


class _Mc2200_GEMC3RemoteLANSpeed_Type(Integer32):
    """Custom type mc2200_GEMC3RemoteLANSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("speed1000M", 1),
          ("speed100M", 2),
          ("speed10M", 3),
          ("down", 4))
    )


_Mc2200_GEMC3RemoteLANSpeed_Type.__name__ = "Integer32"
_Mc2200_GEMC3RemoteLANSpeed_Object = MibTableColumn
mc2200_GEMC3RemoteLANSpeed = _Mc2200_GEMC3RemoteLANSpeed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 56),
    _Mc2200_GEMC3RemoteLANSpeed_Type()
)
mc2200_GEMC3RemoteLANSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3RemoteLANSpeed.setStatus("mandatory")
_Mc2200_GEMC3Localportuser_Type = DisplayString
_Mc2200_GEMC3Localportuser_Object = MibTableColumn
mc2200_GEMC3Localportuser = _Mc2200_GEMC3Localportuser_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 57),
    _Mc2200_GEMC3Localportuser_Type()
)
mc2200_GEMC3Localportuser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC3Localportuser.setStatus("current")
_Mc2200_GEMC3Remoteportuser_Type = DisplayString
_Mc2200_GEMC3Remoteportuser_Object = MibTableColumn
mc2200_GEMC3Remoteportuser = _Mc2200_GEMC3Remoteportuser_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 58),
    _Mc2200_GEMC3Remoteportuser_Type()
)
mc2200_GEMC3Remoteportuser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC3Remoteportuser.setStatus("current")


class _Mc2200_GEMC3WANOpticalPowerCheck_Type(Integer32):
    """Custom type mc2200_GEMC3WANOpticalPowerCheck based on Integer32"""
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


_Mc2200_GEMC3WANOpticalPowerCheck_Type.__name__ = "Integer32"
_Mc2200_GEMC3WANOpticalPowerCheck_Object = MibTableColumn
mc2200_GEMC3WANOpticalPowerCheck = _Mc2200_GEMC3WANOpticalPowerCheck_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 59),
    _Mc2200_GEMC3WANOpticalPowerCheck_Type()
)
mc2200_GEMC3WANOpticalPowerCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC3WANOpticalPowerCheck.setStatus("current")


class _Mc2200_GEMC3WANThreshold_Type(Integer32):
    """Custom type mc2200_GEMC3WANThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71)
        )
    )
    namedValues = NamedValues(
        *(("db-32", 1),
          ("db-31dot5", 2),
          ("db-31", 3),
          ("db-30dot5", 4),
          ("db-30", 5),
          ("db-29dot5", 6),
          ("db-29", 7),
          ("db-28dot5", 8),
          ("db-28", 9),
          ("db-27dot5", 10),
          ("db-27", 11),
          ("db-26dot5", 12),
          ("db-26", 13),
          ("db-25dot5", 14),
          ("db-25", 15),
          ("db-24dot5", 16),
          ("db-24", 17),
          ("db-23dot5", 18),
          ("db-23", 19),
          ("db-22dot5", 20),
          ("db-22", 21),
          ("db-21dot5", 22),
          ("db-21", 23),
          ("db-20dot5", 24),
          ("db-20", 25),
          ("db-19dot5", 26),
          ("db-19", 27),
          ("db-18dot5", 28),
          ("db-18", 29),
          ("db-17dot5", 30),
          ("db-17", 31),
          ("db-16dot5", 32),
          ("db-16", 33),
          ("db-15dot5", 34),
          ("db-15", 35),
          ("db-14dot5", 36),
          ("db-14", 37),
          ("db-13dot5", 38),
          ("db-13", 39),
          ("db-12dot5", 40),
          ("db-12", 41),
          ("db-11dot5", 42),
          ("db-11", 43),
          ("db-10dot5", 44),
          ("db-10", 45),
          ("db-9dot5", 46),
          ("db-9", 47),
          ("db-8dot5", 48),
          ("db-8", 49),
          ("db-7dot5", 50),
          ("db-7", 51),
          ("db-6dot5", 52),
          ("db-6", 53),
          ("db-5dot5", 54),
          ("db-5", 55),
          ("db-4dot5", 56),
          ("db-4", 57),
          ("db-3dot5", 58),
          ("db-3", 59),
          ("db-2dot5", 60),
          ("db-2", 61),
          ("db-1dot5", 62),
          ("db-1", 63),
          ("db-0dot5", 64),
          ("db-0", 65),
          ("db0dot5", 66),
          ("db1", 67),
          ("db1dot5", 68),
          ("db2", 69),
          ("db2dot5", 70),
          ("db3", 71))
    )


_Mc2200_GEMC3WANThreshold_Type.__name__ = "Integer32"
_Mc2200_GEMC3WANThreshold_Object = MibTableColumn
mc2200_GEMC3WANThreshold = _Mc2200_GEMC3WANThreshold_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 60),
    _Mc2200_GEMC3WANThreshold_Type()
)
mc2200_GEMC3WANThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC3WANThreshold.setStatus("current")


class _Mc2200_GEMC3TrapFilterLocalLAN_Type(Integer32):
    """Custom type mc2200_GEMC3TrapFilterLocalLAN based on Integer32"""
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


_Mc2200_GEMC3TrapFilterLocalLAN_Type.__name__ = "Integer32"
_Mc2200_GEMC3TrapFilterLocalLAN_Object = MibTableColumn
mc2200_GEMC3TrapFilterLocalLAN = _Mc2200_GEMC3TrapFilterLocalLAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 61),
    _Mc2200_GEMC3TrapFilterLocalLAN_Type()
)
mc2200_GEMC3TrapFilterLocalLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC3TrapFilterLocalLAN.setStatus("current")


class _Mc2200_GEMC3TrapFilterLocalWAN_Type(Integer32):
    """Custom type mc2200_GEMC3TrapFilterLocalWAN based on Integer32"""
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


_Mc2200_GEMC3TrapFilterLocalWAN_Type.__name__ = "Integer32"
_Mc2200_GEMC3TrapFilterLocalWAN_Object = MibTableColumn
mc2200_GEMC3TrapFilterLocalWAN = _Mc2200_GEMC3TrapFilterLocalWAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 62),
    _Mc2200_GEMC3TrapFilterLocalWAN_Type()
)
mc2200_GEMC3TrapFilterLocalWAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC3TrapFilterLocalWAN.setStatus("current")


class _Mc2200_GEMC3TrapFilterRemotePower_Type(Integer32):
    """Custom type mc2200_GEMC3TrapFilterRemotePower based on Integer32"""
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


_Mc2200_GEMC3TrapFilterRemotePower_Type.__name__ = "Integer32"
_Mc2200_GEMC3TrapFilterRemotePower_Object = MibTableColumn
mc2200_GEMC3TrapFilterRemotePower = _Mc2200_GEMC3TrapFilterRemotePower_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 63),
    _Mc2200_GEMC3TrapFilterRemotePower_Type()
)
mc2200_GEMC3TrapFilterRemotePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC3TrapFilterRemotePower.setStatus("current")


class _Mc2200_GEMC3TrapFilterRemoteLAN_Type(Integer32):
    """Custom type mc2200_GEMC3TrapFilterRemoteLAN based on Integer32"""
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


_Mc2200_GEMC3TrapFilterRemoteLAN_Type.__name__ = "Integer32"
_Mc2200_GEMC3TrapFilterRemoteLAN_Object = MibTableColumn
mc2200_GEMC3TrapFilterRemoteLAN = _Mc2200_GEMC3TrapFilterRemoteLAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 64),
    _Mc2200_GEMC3TrapFilterRemoteLAN_Type()
)
mc2200_GEMC3TrapFilterRemoteLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC3TrapFilterRemoteLAN.setStatus("current")


class _Mc2200_GEMC3TrapFilterRemoteWAN_Type(Integer32):
    """Custom type mc2200_GEMC3TrapFilterRemoteWAN based on Integer32"""
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


_Mc2200_GEMC3TrapFilterRemoteWAN_Type.__name__ = "Integer32"
_Mc2200_GEMC3TrapFilterRemoteWAN_Object = MibTableColumn
mc2200_GEMC3TrapFilterRemoteWAN = _Mc2200_GEMC3TrapFilterRemoteWAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 65),
    _Mc2200_GEMC3TrapFilterRemoteWAN_Type()
)
mc2200_GEMC3TrapFilterRemoteWAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC3TrapFilterRemoteWAN.setStatus("current")


class _Mc2200_GEMC3Loopback_Type(Integer32):
    """Custom type mc2200_GEMC3Loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("local_lanouter", 2),
          ("local_laninner", 3),
          ("local_wanouter", 4),
          ("local_waninner", 5),
          ("remote_lanouter", 6),
          ("remote_laninner", 7))
    )


_Mc2200_GEMC3Loopback_Type.__name__ = "Integer32"
_Mc2200_GEMC3Loopback_Object = MibTableColumn
mc2200_GEMC3Loopback = _Mc2200_GEMC3Loopback_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 66),
    _Mc2200_GEMC3Loopback_Type()
)
mc2200_GEMC3Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMC3Loopback.setStatus("mandatory")
_Mc2200_GEMC3CardType_Type = DisplayString
_Mc2200_GEMC3CardType_Object = MibTableColumn
mc2200_GEMC3CardType = _Mc2200_GEMC3CardType_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 13, 1, 67),
    _Mc2200_GEMC3CardType_Type()
)
mc2200_GEMC3CardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMC3CardType.setStatus("current")
_Mc2200_GESFPAPSTable_Object = MibTable
mc2200_GESFPAPSTable = _Mc2200_GESFPAPSTable_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14)
)
if mibBuilder.loadTexts:
    mc2200_GESFPAPSTable.setStatus("current")
_Mc2200_GESFPAPSEntry_Object = MibTableRow
mc2200_GESFPAPSEntry = _Mc2200_GESFPAPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1)
)
mc2200_GESFPAPSEntry.setIndexNames(
    (0, "OnAccess2200-MIB", "mc2200-GESFPAPSCardIndex"),
)
if mibBuilder.loadTexts:
    mc2200_GESFPAPSEntry.setStatus("current")


class _Mc2200_GESFPAPSCardIndex_Type(Integer32):
    """Custom type mc2200_GESFPAPSCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("card01", 1),
          ("card02", 2),
          ("card03", 3),
          ("card04", 4),
          ("card05", 5),
          ("card06", 6),
          ("card07", 7),
          ("card08", 8),
          ("card09", 9),
          ("card10", 10),
          ("card11", 11),
          ("card12", 12),
          ("card13", 13),
          ("card14", 14),
          ("card15", 15))
    )


_Mc2200_GESFPAPSCardIndex_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSCardIndex_Object = MibTableColumn
mc2200_GESFPAPSCardIndex = _Mc2200_GESFPAPSCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 1),
    _Mc2200_GESFPAPSCardIndex_Type()
)
mc2200_GESFPAPSCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSCardIndex.setStatus("current")


class _Mc2200_GESFPAPSLocalTXLink_Type(Integer32):
    """Custom type mc2200_GESFPAPSLocalTXLink based on Integer32"""
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


_Mc2200_GESFPAPSLocalTXLink_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSLocalTXLink_Object = MibTableColumn
mc2200_GESFPAPSLocalTXLink = _Mc2200_GESFPAPSLocalTXLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 2),
    _Mc2200_GESFPAPSLocalTXLink_Type()
)
mc2200_GESFPAPSLocalTXLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSLocalTXLink.setStatus("mandatory")
_Mc2200_GESFPAPSLocalWAN1SFPInfo_Type = DisplayString
_Mc2200_GESFPAPSLocalWAN1SFPInfo_Object = MibTableColumn
mc2200_GESFPAPSLocalWAN1SFPInfo = _Mc2200_GESFPAPSLocalWAN1SFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 3),
    _Mc2200_GESFPAPSLocalWAN1SFPInfo_Type()
)
mc2200_GESFPAPSLocalWAN1SFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSLocalWAN1SFPInfo.setStatus("current")


class _Mc2200_GESFPAPSLocalWAN1Link_Type(Integer32):
    """Custom type mc2200_GESFPAPSLocalWAN1Link based on Integer32"""
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
          ("active", 3),
          ("standby", 4))
    )


_Mc2200_GESFPAPSLocalWAN1Link_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSLocalWAN1Link_Object = MibTableColumn
mc2200_GESFPAPSLocalWAN1Link = _Mc2200_GESFPAPSLocalWAN1Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 4),
    _Mc2200_GESFPAPSLocalWAN1Link_Type()
)
mc2200_GESFPAPSLocalWAN1Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSLocalWAN1Link.setStatus("current")
_Mc2200_GESFPAPSLocalWAN2SFPInfo_Type = DisplayString
_Mc2200_GESFPAPSLocalWAN2SFPInfo_Object = MibTableColumn
mc2200_GESFPAPSLocalWAN2SFPInfo = _Mc2200_GESFPAPSLocalWAN2SFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 5),
    _Mc2200_GESFPAPSLocalWAN2SFPInfo_Type()
)
mc2200_GESFPAPSLocalWAN2SFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSLocalWAN2SFPInfo.setStatus("current")


class _Mc2200_GESFPAPSLocalWAN2Link_Type(Integer32):
    """Custom type mc2200_GESFPAPSLocalWAN2Link based on Integer32"""
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
          ("active", 3),
          ("standby", 4))
    )


_Mc2200_GESFPAPSLocalWAN2Link_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSLocalWAN2Link_Object = MibTableColumn
mc2200_GESFPAPSLocalWAN2Link = _Mc2200_GESFPAPSLocalWAN2Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 6),
    _Mc2200_GESFPAPSLocalWAN2Link_Type()
)
mc2200_GESFPAPSLocalWAN2Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSLocalWAN2Link.setStatus("current")


class _Mc2200_GESFPAPSLocalActivePort_Type(Integer32):
    """Custom type mc2200_GESFPAPSLocalActivePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wan1", 1),
          ("wan2", 2))
    )


_Mc2200_GESFPAPSLocalActivePort_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSLocalActivePort_Object = MibTableColumn
mc2200_GESFPAPSLocalActivePort = _Mc2200_GESFPAPSLocalActivePort_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 7),
    _Mc2200_GESFPAPSLocalActivePort_Type()
)
mc2200_GESFPAPSLocalActivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSLocalActivePort.setStatus("current")


class _Mc2200_GESFPAPSLocalTXDownStreamBW_Type(Integer32):
    """Custom type mc2200_GESFPAPSLocalTXDownStreamBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              35,
              40,
              45,
              50,
              55,
              60,
              65,
              70,
              75,
              80,
              85,
              90,
              95,
              100,
              150,
              200,
              250,
              300,
              350,
              400,
              450,
              500,
              550,
              600,
              650,
              700,
              750,
              800,
              850,
              900,
              950,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate35M", 35),
          ("rate40M", 40),
          ("rate45M", 45),
          ("rate50M", 50),
          ("rate55M", 55),
          ("rate60M", 60),
          ("rate65M", 65),
          ("rate70M", 70),
          ("rate75M", 75),
          ("rate80M", 80),
          ("rate85M", 85),
          ("rate90M", 90),
          ("rate95M", 95),
          ("rate100M", 100),
          ("rate150M", 150),
          ("rate200M", 200),
          ("rate250M", 250),
          ("rate300M", 300),
          ("rate350M", 350),
          ("rate400M", 400),
          ("rate450M", 450),
          ("rate500M", 500),
          ("rate550M", 550),
          ("rate600M", 600),
          ("rate650M", 650),
          ("rate700M", 700),
          ("rate750M", 750),
          ("rate800M", 800),
          ("rate850M", 850),
          ("rate900M", 900),
          ("rate950M", 950),
          ("rate1000M", 1000))
    )


_Mc2200_GESFPAPSLocalTXDownStreamBW_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSLocalTXDownStreamBW_Object = MibTableColumn
mc2200_GESFPAPSLocalTXDownStreamBW = _Mc2200_GESFPAPSLocalTXDownStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 8),
    _Mc2200_GESFPAPSLocalTXDownStreamBW_Type()
)
mc2200_GESFPAPSLocalTXDownStreamBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSLocalTXDownStreamBW.setStatus("current")


class _Mc2200_GESFPAPSLocalTXUpStreamBW_Type(Integer32):
    """Custom type mc2200_GESFPAPSLocalTXUpStreamBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              35,
              40,
              45,
              50,
              55,
              60,
              65,
              70,
              75,
              80,
              85,
              90,
              95,
              100,
              150,
              200,
              250,
              300,
              350,
              400,
              450,
              500,
              550,
              600,
              650,
              700,
              750,
              800,
              850,
              900,
              950,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate35M", 35),
          ("rate40M", 40),
          ("rate45M", 45),
          ("rate50M", 50),
          ("rate55M", 55),
          ("rate60M", 60),
          ("rate65M", 65),
          ("rate70M", 70),
          ("rate75M", 75),
          ("rate80M", 80),
          ("rate85M", 85),
          ("rate90M", 90),
          ("rate95M", 95),
          ("rate100M", 100),
          ("rate150M", 150),
          ("rate200M", 200),
          ("rate250M", 250),
          ("rate300M", 300),
          ("rate350M", 350),
          ("rate400M", 400),
          ("rate450M", 450),
          ("rate500M", 500),
          ("rate550M", 550),
          ("rate600M", 600),
          ("rate650M", 650),
          ("rate700M", 700),
          ("rate750M", 750),
          ("rate800M", 800),
          ("rate850M", 850),
          ("rate900M", 900),
          ("rate950M", 950),
          ("rate1000M", 1000))
    )


_Mc2200_GESFPAPSLocalTXUpStreamBW_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSLocalTXUpStreamBW_Object = MibTableColumn
mc2200_GESFPAPSLocalTXUpStreamBW = _Mc2200_GESFPAPSLocalTXUpStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 9),
    _Mc2200_GESFPAPSLocalTXUpStreamBW_Type()
)
mc2200_GESFPAPSLocalTXUpStreamBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSLocalTXUpStreamBW.setStatus("current")


class _Mc2200_GESFPAPSLocalTXMode_Type(Integer32):
    """Custom type mc2200_GESFPAPSLocalTXMode based on Integer32"""
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
        *(("auto-10-100-1000", 1),
          ("mode1000F", 2),
          ("mode100F", 3),
          ("mode10F", 4),
          ("mode100H", 5),
          ("mode10H", 6))
    )


_Mc2200_GESFPAPSLocalTXMode_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSLocalTXMode_Object = MibTableColumn
mc2200_GESFPAPSLocalTXMode = _Mc2200_GESFPAPSLocalTXMode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 10),
    _Mc2200_GESFPAPSLocalTXMode_Type()
)
mc2200_GESFPAPSLocalTXMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSLocalTXMode.setStatus("current")


class _Mc2200_GESFPAPSLocalTXMDIX_Type(Integer32):
    """Custom type mc2200_GESFPAPSLocalTXMDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("mdi", 2),
          ("mdiX", 3))
    )


_Mc2200_GESFPAPSLocalTXMDIX_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSLocalTXMDIX_Object = MibTableColumn
mc2200_GESFPAPSLocalTXMDIX = _Mc2200_GESFPAPSLocalTXMDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 11),
    _Mc2200_GESFPAPSLocalTXMDIX_Type()
)
mc2200_GESFPAPSLocalTXMDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSLocalTXMDIX.setStatus("current")
_Mc2200_GESFPAPSRxGoodOctets_Type = Counter64
_Mc2200_GESFPAPSRxGoodOctets_Object = MibTableColumn
mc2200_GESFPAPSRxGoodOctets = _Mc2200_GESFPAPSRxGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 12),
    _Mc2200_GESFPAPSRxGoodOctets_Type()
)
mc2200_GESFPAPSRxGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRxGoodOctets.setStatus("current")
_Mc2200_GESFPAPSRxBadOctets_Type = Counter64
_Mc2200_GESFPAPSRxBadOctets_Object = MibTableColumn
mc2200_GESFPAPSRxBadOctets = _Mc2200_GESFPAPSRxBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 14),
    _Mc2200_GESFPAPSRxBadOctets_Type()
)
mc2200_GESFPAPSRxBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRxBadOctets.setStatus("current")
_Mc2200_GESFPAPSTxFCSErr_Type = Counter64
_Mc2200_GESFPAPSTxFCSErr_Object = MibTableColumn
mc2200_GESFPAPSTxFCSErr = _Mc2200_GESFPAPSTxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 15),
    _Mc2200_GESFPAPSTxFCSErr_Type()
)
mc2200_GESFPAPSTxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSTxFCSErr.setStatus("current")
_Mc2200_GESFPAPSRxUnicast_Type = Counter64
_Mc2200_GESFPAPSRxUnicast_Object = MibTableColumn
mc2200_GESFPAPSRxUnicast = _Mc2200_GESFPAPSRxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 16),
    _Mc2200_GESFPAPSRxUnicast_Type()
)
mc2200_GESFPAPSRxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRxUnicast.setStatus("current")
_Mc2200_GESFPAPSTxDeferred_Type = Counter64
_Mc2200_GESFPAPSTxDeferred_Object = MibTableColumn
mc2200_GESFPAPSTxDeferred = _Mc2200_GESFPAPSTxDeferred_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 17),
    _Mc2200_GESFPAPSTxDeferred_Type()
)
mc2200_GESFPAPSTxDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSTxDeferred.setStatus("current")
_Mc2200_GESFPAPSRxBroadcasts_Type = Counter64
_Mc2200_GESFPAPSRxBroadcasts_Object = MibTableColumn
mc2200_GESFPAPSRxBroadcasts = _Mc2200_GESFPAPSRxBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 18),
    _Mc2200_GESFPAPSRxBroadcasts_Type()
)
mc2200_GESFPAPSRxBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRxBroadcasts.setStatus("current")
_Mc2200_GESFPAPSRxMulticasts_Type = Counter64
_Mc2200_GESFPAPSRxMulticasts_Object = MibTableColumn
mc2200_GESFPAPSRxMulticasts = _Mc2200_GESFPAPSRxMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 19),
    _Mc2200_GESFPAPSRxMulticasts_Type()
)
mc2200_GESFPAPSRxMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRxMulticasts.setStatus("current")
_Mc2200_GESFPAPSRx64Octets_Type = Counter64
_Mc2200_GESFPAPSRx64Octets_Object = MibTableColumn
mc2200_GESFPAPSRx64Octets = _Mc2200_GESFPAPSRx64Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 20),
    _Mc2200_GESFPAPSRx64Octets_Type()
)
mc2200_GESFPAPSRx64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRx64Octets.setStatus("current")
_Mc2200_GESFPAPSRx65to127Octets_Type = Counter64
_Mc2200_GESFPAPSRx65to127Octets_Object = MibTableColumn
mc2200_GESFPAPSRx65to127Octets = _Mc2200_GESFPAPSRx65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 21),
    _Mc2200_GESFPAPSRx65to127Octets_Type()
)
mc2200_GESFPAPSRx65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRx65to127Octets.setStatus("current")
_Mc2200_GESFPAPSRx128to255Octets_Type = Counter64
_Mc2200_GESFPAPSRx128to255Octets_Object = MibTableColumn
mc2200_GESFPAPSRx128to255Octets = _Mc2200_GESFPAPSRx128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 22),
    _Mc2200_GESFPAPSRx128to255Octets_Type()
)
mc2200_GESFPAPSRx128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRx128to255Octets.setStatus("current")
_Mc2200_GESFPAPSRx256to511Octets_Type = Counter64
_Mc2200_GESFPAPSRx256to511Octets_Object = MibTableColumn
mc2200_GESFPAPSRx256to511Octets = _Mc2200_GESFPAPSRx256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 23),
    _Mc2200_GESFPAPSRx256to511Octets_Type()
)
mc2200_GESFPAPSRx256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRx256to511Octets.setStatus("current")
_Mc2200_GESFPAPSRx512to1023Octets_Type = Counter64
_Mc2200_GESFPAPSRx512to1023Octets_Object = MibTableColumn
mc2200_GESFPAPSRx512to1023Octets = _Mc2200_GESFPAPSRx512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 24),
    _Mc2200_GESFPAPSRx512to1023Octets_Type()
)
mc2200_GESFPAPSRx512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRx512to1023Octets.setStatus("current")
_Mc2200_GESFPAPSRx1024toMaxOctets_Type = Counter64
_Mc2200_GESFPAPSRx1024toMaxOctets_Object = MibTableColumn
mc2200_GESFPAPSRx1024toMaxOctets = _Mc2200_GESFPAPSRx1024toMaxOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 25),
    _Mc2200_GESFPAPSRx1024toMaxOctets_Type()
)
mc2200_GESFPAPSRx1024toMaxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRx1024toMaxOctets.setStatus("current")
_Mc2200_GESFPAPSTxOctets_Type = Counter64
_Mc2200_GESFPAPSTxOctets_Object = MibTableColumn
mc2200_GESFPAPSTxOctets = _Mc2200_GESFPAPSTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 26),
    _Mc2200_GESFPAPSTxOctets_Type()
)
mc2200_GESFPAPSTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSTxOctets.setStatus("current")
_Mc2200_GESFPAPSTxUnicast_Type = Counter64
_Mc2200_GESFPAPSTxUnicast_Object = MibTableColumn
mc2200_GESFPAPSTxUnicast = _Mc2200_GESFPAPSTxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 28),
    _Mc2200_GESFPAPSTxUnicast_Type()
)
mc2200_GESFPAPSTxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSTxUnicast.setStatus("current")
_Mc2200_GESFPAPSTxExcessive_Type = Counter64
_Mc2200_GESFPAPSTxExcessive_Object = MibTableColumn
mc2200_GESFPAPSTxExcessive = _Mc2200_GESFPAPSTxExcessive_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 29),
    _Mc2200_GESFPAPSTxExcessive_Type()
)
mc2200_GESFPAPSTxExcessive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSTxExcessive.setStatus("current")
_Mc2200_GESFPAPSTxMulticasts_Type = Counter64
_Mc2200_GESFPAPSTxMulticasts_Object = MibTableColumn
mc2200_GESFPAPSTxMulticasts = _Mc2200_GESFPAPSTxMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 30),
    _Mc2200_GESFPAPSTxMulticasts_Type()
)
mc2200_GESFPAPSTxMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSTxMulticasts.setStatus("current")
_Mc2200_GESFPAPSTxBroadcasts_Type = Counter64
_Mc2200_GESFPAPSTxBroadcasts_Object = MibTableColumn
mc2200_GESFPAPSTxBroadcasts = _Mc2200_GESFPAPSTxBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 31),
    _Mc2200_GESFPAPSTxBroadcasts_Type()
)
mc2200_GESFPAPSTxBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSTxBroadcasts.setStatus("current")
_Mc2200_GESFPAPSTxSingle_Type = Counter64
_Mc2200_GESFPAPSTxSingle_Object = MibTableColumn
mc2200_GESFPAPSTxSingle = _Mc2200_GESFPAPSTxSingle_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 32),
    _Mc2200_GESFPAPSTxSingle_Type()
)
mc2200_GESFPAPSTxSingle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSTxSingle.setStatus("current")
_Mc2200_GESFPAPSTxPause_Type = Counter64
_Mc2200_GESFPAPSTxPause_Object = MibTableColumn
mc2200_GESFPAPSTxPause = _Mc2200_GESFPAPSTxPause_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 33),
    _Mc2200_GESFPAPSTxPause_Type()
)
mc2200_GESFPAPSTxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSTxPause.setStatus("current")
_Mc2200_GESFPAPSRxPause_Type = Counter64
_Mc2200_GESFPAPSRxPause_Object = MibTableColumn
mc2200_GESFPAPSRxPause = _Mc2200_GESFPAPSRxPause_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 34),
    _Mc2200_GESFPAPSRxPause_Type()
)
mc2200_GESFPAPSRxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRxPause.setStatus("current")
_Mc2200_GESFPAPSTxMultiple_Type = Counter64
_Mc2200_GESFPAPSTxMultiple_Object = MibTableColumn
mc2200_GESFPAPSTxMultiple = _Mc2200_GESFPAPSTxMultiple_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 35),
    _Mc2200_GESFPAPSTxMultiple_Type()
)
mc2200_GESFPAPSTxMultiple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSTxMultiple.setStatus("current")
_Mc2200_GESFPAPSRxUndersize_Type = Counter64
_Mc2200_GESFPAPSRxUndersize_Object = MibTableColumn
mc2200_GESFPAPSRxUndersize = _Mc2200_GESFPAPSRxUndersize_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 36),
    _Mc2200_GESFPAPSRxUndersize_Type()
)
mc2200_GESFPAPSRxUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRxUndersize.setStatus("current")
_Mc2200_GESFPAPSRxFragments_Type = Counter64
_Mc2200_GESFPAPSRxFragments_Object = MibTableColumn
mc2200_GESFPAPSRxFragments = _Mc2200_GESFPAPSRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 37),
    _Mc2200_GESFPAPSRxFragments_Type()
)
mc2200_GESFPAPSRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRxFragments.setStatus("current")
_Mc2200_GESFPAPSRxOversize_Type = Counter64
_Mc2200_GESFPAPSRxOversize_Object = MibTableColumn
mc2200_GESFPAPSRxOversize = _Mc2200_GESFPAPSRxOversize_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 38),
    _Mc2200_GESFPAPSRxOversize_Type()
)
mc2200_GESFPAPSRxOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRxOversize.setStatus("current")
_Mc2200_GESFPAPSRxJabber_Type = Counter64
_Mc2200_GESFPAPSRxJabber_Object = MibTableColumn
mc2200_GESFPAPSRxJabber = _Mc2200_GESFPAPSRxJabber_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 39),
    _Mc2200_GESFPAPSRxJabber_Type()
)
mc2200_GESFPAPSRxJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRxJabber.setStatus("current")
_Mc2200_GESFPAPSRxErr_Type = Counter64
_Mc2200_GESFPAPSRxErr_Object = MibTableColumn
mc2200_GESFPAPSRxErr = _Mc2200_GESFPAPSRxErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 40),
    _Mc2200_GESFPAPSRxErr_Type()
)
mc2200_GESFPAPSRxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRxErr.setStatus("current")
_Mc2200_GESFPAPSRxFCSErr_Type = Counter64
_Mc2200_GESFPAPSRxFCSErr_Object = MibTableColumn
mc2200_GESFPAPSRxFCSErr = _Mc2200_GESFPAPSRxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 41),
    _Mc2200_GESFPAPSRxFCSErr_Type()
)
mc2200_GESFPAPSRxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRxFCSErr.setStatus("current")
_Mc2200_GESFPAPSTxCollisions_Type = Counter64
_Mc2200_GESFPAPSTxCollisions_Object = MibTableColumn
mc2200_GESFPAPSTxCollisions = _Mc2200_GESFPAPSTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 42),
    _Mc2200_GESFPAPSTxCollisions_Type()
)
mc2200_GESFPAPSTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSTxCollisions.setStatus("current")
_Mc2200_GESFPAPSTxLate_Type = Counter64
_Mc2200_GESFPAPSTxLate_Object = MibTableColumn
mc2200_GESFPAPSTxLate = _Mc2200_GESFPAPSTxLate_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 43),
    _Mc2200_GESFPAPSTxLate_Type()
)
mc2200_GESFPAPSTxLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSTxLate.setStatus("current")


class _Mc2200_GESFPAPSRemoteTXLink_Type(Integer32):
    """Custom type mc2200_GESFPAPSRemoteTXLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_GESFPAPSRemoteTXLink_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSRemoteTXLink_Object = MibTableColumn
mc2200_GESFPAPSRemoteTXLink = _Mc2200_GESFPAPSRemoteTXLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 44),
    _Mc2200_GESFPAPSRemoteTXLink_Type()
)
mc2200_GESFPAPSRemoteTXLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRemoteTXLink.setStatus("mandatory")
_Mc2200_GESFPAPSRemoteWAN1SFPInfo_Type = DisplayString
_Mc2200_GESFPAPSRemoteWAN1SFPInfo_Object = MibTableColumn
mc2200_GESFPAPSRemoteWAN1SFPInfo = _Mc2200_GESFPAPSRemoteWAN1SFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 45),
    _Mc2200_GESFPAPSRemoteWAN1SFPInfo_Type()
)
mc2200_GESFPAPSRemoteWAN1SFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRemoteWAN1SFPInfo.setStatus("current")


class _Mc2200_GESFPAPSRemoteWAN1Link_Type(Integer32):
    """Custom type mc2200_GESFPAPSRemoteWAN1Link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2),
          ("active", 3),
          ("standby", 4))
    )


_Mc2200_GESFPAPSRemoteWAN1Link_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSRemoteWAN1Link_Object = MibTableColumn
mc2200_GESFPAPSRemoteWAN1Link = _Mc2200_GESFPAPSRemoteWAN1Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 46),
    _Mc2200_GESFPAPSRemoteWAN1Link_Type()
)
mc2200_GESFPAPSRemoteWAN1Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRemoteWAN1Link.setStatus("current")
_Mc2200_GESFPAPSRemoteWAN2SFPInfo_Type = DisplayString
_Mc2200_GESFPAPSRemoteWAN2SFPInfo_Object = MibTableColumn
mc2200_GESFPAPSRemoteWAN2SFPInfo = _Mc2200_GESFPAPSRemoteWAN2SFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 47),
    _Mc2200_GESFPAPSRemoteWAN2SFPInfo_Type()
)
mc2200_GESFPAPSRemoteWAN2SFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRemoteWAN2SFPInfo.setStatus("current")


class _Mc2200_GESFPAPSRemoteWAN2Link_Type(Integer32):
    """Custom type mc2200_GESFPAPSRemoteWAN2Link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2),
          ("active", 3),
          ("standby", 4))
    )


_Mc2200_GESFPAPSRemoteWAN2Link_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSRemoteWAN2Link_Object = MibTableColumn
mc2200_GESFPAPSRemoteWAN2Link = _Mc2200_GESFPAPSRemoteWAN2Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 48),
    _Mc2200_GESFPAPSRemoteWAN2Link_Type()
)
mc2200_GESFPAPSRemoteWAN2Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRemoteWAN2Link.setStatus("current")


class _Mc2200_GESFPAPSRemoteTXMode_Type(Integer32):
    """Custom type mc2200_GESFPAPSRemoteTXMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto-10-100-1000", 1),
          ("mode1000F", 2),
          ("mode100F", 3),
          ("mode10F", 4),
          ("mode100H", 5),
          ("mode10H", 6))
    )


_Mc2200_GESFPAPSRemoteTXMode_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSRemoteTXMode_Object = MibTableColumn
mc2200_GESFPAPSRemoteTXMode = _Mc2200_GESFPAPSRemoteTXMode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 49),
    _Mc2200_GESFPAPSRemoteTXMode_Type()
)
mc2200_GESFPAPSRemoteTXMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRemoteTXMode.setStatus("current")


class _Mc2200_GESFPAPSRemoteTXMDIX_Type(Integer32):
    """Custom type mc2200_GESFPAPSRemoteTXMDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mdi", 2),
          ("mdix", 3))
    )


_Mc2200_GESFPAPSRemoteTXMDIX_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSRemoteTXMDIX_Object = MibTableColumn
mc2200_GESFPAPSRemoteTXMDIX = _Mc2200_GESFPAPSRemoteTXMDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 50),
    _Mc2200_GESFPAPSRemoteTXMDIX_Type()
)
mc2200_GESFPAPSRemoteTXMDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRemoteTXMDIX.setStatus("current")
_Mc2200_GESFPAPSRemoteIPAddress_Type = IpAddress
_Mc2200_GESFPAPSRemoteIPAddress_Object = MibTableColumn
mc2200_GESFPAPSRemoteIPAddress = _Mc2200_GESFPAPSRemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 51),
    _Mc2200_GESFPAPSRemoteIPAddress_Type()
)
mc2200_GESFPAPSRemoteIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRemoteIPAddress.setStatus("mandatory")
_Mc2200_GESFPAPSRemoteSubnetMask_Type = IpAddress
_Mc2200_GESFPAPSRemoteSubnetMask_Object = MibTableColumn
mc2200_GESFPAPSRemoteSubnetMask = _Mc2200_GESFPAPSRemoteSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 52),
    _Mc2200_GESFPAPSRemoteSubnetMask_Type()
)
mc2200_GESFPAPSRemoteSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRemoteSubnetMask.setStatus("mandatory")
_Mc2200_GESFPAPSRemoteGateWay_Type = IpAddress
_Mc2200_GESFPAPSRemoteGateWay_Object = MibTableColumn
mc2200_GESFPAPSRemoteGateWay = _Mc2200_GESFPAPSRemoteGateWay_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 53),
    _Mc2200_GESFPAPSRemoteGateWay_Type()
)
mc2200_GESFPAPSRemoteGateWay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRemoteGateWay.setStatus("mandatory")


class _Mc2200_GESFPAPSRemoteVLANEnable_Type(Integer32):
    """Custom type mc2200_GESFPAPSRemoteVLANEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("enable", 1),
          ("disable", 2))
    )


_Mc2200_GESFPAPSRemoteVLANEnable_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSRemoteVLANEnable_Object = MibTableColumn
mc2200_GESFPAPSRemoteVLANEnable = _Mc2200_GESFPAPSRemoteVLANEnable_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 54),
    _Mc2200_GESFPAPSRemoteVLANEnable_Type()
)
mc2200_GESFPAPSRemoteVLANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRemoteVLANEnable.setStatus("mandatory")
_Mc2200_GESFPAPSRemoteVID_Type = Integer32
_Mc2200_GESFPAPSRemoteVID_Object = MibTableColumn
mc2200_GESFPAPSRemoteVID = _Mc2200_GESFPAPSRemoteVID_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 55),
    _Mc2200_GESFPAPSRemoteVID_Type()
)
mc2200_GESFPAPSRemoteVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRemoteVID.setStatus("mandatory")


class _Mc2200_GESFPAPSRemoteAlarm_Type(Integer32):
    """Custom type mc2200_GESFPAPSRemoteAlarm based on Integer32"""
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


_Mc2200_GESFPAPSRemoteAlarm_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSRemoteAlarm_Object = MibTableColumn
mc2200_GESFPAPSRemoteAlarm = _Mc2200_GESFPAPSRemoteAlarm_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 56),
    _Mc2200_GESFPAPSRemoteAlarm_Type()
)
mc2200_GESFPAPSRemoteAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRemoteAlarm.setStatus("current")


class _Mc2200_GESFPAPSRFD_Type(Integer32):
    """Custom type mc2200_GESFPAPSRFD based on Integer32"""
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


_Mc2200_GESFPAPSRFD_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSRFD_Object = MibTableColumn
mc2200_GESFPAPSRFD = _Mc2200_GESFPAPSRFD_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 57),
    _Mc2200_GESFPAPSRFD_Type()
)
mc2200_GESFPAPSRFD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRFD.setStatus("current")
_Mc2200_GESFPAPSDefault_Type = Integer32
_Mc2200_GESFPAPSDefault_Object = MibTableColumn
mc2200_GESFPAPSDefault = _Mc2200_GESFPAPSDefault_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 58),
    _Mc2200_GESFPAPSDefault_Type()
)
mc2200_GESFPAPSDefault.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSDefault.setStatus("current")
_Mc2200_GESFPAPSReboot_Type = Integer32
_Mc2200_GESFPAPSReboot_Object = MibTableColumn
mc2200_GESFPAPSReboot = _Mc2200_GESFPAPSReboot_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 59),
    _Mc2200_GESFPAPSReboot_Type()
)
mc2200_GESFPAPSReboot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSReboot.setStatus("current")


class _Mc2200_GESFPAPSLocalTXSpeed_Type(Integer32):
    """Custom type mc2200_GESFPAPSLocalTXSpeed based on Integer32"""
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
        *(("speed1000M", 1),
          ("speed100M", 2),
          ("speed10M", 3),
          ("down", 4))
    )


_Mc2200_GESFPAPSLocalTXSpeed_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSLocalTXSpeed_Object = MibTableColumn
mc2200_GESFPAPSLocalTXSpeed = _Mc2200_GESFPAPSLocalTXSpeed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 60),
    _Mc2200_GESFPAPSLocalTXSpeed_Type()
)
mc2200_GESFPAPSLocalTXSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSLocalTXSpeed.setStatus("mandatory")


class _Mc2200_GESFPAPSRemoteTXSpeed_Type(Integer32):
    """Custom type mc2200_GESFPAPSRemoteTXSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("speed1000M", 1),
          ("speed100M", 2),
          ("speed10M", 3),
          ("down", 4))
    )


_Mc2200_GESFPAPSRemoteTXSpeed_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSRemoteTXSpeed_Object = MibTableColumn
mc2200_GESFPAPSRemoteTXSpeed = _Mc2200_GESFPAPSRemoteTXSpeed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 61),
    _Mc2200_GESFPAPSRemoteTXSpeed_Type()
)
mc2200_GESFPAPSRemoteTXSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRemoteTXSpeed.setStatus("mandatory")
_Mc2200_GESFPAPSLocalportuser_Type = DisplayString
_Mc2200_GESFPAPSLocalportuser_Object = MibTableColumn
mc2200_GESFPAPSLocalportuser = _Mc2200_GESFPAPSLocalportuser_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 62),
    _Mc2200_GESFPAPSLocalportuser_Type()
)
mc2200_GESFPAPSLocalportuser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSLocalportuser.setStatus("current")
_Mc2200_GESFPAPSRemoteportuser_Type = DisplayString
_Mc2200_GESFPAPSRemoteportuser_Object = MibTableColumn
mc2200_GESFPAPSRemoteportuser = _Mc2200_GESFPAPSRemoteportuser_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 63),
    _Mc2200_GESFPAPSRemoteportuser_Type()
)
mc2200_GESFPAPSRemoteportuser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRemoteportuser.setStatus("current")


class _Mc2200_GESFPAPSLocalTXDuplex_Type(Integer32):
    """Custom type mc2200_GESFPAPSLocalTXDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2),
          ("down", 3))
    )


_Mc2200_GESFPAPSLocalTXDuplex_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSLocalTXDuplex_Object = MibTableColumn
mc2200_GESFPAPSLocalTXDuplex = _Mc2200_GESFPAPSLocalTXDuplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 64),
    _Mc2200_GESFPAPSLocalTXDuplex_Type()
)
mc2200_GESFPAPSLocalTXDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSLocalTXDuplex.setStatus("mandatory")


class _Mc2200_GESFPAPSRemoteTXDuplex_Type(Integer32):
    """Custom type mc2200_GESFPAPSRemoteTXDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("fullDuplex", 1),
          ("halfDuplex", 2),
          ("down", 3))
    )


_Mc2200_GESFPAPSRemoteTXDuplex_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSRemoteTXDuplex_Object = MibTableColumn
mc2200_GESFPAPSRemoteTXDuplex = _Mc2200_GESFPAPSRemoteTXDuplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 65),
    _Mc2200_GESFPAPSRemoteTXDuplex_Type()
)
mc2200_GESFPAPSRemoteTXDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRemoteTXDuplex.setStatus("mandatory")


class _Mc2200_GESFPAPSFlowControl_Type(Integer32):
    """Custom type mc2200_GESFPAPSFlowControl based on Integer32"""
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


_Mc2200_GESFPAPSFlowControl_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSFlowControl_Object = MibTableColumn
mc2200_GESFPAPSFlowControl = _Mc2200_GESFPAPSFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 66),
    _Mc2200_GESFPAPSFlowControl_Type()
)
mc2200_GESFPAPSFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSFlowControl.setStatus("current")


class _Mc2200_GESFPAPSRevertive_Type(Integer32):
    """Custom type mc2200_GESFPAPSRevertive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("revertive", 1),
          ("norevertive", 2))
    )


_Mc2200_GESFPAPSRevertive_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSRevertive_Object = MibTableColumn
mc2200_GESFPAPSRevertive = _Mc2200_GESFPAPSRevertive_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 67),
    _Mc2200_GESFPAPSRevertive_Type()
)
mc2200_GESFPAPSRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSRevertive.setStatus("current")


class _Mc2200_GESFPAPSWAN1OpticalPowerCheck_Type(Integer32):
    """Custom type mc2200_GESFPAPSWAN1OpticalPowerCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("aps", 3))
    )


_Mc2200_GESFPAPSWAN1OpticalPowerCheck_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSWAN1OpticalPowerCheck_Object = MibTableColumn
mc2200_GESFPAPSWAN1OpticalPowerCheck = _Mc2200_GESFPAPSWAN1OpticalPowerCheck_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 68),
    _Mc2200_GESFPAPSWAN1OpticalPowerCheck_Type()
)
mc2200_GESFPAPSWAN1OpticalPowerCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSWAN1OpticalPowerCheck.setStatus("current")


class _Mc2200_GESFPAPSWAN1Threshold_Type(Integer32):
    """Custom type mc2200_GESFPAPSWAN1Threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71)
        )
    )
    namedValues = NamedValues(
        *(("db-32", 1),
          ("db-31dot5", 2),
          ("db-31", 3),
          ("db-30dot5", 4),
          ("db-30", 5),
          ("db-29dot5", 6),
          ("db-29", 7),
          ("db-28dot5", 8),
          ("db-28", 9),
          ("db-27dot5", 10),
          ("db-27", 11),
          ("db-26dot5", 12),
          ("db-26", 13),
          ("db-25dot5", 14),
          ("db-25", 15),
          ("db-24dot5", 16),
          ("db-24", 17),
          ("db-23dot5", 18),
          ("db-23", 19),
          ("db-22dot5", 20),
          ("db-22", 21),
          ("db-21dot5", 22),
          ("db-21", 23),
          ("db-20dot5", 24),
          ("db-20", 25),
          ("db-19dot5", 26),
          ("db-19", 27),
          ("db-18dot5", 28),
          ("db-18", 29),
          ("db-17dot5", 30),
          ("db-17", 31),
          ("db-16dot5", 32),
          ("db-16", 33),
          ("db-15dot5", 34),
          ("db-15", 35),
          ("db-14dot5", 36),
          ("db-14", 37),
          ("db-13dot5", 38),
          ("db-13", 39),
          ("db-12dot5", 40),
          ("db-12", 41),
          ("db-11dot5", 42),
          ("db-11", 43),
          ("db-10dot5", 44),
          ("db-10", 45),
          ("db-9dot5", 46),
          ("db-9", 47),
          ("db-8dot5", 48),
          ("db-8", 49),
          ("db-7dot5", 50),
          ("db-7", 51),
          ("db-6dot5", 52),
          ("db-6", 53),
          ("db-5dot5", 54),
          ("db-5", 55),
          ("db-4dot5", 56),
          ("db-4", 57),
          ("db-3dot5", 58),
          ("db-3", 59),
          ("db-2dot5", 60),
          ("db-2", 61),
          ("db-1dot5", 62),
          ("db-1", 63),
          ("db-0dot5", 64),
          ("db-0", 65),
          ("db0dot5", 66),
          ("db1", 67),
          ("db1dot5", 68),
          ("db2", 69),
          ("db2dot5", 70),
          ("db3", 71))
    )


_Mc2200_GESFPAPSWAN1Threshold_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSWAN1Threshold_Object = MibTableColumn
mc2200_GESFPAPSWAN1Threshold = _Mc2200_GESFPAPSWAN1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 69),
    _Mc2200_GESFPAPSWAN1Threshold_Type()
)
mc2200_GESFPAPSWAN1Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSWAN1Threshold.setStatus("current")


class _Mc2200_GESFPAPSWAN2OpticalPowerCheck_Type(Integer32):
    """Custom type mc2200_GESFPAPSWAN2OpticalPowerCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("aps", 3))
    )


_Mc2200_GESFPAPSWAN2OpticalPowerCheck_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSWAN2OpticalPowerCheck_Object = MibTableColumn
mc2200_GESFPAPSWAN2OpticalPowerCheck = _Mc2200_GESFPAPSWAN2OpticalPowerCheck_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 70),
    _Mc2200_GESFPAPSWAN2OpticalPowerCheck_Type()
)
mc2200_GESFPAPSWAN2OpticalPowerCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSWAN2OpticalPowerCheck.setStatus("current")


class _Mc2200_GESFPAPSWAN2Threshold_Type(Integer32):
    """Custom type mc2200_GESFPAPSWAN2Threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71)
        )
    )
    namedValues = NamedValues(
        *(("db-32", 1),
          ("db-31dot5", 2),
          ("db-31", 3),
          ("db-30dot5", 4),
          ("db-30", 5),
          ("db-29dot5", 6),
          ("db-29", 7),
          ("db-28dot5", 8),
          ("db-28", 9),
          ("db-27dot5", 10),
          ("db-27", 11),
          ("db-26dot5", 12),
          ("db-26", 13),
          ("db-25dot5", 14),
          ("db-25", 15),
          ("db-24dot5", 16),
          ("db-24", 17),
          ("db-23dot5", 18),
          ("db-23", 19),
          ("db-22dot5", 20),
          ("db-22", 21),
          ("db-21dot5", 22),
          ("db-21", 23),
          ("db-20dot5", 24),
          ("db-20", 25),
          ("db-19dot5", 26),
          ("db-19", 27),
          ("db-18dot5", 28),
          ("db-18", 29),
          ("db-17dot5", 30),
          ("db-17", 31),
          ("db-16dot5", 32),
          ("db-16", 33),
          ("db-15dot5", 34),
          ("db-15", 35),
          ("db-14dot5", 36),
          ("db-14", 37),
          ("db-13dot5", 38),
          ("db-13", 39),
          ("db-12dot5", 40),
          ("db-12", 41),
          ("db-11dot5", 42),
          ("db-11", 43),
          ("db-10dot5", 44),
          ("db-10", 45),
          ("db-9dot5", 46),
          ("db-9", 47),
          ("db-8dot5", 48),
          ("db-8", 49),
          ("db-7dot5", 50),
          ("db-7", 51),
          ("db-6dot5", 52),
          ("db-6", 53),
          ("db-5dot5", 54),
          ("db-5", 55),
          ("db-4dot5", 56),
          ("db-4", 57),
          ("db-3dot5", 58),
          ("db-3", 59),
          ("db-2dot5", 60),
          ("db-2", 61),
          ("db-1dot5", 62),
          ("db-1", 63),
          ("db-0dot5", 64),
          ("db-0", 65),
          ("db0dot5", 66),
          ("db1", 67),
          ("db1dot5", 68),
          ("db2", 69),
          ("db2dot5", 70),
          ("db3", 71))
    )


_Mc2200_GESFPAPSWAN2Threshold_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSWAN2Threshold_Object = MibTableColumn
mc2200_GESFPAPSWAN2Threshold = _Mc2200_GESFPAPSWAN2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 71),
    _Mc2200_GESFPAPSWAN2Threshold_Type()
)
mc2200_GESFPAPSWAN2Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSWAN2Threshold.setStatus("current")


class _Mc2200_GESFPAPSTrapFilterLocalLAN_Type(Integer32):
    """Custom type mc2200_GESFPAPSTrapFilterLocalLAN based on Integer32"""
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


_Mc2200_GESFPAPSTrapFilterLocalLAN_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSTrapFilterLocalLAN_Object = MibTableColumn
mc2200_GESFPAPSTrapFilterLocalLAN = _Mc2200_GESFPAPSTrapFilterLocalLAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 72),
    _Mc2200_GESFPAPSTrapFilterLocalLAN_Type()
)
mc2200_GESFPAPSTrapFilterLocalLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSTrapFilterLocalLAN.setStatus("current")


class _Mc2200_GESFPAPSTrapFilterLocalWAN_Type(Integer32):
    """Custom type mc2200_GESFPAPSTrapFilterLocalWAN based on Integer32"""
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


_Mc2200_GESFPAPSTrapFilterLocalWAN_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSTrapFilterLocalWAN_Object = MibTableColumn
mc2200_GESFPAPSTrapFilterLocalWAN = _Mc2200_GESFPAPSTrapFilterLocalWAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 73),
    _Mc2200_GESFPAPSTrapFilterLocalWAN_Type()
)
mc2200_GESFPAPSTrapFilterLocalWAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSTrapFilterLocalWAN.setStatus("current")


class _Mc2200_GESFPAPSTrapFilterRemotePower_Type(Integer32):
    """Custom type mc2200_GESFPAPSTrapFilterRemotePower based on Integer32"""
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


_Mc2200_GESFPAPSTrapFilterRemotePower_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSTrapFilterRemotePower_Object = MibTableColumn
mc2200_GESFPAPSTrapFilterRemotePower = _Mc2200_GESFPAPSTrapFilterRemotePower_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 74),
    _Mc2200_GESFPAPSTrapFilterRemotePower_Type()
)
mc2200_GESFPAPSTrapFilterRemotePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSTrapFilterRemotePower.setStatus("current")


class _Mc2200_GESFPAPSTrapFilterRemoteLAN_Type(Integer32):
    """Custom type mc2200_GESFPAPSTrapFilterRemoteLAN based on Integer32"""
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


_Mc2200_GESFPAPSTrapFilterRemoteLAN_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSTrapFilterRemoteLAN_Object = MibTableColumn
mc2200_GESFPAPSTrapFilterRemoteLAN = _Mc2200_GESFPAPSTrapFilterRemoteLAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 75),
    _Mc2200_GESFPAPSTrapFilterRemoteLAN_Type()
)
mc2200_GESFPAPSTrapFilterRemoteLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSTrapFilterRemoteLAN.setStatus("current")


class _Mc2200_GESFPAPSTrapFilterRemoteWAN_Type(Integer32):
    """Custom type mc2200_GESFPAPSTrapFilterRemoteWAN based on Integer32"""
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


_Mc2200_GESFPAPSTrapFilterRemoteWAN_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSTrapFilterRemoteWAN_Object = MibTableColumn
mc2200_GESFPAPSTrapFilterRemoteWAN = _Mc2200_GESFPAPSTrapFilterRemoteWAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 76),
    _Mc2200_GESFPAPSTrapFilterRemoteWAN_Type()
)
mc2200_GESFPAPSTrapFilterRemoteWAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSTrapFilterRemoteWAN.setStatus("current")


class _Mc2200_GESFPAPSLoopback_Type(Integer32):
    """Custom type mc2200_GESFPAPSLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("local_lanouter", 2),
          ("local_laninner", 3),
          ("local_wanouter", 4),
          ("local_waninner", 5),
          ("remote_lanouter", 6),
          ("remote_laninner", 7))
    )


_Mc2200_GESFPAPSLoopback_Type.__name__ = "Integer32"
_Mc2200_GESFPAPSLoopback_Object = MibTableColumn
mc2200_GESFPAPSLoopback = _Mc2200_GESFPAPSLoopback_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 77),
    _Mc2200_GESFPAPSLoopback_Type()
)
mc2200_GESFPAPSLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSLoopback.setStatus("mandatory")
_Mc2200_GESFPAPSCardType_Type = DisplayString
_Mc2200_GESFPAPSCardType_Object = MibTableColumn
mc2200_GESFPAPSCardType = _Mc2200_GESFPAPSCardType_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 14, 1, 78),
    _Mc2200_GESFPAPSCardType_Type()
)
mc2200_GESFPAPSCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFPAPSCardType.setStatus("current")
_Mc2200_GEMCAPSTable_Object = MibTable
mc2200_GEMCAPSTable = _Mc2200_GEMCAPSTable_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15)
)
if mibBuilder.loadTexts:
    mc2200_GEMCAPSTable.setStatus("current")
_Mc2200_GEMCAPSEntry_Object = MibTableRow
mc2200_GEMCAPSEntry = _Mc2200_GEMCAPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1)
)
mc2200_GEMCAPSEntry.setIndexNames(
    (0, "OnAccess2200-MIB", "mc2200-GEMCAPSCardIndex"),
)
if mibBuilder.loadTexts:
    mc2200_GEMCAPSEntry.setStatus("current")


class _Mc2200_GEMCAPSCardIndex_Type(Integer32):
    """Custom type mc2200_GEMCAPSCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("card01", 1),
          ("card02", 2),
          ("card03", 3),
          ("card04", 4),
          ("card05", 5),
          ("card06", 6),
          ("card07", 7),
          ("card08", 8),
          ("card09", 9),
          ("card10", 10),
          ("card11", 11),
          ("card12", 12),
          ("card13", 13),
          ("card14", 14),
          ("card15", 15))
    )


_Mc2200_GEMCAPSCardIndex_Type.__name__ = "Integer32"
_Mc2200_GEMCAPSCardIndex_Object = MibTableColumn
mc2200_GEMCAPSCardIndex = _Mc2200_GEMCAPSCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 1),
    _Mc2200_GEMCAPSCardIndex_Type()
)
mc2200_GEMCAPSCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSCardIndex.setStatus("current")
_Mc2200_GEMCAPSLocalLANSFPInfo_Type = DisplayString
_Mc2200_GEMCAPSLocalLANSFPInfo_Object = MibTableColumn
mc2200_GEMCAPSLocalLANSFPInfo = _Mc2200_GEMCAPSLocalLANSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 2),
    _Mc2200_GEMCAPSLocalLANSFPInfo_Type()
)
mc2200_GEMCAPSLocalLANSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSLocalLANSFPInfo.setStatus("current")


class _Mc2200_GEMCAPSLocalLANLink_Type(Integer32):
    """Custom type mc2200_GEMCAPSLocalLANLink based on Integer32"""
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


_Mc2200_GEMCAPSLocalLANLink_Type.__name__ = "Integer32"
_Mc2200_GEMCAPSLocalLANLink_Object = MibTableColumn
mc2200_GEMCAPSLocalLANLink = _Mc2200_GEMCAPSLocalLANLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 3),
    _Mc2200_GEMCAPSLocalLANLink_Type()
)
mc2200_GEMCAPSLocalLANLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSLocalLANLink.setStatus("mandatory")
_Mc2200_GEMCAPSLocalWAN1SFPInfo_Type = DisplayString
_Mc2200_GEMCAPSLocalWAN1SFPInfo_Object = MibTableColumn
mc2200_GEMCAPSLocalWAN1SFPInfo = _Mc2200_GEMCAPSLocalWAN1SFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 4),
    _Mc2200_GEMCAPSLocalWAN1SFPInfo_Type()
)
mc2200_GEMCAPSLocalWAN1SFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSLocalWAN1SFPInfo.setStatus("current")


class _Mc2200_GEMCAPSLocalWAN1Link_Type(Integer32):
    """Custom type mc2200_GEMCAPSLocalWAN1Link based on Integer32"""
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
          ("active", 3),
          ("standby", 4))
    )


_Mc2200_GEMCAPSLocalWAN1Link_Type.__name__ = "Integer32"
_Mc2200_GEMCAPSLocalWAN1Link_Object = MibTableColumn
mc2200_GEMCAPSLocalWAN1Link = _Mc2200_GEMCAPSLocalWAN1Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 5),
    _Mc2200_GEMCAPSLocalWAN1Link_Type()
)
mc2200_GEMCAPSLocalWAN1Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSLocalWAN1Link.setStatus("current")
_Mc2200_GEMCAPSLocalWAN2SFPInfo_Type = DisplayString
_Mc2200_GEMCAPSLocalWAN2SFPInfo_Object = MibTableColumn
mc2200_GEMCAPSLocalWAN2SFPInfo = _Mc2200_GEMCAPSLocalWAN2SFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 6),
    _Mc2200_GEMCAPSLocalWAN2SFPInfo_Type()
)
mc2200_GEMCAPSLocalWAN2SFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSLocalWAN2SFPInfo.setStatus("current")


class _Mc2200_GEMCAPSLocalWAN2Link_Type(Integer32):
    """Custom type mc2200_GEMCAPSLocalWAN2Link based on Integer32"""
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
          ("active", 3),
          ("standby", 4))
    )


_Mc2200_GEMCAPSLocalWAN2Link_Type.__name__ = "Integer32"
_Mc2200_GEMCAPSLocalWAN2Link_Object = MibTableColumn
mc2200_GEMCAPSLocalWAN2Link = _Mc2200_GEMCAPSLocalWAN2Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 7),
    _Mc2200_GEMCAPSLocalWAN2Link_Type()
)
mc2200_GEMCAPSLocalWAN2Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSLocalWAN2Link.setStatus("current")


class _Mc2200_GEMCAPSLocalActivePort_Type(Integer32):
    """Custom type mc2200_GEMCAPSLocalActivePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wan1", 1),
          ("wan2", 2))
    )


_Mc2200_GEMCAPSLocalActivePort_Type.__name__ = "Integer32"
_Mc2200_GEMCAPSLocalActivePort_Object = MibTableColumn
mc2200_GEMCAPSLocalActivePort = _Mc2200_GEMCAPSLocalActivePort_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 8),
    _Mc2200_GEMCAPSLocalActivePort_Type()
)
mc2200_GEMCAPSLocalActivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSLocalActivePort.setStatus("current")


class _Mc2200_GEMCAPSLocalLANDownStreamBW_Type(Integer32):
    """Custom type mc2200_GEMCAPSLocalLANDownStreamBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              35,
              40,
              45,
              50,
              55,
              60,
              65,
              70,
              75,
              80,
              85,
              90,
              95,
              100,
              150,
              200,
              250,
              300,
              350,
              400,
              450,
              500,
              550,
              600,
              650,
              700,
              750,
              800,
              850,
              900,
              950,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate35M", 35),
          ("rate40M", 40),
          ("rate45M", 45),
          ("rate50M", 50),
          ("rate55M", 55),
          ("rate60M", 60),
          ("rate65M", 65),
          ("rate70M", 70),
          ("rate75M", 75),
          ("rate80M", 80),
          ("rate85M", 85),
          ("rate90M", 90),
          ("rate95M", 95),
          ("rate100M", 100),
          ("rate150M", 150),
          ("rate200M", 200),
          ("rate250M", 250),
          ("rate300M", 300),
          ("rate350M", 350),
          ("rate400M", 400),
          ("rate450M", 450),
          ("rate500M", 500),
          ("rate550M", 550),
          ("rate600M", 600),
          ("rate650M", 650),
          ("rate700M", 700),
          ("rate750M", 750),
          ("rate800M", 800),
          ("rate850M", 850),
          ("rate900M", 900),
          ("rate950M", 950),
          ("rate1000M", 1000))
    )


_Mc2200_GEMCAPSLocalLANDownStreamBW_Type.__name__ = "Integer32"
_Mc2200_GEMCAPSLocalLANDownStreamBW_Object = MibTableColumn
mc2200_GEMCAPSLocalLANDownStreamBW = _Mc2200_GEMCAPSLocalLANDownStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 9),
    _Mc2200_GEMCAPSLocalLANDownStreamBW_Type()
)
mc2200_GEMCAPSLocalLANDownStreamBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSLocalLANDownStreamBW.setStatus("current")


class _Mc2200_GEMCAPSLocalLANUpStreamBW_Type(Integer32):
    """Custom type mc2200_GEMCAPSLocalLANUpStreamBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              35,
              40,
              45,
              50,
              55,
              60,
              65,
              70,
              75,
              80,
              85,
              90,
              95,
              100,
              150,
              200,
              250,
              300,
              350,
              400,
              450,
              500,
              550,
              600,
              650,
              700,
              750,
              800,
              850,
              900,
              950,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate35M", 35),
          ("rate40M", 40),
          ("rate45M", 45),
          ("rate50M", 50),
          ("rate55M", 55),
          ("rate60M", 60),
          ("rate65M", 65),
          ("rate70M", 70),
          ("rate75M", 75),
          ("rate80M", 80),
          ("rate85M", 85),
          ("rate90M", 90),
          ("rate95M", 95),
          ("rate100M", 100),
          ("rate150M", 150),
          ("rate200M", 200),
          ("rate250M", 250),
          ("rate300M", 300),
          ("rate350M", 350),
          ("rate400M", 400),
          ("rate450M", 450),
          ("rate500M", 500),
          ("rate550M", 550),
          ("rate600M", 600),
          ("rate650M", 650),
          ("rate700M", 700),
          ("rate750M", 750),
          ("rate800M", 800),
          ("rate850M", 850),
          ("rate900M", 900),
          ("rate950M", 950),
          ("rate1000M", 1000))
    )


_Mc2200_GEMCAPSLocalLANUpStreamBW_Type.__name__ = "Integer32"
_Mc2200_GEMCAPSLocalLANUpStreamBW_Object = MibTableColumn
mc2200_GEMCAPSLocalLANUpStreamBW = _Mc2200_GEMCAPSLocalLANUpStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 10),
    _Mc2200_GEMCAPSLocalLANUpStreamBW_Type()
)
mc2200_GEMCAPSLocalLANUpStreamBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSLocalLANUpStreamBW.setStatus("current")


class _Mc2200_GEMCAPSLocalLANMode_Type(Integer32):
    """Custom type mc2200_GEMCAPSLocalLANMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("mode1000Base-X-auto", 1),
          ("mode1000Base-X-Force", 2),
          ("auto-10-100-1000T", 3),
          ("mode1000Base-T-full", 4),
          ("mode100Base-T-full", 5),
          ("mode100Base-T-Half", 6),
          ("mode10Base-T-full", 7),
          ("mode10Base-T-Half", 8))
    )


_Mc2200_GEMCAPSLocalLANMode_Type.__name__ = "Integer32"
_Mc2200_GEMCAPSLocalLANMode_Object = MibTableColumn
mc2200_GEMCAPSLocalLANMode = _Mc2200_GEMCAPSLocalLANMode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 11),
    _Mc2200_GEMCAPSLocalLANMode_Type()
)
mc2200_GEMCAPSLocalLANMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSLocalLANMode.setStatus("current")
_Mc2200_GEMCAPSRxGoodOctets_Type = Counter64
_Mc2200_GEMCAPSRxGoodOctets_Object = MibTableColumn
mc2200_GEMCAPSRxGoodOctets = _Mc2200_GEMCAPSRxGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 12),
    _Mc2200_GEMCAPSRxGoodOctets_Type()
)
mc2200_GEMCAPSRxGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRxGoodOctets.setStatus("current")
_Mc2200_GEMCAPSRxBadOctets_Type = Counter64
_Mc2200_GEMCAPSRxBadOctets_Object = MibTableColumn
mc2200_GEMCAPSRxBadOctets = _Mc2200_GEMCAPSRxBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 14),
    _Mc2200_GEMCAPSRxBadOctets_Type()
)
mc2200_GEMCAPSRxBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRxBadOctets.setStatus("current")
_Mc2200_GEMCAPSTxFCSErr_Type = Counter64
_Mc2200_GEMCAPSTxFCSErr_Object = MibTableColumn
mc2200_GEMCAPSTxFCSErr = _Mc2200_GEMCAPSTxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 15),
    _Mc2200_GEMCAPSTxFCSErr_Type()
)
mc2200_GEMCAPSTxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSTxFCSErr.setStatus("current")
_Mc2200_GEMCAPSRxUnicast_Type = Counter64
_Mc2200_GEMCAPSRxUnicast_Object = MibTableColumn
mc2200_GEMCAPSRxUnicast = _Mc2200_GEMCAPSRxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 16),
    _Mc2200_GEMCAPSRxUnicast_Type()
)
mc2200_GEMCAPSRxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRxUnicast.setStatus("current")
_Mc2200_GEMCAPSTxDeferred_Type = Counter64
_Mc2200_GEMCAPSTxDeferred_Object = MibTableColumn
mc2200_GEMCAPSTxDeferred = _Mc2200_GEMCAPSTxDeferred_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 17),
    _Mc2200_GEMCAPSTxDeferred_Type()
)
mc2200_GEMCAPSTxDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSTxDeferred.setStatus("current")
_Mc2200_GEMCAPSRxBroadcasts_Type = Counter64
_Mc2200_GEMCAPSRxBroadcasts_Object = MibTableColumn
mc2200_GEMCAPSRxBroadcasts = _Mc2200_GEMCAPSRxBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 18),
    _Mc2200_GEMCAPSRxBroadcasts_Type()
)
mc2200_GEMCAPSRxBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRxBroadcasts.setStatus("current")
_Mc2200_GEMCAPSRxMulticasts_Type = Counter64
_Mc2200_GEMCAPSRxMulticasts_Object = MibTableColumn
mc2200_GEMCAPSRxMulticasts = _Mc2200_GEMCAPSRxMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 19),
    _Mc2200_GEMCAPSRxMulticasts_Type()
)
mc2200_GEMCAPSRxMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRxMulticasts.setStatus("current")
_Mc2200_GEMCAPSRx64Octets_Type = Counter64
_Mc2200_GEMCAPSRx64Octets_Object = MibTableColumn
mc2200_GEMCAPSRx64Octets = _Mc2200_GEMCAPSRx64Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 20),
    _Mc2200_GEMCAPSRx64Octets_Type()
)
mc2200_GEMCAPSRx64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRx64Octets.setStatus("current")
_Mc2200_GEMCAPSRx65to127Octets_Type = Counter64
_Mc2200_GEMCAPSRx65to127Octets_Object = MibTableColumn
mc2200_GEMCAPSRx65to127Octets = _Mc2200_GEMCAPSRx65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 21),
    _Mc2200_GEMCAPSRx65to127Octets_Type()
)
mc2200_GEMCAPSRx65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRx65to127Octets.setStatus("current")
_Mc2200_GEMCAPSRx128to255Octets_Type = Counter64
_Mc2200_GEMCAPSRx128to255Octets_Object = MibTableColumn
mc2200_GEMCAPSRx128to255Octets = _Mc2200_GEMCAPSRx128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 22),
    _Mc2200_GEMCAPSRx128to255Octets_Type()
)
mc2200_GEMCAPSRx128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRx128to255Octets.setStatus("current")
_Mc2200_GEMCAPSRx256to511Octets_Type = Counter64
_Mc2200_GEMCAPSRx256to511Octets_Object = MibTableColumn
mc2200_GEMCAPSRx256to511Octets = _Mc2200_GEMCAPSRx256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 23),
    _Mc2200_GEMCAPSRx256to511Octets_Type()
)
mc2200_GEMCAPSRx256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRx256to511Octets.setStatus("current")
_Mc2200_GEMCAPSRx512to1023Octets_Type = Counter64
_Mc2200_GEMCAPSRx512to1023Octets_Object = MibTableColumn
mc2200_GEMCAPSRx512to1023Octets = _Mc2200_GEMCAPSRx512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 24),
    _Mc2200_GEMCAPSRx512to1023Octets_Type()
)
mc2200_GEMCAPSRx512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRx512to1023Octets.setStatus("current")
_Mc2200_GEMCAPSRx1024toMaxOctets_Type = Counter64
_Mc2200_GEMCAPSRx1024toMaxOctets_Object = MibTableColumn
mc2200_GEMCAPSRx1024toMaxOctets = _Mc2200_GEMCAPSRx1024toMaxOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 25),
    _Mc2200_GEMCAPSRx1024toMaxOctets_Type()
)
mc2200_GEMCAPSRx1024toMaxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRx1024toMaxOctets.setStatus("current")
_Mc2200_GEMCAPSTxOctets_Type = Counter64
_Mc2200_GEMCAPSTxOctets_Object = MibTableColumn
mc2200_GEMCAPSTxOctets = _Mc2200_GEMCAPSTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 26),
    _Mc2200_GEMCAPSTxOctets_Type()
)
mc2200_GEMCAPSTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSTxOctets.setStatus("current")
_Mc2200_GEMCAPSTxUnicast_Type = Counter64
_Mc2200_GEMCAPSTxUnicast_Object = MibTableColumn
mc2200_GEMCAPSTxUnicast = _Mc2200_GEMCAPSTxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 28),
    _Mc2200_GEMCAPSTxUnicast_Type()
)
mc2200_GEMCAPSTxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSTxUnicast.setStatus("current")
_Mc2200_GEMCAPSTxExcessive_Type = Counter64
_Mc2200_GEMCAPSTxExcessive_Object = MibTableColumn
mc2200_GEMCAPSTxExcessive = _Mc2200_GEMCAPSTxExcessive_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 29),
    _Mc2200_GEMCAPSTxExcessive_Type()
)
mc2200_GEMCAPSTxExcessive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSTxExcessive.setStatus("current")
_Mc2200_GEMCAPSTxMulticasts_Type = Counter64
_Mc2200_GEMCAPSTxMulticasts_Object = MibTableColumn
mc2200_GEMCAPSTxMulticasts = _Mc2200_GEMCAPSTxMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 30),
    _Mc2200_GEMCAPSTxMulticasts_Type()
)
mc2200_GEMCAPSTxMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSTxMulticasts.setStatus("current")
_Mc2200_GEMCAPSTxBroadcasts_Type = Counter64
_Mc2200_GEMCAPSTxBroadcasts_Object = MibTableColumn
mc2200_GEMCAPSTxBroadcasts = _Mc2200_GEMCAPSTxBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 31),
    _Mc2200_GEMCAPSTxBroadcasts_Type()
)
mc2200_GEMCAPSTxBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSTxBroadcasts.setStatus("current")
_Mc2200_GEMCAPSTxSingle_Type = Counter64
_Mc2200_GEMCAPSTxSingle_Object = MibTableColumn
mc2200_GEMCAPSTxSingle = _Mc2200_GEMCAPSTxSingle_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 32),
    _Mc2200_GEMCAPSTxSingle_Type()
)
mc2200_GEMCAPSTxSingle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSTxSingle.setStatus("current")
_Mc2200_GEMCAPSTxPause_Type = Counter64
_Mc2200_GEMCAPSTxPause_Object = MibTableColumn
mc2200_GEMCAPSTxPause = _Mc2200_GEMCAPSTxPause_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 33),
    _Mc2200_GEMCAPSTxPause_Type()
)
mc2200_GEMCAPSTxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSTxPause.setStatus("current")
_Mc2200_GEMCAPSRxPause_Type = Counter64
_Mc2200_GEMCAPSRxPause_Object = MibTableColumn
mc2200_GEMCAPSRxPause = _Mc2200_GEMCAPSRxPause_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 34),
    _Mc2200_GEMCAPSRxPause_Type()
)
mc2200_GEMCAPSRxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRxPause.setStatus("current")
_Mc2200_GEMCAPSTxMultiple_Type = Counter64
_Mc2200_GEMCAPSTxMultiple_Object = MibTableColumn
mc2200_GEMCAPSTxMultiple = _Mc2200_GEMCAPSTxMultiple_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 35),
    _Mc2200_GEMCAPSTxMultiple_Type()
)
mc2200_GEMCAPSTxMultiple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSTxMultiple.setStatus("current")
_Mc2200_GEMCAPSRxUndersize_Type = Counter64
_Mc2200_GEMCAPSRxUndersize_Object = MibTableColumn
mc2200_GEMCAPSRxUndersize = _Mc2200_GEMCAPSRxUndersize_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 36),
    _Mc2200_GEMCAPSRxUndersize_Type()
)
mc2200_GEMCAPSRxUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRxUndersize.setStatus("current")
_Mc2200_GEMCAPSRxFragments_Type = Counter64
_Mc2200_GEMCAPSRxFragments_Object = MibTableColumn
mc2200_GEMCAPSRxFragments = _Mc2200_GEMCAPSRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 37),
    _Mc2200_GEMCAPSRxFragments_Type()
)
mc2200_GEMCAPSRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRxFragments.setStatus("current")
_Mc2200_GEMCAPSRxOversize_Type = Counter64
_Mc2200_GEMCAPSRxOversize_Object = MibTableColumn
mc2200_GEMCAPSRxOversize = _Mc2200_GEMCAPSRxOversize_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 38),
    _Mc2200_GEMCAPSRxOversize_Type()
)
mc2200_GEMCAPSRxOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRxOversize.setStatus("current")
_Mc2200_GEMCAPSRxJabber_Type = Counter64
_Mc2200_GEMCAPSRxJabber_Object = MibTableColumn
mc2200_GEMCAPSRxJabber = _Mc2200_GEMCAPSRxJabber_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 39),
    _Mc2200_GEMCAPSRxJabber_Type()
)
mc2200_GEMCAPSRxJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRxJabber.setStatus("current")
_Mc2200_GEMCAPSRxErr_Type = Counter64
_Mc2200_GEMCAPSRxErr_Object = MibTableColumn
mc2200_GEMCAPSRxErr = _Mc2200_GEMCAPSRxErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 40),
    _Mc2200_GEMCAPSRxErr_Type()
)
mc2200_GEMCAPSRxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRxErr.setStatus("current")
_Mc2200_GEMCAPSRxFCSErr_Type = Counter64
_Mc2200_GEMCAPSRxFCSErr_Object = MibTableColumn
mc2200_GEMCAPSRxFCSErr = _Mc2200_GEMCAPSRxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 41),
    _Mc2200_GEMCAPSRxFCSErr_Type()
)
mc2200_GEMCAPSRxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRxFCSErr.setStatus("current")
_Mc2200_GEMCAPSTxCollisions_Type = Counter64
_Mc2200_GEMCAPSTxCollisions_Object = MibTableColumn
mc2200_GEMCAPSTxCollisions = _Mc2200_GEMCAPSTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 42),
    _Mc2200_GEMCAPSTxCollisions_Type()
)
mc2200_GEMCAPSTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSTxCollisions.setStatus("current")
_Mc2200_GEMCAPSTxLate_Type = Counter64
_Mc2200_GEMCAPSTxLate_Object = MibTableColumn
mc2200_GEMCAPSTxLate = _Mc2200_GEMCAPSTxLate_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 43),
    _Mc2200_GEMCAPSTxLate_Type()
)
mc2200_GEMCAPSTxLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSTxLate.setStatus("current")
_Mc2200_GEMCAPSRemoteLANSFPInfo_Type = DisplayString
_Mc2200_GEMCAPSRemoteLANSFPInfo_Object = MibTableColumn
mc2200_GEMCAPSRemoteLANSFPInfo = _Mc2200_GEMCAPSRemoteLANSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 44),
    _Mc2200_GEMCAPSRemoteLANSFPInfo_Type()
)
mc2200_GEMCAPSRemoteLANSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRemoteLANSFPInfo.setStatus("current")


class _Mc2200_GEMCAPSRemoteLANLink_Type(Integer32):
    """Custom type mc2200_GEMCAPSRemoteLANLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_GEMCAPSRemoteLANLink_Type.__name__ = "Integer32"
_Mc2200_GEMCAPSRemoteLANLink_Object = MibTableColumn
mc2200_GEMCAPSRemoteLANLink = _Mc2200_GEMCAPSRemoteLANLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 45),
    _Mc2200_GEMCAPSRemoteLANLink_Type()
)
mc2200_GEMCAPSRemoteLANLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRemoteLANLink.setStatus("mandatory")
_Mc2200_GEMCAPSRemoteWAN1SFPInfo_Type = DisplayString
_Mc2200_GEMCAPSRemoteWAN1SFPInfo_Object = MibTableColumn
mc2200_GEMCAPSRemoteWAN1SFPInfo = _Mc2200_GEMCAPSRemoteWAN1SFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 46),
    _Mc2200_GEMCAPSRemoteWAN1SFPInfo_Type()
)
mc2200_GEMCAPSRemoteWAN1SFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRemoteWAN1SFPInfo.setStatus("current")


class _Mc2200_GEMCAPSRemoteWAN1Link_Type(Integer32):
    """Custom type mc2200_GEMCAPSRemoteWAN1Link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2),
          ("active", 3),
          ("standby", 4))
    )


_Mc2200_GEMCAPSRemoteWAN1Link_Type.__name__ = "Integer32"
_Mc2200_GEMCAPSRemoteWAN1Link_Object = MibTableColumn
mc2200_GEMCAPSRemoteWAN1Link = _Mc2200_GEMCAPSRemoteWAN1Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 47),
    _Mc2200_GEMCAPSRemoteWAN1Link_Type()
)
mc2200_GEMCAPSRemoteWAN1Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRemoteWAN1Link.setStatus("current")
_Mc2200_GEMCAPSRemoteWAN2SFPInfo_Type = DisplayString
_Mc2200_GEMCAPSRemoteWAN2SFPInfo_Object = MibTableColumn
mc2200_GEMCAPSRemoteWAN2SFPInfo = _Mc2200_GEMCAPSRemoteWAN2SFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 48),
    _Mc2200_GEMCAPSRemoteWAN2SFPInfo_Type()
)
mc2200_GEMCAPSRemoteWAN2SFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRemoteWAN2SFPInfo.setStatus("current")


class _Mc2200_GEMCAPSRemoteWAN2Link_Type(Integer32):
    """Custom type mc2200_GEMCAPSRemoteWAN2Link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2),
          ("active", 3),
          ("standby", 4))
    )


_Mc2200_GEMCAPSRemoteWAN2Link_Type.__name__ = "Integer32"
_Mc2200_GEMCAPSRemoteWAN2Link_Object = MibTableColumn
mc2200_GEMCAPSRemoteWAN2Link = _Mc2200_GEMCAPSRemoteWAN2Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 49),
    _Mc2200_GEMCAPSRemoteWAN2Link_Type()
)
mc2200_GEMCAPSRemoteWAN2Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRemoteWAN2Link.setStatus("current")


class _Mc2200_GEMCAPSRemoteLANMode_Type(Integer32):
    """Custom type mc2200_GEMCAPSRemoteLANMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("mode1000Base-X-auto", 1),
          ("mode1000Base-X-Force", 2),
          ("auto-10-100-1000T", 3),
          ("mode1000Base-T-full", 4),
          ("mode100Base-T-full", 5),
          ("mode100Base-T-Half", 6),
          ("mode10Base-T-full", 7),
          ("mode10Base-T-Half", 8))
    )


_Mc2200_GEMCAPSRemoteLANMode_Type.__name__ = "Integer32"
_Mc2200_GEMCAPSRemoteLANMode_Object = MibTableColumn
mc2200_GEMCAPSRemoteLANMode = _Mc2200_GEMCAPSRemoteLANMode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 50),
    _Mc2200_GEMCAPSRemoteLANMode_Type()
)
mc2200_GEMCAPSRemoteLANMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRemoteLANMode.setStatus("current")
_Mc2200_GEMCAPSRemoteIPAddress_Type = IpAddress
_Mc2200_GEMCAPSRemoteIPAddress_Object = MibTableColumn
mc2200_GEMCAPSRemoteIPAddress = _Mc2200_GEMCAPSRemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 51),
    _Mc2200_GEMCAPSRemoteIPAddress_Type()
)
mc2200_GEMCAPSRemoteIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRemoteIPAddress.setStatus("mandatory")
_Mc2200_GEMCAPSRemoteSubnetMask_Type = IpAddress
_Mc2200_GEMCAPSRemoteSubnetMask_Object = MibTableColumn
mc2200_GEMCAPSRemoteSubnetMask = _Mc2200_GEMCAPSRemoteSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 52),
    _Mc2200_GEMCAPSRemoteSubnetMask_Type()
)
mc2200_GEMCAPSRemoteSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRemoteSubnetMask.setStatus("mandatory")
_Mc2200_GEMCAPSRemoteGateWay_Type = IpAddress
_Mc2200_GEMCAPSRemoteGateWay_Object = MibTableColumn
mc2200_GEMCAPSRemoteGateWay = _Mc2200_GEMCAPSRemoteGateWay_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 53),
    _Mc2200_GEMCAPSRemoteGateWay_Type()
)
mc2200_GEMCAPSRemoteGateWay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRemoteGateWay.setStatus("mandatory")


class _Mc2200_GEMCAPSRemoteVLANEnable_Type(Integer32):
    """Custom type mc2200_GEMCAPSRemoteVLANEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("enable", 1),
          ("disable", 2))
    )


_Mc2200_GEMCAPSRemoteVLANEnable_Type.__name__ = "Integer32"
_Mc2200_GEMCAPSRemoteVLANEnable_Object = MibTableColumn
mc2200_GEMCAPSRemoteVLANEnable = _Mc2200_GEMCAPSRemoteVLANEnable_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 54),
    _Mc2200_GEMCAPSRemoteVLANEnable_Type()
)
mc2200_GEMCAPSRemoteVLANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRemoteVLANEnable.setStatus("mandatory")
_Mc2200_GEMCAPSRemoteVID_Type = Integer32
_Mc2200_GEMCAPSRemoteVID_Object = MibTableColumn
mc2200_GEMCAPSRemoteVID = _Mc2200_GEMCAPSRemoteVID_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 55),
    _Mc2200_GEMCAPSRemoteVID_Type()
)
mc2200_GEMCAPSRemoteVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRemoteVID.setStatus("mandatory")


class _Mc2200_GEMCAPSRemoteAlarm_Type(Integer32):
    """Custom type mc2200_GEMCAPSRemoteAlarm based on Integer32"""
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


_Mc2200_GEMCAPSRemoteAlarm_Type.__name__ = "Integer32"
_Mc2200_GEMCAPSRemoteAlarm_Object = MibTableColumn
mc2200_GEMCAPSRemoteAlarm = _Mc2200_GEMCAPSRemoteAlarm_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 56),
    _Mc2200_GEMCAPSRemoteAlarm_Type()
)
mc2200_GEMCAPSRemoteAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRemoteAlarm.setStatus("current")


class _Mc2200_GEMCAPSRFD_Type(Integer32):
    """Custom type mc2200_GEMCAPSRFD based on Integer32"""
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


_Mc2200_GEMCAPSRFD_Type.__name__ = "Integer32"
_Mc2200_GEMCAPSRFD_Object = MibTableColumn
mc2200_GEMCAPSRFD = _Mc2200_GEMCAPSRFD_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 57),
    _Mc2200_GEMCAPSRFD_Type()
)
mc2200_GEMCAPSRFD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRFD.setStatus("current")
_Mc2200_GEMCAPSDefault_Type = Integer32
_Mc2200_GEMCAPSDefault_Object = MibTableColumn
mc2200_GEMCAPSDefault = _Mc2200_GEMCAPSDefault_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 58),
    _Mc2200_GEMCAPSDefault_Type()
)
mc2200_GEMCAPSDefault.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSDefault.setStatus("current")
_Mc2200_GEMCAPSReboot_Type = Integer32
_Mc2200_GEMCAPSReboot_Object = MibTableColumn
mc2200_GEMCAPSReboot = _Mc2200_GEMCAPSReboot_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 59),
    _Mc2200_GEMCAPSReboot_Type()
)
mc2200_GEMCAPSReboot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSReboot.setStatus("current")


class _Mc2200_GEMCAPSLocalLANSpeed_Type(Integer32):
    """Custom type mc2200_GEMCAPSLocalLANSpeed based on Integer32"""
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
        *(("speed1000M", 1),
          ("speed100M", 2),
          ("speed10M", 3),
          ("down", 4))
    )


_Mc2200_GEMCAPSLocalLANSpeed_Type.__name__ = "Integer32"
_Mc2200_GEMCAPSLocalLANSpeed_Object = MibTableColumn
mc2200_GEMCAPSLocalLANSpeed = _Mc2200_GEMCAPSLocalLANSpeed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 60),
    _Mc2200_GEMCAPSLocalLANSpeed_Type()
)
mc2200_GEMCAPSLocalLANSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSLocalLANSpeed.setStatus("mandatory")


class _Mc2200_GEMCAPSRemoteLANSpeed_Type(Integer32):
    """Custom type mc2200_GEMCAPSRemoteLANSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("speed1000M", 1),
          ("speed100M", 2),
          ("speed10M", 3),
          ("down", 4))
    )


_Mc2200_GEMCAPSRemoteLANSpeed_Type.__name__ = "Integer32"
_Mc2200_GEMCAPSRemoteLANSpeed_Object = MibTableColumn
mc2200_GEMCAPSRemoteLANSpeed = _Mc2200_GEMCAPSRemoteLANSpeed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 61),
    _Mc2200_GEMCAPSRemoteLANSpeed_Type()
)
mc2200_GEMCAPSRemoteLANSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRemoteLANSpeed.setStatus("mandatory")
_Mc2200_GEMCAPSLocalportuser_Type = DisplayString
_Mc2200_GEMCAPSLocalportuser_Object = MibTableColumn
mc2200_GEMCAPSLocalportuser = _Mc2200_GEMCAPSLocalportuser_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 62),
    _Mc2200_GEMCAPSLocalportuser_Type()
)
mc2200_GEMCAPSLocalportuser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSLocalportuser.setStatus("current")
_Mc2200_GEMCAPSRemoteportuser_Type = DisplayString
_Mc2200_GEMCAPSRemoteportuser_Object = MibTableColumn
mc2200_GEMCAPSRemoteportuser = _Mc2200_GEMCAPSRemoteportuser_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 63),
    _Mc2200_GEMCAPSRemoteportuser_Type()
)
mc2200_GEMCAPSRemoteportuser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRemoteportuser.setStatus("current")


class _Mc2200_GEMCAPSRevertive_Type(Integer32):
    """Custom type mc2200_GEMCAPSRevertive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("revertive", 1),
          ("norevertive", 2))
    )


_Mc2200_GEMCAPSRevertive_Type.__name__ = "Integer32"
_Mc2200_GEMCAPSRevertive_Object = MibTableColumn
mc2200_GEMCAPSRevertive = _Mc2200_GEMCAPSRevertive_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 64),
    _Mc2200_GEMCAPSRevertive_Type()
)
mc2200_GEMCAPSRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSRevertive.setStatus("current")


class _Mc2200_GEMCAPSWAN1OpticalPowerCheck_Type(Integer32):
    """Custom type mc2200_GEMCAPSWAN1OpticalPowerCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("aps", 3))
    )


_Mc2200_GEMCAPSWAN1OpticalPowerCheck_Type.__name__ = "Integer32"
_Mc2200_GEMCAPSWAN1OpticalPowerCheck_Object = MibTableColumn
mc2200_GEMCAPSWAN1OpticalPowerCheck = _Mc2200_GEMCAPSWAN1OpticalPowerCheck_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 65),
    _Mc2200_GEMCAPSWAN1OpticalPowerCheck_Type()
)
mc2200_GEMCAPSWAN1OpticalPowerCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSWAN1OpticalPowerCheck.setStatus("current")


class _Mc2200_GEMCAPSWAN1Threshold_Type(Integer32):
    """Custom type mc2200_GEMCAPSWAN1Threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71)
        )
    )
    namedValues = NamedValues(
        *(("db-32", 1),
          ("db-31dot5", 2),
          ("db-31", 3),
          ("db-30dot5", 4),
          ("db-30", 5),
          ("db-29dot5", 6),
          ("db-29", 7),
          ("db-28dot5", 8),
          ("db-28", 9),
          ("db-27dot5", 10),
          ("db-27", 11),
          ("db-26dot5", 12),
          ("db-26", 13),
          ("db-25dot5", 14),
          ("db-25", 15),
          ("db-24dot5", 16),
          ("db-24", 17),
          ("db-23dot5", 18),
          ("db-23", 19),
          ("db-22dot5", 20),
          ("db-22", 21),
          ("db-21dot5", 22),
          ("db-21", 23),
          ("db-20dot5", 24),
          ("db-20", 25),
          ("db-19dot5", 26),
          ("db-19", 27),
          ("db-18dot5", 28),
          ("db-18", 29),
          ("db-17dot5", 30),
          ("db-17", 31),
          ("db-16dot5", 32),
          ("db-16", 33),
          ("db-15dot5", 34),
          ("db-15", 35),
          ("db-14dot5", 36),
          ("db-14", 37),
          ("db-13dot5", 38),
          ("db-13", 39),
          ("db-12dot5", 40),
          ("db-12", 41),
          ("db-11dot5", 42),
          ("db-11", 43),
          ("db-10dot5", 44),
          ("db-10", 45),
          ("db-9dot5", 46),
          ("db-9", 47),
          ("db-8dot5", 48),
          ("db-8", 49),
          ("db-7dot5", 50),
          ("db-7", 51),
          ("db-6dot5", 52),
          ("db-6", 53),
          ("db-5dot5", 54),
          ("db-5", 55),
          ("db-4dot5", 56),
          ("db-4", 57),
          ("db-3dot5", 58),
          ("db-3", 59),
          ("db-2dot5", 60),
          ("db-2", 61),
          ("db-1dot5", 62),
          ("db-1", 63),
          ("db-0dot5", 64),
          ("db-0", 65),
          ("db0dot5", 66),
          ("db1", 67),
          ("db1dot5", 68),
          ("db2", 69),
          ("db2dot5", 70),
          ("db3", 71))
    )


_Mc2200_GEMCAPSWAN1Threshold_Type.__name__ = "Integer32"
_Mc2200_GEMCAPSWAN1Threshold_Object = MibTableColumn
mc2200_GEMCAPSWAN1Threshold = _Mc2200_GEMCAPSWAN1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 66),
    _Mc2200_GEMCAPSWAN1Threshold_Type()
)
mc2200_GEMCAPSWAN1Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSWAN1Threshold.setStatus("current")


class _Mc2200_GEMCAPSWAN2OpticalPowerCheck_Type(Integer32):
    """Custom type mc2200_GEMCAPSWAN2OpticalPowerCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("aps", 3))
    )


_Mc2200_GEMCAPSWAN2OpticalPowerCheck_Type.__name__ = "Integer32"
_Mc2200_GEMCAPSWAN2OpticalPowerCheck_Object = MibTableColumn
mc2200_GEMCAPSWAN2OpticalPowerCheck = _Mc2200_GEMCAPSWAN2OpticalPowerCheck_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 67),
    _Mc2200_GEMCAPSWAN2OpticalPowerCheck_Type()
)
mc2200_GEMCAPSWAN2OpticalPowerCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSWAN2OpticalPowerCheck.setStatus("current")


class _Mc2200_GEMCAPSWAN2Threshold_Type(Integer32):
    """Custom type mc2200_GEMCAPSWAN2Threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71)
        )
    )
    namedValues = NamedValues(
        *(("db-32", 1),
          ("db-31dot5", 2),
          ("db-31", 3),
          ("db-30dot5", 4),
          ("db-30", 5),
          ("db-29dot5", 6),
          ("db-29", 7),
          ("db-28dot5", 8),
          ("db-28", 9),
          ("db-27dot5", 10),
          ("db-27", 11),
          ("db-26dot5", 12),
          ("db-26", 13),
          ("db-25dot5", 14),
          ("db-25", 15),
          ("db-24dot5", 16),
          ("db-24", 17),
          ("db-23dot5", 18),
          ("db-23", 19),
          ("db-22dot5", 20),
          ("db-22", 21),
          ("db-21dot5", 22),
          ("db-21", 23),
          ("db-20dot5", 24),
          ("db-20", 25),
          ("db-19dot5", 26),
          ("db-19", 27),
          ("db-18dot5", 28),
          ("db-18", 29),
          ("db-17dot5", 30),
          ("db-17", 31),
          ("db-16dot5", 32),
          ("db-16", 33),
          ("db-15dot5", 34),
          ("db-15", 35),
          ("db-14dot5", 36),
          ("db-14", 37),
          ("db-13dot5", 38),
          ("db-13", 39),
          ("db-12dot5", 40),
          ("db-12", 41),
          ("db-11dot5", 42),
          ("db-11", 43),
          ("db-10dot5", 44),
          ("db-10", 45),
          ("db-9dot5", 46),
          ("db-9", 47),
          ("db-8dot5", 48),
          ("db-8", 49),
          ("db-7dot5", 50),
          ("db-7", 51),
          ("db-6dot5", 52),
          ("db-6", 53),
          ("db-5dot5", 54),
          ("db-5", 55),
          ("db-4dot5", 56),
          ("db-4", 57),
          ("db-3dot5", 58),
          ("db-3", 59),
          ("db-2dot5", 60),
          ("db-2", 61),
          ("db-1dot5", 62),
          ("db-1", 63),
          ("db-0dot5", 64),
          ("db-0", 65),
          ("db0dot5", 66),
          ("db1", 67),
          ("db1dot5", 68),
          ("db2", 69),
          ("db2dot5", 70),
          ("db3", 71))
    )


_Mc2200_GEMCAPSWAN2Threshold_Type.__name__ = "Integer32"
_Mc2200_GEMCAPSWAN2Threshold_Object = MibTableColumn
mc2200_GEMCAPSWAN2Threshold = _Mc2200_GEMCAPSWAN2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 68),
    _Mc2200_GEMCAPSWAN2Threshold_Type()
)
mc2200_GEMCAPSWAN2Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSWAN2Threshold.setStatus("current")


class _Mc2200_GEMCAPSTrapFilterLocalLAN_Type(Integer32):
    """Custom type mc2200_GEMCAPSTrapFilterLocalLAN based on Integer32"""
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


_Mc2200_GEMCAPSTrapFilterLocalLAN_Type.__name__ = "Integer32"
_Mc2200_GEMCAPSTrapFilterLocalLAN_Object = MibTableColumn
mc2200_GEMCAPSTrapFilterLocalLAN = _Mc2200_GEMCAPSTrapFilterLocalLAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 69),
    _Mc2200_GEMCAPSTrapFilterLocalLAN_Type()
)
mc2200_GEMCAPSTrapFilterLocalLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSTrapFilterLocalLAN.setStatus("current")


class _Mc2200_GEMCAPSTrapFilterLocalWAN_Type(Integer32):
    """Custom type mc2200_GEMCAPSTrapFilterLocalWAN based on Integer32"""
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


_Mc2200_GEMCAPSTrapFilterLocalWAN_Type.__name__ = "Integer32"
_Mc2200_GEMCAPSTrapFilterLocalWAN_Object = MibTableColumn
mc2200_GEMCAPSTrapFilterLocalWAN = _Mc2200_GEMCAPSTrapFilterLocalWAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 70),
    _Mc2200_GEMCAPSTrapFilterLocalWAN_Type()
)
mc2200_GEMCAPSTrapFilterLocalWAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSTrapFilterLocalWAN.setStatus("current")


class _Mc2200_GEMCAPSTrapFilterRemotePower_Type(Integer32):
    """Custom type mc2200_GEMCAPSTrapFilterRemotePower based on Integer32"""
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


_Mc2200_GEMCAPSTrapFilterRemotePower_Type.__name__ = "Integer32"
_Mc2200_GEMCAPSTrapFilterRemotePower_Object = MibTableColumn
mc2200_GEMCAPSTrapFilterRemotePower = _Mc2200_GEMCAPSTrapFilterRemotePower_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 71),
    _Mc2200_GEMCAPSTrapFilterRemotePower_Type()
)
mc2200_GEMCAPSTrapFilterRemotePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSTrapFilterRemotePower.setStatus("current")


class _Mc2200_GEMCAPSTrapFilterRemoteLAN_Type(Integer32):
    """Custom type mc2200_GEMCAPSTrapFilterRemoteLAN based on Integer32"""
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


_Mc2200_GEMCAPSTrapFilterRemoteLAN_Type.__name__ = "Integer32"
_Mc2200_GEMCAPSTrapFilterRemoteLAN_Object = MibTableColumn
mc2200_GEMCAPSTrapFilterRemoteLAN = _Mc2200_GEMCAPSTrapFilterRemoteLAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 72),
    _Mc2200_GEMCAPSTrapFilterRemoteLAN_Type()
)
mc2200_GEMCAPSTrapFilterRemoteLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSTrapFilterRemoteLAN.setStatus("current")


class _Mc2200_GEMCAPSTrapFilterRemoteWAN_Type(Integer32):
    """Custom type mc2200_GEMCAPSTrapFilterRemoteWAN based on Integer32"""
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


_Mc2200_GEMCAPSTrapFilterRemoteWAN_Type.__name__ = "Integer32"
_Mc2200_GEMCAPSTrapFilterRemoteWAN_Object = MibTableColumn
mc2200_GEMCAPSTrapFilterRemoteWAN = _Mc2200_GEMCAPSTrapFilterRemoteWAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 73),
    _Mc2200_GEMCAPSTrapFilterRemoteWAN_Type()
)
mc2200_GEMCAPSTrapFilterRemoteWAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSTrapFilterRemoteWAN.setStatus("current")


class _Mc2200_GEMCAPSLoopback_Type(Integer32):
    """Custom type mc2200_GEMCAPSLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("local_lanouter", 2),
          ("local_laninner", 3),
          ("local_wanouter", 4),
          ("local_waninner", 5),
          ("remote_lanouter", 6),
          ("remote_laninner", 7))
    )


_Mc2200_GEMCAPSLoopback_Type.__name__ = "Integer32"
_Mc2200_GEMCAPSLoopback_Object = MibTableColumn
mc2200_GEMCAPSLoopback = _Mc2200_GEMCAPSLoopback_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 74),
    _Mc2200_GEMCAPSLoopback_Type()
)
mc2200_GEMCAPSLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSLoopback.setStatus("mandatory")
_Mc2200_GEMCAPSCardType_Type = DisplayString
_Mc2200_GEMCAPSCardType_Object = MibTableColumn
mc2200_GEMCAPSCardType = _Mc2200_GEMCAPSCardType_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 15, 1, 75),
    _Mc2200_GEMCAPSCardType_Type()
)
mc2200_GEMCAPSCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GEMCAPSCardType.setStatus("current")
_Mc2200_OAPSTable_Object = MibTable
mc2200_OAPSTable = _Mc2200_OAPSTable_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 16)
)
if mibBuilder.loadTexts:
    mc2200_OAPSTable.setStatus("current")
_Mc2200_OAPSEntry_Object = MibTableRow
mc2200_OAPSEntry = _Mc2200_OAPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 16, 1)
)
mc2200_OAPSEntry.setIndexNames(
    (0, "OnAccess2200-MIB", "mc2200-OAPSCardIndex"),
)
if mibBuilder.loadTexts:
    mc2200_OAPSEntry.setStatus("current")


class _Mc2200_OAPSCardIndex_Type(Integer32):
    """Custom type mc2200_OAPSCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("card01", 1),
          ("card02", 2),
          ("card03", 3),
          ("card04", 4),
          ("card05", 5),
          ("card06", 6),
          ("card07", 7),
          ("card08", 8),
          ("card09", 9),
          ("card10", 10),
          ("card11", 11),
          ("card12", 12),
          ("card13", 13),
          ("card14", 14),
          ("card15", 15))
    )


_Mc2200_OAPSCardIndex_Type.__name__ = "Integer32"
_Mc2200_OAPSCardIndex_Object = MibTableColumn
mc2200_OAPSCardIndex = _Mc2200_OAPSCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 16, 1, 1),
    _Mc2200_OAPSCardIndex_Type()
)
mc2200_OAPSCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_OAPSCardIndex.setStatus("current")


class _Mc2200_OAPSLocalLANLink_Type(Integer32):
    """Custom type mc2200_OAPSLocalLANLink based on Integer32"""
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


_Mc2200_OAPSLocalLANLink_Type.__name__ = "Integer32"
_Mc2200_OAPSLocalLANLink_Object = MibTableColumn
mc2200_OAPSLocalLANLink = _Mc2200_OAPSLocalLANLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 16, 1, 2),
    _Mc2200_OAPSLocalLANLink_Type()
)
mc2200_OAPSLocalLANLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_OAPSLocalLANLink.setStatus("mandatory")
_Mc2200_OAPSLocalLANPower_Type = DisplayString
_Mc2200_OAPSLocalLANPower_Object = MibTableColumn
mc2200_OAPSLocalLANPower = _Mc2200_OAPSLocalLANPower_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 16, 1, 3),
    _Mc2200_OAPSLocalLANPower_Type()
)
mc2200_OAPSLocalLANPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_OAPSLocalLANPower.setStatus("mandatory")


class _Mc2200_OAPSLocalLANThreshold_Type(Integer32):
    """Custom type mc2200_OAPSLocalLANThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71)
        )
    )
    namedValues = NamedValues(
        *(("db-32", 1),
          ("db-31dot5", 2),
          ("db-31", 3),
          ("db-30dot5", 4),
          ("db-30", 5),
          ("db-29dot5", 6),
          ("db-29", 7),
          ("db-28dot5", 8),
          ("db-28", 9),
          ("db-27dot5", 10),
          ("db-27", 11),
          ("db-26dot5", 12),
          ("db-26", 13),
          ("db-25dot5", 14),
          ("db-25", 15),
          ("db-24dot5", 16),
          ("db-24", 17),
          ("db-23dot5", 18),
          ("db-23", 19),
          ("db-22dot5", 20),
          ("db-22", 21),
          ("db-21dot5", 22),
          ("db-21", 23),
          ("db-20dot5", 24),
          ("db-20", 25),
          ("db-19dot5", 26),
          ("db-19", 27),
          ("db-18dot5", 28),
          ("db-18", 29),
          ("db-17dot5", 30),
          ("db-17", 31),
          ("db-16dot5", 32),
          ("db-16", 33),
          ("db-15dot5", 34),
          ("db-15", 35),
          ("db-14dot5", 36),
          ("db-14", 37),
          ("db-13dot5", 38),
          ("db-13", 39),
          ("db-12dot5", 40),
          ("db-12", 41),
          ("db-11dot5", 42),
          ("db-11", 43),
          ("db-10dot5", 44),
          ("db-10", 45),
          ("db-9dot5", 46),
          ("db-9", 47),
          ("db-8dot5", 48),
          ("db-8", 49),
          ("db-7dot5", 50),
          ("db-7", 51),
          ("db-6dot5", 52),
          ("db-6", 53),
          ("db-5dot5", 54),
          ("db-5", 55),
          ("db-4dot5", 56),
          ("db-4", 57),
          ("db-3dot5", 58),
          ("db-3", 59),
          ("db-2dot5", 60),
          ("db-2", 61),
          ("db-1dot5", 62),
          ("db-1", 63),
          ("db-0dot5", 64),
          ("db-0", 65),
          ("db0dot5", 66),
          ("db1", 67),
          ("db1dot5", 68),
          ("db2", 69),
          ("db2dot5", 70),
          ("db3", 71))
    )


_Mc2200_OAPSLocalLANThreshold_Type.__name__ = "Integer32"
_Mc2200_OAPSLocalLANThreshold_Object = MibTableColumn
mc2200_OAPSLocalLANThreshold = _Mc2200_OAPSLocalLANThreshold_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 16, 1, 4),
    _Mc2200_OAPSLocalLANThreshold_Type()
)
mc2200_OAPSLocalLANThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_OAPSLocalLANThreshold.setStatus("mandatory")


class _Mc2200_OAPSLocalWAN1Link_Type(Integer32):
    """Custom type mc2200_OAPSLocalWAN1Link based on Integer32"""
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
          ("active", 3),
          ("standby", 4))
    )


_Mc2200_OAPSLocalWAN1Link_Type.__name__ = "Integer32"
_Mc2200_OAPSLocalWAN1Link_Object = MibTableColumn
mc2200_OAPSLocalWAN1Link = _Mc2200_OAPSLocalWAN1Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 16, 1, 5),
    _Mc2200_OAPSLocalWAN1Link_Type()
)
mc2200_OAPSLocalWAN1Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_OAPSLocalWAN1Link.setStatus("mandatory")
_Mc2200_OAPSLocalWAN1Power_Type = DisplayString
_Mc2200_OAPSLocalWAN1Power_Object = MibTableColumn
mc2200_OAPSLocalWAN1Power = _Mc2200_OAPSLocalWAN1Power_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 16, 1, 6),
    _Mc2200_OAPSLocalWAN1Power_Type()
)
mc2200_OAPSLocalWAN1Power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_OAPSLocalWAN1Power.setStatus("mandatory")


class _Mc2200_OAPSLocalWAN1Threshold_Type(Integer32):
    """Custom type mc2200_OAPSLocalWAN1Threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71)
        )
    )
    namedValues = NamedValues(
        *(("db-32", 1),
          ("db-31dot5", 2),
          ("db-31", 3),
          ("db-30dot5", 4),
          ("db-30", 5),
          ("db-29dot5", 6),
          ("db-29", 7),
          ("db-28dot5", 8),
          ("db-28", 9),
          ("db-27dot5", 10),
          ("db-27", 11),
          ("db-26dot5", 12),
          ("db-26", 13),
          ("db-25dot5", 14),
          ("db-25", 15),
          ("db-24dot5", 16),
          ("db-24", 17),
          ("db-23dot5", 18),
          ("db-23", 19),
          ("db-22dot5", 20),
          ("db-22", 21),
          ("db-21dot5", 22),
          ("db-21", 23),
          ("db-20dot5", 24),
          ("db-20", 25),
          ("db-19dot5", 26),
          ("db-19", 27),
          ("db-18dot5", 28),
          ("db-18", 29),
          ("db-17dot5", 30),
          ("db-17", 31),
          ("db-16dot5", 32),
          ("db-16", 33),
          ("db-15dot5", 34),
          ("db-15", 35),
          ("db-14dot5", 36),
          ("db-14", 37),
          ("db-13dot5", 38),
          ("db-13", 39),
          ("db-12dot5", 40),
          ("db-12", 41),
          ("db-11dot5", 42),
          ("db-11", 43),
          ("db-10dot5", 44),
          ("db-10", 45),
          ("db-9dot5", 46),
          ("db-9", 47),
          ("db-8dot5", 48),
          ("db-8", 49),
          ("db-7dot5", 50),
          ("db-7", 51),
          ("db-6dot5", 52),
          ("db-6", 53),
          ("db-5dot5", 54),
          ("db-5", 55),
          ("db-4dot5", 56),
          ("db-4", 57),
          ("db-3dot5", 58),
          ("db-3", 59),
          ("db-2dot5", 60),
          ("db-2", 61),
          ("db-1dot5", 62),
          ("db-1", 63),
          ("db-0dot5", 64),
          ("db-0", 65),
          ("db0dot5", 66),
          ("db1", 67),
          ("db1dot5", 68),
          ("db2", 69),
          ("db2dot5", 70),
          ("db3", 71))
    )


_Mc2200_OAPSLocalWAN1Threshold_Type.__name__ = "Integer32"
_Mc2200_OAPSLocalWAN1Threshold_Object = MibTableColumn
mc2200_OAPSLocalWAN1Threshold = _Mc2200_OAPSLocalWAN1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 16, 1, 7),
    _Mc2200_OAPSLocalWAN1Threshold_Type()
)
mc2200_OAPSLocalWAN1Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_OAPSLocalWAN1Threshold.setStatus("mandatory")


class _Mc2200_OAPSLocalWAN2Link_Type(Integer32):
    """Custom type mc2200_OAPSLocalWAN2Link based on Integer32"""
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
          ("active", 3),
          ("standby", 4))
    )


_Mc2200_OAPSLocalWAN2Link_Type.__name__ = "Integer32"
_Mc2200_OAPSLocalWAN2Link_Object = MibTableColumn
mc2200_OAPSLocalWAN2Link = _Mc2200_OAPSLocalWAN2Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 16, 1, 8),
    _Mc2200_OAPSLocalWAN2Link_Type()
)
mc2200_OAPSLocalWAN2Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_OAPSLocalWAN2Link.setStatus("mandatory")
_Mc2200_OAPSLocalWAN2Power_Type = DisplayString
_Mc2200_OAPSLocalWAN2Power_Object = MibTableColumn
mc2200_OAPSLocalWAN2Power = _Mc2200_OAPSLocalWAN2Power_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 16, 1, 9),
    _Mc2200_OAPSLocalWAN2Power_Type()
)
mc2200_OAPSLocalWAN2Power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_OAPSLocalWAN2Power.setStatus("mandatory")


class _Mc2200_OAPSLocalWAN2Threshold_Type(Integer32):
    """Custom type mc2200_OAPSLocalWAN2Threshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71)
        )
    )
    namedValues = NamedValues(
        *(("db-32", 1),
          ("db-31dot5", 2),
          ("db-31", 3),
          ("db-30dot5", 4),
          ("db-30", 5),
          ("db-29dot5", 6),
          ("db-29", 7),
          ("db-28dot5", 8),
          ("db-28", 9),
          ("db-27dot5", 10),
          ("db-27", 11),
          ("db-26dot5", 12),
          ("db-26", 13),
          ("db-25dot5", 14),
          ("db-25", 15),
          ("db-24dot5", 16),
          ("db-24", 17),
          ("db-23dot5", 18),
          ("db-23", 19),
          ("db-22dot5", 20),
          ("db-22", 21),
          ("db-21dot5", 22),
          ("db-21", 23),
          ("db-20dot5", 24),
          ("db-20", 25),
          ("db-19dot5", 26),
          ("db-19", 27),
          ("db-18dot5", 28),
          ("db-18", 29),
          ("db-17dot5", 30),
          ("db-17", 31),
          ("db-16dot5", 32),
          ("db-16", 33),
          ("db-15dot5", 34),
          ("db-15", 35),
          ("db-14dot5", 36),
          ("db-14", 37),
          ("db-13dot5", 38),
          ("db-13", 39),
          ("db-12dot5", 40),
          ("db-12", 41),
          ("db-11dot5", 42),
          ("db-11", 43),
          ("db-10dot5", 44),
          ("db-10", 45),
          ("db-9dot5", 46),
          ("db-9", 47),
          ("db-8dot5", 48),
          ("db-8", 49),
          ("db-7dot5", 50),
          ("db-7", 51),
          ("db-6dot5", 52),
          ("db-6", 53),
          ("db-5dot5", 54),
          ("db-5", 55),
          ("db-4dot5", 56),
          ("db-4", 57),
          ("db-3dot5", 58),
          ("db-3", 59),
          ("db-2dot5", 60),
          ("db-2", 61),
          ("db-1dot5", 62),
          ("db-1", 63),
          ("db-0dot5", 64),
          ("db-0", 65),
          ("db0dot5", 66),
          ("db1", 67),
          ("db1dot5", 68),
          ("db2", 69),
          ("db2dot5", 70),
          ("db3", 71))
    )


_Mc2200_OAPSLocalWAN2Threshold_Type.__name__ = "Integer32"
_Mc2200_OAPSLocalWAN2Threshold_Object = MibTableColumn
mc2200_OAPSLocalWAN2Threshold = _Mc2200_OAPSLocalWAN2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 16, 1, 10),
    _Mc2200_OAPSLocalWAN2Threshold_Type()
)
mc2200_OAPSLocalWAN2Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_OAPSLocalWAN2Threshold.setStatus("mandatory")


class _Mc2200_OAPSLocalActivePort_Type(Integer32):
    """Custom type mc2200_OAPSLocalActivePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wan1", 1),
          ("wan2", 2))
    )


_Mc2200_OAPSLocalActivePort_Type.__name__ = "Integer32"
_Mc2200_OAPSLocalActivePort_Object = MibTableColumn
mc2200_OAPSLocalActivePort = _Mc2200_OAPSLocalActivePort_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 16, 1, 11),
    _Mc2200_OAPSLocalActivePort_Type()
)
mc2200_OAPSLocalActivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_OAPSLocalActivePort.setStatus("current")


class _Mc2200_OAPSRevertive_Type(Integer32):
    """Custom type mc2200_OAPSRevertive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("revertive", 1),
          ("norevertive", 2))
    )


_Mc2200_OAPSRevertive_Type.__name__ = "Integer32"
_Mc2200_OAPSRevertive_Object = MibTableColumn
mc2200_OAPSRevertive = _Mc2200_OAPSRevertive_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 16, 1, 12),
    _Mc2200_OAPSRevertive_Type()
)
mc2200_OAPSRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_OAPSRevertive.setStatus("current")
_Mc2200_OAPSDefault_Type = Integer32
_Mc2200_OAPSDefault_Object = MibTableColumn
mc2200_OAPSDefault = _Mc2200_OAPSDefault_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 16, 1, 13),
    _Mc2200_OAPSDefault_Type()
)
mc2200_OAPSDefault.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mc2200_OAPSDefault.setStatus("current")
_Mc2200_OAPSReboot_Type = Integer32
_Mc2200_OAPSReboot_Object = MibTableColumn
mc2200_OAPSReboot = _Mc2200_OAPSReboot_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 16, 1, 14),
    _Mc2200_OAPSReboot_Type()
)
mc2200_OAPSReboot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mc2200_OAPSReboot.setStatus("current")
_Mc2200_OAPSLocalportuser_Type = DisplayString
_Mc2200_OAPSLocalportuser_Object = MibTableColumn
mc2200_OAPSLocalportuser = _Mc2200_OAPSLocalportuser_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 16, 1, 15),
    _Mc2200_OAPSLocalportuser_Type()
)
mc2200_OAPSLocalportuser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_OAPSLocalportuser.setStatus("current")
_Mc2200_OAPSRemoteportuser_Type = DisplayString
_Mc2200_OAPSRemoteportuser_Object = MibTableColumn
mc2200_OAPSRemoteportuser = _Mc2200_OAPSRemoteportuser_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 16, 1, 16),
    _Mc2200_OAPSRemoteportuser_Type()
)
mc2200_OAPSRemoteportuser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_OAPSRemoteportuser.setStatus("current")
_Mc2200_OAPSUsingActiveport_Type = DisplayString
_Mc2200_OAPSUsingActiveport_Object = MibTableColumn
mc2200_OAPSUsingActiveport = _Mc2200_OAPSUsingActiveport_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 16, 1, 17),
    _Mc2200_OAPSUsingActiveport_Type()
)
mc2200_OAPSUsingActiveport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_OAPSUsingActiveport.setStatus("current")


class _Mc2200_OAPSTrapFilterLocalLAN_Type(Integer32):
    """Custom type mc2200_OAPSTrapFilterLocalLAN based on Integer32"""
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


_Mc2200_OAPSTrapFilterLocalLAN_Type.__name__ = "Integer32"
_Mc2200_OAPSTrapFilterLocalLAN_Object = MibTableColumn
mc2200_OAPSTrapFilterLocalLAN = _Mc2200_OAPSTrapFilterLocalLAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 16, 1, 18),
    _Mc2200_OAPSTrapFilterLocalLAN_Type()
)
mc2200_OAPSTrapFilterLocalLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_OAPSTrapFilterLocalLAN.setStatus("current")


class _Mc2200_OAPSTrapFilterLocalWAN_Type(Integer32):
    """Custom type mc2200_OAPSTrapFilterLocalWAN based on Integer32"""
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


_Mc2200_OAPSTrapFilterLocalWAN_Type.__name__ = "Integer32"
_Mc2200_OAPSTrapFilterLocalWAN_Object = MibTableColumn
mc2200_OAPSTrapFilterLocalWAN = _Mc2200_OAPSTrapFilterLocalWAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 16, 1, 19),
    _Mc2200_OAPSTrapFilterLocalWAN_Type()
)
mc2200_OAPSTrapFilterLocalWAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_OAPSTrapFilterLocalWAN.setStatus("current")
_Mc2200_QS2204Table_Object = MibTable
mc2200_QS2204Table = _Mc2200_QS2204Table_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17)
)
if mibBuilder.loadTexts:
    mc2200_QS2204Table.setStatus("current")
_Mc2200_QS2204Entry_Object = MibTableRow
mc2200_QS2204Entry = _Mc2200_QS2204Entry_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1)
)
mc2200_QS2204Entry.setIndexNames(
    (0, "OnAccess2200-MIB", "mc2200-QS2204CardIndex"),
)
if mibBuilder.loadTexts:
    mc2200_QS2204Entry.setStatus("current")


class _Mc2200_QS2204CardIndex_Type(Integer32):
    """Custom type mc2200_QS2204CardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("card01", 1),
          ("card02", 2),
          ("card03", 3),
          ("card04", 4),
          ("card05", 5),
          ("card06", 6),
          ("card07", 7),
          ("card08", 8),
          ("card09", 9),
          ("card10", 10),
          ("card11", 11),
          ("card12", 12),
          ("card13", 13),
          ("card14", 14),
          ("card15", 15))
    )


_Mc2200_QS2204CardIndex_Type.__name__ = "Integer32"
_Mc2200_QS2204CardIndex_Object = MibTableColumn
mc2200_QS2204CardIndex = _Mc2200_QS2204CardIndex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1, 1),
    _Mc2200_QS2204CardIndex_Type()
)
mc2200_QS2204CardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_QS2204CardIndex.setStatus("current")


class _Mc2200_QS2204LocalLAN1Link_Type(Integer32):
    """Custom type mc2200_QS2204LocalLAN1Link based on Integer32"""
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


_Mc2200_QS2204LocalLAN1Link_Type.__name__ = "Integer32"
_Mc2200_QS2204LocalLAN1Link_Object = MibTableColumn
mc2200_QS2204LocalLAN1Link = _Mc2200_QS2204LocalLAN1Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1, 2),
    _Mc2200_QS2204LocalLAN1Link_Type()
)
mc2200_QS2204LocalLAN1Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_QS2204LocalLAN1Link.setStatus("mandatory")


class _Mc2200_QS2204LocalLAN1TxStatus_Type(Integer32):
    """Custom type mc2200_QS2204LocalLAN1TxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Mc2200_QS2204LocalLAN1TxStatus_Type.__name__ = "Integer32"
_Mc2200_QS2204LocalLAN1TxStatus_Object = MibTableColumn
mc2200_QS2204LocalLAN1TxStatus = _Mc2200_QS2204LocalLAN1TxStatus_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1, 3),
    _Mc2200_QS2204LocalLAN1TxStatus_Type()
)
mc2200_QS2204LocalLAN1TxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_QS2204LocalLAN1TxStatus.setStatus("mandatory")
_Mc2200_QS2204LocalLAN1SFPInfo_Type = DisplayString
_Mc2200_QS2204LocalLAN1SFPInfo_Object = MibTableColumn
mc2200_QS2204LocalLAN1SFPInfo = _Mc2200_QS2204LocalLAN1SFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1, 4),
    _Mc2200_QS2204LocalLAN1SFPInfo_Type()
)
mc2200_QS2204LocalLAN1SFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_QS2204LocalLAN1SFPInfo.setStatus("mandatory")


class _Mc2200_QS2204LocalLAN1Loopback_Type(Integer32):
    """Custom type mc2200_QS2204LocalLAN1Loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Mc2200_QS2204LocalLAN1Loopback_Type.__name__ = "Integer32"
_Mc2200_QS2204LocalLAN1Loopback_Object = MibTableColumn
mc2200_QS2204LocalLAN1Loopback = _Mc2200_QS2204LocalLAN1Loopback_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1, 5),
    _Mc2200_QS2204LocalLAN1Loopback_Type()
)
mc2200_QS2204LocalLAN1Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_QS2204LocalLAN1Loopback.setStatus("mandatory")


class _Mc2200_QS2204LocalLAN2Link_Type(Integer32):
    """Custom type mc2200_QS2204LocalLAN2Link based on Integer32"""
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


_Mc2200_QS2204LocalLAN2Link_Type.__name__ = "Integer32"
_Mc2200_QS2204LocalLAN2Link_Object = MibTableColumn
mc2200_QS2204LocalLAN2Link = _Mc2200_QS2204LocalLAN2Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1, 6),
    _Mc2200_QS2204LocalLAN2Link_Type()
)
mc2200_QS2204LocalLAN2Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_QS2204LocalLAN2Link.setStatus("mandatory")


class _Mc2200_QS2204LocalLAN2TxStatus_Type(Integer32):
    """Custom type mc2200_QS2204LocalLAN2TxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Mc2200_QS2204LocalLAN2TxStatus_Type.__name__ = "Integer32"
_Mc2200_QS2204LocalLAN2TxStatus_Object = MibTableColumn
mc2200_QS2204LocalLAN2TxStatus = _Mc2200_QS2204LocalLAN2TxStatus_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1, 7),
    _Mc2200_QS2204LocalLAN2TxStatus_Type()
)
mc2200_QS2204LocalLAN2TxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_QS2204LocalLAN2TxStatus.setStatus("mandatory")
_Mc2200_QS2204LocalLAN2SFPInfo_Type = DisplayString
_Mc2200_QS2204LocalLAN2SFPInfo_Object = MibTableColumn
mc2200_QS2204LocalLAN2SFPInfo = _Mc2200_QS2204LocalLAN2SFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1, 8),
    _Mc2200_QS2204LocalLAN2SFPInfo_Type()
)
mc2200_QS2204LocalLAN2SFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_QS2204LocalLAN2SFPInfo.setStatus("mandatory")


class _Mc2200_QS2204LocalLAN2Loopback_Type(Integer32):
    """Custom type mc2200_QS2204LocalLAN2Loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Mc2200_QS2204LocalLAN2Loopback_Type.__name__ = "Integer32"
_Mc2200_QS2204LocalLAN2Loopback_Object = MibTableColumn
mc2200_QS2204LocalLAN2Loopback = _Mc2200_QS2204LocalLAN2Loopback_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1, 9),
    _Mc2200_QS2204LocalLAN2Loopback_Type()
)
mc2200_QS2204LocalLAN2Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_QS2204LocalLAN2Loopback.setStatus("mandatory")


class _Mc2200_QS2204LocalLAN3Link_Type(Integer32):
    """Custom type mc2200_QS2204LocalLAN3Link based on Integer32"""
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


_Mc2200_QS2204LocalLAN3Link_Type.__name__ = "Integer32"
_Mc2200_QS2204LocalLAN3Link_Object = MibTableColumn
mc2200_QS2204LocalLAN3Link = _Mc2200_QS2204LocalLAN3Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1, 10),
    _Mc2200_QS2204LocalLAN3Link_Type()
)
mc2200_QS2204LocalLAN3Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_QS2204LocalLAN3Link.setStatus("mandatory")


class _Mc2200_QS2204LocalLAN3TxStatus_Type(Integer32):
    """Custom type mc2200_QS2204LocalLAN3TxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Mc2200_QS2204LocalLAN3TxStatus_Type.__name__ = "Integer32"
_Mc2200_QS2204LocalLAN3TxStatus_Object = MibTableColumn
mc2200_QS2204LocalLAN3TxStatus = _Mc2200_QS2204LocalLAN3TxStatus_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1, 11),
    _Mc2200_QS2204LocalLAN3TxStatus_Type()
)
mc2200_QS2204LocalLAN3TxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_QS2204LocalLAN3TxStatus.setStatus("mandatory")
_Mc2200_QS2204LocalLAN3SFPInfo_Type = DisplayString
_Mc2200_QS2204LocalLAN3SFPInfo_Object = MibTableColumn
mc2200_QS2204LocalLAN3SFPInfo = _Mc2200_QS2204LocalLAN3SFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1, 12),
    _Mc2200_QS2204LocalLAN3SFPInfo_Type()
)
mc2200_QS2204LocalLAN3SFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_QS2204LocalLAN3SFPInfo.setStatus("mandatory")


class _Mc2200_QS2204LocalLAN3Loopback_Type(Integer32):
    """Custom type mc2200_QS2204LocalLAN3Loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Mc2200_QS2204LocalLAN3Loopback_Type.__name__ = "Integer32"
_Mc2200_QS2204LocalLAN3Loopback_Object = MibTableColumn
mc2200_QS2204LocalLAN3Loopback = _Mc2200_QS2204LocalLAN3Loopback_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1, 13),
    _Mc2200_QS2204LocalLAN3Loopback_Type()
)
mc2200_QS2204LocalLAN3Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_QS2204LocalLAN3Loopback.setStatus("mandatory")


class _Mc2200_QS2204LocalLAN4Link_Type(Integer32):
    """Custom type mc2200_QS2204LocalLAN4Link based on Integer32"""
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


_Mc2200_QS2204LocalLAN4Link_Type.__name__ = "Integer32"
_Mc2200_QS2204LocalLAN4Link_Object = MibTableColumn
mc2200_QS2204LocalLAN4Link = _Mc2200_QS2204LocalLAN4Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1, 14),
    _Mc2200_QS2204LocalLAN4Link_Type()
)
mc2200_QS2204LocalLAN4Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_QS2204LocalLAN4Link.setStatus("mandatory")


class _Mc2200_QS2204LocalLAN4TxStatus_Type(Integer32):
    """Custom type mc2200_QS2204LocalLAN4TxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_Mc2200_QS2204LocalLAN4TxStatus_Type.__name__ = "Integer32"
_Mc2200_QS2204LocalLAN4TxStatus_Object = MibTableColumn
mc2200_QS2204LocalLAN4TxStatus = _Mc2200_QS2204LocalLAN4TxStatus_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1, 15),
    _Mc2200_QS2204LocalLAN4TxStatus_Type()
)
mc2200_QS2204LocalLAN4TxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_QS2204LocalLAN4TxStatus.setStatus("mandatory")
_Mc2200_QS2204LocalLAN4SFPInfo_Type = DisplayString
_Mc2200_QS2204LocalLAN4SFPInfo_Object = MibTableColumn
mc2200_QS2204LocalLAN4SFPInfo = _Mc2200_QS2204LocalLAN4SFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1, 16),
    _Mc2200_QS2204LocalLAN4SFPInfo_Type()
)
mc2200_QS2204LocalLAN4SFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_QS2204LocalLAN4SFPInfo.setStatus("mandatory")


class _Mc2200_QS2204LocalLAN4Loopback_Type(Integer32):
    """Custom type mc2200_QS2204LocalLAN4Loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Mc2200_QS2204LocalLAN4Loopback_Type.__name__ = "Integer32"
_Mc2200_QS2204LocalLAN4Loopback_Object = MibTableColumn
mc2200_QS2204LocalLAN4Loopback = _Mc2200_QS2204LocalLAN4Loopback_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1, 17),
    _Mc2200_QS2204LocalLAN4Loopback_Type()
)
mc2200_QS2204LocalLAN4Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_QS2204LocalLAN4Loopback.setStatus("mandatory")
_Mc2200_QS2204LocalWANLink_Type = DisplayString
_Mc2200_QS2204LocalWANLink_Object = MibTableColumn
mc2200_QS2204LocalWANLink = _Mc2200_QS2204LocalWANLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1, 18),
    _Mc2200_QS2204LocalWANLink_Type()
)
mc2200_QS2204LocalWANLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_QS2204LocalWANLink.setStatus("mandatory")
_Mc2200_QS2204LocalWANTxStatus_Type = DisplayString
_Mc2200_QS2204LocalWANTxStatus_Object = MibTableColumn
mc2200_QS2204LocalWANTxStatus = _Mc2200_QS2204LocalWANTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1, 19),
    _Mc2200_QS2204LocalWANTxStatus_Type()
)
mc2200_QS2204LocalWANTxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_QS2204LocalWANTxStatus.setStatus("mandatory")
_Mc2200_QS2204LocalWANSFPInfo_Type = DisplayString
_Mc2200_QS2204LocalWANSFPInfo_Object = MibTableColumn
mc2200_QS2204LocalWANSFPInfo = _Mc2200_QS2204LocalWANSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1, 20),
    _Mc2200_QS2204LocalWANSFPInfo_Type()
)
mc2200_QS2204LocalWANSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_QS2204LocalWANSFPInfo.setStatus("mandatory")


class _Mc2200_QS2204LocalWANLoopback_Type(Integer32):
    """Custom type mc2200_QS2204LocalWANLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Mc2200_QS2204LocalWANLoopback_Type.__name__ = "Integer32"
_Mc2200_QS2204LocalWANLoopback_Object = MibTableColumn
mc2200_QS2204LocalWANLoopback = _Mc2200_QS2204LocalWANLoopback_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1, 21),
    _Mc2200_QS2204LocalWANLoopback_Type()
)
mc2200_QS2204LocalWANLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_QS2204LocalWANLoopback.setStatus("mandatory")


class _Mc2200_QS2204RFD_Type(Integer32):
    """Custom type mc2200_QS2204RFD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Mc2200_QS2204RFD_Type.__name__ = "Integer32"
_Mc2200_QS2204RFD_Object = MibTableColumn
mc2200_QS2204RFD = _Mc2200_QS2204RFD_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1, 22),
    _Mc2200_QS2204RFD_Type()
)
mc2200_QS2204RFD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_QS2204RFD.setStatus("current")
_Mc2200_QS2204Default_Type = Integer32
_Mc2200_QS2204Default_Object = MibTableColumn
mc2200_QS2204Default = _Mc2200_QS2204Default_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1, 23),
    _Mc2200_QS2204Default_Type()
)
mc2200_QS2204Default.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mc2200_QS2204Default.setStatus("current")
_Mc2200_QS2204Reboot_Type = Integer32
_Mc2200_QS2204Reboot_Object = MibTableColumn
mc2200_QS2204Reboot = _Mc2200_QS2204Reboot_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1, 24),
    _Mc2200_QS2204Reboot_Type()
)
mc2200_QS2204Reboot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mc2200_QS2204Reboot.setStatus("current")
_Mc2200_QS2204LocalLAN1user_Type = DisplayString
_Mc2200_QS2204LocalLAN1user_Object = MibTableColumn
mc2200_QS2204LocalLAN1user = _Mc2200_QS2204LocalLAN1user_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1, 25),
    _Mc2200_QS2204LocalLAN1user_Type()
)
mc2200_QS2204LocalLAN1user.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_QS2204LocalLAN1user.setStatus("current")
_Mc2200_QS2204LocalLAN2user_Type = DisplayString
_Mc2200_QS2204LocalLAN2user_Object = MibTableColumn
mc2200_QS2204LocalLAN2user = _Mc2200_QS2204LocalLAN2user_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1, 26),
    _Mc2200_QS2204LocalLAN2user_Type()
)
mc2200_QS2204LocalLAN2user.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_QS2204LocalLAN2user.setStatus("current")
_Mc2200_QS2204LocalLAN3user_Type = DisplayString
_Mc2200_QS2204LocalLAN3user_Object = MibTableColumn
mc2200_QS2204LocalLAN3user = _Mc2200_QS2204LocalLAN3user_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1, 27),
    _Mc2200_QS2204LocalLAN3user_Type()
)
mc2200_QS2204LocalLAN3user.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_QS2204LocalLAN3user.setStatus("current")
_Mc2200_QS2204LocalLAN4user_Type = DisplayString
_Mc2200_QS2204LocalLAN4user_Object = MibTableColumn
mc2200_QS2204LocalLAN4user = _Mc2200_QS2204LocalLAN4user_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 17, 1, 28),
    _Mc2200_QS2204LocalLAN4user_Type()
)
mc2200_QS2204LocalLAN4user.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_QS2204LocalLAN4user.setStatus("current")
_Mc2200_Q2202Table_Object = MibTable
mc2200_Q2202Table = _Mc2200_Q2202Table_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 18)
)
if mibBuilder.loadTexts:
    mc2200_Q2202Table.setStatus("current")
_Mc2200_Q2202Entry_Object = MibTableRow
mc2200_Q2202Entry = _Mc2200_Q2202Entry_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 18, 1)
)
mc2200_Q2202Entry.setIndexNames(
    (0, "OnAccess2200-MIB", "mc2200-Q2202CardIndex"),
)
if mibBuilder.loadTexts:
    mc2200_Q2202Entry.setStatus("current")


class _Mc2200_Q2202CardIndex_Type(Integer32):
    """Custom type mc2200_Q2202CardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("card01", 1),
          ("card02", 2),
          ("card03", 3),
          ("card04", 4),
          ("card05", 5),
          ("card06", 6),
          ("card07", 7),
          ("card08", 8),
          ("card09", 9),
          ("card10", 10),
          ("card11", 11),
          ("card12", 12),
          ("card13", 13),
          ("card14", 14),
          ("card15", 15))
    )


_Mc2200_Q2202CardIndex_Type.__name__ = "Integer32"
_Mc2200_Q2202CardIndex_Object = MibTableColumn
mc2200_Q2202CardIndex = _Mc2200_Q2202CardIndex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 18, 1, 1),
    _Mc2200_Q2202CardIndex_Type()
)
mc2200_Q2202CardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_Q2202CardIndex.setStatus("current")


class _Mc2200_Q2202LocalLANLink_Type(Integer32):
    """Custom type mc2200_Q2202LocalLANLink based on Integer32"""
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


_Mc2200_Q2202LocalLANLink_Type.__name__ = "Integer32"
_Mc2200_Q2202LocalLANLink_Object = MibTableColumn
mc2200_Q2202LocalLANLink = _Mc2200_Q2202LocalLANLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 18, 1, 2),
    _Mc2200_Q2202LocalLANLink_Type()
)
mc2200_Q2202LocalLANLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_Q2202LocalLANLink.setStatus("mandatory")
_Mc2200_Q2202LocalLANTxStatus_Type = DisplayString
_Mc2200_Q2202LocalLANTxStatus_Object = MibTableColumn
mc2200_Q2202LocalLANTxStatus = _Mc2200_Q2202LocalLANTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 18, 1, 3),
    _Mc2200_Q2202LocalLANTxStatus_Type()
)
mc2200_Q2202LocalLANTxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_Q2202LocalLANTxStatus.setStatus("mandatory")
_Mc2200_Q2202LocalLANSFPInfo_Type = DisplayString
_Mc2200_Q2202LocalLANSFPInfo_Object = MibTableColumn
mc2200_Q2202LocalLANSFPInfo = _Mc2200_Q2202LocalLANSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 18, 1, 4),
    _Mc2200_Q2202LocalLANSFPInfo_Type()
)
mc2200_Q2202LocalLANSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_Q2202LocalLANSFPInfo.setStatus("mandatory")


class _Mc2200_Q2202LocalWANLink_Type(Integer32):
    """Custom type mc2200_Q2202LocalWANLink based on Integer32"""
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


_Mc2200_Q2202LocalWANLink_Type.__name__ = "Integer32"
_Mc2200_Q2202LocalWANLink_Object = MibTableColumn
mc2200_Q2202LocalWANLink = _Mc2200_Q2202LocalWANLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 18, 1, 5),
    _Mc2200_Q2202LocalWANLink_Type()
)
mc2200_Q2202LocalWANLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_Q2202LocalWANLink.setStatus("mandatory")
_Mc2200_Q2202LocalWANTxStatus_Type = DisplayString
_Mc2200_Q2202LocalWANTxStatus_Object = MibTableColumn
mc2200_Q2202LocalWANTxStatus = _Mc2200_Q2202LocalWANTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 18, 1, 6),
    _Mc2200_Q2202LocalWANTxStatus_Type()
)
mc2200_Q2202LocalWANTxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_Q2202LocalWANTxStatus.setStatus("mandatory")
_Mc2200_Q2202LocalWANSFPInfo_Type = DisplayString
_Mc2200_Q2202LocalWANSFPInfo_Object = MibTableColumn
mc2200_Q2202LocalWANSFPInfo = _Mc2200_Q2202LocalWANSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 18, 1, 7),
    _Mc2200_Q2202LocalWANSFPInfo_Type()
)
mc2200_Q2202LocalWANSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_Q2202LocalWANSFPInfo.setStatus("mandatory")


class _Mc2200_Q2202Loopback_Type(Integer32):
    """Custom type mc2200_Q2202Loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Mc2200_Q2202Loopback_Type.__name__ = "Integer32"
_Mc2200_Q2202Loopback_Object = MibTableColumn
mc2200_Q2202Loopback = _Mc2200_Q2202Loopback_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 18, 1, 8),
    _Mc2200_Q2202Loopback_Type()
)
mc2200_Q2202Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_Q2202Loopback.setStatus("mandatory")


class _Mc2200_Q2202RFD_Type(Integer32):
    """Custom type mc2200_Q2202RFD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Mc2200_Q2202RFD_Type.__name__ = "Integer32"
_Mc2200_Q2202RFD_Object = MibTableColumn
mc2200_Q2202RFD = _Mc2200_Q2202RFD_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 18, 1, 9),
    _Mc2200_Q2202RFD_Type()
)
mc2200_Q2202RFD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_Q2202RFD.setStatus("current")
_Mc2200_Q2202Default_Type = Integer32
_Mc2200_Q2202Default_Object = MibTableColumn
mc2200_Q2202Default = _Mc2200_Q2202Default_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 18, 1, 10),
    _Mc2200_Q2202Default_Type()
)
mc2200_Q2202Default.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mc2200_Q2202Default.setStatus("current")
_Mc2200_Q2202Reboot_Type = Integer32
_Mc2200_Q2202Reboot_Object = MibTableColumn
mc2200_Q2202Reboot = _Mc2200_Q2202Reboot_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 18, 1, 11),
    _Mc2200_Q2202Reboot_Type()
)
mc2200_Q2202Reboot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mc2200_Q2202Reboot.setStatus("current")
_Mc2200_Q2202LocalLANuser_Type = DisplayString
_Mc2200_Q2202LocalLANuser_Object = MibTableColumn
mc2200_Q2202LocalLANuser = _Mc2200_Q2202LocalLANuser_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 18, 1, 12),
    _Mc2200_Q2202LocalLANuser_Type()
)
mc2200_Q2202LocalLANuser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_Q2202LocalLANuser.setStatus("current")


class _Mc2200_Q2202Rate_Type(Integer32):
    """Custom type mc2200_Q2202Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rate40G", 1),
          ("rate100G", 2))
    )


_Mc2200_Q2202Rate_Type.__name__ = "Integer32"
_Mc2200_Q2202Rate_Object = MibTableColumn
mc2200_Q2202Rate = _Mc2200_Q2202Rate_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 18, 1, 13),
    _Mc2200_Q2202Rate_Type()
)
mc2200_Q2202Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_Q2202Rate.setStatus("current")
_Mc2200_GESFP2Table_Object = MibTable
mc2200_GESFP2Table = _Mc2200_GESFP2Table_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19)
)
if mibBuilder.loadTexts:
    mc2200_GESFP2Table.setStatus("current")
_Mc2200_GESFP2Entry_Object = MibTableRow
mc2200_GESFP2Entry = _Mc2200_GESFP2Entry_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1)
)
mc2200_GESFP2Entry.setIndexNames(
    (0, "OnAccess2200-MIB", "mc2200-GESFP2CardIndex"),
)
if mibBuilder.loadTexts:
    mc2200_GESFP2Entry.setStatus("current")


class _Mc2200_GESFP2CardIndex_Type(Integer32):
    """Custom type mc2200_GESFP2CardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("card01", 1),
          ("card02", 2),
          ("card03", 3),
          ("card04", 4),
          ("card05", 5),
          ("card06", 6),
          ("card07", 7),
          ("card08", 8),
          ("card09", 9),
          ("card10", 10),
          ("card11", 11),
          ("card12", 12),
          ("card13", 13),
          ("card14", 14),
          ("card15", 15))
    )


_Mc2200_GESFP2CardIndex_Type.__name__ = "Integer32"
_Mc2200_GESFP2CardIndex_Object = MibTableColumn
mc2200_GESFP2CardIndex = _Mc2200_GESFP2CardIndex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 1),
    _Mc2200_GESFP2CardIndex_Type()
)
mc2200_GESFP2CardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2CardIndex.setStatus("current")


class _Mc2200_GESFP2LocalTXLink_Type(Integer32):
    """Custom type mc2200_GESFP2LocalTXLink based on Integer32"""
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


_Mc2200_GESFP2LocalTXLink_Type.__name__ = "Integer32"
_Mc2200_GESFP2LocalTXLink_Object = MibTableColumn
mc2200_GESFP2LocalTXLink = _Mc2200_GESFP2LocalTXLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 2),
    _Mc2200_GESFP2LocalTXLink_Type()
)
mc2200_GESFP2LocalTXLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2LocalTXLink.setStatus("mandatory")
_Mc2200_GESFP2LocalWANSFPInfo_Type = DisplayString
_Mc2200_GESFP2LocalWANSFPInfo_Object = MibTableColumn
mc2200_GESFP2LocalWANSFPInfo = _Mc2200_GESFP2LocalWANSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 3),
    _Mc2200_GESFP2LocalWANSFPInfo_Type()
)
mc2200_GESFP2LocalWANSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2LocalWANSFPInfo.setStatus("current")


class _Mc2200_GESFP2LocalWANLink_Type(Integer32):
    """Custom type mc2200_GESFP2LocalWANLink based on Integer32"""
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


_Mc2200_GESFP2LocalWANLink_Type.__name__ = "Integer32"
_Mc2200_GESFP2LocalWANLink_Object = MibTableColumn
mc2200_GESFP2LocalWANLink = _Mc2200_GESFP2LocalWANLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 4),
    _Mc2200_GESFP2LocalWANLink_Type()
)
mc2200_GESFP2LocalWANLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2LocalWANLink.setStatus("current")


class _Mc2200_GESFP2LocalTXMode_Type(Integer32):
    """Custom type mc2200_GESFP2LocalTXMode based on Integer32"""
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
        *(("auto-10-100-1000", 1),
          ("mode1000F", 2),
          ("mode100F", 3),
          ("mode10F", 4),
          ("mode100H", 5),
          ("mode10H", 6))
    )


_Mc2200_GESFP2LocalTXMode_Type.__name__ = "Integer32"
_Mc2200_GESFP2LocalTXMode_Object = MibTableColumn
mc2200_GESFP2LocalTXMode = _Mc2200_GESFP2LocalTXMode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 5),
    _Mc2200_GESFP2LocalTXMode_Type()
)
mc2200_GESFP2LocalTXMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2LocalTXMode.setStatus("current")


class _Mc2200_GESFP2LocalTXMDIX_Type(Integer32):
    """Custom type mc2200_GESFP2LocalTXMDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("mdi", 2),
          ("mdiX", 3))
    )


_Mc2200_GESFP2LocalTXMDIX_Type.__name__ = "Integer32"
_Mc2200_GESFP2LocalTXMDIX_Object = MibTableColumn
mc2200_GESFP2LocalTXMDIX = _Mc2200_GESFP2LocalTXMDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 6),
    _Mc2200_GESFP2LocalTXMDIX_Type()
)
mc2200_GESFP2LocalTXMDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2LocalTXMDIX.setStatus("current")
_Mc2200_GESFP2RxGoodOctets_Type = Counter64
_Mc2200_GESFP2RxGoodOctets_Object = MibTableColumn
mc2200_GESFP2RxGoodOctets = _Mc2200_GESFP2RxGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 7),
    _Mc2200_GESFP2RxGoodOctets_Type()
)
mc2200_GESFP2RxGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RxGoodOctets.setStatus("current")
_Mc2200_GESFP2RxBadOctets_Type = Counter64
_Mc2200_GESFP2RxBadOctets_Object = MibTableColumn
mc2200_GESFP2RxBadOctets = _Mc2200_GESFP2RxBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 8),
    _Mc2200_GESFP2RxBadOctets_Type()
)
mc2200_GESFP2RxBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RxBadOctets.setStatus("current")
_Mc2200_GESFP2TxFCSErr_Type = Counter64
_Mc2200_GESFP2TxFCSErr_Object = MibTableColumn
mc2200_GESFP2TxFCSErr = _Mc2200_GESFP2TxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 9),
    _Mc2200_GESFP2TxFCSErr_Type()
)
mc2200_GESFP2TxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2TxFCSErr.setStatus("current")
_Mc2200_GESFP2RxUnicast_Type = Counter64
_Mc2200_GESFP2RxUnicast_Object = MibTableColumn
mc2200_GESFP2RxUnicast = _Mc2200_GESFP2RxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 10),
    _Mc2200_GESFP2RxUnicast_Type()
)
mc2200_GESFP2RxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RxUnicast.setStatus("current")
_Mc2200_GESFP2TxDeferred_Type = Counter64
_Mc2200_GESFP2TxDeferred_Object = MibTableColumn
mc2200_GESFP2TxDeferred = _Mc2200_GESFP2TxDeferred_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 11),
    _Mc2200_GESFP2TxDeferred_Type()
)
mc2200_GESFP2TxDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2TxDeferred.setStatus("current")
_Mc2200_GESFP2RxBroadcasts_Type = Counter64
_Mc2200_GESFP2RxBroadcasts_Object = MibTableColumn
mc2200_GESFP2RxBroadcasts = _Mc2200_GESFP2RxBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 12),
    _Mc2200_GESFP2RxBroadcasts_Type()
)
mc2200_GESFP2RxBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RxBroadcasts.setStatus("current")
_Mc2200_GESFP2RxMulticasts_Type = Counter64
_Mc2200_GESFP2RxMulticasts_Object = MibTableColumn
mc2200_GESFP2RxMulticasts = _Mc2200_GESFP2RxMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 13),
    _Mc2200_GESFP2RxMulticasts_Type()
)
mc2200_GESFP2RxMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RxMulticasts.setStatus("current")
_Mc2200_GESFP2Rx64Octets_Type = Counter64
_Mc2200_GESFP2Rx64Octets_Object = MibTableColumn
mc2200_GESFP2Rx64Octets = _Mc2200_GESFP2Rx64Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 14),
    _Mc2200_GESFP2Rx64Octets_Type()
)
mc2200_GESFP2Rx64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2Rx64Octets.setStatus("current")
_Mc2200_GESFP2Rx65to127Octets_Type = Counter64
_Mc2200_GESFP2Rx65to127Octets_Object = MibTableColumn
mc2200_GESFP2Rx65to127Octets = _Mc2200_GESFP2Rx65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 15),
    _Mc2200_GESFP2Rx65to127Octets_Type()
)
mc2200_GESFP2Rx65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2Rx65to127Octets.setStatus("current")
_Mc2200_GESFP2Rx128to255Octets_Type = Counter64
_Mc2200_GESFP2Rx128to255Octets_Object = MibTableColumn
mc2200_GESFP2Rx128to255Octets = _Mc2200_GESFP2Rx128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 16),
    _Mc2200_GESFP2Rx128to255Octets_Type()
)
mc2200_GESFP2Rx128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2Rx128to255Octets.setStatus("current")
_Mc2200_GESFP2Rx256to511Octets_Type = Counter64
_Mc2200_GESFP2Rx256to511Octets_Object = MibTableColumn
mc2200_GESFP2Rx256to511Octets = _Mc2200_GESFP2Rx256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 17),
    _Mc2200_GESFP2Rx256to511Octets_Type()
)
mc2200_GESFP2Rx256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2Rx256to511Octets.setStatus("current")
_Mc2200_GESFP2Rx512to1023Octets_Type = Counter64
_Mc2200_GESFP2Rx512to1023Octets_Object = MibTableColumn
mc2200_GESFP2Rx512to1023Octets = _Mc2200_GESFP2Rx512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 18),
    _Mc2200_GESFP2Rx512to1023Octets_Type()
)
mc2200_GESFP2Rx512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2Rx512to1023Octets.setStatus("current")
_Mc2200_GESFP2Rx1024toMaxOctets_Type = Counter64
_Mc2200_GESFP2Rx1024toMaxOctets_Object = MibTableColumn
mc2200_GESFP2Rx1024toMaxOctets = _Mc2200_GESFP2Rx1024toMaxOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 19),
    _Mc2200_GESFP2Rx1024toMaxOctets_Type()
)
mc2200_GESFP2Rx1024toMaxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2Rx1024toMaxOctets.setStatus("current")
_Mc2200_GESFP2TxOctets_Type = Counter64
_Mc2200_GESFP2TxOctets_Object = MibTableColumn
mc2200_GESFP2TxOctets = _Mc2200_GESFP2TxOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 20),
    _Mc2200_GESFP2TxOctets_Type()
)
mc2200_GESFP2TxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2TxOctets.setStatus("current")
_Mc2200_GESFP2TxUnicast_Type = Counter64
_Mc2200_GESFP2TxUnicast_Object = MibTableColumn
mc2200_GESFP2TxUnicast = _Mc2200_GESFP2TxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 21),
    _Mc2200_GESFP2TxUnicast_Type()
)
mc2200_GESFP2TxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2TxUnicast.setStatus("current")
_Mc2200_GESFP2TxExcessive_Type = Counter64
_Mc2200_GESFP2TxExcessive_Object = MibTableColumn
mc2200_GESFP2TxExcessive = _Mc2200_GESFP2TxExcessive_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 22),
    _Mc2200_GESFP2TxExcessive_Type()
)
mc2200_GESFP2TxExcessive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2TxExcessive.setStatus("current")
_Mc2200_GESFP2TxMulticasts_Type = Counter64
_Mc2200_GESFP2TxMulticasts_Object = MibTableColumn
mc2200_GESFP2TxMulticasts = _Mc2200_GESFP2TxMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 23),
    _Mc2200_GESFP2TxMulticasts_Type()
)
mc2200_GESFP2TxMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2TxMulticasts.setStatus("current")
_Mc2200_GESFP2TxBroadcasts_Type = Counter64
_Mc2200_GESFP2TxBroadcasts_Object = MibTableColumn
mc2200_GESFP2TxBroadcasts = _Mc2200_GESFP2TxBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 24),
    _Mc2200_GESFP2TxBroadcasts_Type()
)
mc2200_GESFP2TxBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2TxBroadcasts.setStatus("current")
_Mc2200_GESFP2TxSingle_Type = Counter64
_Mc2200_GESFP2TxSingle_Object = MibTableColumn
mc2200_GESFP2TxSingle = _Mc2200_GESFP2TxSingle_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 25),
    _Mc2200_GESFP2TxSingle_Type()
)
mc2200_GESFP2TxSingle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2TxSingle.setStatus("current")
_Mc2200_GESFP2TxPause_Type = Counter64
_Mc2200_GESFP2TxPause_Object = MibTableColumn
mc2200_GESFP2TxPause = _Mc2200_GESFP2TxPause_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 26),
    _Mc2200_GESFP2TxPause_Type()
)
mc2200_GESFP2TxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2TxPause.setStatus("current")
_Mc2200_GESFP2RxPause_Type = Counter64
_Mc2200_GESFP2RxPause_Object = MibTableColumn
mc2200_GESFP2RxPause = _Mc2200_GESFP2RxPause_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 27),
    _Mc2200_GESFP2RxPause_Type()
)
mc2200_GESFP2RxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RxPause.setStatus("current")
_Mc2200_GESFP2TxMultiple_Type = Counter64
_Mc2200_GESFP2TxMultiple_Object = MibTableColumn
mc2200_GESFP2TxMultiple = _Mc2200_GESFP2TxMultiple_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 28),
    _Mc2200_GESFP2TxMultiple_Type()
)
mc2200_GESFP2TxMultiple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2TxMultiple.setStatus("current")
_Mc2200_GESFP2RxUndersize_Type = Counter64
_Mc2200_GESFP2RxUndersize_Object = MibTableColumn
mc2200_GESFP2RxUndersize = _Mc2200_GESFP2RxUndersize_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 29),
    _Mc2200_GESFP2RxUndersize_Type()
)
mc2200_GESFP2RxUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RxUndersize.setStatus("current")
_Mc2200_GESFP2RxFragments_Type = Counter64
_Mc2200_GESFP2RxFragments_Object = MibTableColumn
mc2200_GESFP2RxFragments = _Mc2200_GESFP2RxFragments_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 30),
    _Mc2200_GESFP2RxFragments_Type()
)
mc2200_GESFP2RxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RxFragments.setStatus("current")
_Mc2200_GESFP2RxOversize_Type = Counter64
_Mc2200_GESFP2RxOversize_Object = MibTableColumn
mc2200_GESFP2RxOversize = _Mc2200_GESFP2RxOversize_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 31),
    _Mc2200_GESFP2RxOversize_Type()
)
mc2200_GESFP2RxOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RxOversize.setStatus("current")
_Mc2200_GESFP2RxJabber_Type = Counter64
_Mc2200_GESFP2RxJabber_Object = MibTableColumn
mc2200_GESFP2RxJabber = _Mc2200_GESFP2RxJabber_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 32),
    _Mc2200_GESFP2RxJabber_Type()
)
mc2200_GESFP2RxJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RxJabber.setStatus("current")
_Mc2200_GESFP2RxErr_Type = Counter64
_Mc2200_GESFP2RxErr_Object = MibTableColumn
mc2200_GESFP2RxErr = _Mc2200_GESFP2RxErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 33),
    _Mc2200_GESFP2RxErr_Type()
)
mc2200_GESFP2RxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RxErr.setStatus("current")
_Mc2200_GESFP2RxFCSErr_Type = Counter64
_Mc2200_GESFP2RxFCSErr_Object = MibTableColumn
mc2200_GESFP2RxFCSErr = _Mc2200_GESFP2RxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 34),
    _Mc2200_GESFP2RxFCSErr_Type()
)
mc2200_GESFP2RxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RxFCSErr.setStatus("current")
_Mc2200_GESFP2TxCollisions_Type = Counter64
_Mc2200_GESFP2TxCollisions_Object = MibTableColumn
mc2200_GESFP2TxCollisions = _Mc2200_GESFP2TxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 35),
    _Mc2200_GESFP2TxCollisions_Type()
)
mc2200_GESFP2TxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2TxCollisions.setStatus("current")
_Mc2200_GESFP2TxLate_Type = Counter64
_Mc2200_GESFP2TxLate_Object = MibTableColumn
mc2200_GESFP2TxLate = _Mc2200_GESFP2TxLate_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 36),
    _Mc2200_GESFP2TxLate_Type()
)
mc2200_GESFP2TxLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2TxLate.setStatus("current")
_Mc2200_GESFP2RemoteWANSFPInfo_Type = DisplayString
_Mc2200_GESFP2RemoteWANSFPInfo_Object = MibTableColumn
mc2200_GESFP2RemoteWANSFPInfo = _Mc2200_GESFP2RemoteWANSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 37),
    _Mc2200_GESFP2RemoteWANSFPInfo_Type()
)
mc2200_GESFP2RemoteWANSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemoteWANSFPInfo.setStatus("current")


class _Mc2200_GESFP2RemoteWANLink_Type(Integer32):
    """Custom type mc2200_GESFP2RemoteWANLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_GESFP2RemoteWANLink_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemoteWANLink_Object = MibTableColumn
mc2200_GESFP2RemoteWANLink = _Mc2200_GESFP2RemoteWANLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 38),
    _Mc2200_GESFP2RemoteWANLink_Type()
)
mc2200_GESFP2RemoteWANLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemoteWANLink.setStatus("current")


class _Mc2200_GESFP2RemotePort1Link_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort1Link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_GESFP2RemotePort1Link_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort1Link_Object = MibTableColumn
mc2200_GESFP2RemotePort1Link = _Mc2200_GESFP2RemotePort1Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 39),
    _Mc2200_GESFP2RemotePort1Link_Type()
)
mc2200_GESFP2RemotePort1Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort1Link.setStatus("current")


class _Mc2200_GESFP2RemotePort1Speed_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort1Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("speed100M", 1),
          ("speed10M", 2),
          ("auto", 3))
    )


_Mc2200_GESFP2RemotePort1Speed_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort1Speed_Object = MibTableColumn
mc2200_GESFP2RemotePort1Speed = _Mc2200_GESFP2RemotePort1Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 40),
    _Mc2200_GESFP2RemotePort1Speed_Type()
)
mc2200_GESFP2RemotePort1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort1Speed.setStatus("current")


class _Mc2200_GESFP2RemotePort1Duplex_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort1Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_Mc2200_GESFP2RemotePort1Duplex_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort1Duplex_Object = MibTableColumn
mc2200_GESFP2RemotePort1Duplex = _Mc2200_GESFP2RemotePort1Duplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 41),
    _Mc2200_GESFP2RemotePort1Duplex_Type()
)
mc2200_GESFP2RemotePort1Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort1Duplex.setStatus("current")


class _Mc2200_GESFP2RemotePort1Mode_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort1Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mode10MHALFDUPLEX", 2),
          ("mode10MFULLDUPLEX", 3),
          ("mode100MHALFDUPLEX", 4),
          ("mode100MFULLDUPLEX", 5))
    )


_Mc2200_GESFP2RemotePort1Mode_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort1Mode_Object = MibTableColumn
mc2200_GESFP2RemotePort1Mode = _Mc2200_GESFP2RemotePort1Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 42),
    _Mc2200_GESFP2RemotePort1Mode_Type()
)
mc2200_GESFP2RemotePort1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort1Mode.setStatus("current")


class _Mc2200_GESFP2RemotePort1MDIX_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort1MDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mdi", 2),
          ("mdi-X", 3))
    )


_Mc2200_GESFP2RemotePort1MDIX_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort1MDIX_Object = MibTableColumn
mc2200_GESFP2RemotePort1MDIX = _Mc2200_GESFP2RemotePort1MDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 43),
    _Mc2200_GESFP2RemotePort1MDIX_Type()
)
mc2200_GESFP2RemotePort1MDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort1MDIX.setStatus("current")


class _Mc2200_GESFP2RemotePort2Link_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort2Link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_GESFP2RemotePort2Link_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort2Link_Object = MibTableColumn
mc2200_GESFP2RemotePort2Link = _Mc2200_GESFP2RemotePort2Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 44),
    _Mc2200_GESFP2RemotePort2Link_Type()
)
mc2200_GESFP2RemotePort2Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort2Link.setStatus("current")


class _Mc2200_GESFP2RemotePort2Speed_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort2Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("speed100M", 1),
          ("speed10M", 2),
          ("auto", 3))
    )


_Mc2200_GESFP2RemotePort2Speed_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort2Speed_Object = MibTableColumn
mc2200_GESFP2RemotePort2Speed = _Mc2200_GESFP2RemotePort2Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 45),
    _Mc2200_GESFP2RemotePort2Speed_Type()
)
mc2200_GESFP2RemotePort2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort2Speed.setStatus("current")


class _Mc2200_GESFP2RemotePort2Duplex_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort2Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_Mc2200_GESFP2RemotePort2Duplex_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort2Duplex_Object = MibTableColumn
mc2200_GESFP2RemotePort2Duplex = _Mc2200_GESFP2RemotePort2Duplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 46),
    _Mc2200_GESFP2RemotePort2Duplex_Type()
)
mc2200_GESFP2RemotePort2Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort2Duplex.setStatus("current")


class _Mc2200_GESFP2RemotePort2Mode_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort2Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mode10MHALFDUPLEX", 2),
          ("mode10MFULLDUPLEX", 3),
          ("mode100MHALFDUPLEX", 4),
          ("mode100MFULLDUPLEX", 5))
    )


_Mc2200_GESFP2RemotePort2Mode_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort2Mode_Object = MibTableColumn
mc2200_GESFP2RemotePort2Mode = _Mc2200_GESFP2RemotePort2Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 47),
    _Mc2200_GESFP2RemotePort2Mode_Type()
)
mc2200_GESFP2RemotePort2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort2Mode.setStatus("current")


class _Mc2200_GESFP2RemotePort2MDIX_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort2MDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mdi", 2),
          ("mdi-X", 3))
    )


_Mc2200_GESFP2RemotePort2MDIX_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort2MDIX_Object = MibTableColumn
mc2200_GESFP2RemotePort2MDIX = _Mc2200_GESFP2RemotePort2MDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 48),
    _Mc2200_GESFP2RemotePort2MDIX_Type()
)
mc2200_GESFP2RemotePort2MDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort2MDIX.setStatus("current")


class _Mc2200_GESFP2RemotePort3Link_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort3Link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_GESFP2RemotePort3Link_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort3Link_Object = MibTableColumn
mc2200_GESFP2RemotePort3Link = _Mc2200_GESFP2RemotePort3Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 49),
    _Mc2200_GESFP2RemotePort3Link_Type()
)
mc2200_GESFP2RemotePort3Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort3Link.setStatus("current")


class _Mc2200_GESFP2RemotePort3Speed_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort3Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("speed100M", 1),
          ("speed10M", 2),
          ("auto", 3))
    )


_Mc2200_GESFP2RemotePort3Speed_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort3Speed_Object = MibTableColumn
mc2200_GESFP2RemotePort3Speed = _Mc2200_GESFP2RemotePort3Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 50),
    _Mc2200_GESFP2RemotePort3Speed_Type()
)
mc2200_GESFP2RemotePort3Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort3Speed.setStatus("current")


class _Mc2200_GESFP2RemotePort3Duplex_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort3Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_Mc2200_GESFP2RemotePort3Duplex_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort3Duplex_Object = MibTableColumn
mc2200_GESFP2RemotePort3Duplex = _Mc2200_GESFP2RemotePort3Duplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 51),
    _Mc2200_GESFP2RemotePort3Duplex_Type()
)
mc2200_GESFP2RemotePort3Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort3Duplex.setStatus("current")


class _Mc2200_GESFP2RemotePort3Mode_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort3Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mode10MHALFDUPLEX", 2),
          ("mode10MFULLDUPLEX", 3),
          ("mode100MHALFDUPLEX", 4),
          ("mode100MFULLDUPLEX", 5))
    )


_Mc2200_GESFP2RemotePort3Mode_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort3Mode_Object = MibTableColumn
mc2200_GESFP2RemotePort3Mode = _Mc2200_GESFP2RemotePort3Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 52),
    _Mc2200_GESFP2RemotePort3Mode_Type()
)
mc2200_GESFP2RemotePort3Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort3Mode.setStatus("current")


class _Mc2200_GESFP2RemotePort3MDIX_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort3MDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mdi", 2),
          ("mdi-X", 3))
    )


_Mc2200_GESFP2RemotePort3MDIX_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort3MDIX_Object = MibTableColumn
mc2200_GESFP2RemotePort3MDIX = _Mc2200_GESFP2RemotePort3MDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 53),
    _Mc2200_GESFP2RemotePort3MDIX_Type()
)
mc2200_GESFP2RemotePort3MDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort3MDIX.setStatus("current")


class _Mc2200_GESFP2RemotePort4Link_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort4Link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_GESFP2RemotePort4Link_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort4Link_Object = MibTableColumn
mc2200_GESFP2RemotePort4Link = _Mc2200_GESFP2RemotePort4Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 54),
    _Mc2200_GESFP2RemotePort4Link_Type()
)
mc2200_GESFP2RemotePort4Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort4Link.setStatus("current")


class _Mc2200_GESFP2RemotePort4Speed_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort4Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("speed100M", 1),
          ("speed10M", 2),
          ("auto", 3))
    )


_Mc2200_GESFP2RemotePort4Speed_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort4Speed_Object = MibTableColumn
mc2200_GESFP2RemotePort4Speed = _Mc2200_GESFP2RemotePort4Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 55),
    _Mc2200_GESFP2RemotePort4Speed_Type()
)
mc2200_GESFP2RemotePort4Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort4Speed.setStatus("current")


class _Mc2200_GESFP2RemotePort4Duplex_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort4Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_Mc2200_GESFP2RemotePort4Duplex_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort4Duplex_Object = MibTableColumn
mc2200_GESFP2RemotePort4Duplex = _Mc2200_GESFP2RemotePort4Duplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 56),
    _Mc2200_GESFP2RemotePort4Duplex_Type()
)
mc2200_GESFP2RemotePort4Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort4Duplex.setStatus("current")


class _Mc2200_GESFP2RemotePort4Mode_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort4Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mode10MHALFDUPLEX", 2),
          ("mode10MFULLDUPLEX", 3),
          ("mode100MHALFDUPLEX", 4),
          ("mode100MFULLDUPLEX", 5))
    )


_Mc2200_GESFP2RemotePort4Mode_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort4Mode_Object = MibTableColumn
mc2200_GESFP2RemotePort4Mode = _Mc2200_GESFP2RemotePort4Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 57),
    _Mc2200_GESFP2RemotePort4Mode_Type()
)
mc2200_GESFP2RemotePort4Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort4Mode.setStatus("current")


class _Mc2200_GESFP2RemotePort4MDIX_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort4MDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mdi", 2),
          ("mdi-X", 3))
    )


_Mc2200_GESFP2RemotePort4MDIX_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort4MDIX_Object = MibTableColumn
mc2200_GESFP2RemotePort4MDIX = _Mc2200_GESFP2RemotePort4MDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 58),
    _Mc2200_GESFP2RemotePort4MDIX_Type()
)
mc2200_GESFP2RemotePort4MDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort4MDIX.setStatus("current")


class _Mc2200_GESFP2RemotePort5Link_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort5Link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_GESFP2RemotePort5Link_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort5Link_Object = MibTableColumn
mc2200_GESFP2RemotePort5Link = _Mc2200_GESFP2RemotePort5Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 59),
    _Mc2200_GESFP2RemotePort5Link_Type()
)
mc2200_GESFP2RemotePort5Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort5Link.setStatus("current")


class _Mc2200_GESFP2RemotePort5Speed_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort5Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("speed100M", 1),
          ("speed10M", 2),
          ("auto", 3))
    )


_Mc2200_GESFP2RemotePort5Speed_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort5Speed_Object = MibTableColumn
mc2200_GESFP2RemotePort5Speed = _Mc2200_GESFP2RemotePort5Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 60),
    _Mc2200_GESFP2RemotePort5Speed_Type()
)
mc2200_GESFP2RemotePort5Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort5Speed.setStatus("current")


class _Mc2200_GESFP2RemotePort5Duplex_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort5Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_Mc2200_GESFP2RemotePort5Duplex_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort5Duplex_Object = MibTableColumn
mc2200_GESFP2RemotePort5Duplex = _Mc2200_GESFP2RemotePort5Duplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 61),
    _Mc2200_GESFP2RemotePort5Duplex_Type()
)
mc2200_GESFP2RemotePort5Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort5Duplex.setStatus("current")


class _Mc2200_GESFP2RemotePort5Mode_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort5Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mode10MHALFDUPLEX", 2),
          ("mode10MFULLDUPLEX", 3),
          ("mode100MHALFDUPLEX", 4),
          ("mode100MFULLDUPLEX", 5))
    )


_Mc2200_GESFP2RemotePort5Mode_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort5Mode_Object = MibTableColumn
mc2200_GESFP2RemotePort5Mode = _Mc2200_GESFP2RemotePort5Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 62),
    _Mc2200_GESFP2RemotePort5Mode_Type()
)
mc2200_GESFP2RemotePort5Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort5Mode.setStatus("current")


class _Mc2200_GESFP2RemotePort5MDIX_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort5MDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mdi", 2),
          ("mdi-X", 3))
    )


_Mc2200_GESFP2RemotePort5MDIX_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort5MDIX_Object = MibTableColumn
mc2200_GESFP2RemotePort5MDIX = _Mc2200_GESFP2RemotePort5MDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 63),
    _Mc2200_GESFP2RemotePort5MDIX_Type()
)
mc2200_GESFP2RemotePort5MDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort5MDIX.setStatus("current")


class _Mc2200_GESFP2RemotePort6Link_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort6Link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_GESFP2RemotePort6Link_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort6Link_Object = MibTableColumn
mc2200_GESFP2RemotePort6Link = _Mc2200_GESFP2RemotePort6Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 64),
    _Mc2200_GESFP2RemotePort6Link_Type()
)
mc2200_GESFP2RemotePort6Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort6Link.setStatus("current")


class _Mc2200_GESFP2RemotePort6Speed_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort6Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("speed100M", 1),
          ("speed10M", 2),
          ("auto", 3))
    )


_Mc2200_GESFP2RemotePort6Speed_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort6Speed_Object = MibTableColumn
mc2200_GESFP2RemotePort6Speed = _Mc2200_GESFP2RemotePort6Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 65),
    _Mc2200_GESFP2RemotePort6Speed_Type()
)
mc2200_GESFP2RemotePort6Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort6Speed.setStatus("current")


class _Mc2200_GESFP2RemotePort6Duplex_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort6Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_Mc2200_GESFP2RemotePort6Duplex_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort6Duplex_Object = MibTableColumn
mc2200_GESFP2RemotePort6Duplex = _Mc2200_GESFP2RemotePort6Duplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 66),
    _Mc2200_GESFP2RemotePort6Duplex_Type()
)
mc2200_GESFP2RemotePort6Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort6Duplex.setStatus("current")


class _Mc2200_GESFP2RemotePort6Mode_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort6Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mode10MHALFDUPLEX", 2),
          ("mode10MFULLDUPLEX", 3),
          ("mode100MHALFDUPLEX", 4),
          ("mode100MFULLDUPLEX", 5))
    )


_Mc2200_GESFP2RemotePort6Mode_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort6Mode_Object = MibTableColumn
mc2200_GESFP2RemotePort6Mode = _Mc2200_GESFP2RemotePort6Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 67),
    _Mc2200_GESFP2RemotePort6Mode_Type()
)
mc2200_GESFP2RemotePort6Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort6Mode.setStatus("current")


class _Mc2200_GESFP2RemotePort6MDIX_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort6MDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mdi", 2),
          ("mdi-X", 3))
    )


_Mc2200_GESFP2RemotePort6MDIX_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort6MDIX_Object = MibTableColumn
mc2200_GESFP2RemotePort6MDIX = _Mc2200_GESFP2RemotePort6MDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 68),
    _Mc2200_GESFP2RemotePort6MDIX_Type()
)
mc2200_GESFP2RemotePort6MDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort6MDIX.setStatus("current")


class _Mc2200_GESFP2RemotePort7Link_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort7Link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_GESFP2RemotePort7Link_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort7Link_Object = MibTableColumn
mc2200_GESFP2RemotePort7Link = _Mc2200_GESFP2RemotePort7Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 69),
    _Mc2200_GESFP2RemotePort7Link_Type()
)
mc2200_GESFP2RemotePort7Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort7Link.setStatus("current")


class _Mc2200_GESFP2RemotePort7Speed_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort7Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("speed100M", 1),
          ("speed10M", 2),
          ("auto", 3))
    )


_Mc2200_GESFP2RemotePort7Speed_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort7Speed_Object = MibTableColumn
mc2200_GESFP2RemotePort7Speed = _Mc2200_GESFP2RemotePort7Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 70),
    _Mc2200_GESFP2RemotePort7Speed_Type()
)
mc2200_GESFP2RemotePort7Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort7Speed.setStatus("current")


class _Mc2200_GESFP2RemotePort7Duplex_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort7Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_Mc2200_GESFP2RemotePort7Duplex_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort7Duplex_Object = MibTableColumn
mc2200_GESFP2RemotePort7Duplex = _Mc2200_GESFP2RemotePort7Duplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 71),
    _Mc2200_GESFP2RemotePort7Duplex_Type()
)
mc2200_GESFP2RemotePort7Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort7Duplex.setStatus("current")


class _Mc2200_GESFP2RemotePort7Mode_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort7Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mode10MHALFDUPLEX", 2),
          ("mode10MFULLDUPLEX", 3),
          ("mode100MHALFDUPLEX", 4),
          ("mode100MFULLDUPLEX", 5))
    )


_Mc2200_GESFP2RemotePort7Mode_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort7Mode_Object = MibTableColumn
mc2200_GESFP2RemotePort7Mode = _Mc2200_GESFP2RemotePort7Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 72),
    _Mc2200_GESFP2RemotePort7Mode_Type()
)
mc2200_GESFP2RemotePort7Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort7Mode.setStatus("current")


class _Mc2200_GESFP2RemotePort7MDIX_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort7MDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mdi", 2),
          ("mdi-X", 3))
    )


_Mc2200_GESFP2RemotePort7MDIX_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort7MDIX_Object = MibTableColumn
mc2200_GESFP2RemotePort7MDIX = _Mc2200_GESFP2RemotePort7MDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 73),
    _Mc2200_GESFP2RemotePort7MDIX_Type()
)
mc2200_GESFP2RemotePort7MDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort7MDIX.setStatus("current")


class _Mc2200_GESFP2RemotePort8Link_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort8Link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_GESFP2RemotePort8Link_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort8Link_Object = MibTableColumn
mc2200_GESFP2RemotePort8Link = _Mc2200_GESFP2RemotePort8Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 74),
    _Mc2200_GESFP2RemotePort8Link_Type()
)
mc2200_GESFP2RemotePort8Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort8Link.setStatus("current")


class _Mc2200_GESFP2RemotePort8Speed_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort8Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("speed100M", 1),
          ("speed10M", 2),
          ("auto", 3))
    )


_Mc2200_GESFP2RemotePort8Speed_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort8Speed_Object = MibTableColumn
mc2200_GESFP2RemotePort8Speed = _Mc2200_GESFP2RemotePort8Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 75),
    _Mc2200_GESFP2RemotePort8Speed_Type()
)
mc2200_GESFP2RemotePort8Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort8Speed.setStatus("current")


class _Mc2200_GESFP2RemotePort8Duplex_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort8Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_Mc2200_GESFP2RemotePort8Duplex_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort8Duplex_Object = MibTableColumn
mc2200_GESFP2RemotePort8Duplex = _Mc2200_GESFP2RemotePort8Duplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 76),
    _Mc2200_GESFP2RemotePort8Duplex_Type()
)
mc2200_GESFP2RemotePort8Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort8Duplex.setStatus("current")


class _Mc2200_GESFP2RemotePort8Mode_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort8Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mode10MHALFDUPLEX", 2),
          ("mode10MFULLDUPLEX", 3),
          ("mode100MHALFDUPLEX", 4),
          ("mode100MFULLDUPLEX", 5))
    )


_Mc2200_GESFP2RemotePort8Mode_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort8Mode_Object = MibTableColumn
mc2200_GESFP2RemotePort8Mode = _Mc2200_GESFP2RemotePort8Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 77),
    _Mc2200_GESFP2RemotePort8Mode_Type()
)
mc2200_GESFP2RemotePort8Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort8Mode.setStatus("current")


class _Mc2200_GESFP2RemotePort8MDIX_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort8MDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("auto", 1),
          ("mdi", 2),
          ("mdi-X", 3))
    )


_Mc2200_GESFP2RemotePort8MDIX_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort8MDIX_Object = MibTableColumn
mc2200_GESFP2RemotePort8MDIX = _Mc2200_GESFP2RemotePort8MDIX_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 78),
    _Mc2200_GESFP2RemotePort8MDIX_Type()
)
mc2200_GESFP2RemotePort8MDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort8MDIX.setStatus("current")


class _Mc2200_GESFP2RemotePort9Link_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort9Link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_GESFP2RemotePort9Link_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort9Link_Object = MibTableColumn
mc2200_GESFP2RemotePort9Link = _Mc2200_GESFP2RemotePort9Link_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 79),
    _Mc2200_GESFP2RemotePort9Link_Type()
)
mc2200_GESFP2RemotePort9Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort9Link.setStatus("current")


class _Mc2200_GESFP2RemotePort9Speed_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort9Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("speed1000M", 0),
          ("speed100M", 1),
          ("speed10M", 2),
          ("auto", 3),
          ("noremotecard", 4))
    )


_Mc2200_GESFP2RemotePort9Speed_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort9Speed_Object = MibTableColumn
mc2200_GESFP2RemotePort9Speed = _Mc2200_GESFP2RemotePort9Speed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 80),
    _Mc2200_GESFP2RemotePort9Speed_Type()
)
mc2200_GESFP2RemotePort9Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort9Speed.setStatus("current")


class _Mc2200_GESFP2RemotePort9Duplex_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort9Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_Mc2200_GESFP2RemotePort9Duplex_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort9Duplex_Object = MibTableColumn
mc2200_GESFP2RemotePort9Duplex = _Mc2200_GESFP2RemotePort9Duplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 81),
    _Mc2200_GESFP2RemotePort9Duplex_Type()
)
mc2200_GESFP2RemotePort9Duplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort9Duplex.setStatus("current")


class _Mc2200_GESFP2RemotePort9Mode_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort9Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("mode1000Xauto", 1),
          ("mode1000XFORCE", 2))
    )


_Mc2200_GESFP2RemotePort9Mode_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort9Mode_Object = MibTableColumn
mc2200_GESFP2RemotePort9Mode = _Mc2200_GESFP2RemotePort9Mode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 82),
    _Mc2200_GESFP2RemotePort9Mode_Type()
)
mc2200_GESFP2RemotePort9Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort9Mode.setStatus("current")
_Mc2200_GESFP2RemotePort9SFPInfo_Type = DisplayString
_Mc2200_GESFP2RemotePort9SFPInfo_Object = MibTableColumn
mc2200_GESFP2RemotePort9SFPInfo = _Mc2200_GESFP2RemotePort9SFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 84),
    _Mc2200_GESFP2RemotePort9SFPInfo_Type()
)
mc2200_GESFP2RemotePort9SFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort9SFPInfo.setStatus("current")
_Mc2200_GESFP2RemoteIPAddress_Type = IpAddress
_Mc2200_GESFP2RemoteIPAddress_Object = MibTableColumn
mc2200_GESFP2RemoteIPAddress = _Mc2200_GESFP2RemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 85),
    _Mc2200_GESFP2RemoteIPAddress_Type()
)
mc2200_GESFP2RemoteIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemoteIPAddress.setStatus("mandatory")
_Mc2200_GESFP2RemoteSubnetMask_Type = IpAddress
_Mc2200_GESFP2RemoteSubnetMask_Object = MibTableColumn
mc2200_GESFP2RemoteSubnetMask = _Mc2200_GESFP2RemoteSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 86),
    _Mc2200_GESFP2RemoteSubnetMask_Type()
)
mc2200_GESFP2RemoteSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemoteSubnetMask.setStatus("mandatory")
_Mc2200_GESFP2RemoteGateWay_Type = IpAddress
_Mc2200_GESFP2RemoteGateWay_Object = MibTableColumn
mc2200_GESFP2RemoteGateWay = _Mc2200_GESFP2RemoteGateWay_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 87),
    _Mc2200_GESFP2RemoteGateWay_Type()
)
mc2200_GESFP2RemoteGateWay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemoteGateWay.setStatus("mandatory")


class _Mc2200_GESFP2RemoteVLANEnable_Type(Integer32):
    """Custom type mc2200_GESFP2RemoteVLANEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("enable", 1),
          ("disable", 2))
    )


_Mc2200_GESFP2RemoteVLANEnable_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemoteVLANEnable_Object = MibTableColumn
mc2200_GESFP2RemoteVLANEnable = _Mc2200_GESFP2RemoteVLANEnable_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 88),
    _Mc2200_GESFP2RemoteVLANEnable_Type()
)
mc2200_GESFP2RemoteVLANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemoteVLANEnable.setStatus("mandatory")
_Mc2200_GESFP2RemoteVID_Type = Integer32
_Mc2200_GESFP2RemoteVID_Object = MibTableColumn
mc2200_GESFP2RemoteVID = _Mc2200_GESFP2RemoteVID_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 89),
    _Mc2200_GESFP2RemoteVID_Type()
)
mc2200_GESFP2RemoteVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemoteVID.setStatus("mandatory")


class _Mc2200_GESFP2RemoteAlarm_Type(Integer32):
    """Custom type mc2200_GESFP2RemoteAlarm based on Integer32"""
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


_Mc2200_GESFP2RemoteAlarm_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemoteAlarm_Object = MibTableColumn
mc2200_GESFP2RemoteAlarm = _Mc2200_GESFP2RemoteAlarm_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 90),
    _Mc2200_GESFP2RemoteAlarm_Type()
)
mc2200_GESFP2RemoteAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemoteAlarm.setStatus("current")
_Mc2200_GESFP2Default_Type = Integer32
_Mc2200_GESFP2Default_Object = MibTableColumn
mc2200_GESFP2Default = _Mc2200_GESFP2Default_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 91),
    _Mc2200_GESFP2Default_Type()
)
mc2200_GESFP2Default.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2Default.setStatus("current")
_Mc2200_GESFP2Reboot_Type = Integer32
_Mc2200_GESFP2Reboot_Object = MibTableColumn
mc2200_GESFP2Reboot = _Mc2200_GESFP2Reboot_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 92),
    _Mc2200_GESFP2Reboot_Type()
)
mc2200_GESFP2Reboot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2Reboot.setStatus("current")


class _Mc2200_GESFP2LocalTXSpeed_Type(Integer32):
    """Custom type mc2200_GESFP2LocalTXSpeed based on Integer32"""
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
        *(("speed1000M", 1),
          ("speed100M", 2),
          ("speed10M", 3),
          ("down", 4))
    )


_Mc2200_GESFP2LocalTXSpeed_Type.__name__ = "Integer32"
_Mc2200_GESFP2LocalTXSpeed_Object = MibTableColumn
mc2200_GESFP2LocalTXSpeed = _Mc2200_GESFP2LocalTXSpeed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 93),
    _Mc2200_GESFP2LocalTXSpeed_Type()
)
mc2200_GESFP2LocalTXSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2LocalTXSpeed.setStatus("mandatory")


class _Mc2200_GESFP2RemoteLanIsolate_Type(Integer32):
    """Custom type mc2200_GESFP2RemoteLanIsolate based on Integer32"""
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


_Mc2200_GESFP2RemoteLanIsolate_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemoteLanIsolate_Object = MibTableColumn
mc2200_GESFP2RemoteLanIsolate = _Mc2200_GESFP2RemoteLanIsolate_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 94),
    _Mc2200_GESFP2RemoteLanIsolate_Type()
)
mc2200_GESFP2RemoteLanIsolate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemoteLanIsolate.setStatus("current")
_Mc2200_GESFP2Localportuser_Type = DisplayString
_Mc2200_GESFP2Localportuser_Object = MibTableColumn
mc2200_GESFP2Localportuser = _Mc2200_GESFP2Localportuser_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 95),
    _Mc2200_GESFP2Localportuser_Type()
)
mc2200_GESFP2Localportuser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2Localportuser.setStatus("current")
_Mc2200_GESFP2Remoteportuser1_Type = DisplayString
_Mc2200_GESFP2Remoteportuser1_Object = MibTableColumn
mc2200_GESFP2Remoteportuser1 = _Mc2200_GESFP2Remoteportuser1_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 96),
    _Mc2200_GESFP2Remoteportuser1_Type()
)
mc2200_GESFP2Remoteportuser1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2Remoteportuser1.setStatus("current")
_Mc2200_GESFP2Remoteportuser2_Type = DisplayString
_Mc2200_GESFP2Remoteportuser2_Object = MibTableColumn
mc2200_GESFP2Remoteportuser2 = _Mc2200_GESFP2Remoteportuser2_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 97),
    _Mc2200_GESFP2Remoteportuser2_Type()
)
mc2200_GESFP2Remoteportuser2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2Remoteportuser2.setStatus("current")
_Mc2200_GESFP2Remoteportuser3_Type = DisplayString
_Mc2200_GESFP2Remoteportuser3_Object = MibTableColumn
mc2200_GESFP2Remoteportuser3 = _Mc2200_GESFP2Remoteportuser3_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 98),
    _Mc2200_GESFP2Remoteportuser3_Type()
)
mc2200_GESFP2Remoteportuser3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2Remoteportuser3.setStatus("current")
_Mc2200_GESFP2Remoteportuser4_Type = DisplayString
_Mc2200_GESFP2Remoteportuser4_Object = MibTableColumn
mc2200_GESFP2Remoteportuser4 = _Mc2200_GESFP2Remoteportuser4_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 99),
    _Mc2200_GESFP2Remoteportuser4_Type()
)
mc2200_GESFP2Remoteportuser4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2Remoteportuser4.setStatus("current")
_Mc2200_GESFP2Remoteportuser5_Type = DisplayString
_Mc2200_GESFP2Remoteportuser5_Object = MibTableColumn
mc2200_GESFP2Remoteportuser5 = _Mc2200_GESFP2Remoteportuser5_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 100),
    _Mc2200_GESFP2Remoteportuser5_Type()
)
mc2200_GESFP2Remoteportuser5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2Remoteportuser5.setStatus("current")
_Mc2200_GESFP2Remoteportuser6_Type = DisplayString
_Mc2200_GESFP2Remoteportuser6_Object = MibTableColumn
mc2200_GESFP2Remoteportuser6 = _Mc2200_GESFP2Remoteportuser6_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 101),
    _Mc2200_GESFP2Remoteportuser6_Type()
)
mc2200_GESFP2Remoteportuser6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2Remoteportuser6.setStatus("current")
_Mc2200_GESFP2Remoteportuser7_Type = DisplayString
_Mc2200_GESFP2Remoteportuser7_Object = MibTableColumn
mc2200_GESFP2Remoteportuser7 = _Mc2200_GESFP2Remoteportuser7_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 102),
    _Mc2200_GESFP2Remoteportuser7_Type()
)
mc2200_GESFP2Remoteportuser7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2Remoteportuser7.setStatus("current")
_Mc2200_GESFP2Remoteportuser8_Type = DisplayString
_Mc2200_GESFP2Remoteportuser8_Object = MibTableColumn
mc2200_GESFP2Remoteportuser8 = _Mc2200_GESFP2Remoteportuser8_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 103),
    _Mc2200_GESFP2Remoteportuser8_Type()
)
mc2200_GESFP2Remoteportuser8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2Remoteportuser8.setStatus("current")
_Mc2200_GESFP2Remoteportuser9_Type = DisplayString
_Mc2200_GESFP2Remoteportuser9_Object = MibTableColumn
mc2200_GESFP2Remoteportuser9 = _Mc2200_GESFP2Remoteportuser9_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 104),
    _Mc2200_GESFP2Remoteportuser9_Type()
)
mc2200_GESFP2Remoteportuser9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2Remoteportuser9.setStatus("current")


class _Mc2200_GESFP2LocalTXDuplex_Type(Integer32):
    """Custom type mc2200_GESFP2LocalTXDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2),
          ("down", 3))
    )


_Mc2200_GESFP2LocalTXDuplex_Type.__name__ = "Integer32"
_Mc2200_GESFP2LocalTXDuplex_Object = MibTableColumn
mc2200_GESFP2LocalTXDuplex = _Mc2200_GESFP2LocalTXDuplex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 105),
    _Mc2200_GESFP2LocalTXDuplex_Type()
)
mc2200_GESFP2LocalTXDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2LocalTXDuplex.setStatus("mandatory")


class _Mc2200_GESFP2WANOpticalPowerCheck_Type(Integer32):
    """Custom type mc2200_GESFP2WANOpticalPowerCheck based on Integer32"""
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


_Mc2200_GESFP2WANOpticalPowerCheck_Type.__name__ = "Integer32"
_Mc2200_GESFP2WANOpticalPowerCheck_Object = MibTableColumn
mc2200_GESFP2WANOpticalPowerCheck = _Mc2200_GESFP2WANOpticalPowerCheck_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 106),
    _Mc2200_GESFP2WANOpticalPowerCheck_Type()
)
mc2200_GESFP2WANOpticalPowerCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2WANOpticalPowerCheck.setStatus("current")


class _Mc2200_GESFP2WANThreshold_Type(Integer32):
    """Custom type mc2200_GESFP2WANThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71)
        )
    )
    namedValues = NamedValues(
        *(("db-32", 1),
          ("db-31dot5", 2),
          ("db-31", 3),
          ("db-30dot5", 4),
          ("db-30", 5),
          ("db-29dot5", 6),
          ("db-29", 7),
          ("db-28dot5", 8),
          ("db-28", 9),
          ("db-27dot5", 10),
          ("db-27", 11),
          ("db-26dot5", 12),
          ("db-26", 13),
          ("db-25dot5", 14),
          ("db-25", 15),
          ("db-24dot5", 16),
          ("db-24", 17),
          ("db-23dot5", 18),
          ("db-23", 19),
          ("db-22dot5", 20),
          ("db-22", 21),
          ("db-21dot5", 22),
          ("db-21", 23),
          ("db-20dot5", 24),
          ("db-20", 25),
          ("db-19dot5", 26),
          ("db-19", 27),
          ("db-18dot5", 28),
          ("db-18", 29),
          ("db-17dot5", 30),
          ("db-17", 31),
          ("db-16dot5", 32),
          ("db-16", 33),
          ("db-15dot5", 34),
          ("db-15", 35),
          ("db-14dot5", 36),
          ("db-14", 37),
          ("db-13dot5", 38),
          ("db-13", 39),
          ("db-12dot5", 40),
          ("db-12", 41),
          ("db-11dot5", 42),
          ("db-11", 43),
          ("db-10dot5", 44),
          ("db-10", 45),
          ("db-9dot5", 46),
          ("db-9", 47),
          ("db-8dot5", 48),
          ("db-8", 49),
          ("db-7dot5", 50),
          ("db-7", 51),
          ("db-6dot5", 52),
          ("db-6", 53),
          ("db-5dot5", 54),
          ("db-5", 55),
          ("db-4dot5", 56),
          ("db-4", 57),
          ("db-3dot5", 58),
          ("db-3", 59),
          ("db-2dot5", 60),
          ("db-2", 61),
          ("db-1dot5", 62),
          ("db-1", 63),
          ("db-0dot5", 64),
          ("db-0", 65),
          ("db0dot5", 66),
          ("db1", 67),
          ("db1dot5", 68),
          ("db2", 69),
          ("db2dot5", 70),
          ("db3", 71))
    )


_Mc2200_GESFP2WANThreshold_Type.__name__ = "Integer32"
_Mc2200_GESFP2WANThreshold_Object = MibTableColumn
mc2200_GESFP2WANThreshold = _Mc2200_GESFP2WANThreshold_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 107),
    _Mc2200_GESFP2WANThreshold_Type()
)
mc2200_GESFP2WANThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2WANThreshold.setStatus("current")


class _Mc2200_GESFP2TrapFilterLocalLAN_Type(Integer32):
    """Custom type mc2200_GESFP2TrapFilterLocalLAN based on Integer32"""
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


_Mc2200_GESFP2TrapFilterLocalLAN_Type.__name__ = "Integer32"
_Mc2200_GESFP2TrapFilterLocalLAN_Object = MibTableColumn
mc2200_GESFP2TrapFilterLocalLAN = _Mc2200_GESFP2TrapFilterLocalLAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 108),
    _Mc2200_GESFP2TrapFilterLocalLAN_Type()
)
mc2200_GESFP2TrapFilterLocalLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2TrapFilterLocalLAN.setStatus("current")


class _Mc2200_GESFP2TrapFilterLocalWAN_Type(Integer32):
    """Custom type mc2200_GESFP2TrapFilterLocalWAN based on Integer32"""
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


_Mc2200_GESFP2TrapFilterLocalWAN_Type.__name__ = "Integer32"
_Mc2200_GESFP2TrapFilterLocalWAN_Object = MibTableColumn
mc2200_GESFP2TrapFilterLocalWAN = _Mc2200_GESFP2TrapFilterLocalWAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 109),
    _Mc2200_GESFP2TrapFilterLocalWAN_Type()
)
mc2200_GESFP2TrapFilterLocalWAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2TrapFilterLocalWAN.setStatus("current")


class _Mc2200_GESFP2TrapFilterRemotePower_Type(Integer32):
    """Custom type mc2200_GESFP2TrapFilterRemotePower based on Integer32"""
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


_Mc2200_GESFP2TrapFilterRemotePower_Type.__name__ = "Integer32"
_Mc2200_GESFP2TrapFilterRemotePower_Object = MibTableColumn
mc2200_GESFP2TrapFilterRemotePower = _Mc2200_GESFP2TrapFilterRemotePower_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 110),
    _Mc2200_GESFP2TrapFilterRemotePower_Type()
)
mc2200_GESFP2TrapFilterRemotePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2TrapFilterRemotePower.setStatus("current")


class _Mc2200_GESFP2TrapFilterRemoteLAN_Type(Integer32):
    """Custom type mc2200_GESFP2TrapFilterRemoteLAN based on Integer32"""
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


_Mc2200_GESFP2TrapFilterRemoteLAN_Type.__name__ = "Integer32"
_Mc2200_GESFP2TrapFilterRemoteLAN_Object = MibTableColumn
mc2200_GESFP2TrapFilterRemoteLAN = _Mc2200_GESFP2TrapFilterRemoteLAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 111),
    _Mc2200_GESFP2TrapFilterRemoteLAN_Type()
)
mc2200_GESFP2TrapFilterRemoteLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2TrapFilterRemoteLAN.setStatus("current")


class _Mc2200_GESFP2TrapFilterRemoteWAN_Type(Integer32):
    """Custom type mc2200_GESFP2TrapFilterRemoteWAN based on Integer32"""
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


_Mc2200_GESFP2TrapFilterRemoteWAN_Type.__name__ = "Integer32"
_Mc2200_GESFP2TrapFilterRemoteWAN_Object = MibTableColumn
mc2200_GESFP2TrapFilterRemoteWAN = _Mc2200_GESFP2TrapFilterRemoteWAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 112),
    _Mc2200_GESFP2TrapFilterRemoteWAN_Type()
)
mc2200_GESFP2TrapFilterRemoteWAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2TrapFilterRemoteWAN.setStatus("current")
_Mc2200_GESFP2CardType_Type = DisplayString
_Mc2200_GESFP2CardType_Object = MibTableColumn
mc2200_GESFP2CardType = _Mc2200_GESFP2CardType_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 114),
    _Mc2200_GESFP2CardType_Type()
)
mc2200_GESFP2CardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_GESFP2CardType.setStatus("current")


class _Mc2200_GESFP2RemotePort1UpstreamBandwidth_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort1UpstreamBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GESFP2RemotePort1UpstreamBandwidth_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort1UpstreamBandwidth_Object = MibTableColumn
mc2200_GESFP2RemotePort1UpstreamBandwidth = _Mc2200_GESFP2RemotePort1UpstreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 115),
    _Mc2200_GESFP2RemotePort1UpstreamBandwidth_Type()
)
mc2200_GESFP2RemotePort1UpstreamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort1UpstreamBandwidth.setStatus("current")


class _Mc2200_GESFP2RemotePort1DownstreamBandwidth_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort1DownstreamBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GESFP2RemotePort1DownstreamBandwidth_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort1DownstreamBandwidth_Object = MibTableColumn
mc2200_GESFP2RemotePort1DownstreamBandwidth = _Mc2200_GESFP2RemotePort1DownstreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 116),
    _Mc2200_GESFP2RemotePort1DownstreamBandwidth_Type()
)
mc2200_GESFP2RemotePort1DownstreamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort1DownstreamBandwidth.setStatus("current")


class _Mc2200_GESFP2RemotePort2UpstreamBandwidth_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort2UpstreamBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GESFP2RemotePort2UpstreamBandwidth_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort2UpstreamBandwidth_Object = MibTableColumn
mc2200_GESFP2RemotePort2UpstreamBandwidth = _Mc2200_GESFP2RemotePort2UpstreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 117),
    _Mc2200_GESFP2RemotePort2UpstreamBandwidth_Type()
)
mc2200_GESFP2RemotePort2UpstreamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort2UpstreamBandwidth.setStatus("current")


class _Mc2200_GESFP2RemotePort2DownstreamBandwidth_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort2DownstreamBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GESFP2RemotePort2DownstreamBandwidth_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort2DownstreamBandwidth_Object = MibTableColumn
mc2200_GESFP2RemotePort2DownstreamBandwidth = _Mc2200_GESFP2RemotePort2DownstreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 118),
    _Mc2200_GESFP2RemotePort2DownstreamBandwidth_Type()
)
mc2200_GESFP2RemotePort2DownstreamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort2DownstreamBandwidth.setStatus("current")


class _Mc2200_GESFP2RemotePort3UpstreamBandwidth_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort3UpstreamBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GESFP2RemotePort3UpstreamBandwidth_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort3UpstreamBandwidth_Object = MibTableColumn
mc2200_GESFP2RemotePort3UpstreamBandwidth = _Mc2200_GESFP2RemotePort3UpstreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 119),
    _Mc2200_GESFP2RemotePort3UpstreamBandwidth_Type()
)
mc2200_GESFP2RemotePort3UpstreamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort3UpstreamBandwidth.setStatus("current")


class _Mc2200_GESFP2RemotePort3DownstreamBandwidth_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort3DownstreamBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GESFP2RemotePort3DownstreamBandwidth_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort3DownstreamBandwidth_Object = MibTableColumn
mc2200_GESFP2RemotePort3DownstreamBandwidth = _Mc2200_GESFP2RemotePort3DownstreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 120),
    _Mc2200_GESFP2RemotePort3DownstreamBandwidth_Type()
)
mc2200_GESFP2RemotePort3DownstreamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort3DownstreamBandwidth.setStatus("current")


class _Mc2200_GESFP2RemotePort4UpstreamBandwidth_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort4UpstreamBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GESFP2RemotePort4UpstreamBandwidth_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort4UpstreamBandwidth_Object = MibTableColumn
mc2200_GESFP2RemotePort4UpstreamBandwidth = _Mc2200_GESFP2RemotePort4UpstreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 121),
    _Mc2200_GESFP2RemotePort4UpstreamBandwidth_Type()
)
mc2200_GESFP2RemotePort4UpstreamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort4UpstreamBandwidth.setStatus("current")


class _Mc2200_GESFP2RemotePort4DownstreamBandwidth_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort4DownstreamBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GESFP2RemotePort4DownstreamBandwidth_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort4DownstreamBandwidth_Object = MibTableColumn
mc2200_GESFP2RemotePort4DownstreamBandwidth = _Mc2200_GESFP2RemotePort4DownstreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 122),
    _Mc2200_GESFP2RemotePort4DownstreamBandwidth_Type()
)
mc2200_GESFP2RemotePort4DownstreamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort4DownstreamBandwidth.setStatus("current")


class _Mc2200_GESFP2RemotePort5UpstreamBandwidth_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort5UpstreamBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GESFP2RemotePort5UpstreamBandwidth_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort5UpstreamBandwidth_Object = MibTableColumn
mc2200_GESFP2RemotePort5UpstreamBandwidth = _Mc2200_GESFP2RemotePort5UpstreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 123),
    _Mc2200_GESFP2RemotePort5UpstreamBandwidth_Type()
)
mc2200_GESFP2RemotePort5UpstreamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort5UpstreamBandwidth.setStatus("current")


class _Mc2200_GESFP2RemotePort5DownstreamBandwidth_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort5DownstreamBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GESFP2RemotePort5DownstreamBandwidth_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort5DownstreamBandwidth_Object = MibTableColumn
mc2200_GESFP2RemotePort5DownstreamBandwidth = _Mc2200_GESFP2RemotePort5DownstreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 124),
    _Mc2200_GESFP2RemotePort5DownstreamBandwidth_Type()
)
mc2200_GESFP2RemotePort5DownstreamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort5DownstreamBandwidth.setStatus("current")


class _Mc2200_GESFP2RemotePort6UpstreamBandwidth_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort6UpstreamBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GESFP2RemotePort6UpstreamBandwidth_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort6UpstreamBandwidth_Object = MibTableColumn
mc2200_GESFP2RemotePort6UpstreamBandwidth = _Mc2200_GESFP2RemotePort6UpstreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 125),
    _Mc2200_GESFP2RemotePort6UpstreamBandwidth_Type()
)
mc2200_GESFP2RemotePort6UpstreamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort6UpstreamBandwidth.setStatus("current")


class _Mc2200_GESFP2RemotePort6DownstreamBandwidth_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort6DownstreamBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GESFP2RemotePort6DownstreamBandwidth_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort6DownstreamBandwidth_Object = MibTableColumn
mc2200_GESFP2RemotePort6DownstreamBandwidth = _Mc2200_GESFP2RemotePort6DownstreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 126),
    _Mc2200_GESFP2RemotePort6DownstreamBandwidth_Type()
)
mc2200_GESFP2RemotePort6DownstreamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort6DownstreamBandwidth.setStatus("current")


class _Mc2200_GESFP2RemotePort7UpstreamBandwidth_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort7UpstreamBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GESFP2RemotePort7UpstreamBandwidth_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort7UpstreamBandwidth_Object = MibTableColumn
mc2200_GESFP2RemotePort7UpstreamBandwidth = _Mc2200_GESFP2RemotePort7UpstreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 127),
    _Mc2200_GESFP2RemotePort7UpstreamBandwidth_Type()
)
mc2200_GESFP2RemotePort7UpstreamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort7UpstreamBandwidth.setStatus("current")


class _Mc2200_GESFP2RemotePort7DownstreamBandwidth_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort7DownstreamBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GESFP2RemotePort7DownstreamBandwidth_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort7DownstreamBandwidth_Object = MibTableColumn
mc2200_GESFP2RemotePort7DownstreamBandwidth = _Mc2200_GESFP2RemotePort7DownstreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 128),
    _Mc2200_GESFP2RemotePort7DownstreamBandwidth_Type()
)
mc2200_GESFP2RemotePort7DownstreamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort7DownstreamBandwidth.setStatus("current")


class _Mc2200_GESFP2RemotePort8UpstreamBandwidth_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort8UpstreamBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GESFP2RemotePort8UpstreamBandwidth_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort8UpstreamBandwidth_Object = MibTableColumn
mc2200_GESFP2RemotePort8UpstreamBandwidth = _Mc2200_GESFP2RemotePort8UpstreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 129),
    _Mc2200_GESFP2RemotePort8UpstreamBandwidth_Type()
)
mc2200_GESFP2RemotePort8UpstreamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort8UpstreamBandwidth.setStatus("current")


class _Mc2200_GESFP2RemotePort8DownstreamBandwidth_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort8DownstreamBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GESFP2RemotePort8DownstreamBandwidth_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort8DownstreamBandwidth_Object = MibTableColumn
mc2200_GESFP2RemotePort8DownstreamBandwidth = _Mc2200_GESFP2RemotePort8DownstreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 130),
    _Mc2200_GESFP2RemotePort8DownstreamBandwidth_Type()
)
mc2200_GESFP2RemotePort8DownstreamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort8DownstreamBandwidth.setStatus("current")


class _Mc2200_GESFP2RemotePort9UpstreamBandwidth_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort9UpstreamBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GESFP2RemotePort9UpstreamBandwidth_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort9UpstreamBandwidth_Object = MibTableColumn
mc2200_GESFP2RemotePort9UpstreamBandwidth = _Mc2200_GESFP2RemotePort9UpstreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 131),
    _Mc2200_GESFP2RemotePort9UpstreamBandwidth_Type()
)
mc2200_GESFP2RemotePort9UpstreamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort9UpstreamBandwidth.setStatus("current")


class _Mc2200_GESFP2RemotePort9DownstreamBandwidth_Type(Integer32):
    """Custom type mc2200_GESFP2RemotePort9DownstreamBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate50M", 50),
          ("rate100M", 100))
    )


_Mc2200_GESFP2RemotePort9DownstreamBandwidth_Type.__name__ = "Integer32"
_Mc2200_GESFP2RemotePort9DownstreamBandwidth_Object = MibTableColumn
mc2200_GESFP2RemotePort9DownstreamBandwidth = _Mc2200_GESFP2RemotePort9DownstreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 19, 1, 132),
    _Mc2200_GESFP2RemotePort9DownstreamBandwidth_Type()
)
mc2200_GESFP2RemotePort9DownstreamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_GESFP2RemotePort9DownstreamBandwidth.setStatus("current")
_Mc2200_FEMCTable_Object = MibTable
mc2200_FEMCTable = _Mc2200_FEMCTable_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20)
)
if mibBuilder.loadTexts:
    mc2200_FEMCTable.setStatus("current")
_Mc2200_FEMCEntry_Object = MibTableRow
mc2200_FEMCEntry = _Mc2200_FEMCEntry_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1)
)
mc2200_FEMCEntry.setIndexNames(
    (0, "OnAccess2200-MIB", "mc2200-FEMCCardIndex"),
)
if mibBuilder.loadTexts:
    mc2200_FEMCEntry.setStatus("current")


class _Mc2200_FEMCCardIndex_Type(Integer32):
    """Custom type mc2200_FEMCCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("card01", 1),
          ("card02", 2),
          ("card03", 3),
          ("card04", 4),
          ("card05", 5),
          ("card06", 6),
          ("card07", 7),
          ("card08", 8),
          ("card09", 9),
          ("card10", 10),
          ("card11", 11),
          ("card12", 12),
          ("card13", 13),
          ("card14", 14),
          ("card15", 15))
    )


_Mc2200_FEMCCardIndex_Type.__name__ = "Integer32"
_Mc2200_FEMCCardIndex_Object = MibTableColumn
mc2200_FEMCCardIndex = _Mc2200_FEMCCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 1),
    _Mc2200_FEMCCardIndex_Type()
)
mc2200_FEMCCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCCardIndex.setStatus("current")
_Mc2200_FEMCLocalLANSFPInfo_Type = DisplayString
_Mc2200_FEMCLocalLANSFPInfo_Object = MibTableColumn
mc2200_FEMCLocalLANSFPInfo = _Mc2200_FEMCLocalLANSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 2),
    _Mc2200_FEMCLocalLANSFPInfo_Type()
)
mc2200_FEMCLocalLANSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCLocalLANSFPInfo.setStatus("current")


class _Mc2200_FEMCLocalLANLink_Type(Integer32):
    """Custom type mc2200_FEMCLocalLANLink based on Integer32"""
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


_Mc2200_FEMCLocalLANLink_Type.__name__ = "Integer32"
_Mc2200_FEMCLocalLANLink_Object = MibTableColumn
mc2200_FEMCLocalLANLink = _Mc2200_FEMCLocalLANLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 3),
    _Mc2200_FEMCLocalLANLink_Type()
)
mc2200_FEMCLocalLANLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCLocalLANLink.setStatus("mandatory")
_Mc2200_FEMCLocalWANSFPInfo_Type = DisplayString
_Mc2200_FEMCLocalWANSFPInfo_Object = MibTableColumn
mc2200_FEMCLocalWANSFPInfo = _Mc2200_FEMCLocalWANSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 4),
    _Mc2200_FEMCLocalWANSFPInfo_Type()
)
mc2200_FEMCLocalWANSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCLocalWANSFPInfo.setStatus("current")


class _Mc2200_FEMCLocalWANLink_Type(Integer32):
    """Custom type mc2200_FEMCLocalWANLink based on Integer32"""
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


_Mc2200_FEMCLocalWANLink_Type.__name__ = "Integer32"
_Mc2200_FEMCLocalWANLink_Object = MibTableColumn
mc2200_FEMCLocalWANLink = _Mc2200_FEMCLocalWANLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 5),
    _Mc2200_FEMCLocalWANLink_Type()
)
mc2200_FEMCLocalWANLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCLocalWANLink.setStatus("current")


class _Mc2200_FEMCLocalLANDownStreamBW_Type(Integer32):
    """Custom type mc2200_FEMCLocalLANDownStreamBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              35,
              40,
              45,
              50,
              55,
              60,
              65,
              70,
              75,
              80,
              85,
              90,
              95,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate35M", 35),
          ("rate40M", 40),
          ("rate45M", 45),
          ("rate50M", 50),
          ("rate55M", 55),
          ("rate60M", 60),
          ("rate65M", 65),
          ("rate70M", 70),
          ("rate75M", 75),
          ("rate80M", 80),
          ("rate85M", 85),
          ("rate90M", 90),
          ("rate95M", 95),
          ("rate100M", 100))
    )


_Mc2200_FEMCLocalLANDownStreamBW_Type.__name__ = "Integer32"
_Mc2200_FEMCLocalLANDownStreamBW_Object = MibTableColumn
mc2200_FEMCLocalLANDownStreamBW = _Mc2200_FEMCLocalLANDownStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 6),
    _Mc2200_FEMCLocalLANDownStreamBW_Type()
)
mc2200_FEMCLocalLANDownStreamBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FEMCLocalLANDownStreamBW.setStatus("current")


class _Mc2200_FEMCLocalLANUpStreamBW_Type(Integer32):
    """Custom type mc2200_FEMCLocalLANUpStreamBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              15,
              20,
              25,
              30,
              35,
              40,
              45,
              50,
              55,
              60,
              65,
              70,
              75,
              80,
              85,
              90,
              95,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("rate1M", 1),
          ("rate2M", 2),
          ("rate3M", 3),
          ("rate4M", 4),
          ("rate5M", 5),
          ("rate6M", 6),
          ("rate7M", 7),
          ("rate8M", 8),
          ("rate9M", 9),
          ("rate10M", 10),
          ("rate15M", 15),
          ("rate20M", 20),
          ("rate25M", 25),
          ("rate30M", 30),
          ("rate35M", 35),
          ("rate40M", 40),
          ("rate45M", 45),
          ("rate50M", 50),
          ("rate55M", 55),
          ("rate60M", 60),
          ("rate65M", 65),
          ("rate70M", 70),
          ("rate75M", 75),
          ("rate80M", 80),
          ("rate85M", 85),
          ("rate90M", 90),
          ("rate95M", 95),
          ("rate100M", 100))
    )


_Mc2200_FEMCLocalLANUpStreamBW_Type.__name__ = "Integer32"
_Mc2200_FEMCLocalLANUpStreamBW_Object = MibTableColumn
mc2200_FEMCLocalLANUpStreamBW = _Mc2200_FEMCLocalLANUpStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 7),
    _Mc2200_FEMCLocalLANUpStreamBW_Type()
)
mc2200_FEMCLocalLANUpStreamBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FEMCLocalLANUpStreamBW.setStatus("current")


class _Mc2200_FEMCLocalLANMode_Type(Integer32):
    """Custom type mc2200_FEMCLocalLANMode based on Integer32"""
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
        *(("mode100Base-FX-auto", 1),
          ("mode100Base-full", 2),
          ("mode100Base-Half", 3),
          ("mode10Base-full", 4),
          ("mode10Base-Half", 5))
    )


_Mc2200_FEMCLocalLANMode_Type.__name__ = "Integer32"
_Mc2200_FEMCLocalLANMode_Object = MibTableColumn
mc2200_FEMCLocalLANMode = _Mc2200_FEMCLocalLANMode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 8),
    _Mc2200_FEMCLocalLANMode_Type()
)
mc2200_FEMCLocalLANMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FEMCLocalLANMode.setStatus("current")
_Mc2200_FEMCRxGoodOctets_Type = Counter64
_Mc2200_FEMCRxGoodOctets_Object = MibTableColumn
mc2200_FEMCRxGoodOctets = _Mc2200_FEMCRxGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 9),
    _Mc2200_FEMCRxGoodOctets_Type()
)
mc2200_FEMCRxGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCRxGoodOctets.setStatus("current")
_Mc2200_FEMCRxBadOctets_Type = Counter64
_Mc2200_FEMCRxBadOctets_Object = MibTableColumn
mc2200_FEMCRxBadOctets = _Mc2200_FEMCRxBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 11),
    _Mc2200_FEMCRxBadOctets_Type()
)
mc2200_FEMCRxBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCRxBadOctets.setStatus("current")
_Mc2200_FEMCTxFCSErr_Type = Counter64
_Mc2200_FEMCTxFCSErr_Object = MibTableColumn
mc2200_FEMCTxFCSErr = _Mc2200_FEMCTxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 12),
    _Mc2200_FEMCTxFCSErr_Type()
)
mc2200_FEMCTxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCTxFCSErr.setStatus("current")
_Mc2200_FEMCRxUnicast_Type = Counter64
_Mc2200_FEMCRxUnicast_Object = MibTableColumn
mc2200_FEMCRxUnicast = _Mc2200_FEMCRxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 13),
    _Mc2200_FEMCRxUnicast_Type()
)
mc2200_FEMCRxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCRxUnicast.setStatus("current")
_Mc2200_FEMCTxDeferred_Type = Counter64
_Mc2200_FEMCTxDeferred_Object = MibTableColumn
mc2200_FEMCTxDeferred = _Mc2200_FEMCTxDeferred_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 14),
    _Mc2200_FEMCTxDeferred_Type()
)
mc2200_FEMCTxDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCTxDeferred.setStatus("current")
_Mc2200_FEMCRxBroadcasts_Type = Counter64
_Mc2200_FEMCRxBroadcasts_Object = MibTableColumn
mc2200_FEMCRxBroadcasts = _Mc2200_FEMCRxBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 15),
    _Mc2200_FEMCRxBroadcasts_Type()
)
mc2200_FEMCRxBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCRxBroadcasts.setStatus("current")
_Mc2200_FEMCRxMulticasts_Type = Counter64
_Mc2200_FEMCRxMulticasts_Object = MibTableColumn
mc2200_FEMCRxMulticasts = _Mc2200_FEMCRxMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 16),
    _Mc2200_FEMCRxMulticasts_Type()
)
mc2200_FEMCRxMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCRxMulticasts.setStatus("current")
_Mc2200_FEMCRx64Octets_Type = Counter64
_Mc2200_FEMCRx64Octets_Object = MibTableColumn
mc2200_FEMCRx64Octets = _Mc2200_FEMCRx64Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 17),
    _Mc2200_FEMCRx64Octets_Type()
)
mc2200_FEMCRx64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCRx64Octets.setStatus("current")
_Mc2200_FEMCRx65to127Octets_Type = Counter64
_Mc2200_FEMCRx65to127Octets_Object = MibTableColumn
mc2200_FEMCRx65to127Octets = _Mc2200_FEMCRx65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 18),
    _Mc2200_FEMCRx65to127Octets_Type()
)
mc2200_FEMCRx65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCRx65to127Octets.setStatus("current")
_Mc2200_FEMCRx128to255Octets_Type = Counter64
_Mc2200_FEMCRx128to255Octets_Object = MibTableColumn
mc2200_FEMCRx128to255Octets = _Mc2200_FEMCRx128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 19),
    _Mc2200_FEMCRx128to255Octets_Type()
)
mc2200_FEMCRx128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCRx128to255Octets.setStatus("current")
_Mc2200_FEMCRx256to511Octets_Type = Counter64
_Mc2200_FEMCRx256to511Octets_Object = MibTableColumn
mc2200_FEMCRx256to511Octets = _Mc2200_FEMCRx256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 20),
    _Mc2200_FEMCRx256to511Octets_Type()
)
mc2200_FEMCRx256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCRx256to511Octets.setStatus("current")
_Mc2200_FEMCRx512to1023Octets_Type = Counter64
_Mc2200_FEMCRx512to1023Octets_Object = MibTableColumn
mc2200_FEMCRx512to1023Octets = _Mc2200_FEMCRx512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 21),
    _Mc2200_FEMCRx512to1023Octets_Type()
)
mc2200_FEMCRx512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCRx512to1023Octets.setStatus("current")
_Mc2200_FEMCRx1024toMaxOctets_Type = Counter64
_Mc2200_FEMCRx1024toMaxOctets_Object = MibTableColumn
mc2200_FEMCRx1024toMaxOctets = _Mc2200_FEMCRx1024toMaxOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 22),
    _Mc2200_FEMCRx1024toMaxOctets_Type()
)
mc2200_FEMCRx1024toMaxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCRx1024toMaxOctets.setStatus("current")
_Mc2200_FEMCTxOctets_Type = Counter64
_Mc2200_FEMCTxOctets_Object = MibTableColumn
mc2200_FEMCTxOctets = _Mc2200_FEMCTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 23),
    _Mc2200_FEMCTxOctets_Type()
)
mc2200_FEMCTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCTxOctets.setStatus("current")
_Mc2200_FEMCTxUnicast_Type = Counter64
_Mc2200_FEMCTxUnicast_Object = MibTableColumn
mc2200_FEMCTxUnicast = _Mc2200_FEMCTxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 25),
    _Mc2200_FEMCTxUnicast_Type()
)
mc2200_FEMCTxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCTxUnicast.setStatus("current")
_Mc2200_FEMCTxExcessive_Type = Counter64
_Mc2200_FEMCTxExcessive_Object = MibTableColumn
mc2200_FEMCTxExcessive = _Mc2200_FEMCTxExcessive_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 26),
    _Mc2200_FEMCTxExcessive_Type()
)
mc2200_FEMCTxExcessive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCTxExcessive.setStatus("current")
_Mc2200_FEMCTxMulticasts_Type = Counter64
_Mc2200_FEMCTxMulticasts_Object = MibTableColumn
mc2200_FEMCTxMulticasts = _Mc2200_FEMCTxMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 27),
    _Mc2200_FEMCTxMulticasts_Type()
)
mc2200_FEMCTxMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCTxMulticasts.setStatus("current")
_Mc2200_FEMCTxBroadcasts_Type = Counter64
_Mc2200_FEMCTxBroadcasts_Object = MibTableColumn
mc2200_FEMCTxBroadcasts = _Mc2200_FEMCTxBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 28),
    _Mc2200_FEMCTxBroadcasts_Type()
)
mc2200_FEMCTxBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCTxBroadcasts.setStatus("current")
_Mc2200_FEMCTxSingle_Type = Counter64
_Mc2200_FEMCTxSingle_Object = MibTableColumn
mc2200_FEMCTxSingle = _Mc2200_FEMCTxSingle_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 29),
    _Mc2200_FEMCTxSingle_Type()
)
mc2200_FEMCTxSingle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCTxSingle.setStatus("current")
_Mc2200_FEMCTxPause_Type = Counter64
_Mc2200_FEMCTxPause_Object = MibTableColumn
mc2200_FEMCTxPause = _Mc2200_FEMCTxPause_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 30),
    _Mc2200_FEMCTxPause_Type()
)
mc2200_FEMCTxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCTxPause.setStatus("current")
_Mc2200_FEMCRxPause_Type = Counter64
_Mc2200_FEMCRxPause_Object = MibTableColumn
mc2200_FEMCRxPause = _Mc2200_FEMCRxPause_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 31),
    _Mc2200_FEMCRxPause_Type()
)
mc2200_FEMCRxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCRxPause.setStatus("current")
_Mc2200_FEMCTxMultiple_Type = Counter64
_Mc2200_FEMCTxMultiple_Object = MibTableColumn
mc2200_FEMCTxMultiple = _Mc2200_FEMCTxMultiple_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 32),
    _Mc2200_FEMCTxMultiple_Type()
)
mc2200_FEMCTxMultiple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCTxMultiple.setStatus("current")
_Mc2200_FEMCRxUndersize_Type = Counter64
_Mc2200_FEMCRxUndersize_Object = MibTableColumn
mc2200_FEMCRxUndersize = _Mc2200_FEMCRxUndersize_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 33),
    _Mc2200_FEMCRxUndersize_Type()
)
mc2200_FEMCRxUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCRxUndersize.setStatus("current")
_Mc2200_FEMCRxFragments_Type = Counter64
_Mc2200_FEMCRxFragments_Object = MibTableColumn
mc2200_FEMCRxFragments = _Mc2200_FEMCRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 34),
    _Mc2200_FEMCRxFragments_Type()
)
mc2200_FEMCRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCRxFragments.setStatus("current")
_Mc2200_FEMCRxOversize_Type = Counter64
_Mc2200_FEMCRxOversize_Object = MibTableColumn
mc2200_FEMCRxOversize = _Mc2200_FEMCRxOversize_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 35),
    _Mc2200_FEMCRxOversize_Type()
)
mc2200_FEMCRxOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCRxOversize.setStatus("current")
_Mc2200_FEMCRxJabber_Type = Counter64
_Mc2200_FEMCRxJabber_Object = MibTableColumn
mc2200_FEMCRxJabber = _Mc2200_FEMCRxJabber_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 36),
    _Mc2200_FEMCRxJabber_Type()
)
mc2200_FEMCRxJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCRxJabber.setStatus("current")
_Mc2200_FEMCRxErr_Type = Counter64
_Mc2200_FEMCRxErr_Object = MibTableColumn
mc2200_FEMCRxErr = _Mc2200_FEMCRxErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 37),
    _Mc2200_FEMCRxErr_Type()
)
mc2200_FEMCRxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCRxErr.setStatus("current")
_Mc2200_FEMCRxFCSErr_Type = Counter64
_Mc2200_FEMCRxFCSErr_Object = MibTableColumn
mc2200_FEMCRxFCSErr = _Mc2200_FEMCRxFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 38),
    _Mc2200_FEMCRxFCSErr_Type()
)
mc2200_FEMCRxFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCRxFCSErr.setStatus("current")
_Mc2200_FEMCTxCollisions_Type = Counter64
_Mc2200_FEMCTxCollisions_Object = MibTableColumn
mc2200_FEMCTxCollisions = _Mc2200_FEMCTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 39),
    _Mc2200_FEMCTxCollisions_Type()
)
mc2200_FEMCTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCTxCollisions.setStatus("current")
_Mc2200_FEMCTxLate_Type = Counter64
_Mc2200_FEMCTxLate_Object = MibTableColumn
mc2200_FEMCTxLate = _Mc2200_FEMCTxLate_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 40),
    _Mc2200_FEMCTxLate_Type()
)
mc2200_FEMCTxLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCTxLate.setStatus("current")
_Mc2200_FEMCRemoteLANSFPInfo_Type = DisplayString
_Mc2200_FEMCRemoteLANSFPInfo_Object = MibTableColumn
mc2200_FEMCRemoteLANSFPInfo = _Mc2200_FEMCRemoteLANSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 41),
    _Mc2200_FEMCRemoteLANSFPInfo_Type()
)
mc2200_FEMCRemoteLANSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCRemoteLANSFPInfo.setStatus("current")


class _Mc2200_FEMCRemoteLANLink_Type(Integer32):
    """Custom type mc2200_FEMCRemoteLANLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_FEMCRemoteLANLink_Type.__name__ = "Integer32"
_Mc2200_FEMCRemoteLANLink_Object = MibTableColumn
mc2200_FEMCRemoteLANLink = _Mc2200_FEMCRemoteLANLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 42),
    _Mc2200_FEMCRemoteLANLink_Type()
)
mc2200_FEMCRemoteLANLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCRemoteLANLink.setStatus("mandatory")
_Mc2200_FEMCRemoteWANSFPInfo_Type = DisplayString
_Mc2200_FEMCRemoteWANSFPInfo_Object = MibTableColumn
mc2200_FEMCRemoteWANSFPInfo = _Mc2200_FEMCRemoteWANSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 43),
    _Mc2200_FEMCRemoteWANSFPInfo_Type()
)
mc2200_FEMCRemoteWANSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCRemoteWANSFPInfo.setStatus("current")


class _Mc2200_FEMCRemoteWANLink_Type(Integer32):
    """Custom type mc2200_FEMCRemoteWANLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("up", 1),
          ("down", 2))
    )


_Mc2200_FEMCRemoteWANLink_Type.__name__ = "Integer32"
_Mc2200_FEMCRemoteWANLink_Object = MibTableColumn
mc2200_FEMCRemoteWANLink = _Mc2200_FEMCRemoteWANLink_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 44),
    _Mc2200_FEMCRemoteWANLink_Type()
)
mc2200_FEMCRemoteWANLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCRemoteWANLink.setStatus("current")


class _Mc2200_FEMCRemoteLANMode_Type(Integer32):
    """Custom type mc2200_FEMCRemoteLANMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("mode100Base-FX-auto", 1),
          ("mode100Base-full", 2),
          ("mode100Base-Half", 3),
          ("mode10Base-full", 4),
          ("mode10Base-Half", 5))
    )


_Mc2200_FEMCRemoteLANMode_Type.__name__ = "Integer32"
_Mc2200_FEMCRemoteLANMode_Object = MibTableColumn
mc2200_FEMCRemoteLANMode = _Mc2200_FEMCRemoteLANMode_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 45),
    _Mc2200_FEMCRemoteLANMode_Type()
)
mc2200_FEMCRemoteLANMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FEMCRemoteLANMode.setStatus("current")
_Mc2200_FEMCRemoteIPAddress_Type = IpAddress
_Mc2200_FEMCRemoteIPAddress_Object = MibTableColumn
mc2200_FEMCRemoteIPAddress = _Mc2200_FEMCRemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 46),
    _Mc2200_FEMCRemoteIPAddress_Type()
)
mc2200_FEMCRemoteIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FEMCRemoteIPAddress.setStatus("mandatory")
_Mc2200_FEMCRemoteSubnetMask_Type = IpAddress
_Mc2200_FEMCRemoteSubnetMask_Object = MibTableColumn
mc2200_FEMCRemoteSubnetMask = _Mc2200_FEMCRemoteSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 47),
    _Mc2200_FEMCRemoteSubnetMask_Type()
)
mc2200_FEMCRemoteSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FEMCRemoteSubnetMask.setStatus("mandatory")
_Mc2200_FEMCRemoteGateWay_Type = IpAddress
_Mc2200_FEMCRemoteGateWay_Object = MibTableColumn
mc2200_FEMCRemoteGateWay = _Mc2200_FEMCRemoteGateWay_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 48),
    _Mc2200_FEMCRemoteGateWay_Type()
)
mc2200_FEMCRemoteGateWay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FEMCRemoteGateWay.setStatus("mandatory")


class _Mc2200_FEMCRemoteVLANEnable_Type(Integer32):
    """Custom type mc2200_FEMCRemoteVLANEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("enable", 1),
          ("disable", 2))
    )


_Mc2200_FEMCRemoteVLANEnable_Type.__name__ = "Integer32"
_Mc2200_FEMCRemoteVLANEnable_Object = MibTableColumn
mc2200_FEMCRemoteVLANEnable = _Mc2200_FEMCRemoteVLANEnable_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 49),
    _Mc2200_FEMCRemoteVLANEnable_Type()
)
mc2200_FEMCRemoteVLANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FEMCRemoteVLANEnable.setStatus("mandatory")
_Mc2200_FEMCRemoteVID_Type = Integer32
_Mc2200_FEMCRemoteVID_Object = MibTableColumn
mc2200_FEMCRemoteVID = _Mc2200_FEMCRemoteVID_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 50),
    _Mc2200_FEMCRemoteVID_Type()
)
mc2200_FEMCRemoteVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FEMCRemoteVID.setStatus("mandatory")


class _Mc2200_FEMCRemoteAlarm_Type(Integer32):
    """Custom type mc2200_FEMCRemoteAlarm based on Integer32"""
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


_Mc2200_FEMCRemoteAlarm_Type.__name__ = "Integer32"
_Mc2200_FEMCRemoteAlarm_Object = MibTableColumn
mc2200_FEMCRemoteAlarm = _Mc2200_FEMCRemoteAlarm_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 51),
    _Mc2200_FEMCRemoteAlarm_Type()
)
mc2200_FEMCRemoteAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FEMCRemoteAlarm.setStatus("current")


class _Mc2200_FEMCRFD_Type(Integer32):
    """Custom type mc2200_FEMCRFD based on Integer32"""
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


_Mc2200_FEMCRFD_Type.__name__ = "Integer32"
_Mc2200_FEMCRFD_Object = MibTableColumn
mc2200_FEMCRFD = _Mc2200_FEMCRFD_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 52),
    _Mc2200_FEMCRFD_Type()
)
mc2200_FEMCRFD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FEMCRFD.setStatus("current")
_Mc2200_FEMCDefault_Type = Integer32
_Mc2200_FEMCDefault_Object = MibTableColumn
mc2200_FEMCDefault = _Mc2200_FEMCDefault_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 53),
    _Mc2200_FEMCDefault_Type()
)
mc2200_FEMCDefault.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mc2200_FEMCDefault.setStatus("current")
_Mc2200_FEMCReboot_Type = Integer32
_Mc2200_FEMCReboot_Object = MibTableColumn
mc2200_FEMCReboot = _Mc2200_FEMCReboot_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 54),
    _Mc2200_FEMCReboot_Type()
)
mc2200_FEMCReboot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mc2200_FEMCReboot.setStatus("current")


class _Mc2200_FEMCLocalLANSpeed_Type(Integer32):
    """Custom type mc2200_FEMCLocalLANSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed100M", 1),
          ("speed10M", 2),
          ("down", 3))
    )


_Mc2200_FEMCLocalLANSpeed_Type.__name__ = "Integer32"
_Mc2200_FEMCLocalLANSpeed_Object = MibTableColumn
mc2200_FEMCLocalLANSpeed = _Mc2200_FEMCLocalLANSpeed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 55),
    _Mc2200_FEMCLocalLANSpeed_Type()
)
mc2200_FEMCLocalLANSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCLocalLANSpeed.setStatus("mandatory")


class _Mc2200_FEMCRemoteLANSpeed_Type(Integer32):
    """Custom type mc2200_FEMCRemoteLANSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noremotecard", 0),
          ("speed100M", 1),
          ("speed10M", 2),
          ("down", 3))
    )


_Mc2200_FEMCRemoteLANSpeed_Type.__name__ = "Integer32"
_Mc2200_FEMCRemoteLANSpeed_Object = MibTableColumn
mc2200_FEMCRemoteLANSpeed = _Mc2200_FEMCRemoteLANSpeed_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 56),
    _Mc2200_FEMCRemoteLANSpeed_Type()
)
mc2200_FEMCRemoteLANSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCRemoteLANSpeed.setStatus("mandatory")
_Mc2200_FEMCLocalportuser_Type = DisplayString
_Mc2200_FEMCLocalportuser_Object = MibTableColumn
mc2200_FEMCLocalportuser = _Mc2200_FEMCLocalportuser_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 57),
    _Mc2200_FEMCLocalportuser_Type()
)
mc2200_FEMCLocalportuser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FEMCLocalportuser.setStatus("current")
_Mc2200_FEMCRemoteportuser_Type = DisplayString
_Mc2200_FEMCRemoteportuser_Object = MibTableColumn
mc2200_FEMCRemoteportuser = _Mc2200_FEMCRemoteportuser_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 58),
    _Mc2200_FEMCRemoteportuser_Type()
)
mc2200_FEMCRemoteportuser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FEMCRemoteportuser.setStatus("current")


class _Mc2200_FEMCWANOpticalPowerCheck_Type(Integer32):
    """Custom type mc2200_FEMCWANOpticalPowerCheck based on Integer32"""
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


_Mc2200_FEMCWANOpticalPowerCheck_Type.__name__ = "Integer32"
_Mc2200_FEMCWANOpticalPowerCheck_Object = MibTableColumn
mc2200_FEMCWANOpticalPowerCheck = _Mc2200_FEMCWANOpticalPowerCheck_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 59),
    _Mc2200_FEMCWANOpticalPowerCheck_Type()
)
mc2200_FEMCWANOpticalPowerCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FEMCWANOpticalPowerCheck.setStatus("current")


class _Mc2200_FEMCWANThreshold_Type(Integer32):
    """Custom type mc2200_FEMCWANThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71)
        )
    )
    namedValues = NamedValues(
        *(("db-32", 1),
          ("db-31dot5", 2),
          ("db-31", 3),
          ("db-30dot5", 4),
          ("db-30", 5),
          ("db-29dot5", 6),
          ("db-29", 7),
          ("db-28dot5", 8),
          ("db-28", 9),
          ("db-27dot5", 10),
          ("db-27", 11),
          ("db-26dot5", 12),
          ("db-26", 13),
          ("db-25dot5", 14),
          ("db-25", 15),
          ("db-24dot5", 16),
          ("db-24", 17),
          ("db-23dot5", 18),
          ("db-23", 19),
          ("db-22dot5", 20),
          ("db-22", 21),
          ("db-21dot5", 22),
          ("db-21", 23),
          ("db-20dot5", 24),
          ("db-20", 25),
          ("db-19dot5", 26),
          ("db-19", 27),
          ("db-18dot5", 28),
          ("db-18", 29),
          ("db-17dot5", 30),
          ("db-17", 31),
          ("db-16dot5", 32),
          ("db-16", 33),
          ("db-15dot5", 34),
          ("db-15", 35),
          ("db-14dot5", 36),
          ("db-14", 37),
          ("db-13dot5", 38),
          ("db-13", 39),
          ("db-12dot5", 40),
          ("db-12", 41),
          ("db-11dot5", 42),
          ("db-11", 43),
          ("db-10dot5", 44),
          ("db-10", 45),
          ("db-9dot5", 46),
          ("db-9", 47),
          ("db-8dot5", 48),
          ("db-8", 49),
          ("db-7dot5", 50),
          ("db-7", 51),
          ("db-6dot5", 52),
          ("db-6", 53),
          ("db-5dot5", 54),
          ("db-5", 55),
          ("db-4dot5", 56),
          ("db-4", 57),
          ("db-3dot5", 58),
          ("db-3", 59),
          ("db-2dot5", 60),
          ("db-2", 61),
          ("db-1dot5", 62),
          ("db-1", 63),
          ("db-0dot5", 64),
          ("db-0", 65),
          ("db0dot5", 66),
          ("db1", 67),
          ("db1dot5", 68),
          ("db2", 69),
          ("db2dot5", 70),
          ("db3", 71))
    )


_Mc2200_FEMCWANThreshold_Type.__name__ = "Integer32"
_Mc2200_FEMCWANThreshold_Object = MibTableColumn
mc2200_FEMCWANThreshold = _Mc2200_FEMCWANThreshold_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 60),
    _Mc2200_FEMCWANThreshold_Type()
)
mc2200_FEMCWANThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FEMCWANThreshold.setStatus("current")


class _Mc2200_FEMCTrapFilterLocalLAN_Type(Integer32):
    """Custom type mc2200_FEMCTrapFilterLocalLAN based on Integer32"""
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


_Mc2200_FEMCTrapFilterLocalLAN_Type.__name__ = "Integer32"
_Mc2200_FEMCTrapFilterLocalLAN_Object = MibTableColumn
mc2200_FEMCTrapFilterLocalLAN = _Mc2200_FEMCTrapFilterLocalLAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 61),
    _Mc2200_FEMCTrapFilterLocalLAN_Type()
)
mc2200_FEMCTrapFilterLocalLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FEMCTrapFilterLocalLAN.setStatus("current")


class _Mc2200_FEMCTrapFilterLocalWAN_Type(Integer32):
    """Custom type mc2200_FEMCTrapFilterLocalWAN based on Integer32"""
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


_Mc2200_FEMCTrapFilterLocalWAN_Type.__name__ = "Integer32"
_Mc2200_FEMCTrapFilterLocalWAN_Object = MibTableColumn
mc2200_FEMCTrapFilterLocalWAN = _Mc2200_FEMCTrapFilterLocalWAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 62),
    _Mc2200_FEMCTrapFilterLocalWAN_Type()
)
mc2200_FEMCTrapFilterLocalWAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FEMCTrapFilterLocalWAN.setStatus("current")


class _Mc2200_FEMCTrapFilterRemotePower_Type(Integer32):
    """Custom type mc2200_FEMCTrapFilterRemotePower based on Integer32"""
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


_Mc2200_FEMCTrapFilterRemotePower_Type.__name__ = "Integer32"
_Mc2200_FEMCTrapFilterRemotePower_Object = MibTableColumn
mc2200_FEMCTrapFilterRemotePower = _Mc2200_FEMCTrapFilterRemotePower_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 63),
    _Mc2200_FEMCTrapFilterRemotePower_Type()
)
mc2200_FEMCTrapFilterRemotePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FEMCTrapFilterRemotePower.setStatus("current")


class _Mc2200_FEMCTrapFilterRemoteLAN_Type(Integer32):
    """Custom type mc2200_FEMCTrapFilterRemoteLAN based on Integer32"""
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


_Mc2200_FEMCTrapFilterRemoteLAN_Type.__name__ = "Integer32"
_Mc2200_FEMCTrapFilterRemoteLAN_Object = MibTableColumn
mc2200_FEMCTrapFilterRemoteLAN = _Mc2200_FEMCTrapFilterRemoteLAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 64),
    _Mc2200_FEMCTrapFilterRemoteLAN_Type()
)
mc2200_FEMCTrapFilterRemoteLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FEMCTrapFilterRemoteLAN.setStatus("current")


class _Mc2200_FEMCTrapFilterRemoteWAN_Type(Integer32):
    """Custom type mc2200_FEMCTrapFilterRemoteWAN based on Integer32"""
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


_Mc2200_FEMCTrapFilterRemoteWAN_Type.__name__ = "Integer32"
_Mc2200_FEMCTrapFilterRemoteWAN_Object = MibTableColumn
mc2200_FEMCTrapFilterRemoteWAN = _Mc2200_FEMCTrapFilterRemoteWAN_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 65),
    _Mc2200_FEMCTrapFilterRemoteWAN_Type()
)
mc2200_FEMCTrapFilterRemoteWAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FEMCTrapFilterRemoteWAN.setStatus("current")


class _Mc2200_FEMCLoopback_Type(Integer32):
    """Custom type mc2200_FEMCLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("local_lanouter", 2),
          ("local_laninner", 3),
          ("local_wanouter", 4),
          ("local_waninner", 5),
          ("remote_lanouter", 6),
          ("remote_laninner", 7))
    )


_Mc2200_FEMCLoopback_Type.__name__ = "Integer32"
_Mc2200_FEMCLoopback_Object = MibTableColumn
mc2200_FEMCLoopback = _Mc2200_FEMCLoopback_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 66),
    _Mc2200_FEMCLoopback_Type()
)
mc2200_FEMCLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mc2200_FEMCLoopback.setStatus("mandatory")
_Mc2200_FEMCCardType_Type = DisplayString
_Mc2200_FEMCCardType_Object = MibTableColumn
mc2200_FEMCCardType = _Mc2200_FEMCCardType_Object(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 3, 20, 1, 67),
    _Mc2200_FEMCCardType_Type()
)
mc2200_FEMCCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mc2200_FEMCCardType.setStatus("current")

# Managed Objects groups


# Notification objects

mc2200_card_PlugIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 1)
)
if mibBuilder.loadTexts:
    mc2200_card_PlugIn.setStatus(
        ""
    )

mc2200_card_PullOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 2)
)
if mibBuilder.loadTexts:
    mc2200_card_PullOut.setStatus(
        ""
    )

mc2200_card_Local_Tx_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 3)
)
if mibBuilder.loadTexts:
    mc2200_card_Local_Tx_Up.setStatus(
        ""
    )

mc2200_card_Local_Tx_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 4)
)
if mibBuilder.loadTexts:
    mc2200_card_Local_Tx_Down.setStatus(
        ""
    )

mc2200_card_Local_Fx_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 5)
)
if mibBuilder.loadTexts:
    mc2200_card_Local_Fx_Up.setStatus(
        ""
    )

mc2200_card_Local_Fx_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 6)
)
if mibBuilder.loadTexts:
    mc2200_card_Local_Fx_Down.setStatus(
        ""
    )

mc2200_card_Remote_Power_On = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 7)
)
if mibBuilder.loadTexts:
    mc2200_card_Remote_Power_On.setStatus(
        ""
    )

mc2200_card_Remote_Power_Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 8)
)
if mibBuilder.loadTexts:
    mc2200_card_Remote_Power_Off.setStatus(
        ""
    )

mc2200_card_Remote_Tx_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 9)
)
if mibBuilder.loadTexts:
    mc2200_card_Remote_Tx_Up.setStatus(
        ""
    )

mc2200_card_Remote_Tx_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 10)
)
if mibBuilder.loadTexts:
    mc2200_card_Remote_Tx_Down.setStatus(
        ""
    )

mc2200_chassis_Power_A_Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 11)
)
if mibBuilder.loadTexts:
    mc2200_chassis_Power_A_Active.setStatus(
        ""
    )

mc2200_chassis_Power_A_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 12)
)
if mibBuilder.loadTexts:
    mc2200_chassis_Power_A_Down.setStatus(
        ""
    )

mc2200_chassis_Power_A_Standby = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 13)
)
if mibBuilder.loadTexts:
    mc2200_chassis_Power_A_Standby.setStatus(
        ""
    )

mc2200_chassis_Power_B_Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 14)
)
if mibBuilder.loadTexts:
    mc2200_chassis_Power_B_Active.setStatus(
        ""
    )

mc2200_chassis_Power_B_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 15)
)
if mibBuilder.loadTexts:
    mc2200_chassis_Power_B_Down.setStatus(
        ""
    )

mc2200_chassis_Power_B_Standby = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 16)
)
if mibBuilder.loadTexts:
    mc2200_chassis_Power_B_Standby.setStatus(
        ""
    )

mc2200_chassis_Fan_A_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 17)
)
if mibBuilder.loadTexts:
    mc2200_chassis_Fan_A_Up.setStatus(
        ""
    )

mc2200_chassis_Fan_A_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 18)
)
if mibBuilder.loadTexts:
    mc2200_chassis_Fan_A_Down.setStatus(
        ""
    )

mc2200_chassis_Fan_B_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 19)
)
if mibBuilder.loadTexts:
    mc2200_chassis_Fan_B_Up.setStatus(
        ""
    )

mc2200_chassis_Fan_B_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 20)
)
if mibBuilder.loadTexts:
    mc2200_chassis_Fan_B_Down.setStatus(
        ""
    )

mc2200_chassis_Connected = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 21)
)
if mibBuilder.loadTexts:
    mc2200_chassis_Connected.setStatus(
        ""
    )

mc2200_chassis_Disconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 22)
)
if mibBuilder.loadTexts:
    mc2200_chassis_Disconnected.setStatus(
        ""
    )

mc2200_GEMux8_local_WAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 23)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_local_WAN_linkup.setStatus(
        ""
    )

mc2200_GEMux8_local_WAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 24)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_local_WAN_linkdown.setStatus(
        ""
    )

mc2200_GEMux8_local_LAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 25)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_local_LAN_linkup.setStatus(
        ""
    )

mc2200_GEMux8_local_LAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 26)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_local_LAN_linkdown.setStatus(
        ""
    )

mc2200_GEMux8_local_PORT1_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 27)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_local_PORT1_linkup.setStatus(
        ""
    )

mc2200_GEMux8_local_PORT1_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 28)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_local_PORT1_linkdown.setStatus(
        ""
    )

mc2200_GEMux8_local_PORT2_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 29)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_local_PORT2_linkup.setStatus(
        ""
    )

mc2200_GEMux8_local_PORT2_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 30)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_local_PORT2_linkdown.setStatus(
        ""
    )

mc2200_GEMux8_local_PORT3_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 31)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_local_PORT3_linkup.setStatus(
        ""
    )

mc2200_GEMux8_local_PORT3_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 32)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_local_PORT3_linkdown.setStatus(
        ""
    )

mc2200_GEMux8_local_PORT4_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 33)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_local_PORT4_linkup.setStatus(
        ""
    )

mc2200_GEMux8_local_PORT4_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 34)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_local_PORT4_linkdown.setStatus(
        ""
    )

mc2200_GEMux8_local_PORT5_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 35)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_local_PORT5_linkup.setStatus(
        ""
    )

mc2200_GEMux8_local_PORT5_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 36)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_local_PORT5_linkdown.setStatus(
        ""
    )

mc2200_GEMux8_local_PORT6_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 37)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_local_PORT6_linkup.setStatus(
        ""
    )

mc2200_GEMux8_local_PORT6_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 38)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_local_PORT6_linkdown.setStatus(
        ""
    )

mc2200_GEMux8_local_PORT7_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 39)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_local_PORT7_linkup.setStatus(
        ""
    )

mc2200_GEMux8_local_PORT7_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 40)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_local_PORT7_linkdown.setStatus(
        ""
    )

mc2200_GEMux8_local_PORT8_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 41)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_local_PORT8_linkup.setStatus(
        ""
    )

mc2200_GEMux8_local_PORT8_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 42)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_local_PORT8_linkdown.setStatus(
        ""
    )

mc2200_GEMux8_remote_LAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 43)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_remote_LAN_linkup.setStatus(
        ""
    )

mc2200_GEMux8_remote_LAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 44)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_remote_LAN_linkdown.setStatus(
        ""
    )

mc2200_GEMux8_remote_PORT1_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 45)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_remote_PORT1_linkup.setStatus(
        ""
    )

mc2200_GEMux8_remote_PORT1_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 46)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_remote_PORT1_linkdown.setStatus(
        ""
    )

mc2200_GEMux8_remote_PORT2_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 47)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_remote_PORT2_linkup.setStatus(
        ""
    )

mc2200_GEMux8_remote_PORT2_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 48)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_remote_PORT2_linkdown.setStatus(
        ""
    )

mc2200_GEMux8_remote_PORT3_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 49)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_remote_PORT3_linkup.setStatus(
        ""
    )

mc2200_GEMux8_remote_PORT3_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 50)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_remote_PORT3_linkdown.setStatus(
        ""
    )

mc2200_GEMux8_remote_PORT4_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 51)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_remote_PORT4_linkup.setStatus(
        ""
    )

mc2200_GEMux8_remote_PORT4_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 52)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_remote_PORT4_linkdown.setStatus(
        ""
    )

mc2200_GEMux8_remote_PORT5_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 53)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_remote_PORT5_linkup.setStatus(
        ""
    )

mc2200_GEMux8_remote_PORT5_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 54)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_remote_PORT5_linkdown.setStatus(
        ""
    )

mc2200_GEMux8_remote_PORT6_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 55)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_remote_PORT6_linkup.setStatus(
        ""
    )

mc2200_GEMux8_remote_PORT6_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 56)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_remote_PORT6_linkdown.setStatus(
        ""
    )

mc2200_GEMux8_remote_PORT7_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 57)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_remote_PORT7_linkup.setStatus(
        ""
    )

mc2200_GEMux8_remote_PORT7_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 58)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_remote_PORT7_linkdown.setStatus(
        ""
    )

mc2200_GEMux8_remote_PORT8_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 59)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_remote_PORT8_linkup.setStatus(
        ""
    )

mc2200_GEMux8_remote_PORT8_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 60)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_remote_PORT8_linkdown.setStatus(
        ""
    )

mc2200_GEMux8_remote_PORT9_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 61)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_remote_PORT9_linkup.setStatus(
        ""
    )

mc2200_GEMux8_remote_PORT9_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 62)
)
if mibBuilder.loadTexts:
    mc2200_GEMux8_remote_PORT9_linkdown.setStatus(
        ""
    )

mc2200_chassis_Power_Card_PlugIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 63)
)
if mibBuilder.loadTexts:
    mc2200_chassis_Power_Card_PlugIn.setStatus(
        ""
    )

mc2200_chassis_Power_Card_Removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 64)
)
if mibBuilder.loadTexts:
    mc2200_chassis_Power_Card_Removed.setStatus(
        ""
    )

mc2200_card_Remote_PowerA_Up_PowerB_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 65)
)
if mibBuilder.loadTexts:
    mc2200_card_Remote_PowerA_Up_PowerB_Down.setStatus(
        ""
    )

mc2200_card_Remote_PowerA_Down_PowerB_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 66)
)
if mibBuilder.loadTexts:
    mc2200_card_Remote_PowerA_Down_PowerB_Up.setStatus(
        ""
    )

mc2200_GEMC_local_LAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 67)
)
if mibBuilder.loadTexts:
    mc2200_GEMC_local_LAN_linkup.setStatus(
        ""
    )

mc2200_GEMC_local_LAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 68)
)
if mibBuilder.loadTexts:
    mc2200_GEMC_local_LAN_linkdown.setStatus(
        ""
    )

mc2200_GEMC_local_WAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 69)
)
if mibBuilder.loadTexts:
    mc2200_GEMC_local_WAN_linkup.setStatus(
        ""
    )

mc2200_GEMC_local_WAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 70)
)
if mibBuilder.loadTexts:
    mc2200_GEMC_local_WAN_linkdown.setStatus(
        ""
    )

mc2200_GEMC_remote_LAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 71)
)
if mibBuilder.loadTexts:
    mc2200_GEMC_remote_LAN_linkup.setStatus(
        ""
    )

mc2200_GEMC_remote_LAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 72)
)
if mibBuilder.loadTexts:
    mc2200_GEMC_remote_LAN_linkdown.setStatus(
        ""
    )

mc2200_GEMC4_local_LAN1_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 73)
)
if mibBuilder.loadTexts:
    mc2200_GEMC4_local_LAN1_linkup.setStatus(
        ""
    )

mc2200_GEMC4_local_LAN1_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 74)
)
if mibBuilder.loadTexts:
    mc2200_GEMC4_local_LAN1_linkdown.setStatus(
        ""
    )

mc2200_GEMC4_local_LAN2_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 75)
)
if mibBuilder.loadTexts:
    mc2200_GEMC4_local_LAN2_linkup.setStatus(
        ""
    )

mc2200_GEMC4_local_LAN2_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 76)
)
if mibBuilder.loadTexts:
    mc2200_GEMC4_local_LAN2_linkdown.setStatus(
        ""
    )

mc2200_GEMC4_local_WAN2LAN3_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 77)
)
if mibBuilder.loadTexts:
    mc2200_GEMC4_local_WAN2LAN3_linkup.setStatus(
        ""
    )

mc2200_GEMC4_local_WAN2LAN3_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 78)
)
if mibBuilder.loadTexts:
    mc2200_GEMC4_local_WAN2LAN3_linkdown.setStatus(
        ""
    )

mc2200_GEMC4_local_WAN1_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 79)
)
if mibBuilder.loadTexts:
    mc2200_GEMC4_local_WAN1_linkup.setStatus(
        ""
    )

mc2200_GEMC4_local_WAN1_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 80)
)
if mibBuilder.loadTexts:
    mc2200_GEMC4_local_WAN1_linkdown.setStatus(
        ""
    )

mc2200_GEMC4_remote_LAN1_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 81)
)
if mibBuilder.loadTexts:
    mc2200_GEMC4_remote_LAN1_linkup.setStatus(
        ""
    )

mc2200_GEMC4_remote_LAN1_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 82)
)
if mibBuilder.loadTexts:
    mc2200_GEMC4_remote_LAN1_linkdown.setStatus(
        ""
    )

mc2200_GEMC4_remote_LAN2_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 83)
)
if mibBuilder.loadTexts:
    mc2200_GEMC4_remote_LAN2_linkup.setStatus(
        ""
    )

mc2200_GEMC4_remote_LAN2_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 84)
)
if mibBuilder.loadTexts:
    mc2200_GEMC4_remote_LAN2_linkdown.setStatus(
        ""
    )

mc2200_GEMC4_remote_WAN2LAN3_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 85)
)
if mibBuilder.loadTexts:
    mc2200_GEMC4_remote_WAN2LAN3_linkup.setStatus(
        ""
    )

mc2200_GEMC4_remote_WAN2LAN3_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 86)
)
if mibBuilder.loadTexts:
    mc2200_GEMC4_remote_WAN2LAN3_linkdown.setStatus(
        ""
    )

mc2200_GEMC2_local_LAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 97)
)
if mibBuilder.loadTexts:
    mc2200_GEMC2_local_LAN_linkup.setStatus(
        ""
    )

mc2200_GEMC2_local_LAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 98)
)
if mibBuilder.loadTexts:
    mc2200_GEMC2_local_LAN_linkdown.setStatus(
        ""
    )

mc2200_GEMC2_local_WAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 99)
)
if mibBuilder.loadTexts:
    mc2200_GEMC2_local_WAN_linkup.setStatus(
        ""
    )

mc2200_GEMC2_local_WAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 100)
)
if mibBuilder.loadTexts:
    mc2200_GEMC2_local_WAN_linkdown.setStatus(
        ""
    )

mc2200_GEMC2_remote_LAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 101)
)
if mibBuilder.loadTexts:
    mc2200_GEMC2_remote_LAN_linkup.setStatus(
        ""
    )

mc2200_GEMC2_remote_LAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 102)
)
if mibBuilder.loadTexts:
    mc2200_GEMC2_remote_LAN_linkdown.setStatus(
        ""
    )

mc2200_GEMC2E_local_LAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 103)
)
if mibBuilder.loadTexts:
    mc2200_GEMC2E_local_LAN_linkup.setStatus(
        ""
    )

mc2200_GEMC2E_local_LAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 104)
)
if mibBuilder.loadTexts:
    mc2200_GEMC2E_local_LAN_linkdown.setStatus(
        ""
    )

mc2200_GEMC2E_local_WAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 105)
)
if mibBuilder.loadTexts:
    mc2200_GEMC2E_local_WAN_linkup.setStatus(
        ""
    )

mc2200_GEMC2E_local_WAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 106)
)
if mibBuilder.loadTexts:
    mc2200_GEMC2E_local_WAN_linkdown.setStatus(
        ""
    )

mc2200_GEMC2E_remote_LAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 107)
)
if mibBuilder.loadTexts:
    mc2200_GEMC2E_remote_LAN_linkup.setStatus(
        ""
    )

mc2200_GEMC2E_remote_LAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 108)
)
if mibBuilder.loadTexts:
    mc2200_GEMC2E_remote_LAN_linkdown.setStatus(
        ""
    )

mc2200_GE_FE_MC_local_LAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 109)
)
if mibBuilder.loadTexts:
    mc2200_GE_FE_MC_local_LAN_linkup.setStatus(
        ""
    )

mc2200_GE_FE_MC_local_LAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 110)
)
if mibBuilder.loadTexts:
    mc2200_GE_FE_MC_local_LAN_linkdown.setStatus(
        ""
    )

mc2200_GE_FE_MC_local_WAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 111)
)
if mibBuilder.loadTexts:
    mc2200_GE_FE_MC_local_WAN_linkup.setStatus(
        ""
    )

mc2200_GE_FE_MC_local_WAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 112)
)
if mibBuilder.loadTexts:
    mc2200_GE_FE_MC_local_WAN_linkdown.setStatus(
        ""
    )

mc2200_GE_FE_MC_remote_LAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 113)
)
if mibBuilder.loadTexts:
    mc2200_GE_FE_MC_remote_LAN_linkup.setStatus(
        ""
    )

mc2200_GE_FE_MC_remote_LAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 114)
)
if mibBuilder.loadTexts:
    mc2200_GE_FE_MC_remote_LAN_linkdown.setStatus(
        ""
    )

mc2200_GE_FE_MC2S_local_LAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 115)
)
if mibBuilder.loadTexts:
    mc2200_GE_FE_MC2S_local_LAN_linkup.setStatus(
        ""
    )

mc2200_GE_FE_MC2S_local_LAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 116)
)
if mibBuilder.loadTexts:
    mc2200_GE_FE_MC2S_local_LAN_linkdown.setStatus(
        ""
    )

mc2200_GE_FE_MC2S_local_WAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 117)
)
if mibBuilder.loadTexts:
    mc2200_GE_FE_MC2S_local_WAN_linkup.setStatus(
        ""
    )

mc2200_GE_FE_MC2S_local_WAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 118)
)
if mibBuilder.loadTexts:
    mc2200_GE_FE_MC2S_local_WAN_linkdown.setStatus(
        ""
    )

mc2200_GE_FE_MC2S_remote_LAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 119)
)
if mibBuilder.loadTexts:
    mc2200_GE_FE_MC2S_remote_LAN_linkup.setStatus(
        ""
    )

mc2200_GE_FE_MC2S_remote_LAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 120)
)
if mibBuilder.loadTexts:
    mc2200_GE_FE_MC2S_remote_LAN_linkdown.setStatus(
        ""
    )

mc2200_GE_FE_MC2T_local_LAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 121)
)
if mibBuilder.loadTexts:
    mc2200_GE_FE_MC2T_local_LAN_linkup.setStatus(
        ""
    )

mc2200_GE_FE_MC2T_local_LAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 122)
)
if mibBuilder.loadTexts:
    mc2200_GE_FE_MC2T_local_LAN_linkdown.setStatus(
        ""
    )

mc2200_GE_FE_MC2T_local_WAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 123)
)
if mibBuilder.loadTexts:
    mc2200_GE_FE_MC2T_local_WAN_linkup.setStatus(
        ""
    )

mc2200_GE_FE_MC2T_local_WAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 124)
)
if mibBuilder.loadTexts:
    mc2200_GE_FE_MC2T_local_WAN_linkdown.setStatus(
        ""
    )

mc2200_GE_FE_MC2T_remote_LAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 125)
)
if mibBuilder.loadTexts:
    mc2200_GE_FE_MC2T_remote_LAN_linkup.setStatus(
        ""
    )

mc2200_GE_FE_MC2T_remote_LAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 126)
)
if mibBuilder.loadTexts:
    mc2200_GE_FE_MC2T_remote_LAN_linkdown.setStatus(
        ""
    )

mc2200_FE_SFP_local_LAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 127)
)
if mibBuilder.loadTexts:
    mc2200_FE_SFP_local_LAN_linkup.setStatus(
        ""
    )

mc2200_FE_SFP_local_LAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 128)
)
if mibBuilder.loadTexts:
    mc2200_FE_SFP_local_LAN_linkdown.setStatus(
        ""
    )

mc2200_FE_SFP_local_WAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 129)
)
if mibBuilder.loadTexts:
    mc2200_FE_SFP_local_WAN_linkup.setStatus(
        ""
    )

mc2200_FE_SFP_local_WAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 130)
)
if mibBuilder.loadTexts:
    mc2200_FE_SFP_local_WAN_linkdown.setStatus(
        ""
    )

mc2200_FE_SFP_remote_LAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 131)
)
if mibBuilder.loadTexts:
    mc2200_FE_SFP_remote_LAN_linkup.setStatus(
        ""
    )

mc2200_FE_SFP_remote_LAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 132)
)
if mibBuilder.loadTexts:
    mc2200_FE_SFP_remote_LAN_linkdown.setStatus(
        ""
    )

mc2200_GE_SFP_local_LAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 133)
)
if mibBuilder.loadTexts:
    mc2200_GE_SFP_local_LAN_linkup.setStatus(
        ""
    )

mc2200_GE_SFP_local_LAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 134)
)
if mibBuilder.loadTexts:
    mc2200_GE_SFP_local_LAN_linkdown.setStatus(
        ""
    )

mc2200_GE_SFP_local_WAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 135)
)
if mibBuilder.loadTexts:
    mc2200_GE_SFP_local_WAN_linkup.setStatus(
        ""
    )

mc2200_GE_SFP_local_WAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 136)
)
if mibBuilder.loadTexts:
    mc2200_GE_SFP_local_WAN_linkdown.setStatus(
        ""
    )

mc2200_GE_SFP_remote_LAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 137)
)
if mibBuilder.loadTexts:
    mc2200_GE_SFP_remote_LAN_linkup.setStatus(
        ""
    )

mc2200_GE_SFP_remote_LAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 138)
)
if mibBuilder.loadTexts:
    mc2200_GE_SFP_remote_LAN_linkdown.setStatus(
        ""
    )

mc2200_GE_MC3_local_LAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 139)
)
if mibBuilder.loadTexts:
    mc2200_GE_MC3_local_LAN_linkup.setStatus(
        ""
    )

mc2200_GE_MC3_local_LAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 140)
)
if mibBuilder.loadTexts:
    mc2200_GE_MC3_local_LAN_linkdown.setStatus(
        ""
    )

mc2200_GE_MC3_local_WAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 141)
)
if mibBuilder.loadTexts:
    mc2200_GE_MC3_local_WAN_linkup.setStatus(
        ""
    )

mc2200_GE_MC3_local_WAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 142)
)
if mibBuilder.loadTexts:
    mc2200_GE_MC3_local_WAN_linkdown.setStatus(
        ""
    )

mc2200_GE_MC3_remote_LAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 143)
)
if mibBuilder.loadTexts:
    mc2200_GE_MC3_remote_LAN_linkup.setStatus(
        ""
    )

mc2200_GE_MC3_remote_LAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 144)
)
if mibBuilder.loadTexts:
    mc2200_GE_MC3_remote_LAN_linkdown.setStatus(
        ""
    )

mc2200_GE_SFP_APS_local_LAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 145)
)
if mibBuilder.loadTexts:
    mc2200_GE_SFP_APS_local_LAN_linkup.setStatus(
        ""
    )

mc2200_GE_SFP_APS_local_LAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 146)
)
if mibBuilder.loadTexts:
    mc2200_GE_SFP_APS_local_LAN_linkdown.setStatus(
        ""
    )

mc2200_GE_SFP_APS_local_WAN1_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 147)
)
if mibBuilder.loadTexts:
    mc2200_GE_SFP_APS_local_WAN1_linkup.setStatus(
        ""
    )

mc2200_GE_SFP_APS_local_WAN1_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 148)
)
if mibBuilder.loadTexts:
    mc2200_GE_SFP_APS_local_WAN1_linkdown.setStatus(
        ""
    )

mc2200_GE_SFP_APS_local_WAN2_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 149)
)
if mibBuilder.loadTexts:
    mc2200_GE_SFP_APS_local_WAN2_linkup.setStatus(
        ""
    )

mc2200_GE_SFP_APS_local_WAN2_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 150)
)
if mibBuilder.loadTexts:
    mc2200_GE_SFP_APS_local_WAN2_linkdown.setStatus(
        ""
    )

mc2200_GE_SFP_APS_remote_LAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 151)
)
if mibBuilder.loadTexts:
    mc2200_GE_SFP_APS_remote_LAN_linkup.setStatus(
        ""
    )

mc2200_GE_SFP_APS_remote_LAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 152)
)
if mibBuilder.loadTexts:
    mc2200_GE_SFP_APS_remote_LAN_linkdown.setStatus(
        ""
    )

mc2200_GE_MC_APS_local_LAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 153)
)
if mibBuilder.loadTexts:
    mc2200_GE_MC_APS_local_LAN_linkup.setStatus(
        ""
    )

mc2200_GE_MC_APS_local_LAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 154)
)
if mibBuilder.loadTexts:
    mc2200_GE_MC_APS_local_LAN_linkdown.setStatus(
        ""
    )

mc2200_GE_MC_APS_local_WAN1_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 155)
)
if mibBuilder.loadTexts:
    mc2200_GE_MC_APS_local_WAN1_linkup.setStatus(
        ""
    )

mc2200_GE_MC_APS_local_WAN1_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 156)
)
if mibBuilder.loadTexts:
    mc2200_GE_MC_APS_local_WAN1_linkdown.setStatus(
        ""
    )

mc2200_GE_MC_APS_local_WAN2_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 157)
)
if mibBuilder.loadTexts:
    mc2200_GE_MC_APS_local_WAN2_linkup.setStatus(
        ""
    )

mc2200_GE_MC_APS_local_WAN2_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 158)
)
if mibBuilder.loadTexts:
    mc2200_GE_MC_APS_local_WAN2_linkdown.setStatus(
        ""
    )

mc2200_GE_MC_APS_remote_LAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 159)
)
if mibBuilder.loadTexts:
    mc2200_GE_MC_APS_remote_LAN_linkup.setStatus(
        ""
    )

mc2200_GE_MC_APS_remote_LAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 160)
)
if mibBuilder.loadTexts:
    mc2200_GE_MC_APS_remote_LAN_linkdown.setStatus(
        ""
    )

mc2200_CARD_WAN1_switch_WAN2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 161)
)
if mibBuilder.loadTexts:
    mc2200_CARD_WAN1_switch_WAN2.setStatus(
        ""
    )

mc2200_CARD_WAN2_switch_WAN1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 162)
)
if mibBuilder.loadTexts:
    mc2200_CARD_WAN2_switch_WAN1.setStatus(
        ""
    )

mc2200_OAPS_local_LAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 163)
)
if mibBuilder.loadTexts:
    mc2200_OAPS_local_LAN_linkup.setStatus(
        ""
    )

mc2200_OAPS_local_LAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 164)
)
if mibBuilder.loadTexts:
    mc2200_OAPS_local_LAN_linkdown.setStatus(
        ""
    )

mc2200_OAPS_local_WAN1_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 165)
)
if mibBuilder.loadTexts:
    mc2200_OAPS_local_WAN1_linkup.setStatus(
        ""
    )

mc2200_OAPS_local_WAN1_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 166)
)
if mibBuilder.loadTexts:
    mc2200_OAPS_local_WAN1_linkdown.setStatus(
        ""
    )

mc2200_OAPS_local_WAN2_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 167)
)
if mibBuilder.loadTexts:
    mc2200_OAPS_local_WAN2_linkup.setStatus(
        ""
    )

mc2200_OAPS_local_WAN2_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 168)
)
if mibBuilder.loadTexts:
    mc2200_OAPS_local_WAN2_linkdown.setStatus(
        ""
    )

mc2200_PORT_RX_POWER_LOW = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 169)
)
if mibBuilder.loadTexts:
    mc2200_PORT_RX_POWER_LOW.setStatus(
        ""
    )

mc2200_PORT_RX_POWER_NORMAL = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 170)
)
if mibBuilder.loadTexts:
    mc2200_PORT_RX_POWER_NORMAL.setStatus(
        ""
    )

mc2200_QS2204_local_LAN1_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 171)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_LAN1_linkup.setStatus(
        ""
    )

mc2200_QS2204_local_LAN1_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 172)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_LAN1_linkdown.setStatus(
        ""
    )

mc2200_QS2204_local_LAN2_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 173)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_LAN2_linkup.setStatus(
        ""
    )

mc2200_QS2204_local_LAN2_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 174)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_LAN2_linkdown.setStatus(
        ""
    )

mc2200_QS2204_local_LAN3_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 175)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_LAN3_linkup.setStatus(
        ""
    )

mc2200_QS2204_local_LAN3_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 176)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_LAN3_linkdown.setStatus(
        ""
    )

mc2200_QS2204_local_LAN4_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 177)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_LAN4_linkup.setStatus(
        ""
    )

mc2200_QS2204_local_LAN4_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 178)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_LAN4_linkdown.setStatus(
        ""
    )

mc2200_QS2204_local_WAN_lane1_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 179)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_WAN_lane1_linkup.setStatus(
        ""
    )

mc2200_QS2204_local_WAN_lane1_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 180)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_WAN_lane1_linkdown.setStatus(
        ""
    )

mc2200_QS2204_local_WAN_lane2_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 181)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_WAN_lane2_linkup.setStatus(
        ""
    )

mc2200_QS2204_local_WAN_lane2_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 182)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_WAN_lane2_linkdown.setStatus(
        ""
    )

mc2200_QS2204_local_WAN_lane3_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 183)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_WAN_lane3_linkup.setStatus(
        ""
    )

mc2200_QS2204_local_WAN_lane3_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 184)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_WAN_lane3_linkdown.setStatus(
        ""
    )

mc2200_QS2204_local_WAN_lane4_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 185)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_WAN_lane4_linkup.setStatus(
        ""
    )

mc2200_QS2204_local_WAN_lane4_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 186)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_WAN_lane4_linkdown.setStatus(
        ""
    )

mc2200_QS2204_local_LAN1_txup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 187)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_LAN1_txup.setStatus(
        ""
    )

mc2200_QS2204_local_LAN1_txdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 188)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_LAN1_txdown.setStatus(
        ""
    )

mc2200_QS2204_local_LAN2_txup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 189)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_LAN2_txup.setStatus(
        ""
    )

mc2200_QS2204_local_LAN2_txdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 190)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_LAN2_txdown.setStatus(
        ""
    )

mc2200_QS2204_local_LAN3_txkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 191)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_LAN3_txkup.setStatus(
        ""
    )

mc2200_QS2204_local_LAN3_txdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 192)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_LAN3_txdown.setStatus(
        ""
    )

mc2200_QS2204_local_LAN4_txup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 193)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_LAN4_txup.setStatus(
        ""
    )

mc2200_QS2204_local_LAN4_txdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 194)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_LAN4_txdown.setStatus(
        ""
    )

mc2200_QS2204_local_WAN_lane1_txup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 195)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_WAN_lane1_txup.setStatus(
        ""
    )

mc2200_QS2204_local_WAN_lane1_txdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 196)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_WAN_lane1_txdown.setStatus(
        ""
    )

mc2200_QS2204_local_WAN_lane2_txup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 197)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_WAN_lane2_txup.setStatus(
        ""
    )

mc2200_QS2204_local_WAN_lane2_txdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 198)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_WAN_lane2_txdown.setStatus(
        ""
    )

mc2200_QS2204_local_WAN_lane3_txup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 199)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_WAN_lane3_txup.setStatus(
        ""
    )

mc2200_QS2204_local_WAN_lane3_txdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 200)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_WAN_lane3_txdown.setStatus(
        ""
    )

mc2200_QS2204_local_WAN_lane4_txup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 201)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_WAN_lane4_txup.setStatus(
        ""
    )

mc2200_QS2204_local_WAN_lane4_txdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 202)
)
if mibBuilder.loadTexts:
    mc2200_QS2204_local_WAN_lane4_txdown.setStatus(
        ""
    )

mc2200_Q2202_local_LAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 203)
)
if mibBuilder.loadTexts:
    mc2200_Q2202_local_LAN_linkup.setStatus(
        ""
    )

mc2200_Q2202_local_LAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 204)
)
if mibBuilder.loadTexts:
    mc2200_Q2202_local_LAN_linkdown.setStatus(
        ""
    )

mc2200_Q2202_local_WAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 205)
)
if mibBuilder.loadTexts:
    mc2200_Q2202_local_WAN_linkup.setStatus(
        ""
    )

mc2200_Q2202_local_WAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 206)
)
if mibBuilder.loadTexts:
    mc2200_Q2202_local_WAN_linkdown.setStatus(
        ""
    )

mc2200_Q2202_local_LAN_txup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 207)
)
if mibBuilder.loadTexts:
    mc2200_Q2202_local_LAN_txup.setStatus(
        ""
    )

mc2200_Q2202_local_LAN_txdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 208)
)
if mibBuilder.loadTexts:
    mc2200_Q2202_local_LAN_txdown.setStatus(
        ""
    )

mc2200_Q2202_local_WAN_txup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 209)
)
if mibBuilder.loadTexts:
    mc2200_Q2202_local_WAN_txup.setStatus(
        ""
    )

mc2200_Q2202_local_WAN_txdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 210)
)
if mibBuilder.loadTexts:
    mc2200_Q2202_local_WAN_txdown.setStatus(
        ""
    )

mc2200_Q2202_rate_40G = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 211)
)
if mibBuilder.loadTexts:
    mc2200_Q2202_rate_40G.setStatus(
        ""
    )

mc2200_Q2202_rate_100G = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 212)
)
if mibBuilder.loadTexts:
    mc2200_Q2202_rate_100G.setStatus(
        ""
    )

mc2200_card_Remote_Connected = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 213)
)
if mibBuilder.loadTexts:
    mc2200_card_Remote_Connected.setStatus(
        ""
    )

mc2200_card_Remote_Disconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 214)
)
if mibBuilder.loadTexts:
    mc2200_card_Remote_Disconnected.setStatus(
        ""
    )

mc2200_card_SFP_model_insert = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 215)
)
if mibBuilder.loadTexts:
    mc2200_card_SFP_model_insert.setStatus(
        ""
    )

mc2200_card_SFP_model_pull_out = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 216)
)
if mibBuilder.loadTexts:
    mc2200_card_SFP_model_pull_out.setStatus(
        ""
    )

mc2200_card_loopback = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 217)
)
if mibBuilder.loadTexts:
    mc2200_card_loopback.setStatus(
        ""
    )

mc2200_NMCsystemStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 218)
)
if mibBuilder.loadTexts:
    mc2200_NMCsystemStatus.setStatus(
        ""
    )

mc2200_FE_MC_local_LAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 219)
)
if mibBuilder.loadTexts:
    mc2200_FE_MC_local_LAN_linkup.setStatus(
        ""
    )

mc2200_FE_MC_local_LAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 220)
)
if mibBuilder.loadTexts:
    mc2200_FE_MC_local_LAN_linkdown.setStatus(
        ""
    )

mc2200_FE_MC_local_WAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 221)
)
if mibBuilder.loadTexts:
    mc2200_FE_MC_local_WAN_linkup.setStatus(
        ""
    )

mc2200_FE_MC_local_WAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 222)
)
if mibBuilder.loadTexts:
    mc2200_FE_MC_local_WAN_linkdown.setStatus(
        ""
    )

mc2200_FE_MC_remote_LAN_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 223)
)
if mibBuilder.loadTexts:
    mc2200_FE_MC_remote_LAN_linkup.setStatus(
        ""
    )

mc2200_FE_MC_remote_LAN_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 28350, 4, 1, 2, 0, 224)
)
if mibBuilder.loadTexts:
    mc2200_FE_MC_remote_LAN_linkdown.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OnAccess2200-MIB",
    **{"firstmilecom": firstmilecom,
       "mc": mc,
       "onaccess2200": onaccess2200,
       "mc2200-NMC": mc2200_NMC,
       "mc2200-SystemInfo": mc2200_SystemInfo,
       "mc2200-SysIPAddress": mc2200_SysIPAddress,
       "mc2200-SysSubnetMask": mc2200_SysSubnetMask,
       "mc2200-SysGateway": mc2200_SysGateway,
       "mc2200-SysMACAddress": mc2200_SysMACAddress,
       "mc2200-SysContact": mc2200_SysContact,
       "mc2200-SysName": mc2200_SysName,
       "mc2200-SysLocation": mc2200_SysLocation,
       "mc2200-SNMPTrapIP1": mc2200_SNMPTrapIP1,
       "mc2200-SNMPTrapIP2": mc2200_SNMPTrapIP2,
       "mc2200-SNMPTrapIP3": mc2200_SNMPTrapIP3,
       "mc2200-SNMPTrapIP4": mc2200_SNMPTrapIP4,
       "mc2200-SNMPTrapIP5": mc2200_SNMPTrapIP5,
       "mc2200-alarminfor": mc2200_alarminfor,
       "mc2200-Master": mc2200_Master,
       "mc2200-ch0ChassisDetail": mc2200_ch0ChassisDetail,
       "mc2200-ch0Status": mc2200_ch0Status,
       "mc2200-ch0LocalConverterNumber": mc2200_ch0LocalConverterNumber,
       "mc2200-ch0RemoteConverterNumber": mc2200_ch0RemoteConverterNumber,
       "mc2200-ch0PowerA": mc2200_ch0PowerA,
       "mc2200-ch0PowerB": mc2200_ch0PowerB,
       "mc2200-ch0FanA": mc2200_ch0FanA,
       "mc2200-ch0FanB": mc2200_ch0FanB,
       "mc2200-ch0HardwareVersion": mc2200_ch0HardwareVersion,
       "mc2200-ch0Description": mc2200_ch0Description,
       "mc2200-ch0AvailableConverterSlots": mc2200_ch0AvailableConverterSlots,
       "mc2200-ch0OccupiedSlots": mc2200_ch0OccupiedSlots,
       "mc2200-ch0EmptySlots": mc2200_ch0EmptySlots,
       "mc2200-TrapID": mc2200_TrapID,
       "mc2200-card-PlugIn": mc2200_card_PlugIn,
       "mc2200-card-PullOut": mc2200_card_PullOut,
       "mc2200-card-Local-Tx-Up": mc2200_card_Local_Tx_Up,
       "mc2200-card-Local-Tx-Down": mc2200_card_Local_Tx_Down,
       "mc2200-card-Local-Fx-Up": mc2200_card_Local_Fx_Up,
       "mc2200-card-Local-Fx-Down": mc2200_card_Local_Fx_Down,
       "mc2200-card-Remote-Power-On": mc2200_card_Remote_Power_On,
       "mc2200-card-Remote-Power-Off": mc2200_card_Remote_Power_Off,
       "mc2200-card-Remote-Tx-Up": mc2200_card_Remote_Tx_Up,
       "mc2200-card-Remote-Tx-Down": mc2200_card_Remote_Tx_Down,
       "mc2200-chassis-Power-A-Active": mc2200_chassis_Power_A_Active,
       "mc2200-chassis-Power-A-Down": mc2200_chassis_Power_A_Down,
       "mc2200-chassis-Power-A-Standby": mc2200_chassis_Power_A_Standby,
       "mc2200-chassis-Power-B-Active": mc2200_chassis_Power_B_Active,
       "mc2200-chassis-Power-B-Down": mc2200_chassis_Power_B_Down,
       "mc2200-chassis-Power-B-Standby": mc2200_chassis_Power_B_Standby,
       "mc2200-chassis-Fan-A-Up": mc2200_chassis_Fan_A_Up,
       "mc2200-chassis-Fan-A-Down": mc2200_chassis_Fan_A_Down,
       "mc2200-chassis-Fan-B-Up": mc2200_chassis_Fan_B_Up,
       "mc2200-chassis-Fan-B-Down": mc2200_chassis_Fan_B_Down,
       "mc2200-chassis-Connected": mc2200_chassis_Connected,
       "mc2200-chassis-Disconnected": mc2200_chassis_Disconnected,
       "mc2200-GEMux8-local-WAN-linkup": mc2200_GEMux8_local_WAN_linkup,
       "mc2200-GEMux8-local-WAN-linkdown": mc2200_GEMux8_local_WAN_linkdown,
       "mc2200-GEMux8-local-LAN-linkup": mc2200_GEMux8_local_LAN_linkup,
       "mc2200-GEMux8-local-LAN-linkdown": mc2200_GEMux8_local_LAN_linkdown,
       "mc2200-GEMux8-local-PORT1-linkup": mc2200_GEMux8_local_PORT1_linkup,
       "mc2200-GEMux8-local-PORT1-linkdown": mc2200_GEMux8_local_PORT1_linkdown,
       "mc2200-GEMux8-local-PORT2-linkup": mc2200_GEMux8_local_PORT2_linkup,
       "mc2200-GEMux8-local-PORT2-linkdown": mc2200_GEMux8_local_PORT2_linkdown,
       "mc2200-GEMux8-local-PORT3-linkup": mc2200_GEMux8_local_PORT3_linkup,
       "mc2200-GEMux8-local-PORT3-linkdown": mc2200_GEMux8_local_PORT3_linkdown,
       "mc2200-GEMux8-local-PORT4-linkup": mc2200_GEMux8_local_PORT4_linkup,
       "mc2200-GEMux8-local-PORT4-linkdown": mc2200_GEMux8_local_PORT4_linkdown,
       "mc2200-GEMux8-local-PORT5-linkup": mc2200_GEMux8_local_PORT5_linkup,
       "mc2200-GEMux8-local-PORT5-linkdown": mc2200_GEMux8_local_PORT5_linkdown,
       "mc2200-GEMux8-local-PORT6-linkup": mc2200_GEMux8_local_PORT6_linkup,
       "mc2200-GEMux8-local-PORT6-linkdown": mc2200_GEMux8_local_PORT6_linkdown,
       "mc2200-GEMux8-local-PORT7-linkup": mc2200_GEMux8_local_PORT7_linkup,
       "mc2200-GEMux8-local-PORT7-linkdown": mc2200_GEMux8_local_PORT7_linkdown,
       "mc2200-GEMux8-local-PORT8-linkup": mc2200_GEMux8_local_PORT8_linkup,
       "mc2200-GEMux8-local-PORT8-linkdown": mc2200_GEMux8_local_PORT8_linkdown,
       "mc2200-GEMux8-remote-LAN-linkup": mc2200_GEMux8_remote_LAN_linkup,
       "mc2200-GEMux8-remote-LAN-linkdown": mc2200_GEMux8_remote_LAN_linkdown,
       "mc2200-GEMux8-remote-PORT1-linkup": mc2200_GEMux8_remote_PORT1_linkup,
       "mc2200-GEMux8-remote-PORT1-linkdown": mc2200_GEMux8_remote_PORT1_linkdown,
       "mc2200-GEMux8-remote-PORT2-linkup": mc2200_GEMux8_remote_PORT2_linkup,
       "mc2200-GEMux8-remote-PORT2-linkdown": mc2200_GEMux8_remote_PORT2_linkdown,
       "mc2200-GEMux8-remote-PORT3-linkup": mc2200_GEMux8_remote_PORT3_linkup,
       "mc2200-GEMux8-remote-PORT3-linkdown": mc2200_GEMux8_remote_PORT3_linkdown,
       "mc2200-GEMux8-remote-PORT4-linkup": mc2200_GEMux8_remote_PORT4_linkup,
       "mc2200-GEMux8-remote-PORT4-linkdown": mc2200_GEMux8_remote_PORT4_linkdown,
       "mc2200-GEMux8-remote-PORT5-linkup": mc2200_GEMux8_remote_PORT5_linkup,
       "mc2200-GEMux8-remote-PORT5-linkdown": mc2200_GEMux8_remote_PORT5_linkdown,
       "mc2200-GEMux8-remote-PORT6-linkup": mc2200_GEMux8_remote_PORT6_linkup,
       "mc2200-GEMux8-remote-PORT6-linkdown": mc2200_GEMux8_remote_PORT6_linkdown,
       "mc2200-GEMux8-remote-PORT7-linkup": mc2200_GEMux8_remote_PORT7_linkup,
       "mc2200-GEMux8-remote-PORT7-linkdown": mc2200_GEMux8_remote_PORT7_linkdown,
       "mc2200-GEMux8-remote-PORT8-linkup": mc2200_GEMux8_remote_PORT8_linkup,
       "mc2200-GEMux8-remote-PORT8-linkdown": mc2200_GEMux8_remote_PORT8_linkdown,
       "mc2200-GEMux8-remote-PORT9-linkup": mc2200_GEMux8_remote_PORT9_linkup,
       "mc2200-GEMux8-remote-PORT9-linkdown": mc2200_GEMux8_remote_PORT9_linkdown,
       "mc2200-chassis-Power-Card-PlugIn": mc2200_chassis_Power_Card_PlugIn,
       "mc2200-chassis-Power-Card-Removed": mc2200_chassis_Power_Card_Removed,
       "mc2200-card-Remote-PowerA-Up-PowerB-Down": mc2200_card_Remote_PowerA_Up_PowerB_Down,
       "mc2200-card-Remote-PowerA-Down-PowerB-Up": mc2200_card_Remote_PowerA_Down_PowerB_Up,
       "mc2200-GEMC-local-LAN-linkup": mc2200_GEMC_local_LAN_linkup,
       "mc2200-GEMC-local-LAN-linkdown": mc2200_GEMC_local_LAN_linkdown,
       "mc2200-GEMC-local-WAN-linkup": mc2200_GEMC_local_WAN_linkup,
       "mc2200-GEMC-local-WAN-linkdown": mc2200_GEMC_local_WAN_linkdown,
       "mc2200-GEMC-remote-LAN-linkup": mc2200_GEMC_remote_LAN_linkup,
       "mc2200-GEMC-remote-LAN-linkdown": mc2200_GEMC_remote_LAN_linkdown,
       "mc2200-GEMC4-local-LAN1-linkup": mc2200_GEMC4_local_LAN1_linkup,
       "mc2200-GEMC4-local-LAN1-linkdown": mc2200_GEMC4_local_LAN1_linkdown,
       "mc2200-GEMC4-local-LAN2-linkup": mc2200_GEMC4_local_LAN2_linkup,
       "mc2200-GEMC4-local-LAN2-linkdown": mc2200_GEMC4_local_LAN2_linkdown,
       "mc2200-GEMC4-local-WAN2LAN3-linkup": mc2200_GEMC4_local_WAN2LAN3_linkup,
       "mc2200-GEMC4-local-WAN2LAN3-linkdown": mc2200_GEMC4_local_WAN2LAN3_linkdown,
       "mc2200-GEMC4-local-WAN1-linkup": mc2200_GEMC4_local_WAN1_linkup,
       "mc2200-GEMC4-local-WAN1-linkdown": mc2200_GEMC4_local_WAN1_linkdown,
       "mc2200-GEMC4-remote-LAN1-linkup": mc2200_GEMC4_remote_LAN1_linkup,
       "mc2200-GEMC4-remote-LAN1-linkdown": mc2200_GEMC4_remote_LAN1_linkdown,
       "mc2200-GEMC4-remote-LAN2-linkup": mc2200_GEMC4_remote_LAN2_linkup,
       "mc2200-GEMC4-remote-LAN2-linkdown": mc2200_GEMC4_remote_LAN2_linkdown,
       "mc2200-GEMC4-remote-WAN2LAN3-linkup": mc2200_GEMC4_remote_WAN2LAN3_linkup,
       "mc2200-GEMC4-remote-WAN2LAN3-linkdown": mc2200_GEMC4_remote_WAN2LAN3_linkdown,
       "mc2200-GEMC2-local-LAN-linkup": mc2200_GEMC2_local_LAN_linkup,
       "mc2200-GEMC2-local-LAN-linkdown": mc2200_GEMC2_local_LAN_linkdown,
       "mc2200-GEMC2-local-WAN-linkup": mc2200_GEMC2_local_WAN_linkup,
       "mc2200-GEMC2-local-WAN-linkdown": mc2200_GEMC2_local_WAN_linkdown,
       "mc2200-GEMC2-remote-LAN-linkup": mc2200_GEMC2_remote_LAN_linkup,
       "mc2200-GEMC2-remote-LAN-linkdown": mc2200_GEMC2_remote_LAN_linkdown,
       "mc2200-GEMC2E-local-LAN-linkup": mc2200_GEMC2E_local_LAN_linkup,
       "mc2200-GEMC2E-local-LAN-linkdown": mc2200_GEMC2E_local_LAN_linkdown,
       "mc2200-GEMC2E-local-WAN-linkup": mc2200_GEMC2E_local_WAN_linkup,
       "mc2200-GEMC2E-local-WAN-linkdown": mc2200_GEMC2E_local_WAN_linkdown,
       "mc2200-GEMC2E-remote-LAN-linkup": mc2200_GEMC2E_remote_LAN_linkup,
       "mc2200-GEMC2E-remote-LAN-linkdown": mc2200_GEMC2E_remote_LAN_linkdown,
       "mc2200-GE-FE-MC-local-LAN-linkup": mc2200_GE_FE_MC_local_LAN_linkup,
       "mc2200-GE-FE-MC-local-LAN-linkdown": mc2200_GE_FE_MC_local_LAN_linkdown,
       "mc2200-GE-FE-MC-local-WAN-linkup": mc2200_GE_FE_MC_local_WAN_linkup,
       "mc2200-GE-FE-MC-local-WAN-linkdown": mc2200_GE_FE_MC_local_WAN_linkdown,
       "mc2200-GE-FE-MC-remote-LAN-linkup": mc2200_GE_FE_MC_remote_LAN_linkup,
       "mc2200-GE-FE-MC-remote-LAN-linkdown": mc2200_GE_FE_MC_remote_LAN_linkdown,
       "mc2200-GE-FE-MC2S-local-LAN-linkup": mc2200_GE_FE_MC2S_local_LAN_linkup,
       "mc2200-GE-FE-MC2S-local-LAN-linkdown": mc2200_GE_FE_MC2S_local_LAN_linkdown,
       "mc2200-GE-FE-MC2S-local-WAN-linkup": mc2200_GE_FE_MC2S_local_WAN_linkup,
       "mc2200-GE-FE-MC2S-local-WAN-linkdown": mc2200_GE_FE_MC2S_local_WAN_linkdown,
       "mc2200-GE-FE-MC2S-remote-LAN-linkup": mc2200_GE_FE_MC2S_remote_LAN_linkup,
       "mc2200-GE-FE-MC2S-remote-LAN-linkdown": mc2200_GE_FE_MC2S_remote_LAN_linkdown,
       "mc2200-GE-FE-MC2T-local-LAN-linkup": mc2200_GE_FE_MC2T_local_LAN_linkup,
       "mc2200-GE-FE-MC2T-local-LAN-linkdown": mc2200_GE_FE_MC2T_local_LAN_linkdown,
       "mc2200-GE-FE-MC2T-local-WAN-linkup": mc2200_GE_FE_MC2T_local_WAN_linkup,
       "mc2200-GE-FE-MC2T-local-WAN-linkdown": mc2200_GE_FE_MC2T_local_WAN_linkdown,
       "mc2200-GE-FE-MC2T-remote-LAN-linkup": mc2200_GE_FE_MC2T_remote_LAN_linkup,
       "mc2200-GE-FE-MC2T-remote-LAN-linkdown": mc2200_GE_FE_MC2T_remote_LAN_linkdown,
       "mc2200-FE-SFP-local-LAN-linkup": mc2200_FE_SFP_local_LAN_linkup,
       "mc2200-FE-SFP-local-LAN-linkdown": mc2200_FE_SFP_local_LAN_linkdown,
       "mc2200-FE-SFP-local-WAN-linkup": mc2200_FE_SFP_local_WAN_linkup,
       "mc2200-FE-SFP-local-WAN-linkdown": mc2200_FE_SFP_local_WAN_linkdown,
       "mc2200-FE-SFP-remote-LAN-linkup": mc2200_FE_SFP_remote_LAN_linkup,
       "mc2200-FE-SFP-remote-LAN-linkdown": mc2200_FE_SFP_remote_LAN_linkdown,
       "mc2200-GE-SFP-local-LAN-linkup": mc2200_GE_SFP_local_LAN_linkup,
       "mc2200-GE-SFP-local-LAN-linkdown": mc2200_GE_SFP_local_LAN_linkdown,
       "mc2200-GE-SFP-local-WAN-linkup": mc2200_GE_SFP_local_WAN_linkup,
       "mc2200-GE-SFP-local-WAN-linkdown": mc2200_GE_SFP_local_WAN_linkdown,
       "mc2200-GE-SFP-remote-LAN-linkup": mc2200_GE_SFP_remote_LAN_linkup,
       "mc2200-GE-SFP-remote-LAN-linkdown": mc2200_GE_SFP_remote_LAN_linkdown,
       "mc2200-GE-MC3-local-LAN-linkup": mc2200_GE_MC3_local_LAN_linkup,
       "mc2200-GE-MC3-local-LAN-linkdown": mc2200_GE_MC3_local_LAN_linkdown,
       "mc2200-GE-MC3-local-WAN-linkup": mc2200_GE_MC3_local_WAN_linkup,
       "mc2200-GE-MC3-local-WAN-linkdown": mc2200_GE_MC3_local_WAN_linkdown,
       "mc2200-GE-MC3-remote-LAN-linkup": mc2200_GE_MC3_remote_LAN_linkup,
       "mc2200-GE-MC3-remote-LAN-linkdown": mc2200_GE_MC3_remote_LAN_linkdown,
       "mc2200-GE-SFP-APS-local-LAN-linkup": mc2200_GE_SFP_APS_local_LAN_linkup,
       "mc2200-GE-SFP-APS-local-LAN-linkdown": mc2200_GE_SFP_APS_local_LAN_linkdown,
       "mc2200-GE-SFP-APS-local-WAN1-linkup": mc2200_GE_SFP_APS_local_WAN1_linkup,
       "mc2200-GE-SFP-APS-local-WAN1-linkdown": mc2200_GE_SFP_APS_local_WAN1_linkdown,
       "mc2200-GE-SFP-APS-local-WAN2-linkup": mc2200_GE_SFP_APS_local_WAN2_linkup,
       "mc2200-GE-SFP-APS-local-WAN2-linkdown": mc2200_GE_SFP_APS_local_WAN2_linkdown,
       "mc2200-GE-SFP-APS-remote-LAN-linkup": mc2200_GE_SFP_APS_remote_LAN_linkup,
       "mc2200-GE-SFP-APS-remote-LAN-linkdown": mc2200_GE_SFP_APS_remote_LAN_linkdown,
       "mc2200-GE-MC-APS-local-LAN-linkup": mc2200_GE_MC_APS_local_LAN_linkup,
       "mc2200-GE-MC-APS-local-LAN-linkdown": mc2200_GE_MC_APS_local_LAN_linkdown,
       "mc2200-GE-MC-APS-local-WAN1-linkup": mc2200_GE_MC_APS_local_WAN1_linkup,
       "mc2200-GE-MC-APS-local-WAN1-linkdown": mc2200_GE_MC_APS_local_WAN1_linkdown,
       "mc2200-GE-MC-APS-local-WAN2-linkup": mc2200_GE_MC_APS_local_WAN2_linkup,
       "mc2200-GE-MC-APS-local-WAN2-linkdown": mc2200_GE_MC_APS_local_WAN2_linkdown,
       "mc2200-GE-MC-APS-remote-LAN-linkup": mc2200_GE_MC_APS_remote_LAN_linkup,
       "mc2200-GE-MC-APS-remote-LAN-linkdown": mc2200_GE_MC_APS_remote_LAN_linkdown,
       "mc2200-CARD-WAN1-switch-WAN2": mc2200_CARD_WAN1_switch_WAN2,
       "mc2200-CARD-WAN2-switch-WAN1": mc2200_CARD_WAN2_switch_WAN1,
       "mc2200-OAPS-local-LAN-linkup": mc2200_OAPS_local_LAN_linkup,
       "mc2200-OAPS-local-LAN-linkdown": mc2200_OAPS_local_LAN_linkdown,
       "mc2200-OAPS-local-WAN1-linkup": mc2200_OAPS_local_WAN1_linkup,
       "mc2200-OAPS-local-WAN1-linkdown": mc2200_OAPS_local_WAN1_linkdown,
       "mc2200-OAPS-local-WAN2-linkup": mc2200_OAPS_local_WAN2_linkup,
       "mc2200-OAPS-local-WAN2-linkdown": mc2200_OAPS_local_WAN2_linkdown,
       "mc2200-PORT-RX-POWER-LOW": mc2200_PORT_RX_POWER_LOW,
       "mc2200-PORT-RX-POWER-NORMAL": mc2200_PORT_RX_POWER_NORMAL,
       "mc2200-QS2204-local-LAN1-linkup": mc2200_QS2204_local_LAN1_linkup,
       "mc2200-QS2204-local-LAN1-linkdown": mc2200_QS2204_local_LAN1_linkdown,
       "mc2200-QS2204-local-LAN2-linkup": mc2200_QS2204_local_LAN2_linkup,
       "mc2200-QS2204-local-LAN2-linkdown": mc2200_QS2204_local_LAN2_linkdown,
       "mc2200-QS2204-local-LAN3-linkup": mc2200_QS2204_local_LAN3_linkup,
       "mc2200-QS2204-local-LAN3-linkdown": mc2200_QS2204_local_LAN3_linkdown,
       "mc2200-QS2204-local-LAN4-linkup": mc2200_QS2204_local_LAN4_linkup,
       "mc2200-QS2204-local-LAN4-linkdown": mc2200_QS2204_local_LAN4_linkdown,
       "mc2200-QS2204-local-WAN-lane1-linkup": mc2200_QS2204_local_WAN_lane1_linkup,
       "mc2200-QS2204-local-WAN-lane1-linkdown": mc2200_QS2204_local_WAN_lane1_linkdown,
       "mc2200-QS2204-local-WAN-lane2-linkup": mc2200_QS2204_local_WAN_lane2_linkup,
       "mc2200-QS2204-local-WAN-lane2-linkdown": mc2200_QS2204_local_WAN_lane2_linkdown,
       "mc2200-QS2204-local-WAN-lane3-linkup": mc2200_QS2204_local_WAN_lane3_linkup,
       "mc2200-QS2204-local-WAN-lane3-linkdown": mc2200_QS2204_local_WAN_lane3_linkdown,
       "mc2200-QS2204-local-WAN-lane4-linkup": mc2200_QS2204_local_WAN_lane4_linkup,
       "mc2200-QS2204-local-WAN-lane4-linkdown": mc2200_QS2204_local_WAN_lane4_linkdown,
       "mc2200-QS2204-local-LAN1-txup": mc2200_QS2204_local_LAN1_txup,
       "mc2200-QS2204-local-LAN1-txdown": mc2200_QS2204_local_LAN1_txdown,
       "mc2200-QS2204-local-LAN2-txup": mc2200_QS2204_local_LAN2_txup,
       "mc2200-QS2204-local-LAN2-txdown": mc2200_QS2204_local_LAN2_txdown,
       "mc2200-QS2204-local-LAN3-txkup": mc2200_QS2204_local_LAN3_txkup,
       "mc2200-QS2204-local-LAN3-txdown": mc2200_QS2204_local_LAN3_txdown,
       "mc2200-QS2204-local-LAN4-txup": mc2200_QS2204_local_LAN4_txup,
       "mc2200-QS2204-local-LAN4-txdown": mc2200_QS2204_local_LAN4_txdown,
       "mc2200-QS2204-local-WAN-lane1-txup": mc2200_QS2204_local_WAN_lane1_txup,
       "mc2200-QS2204-local-WAN-lane1-txdown": mc2200_QS2204_local_WAN_lane1_txdown,
       "mc2200-QS2204-local-WAN-lane2-txup": mc2200_QS2204_local_WAN_lane2_txup,
       "mc2200-QS2204-local-WAN-lane2-txdown": mc2200_QS2204_local_WAN_lane2_txdown,
       "mc2200-QS2204-local-WAN-lane3-txup": mc2200_QS2204_local_WAN_lane3_txup,
       "mc2200-QS2204-local-WAN-lane3-txdown": mc2200_QS2204_local_WAN_lane3_txdown,
       "mc2200-QS2204-local-WAN-lane4-txup": mc2200_QS2204_local_WAN_lane4_txup,
       "mc2200-QS2204-local-WAN-lane4-txdown": mc2200_QS2204_local_WAN_lane4_txdown,
       "mc2200-Q2202-local-LAN-linkup": mc2200_Q2202_local_LAN_linkup,
       "mc2200-Q2202-local-LAN-linkdown": mc2200_Q2202_local_LAN_linkdown,
       "mc2200-Q2202-local-WAN-linkup": mc2200_Q2202_local_WAN_linkup,
       "mc2200-Q2202-local-WAN-linkdown": mc2200_Q2202_local_WAN_linkdown,
       "mc2200-Q2202-local-LAN-txup": mc2200_Q2202_local_LAN_txup,
       "mc2200-Q2202-local-LAN-txdown": mc2200_Q2202_local_LAN_txdown,
       "mc2200-Q2202-local-WAN-txup": mc2200_Q2202_local_WAN_txup,
       "mc2200-Q2202-local-WAN-txdown": mc2200_Q2202_local_WAN_txdown,
       "mc2200-Q2202-rate-40G": mc2200_Q2202_rate_40G,
       "mc2200-Q2202-rate-100G": mc2200_Q2202_rate_100G,
       "mc2200-card-Remote-Connected": mc2200_card_Remote_Connected,
       "mc2200-card-Remote-Disconnected": mc2200_card_Remote_Disconnected,
       "mc2200-card-SFP-model-insert": mc2200_card_SFP_model_insert,
       "mc2200-card-SFP-model-pull-out": mc2200_card_SFP_model_pull_out,
       "mc2200-card-loopback": mc2200_card_loopback,
       "mc2200-NMCsystemStatus": mc2200_NMCsystemStatus,
       "mc2200-FE-MC-local-LAN-linkup": mc2200_FE_MC_local_LAN_linkup,
       "mc2200-FE-MC-local-LAN-linkdown": mc2200_FE_MC_local_LAN_linkdown,
       "mc2200-FE-MC-local-WAN-linkup": mc2200_FE_MC_local_WAN_linkup,
       "mc2200-FE-MC-local-WAN-linkdown": mc2200_FE_MC_local_WAN_linkdown,
       "mc2200-FE-MC-remote-LAN-linkup": mc2200_FE_MC_remote_LAN_linkup,
       "mc2200-FE-MC-remote-LAN-linkdown": mc2200_FE_MC_remote_LAN_linkdown,
       "mc2200-GEmib": mc2200_GEmib,
       "mc2200-GEmux8Table": mc2200_GEmux8Table,
       "mc2200-GEmux8Entry": mc2200_GEmux8Entry,
       "mc2200-GEmux8CardIndex": mc2200_GEmux8CardIndex,
       "mc2200-GEmux8LocalLANSFPInfo": mc2200_GEmux8LocalLANSFPInfo,
       "mc2200-GEmux8LocalLANLink": mc2200_GEmux8LocalLANLink,
       "mc2200-GEmux8LocalWANSFPInfo": mc2200_GEmux8LocalWANSFPInfo,
       "mc2200-GEmux8LocalWANLink": mc2200_GEmux8LocalWANLink,
       "mc2200-GEmux8APSActivePort": mc2200_GEmux8APSActivePort,
       "mc2200-GEmux8LocalPort1Link": mc2200_GEmux8LocalPort1Link,
       "mc2200-GEmux8LocalPort1Speed": mc2200_GEmux8LocalPort1Speed,
       "mc2200-GEmux8LocalPort1Duplex": mc2200_GEmux8LocalPort1Duplex,
       "mc2200-GEmux8LocalPort1TxRate": mc2200_GEmux8LocalPort1TxRate,
       "mc2200-GEmux8LocalPort1RxRate": mc2200_GEmux8LocalPort1RxRate,
       "mc2200-GEmux8LocalPort1Mode": mc2200_GEmux8LocalPort1Mode,
       "mc2200-GEmux8LocalPort1MDIX": mc2200_GEmux8LocalPort1MDIX,
       "mc2200-GEmux8LocalPort2Link": mc2200_GEmux8LocalPort2Link,
       "mc2200-GEmux8LocalPort2Speed": mc2200_GEmux8LocalPort2Speed,
       "mc2200-GEmux8LocalPort2Duplex": mc2200_GEmux8LocalPort2Duplex,
       "mc2200-GEmux8LocalPort2TxRate": mc2200_GEmux8LocalPort2TxRate,
       "mc2200-GEmux8LocalPort2RxRate": mc2200_GEmux8LocalPort2RxRate,
       "mc2200-GEmux8LocalPort2Mode": mc2200_GEmux8LocalPort2Mode,
       "mc2200-GEmux8LocalPort2MDIX": mc2200_GEmux8LocalPort2MDIX,
       "mc2200-GEmux8LocalPort3Link": mc2200_GEmux8LocalPort3Link,
       "mc2200-GEmux8LocalPort3Speed": mc2200_GEmux8LocalPort3Speed,
       "mc2200-GEmux8LocalPort3Duplex": mc2200_GEmux8LocalPort3Duplex,
       "mc2200-GEmux8LocalPort3TxRate": mc2200_GEmux8LocalPort3TxRate,
       "mc2200-GEmux8LocalPort3RxRate": mc2200_GEmux8LocalPort3RxRate,
       "mc2200-GEmux8LocalPort3Mode": mc2200_GEmux8LocalPort3Mode,
       "mc2200-GEmux8LocalPort3MDIX": mc2200_GEmux8LocalPort3MDIX,
       "mc2200-GEmux8LocalPort4Link": mc2200_GEmux8LocalPort4Link,
       "mc2200-GEmux8LocalPort4Speed": mc2200_GEmux8LocalPort4Speed,
       "mc2200-GEmux8LocalPort4Duplex": mc2200_GEmux8LocalPort4Duplex,
       "mc2200-GEmux8LocalPort4TxRate": mc2200_GEmux8LocalPort4TxRate,
       "mc2200-GEmux8LocalPort4RxRate": mc2200_GEmux8LocalPort4RxRate,
       "mc2200-GEmux8LocalPort4Mode": mc2200_GEmux8LocalPort4Mode,
       "mc2200-GEmux8LocalPort4MDIX": mc2200_GEmux8LocalPort4MDIX,
       "mc2200-GEmux8LocalPort5Link": mc2200_GEmux8LocalPort5Link,
       "mc2200-GEmux8LocalPort5Speed": mc2200_GEmux8LocalPort5Speed,
       "mc2200-GEmux8LocalPort5Duplex": mc2200_GEmux8LocalPort5Duplex,
       "mc2200-GEmux8LocalPort5TxRate": mc2200_GEmux8LocalPort5TxRate,
       "mc2200-GEmux8LocalPort5RxRate": mc2200_GEmux8LocalPort5RxRate,
       "mc2200-GEmux8LocalPort5Mode": mc2200_GEmux8LocalPort5Mode,
       "mc2200-GEmux8LocalPort5MDIX": mc2200_GEmux8LocalPort5MDIX,
       "mc2200-GEmux8LocalPort6Link": mc2200_GEmux8LocalPort6Link,
       "mc2200-GEmux8LocalPort6Speed": mc2200_GEmux8LocalPort6Speed,
       "mc2200-GEmux8LocalPort6Duplex": mc2200_GEmux8LocalPort6Duplex,
       "mc2200-GEmux8LocalPort6TxRate": mc2200_GEmux8LocalPort6TxRate,
       "mc2200-GEmux8LocalPort6RxRate": mc2200_GEmux8LocalPort6RxRate,
       "mc2200-GEmux8LocalPort6Mode": mc2200_GEmux8LocalPort6Mode,
       "mc2200-GEmux8LocalPort6MDIX": mc2200_GEmux8LocalPort6MDIX,
       "mc2200-GEmux8LocalPort7Link": mc2200_GEmux8LocalPort7Link,
       "mc2200-GEmux8LocalPort7Speed": mc2200_GEmux8LocalPort7Speed,
       "mc2200-GEmux8LocalPort7Duplex": mc2200_GEmux8LocalPort7Duplex,
       "mc2200-GEmux8LocalPort7TxRate": mc2200_GEmux8LocalPort7TxRate,
       "mc2200-GEmux8LocalPort7RxRate": mc2200_GEmux8LocalPort7RxRate,
       "mc2200-GEmux8LocalPort7Mode": mc2200_GEmux8LocalPort7Mode,
       "mc2200-GEmux8LocalPort7MDIX": mc2200_GEmux8LocalPort7MDIX,
       "mc2200-GEmux8LocalPort8Link": mc2200_GEmux8LocalPort8Link,
       "mc2200-GEmux8LocalPort8Speed": mc2200_GEmux8LocalPort8Speed,
       "mc2200-GEmux8LocalPort8Duplex": mc2200_GEmux8LocalPort8Duplex,
       "mc2200-GEmux8LocalPort8TxRate": mc2200_GEmux8LocalPort8TxRate,
       "mc2200-GEmux8LocalPort8RxRate": mc2200_GEmux8LocalPort8RxRate,
       "mc2200-GEmux8LocalPort8Mode": mc2200_GEmux8LocalPort8Mode,
       "mc2200-GEmux8LocalPort8MDIX": mc2200_GEmux8LocalPort8MDIX,
       "mc2200-GEmux8MibPort1RxGoodOctets": mc2200_GEmux8MibPort1RxGoodOctets,
       "mc2200-GEmux8MibPort1RxFCSErr": mc2200_GEmux8MibPort1RxFCSErr,
       "mc2200-GEmux8MibPort1TxFCSErr": mc2200_GEmux8MibPort1TxFCSErr,
       "mc2200-GEmux8MibPort2RxGoodOctets": mc2200_GEmux8MibPort2RxGoodOctets,
       "mc2200-GEmux8MibPort2RxFCSErr": mc2200_GEmux8MibPort2RxFCSErr,
       "mc2200-GEmux8MibPort2TxFCSErr": mc2200_GEmux8MibPort2TxFCSErr,
       "mc2200-GEmux8MibPort3RxGoodOctets": mc2200_GEmux8MibPort3RxGoodOctets,
       "mc2200-GEmux8MibPort3RxFCSErr": mc2200_GEmux8MibPort3RxFCSErr,
       "mc2200-GEmux8MibPort3TxFCSErr": mc2200_GEmux8MibPort3TxFCSErr,
       "mc2200-GEmux8MibPort4RxGoodOctets": mc2200_GEmux8MibPort4RxGoodOctets,
       "mc2200-GEmux8MibPort4RxFCSErr": mc2200_GEmux8MibPort4RxFCSErr,
       "mc2200-GEmux8MibPort4TxFCSErr": mc2200_GEmux8MibPort4TxFCSErr,
       "mc2200-GEmux8MibPort5RxGoodOctets": mc2200_GEmux8MibPort5RxGoodOctets,
       "mc2200-GEmux8MibPort5RxFCSErr": mc2200_GEmux8MibPort5RxFCSErr,
       "mc2200-GEmux8MibPort5TxFCSErr": mc2200_GEmux8MibPort5TxFCSErr,
       "mc2200-GEmux8MibPort6RxGoodOctets": mc2200_GEmux8MibPort6RxGoodOctets,
       "mc2200-GEmux8MibPort6RxFCSErr": mc2200_GEmux8MibPort6RxFCSErr,
       "mc2200-GEmux8MibPort6TxFCSErr": mc2200_GEmux8MibPort6TxFCSErr,
       "mc2200-GEmux8MibPort7RxGoodOctets": mc2200_GEmux8MibPort7RxGoodOctets,
       "mc2200-GEmux8MibPort7RxFCSErr": mc2200_GEmux8MibPort7RxFCSErr,
       "mc2200-GEmux8MibPort7TxFCSErr": mc2200_GEmux8MibPort7TxFCSErr,
       "mc2200-GEmux8MibPort8RxGoodOctets": mc2200_GEmux8MibPort8RxGoodOctets,
       "mc2200-GEmux8MibPort8RxFCSErr": mc2200_GEmux8MibPort8RxFCSErr,
       "mc2200-GEmux8MibPort8TxFCSErr": mc2200_GEmux8MibPort8TxFCSErr,
       "mc2200-GEmux8RemoteLANSFPInfo": mc2200_GEmux8RemoteLANSFPInfo,
       "mc2200-GEmux8RemoteLANLink": mc2200_GEmux8RemoteLANLink,
       "mc2200-GEmux8RemoteWANSFPInfo": mc2200_GEmux8RemoteWANSFPInfo,
       "mc2200-GEmux8RemoteWANLink": mc2200_GEmux8RemoteWANLink,
       "mc2200-GEmux8RemotePort1Link": mc2200_GEmux8RemotePort1Link,
       "mc2200-GEmux8RemotePort1Speed": mc2200_GEmux8RemotePort1Speed,
       "mc2200-GEmux8RemotePort1Duplex": mc2200_GEmux8RemotePort1Duplex,
       "mc2200-GEmux8RemotePort1Mode": mc2200_GEmux8RemotePort1Mode,
       "mc2200-GEmux8RemotePort1MDIX": mc2200_GEmux8RemotePort1MDIX,
       "mc2200-GEmux8RemotePort2Link": mc2200_GEmux8RemotePort2Link,
       "mc2200-GEmux8RemotePort2Speed": mc2200_GEmux8RemotePort2Speed,
       "mc2200-GEmux8RemotePort2Duplex": mc2200_GEmux8RemotePort2Duplex,
       "mc2200-GEmux8RemotePort2Mode": mc2200_GEmux8RemotePort2Mode,
       "mc2200-GEmux8RemotePort2MDIX": mc2200_GEmux8RemotePort2MDIX,
       "mc2200-GEmux8RemotePort3Link": mc2200_GEmux8RemotePort3Link,
       "mc2200-GEmux8RemotePort3Speed": mc2200_GEmux8RemotePort3Speed,
       "mc2200-GEmux8RemotePort3Duplex": mc2200_GEmux8RemotePort3Duplex,
       "mc2200-GEmux8RemotePort3Mode": mc2200_GEmux8RemotePort3Mode,
       "mc2200-GEmux8RemotePort3MDIX": mc2200_GEmux8RemotePort3MDIX,
       "mc2200-GEmux8RemotePort4Link": mc2200_GEmux8RemotePort4Link,
       "mc2200-GEmux8RemotePort4Speed": mc2200_GEmux8RemotePort4Speed,
       "mc2200-GEmux8RemotePort4Duplex": mc2200_GEmux8RemotePort4Duplex,
       "mc2200-GEmux8RemotePort4Mode": mc2200_GEmux8RemotePort4Mode,
       "mc2200-GEmux8RemotePort4MDIX": mc2200_GEmux8RemotePort4MDIX,
       "mc2200-GEmux8RemotePort5Link": mc2200_GEmux8RemotePort5Link,
       "mc2200-GEmux8RemotePort5Speed": mc2200_GEmux8RemotePort5Speed,
       "mc2200-GEmux8RemotePort5Duplex": mc2200_GEmux8RemotePort5Duplex,
       "mc2200-GEmux8RemotePort5Mode": mc2200_GEmux8RemotePort5Mode,
       "mc2200-GEmux8RemotePort5MDIX": mc2200_GEmux8RemotePort5MDIX,
       "mc2200-GEmux8RemotePort6Link": mc2200_GEmux8RemotePort6Link,
       "mc2200-GEmux8RemotePort6Speed": mc2200_GEmux8RemotePort6Speed,
       "mc2200-GEmux8RemotePort6Duplex": mc2200_GEmux8RemotePort6Duplex,
       "mc2200-GEmux8RemotePort6Mode": mc2200_GEmux8RemotePort6Mode,
       "mc2200-GEmux8RemotePort6MDIX": mc2200_GEmux8RemotePort6MDIX,
       "mc2200-GEmux8RemotePort7Link": mc2200_GEmux8RemotePort7Link,
       "mc2200-GEmux8RemotePort7Speed": mc2200_GEmux8RemotePort7Speed,
       "mc2200-GEmux8RemotePort7Duplex": mc2200_GEmux8RemotePort7Duplex,
       "mc2200-GEmux8RemotePort7Mode": mc2200_GEmux8RemotePort7Mode,
       "mc2200-GEmux8RemotePort7MDIX": mc2200_GEmux8RemotePort7MDIX,
       "mc2200-GEmux8RemotePort8Link": mc2200_GEmux8RemotePort8Link,
       "mc2200-GEmux8RemotePort8Speed": mc2200_GEmux8RemotePort8Speed,
       "mc2200-GEmux8RemotePort8Duplex": mc2200_GEmux8RemotePort8Duplex,
       "mc2200-GEmux8RemotePort8Mode": mc2200_GEmux8RemotePort8Mode,
       "mc2200-GEmux8RemotePort8MDIX": mc2200_GEmux8RemotePort8MDIX,
       "mc2200-GEmux8RemoteIPAddress": mc2200_GEmux8RemoteIPAddress,
       "mc2200-GEmux8RemoteSubnetMask": mc2200_GEmux8RemoteSubnetMask,
       "mc2200-GEmux8RemoteGateWay": mc2200_GEmux8RemoteGateWay,
       "mc2200-GEmux8RemoteVLANEnable": mc2200_GEmux8RemoteVLANEnable,
       "mc2200-GEmux8RemoteVID": mc2200_GEmux8RemoteVID,
       "mc2200-GEmux8RemoteAlarm": mc2200_GEmux8RemoteAlarm,
       "mc2200-GEmux8RFD": mc2200_GEmux8RFD,
       "mc2200-GEmux8Default": mc2200_GEmux8Default,
       "mc2200-GEmux8Reboot": mc2200_GEmux8Reboot,
       "mc2200-GEmux8LocalCardREMOTEMODE": mc2200_GEmux8LocalCardREMOTEMODE,
       "mc2200-GEmux8Localportuser1": mc2200_GEmux8Localportuser1,
       "mc2200-GEmux8Localportuser2": mc2200_GEmux8Localportuser2,
       "mc2200-GEmux8Localportuser3": mc2200_GEmux8Localportuser3,
       "mc2200-GEmux8Localportuser4": mc2200_GEmux8Localportuser4,
       "mc2200-GEmux8Localportuser5": mc2200_GEmux8Localportuser5,
       "mc2200-GEmux8Localportuser6": mc2200_GEmux8Localportuser6,
       "mc2200-GEmux8Localportuser7": mc2200_GEmux8Localportuser7,
       "mc2200-GEmux8Localportuser8": mc2200_GEmux8Localportuser8,
       "mc2200-GEmux8Remoteportuser1": mc2200_GEmux8Remoteportuser1,
       "mc2200-GEmux8Remoteportuser2": mc2200_GEmux8Remoteportuser2,
       "mc2200-GEmux8Remoteportuser3": mc2200_GEmux8Remoteportuser3,
       "mc2200-GEmux8Remoteportuser4": mc2200_GEmux8Remoteportuser4,
       "mc2200-GEmux8Remoteportuser5": mc2200_GEmux8Remoteportuser5,
       "mc2200-GEmux8Remoteportuser6": mc2200_GEmux8Remoteportuser6,
       "mc2200-GEmux8Remoteportuser7": mc2200_GEmux8Remoteportuser7,
       "mc2200-GEmux8Remoteportuser8": mc2200_GEmux8Remoteportuser8,
       "mc2200-GEmux8TrapFilterLocalLAN": mc2200_GEmux8TrapFilterLocalLAN,
       "mc2200-GEmux8TrapFilterLocalWAN": mc2200_GEmux8TrapFilterLocalWAN,
       "mc2200-GEmux8TrapFilterRemotePower": mc2200_GEmux8TrapFilterRemotePower,
       "mc2200-GEmux8TrapFilterRemoteLAN": mc2200_GEmux8TrapFilterRemoteLAN,
       "mc2200-GEmux8TrapFilterRemoteWAN": mc2200_GEmux8TrapFilterRemoteWAN,
       "mc2200-GEMC4Table": mc2200_GEMC4Table,
       "mc2200-GEMC4Entry": mc2200_GEMC4Entry,
       "mc2200-GEMC4CardIndex": mc2200_GEMC4CardIndex,
       "mc2200-GEMC4CardMode": mc2200_GEMC4CardMode,
       "mc2200-GEMC4LocalLAN1SFPInfo": mc2200_GEMC4LocalLAN1SFPInfo,
       "mc2200-GEMC4LocalLAN1Link": mc2200_GEMC4LocalLAN1Link,
       "mc2200-GEMC4LocalLAN2SFPInfo": mc2200_GEMC4LocalLAN2SFPInfo,
       "mc2200-GEMC4LocalLAN2Link": mc2200_GEMC4LocalLAN2Link,
       "mc2200-GEMC4LocalWAN1SFPInfo": mc2200_GEMC4LocalWAN1SFPInfo,
       "mc2200-GEMC4LocalWAN1Link": mc2200_GEMC4LocalWAN1Link,
       "mc2200-GEMC4LocalWAN2LAN3SFPInfo": mc2200_GEMC4LocalWAN2LAN3SFPInfo,
       "mc2200-GEMC4LocalWAN2LAN3Link": mc2200_GEMC4LocalWAN2LAN3Link,
       "mc2200-GEMC4LocalLAN1DownStreamBW": mc2200_GEMC4LocalLAN1DownStreamBW,
       "mc2200-GEMC4LocalLAN1UpStreamBW": mc2200_GEMC4LocalLAN1UpStreamBW,
       "mc2200-GEMC4LocalLAN2DownStreamBW": mc2200_GEMC4LocalLAN2DownStreamBW,
       "mc2200-GEMC4LocalLAN2UpStreamBW": mc2200_GEMC4LocalLAN2UpStreamBW,
       "mc2200-GEMC4LocalLAN3DownStreamBW": mc2200_GEMC4LocalLAN3DownStreamBW,
       "mc2200-GEMC4LocalLAN3UpStreamBW": mc2200_GEMC4LocalLAN3UpStreamBW,
       "mc2200-GEMC4LocalLAN1Mode": mc2200_GEMC4LocalLAN1Mode,
       "mc2200-GEMC4LocalLAN2Mode": mc2200_GEMC4LocalLAN2Mode,
       "mc2200-GEMC4LocalLAN3Mode": mc2200_GEMC4LocalLAN3Mode,
       "mc2200-GEMC4MibCounter1": mc2200_GEMC4MibCounter1,
       "mc2200-GEMC4MibCounter2": mc2200_GEMC4MibCounter2,
       "mc2200-GEMC4MibCounter3": mc2200_GEMC4MibCounter3,
       "mc2200-GEMC4MibCounter4": mc2200_GEMC4MibCounter4,
       "mc2200-GEMC4MibCounter5": mc2200_GEMC4MibCounter5,
       "mc2200-GEMC4MibCounter6": mc2200_GEMC4MibCounter6,
       "mc2200-GEMC4MibCounter7": mc2200_GEMC4MibCounter7,
       "mc2200-GEMC4MibCounter8": mc2200_GEMC4MibCounter8,
       "mc2200-GEMC4MibCounter9": mc2200_GEMC4MibCounter9,
       "mc2200-GEMC4MibCounter10": mc2200_GEMC4MibCounter10,
       "mc2200-GEMC4MibCounter11": mc2200_GEMC4MibCounter11,
       "mc2200-GEMC4MibCounter12": mc2200_GEMC4MibCounter12,
       "mc2200-GEMC4MibCounter13": mc2200_GEMC4MibCounter13,
       "mc2200-GEMC4MibCounter14": mc2200_GEMC4MibCounter14,
       "mc2200-GEMC4MibCounter15": mc2200_GEMC4MibCounter15,
       "mc2200-GEMC4MibCounter16": mc2200_GEMC4MibCounter16,
       "mc2200-GEMC4MibCounter17": mc2200_GEMC4MibCounter17,
       "mc2200-GEMC4MibCounter18": mc2200_GEMC4MibCounter18,
       "mc2200-GEMC4MibCounter19": mc2200_GEMC4MibCounter19,
       "mc2200-GEMC4MibCounter20": mc2200_GEMC4MibCounter20,
       "mc2200-GEMC4MibCounter21": mc2200_GEMC4MibCounter21,
       "mc2200-GEMC4MibCounter22": mc2200_GEMC4MibCounter22,
       "mc2200-GEMC4MibCounter23": mc2200_GEMC4MibCounter23,
       "mc2200-GEMC4MibCounter24": mc2200_GEMC4MibCounter24,
       "mc2200-GEMC4MibCounter25": mc2200_GEMC4MibCounter25,
       "mc2200-GEMC4MibCounter26": mc2200_GEMC4MibCounter26,
       "mc2200-GEMC4MibCounter27": mc2200_GEMC4MibCounter27,
       "mc2200-GEMC4MibCounter28": mc2200_GEMC4MibCounter28,
       "mc2200-GEMC4MibCounter29": mc2200_GEMC4MibCounter29,
       "mc2200-GEMC4MibCounter30": mc2200_GEMC4MibCounter30,
       "mc2200-GEMC4MibCounter31": mc2200_GEMC4MibCounter31,
       "mc2200-GEMC4MibCounter32": mc2200_GEMC4MibCounter32,
       "mc2200-GEMC4RemoteLAN1SFPInfo": mc2200_GEMC4RemoteLAN1SFPInfo,
       "mc2200-GEMC4RemoteLAN1Link": mc2200_GEMC4RemoteLAN1Link,
       "mc2200-GEMC4RemoteLAN2SFPInfo": mc2200_GEMC4RemoteLAN2SFPInfo,
       "mc2200-GEMC4RemoteLAN2Link": mc2200_GEMC4RemoteLAN2Link,
       "mc2200-GEMC4RemoteWAN1SFPInfo": mc2200_GEMC4RemoteWAN1SFPInfo,
       "mc2200-GEMC4RemoteWAN1Link": mc2200_GEMC4RemoteWAN1Link,
       "mc2200-GEMC4RemoteWAN2LAN3SFPInfo": mc2200_GEMC4RemoteWAN2LAN3SFPInfo,
       "mc2200-GEMC4RemoteWAN2LAN3Link": mc2200_GEMC4RemoteWAN2LAN3Link,
       "mc2200-GEMC4RemoteLAN1Mode": mc2200_GEMC4RemoteLAN1Mode,
       "mc2200-GEMC4RemoteLAN2Mode": mc2200_GEMC4RemoteLAN2Mode,
       "mc2200-GEMC4RemoteLAN3Mode": mc2200_GEMC4RemoteLAN3Mode,
       "mc2200-GEMC4RemoteIPAddress": mc2200_GEMC4RemoteIPAddress,
       "mc2200-GEMC4RemoteSubnetMask": mc2200_GEMC4RemoteSubnetMask,
       "mc2200-GEMC4RemoteGateWay": mc2200_GEMC4RemoteGateWay,
       "mc2200-GEMC4RemoteVLANEnable": mc2200_GEMC4RemoteVLANEnable,
       "mc2200-GEMC4RemoteVID": mc2200_GEMC4RemoteVID,
       "mc2200-GEMC4RemoteAlarm": mc2200_GEMC4RemoteAlarm,
       "mc2200-GEMC4RFD": mc2200_GEMC4RFD,
       "mc2200-GEMC4Default": mc2200_GEMC4Default,
       "mc2200-GEMC4Reboot": mc2200_GEMC4Reboot,
       "mc2200-GEMC4LocalCardREMOTEMODE": mc2200_GEMC4LocalCardREMOTEMODE,
       "mc2200-GEMC4LocalLAN1Speed": mc2200_GEMC4LocalLAN1Speed,
       "mc2200-GEMC4LocalLAN2Speed": mc2200_GEMC4LocalLAN2Speed,
       "mc2200-GEMC4LocalWAN2LAN3Speed": mc2200_GEMC4LocalWAN2LAN3Speed,
       "mc2200-GEMC4RemoteLAN1Speed": mc2200_GEMC4RemoteLAN1Speed,
       "mc2200-GEMC4RemoteLAN2Speed": mc2200_GEMC4RemoteLAN2Speed,
       "mc2200-GEMC4RemoteWAN2LAN3Speed": mc2200_GEMC4RemoteWAN2LAN3Speed,
       "mc2200-GEMC4APSActivePort": mc2200_GEMC4APSActivePort,
       "mc2200-GEMC4Localportuser1": mc2200_GEMC4Localportuser1,
       "mc2200-GEMC4Localportuser2": mc2200_GEMC4Localportuser2,
       "mc2200-GEMC4Localportuser3": mc2200_GEMC4Localportuser3,
       "mc2200-GEMC4Remoteportuser1": mc2200_GEMC4Remoteportuser1,
       "mc2200-GEMC4Remoteportuser2": mc2200_GEMC4Remoteportuser2,
       "mc2200-GEMC4Remoteportuser3": mc2200_GEMC4Remoteportuser3,
       "mc2200-GEMC4TrapFilterLocalLAN": mc2200_GEMC4TrapFilterLocalLAN,
       "mc2200-GEMC4TrapFilterLocalWAN": mc2200_GEMC4TrapFilterLocalWAN,
       "mc2200-GEMC4TrapFilterRemotePower": mc2200_GEMC4TrapFilterRemotePower,
       "mc2200-GEMC4TrapFilterRemoteLAN": mc2200_GEMC4TrapFilterRemoteLAN,
       "mc2200-GEMC4TrapFilterRemoteWAN": mc2200_GEMC4TrapFilterRemoteWAN,
       "mc2200-GEMC2Table": mc2200_GEMC2Table,
       "mc2200-GEMC2Entry": mc2200_GEMC2Entry,
       "mc2200-GEMC2CardIndex": mc2200_GEMC2CardIndex,
       "mc2200-GEMC2LocalLANSFPInfo": mc2200_GEMC2LocalLANSFPInfo,
       "mc2200-GEMC2LocalLANLink": mc2200_GEMC2LocalLANLink,
       "mc2200-GEMC2LocalWANSFPInfo": mc2200_GEMC2LocalWANSFPInfo,
       "mc2200-GEMC2LocalWANLink": mc2200_GEMC2LocalWANLink,
       "mc2200-GEMC2LocalLANDownStreamBW": mc2200_GEMC2LocalLANDownStreamBW,
       "mc2200-GEMC2LocalLANUpStreamBW": mc2200_GEMC2LocalLANUpStreamBW,
       "mc2200-GEMC2LocalLANMode": mc2200_GEMC2LocalLANMode,
       "mc2200-GEMC2RxGoodOctets": mc2200_GEMC2RxGoodOctets,
       "mc2200-GEMC2RxBadOctets": mc2200_GEMC2RxBadOctets,
       "mc2200-GEMC2TxFCSErr": mc2200_GEMC2TxFCSErr,
       "mc2200-GEMC2RxUnicast": mc2200_GEMC2RxUnicast,
       "mc2200-GEMC2TxDeferred": mc2200_GEMC2TxDeferred,
       "mc2200-GEMC2RxBroadcasts": mc2200_GEMC2RxBroadcasts,
       "mc2200-GEMC2RxMulticasts": mc2200_GEMC2RxMulticasts,
       "mc2200-GEMC2Rx64Octets": mc2200_GEMC2Rx64Octets,
       "mc2200-GEMC2Rx65to127Octets": mc2200_GEMC2Rx65to127Octets,
       "mc2200-GEMC2Rx128to255Octets": mc2200_GEMC2Rx128to255Octets,
       "mc2200-GEMC2Rx256to511Octets": mc2200_GEMC2Rx256to511Octets,
       "mc2200-GEMC2Rx512to1023Octets": mc2200_GEMC2Rx512to1023Octets,
       "mc2200-GEMC2Rx1024toMaxOctets": mc2200_GEMC2Rx1024toMaxOctets,
       "mc2200-GEMC2TxOctets": mc2200_GEMC2TxOctets,
       "mc2200-GEMC2TxUnicast": mc2200_GEMC2TxUnicast,
       "mc2200-GEMC2TxExcessive": mc2200_GEMC2TxExcessive,
       "mc2200-GEMC2TxMulticasts": mc2200_GEMC2TxMulticasts,
       "mc2200-GEMC2TxBroadcasts": mc2200_GEMC2TxBroadcasts,
       "mc2200-GEMC2TxSingle": mc2200_GEMC2TxSingle,
       "mc2200-GEMC2TxPause": mc2200_GEMC2TxPause,
       "mc2200-GEMC2RxPause": mc2200_GEMC2RxPause,
       "mc2200-GEMC2TxMultiple": mc2200_GEMC2TxMultiple,
       "mc2200-GEMC2RxUndersize": mc2200_GEMC2RxUndersize,
       "mc2200-GEMC2RxFragments": mc2200_GEMC2RxFragments,
       "mc2200-GEMC2RxOversize": mc2200_GEMC2RxOversize,
       "mc2200-GEMC2RxJabber": mc2200_GEMC2RxJabber,
       "mc2200-GEMC2RxErr": mc2200_GEMC2RxErr,
       "mc2200-GEMC2RxFCSErr": mc2200_GEMC2RxFCSErr,
       "mc2200-GEMC2TxCollisions": mc2200_GEMC2TxCollisions,
       "mc2200-GEMC2TxLate": mc2200_GEMC2TxLate,
       "mc2200-GEMC2RemoteLANSFPInfo": mc2200_GEMC2RemoteLANSFPInfo,
       "mc2200-GEMC2RemoteLANLink": mc2200_GEMC2RemoteLANLink,
       "mc2200-GEMC2RemoteWANSFPInfo": mc2200_GEMC2RemoteWANSFPInfo,
       "mc2200-GEMC2RemoteWANLink": mc2200_GEMC2RemoteWANLink,
       "mc2200-GEMC2RemoteLANMode": mc2200_GEMC2RemoteLANMode,
       "mc2200-GEMC2RemoteIPAddress": mc2200_GEMC2RemoteIPAddress,
       "mc2200-GEMC2RemoteSubnetMask": mc2200_GEMC2RemoteSubnetMask,
       "mc2200-GEMC2RemoteGateWay": mc2200_GEMC2RemoteGateWay,
       "mc2200-GEMC2RemoteVLANEnable": mc2200_GEMC2RemoteVLANEnable,
       "mc2200-GEMC2RemoteVID": mc2200_GEMC2RemoteVID,
       "mc2200-GEMC2RemoteAlarm": mc2200_GEMC2RemoteAlarm,
       "mc2200-GEMC2RFD": mc2200_GEMC2RFD,
       "mc2200-GEMC2Default": mc2200_GEMC2Default,
       "mc2200-GEMC2Reboot": mc2200_GEMC2Reboot,
       "mc2200-GEMC2LocalCardREMOTEMODE": mc2200_GEMC2LocalCardREMOTEMODE,
       "mc2200-GEMC2LocalLANSpeed": mc2200_GEMC2LocalLANSpeed,
       "mc2200-GEMC2RemoteLANSpeed": mc2200_GEMC2RemoteLANSpeed,
       "mc2200-GEMC2Localportuser": mc2200_GEMC2Localportuser,
       "mc2200-GEMC2Remoteportuser": mc2200_GEMC2Remoteportuser,
       "mc2200-GEMC2TrapFilterLocalLAN": mc2200_GEMC2TrapFilterLocalLAN,
       "mc2200-GEMC2TrapFilterLocalWAN": mc2200_GEMC2TrapFilterLocalWAN,
       "mc2200-GEMC2TrapFilterRemotePower": mc2200_GEMC2TrapFilterRemotePower,
       "mc2200-GEMC2TrapFilterRemoteLAN": mc2200_GEMC2TrapFilterRemoteLAN,
       "mc2200-GEMC2TrapFilterRemoteWAN": mc2200_GEMC2TrapFilterRemoteWAN,
       "mc2200-FESFPTable": mc2200_FESFPTable,
       "mc2200-FESFPEntry": mc2200_FESFPEntry,
       "mc2200-FESFPCardIndex": mc2200_FESFPCardIndex,
       "mc2200-FESFPLocalTXLink": mc2200_FESFPLocalTXLink,
       "mc2200-FESFPLocalWANSFPInfo": mc2200_FESFPLocalWANSFPInfo,
       "mc2200-FESFPLocalWANLink": mc2200_FESFPLocalWANLink,
       "mc2200-FESFPLocalTXDownStreamBW": mc2200_FESFPLocalTXDownStreamBW,
       "mc2200-FESFPLocalTXUpStreamBW": mc2200_FESFPLocalTXUpStreamBW,
       "mc2200-FESFPLocalTXMode": mc2200_FESFPLocalTXMode,
       "mc2200-FESFPLocalTXMDIX": mc2200_FESFPLocalTXMDIX,
       "mc2200-FESFPRxGoodOctets": mc2200_FESFPRxGoodOctets,
       "mc2200-FESFPRxBadOctets": mc2200_FESFPRxBadOctets,
       "mc2200-FESFPTxFCSErr": mc2200_FESFPTxFCSErr,
       "mc2200-FESFPRxUnicast": mc2200_FESFPRxUnicast,
       "mc2200-FESFPTxDeferred": mc2200_FESFPTxDeferred,
       "mc2200-FESFPRxBroadcasts": mc2200_FESFPRxBroadcasts,
       "mc2200-FESFPRxMulticasts": mc2200_FESFPRxMulticasts,
       "mc2200-FESFPRx64Octets": mc2200_FESFPRx64Octets,
       "mc2200-FESFPRx65to127Octets": mc2200_FESFPRx65to127Octets,
       "mc2200-FESFPRx128to255Octets": mc2200_FESFPRx128to255Octets,
       "mc2200-FESFPRx256to511Octets": mc2200_FESFPRx256to511Octets,
       "mc2200-FESFPRx512to1023Octets": mc2200_FESFPRx512to1023Octets,
       "mc2200-FESFPRx1024toMaxOctets": mc2200_FESFPRx1024toMaxOctets,
       "mc2200-FESFPTxOctets": mc2200_FESFPTxOctets,
       "mc2200-FESFPTxUnicast": mc2200_FESFPTxUnicast,
       "mc2200-FESFPTxExcessive": mc2200_FESFPTxExcessive,
       "mc2200-FESFPTxMulticasts": mc2200_FESFPTxMulticasts,
       "mc2200-FESFPTxBroadcasts": mc2200_FESFPTxBroadcasts,
       "mc2200-FESFPTxSingle": mc2200_FESFPTxSingle,
       "mc2200-FESFPTxPause": mc2200_FESFPTxPause,
       "mc2200-FESFPRxPause": mc2200_FESFPRxPause,
       "mc2200-FESFPTxMultiple": mc2200_FESFPTxMultiple,
       "mc2200-FESFPRxUndersize": mc2200_FESFPRxUndersize,
       "mc2200-FESFPRxFragments": mc2200_FESFPRxFragments,
       "mc2200-FESFPRxOversize": mc2200_FESFPRxOversize,
       "mc2200-FESFPRxJabber": mc2200_FESFPRxJabber,
       "mc2200-FESFPRxErr": mc2200_FESFPRxErr,
       "mc2200-FESFPRxFCSErr": mc2200_FESFPRxFCSErr,
       "mc2200-FESFPTxCollisions": mc2200_FESFPTxCollisions,
       "mc2200-FESFPTxLate": mc2200_FESFPTxLate,
       "mc2200-FESFPRemoteTXLink": mc2200_FESFPRemoteTXLink,
       "mc2200-FESFPRemoteWANSFPInfo": mc2200_FESFPRemoteWANSFPInfo,
       "mc2200-FESFPRemoteWANLink": mc2200_FESFPRemoteWANLink,
       "mc2200-FESFPRemoteTXMode": mc2200_FESFPRemoteTXMode,
       "mc2200-FESFPRemoteTXMDIX": mc2200_FESFPRemoteTXMDIX,
       "mc2200-FESFPRemoteIPAddress": mc2200_FESFPRemoteIPAddress,
       "mc2200-FESFPRemoteSubnetMask": mc2200_FESFPRemoteSubnetMask,
       "mc2200-FESFPRemoteGateWay": mc2200_FESFPRemoteGateWay,
       "mc2200-FESFPRemoteVLANEnable": mc2200_FESFPRemoteVLANEnable,
       "mc2200-FESFPRemoteVID": mc2200_FESFPRemoteVID,
       "mc2200-FESFPRemoteAlarm": mc2200_FESFPRemoteAlarm,
       "mc2200-FESFPRFD": mc2200_FESFPRFD,
       "mc2200-FESFPDefault": mc2200_FESFPDefault,
       "mc2200-FESFPReboot": mc2200_FESFPReboot,
       "mc2200-FESFPLocalTXSpeed": mc2200_FESFPLocalTXSpeed,
       "mc2200-FESFPRemoteTXSpeed": mc2200_FESFPRemoteTXSpeed,
       "mc2200-FESFPLocalportuser": mc2200_FESFPLocalportuser,
       "mc2200-FESFPRemoteportuser": mc2200_FESFPRemoteportuser,
       "mc2200-FESFPLocalTXDuplex": mc2200_FESFPLocalTXDuplex,
       "mc2200-FESFPRemoteTXDuplex": mc2200_FESFPRemoteTXDuplex,
       "mc2200-FESFPFlowControl": mc2200_FESFPFlowControl,
       "mc2200-FESFPWANOpticalPowerCheck": mc2200_FESFPWANOpticalPowerCheck,
       "mc2200-FESFPWANThreshold": mc2200_FESFPWANThreshold,
       "mc2200-FESFPTrapFilterLocalLAN": mc2200_FESFPTrapFilterLocalLAN,
       "mc2200-FESFPTrapFilterLocalWAN": mc2200_FESFPTrapFilterLocalWAN,
       "mc2200-FESFPTrapFilterRemotePower": mc2200_FESFPTrapFilterRemotePower,
       "mc2200-FESFPTrapFilterRemoteLAN": mc2200_FESFPTrapFilterRemoteLAN,
       "mc2200-FESFPTrapFilterRemoteWAN": mc2200_FESFPTrapFilterRemoteWAN,
       "mc2200-FESFPLoopback": mc2200_FESFPLoopback,
       "mc2200-FESFPCardType": mc2200_FESFPCardType,
       "mc2200-GESFPTable": mc2200_GESFPTable,
       "mc2200-GESFPEntry": mc2200_GESFPEntry,
       "mc2200-GESFPCardIndex": mc2200_GESFPCardIndex,
       "mc2200-GESFPLocalTXLink": mc2200_GESFPLocalTXLink,
       "mc2200-GESFPLocalWANSFPInfo": mc2200_GESFPLocalWANSFPInfo,
       "mc2200-GESFPLocalWANLink": mc2200_GESFPLocalWANLink,
       "mc2200-GESFPLocalTXDownStreamBW": mc2200_GESFPLocalTXDownStreamBW,
       "mc2200-GESFPLocalTXUpStreamBW": mc2200_GESFPLocalTXUpStreamBW,
       "mc2200-GESFPLocalTXMode": mc2200_GESFPLocalTXMode,
       "mc2200-GESFPLocalTXMDIX": mc2200_GESFPLocalTXMDIX,
       "mc2200-GESFPRxGoodOctets": mc2200_GESFPRxGoodOctets,
       "mc2200-GESFPRxBadOctets": mc2200_GESFPRxBadOctets,
       "mc2200-GESFPTxFCSErr": mc2200_GESFPTxFCSErr,
       "mc2200-GESFPRxUnicast": mc2200_GESFPRxUnicast,
       "mc2200-GESFPTxDeferred": mc2200_GESFPTxDeferred,
       "mc2200-GESFPRxBroadcasts": mc2200_GESFPRxBroadcasts,
       "mc2200-GESFPRxMulticasts": mc2200_GESFPRxMulticasts,
       "mc2200-GESFPRx64Octets": mc2200_GESFPRx64Octets,
       "mc2200-GESFPRx65to127Octets": mc2200_GESFPRx65to127Octets,
       "mc2200-GESFPRx128to255Octets": mc2200_GESFPRx128to255Octets,
       "mc2200-GESFPRx256to511Octets": mc2200_GESFPRx256to511Octets,
       "mc2200-GESFPRx512to1023Octets": mc2200_GESFPRx512to1023Octets,
       "mc2200-GESFPRx1024toMaxOctets": mc2200_GESFPRx1024toMaxOctets,
       "mc2200-GESFPTxOctets": mc2200_GESFPTxOctets,
       "mc2200-GESFPTxUnicast": mc2200_GESFPTxUnicast,
       "mc2200-GESFPTxExcessive": mc2200_GESFPTxExcessive,
       "mc2200-GESFPTxMulticasts": mc2200_GESFPTxMulticasts,
       "mc2200-GESFPTxBroadcasts": mc2200_GESFPTxBroadcasts,
       "mc2200-GESFPTxSingle": mc2200_GESFPTxSingle,
       "mc2200-GESFPTxPause": mc2200_GESFPTxPause,
       "mc2200-GESFPRxPause": mc2200_GESFPRxPause,
       "mc2200-GESFPTxMultiple": mc2200_GESFPTxMultiple,
       "mc2200-GESFPRxUndersize": mc2200_GESFPRxUndersize,
       "mc2200-GESFPRxFragments": mc2200_GESFPRxFragments,
       "mc2200-GESFPRxOversize": mc2200_GESFPRxOversize,
       "mc2200-GESFPRxJabber": mc2200_GESFPRxJabber,
       "mc2200-GESFPRxErr": mc2200_GESFPRxErr,
       "mc2200-GESFPRxFCSErr": mc2200_GESFPRxFCSErr,
       "mc2200-GESFPTxCollisions": mc2200_GESFPTxCollisions,
       "mc2200-GESFPTxLate": mc2200_GESFPTxLate,
       "mc2200-GESFPRemoteTXLink": mc2200_GESFPRemoteTXLink,
       "mc2200-GESFPRemoteWANSFPInfo": mc2200_GESFPRemoteWANSFPInfo,
       "mc2200-GESFPRemoteWANLink": mc2200_GESFPRemoteWANLink,
       "mc2200-GESFPRemoteTXMode": mc2200_GESFPRemoteTXMode,
       "mc2200-GESFPRemoteTXMDIX": mc2200_GESFPRemoteTXMDIX,
       "mc2200-GESFPRemoteIPAddress": mc2200_GESFPRemoteIPAddress,
       "mc2200-GESFPRemoteSubnetMask": mc2200_GESFPRemoteSubnetMask,
       "mc2200-GESFPRemoteGateWay": mc2200_GESFPRemoteGateWay,
       "mc2200-GESFPRemoteVLANEnable": mc2200_GESFPRemoteVLANEnable,
       "mc2200-GESFPRemoteVID": mc2200_GESFPRemoteVID,
       "mc2200-GESFPRemoteAlarm": mc2200_GESFPRemoteAlarm,
       "mc2200-GESFPRFD": mc2200_GESFPRFD,
       "mc2200-GESFPDefault": mc2200_GESFPDefault,
       "mc2200-GESFPReboot": mc2200_GESFPReboot,
       "mc2200-GESFPLocalTXSpeed": mc2200_GESFPLocalTXSpeed,
       "mc2200-GESFPRemoteTXSpeed": mc2200_GESFPRemoteTXSpeed,
       "mc2200-GESFPLocalportuser": mc2200_GESFPLocalportuser,
       "mc2200-GESFPRemoteportuser": mc2200_GESFPRemoteportuser,
       "mc2200-GESFPLocalTXDuplex": mc2200_GESFPLocalTXDuplex,
       "mc2200-GESFPRemoteTXDuplex": mc2200_GESFPRemoteTXDuplex,
       "mc2200-GESFPFlowControl": mc2200_GESFPFlowControl,
       "mc2200-GESFPWANOpticalPowerCheck": mc2200_GESFPWANOpticalPowerCheck,
       "mc2200-GESFPWANThreshold": mc2200_GESFPWANThreshold,
       "mc2200-GESFPTrapFilterLocalLAN": mc2200_GESFPTrapFilterLocalLAN,
       "mc2200-GESFPTrapFilterLocalWAN": mc2200_GESFPTrapFilterLocalWAN,
       "mc2200-GESFPTrapFilterRemotePower": mc2200_GESFPTrapFilterRemotePower,
       "mc2200-GESFPTrapFilterRemoteLAN": mc2200_GESFPTrapFilterRemoteLAN,
       "mc2200-GESFPTrapFilterRemoteWAN": mc2200_GESFPTrapFilterRemoteWAN,
       "mc2200-GESFPLoopback": mc2200_GESFPLoopback,
       "mc2200-GESFPCardType": mc2200_GESFPCardType,
       "mc2200-GEMC3Table": mc2200_GEMC3Table,
       "mc2200-GEMC3Entry": mc2200_GEMC3Entry,
       "mc2200-GEMC3CardIndex": mc2200_GEMC3CardIndex,
       "mc2200-GEMC3LocalLANSFPInfo": mc2200_GEMC3LocalLANSFPInfo,
       "mc2200-GEMC3LocalLANLink": mc2200_GEMC3LocalLANLink,
       "mc2200-GEMC3LocalWANSFPInfo": mc2200_GEMC3LocalWANSFPInfo,
       "mc2200-GEMC3LocalWANLink": mc2200_GEMC3LocalWANLink,
       "mc2200-GEMC3LocalLANDownStreamBW": mc2200_GEMC3LocalLANDownStreamBW,
       "mc2200-GEMC3LocalLANUpStreamBW": mc2200_GEMC3LocalLANUpStreamBW,
       "mc2200-GEMC3LocalLANMode": mc2200_GEMC3LocalLANMode,
       "mc2200-GEMC3RxGoodOctets": mc2200_GEMC3RxGoodOctets,
       "mc2200-GEMC3RxBadOctets": mc2200_GEMC3RxBadOctets,
       "mc2200-GEMC3TxFCSErr": mc2200_GEMC3TxFCSErr,
       "mc2200-GEMC3RxUnicast": mc2200_GEMC3RxUnicast,
       "mc2200-GEMC3TxDeferred": mc2200_GEMC3TxDeferred,
       "mc2200-GEMC3RxBroadcasts": mc2200_GEMC3RxBroadcasts,
       "mc2200-GEMC3RxMulticasts": mc2200_GEMC3RxMulticasts,
       "mc2200-GEMC3Rx64Octets": mc2200_GEMC3Rx64Octets,
       "mc2200-GEMC3Rx65to127Octets": mc2200_GEMC3Rx65to127Octets,
       "mc2200-GEMC3Rx128to255Octets": mc2200_GEMC3Rx128to255Octets,
       "mc2200-GEMC3Rx256to511Octets": mc2200_GEMC3Rx256to511Octets,
       "mc2200-GEMC3Rx512to1023Octets": mc2200_GEMC3Rx512to1023Octets,
       "mc2200-GEMC3Rx1024toMaxOctets": mc2200_GEMC3Rx1024toMaxOctets,
       "mc2200-GEMC3TxOctets": mc2200_GEMC3TxOctets,
       "mc2200-GEMC3TxUnicast": mc2200_GEMC3TxUnicast,
       "mc2200-GEMC3TxExcessive": mc2200_GEMC3TxExcessive,
       "mc2200-GEMC3TxMulticasts": mc2200_GEMC3TxMulticasts,
       "mc2200-GEMC3TxBroadcasts": mc2200_GEMC3TxBroadcasts,
       "mc2200-GEMC3TxSingle": mc2200_GEMC3TxSingle,
       "mc2200-GEMC3TxPause": mc2200_GEMC3TxPause,
       "mc2200-GEMC3RxPause": mc2200_GEMC3RxPause,
       "mc2200-GEMC3TxMultiple": mc2200_GEMC3TxMultiple,
       "mc2200-GEMC3RxUndersize": mc2200_GEMC3RxUndersize,
       "mc2200-GEMC3RxFragments": mc2200_GEMC3RxFragments,
       "mc2200-GEMC3RxOversize": mc2200_GEMC3RxOversize,
       "mc2200-GEMC3RxJabber": mc2200_GEMC3RxJabber,
       "mc2200-GEMC3RxErr": mc2200_GEMC3RxErr,
       "mc2200-GEMC3RxFCSErr": mc2200_GEMC3RxFCSErr,
       "mc2200-GEMC3TxCollisions": mc2200_GEMC3TxCollisions,
       "mc2200-GEMC3TxLate": mc2200_GEMC3TxLate,
       "mc2200-GEMC3RemoteLANSFPInfo": mc2200_GEMC3RemoteLANSFPInfo,
       "mc2200-GEMC3RemoteLANLink": mc2200_GEMC3RemoteLANLink,
       "mc2200-GEMC3RemoteWANSFPInfo": mc2200_GEMC3RemoteWANSFPInfo,
       "mc2200-GEMC3RemoteWANLink": mc2200_GEMC3RemoteWANLink,
       "mc2200-GEMC3RemoteLANMode": mc2200_GEMC3RemoteLANMode,
       "mc2200-GEMC3RemoteIPAddress": mc2200_GEMC3RemoteIPAddress,
       "mc2200-GEMC3RemoteSubnetMask": mc2200_GEMC3RemoteSubnetMask,
       "mc2200-GEMC3RemoteGateWay": mc2200_GEMC3RemoteGateWay,
       "mc2200-GEMC3RemoteVLANEnable": mc2200_GEMC3RemoteVLANEnable,
       "mc2200-GEMC3RemoteVID": mc2200_GEMC3RemoteVID,
       "mc2200-GEMC3RemoteAlarm": mc2200_GEMC3RemoteAlarm,
       "mc2200-GEMC3RFD": mc2200_GEMC3RFD,
       "mc2200-GEMC3Default": mc2200_GEMC3Default,
       "mc2200-GEMC3Reboot": mc2200_GEMC3Reboot,
       "mc2200-GEMC3LocalLANSpeed": mc2200_GEMC3LocalLANSpeed,
       "mc2200-GEMC3RemoteLANSpeed": mc2200_GEMC3RemoteLANSpeed,
       "mc2200-GEMC3Localportuser": mc2200_GEMC3Localportuser,
       "mc2200-GEMC3Remoteportuser": mc2200_GEMC3Remoteportuser,
       "mc2200-GEMC3WANOpticalPowerCheck": mc2200_GEMC3WANOpticalPowerCheck,
       "mc2200-GEMC3WANThreshold": mc2200_GEMC3WANThreshold,
       "mc2200-GEMC3TrapFilterLocalLAN": mc2200_GEMC3TrapFilterLocalLAN,
       "mc2200-GEMC3TrapFilterLocalWAN": mc2200_GEMC3TrapFilterLocalWAN,
       "mc2200-GEMC3TrapFilterRemotePower": mc2200_GEMC3TrapFilterRemotePower,
       "mc2200-GEMC3TrapFilterRemoteLAN": mc2200_GEMC3TrapFilterRemoteLAN,
       "mc2200-GEMC3TrapFilterRemoteWAN": mc2200_GEMC3TrapFilterRemoteWAN,
       "mc2200-GEMC3Loopback": mc2200_GEMC3Loopback,
       "mc2200-GEMC3CardType": mc2200_GEMC3CardType,
       "mc2200-GESFPAPSTable": mc2200_GESFPAPSTable,
       "mc2200-GESFPAPSEntry": mc2200_GESFPAPSEntry,
       "mc2200-GESFPAPSCardIndex": mc2200_GESFPAPSCardIndex,
       "mc2200-GESFPAPSLocalTXLink": mc2200_GESFPAPSLocalTXLink,
       "mc2200-GESFPAPSLocalWAN1SFPInfo": mc2200_GESFPAPSLocalWAN1SFPInfo,
       "mc2200-GESFPAPSLocalWAN1Link": mc2200_GESFPAPSLocalWAN1Link,
       "mc2200-GESFPAPSLocalWAN2SFPInfo": mc2200_GESFPAPSLocalWAN2SFPInfo,
       "mc2200-GESFPAPSLocalWAN2Link": mc2200_GESFPAPSLocalWAN2Link,
       "mc2200-GESFPAPSLocalActivePort": mc2200_GESFPAPSLocalActivePort,
       "mc2200-GESFPAPSLocalTXDownStreamBW": mc2200_GESFPAPSLocalTXDownStreamBW,
       "mc2200-GESFPAPSLocalTXUpStreamBW": mc2200_GESFPAPSLocalTXUpStreamBW,
       "mc2200-GESFPAPSLocalTXMode": mc2200_GESFPAPSLocalTXMode,
       "mc2200-GESFPAPSLocalTXMDIX": mc2200_GESFPAPSLocalTXMDIX,
       "mc2200-GESFPAPSRxGoodOctets": mc2200_GESFPAPSRxGoodOctets,
       "mc2200-GESFPAPSRxBadOctets": mc2200_GESFPAPSRxBadOctets,
       "mc2200-GESFPAPSTxFCSErr": mc2200_GESFPAPSTxFCSErr,
       "mc2200-GESFPAPSRxUnicast": mc2200_GESFPAPSRxUnicast,
       "mc2200-GESFPAPSTxDeferred": mc2200_GESFPAPSTxDeferred,
       "mc2200-GESFPAPSRxBroadcasts": mc2200_GESFPAPSRxBroadcasts,
       "mc2200-GESFPAPSRxMulticasts": mc2200_GESFPAPSRxMulticasts,
       "mc2200-GESFPAPSRx64Octets": mc2200_GESFPAPSRx64Octets,
       "mc2200-GESFPAPSRx65to127Octets": mc2200_GESFPAPSRx65to127Octets,
       "mc2200-GESFPAPSRx128to255Octets": mc2200_GESFPAPSRx128to255Octets,
       "mc2200-GESFPAPSRx256to511Octets": mc2200_GESFPAPSRx256to511Octets,
       "mc2200-GESFPAPSRx512to1023Octets": mc2200_GESFPAPSRx512to1023Octets,
       "mc2200-GESFPAPSRx1024toMaxOctets": mc2200_GESFPAPSRx1024toMaxOctets,
       "mc2200-GESFPAPSTxOctets": mc2200_GESFPAPSTxOctets,
       "mc2200-GESFPAPSTxUnicast": mc2200_GESFPAPSTxUnicast,
       "mc2200-GESFPAPSTxExcessive": mc2200_GESFPAPSTxExcessive,
       "mc2200-GESFPAPSTxMulticasts": mc2200_GESFPAPSTxMulticasts,
       "mc2200-GESFPAPSTxBroadcasts": mc2200_GESFPAPSTxBroadcasts,
       "mc2200-GESFPAPSTxSingle": mc2200_GESFPAPSTxSingle,
       "mc2200-GESFPAPSTxPause": mc2200_GESFPAPSTxPause,
       "mc2200-GESFPAPSRxPause": mc2200_GESFPAPSRxPause,
       "mc2200-GESFPAPSTxMultiple": mc2200_GESFPAPSTxMultiple,
       "mc2200-GESFPAPSRxUndersize": mc2200_GESFPAPSRxUndersize,
       "mc2200-GESFPAPSRxFragments": mc2200_GESFPAPSRxFragments,
       "mc2200-GESFPAPSRxOversize": mc2200_GESFPAPSRxOversize,
       "mc2200-GESFPAPSRxJabber": mc2200_GESFPAPSRxJabber,
       "mc2200-GESFPAPSRxErr": mc2200_GESFPAPSRxErr,
       "mc2200-GESFPAPSRxFCSErr": mc2200_GESFPAPSRxFCSErr,
       "mc2200-GESFPAPSTxCollisions": mc2200_GESFPAPSTxCollisions,
       "mc2200-GESFPAPSTxLate": mc2200_GESFPAPSTxLate,
       "mc2200-GESFPAPSRemoteTXLink": mc2200_GESFPAPSRemoteTXLink,
       "mc2200-GESFPAPSRemoteWAN1SFPInfo": mc2200_GESFPAPSRemoteWAN1SFPInfo,
       "mc2200-GESFPAPSRemoteWAN1Link": mc2200_GESFPAPSRemoteWAN1Link,
       "mc2200-GESFPAPSRemoteWAN2SFPInfo": mc2200_GESFPAPSRemoteWAN2SFPInfo,
       "mc2200-GESFPAPSRemoteWAN2Link": mc2200_GESFPAPSRemoteWAN2Link,
       "mc2200-GESFPAPSRemoteTXMode": mc2200_GESFPAPSRemoteTXMode,
       "mc2200-GESFPAPSRemoteTXMDIX": mc2200_GESFPAPSRemoteTXMDIX,
       "mc2200-GESFPAPSRemoteIPAddress": mc2200_GESFPAPSRemoteIPAddress,
       "mc2200-GESFPAPSRemoteSubnetMask": mc2200_GESFPAPSRemoteSubnetMask,
       "mc2200-GESFPAPSRemoteGateWay": mc2200_GESFPAPSRemoteGateWay,
       "mc2200-GESFPAPSRemoteVLANEnable": mc2200_GESFPAPSRemoteVLANEnable,
       "mc2200-GESFPAPSRemoteVID": mc2200_GESFPAPSRemoteVID,
       "mc2200-GESFPAPSRemoteAlarm": mc2200_GESFPAPSRemoteAlarm,
       "mc2200-GESFPAPSRFD": mc2200_GESFPAPSRFD,
       "mc2200-GESFPAPSDefault": mc2200_GESFPAPSDefault,
       "mc2200-GESFPAPSReboot": mc2200_GESFPAPSReboot,
       "mc2200-GESFPAPSLocalTXSpeed": mc2200_GESFPAPSLocalTXSpeed,
       "mc2200-GESFPAPSRemoteTXSpeed": mc2200_GESFPAPSRemoteTXSpeed,
       "mc2200-GESFPAPSLocalportuser": mc2200_GESFPAPSLocalportuser,
       "mc2200-GESFPAPSRemoteportuser": mc2200_GESFPAPSRemoteportuser,
       "mc2200-GESFPAPSLocalTXDuplex": mc2200_GESFPAPSLocalTXDuplex,
       "mc2200-GESFPAPSRemoteTXDuplex": mc2200_GESFPAPSRemoteTXDuplex,
       "mc2200-GESFPAPSFlowControl": mc2200_GESFPAPSFlowControl,
       "mc2200-GESFPAPSRevertive": mc2200_GESFPAPSRevertive,
       "mc2200-GESFPAPSWAN1OpticalPowerCheck": mc2200_GESFPAPSWAN1OpticalPowerCheck,
       "mc2200-GESFPAPSWAN1Threshold": mc2200_GESFPAPSWAN1Threshold,
       "mc2200-GESFPAPSWAN2OpticalPowerCheck": mc2200_GESFPAPSWAN2OpticalPowerCheck,
       "mc2200-GESFPAPSWAN2Threshold": mc2200_GESFPAPSWAN2Threshold,
       "mc2200-GESFPAPSTrapFilterLocalLAN": mc2200_GESFPAPSTrapFilterLocalLAN,
       "mc2200-GESFPAPSTrapFilterLocalWAN": mc2200_GESFPAPSTrapFilterLocalWAN,
       "mc2200-GESFPAPSTrapFilterRemotePower": mc2200_GESFPAPSTrapFilterRemotePower,
       "mc2200-GESFPAPSTrapFilterRemoteLAN": mc2200_GESFPAPSTrapFilterRemoteLAN,
       "mc2200-GESFPAPSTrapFilterRemoteWAN": mc2200_GESFPAPSTrapFilterRemoteWAN,
       "mc2200-GESFPAPSLoopback": mc2200_GESFPAPSLoopback,
       "mc2200-GESFPAPSCardType": mc2200_GESFPAPSCardType,
       "mc2200-GEMCAPSTable": mc2200_GEMCAPSTable,
       "mc2200-GEMCAPSEntry": mc2200_GEMCAPSEntry,
       "mc2200-GEMCAPSCardIndex": mc2200_GEMCAPSCardIndex,
       "mc2200-GEMCAPSLocalLANSFPInfo": mc2200_GEMCAPSLocalLANSFPInfo,
       "mc2200-GEMCAPSLocalLANLink": mc2200_GEMCAPSLocalLANLink,
       "mc2200-GEMCAPSLocalWAN1SFPInfo": mc2200_GEMCAPSLocalWAN1SFPInfo,
       "mc2200-GEMCAPSLocalWAN1Link": mc2200_GEMCAPSLocalWAN1Link,
       "mc2200-GEMCAPSLocalWAN2SFPInfo": mc2200_GEMCAPSLocalWAN2SFPInfo,
       "mc2200-GEMCAPSLocalWAN2Link": mc2200_GEMCAPSLocalWAN2Link,
       "mc2200-GEMCAPSLocalActivePort": mc2200_GEMCAPSLocalActivePort,
       "mc2200-GEMCAPSLocalLANDownStreamBW": mc2200_GEMCAPSLocalLANDownStreamBW,
       "mc2200-GEMCAPSLocalLANUpStreamBW": mc2200_GEMCAPSLocalLANUpStreamBW,
       "mc2200-GEMCAPSLocalLANMode": mc2200_GEMCAPSLocalLANMode,
       "mc2200-GEMCAPSRxGoodOctets": mc2200_GEMCAPSRxGoodOctets,
       "mc2200-GEMCAPSRxBadOctets": mc2200_GEMCAPSRxBadOctets,
       "mc2200-GEMCAPSTxFCSErr": mc2200_GEMCAPSTxFCSErr,
       "mc2200-GEMCAPSRxUnicast": mc2200_GEMCAPSRxUnicast,
       "mc2200-GEMCAPSTxDeferred": mc2200_GEMCAPSTxDeferred,
       "mc2200-GEMCAPSRxBroadcasts": mc2200_GEMCAPSRxBroadcasts,
       "mc2200-GEMCAPSRxMulticasts": mc2200_GEMCAPSRxMulticasts,
       "mc2200-GEMCAPSRx64Octets": mc2200_GEMCAPSRx64Octets,
       "mc2200-GEMCAPSRx65to127Octets": mc2200_GEMCAPSRx65to127Octets,
       "mc2200-GEMCAPSRx128to255Octets": mc2200_GEMCAPSRx128to255Octets,
       "mc2200-GEMCAPSRx256to511Octets": mc2200_GEMCAPSRx256to511Octets,
       "mc2200-GEMCAPSRx512to1023Octets": mc2200_GEMCAPSRx512to1023Octets,
       "mc2200-GEMCAPSRx1024toMaxOctets": mc2200_GEMCAPSRx1024toMaxOctets,
       "mc2200-GEMCAPSTxOctets": mc2200_GEMCAPSTxOctets,
       "mc2200-GEMCAPSTxUnicast": mc2200_GEMCAPSTxUnicast,
       "mc2200-GEMCAPSTxExcessive": mc2200_GEMCAPSTxExcessive,
       "mc2200-GEMCAPSTxMulticasts": mc2200_GEMCAPSTxMulticasts,
       "mc2200-GEMCAPSTxBroadcasts": mc2200_GEMCAPSTxBroadcasts,
       "mc2200-GEMCAPSTxSingle": mc2200_GEMCAPSTxSingle,
       "mc2200-GEMCAPSTxPause": mc2200_GEMCAPSTxPause,
       "mc2200-GEMCAPSRxPause": mc2200_GEMCAPSRxPause,
       "mc2200-GEMCAPSTxMultiple": mc2200_GEMCAPSTxMultiple,
       "mc2200-GEMCAPSRxUndersize": mc2200_GEMCAPSRxUndersize,
       "mc2200-GEMCAPSRxFragments": mc2200_GEMCAPSRxFragments,
       "mc2200-GEMCAPSRxOversize": mc2200_GEMCAPSRxOversize,
       "mc2200-GEMCAPSRxJabber": mc2200_GEMCAPSRxJabber,
       "mc2200-GEMCAPSRxErr": mc2200_GEMCAPSRxErr,
       "mc2200-GEMCAPSRxFCSErr": mc2200_GEMCAPSRxFCSErr,
       "mc2200-GEMCAPSTxCollisions": mc2200_GEMCAPSTxCollisions,
       "mc2200-GEMCAPSTxLate": mc2200_GEMCAPSTxLate,
       "mc2200-GEMCAPSRemoteLANSFPInfo": mc2200_GEMCAPSRemoteLANSFPInfo,
       "mc2200-GEMCAPSRemoteLANLink": mc2200_GEMCAPSRemoteLANLink,
       "mc2200-GEMCAPSRemoteWAN1SFPInfo": mc2200_GEMCAPSRemoteWAN1SFPInfo,
       "mc2200-GEMCAPSRemoteWAN1Link": mc2200_GEMCAPSRemoteWAN1Link,
       "mc2200-GEMCAPSRemoteWAN2SFPInfo": mc2200_GEMCAPSRemoteWAN2SFPInfo,
       "mc2200-GEMCAPSRemoteWAN2Link": mc2200_GEMCAPSRemoteWAN2Link,
       "mc2200-GEMCAPSRemoteLANMode": mc2200_GEMCAPSRemoteLANMode,
       "mc2200-GEMCAPSRemoteIPAddress": mc2200_GEMCAPSRemoteIPAddress,
       "mc2200-GEMCAPSRemoteSubnetMask": mc2200_GEMCAPSRemoteSubnetMask,
       "mc2200-GEMCAPSRemoteGateWay": mc2200_GEMCAPSRemoteGateWay,
       "mc2200-GEMCAPSRemoteVLANEnable": mc2200_GEMCAPSRemoteVLANEnable,
       "mc2200-GEMCAPSRemoteVID": mc2200_GEMCAPSRemoteVID,
       "mc2200-GEMCAPSRemoteAlarm": mc2200_GEMCAPSRemoteAlarm,
       "mc2200-GEMCAPSRFD": mc2200_GEMCAPSRFD,
       "mc2200-GEMCAPSDefault": mc2200_GEMCAPSDefault,
       "mc2200-GEMCAPSReboot": mc2200_GEMCAPSReboot,
       "mc2200-GEMCAPSLocalLANSpeed": mc2200_GEMCAPSLocalLANSpeed,
       "mc2200-GEMCAPSRemoteLANSpeed": mc2200_GEMCAPSRemoteLANSpeed,
       "mc2200-GEMCAPSLocalportuser": mc2200_GEMCAPSLocalportuser,
       "mc2200-GEMCAPSRemoteportuser": mc2200_GEMCAPSRemoteportuser,
       "mc2200-GEMCAPSRevertive": mc2200_GEMCAPSRevertive,
       "mc2200-GEMCAPSWAN1OpticalPowerCheck": mc2200_GEMCAPSWAN1OpticalPowerCheck,
       "mc2200-GEMCAPSWAN1Threshold": mc2200_GEMCAPSWAN1Threshold,
       "mc2200-GEMCAPSWAN2OpticalPowerCheck": mc2200_GEMCAPSWAN2OpticalPowerCheck,
       "mc2200-GEMCAPSWAN2Threshold": mc2200_GEMCAPSWAN2Threshold,
       "mc2200-GEMCAPSTrapFilterLocalLAN": mc2200_GEMCAPSTrapFilterLocalLAN,
       "mc2200-GEMCAPSTrapFilterLocalWAN": mc2200_GEMCAPSTrapFilterLocalWAN,
       "mc2200-GEMCAPSTrapFilterRemotePower": mc2200_GEMCAPSTrapFilterRemotePower,
       "mc2200-GEMCAPSTrapFilterRemoteLAN": mc2200_GEMCAPSTrapFilterRemoteLAN,
       "mc2200-GEMCAPSTrapFilterRemoteWAN": mc2200_GEMCAPSTrapFilterRemoteWAN,
       "mc2200-GEMCAPSLoopback": mc2200_GEMCAPSLoopback,
       "mc2200-GEMCAPSCardType": mc2200_GEMCAPSCardType,
       "mc2200-OAPSTable": mc2200_OAPSTable,
       "mc2200-OAPSEntry": mc2200_OAPSEntry,
       "mc2200-OAPSCardIndex": mc2200_OAPSCardIndex,
       "mc2200-OAPSLocalLANLink": mc2200_OAPSLocalLANLink,
       "mc2200-OAPSLocalLANPower": mc2200_OAPSLocalLANPower,
       "mc2200-OAPSLocalLANThreshold": mc2200_OAPSLocalLANThreshold,
       "mc2200-OAPSLocalWAN1Link": mc2200_OAPSLocalWAN1Link,
       "mc2200-OAPSLocalWAN1Power": mc2200_OAPSLocalWAN1Power,
       "mc2200-OAPSLocalWAN1Threshold": mc2200_OAPSLocalWAN1Threshold,
       "mc2200-OAPSLocalWAN2Link": mc2200_OAPSLocalWAN2Link,
       "mc2200-OAPSLocalWAN2Power": mc2200_OAPSLocalWAN2Power,
       "mc2200-OAPSLocalWAN2Threshold": mc2200_OAPSLocalWAN2Threshold,
       "mc2200-OAPSLocalActivePort": mc2200_OAPSLocalActivePort,
       "mc2200-OAPSRevertive": mc2200_OAPSRevertive,
       "mc2200-OAPSDefault": mc2200_OAPSDefault,
       "mc2200-OAPSReboot": mc2200_OAPSReboot,
       "mc2200-OAPSLocalportuser": mc2200_OAPSLocalportuser,
       "mc2200-OAPSRemoteportuser": mc2200_OAPSRemoteportuser,
       "mc2200-OAPSUsingActiveport": mc2200_OAPSUsingActiveport,
       "mc2200-OAPSTrapFilterLocalLAN": mc2200_OAPSTrapFilterLocalLAN,
       "mc2200-OAPSTrapFilterLocalWAN": mc2200_OAPSTrapFilterLocalWAN,
       "mc2200-QS2204Table": mc2200_QS2204Table,
       "mc2200-QS2204Entry": mc2200_QS2204Entry,
       "mc2200-QS2204CardIndex": mc2200_QS2204CardIndex,
       "mc2200-QS2204LocalLAN1Link": mc2200_QS2204LocalLAN1Link,
       "mc2200-QS2204LocalLAN1TxStatus": mc2200_QS2204LocalLAN1TxStatus,
       "mc2200-QS2204LocalLAN1SFPInfo": mc2200_QS2204LocalLAN1SFPInfo,
       "mc2200-QS2204LocalLAN1Loopback": mc2200_QS2204LocalLAN1Loopback,
       "mc2200-QS2204LocalLAN2Link": mc2200_QS2204LocalLAN2Link,
       "mc2200-QS2204LocalLAN2TxStatus": mc2200_QS2204LocalLAN2TxStatus,
       "mc2200-QS2204LocalLAN2SFPInfo": mc2200_QS2204LocalLAN2SFPInfo,
       "mc2200-QS2204LocalLAN2Loopback": mc2200_QS2204LocalLAN2Loopback,
       "mc2200-QS2204LocalLAN3Link": mc2200_QS2204LocalLAN3Link,
       "mc2200-QS2204LocalLAN3TxStatus": mc2200_QS2204LocalLAN3TxStatus,
       "mc2200-QS2204LocalLAN3SFPInfo": mc2200_QS2204LocalLAN3SFPInfo,
       "mc2200-QS2204LocalLAN3Loopback": mc2200_QS2204LocalLAN3Loopback,
       "mc2200-QS2204LocalLAN4Link": mc2200_QS2204LocalLAN4Link,
       "mc2200-QS2204LocalLAN4TxStatus": mc2200_QS2204LocalLAN4TxStatus,
       "mc2200-QS2204LocalLAN4SFPInfo": mc2200_QS2204LocalLAN4SFPInfo,
       "mc2200-QS2204LocalLAN4Loopback": mc2200_QS2204LocalLAN4Loopback,
       "mc2200-QS2204LocalWANLink": mc2200_QS2204LocalWANLink,
       "mc2200-QS2204LocalWANTxStatus": mc2200_QS2204LocalWANTxStatus,
       "mc2200-QS2204LocalWANSFPInfo": mc2200_QS2204LocalWANSFPInfo,
       "mc2200-QS2204LocalWANLoopback": mc2200_QS2204LocalWANLoopback,
       "mc2200-QS2204RFD": mc2200_QS2204RFD,
       "mc2200-QS2204Default": mc2200_QS2204Default,
       "mc2200-QS2204Reboot": mc2200_QS2204Reboot,
       "mc2200-QS2204LocalLAN1user": mc2200_QS2204LocalLAN1user,
       "mc2200-QS2204LocalLAN2user": mc2200_QS2204LocalLAN2user,
       "mc2200-QS2204LocalLAN3user": mc2200_QS2204LocalLAN3user,
       "mc2200-QS2204LocalLAN4user": mc2200_QS2204LocalLAN4user,
       "mc2200-Q2202Table": mc2200_Q2202Table,
       "mc2200-Q2202Entry": mc2200_Q2202Entry,
       "mc2200-Q2202CardIndex": mc2200_Q2202CardIndex,
       "mc2200-Q2202LocalLANLink": mc2200_Q2202LocalLANLink,
       "mc2200-Q2202LocalLANTxStatus": mc2200_Q2202LocalLANTxStatus,
       "mc2200-Q2202LocalLANSFPInfo": mc2200_Q2202LocalLANSFPInfo,
       "mc2200-Q2202LocalWANLink": mc2200_Q2202LocalWANLink,
       "mc2200-Q2202LocalWANTxStatus": mc2200_Q2202LocalWANTxStatus,
       "mc2200-Q2202LocalWANSFPInfo": mc2200_Q2202LocalWANSFPInfo,
       "mc2200-Q2202Loopback": mc2200_Q2202Loopback,
       "mc2200-Q2202RFD": mc2200_Q2202RFD,
       "mc2200-Q2202Default": mc2200_Q2202Default,
       "mc2200-Q2202Reboot": mc2200_Q2202Reboot,
       "mc2200-Q2202LocalLANuser": mc2200_Q2202LocalLANuser,
       "mc2200-Q2202Rate": mc2200_Q2202Rate,
       "mc2200-GESFP2Table": mc2200_GESFP2Table,
       "mc2200-GESFP2Entry": mc2200_GESFP2Entry,
       "mc2200-GESFP2CardIndex": mc2200_GESFP2CardIndex,
       "mc2200-GESFP2LocalTXLink": mc2200_GESFP2LocalTXLink,
       "mc2200-GESFP2LocalWANSFPInfo": mc2200_GESFP2LocalWANSFPInfo,
       "mc2200-GESFP2LocalWANLink": mc2200_GESFP2LocalWANLink,
       "mc2200-GESFP2LocalTXMode": mc2200_GESFP2LocalTXMode,
       "mc2200-GESFP2LocalTXMDIX": mc2200_GESFP2LocalTXMDIX,
       "mc2200-GESFP2RxGoodOctets": mc2200_GESFP2RxGoodOctets,
       "mc2200-GESFP2RxBadOctets": mc2200_GESFP2RxBadOctets,
       "mc2200-GESFP2TxFCSErr": mc2200_GESFP2TxFCSErr,
       "mc2200-GESFP2RxUnicast": mc2200_GESFP2RxUnicast,
       "mc2200-GESFP2TxDeferred": mc2200_GESFP2TxDeferred,
       "mc2200-GESFP2RxBroadcasts": mc2200_GESFP2RxBroadcasts,
       "mc2200-GESFP2RxMulticasts": mc2200_GESFP2RxMulticasts,
       "mc2200-GESFP2Rx64Octets": mc2200_GESFP2Rx64Octets,
       "mc2200-GESFP2Rx65to127Octets": mc2200_GESFP2Rx65to127Octets,
       "mc2200-GESFP2Rx128to255Octets": mc2200_GESFP2Rx128to255Octets,
       "mc2200-GESFP2Rx256to511Octets": mc2200_GESFP2Rx256to511Octets,
       "mc2200-GESFP2Rx512to1023Octets": mc2200_GESFP2Rx512to1023Octets,
       "mc2200-GESFP2Rx1024toMaxOctets": mc2200_GESFP2Rx1024toMaxOctets,
       "mc2200-GESFP2TxOctets": mc2200_GESFP2TxOctets,
       "mc2200-GESFP2TxUnicast": mc2200_GESFP2TxUnicast,
       "mc2200-GESFP2TxExcessive": mc2200_GESFP2TxExcessive,
       "mc2200-GESFP2TxMulticasts": mc2200_GESFP2TxMulticasts,
       "mc2200-GESFP2TxBroadcasts": mc2200_GESFP2TxBroadcasts,
       "mc2200-GESFP2TxSingle": mc2200_GESFP2TxSingle,
       "mc2200-GESFP2TxPause": mc2200_GESFP2TxPause,
       "mc2200-GESFP2RxPause": mc2200_GESFP2RxPause,
       "mc2200-GESFP2TxMultiple": mc2200_GESFP2TxMultiple,
       "mc2200-GESFP2RxUndersize": mc2200_GESFP2RxUndersize,
       "mc2200-GESFP2RxFragments": mc2200_GESFP2RxFragments,
       "mc2200-GESFP2RxOversize": mc2200_GESFP2RxOversize,
       "mc2200-GESFP2RxJabber": mc2200_GESFP2RxJabber,
       "mc2200-GESFP2RxErr": mc2200_GESFP2RxErr,
       "mc2200-GESFP2RxFCSErr": mc2200_GESFP2RxFCSErr,
       "mc2200-GESFP2TxCollisions": mc2200_GESFP2TxCollisions,
       "mc2200-GESFP2TxLate": mc2200_GESFP2TxLate,
       "mc2200-GESFP2RemoteWANSFPInfo": mc2200_GESFP2RemoteWANSFPInfo,
       "mc2200-GESFP2RemoteWANLink": mc2200_GESFP2RemoteWANLink,
       "mc2200-GESFP2RemotePort1Link": mc2200_GESFP2RemotePort1Link,
       "mc2200-GESFP2RemotePort1Speed": mc2200_GESFP2RemotePort1Speed,
       "mc2200-GESFP2RemotePort1Duplex": mc2200_GESFP2RemotePort1Duplex,
       "mc2200-GESFP2RemotePort1Mode": mc2200_GESFP2RemotePort1Mode,
       "mc2200-GESFP2RemotePort1MDIX": mc2200_GESFP2RemotePort1MDIX,
       "mc2200-GESFP2RemotePort2Link": mc2200_GESFP2RemotePort2Link,
       "mc2200-GESFP2RemotePort2Speed": mc2200_GESFP2RemotePort2Speed,
       "mc2200-GESFP2RemotePort2Duplex": mc2200_GESFP2RemotePort2Duplex,
       "mc2200-GESFP2RemotePort2Mode": mc2200_GESFP2RemotePort2Mode,
       "mc2200-GESFP2RemotePort2MDIX": mc2200_GESFP2RemotePort2MDIX,
       "mc2200-GESFP2RemotePort3Link": mc2200_GESFP2RemotePort3Link,
       "mc2200-GESFP2RemotePort3Speed": mc2200_GESFP2RemotePort3Speed,
       "mc2200-GESFP2RemotePort3Duplex": mc2200_GESFP2RemotePort3Duplex,
       "mc2200-GESFP2RemotePort3Mode": mc2200_GESFP2RemotePort3Mode,
       "mc2200-GESFP2RemotePort3MDIX": mc2200_GESFP2RemotePort3MDIX,
       "mc2200-GESFP2RemotePort4Link": mc2200_GESFP2RemotePort4Link,
       "mc2200-GESFP2RemotePort4Speed": mc2200_GESFP2RemotePort4Speed,
       "mc2200-GESFP2RemotePort4Duplex": mc2200_GESFP2RemotePort4Duplex,
       "mc2200-GESFP2RemotePort4Mode": mc2200_GESFP2RemotePort4Mode,
       "mc2200-GESFP2RemotePort4MDIX": mc2200_GESFP2RemotePort4MDIX,
       "mc2200-GESFP2RemotePort5Link": mc2200_GESFP2RemotePort5Link,
       "mc2200-GESFP2RemotePort5Speed": mc2200_GESFP2RemotePort5Speed,
       "mc2200-GESFP2RemotePort5Duplex": mc2200_GESFP2RemotePort5Duplex,
       "mc2200-GESFP2RemotePort5Mode": mc2200_GESFP2RemotePort5Mode,
       "mc2200-GESFP2RemotePort5MDIX": mc2200_GESFP2RemotePort5MDIX,
       "mc2200-GESFP2RemotePort6Link": mc2200_GESFP2RemotePort6Link,
       "mc2200-GESFP2RemotePort6Speed": mc2200_GESFP2RemotePort6Speed,
       "mc2200-GESFP2RemotePort6Duplex": mc2200_GESFP2RemotePort6Duplex,
       "mc2200-GESFP2RemotePort6Mode": mc2200_GESFP2RemotePort6Mode,
       "mc2200-GESFP2RemotePort6MDIX": mc2200_GESFP2RemotePort6MDIX,
       "mc2200-GESFP2RemotePort7Link": mc2200_GESFP2RemotePort7Link,
       "mc2200-GESFP2RemotePort7Speed": mc2200_GESFP2RemotePort7Speed,
       "mc2200-GESFP2RemotePort7Duplex": mc2200_GESFP2RemotePort7Duplex,
       "mc2200-GESFP2RemotePort7Mode": mc2200_GESFP2RemotePort7Mode,
       "mc2200-GESFP2RemotePort7MDIX": mc2200_GESFP2RemotePort7MDIX,
       "mc2200-GESFP2RemotePort8Link": mc2200_GESFP2RemotePort8Link,
       "mc2200-GESFP2RemotePort8Speed": mc2200_GESFP2RemotePort8Speed,
       "mc2200-GESFP2RemotePort8Duplex": mc2200_GESFP2RemotePort8Duplex,
       "mc2200-GESFP2RemotePort8Mode": mc2200_GESFP2RemotePort8Mode,
       "mc2200-GESFP2RemotePort8MDIX": mc2200_GESFP2RemotePort8MDIX,
       "mc2200-GESFP2RemotePort9Link": mc2200_GESFP2RemotePort9Link,
       "mc2200-GESFP2RemotePort9Speed": mc2200_GESFP2RemotePort9Speed,
       "mc2200-GESFP2RemotePort9Duplex": mc2200_GESFP2RemotePort9Duplex,
       "mc2200-GESFP2RemotePort9Mode": mc2200_GESFP2RemotePort9Mode,
       "mc2200-GESFP2RemotePort9SFPInfo": mc2200_GESFP2RemotePort9SFPInfo,
       "mc2200-GESFP2RemoteIPAddress": mc2200_GESFP2RemoteIPAddress,
       "mc2200-GESFP2RemoteSubnetMask": mc2200_GESFP2RemoteSubnetMask,
       "mc2200-GESFP2RemoteGateWay": mc2200_GESFP2RemoteGateWay,
       "mc2200-GESFP2RemoteVLANEnable": mc2200_GESFP2RemoteVLANEnable,
       "mc2200-GESFP2RemoteVID": mc2200_GESFP2RemoteVID,
       "mc2200-GESFP2RemoteAlarm": mc2200_GESFP2RemoteAlarm,
       "mc2200-GESFP2Default": mc2200_GESFP2Default,
       "mc2200-GESFP2Reboot": mc2200_GESFP2Reboot,
       "mc2200-GESFP2LocalTXSpeed": mc2200_GESFP2LocalTXSpeed,
       "mc2200-GESFP2RemoteLanIsolate": mc2200_GESFP2RemoteLanIsolate,
       "mc2200-GESFP2Localportuser": mc2200_GESFP2Localportuser,
       "mc2200-GESFP2Remoteportuser1": mc2200_GESFP2Remoteportuser1,
       "mc2200-GESFP2Remoteportuser2": mc2200_GESFP2Remoteportuser2,
       "mc2200-GESFP2Remoteportuser3": mc2200_GESFP2Remoteportuser3,
       "mc2200-GESFP2Remoteportuser4": mc2200_GESFP2Remoteportuser4,
       "mc2200-GESFP2Remoteportuser5": mc2200_GESFP2Remoteportuser5,
       "mc2200-GESFP2Remoteportuser6": mc2200_GESFP2Remoteportuser6,
       "mc2200-GESFP2Remoteportuser7": mc2200_GESFP2Remoteportuser7,
       "mc2200-GESFP2Remoteportuser8": mc2200_GESFP2Remoteportuser8,
       "mc2200-GESFP2Remoteportuser9": mc2200_GESFP2Remoteportuser9,
       "mc2200-GESFP2LocalTXDuplex": mc2200_GESFP2LocalTXDuplex,
       "mc2200-GESFP2WANOpticalPowerCheck": mc2200_GESFP2WANOpticalPowerCheck,
       "mc2200-GESFP2WANThreshold": mc2200_GESFP2WANThreshold,
       "mc2200-GESFP2TrapFilterLocalLAN": mc2200_GESFP2TrapFilterLocalLAN,
       "mc2200-GESFP2TrapFilterLocalWAN": mc2200_GESFP2TrapFilterLocalWAN,
       "mc2200-GESFP2TrapFilterRemotePower": mc2200_GESFP2TrapFilterRemotePower,
       "mc2200-GESFP2TrapFilterRemoteLAN": mc2200_GESFP2TrapFilterRemoteLAN,
       "mc2200-GESFP2TrapFilterRemoteWAN": mc2200_GESFP2TrapFilterRemoteWAN,
       "mc2200-GESFP2CardType": mc2200_GESFP2CardType,
       "mc2200-GESFP2RemotePort1UpstreamBandwidth": mc2200_GESFP2RemotePort1UpstreamBandwidth,
       "mc2200-GESFP2RemotePort1DownstreamBandwidth": mc2200_GESFP2RemotePort1DownstreamBandwidth,
       "mc2200-GESFP2RemotePort2UpstreamBandwidth": mc2200_GESFP2RemotePort2UpstreamBandwidth,
       "mc2200-GESFP2RemotePort2DownstreamBandwidth": mc2200_GESFP2RemotePort2DownstreamBandwidth,
       "mc2200-GESFP2RemotePort3UpstreamBandwidth": mc2200_GESFP2RemotePort3UpstreamBandwidth,
       "mc2200-GESFP2RemotePort3DownstreamBandwidth": mc2200_GESFP2RemotePort3DownstreamBandwidth,
       "mc2200-GESFP2RemotePort4UpstreamBandwidth": mc2200_GESFP2RemotePort4UpstreamBandwidth,
       "mc2200-GESFP2RemotePort4DownstreamBandwidth": mc2200_GESFP2RemotePort4DownstreamBandwidth,
       "mc2200-GESFP2RemotePort5UpstreamBandwidth": mc2200_GESFP2RemotePort5UpstreamBandwidth,
       "mc2200-GESFP2RemotePort5DownstreamBandwidth": mc2200_GESFP2RemotePort5DownstreamBandwidth,
       "mc2200-GESFP2RemotePort6UpstreamBandwidth": mc2200_GESFP2RemotePort6UpstreamBandwidth,
       "mc2200-GESFP2RemotePort6DownstreamBandwidth": mc2200_GESFP2RemotePort6DownstreamBandwidth,
       "mc2200-GESFP2RemotePort7UpstreamBandwidth": mc2200_GESFP2RemotePort7UpstreamBandwidth,
       "mc2200-GESFP2RemotePort7DownstreamBandwidth": mc2200_GESFP2RemotePort7DownstreamBandwidth,
       "mc2200-GESFP2RemotePort8UpstreamBandwidth": mc2200_GESFP2RemotePort8UpstreamBandwidth,
       "mc2200-GESFP2RemotePort8DownstreamBandwidth": mc2200_GESFP2RemotePort8DownstreamBandwidth,
       "mc2200-GESFP2RemotePort9UpstreamBandwidth": mc2200_GESFP2RemotePort9UpstreamBandwidth,
       "mc2200-GESFP2RemotePort9DownstreamBandwidth": mc2200_GESFP2RemotePort9DownstreamBandwidth,
       "mc2200-FEMCTable": mc2200_FEMCTable,
       "mc2200-FEMCEntry": mc2200_FEMCEntry,
       "mc2200-FEMCCardIndex": mc2200_FEMCCardIndex,
       "mc2200-FEMCLocalLANSFPInfo": mc2200_FEMCLocalLANSFPInfo,
       "mc2200-FEMCLocalLANLink": mc2200_FEMCLocalLANLink,
       "mc2200-FEMCLocalWANSFPInfo": mc2200_FEMCLocalWANSFPInfo,
       "mc2200-FEMCLocalWANLink": mc2200_FEMCLocalWANLink,
       "mc2200-FEMCLocalLANDownStreamBW": mc2200_FEMCLocalLANDownStreamBW,
       "mc2200-FEMCLocalLANUpStreamBW": mc2200_FEMCLocalLANUpStreamBW,
       "mc2200-FEMCLocalLANMode": mc2200_FEMCLocalLANMode,
       "mc2200-FEMCRxGoodOctets": mc2200_FEMCRxGoodOctets,
       "mc2200-FEMCRxBadOctets": mc2200_FEMCRxBadOctets,
       "mc2200-FEMCTxFCSErr": mc2200_FEMCTxFCSErr,
       "mc2200-FEMCRxUnicast": mc2200_FEMCRxUnicast,
       "mc2200-FEMCTxDeferred": mc2200_FEMCTxDeferred,
       "mc2200-FEMCRxBroadcasts": mc2200_FEMCRxBroadcasts,
       "mc2200-FEMCRxMulticasts": mc2200_FEMCRxMulticasts,
       "mc2200-FEMCRx64Octets": mc2200_FEMCRx64Octets,
       "mc2200-FEMCRx65to127Octets": mc2200_FEMCRx65to127Octets,
       "mc2200-FEMCRx128to255Octets": mc2200_FEMCRx128to255Octets,
       "mc2200-FEMCRx256to511Octets": mc2200_FEMCRx256to511Octets,
       "mc2200-FEMCRx512to1023Octets": mc2200_FEMCRx512to1023Octets,
       "mc2200-FEMCRx1024toMaxOctets": mc2200_FEMCRx1024toMaxOctets,
       "mc2200-FEMCTxOctets": mc2200_FEMCTxOctets,
       "mc2200-FEMCTxUnicast": mc2200_FEMCTxUnicast,
       "mc2200-FEMCTxExcessive": mc2200_FEMCTxExcessive,
       "mc2200-FEMCTxMulticasts": mc2200_FEMCTxMulticasts,
       "mc2200-FEMCTxBroadcasts": mc2200_FEMCTxBroadcasts,
       "mc2200-FEMCTxSingle": mc2200_FEMCTxSingle,
       "mc2200-FEMCTxPause": mc2200_FEMCTxPause,
       "mc2200-FEMCRxPause": mc2200_FEMCRxPause,
       "mc2200-FEMCTxMultiple": mc2200_FEMCTxMultiple,
       "mc2200-FEMCRxUndersize": mc2200_FEMCRxUndersize,
       "mc2200-FEMCRxFragments": mc2200_FEMCRxFragments,
       "mc2200-FEMCRxOversize": mc2200_FEMCRxOversize,
       "mc2200-FEMCRxJabber": mc2200_FEMCRxJabber,
       "mc2200-FEMCRxErr": mc2200_FEMCRxErr,
       "mc2200-FEMCRxFCSErr": mc2200_FEMCRxFCSErr,
       "mc2200-FEMCTxCollisions": mc2200_FEMCTxCollisions,
       "mc2200-FEMCTxLate": mc2200_FEMCTxLate,
       "mc2200-FEMCRemoteLANSFPInfo": mc2200_FEMCRemoteLANSFPInfo,
       "mc2200-FEMCRemoteLANLink": mc2200_FEMCRemoteLANLink,
       "mc2200-FEMCRemoteWANSFPInfo": mc2200_FEMCRemoteWANSFPInfo,
       "mc2200-FEMCRemoteWANLink": mc2200_FEMCRemoteWANLink,
       "mc2200-FEMCRemoteLANMode": mc2200_FEMCRemoteLANMode,
       "mc2200-FEMCRemoteIPAddress": mc2200_FEMCRemoteIPAddress,
       "mc2200-FEMCRemoteSubnetMask": mc2200_FEMCRemoteSubnetMask,
       "mc2200-FEMCRemoteGateWay": mc2200_FEMCRemoteGateWay,
       "mc2200-FEMCRemoteVLANEnable": mc2200_FEMCRemoteVLANEnable,
       "mc2200-FEMCRemoteVID": mc2200_FEMCRemoteVID,
       "mc2200-FEMCRemoteAlarm": mc2200_FEMCRemoteAlarm,
       "mc2200-FEMCRFD": mc2200_FEMCRFD,
       "mc2200-FEMCDefault": mc2200_FEMCDefault,
       "mc2200-FEMCReboot": mc2200_FEMCReboot,
       "mc2200-FEMCLocalLANSpeed": mc2200_FEMCLocalLANSpeed,
       "mc2200-FEMCRemoteLANSpeed": mc2200_FEMCRemoteLANSpeed,
       "mc2200-FEMCLocalportuser": mc2200_FEMCLocalportuser,
       "mc2200-FEMCRemoteportuser": mc2200_FEMCRemoteportuser,
       "mc2200-FEMCWANOpticalPowerCheck": mc2200_FEMCWANOpticalPowerCheck,
       "mc2200-FEMCWANThreshold": mc2200_FEMCWANThreshold,
       "mc2200-FEMCTrapFilterLocalLAN": mc2200_FEMCTrapFilterLocalLAN,
       "mc2200-FEMCTrapFilterLocalWAN": mc2200_FEMCTrapFilterLocalWAN,
       "mc2200-FEMCTrapFilterRemotePower": mc2200_FEMCTrapFilterRemotePower,
       "mc2200-FEMCTrapFilterRemoteLAN": mc2200_FEMCTrapFilterRemoteLAN,
       "mc2200-FEMCTrapFilterRemoteWAN": mc2200_FEMCTrapFilterRemoteWAN,
       "mc2200-FEMCLoopback": mc2200_FEMCLoopback,
       "mc2200-FEMCCardType": mc2200_FEMCCardType}
)
