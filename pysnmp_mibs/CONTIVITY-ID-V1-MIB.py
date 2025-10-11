# SNMP MIB module (CONTIVITY-ID-V1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/CONTIVITY-ID-V1-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:20:26 2025
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

(contivity,) = mibBuilder.importSymbols(
    "NEWOAK-MIB",
    "contivity")

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

id_ces = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 16)
)
if mibBuilder.loadTexts:
    id_ces.setRevisions(
        ("1901-05-10 23:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Id_Software_ces_ObjectIdentity = ObjectIdentity
id_Software_ces = _Id_Software_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 16, 1)
)
if mibBuilder.loadTexts:
    id_Software_ces.setStatus("current")
_Id_SW_Server_ces_ObjectIdentity = ObjectIdentity
id_SW_Server_ces = _Id_SW_Server_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 16, 1, 1)
)
if mibBuilder.loadTexts:
    id_SW_Server_ces.setStatus("current")
_Id_SW_Routing_ces_ObjectIdentity = ObjectIdentity
id_SW_Routing_ces = _Id_SW_Routing_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 16, 1, 1, 1)
)
if mibBuilder.loadTexts:
    id_SW_Routing_ces.setStatus("current")
_Id_SW_Routing_RoutingInformationProtocol_ces_ObjectIdentity = ObjectIdentity
id_SW_Routing_RoutingInformationProtocol_ces = _Id_SW_Routing_RoutingInformationProtocol_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 16, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    id_SW_Routing_RoutingInformationProtocol_ces.setStatus("current")
_Id_SW_Routing_AdvancedRouting_ces_ObjectIdentity = ObjectIdentity
id_SW_Routing_AdvancedRouting_ces = _Id_SW_Routing_AdvancedRouting_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 16, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    id_SW_Routing_AdvancedRouting_ces.setStatus("current")
_Id_SW_AdvancedRouting_OpenShortestPathFirst_ces_ObjectIdentity = ObjectIdentity
id_SW_AdvancedRouting_OpenShortestPathFirst_ces = _Id_SW_AdvancedRouting_OpenShortestPathFirst_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 16, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    id_SW_AdvancedRouting_OpenShortestPathFirst_ces.setStatus("current")
_Id_SW_AdvancedRouting_VirtualRouterRedundancyProtocol_ces_ObjectIdentity = ObjectIdentity
id_SW_AdvancedRouting_VirtualRouterRedundancyProtocol_ces = _Id_SW_AdvancedRouting_VirtualRouterRedundancyProtocol_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 16, 1, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    id_SW_AdvancedRouting_VirtualRouterRedundancyProtocol_ces.setStatus("current")
_Id_SW_AdvancedRouting_BandWidthManagement_ces_ObjectIdentity = ObjectIdentity
id_SW_AdvancedRouting_BandWidthManagement_ces = _Id_SW_AdvancedRouting_BandWidthManagement_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 16, 1, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    id_SW_AdvancedRouting_BandWidthManagement_ces.setStatus("current")
_Id_SW_AdvancedRouting_DiffServ_ces_ObjectIdentity = ObjectIdentity
id_SW_AdvancedRouting_DiffServ_ces = _Id_SW_AdvancedRouting_DiffServ_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 16, 1, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    id_SW_AdvancedRouting_DiffServ_ces.setStatus("current")
_Id_SW_DataLinkSwitchingFeature_ces_ObjectIdentity = ObjectIdentity
id_SW_DataLinkSwitchingFeature_ces = _Id_SW_DataLinkSwitchingFeature_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 16, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    id_SW_DataLinkSwitchingFeature_ces.setStatus("current")
_Id_SW_Routing_BGPRouting_ces_ObjectIdentity = ObjectIdentity
id_SW_Routing_BGPRouting_ces = _Id_SW_Routing_BGPRouting_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 16, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    id_SW_Routing_BGPRouting_ces.setStatus("current")
_Id_SW_BorderGatewayProtocol_ces_ObjectIdentity = ObjectIdentity
id_SW_BorderGatewayProtocol_ces = _Id_SW_BorderGatewayProtocol_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 16, 1, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    id_SW_BorderGatewayProtocol_ces.setStatus("current")
_Id_SW_Routing_Premium_Routing_ces_ObjectIdentity = ObjectIdentity
id_SW_Routing_Premium_Routing_ces = _Id_SW_Routing_Premium_Routing_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 16, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    id_SW_Routing_Premium_Routing_ces.setStatus("current")
_Id_SW_Security_ces_ObjectIdentity = ObjectIdentity
id_SW_Security_ces = _Id_SW_Security_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 16, 1, 1, 2)
)
if mibBuilder.loadTexts:
    id_SW_Security_ces.setStatus("current")
_Id_SW_Security_Firewall_ces_ObjectIdentity = ObjectIdentity
id_SW_Security_Firewall_ces = _Id_SW_Security_Firewall_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 16, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    id_SW_Security_Firewall_ces.setStatus("current")
_Id_SW_Firewall_Contivity_ces_ObjectIdentity = ObjectIdentity
id_SW_Firewall_Contivity_ces = _Id_SW_Firewall_Contivity_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 16, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    id_SW_Firewall_Contivity_ces.setStatus("current")
_Id_SW_Contivity_Stateful_Inspection_ces_ObjectIdentity = ObjectIdentity
id_SW_Contivity_Stateful_Inspection_ces = _Id_SW_Contivity_Stateful_Inspection_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 16, 1, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    id_SW_Contivity_Stateful_Inspection_ces.setStatus("current")
_Id_SW_Contivity_Interface_Filters_ces_ObjectIdentity = ObjectIdentity
id_SW_Contivity_Interface_Filters_ces = _Id_SW_Contivity_Interface_Filters_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 16, 1, 1, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    id_SW_Contivity_Interface_Filters_ces.setStatus("current")
_Id_SW_Firewall_CheckPoint_ces_ObjectIdentity = ObjectIdentity
id_SW_Firewall_CheckPoint_ces = _Id_SW_Firewall_CheckPoint_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 16, 1, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    id_SW_Firewall_CheckPoint_ces.setStatus("current")
_Id_SW_Security_FIPS_ces_ObjectIdentity = ObjectIdentity
id_SW_Security_FIPS_ces = _Id_SW_Security_FIPS_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 16, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    id_SW_Security_FIPS_ces.setStatus("current")
_Id_SW_Tunnel_ces_ObjectIdentity = ObjectIdentity
id_SW_Tunnel_ces = _Id_SW_Tunnel_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 16, 1, 1, 3)
)
if mibBuilder.loadTexts:
    id_SW_Tunnel_ces.setStatus("current")
_Id_SW_Tunnel_BaseLevel_ces_ObjectIdentity = ObjectIdentity
id_SW_Tunnel_BaseLevel_ces = _Id_SW_Tunnel_BaseLevel_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 16, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    id_SW_Tunnel_BaseLevel_ces.setStatus("current")
_Id_Hardware_ces_ObjectIdentity = ObjectIdentity
id_Hardware_ces = _Id_Hardware_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 16, 2)
)
if mibBuilder.loadTexts:
    id_Hardware_ces.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CONTIVITY-ID-V1-MIB",
    **{"id-ces": id_ces,
       "id-Software-ces": id_Software_ces,
       "id-SW-Server-ces": id_SW_Server_ces,
       "id-SW-Routing-ces": id_SW_Routing_ces,
       "id-SW-Routing-RoutingInformationProtocol-ces": id_SW_Routing_RoutingInformationProtocol_ces,
       "id-SW-Routing-AdvancedRouting-ces": id_SW_Routing_AdvancedRouting_ces,
       "id-SW-AdvancedRouting-OpenShortestPathFirst-ces": id_SW_AdvancedRouting_OpenShortestPathFirst_ces,
       "id-SW-AdvancedRouting-VirtualRouterRedundancyProtocol-ces": id_SW_AdvancedRouting_VirtualRouterRedundancyProtocol_ces,
       "id-SW-AdvancedRouting-BandWidthManagement-ces": id_SW_AdvancedRouting_BandWidthManagement_ces,
       "id-SW-AdvancedRouting-DiffServ-ces": id_SW_AdvancedRouting_DiffServ_ces,
       "id-SW-DataLinkSwitchingFeature-ces": id_SW_DataLinkSwitchingFeature_ces,
       "id-SW-Routing-BGPRouting-ces": id_SW_Routing_BGPRouting_ces,
       "id-SW-BorderGatewayProtocol-ces": id_SW_BorderGatewayProtocol_ces,
       "id-SW-Routing-Premium-Routing-ces": id_SW_Routing_Premium_Routing_ces,
       "id-SW-Security-ces": id_SW_Security_ces,
       "id-SW-Security-Firewall-ces": id_SW_Security_Firewall_ces,
       "id-SW-Firewall-Contivity-ces": id_SW_Firewall_Contivity_ces,
       "id-SW-Contivity-Stateful-Inspection-ces": id_SW_Contivity_Stateful_Inspection_ces,
       "id-SW-Contivity-Interface-Filters-ces": id_SW_Contivity_Interface_Filters_ces,
       "id-SW-Firewall-CheckPoint-ces": id_SW_Firewall_CheckPoint_ces,
       "id-SW-Security-FIPS-ces": id_SW_Security_FIPS_ces,
       "id-SW-Tunnel-ces": id_SW_Tunnel_ces,
       "id-SW-Tunnel-BaseLevel-ces": id_SW_Tunnel_BaseLevel_ces,
       "id-Hardware-ces": id_Hardware_ces}
)
