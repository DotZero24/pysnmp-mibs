_A3='hpicfFaultConfig5Group'
_A2='hpicfFaultConfig4Group'
_A1='hpicfFaultConfig3Group'
_A0='hpicfFaultStatusGroup'
_z='hpicfFaultConfig2Group'
_y='hpicfFaultConfigGroup'
_x='hpicfFaultFinderTrap'
_w='hpicfFfMcastStormPortDisablTimer'
_v='hpicfFfMcastStormAction'
_u='hpicfFfMcastStormRisingpps'
_t='hpicfFfMcastStormRisingpercent'
_s='hpicfFfMcastStormMode'
_r='hpicfFfLinkFlapControlPortDisableTimer'
_q='hpicfFfLinkFlapControlAction'
_p='hpicfFfLinkFlapControlSensitivity'
_o='hpicfFfBcastStormControlPortDisableTimer'
_n='hpicfFfBcastStormControlAction'
_m='hpicfFfBcastStormControlRisingpps'
_l='hpicfFfBcastStormControlRisingpercent'
_k='hpicfFfBcastStormControlMode'
_j='hpicfFfFaultLightStatus'
_i='hpicfFfSpeedReduceTolerance'
_h='hpicfFfLogInfo'
_g='hpicfFfLogInfoType'
_f='hpicfFfLogPhysClass'
_e='hpicfFfLogStatus'
_d='hpicfFfLogCreateTime'
_c='hpicfFfMcastStormPortIndex'
_b='hpicfFfLinkFlapControlPortIndex'
_a='disabled'
_Z='hpicfFfBcastStormControlPortIndex'
_Y='medium'
_X='hpicfFfLogIndex'
_W='hpicfFfControlIndex'
_V='OctetString'
_U='hpicfFaultNotifyGroup'
_T='hpicfFaultLogGroup'
_S='hpicfFfFaultInfoURL'
_R='hpicfFfLogSeverity'
_Q='hpicfFfLogAction'
_P='hpicfFfLogFaultType'
_O='hpicfFfLogPhysEntity'
_N='hpicfFfDisablePortTolerance'
_M='hpicfFfWarnTolerance'
_L='hpicfFfAction'
_K='seconds'
_J='warnAndDisable'
_I='warn'
_H='Unsigned32'
_G='not-accessible'
_F='none'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='HP-ICF-FAULT-FINDER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_V,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PhysicalClass,PhysicalIndex=mibBuilder.importSymbols('ENTITY-MIB','PhysicalClass','PhysicalIndex')
hpicfCommon,hpicfCommonTrapsPrefix,hpicfObjectModules=mibBuilder.importSymbols('HP-ICF-OID','hpicfCommon','hpicfCommonTrapsPrefix','hpicfObjectModules')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
hpicfFaultFinderMib=ModuleIdentity((1,3,6,1,4,1,11,2,14,10,2,12))
if mibBuilder.loadTexts:hpicfFaultFinderMib.setRevisions(('2017-11-20 14:12','2015-08-04 14:12','2013-08-21 00:00','2010-01-25 20:24','2009-05-22 00:00','2009-02-25 13:31','2007-01-09 14:56','2005-05-02 19:34','2005-03-22 11:30','2003-07-28 07:07','2000-11-03 07:07','1998-11-20 23:50','1997-10-21 02:49'))
class HpicfFaultType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42)));namedValues=NamedValues(*(('badDriver',1),('badXcvr',2),('badCable',3),('tooLongCable',4),('overBandwidth',5),('bcastStorm',6),('partition',7),('misconfiguredSQE',8),('polarityReversal',9),('networkLoop',10),('lossOfLink',11),('portSecurityViolation',12),('backupLinkTransition',13),('meshingFault',14),('fanFault',15),('rpsFault',16),('stuck10MbFault',17),('lossOfStackMember',18),('hotSwapReboot',19),('duplexMismatchHDX',20),('duplexMismatchFDX',21),('flowcntlJumbosFault',22),('portSelftestFailure',23),('xcvrUnidentified',24),('xcvrUnsupported',25),('crfNotify',26),('crfThrottled',27),('crfBlocked',28),('xcvrNotYetSupported',29),('xcvrBRevOnly',30),('xcvrNotSupportedOnPort',31),('phyReadFailure',32),('linkFlap',33),('intel82566dmportprotect',34),('xcvrExceedQty',35),('xcvrClone',36),('xcvrCloneReminder',37),('bcastStormPerPort',38),('linkFlapPerPort',39),('rxNonStdPreamble',40),('mcastStorm',41),('mcastStormPerPort',42)))
class HpicfFaultTolerance(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class HpicfFaultAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_I,2),(_J,3),('warnAndSpeedReduce',4),('warnAndSpeedReduceAndDisable',5)))
class HpicfUrlString(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpicfFaultFinderConformance_ObjectIdentity=ObjectIdentity
hpicfFaultFinderConformance=_HpicfFaultFinderConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,12,1))
_HpicfFaultFinderCompliances_ObjectIdentity=ObjectIdentity
hpicfFaultFinderCompliances=_HpicfFaultFinderCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,12,1,1))
_HpicfFaultFinderGroups_ObjectIdentity=ObjectIdentity
hpicfFaultFinderGroups=_HpicfFaultFinderGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,10,2,12,1,2))
_HpicfFaultFinder_ObjectIdentity=ObjectIdentity
hpicfFaultFinder=_HpicfFaultFinder_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,7))
_HpicfFfControlTable_Object=MibTable
hpicfFfControlTable=_HpicfFfControlTable_Object((1,3,6,1,4,1,11,2,14,11,1,7,1))
if mibBuilder.loadTexts:hpicfFfControlTable.setStatus(_A)
_HpicfFfControlEntry_Object=MibTableRow
hpicfFfControlEntry=_HpicfFfControlEntry_Object((1,3,6,1,4,1,11,2,14,11,1,7,1,1))
hpicfFfControlEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:hpicfFfControlEntry.setStatus(_A)
_HpicfFfControlIndex_Type=HpicfFaultType
_HpicfFfControlIndex_Object=MibTableColumn
hpicfFfControlIndex=_HpicfFfControlIndex_Object((1,3,6,1,4,1,11,2,14,11,1,7,1,1,1),_HpicfFfControlIndex_Type())
hpicfFfControlIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfFfControlIndex.setStatus(_A)
_HpicfFfAction_Type=HpicfFaultAction
_HpicfFfAction_Object=MibTableColumn
hpicfFfAction=_HpicfFfAction_Object((1,3,6,1,4,1,11,2,14,11,1,7,1,1,2),_HpicfFfAction_Type())
hpicfFfAction.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfFfAction.setStatus(_A)
_HpicfFfWarnTolerance_Type=HpicfFaultTolerance
_HpicfFfWarnTolerance_Object=MibTableColumn
hpicfFfWarnTolerance=_HpicfFfWarnTolerance_Object((1,3,6,1,4,1,11,2,14,11,1,7,1,1,3),_HpicfFfWarnTolerance_Type())
hpicfFfWarnTolerance.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfFfWarnTolerance.setStatus(_A)
_HpicfFfDisablePortTolerance_Type=HpicfFaultTolerance
_HpicfFfDisablePortTolerance_Object=MibTableColumn
hpicfFfDisablePortTolerance=_HpicfFfDisablePortTolerance_Object((1,3,6,1,4,1,11,2,14,11,1,7,1,1,4),_HpicfFfDisablePortTolerance_Type())
hpicfFfDisablePortTolerance.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfFfDisablePortTolerance.setStatus(_A)
_HpicfFfSpeedReduceTolerance_Type=HpicfFaultTolerance
_HpicfFfSpeedReduceTolerance_Object=MibTableColumn
hpicfFfSpeedReduceTolerance=_HpicfFfSpeedReduceTolerance_Object((1,3,6,1,4,1,11,2,14,11,1,7,1,1,5),_HpicfFfSpeedReduceTolerance_Type())
hpicfFfSpeedReduceTolerance.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfFfSpeedReduceTolerance.setStatus(_A)
_HpicfFfLogTable_Object=MibTable
hpicfFfLogTable=_HpicfFfLogTable_Object((1,3,6,1,4,1,11,2,14,11,1,7,2))
if mibBuilder.loadTexts:hpicfFfLogTable.setStatus(_A)
_HpicfFfLogEntry_Object=MibTableRow
hpicfFfLogEntry=_HpicfFfLogEntry_Object((1,3,6,1,4,1,11,2,14,11,1,7,2,1))
hpicfFfLogEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:hpicfFfLogEntry.setStatus(_A)
class _HpicfFfLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpicfFfLogIndex_Type.__name__=_D
_HpicfFfLogIndex_Object=MibTableColumn
hpicfFfLogIndex=_HpicfFfLogIndex_Object((1,3,6,1,4,1,11,2,14,11,1,7,2,1,1),_HpicfFfLogIndex_Type())
hpicfFfLogIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfFfLogIndex.setStatus(_A)
_HpicfFfLogCreateTime_Type=TimeStamp
_HpicfFfLogCreateTime_Object=MibTableColumn
hpicfFfLogCreateTime=_HpicfFfLogCreateTime_Object((1,3,6,1,4,1,11,2,14,11,1,7,2,1,2),_HpicfFfLogCreateTime_Type())
hpicfFfLogCreateTime.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfFfLogCreateTime.setStatus(_A)
_HpicfFfLogPhysEntity_Type=PhysicalIndex
_HpicfFfLogPhysEntity_Object=MibTableColumn
hpicfFfLogPhysEntity=_HpicfFfLogPhysEntity_Object((1,3,6,1,4,1,11,2,14,11,1,7,2,1,3),_HpicfFfLogPhysEntity_Type())
hpicfFfLogPhysEntity.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfFfLogPhysEntity.setStatus(_A)
_HpicfFfLogFaultType_Type=HpicfFaultType
_HpicfFfLogFaultType_Object=MibTableColumn
hpicfFfLogFaultType=_HpicfFfLogFaultType_Object((1,3,6,1,4,1,11,2,14,11,1,7,2,1,4),_HpicfFfLogFaultType_Type())
hpicfFfLogFaultType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfFfLogFaultType.setStatus(_A)
_HpicfFfLogAction_Type=HpicfFaultAction
_HpicfFfLogAction_Object=MibTableColumn
hpicfFfLogAction=_HpicfFfLogAction_Object((1,3,6,1,4,1,11,2,14,11,1,7,2,1,5),_HpicfFfLogAction_Type())
hpicfFfLogAction.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfFfLogAction.setStatus(_A)
class _HpicfFfLogSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('informational',1),(_Y,2),('critical',3)))
_HpicfFfLogSeverity_Type.__name__=_D
_HpicfFfLogSeverity_Object=MibTableColumn
hpicfFfLogSeverity=_HpicfFfLogSeverity_Object((1,3,6,1,4,1,11,2,14,11,1,7,2,1,6),_HpicfFfLogSeverity_Type())
hpicfFfLogSeverity.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfFfLogSeverity.setStatus(_A)
class _HpicfFfLogStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('new',1),('active',2),('old',3)))
_HpicfFfLogStatus_Type.__name__=_D
_HpicfFfLogStatus_Object=MibTableColumn
hpicfFfLogStatus=_HpicfFfLogStatus_Object((1,3,6,1,4,1,11,2,14,11,1,7,2,1,7),_HpicfFfLogStatus_Type())
hpicfFfLogStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfFfLogStatus.setStatus(_A)
_HpicfFfLogPhysClass_Type=PhysicalClass
_HpicfFfLogPhysClass_Object=MibTableColumn
hpicfFfLogPhysClass=_HpicfFfLogPhysClass_Object((1,3,6,1,4,1,11,2,14,11,1,7,2,1,8),_HpicfFfLogPhysClass_Type())
hpicfFfLogPhysClass.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfFfLogPhysClass.setStatus(_A)
class _HpicfFfLogInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4Address',1),('displayString',2)))
_HpicfFfLogInfoType_Type.__name__=_D
_HpicfFfLogInfoType_Object=MibTableColumn
hpicfFfLogInfoType=_HpicfFfLogInfoType_Object((1,3,6,1,4,1,11,2,14,11,1,7,2,1,9),_HpicfFfLogInfoType_Type())
hpicfFfLogInfoType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfFfLogInfoType.setStatus(_A)
class _HpicfFfLogInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpicfFfLogInfo_Type.__name__=_V
_HpicfFfLogInfo_Object=MibTableColumn
hpicfFfLogInfo=_HpicfFfLogInfo_Object((1,3,6,1,4,1,11,2,14,11,1,7,2,1,10),_HpicfFfLogInfo_Type())
hpicfFfLogInfo.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfFfLogInfo.setStatus(_A)
_HpicfFfFaultInfoURL_Type=HpicfUrlString
_HpicfFfFaultInfoURL_Object=MibScalar
hpicfFfFaultInfoURL=_HpicfFfFaultInfoURL_Object((1,3,6,1,4,1,11,2,14,11,1,7,3),_HpicfFfFaultInfoURL_Type())
hpicfFfFaultInfoURL.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:hpicfFfFaultInfoURL.setStatus(_A)
class _HpicfFfFaultLightStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('faultLightOff',1),('faultLightOn',2)))
_HpicfFfFaultLightStatus_Type.__name__=_D
_HpicfFfFaultLightStatus_Object=MibScalar
hpicfFfFaultLightStatus=_HpicfFfFaultLightStatus_Object((1,3,6,1,4,1,11,2,14,11,1,7,4),_HpicfFfFaultLightStatus_Type())
hpicfFfFaultLightStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfFfFaultLightStatus.setStatus(_A)
_HpicfFfBcastStormControlPortConfig_ObjectIdentity=ObjectIdentity
hpicfFfBcastStormControlPortConfig=_HpicfFfBcastStormControlPortConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,7,5))
_HpicfFfBcastStormControlPortConfigTable_Object=MibTable
hpicfFfBcastStormControlPortConfigTable=_HpicfFfBcastStormControlPortConfigTable_Object((1,3,6,1,4,1,11,2,14,11,1,7,5,1))
if mibBuilder.loadTexts:hpicfFfBcastStormControlPortConfigTable.setStatus(_A)
_HpicfFfBcastStormControlPortConfigEntry_Object=MibTableRow
hpicfFfBcastStormControlPortConfigEntry=_HpicfFfBcastStormControlPortConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,1,7,5,1,1))
hpicfFfBcastStormControlPortConfigEntry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:hpicfFfBcastStormControlPortConfigEntry.setStatus(_A)
_HpicfFfBcastStormControlPortIndex_Type=InterfaceIndex
_HpicfFfBcastStormControlPortIndex_Object=MibTableColumn
hpicfFfBcastStormControlPortIndex=_HpicfFfBcastStormControlPortIndex_Object((1,3,6,1,4,1,11,2,14,11,1,7,5,1,1,1),_HpicfFfBcastStormControlPortIndex_Type())
hpicfFfBcastStormControlPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfFfBcastStormControlPortIndex.setStatus(_A)
class _HpicfFfBcastStormControlMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_a,1),('bcastRisingLevelpercent',2),('bcastRisingLevelpps',3)))
_HpicfFfBcastStormControlMode_Type.__name__=_D
_HpicfFfBcastStormControlMode_Object=MibTableColumn
hpicfFfBcastStormControlMode=_HpicfFfBcastStormControlMode_Object((1,3,6,1,4,1,11,2,14,11,1,7,5,1,1,2),_HpicfFfBcastStormControlMode_Type())
hpicfFfBcastStormControlMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfFfBcastStormControlMode.setStatus(_A)
class _HpicfFfBcastStormControlRisingpercent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HpicfFfBcastStormControlRisingpercent_Type.__name__=_D
_HpicfFfBcastStormControlRisingpercent_Object=MibTableColumn
hpicfFfBcastStormControlRisingpercent=_HpicfFfBcastStormControlRisingpercent_Object((1,3,6,1,4,1,11,2,14,11,1,7,5,1,1,3),_HpicfFfBcastStormControlRisingpercent_Type())
hpicfFfBcastStormControlRisingpercent.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfFfBcastStormControlRisingpercent.setStatus(_A)
class _HpicfFfBcastStormControlRisingpps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000000))
_HpicfFfBcastStormControlRisingpps_Type.__name__=_D
_HpicfFfBcastStormControlRisingpps_Object=MibTableColumn
hpicfFfBcastStormControlRisingpps=_HpicfFfBcastStormControlRisingpps_Object((1,3,6,1,4,1,11,2,14,11,1,7,5,1,1,4),_HpicfFfBcastStormControlRisingpps_Type())
hpicfFfBcastStormControlRisingpps.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfFfBcastStormControlRisingpps.setStatus(_A)
class _HpicfFfBcastStormControlAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_I,2),(_J,3)))
_HpicfFfBcastStormControlAction_Type.__name__=_D
_HpicfFfBcastStormControlAction_Object=MibTableColumn
hpicfFfBcastStormControlAction=_HpicfFfBcastStormControlAction_Object((1,3,6,1,4,1,11,2,14,11,1,7,5,1,1,5),_HpicfFfBcastStormControlAction_Type())
hpicfFfBcastStormControlAction.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfFfBcastStormControlAction.setStatus(_A)
class _HpicfFfBcastStormControlPortDisableTimer_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,604800))
_HpicfFfBcastStormControlPortDisableTimer_Type.__name__=_H
_HpicfFfBcastStormControlPortDisableTimer_Object=MibTableColumn
hpicfFfBcastStormControlPortDisableTimer=_HpicfFfBcastStormControlPortDisableTimer_Object((1,3,6,1,4,1,11,2,14,11,1,7,5,1,1,6),_HpicfFfBcastStormControlPortDisableTimer_Type())
hpicfFfBcastStormControlPortDisableTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfFfBcastStormControlPortDisableTimer.setStatus(_A)
if mibBuilder.loadTexts:hpicfFfBcastStormControlPortDisableTimer.setUnits(_K)
_HpicfFfLinkFlapControlPortConfig_ObjectIdentity=ObjectIdentity
hpicfFfLinkFlapControlPortConfig=_HpicfFfLinkFlapControlPortConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,7,6))
_HpicfFfLinkFlapControlPortConfigTable_Object=MibTable
hpicfFfLinkFlapControlPortConfigTable=_HpicfFfLinkFlapControlPortConfigTable_Object((1,3,6,1,4,1,11,2,14,11,1,7,6,1))
if mibBuilder.loadTexts:hpicfFfLinkFlapControlPortConfigTable.setStatus(_A)
_HpicfFfLinkFlapControlPortConfigEntry_Object=MibTableRow
hpicfFfLinkFlapControlPortConfigEntry=_HpicfFfLinkFlapControlPortConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,1,7,6,1,1))
hpicfFfLinkFlapControlPortConfigEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:hpicfFfLinkFlapControlPortConfigEntry.setStatus(_A)
_HpicfFfLinkFlapControlPortIndex_Type=InterfaceIndex
_HpicfFfLinkFlapControlPortIndex_Object=MibTableColumn
hpicfFfLinkFlapControlPortIndex=_HpicfFfLinkFlapControlPortIndex_Object((1,3,6,1,4,1,11,2,14,11,1,7,6,1,1,1),_HpicfFfLinkFlapControlPortIndex_Type())
hpicfFfLinkFlapControlPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfFfLinkFlapControlPortIndex.setStatus(_A)
class _HpicfFfLinkFlapControlSensitivity_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,3,6,10)));namedValues=NamedValues(*((_F,0),('high',3),(_Y,6),('low',10)))
_HpicfFfLinkFlapControlSensitivity_Type.__name__=_D
_HpicfFfLinkFlapControlSensitivity_Object=MibTableColumn
hpicfFfLinkFlapControlSensitivity=_HpicfFfLinkFlapControlSensitivity_Object((1,3,6,1,4,1,11,2,14,11,1,7,6,1,1,2),_HpicfFfLinkFlapControlSensitivity_Type())
hpicfFfLinkFlapControlSensitivity.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfFfLinkFlapControlSensitivity.setStatus(_A)
class _HpicfFfLinkFlapControlAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_I,2),(_J,3)))
_HpicfFfLinkFlapControlAction_Type.__name__=_D
_HpicfFfLinkFlapControlAction_Object=MibTableColumn
hpicfFfLinkFlapControlAction=_HpicfFfLinkFlapControlAction_Object((1,3,6,1,4,1,11,2,14,11,1,7,6,1,1,3),_HpicfFfLinkFlapControlAction_Type())
hpicfFfLinkFlapControlAction.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfFfLinkFlapControlAction.setStatus(_A)
class _HpicfFfLinkFlapControlPortDisableTimer_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,604800))
_HpicfFfLinkFlapControlPortDisableTimer_Type.__name__=_H
_HpicfFfLinkFlapControlPortDisableTimer_Object=MibTableColumn
hpicfFfLinkFlapControlPortDisableTimer=_HpicfFfLinkFlapControlPortDisableTimer_Object((1,3,6,1,4,1,11,2,14,11,1,7,6,1,1,4),_HpicfFfLinkFlapControlPortDisableTimer_Type())
hpicfFfLinkFlapControlPortDisableTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfFfLinkFlapControlPortDisableTimer.setStatus(_A)
if mibBuilder.loadTexts:hpicfFfLinkFlapControlPortDisableTimer.setUnits(_K)
_HpicfFfMcastStormPortConfig_ObjectIdentity=ObjectIdentity
hpicfFfMcastStormPortConfig=_HpicfFfMcastStormPortConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,7,7))
_HpicfFfMcastStormPortConfigTable_Object=MibTable
hpicfFfMcastStormPortConfigTable=_HpicfFfMcastStormPortConfigTable_Object((1,3,6,1,4,1,11,2,14,11,1,7,7,1))
if mibBuilder.loadTexts:hpicfFfMcastStormPortConfigTable.setStatus(_A)
_HpicfFfMcastStormPortConfigEntry_Object=MibTableRow
hpicfFfMcastStormPortConfigEntry=_HpicfFfMcastStormPortConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,1,7,7,1,1))
hpicfFfMcastStormPortConfigEntry.setIndexNames((0,_B,_c))
if mibBuilder.loadTexts:hpicfFfMcastStormPortConfigEntry.setStatus(_A)
_HpicfFfMcastStormPortIndex_Type=InterfaceIndex
_HpicfFfMcastStormPortIndex_Object=MibTableColumn
hpicfFfMcastStormPortIndex=_HpicfFfMcastStormPortIndex_Object((1,3,6,1,4,1,11,2,14,11,1,7,7,1,1,1),_HpicfFfMcastStormPortIndex_Type())
hpicfFfMcastStormPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfFfMcastStormPortIndex.setStatus(_A)
class _HpicfFfMcastStormMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_a,1),('mcastRisingLevelpercent',2),('mcastRisingLevelpps',3)))
_HpicfFfMcastStormMode_Type.__name__=_D
_HpicfFfMcastStormMode_Object=MibTableColumn
hpicfFfMcastStormMode=_HpicfFfMcastStormMode_Object((1,3,6,1,4,1,11,2,14,11,1,7,7,1,1,2),_HpicfFfMcastStormMode_Type())
hpicfFfMcastStormMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfFfMcastStormMode.setStatus(_A)
class _HpicfFfMcastStormRisingpercent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HpicfFfMcastStormRisingpercent_Type.__name__=_D
_HpicfFfMcastStormRisingpercent_Object=MibTableColumn
hpicfFfMcastStormRisingpercent=_HpicfFfMcastStormRisingpercent_Object((1,3,6,1,4,1,11,2,14,11,1,7,7,1,1,3),_HpicfFfMcastStormRisingpercent_Type())
hpicfFfMcastStormRisingpercent.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfFfMcastStormRisingpercent.setStatus(_A)
class _HpicfFfMcastStormRisingpps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000000))
_HpicfFfMcastStormRisingpps_Type.__name__=_D
_HpicfFfMcastStormRisingpps_Object=MibTableColumn
hpicfFfMcastStormRisingpps=_HpicfFfMcastStormRisingpps_Object((1,3,6,1,4,1,11,2,14,11,1,7,7,1,1,4),_HpicfFfMcastStormRisingpps_Type())
hpicfFfMcastStormRisingpps.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfFfMcastStormRisingpps.setStatus(_A)
class _HpicfFfMcastStormAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_I,2),(_J,3)))
_HpicfFfMcastStormAction_Type.__name__=_D
_HpicfFfMcastStormAction_Object=MibTableColumn
hpicfFfMcastStormAction=_HpicfFfMcastStormAction_Object((1,3,6,1,4,1,11,2,14,11,1,7,7,1,1,5),_HpicfFfMcastStormAction_Type())
hpicfFfMcastStormAction.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfFfMcastStormAction.setStatus(_A)
class _HpicfFfMcastStormPortDisablTimer_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,604800))
_HpicfFfMcastStormPortDisablTimer_Type.__name__=_H
_HpicfFfMcastStormPortDisablTimer_Object=MibTableColumn
hpicfFfMcastStormPortDisablTimer=_HpicfFfMcastStormPortDisablTimer_Object((1,3,6,1,4,1,11,2,14,11,1,7,7,1,1,6),_HpicfFfMcastStormPortDisablTimer_Type())
hpicfFfMcastStormPortDisablTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfFfMcastStormPortDisablTimer.setStatus(_A)
if mibBuilder.loadTexts:hpicfFfMcastStormPortDisablTimer.setUnits(_K)
hpicfFaultConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,10,2,12,1,2,1))
hpicfFaultConfigGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:hpicfFaultConfigGroup.setStatus(_A)
hpicfFaultLogGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,10,2,12,1,2,2))
hpicfFaultLogGroup.setObjects(*((_B,_d),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_e),(_B,_S),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:hpicfFaultLogGroup.setStatus(_A)
hpicfFaultConfig2Group=ObjectGroup((1,3,6,1,4,1,11,2,14,10,2,12,1,2,4))
hpicfFaultConfig2Group.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_i)))
if mibBuilder.loadTexts:hpicfFaultConfig2Group.setStatus(_A)
hpicfFaultStatusGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,10,2,12,1,2,5))
hpicfFaultStatusGroup.setObjects((_B,_j))
if mibBuilder.loadTexts:hpicfFaultStatusGroup.setStatus(_A)
hpicfFaultConfig3Group=ObjectGroup((1,3,6,1,4,1,11,2,14,10,2,12,1,2,6))
hpicfFaultConfig3Group.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:hpicfFaultConfig3Group.setStatus(_A)
hpicfFaultConfig4Group=ObjectGroup((1,3,6,1,4,1,11,2,14,10,2,12,1,2,7))
hpicfFaultConfig4Group.setObjects(*((_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:hpicfFaultConfig4Group.setStatus(_A)
hpicfFaultConfig5Group=ObjectGroup((1,3,6,1,4,1,11,2,14,10,2,12,1,2,8))
hpicfFaultConfig5Group.setObjects(*((_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:hpicfFaultConfig5Group.setStatus(_A)
hpicfFaultFinderTrap=NotificationType((1,3,6,1,4,1,11,2,14,12,1,0,5))
hpicfFaultFinderTrap.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_O)))
if mibBuilder.loadTexts:hpicfFaultFinderTrap.setStatus(_A)
hpicfFaultNotifyGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,10,2,12,1,2,3))
hpicfFaultNotifyGroup.setObjects((_B,_x))
if mibBuilder.loadTexts:hpicfFaultNotifyGroup.setStatus(_A)
hpicfFaultFinderCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,10,2,12,1,1,1))
hpicfFaultFinderCompliance.setObjects(*((_B,_y),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:hpicfFaultFinderCompliance.setStatus(_A)
hpicfFaultFinder2Compliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,10,2,12,1,1,2))
hpicfFaultFinder2Compliance.setObjects(*((_B,_z),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:hpicfFaultFinder2Compliance.setStatus(_A)
hpicfFaultStatusCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,10,2,12,1,1,3))
hpicfFaultStatusCompliance.setObjects((_B,_A0))
if mibBuilder.loadTexts:hpicfFaultStatusCompliance.setStatus(_A)
hpicfFaultFinder3Compliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,10,2,12,1,1,4))
hpicfFaultFinder3Compliance.setObjects((_B,_A1))
if mibBuilder.loadTexts:hpicfFaultFinder3Compliance.setStatus(_A)
hpicfFaultFinder4Compliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,10,2,12,1,1,5))
hpicfFaultFinder4Compliance.setObjects((_B,_A2))
if mibBuilder.loadTexts:hpicfFaultFinder4Compliance.setStatus(_A)
hpicfFaultFinder5Compliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,10,2,12,1,1,6))
hpicfFaultFinder5Compliance.setObjects((_B,_A3))
if mibBuilder.loadTexts:hpicfFaultFinder5Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'HpicfFaultType':HpicfFaultType,'HpicfFaultTolerance':HpicfFaultTolerance,'HpicfFaultAction':HpicfFaultAction,'HpicfUrlString':HpicfUrlString,'hpicfFaultFinderMib':hpicfFaultFinderMib,'hpicfFaultFinderConformance':hpicfFaultFinderConformance,'hpicfFaultFinderCompliances':hpicfFaultFinderCompliances,'hpicfFaultFinderCompliance':hpicfFaultFinderCompliance,'hpicfFaultFinder2Compliance':hpicfFaultFinder2Compliance,'hpicfFaultStatusCompliance':hpicfFaultStatusCompliance,'hpicfFaultFinder3Compliance':hpicfFaultFinder3Compliance,'hpicfFaultFinder4Compliance':hpicfFaultFinder4Compliance,'hpicfFaultFinder5Compliance':hpicfFaultFinder5Compliance,'hpicfFaultFinderGroups':hpicfFaultFinderGroups,_y:hpicfFaultConfigGroup,_T:hpicfFaultLogGroup,_U:hpicfFaultNotifyGroup,_z:hpicfFaultConfig2Group,_A0:hpicfFaultStatusGroup,_A1:hpicfFaultConfig3Group,_A2:hpicfFaultConfig4Group,_A3:hpicfFaultConfig5Group,'hpicfFaultFinder':hpicfFaultFinder,'hpicfFfControlTable':hpicfFfControlTable,'hpicfFfControlEntry':hpicfFfControlEntry,_W:hpicfFfControlIndex,_L:hpicfFfAction,_M:hpicfFfWarnTolerance,_N:hpicfFfDisablePortTolerance,_i:hpicfFfSpeedReduceTolerance,'hpicfFfLogTable':hpicfFfLogTable,'hpicfFfLogEntry':hpicfFfLogEntry,_X:hpicfFfLogIndex,_d:hpicfFfLogCreateTime,_O:hpicfFfLogPhysEntity,_P:hpicfFfLogFaultType,_Q:hpicfFfLogAction,_R:hpicfFfLogSeverity,_e:hpicfFfLogStatus,_f:hpicfFfLogPhysClass,_g:hpicfFfLogInfoType,_h:hpicfFfLogInfo,_S:hpicfFfFaultInfoURL,_j:hpicfFfFaultLightStatus,'hpicfFfBcastStormControlPortConfig':hpicfFfBcastStormControlPortConfig,'hpicfFfBcastStormControlPortConfigTable':hpicfFfBcastStormControlPortConfigTable,'hpicfFfBcastStormControlPortConfigEntry':hpicfFfBcastStormControlPortConfigEntry,_Z:hpicfFfBcastStormControlPortIndex,_k:hpicfFfBcastStormControlMode,_l:hpicfFfBcastStormControlRisingpercent,_m:hpicfFfBcastStormControlRisingpps,_n:hpicfFfBcastStormControlAction,_o:hpicfFfBcastStormControlPortDisableTimer,'hpicfFfLinkFlapControlPortConfig':hpicfFfLinkFlapControlPortConfig,'hpicfFfLinkFlapControlPortConfigTable':hpicfFfLinkFlapControlPortConfigTable,'hpicfFfLinkFlapControlPortConfigEntry':hpicfFfLinkFlapControlPortConfigEntry,_b:hpicfFfLinkFlapControlPortIndex,_p:hpicfFfLinkFlapControlSensitivity,_q:hpicfFfLinkFlapControlAction,_r:hpicfFfLinkFlapControlPortDisableTimer,'hpicfFfMcastStormPortConfig':hpicfFfMcastStormPortConfig,'hpicfFfMcastStormPortConfigTable':hpicfFfMcastStormPortConfigTable,'hpicfFfMcastStormPortConfigEntry':hpicfFfMcastStormPortConfigEntry,_c:hpicfFfMcastStormPortIndex,_s:hpicfFfMcastStormMode,_t:hpicfFfMcastStormRisingpercent,_u:hpicfFfMcastStormRisingpps,_v:hpicfFfMcastStormAction,_w:hpicfFfMcastStormPortDisablTimer,_x:hpicfFaultFinderTrap})