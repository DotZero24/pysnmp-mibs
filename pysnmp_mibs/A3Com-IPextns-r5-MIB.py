_W='a3IPicmpGenIfIndex'
_V='a3IPx25configPort'
_U='a3IPsmdsGaIpNet'
_T='a3IParpPortIndex'
_S='a3IPforwardExtNextHop'
_R='a3IPforwardExtPolicy'
_Q='a3IPforwardExtProto'
_P='a3IPforwardExtDest'
_O='a3IPaddrConfigAddr'
_N='a3IPaddrConfigPort'
_M='noProxy'
_L='ethernet'
_K='a3IPntmNetAddress'
_J='a3IPntmIfIndex'
_I='deprecated'
_H='other'
_G='disabled'
_F='enabled'
_E='read-only'
_D='A3Com-IPextns-r5-MIB'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class SMDSAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class RowStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('active',1),('notInService',2),('notReady',3),('createAndGo',4),('createAndWait',5),('destroy',6)))
_A3Com_ObjectIdentity=ObjectIdentity
a3Com=_A3Com_ObjectIdentity((1,3,6,1,4,1,43))
_BrouterMIB_ObjectIdentity=ObjectIdentity
brouterMIB=_BrouterMIB_ObjectIdentity((1,3,6,1,4,1,43,2))
_A3ComIPextns_ObjectIdentity=ObjectIdentity
a3ComIPextns=_A3ComIPextns_ObjectIdentity((1,3,6,1,4,1,43,2,6))
class _A3IPextMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('multipleNet',1),('singleNet',2)))
_A3IPextMode_Type.__name__=_C
_A3IPextMode_Object=MibScalar
a3IPextMode=_A3IPextMode_Object((1,3,6,1,4,1,43,2,6,1),_A3IPextMode_Type())
a3IPextMode.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPextMode.setStatus(_A)
class _A3IPextFlushCtl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('flushRoutes',2),('flushARP',3)))
_A3IPextFlushCtl_Type.__name__=_C
_A3IPextFlushCtl_Object=MibScalar
a3IPextFlushCtl=_A3IPextFlushCtl_Object((1,3,6,1,4,1,43,2,6,2),_A3IPextFlushCtl_Type())
a3IPextFlushCtl.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPextFlushCtl.setStatus(_A)
class _A3IPextRelaySrcRteCtl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('relay',1),('discard',2)))
_A3IPextRelaySrcRteCtl_Type.__name__=_C
_A3IPextRelaySrcRteCtl_Object=MibScalar
a3IPextRelaySrcRteCtl=_A3IPextRelaySrcRteCtl_Object((1,3,6,1,4,1,43,2,6,3),_A3IPextRelaySrcRteCtl_Type())
a3IPextRelaySrcRteCtl.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPextRelaySrcRteCtl.setStatus(_A)
class _A3IPextSplitLoadCtl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('split',1),('noSplit',2)))
_A3IPextSplitLoadCtl_Type.__name__=_C
_A3IPextSplitLoadCtl_Object=MibScalar
a3IPextSplitLoadCtl=_A3IPextSplitLoadCtl_Object((1,3,6,1,4,1,43,2,6,4),_A3IPextSplitLoadCtl_Type())
a3IPextSplitLoadCtl.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPextSplitLoadCtl.setStatus(_A)
class _A3IPicmpInfoCtl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('info',1),('noInfo',2)))
_A3IPicmpInfoCtl_Type.__name__=_C
_A3IPicmpInfoCtl_Object=MibScalar
a3IPicmpInfoCtl=_A3IPicmpInfoCtl_Object((1,3,6,1,4,1,43,2,6,5),_A3IPicmpInfoCtl_Type())
a3IPicmpInfoCtl.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPicmpInfoCtl.setStatus(_A)
class _A3IPicmpMaskCtl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mask',1),('noMask',2)))
_A3IPicmpMaskCtl_Type.__name__=_C
_A3IPicmpMaskCtl_Object=MibScalar
a3IPicmpMaskCtl=_A3IPicmpMaskCtl_Object((1,3,6,1,4,1,43,2,6,6),_A3IPicmpMaskCtl_Type())
a3IPicmpMaskCtl.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPicmpMaskCtl.setStatus(_A)
_A3IPntmExtTable_Object=MibTable
a3IPntmExtTable=_A3IPntmExtTable_Object((1,3,6,1,4,1,43,2,6,7))
if mibBuilder.loadTexts:a3IPntmExtTable.setStatus(_A)
_A3IPntmExtEntry_Object=MibTableRow
a3IPntmExtEntry=_A3IPntmExtEntry_Object((1,3,6,1,4,1,43,2,6,7,1))
a3IPntmExtEntry.setIndexNames((0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:a3IPntmExtEntry.setStatus(_A)
_A3IPntmIfIndex_Type=Integer32
_A3IPntmIfIndex_Object=MibTableColumn
a3IPntmIfIndex=_A3IPntmIfIndex_Object((1,3,6,1,4,1,43,2,6,7,1,1),_A3IPntmIfIndex_Type())
a3IPntmIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:a3IPntmIfIndex.setStatus(_A)
_A3IPntmNetAddress_Type=IpAddress
_A3IPntmNetAddress_Object=MibTableColumn
a3IPntmNetAddress=_A3IPntmNetAddress_Object((1,3,6,1,4,1,43,2,6,7,1,2),_A3IPntmNetAddress_Type())
a3IPntmNetAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:a3IPntmNetAddress.setStatus(_A)
class _A3IPntmHdrFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_L,2),('ieee',3),('snap',4)))
_A3IPntmHdrFormat_Type.__name__=_C
_A3IPntmHdrFormat_Object=MibTableColumn
a3IPntmHdrFormat=_A3IPntmHdrFormat_Object((1,3,6,1,4,1,43,2,6,7,1,3),_A3IPntmHdrFormat_Type())
a3IPntmHdrFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPntmHdrFormat.setStatus(_A)
class _A3IPntmProxyArp_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('proxy',1),(_M,2)))
_A3IPntmProxyArp_Type.__name__=_C
_A3IPntmProxyArp_Object=MibTableColumn
a3IPntmProxyArp=_A3IPntmProxyArp_Object((1,3,6,1,4,1,43,2,6,7,1,4),_A3IPntmProxyArp_Type())
a3IPntmProxyArp.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPntmProxyArp.setStatus(_A)
_A3IPaddrConfigTable_Object=MibTable
a3IPaddrConfigTable=_A3IPaddrConfigTable_Object((1,3,6,1,4,1,43,2,6,8))
if mibBuilder.loadTexts:a3IPaddrConfigTable.setStatus(_A)
_A3IPaddrConfigEntry_Object=MibTableRow
a3IPaddrConfigEntry=_A3IPaddrConfigEntry_Object((1,3,6,1,4,1,43,2,6,8,1))
a3IPaddrConfigEntry.setIndexNames((0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:a3IPaddrConfigEntry.setStatus(_A)
_A3IPaddrConfigPort_Type=Integer32
_A3IPaddrConfigPort_Object=MibTableColumn
a3IPaddrConfigPort=_A3IPaddrConfigPort_Object((1,3,6,1,4,1,43,2,6,8,1,1),_A3IPaddrConfigPort_Type())
a3IPaddrConfigPort.setMaxAccess(_E)
if mibBuilder.loadTexts:a3IPaddrConfigPort.setStatus(_A)
_A3IPaddrConfigAddr_Type=IpAddress
_A3IPaddrConfigAddr_Object=MibTableColumn
a3IPaddrConfigAddr=_A3IPaddrConfigAddr_Object((1,3,6,1,4,1,43,2,6,8,1,2),_A3IPaddrConfigAddr_Type())
a3IPaddrConfigAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:a3IPaddrConfigAddr.setStatus(_A)
class _A3IPaddrConfigType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('secondary',2)))
_A3IPaddrConfigType_Type.__name__=_C
_A3IPaddrConfigType_Object=MibTableColumn
a3IPaddrConfigType=_A3IPaddrConfigType_Object((1,3,6,1,4,1,43,2,6,8,1,3),_A3IPaddrConfigType_Type())
a3IPaddrConfigType.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPaddrConfigType.setStatus(_A)
_A3IPaddrConfigNetMask_Type=IpAddress
_A3IPaddrConfigNetMask_Object=MibTableColumn
a3IPaddrConfigNetMask=_A3IPaddrConfigNetMask_Object((1,3,6,1,4,1,43,2,6,8,1,4),_A3IPaddrConfigNetMask_Type())
a3IPaddrConfigNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPaddrConfigNetMask.setStatus(_A)
class _A3IPaddrConfigBcastAddr_Type(Integer32):defaultValue=1
_A3IPaddrConfigBcastAddr_Type.__name__=_C
_A3IPaddrConfigBcastAddr_Object=MibTableColumn
a3IPaddrConfigBcastAddr=_A3IPaddrConfigBcastAddr_Object((1,3,6,1,4,1,43,2,6,8,1,5),_A3IPaddrConfigBcastAddr_Type())
a3IPaddrConfigBcastAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPaddrConfigBcastAddr.setStatus(_A)
class _A3IPaddrConfigMtu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(68,32767))
_A3IPaddrConfigMtu_Type.__name__=_C
_A3IPaddrConfigMtu_Object=MibTableColumn
a3IPaddrConfigMtu=_A3IPaddrConfigMtu_Object((1,3,6,1,4,1,43,2,6,8,1,6),_A3IPaddrConfigMtu_Type())
a3IPaddrConfigMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPaddrConfigMtu.setStatus(_A)
_A3IPaddrConfigStatus_Type=RowStatus
_A3IPaddrConfigStatus_Object=MibTableColumn
a3IPaddrConfigStatus=_A3IPaddrConfigStatus_Object((1,3,6,1,4,1,43,2,6,8,1,7),_A3IPaddrConfigStatus_Type())
a3IPaddrConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPaddrConfigStatus.setStatus(_A)
_A3IPforwardExtTable_Object=MibTable
a3IPforwardExtTable=_A3IPforwardExtTable_Object((1,3,6,1,4,1,43,2,6,9))
if mibBuilder.loadTexts:a3IPforwardExtTable.setStatus(_A)
_A3IPforwardExtEntry_Object=MibTableRow
a3IPforwardExtEntry=_A3IPforwardExtEntry_Object((1,3,6,1,4,1,43,2,6,9,1))
a3IPforwardExtEntry.setIndexNames((0,_D,_P),(0,_D,_Q),(0,_D,_R),(0,_D,_S))
if mibBuilder.loadTexts:a3IPforwardExtEntry.setStatus(_A)
_A3IPforwardExtDest_Type=IpAddress
_A3IPforwardExtDest_Object=MibTableColumn
a3IPforwardExtDest=_A3IPforwardExtDest_Object((1,3,6,1,4,1,43,2,6,9,1,1),_A3IPforwardExtDest_Type())
a3IPforwardExtDest.setMaxAccess(_E)
if mibBuilder.loadTexts:a3IPforwardExtDest.setStatus(_A)
class _A3IPforwardExtProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_H,1),('local',2),('netmgmt',3),('icmp',4),('egp',5),('ggp',6),('hello',7),('rip',8),('is-is',9),('es-is',10),('ciscoIgrp',11),('bbnSpfIgp',12),('ospf',13),('bgp',14),('idpr',15)))
_A3IPforwardExtProto_Type.__name__=_C
_A3IPforwardExtProto_Object=MibTableColumn
a3IPforwardExtProto=_A3IPforwardExtProto_Object((1,3,6,1,4,1,43,2,6,9,1,2),_A3IPforwardExtProto_Type())
a3IPforwardExtProto.setMaxAccess(_E)
if mibBuilder.loadTexts:a3IPforwardExtProto.setStatus(_A)
_A3IPforwardExtPolicy_Type=Integer32
_A3IPforwardExtPolicy_Object=MibTableColumn
a3IPforwardExtPolicy=_A3IPforwardExtPolicy_Object((1,3,6,1,4,1,43,2,6,9,1,3),_A3IPforwardExtPolicy_Type())
a3IPforwardExtPolicy.setMaxAccess(_E)
if mibBuilder.loadTexts:a3IPforwardExtPolicy.setStatus(_A)
_A3IPforwardExtNextHop_Type=IpAddress
_A3IPforwardExtNextHop_Object=MibTableColumn
a3IPforwardExtNextHop=_A3IPforwardExtNextHop_Object((1,3,6,1,4,1,43,2,6,9,1,4),_A3IPforwardExtNextHop_Type())
a3IPforwardExtNextHop.setMaxAccess(_E)
if mibBuilder.loadTexts:a3IPforwardExtNextHop.setStatus(_A)
class _A3IPforwardExtOverride_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('override',1),('noOverride',2)))
_A3IPforwardExtOverride_Type.__name__=_C
_A3IPforwardExtOverride_Object=MibTableColumn
a3IPforwardExtOverride=_A3IPforwardExtOverride_Object((1,3,6,1,4,1,43,2,6,9,1,5),_A3IPforwardExtOverride_Type())
a3IPforwardExtOverride.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPforwardExtOverride.setStatus(_A)
class _A3IParpOverBlocked_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_A3IParpOverBlocked_Type.__name__=_C
_A3IParpOverBlocked_Object=MibScalar
a3IParpOverBlocked=_A3IParpOverBlocked_Object((1,3,6,1,4,1,43,2,6,10),_A3IParpOverBlocked_Type())
a3IParpOverBlocked.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IParpOverBlocked.setStatus(_A)
class _A3IPrarpClientCtl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_A3IPrarpClientCtl_Type.__name__=_C
_A3IPrarpClientCtl_Object=MibScalar
a3IPrarpClientCtl=_A3IPrarpClientCtl_Object((1,3,6,1,4,1,43,2,6,11),_A3IPrarpClientCtl_Type())
a3IPrarpClientCtl.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPrarpClientCtl.setStatus(_A)
class _A3IPrarpServerCtl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_A3IPrarpServerCtl_Type.__name__=_C
_A3IPrarpServerCtl_Object=MibScalar
a3IPrarpServerCtl=_A3IPrarpServerCtl_Object((1,3,6,1,4,1,43,2,6,12),_A3IPrarpServerCtl_Type())
a3IPrarpServerCtl.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPrarpServerCtl.setStatus(_A)
_A3IParpConfigTable_Object=MibTable
a3IParpConfigTable=_A3IParpConfigTable_Object((1,3,6,1,4,1,43,2,6,13))
if mibBuilder.loadTexts:a3IParpConfigTable.setStatus(_A)
_A3IParpConfigEntry_Object=MibTableRow
a3IParpConfigEntry=_A3IParpConfigEntry_Object((1,3,6,1,4,1,43,2,6,13,1))
a3IParpConfigEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:a3IParpConfigEntry.setStatus(_A)
_A3IParpPortIndex_Type=Integer32
_A3IParpPortIndex_Object=MibTableColumn
a3IParpPortIndex=_A3IParpPortIndex_Object((1,3,6,1,4,1,43,2,6,13,1,1),_A3IParpPortIndex_Type())
a3IParpPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:a3IParpPortIndex.setStatus(_A)
class _A3IParpProxyCtl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('proxy',1),(_M,2)))
_A3IParpProxyCtl_Type.__name__=_C
_A3IParpProxyCtl_Object=MibTableColumn
a3IParpProxyCtl=_A3IParpProxyCtl_Object((1,3,6,1,4,1,43,2,6,13,1,2),_A3IParpProxyCtl_Type())
a3IParpProxyCtl.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IParpProxyCtl.setStatus(_A)
class _A3IParpHoldTime_Type(Integer32):defaultValue=24;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_A3IParpHoldTime_Type.__name__=_C
_A3IParpHoldTime_Object=MibTableColumn
a3IParpHoldTime=_A3IParpHoldTime_Object((1,3,6,1,4,1,43,2,6,13,1,3),_A3IParpHoldTime_Type())
a3IParpHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IParpHoldTime.setStatus(_A)
class _A3IParpReqFormat_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,128,129,130,131)));namedValues=NamedValues(*((_L,1),('snap',2),('both',3),('auto',128),('ethAuto',129),('snapAuto',130),('bothAuto',131)))
_A3IParpReqFormat_Type.__name__=_C
_A3IParpReqFormat_Object=MibTableColumn
a3IParpReqFormat=_A3IParpReqFormat_Object((1,3,6,1,4,1,43,2,6,13,1,4),_A3IParpReqFormat_Type())
a3IParpReqFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IParpReqFormat.setStatus(_A)
_A3IParpRemAddr_Type=IpAddress
_A3IParpRemAddr_Object=MibTableColumn
a3IParpRemAddr=_A3IParpRemAddr_Object((1,3,6,1,4,1,43,2,6,13,1,5),_A3IParpRemAddr_Type())
a3IParpRemAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IParpRemAddr.setStatus(_A)
class _A3IParpInvCtl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_A3IParpInvCtl_Type.__name__=_C
_A3IParpInvCtl_Object=MibTableColumn
a3IParpInvCtl=_A3IParpInvCtl_Object((1,3,6,1,4,1,43,2,6,13,1,6),_A3IParpInvCtl_Type())
a3IParpInvCtl.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IParpInvCtl.setStatus(_A)
_A3IPsmdsGaTable_Object=MibTable
a3IPsmdsGaTable=_A3IPsmdsGaTable_Object((1,3,6,1,4,1,43,2,6,14))
if mibBuilder.loadTexts:a3IPsmdsGaTable.setStatus(_A)
_A3IPsmdsGaEntry_Object=MibTableRow
a3IPsmdsGaEntry=_A3IPsmdsGaEntry_Object((1,3,6,1,4,1,43,2,6,14,1))
a3IPsmdsGaEntry.setIndexNames((0,_D,_U))
if mibBuilder.loadTexts:a3IPsmdsGaEntry.setStatus(_A)
_A3IPsmdsGaIpNet_Type=IpAddress
_A3IPsmdsGaIpNet_Object=MibTableColumn
a3IPsmdsGaIpNet=_A3IPsmdsGaIpNet_Object((1,3,6,1,4,1,43,2,6,14,1,1),_A3IPsmdsGaIpNet_Type())
a3IPsmdsGaIpNet.setMaxAccess(_E)
if mibBuilder.loadTexts:a3IPsmdsGaIpNet.setStatus(_A)
_A3IPsmdsGa_Type=SMDSAddress
_A3IPsmdsGa_Object=MibTableColumn
a3IPsmdsGa=_A3IPsmdsGa_Object((1,3,6,1,4,1,43,2,6,14,1,2),_A3IPsmdsGa_Type())
a3IPsmdsGa.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPsmdsGa.setStatus(_A)
_A3IPsmdsGaStatus_Type=RowStatus
_A3IPsmdsGaStatus_Object=MibTableColumn
a3IPsmdsGaStatus=_A3IPsmdsGaStatus_Object((1,3,6,1,4,1,43,2,6,14,1,3),_A3IPsmdsGaStatus_Type())
a3IPsmdsGaStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPsmdsGaStatus.setStatus(_A)
_A3IPx25configTable_Object=MibTable
a3IPx25configTable=_A3IPx25configTable_Object((1,3,6,1,4,1,43,2,6,15))
if mibBuilder.loadTexts:a3IPx25configTable.setStatus(_A)
_A3IPx25configEntry_Object=MibTableRow
a3IPx25configEntry=_A3IPx25configEntry_Object((1,3,6,1,4,1,43,2,6,15,1))
a3IPx25configEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:a3IPx25configEntry.setStatus(_A)
_A3IPx25configPort_Type=Integer32
_A3IPx25configPort_Object=MibTableColumn
a3IPx25configPort=_A3IPx25configPort_Object((1,3,6,1,4,1,43,2,6,15,1,1),_A3IPx25configPort_Type())
a3IPx25configPort.setMaxAccess(_E)
if mibBuilder.loadTexts:a3IPx25configPort.setStatus(_A)
class _A3IPx25configPID_Type(Integer32):defaultValue=204;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_A3IPx25configPID_Type.__name__=_C
_A3IPx25configPID_Object=MibTableColumn
a3IPx25configPID=_A3IPx25configPID_Object((1,3,6,1,4,1,43,2,6,15,1,2),_A3IPx25configPID_Type())
a3IPx25configPID.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPx25configPID.setStatus(_A)
class _A3IPx25configQueueSize_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_A3IPx25configQueueSize_Type.__name__=_C
_A3IPx25configQueueSize_Object=MibTableColumn
a3IPx25configQueueSize=_A3IPx25configQueueSize_Object((1,3,6,1,4,1,43,2,6,15,1,3),_A3IPx25configQueueSize_Type())
a3IPx25configQueueSize.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPx25configQueueSize.setStatus(_I)
class _A3IPx25configVClimit_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_A3IPx25configVClimit_Type.__name__=_C
_A3IPx25configVClimit_Object=MibTableColumn
a3IPx25configVClimit=_A3IPx25configVClimit_Object((1,3,6,1,4,1,43,2,6,15,1,4),_A3IPx25configVClimit_Type())
a3IPx25configVClimit.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPx25configVClimit.setStatus(_I)
class _A3IPx25configVCtimer_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_A3IPx25configVCtimer_Type.__name__=_C
_A3IPx25configVCtimer_Object=MibTableColumn
a3IPx25configVCtimer=_A3IPx25configVCtimer_Object((1,3,6,1,4,1,43,2,6,15,1,5),_A3IPx25configVCtimer_Type())
a3IPx25configVCtimer.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPx25configVCtimer.setStatus(_I)
class _A3IPx25configProfID_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_A3IPx25configProfID_Type.__name__=_C
_A3IPx25configProfID_Object=MibTableColumn
a3IPx25configProfID=_A3IPx25configProfID_Object((1,3,6,1,4,1,43,2,6,15,1,6),_A3IPx25configProfID_Type())
a3IPx25configProfID.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPx25configProfID.setStatus(_A)
class _A3IPqueuePriority_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('high',1),('medium',2),('low',3),('default',4),('unknown',5)))
_A3IPqueuePriority_Type.__name__=_C
_A3IPqueuePriority_Object=MibScalar
a3IPqueuePriority=_A3IPqueuePriority_Object((1,3,6,1,4,1,43,2,6,16),_A3IPqueuePriority_Type())
a3IPqueuePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPqueuePriority.setStatus(_A)
class _A3IPfwdSubnetBcast_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fwdSubnetBcast',1),('noFwdSubnetBcast',2)))
_A3IPfwdSubnetBcast_Type.__name__=_C
_A3IPfwdSubnetBcast_Object=MibScalar
a3IPfwdSubnetBcast=_A3IPfwdSubnetBcast_Object((1,3,6,1,4,1,43,2,6,17),_A3IPfwdSubnetBcast_Type())
a3IPfwdSubnetBcast.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPfwdSubnetBcast.setStatus(_A)
_A3IPicmpGenTable_Object=MibTable
a3IPicmpGenTable=_A3IPicmpGenTable_Object((1,3,6,1,4,1,43,2,6,18))
if mibBuilder.loadTexts:a3IPicmpGenTable.setStatus(_A)
_A3IPicmpGenEntry_Object=MibTableRow
a3IPicmpGenEntry=_A3IPicmpGenEntry_Object((1,3,6,1,4,1,43,2,6,18,1))
a3IPicmpGenEntry.setIndexNames((0,_D,_W))
if mibBuilder.loadTexts:a3IPicmpGenEntry.setStatus(_A)
_A3IPicmpGenIfIndex_Type=Integer32
_A3IPicmpGenIfIndex_Object=MibTableColumn
a3IPicmpGenIfIndex=_A3IPicmpGenIfIndex_Object((1,3,6,1,4,1,43,2,6,18,1,1),_A3IPicmpGenIfIndex_Type())
a3IPicmpGenIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:a3IPicmpGenIfIndex.setStatus(_A)
class _A3IPicmpGenRedirect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('redirect',1),('noRedirect',2)))
_A3IPicmpGenRedirect_Type.__name__=_C
_A3IPicmpGenRedirect_Object=MibTableColumn
a3IPicmpGenRedirect=_A3IPicmpGenRedirect_Object((1,3,6,1,4,1,43,2,6,18,1,2),_A3IPicmpGenRedirect_Type())
a3IPicmpGenRedirect.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPicmpGenRedirect.setStatus(_A)
class _A3IPicmpGenDestUnreach_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('destUnreachable',1),('noDestUnreachable',2)))
_A3IPicmpGenDestUnreach_Type.__name__=_C
_A3IPicmpGenDestUnreach_Object=MibTableColumn
a3IPicmpGenDestUnreach=_A3IPicmpGenDestUnreach_Object((1,3,6,1,4,1,43,2,6,18,1,3),_A3IPicmpGenDestUnreach_Type())
a3IPicmpGenDestUnreach.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPicmpGenDestUnreach.setStatus(_A)
class _A3IPicmpGenTimeExceed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('timeExceed',1),('noTimeExceed',2)))
_A3IPicmpGenTimeExceed_Type.__name__=_C
_A3IPicmpGenTimeExceed_Object=MibTableColumn
a3IPicmpGenTimeExceed=_A3IPicmpGenTimeExceed_Object((1,3,6,1,4,1,43,2,6,18,1,4),_A3IPicmpGenTimeExceed_Type())
a3IPicmpGenTimeExceed.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPicmpGenTimeExceed.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'SMDSAddress':SMDSAddress,'RowStatus':RowStatus,'a3Com':a3Com,'brouterMIB':brouterMIB,'a3ComIPextns':a3ComIPextns,'a3IPextMode':a3IPextMode,'a3IPextFlushCtl':a3IPextFlushCtl,'a3IPextRelaySrcRteCtl':a3IPextRelaySrcRteCtl,'a3IPextSplitLoadCtl':a3IPextSplitLoadCtl,'a3IPicmpInfoCtl':a3IPicmpInfoCtl,'a3IPicmpMaskCtl':a3IPicmpMaskCtl,'a3IPntmExtTable':a3IPntmExtTable,'a3IPntmExtEntry':a3IPntmExtEntry,_J:a3IPntmIfIndex,_K:a3IPntmNetAddress,'a3IPntmHdrFormat':a3IPntmHdrFormat,'a3IPntmProxyArp':a3IPntmProxyArp,'a3IPaddrConfigTable':a3IPaddrConfigTable,'a3IPaddrConfigEntry':a3IPaddrConfigEntry,_N:a3IPaddrConfigPort,_O:a3IPaddrConfigAddr,'a3IPaddrConfigType':a3IPaddrConfigType,'a3IPaddrConfigNetMask':a3IPaddrConfigNetMask,'a3IPaddrConfigBcastAddr':a3IPaddrConfigBcastAddr,'a3IPaddrConfigMtu':a3IPaddrConfigMtu,'a3IPaddrConfigStatus':a3IPaddrConfigStatus,'a3IPforwardExtTable':a3IPforwardExtTable,'a3IPforwardExtEntry':a3IPforwardExtEntry,_P:a3IPforwardExtDest,_Q:a3IPforwardExtProto,_R:a3IPforwardExtPolicy,_S:a3IPforwardExtNextHop,'a3IPforwardExtOverride':a3IPforwardExtOverride,'a3IParpOverBlocked':a3IParpOverBlocked,'a3IPrarpClientCtl':a3IPrarpClientCtl,'a3IPrarpServerCtl':a3IPrarpServerCtl,'a3IParpConfigTable':a3IParpConfigTable,'a3IParpConfigEntry':a3IParpConfigEntry,_T:a3IParpPortIndex,'a3IParpProxyCtl':a3IParpProxyCtl,'a3IParpHoldTime':a3IParpHoldTime,'a3IParpReqFormat':a3IParpReqFormat,'a3IParpRemAddr':a3IParpRemAddr,'a3IParpInvCtl':a3IParpInvCtl,'a3IPsmdsGaTable':a3IPsmdsGaTable,'a3IPsmdsGaEntry':a3IPsmdsGaEntry,_U:a3IPsmdsGaIpNet,'a3IPsmdsGa':a3IPsmdsGa,'a3IPsmdsGaStatus':a3IPsmdsGaStatus,'a3IPx25configTable':a3IPx25configTable,'a3IPx25configEntry':a3IPx25configEntry,_V:a3IPx25configPort,'a3IPx25configPID':a3IPx25configPID,'a3IPx25configQueueSize':a3IPx25configQueueSize,'a3IPx25configVClimit':a3IPx25configVClimit,'a3IPx25configVCtimer':a3IPx25configVCtimer,'a3IPx25configProfID':a3IPx25configProfID,'a3IPqueuePriority':a3IPqueuePriority,'a3IPfwdSubnetBcast':a3IPfwdSubnetBcast,'a3IPicmpGenTable':a3IPicmpGenTable,'a3IPicmpGenEntry':a3IPicmpGenEntry,_W:a3IPicmpGenIfIndex,'a3IPicmpGenRedirect':a3IPicmpGenRedirect,'a3IPicmpGenDestUnreach':a3IPicmpGenDestUnreach,'a3IPicmpGenTimeExceed':a3IPicmpGenTimeExceed})