_Y='x25AgentIfIndex'
_X='x25AgentLogicAddr'
_W='x25RouteConfX121Addr'
_V='x25VcStatNum'
_U='x25VcStatIfIndex'
_T='interface'
_S='x25PvcConfNum'
_R='x25PvcConfIfIndex'
_Q='compressedIp'
_P='x25MapConfAddr'
_O='x25MapConfMode'
_N='x25MapConfIfIndex'
_M='lapbIfIndex'
_L='modulo128'
_K='modulo8'
_J='x25ConfIfIndex'
_I='Unsigned32'
_H='DisplayString'
_G='OctetString'
_F='MAIPU-X25-MIB'
_E='read-create'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mpMgmt,=mibBuilder.importSymbols('MAIPU-SMI','mpMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','RowStatus','TextualConvention')
mpX25Mib=ModuleIdentity((1,3,6,1,4,1,5651,3,7))
_X25IfMib_ObjectIdentity=ObjectIdentity
x25IfMib=_X25IfMib_ObjectIdentity((1,3,6,1,4,1,5651,3,7,1))
_X25ConfTable_Object=MibTable
x25ConfTable=_X25ConfTable_Object((1,3,6,1,4,1,5651,3,7,1,1))
if mibBuilder.loadTexts:x25ConfTable.setStatus(_A)
_X25ConfEntry_Object=MibTableRow
x25ConfEntry=_X25ConfEntry_Object((1,3,6,1,4,1,5651,3,7,1,1,1))
x25ConfEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:x25ConfEntry.setStatus(_A)
_X25ConfIfIndex_Type=Integer32
_X25ConfIfIndex_Object=MibTableColumn
x25ConfIfIndex=_X25ConfIfIndex_Object((1,3,6,1,4,1,5651,3,7,1,1,1,1),_X25ConfIfIndex_Type())
x25ConfIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:x25ConfIfIndex.setStatus(_A)
class _X25ConfMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dte',1),('dce',2)))
_X25ConfMode_Type.__name__=_B
_X25ConfMode_Object=MibTableColumn
x25ConfMode=_X25ConfMode_Object((1,3,6,1,4,1,5651,3,7,1,1,1,2),_X25ConfMode_Type())
x25ConfMode.setMaxAccess(_D)
if mibBuilder.loadTexts:x25ConfMode.setStatus(_A)
class _X25ConfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('r0',0),('r1',1),('r23',2)))
_X25ConfState_Type.__name__=_B
_X25ConfState_Object=MibScalar
x25ConfState=_X25ConfState_Object((1,3,6,1,4,1,5651,3,7,1,1,1,3),_X25ConfState_Type())
x25ConfState.setMaxAccess(_C)
if mibBuilder.loadTexts:x25ConfState.setStatus(_A)
class _X25ConfAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,14))
_X25ConfAddress_Type.__name__=_G
_X25ConfAddress_Object=MibTableColumn
x25ConfAddress=_X25ConfAddress_Object((1,3,6,1,4,1,5651,3,7,1,1,1,4),_X25ConfAddress_Type())
x25ConfAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:x25ConfAddress.setStatus(_A)
class _X25ConfHtc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_X25ConfHtc_Type.__name__=_B
_X25ConfHtc_Object=MibTableColumn
x25ConfHtc=_X25ConfHtc_Object((1,3,6,1,4,1,5651,3,7,1,1,1,5),_X25ConfHtc_Type())
x25ConfHtc.setMaxAccess(_D)
if mibBuilder.loadTexts:x25ConfHtc.setStatus(_A)
class _X25ConfLtc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_X25ConfLtc_Type.__name__=_B
_X25ConfLtc_Object=MibTableColumn
x25ConfLtc=_X25ConfLtc_Object((1,3,6,1,4,1,5651,3,7,1,1,1,6),_X25ConfLtc_Type())
x25ConfLtc.setMaxAccess(_D)
if mibBuilder.loadTexts:x25ConfLtc.setStatus(_A)
class _X25ConfHoldQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_X25ConfHoldQueue_Type.__name__=_B
_X25ConfHoldQueue_Object=MibTableColumn
x25ConfHoldQueue=_X25ConfHoldQueue_Object((1,3,6,1,4,1,5651,3,7,1,1,1,7),_X25ConfHoldQueue_Type())
x25ConfHoldQueue.setMaxAccess(_D)
if mibBuilder.loadTexts:x25ConfHoldQueue.setStatus(_A)
class _X25ConfIdle_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_X25ConfIdle_Type.__name__=_B
_X25ConfIdle_Object=MibTableColumn
x25ConfIdle=_X25ConfIdle_Object((1,3,6,1,4,1,5651,3,7,1,1,1,8),_X25ConfIdle_Type())
x25ConfIdle.setMaxAccess(_D)
if mibBuilder.loadTexts:x25ConfIdle.setStatus(_A)
class _X25ConfIps_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,4096))
_X25ConfIps_Type.__name__=_B
_X25ConfIps_Object=MibTableColumn
x25ConfIps=_X25ConfIps_Object((1,3,6,1,4,1,5651,3,7,1,1,1,9),_X25ConfIps_Type())
x25ConfIps.setMaxAccess(_D)
if mibBuilder.loadTexts:x25ConfIps.setStatus(_A)
class _X25ConfOps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,4096))
_X25ConfOps_Type.__name__=_B
_X25ConfOps_Object=MibTableColumn
x25ConfOps=_X25ConfOps_Object((1,3,6,1,4,1,5651,3,7,1,1,1,10),_X25ConfOps_Type())
x25ConfOps.setMaxAccess(_D)
if mibBuilder.loadTexts:x25ConfOps.setStatus(_A)
class _X25ConfModulo_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_X25ConfModulo_Type.__name__=_B
_X25ConfModulo_Object=MibTableColumn
x25ConfModulo=_X25ConfModulo_Object((1,3,6,1,4,1,5651,3,7,1,1,1,11),_X25ConfModulo_Type())
x25ConfModulo.setMaxAccess(_D)
if mibBuilder.loadTexts:x25ConfModulo.setStatus(_A)
class _X25ConfNvc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_X25ConfNvc_Type.__name__=_B
_X25ConfNvc_Object=MibTableColumn
x25ConfNvc=_X25ConfNvc_Object((1,3,6,1,4,1,5651,3,7,1,1,1,12),_X25ConfNvc_Type())
x25ConfNvc.setMaxAccess(_D)
if mibBuilder.loadTexts:x25ConfNvc.setStatus(_A)
class _X25ConfWin_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_X25ConfWin_Type.__name__=_B
_X25ConfWin_Object=MibTableColumn
x25ConfWin=_X25ConfWin_Object((1,3,6,1,4,1,5651,3,7,1,1,1,13),_X25ConfWin_Type())
x25ConfWin.setMaxAccess(_D)
if mibBuilder.loadTexts:x25ConfWin.setStatus(_A)
class _X25ConfWout_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_X25ConfWout_Type.__name__=_B
_X25ConfWout_Object=MibTableColumn
x25ConfWout=_X25ConfWout_Object((1,3,6,1,4,1,5651,3,7,1,1,1,14),_X25ConfWout_Type())
x25ConfWout.setMaxAccess(_D)
if mibBuilder.loadTexts:x25ConfWout.setStatus(_A)
class _X25ConfT20_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_X25ConfT20_Type.__name__=_B
_X25ConfT20_Object=MibTableColumn
x25ConfT20=_X25ConfT20_Object((1,3,6,1,4,1,5651,3,7,1,1,1,15),_X25ConfT20_Type())
x25ConfT20.setMaxAccess(_D)
if mibBuilder.loadTexts:x25ConfT20.setStatus(_A)
class _X25ConfT21_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_X25ConfT21_Type.__name__=_B
_X25ConfT21_Object=MibTableColumn
x25ConfT21=_X25ConfT21_Object((1,3,6,1,4,1,5651,3,7,1,1,1,16),_X25ConfT21_Type())
x25ConfT21.setMaxAccess(_D)
if mibBuilder.loadTexts:x25ConfT21.setStatus(_A)
class _X25ConfT22_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_X25ConfT22_Type.__name__=_B
_X25ConfT22_Object=MibTableColumn
x25ConfT22=_X25ConfT22_Object((1,3,6,1,4,1,5651,3,7,1,1,1,17),_X25ConfT22_Type())
x25ConfT22.setMaxAccess(_D)
if mibBuilder.loadTexts:x25ConfT22.setStatus(_A)
class _X25ConfT23_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_X25ConfT23_Type.__name__=_B
_X25ConfT23_Object=MibTableColumn
x25ConfT23=_X25ConfT23_Object((1,3,6,1,4,1,5651,3,7,1,1,1,18),_X25ConfT23_Type())
x25ConfT23.setMaxAccess(_D)
if mibBuilder.loadTexts:x25ConfT23.setStatus(_A)
class _X25ConfHic_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_X25ConfHic_Type.__name__=_B
_X25ConfHic_Object=MibTableColumn
x25ConfHic=_X25ConfHic_Object((1,3,6,1,4,1,5651,3,7,1,1,1,19),_X25ConfHic_Type())
x25ConfHic.setMaxAccess(_D)
if mibBuilder.loadTexts:x25ConfHic.setStatus(_A)
class _X25ConfHoc_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_X25ConfHoc_Type.__name__=_B
_X25ConfHoc_Object=MibTableColumn
x25ConfHoc=_X25ConfHoc_Object((1,3,6,1,4,1,5651,3,7,1,1,1,20),_X25ConfHoc_Type())
x25ConfHoc.setMaxAccess(_D)
if mibBuilder.loadTexts:x25ConfHoc.setStatus(_A)
_LapbConfTable_Object=MibTable
lapbConfTable=_LapbConfTable_Object((1,3,6,1,4,1,5651,3,7,1,3))
if mibBuilder.loadTexts:lapbConfTable.setStatus(_A)
_LapbConfEntry_Object=MibTableRow
lapbConfEntry=_LapbConfEntry_Object((1,3,6,1,4,1,5651,3,7,1,3,1))
lapbConfEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:lapbConfEntry.setStatus(_A)
_LapbIfIndex_Type=Integer32
_LapbIfIndex_Object=MibTableColumn
lapbIfIndex=_LapbIfIndex_Object((1,3,6,1,4,1,5651,3,7,1,3,1,1),_LapbIfIndex_Type())
lapbIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:lapbIfIndex.setStatus(_A)
class _LapbMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dte',1),('dce',2)))
_LapbMode_Type.__name__=_B
_LapbMode_Object=MibTableColumn
lapbMode=_LapbMode_Object((1,3,6,1,4,1,5651,3,7,1,3,1,2),_LapbMode_Type())
lapbMode.setMaxAccess(_D)
if mibBuilder.loadTexts:lapbMode.setStatus(_A)
class _LapbState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('init',0),('dm_sent',1),('sabm_sent',2),('abm',3),('wait_sabm',4),('wait_ua',5),('disc_sent',6),('disconnected',7),('init_start',8)))
_LapbState_Type.__name__=_B
_LapbState_Object=MibTableColumn
lapbState=_LapbState_Object((1,3,6,1,4,1,5651,3,7,1,3,1,3),_LapbState_Type())
lapbState.setMaxAccess(_C)
if mibBuilder.loadTexts:lapbState.setStatus(_A)
class _LapbModulo_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_LapbModulo_Type.__name__=_B
_LapbModulo_Object=MibTableColumn
lapbModulo=_LapbModulo_Object((1,3,6,1,4,1,5651,3,7,1,3,1,4),_LapbModulo_Type())
lapbModulo.setMaxAccess(_D)
if mibBuilder.loadTexts:lapbModulo.setStatus(_A)
class _LapbN1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(137,1513))
_LapbN1_Type.__name__=_B
_LapbN1_Object=MibTableColumn
lapbN1=_LapbN1_Object((1,3,6,1,4,1,5651,3,7,1,3,1,5),_LapbN1_Type())
lapbN1.setMaxAccess(_D)
if mibBuilder.loadTexts:lapbN1.setStatus(_A)
class _LapbN2_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_LapbN2_Type.__name__=_B
_LapbN2_Object=MibTableColumn
lapbN2=_LapbN2_Object((1,3,6,1,4,1,5651,3,7,1,3,1,6),_LapbN2_Type())
lapbN2.setMaxAccess(_D)
if mibBuilder.loadTexts:lapbN2.setStatus(_A)
class _LapbT1_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64000))
_LapbT1_Type.__name__=_B
_LapbT1_Object=MibTableColumn
lapbT1=_LapbT1_Object((1,3,6,1,4,1,5651,3,7,1,3,1,7),_LapbT1_Type())
lapbT1.setMaxAccess(_D)
if mibBuilder.loadTexts:lapbT1.setStatus(_A)
class _LapbT2_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32000))
_LapbT2_Type.__name__=_B
_LapbT2_Object=MibTableColumn
lapbT2=_LapbT2_Object((1,3,6,1,4,1,5651,3,7,1,3,1,8),_LapbT2_Type())
lapbT2.setMaxAccess(_D)
if mibBuilder.loadTexts:lapbT2.setStatus(_A)
class _LapbT4_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_LapbT4_Type.__name__=_B
_LapbT4_Object=MibTableColumn
lapbT4=_LapbT4_Object((1,3,6,1,4,1,5651,3,7,1,3,1,9),_LapbT4_Type())
lapbT4.setMaxAccess(_D)
if mibBuilder.loadTexts:lapbT4.setStatus(_A)
class _LapbK_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_LapbK_Type.__name__=_B
_LapbK_Object=MibTableColumn
lapbK=_LapbK_Object((1,3,6,1,4,1,5651,3,7,1,3,1,10),_LapbK_Type())
lapbK.setMaxAccess(_D)
if mibBuilder.loadTexts:lapbK.setStatus(_A)
_X25MapMib_ObjectIdentity=ObjectIdentity
x25MapMib=_X25MapMib_ObjectIdentity((1,3,6,1,4,1,5651,3,7,2))
_X25MapConfTable_Object=MibTable
x25MapConfTable=_X25MapConfTable_Object((1,3,6,1,4,1,5651,3,7,2,1))
if mibBuilder.loadTexts:x25MapConfTable.setStatus(_A)
_X25MapConfEntry_Object=MibTableRow
x25MapConfEntry=_X25MapConfEntry_Object((1,3,6,1,4,1,5651,3,7,2,1,1))
x25MapConfEntry.setIndexNames((0,_F,_N),(0,_F,_O),(0,_F,_P))
if mibBuilder.loadTexts:x25MapConfEntry.setStatus(_A)
_X25MapConfIfIndex_Type=Integer32
_X25MapConfIfIndex_Object=MibTableColumn
x25MapConfIfIndex=_X25MapConfIfIndex_Object((1,3,6,1,4,1,5651,3,7,2,1,1,1),_X25MapConfIfIndex_Type())
x25MapConfIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:x25MapConfIfIndex.setStatus(_A)
class _X25MapConfMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ip',1),(_Q,2),('qllc',3),('bridge',4)))
_X25MapConfMode_Type.__name__=_B
_X25MapConfMode_Object=MibTableColumn
x25MapConfMode=_X25MapConfMode_Object((1,3,6,1,4,1,5651,3,7,2,1,1,2),_X25MapConfMode_Type())
x25MapConfMode.setMaxAccess(_E)
if mibBuilder.loadTexts:x25MapConfMode.setStatus(_A)
class _X25MapConfAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_X25MapConfAddr_Type.__name__=_G
_X25MapConfAddr_Object=MibTableColumn
x25MapConfAddr=_X25MapConfAddr_Object((1,3,6,1,4,1,5651,3,7,2,1,1,3),_X25MapConfAddr_Type())
x25MapConfAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:x25MapConfAddr.setStatus(_A)
class _X25MapConfX121Addr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,14))
_X25MapConfX121Addr_Type.__name__=_G
_X25MapConfX121Addr_Object=MibTableColumn
x25MapConfX121Addr=_X25MapConfX121Addr_Object((1,3,6,1,4,1,5651,3,7,2,1,1,4),_X25MapConfX121Addr_Type())
x25MapConfX121Addr.setMaxAccess(_E)
if mibBuilder.loadTexts:x25MapConfX121Addr.setStatus(_A)
_X25MapConfLimite_Type=Integer32
_X25MapConfLimite_Object=MibTableColumn
x25MapConfLimite=_X25MapConfLimite_Object((1,3,6,1,4,1,5651,3,7,2,1,1,5),_X25MapConfLimite_Type())
x25MapConfLimite.setMaxAccess(_E)
if mibBuilder.loadTexts:x25MapConfLimite.setStatus(_A)
_X25MapConfBridgeIfIndex_Type=Integer32
_X25MapConfBridgeIfIndex_Object=MibTableColumn
x25MapConfBridgeIfIndex=_X25MapConfBridgeIfIndex_Object((1,3,6,1,4,1,5651,3,7,2,1,1,6),_X25MapConfBridgeIfIndex_Type())
x25MapConfBridgeIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:x25MapConfBridgeIfIndex.setStatus(_A)
class _X25MapConfBridgePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_X25MapConfBridgePort_Type.__name__=_B
_X25MapConfBridgePort_Object=MibTableColumn
x25MapConfBridgePort=_X25MapConfBridgePort_Object((1,3,6,1,4,1,5651,3,7,2,1,1,7),_X25MapConfBridgePort_Type())
x25MapConfBridgePort.setMaxAccess(_E)
if mibBuilder.loadTexts:x25MapConfBridgePort.setStatus(_A)
class _X25MapConfBridgeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tp-tcp',1),('none',2)))
_X25MapConfBridgeType_Type.__name__=_B
_X25MapConfBridgeType_Object=MibTableColumn
x25MapConfBridgeType=_X25MapConfBridgeType_Object((1,3,6,1,4,1,5651,3,7,2,1,1,8),_X25MapConfBridgeType_Type())
x25MapConfBridgeType.setMaxAccess(_E)
if mibBuilder.loadTexts:x25MapConfBridgeType.setStatus(_A)
class _X25MapConfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('pvc',2)))
_X25MapConfType_Type.__name__=_B
_X25MapConfType_Object=MibTableColumn
x25MapConfType=_X25MapConfType_Object((1,3,6,1,4,1,5651,3,7,2,1,1,9),_X25MapConfType_Type())
x25MapConfType.setMaxAccess(_C)
if mibBuilder.loadTexts:x25MapConfType.setStatus(_A)
_X25MapConfStatus_Type=RowStatus
_X25MapConfStatus_Object=MibTableColumn
x25MapConfStatus=_X25MapConfStatus_Object((1,3,6,1,4,1,5651,3,7,2,1,1,10),_X25MapConfStatus_Type())
x25MapConfStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:x25MapConfStatus.setStatus(_A)
_X25VcMib_ObjectIdentity=ObjectIdentity
x25VcMib=_X25VcMib_ObjectIdentity((1,3,6,1,4,1,5651,3,7,3))
_X25PvcConfTable_Object=MibTable
x25PvcConfTable=_X25PvcConfTable_Object((1,3,6,1,4,1,5651,3,7,3,1))
if mibBuilder.loadTexts:x25PvcConfTable.setStatus(_A)
_X25PvcConfEntry_Object=MibTableRow
x25PvcConfEntry=_X25PvcConfEntry_Object((1,3,6,1,4,1,5651,3,7,3,1,1))
x25PvcConfEntry.setIndexNames((0,_F,_R),(0,_F,_S))
if mibBuilder.loadTexts:x25PvcConfEntry.setStatus(_A)
_X25PvcConfIfIndex_Type=Integer32
_X25PvcConfIfIndex_Object=MibTableColumn
x25PvcConfIfIndex=_X25PvcConfIfIndex_Object((1,3,6,1,4,1,5651,3,7,3,1,1,1),_X25PvcConfIfIndex_Type())
x25PvcConfIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:x25PvcConfIfIndex.setStatus(_A)
class _X25PvcConfNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_X25PvcConfNum_Type.__name__=_B
_X25PvcConfNum_Object=MibTableColumn
x25PvcConfNum=_X25PvcConfNum_Object((1,3,6,1,4,1,5651,3,7,3,1,1,2),_X25PvcConfNum_Type())
x25PvcConfNum.setMaxAccess(_E)
if mibBuilder.loadTexts:x25PvcConfNum.setStatus(_A)
class _X25PvcConfMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ip',1),(_Q,2),('qllc',3),('xot',4),(_T,5)))
_X25PvcConfMode_Type.__name__=_B
_X25PvcConfMode_Object=MibTableColumn
x25PvcConfMode=_X25PvcConfMode_Object((1,3,6,1,4,1,5651,3,7,3,1,1,3),_X25PvcConfMode_Type())
x25PvcConfMode.setMaxAccess(_E)
if mibBuilder.loadTexts:x25PvcConfMode.setStatus(_A)
class _X25PvcConfAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_X25PvcConfAddr_Type.__name__=_G
_X25PvcConfAddr_Object=MibTableColumn
x25PvcConfAddr=_X25PvcConfAddr_Object((1,3,6,1,4,1,5651,3,7,3,1,1,4),_X25PvcConfAddr_Type())
x25PvcConfAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:x25PvcConfAddr.setStatus(_A)
class _X25PvcConfX121Addr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_X25PvcConfX121Addr_Type.__name__=_G
_X25PvcConfX121Addr_Object=MibTableColumn
x25PvcConfX121Addr=_X25PvcConfX121Addr_Object((1,3,6,1,4,1,5651,3,7,3,1,1,5),_X25PvcConfX121Addr_Type())
x25PvcConfX121Addr.setMaxAccess(_E)
if mibBuilder.loadTexts:x25PvcConfX121Addr.setStatus(_A)
class _X25PvcConfLimite_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('broadcast',1),('passive',2),('none',3)))
_X25PvcConfLimite_Type.__name__=_B
_X25PvcConfLimite_Object=MibTableColumn
x25PvcConfLimite=_X25PvcConfLimite_Object((1,3,6,1,4,1,5651,3,7,3,1,1,6),_X25PvcConfLimite_Type())
x25PvcConfLimite.setMaxAccess(_E)
if mibBuilder.loadTexts:x25PvcConfLimite.setStatus(_A)
_X25PvcConfXotIpAddr_Type=IpAddress
_X25PvcConfXotIpAddr_Object=MibTableColumn
x25PvcConfXotIpAddr=_X25PvcConfXotIpAddr_Object((1,3,6,1,4,1,5651,3,7,3,1,1,7),_X25PvcConfXotIpAddr_Type())
x25PvcConfXotIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:x25PvcConfXotIpAddr.setStatus(_A)
class _X25PvcConfRouteIntf_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_X25PvcConfRouteIntf_Type.__name__=_G
_X25PvcConfRouteIntf_Object=MibTableColumn
x25PvcConfRouteIntf=_X25PvcConfRouteIntf_Object((1,3,6,1,4,1,5651,3,7,3,1,1,8),_X25PvcConfRouteIntf_Type())
x25PvcConfRouteIntf.setMaxAccess(_E)
if mibBuilder.loadTexts:x25PvcConfRouteIntf.setStatus(_A)
class _X25PvcConfRouteNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_X25PvcConfRouteNum_Type.__name__=_B
_X25PvcConfRouteNum_Object=MibTableColumn
x25PvcConfRouteNum=_X25PvcConfRouteNum_Object((1,3,6,1,4,1,5651,3,7,3,1,1,9),_X25PvcConfRouteNum_Type())
x25PvcConfRouteNum.setMaxAccess(_E)
if mibBuilder.loadTexts:x25PvcConfRouteNum.setStatus(_A)
_X25PvcConfStatus_Type=RowStatus
_X25PvcConfStatus_Object=MibTableColumn
x25PvcConfStatus=_X25PvcConfStatus_Object((1,3,6,1,4,1,5651,3,7,3,1,1,10),_X25PvcConfStatus_Type())
x25PvcConfStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:x25PvcConfStatus.setStatus(_A)
_X25VcStatTable_Object=MibTable
x25VcStatTable=_X25VcStatTable_Object((1,3,6,1,4,1,5651,3,7,3,2))
if mibBuilder.loadTexts:x25VcStatTable.setStatus(_A)
_X25VcStatEntry_Object=MibTableRow
x25VcStatEntry=_X25VcStatEntry_Object((1,3,6,1,4,1,5651,3,7,3,2,1))
x25VcStatEntry.setIndexNames((0,_F,_U),(0,_F,_V))
if mibBuilder.loadTexts:x25VcStatEntry.setStatus(_A)
_X25VcStatIfIndex_Type=Integer32
_X25VcStatIfIndex_Object=MibTableColumn
x25VcStatIfIndex=_X25VcStatIfIndex_Object((1,3,6,1,4,1,5651,3,7,3,2,1,1),_X25VcStatIfIndex_Type())
x25VcStatIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatIfIndex.setStatus(_A)
class _X25VcStatNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_X25VcStatNum_Type.__name__=_B
_X25VcStatNum_Object=MibTableColumn
x25VcStatNum=_X25VcStatNum_Object((1,3,6,1,4,1,5651,3,7,3,2,1,2),_X25VcStatNum_Type())
x25VcStatNum.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatNum.setStatus(_A)
class _X25VcStatType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pvc',1),('svc',2)))
_X25VcStatType_Type.__name__=_B
_X25VcStatType_Object=MibTableColumn
x25VcStatType=_X25VcStatType_Object((1,3,6,1,4,1,5651,3,7,3,2,1,3),_X25VcStatType_Type())
x25VcStatType.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatType.setStatus(_A)
_X25VcStatTime_Type=DisplayString
_X25VcStatTime_Object=MibTableColumn
x25VcStatTime=_X25VcStatTime_Object((1,3,6,1,4,1,5651,3,7,3,2,1,4),_X25VcStatTime_Type())
x25VcStatTime.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatTime.setStatus(_A)
class _X25VcStatLocalX121Addr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,14))
_X25VcStatLocalX121Addr_Type.__name__=_G
_X25VcStatLocalX121Addr_Object=MibTableColumn
x25VcStatLocalX121Addr=_X25VcStatLocalX121Addr_Object((1,3,6,1,4,1,5651,3,7,3,2,1,5),_X25VcStatLocalX121Addr_Type())
x25VcStatLocalX121Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatLocalX121Addr.setStatus(_A)
class _X25VcStatRemoteX121Addr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_X25VcStatRemoteX121Addr_Type.__name__=_G
_X25VcStatRemoteX121Addr_Object=MibTableColumn
x25VcStatRemoteX121Addr=_X25VcStatRemoteX121Addr_Object((1,3,6,1,4,1,5651,3,7,3,2,1,6),_X25VcStatRemoteX121Addr_Type())
x25VcStatRemoteX121Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatRemoteX121Addr.setStatus(_A)
_X25VcStatRemoteAddr_Type=OctetString
_X25VcStatRemoteAddr_Object=MibTableColumn
x25VcStatRemoteAddr=_X25VcStatRemoteAddr_Object((1,3,6,1,4,1,5651,3,7,3,2,1,7),_X25VcStatRemoteAddr_Type())
x25VcStatRemoteAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatRemoteAddr.setStatus(_A)
class _X25VcStatFlowState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('readyD1',1),('dteResetingD2',2),('dceResetingD3',3),('error',4)))
_X25VcStatFlowState_Type.__name__=_B
_X25VcStatFlowState_Object=MibTableColumn
x25VcStatFlowState=_X25VcStatFlowState_Object((1,3,6,1,4,1,5651,3,7,3,2,1,8),_X25VcStatFlowState_Type())
x25VcStatFlowState.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatFlowState.setStatus(_A)
_X25VcStatSwin_Type=Integer32
_X25VcStatSwin_Object=MibTableColumn
x25VcStatSwin=_X25VcStatSwin_Object((1,3,6,1,4,1,5651,3,7,3,2,1,9),_X25VcStatSwin_Type())
x25VcStatSwin.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatSwin.setStatus(_A)
_X25VcStatRwin_Type=Integer32
_X25VcStatRwin_Object=MibTableColumn
x25VcStatRwin=_X25VcStatRwin_Object((1,3,6,1,4,1,5651,3,7,3,2,1,10),_X25VcStatRwin_Type())
x25VcStatRwin.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatRwin.setStatus(_A)
_X25VcStatSMaxPktSize_Type=Integer32
_X25VcStatSMaxPktSize_Object=MibTableColumn
x25VcStatSMaxPktSize=_X25VcStatSMaxPktSize_Object((1,3,6,1,4,1,5651,3,7,3,2,1,11),_X25VcStatSMaxPktSize_Type())
x25VcStatSMaxPktSize.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatSMaxPktSize.setStatus(_A)
_X25VcStatRMaxPktSize_Type=Integer32
_X25VcStatRMaxPktSize_Object=MibTableColumn
x25VcStatRMaxPktSize=_X25VcStatRMaxPktSize_Object((1,3,6,1,4,1,5651,3,7,3,2,1,12),_X25VcStatRMaxPktSize_Type())
x25VcStatRMaxPktSize.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatRMaxPktSize.setStatus(_A)
_X25VcStatVr_Type=Counter32
_X25VcStatVr_Object=MibTableColumn
x25VcStatVr=_X25VcStatVr_Object((1,3,6,1,4,1,5651,3,7,3,2,1,13),_X25VcStatVr_Type())
x25VcStatVr.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatVr.setStatus(_A)
_X25VcStatVs_Type=Counter32
_X25VcStatVs_Object=MibTableColumn
x25VcStatVs=_X25VcStatVs_Object((1,3,6,1,4,1,5651,3,7,3,2,1,14),_X25VcStatVs_Type())
x25VcStatVs.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatVs.setStatus(_A)
_X25VcStatNr_Type=Counter32
_X25VcStatNr_Object=MibTableColumn
x25VcStatNr=_X25VcStatNr_Object((1,3,6,1,4,1,5651,3,7,3,2,1,15),_X25VcStatNr_Type())
x25VcStatNr.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatNr.setStatus(_A)
_X25VcStatNs_Type=Counter32
_X25VcStatNs_Object=MibTableColumn
x25VcStatNs=_X25VcStatNs_Object((1,3,6,1,4,1,5651,3,7,3,2,1,16),_X25VcStatNs_Type())
x25VcStatNs.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatNs.setStatus(_A)
_X25VcStatLastNr_Type=Counter32
_X25VcStatLastNr_Object=MibTableColumn
x25VcStatLastNr=_X25VcStatLastNr_Object((1,3,6,1,4,1,5651,3,7,3,2,1,17),_X25VcStatLastNr_Type())
x25VcStatLastNr.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatLastNr.setStatus(_A)
_X25VcStatNoRsp_Type=Counter32
_X25VcStatNoRsp_Object=MibTableColumn
x25VcStatNoRsp=_X25VcStatNoRsp_Object((1,3,6,1,4,1,5651,3,7,3,2,1,18),_X25VcStatNoRsp_Type())
x25VcStatNoRsp.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatNoRsp.setStatus(_A)
_X25VcStatStxqPriority_Type=Integer32
_X25VcStatStxqPriority_Object=MibTableColumn
x25VcStatStxqPriority=_X25VcStatStxqPriority_Object((1,3,6,1,4,1,5651,3,7,3,2,1,19),_X25VcStatStxqPriority_Type())
x25VcStatStxqPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatStxqPriority.setStatus(_A)
_X25VcStatStxqCnt_Type=Counter32
_X25VcStatStxqCnt_Object=MibTableColumn
x25VcStatStxqCnt=_X25VcStatStxqCnt_Object((1,3,6,1,4,1,5651,3,7,3,2,1,20),_X25VcStatStxqCnt_Type())
x25VcStatStxqCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatStxqCnt.setStatus(_A)
_X25VcStatStxqMax_Type=Counter32
_X25VcStatStxqMax_Object=MibTableColumn
x25VcStatStxqMax=_X25VcStatStxqMax_Object((1,3,6,1,4,1,5651,3,7,3,2,1,21),_X25VcStatStxqMax_Type())
x25VcStatStxqMax.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatStxqMax.setStatus(_A)
_X25VcStatStxqSmax_Type=Counter32
_X25VcStatStxqSmax_Object=MibTableColumn
x25VcStatStxqSmax=_X25VcStatStxqSmax_Object((1,3,6,1,4,1,5651,3,7,3,2,1,22),_X25VcStatStxqSmax_Type())
x25VcStatStxqSmax.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatStxqSmax.setStatus(_A)
_X25VcStatStxqQw_Type=Counter32
_X25VcStatStxqQw_Object=MibTableColumn
x25VcStatStxqQw=_X25VcStatStxqQw_Object((1,3,6,1,4,1,5651,3,7,3,2,1,23),_X25VcStatStxqQw_Type())
x25VcStatStxqQw.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatStxqQw.setStatus(_A)
_X25VcStatStxqQwmax_Type=Counter32
_X25VcStatStxqQwmax_Object=MibTableColumn
x25VcStatStxqQwmax=_X25VcStatStxqQwmax_Object((1,3,6,1,4,1,5651,3,7,3,2,1,24),_X25VcStatStxqQwmax_Type())
x25VcStatStxqQwmax.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatStxqQwmax.setStatus(_A)
_X25VcStatTxqPriority_Type=Integer32
_X25VcStatTxqPriority_Object=MibTableColumn
x25VcStatTxqPriority=_X25VcStatTxqPriority_Object((1,3,6,1,4,1,5651,3,7,3,2,1,25),_X25VcStatTxqPriority_Type())
x25VcStatTxqPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatTxqPriority.setStatus(_A)
_X25VcStatTxqCnt_Type=Counter32
_X25VcStatTxqCnt_Object=MibTableColumn
x25VcStatTxqCnt=_X25VcStatTxqCnt_Object((1,3,6,1,4,1,5651,3,7,3,2,1,26),_X25VcStatTxqCnt_Type())
x25VcStatTxqCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatTxqCnt.setStatus(_A)
_X25VcStatTxqMax_Type=Counter32
_X25VcStatTxqMax_Object=MibTableColumn
x25VcStatTxqMax=_X25VcStatTxqMax_Object((1,3,6,1,4,1,5651,3,7,3,2,1,27),_X25VcStatTxqMax_Type())
x25VcStatTxqMax.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatTxqMax.setStatus(_A)
_X25VcStatTxqSmax_Type=Counter32
_X25VcStatTxqSmax_Object=MibTableColumn
x25VcStatTxqSmax=_X25VcStatTxqSmax_Object((1,3,6,1,4,1,5651,3,7,3,2,1,28),_X25VcStatTxqSmax_Type())
x25VcStatTxqSmax.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatTxqSmax.setStatus(_A)
_X25VcStatTxqQw_Type=Counter32
_X25VcStatTxqQw_Object=MibTableColumn
x25VcStatTxqQw=_X25VcStatTxqQw_Object((1,3,6,1,4,1,5651,3,7,3,2,1,29),_X25VcStatTxqQw_Type())
x25VcStatTxqQw.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatTxqQw.setStatus(_A)
_X25VcStatTxqQwmax_Type=Counter32
_X25VcStatTxqQwmax_Object=MibTableColumn
x25VcStatTxqQwmax=_X25VcStatTxqQwmax_Object((1,3,6,1,4,1,5651,3,7,3,2,1,30),_X25VcStatTxqQwmax_Type())
x25VcStatTxqQwmax.setMaxAccess(_C)
if mibBuilder.loadTexts:x25VcStatTxqQwmax.setStatus(_A)
_X25RouteMib_ObjectIdentity=ObjectIdentity
x25RouteMib=_X25RouteMib_ObjectIdentity((1,3,6,1,4,1,5651,3,7,4))
class _X25RoutingConfSwitch_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('close',1),('open',2)))
_X25RoutingConfSwitch_Type.__name__=_B
_X25RoutingConfSwitch_Object=MibScalar
x25RoutingConfSwitch=_X25RoutingConfSwitch_Object((1,3,6,1,4,1,5651,3,7,4,1),_X25RoutingConfSwitch_Type())
x25RoutingConfSwitch.setMaxAccess(_D)
if mibBuilder.loadTexts:x25RoutingConfSwitch.setStatus(_A)
_X25RouteConfTable_Object=MibTable
x25RouteConfTable=_X25RouteConfTable_Object((1,3,6,1,4,1,5651,3,7,4,2))
if mibBuilder.loadTexts:x25RouteConfTable.setStatus(_A)
_X25RouteConfEntry_Object=MibTableRow
x25RouteConfEntry=_X25RouteConfEntry_Object((1,3,6,1,4,1,5651,3,7,4,2,1))
x25RouteConfEntry.setIndexNames((0,_F,_W))
if mibBuilder.loadTexts:x25RouteConfEntry.setStatus(_A)
class _X25RouteConfX121Addr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_X25RouteConfX121Addr_Type.__name__=_G
_X25RouteConfX121Addr_Object=MibTableColumn
x25RouteConfX121Addr=_X25RouteConfX121Addr_Object((1,3,6,1,4,1,5651,3,7,4,2,1,1),_X25RouteConfX121Addr_Type())
x25RouteConfX121Addr.setMaxAccess(_E)
if mibBuilder.loadTexts:x25RouteConfX121Addr.setStatus(_A)
class _X25RouteConfType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),('xot',2)))
_X25RouteConfType_Type.__name__=_B
_X25RouteConfType_Object=MibTableColumn
x25RouteConfType=_X25RouteConfType_Object((1,3,6,1,4,1,5651,3,7,4,2,1,2),_X25RouteConfType_Type())
x25RouteConfType.setMaxAccess(_E)
if mibBuilder.loadTexts:x25RouteConfType.setStatus(_A)
_X25RouteConfIfIndex_Type=Integer32
_X25RouteConfIfIndex_Object=MibTableColumn
x25RouteConfIfIndex=_X25RouteConfIfIndex_Object((1,3,6,1,4,1,5651,3,7,4,2,1,3),_X25RouteConfIfIndex_Type())
x25RouteConfIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:x25RouteConfIfIndex.setStatus(_A)
class _X25RouteConfXotIpAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_X25RouteConfXotIpAddr_Type.__name__=_G
_X25RouteConfXotIpAddr_Object=MibTableColumn
x25RouteConfXotIpAddr=_X25RouteConfXotIpAddr_Object((1,3,6,1,4,1,5651,3,7,4,2,1,4),_X25RouteConfXotIpAddr_Type())
x25RouteConfXotIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:x25RouteConfXotIpAddr.setStatus(_A)
_X25RouteConfStatus_Type=RowStatus
_X25RouteConfStatus_Object=MibTableColumn
x25RouteConfStatus=_X25RouteConfStatus_Object((1,3,6,1,4,1,5651,3,7,4,2,1,5),_X25RouteConfStatus_Type())
x25RouteConfStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:x25RouteConfStatus.setStatus(_A)
_X25AgentMib_ObjectIdentity=ObjectIdentity
x25AgentMib=_X25AgentMib_ObjectIdentity((1,3,6,1,4,1,5651,3,7,5))
class _X25AgentTcpPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5000,10000))
_X25AgentTcpPort_Type.__name__=_I
_X25AgentTcpPort_Object=MibScalar
x25AgentTcpPort=_X25AgentTcpPort_Object((1,3,6,1,4,1,5651,3,7,5,1),_X25AgentTcpPort_Type())
x25AgentTcpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:x25AgentTcpPort.setStatus(_A)
class _X25AgentInitTimeout_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,30))
_X25AgentInitTimeout_Type.__name__=_I
_X25AgentInitTimeout_Object=MibScalar
x25AgentInitTimeout=_X25AgentInitTimeout_Object((1,3,6,1,4,1,5651,3,7,5,2),_X25AgentInitTimeout_Type())
x25AgentInitTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:x25AgentInitTimeout.setStatus(_A)
class _X25AgentBufferFlush_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,180))
_X25AgentBufferFlush_Type.__name__=_I
_X25AgentBufferFlush_Object=MibScalar
x25AgentBufferFlush=_X25AgentBufferFlush_Object((1,3,6,1,4,1,5651,3,7,5,3),_X25AgentBufferFlush_Type())
x25AgentBufferFlush.setMaxAccess(_D)
if mibBuilder.loadTexts:x25AgentBufferFlush.setStatus(_A)
_X25AgentAddressTable_Object=MibTable
x25AgentAddressTable=_X25AgentAddressTable_Object((1,3,6,1,4,1,5651,3,7,5,4))
if mibBuilder.loadTexts:x25AgentAddressTable.setStatus(_A)
_X25AgentAddressEntry_Object=MibTableRow
x25AgentAddressEntry=_X25AgentAddressEntry_Object((1,3,6,1,4,1,5651,3,7,5,4,1))
x25AgentAddressEntry.setIndexNames((0,_F,_X))
if mibBuilder.loadTexts:x25AgentAddressEntry.setStatus(_A)
class _X25AgentLogicAddr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_X25AgentLogicAddr_Type.__name__=_H
_X25AgentLogicAddr_Object=MibTableColumn
x25AgentLogicAddr=_X25AgentLogicAddr_Object((1,3,6,1,4,1,5651,3,7,5,4,1,1),_X25AgentLogicAddr_Type())
x25AgentLogicAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:x25AgentLogicAddr.setStatus(_A)
class _X25AgentX121Addr0_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_X25AgentX121Addr0_Type.__name__=_H
_X25AgentX121Addr0_Object=MibTableColumn
x25AgentX121Addr0=_X25AgentX121Addr0_Object((1,3,6,1,4,1,5651,3,7,5,4,1,2),_X25AgentX121Addr0_Type())
x25AgentX121Addr0.setMaxAccess(_D)
if mibBuilder.loadTexts:x25AgentX121Addr0.setStatus(_A)
class _X25AgentX121Addr1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_X25AgentX121Addr1_Type.__name__=_H
_X25AgentX121Addr1_Object=MibTableColumn
x25AgentX121Addr1=_X25AgentX121Addr1_Object((1,3,6,1,4,1,5651,3,7,5,4,1,3),_X25AgentX121Addr1_Type())
x25AgentX121Addr1.setMaxAccess(_D)
if mibBuilder.loadTexts:x25AgentX121Addr1.setStatus(_A)
class _X25AgentX121Addr2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_X25AgentX121Addr2_Type.__name__=_H
_X25AgentX121Addr2_Object=MibTableColumn
x25AgentX121Addr2=_X25AgentX121Addr2_Object((1,3,6,1,4,1,5651,3,7,5,4,1,4),_X25AgentX121Addr2_Type())
x25AgentX121Addr2.setMaxAccess(_D)
if mibBuilder.loadTexts:x25AgentX121Addr2.setStatus(_A)
class _X25AgentX121Addr3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_X25AgentX121Addr3_Type.__name__=_H
_X25AgentX121Addr3_Object=MibTableColumn
x25AgentX121Addr3=_X25AgentX121Addr3_Object((1,3,6,1,4,1,5651,3,7,5,4,1,5),_X25AgentX121Addr3_Type())
x25AgentX121Addr3.setMaxAccess(_D)
if mibBuilder.loadTexts:x25AgentX121Addr3.setStatus(_A)
class _X25AgentX121Addr4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_X25AgentX121Addr4_Type.__name__=_H
_X25AgentX121Addr4_Object=MibTableColumn
x25AgentX121Addr4=_X25AgentX121Addr4_Object((1,3,6,1,4,1,5651,3,7,5,4,1,6),_X25AgentX121Addr4_Type())
x25AgentX121Addr4.setMaxAccess(_D)
if mibBuilder.loadTexts:x25AgentX121Addr4.setStatus(_A)
_X25AgentAddressRowStatus_Type=RowStatus
_X25AgentAddressRowStatus_Object=MibTableColumn
x25AgentAddressRowStatus=_X25AgentAddressRowStatus_Object((1,3,6,1,4,1,5651,3,7,5,4,1,7),_X25AgentAddressRowStatus_Type())
x25AgentAddressRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:x25AgentAddressRowStatus.setStatus(_A)
_X25AgentInterfaceTable_Object=MibTable
x25AgentInterfaceTable=_X25AgentInterfaceTable_Object((1,3,6,1,4,1,5651,3,7,5,5))
if mibBuilder.loadTexts:x25AgentInterfaceTable.setStatus(_A)
_X25AgentInterfaceEntry_Object=MibTableRow
x25AgentInterfaceEntry=_X25AgentInterfaceEntry_Object((1,3,6,1,4,1,5651,3,7,5,5,1))
x25AgentInterfaceEntry.setIndexNames((0,_F,_Y))
if mibBuilder.loadTexts:x25AgentInterfaceEntry.setStatus(_A)
_X25AgentIfIndex_Type=Integer32
_X25AgentIfIndex_Object=MibTableColumn
x25AgentIfIndex=_X25AgentIfIndex_Object((1,3,6,1,4,1,5651,3,7,5,5,1,1),_X25AgentIfIndex_Type())
x25AgentIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:x25AgentIfIndex.setStatus(_A)
class _X25AgentNetworkNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_X25AgentNetworkNumber_Type.__name__=_B
_X25AgentNetworkNumber_Object=MibTableColumn
x25AgentNetworkNumber=_X25AgentNetworkNumber_Object((1,3,6,1,4,1,5651,3,7,5,5,1,2),_X25AgentNetworkNumber_Type())
x25AgentNetworkNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:x25AgentNetworkNumber.setStatus(_A)
_X25AgentInterfaceRowStatus_Type=RowStatus
_X25AgentInterfaceRowStatus_Object=MibTableColumn
x25AgentInterfaceRowStatus=_X25AgentInterfaceRowStatus_Object((1,3,6,1,4,1,5651,3,7,5,5,1,3),_X25AgentInterfaceRowStatus_Type())
x25AgentInterfaceRowStatus.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:x25AgentInterfaceRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'mpX25Mib':mpX25Mib,'x25IfMib':x25IfMib,'x25ConfTable':x25ConfTable,'x25ConfEntry':x25ConfEntry,_J:x25ConfIfIndex,'x25ConfMode':x25ConfMode,'x25ConfState':x25ConfState,'x25ConfAddress':x25ConfAddress,'x25ConfHtc':x25ConfHtc,'x25ConfLtc':x25ConfLtc,'x25ConfHoldQueue':x25ConfHoldQueue,'x25ConfIdle':x25ConfIdle,'x25ConfIps':x25ConfIps,'x25ConfOps':x25ConfOps,'x25ConfModulo':x25ConfModulo,'x25ConfNvc':x25ConfNvc,'x25ConfWin':x25ConfWin,'x25ConfWout':x25ConfWout,'x25ConfT20':x25ConfT20,'x25ConfT21':x25ConfT21,'x25ConfT22':x25ConfT22,'x25ConfT23':x25ConfT23,'x25ConfHic':x25ConfHic,'x25ConfHoc':x25ConfHoc,'lapbConfTable':lapbConfTable,'lapbConfEntry':lapbConfEntry,_M:lapbIfIndex,'lapbMode':lapbMode,'lapbState':lapbState,'lapbModulo':lapbModulo,'lapbN1':lapbN1,'lapbN2':lapbN2,'lapbT1':lapbT1,'lapbT2':lapbT2,'lapbT4':lapbT4,'lapbK':lapbK,'x25MapMib':x25MapMib,'x25MapConfTable':x25MapConfTable,'x25MapConfEntry':x25MapConfEntry,_N:x25MapConfIfIndex,_O:x25MapConfMode,_P:x25MapConfAddr,'x25MapConfX121Addr':x25MapConfX121Addr,'x25MapConfLimite':x25MapConfLimite,'x25MapConfBridgeIfIndex':x25MapConfBridgeIfIndex,'x25MapConfBridgePort':x25MapConfBridgePort,'x25MapConfBridgeType':x25MapConfBridgeType,'x25MapConfType':x25MapConfType,'x25MapConfStatus':x25MapConfStatus,'x25VcMib':x25VcMib,'x25PvcConfTable':x25PvcConfTable,'x25PvcConfEntry':x25PvcConfEntry,_R:x25PvcConfIfIndex,_S:x25PvcConfNum,'x25PvcConfMode':x25PvcConfMode,'x25PvcConfAddr':x25PvcConfAddr,'x25PvcConfX121Addr':x25PvcConfX121Addr,'x25PvcConfLimite':x25PvcConfLimite,'x25PvcConfXotIpAddr':x25PvcConfXotIpAddr,'x25PvcConfRouteIntf':x25PvcConfRouteIntf,'x25PvcConfRouteNum':x25PvcConfRouteNum,'x25PvcConfStatus':x25PvcConfStatus,'x25VcStatTable':x25VcStatTable,'x25VcStatEntry':x25VcStatEntry,_U:x25VcStatIfIndex,_V:x25VcStatNum,'x25VcStatType':x25VcStatType,'x25VcStatTime':x25VcStatTime,'x25VcStatLocalX121Addr':x25VcStatLocalX121Addr,'x25VcStatRemoteX121Addr':x25VcStatRemoteX121Addr,'x25VcStatRemoteAddr':x25VcStatRemoteAddr,'x25VcStatFlowState':x25VcStatFlowState,'x25VcStatSwin':x25VcStatSwin,'x25VcStatRwin':x25VcStatRwin,'x25VcStatSMaxPktSize':x25VcStatSMaxPktSize,'x25VcStatRMaxPktSize':x25VcStatRMaxPktSize,'x25VcStatVr':x25VcStatVr,'x25VcStatVs':x25VcStatVs,'x25VcStatNr':x25VcStatNr,'x25VcStatNs':x25VcStatNs,'x25VcStatLastNr':x25VcStatLastNr,'x25VcStatNoRsp':x25VcStatNoRsp,'x25VcStatStxqPriority':x25VcStatStxqPriority,'x25VcStatStxqCnt':x25VcStatStxqCnt,'x25VcStatStxqMax':x25VcStatStxqMax,'x25VcStatStxqSmax':x25VcStatStxqSmax,'x25VcStatStxqQw':x25VcStatStxqQw,'x25VcStatStxqQwmax':x25VcStatStxqQwmax,'x25VcStatTxqPriority':x25VcStatTxqPriority,'x25VcStatTxqCnt':x25VcStatTxqCnt,'x25VcStatTxqMax':x25VcStatTxqMax,'x25VcStatTxqSmax':x25VcStatTxqSmax,'x25VcStatTxqQw':x25VcStatTxqQw,'x25VcStatTxqQwmax':x25VcStatTxqQwmax,'x25RouteMib':x25RouteMib,'x25RoutingConfSwitch':x25RoutingConfSwitch,'x25RouteConfTable':x25RouteConfTable,'x25RouteConfEntry':x25RouteConfEntry,_W:x25RouteConfX121Addr,'x25RouteConfType':x25RouteConfType,'x25RouteConfIfIndex':x25RouteConfIfIndex,'x25RouteConfXotIpAddr':x25RouteConfXotIpAddr,'x25RouteConfStatus':x25RouteConfStatus,'x25AgentMib':x25AgentMib,'x25AgentTcpPort':x25AgentTcpPort,'x25AgentInitTimeout':x25AgentInitTimeout,'x25AgentBufferFlush':x25AgentBufferFlush,'x25AgentAddressTable':x25AgentAddressTable,'x25AgentAddressEntry':x25AgentAddressEntry,_X:x25AgentLogicAddr,'x25AgentX121Addr0':x25AgentX121Addr0,'x25AgentX121Addr1':x25AgentX121Addr1,'x25AgentX121Addr2':x25AgentX121Addr2,'x25AgentX121Addr3':x25AgentX121Addr3,'x25AgentX121Addr4':x25AgentX121Addr4,'x25AgentAddressRowStatus':x25AgentAddressRowStatus,'x25AgentInterfaceTable':x25AgentInterfaceTable,'x25AgentInterfaceEntry':x25AgentInterfaceEntry,_Y:x25AgentIfIndex,'x25AgentNetworkNumber':x25AgentNetworkNumber,'x25AgentInterfaceRowStatus':x25AgentInterfaceRowStatus})