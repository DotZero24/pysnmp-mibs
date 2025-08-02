_H='aniBsuSuMacAddr'
_G='BSUSUINV-MIB'
_F='Integer32'
_E='aniBsuWirelessPort'
_D='BSUWIRELESSIF-MIB'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aniBsuSuGroup,=mibBuilder.importSymbols('ANIROOT-MIB','aniBsuSuGroup')
aniBsuWirelessPort,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'MacAddress','PhysAddress','TextualConvention')
aniBsuSuInventory=ModuleIdentity((1,3,6,1,4,1,4325,3,7,1))
_AniBsuSuInvTable_Object=MibTable
aniBsuSuInvTable=_AniBsuSuInvTable_Object((1,3,6,1,4,1,4325,3,7,1,1))
if mibBuilder.loadTexts:aniBsuSuInvTable.setStatus(_A)
_AniBsuSuInvEntry_Object=MibTableRow
aniBsuSuInvEntry=_AniBsuSuInvEntry_Object((1,3,6,1,4,1,4325,3,7,1,1,1))
aniBsuSuInvEntry.setIndexNames((0,_D,_E),(0,_G,_H))
if mibBuilder.loadTexts:aniBsuSuInvEntry.setStatus(_A)
_AniBsuSuMacAddr_Type=MacAddress
_AniBsuSuMacAddr_Object=MibTableColumn
aniBsuSuMacAddr=_AniBsuSuMacAddr_Object((1,3,6,1,4,1,4325,3,7,1,1,1,1),_AniBsuSuMacAddr_Type())
aniBsuSuMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSuMacAddr.setStatus(_A)
_AniBsuSuIpAddr_Type=IpAddress
_AniBsuSuIpAddr_Object=MibTableColumn
aniBsuSuIpAddr=_AniBsuSuIpAddr_Object((1,3,6,1,4,1,4325,3,7,1,1,1,3),_AniBsuSuIpAddr_Type())
aniBsuSuIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSuIpAddr.setStatus(_A)
class _AniBsuSuName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_AniBsuSuName_Type.__name__=_C
_AniBsuSuName_Object=MibTableColumn
aniBsuSuName=_AniBsuSuName_Object((1,3,6,1,4,1,4325,3,7,1,1,1,4),_AniBsuSuName_Type())
aniBsuSuName.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSuName.setStatus(_A)
class _AniBsuSuCustomerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_AniBsuSuCustomerName_Type.__name__=_C
_AniBsuSuCustomerName_Object=MibTableColumn
aniBsuSuCustomerName=_AniBsuSuCustomerName_Object((1,3,6,1,4,1,4325,3,7,1,1,1,5),_AniBsuSuCustomerName_Type())
aniBsuSuCustomerName.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSuCustomerName.setStatus(_A)
class _AniBsuSuLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,255)));namedValues=NamedValues(*(('initial',1),('ulm-req-rcvd',2),('ulm-rsp-sent',3),('dhcp-req-rcvd',4),('dhcp-rsp-sent',5),('tod-req-rcvd',6),('tod-rsp-sent',7),('config-file-req-rcvd',8),('config-file-req-sent',9),('reg-req-rcvd',10),('lic-rsp-recd',11),('reg-rsp-sent',12),('reg-ack-rcvd',13),('operational',14),('stand-by',15),('delete',255)))
_AniBsuSuLinkStatus_Type.__name__=_F
_AniBsuSuLinkStatus_Object=MibTableColumn
aniBsuSuLinkStatus=_AniBsuSuLinkStatus_Object((1,3,6,1,4,1,4325,3,7,1,1,1,6),_AniBsuSuLinkStatus_Type())
aniBsuSuLinkStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:aniBsuSuLinkStatus.setStatus(_A)
_AniBsuSuModelNumber_Type=DisplayString
_AniBsuSuModelNumber_Object=MibTableColumn
aniBsuSuModelNumber=_AniBsuSuModelNumber_Object((1,3,6,1,4,1,4325,3,7,1,1,1,7),_AniBsuSuModelNumber_Type())
aniBsuSuModelNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSuModelNumber.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'aniBsuSuInventory':aniBsuSuInventory,'aniBsuSuInvTable':aniBsuSuInvTable,'aniBsuSuInvEntry':aniBsuSuInvEntry,_H:aniBsuSuMacAddr,'aniBsuSuIpAddr':aniBsuSuIpAddr,'aniBsuSuName':aniBsuSuName,'aniBsuSuCustomerName':aniBsuSuCustomerName,'aniBsuSuLinkStatus':aniBsuSuLinkStatus,'aniBsuSuModelNumber':aniBsuSuModelNumber})