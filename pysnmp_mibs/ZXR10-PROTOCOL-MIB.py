_L='zxr10tcpConnRemPort'
_K='zxr10tcpConnRemAddress'
_J='zxr10tcpConnLocalPort'
_I='zxr10tcpConnLocalAddress'
_H='zxr10tcpConnVrfVpnName'
_G='zxr10ipVrfAddr'
_F='zxr10ipVrfVpnName'
_E='DisplayString'
_D='Integer32'
_C='ZXR10-PROTOCOL-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_Zxr10_ObjectIdentity=ObjectIdentity
zxr10=_Zxr10_ObjectIdentity((1,3,6,1,4,1,3902,3))
_Zxr10protocol_ObjectIdentity=ObjectIdentity
zxr10protocol=_Zxr10protocol_ObjectIdentity((1,3,6,1,4,1,3902,3,101))
_Zxr10ip_ObjectIdentity=ObjectIdentity
zxr10ip=_Zxr10ip_ObjectIdentity((1,3,6,1,4,1,3902,3,101,1))
_Zxr10ipvrfaddrTable_Object=MibTable
zxr10ipvrfaddrTable=_Zxr10ipvrfaddrTable_Object((1,3,6,1,4,1,3902,3,101,1,1))
if mibBuilder.loadTexts:zxr10ipvrfaddrTable.setStatus(_A)
_Zxr10ipvrfaddrEntry_Object=MibTableRow
zxr10ipvrfaddrEntry=_Zxr10ipvrfaddrEntry_Object((1,3,6,1,4,1,3902,3,101,1,1,1))
zxr10ipvrfaddrEntry.setIndexNames((0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:zxr10ipvrfaddrEntry.setStatus(_A)
class _Zxr10ipVrfVpnName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_Zxr10ipVrfVpnName_Type.__name__=_E
_Zxr10ipVrfVpnName_Object=MibTableColumn
zxr10ipVrfVpnName=_Zxr10ipVrfVpnName_Object((1,3,6,1,4,1,3902,3,101,1,1,1,1),_Zxr10ipVrfVpnName_Type())
zxr10ipVrfVpnName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10ipVrfVpnName.setStatus(_A)
_Zxr10ipVrfAddr_Type=IpAddress
_Zxr10ipVrfAddr_Object=MibTableColumn
zxr10ipVrfAddr=_Zxr10ipVrfAddr_Object((1,3,6,1,4,1,3902,3,101,1,1,1,2),_Zxr10ipVrfAddr_Type())
zxr10ipVrfAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10ipVrfAddr.setStatus(_A)
_Zxr10ipVrfNetMask_Type=IpAddress
_Zxr10ipVrfNetMask_Object=MibTableColumn
zxr10ipVrfNetMask=_Zxr10ipVrfNetMask_Object((1,3,6,1,4,1,3902,3,101,1,1,1,3),_Zxr10ipVrfNetMask_Type())
zxr10ipVrfNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10ipVrfNetMask.setStatus(_A)
_Zxr10ipVrfIfIndex_Type=Integer32
_Zxr10ipVrfIfIndex_Object=MibTableColumn
zxr10ipVrfIfIndex=_Zxr10ipVrfIfIndex_Object((1,3,6,1,4,1,3902,3,101,1,1,1,4),_Zxr10ipVrfIfIndex_Type())
zxr10ipVrfIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10ipVrfIfIndex.setStatus(_A)
_Zxr10ipVrfBcastAddr_Type=Integer32
_Zxr10ipVrfBcastAddr_Object=MibTableColumn
zxr10ipVrfBcastAddr=_Zxr10ipVrfBcastAddr_Object((1,3,6,1,4,1,3902,3,101,1,1,1,5),_Zxr10ipVrfBcastAddr_Type())
zxr10ipVrfBcastAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10ipVrfBcastAddr.setStatus(_A)
class _Zxr10ipVrfReasmMaxSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Zxr10ipVrfReasmMaxSize_Type.__name__=_D
_Zxr10ipVrfReasmMaxSize_Object=MibTableColumn
zxr10ipVrfReasmMaxSize=_Zxr10ipVrfReasmMaxSize_Object((1,3,6,1,4,1,3902,3,101,1,1,1,6),_Zxr10ipVrfReasmMaxSize_Type())
zxr10ipVrfReasmMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10ipVrfReasmMaxSize.setStatus(_A)
_Zxr10tcp_ObjectIdentity=ObjectIdentity
zxr10tcp=_Zxr10tcp_ObjectIdentity((1,3,6,1,4,1,3902,3,101,2))
_Zxr10tcpConnTable_Object=MibTable
zxr10tcpConnTable=_Zxr10tcpConnTable_Object((1,3,6,1,4,1,3902,3,101,2,1))
if mibBuilder.loadTexts:zxr10tcpConnTable.setStatus(_A)
_Zxr10tcpconnEntry_Object=MibTableRow
zxr10tcpconnEntry=_Zxr10tcpconnEntry_Object((1,3,6,1,4,1,3902,3,101,2,1,1))
zxr10tcpconnEntry.setIndexNames((0,_C,_H),(0,_C,_I),(0,_C,_J),(0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:zxr10tcpconnEntry.setStatus(_A)
class _Zxr10tcpConnVrfVpnName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_Zxr10tcpConnVrfVpnName_Type.__name__=_E
_Zxr10tcpConnVrfVpnName_Object=MibTableColumn
zxr10tcpConnVrfVpnName=_Zxr10tcpConnVrfVpnName_Object((1,3,6,1,4,1,3902,3,101,2,1,1,1),_Zxr10tcpConnVrfVpnName_Type())
zxr10tcpConnVrfVpnName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10tcpConnVrfVpnName.setStatus(_A)
class _Zxr10tcpConnState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('closed',1),('listen',2),('synSent',3),('synReceived',4),('established',5),('finWait1',6),('finWait2',7),('closeWait',8),('lastAck',9),('closing',10),('timeWait',11),('deleteTCB',12)))
_Zxr10tcpConnState_Type.__name__=_D
_Zxr10tcpConnState_Object=MibTableColumn
zxr10tcpConnState=_Zxr10tcpConnState_Object((1,3,6,1,4,1,3902,3,101,2,1,1,2),_Zxr10tcpConnState_Type())
zxr10tcpConnState.setMaxAccess('read-write')
if mibBuilder.loadTexts:zxr10tcpConnState.setStatus(_A)
_Zxr10tcpConnLocalAddress_Type=IpAddress
_Zxr10tcpConnLocalAddress_Object=MibTableColumn
zxr10tcpConnLocalAddress=_Zxr10tcpConnLocalAddress_Object((1,3,6,1,4,1,3902,3,101,2,1,1,3),_Zxr10tcpConnLocalAddress_Type())
zxr10tcpConnLocalAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10tcpConnLocalAddress.setStatus(_A)
class _Zxr10tcpConnLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Zxr10tcpConnLocalPort_Type.__name__=_D
_Zxr10tcpConnLocalPort_Object=MibTableColumn
zxr10tcpConnLocalPort=_Zxr10tcpConnLocalPort_Object((1,3,6,1,4,1,3902,3,101,2,1,1,4),_Zxr10tcpConnLocalPort_Type())
zxr10tcpConnLocalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10tcpConnLocalPort.setStatus(_A)
_Zxr10tcpConnRemAddress_Type=IpAddress
_Zxr10tcpConnRemAddress_Object=MibTableColumn
zxr10tcpConnRemAddress=_Zxr10tcpConnRemAddress_Object((1,3,6,1,4,1,3902,3,101,2,1,1,5),_Zxr10tcpConnRemAddress_Type())
zxr10tcpConnRemAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10tcpConnRemAddress.setStatus(_A)
class _Zxr10tcpConnRemPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Zxr10tcpConnRemPort_Type.__name__=_D
_Zxr10tcpConnRemPort_Object=MibTableColumn
zxr10tcpConnRemPort=_Zxr10tcpConnRemPort_Object((1,3,6,1,4,1,3902,3,101,2,1,1,6),_Zxr10tcpConnRemPort_Type())
zxr10tcpConnRemPort.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10tcpConnRemPort.setStatus(_A)
mibBuilder.exportSymbols(_C,**{_E:DisplayString,'zte':zte,'zxr10':zxr10,'zxr10protocol':zxr10protocol,'zxr10ip':zxr10ip,'zxr10ipvrfaddrTable':zxr10ipvrfaddrTable,'zxr10ipvrfaddrEntry':zxr10ipvrfaddrEntry,_F:zxr10ipVrfVpnName,_G:zxr10ipVrfAddr,'zxr10ipVrfNetMask':zxr10ipVrfNetMask,'zxr10ipVrfIfIndex':zxr10ipVrfIfIndex,'zxr10ipVrfBcastAddr':zxr10ipVrfBcastAddr,'zxr10ipVrfReasmMaxSize':zxr10ipVrfReasmMaxSize,'zxr10tcp':zxr10tcp,'zxr10tcpConnTable':zxr10tcpConnTable,'zxr10tcpconnEntry':zxr10tcpconnEntry,_H:zxr10tcpConnVrfVpnName,'zxr10tcpConnState':zxr10tcpConnState,_I:zxr10tcpConnLocalAddress,_J:zxr10tcpConnLocalPort,_K:zxr10tcpConnRemAddress,_L:zxr10tcpConnRemPort})