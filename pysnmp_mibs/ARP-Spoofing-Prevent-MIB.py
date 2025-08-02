_F='read-create'
_E='read-only'
_D='swARPSpoofingPreventMgmtGatewayMAC'
_C='swARPSpoofingPreventMgmtGatewayIP'
_B='ARP-Spoofing-Prevent-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
swARPSpoofingPreventMIB=ModuleIdentity((1,3,6,1,4,1,171,12,62))
class PortList(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwARPSpoofingPreventCtrl_ObjectIdentity=ObjectIdentity
swARPSpoofingPreventCtrl=_SwARPSpoofingPreventCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,62,1))
_SwARPSpoofingPreventInfo_ObjectIdentity=ObjectIdentity
swARPSpoofingPreventInfo=_SwARPSpoofingPreventInfo_ObjectIdentity((1,3,6,1,4,1,171,12,62,2))
_SwARPSpoofingPreventMgmt_ObjectIdentity=ObjectIdentity
swARPSpoofingPreventMgmt=_SwARPSpoofingPreventMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,62,3))
_SwARPSpoofingPreventMgmtTable_Object=MibTable
swARPSpoofingPreventMgmtTable=_SwARPSpoofingPreventMgmtTable_Object((1,3,6,1,4,1,171,12,62,3,1))
if mibBuilder.loadTexts:swARPSpoofingPreventMgmtTable.setStatus(_A)
_SwARPSpoofingPreventMgmtEntry_Object=MibTableRow
swARPSpoofingPreventMgmtEntry=_SwARPSpoofingPreventMgmtEntry_Object((1,3,6,1,4,1,171,12,62,3,1,1))
swARPSpoofingPreventMgmtEntry.setIndexNames((0,_B,_C),(0,_B,_D))
if mibBuilder.loadTexts:swARPSpoofingPreventMgmtEntry.setStatus(_A)
_SwARPSpoofingPreventMgmtGatewayIP_Type=IpAddress
_SwARPSpoofingPreventMgmtGatewayIP_Object=MibTableColumn
swARPSpoofingPreventMgmtGatewayIP=_SwARPSpoofingPreventMgmtGatewayIP_Object((1,3,6,1,4,1,171,12,62,3,1,1,1),_SwARPSpoofingPreventMgmtGatewayIP_Type())
swARPSpoofingPreventMgmtGatewayIP.setMaxAccess(_E)
if mibBuilder.loadTexts:swARPSpoofingPreventMgmtGatewayIP.setStatus(_A)
_SwARPSpoofingPreventMgmtGatewayMAC_Type=MacAddress
_SwARPSpoofingPreventMgmtGatewayMAC_Object=MibTableColumn
swARPSpoofingPreventMgmtGatewayMAC=_SwARPSpoofingPreventMgmtGatewayMAC_Object((1,3,6,1,4,1,171,12,62,3,1,1,2),_SwARPSpoofingPreventMgmtGatewayMAC_Type())
swARPSpoofingPreventMgmtGatewayMAC.setMaxAccess(_E)
if mibBuilder.loadTexts:swARPSpoofingPreventMgmtGatewayMAC.setStatus(_A)
_SwARPSpoofingPreventMgmtPorts_Type=PortList
_SwARPSpoofingPreventMgmtPorts_Object=MibTableColumn
swARPSpoofingPreventMgmtPorts=_SwARPSpoofingPreventMgmtPorts_Object((1,3,6,1,4,1,171,12,62,3,1,1,3),_SwARPSpoofingPreventMgmtPorts_Type())
swARPSpoofingPreventMgmtPorts.setMaxAccess(_F)
if mibBuilder.loadTexts:swARPSpoofingPreventMgmtPorts.setStatus(_A)
_SwARPSpoofingPreventMgmtStatus_Type=RowStatus
_SwARPSpoofingPreventMgmtStatus_Object=MibTableColumn
swARPSpoofingPreventMgmtStatus=_SwARPSpoofingPreventMgmtStatus_Object((1,3,6,1,4,1,171,12,62,3,1,1,4),_SwARPSpoofingPreventMgmtStatus_Type())
swARPSpoofingPreventMgmtStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:swARPSpoofingPreventMgmtStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'PortList':PortList,'swARPSpoofingPreventMIB':swARPSpoofingPreventMIB,'swARPSpoofingPreventCtrl':swARPSpoofingPreventCtrl,'swARPSpoofingPreventInfo':swARPSpoofingPreventInfo,'swARPSpoofingPreventMgmt':swARPSpoofingPreventMgmt,'swARPSpoofingPreventMgmtTable':swARPSpoofingPreventMgmtTable,'swARPSpoofingPreventMgmtEntry':swARPSpoofingPreventMgmtEntry,_C:swARPSpoofingPreventMgmtGatewayIP,_D:swARPSpoofingPreventMgmtGatewayMAC,'swARPSpoofingPreventMgmtPorts':swARPSpoofingPreventMgmtPorts,'swARPSpoofingPreventMgmtStatus':swARPSpoofingPreventMgmtStatus})