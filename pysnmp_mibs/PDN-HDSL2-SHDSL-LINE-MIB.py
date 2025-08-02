_Aa='pdnHdsl2ShdslNotificationGroup'
_AZ='pdnHdsl2ShdslExtendedRateModeGroup'
_AY='pdnHdsl2ShdslIfTableGroup'
_AX='pdnHdsl2ShdslSpanConfProfileGroup'
_AW='pdnHdsl2Shdsl1DayIntervalGroup'
_AV='pdnHdsl2Shdsl15MinIntervalGroup'
_AU='pdnHdsl2ShdslEndpointCurrGroup'
_AT='pdnHdsl2ShdslEndpointConfGroup'
_AS='pdnHdsl2ShdslSpanShdslStatusGroup'
_AR='pdnHdsl2ShdslnoNeighborPresent'
_AQ='pdnHdsl2ShdslprotocolInitFailure'
_AP='pdnHdsl2ShdslconfigInitFailure'
_AO='pdnHdsl2ShdsldcContinuityFault'
_AN='pdnHdsl2ShdsldeviceFault'
_AM='pdnHdsl2ShdslpowerBackoff'
_AL='pdnHdsl2ShdslPerfUASThresh'
_AK='pdnHdsl2ShdslPerfLOSWSThresh'
_AJ='pdnHdsl2ShdslPerfCRCanomaliesThresh'
_AI='pdnHdsl2ShdslPerfSESThresh'
_AH='pdnHdsl2ShdslPerfESThresh'
_AG='pdnHdsl2ShdslSNRMarginCrossing'
_AF='pdnHdsl2ShdslLoopAttenCrossing'
_AE='pdnHdsl2ShdslExtendedRateMode'
_AD='pdnHdsl2ShdslIfTableEquipMode'
_AC='pdnHdsl2ShdslSpanConfMaxLineRate'
_AB='pdnHdsl2ShdslSpanConfMinLineRate'
_AA='pdnHdsl2ShdslSpanConfWireInterface'
_A9='pdnHdsl2Shdsl1DayIntervalUAS'
_A8='pdnHdsl2Shdsl1DayIntervalLOSWS'
_A7='pdnHdsl2Shdsl1DayIntervalCRCanomalies'
_A6='pdnHdsl2Shdsl1DayIntervalSES'
_A5='pdnHdsl2Shdsl1DayIntervalES'
_A4='pdnHdsl2Shdsl1DayIntervalMoniSecs'
_A3='pdnHdsl2Shdsl15MinIntervalUAS'
_A2='pdnHdsl2Shdsl15MinIntervalLOSWS'
_A1='pdnHdsl2Shdsl15MinIntervalCRCanomalies'
_A0='pdnHdsl2Shdsl15MinIntervalSES'
_z='pdnHdsl2Shdsl15MinIntervalES'
_y='pdnHdsl2ShdslEndpointCurr1DayUAS'
_x='pdnHdsl2ShdslEndpointCurr1DayLOSWS'
_w='pdnHdsl2ShdslEndpointCurr1DayCRCanomalies'
_v='pdnHdsl2ShdslEndpointCurr1DaySES'
_u='pdnHdsl2ShdslEndpointCurr1DayES'
_t='pdnHdsl2ShdslEndpointCurr1DayTimeElapsed'
_s='pdnHdsl2ShdslEndpointCurr15MinTimeElapsed'
_r='pdnHdsl2ShdslEndpointUAS'
_q='pdnHdsl2ShdslEndpointLOSWS'
_p='pdnHdsl2ShdslEndpointCRCanomalies'
_o='pdnHdsl2ShdslEndpointSES'
_n='pdnHdsl2ShdslEndpointES'
_m='pdnHdsl2ShdslEndpointAlarmConfProfile'
_l='pdnHdsl2ShdslStatusActualLineRate'
_k='pdnHdsl2ShdslStatusMaxAttainableLineRate'
_j='pdnHdsl2Shdsl1DayIntervalNumber'
_i='pdnHdsl2Shdsl15MinIntervalNumber'
_h='SnmpAdminString'
_g='hdsl2ShdslSpanConfProfileName'
_f='hdsl2ShdslEndpointThreshUAS'
_e='hdsl2ShdslEndpointThreshSNRMargin'
_d='hdsl2ShdslEndpointThreshSES'
_c='hdsl2ShdslEndpointThreshLoopAttenuation'
_b='hdsl2ShdslEndpointThreshLOSWS'
_a='hdsl2ShdslEndpointThreshES'
_Z='hdsl2ShdslEndpointThreshCRCanomalies'
_Y='pdnHdsl2ShdslEndpointCurr15MinUAS'
_X='pdnHdsl2ShdslEndpointCurr15MinLOSWS'
_W='pdnHdsl2ShdslEndpointCurr15MinCRCanomalies'
_V='pdnHdsl2ShdslEndpointCurr15MinSES'
_U='pdnHdsl2ShdslEndpointCurr15MinES'
_T='pdnHdsl2ShdslEndpointCurrSnrMgn'
_S='pdnHdsl2ShdslEndpointCurrAtn'
_R='read-create'
_Q='read-write'
_P='not-accessible'
_O='bps'
_N='detected CRC Anomalies'
_M='pdnHdsl2ShdslEndpointWirePair'
_L='Unsigned32'
_K='hdsl2ShdslInvIndex'
_J='hdsl2ShdslEndpointSide'
_I='Integer32'
_H='ifIndex'
_G='IF-MIB'
_F='pdnHdsl2ShdslEndpointCurrStatus'
_E='HDSL2-SHDSL-LINE-MIB'
_D='seconds'
_C='read-only'
_B='current'
_A='PDN-HDSL2-SHDSL-LINE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Hdsl2Shdsl1DayIntervalCount,Hdsl2ShdslPerfCurrDayCount,Hdsl2ShdslPerfTimeElapsed,hdsl2ShdslEndpointSide,hdsl2ShdslEndpointThreshCRCanomalies,hdsl2ShdslEndpointThreshES,hdsl2ShdslEndpointThreshLOSWS,hdsl2ShdslEndpointThreshLoopAttenuation,hdsl2ShdslEndpointThreshSES,hdsl2ShdslEndpointThreshSNRMargin,hdsl2ShdslEndpointThreshUAS,hdsl2ShdslInvIndex,hdsl2ShdslSpanConfProfileName=mibBuilder.importSymbols(_E,'Hdsl2Shdsl1DayIntervalCount','Hdsl2ShdslPerfCurrDayCount','Hdsl2ShdslPerfTimeElapsed',_J,_Z,_a,_b,_c,_d,_e,_f,_K,_g)
ifIndex,=mibBuilder.importSymbols(_G,_H)
pdn_interfaces,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-interfaces')
PerfCurrentCount,PerfIntervalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_h)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pdnHdsl2ShdslLineMIB=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,6,23))
if mibBuilder.loadTexts:pdnHdsl2ShdslLineMIB.setRevisions(('2005-01-28 00:00','2004-04-27 00:00','2004-04-21 00:00','2004-01-16 15:00','2003-11-06 15:00','2003-10-23 15:00'))
class PdnHdsl2ShdslWirePair(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('wirePair1',1),('wirePair2',2),('wirePair3',3),('wirePair4',4)))
_PdnHdsl2ShdslLineNotifications_ObjectIdentity=ObjectIdentity
pdnHdsl2ShdslLineNotifications=_PdnHdsl2ShdslLineNotifications_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,23,0))
_PdnHdsl2ShdslLineObjects_ObjectIdentity=ObjectIdentity
pdnHdsl2ShdslLineObjects=_PdnHdsl2ShdslLineObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,23,1))
_PdnHdsl2ShdslSpanStatusExtTable_Object=MibTable
pdnHdsl2ShdslSpanStatusExtTable=_PdnHdsl2ShdslSpanStatusExtTable_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,1))
if mibBuilder.loadTexts:pdnHdsl2ShdslSpanStatusExtTable.setStatus(_B)
_PdnHdsl2ShdslSpanStatusExtEntry_Object=MibTableRow
pdnHdsl2ShdslSpanStatusExtEntry=_PdnHdsl2ShdslSpanStatusExtEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,1,1))
pdnHdsl2ShdslSpanStatusExtEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:pdnHdsl2ShdslSpanStatusExtEntry.setStatus(_B)
_PdnHdsl2ShdslStatusMaxAttainableLineRate_Type=Unsigned32
_PdnHdsl2ShdslStatusMaxAttainableLineRate_Object=MibTableColumn
pdnHdsl2ShdslStatusMaxAttainableLineRate=_PdnHdsl2ShdslStatusMaxAttainableLineRate_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,1,1,1),_PdnHdsl2ShdslStatusMaxAttainableLineRate_Type())
pdnHdsl2ShdslStatusMaxAttainableLineRate.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2ShdslStatusMaxAttainableLineRate.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2ShdslStatusMaxAttainableLineRate.setUnits(_O)
_PdnHdsl2ShdslStatusActualLineRate_Type=Unsigned32
_PdnHdsl2ShdslStatusActualLineRate_Object=MibTableColumn
pdnHdsl2ShdslStatusActualLineRate=_PdnHdsl2ShdslStatusActualLineRate_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,1,1,2),_PdnHdsl2ShdslStatusActualLineRate_Type())
pdnHdsl2ShdslStatusActualLineRate.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2ShdslStatusActualLineRate.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2ShdslStatusActualLineRate.setUnits(_O)
_PdnHdsl2ShdslEndpointConfTable_Object=MibTable
pdnHdsl2ShdslEndpointConfTable=_PdnHdsl2ShdslEndpointConfTable_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,2))
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointConfTable.setStatus(_B)
_PdnHdsl2ShdslEndpointConfEntry_Object=MibTableRow
pdnHdsl2ShdslEndpointConfEntry=_PdnHdsl2ShdslEndpointConfEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,2,1))
pdnHdsl2ShdslEndpointConfEntry.setIndexNames((0,_G,_H),(0,_E,_K),(0,_E,_J),(0,_A,_M))
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointConfEntry.setStatus(_B)
_PdnHdsl2ShdslEndpointWirePair_Type=PdnHdsl2ShdslWirePair
_PdnHdsl2ShdslEndpointWirePair_Object=MibTableColumn
pdnHdsl2ShdslEndpointWirePair=_PdnHdsl2ShdslEndpointWirePair_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,2,1,1),_PdnHdsl2ShdslEndpointWirePair_Type())
pdnHdsl2ShdslEndpointWirePair.setMaxAccess(_P)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointWirePair.setStatus(_B)
class _PdnHdsl2ShdslEndpointAlarmConfProfile_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PdnHdsl2ShdslEndpointAlarmConfProfile_Type.__name__=_h
_PdnHdsl2ShdslEndpointAlarmConfProfile_Object=MibTableColumn
pdnHdsl2ShdslEndpointAlarmConfProfile=_PdnHdsl2ShdslEndpointAlarmConfProfile_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,2,1,2),_PdnHdsl2ShdslEndpointAlarmConfProfile_Type())
pdnHdsl2ShdslEndpointAlarmConfProfile.setMaxAccess(_Q)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointAlarmConfProfile.setStatus(_B)
_PdnHdsl2ShdslEndpointCurrTable_Object=MibTable
pdnHdsl2ShdslEndpointCurrTable=_PdnHdsl2ShdslEndpointCurrTable_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,3))
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurrTable.setStatus(_B)
_PdnHdsl2ShdslEndpointCurrEntry_Object=MibTableRow
pdnHdsl2ShdslEndpointCurrEntry=_PdnHdsl2ShdslEndpointCurrEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,3,1))
pdnHdsl2ShdslEndpointCurrEntry.setIndexNames((0,_G,_H),(0,_E,_K),(0,_E,_J),(0,_A,_M))
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurrEntry.setStatus(_B)
class _PdnHdsl2ShdslEndpointCurrAtn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-127,128))
_PdnHdsl2ShdslEndpointCurrAtn_Type.__name__=_I
_PdnHdsl2ShdslEndpointCurrAtn_Object=MibTableColumn
pdnHdsl2ShdslEndpointCurrAtn=_PdnHdsl2ShdslEndpointCurrAtn_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,3,1,1),_PdnHdsl2ShdslEndpointCurrAtn_Type())
pdnHdsl2ShdslEndpointCurrAtn.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurrAtn.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurrAtn.setUnits('dB')
class _PdnHdsl2ShdslEndpointCurrSnrMgn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-127,128))
_PdnHdsl2ShdslEndpointCurrSnrMgn_Type.__name__=_I
_PdnHdsl2ShdslEndpointCurrSnrMgn_Object=MibTableColumn
pdnHdsl2ShdslEndpointCurrSnrMgn=_PdnHdsl2ShdslEndpointCurrSnrMgn_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,3,1,2),_PdnHdsl2ShdslEndpointCurrSnrMgn_Type())
pdnHdsl2ShdslEndpointCurrSnrMgn.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurrSnrMgn.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurrSnrMgn.setUnits('dB')
class _PdnHdsl2ShdslEndpointCurrStatus_Type(Bits):namedValues=NamedValues(*(('noDefect',0),('powerBackoff',1),('deviceFault',2),('dcContinuityFault',3),('snrMarginAlarm',4),('loopAttenuationAlarm',5),('loswFailureAlarm',6),('configInitFailure',7),('protocolInitFailure',8),('noNeighborPresent',9),('loopbackActive',10)))
_PdnHdsl2ShdslEndpointCurrStatus_Type.__name__='Bits'
_PdnHdsl2ShdslEndpointCurrStatus_Object=MibTableColumn
pdnHdsl2ShdslEndpointCurrStatus=_PdnHdsl2ShdslEndpointCurrStatus_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,3,1,3),_PdnHdsl2ShdslEndpointCurrStatus_Type())
pdnHdsl2ShdslEndpointCurrStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurrStatus.setStatus(_B)
_PdnHdsl2ShdslEndpointES_Type=Counter32
_PdnHdsl2ShdslEndpointES_Object=MibTableColumn
pdnHdsl2ShdslEndpointES=_PdnHdsl2ShdslEndpointES_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,3,1,4),_PdnHdsl2ShdslEndpointES_Type())
pdnHdsl2ShdslEndpointES.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointES.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointES.setUnits(_D)
_PdnHdsl2ShdslEndpointSES_Type=Counter32
_PdnHdsl2ShdslEndpointSES_Object=MibTableColumn
pdnHdsl2ShdslEndpointSES=_PdnHdsl2ShdslEndpointSES_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,3,1,5),_PdnHdsl2ShdslEndpointSES_Type())
pdnHdsl2ShdslEndpointSES.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointSES.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointSES.setUnits(_D)
_PdnHdsl2ShdslEndpointCRCanomalies_Type=Counter32
_PdnHdsl2ShdslEndpointCRCanomalies_Object=MibTableColumn
pdnHdsl2ShdslEndpointCRCanomalies=_PdnHdsl2ShdslEndpointCRCanomalies_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,3,1,6),_PdnHdsl2ShdslEndpointCRCanomalies_Type())
pdnHdsl2ShdslEndpointCRCanomalies.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCRCanomalies.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCRCanomalies.setUnits(_N)
_PdnHdsl2ShdslEndpointLOSWS_Type=Counter32
_PdnHdsl2ShdslEndpointLOSWS_Object=MibTableColumn
pdnHdsl2ShdslEndpointLOSWS=_PdnHdsl2ShdslEndpointLOSWS_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,3,1,7),_PdnHdsl2ShdslEndpointLOSWS_Type())
pdnHdsl2ShdslEndpointLOSWS.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointLOSWS.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointLOSWS.setUnits(_D)
_PdnHdsl2ShdslEndpointUAS_Type=Counter32
_PdnHdsl2ShdslEndpointUAS_Object=MibTableColumn
pdnHdsl2ShdslEndpointUAS=_PdnHdsl2ShdslEndpointUAS_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,3,1,8),_PdnHdsl2ShdslEndpointUAS_Type())
pdnHdsl2ShdslEndpointUAS.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointUAS.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointUAS.setUnits(_D)
_PdnHdsl2ShdslEndpointCurr15MinTimeElapsed_Type=Hdsl2ShdslPerfTimeElapsed
_PdnHdsl2ShdslEndpointCurr15MinTimeElapsed_Object=MibTableColumn
pdnHdsl2ShdslEndpointCurr15MinTimeElapsed=_PdnHdsl2ShdslEndpointCurr15MinTimeElapsed_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,3,1,9),_PdnHdsl2ShdslEndpointCurr15MinTimeElapsed_Type())
pdnHdsl2ShdslEndpointCurr15MinTimeElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurr15MinTimeElapsed.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurr15MinTimeElapsed.setUnits(_D)
_PdnHdsl2ShdslEndpointCurr15MinES_Type=PerfCurrentCount
_PdnHdsl2ShdslEndpointCurr15MinES_Object=MibTableColumn
pdnHdsl2ShdslEndpointCurr15MinES=_PdnHdsl2ShdslEndpointCurr15MinES_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,3,1,10),_PdnHdsl2ShdslEndpointCurr15MinES_Type())
pdnHdsl2ShdslEndpointCurr15MinES.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurr15MinES.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurr15MinES.setUnits(_D)
_PdnHdsl2ShdslEndpointCurr15MinSES_Type=PerfCurrentCount
_PdnHdsl2ShdslEndpointCurr15MinSES_Object=MibTableColumn
pdnHdsl2ShdslEndpointCurr15MinSES=_PdnHdsl2ShdslEndpointCurr15MinSES_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,3,1,11),_PdnHdsl2ShdslEndpointCurr15MinSES_Type())
pdnHdsl2ShdslEndpointCurr15MinSES.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurr15MinSES.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurr15MinSES.setUnits(_D)
_PdnHdsl2ShdslEndpointCurr15MinCRCanomalies_Type=PerfCurrentCount
_PdnHdsl2ShdslEndpointCurr15MinCRCanomalies_Object=MibTableColumn
pdnHdsl2ShdslEndpointCurr15MinCRCanomalies=_PdnHdsl2ShdslEndpointCurr15MinCRCanomalies_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,3,1,12),_PdnHdsl2ShdslEndpointCurr15MinCRCanomalies_Type())
pdnHdsl2ShdslEndpointCurr15MinCRCanomalies.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurr15MinCRCanomalies.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurr15MinCRCanomalies.setUnits(_N)
_PdnHdsl2ShdslEndpointCurr15MinLOSWS_Type=PerfCurrentCount
_PdnHdsl2ShdslEndpointCurr15MinLOSWS_Object=MibTableColumn
pdnHdsl2ShdslEndpointCurr15MinLOSWS=_PdnHdsl2ShdslEndpointCurr15MinLOSWS_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,3,1,13),_PdnHdsl2ShdslEndpointCurr15MinLOSWS_Type())
pdnHdsl2ShdslEndpointCurr15MinLOSWS.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurr15MinLOSWS.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurr15MinLOSWS.setUnits(_D)
_PdnHdsl2ShdslEndpointCurr15MinUAS_Type=PerfCurrentCount
_PdnHdsl2ShdslEndpointCurr15MinUAS_Object=MibTableColumn
pdnHdsl2ShdslEndpointCurr15MinUAS=_PdnHdsl2ShdslEndpointCurr15MinUAS_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,3,1,14),_PdnHdsl2ShdslEndpointCurr15MinUAS_Type())
pdnHdsl2ShdslEndpointCurr15MinUAS.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurr15MinUAS.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurr15MinUAS.setUnits(_D)
_PdnHdsl2ShdslEndpointCurr1DayTimeElapsed_Type=Hdsl2ShdslPerfTimeElapsed
_PdnHdsl2ShdslEndpointCurr1DayTimeElapsed_Object=MibTableColumn
pdnHdsl2ShdslEndpointCurr1DayTimeElapsed=_PdnHdsl2ShdslEndpointCurr1DayTimeElapsed_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,3,1,15),_PdnHdsl2ShdslEndpointCurr1DayTimeElapsed_Type())
pdnHdsl2ShdslEndpointCurr1DayTimeElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurr1DayTimeElapsed.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurr1DayTimeElapsed.setUnits(_D)
_PdnHdsl2ShdslEndpointCurr1DayES_Type=Hdsl2ShdslPerfCurrDayCount
_PdnHdsl2ShdslEndpointCurr1DayES_Object=MibTableColumn
pdnHdsl2ShdslEndpointCurr1DayES=_PdnHdsl2ShdslEndpointCurr1DayES_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,3,1,16),_PdnHdsl2ShdslEndpointCurr1DayES_Type())
pdnHdsl2ShdslEndpointCurr1DayES.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurr1DayES.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurr1DayES.setUnits(_D)
_PdnHdsl2ShdslEndpointCurr1DaySES_Type=Hdsl2ShdslPerfCurrDayCount
_PdnHdsl2ShdslEndpointCurr1DaySES_Object=MibTableColumn
pdnHdsl2ShdslEndpointCurr1DaySES=_PdnHdsl2ShdslEndpointCurr1DaySES_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,3,1,17),_PdnHdsl2ShdslEndpointCurr1DaySES_Type())
pdnHdsl2ShdslEndpointCurr1DaySES.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurr1DaySES.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurr1DaySES.setUnits(_D)
_PdnHdsl2ShdslEndpointCurr1DayCRCanomalies_Type=Hdsl2ShdslPerfCurrDayCount
_PdnHdsl2ShdslEndpointCurr1DayCRCanomalies_Object=MibTableColumn
pdnHdsl2ShdslEndpointCurr1DayCRCanomalies=_PdnHdsl2ShdslEndpointCurr1DayCRCanomalies_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,3,1,18),_PdnHdsl2ShdslEndpointCurr1DayCRCanomalies_Type())
pdnHdsl2ShdslEndpointCurr1DayCRCanomalies.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurr1DayCRCanomalies.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurr1DayCRCanomalies.setUnits(_N)
_PdnHdsl2ShdslEndpointCurr1DayLOSWS_Type=Hdsl2ShdslPerfCurrDayCount
_PdnHdsl2ShdslEndpointCurr1DayLOSWS_Object=MibTableColumn
pdnHdsl2ShdslEndpointCurr1DayLOSWS=_PdnHdsl2ShdslEndpointCurr1DayLOSWS_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,3,1,19),_PdnHdsl2ShdslEndpointCurr1DayLOSWS_Type())
pdnHdsl2ShdslEndpointCurr1DayLOSWS.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurr1DayLOSWS.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurr1DayLOSWS.setUnits(_D)
_PdnHdsl2ShdslEndpointCurr1DayUAS_Type=Hdsl2ShdslPerfCurrDayCount
_PdnHdsl2ShdslEndpointCurr1DayUAS_Object=MibTableColumn
pdnHdsl2ShdslEndpointCurr1DayUAS=_PdnHdsl2ShdslEndpointCurr1DayUAS_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,3,1,20),_PdnHdsl2ShdslEndpointCurr1DayUAS_Type())
pdnHdsl2ShdslEndpointCurr1DayUAS.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurr1DayUAS.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurr1DayUAS.setUnits(_D)
_PdnHdsl2Shdsl15MinIntervalTable_Object=MibTable
pdnHdsl2Shdsl15MinIntervalTable=_PdnHdsl2Shdsl15MinIntervalTable_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,4))
if mibBuilder.loadTexts:pdnHdsl2Shdsl15MinIntervalTable.setStatus(_B)
_PdnHdsl2Shdsl15MinIntervalEntry_Object=MibTableRow
pdnHdsl2Shdsl15MinIntervalEntry=_PdnHdsl2Shdsl15MinIntervalEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,4,1))
pdnHdsl2Shdsl15MinIntervalEntry.setIndexNames((0,_G,_H),(0,_E,_K),(0,_E,_J),(0,_A,_M),(0,_A,_i))
if mibBuilder.loadTexts:pdnHdsl2Shdsl15MinIntervalEntry.setStatus(_B)
class _PdnHdsl2Shdsl15MinIntervalNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_PdnHdsl2Shdsl15MinIntervalNumber_Type.__name__=_L
_PdnHdsl2Shdsl15MinIntervalNumber_Object=MibTableColumn
pdnHdsl2Shdsl15MinIntervalNumber=_PdnHdsl2Shdsl15MinIntervalNumber_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,4,1,1),_PdnHdsl2Shdsl15MinIntervalNumber_Type())
pdnHdsl2Shdsl15MinIntervalNumber.setMaxAccess(_P)
if mibBuilder.loadTexts:pdnHdsl2Shdsl15MinIntervalNumber.setStatus(_B)
_PdnHdsl2Shdsl15MinIntervalES_Type=PerfIntervalCount
_PdnHdsl2Shdsl15MinIntervalES_Object=MibTableColumn
pdnHdsl2Shdsl15MinIntervalES=_PdnHdsl2Shdsl15MinIntervalES_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,4,1,2),_PdnHdsl2Shdsl15MinIntervalES_Type())
pdnHdsl2Shdsl15MinIntervalES.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2Shdsl15MinIntervalES.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2Shdsl15MinIntervalES.setUnits(_D)
_PdnHdsl2Shdsl15MinIntervalSES_Type=PerfIntervalCount
_PdnHdsl2Shdsl15MinIntervalSES_Object=MibTableColumn
pdnHdsl2Shdsl15MinIntervalSES=_PdnHdsl2Shdsl15MinIntervalSES_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,4,1,3),_PdnHdsl2Shdsl15MinIntervalSES_Type())
pdnHdsl2Shdsl15MinIntervalSES.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2Shdsl15MinIntervalSES.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2Shdsl15MinIntervalSES.setUnits(_D)
_PdnHdsl2Shdsl15MinIntervalCRCanomalies_Type=PerfIntervalCount
_PdnHdsl2Shdsl15MinIntervalCRCanomalies_Object=MibTableColumn
pdnHdsl2Shdsl15MinIntervalCRCanomalies=_PdnHdsl2Shdsl15MinIntervalCRCanomalies_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,4,1,4),_PdnHdsl2Shdsl15MinIntervalCRCanomalies_Type())
pdnHdsl2Shdsl15MinIntervalCRCanomalies.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2Shdsl15MinIntervalCRCanomalies.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2Shdsl15MinIntervalCRCanomalies.setUnits(_N)
_PdnHdsl2Shdsl15MinIntervalLOSWS_Type=PerfIntervalCount
_PdnHdsl2Shdsl15MinIntervalLOSWS_Object=MibTableColumn
pdnHdsl2Shdsl15MinIntervalLOSWS=_PdnHdsl2Shdsl15MinIntervalLOSWS_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,4,1,5),_PdnHdsl2Shdsl15MinIntervalLOSWS_Type())
pdnHdsl2Shdsl15MinIntervalLOSWS.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2Shdsl15MinIntervalLOSWS.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2Shdsl15MinIntervalLOSWS.setUnits(_D)
_PdnHdsl2Shdsl15MinIntervalUAS_Type=PerfIntervalCount
_PdnHdsl2Shdsl15MinIntervalUAS_Object=MibTableColumn
pdnHdsl2Shdsl15MinIntervalUAS=_PdnHdsl2Shdsl15MinIntervalUAS_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,4,1,6),_PdnHdsl2Shdsl15MinIntervalUAS_Type())
pdnHdsl2Shdsl15MinIntervalUAS.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2Shdsl15MinIntervalUAS.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2Shdsl15MinIntervalUAS.setUnits(_D)
_PdnHdsl2Shdsl1DayIntervalTable_Object=MibTable
pdnHdsl2Shdsl1DayIntervalTable=_PdnHdsl2Shdsl1DayIntervalTable_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,5))
if mibBuilder.loadTexts:pdnHdsl2Shdsl1DayIntervalTable.setStatus(_B)
_PdnHdsl2Shdsl1DayIntervalEntry_Object=MibTableRow
pdnHdsl2Shdsl1DayIntervalEntry=_PdnHdsl2Shdsl1DayIntervalEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,5,1))
pdnHdsl2Shdsl1DayIntervalEntry.setIndexNames((0,_G,_H),(0,_E,_K),(0,_E,_J),(0,_A,_M),(0,_A,_j))
if mibBuilder.loadTexts:pdnHdsl2Shdsl1DayIntervalEntry.setStatus(_B)
class _PdnHdsl2Shdsl1DayIntervalNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_PdnHdsl2Shdsl1DayIntervalNumber_Type.__name__=_L
_PdnHdsl2Shdsl1DayIntervalNumber_Object=MibTableColumn
pdnHdsl2Shdsl1DayIntervalNumber=_PdnHdsl2Shdsl1DayIntervalNumber_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,5,1,1),_PdnHdsl2Shdsl1DayIntervalNumber_Type())
pdnHdsl2Shdsl1DayIntervalNumber.setMaxAccess(_P)
if mibBuilder.loadTexts:pdnHdsl2Shdsl1DayIntervalNumber.setStatus(_B)
_PdnHdsl2Shdsl1DayIntervalMoniSecs_Type=Hdsl2ShdslPerfTimeElapsed
_PdnHdsl2Shdsl1DayIntervalMoniSecs_Object=MibTableColumn
pdnHdsl2Shdsl1DayIntervalMoniSecs=_PdnHdsl2Shdsl1DayIntervalMoniSecs_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,5,1,2),_PdnHdsl2Shdsl1DayIntervalMoniSecs_Type())
pdnHdsl2Shdsl1DayIntervalMoniSecs.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2Shdsl1DayIntervalMoniSecs.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2Shdsl1DayIntervalMoniSecs.setUnits(_D)
_PdnHdsl2Shdsl1DayIntervalES_Type=Hdsl2Shdsl1DayIntervalCount
_PdnHdsl2Shdsl1DayIntervalES_Object=MibTableColumn
pdnHdsl2Shdsl1DayIntervalES=_PdnHdsl2Shdsl1DayIntervalES_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,5,1,3),_PdnHdsl2Shdsl1DayIntervalES_Type())
pdnHdsl2Shdsl1DayIntervalES.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2Shdsl1DayIntervalES.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2Shdsl1DayIntervalES.setUnits(_D)
_PdnHdsl2Shdsl1DayIntervalSES_Type=Hdsl2Shdsl1DayIntervalCount
_PdnHdsl2Shdsl1DayIntervalSES_Object=MibTableColumn
pdnHdsl2Shdsl1DayIntervalSES=_PdnHdsl2Shdsl1DayIntervalSES_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,5,1,4),_PdnHdsl2Shdsl1DayIntervalSES_Type())
pdnHdsl2Shdsl1DayIntervalSES.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2Shdsl1DayIntervalSES.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2Shdsl1DayIntervalSES.setUnits(_D)
_PdnHdsl2Shdsl1DayIntervalCRCanomalies_Type=Hdsl2Shdsl1DayIntervalCount
_PdnHdsl2Shdsl1DayIntervalCRCanomalies_Object=MibTableColumn
pdnHdsl2Shdsl1DayIntervalCRCanomalies=_PdnHdsl2Shdsl1DayIntervalCRCanomalies_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,5,1,5),_PdnHdsl2Shdsl1DayIntervalCRCanomalies_Type())
pdnHdsl2Shdsl1DayIntervalCRCanomalies.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2Shdsl1DayIntervalCRCanomalies.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2Shdsl1DayIntervalCRCanomalies.setUnits(_N)
_PdnHdsl2Shdsl1DayIntervalLOSWS_Type=Hdsl2Shdsl1DayIntervalCount
_PdnHdsl2Shdsl1DayIntervalLOSWS_Object=MibTableColumn
pdnHdsl2Shdsl1DayIntervalLOSWS=_PdnHdsl2Shdsl1DayIntervalLOSWS_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,5,1,6),_PdnHdsl2Shdsl1DayIntervalLOSWS_Type())
pdnHdsl2Shdsl1DayIntervalLOSWS.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2Shdsl1DayIntervalLOSWS.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2Shdsl1DayIntervalLOSWS.setUnits(_D)
_PdnHdsl2Shdsl1DayIntervalUAS_Type=Hdsl2Shdsl1DayIntervalCount
_PdnHdsl2Shdsl1DayIntervalUAS_Object=MibTableColumn
pdnHdsl2Shdsl1DayIntervalUAS=_PdnHdsl2Shdsl1DayIntervalUAS_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,5,1,7),_PdnHdsl2Shdsl1DayIntervalUAS_Type())
pdnHdsl2Shdsl1DayIntervalUAS.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdsl2Shdsl1DayIntervalUAS.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2Shdsl1DayIntervalUAS.setUnits(_D)
_PdnHdsl2ShdslSpanConfProfileExtTable_Object=MibTable
pdnHdsl2ShdslSpanConfProfileExtTable=_PdnHdsl2ShdslSpanConfProfileExtTable_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,6))
if mibBuilder.loadTexts:pdnHdsl2ShdslSpanConfProfileExtTable.setStatus(_B)
_PdnHdsl2ShdslSpanConfProfileExtEntry_Object=MibTableRow
pdnHdsl2ShdslSpanConfProfileExtEntry=_PdnHdsl2ShdslSpanConfProfileExtEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,6,1))
pdnHdsl2ShdslSpanConfProfileExtEntry.setIndexNames((1,_E,_g))
if mibBuilder.loadTexts:pdnHdsl2ShdslSpanConfProfileExtEntry.setStatus(_B)
class _PdnHdsl2ShdslSpanConfWireInterface_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('twoWire',1),('fourWire',2),('sixWire',3),('eightWire',4)))
_PdnHdsl2ShdslSpanConfWireInterface_Type.__name__=_I
_PdnHdsl2ShdslSpanConfWireInterface_Object=MibTableColumn
pdnHdsl2ShdslSpanConfWireInterface=_PdnHdsl2ShdslSpanConfWireInterface_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,6,1,1),_PdnHdsl2ShdslSpanConfWireInterface_Type())
pdnHdsl2ShdslSpanConfWireInterface.setMaxAccess(_R)
if mibBuilder.loadTexts:pdnHdsl2ShdslSpanConfWireInterface.setStatus(_B)
class _PdnHdsl2ShdslSpanConfMinLineRate_Type(Unsigned32):defaultValue=155200
_PdnHdsl2ShdslSpanConfMinLineRate_Type.__name__=_L
_PdnHdsl2ShdslSpanConfMinLineRate_Object=MibTableColumn
pdnHdsl2ShdslSpanConfMinLineRate=_PdnHdsl2ShdslSpanConfMinLineRate_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,6,1,2),_PdnHdsl2ShdslSpanConfMinLineRate_Type())
pdnHdsl2ShdslSpanConfMinLineRate.setMaxAccess(_R)
if mibBuilder.loadTexts:pdnHdsl2ShdslSpanConfMinLineRate.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2ShdslSpanConfMinLineRate.setUnits(_O)
class _PdnHdsl2ShdslSpanConfMaxLineRate_Type(Unsigned32):defaultValue=155200
_PdnHdsl2ShdslSpanConfMaxLineRate_Type.__name__=_L
_PdnHdsl2ShdslSpanConfMaxLineRate_Object=MibTableColumn
pdnHdsl2ShdslSpanConfMaxLineRate=_PdnHdsl2ShdslSpanConfMaxLineRate_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,6,1,3),_PdnHdsl2ShdslSpanConfMaxLineRate_Type())
pdnHdsl2ShdslSpanConfMaxLineRate.setMaxAccess(_R)
if mibBuilder.loadTexts:pdnHdsl2ShdslSpanConfMaxLineRate.setStatus(_B)
if mibBuilder.loadTexts:pdnHdsl2ShdslSpanConfMaxLineRate.setUnits(_O)
_PdnHdsl2ShdslIfTable_Object=MibTable
pdnHdsl2ShdslIfTable=_PdnHdsl2ShdslIfTable_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,7))
if mibBuilder.loadTexts:pdnHdsl2ShdslIfTable.setStatus(_B)
_PdnHdsl2ShdslIfEntry_Object=MibTableRow
pdnHdsl2ShdslIfEntry=_PdnHdsl2ShdslIfEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,7,1))
pdnHdsl2ShdslIfEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:pdnHdsl2ShdslIfEntry.setStatus(_B)
class _PdnHdsl2ShdslIfTableEquipMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('coMode',1),('cpeMode',2)))
_PdnHdsl2ShdslIfTableEquipMode_Type.__name__=_I
_PdnHdsl2ShdslIfTableEquipMode_Object=MibTableColumn
pdnHdsl2ShdslIfTableEquipMode=_PdnHdsl2ShdslIfTableEquipMode_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,7,1,1),_PdnHdsl2ShdslIfTableEquipMode_Type())
pdnHdsl2ShdslIfTableEquipMode.setMaxAccess(_Q)
if mibBuilder.loadTexts:pdnHdsl2ShdslIfTableEquipMode.setStatus(_B)
class _PdnHdsl2ShdslExtendedRateMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('payload5696',2)))
_PdnHdsl2ShdslExtendedRateMode_Type.__name__=_I
_PdnHdsl2ShdslExtendedRateMode_Object=MibScalar
pdnHdsl2ShdslExtendedRateMode=_PdnHdsl2ShdslExtendedRateMode_Object((1,3,6,1,4,1,1795,2,24,2,6,23,1,8),_PdnHdsl2ShdslExtendedRateMode_Type())
pdnHdsl2ShdslExtendedRateMode.setMaxAccess(_Q)
if mibBuilder.loadTexts:pdnHdsl2ShdslExtendedRateMode.setStatus(_B)
_PdnHdsl2ShdslLineAFNs_ObjectIdentity=ObjectIdentity
pdnHdsl2ShdslLineAFNs=_PdnHdsl2ShdslLineAFNs_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,23,2))
_PdnHdsl2ShdslLineConformance_ObjectIdentity=ObjectIdentity
pdnHdsl2ShdslLineConformance=_PdnHdsl2ShdslLineConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,23,3))
_PdnHdsl2ShdslLineCompliances_ObjectIdentity=ObjectIdentity
pdnHdsl2ShdslLineCompliances=_PdnHdsl2ShdslLineCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,23,3,1))
_PdnHdsl2ShdslLineGroups_ObjectIdentity=ObjectIdentity
pdnHdsl2ShdslLineGroups=_PdnHdsl2ShdslLineGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,23,3,2))
_PdnHdsl2ShdslLineObjGroups_ObjectIdentity=ObjectIdentity
pdnHdsl2ShdslLineObjGroups=_PdnHdsl2ShdslLineObjGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,23,3,2,1))
_PdnHdsl2ShdslLineAfnGroups_ObjectIdentity=ObjectIdentity
pdnHdsl2ShdslLineAfnGroups=_PdnHdsl2ShdslLineAfnGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,23,3,2,2))
_PdnHdsl2ShdslLineNtfyGroups_ObjectIdentity=ObjectIdentity
pdnHdsl2ShdslLineNtfyGroups=_PdnHdsl2ShdslLineNtfyGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,23,3,2,3))
pdnHdsl2ShdslSpanShdslStatusGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,23,3,2,1,1))
pdnHdsl2ShdslSpanShdslStatusGroup.setObjects(*((_A,_k),(_A,_l)))
if mibBuilder.loadTexts:pdnHdsl2ShdslSpanShdslStatusGroup.setStatus(_B)
pdnHdsl2ShdslEndpointConfGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,23,3,2,1,2))
pdnHdsl2ShdslEndpointConfGroup.setObjects((_A,_m))
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointConfGroup.setStatus(_B)
pdnHdsl2ShdslEndpointCurrGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,23,3,2,1,3))
pdnHdsl2ShdslEndpointCurrGroup.setObjects(*((_A,_S),(_A,_T),(_A,_F),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:pdnHdsl2ShdslEndpointCurrGroup.setStatus(_B)
pdnHdsl2Shdsl15MinIntervalGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,23,3,2,1,4))
pdnHdsl2Shdsl15MinIntervalGroup.setObjects(*((_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:pdnHdsl2Shdsl15MinIntervalGroup.setStatus(_B)
pdnHdsl2Shdsl1DayIntervalGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,23,3,2,1,5))
pdnHdsl2Shdsl1DayIntervalGroup.setObjects(*((_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:pdnHdsl2Shdsl1DayIntervalGroup.setStatus(_B)
pdnHdsl2ShdslSpanConfProfileGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,23,3,2,1,6))
pdnHdsl2ShdslSpanConfProfileGroup.setObjects(*((_A,_AA),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:pdnHdsl2ShdslSpanConfProfileGroup.setStatus(_B)
pdnHdsl2ShdslIfTableGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,23,3,2,1,7))
pdnHdsl2ShdslIfTableGroup.setObjects((_A,_AD))
if mibBuilder.loadTexts:pdnHdsl2ShdslIfTableGroup.setStatus(_B)
pdnHdsl2ShdslExtendedRateModeGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,23,3,2,1,8))
pdnHdsl2ShdslExtendedRateModeGroup.setObjects((_A,_AE))
if mibBuilder.loadTexts:pdnHdsl2ShdslExtendedRateModeGroup.setStatus(_B)
pdnHdsl2ShdslLoopAttenCrossing=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,23,0,1))
pdnHdsl2ShdslLoopAttenCrossing.setObjects(*((_A,_S),(_E,_c)))
if mibBuilder.loadTexts:pdnHdsl2ShdslLoopAttenCrossing.setStatus(_B)
pdnHdsl2ShdslSNRMarginCrossing=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,23,0,2))
pdnHdsl2ShdslSNRMarginCrossing.setObjects(*((_A,_T),(_E,_e)))
if mibBuilder.loadTexts:pdnHdsl2ShdslSNRMarginCrossing.setStatus(_B)
pdnHdsl2ShdslPerfESThresh=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,23,0,3))
pdnHdsl2ShdslPerfESThresh.setObjects(*((_A,_U),(_E,_a)))
if mibBuilder.loadTexts:pdnHdsl2ShdslPerfESThresh.setStatus(_B)
pdnHdsl2ShdslPerfSESThresh=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,23,0,4))
pdnHdsl2ShdslPerfSESThresh.setObjects(*((_A,_V),(_E,_d)))
if mibBuilder.loadTexts:pdnHdsl2ShdslPerfSESThresh.setStatus(_B)
pdnHdsl2ShdslPerfCRCanomaliesThresh=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,23,0,5))
pdnHdsl2ShdslPerfCRCanomaliesThresh.setObjects(*((_A,_W),(_E,_Z)))
if mibBuilder.loadTexts:pdnHdsl2ShdslPerfCRCanomaliesThresh.setStatus(_B)
pdnHdsl2ShdslPerfLOSWSThresh=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,23,0,6))
pdnHdsl2ShdslPerfLOSWSThresh.setObjects(*((_A,_X),(_E,_b)))
if mibBuilder.loadTexts:pdnHdsl2ShdslPerfLOSWSThresh.setStatus(_B)
pdnHdsl2ShdslPerfUASThresh=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,23,0,7))
pdnHdsl2ShdslPerfUASThresh.setObjects(*((_A,_Y),(_E,_f)))
if mibBuilder.loadTexts:pdnHdsl2ShdslPerfUASThresh.setStatus(_B)
pdnHdsl2ShdslpowerBackoff=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,23,0,8))
pdnHdsl2ShdslpowerBackoff.setObjects((_A,_F))
if mibBuilder.loadTexts:pdnHdsl2ShdslpowerBackoff.setStatus(_B)
pdnHdsl2ShdsldeviceFault=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,23,0,9))
pdnHdsl2ShdsldeviceFault.setObjects((_A,_F))
if mibBuilder.loadTexts:pdnHdsl2ShdsldeviceFault.setStatus(_B)
pdnHdsl2ShdsldcContinuityFault=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,23,0,10))
pdnHdsl2ShdsldcContinuityFault.setObjects((_A,_F))
if mibBuilder.loadTexts:pdnHdsl2ShdsldcContinuityFault.setStatus(_B)
pdnHdsl2ShdslconfigInitFailure=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,23,0,11))
pdnHdsl2ShdslconfigInitFailure.setObjects((_A,_F))
if mibBuilder.loadTexts:pdnHdsl2ShdslconfigInitFailure.setStatus(_B)
pdnHdsl2ShdslprotocolInitFailure=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,23,0,12))
pdnHdsl2ShdslprotocolInitFailure.setObjects((_A,_F))
if mibBuilder.loadTexts:pdnHdsl2ShdslprotocolInitFailure.setStatus(_B)
pdnHdsl2ShdslnoNeighborPresent=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,23,0,13))
pdnHdsl2ShdslnoNeighborPresent.setObjects((_A,_F))
if mibBuilder.loadTexts:pdnHdsl2ShdslnoNeighborPresent.setStatus(_B)
pdnHdsl2ShdslNotificationGroup=NotificationGroup((1,3,6,1,4,1,1795,2,24,2,6,23,3,2,3,1))
pdnHdsl2ShdslNotificationGroup.setObjects(*((_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR)))
if mibBuilder.loadTexts:pdnHdsl2ShdslNotificationGroup.setStatus(_B)
pdnHdsl2ShdslLineMIBCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,6,23,3,1,1))
pdnHdsl2ShdslLineMIBCompliance.setObjects(*((_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa)))
if mibBuilder.loadTexts:pdnHdsl2ShdslLineMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'PdnHdsl2ShdslWirePair':PdnHdsl2ShdslWirePair,'pdnHdsl2ShdslLineMIB':pdnHdsl2ShdslLineMIB,'pdnHdsl2ShdslLineNotifications':pdnHdsl2ShdslLineNotifications,_AF:pdnHdsl2ShdslLoopAttenCrossing,_AG:pdnHdsl2ShdslSNRMarginCrossing,_AH:pdnHdsl2ShdslPerfESThresh,_AI:pdnHdsl2ShdslPerfSESThresh,_AJ:pdnHdsl2ShdslPerfCRCanomaliesThresh,_AK:pdnHdsl2ShdslPerfLOSWSThresh,_AL:pdnHdsl2ShdslPerfUASThresh,_AM:pdnHdsl2ShdslpowerBackoff,_AN:pdnHdsl2ShdsldeviceFault,_AO:pdnHdsl2ShdsldcContinuityFault,_AP:pdnHdsl2ShdslconfigInitFailure,_AQ:pdnHdsl2ShdslprotocolInitFailure,_AR:pdnHdsl2ShdslnoNeighborPresent,'pdnHdsl2ShdslLineObjects':pdnHdsl2ShdslLineObjects,'pdnHdsl2ShdslSpanStatusExtTable':pdnHdsl2ShdslSpanStatusExtTable,'pdnHdsl2ShdslSpanStatusExtEntry':pdnHdsl2ShdslSpanStatusExtEntry,_k:pdnHdsl2ShdslStatusMaxAttainableLineRate,_l:pdnHdsl2ShdslStatusActualLineRate,'pdnHdsl2ShdslEndpointConfTable':pdnHdsl2ShdslEndpointConfTable,'pdnHdsl2ShdslEndpointConfEntry':pdnHdsl2ShdslEndpointConfEntry,_M:pdnHdsl2ShdslEndpointWirePair,_m:pdnHdsl2ShdslEndpointAlarmConfProfile,'pdnHdsl2ShdslEndpointCurrTable':pdnHdsl2ShdslEndpointCurrTable,'pdnHdsl2ShdslEndpointCurrEntry':pdnHdsl2ShdslEndpointCurrEntry,_S:pdnHdsl2ShdslEndpointCurrAtn,_T:pdnHdsl2ShdslEndpointCurrSnrMgn,_F:pdnHdsl2ShdslEndpointCurrStatus,_n:pdnHdsl2ShdslEndpointES,_o:pdnHdsl2ShdslEndpointSES,_p:pdnHdsl2ShdslEndpointCRCanomalies,_q:pdnHdsl2ShdslEndpointLOSWS,_r:pdnHdsl2ShdslEndpointUAS,_s:pdnHdsl2ShdslEndpointCurr15MinTimeElapsed,_U:pdnHdsl2ShdslEndpointCurr15MinES,_V:pdnHdsl2ShdslEndpointCurr15MinSES,_W:pdnHdsl2ShdslEndpointCurr15MinCRCanomalies,_X:pdnHdsl2ShdslEndpointCurr15MinLOSWS,_Y:pdnHdsl2ShdslEndpointCurr15MinUAS,_t:pdnHdsl2ShdslEndpointCurr1DayTimeElapsed,_u:pdnHdsl2ShdslEndpointCurr1DayES,_v:pdnHdsl2ShdslEndpointCurr1DaySES,_w:pdnHdsl2ShdslEndpointCurr1DayCRCanomalies,_x:pdnHdsl2ShdslEndpointCurr1DayLOSWS,_y:pdnHdsl2ShdslEndpointCurr1DayUAS,'pdnHdsl2Shdsl15MinIntervalTable':pdnHdsl2Shdsl15MinIntervalTable,'pdnHdsl2Shdsl15MinIntervalEntry':pdnHdsl2Shdsl15MinIntervalEntry,_i:pdnHdsl2Shdsl15MinIntervalNumber,_z:pdnHdsl2Shdsl15MinIntervalES,_A0:pdnHdsl2Shdsl15MinIntervalSES,_A1:pdnHdsl2Shdsl15MinIntervalCRCanomalies,_A2:pdnHdsl2Shdsl15MinIntervalLOSWS,_A3:pdnHdsl2Shdsl15MinIntervalUAS,'pdnHdsl2Shdsl1DayIntervalTable':pdnHdsl2Shdsl1DayIntervalTable,'pdnHdsl2Shdsl1DayIntervalEntry':pdnHdsl2Shdsl1DayIntervalEntry,_j:pdnHdsl2Shdsl1DayIntervalNumber,_A4:pdnHdsl2Shdsl1DayIntervalMoniSecs,_A5:pdnHdsl2Shdsl1DayIntervalES,_A6:pdnHdsl2Shdsl1DayIntervalSES,_A7:pdnHdsl2Shdsl1DayIntervalCRCanomalies,_A8:pdnHdsl2Shdsl1DayIntervalLOSWS,_A9:pdnHdsl2Shdsl1DayIntervalUAS,'pdnHdsl2ShdslSpanConfProfileExtTable':pdnHdsl2ShdslSpanConfProfileExtTable,'pdnHdsl2ShdslSpanConfProfileExtEntry':pdnHdsl2ShdslSpanConfProfileExtEntry,_AA:pdnHdsl2ShdslSpanConfWireInterface,_AB:pdnHdsl2ShdslSpanConfMinLineRate,_AC:pdnHdsl2ShdslSpanConfMaxLineRate,'pdnHdsl2ShdslIfTable':pdnHdsl2ShdslIfTable,'pdnHdsl2ShdslIfEntry':pdnHdsl2ShdslIfEntry,_AD:pdnHdsl2ShdslIfTableEquipMode,_AE:pdnHdsl2ShdslExtendedRateMode,'pdnHdsl2ShdslLineAFNs':pdnHdsl2ShdslLineAFNs,'pdnHdsl2ShdslLineConformance':pdnHdsl2ShdslLineConformance,'pdnHdsl2ShdslLineCompliances':pdnHdsl2ShdslLineCompliances,'pdnHdsl2ShdslLineMIBCompliance':pdnHdsl2ShdslLineMIBCompliance,'pdnHdsl2ShdslLineGroups':pdnHdsl2ShdslLineGroups,'pdnHdsl2ShdslLineObjGroups':pdnHdsl2ShdslLineObjGroups,_AS:pdnHdsl2ShdslSpanShdslStatusGroup,_AT:pdnHdsl2ShdslEndpointConfGroup,_AU:pdnHdsl2ShdslEndpointCurrGroup,_AV:pdnHdsl2Shdsl15MinIntervalGroup,_AW:pdnHdsl2Shdsl1DayIntervalGroup,_AX:pdnHdsl2ShdslSpanConfProfileGroup,_AY:pdnHdsl2ShdslIfTableGroup,_AZ:pdnHdsl2ShdslExtendedRateModeGroup,'pdnHdsl2ShdslLineAfnGroups':pdnHdsl2ShdslLineAfnGroups,'pdnHdsl2ShdslLineNtfyGroups':pdnHdsl2ShdslLineNtfyGroups,_Aa:pdnHdsl2ShdslNotificationGroup})