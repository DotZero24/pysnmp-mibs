_AD='ntcTrfShapeConfGrpV1Standard'
_AC='ntcTrfShapeUnit'
_AB='ntcTrfMaxQTExtime'
_AA='ntcTrfShapeExtPrio'
_A9='ntcTrfShapeExtDestChan'
_A8='ntcTrfShapeExtPir'
_A7='ntcTrfShapeExtCir'
_A6='ntcTrfShapeExtParentNam'
_A5='ntcTrfShExtShapingNodeEnable'
_A4='ntcTrfShExtShapingNodeRowStatus'
_A3='ntcTrfShapeExtMatchingOrder'
_A2='ntcTrfShapeExtShapingNode'
_A1='ntcTrfShapeExtExpr'
_A0='ntcTrfShapeExtNetwAddr'
_z='ntcTrfShapeExtUseNetwAddr'
_y='ntcTrfShExtClassifEnable'
_x='ntcTrfShExtClassifRowStatus'
_w='ntcTrfShMonFwdBitRate'
_v='ntcTrfShMonReset'
_u='ntcTrfShapeNodeVolUnit'
_t='ntcTrfShapeNodeDropRate'
_s='ntcTrfShapeNodeVolRate'
_r='ntcTrfShapeNodeAverageDelay'
_q='ntcTrfShapeNodeDropPackets'
_p='ntcTrfMonShNodeDropByt'
_o='ntcTfrMonShNodeFwdPackets'
_n='ntcTrfMonShNodeFwdByte'
_m='ntcTrfMonShNodeName'
_l='ntcTrfShMonDropPackets'
_k='ntcTrfShMonDropBytes'
_j='ntcTrfShMonFwdPackets'
_i='ntcTrfShMonFwdBytes'
_h='ntcTrfMaxQTime'
_g='ntcTrfShapePrio'
_f='ntcTrfShapeDestChannel'
_e='ntcTrfShapePir'
_d='ntcTrfShapeCir'
_c='ntcTrfShapeParentName'
_b='ntcTrfShShapingNodeEnable'
_a='ntcTrfShapeNodeName'
_Z='ntcTrfShapeShapingNode'
_Y='ntcTrfShapeExpr'
_X='ntcTrfShapeNetwAddress'
_W='ntcTrfShapeUseNetwAddress'
_V='ntcTrfShClassificationEnable'
_U='ntcTrfShapeClassifName'
_T='ntcTrfShInputSelection'
_S='ntcTrfShEnable'
_R='ntcTrfShExtShapingNodeName'
_Q='ntcTrfShExtClassifName'
_P='ntcTrfShMonShapingNodeInx'
_O='ntcTrfShShapingNodeInx'
_N='ntcTrfShClassificationInx'
_M='NtcNetworkAddress'
_L='packets'
_K='bytes'
_J='NtcEnable'
_I='not-accessible'
_H='Unsigned32'
_G='Integer32'
_F='read-only'
_E='DisplayString'
_D='read-create'
_C='read-write'
_B='NEWTEC-TRAFFICSHAPER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcEnable,NtcNetworkAddress=mibBuilder.importSymbols('NEWTEC-TC-MIB',_J,_M)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention')
ntcTrafficShaper=ModuleIdentity((1,3,6,1,4,1,5835,5,2,2000))
if mibBuilder.loadTexts:ntcTrafficShaper.setRevisions(('2017-07-10 12:00','2014-09-09 09:00','2014-09-04 12:00','2014-07-15 08:00','2014-02-03 12:00','2013-07-05 06:00','2013-05-22 06:00','2013-01-08 12:00','2012-06-28 12:00'))
_NtcTrfShapeObjects_ObjectIdentity=ObjectIdentity
ntcTrfShapeObjects=_NtcTrfShapeObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,2000,1))
if mibBuilder.loadTexts:ntcTrfShapeObjects.setStatus(_A)
class _NtcTrfShEnable_Type(NtcEnable):defaultValue=0
_NtcTrfShEnable_Type.__name__=_J
_NtcTrfShEnable_Object=MibScalar
ntcTrfShEnable=_NtcTrfShEnable_Object((1,3,6,1,4,1,5835,5,2,2000,1,1),_NtcTrfShEnable_Type())
ntcTrfShEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTrfShEnable.setStatus(_A)
class _NtcTrfShInputSelection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('data1',1),('data2',2),('data',3)))
_NtcTrfShInputSelection_Type.__name__=_G
_NtcTrfShInputSelection_Object=MibScalar
ntcTrfShInputSelection=_NtcTrfShInputSelection_Object((1,3,6,1,4,1,5835,5,2,2000,1,2),_NtcTrfShInputSelection_Type())
ntcTrfShInputSelection.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTrfShInputSelection.setStatus(_A)
_NtcTrfShClassificationTable_Object=MibTable
ntcTrfShClassificationTable=_NtcTrfShClassificationTable_Object((1,3,6,1,4,1,5835,5,2,2000,1,3))
if mibBuilder.loadTexts:ntcTrfShClassificationTable.setStatus(_A)
_NtcTrfShClassificationEntry_Object=MibTableRow
ntcTrfShClassificationEntry=_NtcTrfShClassificationEntry_Object((1,3,6,1,4,1,5835,5,2,2000,1,3,1))
ntcTrfShClassificationEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:ntcTrfShClassificationEntry.setStatus(_A)
_NtcTrfShClassificationInx_Type=Unsigned32
_NtcTrfShClassificationInx_Object=MibTableColumn
ntcTrfShClassificationInx=_NtcTrfShClassificationInx_Object((1,3,6,1,4,1,5835,5,2,2000,1,3,1,1),_NtcTrfShClassificationInx_Type())
ntcTrfShClassificationInx.setMaxAccess(_I)
if mibBuilder.loadTexts:ntcTrfShClassificationInx.setStatus(_A)
class _NtcTrfShapeClassifName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_NtcTrfShapeClassifName_Type.__name__=_E
_NtcTrfShapeClassifName_Object=MibTableColumn
ntcTrfShapeClassifName=_NtcTrfShapeClassifName_Object((1,3,6,1,4,1,5835,5,2,2000,1,3,1,2),_NtcTrfShapeClassifName_Type())
ntcTrfShapeClassifName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTrfShapeClassifName.setStatus(_A)
class _NtcTrfShClassificationEnable_Type(NtcEnable):defaultValue=0
_NtcTrfShClassificationEnable_Type.__name__=_J
_NtcTrfShClassificationEnable_Object=MibTableColumn
ntcTrfShClassificationEnable=_NtcTrfShClassificationEnable_Object((1,3,6,1,4,1,5835,5,2,2000,1,3,1,3),_NtcTrfShClassificationEnable_Type())
ntcTrfShClassificationEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTrfShClassificationEnable.setStatus(_A)
class _NtcTrfShapeUseNetwAddress_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_NtcTrfShapeUseNetwAddress_Type.__name__=_G
_NtcTrfShapeUseNetwAddress_Object=MibTableColumn
ntcTrfShapeUseNetwAddress=_NtcTrfShapeUseNetwAddress_Object((1,3,6,1,4,1,5835,5,2,2000,1,3,1,4),_NtcTrfShapeUseNetwAddress_Type())
ntcTrfShapeUseNetwAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTrfShapeUseNetwAddress.setStatus(_A)
class _NtcTrfShapeNetwAddress_Type(NtcNetworkAddress):defaultValue=OctetString('0.0.0.0/24')
_NtcTrfShapeNetwAddress_Type.__name__=_M
_NtcTrfShapeNetwAddress_Object=MibTableColumn
ntcTrfShapeNetwAddress=_NtcTrfShapeNetwAddress_Object((1,3,6,1,4,1,5835,5,2,2000,1,3,1,5),_NtcTrfShapeNetwAddress_Type())
ntcTrfShapeNetwAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTrfShapeNetwAddress.setStatus(_A)
class _NtcTrfShapeExpr_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4000))
_NtcTrfShapeExpr_Type.__name__=_E
_NtcTrfShapeExpr_Object=MibTableColumn
ntcTrfShapeExpr=_NtcTrfShapeExpr_Object((1,3,6,1,4,1,5835,5,2,2000,1,3,1,6),_NtcTrfShapeExpr_Type())
ntcTrfShapeExpr.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTrfShapeExpr.setStatus(_A)
class _NtcTrfShapeShapingNode_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_NtcTrfShapeShapingNode_Type.__name__=_E
_NtcTrfShapeShapingNode_Object=MibTableColumn
ntcTrfShapeShapingNode=_NtcTrfShapeShapingNode_Object((1,3,6,1,4,1,5835,5,2,2000,1,3,1,7),_NtcTrfShapeShapingNode_Type())
ntcTrfShapeShapingNode.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTrfShapeShapingNode.setStatus(_A)
_NtcTrfShShapingNodeTable_Object=MibTable
ntcTrfShShapingNodeTable=_NtcTrfShShapingNodeTable_Object((1,3,6,1,4,1,5835,5,2,2000,1,4))
if mibBuilder.loadTexts:ntcTrfShShapingNodeTable.setStatus(_A)
_NtcTrfShShapingNodeEntry_Object=MibTableRow
ntcTrfShShapingNodeEntry=_NtcTrfShShapingNodeEntry_Object((1,3,6,1,4,1,5835,5,2,2000,1,4,1))
ntcTrfShShapingNodeEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:ntcTrfShShapingNodeEntry.setStatus(_A)
_NtcTrfShShapingNodeInx_Type=Unsigned32
_NtcTrfShShapingNodeInx_Object=MibTableColumn
ntcTrfShShapingNodeInx=_NtcTrfShShapingNodeInx_Object((1,3,6,1,4,1,5835,5,2,2000,1,4,1,1),_NtcTrfShShapingNodeInx_Type())
ntcTrfShShapingNodeInx.setMaxAccess(_I)
if mibBuilder.loadTexts:ntcTrfShShapingNodeInx.setStatus(_A)
class _NtcTrfShapeNodeName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_NtcTrfShapeNodeName_Type.__name__=_E
_NtcTrfShapeNodeName_Object=MibTableColumn
ntcTrfShapeNodeName=_NtcTrfShapeNodeName_Object((1,3,6,1,4,1,5835,5,2,2000,1,4,1,2),_NtcTrfShapeNodeName_Type())
ntcTrfShapeNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTrfShapeNodeName.setStatus(_A)
class _NtcTrfShShapingNodeEnable_Type(NtcEnable):defaultValue=0
_NtcTrfShShapingNodeEnable_Type.__name__=_J
_NtcTrfShShapingNodeEnable_Object=MibTableColumn
ntcTrfShShapingNodeEnable=_NtcTrfShShapingNodeEnable_Object((1,3,6,1,4,1,5835,5,2,2000,1,4,1,3),_NtcTrfShShapingNodeEnable_Type())
ntcTrfShShapingNodeEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTrfShShapingNodeEnable.setStatus(_A)
class _NtcTrfShapeParentName_Type(DisplayString):defaultValue=OctetString('Root');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_NtcTrfShapeParentName_Type.__name__=_E
_NtcTrfShapeParentName_Object=MibTableColumn
ntcTrfShapeParentName=_NtcTrfShapeParentName_Object((1,3,6,1,4,1,5835,5,2,2000,1,4,1,4),_NtcTrfShapeParentName_Type())
ntcTrfShapeParentName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTrfShapeParentName.setStatus(_A)
class _NtcTrfShapeCir_Type(Unsigned32):defaultValue=0
_NtcTrfShapeCir_Type.__name__=_H
_NtcTrfShapeCir_Object=MibTableColumn
ntcTrfShapeCir=_NtcTrfShapeCir_Object((1,3,6,1,4,1,5835,5,2,2000,1,4,1,5),_NtcTrfShapeCir_Type())
ntcTrfShapeCir.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTrfShapeCir.setStatus(_A)
class _NtcTrfShapePir_Type(Unsigned32):defaultValue=10000000
_NtcTrfShapePir_Type.__name__=_H
_NtcTrfShapePir_Object=MibTableColumn
ntcTrfShapePir=_NtcTrfShapePir_Object((1,3,6,1,4,1,5835,5,2,2000,1,4,1,6),_NtcTrfShapePir_Type())
ntcTrfShapePir.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTrfShapePir.setStatus(_A)
class _NtcTrfShapeDestChannel_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_NtcTrfShapeDestChannel_Type.__name__=_E
_NtcTrfShapeDestChannel_Object=MibTableColumn
ntcTrfShapeDestChannel=_NtcTrfShapeDestChannel_Object((1,3,6,1,4,1,5835,5,2,2000,1,4,1,7),_NtcTrfShapeDestChannel_Type())
ntcTrfShapeDestChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTrfShapeDestChannel.setStatus(_A)
class _NtcTrfShapePrio_Type(Unsigned32):defaultValue=50
_NtcTrfShapePrio_Type.__name__=_H
_NtcTrfShapePrio_Object=MibTableColumn
ntcTrfShapePrio=_NtcTrfShapePrio_Object((1,3,6,1,4,1,5835,5,2,2000,1,4,1,8),_NtcTrfShapePrio_Type())
ntcTrfShapePrio.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTrfShapePrio.setStatus(_A)
class _NtcTrfMaxQTime_Type(Unsigned32):defaultValue=100
_NtcTrfMaxQTime_Type.__name__=_H
_NtcTrfMaxQTime_Object=MibTableColumn
ntcTrfMaxQTime=_NtcTrfMaxQTime_Object((1,3,6,1,4,1,5835,5,2,2000,1,4,1,9),_NtcTrfMaxQTime_Type())
ntcTrfMaxQTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTrfMaxQTime.setStatus(_A)
if mibBuilder.loadTexts:ntcTrfMaxQTime.setUnits('ms')
_NtcTrfShMonitor_ObjectIdentity=ObjectIdentity
ntcTrfShMonitor=_NtcTrfShMonitor_ObjectIdentity((1,3,6,1,4,1,5835,5,2,2000,1,5))
if mibBuilder.loadTexts:ntcTrfShMonitor.setStatus(_A)
_NtcTrfShMonFwdBytes_Type=Counter64
_NtcTrfShMonFwdBytes_Object=MibScalar
ntcTrfShMonFwdBytes=_NtcTrfShMonFwdBytes_Object((1,3,6,1,4,1,5835,5,2,2000,1,5,1),_NtcTrfShMonFwdBytes_Type())
ntcTrfShMonFwdBytes.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcTrfShMonFwdBytes.setStatus(_A)
if mibBuilder.loadTexts:ntcTrfShMonFwdBytes.setUnits(_K)
_NtcTrfShMonFwdPackets_Type=Counter64
_NtcTrfShMonFwdPackets_Object=MibScalar
ntcTrfShMonFwdPackets=_NtcTrfShMonFwdPackets_Object((1,3,6,1,4,1,5835,5,2,2000,1,5,2),_NtcTrfShMonFwdPackets_Type())
ntcTrfShMonFwdPackets.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcTrfShMonFwdPackets.setStatus(_A)
if mibBuilder.loadTexts:ntcTrfShMonFwdPackets.setUnits(_L)
_NtcTrfShMonDropBytes_Type=Counter64
_NtcTrfShMonDropBytes_Object=MibScalar
ntcTrfShMonDropBytes=_NtcTrfShMonDropBytes_Object((1,3,6,1,4,1,5835,5,2,2000,1,5,3),_NtcTrfShMonDropBytes_Type())
ntcTrfShMonDropBytes.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcTrfShMonDropBytes.setStatus(_A)
if mibBuilder.loadTexts:ntcTrfShMonDropBytes.setUnits(_K)
_NtcTrfShMonDropPackets_Type=Counter64
_NtcTrfShMonDropPackets_Object=MibScalar
ntcTrfShMonDropPackets=_NtcTrfShMonDropPackets_Object((1,3,6,1,4,1,5835,5,2,2000,1,5,4),_NtcTrfShMonDropPackets_Type())
ntcTrfShMonDropPackets.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcTrfShMonDropPackets.setStatus(_A)
if mibBuilder.loadTexts:ntcTrfShMonDropPackets.setUnits(_L)
_NtcTrfShMonShapingNodeTable_Object=MibTable
ntcTrfShMonShapingNodeTable=_NtcTrfShMonShapingNodeTable_Object((1,3,6,1,4,1,5835,5,2,2000,1,5,5))
if mibBuilder.loadTexts:ntcTrfShMonShapingNodeTable.setStatus(_A)
_NtcTrfShMonShapingNodeEntry_Object=MibTableRow
ntcTrfShMonShapingNodeEntry=_NtcTrfShMonShapingNodeEntry_Object((1,3,6,1,4,1,5835,5,2,2000,1,5,5,1))
ntcTrfShMonShapingNodeEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:ntcTrfShMonShapingNodeEntry.setStatus(_A)
_NtcTrfShMonShapingNodeInx_Type=Unsigned32
_NtcTrfShMonShapingNodeInx_Object=MibTableColumn
ntcTrfShMonShapingNodeInx=_NtcTrfShMonShapingNodeInx_Object((1,3,6,1,4,1,5835,5,2,2000,1,5,5,1,1),_NtcTrfShMonShapingNodeInx_Type())
ntcTrfShMonShapingNodeInx.setMaxAccess(_I)
if mibBuilder.loadTexts:ntcTrfShMonShapingNodeInx.setStatus(_A)
class _NtcTrfMonShNodeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_NtcTrfMonShNodeName_Type.__name__=_E
_NtcTrfMonShNodeName_Object=MibTableColumn
ntcTrfMonShNodeName=_NtcTrfMonShNodeName_Object((1,3,6,1,4,1,5835,5,2,2000,1,5,5,1,2),_NtcTrfMonShNodeName_Type())
ntcTrfMonShNodeName.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcTrfMonShNodeName.setStatus(_A)
_NtcTrfMonShNodeFwdByte_Type=Counter64
_NtcTrfMonShNodeFwdByte_Object=MibTableColumn
ntcTrfMonShNodeFwdByte=_NtcTrfMonShNodeFwdByte_Object((1,3,6,1,4,1,5835,5,2,2000,1,5,5,1,3),_NtcTrfMonShNodeFwdByte_Type())
ntcTrfMonShNodeFwdByte.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcTrfMonShNodeFwdByte.setStatus(_A)
_NtcTfrMonShNodeFwdPackets_Type=Counter64
_NtcTfrMonShNodeFwdPackets_Object=MibTableColumn
ntcTfrMonShNodeFwdPackets=_NtcTfrMonShNodeFwdPackets_Object((1,3,6,1,4,1,5835,5,2,2000,1,5,5,1,4),_NtcTfrMonShNodeFwdPackets_Type())
ntcTfrMonShNodeFwdPackets.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcTfrMonShNodeFwdPackets.setStatus(_A)
if mibBuilder.loadTexts:ntcTfrMonShNodeFwdPackets.setUnits(_L)
_NtcTrfMonShNodeDropByt_Type=Counter64
_NtcTrfMonShNodeDropByt_Object=MibTableColumn
ntcTrfMonShNodeDropByt=_NtcTrfMonShNodeDropByt_Object((1,3,6,1,4,1,5835,5,2,2000,1,5,5,1,5),_NtcTrfMonShNodeDropByt_Type())
ntcTrfMonShNodeDropByt.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcTrfMonShNodeDropByt.setStatus(_A)
if mibBuilder.loadTexts:ntcTrfMonShNodeDropByt.setUnits(_K)
_NtcTrfShapeNodeDropPackets_Type=Counter64
_NtcTrfShapeNodeDropPackets_Object=MibTableColumn
ntcTrfShapeNodeDropPackets=_NtcTrfShapeNodeDropPackets_Object((1,3,6,1,4,1,5835,5,2,2000,1,5,5,1,6),_NtcTrfShapeNodeDropPackets_Type())
ntcTrfShapeNodeDropPackets.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcTrfShapeNodeDropPackets.setStatus(_A)
if mibBuilder.loadTexts:ntcTrfShapeNodeDropPackets.setUnits(_L)
_NtcTrfShapeNodeAverageDelay_Type=Unsigned32
_NtcTrfShapeNodeAverageDelay_Object=MibTableColumn
ntcTrfShapeNodeAverageDelay=_NtcTrfShapeNodeAverageDelay_Object((1,3,6,1,4,1,5835,5,2,2000,1,5,5,1,7),_NtcTrfShapeNodeAverageDelay_Type())
ntcTrfShapeNodeAverageDelay.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcTrfShapeNodeAverageDelay.setStatus(_A)
if mibBuilder.loadTexts:ntcTrfShapeNodeAverageDelay.setUnits('ms')
_NtcTrfShapeNodeVolRate_Type=Counter64
_NtcTrfShapeNodeVolRate_Object=MibTableColumn
ntcTrfShapeNodeVolRate=_NtcTrfShapeNodeVolRate_Object((1,3,6,1,4,1,5835,5,2,2000,1,5,5,1,8),_NtcTrfShapeNodeVolRate_Type())
ntcTrfShapeNodeVolRate.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcTrfShapeNodeVolRate.setStatus(_A)
_NtcTrfShapeNodeDropRate_Type=Counter64
_NtcTrfShapeNodeDropRate_Object=MibTableColumn
ntcTrfShapeNodeDropRate=_NtcTrfShapeNodeDropRate_Object((1,3,6,1,4,1,5835,5,2,2000,1,5,5,1,9),_NtcTrfShapeNodeDropRate_Type())
ntcTrfShapeNodeDropRate.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcTrfShapeNodeDropRate.setStatus(_A)
if mibBuilder.loadTexts:ntcTrfShapeNodeDropRate.setUnits('bps')
class _NtcTrfShapeNodeVolUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),('symbols',1)))
_NtcTrfShapeNodeVolUnit_Type.__name__=_G
_NtcTrfShapeNodeVolUnit_Object=MibTableColumn
ntcTrfShapeNodeVolUnit=_NtcTrfShapeNodeVolUnit_Object((1,3,6,1,4,1,5835,5,2,2000,1,5,5,1,10),_NtcTrfShapeNodeVolUnit_Type())
ntcTrfShapeNodeVolUnit.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcTrfShapeNodeVolUnit.setStatus(_A)
class _NtcTrfShMonReset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('counting',0),('reset',1)))
_NtcTrfShMonReset_Type.__name__=_G
_NtcTrfShMonReset_Object=MibScalar
ntcTrfShMonReset=_NtcTrfShMonReset_Object((1,3,6,1,4,1,5835,5,2,2000,1,5,6),_NtcTrfShMonReset_Type())
ntcTrfShMonReset.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTrfShMonReset.setStatus(_A)
_NtcTrfShMonFwdBitRate_Type=Counter64
_NtcTrfShMonFwdBitRate_Object=MibScalar
ntcTrfShMonFwdBitRate=_NtcTrfShMonFwdBitRate_Object((1,3,6,1,4,1,5835,5,2,2000,1,5,7),_NtcTrfShMonFwdBitRate_Type())
ntcTrfShMonFwdBitRate.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcTrfShMonFwdBitRate.setStatus(_A)
if mibBuilder.loadTexts:ntcTrfShMonFwdBitRate.setUnits('bps')
_NtcTrfShExtClassifTable_Object=MibTable
ntcTrfShExtClassifTable=_NtcTrfShExtClassifTable_Object((1,3,6,1,4,1,5835,5,2,2000,1,6))
if mibBuilder.loadTexts:ntcTrfShExtClassifTable.setStatus(_A)
_NtcTrfShExtClassifEntry_Object=MibTableRow
ntcTrfShExtClassifEntry=_NtcTrfShExtClassifEntry_Object((1,3,6,1,4,1,5835,5,2,2000,1,6,1))
ntcTrfShExtClassifEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:ntcTrfShExtClassifEntry.setStatus(_A)
class _NtcTrfShExtClassifName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_NtcTrfShExtClassifName_Type.__name__=_E
_NtcTrfShExtClassifName_Object=MibTableColumn
ntcTrfShExtClassifName=_NtcTrfShExtClassifName_Object((1,3,6,1,4,1,5835,5,2,2000,1,6,1,1),_NtcTrfShExtClassifName_Type())
ntcTrfShExtClassifName.setMaxAccess(_I)
if mibBuilder.loadTexts:ntcTrfShExtClassifName.setStatus(_A)
_NtcTrfShExtClassifRowStatus_Type=RowStatus
_NtcTrfShExtClassifRowStatus_Object=MibTableColumn
ntcTrfShExtClassifRowStatus=_NtcTrfShExtClassifRowStatus_Object((1,3,6,1,4,1,5835,5,2,2000,1,6,1,2),_NtcTrfShExtClassifRowStatus_Type())
ntcTrfShExtClassifRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTrfShExtClassifRowStatus.setStatus(_A)
_NtcTrfShExtClassifEnable_Type=NtcEnable
_NtcTrfShExtClassifEnable_Object=MibTableColumn
ntcTrfShExtClassifEnable=_NtcTrfShExtClassifEnable_Object((1,3,6,1,4,1,5835,5,2,2000,1,6,1,3),_NtcTrfShExtClassifEnable_Type())
ntcTrfShExtClassifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTrfShExtClassifEnable.setStatus(_A)
class _NtcTrfShapeExtUseNetwAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_NtcTrfShapeExtUseNetwAddr_Type.__name__=_G
_NtcTrfShapeExtUseNetwAddr_Object=MibTableColumn
ntcTrfShapeExtUseNetwAddr=_NtcTrfShapeExtUseNetwAddr_Object((1,3,6,1,4,1,5835,5,2,2000,1,6,1,4),_NtcTrfShapeExtUseNetwAddr_Type())
ntcTrfShapeExtUseNetwAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTrfShapeExtUseNetwAddr.setStatus(_A)
_NtcTrfShapeExtNetwAddr_Type=NtcNetworkAddress
_NtcTrfShapeExtNetwAddr_Object=MibTableColumn
ntcTrfShapeExtNetwAddr=_NtcTrfShapeExtNetwAddr_Object((1,3,6,1,4,1,5835,5,2,2000,1,6,1,5),_NtcTrfShapeExtNetwAddr_Type())
ntcTrfShapeExtNetwAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTrfShapeExtNetwAddr.setStatus(_A)
class _NtcTrfShapeExtExpr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4000))
_NtcTrfShapeExtExpr_Type.__name__=_E
_NtcTrfShapeExtExpr_Object=MibTableColumn
ntcTrfShapeExtExpr=_NtcTrfShapeExtExpr_Object((1,3,6,1,4,1,5835,5,2,2000,1,6,1,6),_NtcTrfShapeExtExpr_Type())
ntcTrfShapeExtExpr.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTrfShapeExtExpr.setStatus(_A)
class _NtcTrfShapeExtShapingNode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_NtcTrfShapeExtShapingNode_Type.__name__=_E
_NtcTrfShapeExtShapingNode_Object=MibTableColumn
ntcTrfShapeExtShapingNode=_NtcTrfShapeExtShapingNode_Object((1,3,6,1,4,1,5835,5,2,2000,1,6,1,7),_NtcTrfShapeExtShapingNode_Type())
ntcTrfShapeExtShapingNode.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTrfShapeExtShapingNode.setStatus(_A)
class _NtcTrfShapeExtMatchingOrder_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_NtcTrfShapeExtMatchingOrder_Type.__name__=_H
_NtcTrfShapeExtMatchingOrder_Object=MibTableColumn
ntcTrfShapeExtMatchingOrder=_NtcTrfShapeExtMatchingOrder_Object((1,3,6,1,4,1,5835,5,2,2000,1,6,1,8),_NtcTrfShapeExtMatchingOrder_Type())
ntcTrfShapeExtMatchingOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTrfShapeExtMatchingOrder.setStatus(_A)
_NtcTrfShExtShapingNodeTable_Object=MibTable
ntcTrfShExtShapingNodeTable=_NtcTrfShExtShapingNodeTable_Object((1,3,6,1,4,1,5835,5,2,2000,1,7))
if mibBuilder.loadTexts:ntcTrfShExtShapingNodeTable.setStatus(_A)
_NtcTrfShExtShapingNodeEntry_Object=MibTableRow
ntcTrfShExtShapingNodeEntry=_NtcTrfShExtShapingNodeEntry_Object((1,3,6,1,4,1,5835,5,2,2000,1,7,1))
ntcTrfShExtShapingNodeEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:ntcTrfShExtShapingNodeEntry.setStatus(_A)
class _NtcTrfShExtShapingNodeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_NtcTrfShExtShapingNodeName_Type.__name__=_E
_NtcTrfShExtShapingNodeName_Object=MibTableColumn
ntcTrfShExtShapingNodeName=_NtcTrfShExtShapingNodeName_Object((1,3,6,1,4,1,5835,5,2,2000,1,7,1,1),_NtcTrfShExtShapingNodeName_Type())
ntcTrfShExtShapingNodeName.setMaxAccess(_I)
if mibBuilder.loadTexts:ntcTrfShExtShapingNodeName.setStatus(_A)
_NtcTrfShExtShapingNodeRowStatus_Type=RowStatus
_NtcTrfShExtShapingNodeRowStatus_Object=MibTableColumn
ntcTrfShExtShapingNodeRowStatus=_NtcTrfShExtShapingNodeRowStatus_Object((1,3,6,1,4,1,5835,5,2,2000,1,7,1,2),_NtcTrfShExtShapingNodeRowStatus_Type())
ntcTrfShExtShapingNodeRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTrfShExtShapingNodeRowStatus.setStatus(_A)
_NtcTrfShExtShapingNodeEnable_Type=NtcEnable
_NtcTrfShExtShapingNodeEnable_Object=MibTableColumn
ntcTrfShExtShapingNodeEnable=_NtcTrfShExtShapingNodeEnable_Object((1,3,6,1,4,1,5835,5,2,2000,1,7,1,3),_NtcTrfShExtShapingNodeEnable_Type())
ntcTrfShExtShapingNodeEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTrfShExtShapingNodeEnable.setStatus(_A)
class _NtcTrfShapeExtParentNam_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_NtcTrfShapeExtParentNam_Type.__name__=_E
_NtcTrfShapeExtParentNam_Object=MibTableColumn
ntcTrfShapeExtParentNam=_NtcTrfShapeExtParentNam_Object((1,3,6,1,4,1,5835,5,2,2000,1,7,1,4),_NtcTrfShapeExtParentNam_Type())
ntcTrfShapeExtParentNam.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTrfShapeExtParentNam.setStatus(_A)
_NtcTrfShapeExtCir_Type=Unsigned32
_NtcTrfShapeExtCir_Object=MibTableColumn
ntcTrfShapeExtCir=_NtcTrfShapeExtCir_Object((1,3,6,1,4,1,5835,5,2,2000,1,7,1,5),_NtcTrfShapeExtCir_Type())
ntcTrfShapeExtCir.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTrfShapeExtCir.setStatus(_A)
_NtcTrfShapeExtPir_Type=Unsigned32
_NtcTrfShapeExtPir_Object=MibTableColumn
ntcTrfShapeExtPir=_NtcTrfShapeExtPir_Object((1,3,6,1,4,1,5835,5,2,2000,1,7,1,6),_NtcTrfShapeExtPir_Type())
ntcTrfShapeExtPir.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTrfShapeExtPir.setStatus(_A)
class _NtcTrfShapeExtDestChan_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_NtcTrfShapeExtDestChan_Type.__name__=_E
_NtcTrfShapeExtDestChan_Object=MibTableColumn
ntcTrfShapeExtDestChan=_NtcTrfShapeExtDestChan_Object((1,3,6,1,4,1,5835,5,2,2000,1,7,1,7),_NtcTrfShapeExtDestChan_Type())
ntcTrfShapeExtDestChan.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTrfShapeExtDestChan.setStatus(_A)
_NtcTrfShapeExtPrio_Type=Unsigned32
_NtcTrfShapeExtPrio_Object=MibTableColumn
ntcTrfShapeExtPrio=_NtcTrfShapeExtPrio_Object((1,3,6,1,4,1,5835,5,2,2000,1,7,1,8),_NtcTrfShapeExtPrio_Type())
ntcTrfShapeExtPrio.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTrfShapeExtPrio.setStatus(_A)
_NtcTrfMaxQTExtime_Type=Unsigned32
_NtcTrfMaxQTExtime_Object=MibTableColumn
ntcTrfMaxQTExtime=_NtcTrfMaxQTExtime_Object((1,3,6,1,4,1,5835,5,2,2000,1,7,1,9),_NtcTrfMaxQTExtime_Type())
ntcTrfMaxQTExtime.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTrfMaxQTExtime.setStatus(_A)
if mibBuilder.loadTexts:ntcTrfMaxQTExtime.setUnits('ms')
class _NtcTrfShapeUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('bitrate',0),('symbolrate',1)))
_NtcTrfShapeUnit_Type.__name__=_G
_NtcTrfShapeUnit_Object=MibTableColumn
ntcTrfShapeUnit=_NtcTrfShapeUnit_Object((1,3,6,1,4,1,5835,5,2,2000,1,7,1,10),_NtcTrfShapeUnit_Type())
ntcTrfShapeUnit.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTrfShapeUnit.setStatus(_A)
_NtcTrfShapeConformance_ObjectIdentity=ObjectIdentity
ntcTrfShapeConformance=_NtcTrfShapeConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,2000,2))
if mibBuilder.loadTexts:ntcTrfShapeConformance.setStatus(_A)
_NtcTrfShapeConfCompliance_ObjectIdentity=ObjectIdentity
ntcTrfShapeConfCompliance=_NtcTrfShapeConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,2000,2,1))
if mibBuilder.loadTexts:ntcTrfShapeConfCompliance.setStatus(_A)
_NtcTrfShapeConfGroup_ObjectIdentity=ObjectIdentity
ntcTrfShapeConfGroup=_NtcTrfShapeConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,2000,2,2))
if mibBuilder.loadTexts:ntcTrfShapeConfGroup.setStatus(_A)
ntcTrfShapeConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,2000,2,2,1))
ntcTrfShapeConfGrpV1Standard.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:ntcTrfShapeConfGrpV1Standard.setStatus(_A)
ntcTrfShapeConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,2000,2,1,1))
ntcTrfShapeConfCompV1Standard.setObjects((_B,_AD))
if mibBuilder.loadTexts:ntcTrfShapeConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcTrafficShaper':ntcTrafficShaper,'ntcTrfShapeObjects':ntcTrfShapeObjects,_S:ntcTrfShEnable,_T:ntcTrfShInputSelection,'ntcTrfShClassificationTable':ntcTrfShClassificationTable,'ntcTrfShClassificationEntry':ntcTrfShClassificationEntry,_N:ntcTrfShClassificationInx,_U:ntcTrfShapeClassifName,_V:ntcTrfShClassificationEnable,_W:ntcTrfShapeUseNetwAddress,_X:ntcTrfShapeNetwAddress,_Y:ntcTrfShapeExpr,_Z:ntcTrfShapeShapingNode,'ntcTrfShShapingNodeTable':ntcTrfShShapingNodeTable,'ntcTrfShShapingNodeEntry':ntcTrfShShapingNodeEntry,_O:ntcTrfShShapingNodeInx,_a:ntcTrfShapeNodeName,_b:ntcTrfShShapingNodeEnable,_c:ntcTrfShapeParentName,_d:ntcTrfShapeCir,_e:ntcTrfShapePir,_f:ntcTrfShapeDestChannel,_g:ntcTrfShapePrio,_h:ntcTrfMaxQTime,'ntcTrfShMonitor':ntcTrfShMonitor,_i:ntcTrfShMonFwdBytes,_j:ntcTrfShMonFwdPackets,_k:ntcTrfShMonDropBytes,_l:ntcTrfShMonDropPackets,'ntcTrfShMonShapingNodeTable':ntcTrfShMonShapingNodeTable,'ntcTrfShMonShapingNodeEntry':ntcTrfShMonShapingNodeEntry,_P:ntcTrfShMonShapingNodeInx,_m:ntcTrfMonShNodeName,_n:ntcTrfMonShNodeFwdByte,_o:ntcTfrMonShNodeFwdPackets,_p:ntcTrfMonShNodeDropByt,_q:ntcTrfShapeNodeDropPackets,_r:ntcTrfShapeNodeAverageDelay,_s:ntcTrfShapeNodeVolRate,_t:ntcTrfShapeNodeDropRate,_u:ntcTrfShapeNodeVolUnit,_v:ntcTrfShMonReset,_w:ntcTrfShMonFwdBitRate,'ntcTrfShExtClassifTable':ntcTrfShExtClassifTable,'ntcTrfShExtClassifEntry':ntcTrfShExtClassifEntry,_Q:ntcTrfShExtClassifName,_x:ntcTrfShExtClassifRowStatus,_y:ntcTrfShExtClassifEnable,_z:ntcTrfShapeExtUseNetwAddr,_A0:ntcTrfShapeExtNetwAddr,_A1:ntcTrfShapeExtExpr,_A2:ntcTrfShapeExtShapingNode,_A3:ntcTrfShapeExtMatchingOrder,'ntcTrfShExtShapingNodeTable':ntcTrfShExtShapingNodeTable,'ntcTrfShExtShapingNodeEntry':ntcTrfShExtShapingNodeEntry,_R:ntcTrfShExtShapingNodeName,_A4:ntcTrfShExtShapingNodeRowStatus,_A5:ntcTrfShExtShapingNodeEnable,_A6:ntcTrfShapeExtParentNam,_A7:ntcTrfShapeExtCir,_A8:ntcTrfShapeExtPir,_A9:ntcTrfShapeExtDestChan,_AA:ntcTrfShapeExtPrio,_AB:ntcTrfMaxQTExtime,_AC:ntcTrfShapeUnit,'ntcTrfShapeConformance':ntcTrfShapeConformance,'ntcTrfShapeConfCompliance':ntcTrfShapeConfCompliance,'ntcTrfShapeConfCompV1Standard':ntcTrfShapeConfCompV1Standard,'ntcTrfShapeConfGroup':ntcTrfShapeConfGroup,_AD:ntcTrfShapeConfGrpV1Standard})