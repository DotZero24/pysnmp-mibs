_z='wsFanVoltage'
_y='wsFanRPM'
_x='wsVoltThresholdHigh'
_w='wsVoltThresholdLow'
_v='wsTempThresholdHigh'
_u='wsTempThresholdLow'
_t='wsIfXEntry'
_s='wsXFPIndex'
_r='wsPolicyName'
_q='wsPolicyIfIndex'
_p='e8B10B'
_o='copperPigtail'
_n='hssdcii'
_m='opticalPigtail'
_l='fiberJack'
_k='invalid'
_j='missing'
_i='wsSFPIndex'
_h='wsNeighbourPortSNPASIndex'
_g='wsNeighbourPortSNPAPIndex'
_f='wsNeighbourPortSNPANIndex'
_e='wsNeighbourPortSNPAIfIndex'
_d='reserved2'
_c='reserved1'
_b='wsNeighbourPortPIndex'
_a='wsNeighbourPortNIndex'
_Z='wsNeighbourPortIfIndex'
_Y='wsNeighbourNIndex'
_X='wsNeighbourIfIndex'
_W='failed'
_V='wsVoltStatus'
_U='wsVoltMeasured'
_T='wsTempStatus'
_S='wsTempMeasured'
_R='reserved0'
_Q='wsFanNumber'
_P='disabled'
_O='read-write'
_N='DisplayString'
_M='wsVoltChannel'
_L='wsTempSensor'
_K='Bits'
_J='alarmHigh'
_I='warnHigh'
_H='warnLow'
_G='alarmLow'
_F='unknown'
_E='ok'
_D='Integer32'
_C='WAYSTREAM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifEntry,=mibBuilder.importSymbols('IF-MIB','ifEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_K,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_N,'PhysAddress','TextualConvention')
wsExperiment,wsMgmt=mibBuilder.importSymbols('WAYSTREAM-SMI','wsExperiment','wsMgmt')
ibos=ModuleIdentity((1,3,6,1,4,1,9303,4,1))
if mibBuilder.loadTexts:ibos.setRevisions(('2017-10-23 11:00','2017-09-18 11:00','2017-02-10 11:00','2012-07-05 19:30','2011-12-20 09:08','2011-12-06 09:34','2011-01-11 17:55','2009-04-17 15:29','2009-03-23 11:02','2008-04-30 14:26','2007-10-03 18:35','2007-06-13 14:37','2006-10-18 13:41','2006-08-23 11:00','2006-01-25 13:30','2005-05-10 11:24','2005-02-01 09:11','2005-01-14 15:00','2004-10-20 14:34','2004-05-14 11:55'))
_WsSystem_ObjectIdentity=ObjectIdentity
wsSystem=_WsSystem_ObjectIdentity((1,3,6,1,4,1,9303,4,1,1))
if mibBuilder.loadTexts:wsSystem.setStatus(_A)
class _WsWritedummy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WsWritedummy_Type.__name__=_D
_WsWritedummy_Object=MibScalar
wsWritedummy=_WsWritedummy_Object((1,3,6,1,4,1,9303,4,1,1,1),_WsWritedummy_Type())
wsWritedummy.setMaxAccess(_O)
if mibBuilder.loadTexts:wsWritedummy.setStatus(_A)
class _WsReload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WsReload_Type.__name__=_D
_WsReload_Object=MibScalar
wsReload=_WsReload_Object((1,3,6,1,4,1,9303,4,1,1,2),_WsReload_Type())
wsReload.setMaxAccess(_O)
if mibBuilder.loadTexts:wsReload.setStatus(_A)
class _WsVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WsVersion_Type.__name__=_D
_WsVersion_Object=MibScalar
wsVersion=_WsVersion_Object((1,3,6,1,4,1,9303,4,1,1,3),_WsVersion_Type())
wsVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:wsVersion.setStatus(_A)
class _WsAsrRevision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WsAsrRevision_Type.__name__=_D
_WsAsrRevision_Object=MibScalar
wsAsrRevision=_WsAsrRevision_Object((1,3,6,1,4,1,9303,4,1,1,4),_WsAsrRevision_Type())
wsAsrRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:wsAsrRevision.setStatus(_A)
_WsVersionString_Type=DisplayString
_WsVersionString_Object=MibScalar
wsVersionString=_WsVersionString_Object((1,3,6,1,4,1,9303,4,1,1,5),_WsVersionString_Type())
wsVersionString.setMaxAccess(_B)
if mibBuilder.loadTexts:wsVersionString.setStatus(_A)
_WsEnvironment_ObjectIdentity=ObjectIdentity
wsEnvironment=_WsEnvironment_ObjectIdentity((1,3,6,1,4,1,9303,4,1,2))
if mibBuilder.loadTexts:wsEnvironment.setStatus(_A)
_WsIbosEnvironmentNotifications_ObjectIdentity=ObjectIdentity
wsIbosEnvironmentNotifications=_WsIbosEnvironmentNotifications_ObjectIdentity((1,3,6,1,4,1,9303,4,1,2,0))
_WsTempTable_Object=MibTable
wsTempTable=_WsTempTable_Object((1,3,6,1,4,1,9303,4,1,2,1))
if mibBuilder.loadTexts:wsTempTable.setStatus(_A)
_WsTempEntry_Object=MibTableRow
wsTempEntry=_WsTempEntry_Object((1,3,6,1,4,1,9303,4,1,2,1,1))
wsTempEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:wsTempEntry.setStatus(_A)
_WsTempSensor_Type=Unsigned32
_WsTempSensor_Object=MibTableColumn
wsTempSensor=_WsTempSensor_Object((1,3,6,1,4,1,9303,4,1,2,1,1,1),_WsTempSensor_Type())
wsTempSensor.setMaxAccess(_B)
if mibBuilder.loadTexts:wsTempSensor.setStatus(_A)
_WsTempMeasured_Type=Integer32
_WsTempMeasured_Object=MibTableColumn
wsTempMeasured=_WsTempMeasured_Object((1,3,6,1,4,1,9303,4,1,2,1,1,2),_WsTempMeasured_Type())
wsTempMeasured.setMaxAccess(_B)
if mibBuilder.loadTexts:wsTempMeasured.setStatus(_A)
_WsTempTOS_Type=Integer32
_WsTempTOS_Object=MibTableColumn
wsTempTOS=_WsTempTOS_Object((1,3,6,1,4,1,9303,4,1,2,1,1,3),_WsTempTOS_Type())
wsTempTOS.setMaxAccess(_B)
if mibBuilder.loadTexts:wsTempTOS.setStatus(_A)
_WsTempTHYST_Type=Integer32
_WsTempTHYST_Object=MibTableColumn
wsTempTHYST=_WsTempTHYST_Object((1,3,6,1,4,1,9303,4,1,2,1,1,4),_WsTempTHYST_Type())
wsTempTHYST.setMaxAccess(_B)
if mibBuilder.loadTexts:wsTempTHYST.setStatus(_A)
_WsTempThresholdLow_Type=Integer32
_WsTempThresholdLow_Object=MibTableColumn
wsTempThresholdLow=_WsTempThresholdLow_Object((1,3,6,1,4,1,9303,4,1,2,1,1,5),_WsTempThresholdLow_Type())
wsTempThresholdLow.setMaxAccess(_B)
if mibBuilder.loadTexts:wsTempThresholdLow.setStatus(_A)
_WsTempThresholdHigh_Type=Integer32
_WsTempThresholdHigh_Object=MibTableColumn
wsTempThresholdHigh=_WsTempThresholdHigh_Object((1,3,6,1,4,1,9303,4,1,2,1,1,6),_WsTempThresholdHigh_Type())
wsTempThresholdHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:wsTempThresholdHigh.setStatus(_A)
class _WsTempStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2,4)));namedValues=NamedValues(*((_W,-1),(_E,0),('high',1),('low',2),(_P,4)))
_WsTempStatus_Type.__name__=_D
_WsTempStatus_Object=MibTableColumn
wsTempStatus=_WsTempStatus_Object((1,3,6,1,4,1,9303,4,1,2,1,1,7),_WsTempStatus_Type())
wsTempStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wsTempStatus.setStatus(_A)
_WsVoltTable_Object=MibTable
wsVoltTable=_WsVoltTable_Object((1,3,6,1,4,1,9303,4,1,2,2))
if mibBuilder.loadTexts:wsVoltTable.setStatus(_A)
_WsVoltEntry_Object=MibTableRow
wsVoltEntry=_WsVoltEntry_Object((1,3,6,1,4,1,9303,4,1,2,2,1))
wsVoltEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:wsVoltEntry.setStatus(_A)
_WsVoltChannel_Type=Unsigned32
_WsVoltChannel_Object=MibTableColumn
wsVoltChannel=_WsVoltChannel_Object((1,3,6,1,4,1,9303,4,1,2,2,1,1),_WsVoltChannel_Type())
wsVoltChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:wsVoltChannel.setStatus(_A)
_WsVoltNominal_Type=Integer32
_WsVoltNominal_Object=MibTableColumn
wsVoltNominal=_WsVoltNominal_Object((1,3,6,1,4,1,9303,4,1,2,2,1,2),_WsVoltNominal_Type())
wsVoltNominal.setMaxAccess(_B)
if mibBuilder.loadTexts:wsVoltNominal.setStatus(_A)
_WsVoltMeasured_Type=Integer32
_WsVoltMeasured_Object=MibTableColumn
wsVoltMeasured=_WsVoltMeasured_Object((1,3,6,1,4,1,9303,4,1,2,2,1,3),_WsVoltMeasured_Type())
wsVoltMeasured.setMaxAccess(_B)
if mibBuilder.loadTexts:wsVoltMeasured.setStatus(_A)
_WsVoltThresholdLow_Type=Integer32
_WsVoltThresholdLow_Object=MibTableColumn
wsVoltThresholdLow=_WsVoltThresholdLow_Object((1,3,6,1,4,1,9303,4,1,2,2,1,4),_WsVoltThresholdLow_Type())
wsVoltThresholdLow.setMaxAccess(_B)
if mibBuilder.loadTexts:wsVoltThresholdLow.setStatus(_A)
_WsVoltThresholdHigh_Type=Integer32
_WsVoltThresholdHigh_Object=MibTableColumn
wsVoltThresholdHigh=_WsVoltThresholdHigh_Object((1,3,6,1,4,1,9303,4,1,2,2,1,5),_WsVoltThresholdHigh_Type())
wsVoltThresholdHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:wsVoltThresholdHigh.setStatus(_A)
class _WsVoltStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-3,-1,0,1,2,3,4)));namedValues=NamedValues(*(('na',-3),(_W,-1),(_E,0),('high',1),('low',2),('notPresent',3),(_P,4)))
_WsVoltStatus_Type.__name__=_D
_WsVoltStatus_Object=MibTableColumn
wsVoltStatus=_WsVoltStatus_Object((1,3,6,1,4,1,9303,4,1,2,2,1,6),_WsVoltStatus_Type())
wsVoltStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wsVoltStatus.setStatus(_A)
_WsFanTable_Object=MibTable
wsFanTable=_WsFanTable_Object((1,3,6,1,4,1,9303,4,1,2,3))
if mibBuilder.loadTexts:wsFanTable.setStatus(_A)
_WsFanEntry_Object=MibTableRow
wsFanEntry=_WsFanEntry_Object((1,3,6,1,4,1,9303,4,1,2,3,1))
wsFanEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:wsFanEntry.setStatus(_A)
_WsFanNumber_Type=Unsigned32
_WsFanNumber_Object=MibTableColumn
wsFanNumber=_WsFanNumber_Object((1,3,6,1,4,1,9303,4,1,2,3,1,1),_WsFanNumber_Type())
wsFanNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wsFanNumber.setStatus(_A)
_WsFanRPM_Type=Integer32
_WsFanRPM_Object=MibTableColumn
wsFanRPM=_WsFanRPM_Object((1,3,6,1,4,1,9303,4,1,2,3,1,2),_WsFanRPM_Type())
wsFanRPM.setMaxAccess(_B)
if mibBuilder.loadTexts:wsFanRPM.setStatus(_A)
_WsFanVoltage_Type=Integer32
_WsFanVoltage_Object=MibScalar
wsFanVoltage=_WsFanVoltage_Object((1,3,6,1,4,1,9303,4,1,2,4),_WsFanVoltage_Type())
wsFanVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:wsFanVoltage.setStatus(_A)
class _WsIbosEnvironmentTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_P,2)))
_WsIbosEnvironmentTrapEnable_Type.__name__=_D
_WsIbosEnvironmentTrapEnable_Object=MibScalar
wsIbosEnvironmentTrapEnable=_WsIbosEnvironmentTrapEnable_Object((1,3,6,1,4,1,9303,4,1,2,5),_WsIbosEnvironmentTrapEnable_Type())
wsIbosEnvironmentTrapEnable.setMaxAccess(_O)
if mibBuilder.loadTexts:wsIbosEnvironmentTrapEnable.setStatus(_A)
_WsPFDP_ObjectIdentity=ObjectIdentity
wsPFDP=_WsPFDP_ObjectIdentity((1,3,6,1,4,1,9303,4,1,3))
if mibBuilder.loadTexts:wsPFDP.setStatus(_A)
_WsNeighboursTable_Object=MibTable
wsNeighboursTable=_WsNeighboursTable_Object((1,3,6,1,4,1,9303,4,1,3,1))
if mibBuilder.loadTexts:wsNeighboursTable.setStatus(_A)
_WsNeighboursEntry_Object=MibTableRow
wsNeighboursEntry=_WsNeighboursEntry_Object((1,3,6,1,4,1,9303,4,1,3,1,1))
wsNeighboursEntry.setIndexNames((0,_C,_X),(0,_C,_Y))
if mibBuilder.loadTexts:wsNeighboursEntry.setStatus(_A)
_WsNeighbourIfIndex_Type=Unsigned32
_WsNeighbourIfIndex_Object=MibTableColumn
wsNeighbourIfIndex=_WsNeighbourIfIndex_Object((1,3,6,1,4,1,9303,4,1,3,1,1,1),_WsNeighbourIfIndex_Type())
wsNeighbourIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourIfIndex.setStatus(_A)
_WsNeighbourNIndex_Type=Unsigned32
_WsNeighbourNIndex_Object=MibTableColumn
wsNeighbourNIndex=_WsNeighbourNIndex_Object((1,3,6,1,4,1,9303,4,1,3,1,1,2),_WsNeighbourNIndex_Type())
wsNeighbourNIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourNIndex.setStatus(_A)
_WsNeighbourHostname_Type=DisplayString
_WsNeighbourHostname_Object=MibTableColumn
wsNeighbourHostname=_WsNeighbourHostname_Object((1,3,6,1,4,1,9303,4,1,3,1,1,3),_WsNeighbourHostname_Type())
wsNeighbourHostname.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourHostname.setStatus(_A)
_WsNeighbourLocalIf_Type=DisplayString
_WsNeighbourLocalIf_Object=MibTableColumn
wsNeighbourLocalIf=_WsNeighbourLocalIf_Object((1,3,6,1,4,1,9303,4,1,3,1,1,4),_WsNeighbourLocalIf_Type())
wsNeighbourLocalIf.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourLocalIf.setStatus(_A)
_WsNeighbourRemoteIf_Type=DisplayString
_WsNeighbourRemoteIf_Object=MibTableColumn
wsNeighbourRemoteIf=_WsNeighbourRemoteIf_Object((1,3,6,1,4,1,9303,4,1,3,1,1,5),_WsNeighbourRemoteIf_Type())
wsNeighbourRemoteIf.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourRemoteIf.setStatus(_A)
_WsNeighbourModel_Type=DisplayString
_WsNeighbourModel_Object=MibTableColumn
wsNeighbourModel=_WsNeighbourModel_Object((1,3,6,1,4,1,9303,4,1,3,1,1,6),_WsNeighbourModel_Type())
wsNeighbourModel.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourModel.setStatus(_A)
_WsNeighbourLastAct_Type=Integer32
_WsNeighbourLastAct_Object=MibTableColumn
wsNeighbourLastAct=_WsNeighbourLastAct_Object((1,3,6,1,4,1,9303,4,1,3,1,1,7),_WsNeighbourLastAct_Type())
wsNeighbourLastAct.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourLastAct.setStatus(_A)
_WsNeighbourOSVersion_Type=DisplayString
_WsNeighbourOSVersion_Object=MibTableColumn
wsNeighbourOSVersion=_WsNeighbourOSVersion_Object((1,3,6,1,4,1,9303,4,1,3,1,1,8),_WsNeighbourOSVersion_Type())
wsNeighbourOSVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourOSVersion.setStatus(_A)
_WsNeighbourSNPA_Type=OctetString
_WsNeighbourSNPA_Object=MibTableColumn
wsNeighbourSNPA=_WsNeighbourSNPA_Object((1,3,6,1,4,1,9303,4,1,3,1,1,9),_WsNeighbourSNPA_Type())
wsNeighbourSNPA.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourSNPA.setStatus(_A)
_WsNeighbourUptime_Type=Unsigned32
_WsNeighbourUptime_Object=MibTableColumn
wsNeighbourUptime=_WsNeighbourUptime_Object((1,3,6,1,4,1,9303,4,1,3,1,1,10),_WsNeighbourUptime_Type())
wsNeighbourUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourUptime.setStatus(_A)
class _WsNeighbourState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bidirectional',1),('unidirectional',2)))
_WsNeighbourState_Type.__name__=_D
_WsNeighbourState_Object=MibTableColumn
wsNeighbourState=_WsNeighbourState_Object((1,3,6,1,4,1,9303,4,1,3,1,1,11),_WsNeighbourState_Type())
wsNeighbourState.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourState.setStatus(_A)
_WsNeighbourDBCount_Type=Unsigned32
_WsNeighbourDBCount_Object=MibTableColumn
wsNeighbourDBCount=_WsNeighbourDBCount_Object((1,3,6,1,4,1,9303,4,1,3,1,1,12),_WsNeighbourDBCount_Type())
wsNeighbourDBCount.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourDBCount.setStatus(_A)
_WsNeighbourCreated_Type=TimeTicks
_WsNeighbourCreated_Object=MibTableColumn
wsNeighbourCreated=_WsNeighbourCreated_Object((1,3,6,1,4,1,9303,4,1,3,1,1,13),_WsNeighbourCreated_Type())
wsNeighbourCreated.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourCreated.setStatus(_A)
_WsNeighbourPacketsIn_Type=Unsigned32
_WsNeighbourPacketsIn_Object=MibTableColumn
wsNeighbourPacketsIn=_WsNeighbourPacketsIn_Object((1,3,6,1,4,1,9303,4,1,3,1,1,14),_WsNeighbourPacketsIn_Type())
wsNeighbourPacketsIn.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPacketsIn.setStatus(_A)
_WsNeighbourPacketErrorsrIn_Type=Unsigned32
_WsNeighbourPacketErrorsrIn_Object=MibTableColumn
wsNeighbourPacketErrorsrIn=_WsNeighbourPacketErrorsrIn_Object((1,3,6,1,4,1,9303,4,1,3,1,1,15),_WsNeighbourPacketErrorsrIn_Type())
wsNeighbourPacketErrorsrIn.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPacketErrorsrIn.setStatus(_A)
_WsNeighbourPortsTable_Object=MibTable
wsNeighbourPortsTable=_WsNeighbourPortsTable_Object((1,3,6,1,4,1,9303,4,1,3,2))
if mibBuilder.loadTexts:wsNeighbourPortsTable.setStatus(_A)
_WsNeighbourPortsEntry_Object=MibTableRow
wsNeighbourPortsEntry=_WsNeighbourPortsEntry_Object((1,3,6,1,4,1,9303,4,1,3,2,1))
wsNeighbourPortsEntry.setIndexNames((0,_C,_Z),(0,_C,_a),(0,_C,_b))
if mibBuilder.loadTexts:wsNeighbourPortsEntry.setStatus(_A)
_WsNeighbourPortIfIndex_Type=Unsigned32
_WsNeighbourPortIfIndex_Object=MibTableColumn
wsNeighbourPortIfIndex=_WsNeighbourPortIfIndex_Object((1,3,6,1,4,1,9303,4,1,3,2,1,1),_WsNeighbourPortIfIndex_Type())
wsNeighbourPortIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortIfIndex.setStatus(_A)
_WsNeighbourPortNIndex_Type=Unsigned32
_WsNeighbourPortNIndex_Object=MibTableColumn
wsNeighbourPortNIndex=_WsNeighbourPortNIndex_Object((1,3,6,1,4,1,9303,4,1,3,2,1,2),_WsNeighbourPortNIndex_Type())
wsNeighbourPortNIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortNIndex.setStatus(_A)
_WsNeighbourPortPIndex_Type=Unsigned32
_WsNeighbourPortPIndex_Object=MibTableColumn
wsNeighbourPortPIndex=_WsNeighbourPortPIndex_Object((1,3,6,1,4,1,9303,4,1,3,2,1,3),_WsNeighbourPortPIndex_Type())
wsNeighbourPortPIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortPIndex.setStatus(_A)
_WsNeighbourPortName_Type=DisplayString
_WsNeighbourPortName_Object=MibTableColumn
wsNeighbourPortName=_WsNeighbourPortName_Object((1,3,6,1,4,1,9303,4,1,3,2,1,4),_WsNeighbourPortName_Type())
wsNeighbourPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortName.setStatus(_A)
class _WsNeighbourPortState_Type(Bits):namedValues=NamedValues(*((_R,0),(_c,1),(_d,2),('reserved3',3),('vlaninfo',4),('s100mbit',5),('fullduplex',6),('up',7)))
_WsNeighbourPortState_Type.__name__=_K
_WsNeighbourPortState_Object=MibTableColumn
wsNeighbourPortState=_WsNeighbourPortState_Object((1,3,6,1,4,1,9303,4,1,3,2,1,5),_WsNeighbourPortState_Type())
wsNeighbourPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortState.setStatus(_A)
_WsNeighbourPortTxOctets_Type=Counter64
_WsNeighbourPortTxOctets_Object=MibTableColumn
wsNeighbourPortTxOctets=_WsNeighbourPortTxOctets_Object((1,3,6,1,4,1,9303,4,1,3,2,1,6),_WsNeighbourPortTxOctets_Type())
wsNeighbourPortTxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortTxOctets.setStatus(_A)
_WsNeighbourPortTxDropPkts_Type=Unsigned32
_WsNeighbourPortTxDropPkts_Object=MibTableColumn
wsNeighbourPortTxDropPkts=_WsNeighbourPortTxDropPkts_Object((1,3,6,1,4,1,9303,4,1,3,2,1,7),_WsNeighbourPortTxDropPkts_Type())
wsNeighbourPortTxDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortTxDropPkts.setStatus(_A)
_WsNeighbourPortTxBroadcastPkts_Type=Unsigned32
_WsNeighbourPortTxBroadcastPkts_Object=MibTableColumn
wsNeighbourPortTxBroadcastPkts=_WsNeighbourPortTxBroadcastPkts_Object((1,3,6,1,4,1,9303,4,1,3,2,1,8),_WsNeighbourPortTxBroadcastPkts_Type())
wsNeighbourPortTxBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortTxBroadcastPkts.setStatus(_A)
_WsNeighbourPortTxMulticastPkts_Type=Unsigned32
_WsNeighbourPortTxMulticastPkts_Object=MibTableColumn
wsNeighbourPortTxMulticastPkts=_WsNeighbourPortTxMulticastPkts_Object((1,3,6,1,4,1,9303,4,1,3,2,1,9),_WsNeighbourPortTxMulticastPkts_Type())
wsNeighbourPortTxMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortTxMulticastPkts.setStatus(_A)
_WsNeighbourPortTxUnicastPkts_Type=Unsigned32
_WsNeighbourPortTxUnicastPkts_Object=MibTableColumn
wsNeighbourPortTxUnicastPkts=_WsNeighbourPortTxUnicastPkts_Object((1,3,6,1,4,1,9303,4,1,3,2,1,10),_WsNeighbourPortTxUnicastPkts_Type())
wsNeighbourPortTxUnicastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortTxUnicastPkts.setStatus(_A)
_WsNeighbourPortTxCollisions_Type=Unsigned32
_WsNeighbourPortTxCollisions_Object=MibTableColumn
wsNeighbourPortTxCollisions=_WsNeighbourPortTxCollisions_Object((1,3,6,1,4,1,9303,4,1,3,2,1,11),_WsNeighbourPortTxCollisions_Type())
wsNeighbourPortTxCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortTxCollisions.setStatus(_A)
_WsNeighbourPortTxDeferredTransmit_Type=Unsigned32
_WsNeighbourPortTxDeferredTransmit_Object=MibTableColumn
wsNeighbourPortTxDeferredTransmit=_WsNeighbourPortTxDeferredTransmit_Object((1,3,6,1,4,1,9303,4,1,3,2,1,12),_WsNeighbourPortTxDeferredTransmit_Type())
wsNeighbourPortTxDeferredTransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortTxDeferredTransmit.setStatus(_A)
_WsNeighbourPortTxFrameInDisc_Type=Unsigned32
_WsNeighbourPortTxFrameInDisc_Object=MibTableColumn
wsNeighbourPortTxFrameInDisc=_WsNeighbourPortTxFrameInDisc_Object((1,3,6,1,4,1,9303,4,1,3,2,1,13),_WsNeighbourPortTxFrameInDisc_Type())
wsNeighbourPortTxFrameInDisc.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortTxFrameInDisc.setStatus(_A)
_WsNeighbourPortRxOctets_Type=Counter64
_WsNeighbourPortRxOctets_Object=MibTableColumn
wsNeighbourPortRxOctets=_WsNeighbourPortRxOctets_Object((1,3,6,1,4,1,9303,4,1,3,2,1,14),_WsNeighbourPortRxOctets_Type())
wsNeighbourPortRxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortRxOctets.setStatus(_A)
_WsNeighbourPortRxUndersizePkts_Type=Unsigned32
_WsNeighbourPortRxUndersizePkts_Object=MibTableColumn
wsNeighbourPortRxUndersizePkts=_WsNeighbourPortRxUndersizePkts_Object((1,3,6,1,4,1,9303,4,1,3,2,1,15),_WsNeighbourPortRxUndersizePkts_Type())
wsNeighbourPortRxUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortRxUndersizePkts.setStatus(_A)
_WsNeighbourPortPkts64Octets_Type=Unsigned32
_WsNeighbourPortPkts64Octets_Object=MibTableColumn
wsNeighbourPortPkts64Octets=_WsNeighbourPortPkts64Octets_Object((1,3,6,1,4,1,9303,4,1,3,2,1,16),_WsNeighbourPortPkts64Octets_Type())
wsNeighbourPortPkts64Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortPkts64Octets.setStatus(_A)
_WsNeighbourPortPkts65to127Octets_Type=Unsigned32
_WsNeighbourPortPkts65to127Octets_Object=MibTableColumn
wsNeighbourPortPkts65to127Octets=_WsNeighbourPortPkts65to127Octets_Object((1,3,6,1,4,1,9303,4,1,3,2,1,17),_WsNeighbourPortPkts65to127Octets_Type())
wsNeighbourPortPkts65to127Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortPkts65to127Octets.setStatus(_A)
_WsNeighbourPortPkts128to255Octets_Type=Unsigned32
_WsNeighbourPortPkts128to255Octets_Object=MibTableColumn
wsNeighbourPortPkts128to255Octets=_WsNeighbourPortPkts128to255Octets_Object((1,3,6,1,4,1,9303,4,1,3,2,1,18),_WsNeighbourPortPkts128to255Octets_Type())
wsNeighbourPortPkts128to255Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortPkts128to255Octets.setStatus(_A)
_WsNeighbourPortPkts256to511Octets_Type=Unsigned32
_WsNeighbourPortPkts256to511Octets_Object=MibTableColumn
wsNeighbourPortPkts256to511Octets=_WsNeighbourPortPkts256to511Octets_Object((1,3,6,1,4,1,9303,4,1,3,2,1,19),_WsNeighbourPortPkts256to511Octets_Type())
wsNeighbourPortPkts256to511Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortPkts256to511Octets.setStatus(_A)
_WsNeighbourPortPkts512to1023Octets_Type=Unsigned32
_WsNeighbourPortPkts512to1023Octets_Object=MibTableColumn
wsNeighbourPortPkts512to1023Octets=_WsNeighbourPortPkts512to1023Octets_Object((1,3,6,1,4,1,9303,4,1,3,2,1,20),_WsNeighbourPortPkts512to1023Octets_Type())
wsNeighbourPortPkts512to1023Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortPkts512to1023Octets.setStatus(_A)
_WsNeighbourPortPkts1024to1522Octets_Type=Unsigned32
_WsNeighbourPortPkts1024to1522Octets_Object=MibTableColumn
wsNeighbourPortPkts1024to1522Octets=_WsNeighbourPortPkts1024to1522Octets_Object((1,3,6,1,4,1,9303,4,1,3,2,1,21),_WsNeighbourPortPkts1024to1522Octets_Type())
wsNeighbourPortPkts1024to1522Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortPkts1024to1522Octets.setStatus(_A)
_WsNeighbourPortRxOversizePkts_Type=Unsigned32
_WsNeighbourPortRxOversizePkts_Object=MibTableColumn
wsNeighbourPortRxOversizePkts=_WsNeighbourPortRxOversizePkts_Object((1,3,6,1,4,1,9303,4,1,3,2,1,22),_WsNeighbourPortRxOversizePkts_Type())
wsNeighbourPortRxOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortRxOversizePkts.setStatus(_A)
_WsNeighbourPortRxJabbers_Type=Unsigned32
_WsNeighbourPortRxJabbers_Object=MibTableColumn
wsNeighbourPortRxJabbers=_WsNeighbourPortRxJabbers_Object((1,3,6,1,4,1,9303,4,1,3,2,1,23),_WsNeighbourPortRxJabbers_Type())
wsNeighbourPortRxJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortRxJabbers.setStatus(_A)
_WsNeighbourPortRxAlignmentErrors_Type=Unsigned32
_WsNeighbourPortRxAlignmentErrors_Object=MibTableColumn
wsNeighbourPortRxAlignmentErrors=_WsNeighbourPortRxAlignmentErrors_Object((1,3,6,1,4,1,9303,4,1,3,2,1,24),_WsNeighbourPortRxAlignmentErrors_Type())
wsNeighbourPortRxAlignmentErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortRxAlignmentErrors.setStatus(_A)
_WsNeighbourPortRxFCSErrors_Type=Unsigned32
_WsNeighbourPortRxFCSErrors_Object=MibTableColumn
wsNeighbourPortRxFCSErrors=_WsNeighbourPortRxFCSErrors_Object((1,3,6,1,4,1,9303,4,1,3,2,1,25),_WsNeighbourPortRxFCSErrors_Type())
wsNeighbourPortRxFCSErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortRxFCSErrors.setStatus(_A)
_WsNeighbourPortRxGoodOctets_Type=Counter64
_WsNeighbourPortRxGoodOctets_Object=MibTableColumn
wsNeighbourPortRxGoodOctets=_WsNeighbourPortRxGoodOctets_Object((1,3,6,1,4,1,9303,4,1,3,2,1,26),_WsNeighbourPortRxGoodOctets_Type())
wsNeighbourPortRxGoodOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortRxGoodOctets.setStatus(_A)
_WsNeighbourPortRxDropPkts_Type=Unsigned32
_WsNeighbourPortRxDropPkts_Object=MibTableColumn
wsNeighbourPortRxDropPkts=_WsNeighbourPortRxDropPkts_Object((1,3,6,1,4,1,9303,4,1,3,2,1,27),_WsNeighbourPortRxDropPkts_Type())
wsNeighbourPortRxDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortRxDropPkts.setStatus(_A)
_WsNeighbourPortRxUnicastPkts_Type=Unsigned32
_WsNeighbourPortRxUnicastPkts_Object=MibTableColumn
wsNeighbourPortRxUnicastPkts=_WsNeighbourPortRxUnicastPkts_Object((1,3,6,1,4,1,9303,4,1,3,2,1,28),_WsNeighbourPortRxUnicastPkts_Type())
wsNeighbourPortRxUnicastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortRxUnicastPkts.setStatus(_A)
_WsNeighbourPortRxMulticastPkts_Type=Unsigned32
_WsNeighbourPortRxMulticastPkts_Object=MibTableColumn
wsNeighbourPortRxMulticastPkts=_WsNeighbourPortRxMulticastPkts_Object((1,3,6,1,4,1,9303,4,1,3,2,1,29),_WsNeighbourPortRxMulticastPkts_Type())
wsNeighbourPortRxMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortRxMulticastPkts.setStatus(_A)
_WsNeighbourPortRxBroadcastPkts_Type=Unsigned32
_WsNeighbourPortRxBroadcastPkts_Object=MibTableColumn
wsNeighbourPortRxBroadcastPkts=_WsNeighbourPortRxBroadcastPkts_Object((1,3,6,1,4,1,9303,4,1,3,2,1,30),_WsNeighbourPortRxBroadcastPkts_Type())
wsNeighbourPortRxBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortRxBroadcastPkts.setStatus(_A)
_WsNeighbourPortRxFragments_Type=Unsigned32
_WsNeighbourPortRxFragments_Object=MibTableColumn
wsNeighbourPortRxFragments=_WsNeighbourPortRxFragments_Object((1,3,6,1,4,1,9303,4,1,3,2,1,31),_WsNeighbourPortRxFragments_Type())
wsNeighbourPortRxFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortRxFragments.setStatus(_A)
_WsNeighbourPortRxExcessSizeDisc_Type=Unsigned32
_WsNeighbourPortRxExcessSizeDisc_Object=MibTableColumn
wsNeighbourPortRxExcessSizeDisc=_WsNeighbourPortRxExcessSizeDisc_Object((1,3,6,1,4,1,9303,4,1,3,2,1,32),_WsNeighbourPortRxExcessSizeDisc_Type())
wsNeighbourPortRxExcessSizeDisc.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortRxExcessSizeDisc.setStatus(_A)
_WsNeighbourPortRxSymbolError_Type=Unsigned32
_WsNeighbourPortRxSymbolError_Object=MibTableColumn
wsNeighbourPortRxSymbolError=_WsNeighbourPortRxSymbolError_Object((1,3,6,1,4,1,9303,4,1,3,2,1,33),_WsNeighbourPortRxSymbolError_Type())
wsNeighbourPortRxSymbolError.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortRxSymbolError.setStatus(_A)
_WsNeighbourPortSNPATable_Object=MibTable
wsNeighbourPortSNPATable=_WsNeighbourPortSNPATable_Object((1,3,6,1,4,1,9303,4,1,3,3))
if mibBuilder.loadTexts:wsNeighbourPortSNPATable.setStatus(_A)
_WsNeighbourPortSNPAEntry_Object=MibTableRow
wsNeighbourPortSNPAEntry=_WsNeighbourPortSNPAEntry_Object((1,3,6,1,4,1,9303,4,1,3,3,1))
wsNeighbourPortSNPAEntry.setIndexNames((0,_C,_e),(0,_C,_f),(0,_C,_g),(0,_C,_h))
if mibBuilder.loadTexts:wsNeighbourPortSNPAEntry.setStatus(_A)
_WsNeighbourPortSNPAIfIndex_Type=Unsigned32
_WsNeighbourPortSNPAIfIndex_Object=MibTableColumn
wsNeighbourPortSNPAIfIndex=_WsNeighbourPortSNPAIfIndex_Object((1,3,6,1,4,1,9303,4,1,3,3,1,1),_WsNeighbourPortSNPAIfIndex_Type())
wsNeighbourPortSNPAIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortSNPAIfIndex.setStatus(_A)
_WsNeighbourPortSNPANIndex_Type=Unsigned32
_WsNeighbourPortSNPANIndex_Object=MibTableColumn
wsNeighbourPortSNPANIndex=_WsNeighbourPortSNPANIndex_Object((1,3,6,1,4,1,9303,4,1,3,3,1,2),_WsNeighbourPortSNPANIndex_Type())
wsNeighbourPortSNPANIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortSNPANIndex.setStatus(_A)
_WsNeighbourPortSNPAPIndex_Type=Unsigned32
_WsNeighbourPortSNPAPIndex_Object=MibTableColumn
wsNeighbourPortSNPAPIndex=_WsNeighbourPortSNPAPIndex_Object((1,3,6,1,4,1,9303,4,1,3,3,1,3),_WsNeighbourPortSNPAPIndex_Type())
wsNeighbourPortSNPAPIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortSNPAPIndex.setStatus(_A)
_WsNeighbourPortSNPASIndex_Type=Unsigned32
_WsNeighbourPortSNPASIndex_Object=MibTableColumn
wsNeighbourPortSNPASIndex=_WsNeighbourPortSNPASIndex_Object((1,3,6,1,4,1,9303,4,1,3,3,1,4),_WsNeighbourPortSNPASIndex_Type())
wsNeighbourPortSNPASIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortSNPASIndex.setStatus(_A)
_WsNeighbourPortSNPASMCast_Type=Integer32
_WsNeighbourPortSNPASMCast_Object=MibTableColumn
wsNeighbourPortSNPASMCast=_WsNeighbourPortSNPASMCast_Object((1,3,6,1,4,1,9303,4,1,3,3,1,5),_WsNeighbourPortSNPASMCast_Type())
wsNeighbourPortSNPASMCast.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortSNPASMCast.setStatus(_A)
_WsNeighbourPortSNPA_Type=OctetString
_WsNeighbourPortSNPA_Object=MibTableColumn
wsNeighbourPortSNPA=_WsNeighbourPortSNPA_Object((1,3,6,1,4,1,9303,4,1,3,3,1,6),_WsNeighbourPortSNPA_Type())
wsNeighbourPortSNPA.setMaxAccess(_B)
if mibBuilder.loadTexts:wsNeighbourPortSNPA.setStatus(_A)
_WsSFPTable_Object=MibTable
wsSFPTable=_WsSFPTable_Object((1,3,6,1,4,1,9303,4,1,4))
if mibBuilder.loadTexts:wsSFPTable.setStatus(_A)
_WsSFPEntry_Object=MibTableRow
wsSFPEntry=_WsSFPEntry_Object((1,3,6,1,4,1,9303,4,1,4,1))
wsSFPEntry.setIndexNames((0,_C,_i))
if mibBuilder.loadTexts:wsSFPEntry.setStatus(_A)
_WsSFPIndex_Type=Unsigned32
_WsSFPIndex_Object=MibTableColumn
wsSFPIndex=_WsSFPIndex_Object((1,3,6,1,4,1,9303,4,1,4,1,1),_WsSFPIndex_Type())
wsSFPIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPIndex.setStatus(_A)
class _WsSFPStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_j,1),(_k,2)))
_WsSFPStatus_Type.__name__=_D
_WsSFPStatus_Object=MibTableColumn
wsSFPStatus=_WsSFPStatus_Object((1,3,6,1,4,1,9303,4,1,4,1,2),_WsSFPStatus_Type())
wsSFPStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPStatus.setStatus(_A)
class _WsSFPConnector_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,6,7,8,9,10,11,32,33)));namedValues=NamedValues(*(('sc',1),(_l,6),('lc',7),('mtrj',8),('mu',9),('sg',10),(_m,11),(_n,32),(_o,33)))
_WsSFPConnector_Type.__name__=_D
_WsSFPConnector_Object=MibTableColumn
wsSFPConnector=_WsSFPConnector_Object((1,3,6,1,4,1,9303,4,1,4,1,3),_WsSFPConnector_Type())
wsSFPConnector.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPConnector.setStatus(_A)
class _WsSFPTransceiver_Type(Bits):namedValues=NamedValues(*(('sBasePX',0),('sBaseBX10',1),('s100BaseFX',2),('s100BaseLX',3),('s1000BaseT',4),('s1000BaseCX',5),('s1000BaseLX',6),('s1000BaseSX',7)))
_WsSFPTransceiver_Type.__name__=_K
_WsSFPTransceiver_Object=MibTableColumn
wsSFPTransceiver=_WsSFPTransceiver_Object((1,3,6,1,4,1,9303,4,1,4,1,4),_WsSFPTransceiver_Type())
wsSFPTransceiver.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPTransceiver.setStatus(_A)
class _WsSFPEncoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_p,1),('e4B5B',2),('eNRZ',3),('eManchester',4)))
_WsSFPEncoding_Type.__name__=_D
_WsSFPEncoding_Object=MibTableColumn
wsSFPEncoding=_WsSFPEncoding_Object((1,3,6,1,4,1,9303,4,1,4,1,5),_WsSFPEncoding_Type())
wsSFPEncoding.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPEncoding.setStatus(_A)
_WsSFPBitrate_Type=Unsigned32
_WsSFPBitrate_Object=MibTableColumn
wsSFPBitrate=_WsSFPBitrate_Object((1,3,6,1,4,1,9303,4,1,4,1,6),_WsSFPBitrate_Type())
wsSFPBitrate.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPBitrate.setStatus(_A)
_WsSFPSingleModeLen_Type=Unsigned32
_WsSFPSingleModeLen_Object=MibTableColumn
wsSFPSingleModeLen=_WsSFPSingleModeLen_Object((1,3,6,1,4,1,9303,4,1,4,1,7),_WsSFPSingleModeLen_Type())
wsSFPSingleModeLen.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPSingleModeLen.setStatus(_A)
_WsSFPMultiMode50Len_Type=Unsigned32
_WsSFPMultiMode50Len_Object=MibTableColumn
wsSFPMultiMode50Len=_WsSFPMultiMode50Len_Object((1,3,6,1,4,1,9303,4,1,4,1,8),_WsSFPMultiMode50Len_Type())
wsSFPMultiMode50Len.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPMultiMode50Len.setStatus(_A)
_WsSFPMultiMode625Len_Type=Unsigned32
_WsSFPMultiMode625Len_Object=MibTableColumn
wsSFPMultiMode625Len=_WsSFPMultiMode625Len_Object((1,3,6,1,4,1,9303,4,1,4,1,9),_WsSFPMultiMode625Len_Type())
wsSFPMultiMode625Len.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPMultiMode625Len.setStatus(_A)
_WsSFPCopperLen_Type=Unsigned32
_WsSFPCopperLen_Object=MibTableColumn
wsSFPCopperLen=_WsSFPCopperLen_Object((1,3,6,1,4,1,9303,4,1,4,1,10),_WsSFPCopperLen_Type())
wsSFPCopperLen.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPCopperLen.setStatus(_A)
class _WsSFPTempStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_E,3),(_I,4),(_J,5)))
_WsSFPTempStatus_Type.__name__=_D
_WsSFPTempStatus_Object=MibTableColumn
wsSFPTempStatus=_WsSFPTempStatus_Object((1,3,6,1,4,1,9303,4,1,4,1,11),_WsSFPTempStatus_Type())
wsSFPTempStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPTempStatus.setStatus(_A)
_WsSFPTemp_Type=Integer32
_WsSFPTemp_Object=MibTableColumn
wsSFPTemp=_WsSFPTemp_Object((1,3,6,1,4,1,9303,4,1,4,1,12),_WsSFPTemp_Type())
wsSFPTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPTemp.setStatus(_A)
class _WsSFPVoltStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_E,3),(_I,4),(_J,5)))
_WsSFPVoltStatus_Type.__name__=_D
_WsSFPVoltStatus_Object=MibTableColumn
wsSFPVoltStatus=_WsSFPVoltStatus_Object((1,3,6,1,4,1,9303,4,1,4,1,13),_WsSFPVoltStatus_Type())
wsSFPVoltStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPVoltStatus.setStatus(_A)
_WsSFPVolt_Type=Integer32
_WsSFPVolt_Object=MibTableColumn
wsSFPVolt=_WsSFPVolt_Object((1,3,6,1,4,1,9303,4,1,4,1,14),_WsSFPVolt_Type())
wsSFPVolt.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPVolt.setStatus(_A)
class _WsSFPTXCurrentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_E,3),(_I,4),(_J,5)))
_WsSFPTXCurrentStatus_Type.__name__=_D
_WsSFPTXCurrentStatus_Object=MibTableColumn
wsSFPTXCurrentStatus=_WsSFPTXCurrentStatus_Object((1,3,6,1,4,1,9303,4,1,4,1,15),_WsSFPTXCurrentStatus_Type())
wsSFPTXCurrentStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPTXCurrentStatus.setStatus(_A)
_WsSFPTXCurrent_Type=Integer32
_WsSFPTXCurrent_Object=MibTableColumn
wsSFPTXCurrent=_WsSFPTXCurrent_Object((1,3,6,1,4,1,9303,4,1,4,1,16),_WsSFPTXCurrent_Type())
wsSFPTXCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPTXCurrent.setStatus(_A)
class _WsSFPTXPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_E,3),(_I,4),(_J,5)))
_WsSFPTXPowerStatus_Type.__name__=_D
_WsSFPTXPowerStatus_Object=MibTableColumn
wsSFPTXPowerStatus=_WsSFPTXPowerStatus_Object((1,3,6,1,4,1,9303,4,1,4,1,17),_WsSFPTXPowerStatus_Type())
wsSFPTXPowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPTXPowerStatus.setStatus(_A)
_WsSFPTXPower_Type=Integer32
_WsSFPTXPower_Object=MibTableColumn
wsSFPTXPower=_WsSFPTXPower_Object((1,3,6,1,4,1,9303,4,1,4,1,18),_WsSFPTXPower_Type())
wsSFPTXPower.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPTXPower.setStatus(_A)
class _WsSFPRXPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_E,3),(_I,4),(_J,5)))
_WsSFPRXPowerStatus_Type.__name__=_D
_WsSFPRXPowerStatus_Object=MibTableColumn
wsSFPRXPowerStatus=_WsSFPRXPowerStatus_Object((1,3,6,1,4,1,9303,4,1,4,1,19),_WsSFPRXPowerStatus_Type())
wsSFPRXPowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPRXPowerStatus.setStatus(_A)
_WsSFPRXPower_Type=Integer32
_WsSFPRXPower_Object=MibTableColumn
wsSFPRXPower=_WsSFPRXPower_Object((1,3,6,1,4,1,9303,4,1,4,1,20),_WsSFPRXPower_Type())
wsSFPRXPower.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPRXPower.setStatus(_A)
class _WsSFPTransceiverExt_Type(Bits):namedValues=NamedValues(*(('s10000BaseER',0),('s10000BaseLRM',1),('s10000BaseLR',2),('s10000BaseSR',3),('sActiveCable',4),('sPassiveCable',5),('reserved6',6),('reserved7',7)))
_WsSFPTransceiverExt_Type.__name__=_K
_WsSFPTransceiverExt_Object=MibTableColumn
wsSFPTransceiverExt=_WsSFPTransceiverExt_Object((1,3,6,1,4,1,9303,4,1,4,1,21),_WsSFPTransceiverExt_Type())
wsSFPTransceiverExt.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPTransceiverExt.setStatus(_A)
_WsSFPTXdBmPower_Type=Integer32
_WsSFPTXdBmPower_Object=MibTableColumn
wsSFPTXdBmPower=_WsSFPTXdBmPower_Object((1,3,6,1,4,1,9303,4,1,4,1,22),_WsSFPTXdBmPower_Type())
wsSFPTXdBmPower.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPTXdBmPower.setStatus(_A)
_WsSFPRXdBmPower_Type=Integer32
_WsSFPRXdBmPower_Object=MibTableColumn
wsSFPRXdBmPower=_WsSFPRXdBmPower_Object((1,3,6,1,4,1,9303,4,1,4,1,23),_WsSFPRXdBmPower_Type())
wsSFPRXdBmPower.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPRXdBmPower.setStatus(_A)
_WsSFPTempNormalLow_Type=Integer32
_WsSFPTempNormalLow_Object=MibTableColumn
wsSFPTempNormalLow=_WsSFPTempNormalLow_Object((1,3,6,1,4,1,9303,4,1,4,1,24),_WsSFPTempNormalLow_Type())
wsSFPTempNormalLow.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPTempNormalLow.setStatus(_A)
_WsSFPTempNormalHigh_Type=Integer32
_WsSFPTempNormalHigh_Object=MibTableColumn
wsSFPTempNormalHigh=_WsSFPTempNormalHigh_Object((1,3,6,1,4,1,9303,4,1,4,1,25),_WsSFPTempNormalHigh_Type())
wsSFPTempNormalHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPTempNormalHigh.setStatus(_A)
_WsSFPTempWarningLow_Type=Integer32
_WsSFPTempWarningLow_Object=MibTableColumn
wsSFPTempWarningLow=_WsSFPTempWarningLow_Object((1,3,6,1,4,1,9303,4,1,4,1,26),_WsSFPTempWarningLow_Type())
wsSFPTempWarningLow.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPTempWarningLow.setStatus(_A)
_WsSFPTempWarningHigh_Type=Integer32
_WsSFPTempWarningHigh_Object=MibTableColumn
wsSFPTempWarningHigh=_WsSFPTempWarningHigh_Object((1,3,6,1,4,1,9303,4,1,4,1,27),_WsSFPTempWarningHigh_Type())
wsSFPTempWarningHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPTempWarningHigh.setStatus(_A)
_WsSFPVoltNormalLow_Type=Integer32
_WsSFPVoltNormalLow_Object=MibTableColumn
wsSFPVoltNormalLow=_WsSFPVoltNormalLow_Object((1,3,6,1,4,1,9303,4,1,4,1,28),_WsSFPVoltNormalLow_Type())
wsSFPVoltNormalLow.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPVoltNormalLow.setStatus(_A)
_WsSFPVoltNormalHigh_Type=Integer32
_WsSFPVoltNormalHigh_Object=MibTableColumn
wsSFPVoltNormalHigh=_WsSFPVoltNormalHigh_Object((1,3,6,1,4,1,9303,4,1,4,1,29),_WsSFPVoltNormalHigh_Type())
wsSFPVoltNormalHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPVoltNormalHigh.setStatus(_A)
_WsSFPVoltWarningLow_Type=Integer32
_WsSFPVoltWarningLow_Object=MibTableColumn
wsSFPVoltWarningLow=_WsSFPVoltWarningLow_Object((1,3,6,1,4,1,9303,4,1,4,1,30),_WsSFPVoltWarningLow_Type())
wsSFPVoltWarningLow.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPVoltWarningLow.setStatus(_A)
_WsSFPVoltWarningHigh_Type=Integer32
_WsSFPVoltWarningHigh_Object=MibTableColumn
wsSFPVoltWarningHigh=_WsSFPVoltWarningHigh_Object((1,3,6,1,4,1,9303,4,1,4,1,31),_WsSFPVoltWarningHigh_Type())
wsSFPVoltWarningHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPVoltWarningHigh.setStatus(_A)
_WsSFPTXCurrentNormalLow_Type=Integer32
_WsSFPTXCurrentNormalLow_Object=MibTableColumn
wsSFPTXCurrentNormalLow=_WsSFPTXCurrentNormalLow_Object((1,3,6,1,4,1,9303,4,1,4,1,32),_WsSFPTXCurrentNormalLow_Type())
wsSFPTXCurrentNormalLow.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPTXCurrentNormalLow.setStatus(_A)
_WsSFPTXCurrentNormalHigh_Type=Integer32
_WsSFPTXCurrentNormalHigh_Object=MibTableColumn
wsSFPTXCurrentNormalHigh=_WsSFPTXCurrentNormalHigh_Object((1,3,6,1,4,1,9303,4,1,4,1,33),_WsSFPTXCurrentNormalHigh_Type())
wsSFPTXCurrentNormalHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPTXCurrentNormalHigh.setStatus(_A)
_WsSFPTXCurrentWarningLow_Type=Integer32
_WsSFPTXCurrentWarningLow_Object=MibTableColumn
wsSFPTXCurrentWarningLow=_WsSFPTXCurrentWarningLow_Object((1,3,6,1,4,1,9303,4,1,4,1,34),_WsSFPTXCurrentWarningLow_Type())
wsSFPTXCurrentWarningLow.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPTXCurrentWarningLow.setStatus(_A)
_WsSFPTXCurrentWarningHigh_Type=Integer32
_WsSFPTXCurrentWarningHigh_Object=MibTableColumn
wsSFPTXCurrentWarningHigh=_WsSFPTXCurrentWarningHigh_Object((1,3,6,1,4,1,9303,4,1,4,1,35),_WsSFPTXCurrentWarningHigh_Type())
wsSFPTXCurrentWarningHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPTXCurrentWarningHigh.setStatus(_A)
_WsSFPTXOutputPowNormalLowuW_Type=Integer32
_WsSFPTXOutputPowNormalLowuW_Object=MibTableColumn
wsSFPTXOutputPowNormalLowuW=_WsSFPTXOutputPowNormalLowuW_Object((1,3,6,1,4,1,9303,4,1,4,1,36),_WsSFPTXOutputPowNormalLowuW_Type())
wsSFPTXOutputPowNormalLowuW.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPTXOutputPowNormalLowuW.setStatus(_A)
_WsSFPTXOutputPowNormalHighuW_Type=Integer32
_WsSFPTXOutputPowNormalHighuW_Object=MibTableColumn
wsSFPTXOutputPowNormalHighuW=_WsSFPTXOutputPowNormalHighuW_Object((1,3,6,1,4,1,9303,4,1,4,1,37),_WsSFPTXOutputPowNormalHighuW_Type())
wsSFPTXOutputPowNormalHighuW.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPTXOutputPowNormalHighuW.setStatus(_A)
_WsSFPTXOutputPowWarningLowuW_Type=Integer32
_WsSFPTXOutputPowWarningLowuW_Object=MibTableColumn
wsSFPTXOutputPowWarningLowuW=_WsSFPTXOutputPowWarningLowuW_Object((1,3,6,1,4,1,9303,4,1,4,1,38),_WsSFPTXOutputPowWarningLowuW_Type())
wsSFPTXOutputPowWarningLowuW.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPTXOutputPowWarningLowuW.setStatus(_A)
_WsSFPTXOutputPowWarningHighuW_Type=Integer32
_WsSFPTXOutputPowWarningHighuW_Object=MibTableColumn
wsSFPTXOutputPowWarningHighuW=_WsSFPTXOutputPowWarningHighuW_Object((1,3,6,1,4,1,9303,4,1,4,1,39),_WsSFPTXOutputPowWarningHighuW_Type())
wsSFPTXOutputPowWarningHighuW.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPTXOutputPowWarningHighuW.setStatus(_A)
_WsSFPTXOutputPowNormalLowdBm_Type=Integer32
_WsSFPTXOutputPowNormalLowdBm_Object=MibTableColumn
wsSFPTXOutputPowNormalLowdBm=_WsSFPTXOutputPowNormalLowdBm_Object((1,3,6,1,4,1,9303,4,1,4,1,40),_WsSFPTXOutputPowNormalLowdBm_Type())
wsSFPTXOutputPowNormalLowdBm.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPTXOutputPowNormalLowdBm.setStatus(_A)
_WsSFPTXOutputPowNormalHighdBm_Type=Integer32
_WsSFPTXOutputPowNormalHighdBm_Object=MibTableColumn
wsSFPTXOutputPowNormalHighdBm=_WsSFPTXOutputPowNormalHighdBm_Object((1,3,6,1,4,1,9303,4,1,4,1,41),_WsSFPTXOutputPowNormalHighdBm_Type())
wsSFPTXOutputPowNormalHighdBm.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPTXOutputPowNormalHighdBm.setStatus(_A)
_WsSFPTXOutputPowWarningLowdBm_Type=Integer32
_WsSFPTXOutputPowWarningLowdBm_Object=MibTableColumn
wsSFPTXOutputPowWarningLowdBm=_WsSFPTXOutputPowWarningLowdBm_Object((1,3,6,1,4,1,9303,4,1,4,1,42),_WsSFPTXOutputPowWarningLowdBm_Type())
wsSFPTXOutputPowWarningLowdBm.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPTXOutputPowWarningLowdBm.setStatus(_A)
_WsSFPTXOutputPowWarningHighdBm_Type=Integer32
_WsSFPTXOutputPowWarningHighdBm_Object=MibTableColumn
wsSFPTXOutputPowWarningHighdBm=_WsSFPTXOutputPowWarningHighdBm_Object((1,3,6,1,4,1,9303,4,1,4,1,43),_WsSFPTXOutputPowWarningHighdBm_Type())
wsSFPTXOutputPowWarningHighdBm.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPTXOutputPowWarningHighdBm.setStatus(_A)
_WsSFPRXInputPowNormalLowuW_Type=Integer32
_WsSFPRXInputPowNormalLowuW_Object=MibTableColumn
wsSFPRXInputPowNormalLowuW=_WsSFPRXInputPowNormalLowuW_Object((1,3,6,1,4,1,9303,4,1,4,1,44),_WsSFPRXInputPowNormalLowuW_Type())
wsSFPRXInputPowNormalLowuW.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPRXInputPowNormalLowuW.setStatus(_A)
_WsSFPRXInputPowNormalHighuW_Type=Integer32
_WsSFPRXInputPowNormalHighuW_Object=MibTableColumn
wsSFPRXInputPowNormalHighuW=_WsSFPRXInputPowNormalHighuW_Object((1,3,6,1,4,1,9303,4,1,4,1,45),_WsSFPRXInputPowNormalHighuW_Type())
wsSFPRXInputPowNormalHighuW.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPRXInputPowNormalHighuW.setStatus(_A)
_WsSFPRXInputPowWarningLowuW_Type=Integer32
_WsSFPRXInputPowWarningLowuW_Object=MibTableColumn
wsSFPRXInputPowWarningLowuW=_WsSFPRXInputPowWarningLowuW_Object((1,3,6,1,4,1,9303,4,1,4,1,46),_WsSFPRXInputPowWarningLowuW_Type())
wsSFPRXInputPowWarningLowuW.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPRXInputPowWarningLowuW.setStatus(_A)
_WsSFPRXInputPowWarningHighuW_Type=Integer32
_WsSFPRXInputPowWarningHighuW_Object=MibTableColumn
wsSFPRXInputPowWarningHighuW=_WsSFPRXInputPowWarningHighuW_Object((1,3,6,1,4,1,9303,4,1,4,1,47),_WsSFPRXInputPowWarningHighuW_Type())
wsSFPRXInputPowWarningHighuW.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPRXInputPowWarningHighuW.setStatus(_A)
_WsSFPRXInputPowNormalLowdBm_Type=Integer32
_WsSFPRXInputPowNormalLowdBm_Object=MibTableColumn
wsSFPRXInputPowNormalLowdBm=_WsSFPRXInputPowNormalLowdBm_Object((1,3,6,1,4,1,9303,4,1,4,1,48),_WsSFPRXInputPowNormalLowdBm_Type())
wsSFPRXInputPowNormalLowdBm.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPRXInputPowNormalLowdBm.setStatus(_A)
_WsSFPRXInputPowNormalHighdBm_Type=Integer32
_WsSFPRXInputPowNormalHighdBm_Object=MibTableColumn
wsSFPRXInputPowNormalHighdBm=_WsSFPRXInputPowNormalHighdBm_Object((1,3,6,1,4,1,9303,4,1,4,1,49),_WsSFPRXInputPowNormalHighdBm_Type())
wsSFPRXInputPowNormalHighdBm.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPRXInputPowNormalHighdBm.setStatus(_A)
_WsSFPRXInputPowWarningLowdBm_Type=Integer32
_WsSFPRXInputPowWarningLowdBm_Object=MibTableColumn
wsSFPRXInputPowWarningLowdBm=_WsSFPRXInputPowWarningLowdBm_Object((1,3,6,1,4,1,9303,4,1,4,1,50),_WsSFPRXInputPowWarningLowdBm_Type())
wsSFPRXInputPowWarningLowdBm.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPRXInputPowWarningLowdBm.setStatus(_A)
_WsSFPRXInputPowWarningHighdBm_Type=Integer32
_WsSFPRXInputPowWarningHighdBm_Object=MibTableColumn
wsSFPRXInputPowWarningHighdBm=_WsSFPRXInputPowWarningHighdBm_Object((1,3,6,1,4,1,9303,4,1,4,1,51),_WsSFPRXInputPowWarningHighdBm_Type())
wsSFPRXInputPowWarningHighdBm.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPRXInputPowWarningHighdBm.setStatus(_A)
class _WsSFPPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WsSFPPartNumber_Type.__name__=_N
_WsSFPPartNumber_Object=MibTableColumn
wsSFPPartNumber=_WsSFPPartNumber_Object((1,3,6,1,4,1,9303,4,1,4,1,52),_WsSFPPartNumber_Type())
wsSFPPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPPartNumber.setStatus(_A)
class _WsSFPSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WsSFPSerialNumber_Type.__name__=_N
_WsSFPSerialNumber_Object=MibTableColumn
wsSFPSerialNumber=_WsSFPSerialNumber_Object((1,3,6,1,4,1,9303,4,1,4,1,53),_WsSFPSerialNumber_Type())
wsSFPSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wsSFPSerialNumber.setStatus(_A)
_WsAccounting_ObjectIdentity=ObjectIdentity
wsAccounting=_WsAccounting_ObjectIdentity((1,3,6,1,4,1,9303,4,1,5))
if mibBuilder.loadTexts:wsAccounting.setStatus(_A)
_WsPolicyTable_Object=MibTable
wsPolicyTable=_WsPolicyTable_Object((1,3,6,1,4,1,9303,4,1,5,1))
if mibBuilder.loadTexts:wsPolicyTable.setStatus(_A)
_WsPolicyEntry_Object=MibTableRow
wsPolicyEntry=_WsPolicyEntry_Object((1,3,6,1,4,1,9303,4,1,5,1,1))
wsPolicyEntry.setIndexNames((0,_C,_q),(0,_C,_r))
if mibBuilder.loadTexts:wsPolicyEntry.setStatus(_A)
_WsPolicyIfIndex_Type=Unsigned32
_WsPolicyIfIndex_Object=MibTableColumn
wsPolicyIfIndex=_WsPolicyIfIndex_Object((1,3,6,1,4,1,9303,4,1,5,1,1,1),_WsPolicyIfIndex_Type())
wsPolicyIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wsPolicyIfIndex.setStatus(_A)
_WsPolicyIfName_Type=DisplayString
_WsPolicyIfName_Object=MibTableColumn
wsPolicyIfName=_WsPolicyIfName_Object((1,3,6,1,4,1,9303,4,1,5,1,1,2),_WsPolicyIfName_Type())
wsPolicyIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:wsPolicyIfName.setStatus(_A)
_WsPolicyName_Type=DisplayString
_WsPolicyName_Object=MibTableColumn
wsPolicyName=_WsPolicyName_Object((1,3,6,1,4,1,9303,4,1,5,1,1,3),_WsPolicyName_Type())
wsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:wsPolicyName.setStatus(_A)
_WsPolicyCookie_Type=DisplayString
_WsPolicyCookie_Object=MibTableColumn
wsPolicyCookie=_WsPolicyCookie_Object((1,3,6,1,4,1,9303,4,1,5,1,1,4),_WsPolicyCookie_Type())
wsPolicyCookie.setMaxAccess(_B)
if mibBuilder.loadTexts:wsPolicyCookie.setStatus(_A)
_WsPolicyInPkts_Type=Counter64
_WsPolicyInPkts_Object=MibTableColumn
wsPolicyInPkts=_WsPolicyInPkts_Object((1,3,6,1,4,1,9303,4,1,5,1,1,5),_WsPolicyInPkts_Type())
wsPolicyInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wsPolicyInPkts.setStatus(_A)
_WsPolicyInBytes_Type=Counter64
_WsPolicyInBytes_Object=MibTableColumn
wsPolicyInBytes=_WsPolicyInBytes_Object((1,3,6,1,4,1,9303,4,1,5,1,1,6),_WsPolicyInBytes_Type())
wsPolicyInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wsPolicyInBytes.setStatus(_A)
_WsPolicyInDrops_Type=Counter64
_WsPolicyInDrops_Object=MibTableColumn
wsPolicyInDrops=_WsPolicyInDrops_Object((1,3,6,1,4,1,9303,4,1,5,1,1,7),_WsPolicyInDrops_Type())
wsPolicyInDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:wsPolicyInDrops.setStatus(_A)
_WsPolicyOutPkts_Type=Counter64
_WsPolicyOutPkts_Object=MibTableColumn
wsPolicyOutPkts=_WsPolicyOutPkts_Object((1,3,6,1,4,1,9303,4,1,5,1,1,8),_WsPolicyOutPkts_Type())
wsPolicyOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wsPolicyOutPkts.setStatus(_A)
_WsPolicyOutBytes_Type=Counter64
_WsPolicyOutBytes_Object=MibTableColumn
wsPolicyOutBytes=_WsPolicyOutBytes_Object((1,3,6,1,4,1,9303,4,1,5,1,1,9),_WsPolicyOutBytes_Type())
wsPolicyOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wsPolicyOutBytes.setStatus(_A)
_WsPolicyOutDrops_Type=Counter64
_WsPolicyOutDrops_Object=MibTableColumn
wsPolicyOutDrops=_WsPolicyOutDrops_Object((1,3,6,1,4,1,9303,4,1,5,1,1,10),_WsPolicyOutDrops_Type())
wsPolicyOutDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:wsPolicyOutDrops.setStatus(_A)
_WsPolicyUsedCnt_Type=Gauge32
_WsPolicyUsedCnt_Object=MibTableColumn
wsPolicyUsedCnt=_WsPolicyUsedCnt_Object((1,3,6,1,4,1,9303,4,1,5,1,1,11),_WsPolicyUsedCnt_Type())
wsPolicyUsedCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:wsPolicyUsedCnt.setStatus(_A)
_WsXFPTable_Object=MibTable
wsXFPTable=_WsXFPTable_Object((1,3,6,1,4,1,9303,4,1,6))
if mibBuilder.loadTexts:wsXFPTable.setStatus(_A)
_WsXFPEntry_Object=MibTableRow
wsXFPEntry=_WsXFPEntry_Object((1,3,6,1,4,1,9303,4,1,6,1))
wsXFPEntry.setIndexNames((0,_C,_s))
if mibBuilder.loadTexts:wsXFPEntry.setStatus(_A)
_WsXFPIndex_Type=Unsigned32
_WsXFPIndex_Object=MibTableColumn
wsXFPIndex=_WsXFPIndex_Object((1,3,6,1,4,1,9303,4,1,6,1,1),_WsXFPIndex_Type())
wsXFPIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wsXFPIndex.setStatus(_A)
class _WsXFPStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_j,1),(_k,2)))
_WsXFPStatus_Type.__name__=_D
_WsXFPStatus_Object=MibTableColumn
wsXFPStatus=_WsXFPStatus_Object((1,3,6,1,4,1,9303,4,1,6,1,2),_WsXFPStatus_Type())
wsXFPStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wsXFPStatus.setStatus(_A)
class _WsXFPConnector_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,6,7,8,9,10,11,32,33)));namedValues=NamedValues(*(('sc',1),(_l,6),('lc',7),('mtrj',8),('mu',9),('sg',10),(_m,11),(_n,32),(_o,33)))
_WsXFPConnector_Type.__name__=_D
_WsXFPConnector_Object=MibTableColumn
wsXFPConnector=_WsXFPConnector_Object((1,3,6,1,4,1,9303,4,1,6,1,3),_WsXFPConnector_Type())
wsXFPConnector.setMaxAccess(_B)
if mibBuilder.loadTexts:wsXFPConnector.setStatus(_A)
class _WsXFPTransceiver_Type(Bits):namedValues=NamedValues(*((_R,0),('s10GBaseEW',1),('s10GBaseLW',2),('s10GBaseSW',3),('s10GBaseLRM',4),('s10GBaseER',5),('s10GBaseLR',6),('s10GBaseSR',7)))
_WsXFPTransceiver_Type.__name__=_K
_WsXFPTransceiver_Object=MibTableColumn
wsXFPTransceiver=_WsXFPTransceiver_Object((1,3,6,1,4,1,9303,4,1,6,1,4),_WsXFPTransceiver_Type())
wsXFPTransceiver.setMaxAccess(_B)
if mibBuilder.loadTexts:wsXFPTransceiver.setStatus(_A)
class _WsXFPEncoding_Type(Bits):namedValues=NamedValues(*((_R,0),(_c,1),(_d,2),('eRZ',3),('eNRZ',4),('eSonetScrambl',5),(_p,6),('e64B66B',7)))
_WsXFPEncoding_Type.__name__=_K
_WsXFPEncoding_Object=MibTableColumn
wsXFPEncoding=_WsXFPEncoding_Object((1,3,6,1,4,1,9303,4,1,6,1,5),_WsXFPEncoding_Type())
wsXFPEncoding.setMaxAccess(_B)
if mibBuilder.loadTexts:wsXFPEncoding.setStatus(_A)
_WsXFPBitrateMin_Type=Unsigned32
_WsXFPBitrateMin_Object=MibTableColumn
wsXFPBitrateMin=_WsXFPBitrateMin_Object((1,3,6,1,4,1,9303,4,1,6,1,6),_WsXFPBitrateMin_Type())
wsXFPBitrateMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wsXFPBitrateMin.setStatus(_A)
_WsXFPBitrateMax_Type=Unsigned32
_WsXFPBitrateMax_Object=MibTableColumn
wsXFPBitrateMax=_WsXFPBitrateMax_Object((1,3,6,1,4,1,9303,4,1,6,1,7),_WsXFPBitrateMax_Type())
wsXFPBitrateMax.setMaxAccess(_B)
if mibBuilder.loadTexts:wsXFPBitrateMax.setStatus(_A)
_WsXFPSingleModeLen_Type=Unsigned32
_WsXFPSingleModeLen_Object=MibTableColumn
wsXFPSingleModeLen=_WsXFPSingleModeLen_Object((1,3,6,1,4,1,9303,4,1,6,1,8),_WsXFPSingleModeLen_Type())
wsXFPSingleModeLen.setMaxAccess(_B)
if mibBuilder.loadTexts:wsXFPSingleModeLen.setStatus(_A)
_WsXFPMultiMode50Len_Type=Unsigned32
_WsXFPMultiMode50Len_Object=MibTableColumn
wsXFPMultiMode50Len=_WsXFPMultiMode50Len_Object((1,3,6,1,4,1,9303,4,1,6,1,9),_WsXFPMultiMode50Len_Type())
wsXFPMultiMode50Len.setMaxAccess(_B)
if mibBuilder.loadTexts:wsXFPMultiMode50Len.setStatus(_A)
_WsXFPMultiMode625Len_Type=Unsigned32
_WsXFPMultiMode625Len_Object=MibTableColumn
wsXFPMultiMode625Len=_WsXFPMultiMode625Len_Object((1,3,6,1,4,1,9303,4,1,6,1,10),_WsXFPMultiMode625Len_Type())
wsXFPMultiMode625Len.setMaxAccess(_B)
if mibBuilder.loadTexts:wsXFPMultiMode625Len.setStatus(_A)
_WsXFPCopperLen_Type=Unsigned32
_WsXFPCopperLen_Object=MibTableColumn
wsXFPCopperLen=_WsXFPCopperLen_Object((1,3,6,1,4,1,9303,4,1,6,1,11),_WsXFPCopperLen_Type())
wsXFPCopperLen.setMaxAccess(_B)
if mibBuilder.loadTexts:wsXFPCopperLen.setStatus(_A)
class _WsXFPTempStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_E,3),(_I,4),(_J,5)))
_WsXFPTempStatus_Type.__name__=_D
_WsXFPTempStatus_Object=MibTableColumn
wsXFPTempStatus=_WsXFPTempStatus_Object((1,3,6,1,4,1,9303,4,1,6,1,12),_WsXFPTempStatus_Type())
wsXFPTempStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wsXFPTempStatus.setStatus(_A)
_WsXFPTemp_Type=Integer32
_WsXFPTemp_Object=MibTableColumn
wsXFPTemp=_WsXFPTemp_Object((1,3,6,1,4,1,9303,4,1,6,1,13),_WsXFPTemp_Type())
wsXFPTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:wsXFPTemp.setStatus(_A)
class _WsXFPTXCurrentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_E,3),(_I,4),(_J,5)))
_WsXFPTXCurrentStatus_Type.__name__=_D
_WsXFPTXCurrentStatus_Object=MibTableColumn
wsXFPTXCurrentStatus=_WsXFPTXCurrentStatus_Object((1,3,6,1,4,1,9303,4,1,6,1,14),_WsXFPTXCurrentStatus_Type())
wsXFPTXCurrentStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wsXFPTXCurrentStatus.setStatus(_A)
_WsXFPTXCurrent_Type=Integer32
_WsXFPTXCurrent_Object=MibTableColumn
wsXFPTXCurrent=_WsXFPTXCurrent_Object((1,3,6,1,4,1,9303,4,1,6,1,15),_WsXFPTXCurrent_Type())
wsXFPTXCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:wsXFPTXCurrent.setStatus(_A)
class _WsXFPTXPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_E,3),(_I,4),(_J,5)))
_WsXFPTXPowerStatus_Type.__name__=_D
_WsXFPTXPowerStatus_Object=MibTableColumn
wsXFPTXPowerStatus=_WsXFPTXPowerStatus_Object((1,3,6,1,4,1,9303,4,1,6,1,16),_WsXFPTXPowerStatus_Type())
wsXFPTXPowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wsXFPTXPowerStatus.setStatus(_A)
_WsXFPTXPower_Type=Integer32
_WsXFPTXPower_Object=MibTableColumn
wsXFPTXPower=_WsXFPTXPower_Object((1,3,6,1,4,1,9303,4,1,6,1,17),_WsXFPTXPower_Type())
wsXFPTXPower.setMaxAccess(_B)
if mibBuilder.loadTexts:wsXFPTXPower.setStatus(_A)
class _WsXFPRXPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_E,3),(_I,4),(_J,5)))
_WsXFPRXPowerStatus_Type.__name__=_D
_WsXFPRXPowerStatus_Object=MibTableColumn
wsXFPRXPowerStatus=_WsXFPRXPowerStatus_Object((1,3,6,1,4,1,9303,4,1,6,1,18),_WsXFPRXPowerStatus_Type())
wsXFPRXPowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wsXFPRXPowerStatus.setStatus(_A)
_WsXFPRXPower_Type=Integer32
_WsXFPRXPower_Object=MibTableColumn
wsXFPRXPower=_WsXFPRXPower_Object((1,3,6,1,4,1,9303,4,1,6,1,19),_WsXFPRXPower_Type())
wsXFPRXPower.setMaxAccess(_B)
if mibBuilder.loadTexts:wsXFPRXPower.setStatus(_A)
_WsIfXTable_Object=MibTable
wsIfXTable=_WsIfXTable_Object((1,3,6,1,4,1,9303,4,1,7))
if mibBuilder.loadTexts:wsIfXTable.setStatus(_A)
_WsIfXEntry_Object=MibTableRow
wsIfXEntry=_WsIfXEntry_Object((1,3,6,1,4,1,9303,4,1,7,1))
if mibBuilder.loadTexts:wsIfXEntry.setStatus(_A)
_IfHCInErrors_Type=Counter64
_IfHCInErrors_Object=MibTableColumn
ifHCInErrors=_IfHCInErrors_Object((1,3,6,1,4,1,9303,4,1,7,1,1),_IfHCInErrors_Type())
ifHCInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ifHCInErrors.setStatus(_A)
_IfHCInRunts_Type=Counter64
_IfHCInRunts_Object=MibTableColumn
ifHCInRunts=_IfHCInRunts_Object((1,3,6,1,4,1,9303,4,1,7,1,2),_IfHCInRunts_Type())
ifHCInRunts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifHCInRunts.setStatus(_A)
_IfHCInOversized_Type=Counter64
_IfHCInOversized_Object=MibTableColumn
ifHCInOversized=_IfHCInOversized_Object((1,3,6,1,4,1,9303,4,1,7,1,3),_IfHCInOversized_Type())
ifHCInOversized.setMaxAccess(_B)
if mibBuilder.loadTexts:ifHCInOversized.setStatus(_A)
_IfHCInCRCErrors_Type=Counter64
_IfHCInCRCErrors_Object=MibTableColumn
ifHCInCRCErrors=_IfHCInCRCErrors_Object((1,3,6,1,4,1,9303,4,1,7,1,4),_IfHCInCRCErrors_Type())
ifHCInCRCErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ifHCInCRCErrors.setStatus(_A)
_IfHCInJabbers_Type=Counter64
_IfHCInJabbers_Object=MibTableColumn
ifHCInJabbers=_IfHCInJabbers_Object((1,3,6,1,4,1,9303,4,1,7,1,5),_IfHCInJabbers_Type())
ifHCInJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:ifHCInJabbers.setStatus(_A)
_IfHCInFragments_Type=Counter64
_IfHCInFragments_Object=MibTableColumn
ifHCInFragments=_IfHCInFragments_Object((1,3,6,1,4,1,9303,4,1,7,1,6),_IfHCInFragments_Type())
ifHCInFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:ifHCInFragments.setStatus(_A)
_IfHCInSymbolErrors_Type=Counter64
_IfHCInSymbolErrors_Object=MibTableColumn
ifHCInSymbolErrors=_IfHCInSymbolErrors_Object((1,3,6,1,4,1,9303,4,1,7,1,7),_IfHCInSymbolErrors_Type())
ifHCInSymbolErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ifHCInSymbolErrors.setStatus(_A)
_IfHCInAlignmentErrors_Type=Counter64
_IfHCInAlignmentErrors_Object=MibTableColumn
ifHCInAlignmentErrors=_IfHCInAlignmentErrors_Object((1,3,6,1,4,1,9303,4,1,7,1,8),_IfHCInAlignmentErrors_Type())
ifHCInAlignmentErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ifHCInAlignmentErrors.setStatus(_A)
_IfHCOutErrors_Type=Counter64
_IfHCOutErrors_Object=MibTableColumn
ifHCOutErrors=_IfHCOutErrors_Object((1,3,6,1,4,1,9303,4,1,7,1,9),_IfHCOutErrors_Type())
ifHCOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ifHCOutErrors.setStatus(_A)
_IfHCOutCollisions_Type=Counter64
_IfHCOutCollisions_Object=MibTableColumn
ifHCOutCollisions=_IfHCOutCollisions_Object((1,3,6,1,4,1,9303,4,1,7,1,10),_IfHCOutCollisions_Type())
ifHCOutCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:ifHCOutCollisions.setStatus(_A)
_IfHCOutDeferred_Type=Counter64
_IfHCOutDeferred_Object=MibTableColumn
ifHCOutDeferred=_IfHCOutDeferred_Object((1,3,6,1,4,1,9303,4,1,7,1,11),_IfHCOutDeferred_Type())
ifHCOutDeferred.setMaxAccess(_B)
if mibBuilder.loadTexts:ifHCOutDeferred.setStatus(_A)
ifEntry.registerAugmentions((_C,_t))
wsIfXEntry.setIndexNames(*ifEntry.getIndexNames())
wsIbosTempLow=NotificationType((1,3,6,1,4,1,9303,4,1,2,0,1))
wsIbosTempLow.setObjects(*((_C,_L),(_C,_S),(_C,_u),(_C,_T)))
if mibBuilder.loadTexts:wsIbosTempLow.setStatus(_A)
wsIbosTempHigh=NotificationType((1,3,6,1,4,1,9303,4,1,2,0,2))
wsIbosTempHigh.setObjects(*((_C,_L),(_C,_S),(_C,_v),(_C,_T)))
if mibBuilder.loadTexts:wsIbosTempHigh.setStatus(_A)
wsIbosVoltLow=NotificationType((1,3,6,1,4,1,9303,4,1,2,0,3))
wsIbosVoltLow.setObjects(*((_C,_M),(_C,_U),(_C,_w),(_C,_V)))
if mibBuilder.loadTexts:wsIbosVoltLow.setStatus(_A)
wsIbosVoltHigh=NotificationType((1,3,6,1,4,1,9303,4,1,2,0,4))
wsIbosVoltHigh.setObjects(*((_C,_M),(_C,_U),(_C,_x),(_C,_V)))
if mibBuilder.loadTexts:wsIbosVoltHigh.setStatus(_A)
wsIbosFanRPMLow=NotificationType((1,3,6,1,4,1,9303,4,1,2,0,5))
wsIbosFanRPMLow.setObjects(*((_C,_Q),(_C,_y)))
if mibBuilder.loadTexts:wsIbosFanRPMLow.setStatus(_A)
wsIbosFanOutVoltLow=NotificationType((1,3,6,1,4,1,9303,4,1,2,0,6))
wsIbosFanOutVoltLow.setObjects((_C,_z))
if mibBuilder.loadTexts:wsIbosFanOutVoltLow.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ibos':ibos,'wsSystem':wsSystem,'wsWritedummy':wsWritedummy,'wsReload':wsReload,'wsVersion':wsVersion,'wsAsrRevision':wsAsrRevision,'wsVersionString':wsVersionString,'wsEnvironment':wsEnvironment,'wsIbosEnvironmentNotifications':wsIbosEnvironmentNotifications,'wsIbosTempLow':wsIbosTempLow,'wsIbosTempHigh':wsIbosTempHigh,'wsIbosVoltLow':wsIbosVoltLow,'wsIbosVoltHigh':wsIbosVoltHigh,'wsIbosFanRPMLow':wsIbosFanRPMLow,'wsIbosFanOutVoltLow':wsIbosFanOutVoltLow,'wsTempTable':wsTempTable,'wsTempEntry':wsTempEntry,_L:wsTempSensor,_S:wsTempMeasured,'wsTempTOS':wsTempTOS,'wsTempTHYST':wsTempTHYST,_u:wsTempThresholdLow,_v:wsTempThresholdHigh,_T:wsTempStatus,'wsVoltTable':wsVoltTable,'wsVoltEntry':wsVoltEntry,_M:wsVoltChannel,'wsVoltNominal':wsVoltNominal,_U:wsVoltMeasured,_w:wsVoltThresholdLow,_x:wsVoltThresholdHigh,_V:wsVoltStatus,'wsFanTable':wsFanTable,'wsFanEntry':wsFanEntry,_Q:wsFanNumber,_y:wsFanRPM,_z:wsFanVoltage,'wsIbosEnvironmentTrapEnable':wsIbosEnvironmentTrapEnable,'wsPFDP':wsPFDP,'wsNeighboursTable':wsNeighboursTable,'wsNeighboursEntry':wsNeighboursEntry,_X:wsNeighbourIfIndex,_Y:wsNeighbourNIndex,'wsNeighbourHostname':wsNeighbourHostname,'wsNeighbourLocalIf':wsNeighbourLocalIf,'wsNeighbourRemoteIf':wsNeighbourRemoteIf,'wsNeighbourModel':wsNeighbourModel,'wsNeighbourLastAct':wsNeighbourLastAct,'wsNeighbourOSVersion':wsNeighbourOSVersion,'wsNeighbourSNPA':wsNeighbourSNPA,'wsNeighbourUptime':wsNeighbourUptime,'wsNeighbourState':wsNeighbourState,'wsNeighbourDBCount':wsNeighbourDBCount,'wsNeighbourCreated':wsNeighbourCreated,'wsNeighbourPacketsIn':wsNeighbourPacketsIn,'wsNeighbourPacketErrorsrIn':wsNeighbourPacketErrorsrIn,'wsNeighbourPortsTable':wsNeighbourPortsTable,'wsNeighbourPortsEntry':wsNeighbourPortsEntry,_Z:wsNeighbourPortIfIndex,_a:wsNeighbourPortNIndex,_b:wsNeighbourPortPIndex,'wsNeighbourPortName':wsNeighbourPortName,'wsNeighbourPortState':wsNeighbourPortState,'wsNeighbourPortTxOctets':wsNeighbourPortTxOctets,'wsNeighbourPortTxDropPkts':wsNeighbourPortTxDropPkts,'wsNeighbourPortTxBroadcastPkts':wsNeighbourPortTxBroadcastPkts,'wsNeighbourPortTxMulticastPkts':wsNeighbourPortTxMulticastPkts,'wsNeighbourPortTxUnicastPkts':wsNeighbourPortTxUnicastPkts,'wsNeighbourPortTxCollisions':wsNeighbourPortTxCollisions,'wsNeighbourPortTxDeferredTransmit':wsNeighbourPortTxDeferredTransmit,'wsNeighbourPortTxFrameInDisc':wsNeighbourPortTxFrameInDisc,'wsNeighbourPortRxOctets':wsNeighbourPortRxOctets,'wsNeighbourPortRxUndersizePkts':wsNeighbourPortRxUndersizePkts,'wsNeighbourPortPkts64Octets':wsNeighbourPortPkts64Octets,'wsNeighbourPortPkts65to127Octets':wsNeighbourPortPkts65to127Octets,'wsNeighbourPortPkts128to255Octets':wsNeighbourPortPkts128to255Octets,'wsNeighbourPortPkts256to511Octets':wsNeighbourPortPkts256to511Octets,'wsNeighbourPortPkts512to1023Octets':wsNeighbourPortPkts512to1023Octets,'wsNeighbourPortPkts1024to1522Octets':wsNeighbourPortPkts1024to1522Octets,'wsNeighbourPortRxOversizePkts':wsNeighbourPortRxOversizePkts,'wsNeighbourPortRxJabbers':wsNeighbourPortRxJabbers,'wsNeighbourPortRxAlignmentErrors':wsNeighbourPortRxAlignmentErrors,'wsNeighbourPortRxFCSErrors':wsNeighbourPortRxFCSErrors,'wsNeighbourPortRxGoodOctets':wsNeighbourPortRxGoodOctets,'wsNeighbourPortRxDropPkts':wsNeighbourPortRxDropPkts,'wsNeighbourPortRxUnicastPkts':wsNeighbourPortRxUnicastPkts,'wsNeighbourPortRxMulticastPkts':wsNeighbourPortRxMulticastPkts,'wsNeighbourPortRxBroadcastPkts':wsNeighbourPortRxBroadcastPkts,'wsNeighbourPortRxFragments':wsNeighbourPortRxFragments,'wsNeighbourPortRxExcessSizeDisc':wsNeighbourPortRxExcessSizeDisc,'wsNeighbourPortRxSymbolError':wsNeighbourPortRxSymbolError,'wsNeighbourPortSNPATable':wsNeighbourPortSNPATable,'wsNeighbourPortSNPAEntry':wsNeighbourPortSNPAEntry,_e:wsNeighbourPortSNPAIfIndex,_f:wsNeighbourPortSNPANIndex,_g:wsNeighbourPortSNPAPIndex,_h:wsNeighbourPortSNPASIndex,'wsNeighbourPortSNPASMCast':wsNeighbourPortSNPASMCast,'wsNeighbourPortSNPA':wsNeighbourPortSNPA,'wsSFPTable':wsSFPTable,'wsSFPEntry':wsSFPEntry,_i:wsSFPIndex,'wsSFPStatus':wsSFPStatus,'wsSFPConnector':wsSFPConnector,'wsSFPTransceiver':wsSFPTransceiver,'wsSFPEncoding':wsSFPEncoding,'wsSFPBitrate':wsSFPBitrate,'wsSFPSingleModeLen':wsSFPSingleModeLen,'wsSFPMultiMode50Len':wsSFPMultiMode50Len,'wsSFPMultiMode625Len':wsSFPMultiMode625Len,'wsSFPCopperLen':wsSFPCopperLen,'wsSFPTempStatus':wsSFPTempStatus,'wsSFPTemp':wsSFPTemp,'wsSFPVoltStatus':wsSFPVoltStatus,'wsSFPVolt':wsSFPVolt,'wsSFPTXCurrentStatus':wsSFPTXCurrentStatus,'wsSFPTXCurrent':wsSFPTXCurrent,'wsSFPTXPowerStatus':wsSFPTXPowerStatus,'wsSFPTXPower':wsSFPTXPower,'wsSFPRXPowerStatus':wsSFPRXPowerStatus,'wsSFPRXPower':wsSFPRXPower,'wsSFPTransceiverExt':wsSFPTransceiverExt,'wsSFPTXdBmPower':wsSFPTXdBmPower,'wsSFPRXdBmPower':wsSFPRXdBmPower,'wsSFPTempNormalLow':wsSFPTempNormalLow,'wsSFPTempNormalHigh':wsSFPTempNormalHigh,'wsSFPTempWarningLow':wsSFPTempWarningLow,'wsSFPTempWarningHigh':wsSFPTempWarningHigh,'wsSFPVoltNormalLow':wsSFPVoltNormalLow,'wsSFPVoltNormalHigh':wsSFPVoltNormalHigh,'wsSFPVoltWarningLow':wsSFPVoltWarningLow,'wsSFPVoltWarningHigh':wsSFPVoltWarningHigh,'wsSFPTXCurrentNormalLow':wsSFPTXCurrentNormalLow,'wsSFPTXCurrentNormalHigh':wsSFPTXCurrentNormalHigh,'wsSFPTXCurrentWarningLow':wsSFPTXCurrentWarningLow,'wsSFPTXCurrentWarningHigh':wsSFPTXCurrentWarningHigh,'wsSFPTXOutputPowNormalLowuW':wsSFPTXOutputPowNormalLowuW,'wsSFPTXOutputPowNormalHighuW':wsSFPTXOutputPowNormalHighuW,'wsSFPTXOutputPowWarningLowuW':wsSFPTXOutputPowWarningLowuW,'wsSFPTXOutputPowWarningHighuW':wsSFPTXOutputPowWarningHighuW,'wsSFPTXOutputPowNormalLowdBm':wsSFPTXOutputPowNormalLowdBm,'wsSFPTXOutputPowNormalHighdBm':wsSFPTXOutputPowNormalHighdBm,'wsSFPTXOutputPowWarningLowdBm':wsSFPTXOutputPowWarningLowdBm,'wsSFPTXOutputPowWarningHighdBm':wsSFPTXOutputPowWarningHighdBm,'wsSFPRXInputPowNormalLowuW':wsSFPRXInputPowNormalLowuW,'wsSFPRXInputPowNormalHighuW':wsSFPRXInputPowNormalHighuW,'wsSFPRXInputPowWarningLowuW':wsSFPRXInputPowWarningLowuW,'wsSFPRXInputPowWarningHighuW':wsSFPRXInputPowWarningHighuW,'wsSFPRXInputPowNormalLowdBm':wsSFPRXInputPowNormalLowdBm,'wsSFPRXInputPowNormalHighdBm':wsSFPRXInputPowNormalHighdBm,'wsSFPRXInputPowWarningLowdBm':wsSFPRXInputPowWarningLowdBm,'wsSFPRXInputPowWarningHighdBm':wsSFPRXInputPowWarningHighdBm,'wsSFPPartNumber':wsSFPPartNumber,'wsSFPSerialNumber':wsSFPSerialNumber,'wsAccounting':wsAccounting,'wsPolicyTable':wsPolicyTable,'wsPolicyEntry':wsPolicyEntry,_q:wsPolicyIfIndex,'wsPolicyIfName':wsPolicyIfName,_r:wsPolicyName,'wsPolicyCookie':wsPolicyCookie,'wsPolicyInPkts':wsPolicyInPkts,'wsPolicyInBytes':wsPolicyInBytes,'wsPolicyInDrops':wsPolicyInDrops,'wsPolicyOutPkts':wsPolicyOutPkts,'wsPolicyOutBytes':wsPolicyOutBytes,'wsPolicyOutDrops':wsPolicyOutDrops,'wsPolicyUsedCnt':wsPolicyUsedCnt,'wsXFPTable':wsXFPTable,'wsXFPEntry':wsXFPEntry,_s:wsXFPIndex,'wsXFPStatus':wsXFPStatus,'wsXFPConnector':wsXFPConnector,'wsXFPTransceiver':wsXFPTransceiver,'wsXFPEncoding':wsXFPEncoding,'wsXFPBitrateMin':wsXFPBitrateMin,'wsXFPBitrateMax':wsXFPBitrateMax,'wsXFPSingleModeLen':wsXFPSingleModeLen,'wsXFPMultiMode50Len':wsXFPMultiMode50Len,'wsXFPMultiMode625Len':wsXFPMultiMode625Len,'wsXFPCopperLen':wsXFPCopperLen,'wsXFPTempStatus':wsXFPTempStatus,'wsXFPTemp':wsXFPTemp,'wsXFPTXCurrentStatus':wsXFPTXCurrentStatus,'wsXFPTXCurrent':wsXFPTXCurrent,'wsXFPTXPowerStatus':wsXFPTXPowerStatus,'wsXFPTXPower':wsXFPTXPower,'wsXFPRXPowerStatus':wsXFPRXPowerStatus,'wsXFPRXPower':wsXFPRXPower,'wsIfXTable':wsIfXTable,_t:wsIfXEntry,'ifHCInErrors':ifHCInErrors,'ifHCInRunts':ifHCInRunts,'ifHCInOversized':ifHCInOversized,'ifHCInCRCErrors':ifHCInCRCErrors,'ifHCInJabbers':ifHCInJabbers,'ifHCInFragments':ifHCInFragments,'ifHCInSymbolErrors':ifHCInSymbolErrors,'ifHCInAlignmentErrors':ifHCInAlignmentErrors,'ifHCOutErrors':ifHCOutErrors,'ifHCOutCollisions':ifHCOutCollisions,'ifHCOutDeferred':ifHCOutDeferred})