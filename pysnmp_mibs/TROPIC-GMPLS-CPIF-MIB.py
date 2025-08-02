_A0='tnGmplsLmpGroup'
_z='tnGmplsDprGroup'
_y='tnGmplsRsvpGroup'
_x='tnGmplsCPNbrGroup'
_w='tnGmplsCpifObjsGroup'
_v='tnGmplsLmpIfRowStatus'
_u='tnGmplsLmpIfOpState'
_t='tnGmplsLmpIfAdminStatus'
_s='tnGmplsLmpIfEndPointDiscEnabled'
_r='tnGmplsLmpIfTraceMonEnabled'
_q='tnGmplsLmpIfLinkPropCorrEnabled'
_p='tnGmplsLmpIfHelloEnabled'
_o='tnGmplsLmpIfCPNbr'
_n='tnGmplsLmpIfName'
_m='tnGmplsDprIfRowStatus'
_l='tnGmplsDprIfNVMismatch'
_k='tnGmplsDprIfOpState'
_j='tnGmplsDprIfAdminStatus'
_i='tnGmplsDprIfCPNbr'
_h='tnGmplsDprIfEncaps'
_g='tnGmplsDprIfType'
_f='tnGmplsDprIfName'
_e='tnGmplsRsvpIfRowStatus'
_d='tnGmplsRsvpIfOpState'
_c='tnGmplsRsvpIfAdminStatus'
_b='tnGmplsRsvpIfCPNbr'
_a='tnGmplsRsvpIfEncaps'
_Z='tnGmplsRsvpIfType'
_Y='tnGmplsRsvpIfName'
_X='tnGmplsCPNbrRowStatus'
_W='tnGmplsCPNbrRemoteCPNodeId'
_V='tnGmplsCPNbrAdminStatus'
_U='tnGmplsCPNbrOspfArea'
_T='tnGmplsCPNbrRemoteTEP'
_S='tnGmplsCPNbrEncaps'
_R='tnGmplsCPNbrRemoteRouterAddr'
_Q='tnGmplsCPNbrAddrType'
_P='tnGmplsCPNbrIfName'
_O='tnGmplsCpifAttributeTotal'
_N='tnGmplsLmpIfId'
_M='tnGmplsDprIfId'
_L='ipminimal'
_K='tnGmplsRsvpIfId'
_J='tnGmplsCPNbrIfId'
_I='degraded'
_H='not-accessible'
_G='read-only'
_F='up'
_E='down'
_D='Integer32'
_C='read-create'
_B='TROPIC-GMPLS-CPIF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressIPv4,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressIPv4','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
tnGmplsMIBModules,tnGmplsObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnGmplsMIBModules','tnGmplsObjs')
tnGmplsCpifMibModule=ModuleIdentity((1,3,6,1,4,1,7483,1,1,2,6,1))
if mibBuilder.loadTexts:tnGmplsCpifMibModule.setRevisions(('2018-02-23 12:00','2016-11-16 12:00','2013-06-27 12:00'))
_TnGmplsCpifMIB_ObjectIdentity=ObjectIdentity
tnGmplsCpifMIB=_TnGmplsCpifMIB_ObjectIdentity((1,3,6,1,4,1,7483,2,1,10,1,1))
_TnGmplsCpifObjs_ObjectIdentity=ObjectIdentity
tnGmplsCpifObjs=_TnGmplsCpifObjs_ObjectIdentity((1,3,6,1,4,1,7483,2,1,10,1,1,1))
_TnGmplsCpifAttributeTotal_Type=Integer32
_TnGmplsCpifAttributeTotal_Object=MibScalar
tnGmplsCpifAttributeTotal=_TnGmplsCpifAttributeTotal_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,1),_TnGmplsCpifAttributeTotal_Type())
tnGmplsCpifAttributeTotal.setMaxAccess(_G)
if mibBuilder.loadTexts:tnGmplsCpifAttributeTotal.setStatus(_A)
_TnGmplsCPNbrTable_Object=MibTable
tnGmplsCPNbrTable=_TnGmplsCPNbrTable_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,2))
if mibBuilder.loadTexts:tnGmplsCPNbrTable.setStatus(_A)
_TnGmplsCPNbrEntry_Object=MibTableRow
tnGmplsCPNbrEntry=_TnGmplsCPNbrEntry_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,2,1))
tnGmplsCPNbrEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:tnGmplsCPNbrEntry.setStatus(_A)
_TnGmplsCPNbrIfId_Type=Unsigned32
_TnGmplsCPNbrIfId_Object=MibTableColumn
tnGmplsCPNbrIfId=_TnGmplsCPNbrIfId_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,2,1,1),_TnGmplsCPNbrIfId_Type())
tnGmplsCPNbrIfId.setMaxAccess(_H)
if mibBuilder.loadTexts:tnGmplsCPNbrIfId.setStatus(_A)
_TnGmplsCPNbrIfName_Type=DisplayString
_TnGmplsCPNbrIfName_Object=MibTableColumn
tnGmplsCPNbrIfName=_TnGmplsCPNbrIfName_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,2,1,2),_TnGmplsCPNbrIfName_Type())
tnGmplsCPNbrIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsCPNbrIfName.setStatus(_A)
_TnGmplsCPNbrAddrType_Type=InetAddressType
_TnGmplsCPNbrAddrType_Object=MibTableColumn
tnGmplsCPNbrAddrType=_TnGmplsCPNbrAddrType_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,2,1,3),_TnGmplsCPNbrAddrType_Type())
tnGmplsCPNbrAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsCPNbrAddrType.setStatus(_A)
_TnGmplsCPNbrRemoteRouterAddr_Type=InetAddress
_TnGmplsCPNbrRemoteRouterAddr_Object=MibTableColumn
tnGmplsCPNbrRemoteRouterAddr=_TnGmplsCPNbrRemoteRouterAddr_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,2,1,4),_TnGmplsCPNbrRemoteRouterAddr_Type())
tnGmplsCPNbrRemoteRouterAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsCPNbrRemoteRouterAddr.setStatus(_A)
class _TnGmplsCPNbrEncaps_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('ipinip',2),('gre',3)))
_TnGmplsCPNbrEncaps_Type.__name__=_D
_TnGmplsCPNbrEncaps_Object=MibTableColumn
tnGmplsCPNbrEncaps=_TnGmplsCPNbrEncaps_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,2,1,5),_TnGmplsCPNbrEncaps_Type())
tnGmplsCPNbrEncaps.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsCPNbrEncaps.setStatus(_A)
_TnGmplsCPNbrRemoteTEP_Type=InetAddress
_TnGmplsCPNbrRemoteTEP_Object=MibTableColumn
tnGmplsCPNbrRemoteTEP=_TnGmplsCPNbrRemoteTEP_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,2,1,6),_TnGmplsCPNbrRemoteTEP_Type())
tnGmplsCPNbrRemoteTEP.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsCPNbrRemoteTEP.setStatus(_A)
_TnGmplsCPNbrOspfArea_Type=IpAddress
_TnGmplsCPNbrOspfArea_Object=MibTableColumn
tnGmplsCPNbrOspfArea=_TnGmplsCPNbrOspfArea_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,2,1,7),_TnGmplsCPNbrOspfArea_Type())
tnGmplsCPNbrOspfArea.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsCPNbrOspfArea.setStatus(_A)
class _TnGmplsCPNbrAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_TnGmplsCPNbrAdminStatus_Type.__name__=_D
_TnGmplsCPNbrAdminStatus_Object=MibTableColumn
tnGmplsCPNbrAdminStatus=_TnGmplsCPNbrAdminStatus_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,2,1,8),_TnGmplsCPNbrAdminStatus_Type())
tnGmplsCPNbrAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsCPNbrAdminStatus.setStatus(_A)
_TnGmplsCPNbrRemoteCPNodeId_Type=InetAddressIPv4
_TnGmplsCPNbrRemoteCPNodeId_Object=MibTableColumn
tnGmplsCPNbrRemoteCPNodeId=_TnGmplsCPNbrRemoteCPNodeId_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,2,1,9),_TnGmplsCPNbrRemoteCPNodeId_Type())
tnGmplsCPNbrRemoteCPNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsCPNbrRemoteCPNodeId.setStatus(_A)
_TnGmplsCPNbrRowStatus_Type=RowStatus
_TnGmplsCPNbrRowStatus_Object=MibTableColumn
tnGmplsCPNbrRowStatus=_TnGmplsCPNbrRowStatus_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,2,1,10),_TnGmplsCPNbrRowStatus_Type())
tnGmplsCPNbrRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsCPNbrRowStatus.setStatus(_A)
_TnGmplsRsvpIfTable_Object=MibTable
tnGmplsRsvpIfTable=_TnGmplsRsvpIfTable_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,3))
if mibBuilder.loadTexts:tnGmplsRsvpIfTable.setStatus(_A)
_TnGmplsRsvpIfEntry_Object=MibTableRow
tnGmplsRsvpIfEntry=_TnGmplsRsvpIfEntry_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,3,1))
tnGmplsRsvpIfEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:tnGmplsRsvpIfEntry.setStatus(_A)
_TnGmplsRsvpIfId_Type=Unsigned32
_TnGmplsRsvpIfId_Object=MibTableColumn
tnGmplsRsvpIfId=_TnGmplsRsvpIfId_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,3,1,1),_TnGmplsRsvpIfId_Type())
tnGmplsRsvpIfId.setMaxAccess(_H)
if mibBuilder.loadTexts:tnGmplsRsvpIfId.setStatus(_A)
_TnGmplsRsvpIfName_Type=DisplayString
_TnGmplsRsvpIfName_Object=MibTableColumn
tnGmplsRsvpIfName=_TnGmplsRsvpIfName_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,3,1,2),_TnGmplsRsvpIfName_Type())
tnGmplsRsvpIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsRsvpIfName.setStatus(_A)
class _TnGmplsRsvpIfType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('uni',1),('nni',2)))
_TnGmplsRsvpIfType_Type.__name__=_D
_TnGmplsRsvpIfType_Object=MibTableColumn
tnGmplsRsvpIfType=_TnGmplsRsvpIfType_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,3,1,3),_TnGmplsRsvpIfType_Type())
tnGmplsRsvpIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsRsvpIfType.setStatus(_A)
class _TnGmplsRsvpIfEncaps_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),(_L,2)))
_TnGmplsRsvpIfEncaps_Type.__name__=_D
_TnGmplsRsvpIfEncaps_Object=MibTableColumn
tnGmplsRsvpIfEncaps=_TnGmplsRsvpIfEncaps_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,3,1,4),_TnGmplsRsvpIfEncaps_Type())
tnGmplsRsvpIfEncaps.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsRsvpIfEncaps.setStatus(_A)
_TnGmplsRsvpIfCPNbr_Type=Unsigned32
_TnGmplsRsvpIfCPNbr_Object=MibTableColumn
tnGmplsRsvpIfCPNbr=_TnGmplsRsvpIfCPNbr_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,3,1,5),_TnGmplsRsvpIfCPNbr_Type())
tnGmplsRsvpIfCPNbr.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsRsvpIfCPNbr.setStatus(_A)
class _TnGmplsRsvpIfAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_TnGmplsRsvpIfAdminStatus_Type.__name__=_D
_TnGmplsRsvpIfAdminStatus_Object=MibTableColumn
tnGmplsRsvpIfAdminStatus=_TnGmplsRsvpIfAdminStatus_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,3,1,6),_TnGmplsRsvpIfAdminStatus_Type())
tnGmplsRsvpIfAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsRsvpIfAdminStatus.setStatus(_A)
class _TnGmplsRsvpIfOpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_I,3)))
_TnGmplsRsvpIfOpState_Type.__name__=_D
_TnGmplsRsvpIfOpState_Object=MibTableColumn
tnGmplsRsvpIfOpState=_TnGmplsRsvpIfOpState_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,3,1,7),_TnGmplsRsvpIfOpState_Type())
tnGmplsRsvpIfOpState.setMaxAccess(_G)
if mibBuilder.loadTexts:tnGmplsRsvpIfOpState.setStatus(_A)
_TnGmplsRsvpIfRowStatus_Type=RowStatus
_TnGmplsRsvpIfRowStatus_Object=MibTableColumn
tnGmplsRsvpIfRowStatus=_TnGmplsRsvpIfRowStatus_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,3,1,8),_TnGmplsRsvpIfRowStatus_Type())
tnGmplsRsvpIfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsRsvpIfRowStatus.setStatus(_A)
_TnGmplsDprIfTable_Object=MibTable
tnGmplsDprIfTable=_TnGmplsDprIfTable_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,4))
if mibBuilder.loadTexts:tnGmplsDprIfTable.setStatus(_A)
_TnGmplsDprIfEntry_Object=MibTableRow
tnGmplsDprIfEntry=_TnGmplsDprIfEntry_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,4,1))
tnGmplsDprIfEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:tnGmplsDprIfEntry.setStatus(_A)
_TnGmplsDprIfId_Type=Unsigned32
_TnGmplsDprIfId_Object=MibTableColumn
tnGmplsDprIfId=_TnGmplsDprIfId_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,4,1,1),_TnGmplsDprIfId_Type())
tnGmplsDprIfId.setMaxAccess(_H)
if mibBuilder.loadTexts:tnGmplsDprIfId.setStatus(_A)
_TnGmplsDprIfName_Type=DisplayString
_TnGmplsDprIfName_Object=MibTableColumn
tnGmplsDprIfName=_TnGmplsDprIfName_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,4,1,2),_TnGmplsDprIfName_Type())
tnGmplsDprIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsDprIfName.setStatus(_A)
class _TnGmplsDprIfType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('nni',1))
_TnGmplsDprIfType_Type.__name__=_D
_TnGmplsDprIfType_Object=MibTableColumn
tnGmplsDprIfType=_TnGmplsDprIfType_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,4,1,3),_TnGmplsDprIfType_Type())
tnGmplsDprIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsDprIfType.setStatus(_A)
class _TnGmplsDprIfEncaps_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_L,1))
_TnGmplsDprIfEncaps_Type.__name__=_D
_TnGmplsDprIfEncaps_Object=MibTableColumn
tnGmplsDprIfEncaps=_TnGmplsDprIfEncaps_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,4,1,4),_TnGmplsDprIfEncaps_Type())
tnGmplsDprIfEncaps.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsDprIfEncaps.setStatus(_A)
_TnGmplsDprIfCPNbr_Type=Unsigned32
_TnGmplsDprIfCPNbr_Object=MibTableColumn
tnGmplsDprIfCPNbr=_TnGmplsDprIfCPNbr_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,4,1,5),_TnGmplsDprIfCPNbr_Type())
tnGmplsDprIfCPNbr.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsDprIfCPNbr.setStatus(_A)
class _TnGmplsDprIfAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_TnGmplsDprIfAdminStatus_Type.__name__=_D
_TnGmplsDprIfAdminStatus_Object=MibTableColumn
tnGmplsDprIfAdminStatus=_TnGmplsDprIfAdminStatus_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,4,1,6),_TnGmplsDprIfAdminStatus_Type())
tnGmplsDprIfAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsDprIfAdminStatus.setStatus(_A)
class _TnGmplsDprIfOpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_I,3)))
_TnGmplsDprIfOpState_Type.__name__=_D
_TnGmplsDprIfOpState_Object=MibTableColumn
tnGmplsDprIfOpState=_TnGmplsDprIfOpState_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,4,1,7),_TnGmplsDprIfOpState_Type())
tnGmplsDprIfOpState.setMaxAccess(_G)
if mibBuilder.loadTexts:tnGmplsDprIfOpState.setStatus(_A)
_TnGmplsDprIfNVMismatch_Type=TruthValue
_TnGmplsDprIfNVMismatch_Object=MibTableColumn
tnGmplsDprIfNVMismatch=_TnGmplsDprIfNVMismatch_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,4,1,8),_TnGmplsDprIfNVMismatch_Type())
tnGmplsDprIfNVMismatch.setMaxAccess(_G)
if mibBuilder.loadTexts:tnGmplsDprIfNVMismatch.setStatus(_A)
_TnGmplsDprIfRowStatus_Type=RowStatus
_TnGmplsDprIfRowStatus_Object=MibTableColumn
tnGmplsDprIfRowStatus=_TnGmplsDprIfRowStatus_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,4,1,9),_TnGmplsDprIfRowStatus_Type())
tnGmplsDprIfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsDprIfRowStatus.setStatus(_A)
_TnGmplsLmpIfTable_Object=MibTable
tnGmplsLmpIfTable=_TnGmplsLmpIfTable_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,5))
if mibBuilder.loadTexts:tnGmplsLmpIfTable.setStatus(_A)
_TnGmplsLmpIfEntry_Object=MibTableRow
tnGmplsLmpIfEntry=_TnGmplsLmpIfEntry_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,5,1))
tnGmplsLmpIfEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:tnGmplsLmpIfEntry.setStatus(_A)
_TnGmplsLmpIfId_Type=Unsigned32
_TnGmplsLmpIfId_Object=MibTableColumn
tnGmplsLmpIfId=_TnGmplsLmpIfId_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,5,1,1),_TnGmplsLmpIfId_Type())
tnGmplsLmpIfId.setMaxAccess(_H)
if mibBuilder.loadTexts:tnGmplsLmpIfId.setStatus(_A)
_TnGmplsLmpIfName_Type=DisplayString
_TnGmplsLmpIfName_Object=MibTableColumn
tnGmplsLmpIfName=_TnGmplsLmpIfName_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,5,1,2),_TnGmplsLmpIfName_Type())
tnGmplsLmpIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLmpIfName.setStatus(_A)
_TnGmplsLmpIfCPNbr_Type=Unsigned32
_TnGmplsLmpIfCPNbr_Object=MibTableColumn
tnGmplsLmpIfCPNbr=_TnGmplsLmpIfCPNbr_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,5,1,3),_TnGmplsLmpIfCPNbr_Type())
tnGmplsLmpIfCPNbr.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLmpIfCPNbr.setStatus(_A)
_TnGmplsLmpIfHelloEnabled_Type=TruthValue
_TnGmplsLmpIfHelloEnabled_Object=MibTableColumn
tnGmplsLmpIfHelloEnabled=_TnGmplsLmpIfHelloEnabled_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,5,1,4),_TnGmplsLmpIfHelloEnabled_Type())
tnGmplsLmpIfHelloEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLmpIfHelloEnabled.setStatus(_A)
_TnGmplsLmpIfLinkPropCorrEnabled_Type=TruthValue
_TnGmplsLmpIfLinkPropCorrEnabled_Object=MibTableColumn
tnGmplsLmpIfLinkPropCorrEnabled=_TnGmplsLmpIfLinkPropCorrEnabled_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,5,1,5),_TnGmplsLmpIfLinkPropCorrEnabled_Type())
tnGmplsLmpIfLinkPropCorrEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLmpIfLinkPropCorrEnabled.setStatus(_A)
_TnGmplsLmpIfTraceMonEnabled_Type=TruthValue
_TnGmplsLmpIfTraceMonEnabled_Object=MibTableColumn
tnGmplsLmpIfTraceMonEnabled=_TnGmplsLmpIfTraceMonEnabled_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,5,1,6),_TnGmplsLmpIfTraceMonEnabled_Type())
tnGmplsLmpIfTraceMonEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLmpIfTraceMonEnabled.setStatus(_A)
_TnGmplsLmpIfEndPointDiscEnabled_Type=TruthValue
_TnGmplsLmpIfEndPointDiscEnabled_Object=MibTableColumn
tnGmplsLmpIfEndPointDiscEnabled=_TnGmplsLmpIfEndPointDiscEnabled_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,5,1,7),_TnGmplsLmpIfEndPointDiscEnabled_Type())
tnGmplsLmpIfEndPointDiscEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLmpIfEndPointDiscEnabled.setStatus(_A)
class _TnGmplsLmpIfAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_TnGmplsLmpIfAdminStatus_Type.__name__=_D
_TnGmplsLmpIfAdminStatus_Object=MibTableColumn
tnGmplsLmpIfAdminStatus=_TnGmplsLmpIfAdminStatus_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,5,1,8),_TnGmplsLmpIfAdminStatus_Type())
tnGmplsLmpIfAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLmpIfAdminStatus.setStatus(_A)
class _TnGmplsLmpIfOpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_I,3)))
_TnGmplsLmpIfOpState_Type.__name__=_D
_TnGmplsLmpIfOpState_Object=MibTableColumn
tnGmplsLmpIfOpState=_TnGmplsLmpIfOpState_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,5,1,9),_TnGmplsLmpIfOpState_Type())
tnGmplsLmpIfOpState.setMaxAccess(_G)
if mibBuilder.loadTexts:tnGmplsLmpIfOpState.setStatus(_A)
_TnGmplsLmpIfRowStatus_Type=RowStatus
_TnGmplsLmpIfRowStatus_Object=MibTableColumn
tnGmplsLmpIfRowStatus=_TnGmplsLmpIfRowStatus_Object((1,3,6,1,4,1,7483,2,1,10,1,1,1,5,1,10),_TnGmplsLmpIfRowStatus_Type())
tnGmplsLmpIfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLmpIfRowStatus.setStatus(_A)
_TnGmplsCpifConf_ObjectIdentity=ObjectIdentity
tnGmplsCpifConf=_TnGmplsCpifConf_ObjectIdentity((1,3,6,1,4,1,7483,2,1,10,1,1,3))
_TnGmplsCpifGroups_ObjectIdentity=ObjectIdentity
tnGmplsCpifGroups=_TnGmplsCpifGroups_ObjectIdentity((1,3,6,1,4,1,7483,2,1,10,1,1,3,1))
_TnGmplsCpifCompliances_ObjectIdentity=ObjectIdentity
tnGmplsCpifCompliances=_TnGmplsCpifCompliances_ObjectIdentity((1,3,6,1,4,1,7483,2,1,10,1,1,3,2))
tnGmplsCpifObjsGroup=ObjectGroup((1,3,6,1,4,1,7483,2,1,10,1,1,3,1,1))
tnGmplsCpifObjsGroup.setObjects((_B,_O))
if mibBuilder.loadTexts:tnGmplsCpifObjsGroup.setStatus(_A)
tnGmplsCPNbrGroup=ObjectGroup((1,3,6,1,4,1,7483,2,1,10,1,1,3,1,2))
tnGmplsCPNbrGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:tnGmplsCPNbrGroup.setStatus(_A)
tnGmplsRsvpGroup=ObjectGroup((1,3,6,1,4,1,7483,2,1,10,1,1,3,1,3))
tnGmplsRsvpGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:tnGmplsRsvpGroup.setStatus(_A)
tnGmplsDprGroup=ObjectGroup((1,3,6,1,4,1,7483,2,1,10,1,1,3,1,4))
tnGmplsDprGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:tnGmplsDprGroup.setStatus(_A)
tnGmplsLmpGroup=ObjectGroup((1,3,6,1,4,1,7483,2,1,10,1,1,3,1,5))
tnGmplsLmpGroup.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:tnGmplsLmpGroup.setStatus(_A)
tnGmplsCpifCompliance=ModuleCompliance((1,3,6,1,4,1,7483,2,1,10,1,1,3,2,1))
tnGmplsCpifCompliance.setObjects(*((_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:tnGmplsCpifCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'tnGmplsCpifMibModule':tnGmplsCpifMibModule,'tnGmplsCpifMIB':tnGmplsCpifMIB,'tnGmplsCpifObjs':tnGmplsCpifObjs,_O:tnGmplsCpifAttributeTotal,'tnGmplsCPNbrTable':tnGmplsCPNbrTable,'tnGmplsCPNbrEntry':tnGmplsCPNbrEntry,_J:tnGmplsCPNbrIfId,_P:tnGmplsCPNbrIfName,_Q:tnGmplsCPNbrAddrType,_R:tnGmplsCPNbrRemoteRouterAddr,_S:tnGmplsCPNbrEncaps,_T:tnGmplsCPNbrRemoteTEP,_U:tnGmplsCPNbrOspfArea,_V:tnGmplsCPNbrAdminStatus,_W:tnGmplsCPNbrRemoteCPNodeId,_X:tnGmplsCPNbrRowStatus,'tnGmplsRsvpIfTable':tnGmplsRsvpIfTable,'tnGmplsRsvpIfEntry':tnGmplsRsvpIfEntry,_K:tnGmplsRsvpIfId,_Y:tnGmplsRsvpIfName,_Z:tnGmplsRsvpIfType,_a:tnGmplsRsvpIfEncaps,_b:tnGmplsRsvpIfCPNbr,_c:tnGmplsRsvpIfAdminStatus,_d:tnGmplsRsvpIfOpState,_e:tnGmplsRsvpIfRowStatus,'tnGmplsDprIfTable':tnGmplsDprIfTable,'tnGmplsDprIfEntry':tnGmplsDprIfEntry,_M:tnGmplsDprIfId,_f:tnGmplsDprIfName,_g:tnGmplsDprIfType,_h:tnGmplsDprIfEncaps,_i:tnGmplsDprIfCPNbr,_j:tnGmplsDprIfAdminStatus,_k:tnGmplsDprIfOpState,_l:tnGmplsDprIfNVMismatch,_m:tnGmplsDprIfRowStatus,'tnGmplsLmpIfTable':tnGmplsLmpIfTable,'tnGmplsLmpIfEntry':tnGmplsLmpIfEntry,_N:tnGmplsLmpIfId,_n:tnGmplsLmpIfName,_o:tnGmplsLmpIfCPNbr,_p:tnGmplsLmpIfHelloEnabled,_q:tnGmplsLmpIfLinkPropCorrEnabled,_r:tnGmplsLmpIfTraceMonEnabled,_s:tnGmplsLmpIfEndPointDiscEnabled,_t:tnGmplsLmpIfAdminStatus,_u:tnGmplsLmpIfOpState,_v:tnGmplsLmpIfRowStatus,'tnGmplsCpifConf':tnGmplsCpifConf,'tnGmplsCpifGroups':tnGmplsCpifGroups,_w:tnGmplsCpifObjsGroup,_x:tnGmplsCPNbrGroup,_y:tnGmplsRsvpGroup,_z:tnGmplsDprGroup,_A0:tnGmplsLmpGroup,'tnGmplsCpifCompliances':tnGmplsCpifCompliances,'tnGmplsCpifCompliance':tnGmplsCpifCompliance})