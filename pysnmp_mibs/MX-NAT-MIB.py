# SNMP MIB module (MX-NAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-NAT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:19 2025
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

(mediatrixServices,) = mibBuilder.importSymbols(
    "MX-SMI2",
    "mediatrixServices")

(MxActivationState,
 MxAdvancedIpPort,
 MxDigitMap,
 MxEnableState,
 MxIpAddress,
 MxIpHostName,
 MxIpPort,
 MxIpSubnetMask) = mibBuilder.importSymbols(
    "MX-TC",
    "MxActivationState",
    "MxAdvancedIpPort",
    "MxDigitMap",
    "MxEnableState",
    "MxIpAddress",
    "MxIpHostName",
    "MxIpPort",
    "MxIpSubnetMask")

(MxFloat32,
 MxIpAddr,
 MxIpAddrMask,
 MxIpAddrPort,
 MxIpHostNamePort,
 MxUInt64,
 MxUri,
 MxUrl) = mibBuilder.importSymbols(
    "MX-TC2",
    "MxFloat32",
    "MxIpAddr",
    "MxIpAddrMask",
    "MxIpAddrPort",
    "MxIpHostNamePort",
    "MxUInt64",
    "MxUri",
    "MxUrl")

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

natMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NatMIBObjects_ObjectIdentity = ObjectIdentity
natMIBObjects = _NatMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1)
)


class _ConfigModifiedStatus_Type(Integer32):
    """Custom type configModifiedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("yes", 100),
          ("no", 200))
    )


_ConfigModifiedStatus_Type.__name__ = "Integer32"
_ConfigModifiedStatus_Object = MibScalar
configModifiedStatus = _ConfigModifiedStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 100),
    _ConfigModifiedStatus_Type()
)
configModifiedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configModifiedStatus.setStatus("current")
_SNatRulesStatusTable_Object = MibTable
sNatRulesStatusTable = _SNatRulesStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 200)
)
if mibBuilder.loadTexts:
    sNatRulesStatusTable.setStatus("current")
_SNatRulesStatusEntry_Object = MibTableRow
sNatRulesStatusEntry = _SNatRulesStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 200, 1)
)
sNatRulesStatusEntry.setIndexNames(
    (0, "MX-NAT-MIB", "sNatRulesStatusPriority"),
)
if mibBuilder.loadTexts:
    sNatRulesStatusEntry.setStatus("current")
_SNatRulesStatusPriority_Type = Unsigned32
_SNatRulesStatusPriority_Object = MibTableColumn
sNatRulesStatusPriority = _SNatRulesStatusPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 200, 1, 100),
    _SNatRulesStatusPriority_Type()
)
sNatRulesStatusPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNatRulesStatusPriority.setStatus("current")
_SNatRulesStatusSourceAddress_Type = OctetString
_SNatRulesStatusSourceAddress_Object = MibTableColumn
sNatRulesStatusSourceAddress = _SNatRulesStatusSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 200, 1, 200),
    _SNatRulesStatusSourceAddress_Type()
)
sNatRulesStatusSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNatRulesStatusSourceAddress.setStatus("current")
_SNatRulesStatusSourcePort_Type = OctetString
_SNatRulesStatusSourcePort_Object = MibTableColumn
sNatRulesStatusSourcePort = _SNatRulesStatusSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 200, 1, 300),
    _SNatRulesStatusSourcePort_Type()
)
sNatRulesStatusSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNatRulesStatusSourcePort.setStatus("current")
_SNatRulesStatusDestinationAddress_Type = OctetString
_SNatRulesStatusDestinationAddress_Object = MibTableColumn
sNatRulesStatusDestinationAddress = _SNatRulesStatusDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 200, 1, 400),
    _SNatRulesStatusDestinationAddress_Type()
)
sNatRulesStatusDestinationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNatRulesStatusDestinationAddress.setStatus("current")
_SNatRulesStatusDestinationPort_Type = OctetString
_SNatRulesStatusDestinationPort_Object = MibTableColumn
sNatRulesStatusDestinationPort = _SNatRulesStatusDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 200, 1, 500),
    _SNatRulesStatusDestinationPort_Type()
)
sNatRulesStatusDestinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNatRulesStatusDestinationPort.setStatus("current")


class _SNatRulesStatusProtocol_Type(Integer32):
    """Custom type sNatRulesStatusProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400)
        )
    )
    namedValues = NamedValues(
        *(("all", 100),
          ("tcp", 200),
          ("udp", 300),
          ("icmp", 400))
    )


_SNatRulesStatusProtocol_Type.__name__ = "Integer32"
_SNatRulesStatusProtocol_Object = MibTableColumn
sNatRulesStatusProtocol = _SNatRulesStatusProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 200, 1, 600),
    _SNatRulesStatusProtocol_Type()
)
sNatRulesStatusProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNatRulesStatusProtocol.setStatus("current")
_SNatRulesStatusNewAddress_Type = OctetString
_SNatRulesStatusNewAddress_Object = MibTableColumn
sNatRulesStatusNewAddress = _SNatRulesStatusNewAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 200, 1, 700),
    _SNatRulesStatusNewAddress_Type()
)
sNatRulesStatusNewAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNatRulesStatusNewAddress.setStatus("current")
_SNatRulesTable_Object = MibTable
sNatRulesTable = _SNatRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 700)
)
if mibBuilder.loadTexts:
    sNatRulesTable.setStatus("current")
_SNatRulesEntry_Object = MibTableRow
sNatRulesEntry = _SNatRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 700, 1)
)
sNatRulesEntry.setIndexNames(
    (0, "MX-NAT-MIB", "sNatRulesPriority"),
)
if mibBuilder.loadTexts:
    sNatRulesEntry.setStatus("current")
_SNatRulesPriority_Type = Unsigned32
_SNatRulesPriority_Object = MibTableColumn
sNatRulesPriority = _SNatRulesPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 700, 1, 100),
    _SNatRulesPriority_Type()
)
sNatRulesPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNatRulesPriority.setStatus("current")


class _SNatRulesActivation_Type(MxEnableState):
    """Custom type sNatRulesActivation based on MxEnableState"""
    defaultValue = 0


_SNatRulesActivation_Type.__name__ = "MxEnableState"
_SNatRulesActivation_Object = MibTableColumn
sNatRulesActivation = _SNatRulesActivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 700, 1, 200),
    _SNatRulesActivation_Type()
)
sNatRulesActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNatRulesActivation.setStatus("current")


class _SNatRulesSourceAddress_Type(OctetString):
    """Custom type sNatRulesSourceAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 51),
    )


_SNatRulesSourceAddress_Type.__name__ = "OctetString"
_SNatRulesSourceAddress_Object = MibTableColumn
sNatRulesSourceAddress = _SNatRulesSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 700, 1, 300),
    _SNatRulesSourceAddress_Type()
)
sNatRulesSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNatRulesSourceAddress.setStatus("current")


class _SNatRulesSourcePort_Type(OctetString):
    """Custom type sNatRulesSourcePort based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_SNatRulesSourcePort_Type.__name__ = "OctetString"
_SNatRulesSourcePort_Object = MibTableColumn
sNatRulesSourcePort = _SNatRulesSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 700, 1, 400),
    _SNatRulesSourcePort_Type()
)
sNatRulesSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNatRulesSourcePort.setStatus("current")


class _SNatRulesDestinationAddress_Type(OctetString):
    """Custom type sNatRulesDestinationAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 51),
    )


_SNatRulesDestinationAddress_Type.__name__ = "OctetString"
_SNatRulesDestinationAddress_Object = MibTableColumn
sNatRulesDestinationAddress = _SNatRulesDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 700, 1, 500),
    _SNatRulesDestinationAddress_Type()
)
sNatRulesDestinationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNatRulesDestinationAddress.setStatus("current")


class _SNatRulesDestinationPort_Type(OctetString):
    """Custom type sNatRulesDestinationPort based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_SNatRulesDestinationPort_Type.__name__ = "OctetString"
_SNatRulesDestinationPort_Object = MibTableColumn
sNatRulesDestinationPort = _SNatRulesDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 700, 1, 600),
    _SNatRulesDestinationPort_Type()
)
sNatRulesDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNatRulesDestinationPort.setStatus("current")


class _SNatRulesProtocol_Type(Integer32):
    """Custom type sNatRulesProtocol based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400)
        )
    )
    namedValues = NamedValues(
        *(("all", 100),
          ("tcp", 200),
          ("udp", 300),
          ("icmp", 400))
    )


_SNatRulesProtocol_Type.__name__ = "Integer32"
_SNatRulesProtocol_Object = MibTableColumn
sNatRulesProtocol = _SNatRulesProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 700, 1, 700),
    _SNatRulesProtocol_Type()
)
sNatRulesProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNatRulesProtocol.setStatus("current")


class _SNatRulesNewAddress_Type(OctetString):
    """Custom type sNatRulesNewAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 51),
    )


_SNatRulesNewAddress_Type.__name__ = "OctetString"
_SNatRulesNewAddress_Object = MibTableColumn
sNatRulesNewAddress = _SNatRulesNewAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 700, 1, 800),
    _SNatRulesNewAddress_Type()
)
sNatRulesNewAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNatRulesNewAddress.setStatus("current")


class _SNatRulesUp_Type(Integer32):
    """Custom type sNatRulesUp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("up", 10))
    )


_SNatRulesUp_Type.__name__ = "Integer32"
_SNatRulesUp_Object = MibTableColumn
sNatRulesUp = _SNatRulesUp_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 700, 1, 900),
    _SNatRulesUp_Type()
)
sNatRulesUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNatRulesUp.setStatus("current")


class _SNatRulesDown_Type(Integer32):
    """Custom type sNatRulesDown based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("down", 10))
    )


_SNatRulesDown_Type.__name__ = "Integer32"
_SNatRulesDown_Object = MibTableColumn
sNatRulesDown = _SNatRulesDown_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 700, 1, 1000),
    _SNatRulesDown_Type()
)
sNatRulesDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNatRulesDown.setStatus("current")


class _SNatRulesInsert_Type(Integer32):
    """Custom type sNatRulesInsert based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("insert", 10))
    )


_SNatRulesInsert_Type.__name__ = "Integer32"
_SNatRulesInsert_Object = MibTableColumn
sNatRulesInsert = _SNatRulesInsert_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 700, 1, 1100),
    _SNatRulesInsert_Type()
)
sNatRulesInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNatRulesInsert.setStatus("current")


class _SNatRulesDelete_Type(Integer32):
    """Custom type sNatRulesDelete based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("delete", 10))
    )


_SNatRulesDelete_Type.__name__ = "Integer32"
_SNatRulesDelete_Object = MibTableColumn
sNatRulesDelete = _SNatRulesDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 700, 1, 1200),
    _SNatRulesDelete_Type()
)
sNatRulesDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNatRulesDelete.setStatus("current")
_DNatRulesStatusTable_Object = MibTable
dNatRulesStatusTable = _DNatRulesStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 800)
)
if mibBuilder.loadTexts:
    dNatRulesStatusTable.setStatus("current")
_DNatRulesStatusEntry_Object = MibTableRow
dNatRulesStatusEntry = _DNatRulesStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 800, 1)
)
dNatRulesStatusEntry.setIndexNames(
    (0, "MX-NAT-MIB", "dNatRulesStatusPriority"),
)
if mibBuilder.loadTexts:
    dNatRulesStatusEntry.setStatus("current")
_DNatRulesStatusPriority_Type = Unsigned32
_DNatRulesStatusPriority_Object = MibTableColumn
dNatRulesStatusPriority = _DNatRulesStatusPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 800, 1, 100),
    _DNatRulesStatusPriority_Type()
)
dNatRulesStatusPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dNatRulesStatusPriority.setStatus("current")
_DNatRulesStatusSourceAddress_Type = OctetString
_DNatRulesStatusSourceAddress_Object = MibTableColumn
dNatRulesStatusSourceAddress = _DNatRulesStatusSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 800, 1, 200),
    _DNatRulesStatusSourceAddress_Type()
)
dNatRulesStatusSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dNatRulesStatusSourceAddress.setStatus("current")
_DNatRulesStatusSourcePort_Type = OctetString
_DNatRulesStatusSourcePort_Object = MibTableColumn
dNatRulesStatusSourcePort = _DNatRulesStatusSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 800, 1, 300),
    _DNatRulesStatusSourcePort_Type()
)
dNatRulesStatusSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dNatRulesStatusSourcePort.setStatus("current")
_DNatRulesStatusDestinationAddress_Type = OctetString
_DNatRulesStatusDestinationAddress_Object = MibTableColumn
dNatRulesStatusDestinationAddress = _DNatRulesStatusDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 800, 1, 400),
    _DNatRulesStatusDestinationAddress_Type()
)
dNatRulesStatusDestinationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dNatRulesStatusDestinationAddress.setStatus("current")
_DNatRulesStatusDestinationPort_Type = OctetString
_DNatRulesStatusDestinationPort_Object = MibTableColumn
dNatRulesStatusDestinationPort = _DNatRulesStatusDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 800, 1, 500),
    _DNatRulesStatusDestinationPort_Type()
)
dNatRulesStatusDestinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dNatRulesStatusDestinationPort.setStatus("current")


class _DNatRulesStatusProtocol_Type(Integer32):
    """Custom type dNatRulesStatusProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400)
        )
    )
    namedValues = NamedValues(
        *(("all", 100),
          ("tcp", 200),
          ("udp", 300),
          ("icmp", 400))
    )


_DNatRulesStatusProtocol_Type.__name__ = "Integer32"
_DNatRulesStatusProtocol_Object = MibTableColumn
dNatRulesStatusProtocol = _DNatRulesStatusProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 800, 1, 600),
    _DNatRulesStatusProtocol_Type()
)
dNatRulesStatusProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dNatRulesStatusProtocol.setStatus("current")
_DNatRulesStatusNewAddress_Type = OctetString
_DNatRulesStatusNewAddress_Object = MibTableColumn
dNatRulesStatusNewAddress = _DNatRulesStatusNewAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 800, 1, 700),
    _DNatRulesStatusNewAddress_Type()
)
dNatRulesStatusNewAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dNatRulesStatusNewAddress.setStatus("current")
_DNatRulesTable_Object = MibTable
dNatRulesTable = _DNatRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 900)
)
if mibBuilder.loadTexts:
    dNatRulesTable.setStatus("current")
_DNatRulesEntry_Object = MibTableRow
dNatRulesEntry = _DNatRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 900, 1)
)
dNatRulesEntry.setIndexNames(
    (0, "MX-NAT-MIB", "dNatRulesPriority"),
)
if mibBuilder.loadTexts:
    dNatRulesEntry.setStatus("current")
_DNatRulesPriority_Type = Unsigned32
_DNatRulesPriority_Object = MibTableColumn
dNatRulesPriority = _DNatRulesPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 900, 1, 100),
    _DNatRulesPriority_Type()
)
dNatRulesPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dNatRulesPriority.setStatus("current")


class _DNatRulesActivation_Type(MxEnableState):
    """Custom type dNatRulesActivation based on MxEnableState"""
    defaultValue = 0


_DNatRulesActivation_Type.__name__ = "MxEnableState"
_DNatRulesActivation_Object = MibTableColumn
dNatRulesActivation = _DNatRulesActivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 900, 1, 200),
    _DNatRulesActivation_Type()
)
dNatRulesActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNatRulesActivation.setStatus("current")


class _DNatRulesSourceAddress_Type(OctetString):
    """Custom type dNatRulesSourceAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 51),
    )


_DNatRulesSourceAddress_Type.__name__ = "OctetString"
_DNatRulesSourceAddress_Object = MibTableColumn
dNatRulesSourceAddress = _DNatRulesSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 900, 1, 300),
    _DNatRulesSourceAddress_Type()
)
dNatRulesSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNatRulesSourceAddress.setStatus("current")


class _DNatRulesSourcePort_Type(OctetString):
    """Custom type dNatRulesSourcePort based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_DNatRulesSourcePort_Type.__name__ = "OctetString"
_DNatRulesSourcePort_Object = MibTableColumn
dNatRulesSourcePort = _DNatRulesSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 900, 1, 400),
    _DNatRulesSourcePort_Type()
)
dNatRulesSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNatRulesSourcePort.setStatus("current")


class _DNatRulesDestinationAddress_Type(OctetString):
    """Custom type dNatRulesDestinationAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 51),
    )


_DNatRulesDestinationAddress_Type.__name__ = "OctetString"
_DNatRulesDestinationAddress_Object = MibTableColumn
dNatRulesDestinationAddress = _DNatRulesDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 900, 1, 500),
    _DNatRulesDestinationAddress_Type()
)
dNatRulesDestinationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNatRulesDestinationAddress.setStatus("current")


class _DNatRulesDestinationPort_Type(OctetString):
    """Custom type dNatRulesDestinationPort based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_DNatRulesDestinationPort_Type.__name__ = "OctetString"
_DNatRulesDestinationPort_Object = MibTableColumn
dNatRulesDestinationPort = _DNatRulesDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 900, 1, 600),
    _DNatRulesDestinationPort_Type()
)
dNatRulesDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNatRulesDestinationPort.setStatus("current")


class _DNatRulesProtocol_Type(Integer32):
    """Custom type dNatRulesProtocol based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400)
        )
    )
    namedValues = NamedValues(
        *(("all", 100),
          ("tcp", 200),
          ("udp", 300),
          ("icmp", 400))
    )


_DNatRulesProtocol_Type.__name__ = "Integer32"
_DNatRulesProtocol_Object = MibTableColumn
dNatRulesProtocol = _DNatRulesProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 900, 1, 700),
    _DNatRulesProtocol_Type()
)
dNatRulesProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNatRulesProtocol.setStatus("current")


class _DNatRulesNewAddress_Type(OctetString):
    """Custom type dNatRulesNewAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 51),
    )


_DNatRulesNewAddress_Type.__name__ = "OctetString"
_DNatRulesNewAddress_Object = MibTableColumn
dNatRulesNewAddress = _DNatRulesNewAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 900, 1, 800),
    _DNatRulesNewAddress_Type()
)
dNatRulesNewAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNatRulesNewAddress.setStatus("current")


class _DNatRulesUp_Type(Integer32):
    """Custom type dNatRulesUp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("up", 10))
    )


_DNatRulesUp_Type.__name__ = "Integer32"
_DNatRulesUp_Object = MibTableColumn
dNatRulesUp = _DNatRulesUp_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 900, 1, 900),
    _DNatRulesUp_Type()
)
dNatRulesUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNatRulesUp.setStatus("current")


class _DNatRulesDown_Type(Integer32):
    """Custom type dNatRulesDown based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("down", 10))
    )


_DNatRulesDown_Type.__name__ = "Integer32"
_DNatRulesDown_Object = MibTableColumn
dNatRulesDown = _DNatRulesDown_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 900, 1, 1000),
    _DNatRulesDown_Type()
)
dNatRulesDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNatRulesDown.setStatus("current")


class _DNatRulesInsert_Type(Integer32):
    """Custom type dNatRulesInsert based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("insert", 10))
    )


_DNatRulesInsert_Type.__name__ = "Integer32"
_DNatRulesInsert_Object = MibTableColumn
dNatRulesInsert = _DNatRulesInsert_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 900, 1, 1100),
    _DNatRulesInsert_Type()
)
dNatRulesInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNatRulesInsert.setStatus("current")


class _DNatRulesDelete_Type(Integer32):
    """Custom type dNatRulesDelete based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("delete", 10))
    )


_DNatRulesDelete_Type.__name__ = "Integer32"
_DNatRulesDelete_Object = MibTableColumn
dNatRulesDelete = _DNatRulesDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 900, 1, 1200),
    _DNatRulesDelete_Type()
)
dNatRulesDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNatRulesDelete.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 60010)
)


class _MinSeverity_Type(Integer32):
    """Custom type minSeverity based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100,
              200,
              300,
              400,
              500)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("debug", 100),
          ("info", 200),
          ("warning", 300),
          ("error", 400),
          ("critical", 500))
    )


_MinSeverity_Type.__name__ = "Integer32"
_MinSeverity_Object = MibScalar
minSeverity = _MinSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 60020)
)


class _NeedRestartInfo_Type(Integer32):
    """Custom type needRestartInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 100))
    )


_NeedRestartInfo_Type.__name__ = "Integer32"
_NeedRestartInfo_Object = MibScalar
needRestartInfo = _NeedRestartInfo_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2275, 1, 60020, 100),
    _NeedRestartInfo_Type()
)
needRestartInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    needRestartInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-NAT-MIB",
    **{"natMIB": natMIB,
       "natMIBObjects": natMIBObjects,
       "configModifiedStatus": configModifiedStatus,
       "sNatRulesStatusTable": sNatRulesStatusTable,
       "sNatRulesStatusEntry": sNatRulesStatusEntry,
       "sNatRulesStatusPriority": sNatRulesStatusPriority,
       "sNatRulesStatusSourceAddress": sNatRulesStatusSourceAddress,
       "sNatRulesStatusSourcePort": sNatRulesStatusSourcePort,
       "sNatRulesStatusDestinationAddress": sNatRulesStatusDestinationAddress,
       "sNatRulesStatusDestinationPort": sNatRulesStatusDestinationPort,
       "sNatRulesStatusProtocol": sNatRulesStatusProtocol,
       "sNatRulesStatusNewAddress": sNatRulesStatusNewAddress,
       "sNatRulesTable": sNatRulesTable,
       "sNatRulesEntry": sNatRulesEntry,
       "sNatRulesPriority": sNatRulesPriority,
       "sNatRulesActivation": sNatRulesActivation,
       "sNatRulesSourceAddress": sNatRulesSourceAddress,
       "sNatRulesSourcePort": sNatRulesSourcePort,
       "sNatRulesDestinationAddress": sNatRulesDestinationAddress,
       "sNatRulesDestinationPort": sNatRulesDestinationPort,
       "sNatRulesProtocol": sNatRulesProtocol,
       "sNatRulesNewAddress": sNatRulesNewAddress,
       "sNatRulesUp": sNatRulesUp,
       "sNatRulesDown": sNatRulesDown,
       "sNatRulesInsert": sNatRulesInsert,
       "sNatRulesDelete": sNatRulesDelete,
       "dNatRulesStatusTable": dNatRulesStatusTable,
       "dNatRulesStatusEntry": dNatRulesStatusEntry,
       "dNatRulesStatusPriority": dNatRulesStatusPriority,
       "dNatRulesStatusSourceAddress": dNatRulesStatusSourceAddress,
       "dNatRulesStatusSourcePort": dNatRulesStatusSourcePort,
       "dNatRulesStatusDestinationAddress": dNatRulesStatusDestinationAddress,
       "dNatRulesStatusDestinationPort": dNatRulesStatusDestinationPort,
       "dNatRulesStatusProtocol": dNatRulesStatusProtocol,
       "dNatRulesStatusNewAddress": dNatRulesStatusNewAddress,
       "dNatRulesTable": dNatRulesTable,
       "dNatRulesEntry": dNatRulesEntry,
       "dNatRulesPriority": dNatRulesPriority,
       "dNatRulesActivation": dNatRulesActivation,
       "dNatRulesSourceAddress": dNatRulesSourceAddress,
       "dNatRulesSourcePort": dNatRulesSourcePort,
       "dNatRulesDestinationAddress": dNatRulesDestinationAddress,
       "dNatRulesDestinationPort": dNatRulesDestinationPort,
       "dNatRulesProtocol": dNatRulesProtocol,
       "dNatRulesNewAddress": dNatRulesNewAddress,
       "dNatRulesUp": dNatRulesUp,
       "dNatRulesDown": dNatRulesDown,
       "dNatRulesInsert": dNatRulesInsert,
       "dNatRulesDelete": dNatRulesDelete,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
