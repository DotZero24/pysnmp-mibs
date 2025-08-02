_Aa='pdnAdslLineSubCarStatusHlogGroup'
_AZ='pdnAdslLineSubCarStatusBitsGroup'
_AY='pdnAdslLineSubCarStatusSnrGroup'
_AX='pdnAdslLineSubCarStatusQlnGroup'
_AW='pdnAdslLineSubCarStatusHlogMtGroup'
_AV='pdnAdslLineSubCarStatusHlinGroup'
_AU='pdnAdslLineStatusActAtpGroup'
_AT='pdnAdslLineStatusMaxattainableLineRateGroup'
_AS='pdnAdslLineStatusSnrMgnGroup'
_AR='pdnAdslLineStatusSignalAtnGroup'
_AQ='pdnAdslLineStatusLineAtnGroup'
_AP='pdnAdslLineL2AtprtGroup'
_AO='pdnAdslCarMaskGroup'
_AN='pdnAdslPsdGroup'
_AM='pdnAdslModeSpecificPsdGroup'
_AL='pdnAdslLineSpectrumGroup'
_AK='pdnAdslLineExtGroup'
_AJ='pdnAdslLineSubCarAturHlogPs'
_AI='pdnAdslLineSubCarAtucHlogPs'
_AH='pdnAdslLineSubCarAturBitsPs'
_AG='pdnAdslLineSubCarAtucBitsPs'
_AF='pdnAdslLineSubCarAturSnrPs'
_AE='pdnAdslLineSubCarAtucSnrPs'
_AD='pdnAdslLineSubCarAturQlnPs'
_AC='pdnAdslLineSubCarAtucQlnPs'
_AB='pdnAdslLineSubCarAturHlogMt'
_AA='pdnAdslLineSubCarAtucHlogMt'
_A9='pdnAdslLineSubCarAturHlinPs'
_A8='pdnAdslLineSubCarAtucHlinPs'
_A7='pdnAdslLineStatusAturActAtp'
_A6='pdnAdslLineStatusAtucActAtp'
_A5='pdnAdslLineStatusAturMaxAttainableLineRate'
_A4='pdnAdslLineStatusAtucMaxAttainableLineRate'
_A3='pdnAdslLineStatusAturSnrMgn'
_A2='pdnAdslLineStatusAtucSnrMgn'
_A1='pdnAdslLineStatusAturSignalAtn'
_A0='pdnAdslLineStatusAtucSignalAtn'
_z='pdnAdslLineStatusAturLineAtn'
_y='pdnAdslLineStatusAtucLineAtn'
_x='pdnAdslLineL2Atprt'
_w='pdnAdslCarMaskSubCarrierStatus'
_v='pdnAdslCarMaskRowStatus'
_u='pdnAdslPsdConfAtucMaxRxPwr'
_t='pdnAdslPsdConfAturMaxNomAtp'
_s='pdnAdslPsdConfAtucMaxNomAtp'
_r='pdnAdslPsdConfAturMaxNomPsd'
_q='pdnAdslPsdConfAtucMaxNomPsd'
_p='pdnAdslPsdConfRowStatus'
_o='pdnAdslModeSpecificPsdConfRowStatus'
_n='pdnAdslModeSpecificPsdConfAdslPsdConfProfile'
_m='pdnAdslLineSpectrumAturCarMaskProfile'
_l='pdnAdslLineSpectrumAtucCarMaskProfile'
_k='pdnAdslLineSpectrumModeSpecificPsdProfile'
_j='pdnAdslLineSpectrumProfileRowStatus'
_i='pdnAdslLineLdsf'
_h='pdnAdslLineL2Atpr'
_g='pdnAdslLineL2Time'
_f='pdnAdslLineL0Time'
_e='pdnAdslLinePmMode'
_d='pdnAdslLineSpectrumProfile'
_c='pdnAdslLinePowerManagementConfig'
_b='pdnAdslLineTransAtucActual'
_a='pdnAdslLineTransAtucConfig'
_Z='pdnAdslLineTransAtucCap'
_Y='pdnAdslLineCarrierIndex'
_X='pdnAdslCarMaskSubCarrierIndex'
_W='pdnAdslCarMaskProfileName'
_V='tenth dBm/Hz'
_U='pdnAdslPsdConfProfileName'
_T='pdnAdslModeSpecificPsdConfAdslMode'
_S='pdnAdslModeSpecificPsdConfProfileName'
_R='pdnAdslLineSpectrumProfileName'
_Q='seconds'
_P='DEFVAL'
_O='Bits'
_N='ifIndex'
_M='IF-MIB'
_L='tenth dBm'
_K='tenth dB'
_J='not-accessible'
_I='dB'
_H='read-write'
_G='SnmpAdminString'
_F='read-create'
_E='Integer32'
_D='Unsigned32'
_C='read-only'
_B='PDN-ADSL-LINE-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_M,_N)
pdn_interfaces,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-interfaces')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_O,'Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
pdnAdslLineExtMIB=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,6,24))
if mibBuilder.loadTexts:pdnAdslLineExtMIB.setRevisions(('2005-03-29 00:00','2005-01-06 00:00','2004-10-15 00:00','2004-09-10 00:00','2004-04-21 00:00','2004-04-20 00:00','2004-03-01 00:00','2003-12-08 00:00','2003-12-03 00:00','2003-11-19 15:00','2003-11-11 15:00','2003-11-06 15:00','2003-10-31 15:00','2003-10-23 15:00'))
class PdnAdslTransmissionModeType(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('ansit1413',0),('etsi',1),('q9921PotsNonOverlapped',2),('q9921PotsOverlapped',3),('q9921IsdnNonOverlapped',4),('q9921isdnOverlapped',5),('q9921tcmIsdnNonOverlapped',6),('q9921tcmIsdnOverlapped',7),('q9922potsNonOverlapeed',8),('q9922potsOverlapped',9),('q9922tcmIsdnNonOverlapped',10),('q9922tcmIsdnOverlapped',11),('q9921tcmIsdnSymmetric',12),('reservedBit13',13),('reservedBit14',14),('reservedBit15',15),('reservedBit16',16),('reservedBit17',17),('q9923potsNonOverlapped',18),('q9923potsOverlapped',19),('q9923isdnNonOverlapped',20),('q9923isdnOverlapped',21),('reservedBit22',22),('reservedBit23',23),('q9924potsNonOverlapped',24),('q9924potsOverlapped',25),('reservedBit26',26),('reservedBit27',27),('q9923DigitalNonOverlappedI',28),('q9923DigitalOverlappedI',29),('q9923DigitalNonOverlappedJ',30),('q9923DigitalOverlappedJ',31),('q9924DigitalNonOverlappedI',32),('q9924DigitalOverlappedI',33),('q9923ReachExtOverPotsMode1L',34),('q9923ReachExtOverPotsMode2L',35),('q9923ReachExtOverPotsMode3L',36),('q9923ReachExtOverPotsMode4L',37),('q9923ExtUpOverPotsNonOverlappedM',38),('q9923ExtUpOverPotsOverlappedM',39),('q9925potsNonOverlapped',40),('q9925potsOverlapped',41),('q9925isdnNonOverlapped',42),('q9925isdnOverlapped',43),('reserved44',44),('reserved45',45),('q9925DigitalNonOverlappedI',46),('q9925DigitalOverlappedI',47),('q9925DigitalNonOverlappedJ',48),('q9925OverlappedJ',49),('q9925ExtUpOverPotsNonOverlappedM',50),('q9925ExtUpOverPotsOverlappedM',51),('reservedBit52',52),('reservedBit53',53),('reservedBit54',54),('reservedBit55',55)))
_PdnAdslLineExtNotifications_ObjectIdentity=ObjectIdentity
pdnAdslLineExtNotifications=_PdnAdslLineExtNotifications_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,24,0))
_PdnAdslLineExtObjects_ObjectIdentity=ObjectIdentity
pdnAdslLineExtObjects=_PdnAdslLineExtObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,24,1))
_PdnAdslLineExtTable_Object=MibTable
pdnAdslLineExtTable=_PdnAdslLineExtTable_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,1))
if mibBuilder.loadTexts:pdnAdslLineExtTable.setStatus(_A)
_PdnAdslLineExtEntry_Object=MibTableRow
pdnAdslLineExtEntry=_PdnAdslLineExtEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,1,1))
pdnAdslLineExtEntry.setIndexNames((0,_M,_N))
if mibBuilder.loadTexts:pdnAdslLineExtEntry.setStatus(_A)
_PdnAdslLineTransAtucCap_Type=PdnAdslTransmissionModeType
_PdnAdslLineTransAtucCap_Object=MibTableColumn
pdnAdslLineTransAtucCap=_PdnAdslLineTransAtucCap_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,1,1,1),_PdnAdslLineTransAtucCap_Type())
pdnAdslLineTransAtucCap.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAdslLineTransAtucCap.setStatus(_A)
_PdnAdslLineTransAtucConfig_Type=PdnAdslTransmissionModeType
_PdnAdslLineTransAtucConfig_Object=MibTableColumn
pdnAdslLineTransAtucConfig=_PdnAdslLineTransAtucConfig_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,1,1,2),_PdnAdslLineTransAtucConfig_Type())
pdnAdslLineTransAtucConfig.setMaxAccess(_H)
if mibBuilder.loadTexts:pdnAdslLineTransAtucConfig.setStatus(_A)
_PdnAdslLineTransAtucActual_Type=PdnAdslTransmissionModeType
_PdnAdslLineTransAtucActual_Object=MibTableColumn
pdnAdslLineTransAtucActual=_PdnAdslLineTransAtucActual_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,1,1,3),_PdnAdslLineTransAtucActual_Type())
pdnAdslLineTransAtucActual.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAdslLineTransAtucActual.setStatus(_A)
class _PdnAdslLinePowerManagementConfig_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_PdnAdslLinePowerManagementConfig_Type.__name__=_E
_PdnAdslLinePowerManagementConfig_Object=MibTableColumn
pdnAdslLinePowerManagementConfig=_PdnAdslLinePowerManagementConfig_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,1,1,4),_PdnAdslLinePowerManagementConfig_Type())
pdnAdslLinePowerManagementConfig.setMaxAccess(_H)
if mibBuilder.loadTexts:pdnAdslLinePowerManagementConfig.setStatus(_A)
class _PdnAdslLineSpectrumProfile_Type(SnmpAdminString):defaultValue=OctetString(_P);subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(1,32))
_PdnAdslLineSpectrumProfile_Type.__name__=_G
_PdnAdslLineSpectrumProfile_Object=MibTableColumn
pdnAdslLineSpectrumProfile=_PdnAdslLineSpectrumProfile_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,1,1,5),_PdnAdslLineSpectrumProfile_Type())
pdnAdslLineSpectrumProfile.setMaxAccess(_H)
if mibBuilder.loadTexts:pdnAdslLineSpectrumProfile.setStatus(_A)
class _PdnAdslLinePmMode_Type(Bits):namedValues=NamedValues(*(('idleStateL3',0),('lowPwrStateL1L2',1)))
_PdnAdslLinePmMode_Type.__name__=_O
_PdnAdslLinePmMode_Object=MibTableColumn
pdnAdslLinePmMode=_PdnAdslLinePmMode_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,1,1,6),_PdnAdslLinePmMode_Type())
pdnAdslLinePmMode.setMaxAccess(_H)
if mibBuilder.loadTexts:pdnAdslLinePmMode.setStatus(_A)
class _PdnAdslLineL0Time_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PdnAdslLineL0Time_Type.__name__=_D
_PdnAdslLineL0Time_Object=MibTableColumn
pdnAdslLineL0Time=_PdnAdslLineL0Time_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,1,1,7),_PdnAdslLineL0Time_Type())
pdnAdslLineL0Time.setMaxAccess(_H)
if mibBuilder.loadTexts:pdnAdslLineL0Time.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslLineL0Time.setUnits(_Q)
class _PdnAdslLineL2Time_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PdnAdslLineL2Time_Type.__name__=_D
_PdnAdslLineL2Time_Object=MibTableColumn
pdnAdslLineL2Time=_PdnAdslLineL2Time_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,1,1,8),_PdnAdslLineL2Time_Type())
pdnAdslLineL2Time.setMaxAccess(_H)
if mibBuilder.loadTexts:pdnAdslLineL2Time.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslLineL2Time.setUnits(_Q)
class _PdnAdslLineL2Atpr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_PdnAdslLineL2Atpr_Type.__name__=_D
_PdnAdslLineL2Atpr_Object=MibTableColumn
pdnAdslLineL2Atpr=_PdnAdslLineL2Atpr_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,1,1,9),_PdnAdslLineL2Atpr_Type())
pdnAdslLineL2Atpr.setMaxAccess(_H)
if mibBuilder.loadTexts:pdnAdslLineL2Atpr.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslLineL2Atpr.setUnits(_I)
class _PdnAdslLineLdsf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ldsfMode0',1),('ldsfMode1',2)))
_PdnAdslLineLdsf_Type.__name__=_E
_PdnAdslLineLdsf_Object=MibTableColumn
pdnAdslLineLdsf=_PdnAdslLineLdsf_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,1,1,10),_PdnAdslLineLdsf_Type())
pdnAdslLineLdsf.setMaxAccess(_H)
if mibBuilder.loadTexts:pdnAdslLineLdsf.setStatus(_A)
class _PdnAdslLineL2Atprt_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_PdnAdslLineL2Atprt_Type.__name__=_D
_PdnAdslLineL2Atprt_Object=MibTableColumn
pdnAdslLineL2Atprt=_PdnAdslLineL2Atprt_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,1,1,11),_PdnAdslLineL2Atprt_Type())
pdnAdslLineL2Atprt.setMaxAccess(_H)
if mibBuilder.loadTexts:pdnAdslLineL2Atprt.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslLineL2Atprt.setUnits(_I)
_PdnAdslLineSpectrumProfileTable_Object=MibTable
pdnAdslLineSpectrumProfileTable=_PdnAdslLineSpectrumProfileTable_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,2))
if mibBuilder.loadTexts:pdnAdslLineSpectrumProfileTable.setStatus(_A)
_PdnAdslLineSpectrumProfileEntry_Object=MibTableRow
pdnAdslLineSpectrumProfileEntry=_PdnAdslLineSpectrumProfileEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,2,1))
pdnAdslLineSpectrumProfileEntry.setIndexNames((1,_B,_R))
if mibBuilder.loadTexts:pdnAdslLineSpectrumProfileEntry.setStatus(_A)
class _PdnAdslLineSpectrumProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_PdnAdslLineSpectrumProfileName_Type.__name__=_G
_PdnAdslLineSpectrumProfileName_Object=MibTableColumn
pdnAdslLineSpectrumProfileName=_PdnAdslLineSpectrumProfileName_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,2,1,1),_PdnAdslLineSpectrumProfileName_Type())
pdnAdslLineSpectrumProfileName.setMaxAccess(_J)
if mibBuilder.loadTexts:pdnAdslLineSpectrumProfileName.setStatus(_A)
_PdnAdslLineSpectrumProfileRowStatus_Type=RowStatus
_PdnAdslLineSpectrumProfileRowStatus_Object=MibTableColumn
pdnAdslLineSpectrumProfileRowStatus=_PdnAdslLineSpectrumProfileRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,2,1,2),_PdnAdslLineSpectrumProfileRowStatus_Type())
pdnAdslLineSpectrumProfileRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnAdslLineSpectrumProfileRowStatus.setStatus(_A)
class _PdnAdslLineSpectrumModeSpecificPsdProfile_Type(SnmpAdminString):defaultValue=OctetString(_P);subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_PdnAdslLineSpectrumModeSpecificPsdProfile_Type.__name__=_G
_PdnAdslLineSpectrumModeSpecificPsdProfile_Object=MibTableColumn
pdnAdslLineSpectrumModeSpecificPsdProfile=_PdnAdslLineSpectrumModeSpecificPsdProfile_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,2,1,3),_PdnAdslLineSpectrumModeSpecificPsdProfile_Type())
pdnAdslLineSpectrumModeSpecificPsdProfile.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnAdslLineSpectrumModeSpecificPsdProfile.setStatus(_A)
class _PdnAdslLineSpectrumAtucCarMaskProfile_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PdnAdslLineSpectrumAtucCarMaskProfile_Type.__name__=_G
_PdnAdslLineSpectrumAtucCarMaskProfile_Object=MibTableColumn
pdnAdslLineSpectrumAtucCarMaskProfile=_PdnAdslLineSpectrumAtucCarMaskProfile_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,2,1,4),_PdnAdslLineSpectrumAtucCarMaskProfile_Type())
pdnAdslLineSpectrumAtucCarMaskProfile.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnAdslLineSpectrumAtucCarMaskProfile.setStatus(_A)
class _PdnAdslLineSpectrumAturCarMaskProfile_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PdnAdslLineSpectrumAturCarMaskProfile_Type.__name__=_G
_PdnAdslLineSpectrumAturCarMaskProfile_Object=MibTableColumn
pdnAdslLineSpectrumAturCarMaskProfile=_PdnAdslLineSpectrumAturCarMaskProfile_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,2,1,5),_PdnAdslLineSpectrumAturCarMaskProfile_Type())
pdnAdslLineSpectrumAturCarMaskProfile.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnAdslLineSpectrumAturCarMaskProfile.setStatus(_A)
_PdnAdslModeSpecificPsdConfTable_Object=MibTable
pdnAdslModeSpecificPsdConfTable=_PdnAdslModeSpecificPsdConfTable_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,3))
if mibBuilder.loadTexts:pdnAdslModeSpecificPsdConfTable.setStatus(_A)
_PdnAdslModeSpecificPsdConfEntry_Object=MibTableRow
pdnAdslModeSpecificPsdConfEntry=_PdnAdslModeSpecificPsdConfEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,3,1))
pdnAdslModeSpecificPsdConfEntry.setIndexNames((0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:pdnAdslModeSpecificPsdConfEntry.setStatus(_A)
class _PdnAdslModeSpecificPsdConfProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_PdnAdslModeSpecificPsdConfProfileName_Type.__name__=_G
_PdnAdslModeSpecificPsdConfProfileName_Object=MibTableColumn
pdnAdslModeSpecificPsdConfProfileName=_PdnAdslModeSpecificPsdConfProfileName_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,3,1,1),_PdnAdslModeSpecificPsdConfProfileName_Type())
pdnAdslModeSpecificPsdConfProfileName.setMaxAccess(_J)
if mibBuilder.loadTexts:pdnAdslModeSpecificPsdConfProfileName.setStatus(_A)
class _PdnAdslModeSpecificPsdConfAdslMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('adsl2',1),('adsl2NoSplitter',2),('adsl2plus',3)))
_PdnAdslModeSpecificPsdConfAdslMode_Type.__name__=_E
_PdnAdslModeSpecificPsdConfAdslMode_Object=MibTableColumn
pdnAdslModeSpecificPsdConfAdslMode=_PdnAdslModeSpecificPsdConfAdslMode_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,3,1,2),_PdnAdslModeSpecificPsdConfAdslMode_Type())
pdnAdslModeSpecificPsdConfAdslMode.setMaxAccess(_J)
if mibBuilder.loadTexts:pdnAdslModeSpecificPsdConfAdslMode.setStatus(_A)
_PdnAdslModeSpecificPsdConfRowStatus_Type=RowStatus
_PdnAdslModeSpecificPsdConfRowStatus_Object=MibTableColumn
pdnAdslModeSpecificPsdConfRowStatus=_PdnAdslModeSpecificPsdConfRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,3,1,3),_PdnAdslModeSpecificPsdConfRowStatus_Type())
pdnAdslModeSpecificPsdConfRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnAdslModeSpecificPsdConfRowStatus.setStatus(_A)
class _PdnAdslModeSpecificPsdConfAdslPsdConfProfile_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_PdnAdslModeSpecificPsdConfAdslPsdConfProfile_Type.__name__=_G
_PdnAdslModeSpecificPsdConfAdslPsdConfProfile_Object=MibTableColumn
pdnAdslModeSpecificPsdConfAdslPsdConfProfile=_PdnAdslModeSpecificPsdConfAdslPsdConfProfile_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,3,1,4),_PdnAdslModeSpecificPsdConfAdslPsdConfProfile_Type())
pdnAdslModeSpecificPsdConfAdslPsdConfProfile.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnAdslModeSpecificPsdConfAdslPsdConfProfile.setStatus(_A)
_PdnAdslPsdConfTable_Object=MibTable
pdnAdslPsdConfTable=_PdnAdslPsdConfTable_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,4))
if mibBuilder.loadTexts:pdnAdslPsdConfTable.setStatus(_A)
_PdnAdslPsdConfEntry_Object=MibTableRow
pdnAdslPsdConfEntry=_PdnAdslPsdConfEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,4,1))
pdnAdslPsdConfEntry.setIndexNames((1,_B,_U))
if mibBuilder.loadTexts:pdnAdslPsdConfEntry.setStatus(_A)
class _PdnAdslPsdConfProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_PdnAdslPsdConfProfileName_Type.__name__=_G
_PdnAdslPsdConfProfileName_Object=MibTableColumn
pdnAdslPsdConfProfileName=_PdnAdslPsdConfProfileName_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,4,1,1),_PdnAdslPsdConfProfileName_Type())
pdnAdslPsdConfProfileName.setMaxAccess(_J)
if mibBuilder.loadTexts:pdnAdslPsdConfProfileName.setStatus(_A)
_PdnAdslPsdConfRowStatus_Type=RowStatus
_PdnAdslPsdConfRowStatus_Object=MibTableColumn
pdnAdslPsdConfRowStatus=_PdnAdslPsdConfRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,4,1,2),_PdnAdslPsdConfRowStatus_Type())
pdnAdslPsdConfRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnAdslPsdConfRowStatus.setStatus(_A)
class _PdnAdslPsdConfAtucMaxNomPsd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-800,-400))
_PdnAdslPsdConfAtucMaxNomPsd_Type.__name__=_E
_PdnAdslPsdConfAtucMaxNomPsd_Object=MibTableColumn
pdnAdslPsdConfAtucMaxNomPsd=_PdnAdslPsdConfAtucMaxNomPsd_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,4,1,3),_PdnAdslPsdConfAtucMaxNomPsd_Type())
pdnAdslPsdConfAtucMaxNomPsd.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnAdslPsdConfAtucMaxNomPsd.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslPsdConfAtucMaxNomPsd.setUnits(_V)
class _PdnAdslPsdConfAturMaxNomPsd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-650,-380))
_PdnAdslPsdConfAturMaxNomPsd_Type.__name__=_E
_PdnAdslPsdConfAturMaxNomPsd_Object=MibTableColumn
pdnAdslPsdConfAturMaxNomPsd=_PdnAdslPsdConfAturMaxNomPsd_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,4,1,4),_PdnAdslPsdConfAturMaxNomPsd_Type())
pdnAdslPsdConfAturMaxNomPsd.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnAdslPsdConfAturMaxNomPsd.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslPsdConfAturMaxNomPsd.setUnits(_V)
class _PdnAdslPsdConfAtucMaxNomAtp_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PdnAdslPsdConfAtucMaxNomAtp_Type.__name__=_D
_PdnAdslPsdConfAtucMaxNomAtp_Object=MibTableColumn
pdnAdslPsdConfAtucMaxNomAtp=_PdnAdslPsdConfAtucMaxNomAtp_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,4,1,5),_PdnAdslPsdConfAtucMaxNomAtp_Type())
pdnAdslPsdConfAtucMaxNomAtp.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnAdslPsdConfAtucMaxNomAtp.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslPsdConfAtucMaxNomAtp.setUnits(_L)
class _PdnAdslPsdConfAturMaxNomAtp_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PdnAdslPsdConfAturMaxNomAtp_Type.__name__=_D
_PdnAdslPsdConfAturMaxNomAtp_Object=MibTableColumn
pdnAdslPsdConfAturMaxNomAtp=_PdnAdslPsdConfAturMaxNomAtp_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,4,1,6),_PdnAdslPsdConfAturMaxNomAtp_Type())
pdnAdslPsdConfAturMaxNomAtp.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnAdslPsdConfAturMaxNomAtp.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslPsdConfAturMaxNomAtp.setUnits(_L)
class _PdnAdslPsdConfAtucMaxRxPwr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-255,255),ValueRangeConstraint(2048,2048))
_PdnAdslPsdConfAtucMaxRxPwr_Type.__name__=_E
_PdnAdslPsdConfAtucMaxRxPwr_Object=MibTableColumn
pdnAdslPsdConfAtucMaxRxPwr=_PdnAdslPsdConfAtucMaxRxPwr_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,4,1,7),_PdnAdslPsdConfAtucMaxRxPwr_Type())
pdnAdslPsdConfAtucMaxRxPwr.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnAdslPsdConfAtucMaxRxPwr.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslPsdConfAtucMaxRxPwr.setUnits(_L)
_PdnAdslCarMaskTable_Object=MibTable
pdnAdslCarMaskTable=_PdnAdslCarMaskTable_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,5))
if mibBuilder.loadTexts:pdnAdslCarMaskTable.setStatus(_A)
_PdnAdslCarMaskEntry_Object=MibTableRow
pdnAdslCarMaskEntry=_PdnAdslCarMaskEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,5,1))
pdnAdslCarMaskEntry.setIndexNames((0,_B,_W),(0,_B,_X))
if mibBuilder.loadTexts:pdnAdslCarMaskEntry.setStatus(_A)
class _PdnAdslCarMaskProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_PdnAdslCarMaskProfileName_Type.__name__=_G
_PdnAdslCarMaskProfileName_Object=MibTableColumn
pdnAdslCarMaskProfileName=_PdnAdslCarMaskProfileName_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,5,1,1),_PdnAdslCarMaskProfileName_Type())
pdnAdslCarMaskProfileName.setMaxAccess(_J)
if mibBuilder.loadTexts:pdnAdslCarMaskProfileName.setStatus(_A)
_PdnAdslCarMaskSubCarrierIndex_Type=Unsigned32
_PdnAdslCarMaskSubCarrierIndex_Object=MibTableColumn
pdnAdslCarMaskSubCarrierIndex=_PdnAdslCarMaskSubCarrierIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,5,1,2),_PdnAdslCarMaskSubCarrierIndex_Type())
pdnAdslCarMaskSubCarrierIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:pdnAdslCarMaskSubCarrierIndex.setStatus(_A)
_PdnAdslCarMaskRowStatus_Type=RowStatus
_PdnAdslCarMaskRowStatus_Object=MibTableColumn
pdnAdslCarMaskRowStatus=_PdnAdslCarMaskRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,5,1,3),_PdnAdslCarMaskRowStatus_Type())
pdnAdslCarMaskRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnAdslCarMaskRowStatus.setStatus(_A)
class _PdnAdslCarMaskSubCarrierStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('masked',1))
_PdnAdslCarMaskSubCarrierStatus_Type.__name__=_E
_PdnAdslCarMaskSubCarrierStatus_Object=MibTableColumn
pdnAdslCarMaskSubCarrierStatus=_PdnAdslCarMaskSubCarrierStatus_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,5,1,4),_PdnAdslCarMaskSubCarrierStatus_Type())
pdnAdslCarMaskSubCarrierStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAdslCarMaskSubCarrierStatus.setStatus(_A)
_PdnAdslLineStatusTable_Object=MibTable
pdnAdslLineStatusTable=_PdnAdslLineStatusTable_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,6))
if mibBuilder.loadTexts:pdnAdslLineStatusTable.setStatus(_A)
_PdnAdslLineStatusEntry_Object=MibTableRow
pdnAdslLineStatusEntry=_PdnAdslLineStatusEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,6,1))
pdnAdslLineStatusEntry.setIndexNames((0,_M,_N))
if mibBuilder.loadTexts:pdnAdslLineStatusEntry.setStatus(_A)
class _PdnAdslLineStatusAtucLineAtn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1270),ValueRangeConstraint(2048,2048))
_PdnAdslLineStatusAtucLineAtn_Type.__name__=_D
_PdnAdslLineStatusAtucLineAtn_Object=MibTableColumn
pdnAdslLineStatusAtucLineAtn=_PdnAdslLineStatusAtucLineAtn_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,6,1,1),_PdnAdslLineStatusAtucLineAtn_Type())
pdnAdslLineStatusAtucLineAtn.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAdslLineStatusAtucLineAtn.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslLineStatusAtucLineAtn.setUnits(_K)
class _PdnAdslLineStatusAturLineAtn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1270),ValueRangeConstraint(2048,2048))
_PdnAdslLineStatusAturLineAtn_Type.__name__=_D
_PdnAdslLineStatusAturLineAtn_Object=MibTableColumn
pdnAdslLineStatusAturLineAtn=_PdnAdslLineStatusAturLineAtn_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,6,1,2),_PdnAdslLineStatusAturLineAtn_Type())
pdnAdslLineStatusAturLineAtn.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAdslLineStatusAturLineAtn.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslLineStatusAturLineAtn.setUnits(_K)
class _PdnAdslLineStatusAtucSignalAtn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1270),ValueRangeConstraint(2048,2048))
_PdnAdslLineStatusAtucSignalAtn_Type.__name__=_D
_PdnAdslLineStatusAtucSignalAtn_Object=MibTableColumn
pdnAdslLineStatusAtucSignalAtn=_PdnAdslLineStatusAtucSignalAtn_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,6,1,3),_PdnAdslLineStatusAtucSignalAtn_Type())
pdnAdslLineStatusAtucSignalAtn.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAdslLineStatusAtucSignalAtn.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslLineStatusAtucSignalAtn.setUnits(_K)
class _PdnAdslLineStatusAturSignalAtn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1270),ValueRangeConstraint(2048,2048))
_PdnAdslLineStatusAturSignalAtn_Type.__name__=_D
_PdnAdslLineStatusAturSignalAtn_Object=MibTableColumn
pdnAdslLineStatusAturSignalAtn=_PdnAdslLineStatusAturSignalAtn_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,6,1,4),_PdnAdslLineStatusAturSignalAtn_Type())
pdnAdslLineStatusAturSignalAtn.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAdslLineStatusAturSignalAtn.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslLineStatusAturSignalAtn.setUnits(_K)
class _PdnAdslLineStatusAtucSnrMgn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-640,630),ValueRangeConstraint(2048,2048))
_PdnAdslLineStatusAtucSnrMgn_Type.__name__=_E
_PdnAdslLineStatusAtucSnrMgn_Object=MibTableColumn
pdnAdslLineStatusAtucSnrMgn=_PdnAdslLineStatusAtucSnrMgn_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,6,1,5),_PdnAdslLineStatusAtucSnrMgn_Type())
pdnAdslLineStatusAtucSnrMgn.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAdslLineStatusAtucSnrMgn.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslLineStatusAtucSnrMgn.setUnits(_K)
class _PdnAdslLineStatusAturSnrMgn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-640,630),ValueRangeConstraint(2048,2048))
_PdnAdslLineStatusAturSnrMgn_Type.__name__=_E
_PdnAdslLineStatusAturSnrMgn_Object=MibTableColumn
pdnAdslLineStatusAturSnrMgn=_PdnAdslLineStatusAturSnrMgn_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,6,1,6),_PdnAdslLineStatusAturSnrMgn_Type())
pdnAdslLineStatusAturSnrMgn.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAdslLineStatusAturSnrMgn.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslLineStatusAturSnrMgn.setUnits(_K)
_PdnAdslLineStatusAtucMaxAttainableLineRate_Type=Gauge32
_PdnAdslLineStatusAtucMaxAttainableLineRate_Object=MibTableColumn
pdnAdslLineStatusAtucMaxAttainableLineRate=_PdnAdslLineStatusAtucMaxAttainableLineRate_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,6,1,7),_PdnAdslLineStatusAtucMaxAttainableLineRate_Type())
pdnAdslLineStatusAtucMaxAttainableLineRate.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAdslLineStatusAtucMaxAttainableLineRate.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslLineStatusAtucMaxAttainableLineRate.setUnits('bps')
_PdnAdslLineStatusAturMaxAttainableLineRate_Type=Gauge32
_PdnAdslLineStatusAturMaxAttainableLineRate_Object=MibTableColumn
pdnAdslLineStatusAturMaxAttainableLineRate=_PdnAdslLineStatusAturMaxAttainableLineRate_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,6,1,8),_PdnAdslLineStatusAturMaxAttainableLineRate_Type())
pdnAdslLineStatusAturMaxAttainableLineRate.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAdslLineStatusAturMaxAttainableLineRate.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslLineStatusAturMaxAttainableLineRate.setUnits('bps')
class _PdnAdslLineStatusAtucActAtp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-310,310),ValueRangeConstraint(2048,2048))
_PdnAdslLineStatusAtucActAtp_Type.__name__=_E
_PdnAdslLineStatusAtucActAtp_Object=MibTableColumn
pdnAdslLineStatusAtucActAtp=_PdnAdslLineStatusAtucActAtp_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,6,1,9),_PdnAdslLineStatusAtucActAtp_Type())
pdnAdslLineStatusAtucActAtp.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAdslLineStatusAtucActAtp.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslLineStatusAtucActAtp.setUnits(_L)
class _PdnAdslLineStatusAturActAtp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-310,310),ValueRangeConstraint(2048,2048))
_PdnAdslLineStatusAturActAtp_Type.__name__=_E
_PdnAdslLineStatusAturActAtp_Object=MibTableColumn
pdnAdslLineStatusAturActAtp=_PdnAdslLineStatusAturActAtp_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,6,1,10),_PdnAdslLineStatusAturActAtp_Type())
pdnAdslLineStatusAturActAtp.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAdslLineStatusAturActAtp.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslLineStatusAturActAtp.setUnits(_L)
_PdnAdslLineSubCarStatusTable_Object=MibTable
pdnAdslLineSubCarStatusTable=_PdnAdslLineSubCarStatusTable_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,7))
if mibBuilder.loadTexts:pdnAdslLineSubCarStatusTable.setStatus(_A)
_PdnAdslLineSubCarStatusEntry_Object=MibTableRow
pdnAdslLineSubCarStatusEntry=_PdnAdslLineSubCarStatusEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,7,1))
pdnAdslLineSubCarStatusEntry.setIndexNames((0,_M,_N),(0,_B,_Y))
if mibBuilder.loadTexts:pdnAdslLineSubCarStatusEntry.setStatus(_A)
_PdnAdslLineCarrierIndex_Type=Unsigned32
_PdnAdslLineCarrierIndex_Object=MibTableColumn
pdnAdslLineCarrierIndex=_PdnAdslLineCarrierIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,7,1,1),_PdnAdslLineCarrierIndex_Type())
pdnAdslLineCarrierIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:pdnAdslLineCarrierIndex.setStatus(_A)
class _PdnAdslLineSubCarAtucHlinPs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,-32768),ValueRangeConstraint(-32767,32767))
_PdnAdslLineSubCarAtucHlinPs_Type.__name__=_E
_PdnAdslLineSubCarAtucHlinPs_Object=MibTableColumn
pdnAdslLineSubCarAtucHlinPs=_PdnAdslLineSubCarAtucHlinPs_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,7,1,2),_PdnAdslLineSubCarAtucHlinPs_Type())
pdnAdslLineSubCarAtucHlinPs.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAdslLineSubCarAtucHlinPs.setStatus(_A)
class _PdnAdslLineSubCarAturHlinPs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,-32768),ValueRangeConstraint(-32767,32767))
_PdnAdslLineSubCarAturHlinPs_Type.__name__=_E
_PdnAdslLineSubCarAturHlinPs_Object=MibTableColumn
pdnAdslLineSubCarAturHlinPs=_PdnAdslLineSubCarAturHlinPs_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,7,1,3),_PdnAdslLineSubCarAturHlinPs_Type())
pdnAdslLineSubCarAturHlinPs.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAdslLineSubCarAturHlinPs.setStatus(_A)
class _PdnAdslLineSubCarAtucHlogMt_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PdnAdslLineSubCarAtucHlogMt_Type.__name__=_D
_PdnAdslLineSubCarAtucHlogMt_Object=MibTableColumn
pdnAdslLineSubCarAtucHlogMt=_PdnAdslLineSubCarAtucHlogMt_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,7,1,4),_PdnAdslLineSubCarAtucHlogMt_Type())
pdnAdslLineSubCarAtucHlogMt.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAdslLineSubCarAtucHlogMt.setStatus(_A)
class _PdnAdslLineSubCarAturHlogMt_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PdnAdslLineSubCarAturHlogMt_Type.__name__=_D
_PdnAdslLineSubCarAturHlogMt_Object=MibTableColumn
pdnAdslLineSubCarAturHlogMt=_PdnAdslLineSubCarAturHlogMt_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,7,1,5),_PdnAdslLineSubCarAturHlogMt_Type())
pdnAdslLineSubCarAturHlogMt.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAdslLineSubCarAturHlogMt.setStatus(_A)
class _PdnAdslLineSubCarAtucQlnPs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254),ValueRangeConstraint(255,255))
_PdnAdslLineSubCarAtucQlnPs_Type.__name__=_D
_PdnAdslLineSubCarAtucQlnPs_Object=MibTableColumn
pdnAdslLineSubCarAtucQlnPs=_PdnAdslLineSubCarAtucQlnPs_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,7,1,6),_PdnAdslLineSubCarAtucQlnPs_Type())
pdnAdslLineSubCarAtucQlnPs.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAdslLineSubCarAtucQlnPs.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslLineSubCarAtucQlnPs.setUnits(_I)
class _PdnAdslLineSubCarAturQlnPs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254),ValueRangeConstraint(255,255))
_PdnAdslLineSubCarAturQlnPs_Type.__name__=_D
_PdnAdslLineSubCarAturQlnPs_Object=MibTableColumn
pdnAdslLineSubCarAturQlnPs=_PdnAdslLineSubCarAturQlnPs_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,7,1,7),_PdnAdslLineSubCarAturQlnPs_Type())
pdnAdslLineSubCarAturQlnPs.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAdslLineSubCarAturQlnPs.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslLineSubCarAturQlnPs.setUnits(_I)
class _PdnAdslLineSubCarAtucSnrPs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254),ValueRangeConstraint(255,255))
_PdnAdslLineSubCarAtucSnrPs_Type.__name__=_D
_PdnAdslLineSubCarAtucSnrPs_Object=MibTableColumn
pdnAdslLineSubCarAtucSnrPs=_PdnAdslLineSubCarAtucSnrPs_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,7,1,8),_PdnAdslLineSubCarAtucSnrPs_Type())
pdnAdslLineSubCarAtucSnrPs.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAdslLineSubCarAtucSnrPs.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslLineSubCarAtucSnrPs.setUnits(_I)
class _PdnAdslLineSubCarAturSnrPs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254),ValueRangeConstraint(255,255))
_PdnAdslLineSubCarAturSnrPs_Type.__name__=_D
_PdnAdslLineSubCarAturSnrPs_Object=MibTableColumn
pdnAdslLineSubCarAturSnrPs=_PdnAdslLineSubCarAturSnrPs_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,7,1,9),_PdnAdslLineSubCarAturSnrPs_Type())
pdnAdslLineSubCarAturSnrPs.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAdslLineSubCarAturSnrPs.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslLineSubCarAturSnrPs.setUnits(_I)
class _PdnAdslLineSubCarAtucBitsPs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_PdnAdslLineSubCarAtucBitsPs_Type.__name__=_D
_PdnAdslLineSubCarAtucBitsPs_Object=MibTableColumn
pdnAdslLineSubCarAtucBitsPs=_PdnAdslLineSubCarAtucBitsPs_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,7,1,10),_PdnAdslLineSubCarAtucBitsPs_Type())
pdnAdslLineSubCarAtucBitsPs.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAdslLineSubCarAtucBitsPs.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslLineSubCarAtucBitsPs.setUnits(_O)
class _PdnAdslLineSubCarAturBitsPs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_PdnAdslLineSubCarAturBitsPs_Type.__name__=_D
_PdnAdslLineSubCarAturBitsPs_Object=MibTableColumn
pdnAdslLineSubCarAturBitsPs=_PdnAdslLineSubCarAturBitsPs_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,7,1,11),_PdnAdslLineSubCarAturBitsPs_Type())
pdnAdslLineSubCarAturBitsPs.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAdslLineSubCarAturBitsPs.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslLineSubCarAturBitsPs.setUnits(_O)
class _PdnAdslLineSubCarAtucHlogPs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1022),ValueRangeConstraint(1023,1023))
_PdnAdslLineSubCarAtucHlogPs_Type.__name__=_D
_PdnAdslLineSubCarAtucHlogPs_Object=MibTableColumn
pdnAdslLineSubCarAtucHlogPs=_PdnAdslLineSubCarAtucHlogPs_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,7,1,12),_PdnAdslLineSubCarAtucHlogPs_Type())
pdnAdslLineSubCarAtucHlogPs.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAdslLineSubCarAtucHlogPs.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslLineSubCarAtucHlogPs.setUnits(_I)
class _PdnAdslLineSubCarAturHlogPs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1022),ValueRangeConstraint(1023,1023))
_PdnAdslLineSubCarAturHlogPs_Type.__name__=_D
_PdnAdslLineSubCarAturHlogPs_Object=MibTableColumn
pdnAdslLineSubCarAturHlogPs=_PdnAdslLineSubCarAturHlogPs_Object((1,3,6,1,4,1,1795,2,24,2,6,24,1,7,1,13),_PdnAdslLineSubCarAturHlogPs_Type())
pdnAdslLineSubCarAturHlogPs.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAdslLineSubCarAturHlogPs.setStatus(_A)
if mibBuilder.loadTexts:pdnAdslLineSubCarAturHlogPs.setUnits(_I)
_PdnAdslLineExtAFNs_ObjectIdentity=ObjectIdentity
pdnAdslLineExtAFNs=_PdnAdslLineExtAFNs_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,24,2))
_PdnAdslLineExtConformance_ObjectIdentity=ObjectIdentity
pdnAdslLineExtConformance=_PdnAdslLineExtConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,24,3))
_PdnAdslLineExtCompliances_ObjectIdentity=ObjectIdentity
pdnAdslLineExtCompliances=_PdnAdslLineExtCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,24,3,1))
_PdnAdslLineExtGroups_ObjectIdentity=ObjectIdentity
pdnAdslLineExtGroups=_PdnAdslLineExtGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,24,3,2))
_PdnAdslLineExtObjGroups_ObjectIdentity=ObjectIdentity
pdnAdslLineExtObjGroups=_PdnAdslLineExtObjGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,24,3,2,1))
_PdnAdslLineExtAfnGroups_ObjectIdentity=ObjectIdentity
pdnAdslLineExtAfnGroups=_PdnAdslLineExtAfnGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,24,3,2,2))
_PdnAdslLineExtNtfyGroups_ObjectIdentity=ObjectIdentity
pdnAdslLineExtNtfyGroups=_PdnAdslLineExtNtfyGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,24,3,2,3))
pdnAdslLineExtGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,24,3,2,1,1))
pdnAdslLineExtGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:pdnAdslLineExtGroup.setStatus(_A)
pdnAdslLineSpectrumGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,24,3,2,1,2))
pdnAdslLineSpectrumGroup.setObjects(*((_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:pdnAdslLineSpectrumGroup.setStatus(_A)
pdnAdslModeSpecificPsdGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,24,3,2,1,3))
pdnAdslModeSpecificPsdGroup.setObjects(*((_B,_n),(_B,_o)))
if mibBuilder.loadTexts:pdnAdslModeSpecificPsdGroup.setStatus(_A)
pdnAdslPsdGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,24,3,2,1,4))
pdnAdslPsdGroup.setObjects(*((_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:pdnAdslPsdGroup.setStatus(_A)
pdnAdslCarMaskGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,24,3,2,1,5))
pdnAdslCarMaskGroup.setObjects(*((_B,_v),(_B,_w)))
if mibBuilder.loadTexts:pdnAdslCarMaskGroup.setStatus(_A)
pdnAdslLineL2AtprtGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,24,3,2,1,6))
pdnAdslLineL2AtprtGroup.setObjects((_B,_x))
if mibBuilder.loadTexts:pdnAdslLineL2AtprtGroup.setStatus(_A)
pdnAdslLineStatusLineAtnGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,24,3,2,1,7))
pdnAdslLineStatusLineAtnGroup.setObjects(*((_B,_y),(_B,_z)))
if mibBuilder.loadTexts:pdnAdslLineStatusLineAtnGroup.setStatus(_A)
pdnAdslLineStatusSignalAtnGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,24,3,2,1,8))
pdnAdslLineStatusSignalAtnGroup.setObjects(*((_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:pdnAdslLineStatusSignalAtnGroup.setStatus(_A)
pdnAdslLineStatusSnrMgnGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,24,3,2,1,9))
pdnAdslLineStatusSnrMgnGroup.setObjects(*((_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:pdnAdslLineStatusSnrMgnGroup.setStatus(_A)
pdnAdslLineStatusMaxattainableLineRateGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,24,3,2,1,10))
pdnAdslLineStatusMaxattainableLineRateGroup.setObjects(*((_B,_A4),(_B,_A5)))
if mibBuilder.loadTexts:pdnAdslLineStatusMaxattainableLineRateGroup.setStatus(_A)
pdnAdslLineStatusActAtpGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,24,3,2,1,11))
pdnAdslLineStatusActAtpGroup.setObjects(*((_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:pdnAdslLineStatusActAtpGroup.setStatus(_A)
pdnAdslLineSubCarStatusHlinGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,24,3,2,1,12))
pdnAdslLineSubCarStatusHlinGroup.setObjects(*((_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:pdnAdslLineSubCarStatusHlinGroup.setStatus(_A)
pdnAdslLineSubCarStatusHlogMtGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,24,3,2,1,13))
pdnAdslLineSubCarStatusHlogMtGroup.setObjects(*((_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:pdnAdslLineSubCarStatusHlogMtGroup.setStatus(_A)
pdnAdslLineSubCarStatusQlnGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,24,3,2,1,14))
pdnAdslLineSubCarStatusQlnGroup.setObjects(*((_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:pdnAdslLineSubCarStatusQlnGroup.setStatus(_A)
pdnAdslLineSubCarStatusSnrGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,24,3,2,1,15))
pdnAdslLineSubCarStatusSnrGroup.setObjects(*((_B,_AE),(_B,_AF)))
if mibBuilder.loadTexts:pdnAdslLineSubCarStatusSnrGroup.setStatus(_A)
pdnAdslLineSubCarStatusBitsGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,24,3,2,1,16))
pdnAdslLineSubCarStatusBitsGroup.setObjects(*((_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:pdnAdslLineSubCarStatusBitsGroup.setStatus(_A)
pdnAdslLineSubCarStatusHlogGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,24,3,2,1,17))
pdnAdslLineSubCarStatusHlogGroup.setObjects(*((_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:pdnAdslLineSubCarStatusHlogGroup.setStatus(_A)
pdnAdslLineExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,6,24,3,1,1))
pdnAdslLineExtMIBCompliance.setObjects(*((_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa)))
if mibBuilder.loadTexts:pdnAdslLineExtMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'PdnAdslTransmissionModeType':PdnAdslTransmissionModeType,'pdnAdslLineExtMIB':pdnAdslLineExtMIB,'pdnAdslLineExtNotifications':pdnAdslLineExtNotifications,'pdnAdslLineExtObjects':pdnAdslLineExtObjects,'pdnAdslLineExtTable':pdnAdslLineExtTable,'pdnAdslLineExtEntry':pdnAdslLineExtEntry,_Z:pdnAdslLineTransAtucCap,_a:pdnAdslLineTransAtucConfig,_b:pdnAdslLineTransAtucActual,_c:pdnAdslLinePowerManagementConfig,_d:pdnAdslLineSpectrumProfile,_e:pdnAdslLinePmMode,_f:pdnAdslLineL0Time,_g:pdnAdslLineL2Time,_h:pdnAdslLineL2Atpr,_i:pdnAdslLineLdsf,_x:pdnAdslLineL2Atprt,'pdnAdslLineSpectrumProfileTable':pdnAdslLineSpectrumProfileTable,'pdnAdslLineSpectrumProfileEntry':pdnAdslLineSpectrumProfileEntry,_R:pdnAdslLineSpectrumProfileName,_j:pdnAdslLineSpectrumProfileRowStatus,_k:pdnAdslLineSpectrumModeSpecificPsdProfile,_l:pdnAdslLineSpectrumAtucCarMaskProfile,_m:pdnAdslLineSpectrumAturCarMaskProfile,'pdnAdslModeSpecificPsdConfTable':pdnAdslModeSpecificPsdConfTable,'pdnAdslModeSpecificPsdConfEntry':pdnAdslModeSpecificPsdConfEntry,_S:pdnAdslModeSpecificPsdConfProfileName,_T:pdnAdslModeSpecificPsdConfAdslMode,_o:pdnAdslModeSpecificPsdConfRowStatus,_n:pdnAdslModeSpecificPsdConfAdslPsdConfProfile,'pdnAdslPsdConfTable':pdnAdslPsdConfTable,'pdnAdslPsdConfEntry':pdnAdslPsdConfEntry,_U:pdnAdslPsdConfProfileName,_p:pdnAdslPsdConfRowStatus,_q:pdnAdslPsdConfAtucMaxNomPsd,_r:pdnAdslPsdConfAturMaxNomPsd,_s:pdnAdslPsdConfAtucMaxNomAtp,_t:pdnAdslPsdConfAturMaxNomAtp,_u:pdnAdslPsdConfAtucMaxRxPwr,'pdnAdslCarMaskTable':pdnAdslCarMaskTable,'pdnAdslCarMaskEntry':pdnAdslCarMaskEntry,_W:pdnAdslCarMaskProfileName,_X:pdnAdslCarMaskSubCarrierIndex,_v:pdnAdslCarMaskRowStatus,_w:pdnAdslCarMaskSubCarrierStatus,'pdnAdslLineStatusTable':pdnAdslLineStatusTable,'pdnAdslLineStatusEntry':pdnAdslLineStatusEntry,_y:pdnAdslLineStatusAtucLineAtn,_z:pdnAdslLineStatusAturLineAtn,_A0:pdnAdslLineStatusAtucSignalAtn,_A1:pdnAdslLineStatusAturSignalAtn,_A2:pdnAdslLineStatusAtucSnrMgn,_A3:pdnAdslLineStatusAturSnrMgn,_A4:pdnAdslLineStatusAtucMaxAttainableLineRate,_A5:pdnAdslLineStatusAturMaxAttainableLineRate,_A6:pdnAdslLineStatusAtucActAtp,_A7:pdnAdslLineStatusAturActAtp,'pdnAdslLineSubCarStatusTable':pdnAdslLineSubCarStatusTable,'pdnAdslLineSubCarStatusEntry':pdnAdslLineSubCarStatusEntry,_Y:pdnAdslLineCarrierIndex,_A8:pdnAdslLineSubCarAtucHlinPs,_A9:pdnAdslLineSubCarAturHlinPs,_AA:pdnAdslLineSubCarAtucHlogMt,_AB:pdnAdslLineSubCarAturHlogMt,_AC:pdnAdslLineSubCarAtucQlnPs,_AD:pdnAdslLineSubCarAturQlnPs,_AE:pdnAdslLineSubCarAtucSnrPs,_AF:pdnAdslLineSubCarAturSnrPs,_AG:pdnAdslLineSubCarAtucBitsPs,_AH:pdnAdslLineSubCarAturBitsPs,_AI:pdnAdslLineSubCarAtucHlogPs,_AJ:pdnAdslLineSubCarAturHlogPs,'pdnAdslLineExtAFNs':pdnAdslLineExtAFNs,'pdnAdslLineExtConformance':pdnAdslLineExtConformance,'pdnAdslLineExtCompliances':pdnAdslLineExtCompliances,'pdnAdslLineExtMIBCompliance':pdnAdslLineExtMIBCompliance,'pdnAdslLineExtGroups':pdnAdslLineExtGroups,'pdnAdslLineExtObjGroups':pdnAdslLineExtObjGroups,_AK:pdnAdslLineExtGroup,_AL:pdnAdslLineSpectrumGroup,_AM:pdnAdslModeSpecificPsdGroup,_AN:pdnAdslPsdGroup,_AO:pdnAdslCarMaskGroup,_AP:pdnAdslLineL2AtprtGroup,_AQ:pdnAdslLineStatusLineAtnGroup,_AR:pdnAdslLineStatusSignalAtnGroup,_AS:pdnAdslLineStatusSnrMgnGroup,_AT:pdnAdslLineStatusMaxattainableLineRateGroup,_AU:pdnAdslLineStatusActAtpGroup,_AV:pdnAdslLineSubCarStatusHlinGroup,_AW:pdnAdslLineSubCarStatusHlogMtGroup,_AX:pdnAdslLineSubCarStatusQlnGroup,_AY:pdnAdslLineSubCarStatusSnrGroup,_AZ:pdnAdslLineSubCarStatusBitsGroup,_Aa:pdnAdslLineSubCarStatusHlogGroup,'pdnAdslLineExtAfnGroups':pdnAdslLineExtAfnGroups,'pdnAdslLineExtNtfyGroups':pdnAdslLineExtNtfyGroups})