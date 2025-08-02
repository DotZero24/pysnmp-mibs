_Ab='tnSysTopologyGroup'
_Aa='tnIfGroup'
_AZ='tnAccessPortGroup'
_AY='tnSysTopologyAudit'
_AX='tnIfAlmProfName'
_AW='tnIfnumofTimeSlots'
_AV='tnIfForceAdminStatus'
_AU='tnIfSupportedTypesAlternate'
_AT='tnIfSupportedTypes'
_AS='tnIfPhysicalLocation'
_AR='tnAccessPortModuleReset'
_AQ='tnAccessPortAlienWavebank'
_AP='tnAccessPortFacilityDescriptorCirId'
_AO='tnAccessPortFacilityDescriptorDesc'
_AN='tnAccessPortFacilityDescriptorName'
_AM='tnAccessPortRole'
_AL='tnAccessPortAseMode'
_AK='tnAccessPortCpriRole'
_AJ='tnAccessPortFecBypassInd'
_AI='tnAccessPortFecType'
_AH='tnAccessPortCpriMappingType'
_AG='tnAccessPortDirectionCapability'
_AF='tnAccessPortL2FarEndMacAddress'
_AE='tnAccessPortL2FarEndIfIndex'
_AD='tnAccessFilterScheduledTime'
_AC='tnAccessFilterCalibrateTime'
_AB='tnAccessFilterRecordTime'
_AA='tnAccessFilterAltitude'
_A9='tnAccessFilterCalibrated'
_A8='tnAccessFilterRecorded'
_A7='tnAccessFilterPressure'
_A6='tnAccessFilterAmbientTemperature'
_A5='tnAccessPortmfcDifferentialPressure'
_A4='tnAccessPortmfcNominalPressure'
_A3='tnAccessPortmfcTemperature'
_A2='tnAccessPortAlmProfName'
_A1='tnAccessPortMonOcmConnAddress'
_A0='tnAccessPortIsMpo'
_z='tnAccessPortMpoConnectorPortInIfIndex'
_y='tnAccessPortMpoConnectorPortOutIfIndex'
_x='tnAccessPortHasMpoConnector'
_w='tnAccessPortWtDomainNumber'
_v='tnAccessPortIsValidInternalOTSXcEndpoint'
_u='tnAccessPortOppDirectionPortAddress'
_t='tnAccessPortWtocmConnAddress'
_s='tnAccessPortWtocmConnLoss'
_r='tnAccessPortExtAmpIpAddressOut'
_q='tnAccessPortExtAmpIpAddressIn'
_p='tnAccessPortFarEndTypeConnFrom'
_o='tnAccessPortFarEndIfIndexConnFrom'
_n='tnAccessPortFarEndAddressConnFrom'
_m='tnAccessPortIsDomainEdgePort'
_l='tnAccessPortAINSDebounceTimeRemaining'
_k='tnAccessPortUsingSysAINSDebounceTime'
_j='tnAccessPortAINSDebounceTime'
_i='tnAccessPortAINS'
_h='tnAccessPortDirection'
_g='tnAccessPortFarEndType'
_f='tnAccessPortFarEndIfIndex'
_e='tnAccessPortFarEndAddress'
_d='tnAccessPortStateQualifier'
_c='tnAccessPortOperationalCapability'
_b='tnAccessPortStatusLEDState'
_a='tnAccessPortStatusLEDColor'
_Z='tnAccessPortDescr'
_Y='tnIfEntry'
_X='Celsius'
_W='00000000'
_V='seconds'
_U='cluster'
_T='interCompound'
_S='external'
_R='internal'
_Q='notConnected'
_P='TropicStateQualifierType'
_O='TropicOperationalCapabilityType'
_N='AluWdmFecMode'
_M='ifIndex'
_L='IF-MIB'
_K='Unsigned32'
_J='IpAddress'
_I='OctetString'
_H='TruthValue'
_G='InterfaceIndexOrZero'
_F='SnmpAdminString'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='TROPIC-ACCESSPORT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero,ifEntry,ifIndex=mibBuilder.importSymbols(_L,'InterfaceIndex',_G,'ifEntry',_M)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,_J,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_H)
tnAccessPortMIB,tnPortModules=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnAccessPortMIB','tnPortModules')
AluWdmFecMode,AluWdmTnIfType,TnCommand,TropicLEDColorType,TropicLEDStateType,TropicOperationalCapabilityType,TropicStateQualifierType=mibBuilder.importSymbols('TROPIC-TC',_N,'AluWdmTnIfType','TnCommand','TropicLEDColorType','TropicLEDStateType',_O,_P)
tnAccessPortMibModules=ModuleIdentity((1,3,6,1,4,1,7483,1,1,2,2,4,1))
if mibBuilder.loadTexts:tnAccessPortMibModules.setRevisions(('2020-12-11 12:00','2020-11-27 12:00','2020-05-01 12:00','2020-04-03 12:00','2020-03-27 12:00','2020-03-20 12:00','2020-02-28 12:00','2020-02-21 12:00','2020-01-24 12:00','2019-12-27 12:00','2019-10-18 12:00','2019-09-06 12:00','2019-08-09 12:00','2019-05-17 12:00','2019-03-08 12:00','2019-01-11 12:00','2018-11-02 12:00','2018-08-03 12:00','2018-07-20 12:00','2018-06-08 12:00','2018-05-11 12:00','2018-04-20 12:00','2018-02-23 12:00','2018-01-05 12:00','2017-12-29 12:00','2017-10-06 12:00','2017-04-07 12:00','2017-01-13 12:00','2016-12-28 12:00','2016-11-22 12:00','2016-11-16 12:00','2016-10-19 12:00','2016-08-24 12:00','2016-05-11 12:00','2015-10-05 12:00','2015-09-28 12:00','2015-07-03 12:00','2015-05-18 12:00','2015-05-15 12:00','2015-01-22 12:00','2014-11-24 12:00','2014-05-18 12:00','2014-03-18 12:00','2014-02-26 12:00','2013-06-13 12:00','2013-05-21 12:00','2013-04-12 12:00','2013-03-15 12:00','2012-12-17 12:00','2012-09-27 12:00','2012-09-06 12:00','2012-08-06 12:00','2012-04-25 12:00','2012-02-28 12:00','2011-11-16 12:00','2011-09-30 12:00','2010-10-19 12:00','2010-09-20 12:00','2010-06-28 12:00','2010-06-04 12:00','2010-05-10 12:00','2010-01-15 12:00','2010-01-04 12:00','2009-11-01 12:00','2009-07-10 12:00','2009-07-08 12:00','2009-06-07 12:00','2009-03-31 12:00','2009-03-22 12:00','2009-03-10 12:00','2009-03-03 12:00','2009-02-11 12:00','2008-03-20 12:00','2008-03-10 12:00'))
_TnAccessPortConf_ObjectIdentity=ObjectIdentity
tnAccessPortConf=_TnAccessPortConf_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,1,1))
_TnAccessPortGroups_ObjectIdentity=ObjectIdentity
tnAccessPortGroups=_TnAccessPortGroups_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,1,1,1))
_TnAccessPortCompliances_ObjectIdentity=ObjectIdentity
tnAccessPortCompliances=_TnAccessPortCompliances_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,1,1,2))
_TnAccessPortObjs_ObjectIdentity=ObjectIdentity
tnAccessPortObjs=_TnAccessPortObjs_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,1,2))
_TnAccessPortTable_Object=MibTable
tnAccessPortTable=_TnAccessPortTable_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1))
if mibBuilder.loadTexts:tnAccessPortTable.setStatus(_A)
_TnAccessPortEntry_Object=MibTableRow
tnAccessPortEntry=_TnAccessPortEntry_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1))
tnAccessPortEntry.setIndexNames((0,_L,_M))
if mibBuilder.loadTexts:tnAccessPortEntry.setStatus(_A)
class _TnAccessPortDescr_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TnAccessPortDescr_Type.__name__=_F
_TnAccessPortDescr_Object=MibTableColumn
tnAccessPortDescr=_TnAccessPortDescr_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,1),_TnAccessPortDescr_Type())
tnAccessPortDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortDescr.setStatus(_A)
_TnAccessPortStatusLEDColor_Type=TropicLEDColorType
_TnAccessPortStatusLEDColor_Object=MibTableColumn
tnAccessPortStatusLEDColor=_TnAccessPortStatusLEDColor_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,2),_TnAccessPortStatusLEDColor_Type())
tnAccessPortStatusLEDColor.setMaxAccess(_D)
if mibBuilder.loadTexts:tnAccessPortStatusLEDColor.setStatus(_A)
_TnAccessPortStatusLEDState_Type=TropicLEDStateType
_TnAccessPortStatusLEDState_Object=MibTableColumn
tnAccessPortStatusLEDState=_TnAccessPortStatusLEDState_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,3),_TnAccessPortStatusLEDState_Type())
tnAccessPortStatusLEDState.setMaxAccess(_D)
if mibBuilder.loadTexts:tnAccessPortStatusLEDState.setStatus(_A)
class _TnAccessPortOperationalCapability_Type(TropicOperationalCapabilityType):defaultValue=1
_TnAccessPortOperationalCapability_Type.__name__=_O
_TnAccessPortOperationalCapability_Object=MibTableColumn
tnAccessPortOperationalCapability=_TnAccessPortOperationalCapability_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,4),_TnAccessPortOperationalCapability_Type())
tnAccessPortOperationalCapability.setMaxAccess(_D)
if mibBuilder.loadTexts:tnAccessPortOperationalCapability.setStatus(_A)
class _TnAccessPortStateQualifier_Type(TropicStateQualifierType):defaultBinValue='0'
_TnAccessPortStateQualifier_Type.__name__=_P
_TnAccessPortStateQualifier_Object=MibTableColumn
tnAccessPortStateQualifier=_TnAccessPortStateQualifier_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,5),_TnAccessPortStateQualifier_Type())
tnAccessPortStateQualifier.setMaxAccess(_D)
if mibBuilder.loadTexts:tnAccessPortStateQualifier.setStatus(_A)
class _TnAccessPortFarEndAddress_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_TnAccessPortFarEndAddress_Type.__name__=_F
_TnAccessPortFarEndAddress_Object=MibTableColumn
tnAccessPortFarEndAddress=_TnAccessPortFarEndAddress_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,6),_TnAccessPortFarEndAddress_Type())
tnAccessPortFarEndAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortFarEndAddress.setStatus(_A)
class _TnAccessPortFarEndIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_TnAccessPortFarEndIfIndex_Type.__name__=_G
_TnAccessPortFarEndIfIndex_Object=MibTableColumn
tnAccessPortFarEndIfIndex=_TnAccessPortFarEndIfIndex_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,7),_TnAccessPortFarEndIfIndex_Type())
tnAccessPortFarEndIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortFarEndIfIndex.setStatus(_A)
class _TnAccessPortFarEndType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5,6)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3),(_T,5),(_U,6)))
_TnAccessPortFarEndType_Type.__name__=_E
_TnAccessPortFarEndType_Object=MibTableColumn
tnAccessPortFarEndType=_TnAccessPortFarEndType_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,8),_TnAccessPortFarEndType_Type())
tnAccessPortFarEndType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortFarEndType.setStatus(_A)
class _TnAccessPortDirection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('bidirectional',1),('unidirectionalTx',2),('unidirectionalRx',3)))
_TnAccessPortDirection_Type.__name__=_E
_TnAccessPortDirection_Object=MibTableColumn
tnAccessPortDirection=_TnAccessPortDirection_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,9),_TnAccessPortDirection_Type())
tnAccessPortDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortDirection.setStatus(_A)
class _TnAccessPortAINS_Type(TruthValue):defaultValue=2
_TnAccessPortAINS_Type.__name__=_H
_TnAccessPortAINS_Object=MibTableColumn
tnAccessPortAINS=_TnAccessPortAINS_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,10),_TnAccessPortAINS_Type())
tnAccessPortAINS.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortAINS.setStatus(_A)
class _TnAccessPortAINSDebounceTime_Type(Integer32):defaultValue=-1
_TnAccessPortAINSDebounceTime_Type.__name__=_E
_TnAccessPortAINSDebounceTime_Object=MibTableColumn
tnAccessPortAINSDebounceTime=_TnAccessPortAINSDebounceTime_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,11),_TnAccessPortAINSDebounceTime_Type())
tnAccessPortAINSDebounceTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortAINSDebounceTime.setStatus(_A)
if mibBuilder.loadTexts:tnAccessPortAINSDebounceTime.setUnits(_V)
_TnAccessPortUsingSysAINSDebounceTime_Type=TruthValue
_TnAccessPortUsingSysAINSDebounceTime_Object=MibTableColumn
tnAccessPortUsingSysAINSDebounceTime=_TnAccessPortUsingSysAINSDebounceTime_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,12),_TnAccessPortUsingSysAINSDebounceTime_Type())
tnAccessPortUsingSysAINSDebounceTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortUsingSysAINSDebounceTime.setStatus(_A)
class _TnAccessPortAINSDebounceTimeRemaining_Type(Unsigned32):defaultValue=0
_TnAccessPortAINSDebounceTimeRemaining_Type.__name__=_K
_TnAccessPortAINSDebounceTimeRemaining_Object=MibTableColumn
tnAccessPortAINSDebounceTimeRemaining=_TnAccessPortAINSDebounceTimeRemaining_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,13),_TnAccessPortAINSDebounceTimeRemaining_Type())
tnAccessPortAINSDebounceTimeRemaining.setMaxAccess(_D)
if mibBuilder.loadTexts:tnAccessPortAINSDebounceTimeRemaining.setStatus(_A)
if mibBuilder.loadTexts:tnAccessPortAINSDebounceTimeRemaining.setUnits(_V)
class _TnAccessPortIsDomainEdgePort_Type(TruthValue):defaultValue=1
_TnAccessPortIsDomainEdgePort_Type.__name__=_H
_TnAccessPortIsDomainEdgePort_Object=MibTableColumn
tnAccessPortIsDomainEdgePort=_TnAccessPortIsDomainEdgePort_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,14),_TnAccessPortIsDomainEdgePort_Type())
tnAccessPortIsDomainEdgePort.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortIsDomainEdgePort.setStatus(_A)
class _TnAccessPortFarEndAddressConnFrom_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_TnAccessPortFarEndAddressConnFrom_Type.__name__=_F
_TnAccessPortFarEndAddressConnFrom_Object=MibTableColumn
tnAccessPortFarEndAddressConnFrom=_TnAccessPortFarEndAddressConnFrom_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,15),_TnAccessPortFarEndAddressConnFrom_Type())
tnAccessPortFarEndAddressConnFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortFarEndAddressConnFrom.setStatus(_A)
class _TnAccessPortFarEndIfIndexConnFrom_Type(InterfaceIndexOrZero):defaultValue=0
_TnAccessPortFarEndIfIndexConnFrom_Type.__name__=_G
_TnAccessPortFarEndIfIndexConnFrom_Object=MibTableColumn
tnAccessPortFarEndIfIndexConnFrom=_TnAccessPortFarEndIfIndexConnFrom_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,16),_TnAccessPortFarEndIfIndexConnFrom_Type())
tnAccessPortFarEndIfIndexConnFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortFarEndIfIndexConnFrom.setStatus(_A)
class _TnAccessPortFarEndTypeConnFrom_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5,6)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3),(_T,5),(_U,6)))
_TnAccessPortFarEndTypeConnFrom_Type.__name__=_E
_TnAccessPortFarEndTypeConnFrom_Object=MibTableColumn
tnAccessPortFarEndTypeConnFrom=_TnAccessPortFarEndTypeConnFrom_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,17),_TnAccessPortFarEndTypeConnFrom_Type())
tnAccessPortFarEndTypeConnFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortFarEndTypeConnFrom.setStatus(_A)
class _TnAccessPortExtAmpIpAddressIn_Type(IpAddress):defaultHexValue=_W
_TnAccessPortExtAmpIpAddressIn_Type.__name__=_J
_TnAccessPortExtAmpIpAddressIn_Object=MibTableColumn
tnAccessPortExtAmpIpAddressIn=_TnAccessPortExtAmpIpAddressIn_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,18),_TnAccessPortExtAmpIpAddressIn_Type())
tnAccessPortExtAmpIpAddressIn.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortExtAmpIpAddressIn.setStatus(_A)
class _TnAccessPortExtAmpIpAddressOut_Type(IpAddress):defaultHexValue=_W
_TnAccessPortExtAmpIpAddressOut_Type.__name__=_J
_TnAccessPortExtAmpIpAddressOut_Object=MibTableColumn
tnAccessPortExtAmpIpAddressOut=_TnAccessPortExtAmpIpAddressOut_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,19),_TnAccessPortExtAmpIpAddressOut_Type())
tnAccessPortExtAmpIpAddressOut.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortExtAmpIpAddressOut.setStatus(_A)
class _TnAccessPortWtocmConnLoss_Type(Integer32):defaultValue=0
_TnAccessPortWtocmConnLoss_Type.__name__=_E
_TnAccessPortWtocmConnLoss_Object=MibTableColumn
tnAccessPortWtocmConnLoss=_TnAccessPortWtocmConnLoss_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,20),_TnAccessPortWtocmConnLoss_Type())
tnAccessPortWtocmConnLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortWtocmConnLoss.setStatus(_A)
if mibBuilder.loadTexts:tnAccessPortWtocmConnLoss.setUnits('mB')
class _TnAccessPortWtocmConnAddress_Type(InterfaceIndexOrZero):defaultValue=0
_TnAccessPortWtocmConnAddress_Type.__name__=_G
_TnAccessPortWtocmConnAddress_Object=MibTableColumn
tnAccessPortWtocmConnAddress=_TnAccessPortWtocmConnAddress_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,21),_TnAccessPortWtocmConnAddress_Type())
tnAccessPortWtocmConnAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortWtocmConnAddress.setStatus(_A)
class _TnAccessPortOppDirectionPortAddress_Type(InterfaceIndexOrZero):defaultValue=0
_TnAccessPortOppDirectionPortAddress_Type.__name__=_G
_TnAccessPortOppDirectionPortAddress_Object=MibTableColumn
tnAccessPortOppDirectionPortAddress=_TnAccessPortOppDirectionPortAddress_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,22),_TnAccessPortOppDirectionPortAddress_Type())
tnAccessPortOppDirectionPortAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortOppDirectionPortAddress.setStatus(_A)
class _TnAccessPortIsValidInternalOTSXcEndpoint_Type(TruthValue):defaultValue=2
_TnAccessPortIsValidInternalOTSXcEndpoint_Type.__name__=_H
_TnAccessPortIsValidInternalOTSXcEndpoint_Object=MibTableColumn
tnAccessPortIsValidInternalOTSXcEndpoint=_TnAccessPortIsValidInternalOTSXcEndpoint_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,23),_TnAccessPortIsValidInternalOTSXcEndpoint_Type())
tnAccessPortIsValidInternalOTSXcEndpoint.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortIsValidInternalOTSXcEndpoint.setStatus(_A)
class _TnAccessPortWtDomainNumber_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,19))
_TnAccessPortWtDomainNumber_Type.__name__=_E
_TnAccessPortWtDomainNumber_Object=MibTableColumn
tnAccessPortWtDomainNumber=_TnAccessPortWtDomainNumber_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,24),_TnAccessPortWtDomainNumber_Type())
tnAccessPortWtDomainNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortWtDomainNumber.setStatus(_A)
_TnAccessPortHasMpoConnector_Type=TruthValue
_TnAccessPortHasMpoConnector_Object=MibTableColumn
tnAccessPortHasMpoConnector=_TnAccessPortHasMpoConnector_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,25),_TnAccessPortHasMpoConnector_Type())
tnAccessPortHasMpoConnector.setMaxAccess(_D)
if mibBuilder.loadTexts:tnAccessPortHasMpoConnector.setStatus(_A)
_TnAccessPortMpoConnectorPortOutIfIndex_Type=InterfaceIndexOrZero
_TnAccessPortMpoConnectorPortOutIfIndex_Object=MibTableColumn
tnAccessPortMpoConnectorPortOutIfIndex=_TnAccessPortMpoConnectorPortOutIfIndex_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,26),_TnAccessPortMpoConnectorPortOutIfIndex_Type())
tnAccessPortMpoConnectorPortOutIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tnAccessPortMpoConnectorPortOutIfIndex.setStatus(_A)
_TnAccessPortMpoConnectorPortInIfIndex_Type=InterfaceIndexOrZero
_TnAccessPortMpoConnectorPortInIfIndex_Object=MibTableColumn
tnAccessPortMpoConnectorPortInIfIndex=_TnAccessPortMpoConnectorPortInIfIndex_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,27),_TnAccessPortMpoConnectorPortInIfIndex_Type())
tnAccessPortMpoConnectorPortInIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tnAccessPortMpoConnectorPortInIfIndex.setStatus(_A)
_TnAccessPortIsMpo_Type=TruthValue
_TnAccessPortIsMpo_Object=MibTableColumn
tnAccessPortIsMpo=_TnAccessPortIsMpo_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,28),_TnAccessPortIsMpo_Type())
tnAccessPortIsMpo.setMaxAccess(_D)
if mibBuilder.loadTexts:tnAccessPortIsMpo.setStatus(_A)
class _TnAccessPortMonOcmConnAddress_Type(InterfaceIndexOrZero):defaultValue=0
_TnAccessPortMonOcmConnAddress_Type.__name__=_G
_TnAccessPortMonOcmConnAddress_Object=MibTableColumn
tnAccessPortMonOcmConnAddress=_TnAccessPortMonOcmConnAddress_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,29),_TnAccessPortMonOcmConnAddress_Type())
tnAccessPortMonOcmConnAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortMonOcmConnAddress.setStatus(_A)
class _TnAccessPortAlmProfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_TnAccessPortAlmProfName_Type.__name__=_I
_TnAccessPortAlmProfName_Object=MibTableColumn
tnAccessPortAlmProfName=_TnAccessPortAlmProfName_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,30),_TnAccessPortAlmProfName_Type())
tnAccessPortAlmProfName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortAlmProfName.setStatus(_A)
_TnAccessPortmfcTemperature_Type=Integer32
_TnAccessPortmfcTemperature_Object=MibTableColumn
tnAccessPortmfcTemperature=_TnAccessPortmfcTemperature_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,31),_TnAccessPortmfcTemperature_Type())
tnAccessPortmfcTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:tnAccessPortmfcTemperature.setStatus(_A)
if mibBuilder.loadTexts:tnAccessPortmfcTemperature.setUnits(_X)
class _TnAccessPortmfcNominalPressure_Type(Integer32):defaultValue=0
_TnAccessPortmfcNominalPressure_Type.__name__=_E
_TnAccessPortmfcNominalPressure_Object=MibTableColumn
tnAccessPortmfcNominalPressure=_TnAccessPortmfcNominalPressure_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,32),_TnAccessPortmfcNominalPressure_Type())
tnAccessPortmfcNominalPressure.setMaxAccess(_D)
if mibBuilder.loadTexts:tnAccessPortmfcNominalPressure.setStatus(_A)
class _TnAccessPortmfcDifferentialPressure_Type(Integer32):defaultValue=0
_TnAccessPortmfcDifferentialPressure_Type.__name__=_E
_TnAccessPortmfcDifferentialPressure_Object=MibTableColumn
tnAccessPortmfcDifferentialPressure=_TnAccessPortmfcDifferentialPressure_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,33),_TnAccessPortmfcDifferentialPressure_Type())
tnAccessPortmfcDifferentialPressure.setMaxAccess(_D)
if mibBuilder.loadTexts:tnAccessPortmfcDifferentialPressure.setStatus(_A)
_TnAccessFilterAmbientTemperature_Type=Integer32
_TnAccessFilterAmbientTemperature_Object=MibTableColumn
tnAccessFilterAmbientTemperature=_TnAccessFilterAmbientTemperature_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,34),_TnAccessFilterAmbientTemperature_Type())
tnAccessFilterAmbientTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:tnAccessFilterAmbientTemperature.setStatus(_A)
if mibBuilder.loadTexts:tnAccessFilterAmbientTemperature.setUnits(_X)
_TnAccessFilterPressure_Type=Integer32
_TnAccessFilterPressure_Object=MibTableColumn
tnAccessFilterPressure=_TnAccessFilterPressure_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,35),_TnAccessFilterPressure_Type())
tnAccessFilterPressure.setMaxAccess(_D)
if mibBuilder.loadTexts:tnAccessFilterPressure.setStatus(_A)
if mibBuilder.loadTexts:tnAccessFilterPressure.setUnits('Pa')
_TnAccessFilterRecorded_Type=Integer32
_TnAccessFilterRecorded_Object=MibTableColumn
tnAccessFilterRecorded=_TnAccessFilterRecorded_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,36),_TnAccessFilterRecorded_Type())
tnAccessFilterRecorded.setMaxAccess(_D)
if mibBuilder.loadTexts:tnAccessFilterRecorded.setStatus(_A)
if mibBuilder.loadTexts:tnAccessFilterRecorded.setUnits('Pa')
_TnAccessFilterCalibrated_Type=Integer32
_TnAccessFilterCalibrated_Object=MibTableColumn
tnAccessFilterCalibrated=_TnAccessFilterCalibrated_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,37),_TnAccessFilterCalibrated_Type())
tnAccessFilterCalibrated.setMaxAccess(_D)
if mibBuilder.loadTexts:tnAccessFilterCalibrated.setStatus(_A)
if mibBuilder.loadTexts:tnAccessFilterCalibrated.setUnits('Pa')
_TnAccessFilterAltitude_Type=Integer32
_TnAccessFilterAltitude_Object=MibTableColumn
tnAccessFilterAltitude=_TnAccessFilterAltitude_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,38),_TnAccessFilterAltitude_Type())
tnAccessFilterAltitude.setMaxAccess(_D)
if mibBuilder.loadTexts:tnAccessFilterAltitude.setStatus(_A)
if mibBuilder.loadTexts:tnAccessFilterAltitude.setUnits('kilometers')
_TnAccessFilterRecordTime_Type=TimeTicks
_TnAccessFilterRecordTime_Object=MibTableColumn
tnAccessFilterRecordTime=_TnAccessFilterRecordTime_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,39),_TnAccessFilterRecordTime_Type())
tnAccessFilterRecordTime.setMaxAccess(_D)
if mibBuilder.loadTexts:tnAccessFilterRecordTime.setStatus(_A)
_TnAccessFilterCalibrateTime_Type=TimeTicks
_TnAccessFilterCalibrateTime_Object=MibTableColumn
tnAccessFilterCalibrateTime=_TnAccessFilterCalibrateTime_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,40),_TnAccessFilterCalibrateTime_Type())
tnAccessFilterCalibrateTime.setMaxAccess(_D)
if mibBuilder.loadTexts:tnAccessFilterCalibrateTime.setStatus(_A)
_TnAccessFilterScheduledTime_Type=TimeTicks
_TnAccessFilterScheduledTime_Object=MibTableColumn
tnAccessFilterScheduledTime=_TnAccessFilterScheduledTime_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,41),_TnAccessFilterScheduledTime_Type())
tnAccessFilterScheduledTime.setMaxAccess(_D)
if mibBuilder.loadTexts:tnAccessFilterScheduledTime.setStatus(_A)
_TnAccessPortL2FarEndIfIndex_Type=InterfaceIndexOrZero
_TnAccessPortL2FarEndIfIndex_Object=MibTableColumn
tnAccessPortL2FarEndIfIndex=_TnAccessPortL2FarEndIfIndex_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,42),_TnAccessPortL2FarEndIfIndex_Type())
tnAccessPortL2FarEndIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tnAccessPortL2FarEndIfIndex.setStatus(_A)
_TnAccessPortL2FarEndMacAddress_Type=MacAddress
_TnAccessPortL2FarEndMacAddress_Object=MibTableColumn
tnAccessPortL2FarEndMacAddress=_TnAccessPortL2FarEndMacAddress_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,43),_TnAccessPortL2FarEndMacAddress_Type())
tnAccessPortL2FarEndMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:tnAccessPortL2FarEndMacAddress.setStatus(_A)
class _TnAccessPortDirectionCapability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('notInstalled',0),('singleBidi',1),('dualBidi',2),('rxOnly',3),('txOnly',4),('rxAndTx',5)))
_TnAccessPortDirectionCapability_Type.__name__=_E
_TnAccessPortDirectionCapability_Object=MibTableColumn
tnAccessPortDirectionCapability=_TnAccessPortDirectionCapability_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,44),_TnAccessPortDirectionCapability_Type())
tnAccessPortDirectionCapability.setMaxAccess(_D)
if mibBuilder.loadTexts:tnAccessPortDirectionCapability.setStatus(_A)
class _TnAccessPortCpriMappingType_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(6,7,8,9,10)));namedValues=NamedValues(*(('tunneling',6),('linecodeAware',7),('structureAware',8),('structureAwareControl',9),('nomapping',10)))
_TnAccessPortCpriMappingType_Type.__name__=_E
_TnAccessPortCpriMappingType_Object=MibTableColumn
tnAccessPortCpriMappingType=_TnAccessPortCpriMappingType_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,45),_TnAccessPortCpriMappingType_Type())
tnAccessPortCpriMappingType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortCpriMappingType.setStatus(_A)
class _TnAccessPortFecType_Type(AluWdmFecMode):defaultValue=1
_TnAccessPortFecType_Type.__name__=_N
_TnAccessPortFecType_Object=MibTableColumn
tnAccessPortFecType=_TnAccessPortFecType_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,46),_TnAccessPortFecType_Type())
tnAccessPortFecType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortFecType.setStatus(_A)
class _TnAccessPortFecBypassInd_Type(TruthValue):defaultValue=2
_TnAccessPortFecBypassInd_Type.__name__=_H
_TnAccessPortFecBypassInd_Object=MibTableColumn
tnAccessPortFecBypassInd=_TnAccessPortFecBypassInd_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,47),_TnAccessPortFecBypassInd_Type())
tnAccessPortFecBypassInd.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortFecBypassInd.setStatus(_A)
class _TnAccessPortCpriRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('master',1),('slave',2),('none',3)))
_TnAccessPortCpriRole_Type.__name__=_E
_TnAccessPortCpriRole_Object=MibTableColumn
tnAccessPortCpriRole=_TnAccessPortCpriRole_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,48),_TnAccessPortCpriRole_Type())
tnAccessPortCpriRole.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortCpriRole.setStatus(_A)
class _TnAccessPortAseMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unconfigured',1),('noNoise',2),('low',3),('standard',4)))
_TnAccessPortAseMode_Type.__name__=_E
_TnAccessPortAseMode_Object=MibTableColumn
tnAccessPortAseMode=_TnAccessPortAseMode_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,49),_TnAccessPortAseMode_Type())
tnAccessPortAseMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortAseMode.setStatus(_A)
class _TnAccessPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('undetermined',1),('in',2),('out',3)))
_TnAccessPortRole_Type.__name__=_E
_TnAccessPortRole_Object=MibTableColumn
tnAccessPortRole=_TnAccessPortRole_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,50),_TnAccessPortRole_Type())
tnAccessPortRole.setMaxAccess(_D)
if mibBuilder.loadTexts:tnAccessPortRole.setStatus(_A)
class _TnAccessPortFacilityDescriptorName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,45))
_TnAccessPortFacilityDescriptorName_Type.__name__=_F
_TnAccessPortFacilityDescriptorName_Object=MibTableColumn
tnAccessPortFacilityDescriptorName=_TnAccessPortFacilityDescriptorName_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,51),_TnAccessPortFacilityDescriptorName_Type())
tnAccessPortFacilityDescriptorName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortFacilityDescriptorName.setStatus(_A)
class _TnAccessPortFacilityDescriptorDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TnAccessPortFacilityDescriptorDesc_Type.__name__=_F
_TnAccessPortFacilityDescriptorDesc_Object=MibTableColumn
tnAccessPortFacilityDescriptorDesc=_TnAccessPortFacilityDescriptorDesc_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,52),_TnAccessPortFacilityDescriptorDesc_Type())
tnAccessPortFacilityDescriptorDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortFacilityDescriptorDesc.setStatus(_A)
class _TnAccessPortFacilityDescriptorCirId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,45))
_TnAccessPortFacilityDescriptorCirId_Type.__name__=_F
_TnAccessPortFacilityDescriptorCirId_Object=MibTableColumn
tnAccessPortFacilityDescriptorCirId=_TnAccessPortFacilityDescriptorCirId_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,53),_TnAccessPortFacilityDescriptorCirId_Type())
tnAccessPortFacilityDescriptorCirId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortFacilityDescriptorCirId.setStatus(_A)
class _TnAccessPortAlienWavebank_Type(TruthValue):defaultValue=2
_TnAccessPortAlienWavebank_Type.__name__=_H
_TnAccessPortAlienWavebank_Object=MibTableColumn
tnAccessPortAlienWavebank=_TnAccessPortAlienWavebank_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,54),_TnAccessPortAlienWavebank_Type())
tnAccessPortAlienWavebank.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortAlienWavebank.setStatus(_A)
class _TnAccessPortModuleReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noCmd',1),('warmReset',2),('coldReset',3),('forceReset',4)))
_TnAccessPortModuleReset_Type.__name__=_E
_TnAccessPortModuleReset_Object=MibTableColumn
tnAccessPortModuleReset=_TnAccessPortModuleReset_Object((1,3,6,1,4,1,7483,2,2,4,1,2,1,1,55),_TnAccessPortModuleReset_Type())
tnAccessPortModuleReset.setMaxAccess(_C)
if mibBuilder.loadTexts:tnAccessPortModuleReset.setStatus(_A)
_TnIfTable_Object=MibTable
tnIfTable=_TnIfTable_Object((1,3,6,1,4,1,7483,2,2,4,1,2,2))
if mibBuilder.loadTexts:tnIfTable.setStatus(_A)
_TnIfEntry_Object=MibTableRow
tnIfEntry=_TnIfEntry_Object((1,3,6,1,4,1,7483,2,2,4,1,2,2,1))
if mibBuilder.loadTexts:tnIfEntry.setStatus(_A)
_TnIfPhysicalLocation_Type=InterfaceIndex
_TnIfPhysicalLocation_Object=MibTableColumn
tnIfPhysicalLocation=_TnIfPhysicalLocation_Object((1,3,6,1,4,1,7483,2,2,4,1,2,2,1,1),_TnIfPhysicalLocation_Type())
tnIfPhysicalLocation.setMaxAccess(_D)
if mibBuilder.loadTexts:tnIfPhysicalLocation.setStatus(_A)
_TnIfType_Type=AluWdmTnIfType
_TnIfType_Object=MibTableColumn
tnIfType=_TnIfType_Object((1,3,6,1,4,1,7483,2,2,4,1,2,2,1,2),_TnIfType_Type())
tnIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnIfType.setStatus(_A)
class _TnIfSupportedTypes_Type(Bits):namedValues=NamedValues(*(('oc3',0),('oc12',1),('oc48',2),('oc192',3),('ots',4),('och',5),('otu1',6),('otu2',7),('gige',8),('tenGige',9),('stm1',10),('stm4',11),('stm16',12),('stm64',13),('fc1g',14),('fc2g',15),('fc4g',16),('fc10g',17),('cbr2g5',18),('cbr10g',19),('anyRate',20),('hdSdi',21),('fe',22),('fddi',23),('esCon',24),('dvbAsi',25),('dvi6000',26),('otu3',27),('oc768',28),('stm256',29),('otu4',30),('fc8g',31),('hundredGige',32),('sdsdi',33),('e1',34),('sdi3g',35),('dcn',36),('evoa',37),('fee',38),('oduptf',39),('ds1',40),('otu3e2',41),('otu2e',42),('fortyGige',43),('sdr',44),('ddr',45),('tod',46),('lagGroup',47),('otl44',48),('fc16g',49),('qdr',50),('bits',51),('oneTru',52),('otu4x2',53),('otu1f',54),('cbr10g3',55),('fortyGigeMLD',56),('interLaken',57),('otl410',58),('otu4x4',59),('otu4Half',60),('otu4Halfx5',61),('sensor',62),('xfi',63),('caui',64),('otu2ewaneth',65),('otu4waneth',66),('tengigelaneth',67),('hundredGigeLaneth',68),('gigeConv',69),('otu2eeth',70),('gigelaneth',71),('felaneth',72),('ethman',73),('ilkpif',74),('feed',75),('otu2eNimEth',76),('twentyFiveGbeLaneth',77),('otu4x2waneth',78),('otsi',79),('fourHundredGige',80),('cpri3',81),('cpri5',82),('cpri6',83),('cpri7',84),('cpri8',85),('cpri10',86),('obsai8',87),('obsai4',88),('tfgige',89),('cauiV2',90),('fc32g',91),('otuc4mld',92),('equipment',93),('cpri4',94),('tengigelaneth2g5ce',95)))
_TnIfSupportedTypes_Type.__name__='Bits'
_TnIfSupportedTypes_Object=MibTableColumn
tnIfSupportedTypes=_TnIfSupportedTypes_Object((1,3,6,1,4,1,7483,2,2,4,1,2,2,1,3),_TnIfSupportedTypes_Type())
tnIfSupportedTypes.setMaxAccess(_D)
if mibBuilder.loadTexts:tnIfSupportedTypes.setStatus(_A)
class _TnIfSupportedTypesAlternate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_TnIfSupportedTypesAlternate_Type.__name__=_I
_TnIfSupportedTypesAlternate_Object=MibTableColumn
tnIfSupportedTypesAlternate=_TnIfSupportedTypesAlternate_Object((1,3,6,1,4,1,7483,2,2,4,1,2,2,1,4),_TnIfSupportedTypesAlternate_Type())
tnIfSupportedTypesAlternate.setMaxAccess(_D)
if mibBuilder.loadTexts:tnIfSupportedTypesAlternate.setStatus(_A)
_TnIfForceAdminStatus_Type=TnCommand
_TnIfForceAdminStatus_Object=MibTableColumn
tnIfForceAdminStatus=_TnIfForceAdminStatus_Object((1,3,6,1,4,1,7483,2,2,4,1,2,2,1,5),_TnIfForceAdminStatus_Type())
tnIfForceAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnIfForceAdminStatus.setStatus(_A)
class _TnIfnumofTimeSlots_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,80))
_TnIfnumofTimeSlots_Type.__name__=_K
_TnIfnumofTimeSlots_Object=MibTableColumn
tnIfnumofTimeSlots=_TnIfnumofTimeSlots_Object((1,3,6,1,4,1,7483,2,2,4,1,2,2,1,6),_TnIfnumofTimeSlots_Type())
tnIfnumofTimeSlots.setMaxAccess(_D)
if mibBuilder.loadTexts:tnIfnumofTimeSlots.setStatus(_A)
class _TnIfAlmProfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_TnIfAlmProfName_Type.__name__=_I
_TnIfAlmProfName_Object=MibTableColumn
tnIfAlmProfName=_TnIfAlmProfName_Object((1,3,6,1,4,1,7483,2,2,4,1,2,2,1,7),_TnIfAlmProfName_Type())
tnIfAlmProfName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnIfAlmProfName.setStatus(_A)
_TnAccessPortScalarObjs_ObjectIdentity=ObjectIdentity
tnAccessPortScalarObjs=_TnAccessPortScalarObjs_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,1,2,3))
_TnSysTopology_ObjectIdentity=ObjectIdentity
tnSysTopology=_TnSysTopology_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,1,2,3,1))
class _TnSysTopologyAudit_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TnSysTopologyAudit_Type.__name__=_F
_TnSysTopologyAudit_Object=MibScalar
tnSysTopologyAudit=_TnSysTopologyAudit_Object((1,3,6,1,4,1,7483,2,2,4,1,2,3,1,1),_TnSysTopologyAudit_Type())
tnSysTopologyAudit.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSysTopologyAudit.setStatus(_A)
ifEntry.registerAugmentions((_B,_Y))
tnIfEntry.setIndexNames(*ifEntry.getIndexNames())
tnAccessPortGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,4,1,1,1,1))
tnAccessPortGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR)))
if mibBuilder.loadTexts:tnAccessPortGroup.setStatus(_A)
tnIfGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,4,1,1,1,2))
tnIfGroup.setObjects(*((_B,_AS),(_B,'tnIfType'),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX)))
if mibBuilder.loadTexts:tnIfGroup.setStatus(_A)
tnSysTopologyGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,4,1,1,1,3))
tnSysTopologyGroup.setObjects((_B,_AY))
if mibBuilder.loadTexts:tnSysTopologyGroup.setStatus(_A)
tnAccessPortCompliance=ModuleCompliance((1,3,6,1,4,1,7483,2,2,4,1,1,2,1))
tnAccessPortCompliance.setObjects(*((_B,_AZ),(_B,_Aa),(_B,_Ab)))
if mibBuilder.loadTexts:tnAccessPortCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'tnAccessPortMibModules':tnAccessPortMibModules,'tnAccessPortConf':tnAccessPortConf,'tnAccessPortGroups':tnAccessPortGroups,_AZ:tnAccessPortGroup,_Aa:tnIfGroup,_Ab:tnSysTopologyGroup,'tnAccessPortCompliances':tnAccessPortCompliances,'tnAccessPortCompliance':tnAccessPortCompliance,'tnAccessPortObjs':tnAccessPortObjs,'tnAccessPortTable':tnAccessPortTable,'tnAccessPortEntry':tnAccessPortEntry,_Z:tnAccessPortDescr,_a:tnAccessPortStatusLEDColor,_b:tnAccessPortStatusLEDState,_c:tnAccessPortOperationalCapability,_d:tnAccessPortStateQualifier,_e:tnAccessPortFarEndAddress,_f:tnAccessPortFarEndIfIndex,_g:tnAccessPortFarEndType,_h:tnAccessPortDirection,_i:tnAccessPortAINS,_j:tnAccessPortAINSDebounceTime,_k:tnAccessPortUsingSysAINSDebounceTime,_l:tnAccessPortAINSDebounceTimeRemaining,_m:tnAccessPortIsDomainEdgePort,_n:tnAccessPortFarEndAddressConnFrom,_o:tnAccessPortFarEndIfIndexConnFrom,_p:tnAccessPortFarEndTypeConnFrom,_q:tnAccessPortExtAmpIpAddressIn,_r:tnAccessPortExtAmpIpAddressOut,_s:tnAccessPortWtocmConnLoss,_t:tnAccessPortWtocmConnAddress,_u:tnAccessPortOppDirectionPortAddress,_v:tnAccessPortIsValidInternalOTSXcEndpoint,_w:tnAccessPortWtDomainNumber,_x:tnAccessPortHasMpoConnector,_y:tnAccessPortMpoConnectorPortOutIfIndex,_z:tnAccessPortMpoConnectorPortInIfIndex,_A0:tnAccessPortIsMpo,_A1:tnAccessPortMonOcmConnAddress,_A2:tnAccessPortAlmProfName,_A3:tnAccessPortmfcTemperature,_A4:tnAccessPortmfcNominalPressure,_A5:tnAccessPortmfcDifferentialPressure,_A6:tnAccessFilterAmbientTemperature,_A7:tnAccessFilterPressure,_A8:tnAccessFilterRecorded,_A9:tnAccessFilterCalibrated,_AA:tnAccessFilterAltitude,_AB:tnAccessFilterRecordTime,_AC:tnAccessFilterCalibrateTime,_AD:tnAccessFilterScheduledTime,_AE:tnAccessPortL2FarEndIfIndex,_AF:tnAccessPortL2FarEndMacAddress,_AG:tnAccessPortDirectionCapability,_AH:tnAccessPortCpriMappingType,_AI:tnAccessPortFecType,_AJ:tnAccessPortFecBypassInd,_AK:tnAccessPortCpriRole,_AL:tnAccessPortAseMode,_AM:tnAccessPortRole,_AN:tnAccessPortFacilityDescriptorName,_AO:tnAccessPortFacilityDescriptorDesc,_AP:tnAccessPortFacilityDescriptorCirId,_AQ:tnAccessPortAlienWavebank,_AR:tnAccessPortModuleReset,'tnIfTable':tnIfTable,_Y:tnIfEntry,_AS:tnIfPhysicalLocation,'tnIfType':tnIfType,_AT:tnIfSupportedTypes,_AU:tnIfSupportedTypesAlternate,_AV:tnIfForceAdminStatus,_AW:tnIfnumofTimeSlots,_AX:tnIfAlmProfName,'tnAccessPortScalarObjs':tnAccessPortScalarObjs,'tnSysTopology':tnSysTopology,_AY:tnSysTopologyAudit})