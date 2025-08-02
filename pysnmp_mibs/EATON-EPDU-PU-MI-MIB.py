_BZ='thresholdGroupOld'
_BY='measurementGroup'
_BX='unitGroup'
_BW='thresholdGroup'
_BV='lowCurrentThreshold8old'
_BU='lowCurrentThreshold7old'
_BT='lowCurrentThreshold6old'
_BS='lowCurrentThreshold5old'
_BR='lowCurrentThreshold4old'
_BQ='lowCurrentThreshold3old'
_BP='lowCurrentThreshold2old'
_BO='lowCurrentThreshold1old'
_BN='highCurrentThreshold8old'
_BM='highCurrentThreshold7old'
_BL='highCurrentThreshold6old'
_BK='highCurrentThreshold5old'
_BJ='highCurrentThreshold4old'
_BI='highCurrentThreshold3old'
_BH='highCurrentThreshold2old'
_BG='highCurrentThreshold1old'
_BF='lowTempThreshold2'
_BE='lowTempThreshold1'
_BD='lowCurrentThreshold9'
_BC='lowCurrentThreshold8'
_BB='lowCurrentThreshold7'
_BA='lowCurrentThreshold6'
_B9='lowCurrentThreshold5'
_B8='lowCurrentThreshold4'
_B7='lowCurrentThreshold32'
_B6='lowCurrentThreshold31'
_B5='lowCurrentThreshold30'
_B4='lowCurrentThreshold3'
_B3='lowCurrentThreshold29'
_B2='lowCurrentThreshold28'
_B1='lowCurrentThreshold27'
_B0='lowCurrentThreshold26'
_A_='lowCurrentThreshold25'
_Az='lowCurrentThreshold24'
_Ay='lowCurrentThreshold23'
_Ax='lowCurrentThreshold22'
_Aw='lowCurrentThreshold21'
_Av='lowCurrentThreshold20'
_Au='lowCurrentThreshold2'
_At='lowCurrentThreshold19'
_As='lowCurrentThreshold18'
_Ar='lowCurrentThreshold17'
_Aq='lowCurrentThreshold16'
_Ap='lowCurrentThreshold15'
_Ao='lowCurrentThreshold14'
_An='lowCurrentThreshold13'
_Am='lowCurrentThreshold12'
_Al='lowCurrentThreshold11'
_Ak='lowCurrentThreshold10'
_Aj='lowCurrentThreshold1'
_Ai='highTempThreshold2'
_Ah='highTempThreshold1'
_Ag='highCurrentThreshold9'
_Af='highCurrentThreshold8'
_Ae='highCurrentThreshold7'
_Ad='highCurrentThreshold6'
_Ac='highCurrentThreshold5'
_Ab='highCurrentThreshold4'
_Aa='highCurrentThreshold32'
_AZ='highCurrentThreshold31'
_AY='highCurrentThreshold30'
_AX='highCurrentThreshold3'
_AW='highCurrentThreshold29'
_AV='highCurrentThreshold28'
_AU='highCurrentThreshold27'
_AT='highCurrentThreshold26'
_AS='highCurrentThreshold25'
_AR='highCurrentThreshold24'
_AQ='highCurrentThreshold23'
_AP='highCurrentThreshold22'
_AO='highCurrentThreshold21'
_AN='highCurrentThreshold20'
_AM='highCurrentThreshold2'
_AL='highCurrentThreshold19'
_AK='highCurrentThreshold18'
_AJ='highCurrentThreshold17'
_AI='highCurrentThreshold16'
_AH='highCurrentThreshold15'
_AG='highCurrentThreshold14'
_AF='highCurrentThreshold13'
_AE='highCurrentThreshold12'
_AD='highCurrentThreshold11'
_AC='highCurrentThreshold10'
_AB='highCurrentThreshold1'
_AA='tempChan2'
_A9='tempChan1'
_A8='unitSubnetMask'
_A7='unitMACAddress'
_A6='unitIPAddress'
_A5='unitGateway'
_A4='trapDestIP'
_A3='temperature2Enable'
_A2='temperature1Enable'
_A1='temp2Name'
_A0='temp1Name'
_z='numCurrentChannels'
_y='firmwareRevision'
_x='currentMonitorType'
_w='chan9Name'
_v='chan8Name'
_u='chan7Name'
_t='chan6Name'
_s='chan5Name'
_r='chan4Name'
_q='chan3Name'
_p='chan32Name'
_o='chan31Name'
_n='chan30Name'
_m='chan2Name'
_l='chan29Name'
_k='chan28Name'
_j='chan27Name'
_i='chan26Name'
_h='chan25Name'
_g='chan24Name'
_f='chan23Name'
_e='chan22Name'
_d='chan21Name'
_c='chan20Name'
_b='chan1Name'
_a='chan19Name'
_Z='chan18Name'
_Y='chan17Name'
_X='chan16Name'
_W='chan15Name'
_V='chan14Name'
_U='chan13Name'
_T='chan12Name'
_S='chan11Name'
_R='chan10Name'
_Q='assetID'
_P='alertEmailAddress'
_O='mailServerIP'
_N='Degrees Fahrenheit'
_M='enabled'
_L='disabled'
_K='Degrees'
_J='Amps or Degrees Farenheit'
_I='deprecated'
_H='0.1 Amps RMS'
_G='OctetString'
_F='read-only'
_E='Integer32'
_D='Amps'
_C='read-write'
_B='current'
_A='EATON-EPDU-PU-MI-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pulizzi=ModuleIdentity((1,3,6,1,4,1,20677))
if mibBuilder.loadTexts:pulizzi.setRevisions(('2010-02-03 12:00','2009-01-08 12:00','2008-12-19 12:00','2008-11-06 12:00','2008-08-25 12:00','2008-07-09 12:00'))
_Monitoredepdu_ObjectIdentity=ObjectIdentity
monitoredepdu=_Monitoredepdu_ObjectIdentity((1,3,6,1,4,1,20677,3))
_Epdum1_ObjectIdentity=ObjectIdentity
epdum1=_Epdum1_ObjectIdentity((1,3,6,1,4,1,20677,3,1))
_Epdum11_ObjectIdentity=ObjectIdentity
epdum11=_Epdum11_ObjectIdentity((1,3,6,1,4,1,20677,3,1,1))
_UnitConfig_ObjectIdentity=ObjectIdentity
unitConfig=_UnitConfig_ObjectIdentity((1,3,6,1,4,1,20677,3,1,1,1))
_Uptime_Type=TimeTicks
_Uptime_Object=MibScalar
uptime=_Uptime_Object((1,3,6,1,4,1,20677,3,1,1,1,1),_Uptime_Type())
uptime.setMaxAccess(_F)
if mibBuilder.loadTexts:uptime.setStatus(_B)
class _UnitName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_UnitName_Type.__name__=_G
_UnitName_Object=MibScalar
unitName=_UnitName_Object((1,3,6,1,4,1,20677,3,1,1,1,2),_UnitName_Type())
unitName.setMaxAccess(_C)
if mibBuilder.loadTexts:unitName.setStatus(_B)
_LowCurrentThreshold1old_Type=Integer32
_LowCurrentThreshold1old_Object=MibScalar
lowCurrentThreshold1old=_LowCurrentThreshold1old_Object((1,3,6,1,4,1,20677,3,1,1,1,3),_LowCurrentThreshold1old_Type())
lowCurrentThreshold1old.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold1old.setStatus(_I)
if mibBuilder.loadTexts:lowCurrentThreshold1old.setUnits(_D)
_LowCurrentThreshold2old_Type=Integer32
_LowCurrentThreshold2old_Object=MibScalar
lowCurrentThreshold2old=_LowCurrentThreshold2old_Object((1,3,6,1,4,1,20677,3,1,1,1,4),_LowCurrentThreshold2old_Type())
lowCurrentThreshold2old.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold2old.setStatus(_I)
if mibBuilder.loadTexts:lowCurrentThreshold2old.setUnits(_D)
_LowCurrentThreshold3old_Type=Integer32
_LowCurrentThreshold3old_Object=MibScalar
lowCurrentThreshold3old=_LowCurrentThreshold3old_Object((1,3,6,1,4,1,20677,3,1,1,1,5),_LowCurrentThreshold3old_Type())
lowCurrentThreshold3old.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold3old.setStatus(_I)
if mibBuilder.loadTexts:lowCurrentThreshold3old.setUnits(_D)
_LowCurrentThreshold4old_Type=Integer32
_LowCurrentThreshold4old_Object=MibScalar
lowCurrentThreshold4old=_LowCurrentThreshold4old_Object((1,3,6,1,4,1,20677,3,1,1,1,6),_LowCurrentThreshold4old_Type())
lowCurrentThreshold4old.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold4old.setStatus(_I)
if mibBuilder.loadTexts:lowCurrentThreshold4old.setUnits(_D)
_LowCurrentThreshold5old_Type=Integer32
_LowCurrentThreshold5old_Object=MibScalar
lowCurrentThreshold5old=_LowCurrentThreshold5old_Object((1,3,6,1,4,1,20677,3,1,1,1,7),_LowCurrentThreshold5old_Type())
lowCurrentThreshold5old.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold5old.setStatus(_I)
if mibBuilder.loadTexts:lowCurrentThreshold5old.setUnits(_D)
_LowCurrentThreshold6old_Type=Integer32
_LowCurrentThreshold6old_Object=MibScalar
lowCurrentThreshold6old=_LowCurrentThreshold6old_Object((1,3,6,1,4,1,20677,3,1,1,1,8),_LowCurrentThreshold6old_Type())
lowCurrentThreshold6old.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold6old.setStatus(_I)
if mibBuilder.loadTexts:lowCurrentThreshold6old.setUnits(_D)
_LowCurrentThreshold7old_Type=Integer32
_LowCurrentThreshold7old_Object=MibScalar
lowCurrentThreshold7old=_LowCurrentThreshold7old_Object((1,3,6,1,4,1,20677,3,1,1,1,9),_LowCurrentThreshold7old_Type())
lowCurrentThreshold7old.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold7old.setStatus(_I)
if mibBuilder.loadTexts:lowCurrentThreshold7old.setUnits(_J)
_LowCurrentThreshold8old_Type=Integer32
_LowCurrentThreshold8old_Object=MibScalar
lowCurrentThreshold8old=_LowCurrentThreshold8old_Object((1,3,6,1,4,1,20677,3,1,1,1,10),_LowCurrentThreshold8old_Type())
lowCurrentThreshold8old.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold8old.setStatus(_I)
if mibBuilder.loadTexts:lowCurrentThreshold8old.setUnits(_J)
_HighCurrentThreshold1old_Type=Integer32
_HighCurrentThreshold1old_Object=MibScalar
highCurrentThreshold1old=_HighCurrentThreshold1old_Object((1,3,6,1,4,1,20677,3,1,1,1,11),_HighCurrentThreshold1old_Type())
highCurrentThreshold1old.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold1old.setStatus(_I)
if mibBuilder.loadTexts:highCurrentThreshold1old.setUnits(_D)
_HighCurrentThreshold2old_Type=Integer32
_HighCurrentThreshold2old_Object=MibScalar
highCurrentThreshold2old=_HighCurrentThreshold2old_Object((1,3,6,1,4,1,20677,3,1,1,1,12),_HighCurrentThreshold2old_Type())
highCurrentThreshold2old.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold2old.setStatus(_I)
if mibBuilder.loadTexts:highCurrentThreshold2old.setUnits(_D)
_HighCurrentThreshold3old_Type=Integer32
_HighCurrentThreshold3old_Object=MibScalar
highCurrentThreshold3old=_HighCurrentThreshold3old_Object((1,3,6,1,4,1,20677,3,1,1,1,13),_HighCurrentThreshold3old_Type())
highCurrentThreshold3old.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold3old.setStatus(_I)
if mibBuilder.loadTexts:highCurrentThreshold3old.setUnits(_D)
_HighCurrentThreshold4old_Type=Integer32
_HighCurrentThreshold4old_Object=MibScalar
highCurrentThreshold4old=_HighCurrentThreshold4old_Object((1,3,6,1,4,1,20677,3,1,1,1,14),_HighCurrentThreshold4old_Type())
highCurrentThreshold4old.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold4old.setStatus(_I)
if mibBuilder.loadTexts:highCurrentThreshold4old.setUnits(_D)
_HighCurrentThreshold5old_Type=Integer32
_HighCurrentThreshold5old_Object=MibScalar
highCurrentThreshold5old=_HighCurrentThreshold5old_Object((1,3,6,1,4,1,20677,3,1,1,1,15),_HighCurrentThreshold5old_Type())
highCurrentThreshold5old.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold5old.setStatus(_I)
if mibBuilder.loadTexts:highCurrentThreshold5old.setUnits(_D)
_HighCurrentThreshold6old_Type=Integer32
_HighCurrentThreshold6old_Object=MibScalar
highCurrentThreshold6old=_HighCurrentThreshold6old_Object((1,3,6,1,4,1,20677,3,1,1,1,16),_HighCurrentThreshold6old_Type())
highCurrentThreshold6old.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold6old.setStatus(_I)
if mibBuilder.loadTexts:highCurrentThreshold6old.setUnits(_D)
_HighCurrentThreshold7old_Type=Integer32
_HighCurrentThreshold7old_Object=MibScalar
highCurrentThreshold7old=_HighCurrentThreshold7old_Object((1,3,6,1,4,1,20677,3,1,1,1,17),_HighCurrentThreshold7old_Type())
highCurrentThreshold7old.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold7old.setStatus(_I)
if mibBuilder.loadTexts:highCurrentThreshold7old.setUnits(_J)
_HighCurrentThreshold8old_Type=Integer32
_HighCurrentThreshold8old_Object=MibScalar
highCurrentThreshold8old=_HighCurrentThreshold8old_Object((1,3,6,1,4,1,20677,3,1,1,1,18),_HighCurrentThreshold8old_Type())
highCurrentThreshold8old.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold8old.setStatus(_I)
if mibBuilder.loadTexts:highCurrentThreshold8old.setUnits(_J)
class _Temperature1Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_Temperature1Enable_Type.__name__=_E
_Temperature1Enable_Object=MibScalar
temperature1Enable=_Temperature1Enable_Object((1,3,6,1,4,1,20677,3,1,1,1,19),_Temperature1Enable_Type())
temperature1Enable.setMaxAccess(_C)
if mibBuilder.loadTexts:temperature1Enable.setStatus(_B)
class _Temperature2Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_Temperature2Enable_Type.__name__=_E
_Temperature2Enable_Object=MibScalar
temperature2Enable=_Temperature2Enable_Object((1,3,6,1,4,1,20677,3,1,1,1,20),_Temperature2Enable_Type())
temperature2Enable.setMaxAccess(_C)
if mibBuilder.loadTexts:temperature2Enable.setStatus(_B)
_FirmwareRevision_Type=OctetString
_FirmwareRevision_Object=MibScalar
firmwareRevision=_FirmwareRevision_Object((1,3,6,1,4,1,20677,3,1,1,1,21),_FirmwareRevision_Type())
firmwareRevision.setMaxAccess(_F)
if mibBuilder.loadTexts:firmwareRevision.setStatus(_B)
class _AssetID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,19))
_AssetID_Type.__name__=_G
_AssetID_Object=MibScalar
assetID=_AssetID_Object((1,3,6,1,4,1,20677,3,1,1,1,22),_AssetID_Type())
assetID.setMaxAccess(_C)
if mibBuilder.loadTexts:assetID.setStatus(_B)
_NumCurrentChannels_Type=Integer32
_NumCurrentChannels_Object=MibScalar
numCurrentChannels=_NumCurrentChannels_Object((1,3,6,1,4,1,20677,3,1,1,1,23),_NumCurrentChannels_Type())
numCurrentChannels.setMaxAccess(_F)
if mibBuilder.loadTexts:numCurrentChannels.setStatus(_B)
class _CurrentMonitorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('totalUnitCurrent',1),('branchCurrent',2),('outletCurrent',3),('threePhaseCurrent',4),('splitPhaseCurrent',5),('singlePhaseWithBranch',6),('threePhaseWithBranch',7),('splitPhaseWithBranch',8)))
_CurrentMonitorType_Type.__name__=_E
_CurrentMonitorType_Object=MibScalar
currentMonitorType=_CurrentMonitorType_Object((1,3,6,1,4,1,20677,3,1,1,1,24),_CurrentMonitorType_Type())
currentMonitorType.setMaxAccess(_F)
if mibBuilder.loadTexts:currentMonitorType.setStatus(_B)
_NetworkSettings_ObjectIdentity=ObjectIdentity
networkSettings=_NetworkSettings_ObjectIdentity((1,3,6,1,4,1,20677,3,1,1,2))
_UnitIPAddress_Type=IpAddress
_UnitIPAddress_Object=MibScalar
unitIPAddress=_UnitIPAddress_Object((1,3,6,1,4,1,20677,3,1,1,2,1),_UnitIPAddress_Type())
unitIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:unitIPAddress.setStatus(_B)
_UnitSubnetMask_Type=IpAddress
_UnitSubnetMask_Object=MibScalar
unitSubnetMask=_UnitSubnetMask_Object((1,3,6,1,4,1,20677,3,1,1,2,2),_UnitSubnetMask_Type())
unitSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:unitSubnetMask.setStatus(_B)
_UnitGateway_Type=IpAddress
_UnitGateway_Object=MibScalar
unitGateway=_UnitGateway_Object((1,3,6,1,4,1,20677,3,1,1,2,3),_UnitGateway_Type())
unitGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:unitGateway.setStatus(_B)
_UnitMACAddress_Type=OctetString
_UnitMACAddress_Object=MibScalar
unitMACAddress=_UnitMACAddress_Object((1,3,6,1,4,1,20677,3,1,1,2,4),_UnitMACAddress_Type())
unitMACAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:unitMACAddress.setStatus(_B)
_TrapDestIP_Type=IpAddress
_TrapDestIP_Object=MibScalar
trapDestIP=_TrapDestIP_Object((1,3,6,1,4,1,20677,3,1,1,2,5),_TrapDestIP_Type())
trapDestIP.setMaxAccess(_C)
if mibBuilder.loadTexts:trapDestIP.setStatus(_B)
_MailServerIP_Type=IpAddress
_MailServerIP_Object=MibScalar
mailServerIP=_MailServerIP_Object((1,3,6,1,4,1,20677,3,1,1,2,6),_MailServerIP_Type())
mailServerIP.setMaxAccess(_C)
if mibBuilder.loadTexts:mailServerIP.setStatus(_B)
class _AlertEmailAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,49))
_AlertEmailAddress_Type.__name__=_G
_AlertEmailAddress_Object=MibScalar
alertEmailAddress=_AlertEmailAddress_Object((1,3,6,1,4,1,20677,3,1,1,2,7),_AlertEmailAddress_Type())
alertEmailAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:alertEmailAddress.setStatus(_B)
_Measurements_ObjectIdentity=ObjectIdentity
measurements=_Measurements_ObjectIdentity((1,3,6,1,4,1,20677,3,1,1,3))
_Chan1_Type=Integer32
_Chan1_Object=MibScalar
chan1=_Chan1_Object((1,3,6,1,4,1,20677,3,1,1,3,1),_Chan1_Type())
chan1.setMaxAccess(_F)
if mibBuilder.loadTexts:chan1.setStatus(_B)
if mibBuilder.loadTexts:chan1.setUnits(_H)
_Chan2_Type=Integer32
_Chan2_Object=MibScalar
chan2=_Chan2_Object((1,3,6,1,4,1,20677,3,1,1,3,2),_Chan2_Type())
chan2.setMaxAccess(_F)
if mibBuilder.loadTexts:chan2.setStatus(_B)
if mibBuilder.loadTexts:chan2.setUnits(_H)
_Chan3_Type=Integer32
_Chan3_Object=MibScalar
chan3=_Chan3_Object((1,3,6,1,4,1,20677,3,1,1,3,3),_Chan3_Type())
chan3.setMaxAccess(_F)
if mibBuilder.loadTexts:chan3.setStatus(_B)
if mibBuilder.loadTexts:chan3.setUnits(_H)
_Chan4_Type=Integer32
_Chan4_Object=MibScalar
chan4=_Chan4_Object((1,3,6,1,4,1,20677,3,1,1,3,4),_Chan4_Type())
chan4.setMaxAccess(_F)
if mibBuilder.loadTexts:chan4.setStatus(_B)
if mibBuilder.loadTexts:chan4.setUnits(_H)
_Chan5_Type=Integer32
_Chan5_Object=MibScalar
chan5=_Chan5_Object((1,3,6,1,4,1,20677,3,1,1,3,5),_Chan5_Type())
chan5.setMaxAccess(_F)
if mibBuilder.loadTexts:chan5.setStatus(_B)
if mibBuilder.loadTexts:chan5.setUnits(_H)
_Chan6_Type=Integer32
_Chan6_Object=MibScalar
chan6=_Chan6_Object((1,3,6,1,4,1,20677,3,1,1,3,6),_Chan6_Type())
chan6.setMaxAccess(_F)
if mibBuilder.loadTexts:chan6.setStatus(_B)
if mibBuilder.loadTexts:chan6.setUnits(_H)
_Chan7_Type=Integer32
_Chan7_Object=MibScalar
chan7=_Chan7_Object((1,3,6,1,4,1,20677,3,1,1,3,7),_Chan7_Type())
chan7.setMaxAccess(_F)
if mibBuilder.loadTexts:chan7.setStatus(_B)
if mibBuilder.loadTexts:chan7.setUnits(_H)
_Chan8_Type=Integer32
_Chan8_Object=MibScalar
chan8=_Chan8_Object((1,3,6,1,4,1,20677,3,1,1,3,8),_Chan8_Type())
chan8.setMaxAccess(_F)
if mibBuilder.loadTexts:chan8.setStatus(_B)
if mibBuilder.loadTexts:chan8.setUnits(_H)
_Chan9_Type=Integer32
_Chan9_Object=MibScalar
chan9=_Chan9_Object((1,3,6,1,4,1,20677,3,1,1,3,9),_Chan9_Type())
chan9.setMaxAccess(_F)
if mibBuilder.loadTexts:chan9.setStatus(_B)
if mibBuilder.loadTexts:chan9.setUnits(_H)
_Chan10_Type=Integer32
_Chan10_Object=MibScalar
chan10=_Chan10_Object((1,3,6,1,4,1,20677,3,1,1,3,10),_Chan10_Type())
chan10.setMaxAccess(_F)
if mibBuilder.loadTexts:chan10.setStatus(_B)
if mibBuilder.loadTexts:chan10.setUnits(_H)
_Chan11_Type=Integer32
_Chan11_Object=MibScalar
chan11=_Chan11_Object((1,3,6,1,4,1,20677,3,1,1,3,11),_Chan11_Type())
chan11.setMaxAccess(_F)
if mibBuilder.loadTexts:chan11.setStatus(_B)
if mibBuilder.loadTexts:chan11.setUnits(_H)
_Chan12_Type=Integer32
_Chan12_Object=MibScalar
chan12=_Chan12_Object((1,3,6,1,4,1,20677,3,1,1,3,12),_Chan12_Type())
chan12.setMaxAccess(_F)
if mibBuilder.loadTexts:chan12.setStatus(_B)
if mibBuilder.loadTexts:chan12.setUnits(_H)
_Chan13_Type=Integer32
_Chan13_Object=MibScalar
chan13=_Chan13_Object((1,3,6,1,4,1,20677,3,1,1,3,13),_Chan13_Type())
chan13.setMaxAccess(_F)
if mibBuilder.loadTexts:chan13.setStatus(_B)
if mibBuilder.loadTexts:chan13.setUnits(_H)
_Chan14_Type=Integer32
_Chan14_Object=MibScalar
chan14=_Chan14_Object((1,3,6,1,4,1,20677,3,1,1,3,14),_Chan14_Type())
chan14.setMaxAccess(_F)
if mibBuilder.loadTexts:chan14.setStatus(_B)
if mibBuilder.loadTexts:chan14.setUnits(_H)
_Chan15_Type=Integer32
_Chan15_Object=MibScalar
chan15=_Chan15_Object((1,3,6,1,4,1,20677,3,1,1,3,15),_Chan15_Type())
chan15.setMaxAccess(_F)
if mibBuilder.loadTexts:chan15.setStatus(_B)
if mibBuilder.loadTexts:chan15.setUnits(_H)
_Chan16_Type=Integer32
_Chan16_Object=MibScalar
chan16=_Chan16_Object((1,3,6,1,4,1,20677,3,1,1,3,16),_Chan16_Type())
chan16.setMaxAccess(_F)
if mibBuilder.loadTexts:chan16.setStatus(_B)
if mibBuilder.loadTexts:chan16.setUnits(_H)
_Chan17_Type=Integer32
_Chan17_Object=MibScalar
chan17=_Chan17_Object((1,3,6,1,4,1,20677,3,1,1,3,17),_Chan17_Type())
chan17.setMaxAccess(_F)
if mibBuilder.loadTexts:chan17.setStatus(_B)
if mibBuilder.loadTexts:chan17.setUnits(_H)
_Chan18_Type=Integer32
_Chan18_Object=MibScalar
chan18=_Chan18_Object((1,3,6,1,4,1,20677,3,1,1,3,18),_Chan18_Type())
chan18.setMaxAccess(_F)
if mibBuilder.loadTexts:chan18.setStatus(_B)
if mibBuilder.loadTexts:chan18.setUnits(_H)
_Chan19_Type=Integer32
_Chan19_Object=MibScalar
chan19=_Chan19_Object((1,3,6,1,4,1,20677,3,1,1,3,19),_Chan19_Type())
chan19.setMaxAccess(_F)
if mibBuilder.loadTexts:chan19.setStatus(_B)
if mibBuilder.loadTexts:chan19.setUnits(_H)
_Chan20_Type=Integer32
_Chan20_Object=MibScalar
chan20=_Chan20_Object((1,3,6,1,4,1,20677,3,1,1,3,20),_Chan20_Type())
chan20.setMaxAccess(_F)
if mibBuilder.loadTexts:chan20.setStatus(_B)
if mibBuilder.loadTexts:chan20.setUnits(_H)
_Chan21_Type=Integer32
_Chan21_Object=MibScalar
chan21=_Chan21_Object((1,3,6,1,4,1,20677,3,1,1,3,21),_Chan21_Type())
chan21.setMaxAccess(_F)
if mibBuilder.loadTexts:chan21.setStatus(_B)
if mibBuilder.loadTexts:chan21.setUnits(_H)
_Chan22_Type=Integer32
_Chan22_Object=MibScalar
chan22=_Chan22_Object((1,3,6,1,4,1,20677,3,1,1,3,22),_Chan22_Type())
chan22.setMaxAccess(_F)
if mibBuilder.loadTexts:chan22.setStatus(_B)
if mibBuilder.loadTexts:chan22.setUnits(_H)
_Chan23_Type=Integer32
_Chan23_Object=MibScalar
chan23=_Chan23_Object((1,3,6,1,4,1,20677,3,1,1,3,23),_Chan23_Type())
chan23.setMaxAccess(_F)
if mibBuilder.loadTexts:chan23.setStatus(_B)
if mibBuilder.loadTexts:chan23.setUnits(_H)
_Chan24_Type=Integer32
_Chan24_Object=MibScalar
chan24=_Chan24_Object((1,3,6,1,4,1,20677,3,1,1,3,24),_Chan24_Type())
chan24.setMaxAccess(_F)
if mibBuilder.loadTexts:chan24.setStatus(_B)
if mibBuilder.loadTexts:chan24.setUnits(_H)
_Chan25_Type=Integer32
_Chan25_Object=MibScalar
chan25=_Chan25_Object((1,3,6,1,4,1,20677,3,1,1,3,25),_Chan25_Type())
chan25.setMaxAccess(_F)
if mibBuilder.loadTexts:chan25.setStatus(_B)
if mibBuilder.loadTexts:chan25.setUnits(_H)
_Chan26_Type=Integer32
_Chan26_Object=MibScalar
chan26=_Chan26_Object((1,3,6,1,4,1,20677,3,1,1,3,26),_Chan26_Type())
chan26.setMaxAccess(_F)
if mibBuilder.loadTexts:chan26.setStatus(_B)
if mibBuilder.loadTexts:chan26.setUnits(_H)
_Chan27_Type=Integer32
_Chan27_Object=MibScalar
chan27=_Chan27_Object((1,3,6,1,4,1,20677,3,1,1,3,27),_Chan27_Type())
chan27.setMaxAccess(_F)
if mibBuilder.loadTexts:chan27.setStatus(_B)
if mibBuilder.loadTexts:chan27.setUnits(_H)
_Chan28_Type=Integer32
_Chan28_Object=MibScalar
chan28=_Chan28_Object((1,3,6,1,4,1,20677,3,1,1,3,28),_Chan28_Type())
chan28.setMaxAccess(_F)
if mibBuilder.loadTexts:chan28.setStatus(_B)
if mibBuilder.loadTexts:chan28.setUnits(_H)
_Chan29_Type=Integer32
_Chan29_Object=MibScalar
chan29=_Chan29_Object((1,3,6,1,4,1,20677,3,1,1,3,29),_Chan29_Type())
chan29.setMaxAccess(_F)
if mibBuilder.loadTexts:chan29.setStatus(_B)
if mibBuilder.loadTexts:chan29.setUnits(_H)
_Chan30_Type=Integer32
_Chan30_Object=MibScalar
chan30=_Chan30_Object((1,3,6,1,4,1,20677,3,1,1,3,30),_Chan30_Type())
chan30.setMaxAccess(_F)
if mibBuilder.loadTexts:chan30.setStatus(_B)
if mibBuilder.loadTexts:chan30.setUnits(_H)
_Chan31_Type=Integer32
_Chan31_Object=MibScalar
chan31=_Chan31_Object((1,3,6,1,4,1,20677,3,1,1,3,31),_Chan31_Type())
chan31.setMaxAccess(_F)
if mibBuilder.loadTexts:chan31.setStatus(_B)
if mibBuilder.loadTexts:chan31.setUnits(_H)
_Chan32_Type=Integer32
_Chan32_Object=MibScalar
chan32=_Chan32_Object((1,3,6,1,4,1,20677,3,1,1,3,32),_Chan32_Type())
chan32.setMaxAccess(_F)
if mibBuilder.loadTexts:chan32.setStatus(_B)
if mibBuilder.loadTexts:chan32.setUnits(_H)
_TempChan1_Type=Integer32
_TempChan1_Object=MibScalar
tempChan1=_TempChan1_Object((1,3,6,1,4,1,20677,3,1,1,3,248),_TempChan1_Type())
tempChan1.setMaxAccess(_F)
if mibBuilder.loadTexts:tempChan1.setStatus(_B)
if mibBuilder.loadTexts:tempChan1.setUnits(_N)
_TempChan2_Type=Integer32
_TempChan2_Object=MibScalar
tempChan2=_TempChan2_Object((1,3,6,1,4,1,20677,3,1,1,3,249),_TempChan2_Type())
tempChan2.setMaxAccess(_F)
if mibBuilder.loadTexts:tempChan2.setStatus(_B)
if mibBuilder.loadTexts:tempChan2.setUnits(_N)
_ChanNames_ObjectIdentity=ObjectIdentity
chanNames=_ChanNames_ObjectIdentity((1,3,6,1,4,1,20677,3,1,1,4))
class _Chan1Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan1Name_Type.__name__=_G
_Chan1Name_Object=MibScalar
chan1Name=_Chan1Name_Object((1,3,6,1,4,1,20677,3,1,1,4,1),_Chan1Name_Type())
chan1Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan1Name.setStatus(_B)
class _Chan2Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan2Name_Type.__name__=_G
_Chan2Name_Object=MibScalar
chan2Name=_Chan2Name_Object((1,3,6,1,4,1,20677,3,1,1,4,2),_Chan2Name_Type())
chan2Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan2Name.setStatus(_B)
class _Chan3Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan3Name_Type.__name__=_G
_Chan3Name_Object=MibScalar
chan3Name=_Chan3Name_Object((1,3,6,1,4,1,20677,3,1,1,4,3),_Chan3Name_Type())
chan3Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan3Name.setStatus(_B)
class _Chan4Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan4Name_Type.__name__=_G
_Chan4Name_Object=MibScalar
chan4Name=_Chan4Name_Object((1,3,6,1,4,1,20677,3,1,1,4,4),_Chan4Name_Type())
chan4Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan4Name.setStatus(_B)
class _Chan5Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan5Name_Type.__name__=_G
_Chan5Name_Object=MibScalar
chan5Name=_Chan5Name_Object((1,3,6,1,4,1,20677,3,1,1,4,5),_Chan5Name_Type())
chan5Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan5Name.setStatus(_B)
class _Chan6Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan6Name_Type.__name__=_G
_Chan6Name_Object=MibScalar
chan6Name=_Chan6Name_Object((1,3,6,1,4,1,20677,3,1,1,4,6),_Chan6Name_Type())
chan6Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan6Name.setStatus(_B)
class _Chan7Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan7Name_Type.__name__=_G
_Chan7Name_Object=MibScalar
chan7Name=_Chan7Name_Object((1,3,6,1,4,1,20677,3,1,1,4,7),_Chan7Name_Type())
chan7Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan7Name.setStatus(_B)
class _Chan8Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan8Name_Type.__name__=_G
_Chan8Name_Object=MibScalar
chan8Name=_Chan8Name_Object((1,3,6,1,4,1,20677,3,1,1,4,8),_Chan8Name_Type())
chan8Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan8Name.setStatus(_B)
class _Chan9Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan9Name_Type.__name__=_G
_Chan9Name_Object=MibScalar
chan9Name=_Chan9Name_Object((1,3,6,1,4,1,20677,3,1,1,4,9),_Chan9Name_Type())
chan9Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan9Name.setStatus(_B)
class _Chan10Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan10Name_Type.__name__=_G
_Chan10Name_Object=MibScalar
chan10Name=_Chan10Name_Object((1,3,6,1,4,1,20677,3,1,1,4,10),_Chan10Name_Type())
chan10Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan10Name.setStatus(_B)
class _Chan11Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan11Name_Type.__name__=_G
_Chan11Name_Object=MibScalar
chan11Name=_Chan11Name_Object((1,3,6,1,4,1,20677,3,1,1,4,11),_Chan11Name_Type())
chan11Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan11Name.setStatus(_B)
class _Chan12Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan12Name_Type.__name__=_G
_Chan12Name_Object=MibScalar
chan12Name=_Chan12Name_Object((1,3,6,1,4,1,20677,3,1,1,4,12),_Chan12Name_Type())
chan12Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan12Name.setStatus(_B)
class _Chan13Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan13Name_Type.__name__=_G
_Chan13Name_Object=MibScalar
chan13Name=_Chan13Name_Object((1,3,6,1,4,1,20677,3,1,1,4,13),_Chan13Name_Type())
chan13Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan13Name.setStatus(_B)
class _Chan14Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan14Name_Type.__name__=_G
_Chan14Name_Object=MibScalar
chan14Name=_Chan14Name_Object((1,3,6,1,4,1,20677,3,1,1,4,14),_Chan14Name_Type())
chan14Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan14Name.setStatus(_B)
class _Chan15Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan15Name_Type.__name__=_G
_Chan15Name_Object=MibScalar
chan15Name=_Chan15Name_Object((1,3,6,1,4,1,20677,3,1,1,4,15),_Chan15Name_Type())
chan15Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan15Name.setStatus(_B)
class _Chan16Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan16Name_Type.__name__=_G
_Chan16Name_Object=MibScalar
chan16Name=_Chan16Name_Object((1,3,6,1,4,1,20677,3,1,1,4,16),_Chan16Name_Type())
chan16Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan16Name.setStatus(_B)
class _Chan17Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan17Name_Type.__name__=_G
_Chan17Name_Object=MibScalar
chan17Name=_Chan17Name_Object((1,3,6,1,4,1,20677,3,1,1,4,17),_Chan17Name_Type())
chan17Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan17Name.setStatus(_B)
class _Chan18Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan18Name_Type.__name__=_G
_Chan18Name_Object=MibScalar
chan18Name=_Chan18Name_Object((1,3,6,1,4,1,20677,3,1,1,4,18),_Chan18Name_Type())
chan18Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan18Name.setStatus(_B)
class _Chan19Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan19Name_Type.__name__=_G
_Chan19Name_Object=MibScalar
chan19Name=_Chan19Name_Object((1,3,6,1,4,1,20677,3,1,1,4,19),_Chan19Name_Type())
chan19Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan19Name.setStatus(_B)
class _Chan20Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan20Name_Type.__name__=_G
_Chan20Name_Object=MibScalar
chan20Name=_Chan20Name_Object((1,3,6,1,4,1,20677,3,1,1,4,20),_Chan20Name_Type())
chan20Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan20Name.setStatus(_B)
class _Chan21Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan21Name_Type.__name__=_G
_Chan21Name_Object=MibScalar
chan21Name=_Chan21Name_Object((1,3,6,1,4,1,20677,3,1,1,4,21),_Chan21Name_Type())
chan21Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan21Name.setStatus(_B)
class _Chan22Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan22Name_Type.__name__=_G
_Chan22Name_Object=MibScalar
chan22Name=_Chan22Name_Object((1,3,6,1,4,1,20677,3,1,1,4,22),_Chan22Name_Type())
chan22Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan22Name.setStatus(_B)
class _Chan23Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan23Name_Type.__name__=_G
_Chan23Name_Object=MibScalar
chan23Name=_Chan23Name_Object((1,3,6,1,4,1,20677,3,1,1,4,23),_Chan23Name_Type())
chan23Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan23Name.setStatus(_B)
class _Chan24Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan24Name_Type.__name__=_G
_Chan24Name_Object=MibScalar
chan24Name=_Chan24Name_Object((1,3,6,1,4,1,20677,3,1,1,4,24),_Chan24Name_Type())
chan24Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan24Name.setStatus(_B)
class _Chan25Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan25Name_Type.__name__=_G
_Chan25Name_Object=MibScalar
chan25Name=_Chan25Name_Object((1,3,6,1,4,1,20677,3,1,1,4,25),_Chan25Name_Type())
chan25Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan25Name.setStatus(_B)
class _Chan26Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan26Name_Type.__name__=_G
_Chan26Name_Object=MibScalar
chan26Name=_Chan26Name_Object((1,3,6,1,4,1,20677,3,1,1,4,26),_Chan26Name_Type())
chan26Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan26Name.setStatus(_B)
class _Chan27Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan27Name_Type.__name__=_G
_Chan27Name_Object=MibScalar
chan27Name=_Chan27Name_Object((1,3,6,1,4,1,20677,3,1,1,4,27),_Chan27Name_Type())
chan27Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan27Name.setStatus(_B)
class _Chan28Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan28Name_Type.__name__=_G
_Chan28Name_Object=MibScalar
chan28Name=_Chan28Name_Object((1,3,6,1,4,1,20677,3,1,1,4,28),_Chan28Name_Type())
chan28Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan28Name.setStatus(_B)
class _Chan29Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan29Name_Type.__name__=_G
_Chan29Name_Object=MibScalar
chan29Name=_Chan29Name_Object((1,3,6,1,4,1,20677,3,1,1,4,29),_Chan29Name_Type())
chan29Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan29Name.setStatus(_B)
class _Chan30Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan30Name_Type.__name__=_G
_Chan30Name_Object=MibScalar
chan30Name=_Chan30Name_Object((1,3,6,1,4,1,20677,3,1,1,4,30),_Chan30Name_Type())
chan30Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan30Name.setStatus(_B)
class _Chan31Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan31Name_Type.__name__=_G
_Chan31Name_Object=MibScalar
chan31Name=_Chan31Name_Object((1,3,6,1,4,1,20677,3,1,1,4,31),_Chan31Name_Type())
chan31Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan31Name.setStatus(_B)
class _Chan32Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Chan32Name_Type.__name__=_G
_Chan32Name_Object=MibScalar
chan32Name=_Chan32Name_Object((1,3,6,1,4,1,20677,3,1,1,4,32),_Chan32Name_Type())
chan32Name.setMaxAccess(_C)
if mibBuilder.loadTexts:chan32Name.setStatus(_B)
class _Temp1Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Temp1Name_Type.__name__=_G
_Temp1Name_Object=MibScalar
temp1Name=_Temp1Name_Object((1,3,6,1,4,1,20677,3,1,1,4,248),_Temp1Name_Type())
temp1Name.setMaxAccess(_C)
if mibBuilder.loadTexts:temp1Name.setStatus(_B)
class _Temp2Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_Temp2Name_Type.__name__=_G
_Temp2Name_Object=MibScalar
temp2Name=_Temp2Name_Object((1,3,6,1,4,1,20677,3,1,1,4,249),_Temp2Name_Type())
temp2Name.setMaxAccess(_C)
if mibBuilder.loadTexts:temp2Name.setStatus(_B)
_LowCurrentThresh_ObjectIdentity=ObjectIdentity
lowCurrentThresh=_LowCurrentThresh_ObjectIdentity((1,3,6,1,4,1,20677,3,1,1,5))
class _LowCurrentThreshold1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold1_Type.__name__=_E
_LowCurrentThreshold1_Object=MibScalar
lowCurrentThreshold1=_LowCurrentThreshold1_Object((1,3,6,1,4,1,20677,3,1,1,5,1),_LowCurrentThreshold1_Type())
lowCurrentThreshold1.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold1.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold1.setUnits(_D)
class _LowCurrentThreshold2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold2_Type.__name__=_E
_LowCurrentThreshold2_Object=MibScalar
lowCurrentThreshold2=_LowCurrentThreshold2_Object((1,3,6,1,4,1,20677,3,1,1,5,2),_LowCurrentThreshold2_Type())
lowCurrentThreshold2.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold2.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold2.setUnits(_D)
class _LowCurrentThreshold3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold3_Type.__name__=_E
_LowCurrentThreshold3_Object=MibScalar
lowCurrentThreshold3=_LowCurrentThreshold3_Object((1,3,6,1,4,1,20677,3,1,1,5,3),_LowCurrentThreshold3_Type())
lowCurrentThreshold3.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold3.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold3.setUnits(_D)
class _LowCurrentThreshold4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold4_Type.__name__=_E
_LowCurrentThreshold4_Object=MibScalar
lowCurrentThreshold4=_LowCurrentThreshold4_Object((1,3,6,1,4,1,20677,3,1,1,5,4),_LowCurrentThreshold4_Type())
lowCurrentThreshold4.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold4.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold4.setUnits(_D)
class _LowCurrentThreshold5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold5_Type.__name__=_E
_LowCurrentThreshold5_Object=MibScalar
lowCurrentThreshold5=_LowCurrentThreshold5_Object((1,3,6,1,4,1,20677,3,1,1,5,5),_LowCurrentThreshold5_Type())
lowCurrentThreshold5.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold5.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold5.setUnits(_D)
class _LowCurrentThreshold6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold6_Type.__name__=_E
_LowCurrentThreshold6_Object=MibScalar
lowCurrentThreshold6=_LowCurrentThreshold6_Object((1,3,6,1,4,1,20677,3,1,1,5,6),_LowCurrentThreshold6_Type())
lowCurrentThreshold6.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold6.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold6.setUnits(_D)
class _LowCurrentThreshold7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold7_Type.__name__=_E
_LowCurrentThreshold7_Object=MibScalar
lowCurrentThreshold7=_LowCurrentThreshold7_Object((1,3,6,1,4,1,20677,3,1,1,5,7),_LowCurrentThreshold7_Type())
lowCurrentThreshold7.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold7.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold7.setUnits(_D)
class _LowCurrentThreshold8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold8_Type.__name__=_E
_LowCurrentThreshold8_Object=MibScalar
lowCurrentThreshold8=_LowCurrentThreshold8_Object((1,3,6,1,4,1,20677,3,1,1,5,8),_LowCurrentThreshold8_Type())
lowCurrentThreshold8.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold8.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold8.setUnits(_D)
class _LowCurrentThreshold9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold9_Type.__name__=_E
_LowCurrentThreshold9_Object=MibScalar
lowCurrentThreshold9=_LowCurrentThreshold9_Object((1,3,6,1,4,1,20677,3,1,1,5,9),_LowCurrentThreshold9_Type())
lowCurrentThreshold9.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold9.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold9.setUnits(_D)
class _LowCurrentThreshold10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold10_Type.__name__=_E
_LowCurrentThreshold10_Object=MibScalar
lowCurrentThreshold10=_LowCurrentThreshold10_Object((1,3,6,1,4,1,20677,3,1,1,5,10),_LowCurrentThreshold10_Type())
lowCurrentThreshold10.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold10.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold10.setUnits(_D)
class _LowCurrentThreshold11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold11_Type.__name__=_E
_LowCurrentThreshold11_Object=MibScalar
lowCurrentThreshold11=_LowCurrentThreshold11_Object((1,3,6,1,4,1,20677,3,1,1,5,11),_LowCurrentThreshold11_Type())
lowCurrentThreshold11.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold11.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold11.setUnits(_D)
class _LowCurrentThreshold12_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold12_Type.__name__=_E
_LowCurrentThreshold12_Object=MibScalar
lowCurrentThreshold12=_LowCurrentThreshold12_Object((1,3,6,1,4,1,20677,3,1,1,5,12),_LowCurrentThreshold12_Type())
lowCurrentThreshold12.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold12.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold12.setUnits(_D)
class _LowCurrentThreshold13_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold13_Type.__name__=_E
_LowCurrentThreshold13_Object=MibScalar
lowCurrentThreshold13=_LowCurrentThreshold13_Object((1,3,6,1,4,1,20677,3,1,1,5,13),_LowCurrentThreshold13_Type())
lowCurrentThreshold13.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold13.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold13.setUnits(_D)
class _LowCurrentThreshold14_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold14_Type.__name__=_E
_LowCurrentThreshold14_Object=MibScalar
lowCurrentThreshold14=_LowCurrentThreshold14_Object((1,3,6,1,4,1,20677,3,1,1,5,14),_LowCurrentThreshold14_Type())
lowCurrentThreshold14.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold14.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold14.setUnits(_D)
class _LowCurrentThreshold15_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold15_Type.__name__=_E
_LowCurrentThreshold15_Object=MibScalar
lowCurrentThreshold15=_LowCurrentThreshold15_Object((1,3,6,1,4,1,20677,3,1,1,5,15),_LowCurrentThreshold15_Type())
lowCurrentThreshold15.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold15.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold15.setUnits(_D)
class _LowCurrentThreshold16_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold16_Type.__name__=_E
_LowCurrentThreshold16_Object=MibScalar
lowCurrentThreshold16=_LowCurrentThreshold16_Object((1,3,6,1,4,1,20677,3,1,1,5,16),_LowCurrentThreshold16_Type())
lowCurrentThreshold16.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold16.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold16.setUnits(_D)
class _LowCurrentThreshold17_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold17_Type.__name__=_E
_LowCurrentThreshold17_Object=MibScalar
lowCurrentThreshold17=_LowCurrentThreshold17_Object((1,3,6,1,4,1,20677,3,1,1,5,17),_LowCurrentThreshold17_Type())
lowCurrentThreshold17.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold17.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold17.setUnits(_D)
class _LowCurrentThreshold18_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold18_Type.__name__=_E
_LowCurrentThreshold18_Object=MibScalar
lowCurrentThreshold18=_LowCurrentThreshold18_Object((1,3,6,1,4,1,20677,3,1,1,5,18),_LowCurrentThreshold18_Type())
lowCurrentThreshold18.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold18.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold18.setUnits(_D)
class _LowCurrentThreshold19_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold19_Type.__name__=_E
_LowCurrentThreshold19_Object=MibScalar
lowCurrentThreshold19=_LowCurrentThreshold19_Object((1,3,6,1,4,1,20677,3,1,1,5,19),_LowCurrentThreshold19_Type())
lowCurrentThreshold19.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold19.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold19.setUnits(_D)
class _LowCurrentThreshold20_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold20_Type.__name__=_E
_LowCurrentThreshold20_Object=MibScalar
lowCurrentThreshold20=_LowCurrentThreshold20_Object((1,3,6,1,4,1,20677,3,1,1,5,20),_LowCurrentThreshold20_Type())
lowCurrentThreshold20.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold20.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold20.setUnits(_D)
class _LowCurrentThreshold21_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold21_Type.__name__=_E
_LowCurrentThreshold21_Object=MibScalar
lowCurrentThreshold21=_LowCurrentThreshold21_Object((1,3,6,1,4,1,20677,3,1,1,5,21),_LowCurrentThreshold21_Type())
lowCurrentThreshold21.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold21.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold21.setUnits(_D)
class _LowCurrentThreshold22_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold22_Type.__name__=_E
_LowCurrentThreshold22_Object=MibScalar
lowCurrentThreshold22=_LowCurrentThreshold22_Object((1,3,6,1,4,1,20677,3,1,1,5,22),_LowCurrentThreshold22_Type())
lowCurrentThreshold22.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold22.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold22.setUnits(_D)
class _LowCurrentThreshold23_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold23_Type.__name__=_E
_LowCurrentThreshold23_Object=MibScalar
lowCurrentThreshold23=_LowCurrentThreshold23_Object((1,3,6,1,4,1,20677,3,1,1,5,23),_LowCurrentThreshold23_Type())
lowCurrentThreshold23.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold23.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold23.setUnits(_D)
class _LowCurrentThreshold24_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold24_Type.__name__=_E
_LowCurrentThreshold24_Object=MibScalar
lowCurrentThreshold24=_LowCurrentThreshold24_Object((1,3,6,1,4,1,20677,3,1,1,5,24),_LowCurrentThreshold24_Type())
lowCurrentThreshold24.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold24.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold24.setUnits(_D)
class _LowCurrentThreshold25_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold25_Type.__name__=_E
_LowCurrentThreshold25_Object=MibScalar
lowCurrentThreshold25=_LowCurrentThreshold25_Object((1,3,6,1,4,1,20677,3,1,1,5,25),_LowCurrentThreshold25_Type())
lowCurrentThreshold25.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold25.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold25.setUnits(_D)
class _LowCurrentThreshold26_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold26_Type.__name__=_E
_LowCurrentThreshold26_Object=MibScalar
lowCurrentThreshold26=_LowCurrentThreshold26_Object((1,3,6,1,4,1,20677,3,1,1,5,26),_LowCurrentThreshold26_Type())
lowCurrentThreshold26.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold26.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold26.setUnits(_D)
class _LowCurrentThreshold27_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold27_Type.__name__=_E
_LowCurrentThreshold27_Object=MibScalar
lowCurrentThreshold27=_LowCurrentThreshold27_Object((1,3,6,1,4,1,20677,3,1,1,5,27),_LowCurrentThreshold27_Type())
lowCurrentThreshold27.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold27.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold27.setUnits(_D)
class _LowCurrentThreshold28_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold28_Type.__name__=_E
_LowCurrentThreshold28_Object=MibScalar
lowCurrentThreshold28=_LowCurrentThreshold28_Object((1,3,6,1,4,1,20677,3,1,1,5,28),_LowCurrentThreshold28_Type())
lowCurrentThreshold28.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold28.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold28.setUnits(_D)
class _LowCurrentThreshold29_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold29_Type.__name__=_E
_LowCurrentThreshold29_Object=MibScalar
lowCurrentThreshold29=_LowCurrentThreshold29_Object((1,3,6,1,4,1,20677,3,1,1,5,29),_LowCurrentThreshold29_Type())
lowCurrentThreshold29.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold29.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold29.setUnits(_D)
class _LowCurrentThreshold30_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold30_Type.__name__=_E
_LowCurrentThreshold30_Object=MibScalar
lowCurrentThreshold30=_LowCurrentThreshold30_Object((1,3,6,1,4,1,20677,3,1,1,5,30),_LowCurrentThreshold30_Type())
lowCurrentThreshold30.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold30.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold30.setUnits(_D)
class _LowCurrentThreshold31_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold31_Type.__name__=_E
_LowCurrentThreshold31_Object=MibScalar
lowCurrentThreshold31=_LowCurrentThreshold31_Object((1,3,6,1,4,1,20677,3,1,1,5,31),_LowCurrentThreshold31_Type())
lowCurrentThreshold31.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold31.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold31.setUnits(_D)
class _LowCurrentThreshold32_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LowCurrentThreshold32_Type.__name__=_E
_LowCurrentThreshold32_Object=MibScalar
lowCurrentThreshold32=_LowCurrentThreshold32_Object((1,3,6,1,4,1,20677,3,1,1,5,32),_LowCurrentThreshold32_Type())
lowCurrentThreshold32.setMaxAccess(_C)
if mibBuilder.loadTexts:lowCurrentThreshold32.setStatus(_B)
if mibBuilder.loadTexts:lowCurrentThreshold32.setUnits(_D)
_HighCurrentThresh_ObjectIdentity=ObjectIdentity
highCurrentThresh=_HighCurrentThresh_ObjectIdentity((1,3,6,1,4,1,20677,3,1,1,6))
class _HighCurrentThreshold1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold1_Type.__name__=_E
_HighCurrentThreshold1_Object=MibScalar
highCurrentThreshold1=_HighCurrentThreshold1_Object((1,3,6,1,4,1,20677,3,1,1,6,1),_HighCurrentThreshold1_Type())
highCurrentThreshold1.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold1.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold1.setUnits(_D)
class _HighCurrentThreshold2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold2_Type.__name__=_E
_HighCurrentThreshold2_Object=MibScalar
highCurrentThreshold2=_HighCurrentThreshold2_Object((1,3,6,1,4,1,20677,3,1,1,6,2),_HighCurrentThreshold2_Type())
highCurrentThreshold2.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold2.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold2.setUnits(_D)
class _HighCurrentThreshold3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold3_Type.__name__=_E
_HighCurrentThreshold3_Object=MibScalar
highCurrentThreshold3=_HighCurrentThreshold3_Object((1,3,6,1,4,1,20677,3,1,1,6,3),_HighCurrentThreshold3_Type())
highCurrentThreshold3.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold3.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold3.setUnits(_D)
class _HighCurrentThreshold4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold4_Type.__name__=_E
_HighCurrentThreshold4_Object=MibScalar
highCurrentThreshold4=_HighCurrentThreshold4_Object((1,3,6,1,4,1,20677,3,1,1,6,4),_HighCurrentThreshold4_Type())
highCurrentThreshold4.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold4.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold4.setUnits(_D)
class _HighCurrentThreshold5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold5_Type.__name__=_E
_HighCurrentThreshold5_Object=MibScalar
highCurrentThreshold5=_HighCurrentThreshold5_Object((1,3,6,1,4,1,20677,3,1,1,6,5),_HighCurrentThreshold5_Type())
highCurrentThreshold5.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold5.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold5.setUnits(_D)
class _HighCurrentThreshold6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold6_Type.__name__=_E
_HighCurrentThreshold6_Object=MibScalar
highCurrentThreshold6=_HighCurrentThreshold6_Object((1,3,6,1,4,1,20677,3,1,1,6,6),_HighCurrentThreshold6_Type())
highCurrentThreshold6.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold6.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold6.setUnits(_D)
class _HighCurrentThreshold7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold7_Type.__name__=_E
_HighCurrentThreshold7_Object=MibScalar
highCurrentThreshold7=_HighCurrentThreshold7_Object((1,3,6,1,4,1,20677,3,1,1,6,7),_HighCurrentThreshold7_Type())
highCurrentThreshold7.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold7.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold7.setUnits(_D)
class _HighCurrentThreshold8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold8_Type.__name__=_E
_HighCurrentThreshold8_Object=MibScalar
highCurrentThreshold8=_HighCurrentThreshold8_Object((1,3,6,1,4,1,20677,3,1,1,6,8),_HighCurrentThreshold8_Type())
highCurrentThreshold8.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold8.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold8.setUnits(_D)
class _HighCurrentThreshold9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold9_Type.__name__=_E
_HighCurrentThreshold9_Object=MibScalar
highCurrentThreshold9=_HighCurrentThreshold9_Object((1,3,6,1,4,1,20677,3,1,1,6,9),_HighCurrentThreshold9_Type())
highCurrentThreshold9.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold9.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold9.setUnits(_D)
class _HighCurrentThreshold10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold10_Type.__name__=_E
_HighCurrentThreshold10_Object=MibScalar
highCurrentThreshold10=_HighCurrentThreshold10_Object((1,3,6,1,4,1,20677,3,1,1,6,10),_HighCurrentThreshold10_Type())
highCurrentThreshold10.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold10.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold10.setUnits(_D)
class _HighCurrentThreshold11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold11_Type.__name__=_E
_HighCurrentThreshold11_Object=MibScalar
highCurrentThreshold11=_HighCurrentThreshold11_Object((1,3,6,1,4,1,20677,3,1,1,6,11),_HighCurrentThreshold11_Type())
highCurrentThreshold11.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold11.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold11.setUnits(_D)
class _HighCurrentThreshold12_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold12_Type.__name__=_E
_HighCurrentThreshold12_Object=MibScalar
highCurrentThreshold12=_HighCurrentThreshold12_Object((1,3,6,1,4,1,20677,3,1,1,6,12),_HighCurrentThreshold12_Type())
highCurrentThreshold12.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold12.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold12.setUnits(_D)
class _HighCurrentThreshold13_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold13_Type.__name__=_E
_HighCurrentThreshold13_Object=MibScalar
highCurrentThreshold13=_HighCurrentThreshold13_Object((1,3,6,1,4,1,20677,3,1,1,6,13),_HighCurrentThreshold13_Type())
highCurrentThreshold13.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold13.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold13.setUnits(_D)
class _HighCurrentThreshold14_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold14_Type.__name__=_E
_HighCurrentThreshold14_Object=MibScalar
highCurrentThreshold14=_HighCurrentThreshold14_Object((1,3,6,1,4,1,20677,3,1,1,6,14),_HighCurrentThreshold14_Type())
highCurrentThreshold14.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold14.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold14.setUnits(_D)
class _HighCurrentThreshold15_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold15_Type.__name__=_E
_HighCurrentThreshold15_Object=MibScalar
highCurrentThreshold15=_HighCurrentThreshold15_Object((1,3,6,1,4,1,20677,3,1,1,6,15),_HighCurrentThreshold15_Type())
highCurrentThreshold15.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold15.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold15.setUnits(_D)
class _HighCurrentThreshold16_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold16_Type.__name__=_E
_HighCurrentThreshold16_Object=MibScalar
highCurrentThreshold16=_HighCurrentThreshold16_Object((1,3,6,1,4,1,20677,3,1,1,6,16),_HighCurrentThreshold16_Type())
highCurrentThreshold16.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold16.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold16.setUnits(_D)
class _HighCurrentThreshold17_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold17_Type.__name__=_E
_HighCurrentThreshold17_Object=MibScalar
highCurrentThreshold17=_HighCurrentThreshold17_Object((1,3,6,1,4,1,20677,3,1,1,6,17),_HighCurrentThreshold17_Type())
highCurrentThreshold17.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold17.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold17.setUnits(_D)
class _HighCurrentThreshold18_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold18_Type.__name__=_E
_HighCurrentThreshold18_Object=MibScalar
highCurrentThreshold18=_HighCurrentThreshold18_Object((1,3,6,1,4,1,20677,3,1,1,6,18),_HighCurrentThreshold18_Type())
highCurrentThreshold18.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold18.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold18.setUnits(_D)
class _HighCurrentThreshold19_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold19_Type.__name__=_E
_HighCurrentThreshold19_Object=MibScalar
highCurrentThreshold19=_HighCurrentThreshold19_Object((1,3,6,1,4,1,20677,3,1,1,6,19),_HighCurrentThreshold19_Type())
highCurrentThreshold19.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold19.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold19.setUnits(_D)
class _HighCurrentThreshold20_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold20_Type.__name__=_E
_HighCurrentThreshold20_Object=MibScalar
highCurrentThreshold20=_HighCurrentThreshold20_Object((1,3,6,1,4,1,20677,3,1,1,6,20),_HighCurrentThreshold20_Type())
highCurrentThreshold20.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold20.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold20.setUnits(_D)
class _HighCurrentThreshold21_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold21_Type.__name__=_E
_HighCurrentThreshold21_Object=MibScalar
highCurrentThreshold21=_HighCurrentThreshold21_Object((1,3,6,1,4,1,20677,3,1,1,6,21),_HighCurrentThreshold21_Type())
highCurrentThreshold21.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold21.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold21.setUnits(_D)
class _HighCurrentThreshold22_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold22_Type.__name__=_E
_HighCurrentThreshold22_Object=MibScalar
highCurrentThreshold22=_HighCurrentThreshold22_Object((1,3,6,1,4,1,20677,3,1,1,6,22),_HighCurrentThreshold22_Type())
highCurrentThreshold22.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold22.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold22.setUnits(_D)
class _HighCurrentThreshold23_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold23_Type.__name__=_E
_HighCurrentThreshold23_Object=MibScalar
highCurrentThreshold23=_HighCurrentThreshold23_Object((1,3,6,1,4,1,20677,3,1,1,6,23),_HighCurrentThreshold23_Type())
highCurrentThreshold23.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold23.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold23.setUnits(_D)
class _HighCurrentThreshold24_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold24_Type.__name__=_E
_HighCurrentThreshold24_Object=MibScalar
highCurrentThreshold24=_HighCurrentThreshold24_Object((1,3,6,1,4,1,20677,3,1,1,6,24),_HighCurrentThreshold24_Type())
highCurrentThreshold24.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold24.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold24.setUnits(_D)
class _HighCurrentThreshold25_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold25_Type.__name__=_E
_HighCurrentThreshold25_Object=MibScalar
highCurrentThreshold25=_HighCurrentThreshold25_Object((1,3,6,1,4,1,20677,3,1,1,6,25),_HighCurrentThreshold25_Type())
highCurrentThreshold25.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold25.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold25.setUnits(_D)
class _HighCurrentThreshold26_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold26_Type.__name__=_E
_HighCurrentThreshold26_Object=MibScalar
highCurrentThreshold26=_HighCurrentThreshold26_Object((1,3,6,1,4,1,20677,3,1,1,6,26),_HighCurrentThreshold26_Type())
highCurrentThreshold26.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold26.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold26.setUnits(_D)
class _HighCurrentThreshold27_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold27_Type.__name__=_E
_HighCurrentThreshold27_Object=MibScalar
highCurrentThreshold27=_HighCurrentThreshold27_Object((1,3,6,1,4,1,20677,3,1,1,6,27),_HighCurrentThreshold27_Type())
highCurrentThreshold27.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold27.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold27.setUnits(_D)
class _HighCurrentThreshold28_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold28_Type.__name__=_E
_HighCurrentThreshold28_Object=MibScalar
highCurrentThreshold28=_HighCurrentThreshold28_Object((1,3,6,1,4,1,20677,3,1,1,6,28),_HighCurrentThreshold28_Type())
highCurrentThreshold28.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold28.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold28.setUnits(_D)
class _HighCurrentThreshold29_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold29_Type.__name__=_E
_HighCurrentThreshold29_Object=MibScalar
highCurrentThreshold29=_HighCurrentThreshold29_Object((1,3,6,1,4,1,20677,3,1,1,6,29),_HighCurrentThreshold29_Type())
highCurrentThreshold29.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold29.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold29.setUnits(_D)
class _HighCurrentThreshold30_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold30_Type.__name__=_E
_HighCurrentThreshold30_Object=MibScalar
highCurrentThreshold30=_HighCurrentThreshold30_Object((1,3,6,1,4,1,20677,3,1,1,6,30),_HighCurrentThreshold30_Type())
highCurrentThreshold30.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold30.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold30.setUnits(_D)
class _HighCurrentThreshold31_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold31_Type.__name__=_E
_HighCurrentThreshold31_Object=MibScalar
highCurrentThreshold31=_HighCurrentThreshold31_Object((1,3,6,1,4,1,20677,3,1,1,6,31),_HighCurrentThreshold31_Type())
highCurrentThreshold31.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold31.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold31.setUnits(_D)
class _HighCurrentThreshold32_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HighCurrentThreshold32_Type.__name__=_E
_HighCurrentThreshold32_Object=MibScalar
highCurrentThreshold32=_HighCurrentThreshold32_Object((1,3,6,1,4,1,20677,3,1,1,6,32),_HighCurrentThreshold32_Type())
highCurrentThreshold32.setMaxAccess(_C)
if mibBuilder.loadTexts:highCurrentThreshold32.setStatus(_B)
if mibBuilder.loadTexts:highCurrentThreshold32.setUnits(_D)
_LowTempThresh_ObjectIdentity=ObjectIdentity
lowTempThresh=_LowTempThresh_ObjectIdentity((1,3,6,1,4,1,20677,3,1,1,7))
class _LowTempThreshold1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,150))
_LowTempThreshold1_Type.__name__=_E
_LowTempThreshold1_Object=MibScalar
lowTempThreshold1=_LowTempThreshold1_Object((1,3,6,1,4,1,20677,3,1,1,7,1),_LowTempThreshold1_Type())
lowTempThreshold1.setMaxAccess(_C)
if mibBuilder.loadTexts:lowTempThreshold1.setStatus(_B)
if mibBuilder.loadTexts:lowTempThreshold1.setUnits(_K)
class _LowTempThreshold2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,150))
_LowTempThreshold2_Type.__name__=_E
_LowTempThreshold2_Object=MibScalar
lowTempThreshold2=_LowTempThreshold2_Object((1,3,6,1,4,1,20677,3,1,1,7,2),_LowTempThreshold2_Type())
lowTempThreshold2.setMaxAccess(_C)
if mibBuilder.loadTexts:lowTempThreshold2.setStatus(_B)
if mibBuilder.loadTexts:lowTempThreshold2.setUnits(_K)
_HighTempThresh_ObjectIdentity=ObjectIdentity
highTempThresh=_HighTempThresh_ObjectIdentity((1,3,6,1,4,1,20677,3,1,1,8))
class _HighTempThreshold1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,150))
_HighTempThreshold1_Type.__name__=_E
_HighTempThreshold1_Object=MibScalar
highTempThreshold1=_HighTempThreshold1_Object((1,3,6,1,4,1,20677,3,1,1,8,1),_HighTempThreshold1_Type())
highTempThreshold1.setMaxAccess(_C)
if mibBuilder.loadTexts:highTempThreshold1.setStatus(_B)
if mibBuilder.loadTexts:highTempThreshold1.setUnits(_K)
class _HighTempThreshold2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,150))
_HighTempThreshold2_Type.__name__=_E
_HighTempThreshold2_Object=MibScalar
highTempThreshold2=_HighTempThreshold2_Object((1,3,6,1,4,1,20677,3,1,1,8,2),_HighTempThreshold2_Type())
highTempThreshold2.setMaxAccess(_C)
if mibBuilder.loadTexts:highTempThreshold2.setStatus(_B)
if mibBuilder.loadTexts:highTempThreshold2.setUnits(_K)
_Conformance_ObjectIdentity=ObjectIdentity
conformance=_Conformance_ObjectIdentity((1,3,6,1,4,1,20677,3,1,1,25))
_Groups_ObjectIdentity=ObjectIdentity
groups=_Groups_ObjectIdentity((1,3,6,1,4,1,20677,3,1,1,25,5))
unitGroup=ObjectGroup((1,3,6,1,4,1,20677,3,1,1,25,5,1))
unitGroup.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,'unitName'),(_A,_A8),(_A,'uptime')))
if mibBuilder.loadTexts:unitGroup.setStatus(_B)
measurementGroup=ObjectGroup((1,3,6,1,4,1,20677,3,1,1,25,5,2))
measurementGroup.setObjects(*((_A,'chan1'),(_A,'chan10'),(_A,'chan11'),(_A,'chan12'),(_A,'chan13'),(_A,'chan14'),(_A,'chan15'),(_A,'chan16'),(_A,'chan17'),(_A,'chan18'),(_A,'chan19'),(_A,'chan2'),(_A,'chan20'),(_A,'chan21'),(_A,'chan22'),(_A,'chan23'),(_A,'chan24'),(_A,'chan25'),(_A,'chan26'),(_A,'chan27'),(_A,'chan28'),(_A,'chan29'),(_A,'chan3'),(_A,'chan30'),(_A,'chan31'),(_A,'chan32'),(_A,'chan4'),(_A,'chan5'),(_A,'chan6'),(_A,'chan7'),(_A,'chan8'),(_A,'chan9'),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:measurementGroup.setStatus(_B)
thresholdGroup=ObjectGroup((1,3,6,1,4,1,20677,3,1,1,25,5,3))
thresholdGroup.setObjects(*((_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax),(_A,_Ay),(_A,_Az),(_A,_A_),(_A,_B0),(_A,_B1),(_A,_B2),(_A,_B3),(_A,_B4),(_A,_B5),(_A,_B6),(_A,_B7),(_A,_B8),(_A,_B9),(_A,_BA),(_A,_BB),(_A,_BC),(_A,_BD),(_A,_BE),(_A,_BF)))
if mibBuilder.loadTexts:thresholdGroup.setStatus(_B)
thresholdGroupOld=ObjectGroup((1,3,6,1,4,1,20677,3,1,1,25,5,4))
thresholdGroupOld.setObjects(*((_A,_BG),(_A,_BH),(_A,_BI),(_A,_BJ),(_A,_BK),(_A,_BL),(_A,_BM),(_A,_BN),(_A,_BO),(_A,_BP),(_A,_BQ),(_A,_BR),(_A,_BS),(_A,_BT),(_A,_BU),(_A,_BV)))
if mibBuilder.loadTexts:thresholdGroupOld.setStatus(_I)
compliances=ModuleCompliance((1,3,6,1,4,1,20677,3,1,1,25,1))
compliances.setObjects(*((_A,_BW),(_A,_BX),(_A,_BY)))
if mibBuilder.loadTexts:compliances.setStatus(_B)
oldCompliances=ModuleCompliance((1,3,6,1,4,1,20677,3,1,1,25,2))
oldCompliances.setObjects((_A,_BZ))
if mibBuilder.loadTexts:oldCompliances.setStatus(_I)
mibBuilder.exportSymbols(_A,**{'pulizzi':pulizzi,'monitoredepdu':monitoredepdu,'epdum1':epdum1,'epdum11':epdum11,'unitConfig':unitConfig,'uptime':uptime,'unitName':unitName,_BO:lowCurrentThreshold1old,_BP:lowCurrentThreshold2old,_BQ:lowCurrentThreshold3old,_BR:lowCurrentThreshold4old,_BS:lowCurrentThreshold5old,_BT:lowCurrentThreshold6old,_BU:lowCurrentThreshold7old,_BV:lowCurrentThreshold8old,_BG:highCurrentThreshold1old,_BH:highCurrentThreshold2old,_BI:highCurrentThreshold3old,_BJ:highCurrentThreshold4old,_BK:highCurrentThreshold5old,_BL:highCurrentThreshold6old,_BM:highCurrentThreshold7old,_BN:highCurrentThreshold8old,_A2:temperature1Enable,_A3:temperature2Enable,_y:firmwareRevision,_Q:assetID,_z:numCurrentChannels,_x:currentMonitorType,'networkSettings':networkSettings,_A6:unitIPAddress,_A8:unitSubnetMask,_A5:unitGateway,_A7:unitMACAddress,_A4:trapDestIP,_O:mailServerIP,_P:alertEmailAddress,'measurements':measurements,'chan1':chan1,'chan2':chan2,'chan3':chan3,'chan4':chan4,'chan5':chan5,'chan6':chan6,'chan7':chan7,'chan8':chan8,'chan9':chan9,'chan10':chan10,'chan11':chan11,'chan12':chan12,'chan13':chan13,'chan14':chan14,'chan15':chan15,'chan16':chan16,'chan17':chan17,'chan18':chan18,'chan19':chan19,'chan20':chan20,'chan21':chan21,'chan22':chan22,'chan23':chan23,'chan24':chan24,'chan25':chan25,'chan26':chan26,'chan27':chan27,'chan28':chan28,'chan29':chan29,'chan30':chan30,'chan31':chan31,'chan32':chan32,_A9:tempChan1,_AA:tempChan2,'chanNames':chanNames,_b:chan1Name,_m:chan2Name,_q:chan3Name,_r:chan4Name,_s:chan5Name,_t:chan6Name,_u:chan7Name,_v:chan8Name,_w:chan9Name,_R:chan10Name,_S:chan11Name,_T:chan12Name,_U:chan13Name,_V:chan14Name,_W:chan15Name,_X:chan16Name,_Y:chan17Name,_Z:chan18Name,_a:chan19Name,_c:chan20Name,_d:chan21Name,_e:chan22Name,_f:chan23Name,_g:chan24Name,_h:chan25Name,_i:chan26Name,_j:chan27Name,_k:chan28Name,_l:chan29Name,_n:chan30Name,_o:chan31Name,_p:chan32Name,_A0:temp1Name,_A1:temp2Name,'lowCurrentThresh':lowCurrentThresh,_Aj:lowCurrentThreshold1,_Au:lowCurrentThreshold2,_B4:lowCurrentThreshold3,_B8:lowCurrentThreshold4,_B9:lowCurrentThreshold5,_BA:lowCurrentThreshold6,_BB:lowCurrentThreshold7,_BC:lowCurrentThreshold8,_BD:lowCurrentThreshold9,_Ak:lowCurrentThreshold10,_Al:lowCurrentThreshold11,_Am:lowCurrentThreshold12,_An:lowCurrentThreshold13,_Ao:lowCurrentThreshold14,_Ap:lowCurrentThreshold15,_Aq:lowCurrentThreshold16,_Ar:lowCurrentThreshold17,_As:lowCurrentThreshold18,_At:lowCurrentThreshold19,_Av:lowCurrentThreshold20,_Aw:lowCurrentThreshold21,_Ax:lowCurrentThreshold22,_Ay:lowCurrentThreshold23,_Az:lowCurrentThreshold24,_A_:lowCurrentThreshold25,_B0:lowCurrentThreshold26,_B1:lowCurrentThreshold27,_B2:lowCurrentThreshold28,_B3:lowCurrentThreshold29,_B5:lowCurrentThreshold30,_B6:lowCurrentThreshold31,_B7:lowCurrentThreshold32,'highCurrentThresh':highCurrentThresh,_AB:highCurrentThreshold1,_AM:highCurrentThreshold2,_AX:highCurrentThreshold3,_Ab:highCurrentThreshold4,_Ac:highCurrentThreshold5,_Ad:highCurrentThreshold6,_Ae:highCurrentThreshold7,_Af:highCurrentThreshold8,_Ag:highCurrentThreshold9,_AC:highCurrentThreshold10,_AD:highCurrentThreshold11,_AE:highCurrentThreshold12,_AF:highCurrentThreshold13,_AG:highCurrentThreshold14,_AH:highCurrentThreshold15,_AI:highCurrentThreshold16,_AJ:highCurrentThreshold17,_AK:highCurrentThreshold18,_AL:highCurrentThreshold19,_AN:highCurrentThreshold20,_AO:highCurrentThreshold21,_AP:highCurrentThreshold22,_AQ:highCurrentThreshold23,_AR:highCurrentThreshold24,_AS:highCurrentThreshold25,_AT:highCurrentThreshold26,_AU:highCurrentThreshold27,_AV:highCurrentThreshold28,_AW:highCurrentThreshold29,_AY:highCurrentThreshold30,_AZ:highCurrentThreshold31,_Aa:highCurrentThreshold32,'lowTempThresh':lowTempThresh,_BE:lowTempThreshold1,_BF:lowTempThreshold2,'highTempThresh':highTempThresh,_Ah:highTempThreshold1,_Ai:highTempThreshold2,'conformance':conformance,'compliances':compliances,'oldCompliances':oldCompliances,'groups':groups,_BX:unitGroup,_BY:measurementGroup,_BW:thresholdGroup,_BZ:thresholdGroupOld})