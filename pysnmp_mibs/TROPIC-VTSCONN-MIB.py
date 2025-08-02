_A2='tnEgressVtsCmodeMapGroup'
_A1='tnIngressVtsCmodeMapGroup'
_A0='tnEgressVtsMapGroup'
_z='tnIngressVtsMapGroup'
_y='tnVtsConnIdGroup'
_x='tnVtsMapGroup'
_w='tnVtsConnGroup'
_v='tnEgressVtsCmodeMapRowStatus'
_u='tnEgressVtsCmodeMapCMode'
_t='tnEgressVtsCmodeMapDIP'
_s='tnEgressVtsCmodeMapSIP'
_r='tnEgressVtsCmodeMapSVLANID'
_q='tnEgressVtsCmodeMapCEVLANID'
_p='tnIngressVtsCmodeMapRowStatus'
_o='tnIngressVtsCmodeMapCMode'
_n='tnIngressVtsCmodeMapDIP'
_m='tnIngressVtsCmodeMapSIP'
_l='tnIngressVtsCmodeMapSVLANID'
_k='tnIngressVtsCmodeMapCEVLANID'
_j='tnEgressVtsMapSVLANID'
_i='tnEgressVtsMapCEVLANID'
_h='tnIngressVtsMapSVLANID'
_g='tnIngressVtsMapCEVLANID'
_f='tnVtsConnIdDestVts'
_e='tnVtsConnIdDestIfIndex'
_d='tnVtsConnIdSrcVts'
_c='tnVtsConnIdSrcIfIndex'
_b='tnVtsMapSVLANID'
_a='tnVtsMapCEVLANID'
_Z='tnVtsConnProtectionState'
_Y='tnVtsConnRowStatus'
_X='tnVtsConnEBS'
_W='tnVtsConnCBS'
_V='tnVtsConnEIR'
_U='tnVtsConnCIR'
_T='tnVtsConnName'
_S='tnVtsConnBidirectional'
_R='tnVtsConnOperState'
_Q='tnVtsConnAdminState'
_P='tnVtsConnDestVts'
_O='tnVtsConnDestIfIndex'
_N='tnVtsConnSrcVts'
_M='tnVtsConnSrcIfIndex'
_L='TruthValue'
_K='tnVtsConnId'
_J='Integer32'
_I='Unsigned32'
_H='tnVtsMapVts'
_G='tnVtsMapIfIndex'
_F='not-accessible'
_E='read-only'
_D='OctetString'
_C='read-create'
_B='TROPIC-VTSCONN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_L)
tnPortModules,tnVtsConnMIB=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnPortModules','tnVtsConnMIB')
tnVtsConnMibModule=ModuleIdentity((1,3,6,1,4,1,7483,1,1,2,2,4,4))
if mibBuilder.loadTexts:tnVtsConnMibModule.setRevisions(('2018-02-23 12:00','2016-11-16 12:00','2011-02-25 12:00','2011-02-22 12:00','2010-10-26 12:00','2010-10-14 12:00','2010-06-23 12:00','2010-06-04 12:00','2010-05-18 12:00','2010-03-03 12:00','2009-07-17 12:00','2009-07-07 12:00','2009-06-18 12:00','2009-05-31 12:00','2009-04-27 12:00'))
class AluWdmVtsCmodeMapCMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('cvlan',1),('svlan',2),('sip',3),('dip',4),('sipdip',5),('port',6),('untagged',7)))
_TnVtsConnConf_ObjectIdentity=ObjectIdentity
tnVtsConnConf=_TnVtsConnConf_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,6,1))
_TnVtsConnGroups_ObjectIdentity=ObjectIdentity
tnVtsConnGroups=_TnVtsConnGroups_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,6,1,1))
_TnVtsConnCompliances_ObjectIdentity=ObjectIdentity
tnVtsConnCompliances=_TnVtsConnCompliances_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,6,1,2))
_TnVtsConnObjs_ObjectIdentity=ObjectIdentity
tnVtsConnObjs=_TnVtsConnObjs_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,6,2))
_TnVtsConnBasics_ObjectIdentity=ObjectIdentity
tnVtsConnBasics=_TnVtsConnBasics_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,6,2,1))
_TnVtsConnTable_Object=MibTable
tnVtsConnTable=_TnVtsConnTable_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,1))
if mibBuilder.loadTexts:tnVtsConnTable.setStatus(_A)
_TnVtsConnEntry_Object=MibTableRow
tnVtsConnEntry=_TnVtsConnEntry_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,1,1))
tnVtsConnEntry.setIndexNames((0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:tnVtsConnEntry.setStatus(_A)
_TnVtsConnSrcIfIndex_Type=InterfaceIndex
_TnVtsConnSrcIfIndex_Object=MibTableColumn
tnVtsConnSrcIfIndex=_TnVtsConnSrcIfIndex_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,1,1,1),_TnVtsConnSrcIfIndex_Type())
tnVtsConnSrcIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:tnVtsConnSrcIfIndex.setStatus(_A)
_TnVtsConnSrcVts_Type=Unsigned32
_TnVtsConnSrcVts_Object=MibTableColumn
tnVtsConnSrcVts=_TnVtsConnSrcVts_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,1,1,2),_TnVtsConnSrcVts_Type())
tnVtsConnSrcVts.setMaxAccess(_F)
if mibBuilder.loadTexts:tnVtsConnSrcVts.setStatus(_A)
_TnVtsConnDestIfIndex_Type=InterfaceIndex
_TnVtsConnDestIfIndex_Object=MibTableColumn
tnVtsConnDestIfIndex=_TnVtsConnDestIfIndex_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,1,1,3),_TnVtsConnDestIfIndex_Type())
tnVtsConnDestIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:tnVtsConnDestIfIndex.setStatus(_A)
_TnVtsConnDestVts_Type=Unsigned32
_TnVtsConnDestVts_Object=MibTableColumn
tnVtsConnDestVts=_TnVtsConnDestVts_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,1,1,4),_TnVtsConnDestVts_Type())
tnVtsConnDestVts.setMaxAccess(_F)
if mibBuilder.loadTexts:tnVtsConnDestVts.setStatus(_A)
class _TnVtsConnAdminState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_TnVtsConnAdminState_Type.__name__=_J
_TnVtsConnAdminState_Object=MibTableColumn
tnVtsConnAdminState=_TnVtsConnAdminState_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,1,1,5),_TnVtsConnAdminState_Type())
tnVtsConnAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:tnVtsConnAdminState.setStatus(_A)
class _TnVtsConnOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_TnVtsConnOperState_Type.__name__=_J
_TnVtsConnOperState_Object=MibTableColumn
tnVtsConnOperState=_TnVtsConnOperState_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,1,1,6),_TnVtsConnOperState_Type())
tnVtsConnOperState.setMaxAccess(_E)
if mibBuilder.loadTexts:tnVtsConnOperState.setStatus(_A)
class _TnVtsConnBidirectional_Type(TruthValue):defaultValue=1
_TnVtsConnBidirectional_Type.__name__=_L
_TnVtsConnBidirectional_Object=MibTableColumn
tnVtsConnBidirectional=_TnVtsConnBidirectional_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,1,1,7),_TnVtsConnBidirectional_Type())
tnVtsConnBidirectional.setMaxAccess(_C)
if mibBuilder.loadTexts:tnVtsConnBidirectional.setStatus(_A)
class _TnVtsConnName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_TnVtsConnName_Type.__name__=_D
_TnVtsConnName_Object=MibTableColumn
tnVtsConnName=_TnVtsConnName_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,1,1,8),_TnVtsConnName_Type())
tnVtsConnName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnVtsConnName.setStatus(_A)
class _TnVtsConnCIR_Type(Unsigned32):defaultValue=100
_TnVtsConnCIR_Type.__name__=_I
_TnVtsConnCIR_Object=MibTableColumn
tnVtsConnCIR=_TnVtsConnCIR_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,1,1,9),_TnVtsConnCIR_Type())
tnVtsConnCIR.setMaxAccess(_C)
if mibBuilder.loadTexts:tnVtsConnCIR.setStatus(_A)
class _TnVtsConnEIR_Type(Unsigned32):defaultValue=1000
_TnVtsConnEIR_Type.__name__=_I
_TnVtsConnEIR_Object=MibTableColumn
tnVtsConnEIR=_TnVtsConnEIR_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,1,1,10),_TnVtsConnEIR_Type())
tnVtsConnEIR.setMaxAccess(_C)
if mibBuilder.loadTexts:tnVtsConnEIR.setStatus(_A)
class _TnVtsConnCBS_Type(Unsigned32):defaultValue=256
_TnVtsConnCBS_Type.__name__=_I
_TnVtsConnCBS_Object=MibTableColumn
tnVtsConnCBS=_TnVtsConnCBS_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,1,1,11),_TnVtsConnCBS_Type())
tnVtsConnCBS.setMaxAccess(_C)
if mibBuilder.loadTexts:tnVtsConnCBS.setStatus(_A)
class _TnVtsConnEBS_Type(Unsigned32):defaultValue=4096
_TnVtsConnEBS_Type.__name__=_I
_TnVtsConnEBS_Object=MibTableColumn
tnVtsConnEBS=_TnVtsConnEBS_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,1,1,12),_TnVtsConnEBS_Type())
tnVtsConnEBS.setMaxAccess(_C)
if mibBuilder.loadTexts:tnVtsConnEBS.setStatus(_A)
_TnVtsConnRowStatus_Type=RowStatus
_TnVtsConnRowStatus_Object=MibTableColumn
tnVtsConnRowStatus=_TnVtsConnRowStatus_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,1,1,13),_TnVtsConnRowStatus_Type())
tnVtsConnRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnVtsConnRowStatus.setStatus(_A)
_TnVtsConnId_Type=Unsigned32
_TnVtsConnId_Object=MibTableColumn
tnVtsConnId=_TnVtsConnId_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,1,1,14),_TnVtsConnId_Type())
tnVtsConnId.setMaxAccess(_E)
if mibBuilder.loadTexts:tnVtsConnId.setStatus(_A)
class _TnVtsConnProtectionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('working',2),('protection',3)))
_TnVtsConnProtectionState_Type.__name__=_J
_TnVtsConnProtectionState_Object=MibTableColumn
tnVtsConnProtectionState=_TnVtsConnProtectionState_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,1,1,15),_TnVtsConnProtectionState_Type())
tnVtsConnProtectionState.setMaxAccess(_E)
if mibBuilder.loadTexts:tnVtsConnProtectionState.setStatus(_A)
_TnVtsMapTable_Object=MibTable
tnVtsMapTable=_TnVtsMapTable_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,2))
if mibBuilder.loadTexts:tnVtsMapTable.setStatus(_A)
_TnVtsMapEntry_Object=MibTableRow
tnVtsMapEntry=_TnVtsMapEntry_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,2,1))
tnVtsMapEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:tnVtsMapEntry.setStatus(_A)
_TnVtsMapIfIndex_Type=InterfaceIndex
_TnVtsMapIfIndex_Object=MibTableColumn
tnVtsMapIfIndex=_TnVtsMapIfIndex_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,2,1,1),_TnVtsMapIfIndex_Type())
tnVtsMapIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:tnVtsMapIfIndex.setStatus(_A)
_TnVtsMapVts_Type=Unsigned32
_TnVtsMapVts_Object=MibTableColumn
tnVtsMapVts=_TnVtsMapVts_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,2,1,2),_TnVtsMapVts_Type())
tnVtsMapVts.setMaxAccess(_F)
if mibBuilder.loadTexts:tnVtsMapVts.setStatus(_A)
class _TnVtsMapCEVLANID_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_TnVtsMapCEVLANID_Type.__name__=_D
_TnVtsMapCEVLANID_Object=MibTableColumn
tnVtsMapCEVLANID=_TnVtsMapCEVLANID_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,2,1,3),_TnVtsMapCEVLANID_Type())
tnVtsMapCEVLANID.setMaxAccess(_C)
if mibBuilder.loadTexts:tnVtsMapCEVLANID.setStatus(_A)
_TnVtsMapSVLANID_Type=Unsigned32
_TnVtsMapSVLANID_Object=MibTableColumn
tnVtsMapSVLANID=_TnVtsMapSVLANID_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,2,1,5),_TnVtsMapSVLANID_Type())
tnVtsMapSVLANID.setMaxAccess(_C)
if mibBuilder.loadTexts:tnVtsMapSVLANID.setStatus(_A)
_TnVtsConnIdTable_Object=MibTable
tnVtsConnIdTable=_TnVtsConnIdTable_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,3))
if mibBuilder.loadTexts:tnVtsConnIdTable.setStatus(_A)
_TnVtsConnIdEntry_Object=MibTableRow
tnVtsConnIdEntry=_TnVtsConnIdEntry_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,3,1))
tnVtsConnIdEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:tnVtsConnIdEntry.setStatus(_A)
_TnVtsConnIdSrcIfIndex_Type=InterfaceIndex
_TnVtsConnIdSrcIfIndex_Object=MibTableColumn
tnVtsConnIdSrcIfIndex=_TnVtsConnIdSrcIfIndex_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,3,1,1),_TnVtsConnIdSrcIfIndex_Type())
tnVtsConnIdSrcIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:tnVtsConnIdSrcIfIndex.setStatus(_A)
_TnVtsConnIdSrcVts_Type=Unsigned32
_TnVtsConnIdSrcVts_Object=MibTableColumn
tnVtsConnIdSrcVts=_TnVtsConnIdSrcVts_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,3,1,2),_TnVtsConnIdSrcVts_Type())
tnVtsConnIdSrcVts.setMaxAccess(_E)
if mibBuilder.loadTexts:tnVtsConnIdSrcVts.setStatus(_A)
_TnVtsConnIdDestIfIndex_Type=InterfaceIndex
_TnVtsConnIdDestIfIndex_Object=MibTableColumn
tnVtsConnIdDestIfIndex=_TnVtsConnIdDestIfIndex_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,3,1,3),_TnVtsConnIdDestIfIndex_Type())
tnVtsConnIdDestIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:tnVtsConnIdDestIfIndex.setStatus(_A)
_TnVtsConnIdDestVts_Type=Unsigned32
_TnVtsConnIdDestVts_Object=MibTableColumn
tnVtsConnIdDestVts=_TnVtsConnIdDestVts_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,3,1,4),_TnVtsConnIdDestVts_Type())
tnVtsConnIdDestVts.setMaxAccess(_E)
if mibBuilder.loadTexts:tnVtsConnIdDestVts.setStatus(_A)
_TnIngressVtsMapTable_Object=MibTable
tnIngressVtsMapTable=_TnIngressVtsMapTable_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,4))
if mibBuilder.loadTexts:tnIngressVtsMapTable.setStatus(_A)
_TnIngressVtsMapEntry_Object=MibTableRow
tnIngressVtsMapEntry=_TnIngressVtsMapEntry_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,4,1))
tnIngressVtsMapEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:tnIngressVtsMapEntry.setStatus(_A)
class _TnIngressVtsMapCEVLANID_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_TnIngressVtsMapCEVLANID_Type.__name__=_D
_TnIngressVtsMapCEVLANID_Object=MibTableColumn
tnIngressVtsMapCEVLANID=_TnIngressVtsMapCEVLANID_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,4,1,1),_TnIngressVtsMapCEVLANID_Type())
tnIngressVtsMapCEVLANID.setMaxAccess(_C)
if mibBuilder.loadTexts:tnIngressVtsMapCEVLANID.setStatus(_A)
_TnIngressVtsMapSVLANID_Type=Unsigned32
_TnIngressVtsMapSVLANID_Object=MibTableColumn
tnIngressVtsMapSVLANID=_TnIngressVtsMapSVLANID_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,4,1,2),_TnIngressVtsMapSVLANID_Type())
tnIngressVtsMapSVLANID.setMaxAccess(_C)
if mibBuilder.loadTexts:tnIngressVtsMapSVLANID.setStatus(_A)
_TnEgressVtsMapTable_Object=MibTable
tnEgressVtsMapTable=_TnEgressVtsMapTable_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,5))
if mibBuilder.loadTexts:tnEgressVtsMapTable.setStatus(_A)
_TnEgressVtsMapEntry_Object=MibTableRow
tnEgressVtsMapEntry=_TnEgressVtsMapEntry_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,5,1))
tnEgressVtsMapEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:tnEgressVtsMapEntry.setStatus(_A)
class _TnEgressVtsMapCEVLANID_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_TnEgressVtsMapCEVLANID_Type.__name__=_D
_TnEgressVtsMapCEVLANID_Object=MibTableColumn
tnEgressVtsMapCEVLANID=_TnEgressVtsMapCEVLANID_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,5,1,1),_TnEgressVtsMapCEVLANID_Type())
tnEgressVtsMapCEVLANID.setMaxAccess(_C)
if mibBuilder.loadTexts:tnEgressVtsMapCEVLANID.setStatus(_A)
_TnEgressVtsMapSVLANID_Type=Unsigned32
_TnEgressVtsMapSVLANID_Object=MibTableColumn
tnEgressVtsMapSVLANID=_TnEgressVtsMapSVLANID_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,5,1,2),_TnEgressVtsMapSVLANID_Type())
tnEgressVtsMapSVLANID.setMaxAccess(_C)
if mibBuilder.loadTexts:tnEgressVtsMapSVLANID.setStatus(_A)
_TnIngressVtsCmodeMapTable_Object=MibTable
tnIngressVtsCmodeMapTable=_TnIngressVtsCmodeMapTable_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,6))
if mibBuilder.loadTexts:tnIngressVtsCmodeMapTable.setStatus(_A)
_TnIngressVtsCmodeMapEntry_Object=MibTableRow
tnIngressVtsCmodeMapEntry=_TnIngressVtsCmodeMapEntry_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,6,1))
tnIngressVtsCmodeMapEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:tnIngressVtsCmodeMapEntry.setStatus(_A)
class _TnIngressVtsCmodeMapCEVLANID_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_TnIngressVtsCmodeMapCEVLANID_Type.__name__=_D
_TnIngressVtsCmodeMapCEVLANID_Object=MibTableColumn
tnIngressVtsCmodeMapCEVLANID=_TnIngressVtsCmodeMapCEVLANID_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,6,1,1),_TnIngressVtsCmodeMapCEVLANID_Type())
tnIngressVtsCmodeMapCEVLANID.setMaxAccess(_C)
if mibBuilder.loadTexts:tnIngressVtsCmodeMapCEVLANID.setStatus(_A)
_TnIngressVtsCmodeMapSVLANID_Type=Unsigned32
_TnIngressVtsCmodeMapSVLANID_Object=MibTableColumn
tnIngressVtsCmodeMapSVLANID=_TnIngressVtsCmodeMapSVLANID_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,6,1,2),_TnIngressVtsCmodeMapSVLANID_Type())
tnIngressVtsCmodeMapSVLANID.setMaxAccess(_C)
if mibBuilder.loadTexts:tnIngressVtsCmodeMapSVLANID.setStatus(_A)
_TnIngressVtsCmodeMapSIP_Type=IpAddress
_TnIngressVtsCmodeMapSIP_Object=MibTableColumn
tnIngressVtsCmodeMapSIP=_TnIngressVtsCmodeMapSIP_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,6,1,3),_TnIngressVtsCmodeMapSIP_Type())
tnIngressVtsCmodeMapSIP.setMaxAccess(_C)
if mibBuilder.loadTexts:tnIngressVtsCmodeMapSIP.setStatus(_A)
_TnIngressVtsCmodeMapDIP_Type=IpAddress
_TnIngressVtsCmodeMapDIP_Object=MibTableColumn
tnIngressVtsCmodeMapDIP=_TnIngressVtsCmodeMapDIP_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,6,1,4),_TnIngressVtsCmodeMapDIP_Type())
tnIngressVtsCmodeMapDIP.setMaxAccess(_C)
if mibBuilder.loadTexts:tnIngressVtsCmodeMapDIP.setStatus(_A)
_TnIngressVtsCmodeMapCMode_Type=AluWdmVtsCmodeMapCMode
_TnIngressVtsCmodeMapCMode_Object=MibTableColumn
tnIngressVtsCmodeMapCMode=_TnIngressVtsCmodeMapCMode_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,6,1,5),_TnIngressVtsCmodeMapCMode_Type())
tnIngressVtsCmodeMapCMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tnIngressVtsCmodeMapCMode.setStatus(_A)
_TnIngressVtsCmodeMapRowStatus_Type=RowStatus
_TnIngressVtsCmodeMapRowStatus_Object=MibTableColumn
tnIngressVtsCmodeMapRowStatus=_TnIngressVtsCmodeMapRowStatus_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,6,1,6),_TnIngressVtsCmodeMapRowStatus_Type())
tnIngressVtsCmodeMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnIngressVtsCmodeMapRowStatus.setStatus(_A)
_TnEgressVtsCmodeMapTable_Object=MibTable
tnEgressVtsCmodeMapTable=_TnEgressVtsCmodeMapTable_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,7))
if mibBuilder.loadTexts:tnEgressVtsCmodeMapTable.setStatus(_A)
_TnEgressVtsCmodeMapEntry_Object=MibTableRow
tnEgressVtsCmodeMapEntry=_TnEgressVtsCmodeMapEntry_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,7,1))
tnEgressVtsCmodeMapEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:tnEgressVtsCmodeMapEntry.setStatus(_A)
class _TnEgressVtsCmodeMapCEVLANID_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_TnEgressVtsCmodeMapCEVLANID_Type.__name__=_D
_TnEgressVtsCmodeMapCEVLANID_Object=MibTableColumn
tnEgressVtsCmodeMapCEVLANID=_TnEgressVtsCmodeMapCEVLANID_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,7,1,1),_TnEgressVtsCmodeMapCEVLANID_Type())
tnEgressVtsCmodeMapCEVLANID.setMaxAccess(_C)
if mibBuilder.loadTexts:tnEgressVtsCmodeMapCEVLANID.setStatus(_A)
_TnEgressVtsCmodeMapSVLANID_Type=Unsigned32
_TnEgressVtsCmodeMapSVLANID_Object=MibTableColumn
tnEgressVtsCmodeMapSVLANID=_TnEgressVtsCmodeMapSVLANID_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,7,1,2),_TnEgressVtsCmodeMapSVLANID_Type())
tnEgressVtsCmodeMapSVLANID.setMaxAccess(_C)
if mibBuilder.loadTexts:tnEgressVtsCmodeMapSVLANID.setStatus(_A)
_TnEgressVtsCmodeMapSIP_Type=IpAddress
_TnEgressVtsCmodeMapSIP_Object=MibTableColumn
tnEgressVtsCmodeMapSIP=_TnEgressVtsCmodeMapSIP_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,7,1,3),_TnEgressVtsCmodeMapSIP_Type())
tnEgressVtsCmodeMapSIP.setMaxAccess(_C)
if mibBuilder.loadTexts:tnEgressVtsCmodeMapSIP.setStatus(_A)
_TnEgressVtsCmodeMapDIP_Type=IpAddress
_TnEgressVtsCmodeMapDIP_Object=MibTableColumn
tnEgressVtsCmodeMapDIP=_TnEgressVtsCmodeMapDIP_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,7,1,4),_TnEgressVtsCmodeMapDIP_Type())
tnEgressVtsCmodeMapDIP.setMaxAccess(_C)
if mibBuilder.loadTexts:tnEgressVtsCmodeMapDIP.setStatus(_A)
_TnEgressVtsCmodeMapCMode_Type=AluWdmVtsCmodeMapCMode
_TnEgressVtsCmodeMapCMode_Object=MibTableColumn
tnEgressVtsCmodeMapCMode=_TnEgressVtsCmodeMapCMode_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,7,1,5),_TnEgressVtsCmodeMapCMode_Type())
tnEgressVtsCmodeMapCMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tnEgressVtsCmodeMapCMode.setStatus(_A)
_TnEgressVtsCmodeMapRowStatus_Type=RowStatus
_TnEgressVtsCmodeMapRowStatus_Object=MibTableColumn
tnEgressVtsCmodeMapRowStatus=_TnEgressVtsCmodeMapRowStatus_Object((1,3,6,1,4,1,7483,2,2,4,6,2,1,7,1,6),_TnEgressVtsCmodeMapRowStatus_Type())
tnEgressVtsCmodeMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnEgressVtsCmodeMapRowStatus.setStatus(_A)
tnVtsConnGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,4,6,1,1,1))
tnVtsConnGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_K),(_B,_Z)))
if mibBuilder.loadTexts:tnVtsConnGroup.setStatus(_A)
tnVtsMapGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,4,6,1,1,2))
tnVtsMapGroup.setObjects(*((_B,_a),(_B,_b)))
if mibBuilder.loadTexts:tnVtsMapGroup.setStatus(_A)
tnVtsConnIdGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,4,6,1,1,3))
tnVtsConnIdGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:tnVtsConnIdGroup.setStatus(_A)
tnIngressVtsMapGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,4,6,1,1,4))
tnIngressVtsMapGroup.setObjects(*((_B,_g),(_B,_h)))
if mibBuilder.loadTexts:tnIngressVtsMapGroup.setStatus(_A)
tnEgressVtsMapGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,4,6,1,1,5))
tnEgressVtsMapGroup.setObjects(*((_B,_i),(_B,_j)))
if mibBuilder.loadTexts:tnEgressVtsMapGroup.setStatus(_A)
tnIngressVtsCmodeMapGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,4,6,1,1,6))
tnIngressVtsCmodeMapGroup.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:tnIngressVtsCmodeMapGroup.setStatus(_A)
tnEgressVtsCmodeMapGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,4,6,1,1,7))
tnEgressVtsCmodeMapGroup.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:tnEgressVtsCmodeMapGroup.setStatus(_A)
tnVtsConnCompliance=ModuleCompliance((1,3,6,1,4,1,7483,2,2,4,6,1,2,1))
tnVtsConnCompliance.setObjects(*((_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:tnVtsConnCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AluWdmVtsCmodeMapCMode':AluWdmVtsCmodeMapCMode,'tnVtsConnMibModule':tnVtsConnMibModule,'tnVtsConnConf':tnVtsConnConf,'tnVtsConnGroups':tnVtsConnGroups,_w:tnVtsConnGroup,_x:tnVtsMapGroup,_y:tnVtsConnIdGroup,_z:tnIngressVtsMapGroup,_A0:tnEgressVtsMapGroup,_A1:tnIngressVtsCmodeMapGroup,_A2:tnEgressVtsCmodeMapGroup,'tnVtsConnCompliances':tnVtsConnCompliances,'tnVtsConnCompliance':tnVtsConnCompliance,'tnVtsConnObjs':tnVtsConnObjs,'tnVtsConnBasics':tnVtsConnBasics,'tnVtsConnTable':tnVtsConnTable,'tnVtsConnEntry':tnVtsConnEntry,_M:tnVtsConnSrcIfIndex,_N:tnVtsConnSrcVts,_O:tnVtsConnDestIfIndex,_P:tnVtsConnDestVts,_Q:tnVtsConnAdminState,_R:tnVtsConnOperState,_S:tnVtsConnBidirectional,_T:tnVtsConnName,_U:tnVtsConnCIR,_V:tnVtsConnEIR,_W:tnVtsConnCBS,_X:tnVtsConnEBS,_Y:tnVtsConnRowStatus,_K:tnVtsConnId,_Z:tnVtsConnProtectionState,'tnVtsMapTable':tnVtsMapTable,'tnVtsMapEntry':tnVtsMapEntry,_G:tnVtsMapIfIndex,_H:tnVtsMapVts,_a:tnVtsMapCEVLANID,_b:tnVtsMapSVLANID,'tnVtsConnIdTable':tnVtsConnIdTable,'tnVtsConnIdEntry':tnVtsConnIdEntry,_c:tnVtsConnIdSrcIfIndex,_d:tnVtsConnIdSrcVts,_e:tnVtsConnIdDestIfIndex,_f:tnVtsConnIdDestVts,'tnIngressVtsMapTable':tnIngressVtsMapTable,'tnIngressVtsMapEntry':tnIngressVtsMapEntry,_g:tnIngressVtsMapCEVLANID,_h:tnIngressVtsMapSVLANID,'tnEgressVtsMapTable':tnEgressVtsMapTable,'tnEgressVtsMapEntry':tnEgressVtsMapEntry,_i:tnEgressVtsMapCEVLANID,_j:tnEgressVtsMapSVLANID,'tnIngressVtsCmodeMapTable':tnIngressVtsCmodeMapTable,'tnIngressVtsCmodeMapEntry':tnIngressVtsCmodeMapEntry,_k:tnIngressVtsCmodeMapCEVLANID,_l:tnIngressVtsCmodeMapSVLANID,_m:tnIngressVtsCmodeMapSIP,_n:tnIngressVtsCmodeMapDIP,_o:tnIngressVtsCmodeMapCMode,_p:tnIngressVtsCmodeMapRowStatus,'tnEgressVtsCmodeMapTable':tnEgressVtsCmodeMapTable,'tnEgressVtsCmodeMapEntry':tnEgressVtsCmodeMapEntry,_q:tnEgressVtsCmodeMapCEVLANID,_r:tnEgressVtsCmodeMapSVLANID,_s:tnEgressVtsCmodeMapSIP,_t:tnEgressVtsCmodeMapDIP,_u:tnEgressVtsCmodeMapCMode,_v:tnEgressVtsCmodeMapRowStatus})