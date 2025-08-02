_O='zxUasActiveSubscriberPPPID'
_N='zxUasActiveSubscriberIPAddr'
_M='zxUasActiveSubscriberVirtualRouteField'
_L='zxUasIPPoolEndIPAddr'
_K='zxUasIPPoolStartIPAddr'
_J='zxUasIPPoolID'
_I='zxUasIPPoolInterfaceName'
_H='zxUasIPPoolVirtualRouteField'
_G='zxUasIPPoolName'
_F='zxUasActiveSubscriberType'
_E='DisplayString'
_D='Integer32'
_C='UAS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
zxUasMib=ModuleIdentity((1,3,6,1,4,1,3902,1006,1))
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_ZxUas_ObjectIdentity=ObjectIdentity
zxUas=_ZxUas_ObjectIdentity((1,3,6,1,4,1,3902,1006))
_ZxUasMibObjects_ObjectIdentity=ObjectIdentity
zxUasMibObjects=_ZxUasMibObjects_ObjectIdentity((1,3,6,1,4,1,3902,1006,1,1))
_ZxUasSystemGroup_ObjectIdentity=ObjectIdentity
zxUasSystemGroup=_ZxUasSystemGroup_ObjectIdentity((1,3,6,1,4,1,3902,1006,1,1,1))
_ZxUasServiceMgmtGroup_ObjectIdentity=ObjectIdentity
zxUasServiceMgmtGroup=_ZxUasServiceMgmtGroup_ObjectIdentity((1,3,6,1,4,1,3902,1006,1,1,2))
_ZxUasInterfaceIPPoolTable_Object=MibTable
zxUasInterfaceIPPoolTable=_ZxUasInterfaceIPPoolTable_Object((1,3,6,1,4,1,3902,1006,1,1,2,1))
if mibBuilder.loadTexts:zxUasInterfaceIPPoolTable.setStatus(_A)
_ZxUasInterfaceIPPoolEntry_Object=MibTableRow
zxUasInterfaceIPPoolEntry=_ZxUasInterfaceIPPoolEntry_Object((1,3,6,1,4,1,3902,1006,1,1,2,1,1))
zxUasInterfaceIPPoolEntry.setIndexNames((0,_C,_G),(0,_C,_H),(0,_C,_I),(0,_C,_J),(0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:zxUasInterfaceIPPoolEntry.setStatus(_A)
class _ZxUasIPPoolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ZxUasIPPoolName_Type.__name__=_E
_ZxUasIPPoolName_Object=MibTableColumn
zxUasIPPoolName=_ZxUasIPPoolName_Object((1,3,6,1,4,1,3902,1006,1,1,2,1,1,1),_ZxUasIPPoolName_Type())
zxUasIPPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasIPPoolName.setStatus(_A)
class _ZxUasIPPoolVirtualRouteField_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_ZxUasIPPoolVirtualRouteField_Type.__name__=_E
_ZxUasIPPoolVirtualRouteField_Object=MibTableColumn
zxUasIPPoolVirtualRouteField=_ZxUasIPPoolVirtualRouteField_Object((1,3,6,1,4,1,3902,1006,1,1,2,1,1,2),_ZxUasIPPoolVirtualRouteField_Type())
zxUasIPPoolVirtualRouteField.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasIPPoolVirtualRouteField.setStatus(_A)
class _ZxUasIPPoolInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ZxUasIPPoolInterfaceName_Type.__name__=_E
_ZxUasIPPoolInterfaceName_Object=MibTableColumn
zxUasIPPoolInterfaceName=_ZxUasIPPoolInterfaceName_Object((1,3,6,1,4,1,3902,1006,1,1,2,1,1,3),_ZxUasIPPoolInterfaceName_Type())
zxUasIPPoolInterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasIPPoolInterfaceName.setStatus(_A)
_ZxUasIPPoolID_Type=Integer32
_ZxUasIPPoolID_Object=MibTableColumn
zxUasIPPoolID=_ZxUasIPPoolID_Object((1,3,6,1,4,1,3902,1006,1,1,2,1,1,4),_ZxUasIPPoolID_Type())
zxUasIPPoolID.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasIPPoolID.setStatus(_A)
_ZxUasIPPoolStartIPAddr_Type=IpAddress
_ZxUasIPPoolStartIPAddr_Object=MibTableColumn
zxUasIPPoolStartIPAddr=_ZxUasIPPoolStartIPAddr_Object((1,3,6,1,4,1,3902,1006,1,1,2,1,1,5),_ZxUasIPPoolStartIPAddr_Type())
zxUasIPPoolStartIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasIPPoolStartIPAddr.setStatus(_A)
_ZxUasIPPoolEndIPAddr_Type=IpAddress
_ZxUasIPPoolEndIPAddr_Object=MibTableColumn
zxUasIPPoolEndIPAddr=_ZxUasIPPoolEndIPAddr_Object((1,3,6,1,4,1,3902,1006,1,1,2,1,1,6),_ZxUasIPPoolEndIPAddr_Type())
zxUasIPPoolEndIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasIPPoolEndIPAddr.setStatus(_A)
class _ZxUasIPPoolFreeIPNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_ZxUasIPPoolFreeIPNum_Type.__name__=_D
_ZxUasIPPoolFreeIPNum_Object=MibTableColumn
zxUasIPPoolFreeIPNum=_ZxUasIPPoolFreeIPNum_Object((1,3,6,1,4,1,3902,1006,1,1,2,1,1,7),_ZxUasIPPoolFreeIPNum_Type())
zxUasIPPoolFreeIPNum.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasIPPoolFreeIPNum.setStatus(_A)
class _ZxUasIPPoolUsedIPNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_ZxUasIPPoolUsedIPNum_Type.__name__=_D
_ZxUasIPPoolUsedIPNum_Object=MibTableColumn
zxUasIPPoolUsedIPNum=_ZxUasIPPoolUsedIPNum_Object((1,3,6,1,4,1,3902,1006,1,1,2,1,1,8),_ZxUasIPPoolUsedIPNum_Type())
zxUasIPPoolUsedIPNum.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasIPPoolUsedIPNum.setStatus(_A)
class _ZxUasIPPoolUnavailableIPNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_ZxUasIPPoolUnavailableIPNum_Type.__name__=_D
_ZxUasIPPoolUnavailableIPNum_Object=MibTableColumn
zxUasIPPoolUnavailableIPNum=_ZxUasIPPoolUnavailableIPNum_Object((1,3,6,1,4,1,3902,1006,1,1,2,1,1,9),_ZxUasIPPoolUnavailableIPNum_Type())
zxUasIPPoolUnavailableIPNum.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasIPPoolUnavailableIPNum.setStatus(_A)
class _ZxUasIPPoolBindToDomainFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unreserved',1),('reserved',2)))
_ZxUasIPPoolBindToDomainFlag_Type.__name__=_D
_ZxUasIPPoolBindToDomainFlag_Object=MibTableColumn
zxUasIPPoolBindToDomainFlag=_ZxUasIPPoolBindToDomainFlag_Object((1,3,6,1,4,1,3902,1006,1,1,2,1,1,10),_ZxUasIPPoolBindToDomainFlag_Type())
zxUasIPPoolBindToDomainFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasIPPoolBindToDomainFlag.setStatus(_A)
_ZxUasActiveSubscriberTable_Object=MibTable
zxUasActiveSubscriberTable=_ZxUasActiveSubscriberTable_Object((1,3,6,1,4,1,3902,1006,1,1,2,2))
if mibBuilder.loadTexts:zxUasActiveSubscriberTable.setStatus(_A)
_ZxUasActiveSubscriberEntry_Object=MibTableRow
zxUasActiveSubscriberEntry=_ZxUasActiveSubscriberEntry_Object((1,3,6,1,4,1,3902,1006,1,1,2,2,1))
zxUasActiveSubscriberEntry.setIndexNames((0,_C,_M),(0,_C,_N),(0,_C,_F),(0,_C,_O))
if mibBuilder.loadTexts:zxUasActiveSubscriberEntry.setStatus(_A)
class _ZxUasActiveSubscriberVirtualRouteField_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_ZxUasActiveSubscriberVirtualRouteField_Type.__name__=_E
_ZxUasActiveSubscriberVirtualRouteField_Object=MibTableColumn
zxUasActiveSubscriberVirtualRouteField=_ZxUasActiveSubscriberVirtualRouteField_Object((1,3,6,1,4,1,3902,1006,1,1,2,2,1,1),_ZxUasActiveSubscriberVirtualRouteField_Type())
zxUasActiveSubscriberVirtualRouteField.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasActiveSubscriberVirtualRouteField.setStatus(_A)
_ZxUasActiveSubscriberIPAddr_Type=IpAddress
_ZxUasActiveSubscriberIPAddr_Object=MibTableColumn
zxUasActiveSubscriberIPAddr=_ZxUasActiveSubscriberIPAddr_Object((1,3,6,1,4,1,3902,1006,1,1,2,2,1,2),_ZxUasActiveSubscriberIPAddr_Type())
zxUasActiveSubscriberIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasActiveSubscriberIPAddr.setStatus(_A)
class _ZxUasActiveSubscriberType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('ppp',1),('ipdhcp',2),('remotedhcp',3),('ipdhcprelay',4),('iphost',5),('remotehost',6),('vpn',7),('brg',8)))
_ZxUasActiveSubscriberType_Type.__name__=_D
_ZxUasActiveSubscriberType_Object=MibTableColumn
zxUasActiveSubscriberType=_ZxUasActiveSubscriberType_Object((1,3,6,1,4,1,3902,1006,1,1,2,2,1,3),_ZxUasActiveSubscriberType_Type())
zxUasActiveSubscriberType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasActiveSubscriberType.setStatus(_A)
_ZxUasActiveSubscriberPPPID_Type=Integer32
_ZxUasActiveSubscriberPPPID_Object=MibTableColumn
zxUasActiveSubscriberPPPID=_ZxUasActiveSubscriberPPPID_Object((1,3,6,1,4,1,3902,1006,1,1,2,2,1,4),_ZxUasActiveSubscriberPPPID_Type())
zxUasActiveSubscriberPPPID.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasActiveSubscriberPPPID.setStatus(_A)
class _ZxUasActiveSubscriberName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_ZxUasActiveSubscriberName_Type.__name__=_E
_ZxUasActiveSubscriberName_Object=MibTableColumn
zxUasActiveSubscriberName=_ZxUasActiveSubscriberName_Object((1,3,6,1,4,1,3902,1006,1,1,2,2,1,5),_ZxUasActiveSubscriberName_Type())
zxUasActiveSubscriberName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasActiveSubscriberName.setStatus(_A)
class _ZxUasActiveSubscriberInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ZxUasActiveSubscriberInterfaceName_Type.__name__=_E
_ZxUasActiveSubscriberInterfaceName_Object=MibTableColumn
zxUasActiveSubscriberInterfaceName=_ZxUasActiveSubscriberInterfaceName_Object((1,3,6,1,4,1,3902,1006,1,1,2,2,1,6),_ZxUasActiveSubscriberInterfaceName_Type())
zxUasActiveSubscriberInterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasActiveSubscriberInterfaceName.setStatus(_A)
_ZxUasActiveSubscriberDoaminID_Type=Integer32
_ZxUasActiveSubscriberDoaminID_Object=MibTableColumn
zxUasActiveSubscriberDoaminID=_ZxUasActiveSubscriberDoaminID_Object((1,3,6,1,4,1,3902,1006,1,1,2,2,1,7),_ZxUasActiveSubscriberDoaminID_Type())
zxUasActiveSubscriberDoaminID.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasActiveSubscriberDoaminID.setStatus(_A)
_ZxUasActiveSubscriberSlot_Type=Integer32
_ZxUasActiveSubscriberSlot_Object=MibTableColumn
zxUasActiveSubscriberSlot=_ZxUasActiveSubscriberSlot_Object((1,3,6,1,4,1,3902,1006,1,1,2,2,1,8),_ZxUasActiveSubscriberSlot_Type())
zxUasActiveSubscriberSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasActiveSubscriberSlot.setStatus(_A)
_ZxUasActiveSubscriberPort_Type=Integer32
_ZxUasActiveSubscriberPort_Object=MibTableColumn
zxUasActiveSubscriberPort=_ZxUasActiveSubscriberPort_Object((1,3,6,1,4,1,3902,1006,1,1,2,2,1,9),_ZxUasActiveSubscriberPort_Type())
zxUasActiveSubscriberPort.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasActiveSubscriberPort.setStatus(_A)
_ZxUasActiveSubscriberVlanId_Type=Integer32
_ZxUasActiveSubscriberVlanId_Object=MibTableColumn
zxUasActiveSubscriberVlanId=_ZxUasActiveSubscriberVlanId_Object((1,3,6,1,4,1,3902,1006,1,1,2,2,1,10),_ZxUasActiveSubscriberVlanId_Type())
zxUasActiveSubscriberVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasActiveSubscriberVlanId.setStatus(_A)
_ZxUasActiveSubscriberVpi_Type=Integer32
_ZxUasActiveSubscriberVpi_Object=MibTableColumn
zxUasActiveSubscriberVpi=_ZxUasActiveSubscriberVpi_Object((1,3,6,1,4,1,3902,1006,1,1,2,2,1,11),_ZxUasActiveSubscriberVpi_Type())
zxUasActiveSubscriberVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasActiveSubscriberVpi.setStatus(_A)
_ZxUasActiveSubscriberVci_Type=Integer32
_ZxUasActiveSubscriberVci_Object=MibTableColumn
zxUasActiveSubscriberVci=_ZxUasActiveSubscriberVci_Object((1,3,6,1,4,1,3902,1006,1,1,2,2,1,12),_ZxUasActiveSubscriberVci_Type())
zxUasActiveSubscriberVci.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasActiveSubscriberVci.setStatus(_A)
_ZxUasActiveSubscriberMACAddr_Type=PhysAddress
_ZxUasActiveSubscriberMACAddr_Object=MibTableColumn
zxUasActiveSubscriberMACAddr=_ZxUasActiveSubscriberMACAddr_Object((1,3,6,1,4,1,3902,1006,1,1,2,2,1,13),_ZxUasActiveSubscriberMACAddr_Type())
zxUasActiveSubscriberMACAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasActiveSubscriberMACAddr.setStatus(_A)
_ZxUasActiveSubscriberUpOctets_Type=Counter32
_ZxUasActiveSubscriberUpOctets_Object=MibTableColumn
zxUasActiveSubscriberUpOctets=_ZxUasActiveSubscriberUpOctets_Object((1,3,6,1,4,1,3902,1006,1,1,2,2,1,14),_ZxUasActiveSubscriberUpOctets_Type())
zxUasActiveSubscriberUpOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasActiveSubscriberUpOctets.setStatus(_A)
_ZxUasActiveSubscriberUpGigaOctets_Type=Counter32
_ZxUasActiveSubscriberUpGigaOctets_Object=MibTableColumn
zxUasActiveSubscriberUpGigaOctets=_ZxUasActiveSubscriberUpGigaOctets_Object((1,3,6,1,4,1,3902,1006,1,1,2,2,1,15),_ZxUasActiveSubscriberUpGigaOctets_Type())
zxUasActiveSubscriberUpGigaOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasActiveSubscriberUpGigaOctets.setStatus(_A)
_ZxUasActiveSubscriberDownOctets_Type=Counter32
_ZxUasActiveSubscriberDownOctets_Object=MibTableColumn
zxUasActiveSubscriberDownOctets=_ZxUasActiveSubscriberDownOctets_Object((1,3,6,1,4,1,3902,1006,1,1,2,2,1,16),_ZxUasActiveSubscriberDownOctets_Type())
zxUasActiveSubscriberDownOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasActiveSubscriberDownOctets.setStatus(_A)
_ZxUasActiveSubscriberDownGigaOctets_Type=Counter32
_ZxUasActiveSubscriberDownGigaOctets_Object=MibTableColumn
zxUasActiveSubscriberDownGigaOctets=_ZxUasActiveSubscriberDownGigaOctets_Object((1,3,6,1,4,1,3902,1006,1,1,2,2,1,17),_ZxUasActiveSubscriberDownGigaOctets_Type())
zxUasActiveSubscriberDownGigaOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasActiveSubscriberDownGigaOctets.setStatus(_A)
_ZxUasActiveDhcpSubscriberAuthFlag_Type=Integer32
_ZxUasActiveDhcpSubscriberAuthFlag_Object=MibTableColumn
zxUasActiveDhcpSubscriberAuthFlag=_ZxUasActiveDhcpSubscriberAuthFlag_Object((1,3,6,1,4,1,3902,1006,1,1,2,2,1,18),_ZxUasActiveDhcpSubscriberAuthFlag_Type())
zxUasActiveDhcpSubscriberAuthFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasActiveDhcpSubscriberAuthFlag.setStatus(_A)
_ZxUasActiveSubscriberUpTime_Type=TimeTicks
_ZxUasActiveSubscriberUpTime_Object=MibTableColumn
zxUasActiveSubscriberUpTime=_ZxUasActiveSubscriberUpTime_Object((1,3,6,1,4,1,3902,1006,1,1,2,2,1,19),_ZxUasActiveSubscriberUpTime_Type())
zxUasActiveSubscriberUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasActiveSubscriberUpTime.setStatus(_A)
class _ZxUasTail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_ZxUasTail_Type.__name__=_D
_ZxUasTail_Object=MibScalar
zxUasTail=_ZxUasTail_Object((1,3,6,1,4,1,3902,1006,1,1,2,3),_ZxUasTail_Type())
zxUasTail.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zxUasTail.setStatus(_A)
_ZxUasStaticsGroup_ObjectIdentity=ObjectIdentity
zxUasStaticsGroup=_ZxUasStaticsGroup_ObjectIdentity((1,3,6,1,4,1,3902,1006,1,1,3))
_ZxUasPppStatics_ObjectIdentity=ObjectIdentity
zxUasPppStatics=_ZxUasPppStatics_ObjectIdentity((1,3,6,1,4,1,3902,1006,1,1,3,1))
_ZxUasPppCallCount_Type=Counter32
_ZxUasPppCallCount_Object=MibScalar
zxUasPppCallCount=_ZxUasPppCallCount_Object((1,3,6,1,4,1,3902,1006,1,1,3,1,1),_ZxUasPppCallCount_Type())
zxUasPppCallCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasPppCallCount.setStatus(_A)
_ZxUasPppCallFailedCount_Type=Counter32
_ZxUasPppCallFailedCount_Object=MibScalar
zxUasPppCallFailedCount=_ZxUasPppCallFailedCount_Object((1,3,6,1,4,1,3902,1006,1,1,3,1,2),_ZxUasPppCallFailedCount_Type())
zxUasPppCallFailedCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasPppCallFailedCount.setStatus(_A)
_ZxUasPppLinkBreakFailedCount_Type=Counter32
_ZxUasPppLinkBreakFailedCount_Object=MibScalar
zxUasPppLinkBreakFailedCount=_ZxUasPppLinkBreakFailedCount_Object((1,3,6,1,4,1,3902,1006,1,1,3,1,3),_ZxUasPppLinkBreakFailedCount_Type())
zxUasPppLinkBreakFailedCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasPppLinkBreakFailedCount.setStatus(_A)
_ZxUasPppAbnormalCloseCount_Type=Counter32
_ZxUasPppAbnormalCloseCount_Object=MibScalar
zxUasPppAbnormalCloseCount=_ZxUasPppAbnormalCloseCount_Object((1,3,6,1,4,1,3902,1006,1,1,3,1,4),_ZxUasPppAbnormalCloseCount_Type())
zxUasPppAbnormalCloseCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasPppAbnormalCloseCount.setStatus(_A)
_ZxUasActiveSubscriberStaticsTable_Object=MibTable
zxUasActiveSubscriberStaticsTable=_ZxUasActiveSubscriberStaticsTable_Object((1,3,6,1,4,1,3902,1006,1,1,3,2))
if mibBuilder.loadTexts:zxUasActiveSubscriberStaticsTable.setStatus(_A)
_ZxUasActiveSubscriberStaticsEntry_Object=MibTableRow
zxUasActiveSubscriberStaticsEntry=_ZxUasActiveSubscriberStaticsEntry_Object((1,3,6,1,4,1,3902,1006,1,1,3,2,1))
zxUasActiveSubscriberStaticsEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:zxUasActiveSubscriberStaticsEntry.setStatus(_A)
_ZxUasActiveSubscriberNum_Type=Integer32
_ZxUasActiveSubscriberNum_Object=MibTableColumn
zxUasActiveSubscriberNum=_ZxUasActiveSubscriberNum_Object((1,3,6,1,4,1,3902,1006,1,1,3,2,1,1),_ZxUasActiveSubscriberNum_Type())
zxUasActiveSubscriberNum.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasActiveSubscriberNum.setStatus(_A)
_ZxUasMaxSubscriberOnlineCount_Type=Integer32
_ZxUasMaxSubscriberOnlineCount_Object=MibScalar
zxUasMaxSubscriberOnlineCount=_ZxUasMaxSubscriberOnlineCount_Object((1,3,6,1,4,1,3902,1006,1,1,3,3),_ZxUasMaxSubscriberOnlineCount_Type())
zxUasMaxSubscriberOnlineCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasMaxSubscriberOnlineCount.setStatus(_A)
class _ZxUasMaxSubscriberOnlineClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normal',0),('clear',1)))
_ZxUasMaxSubscriberOnlineClear_Type.__name__=_D
_ZxUasMaxSubscriberOnlineClear_Object=MibScalar
zxUasMaxSubscriberOnlineClear=_ZxUasMaxSubscriberOnlineClear_Object((1,3,6,1,4,1,3902,1006,1,1,3,4),_ZxUasMaxSubscriberOnlineClear_Type())
zxUasMaxSubscriberOnlineClear.setMaxAccess('read-write')
if mibBuilder.loadTexts:zxUasMaxSubscriberOnlineClear.setStatus(_A)
class _ZxUasMaxSubscriberOnlineTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ZxUasMaxSubscriberOnlineTime_Type.__name__=_E
_ZxUasMaxSubscriberOnlineTime_Object=MibScalar
zxUasMaxSubscriberOnlineTime=_ZxUasMaxSubscriberOnlineTime_Object((1,3,6,1,4,1,3902,1006,1,1,3,5),_ZxUasMaxSubscriberOnlineTime_Type())
zxUasMaxSubscriberOnlineTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zxUasMaxSubscriberOnlineTime.setStatus(_A)
_ZxUasTraps_ObjectIdentity=ObjectIdentity
zxUasTraps=_ZxUasTraps_ObjectIdentity((1,3,6,1,4,1,3902,1006,1,2))
mibBuilder.exportSymbols(_C,**{'zte':zte,'zxUas':zxUas,'zxUasMib':zxUasMib,'zxUasMibObjects':zxUasMibObjects,'zxUasSystemGroup':zxUasSystemGroup,'zxUasServiceMgmtGroup':zxUasServiceMgmtGroup,'zxUasInterfaceIPPoolTable':zxUasInterfaceIPPoolTable,'zxUasInterfaceIPPoolEntry':zxUasInterfaceIPPoolEntry,_G:zxUasIPPoolName,_H:zxUasIPPoolVirtualRouteField,_I:zxUasIPPoolInterfaceName,_J:zxUasIPPoolID,_K:zxUasIPPoolStartIPAddr,_L:zxUasIPPoolEndIPAddr,'zxUasIPPoolFreeIPNum':zxUasIPPoolFreeIPNum,'zxUasIPPoolUsedIPNum':zxUasIPPoolUsedIPNum,'zxUasIPPoolUnavailableIPNum':zxUasIPPoolUnavailableIPNum,'zxUasIPPoolBindToDomainFlag':zxUasIPPoolBindToDomainFlag,'zxUasActiveSubscriberTable':zxUasActiveSubscriberTable,'zxUasActiveSubscriberEntry':zxUasActiveSubscriberEntry,_M:zxUasActiveSubscriberVirtualRouteField,_N:zxUasActiveSubscriberIPAddr,_F:zxUasActiveSubscriberType,_O:zxUasActiveSubscriberPPPID,'zxUasActiveSubscriberName':zxUasActiveSubscriberName,'zxUasActiveSubscriberInterfaceName':zxUasActiveSubscriberInterfaceName,'zxUasActiveSubscriberDoaminID':zxUasActiveSubscriberDoaminID,'zxUasActiveSubscriberSlot':zxUasActiveSubscriberSlot,'zxUasActiveSubscriberPort':zxUasActiveSubscriberPort,'zxUasActiveSubscriberVlanId':zxUasActiveSubscriberVlanId,'zxUasActiveSubscriberVpi':zxUasActiveSubscriberVpi,'zxUasActiveSubscriberVci':zxUasActiveSubscriberVci,'zxUasActiveSubscriberMACAddr':zxUasActiveSubscriberMACAddr,'zxUasActiveSubscriberUpOctets':zxUasActiveSubscriberUpOctets,'zxUasActiveSubscriberUpGigaOctets':zxUasActiveSubscriberUpGigaOctets,'zxUasActiveSubscriberDownOctets':zxUasActiveSubscriberDownOctets,'zxUasActiveSubscriberDownGigaOctets':zxUasActiveSubscriberDownGigaOctets,'zxUasActiveDhcpSubscriberAuthFlag':zxUasActiveDhcpSubscriberAuthFlag,'zxUasActiveSubscriberUpTime':zxUasActiveSubscriberUpTime,'zxUasTail':zxUasTail,'zxUasStaticsGroup':zxUasStaticsGroup,'zxUasPppStatics':zxUasPppStatics,'zxUasPppCallCount':zxUasPppCallCount,'zxUasPppCallFailedCount':zxUasPppCallFailedCount,'zxUasPppLinkBreakFailedCount':zxUasPppLinkBreakFailedCount,'zxUasPppAbnormalCloseCount':zxUasPppAbnormalCloseCount,'zxUasActiveSubscriberStaticsTable':zxUasActiveSubscriberStaticsTable,'zxUasActiveSubscriberStaticsEntry':zxUasActiveSubscriberStaticsEntry,'zxUasActiveSubscriberNum':zxUasActiveSubscriberNum,'zxUasMaxSubscriberOnlineCount':zxUasMaxSubscriberOnlineCount,'zxUasMaxSubscriberOnlineClear':zxUasMaxSubscriberOnlineClear,'zxUasMaxSubscriberOnlineTime':zxUasMaxSubscriberOnlineTime,'zxUasTraps':zxUasTraps})