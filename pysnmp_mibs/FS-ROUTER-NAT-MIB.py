# SNMP MIB module (FS-ROUTER-NAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-ROUTER-NAT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:29 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsNatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136)
)
if mibBuilder.loadTexts:
    fsNatMIB.setRevisions(
        ("2015-03-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FSNatType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inside", 1),
          ("outside", 2),
          ("application", 3))
    )



class FSNatSrcDstType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("source", 1),
          ("destination", 2))
    )



class FSNatTcpUdpType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2),
          ("all", 3))
    )



class FSNatPoolAddressntmskprefixFlag(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("netmask", 1),
          ("prefix-length", 2))
    )



# MIB Managed Objects in the order of their OIDs

_FsNatMIBObjects_ObjectIdentity = ObjectIdentity
fsNatMIBObjects = _FsNatMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1)
)
_FsNatSettingObjects_ObjectIdentity = ObjectIdentity
fsNatSettingObjects = _FsNatSettingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 1)
)
_FsNatSettingTable_Object = MibTable
fsNatSettingTable = _FsNatSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fsNatSettingTable.setStatus("current")
_FsNatSettingEntry_Object = MibTableRow
fsNatSettingEntry = _FsNatSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 1, 1, 1)
)
fsNatSettingEntry.setIndexNames(
    (0, "FS-ROUTER-NAT-MIB", "fsNatSettingIndex"),
)
if mibBuilder.loadTexts:
    fsNatSettingEntry.setStatus("current")
_FsNatSettingIndex_Type = Integer32
_FsNatSettingIndex_Object = MibTableColumn
fsNatSettingIndex = _FsNatSettingIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 1, 1, 1, 1),
    _FsNatSettingIndex_Type()
)
fsNatSettingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNatSettingIndex.setStatus("current")


class _FsNatSettingisno_Type(Integer32):
    """Custom type fsNatSettingisno based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsNatSettingisno_Type.__name__ = "Integer32"
_FsNatSettingisno_Object = MibTableColumn
fsNatSettingisno = _FsNatSettingisno_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 1, 1, 1, 2),
    _FsNatSettingisno_Type()
)
fsNatSettingisno.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatSettingisno.setStatus("current")
_FsNatSettingtype_Type = FSNatType
_FsNatSettingtype_Object = MibTableColumn
fsNatSettingtype = _FsNatSettingtype_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 1, 1, 1, 3),
    _FsNatSettingtype_Type()
)
fsNatSettingtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatSettingtype.setStatus("current")
_FsNatSettingsrcdst_Type = FSNatSrcDstType
_FsNatSettingsrcdst_Object = MibTableColumn
fsNatSettingsrcdst = _FsNatSettingsrcdst_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 1, 1, 1, 4),
    _FsNatSettingsrcdst_Type()
)
fsNatSettingsrcdst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatSettingsrcdst.setStatus("current")


class _FsNatSettingacltype_Type(Integer32):
    """Custom type fsNatSettingacltype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsNatSettingacltype_Type.__name__ = "Integer32"
_FsNatSettingacltype_Object = MibTableColumn
fsNatSettingacltype = _FsNatSettingacltype_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 1, 1, 1, 5),
    _FsNatSettingacltype_Type()
)
fsNatSettingacltype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatSettingacltype.setStatus("current")
_FsNatSettingaclnumber_Type = Integer32
_FsNatSettingaclnumber_Object = MibTableColumn
fsNatSettingaclnumber = _FsNatSettingaclnumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 1, 1, 1, 6),
    _FsNatSettingaclnumber_Type()
)
fsNatSettingaclnumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatSettingaclnumber.setStatus("current")


class _FsNatSettingaclname_Type(DisplayString):
    """Custom type fsNatSettingaclname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FsNatSettingaclname_Type.__name__ = "DisplayString"
_FsNatSettingaclname_Object = MibTableColumn
fsNatSettingaclname = _FsNatSettingaclname_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 1, 1, 1, 7),
    _FsNatSettingaclname_Type()
)
fsNatSettingaclname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatSettingaclname.setStatus("current")


class _FsNatSettingstaticrule_Type(Integer32):
    """Custom type fsNatSettingstaticrule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsNatSettingstaticrule_Type.__name__ = "Integer32"
_FsNatSettingstaticrule_Object = MibTableColumn
fsNatSettingstaticrule = _FsNatSettingstaticrule_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 1, 1, 1, 8),
    _FsNatSettingstaticrule_Type()
)
fsNatSettingstaticrule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatSettingstaticrule.setStatus("current")
_FsNatSettingproto_Type = FSNatTcpUdpType
_FsNatSettingproto_Object = MibTableColumn
fsNatSettingproto = _FsNatSettingproto_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 1, 1, 1, 9),
    _FsNatSettingproto_Type()
)
fsNatSettingproto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatSettingproto.setStatus("current")
_FsNatSettinginlocalip_Type = IpAddress
_FsNatSettinginlocalip_Object = MibTableColumn
fsNatSettinginlocalip = _FsNatSettinginlocalip_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 1, 1, 1, 10),
    _FsNatSettinginlocalip_Type()
)
fsNatSettinginlocalip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatSettinginlocalip.setStatus("current")
_FsNatSettinginglobalip_Type = IpAddress
_FsNatSettinginglobalip_Object = MibTableColumn
fsNatSettinginglobalip = _FsNatSettinginglobalip_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 1, 1, 1, 11),
    _FsNatSettinginglobalip_Type()
)
fsNatSettinginglobalip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatSettinginglobalip.setStatus("current")
_FsNatSettingnetmask_Type = IpAddress
_FsNatSettingnetmask_Object = MibTableColumn
fsNatSettingnetmask = _FsNatSettingnetmask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 1, 1, 1, 12),
    _FsNatSettingnetmask_Type()
)
fsNatSettingnetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatSettingnetmask.setStatus("current")
_FsNatSettinglocalport_Type = Integer32
_FsNatSettinglocalport_Object = MibTableColumn
fsNatSettinglocalport = _FsNatSettinglocalport_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 1, 1, 1, 13),
    _FsNatSettinglocalport_Type()
)
fsNatSettinglocalport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatSettinglocalport.setStatus("current")
_FsNatSettingglobalport_Type = Integer32
_FsNatSettingglobalport_Object = MibTableColumn
fsNatSettingglobalport = _FsNatSettingglobalport_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 1, 1, 1, 14),
    _FsNatSettingglobalport_Type()
)
fsNatSettingglobalport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatSettingglobalport.setStatus("current")
_FsNatSettingmatchinterface_Type = Integer32
_FsNatSettingmatchinterface_Object = MibTableColumn
fsNatSettingmatchinterface = _FsNatSettingmatchinterface_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 1, 1, 1, 15),
    _FsNatSettingmatchinterface_Type()
)
fsNatSettingmatchinterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatSettingmatchinterface.setStatus("current")
_FsNatSettingpermisinside_Type = Integer32
_FsNatSettingpermisinside_Object = MibTableColumn
fsNatSettingpermisinside = _FsNatSettingpermisinside_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 1, 1, 1, 16),
    _FsNatSettingpermisinside_Type()
)
fsNatSettingpermisinside.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatSettingpermisinside.setStatus("current")
_FsNatSettinginterface_Type = Integer32
_FsNatSettinginterface_Object = MibTableColumn
fsNatSettinginterface = _FsNatSettinginterface_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 1, 1, 1, 17),
    _FsNatSettinginterface_Type()
)
fsNatSettinginterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatSettinginterface.setStatus("current")


class _FsNatSettingpool_Type(DisplayString):
    """Custom type fsNatSettingpool based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FsNatSettingpool_Type.__name__ = "DisplayString"
_FsNatSettingpool_Object = MibTableColumn
fsNatSettingpool = _FsNatSettingpool_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 1, 1, 1, 18),
    _FsNatSettingpool_Type()
)
fsNatSettingpool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatSettingpool.setStatus("current")
_FsNatSettingdstchange_Type = IpAddress
_FsNatSettingdstchange_Object = MibTableColumn
fsNatSettingdstchange = _FsNatSettingdstchange_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 1, 1, 1, 19),
    _FsNatSettingdstchange_Type()
)
fsNatSettingdstchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatSettingdstchange.setStatus("current")
_FsNatSettingsrcchange_Type = IpAddress
_FsNatSettingsrcchange_Object = MibTableColumn
fsNatSettingsrcchange = _FsNatSettingsrcchange_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 1, 1, 1, 20),
    _FsNatSettingsrcchange_Type()
)
fsNatSettingsrcchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatSettingsrcchange.setStatus("current")
_FsNatPoolAddressObjects_ObjectIdentity = ObjectIdentity
fsNatPoolAddressObjects = _FsNatPoolAddressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 2)
)
_FsNatPoolAddressTable_Object = MibTable
fsNatPoolAddressTable = _FsNatPoolAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsNatPoolAddressTable.setStatus("current")
_FsNatPoolAddressEntry_Object = MibTableRow
fsNatPoolAddressEntry = _FsNatPoolAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 2, 1, 1)
)
fsNatPoolAddressEntry.setIndexNames(
    (0, "FS-ROUTER-NAT-MIB", "fsNatPoolAddressIndex"),
)
if mibBuilder.loadTexts:
    fsNatPoolAddressEntry.setStatus("current")
_FsNatPoolAddressIndex_Type = Integer32
_FsNatPoolAddressIndex_Object = MibTableColumn
fsNatPoolAddressIndex = _FsNatPoolAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 2, 1, 1, 1),
    _FsNatPoolAddressIndex_Type()
)
fsNatPoolAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNatPoolAddressIndex.setStatus("current")


class _FsNatPoolAddressisno_Type(Integer32):
    """Custom type fsNatPoolAddressisno based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsNatPoolAddressisno_Type.__name__ = "Integer32"
_FsNatPoolAddressisno_Object = MibTableColumn
fsNatPoolAddressisno = _FsNatPoolAddressisno_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 2, 1, 1, 2),
    _FsNatPoolAddressisno_Type()
)
fsNatPoolAddressisno.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatPoolAddressisno.setStatus("current")


class _FsNatPoolAddressname_Type(DisplayString):
    """Custom type fsNatPoolAddressname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FsNatPoolAddressname_Type.__name__ = "DisplayString"
_FsNatPoolAddressname_Object = MibTableColumn
fsNatPoolAddressname = _FsNatPoolAddressname_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 2, 1, 1, 3),
    _FsNatPoolAddressname_Type()
)
fsNatPoolAddressname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatPoolAddressname.setStatus("current")
_FsNatPoolAddressntmskprefix_Type = FSNatPoolAddressntmskprefixFlag
_FsNatPoolAddressntmskprefix_Object = MibTableColumn
fsNatPoolAddressntmskprefix = _FsNatPoolAddressntmskprefix_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 2, 1, 1, 4),
    _FsNatPoolAddressntmskprefix_Type()
)
fsNatPoolAddressntmskprefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatPoolAddressntmskprefix.setStatus("current")
_FsNatPoolAddressnetmask_Type = IpAddress
_FsNatPoolAddressnetmask_Object = MibTableColumn
fsNatPoolAddressnetmask = _FsNatPoolAddressnetmask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 2, 1, 1, 5),
    _FsNatPoolAddressnetmask_Type()
)
fsNatPoolAddressnetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatPoolAddressnetmask.setStatus("current")
_FsNatPoolAddressprefixlength_Type = Integer32
_FsNatPoolAddressprefixlength_Object = MibTableColumn
fsNatPoolAddressprefixlength = _FsNatPoolAddressprefixlength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 2, 1, 1, 6),
    _FsNatPoolAddressprefixlength_Type()
)
fsNatPoolAddressprefixlength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatPoolAddressprefixlength.setStatus("current")
_FsNatPoolAddressstartip_Type = IpAddress
_FsNatPoolAddressstartip_Object = MibTableColumn
fsNatPoolAddressstartip = _FsNatPoolAddressstartip_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 2, 1, 1, 7),
    _FsNatPoolAddressstartip_Type()
)
fsNatPoolAddressstartip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatPoolAddressstartip.setStatus("current")
_FsNatPoolAddressendip_Type = IpAddress
_FsNatPoolAddressendip_Object = MibTableColumn
fsNatPoolAddressendip = _FsNatPoolAddressendip_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 2, 1, 1, 8),
    _FsNatPoolAddressendip_Type()
)
fsNatPoolAddressendip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatPoolAddressendip.setStatus("current")
_FsNatPoolAddressstartinterface_Type = Integer32
_FsNatPoolAddressstartinterface_Object = MibTableColumn
fsNatPoolAddressstartinterface = _FsNatPoolAddressstartinterface_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 2, 1, 1, 9),
    _FsNatPoolAddressstartinterface_Type()
)
fsNatPoolAddressstartinterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatPoolAddressstartinterface.setStatus("current")
_FsNatPoolAddressendinterface_Type = Integer32
_FsNatPoolAddressendinterface_Object = MibTableColumn
fsNatPoolAddressendinterface = _FsNatPoolAddressendinterface_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 2, 1, 1, 10),
    _FsNatPoolAddressendinterface_Type()
)
fsNatPoolAddressendinterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatPoolAddressendinterface.setStatus("current")
_FsNatPoolAddresstype_Type = Integer32
_FsNatPoolAddresstype_Object = MibTableColumn
fsNatPoolAddresstype = _FsNatPoolAddresstype_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 2, 1, 1, 11),
    _FsNatPoolAddresstype_Type()
)
fsNatPoolAddresstype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatPoolAddresstype.setStatus("current")
_FsNatInterfaceObjects_ObjectIdentity = ObjectIdentity
fsNatInterfaceObjects = _FsNatInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 3)
)
_FsNatInterfaceTable_Object = MibTable
fsNatInterfaceTable = _FsNatInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fsNatInterfaceTable.setStatus("current")
_FsNatInterfaceEntry_Object = MibTableRow
fsNatInterfaceEntry = _FsNatInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 3, 1, 1)
)
fsNatInterfaceEntry.setIndexNames(
    (0, "FS-ROUTER-NAT-MIB", "fsNatInterfaceIndex"),
)
if mibBuilder.loadTexts:
    fsNatInterfaceEntry.setStatus("current")
_FsNatInterfaceIndex_Type = Integer32
_FsNatInterfaceIndex_Object = MibTableColumn
fsNatInterfaceIndex = _FsNatInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 3, 1, 1, 1),
    _FsNatInterfaceIndex_Type()
)
fsNatInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNatInterfaceIndex.setStatus("current")


class _FsNatInterfaceisno_Type(Integer32):
    """Custom type fsNatInterfaceisno based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsNatInterfaceisno_Type.__name__ = "Integer32"
_FsNatInterfaceisno_Object = MibTableColumn
fsNatInterfaceisno = _FsNatInterfaceisno_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 3, 1, 1, 2),
    _FsNatInterfaceisno_Type()
)
fsNatInterfaceisno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNatInterfaceisno.setStatus("current")
_FsNatInterfacedirector_Type = Integer32
_FsNatInterfacedirector_Object = MibTableColumn
fsNatInterfacedirector = _FsNatInterfacedirector_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 136, 1, 3, 1, 1, 3),
    _FsNatInterfacedirector_Type()
)
fsNatInterfacedirector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNatInterfacedirector.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-ROUTER-NAT-MIB",
    **{"FSNatType": FSNatType,
       "FSNatSrcDstType": FSNatSrcDstType,
       "FSNatTcpUdpType": FSNatTcpUdpType,
       "FSNatPoolAddressntmskprefixFlag": FSNatPoolAddressntmskprefixFlag,
       "fsNatMIB": fsNatMIB,
       "fsNatMIBObjects": fsNatMIBObjects,
       "fsNatSettingObjects": fsNatSettingObjects,
       "fsNatSettingTable": fsNatSettingTable,
       "fsNatSettingEntry": fsNatSettingEntry,
       "fsNatSettingIndex": fsNatSettingIndex,
       "fsNatSettingisno": fsNatSettingisno,
       "fsNatSettingtype": fsNatSettingtype,
       "fsNatSettingsrcdst": fsNatSettingsrcdst,
       "fsNatSettingacltype": fsNatSettingacltype,
       "fsNatSettingaclnumber": fsNatSettingaclnumber,
       "fsNatSettingaclname": fsNatSettingaclname,
       "fsNatSettingstaticrule": fsNatSettingstaticrule,
       "fsNatSettingproto": fsNatSettingproto,
       "fsNatSettinginlocalip": fsNatSettinginlocalip,
       "fsNatSettinginglobalip": fsNatSettinginglobalip,
       "fsNatSettingnetmask": fsNatSettingnetmask,
       "fsNatSettinglocalport": fsNatSettinglocalport,
       "fsNatSettingglobalport": fsNatSettingglobalport,
       "fsNatSettingmatchinterface": fsNatSettingmatchinterface,
       "fsNatSettingpermisinside": fsNatSettingpermisinside,
       "fsNatSettinginterface": fsNatSettinginterface,
       "fsNatSettingpool": fsNatSettingpool,
       "fsNatSettingdstchange": fsNatSettingdstchange,
       "fsNatSettingsrcchange": fsNatSettingsrcchange,
       "fsNatPoolAddressObjects": fsNatPoolAddressObjects,
       "fsNatPoolAddressTable": fsNatPoolAddressTable,
       "fsNatPoolAddressEntry": fsNatPoolAddressEntry,
       "fsNatPoolAddressIndex": fsNatPoolAddressIndex,
       "fsNatPoolAddressisno": fsNatPoolAddressisno,
       "fsNatPoolAddressname": fsNatPoolAddressname,
       "fsNatPoolAddressntmskprefix": fsNatPoolAddressntmskprefix,
       "fsNatPoolAddressnetmask": fsNatPoolAddressnetmask,
       "fsNatPoolAddressprefixlength": fsNatPoolAddressprefixlength,
       "fsNatPoolAddressstartip": fsNatPoolAddressstartip,
       "fsNatPoolAddressendip": fsNatPoolAddressendip,
       "fsNatPoolAddressstartinterface": fsNatPoolAddressstartinterface,
       "fsNatPoolAddressendinterface": fsNatPoolAddressendinterface,
       "fsNatPoolAddresstype": fsNatPoolAddresstype,
       "fsNatInterfaceObjects": fsNatInterfaceObjects,
       "fsNatInterfaceTable": fsNatInterfaceTable,
       "fsNatInterfaceEntry": fsNatInterfaceEntry,
       "fsNatInterfaceIndex": fsNatInterfaceIndex,
       "fsNatInterfaceisno": fsNatInterfaceisno,
       "fsNatInterfacedirector": fsNatInterfacedirector}
)
