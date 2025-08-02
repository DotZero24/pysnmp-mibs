_y='udldPortTrapGroup'
_x='udldPortNeighborStatsGroup'
_w='udldPortStatsGroup'
_v='udldPortConfigGroup'
_u='udldPortBaseGroup'
_t='udldStateChange'
_s='alaUdldNumEchoRcvd'
_r='alaUdldNumHelloRcvd'
_q='alaUdldNeighborName'
_p='alaUdldPortNumFlushRcvd'
_o='alaUdldPortNumInvalidRcvd'
_n='alaUdldPortNumEchoSent'
_m='alaUdldPortNumProbeSent'
_l='alaUdldPortStatsClear'
_k='alaUdldNumUDLDNeighbors'
_j='alaUdldPortConfigUdldOperationalStatus'
_i='alaUdldPortConfigUdldDetectionPeriodTimer'
_h='alaUdldPortConfigUdldProbeIntervalTimer'
_g='alaUdldPortConfigUdldMode'
_f='alaUdldPortConfigUdldStatus'
_e='alaUdldGlobalConfigUdldDetectionPeriodTimer'
_d='alaUdldGlobalConfigUdldProbeIntervalTimer'
_c='alaUdldGlobalConfigUdldMode'
_b='alaUdldGlobalClearStats'
_a='alaUdldGlobalStatus'
_Z='alaUdldNeighborIfIndex'
_Y='alaUdldPortNeighborStatsIfIndex'
_X='alaUdldPortStatsIfIndex'
_W='alaUdldPortConfigIfIndex'
_V='aggressive'
_U='normal'
_T='default'
_S='disable'
_R='enable'
_Q='SnmpAdminString'
_P='alaUdldPortIfIndex'
_O='alaUdldCurrentState'
_N='alaUdldPrevState'
_M='accessible-for-notify'
_L='bidirectional'
_K='undetermined'
_J='shutdown'
_I='notapplicable'
_H='not-accessible'
_G='seconds'
_F='Unsigned32'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='ALCATEL-ENT1-UDLD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1Udld,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1Udld')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_Q)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
alcatelIND1UDLDMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,44,1))
if mibBuilder.loadTexts:alcatelIND1UDLDMIB.setRevisions(('2007-02-14 00:00',))
_AlcatelIND1UDLDMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1UDLDMIBObjects=_AlcatelIND1UDLDMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,44,1,1))
if mibBuilder.loadTexts:alcatelIND1UDLDMIBObjects.setStatus(_A)
class _AlaUdldGlobalStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_AlaUdldGlobalStatus_Type.__name__=_C
_AlaUdldGlobalStatus_Object=MibScalar
alaUdldGlobalStatus=_AlaUdldGlobalStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,1),_AlaUdldGlobalStatus_Type())
alaUdldGlobalStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaUdldGlobalStatus.setStatus(_A)
class _AlaUdldGlobalClearStats_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),('reset',1)))
_AlaUdldGlobalClearStats_Type.__name__=_C
_AlaUdldGlobalClearStats_Object=MibScalar
alaUdldGlobalClearStats=_AlaUdldGlobalClearStats_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,2),_AlaUdldGlobalClearStats_Type())
alaUdldGlobalClearStats.setMaxAccess(_D)
if mibBuilder.loadTexts:alaUdldGlobalClearStats.setStatus(_A)
class _AlaUdldGlobalConfigUdldMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_AlaUdldGlobalConfigUdldMode_Type.__name__=_C
_AlaUdldGlobalConfigUdldMode_Object=MibScalar
alaUdldGlobalConfigUdldMode=_AlaUdldGlobalConfigUdldMode_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,3),_AlaUdldGlobalConfigUdldMode_Type())
alaUdldGlobalConfigUdldMode.setMaxAccess(_D)
if mibBuilder.loadTexts:alaUdldGlobalConfigUdldMode.setStatus(_A)
class _AlaUdldGlobalConfigUdldProbeIntervalTimer_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(7,90))
_AlaUdldGlobalConfigUdldProbeIntervalTimer_Type.__name__=_F
_AlaUdldGlobalConfigUdldProbeIntervalTimer_Object=MibScalar
alaUdldGlobalConfigUdldProbeIntervalTimer=_AlaUdldGlobalConfigUdldProbeIntervalTimer_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,4),_AlaUdldGlobalConfigUdldProbeIntervalTimer_Type())
alaUdldGlobalConfigUdldProbeIntervalTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:alaUdldGlobalConfigUdldProbeIntervalTimer.setStatus(_A)
if mibBuilder.loadTexts:alaUdldGlobalConfigUdldProbeIntervalTimer.setUnits(_G)
class _AlaUdldGlobalConfigUdldDetectionPeriodTimer_Type(Unsigned32):defaultValue=8;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,15))
_AlaUdldGlobalConfigUdldDetectionPeriodTimer_Type.__name__=_F
_AlaUdldGlobalConfigUdldDetectionPeriodTimer_Object=MibScalar
alaUdldGlobalConfigUdldDetectionPeriodTimer=_AlaUdldGlobalConfigUdldDetectionPeriodTimer_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,5),_AlaUdldGlobalConfigUdldDetectionPeriodTimer_Type())
alaUdldGlobalConfigUdldDetectionPeriodTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:alaUdldGlobalConfigUdldDetectionPeriodTimer.setStatus(_A)
if mibBuilder.loadTexts:alaUdldGlobalConfigUdldDetectionPeriodTimer.setUnits(_G)
_UdldPortConfig_ObjectIdentity=ObjectIdentity
udldPortConfig=_UdldPortConfig_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,6))
_AlaUdldPortConfigTable_Object=MibTable
alaUdldPortConfigTable=_AlaUdldPortConfigTable_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,6,1))
if mibBuilder.loadTexts:alaUdldPortConfigTable.setStatus(_A)
_AlaUdldPortConfigEntry_Object=MibTableRow
alaUdldPortConfigEntry=_AlaUdldPortConfigEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,6,1,1))
alaUdldPortConfigEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:alaUdldPortConfigEntry.setStatus(_A)
_AlaUdldPortConfigIfIndex_Type=InterfaceIndex
_AlaUdldPortConfigIfIndex_Object=MibTableColumn
alaUdldPortConfigIfIndex=_AlaUdldPortConfigIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,6,1,1,1),_AlaUdldPortConfigIfIndex_Type())
alaUdldPortConfigIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:alaUdldPortConfigIfIndex.setStatus(_A)
class _AlaUdldPortConfigUdldStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_AlaUdldPortConfigUdldStatus_Type.__name__=_C
_AlaUdldPortConfigUdldStatus_Object=MibTableColumn
alaUdldPortConfigUdldStatus=_AlaUdldPortConfigUdldStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,6,1,1,2),_AlaUdldPortConfigUdldStatus_Type())
alaUdldPortConfigUdldStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaUdldPortConfigUdldStatus.setStatus(_A)
class _AlaUdldPortConfigUdldMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_AlaUdldPortConfigUdldMode_Type.__name__=_C
_AlaUdldPortConfigUdldMode_Object=MibTableColumn
alaUdldPortConfigUdldMode=_AlaUdldPortConfigUdldMode_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,6,1,1,3),_AlaUdldPortConfigUdldMode_Type())
alaUdldPortConfigUdldMode.setMaxAccess(_D)
if mibBuilder.loadTexts:alaUdldPortConfigUdldMode.setStatus(_A)
class _AlaUdldPortConfigUdldProbeIntervalTimer_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(7,90))
_AlaUdldPortConfigUdldProbeIntervalTimer_Type.__name__=_F
_AlaUdldPortConfigUdldProbeIntervalTimer_Object=MibTableColumn
alaUdldPortConfigUdldProbeIntervalTimer=_AlaUdldPortConfigUdldProbeIntervalTimer_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,6,1,1,4),_AlaUdldPortConfigUdldProbeIntervalTimer_Type())
alaUdldPortConfigUdldProbeIntervalTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:alaUdldPortConfigUdldProbeIntervalTimer.setStatus(_A)
if mibBuilder.loadTexts:alaUdldPortConfigUdldProbeIntervalTimer.setUnits(_G)
class _AlaUdldPortConfigUdldDetectionPeriodTimer_Type(Unsigned32):defaultValue=8;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,15))
_AlaUdldPortConfigUdldDetectionPeriodTimer_Type.__name__=_F
_AlaUdldPortConfigUdldDetectionPeriodTimer_Object=MibTableColumn
alaUdldPortConfigUdldDetectionPeriodTimer=_AlaUdldPortConfigUdldDetectionPeriodTimer_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,6,1,1,5),_AlaUdldPortConfigUdldDetectionPeriodTimer_Type())
alaUdldPortConfigUdldDetectionPeriodTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:alaUdldPortConfigUdldDetectionPeriodTimer.setStatus(_A)
if mibBuilder.loadTexts:alaUdldPortConfigUdldDetectionPeriodTimer.setUnits(_G)
class _AlaUdldPortConfigUdldOperationalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3)))
_AlaUdldPortConfigUdldOperationalStatus_Type.__name__=_C
_AlaUdldPortConfigUdldOperationalStatus_Object=MibTableColumn
alaUdldPortConfigUdldOperationalStatus=_AlaUdldPortConfigUdldOperationalStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,6,1,1,6),_AlaUdldPortConfigUdldOperationalStatus_Type())
alaUdldPortConfigUdldOperationalStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaUdldPortConfigUdldOperationalStatus.setStatus(_A)
_UdldPortStats_ObjectIdentity=ObjectIdentity
udldPortStats=_UdldPortStats_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,7))
_AlaUdldPortStatsTable_Object=MibTable
alaUdldPortStatsTable=_AlaUdldPortStatsTable_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,7,1))
if mibBuilder.loadTexts:alaUdldPortStatsTable.setStatus(_A)
_AlaUdldPortStatsEntry_Object=MibTableRow
alaUdldPortStatsEntry=_AlaUdldPortStatsEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,7,1,1))
alaUdldPortStatsEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:alaUdldPortStatsEntry.setStatus(_A)
_AlaUdldPortStatsIfIndex_Type=InterfaceIndex
_AlaUdldPortStatsIfIndex_Object=MibTableColumn
alaUdldPortStatsIfIndex=_AlaUdldPortStatsIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,7,1,1,1),_AlaUdldPortStatsIfIndex_Type())
alaUdldPortStatsIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:alaUdldPortStatsIfIndex.setStatus(_A)
class _AlaUdldNumUDLDNeighbors_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AlaUdldNumUDLDNeighbors_Type.__name__=_F
_AlaUdldNumUDLDNeighbors_Object=MibTableColumn
alaUdldNumUDLDNeighbors=_AlaUdldNumUDLDNeighbors_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,7,1,1,2),_AlaUdldNumUDLDNeighbors_Type())
alaUdldNumUDLDNeighbors.setMaxAccess(_E)
if mibBuilder.loadTexts:alaUdldNumUDLDNeighbors.setStatus(_A)
class _AlaUdldPortStatsClear_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),('reset',1)))
_AlaUdldPortStatsClear_Type.__name__=_C
_AlaUdldPortStatsClear_Object=MibTableColumn
alaUdldPortStatsClear=_AlaUdldPortStatsClear_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,7,1,1,3),_AlaUdldPortStatsClear_Type())
alaUdldPortStatsClear.setMaxAccess(_D)
if mibBuilder.loadTexts:alaUdldPortStatsClear.setStatus(_A)
_AlaUdldPortNumProbeSent_Type=Counter32
_AlaUdldPortNumProbeSent_Object=MibTableColumn
alaUdldPortNumProbeSent=_AlaUdldPortNumProbeSent_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,7,1,1,4),_AlaUdldPortNumProbeSent_Type())
alaUdldPortNumProbeSent.setMaxAccess(_E)
if mibBuilder.loadTexts:alaUdldPortNumProbeSent.setStatus(_A)
_AlaUdldPortNumEchoSent_Type=Counter32
_AlaUdldPortNumEchoSent_Object=MibTableColumn
alaUdldPortNumEchoSent=_AlaUdldPortNumEchoSent_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,7,1,1,5),_AlaUdldPortNumEchoSent_Type())
alaUdldPortNumEchoSent.setMaxAccess(_E)
if mibBuilder.loadTexts:alaUdldPortNumEchoSent.setStatus(_A)
_AlaUdldPortNumInvalidRcvd_Type=Counter32
_AlaUdldPortNumInvalidRcvd_Object=MibTableColumn
alaUdldPortNumInvalidRcvd=_AlaUdldPortNumInvalidRcvd_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,7,1,1,6),_AlaUdldPortNumInvalidRcvd_Type())
alaUdldPortNumInvalidRcvd.setMaxAccess(_E)
if mibBuilder.loadTexts:alaUdldPortNumInvalidRcvd.setStatus(_A)
_AlaUdldPortNumFlushRcvd_Type=Counter32
_AlaUdldPortNumFlushRcvd_Object=MibTableColumn
alaUdldPortNumFlushRcvd=_AlaUdldPortNumFlushRcvd_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,7,1,1,7),_AlaUdldPortNumFlushRcvd_Type())
alaUdldPortNumFlushRcvd.setMaxAccess(_E)
if mibBuilder.loadTexts:alaUdldPortNumFlushRcvd.setStatus(_A)
_UdldPortNeighborStats_ObjectIdentity=ObjectIdentity
udldPortNeighborStats=_UdldPortNeighborStats_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,8))
_AlaUdldPortNeighborStatsTable_Object=MibTable
alaUdldPortNeighborStatsTable=_AlaUdldPortNeighborStatsTable_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,8,1))
if mibBuilder.loadTexts:alaUdldPortNeighborStatsTable.setStatus(_A)
_AlaUdldPortNeighborStatsEntry_Object=MibTableRow
alaUdldPortNeighborStatsEntry=_AlaUdldPortNeighborStatsEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,8,1,1))
alaUdldPortNeighborStatsEntry.setIndexNames((0,_B,_Y),(0,_B,_Z))
if mibBuilder.loadTexts:alaUdldPortNeighborStatsEntry.setStatus(_A)
_AlaUdldPortNeighborStatsIfIndex_Type=InterfaceIndex
_AlaUdldPortNeighborStatsIfIndex_Object=MibTableColumn
alaUdldPortNeighborStatsIfIndex=_AlaUdldPortNeighborStatsIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,8,1,1,1),_AlaUdldPortNeighborStatsIfIndex_Type())
alaUdldPortNeighborStatsIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:alaUdldPortNeighborStatsIfIndex.setStatus(_A)
class _AlaUdldNeighborIfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_AlaUdldNeighborIfIndex_Type.__name__=_F
_AlaUdldNeighborIfIndex_Object=MibTableColumn
alaUdldNeighborIfIndex=_AlaUdldNeighborIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,8,1,1,2),_AlaUdldNeighborIfIndex_Type())
alaUdldNeighborIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:alaUdldNeighborIfIndex.setStatus(_A)
class _AlaUdldNeighborName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AlaUdldNeighborName_Type.__name__=_Q
_AlaUdldNeighborName_Object=MibTableColumn
alaUdldNeighborName=_AlaUdldNeighborName_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,8,1,1,3),_AlaUdldNeighborName_Type())
alaUdldNeighborName.setMaxAccess(_E)
if mibBuilder.loadTexts:alaUdldNeighborName.setStatus(_A)
_AlaUdldNumHelloRcvd_Type=Counter32
_AlaUdldNumHelloRcvd_Object=MibTableColumn
alaUdldNumHelloRcvd=_AlaUdldNumHelloRcvd_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,8,1,1,4),_AlaUdldNumHelloRcvd_Type())
alaUdldNumHelloRcvd.setMaxAccess(_E)
if mibBuilder.loadTexts:alaUdldNumHelloRcvd.setStatus(_A)
_AlaUdldNumEchoRcvd_Type=Counter32
_AlaUdldNumEchoRcvd_Object=MibTableColumn
alaUdldNumEchoRcvd=_AlaUdldNumEchoRcvd_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,8,1,1,5),_AlaUdldNumEchoRcvd_Type())
alaUdldNumEchoRcvd.setMaxAccess(_E)
if mibBuilder.loadTexts:alaUdldNumEchoRcvd.setStatus(_A)
class _AlaUdldPrevState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3)))
_AlaUdldPrevState_Type.__name__=_C
_AlaUdldPrevState_Object=MibScalar
alaUdldPrevState=_AlaUdldPrevState_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,9),_AlaUdldPrevState_Type())
alaUdldPrevState.setMaxAccess(_M)
if mibBuilder.loadTexts:alaUdldPrevState.setStatus(_A)
class _AlaUdldCurrentState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3)))
_AlaUdldCurrentState_Type.__name__=_C
_AlaUdldCurrentState_Object=MibScalar
alaUdldCurrentState=_AlaUdldCurrentState_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,10),_AlaUdldCurrentState_Type())
alaUdldCurrentState.setMaxAccess(_M)
if mibBuilder.loadTexts:alaUdldCurrentState.setStatus(_A)
_AlaUdldPortIfIndex_Type=InterfaceIndex
_AlaUdldPortIfIndex_Object=MibScalar
alaUdldPortIfIndex=_AlaUdldPortIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,44,1,1,11),_AlaUdldPortIfIndex_Type())
alaUdldPortIfIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:alaUdldPortIfIndex.setStatus(_A)
_AlcatelIND1UDLDMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1UDLDMIBConformance=_AlcatelIND1UDLDMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,44,1,2))
if mibBuilder.loadTexts:alcatelIND1UDLDMIBConformance.setStatus(_A)
_AlcatelIND1UDLDMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1UDLDMIBGroups=_AlcatelIND1UDLDMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,44,1,2,1))
if mibBuilder.loadTexts:alcatelIND1UDLDMIBGroups.setStatus(_A)
_AlcatelIND1UDLDMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1UDLDMIBCompliances=_AlcatelIND1UDLDMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,44,1,2,2))
if mibBuilder.loadTexts:alcatelIND1UDLDMIBCompliances.setStatus(_A)
_AlaUdldEvents_ObjectIdentity=ObjectIdentity
alaUdldEvents=_AlaUdldEvents_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,44,1,3))
udldPortBaseGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,44,1,2,1,1))
udldPortBaseGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:udldPortBaseGroup.setStatus(_A)
udldPortConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,44,1,2,1,2))
udldPortConfigGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:udldPortConfigGroup.setStatus(_A)
udldPortStatsGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,44,1,2,1,3))
udldPortStatsGroup.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:udldPortStatsGroup.setStatus(_A)
udldPortNeighborStatsGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,44,1,2,1,4))
udldPortNeighborStatsGroup.setObjects(*((_B,_q),(_B,_r),(_B,_s)))
if mibBuilder.loadTexts:udldPortNeighborStatsGroup.setStatus(_A)
udldStateChange=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,44,1,3,0,1))
udldStateChange.setObjects(*((_B,_P),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:udldStateChange.setStatus(_A)
udldPortTrapGroup=NotificationGroup((1,3,6,1,4,1,6486,801,1,2,1,44,1,2,1,5))
udldPortTrapGroup.setObjects((_B,_t))
if mibBuilder.loadTexts:udldPortTrapGroup.setStatus(_A)
alcatelIND1UDLDMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,44,1,2,2,1))
alcatelIND1UDLDMIBCompliance.setObjects(*((_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:alcatelIND1UDLDMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1UDLDMIB':alcatelIND1UDLDMIB,'alcatelIND1UDLDMIBObjects':alcatelIND1UDLDMIBObjects,_a:alaUdldGlobalStatus,_b:alaUdldGlobalClearStats,_c:alaUdldGlobalConfigUdldMode,_d:alaUdldGlobalConfigUdldProbeIntervalTimer,_e:alaUdldGlobalConfigUdldDetectionPeriodTimer,'udldPortConfig':udldPortConfig,'alaUdldPortConfigTable':alaUdldPortConfigTable,'alaUdldPortConfigEntry':alaUdldPortConfigEntry,_W:alaUdldPortConfigIfIndex,_f:alaUdldPortConfigUdldStatus,_g:alaUdldPortConfigUdldMode,_h:alaUdldPortConfigUdldProbeIntervalTimer,_i:alaUdldPortConfigUdldDetectionPeriodTimer,_j:alaUdldPortConfigUdldOperationalStatus,'udldPortStats':udldPortStats,'alaUdldPortStatsTable':alaUdldPortStatsTable,'alaUdldPortStatsEntry':alaUdldPortStatsEntry,_X:alaUdldPortStatsIfIndex,_k:alaUdldNumUDLDNeighbors,_l:alaUdldPortStatsClear,_m:alaUdldPortNumProbeSent,_n:alaUdldPortNumEchoSent,_o:alaUdldPortNumInvalidRcvd,_p:alaUdldPortNumFlushRcvd,'udldPortNeighborStats':udldPortNeighborStats,'alaUdldPortNeighborStatsTable':alaUdldPortNeighborStatsTable,'alaUdldPortNeighborStatsEntry':alaUdldPortNeighborStatsEntry,_Y:alaUdldPortNeighborStatsIfIndex,_Z:alaUdldNeighborIfIndex,_q:alaUdldNeighborName,_r:alaUdldNumHelloRcvd,_s:alaUdldNumEchoRcvd,_N:alaUdldPrevState,_O:alaUdldCurrentState,_P:alaUdldPortIfIndex,'alcatelIND1UDLDMIBConformance':alcatelIND1UDLDMIBConformance,'alcatelIND1UDLDMIBGroups':alcatelIND1UDLDMIBGroups,_u:udldPortBaseGroup,_v:udldPortConfigGroup,_w:udldPortStatsGroup,_x:udldPortNeighborStatsGroup,_y:udldPortTrapGroup,'alcatelIND1UDLDMIBCompliances':alcatelIND1UDLDMIBCompliances,'alcatelIND1UDLDMIBCompliance':alcatelIND1UDLDMIBCompliance,'alaUdldEvents':alaUdldEvents,_t:udldStateChange})