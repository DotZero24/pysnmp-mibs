_z='qllcLSStatsGroup'
_y='qllcLSOperGroup'
_x='qllcLSAdminGroup'
_w='qllcLSStatsNumErrs'
_v='qllcLSStatsNumDrops'
_u='qllcLSStatsNumSndFrmrs'
_t='qllcLSStatsNumRcvFrmrs'
_s='qllcLSStatsNumSndDms'
_r='qllcLSStatsNumRcvDms'
_q='qllcLSStatsNumSndDiscs'
_p='qllcLSStatsNumRcvDiscs'
_o='qllcLSStatsNumSndQsms'
_n='qllcLSStatsNumRcvQsms'
_m='qllcLSStatsOutBytes'
_l='qllcLSStatsInBytes'
_k='qllcLSStatsOutPaks'
_j='qllcLSStatsInPaks'
_i='qllcLSStatsQuenchOn'
_h='qllcLSStatsQuenchOff'
_g='qllcLSStatsTestOut'
_f='qllcLSStatsTestIn'
_e='qllcLSStatsXidOut'
_d='qllcLSStatsXidIn'
_c='qllcLSOperLgX25'
_b='qllcLSOperState'
_a='qllcLSOperModulo'
_Z='qllcLSOperX25Add'
_Y='qllcLSOperRole'
_X='qllcLSOperCircuitType'
_W='qllcLSAdminLgX25'
_V='qllcLSAdminModulo'
_U='qllcLSAdminX25Add'
_T='qllcLSAdminCircuitType'
_S='qllcLSAdminRole'
_R='modulo128'
_Q='modulo8'
_P='peerToPeer'
_O='secondary'
_N='primary'
_M='permanentVC'
_L='switchedVC'
_K='qllcLSStatsLciVcIndex'
_J='qllcLSStatsIfIndex'
_I='qllcLSOperLciVcIndex'
_H='qllcLSOperIfIndex'
_G='qllcLSAdminLciVcIndex'
_F='qllcLSAdminIfIndex'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='CISCO-QLLC01-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
snaqllc01=ModuleIdentity((1,3,6,1,4,1,9,10,6))
class IfIndexType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class X121Address(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_Qllc_ObjectIdentity=ObjectIdentity
qllc=_Qllc_ObjectIdentity((1,3,6,1,4,1,9,10,6,1))
_QllcLSAdminTable_Object=MibTable
qllcLSAdminTable=_QllcLSAdminTable_Object((1,3,6,1,4,1,9,10,6,1,1))
if mibBuilder.loadTexts:qllcLSAdminTable.setStatus(_A)
_QllcLSAdminEntry_Object=MibTableRow
qllcLSAdminEntry=_QllcLSAdminEntry_Object((1,3,6,1,4,1,9,10,6,1,1,1))
qllcLSAdminEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:qllcLSAdminEntry.setStatus(_A)
_QllcLSAdminIfIndex_Type=IfIndexType
_QllcLSAdminIfIndex_Object=MibTableColumn
qllcLSAdminIfIndex=_QllcLSAdminIfIndex_Object((1,3,6,1,4,1,9,10,6,1,1,1,1),_QllcLSAdminIfIndex_Type())
qllcLSAdminIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:qllcLSAdminIfIndex.setStatus(_A)
_QllcLSAdminLciVcIndex_Type=IfIndexType
_QllcLSAdminLciVcIndex_Object=MibTableColumn
qllcLSAdminLciVcIndex=_QllcLSAdminLciVcIndex_Object((1,3,6,1,4,1,9,10,6,1,1,1,2),_QllcLSAdminLciVcIndex_Type())
qllcLSAdminLciVcIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:qllcLSAdminLciVcIndex.setStatus(_A)
class _QllcLSAdminCircuitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_QllcLSAdminCircuitType_Type.__name__=_D
_QllcLSAdminCircuitType_Object=MibTableColumn
qllcLSAdminCircuitType=_QllcLSAdminCircuitType_Object((1,3,6,1,4,1,9,10,6,1,1,1,3),_QllcLSAdminCircuitType_Type())
qllcLSAdminCircuitType.setMaxAccess(_E)
if mibBuilder.loadTexts:qllcLSAdminCircuitType.setStatus(_A)
class _QllcLSAdminRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3)))
_QllcLSAdminRole_Type.__name__=_D
_QllcLSAdminRole_Object=MibTableColumn
qllcLSAdminRole=_QllcLSAdminRole_Object((1,3,6,1,4,1,9,10,6,1,1,1,4),_QllcLSAdminRole_Type())
qllcLSAdminRole.setMaxAccess(_E)
if mibBuilder.loadTexts:qllcLSAdminRole.setStatus(_A)
_QllcLSAdminX25Add_Type=X121Address
_QllcLSAdminX25Add_Object=MibTableColumn
qllcLSAdminX25Add=_QllcLSAdminX25Add_Object((1,3,6,1,4,1,9,10,6,1,1,1,5),_QllcLSAdminX25Add_Type())
qllcLSAdminX25Add.setMaxAccess(_E)
if mibBuilder.loadTexts:qllcLSAdminX25Add.setStatus(_A)
class _QllcLSAdminModulo_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_QllcLSAdminModulo_Type.__name__=_D
_QllcLSAdminModulo_Object=MibTableColumn
qllcLSAdminModulo=_QllcLSAdminModulo_Object((1,3,6,1,4,1,9,10,6,1,1,1,6),_QllcLSAdminModulo_Type())
qllcLSAdminModulo.setMaxAccess(_E)
if mibBuilder.loadTexts:qllcLSAdminModulo.setStatus(_A)
_QllcLSAdminLgX25_Type=Integer32
_QllcLSAdminLgX25_Object=MibTableColumn
qllcLSAdminLgX25=_QllcLSAdminLgX25_Object((1,3,6,1,4,1,9,10,6,1,1,1,7),_QllcLSAdminLgX25_Type())
qllcLSAdminLgX25.setMaxAccess(_E)
if mibBuilder.loadTexts:qllcLSAdminLgX25.setStatus(_A)
_QllcLSOperTable_Object=MibTable
qllcLSOperTable=_QllcLSOperTable_Object((1,3,6,1,4,1,9,10,6,1,2))
if mibBuilder.loadTexts:qllcLSOperTable.setStatus(_A)
_QllcLSOperEntry_Object=MibTableRow
qllcLSOperEntry=_QllcLSOperEntry_Object((1,3,6,1,4,1,9,10,6,1,2,1))
qllcLSOperEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:qllcLSOperEntry.setStatus(_A)
_QllcLSOperIfIndex_Type=IfIndexType
_QllcLSOperIfIndex_Object=MibTableColumn
qllcLSOperIfIndex=_QllcLSOperIfIndex_Object((1,3,6,1,4,1,9,10,6,1,2,1,1),_QllcLSOperIfIndex_Type())
qllcLSOperIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSOperIfIndex.setStatus(_A)
_QllcLSOperLciVcIndex_Type=IfIndexType
_QllcLSOperLciVcIndex_Object=MibTableColumn
qllcLSOperLciVcIndex=_QllcLSOperLciVcIndex_Object((1,3,6,1,4,1,9,10,6,1,2,1,2),_QllcLSOperLciVcIndex_Type())
qllcLSOperLciVcIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSOperLciVcIndex.setStatus(_A)
class _QllcLSOperCircuitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_QllcLSOperCircuitType_Type.__name__=_D
_QllcLSOperCircuitType_Object=MibTableColumn
qllcLSOperCircuitType=_QllcLSOperCircuitType_Object((1,3,6,1,4,1,9,10,6,1,2,1,3),_QllcLSOperCircuitType_Type())
qllcLSOperCircuitType.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSOperCircuitType.setStatus(_A)
class _QllcLSOperRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3)))
_QllcLSOperRole_Type.__name__=_D
_QllcLSOperRole_Object=MibTableColumn
qllcLSOperRole=_QllcLSOperRole_Object((1,3,6,1,4,1,9,10,6,1,2,1,4),_QllcLSOperRole_Type())
qllcLSOperRole.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSOperRole.setStatus(_A)
_QllcLSOperX25Add_Type=X121Address
_QllcLSOperX25Add_Object=MibTableColumn
qllcLSOperX25Add=_QllcLSOperX25Add_Object((1,3,6,1,4,1,9,10,6,1,2,1,5),_QllcLSOperX25Add_Type())
qllcLSOperX25Add.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSOperX25Add.setStatus(_A)
class _QllcLSOperModulo_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_QllcLSOperModulo_Type.__name__=_D
_QllcLSOperModulo_Object=MibTableColumn
qllcLSOperModulo=_QllcLSOperModulo_Object((1,3,6,1,4,1,9,10,6,1,2,1,6),_QllcLSOperModulo_Type())
qllcLSOperModulo.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSOperModulo.setStatus(_A)
class _QllcLSOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('lsStateInop',1),('lsStateClosed',2),('lsStateOpening',3),('lsStateClosing',4),('lsStateRecovery',5),('lsStateOpened',6)))
_QllcLSOperState_Type.__name__=_D
_QllcLSOperState_Object=MibTableColumn
qllcLSOperState=_QllcLSOperState_Object((1,3,6,1,4,1,9,10,6,1,2,1,7),_QllcLSOperState_Type())
qllcLSOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSOperState.setStatus(_A)
_QllcLSOperLgX25_Type=Integer32
_QllcLSOperLgX25_Object=MibTableColumn
qllcLSOperLgX25=_QllcLSOperLgX25_Object((1,3,6,1,4,1,9,10,6,1,2,1,8),_QllcLSOperLgX25_Type())
qllcLSOperLgX25.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSOperLgX25.setStatus(_A)
_QllcLSStatsTable_Object=MibTable
qllcLSStatsTable=_QllcLSStatsTable_Object((1,3,6,1,4,1,9,10,6,1,3))
if mibBuilder.loadTexts:qllcLSStatsTable.setStatus(_A)
_QllcLSStatsEntry_Object=MibTableRow
qllcLSStatsEntry=_QllcLSStatsEntry_Object((1,3,6,1,4,1,9,10,6,1,3,1))
qllcLSStatsEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:qllcLSStatsEntry.setStatus(_A)
_QllcLSStatsIfIndex_Type=IfIndexType
_QllcLSStatsIfIndex_Object=MibTableColumn
qllcLSStatsIfIndex=_QllcLSStatsIfIndex_Object((1,3,6,1,4,1,9,10,6,1,3,1,1),_QllcLSStatsIfIndex_Type())
qllcLSStatsIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSStatsIfIndex.setStatus(_A)
_QllcLSStatsLciVcIndex_Type=IfIndexType
_QllcLSStatsLciVcIndex_Object=MibTableColumn
qllcLSStatsLciVcIndex=_QllcLSStatsLciVcIndex_Object((1,3,6,1,4,1,9,10,6,1,3,1,2),_QllcLSStatsLciVcIndex_Type())
qllcLSStatsLciVcIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSStatsLciVcIndex.setStatus(_A)
_QllcLSStatsXidIn_Type=Counter32
_QllcLSStatsXidIn_Object=MibTableColumn
qllcLSStatsXidIn=_QllcLSStatsXidIn_Object((1,3,6,1,4,1,9,10,6,1,3,1,3),_QllcLSStatsXidIn_Type())
qllcLSStatsXidIn.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSStatsXidIn.setStatus(_A)
_QllcLSStatsXidOut_Type=Counter32
_QllcLSStatsXidOut_Object=MibTableColumn
qllcLSStatsXidOut=_QllcLSStatsXidOut_Object((1,3,6,1,4,1,9,10,6,1,3,1,4),_QllcLSStatsXidOut_Type())
qllcLSStatsXidOut.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSStatsXidOut.setStatus(_A)
_QllcLSStatsTestIn_Type=Counter32
_QllcLSStatsTestIn_Object=MibTableColumn
qllcLSStatsTestIn=_QllcLSStatsTestIn_Object((1,3,6,1,4,1,9,10,6,1,3,1,5),_QllcLSStatsTestIn_Type())
qllcLSStatsTestIn.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSStatsTestIn.setStatus(_A)
_QllcLSStatsTestOut_Type=Counter32
_QllcLSStatsTestOut_Object=MibTableColumn
qllcLSStatsTestOut=_QllcLSStatsTestOut_Object((1,3,6,1,4,1,9,10,6,1,3,1,6),_QllcLSStatsTestOut_Type())
qllcLSStatsTestOut.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSStatsTestOut.setStatus(_A)
_QllcLSStatsQuenchOff_Type=Counter32
_QllcLSStatsQuenchOff_Object=MibTableColumn
qllcLSStatsQuenchOff=_QllcLSStatsQuenchOff_Object((1,3,6,1,4,1,9,10,6,1,3,1,7),_QllcLSStatsQuenchOff_Type())
qllcLSStatsQuenchOff.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSStatsQuenchOff.setStatus(_A)
_QllcLSStatsQuenchOn_Type=Counter32
_QllcLSStatsQuenchOn_Object=MibTableColumn
qllcLSStatsQuenchOn=_QllcLSStatsQuenchOn_Object((1,3,6,1,4,1,9,10,6,1,3,1,8),_QllcLSStatsQuenchOn_Type())
qllcLSStatsQuenchOn.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSStatsQuenchOn.setStatus(_A)
_QllcLSStatsInPaks_Type=Counter32
_QllcLSStatsInPaks_Object=MibTableColumn
qllcLSStatsInPaks=_QllcLSStatsInPaks_Object((1,3,6,1,4,1,9,10,6,1,3,1,9),_QllcLSStatsInPaks_Type())
qllcLSStatsInPaks.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSStatsInPaks.setStatus(_A)
_QllcLSStatsOutPaks_Type=Counter32
_QllcLSStatsOutPaks_Object=MibTableColumn
qllcLSStatsOutPaks=_QllcLSStatsOutPaks_Object((1,3,6,1,4,1,9,10,6,1,3,1,10),_QllcLSStatsOutPaks_Type())
qllcLSStatsOutPaks.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSStatsOutPaks.setStatus(_A)
_QllcLSStatsInBytes_Type=Counter32
_QllcLSStatsInBytes_Object=MibTableColumn
qllcLSStatsInBytes=_QllcLSStatsInBytes_Object((1,3,6,1,4,1,9,10,6,1,3,1,11),_QllcLSStatsInBytes_Type())
qllcLSStatsInBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSStatsInBytes.setStatus(_A)
_QllcLSStatsOutBytes_Type=Counter32
_QllcLSStatsOutBytes_Object=MibTableColumn
qllcLSStatsOutBytes=_QllcLSStatsOutBytes_Object((1,3,6,1,4,1,9,10,6,1,3,1,12),_QllcLSStatsOutBytes_Type())
qllcLSStatsOutBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSStatsOutBytes.setStatus(_A)
_QllcLSStatsNumRcvQsms_Type=Counter32
_QllcLSStatsNumRcvQsms_Object=MibTableColumn
qllcLSStatsNumRcvQsms=_QllcLSStatsNumRcvQsms_Object((1,3,6,1,4,1,9,10,6,1,3,1,13),_QllcLSStatsNumRcvQsms_Type())
qllcLSStatsNumRcvQsms.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSStatsNumRcvQsms.setStatus(_A)
_QllcLSStatsNumSndQsms_Type=Counter32
_QllcLSStatsNumSndQsms_Object=MibTableColumn
qllcLSStatsNumSndQsms=_QllcLSStatsNumSndQsms_Object((1,3,6,1,4,1,9,10,6,1,3,1,14),_QllcLSStatsNumSndQsms_Type())
qllcLSStatsNumSndQsms.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSStatsNumSndQsms.setStatus(_A)
_QllcLSStatsNumRcvDiscs_Type=Counter32
_QllcLSStatsNumRcvDiscs_Object=MibTableColumn
qllcLSStatsNumRcvDiscs=_QllcLSStatsNumRcvDiscs_Object((1,3,6,1,4,1,9,10,6,1,3,1,15),_QllcLSStatsNumRcvDiscs_Type())
qllcLSStatsNumRcvDiscs.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSStatsNumRcvDiscs.setStatus(_A)
_QllcLSStatsNumSndDiscs_Type=Counter32
_QllcLSStatsNumSndDiscs_Object=MibTableColumn
qllcLSStatsNumSndDiscs=_QllcLSStatsNumSndDiscs_Object((1,3,6,1,4,1,9,10,6,1,3,1,16),_QllcLSStatsNumSndDiscs_Type())
qllcLSStatsNumSndDiscs.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSStatsNumSndDiscs.setStatus(_A)
_QllcLSStatsNumRcvDms_Type=Counter32
_QllcLSStatsNumRcvDms_Object=MibTableColumn
qllcLSStatsNumRcvDms=_QllcLSStatsNumRcvDms_Object((1,3,6,1,4,1,9,10,6,1,3,1,17),_QllcLSStatsNumRcvDms_Type())
qllcLSStatsNumRcvDms.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSStatsNumRcvDms.setStatus(_A)
_QllcLSStatsNumSndDms_Type=Counter32
_QllcLSStatsNumSndDms_Object=MibTableColumn
qllcLSStatsNumSndDms=_QllcLSStatsNumSndDms_Object((1,3,6,1,4,1,9,10,6,1,3,1,18),_QllcLSStatsNumSndDms_Type())
qllcLSStatsNumSndDms.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSStatsNumSndDms.setStatus(_A)
_QllcLSStatsNumRcvFrmrs_Type=Counter32
_QllcLSStatsNumRcvFrmrs_Object=MibTableColumn
qllcLSStatsNumRcvFrmrs=_QllcLSStatsNumRcvFrmrs_Object((1,3,6,1,4,1,9,10,6,1,3,1,19),_QllcLSStatsNumRcvFrmrs_Type())
qllcLSStatsNumRcvFrmrs.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSStatsNumRcvFrmrs.setStatus(_A)
_QllcLSStatsNumSndFrmrs_Type=Counter32
_QllcLSStatsNumSndFrmrs_Object=MibTableColumn
qllcLSStatsNumSndFrmrs=_QllcLSStatsNumSndFrmrs_Object((1,3,6,1,4,1,9,10,6,1,3,1,20),_QllcLSStatsNumSndFrmrs_Type())
qllcLSStatsNumSndFrmrs.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSStatsNumSndFrmrs.setStatus(_A)
_QllcLSStatsNumDrops_Type=Counter32
_QllcLSStatsNumDrops_Object=MibTableColumn
qllcLSStatsNumDrops=_QllcLSStatsNumDrops_Object((1,3,6,1,4,1,9,10,6,1,3,1,21),_QllcLSStatsNumDrops_Type())
qllcLSStatsNumDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSStatsNumDrops.setStatus(_A)
_QllcLSStatsNumErrs_Type=Counter32
_QllcLSStatsNumErrs_Object=MibTableColumn
qllcLSStatsNumErrs=_QllcLSStatsNumErrs_Object((1,3,6,1,4,1,9,10,6,1,3,1,22),_QllcLSStatsNumErrs_Type())
qllcLSStatsNumErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:qllcLSStatsNumErrs.setStatus(_A)
_QllcMibConformance_ObjectIdentity=ObjectIdentity
qllcMibConformance=_QllcMibConformance_ObjectIdentity((1,3,6,1,4,1,9,10,6,2))
_QllcMibCompliances_ObjectIdentity=ObjectIdentity
qllcMibCompliances=_QllcMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,6,2,1))
_QllcMibGroups_ObjectIdentity=ObjectIdentity
qllcMibGroups=_QllcMibGroups_ObjectIdentity((1,3,6,1,4,1,9,10,6,2,2))
qllcLSAdminGroup=ObjectGroup((1,3,6,1,4,1,9,10,6,2,2,1))
qllcLSAdminGroup.setObjects(*((_B,_F),(_B,_G),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:qllcLSAdminGroup.setStatus(_A)
qllcLSOperGroup=ObjectGroup((1,3,6,1,4,1,9,10,6,2,2,2))
qllcLSOperGroup.setObjects(*((_B,_H),(_B,_I),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:qllcLSOperGroup.setStatus(_A)
qllcLSStatsGroup=ObjectGroup((1,3,6,1,4,1,9,10,6,2,2,3))
qllcLSStatsGroup.setObjects(*((_B,_J),(_B,_K),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:qllcLSStatsGroup.setStatus(_A)
qllcMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,6,2,1,1))
qllcMibCompliance.setObjects(*((_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:qllcMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'IfIndexType':IfIndexType,'X121Address':X121Address,'snaqllc01':snaqllc01,'qllc':qllc,'qllcLSAdminTable':qllcLSAdminTable,'qllcLSAdminEntry':qllcLSAdminEntry,_F:qllcLSAdminIfIndex,_G:qllcLSAdminLciVcIndex,_T:qllcLSAdminCircuitType,_S:qllcLSAdminRole,_U:qllcLSAdminX25Add,_V:qllcLSAdminModulo,_W:qllcLSAdminLgX25,'qllcLSOperTable':qllcLSOperTable,'qllcLSOperEntry':qllcLSOperEntry,_H:qllcLSOperIfIndex,_I:qllcLSOperLciVcIndex,_X:qllcLSOperCircuitType,_Y:qllcLSOperRole,_Z:qllcLSOperX25Add,_a:qllcLSOperModulo,_b:qllcLSOperState,_c:qllcLSOperLgX25,'qllcLSStatsTable':qllcLSStatsTable,'qllcLSStatsEntry':qllcLSStatsEntry,_J:qllcLSStatsIfIndex,_K:qllcLSStatsLciVcIndex,_d:qllcLSStatsXidIn,_e:qllcLSStatsXidOut,_f:qllcLSStatsTestIn,_g:qllcLSStatsTestOut,_h:qllcLSStatsQuenchOff,_i:qllcLSStatsQuenchOn,_j:qllcLSStatsInPaks,_k:qllcLSStatsOutPaks,_l:qllcLSStatsInBytes,_m:qllcLSStatsOutBytes,_n:qllcLSStatsNumRcvQsms,_o:qllcLSStatsNumSndQsms,_p:qllcLSStatsNumRcvDiscs,_q:qllcLSStatsNumSndDiscs,_r:qllcLSStatsNumRcvDms,_s:qllcLSStatsNumSndDms,_t:qllcLSStatsNumRcvFrmrs,_u:qllcLSStatsNumSndFrmrs,_v:qllcLSStatsNumDrops,_w:qllcLSStatsNumErrs,'qllcMibConformance':qllcMibConformance,'qllcMibCompliances':qllcMibCompliances,'qllcMibCompliance':qllcMibCompliance,'qllcMibGroups':qllcMibGroups,_x:qllcLSAdminGroup,_y:qllcLSOperGroup,_z:qllcLSStatsGroup})