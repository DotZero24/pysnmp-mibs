_E='nmsDhcpIpAddrPoolIndex'
_D='FS-NMS-DHCP-SERVER-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nmsMgmt,=mibBuilder.importSymbols('FS-NMS-SMI','nmsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Dhcp_ObjectIdentity=ObjectIdentity
dhcp=_Dhcp_ObjectIdentity((1,3,6,1,4,1,52642,9,355))
class _DhcpServerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_DhcpServerStatus_Type.__name__=_C
_DhcpServerStatus_Object=MibScalar
dhcpServerStatus=_DhcpServerStatus_Object((1,3,6,1,4,1,52642,9,355,1),_DhcpServerStatus_Type())
dhcpServerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpServerStatus.setStatus(_A)
_NmsDhcpIpAddrPoolTable_Object=MibTable
nmsDhcpIpAddrPoolTable=_NmsDhcpIpAddrPoolTable_Object((1,3,6,1,4,1,52642,9,355,2))
if mibBuilder.loadTexts:nmsDhcpIpAddrPoolTable.setStatus(_A)
_NmsDhcpIpAddrPoolEntry_Object=MibTableRow
nmsDhcpIpAddrPoolEntry=_NmsDhcpIpAddrPoolEntry_Object((1,3,6,1,4,1,52642,9,355,2,1))
nmsDhcpIpAddrPoolEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:nmsDhcpIpAddrPoolEntry.setStatus(_A)
_NmsDhcpIpAddrPoolIndex_Type=Integer32
_NmsDhcpIpAddrPoolIndex_Object=MibTableColumn
nmsDhcpIpAddrPoolIndex=_NmsDhcpIpAddrPoolIndex_Object((1,3,6,1,4,1,52642,9,355,2,1,1),_NmsDhcpIpAddrPoolIndex_Type())
nmsDhcpIpAddrPoolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsDhcpIpAddrPoolIndex.setStatus(_A)
_NmsDhcpIpAddrPoolSubNetwork_Type=IpAddress
_NmsDhcpIpAddrPoolSubNetwork_Object=MibTableColumn
nmsDhcpIpAddrPoolSubNetwork=_NmsDhcpIpAddrPoolSubNetwork_Object((1,3,6,1,4,1,52642,9,355,2,1,2),_NmsDhcpIpAddrPoolSubNetwork_Type())
nmsDhcpIpAddrPoolSubNetwork.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsDhcpIpAddrPoolSubNetwork.setStatus(_A)
_NmsDhcpIpAddrPoolMask_Type=IpAddress
_NmsDhcpIpAddrPoolMask_Object=MibTableColumn
nmsDhcpIpAddrPoolMask=_NmsDhcpIpAddrPoolMask_Object((1,3,6,1,4,1,52642,9,355,2,1,3),_NmsDhcpIpAddrPoolMask_Type())
nmsDhcpIpAddrPoolMask.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsDhcpIpAddrPoolMask.setStatus(_A)
_NmsDhcpIpAddrPoolStart_Type=IpAddress
_NmsDhcpIpAddrPoolStart_Object=MibTableColumn
nmsDhcpIpAddrPoolStart=_NmsDhcpIpAddrPoolStart_Object((1,3,6,1,4,1,52642,9,355,2,1,4),_NmsDhcpIpAddrPoolStart_Type())
nmsDhcpIpAddrPoolStart.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsDhcpIpAddrPoolStart.setStatus(_A)
_NmsDhcpIpAddrPoolEnd_Type=IpAddress
_NmsDhcpIpAddrPoolEnd_Object=MibTableColumn
nmsDhcpIpAddrPoolEnd=_NmsDhcpIpAddrPoolEnd_Object((1,3,6,1,4,1,52642,9,355,2,1,5),_NmsDhcpIpAddrPoolEnd_Type())
nmsDhcpIpAddrPoolEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsDhcpIpAddrPoolEnd.setStatus(_A)
_NmsDhcpIpAddrPoolReserveAddrList_Type=OctetString
_NmsDhcpIpAddrPoolReserveAddrList_Object=MibTableColumn
nmsDhcpIpAddrPoolReserveAddrList=_NmsDhcpIpAddrPoolReserveAddrList_Object((1,3,6,1,4,1,52642,9,355,2,1,6),_NmsDhcpIpAddrPoolReserveAddrList_Type())
nmsDhcpIpAddrPoolReserveAddrList.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsDhcpIpAddrPoolReserveAddrList.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'dhcp':dhcp,'dhcpServerStatus':dhcpServerStatus,'nmsDhcpIpAddrPoolTable':nmsDhcpIpAddrPoolTable,'nmsDhcpIpAddrPoolEntry':nmsDhcpIpAddrPoolEntry,_E:nmsDhcpIpAddrPoolIndex,'nmsDhcpIpAddrPoolSubNetwork':nmsDhcpIpAddrPoolSubNetwork,'nmsDhcpIpAddrPoolMask':nmsDhcpIpAddrPoolMask,'nmsDhcpIpAddrPoolStart':nmsDhcpIpAddrPoolStart,'nmsDhcpIpAddrPoolEnd':nmsDhcpIpAddrPoolEnd,'nmsDhcpIpAddrPoolReserveAddrList':nmsDhcpIpAddrPoolReserveAddrList})