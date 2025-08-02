_A6='unifiApSystemVersion'
_A5='unifiApSystemUptime'
_A4='unifiApSystemUplink'
_A3='unifiApSystemModel'
_A2='unifiApSystemIsolated'
_A1='unifiApSystemIp'
_A0='unifiVapUsage'
_z='unifiVapUp'
_y='unifiVapTxPower'
_x='unifiVapTxRetries'
_w='unifiVapTxPackets'
_v='unifiVapTxErrors'
_u='unifiVapTxDropped'
_t='unifiVapTxBytes'
_s='unifiVapRxPackets'
_r='unifiVapRxFrags'
_q='unifiVapRxErrors'
_p='unifiVapRxDropped'
_o='unifiVapRxCrypts'
_n='unifiVapRxBytes'
_m='unifiVapRadio'
_l='unifiVapNumStations'
_k='unifiVapName'
_j='unifiVapEssId'
_i='unifiVapExtChannel'
_h='unifiVapChannel'
_g='unifiVapCcq'
_f='unifiVapBssId'
_e='unifiRadioOtherBss'
_d='unifiRadioCuSelfTx'
_c='unifiRadioCuSelfRx'
_b='unifiRadioCuTotal'
_a='unifiRadioTxPackets'
_Z='unifiRadioRxPackets'
_Y='unifiRadioRadio'
_X='unifiRadioName'
_W='unifiIfUp'
_V='unifiIfTxPackets'
_U='unifiIfTxError'
_T='unifiIfTxDropped'
_S='unifiIfTxBytes'
_R='unifiIfSpeed'
_Q='unifiIfRxPackets'
_P='unifiIfRxMulticast'
_O='unifiIfRxError'
_N='unifiIfRxDropped'
_M='unifiIfRxBytes'
_L='unifiIfName'
_K='unifiIfMac'
_J='unifiIfIp'
_I='unifiIfFullDuplex'
_H='unifiIfIndex'
_G='unifiVapIndex'
_F='unifiRadioIndex'
_E='ubntUniFi'
_D='not-accessible'
_C='read-only'
_B='UBNT-UniFi-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
ubntMIB,ubntUniFi,ubntUniFiGroups=mibBuilder.importSymbols('UBNT-MIB','ubntMIB',_E,'ubntUniFiGroups')
ubntUniFi=ModuleIdentity((1,3,6,1,4,1,41112,1,6))
if mibBuilder.loadTexts:ubntUniFi.setRevisions(('2016-06-25 00:00',))
class TableIndex(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class ObjectIndex(TextualConvention,Integer32):status=_A;displayHint='x';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class Voltage(TextualConvention,Integer32):status=_A;displayHint='d-2';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
class Temperature(TextualConvention,Integer32):status=_A;displayHint='d-1';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_UnifiApWireless_ObjectIdentity=ObjectIdentity
unifiApWireless=_UnifiApWireless_ObjectIdentity((1,3,6,1,4,1,41112,1,6,1))
_UnifiRadioTable_Object=MibTable
unifiRadioTable=_UnifiRadioTable_Object((1,3,6,1,4,1,41112,1,6,1,1))
if mibBuilder.loadTexts:unifiRadioTable.setStatus(_A)
_UnifiRadioEntry_Object=MibTableRow
unifiRadioEntry=_UnifiRadioEntry_Object((1,3,6,1,4,1,41112,1,6,1,1,1))
unifiRadioEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:unifiRadioEntry.setStatus(_A)
_UnifiRadioIndex_Type=ObjectIndex
_UnifiRadioIndex_Object=MibTableColumn
unifiRadioIndex=_UnifiRadioIndex_Object((1,3,6,1,4,1,41112,1,6,1,1,1,1),_UnifiRadioIndex_Type())
unifiRadioIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:unifiRadioIndex.setStatus(_A)
_UnifiRadioName_Type=DisplayString
_UnifiRadioName_Object=MibTableColumn
unifiRadioName=_UnifiRadioName_Object((1,3,6,1,4,1,41112,1,6,1,1,1,2),_UnifiRadioName_Type())
unifiRadioName.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiRadioName.setStatus(_A)
_UnifiRadioRadio_Type=DisplayString
_UnifiRadioRadio_Object=MibTableColumn
unifiRadioRadio=_UnifiRadioRadio_Object((1,3,6,1,4,1,41112,1,6,1,1,1,3),_UnifiRadioRadio_Type())
unifiRadioRadio.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiRadioRadio.setStatus(_A)
_UnifiRadioRxPackets_Type=Counter32
_UnifiRadioRxPackets_Object=MibTableColumn
unifiRadioRxPackets=_UnifiRadioRxPackets_Object((1,3,6,1,4,1,41112,1,6,1,1,1,4),_UnifiRadioRxPackets_Type())
unifiRadioRxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiRadioRxPackets.setStatus(_A)
_UnifiRadioTxPackets_Type=Counter32
_UnifiRadioTxPackets_Object=MibTableColumn
unifiRadioTxPackets=_UnifiRadioTxPackets_Object((1,3,6,1,4,1,41112,1,6,1,1,1,5),_UnifiRadioTxPackets_Type())
unifiRadioTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiRadioTxPackets.setStatus(_A)
_UnifiRadioCuTotal_Type=Integer32
_UnifiRadioCuTotal_Object=MibTableColumn
unifiRadioCuTotal=_UnifiRadioCuTotal_Object((1,3,6,1,4,1,41112,1,6,1,1,1,6),_UnifiRadioCuTotal_Type())
unifiRadioCuTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiRadioCuTotal.setStatus(_A)
_UnifiRadioCuSelfRx_Type=Integer32
_UnifiRadioCuSelfRx_Object=MibTableColumn
unifiRadioCuSelfRx=_UnifiRadioCuSelfRx_Object((1,3,6,1,4,1,41112,1,6,1,1,1,7),_UnifiRadioCuSelfRx_Type())
unifiRadioCuSelfRx.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiRadioCuSelfRx.setStatus(_A)
_UnifiRadioCuSelfTx_Type=Integer32
_UnifiRadioCuSelfTx_Object=MibTableColumn
unifiRadioCuSelfTx=_UnifiRadioCuSelfTx_Object((1,3,6,1,4,1,41112,1,6,1,1,1,8),_UnifiRadioCuSelfTx_Type())
unifiRadioCuSelfTx.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiRadioCuSelfTx.setStatus(_A)
_UnifiRadioOtherBss_Type=Integer32
_UnifiRadioOtherBss_Object=MibTableColumn
unifiRadioOtherBss=_UnifiRadioOtherBss_Object((1,3,6,1,4,1,41112,1,6,1,1,1,9),_UnifiRadioOtherBss_Type())
unifiRadioOtherBss.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiRadioOtherBss.setStatus(_A)
_UnifiVapTable_Object=MibTable
unifiVapTable=_UnifiVapTable_Object((1,3,6,1,4,1,41112,1,6,1,2))
if mibBuilder.loadTexts:unifiVapTable.setStatus(_A)
_UnifiVapEntry_Object=MibTableRow
unifiVapEntry=_UnifiVapEntry_Object((1,3,6,1,4,1,41112,1,6,1,2,1))
unifiVapEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:unifiVapEntry.setStatus(_A)
_UnifiVapIndex_Type=ObjectIndex
_UnifiVapIndex_Object=MibTableColumn
unifiVapIndex=_UnifiVapIndex_Object((1,3,6,1,4,1,41112,1,6,1,2,1,1),_UnifiVapIndex_Type())
unifiVapIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:unifiVapIndex.setStatus(_A)
_UnifiVapBssId_Type=MacAddress
_UnifiVapBssId_Object=MibTableColumn
unifiVapBssId=_UnifiVapBssId_Object((1,3,6,1,4,1,41112,1,6,1,2,1,2),_UnifiVapBssId_Type())
unifiVapBssId.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiVapBssId.setStatus(_A)
_UnifiVapCcq_Type=Integer32
_UnifiVapCcq_Object=MibTableColumn
unifiVapCcq=_UnifiVapCcq_Object((1,3,6,1,4,1,41112,1,6,1,2,1,3),_UnifiVapCcq_Type())
unifiVapCcq.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiVapCcq.setStatus(_A)
_UnifiVapChannel_Type=Integer32
_UnifiVapChannel_Object=MibTableColumn
unifiVapChannel=_UnifiVapChannel_Object((1,3,6,1,4,1,41112,1,6,1,2,1,4),_UnifiVapChannel_Type())
unifiVapChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiVapChannel.setStatus(_A)
_UnifiVapExtChannel_Type=Integer32
_UnifiVapExtChannel_Object=MibTableColumn
unifiVapExtChannel=_UnifiVapExtChannel_Object((1,3,6,1,4,1,41112,1,6,1,2,1,5),_UnifiVapExtChannel_Type())
unifiVapExtChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiVapExtChannel.setStatus(_A)
_UnifiVapEssId_Type=DisplayString
_UnifiVapEssId_Object=MibTableColumn
unifiVapEssId=_UnifiVapEssId_Object((1,3,6,1,4,1,41112,1,6,1,2,1,6),_UnifiVapEssId_Type())
unifiVapEssId.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiVapEssId.setStatus(_A)
_UnifiVapName_Type=DisplayString
_UnifiVapName_Object=MibTableColumn
unifiVapName=_UnifiVapName_Object((1,3,6,1,4,1,41112,1,6,1,2,1,7),_UnifiVapName_Type())
unifiVapName.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiVapName.setStatus(_A)
_UnifiVapNumStations_Type=Integer32
_UnifiVapNumStations_Object=MibTableColumn
unifiVapNumStations=_UnifiVapNumStations_Object((1,3,6,1,4,1,41112,1,6,1,2,1,8),_UnifiVapNumStations_Type())
unifiVapNumStations.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiVapNumStations.setStatus(_A)
_UnifiVapRadio_Type=DisplayString
_UnifiVapRadio_Object=MibTableColumn
unifiVapRadio=_UnifiVapRadio_Object((1,3,6,1,4,1,41112,1,6,1,2,1,9),_UnifiVapRadio_Type())
unifiVapRadio.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiVapRadio.setStatus(_A)
_UnifiVapRxBytes_Type=Counter32
_UnifiVapRxBytes_Object=MibTableColumn
unifiVapRxBytes=_UnifiVapRxBytes_Object((1,3,6,1,4,1,41112,1,6,1,2,1,10),_UnifiVapRxBytes_Type())
unifiVapRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiVapRxBytes.setStatus(_A)
_UnifiVapRxCrypts_Type=Counter32
_UnifiVapRxCrypts_Object=MibTableColumn
unifiVapRxCrypts=_UnifiVapRxCrypts_Object((1,3,6,1,4,1,41112,1,6,1,2,1,11),_UnifiVapRxCrypts_Type())
unifiVapRxCrypts.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiVapRxCrypts.setStatus(_A)
_UnifiVapRxDropped_Type=Counter32
_UnifiVapRxDropped_Object=MibTableColumn
unifiVapRxDropped=_UnifiVapRxDropped_Object((1,3,6,1,4,1,41112,1,6,1,2,1,12),_UnifiVapRxDropped_Type())
unifiVapRxDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiVapRxDropped.setStatus(_A)
_UnifiVapRxErrors_Type=Counter32
_UnifiVapRxErrors_Object=MibTableColumn
unifiVapRxErrors=_UnifiVapRxErrors_Object((1,3,6,1,4,1,41112,1,6,1,2,1,13),_UnifiVapRxErrors_Type())
unifiVapRxErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiVapRxErrors.setStatus(_A)
_UnifiVapRxFrags_Type=Counter32
_UnifiVapRxFrags_Object=MibTableColumn
unifiVapRxFrags=_UnifiVapRxFrags_Object((1,3,6,1,4,1,41112,1,6,1,2,1,14),_UnifiVapRxFrags_Type())
unifiVapRxFrags.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiVapRxFrags.setStatus(_A)
_UnifiVapRxPackets_Type=Counter32
_UnifiVapRxPackets_Object=MibTableColumn
unifiVapRxPackets=_UnifiVapRxPackets_Object((1,3,6,1,4,1,41112,1,6,1,2,1,15),_UnifiVapRxPackets_Type())
unifiVapRxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiVapRxPackets.setStatus(_A)
_UnifiVapTxBytes_Type=Counter32
_UnifiVapTxBytes_Object=MibTableColumn
unifiVapTxBytes=_UnifiVapTxBytes_Object((1,3,6,1,4,1,41112,1,6,1,2,1,16),_UnifiVapTxBytes_Type())
unifiVapTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiVapTxBytes.setStatus(_A)
_UnifiVapTxDropped_Type=Counter32
_UnifiVapTxDropped_Object=MibTableColumn
unifiVapTxDropped=_UnifiVapTxDropped_Object((1,3,6,1,4,1,41112,1,6,1,2,1,17),_UnifiVapTxDropped_Type())
unifiVapTxDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiVapTxDropped.setStatus(_A)
_UnifiVapTxErrors_Type=Counter32
_UnifiVapTxErrors_Object=MibTableColumn
unifiVapTxErrors=_UnifiVapTxErrors_Object((1,3,6,1,4,1,41112,1,6,1,2,1,18),_UnifiVapTxErrors_Type())
unifiVapTxErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiVapTxErrors.setStatus(_A)
_UnifiVapTxPackets_Type=Counter32
_UnifiVapTxPackets_Object=MibTableColumn
unifiVapTxPackets=_UnifiVapTxPackets_Object((1,3,6,1,4,1,41112,1,6,1,2,1,19),_UnifiVapTxPackets_Type())
unifiVapTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiVapTxPackets.setStatus(_A)
_UnifiVapTxRetries_Type=Counter32
_UnifiVapTxRetries_Object=MibTableColumn
unifiVapTxRetries=_UnifiVapTxRetries_Object((1,3,6,1,4,1,41112,1,6,1,2,1,20),_UnifiVapTxRetries_Type())
unifiVapTxRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiVapTxRetries.setStatus(_A)
_UnifiVapTxPower_Type=Integer32
_UnifiVapTxPower_Object=MibTableColumn
unifiVapTxPower=_UnifiVapTxPower_Object((1,3,6,1,4,1,41112,1,6,1,2,1,21),_UnifiVapTxPower_Type())
unifiVapTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiVapTxPower.setStatus(_A)
_UnifiVapUp_Type=TruthValue
_UnifiVapUp_Object=MibTableColumn
unifiVapUp=_UnifiVapUp_Object((1,3,6,1,4,1,41112,1,6,1,2,1,22),_UnifiVapUp_Type())
unifiVapUp.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiVapUp.setStatus(_A)
_UnifiVapUsage_Type=DisplayString
_UnifiVapUsage_Object=MibTableColumn
unifiVapUsage=_UnifiVapUsage_Object((1,3,6,1,4,1,41112,1,6,1,2,1,23),_UnifiVapUsage_Type())
unifiVapUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiVapUsage.setStatus(_A)
_UnifiApIf_ObjectIdentity=ObjectIdentity
unifiApIf=_UnifiApIf_ObjectIdentity((1,3,6,1,4,1,41112,1,6,2))
_UnifiIfTable_Object=MibTable
unifiIfTable=_UnifiIfTable_Object((1,3,6,1,4,1,41112,1,6,2,1))
if mibBuilder.loadTexts:unifiIfTable.setStatus(_A)
_UnifiIfEntry_Object=MibTableRow
unifiIfEntry=_UnifiIfEntry_Object((1,3,6,1,4,1,41112,1,6,2,1,1))
unifiIfEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:unifiIfEntry.setStatus(_A)
_UnifiIfIndex_Type=ObjectIndex
_UnifiIfIndex_Object=MibTableColumn
unifiIfIndex=_UnifiIfIndex_Object((1,3,6,1,4,1,41112,1,6,2,1,1,1),_UnifiIfIndex_Type())
unifiIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:unifiIfIndex.setStatus(_A)
_UnifiIfFullDuplex_Type=TruthValue
_UnifiIfFullDuplex_Object=MibTableColumn
unifiIfFullDuplex=_UnifiIfFullDuplex_Object((1,3,6,1,4,1,41112,1,6,2,1,1,2),_UnifiIfFullDuplex_Type())
unifiIfFullDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiIfFullDuplex.setStatus(_A)
_UnifiIfIp_Type=IpAddress
_UnifiIfIp_Object=MibTableColumn
unifiIfIp=_UnifiIfIp_Object((1,3,6,1,4,1,41112,1,6,2,1,1,3),_UnifiIfIp_Type())
unifiIfIp.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiIfIp.setStatus(_A)
_UnifiIfMac_Type=MacAddress
_UnifiIfMac_Object=MibTableColumn
unifiIfMac=_UnifiIfMac_Object((1,3,6,1,4,1,41112,1,6,2,1,1,4),_UnifiIfMac_Type())
unifiIfMac.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiIfMac.setStatus(_A)
_UnifiIfName_Type=DisplayString
_UnifiIfName_Object=MibTableColumn
unifiIfName=_UnifiIfName_Object((1,3,6,1,4,1,41112,1,6,2,1,1,5),_UnifiIfName_Type())
unifiIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiIfName.setStatus(_A)
_UnifiIfRxBytes_Type=Counter32
_UnifiIfRxBytes_Object=MibTableColumn
unifiIfRxBytes=_UnifiIfRxBytes_Object((1,3,6,1,4,1,41112,1,6,2,1,1,6),_UnifiIfRxBytes_Type())
unifiIfRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiIfRxBytes.setStatus(_A)
_UnifiIfRxDropped_Type=Counter32
_UnifiIfRxDropped_Object=MibTableColumn
unifiIfRxDropped=_UnifiIfRxDropped_Object((1,3,6,1,4,1,41112,1,6,2,1,1,7),_UnifiIfRxDropped_Type())
unifiIfRxDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiIfRxDropped.setStatus(_A)
_UnifiIfRxError_Type=Counter32
_UnifiIfRxError_Object=MibTableColumn
unifiIfRxError=_UnifiIfRxError_Object((1,3,6,1,4,1,41112,1,6,2,1,1,8),_UnifiIfRxError_Type())
unifiIfRxError.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiIfRxError.setStatus(_A)
_UnifiIfRxMulticast_Type=Counter32
_UnifiIfRxMulticast_Object=MibTableColumn
unifiIfRxMulticast=_UnifiIfRxMulticast_Object((1,3,6,1,4,1,41112,1,6,2,1,1,9),_UnifiIfRxMulticast_Type())
unifiIfRxMulticast.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiIfRxMulticast.setStatus(_A)
_UnifiIfRxPackets_Type=Counter32
_UnifiIfRxPackets_Object=MibTableColumn
unifiIfRxPackets=_UnifiIfRxPackets_Object((1,3,6,1,4,1,41112,1,6,2,1,1,10),_UnifiIfRxPackets_Type())
unifiIfRxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiIfRxPackets.setStatus(_A)
_UnifiIfSpeed_Type=Integer32
_UnifiIfSpeed_Object=MibTableColumn
unifiIfSpeed=_UnifiIfSpeed_Object((1,3,6,1,4,1,41112,1,6,2,1,1,11),_UnifiIfSpeed_Type())
unifiIfSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiIfSpeed.setStatus(_A)
_UnifiIfTxBytes_Type=Counter32
_UnifiIfTxBytes_Object=MibTableColumn
unifiIfTxBytes=_UnifiIfTxBytes_Object((1,3,6,1,4,1,41112,1,6,2,1,1,12),_UnifiIfTxBytes_Type())
unifiIfTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiIfTxBytes.setStatus(_A)
_UnifiIfTxDropped_Type=Counter32
_UnifiIfTxDropped_Object=MibTableColumn
unifiIfTxDropped=_UnifiIfTxDropped_Object((1,3,6,1,4,1,41112,1,6,2,1,1,13),_UnifiIfTxDropped_Type())
unifiIfTxDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiIfTxDropped.setStatus(_A)
_UnifiIfTxError_Type=Counter32
_UnifiIfTxError_Object=MibTableColumn
unifiIfTxError=_UnifiIfTxError_Object((1,3,6,1,4,1,41112,1,6,2,1,1,14),_UnifiIfTxError_Type())
unifiIfTxError.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiIfTxError.setStatus(_A)
_UnifiIfTxPackets_Type=Counter32
_UnifiIfTxPackets_Object=MibTableColumn
unifiIfTxPackets=_UnifiIfTxPackets_Object((1,3,6,1,4,1,41112,1,6,2,1,1,15),_UnifiIfTxPackets_Type())
unifiIfTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiIfTxPackets.setStatus(_A)
_UnifiIfUp_Type=TruthValue
_UnifiIfUp_Object=MibTableColumn
unifiIfUp=_UnifiIfUp_Object((1,3,6,1,4,1,41112,1,6,2,1,1,16),_UnifiIfUp_Type())
unifiIfUp.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiIfUp.setStatus(_A)
_UnifiApSystem_ObjectIdentity=ObjectIdentity
unifiApSystem=_UnifiApSystem_ObjectIdentity((1,3,6,1,4,1,41112,1,6,3))
_UnifiApSystemIp_Type=IpAddress
_UnifiApSystemIp_Object=MibScalar
unifiApSystemIp=_UnifiApSystemIp_Object((1,3,6,1,4,1,41112,1,6,3,1),_UnifiApSystemIp_Type())
unifiApSystemIp.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiApSystemIp.setStatus(_A)
_UnifiApSystemIsolated_Type=TruthValue
_UnifiApSystemIsolated_Object=MibScalar
unifiApSystemIsolated=_UnifiApSystemIsolated_Object((1,3,6,1,4,1,41112,1,6,3,2),_UnifiApSystemIsolated_Type())
unifiApSystemIsolated.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiApSystemIsolated.setStatus(_A)
_UnifiApSystemModel_Type=DisplayString
_UnifiApSystemModel_Object=MibScalar
unifiApSystemModel=_UnifiApSystemModel_Object((1,3,6,1,4,1,41112,1,6,3,3),_UnifiApSystemModel_Type())
unifiApSystemModel.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiApSystemModel.setStatus(_A)
_UnifiApSystemUplink_Type=DisplayString
_UnifiApSystemUplink_Object=MibScalar
unifiApSystemUplink=_UnifiApSystemUplink_Object((1,3,6,1,4,1,41112,1,6,3,4),_UnifiApSystemUplink_Type())
unifiApSystemUplink.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiApSystemUplink.setStatus(_A)
_UnifiApSystemUptime_Type=Counter32
_UnifiApSystemUptime_Object=MibScalar
unifiApSystemUptime=_UnifiApSystemUptime_Object((1,3,6,1,4,1,41112,1,6,3,5),_UnifiApSystemUptime_Type())
unifiApSystemUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiApSystemUptime.setStatus(_A)
_UnifiApSystemVersion_Type=DisplayString
_UnifiApSystemVersion_Object=MibScalar
unifiApSystemVersion=_UnifiApSystemVersion_Object((1,3,6,1,4,1,41112,1,6,3,6),_UnifiApSystemVersion_Type())
unifiApSystemVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:unifiApSystemVersion.setStatus(_A)
unifiIfGroup=ObjectGroup((1,3,6,1,4,1,41112,1,2,5,1))
unifiIfGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:unifiIfGroup.setStatus(_A)
unifiRadioGroups=ObjectGroup((1,3,6,1,4,1,41112,1,2,5,2))
unifiRadioGroups.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:unifiRadioGroups.setStatus(_A)
unifiVapGroups=ObjectGroup((1,3,6,1,4,1,41112,1,2,5,3))
unifiVapGroups.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:unifiVapGroups.setStatus(_A)
unifiApSystemGroup=ObjectGroup((1,3,6,1,4,1,41112,1,2,5,4))
unifiApSystemGroup.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:unifiApSystemGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TableIndex':TableIndex,'ObjectIndex':ObjectIndex,'Voltage':Voltage,'Temperature':Temperature,'unifiIfGroup':unifiIfGroup,'unifiRadioGroups':unifiRadioGroups,'unifiVapGroups':unifiVapGroups,'unifiApSystemGroup':unifiApSystemGroup,_E:ubntUniFi,'unifiApWireless':unifiApWireless,'unifiRadioTable':unifiRadioTable,'unifiRadioEntry':unifiRadioEntry,_F:unifiRadioIndex,_X:unifiRadioName,_Y:unifiRadioRadio,_Z:unifiRadioRxPackets,_a:unifiRadioTxPackets,_b:unifiRadioCuTotal,_c:unifiRadioCuSelfRx,_d:unifiRadioCuSelfTx,_e:unifiRadioOtherBss,'unifiVapTable':unifiVapTable,'unifiVapEntry':unifiVapEntry,_G:unifiVapIndex,_f:unifiVapBssId,_g:unifiVapCcq,_h:unifiVapChannel,_i:unifiVapExtChannel,_j:unifiVapEssId,_k:unifiVapName,_l:unifiVapNumStations,_m:unifiVapRadio,_n:unifiVapRxBytes,_o:unifiVapRxCrypts,_p:unifiVapRxDropped,_q:unifiVapRxErrors,_r:unifiVapRxFrags,_s:unifiVapRxPackets,_t:unifiVapTxBytes,_u:unifiVapTxDropped,_v:unifiVapTxErrors,_w:unifiVapTxPackets,_x:unifiVapTxRetries,_y:unifiVapTxPower,_z:unifiVapUp,_A0:unifiVapUsage,'unifiApIf':unifiApIf,'unifiIfTable':unifiIfTable,'unifiIfEntry':unifiIfEntry,_H:unifiIfIndex,_I:unifiIfFullDuplex,_J:unifiIfIp,_K:unifiIfMac,_L:unifiIfName,_M:unifiIfRxBytes,_N:unifiIfRxDropped,_O:unifiIfRxError,_P:unifiIfRxMulticast,_Q:unifiIfRxPackets,_R:unifiIfSpeed,_S:unifiIfTxBytes,_T:unifiIfTxDropped,_U:unifiIfTxError,_V:unifiIfTxPackets,_W:unifiIfUp,'unifiApSystem':unifiApSystem,_A1:unifiApSystemIp,_A2:unifiApSystemIsolated,_A3:unifiApSystemModel,_A4:unifiApSystemUplink,_A5:unifiApSystemUptime,_A6:unifiApSystemVersion})