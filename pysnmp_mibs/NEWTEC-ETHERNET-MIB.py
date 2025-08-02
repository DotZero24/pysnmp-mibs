_Ac='ntcEtherConfGrpV1Standard'
_Ab='ntcEtherDataIgmpVersion'
_Aa='ntcEtherAlmSatEthGenIfFail'
_AZ='ntcEtherAlmDataEthGenIfFail'
_AY='ntcEtherAlmMgmtEthGenIfFail'
_AX='ntcEtherAlmSatEthInterfaceFail'
_AW='ntcEtherAlmSat2EthHalfDuplex'
_AV='ntcEtherAlmSat2EthLinkFail'
_AU='ntcEtherAlmSat1EthHalfDuplex'
_AT='ntcEtherAlmSat1EthLinkFail'
_AS='ntcEtherAlmDataEthInterfaceFail'
_AR='ntcEtherAlmMgmtEthInterfaceFail'
_AQ='ntcEtherAlmMgmtFpEthHalfDuplex'
_AP='ntcEtherAlmMgmtFpEthLinkFail'
_AO='ntcEtherAlmData2EthHalfDuplex'
_AN='ntcEtherAlmData2EthLinkFail'
_AM='ntcEtherAlmData1EthHalfDuplex'
_AL='ntcEtherAlmData1EthLinkFail'
_AK='ntcEtherAlmMgmt2EthHalfDuplex'
_AJ='ntcEtherAlmMgmt2EthLinkFail'
_AI='ntcEtherAlmMgmt1EthHalfDuplex'
_AH='ntcEtherAlmMgmt1EthLinkFail'
_AG='ntcEtherIfRedSatActiveInterface'
_AF='ntcEtherIfRedSatSwitchCount'
_AE='ntcEtherIfRedSatSwitchOrder'
_AD='ntcEtherIfRedDataGwUnreachImpact'
_AC='ntcEtherIfRedDataActiveInterface'
_AB='ntcEtherIfRedDataSwitchCount'
_AA='ntcEtherIfRedDataSwitchOrder'
_A9='ntcEtherIfRedMgmtActiveInterface'
_A8='ntcEtherIfRedMgmtSwitchCount'
_A7='ntcEtherIfRedMgmtSwitchOrder'
_A6='ntcEtherStatDataOutputerrors'
_A5='ntcEtherStatDataInputErrors'
_A4='ntcEtherStatDataOutputDropped'
_A3='ntcEtherStatDataOutputPackets'
_A2='ntcEtherStatDataOutputBytes'
_A1='ntcEtherStatDataInputDropped'
_A0='ntcEtherStatDataInputPackets'
_z='ntcEtherStatDataInputBytes'
_y='ntcEtherStatMgmtOutputerrors'
_x='ntcEtherStatMgmtInputErrors'
_w='ntcEtherStatMgmtOutputDropped'
_v='ntcEtherStatMgmtOutputPackets'
_u='ntcEtherStatMgmtOutputBytes'
_t='ntcEtherStatMgmtInputDropped'
_s='ntcEtherStatMgmtInputPackets'
_r='ntcEtherStatMgmtInputBytes'
_q='ntcEtherLinkDataMtu'
_p='ntcEtherLinkDataLinkState'
_o='ntcEtherLinkDataForcedSpeed'
_n='ntcEtherLinkDataAdvertisedSpeeds'
_m='ntcEtherLinkDataAutoNegotiation'
_l='ntcEtherLinkDataMacAddress'
_k='ntcEtherLinkDataEnable'
_j='ntcEtherLinkMgmtMtu'
_i='ntcEtherLinkMgmtLinkState'
_h='ntcEtherLinkMgmtForcedSpeed'
_g='ntcEtherLinkMgmtAdvertisedSpeeds'
_f='ntcEtherLinkMgmtAutoNegotiation'
_e='ntcEtherLinkMgmtMacAddress'
_d='ntcEtherLinkMgmtEnable'
_c='ntcEtherStatDataInterface'
_b='ntcEtherStatMgmtInterface'
_a='ntcEtherLinkDataInterface'
_Z='e10GSFPplus'
_Y='linkDown'
_X='mgmtfp'
_W='ntcEtherLinkMgmtInterface'
_V='mgmt2'
_U='mgmt1'
_T='Unsigned32'
_S='bytes'
_R='sat2'
_Q='sat1'
_P='data2'
_O='data1'
_N='e1000BTFullDuplex'
_M='not-accessible'
_L='NtcEnable'
_K='none'
_J='e100BTFullDuplex'
_I='e100BTHalfDuplex'
_H='e10BTFullDuplex'
_G='e10BTHalfDuplex'
_F='packets'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='NEWTEC-ETHERNET-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcAlarmState,NtcEnable=mibBuilder.importSymbols('NEWTEC-TC-MIB','NtcAlarmState',_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_T,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
ntcEthernet=ModuleIdentity((1,3,6,1,4,1,5835,5,2,500))
if mibBuilder.loadTexts:ntcEthernet.setRevisions(('2018-02-02 09:00','2017-07-10 12:00','2014-11-24 12:00','2013-05-22 06:00','2013-03-27 10:00','2013-01-08 12:00','2012-06-28 12:00'))
_NtcEtherObjects_ObjectIdentity=ObjectIdentity
ntcEtherObjects=_NtcEtherObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,500,1))
if mibBuilder.loadTexts:ntcEtherObjects.setStatus(_A)
_NtcEtherLinkMgmtTable_Object=MibTable
ntcEtherLinkMgmtTable=_NtcEtherLinkMgmtTable_Object((1,3,6,1,4,1,5835,5,2,500,1,1))
if mibBuilder.loadTexts:ntcEtherLinkMgmtTable.setStatus(_A)
_NtcEtherLinkMgmtEntry_Object=MibTableRow
ntcEtherLinkMgmtEntry=_NtcEtherLinkMgmtEntry_Object((1,3,6,1,4,1,5835,5,2,500,1,1,1))
ntcEtherLinkMgmtEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:ntcEtherLinkMgmtEntry.setStatus(_A)
class _NtcEtherLinkMgmtInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_U,0),(_V,1),(_X,2)))
_NtcEtherLinkMgmtInterface_Type.__name__=_D
_NtcEtherLinkMgmtInterface_Object=MibTableColumn
ntcEtherLinkMgmtInterface=_NtcEtherLinkMgmtInterface_Object((1,3,6,1,4,1,5835,5,2,500,1,1,1,1),_NtcEtherLinkMgmtInterface_Type())
ntcEtherLinkMgmtInterface.setMaxAccess(_M)
if mibBuilder.loadTexts:ntcEtherLinkMgmtInterface.setStatus(_A)
class _NtcEtherLinkMgmtEnable_Type(NtcEnable):defaultValue=0
_NtcEtherLinkMgmtEnable_Type.__name__=_L
_NtcEtherLinkMgmtEnable_Object=MibTableColumn
ntcEtherLinkMgmtEnable=_NtcEtherLinkMgmtEnable_Object((1,3,6,1,4,1,5835,5,2,500,1,1,1,2),_NtcEtherLinkMgmtEnable_Type())
ntcEtherLinkMgmtEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcEtherLinkMgmtEnable.setStatus(_A)
_NtcEtherLinkMgmtMacAddress_Type=MacAddress
_NtcEtherLinkMgmtMacAddress_Object=MibTableColumn
ntcEtherLinkMgmtMacAddress=_NtcEtherLinkMgmtMacAddress_Object((1,3,6,1,4,1,5835,5,2,500,1,1,1,3),_NtcEtherLinkMgmtMacAddress_Type())
ntcEtherLinkMgmtMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherLinkMgmtMacAddress.setStatus(_A)
class _NtcEtherLinkMgmtAutoNegotiation_Type(NtcEnable):defaultValue=1
_NtcEtherLinkMgmtAutoNegotiation_Type.__name__=_L
_NtcEtherLinkMgmtAutoNegotiation_Object=MibTableColumn
ntcEtherLinkMgmtAutoNegotiation=_NtcEtherLinkMgmtAutoNegotiation_Object((1,3,6,1,4,1,5835,5,2,500,1,1,1,4),_NtcEtherLinkMgmtAutoNegotiation_Type())
ntcEtherLinkMgmtAutoNegotiation.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcEtherLinkMgmtAutoNegotiation.setStatus(_A)
class _NtcEtherLinkMgmtAdvertisedSpeeds_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('all',0),(_G,1),(_H,2),(_I,3),(_J,4),(_N,5)))
_NtcEtherLinkMgmtAdvertisedSpeeds_Type.__name__=_D
_NtcEtherLinkMgmtAdvertisedSpeeds_Object=MibTableColumn
ntcEtherLinkMgmtAdvertisedSpeeds=_NtcEtherLinkMgmtAdvertisedSpeeds_Object((1,3,6,1,4,1,5835,5,2,500,1,1,1,5),_NtcEtherLinkMgmtAdvertisedSpeeds_Type())
ntcEtherLinkMgmtAdvertisedSpeeds.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcEtherLinkMgmtAdvertisedSpeeds.setStatus(_A)
class _NtcEtherLinkMgmtForcedSpeed_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4)))
_NtcEtherLinkMgmtForcedSpeed_Type.__name__=_D
_NtcEtherLinkMgmtForcedSpeed_Object=MibTableColumn
ntcEtherLinkMgmtForcedSpeed=_NtcEtherLinkMgmtForcedSpeed_Object((1,3,6,1,4,1,5835,5,2,500,1,1,1,6),_NtcEtherLinkMgmtForcedSpeed_Type())
ntcEtherLinkMgmtForcedSpeed.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcEtherLinkMgmtForcedSpeed.setStatus(_A)
class _NtcEtherLinkMgmtLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_Y,0),(_G,1),(_H,2),(_I,3),(_J,4),(_N,5),(_Z,6)))
_NtcEtherLinkMgmtLinkState_Type.__name__=_D
_NtcEtherLinkMgmtLinkState_Object=MibTableColumn
ntcEtherLinkMgmtLinkState=_NtcEtherLinkMgmtLinkState_Object((1,3,6,1,4,1,5835,5,2,500,1,1,1,7),_NtcEtherLinkMgmtLinkState_Type())
ntcEtherLinkMgmtLinkState.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherLinkMgmtLinkState.setStatus(_A)
class _NtcEtherLinkMgmtMtu_Type(Unsigned32):defaultValue=1500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(68,9216))
_NtcEtherLinkMgmtMtu_Type.__name__=_T
_NtcEtherLinkMgmtMtu_Object=MibTableColumn
ntcEtherLinkMgmtMtu=_NtcEtherLinkMgmtMtu_Object((1,3,6,1,4,1,5835,5,2,500,1,1,1,8),_NtcEtherLinkMgmtMtu_Type())
ntcEtherLinkMgmtMtu.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcEtherLinkMgmtMtu.setStatus(_A)
_NtcEtherLinkDataTable_Object=MibTable
ntcEtherLinkDataTable=_NtcEtherLinkDataTable_Object((1,3,6,1,4,1,5835,5,2,500,1,2))
if mibBuilder.loadTexts:ntcEtherLinkDataTable.setStatus(_A)
_NtcEtherLinkDataEntry_Object=MibTableRow
ntcEtherLinkDataEntry=_NtcEtherLinkDataEntry_Object((1,3,6,1,4,1,5835,5,2,500,1,2,1))
ntcEtherLinkDataEntry.setIndexNames((0,_B,_a))
if mibBuilder.loadTexts:ntcEtherLinkDataEntry.setStatus(_A)
class _NtcEtherLinkDataInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_O,0),(_P,1),(_Q,2),(_R,3)))
_NtcEtherLinkDataInterface_Type.__name__=_D
_NtcEtherLinkDataInterface_Object=MibTableColumn
ntcEtherLinkDataInterface=_NtcEtherLinkDataInterface_Object((1,3,6,1,4,1,5835,5,2,500,1,2,1,1),_NtcEtherLinkDataInterface_Type())
ntcEtherLinkDataInterface.setMaxAccess(_M)
if mibBuilder.loadTexts:ntcEtherLinkDataInterface.setStatus(_A)
class _NtcEtherLinkDataEnable_Type(NtcEnable):defaultValue=0
_NtcEtherLinkDataEnable_Type.__name__=_L
_NtcEtherLinkDataEnable_Object=MibTableColumn
ntcEtherLinkDataEnable=_NtcEtherLinkDataEnable_Object((1,3,6,1,4,1,5835,5,2,500,1,2,1,2),_NtcEtherLinkDataEnable_Type())
ntcEtherLinkDataEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcEtherLinkDataEnable.setStatus(_A)
_NtcEtherLinkDataMacAddress_Type=MacAddress
_NtcEtherLinkDataMacAddress_Object=MibTableColumn
ntcEtherLinkDataMacAddress=_NtcEtherLinkDataMacAddress_Object((1,3,6,1,4,1,5835,5,2,500,1,2,1,3),_NtcEtherLinkDataMacAddress_Type())
ntcEtherLinkDataMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherLinkDataMacAddress.setStatus(_A)
class _NtcEtherLinkDataAutoNegotiation_Type(NtcEnable):defaultValue=1
_NtcEtherLinkDataAutoNegotiation_Type.__name__=_L
_NtcEtherLinkDataAutoNegotiation_Object=MibTableColumn
ntcEtherLinkDataAutoNegotiation=_NtcEtherLinkDataAutoNegotiation_Object((1,3,6,1,4,1,5835,5,2,500,1,2,1,4),_NtcEtherLinkDataAutoNegotiation_Type())
ntcEtherLinkDataAutoNegotiation.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcEtherLinkDataAutoNegotiation.setStatus(_A)
class _NtcEtherLinkDataAdvertisedSpeeds_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('all',0),(_G,1),(_H,2),(_I,3),(_J,4),(_N,5)))
_NtcEtherLinkDataAdvertisedSpeeds_Type.__name__=_D
_NtcEtherLinkDataAdvertisedSpeeds_Object=MibTableColumn
ntcEtherLinkDataAdvertisedSpeeds=_NtcEtherLinkDataAdvertisedSpeeds_Object((1,3,6,1,4,1,5835,5,2,500,1,2,1,5),_NtcEtherLinkDataAdvertisedSpeeds_Type())
ntcEtherLinkDataAdvertisedSpeeds.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcEtherLinkDataAdvertisedSpeeds.setStatus(_A)
class _NtcEtherLinkDataForcedSpeed_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4)))
_NtcEtherLinkDataForcedSpeed_Type.__name__=_D
_NtcEtherLinkDataForcedSpeed_Object=MibTableColumn
ntcEtherLinkDataForcedSpeed=_NtcEtherLinkDataForcedSpeed_Object((1,3,6,1,4,1,5835,5,2,500,1,2,1,6),_NtcEtherLinkDataForcedSpeed_Type())
ntcEtherLinkDataForcedSpeed.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcEtherLinkDataForcedSpeed.setStatus(_A)
class _NtcEtherLinkDataLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_Y,0),(_G,1),(_H,2),(_I,3),(_J,4),(_N,5),(_Z,6)))
_NtcEtherLinkDataLinkState_Type.__name__=_D
_NtcEtherLinkDataLinkState_Object=MibTableColumn
ntcEtherLinkDataLinkState=_NtcEtherLinkDataLinkState_Object((1,3,6,1,4,1,5835,5,2,500,1,2,1,7),_NtcEtherLinkDataLinkState_Type())
ntcEtherLinkDataLinkState.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherLinkDataLinkState.setStatus(_A)
class _NtcEtherLinkDataMtu_Type(Unsigned32):defaultValue=1500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(68,9216))
_NtcEtherLinkDataMtu_Type.__name__=_T
_NtcEtherLinkDataMtu_Object=MibTableColumn
ntcEtherLinkDataMtu=_NtcEtherLinkDataMtu_Object((1,3,6,1,4,1,5835,5,2,500,1,2,1,8),_NtcEtherLinkDataMtu_Type())
ntcEtherLinkDataMtu.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcEtherLinkDataMtu.setStatus(_A)
_NtcEtherStatMgmtTable_Object=MibTable
ntcEtherStatMgmtTable=_NtcEtherStatMgmtTable_Object((1,3,6,1,4,1,5835,5,2,500,1,3))
if mibBuilder.loadTexts:ntcEtherStatMgmtTable.setStatus(_A)
_NtcEtherStatMgmtEntry_Object=MibTableRow
ntcEtherStatMgmtEntry=_NtcEtherStatMgmtEntry_Object((1,3,6,1,4,1,5835,5,2,500,1,3,1))
ntcEtherStatMgmtEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:ntcEtherStatMgmtEntry.setStatus(_A)
class _NtcEtherStatMgmtInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_U,0),(_V,1),(_X,2),('mgmtbond',3)))
_NtcEtherStatMgmtInterface_Type.__name__=_D
_NtcEtherStatMgmtInterface_Object=MibTableColumn
ntcEtherStatMgmtInterface=_NtcEtherStatMgmtInterface_Object((1,3,6,1,4,1,5835,5,2,500,1,3,1,1),_NtcEtherStatMgmtInterface_Type())
ntcEtherStatMgmtInterface.setMaxAccess(_M)
if mibBuilder.loadTexts:ntcEtherStatMgmtInterface.setStatus(_A)
_NtcEtherStatMgmtInputBytes_Type=Counter32
_NtcEtherStatMgmtInputBytes_Object=MibTableColumn
ntcEtherStatMgmtInputBytes=_NtcEtherStatMgmtInputBytes_Object((1,3,6,1,4,1,5835,5,2,500,1,3,1,2),_NtcEtherStatMgmtInputBytes_Type())
ntcEtherStatMgmtInputBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherStatMgmtInputBytes.setStatus(_A)
if mibBuilder.loadTexts:ntcEtherStatMgmtInputBytes.setUnits(_S)
_NtcEtherStatMgmtInputPackets_Type=Counter32
_NtcEtherStatMgmtInputPackets_Object=MibTableColumn
ntcEtherStatMgmtInputPackets=_NtcEtherStatMgmtInputPackets_Object((1,3,6,1,4,1,5835,5,2,500,1,3,1,3),_NtcEtherStatMgmtInputPackets_Type())
ntcEtherStatMgmtInputPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherStatMgmtInputPackets.setStatus(_A)
if mibBuilder.loadTexts:ntcEtherStatMgmtInputPackets.setUnits(_F)
_NtcEtherStatMgmtInputDropped_Type=Counter32
_NtcEtherStatMgmtInputDropped_Object=MibTableColumn
ntcEtherStatMgmtInputDropped=_NtcEtherStatMgmtInputDropped_Object((1,3,6,1,4,1,5835,5,2,500,1,3,1,4),_NtcEtherStatMgmtInputDropped_Type())
ntcEtherStatMgmtInputDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherStatMgmtInputDropped.setStatus(_A)
if mibBuilder.loadTexts:ntcEtherStatMgmtInputDropped.setUnits(_F)
_NtcEtherStatMgmtOutputBytes_Type=Counter32
_NtcEtherStatMgmtOutputBytes_Object=MibTableColumn
ntcEtherStatMgmtOutputBytes=_NtcEtherStatMgmtOutputBytes_Object((1,3,6,1,4,1,5835,5,2,500,1,3,1,5),_NtcEtherStatMgmtOutputBytes_Type())
ntcEtherStatMgmtOutputBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherStatMgmtOutputBytes.setStatus(_A)
if mibBuilder.loadTexts:ntcEtherStatMgmtOutputBytes.setUnits(_S)
_NtcEtherStatMgmtOutputPackets_Type=Counter32
_NtcEtherStatMgmtOutputPackets_Object=MibTableColumn
ntcEtherStatMgmtOutputPackets=_NtcEtherStatMgmtOutputPackets_Object((1,3,6,1,4,1,5835,5,2,500,1,3,1,6),_NtcEtherStatMgmtOutputPackets_Type())
ntcEtherStatMgmtOutputPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherStatMgmtOutputPackets.setStatus(_A)
if mibBuilder.loadTexts:ntcEtherStatMgmtOutputPackets.setUnits(_F)
_NtcEtherStatMgmtOutputDropped_Type=Counter32
_NtcEtherStatMgmtOutputDropped_Object=MibTableColumn
ntcEtherStatMgmtOutputDropped=_NtcEtherStatMgmtOutputDropped_Object((1,3,6,1,4,1,5835,5,2,500,1,3,1,7),_NtcEtherStatMgmtOutputDropped_Type())
ntcEtherStatMgmtOutputDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherStatMgmtOutputDropped.setStatus(_A)
if mibBuilder.loadTexts:ntcEtherStatMgmtOutputDropped.setUnits(_F)
_NtcEtherStatMgmtInputErrors_Type=Counter64
_NtcEtherStatMgmtInputErrors_Object=MibTableColumn
ntcEtherStatMgmtInputErrors=_NtcEtherStatMgmtInputErrors_Object((1,3,6,1,4,1,5835,5,2,500,1,3,1,8),_NtcEtherStatMgmtInputErrors_Type())
ntcEtherStatMgmtInputErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherStatMgmtInputErrors.setStatus(_A)
if mibBuilder.loadTexts:ntcEtherStatMgmtInputErrors.setUnits(_F)
_NtcEtherStatMgmtOutputerrors_Type=Counter64
_NtcEtherStatMgmtOutputerrors_Object=MibTableColumn
ntcEtherStatMgmtOutputerrors=_NtcEtherStatMgmtOutputerrors_Object((1,3,6,1,4,1,5835,5,2,500,1,3,1,9),_NtcEtherStatMgmtOutputerrors_Type())
ntcEtherStatMgmtOutputerrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherStatMgmtOutputerrors.setStatus(_A)
if mibBuilder.loadTexts:ntcEtherStatMgmtOutputerrors.setUnits(_F)
_NtcEtherStatDataTable_Object=MibTable
ntcEtherStatDataTable=_NtcEtherStatDataTable_Object((1,3,6,1,4,1,5835,5,2,500,1,4))
if mibBuilder.loadTexts:ntcEtherStatDataTable.setStatus(_A)
_NtcEtherStatDataEntry_Object=MibTableRow
ntcEtherStatDataEntry=_NtcEtherStatDataEntry_Object((1,3,6,1,4,1,5835,5,2,500,1,4,1))
ntcEtherStatDataEntry.setIndexNames((0,_B,_c))
if mibBuilder.loadTexts:ntcEtherStatDataEntry.setStatus(_A)
class _NtcEtherStatDataInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_O,0),(_P,1),('databond',2),(_Q,3),(_R,4),('satbond',5)))
_NtcEtherStatDataInterface_Type.__name__=_D
_NtcEtherStatDataInterface_Object=MibTableColumn
ntcEtherStatDataInterface=_NtcEtherStatDataInterface_Object((1,3,6,1,4,1,5835,5,2,500,1,4,1,1),_NtcEtherStatDataInterface_Type())
ntcEtherStatDataInterface.setMaxAccess(_M)
if mibBuilder.loadTexts:ntcEtherStatDataInterface.setStatus(_A)
_NtcEtherStatDataInputBytes_Type=Counter32
_NtcEtherStatDataInputBytes_Object=MibTableColumn
ntcEtherStatDataInputBytes=_NtcEtherStatDataInputBytes_Object((1,3,6,1,4,1,5835,5,2,500,1,4,1,2),_NtcEtherStatDataInputBytes_Type())
ntcEtherStatDataInputBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherStatDataInputBytes.setStatus(_A)
if mibBuilder.loadTexts:ntcEtherStatDataInputBytes.setUnits(_S)
_NtcEtherStatDataInputPackets_Type=Counter32
_NtcEtherStatDataInputPackets_Object=MibTableColumn
ntcEtherStatDataInputPackets=_NtcEtherStatDataInputPackets_Object((1,3,6,1,4,1,5835,5,2,500,1,4,1,3),_NtcEtherStatDataInputPackets_Type())
ntcEtherStatDataInputPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherStatDataInputPackets.setStatus(_A)
if mibBuilder.loadTexts:ntcEtherStatDataInputPackets.setUnits(_F)
_NtcEtherStatDataInputDropped_Type=Counter32
_NtcEtherStatDataInputDropped_Object=MibTableColumn
ntcEtherStatDataInputDropped=_NtcEtherStatDataInputDropped_Object((1,3,6,1,4,1,5835,5,2,500,1,4,1,4),_NtcEtherStatDataInputDropped_Type())
ntcEtherStatDataInputDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherStatDataInputDropped.setStatus(_A)
if mibBuilder.loadTexts:ntcEtherStatDataInputDropped.setUnits(_F)
_NtcEtherStatDataOutputBytes_Type=Counter32
_NtcEtherStatDataOutputBytes_Object=MibTableColumn
ntcEtherStatDataOutputBytes=_NtcEtherStatDataOutputBytes_Object((1,3,6,1,4,1,5835,5,2,500,1,4,1,5),_NtcEtherStatDataOutputBytes_Type())
ntcEtherStatDataOutputBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherStatDataOutputBytes.setStatus(_A)
if mibBuilder.loadTexts:ntcEtherStatDataOutputBytes.setUnits(_S)
_NtcEtherStatDataOutputPackets_Type=Counter32
_NtcEtherStatDataOutputPackets_Object=MibTableColumn
ntcEtherStatDataOutputPackets=_NtcEtherStatDataOutputPackets_Object((1,3,6,1,4,1,5835,5,2,500,1,4,1,6),_NtcEtherStatDataOutputPackets_Type())
ntcEtherStatDataOutputPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherStatDataOutputPackets.setStatus(_A)
if mibBuilder.loadTexts:ntcEtherStatDataOutputPackets.setUnits(_F)
_NtcEtherStatDataOutputDropped_Type=Counter32
_NtcEtherStatDataOutputDropped_Object=MibTableColumn
ntcEtherStatDataOutputDropped=_NtcEtherStatDataOutputDropped_Object((1,3,6,1,4,1,5835,5,2,500,1,4,1,7),_NtcEtherStatDataOutputDropped_Type())
ntcEtherStatDataOutputDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherStatDataOutputDropped.setStatus(_A)
if mibBuilder.loadTexts:ntcEtherStatDataOutputDropped.setUnits(_F)
_NtcEtherStatDataInputErrors_Type=Counter64
_NtcEtherStatDataInputErrors_Object=MibTableColumn
ntcEtherStatDataInputErrors=_NtcEtherStatDataInputErrors_Object((1,3,6,1,4,1,5835,5,2,500,1,4,1,8),_NtcEtherStatDataInputErrors_Type())
ntcEtherStatDataInputErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherStatDataInputErrors.setStatus(_A)
if mibBuilder.loadTexts:ntcEtherStatDataInputErrors.setUnits(_F)
_NtcEtherStatDataOutputerrors_Type=Counter64
_NtcEtherStatDataOutputerrors_Object=MibTableColumn
ntcEtherStatDataOutputerrors=_NtcEtherStatDataOutputerrors_Object((1,3,6,1,4,1,5835,5,2,500,1,4,1,9),_NtcEtherStatDataOutputerrors_Type())
ntcEtherStatDataOutputerrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherStatDataOutputerrors.setStatus(_A)
if mibBuilder.loadTexts:ntcEtherStatDataOutputerrors.setUnits(_F)
_NtcEtherInterfaceRedundancy_ObjectIdentity=ObjectIdentity
ntcEtherInterfaceRedundancy=_NtcEtherInterfaceRedundancy_ObjectIdentity((1,3,6,1,4,1,5835,5,2,500,1,5))
if mibBuilder.loadTexts:ntcEtherInterfaceRedundancy.setStatus(_A)
_NtcEtherIfRedMgmt_ObjectIdentity=ObjectIdentity
ntcEtherIfRedMgmt=_NtcEtherIfRedMgmt_ObjectIdentity((1,3,6,1,4,1,5835,5,2,500,1,5,1))
if mibBuilder.loadTexts:ntcEtherIfRedMgmt.setStatus(_A)
class _NtcEtherIfRedMgmtSwitchOrder_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_K,0),('mgmt1or2',1),('mgmt1before2',2),('mgmt2before1',3)))
_NtcEtherIfRedMgmtSwitchOrder_Type.__name__=_D
_NtcEtherIfRedMgmtSwitchOrder_Object=MibScalar
ntcEtherIfRedMgmtSwitchOrder=_NtcEtherIfRedMgmtSwitchOrder_Object((1,3,6,1,4,1,5835,5,2,500,1,5,1,1),_NtcEtherIfRedMgmtSwitchOrder_Type())
ntcEtherIfRedMgmtSwitchOrder.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcEtherIfRedMgmtSwitchOrder.setStatus(_A)
_NtcEtherIfRedMgmtSwitchCount_Type=Counter32
_NtcEtherIfRedMgmtSwitchCount_Object=MibScalar
ntcEtherIfRedMgmtSwitchCount=_NtcEtherIfRedMgmtSwitchCount_Object((1,3,6,1,4,1,5835,5,2,500,1,5,1,2),_NtcEtherIfRedMgmtSwitchCount_Type())
ntcEtherIfRedMgmtSwitchCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherIfRedMgmtSwitchCount.setStatus(_A)
class _NtcEtherIfRedMgmtActiveInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_K,0),(_U,1),(_V,2),('na',3)))
_NtcEtherIfRedMgmtActiveInterface_Type.__name__=_D
_NtcEtherIfRedMgmtActiveInterface_Object=MibScalar
ntcEtherIfRedMgmtActiveInterface=_NtcEtherIfRedMgmtActiveInterface_Object((1,3,6,1,4,1,5835,5,2,500,1,5,1,3),_NtcEtherIfRedMgmtActiveInterface_Type())
ntcEtherIfRedMgmtActiveInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherIfRedMgmtActiveInterface.setStatus(_A)
_NtcEtherIfRedData_ObjectIdentity=ObjectIdentity
ntcEtherIfRedData=_NtcEtherIfRedData_ObjectIdentity((1,3,6,1,4,1,5835,5,2,500,1,5,2))
if mibBuilder.loadTexts:ntcEtherIfRedData.setStatus(_A)
class _NtcEtherIfRedDataSwitchOrder_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_K,0),('data1or2',1),('data1before2',2),('data2before1',3),(_O,4),(_P,5)))
_NtcEtherIfRedDataSwitchOrder_Type.__name__=_D
_NtcEtherIfRedDataSwitchOrder_Object=MibScalar
ntcEtherIfRedDataSwitchOrder=_NtcEtherIfRedDataSwitchOrder_Object((1,3,6,1,4,1,5835,5,2,500,1,5,2,1),_NtcEtherIfRedDataSwitchOrder_Type())
ntcEtherIfRedDataSwitchOrder.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcEtherIfRedDataSwitchOrder.setStatus(_A)
_NtcEtherIfRedDataSwitchCount_Type=Counter32
_NtcEtherIfRedDataSwitchCount_Object=MibScalar
ntcEtherIfRedDataSwitchCount=_NtcEtherIfRedDataSwitchCount_Object((1,3,6,1,4,1,5835,5,2,500,1,5,2,2),_NtcEtherIfRedDataSwitchCount_Type())
ntcEtherIfRedDataSwitchCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherIfRedDataSwitchCount.setStatus(_A)
class _NtcEtherIfRedDataActiveInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_K,0),(_O,1),(_P,2),('na',3)))
_NtcEtherIfRedDataActiveInterface_Type.__name__=_D
_NtcEtherIfRedDataActiveInterface_Object=MibScalar
ntcEtherIfRedDataActiveInterface=_NtcEtherIfRedDataActiveInterface_Object((1,3,6,1,4,1,5835,5,2,500,1,5,2,3),_NtcEtherIfRedDataActiveInterface_Type())
ntcEtherIfRedDataActiveInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherIfRedDataActiveInterface.setStatus(_A)
class _NtcEtherIfRedDataGwUnreachImpact_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noImpact',0),('linkRedundancyTrigger',1)))
_NtcEtherIfRedDataGwUnreachImpact_Type.__name__=_D
_NtcEtherIfRedDataGwUnreachImpact_Object=MibScalar
ntcEtherIfRedDataGwUnreachImpact=_NtcEtherIfRedDataGwUnreachImpact_Object((1,3,6,1,4,1,5835,5,2,500,1,5,2,4),_NtcEtherIfRedDataGwUnreachImpact_Type())
ntcEtherIfRedDataGwUnreachImpact.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcEtherIfRedDataGwUnreachImpact.setStatus(_A)
_NtcEtherIfRedSat_ObjectIdentity=ObjectIdentity
ntcEtherIfRedSat=_NtcEtherIfRedSat_ObjectIdentity((1,3,6,1,4,1,5835,5,2,500,1,5,3))
if mibBuilder.loadTexts:ntcEtherIfRedSat.setStatus(_A)
class _NtcEtherIfRedSatSwitchOrder_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_K,0),('sat1or2',1),('sat1before2',2),('sat2before1',3),(_Q,4),(_R,5)))
_NtcEtherIfRedSatSwitchOrder_Type.__name__=_D
_NtcEtherIfRedSatSwitchOrder_Object=MibScalar
ntcEtherIfRedSatSwitchOrder=_NtcEtherIfRedSatSwitchOrder_Object((1,3,6,1,4,1,5835,5,2,500,1,5,3,1),_NtcEtherIfRedSatSwitchOrder_Type())
ntcEtherIfRedSatSwitchOrder.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcEtherIfRedSatSwitchOrder.setStatus(_A)
_NtcEtherIfRedSatSwitchCount_Type=Counter32
_NtcEtherIfRedSatSwitchCount_Object=MibScalar
ntcEtherIfRedSatSwitchCount=_NtcEtherIfRedSatSwitchCount_Object((1,3,6,1,4,1,5835,5,2,500,1,5,3,2),_NtcEtherIfRedSatSwitchCount_Type())
ntcEtherIfRedSatSwitchCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherIfRedSatSwitchCount.setStatus(_A)
class _NtcEtherIfRedSatActiveInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_K,0),(_Q,1),(_R,2),('na',3)))
_NtcEtherIfRedSatActiveInterface_Type.__name__=_D
_NtcEtherIfRedSatActiveInterface_Object=MibScalar
ntcEtherIfRedSatActiveInterface=_NtcEtherIfRedSatActiveInterface_Object((1,3,6,1,4,1,5835,5,2,500,1,5,3,3),_NtcEtherIfRedSatActiveInterface_Type())
ntcEtherIfRedSatActiveInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherIfRedSatActiveInterface.setStatus(_A)
_NtcEtherAlarm_ObjectIdentity=ObjectIdentity
ntcEtherAlarm=_NtcEtherAlarm_ObjectIdentity((1,3,6,1,4,1,5835,5,2,500,1,6))
if mibBuilder.loadTexts:ntcEtherAlarm.setStatus(_A)
_NtcEtherAlmMgmt1EthLinkFail_Type=NtcAlarmState
_NtcEtherAlmMgmt1EthLinkFail_Object=MibScalar
ntcEtherAlmMgmt1EthLinkFail=_NtcEtherAlmMgmt1EthLinkFail_Object((1,3,6,1,4,1,5835,5,2,500,1,6,1),_NtcEtherAlmMgmt1EthLinkFail_Type())
ntcEtherAlmMgmt1EthLinkFail.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherAlmMgmt1EthLinkFail.setStatus(_A)
_NtcEtherAlmMgmt1EthHalfDuplex_Type=NtcAlarmState
_NtcEtherAlmMgmt1EthHalfDuplex_Object=MibScalar
ntcEtherAlmMgmt1EthHalfDuplex=_NtcEtherAlmMgmt1EthHalfDuplex_Object((1,3,6,1,4,1,5835,5,2,500,1,6,2),_NtcEtherAlmMgmt1EthHalfDuplex_Type())
ntcEtherAlmMgmt1EthHalfDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherAlmMgmt1EthHalfDuplex.setStatus(_A)
_NtcEtherAlmMgmt2EthLinkFail_Type=NtcAlarmState
_NtcEtherAlmMgmt2EthLinkFail_Object=MibScalar
ntcEtherAlmMgmt2EthLinkFail=_NtcEtherAlmMgmt2EthLinkFail_Object((1,3,6,1,4,1,5835,5,2,500,1,6,3),_NtcEtherAlmMgmt2EthLinkFail_Type())
ntcEtherAlmMgmt2EthLinkFail.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherAlmMgmt2EthLinkFail.setStatus(_A)
_NtcEtherAlmMgmt2EthHalfDuplex_Type=NtcAlarmState
_NtcEtherAlmMgmt2EthHalfDuplex_Object=MibScalar
ntcEtherAlmMgmt2EthHalfDuplex=_NtcEtherAlmMgmt2EthHalfDuplex_Object((1,3,6,1,4,1,5835,5,2,500,1,6,4),_NtcEtherAlmMgmt2EthHalfDuplex_Type())
ntcEtherAlmMgmt2EthHalfDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherAlmMgmt2EthHalfDuplex.setStatus(_A)
_NtcEtherAlmData1EthLinkFail_Type=NtcAlarmState
_NtcEtherAlmData1EthLinkFail_Object=MibScalar
ntcEtherAlmData1EthLinkFail=_NtcEtherAlmData1EthLinkFail_Object((1,3,6,1,4,1,5835,5,2,500,1,6,5),_NtcEtherAlmData1EthLinkFail_Type())
ntcEtherAlmData1EthLinkFail.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherAlmData1EthLinkFail.setStatus(_A)
_NtcEtherAlmData1EthHalfDuplex_Type=NtcAlarmState
_NtcEtherAlmData1EthHalfDuplex_Object=MibScalar
ntcEtherAlmData1EthHalfDuplex=_NtcEtherAlmData1EthHalfDuplex_Object((1,3,6,1,4,1,5835,5,2,500,1,6,6),_NtcEtherAlmData1EthHalfDuplex_Type())
ntcEtherAlmData1EthHalfDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherAlmData1EthHalfDuplex.setStatus(_A)
_NtcEtherAlmData2EthLinkFail_Type=NtcAlarmState
_NtcEtherAlmData2EthLinkFail_Object=MibScalar
ntcEtherAlmData2EthLinkFail=_NtcEtherAlmData2EthLinkFail_Object((1,3,6,1,4,1,5835,5,2,500,1,6,7),_NtcEtherAlmData2EthLinkFail_Type())
ntcEtherAlmData2EthLinkFail.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherAlmData2EthLinkFail.setStatus(_A)
_NtcEtherAlmData2EthHalfDuplex_Type=NtcAlarmState
_NtcEtherAlmData2EthHalfDuplex_Object=MibScalar
ntcEtherAlmData2EthHalfDuplex=_NtcEtherAlmData2EthHalfDuplex_Object((1,3,6,1,4,1,5835,5,2,500,1,6,8),_NtcEtherAlmData2EthHalfDuplex_Type())
ntcEtherAlmData2EthHalfDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherAlmData2EthHalfDuplex.setStatus(_A)
_NtcEtherAlmMgmtFpEthLinkFail_Type=NtcAlarmState
_NtcEtherAlmMgmtFpEthLinkFail_Object=MibScalar
ntcEtherAlmMgmtFpEthLinkFail=_NtcEtherAlmMgmtFpEthLinkFail_Object((1,3,6,1,4,1,5835,5,2,500,1,6,9),_NtcEtherAlmMgmtFpEthLinkFail_Type())
ntcEtherAlmMgmtFpEthLinkFail.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherAlmMgmtFpEthLinkFail.setStatus(_A)
_NtcEtherAlmMgmtFpEthHalfDuplex_Type=NtcAlarmState
_NtcEtherAlmMgmtFpEthHalfDuplex_Object=MibScalar
ntcEtherAlmMgmtFpEthHalfDuplex=_NtcEtherAlmMgmtFpEthHalfDuplex_Object((1,3,6,1,4,1,5835,5,2,500,1,6,10),_NtcEtherAlmMgmtFpEthHalfDuplex_Type())
ntcEtherAlmMgmtFpEthHalfDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherAlmMgmtFpEthHalfDuplex.setStatus(_A)
_NtcEtherAlmMgmtEthInterfaceFail_Type=NtcAlarmState
_NtcEtherAlmMgmtEthInterfaceFail_Object=MibScalar
ntcEtherAlmMgmtEthInterfaceFail=_NtcEtherAlmMgmtEthInterfaceFail_Object((1,3,6,1,4,1,5835,5,2,500,1,6,11),_NtcEtherAlmMgmtEthInterfaceFail_Type())
ntcEtherAlmMgmtEthInterfaceFail.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherAlmMgmtEthInterfaceFail.setStatus(_A)
_NtcEtherAlmDataEthInterfaceFail_Type=NtcAlarmState
_NtcEtherAlmDataEthInterfaceFail_Object=MibScalar
ntcEtherAlmDataEthInterfaceFail=_NtcEtherAlmDataEthInterfaceFail_Object((1,3,6,1,4,1,5835,5,2,500,1,6,12),_NtcEtherAlmDataEthInterfaceFail_Type())
ntcEtherAlmDataEthInterfaceFail.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherAlmDataEthInterfaceFail.setStatus(_A)
_NtcEtherAlmSat1EthLinkFail_Type=NtcAlarmState
_NtcEtherAlmSat1EthLinkFail_Object=MibScalar
ntcEtherAlmSat1EthLinkFail=_NtcEtherAlmSat1EthLinkFail_Object((1,3,6,1,4,1,5835,5,2,500,1,6,13),_NtcEtherAlmSat1EthLinkFail_Type())
ntcEtherAlmSat1EthLinkFail.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherAlmSat1EthLinkFail.setStatus(_A)
_NtcEtherAlmSat1EthHalfDuplex_Type=NtcAlarmState
_NtcEtherAlmSat1EthHalfDuplex_Object=MibScalar
ntcEtherAlmSat1EthHalfDuplex=_NtcEtherAlmSat1EthHalfDuplex_Object((1,3,6,1,4,1,5835,5,2,500,1,6,14),_NtcEtherAlmSat1EthHalfDuplex_Type())
ntcEtherAlmSat1EthHalfDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherAlmSat1EthHalfDuplex.setStatus(_A)
_NtcEtherAlmSat2EthLinkFail_Type=NtcAlarmState
_NtcEtherAlmSat2EthLinkFail_Object=MibScalar
ntcEtherAlmSat2EthLinkFail=_NtcEtherAlmSat2EthLinkFail_Object((1,3,6,1,4,1,5835,5,2,500,1,6,15),_NtcEtherAlmSat2EthLinkFail_Type())
ntcEtherAlmSat2EthLinkFail.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherAlmSat2EthLinkFail.setStatus(_A)
_NtcEtherAlmSat2EthHalfDuplex_Type=NtcAlarmState
_NtcEtherAlmSat2EthHalfDuplex_Object=MibScalar
ntcEtherAlmSat2EthHalfDuplex=_NtcEtherAlmSat2EthHalfDuplex_Object((1,3,6,1,4,1,5835,5,2,500,1,6,16),_NtcEtherAlmSat2EthHalfDuplex_Type())
ntcEtherAlmSat2EthHalfDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherAlmSat2EthHalfDuplex.setStatus(_A)
_NtcEtherAlmSatEthInterfaceFail_Type=NtcAlarmState
_NtcEtherAlmSatEthInterfaceFail_Object=MibScalar
ntcEtherAlmSatEthInterfaceFail=_NtcEtherAlmSatEthInterfaceFail_Object((1,3,6,1,4,1,5835,5,2,500,1,6,17),_NtcEtherAlmSatEthInterfaceFail_Type())
ntcEtherAlmSatEthInterfaceFail.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherAlmSatEthInterfaceFail.setStatus(_A)
_NtcEtherAlmMgmtEthGenIfFail_Type=NtcAlarmState
_NtcEtherAlmMgmtEthGenIfFail_Object=MibScalar
ntcEtherAlmMgmtEthGenIfFail=_NtcEtherAlmMgmtEthGenIfFail_Object((1,3,6,1,4,1,5835,5,2,500,1,6,18),_NtcEtherAlmMgmtEthGenIfFail_Type())
ntcEtherAlmMgmtEthGenIfFail.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherAlmMgmtEthGenIfFail.setStatus(_A)
_NtcEtherAlmDataEthGenIfFail_Type=NtcAlarmState
_NtcEtherAlmDataEthGenIfFail_Object=MibScalar
ntcEtherAlmDataEthGenIfFail=_NtcEtherAlmDataEthGenIfFail_Object((1,3,6,1,4,1,5835,5,2,500,1,6,19),_NtcEtherAlmDataEthGenIfFail_Type())
ntcEtherAlmDataEthGenIfFail.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherAlmDataEthGenIfFail.setStatus(_A)
_NtcEtherAlmSatEthGenIfFail_Type=NtcAlarmState
_NtcEtherAlmSatEthGenIfFail_Object=MibScalar
ntcEtherAlmSatEthGenIfFail=_NtcEtherAlmSatEthGenIfFail_Object((1,3,6,1,4,1,5835,5,2,500,1,6,20),_NtcEtherAlmSatEthGenIfFail_Type())
ntcEtherAlmSatEthGenIfFail.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcEtherAlmSatEthGenIfFail.setStatus(_A)
class _NtcEtherDataIgmpVersion_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('v2',0),('v3',1)))
_NtcEtherDataIgmpVersion_Type.__name__=_D
_NtcEtherDataIgmpVersion_Object=MibScalar
ntcEtherDataIgmpVersion=_NtcEtherDataIgmpVersion_Object((1,3,6,1,4,1,5835,5,2,500,1,7),_NtcEtherDataIgmpVersion_Type())
ntcEtherDataIgmpVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcEtherDataIgmpVersion.setStatus(_A)
_NtcEtherConformance_ObjectIdentity=ObjectIdentity
ntcEtherConformance=_NtcEtherConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,500,2))
if mibBuilder.loadTexts:ntcEtherConformance.setStatus(_A)
_NtcEtherConfCompliance_ObjectIdentity=ObjectIdentity
ntcEtherConfCompliance=_NtcEtherConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,500,2,1))
if mibBuilder.loadTexts:ntcEtherConfCompliance.setStatus(_A)
_NtcEtherConfGroup_ObjectIdentity=ObjectIdentity
ntcEtherConfGroup=_NtcEtherConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,500,2,2))
if mibBuilder.loadTexts:ntcEtherConfGroup.setStatus(_A)
ntcEtherConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,500,2,2,1))
ntcEtherConfGrpV1Standard.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab)))
if mibBuilder.loadTexts:ntcEtherConfGrpV1Standard.setStatus(_A)
ntcEtherConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,500,2,1,1))
ntcEtherConfCompV1Standard.setObjects((_B,_Ac))
if mibBuilder.loadTexts:ntcEtherConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcEthernet':ntcEthernet,'ntcEtherObjects':ntcEtherObjects,'ntcEtherLinkMgmtTable':ntcEtherLinkMgmtTable,'ntcEtherLinkMgmtEntry':ntcEtherLinkMgmtEntry,_W:ntcEtherLinkMgmtInterface,_d:ntcEtherLinkMgmtEnable,_e:ntcEtherLinkMgmtMacAddress,_f:ntcEtherLinkMgmtAutoNegotiation,_g:ntcEtherLinkMgmtAdvertisedSpeeds,_h:ntcEtherLinkMgmtForcedSpeed,_i:ntcEtherLinkMgmtLinkState,_j:ntcEtherLinkMgmtMtu,'ntcEtherLinkDataTable':ntcEtherLinkDataTable,'ntcEtherLinkDataEntry':ntcEtherLinkDataEntry,_a:ntcEtherLinkDataInterface,_k:ntcEtherLinkDataEnable,_l:ntcEtherLinkDataMacAddress,_m:ntcEtherLinkDataAutoNegotiation,_n:ntcEtherLinkDataAdvertisedSpeeds,_o:ntcEtherLinkDataForcedSpeed,_p:ntcEtherLinkDataLinkState,_q:ntcEtherLinkDataMtu,'ntcEtherStatMgmtTable':ntcEtherStatMgmtTable,'ntcEtherStatMgmtEntry':ntcEtherStatMgmtEntry,_b:ntcEtherStatMgmtInterface,_r:ntcEtherStatMgmtInputBytes,_s:ntcEtherStatMgmtInputPackets,_t:ntcEtherStatMgmtInputDropped,_u:ntcEtherStatMgmtOutputBytes,_v:ntcEtherStatMgmtOutputPackets,_w:ntcEtherStatMgmtOutputDropped,_x:ntcEtherStatMgmtInputErrors,_y:ntcEtherStatMgmtOutputerrors,'ntcEtherStatDataTable':ntcEtherStatDataTable,'ntcEtherStatDataEntry':ntcEtherStatDataEntry,_c:ntcEtherStatDataInterface,_z:ntcEtherStatDataInputBytes,_A0:ntcEtherStatDataInputPackets,_A1:ntcEtherStatDataInputDropped,_A2:ntcEtherStatDataOutputBytes,_A3:ntcEtherStatDataOutputPackets,_A4:ntcEtherStatDataOutputDropped,_A5:ntcEtherStatDataInputErrors,_A6:ntcEtherStatDataOutputerrors,'ntcEtherInterfaceRedundancy':ntcEtherInterfaceRedundancy,'ntcEtherIfRedMgmt':ntcEtherIfRedMgmt,_A7:ntcEtherIfRedMgmtSwitchOrder,_A8:ntcEtherIfRedMgmtSwitchCount,_A9:ntcEtherIfRedMgmtActiveInterface,'ntcEtherIfRedData':ntcEtherIfRedData,_AA:ntcEtherIfRedDataSwitchOrder,_AB:ntcEtherIfRedDataSwitchCount,_AC:ntcEtherIfRedDataActiveInterface,_AD:ntcEtherIfRedDataGwUnreachImpact,'ntcEtherIfRedSat':ntcEtherIfRedSat,_AE:ntcEtherIfRedSatSwitchOrder,_AF:ntcEtherIfRedSatSwitchCount,_AG:ntcEtherIfRedSatActiveInterface,'ntcEtherAlarm':ntcEtherAlarm,_AH:ntcEtherAlmMgmt1EthLinkFail,_AI:ntcEtherAlmMgmt1EthHalfDuplex,_AJ:ntcEtherAlmMgmt2EthLinkFail,_AK:ntcEtherAlmMgmt2EthHalfDuplex,_AL:ntcEtherAlmData1EthLinkFail,_AM:ntcEtherAlmData1EthHalfDuplex,_AN:ntcEtherAlmData2EthLinkFail,_AO:ntcEtherAlmData2EthHalfDuplex,_AP:ntcEtherAlmMgmtFpEthLinkFail,_AQ:ntcEtherAlmMgmtFpEthHalfDuplex,_AR:ntcEtherAlmMgmtEthInterfaceFail,_AS:ntcEtherAlmDataEthInterfaceFail,_AT:ntcEtherAlmSat1EthLinkFail,_AU:ntcEtherAlmSat1EthHalfDuplex,_AV:ntcEtherAlmSat2EthLinkFail,_AW:ntcEtherAlmSat2EthHalfDuplex,_AX:ntcEtherAlmSatEthInterfaceFail,_AY:ntcEtherAlmMgmtEthGenIfFail,_AZ:ntcEtherAlmDataEthGenIfFail,_Aa:ntcEtherAlmSatEthGenIfFail,_Ab:ntcEtherDataIgmpVersion,'ntcEtherConformance':ntcEtherConformance,'ntcEtherConfCompliance':ntcEtherConfCompliance,'ntcEtherConfCompV1Standard':ntcEtherConfCompV1Standard,'ntcEtherConfGroup':ntcEtherConfGroup,_Ac:ntcEtherConfGrpV1Standard})