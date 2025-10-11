# SNMP MIB module (MY-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ruijie/MY-ACL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:34:30 2025
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

(myMgmt,) = mibBuilder.importSymbols(
    "MY-SMI",
    "myMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "MY-TC",
    "ConfigStatus",
    "IfIndex")

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

myAclMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17)
)
if mibBuilder.loadTexts:
    myAclMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MyAclMIBObjects_ObjectIdentity = ObjectIdentity
myAclMIBObjects = _MyAclMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1)
)
_MyAclTable_Object = MibTable
myAclTable = _MyAclTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 1)
)
if mibBuilder.loadTexts:
    myAclTable.setStatus("current")
_MyAclEntry_Object = MibTableRow
myAclEntry = _MyAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 1, 1)
)
myAclEntry.setIndexNames(
    (0, "MY-ACL-MIB", "myAclName"),
)
if mibBuilder.loadTexts:
    myAclEntry.setStatus("current")


class _MyAclName_Type(DisplayString):
    """Custom type myAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MyAclName_Type.__name__ = "DisplayString"
_MyAclName_Object = MibTableColumn
myAclName = _MyAclName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 1, 1, 1),
    _MyAclName_Type()
)
myAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myAclName.setStatus("current")


class _MyAclMode_Type(Integer32):
    """Custom type myAclMode based on Integer32"""
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
        *(("acl-ip-standard", 1),
          ("acl-ip-extended", 2),
          ("acl-mac-extended", 3),
          ("acl-expert", 4))
    )


_MyAclMode_Type.__name__ = "Integer32"
_MyAclMode_Object = MibTableColumn
myAclMode = _MyAclMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 1, 1, 2),
    _MyAclMode_Type()
)
myAclMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myAclMode.setStatus("current")
_MyAclEntryStatus_Type = ConfigStatus
_MyAclEntryStatus_Object = MibTableColumn
myAclEntryStatus = _MyAclEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 1, 1, 3),
    _MyAclEntryStatus_Type()
)
myAclEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myAclEntryStatus.setStatus("current")
_MyAceTable_Object = MibTable
myAceTable = _MyAceTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2)
)
if mibBuilder.loadTexts:
    myAceTable.setStatus("current")
_MyAceEntry_Object = MibTableRow
myAceEntry = _MyAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1)
)
myAceEntry.setIndexNames(
    (0, "MY-ACL-MIB", "myAceAclName"),
    (0, "MY-ACL-MIB", "myAceIndex"),
)
if mibBuilder.loadTexts:
    myAceEntry.setStatus("current")


class _MyAceAclName_Type(DisplayString):
    """Custom type myAceAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MyAceAclName_Type.__name__ = "DisplayString"
_MyAceAclName_Object = MibTableColumn
myAceAclName = _MyAceAclName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 1),
    _MyAceAclName_Type()
)
myAceAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myAceAclName.setStatus("current")


class _MyAceIndex_Type(Integer32):
    """Custom type myAceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MyAceIndex_Type.__name__ = "Integer32"
_MyAceIndex_Object = MibTableColumn
myAceIndex = _MyAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 2),
    _MyAceIndex_Type()
)
myAceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myAceIndex.setStatus("current")


class _MyAceIfAnyVID_Type(TruthValue):
    """Custom type myAceIfAnyVID based on TruthValue"""
    defaultValue = 1


_MyAceIfAnyVID_Type.__name__ = "TruthValue"
_MyAceIfAnyVID_Object = MibTableColumn
myAceIfAnyVID = _MyAceIfAnyVID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 3),
    _MyAceIfAnyVID_Type()
)
myAceIfAnyVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceIfAnyVID.setStatus("current")


class _MyAceVID_Type(Unsigned32):
    """Custom type myAceVID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MyAceVID_Type.__name__ = "Unsigned32"
_MyAceVID_Object = MibTableColumn
myAceVID = _MyAceVID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 4),
    _MyAceVID_Type()
)
myAceVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceVID.setStatus("current")


class _MyAceIfAnySourceIp_Type(TruthValue):
    """Custom type myAceIfAnySourceIp based on TruthValue"""
    defaultValue = 1


_MyAceIfAnySourceIp_Type.__name__ = "TruthValue"
_MyAceIfAnySourceIp_Object = MibTableColumn
myAceIfAnySourceIp = _MyAceIfAnySourceIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 5),
    _MyAceIfAnySourceIp_Type()
)
myAceIfAnySourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceIfAnySourceIp.setStatus("current")
_MyAceSourceIp_Type = IpAddress
_MyAceSourceIp_Object = MibTableColumn
myAceSourceIp = _MyAceSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 6),
    _MyAceSourceIp_Type()
)
myAceSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceSourceIp.setStatus("current")


class _MyAceIfAnySourceWildCard_Type(TruthValue):
    """Custom type myAceIfAnySourceWildCard based on TruthValue"""
    defaultValue = 1


_MyAceIfAnySourceWildCard_Type.__name__ = "TruthValue"
_MyAceIfAnySourceWildCard_Object = MibTableColumn
myAceIfAnySourceWildCard = _MyAceIfAnySourceWildCard_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 7),
    _MyAceIfAnySourceWildCard_Type()
)
myAceIfAnySourceWildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceIfAnySourceWildCard.setStatus("current")
_MyAceSourceWildCard_Type = IpAddress
_MyAceSourceWildCard_Object = MibTableColumn
myAceSourceWildCard = _MyAceSourceWildCard_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 8),
    _MyAceSourceWildCard_Type()
)
myAceSourceWildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceSourceWildCard.setStatus("current")


class _MyAceIfAnySourceMacAddr_Type(TruthValue):
    """Custom type myAceIfAnySourceMacAddr based on TruthValue"""
    defaultValue = 1


_MyAceIfAnySourceMacAddr_Type.__name__ = "TruthValue"
_MyAceIfAnySourceMacAddr_Object = MibTableColumn
myAceIfAnySourceMacAddr = _MyAceIfAnySourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 9),
    _MyAceIfAnySourceMacAddr_Type()
)
myAceIfAnySourceMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceIfAnySourceMacAddr.setStatus("current")
_MyAceSourceMacAddr_Type = MacAddress
_MyAceSourceMacAddr_Object = MibTableColumn
myAceSourceMacAddr = _MyAceSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 10),
    _MyAceSourceMacAddr_Type()
)
myAceSourceMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceSourceMacAddr.setStatus("current")


class _MyAceIfAnyDestIp_Type(TruthValue):
    """Custom type myAceIfAnyDestIp based on TruthValue"""
    defaultValue = 1


_MyAceIfAnyDestIp_Type.__name__ = "TruthValue"
_MyAceIfAnyDestIp_Object = MibTableColumn
myAceIfAnyDestIp = _MyAceIfAnyDestIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 11),
    _MyAceIfAnyDestIp_Type()
)
myAceIfAnyDestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceIfAnyDestIp.setStatus("current")
_MyAceDestIp_Type = IpAddress
_MyAceDestIp_Object = MibTableColumn
myAceDestIp = _MyAceDestIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 12),
    _MyAceDestIp_Type()
)
myAceDestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceDestIp.setStatus("current")


class _MyAceIfAnyDestWildCard_Type(TruthValue):
    """Custom type myAceIfAnyDestWildCard based on TruthValue"""
    defaultValue = 1


_MyAceIfAnyDestWildCard_Type.__name__ = "TruthValue"
_MyAceIfAnyDestWildCard_Object = MibTableColumn
myAceIfAnyDestWildCard = _MyAceIfAnyDestWildCard_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 13),
    _MyAceIfAnyDestWildCard_Type()
)
myAceIfAnyDestWildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceIfAnyDestWildCard.setStatus("current")
_MyAceDestIpWildCard_Type = IpAddress
_MyAceDestIpWildCard_Object = MibTableColumn
myAceDestIpWildCard = _MyAceDestIpWildCard_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 14),
    _MyAceDestIpWildCard_Type()
)
myAceDestIpWildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceDestIpWildCard.setStatus("current")


class _MyAceIfAnyDestMacAddr_Type(TruthValue):
    """Custom type myAceIfAnyDestMacAddr based on TruthValue"""
    defaultValue = 1


_MyAceIfAnyDestMacAddr_Type.__name__ = "TruthValue"
_MyAceIfAnyDestMacAddr_Object = MibTableColumn
myAceIfAnyDestMacAddr = _MyAceIfAnyDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 15),
    _MyAceIfAnyDestMacAddr_Type()
)
myAceIfAnyDestMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceIfAnyDestMacAddr.setStatus("current")
_MyAceDestMacAddr_Type = MacAddress
_MyAceDestMacAddr_Object = MibTableColumn
myAceDestMacAddr = _MyAceDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 16),
    _MyAceDestMacAddr_Type()
)
myAceDestMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceDestMacAddr.setStatus("current")


class _MyAceIfAnyEtherLikeType_Type(TruthValue):
    """Custom type myAceIfAnyEtherLikeType based on TruthValue"""
    defaultValue = 1


_MyAceIfAnyEtherLikeType_Type.__name__ = "TruthValue"
_MyAceIfAnyEtherLikeType_Object = MibTableColumn
myAceIfAnyEtherLikeType = _MyAceIfAnyEtherLikeType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 17),
    _MyAceIfAnyEtherLikeType_Type()
)
myAceIfAnyEtherLikeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceIfAnyEtherLikeType.setStatus("current")
_MyAceEtherLikeType_Type = Integer32
_MyAceEtherLikeType_Object = MibTableColumn
myAceEtherLikeType = _MyAceEtherLikeType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 18),
    _MyAceEtherLikeType_Type()
)
myAceEtherLikeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceEtherLikeType.setStatus("current")


class _MyAceIfAnyIpProtocolField_Type(TruthValue):
    """Custom type myAceIfAnyIpProtocolField based on TruthValue"""
    defaultValue = 1


_MyAceIfAnyIpProtocolField_Type.__name__ = "TruthValue"
_MyAceIfAnyIpProtocolField_Object = MibTableColumn
myAceIfAnyIpProtocolField = _MyAceIfAnyIpProtocolField_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 19),
    _MyAceIfAnyIpProtocolField_Type()
)
myAceIfAnyIpProtocolField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceIfAnyIpProtocolField.setStatus("current")
_MyAceIpProtocolField_Type = Integer32
_MyAceIpProtocolField_Object = MibTableColumn
myAceIpProtocolField = _MyAceIpProtocolField_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 20),
    _MyAceIpProtocolField_Type()
)
myAceIpProtocolField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceIpProtocolField.setStatus("current")


class _MyAceIfAnySourceProtocolPort_Type(TruthValue):
    """Custom type myAceIfAnySourceProtocolPort based on TruthValue"""
    defaultValue = 1


_MyAceIfAnySourceProtocolPort_Type.__name__ = "TruthValue"
_MyAceIfAnySourceProtocolPort_Object = MibTableColumn
myAceIfAnySourceProtocolPort = _MyAceIfAnySourceProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 21),
    _MyAceIfAnySourceProtocolPort_Type()
)
myAceIfAnySourceProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceIfAnySourceProtocolPort.setStatus("current")
_MyAceSourceProtocolPort_Type = Integer32
_MyAceSourceProtocolPort_Object = MibTableColumn
myAceSourceProtocolPort = _MyAceSourceProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 22),
    _MyAceSourceProtocolPort_Type()
)
myAceSourceProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceSourceProtocolPort.setStatus("current")


class _MyAceIfAnyDestProtocolPort_Type(TruthValue):
    """Custom type myAceIfAnyDestProtocolPort based on TruthValue"""
    defaultValue = 1


_MyAceIfAnyDestProtocolPort_Type.__name__ = "TruthValue"
_MyAceIfAnyDestProtocolPort_Object = MibTableColumn
myAceIfAnyDestProtocolPort = _MyAceIfAnyDestProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 23),
    _MyAceIfAnyDestProtocolPort_Type()
)
myAceIfAnyDestProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceIfAnyDestProtocolPort.setStatus("current")
_MyAceDestProtocolPort_Type = Integer32
_MyAceDestProtocolPort_Object = MibTableColumn
myAceDestProtocolPort = _MyAceDestProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 24),
    _MyAceDestProtocolPort_Type()
)
myAceDestProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceDestProtocolPort.setStatus("current")


class _MyAceIfAnyProtocolType_Type(TruthValue):
    """Custom type myAceIfAnyProtocolType based on TruthValue"""
    defaultValue = 1


_MyAceIfAnyProtocolType_Type.__name__ = "TruthValue"
_MyAceIfAnyProtocolType_Object = MibTableColumn
myAceIfAnyProtocolType = _MyAceIfAnyProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 25),
    _MyAceIfAnyProtocolType_Type()
)
myAceIfAnyProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceIfAnyProtocolType.setStatus("current")
_MyAceProtocolType_Type = Integer32
_MyAceProtocolType_Object = MibTableColumn
myAceProtocolType = _MyAceProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 26),
    _MyAceProtocolType_Type()
)
myAceProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceProtocolType.setStatus("current")


class _MyAceFlowAction_Type(Integer32):
    """Custom type myAceFlowAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("delay", 2))
    )


_MyAceFlowAction_Type.__name__ = "Integer32"
_MyAceFlowAction_Object = MibTableColumn
myAceFlowAction = _MyAceFlowAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 27),
    _MyAceFlowAction_Type()
)
myAceFlowAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceFlowAction.setStatus("current")
_MyAceEntryStauts_Type = RowStatus
_MyAceEntryStauts_Object = MibTableColumn
myAceEntryStauts = _MyAceEntryStauts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 28),
    _MyAceEntryStauts_Type()
)
myAceEntryStauts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myAceEntryStauts.setStatus("current")


class _MyAceTimeRangeName_Type(DisplayString):
    """Custom type myAceTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MyAceTimeRangeName_Type.__name__ = "DisplayString"
_MyAceTimeRangeName_Object = MibTableColumn
myAceTimeRangeName = _MyAceTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 2, 1, 29),
    _MyAceTimeRangeName_Type()
)
myAceTimeRangeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    myAceTimeRangeName.setStatus("current")
_MyAclIfTable_Object = MibTable
myAclIfTable = _MyAclIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 3)
)
if mibBuilder.loadTexts:
    myAclIfTable.setStatus("current")
_MyAclIfEntry_Object = MibTableRow
myAclIfEntry = _MyAclIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 3, 1)
)
myAclIfEntry.setIndexNames(
    (0, "MY-ACL-MIB", "myAclIfIndex"),
)
if mibBuilder.loadTexts:
    myAclIfEntry.setStatus("current")
_MyAclIfIndex_Type = IfIndex
_MyAclIfIndex_Object = MibTableColumn
myAclIfIndex = _MyAclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 3, 1, 1),
    _MyAclIfIndex_Type()
)
myAclIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myAclIfIndex.setStatus("current")
_MyAclIfMaxEntryNum_Type = Integer32
_MyAclIfMaxEntryNum_Object = MibTableColumn
myAclIfMaxEntryNum = _MyAclIfMaxEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 3, 1, 2),
    _MyAclIfMaxEntryNum_Type()
)
myAclIfMaxEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myAclIfMaxEntryNum.setStatus("current")
_MyAclIfCurruntEntryNum_Type = Integer32
_MyAclIfCurruntEntryNum_Object = MibTableColumn
myAclIfCurruntEntryNum = _MyAclIfCurruntEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 3, 1, 3),
    _MyAclIfCurruntEntryNum_Type()
)
myAclIfCurruntEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myAclIfCurruntEntryNum.setStatus("current")


class _MyIfInAclName_Type(DisplayString):
    """Custom type myIfInAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MyIfInAclName_Type.__name__ = "DisplayString"
_MyIfInAclName_Object = MibTableColumn
myIfInAclName = _MyIfInAclName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 3, 1, 4),
    _MyIfInAclName_Type()
)
myIfInAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIfInAclName.setStatus("current")


class _MyIfOutAclName_Type(DisplayString):
    """Custom type myIfOutAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MyIfOutAclName_Type.__name__ = "DisplayString"
_MyIfOutAclName_Object = MibTableColumn
myIfOutAclName = _MyIfOutAclName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 1, 3, 1, 5),
    _MyIfOutAclName_Type()
)
myIfOutAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIfOutAclName.setStatus("current")
_MyAclMIBConformance_ObjectIdentity = ObjectIdentity
myAclMIBConformance = _MyAclMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 2)
)
_MyAclMIBCompliances_ObjectIdentity = ObjectIdentity
myAclMIBCompliances = _MyAclMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 2, 1)
)
_MyAclMIBGroups_ObjectIdentity = ObjectIdentity
myAclMIBGroups = _MyAclMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 2, 2)
)

# Managed Objects groups

myAclMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 2, 2, 1)
)
myAclMIBGroup.setObjects(
      *(("MY-ACL-MIB", "myAclName"),
        ("MY-ACL-MIB", "myAclMode"),
        ("MY-ACL-MIB", "myAclEntryStatus"),
        ("MY-ACL-MIB", "myAceAclName"),
        ("MY-ACL-MIB", "myAceIndex"),
        ("MY-ACL-MIB", "myAceIfAnyVID"),
        ("MY-ACL-MIB", "myAceVID"),
        ("MY-ACL-MIB", "myAceIfAnySourceIp"),
        ("MY-ACL-MIB", "myAceSourceIp"),
        ("MY-ACL-MIB", "myAceIfAnySourceWildCard"),
        ("MY-ACL-MIB", "myAceSourceWildCard"),
        ("MY-ACL-MIB", "myAceIfAnySourceMacAddr"),
        ("MY-ACL-MIB", "myAceSourceMacAddr"),
        ("MY-ACL-MIB", "myAceIfAnyDestIp"),
        ("MY-ACL-MIB", "myAceDestIp"),
        ("MY-ACL-MIB", "myAceIfAnyDestWildCard"),
        ("MY-ACL-MIB", "myAceDestIpWildCard"),
        ("MY-ACL-MIB", "myAceIfAnyDestMacAddr"),
        ("MY-ACL-MIB", "myAceDestMacAddr"),
        ("MY-ACL-MIB", "myAceIfAnyEtherLikeType"),
        ("MY-ACL-MIB", "myAceEtherLikeType"),
        ("MY-ACL-MIB", "myAceIfAnyIpProtocolField"),
        ("MY-ACL-MIB", "myAceIpProtocolField"),
        ("MY-ACL-MIB", "myAceIfAnySourceProtocolPort"),
        ("MY-ACL-MIB", "myAceSourceProtocolPort"),
        ("MY-ACL-MIB", "myAceIfAnyDestProtocolPort"),
        ("MY-ACL-MIB", "myAceDestProtocolPort"),
        ("MY-ACL-MIB", "myAceProtocolType"),
        ("MY-ACL-MIB", "myAceProtocolType"),
        ("MY-ACL-MIB", "myAceFlowAction"),
        ("MY-ACL-MIB", "myAceEntryStauts"),
        ("MY-ACL-MIB", "myAceTimeRangeName"),
        ("MY-ACL-MIB", "myAclIfIndex"),
        ("MY-ACL-MIB", "myAclIfMaxEntryNum"),
        ("MY-ACL-MIB", "myAclIfCurruntEntryNum"),
        ("MY-ACL-MIB", "myIfInAclName"),
        ("MY-ACL-MIB", "myIfOutAclName"))
)
if mibBuilder.loadTexts:
    myAclMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

myAclMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 17, 2, 1, 1)
)
myAclMIBCompliance.setObjects(
    ("MY-ACL-MIB", "myAclMIBGroup")
)
if mibBuilder.loadTexts:
    myAclMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MY-ACL-MIB",
    **{"myAclMIB": myAclMIB,
       "myAclMIBObjects": myAclMIBObjects,
       "myAclTable": myAclTable,
       "myAclEntry": myAclEntry,
       "myAclName": myAclName,
       "myAclMode": myAclMode,
       "myAclEntryStatus": myAclEntryStatus,
       "myAceTable": myAceTable,
       "myAceEntry": myAceEntry,
       "myAceAclName": myAceAclName,
       "myAceIndex": myAceIndex,
       "myAceIfAnyVID": myAceIfAnyVID,
       "myAceVID": myAceVID,
       "myAceIfAnySourceIp": myAceIfAnySourceIp,
       "myAceSourceIp": myAceSourceIp,
       "myAceIfAnySourceWildCard": myAceIfAnySourceWildCard,
       "myAceSourceWildCard": myAceSourceWildCard,
       "myAceIfAnySourceMacAddr": myAceIfAnySourceMacAddr,
       "myAceSourceMacAddr": myAceSourceMacAddr,
       "myAceIfAnyDestIp": myAceIfAnyDestIp,
       "myAceDestIp": myAceDestIp,
       "myAceIfAnyDestWildCard": myAceIfAnyDestWildCard,
       "myAceDestIpWildCard": myAceDestIpWildCard,
       "myAceIfAnyDestMacAddr": myAceIfAnyDestMacAddr,
       "myAceDestMacAddr": myAceDestMacAddr,
       "myAceIfAnyEtherLikeType": myAceIfAnyEtherLikeType,
       "myAceEtherLikeType": myAceEtherLikeType,
       "myAceIfAnyIpProtocolField": myAceIfAnyIpProtocolField,
       "myAceIpProtocolField": myAceIpProtocolField,
       "myAceIfAnySourceProtocolPort": myAceIfAnySourceProtocolPort,
       "myAceSourceProtocolPort": myAceSourceProtocolPort,
       "myAceIfAnyDestProtocolPort": myAceIfAnyDestProtocolPort,
       "myAceDestProtocolPort": myAceDestProtocolPort,
       "myAceIfAnyProtocolType": myAceIfAnyProtocolType,
       "myAceProtocolType": myAceProtocolType,
       "myAceFlowAction": myAceFlowAction,
       "myAceEntryStauts": myAceEntryStauts,
       "myAceTimeRangeName": myAceTimeRangeName,
       "myAclIfTable": myAclIfTable,
       "myAclIfEntry": myAclIfEntry,
       "myAclIfIndex": myAclIfIndex,
       "myAclIfMaxEntryNum": myAclIfMaxEntryNum,
       "myAclIfCurruntEntryNum": myAclIfCurruntEntryNum,
       "myIfInAclName": myIfInAclName,
       "myIfOutAclName": myIfOutAclName,
       "myAclMIBConformance": myAclMIBConformance,
       "myAclMIBCompliances": myAclMIBCompliances,
       "myAclMIBCompliance": myAclMIBCompliance,
       "myAclMIBGroups": myAclMIBGroups,
       "myAclMIBGroup": myAclMIBGroup}
)
