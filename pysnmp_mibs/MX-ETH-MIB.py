# SNMP MIB module (MX-ETH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-ETH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:53 2025
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

ethMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EthMIBObjects_ObjectIdentity = ObjectIdentity
ethMIBObjects = _EthMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1)
)
_LinkStatusTable_Object = MibTable
linkStatusTable = _LinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 25)
)
if mibBuilder.loadTexts:
    linkStatusTable.setStatus("current")
_LinkStatusEntry_Object = MibTableRow
linkStatusEntry = _LinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 25, 1)
)
linkStatusEntry.setIndexNames(
    (0, "MX-ETH-MIB", "linkStatusLinkName"),
)
if mibBuilder.loadTexts:
    linkStatusEntry.setStatus("current")
_LinkStatusLinkName_Type = OctetString
_LinkStatusLinkName_Object = MibTableColumn
linkStatusLinkName = _LinkStatusLinkName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 25, 1, 100),
    _LinkStatusLinkName_Type()
)
linkStatusLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusLinkName.setStatus("current")
_LinkStatusLinkType_Type = OctetString
_LinkStatusLinkType_Object = MibTableColumn
linkStatusLinkType = _LinkStatusLinkType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 25, 1, 200),
    _LinkStatusLinkType_Type()
)
linkStatusLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusLinkType.setStatus("current")


class _LinkStatusLinkState_Type(Integer32):
    """Custom type linkStatusLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 100),
          ("up", 200))
    )


_LinkStatusLinkState_Type.__name__ = "Integer32"
_LinkStatusLinkState_Object = MibTableColumn
linkStatusLinkState = _LinkStatusLinkState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 25, 1, 300),
    _LinkStatusLinkState_Type()
)
linkStatusLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusLinkState.setStatus("current")
_LinksTable_Object = MibTable
linksTable = _LinksTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 50)
)
if mibBuilder.loadTexts:
    linksTable.setStatus("current")
_LinksEntry_Object = MibTableRow
linksEntry = _LinksEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 50, 1)
)
linksEntry.setIndexNames(
    (0, "MX-ETH-MIB", "linksName"),
)
if mibBuilder.loadTexts:
    linksEntry.setStatus("current")
_LinksName_Type = OctetString
_LinksName_Object = MibTableColumn
linksName = _LinksName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 50, 1, 100),
    _LinksName_Type()
)
linksName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linksName.setStatus("current")


class _LinksMtu_Type(Unsigned32):
    """Custom type linksMtu based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(576, 1500),
    )


_LinksMtu_Type.__name__ = "Unsigned32"
_LinksMtu_Object = MibTableColumn
linksMtu = _LinksMtu_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 50, 1, 200),
    _LinksMtu_Type()
)
linksMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linksMtu.setStatus("current")


class _LinksIeee8021XAuthentication_Type(Integer32):
    """Custom type linksIeee8021XAuthentication based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("disable", 100),
          ("enable", 200))
    )


_LinksIeee8021XAuthentication_Type.__name__ = "Integer32"
_LinksIeee8021XAuthentication_Object = MibTableColumn
linksIeee8021XAuthentication = _LinksIeee8021XAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 50, 1, 300),
    _LinksIeee8021XAuthentication_Type()
)
linksIeee8021XAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linksIeee8021XAuthentication.setStatus("current")


class _LinksVirtualSwitch_Type(MxEnableState):
    """Custom type linksVirtualSwitch based on MxEnableState"""
    defaultValue = 0


_LinksVirtualSwitch_Type.__name__ = "MxEnableState"
_LinksVirtualSwitch_Object = MibTableColumn
linksVirtualSwitch = _LinksVirtualSwitch_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 50, 1, 400),
    _LinksVirtualSwitch_Type()
)
linksVirtualSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linksVirtualSwitch.setStatus("current")
_PortsStatusTable_Object = MibTable
portsStatusTable = _PortsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 100)
)
if mibBuilder.loadTexts:
    portsStatusTable.setStatus("current")
_PortsStatusEntry_Object = MibTableRow
portsStatusEntry = _PortsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 100, 1)
)
portsStatusEntry.setIndexNames(
    (0, "MX-ETH-MIB", "portsStatusName"),
)
if mibBuilder.loadTexts:
    portsStatusEntry.setStatus("current")
_PortsStatusName_Type = OctetString
_PortsStatusName_Object = MibTableColumn
portsStatusName = _PortsStatusName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 100, 1, 100),
    _PortsStatusName_Type()
)
portsStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsStatusName.setStatus("current")
_PortsStatusLinkName_Type = OctetString
_PortsStatusLinkName_Object = MibTableColumn
portsStatusLinkName = _PortsStatusLinkName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 100, 1, 200),
    _PortsStatusLinkName_Type()
)
portsStatusLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsStatusLinkName.setStatus("current")


class _PortsStatusConnection_Type(Integer32):
    """Custom type portsStatusConnection based on Integer32"""
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
        *(("disconnected", 0),
          ("half10", 100),
          ("full10", 200),
          ("half100", 300),
          ("full100", 400),
          ("full1000", 500))
    )


_PortsStatusConnection_Type.__name__ = "Integer32"
_PortsStatusConnection_Object = MibTableColumn
portsStatusConnection = _PortsStatusConnection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 100, 1, 300),
    _PortsStatusConnection_Type()
)
portsStatusConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsStatusConnection.setStatus("current")
_PortsTable_Object = MibTable
portsTable = _PortsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 200)
)
if mibBuilder.loadTexts:
    portsTable.setStatus("current")
_PortsEntry_Object = MibTableRow
portsEntry = _PortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 200, 1)
)
portsEntry.setIndexNames(
    (0, "MX-ETH-MIB", "portsName"),
)
if mibBuilder.loadTexts:
    portsEntry.setStatus("current")
_PortsName_Type = OctetString
_PortsName_Object = MibTableColumn
portsName = _PortsName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 200, 1, 100),
    _PortsName_Type()
)
portsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsName.setStatus("current")


class _PortsSpeed_Type(Integer32):
    """Custom type portsSpeed based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              600)
        )
    )
    namedValues = NamedValues(
        *(("auto", 100),
          ("half10", 200),
          ("full10", 300),
          ("half100", 400),
          ("full100", 500),
          ("full1000", 600))
    )


_PortsSpeed_Type.__name__ = "Integer32"
_PortsSpeed_Object = MibTableColumn
portsSpeed = _PortsSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 200, 1, 200),
    _PortsSpeed_Type()
)
portsSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsSpeed.setStatus("current")
_VlanTable_Object = MibTable
vlanTable = _VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 300)
)
if mibBuilder.loadTexts:
    vlanTable.setStatus("current")
_VlanEntry_Object = MibTableRow
vlanEntry = _VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 300, 1)
)
vlanEntry.setIndexNames(
    (0, "MX-ETH-MIB", "vlanIdx"),
)
if mibBuilder.loadTexts:
    vlanEntry.setStatus("current")
_VlanIdx_Type = Unsigned32
_VlanIdx_Object = MibTableColumn
vlanIdx = _VlanIdx_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 300, 1, 50),
    _VlanIdx_Type()
)
vlanIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanIdx.setStatus("current")


class _VlanLinkName_Type(OctetString):
    """Custom type vlanLinkName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_VlanLinkName_Type.__name__ = "OctetString"
_VlanLinkName_Object = MibTableColumn
vlanLinkName = _VlanLinkName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 300, 1, 100),
    _VlanLinkName_Type()
)
vlanLinkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanLinkName.setStatus("current")


class _VlanVlanId_Type(Unsigned32):
    """Custom type vlanVlanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_VlanVlanId_Type.__name__ = "Unsigned32"
_VlanVlanId_Object = MibTableColumn
vlanVlanId = _VlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 300, 1, 200),
    _VlanVlanId_Type()
)
vlanVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanVlanId.setStatus("current")


class _VlanDefaultUserPriority_Type(Unsigned32):
    """Custom type vlanDefaultUserPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VlanDefaultUserPriority_Type.__name__ = "Unsigned32"
_VlanDefaultUserPriority_Object = MibTableColumn
vlanDefaultUserPriority = _VlanDefaultUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 300, 1, 300),
    _VlanDefaultUserPriority_Type()
)
vlanDefaultUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanDefaultUserPriority.setStatus("current")


class _VlanConfigStatus_Type(Integer32):
    """Custom type vlanConfigStatus based on Integer32"""
    defaultValue = 200

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
        *(("validConfig", 100),
          ("invalidLinkName", 200),
          ("invalidVlanId", 300),
          ("duplicateLinkVlanId", 400))
    )


_VlanConfigStatus_Type.__name__ = "Integer32"
_VlanConfigStatus_Object = MibTableColumn
vlanConfigStatus = _VlanConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 300, 1, 350),
    _VlanConfigStatus_Type()
)
vlanConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanConfigStatus.setStatus("current")


class _VlanDelete_Type(Integer32):
    """Custom type vlanDelete based on Integer32"""
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


_VlanDelete_Type.__name__ = "Integer32"
_VlanDelete_Object = MibTableColumn
vlanDelete = _VlanDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 300, 1, 400),
    _VlanDelete_Type()
)
vlanDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanDelete.setStatus("current")
_EapGroup_ObjectIdentity = ObjectIdentity
eapGroup = _EapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 10000)
)
_EapTable_Object = MibTable
eapTable = _EapTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 10000, 100)
)
if mibBuilder.loadTexts:
    eapTable.setStatus("current")
_EapEntry_Object = MibTableRow
eapEntry = _EapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 10000, 100, 1)
)
eapEntry.setIndexNames(
    (0, "MX-ETH-MIB", "eapName"),
)
if mibBuilder.loadTexts:
    eapEntry.setStatus("current")
_EapName_Type = OctetString
_EapName_Object = MibTableColumn
eapName = _EapName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 10000, 100, 1, 100),
    _EapName_Type()
)
eapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eapName.setStatus("current")


class _EapUsername_Type(OctetString):
    """Custom type eapUsername based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EapUsername_Type.__name__ = "OctetString"
_EapUsername_Object = MibTableColumn
eapUsername = _EapUsername_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 10000, 100, 1, 200),
    _EapUsername_Type()
)
eapUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eapUsername.setStatus("current")


class _EapCertificateValidation_Type(Integer32):
    """Custom type eapCertificateValidation based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("noValidation", 100),
          ("trustedAndValid", 200))
    )


_EapCertificateValidation_Type.__name__ = "Integer32"
_EapCertificateValidation_Object = MibTableColumn
eapCertificateValidation = _EapCertificateValidation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 10000, 100, 1, 300),
    _EapCertificateValidation_Type()
)
eapCertificateValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eapCertificateValidation.setStatus("current")


class _Ieee8021XVersion_Type(Integer32):
    """Custom type ieee8021XVersion based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("ieee8021X2001", 100),
          ("ieee8021X2004", 200))
    )


_Ieee8021XVersion_Type.__name__ = "Integer32"
_Ieee8021XVersion_Object = MibScalar
ieee8021XVersion = _Ieee8021XVersion_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 10000, 200),
    _Ieee8021XVersion_Type()
)
ieee8021XVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021XVersion.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 60010)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 60020)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2400, 1, 60020, 100),
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
    "MX-ETH-MIB",
    **{"ethMIB": ethMIB,
       "ethMIBObjects": ethMIBObjects,
       "linkStatusTable": linkStatusTable,
       "linkStatusEntry": linkStatusEntry,
       "linkStatusLinkName": linkStatusLinkName,
       "linkStatusLinkType": linkStatusLinkType,
       "linkStatusLinkState": linkStatusLinkState,
       "linksTable": linksTable,
       "linksEntry": linksEntry,
       "linksName": linksName,
       "linksMtu": linksMtu,
       "linksIeee8021XAuthentication": linksIeee8021XAuthentication,
       "linksVirtualSwitch": linksVirtualSwitch,
       "portsStatusTable": portsStatusTable,
       "portsStatusEntry": portsStatusEntry,
       "portsStatusName": portsStatusName,
       "portsStatusLinkName": portsStatusLinkName,
       "portsStatusConnection": portsStatusConnection,
       "portsTable": portsTable,
       "portsEntry": portsEntry,
       "portsName": portsName,
       "portsSpeed": portsSpeed,
       "vlanTable": vlanTable,
       "vlanEntry": vlanEntry,
       "vlanIdx": vlanIdx,
       "vlanLinkName": vlanLinkName,
       "vlanVlanId": vlanVlanId,
       "vlanDefaultUserPriority": vlanDefaultUserPriority,
       "vlanConfigStatus": vlanConfigStatus,
       "vlanDelete": vlanDelete,
       "eapGroup": eapGroup,
       "eapTable": eapTable,
       "eapEntry": eapEntry,
       "eapName": eapName,
       "eapUsername": eapUsername,
       "eapCertificateValidation": eapCertificateValidation,
       "ieee8021XVersion": ieee8021XVersion,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
