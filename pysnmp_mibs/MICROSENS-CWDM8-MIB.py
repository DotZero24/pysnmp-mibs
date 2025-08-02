_AI='portLineLink'
_AH='portLocalLink'
_AG='powerFanStatus'
_AF='deviceTempShutdown'
_AE='deviceTempAlarm'
_AD='powerStatus'
_AC='deviceMajorAlarm'
_AB='deviceMinorAlarm'
_AA='passiveId'
_A9='not-in-use'
_A8='not-active'
_A7='lineModuleId'
_A6='speed-400MBytes-per-sec'
_A5='speed-200MBytes-per-sec'
_A4='speed-100MBytes-per-sec'
_A3='twin-axial-pair'
_A2='shielded-twisted-pair'
_A1='miniature-coax'
_A0='video-coax'
_z='multi-mode-62-5'
_y='multi-mode-50'
_x='single-mode'
_w='longwave-laser-LC'
_v='electrical-inter-enclosure'
_u='electrical-intra-enclosure'
_t='shortwave-laser-no-OFC'
_s='shortwave-laser-OFC'
_r='longwave-laser-LL'
_q='short-distance'
_p='intermediate-distance'
_o='long-distance'
_n='oc48-long-reach'
_m='oc48-intermediate-reach'
_l='oc48-short-reach'
_k='oc12-single-mode-long-reach'
_j='oc12-single-mode-intermediate-reach'
_i='oc12-multi-mode-short-reach'
_h='oc3-single-mode-long-reach'
_g='oc3-single-mode-intermediate-reach'
_f='oc3-multi-mode-short-reach'
_e='copperpigtail'
_d='hssdc2'
_c='opticalpigtail'
_b='fiberjack'
_a='coaxial-headers'
_Z='bnc-tnc'
_Y='style2-copper'
_X='style1-copper'
_W='localModuleId'
_V='installed'
_U='not-installed'
_T='deviceId'
_S='NotificationType'
_R='deviceTemperature'
_Q='enabled'
_P='disabled'
_O='powerId'
_N='error'
_M='no-error'
_L='on'
_K='off'
_J='portId'
_I='alarm'
_H='no-alarm'
_G='optional'
_F='DisplayString'
_E='MICROSENS-CWDM8-MIB'
_D='unknown'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_S,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_S,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
_Microsens_ObjectIdentity=ObjectIdentity
microsens=_Microsens_ObjectIdentity((1,3,6,1,4,1,3181))
_Cwdm_ObjectIdentity=ObjectIdentity
cwdm=_Cwdm_ObjectIdentity((1,3,6,1,4,1,3181,6))
_EightChannelCwdm_ObjectIdentity=ObjectIdentity
eightChannelCwdm=_EightChannelCwdm_ObjectIdentity((1,3,6,1,4,1,3181,6,4))
_DeviceTable_Object=MibTable
deviceTable=_DeviceTable_Object((1,3,6,1,4,1,3181,6,4,1))
if mibBuilder.loadTexts:deviceTable.setStatus(_A)
_DeviceTableEntry_Object=MibTableRow
deviceTableEntry=_DeviceTableEntry_Object((1,3,6,1,4,1,3181,6,4,1,1))
deviceTableEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:deviceTableEntry.setStatus(_A)
_DeviceId_Type=Integer32
_DeviceId_Object=MibTableColumn
deviceId=_DeviceId_Object((1,3,6,1,4,1,3181,6,4,1,1,1),_DeviceId_Type())
deviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceId.setStatus(_A)
class _DeviceArtNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_DeviceArtNo_Type.__name__=_F
_DeviceArtNo_Object=MibTableColumn
deviceArtNo=_DeviceArtNo_Object((1,3,6,1,4,1,3181,6,4,1,1,2),_DeviceArtNo_Type())
deviceArtNo.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceArtNo.setStatus(_A)
class _DeviceSerNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_DeviceSerNo_Type.__name__=_F
_DeviceSerNo_Object=MibTableColumn
deviceSerNo=_DeviceSerNo_Object((1,3,6,1,4,1,3181,6,4,1,1,3),_DeviceSerNo_Type())
deviceSerNo.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceSerNo.setStatus(_A)
class _DeviceDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DeviceDesc_Type.__name__=_F
_DeviceDesc_Object=MibTableColumn
deviceDesc=_DeviceDesc_Object((1,3,6,1,4,1,3181,6,4,1,1,4),_DeviceDesc_Type())
deviceDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceDesc.setStatus(_A)
class _DeviceTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_DeviceTemperature_Type.__name__=_C
_DeviceTemperature_Object=MibTableColumn
deviceTemperature=_DeviceTemperature_Object((1,3,6,1,4,1,3181,6,4,1,1,5),_DeviceTemperature_Type())
deviceTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceTemperature.setStatus(_A)
class _DeviceTempAlarmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_DeviceTempAlarmThreshold_Type.__name__=_C
_DeviceTempAlarmThreshold_Object=MibTableColumn
deviceTempAlarmThreshold=_DeviceTempAlarmThreshold_Object((1,3,6,1,4,1,3181,6,4,1,1,6),_DeviceTempAlarmThreshold_Type())
deviceTempAlarmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceTempAlarmThreshold.setStatus(_A)
class _DeviceTempAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,0,1)));namedValues=NamedValues(*((_D,-255),(_H,0),(_I,1)))
_DeviceTempAlarm_Type.__name__=_C
_DeviceTempAlarm_Object=MibTableColumn
deviceTempAlarm=_DeviceTempAlarm_Object((1,3,6,1,4,1,3181,6,4,1,1,7),_DeviceTempAlarm_Type())
deviceTempAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceTempAlarm.setStatus(_A)
class _DeviceTempShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,0,1)));namedValues=NamedValues(*((_D,-255),(_H,0),(_I,1)))
_DeviceTempShutdown_Type.__name__=_C
_DeviceTempShutdown_Object=MibTableColumn
deviceTempShutdown=_DeviceTempShutdown_Object((1,3,6,1,4,1,3181,6,4,1,1,8),_DeviceTempShutdown_Type())
deviceTempShutdown.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceTempShutdown.setStatus(_A)
class _DeviceTrPowerFailureAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,0,1,2,3)));namedValues=NamedValues(*((_D,-255),(_H,0),('alarm-channel-1-4',1),('alarm-channel-5-8',2),('alarm-channel-1-8',3)))
_DeviceTrPowerFailureAlarm_Type.__name__=_C
_DeviceTrPowerFailureAlarm_Object=MibTableColumn
deviceTrPowerFailureAlarm=_DeviceTrPowerFailureAlarm_Object((1,3,6,1,4,1,3181,6,4,1,1,9),_DeviceTrPowerFailureAlarm_Type())
deviceTrPowerFailureAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceTrPowerFailureAlarm.setStatus(_A)
class _DeviceMinorAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,0,1)));namedValues=NamedValues(*((_D,-255),(_H,0),(_I,1)))
_DeviceMinorAlarm_Type.__name__=_C
_DeviceMinorAlarm_Object=MibTableColumn
deviceMinorAlarm=_DeviceMinorAlarm_Object((1,3,6,1,4,1,3181,6,4,1,1,10),_DeviceMinorAlarm_Type())
deviceMinorAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceMinorAlarm.setStatus(_A)
class _DeviceMajorAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,0,1)));namedValues=NamedValues(*((_D,-255),(_H,0),(_I,1)))
_DeviceMajorAlarm_Type.__name__=_C
_DeviceMajorAlarm_Object=MibTableColumn
deviceMajorAlarm=_DeviceMajorAlarm_Object((1,3,6,1,4,1,3181,6,4,1,1,11),_DeviceMajorAlarm_Type())
deviceMajorAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceMajorAlarm.setStatus(_A)
_PortTable_Object=MibTable
portTable=_PortTable_Object((1,3,6,1,4,1,3181,6,4,2))
if mibBuilder.loadTexts:portTable.setStatus(_A)
_PortTableEntry_Object=MibTableRow
portTableEntry=_PortTableEntry_Object((1,3,6,1,4,1,3181,6,4,2,1))
portTableEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:portTableEntry.setStatus(_A)
_PortId_Type=Integer32
_PortId_Object=MibTableColumn
portId=_PortId_Object((1,3,6,1,4,1,3181,6,4,2,1,1),_PortId_Type())
portId.setMaxAccess(_B)
if mibBuilder.loadTexts:portId.setStatus(_A)
class _PortChannelEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,0,1)));namedValues=NamedValues(*((_D,-255),(_P,0),(_Q,1)))
_PortChannelEnabled_Type.__name__=_C
_PortChannelEnabled_Object=MibTableColumn
portChannelEnabled=_PortChannelEnabled_Object((1,3,6,1,4,1,3181,6,4,2,1,2),_PortChannelEnabled_Type())
portChannelEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:portChannelEnabled.setStatus(_A)
class _PortLinkThroughLocalLine_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,0,1)));namedValues=NamedValues(*((_D,-255),(_P,0),(_Q,1)))
_PortLinkThroughLocalLine_Type.__name__=_C
_PortLinkThroughLocalLine_Object=MibTableColumn
portLinkThroughLocalLine=_PortLinkThroughLocalLine_Object((1,3,6,1,4,1,3181,6,4,2,1,3),_PortLinkThroughLocalLine_Type())
portLinkThroughLocalLine.setMaxAccess(_B)
if mibBuilder.loadTexts:portLinkThroughLocalLine.setStatus(_A)
class _PortLinkThroughLineLocal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,0,1)));namedValues=NamedValues(*((_D,-255),(_P,0),(_Q,1)))
_PortLinkThroughLineLocal_Type.__name__=_C
_PortLinkThroughLineLocal_Object=MibTableColumn
portLinkThroughLineLocal=_PortLinkThroughLineLocal_Object((1,3,6,1,4,1,3181,6,4,2,1,4),_PortLinkThroughLineLocal_Type())
portLinkThroughLineLocal.setMaxAccess(_B)
if mibBuilder.loadTexts:portLinkThroughLineLocal.setStatus(_A)
class _PortLocalModuleInstalled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,0,1)));namedValues=NamedValues(*((_D,-255),(_U,0),(_V,1)))
_PortLocalModuleInstalled_Type.__name__=_C
_PortLocalModuleInstalled_Object=MibTableColumn
portLocalModuleInstalled=_PortLocalModuleInstalled_Object((1,3,6,1,4,1,3181,6,4,2,1,5),_PortLocalModuleInstalled_Type())
portLocalModuleInstalled.setMaxAccess(_B)
if mibBuilder.loadTexts:portLocalModuleInstalled.setStatus(_A)
class _PortLineModuleInstalled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,0,1)));namedValues=NamedValues(*((_D,-255),(_U,0),(_V,1)))
_PortLineModuleInstalled_Type.__name__=_C
_PortLineModuleInstalled_Object=MibTableColumn
portLineModuleInstalled=_PortLineModuleInstalled_Object((1,3,6,1,4,1,3181,6,4,2,1,6),_PortLineModuleInstalled_Type())
portLineModuleInstalled.setMaxAccess(_B)
if mibBuilder.loadTexts:portLineModuleInstalled.setStatus(_A)
class _PortLocalLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,0,1)));namedValues=NamedValues(*((_D,-255),(_K,0),(_L,1)))
_PortLocalLink_Type.__name__=_C
_PortLocalLink_Object=MibTableColumn
portLocalLink=_PortLocalLink_Object((1,3,6,1,4,1,3181,6,4,2,1,7),_PortLocalLink_Type())
portLocalLink.setMaxAccess(_B)
if mibBuilder.loadTexts:portLocalLink.setStatus(_A)
class _PortLineLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,0,1)));namedValues=NamedValues(*((_D,-255),(_K,0),(_L,1)))
_PortLineLink_Type.__name__=_C
_PortLineLink_Object=MibTableColumn
portLineLink=_PortLineLink_Object((1,3,6,1,4,1,3181,6,4,2,1,8),_PortLineLink_Type())
portLineLink.setMaxAccess(_B)
if mibBuilder.loadTexts:portLineLink.setStatus(_A)
class _PortLocalTxFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,0,1)));namedValues=NamedValues(*((_D,-255),(_M,0),(_N,1)))
_PortLocalTxFault_Type.__name__=_C
_PortLocalTxFault_Object=MibTableColumn
portLocalTxFault=_PortLocalTxFault_Object((1,3,6,1,4,1,3181,6,4,2,1,9),_PortLocalTxFault_Type())
portLocalTxFault.setMaxAccess(_B)
if mibBuilder.loadTexts:portLocalTxFault.setStatus(_A)
class _PortLineTxFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,0,1)));namedValues=NamedValues(*((_D,-255),(_M,0),(_N,1)))
_PortLineTxFault_Type.__name__=_C
_PortLineTxFault_Object=MibTableColumn
portLineTxFault=_PortLineTxFault_Object((1,3,6,1,4,1,3181,6,4,2,1,10),_PortLineTxFault_Type())
portLineTxFault.setMaxAccess(_B)
if mibBuilder.loadTexts:portLineTxFault.setStatus(_A)
class _PortLocalPowerFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,0,1)));namedValues=NamedValues(*((_D,-255),(_M,0),(_N,1)))
_PortLocalPowerFault_Type.__name__=_C
_PortLocalPowerFault_Object=MibTableColumn
portLocalPowerFault=_PortLocalPowerFault_Object((1,3,6,1,4,1,3181,6,4,2,1,11),_PortLocalPowerFault_Type())
portLocalPowerFault.setMaxAccess(_B)
if mibBuilder.loadTexts:portLocalPowerFault.setStatus(_A)
class _PortLinePowerFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,0,1)));namedValues=NamedValues(*((_D,-255),(_M,0),(_N,1)))
_PortLinePowerFault_Type.__name__=_C
_PortLinePowerFault_Object=MibTableColumn
portLinePowerFault=_PortLinePowerFault_Object((1,3,6,1,4,1,3181,6,4,2,1,12),_PortLinePowerFault_Type())
portLinePowerFault.setMaxAccess(_B)
if mibBuilder.loadTexts:portLinePowerFault.setStatus(_A)
class _PortRateSelect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,0,1)));namedValues=NamedValues(*((_D,-255),('reduced',0),('full',1)))
_PortRateSelect_Type.__name__=_C
_PortRateSelect_Object=MibTableColumn
portRateSelect=_PortRateSelect_Object((1,3,6,1,4,1,3181,6,4,2,1,13),_PortRateSelect_Type())
portRateSelect.setMaxAccess(_B)
if mibBuilder.loadTexts:portRateSelect.setStatus(_A)
_LocalModuleTable_Object=MibTable
localModuleTable=_LocalModuleTable_Object((1,3,6,1,4,1,3181,6,4,3))
if mibBuilder.loadTexts:localModuleTable.setStatus(_A)
_LocalModuleTableEntry_Object=MibTableRow
localModuleTableEntry=_LocalModuleTableEntry_Object((1,3,6,1,4,1,3181,6,4,3,1))
localModuleTableEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:localModuleTableEntry.setStatus(_A)
_LocalModuleId_Type=Integer32
_LocalModuleId_Object=MibTableColumn
localModuleId=_LocalModuleId_Object((1,3,6,1,4,1,3181,6,4,3,1,1),_LocalModuleId_Type())
localModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:localModuleId.setStatus(_A)
class _LocalModuleConnector_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,32,33)));namedValues=NamedValues(*((_D,0),('sc',1),(_X,2),(_Y,3),(_Z,4),(_a,5),(_b,6),('lc',7),('mt-rj',8),('mu',9),('sg',10),(_c,11),(_d,32),(_e,33)))
_LocalModuleConnector_Type.__name__=_C
_LocalModuleConnector_Object=MibTableColumn
localModuleConnector=_LocalModuleConnector_Object((1,3,6,1,4,1,3181,6,4,3,1,2),_LocalModuleConnector_Type())
localModuleConnector.setMaxAccess(_B)
if mibBuilder.loadTexts:localModuleConnector.setStatus(_A)
class _LocalModuleTrCodeSonet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,16,32,64,128,256,512)));namedValues=NamedValues(*((_D,0),(_f,1),(_g,2),(_h,4),(_i,16),(_j,32),(_k,64),(_l,128),(_m,256),(_n,512)))
_LocalModuleTrCodeSonet_Type.__name__=_C
_LocalModuleTrCodeSonet_Object=MibTableColumn
localModuleTrCodeSonet=_LocalModuleTrCodeSonet_Object((1,3,6,1,4,1,3181,6,4,3,1,3),_LocalModuleTrCodeSonet_Type())
localModuleTrCodeSonet.setMaxAccess(_B)
if mibBuilder.loadTexts:localModuleTrCodeSonet.setStatus(_A)
class _LocalModuleTrCodeGigabit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8)));namedValues=NamedValues(*((_D,0),('base-1000-sx',1),('base-1000-lx',2),('base-1000-cx',4),('base-1000-t',8)))
_LocalModuleTrCodeGigabit_Type.__name__=_C
_LocalModuleTrCodeGigabit_Object=MibTableColumn
localModuleTrCodeGigabit=_LocalModuleTrCodeGigabit_Object((1,3,6,1,4,1,3181,6,4,3,1,4),_LocalModuleTrCodeGigabit_Type())
localModuleTrCodeGigabit.setMaxAccess(_B)
if mibBuilder.loadTexts:localModuleTrCodeGigabit.setStatus(_A)
class _LocalModuleTrCodeFbLinkLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4)));namedValues=NamedValues(*((_D,0),(_o,1),(_p,2),(_q,4)))
_LocalModuleTrCodeFbLinkLength_Type.__name__=_C
_LocalModuleTrCodeFbLinkLength_Object=MibTableColumn
localModuleTrCodeFbLinkLength=_LocalModuleTrCodeFbLinkLength_Object((1,3,6,1,4,1,3181,6,4,3,1,5),_LocalModuleTrCodeFbLinkLength_Type())
localModuleTrCodeFbLinkLength.setMaxAccess(_B)
if mibBuilder.loadTexts:localModuleTrCodeFbLinkLength.setStatus(_A)
class _LocalModuleTrCodeFbTrTech_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8,16,32)));namedValues=NamedValues(*((_D,0),(_r,1),(_s,2),(_t,4),(_u,8),(_v,16),(_w,32)))
_LocalModuleTrCodeFbTrTech_Type.__name__=_C
_LocalModuleTrCodeFbTrTech_Object=MibTableColumn
localModuleTrCodeFbTrTech=_LocalModuleTrCodeFbTrTech_Object((1,3,6,1,4,1,3181,6,4,3,1,6),_LocalModuleTrCodeFbTrTech_Type())
localModuleTrCodeFbTrTech.setMaxAccess(_B)
if mibBuilder.loadTexts:localModuleTrCodeFbTrTech.setStatus(_A)
class _LocalModuleTrCodeFbTrMedia_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,4,8,16,32,64,128)));namedValues=NamedValues(*((_D,0),(_x,1),(_y,4),(_z,8),(_A0,16),(_A1,32),(_A2,64),(_A3,128)))
_LocalModuleTrCodeFbTrMedia_Type.__name__=_C
_LocalModuleTrCodeFbTrMedia_Object=MibTableColumn
localModuleTrCodeFbTrMedia=_LocalModuleTrCodeFbTrMedia_Object((1,3,6,1,4,1,3181,6,4,3,1,7),_LocalModuleTrCodeFbTrMedia_Type())
localModuleTrCodeFbTrMedia.setMaxAccess(_B)
if mibBuilder.loadTexts:localModuleTrCodeFbTrMedia.setStatus(_A)
class _LocalModuleTrCodeFbSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,4,16)));namedValues=NamedValues(*((_D,0),(_A4,1),(_A5,4),(_A6,16)))
_LocalModuleTrCodeFbSpeed_Type.__name__=_C
_LocalModuleTrCodeFbSpeed_Object=MibTableColumn
localModuleTrCodeFbSpeed=_LocalModuleTrCodeFbSpeed_Object((1,3,6,1,4,1,3181,6,4,3,1,8),_LocalModuleTrCodeFbSpeed_Type())
localModuleTrCodeFbSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:localModuleTrCodeFbSpeed.setStatus(_A)
class _LocalModuleBrNominal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_LocalModuleBrNominal_Type.__name__=_C
_LocalModuleBrNominal_Object=MibTableColumn
localModuleBrNominal=_LocalModuleBrNominal_Object((1,3,6,1,4,1,3181,6,4,3,1,9),_LocalModuleBrNominal_Type())
localModuleBrNominal.setMaxAccess(_B)
if mibBuilder.loadTexts:localModuleBrNominal.setStatus(_A)
class _LocalModuleLength9km_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_LocalModuleLength9km_Type.__name__=_C
_LocalModuleLength9km_Object=MibTableColumn
localModuleLength9km=_LocalModuleLength9km_Object((1,3,6,1,4,1,3181,6,4,3,1,10),_LocalModuleLength9km_Type())
localModuleLength9km.setMaxAccess(_B)
if mibBuilder.loadTexts:localModuleLength9km.setStatus(_A)
class _LocalModuleLength9m_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_LocalModuleLength9m_Type.__name__=_C
_LocalModuleLength9m_Object=MibTableColumn
localModuleLength9m=_LocalModuleLength9m_Object((1,3,6,1,4,1,3181,6,4,3,1,11),_LocalModuleLength9m_Type())
localModuleLength9m.setMaxAccess(_B)
if mibBuilder.loadTexts:localModuleLength9m.setStatus(_A)
class _LocalModuleLength50_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_LocalModuleLength50_Type.__name__=_C
_LocalModuleLength50_Object=MibTableColumn
localModuleLength50=_LocalModuleLength50_Object((1,3,6,1,4,1,3181,6,4,3,1,12),_LocalModuleLength50_Type())
localModuleLength50.setMaxAccess(_B)
if mibBuilder.loadTexts:localModuleLength50.setStatus(_A)
class _LocalModuleLength62_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_LocalModuleLength62_Type.__name__=_C
_LocalModuleLength62_Object=MibTableColumn
localModuleLength62=_LocalModuleLength62_Object((1,3,6,1,4,1,3181,6,4,3,1,13),_LocalModuleLength62_Type())
localModuleLength62.setMaxAccess(_B)
if mibBuilder.loadTexts:localModuleLength62.setStatus(_A)
class _LocalModuleLengthCopper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_LocalModuleLengthCopper_Type.__name__=_C
_LocalModuleLengthCopper_Object=MibTableColumn
localModuleLengthCopper=_LocalModuleLengthCopper_Object((1,3,6,1,4,1,3181,6,4,3,1,14),_LocalModuleLengthCopper_Type())
localModuleLengthCopper.setMaxAccess(_B)
if mibBuilder.loadTexts:localModuleLengthCopper.setStatus(_A)
class _LocalModuleVendorSN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_LocalModuleVendorSN_Type.__name__=_F
_LocalModuleVendorSN_Object=MibTableColumn
localModuleVendorSN=_LocalModuleVendorSN_Object((1,3,6,1,4,1,3181,6,4,3,1,15),_LocalModuleVendorSN_Type())
localModuleVendorSN.setMaxAccess(_B)
if mibBuilder.loadTexts:localModuleVendorSN.setStatus(_A)
class _LocalModuleDateCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_LocalModuleDateCode_Type.__name__=_F
_LocalModuleDateCode_Object=MibTableColumn
localModuleDateCode=_LocalModuleDateCode_Object((1,3,6,1,4,1,3181,6,4,3,1,16),_LocalModuleDateCode_Type())
localModuleDateCode.setMaxAccess(_B)
if mibBuilder.loadTexts:localModuleDateCode.setStatus(_A)
class _LocalModuleLaserCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_LocalModuleLaserCurrent_Type.__name__=_C
_LocalModuleLaserCurrent_Object=MibTableColumn
localModuleLaserCurrent=_LocalModuleLaserCurrent_Object((1,3,6,1,4,1,3181,6,4,3,1,17),_LocalModuleLaserCurrent_Type())
localModuleLaserCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:localModuleLaserCurrent.setStatus(_G)
class _LocalModuleTransmittedPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_LocalModuleTransmittedPower_Type.__name__=_C
_LocalModuleTransmittedPower_Object=MibTableColumn
localModuleTransmittedPower=_LocalModuleTransmittedPower_Object((1,3,6,1,4,1,3181,6,4,3,1,18),_LocalModuleTransmittedPower_Type())
localModuleTransmittedPower.setMaxAccess(_B)
if mibBuilder.loadTexts:localModuleTransmittedPower.setStatus(_G)
class _LocalModuleReceivedPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_LocalModuleReceivedPower_Type.__name__=_C
_LocalModuleReceivedPower_Object=MibTableColumn
localModuleReceivedPower=_LocalModuleReceivedPower_Object((1,3,6,1,4,1,3181,6,4,3,1,19),_LocalModuleReceivedPower_Type())
localModuleReceivedPower.setMaxAccess(_B)
if mibBuilder.loadTexts:localModuleReceivedPower.setStatus(_G)
class _LocalModuleLaserTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_LocalModuleLaserTemperature_Type.__name__=_C
_LocalModuleLaserTemperature_Object=MibTableColumn
localModuleLaserTemperature=_LocalModuleLaserTemperature_Object((1,3,6,1,4,1,3181,6,4,3,1,20),_LocalModuleLaserTemperature_Type())
localModuleLaserTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:localModuleLaserTemperature.setStatus(_G)
class _LocalModuleVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_LocalModuleVoltage_Type.__name__=_C
_LocalModuleVoltage_Object=MibTableColumn
localModuleVoltage=_LocalModuleVoltage_Object((1,3,6,1,4,1,3181,6,4,3,1,21),_LocalModuleVoltage_Type())
localModuleVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:localModuleVoltage.setStatus(_G)
_LineModuleTable_Object=MibTable
lineModuleTable=_LineModuleTable_Object((1,3,6,1,4,1,3181,6,4,4))
if mibBuilder.loadTexts:lineModuleTable.setStatus(_A)
_LineModuleTableEntry_Object=MibTableRow
lineModuleTableEntry=_LineModuleTableEntry_Object((1,3,6,1,4,1,3181,6,4,4,1))
lineModuleTableEntry.setIndexNames((0,_E,_A7))
if mibBuilder.loadTexts:lineModuleTableEntry.setStatus(_A)
_LineModuleId_Type=Integer32
_LineModuleId_Object=MibTableColumn
lineModuleId=_LineModuleId_Object((1,3,6,1,4,1,3181,6,4,4,1,1),_LineModuleId_Type())
lineModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:lineModuleId.setStatus(_A)
class _LineModuleConnector_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,32,33)));namedValues=NamedValues(*((_D,0),('sc',1),(_X,2),(_Y,3),(_Z,4),(_a,5),(_b,6),('lc',7),('mt-rj',8),('mu',9),('sg',10),(_c,11),(_d,32),(_e,33)))
_LineModuleConnector_Type.__name__=_C
_LineModuleConnector_Object=MibTableColumn
lineModuleConnector=_LineModuleConnector_Object((1,3,6,1,4,1,3181,6,4,4,1,2),_LineModuleConnector_Type())
lineModuleConnector.setMaxAccess(_B)
if mibBuilder.loadTexts:lineModuleConnector.setStatus(_A)
class _LineModuleTrCodeSonet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,16,32,64,128,256,512)));namedValues=NamedValues(*((_D,0),(_f,1),(_g,2),(_h,4),(_i,16),(_j,32),(_k,64),(_l,128),(_m,256),(_n,512)))
_LineModuleTrCodeSonet_Type.__name__=_C
_LineModuleTrCodeSonet_Object=MibTableColumn
lineModuleTrCodeSonet=_LineModuleTrCodeSonet_Object((1,3,6,1,4,1,3181,6,4,4,1,3),_LineModuleTrCodeSonet_Type())
lineModuleTrCodeSonet.setMaxAccess(_B)
if mibBuilder.loadTexts:lineModuleTrCodeSonet.setStatus(_A)
class _LineModuleTrCodeGigabit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8)));namedValues=NamedValues(*((_D,0),('base-1000-SX',1),('base-1000-LX',2),('base-1000-CX',4),('base-1000-T',8)))
_LineModuleTrCodeGigabit_Type.__name__=_C
_LineModuleTrCodeGigabit_Object=MibTableColumn
lineModuleTrCodeGigabit=_LineModuleTrCodeGigabit_Object((1,3,6,1,4,1,3181,6,4,4,1,4),_LineModuleTrCodeGigabit_Type())
lineModuleTrCodeGigabit.setMaxAccess(_B)
if mibBuilder.loadTexts:lineModuleTrCodeGigabit.setStatus(_A)
class _LineModuleTrCodeFbLinkLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4)));namedValues=NamedValues(*((_D,0),(_o,1),(_p,2),(_q,4)))
_LineModuleTrCodeFbLinkLength_Type.__name__=_C
_LineModuleTrCodeFbLinkLength_Object=MibTableColumn
lineModuleTrCodeFbLinkLength=_LineModuleTrCodeFbLinkLength_Object((1,3,6,1,4,1,3181,6,4,4,1,5),_LineModuleTrCodeFbLinkLength_Type())
lineModuleTrCodeFbLinkLength.setMaxAccess(_B)
if mibBuilder.loadTexts:lineModuleTrCodeFbLinkLength.setStatus(_A)
class _LineModuleTrCodeFbTrTech_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8,16,32)));namedValues=NamedValues(*((_D,0),(_r,1),(_s,2),(_t,4),(_u,8),(_v,16),(_w,32)))
_LineModuleTrCodeFbTrTech_Type.__name__=_C
_LineModuleTrCodeFbTrTech_Object=MibTableColumn
lineModuleTrCodeFbTrTech=_LineModuleTrCodeFbTrTech_Object((1,3,6,1,4,1,3181,6,4,4,1,6),_LineModuleTrCodeFbTrTech_Type())
lineModuleTrCodeFbTrTech.setMaxAccess(_B)
if mibBuilder.loadTexts:lineModuleTrCodeFbTrTech.setStatus(_A)
class _LineModuleTrCodeFbTrMedia_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,4,8,16,32,64,128)));namedValues=NamedValues(*((_D,0),(_x,1),(_y,4),(_z,8),(_A0,16),(_A1,32),(_A2,64),(_A3,128)))
_LineModuleTrCodeFbTrMedia_Type.__name__=_C
_LineModuleTrCodeFbTrMedia_Object=MibTableColumn
lineModuleTrCodeFbTrMedia=_LineModuleTrCodeFbTrMedia_Object((1,3,6,1,4,1,3181,6,4,4,1,7),_LineModuleTrCodeFbTrMedia_Type())
lineModuleTrCodeFbTrMedia.setMaxAccess(_B)
if mibBuilder.loadTexts:lineModuleTrCodeFbTrMedia.setStatus(_A)
class _LineModuleTrCodeFbSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,4,16)));namedValues=NamedValues(*((_D,0),(_A4,1),(_A5,4),(_A6,16)))
_LineModuleTrCodeFbSpeed_Type.__name__=_C
_LineModuleTrCodeFbSpeed_Object=MibTableColumn
lineModuleTrCodeFbSpeed=_LineModuleTrCodeFbSpeed_Object((1,3,6,1,4,1,3181,6,4,4,1,8),_LineModuleTrCodeFbSpeed_Type())
lineModuleTrCodeFbSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:lineModuleTrCodeFbSpeed.setStatus(_A)
class _LineModuleBrNominal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_LineModuleBrNominal_Type.__name__=_C
_LineModuleBrNominal_Object=MibTableColumn
lineModuleBrNominal=_LineModuleBrNominal_Object((1,3,6,1,4,1,3181,6,4,4,1,9),_LineModuleBrNominal_Type())
lineModuleBrNominal.setMaxAccess(_B)
if mibBuilder.loadTexts:lineModuleBrNominal.setStatus(_A)
class _LineModuleLength9km_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_LineModuleLength9km_Type.__name__=_C
_LineModuleLength9km_Object=MibTableColumn
lineModuleLength9km=_LineModuleLength9km_Object((1,3,6,1,4,1,3181,6,4,4,1,10),_LineModuleLength9km_Type())
lineModuleLength9km.setMaxAccess(_B)
if mibBuilder.loadTexts:lineModuleLength9km.setStatus(_A)
class _LineModuleLength9m_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_LineModuleLength9m_Type.__name__=_C
_LineModuleLength9m_Object=MibTableColumn
lineModuleLength9m=_LineModuleLength9m_Object((1,3,6,1,4,1,3181,6,4,4,1,11),_LineModuleLength9m_Type())
lineModuleLength9m.setMaxAccess(_B)
if mibBuilder.loadTexts:lineModuleLength9m.setStatus(_A)
class _LineModuleLength50_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_LineModuleLength50_Type.__name__=_C
_LineModuleLength50_Object=MibTableColumn
lineModuleLength50=_LineModuleLength50_Object((1,3,6,1,4,1,3181,6,4,4,1,12),_LineModuleLength50_Type())
lineModuleLength50.setMaxAccess(_B)
if mibBuilder.loadTexts:lineModuleLength50.setStatus(_A)
class _LineModuleLength62_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_LineModuleLength62_Type.__name__=_C
_LineModuleLength62_Object=MibTableColumn
lineModuleLength62=_LineModuleLength62_Object((1,3,6,1,4,1,3181,6,4,4,1,13),_LineModuleLength62_Type())
lineModuleLength62.setMaxAccess(_B)
if mibBuilder.loadTexts:lineModuleLength62.setStatus(_A)
class _LineModuleLengthCopper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_LineModuleLengthCopper_Type.__name__=_C
_LineModuleLengthCopper_Object=MibTableColumn
lineModuleLengthCopper=_LineModuleLengthCopper_Object((1,3,6,1,4,1,3181,6,4,4,1,14),_LineModuleLengthCopper_Type())
lineModuleLengthCopper.setMaxAccess(_B)
if mibBuilder.loadTexts:lineModuleLengthCopper.setStatus(_A)
class _LineModuleVendorSN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_LineModuleVendorSN_Type.__name__=_F
_LineModuleVendorSN_Object=MibTableColumn
lineModuleVendorSN=_LineModuleVendorSN_Object((1,3,6,1,4,1,3181,6,4,4,1,15),_LineModuleVendorSN_Type())
lineModuleVendorSN.setMaxAccess(_B)
if mibBuilder.loadTexts:lineModuleVendorSN.setStatus(_A)
class _LineModuleDateCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_LineModuleDateCode_Type.__name__=_F
_LineModuleDateCode_Object=MibTableColumn
lineModuleDateCode=_LineModuleDateCode_Object((1,3,6,1,4,1,3181,6,4,4,1,16),_LineModuleDateCode_Type())
lineModuleDateCode.setMaxAccess(_B)
if mibBuilder.loadTexts:lineModuleDateCode.setStatus(_A)
class _LineModuleLaserCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_LineModuleLaserCurrent_Type.__name__=_C
_LineModuleLaserCurrent_Object=MibTableColumn
lineModuleLaserCurrent=_LineModuleLaserCurrent_Object((1,3,6,1,4,1,3181,6,4,4,1,17),_LineModuleLaserCurrent_Type())
lineModuleLaserCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:lineModuleLaserCurrent.setStatus(_A)
class _LineModuleTransmittedPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_LineModuleTransmittedPower_Type.__name__=_C
_LineModuleTransmittedPower_Object=MibTableColumn
lineModuleTransmittedPower=_LineModuleTransmittedPower_Object((1,3,6,1,4,1,3181,6,4,4,1,18),_LineModuleTransmittedPower_Type())
lineModuleTransmittedPower.setMaxAccess(_B)
if mibBuilder.loadTexts:lineModuleTransmittedPower.setStatus(_A)
class _LineModuleReceivedPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_LineModuleReceivedPower_Type.__name__=_C
_LineModuleReceivedPower_Object=MibTableColumn
lineModuleReceivedPower=_LineModuleReceivedPower_Object((1,3,6,1,4,1,3181,6,4,4,1,19),_LineModuleReceivedPower_Type())
lineModuleReceivedPower.setMaxAccess(_B)
if mibBuilder.loadTexts:lineModuleReceivedPower.setStatus(_A)
class _LineModuleLaserTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_LineModuleLaserTemperature_Type.__name__=_C
_LineModuleLaserTemperature_Object=MibTableColumn
lineModuleLaserTemperature=_LineModuleLaserTemperature_Object((1,3,6,1,4,1,3181,6,4,4,1,20),_LineModuleLaserTemperature_Type())
lineModuleLaserTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:lineModuleLaserTemperature.setStatus(_A)
class _LineModuleVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_LineModuleVoltage_Type.__name__=_C
_LineModuleVoltage_Object=MibTableColumn
lineModuleVoltage=_LineModuleVoltage_Object((1,3,6,1,4,1,3181,6,4,4,1,21),_LineModuleVoltage_Type())
lineModuleVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:lineModuleVoltage.setStatus(_A)
_PowerTable_Object=MibTable
powerTable=_PowerTable_Object((1,3,6,1,4,1,3181,6,4,5))
if mibBuilder.loadTexts:powerTable.setStatus(_A)
_PowerTableEntry_Object=MibTableRow
powerTableEntry=_PowerTableEntry_Object((1,3,6,1,4,1,3181,6,4,5,1))
powerTableEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:powerTableEntry.setStatus(_A)
_PowerId_Type=Integer32
_PowerId_Object=MibTableColumn
powerId=_PowerId_Object((1,3,6,1,4,1,3181,6,4,5,1,1),_PowerId_Type())
powerId.setMaxAccess(_B)
if mibBuilder.loadTexts:powerId.setStatus(_A)
class _PowerArtNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PowerArtNo_Type.__name__=_F
_PowerArtNo_Object=MibTableColumn
powerArtNo=_PowerArtNo_Object((1,3,6,1,4,1,3181,6,4,5,1,2),_PowerArtNo_Type())
powerArtNo.setMaxAccess(_B)
if mibBuilder.loadTexts:powerArtNo.setStatus(_A)
class _PowerSerNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PowerSerNo_Type.__name__=_F
_PowerSerNo_Object=MibTableColumn
powerSerNo=_PowerSerNo_Object((1,3,6,1,4,1,3181,6,4,5,1,3),_PowerSerNo_Type())
powerSerNo.setMaxAccess(_B)
if mibBuilder.loadTexts:powerSerNo.setStatus(_A)
class _PowerDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PowerDesc_Type.__name__=_F
_PowerDesc_Object=MibTableColumn
powerDesc=_PowerDesc_Object((1,3,6,1,4,1,3181,6,4,5,1,4),_PowerDesc_Type())
powerDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:powerDesc.setStatus(_A)
class _PowerTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_PowerTemperature_Type.__name__=_C
_PowerTemperature_Object=MibTableColumn
powerTemperature=_PowerTemperature_Object((1,3,6,1,4,1,3181,6,4,5,1,5),_PowerTemperature_Type())
powerTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:powerTemperature.setStatus(_A)
class _PowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,0,1)));namedValues=NamedValues(*((_D,-255),(_A8,0),('active',1)))
_PowerStatus_Type.__name__=_C
_PowerStatus_Object=MibTableColumn
powerStatus=_PowerStatus_Object((1,3,6,1,4,1,3181,6,4,5,1,6),_PowerStatus_Type())
powerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:powerStatus.setStatus(_A)
class _PowerSuppliedPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_PowerSuppliedPower_Type.__name__=_C
_PowerSuppliedPower_Object=MibTableColumn
powerSuppliedPower=_PowerSuppliedPower_Object((1,3,6,1,4,1,3181,6,4,5,1,7),_PowerSuppliedPower_Type())
powerSuppliedPower.setMaxAccess(_B)
if mibBuilder.loadTexts:powerSuppliedPower.setStatus(_A)
class _PowerLoad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_PowerLoad_Type.__name__=_C
_PowerLoad_Object=MibTableColumn
powerLoad=_PowerLoad_Object((1,3,6,1,4,1,3181,6,4,5,1,8),_PowerLoad_Type())
powerLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:powerLoad.setStatus(_A)
class _PowerFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,0,1)));namedValues=NamedValues(*((_D,-255),(_A8,0),('active',1)))
_PowerFanStatus_Type.__name__=_C
_PowerFanStatus_Object=MibTableColumn
powerFanStatus=_PowerFanStatus_Object((1,3,6,1,4,1,3181,6,4,5,1,9),_PowerFanStatus_Type())
powerFanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:powerFanStatus.setStatus(_A)
_LineIfTable_Object=MibTable
lineIfTable=_LineIfTable_Object((1,3,6,1,4,1,3181,6,4,6))
if mibBuilder.loadTexts:lineIfTable.setStatus(_A)
_LineIfTableEntry_Object=MibTableRow
lineIfTableEntry=_LineIfTableEntry_Object((1,3,6,1,4,1,3181,6,4,6,1))
lineIfTableEntry.setIndexNames((0,_E,'lineIfId'))
if mibBuilder.loadTexts:lineIfTableEntry.setStatus(_A)
_LineIfId_Type=Integer32
_LineIfId_Object=MibTableColumn
lineIfId=_LineIfId_Object((1,3,6,1,4,1,3181,6,4,6,1,1),_LineIfId_Type())
lineIfId.setMaxAccess(_B)
if mibBuilder.loadTexts:lineIfId.setStatus(_A)
class _LineIfArtNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_LineIfArtNo_Type.__name__=_F
_LineIfArtNo_Object=MibTableColumn
lineIfArtNo=_LineIfArtNo_Object((1,3,6,1,4,1,3181,6,4,6,1,2),_LineIfArtNo_Type())
lineIfArtNo.setMaxAccess(_B)
if mibBuilder.loadTexts:lineIfArtNo.setStatus(_A)
class _LineIfSerNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_LineIfSerNo_Type.__name__=_F
_LineIfSerNo_Object=MibTableColumn
lineIfSerNo=_LineIfSerNo_Object((1,3,6,1,4,1,3181,6,4,6,1,3),_LineIfSerNo_Type())
lineIfSerNo.setMaxAccess(_B)
if mibBuilder.loadTexts:lineIfSerNo.setStatus(_A)
class _LineIfWestLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,0,1)));namedValues=NamedValues(*((_D,-255),(_K,0),(_L,1)))
_LineIfWestLinkStatus_Type.__name__=_C
_LineIfWestLinkStatus_Object=MibTableColumn
lineIfWestLinkStatus=_LineIfWestLinkStatus_Object((1,3,6,1,4,1,3181,6,4,6,1,4),_LineIfWestLinkStatus_Type())
lineIfWestLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lineIfWestLinkStatus.setStatus(_G)
class _LineIfEastLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,0,1)));namedValues=NamedValues(*((_D,-255),(_K,0),(_L,1)))
_LineIfEastLinkStatus_Type.__name__=_C
_LineIfEastLinkStatus_Object=MibTableColumn
lineIfEastLinkStatus=_LineIfEastLinkStatus_Object((1,3,6,1,4,1,3181,6,4,6,1,5),_LineIfEastLinkStatus_Type())
lineIfEastLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lineIfEastLinkStatus.setStatus(_G)
class _LineIfWestChannelStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,0,1)));namedValues=NamedValues(*((_D,-255),(_A9,0),('in-use',1)))
_LineIfWestChannelStatus_Type.__name__=_C
_LineIfWestChannelStatus_Object=MibTableColumn
lineIfWestChannelStatus=_LineIfWestChannelStatus_Object((1,3,6,1,4,1,3181,6,4,6,1,6),_LineIfWestChannelStatus_Type())
lineIfWestChannelStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lineIfWestChannelStatus.setStatus(_G)
class _LineIfEastChannelStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-255,0,1)));namedValues=NamedValues(*((_D,-255),(_A9,0),('in-use',1)))
_LineIfEastChannelStatus_Type.__name__=_C
_LineIfEastChannelStatus_Object=MibTableColumn
lineIfEastChannelStatus=_LineIfEastChannelStatus_Object((1,3,6,1,4,1,3181,6,4,6,1,7),_LineIfEastChannelStatus_Type())
lineIfEastChannelStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lineIfEastChannelStatus.setStatus(_G)
class _LineIfWestLinkRcvPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_LineIfWestLinkRcvPower_Type.__name__=_C
_LineIfWestLinkRcvPower_Object=MibTableColumn
lineIfWestLinkRcvPower=_LineIfWestLinkRcvPower_Object((1,3,6,1,4,1,3181,6,4,6,1,8),_LineIfWestLinkRcvPower_Type())
lineIfWestLinkRcvPower.setMaxAccess(_B)
if mibBuilder.loadTexts:lineIfWestLinkRcvPower.setStatus(_G)
class _LineIfEastLinkRcvPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-255));namedValues=NamedValues((_D,-255))
_LineIfEastLinkRcvPower_Type.__name__=_C
_LineIfEastLinkRcvPower_Object=MibTableColumn
lineIfEastLinkRcvPower=_LineIfEastLinkRcvPower_Object((1,3,6,1,4,1,3181,6,4,6,1,9),_LineIfEastLinkRcvPower_Type())
lineIfEastLinkRcvPower.setMaxAccess(_B)
if mibBuilder.loadTexts:lineIfEastLinkRcvPower.setStatus(_G)
_PassiveTable_Object=MibTable
passiveTable=_PassiveTable_Object((1,3,6,1,4,1,3181,6,4,7))
if mibBuilder.loadTexts:passiveTable.setStatus(_A)
_PassiveTableEntry_Object=MibTableRow
passiveTableEntry=_PassiveTableEntry_Object((1,3,6,1,4,1,3181,6,4,7,1))
passiveTableEntry.setIndexNames((0,_E,_AA))
if mibBuilder.loadTexts:passiveTableEntry.setStatus(_A)
_PassiveId_Type=Integer32
_PassiveId_Object=MibTableColumn
passiveId=_PassiveId_Object((1,3,6,1,4,1,3181,6,4,7,1,1),_PassiveId_Type())
passiveId.setMaxAccess(_B)
if mibBuilder.loadTexts:passiveId.setStatus(_A)
class _PassiveArtNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PassiveArtNo_Type.__name__=_F
_PassiveArtNo_Object=MibTableColumn
passiveArtNo=_PassiveArtNo_Object((1,3,6,1,4,1,3181,6,4,7,1,2),_PassiveArtNo_Type())
passiveArtNo.setMaxAccess(_B)
if mibBuilder.loadTexts:passiveArtNo.setStatus(_A)
class _PassiveSerNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PassiveSerNo_Type.__name__=_F
_PassiveSerNo_Object=MibTableColumn
passiveSerNo=_PassiveSerNo_Object((1,3,6,1,4,1,3181,6,4,7,1,3),_PassiveSerNo_Type())
passiveSerNo.setMaxAccess(_B)
if mibBuilder.loadTexts:passiveSerNo.setStatus(_A)
_ChannelCount_Type=Integer32
_ChannelCount_Object=MibScalar
channelCount=_ChannelCount_Object((1,3,6,1,4,1,3181,6,4,100),_ChannelCount_Type())
channelCount.setMaxAccess(_B)
if mibBuilder.loadTexts:channelCount.setStatus(_A)
minorAlarmRelayTrap=NotificationType((1,3,6,1,4,1,3181,6,4,0,0))
minorAlarmRelayTrap.setObjects((_E,_AB))
if mibBuilder.loadTexts:minorAlarmRelayTrap.setStatus('')
majorAlarmRelayTrap=NotificationType((1,3,6,1,4,1,3181,6,4,0,1))
majorAlarmRelayTrap.setObjects((_E,_AC))
if mibBuilder.loadTexts:majorAlarmRelayTrap.setStatus('')
devicePowerSupplyTrap=NotificationType((1,3,6,1,4,1,3181,6,4,0,2))
devicePowerSupplyTrap.setObjects(*((_E,_O),(_E,_AD)))
if mibBuilder.loadTexts:devicePowerSupplyTrap.setStatus('')
deviceTemperatureAlarmTrap=NotificationType((1,3,6,1,4,1,3181,6,4,0,3))
deviceTemperatureAlarmTrap.setObjects(*((_E,_R),(_E,_AE)))
if mibBuilder.loadTexts:deviceTemperatureAlarmTrap.setStatus('')
deviceTemperatureShutdownTrap=NotificationType((1,3,6,1,4,1,3181,6,4,0,4))
deviceTemperatureShutdownTrap.setObjects(*((_E,_R),(_E,_AF)))
if mibBuilder.loadTexts:deviceTemperatureShutdownTrap.setStatus('')
fanAlarmTrap=NotificationType((1,3,6,1,4,1,3181,6,4,0,5))
fanAlarmTrap.setObjects(*((_E,_O),(_E,_AG)))
if mibBuilder.loadTexts:fanAlarmTrap.setStatus('')
portLocalLinkChangeTrap=NotificationType((1,3,6,1,4,1,3181,6,4,0,6))
portLocalLinkChangeTrap.setObjects(*((_E,_J),(_E,_AH)))
if mibBuilder.loadTexts:portLocalLinkChangeTrap.setStatus('')
portLineLinkChangeTrap=NotificationType((1,3,6,1,4,1,3181,6,4,0,7))
portLineLinkChangeTrap.setObjects(*((_E,_J),(_E,_AI)))
if mibBuilder.loadTexts:portLineLinkChangeTrap.setStatus('')
mibBuilder.exportSymbols(_E,**{'microsens':microsens,'cwdm':cwdm,'eightChannelCwdm':eightChannelCwdm,'minorAlarmRelayTrap':minorAlarmRelayTrap,'majorAlarmRelayTrap':majorAlarmRelayTrap,'devicePowerSupplyTrap':devicePowerSupplyTrap,'deviceTemperatureAlarmTrap':deviceTemperatureAlarmTrap,'deviceTemperatureShutdownTrap':deviceTemperatureShutdownTrap,'fanAlarmTrap':fanAlarmTrap,'portLocalLinkChangeTrap':portLocalLinkChangeTrap,'portLineLinkChangeTrap':portLineLinkChangeTrap,'deviceTable':deviceTable,'deviceTableEntry':deviceTableEntry,_T:deviceId,'deviceArtNo':deviceArtNo,'deviceSerNo':deviceSerNo,'deviceDesc':deviceDesc,_R:deviceTemperature,'deviceTempAlarmThreshold':deviceTempAlarmThreshold,_AE:deviceTempAlarm,_AF:deviceTempShutdown,'deviceTrPowerFailureAlarm':deviceTrPowerFailureAlarm,_AB:deviceMinorAlarm,_AC:deviceMajorAlarm,'portTable':portTable,'portTableEntry':portTableEntry,_J:portId,'portChannelEnabled':portChannelEnabled,'portLinkThroughLocalLine':portLinkThroughLocalLine,'portLinkThroughLineLocal':portLinkThroughLineLocal,'portLocalModuleInstalled':portLocalModuleInstalled,'portLineModuleInstalled':portLineModuleInstalled,_AH:portLocalLink,_AI:portLineLink,'portLocalTxFault':portLocalTxFault,'portLineTxFault':portLineTxFault,'portLocalPowerFault':portLocalPowerFault,'portLinePowerFault':portLinePowerFault,'portRateSelect':portRateSelect,'localModuleTable':localModuleTable,'localModuleTableEntry':localModuleTableEntry,_W:localModuleId,'localModuleConnector':localModuleConnector,'localModuleTrCodeSonet':localModuleTrCodeSonet,'localModuleTrCodeGigabit':localModuleTrCodeGigabit,'localModuleTrCodeFbLinkLength':localModuleTrCodeFbLinkLength,'localModuleTrCodeFbTrTech':localModuleTrCodeFbTrTech,'localModuleTrCodeFbTrMedia':localModuleTrCodeFbTrMedia,'localModuleTrCodeFbSpeed':localModuleTrCodeFbSpeed,'localModuleBrNominal':localModuleBrNominal,'localModuleLength9km':localModuleLength9km,'localModuleLength9m':localModuleLength9m,'localModuleLength50':localModuleLength50,'localModuleLength62':localModuleLength62,'localModuleLengthCopper':localModuleLengthCopper,'localModuleVendorSN':localModuleVendorSN,'localModuleDateCode':localModuleDateCode,'localModuleLaserCurrent':localModuleLaserCurrent,'localModuleTransmittedPower':localModuleTransmittedPower,'localModuleReceivedPower':localModuleReceivedPower,'localModuleLaserTemperature':localModuleLaserTemperature,'localModuleVoltage':localModuleVoltage,'lineModuleTable':lineModuleTable,'lineModuleTableEntry':lineModuleTableEntry,_A7:lineModuleId,'lineModuleConnector':lineModuleConnector,'lineModuleTrCodeSonet':lineModuleTrCodeSonet,'lineModuleTrCodeGigabit':lineModuleTrCodeGigabit,'lineModuleTrCodeFbLinkLength':lineModuleTrCodeFbLinkLength,'lineModuleTrCodeFbTrTech':lineModuleTrCodeFbTrTech,'lineModuleTrCodeFbTrMedia':lineModuleTrCodeFbTrMedia,'lineModuleTrCodeFbSpeed':lineModuleTrCodeFbSpeed,'lineModuleBrNominal':lineModuleBrNominal,'lineModuleLength9km':lineModuleLength9km,'lineModuleLength9m':lineModuleLength9m,'lineModuleLength50':lineModuleLength50,'lineModuleLength62':lineModuleLength62,'lineModuleLengthCopper':lineModuleLengthCopper,'lineModuleVendorSN':lineModuleVendorSN,'lineModuleDateCode':lineModuleDateCode,'lineModuleLaserCurrent':lineModuleLaserCurrent,'lineModuleTransmittedPower':lineModuleTransmittedPower,'lineModuleReceivedPower':lineModuleReceivedPower,'lineModuleLaserTemperature':lineModuleLaserTemperature,'lineModuleVoltage':lineModuleVoltage,'powerTable':powerTable,'powerTableEntry':powerTableEntry,_O:powerId,'powerArtNo':powerArtNo,'powerSerNo':powerSerNo,'powerDesc':powerDesc,'powerTemperature':powerTemperature,_AD:powerStatus,'powerSuppliedPower':powerSuppliedPower,'powerLoad':powerLoad,_AG:powerFanStatus,'lineIfTable':lineIfTable,'lineIfTableEntry':lineIfTableEntry,'lineIfId':lineIfId,'lineIfArtNo':lineIfArtNo,'lineIfSerNo':lineIfSerNo,'lineIfWestLinkStatus':lineIfWestLinkStatus,'lineIfEastLinkStatus':lineIfEastLinkStatus,'lineIfWestChannelStatus':lineIfWestChannelStatus,'lineIfEastChannelStatus':lineIfEastChannelStatus,'lineIfWestLinkRcvPower':lineIfWestLinkRcvPower,'lineIfEastLinkRcvPower':lineIfEastLinkRcvPower,'passiveTable':passiveTable,'passiveTableEntry':passiveTableEntry,_AA:passiveId,'passiveArtNo':passiveArtNo,'passiveSerNo':passiveSerNo,'channelCount':channelCount})